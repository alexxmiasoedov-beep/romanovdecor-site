"""Разбор jsonParsed-транзакции в запись свопа по разницам балансов.

Не зависит от конкретной программы: смотрим, сколько SOL и токена
изменилось у кошелька и у пула. Пул = владелец токен-хранилища с
самым большим встречным изменением. Резервы пула после сделки — из
postBalances/postTokenBalances (это даёт честную цену нашего входа
сразу после сделки лидера).
"""
from .config import (CONCENTRATED_VENUES, LAMPORTS, PRE_MIGRATION_PROGRAMS, POST_MIGRATION_PROGRAMS,
                     PUMP_FUN, PUMP_VIRTUAL_SOL, PUMP_VIRTUAL_TOKENS, STABLES, WSOL)


def _amount(b):
    ui = b["uiTokenAmount"]
    if ui.get("amount") is None:
        return 0.0
    return int(ui["amount"]) / (10 ** ui["decimals"])


def trusted_reserves(venue, sol_amount, token_amount, sol_res, tok_res):
    """Резервам верим только там, где пул — константное произведение, и только если
    цена пула сходится с ценой исполнения (иначе выбрали не то хранилище)."""
    if venue in CONCENTRATED_VENUES or not sol_res or not tok_res or sol_res <= 0 or tok_res <= 0:
        return None, None
    pool_px, fill_px = sol_res / tok_res, sol_amount / token_amount
    if not (0.5 < pool_px / fill_px < 2.0):
        return None, None
    return sol_res, tok_res


def sanitize(swap):
    """Применить те же проверки к записи из кэша (разобранной старой версией)."""
    if swap:
        swap["sol_res"], swap["tok_res"] = trusted_reserves(swap["venue"], swap["sol"], swap["tokens"], swap.get("sol_res"), swap.get("tok_res"))
    return swap


def parse_swap(tx):
    """-> dict свопа или None (не своп / не разобрали)."""
    if tx is None or tx.get("meta") is None or tx["meta"].get("err") is not None:
        return None
    meta, msg = tx["meta"], tx["transaction"]["message"]
    keys = [k["pubkey"] for k in msg["accountKeys"]]
    wallet = keys[0]

    programs = {i["programId"] for i in msg["instructions"]}
    for inner in meta.get("innerInstructions") or []:
        programs |= {i["programId"] for i in inner["instructions"]}
    venue, pre_migration = None, None
    for pid, name in PRE_MIGRATION_PROGRAMS.items():
        if pid in programs:
            venue, pre_migration = name, True
    if venue is None:
        for pid, name in POST_MIGRATION_PROGRAMS.items():
            if pid in programs:
                venue, pre_migration = name, False
    if venue is None:
        return None

    # изменения токенов: (owner, mint, accountIndex) -> delta
    pre = {(b["accountIndex"]): b for b in meta.get("preTokenBalances") or []}
    post = {(b["accountIndex"]): b for b in meta.get("postTokenBalances") or []}
    deltas = []
    for idx in set(pre) | set(post):
        b = post.get(idx) or pre.get(idx)
        d = _amount(post[idx]) if idx in post else 0.0
        d -= _amount(pre[idx]) if idx in pre else 0.0
        deltas.append((b.get("owner"), b["mint"], idx, d, _amount(post[idx]) if idx in post else 0.0))

    wallet_tokens = {}
    for owner, mint, idx, d, _ in deltas:
        if owner == wallet and mint != WSOL and mint not in STABLES and abs(d) > 0:
            wallet_tokens[mint] = wallet_tokens.get(mint, 0.0) + d
    if len(wallet_tokens) != 1:
        return None            # не своп SOL<->токен (или токен-токен) — пропускаем
    mint, token_delta = next(iter(wallet_tokens.items()))
    side = "buy" if token_delta > 0 else "sell"

    lamport_delta = {i: (meta["postBalances"][i] - meta["preBalances"][i]) / LAMPORTS for i in range(len(keys))}
    wallet_sol = lamport_delta.get(0, 0.0) + meta["fee"] / LAMPORTS
    for owner, m, idx, d, _ in deltas:
        if owner == wallet and m == WSOL:
            wallet_sol += d

    # пул: хранилище токена с самым большим встречным изменением
    vault = None
    for owner, m, idx, d, post_amt in deltas:
        if m == mint and owner != wallet and (d < 0) == (side == "buy"):
            if vault is None or abs(d) > abs(vault[3]):
                vault = (owner, m, idx, d, post_amt)
    sol_res = tok_res = pool_sol_delta = None
    if vault is not None:
        pool_owner, tok_res = vault[0], vault[4]
        # SOL-сторона пула: нативные лампорты владельца (бонд-кривая) или его WSOL-счёт
        cands = []
        if pool_owner in keys:
            i = keys.index(pool_owner)
            cands.append((lamport_delta[i], meta["postBalances"][i] / LAMPORTS))
        for owner, m, idx, d, post_amt in deltas:
            if m == WSOL and owner == pool_owner:
                cands.append((d, post_amt))
        cands = [c for c in cands if (c[0] > 0) == (side == "buy") and abs(c[0]) > 0]
        if cands:
            pool_sol_delta, sol_res = max(cands, key=lambda c: abs(c[0]))
        if venue == "pumpfun" and sol_res is not None:
            sol_res += PUMP_VIRTUAL_SOL
            tok_res += PUMP_VIRTUAL_TOKENS

    sol_amount = abs(pool_sol_delta) if pool_sol_delta else abs(wallet_sol)
    token_amount = abs(token_delta)
    if sol_amount <= 0 or token_amount <= 0:
        return None
    sol_res, tok_res = trusted_reserves(venue, sol_amount, token_amount, sol_res, tok_res)
    return {
        "sig": tx["transaction"]["signatures"][0],
        "slot": tx["slot"],
        "time": tx.get("blockTime"),
        "wallet": wallet,
        "mint": mint,
        "side": side,
        "sol": sol_amount,
        "tokens": token_amount,
        "venue": venue,
        "pre_migration": pre_migration,
        "sol_res": sol_res,       # резерв SOL пула ПОСЛЕ сделки (для pump.fun — виртуальный)
        "tok_res": tok_res,
        "real_sol_res": (sol_res - PUMP_VIRTUAL_SOL) if (venue == "pumpfun" and sol_res is not None) else sol_res,
    }


def first_funder(tx, wallet):
    """Кто прислал SOL в первой транзакции кошелька (ключ кластера)."""
    if tx is None or tx.get("meta") is None:
        return None
    keys = [k["pubkey"] for k in tx["transaction"]["message"]["accountKeys"]]
    meta = tx["meta"]
    best = None
    for i, k in enumerate(keys):
        d = meta["postBalances"][i] - meta["preBalances"][i]
        if k != wallet and d < 0 and (best is None or d < best[1]):
            best = (k, d)
    return best[0] if best else None
