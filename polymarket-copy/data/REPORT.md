# Отчёт воронки, 2026-10-07 07:29 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 23849 |
| 0. Из них не только 5-мин крипта | 21366 |
| 1. Прошли дешёвые отсечки | 2845 из 21365 |
| 2. Прошли по полной истории | 9 + сегментом 69 из 2845 |
| 3. Прошли реалистичный вход | 35 из 78 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 11479 |
| history<90d | 6372 |
| closed<50 | 5207 |
| top1_concentration | 4342 |
| entries>=0.90 | 3751 |
| open_now>10 | 3260 |
| short_crypto | 1933 |
| profit_from<0.10 | 1205 |
| positions>5000 | 137 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 2439 |
| drawdown | 2349 |
| concurrency_p95>8 | 2216 |
| unstable_halves | 1772 |
| roi_copy<=0 | 1157 |
| low_liquidity | 509 |
| both_sides | 490 |
| history<90d | 274 |
| hold<1h | 154 |
| entries>=0.90 | 88 |
| top1_concentration | 76 |
| segment_only:t<2.0 | 65 |
| short_crypto | 63 |
| segment_only:drawdown | 52 |
| closed<50 | 51 |
| sniping | 38 |
| segment_only:unstable_halves | 32 |
| profit_from<0.10 | 22 |
| segment_only:roi_copy<=0 | 7 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 37 |
| edge_decays_with_delay | 6 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x52bf12a2afc2e161120563352faa8aa251c93e9f` | thparvej24 | Sports | 0.2588 | 2.43 | 0.1882 | 0.2218 | 0.2482 | 3.0 | 2.4 | н/д | Sports / Soccer / live (n=65, roi=+0.30) | Sports / Soccer (n=69, roi=+0.28) | Sports / Soccer / type=moneyline (n=69, roi=+0.28) | Sports (n=71, roi=+0.26) | Sports / price=0.50-0.70 (n=30, roi=+0.36) |
| `0x3c14d6729861ea0dd9a7cd246a79280a0ceca20a` | KVBA7 | Sports | 0.1141 | 2.75 | 0.1212 | 0.1304 | 0.0978 | 6.0 | 16.98 | 0.0116 | Sports (n=82, roi=+0.18) | Sports / Other sport (n=44, roi=+0.18) | Sports / Other sport / type=binary (n=44, roi=+0.18) | Sports / Other sport / live (n=44, roi=+0.18) | Sports / Soccer (n=36, roi=+0.17) | Sports / price=0.70-0.90 (n=47, roi=+0.14) |
| `0x52c1afbe1b05dce1cc2338bff041946a8e665f35` |  | Sports | 0.184 | 2.03 | 0.1599 | 0.1634 | 0.1872 | 3.0 | 13.03 | н/д | Sports (n=101, roi=+0.18) |
| `0x4a1b8e8d38aecdc9687bb0f601801d59fa44724f` | ox1star84 | Sports | 0.1397 | 2.25 | 0.1197 | 0.1343 | 0.0918 | 5.0 | 11.09 | 0.0 | Sports / price=0.50-0.70 (n=30, roi=+0.25) | Sports (n=100, roi=+0.13) | Sports / MMA/Boxing (n=92, roi=+0.14) | Sports / MMA/Boxing / price=0.70-0.90 (n=54, roi=+0.12) |
| `0x0f153384f580c28b1ebe1d02c1f7ee6f9af3633b` | Artur5 | Sports | 0.1249 | 2.07 | 0.1115 | 0.1199 | 0.1151 | 7.0 | 8.61 | н/д | Sports / Soccer / price=0.50-0.70 (n=49, roi=+0.30) | Sports / Soccer / pre (n=50, roi=+0.29) | Sports / Soccer (n=61, roi=+0.26) | Sports / price=0.50-0.70 (n=58, roi=+0.25) | Sports / Soccer / type=moneyline (n=51, roi=+0.25) | Sports (n=81, roi=+0.17) |
| `0x149a9ec31ae097faa33b2f2ae8df659889c149d0` | web3Boss | Esports | 0.0843 | 2.85 | 0.138 | 0.1604 | 0.1963 | 3.0 | 2.31 | н/д | Esports / Esports / type=child_moneyline (n=412, roi=+0.11) | Esports / Esports / live (n=498, roi=+0.10) | Esports / Esports (n=500, roi=+0.09) | Esports / Esports / Dota 2 (n=500, roi=+0.09) | Esports (n=502, roi=+0.09) | Esports / price=0.30-0.50 (n=36, roi=+0.31) |
| `0xf13dd60c30d95129690fc58e8e3784110167afc3` | EdgeBot1 | Sports | 0.1364 | 2.09 | 0.0579 | 0.0864 | 0.0988 | 8.0 | 3.47 | 0.0 | Sports / Soccer (n=121, roi=+0.18) | Sports (n=168, roi=+0.14) | Sports / Soccer / pre (n=34, roi=+0.26) |
| `0xc0d5e31d1a5e91dc36dfa5c3d4d184e2c5a6fefe` | ManiNTheMidddle | Esports | 0.1221 | 1.6 | 0.13 | 0.1503 | 0.1754 | 5.0 | 2.73 | н/д | Esports / price=0.30-0.50 (n=88, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=88, roi=+0.24) |
| `0x44d682939eb6a4a1349fa50411531876a6089858` | BobMcAdoo | Sports | 0.1536 | 1.62 | 0.0753 | 0.0812 | 0.1292 | 8.0 | 14.25 | н/д | Sports / Hockey (n=75, roi=+0.26) | Sports / Hockey / NHL 2026 (n=75, roi=+0.26) | Sports / Hockey / pre (n=75, roi=+0.26) |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | Sports | 0.0567 | 1.48 | 0.0715 | 0.0936 | 0.0585 | 5.0 | 3.35 | 0.0 | Sports / Soccer (n=63, roi=+0.08) | Sports / Soccer / pre (n=41, roi=+0.10) |
| `0xa6f3d2650a19386887ba4c17c672c2b0a84da946` |  | Esports | 0.0823 | 1.89 | 0.0579 | 0.0884 | 0.0829 | 5.0 | 2.07 | н/д | Sports / Soccer / type=moneyline (n=39, roi=+0.23) | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) |
| `0xde0e338ed6cb3a7bf316d33b3c7b3549c8d1e5bc` | kicaumania88 | Sports | 0.3403 | 1.57 | 0.0769 | 0.0872 | 0.4099 | 4.0 | 6.71 | 0.0223 | Sports / price=0.50-0.70 (n=36, roi=+0.28) |
| `0x3d0abd76643bf53273ea9ba421545b4b806db4e7` | CashCremator | Sports | 0.1202 | 0.96 | 0.0866 | 0.1071 | 0.0602 | 2.0 | 23.18 | н/д | Sports / price=0.30-0.50 (n=33, roi=+0.35) | Sports / Hockey / price=0.30-0.50 (n=32, roi=+0.34) |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | Esports | -0.0559 | -1.82 | 0.0067 | 0.0175 | 0.009 | 8.0 | 3.13 | н/д | Sports / price=0.70-0.90 (n=82, roi=+0.08) |
| `0x6f5ce61d6f49ad5d6f8a93a28af2807fe083bf79` | 0x6f5Ce61D6F49ad5D6F8a93A28Af2807fE083bF79-1782228615289 | Sports | 0.0971 | 1.24 | 0.0417 | 0.0493 | 0.1216 | 6.0 | 6.34 | н/д | Sports / price=0.50-0.70 (n=36, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=36, roi=+0.21) |
| `0xe645f56c0c355567c59ad3ba045568017b8101d3` |  | Sports | 0.0782 | 1.43 | 0.0536 | 0.0666 | 0.0624 | 5.0 | 4.67 | н/д | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.20) | Sports / price=0.50-0.70 (n=63, roi=+0.19) | Sports / Soccer / pre (n=102, roi=+0.14) |
| `0x346403e31069abc77d4341be9690b23def01890d` | PaDeH | Sports | 0.1337 | 1.04 | 0.0327 | 0.0473 | -0.0625 | 7.0 | 28.02 | 0.0129 | Sports / Other sport / price=0.10-0.30 (n=38, roi=+0.33) |
| `0x093506de4a173bd4ea393a7cf5393495df14d9ef` | xxyr | Esports | 0.0237 | 1.31 | 0.0388 | 0.0369 | 0.0293 | 5.0 | 2.34 | 0.0005 | Sports / price=0.70-0.90 (n=50, roi=+0.07) |
| `0x3e691e86aefed3e9181a76c714e0c81e9ec5074b` |  | Esports | 0.1397 | 2.12 | 0.1218 | 0.1198 | 0.2997 | 5.0 | 2.58 | н/д | Esports / Esports / type=child_moneyline (n=129, roi=+0.23) | Sports / Soccer / pre (n=94, roi=+0.24) |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | Sports | 0.1003 | 1.19 | 0.0228 | 0.0395 | 0.0909 | 4.0 | 4.37 | 0.0 | Sports / price=0.50-0.70 (n=51, roi=+0.17) | Sports / Soccer / price=0.50-0.70 (n=51, roi=+0.17) |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | Sports | 0.0275 | 1.51 | 0.0595 | 0.0675 | 0.0963 | 8.0 | 3.16 | 0.0003 | Esports / price=0.50-0.70 (n=55, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=55, roi=+0.19) | Esports / Esports / Counter Strike (n=156, roi=+0.10) |
| `0xe3015c631605e328b39f5888da942b3078ab9bd9` | Miami222 | Sports | 0.2064 | 1.16 | 0.042 | 0.0517 | 0.0947 | 6.0 | 19.0 | 0.002 | Sports / price=0.50-0.70 (n=33, roi=+0.27) |
| `0xfe233dda1ca840ca86808d6f43f54ea84ed85072` | Tom5737 | Sports | 0.1186 | 1.29 | 0.0336 | 0.0375 | 0.1022 | 6.0 | 9.76 | н/д | Sports / Soccer / type=totals (n=35, roi=+0.28) |
| `0xcfae0acbdaa00028945da2df935496d7d35074e3` | 0xcfae0acBdaa00028945Da2dF935496D7d35074E3-1776430522638 | Sports | 0.066 | 0.78 | 0.0599 | 0.2828 | 0.0335 | 5.0 | 5.44 | 0.0 | Sports (n=36, roi=+0.18) | Sports / Soccer (n=36, roi=+0.18) | Sports / Soccer / type=moneyline (n=35, roi=+0.19) | Sports / Soccer / pre (n=34, roi=+0.17) |
| `0x758f40d5c4a76350096f3deaa0d016ed52efdfb7` | 0nglee | Esports | 0.0189 | 0.79 | 0.0705 | 0.0709 | 0.076 | 7.0 | 2.92 | н/д | Sports / Soccer / type=moneyline (n=30, roi=+0.12) |
| `0xaa9737b3db5d88aefcee007717a7c00b0df48c9c` | 0xf2cbF139C52b66c568dA19EF028f085289597B0e-1777085067547 | Sports | 0.2068 | 1.38 | 0.0186 | 0.0753 | 0.2723 | 4.0 | 4.34 | н/д | Sports / Soccer (n=54, roi=+0.41) |
| `0xa70ff0f435600e9779627ff1b6906fcc1691143d` | 0xA70ff0F435600e9779627fF1b6906fCC1691143D-1775659489890 | Sports | 0.0578 | 1.06 | 0.0644 | 0.0747 | 0.0611 | 7.0 | 4.07 | н/д | Sports / price=0.50-0.70 (n=69, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=67, roi=+0.16) |
| `0x339a9ace6a1950797b8e0a50a125b5b4e23c6a00` | superlarry | Sports | 0.02 | 0.43 | 0.0401 | 0.0589 | 0.0292 | 5.0 | 5.92 | 0.0 | Sports / Tennis / pre (n=39, roi=+0.17) |
| `0xc406a11fccbaf0df26f380f593ab08e2a70b4deb` | Galaktor | Sports | 0.1668 | 1.32 | 0.0037 | -0.0151 | 0.1348 | 8.0 | 21.64 | 0.0 | Sports / Basketball / price=0.10-0.30 (n=165, roi=+0.36) | Sports / Basketball / pre (n=154, roi=+0.35) | Sports / price=0.10-0.30 (n=174, roi=+0.32) |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | Sports | 0.0815 | 1.12 | 0.0337 | 0.0437 | 0.0936 | 7.0 | 2.48 | 0.0 | Sports / Tennis / price=0.50-0.70 (n=49, roi=+0.19) |
| `0x1baea97d6fa6bd5b1cd1390d1339e748b7afae9f` | 0x1Baea97d6FA6bD5b1CD1390D1339e748b7AfAe9F-1771653872374 | Esports | 0.0028 | 0.08 | 0.0372 | 0.0574 | 0.0406 | 4.0 | 3.91 | 0.0 | Esports / Esports / pre (n=73, roi=+0.11) |
| `0x776713e6791578ffa93fb6cc81da941dd4334fb2` | 0x776713E6791578FFA93Fb6cc81da941dD4334fB2-1769702052456 | Esports | 0.0341 | 0.7 | 0.0468 | 0.0595 | 0.09 | 5.0 | 3.19 | н/д | Esports / Esports / type=moneyline (n=82, roi=+0.21) |
| `0x0dbe4798a1719b1fc08cd3acc2369dd77c069013` | brussssss | Sports | 0.0101 | 0.3 | 0.0767 | 0.1173 | 0.1906 | 8.0 | 3.42 | н/д | Sports / price=0.50-0.70 (n=196, roi=+0.11) |
| `0x2d51fbb5706bfe7ab7d21853fc054f0a17d4d971` | fFffffFFFfFFFfFFFFfjjh | Esports | 0.0507 | 1.52 | 0.0394 | 0.0111 | 0.0969 | 7.0 | 3.13 | 0.1499 | Esports / price=0.30-0.50 (n=241, roi=+0.22) | Esports / Esports / price=0.30-0.50 (n=241, roi=+0.22) |
| `0x791e45264c99eecaeb095caea9ad863740d29bda` | easymoneysniperzz | Esports | 0.0473 | 1.04 | 0.0365 | 0.0539 | 0.1675 | 5.0 | 5.13 | н/д | Esports / Esports / type=map_handicap (n=131, roi=+0.20) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xa6f3d2650a19386887ba4c17c672c2b0a84da946` |  | 0.0823 | Sports / Soccer / type=moneyline (n=39, roi=+0.23) | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0 |
| `0x44d682939eb6a4a1349fa50411531876a6089858` | BobMcAdoo | 0.1536 | Sports / Hockey (n=75, roi=+0.26) | Sports / Hockey / NHL 2026 (n=75, roi=+0.26) | Sports / Hockey / pre (n=75, roi=+0.26) | segment_only:t<2.0 |
| `0xc0d5e31d1a5e91dc36dfa5c3d4d184e2c5a6fefe` | ManiNTheMidddle | 0.1221 | Esports / price=0.30-0.50 (n=88, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=88, roi=+0.24) | segment_only:t<2.0 |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0691 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | 0.0567 | Sports / Soccer (n=63, roi=+0.08) | Sports / Soccer / pre (n=41, roi=+0.10) | segment_only:t<2.0 |
| `0xde0e338ed6cb3a7bf316d33b3c7b3549c8d1e5bc` | kicaumania88 | 0.3403 | Sports / price=0.50-0.70 (n=36, roi=+0.28) | segment_only:t<2.0 |
| `0x3d0abd76643bf53273ea9ba421545b4b806db4e7` | CashCremator | 0.1202 | Sports / price=0.30-0.50 (n=33, roi=+0.35) | Sports / Hockey / price=0.30-0.50 (n=32, roi=+0.34) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1747 | Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / type=child_moneyline (n=568, roi=+0.19) | Esports (n=659, roi=+0.17) | Esports / Esports (n=659, roi=+0.17) | Esports / Esports / Dota 2 (n=659, roi=+0.17) | segment_only:drawdown |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.0559 | Sports / price=0.70-0.90 (n=82, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1d3178edc0f3342b26e170897cbf9704900e2cbf` | Chrom | 0.1155 | Sports / Hockey (n=72, roi=+0.27) | Sports / Hockey / NHL 2026 (n=72, roi=+0.27) | Sports / Hockey / type=moneyline (n=72, roi=+0.27) | Sports / Hockey / pre (n=72, roi=+0.27) | Sports / price=0.50-0.70 (n=90, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown |
| `0x093506de4a173bd4ea393a7cf5393495df14d9ef` | xxyr | 0.0237 | Sports / price=0.70-0.90 (n=50, roi=+0.07) | segment_only:t<2.0 |
| `0xe645f56c0c355567c59ad3ba045568017b8101d3` |  | 0.0782 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.20) | Sports / price=0.50-0.70 (n=63, roi=+0.19) | Sports / Soccer / pre (n=102, roi=+0.14) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x6f5ce61d6f49ad5d6f8a93a28af2807fe083bf79` | 0x6f5Ce61D6F49ad5D6F8a93A28Af2807fE083bF79-1782228615289 | 0.0971 | Sports / price=0.50-0.70 (n=36, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=36, roi=+0.21) | segment_only:t<2.0 |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | 0.1003 | Sports / price=0.50-0.70 (n=51, roi=+0.17) | Sports / Soccer / price=0.50-0.70 (n=51, roi=+0.17) | segment_only:t<2.0 |
| `0x346403e31069abc77d4341be9690b23def01890d` | PaDeH | 0.1337 | Sports / Other sport / price=0.10-0.30 (n=38, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0x3e691e86aefed3e9181a76c714e0c81e9ec5074b` |  | 0.1397 | Esports / Esports / type=child_moneyline (n=129, roi=+0.23) | Sports / Soccer / pre (n=94, roi=+0.24) | segment_only:drawdown;segment_only:unstable_halves |
| `0x2da245862be758df3908195772b1b06ef4808c2b` | vitbash | 0.0433 | Sports (n=86, roi=+0.14) | Sports / Soccer / live (n=31, roi=+0.17) | segment_only:t<2.0 |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.0287 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe3015c631605e328b39f5888da942b3078ab9bd9` | Miami222 | 0.2064 | Sports / price=0.50-0.70 (n=33, roi=+0.27) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | 0.0275 | Esports / price=0.50-0.70 (n=55, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=55, roi=+0.19) | Esports / Esports / Counter Strike (n=156, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfe233dda1ca840ca86808d6f43f54ea84ed85072` | Tom5737 | 0.1186 | Sports / Soccer / type=totals (n=35, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0494 | Esports / price=0.50-0.70 (n=36, roi=+0.21) | Esports / Esports / price=0.50-0.70 (n=36, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xcfae0acbdaa00028945da2df935496d7d35074e3` | 0xcfae0acBdaa00028945Da2dF935496D7d35074E3-1776430522638 | 0.066 | Sports (n=36, roi=+0.18) | Sports / Soccer (n=36, roi=+0.18) | Sports / Soccer / type=moneyline (n=35, roi=+0.19) | Sports / Soccer / pre (n=34, roi=+0.17) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0214 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | 0.0098 | Sports / Other sport / price=0.70-0.90 (n=77, roi=+0.08) | Sports / Other sport (n=123, roi=+0.06) | Sports / Other sport / type=totals (n=36, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x758f40d5c4a76350096f3deaa0d016ed52efdfb7` | 0nglee | 0.0189 | Sports / Soccer / type=moneyline (n=30, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown |
| `0xdefdba677384e28a8c3e6e6fa6303a9e29193f9d` | chet1101 | 0.1064 | Esports / Esports / League of Legends (n=30, roi=+0.34) | segment_only:t<2.0 |
| `0xaa9737b3db5d88aefcee007717a7c00b0df48c9c` | 0xf2cbF139C52b66c568dA19EF028f085289597B0e-1777085067547 | 0.2068 | Sports / Soccer (n=54, roi=+0.41) | segment_only:t<2.0;segment_only:drawdown |
| `0xa538af775227c7add77418ba079ea3ae6a9212c3` | WinsonEnterpriseCorp | -0.0214 | Sports (n=58, roi=+0.19) | Sports / price=0.50-0.70 (n=35, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1073cb696e3265bdabc8bafbfd818f0cd3f79b1f` | 0x1073Cb696E3265bDABC8BafbFD818F0Cd3f79b1f-1774760477935 | 0.0488 | Esports / Esports / type=moneyline (n=80, roi=+0.14) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xa70ff0f435600e9779627ff1b6906fcc1691143d` | 0xA70ff0F435600e9779627fF1b6906fCC1691143D-1775659489890 | 0.0578 | Sports / price=0.50-0.70 (n=69, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=67, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0071 | Sports / Soccer / price=0.50-0.70 (n=53, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x06a0402a3b327f2eaec00400a72c6813a0395804` | JeanValjean7 | -0.0032 | Sports / Soccer / price=0.30-0.50 (n=135, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x339a9ace6a1950797b8e0a50a125b5b4e23c6a00` | superlarry | 0.02 | Sports / Tennis / pre (n=39, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0768 | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0032 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=138, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | 0.0815 | Sports / Tennis / price=0.50-0.70 (n=49, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown |
| `0x1baea97d6fa6bd5b1cd1390d1339e748b7afae9f` | 0x1Baea97d6FA6bD5b1CD1390D1339e748b7AfAe9F-1771653872374 | 0.0028 | Esports / Esports / pre (n=73, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0348 | Sports / price=0.30-0.50 (n=85, roi=+0.25) | Sports / Tennis / price=0.30-0.50 (n=36, roi=+0.30) | Sports (n=404, roi=+0.08) | Sports / Basketball / type=moneyline (n=33, roi=+0.21) | Sports / Basketball (n=36, roi=+0.17) | Sports / Basketball / live (n=31, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0052 | Sports / Soccer / pre (n=166, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=142, roi=+0.09) | Sports / price=0.70-0.90 (n=171, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 974 | 0.3514 | 0.2591 | 10.84 | 0.746 | 8.0 | 1.22 | 33055 | delayed_roi<=0 |
| `0x52bf12a2afc2e161120563352faa8aa251c93e9f` | thparvej24 | Sports | 71 | 0.2588 | 0.2296 | 2.43 | 0.563 | 3.0 | 2.4 | 1675935 | прошёл |
| `0x3c14d6729861ea0dd9a7cd246a79280a0ceca20a` | KVBA7 | Sports | 109 | 0.1141 | 0.1304 | 2.75 | 0.817 | 6.0 | 16.98 | 179410 | прошёл |
| `0x52c1afbe1b05dce1cc2338bff041946a8e665f35` |  | Sports | 101 | 0.184 | 0.1684 | 2.03 | 0.653 | 3.0 | 13.03 | 916080 | прошёл |
| `0x4a1b8e8d38aecdc9687bb0f601801d59fa44724f` | ox1star84 | Sports | 104 | 0.1397 | 0.136 | 2.25 | 0.808 | 5.0 | 11.09 | 280743 | прошёл |
| `0x0f153384f580c28b1ebe1d02c1f7ee6f9af3633b` | Artur5 | Sports | 124 | 0.1249 | 0.1218 | 2.07 | 0.782 | 7.0 | 8.61 | 235087 | прошёл |
| `0x149a9ec31ae097faa33b2f2ae8df659889c149d0` | web3Boss | Esports | 555 | 0.0843 | 0.0766 | 2.85 | 0.728 | 3.0 | 2.31 | 188289 | прошёл |
| `0xf13dd60c30d95129690fc58e8e3784110167afc3` | EdgeBot1 | Sports | 168 | 0.1364 | 0.1026 | 2.09 | 0.667 | 8.0 | 3.47 | 2082228 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 710 | 0.1191 | 0.0577 | 3.45 | 0.725 | 8.0 | 2.85 | 392030 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 213 | 13.1189 | 12.111 | 5.93 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8868 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 97 | 15.2607 | 13.1736 | 4.13 | 0.186 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1052 | 4.18 | 0.329 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7091 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 129 | 9.6001 | 8.4597 | 3.79 | 0.178 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 129 | 9.6001 | 8.4597 | 3.79 | 0.178 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9627 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9627 | 3.45 | 0.324 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 818 | 2.9681 | 2.9192 | 2.23 | 0.227 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 819 | 2.9639 | 2.9151 | 2.23 | 0.227 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2173 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 244 | 5.617 | 5.2751 | 3.99 | 0.139 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4834 | 3.61 | 0.17 |
| `0xeda67a7f…` | Sports | 463 | 3.4357 | 3.4198 | 4.17 | 0.546 |
| `0x86c878cd…` | Sports / Tennis / live | 755 | 2.4997 | 2.4707 | 4.63 | 0.661 |
| `0x86c878cd…` | Sports | 2257 | 1.4206 | 1.4202 | 6.33 | 0.637 |
| `0x86c878cd…` | Sports / Tennis | 834 | 2.3272 | 2.305 | 4.75 | 0.649 |
| `0x2690fe45…` | Sports / price=0.00-0.10 | 55 | 9.8933 | 8.165 | 2.51 | 0.182 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8631 | 2.77 | 0.125 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8631 | 2.77 | 0.125 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.6198 | 2.28 | 0.167 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6274 | 2.81 | 0.636 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 84 | 6.9336 | 5.8649 | 2.57 | 0.131 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3935 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7445 | 3.14 | 0.246 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.436 | 4.18 | 0.62 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 31 | 13.5161 | 9.412 | 2.17 | 0.161 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9844 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2886 | 0.9358 | 0.9356 | 2.47 | 0.54 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2886 | 0.9358 | 0.9356 | 2.47 | 0.54 |
| `0x1941ca5d…` | Sports | 2888 | 0.9352 | 0.9351 | 2.47 | 0.54 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.9463 | 2.72 | 0.209 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6121 | 2.86 | 0.07 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 156 | 4.0581 | 3.6542 | 2.7 | 0.115 |
| `0xef185339…` | Sports | 3825 | 0.7308 | 0.7308 | 22.65 | 0.693 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1872 | 2.73 | 0.665 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9287 | 2.43 | 0.3 |
| `0x13997bdb…` | Sports | 4100 | 0.6748 | 0.6748 | 22.4 | 0.684 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5461 | 2.39 | 0.133 |
| `0xb209ec04…` | Sports | 1543 | 1.0663 | 1.0668 | 4.64 | 0.518 |
| `0x2690fe45…` | Sports | 186 | 3.0003 | 3.0403 | 2.49 | 0.468 |
| `0xd60c6fa3…` | Sports | 3565 | 0.6928 | 0.6928 | 21.02 | 0.688 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1761 | 2.41 | 0.526 |
| `0xb209ec04…` | Sports / Soccer | 888 | 1.3829 | 1.3768 | 4.01 | 0.511 |
| `0xb209ec04…` | Esports / Esports / live | 954 | 1.3304 | 1.3258 | 3.77 | 0.507 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 124 | 4.1182 | 3.6692 | 2.99 | 0.411 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.6286 | 3.4 | 0.478 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 332 | 2.2888 | 2.2042 | 4.34 | 0.41 |
| `0xb209ec04…` | Esports | 1209 | 1.1558 | 1.155 | 4.06 | 0.5 |
| `0xb209ec04…` | Esports / Esports | 1209 | 1.1558 | 1.155 | 4.06 | 0.5 |
| `0xd970693a…` | Sports | 2418 | 0.7994 | 0.7994 | 10.31 | 0.665 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 380 | 2.09 | 2.0066 | 3.43 | 0.287 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 390 | 2.0393 | 1.9604 | 3.43 | 0.282 |
| `0xb209ec04…` | Esports / Esports / Valorant | 199 | 2.9053 | 2.7408 | 2.41 | 0.482 |
| `0xeda67a7f…` | Sports / Tennis / live | 177 | 2.878 | 2.8955 | 2.32 | 0.576 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 538 | 1.6869 | 1.6564 | 3.62 | 0.586 |
| `0x4afbb658…` | Sports | 166 | 3.1455 | 2.9807 | 2.37 | 0.416 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1035 | 1.2021 | 1.1932 | 17.07 | 0.599 |
| `0x86c878cd…` | Sports / Tennis / ATP | 398 | 1.9064 | 1.8811 | 3.1 | 0.631 |
