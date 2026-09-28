"""Позиции лидера и симуляция нашей копии.

Копия: фиксированная сумма SOL на первой покупке лидера, один вход,
пропорциональный выход (лидер продал долю f своей позиции -> мы
продаём долю f своей). Исполнение считаем по константному произведению
на резервах пула ПОСЛЕ сделки лидера: мы всегда следующие в очереди.
"""
from .config import PUMP_SUPPLY


def cp_buy(sol_in, sol_res, tok_res):
    return tok_res * sol_in / (sol_res + sol_in)


def cp_sell(tok_in, sol_res, tok_res):
    return sol_res * tok_in / (tok_res + tok_in)


def build_positions(swaps):
    """Свопы одного кошелька -> список позиций по токенам."""
    by_mint = {}
    for s in swaps:
        by_mint.setdefault(s["mint"], []).append(s)
    positions = []
    for mint, ss in by_mint.items():
        cur = None
        for s in ss:
            if s["side"] == "buy":
                if cur is None:
                    cur = {"mint": mint, "trades": [], "held": 0.0, "max_held": 0.0}
                    positions.append(cur)
                cur["held"] += s["tokens"]
                cur["max_held"] = max(cur["max_held"], cur["held"])
                cur["trades"].append(s)
            else:
                if cur is None:
                    continue                      # продажа без покупки в окне (перевод/аирдроп)
                sold = min(s["tokens"], cur["held"])
                frac = sold / cur["held"] if cur["held"] > 0 else 1.0
                cur["held"] -= sold
                t = dict(s); t["frac"] = frac
                cur["trades"].append(t)
                if cur["held"] <= cur["max_held"] * 0.01:
                    cur["closed"] = True
                    cur = None
    return positions


def leader_stats(p, sol_usd):
    buys = [t for t in p["trades"] if t["side"] == "buy"]
    sells = [t for t in p["trades"] if t["side"] == "sell"]
    first = buys[0]
    sol_in = sum(t["sol"] for t in buys)
    sol_out = sum(t["sol"] for t in sells)
    entry_impact = first["sol"] / (first["sol_res"] - first["sol"]) if first.get("sol_res") and first["sol_res"] > first["sol"] else None
    exit_impacts = [t["sol"] / (t["sol_res"] + t["sol"]) for t in sells if t.get("sol_res")]
    mc_usd = None
    if first.get("sol_res") and first.get("tok_res") and sol_usd:
        mc_usd = first["sol_res"] / first["tok_res"] * PUMP_SUPPLY * sol_usd
    hold = (sells[-1]["time"] - first["time"]) if sells else None
    return {
        "mint": p["mint"], "open_time": first["time"], "closed": p.get("closed", False),
        "n_buys": len(buys), "n_sells": len(sells),
        "pre_migration": bool(first["pre_migration"]), "venue": first["venue"],
        "sniper": bool(first["pre_migration"]) and first.get("real_sol_res") is not None and first["real_sol_res"] < 2.0,
        "sol_in": sol_in, "sol_out": sol_out, "hold_sec": hold,
        "entry_impact": entry_impact, "max_exit_impact": max(exit_impacts) if exit_impacts else None,
        "entry_sol_res": first.get("sol_res"), "entry_mc_usd": mc_usd,
        "held_left": p["held"],
    }


def simulate_copy(p, cfg, latency_bps=None, token_price_now=None, now=None):
    """-> (наша_доходность, sol_out, замечание). None если позицию нельзя скопировать."""
    lat = (cfg.latency_slippage_bps if latency_bps is None else latency_bps) / 10_000
    fee = cfg.fee_bps / 10_000
    first = p["trades"][0]
    F = cfg.copy_size_sol
    if first.get("sol_res") and first.get("tok_res"):
        tokens = cp_buy(F * (1 - fee), first["sol_res"], first["tok_res"]) * (1 - lat)
    else:   # резервы неизвестны: цена лидера + предполагаемый импакт
        tokens = F * (1 - fee) / (first["sol"] / first["tokens"]) * (1 - cfg.assumed_entry_impact_bps / 10_000) * (1 - lat)
    our = tokens
    sol_out = 0.0
    for t in p["trades"][1:]:
        if t["side"] != "sell" or our <= 0:
            continue
        q = our * t["frac"]
        if t.get("sol_res") and t.get("tok_res"):
            got = cp_sell(q, t["sol_res"], t["tok_res"])
        else:
            got = q * t["sol"] / t["tokens"]           # нет резервов — по цене лидера
        sol_out += got * (1 - fee) * (1 - lat)
        our -= q
    note = ""
    if our > 1e-9:
        age = (now or first["time"]) - first["time"]
        if age > cfg.dead_bag_days * 86400:
            price = (token_price_now or {}).get(p["mint"], 0.0)
            sol_out += our * price * cfg.dead_bag_value_haircut
            note = "dead_bag"
        else:
            return None                                 # свежая открытая позиция — не считаем
    return (sol_out - F) / F, sol_out, note
