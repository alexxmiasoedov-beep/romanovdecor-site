"""Восстановление бида и аска на момент времени из ленты сделок рынка.

Лента Data API тейкерская и односторонняя (одна запись на транзакцию), поэтому:
  BUY  по нашему токену  → тейкер снял аск: ask = p
  SELL по нашему токену  → тейкер ударил в бид: bid = p
  BUY  по противоположному токену по q → его аск q, наш бид = 1 − q
  SELL по противоположному токену по q → его бид q, наш аск = 1 − q
Рыночная покупка исполняется по аску, продажа по биду. Ордер на $1 глубину не выбирает.
"""
from __future__ import annotations

from . import api, config, metrics

SPREAD_FALLBACK = 0.02   # если аск не наблюдался: бид + типичный спред ленты, иначе +2 цента
LOOKBACK = 1800          # сколько секунд назад искать последнюю котировку
LOOKAHEAD = 1800         # сколько секунд вперёд ждать первую сделку после нужного момента


def _events(tape: list[dict], asset: str) -> list[tuple[float, str, float]]:
    ev = []
    for t in tape:
        p = float(t.get("price") or 0)
        tt = float(t.get("timestamp") or 0)
        if p <= 0 or not tt:
            continue
        same = t.get("asset") == asset
        if same:
            ev.append((tt, "ask" if t.get("side") == "BUY" else "bid", p))
        else:
            ev.append((tt, "bid" if t.get("side") == "BUY" else "ask", 1 - p))
    ev.sort()
    return ev


def _typical_spread(ev) -> float:
    asks = [(t, p) for t, k, p in ev if k == "ask"]
    bids = [(t, p) for t, k, p in ev if k == "bid"]
    if not asks or not bids:
        return SPREAD_FALLBACK
    diffs = []
    j = 0
    for t, a in asks:
        while j + 1 < len(bids) and bids[j + 1][0] <= t:
            j += 1
        if abs(bids[j][0] - t) <= 600:
            diffs.append(max(a - bids[j][1], 0.0))
    return max(metrics.percentile(diffs, 0.5), 0.01) if diffs else SPREAD_FALLBACK


def quote(cid: str, asset: str, ts: float, cache: bool = False, tape: list[dict] | None = None) -> dict:
    """→ {"bid", "ask", "src"}; src: tape | tape_est | history | none."""
    if tape is None:
        tape = api.trades_market(cid, max_pages=config.TAPE_PAGES, cache=cache)
    ev = _events(tape, asset)
    oldest = ev[0][0] if ev else None
    out = {"bid": None, "ask": None, "src": "none"}
    if ev and oldest <= ts:
        for kind in ("ask", "bid"):
            after = [(t, p) for t, k, p in ev if k == kind and ts <= t <= ts + LOOKAHEAD]
            before = [(t, p) for t, k, p in ev if k == kind and ts - LOOKBACK <= t < ts]
            if after:
                out[kind] = after[0][1]
            elif before:
                out[kind] = before[-1][1]
        if out["ask"] is not None or out["bid"] is not None:
            out["src"] = "tape"
            sp = _typical_spread(ev)
            if out["ask"] is None:
                out["ask"] = min(out["bid"] + sp, 0.999)
                out["src"] = "tape_est"
            if out["bid"] is None:
                out["bid"] = max(out["ask"] - sp, 0.001)
                out["src"] = "tape_est"
            if out["ask"] < out["bid"]:  # котировки из разных моментов — берём консервативно
                out["ask"] = out["bid"]
            return out
    hist = api.prices_history(asset, int(ts) - 120, int(ts) + 600, fidelity=1)
    pts = sorted((h for h in hist if h["t"] <= ts + 60), key=lambda h: h["t"])
    if pts:
        p = pts[-1]["p"]
        return {"bid": max(p - SPREAD_FALLBACK / 2, 0.001), "ask": min(p + SPREAD_FALLBACK / 2, 0.999),
                "src": "history"}
    return out
