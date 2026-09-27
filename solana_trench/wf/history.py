"""История кошелька: дешёвый префильтр по подписям, потом полная загрузка свопов."""
import time
from concurrent.futures import ThreadPoolExecutor

from .parse_tx import parse_swap, first_funder


def prefilter_wallet(rpc, wallet, cfg, now=None):
    """Возраст, число tx в окне, доля неудачных. Одна-несколько страниц подписей.
    -> (info, reason) — reason=None если прошёл."""
    now = now or time.time()
    min_time = now - cfg.history_days * 86400
    sigs, exhausted = rpc.signatures_until(wallet, min_time, max_pages=max(2, cfg.max_tx_per_day * cfg.history_days // 1000 + 1))
    info = {"wallet": wallet, "tx_in_window": len(sigs), "sigs": sigs}
    if not sigs:
        return info, "no_tx"
    failed = sum(1 for s in sigs if s.get("err"))
    info["failed_share"] = failed / len(sigs)
    if len(sigs) < cfg.min_tx_in_window:
        return info, "too_few_tx"
    if len(sigs) / cfg.history_days > cfg.max_tx_per_day:
        return info, "too_many_tx_bot"
    if info["failed_share"] > cfg.max_failed_tx_share:
        return info, "failed_tx_spam"

    # возраст: если история не исчерпана в окне — кошелёк старше окна (>= history_days >= 15)
    if exhausted:
        oldest = sigs[-1].get("blockTime") or now
        info["first_tx_time"] = oldest
        info["first_sig"] = sigs[-1]["signature"]
    else:
        old = rpc.oldest_signature(wallet, max_pages=5)
        if old is None:
            info["first_tx_time"] = None      # длинная история, точно старше окна
        else:
            info["first_tx_time"] = old.get("blockTime")
            info["first_sig"] = old["signature"]
    age_days = (now - info["first_tx_time"]) / 86400 if info.get("first_tx_time") else cfg.history_days + 1
    info["age_days"] = round(age_days, 1)
    if age_days < cfg.min_wallet_age_days:
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
            return cached or None
        try:
            tx = rpc.transaction(sig)
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
    sig = info.get("first_sig")
    if not sig:
        return None
    key = "funder:" + info["wallet"]
    cached = rpc.kv_get(key)
    if cached is not None:
        return cached or None
    try:
        tx = rpc.transaction(sig)
    except RuntimeError:
        return None
    f = first_funder(tx, info["wallet"])
    rpc.kv_set(key, f or "")
    return f
