"""Регулярный прогон: сбор → 3 стадии → реестр → зачисление в симуляцию → симуляция → отчёты [→ commit/push].

  python3 pipeline.py            # без git
  python3 pipeline.py --push     # плюс коммит и push в текущую ветку
  python3 pipeline.py --from stage2 --push   # перезапуск с упавшей стадии
  python3 pipeline.py --evening --push       # вечерний снимок кошельков (17:00 UTC), без воронки
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))


def run(*cmd, check=True, env=None):
    print(">>", " ".join(cmd), file=sys.stderr, flush=True)
    return subprocess.run(cmd, cwd=HERE, check=check, env={**os.environ, **(env or {})})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--skip-collect", action="store_true", help="только симуляция и отчёты")
    ap.add_argument("--from", dest="start", default="collect", choices=["collect", "stage1", "stage2", "stage3"],
                    help="перезапуск с указанной стадии (предыдущие результаты уже на диске)")
    ap.add_argument("--evening", action="store_true", help="только вечерний снимок сбора → data/wallets_evening.json")
    a = ap.parse_args()
    py = sys.executable
    fast = {"PM_MIN_INTERVAL": "0.01"}
    if a.evening:
        run(py, "collect_wallets.py", "--since", "12", "--out", "data/wallets_evening.json", env=fast)
        if a.push:
            run("git", "add", "data/wallets_evening.json")
            if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=HERE).returncode != 0:
                run("git", "commit", "-q", "-m", f"Polymarket: вечерний снимок кошельков {datetime.now(timezone.utc):%Y-%m-%d}")
                for i in range(5):
                    if run("git", "push", check=False).returncode == 0:
                        break
                    time.sleep(2 ** (i + 1))
        return
    order = ["collect", "stage1", "stage2", "stage3"]
    todo = set(order[order.index(a.start):])
    # кэш API растёт на 10–20 ГБ за прогон и переполняет диск; данные по кошелькам живут 6 ч (TTL),
    # так что всё старше 7 ч только занимает место
    run("find", os.path.join(HERE, "data", "cache"), "-type", "f", "-mmin", "+420", "-delete", check=False)
    if not a.skip_collect:
        if "collect" in todo:
            # окно 24 ч (прогон в 05:00 UTC) + вечерний снимок 17:00 UTC, чтобы не терять дневные сделки
            run(py, "collect_wallets.py", "--since", "24", "--merge", "data/wallets_evening.json")
        if "stage1" in todo:
            run(py, "stage1_screen.py", "--workers", "24", env=fast)
        if "stage2" in todo:
            run(py, "stage2_analyze.py", "--workers", "16", env=fast)
        if "stage3" in todo:
            run(py, "stage3_markout.py", env=fast)
        run(py, "report.py")
        run(py, "db_update.py")
        run(py, "sim.py", "enroll")  # прошедшие стадию 3 сразу в симуляцию, новым батчем
    run(py, "sim.py", "update", env=fast)
    if a.push:
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        run("git", "add", "data/db", "data/REPORT.md", "data/stage1.csv", "data/stage2.csv", "data/stage3.csv",
            "data/segments.csv", "data/wallets_today.json")
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=HERE).returncode != 0:
            run("git", "commit", "-q", "-m", f"Polymarket: прогон воронки и симуляции {date}")
            for i in range(5):
                if run("git", "push", check=False).returncode == 0:
                    break
                time.sleep(2 ** (i + 1))


if __name__ == "__main__":
    main()
