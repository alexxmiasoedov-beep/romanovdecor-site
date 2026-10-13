# Отчёт воронки, 2026-10-13 07:30 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 54479 |
| 0. Из них не только 5-мин крипта | 51952 |
| 1. Прошли дешёвые отсечки | 4062 из 21555 |
| 2. Прошли по полной истории | 6 + сегментом 61 из 4062 |
| 3. Прошли реалистичный вход | 8 из 67 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 10467 |
| closed<50 | 5932 |
| top1_concentration | 5286 |
| history<90d | 4471 |
| entries>=0.90 | 4310 |
| open_now>10 | 3158 |
| short_crypto | 1480 |
| profit_from<0.10 | 1196 |
| positions>5000 | 137 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3657 |
| concurrency_p95>8 | 3207 |
| drawdown | 3112 |
| unstable_halves | 2670 |
| roi_copy<=0 | 1617 |
| silent | 724 |
| low_liquidity | 688 |
| both_sides | 571 |
| history<90d | 324 |
| top1_concentration | 299 |
| closed<50 | 252 |
| hold<1h | 171 |
| entries>=0.90 | 146 |
| short_crypto | 86 |
| segment_only:t<2.0 | 57 |
| profit_from<0.10 | 52 |
| segment_only:drawdown | 51 |
| sniping | 50 |
| segment_only:unstable_halves | 27 |
| segment_only:roi_copy<=0 | 11 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 55 |
| edge_decays_with_delay | 4 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xf765ab3b0652bf5919267dfb34b0a735d0f5752c` | peliasf7 | Crypto | 0.2768 | 2.71 | 0.238 | 0.2494 | 0.2086 | 3.0 | 24.92 | 0.0 | Crypto (n=97, roi=+0.28) | Crypto / Bitcoin (n=97, roi=+0.28) | Crypto / Bitcoin / BTC Multi Strikes Weekly (n=97, roi=+0.28) | Crypto / Bitcoin / type=binary (n=97, roi=+0.28) | Crypto / price=0.50-0.70 (n=48, roi=+0.25) | Crypto / Bitcoin / price=0.50-0.70 (n=48, roi=+0.25) |
| `0x85164d78aa4c8c2431ad451f9ee96faa97a62957` |  | Esports | 0.2586 | 2.18 | 0.1507 | 0.1736 | 0.2876 | 7.0 | 3.58 | 0.0 | все рынки |
| `0x75eec3edfdb7ffdcbdf80356eecffdf84ef576e1` | 0x4E4791190A23380576033adD5459a09fd41aa72A-1771581891454 | Sports | 0.2735 | 1.82 | 0.0896 | 0.0869 | 0.1626 | 7.0 | 6.87 | н/д | Sports / price=0.30-0.50 (n=33, roi=+0.38) |
| `0x9e7dcedc785d7f5497e715bca0335a9673e24368` | vinbot2 | Sports | 0.1233 | 1.22 | 0.0509 | 0.0647 | 0.0781 | 4.0 | 8.09 | 0.0 | Sports / Basketball / pre (n=31, roi=+0.31) |
| `0x49175d7f0ebdb4cae1a8e57141a6643c5e40d7c8` | yiuiyu | Sports | 0.0338 | 0.86 | 0.0548 | 0.0742 | 0.0516 | 6.0 | 4.21 | н/д | Sports / Baseball (n=32, roi=+0.14) | Sports / Baseball / MLB (n=32, roi=+0.14) | Sports / Baseball / type=moneyline (n=30, roi=+0.14) |
| `0x2763960f48eeedbea5796a55337b960815c386dd` | Ricardo30 | Sports | 0.0828 | 0.81 | 0.0134 | 0.0184 | 0.2101 | 4.0 | 20.4 | 0.0 | Sports / price=0.50-0.70 (n=33, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=33, roi=+0.18) |
| `0x68c26f360fb90ee2a44a7507c893a14acb7ec7e6` | yui6776 | Sports | 0.0123 | 0.29 | 0.0598 | 0.0744 | 0.0526 | 5.0 | 3.82 | н/д | Sports / Baseball (n=30, roi=+0.13) | Sports / Baseball / MLB (n=30, roi=+0.13) |
| `0x6a5ca57dc2e7786119f114a547d4d4ad1d4e493b` | MCB75 | Sports | 0.089 | 1.48 | 0.0935 | 0.0974 | 0.2747 | 6.0 | 14.7 | н/д | Sports / price=0.30-0.50 (n=113, roi=+0.23) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x75eec3edfdb7ffdcbdf80356eecffdf84ef576e1` | 0x4E4791190A23380576033adD5459a09fd41aa72A-1771581891454 | 0.2735 | Sports / price=0.30-0.50 (n=33, roi=+0.38) | segment_only:t<2.0 |
| `0x9e7dcedc785d7f5497e715bca0335a9673e24368` | vinbot2 | 0.1233 | Sports / Basketball / pre (n=31, roi=+0.31) | segment_only:t<2.0 |
| `0x73da1e371be9c623b3d80b86c42eacd92977b7ac` | ZOFGK | -0.0614 | Esports / Esports / pre (n=37, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.085 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1667 | Esports / price=0.10-0.30 (n=104, roi=+0.54) | Esports / Esports / price=0.10-0.30 (n=104, roi=+0.54) | Esports / Esports / type=child_moneyline (n=581, roi=+0.18) | Esports (n=675, roi=+0.16) | Esports / Esports (n=675, roi=+0.16) | Esports / Esports / Dota 2 (n=675, roi=+0.16) | segment_only:drawdown |
| `0x9246043ac062d160f1c8ee96872a3ccb2db59195` | 0x9246043AC062D160F1C8ee96872a3CCB2DB59195-1775834612409 | 0.039 | Sports (n=185, roi=+0.10) | Sports / Soccer (n=137, roi=+0.10) | Sports / Soccer / Premier League 2025 (n=38, roi=+0.17) | segment_only:t<2.0 |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.05 | Esports / price=0.50-0.70 (n=38, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=38, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown |
| `0x49175d7f0ebdb4cae1a8e57141a6643c5e40d7c8` | yiuiyu | 0.0338 | Sports / Baseball (n=32, roi=+0.14) | Sports / Baseball / MLB (n=32, roi=+0.14) | Sports / Baseball / type=moneyline (n=30, roi=+0.14) | segment_only:t<2.0 |
| `0x2763960f48eeedbea5796a55337b960815c386dd` | Ricardo30 | 0.0828 | Sports / price=0.50-0.70 (n=33, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=33, roi=+0.18) | segment_only:t<2.0 |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0167 | Sports / Soccer / price=0.50-0.70 (n=54, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0258 | Sports (n=92, roi=+0.07) | Sports / Soccer / Counter Strike (n=36, roi=+0.09) | Sports / price=0.70-0.90 (n=66, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3740f38cb19308b573d4cf550d1865e0f6f9a935` | tiltedinv | -0.0142 | Sports / Hockey / price=0.70-0.90 (n=31, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x20255f1ed1e9db14d2c663b588cbcc41306113c0` | 182837282 | -0.0123 | Sports / Tennis / price=0.70-0.90 (n=59, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1940efc707c1c2aaccd0eefabb63884ff190123e` | 0x1940EfC707c1c2AacCd0EEFaBb63884FF190123E-1768266454473 | -0.028 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | Sports / Basketball / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xce041dc32d338cf0a44d7a1b860e793fbdd0dbf6` |  | -0.0172 | Sports / price=0.70-0.90 (n=40, roi=+0.11) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c5a66321fd29406669f00391b6689e6d80bf75` | FrankCastro21 | -0.0106 | Esports / Esports / Dota 2 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0118 | Sports / Other sport / price=0.70-0.90 (n=48, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0026 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0036 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x68c26f360fb90ee2a44a7507c893a14acb7ec7e6` | yui6776 | 0.0123 | Sports / Baseball (n=30, roi=+0.13) | Sports / Baseball / MLB (n=30, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x75e04cc2fff48a555afc5415053b2ac2636f5c67` | MOCKBA | 0.0496 | Sports / Other sport / Elon Tweets (n=35, roi=+0.19) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0353 | Sports / price=0.30-0.50 (n=89, roi=+0.26) | Sports / Tennis / price=0.30-0.50 (n=36, roi=+0.30) | Sports / Basketball / type=moneyline (n=34, roi=+0.22) | Sports / Basketball (n=37, roi=+0.18) | Sports / Basketball / live (n=32, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xa0e16dbb5456cdd0c17c83b622178f20d932ba6d` | sunxiaochuan278 | 0.0055 | Esports / Esports / Counter Strike (n=37, roi=+0.04) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0096 | Sports / Soccer / pre (n=174, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=153, roi=+0.09) | Sports / price=0.70-0.90 (n=182, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.0159 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.031 | Sports / American Football (n=161, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0207 | Esports / price=0.50-0.70 (n=46, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=46, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0395 | Sports / Basketball / price=0.50-0.70 (n=31, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | 0.0201 | Sports / American Football / CFB 2026 (n=40, roi=+0.09) | Sports / American Football / live (n=32, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0214 | Esports / price=0.50-0.70 (n=44, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=44, roi=+0.18) | segment_only:t<2.0 |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0333 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x332d40ed4b0cb313059f4fc037dbe520bf2f7b0e` | NJ100DOLLAR | 0.0146 | Sports / Soccer / type=moneyline (n=236, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1352 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0657 | Sports / American Football / pre (n=53, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9cbb674bdacc27020e6adb549461e45ade24a2e1` | Tentm1 | 0.0346 | Sports / American Football / NFL (n=41, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xfb6256ad7ef7746d80c5f727c48b65e49d65288e` | WorldLive | Sports | 64 | 0.3595 | 0.3269 | 3.67 | 0.672 | 5.0 | 2.23 | 32437 | delayed_roi<=0 |
| `0x92d8a88f0a9fef812bdf5628770d6a0ecee39762` | pfk.bgd | Sports | 351 | 1.3562 | 0.2659 | 2.98 | 0.547 | 6.0 | 3.44 | 162733 | delayed_roi<=0 |
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 1037 | 0.3591 | 0.2621 | 11.17 | 0.743 | 8.0 | 1.22 | 30744 | delayed_roi<=0 |
| `0xf765ab3b0652bf5919267dfb34b0a735d0f5752c` | peliasf7 | Crypto | 97 | 0.2768 | 0.2366 | 2.71 | 0.629 | 3.0 | 24.92 | 291784 | прошёл |
| `0x85164d78aa4c8c2431ad451f9ee96faa97a62957` |  | Esports | 72 | 0.2586 | 0.1911 | 2.18 | 0.653 | 7.0 | 3.58 | 913402 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 740 | 0.1198 | 0.0562 | 3.51 | 0.719 | 8.0 | 2.77 | 390348 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 252 | 23.2304 | 21.8016 | 4.0 | 0.504 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0756 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0539 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1502 | 4.3223 | 4.3154 | 4.33 | 0.709 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8843 | 5.01 | 0.351 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.289 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7667 | 4.16 | 0.626 |
| `0x31121402…` | Sports / price=0.00-0.10 | 92 | 14.3986 | 11.8691 | 3.83 | 0.163 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1044 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 550 | 4.2364 | 4.2211 | 5.86 | 0.718 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7081 | 4.03 | 0.362 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9626 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9626 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8085 | 3.23 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 818 | 2.9609 | 2.9119 | 2.22 | 0.225 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 819 | 2.9567 | 2.9079 | 2.22 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2156 | 3.53 | 0.794 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6115 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6115 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.442 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3383 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 759 | 2.4893 | 2.4604 | 4.63 | 0.66 |
| `0x86c878cd…` | Sports | 2276 | 1.4092 | 1.4088 | 6.33 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 838 | 2.3187 | 2.2964 | 4.75 | 0.648 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8067 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8067 | 2.77 | 0.124 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7972 | 2.57 | 0.129 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3868 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7439 | 3.14 | 0.246 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3145 | 7.86 | 0.681 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.4358 | 4.18 | 0.62 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9791 | 8.06 | 0.75 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 46 | 10.7518 | 7.6778 | 2.58 | 0.457 |
| `0x1941ca5d…` | Sports / Other sport | 2918 | 0.9248 | 0.9247 | 2.47 | 0.545 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2918 | 0.9248 | 0.9247 | 2.47 | 0.545 |
| `0x1941ca5d…` | Sports | 2920 | 0.9243 | 0.9242 | 2.47 | 0.545 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8619 | 2.71 | 0.206 |
| `0xe8ca3f75…` | Esports / Esports / live | 148 | 3.9439 | 3.9265 | 2.83 | 0.574 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6119 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 455 | 2.0689 | 2.1417 | 4.26 | 0.657 |
| `0xe8ca3f75…` | Esports / Esports | 455 | 2.0689 | 2.1417 | 4.26 | 0.657 |
| `0xef185339…` | Sports | 3850 | 0.7314 | 0.7314 | 22.76 | 0.692 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.808 | 2.13 | 0.183 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1861 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0243 | 5.01 | 0.567 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9277 | 2.43 | 0.3 |
| `0x13997bdb…` | Sports | 4134 | 0.6783 | 0.6783 | 22.49 | 0.684 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5286 | 4.77 | 0.568 |
| `0xf5fe759c…` | Sports / Tennis / pre | 126 | 4.0477 | 3.8407 | 6.84 | 0.754 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7267 | 4.71 | 0.561 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7972 | 6.78 | 0.656 |
| `0xd60c6fa3…` | Sports | 3576 | 0.6966 | 0.6966 | 21.02 | 0.687 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7733 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 430 | 1.9199 | 2.0034 | 4.77 | 0.765 |
| `0x9e1ac2a1…` | Sports / price=0.00-0.10 | 44 | 8.7609 | 6.2168 | 2.09 | 0.159 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 333 | 2.2789 | 2.1949 | 4.33 | 0.408 |
| `0xd970693a…` | Sports | 2435 | 0.7963 | 0.7963 | 10.34 | 0.665 |
| `0xf5fe759c…` | Sports / Tennis | 161 | 3.1465 | 3.0791 | 6.46 | 0.677 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1049 | 1.2128 | 1.2038 | 17.26 | 0.6 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 538 | 1.6869 | 1.6563 | 3.62 | 0.586 |
