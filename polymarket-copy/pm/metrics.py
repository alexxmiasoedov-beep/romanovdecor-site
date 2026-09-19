"""Общие вычисления: доходности, значимость, корзины цен, сегментация."""
from __future__ import annotations

import math
from collections import defaultdict

from . import config


def price_bucket(p: float) -> str:
    for lo, hi in config.PRICE_BUCKETS:
        if lo <= p < hi:
            return f"{lo:.2f}-{min(hi, 1):.2f}"
    return "?"


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 0.0


def std(xs):
    xs = list(xs)
    if len(xs) < 2:
        return 0.0
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def t_stat(xs) -> float:
    xs = list(xs)
    s = std(xs)
    if len(xs) < 2 or s == 0:
        return 0.0
    return mean(xs) / (s / math.sqrt(len(xs)))


def trimmed_mean(xs, frac: float = 0.05) -> float:
    xs = sorted(xs)
    k = int(len(xs) * frac)
    core = xs[k: len(xs) - k] if len(xs) > 2 * k else xs
    return mean(core)


def percentile(xs, q: float) -> float:
    xs = sorted(xs)
    if not xs:
        return 0.0
    i = min(len(xs) - 1, int(math.ceil(q * len(xs))) - 1)
    return xs[max(i, 0)]


def max_drawdown(rs) -> float:
    """Максимальная просадка кумулятивной суммы доходностей (в ставках)."""
    peak = cum = 0.0
    dd = 0.0
    for r in rs:
        cum += r
        peak = max(peak, cum)
        dd = max(dd, peak - cum)
    return dd


def profit_shares(positions: list[dict]) -> dict:
    """Доли прибыли: от входов <0,10, от входов ≥0,90, от лучшей позиции."""
    gains = [p["pnl"] for p in positions if p["pnl"] > 0]
    total_gain = sum(gains) or 1e-9
    lt10 = sum(p["pnl"] for p in positions if p["pnl"] > 0 and p["entry"] < 0.10)
    ge90 = sum(p["pnl"] for p in positions if p["pnl"] > 0 and p["entry"] >= 0.90)
    top1 = max(gains) if gains else 0.0
    return {"profit_share_lt10": lt10 / total_gain, "profit_share_ge90": ge90 / total_gain,
            "profit_share_top1": top1 / total_gain}


def calibration_edge(positions: list[dict]) -> dict:
    """Edge = винрейт − цена входа по корзинам; только позиции, дошедшие до резолва."""
    by = defaultdict(list)
    for p in positions:
        if p.get("resolved") is not None:
            by[price_bucket(p["entry"])].append((p["resolved"], p["entry"]))
    out = {}
    for b, xs in sorted(by.items()):
        wr = mean(w for w, _ in xs)
        pr = mean(e for _, e in xs)
        out[b] = {"n": len(xs), "winrate": round(wr, 3), "avg_price": round(pr, 3), "edge": round(wr - pr, 3)}
    allx = [(w, e) for xs in by.values() for w, e in xs]
    out["_all"] = {"n": len(allx), "edge": round(mean(w - e for w, e in allx), 4) if allx else 0.0}
    return out


def segment_stats(positions: list[dict], key_fn, overall_mean: float) -> list[dict]:
    """Статистика по сегментам со сжатием к общему среднему и walk-forward проверкой."""
    groups = defaultdict(list)
    for p in positions:
        k = key_fn(p)
        if k:
            groups[k].append(p)
    rows = []
    k_shrink = config.SEG_SHRINK_K
    for k, ps in groups.items():
        ps.sort(key=lambda p: p["t_open"])
        rs = [p["r"] for p in ps]
        n = len(rs)
        m = mean(rs)
        shrunk = (n * m + k_shrink * overall_mean) / (n + k_shrink)
        half = n // 2
        r1, r2 = rs[:half], rs[half:]
        rows.append({
            "segment": k, "n": n, "roi_mean": round(m, 4), "roi_shrunk": round(shrunk, 4),
            "t": round(t_stat(rs), 2), "roi_half1": round(mean(r1), 4), "roi_half2": round(mean(r2), 4),
            "winrate": round(mean(1.0 if r > 0 else 0.0 for r in rs), 3),
            "approved": n >= config.SEG_MIN_N and t_stat(rs) >= config.SEG_MIN_T and shrunk > 0
                        and mean(r1) > 0 and mean(r2) > 0,
        })
    rows.sort(key=lambda r: (-r["approved"], -r["roi_shrunk"] * math.sqrt(r["n"])))
    return rows
