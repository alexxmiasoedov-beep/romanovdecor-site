# Отчёт воронки, 2026-09-30 05:59 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 8259 |
| 0. Из них не только 5-мин крипта | 6993 |
| 1. Прошли дешёвые отсечки | 909 из 6993 |
| 2. Прошли по полной истории | 2 + сегментом 21 из 909 |
| 3. Прошли реалистичный вход | 9 из 23 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3559 |
| history<90d | 1932 |
| open_now>10 | 1506 |
| closed<50 | 1459 |
| entries>=0.90 | 1408 |
| top1_concentration | 1393 |
| short_crypto | 573 |
| profit_from<0.10 | 463 |
| positions>5000 | 100 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 757 |
| concurrency_p95>8 | 728 |
| t<2.0 | 716 |
| unstable_halves | 540 |
| roi_copy<=0 | 347 |
| low_liquidity | 214 |
| both_sides | 201 |
| history<90d | 142 |
| hold<1h | 70 |
| entries>=0.90 | 44 |
| short_crypto | 30 |
| sniping | 20 |
| segment_only:t<2.0 | 19 |
| top1_concentration | 16 |
| closed<50 | 15 |
| segment_only:drawdown | 14 |
| segment_only:unstable_halves | 10 |
| profit_from<0.10 | 8 |
| segment_only:roi_copy<=0 | 4 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 13 |
| edge_decays_with_delay | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x2edd21765f4ec11beb6e36b02324a6f6f33ce968` | wally77777 | Sports | 0.1305 | 2.22 | 0.1403 | 0.1582 | 0.137 | 8.0 | 4.61 | 0.0 | Sports / Baseball / price=0.30-0.50 (n=194, roi=+0.22) | Sports / price=0.30-0.50 (n=202, roi=+0.21) | Sports / Baseball (n=273, roi=+0.15) | Sports / Baseball / MLB (n=273, roi=+0.15) | Sports / Baseball / type=moneyline (n=273, roi=+0.15) | Sports (n=323, roi=+0.13) |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | Esports | 0.1616 | 1.89 | 0.0879 | 0.086 | 0.1777 | 3.0 | 2.29 | н/д | Esports / Esports / live (n=101, roi=+0.28) | Esports / Esports / Counter Strike (n=92, roi=+0.26) | Esports (n=114, roi=+0.23) | Esports / Esports (n=114, roi=+0.23) | Esports / price=0.30-0.50 (n=45, roi=+0.33) | Esports / Esports / price=0.30-0.50 (n=45, roi=+0.33) |
| `0x44d682939eb6a4a1349fa50411531876a6089858` | BobMcAdoo | Sports | 0.1618 | 1.68 | 0.0867 | 0.0921 | 0.1224 | 8.0 | 13.34 | н/д | Sports / Hockey (n=70, roi=+0.28) | Sports / Hockey / NHL 2026 (n=70, roi=+0.28) | Sports / Hockey / pre (n=70, roi=+0.28) |
| `0xa6f3d2650a19386887ba4c17c672c2b0a84da946` |  | Sports | 0.0915 | 1.92 | 0.0723 | 0.0905 | 0.0971 | 5.0 | 2.16 | н/д | Sports / Soccer / type=moneyline (n=39, roi=+0.23) | Esports / Esports / Counter Strike (n=41, roi=+0.14) |
| `0x6580ee60b526c9f7e3c3418faec466824caa96e5` | Staticglasshouse | Sports | 0.0539 | 1.04 | 0.0715 | 0.0794 | 0.0052 | 5.0 | 82.94 | 0.0 | Sports / Other sport / Elon Tweets 48H (n=38, roi=+0.13) |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | Sports | 0.0443 | 0.93 | 0.051 | 0.0729 | 0.0427 | 4.0 | 5.29 | 0.0 | Sports / price=0.70-0.90 (n=30, roi=+0.11) |
| `0xd1107f89750aaec9e290b61735b3a1399fb4566c` | Shane3200 | Sports | 0.0639 | 0.59 | 0.0408 | 0.0582 | 0.0903 | 7.0 | 8.6 | н/д | Sports / Baseball / price=0.50-0.70 (n=31, roi=+0.23) | Sports / price=0.50-0.70 (n=40, roi=+0.20) |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | Sports | 0.0529 | 1.13 | 0.0315 | 0.0499 | 0.1335 | 6.0 | 4.18 | н/д | Sports / price=0.50-0.70 (n=201, roi=+0.14) |
| `0x76c4ddc633346cee700360cec07b8617e9b1470b` | eXistenZ | Sports | 0.0547 | 1.18 | 0.0173 | 0.0165 | 0.0717 | 8.0 | 16.15 | -0.0 | Sports / price=0.30-0.50 (n=72, roi=+0.30) | Sports / Basketball / price=0.30-0.50 (n=70, roi=+0.30) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x2edd21765f4ec11beb6e36b02324a6f6f33ce968` | wally77777 | 0.1305 | Sports / Baseball / price=0.30-0.50 (n=194, roi=+0.22) | Sports / price=0.30-0.50 (n=202, roi=+0.21) | Sports / Baseball (n=273, roi=+0.15) | Sports / Baseball / MLB (n=273, roi=+0.15) | Sports / Baseball / type=moneyline (n=273, roi=+0.15) | Sports (n=323, roi=+0.13) | segment_only:drawdown |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | 0.1616 | Esports / Esports / live (n=101, roi=+0.28) | Esports / Esports / Counter Strike (n=92, roi=+0.26) | Esports (n=114, roi=+0.23) | Esports / Esports (n=114, roi=+0.23) | Esports / price=0.30-0.50 (n=45, roi=+0.33) | Esports / Esports / price=0.30-0.50 (n=45, roi=+0.33) | segment_only:t<2.0 |
| `0xa6f3d2650a19386887ba4c17c672c2b0a84da946` |  | 0.0915 | Sports / Soccer / type=moneyline (n=39, roi=+0.23) | Esports / Esports / Counter Strike (n=41, roi=+0.14) | segment_only:t<2.0 |
| `0x44d682939eb6a4a1349fa50411531876a6089858` | BobMcAdoo | 0.1618 | Sports / Hockey (n=70, roi=+0.28) | Sports / Hockey / NHL 2026 (n=70, roi=+0.28) | Sports / Hockey / pre (n=70, roi=+0.28) | segment_only:t<2.0 |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0727 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6580ee60b526c9f7e3c3418faec466824caa96e5` | Staticglasshouse | 0.0539 | Sports / Other sport / Elon Tweets 48H (n=38, roi=+0.13) | segment_only:t<2.0 |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.0559 | Sports / price=0.70-0.90 (n=74, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.0266 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | 0.0443 | Sports / price=0.70-0.90 (n=30, roi=+0.11) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd1107f89750aaec9e290b61735b3a1399fb4566c` | Shane3200 | 0.0639 | Sports / Baseball / price=0.50-0.70 (n=31, roi=+0.23) | Sports / price=0.50-0.70 (n=40, roi=+0.20) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | 0.0529 | Sports / price=0.50-0.70 (n=201, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0175 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x76c4ddc633346cee700360cec07b8617e9b1470b` | eXistenZ | 0.0547 | Sports / price=0.30-0.50 (n=72, roi=+0.30) | Sports / Basketball / price=0.30-0.50 (n=70, roi=+0.30) | segment_only:t<2.0;segment_only:drawdown |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0735 | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x191267f5c2074ccbfe4fe3d6996797148fdfdef8` | heal1god | 0.0597 | Sports / Hockey (n=35, roi=+0.31) | Sports / Hockey / NHL 2026 (n=35, roi=+0.31) | Sports / Hockey / type=moneyline (n=30, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.031 | Sports / price=0.30-0.50 (n=80, roi=+0.22) | Sports / Basketball / type=moneyline (n=32, roi=+0.20) | Sports / Basketball (n=35, roi=+0.16) | Sports / Basketball / live (n=30, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0108 | Esports / price=0.50-0.70 (n=106, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=106, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xdc81f14a6e9af07af6ca443f63de558c7612e889` |  | 0.0363 | Sports / Tennis / live (n=44, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0682 | Esports / price=0.50-0.70 (n=40, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=40, roi=+0.19) | segment_only:t<2.0 |
| `0x12d3cbfc0b5e095d03cb2a04f0676e46615d16c5` |  | 0.1074 | Sports / price=0.70-0.90 (n=32, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0xe23cd5fb6bee7b1c9f60f5d9969ac7ba52cc5ae7` | apprentice15 | 0.2252 | Sports / Soccer (n=438, roi=+0.26) | Sports / Soccer / live (n=428, roi=+0.26) | Sports (n=540, roi=+0.23) | Sports / price=0.10-0.30 (n=115, roi=+0.41) | Sports / Soccer / price=0.30-0.50 (n=148, roi=+0.19) | segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 522 | 0.192 | 0.1005 | 5.47 | 0.533 | 5.0 | 5.76 | 354717 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 682 | 0.115 | 0.0581 | 3.32 | 0.729 | 8.0 | 2.93 | 389189 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 824 | 2.9484 | 2.9004 | 2.23 | 0.225 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 825 | 2.9442 | 2.8963 | 2.23 | 0.224 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3172 | 7.86 | 0.681 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9822 | 8.06 | 0.75 |
| `0x1941ca5d…` | Sports / Other sport | 2863 | 0.9412 | 0.9411 | 2.47 | 0.53 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2863 | 0.9412 | 0.9411 | 2.47 | 0.53 |
| `0x1941ca5d…` | Sports | 2865 | 0.9406 | 0.9405 | 2.47 | 0.529 |
| `0xef185339…` | Sports | 3801 | 0.7293 | 0.7293 | 22.56 | 0.694 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9295 | 2.43 | 0.3 |
| `0xf5fe759c…` | Sports / Tennis / pre | 125 | 4.0799 | 3.8687 | 6.85 | 0.752 |
| `0x13997bdb…` | Sports | 4052 | 0.6787 | 0.6787 | 22.32 | 0.686 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7988 | 6.78 | 0.656 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 331 | 2.2968 | 2.2117 | 4.34 | 0.411 |
| `0xd970693a…` | Sports | 2384 | 0.8038 | 0.8038 | 10.22 | 0.663 |
| `0xf5fe759c…` | Sports / Tennis | 160 | 3.166 | 3.0974 | 6.47 | 0.675 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1030 | 1.196 | 1.1871 | 16.88 | 0.596 |
| `0xf5fe759c…` | Sports | 210 | 2.5652 | 2.5638 | 6.56 | 0.667 |
| `0x1985327e…` | Sports | 1273 | 1.0238 | 1.0238 | 2.59 | 0.72 |
| `0x13997bdb…` | Sports / Soccer | 2831 | 0.6851 | 0.685 | 18.35 | 0.691 |
| `0x13997bdb…` | Sports / Soccer / live | 2789 | 0.6883 | 0.6882 | 18.2 | 0.69 |
| `0xef185339…` | Sports / Soccer | 2571 | 0.7016 | 0.7018 | 18.74 | 0.693 |
| `0xef185339…` | Sports / Soccer / live | 2537 | 0.7018 | 0.702 | 18.55 | 0.691 |
| `0x1985327e…` | Sports / Soccer / live | 825 | 1.2325 | 1.2276 | 2.03 | 0.709 |
| `0x1985327e…` | Sports / Soccer | 835 | 1.2177 | 1.2132 | 2.03 | 0.708 |
| `0x13997bdb…` | Sports / price=0.10-0.30 | 1121 | 1.0395 | 1.0332 | 15.98 | 0.564 |
| `0xf5fe759c…` | Sports / Tennis / ATP | 91 | 3.8374 | 3.6051 | 6.47 | 0.758 |
| `0x1941ca5d…` | Sports / Other sport / live | 2167 | 0.7264 | 0.7282 | 3.58 | 0.573 |
| `0xed61f86b…` | Sports / price=0.10-0.30 | 801 | 1.182 | 1.165 | 20.2 | 0.795 |
| `0xed61f86b…` | Sports / Soccer / price=0.10-0.30 | 507 | 1.4304 | 1.3946 | 17.55 | 0.781 |
| `0xef185339…` | Sports / Soccer / price=0.10-0.30 | 671 | 1.2197 | 1.2055 | 13.86 | 0.607 |
| `0xed61f86b…` | Sports | 4059 | 0.488 | 0.488 | 26.16 | 0.846 |
| `0xdba10a9b…` | Sports / price=0.00-0.10 | 157 | 2.6369 | 2.4508 | 2.28 | 0.248 |
| `0xdba10a9b…` | Sports / Other sport / price=0.00-0.10 | 157 | 2.6369 | 2.4508 | 2.28 | 0.248 |
| `0xbfeceb41…` | Sports / price=0.00-0.10 | 389 | 1.5769 | 1.5226 | 2.34 | 0.077 |
| `0xd970693a…` | Sports / Soccer | 1590 | 0.7454 | 0.7461 | 8.77 | 0.665 |
| `0xed61f86b…` | Sports / Soccer | 2388 | 0.6078 | 0.6068 | 20.93 | 0.833 |
| `0xd970693a…` | Sports / Soccer / live | 1569 | 0.7475 | 0.7482 | 8.69 | 0.667 |
| `0xed61f86b…` | Sports / Soccer / live | 2330 | 0.6134 | 0.6123 | 21.02 | 0.84 |
| `0x13997bdb…` | Sports / Soccer / price=0.10-0.30 | 773 | 1.0463 | 1.037 | 13.32 | 0.564 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 135 | 2.8009 | 2.4698 | 2.47 | 0.348 |
| `0x03c9e3c6…` | Sports | 1010 | 0.8889 | 0.8889 | 7.1 | 0.701 |
| `0xd970693a…` | Sports / Other sport / price=0.00-0.10 | 112 | 2.9793 | 2.6496 | 2.71 | 0.339 |
| `0xef185339…` | Sports / price=0.00-0.10 | 234 | 1.9165 | 1.8229 | 5.22 | 0.483 |
| `0xaa930fdc…` | Sports / price=0.00-0.10 | 801 | 0.9897 | 0.9736 | 2.28 | 0.099 |
| `0xaa930fdc…` | Sports / Other sport / price=0.00-0.10 | 790 | 0.9959 | 0.9795 | 2.26 | 0.097 |
| `0xd970693a…` | Sports / Soccer / price=0.00-0.10 | 219 | 1.9477 | 1.852 | 3.42 | 0.447 |
| `0xef185339…` | Sports / Other sport / live | 1223 | 0.7822 | 0.7813 | 12.57 | 0.697 |
| `0xef185339…` | Sports / Other sport | 1224 | 0.7807 | 0.7799 | 12.55 | 0.696 |
| `0x482acc0c…` | Sports / Soccer / price=0.00-0.10 | 223 | 1.8959 | 1.7658 | 2.18 | 0.112 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 183 | 2.141 | 1.946 | 2.4 | 0.126 |
| `0x41558102…` | Sports / price=0.10-0.30 | 328 | 1.5216 | 1.4528 | 11.74 | 0.601 |
| `0xd970693a…` | Sports / Other sport / live | 775 | 0.9424 | 0.9389 | 5.62 | 0.666 |
| `0xd970693a…` | Sports / price=0.10-0.30 | 591 | 1.0725 | 1.0637 | 12.12 | 0.596 |
| `0xd970693a…` | Sports / Other sport | 791 | 0.921 | 0.9181 | 5.6 | 0.657 |
| `0x13997bdb…` | Sports / price=0.00-0.10 | 270 | 1.595 | 1.5318 | 4.91 | 0.448 |
| `0x03c9e3c6…` | Sports / price=0.00-0.10 | 57 | 4.191 | 3.3333 | 2.07 | 0.333 |
| `0x41558102…` | Sports | 6013 | 0.3244 | 0.3244 | 10.3 | 0.851 |
| `0x122b758a…` | Sports / price=0.00-0.10 | 301 | 1.4809 | 1.411 | 2.52 | 0.163 |
| `0x13997bdb…` | Sports / Soccer / type=moneyline | 529 | 1.076 | 1.0615 | 11.5 | 0.745 |
| `0x03c9e3c6…` | Sports / Soccer / live | 686 | 0.9202 | 0.9193 | 5.54 | 0.685 |
