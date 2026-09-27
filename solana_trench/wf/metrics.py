"""Метрики кошелька и пороги фильтра. Каждый порог -> причина отказа."""
import statistics as st
import time

from .positions import build_positions, leader_stats, simulate_copy


def _median(xs):
    xs = [x for x in xs if x is not None]
    return st.median(xs) if xs else None


def wallet_metrics(swaps, cfg, sol_price_by_day=None, sol_now=None, token_prices=None, now=None):
    now = now or time.time()
    positions = build_positions(swaps)
    rows = []
    for p in positions:
        day = (p["trades"][0]["time"] or now) // 86400 * 86400
        sol_usd = (sol_price_by_day or {}).get(day) or sol_now
        s = leader_stats(p, sol_usd)
        sim = simulate_copy(p, cfg, token_price_now=token_prices, now=now)
        sim2 = simulate_copy(p, cfg, latency_bps=cfg.latency_slippage_bps * 2, token_price_now=token_prices, now=now)
        s["copy_ret"] = sim[0] if sim else None
        s["copy_pnl"] = (sim[1] - cfg.copy_size_sol) if sim else None
        s["copy_pnl_2x_latency"] = (sim2[1] - cfg.copy_size_sol) if sim2 else None
        s["dead_bag"] = bool(sim and sim[2] == "dead_bag")
        rows.append(s)

    closed = [r for r in rows if r["closed"] or r["dead_bag"]]
    sim_rows = [r for r in closed if r["copy_ret"] is not None]
    m = {
        "n_swaps": len(swaps),
        "n_positions": len(rows),
        "n_closed": len(closed),
        "n_dead_bags": sum(r["dead_bag"] for r in rows),
        "post_migration_share": (1 - sum(r["pre_migration"] for r in rows) / len(rows)) if rows else None,
        "sniper_share": (sum(r["sniper"] for r in rows) / len(rows)) if rows else None,
        "avg_buys_per_position": (sum(r["n_buys"] for r in rows) / len(rows)) if rows else None,
        "median_hold_sec": _median([r["hold_sec"] for r in closed if r["closed"]]),
        "fast_exit_share": (sum(1 for r in closed if r["closed"] and r["hold_sec"] is not None and r["hold_sec"] < cfg.min_median_hold_sec) / len(closed)) if closed else None,
        "median_entry_impact": _median([r["entry_impact"] for r in rows]),
        "big_entry_share": (sum(1 for r in rows if (r["entry_impact"] or 0) > cfg.big_entry_impact) / len(rows)) if rows else None,
        "median_exit_impact": _median([r["max_exit_impact"] for r in closed]),
        "median_entry_mc_usd": _median([r["entry_mc_usd"] for r in rows]),
        "median_entry_sol": _median([r["sol_in"] / r["n_buys"] for r in rows]),
        "leader_pnl_sol": sum(r["sol_out"] - r["sol_in"] for r in closed),
        "leader_win_rate": (sum(1 for r in closed if r["sol_out"] > r["sol_in"]) / len(closed)) if closed else None,
        "leader_median_ret": _median([r["sol_out"] / r["sol_in"] - 1 for r in closed if r["sol_in"] > 0]),
    }
    if sim_rows:
        pnls = [r["copy_pnl"] for r in sim_rows]
        wins = [x for x in pnls if x > 0]
        losses = [-x for x in pnls if x <= 0]
        streak = best = 0
        for x in sorted(sim_rows, key=lambda r: r["open_time"]):
            streak = streak + 1 if x["copy_pnl"] <= 0 else 0
            best = max(best, streak)
        weeks = {}
        for r in sim_rows:
            weeks[r["open_time"] // (7 * 86400)] = weeks.get(r["open_time"] // (7 * 86400), 0) + r["copy_pnl"]
        by_token = {}
        for r in sim_rows:
            by_token[r["mint"]] = by_token.get(r["mint"], 0) + r["copy_pnl"]
        total_pos = sum(v for v in by_token.values() if v > 0)
        m.update({
            "copy_n": len(sim_rows),
            "copy_pnl_sol": sum(pnls),
            "copy_pnl_2x_latency": sum(r["copy_pnl_2x_latency"] for r in sim_rows if r["copy_pnl_2x_latency"] is not None),
            "copy_median_ret": st.median([r["copy_ret"] for r in sim_rows]),
            "copy_win_rate": len(wins) / len(pnls),
            "copy_profit_factor": (sum(wins) / sum(losses)) if losses else (99.0 if wins else 0.0),
            "copy_max_loss_streak": best,
            "top_token_profit_share": (max(by_token.values()) / total_pos) if total_pos > 0 else None,
            "positive_weeks_share": sum(1 for v in weeks.values() if v > 0) / len(weeks),
            "n_weeks": len(weeks),
        })
    else:
        m.update({"copy_n": 0, "copy_pnl_sol": None, "copy_pnl_2x_latency": None, "copy_median_ret": None,
                  "copy_win_rate": None, "copy_profit_factor": None, "copy_max_loss_streak": None,
                  "top_token_profit_share": None, "positive_weeks_share": None, "n_weeks": 0})
    return m, rows


def apply_filters(m, cfg):
    """-> список причин отказа (пустой = прошёл)."""
    reasons = []

    def need(cond, reason):
        if not cond:
            reasons.append(reason)

    def val(k):
        return m.get(k)

    need((val("n_closed") or 0) >= cfg.min_closed_positions, "few_closed_positions")
    if val("median_hold_sec") is not None:
        need(val("median_hold_sec") >= cfg.min_median_hold_sec, "median_hold_too_short")
    if val("fast_exit_share") is not None:
        need(val("fast_exit_share") <= cfg.max_fast_exit_share, "too_many_fast_exits")
    if val("post_migration_share") is not None:
        need(val("post_migration_share") >= cfg.min_post_migration_share, "trades_pre_migration")
    if val("sniper_share") is not None:
        need(val("sniper_share") <= cfg.max_sniper_share, "sniper")
    if val("median_entry_impact") is not None:
        need(val("median_entry_impact") <= cfg.max_median_entry_impact, "entry_too_big_for_pool")
    if val("big_entry_share") is not None:
        need(val("big_entry_share") <= cfg.max_big_entry_share, "many_big_entries")
    if val("median_exit_impact") is not None:
        need(val("median_exit_impact") <= cfg.max_median_exit_impact, "exit_too_big_for_pool")
    if val("avg_buys_per_position") is not None:
        need(val("avg_buys_per_position") <= cfg.max_avg_buys_per_position, "averaging_entries")
    if val("copy_n"):
        need(val("copy_median_ret") >= cfg.min_copy_median_ret, "copy_median_ret_low")
        need(val("copy_win_rate") >= cfg.min_copy_win_rate, "copy_win_rate_low")
        need(val("copy_profit_factor") >= cfg.min_copy_profit_factor, "copy_profit_factor_low")
        need(val("copy_pnl_sol") > cfg.min_copy_pnl_sol, "copy_pnl_negative")
        if val("top_token_profit_share") is not None:
            need(val("top_token_profit_share") <= cfg.max_top_token_profit_share, "profit_from_one_token")
        need(val("positive_weeks_share") >= cfg.min_positive_weeks_share, "inconsistent_weeks")
        if cfg.require_latency_robust:
            need((val("copy_pnl_2x_latency") or 0) > 0, "latency_sensitive")
    else:
        reasons.append("nothing_to_simulate")
    return reasons
