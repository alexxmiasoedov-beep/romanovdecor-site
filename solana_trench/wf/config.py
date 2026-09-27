"""Все параметры и пороги фильтра в одном месте."""
import os
from dataclasses import dataclass, field, asdict


@dataclass
class Config:
    # --- источники данных ---
    rpc_url: str = os.environ.get("SOLANA_RPC_URL", "https://solana-rpc.publicnode.com")
    rpc_rps: float = float(os.environ.get("SOLANA_RPC_RPS", "15"))   # запросов/сек
    rpc_threads: int = int(os.environ.get("SOLANA_RPC_THREADS", "8"))
    gecko_delay_sec: float = 2.1          # лимит GeckoTerminal ~30 запросов/мин
    cache_dir: str = "cache"
    out_dir: str = "out"

    # --- discover: какие пулы считаем "после миграции" ---
    post_migration_dexes: tuple = ("pumpswap", "raydium", "raydium-cpmm", "meteora-damm-v2")
    pool_age_hours: float = 24.0          # пул создан не раньше чем N часов назад
    new_pool_pages: int = 5               # страниц /new_pools (20 пулов на страницу)
    active_pool_pages: int = 3            # страниц /dexes/pumpswap/pools (самые активные)
    max_pools: int = 40
    min_pool_liquidity_usd: float = 5_000  # пул с меньшей ликвидностью — мусор

    # --- collect / prefilter (дёшево, до загрузки истории) ---
    history_days: int = 30                # окно истории кошелька
    min_wallet_age_days: int = 15         # требование владельца
    min_tx_in_window: int = 20
    max_tx_per_day: float = 300           # больше — бот
    max_failed_tx_share: float = 0.35     # доля неудачных tx (спам-боты)
    max_wallets: int = 60                 # сколько кошельков грузить полностью
    max_tx_per_wallet: int = 600          # кап на загрузку (для публичного RPC)

    # --- симуляция копии ---
    copy_size_sol: float = 0.5            # фиксированная сумма входа
    fee_bps: float = 125                  # комиссия пула+приоритет, на одну сторону
    latency_slippage_bps: float = 100     # штраф за то, что мы в следующем слоте
    dead_bag_days: float = 3.0            # незакрытая позиция старше N дней = мешок
    dead_bag_value_haircut: float = 0.5   # текущую цену мешка режем вдвое

    # --- фильтры по метрикам ---
    min_closed_positions: int = 15
    min_median_hold_sec: float = 3.0
    max_fast_exit_share: float = 0.20     # доля позиций короче min_median_hold_sec
    min_post_migration_share: float = 0.70
    max_sniper_share: float = 0.10        # покупки на кривой с резервом < sniper_sol
    sniper_sol: float = 2.0
    max_median_entry_impact: float = 0.02  # сумма входа / резерв SOL пула
    max_big_entry_share: float = 0.20      # доля входов с импактом > big_entry_impact
    big_entry_impact: float = 0.03
    max_median_exit_impact: float = 0.03
    max_avg_buys_per_position: float = 2.0  # усреднение (владелец против)
    min_copy_median_ret: float = 0.03
    min_copy_win_rate: float = 0.40
    min_copy_profit_factor: float = 1.3
    min_copy_pnl_sol: float = 0.0
    max_top_token_profit_share: float = 0.40
    min_positive_weeks_share: float = 0.50
    require_latency_robust: bool = True    # PnL > 0 при удвоенном штрафе задержки

    def to_dict(self):
        return asdict(self)


PUMP_FUN = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
PUMPSWAP = "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"
LAUNCHLAB = "LanMV9sAd7wArD4vJFi2qDdfnVhFxYSUg6eADduJ3uj"
METEORA_DBC = "dbcij3LWUppWqq96dh6gJWwBifmcGfLSB5D4DuSMaqN"
RAYDIUM_AMM = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
RAYDIUM_CPMM = "CPMMoo8L3F4NbTegBCKVNunggL7H1ZpdTHKxQB5qKP1C"
RAYDIUM_CLMM = "CAMMCzo5YL8w4VFF8KVHrK22GGUsp5VTaW7grrKgrWqK"
METEORA_DAMM2 = "cpamdpZCGKUy5JxQXB4dcpGPiikHawvSWAd6mEn1sGG"
METEORA_DLMM = "LBUZKhRxPF3XUpBCjp4YzTKgLccjZhTSDM9YuVaPwxo"
ORCA = "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc"

# бонд-кривые: сделка ДО миграции
PRE_MIGRATION_PROGRAMS = {PUMP_FUN: "pumpfun", LAUNCHLAB: "launchlab", METEORA_DBC: "meteora-dbc"}
# AMM: сделка ПОСЛЕ миграции
POST_MIGRATION_PROGRAMS = {
    PUMPSWAP: "pumpswap", RAYDIUM_AMM: "raydium", RAYDIUM_CPMM: "raydium-cpmm",
    RAYDIUM_CLMM: "raydium-clmm", METEORA_DAMM2: "meteora-damm2",
    METEORA_DLMM: "meteora-dlmm", ORCA: "orca",
}

WSOL = "So11111111111111111111111111111111111111112"
STABLES = {
    "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
    "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNUS",  # USDT
}
LAMPORTS = 1_000_000_000

# pump.fun: виртуальные резервы = реальные + константы кривой
PUMP_VIRTUAL_SOL = 30.0
PUMP_VIRTUAL_TOKENS = 1_073_000_000 - 793_100_000
PUMP_SUPPLY = 1_000_000_000
