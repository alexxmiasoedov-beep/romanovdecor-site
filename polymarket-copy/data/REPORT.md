# Отчёт воронки, 2026-10-19 08:04 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 55909 |
| 0. Из них не только 5-мин крипта | 53853 |
| 1. Прошли дешёвые отсечки | 4274 из 20594 |
| 2. Прошли по полной истории | 4 + сегментом 53 из 4274 |
| 3. Прошли реалистичный вход | 4 из 57 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 9775 |
| closed<50 | 5779 |
| top1_concentration | 5190 |
| entries>=0.90 | 4117 |
| history<90d | 3944 |
| open_now>10 | 3003 |
| short_crypto | 1416 |
| profit_from<0.10 | 1115 |
| positions>5000 | 145 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3857 |
| concurrency_p95>8 | 3372 |
| drawdown | 3276 |
| unstable_halves | 2789 |
| roi_copy<=0 | 1675 |
| silent | 710 |
| low_liquidity | 660 |
| both_sides | 592 |
| history<90d | 314 |
| top1_concentration | 294 |
| closed<50 | 231 |
| hold<1h | 179 |
| entries>=0.90 | 148 |
| short_crypto | 96 |
| profit_from<0.10 | 51 |
| segment_only:t<2.0 | 50 |
| sniping | 46 |
| segment_only:drawdown | 44 |
| segment_only:unstable_halves | 25 |
| segment_only:roi_copy<=0 | 9 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 51 |
| edge_decays_with_delay | 2 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x30f8c0ca1f263f09da7fc802f442d1edc0cc5edb` | forzodynamo | Sports | 0.0709 | 1.33 | 0.0727 | 0.0846 | 0.048 | 6.0 | 5.41 | н/д | Sports / Soccer / La Liga 2025 (n=30, roi=+0.21) |
| `0x616ed6c5a870f31699aededd72bcf4c2d960a666` | 0x616Ed6c5a870f31699aedEdd72BcF4C2D960A666-1773862150040 | Sports | 0.0634 | 0.83 | 0.0441 | 0.0854 | 0.0279 | 3.0 | 2.47 | 0.0 | Sports / Soccer / pre (n=30, roi=+0.18) |
| `0x51c7d30511ed096b39a9392bad97e0dc76c298aa` | Chopperyyy | Esports | 0.0228 | 0.76 | 0.0196 | 0.0082 | 0.0387 | 4.0 | 4.94 | н/д | Esports / Esports / Counter Strike (n=306, roi=+0.09) |
| `0x5695dbbb252ff9e1478f862ec752f0c7ba5f3cab` | Evlyon | Sports | 0.1647 | 1.94 | 0.0704 | 0.0707 | 0.2963 | 6.0 | 7.49 | н/д | Sports / price=0.30-0.50 (n=153, roi=+0.28) | Sports / Soccer / price=0.30-0.50 (n=117, roi=+0.30) | Sports / Soccer / Serie A 2025 (n=31, roi=+0.47) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.0431 | Sports / price=0.50-0.70 (n=100, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x30f8c0ca1f263f09da7fc802f442d1edc0cc5edb` | forzodynamo | 0.0709 | Sports / Soccer / La Liga 2025 (n=30, roi=+0.21) | segment_only:t<2.0 |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0458 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x616ed6c5a870f31699aededd72bcf4c2d960a666` | 0x616Ed6c5a870f31699aedEdd72BcF4C2D960A666-1773862150040 | 0.0634 | Sports / Soccer / pre (n=30, roi=+0.18) | segment_only:t<2.0 |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0568 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1554 | Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / type=child_moneyline (n=614, roi=+0.18) | Esports (n=712, roi=+0.16) | Esports / Esports (n=712, roi=+0.16) | Esports / Esports / Dota 2 (n=712, roi=+0.16) | segment_only:drawdown |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.023 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca14f80a6daec5144052ee31403c01111cd85915` | 0xcA14F80a6dAeC5144052eE31403C01111CD85915-1772987358266 | 0.0663 | Sports / price=0.30-0.50 (n=31, roi=+0.37) | Sports / Tennis / live (n=35, roi=+0.28) | Sports / Tennis (n=40, roi=+0.20) | Sports / Tennis / type=moneyline (n=40, roi=+0.20) | segment_only:t<2.0 |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.061 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=81, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0xe832bb748b0ce571280268b790c56c31fe137abb` | lucapuca | 0.0581 | Sports / American Football / price=0.30-0.50 (n=35, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0111 | Sports / Soccer / price=0.50-0.70 (n=59, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0155 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0549 | Sports / Soccer / type=moneyline (n=54, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0087 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.022 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0013 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x6046a68e87c83b1bd9477985b302a0104c58afc3` | Itsmakingyoucry | -0.0048 | Sports / Soccer / pre (n=34, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0074 | Sports / Other sport / price=0.70-0.90 (n=58, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0219 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0318 | Sports / American Football (n=169, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0094 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0142 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0295 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x51c7d30511ed096b39a9392bad97e0dc76c298aa` | Chopperyyy | 0.0228 | Esports / Esports / Counter Strike (n=306, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1352 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0412 | Esports / price=0.50-0.70 (n=47, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0 |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0508 | Sports / American Football / pre (n=56, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbcf51140fd48e69c6e6d4bd09d38a629059856a1` | bqy0301 | 0.199 | Sports / price=0.30-0.50 (n=36, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x9cbb674bdacc27020e6adb549461e45ade24a2e1` | Tentm1 | 0.0346 | Sports / American Football / NFL (n=41, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x880dbf161120207d47aef05ec774b331bcec39bc` | akulaxl | 0.0287 | Esports / Esports / type=moneyline (n=53, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c68066fe7466ad3048a4adff9ad18cfecdab7b` | lucianow34 | 0.0253 | Esports / price=0.50-0.70 (n=450, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=450, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0xe3ca22c1bb6f3b637a9baff915d363422f945ed4` | Rubadub | 0.032 | Sports / Soccer / Serie A 2025 (n=33, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x228090cc64ff9dfb8173ac5c46f4c60b9e2531cb` | 0x228090Cc64Ff9dfB8173AC5c46f4c60b9E2531cB-1769517977854 | 0.0323 | Esports / Esports / live (n=167, roi=+0.15) | Esports / Esports / type=moneyline (n=92, roi=+0.19) | Esports / Esports / Counter Strike (n=176, roi=+0.13) | Esports (n=180, roi=+0.13) | Esports / Esports (n=180, roi=+0.13) | Crypto / price=0.70-0.90 (n=57, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0x173e8a681812cee182c8cc8041f8027b647f9ff4` | 0x50f161F7CD7aE6A7Df8E6E9a7A475EFa20f3e3b1-1757699966720 | 0.0605 | Esports / Esports / type=moneyline (n=127, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5e5175106a7dbbd92b10f1b56458fc8c1bdd42ce` | 0x5E5175106a7Dbbd92B10f1b56458Fc8c1Bdd42ce-1730865746538 | 0.0475 | Esports / price=0.30-0.50 (n=134, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=134, roi=+0.24) | Esports / Esports / live (n=426, roi=+0.12) | Esports / Esports / type=moneyline (n=125, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.0706 | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0xd670301420f6011e8136b07c50d7f4002bcee98f` | Mrpitter | Culture | 90 | 0.5276 | 0.1197 | 2.03 | 0.544 | 8.0 | 23.31 | 70640 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 779 | 0.1109 | 0.0484 | 3.34 | 0.712 | 8.0 | 2.73 | 396955 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1435 | 0.2431 | 0.0421 | 6.2 | 0.555 | 8.0 | 2.49 | 57597 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 253 | 23.3322 | 21.9012 | 4.03 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0755 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.053 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1515 | 4.3204 | 4.3136 | 4.37 | 0.71 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.882 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 99 | 14.9322 | 12.9079 | 4.12 | 0.182 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2889 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7666 | 4.16 | 0.626 |
| `0x31121402…` | Sports / price=0.00-0.10 | 94 | 14.9574 | 12.3785 | 3.94 | 0.16 |
| `0xe8ca3f75…` | Sports / Tennis | 552 | 4.2226 | 4.2078 | 5.87 | 0.719 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 815 | 3.3744 | 3.3178 | 2.39 | 0.221 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 816 | 3.3696 | 3.3132 | 2.39 | 0.221 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8143 | 3.23 | 0.167 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2142 | 3.53 | 0.794 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6114 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6114 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4419 | 3.33 | 0.754 |
| `0xeda67a7f…` | Sports | 491 | 3.2428 | 3.2289 | 4.17 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3382 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 765 | 2.4694 | 2.441 | 4.63 | 0.66 |
| `0x86c878cd…` | Sports | 2293 | 1.4001 | 1.3997 | 6.34 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 844 | 2.3018 | 2.2799 | 4.75 | 0.648 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.7862 | 3.06 | 0.279 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8328 | 2.82 | 0.131 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8328 | 2.82 | 0.131 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 75 | 8.3715 | 6.7169 | 2.89 | 0.4 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5615 | 2.28 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport | 2933 | 1.032 | 1.0319 | 2.63 | 0.548 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2933 | 1.032 | 1.0319 | 2.63 | 0.548 |
| `0x1941ca5d…` | Sports | 2935 | 1.0314 | 1.0313 | 2.63 | 0.548 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7951 | 2.57 | 0.129 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3849 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 62 | 8.6662 | 6.6484 | 3.13 | 0.242 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1491 | 2.16 | 0.156 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9768 | 2.51 | 0.519 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.4804 | 2.64 | 0.31 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8603 | 2.71 | 0.206 |
| `0xe8ca3f75…` | Esports / Esports / live | 149 | 3.9107 | 3.8973 | 2.82 | 0.57 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6123 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 457 | 2.0659 | 2.1385 | 4.27 | 0.656 |
| `0xe8ca3f75…` | Esports / Esports | 457 | 2.0659 | 2.1385 | 4.27 | 0.656 |
| `0xef185339…` | Sports | 3851 | 0.731 | 0.731 | 22.73 | 0.69 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 158 | 3.994 | 3.5989 | 2.69 | 0.114 |
| `0x86c878cd…` | Sports / Tennis / WTA | 199 | 3.3376 | 3.1564 | 2.73 | 0.663 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0242 | 5.01 | 0.567 |
| `0x13997bdb…` | Sports | 4155 | 0.6774 | 0.6774 | 22.54 | 0.683 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5285 | 4.77 | 0.568 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5411 | 2.39 | 0.133 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7266 | 4.71 | 0.561 |
| `0xda0f4e3f…` | Sports / price=0.00-0.10 | 113 | 4.6241 | 4.0401 | 2.38 | 0.204 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 105 | 4.8689 | 4.147 | 2.87 | 0.552 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7732 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 432 | 1.9129 | 1.9963 | 4.77 | 0.766 |
| `0xd60c6fa3…` | Sports | 3588 | 0.6877 | 0.6877 | 20.92 | 0.685 |
| `0x1941ca5d…` | Sports / Other sport / live | 2227 | 0.8588 | 0.8602 | 3.34 | 0.592 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1049 | 1.2194 | 1.2102 | 17.34 | 0.6 |
| `0x33ae5c5d…` | Sports / price=0.00-0.10 | 246 | 2.6325 | 2.4556 | 3.13 | 0.419 |
| `0x4afbb658…` | Sports | 167 | 3.1326 | 2.9666 | 2.38 | 0.419 |
