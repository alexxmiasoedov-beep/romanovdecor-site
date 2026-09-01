#!/usr/bin/env python3
"""Поиск арбитража и перекосов цен между Фонбетом и Полимаркетом.

Логика:
  1. Тянем прематч-линию Фонбета (неофициальный JSON-эндпоинт, lang=en).
  2. Тянем матчевые рынки Полимаркета (gamma-api, sportsMarketType=moneyline).
  3. Матчим события по названиям команд (fuzzy) и времени начала (±3 ч).
  4. Считаем:
     - чистый арбитраж: покрываем все исходы самой дешёвой стороной из двух
       площадок; если суммарная цена < 1 — гарантированная прибыль;
     - value-перекосы: цена Полимаркета против безмаржевой вероятности
       Фонбета (маржа букмекера снимается пропорционально).

Цены Полимаркета в выгрузке gamma — mid. Перед реальной сделкой проверь
стакан флагом --books (тянет best ask из CLOB для найденных кандидатов).

Примеры:
  python3 arb_scan.py                        # скан с настройками по умолчанию
  python3 arb_scan.py --days 3 --min-edge 4  # горизонт 3 дня, перекосы от 4%
  python3 arb_scan.py --books --bankroll 100 # проверить стаканом, раскладка на $100
"""

import argparse
import difflib
import gzip
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

FONBET_LINE = "https://line01i.bk6bba-resources.com/events/list?lang=en&scopeMarket=1600"
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

# Лиги Полимаркета, где бывают матчевые moneyline-рынки.
PM_TAGS = [
    "epl", "la-liga", "serie-a", "bundesliga", "ligue-1", "ucl", "uel",
    "mls", "tennis", "atp", "wta", "nba", "nhl", "mlb",
]

# Факторы Фонбета: 921 = П1, 922 = ничья, 923 = П2.
F_W1, F_DRAW, F_W2 = 921, 922, 923

STOPWORDS = {
    "fc", "cf", "afc", "cd", "sc", "ac", "as", "ss", "us", "bk", "fk", "sk",
    "if", "bc", "hc", "club", "de", "the", "town", "city", "united", "utd",
    "calcio", "cfc", "1", "futbol", "futebol", "deportivo", "real",
}


def http_json(url, timeout=45, retries=4):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
                 "Accept-Encoding": "gzip"},
    )
    delay = 2
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
            return json.loads(raw)
        except (urllib.error.URLError, ConnectionError, TimeoutError, OSError):
            if attempt == retries:
                raise
            time.sleep(delay)
            delay *= 2


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    toks = [t for t in s.split() if t not in STOPWORDS]
    return " ".join(toks) or s.strip()


def sim(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    seq = difflib.SequenceMatcher(None, na, nb).ratio()
    ta, tb = set(na.split()), set(nb.split())
    jac = len(ta & tb) / len(ta | tb) if ta | tb else 0.0
    return max(seq, jac)


def pair_score(pm, fb):
    """Сходство пары команд; пробуем прямой и перевёрнутый порядок."""
    direct = min(sim(pm["team1"], fb["team1"]), sim(pm["team2"], fb["team2"]))
    swapped = min(sim(pm["team1"], fb["team2"]), sim(pm["team2"], fb["team1"]))
    return (direct, False) if direct >= swapped else (swapped, True)


def fetch_fonbet(now, horizon):
    d = http_json(FONBET_LINE)
    facts = {}
    for cf in d.get("customFactors", []):
        facts[cf["e"]] = {f["f"]: f.get("v") for f in cf.get("factors", [])
                          if f.get("f") in (F_W1, F_DRAW, F_W2)}
    sports = {s["id"]: s for s in d.get("sports", [])}

    def top_sport(sid):
        seen = set()
        while sid in sports and sports[sid].get("parentId") and sid not in seen:
            seen.add(sid)
            sid = sports[sid]["parentId"]
        return sports.get(sid, {}).get("name", "?")

    games = []
    for e in d.get("events", []):
        if e.get("level") != 1 or not e.get("team1") or not e.get("team2"):
            continue
        ks = facts.get(e["id"]) or {}
        if F_W1 not in ks or F_W2 not in ks:
            continue
        kickoff = datetime.fromtimestamp(e.get("startTime", 0), tz=timezone.utc)
        if not (now - timedelta(hours=1) <= kickoff <= now + horizon):
            continue
        games.append({
            "team1": e["team1"], "team2": e["team2"], "kickoff": kickoff,
            "sport": top_sport(e.get("sportId")),
            "league": sports.get(e.get("sportId"), {}).get("name", ""),
            "odds": {"1": ks.get(F_W1), "X": ks.get(F_DRAW), "2": ks.get(F_W2)},
        })
    return games


def parse_game_start(s):
    if not s:
        return None
    s = s.strip().replace(" ", "T")
    if s.endswith("+00"):
        s += ":00"
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(s).astimezone(timezone.utc)
    except ValueError:
        return None


def fetch_polymarket(now, horizon):
    games, seen = [], set()
    for tag in PM_TAGS:
        url = f"{GAMMA}/events?closed=false&limit=100&tag_slug={urllib.parse.quote(tag)}"
        try:
            events = http_json(url)
        except Exception as ex:  # тег может не существовать — не падаем
            print(f"  ! {tag}: {ex}", file=sys.stderr)
            continue
        for ev in events:
            if ev.get("id") in seen:
                continue
            mls = [m for m in ev.get("markets", [])
                   if m.get("sportsMarketType") == "moneyline"
                   and m.get("active") and not m.get("closed")]
            if not mls:
                continue
            kickoff = parse_game_start(mls[0].get("gameStartTime"))
            if not kickoff or not (now - timedelta(hours=1) <= kickoff <= now + horizon):
                continue
            seen.add(ev.get("id"))
            title = ev.get("title", "")
            m_vs = re.split(r"\s+vs\.?\s+", re.sub(r"^[^:]*:\s*", "", title), flags=re.I)
            g = {"kickoff": kickoff, "title": title, "slug": ev.get("slug", ""),
                 "tag": tag, "prices": {}, "tokens": {}}
            if len(mls) == 1 and len(json.loads(mls[0].get("outcomes", "[]"))) == 2 and "draw" not in mls[0].get("question", "").lower():
                # теннис и прочие двухисходники: один рынок, исходы = игроки
                m = mls[0]
                outs = json.loads(m.get("outcomes", "[]"))
                prices = [float(x) for x in json.loads(m.get("outcomePrices", "[]"))]
                toks = json.loads(m.get("clobTokenIds", "[]"))
                if len(m_vs) != 2:
                    continue
                g["team1"], g["team2"] = m_vs[0].strip(), m_vs[1].strip()
                # сопоставляем исходы с командами из заголовка
                if sim(outs[0], g["team1"]) >= sim(outs[0], g["team2"]):
                    order = (0, 1)
                else:
                    order = (1, 0)
                g["prices"]["1"], g["prices"]["2"] = prices[order[0]], prices[order[1]]
                g["tokens"]["1"], g["tokens"]["2"] = toks[order[0]], toks[order[1]]
            else:
                if len(m_vs) != 2:
                    continue
                g["team1"], g["team2"] = m_vs[0].strip(), m_vs[1].strip()
                for m in mls:
                    q = m.get("question", "")
                    try:
                        p_yes = float(json.loads(m.get("outcomePrices", "[]"))[0])
                        tok = json.loads(m.get("clobTokenIds", "[]"))[0]
                    except (ValueError, IndexError):
                        continue
                    if re.search(r"\bdraw\b", q, flags=re.I):
                        key = "X"
                    elif sim(q, g["team1"]) >= sim(q, g["team2"]):
                        key = "1"
                    else:
                        key = "2"
                    g["prices"][key] = p_yes
                    g["tokens"][key] = tok
            if "1" in g["prices"] and "2" in g["prices"]:
                games.append(g)
    return games


def best_ask(token_id):
    try:
        book = http_json(f"{CLOB}/book?token_id={token_id}", timeout=20)
        asks = [float(a["price"]) for a in book.get("asks", []) if float(a.get("size", 0)) > 0]
        return min(asks) if asks else None
    except Exception:
        return None


def analyze(pm, fb, swapped):
    """Возвращает (запись-результат) для сматченной пары."""
    odds = dict(fb["odds"])
    if swapped:
        odds["1"], odds["2"] = odds["2"], odds["1"]
    keys = [k for k in ("1", "X", "2") if k in pm["prices"] and odds.get(k)]
    # исходов должно хватать на полное покрытие: 3 для футбола, 2 без ничьей
    full = ("X" in keys) == ("X" in pm["prices"] and bool(odds.get("X")))
    if len(keys) < 2 or not full:
        return None
    inv = {k: 1.0 / odds[k] for k in keys}
    margin = sum(inv.values()) - 1.0
    fair = {k: inv[k] / (1.0 + margin) for k in keys}

    # чистый арбитраж: на каждый исход берём дешёвую сторону
    legs, cost = {}, 0.0
    for k in keys:
        pm_p, fb_p = pm["prices"][k], inv[k]
        if pm_p <= fb_p:
            legs[k] = ("PM", pm_p)
            cost += pm_p
        else:
            legs[k] = ("FB", fb_p)
            cost += fb_p
    edges = {k: fair[k] - pm["prices"][k] for k in keys}
    best_k = max(edges, key=lambda k: abs(edges[k]))
    return {
        "pm": pm, "fb": fb, "swapped": swapped,
        "keys": keys, "odds": odds, "fair": fair,
        "margin": margin, "legs": legs, "cost": cost,
        "arb": cost < 1.0, "profit": 1.0 / cost - 1.0 if cost < 1.0 else 0.0,
        "edges": edges, "best_edge_key": best_k, "best_edge": edges[best_k],
    }


def main():
    ap = argparse.ArgumentParser(description="Арбитраж Фонбет ↔ Полимаркет")
    ap.add_argument("--days", type=float, default=2, help="горизонт в днях (по умолчанию 2)")
    ap.add_argument("--min-sim", type=float, default=0.55, help="порог сходства имён (0..1)")
    ap.add_argument("--min-edge", type=float, default=3.0, help="порог перекоса, %% (по умолчанию 3)")
    ap.add_argument("--bankroll", type=float, default=100.0, help="банк для раскладки арбитража, $")
    ap.add_argument("--books", action="store_true",
                    help="проверить кандидатов реальным стаканом CLOB (медленнее)")
    ap.add_argument("--json", dest="json_out", metavar="FILE", help="сохранить результат в JSON")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    horizon = timedelta(days=args.days)

    print(f"Горизонт: до {(now + horizon):%Y-%m-%d %H:%M} UTC", file=sys.stderr)
    print("Тяну линию Фонбета…", file=sys.stderr)
    fb_games = fetch_fonbet(now, horizon)
    print(f"  Фонбет: {len(fb_games)} матчей с котировками", file=sys.stderr)
    print("Тяну рынки Полимаркета…", file=sys.stderr)
    pm_games = fetch_polymarket(now, horizon)
    print(f"  Полимаркет: {len(pm_games)} матчей (moneyline)", file=sys.stderr)

    results = []
    for pm in pm_games:
        best, best_score, best_swap = None, 0.0, False
        for fb in fb_games:
            if abs((pm["kickoff"] - fb["kickoff"]).total_seconds()) > 3 * 3600:
                continue
            score, swap = pair_score(pm, fb)
            if score > best_score:
                best, best_score, best_swap = fb, score, swap
        if not best or best_score < args.min_sim:
            continue
        r = analyze(pm, best, best_swap)
        if r:
            r["match_score"] = best_score
            results.append(r)

    print(f"Сматчено пар: {len(results)}\n", file=sys.stderr)

    if args.books:
        cands = [r for r in results
                 if r["arb"] or abs(r["best_edge"]) * 100 >= args.min_edge]
        print(f"Проверяю стаканы CLOB для {len(cands)} кандидатов…", file=sys.stderr)
        for r in cands:
            for k in r["keys"]:
                tok = r["pm"]["tokens"].get(k)
                ask = best_ask(tok) if tok else None
                if ask is not None:
                    r["pm"]["prices"][k] = ask
            upd = analyze(r["pm"], r["fb"], r["swapped"])
            if upd:
                r.update({k: upd[k] for k in
                          ("legs", "cost", "arb", "profit", "edges",
                           "best_edge_key", "best_edge", "fair")})

    arbs = sorted([r for r in results if r["arb"]], key=lambda r: -r["profit"])
    values = sorted([r for r in results if not r["arb"]
                     and abs(r["best_edge"]) * 100 >= args.min_edge],
                    key=lambda r: -abs(r["best_edge"]))

    def head(r):
        pm, fb = r["pm"], r["fb"]
        return (f"{pm['team1']} — {pm['team2']}  "
                f"[{fb['sport']}, {pm['kickoff']:%d.%m %H:%M} UTC, "
                f"матч имён {r['match_score']:.2f}]")

    label = {"1": "П1", "X": "Х", "2": "П2"}
    if arbs:
        print("=" * 72)
        print("ЧИСТЫЙ АРБИТРАЖ (сумма цен покрытия < 1)")
        print("=" * 72)
        for r in arbs:
            print(f"\n{head(r)}")
            print(f"  прибыль {r['profit'] * 100:.2f}% без риска, цена покрытия {r['cost']:.4f}")
            for k in r["keys"]:
                side, price = r["legs"][k]
                stake = args.bankroll * price / r["cost"]
                where = ("Полимаркет купить Yes" if side == "PM"
                         else f"Фонбет ставка (кф {r['odds'][k]:.2f})")
                print(f"    {label[k]:>2}: {where} по {price:.3f} — ставка ${stake:.2f}")
            print(f"  гарантированный возврат ${args.bankroll / r['cost']:.2f} "
                  f"с банка ${args.bankroll:.2f}")
    else:
        print("Чистого арбитража не найдено (это норма — окна живут минуты).")

    print()
    print("=" * 72)
    print(f"ПЕРЕКОСЫ ≥ {args.min_edge:.0f}% (цена ПМ против безмаржевой вероятности ФБ)")
    print("=" * 72)
    if not values:
        print("Существенных перекосов нет.")
    for r in values[:20]:
        print(f"\n{head(r)}  маржа ФБ {r['margin'] * 100:.1f}%")
        for k in r["keys"]:
            e = r["edges"][k] * 100
            mark = "  <-- " + ("ПМ дешевле (кандидат на покупку Yes)" if e > 0
                               else "ПМ дороже (кандидат на покупку No)") \
                if k == r["best_edge_key"] else ""
            print(f"    {label[k]:>2}: ПМ {r['pm']['prices'][k]:.3f} | "
                  f"ФБ кф {r['odds'][k]:.2f} → честно {r['fair'][k]:.3f} | "
                  f"перекос {e:+.1f}%{mark}")

    if args.json_out:
        def enc(o):
            if isinstance(o, datetime):
                return o.isoformat()
            raise TypeError
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump([{**r, "fb": {**r["fb"]}, "pm": {**r["pm"]}} for r in results],
                      f, ensure_ascii=False, default=enc, indent=1)
        print(f"\nПолный результат: {args.json_out}", file=sys.stderr)


if __name__ == "__main__":
    main()
