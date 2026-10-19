"""Реестр кошельков: data/db/registry.json.gz (gzip-JSON; старый несжатый registry.json читается как фолбэк).

Запись кошелька:
  name, first_seen, last_seen            — когда впервые/последний раз попал в сбор
  runs: {дата: {stage1, stage2, stage3, roi_copy, t_stat, ...}}  — результат каждого прогона
  status: candidate | simulating | positive | negative | rejected
  batch, sim_start, approved_segments, tags (top5 и т.п.)
"""
from __future__ import annotations

import gzip
import json
import os
import time

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "db", "registry.json.gz")
LEGACY = PATH[:-3]  # несжатый файл до 11.10.2026; GitHub не принимает файлы >100 МБ


def load() -> dict:
    if os.path.exists(PATH):
        with gzip.open(PATH, "rt", encoding="utf-8") as f:
            return json.load(f)
    if os.path.exists(LEGACY):
        with open(LEGACY, encoding="utf-8") as f:
            return json.load(f)
    return {"wallets": {}, "batches": {}}


def save(db: dict) -> None:
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    tmp = PATH + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=6) as f:
        json.dump(db, f, ensure_ascii=False, sort_keys=True)
    os.replace(tmp, PATH)


def get(db: dict, wallet: str) -> dict:
    w = db["wallets"].setdefault(wallet, {
        "name": "", "first_seen": time.time(), "last_seen": 0, "runs": {}, "status": "candidate",
        "batch": None, "sim_start": None, "approved_segments": "", "tags": []})
    return w
