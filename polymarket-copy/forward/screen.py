"""Отбор кошельков в симуляцию 2 одной командой (гипотеза владельца, 07.10):
  python3 forward/screen.py --wallets forward/incoming_wallets.txt [--out forward/strategies_new.json]

1) три фильтра: последняя сделка ≤ 2 дней; за 30 дней 20..150 сделок; открытых (нерезолвленных) позиций ≤ 10;
   ликвидность — доля покупок со сдвигом цены >10% за ±минуту не выше 50% (минимум 5 оценённых);
2) бэктест за 30 дней по его позициям, перебор стратегий (сегмент × лайв/прематч × диапазон цены × ставка fix/prop),
   минимум 10 позиций; надёжной считается стратегия с плюсом в обеих половинах периода и t ≥ 2;
3) результат — JSON стратегий для fwd_sim.py enroll --strategies. Ничего общего с симуляцией 1 не трогает.
"""
import argparse, csv, json, math, os, re, sys, time
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pm import api, markets, metrics
HERE = os.path.dirname(os.path.abspath(__file__))
markets.STORE = os.path.join(HERE, "fwd_markets.jsonl"); markets.LEGACY_STORE = os.path.join(HERE, "_none.json")

ap = argparse.ArgumentParser()
ap.add_argument("--wallets", required=True, help="файл: адреса 0x… в любом виде")
ap.add_argument("--out", default=os.path.join(HERE, "strategies_new.json"))
ap.add_argument("--min-t", type=float, default=2.0)
args = ap.parse_args()
wallets = sorted({w.lower() for w in re.findall(r"0x[0-9a-fA-F]{40}", open(args.wallets).read())})
already = set(json.load(open(os.path.join(HERE, "fwd.json")))["wallets"]) if os.path.exists(os.path.join(HERE, "fwd.json")) else set()
print(f"адресов в файле: {len(wallets)}, уже в симуляции 2: {len(set(wallets) & already)}", file=sys.stderr)
wallets = [w for w in wallets if w not in already]
now = time.time(); D2 = now - 2*86400; D30 = now - 30*86400

# ---- фильтр 1 (+ сразу забираем сделки за 30 дней для бэктеста)
KEEP = ("side","asset","conditionId","size","price","timestamp","outcomeIndex","title","name")
def f1(w):
    tr = api.get(f"{api.DATA}/trades", {"user": w, "limit": 500, "offset": 0}, cache=False) or []
    if not tr: return {"ok": False, "why": "no_trades", "tr": []}
    last = max(float(t.get("timestamp") or 0) for t in tr)
    tr30 = [t for t in tr if float(t.get("timestamp") or 0) >= D30]
    ok = last >= D2 and 20 <= len(tr30) <= 150
    return {"ok": ok, "why": "" if ok else ("stale" if last < D2 else "few" if len(tr30) < 20 else "many"),
            "tr": [{k: t.get(k) for k in KEEP} for t in tr30] if ok else []}
r1 = dict(zip(wallets, api.pmap(f1, wallets, workers=24, desc="f1")))
p1 = [w for w, r in r1.items() if r and r["ok"]]
print("фильтр 1:", len(p1), "из", len(wallets), Counter((r or {}).get("why", "error") or "ok" for r in r1.values()), file=sys.stderr)

# ---- фильтр 2
def f2(w):
    pos = api.get(f"{api.DATA}/positions", {"user": w, "limit": 500, "offset": 0, "sizeThreshold": 0}, cache=False) or []
    live = [p for p in pos if not p.get("redeemable") and 0.005 < float(p.get("curPrice") or 0) < 0.995]
    return len(live) <= 10
r2 = dict(zip(p1, api.pmap(f2, p1, workers=24, desc="f2")))
p2 = [w for w in p1 if r2.get(w)]
print("фильтр 2:", len(p2), "из", len(p1), file=sys.stderr)

# ---- фильтр 3
def f3(w):
    buys = sorted((t for t in r1[w]["tr"] if t["side"] == "BUY" and t.get("asset")), key=lambda t: -float(t["timestamp"]))[:20]
    moved = checked = 0
    for b in buys:
        ts = int(float(b["timestamp"]))
        h = api.get(f"{api.CLOB}/prices-history", {"market": b["asset"], "startTs": ts-900, "endTs": ts+900, "fidelity": 1}, cache=False)
        h = (h or {}).get("history", []) if isinstance(h, dict) else []
        before = [x["p"] for x in h if x["t"] <= ts-30]; after = [x["p"] for x in h if x["t"] >= ts+30]
        if not before or not after or before[-1] <= 0: continue
        checked += 1
        if abs(after[0] - before[-1]) / before[-1] > 0.10: moved += 1
    return checked < 5 or moved / checked <= 0.5
r3 = dict(zip(p2, api.pmap(f3, p2, workers=12, desc="f3")))
p3 = [w for w in p2 if r3.get(w)]
print("фильтр 3:", len(p3), "из", len(p2), file=sys.stderr)

# ---- бэктест и стратегии (как в strat_search)
cids = sorted({t["conditionId"] for w in p3 for t in r1[w]["tr"] if t.get("conditionId")})
mk = {}
for i in range(0, len(cids), 500):
    got = markets.ensure(cids[i:i+500])
    for c, m in got.items():
        cls = markets.classify(m, fetch_tags=False)
        mk[c] = {"closed": bool(m.get("closed")), "prices": m.get("outcomePrices") or [], "gst": m.get("gameStartTime") or 0,
                 "cat": cls["category"], "sub": cls["sub"], "mtype": cls["mtype"], "missing": bool(m.get("missing"))}
markets.save()
SLIP = 0.01; MAX_ENTRY = 0.90

def positions(tr):
    """Позиции кошелька за окно: cost, proceeds, остаток × итоговая цена → ROI его позиции."""
    tr = sorted(tr, key=lambda t: float(t["timestamp"]))
    P = {}
    for t in tr:
        a = t["asset"]; px = float(t["price"] or 0); sz = float(t["size"] or 0); ts = float(t["timestamp"])
        if not a or px <= 0 or sz <= 0: continue
        if t["side"] == "BUY":
            p = P.setdefault(a, {"cid": t["conditionId"], "oi": int(t.get("outcomeIndex") or 0), "ts": ts, "cost": 0.0, "sh": 0.0, "sold": 0.0, "proc": 0.0, "title": t.get("title") or ""})
            p["cost"] += px*sz; p["sh"] += sz
        else:
            p = P.get(a)
            if not p or p["sh"] - p["sold"] <= 1e-9: continue
            s = min(sz, p["sh"] - p["sold"]); p["sold"] += s; p["proc"] += s*px
    out = []
    for a, p in P.items():
        m = mk.get(p["cid"])
        if not m or m.get("missing") or not m["prices"] or p["oi"] >= len(m["prices"]): continue
        fin = float(m["prices"][p["oi"]])
        if m["closed"]: fin = 1.0 if fin >= 0.5 else 0.0
        entry = p["cost"]/p["sh"]
        if entry >= MAX_ENTRY: continue
        value = p["proc"] + (p["sh"] - p["sold"]) * fin
        roi_his = value/p["cost"] - 1
        roi_copy = (roi_his + 1) * entry/(entry + SLIP) - 1
        live = bool(m["gst"] and p["ts"] > m["gst"])
        out.append({"ts": p["ts"], "usd": p["cost"], "entry": entry, "roi": roi_copy, "resolved": m["closed"],
                    "cat": m["cat"], "sub": f'{m["cat"]} / {m["sub"]}', "mtype": m["mtype"], "live": live,
                    "bucket": metrics.price_bucket(entry), "title": p["title"]})
    return out

BUCKETS = ["0.10-0.30", "0.30-0.50", "0.50-0.70", "0.70-0.90"]
def bucket_unions():
    u = [None]
    for i in range(4):
        u.append((BUCKETS[i],))
        if i < 3: u.append((BUCKETS[i], BUCKETS[i+1]))
        if i < 2: u.append((BUCKETS[i], BUCKETS[i+1], BUCKETS[i+2]))
    return u

def evaluate(pos, sel, stake_mode, maxusd):
    rows = [p for p in pos if sel(p)]
    if len(rows) < 10: return None
    pnls = []
    for p in rows:
        st = 1.0 if stake_mode == "fix" else min(max(4.0 * p["usd"]/maxusd, 1.0), 4.0)
        pnls.append(st * p["roi"])
    n = len(pnls); tot = sum(pnls); mean = tot/n
    sd = (sum((x-mean)**2 for x in pnls)/(n-1))**0.5 if n > 1 else 0
    t = mean/sd*math.sqrt(n) if sd > 0 else 0
    rows_s = sorted(zip(rows, pnls), key=lambda x: x[0]["ts"]); h = n//2
    h1 = sum(x[1] for x in rows_s[:h]); h2 = sum(x[1] for x in rows_s[h:])
    wins = sum(1 for x in pnls if x > 0)
    return {"n": n, "pnl": round(tot, 2), "t": round(t, 2), "h1": round(h1, 2), "h2": round(h2, 2), "wins": wins,
            "stake_sum": round(sum((1.0 if stake_mode == "fix" else min(max(4.0*p["usd"]/maxusd, 1.0), 4.0)) for p in rows), 1),
            "unresolved": sum(1 for p in rows if not p["resolved"])}

def strategies(pos):
    cats = sorted({p["cat"] for p in pos}); subs = sorted({p["sub"] for p in pos}); mtypes = sorted({p["mtype"] for p in pos})
    segs = [("all", lambda p: True)]
    segs += [(f"cat={c}", (lambda c: lambda p: p["cat"] == c)(c)) for c in cats]
    segs += [(f"sub={s}", (lambda s: lambda p: p["sub"] == s)(s)) for s in subs]
    segs += [(f"type={m}", (lambda m: lambda p: p["mtype"] == m)(m)) for m in mtypes]
    lives = [("", lambda p: True), ("live", lambda p: p["live"]), ("pre", lambda p: not p["live"])]
    for sname, sf in segs:
        for lname, lf in lives:
            for bu in BU:
                bf = (lambda bu: (lambda p: p["bucket"] in bu))(bu) if bu else (lambda p: True)
                name = sname + (f" & {lname}" if lname else "") + (f" & price={'+'.join(bu)}" if bu else "")
                yield name, (lambda sf, lf, bf: lambda p: sf(p) and lf(p) and bf(p))(sf, lf, bf)
BU = bucket_unions()

out = {}; stats = Counter()
for w in p3:
    pos = positions(r1[w]["tr"])
    if len(pos) < 10: stats["<10 позиций"] += 1; continue
    maxusd = max(p["usd"] for p in pos) or 1.0
    best = None
    for name, sel in strategies(pos):
        for mode in ("fix", "prop"):
            r = evaluate(pos, sel, mode, maxusd)
            if not r: continue
            key = (r["pnl"] > 0 and r["h1"] > 0 and r["h2"] > 0, r["t"], r["pnl"])
            if best is None or key > best[0]: best = (key, name, mode, r)
    k, name, mode, r = best
    if r["pnl"] > 0 and r["h1"] > 0 and r["h2"] > 0 and r["t"] >= args.min_t:
        stats["надёжная стратегия"] += 1
        out[w] = {"name": next((t.get("name") for t in r1[w]["tr"] if t.get("name")), ""), "strategy": name, "stake": mode, "maxusd": round(maxusd, 2),
                  "backtest": {"n": r["n"], "pnl": r["pnl"], "t": r["t"]}}
    else:
        stats["нет надёжной"] += 1
json.dump(out, open(args.out, "w"), ensure_ascii=False, indent=0)
print(f"ИТОГ: файл {len(wallets)} → ф1 {len(p1)} → ф2 {len(p2)} → ф3 {len(p3)} → стратегии {dict(stats)}; записано {args.out} ({len(out)} кошельков)", file=sys.stderr)
