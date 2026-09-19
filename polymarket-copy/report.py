"""Сводный отчёт по результатам воронки → data/REPORT.md"""
from __future__ import annotations

import csv
import json
import os
from collections import Counter
from datetime import datetime, timezone

D = os.path.join(os.path.dirname(__file__), "data")


def load(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return []
    with open(p) as f:
        return list(csv.DictReader(f))


def main() -> None:
    w = json.load(open(os.path.join(D, "wallets_today.json")))
    s1, s2, s3 = load("stage1.csv"), load("stage2.csv"), load("stage3.csv")
    segs = load("segments.csv")
    out = []
    out.append(f"# Отчёт воронки, {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n")
    out.append("## Воронка\n")
    out.append("| Стадия | Кошельков |\n|---|---|")
    out.append(f"| 0. Торговали сегодня | {len(w['wallets'])} |")
    out.append(f"| 0. Из них не только 5-мин крипта | {sum(1 for d in w['wallets'].values() if d['short_crypto_share'] < 0.999)} |")
    out.append(f"| 1. Прошли дешёвые отсечки | {sum(1 for r in s1 if r['pass'] == 'True')} из {len(s1)} |")
    out.append(f"| 2. Прошли по полной истории | {sum(1 for r in s2 if r['pass'] == 'True')} + сегментом {sum(1 for r in s2 if r['pass'] == 'segment')} из {len(s2)} |")
    out.append(f"| 3. Прошли реалистичный вход | {sum(1 for r in s3 if r['pass'] == 'True')} из {len(s3)} |\n")

    for title, rows in (("Причины отсева, стадия 1", s1), ("Причины отсева, стадия 2", s2), ("Причины отсева, стадия 3", s3)):
        c = Counter(x for r in rows for x in r["fail_reasons"].split(";") if x)
        if c:
            out.append(f"## {title}\n")
            out.append("| Причина | Кошельков |\n|---|---|")
            out.extend(f"| {k} | {v} |" for k, v in c.most_common())
            out.append("")

    fin = [r for r in s3 if r["pass"] == "True"]
    s2map = {r["wallet"]: r for r in s2}
    if fin:
        out.append("## Финалисты\n")
        out.append("| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for r in fin:
            a = s2map.get(r["wallet"], {})
            out.append(f"| `{r['wallet']}` | {r['name']} | {a.get('top_category','')} | {a.get('roi_copy','')} | {a.get('t_stat','')} | "
                       f"{r['roi_delay5']} | {r['markout_24h']} | {a.get('conc_p95','')} | {a.get('median_hold_h','')} | "
                       f"{r['slippage_median'] or 'н/д'} | {r['approved_segments'] or 'все рынки'} |")
        out.append("")
    seg_only = [r for r in s2 if r["pass"] == "segment"]
    if seg_only:
        out.append("## Кандидаты только на сегмент\n")
        out.append("| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |\n|---|---|---|---|---|")
        for r in seg_only[:40]:
            out.append(f"| `{r['wallet']}` | {r['name']} | {r['roi_copy']} | {r['approved_segments']} | {r['fail_reasons']} |")
        out.append("")
    top2 = sorted([r for r in s2 if r["pass"] == "True"], key=lambda r: -float(r["score"] or 0))[:40]
    if top2:
        out.append("## Прошедшие стадию 2 целиком, по скору\n")
        out.append("| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        s3map = {r["wallet"]: r for r in s3}
        for r in top2:
            t3 = s3map.get(r["wallet"])
            st = "не проверялся" if not t3 else ("прошёл" if t3["pass"] == "True" else t3["fail_reasons"])
            out.append(f"| `{r['wallet']}` | {r['name']} | {r['top_category']} | {r['closed_n']} | {r['roi_copy']} | {r['roi_trimmed']} | "
                       f"{r['t_stat']} | {r['winrate']} | {r['conc_p95']} | {r['median_hold_h']} | {r['median_volume']} | {st} |")
        out.append("")
    appr = [s for s in segs if s["approved"] == "True"]
    if appr:
        out.append("## Утверждённые сегменты, топ по n × ROI\n")
        appr.sort(key=lambda s: -float(s["roi_shrunk"]) * float(s["n"]) ** 0.5)
        out.append("| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |\n|---|---|---|---|---|---|---|")
        for s in appr[:60]:
            out.append(f"| `{s['wallet'][:10]}…` | {s['segment']} | {s['n']} | {s['roi_mean']} | {s['roi_shrunk']} | {s['t']} | {s['winrate']} |")
        out.append("")
    with open(os.path.join(D, "REPORT.md"), "w") as f:
        f.write("\n".join(out))
    print("\n".join(out[:12]))


if __name__ == "__main__":
    main()
