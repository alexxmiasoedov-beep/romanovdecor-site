# polymarket-copy: воронка отбора кошельков для копирования

Стратегия и её обоснование: `СТРАТЕГИЯ.md`. Пороги: `pm/config.py`.

```
pip install requests
python3 collect_wallets.py            # стадия 0: кошельки, торговавшие сегодня → data/wallets_today.json
python3 stage1_screen.py --workers 24 # стадия 1: дешёвые отсечки → data/stage1.csv
python3 stage2_analyze.py             # стадия 2: история сделок, сегменты → data/stage2.csv, segments.csv
python3 stage3_markout.py             # стадия 3: задержка, маркаут, стакан → data/stage3.csv
python3 report.py                     # сводка → data/REPORT.md
python3 run_all.py                    # всё подряд
```

Любой скрипт принимает `--wallets 0x... 0x...` для проверки конкретных адресов.
Ответы API кэшируются в `data/cache/` (TTL 6 часов для данных по кошелькам),
эпизоды позиций каждого кошелька сохраняются в `data/wallets/<addr>.json`.

Колонки `stage2.csv`, на которые смотреть в первую очередь: `roi_copy`,
`t_stat`, `conc_p95`, `median_hold_h`, `approved_segments`, `exit_value_add`,
`size_signal`. В `stage3.csv`: `roi_delay5`, `keep_ratio5`, `skip_share`,
`markout_24h`, `slippage_median`.
