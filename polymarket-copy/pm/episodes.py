"""Сборка эпизодов позиций из сделок (FIFO по токену) и расчёт доходностей.

Эпизод = от первой покупки токена при нулевом остатке до полной продажи либо резолва.
Ключевые доходности (все на одну ставку, т.е. равновзвешенные):
  r_copy — что получил бы копировщик: вход по цене ПЕРВОЙ покупки эпизода, выход
           пропорционально продажам кошелька, остаток — по резолву.
  r_hold — вход как выше, но держим до резолва, продажи кошелька игнорируем.
  r_wallet — фактическая доходность кошелька на вложенный доллар (VWAP входа).
"""
from __future__ import annotations

import time

EPS = 1e-6


def build(trades: list[dict], mkts: dict[str, dict], now: float | None = None) -> list[dict]:
    now = now or time.time()
    trades = sorted(trades, key=lambda t: (t.get("timestamp", 0), t.get("side") != "BUY"))
    state: dict[str, dict] = {}
    episodes: list[dict] = []

    def close(ep: dict, t_close: float, how: str, res: float | None) -> None:
        bought, sold, cost, proceeds = ep["bought"], ep["sold"], ep["cost"], ep["proceeds"]
        remaining = max(bought - sold, 0.0)
        resv = res if res is not None else 0.0
        ep["t_close"] = t_close
        ep["closed_by"] = how
        ep["res"] = res
        ep["remaining"] = remaining
        ep["pnl_wallet"] = proceeds + resv * remaining - cost
        ep["r_wallet"] = ep["pnl_wallet"] / cost if cost > 0 else 0.0
        sold_frac = min(sold / bought, 1.0) if bought > 0 else 0.0
        sell_vwap = proceeds / sold if sold > 0 else 0.0
        exit_val = sell_vwap * sold_frac + resv * (1 - sold_frac)
        ep["exit_val"] = exit_val
        ep["r_copy"] = exit_val / ep["entry"] - 1 if ep["entry"] > 0 else 0.0
        ep["r_hold"] = (res / ep["entry"] - 1) if (res is not None and ep["entry"] > 0) else None
        ep["hold_h"] = (t_close - ep["t_open"]) / 3600
        episodes.append(ep)

    for t in trades:
        asset = t.get("asset")
        cid = t.get("conditionId")
        ts = float(t.get("timestamp") or 0)
        price = float(t.get("price") or 0)
        size = float(t.get("size") or 0)
        if not asset or price <= 0 or size <= 0:
            continue
        st = state.get(asset)
        if t.get("side") == "BUY":
            if st is None or st["qty"] <= EPS:
                st = {"cid": cid, "asset": asset, "qty": 0.0, "bought": 0.0, "sold": 0.0, "cost": 0.0,
                      "proceeds": 0.0, "t_open": ts, "entry": price, "n_buys": 0, "n_sells": 0,
                      "outcome": t.get("outcome"), "title": t.get("title"), "slug": t.get("slug")}
                state[asset] = st
            st["qty"] += size
            st["bought"] += size
            st["cost"] += price * size
            st["n_buys"] += 1
        else:
            if st is None or st["qty"] <= EPS:
                continue  # продажа без позиции (сплит/мердж/негриск) — игнорируем
            sz = min(size, st["qty"])
            st["qty"] -= sz
            st["sold"] += sz
            st["proceeds"] += price * sz
            st["n_sells"] += 1
            if st["qty"] <= EPS:
                m = mkts.get(cid) or {}
                res = _resolution(m, asset)
                close(st, ts, "sell", res)
                state[asset] = None

    for asset, st in state.items():
        if not st or st["qty"] <= EPS:
            continue
        m = mkts.get(st["cid"]) or {}
        res = _resolution(m, asset)
        if m.get("closed") and res is not None:
            t_close = m.get("closedTime") or m.get("endDate") or now
            t_close = max(t_close, st["t_open"] + 1)
            close(st, t_close, "resolve", res)
        else:
            st.update({"t_close": None, "closed_by": None, "res": None, "remaining": st["qty"],
                       "pnl_wallet": None, "r_wallet": None, "r_copy": None, "r_hold": None,
                       "hold_h": (now - st["t_open"]) / 3600, "exit_val": None})
            episodes.append(st)

    for ep in episodes:
        m = mkts.get(ep["cid"]) or {}
        ep["entry_vwap"] = ep["cost"] / ep["bought"] if ep["bought"] else ep["entry"]
        ep["outcome_res"] = _resolution(m, ep["asset"])  # исход рынка, если известен (для калибровки)
        ep["volume"] = m.get("volume", 0)
        gs = m.get("gameStartTime") or 0
        ep["live"] = bool(gs and ep["t_open"] > gs)
        t_end = m.get("closedTime") or m.get("endDate") or 0
        ep["snipe"] = bool(t_end and ep["entry"] >= 0.95 and 0 <= t_end - ep["t_open"] <= 600)
        ep["is_closed"] = ep["closed_by"] is not None
    episodes.sort(key=lambda e: e["t_open"])
    return episodes


def _resolution(m: dict, asset: str) -> float | None:
    if not m.get("closed"):
        return None
    prices, tokens = m.get("outcomePrices") or [], m.get("tokens") or []
    if asset in tokens and len(prices) == len(tokens):
        p = prices[tokens.index(asset)]
        if p in (0.0, 1.0):
            return p
    return None


def concurrency(episodes: list[dict], now: float | None = None) -> tuple[float, int]:
    """95-й перцентиль и максимум числа одновременно открытых эпизодов (в момент каждого входа)."""
    now = now or time.time()
    ev = []
    for e in episodes:
        ev.append((e["t_open"], 1))
        ev.append((e["t_close"] or now, -1))
    ev.sort(key=lambda x: (x[0], x[1]))  # закрытие раньше открытия при равном времени
    cur = 0
    counts = []
    for _, d in ev:
        cur += d
        if d == 1:
            counts.append(cur)
    counts.sort()
    if not counts:
        return 0.0, 0
    p95 = counts[min(len(counts) - 1, int(0.95 * len(counts)))]
    return float(p95), counts[-1]
