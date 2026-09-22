"""Бумажная симуляция копирования: $1 на каждую новую позицию кошелька, старт $100.

  python3 sim.py start --batch 1 --wallets 0x.. 0x.. [--tag top5] [--since-hours 0]
  python3 sim.py update            # подтянуть новые сделки, резолвы, переоценку
  python3 sim.py report            # таблица → data/db/SIM_REPORT.md
  python3 sim.py review --batch 1  # разметить positive/negative по итогу батча

Правила копии (см. СТРАТЕГИЯ.md, раздел 5): вход по цене через 30 с (лента сделок рынка,
запасной вариант — поминутная история) с проскальзыванием 1 %; пропуск, если цена ушла
больше чем на 3 цента или ≥ 0,90; выходы — пропорционально продажам кошелька; резолв — 1/0.
Состояние: data/db/sim.json (перезапускаемо, сделки не обрабатываются дважды).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

from pm import api, config, markets, metrics, registry

PATH = os.environ.get("SIM_PATH", os.path.join(os.path.dirname(__file__), "data", "db", "sim.json"))
REPORT = os.path.join(os.path.dirname(PATH), "SIM_REPORT.md")
STAKE = 1.0
START_BALANCE = 100.0
EPS = 1e-9


def load() -> dict:
    if os.path.exists(PATH):
        with open(PATH) as f:
            return json.load(f)
    return {"batches": {}, "wallets": {}}


def save(s: dict) -> None:
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    tmp = PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(s, f, ensure_ascii=False)
    os.replace(tmp, PATH)


def parse_segments(text: str) -> set[str]:
    return {p.split(" (n=")[0].strip() for p in (text or "").split(" | ") if p.strip()}


def fill_price(cid: str, asset: str, ts: float, his_price: float) -> tuple[float, str]:
    """Цена входа копировщика через 30 с: лента сделок рынка → поминутная история → его цена."""
    tape = api.trades_market(cid, max_pages=config.TAPE_PAGES, cache=False)
    target = ts + 30
    best = None
    for t in tape:
        tt = float(t.get("timestamp") or 0)
        if target <= tt <= target + 1800 and (best is None or tt < best[0]):
            p = float(t.get("price") or 0)
            if t.get("asset") != asset:
                p = 1 - p
            best = (tt, p)
    if best and tape and min(float(t.get("timestamp") or 0) for t in tape) <= target:
        return best[1], "tape"
    hist = api.prices_history(asset, int(ts) - 60, int(ts) + 600, fidelity=1)
    pts = sorted((h for h in hist if h["t"] <= ts + 60), key=lambda h: h["t"])
    if pts:
        return pts[-1]["p"], "history"
    return his_price, "own"


def cmd_start(a) -> None:
    s = load()
    db = registry.load()
    start_ts = time.time() - a.since_hours * 3600
    batch = str(a.batch)
    s["batches"].setdefault(batch, {"start_ts": start_ts, "wallets": [], "stake": STAKE, "balance": START_BALANCE})
    for w in a.wallets:
        w = w.lower()
        if w in s["wallets"]:
            print(f"{w}: уже в симуляции (батч {s['wallets'][w]['batch']})", file=sys.stderr)
            continue
        rec = registry.get(db, w)
        rec.update({"status": "simulating", "batch": batch, "sim_start": start_ts})
        if a.tag and a.tag not in rec["tags"]:
            rec["tags"].append(a.tag)
        s["wallets"][w] = {"batch": batch, "start_ts": start_ts, "name": rec.get("name", ""),
                           "segments": sorted(parse_segments(rec.get("approved_segments", ""))),
                           "cash": START_BALANCE, "realized": 0.0, "positions": {}, "closed": [],
                           "skipped": [], "processed": [], "his_qty": {}, "history": []}
        s["batches"][batch]["wallets"].append(w)
    registry.save(db)
    save(s)
    print(f"батч {batch}: {len(s['batches'][batch]['wallets'])} кошельков, старт "
          f"{datetime.fromtimestamp(start_ts, timezone.utc):%Y-%m-%d %H:%M} UTC", file=sys.stderr)


def in_segment(cid: str, entry: float, live: bool, segments: set[str]) -> bool:
    if not segments:
        return True
    from stage2_analyze import seg_keys
    m = markets.ensure([cid]).get(cid, {})
    keys = seg_keys({"cls": markets.classify(m), "entry": entry, "live": live}).values()
    return bool(set(keys) & segments)


def update_wallet(w: str, st: dict, now: float) -> None:
    trades = api.trades_user(w, ttl=60)
    processed = set(st["processed"])
    new = [t for t in trades if float(t.get("timestamp") or 0) >= st["start_ts"]
           and (t.get("transactionHash", "") + t.get("asset", "")) not in processed]
    new.sort(key=lambda t: (float(t.get("timestamp") or 0), t.get("side") != "BUY"))
    segs = set(st["segments"])
    for t in new:
        key = t.get("transactionHash", "") + t.get("asset", "")
        st["processed"].append(key)
        asset, cid = t.get("asset"), t.get("conditionId")
        ts, price, size = float(t.get("timestamp") or 0), float(t.get("price") or 0), float(t.get("size") or 0)
        if not asset or price <= 0 or size <= 0:
            continue
        pos = st["positions"].get(asset)
        if t.get("side") == "BUY":
            st["his_qty"][asset] = st["his_qty"].get(asset, 0.0) + size
            if pos:
                continue  # докупка кошелька: у нас фикс $1 на позицию, не добавляем
            fill, src = fill_price(cid, asset, ts, price)
            reason = None
            if fill > price + config.MAX_PRICE_DRIFT:
                reason = "drift"
            elif fill >= config.MAX_ENTRY_PRICE:
                reason = "price>=0.90"
            elif st["cash"] < STAKE:
                reason = "no_cash"
            if reason:
                st["skipped"].append({"ts": ts, "title": t.get("title"), "his": price, "fill": fill, "why": reason})
                continue
            eff = fill * (1 + config.ASSUMED_SLIPPAGE_REL)
            m = markets.ensure([cid]).get(cid, {})
            live = bool(m.get("gameStartTime") and ts > m["gameStartTime"])
            st["cash"] -= STAKE
            st["positions"][asset] = {"cid": cid, "asset": asset, "title": t.get("title"), "outcome": t.get("outcome"),
                                      "opened": ts, "his_entry": price, "fill": eff, "fill_src": src,
                                      "shares": STAKE / eff, "shares0": STAKE / eff, "cost": STAKE, "proceeds": 0.0,
                                      "in_segment": in_segment(cid, price, live, segs)}
        else:
            hq = st["his_qty"].get(asset, 0.0)
            if hq > EPS:
                frac = min(size / hq, 1.0)
                st["his_qty"][asset] = max(hq - size, 0.0)
            else:
                frac = 0.0
            if pos and frac > 0:
                sell = pos["shares"] * frac
                got = sell * price * (1 - config.ASSUMED_SLIPPAGE_REL)
                pos["shares"] -= sell
                pos["proceeds"] += got
                st["cash"] += got
                if pos["shares"] <= 1e-6:
                    _close(st, asset, pos, "sell", ts)
    # резолвы и переоценка
    cids = [p["cid"] for p in st["positions"].values()]
    mk = markets.ensure(cids, refresh_open_after=1800)
    for asset, pos in list(st["positions"].items()):
        m = mk.get(pos["cid"], {})
        if m.get("closed") and asset in (m.get("tokens") or []):
            res = (m.get("outcomePrices") or [None] * len(m["tokens"]))[m["tokens"].index(asset)]
            if res in (0.0, 1.0):
                st["cash"] += pos["shares"] * res
                pos["proceeds"] += pos["shares"] * res
                pos["res"] = res
                _close(st, asset, pos, "resolve", m.get("closedTime") or now)
                continue
        cur = None
        if asset in (m.get("tokens") or []):
            cur = (m.get("outcomePrices") or [None] * len(m["tokens"]))[m["tokens"].index(asset)]
        pos["mark"] = cur if cur is not None else pos["fill"]
    open_val = sum(p["shares"] * p["mark"] for p in st["positions"].values())
    seg_pnl = sum(c["pnl"] for c in st["closed"] if c["in_segment"]) + \
        sum(p["shares"] * p["mark"] - p["cost"] + p["proceeds"] for p in st["positions"].values() if p["in_segment"])
    st["history"].append({"ts": now, "equity": round(st["cash"] + open_val, 4), "open": len(st["positions"]),
                          "seg_pnl": round(seg_pnl, 4)})


def _close(st: dict, asset: str, pos: dict, how: str, ts: float) -> None:
    pos["closed"] = ts
    pos["how"] = how
    pos["pnl"] = pos["proceeds"] - pos["cost"]
    st["realized"] += pos["pnl"]
    st["closed"].append(pos)
    del st["positions"][asset]
    st["his_qty"].pop(asset, None)


def cmd_update(a) -> None:
    s = load()
    now = time.time()
    ws = [w for w, st in s["wallets"].items() if not a.batch or st["batch"] == str(a.batch)]
    for i, w in enumerate(ws):
        try:
            update_wallet(w, s["wallets"][w], now)
        except Exception as e:  # noqa: BLE001
            print(f"{w}: {e}", file=sys.stderr)
        print(f"\r[sim] {i + 1}/{len(ws)}", end="", file=sys.stderr, flush=True)
        if i % 5 == 4:
            save(s)
    print(file=sys.stderr)
    markets.save()
    save(s)
    cmd_report(a)


def wallet_row(w: str, st: dict) -> dict:
    h = st["history"][-1] if st["history"] else {"equity": START_BALANCE, "open": 0, "seg_pnl": 0.0}
    days = (time.time() - st["start_ts"]) / 86400
    closed = st["closed"]
    return {"wallet": w, "name": st.get("name", ""), "batch": st["batch"], "days": round(days, 1),
            "copied": len(closed) + len(st["positions"]), "closed": len(closed), "open": len(st["positions"]),
            "skipped": len(st["skipped"]), "winrate": round(metrics.mean(1.0 if c["pnl"] > 0 else 0.0 for c in closed), 2) if closed else "",
            "realized": round(st["realized"], 2), "equity": h["equity"], "pnl": round(h["equity"] - START_BALANCE, 2),
            "pnl_segment": round(h["seg_pnl"], 2), "segments": " | ".join(st["segments"]) or "все рынки"}


def cmd_report(a) -> None:
    s = load()
    rows = [wallet_row(w, st) for w, st in s["wallets"].items()]
    rows.sort(key=lambda r: (r["batch"], -r["pnl"]))
    out = [f"# Симуляция копирования, {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
           f"Ставка ${STAKE:g} на позицию, старт ${START_BALANCE:g} на кошелёк. PnL в долларах.\n",
           "| Батч | Кошелёк | Имя | Дней | Скопировано | Закрыто | Открыто | Пропущено | Винрейт | Реализовано | Капитал | PnL | PnL в сегментах |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['batch']} | `{r['wallet']}` | {r['name']} | {r['days']} | {r['copied']} | {r['closed']} | {r['open']} | "
                   f"{r['skipped']} | {r['winrate']} | {r['realized']} | {r['equity']} | **{r['pnl']:+.2f}** | {r['pnl_segment']:+.2f} |")
    for b, info in s["batches"].items():
        rs = [r for r in rows if r["batch"] == b]
        if rs:
            out.append(f"\nБатч {b}: старт {datetime.fromtimestamp(info['start_ts'], timezone.utc):%Y-%m-%d %H:%M} UTC, "
                       f"кошельков {len(rs)}, суммарный PnL {sum(r['pnl'] for r in rs):+.2f} $, в плюсе {sum(1 for r in rs if r['pnl'] > 0)}.")
    with open(REPORT, "w") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out), file=sys.stderr)


def cmd_review(a) -> None:
    s = load()
    db = registry.load()
    pos, neg = [], []
    for w, st in s["wallets"].items():
        if st["batch"] != str(a.batch):
            continue
        r = wallet_row(w, st)
        rec = registry.get(db, w)
        if r["pnl"] > 0 and r["closed"] >= a.min_closed:
            rec["status"] = "positive"
            pos.append(r)
        else:
            rec["status"] = "negative"
            neg.append(r)
    registry.save(db)
    positive_path = os.path.join(os.path.dirname(PATH), "positive.json")
    prev = json.load(open(positive_path)) if os.path.exists(positive_path) else {}
    for r in pos:
        prev[r["wallet"]] = {"name": r["name"], "batch": r["batch"], "pnl": r["pnl"], "closed": r["closed"],
                             "reviewed": datetime.now(timezone.utc).strftime("%Y-%m-%d")}
    with open(positive_path, "w") as f:
        json.dump(prev, f, ensure_ascii=False, indent=1)
    print(f"батч {a.batch}: в плюсе {len(pos)}, в минусе {len(neg)}; список положительных: {positive_path}", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("start"); p.add_argument("--batch", required=True); p.add_argument("--wallets", nargs="+", required=True)
    p.add_argument("--tag", default=""); p.add_argument("--since-hours", type=float, default=0.0)
    p = sub.add_parser("update"); p.add_argument("--batch", default=None)
    sub.add_parser("report")
    p = sub.add_parser("review"); p.add_argument("--batch", required=True); p.add_argument("--min-closed", type=int, default=5)
    a = ap.parse_args()
    {"start": cmd_start, "update": cmd_update, "report": cmd_report, "review": cmd_review}[a.cmd](a)


if __name__ == "__main__":
    main()
