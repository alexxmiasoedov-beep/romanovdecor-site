"""GeckoTerminal: новые/активные пулы и последние сделки в пуле (без ключа)."""
import time
from datetime import datetime, timezone

import requests

BASE = "https://api.geckoterminal.com/api/v2/networks/solana"


class Gecko:
    def __init__(self, delay_sec=2.1):
        self.delay = delay_sec
        self.session = requests.Session()
        self.session.headers["accept"] = "application/json"
        self._last = 0.0

    def get(self, path, params=None):
        for attempt in range(5):
            wait = self.delay - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            r = self.session.get(BASE + path, params=params, timeout=30)
            if r.status_code == 429:
                time.sleep(10 * (attempt + 1))
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError("geckoterminal: rate limited")

    @staticmethod
    def _pool(p):
        a = p["attributes"]
        created = datetime.fromisoformat(a["pool_created_at"].replace("Z", "+00:00")).timestamp()
        return {
            "pool": a["address"],
            "name": a["name"],
            "dex": p["relationships"]["dex"]["data"]["id"],
            "mint": p["relationships"]["base_token"]["data"]["id"].split("_", 1)[1],
            "quote": p["relationships"]["quote_token"]["data"]["id"].split("_", 1)[1],
            "created": created,
            "liquidity_usd": float(a.get("reserve_in_usd") or 0),
            "volume_h24": float((a.get("volume_usd") or {}).get("h24") or 0),
            "fdv_usd": float(a.get("fdv_usd") or 0),
            "buyers_h24": ((a.get("transactions") or {}).get("h24") or {}).get("buyers", 0),
        }

    def new_pools(self, page=1):
        return [self._pool(p) for p in self.get("/new_pools", {"page": page})["data"]]

    def dex_pools(self, dex, page=1):
        return [self._pool(p) for p in self.get(f"/dexes/{dex}/pools", {"page": page})["data"]]

    def pool_trades(self, pool):
        """До 300 последних сделок за 24ч: кошелёк, сторона, объём."""
        out = []
        for t in self.get(f"/pools/{pool}/trades")["data"]:
            a = t["attributes"]
            out.append({
                "wallet": a["tx_from_address"],
                "kind": a["kind"],
                "usd": float(a.get("volume_in_usd") or 0),
                "time": datetime.fromisoformat(a["block_timestamp"].replace("Z", "+00:00")).timestamp(),
                "tx": a["tx_hash"],
            })
        return out


def sol_price_history(days=30):
    """CoinGecko: {день (unix, 00:00 UTC): цена SOL в USD}. Фолбэк — пусто."""
    try:
        r = requests.get("https://api.coingecko.com/api/v3/coins/solana/market_chart",
                         params={"vs_currency": "usd", "days": days, "interval": "daily"}, timeout=30)
        r.raise_for_status()
        return {int(ts // 1000) // 86400 * 86400: p for ts, p in r.json()["prices"]}
    except Exception:
        return {}


def sol_price_now():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price",
                         params={"ids": "solana", "vs_currencies": "usd"}, timeout=30)
        return float(r.json()["solana"]["usd"])
    except Exception:
        return None


def token_prices_native(mints):
    """DexScreener: текущая цена токена в SOL (для оценки незакрытых мешков)."""
    out = {}
    mints = list(dict.fromkeys(mints))
    for i in range(0, len(mints), 30):
        chunk = mints[i:i + 30]
        try:
            r = requests.get("https://api.dexscreener.com/tokens/v1/solana/" + ",".join(chunk), timeout=30)
            r.raise_for_status()
            for pair in r.json():
                m = pair["baseToken"]["address"]
                if pair.get("quoteToken", {}).get("symbol") not in ("SOL", "WSOL"):
                    continue
                liq = (pair.get("liquidity") or {}).get("usd") or 0
                cur = out.get(m)
                if cur is None or liq > cur[1]:
                    out[m] = (float(pair.get("priceNative") or 0), liq)
        except Exception:
            pass
        time.sleep(0.4)
    return {m: v[0] for m, v in out.items()}
