"""Пороги воронки. Всё, что можно крутить, живёт здесь."""

FIXED_STAKE_USD = 100          # фикс сумма копирования одной сделки, $
BUDGET_POSITIONS = 10          # сколько позиций одновременно тянет бюджет

# --- Стадия 1: дешёвые отсечки по закрытым и открытым позициям (2-5 запросов на кошелёк)
MIN_CLOSED_POSITIONS = 50      # минимум резолвнутых/закрытых позиций
MIN_HISTORY_DAYS = 90          # первая закрытая позиция не моложе N дней
MAX_SILENCE_DAYS = 14          # последняя сделка не старше N дней
MAX_OPEN_NOW = BUDGET_POSITIONS  # открытых позиций прямо сейчас
MAX_SHARE_ENTRY_GE_90 = 0.50   # доля позиций с входом ≥ 0,90
MAX_PROFIT_SHARE_LT_10 = 0.30  # доля прибыли от входов < 0,10
MAX_PROFIT_SHARE_TOP1 = 0.25   # доля прибыли от одной лучшей позиции
MAX_SHORT_CRYPTO_SHARE = 0.50  # доля позиций на "Up or Down" 5/15-мин рынках
MIN_ROI_EQUAL = 0.0            # равновзвешенный ROI на позицию > 0

# --- Стадия 2: полная история сделок + метаданные рынков
MAX_CONCURRENT_P95 = BUDGET_POSITIONS - 2   # 95-й перцентиль одновременно открытых рынков
MIN_MEDIAN_MARKET_VOLUME = 30_000           # медианный объём рынка, $
MIN_MEDIAN_HOLD_HOURS = 1.0                 # медиана удержания позиции
MAX_BOTH_SIDES_SHARE = 0.10                 # доля рынков, где держал и YES и NO
MAX_SNIPE_SHARE = 0.10                      # входы ≥0,95 за 10 мин до конца рынка
MIN_T_STAT = 2.0                            # значимость среднего ROI
MAX_DRAWDOWN_STAKES = 10                    # просадка в ставках
MIN_PROFITABLE_HALF = True                  # обе половины истории в плюсе

# --- Стадия 3: реалистичный вход (история цен)
DELAYS_MIN = (5, 30)                        # задержки копирования, мин
MARKOUT_H = (1, 24)                         # горизонты маркаута, ч
MAX_SLIPPAGE = 0.015                        # проскальзывание нашей суммы по стакану
ASSUMED_SLIPPAGE_REL = 0.01                 # закладываем в цену отложенного входа, доля
MAX_PRICE_DRIFT = 0.03                      # не входим, если цена ушла от его входа больше, чем на N
MAX_ENTRY_PRICE = 0.90                      # не входим по цене выше
STAGE3_EPISODES = 150                       # сколько последних эпизодов прогонять через историю цен
MIN_DELAYED_ROI_KEEP = 0.60                 # ROI с задержкой 5 мин ≥ 60 % сырого
FEE_BPS_BY_CATEGORY = {"Crypto": 0, "Sports": 0}  # тейкер-комиссия, если появится

# --- Сегментация
SEG_MIN_N = 30
SEG_MIN_T = 2.0
SEG_SHRINK_K = 20
PRICE_BUCKETS = [(0, .10), (.10, .30), (.30, .50), (.50, .70), (.70, .90), (.90, 1.01)]

# Категория верхнего уровня: первый совпавший тег в этом порядке
CATEGORY_ORDER = ["Esports", "Sports", "Politics", "Crypto", "Business", "Finance", "Economy",
                  "Pop Culture", "Culture", "Science", "Tech", "Weather", "Mentions", "World"]
SPORT_TAGS = ["Soccer", "NBA", "NFL", "MLB", "NHL", "Tennis", "MMA", "UFC", "Boxing", "Golf", "F1",
              "Cricket", "Rugby", "NCAA", "College Football", "College Basketball", "WNBA", "Hockey",
              "Baseball", "Basketball", "Football", "Esports", "Counter-Strike", "League of Legends",
              "Dota 2", "Valorant", "Cycling", "Darts", "Snooker", "Table Tennis", "Volleyball"]
SHORT_CRYPTO_PATTERNS = ("Up or Down", "up-or-down", "updown")
