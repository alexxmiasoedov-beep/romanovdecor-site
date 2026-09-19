"""Прогон всей воронки подряд."""
import subprocess
import sys

for cmd in (["collect_wallets.py"], ["stage1_screen.py", "--workers", "24"], ["stage2_analyze.py"],
            ["stage3_markout.py"], ["report.py"]):
    print(">>", " ".join(cmd), file=sys.stderr)
    subprocess.run([sys.executable, *cmd], check=True)
