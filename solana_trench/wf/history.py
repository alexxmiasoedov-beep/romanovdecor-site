"""История кошелька: дешёвый префильтр по подписям, потом полная загрузка свопов."""
import time
from concurrent.futures import ThreadPoolExecutor

from .parse_tx import parse_swap, first_funder, sanitize


def prefilter_wallet(rpc, wallet, cfg, now=None):
    """Возраст, число tx в окне, доля неудачных. Экономно по вызовам:
    первая страница подписей сразу выдаёт ботов (1000 tx за < N дней),
    а если в окне нашлась tx старше окна — кошелёк старше окна и возраст ясен.
    -> (info, reason) — reason=None если прошёл."""
    now = now or time.time()
    min_time = now - cfg.history_days * 86400
    info = {"wallet": wallet}
    first = rpc.signatures(wallet)
    if not first:
        info["tx_in_window"] = 0
        return info, "no_tx"
    if len(first) >= 1000:
        span_days = ((first[0].get("blockTime") or now) - (first[-1].get("blockTime") or now)) / 86400
        if span_days < 1000 / cfg.max_tx_per_day:
            info["tx_in_window"] = 1000; info["span_days"] = round(span_days, 2)
            return info, "too_many_tx_bot"
    sigs = [s for s in first if (s.get("blockTime") or 0) >= min_time]
    exhausted = len(first) < 1000
    older_seen = len(sigs) < len(first)
    before = first[-1]["signature"]
    max_pages = int(cfg.max_tx_per_day * cfg.history_days // 1000) + 1
    pages = 1
    while not exhausted and not older_seen and pages < max_pages:
        page = rpc.signatures(wallet, before=before)
        pages += 1
        if not page:
            exhausted = True; break
        keep = [s for s in page if (s.get("blockTime") or 0) >= min_time]
        sigs.extend(keep)
        older_seen = len(keep) < len(page)
        exhausted = len(page) < 1000
        before = page[-1]["signature"]
    info["sigs"] = sigs
    info["tx_in_window"] = len(sigs)
    failed = sum(1 for s in sigs if s.get("err"))
    info["failed_share"] = failed / len(sigs) if sigs else 0.0
    if len(sigs) < cfg.min_tx_in_window:
        return info, "too_few_tx"
    if len(sigs) / cfg.history_days > cfg.max_tx_per_day:
        return info, "too_many_tx_bot"
    if info["failed_share"] > cfg.max_failed_tx_share:
        return info, "failed_tx_spam"

    if older_seen:                      # есть tx старше окна: возраст > history_days
        info["age_days"] = cfg.history_days + 1
        info["first_sig"] = None        # первую tx ищем лениво (funder_of), только для прошедших
    elif exhausted:
        info["first_tx_time"] = sigs[-1].get("blockTime") or now
        info["first_sig"] = sigs[-1]["signature"]
        info["age_days"] = round((now - info["first_tx_time"]) / 86400, 1)
    else:                               # упёрлись в max_pages внутри окна — бот
        return info, "too_many_tx_bot"
    if info["age_days"] < cfg.min_wallet_age_days:
        return info, "wallet_too_young"
    return info, None


def load_swaps(rpc, wallet, sigs, cfg):
    """Загружает и разбирает tx кошелька (без неудачных), из кэша если есть."""
    sigs = [s for s in sigs if not s.get("err")]
    sigs = sigs[: cfg.max_tx_per_wallet]

    def one(s):
        sig = s["signature"]
        cached = rpc.cached_parsed(sig)
        if cached is not None:
            return sanitize(cached) or None
        try:
            tx = rpc.transaction(sig, s.get("blockTime"))
        except RuntimeError:
            return None
        swap = parse_swap(tx) if tx else None
        if swap is not None and swap["wallet"] != wallet:
            swap = None                       # кошелёк не плательщик — чужая tx, где он участвовал
        rpc.store_parsed(sig, swap or {})
        return swap

    with ThreadPoolExecutor(cfg.rpc_threads) as ex:
        swaps = [s for s in ex.map(one, sigs) if s]
    swaps.sort(key=lambda s: (s["slot"], s["sig"]))
    return swaps


def funder_of(rpc, info):
    """Кто пополнил кошелёк первой tx (ключ кластера). Дорого для старых кошельков —
    вызывать только для прошедших фильтр."""
    key = "funder:" + info["wallet"]
    cached = rpc.kv_get(key)
    if cached is not None:
        return cached or None
    sig = info.get("first_sig")
    if not sig:
        old = rpc.oldest_signature(info["wallet"], max_pages=10)
        sig = old["signature"] if old else None
        if not sig:
            rpc.kv_set(key, ""); return None
    try:
        tx = rpc.transaction(sig)
    except RuntimeError:
        return None
    f = first_funder(tx, info["wallet"])
    rpc.kv_set(key, f or "")
    return f
