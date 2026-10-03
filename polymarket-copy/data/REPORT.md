# Отчёт воронки, 2026-10-03 05:54 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 7758 |
| 0. Из них не только 5-мин крипта | 6566 |
| 1. Прошли дешёвые отсечки | 816 из 6566 |
| 2. Прошли по полной истории | 2 + сегментом 19 из 816 |
| 3. Прошли реалистичный вход | 9 из 21 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3469 |
| history<90d | 1822 |
| open_now>10 | 1706 |
| entries>=0.90 | 1424 |
| closed<50 | 1033 |
| top1_concentration | 999 |
| short_crypto | 520 |
| profit_from<0.10 | 399 |
| positions>5000 | 96 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 707 |
| t<2.0 | 669 |
| concurrency_p95>8 | 658 |
| unstable_halves | 506 |
| roi_copy<=0 | 335 |
| low_liquidity | 187 |
| both_sides | 171 |
| history<90d | 126 |
| hold<1h | 50 |
| entries>=0.90 | 36 |
| short_crypto | 23 |
| segment_only:t<2.0 | 19 |
| top1_concentration | 17 |
| sniping | 17 |
| segment_only:drawdown | 13 |
| closed<50 | 11 |
| profit_from<0.10 | 8 |
| segment_only:unstable_halves | 4 |
| segment_only:roi_copy<=0 | 2 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 11 |
| edge_decays_with_delay | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe478d4ca1c959e78f4ad9e563b134c54363128ea` | gmomoney | Sports | 0.1377 | 2.14 | 0.1416 | 0.1799 | 0.1657 | 8.0 | 6.47 | н/д | Sports / price=0.50-0.70 (n=106, roi=+0.21) | Sports (n=173, roi=+0.15) | Sports / Baseball / type=moneyline (n=40, roi=+0.29) | Sports / American Football / price=0.50-0.70 (n=33, roi=+0.31) |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | Sports | 0.1129 | 1.85 | 0.0743 | 0.0692 | 0.1182 | 3.0 | 4.24 | 0.0 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) |
| `0xfd8ff771a52c22a8a29a3156572d9b3e47fd761d` |  | Sports | 0.1836 | 1.3 | 0.0237 | 0.0308 | 0.1773 | 6.0 | 4.03 | 0.0 | Sports / American Football / type=spreads (n=37, roi=+0.27) |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | Sports | 0.035 | 0.72 | 0.0392 | 0.0601 | 0.0334 | 4.0 | 5.9 | 0.0 | Sports / price=0.70-0.90 (n=34, roi=+0.10) |
| `0x097bc96aa01bdc70705b8bdc86c9527265582907` | acey17 | Sports | 0.1031 | 1.13 | 0.02 | 0.0067 | 0.1027 | 6.0 | 2.34 | н/д | Sports / price=0.30-0.50 (n=42, roi=+0.30) |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | Sports | 0.1005 | 1.13 | 0.018 | 0.0339 | 0.0933 | 4.0 | 4.32 | 0.0 | Sports / price=0.50-0.70 (n=46, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=46, roi=+0.18) |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | Sports | 0.0591 | 1.28 | 0.0505 | 0.0688 | 0.1733 | 6.0 | 4.2 | -0.0 | Sports / price=0.50-0.70 (n=205, roi=+0.14) |
| `0x13ce0f6f73a83a2be1eb484c91169c2bd5b935f0` | mozak | Sports | -0.0287 | -1.02 | 0.0594 | 0.0616 | 0.0338 | 8.0 | 6.82 | н/д | Sports / Tennis / price=0.70-0.90 (n=34, roi=+0.10) |
| `0xaa9737b3db5d88aefcee007717a7c00b0df48c9c` | 0xf2cbF139C52b66c568dA19EF028f085289597B0e-1777085067547 | Sports | 0.1641 | 1.18 | 0.0014 | 0.0567 | 0.2331 | 4.0 | 4.27 | 0.0 | Sports / Soccer (n=52, roi=+0.40) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | 0.1129 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) | segment_only:t<2.0 |
| `0x6fe306bbc57d7586cea47730985a3ecce5f5da66` | BanditMarket | -0.0731 | Sports / Other sport (n=110, roi=+0.21) | Sports / Other sport / type=moneyline (n=94, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd8ff771a52c22a8a29a3156572d9b3e47fd761d` |  | 0.1836 | Sports / American Football / type=spreads (n=37, roi=+0.27) | segment_only:t<2.0 |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | 0.035 | Sports / price=0.70-0.90 (n=34, roi=+0.10) | segment_only:t<2.0 |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0567 | Esports / price=0.50-0.70 (n=34, roi=+0.25) | Esports / Esports / price=0.50-0.70 (n=34, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | 0.1005 | Sports / price=0.50-0.70 (n=46, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=46, roi=+0.18) | segment_only:t<2.0 |
| `0x097bc96aa01bdc70705b8bdc86c9527265582907` | acey17 | 0.1031 | Sports / price=0.30-0.50 (n=42, roi=+0.30) | segment_only:t<2.0;segment_only:drawdown |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | 0.0591 | Sports / price=0.50-0.70 (n=205, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x13ce0f6f73a83a2be1eb484c91169c2bd5b935f0` | mozak | -0.0287 | Sports / Tennis / price=0.70-0.90 (n=34, roi=+0.10) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | 0.0917 | Sports / Tennis / ATP (n=49, roi=+0.21) | Sports / Tennis / price=0.50-0.70 (n=48, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0037 | Sports / price=0.70-0.90 (n=132, roi=+0.06) | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=64, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd1e0c0db26fb636fb557704f05f7cd8ae4148913` | DjPonyboots | 0.0155 | Sports / Basketball / price=0.50-0.70 (n=43, roi=+0.19) | Sports / Basketball / NBA 2026 (n=62, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0147 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xaa9737b3db5d88aefcee007717a7c00b0df48c9c` | 0xf2cbF139C52b66c568dA19EF028f085289597B0e-1777085067547 | 0.1641 | Sports / Soccer (n=52, roi=+0.40) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0562 | Esports / price=0.50-0.70 (n=42, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.18) | segment_only:t<2.0 |
| `0xe70ce7a94ee228d75c97b0bdbf2a5eb0e3e11512` | 666CosmicOwl | 0.0162 | Sports / Tennis (n=109, roi=+0.11) | Sports / Tennis / type=moneyline (n=104, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x12d3cbfc0b5e095d03cb2a04f0676e46615d16c5` |  | 0.1217 | Sports / price=0.70-0.90 (n=36, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x43fe17cf68eb58be1d40514be0e52674b71d26ee` | 0x43fE17Cf68EB58BE1d40514Be0e52674B71d26eE-1768993726139 | 0.0561 | Sports / Basketball / price=0.30-0.50 (n=42, roi=+0.27) | Sports / Cricket / price=0.50-0.70 (n=149, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.1105 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 928 | 0.3386 | 0.2516 | 10.39 | 0.746 | 8.0 | 1.12 | 33592 | delayed_roi<=0 |
| `0xe478d4ca1c959e78f4ad9e563b134c54363128ea` | gmomoney | Sports | 190 | 0.1377 | 0.1276 | 2.14 | 0.637 | 8.0 | 6.47 | 267321 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 822 | 2.9471 | 2.899 | 2.22 | 0.224 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 823 | 2.9429 | 2.8949 | 2.22 | 0.224 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3987 | 2.85 | 0.269 |
| `0x1941ca5d…` | Sports / Other sport | 2868 | 0.9409 | 0.9408 | 2.47 | 0.532 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2868 | 0.9409 | 0.9408 | 2.47 | 0.532 |
| `0x1941ca5d…` | Sports | 2870 | 0.9403 | 0.9402 | 2.47 | 0.532 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 65 | 7.8118 | 6.1142 | 2.73 | 0.215 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 374 | 2.1379 | 2.0502 | 3.46 | 0.291 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 389 | 2.0788 | 1.9973 | 3.49 | 0.285 |
| `0x1941ca5d…` | Sports / Other sport / live | 2168 | 0.7272 | 0.729 | 3.59 | 0.576 |
| `0xbfeceb41…` | Sports / price=0.00-0.10 | 407 | 1.7086 | 1.6518 | 2.49 | 0.076 |
| `0x09b045ba…` | Sports | 1623 | 0.8014 | 0.8014 | 9.76 | 0.715 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 121 | 3.0655 | 2.7443 | 3.08 | 0.405 |
| `0x5f612351…` | Sports / Other sport / price=0.00-0.10 | 558 | 1.3025 | 1.2755 | 4.43 | 0.238 |
| `0x5f612351…` | Sports / price=0.00-0.10 | 559 | 1.2984 | 1.2715 | 4.42 | 0.238 |
| `0xdf804b17…` | Sports / price=0.00-0.10 | 88 | 3.8291 | 3.1663 | 2.12 | 0.136 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8088 | 2.81 | 0.664 |
| `0xdf804b17…` | Sports / Soccer / price=0.00-0.10 | 83 | 3.9192 | 3.2068 | 2.06 | 0.133 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 138 | 2.7183 | 2.4034 | 2.45 | 0.341 |
| `0x5f612351…` | Sports / Other sport / live | 2212 | 0.5831 | 0.5826 | 7.22 | 0.447 |
| `0xaa930fdc…` | Sports / price=0.00-0.10 | 812 | 0.9629 | 0.9477 | 2.25 | 0.097 |
| `0xaa930fdc…` | Sports / Other sport / price=0.00-0.10 | 801 | 0.9687 | 0.9531 | 2.23 | 0.096 |
| `0x5f612351…` | Sports / Other sport | 2256 | 0.567 | 0.5666 | 7.16 | 0.448 |
| `0x5f612351…` | Sports / Other sport / type=binary | 2256 | 0.567 | 0.5666 | 7.16 | 0.448 |
| `0x5f612351…` | Sports | 2270 | 0.5633 | 0.563 | 7.15 | 0.447 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 184 | 2.124 | 1.9317 | 2.39 | 0.125 |
| `0x164cb85e…` | Sports / Other sport / type=binary | 3007 | 0.4691 | 0.4687 | 5.87 | 0.554 |
| `0x164cb85e…` | Sports / Other sport | 3031 | 0.4658 | 0.4654 | 5.87 | 0.555 |
| `0x09b045ba…` | Sports / Soccer / live | 1033 | 0.7868 | 0.7871 | 6.81 | 0.709 |
| `0x09b045ba…` | Sports / Soccer | 1039 | 0.7814 | 0.7817 | 6.8 | 0.708 |
| `0x09b045ba…` | Sports / price=0.10-0.30 | 392 | 1.2932 | 1.2692 | 11.32 | 0.589 |
| `0x164cb85e…` | Sports | 3239 | 0.4348 | 0.4347 | 5.83 | 0.55 |
| `0x76697d10…` | Sports / Basketball / live | 952 | 0.7982 | 0.7941 | 3.83 | 0.577 |
| `0x76697d10…` | Sports / Basketball | 953 | 0.7963 | 0.7922 | 3.83 | 0.576 |
| `0x76697d10…` | Sports / Basketball / type=totals | 628 | 0.9795 | 0.9677 | 3.19 | 0.557 |
| `0x164cb85e…` | Sports / Other sport / Shanghai Daily Lowest Temperature | 296 | 1.4555 | 1.3893 | 2.22 | 0.557 |
| `0x09b045ba…` | Sports / Soccer / price=0.00-0.10 | 71 | 3.3985 | 2.8275 | 2.19 | 0.366 |
| `0xbfeceb41…` | Sports | 1468 | 0.6068 | 0.6053 | 3.13 | 0.416 |
| `0x164cb85e…` | Sports / Other sport / live | 2788 | 0.4342 | 0.434 | 5.9 | 0.562 |
| `0x91feec8a…` | Sports / Soccer / price=0.00-0.10 | 296 | 1.382 | 1.3104 | 3.03 | 0.118 |
| `0x76697d10…` | Sports | 1399 | 0.5978 | 0.5978 | 4.18 | 0.603 |
| `0x91feec8a…` | Sports / price=0.00-0.10 | 305 | 1.3117 | 1.2465 | 2.96 | 0.115 |
| `0x88eec58b…` | Sports / price=0.00-0.10 | 156 | 1.8259 | 1.7184 | 2.39 | 0.327 |
| `0x88eec58b…` | Sports / Other sport / price=0.00-0.10 | 156 | 1.8259 | 1.7184 | 2.39 | 0.327 |
| `0x91feec8a…` | Sports / Soccer / live | 2539 | 0.4272 | 0.4258 | 7.12 | 0.58 |
| `0x09b045ba…` | Sports / Other sport / live | 571 | 0.8536 | 0.8518 | 8.22 | 0.734 |
| `0xa991049a…` | Sports / price=0.10-0.30 | 256 | 1.3482 | 1.2678 | 11.1 | 0.641 |
| `0xc66ab53d…` | Sports / price=0.10-0.30 | 268 | 1.3001 | 1.2347 | 11.16 | 0.735 |
| `0x09b045ba…` | Sports / Other sport | 581 | 0.8372 | 0.836 | 8.19 | 0.726 |
| `0x88eec58b…` | Sports / Other sport / live | 474 | 0.9264 | 0.9245 | 3.58 | 0.468 |
| `0x88eec58b…` | Sports / Other sport / Chengdu Daily Weather | 220 | 1.3903 | 1.3478 | 2.71 | 0.495 |
| `0xaa930fdc…` | Sports / Other sport | 2380 | 0.4097 | 0.409 | 2.74 | 0.243 |
| `0xaa930fdc…` | Sports / Other sport / type=binary | 2380 | 0.4097 | 0.409 | 2.74 | 0.243 |
| `0x88eec58b…` | Sports | 496 | 0.8824 | 0.8823 | 3.56 | 0.466 |
| `0x88eec58b…` | Sports / Other sport | 496 | 0.8824 | 0.8823 | 3.56 | 0.466 |
| `0x88eec58b…` | Sports / Other sport / type=binary | 496 | 0.8824 | 0.8823 | 3.56 | 0.466 |
| `0xaa930fdc…` | Sports | 2501 | 0.388 | 0.3875 | 2.72 | 0.25 |
| `0xc66ab53d…` | Sports / Soccer / price=0.10-0.30 | 229 | 1.3295 | 1.2516 | 10.22 | 0.734 |
| `0x09b045ba…` | Sports / Soccer / price=0.10-0.30 | 252 | 1.2155 | 1.1849 | 8.52 | 0.563 |
| `0xa42f3648…` | Sports | 982 | 0.5996 | 0.5996 | 10.26 | 0.677 |
