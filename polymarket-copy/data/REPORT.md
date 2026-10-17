# Отчёт воронки, 2026-10-17 07:07 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 55556 |
| 0. Из них не только 5-мин крипта | 53349 |
| 1. Прошли дешёвые отсечки | 4037 из 14771 |
| 2. Прошли по полной истории | 2 + сегментом 58 из 4037 |
| 3. Прошли реалистичный вход | 1 из 60 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 6740 |
| closed<50 | 6056 |
| top1_concentration | 5117 |
| entries>=0.90 | 3027 |
| history<90d | 2535 |
| short_crypto | 943 |
| open_now>10 | 800 |
| profit_from<0.10 | 553 |
| positions>5000 | 16 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3627 |
| concurrency_p95>8 | 3129 |
| drawdown | 3093 |
| unstable_halves | 2651 |
| roi_copy<=0 | 1613 |
| silent | 743 |
| low_liquidity | 613 |
| both_sides | 586 |
| top1_concentration | 292 |
| history<90d | 286 |
| closed<50 | 247 |
| hold<1h | 156 |
| entries>=0.90 | 155 |
| short_crypto | 77 |
| segment_only:t<2.0 | 55 |
| segment_only:drawdown | 48 |
| profit_from<0.10 | 43 |
| sniping | 33 |
| segment_only:unstable_halves | 29 |
| segment_only:roi_copy<=0 | 11 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 55 |
| edge_decays_with_delay | 4 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe06a77545265fccaf057cac84f5f4a6132b148c2` |  | Crypto | 0.0636 | 1.17 | 0.0687 | 0.0847 | 0.028 | 8.0 | 116.04 | 0.0017 | Crypto / Crypto Prices / price=0.70-0.90 (n=30, roi=+0.15) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x83aff046e16309ef06ae86253a5adf13ea0b4084` | Hollow0329 | 0.1794 | Esports / price=0.50-0.70 (n=31, roi=+0.24) | Esports / Esports / price=0.50-0.70 (n=31, roi=+0.24) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.057 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0599 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.0838 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0xe06a77545265fccaf057cac84f5f4a6132b148c2` |  | 0.0636 | Crypto / Crypto Prices / price=0.70-0.90 (n=30, roi=+0.15) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xb0e3fcbe0d7f17168fdce93f89c0168d3fa329eb` | gagarin59 | 0.0992 | Sports / price=0.50-0.70 (n=48, roi=+0.21) | segment_only:t<2.0 |
| `0x93159a717f382318a7dbed96cfc4d61ab6a3afc1` |  | 0.0575 | Sports / Soccer / Club Friendlies (n=32, roi=+0.15) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1589 | Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / type=child_moneyline (n=604, roi=+0.19) | Esports (n=702, roi=+0.16) | Esports / Esports (n=702, roi=+0.16) | Esports / Esports / Dota 2 (n=702, roi=+0.16) | segment_only:drawdown |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0552 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0195 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0722 | Sports / Soccer / type=moneyline (n=52, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0577 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=73, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0844 | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0xd4f4ee5f2e93d503e5a1a0cbb5495586fd05bb68` | Auagmg | 0.0238 | Sports / price=0.70-0.90 (n=53, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0166 | Sports / Soccer / price=0.50-0.70 (n=55, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x20255f1ed1e9db14d2c663b588cbcc41306113c0` | 182837282 | -0.0163 | Sports / Tennis / price=0.70-0.90 (n=60, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1940efc707c1c2aaccd0eefabb63884ff190123e` | 0x1940EfC707c1c2AacCd0EEFaBb63884FF190123E-1768266454473 | -0.028 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | Sports / Basketball / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0144 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5d68ae7869c19cb27deb63ae8d911d59d6a7ff40` | 0x5D68ae7869C19Cb27DEB63Ae8d911D59D6a7Ff40-1782738338244 | 0.0223 | Sports / Other sport / type=totals (n=77, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0087 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xce041dc32d338cf0a44d7a1b860e793fbdd0dbf6` |  | -0.0074 | Sports / price=0.70-0.90 (n=43, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.013 | Sports / Other sport / price=0.70-0.90 (n=53, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0037 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=142, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xa236024a7acfc8f32f850ba72b68664ed1564cbb` | ganzarolli | 0.0014 | Sports / Soccer / price=0.70-0.90 (n=62, roi=+0.11) | Sports / price=0.70-0.90 (n=70, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x332fb63ddf2478a64a9b090db07bb2a1b3ee80a4` | Fulc | 0.0502 | Sports / price=0.30-0.50 (n=86, roi=+0.27) | Crypto (n=65, roi=+0.23) | Crypto / price=0.50-0.70 (n=41, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0292 | Sports / American Football (n=164, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0116 | Sports / Soccer / pre (n=182, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=161, roi=+0.09) | Sports / price=0.70-0.90 (n=190, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0094 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8342720db0862f72861ada9c74778b3449d06dc8` | gys-bot | 0.0484 | Esports / price=0.50-0.70 (n=387, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=387, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0389 | Sports / Basketball / price=0.50-0.70 (n=33, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0143 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0309 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x45361ff76a9308998703e0acb658691eca9af41b` | russeN1 | 0.0577 | Esports / price=0.30-0.50 (n=82, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=82, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0373 | Esports / price=0.50-0.70 (n=46, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=46, roi=+0.18) | segment_only:t<2.0 |
| `0xbcf51140fd48e69c6e6d4bd09d38a629059856a1` | bqy0301 | 0.199 | Sports / price=0.30-0.50 (n=36, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c68066fe7466ad3048a4adff9ad18cfecdab7b` | lucianow34 | 0.0262 | Esports / price=0.50-0.70 (n=448, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=448, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1400 | 0.2414 | 0.043 | 6.13 | 0.56 | 8.0 | 2.52 | 55523 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x31121402…` | Sports / price=0.00-0.10 | 92 | 14.2174 | 11.7208 | 3.78 | 0.152 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8091 | 3.23 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 815 | 2.9574 | 2.9081 | 2.21 | 0.222 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 816 | 2.9532 | 2.904 | 2.21 | 0.222 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.7972 | 3.06 | 0.279 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8326 | 2.82 | 0.131 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8326 | 2.82 | 0.131 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3861 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 62 | 8.6662 | 6.6489 | 3.13 | 0.242 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 59 | 8.9234 | 6.7914 | 2.71 | 0.441 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9776 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2934 | 0.9157 | 0.9155 | 2.46 | 0.547 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2934 | 0.9157 | 0.9155 | 2.46 | 0.547 |
| `0x1941ca5d…` | Sports | 2936 | 0.9151 | 0.915 | 2.46 | 0.547 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8614 | 2.71 | 0.206 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6121 | 2.86 | 0.07 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 157 | 4.0258 | 3.6252 | 2.69 | 0.115 |
| `0xef185339…` | Sports | 3845 | 0.7294 | 0.7294 | 22.67 | 0.691 |
| `0x13997bdb…` | Sports | 4140 | 0.6769 | 0.6769 | 22.47 | 0.683 |
| `0x41558102…` | Sports / price=0.00-0.10 | 41 | 9.9583 | 6.7977 | 2.42 | 0.293 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5416 | 2.39 | 0.133 |
| `0xd60c6fa3…` | Sports | 3577 | 0.6958 | 0.6958 | 21.0 | 0.686 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 335 | 2.2612 | 2.1785 | 4.32 | 0.406 |
| `0xd970693a…` | Sports | 2442 | 0.7929 | 0.7929 | 10.32 | 0.664 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1048 | 1.2092 | 1.2002 | 17.19 | 0.598 |
| `0x4afbb658…` | Sports | 166 | 3.1455 | 2.9774 | 2.37 | 0.416 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 92 | 4.7206 | 3.9408 | 2.52 | 0.543 |
| `0x70feb53b…` | Sports | 329 | 2.0815 | 2.0663 | 3.33 | 0.726 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 904 | 1.2563 | 1.2441 | 16.37 | 0.595 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 380 | 1.9664 | 1.889 | 3.25 | 0.282 |
| `0x13997bdb…` | Sports / Soccer | 2890 | 0.6839 | 0.6838 | 18.46 | 0.688 |
| `0x13997bdb…` | Sports / Soccer / live | 2848 | 0.687 | 0.6869 | 18.32 | 0.687 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 384 | 1.9355 | 1.8604 | 3.23 | 0.279 |
| `0xef185339…` | Sports / Soccer | 2589 | 0.7016 | 0.7019 | 18.79 | 0.689 |
| `0xef185339…` | Sports / Soccer / live | 2555 | 0.7019 | 0.7021 | 18.59 | 0.688 |
| `0x13997bdb…` | Sports / price=0.10-0.30 | 1147 | 1.0418 | 1.0356 | 16.24 | 0.564 |
| `0xd60c6fa3…` | Sports / Soccer | 2420 | 0.6951 | 0.6951 | 16.6 | 0.685 |
| `0xd60c6fa3…` | Sports / Soccer / live | 2377 | 0.6965 | 0.6965 | 16.39 | 0.683 |
| `0x1941ca5d…` | Sports / Other sport / live | 2238 | 0.7019 | 0.7036 | 3.58 | 0.59 |
| `0x33ae5c5d…` | Sports / price=0.00-0.10 | 215 | 2.3628 | 2.1838 | 2.8 | 0.405 |
| `0xef185339…` | Sports / Soccer / price=0.10-0.30 | 680 | 1.2297 | 1.2153 | 14.04 | 0.607 |
| `0x98689f59…` | Sports / Tennis / ITF | 221 | 2.2458 | 2.0993 | 2.42 | 0.439 |
| `0xdba10a9b…` | Sports / price=0.00-0.10 | 168 | 2.5349 | 2.3663 | 2.34 | 0.262 |
| `0xdba10a9b…` | Sports / Other sport / price=0.00-0.10 | 168 | 2.5349 | 2.3663 | 2.34 | 0.262 |
| `0x2e7c5460…` | Sports / Tennis | 352 | 1.6949 | 1.625 | 3.37 | 0.472 |
| `0xd60c6fa3…` | Sports / Soccer / price=0.10-0.30 | 599 | 1.2523 | 1.2343 | 13.44 | 0.604 |
| `0xd970693a…` | Sports / Soccer | 1630 | 0.738 | 0.7387 | 8.9 | 0.666 |
| `0xd970693a…` | Sports / Soccer / live | 1608 | 0.7405 | 0.7411 | 8.82 | 0.667 |
| `0xdf804b17…` | Sports / price=0.00-0.10 | 89 | 3.7748 | 3.1243 | 2.12 | 0.135 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8057 | 2.81 | 0.664 |
| `0x122b758a…` | Sports / price=0.00-0.10 | 368 | 1.589 | 1.5264 | 2.79 | 0.16 |
| `0xc9ccb64f…` | Sports / Soccer / price=0.00-0.10 | 58 | 5.0464 | 3.843 | 2.07 | 0.534 |
| `0x13997bdb…` | Sports / Soccer / price=0.10-0.30 | 790 | 1.0453 | 1.0362 | 13.52 | 0.565 |
| `0xdf804b17…` | Sports / Soccer / price=0.00-0.10 | 84 | 3.8606 | 3.1623 | 2.05 | 0.131 |
| `0x482acc0c…` | Sports / Soccer / price=0.00-0.10 | 249 | 1.9095 | 1.7927 | 2.36 | 0.112 |
| `0xd3989ba1…` | Politics / Biden | 63 | 4.583 | 3.5611 | 2.02 | 0.683 |
| `0xd3989ba1…` | Politics / Biden / ? | 63 | 4.583 | 3.5611 | 2.02 | 0.683 |
| `0xef185339…` | Sports / price=0.00-0.10 | 232 | 1.9528 | 1.8556 | 5.26 | 0.487 |
