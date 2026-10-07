"""Форвард-тест стратегий по кошелькам (гипотеза владельца, 07.10). ПОЛНОСТЬЮ ОТДЕЛЬНО от sim.py и реестра:
состояние forward/fwd.json, свой стор рынков forward/fwd_markets.jsonl, свой отчёт forward/FWD_REPORT.md.

  python3 forward/fwd_sim.py enroll --strategies forward/strategies.json   # зафиксировать кошельки и их стратегии
  python3 forward/fwd_sim.py update                                        # новые сделки, резолвы → fwd.json, отчёт

Правила копии (как в бэктесте strat_search): покупка — новая позиция, если проходит фильтр стратегии и его цена < 0.90;
наш вход = его цена + 0.01; докупки не копируем; выход — пропорционально его продажам по его цене − 0.01;
резолв — 1/0; ставка fix $1 или prop = clip(4·usd/maxusd, 1, 4), где maxusd — его максимальная позиция в окне бэктеста.
"""
from __future__ import annotations
import argparse, json, os, sys, time
from datetime import datetime, timezone
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from pm import api, markets, metrics
markets.STORE = os.path.join(HERE, "fwd_markets.jsonl")   # отдельный стор, чтобы не трогать основной
markets.LEGACY_STORE = os.path.join(HERE, "_none.json")

STATE = os.path.join(HERE, "fwd.json")
REPORT = os.path.join(HERE, "FWD_REPORT.md")
SLIP = 0.01; MAX_ENTRY = 0.90; START_BALANCE = 100.0

def load():
    return json.load(open(STATE)) if os.path.exists(STATE) else {"start_ts": None, "wallets": {}}
def save(s):
    tmp = STATE + ".tmp"; json.dump(s, open(tmp, "w"), ensure_ascii=False); os.replace(tmp, STATE)

def parse_strategy(name: str) -> dict:
    parts = [p.strip() for p in name.split("&")]
    st = {"seg": "all", "live": None, "buckets": None}
    for p in parts:
        if p == "all": continue
        if p in ("live", "pre"): st["live"] = (p == "live"); continue
        if p.startswith("price="): st["buckets"] = p[6:].split("+"); continue
        st["seg"] = p
    return st

def passes(st: dict, cls: dict, live: bool, price: float) -> bool:
    seg = st["seg"]
    if seg.startswith("cat=") and cls["category"] != seg[4:]: return False
    if seg.startswith("sub=") and f'{cls["category"]} / {cls["sub"]}' != seg[4:]: return False
    if seg.startswith("type=") and cls["mtype"] != seg[5:]: return False
    if st["live"] is not None and live != st["live"]: return False
    if st["buckets"] and metrics.price_bucket(price) not in st["buckets"]: return False
    return True

def stake_for(w: dict, usd: float) -> float:
    if w["stake"] == "fix": return 1.0
    return min(max(4.0 * usd / max(w["maxusd"], 1e-9), 1.0), 4.0)

def cmd_enroll(a):
    s = load()
    strat = json.load(open(a.strategies))
    s["start_ts"] = s.get("start_ts") or time.time()
    n = 0
    for w, d in strat.items():
        w = w.lower()
        if w in s["wallets"]: continue
        s["wallets"][w] = {"name": d.get("name", ""), "strategy": d["strategy"], "stake": d["stake"], "maxusd": d["maxusd"],
                           "backtest": d.get("backtest", {}), "start_ts": s["start_ts"], "cash": START_BALANCE,
                           "positions": {}, "closed": [], "skipped": 0, "seen": 0, "processed": [], "his_qty": {}, "history": []}
        n += 1
    save(s); print(f"зачислено {n}, всего {len(s['wallets'])}, старт {datetime.fromtimestamp(s['start_ts'], timezone.utc):%Y-%m-%d %H:%M} UTC", file=sys.stderr)

def update_wallet(w: str, st: dict, now: float):
    tr = api.get(f"{api.DATA}/trades", {"user": w, "limit": 500, "offset": 0}, cache=False) or []
    proc = set(st["processed"]); strat = parse_strategy(st["strategy"])
    new = [t for t in tr if float(t.get("timestamp") or 0) >= st["start_ts"] and (t.get("transactionHash", "") + t.get("asset", "")) not in proc]
    new.sort(key=lambda t: (float(t.get("timestamp") or 0), t.get("side") != "BUY"))
    cids = list({t.get("conditionId") for t in new if t.get("conditionId")} | {p["cid"] for p in st["positions"].values()})
    mk = markets.ensure(cids) if cids else {}
    for t in new:
        st["processed"].append(t.get("transactionHash", "") + t.get("asset", ""))
        asset, cid = t.get("asset"), t.get("conditionId")
        ts, price, size = float(t.get("timestamp") or 0), float(t.get("price") or 0), float(t.get("size") or 0)
        if not asset or price <= 0 or size <= 0: continue
        pos = st["positions"].get(asset)
        if t.get("side") == "BUY":
            st["his_qty"][asset] = st["his_qty"].get(asset, 0.0) + size
            if pos: continue
            m = mk.get(cid) or {}
            cls = markets.classify(m, fetch_tags=False) if m else {"category": "?", "sub": "?", "mtype": "?"}
            live = bool(m.get("gameStartTime") and ts > m["gameStartTime"])
            st["seen"] += 1
            if price >= MAX_ENTRY or not passes(strat, cls, live, price):
                st["skipped"] += 1; continue
            stake = stake_for(st, price * size)
            if st["cash"] < stake: st["skipped"] += 1; continue
            fill = price + SLIP
            st["cash"] -= stake
            st["positions"][asset] = {"cid": cid, "oi": int(t.get("outcomeIndex") or 0), "title": t.get("title"), "opened": ts,
                                      "his_entry": price, "fill": fill, "stake": stake, "shares": stake / fill, "shares0": stake / fill, "proceeds": 0.0}
        else:
            hq = st["his_qty"].get(asset, 0.0)
            frac = min(size / hq, 1.0) if hq > 1e-9 else 0.0
            st["his_qty"][asset] = max(hq - size, 0.0)
            if pos and frac > 0:
                sell = pos["shares"] * frac; got = sell * max(price - SLIP, 0.0)
                pos["shares"] -= sell; pos["proceeds"] += got; st["cash"] += got
                if pos["shares"] <= 1e-9:
                    _close(st, asset, pos, "sold", ts)
    # резолвы и переоценка
    value = 0.0
    for asset, pos in list(st["positions"].items()):
        m = mk.get(pos["cid"]) or {}
        prices = m.get("outcomePrices") or []
        px = float(prices[pos["oi"]]) if pos["oi"] < len(prices) else None
        if m.get("closed") and px is not None:
            res = 1.0 if px >= 0.5 else 0.0
            pos["proceeds"] += pos["shares"] * res; st["cash"] += pos["shares"] * res; pos["shares"] = 0.0
            _close(st, asset, pos, "resolve", now); continue
        value += pos["shares"] * (px if px is not None else pos["fill"])
    st["history"].append({"ts": now, "equity": round(st["cash"] + value, 4), "open": len(st["positions"])})
    st["processed"] = st["processed"][-3000:]

def _close(st, asset, pos, how, ts):
    pos["closed"] = ts; pos["how"] = how; pos["pnl"] = round(pos["proceeds"] - pos["stake"], 4)
    st["closed"].append(pos); st["positions"].pop(asset, None)

def cmd_update(a):
    s = load(); now = time.time()
    ws = list(s["wallets"].items())
    def work(item):
        w, st = item
        try: update_wallet(w, st, now)
        except Exception as e: print(f"\n{w[:10]}: {e}", file=sys.stderr)
        return True
    api.pmap(work, ws, workers=16, desc="fwd")
    markets.save(); save(s); write_report(s)

def write_report(s):
    rows = []
    for w, st in s["wallets"].items():
        eq = st["history"][-1]["equity"] if st["history"] else START_BALANCE
        rows.append({"w": w, "name": st["name"], "pnl": eq - START_BALANCE, "closed": len(st["closed"]), "open": len(st["positions"]),
                     "wins": sum(1 for c in st["closed"] if c["pnl"] > 0), "seen": st["seen"], "skipped": st["skipped"], "strategy": st["strategy"], "stake": st["stake"]})
    rows.sort(key=lambda r: -r["pnl"])
    tot = sum(r["pnl"] for r in rows); act = [r for r in rows if r["closed"] + r["open"] > 0]
    days = (time.time() - s["start_ts"]) / 86400
    out = [f"# Форвард-тест стратегий — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC", "",
           f"Старт {datetime.fromtimestamp(s['start_ts'], timezone.utc):%Y-%m-%d %H:%M} UTC, {days:.1f} дн. Кошельков {len(rows)}, с позициями {len(act)}, "
           f"в плюсе {sum(1 for r in rows if r['pnl'] > 0)}, в минусе {sum(1 for r in rows if r['pnl'] < 0)}. "
           f"Суммарный PnL {tot:+.2f} $. Закрыто позиций {sum(r['closed'] for r in rows)}, открыто {sum(r['open'] for r in rows)}, "
           f"пропущено фильтром {sum(r['skipped'] for r in rows)} из {sum(r['seen'] for r in rows)} покупок.", "",
           "| кошелёк | имя | PnL | закрыто | выигр. | откр. | стратегия | ставка |", "|---|---|---|---|---|---|---|---|"]
    for r in rows[:40] + ([{"w": "…", "name": "", "pnl": 0, "closed": 0, "wins": 0, "open": 0, "strategy": "", "stake": ""}] if len(rows) > 80 else []) + rows[-40:]:
        out.append(f"| `{r['w'][:10]}` | {r['name']} | {r['pnl']:+.2f} | {r['closed']} | {r['wins']} | {r['open']} | {r['strategy']} | {r['stake']} |")
    open(REPORT, "w").write("\n".join(out) + "\n")
    print(f"форвард: кошельков {len(rows)}, с позициями {len(act)}, PnL {tot:+.2f} $, в плюсе {sum(1 for r in rows if r['pnl'] > 0)}, в минусе {sum(1 for r in rows if r['pnl'] < 0)}", file=sys.stderr)

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("enroll"); p.add_argument("--strategies", required=True)
    sub.add_parser("update")
    a = ap.parse_args(); {"enroll": cmd_enroll, "update": cmd_update}[a.cmd](a)

if __name__ == "__main__":
    main()
