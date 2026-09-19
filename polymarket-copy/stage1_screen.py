"""Стадия 1. Дешёвые отсечки: все позиции кошелька (/positions + /closed-positions).

На кошелёк 2-25 запросов, без разбора сделок. Считает равновзвешенный ROI на позицию, распределение
цен входа, концентрацию прибыли, число открытых позиций сейчас, возраст истории.
Результат: data/stage1.csv (все) и список прошедших для стадии 2.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time

from pm import api, config, metrics
from collect_wallets import is_short_crypto

IN = os.path.join(os.path.dirname(__file__), "data", "wallets_today.json")
OUT = os.path.join(os.path.dirname(__file__), "data", "stage1.csv")
MAX_POS_PAGES = 10      # >5000 позиций за жизнь — гиперактивный бот, не копируется
MAX_CLOSED_PAGES = 10

FIELDS = ["wallet", "name", "closed_n", "open_now", "open_total", "history_days", "roi_equal", "roi_trimmed",
          "t_stat", "winrate", "share_entry_ge90", "share_entry_lt10", "profit_share_ge90",
          "profit_share_lt10", "profit_share_top1", "short_crypto_share", "total_realized_pnl",
          "avg_cost", "pass", "fail_reasons"]


def collect_positions(wallet: str) -> tuple[list[dict], list[dict], dict]:
    """Объединяет /positions (все позиции, в т.ч. проигранные с curPrice=0 и невыкупленные
    выигрыши) и /closed-positions (выкупленные выигрыши). Оба среза берутся в одном окне
    времени, чтобы усечение выкупленных (≤1000 записей) не искажало винрейт."""
    opens = api.positions(wallet, max_pages=1)
    if len(opens) >= 500:
        opens = api.positions(wallet, max_pages=MAX_POS_PAGES)
    closed = api.closed_positions(wallet, max_pages=MAX_CLOSED_PAGES)
    cutoff = 0.0
    if len(closed) >= MAX_CLOSED_PAGES * 50:  # усечено — ограничиваем окно самой старой выкупленной
        cutoff = min(float(c.get("timestamp") or 0) for c in closed)
    pos = []
    for c in closed:
        entry = float(c.get("avgPrice") or 0); bought = float(c.get("totalBought") or 0)
        cost = entry * bought
        if cost <= 0 or float(c.get("timestamp") or 0) < cutoff:
            continue
        pnl = float(c.get("realizedPnl") or 0)
        pos.append({"entry": entry, "cost": cost, "pnl": pnl, "r": pnl / cost, "resolved": 1.0,
                    "t_open": float(c.get("timestamp") or 0), "title": c.get("title", ""),
                    "slug": c.get("slug", ""), "conditionId": c.get("conditionId")})
    live = []
    for o in opens:
        cur = float(o.get("curPrice") or 0)
        entry = float(o.get("avgPrice") or 0); bought = float(o.get("totalBought") or 0)
        cost = entry * bought
        end = o.get("endDate") or ""
        try:
            t_end = time.mktime(time.strptime(end[:10], "%Y-%m-%d"))
        except ValueError:
            t_end = 0.0
        if cur in (0.0, 1.0) and (o.get("redeemable") or float(o.get("size") or 0) > 0):
            if cost <= 0 or (cutoff and t_end < cutoff):
                continue
            pnl = float(o.get("cashPnl") or 0) + float(o.get("realizedPnl") or 0)
            pos.append({"entry": entry, "cost": cost, "pnl": pnl, "r": pnl / cost, "resolved": cur,
                        "t_open": t_end, "title": o.get("title", ""), "slug": o.get("slug", ""),
                        "conditionId": o.get("conditionId")})
        elif 0.001 < cur < 0.999 and float(o.get("size") or 0) > 0 and not o.get("redeemable"):
            live.append(o)
    return pos, live, {"open_total": len(opens), "closed_total": len(closed), "cutoff": cutoff,
                       "positions_truncated": len(opens) >= MAX_POS_PAGES * 500}



def screen(wallet: str, name: str = "") -> dict:
    pos, live, meta = collect_positions(wallet)
    row = {"wallet": wallet, "name": name, "closed_n": len(pos)}
    reasons = []
    if meta["positions_truncated"]:
        reasons.append(f"positions>{MAX_POS_PAGES * 500}")
    if len(pos) < config.MIN_CLOSED_POSITIONS:
        reasons.append(f"closed<{config.MIN_CLOSED_POSITIONS}")
    if pos:
        rs = [p["r"] for p in pos]
        ts = [p["t_open"] for p in pos if p["t_open"]]
        row.update({
            "roi_equal": round(metrics.mean(rs), 4),
            "roi_trimmed": round(metrics.trimmed_mean(rs), 4),
            "t_stat": round(metrics.t_stat(rs), 2),
            "winrate": round(metrics.mean(1.0 if r > 0 else 0.0 for r in rs), 3),
            "share_entry_ge90": round(metrics.mean(1.0 if p["entry"] >= .90 else 0.0 for p in pos), 3),
            "share_entry_lt10": round(metrics.mean(1.0 if p["entry"] < .10 else 0.0 for p in pos), 3),
            "short_crypto_share": round(metrics.mean(1.0 if is_short_crypto(p["title"], p["slug"]) else 0.0 for p in pos), 3),
            "total_realized_pnl": round(sum(p["pnl"] for p in pos), 2),
            "avg_cost": round(metrics.mean(p["cost"] for p in pos), 2),
            "history_days": round((max(ts) - min(ts)) / 86400, 1) if ts else 0,
        })
        row.update({k: round(v, 3) for k, v in metrics.profit_shares(pos).items()})
        if row["roi_equal"] <= config.MIN_ROI_EQUAL:
            reasons.append("roi<=0")
        if row["share_entry_ge90"] > config.MAX_SHARE_ENTRY_GE_90:
            reasons.append("entries>=0.90")
        if row["profit_share_lt10"] > config.MAX_PROFIT_SHARE_LT_10:
            reasons.append("profit_from<0.10")
        if row["profit_share_top1"] > config.MAX_PROFIT_SHARE_TOP1:
            reasons.append("top1_concentration")
        if row["short_crypto_share"] > config.MAX_SHORT_CRYPTO_SHARE:
            reasons.append("short_crypto")
        if not meta["cutoff"] and row["history_days"] < config.MIN_HISTORY_DAYS:
            reasons.append(f"history<{config.MIN_HISTORY_DAYS}d")
    row["open_now"] = len({o.get("conditionId") for o in live})
    row["open_total"] = meta["open_total"]
    if row["open_now"] > config.MAX_OPEN_NOW:
        reasons.append(f"open_now>{config.MAX_OPEN_NOW}")
    row["pass"] = not reasons
    row["fail_reasons"] = ";".join(reasons)
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--wallets", nargs="*", help="проверить конкретные адреса")
    args = ap.parse_args()

    if args.wallets:
        items = [(w, "") for w in args.wallets]
    else:
        with open(IN) as f:
            data = json.load(f)["wallets"]
        # сначала те, у кого сегодня не только 5-минутная крипта
        items = sorted(data.items(), key=lambda kv: (kv[1]["short_crypto_share"] >= 0.999, -kv[1]["trades"]))
        items = [(w, d.get("name", "")) for w, d in items if d["short_crypto_share"] < 0.999]
        if args.limit:
            items = items[: args.limit]
    print(f"стадия 1: {len(items)} кошельков", file=sys.stderr)
    rows = api.pmap(lambda it: screen(*it), items, workers=args.workers, desc="stage1")
    rows = [r for r in rows if r]
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    passed = [r for r in rows if r["pass"]]
    print(f"прошли стадию 1: {len(passed)} из {len(rows)}; {OUT}", file=sys.stderr)
    from collections import Counter
    c = Counter(x for r in rows for x in r["fail_reasons"].split(";") if x)
    for k, v in c.most_common():
        print(f"  {k}: {v}", file=sys.stderr)


if __name__ == "__main__":
    main()
