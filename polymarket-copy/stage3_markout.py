"""Стадия 3. Реалистичный вход: история цен → ROI с задержкой 5/30 мин, маркаут, проскальзывание.

Вход: прошедшие стадию 2 (целиком или сегментом) либо --wallets. Выход: data/stage3.csv.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time

from pm import api, config, markets, metrics

D = os.path.join(os.path.dirname(__file__), "data")
IN = os.path.join(D, "stage2.csv")
OUT = os.path.join(D, "stage3.csv")
WDIR = os.path.join(D, "wallets")

FIELDS = ["wallet", "name", "final_score", "pass", "fail_reasons", "n_checked", "roi_copy_checked",
          "roi_delay_0.5m", "roi_delay_1m", "roi_delay_5m", "roi_delay_30m", "keep_ratio5", "skip_share",
          "roi_delay5_filtered", "t_delay5", "tape_share", "markout_1h", "markout_24h", "slippage_median",
          "slippage_n", "spread_median", "stage2_score", "approved_segments"]


def price_at(hist: list[dict], ts: float) -> float | None:
    p = None
    for h in hist:
        if h["t"] <= ts:
            p = h["p"]
        else:
            break
    if p is None and hist:
        p = hist[0]["p"]
    return p


def tape_price(ep: dict, ts: float, horizon: float = 1800) -> float | None:
    """Цена первой сделки по рынку не раньше ts (в пределах horizon сек) из ленты сделок.
    Сделки по противоположному токену пересчитываются как 1 − p."""
    tape = api.trades_market(ep["cid"], max_pages=config.TAPE_PAGES, cache=True)
    if not tape:
        return None
    oldest = min(float(t.get("timestamp") or 0) for t in tape)
    if oldest > ts:
        return None  # лента усечена раньше нужного момента
    best = None
    for t in tape:
        tt = float(t.get("timestamp") or 0)
        if ts <= tt <= ts + horizon and (best is None or tt < best[0]):
            p = float(t.get("price") or 0)
            if t.get("asset") != ep["asset"]:
                p = 1 - p
            best = (tt, p)
    return best[1] if best else None


def episode_markout(ep: dict) -> dict | None:
    t0 = int(ep["t_open"])
    t1 = int(ep["t_close"])
    end = min(t1, t0 + 25 * 3600) + 600
    hist = api.prices_history(ep["asset"], t0 - 600, end, fidelity=5)
    if not hist:
        return None
    hist.sort(key=lambda h: h["t"])
    hist1 = None  # поминутная история подгружается только для задержек < 5 мин
    exit_val = ep["exit_val"]
    entry = ep["entry"]
    out = {"r_copy": ep["r_copy"]}
    for d in config.DELAYS_MIN:
        ts = t0 + d * 60
        if d < 1:
            p = tape_price(ep, ts)
            out["tape_used"] = p is not None
            if p is None:
                if hist1 is None:
                    hist1 = sorted(api.prices_history(ep["asset"], t0 - 120, min(t1, t0 + 3600) + 60, fidelity=1),
                                   key=lambda h: h["t"])
                p = price_at(hist1, t0 + 60) if hist1 else price_at(hist, ts)
        elif d < 5:
            if hist1 is None:
                hist1 = sorted(api.prices_history(ep["asset"], t0 - 120, min(t1, t0 + 3600) + 60, fidelity=1),
                               key=lambda h: h["t"])
            p = price_at(hist1, ts) if hist1 else price_at(hist, ts)
        else:
            p = price_at(hist, ts)
        if ts >= t1:  # рынок уже закрыт — копия не состоялась
            p = None
        if p is None or p <= 0:
            out[f"r_delay{d:g}"] = None
            continue
        fill = p * (1 + config.ASSUMED_SLIPPAGE_REL)
        out[f"r_delay{d:g}"] = min(exit_val / fill - 1, 5.0)  # кап: цена в истории может провалиться к нулю
        if d == config.DELAYS_MIN[0]:
            out["skipped"] = (p > entry + config.MAX_PRICE_DRIFT) or (p >= config.MAX_ENTRY_PRICE)
    for h in config.MARKOUT_H:
        th = t0 + h * 3600
        if th >= t1:
            p = ep["res"] if ep["res"] is not None else exit_val
        else:
            p = price_at(hist, th)
        out[f"markout_{h}h"] = (p - entry) / entry if p is not None else None
    return out


def slippage(asset: str, stake: float) -> tuple[float | None, float | None]:
    """(проскальзывание при покупке на stake $, спред) по текущему стакану."""
    b = api.book(asset)
    if not b or not b.get("asks"):
        return None, None
    asks = sorted(((float(a["price"]), float(a["size"])) for a in b["asks"]), key=lambda x: x[0])
    bids = [float(x["price"]) for x in b.get("bids", [])]
    best = asks[0][0]
    spread = best - max(bids) if bids else None
    left = stake
    cost = 0.0
    shares = 0.0
    for p, s in asks:
        take = min(s, left / p)
        cost += take * p
        shares += take
        left -= take * p
        if left <= 1e-9:
            break
    if left > 1e-9:
        return 1.0, spread  # глубины не хватило
    return cost / shares / best - 1, spread


def check(wallet: str, name: str, stage2_row: dict) -> dict:
    with open(os.path.join(WDIR, f"{wallet}.json")) as f:
        data = json.load(f)
    eps = [e for e in data["episodes"] if e["is_closed"] and e["exit_val"] is not None]
    eps = sorted(eps, key=lambda e: -e["t_open"])[: config.STAGE3_EPISODES]
    res = [r for r in api.pmap(episode_markout, eps, workers=4, desc=f"hist {wallet[:8]}") if r]
    row = {"wallet": wallet, "name": name, "n_checked": len(res),
           "stage2_score": stage2_row.get("score"), "approved_segments": stage2_row.get("approved_segments")}
    reasons = []
    if len(res) < 20:
        reasons.append("too_few_price_histories")
    else:
        D0 = f"r_delay{config.DELAYS_MIN[0]:g}"
        d5 = [r[D0] for r in res if r.get(D0) is not None]  # рабочая задержка (имя поля историческое)
        base = metrics.trimmed_mean(r["r_copy"] for r in res)
        filt = [r[D0] for r in res if r.get(D0) is not None and not r.get("skipped")]
        row.update({
            "roi_copy_checked": round(base, 4),
            "t_delay5": round(metrics.t_stat(d5), 2) if d5 else "",
            "skip_share": round(1 - len(filt) / max(len(d5), 1), 3),
            "roi_delay5_filtered": round(metrics.trimmed_mean(filt), 4) if filt else "",
            "tape_share": round(metrics.mean(1.0 if r.get("tape_used") else 0.0 for r in res), 3),
            **{f"roi_delay_{d:g}m": (round(metrics.trimmed_mean(xs), 4) if (xs := [r[f"r_delay{d:g}"] for r in res if r.get(f"r_delay{d:g}") is not None]) else "")
               for d in config.DELAYS_MIN},
            **{f"roi_delay_{d:g}m": (round(metrics.trimmed_mean(xs), 4) if (xs := [r[f"r_delay{d:g}"] for r in res if r.get(f"r_delay{d:g}") is not None]) else "")
               for d in config.DELAYS_MIN},
            "markout_1h": round(metrics.mean(r["markout_1h"] for r in res if r.get("markout_1h") is not None), 4),
            "markout_24h": round(metrics.mean(r["markout_24h"] for r in res if r.get("markout_24h") is not None), 4),
        })
        keep = (metrics.trimmed_mean(d5) / base) if (d5 and base > 0) else 0.0
        row["keep_ratio5"] = round(keep, 2)
        if not d5 or metrics.trimmed_mean(d5) <= 0:
            reasons.append("delayed_roi<=0")
        elif base > 0 and keep < config.MIN_DELAYED_ROI_KEEP:
            reasons.append("edge_decays_with_delay")
    # проскальзывание по стаканам ещё идущих рынков кошелька (endDate в будущем, иначе стакан пустой)
    mk = markets._load()
    now = time.time()
    open_eps = [e for e in data["episodes"] if not e["is_closed"]
                and (mk.get(e["cid"], {}).get("endDate") or 0) > now][:10]
    sl = [slippage(e["asset"], config.FIXED_STAKE_USD) for e in open_eps]
    sls = [s for s, _ in sl if s is not None]
    sps = [p for _, p in sl if p is not None]
    row["slippage_n"] = len(sls)
    row["slippage_median"] = round(metrics.percentile(sls, 0.5), 4) if sls else ""
    row["spread_median"] = round(metrics.percentile(sps, 0.5), 3) if sps else ""
    if len(sls) >= 3 and metrics.percentile(sls, 0.5) > config.MAX_SLIPPAGE:
        reasons.append("slippage")
    s2 = float(stage2_row.get("score") or 0)
    row["final_score"] = round(s2 * max(0.0, min(1.0, row.get("keep_ratio5") or 0)), 4) if not reasons else 0
    row["pass"] = not reasons
    row["fail_reasons"] = ";".join(reasons)
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallets", nargs="*")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    with open(IN) as f:
        s2 = {r["wallet"]: r for r in csv.DictReader(f)}
    if args.wallets:
        items = [(w, s2.get(w, {}).get("name", ""), s2.get(w, {})) for w in args.wallets]
    else:
        items = [(w, r["name"], r) for w, r in s2.items() if r["pass"] in ("True", "segment")]
    if args.limit:
        items = items[: args.limit]
    print(f"стадия 3: {len(items)} кошельков", file=sys.stderr)
    rows = []
    for w, n, r in items:
        try:
            rows.append(check(w, n, r))
        except Exception as e:  # noqa: BLE001
            print(f"{w}: {e}", file=sys.stderr)
    rows.sort(key=lambda r: -(r.get("final_score") or 0))
    with open(OUT, "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        wr.writeheader()
        wr.writerows(rows)
    print(f"прошли стадию 3: {sum(1 for r in rows if r['pass'])} из {len(rows)}; {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
