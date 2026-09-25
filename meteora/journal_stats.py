#!/usr/bin/env python3
"""
Статистика по журналу сделок journal.csv.

    python3 journal_stats.py journal.csv

Считает net_pnl там, где он не заполнен вручную:
    net_pnl_usd = fees_claimed_usd + tokens_left_sold_usd + position_withdrawn_usd
                  - deposit_usd - gas_usd - slippage_usd
    net_pnl_pct = net_pnl_usd / deposit_usd * 100

Выводит: общий итог, винрейт, средний плюс/минус, ожидание на сделку,
разбивку по причине выхода и по корзинам ключевых метрик на входе,
чтобы было видно, какие пороги реально отделяют плюс от минуса.
"""
import csv
import sys
from collections import defaultdict


def num(v):
    try:
        return float(str(v).replace(",", ".").replace(" ", ""))
    except (TypeError, ValueError):
        return None


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("symbol") or r["symbol"].upper() == "EXAMPLE":
                continue
            dep = num(r.get("deposit_usd"))
            if not dep:
                continue
            pnl = num(r.get("net_pnl_usd"))
            if pnl is None:
                parts = [num(r.get(k)) or 0 for k in
                         ("fees_claimed_usd", "tokens_left_sold_usd", "position_withdrawn_usd")]
                costs = [num(r.get(k)) or 0 for k in ("gas_usd", "slippage_usd")]
                pnl = sum(parts) - dep - sum(costs)
            r["_pnl"] = pnl
            r["_pct"] = pnl / dep * 100
            r["_dep"] = dep
            rows.append(r)
    return rows


def bucket_report(rows, key, edges, label, fmt=lambda v: f"{v:g}"):
    groups = defaultdict(list)
    for r in rows:
        v = num(r.get(key))
        if v is None:
            groups["нет данных"].append(r)
            continue
        name = None
        lo = None
        for e in edges:
            if v < e:
                name = f"{fmt(lo)}–{fmt(e)}" if lo is not None else f"< {fmt(e)}"
                break
            lo = e
        if name is None:
            name = f">= {fmt(edges[-1])}"
        groups[name].append(r)
    print(f"\n{label}")
    print(f"  {'корзина':<18}{'сделок':>7}{'винрейт':>9}{'ср. %':>8}{'сумма $':>10}")
    for name, g in groups.items():
        wins = sum(1 for r in g if r["_pnl"] > 0)
        print(f"  {name:<18}{len(g):>7}{wins/len(g)*100:>8.0f}%{sum(r['_pct'] for r in g)/len(g):>8.1f}"
              f"{sum(r['_pnl'] for r in g):>10.1f}")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "journal.csv"
    rows = load(path)
    if not rows:
        print("В журнале нет заполненных сделок (строка EXAMPLE не считается).")
        return
    n = len(rows)
    wins = [r for r in rows if r["_pnl"] > 0]
    losses = [r for r in rows if r["_pnl"] <= 0]
    total = sum(r["_pnl"] for r in rows)
    dep = sum(r["_dep"] for r in rows)
    print(f"Сделок: {n}   Итог: {total:+.1f} $   Оборот депозитов: {dep:.0f} $   Доход на оборот: {total/dep*100:+.2f}%")
    print(f"Винрейт: {len(wins)/n*100:.0f}%   "
          f"Средний плюс: {sum(r['_pct'] for r in wins)/len(wins) if wins else 0:+.1f}%   "
          f"Средний минус: {sum(r['_pct'] for r in losses)/len(losses) if losses else 0:+.1f}%")
    print(f"Ожидание на сделку: {total/n:+.1f} $ ({sum(r['_pct'] for r in rows)/n:+.2f}%)")
    worst = min(rows, key=lambda r: r["_pnl"])
    best = max(rows, key=lambda r: r["_pnl"])
    print(f"Худшая: {worst['symbol']} {worst['_pnl']:+.1f} $   Лучшая: {best['symbol']} {best['_pnl']:+.1f} $")
    fees = sum(num(r.get("fees_claimed_usd")) or 0 for r in rows)
    costs = sum((num(r.get("gas_usd")) or 0) + (num(r.get("slippage_usd")) or 0) for r in rows)
    print(f"Комиссий собрано: {fees:.1f} $   Газ+проскальзывание: {costs:.1f} $   "
          f"Изменение стоимости позиций: {total - fees + costs:+.1f} $")

    print("\nПо причине выхода")
    by = defaultdict(list)
    for r in rows:
        by[(r.get("exit_reason") or "?").strip().lower()].append(r)
    print(f"  {'причина':<12}{'сделок':>7}{'винрейт':>9}{'ср. %':>8}{'сумма $':>10}{'ср. мин':>9}")
    for k, g in sorted(by.items(), key=lambda kv: -len(kv[1])):
        w = sum(1 for r in g if r["_pnl"] > 0)
        mins = [num(r.get("minutes_held")) for r in g if num(r.get("minutes_held")) is not None]
        print(f"  {k:<12}{len(g):>7}{w/len(g)*100:>8.0f}%{sum(r['_pct'] for r in g)/len(g):>8.1f}"
              f"{sum(r['_pnl'] for r in g):>10.1f}{(sum(mins)/len(mins) if mins else 0):>9.0f}")

    bucket_report(rows, "fee_tvl_1h_entry", [0.01, 0.02, 0.05, 0.10], "По fee/TVL за 1ч на входе (доля)")
    bucket_report(rows, "mcap_entry", [1e6, 3e6, 10e6, 30e6], "По капитализации на входе",
                  fmt=lambda v: f"{v/1e6:g}M")
    bucket_report(rows, "age_min_entry", [30, 60, 180, 360, 720], "По возрасту токена на входе, мин")
    bucket_report(rows, "top10_pct_entry", [15, 25, 35], "По доле топ-10 держателей, %")
    bucket_report(rows, "vol_trend_entry", [0.7, 1.0, 1.5], "По тренду объёма на входе (1ч / прошлый час)")
    bucket_report(rows, "minutes_held", [60, 120, 240], "По времени в позиции, мин")
    print("\nЧитать так: корзина с отрицательным средним и достаточным числом сделок — кандидат на ужесточение порога.")


if __name__ == "__main__":
    main()
