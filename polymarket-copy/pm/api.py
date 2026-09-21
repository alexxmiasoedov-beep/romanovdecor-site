"""Тонкий клиент к публичным API Polymarket с дисковым кэшем и повторами.

Data API  : https://data-api.polymarket.com  (сделки, позиции, закрытые позиции)
Gamma API : https://gamma-api.polymarket.com (рынки, события, теги)
CLOB API  : https://clob.polymarket.com       (стакан, история цен)
"""
from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from typing import Any, Iterable

import requests

DATA = "https://data-api.polymarket.com"
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

CACHE_DIR = os.environ.get("PM_CACHE", os.path.join(os.path.dirname(__file__), "..", "data", "cache"))
_session = requests.Session()
_session.headers["User-Agent"] = "pm-copy-screener/0.1"
_lock = threading.Lock()
_last_call = 0.0
MIN_INTERVAL = float(os.environ.get("PM_MIN_INTERVAL", "0.05"))  # сек между запросами (глобально)


def _cache_path(url: str, params: dict | None) -> str:
    key = url + "?" + json.dumps(params or {}, sort_keys=True)
    h = hashlib.sha1(key.encode()).hexdigest()
    sub = os.path.join(CACHE_DIR, h[:2])
    os.makedirs(sub, exist_ok=True)
    return os.path.join(sub, h + ".json")


def get(url: str, params: dict | None = None, *, cache: bool = True, ttl: float | None = None,
        retries: int = 5, timeout: int = 30) -> Any:
    """GET с кэшем. ttl=None: кэш вечный; ttl в секундах: перезапрос по истечении."""
    global _last_call
    path = _cache_path(url, params)
    if cache and os.path.exists(path):
        if ttl is None or time.time() - os.path.getmtime(path) < ttl:
            with open(path) as f:
                return json.load(f)
    delay = 1.0
    for attempt in range(retries):
        with _lock:
            wait = MIN_INTERVAL - (time.time() - _last_call)
            if wait > 0:
                time.sleep(wait)
            _last_call = time.time()
        try:
            r = _session.get(url, params=params, timeout=timeout)
            if r.status_code == 429 or r.status_code >= 500:
                raise requests.HTTPError(f"{r.status_code} {url}")
            if r.status_code == 404:
                data = None
            else:
                r.raise_for_status()
                data = r.json()
            if cache:
                tmp = f"{path}.{threading.get_ident()}.tmp"  # уникально на поток: два потока могут писать один ключ
                with open(tmp, "w") as f:
                    json.dump(data, f)
                os.replace(tmp, path)
            return data
        except (requests.RequestException, ValueError) as e:
            if attempt == retries - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 20)


# ---------- Data API ----------

def trades_global(limit: int = 500, offset: int = 0, min_cash: float | None = None, **kw) -> list[dict]:
    p: dict[str, Any] = {"limit": limit, "offset": offset}
    if min_cash:
        p.update(filterType="CASH", filterAmount=min_cash)
    p.update(kw)
    return get(f"{DATA}/trades", p, cache=False) or []


def trades_user(wallet: str, max_pages: int = 21, ttl: float = 6 * 3600) -> list[dict]:
    """Вся история сделок кошелька (API отдаёт максимум ~10 500 сделок, offset ≤ 10000)."""
    out: list[dict] = []
    for page in range(max_pages):
        off = page * 500
        if off > 10000:
            break
        chunk = get(f"{DATA}/trades", {"user": wallet, "limit": 500, "offset": off}, ttl=ttl) or []
        out.extend(chunk)
        if len(chunk) < 500:
            break
    return out


def trades_market(condition_id: str, max_pages: int = 4, cache: bool = False) -> list[dict]:
    """Лента сделок рынка, новые первыми. cache=True — для уже резолвнутых рынков."""
    out: list[dict] = []
    for page in range(max_pages):
        if page * 500 > 10000:
            break
        chunk = get(f"{DATA}/trades", {"market": condition_id, "limit": 500, "offset": page * 500},
                    cache=cache) or []
        out.extend(chunk)
        if len(chunk) < 500:
            break
    return out


def positions(wallet: str, ttl: float = 6 * 3600, max_pages: int = 20) -> list[dict]:
    out: list[dict] = []
    for page in range(max_pages):
        chunk = get(f"{DATA}/positions", {"user": wallet, "limit": 500, "offset": page * 500,
                                          "sizeThreshold": 0}, ttl=ttl) or []
        out.extend(chunk)
        if len(chunk) < 500:
            break
    return out


def closed_positions(wallet: str, max_pages: int = 4, ttl: float = 6 * 3600) -> list[dict]:
    """Закрытые позиции (страница = 50 записей)."""
    out: list[dict] = []
    for page in range(max_pages):
        chunk = get(f"{DATA}/closed-positions", {"user": wallet, "limit": 50, "offset": page * 50},
                    ttl=ttl) or []
        out.extend(chunk)
        if len(chunk) < 50:
            break
    return out


# ---------- Gamma API ----------

def markets_by_condition(condition_ids: Iterable[str]) -> list[dict]:
    ids = list(dict.fromkeys(condition_ids))
    out: list[dict] = []
    for i in range(0, len(ids), 20):
        batch = ids[i:i + 20]
        res = get(f"{GAMMA}/markets", {"condition_ids": batch}) or []
        out.extend(res)
    return out


def event(event_id: str | int) -> dict | None:
    return get(f"{GAMMA}/events/{event_id}")


def top_events(limit: int = 200, closed: bool = False) -> list[dict]:
    out: list[dict] = []
    for off in range(0, limit, 100):
        chunk = get(f"{GAMMA}/events", {"order": "volume24hr", "ascending": "false", "limit": 100,
                                        "offset": off, "closed": str(closed).lower()}, cache=False) or []
        out.extend(chunk)
        if len(chunk) < 100:
            break
    return out[:limit]


# ---------- CLOB API ----------

def book(token_id: str) -> dict | None:
    return get(f"{CLOB}/book", {"token_id": token_id}, cache=False)


def prices_history(token_id: str, start_ts: int, end_ts: int, fidelity: int = 5) -> list[dict]:
    res = get(f"{CLOB}/prices-history", {"market": token_id, "startTs": start_ts, "endTs": end_ts,
                                          "fidelity": fidelity})
    return (res or {}).get("history", []) if isinstance(res, dict) else []


def pmap(fn, items, workers: int = 8, desc: str = ""):
    """Параллельный map с прогрессом в stderr; ошибки отдельного элемента → None."""
    import sys
    from concurrent.futures import ThreadPoolExecutor, as_completed
    items = list(items)
    results = [None] * len(items)
    done = 0
    t0 = time.time()
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(fn, it): i for i, it in enumerate(items)}
        for fut in as_completed(futs):
            i = futs[fut]
            try:
                results[i] = fut.result()
            except Exception as e:  # noqa: BLE001
                print(f"\n[{desc}] item {i} error: {e}", file=sys.stderr)
            done += 1
            if done % 25 == 0 or done == len(items):
                el = time.time() - t0
                print(f"\r[{desc}] {done}/{len(items)}  {el:.0f}s", end="", file=sys.stderr, flush=True)
    print(file=sys.stderr)
    return results
