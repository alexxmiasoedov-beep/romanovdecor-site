"""Ежедневный отбор в симуляцию 2 (решение владельца 11.10.2026):
  python3 forward/daily.py [--push]

1) forward/screen.py по дневному сбору data/wallets_today.json (память проверенных — forward/screened.json.gz,
   повтор через 7 дней; уже зачисленные и убранные владельцем пропускаются);
2) прошедших зачисляем (fwd_sim.py enroll), стратегии сохраняем в forward/strategies_<дата>.json;
3) fwd_sim.py update; с --push — коммит и push файлов forward/.
Симуляцию 1 (sim.py, registry) не трогает.
"""
import argparse, json, os, subprocess, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def run(*cmd, check=True, env=None):
    print(">>", " ".join(cmd), file=sys.stderr, flush=True)
    e = dict(os.environ); e.update(env or {})
    return subprocess.run(cmd, cwd=ROOT, env=e, check=check)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--source", default="data/wallets_today.json")
    a = ap.parse_args()
    py = sys.executable
    fast = {"PM_MIN_INTERVAL": "0.01"}
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = os.path.join("forward", f"strategies_{date}.json")
    if not os.path.exists(os.path.join(ROOT, a.source)):
        sys.exit(f"нет сбора {a.source} — сначала утренний pipeline")
    run(py, "forward/screen.py", "--wallets-json", a.source, "--out", out, env=fast)
    n = len(json.load(open(os.path.join(ROOT, out))))
    if n:
        run(py, "forward/fwd_sim.py", "enroll", "--strategies", out)
    else:
        os.remove(os.path.join(ROOT, out))
    run(py, "forward/fwd_sim.py", "update", env=fast)
    print(f"ежедневный отбор {date}: зачислено {n}", file=sys.stderr)
    if a.push:
        files = ["forward/fwd.json", "forward/FWD_REPORT.md", "forward/screened.json.gz"] + ([out] if n else [])
        run("git", "add", *files)
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode != 0:
            run("git", "commit", "-q", "-m", f"Polymarket: симуляция 2, ежедневный отбор {date}: +{n}")
            for i in range(5):
                if run("git", "push", check=False).returncode == 0:
                    break
                time.sleep(2 ** (i + 1))


if __name__ == "__main__":
    main()
