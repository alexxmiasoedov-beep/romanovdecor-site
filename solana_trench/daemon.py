#!/usr/bin/env python3
"""Непрерывный сбор и фильтрация кошельков.

Каждый цикл: discover пулов -> кошельки из сделок (+ GMGN) -> префильтр
новых -> полный анализ прошедших (с лимитом на цикл) -> отчёт. Состояние в
cache/state.sqlite: кошелёк не проверяется повторно раньше положенного
срока, транзакции берутся из кэша. Отчёт out/passed.json и out/wallets.csv
перестраивается после каждого цикла по последней оценке каждого кошелька.

  export SOLANA_RPC_URL='https://mainnet.helius-rpc.com/?api-key=...'
  nohup python3 daemon.py --gmgn > out/daemon.log 2>&1 &
  python3 daemon.py --once            # один цикл и выход
"""
import argparse
import csv
import json
import os
import sqlite3
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

from run import discover, collect, log
from wf.config import Config
from wf.gecko import Gecko, sol_price_history, sol_price_now, token_prices_native
from wf.gmgn import Gmgn, RANK_TAGS, gmgn_summary
from wf.history import prefilter_wallet, load_swaps, funder_of
from wf.metrics import wallet_metrics, apply_filters
from wf.rpc import Rpc


class State:
    def __init__(self, path):
        self.db = sqlite3.connect(path, timeout=30)
        self.db.execute("""CREATE TABLE IF NOT EXISTS wallets (
            wallet TEXT PRIMARY KEY, first_seen REAL, last_seen REAL, sources TEXT, pools INTEGER,
            gmgn TEXT, prefilter_reason TEXT, prefilter_at REAL, recheck_after REAL,
            analysed_at REAL, result TEXT, pass INTEGER)""")
        self.db.execute("CREATE TABLE IF NOT EXISTS budget (day TEXT PRIMARY KEY, calls INTEGER)")
        self.db.commit()

    def upsert_candidate(self, w, src, pools, gmgn, now):
        row = self.db.execute("SELECT sources, pools, gmgn FROM wallets WHERE wallet=?", (w,)).fetchone()
        if row:
            srcs = set((row[0] or "").split("+")) | set(src); srcs.discard("")
            self.db.execute("UPDATE wallets SET last_seen=?, sources=?, pools=?, gmgn=COALESCE(?, gmgn) WHERE wallet=?",
                            (now, "+".join(sorted(srcs)), max(row[1] or 0, pools), json.dumps(gmgn) if gmgn else None, w))
        else:
            self.db.execute("INSERT INTO wallets (wallet, first_seen, last_seen, sources, pools, gmgn) VALUES (?,?,?,?,?,?)",
                            (w, now, now, "+".join(sorted(src)), pools, json.dumps(gmgn) if gmgn else None))

    def due_for_prefilter(self, now):
        return [r[0] for r in self.db.execute(
            "SELECT wallet FROM wallets WHERE prefilter_at IS NULL OR (recheck_after IS NOT NULL AND recheck_after < ?) ORDER BY pools DESC, last_seen DESC", (now,))]

    def set_prefilter(self, w, reason, recheck_after, now):
        self.db.execute("UPDATE wallets SET prefilter_reason=?, prefilter_at=?, recheck_after=? WHERE wallet=?", (reason, now, recheck_after, w))

    def due_for_analysis(self, now, reanalyse_after):
        return [r[0] for r in self.db.execute(
            "SELECT wallet FROM wallets WHERE prefilter_reason='' AND (analysed_at IS NULL OR analysed_at < ?) ORDER BY analysed_at IS NOT NULL, pools DESC, last_seen DESC",
            (now - reanalyse_after,))]

    def set_result(self, w, rec, now):
        self.db.execute("UPDATE wallets SET analysed_at=?, result=?, pass=? WHERE wallet=?", (now, json.dumps(rec), int(rec["pass"]), w))

    def results(self):
        return [json.loads(r[0]) for r in self.db.execute("SELECT result FROM wallets WHERE result IS NOT NULL")]

    def counts(self):
        rows = self.db.execute("SELECT COALESCE(prefilter_reason,'<new>'), COUNT(*) FROM wallets GROUP BY 1").fetchall()
        return {k if k != "" else "<prefilter ok>": n for k, n in rows}

    def add_calls(self, n):
        day = time.strftime("%Y-%m-%d", time.gmtime())
        self.db.execute("INSERT INTO budget (day, calls) VALUES (?, ?) ON CONFLICT(day) DO UPDATE SET calls = calls + ?", (day, n, n))

    def calls_today(self):
        row = self.db.execute("SELECT calls FROM budget WHERE day=?", (time.strftime("%Y-%m-%d", time.gmtime()),)).fetchone()
        return row[0] if row else 0

    def commit(self):
        self.db.commit()


def write_report(state, cfg):
    results = state.results()
    # кластеры по источнику пополнения: из одного оставляем лучший
    by_funder = {}
    for r in results:
        r["pass"] = not r["fail_reasons"]
        if r.get("funder"):
            by_funder.setdefault(r["funder"], []).append(r)
    for rs in by_funder.values():
        if len(rs) > 1:
            best = max(rs, key=lambda r: r.get("copy_pnl_sol") or -1e9)
            for r in rs:
                r["cluster_size"] = len(rs)
                if r is not best and r["pass"]:
                    r["pass"] = False; r["fail_reasons"] = "same_funder_cluster"
    results.sort(key=lambda r: (not r["pass"], -(r.get("copy_pnl_sol") or -1e9)))
    keys = []
    for r in results:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(os.path.join(cfg.out_dir, "wallets.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in results:
            wr.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
    passed = [r for r in results if r["pass"]]
    json.dump({"config": cfg.to_dict(), "generated": time.time(), "analysed": len(results),
               "prefilter_counts": state.counts(), "passed": passed},
              open(os.path.join(cfg.out_dir, "passed.json"), "w"), indent=1, ensure_ascii=False)
    return results, passed


def cycle(cfg, state, rpc, gecko, gm, args, now):
    # 1-2. кандидаты
    pools = discover(gecko, cfg, now)
    json.dump(pools, open(os.path.join(cfg.out_dir, "pools.json"), "w"), indent=1, ensure_ascii=False)
    for w, v in collect(gecko, pools, cfg.min_trade_usd).items():
        state.upsert_candidate(w, {"onchain"}, len(v["pools"]), None, now)
    if gm and gm.available:
        n = 0
        for tag in RANK_TAGS:
            for r in gm.top_wallets("7d", tag=tag):
                state.upsert_candidate(r["wallet"], {"gmgn_rank"}, 0, r["gmgn"], now); n += 1
        for p in pools:
            for r in gm.token_traders(p["mint"]):
                state.upsert_candidate(r["wallet"], {"gmgn_top_traders"}, 1, None, now); n += 1
        log(f"GMGN: {n} записей кандидатов")
    state.commit()

    # 3. префильтр новых
    due = state.due_for_prefilter(now)[: args.max_prefilter]
    log(f"prefilter: {len(due)} кошельков к проверке")
    calls0 = rpc.calls
    sig_cache = {}

    def pre(w):
        try:
            return w, prefilter_wallet(rpc, w, cfg, now)
        except RuntimeError as e:
            return w, ({"wallet": w}, "rpc_error")

    dropped = {}
    with ThreadPoolExecutor(cfg.rpc_threads) as ex:
        for w, (info, reason) in ex.map(pre, due):
            if reason == "wallet_too_young":
                recheck = now + max(1, cfg.min_wallet_age_days - info.get("age_days", 0)) * 86400
            elif reason in ("too_few_tx", "no_tx", "rpc_error"):
                recheck = now + 3 * 86400
            elif reason:
                recheck = now + 14 * 86400
            else:
                recheck = None
                sig_cache[w] = info
            state.set_prefilter(w, reason or "", recheck, now)
            dropped[reason or "ok"] = dropped.get(reason or "ok", 0) + 1
    state.commit()
    state.add_calls(rpc.calls - calls0); state.commit()
    log(f"prefilter done: {dropped} (rpc calls {rpc.calls - calls0})")

    # 4-6. анализ
    if state.calls_today() > args.daily_budget:
        log(f"дневной бюджет RPC исчерпан ({state.calls_today()}), анализ отложен")
        return
    todo = state.due_for_analysis(now, args.reanalyse_hours * 3600)[: args.max_analyse]
    log(f"analyse: {len(todo)} кошельков")
    sol_hist = sol_price_history(cfg.history_days + 1)
    sol_now = sol_price_now() or (list(sol_hist.values())[-1] if sol_hist else None)
    for k, w in enumerate(todo):
        t0 = time.time(); c0 = rpc.calls
        info = sig_cache.get(w)
        if info is None:
            try:
                info, reason = prefilter_wallet(rpc, w, cfg, now)
            except RuntimeError:
                info, reason = None, "rpc_error"
            if reason:
                state.set_prefilter(w, reason, now + 3 * 86400, now); state.commit()
                continue
        swaps = load_swaps(rpc, w, info["sigs"], cfg)
        mints = list({s["mint"] for s in swaps})
        token_prices = token_prices_native(mints) if mints else {}
        m, rows = wallet_metrics(swaps, cfg, sol_hist, sol_now, token_prices, now)
        reasons = apply_filters(m, cfg)
        funder = funder_of(rpc, info) if not reasons else None
        row = state.db.execute("SELECT sources, pools, gmgn FROM wallets WHERE wallet=?", (w,)).fetchone()
        gm_row = json.loads(row[2]) if row and row[2] else None
        rec = {"wallet": w, "analysed_at": now, "age_days": info.get("age_days"), "tx_in_window": info["tx_in_window"],
               "failed_share": round(info.get("failed_share", 0), 3), "funder": funder,
               "seen_in_pools": row[1] if row else 0, "source": row[0] if row else "", **m,
               **gmgn_summary(gm_row), "pass": not reasons, "fail_reasons": ";".join(reasons)}
        state.set_result(w, rec, now)
        json.dump(rows, open(os.path.join(cfg.out_dir, f"positions_{w}.json"), "w"), indent=1)
        state.add_calls(rpc.calls - c0); state.commit()
        log(f"[{k+1}/{len(todo)}] {w[:8]} swaps={len(swaps)} closed={m['n_closed']} "
            f"copy_pnl={m['copy_pnl_sol'] is not None and round(m['copy_pnl_sol'], 3)} "
            f"{'PASS' if not reasons else reasons} ({time.time()-t0:.0f}s, calls {rpc.calls - c0})")
        if state.calls_today() > args.daily_budget:
            log("дневной бюджет RPC исчерпан, остаток анализа — в следующем цикле")
            break
    results, passed = write_report(state, cfg)
    log(f"report: analysed={len(results)} PASSED={len(passed)} | {[r['wallet'][:8] for r in passed]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--gmgn", action="store_true")
    ap.add_argument("--cycle-minutes", type=float, default=30)
    ap.add_argument("--max-prefilter", type=int, default=3000, help="кошельков в префильтр за цикл")
    ap.add_argument("--max-analyse", type=int, default=40, help="кошельков в полный анализ за цикл")
    ap.add_argument("--reanalyse-hours", type=float, default=24)
    ap.add_argument("--daily-budget", type=int, default=300_000, help="лимит RPC-вызовов в сутки")
    ap.add_argument("--max-tx", type=int)
    ap.add_argument("--pool-age-hours", type=float, default=72)
    ap.add_argument("--min-trade-usd", type=float, default=100)
    ap.add_argument("--max-pools", type=int, default=40)
    a = ap.parse_args()

    cfg = Config()
    cfg.pool_age_hours = a.pool_age_hours; cfg.min_trade_usd = a.min_trade_usd; cfg.max_pools = a.max_pools
    if a.max_tx: cfg.max_tx_per_wallet = a.max_tx
    if not cfg.rpc_url:
        sys.exit("Нужен архивный RPC: export SOLANA_RPC_URL='https://mainnet.helius-rpc.com/?api-key=...'")
    os.makedirs(cfg.out_dir, exist_ok=True); os.makedirs(cfg.cache_dir, exist_ok=True)
    state = State(os.path.join(cfg.cache_dir, "state.sqlite"))
    rpc = Rpc(cfg.rpc_url, cfg.fast_rpc_url, cfg.rpc_rps, cfg.fast_rpc_rps, cfg.cache_dir, cfg.fast_hours)
    gecko = Gecko(cfg.gecko_delay_sec)
    gm = None
    if a.gmgn:
        gm = Gmgn()
        log("GMGN доступен" if gm.check() else "GMGN недоступен отсюда — только on-chain")
    while True:
        t0 = time.time()
        try:
            cycle(cfg, state, rpc, gecko, gm, a, time.time())
        except Exception:
            log("cycle failed:\n" + traceback.format_exc())
        if a.once:
            break
        wait = max(60, a.cycle_minutes * 60 - (time.time() - t0))
        log(f"sleep {wait/60:.0f} min")
        time.sleep(wait)


if __name__ == "__main__":
    main()
