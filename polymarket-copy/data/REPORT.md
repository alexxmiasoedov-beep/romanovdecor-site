# Отчёт воронки, 2026-10-06 06:40 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 18332 |
| 0. Из них не только 5-мин крипта | 16614 |
| 1. Прошли дешёвые отсечки | 2009 из 16614 |
| 2. Прошли по полной истории | 7 + сегментом 40 из 2009 |
| 3. Прошли реалистичный вход | 16 из 47 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 8721 |
| history<90d | 4660 |
| closed<50 | 4354 |
| top1_concentration | 3832 |
| open_now>10 | 3150 |
| entries>=0.90 | 2993 |
| short_crypto | 1460 |
| profit_from<0.10 | 1117 |
| positions>5000 | 133 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 1683 |
| drawdown | 1653 |
| concurrency_p95>8 | 1610 |
| unstable_halves | 1246 |
| roi_copy<=0 | 762 |
| low_liquidity | 399 |
| both_sides | 334 |
| history<90d | 198 |
| hold<1h | 102 |
| entries>=0.90 | 79 |
| top1_concentration | 55 |
| short_crypto | 50 |
| segment_only:t<2.0 | 39 |
| closed<50 | 37 |
| sniping | 33 |
| segment_only:drawdown | 27 |
| profit_from<0.10 | 17 |
| segment_only:unstable_halves | 15 |
| segment_only:roi_copy<=0 | 5 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 23 |
| edge_decays_with_delay | 8 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x3c14d6729861ea0dd9a7cd246a79280a0ceca20a` | KVBA7 | Sports | 0.116 | 2.75 | 0.1235 | 0.1329 | 0.108 | 6.0 | 16.4 | 0.0003 | Sports (n=80, roi=+0.18) | Sports / Other sport (n=42, roi=+0.19) | Sports / Other sport / type=binary (n=42, roi=+0.19) | Sports / Other sport / live (n=42, roi=+0.19) | Sports / Soccer (n=36, roi=+0.17) | Sports / price=0.70-0.90 (n=46, roi=+0.14) |
| `0xe5130df60c5c0482abcbf470bf1ea82d489c5d90` | jjjkl | Sports | 0.1044 | 2.96 | 0.1045 | 0.1048 | 0.0949 | 3.0 | 15.47 | 0.0 | Sports (n=36, roi=+0.14) | Sports / Soccer (n=33, roi=+0.14) | Sports / Soccer / FIFA World Cup (n=33, roi=+0.14) | Sports / Soccer / pre (n=30, roi=+0.13) |
| `0xb2eb870848b24fc746b9171988106014b4975311` | 0xb2Eb870848b24Fc746b9171988106014B4975311-1777056035574 | Sports | 0.2171 | 1.78 | 0.1406 | 0.1626 | 0.2307 | 5.0 | 5.59 | 0.0 | Sports / Soccer / pre (n=56, roi=+0.29) | Sports / Soccer / type=moneyline (n=63, roi=+0.27) |
| `0x63808949537e0a49ada6e63a9ef54a3334f7e633` |  | Sports | 0.0803 | 2.2 | 0.0654 | 0.0743 | 0.0772 | 5.0 | 2.99 | н/д | Sports / Soccer / price=0.50-0.70 (n=39, roi=+0.26) | Sports / price=0.50-0.70 (n=42, roi=+0.22) | Sports / Soccer (n=163, roi=+0.09) | Sports / Soccer / type=moneyline (n=81, roi=+0.13) | Sports (n=197, roi=+0.08) | Sports / Soccer / pre (n=117, roi=+0.10) |
| `0x149a9ec31ae097faa33b2f2ae8df659889c149d0` | web3Boss | Esports | 0.0808 | 2.72 | 0.1148 | 0.1389 | 0.1752 | 3.0 | 2.32 | н/д | Esports / Esports / type=child_moneyline (n=408, roi=+0.11) | Esports / Esports / live (n=494, roi=+0.09) | Esports / Esports (n=496, roi=+0.09) | Esports / Esports / Dota 2 (n=496, roi=+0.09) | Esports (n=498, roi=+0.09) | Esports / price=0.30-0.50 (n=36, roi=+0.31) |
| `0xf13dd60c30d95129690fc58e8e3784110167afc3` | EdgeBot1 | Sports | 0.13 | 1.95 | 0.0431 | 0.0695 | 0.0871 | 8.0 | 3.51 | 0.0 | Sports / Soccer (n=117, roi=+0.17) | Sports / Soccer / pre (n=34, roi=+0.25) |
| `0x8d8a927fb3657b7a6abfe18a7a12b61bcb9d7a39` | 0x8d8A927Fb3657B7a6AbfE18A7A12b61BcB9D7A39-1773773427211 | Sports | 0.0709 | 1.51 | 0.0638 | 0.0693 | 0.0638 | 5.0 | 6.92 | н/д | Sports / Soccer / FIFA World Cup (n=38, roi=+0.17) | Sports / Soccer (n=112, roi=+0.09) | Sports / price=0.70-0.90 (n=81, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=76, roi=+0.09) |
| `0xde0e338ed6cb3a7bf316d33b3c7b3549c8d1e5bc` | kicaumania88 | Sports | 0.3413 | 1.56 | 0.0744 | 0.0847 | 0.4117 | 4.0 | 6.63 | 0.0 | Sports / price=0.50-0.70 (n=36, roi=+0.28) |
| `0x084fccc33d7f6dec43ec6565d095c07e76eb737e` |  | Sports | 0.0751 | 1.59 | 0.0579 | 0.0647 | 0.0715 | 3.0 | 8.2 | 0.0 | Sports (n=61, roi=+0.10) | Sports / Soccer (n=40, roi=+0.11) |
| `0x09dc5dc0b57240dc4c6dea7bcff286ef13dad0a4` | cdsyiede | Sports | 0.0759 | 1.17 | 0.0641 | 0.0719 | 0.0577 | 8.0 | 18.51 | 0.0 | Sports / price=0.50-0.70 (n=113, roi=+0.16) |
| `0x6f5ce61d6f49ad5d6f8a93a28af2807fe083bf79` | 0x6f5Ce61D6F49ad5D6F8a93A28Af2807fE083bF79-1782228615289 | Sports | 0.0897 | 1.14 | 0.033 | 0.035 | 0.1146 | 6.0 | 5.42 | 0.0 | Sports / price=0.50-0.70 (n=36, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=36, roi=+0.21) |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | Esports | -0.0323 | -0.65 | 0.0493 | 0.0584 | 0.1967 | 5.0 | 5.86 | 0.0114 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | Sports | 0.0269 | 1.47 | 0.061 | 0.0735 | 0.0966 | 8.0 | 3.16 | 0.022 | Esports / price=0.50-0.70 (n=52, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=52, roi=+0.20) | Esports / Esports / Counter Strike (n=151, roi=+0.10) |
| `0x26f65d469bd2820cf752b8466d5f25cf4b559068` | Jtcr | Sports | 0.0814 | 1.02 | 0.04 | 0.0442 | 0.0661 | 4.0 | 4.7 | 0.0 | Sports / price=0.50-0.70 (n=61, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=61, roi=+0.18) |
| `0x1073cb696e3265bdabc8bafbfd818f0cd3f79b1f` | 0x1073Cb696E3265bDABC8BafbFD818F0Cd3f79b1f-1774760477935 | Esports | 0.0613 | 0.84 | 0.0337 | 0.0347 | 0.1022 | 5.0 | 15.28 | 0.0 | Esports / Esports / type=moneyline (n=76, roi=+0.15) | Esports / Esports / pre (n=72, roi=+0.14) |
| `0xc3f119fe0be9b7c3631332b2bc0ead67311e8391` | whataretheoddss | Esports | 0.0318 | 1.29 | 0.0401 | 0.0532 | 0.1489 | 8.0 | 2.77 | н/д | Esports / price=0.50-0.70 (n=101, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=101, roi=+0.11) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xb2eb870848b24fc746b9171988106014b4975311` | 0xb2Eb870848b24Fc746b9171988106014B4975311-1777056035574 | 0.2171 | Sports / Soccer / pre (n=56, roi=+0.29) | Sports / Soccer / type=moneyline (n=63, roi=+0.27) | segment_only:t<2.0 |
| `0xf13dd60c30d95129690fc58e8e3784110167afc3` | EdgeBot1 | 0.13 | Sports / Soccer (n=117, roi=+0.17) | Sports / Soccer / pre (n=34, roi=+0.25) | segment_only:t<2.0 |
| `0x8d8a927fb3657b7a6abfe18a7a12b61bcb9d7a39` | 0x8d8A927Fb3657B7a6AbfE18A7A12b61BcB9D7A39-1773773427211 | 0.0709 | Sports / Soccer / FIFA World Cup (n=38, roi=+0.17) | Sports / Soccer (n=112, roi=+0.09) | Sports / price=0.70-0.90 (n=81, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=76, roi=+0.09) | segment_only:t<2.0 |
| `0x084fccc33d7f6dec43ec6565d095c07e76eb737e` |  | 0.0751 | Sports (n=61, roi=+0.10) | Sports / Soccer (n=40, roi=+0.11) | segment_only:t<2.0 |
| `0xde0e338ed6cb3a7bf316d33b3c7b3549c8d1e5bc` | kicaumania88 | 0.3413 | Sports / price=0.50-0.70 (n=36, roi=+0.28) | segment_only:t<2.0 |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | 0.1097 | Esports / Esports / Counter Strike (n=118, roi=+0.22) | Esports / Esports / live (n=135, roi=+0.20) | Esports (n=149, roi=+0.17) | Esports / Esports (n=149, roi=+0.17) | segment_only:t<2.0 |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.0582 | Sports / price=0.70-0.90 (n=80, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcb7ff0ad390ca732ff9d54f5f6da58888046824b` | silentvector10 | 0.1026 | Sports / price=0.50-0.70 (n=74, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x09dc5dc0b57240dc4c6dea7bcff286ef13dad0a4` | cdsyiede | 0.0759 | Sports / price=0.50-0.70 (n=113, roi=+0.16) | segment_only:t<2.0 |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0993 | Sports / Soccer / price=0.50-0.70 (n=91, roi=+0.26) | Sports / Soccer / type=moneyline (n=47, roi=+0.27) | Sports / Soccer / pre (n=97, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.0323 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6f5ce61d6f49ad5d6f8a93a28af2807fe083bf79` | 0x6f5Ce61D6F49ad5D6F8a93A28Af2807fE083bF79-1782228615289 | 0.0897 | Sports / price=0.50-0.70 (n=36, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=36, roi=+0.21) | segment_only:t<2.0 |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0545 | Esports / price=0.50-0.70 (n=35, roi=+0.23) | Esports / Esports / price=0.50-0.70 (n=35, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | 0.0269 | Esports / price=0.50-0.70 (n=52, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=52, roi=+0.20) | Esports / Esports / Counter Strike (n=151, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x26f65d469bd2820cf752b8466d5f25cf4b559068` | Jtcr | 0.0814 | Sports / price=0.50-0.70 (n=61, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=61, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x89879980a13fb82269cc489154fafbad8241d5b9` | soocas | 0.0541 | Esports / price=0.70-0.90 (n=42, roi=+0.11) | Esports / Esports / price=0.70-0.90 (n=42, roi=+0.11) | segment_only:t<2.0 |
| `0xc3f119fe0be9b7c3631332b2bc0ead67311e8391` | whataretheoddss | 0.0318 | Esports / price=0.50-0.70 (n=101, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=101, roi=+0.11) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x1073cb696e3265bdabc8bafbfd818f0cd3f79b1f` | 0x1073Cb696E3265bDABC8BafbFD818F0Cd3f79b1f-1774760477935 | 0.0613 | Esports / Esports / type=moneyline (n=76, roi=+0.15) | Esports / Esports / pre (n=72, roi=+0.14) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0213 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | 0.0091 | Sports / Other sport / price=0.70-0.90 (n=77, roi=+0.08) | Sports / Other sport (n=123, roi=+0.06) | Sports / Other sport / type=totals (n=36, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x20255f1ed1e9db14d2c663b588cbcc41306113c0` | 182837282 | -0.0117 | Sports / Tennis / price=0.70-0.90 (n=58, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0347 | Sports / price=0.30-0.50 (n=85, roi=+0.25) | Sports / Tennis / price=0.30-0.50 (n=36, roi=+0.30) | Sports (n=401, roi=+0.08) | Sports / Basketball / type=moneyline (n=33, roi=+0.21) | Sports / Basketball (n=36, roi=+0.17) | Sports / Basketball / live (n=31, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0358 | Sports / American Football (n=154, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0x0dbe4798a1719b1fc08cd3acc2369dd77c069013` | brussssss | 0.0066 | Sports / price=0.50-0.70 (n=193, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.033 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | 0.0363 | Sports / Soccer (n=34, roi=+0.25) | Sports / Soccer / pre (n=34, roi=+0.25) | segment_only:t<2.0 |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | 0.0753 | Sports / Tennis / price=0.50-0.70 (n=49, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown |
| `0x51c7d30511ed096b39a9392bad97e0dc76c298aa` | Chopperyyy | 0.0218 | Esports / Esports / Counter Strike (n=299, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0x670d76669e567a24a9876f92310436d029020825` | ebglyss | 0.0336 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0375 | Esports / price=0.50-0.70 (n=43, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=43, roi=+0.18) | segment_only:t<2.0 |
| `0x7714c16f86bcfdba47bfcb161dc39a2a1ff2b814` | llllllIIIIIIlIllllllIIIIIIlIllllllIIIIIIlI | 0.0375 | Sports / Soccer (n=62, roi=+0.35) | Sports (n=95, roi=+0.24) | Sports / Soccer / live (n=36, roi=+0.35) | Sports / Soccer / type=moneyline (n=34, roi=+0.31) | Sports / Soccer / price=0.50-0.70 (n=31, roi=+0.23) | Sports / price=0.50-0.70 (n=33, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0521 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x2d51fbb5706bfe7ab7d21853fc054f0a17d4d971` | fFffffFFFfFFFfFFFFfjjh | 0.0514 | Esports / price=0.30-0.50 (n=239, roi=+0.22) | Esports / Esports / price=0.30-0.50 (n=239, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x82882d761b0d7f18b2cc286117d10cd8a15a5519` | Sugarina | 0.1133 | Sports / Other sport / price=0.70-0.90 (n=43, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x791e45264c99eecaeb095caea9ad863740d29bda` | easymoneysniperzz | 0.0461 | Esports / Esports / type=map_handicap (n=131, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0xc406a11fccbaf0df26f380f593ab08e2a70b4deb` | Galaktor | 0.1483 | Sports / Basketball / price=0.10-0.30 (n=164, roi=+0.35) | segment_only:t<2.0;segment_only:drawdown |
| `0xe23cd5fb6bee7b1c9f60f5d9969ac7ba52cc5ae7` | apprentice15 | 0.2202 | Sports / Soccer (n=442, roi=+0.25) | Sports / Soccer / live (n=432, roi=+0.25) | Sports (n=544, roi=+0.22) | Sports / price=0.10-0.30 (n=115, roi=+0.41) | Sports / Soccer / price=0.30-0.50 (n=149, roi=+0.18) | segment_only:drawdown |
| `0x7ce336595687024c9ebf620f2dcb3b71269b1689` | 0x7Ce336595687024C9ebF620F2dCb3b71269B1689-1774766944047 | 0.0878 | Sports / Other sport / live (n=739, roi=+0.15) | Sports / Other sport / Hong Kong Daily Weather (n=479, roi=+0.19) | Sports / Other sport / type=binary (n=841, roi=+0.13) | Sports / Other sport / price=0.10-0.30 (n=352, roi=+0.20) | Sports / Other sport (n=845, roi=+0.13) | Sports / price=0.10-0.30 (n=368, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0xbb360c54a7f8135407954450592f47d6bc940d51` | PiThree14 | 0.2215 | Sports / price=0.00-0.10 (n=48, roi=+1.77) | Sports / Other sport / Elon Tweets (n=120, roi=+0.77) | Sports (n=233, roi=+0.54) | Sports / price=0.50-0.70 (n=45, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 960 | 0.3421 | 0.2518 | 10.6 | 0.746 | 8.0 | 1.16 | 33055 | delayed_roi<=0 |
| `0x3c14d6729861ea0dd9a7cd246a79280a0ceca20a` | KVBA7 | Sports | 107 | 0.116 | 0.1328 | 2.75 | 0.822 | 6.0 | 16.4 | 177313 | прошёл |
| `0xe5130df60c5c0482abcbf470bf1ea82d489c5d90` | jjjkl | Sports | 68 | 0.1044 | 0.113 | 2.96 | 0.794 | 3.0 | 15.47 | 3289605 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 523 | 0.1905 | 0.0993 | 5.43 | 0.533 | 5.0 | 5.96 | 354624 | delayed_roi<=0 |
| `0x63808949537e0a49ada6e63a9ef54a3334f7e633` |  | Sports | 198 | 0.0803 | 0.0995 | 2.2 | 0.813 | 5.0 | 2.99 | 705471 | прошёл |
| `0x149a9ec31ae097faa33b2f2ae8df659889c149d0` | web3Boss | Esports | 551 | 0.0808 | 0.0727 | 2.72 | 0.726 | 3.0 | 2.32 | 185900 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 706 | 0.1221 | 0.0606 | 3.53 | 0.727 | 8.0 | 2.86 | 392030 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 213 | 13.1189 | 12.1112 | 5.93 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8874 | 5.01 | 0.351 |
| `0x465ace6e…` | Sports / price=0.00-0.10 | 50 | 26.926 | 20.4687 | 5.14 | 0.58 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1052 | 4.18 | 0.329 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.709 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 129 | 9.6001 | 8.4599 | 3.79 | 0.178 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 129 | 9.6001 | 8.4599 | 3.79 | 0.178 |
| `0x465ace6e…` | Sports / Tennis | 133 | 8.0667 | 7.5776 | 4.0 | 0.722 |
| `0x465ace6e…` | Sports | 309 | 4.9858 | 4.9457 | 4.95 | 0.718 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 819 | 2.9625 | 2.9138 | 2.23 | 0.226 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 820 | 2.9582 | 2.9097 | 2.23 | 0.226 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2176 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 244 | 5.617 | 5.2753 | 3.99 | 0.139 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4836 | 3.61 | 0.17 |
| `0x465ace6e…` | Sports / Tennis / WTA | 36 | 17.6494 | 12.8908 | 2.99 | 0.778 |
| `0x86c878cd…` | Sports / Tennis / live | 755 | 2.4997 | 2.4708 | 4.63 | 0.661 |
| `0x465ace6e…` | Sports / Tennis / live | 55 | 10.8553 | 9.114 | 2.79 | 0.818 |
| `0x86c878cd…` | Sports | 2249 | 1.4237 | 1.4233 | 6.32 | 0.637 |
| `0x86c878cd…` | Sports / Tennis | 834 | 2.3272 | 2.305 | 4.75 | 0.649 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8634 | 2.77 | 0.125 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8634 | 2.77 | 0.125 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6279 | 2.81 | 0.636 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 84 | 6.9336 | 5.8654 | 2.57 | 0.131 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3948 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.745 | 3.14 | 0.246 |
| `0xe9f5c75e…` | Sports / Basketball / live | 461 | 2.5117 | 2.442 | 4.17 | 0.618 |
| `0x465ace6e…` | Sports / Tennis / pre | 78 | 6.1004 | 5.7381 | 2.95 | 0.654 |
| `0x1941ca5d…` | Sports / Other sport | 2881 | 0.9374 | 0.9372 | 2.47 | 0.538 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2881 | 0.9374 | 0.9372 | 2.47 | 0.538 |
| `0x1941ca5d…` | Sports | 2883 | 0.9368 | 0.9367 | 2.47 | 0.538 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.9474 | 2.72 | 0.209 |
| `0x465ace6e…` | Sports / Tennis / ATP | 56 | 6.9698 | 6.2739 | 2.62 | 0.732 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.828 | 2.13 | 0.183 |
| `0xef185339…` | Sports | 3821 | 0.7303 | 0.7303 | 22.61 | 0.693 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1875 | 2.73 | 0.665 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9289 | 2.43 | 0.3 |
| `0x13997bdb…` | Sports | 4092 | 0.6758 | 0.6758 | 22.4 | 0.685 |
| `0xb209ec04…` | Sports | 1540 | 1.0653 | 1.0658 | 4.62 | 0.518 |
| `0xd60c6fa3…` | Sports | 3561 | 0.693 | 0.693 | 21.01 | 0.688 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1764 | 2.41 | 0.526 |
| `0xb209ec04…` | Esports / Esports / live | 950 | 1.3371 | 1.3323 | 3.77 | 0.507 |
| `0xb209ec04…` | Sports / Soccer | 888 | 1.3829 | 1.3768 | 4.01 | 0.511 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.6287 | 3.4 | 0.478 |
| `0xb209ec04…` | Esports | 1205 | 1.1605 | 1.1596 | 4.06 | 0.5 |
| `0xb209ec04…` | Esports / Esports | 1205 | 1.1605 | 1.1596 | 4.06 | 0.5 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 332 | 2.2888 | 2.2042 | 4.34 | 0.41 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 123 | 4.0143 | 3.5753 | 2.9 | 0.407 |
| `0xd970693a…` | Sports | 2410 | 0.8002 | 0.8002 | 10.28 | 0.664 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 380 | 2.09 | 2.0066 | 3.43 | 0.287 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 393 | 2.0491 | 1.9703 | 3.47 | 0.282 |
| `0xb209ec04…` | Esports / Esports / Valorant | 199 | 2.9053 | 2.741 | 2.41 | 0.482 |
| `0x4afbb658…` | Sports | 165 | 3.1706 | 3.0035 | 2.38 | 0.418 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 536 | 1.6895 | 1.6588 | 3.61 | 0.584 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1034 | 1.1993 | 1.1903 | 17.0 | 0.598 |
| `0x86c878cd…` | Sports / Tennis / ATP | 398 | 1.9064 | 1.8812 | 3.1 | 0.631 |
| `0xe9f5c75e…` | Sports / Basketball | 972 | 1.2084 | 1.2009 | 4.18 | 0.562 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 893 | 1.2527 | 1.2404 | 16.24 | 0.597 |
| `0x1985327e…` | Sports | 1305 | 1.0239 | 1.0239 | 2.66 | 0.718 |
| `0x13997bdb…` | Sports / Soccer | 2859 | 0.6845 | 0.6845 | 18.49 | 0.691 |
| `0x13997bdb…` | Sports / Soccer / live | 2817 | 0.6877 | 0.6876 | 18.34 | 0.69 |
