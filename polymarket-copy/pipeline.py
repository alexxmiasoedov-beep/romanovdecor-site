"""Регулярный прогон: сбор → 3 стадии → реестр → симуляция → отчёты [→ commit/push].

  python3 pipeline.py            # без git
  python3 pipeline.py --push     # плюс коммит и push в текущую ветку
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
    a = ap.parse_args()
    py = sys.executable
    fast = {"PM_MIN_INTERVAL": "0.01"}
    if not a.skip_collect:
        run(py, "collect_wallets.py")
        run(py, "stage1_screen.py", "--workers", "24", env=fast)
        run(py, "stage2_analyze.py", "--workers", "16", env=fast)
        run(py, "stage3_markout.py", env=fast)
        run(py, "report.py")
        run(py, "db_update.py")
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
