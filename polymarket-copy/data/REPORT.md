# Отчёт воронки, 2026-09-27 05:51 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 7714 |
| 0. Из них не только 5-мин крипта | 6562 |
| 1. Прошли дешёвые отсечки | 921 из 6558 |
| 2. Прошли по полной истории | 4 + сегментом 15 из 921 |
| 3. Прошли реалистичный вход | 4 из 19 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3297 |
| history<90d | 2021 |
| open_now>10 | 1359 |
| closed<50 | 1300 |
| entries>=0.90 | 1127 |
| top1_concentration | 1061 |
| short_crypto | 569 |
| profit_from<0.10 | 403 |
| positions>5000 | 97 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 785 |
| t<2.0 | 752 |
| concurrency_p95>8 | 740 |
| unstable_halves | 563 |
| roi_copy<=0 | 353 |
| low_liquidity | 204 |
| both_sides | 190 |
| history<90d | 137 |
| hold<1h | 83 |
| entries>=0.90 | 39 |
| short_crypto | 30 |
| sniping | 16 |
| segment_only:t<2.0 | 15 |
| top1_concentration | 13 |
| closed<50 | 12 |
| segment_only:drawdown | 12 |
| profit_from<0.10 | 9 |
| segment_only:unstable_halves | 6 |
| segment_only:roi_copy<=0 | 4 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 14 |
| edge_decays_with_delay | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x36567ae38757008cee2cbbcdabbf870822b16a0c` | Steijn123. | Sports | 0.1128 | 2.21 | 0.0638 | 0.0945 | 0.1692 | 5.0 | 3.6 | н/д | Sports (n=310, roi=+0.11) | Sports / Other sport (n=35, roi=+0.20) |
| `0x7a741fb44f513f3ad715b2e98ddfc24ad3644c57` | charlo7928 | Sports | 0.2186 | 1.79 | 0.0359 | 0.0609 | 0.1527 | 8.0 | 3.25 | н/д | Sports / MMA/Boxing (n=72, roi=+0.35) | Sports / MMA/Boxing / UFC (n=72, roi=+0.35) | Sports / MMA/Boxing / type=moneyline (n=72, roi=+0.35) |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | Sports | 0.1181 | 1.24 | 0.0323 | 0.0474 | 0.1248 | 4.0 | 4.28 | 0.0107 | Sports / price=0.50-0.70 (n=37, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=37, roi=+0.21) |
| `0xd1e0c0db26fb636fb557704f05f7cd8ae4148913` | DjPonyboots | Sports | 0.0334 | 0.57 | 0.0358 | 0.0413 | 0.0464 | 5.0 | 7.28 | 0.0 | Sports / Basketball / price=0.50-0.70 (n=43, roi=+0.19) | Sports / Basketball / NBA 2026 (n=62, roi=+0.15) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0741 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1208 | Sports / Soccer / price=0.50-0.70 (n=83, roi=+0.29) | Sports / Soccer (n=160, roi=+0.18) | Sports / Soccer / type=moneyline (n=41, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown |
| `0x6fe306bbc57d7586cea47730985a3ecce5f5da66` | BanditMarket | -0.0673 | Sports / Other sport (n=102, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x7a741fb44f513f3ad715b2e98ddfc24ad3644c57` | charlo7928 | 0.2186 | Sports / MMA/Boxing (n=72, roi=+0.35) | Sports / MMA/Boxing / UFC (n=72, roi=+0.35) | Sports / MMA/Boxing / type=moneyline (n=72, roi=+0.35) | segment_only:t<2.0 |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | 0.1181 | Sports / price=0.50-0.70 (n=37, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=37, roi=+0.21) | segment_only:t<2.0 |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.018 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd1e0c0db26fb636fb557704f05f7cd8ae4148913` | DjPonyboots | 0.0334 | Sports / Basketball / price=0.50-0.70 (n=43, roi=+0.19) | Sports / Basketball / NBA 2026 (n=62, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.009 | Sports / Soccer / Indian Premier League (n=97, roi=+0.07) | Sports / price=0.70-0.90 (n=131, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=64, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | -0.005 | Sports / Soccer / price=0.70-0.90 (n=132, roi=+0.09) | Sports / price=0.70-0.90 (n=161, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x758f40d5c4a76350096f3deaa0d016ed52efdfb7` | 0nglee | 0.0128 | Sports / Soccer (n=40, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0364 | Sports / price=0.30-0.50 (n=78, roi=+0.23) | Sports (n=380, roi=+0.08) | Sports / Basketball / type=moneyline (n=32, roi=+0.20) | Sports / Basketball (n=35, roi=+0.17) | Sports / Basketball / live (n=30, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0833 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x3073426164206b8f9165282d0963d70b19fb3413` | conqgs | 0.081 | Esports / price=0.50-0.70 (n=112, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=112, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xad6a849b0139699f370d1d467c00503c8fef9dbd` | stillachance | 0.0211 | Sports / MMA/Boxing / live (n=30, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.1089 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 888 | 0.3356 | 0.2493 | 10.08 | 0.745 | 8.0 | 1.05 | 34157 | delayed_roi<=0 |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 551 | 0.1889 | 0.0994 | 5.58 | 0.528 | 6.0 | 6.07 | 364530 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 677 | 0.1166 | 0.0598 | 3.35 | 0.73 | 8.0 | 2.94 | 389189 | delayed_roi<=0 |
| `0x36567ae38757008cee2cbbcdabbf870822b16a0c` | Steijn123. | Sports | 312 | 0.1128 | 0.0601 | 2.21 | 0.535 | 5.0 | 3.6 | 67197 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 210 | 13.2015 | 12.1745 | 5.88 | 0.219 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8897 | 5.01 | 0.351 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7002 | 4.03 | 0.362 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 84 | 12.5036 | 10.2525 | 4.03 | 0.321 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 820 | 2.9655 | 2.9171 | 2.23 | 0.227 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 821 | 2.9613 | 2.913 | 2.23 | 0.227 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2191 | 3.53 | 0.794 |
| `0x86c878cd…` | Sports / Tennis / live | 747 | 2.5253 | 2.4957 | 4.63 | 0.659 |
| `0x86c878cd…` | Sports | 2205 | 1.4364 | 1.436 | 6.26 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 825 | 2.3515 | 2.3288 | 4.75 | 0.646 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 83 | 7.0292 | 5.9343 | 2.58 | 0.133 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.4034 | 2.85 | 0.269 |
| `0xe9f5c75e…` | Sports / Basketball / live | 458 | 2.5298 | 2.4573 | 4.18 | 0.618 |
| `0x1941ca5d…` | Sports / Other sport | 2841 | 0.9507 | 0.9506 | 2.47 | 0.53 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2841 | 0.9507 | 0.9506 | 2.47 | 0.53 |
| `0x1941ca5d…` | Sports | 2843 | 0.9502 | 0.9501 | 2.47 | 0.53 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 64 | 7.9495 | 6.2029 | 2.74 | 0.219 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.8518 | 2.13 | 0.183 |
| `0xef185339…` | Sports | 3794 | 0.7325 | 0.7325 | 22.6 | 0.695 |
| `0x86c878cd…` | Sports / Tennis / WTA | 196 | 3.3869 | 3.2021 | 2.73 | 0.663 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.93 | 2.43 | 0.3 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 331 | 2.2968 | 2.2118 | 4.34 | 0.411 |
| `0xd970693a…` | Sports | 2361 | 0.8061 | 0.8061 | 10.16 | 0.662 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 532 | 1.7008 | 1.6681 | 3.61 | 0.583 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1033 | 1.2014 | 1.1925 | 16.97 | 0.597 |
| `0x86c878cd…` | Sports / Tennis / ATP | 393 | 1.9302 | 1.9041 | 3.1 | 0.628 |
| `0xe9f5c75e…` | Sports / Basketball | 967 | 1.2123 | 1.2039 | 4.17 | 0.56 |
| `0x1985327e…` | Sports | 1254 | 1.0302 | 1.0302 | 2.57 | 0.719 |
| `0xef185339…` | Sports / Soccer | 2558 | 0.707 | 0.7072 | 18.77 | 0.693 |
| `0xef185339…` | Sports / Soccer / live | 2524 | 0.7073 | 0.7075 | 18.57 | 0.691 |
| `0x1985327e…` | Sports / Soccer / live | 806 | 1.2474 | 1.2421 | 2.01 | 0.707 |
| `0x1985327e…` | Sports / Soccer | 816 | 1.232 | 1.2272 | 2.01 | 0.706 |
| `0x1941ca5d…` | Sports / Other sport / live | 2148 | 0.7361 | 0.7379 | 3.6 | 0.573 |
| `0xbd938b88…` | Sports | 3665 | 0.5618 | 0.5618 | 2.06 | 0.704 |
| `0x5ad5c460…` | Sports / Soccer / live | 167 | 2.11 | 2.5832 | 2.17 | 0.281 |
| `0xed61f86b…` | Sports / price=0.10-0.30 | 799 | 1.1874 | 1.1704 | 20.29 | 0.797 |
| `0xe9f5c75e…` | Sports | 1636 | 0.7969 | 0.7969 | 4.57 | 0.579 |
| `0x09b045ba…` | Sports | 1590 | 0.8069 | 0.8069 | 9.68 | 0.718 |
| `0xed61f86b…` | Sports / Soccer / price=0.10-0.30 | 505 | 1.4401 | 1.4038 | 17.66 | 0.784 |
| `0xef185339…` | Sports / Soccer / price=0.10-0.30 | 673 | 1.2292 | 1.2148 | 13.96 | 0.608 |
| `0xed61f86b…` | Sports | 4052 | 0.49 | 0.49 | 26.24 | 0.847 |
| `0x5ad5c460…` | Sports / Soccer | 194 | 1.7878 | 2.2314 | 2.13 | 0.273 |
| `0xed61f86b…` | Sports / Soccer | 2382 | 0.6111 | 0.6101 | 21.02 | 0.835 |
| `0xd970693a…` | Sports / Soccer | 1569 | 0.7487 | 0.7494 | 8.71 | 0.664 |
| `0xed61f86b…` | Sports / Soccer / live | 2329 | 0.6141 | 0.613 | 21.04 | 0.84 |
| `0xd970693a…` | Sports / Soccer / live | 1548 | 0.7509 | 0.7516 | 8.63 | 0.665 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.81 | 2.81 | 0.664 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 116 | 3.0549 | 2.7241 | 2.96 | 0.405 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 132 | 2.8873 | 2.5395 | 2.49 | 0.356 |
| `0x86c878cd…` | Sports / Tennis / ITF | 179 | 2.2427 | 2.157 | 2.04 | 0.659 |
| `0xef185339…` | Sports / price=0.00-0.10 | 229 | 1.9731 | 1.8734 | 5.27 | 0.489 |
| `0x03c9e3c6…` | Sports | 993 | 0.8947 | 0.8947 | 7.04 | 0.702 |
| `0xd970693a…` | Sports / Other sport / price=0.00-0.10 | 112 | 2.9793 | 2.65 | 2.71 | 0.339 |
| `0x86c878cd…` | Sports / Other sport / live | 148 | 2.4159 | 2.2938 | 2.11 | 0.75 |
| `0xaa930fdc…` | Sports / price=0.00-0.10 | 797 | 0.9997 | 0.9834 | 2.29 | 0.099 |
| `0xaa930fdc…` | Sports / Other sport / price=0.00-0.10 | 786 | 1.0061 | 0.9894 | 2.28 | 0.098 |
| `0xd970693a…` | Sports / Soccer / price=0.00-0.10 | 219 | 1.9477 | 1.8522 | 3.42 | 0.447 |
| `0xef185339…` | Sports / Other sport / live | 1229 | 0.7801 | 0.7793 | 12.59 | 0.697 |
| `0xef185339…` | Sports / Other sport | 1230 | 0.7787 | 0.7779 | 12.57 | 0.697 |
| `0xe9f5c75e…` | Sports / Basketball / type=rebounds | 53 | 4.8164 | 3.7153 | 3.07 | 0.604 |
