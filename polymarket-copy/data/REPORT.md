# Отчёт воронки, 2026-09-23 10:34 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 11975 |
| 0. Из них не только 5-мин крипта | 10448 |
| 1. Прошли дешёвые отсечки | 1030 из 10446 |
| 2. Прошли по полной истории | 2 + сегментом 14 из 1030 |
| 3. Прошли реалистичный вход | 7 из 16 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 5546 |
| entries>=0.90 | 3644 |
| history<90d | 2300 |
| closed<50 | 2159 |
| top1_concentration | 2060 |
| open_now>10 | 1828 |
| short_crypto | 708 |
| profit_from<0.10 | 583 |
| positions>5000 | 100 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 894 |
| drawdown | 873 |
| concurrency_p95>8 | 851 |
| unstable_halves | 669 |
| roi_copy<=0 | 424 |
| low_liquidity | 240 |
| both_sides | 202 |
| history<90d | 146 |
| hold<1h | 67 |
| entries>=0.90 | 54 |
| short_crypto | 32 |
| top1_concentration | 31 |
| sniping | 27 |
| closed<50 | 21 |
| profit_from<0.10 | 13 |
| segment_only:t<2.0 | 12 |
| segment_only:drawdown | 8 |
| segment_only:unstable_halves | 3 |
| segment_only:roi_copy<=0 | 1 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 6 |
| edge_decays_with_delay | 2 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x4a1b8e8d38aecdc9687bb0f601801d59fa44724f` | ox1star84 | Sports | 0.1848 | 3.04 | 0.1647 | 0.1798 | 0.114 | 4.0 | 11.37 | 0.0005 | Sports (n=95, roi=+0.18) | Sports / MMA/Boxing (n=87, roi=+0.19) | Sports / MMA/Boxing / UFC (n=84, roi=+0.18) | Sports / MMA/Boxing / pre (n=66, roi=+0.20) | Sports / MMA/Boxing / type=moneyline (n=80, roi=+0.16) | Sports / MMA/Boxing / price=0.70-0.90 (n=51, roi=+0.17) |
| `0xf6683d202f76fc9b79e5be716ce8519dab5b5c69` | 0xf6683D202f76FC9B79E5BE716CE8519DAb5b5c69-1765800503123 | Sports | 0.1644 | 4.44 | 0.0841 | 0.0964 | 0.2021 | 8.0 | 7.43 | 0.0 | Sports (n=575, roi=+0.17) | Sports / Basketball (n=461, roi=+0.16) | Sports / Basketball / pre (n=456, roi=+0.16) | Sports / Basketball / NBA 2026 (n=408, roi=+0.16) | Sports / Basketball / type=spreads (n=293, roi=+0.17) | Sports / price=0.50-0.70 (n=335, roi=+0.15) |
| `0x2da245862be758df3908195772b1b06ef4808c2b` | vitbash | Esports | 0.0805 | 1.88 | 0.0537 | 0.0622 | 0.0825 | 3.0 | 3.81 | 0.0172 | Sports (n=85, roi=+0.15) | Sports / Soccer / live (n=30, roi=+0.18) |
| `0x4cb03276679d644ec1852f744668f345d41657e0` | l0wkirkenuinely | Esports | 0.1182 | 1.95 | 0.0494 | 0.0561 | 0.107 | 8.0 | 8.16 | 0.0 | Esports / price=0.30-0.50 (n=115, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=115, roi=+0.24) | Esports / Esports / League of Legends (n=106, roi=+0.23) | Esports / Esports / pre (n=226, roi=+0.15) | Esports (n=256, roi=+0.14) | Esports / Esports (n=256, roi=+0.14) |
| `0xc3f119fe0be9b7c3631332b2bc0ead67311e8391` | whataretheoddss | Esports | 0.0324 | 1.3 | 0.0476 | 0.07 | 0.172 | 8.0 | 2.81 | н/д | Esports / price=0.50-0.70 (n=99, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=99, roi=+0.12) |
| `0xf8fb48cefeb4b84ffeefee0d0ed453db403cc3ca` |  | Sports | 0.0206 | 0.52 | 0.0404 | 0.0854 | 0.0922 | 7.0 | 2.74 | 0.0 | Sports / Baseball / live (n=58, roi=+0.16) | Sports / Tennis / live (n=45, roi=+0.16) |
| `0xbf39c303bb8b7f061e3721fa14bf781a590f3394` | parlq | Sports | 0.0254 | 0.9 | 0.0967 | 0.1044 | 0.0629 | 7.0 | 1.64 | н/д | Esports (n=171, roi=+0.08) | Esports / Esports (n=171, roi=+0.08) | Esports / Esports / Dota 2 (n=83, roi=+0.11) | Esports / price=0.70-0.90 (n=86, roi=+0.09) | Esports / Esports / price=0.70-0.90 (n=86, roi=+0.09) | Esports / Esports / League of Legends (n=40, roi=+0.13) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xf6683d202f76fc9b79e5be716ce8519dab5b5c69` | 0xf6683D202f76FC9B79E5BE716CE8519DAb5b5c69-1765800503123 | 0.1644 | Sports (n=575, roi=+0.17) | Sports / Basketball (n=461, roi=+0.16) | Sports / Basketball / pre (n=456, roi=+0.16) | Sports / Basketball / NBA 2026 (n=408, roi=+0.16) | Sports / Basketball / type=spreads (n=293, roi=+0.17) | Sports / price=0.50-0.70 (n=335, roi=+0.15) | segment_only:drawdown |
| `0x2da245862be758df3908195772b1b06ef4808c2b` | vitbash | 0.0805 | Sports (n=85, roi=+0.15) | Sports / Soccer / live (n=30, roi=+0.18) | segment_only:t<2.0 |
| `0x4cb03276679d644ec1852f744668f345d41657e0` | l0wkirkenuinely | 0.1182 | Esports / price=0.30-0.50 (n=115, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=115, roi=+0.24) | Esports / Esports / League of Legends (n=106, roi=+0.23) | Esports / Esports / pre (n=226, roi=+0.15) | Esports (n=256, roi=+0.14) | Esports / Esports (n=256, roi=+0.14) | segment_only:t<2.0 |
| `0x9ac1b39372b486e96e8d0882f553ff8230cfd5a6` | YKBFN | 0.1313 | Sports / Basketball / price=0.30-0.50 (n=166, roi=+0.22) | Sports / Basketball (n=434, roi=+0.13) | Sports / Basketball / type=moneyline (n=434, roi=+0.13) | Sports / Basketball / NBA 2026 (n=321, roi=+0.15) | Sports (n=455, roi=+0.12) | Sports / price=0.30-0.50 (n=173, roi=+0.19) | segment_only:drawdown |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0594 | Esports / price=0.50-0.70 (n=34, roi=+0.26) | Esports / Esports / price=0.50-0.70 (n=34, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown |
| `0xc3f119fe0be9b7c3631332b2bc0ead67311e8391` | whataretheoddss | 0.0324 | Esports / price=0.50-0.70 (n=99, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=99, roi=+0.12) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0186 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf8fb48cefeb4b84ffeefee0d0ed453db403cc3ca` |  | 0.0206 | Sports / Baseball / live (n=58, roi=+0.16) | Sports / Tennis / live (n=45, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0785 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x049acd80fa3dbc98c2edf8b56202ce3a4c22f9d6` | ZKS009 | 0.0869 | Politics / price=0.70-0.90 (n=33, roi=+0.10) | Politics / Tweet Markets / price=0.70-0.90 (n=33, roi=+0.10) | segment_only:t<2.0 |
| `0xbf39c303bb8b7f061e3721fa14bf781a590f3394` | parlq | 0.0254 | Esports (n=171, roi=+0.08) | Esports / Esports (n=171, roi=+0.08) | Esports / Esports / Dota 2 (n=83, roi=+0.11) | Esports / price=0.70-0.90 (n=86, roi=+0.09) | Esports / Esports / price=0.70-0.90 (n=86, roi=+0.09) | Esports / Esports / League of Legends (n=40, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x6c2e83ce8e84ded3ec3c2212e139add8dabca5e8` | ZKS001 | 0.1004 | Politics / price=0.70-0.90 (n=33, roi=+0.08) | Politics / Tweet Markets / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:t<2.0 |
| `0xeead01aae45ba3f13f30d4bad3d0139570923a29` | ZKS008 | 0.0653 | Politics / price=0.70-0.90 (n=32, roi=+0.08) | Politics / Tweet Markets / price=0.70-0.90 (n=32, roi=+0.08) | segment_only:t<2.0 |
| `0x43fe17cf68eb58be1d40514be0e52674b71d26ee` | 0x43fE17Cf68EB58BE1d40514Be0e52674B71d26eE-1768993726139 | 0.0407 | Sports / Cricket / price=0.50-0.70 (n=145, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x4a1b8e8d38aecdc9687bb0f601801d59fa44724f` | ox1star84 | Sports | 99 | 0.1848 | 0.1814 | 3.04 | 0.838 | 4.0 | 11.37 | 286309 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 665 | 0.119 | 0.0622 | 3.38 | 0.731 | 8.0 | 2.98 | 384508 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 89 | 12.228 | 10.4356 | 3.47 | 0.157 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7038 | 4.03 | 0.362 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 84 | 12.5036 | 10.2556 | 4.03 | 0.321 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 817 | 2.992 | 2.9431 | 2.24 | 0.229 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 818 | 2.9877 | 2.939 | 2.24 | 0.229 |
| `0x9cf752d4…` | Sports / price=0.00-0.10 | 67 | 8.7638 | 7.3067 | 3.26 | 0.328 |
| `0xeda67a7f…` | Sports | 428 | 2.7973 | 2.7822 | 3.64 | 0.544 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 34 | 14.1086 | 9.7941 | 2.29 | 0.176 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 51 | 10.2308 | 7.5265 | 2.86 | 0.275 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 59 | 9.1577 | 6.9435 | 3.16 | 0.254 |
| `0xe9f5c75e…` | Sports / Basketball / live | 458 | 2.5298 | 2.458 | 4.18 | 0.618 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3194 | 7.86 | 0.681 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9848 | 8.06 | 0.75 |
| `0x1941ca5d…` | Sports / Other sport | 2826 | 0.9653 | 0.9651 | 2.5 | 0.524 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2826 | 0.9653 | 0.9651 | 2.5 | 0.524 |
| `0x1941ca5d…` | Sports | 2828 | 0.9647 | 0.9646 | 2.5 | 0.524 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 62 | 8.2382 | 6.3827 | 2.76 | 0.226 |
| `0xf5fe759c…` | Sports / Tennis / pre | 124 | 4.1089 | 3.8936 | 6.85 | 0.75 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 127 | 4.0219 | 3.8227 | 6.78 | 0.654 |
| `0xeda67a7f…` | Sports / Tennis / live | 156 | 3.268 | 3.1761 | 2.33 | 0.59 |
| `0xf5fe759c…` | Sports / Tennis | 159 | 3.1829 | 3.1131 | 6.47 | 0.673 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 368 | 2.1242 | 2.0345 | 3.39 | 0.285 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 383 | 2.0648 | 1.9814 | 3.42 | 0.279 |
| `0xeda67a7f…` | Sports / Tennis | 164 | 3.0949 | 3.0258 | 2.31 | 0.585 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 532 | 1.7008 | 1.6687 | 3.61 | 0.583 |
| `0xeda67a7f…` | Sports / Soccer / live | 158 | 3.0478 | 2.9817 | 2.38 | 0.519 |
| `0xe9f5c75e…` | Sports / Basketball | 967 | 1.2123 | 1.2042 | 4.17 | 0.56 |
| `0xf5fe759c…` | Sports | 209 | 2.5752 | 2.5737 | 6.56 | 0.665 |
| `0xeda67a7f…` | Sports / Soccer | 162 | 2.9687 | 2.9127 | 2.38 | 0.519 |
| `0xfe9b2c6d…` | Esports / price=0.00-0.10 | 52 | 6.7801 | 5.0294 | 2.01 | 0.135 |
| `0xfe9b2c6d…` | Esports / Esports / price=0.00-0.10 | 52 | 6.7801 | 5.0294 | 2.01 | 0.135 |
| `0x1941ca5d…` | Sports / Other sport / live | 2140 | 0.7523 | 0.7541 | 3.66 | 0.566 |
| `0x9cf752d4…` | Sports | 464 | 1.5748 | 1.6099 | 3.8 | 0.582 |
| `0xf5fe759c…` | Sports / Tennis / ATP | 91 | 3.8374 | 3.6069 | 6.47 | 0.758 |
| `0xe9f5c75e…` | Sports | 1601 | 0.813 | 0.813 | 4.56 | 0.577 |
| `0x2e7c5460…` | Sports / Tennis | 335 | 1.7822 | 1.705 | 3.38 | 0.463 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8112 | 2.81 | 0.664 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 131 | 2.917 | 2.5629 | 2.5 | 0.359 |
| `0xaa930fdc…` | Sports / price=0.00-0.10 | 783 | 1.0337 | 1.0165 | 2.33 | 0.101 |
| `0xaa930fdc…` | Sports / Other sport / price=0.00-0.10 | 772 | 1.0407 | 1.023 | 2.31 | 0.1 |
| `0xe9f5c75e…` | Sports / Basketball / type=rebounds | 53 | 4.8164 | 3.7197 | 3.07 | 0.604 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 178 | 2.2293 | 2.0202 | 2.43 | 0.129 |
| `0x76b8356b…` | Culture / price=0.00-0.10 | 282 | 1.6563 | 1.5818 | 2.01 | 0.326 |
| `0x482acc0c…` | Sports / Soccer / price=0.00-0.10 | 211 | 1.9026 | 1.7657 | 2.1 | 0.114 |
| `0x164cb85e…` | Sports / Other sport / type=binary | 2904 | 0.4753 | 0.4747 | 5.76 | 0.553 |
| `0x164cb85e…` | Sports / Other sport | 2928 | 0.4718 | 0.4712 | 5.77 | 0.554 |
| `0x76697d10…` | Sports / Basketball / live | 947 | 0.8058 | 0.8022 | 3.85 | 0.579 |
| `0x76697d10…` | Sports / Basketball | 948 | 0.8039 | 0.8003 | 3.84 | 0.578 |
| `0x164cb85e…` | Sports | 3210 | 0.431 | 0.4307 | 5.75 | 0.551 |
| `0x76697d10…` | Sports / Basketball / type=totals | 626 | 0.9858 | 0.9748 | 3.2 | 0.559 |
| `0x164cb85e…` | Sports / Other sport / Shanghai Daily Lowest Temperature | 282 | 1.5238 | 1.4484 | 2.21 | 0.553 |
| `0x76697d10…` | Sports | 1313 | 0.6318 | 0.6318 | 4.15 | 0.607 |
| `0x164cb85e…` | Sports / Other sport / live | 2693 | 0.4377 | 0.4373 | 5.77 | 0.561 |
| `0x91feec8a…` | Sports / Soccer / price=0.00-0.10 | 263 | 1.4361 | 1.3533 | 2.87 | 0.118 |
| `0x91feec8a…` | Sports / Soccer / live | 2186 | 0.4641 | 0.4623 | 6.86 | 0.578 |
| `0x91feec8a…` | Sports / price=0.00-0.10 | 268 | 1.3907 | 1.3125 | 2.83 | 0.116 |
| `0xf5fe759c…` | Sports / Tennis / WTA | 53 | 3.0405 | 2.9083 | 2.92 | 0.585 |
| `0x2e7c5460…` | Sports | 1317 | 0.5777 | 0.5752 | 4.05 | 0.588 |
| `0xaa930fdc…` | Sports / Other sport | 2296 | 0.4323 | 0.4315 | 2.79 | 0.242 |
| `0xaa930fdc…` | Sports / Other sport / type=binary | 2296 | 0.4323 | 0.4315 | 2.79 | 0.242 |
