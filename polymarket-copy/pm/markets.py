"""Метаданные рынков: локальный стор + классификация в дерево сегментов."""
from __future__ import annotations

import json
import os
import re
import threading
import time
from datetime import datetime, timezone

from . import api, config

STORE = os.path.join(os.path.dirname(__file__), "..", "data", "markets.json")
_lock = threading.Lock()
_store: dict[str, dict] | None = None

SPORT_BY_SERIES = [
    (r"\b(epl|la-?liga|serie-?a|bundesliga|ligue-?1|ucl|uel|uecl|mls|soccer|fifa|world-cup|eredivisie|"
     r"liga-mx|copa|premier-league|championship|primeira|primera|super-lig|saudi|brasileirao|libertadores|friendl|open-cup|"
     r"euro|football-(?!american)|efl|fa-cup|dfb|coppa|nations-league|afc|caf|concacaf)", "Soccer"),
    (r"\b(nba|wnba|ncaab|cbb|euroleague|basketball|fiba|nbl|acb)", "Basketball"),
    (r"\b(nfl|ncaaf|cfb|american-football)", "American Football"),
    (r"\b(mlb|baseball|kbo|npb)", "Baseball"),
    (r"\b(nhl|hockey|khl|shl)", "Hockey"),
    (r"\b(atp|wta|tennis|wimbledon|us-open|roland|australian-open|challenger|itf|centurion)", "Tennis"),
    (r"\b(ufc|mma|boxing|pfl|bellator|one-championship)", "MMA/Boxing"),
    (r"\b(cs2|csgo|counter-strike|lol|league-of-legends|dota|valorant|esports|overwatch|rocket-league|"
     r"starcraft|rainbow|call-of-duty|cod|pubg|mlbb|mobile-legends|honor-of-kings|hok|kog)", "Esports"),
    (r"\b(f1|formula|nascar|motogp|indycar)", "Motorsport"),
    (r"\b(cricket|ipl|bbl|t20|odi|test-match|psl|cpl|hundred)", "Cricket"),
    (r"\b(golf|pga|masters|ryder|liv)", "Golf"),
    (r"\b(rugby|nrl|super-rugby|six-nations)", "Rugby"),
    (r"\b(volleyball|handball|darts|snooker|table-tennis|badminton|cycling|tour-de|athletics|olympic|"
     r"chess|afl|lacrosse|pickleball|swimming)", "Other sport"),
]
CRYPTO_RE = re.compile(r"\b(btc|bitcoin|eth|ethereum|sol|solana|xrp|doge|crypto|bnb|ada|token|coin|"
                       r"hyperliquid|memecoin|altcoin|stablecoin|binance|coinbase|defi|nft|airdrop)\b", re.I)


def _load() -> dict[str, dict]:
    global _store
    if _store is None:
        if os.path.exists(STORE):
            with open(STORE) as f:
                _store = json.load(f)
        else:
            _store = {}
    return _store


_last_save = 0.0


def _maybe_save(every: float = 300) -> None:
    """Стор большой, пишем на диск не чаще раза в `every` секунд; финальный save() — в конце прогона."""
    global _last_save
    if time.time() - _last_save > every:
        _last_save = time.time()
        save()


def save() -> None:
    with _lock:
        tmp = STORE + ".tmp"
        with open(tmp, "w") as f:
            json.dump(dict(_load()), f)
        os.replace(tmp, STORE)


def _iso(s: str | None) -> float:
    if not s:
        return 0.0
    s = s.replace(" ", "T").replace("+00", "+00:00")
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(s).timestamp()
    except ValueError:
        return 0.0


def compact(m: dict) -> dict:
    ev = (m.get("events") or [{}])[0]
    series = (ev.get("series") or [{}])
    series = series[0] if series else {}
    try:
        prices = [float(x) for x in json.loads(m.get("outcomePrices") or "[]")]
    except (ValueError, TypeError):
        prices = []
    try:
        tokens = json.loads(m.get("clobTokenIds") or "[]")
    except (ValueError, TypeError):
        tokens = []
    return {
        "conditionId": m.get("conditionId"), "question": m.get("question"), "slug": m.get("slug"),
        "closed": bool(m.get("closed")), "outcomePrices": prices, "tokens": tokens,
        "volume": float(m.get("volumeNum") or 0), "liquidity": float(m.get("liquidityNum") or 0),
        "endDate": _iso(m.get("endDate")), "closedTime": _iso(m.get("closedTime")),
        "gameStartTime": _iso(m.get("gameStartTime")), "sportsMarketType": m.get("sportsMarketType"),
        "negRisk": bool(m.get("negRisk")), "event_id": ev.get("id"), "event_slug": ev.get("slug"),
        "series_slug": ev.get("seriesSlug") or series.get("slug"), "series_title": series.get("title"),
        "game_id": ev.get("gameId") or m.get("gameId"), "fetched": time.time(),
    }


def ensure(condition_ids, refresh_open_after: float = 6 * 3600) -> dict[str, dict]:
    """Гарантирует наличие метаданных по всем conditionId; незакрытые рынки перепрашивает."""
    st = _load()
    now = time.time()
    with _lock:
        need = [c for c in dict.fromkeys(condition_ids) if c and (
            c not in st or (not st[c]["closed"] and now - st[c]["fetched"] > refresh_open_after))]
    if need:
        for i in range(0, len(need), 20):
            batch = need[i:i + 20]
            # Gamma по умолчанию отдаёт только открытые рынки — спрашиваем оба среза
            res = (api.get(f"{api.GAMMA}/markets", {"condition_ids": batch, "closed": "true", "limit": 50},
                           cache=False) or [])
            got = {m["conditionId"] for m in res}
            rest = [c for c in batch if c not in got]
            if rest:
                res += api.get(f"{api.GAMMA}/markets", {"condition_ids": rest, "closed": "false", "limit": 50},
                               cache=False) or []
            with _lock:
                for m in res:
                    st[m["conditionId"]] = compact(m)
                for c in batch:
                    st.setdefault(c, {"conditionId": c, "closed": False, "outcomePrices": [], "tokens": [],
                                      "volume": 0, "liquidity": 0, "endDate": 0, "closedTime": 0,
                                      "gameStartTime": 0, "sportsMarketType": None, "negRisk": False,
                                      "event_id": None, "series_slug": None, "series_title": None,
                                      "game_id": None, "question": "?", "slug": "", "fetched": now,
                                      "missing": True})
        _maybe_save()
    with _lock:
        return {c: st[c] for c in dict.fromkeys(condition_ids) if c in st}


_event_tags: dict[str, list[str]] = {}
TAGS_STORE = os.path.join(os.path.dirname(__file__), "..", "data", "event_tags.json")


def event_tags(event_id) -> list[str]:
    if not event_id:
        return []
    eid = str(event_id)
    if not _event_tags and os.path.exists(TAGS_STORE):
        with _lock:
            if not _event_tags:
                with open(TAGS_STORE) as f:
                    _event_tags.update(json.load(f))
    if eid not in _event_tags:
        ev = api.event(eid)
        _event_tags[eid] = [t.get("label") for t in (ev or {}).get("tags", []) if t.get("label")]
        if len(_event_tags) % 50 == 0:
            with _lock:
                snapshot = dict(_event_tags)
                with open(TAGS_STORE + ".tmp", "w") as f:
                    json.dump(snapshot, f)
                os.replace(TAGS_STORE + ".tmp", TAGS_STORE)
    return _event_tags[eid]


def classify(m: dict, fetch_tags: bool = True) -> dict:
    """→ {category, sub, league, mtype, is_sport, short_crypto}"""
    text = " ".join(str(x or "") for x in (m.get("slug"), m.get("event_slug"), m.get("series_slug"),
                                              m.get("series_title"), m.get("question")))
    low = text.lower().replace(" ", "-")
    short_crypto = any(p.lower() in low for p in config.SHORT_CRYPTO_PATTERNS)
    is_sport = bool(m.get("sportsMarketType") or m.get("gameStartTime") or m.get("game_id"))
    league = m.get("series_title") or m.get("series_slug") or "?"
    if short_crypto:
        return {"category": "Crypto", "sub": "Up/Down short", "league": league, "mtype": "updown",
                "is_sport": False, "short_crypto": True}
    if is_sport:
        sub = "Other sport"
        for rx, name in SPORT_BY_SERIES:
            if re.search(rx, low):
                sub = name
                break
        cat = "Esports" if sub == "Esports" else "Sports"
        mtype = m.get("sportsMarketType") or "binary"
        return {"category": cat, "sub": sub, "league": league, "mtype": mtype, "is_sport": True,
                "short_crypto": False}
    tags = event_tags(m.get("event_id")) if fetch_tags else []
    cat = "Other"
    for c in config.CATEGORY_ORDER:
        if c in tags:
            cat = c
            break
    if cat == "Other" and CRYPTO_RE.search(low):
        cat = "Crypto"
    sub = next((t for t in tags if t not in config.CATEGORY_ORDER), None) or league
    mtype = "negrisk" if m.get("negRisk") else "binary"
    return {"category": cat, "sub": sub, "league": league, "mtype": mtype, "is_sport": False,
            "short_crypto": False}
