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

## Реестр, симуляция и регулярный цикл

```
python3 db_update.py                          # результаты прогона → data/db/registry.json
python3 sim.py start --batch 2 --wallets 0x…  # поставить кошельки на бумажную симуляцию ($1 на позицию, старт $100)
python3 sim.py enroll                         # прошедшие стадию 3, кого ещё нет в симуляции → новый батч
python3 sim.py update                         # подтянуть новые сделки, резолвы, переоценку → data/db/SIM_REPORT.md
python3 sim.py review --batch 1               # через неделю: разметить positive/negative → data/db/positive.json
python3 pipeline.py --push                    # весь цикл: сбор → воронка → реестр → симуляция → коммит
```

Цикл: раз в сутки `pipeline.py --push` собирает кошельки за день, прогоняет воронку,
дописывает реестр, всех новых прошедших стадию 3 сразу ставит на симуляцию отдельным
батчем (`sim.py enroll`, номер батча = следующий, тег `auto-<дата>`) и обновляет симуляцию
всех батчей. Раз в неделю вручную: `sim.py review` по батчам, отработавшим ≥7 дней, разбор
причин, правка порогов в `pm/config.py`.

Симуляция воспроизводима из истории сделок API: состояние в `data/db/sim.json`, каждая
сделка кошелька обрабатывается один раз, вход по цене через 30 с после его сделки.
