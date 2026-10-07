"""Стадия 0. Собрать адреса кошельков, торговавших сегодня.

Источники:
  1. Глобальная лента сделок Data API (offset ≤ 10 000) на нескольких порогах
     минимальной суммы сделки — так лента покрывает больший интервал времени.
  2. Сделки по самым оборотистым рынкам за сутки (Gamma top events → Data API /trades?market=).
  3. Держатели позиций по тем же рынкам (Data API /holders — до 100 крупнейших на каждый исход):
     ловит тех, кто купил дни назад и из ленты уже выпал.
  4. Таблица лидеров (Data API /v1/leaderboard): окна 1d/7d/30d × по прибыли и по обороту, по 1000 адресов.

Результат: data/wallets_today.json  {wallet: {...агрегаты по сделкам за окно...}, tx_keys: [...]}
Вечерний снимок: `--since 12 --out data/wallets_evening.json` (17:00 UTC); утренний прогон вливает его
через `--merge data/wallets_evening.json` — на живых рынках лента глубже 10 000 сделок не достаёт,
и дневные сделки к 05:00 UTC иначе теряются.
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
    ap.add_argument("--holders", type=int, default=100, help="держателей на исход рынка (0 — не собирать)")
    ap.add_argument("--leaderboard", type=int, default=1000, help="адресов из таблицы лидеров на окно (0 — не собирать)")
    ap.add_argument("--out", default=OUT, help="куда писать (вечерний снимок — data/wallets_evening.json)")
    ap.add_argument("--merge", default=None,
                    help="влить снимок (например, вечерний): его сделки не считаются дважды, кошельки объединяются")
    args = ap.parse_args()

    now = time.time()
    if args.since:
        since = now - args.since * 3600
    else:
        since = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    print(f"собираем сделки с {datetime.fromtimestamp(since, timezone.utc):%Y-%m-%d %H:%M} UTC", file=sys.stderr)

    seen_tx: set[str] = set()
    W: dict[str, dict] = defaultdict(lambda: {"trades": 0, "cash": 0.0, "markets": set(), "short_crypto": 0,
                                              "first_ts": 1e12, "last_ts": 0, "name": "", "titles": set(),
                                              "holdings": 0, "holdings_crypto": 0, "held_usd": 0.0, "lb": {}})
    merged = None
    if args.merge and os.path.exists(args.merge):
        with open(args.merge) as f:
            merged = json.load(f)
        if merged.get("since", 0) >= since - 3600:  # снимок внутри нашего окна — его сделки пропускаем
            seen_tx.update(merged.get("tx_keys", []))
            print(f"вливаем {args.merge}: {len(merged['wallets'])} кошельков, {len(merged.get('tx_keys', []))} сделок",
                  file=sys.stderr)
        else:
            print(f"снимок {args.merge} устарел (since {merged.get('since')}), пропускаем", file=sys.stderr)
            merged = None

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
    jobs = []; minfo = {}
    for ev in events:
        ms = [m for m in ev.get("markets", []) if not is_short_crypto(m.get("question", ""), m.get("slug", ""))]
        ms.sort(key=lambda m: float(m.get("volume24hr") or 0), reverse=True)
        for m in ms[: args.markets_per_event]:
            v = float(m.get("volume24hr") or 0)
            if v > 1000 and m.get("conditionId"):
                pages = args.deep_pages if v >= args.deep_volume else args.mid_pages if v >= 20_000 else 2
                jobs.append((m["conditionId"], pages))
                try:
                    prices = [float(x) for x in json.loads(m.get("outcomePrices") or "[]")]
                except (ValueError, TypeError):
                    prices = []
                minfo[m["conditionId"]] = {"title": m.get("question", ""), "slug": m.get("slug", ""), "prices": prices}
    deep = sum(1 for _, p in jobs if p == args.deep_pages)
    print(f"рынков для обхода: {len(jobs)}, из них глубоких ({args.deep_pages} стр.): {deep}", file=sys.stderr)
    res = api.pmap(lambda j: api.trades_market(j[0], max_pages=j[1], since=since), jobs, workers=8,
                   desc="market trades")
    got = sum(absorb(r or []) for r in res)
    print(f"по рынкам: +{got} сделок, кошельков всего {len(W)}", file=sys.stderr)

    # 3. держатели позиций по тем же рынкам
    if args.holders:
        def holders(cid):
            return cid, (api.get(f"{api.DATA}/holders", {"market": cid, "limit": args.holders}, cache=False) or [])
        res = api.pmap(holders, [cid for cid, _ in jobs], workers=8, desc="holders")
        n = 0
        for r in res:
            if not r:
                continue
            cid, toks = r; info = minfo.get(cid, {})
            crypto = is_short_crypto(info.get("title", ""), info.get("slug", ""))
            for tok in toks:
                for h in tok.get("holders", []):
                    wallet = h.get("proxyWallet")
                    amt = float(h.get("amount") or 0)
                    if not wallet or amt <= 0:
                        continue
                    oi = int(h.get("outcomeIndex") or 0); prices = info.get("prices") or []
                    w = W[wallet]
                    w["holdings"] += 1; w["holdings_crypto"] += int(crypto)
                    w["held_usd"] += amt * (prices[oi] if oi < len(prices) else 0.5)
                    w["markets"].add(cid); w["last_ts"] = max(w["last_ts"], now); w["first_ts"] = min(w["first_ts"], now)
                    w["name"] = w["name"] or h.get("name") or h.get("pseudonym") or ""
                    if not crypto and len(w["titles"]) < 5:
                        w["titles"].add(info.get("title", ""))
                    n += 1
        print(f"держатели: +{n} позиций, кошельков всего {len(W)}", file=sys.stderr)

    # 4. таблица лидеров
    if args.leaderboard:
        n = 0
        for window in ("1d", "7d", "30d"):
            for order in ("PNL", "VOL"):
                for off in range(0, args.leaderboard, 50):
                    page = api.get(f"{api.DATA}/v1/leaderboard", {"window": window, "limit": 50, "offset": off, "orderBy": order},
                                   cache=False) or []
                    for e in page:
                        wallet = e.get("proxyWallet")
                        if not wallet:
                            continue
                        w = W[wallet]
                        w["lb"][f"{window}_{order}"] = int(e.get("rank") or 0)
                        w["lb"][f"{window}_pnl"] = round(float(e.get("pnl") or 0), 2); w["lb"][f"{window}_vol"] = round(float(e.get("vol") or 0), 2)
                        w["last_ts"] = max(w["last_ts"], now); w["first_ts"] = min(w["first_ts"], now)
                        w["name"] = w["name"] or e.get("userName") or ""
                        n += 1
                    if len(page) < 50:
                        break
        print(f"лидеры: +{n} записей, кошельков всего {len(W)}", file=sys.stderr)

    if merged:
        for w, d in merged["wallets"].items():
            if d.get("last_ts", 0) < since:
                continue
            x = W[w]
            x["trades"] += d["trades"]; x["cash"] += d["cash"]; x["short_crypto"] += d["short_crypto"]
            x["holdings"] = max(x["holdings"], d.get("holdings", 0)); x["holdings_crypto"] = max(x["holdings_crypto"], d.get("holdings_crypto", 0))
            x["held_usd"] = max(x["held_usd"], d.get("held_usd", 0.0)); x["lb"] = {**d.get("lb", {}), **x["lb"]}
            x["first_ts"] = min(x["first_ts"], d["first_ts"]); x["last_ts"] = max(x["last_ts"], d["last_ts"])
            x["name"] = x["name"] or d.get("name", "")
            x["markets"].update(d.get("market_ids", []))
            if isinstance(d.get("markets"), int) and not d.get("market_ids"):
                x["markets"].update(f"{w}#{i}" for i in range(d["markets"]))  # старый снимок без списка рынков
            for t in d.get("titles", []):
                if len(x["titles"]) < 5:
                    x["titles"].add(t)
        print(f"после слияния кошельков всего {len(W)}", file=sys.stderr)

    out = {}
    for w, d in W.items():
        out[w] = {**d, "markets": len(d["markets"]), "market_ids": sorted(x for x in d["markets"] if x),
                  "titles": sorted(d["titles"]),
                  "held_usd": round(d["held_usd"], 2),
                  "short_crypto_share": round((d["short_crypto"] + d["holdings_crypto"]) / max(d["trades"] + d["holdings"], 1), 3)}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump({"since": since, "collected_at": now, "wallets": out, "tx_keys": sorted(seen_tx)}, f,
                  ensure_ascii=False)
    only_sc = sum(1 for d in out.values() if d["short_crypto_share"] >= 0.999)
    print(f"итого кошельков: {len(out)}, из них только 5-мин крипта: {only_sc}; записано {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
