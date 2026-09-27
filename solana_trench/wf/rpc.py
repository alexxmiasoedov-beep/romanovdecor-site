"""JSON-RPC клиент Solana: троттлинг, ретраи на 429, кэш разобранных tx."""
import json
import os
import sqlite3
import threading
import time

import requests


class RateLimiter:
    def __init__(self, rps: float):
        self.interval = 1.0 / max(rps, 0.1)
        self.lock = threading.Lock()
        self.next_at = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            if now < self.next_at:
                time.sleep(self.next_at - now)
                now = time.monotonic()
            self.next_at = max(now, self.next_at) + self.interval


class Rpc:
    def __init__(self, url: str, rps: float = 15, cache_dir: str = "cache"):
        self.url = url
        self.limiter = RateLimiter(rps)
        self.session = requests.Session()
        os.makedirs(cache_dir, exist_ok=True)
        self.db_path = os.path.join(cache_dir, "cache.sqlite")
        self.db_lock = threading.Lock()
        with self._db() as db:
            db.execute("CREATE TABLE IF NOT EXISTS parsed_tx (sig TEXT PRIMARY KEY, data TEXT)")
            db.execute("CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT, ts REAL)")
        self.calls = 0

    def _db(self):
        return sqlite3.connect(self.db_path, timeout=30)

    def call(self, method, params, retries=6):
        delay = 1.0
        for attempt in range(retries):
            self.limiter.wait()
            try:
                r = self.session.post(self.url, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, timeout=60)
                self.calls += 1
            except requests.RequestException:
                time.sleep(delay); delay *= 2
                continue
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(delay); delay *= 2
                continue
            j = r.json()
            if "error" in j:
                code = j["error"].get("code")
                if code in (-32005, 429):   # node busy / rate limited
                    time.sleep(delay); delay *= 2
                    continue
                raise RuntimeError(f"rpc {method}: {j['error']}")
            return j.get("result")
        raise RuntimeError(f"rpc {method}: retries exhausted")

    # --- подписи ---
    def signatures(self, address, before=None, limit=1000):
        opts = {"limit": limit}
        if before:
            opts["before"] = before
        return self.call("getSignaturesForAddress", [address, opts]) or []

    def signatures_until(self, address, min_time, max_pages=10):
        """Подписи от новых к старым, пока blockTime >= min_time.
        Возвращает (список, exhausted) — exhausted=True, если история кончилась."""
        out, before = [], None
        for _ in range(max_pages):
            page = self.signatures(address, before=before)
            if not page:
                return out, True
            for s in page:
                if s.get("blockTime") is not None and s["blockTime"] < min_time:
                    out.extend(x for x in page if (x.get("blockTime") or 0) >= min_time)
                    return out, False
            out.extend(page)
            if len(page) < 1000:
                return out, True
            before = page[-1]["signature"]
        return out, False

    def oldest_signature(self, address, max_pages=30):
        """Самая старая подпись (для возраста и источника пополнения). None если история длиннее max_pages*1000."""
        before, last = None, None
        for _ in range(max_pages):
            page = self.signatures(address, before=before)
            if not page:
                return last
            last = page[-1]
            if len(page) < 1000:
                return last
            before = last["signature"]
        return None

    # --- транзакции ---
    def transaction(self, sig):
        return self.call("getTransaction", [sig, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}])

    def cached_parsed(self, sig):
        with self.db_lock, self._db() as db:
            row = db.execute("SELECT data FROM parsed_tx WHERE sig=?", (sig,)).fetchone()
        return json.loads(row[0]) if row else None

    def store_parsed(self, sig, data):
        with self.db_lock, self._db() as db:
            db.execute("INSERT OR REPLACE INTO parsed_tx VALUES (?,?)", (sig, json.dumps(data)))

    def kv_get(self, k, max_age=None):
        with self.db_lock, self._db() as db:
            row = db.execute("SELECT v, ts FROM kv WHERE k=?", (k,)).fetchone()
        if not row:
            return None
        if max_age is not None and time.time() - row[1] > max_age:
            return None
        return json.loads(row[0])

    def kv_set(self, k, v):
        with self.db_lock, self._db() as db:
            db.execute("INSERT OR REPLACE INTO kv VALUES (?,?,?)", (k, json.dumps(v), time.time()))
