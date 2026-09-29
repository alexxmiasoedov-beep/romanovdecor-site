#!/usr/bin/env python3
"""Поэтапный отбор кошельков (вариант владельца от 28.09.2026).

  1. Стиль: первая покупка токена ПОСЛЕ миграции и при капе < 300k.
     Требуем долю таких первых покупок >= --style-share (0.7) среди позиций,
     где капа известна (резервы пула разобраны).
  2. Кошелёк существует >= 10 дней.
  3. Два списка по числу ТОКЕНОВ, которыми торгует кошелёк, в день
     (разные токены с покупкой за окно 20 дней / 20):
     A: 10-50 токенов/день, B: 50-300 токенов/день.
  4. PnL за последние 20 дней > 0: реализованный по закрытым позициям +
     нереализованный по открытым по текущей цене DexScreener.

Дешёвые этапы (возраст, частота по подписям) идут первыми, полная история
грузится только для прошедших. Состояние — cache/stages.sqlite, отчёт —
out/list_A_10_50.csv, out/list_B_50_300.csv, out/stages.json.

  export SOLANA_RPC_URL='https://mainnet.helius-rpc.com/?api-key=...'
  nohup python3 stages.py --loop > out/stages.log 2>&1 &
"""
import argparse
import csv
import json
import os
import sqlite3
import statistics as st
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

from run import discover, collect, log
from wf.config import Config, PUMP_SUPPLY
from wf.gecko import Gecko, sol_price_history, sol_price_now, token_prices_native
from wf.gmgn import Gmgn, RANK_TAGS
from wf.history import load_swaps
from wf.metrics import wallet_metrics
from wf.positions import build_positions
from wf.rpc import Rpc

WINDOW_DAYS = 20
MIN_AGE_DAYS = 10
MC_MAX_USD = 300_000
BUCKETS = {"A": (10, 50), "B": (50, 300)}


class Store:
    def __init__(self, path):
        self.db = sqlite3.connect(path, timeout=30)
        self.db.execute("""CREATE TABLE IF NOT EXISTS w (
            wallet TEXT PRIMARY KEY, first_seen REAL, last_seen REAL, src TEXT,
            stage TEXT, reason TEXT, checked_at REAL, recheck_after REAL, info TEXT, result TEXT)""")
        self.db.commit()

    def add(self, w, src, now):
        self.db.execute("INSERT INTO w (wallet, first_seen, last_seen, src) VALUES (?,?,?,?) "
                        "ON CONFLICT(wallet) DO UPDATE SET last_seen=excluded.last_seen", (w, now, now, src))

    def todo(self, stage, now, limit):
        if stage == "cheap":
            q = "SELECT wallet FROM w WHERE stage IS NULL OR (recheck_after IS NOT NULL AND recheck_after < ?) ORDER BY last_seen DESC LIMIT ?"
            return [r[0] for r in self.db.execute(q, (now, limit))]
        # сначала зона списка A (800–3000 tx за 20 дней), потом остальные по возрастанию
        q = ("SELECT wallet, info FROM w WHERE stage='cheap_ok' ORDER BY "
             "CASE WHEN json_extract(info,'$.tx_in_window') BETWEEN 800 AND 3000 THEN 0 ELSE 1 END, "
             "json_extract(info,'$.tx_in_window') ASC LIMIT ?")
        return [(r[0], json.loads(r[1])) for r in self.db.execute(q, (limit,))]

    def set(self, w, stage, reason, now, info=None, result=None, recheck_after=None):
        self.db.execute("UPDATE w SET stage=?, reason=?, checked_at=?, recheck_after=?, info=COALESCE(?, info), result=COALESCE(?, result) WHERE wallet=?",
                        (stage, reason or "", now, recheck_after, json.dumps(info) if info else None, json.dumps(result) if result else None, w))

    def results(self):
        return [json.loads(r[0]) for r in self.db.execute("SELECT result FROM w WHERE result IS NOT NULL AND stage LIKE 'full_%'")]

    def counts(self):
        return {f"{s}:{r}" if r else s: n for s, r, n in self.db.execute("SELECT COALESCE(stage,'<new>'), COALESCE(reason,''), COUNT(*) FROM w GROUP BY 1,2")}


def cheap_stage(rpc, wallet, now):
    """Возраст >= 10 дней и грубая частота по подписям (без загрузки tx).
    -> (info, reason)"""
    min_time = now - WINDOW_DAYS * 86400
    info = {"wallet": wallet}
    first = rpc.signatures(wallet)
    if not first:
        return info, "no_tx"
    if len(first) >= 1000:
        span = ((first[0].get("blockTime") or now) - (first[-1].get("blockTime") or now)) / 86400
        if span < 1000 / 900:                      # > 900 tx/день: даже при 300 покупках столько не бывает
            info["tx_in_window"] = 1000; info["span_days"] = round(span, 2)
            return info, "too_many_tx"
    sigs = [s for s in first if (s.get("blockTime") or 0) >= min_time]
    exhausted = len(first) < 1000
    older_seen = len(sigs) < len(first)
    before = first[-1]["signature"]
    pages = 1
    while not exhausted and not older_seen and pages < 20:
        page = rpc.signatures(wallet, before=before); pages += 1
        if not page:
            exhausted = True; break
        keep = [s for s in page if (s.get("blockTime") or 0) >= min_time]
        sigs.extend(keep)
        older_seen = len(keep) < len(page)
        exhausted = len(page) < 1000
        before = page[-1]["signature"]
    ok = [s for s in sigs if not s.get("err")]
    info["tx_in_window"] = len(ok)
    info["failed_share"] = round(1 - len(ok) / len(sigs), 3) if sigs else 0
    info["sigs"] = ok
    if older_seen:
        info["age_days"] = WINDOW_DAYS + 1
    elif exhausted:
        info["age_days"] = round((now - (sigs[-1].get("blockTime") or now)) / 86400, 1) if sigs else 0
    else:
        return info, "too_many_tx"
    if info["age_days"] < MIN_AGE_DAYS:
        return info, "too_young"
    per_day = len(ok) / WINDOW_DAYS
    if per_day < 28:                               # 10 покупок/день = минимум ~28 tx/день (покупки + продажи + прочее)
        return info, "too_few_tx"
    if per_day > 900:
        return info, "too_many_tx"
    return info, None


def full_stage(rpc, wallet, info, cfg, sol_hist, sol_now, now):
    # проба: 60 свежих tx — если среди них почти нет свопов, это не трейдер
    sample = load_swaps(rpc, wallet, info["sigs"][:60], cfg)
    if len(sample) < 5:
        return None, "no_swaps_in_sample"
    swaps = load_swaps(rpc, wallet, info["sigs"], cfg)
    swaps = [s for s in swaps if s["sol"] >= cfg.min_swap_sol]
    if not swaps:
        return None, "no_swaps"
    # частота — за всё окно 20 дней; только если история обрезана капом max_tx,
    # считаем по реально покрытому отрезку
    truncated = len(info["sigs"]) > cfg.max_tx_per_wallet
    days_covered = max(1e-9, (now - min(s["time"] for s in swaps)) / 86400) if truncated else WINDOW_DAYS
    buys = [s for s in swaps if s["side"] == "buy"]
    buys_per_day = len(buys) / days_covered
    tokens_traded = len({s["mint"] for s in buys})
    tokens_per_day = tokens_traded / days_covered

    positions = build_positions(swaps)
    style_known = style_ok = 0
    for p in positions:
        f = p["trades"][0]
        if f["pre_migration"]:
            style_known += 1; continue
        if f.get("sol_res") and f.get("tok_res"):
            day = (f["time"] or now) // 86400 * 86400
            sol_usd = (sol_hist or {}).get(day) or sol_now or 0
            mc = f["sol_res"] / f["tok_res"] * PUMP_SUPPLY * sol_usd
            style_known += 1
            if mc < MC_MAX_USD:
                style_ok += 1
    style_share = style_ok / style_known if style_known else None

    mints = list({p["mint"] for p in positions if p["held"] > 1e-9})
    prices = token_prices_native(mints) if mints else {}
    realized = unrealized = 0.0
    wins = n_closed = 0
    holds = []
    for p in positions:
        sol_in = sum(t["sol"] for t in p["trades"] if t["side"] == "buy")
        sol_out = sum(t["sol"] for t in p["trades"] if t["side"] == "sell")
        if p.get("closed"):
            realized += sol_out - sol_in; n_closed += 1; wins += sol_out > sol_in
            sells = [t for t in p["trades"] if t["side"] == "sell"]
            holds.append(sells[-1]["time"] - p["trades"][0]["time"])
        else:
            realized += sol_out - sol_in
            unrealized += p["held"] * prices.get(p["mint"], 0.0)
    pnl = realized + unrealized

    m, _ = wallet_metrics(swaps, cfg, sol_hist, sol_now, prices, now)   # справочно: копия старым способом
    res = {
        "wallet": wallet, "age_days": info["age_days"], "days_covered": round(days_covered, 1),
        "tx_in_window": info["tx_in_window"], "swaps": len(swaps), "buys": len(buys),
        "tokens_traded": tokens_traded, "tokens_per_day": round(tokens_per_day, 1),
        "buys_per_day": round(buys_per_day, 1), "positions": len(positions), "closed": n_closed,
        "style_share": None if style_share is None else round(style_share, 2), "style_known": style_known,
        "post_migration_share": m.get("post_migration_share"),
        "pnl_20d_sol": round(pnl, 3), "realized_sol": round(realized, 3), "unrealized_sol": round(unrealized, 3),
        "win_rate": round(wins / n_closed, 2) if n_closed else None,
        "median_hold_sec": round(st.median(holds)) if holds else None,
        "median_entry_mc_usd": m.get("median_entry_mc_usd") and round(m["median_entry_mc_usd"]),
        "median_entry_sol": m.get("median_entry_sol") and round(m["median_entry_sol"], 3),
        "avg_buys_per_position": m.get("avg_buys_per_position") and round(m["avg_buys_per_position"], 2),
        "copy_pnl_sol_ref": m.get("copy_pnl_sol") and round(m["copy_pnl_sol"], 3),
        "copy_median_ret_ref": m.get("copy_median_ret") and round(m["copy_median_ret"], 3),
    }
    reasons = []
    if style_share is None or style_share < STYLE_SHARE:
        reasons.append("style")
    bucket = next((b for b, (lo, hi) in BUCKETS.items() if lo <= tokens_per_day < hi or (b == "B" and tokens_per_day == hi)), None)
    if bucket is None:
        reasons.append("tokens_per_day")
    if pnl <= 0:
        reasons.append("pnl_negative")
    res["bucket"] = bucket
    res["fail"] = ";".join(reasons)
    return res, (";".join(reasons) or None)


STYLE_SHARE = 0.7


def write_report(store, cfg):
    results = store.results()
    results.sort(key=lambda r: -(r.get("pnl_20d_sol") or -1e9))
    lists = {"A": [], "B": []}
    for r in results:
        if not r["fail"] and r["bucket"] in lists:
            lists[r["bucket"]].append(r)
    keys = list(results[0].keys()) if results else ["wallet"]
    for name, fn in (("A", "list_A_10_50.csv"), ("B", "list_B_50_300.csv")):
        with open(os.path.join(cfg.out_dir, fn), "w", newline="") as f:
            wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
            for r in lists[name]:
                wr.writerow(r)
    with open(os.path.join(cfg.out_dir, "stages_all.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in results:
            wr.writerow(r)
    json.dump({"generated": time.time(), "counts": store.counts(), "analysed": len(results),
               "list_A": lists["A"], "list_B": lists["B"]},
              open(os.path.join(cfg.out_dir, "stages.json"), "w"), indent=1, ensure_ascii=False)
    return results, lists


def cycle(a, cfg, store, rpc, gecko, gm, now):
    # кандидаты: старое состояние + свежие пулы + GMGN
    if a.import_state and os.path.exists(a.import_state):
        s = sqlite3.connect(a.import_state)
        for (w, src) in s.execute("SELECT wallet, sources FROM wallets"):
            store.add(w, src or "onchain", now)
        s.close()
    pools = discover(gecko, cfg, now)
    for w, v in collect(gecko, pools, cfg.min_trade_usd).items():
        store.add(w, "onchain", now)
    if gm and gm.available:
        for tag in RANK_TAGS:
            for r in gm.top_wallets("7d", tag=tag):
                store.add(r["wallet"], "gmgn_rank", now)
        for p in pools:
            for r in gm.token_traders(p["mint"]):
                store.add(r["wallet"], "gmgn_top_traders", now)
    store.db.commit()

    # дешёвый этап
    todo = store.todo("cheap", now, a.max_cheap)
    log(f"cheap stage: {len(todo)} кошельков")
    stats = {}

    def one(w):
        try:
            return w, cheap_stage(rpc, w, now)
        except RuntimeError:
            return w, ({"wallet": w}, "rpc_error")

    with ThreadPoolExecutor(cfg.rpc_threads) as ex:
        for w, (info, reason) in ex.map(one, todo):
            stats[reason or "ok"] = stats.get(reason or "ok", 0) + 1
            if reason:
                recheck = now + (max(1, MIN_AGE_DAYS - info.get("age_days", 0)) * 86400 if reason == "too_young" else 3 * 86400)
                store.set(w, "cheap_fail", reason, now, recheck_after=recheck)
            else:
                info_small = {k: v for k, v in info.items() if k != "sigs"}
                store.set(w, "cheap_ok", None, now, info=info_small)
    store.db.commit()
    log(f"cheap stage done: {stats}")

    # полный этап: сначала самые дешёвые (меньше tx)
    sol_hist = sol_price_history(WINDOW_DAYS + 1)
    sol_now = sol_price_now() or (list(sol_hist.values())[-1] if sol_hist else None)
    todo = store.todo("full", now, a.max_full)
    log(f"full stage: {len(todo)} кошельков")
    for k, (w, info_small) in enumerate(todo):
        t0 = time.time(); c0 = rpc.calls
        try:
            info, reason = cheap_stage(rpc, w, now)      # заново подписи (в info_small их нет)
            if reason:
                store.set(w, "cheap_fail", reason, now, recheck_after=now + 3 * 86400); store.db.commit(); continue
            res, fail = full_stage(rpc, w, info, cfg, sol_hist, sol_now, now)
        except Exception:
            log("full stage failed for " + w + "\n" + traceback.format_exc())
            store.set(w, "full_error", "exception", now, recheck_after=now + 86400); store.db.commit(); continue
        store.set(w, "full_ok" if not fail else "full_fail", fail, now, result=res)
        store.db.commit()
        if res:
            log(f"[{k+1}/{len(todo)}] {w[:8]} tx={res['tx_in_window']} tokens/day={res['tokens_per_day']} buys/day={res['buys_per_day']} style={res['style_share']} "
                f"pnl20={res['pnl_20d_sol']} -> {('LIST ' + res['bucket']) if not fail else fail} ({time.time()-t0:.0f}s, calls {rpc.calls-c0})")
    results, lists = write_report(store, cfg)
    log(f"report: analysed={len(results)} list A={len(lists['A'])} list B={len(lists['B'])}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--loop", action="store_true")
    ap.add_argument("--gmgn", action="store_true")
    ap.add_argument("--import-state", default="cache/state.sqlite", help="взять кандидатов из состояния демона")
    ap.add_argument("--max-cheap", type=int, default=4000)
    ap.add_argument("--max-full", type=int, default=60)
    ap.add_argument("--max-tx", type=int, default=4000)
    ap.add_argument("--style-share", type=float, default=0.7)
    ap.add_argument("--cycle-minutes", type=float, default=20)
    a = ap.parse_args()
    global STYLE_SHARE
    STYLE_SHARE = a.style_share

    cfg = Config()
    cfg.history_days = WINDOW_DAYS
    cfg.max_tx_per_wallet = a.max_tx
    cfg.pool_age_hours = 72; cfg.min_trade_usd = 100; cfg.max_pools = 40
    if not cfg.rpc_url:
        sys.exit("Нужен архивный RPC: export SOLANA_RPC_URL=...")
    os.makedirs(cfg.out_dir, exist_ok=True); os.makedirs(cfg.cache_dir, exist_ok=True)
    store = Store(os.path.join(cfg.cache_dir, "stages.sqlite"))
    rpc = Rpc(cfg.rpc_url, cfg.fast_rpc_url, cfg.rpc_rps, cfg.fast_rpc_rps, cfg.cache_dir, cfg.fast_hours)
    gecko = Gecko(cfg.gecko_delay_sec)
    gm = None
    if a.gmgn:
        gm = Gmgn(); log("GMGN доступен" if gm.check() else "GMGN недоступен")
    while True:
        t0 = time.time()
        try:
            cycle(a, cfg, store, rpc, gecko, gm, time.time())
        except Exception:
            log("cycle failed:\n" + traceback.format_exc())
        if not a.loop:
            break
        wait = max(60, a.cycle_minutes * 60 - (time.time() - t0))
        log(f"sleep {wait/60:.0f} min"); time.sleep(wait)


if __name__ == "__main__":
    main()
