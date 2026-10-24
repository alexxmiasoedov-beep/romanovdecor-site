# Отчёт воронки, 2026-10-24 07:35 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 57521 |
| 0. Из них не только 5-мин крипта | 55445 |
| 1. Прошли дешёвые отсечки | 4238 из 16888 |
| 2. Прошли по полной истории | 8 + сегментом 57 из 4238 |
| 3. Прошли реалистичный вход | 5 из 65 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 7684 |
| closed<50 | 6899 |
| top1_concentration | 5487 |
| history<90d | 3280 |
| entries>=0.90 | 3148 |
| short_crypto | 1169 |
| open_now>10 | 1154 |
| profit_from<0.10 | 705 |
| positions>5000 | 26 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3848 |
| concurrency_p95>8 | 3280 |
| drawdown | 3190 |
| unstable_halves | 2797 |
| roi_copy<=0 | 1621 |
| silent | 727 |
| both_sides | 610 |
| low_liquidity | 557 |
| top1_concentration | 285 |
| history<90d | 281 |
| closed<50 | 271 |
| hold<1h | 162 |
| entries>=0.90 | 127 |
| short_crypto | 73 |
| segment_only:t<2.0 | 54 |
| segment_only:drawdown | 51 |
| profit_from<0.10 | 44 |
| sniping | 37 |
| segment_only:unstable_halves | 31 |
| segment_only:roi_copy<=0 | 13 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 59 |
| edge_decays_with_delay | 1 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xb8e1a95b94cefacff9c4ffc90075c2818567e114` | arturixx | Sports | 0.5008 | 2.52 | 0.3551 | 0.4447 | 0.4764 | 7.0 | 5.5 | 0.0 | Sports (n=64, roi=+0.52) | Sports / Soccer (n=56, roi=+0.55) | Sports / Soccer / type=moneyline (n=56, roi=+0.55) | Sports / Soccer / pre (n=31, roi=+0.62) | Sports / price=0.30-0.50 (n=30, roi=+0.61) |
| `0x7774ac7cdac3dac3a9f5806b947e79741bde2b2c` | HackTheSpread | Sports | 0.2 | 2.31 | 0.1674 | 0.1788 | 0.2153 | 6.0 | 8.33 | н/д | Sports (n=136, roi=+0.20) |
| `0x844e3f3b4fa18e68a933a02fd745970c793c4efd` | ljmcha | Sports | 0.2549 | 2.57 | 0.0459 | 0.0944 | 0.1907 | 5.0 | 2.12 | н/д | Sports (n=170, roi=+0.32) | Sports / Hockey (n=54, roi=+0.34) | Sports / Hockey / NHL 2026 (n=54, roi=+0.34) | Sports / Hockey / live (n=54, roi=+0.34) | Sports / Hockey / type=moneyline (n=48, roi=+0.35) | Sports / price=0.30-0.50 (n=67, roi=+0.28) |
| `0xadbcc575108767c8112ce117491dab73ced8c0ff` | trevordm | Esports | 0.1841 | 2.07 | 0.0935 | 0.1457 | 0.1657 | 5.0 | 2.38 | н/д | все рынки |
| `0x8f04c17395c51f27ec8a920383cccaab4c2a182a` | lokisimo | Esports | 0.0892 | 1.27 | 0.0117 | 0.021 | 0.1253 | 8.0 | 8.5 | н/д | Sports / Soccer / pre (n=110, roi=+0.17) | Sports / Soccer / type=moneyline (n=81, roi=+0.19) | Sports / Soccer (n=127, roi=+0.14) | Esports / price=0.50-0.70 (n=35, roi=+0.23) | Esports / Esports / price=0.50-0.70 (n=35, roi=+0.23) | Sports / price=0.70-0.90 (n=70, roi=+0.14) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0577 | Sports / Soccer / price=0.50-0.70 (n=65, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0619 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0515 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x80724b2f2cceea6fc407681ebc0b907f7a66c60a` | JTArb | 0.2306 | Esports / Esports / live (n=75, roi=+0.33) | segment_only:t<2.0 |
| `0x17d3c81eae22badd6c6f31202d7c629e25a5586b` | Buzz-lightyear | -0.0639 | Esports / price=0.70-0.90 (n=32, roi=+0.06) | Esports / Esports / price=0.70-0.90 (n=32, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0457 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca14f80a6daec5144052ee31403c01111cd85915` | UQ147 | 0.0763 | Sports / price=0.30-0.50 (n=34, roi=+0.42) | Sports / Tennis / live (n=37, roi=+0.28) | Sports / Tennis (n=42, roi=+0.20) | Sports / Tennis / type=moneyline (n=42, roi=+0.20) | segment_only:t<2.0 |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0998 | Esports / Esports / Valorant (n=55, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0559 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa538af775227c7add77418ba079ea3ae6a9212c3` | WinsonEnterpriseCorp | -0.0434 | Sports / price=0.50-0.70 (n=36, roi=+0.19) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4408cc367a713840d92693acd35cc205e59e1b6a` | 1xx3 | -0.0214 | Sports / Basketball (n=31, roi=+0.33) | Sports / Basketball / NBA 2026 (n=31, roi=+0.33) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0183 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0213 | Sports / Soccer / pre (n=40, roi=+0.22) | Sports / Soccer (n=41, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0039 | Sports / price=0.50-0.70 (n=208, roi=+0.09) | Sports / Soccer / price=0.50-0.70 (n=63, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9ede9359dd1a35d55edf3e44274c8ee84aca719a` | 0x9EDe9359dD1A35d55EDf3e44274c8eE84aca719a-1775478714615 | 0.1277 | Esports / Esports / price=0.30-0.50 (n=83, roi=+0.26) | Esports / price=0.30-0.50 (n=84, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | -0.0054 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0254 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c5a66321fd29406669f00391b6689e6d80bf75` | FrankCastro21 | -0.0049 | Esports / Esports / Dota 2 (n=39, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5d68ae7869c19cb27deb63ae8d911d59d6a7ff40` | 0x5D68ae7869C19Cb27DEB63Ae8d911D59D6a7Ff40-1782738338244 | 0.0078 | Sports / Other sport / type=totals (n=82, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x75e04cc2fff48a555afc5415053b2ac2636f5c67` | pepebot | 0.0516 | Sports / Other sport / Elon Tweets (n=36, roi=+0.19) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xa0e16dbb5456cdd0c17c83b622178f20d932ba6d` | sunxiaochuan278 | 0.0043 | Esports / Esports / Counter Strike (n=37, roi=+0.04) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1443 | Esports / price=0.10-0.30 (n=117, roi=+0.46) | Esports / Esports / price=0.10-0.30 (n=117, roi=+0.46) | Esports / Esports / type=child_moneyline (n=623, roi=+0.17) | Esports (n=721, roi=+0.15) | Esports / Esports (n=721, roi=+0.15) | Esports / Esports / Dota 2 (n=721, roi=+0.15) | segment_only:drawdown |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0333 | Sports / American Football (n=173, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0053 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | 0.0025 | Sports / Hockey / live (n=30, roi=+0.22) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x757ac68fdcd4c21ce005ba42f5bb6d96c4f11f84` | steadyhodl | 0.0395 | Sports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x880dbf161120207d47aef05ec774b331bcec39bc` | akulaxl | 0.0068 | Esports / Esports / type=moneyline (n=53, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8cbbf4e3d2d0b6fb7b684cf1f5ee12d79dfce8a8` | 0x8cBbF4e3d2D0b6Fb7b684cF1f5EE12d79dFCE8A8-1772503424879 | 0.0223 | Sports / American Football / NFL 2026 (n=41, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0232 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.137 | Sports / Basketball (n=72, roi=+0.38) | Sports / Basketball / NBA 2026 (n=72, roi=+0.38) | Sports / Basketball / type=moneyline (n=72, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0x8007ad03470539b924f93d3d263981c39d05a8f4` | OstapP | 0.007 | Sports / Other sport / price=0.70-0.90 (n=90, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0x0146df0b18f6faf92e814904edef6bf441694d51` | yndaa | 0.049 | Sports / price=0.50-0.70 (n=48, roi=+0.17) | Sports / price=0.70-0.90 (n=30, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2eed9db77bc86b46e2b8bfc2b4a60d87ec9e85a9` | Izreeaal | 0.0471 | Sports / price=0.30-0.50 (n=213, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0459 | Sports / American Football / pre (n=58, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9cbb674bdacc27020e6adb549461e45ade24a2e1` | Tentm1 | 0.0392 | Sports / American Football / NFL (n=41, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.046 | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | Sports / Soccer / price=0.50-0.70 (n=147, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c68066fe7466ad3048a4adff9ad18cfecdab7b` | lucianow34 | 0.0281 | Esports / price=0.50-0.70 (n=453, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=453, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xb8e1a95b94cefacff9c4ffc90075c2818567e114` | arturixx | Sports | 66 | 0.5008 | 0.3702 | 2.52 | 0.485 | 7.0 | 5.5 | 894786 | прошёл |
| `0x7774ac7cdac3dac3a9f5806b947e79741bde2b2c` | HackTheSpread | Sports | 136 | 0.2 | 0.1804 | 2.31 | 0.603 | 6.0 | 8.33 | 193005 | прошёл |
| `0x844e3f3b4fa18e68a933a02fd745970c793c4efd` | ljmcha | Sports | 188 | 0.2549 | 0.1379 | 2.57 | 0.601 | 5.0 | 2.12 | 480147 | прошёл |
| `0xadbcc575108767c8112ce117491dab73ced8c0ff` | trevordm | Esports | 121 | 0.1841 | 0.1391 | 2.07 | 0.612 | 5.0 | 2.38 | 665129 | прошёл |
| `0xd670301420f6011e8136b07c50d7f4002bcee98f` | Mrpitter | Culture | 97 | 0.4969 | 0.1183 | 2.06 | 0.546 | 8.0 | 22.81 | 63381 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 795 | 0.114 | 0.0516 | 3.46 | 0.712 | 8.0 | 2.7 | 398156 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1495 | 0.2326 | 0.0361 | 6.14 | 0.544 | 8.0 | 2.35 | 60125 | delayed_roi<=0 |
| `0x80533b4e25b0f8544311a6dfec062fa545f9d6e9` | paulo31 | Sports | 172 | 0.2065 | 0.0508 | 2.06 | 0.57 | 6.0 | 11.61 | 195320 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0519 | 5.92 | 0.224 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8795 | 5.01 | 0.351 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1041 | 4.18 | 0.329 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7077 | 4.03 | 0.362 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 800 | 3.4213 | 3.3624 | 2.38 | 0.22 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 801 | 3.4164 | 3.3576 | 2.38 | 0.22 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9621 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9621 | 3.45 | 0.324 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2125 | 3.53 | 0.794 |
| `0x31121402…` | Sports / price=0.00-0.10 | 99 | 9.101 | 7.6031 | 2.99 | 0.101 |
| `0x86c878cd…` | Sports / Tennis / live | 770 | 2.4522 | 2.4241 | 4.63 | 0.658 |
| `0x86c878cd…` | Sports | 2317 | 1.3904 | 1.39 | 6.36 | 0.637 |
| `0x86c878cd…` | Sports / Tennis | 850 | 2.2847 | 2.263 | 4.75 | 0.647 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 108 | 6.7828 | 5.7785 | 2.81 | 0.13 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 108 | 6.7828 | 5.7785 | 2.81 | 0.13 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 92 | 7.3868 | 6.1554 | 3.04 | 0.391 |
| `0x1941ca5d…` | Sports / Other sport | 2893 | 1.0424 | 1.0421 | 2.62 | 0.549 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2893 | 1.0424 | 1.0421 | 2.62 | 0.549 |
| `0x1941ca5d…` | Sports | 2895 | 1.0417 | 1.0415 | 2.62 | 0.549 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7928 | 2.57 | 0.129 |
| `0xe9f5c75e…` | Sports / Basketball / live | 465 | 2.4973 | 2.4286 | 4.19 | 0.622 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.4794 | 2.64 | 0.31 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6123 | 2.86 | 0.07 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 51 | 8.8039 | 6.377 | 2.09 | 0.098 |
| `0x86c878cd…` | Sports / Tennis / WTA | 200 | 3.3218 | 3.1417 | 2.73 | 0.665 |
| `0x1941ca5d…` | Sports / Other sport / live | 2203 | 0.8688 | 0.8701 | 3.34 | 0.593 |
| `0x33ae5c5d…` | Sports / price=0.00-0.10 | 272 | 2.6031 | 2.4438 | 3.33 | 0.426 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 545 | 1.6756 | 1.6457 | 3.64 | 0.591 |
| `0x4afbb658…` | Sports | 167 | 3.1326 | 2.9666 | 2.38 | 0.419 |
| `0xe9f5c75e…` | Sports / Basketball | 981 | 1.2051 | 1.1976 | 4.21 | 0.566 |
| `0x86c878cd…` | Sports / Tennis / ATP | 404 | 1.883 | 1.8574 | 3.11 | 0.626 |
| `0x80cd8310…` | Crypto / Ethereum / price=0.00-0.10 | 105 | 4.2204 | 3.6159 | 2.05 | 0.105 |
| `0xe9f5c75e…` | Sports | 1718 | 0.8305 | 0.8305 | 4.72 | 0.585 |
| `0x231034fb…` | Sports / Soccer / price=0.00-0.10 | 65 | 5.2324 | 4.1168 | 2.25 | 0.385 |
| `0xd0551fc6…` | Esports / Esports / type=kill_over_under_game | 78 | 4.1795 | 3.5011 | 2.01 | 0.474 |
| `0x33ae5c5d…` | Sports / Other sport / price=0.00-0.10 | 83 | 4.1177 | 3.3718 | 2.26 | 0.446 |
| `0xdf804b17…` | Sports / price=0.00-0.10 | 91 | 3.6699 | 3.0488 | 2.1 | 0.132 |
| `0xdf804b17…` | Sports / Soccer / price=0.00-0.10 | 84 | 3.8606 | 3.161 | 2.05 | 0.131 |
| `0x86c878cd…` | Sports / Tennis / ITF | 187 | 2.1539 | 2.0754 | 2.05 | 0.674 |
| `0x122b758a…` | Sports / price=0.00-0.10 | 396 | 1.4801 | 1.4261 | 2.78 | 0.159 |
| `0xd3989ba1…` | Politics / Biden | 63 | 4.583 | 3.5611 | 2.02 | 0.683 |
| `0xd3989ba1…` | Politics / Biden / ? | 63 | 4.583 | 3.5611 | 2.02 | 0.683 |
| `0x86c878cd…` | Sports / Other sport / live | 155 | 2.3331 | 2.2197 | 2.14 | 0.742 |
| `0x482acc0c…` | Sports / Soccer / price=0.00-0.10 | 256 | 1.8307 | 1.7223 | 2.33 | 0.109 |
| `0xe9f5c75e…` | Sports / Basketball / type=rebounds | 53 | 4.8164 | 3.7245 | 3.07 | 0.604 |
| `0x41558102…` | Sports / price=0.10-0.30 | 342 | 1.5193 | 1.4531 | 11.83 | 0.594 |
| `0x122b758a…` | Sports / Soccer / price=0.00-0.10 | 326 | 1.5525 | 1.4835 | 2.74 | 0.163 |
| `0xa991049a…` | Sports | 2389 | 0.5457 | 0.5443 | 8.36 | 0.716 |
| `0xd84d970b…` | Sports / Soccer / price=0.00-0.10 | 32 | 7.1213 | 4.6219 | 2.25 | 0.406 |
| `0x86c878cd…` | Sports / Other sport | 198 | 1.8961 | 1.8452 | 2.21 | 0.742 |
| `0x41558102…` | Sports | 6362 | 0.322 | 0.322 | 10.44 | 0.848 |
| `0x88eec58b…` | Sports / price=0.00-0.10 | 176 | 2.0286 | 1.9181 | 2.64 | 0.347 |
| `0x88eec58b…` | Sports / Other sport / price=0.00-0.10 | 176 | 2.0286 | 1.9181 | 2.64 | 0.347 |
| `0x33ae5c5d…` | Sports / Soccer / price=0.00-0.10 | 181 | 2.0637 | 1.8859 | 2.5 | 0.436 |
| `0x86c878cd…` | Sports / Soccer | 954 | 0.803 | 0.8141 | 3.25 | 0.631 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 179 | 2.0716 | 1.8788 | 2.28 | 0.117 |
| `0xcf0aca0d…` | Esports / price=0.00-0.10 | 231 | 1.7602 | 1.6443 | 2.58 | 0.26 |
| `0xcf0aca0d…` | Esports / Esports / price=0.00-0.10 | 231 | 1.7602 | 1.6443 | 2.58 | 0.26 |
| `0x86c878cd…` | Sports / Soccer / live | 786 | 0.8785 | 0.89 | 2.95 | 0.602 |
| `0x482acc0c…` | Sports / price=0.00-0.10 | 297 | 1.4959 | 1.4226 | 2.2 | 0.108 |
