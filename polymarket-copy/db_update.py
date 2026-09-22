"""Занести результаты прогона (stage1/2/3.csv) в реестр. Вызывается после каждого прогона."""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from datetime import datetime, timezone

from pm import registry

D = os.path.join(os.path.dirname(__file__), "data")


def load_csv(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return []
    with open(p) as f:
        return list(csv.DictReader(f))


def main() -> None:
    db = registry.load()
    with open(os.path.join(D, "wallets_today.json")) as f:
        wt = json.load(f)
    today = wt["wallets"]
    run_date = datetime.fromtimestamp(wt.get("collected_at", time.time()), timezone.utc).strftime("%Y-%m-%d")
    s1 = {r["wallet"]: r for r in load_csv("stage1.csv")}
    s2 = {r["wallet"]: r for r in load_csv("stage2.csv")}
    s3 = {r["wallet"]: r for r in load_csv("stage3.csv")}
    n_new = 0
    for w, d in today.items():
        is_new = w not in db["wallets"]
        rec = registry.get(db, w)
        n_new += is_new
        rec["last_seen"] = time.time()
        rec["name"] = rec["name"] or d.get("name", "")
        run = {"seen": True}
        if w in s1:
            run["stage1"] = s1[w]["pass"] == "True"
            run["stage1_fail"] = s1[w]["fail_reasons"]
        if w in s2:
            r = s2[w]
            run["stage2"] = r["pass"]
            run["stage2_fail"] = r["fail_reasons"]
            for k in ("roi_copy", "t_stat", "closed_n", "conc_p95", "median_hold_h", "top_category", "score"):
                run[k] = r.get(k)
            if r["pass"] in ("True", "segment"):
                rec["approved_segments"] = r.get("approved_segments", "")
        if w in s3:
            r = s3[w]
            run["stage3"] = r["pass"] == "True"
            run["stage3_fail"] = r["fail_reasons"]
            for k in ("roi_delay_0.5m", "roi_delay_5m", "skip_share", "final_score"):
                run[k] = r.get(k)
        rec["runs"][run_date] = run
    db.setdefault("run_log", []).append({"date": run_date, "collected": len(today), "stage1_pass": sum(1 for r in s1.values() if r["pass"] == "True"),
                                         "stage2_pass": sum(1 for r in s2.values() if r["pass"] in ("True", "segment")),
                                         "stage3_pass": sum(1 for r in s3.values() if r["pass"] == "True")})
    registry.save(db)
    print(f"реестр: {len(db['wallets'])} кошельков, новых {n_new}, прогон {run_date} записан", file=sys.stderr)


if __name__ == "__main__":
    main()
