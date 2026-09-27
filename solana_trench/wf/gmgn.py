"""GMGN как источник кандидатов и справочных метрик.

API у GMGN неофициальный, за Cloudflare. Обычный requests получает 403,
но с TLS-отпечатком браузера (curl_cffi, impersonate="chrome") без
логина отдаются:
  - рейтинги кошельков по тегам (winrate, pnl, avg hold, распределение PnL);
  - топ трейдеров по токену (/vas/api/v1/token_traders);
  - часть статистики кошелька (/api/v1/wallet_stat).
Лента сделок, холдинги и календарь PnL требуют cookie сессии:
  export GMGN_COOKIE='cf_clearance=...; ...'   # DevTools -> Network -> любой запрос gmgn.ai
  export GMGN_UA='Mozilla/5.0 ...'             # тот же User-Agent, что в браузере
Всё, что GMGN показывает по сделкам, мы и так восстанавливаем из блокчейна
(positions_<wallet>.json); GMGN здесь — источник кандидатов и сверка.
"""
import os
import time

try:
    from curl_cffi import requests as _cffi
except ImportError:            # pip install curl_cffi
    _cffi = None
import requests as _plain

BASE = "https://gmgn.ai"
_COMMON = {"device_id": "wf", "client_id": "gmgn_web", "from_app": "gmgn", "app_ver": "1",
           "tz_name": "UTC", "tz_offset": "0", "app_lang": "en"}
RANK_TAGS = (None, "smart_degen", "pump_smart", "renowned")   # None = общий рейтинг


class Gmgn:
    def __init__(self, cookie=None, ua=None, delay_sec=1.0):
        self.cookie = cookie or os.environ.get("GMGN_COOKIE")
        self.ua = ua or os.environ.get("GMGN_UA")
        self.delay = delay_sec
        self.ca = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE") or True
        self.headers = {"accept": "application/json", "referer": BASE + "/"}
        if self.cookie:
            self.headers["cookie"] = self.cookie
        if self.ua:
            self.headers["user-agent"] = self.ua
        self.available = True
        self.impersonate = _cffi is not None
        self._last = 0.0

    def get(self, path, params=None):
        if not self.available:
            return None
        wait = self.delay - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.monotonic()
        p = {**_COMMON, **(params or {})}
        for attempt in range(3):
            try:
                if self.impersonate:
                    r = _cffi.get(BASE + path, params=p, headers=self.headers, impersonate="chrome", verify=self.ca, timeout=30)
                else:
                    r = _plain.get(BASE + path, params=p, headers=self.headers, timeout=30)
            except Exception:
                time.sleep(2); continue
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1)); continue
            if r.status_code in (403, 404):
                return None
            try:
                j = r.json()
            except Exception:
                return None
            return j.get("data") if isinstance(j, dict) else j
        return None

    def check(self):
        """Доступен ли GMGN отсюда (иначе считаем, что нет, и не долбим)."""
        d = self.get("/defi/quotation/v1/rank/sol/wallets/7d", {"orderby": "pnl_7d", "direction": "desc"})
        self.available = bool(d)
        return self.available

    def top_wallets(self, period="7d", tag=None, orderby="pnl_7d"):
        """Рейтинг GMGN. -> [{wallet, gmgn: {...}}], ~100 штук на тег."""
        params = {"orderby": orderby, "direction": "desc"}
        if tag:
            params["tag"] = tag
        d = self.get(f"/defi/quotation/v1/rank/sol/wallets/{period}", params) or {}
        rows = d.get("rank", []) if isinstance(d, dict) else d
        return [{"wallet": r.get("wallet_address") or r.get("address"), "gmgn": r}
                for r in rows or [] if r.get("wallet_address") or r.get("address")]

    def token_traders(self, mint, orderby="profit", limit=100):
        """Топ трейдеров по токену (avg_cost, avg_sold, buy/sell counts, is_on_curve, is_suspicious…)."""
        d = self.get(f"/vas/api/v1/token_traders/sol/{mint}", {"orderby": orderby, "direction": "desc", "limit": limit}) or {}
        rows = d.get("list", []) if isinstance(d, dict) else d
        return [{"wallet": r.get("address") or r.get("account_address"), "gmgn": r}
                for r in rows or [] if r.get("address") or r.get("account_address")]

    def wallet_stat(self, wallet, period="7d"):
        """Сводка кошелька (без логина часть полей пустая)."""
        return self.get(f"/api/v1/wallet_stat/sol/{wallet}/{period}")

    def wallet_activity(self, wallet, limit=100):
        """Лента сделок с ценами — нужна cookie сессии."""
        d = self.get("/defi/quotation/v1/wallet_activity/sol", [("type", "buy"), ("type", "sell"), ("wallet", wallet), ("limit", limit), ("cost", 10)]) or {}
        return d.get("activities", []) if isinstance(d, dict) else []

    def wallet_holdings(self, wallet, limit=100):
        """Холдинги с PnL по токенам — нужна cookie сессии."""
        d = self.get(f"/api/v1/wallet_holdings/sol/{wallet}", {"limit": limit, "orderby": "last_active_timestamp",
                                                             "direction": "desc", "showsmall": "true", "sellout": "true"}) or {}
        return d.get("holdings", d.get("list", [])) if isinstance(d, dict) else []


def gmgn_summary(g):
    """Короткая сводка полей рейтинга для отчёта."""
    if not g:
        return {}
    def f(k):
        v = g.get(k)
        try:
            return round(float(v), 4) if v is not None else None
        except (TypeError, ValueError):
            return None
    return {"gmgn_pnl_7d": f("pnl_7d"), "gmgn_winrate_7d": f("winrate_7d"), "gmgn_realized_7d": f("realized_profit_7d"),
            "gmgn_txs_7d": g.get("txs_7d"), "gmgn_avg_hold_7d_sec": f("avg_holding_period_7d"),
            "gmgn_tags": ",".join(g.get("tags") or [])}


def read_wallets_file(path):
    """Файл: адрес в строке или CSV, где первая колонка — адрес."""
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
