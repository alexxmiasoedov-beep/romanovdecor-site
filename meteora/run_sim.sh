#!/bin/sh
# Поднимает обе симуляции в фоне, если они не запущены. Состояние подхватывается.
# Использование: ./run_sim.sh [минут]   (по умолчанию 1440 = 24 часа)
cd "$(dirname "$0")" || exit 1
DUR=${1:-1440}
for P in strategy relaxed; do
  if pgrep -f "^python3 simulate.py --profile $P" >/dev/null 2>&1; then
    echo "$P: уже запущена"
  else
    nohup python3 simulate.py --profile "$P" --duration "$DUR" >/dev/null 2>&1 &
    echo "$P: запущена на $DUR мин (pid $!)"
  fi
done
