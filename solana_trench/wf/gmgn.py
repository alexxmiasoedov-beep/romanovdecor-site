"""GMGN как источник кандидатов и справочных метрик.

API у GMGN неофициальный и закрыт Cloudflare: из серверной среды отдаёт 403,
с домашней машины работает с cookie браузерной сессии. Поэтому:

  export GMGN_COOKIE='cf_clearance=...; ...'   # из DevTools -> Network -> любой запрос gmgn.ai
  export GMGN_UA='Mozilla/5.0 ... Chrome/...'  # тот же User-Agent, что в браузере

Если cookie нет — модуль молча возвращает пустые списки, а кандидаты
берутся из on-chain discover. Список кошельков из GMGN можно и просто
скопировать в файл и передать `run.py --wallets-file`.
"""
import os
import time

import requests

BASE = "https://gmgn.ai"
_COMMON = {"device_id": "wf", "client_id": "gmgn_web", "from_app": "gmgn", "app_ver": "1",
           "tz_name": "UTC", "tz_offset": "0", "app_lang": "en"}


class Gmgn:
    def __init__(self, cookie=None, ua=None, delay_sec=1.0):
        self.cookie = cookie or os.environ.get("GMGN_COOKIE")
        self.ua = ua or os.environ.get("GMGN_UA") or "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36"
        self.delay = delay_sec
        self.session = requests.Session()
        self.session.headers.update({"user-agent": self.ua, "accept": "application/json", "referer": BASE + "/"})
        if self.cookie:
            self.session.headers["cookie"] = self.cookie
        self.available = bool(self.cookie)
        self._last = 0.0

    def get(self, path, params=None):
        if not self.available:
            return None
        wait = self.delay - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.monotonic()
        r = self.session.get(BASE + path, params={**_COMMON, **(params or {})}, timeout=30)
        if r.status_code == 403:
            self.available = False          # cookie протухла — дальше не долбим
            return None
        r.raise_for_status()
        j = r.json()
        return j.get("data") if isinstance(j, dict) else j

    def top_wallets(self, period="7d", tag=None, orderby="pnl_7d"):
        """Рейтинг кошельков GMGN (Smart money / KOL / …). -> [{wallet, pnl, winrate, ...}]"""
        params = {"orderby": orderby, "direction": "desc"}
        if tag:
            params["tag"] = tag
        d = self.get(f"/defi/quotation/v1/rank/sol/wallets/{period}", params) or {}
        rows = d.get("rank", d) if isinstance(d, dict) else d
        return [{"wallet": r.get("wallet_address") or r.get("address"), "gmgn": r} for r in rows or [] if r.get("wallet_address") or r.get("address")]

    def top_traders(self, mint, orderby="profit"):
        """Топ трейдеров по токену. -> [{wallet, profit, ...}]"""
        d = self.get(f"/defi/quotation/v1/tokens/top_traders/sol/{mint}", {"orderby": orderby, "direction": "desc"}) or []
        return [{"wallet": r.get("address"), "gmgn": r} for r in d if r.get("address")]

    def wallet_stats(self, wallet, period="7d"):
        """Сводка кошелька GMGN (winrate, pnl, avg hold, ...) — для сверки с нашими метриками."""
        return self.get(f"/defi/quotation/v1/smartmoney/sol/walletNew/{wallet}", {"period": period})


def read_wallets_file(path):
    """Файл: адрес в строке или CSV, где первая колонка/колонка wallet — адрес."""
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cell = line.split(",")[0].split(";")[0].split("\t")[0].strip().strip('"')
            if 32 <= len(cell) <= 44 and cell.isalnum():
                out.append(cell)
    return list(dict.fromkeys(out))
