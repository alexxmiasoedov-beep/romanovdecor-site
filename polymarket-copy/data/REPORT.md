# Отчёт воронки, 2026-09-28 05:57 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 8040 |
| 0. Из них не только 5-мин крипта | 6916 |
| 1. Прошли дешёвые отсечки | 941 из 6916 |
| 2. Прошли по полной истории | 3 + сегментом 21 из 941 |
| 3. Прошли реалистичный вход | 5 из 24 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3455 |
| history<90d | 1822 |
| open_now>10 | 1433 |
| top1_concentration | 1428 |
| entries>=0.90 | 1420 |
| closed<50 | 1415 |
| short_crypto | 594 |
| profit_from<0.10 | 520 |
| positions>5000 | 85 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 789 |
| t<2.0 | 780 |
| concurrency_p95>8 | 756 |
| unstable_halves | 564 |
| roi_copy<=0 | 342 |
| low_liquidity | 237 |
| both_sides | 191 |
| history<90d | 129 |
| hold<1h | 51 |
| entries>=0.90 | 45 |
| short_crypto | 21 |
| segment_only:t<2.0 | 21 |
| top1_concentration | 18 |
| segment_only:drawdown | 17 |
| closed<50 | 16 |
| sniping | 14 |
| segment_only:unstable_halves | 9 |
| profit_from<0.10 | 7 |
| segment_only:roi_copy<=0 | 4 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 17 |
| edge_decays_with_delay | 2 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xaa903818f3f2d6fb6790cc55672bb99ab734c709` | Giannis34x | Sports | 0.1136 | 2.01 | 0.0987 | 0.1069 | 0.1165 | 7.0 | 2.26 | н/д | Sports / price=0.50-0.70 (n=55, roi=+0.23) | Sports (n=139, roi=+0.11) |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | Esports | 0.155 | 1.75 | 0.0798 | 0.0772 | 0.169 | 3.0 | 2.34 | н/д | Esports / Esports / live (n=94, roi=+0.29) | Esports / Esports / Counter Strike (n=85, roi=+0.27) | Esports (n=107, roi=+0.24) | Esports / Esports (n=107, roi=+0.24) | Esports / price=0.30-0.50 (n=42, roi=+0.35) | Esports / Esports / price=0.30-0.50 (n=42, roi=+0.35) |
| `0x310579303783d1b3c2b33cd28d83af946e082e7e` |  | Esports | 0.1166 | 1.61 | 0.0654 | 0.0691 | 0.1571 | 4.0 | 4.92 | 0.0 | Sports / Soccer (n=34, roi=+0.28) |
| `0xcb7ff0ad390ca732ff9d54f5f6da58888046824b` | silentvector10 | Sports | 0.1054 | 1.28 | 0.0457 | 0.0617 | 0.1258 | 6.0 | 4.66 | н/д | Sports / price=0.50-0.70 (n=70, roi=+0.18) | Sports / American Football / type=moneyline (n=30, roi=+0.26) |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | Sports | 0.0551 | 1.17 | 0.0297 | 0.0463 | 0.1268 | 6.0 | 4.24 | 0.0 | Sports / price=0.50-0.70 (n=197, roi=+0.14) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | 0.155 | Esports / Esports / live (n=94, roi=+0.29) | Esports / Esports / Counter Strike (n=85, roi=+0.27) | Esports (n=107, roi=+0.24) | Esports / Esports (n=107, roi=+0.24) | Esports / price=0.30-0.50 (n=42, roi=+0.35) | Esports / Esports / price=0.30-0.50 (n=42, roi=+0.35) | segment_only:t<2.0 |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0769 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1238 | Sports / Soccer / price=0.50-0.70 (n=83, roi=+0.29) | Sports / price=0.50-0.70 (n=125, roi=+0.21) | Sports / Soccer (n=160, roi=+0.18) | Sports / Soccer / type=moneyline (n=41, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown |
| `0x310579303783d1b3c2b33cd28d83af946e082e7e` |  | 0.1166 | Sports / Soccer (n=34, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown |
| `0xcb7ff0ad390ca732ff9d54f5f6da58888046824b` | silentvector10 | 0.1054 | Sports / price=0.50-0.70 (n=70, roi=+0.18) | Sports / American Football / type=moneyline (n=30, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.0268 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0289 | Sports / Baseball / type=moneyline (n=40, roi=+0.26) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | 0.0551 | Sports / price=0.50-0.70 (n=197, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0178 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0088 | Esports / price=0.50-0.70 (n=106, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=106, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd16201ba67a40915b3176272911b9e44aba30d24` | 0xD16201ba67A40915b3176272911b9e44aBa30d24-1763774387576 | 0.1056 | Sports / price=0.30-0.50 (n=36, roi=+0.31) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0737 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x0dbe4798a1719b1fc08cd3acc2369dd77c069013` | brussssss | 0.0068 | Sports / price=0.50-0.70 (n=178, roi=+0.11) | Sports / Soccer / price=0.50-0.70 (n=175, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3a4f2d28f884a5d7bfab73956792bc1c931ac4f2` | arunannaveni | 0.0068 | Sports / Soccer / price=0.30-0.50 (n=43, roi=+0.42) | Sports / Soccer / live (n=70, roi=+0.29) | Sports / Soccer / type=binary (n=85, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x670d76669e567a24a9876f92310436d029020825` | ebglyss | 0.0319 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.25) | Sports / price=0.50-0.70 (n=54, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x049acd80fa3dbc98c2edf8b56202ce3a4c22f9d6` | ZKS009 | 0.0804 | Politics / price=0.70-0.90 (n=33, roi=+0.10) | Politics / Tweet Markets / price=0.70-0.90 (n=33, roi=+0.10) | segment_only:t<2.0 |
| `0xeead01aae45ba3f13f30d4bad3d0139570923a29` | ZKS008 | 0.0596 | Politics / price=0.70-0.90 (n=32, roi=+0.08) | Politics / Tweet Markets / price=0.70-0.90 (n=32, roi=+0.08) | segment_only:t<2.0 |
| `0x43fe17cf68eb58be1d40514be0e52674b71d26ee` | 0x43fE17Cf68EB58BE1d40514Be0e52674B71d26eE-1768993726139 | 0.0538 | Sports / Cricket / price=0.50-0.70 (n=148, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.0994 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x7ce336595687024c9ebf620f2dcb3b71269b1689` | 0x7Ce336595687024C9ebF620F2dCb3b71269B1689-1774766944047 | 0.0933 | Sports / Other sport / live (n=733, roi=+0.16) | Sports / Other sport / Hong Kong Daily Weather (n=474, roi=+0.20) | Sports / Other sport / type=binary (n=834, roi=+0.14) | Sports / Other sport (n=838, roi=+0.14) | Sports / Other sport / price=0.10-0.30 (n=350, roi=+0.21) | Sports / price=0.10-0.30 (n=366, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0xbb360c54a7f8135407954450592f47d6bc940d51` | PiThree14 | 0.2314 | Sports / price=0.00-0.10 (n=44, roi=+1.85) | Sports / Other sport / Elon Tweets (n=112, roi=+0.81) | Sports (n=221, roi=+0.57) | Sports / Other sport (n=130, roi=+0.70) | Sports / Other sport / type=binary (n=130, roi=+0.70) | Sports / price=0.50-0.70 (n=44, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 892 | 0.3323 | 0.2461 | 10.0 | 0.744 | 8.0 | 1.05 | 33916 | delayed_roi<=0 |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 534 | 0.1959 | 0.1067 | 5.64 | 0.532 | 6.0 | 6.12 | 361019 | delayed_roi<=0 |
| `0xaa903818f3f2d6fb6790cc55672bb99ab734c709` | Giannis34x | Sports | 139 | 0.1136 | 0.1132 | 2.01 | 0.748 | 7.0 | 2.26 | 582281 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 210 | 13.2015 | 12.1742 | 5.88 | 0.219 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8889 | 5.01 | 0.351 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 822 | 2.9553 | 2.9071 | 2.23 | 0.225 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 823 | 2.9511 | 2.9031 | 2.23 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2186 | 3.53 | 0.794 |
| `0xb595d09c…` | Sports / price=0.00-0.10 | 34 | 20.3154 | 12.8423 | 2.83 | 0.265 |
| `0x86c878cd…` | Sports / Tennis / live | 747 | 2.5253 | 2.4956 | 4.63 | 0.659 |
| `0x86c878cd…` | Sports | 2212 | 1.432 | 1.4316 | 6.26 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 825 | 2.3515 | 2.3287 | 4.75 | 0.646 |
| `0x9b979a06…` | Sports / price=0.00-0.10 | 50 | 11.0001 | 7.9327 | 2.53 | 0.32 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 83 | 7.0292 | 5.9335 | 2.58 | 0.133 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.4019 | 2.85 | 0.269 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3172 | 7.86 | 0.681 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9822 | 8.06 | 0.75 |
| `0x1941ca5d…` | Sports / Other sport | 2852 | 0.9459 | 0.9458 | 2.47 | 0.529 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2852 | 0.9459 | 0.9458 | 2.47 | 0.529 |
| `0x1941ca5d…` | Sports | 2854 | 0.9453 | 0.9452 | 2.47 | 0.529 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 64 | 7.9495 | 6.2016 | 2.74 | 0.219 |
| `0xef185339…` | Sports | 3794 | 0.7321 | 0.7321 | 22.59 | 0.695 |
| `0x86c878cd…` | Sports / Tennis / WTA | 196 | 3.3869 | 3.2017 | 2.73 | 0.663 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9297 | 2.43 | 0.3 |
| `0xf5fe759c…` | Sports / Tennis / pre | 125 | 4.0799 | 3.8687 | 6.85 | 0.752 |
| `0x13997bdb…` | Sports | 4030 | 0.6798 | 0.6798 | 22.27 | 0.687 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7988 | 6.78 | 0.656 |
| `0xd60c6fa3…` | Sports | 3527 | 0.6909 | 0.6909 | 20.8 | 0.69 |
| `0xf5fe759c…` | Sports / Tennis | 160 | 3.166 | 3.0974 | 6.47 | 0.675 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1032 | 1.1989 | 1.1901 | 16.92 | 0.597 |
| `0x86c878cd…` | Sports / Tennis / ATP | 393 | 1.9302 | 1.9039 | 3.1 | 0.628 |
| `0xf5fe759c…` | Sports | 210 | 2.5652 | 2.5638 | 6.56 | 0.667 |
| `0xb569eb4f…` | Esports | 3394 | 0.6274 | 0.6271 | 2.04 | 0.923 |
| `0xb569eb4f…` | Esports / Esports | 3394 | 0.6274 | 0.6271 | 2.04 | 0.923 |
| `0x13997bdb…` | Sports / Soccer | 2809 | 0.6866 | 0.6865 | 18.29 | 0.691 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 885 | 1.2318 | 1.2198 | 15.93 | 0.595 |
| `0x13997bdb…` | Sports / Soccer / live | 2767 | 0.6898 | 0.6898 | 18.14 | 0.691 |
| `0xef185339…` | Sports / Soccer | 2559 | 0.7062 | 0.7064 | 18.77 | 0.693 |
| `0xef185339…` | Sports / Soccer / live | 2525 | 0.7065 | 0.7067 | 18.57 | 0.691 |
| `0x13997bdb…` | Sports / price=0.10-0.30 | 1118 | 1.0378 | 1.0315 | 15.96 | 0.564 |
| `0xf5fe759c…` | Sports / Tennis / ATP | 91 | 3.8374 | 3.6051 | 6.47 | 0.758 |
| `0x1941ca5d…` | Sports / Other sport / live | 2159 | 0.7315 | 0.7333 | 3.6 | 0.572 |
| `0xd60c6fa3…` | Sports / Soccer | 2366 | 0.6854 | 0.6854 | 16.35 | 0.69 |
| `0xd60c6fa3…` | Sports / Soccer / live | 2323 | 0.6866 | 0.6866 | 16.14 | 0.688 |
| `0xef185339…` | Sports / Soccer / price=0.10-0.30 | 672 | 1.2254 | 1.2111 | 13.91 | 0.607 |
| `0xbfeceb41…` | Sports / price=0.00-0.10 | 372 | 1.6073 | 1.549 | 2.29 | 0.075 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8096 | 2.81 | 0.664 |
| `0xd60c6fa3…` | Sports / Soccer / price=0.10-0.30 | 582 | 1.2352 | 1.2171 | 13.1 | 0.608 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 134 | 2.8293 | 2.4933 | 2.48 | 0.351 |
| `0x86c878cd…` | Sports / Tennis / ITF | 179 | 2.2427 | 2.1566 | 2.04 | 0.659 |
| `0x13997bdb…` | Sports / Soccer / price=0.10-0.30 | 770 | 1.0439 | 1.0346 | 13.29 | 0.565 |
| `0xef185339…` | Sports / price=0.00-0.10 | 230 | 1.9601 | 1.8618 | 5.25 | 0.487 |
| `0x86c878cd…` | Sports / Other sport / live | 148 | 2.4159 | 2.2934 | 2.11 | 0.75 |
| `0xaa930fdc…` | Sports / price=0.00-0.10 | 800 | 0.9922 | 0.9761 | 2.28 | 0.099 |
| `0xaa930fdc…` | Sports / Other sport / price=0.00-0.10 | 789 | 0.9985 | 0.982 | 2.27 | 0.098 |
| `0xef185339…` | Sports / Other sport / live | 1228 | 0.7806 | 0.7798 | 12.59 | 0.697 |
| `0xef185339…` | Sports / Other sport | 1229 | 0.7791 | 0.7784 | 12.57 | 0.697 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 182 | 2.1583 | 1.9607 | 2.4 | 0.126 |
| `0x41558102…` | Sports / price=0.10-0.30 | 326 | 1.5265 | 1.457 | 11.73 | 0.601 |
| `0x86c878cd…` | Sports / Other sport | 190 | 1.9502 | 1.8965 | 2.18 | 0.747 |
| `0x13997bdb…` | Sports / price=0.00-0.10 | 269 | 1.6046 | 1.5406 | 4.93 | 0.45 |
| `0x86c878cd…` | Sports / Soccer | 899 | 0.8285 | 0.8407 | 3.17 | 0.628 |
| `0x41558102…` | Sports | 5988 | 0.3248 | 0.3248 | 10.27 | 0.851 |
