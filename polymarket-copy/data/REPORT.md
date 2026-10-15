# Отчёт воронки, 2026-10-15 07:19 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 57444 |
| 0. Из них не только 5-мин крипта | 55125 |
| 1. Прошли дешёвые отсечки | 4405 из 19755 |
| 2. Прошли по полной истории | 7 + сегментом 61 из 4405 |
| 3. Прошли реалистичный вход | 10 из 68 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 9558 |
| closed<50 | 8938 |
| top1_concentration | 7487 |
| entries>=0.90 | 4034 |
| history<90d | 3382 |
| short_crypto | 1287 |
| open_now>10 | 1056 |
| profit_from<0.10 | 880 |
| positions>5000 | 21 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3946 |
| concurrency_p95>8 | 3490 |
| drawdown | 3350 |
| unstable_halves | 2888 |
| roi_copy<=0 | 1761 |
| silent | 842 |
| low_liquidity | 700 |
| both_sides | 635 |
| top1_concentration | 323 |
| history<90d | 323 |
| closed<50 | 262 |
| hold<1h | 179 |
| entries>=0.90 | 157 |
| short_crypto | 92 |
| segment_only:t<2.0 | 57 |
| sniping | 53 |
| segment_only:drawdown | 49 |
| profit_from<0.10 | 44 |
| segment_only:unstable_halves | 30 |
| segment_only:roi_copy<=0 | 11 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 55 |
| edge_decays_with_delay | 3 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xd9f91fe605f1fb2ad72f0b586029ea212a7f47c7` | 0xd9F91fE605F1fB2AD72F0b586029eA212A7f47C7-1782975475013 | Sports | 0.2537 | 2.05 | 0.1301 | 0.1541 | 0.2346 | 6.0 | 5.02 | 0.0 | Sports (n=107, roi=+0.31) | Sports / Soccer (n=106, roi=+0.30) | Sports / Soccer / pre (n=75, roi=+0.32) | Sports / Soccer / FIFA World Cup (n=44, roi=+0.41) |
| `0x958d1624fdd019d0e78cad7042fcc5a8713ca6d0` | Amam43 | Sports | 0.1429 | 1.78 | 0.1113 | 0.1245 | 0.17 | 3.0 | 3.83 | н/д | Sports / Soccer / type=moneyline (n=51, roi=+0.27) | Sports / Soccer / pre (n=106, roi=+0.17) |
| `0x01f8a3b0b5e36bfa3fded3b17d6a3ad7f3e88a34` | 0mhm0 | Sports | 0.139 | 1.64 | 0.1154 | 0.1261 | 0.1759 | 8.0 | 3.83 | н/д | Sports / Soccer / FIFA World Cup (n=40, roi=+0.19) |
| `0x8d834f40b950244aa91edbe6d638be0409bad89c` | 0x8d83598759 | Esports | 0.1953 | 1.86 | 0.096 | 0.1141 | 0.2693 | 4.0 | 4.27 | н/д | Esports (n=93, roi=+0.26) | Esports / Esports (n=93, roi=+0.26) | Esports / Esports / pre (n=39, roi=+0.39) | Esports / price=0.30-0.50 (n=35, roi=+0.40) | Esports / Esports / price=0.30-0.50 (n=35, roi=+0.40) | Esports / Esports / League of Legends (n=82, roi=+0.24) |
| `0x54afa8b03ffcf582df8959d0f44b21d89d536629` |  | Sports | 0.1225 | 1.3 | 0.113 | 0.1009 | 0.0637 | 7.0 | 6.3 | н/д | Sports / Soccer / type=moneyline (n=61, roi=+0.19) |
| `0xa8f5903e34b304f1d081d41ea7a19f78faf9b772` | 0xA8F5903E34b304F1D081d41eA7A19f78faF9B772-1781575925589 | Sports | 0.2099 | 1.65 | 0.1055 | 0.1036 | 0.1806 | 6.0 | 5.01 | н/д | Sports / Soccer / FIFA World Cup (n=67, roi=+0.27) |
| `0x326763399be9a0a81c47c01f942e8b27f4aa2f71` | pabilao | Sports | 0.193 | 1.68 | 0.041 | 0.0493 | 0.1674 | 7.0 | 4.92 | н/д | Sports / Soccer / live (n=42, roi=+0.51) |
| `0x336ea8af5a4462d01304026af7bc8fd31673cae9` |  | Sports | 0.1142 | 1.15 | 0.0739 | 0.0949 | 0.1184 | 4.0 | 5.97 | 0.0 | Sports / price=0.50-0.70 (n=46, roi=+0.22) |
| `0xadf3fe81c99923655ab4953a242a6b12342e7916` | 0xadf3fE81c99923655AB4953a242A6B12342e7916-1774966799507 | Sports | 0.1053 | 1.21 | 0.0103 | 0.0246 | 0.1365 | 4.0 | 5.13 | 0.0 | Sports / Soccer / pre (n=109, roi=+0.20) |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | Sports | 0.021 | 0.57 | 0.025 | 0.0476 | 0.0193 | 3.0 | 1.41 | н/д | Sports / American Football / CFB 2026 (n=40, roi=+0.09) | Sports / American Football / live (n=32, roi=+0.10) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x8d834f40b950244aa91edbe6d638be0409bad89c` | 0x8d83598759 | 0.1953 | Esports (n=93, roi=+0.26) | Esports / Esports (n=93, roi=+0.26) | Esports / Esports / pre (n=39, roi=+0.39) | Esports / price=0.30-0.50 (n=35, roi=+0.40) | Esports / Esports / price=0.30-0.50 (n=35, roi=+0.40) | Esports / Esports / League of Legends (n=82, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown |
| `0x958d1624fdd019d0e78cad7042fcc5a8713ca6d0` | Amam43 | 0.1429 | Sports / Soccer / type=moneyline (n=51, roi=+0.27) | Sports / Soccer / pre (n=106, roi=+0.17) | segment_only:t<2.0 |
| `0x01f8a3b0b5e36bfa3fded3b17d6a3ad7f3e88a34` | 0mhm0 | 0.139 | Sports / Soccer / FIFA World Cup (n=40, roi=+0.19) | segment_only:t<2.0 |
| `0x54afa8b03ffcf582df8959d0f44b21d89d536629` |  | 0.1225 | Sports / Soccer / type=moneyline (n=61, roi=+0.19) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0547 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0534 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x326763399be9a0a81c47c01f942e8b27f4aa2f71` | pabilao | 0.193 | Sports / Soccer / live (n=42, roi=+0.51) | segment_only:t<2.0 |
| `0xa8f5903e34b304f1d081d41ea7a19f78faf9b772` | 0xA8F5903E34b304F1D081d41eA7A19f78faF9B772-1781575925589 | 0.2099 | Sports / Soccer / FIFA World Cup (n=67, roi=+0.27) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x73da1e371be9c623b3d80b86c42eacd92977b7ac` | ZOFGK | -0.0631 | Esports / Esports / pre (n=37, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.085 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0x336ea8af5a4462d01304026af7bc8fd31673cae9` |  | 0.1142 | Sports / price=0.50-0.70 (n=46, roi=+0.22) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1599 | Esports / price=0.10-0.30 (n=106, roi=+0.55) | Esports / Esports / price=0.10-0.30 (n=106, roi=+0.55) | Esports / Esports / type=child_moneyline (n=593, roi=+0.18) | Esports (n=689, roi=+0.16) | Esports / Esports (n=689, roi=+0.16) | Esports / Esports / Dota 2 (n=689, roi=+0.16) | segment_only:drawdown |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0552 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0756 | Sports / Soccer / type=moneyline (n=52, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xadf3fe81c99923655ab4953a242a6b12342e7916` | 0xadf3fE81c99923655AB4953a242A6B12342e7916-1774966799507 | 0.1053 | Sports / Soccer / pre (n=109, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0125 | Sports / price=0.50-0.70 (n=173, roi=+0.09) | Sports / Soccer / price=0.50-0.70 (n=55, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.023 | Sports (n=92, roi=+0.07) | Sports / Soccer / Counter Strike (n=36, roi=+0.09) | Sports / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5d68ae7869c19cb27deb63ae8d911d59d6a7ff40` | 0x5D68ae7869C19Cb27DEB63Ae8d911D59D6a7Ff40-1782738338244 | 0.0233 | Sports / Other sport / type=totals (n=74, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x596c6cfc62e13ec38e15e1f20161d83ea6af28eb` | Riskyyy | 0.0496 | Sports / price=0.50-0.70 (n=43, roi=+0.22) | Sports / Soccer / price=0.50-0.70 (n=35, roi=+0.22) | Sports / Soccer / pre (n=58, roi=+0.17) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0087 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xce041dc32d338cf0a44d7a1b860e793fbdd0dbf6` |  | -0.0077 | Sports / price=0.70-0.90 (n=42, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0057 | Sports / Soccer / Indian Premier League (n=97, roi=+0.07) | Sports / price=0.70-0.90 (n=142, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x62c5a66321fd29406669f00391b6689e6d80bf75` | FrankCastro21 | -0.0101 | Esports / Esports / Dota 2 (n=36, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0102 | Sports / Other sport / price=0.70-0.90 (n=48, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x75e04cc2fff48a555afc5415053b2ac2636f5c67` | pepebot | 0.0516 | Sports / Other sport / Elon Tweets (n=36, roi=+0.19) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0103 | Sports / Soccer / pre (n=179, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=158, roi=+0.09) | Sports / price=0.70-0.90 (n=187, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0162 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x191267f5c2074ccbfe4fe3d6996797148fdfdef8` | heal1god | 0.0498 | Sports / Hockey (n=35, roi=+0.31) | Sports / Hockey / NHL 2026 (n=35, roi=+0.31) | Sports / Hockey / type=moneyline (n=30, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0404 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | 0.021 | Sports / American Football / CFB 2026 (n=40, roi=+0.09) | Sports / American Football / live (n=32, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0x2d371426b30f6a1d21427c174d45551fc33859b5` | highschoolkidd | 0.0592 | Sports / price=0.50-0.70 (n=78, roi=+0.13) | Sports / Tennis / price=0.50-0.70 (n=40, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0307 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca27292ae5f9c8e6d010e66f37c28928e8cb6f19` | underhaugsvei | 0.0367 | Sports / Soccer / live (n=103, roi=+0.16) | Sports / Soccer / type=totals (n=50, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x45361ff76a9308998703e0acb658691eca9af41b` | russeN1 | 0.0391 | Esports / price=0.30-0.50 (n=72, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=72, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0264 | Esports / price=0.50-0.70 (n=45, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=45, roi=+0.19) | segment_only:t<2.0 |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1352 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xfb6256ad7ef7746d80c5f727c48b65e49d65288e` | WorldLive | Sports | 70 | 0.3468 | 0.316 | 3.84 | 0.671 | 5.0 | 2.17 | 32437 | delayed_roi<=0 |
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 1059 | 0.3589 | 0.2637 | 11.37 | 0.744 | 7.0 | 1.24 | 30311 | delayed_roi<=0 |
| `0x92d8a88f0a9fef812bdf5628770d6a0ecee39762` | pfk.bgd | Sports | 352 | 1.3526 | 0.2653 | 2.98 | 0.548 | 6.0 | 3.41 | 162733 | delayed_roi<=0 |
| `0xd9f91fe605f1fb2ad72f0b586029ea212a7f47c7` | 0xd9F91fE605F1fB2AD72F0b586029eA212A7f47C7-1782975475013 | Sports | 118 | 0.2537 | 0.1393 | 2.05 | 0.551 | 6.0 | 5.02 | 1227741 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 756 | 0.1201 | 0.057 | 3.55 | 0.717 | 8.0 | 2.75 | 398156 | edge_decays_with_delay |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1385 | 0.2477 | 0.0486 | 6.23 | 0.565 | 8.0 | 2.55 | 55523 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0536 | 5.92 | 0.224 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8835 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 98 | 15.0948 | 13.0357 | 4.12 | 0.184 |
| `0x31121402…` | Sports / price=0.00-0.10 | 94 | 14.0709 | 11.6436 | 3.81 | 0.16 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1044 | 4.18 | 0.329 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7081 | 4.03 | 0.362 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8087 | 3.23 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 812 | 2.9719 | 2.9222 | 2.21 | 0.224 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 813 | 2.9677 | 2.9181 | 2.21 | 0.224 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2151 | 3.53 | 0.794 |
| `0xeda67a7f…` | Sports | 479 | 3.3175 | 3.3026 | 4.16 | 0.543 |
| `0x86c878cd…` | Sports / Tennis / live | 762 | 2.4789 | 2.4503 | 4.63 | 0.66 |
| `0x86c878cd…` | Sports | 2282 | 1.406 | 1.4056 | 6.33 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 841 | 2.3098 | 2.2878 | 4.75 | 0.648 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8062 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8062 | 2.77 | 0.124 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5824 | 2.28 | 0.167 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7965 | 2.57 | 0.129 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3854 | 2.85 | 0.269 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 55 | 9.5846 | 7.1755 | 2.73 | 0.455 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7438 | 3.14 | 0.246 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3143 | 7.86 | 0.681 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.4358 | 4.18 | 0.62 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9789 | 8.06 | 0.75 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1716 | 2.16 | 0.156 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9803 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2922 | 0.9193 | 0.9192 | 2.46 | 0.546 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2922 | 0.9193 | 0.9192 | 2.46 | 0.546 |
| `0x1941ca5d…` | Sports | 2924 | 0.9188 | 0.9187 | 2.46 | 0.546 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8608 | 2.71 | 0.206 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6121 | 2.86 | 0.07 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 157 | 4.0258 | 3.6263 | 2.69 | 0.115 |
| `0x7bbb2a27…` | Esports / price=0.00-0.10 | 114 | 4.9036 | 4.2344 | 2.32 | 0.088 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1857 | 2.73 | 0.665 |
| `0x41558102…` | Sports / price=0.00-0.10 | 41 | 9.9583 | 6.7977 | 2.42 | 0.293 |
| `0x7bbb2a27…` | Esports / Esports / price=0.00-0.10 | 111 | 4.7629 | 4.0998 | 2.21 | 0.081 |
| `0xf5fe759c…` | Sports / Tennis / pre | 126 | 4.0477 | 3.8406 | 6.84 | 0.754 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5434 | 2.39 | 0.133 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7971 | 6.78 | 0.656 |
| `0x3803425e…` | Sports / Soccer / price=0.00-0.10 | 155 | 3.8022 | 3.4226 | 2.89 | 0.194 |
| `0x3803425e…` | Sports / price=0.00-0.10 | 162 | 3.5947 | 3.2525 | 2.85 | 0.185 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 125 | 4.0823 | 3.6405 | 2.98 | 0.408 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 334 | 2.271 | 2.1876 | 4.33 | 0.407 |
| `0xd970693a…` | Sports | 2439 | 0.7947 | 0.7947 | 10.33 | 0.664 |
| `0xf5fe759c…` | Sports / Tennis | 161 | 3.1465 | 3.079 | 6.46 | 0.677 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 538 | 1.6869 | 1.6563 | 3.62 | 0.586 |
| `0x7a0ca89b…` | Sports | 233 | 2.5518 | 2.5138 | 2.9 | 0.665 |
| `0x4afbb658…` | Sports | 166 | 3.1455 | 2.9762 | 2.37 | 0.416 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 89 | 4.8672 | 4.0412 | 2.52 | 0.539 |
| `0xeda67a7f…` | Sports / Tennis / live | 186 | 2.7496 | 2.7687 | 2.33 | 0.575 |
| `0x86c878cd…` | Sports / Tennis / ATP | 401 | 1.897 | 1.8715 | 3.11 | 0.628 |
| `0xe9f5c75e…` | Sports / Basketball | 974 | 1.2079 | 1.2004 | 4.19 | 0.563 |
| `0xf5fe759c…` | Sports | 212 | 2.5521 | 2.5507 | 6.59 | 0.67 |
| `0xeda67a7f…` | Sports / Tennis | 196 | 2.597 | 2.6293 | 2.32 | 0.571 |
| `0xeda67a7f…` | Sports / Soccer / live | 172 | 2.773 | 2.7911 | 2.35 | 0.517 |
| `0x09b045ba…` | Sports / Soccer / price=0.00-0.10 | 75 | 5.0753 | 4.1919 | 2.32 | 0.373 |
| `0xeda67a7f…` | Sports / Soccer | 176 | 2.7065 | 2.731 | 2.35 | 0.517 |
| `0x09b045ba…` | Sports | 1660 | 0.8803 | 0.8803 | 8.02 | 0.714 |
| `0x92d8a88f…` | Sports / Soccer / price=0.00-0.10 | 45 | 7.0351 | 5.2866 | 2.08 | 0.244 |
| `0xe9f5c75e…` | Sports | 1706 | 0.8321 | 0.8321 | 4.7 | 0.583 |
