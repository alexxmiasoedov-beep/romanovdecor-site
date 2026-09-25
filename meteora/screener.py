#!/usr/bin/env python3
"""
Скринер мем-пулов Meteora DLMM.

Тянет пулы с dlmm.datapi.meteora.ag (отсортированные по объёму за час),
дотягивает данные по токену с DexScreener (капитализация, возраст,
сделки) и Rugcheck (mint/freeze authority, топ-держатели, инсайдеры),
прогоняет через пороги из CONFIG и печатает таблицу кандидатов.

Только стандартная библиотека Python 3.8+. Запуск:

    python3 screener.py                 # разовый прогон
    python3 screener.py --watch 300     # повторять каждые 5 минут
    python3 screener.py --no-rugcheck   # быстрее, без проверки держателей
    python3 screener.py --all           # показать и отсеянные с причиной
    python3 screener.py --csv cand.csv  # дописывать кандидатов в CSV
    python3 screener.py --json          # вывод в JSON (для своих скриптов)

Пороги можно менять прямо в CONFIG или через флаги, см. --help.
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Пороги стратегии. Это стартовые значения, их надо подкручивать по журналу.
# ---------------------------------------------------------------------------
CONFIG = {
    # --- пул (Meteora) ---
    "min_fee_tvl_1h": 0.01,        # комиссия за 1ч / TVL, доля (0.01 = 1%)
    "min_vol_tvl_1h": 1.0,         # объём за 1ч / TVL
    "min_tvl_usd": 30_000,
    "max_tvl_usd": 500_000,
    "max_vol_drop": 0.30,          # объём 1ч не ниже (1 - 0.30) от прошлого часа
    "bin_step_min": 80,
    "bin_step_max": 250,
    "base_fee_min_pct": 1.0,       # базовая комиссия пула, %
    "base_fee_max_pct": 5.0,
    "quote_mints": {               # пары только против SOL/USDC
        "So11111111111111111111111111111111111111112": "SOL",
        "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v": "USDC",
    },
    # --- токен (DexScreener) ---
    "min_mcap_usd": 1_000_000,
    "max_mcap_usd": 30_000_000,
    "min_age_min": 30,
    "max_age_min": 12 * 60,
    "min_txns_1h": 600,            # сделок за час по всем DEX (прокси числа трейдеров)
    # --- держатели (Rugcheck) ---
    "max_top10_pct": 30.0,
    "max_insiders_pct": 20.0,
    "require_no_mint_authority": True,
    "require_no_freeze_authority": True,
    # --- сбор данных ---
    "pages": 3,                    # страниц по 100 пулов с Meteora (по объёму 1ч)
    "http_timeout": 20,
    "rugcheck_pause": 0.4,         # пауза между запросами к Rugcheck, сек
}

METEORA_URL = "https://dlmm.datapi.meteora.ag/pools"
DEXSCREENER_URL = "https://api.dexscreener.com/tokens/v1/solana/"
RUGCHECK_URL = "https://api.rugcheck.xyz/v1/tokens/{mint}/report"
UA = "meteora-screener/1.0"


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------
def get_json(url, timeout, retries=3):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            if isinstance(e, urllib.error.HTTPError) and e.code in (400, 404):
                return None
            time.sleep(1.5 * (attempt + 1))
    sys.stderr.write(f"[warn] {url[:90]}... : {last}\n")
    return None


# ---------------------------------------------------------------------------
# Сбор данных
# ---------------------------------------------------------------------------
def fetch_meteora_pools(cfg):
    pools = []
    for page in range(1, cfg["pages"] + 1):
        q = urllib.parse.urlencode({"page": page, "page_size": 100, "sort_by": "volume_1h:desc"})
        data = get_json(f"{METEORA_URL}?{q}", cfg["http_timeout"])
        if not data or not data.get("data"):
            break
        pools.extend(data["data"])
    return pools


def fetch_dexscreener(mints, cfg):
    """Возвращает {mint: {mcap, age_min, txns_1h, vol_1h_all, price, pairs}}"""
    out = {}
    mints = list(dict.fromkeys(mints))
    for i in range(0, len(mints), 30):
        chunk = mints[i:i + 30]
        data = get_json(DEXSCREENER_URL + ",".join(chunk), cfg["http_timeout"])
        if not data:
            continue
        by_mint = {}
        for p in data:
            base = (p.get("baseToken") or {}).get("address")
            if base:
                by_mint.setdefault(base, []).append(p)
        now_ms = time.time() * 1000
        for mint, pairs in by_mint.items():
            mcap = max((p.get("marketCap") or p.get("fdv") or 0) for p in pairs)
            created = [p.get("pairCreatedAt") for p in pairs if p.get("pairCreatedAt")]
            age_min = (now_ms - min(created)) / 60000 if created else None
            txns_1h = sum(((p.get("txns") or {}).get("h1") or {}).get("buys", 0)
                          + ((p.get("txns") or {}).get("h1") or {}).get("sells", 0) for p in pairs)
            vol_1h = sum((p.get("volume") or {}).get("h1", 0) or 0 for p in pairs)
            vol_6h = sum((p.get("volume") or {}).get("h6", 0) or 0 for p in pairs)
            price = max((float(p.get("priceUsd") or 0) for p in pairs), default=0)
            out[mint] = {
                "mcap": mcap, "age_min": age_min, "txns_1h": txns_1h,
                "vol_1h_all": vol_1h, "vol_6h_all": vol_6h, "price": price,
                "pairs": len(pairs),
            }
        if i + 30 < len(mints):
            time.sleep(0.3)
    return out


def fetch_rugcheck(mint, cfg):
    data = get_json(RUGCHECK_URL.format(mint=mint), cfg["http_timeout"], retries=2)
    if not data:
        return None
    holders = data.get("topHolders") or []
    # Rugcheck помечает пулы ликвидности/known accounts; исключаем их из топ-10
    known = data.get("knownAccounts") or {}
    real = [h for h in holders if h.get("owner") not in known and h.get("address") not in known]
    top10 = sum(h.get("pct", 0) for h in real[:10])
    insiders = sum(h.get("pct", 0) for h in real if h.get("insider"))
    risks = [r.get("name") for r in (data.get("risks") or []) if r.get("level") == "danger"]
    return {
        "mint_authority": data.get("mintAuthority"),
        "freeze_authority": data.get("freezeAuthority"),
        "top10_pct": top10,
        "insiders_pct": insiders,
        "insider_networks": data.get("graphInsidersDetected") or 0,
        "danger_risks": risks,
        "rugged": bool(data.get("rugged")),
        "score": data.get("score_normalised"),
        "holders": data.get("totalHolders"),
    }


# ---------------------------------------------------------------------------
# Фильтры
# ---------------------------------------------------------------------------
def pool_stage(p, cfg):
    """Дешёвая проверка по данным Meteora. Возвращает (row, reasons)."""
    reasons = []
    tx, ty = p.get("token_x") or {}, p.get("token_y") or {}
    quotes = cfg["quote_mints"]
    if ty.get("address") in quotes:
        meme, quote = tx, ty
    elif tx.get("address") in quotes:
        meme, quote = ty, tx
    else:
        return None, ["пара не против SOL/USDC"]
    if meme.get("address") in quotes:
        return None, ["обе стороны SOL/USDC"]

    pc = p.get("pool_config") or {}
    tvl = float(p.get("tvl") or 0)
    vol = p.get("volume") or {}
    fees = p.get("fees") or {}
    v1 = float(vol.get("1h") or 0)
    v2 = float(vol.get("2h") or 0)
    f1 = float(fees.get("1h") or 0)
    prev_hour = max(v2 - v1, 0.0)
    fee_tvl = f1 / tvl if tvl > 0 else 0
    vol_tvl = v1 / tvl if tvl > 0 else 0
    vol_trend = (v1 / prev_hour) if prev_hour > 0 else (9.99 if v1 > 0 else 0)

    row = {
        "pool": p.get("address"), "name": p.get("name"),
        "meme_mint": meme.get("address"), "symbol": meme.get("symbol"),
        "quote": quotes.get(quote.get("address")),
        "tvl": tvl, "vol_1h": v1, "vol_prev_h": prev_hour, "fees_1h": f1,
        "fee_tvl_1h": fee_tvl, "vol_tvl_1h": vol_tvl, "vol_trend": vol_trend,
        "bin_step": pc.get("bin_step"), "base_fee_pct": pc.get("base_fee_pct"),
        "dyn_fee_pct": p.get("dynamic_fee_pct"),
        "pool_age_min": (time.time() * 1000 - (p.get("created_at") or 0)) / 60000 if p.get("created_at") else None,
        "launchpad": p.get("launchpad") or "",
        "blacklisted": bool(p.get("is_blacklisted")),
        "price": p.get("current_price"),
    }

    if row["blacklisted"]:
        reasons.append("пул в чёрном списке Meteora")
    if tvl < cfg["min_tvl_usd"]:
        reasons.append(f"TVL {tvl:,.0f} < {cfg['min_tvl_usd']:,}")
    if tvl > cfg["max_tvl_usd"]:
        reasons.append(f"TVL {tvl:,.0f} > {cfg['max_tvl_usd']:,}")
    if fee_tvl < cfg["min_fee_tvl_1h"]:
        reasons.append(f"fee/TVL 1ч {fee_tvl*100:.2f}% < {cfg['min_fee_tvl_1h']*100:.1f}%")
    if vol_tvl < cfg["min_vol_tvl_1h"]:
        reasons.append(f"vol/TVL 1ч {vol_tvl:.2f} < {cfg['min_vol_tvl_1h']}")
    if prev_hour > 0 and v1 < prev_hour * (1 - cfg["max_vol_drop"]):
        reasons.append(f"объём падает: {v1:,.0f} vs {prev_hour:,.0f} прошлый час")
    bs = pc.get("bin_step") or 0
    if not (cfg["bin_step_min"] <= bs <= cfg["bin_step_max"]):
        reasons.append(f"bin step {bs} вне {cfg['bin_step_min']}-{cfg['bin_step_max']}")
    bf = float(pc.get("base_fee_pct") or 0)
    if not (cfg["base_fee_min_pct"] <= bf <= cfg["base_fee_max_pct"]):
        reasons.append(f"базовая комиссия {bf}% вне {cfg['base_fee_min_pct']}-{cfg['base_fee_max_pct']}%")
    return row, reasons


def token_stage(row, ds, cfg):
    reasons = []
    if ds is None:
        return ["DexScreener: нет данных по токену"]
    row.update({"mcap": ds["mcap"], "age_min": ds["age_min"], "txns_1h": ds["txns_1h"],
                "vol_1h_all_dex": ds["vol_1h_all"], "dex_pairs": ds["pairs"]})
    if ds["mcap"] < cfg["min_mcap_usd"]:
        reasons.append(f"mcap {ds['mcap']:,.0f} < {cfg['min_mcap_usd']:,}")
    if ds["mcap"] > cfg["max_mcap_usd"]:
        reasons.append(f"mcap {ds['mcap']:,.0f} > {cfg['max_mcap_usd']:,}")
    if ds["age_min"] is None:
        reasons.append("возраст токена неизвестен")
    else:
        if ds["age_min"] < cfg["min_age_min"]:
            reasons.append(f"возраст {ds['age_min']:.0f} мин < {cfg['min_age_min']}")
        if ds["age_min"] > cfg["max_age_min"]:
            reasons.append(f"возраст {ds['age_min']/60:.1f} ч > {cfg['max_age_min']/60:.0f} ч")
    if ds["txns_1h"] < cfg["min_txns_1h"]:
        reasons.append(f"сделок за 1ч {ds['txns_1h']} < {cfg['min_txns_1h']}")
    return reasons


def holders_stage(row, rc, cfg):
    reasons = []
    if rc is None:
        row["rugcheck"] = "нет данных"
        return ["Rugcheck: нет данных"]
    row.update({"top10_pct": rc["top10_pct"], "insiders_pct": rc["insiders_pct"],
                "mint_auth": bool(rc["mint_authority"]), "freeze_auth": bool(rc["freeze_authority"]),
                "rc_score": rc["score"], "holders": rc["holders"], "danger_risks": rc["danger_risks"]})
    if rc["rugged"]:
        reasons.append("Rugcheck: rugged")
    if cfg["require_no_mint_authority"] and rc["mint_authority"]:
        reasons.append("mint authority не отозвана")
    if cfg["require_no_freeze_authority"] and rc["freeze_authority"]:
        reasons.append("freeze authority не отозвана")
    if rc["top10_pct"] > cfg["max_top10_pct"]:
        reasons.append(f"топ-10 держателей {rc['top10_pct']:.1f}% > {cfg['max_top10_pct']}%")
    if rc["insiders_pct"] > cfg["max_insiders_pct"]:
        reasons.append(f"инсайдеры {rc['insiders_pct']:.1f}% > {cfg['max_insiders_pct']}%")
    if rc["danger_risks"]:
        reasons.append("Rugcheck danger: " + ", ".join(rc["danger_risks"]))
    return reasons


# ---------------------------------------------------------------------------
# Основной прогон
# ---------------------------------------------------------------------------
def run(cfg, use_rugcheck=True, show_all=False):
    t0 = time.time()
    pools = fetch_meteora_pools(cfg)
    stage1, rejected = [], []
    for p in pools:
        row, reasons = pool_stage(p, cfg)
        if row is None:
            continue
        if reasons:
            rejected.append((row, reasons))
        else:
            stage1.append(row)

    ds = fetch_dexscreener([r["meme_mint"] for r in stage1], cfg) if stage1 else {}
    stage2 = []
    for row in stage1:
        reasons = token_stage(row, ds.get(row["meme_mint"]), cfg)
        if reasons:
            rejected.append((row, reasons))
        else:
            stage2.append(row)

    candidates = []
    for row in stage2:
        if use_rugcheck:
            rc = fetch_rugcheck(row["meme_mint"], cfg)
            time.sleep(cfg["rugcheck_pause"])
            reasons = holders_stage(row, rc, cfg)
        else:
            reasons = []
            row["rugcheck"] = "пропущен"
        if reasons:
            rejected.append((row, reasons))
        else:
            candidates.append(row)

    candidates.sort(key=lambda r: r["fee_tvl_1h"], reverse=True)
    stats = {"pools_total": len(pools), "after_pool_stage": len(stage1),
             "after_token_stage": len(stage2), "candidates": len(candidates),
             "seconds": round(time.time() - t0, 1)}
    return candidates, rejected, stats


def fmt_usd(v):
    if v is None:
        return "-"
    if v >= 1_000_000:
        return f"{v/1_000_000:.2f}M"
    if v >= 1_000:
        return f"{v/1_000:.0f}k"
    return f"{v:.0f}"


def print_table(cands, stats, cfg):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n=== Meteora DLMM скринер, {now} ===")
    print(f"пулов просмотрено {stats['pools_total']}, прошли фильтр пула {stats['after_pool_stage']}, "
          f"фильтр токена {stats['after_token_stage']}, кандидатов {stats['candidates']} "
          f"({stats['seconds']} с)\n")
    if not cands:
        print("Кандидатов нет. Это нормальное состояние: в тихие часы правильное действие — ничего не открывать.")
        return
    hdr = f"{'токен':<10}{'пара':<6}{'TVL':>7}{'fee/TVL1h':>10}{'vol/TVL':>8}{'тренд':>6}{'bin':>5}{'fee%':>5}" \
          f"{'mcap':>8}{'возр':>6}{'сдел1h':>7}{'top10':>6}{'инс':>5}  пул"
    print(hdr)
    print("-" * len(hdr))
    for r in cands:
        age = r.get("age_min")
        age_s = f"{age/60:.1f}ч" if age is not None else "-"
        top10 = r.get("top10_pct")
        ins = r.get("insiders_pct")
        print(f"{(r['symbol'] or '')[:9]:<10}{r['quote']:<6}{fmt_usd(r['tvl']):>7}{r['fee_tvl_1h']*100:>9.2f}%"
              f"{r['vol_tvl_1h']:>8.2f}{r['vol_trend']:>6.2f}{r['bin_step']:>5}{r['base_fee_pct']:>5.1f}"
              f"{fmt_usd(r.get('mcap')):>8}{age_s:>6}{r.get('txns_1h', 0):>7}"
              f"{(f'{top10:.0f}%' if top10 is not None else '-'):>6}{(f'{ins:.0f}%' if ins is not None else '-'):>5}"
              f"  https://app.meteora.ag/dlmm/{r['pool']}")
    print("\nПеред входом: глянуть Bubblemaps по минту и график на DexScreener. "
          "Вход односторонний в SOL/USDC ниже цены, 10–20 бинов, Bid-Ask. "
          "Выход: 2–4 ч, или 15–25% комиссии от позиции, или цена ниже диапазона, или объём упал вдвое за 30 мин.")


def print_rejected(rejected, limit=40):
    # показываем самые «почти прошедшие»: у кого меньше причин и выше комиссия
    rejected = sorted(rejected, key=lambda x: (len(x[1]), -x[0]["fee_tvl_1h"]))[:limit]
    print(f"\n--- отсеянные (первые {len(rejected)}, ближайшие к порогам) ---")
    for row, reasons in rejected:
        print(f"{(row['symbol'] or '?')[:10]:<11} TVL {fmt_usd(row['tvl']):>6} fee/TVL {row['fee_tvl_1h']*100:5.2f}%  |  "
              + "; ".join(reasons))


def append_csv(path, cands):
    fields = ["scan_time_utc", "symbol", "quote", "pool", "meme_mint", "tvl", "fee_tvl_1h", "vol_tvl_1h",
              "vol_1h", "vol_prev_h", "vol_trend", "bin_step", "base_fee_pct", "mcap", "age_min",
              "txns_1h", "top10_pct", "insiders_pct", "rc_score", "holders", "launchpad", "price"]
    new = not os.path.exists(path)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new:
            w.writeheader()
        for r in cands:
            w.writerow({**r, "scan_time_utc": now})


def main():
    ap = argparse.ArgumentParser(description="Скринер мем-пулов Meteora DLMM")
    ap.add_argument("--watch", type=int, metavar="SEC", help="повторять каждые SEC секунд")
    ap.add_argument("--no-rugcheck", action="store_true", help="не проверять держателей через Rugcheck")
    ap.add_argument("--all", action="store_true", help="показать и отсеянные пулы с причинами")
    ap.add_argument("--csv", metavar="FILE", help="дописывать кандидатов в CSV")
    ap.add_argument("--json", action="store_true", help="печатать кандидатов как JSON")
    ap.add_argument("--pages", type=int, help="страниц по 100 пулов с Meteora (по умолчанию 3)")
    ap.add_argument("--min-fee-tvl", type=float, help="минимум fee/TVL за 1ч, в %% (по умолчанию 1)")
    ap.add_argument("--min-tvl", type=float, help="минимальный TVL пула, $")
    ap.add_argument("--max-tvl", type=float, help="максимальный TVL пула, $")
    ap.add_argument("--min-mcap", type=float, help="минимальная капитализация, $")
    ap.add_argument("--max-mcap", type=float, help="максимальная капитализация, $")
    ap.add_argument("--max-age", type=float, help="максимальный возраст токена, часов")
    ap.add_argument("--min-txns", type=int, help="минимум сделок за час")
    args = ap.parse_args()

    cfg = dict(CONFIG)
    if args.pages: cfg["pages"] = args.pages
    if args.min_fee_tvl is not None: cfg["min_fee_tvl_1h"] = args.min_fee_tvl / 100
    if args.min_tvl is not None: cfg["min_tvl_usd"] = args.min_tvl
    if args.max_tvl is not None: cfg["max_tvl_usd"] = args.max_tvl
    if args.min_mcap is not None: cfg["min_mcap_usd"] = args.min_mcap
    if args.max_mcap is not None: cfg["max_mcap_usd"] = args.max_mcap
    if args.max_age is not None: cfg["max_age_min"] = args.max_age * 60
    if args.min_txns is not None: cfg["min_txns_1h"] = args.min_txns

    while True:
        cands, rejected, stats = run(cfg, use_rugcheck=not args.no_rugcheck, show_all=args.all)
        if args.json:
            print(json.dumps({"stats": stats, "candidates": cands}, ensure_ascii=False, indent=1, default=str))
        else:
            print_table(cands, stats, cfg)
            if args.all:
                print_rejected(rejected)
        if args.csv and cands:
            append_csv(args.csv, cands)
        if not args.watch:
            break
        try:
            time.sleep(args.watch)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
