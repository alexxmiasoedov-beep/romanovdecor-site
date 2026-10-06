"""Стадия 0. Собрать адреса кошельков, торговавших сегодня.

Источники:
  1. Глобальная лента сделок Data API (offset ≤ 10 000) на нескольких порогах
     минимальной суммы сделки — так лента покрывает больший интервал времени.
  2. Сделки по самым оборотистым рынкам за сутки (Gamma top events → Data API /trades?market=).

Результат: data/wallets_today.json  {wallet: {...агрегаты по сегодняшним сделкам...}}
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

from pm import api, config

OUT = os.path.join(os.path.dirname(__file__), "data", "wallets_today.json")


def is_short_crypto(title: str, slug: str) -> bool:
    s = (title or "") + " " + (slug or "")
    return any(p.lower() in s.lower() for p in config.SHORT_CRYPTO_PATTERNS)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=float, default=None,
                    help="часов назад (по умолчанию — с 00:00 UTC сегодня; пайплайн передаёт 24)")
    # глубина ленты ≤ 10 000 сделок на порог: ≥$0 это ~20 мин, ≥$200 ~5 ч, ≥$1000 ~сутки.
    # Промежуточные пороги дают мелкие сделки за больший интервал; дубли отсеиваются по tx.
    ap.add_argument("--thresholds", default="0,10,25,50,100,150,200,300,500,750,1000,2000,5000")
    ap.add_argument("--events", type=int, default=300, help="сколько топ-событий по обороту обойти")
    ap.add_argument("--markets-per-event", type=int, default=6)
    ap.add_argument("--deep-pages", type=int, default=20,
                    help="страниц ленты (по 500) для рынков с оборотом ≥ --deep-volume; потолок API — 20")
    ap.add_argument("--deep-volume", type=float, default=100_000)
    ap.add_argument("--mid-pages", type=int, default=8, help="страниц для рынков с оборотом ≥ 20 000")
    args = ap.parse_args()

    now = time.time()
    if args.since:
        since = now - args.since * 3600
    else:
        since = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    print(f"собираем сделки с {datetime.fromtimestamp(since, timezone.utc):%Y-%m-%d %H:%M} UTC", file=sys.stderr)

    seen_tx: set[str] = set()
    W: dict[str, dict] = defaultdict(lambda: {"trades": 0, "cash": 0.0, "markets": set(), "short_crypto": 0,
                                              "first_ts": 1e12, "last_ts": 0, "name": "", "titles": set()})

    def absorb(trades: list[dict]) -> int:
        n = 0
        for t in trades:
            ts = t.get("timestamp", 0)
            if ts < since:
                continue
            key = (t.get("transactionHash", "") + t.get("asset", "") + str(t.get("proxyWallet")))
            if key in seen_tx:
                continue
            seen_tx.add(key)
            w = W[t["proxyWallet"]]
            w["trades"] += 1
            w["cash"] += float(t.get("price", 0)) * float(t.get("size", 0))
            w["markets"].add(t.get("conditionId"))
            w["first_ts"] = min(w["first_ts"], ts)
            w["last_ts"] = max(w["last_ts"], ts)
            w["name"] = t.get("name") or t.get("pseudonym") or w["name"]
            if is_short_crypto(t.get("title", ""), t.get("slug", "")):
                w["short_crypto"] += 1
            elif len(w["titles"]) < 5:
                w["titles"].add(t.get("title", ""))
            n += 1
        return n

    # 1. глобальная лента на разных порогах суммы
    for thr in [float(x) for x in args.thresholds.split(",")]:
        got = 0
        for off in range(0, 10001, 500):
            chunk = api.trades_global(500, off, min_cash=thr or None)
            if not chunk:
                break
            got += absorb(chunk)
            if chunk[-1].get("timestamp", 0) < since:
                break
        print(f"лента ≥${thr:g}: +{got} сделок, кошельков всего {len(W)}", file=sys.stderr)

    # 2. топ-события за сутки → сделки по их рынкам
    events = api.top_events(args.events)
    # глубина по обороту: на живом спорте 1000 сделок = минуты, на политике = сутки; листаем до `since`
    jobs = []
    for ev in events:
        ms = [m for m in ev.get("markets", []) if not is_short_crypto(m.get("question", ""), m.get("slug", ""))]
        ms.sort(key=lambda m: float(m.get("volume24hr") or 0), reverse=True)
        for m in ms[: args.markets_per_event]:
            v = float(m.get("volume24hr") or 0)
            if v > 1000 and m.get("conditionId"):
                pages = args.deep_pages if v >= args.deep_volume else args.mid_pages if v >= 20_000 else 2
                jobs.append((m["conditionId"], pages))
    deep = sum(1 for _, p in jobs if p == args.deep_pages)
    print(f"рынков для обхода: {len(jobs)}, из них глубоких ({args.deep_pages} стр.): {deep}", file=sys.stderr)
    res = api.pmap(lambda j: api.trades_market(j[0], max_pages=j[1], since=since), jobs, workers=8,
                   desc="market trades")
    got = sum(absorb(r or []) for r in res)
    print(f"по рынкам: +{got} сделок, кошельков всего {len(W)}", file=sys.stderr)

    out = {}
    for w, d in W.items():
        out[w] = {**d, "markets": len(d["markets"]), "titles": sorted(d["titles"]),
                  "short_crypto_share": round(d["short_crypto"] / max(d["trades"], 1), 3)}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump({"since": since, "collected_at": now, "wallets": out}, f, ensure_ascii=False)
    only_sc = sum(1 for d in out.values() if d["short_crypto_share"] >= 0.999)
    print(f"итого кошельков: {len(out)}, из них только 5-мин крипта: {only_sc}; записано {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
