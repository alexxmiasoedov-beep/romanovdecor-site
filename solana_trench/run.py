#!/usr/bin/env python3
"""Запуск пайплайна. Примеры:

  python3 run.py                       # сегодняшние пулы, дефолтные пороги
  python3 run.py --max-wallets 30 --max-tx 300
  python3 run.py --wallets w1,w2,w3    # проверить конкретные кошельки
  SOLANA_RPC_URL=https://mainnet.helius-rpc.com/?api-key=... python3 run.py --rps 50 --threads 16
"""
import argparse
import csv
import json
import os
import random
import sys
import time

from wf.config import Config
from wf.gecko import Gecko, sol_price_history, sol_price_now, token_prices_native
from wf.gmgn import Gmgn, read_wallets_file
from wf.history import prefilter_wallet, load_swaps, funder_of
from wf.metrics import wallet_metrics, apply_filters
from wf.rpc import Rpc


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


def discover(gecko, cfg, now):
    pools, seen = [], set()
    min_created = now - cfg.pool_age_hours * 3600
    for page in range(1, cfg.new_pool_pages + 1):
        for p in gecko.new_pools(page):
            if p["dex"] in cfg.post_migration_dexes and p["pool"] not in seen and p["created"] >= min_created:
                seen.add(p["pool"]); pools.append(p)
    for dex in ("pumpswap",):
        for page in range(1, cfg.active_pool_pages + 1):
            for p in gecko.dex_pools(dex, page):
                if p["pool"] not in seen and p["created"] >= min_created:
                    seen.add(p["pool"]); pools.append(p)
    pools = [p for p in pools if p["liquidity_usd"] >= cfg.min_pool_liquidity_usd]
    pools.sort(key=lambda p: -p["volume_h24"])
    return pools[: cfg.max_pools]


def collect(gecko, pools):
    wallets = {}
    for p in pools:
        try:
            trades = gecko.pool_trades(p["pool"])
        except Exception as e:
            log("trades failed", p["name"], e); continue
        for t in trades:
            w = wallets.setdefault(t["wallet"], {"pools": set(), "buys": 0, "sells": 0, "usd": 0.0})
            w["pools"].add(p["pool"]); w["usd"] += t["usd"]
            w["buys" if t["kind"] == "buy" else "sells"] += 1
        log(f"pool {p['name']:<28} {p['dex']:<10} trades={len(trades)} wallets_total={len(wallets)}")
    return wallets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallets", help="список кошельков через запятую (пропустить discover)")
    ap.add_argument("--wallets-file", help="файл с кошельками (например, экспорт из GMGN), по одному в строке или CSV")
    ap.add_argument("--gmgn", action="store_true", help="добавить кандидатов из GMGN (нужны GMGN_COOKIE/GMGN_UA): рейтинг кошельков + топ трейдеров по найденным токенам")
    ap.add_argument("--max-wallets", type=int)
    ap.add_argument("--max-tx", type=int)
    ap.add_argument("--max-pools", type=int)
    ap.add_argument("--copy-size", type=float)
    ap.add_argument("--rps", type=float)
    ap.add_argument("--threads", type=int)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    cfg = Config()
    if a.max_wallets: cfg.max_wallets = a.max_wallets
    if a.max_tx: cfg.max_tx_per_wallet = a.max_tx
    if a.max_pools: cfg.max_pools = a.max_pools
    if a.copy_size: cfg.copy_size_sol = a.copy_size
    if a.rps: cfg.rpc_rps = a.rps
    if a.threads: cfg.rpc_threads = a.threads
    if a.out: cfg.out_dir = a.out
    os.makedirs(cfg.out_dir, exist_ok=True)
    now = time.time()
    rpc = Rpc(cfg.rpc_url, cfg.rpc_rps, cfg.cache_dir)
    gecko = Gecko(cfg.gecko_delay_sec)

    # 1-2. discover + collect
    def blank():
        return {"pools": set(), "buys": 0, "sells": 0, "usd": 0.0, "src": set()}

    candidates, pools = {}, []
    manual = [w.strip() for w in (a.wallets or "").split(",") if w.strip()]
    if a.wallets_file:
        manual += read_wallets_file(a.wallets_file)
    for w in manual:
        candidates.setdefault(w, blank())["src"].add("manual")
    if not manual or a.gmgn:
        pools = discover(gecko, cfg, now)
        log(f"pools: {len(pools)}")
        json.dump(pools, open(os.path.join(cfg.out_dir, "pools.json"), "w"), indent=1, ensure_ascii=False)
        for w, v in collect(gecko, pools).items():
            c = candidates.setdefault(w, blank()); c.update({k: v[k] for k in ("buys", "sells", "usd")})
            c["pools"] |= v["pools"]; c["src"].add("onchain")
    if a.gmgn:
        gm = Gmgn()
        if not gm.available:
            log("GMGN: нет GMGN_COOKIE — пропускаю (см. wf/gmgn.py)")
        n0 = len(candidates)
        for tag in (None, "smart_degen", "pump_smart"):
            for r in gm.top_wallets("7d", tag=tag):
                c = candidates.setdefault(r["wallet"], blank()); c["src"].add("gmgn_rank"); c["gmgn"] = r["gmgn"]
        for p in pools:
            for r in gm.top_traders(p["mint"]):
                c = candidates.setdefault(r["wallet"], blank()); c["src"].add("gmgn_top_traders"); c["pools"].add(p["pool"])
        log(f"GMGN: +{len(candidates) - n0} кандидатов")
    log(f"candidate wallets: {len(candidates)}")

    # 3. prefilter (дёшево)
    order = sorted(candidates, key=lambda w: (-len(candidates[w]["pools"]), -candidates[w]["usd"]))
    random.Random(1).shuffle(order)  # чтобы не брать только самых громких
    order.sort(key=lambda w: -len(candidates[w]["pools"]))
    prefiltered, dropped = [], {}
    from concurrent.futures import ThreadPoolExecutor

    def pre(w):
        try:
            return prefilter_wallet(rpc, w, cfg, now)
        except RuntimeError as e:
            log("prefilter rpc error", w, e)
            return {"wallet": w}, "rpc_error"

    with ThreadPoolExecutor(cfg.rpc_threads) as ex:
        for i, (info, reason) in enumerate(ex.map(pre, order)):
            if reason:
                dropped[reason] = dropped.get(reason, 0) + 1
            else:
                prefiltered.append(info)
            if (i + 1) % 50 == 0:
                log(f"prefilter {i+1}/{len(order)} passed={len(prefiltered)} dropped={dropped}")
            if len(prefiltered) >= cfg.max_wallets:
                break
    log(f"prefilter done: passed={len(prefiltered)} dropped={dropped}")

    # 4-6. история, позиции, симуляция
    sol_hist = sol_price_history(cfg.history_days + 1)
    sol_now = sol_price_now() or (list(sol_hist.values())[-1] if sol_hist else None)
    results = []
    for k, info in enumerate(prefiltered):
        w = info["wallet"]
        t0 = time.time()
        swaps = load_swaps(rpc, w, info["sigs"], cfg)
        mints = list({s["mint"] for s in swaps})
        token_prices = token_prices_native(mints) if mints else {}
        m, rows = wallet_metrics(swaps, cfg, sol_hist, sol_now, token_prices, now)
        reasons = apply_filters(m, cfg)
        funder = funder_of(rpc, info)
        rec = {"wallet": w, "age_days": info.get("age_days"), "tx_in_window": info["tx_in_window"],
               "failed_share": round(info.get("failed_share", 0), 3), "funder": funder,
               "seen_in_pools": len(candidates[w]["pools"]), "source": "+".join(sorted(candidates[w]["src"])), **m,
               "pass": not reasons, "fail_reasons": ";".join(reasons)}
        results.append(rec)
        json.dump(rows, open(os.path.join(cfg.out_dir, f"positions_{w}.json"), "w"), indent=1)
        log(f"[{k+1}/{len(prefiltered)}] {w[:8]} swaps={len(swaps)} closed={m['n_closed']} "
            f"copy_pnl={m['copy_pnl_sol'] and round(m['copy_pnl_sol'],3)} {'PASS' if not reasons else reasons} ({time.time()-t0:.0f}s, rpc calls {rpc.calls})")

    # кластеры по источнику пополнения: из одного кластера оставляем лучший
    by_funder = {}
    for r in results:
        if r["funder"]:
            by_funder.setdefault(r["funder"], []).append(r)
    for f, rs in by_funder.items():
        if len(rs) > 1:
            best = max(rs, key=lambda r: r["copy_pnl_sol"] or -1e9)
            for r in rs:
                r["cluster_size"] = len(rs)
                if r is not best and r["pass"]:
                    r["pass"] = False; r["fail_reasons"] = "same_funder_cluster"

    # 7. отчёт
    results.sort(key=lambda r: (not r["pass"], -(r["copy_pnl_sol"] or -1e9)))
    keys = list(results[0].keys()) if results else ["wallet"]
    for r in results:
        for k in keys: r.setdefault(k, None)
    with open(os.path.join(cfg.out_dir, "wallets.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in results:
            wr.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
    json.dump({"config": cfg.to_dict(), "generated": now, "prefilter_dropped": dropped,
               "passed": [r for r in results if r["pass"]]},
              open(os.path.join(cfg.out_dir, "passed.json"), "w"), indent=1)
    passed = [r for r in results if r["pass"]]
    print(f"\ncandidates={len(candidates)} prefiltered={len(prefiltered)} analysed={len(results)} PASSED={len(passed)}")
    print("prefilter drops:", dropped)
    fails = {}
    for r in results:
        for x in r["fail_reasons"].split(";"):
            if x: fails[x] = fails.get(x, 0) + 1
    print("filter drops:", dict(sorted(fails.items(), key=lambda kv: -kv[1])))
    for r in passed:
        print(f"PASS {r['wallet']} closed={r['n_closed']} copy_pnl={r['copy_pnl_sol']:.3f} SOL "
              f"med_ret={r['copy_median_ret']:.2%} win={r['copy_win_rate']:.0%} pf={r['copy_profit_factor']:.2f} "
              f"hold_med={r['median_hold_sec']:.0f}s post_mig={r['post_migration_share']:.0%}")
    print(f"\nfiles: {cfg.out_dir}/wallets.csv, {cfg.out_dir}/passed.json, {cfg.out_dir}/positions_<wallet>.json")


if __name__ == "__main__":
    main()
