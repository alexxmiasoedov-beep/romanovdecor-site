"""Стадия 2. Полная история сделок → эпизоды позиций → метрики, отсечки, сегменты.

Вход: прошедшие стадию 1 (data/stage1.csv) либо --wallets.
Выход: data/stage2.csv, data/segments.csv, data/wallets/<addr>.json (эпизоды для стадии 3).
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from collections import defaultdict

from pm import api, config, episodes as E, markets, metrics

D = os.path.join(os.path.dirname(__file__), "data")
IN = os.path.join(D, "stage1.csv")
OUT = os.path.join(D, "stage2.csv")
SEG_OUT = os.path.join(D, "segments.csv")
WDIR = os.path.join(D, "wallets")

FIELDS = ["wallet", "name", "score", "pass", "fail_reasons", "trades_n", "episodes_n", "closed_n", "open_n",
          "history_days", "days_since_last", "roi_copy", "roi_trimmed", "t_stat", "winrate", "roi_hold",
          "roi_wallet", "roi_half1", "roi_half2", "roi_last30", "max_dd_stakes", "conc_p95", "conc_max",
          "median_hold_h", "both_sides_share", "snipe_share", "live_share", "median_volume",
          "share_entry_ge90", "share_entry_lt10", "profit_share_ge90", "profit_share_lt10",
          "profit_share_top1", "short_crypto_share", "edge_all", "exit_value_add", "size_signal",
          "trades_truncated", "top_category", "top_segments", "approved_segments"]


def seg_keys(ep: dict) -> dict[str, str]:
    c = ep["cls"]
    b = metrics.price_bucket(ep["entry"])
    lv = "live" if ep["live"] else "pre"
    keys = {"L1": c["category"], "L2": f'{c["category"]} / {c["sub"]}',
            "L3": f'{c["category"]} / {c["sub"]} / {c["league"]}',
            "L2t": f'{c["category"]} / {c["sub"]} / type={c["mtype"]}',
            "L1b": f'{c["category"]} / price={b}',
            "L2b": f'{c["category"]} / {c["sub"]} / price={b}'}
    if c["is_sport"]:
        keys["L2l"] = f'{c["category"]} / {c["sub"]} / {lv}'
    return keys


def analyze(wallet: str, name: str = "", now: float | None = None) -> tuple[dict, list[dict], list[dict]]:
    now = now or time.time()
    trades = api.trades_user(wallet)
    row = {"wallet": wallet, "name": name or (trades[0].get("name") if trades else ""), "trades_n": len(trades),
           "trades_truncated": len(trades) >= 10500}
    reasons: list[str] = []
    cids = {t.get("conditionId") for t in trades if t.get("conditionId")}
    mk = markets.ensure(cids)
    eps = E.build(trades, mk, now)
    for ep in eps:
        ep["cls"] = markets.classify(mk.get(ep["cid"], {}))
    closed = [e for e in eps if e["is_closed"]]
    opened = [e for e in eps if not e["is_closed"]]
    row.update({"episodes_n": len(eps), "closed_n": len(closed), "open_n": len({e["cid"] for e in opened})})
    if trades:
        ts = [float(t["timestamp"]) for t in trades]
        row["history_days"] = round((max(ts) - min(ts)) / 86400, 1)
        row["days_since_last"] = round((now - max(ts)) / 86400, 1)
    if len(closed) < config.MIN_CLOSED_POSITIONS:
        reasons.append(f"closed<{config.MIN_CLOSED_POSITIONS}")
    if closed:
        rs = [e["r_copy"] for e in closed]
        n = len(rs)
        half = n // 2
        pos_like = [{"entry": e["entry"], "pnl": e["pnl_wallet"], "r": e["r_copy"], "resolved": e["outcome_res"],
                     "t_open": e["t_open"]} for e in closed]
        with_res = [p for p in pos_like if p["resolved"] is not None]
        edge = metrics.calibration_edge(with_res)
        sold = [e for e in closed if e["sold"] > 0 and e["r_hold"] is not None]
        med_cost = metrics.percentile([e["cost"] for e in closed], 0.5)
        big = [e["r_copy"] for e in closed if e["cost"] >= med_cost]
        small = [e["r_copy"] for e in closed if e["cost"] < med_cost]
        sport = [e for e in closed if e["cls"]["is_sport"]]
        cid_assets = defaultdict(set)
        for e in eps:
            cid_assets[e["cid"]].add(e["asset"])
        p95, cmax = E.concurrency(eps, now)
        cat_counter = defaultdict(int)
        for e in closed:
            cat_counter[e["cls"]["category"]] += 1
        row.update({
            "roi_copy": round(metrics.mean(rs), 4), "roi_trimmed": round(metrics.trimmed_mean(rs), 4),
            "t_stat": round(metrics.t_stat(rs), 2),
            "winrate": round(metrics.mean(1.0 if r > 0 else 0.0 for r in rs), 3),
            "roi_hold": round(metrics.mean(e["r_hold"] for e in closed if e["r_hold"] is not None), 4),
            "roi_wallet": round(metrics.mean(e["r_wallet"] for e in closed), 4),
            "roi_half1": round(metrics.mean(rs[:half]), 4), "roi_half2": round(metrics.mean(rs[half:]), 4),
            "roi_last30": round(metrics.mean(rs[-30:]), 4),
            "max_dd_stakes": round(metrics.max_drawdown(rs), 2),
            "conc_p95": p95, "conc_max": cmax,
            "median_hold_h": round(metrics.percentile([e["hold_h"] for e in closed], 0.5), 2),
            "both_sides_share": round(metrics.mean(1.0 if len(a) > 1 else 0.0 for a in cid_assets.values()), 3),
            "snipe_share": round(metrics.mean(1.0 if e["snipe"] else 0.0 for e in closed), 3),
            "live_share": round(metrics.mean(1.0 if e["live"] else 0.0 for e in sport), 3) if sport else "",
            "median_volume": round(metrics.percentile([e["volume"] for e in closed], 0.5)),
            "share_entry_ge90": round(metrics.mean(1.0 if e["entry"] >= .9 else 0.0 for e in closed), 3),
            "share_entry_lt10": round(metrics.mean(1.0 if e["entry"] < .1 else 0.0 for e in closed), 3),
            "short_crypto_share": round(metrics.mean(1.0 if e["cls"]["short_crypto"] else 0.0 for e in closed), 3),
            "edge_all": edge["_all"]["edge"],
            "exit_value_add": round(metrics.mean(e["r_copy"] - e["r_hold"] for e in sold), 4) if sold else "",
            "size_signal": round(metrics.mean(big) - metrics.mean(small), 4) if big and small else "",
            "top_category": max(cat_counter, key=cat_counter.get),
        })
        row.update({k: round(v, 3) for k, v in metrics.profit_shares(pos_like).items()})
        # --- отсечки
        if row["roi_copy"] <= 0:
            reasons.append("roi_copy<=0")
        if row["t_stat"] < config.MIN_T_STAT:
            reasons.append(f"t<{config.MIN_T_STAT}")
        if row["conc_p95"] > config.MAX_CONCURRENT_P95:
            reasons.append(f"concurrency_p95>{config.MAX_CONCURRENT_P95}")
        if row["median_volume"] < config.MIN_MEDIAN_MARKET_VOLUME:
            reasons.append("low_liquidity")
        if row["median_hold_h"] < config.MIN_MEDIAN_HOLD_HOURS:
            reasons.append("hold<1h")
        if row["both_sides_share"] > config.MAX_BOTH_SIDES_SHARE:
            reasons.append("both_sides")
        if row["snipe_share"] > config.MAX_SNIPE_SHARE:
            reasons.append("sniping")
        if row["share_entry_ge90"] > config.MAX_SHARE_ENTRY_GE_90:
            reasons.append("entries>=0.90")
        if row["profit_share_lt10"] > config.MAX_PROFIT_SHARE_LT_10:
            reasons.append("profit_from<0.10")
        if row["profit_share_top1"] > config.MAX_PROFIT_SHARE_TOP1:
            reasons.append("top1_concentration")
        if row["short_crypto_share"] > config.MAX_SHORT_CRYPTO_SHARE:
            reasons.append("short_crypto")
        if row["max_dd_stakes"] > config.MAX_DRAWDOWN_STAKES:
            reasons.append("drawdown")
        if config.MIN_PROFITABLE_HALF and (row["roi_half1"] <= 0 or row["roi_half2"] <= 0):
            reasons.append("unstable_halves")
        if row.get("history_days", 0) < config.MIN_HISTORY_DAYS:
            reasons.append(f"history<{config.MIN_HISTORY_DAYS}d")
        if row.get("days_since_last", 0) > config.MAX_SILENCE_DAYS:
            reasons.append("silent")
        # --- сегменты
        seg_rows = []
        overall = row["roi_copy"]
        for level in ("L1", "L2", "L3", "L2t", "L1b", "L2b", "L2l"):
            def key_fn(e, level=level):
                return seg_keys(e).get(level)
            for s in metrics.segment_stats([{**e, "r": e["r_copy"]} for e in closed], key_fn, overall):
                s.update({"wallet": wallet, "level": level})
                seg_rows.append(s)
        # корзина ≥0,90 и 5-минутная крипта не копируются по условиям стратегии, даже с плюсом
        for s in seg_rows:
            if "price=0.90-1.00" in s["segment"] or "Up/Down short" in s["segment"]:
                s["approved"] = False
        approved = [s for s in seg_rows if s["approved"]]
        approved.sort(key=lambda s: -s["roi_shrunk"] * (s["n"] ** 0.5))
        row["approved_segments"] = " | ".join(f'{s["segment"]} (n={s["n"]}, roi={s["roi_shrunk"]:+.2f})'
                                              for s in approved[:6])
        best = sorted(seg_rows, key=lambda s: -s["roi_shrunk"] * (s["n"] ** 0.5))[:3]
        row["top_segments"] = " | ".join(f'{s["segment"]} (n={s["n"]}, roi={s["roi_shrunk"]:+.2f})' for s in best)
        stability = 1.0 if row["roi_half1"] > 0 and row["roi_half2"] > 0 else 0.5
        row["score"] = round(row["roi_trimmed"] * min(1.0, row["t_stat"] / 3) * stability, 4)
    else:
        seg_rows = []
        row["score"] = 0
    # кошелёк с отрицательным общим ROI, но утверждённым сегментом — кандидат на копирование сегмента
    if reasons and closed and row.get("approved_segments"):
        soft = {"roi_copy<=0", f"t<{config.MIN_T_STAT}", "unstable_halves", "drawdown"}
        if all(r in soft for r in reasons):
            reasons = [f"segment_only:{r}" for r in reasons]
            row["pass"] = "segment"
    row.setdefault("pass", not reasons)
    row["fail_reasons"] = ";".join(reasons)
    return row, seg_rows, eps


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallets", nargs="*")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--all-stage1", action="store_true", help="не только прошедшие стадию 1")
    args = ap.parse_args()
    if args.wallets:
        items = [(w, "") for w in args.wallets]
    else:
        with open(IN) as f:
            rows = list(csv.DictReader(f))
        items = [(r["wallet"], r["name"]) for r in rows if args.all_stage1 or r["pass"] == "True"]
    if args.limit:
        items = items[: args.limit]
    os.makedirs(WDIR, exist_ok=True)
    print(f"стадия 2: {len(items)} кошельков", file=sys.stderr)

    def work(it):
        row, segs, eps = analyze(*it)
        with open(os.path.join(WDIR, f"{it[0]}.json"), "w") as f:
            json.dump({"row": row, "episodes": eps}, f, ensure_ascii=False)
        return row, segs

    res = api.pmap(work, items, workers=args.workers, desc="stage2")
    rows = [r[0] for r in res if r]
    segs = [s for r in res if r for s in r[1]]
    markets.save()
    rows.sort(key=lambda r: -(r.get("score") or 0))
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    with open(SEG_OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["wallet", "level", "segment", "n", "roi_mean", "roi_shrunk", "t",
                                          "winrate", "roi_half1", "roi_half2", "approved"])
        w.writeheader()
        keep = {r["wallet"] for r in rows if r["pass"] in (True, "segment")}
        # пишем сегменты только прошедших кошельков и утверждённые — иначе файл на десятки МБ
        w.writerows(s for s in segs if s["approved"] or (s["wallet"] in keep and s["n"] >= 20))
    passed = [r for r in rows if r["pass"] is True]
    seg_only = [r for r in rows if r["pass"] == "segment"]
    print(f"прошли стадию 2 целиком: {len(passed)}, только сегментом: {len(seg_only)}, всего {len(rows)}",
          file=sys.stderr)
    from collections import Counter
    c = Counter(x for r in rows for x in r["fail_reasons"].split(";") if x)
    for k, v in c.most_common():
        print(f"  {k}: {v}", file=sys.stderr)


if __name__ == "__main__":
    main()
