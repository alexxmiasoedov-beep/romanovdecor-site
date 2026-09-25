#!/usr/bin/env python3
"""
Paper-trading симуляция стратегии по мем-пулам Meteora DLMM.

Каждый тик: прогоняет скринер, открывает виртуальные позиции по
кандидатам, обновляет цену и комиссии по открытым позициям, закрывает
их по правилам выхода и пишет закрытые сделки в журнал (тот же формат,
что journal_template.csv). Никаких транзакций в сеть не отправляет.

    python3 simulate.py                          # профиль strategy, бесконечно
    python3 simulate.py --duration 180           # 3 часа и выход
    python3 simulate.py --profile relaxed        # ослабленные пороги (для набора данных)
    python3 simulate.py --once                   # один тик (проверка)

Состояние (капитал, открытые позиции) хранится в sim_<профиль>.json,
журнал в journal_<профиль>.csv, лог тиков в sim_<профиль>.log.
Остановить и запустить снова можно в любой момент, состояние подхватится.

Модель позиции (упрощённая, но с правильной формой кривой):
  односторонний депозит D в SOL/USDC, равномерно по цене от P_entry
  вниз до P_low = P_entry*(1 - bins*bin_step/10000).
  При цене P внутри диапазона доля (P_entry-P)/(P_entry-P_low) депозита
  сконвертирована в токен по средним ценам пройденных бинов; при
  P < P_low всё в токене. Ниже P_low позиция — это просто мешок токена.
  Комиссия за тик = комиссия пула за тик * D/(TVL+D), пока цена в
  диапазоне или в одном бине над ним; иначе 0.
Это оптимистично по комиссии (реальная зависит от распределения по
бинам) и не учитывает MEV-сэндвичи, поэтому итог симуляции — верхняя
оценка, а не обещание.
"""

import argparse
import csv
import json
import math
import os
import sys
import time
import urllib.parse
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screener  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

PROFILES = {
    # пороги как в стратегии (CONFIG скринера)
    "strategy": {},
    # ослабленные пороги: сделок больше, чтобы быстрее накопить журнал и
    # увидеть, от чего именно спасают строгие фильтры
    "relaxed": {
        "min_fee_tvl_1h": 0.005, "min_vol_tvl_1h": 0.5,
        "min_tvl_usd": 5_000, "max_tvl_usd": 1_000_000,
        "bin_step_min": 50, "base_fee_min_pct": 0.5,
        "min_mcap_usd": 300_000, "max_mcap_usd": 50_000_000,
        "min_age_min": 15, "max_age_min": 24 * 60,
        "min_txns_1h": 200, "max_top10_pct": 40.0, "max_insiders_pct": 30.0,
    },
}

SIM = {
    "capital_usd": 5_000.0,      # стартовый виртуальный капитал
    "position_pct": 0.03,        # размер позиции от капитала
    "max_positions": 4,
    "bins_below": 15,            # ширина диапазона в бинах ниже цены
    "max_hold_min": 180,         # выход по времени
    "fee_take_pct": 0.20,        # выход, когда комиссия >= 20% депозита
    "vol_drop_ratio": 0.5,       # выход, если объём 30м < 50% предыдущих 30м
    "vol_drop_min_hold": 20,     # правило объёма включается через N минут
    "daily_stop_pct": 0.10,      # дневной стоп: -10% капитала
    "cooldown_min": 360,         # не входить в тот же токен повторно N минут
    "gas_open_usd": 1.5,
    "gas_close_usd": 1.0,
    "slippage_base": 0.01,       # 1% на продаже токена + price impact
    "tick_sec": 120,
}

JOURNAL_FIELDS = ["id", "open_utc", "close_utc", "symbol", "quote", "pool", "meme_mint", "bin_step",
                  "base_fee_pct", "strategy", "bins_below", "deposit_sol", "sol_price_usd", "deposit_usd",
                  "tvl_entry", "fee_tvl_1h_entry", "vol_tvl_1h_entry", "vol_trend_entry", "mcap_entry",
                  "age_min_entry", "txns_1h_entry", "top10_pct_entry", "insiders_pct_entry", "price_entry",
                  "price_exit", "exit_reason", "fees_claimed_usd", "tokens_left_sold_usd",
                  "position_withdrawn_usd", "gas_usd", "slippage_usd", "net_pnl_usd", "net_pnl_pct",
                  "minutes_held", "notes"]


def now_utc():
    return datetime.now(timezone.utc)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M")


# ---------------------------------------------------------------------------
# модель позиции
# ---------------------------------------------------------------------------
def position_split(pos, price):
    """Возвращает (quote_usd_remaining, tokens) при цене price."""
    d, pe, pl = pos["deposit_usd"], pos["price_entry"], pos["price_low"]
    if price >= pe:
        return d, 0.0
    p = max(price, pl)
    frac = (pe - p) / (pe - pl)
    tokens = d / (pe - pl) * math.log(pe / p)
    return d * (1 - frac), tokens


def position_value(pos, price):
    q, t = position_split(pos, price)
    return q + t * price


def in_fee_zone(pos, price):
    one_bin = pos["bin_step"] / 10000
    return pos["price_low"] <= price <= pos["price_entry"] * (1 + one_bin)


# ---------------------------------------------------------------------------
# состояние
# ---------------------------------------------------------------------------
def load_state(path, cfg):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"capital": cfg["capital_usd"], "start_capital": cfg["capital_usd"], "open": [],
            "cooldown": {}, "day": None, "day_start_capital": cfg["capital_usd"],
            "next_id": 1, "closed": 0, "ticks": 0}


def save_state(path, st):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def append_journal(path, row):
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=JOURNAL_FIELDS, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow(row)


def log(path, msg):
    line = f"{iso(now_utc())} {msg}"
    print(line, flush=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# ---------------------------------------------------------------------------
# данные по открытым позициям
# ---------------------------------------------------------------------------
def fetch_pool(address, cfg):
    return screener.get_json(f"{screener.METEORA_URL}/{address}", cfg["http_timeout"], retries=2)


def fetch_prices(mints, cfg):
    ds = screener.fetch_dexscreener(mints, cfg) if mints else {}
    return {m: v["price"] for m, v in ds.items() if v.get("price")}


# ---------------------------------------------------------------------------
# открытие / закрытие
# ---------------------------------------------------------------------------
def open_position(st, cand, sim, cfg, logp):
    dep = round(st["capital"] * sim["position_pct"], 2)
    if dep < 10 or dep > st["capital"]:
        return None
    price = cand.get("price_usd") or 0
    if price <= 0:
        return None
    width = sim["bins_below"] * cand["bin_step"] / 10000
    pos = {
        "id": st["next_id"], "open_ts": time.time(), "open_utc": iso(now_utc()),
        "symbol": cand["symbol"], "quote": cand["quote"], "pool": cand["pool"], "meme_mint": cand["meme_mint"],
        "bin_step": cand["bin_step"], "base_fee_pct": cand["base_fee_pct"],
        "deposit_usd": dep, "price_entry": price, "price_low": price * (1 - width),
        "tvl_entry": cand["tvl"], "fee_tvl_1h_entry": cand["fee_tvl_1h"], "vol_tvl_1h_entry": cand["vol_tvl_1h"],
        "vol_trend_entry": cand["vol_trend"], "mcap_entry": cand.get("mcap"), "age_min_entry": cand.get("age_min"),
        "txns_1h_entry": cand.get("txns_1h"), "top10_pct_entry": cand.get("top10_pct"),
        "insiders_pct_entry": cand.get("insiders_pct"),
        "fees_usd": 0.0, "gas_usd": sim["gas_open_usd"], "last_fees_cum": None, "last_price": price,
        "min_price": price, "max_price": price,
    }
    st["next_id"] += 1
    st["capital"] -= dep + sim["gas_open_usd"]
    st["open"].append(pos)
    st["cooldown"][cand["meme_mint"]] = time.time()
    log(logp, f"OPEN #{pos['id']} {pos['symbol']}/{pos['quote']} dep ${dep} price {price:.6g} "
              f"range -{width*100:.1f}% tvl ${cand['tvl']:,.0f} fee/tvl1h {cand['fee_tvl_1h']*100:.2f}%")
    return pos


def close_position(st, pos, price, reason, sim, journal, logp, note=""):
    quote_left, tokens = position_split(pos, price)
    token_val = tokens * price
    tvl = pos.get("last_tvl") or pos["tvl_entry"]
    slippage = token_val * (sim["slippage_base"] + token_val / max(2 * tvl, 1)) if token_val > 0 else 0.0
    sold = token_val - slippage
    gas = pos["gas_usd"] + sim["gas_close_usd"]
    net = pos["fees_usd"] + sold + quote_left - pos["deposit_usd"] - gas
    minutes = (time.time() - pos["open_ts"]) / 60
    st["capital"] += pos["fees_usd"] + sold + quote_left - sim["gas_close_usd"]
    st["closed"] += 1
    row = {k: pos.get(k) for k in JOURNAL_FIELDS}
    row.update({
        "close_utc": iso(now_utc()), "strategy": "bidask", "bins_below": sim["bins_below"],
        "deposit_sol": "", "sol_price_usd": "", "price_exit": price, "exit_reason": reason,
        "fees_claimed_usd": round(pos["fees_usd"], 2), "tokens_left_sold_usd": round(sold, 2),
        "position_withdrawn_usd": round(quote_left, 2), "gas_usd": round(gas, 2), "slippage_usd": round(slippage, 2),
        "net_pnl_usd": round(net, 2), "net_pnl_pct": round(net / pos["deposit_usd"] * 100, 2),
        "minutes_held": round(minutes), "notes": f"sim; min {pos['min_price']:.4g} max {pos['max_price']:.4g}; {note}".strip("; "),
    })
    for k in ("tvl_entry", "mcap_entry", "age_min_entry", "top10_pct_entry", "insiders_pct_entry"):
        if isinstance(row.get(k), float):
            row[k] = round(row[k], 2)
    for k in ("fee_tvl_1h_entry", "vol_tvl_1h_entry", "vol_trend_entry"):
        if isinstance(row.get(k), float):
            row[k] = round(row[k], 4)
    append_journal(journal, row)
    st["open"] = [p for p in st["open"] if p["id"] != pos["id"]]
    log(logp, f"CLOSE #{pos['id']} {pos['symbol']} {reason} price {price:.6g} ({(price/pos['price_entry']-1)*100:+.1f}%) "
              f"fees ${pos['fees_usd']:.2f} net ${net:+.2f} ({net/pos['deposit_usd']*100:+.1f}%) {minutes:.0f} мин; "
              f"капитал ${st['capital'] + sum(position_value(p, p['last_price']) for p in st['open']):,.2f}")


# ---------------------------------------------------------------------------
# тик
# ---------------------------------------------------------------------------
def update_positions(st, sim, cfg, journal, logp):
    if not st["open"]:
        return
    prices = fetch_prices([p["meme_mint"] for p in st["open"]], cfg)
    for pos in list(st["open"]):
        pool = fetch_pool(pos["pool"], cfg)
        price = prices.get(pos["meme_mint"]) or pos["last_price"]
        if pool:
            fees = pool.get("fees") or {}
            vol = pool.get("volume") or {}
            tvl = float(pool.get("tvl") or pos["tvl_entry"])
            pos["last_tvl"] = tvl
            # комиссия пула за тик: берём из 30-минутного окна пропорционально
            fees_30m = float(fees.get("30m") or 0)
            dt = min(time.time() - pos.get("last_tick_ts", pos["open_ts"]), 1800)
            pool_fee_tick = fees_30m * dt / 1800
            if in_fee_zone(pos, price):
                share = pos["deposit_usd"] / (tvl + pos["deposit_usd"])
                pos["fees_usd"] += pool_fee_tick * share
            v30 = float(vol.get("30m") or 0)
            v1h = float(vol.get("1h") or 0)
            pos["vol_30m"], pos["vol_prev_30m"] = v30, max(v1h - v30, 0)
        pos["last_tick_ts"] = time.time()
        pos["last_price"] = price
        pos["min_price"] = min(pos["min_price"], price)
        pos["max_price"] = max(pos["max_price"], price)
        minutes = (time.time() - pos["open_ts"]) / 60

        reason = None
        if price < pos["price_low"]:
            reason = "price"
        elif pos["fees_usd"] >= sim["fee_take_pct"] * pos["deposit_usd"]:
            reason = "fee"
        elif minutes >= sim["max_hold_min"]:
            reason = "time"
        elif (minutes >= sim["vol_drop_min_hold"] and pos.get("vol_prev_30m", 0) > 0
              and pos.get("vol_30m", 0) < sim["vol_drop_ratio"] * pos["vol_prev_30m"]):
            reason = "volume"
        if reason:
            close_position(st, pos, price, reason, sim, journal, logp)


def maybe_open(st, sim, cfg, use_rugcheck, logp):
    today = now_utc().strftime("%Y-%m-%d")
    equity = st["capital"] + sum(position_value(p, p["last_price"]) for p in st["open"])
    if st["day"] != today:
        st["day"], st["day_start_capital"] = today, equity
    if equity < st["day_start_capital"] * (1 - sim["daily_stop_pct"]):
        log(logp, f"дневной стоп: equity ${equity:,.2f} < {st['day_start_capital']*(1-sim['daily_stop_pct']):,.2f}, новых входов сегодня нет")
        return 0
    if len(st["open"]) >= sim["max_positions"]:
        return 0
    cands, rejected, stats = screener.run(cfg, use_rugcheck=use_rugcheck)
    st["ticks"] += 1
    st["last_scan"] = {"time": iso(now_utc()), **stats}
    opened = 0
    open_mints = {p["meme_mint"] for p in st["open"]}
    for c in cands:
        if len(st["open"]) >= sim["max_positions"]:
            break
        m = c["meme_mint"]
        if m in open_mints:
            continue
        if time.time() - st["cooldown"].get(m, 0) < sim["cooldown_min"] * 60:
            continue
        # цена токена в USD c DexScreener (для позиции нужна одна и та же шкала на входе и выходе)
        c["price_usd"] = c.get("price_usd") or fetch_prices([m], cfg).get(m)
        if open_position(st, c, sim, cfg, logp):
            opened += 1
            open_mints.add(m)
    return opened


def status_line(st):
    eq = st["capital"] + sum(position_value(p, p["last_price"]) for p in st["open"])
    ls = st.get("last_scan") or {}
    return (f"tick {st['ticks']} equity ${eq:,.2f} ({(eq/st['start_capital']-1)*100:+.2f}%) "
            f"open {len(st['open'])} closed {st['closed']} | скан: пулов {ls.get('pools_total','-')} "
            f"stage1 {ls.get('after_pool_stage','-')} stage2 {ls.get('after_token_stage','-')} канд {ls.get('candidates','-')}")


def main():
    ap = argparse.ArgumentParser(description="Paper-trading симуляция стратегии Meteora DLMM")
    ap.add_argument("--profile", choices=list(PROFILES), default="strategy")
    ap.add_argument("--duration", type=int, metavar="MIN", help="остановиться через MIN минут")
    ap.add_argument("--tick", type=int, help=f"интервал тика, сек (по умолчанию {SIM['tick_sec']})")
    ap.add_argument("--once", action="store_true", help="один тик и выход")
    ap.add_argument("--no-rugcheck", action="store_true")
    ap.add_argument("--capital", type=float, help="стартовый капитал, $ (только для нового состояния)")
    ap.add_argument("--dir", default=HERE, help="куда писать журнал и состояние")
    args = ap.parse_args()

    sim = dict(SIM)
    if args.tick:
        sim["tick_sec"] = args.tick
    if args.capital:
        sim["capital_usd"] = args.capital
    cfg = dict(screener.CONFIG)
    cfg.update(PROFILES[args.profile])

    os.makedirs(args.dir, exist_ok=True)
    state_path = os.path.join(args.dir, f"sim_{args.profile}.json")
    journal = os.path.join(args.dir, f"journal_{args.profile}.csv")
    logp = os.path.join(args.dir, f"sim_{args.profile}.log")
    st = load_state(state_path, sim)
    log(logp, f"старт симуляции, профиль {args.profile}, капитал ${st['capital']:,.2f}, открыто {len(st['open'])}")

    t_end = time.time() + args.duration * 60 if args.duration else None
    while True:
        try:
            update_positions(st, sim, cfg, journal, logp)
            maybe_open(st, sim, cfg, not args.no_rugcheck, logp)
            save_state(state_path, st)
            log(logp, status_line(st))
        except Exception as e:  # сеть упала и т.п. — не ронять цикл
            log(logp, f"ошибка тика: {type(e).__name__}: {e}")
        if args.once or (t_end and time.time() >= t_end):
            break
        try:
            time.sleep(sim["tick_sec"])
        except KeyboardInterrupt:
            break
    # по окончании открытые позиции НЕ закрываем: при следующем запуске они продолжатся
    save_state(state_path, st)
    log(logp, "стоп. " + status_line(st))


if __name__ == "__main__":
    main()
