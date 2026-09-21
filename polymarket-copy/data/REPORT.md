# Отчёт воронки, 2026-09-21 15:27 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 20118 |
| 0. Из них не только 5-мин крипта | 19153 |
| 1. Прошли дешёвые отсечки | 2455 из 19153 |
| 2. Прошли по полной истории | 5 + сегментом 70 из 2455 |
| 3. Прошли реалистичный вход | 31 из 75 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 9156 |
| history<90d | 5497 |
| closed<50 | 4995 |
| top1_concentration | 4161 |
| entries>=0.90 | 3826 |
| open_now>10 | 2898 |
| short_crypto | 1521 |
| profit_from<0.10 | 1021 |
| positions>5000 | 110 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 2130 |
| drawdown | 1993 |
| concurrency_p95>8 | 1869 |
| unstable_halves | 1560 |
| roi_copy<=0 | 1044 |
| both_sides | 409 |
| low_liquidity | 403 |
| history<90d | 218 |
| hold<1h | 137 |
| entries>=0.90 | 131 |
| top1_concentration | 68 |
| segment_only:t<2.0 | 64 |
| short_crypto | 55 |
| segment_only:drawdown | 54 |
| sniping | 45 |
| closed<50 | 43 |
| segment_only:unstable_halves | 28 |
| profit_from<0.10 | 23 |
| segment_only:roi_copy<=0 | 7 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 39 |
| edge_decays_with_delay | 5 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xf6683d202f76fc9b79e5be716ce8519dab5b5c69` | 0xf6683D202f76FC9B79E5BE716CE8519DAb5b5c69-1765800503123 | Sports | 0.1634 | 4.41 | 0.0816 | 0.0838 | 0.1899 | 8.0 | 7.48 | н/д | Sports (n=574, roi=+0.17) | Sports / Basketball (n=460, roi=+0.16) | Sports / Basketball / pre (n=455, roi=+0.16) | Sports / Basketball / NBA 2026 (n=408, roi=+0.16) | Sports / Basketball / type=spreads (n=292, roi=+0.17) | Sports / price=0.50-0.70 (n=334, roi=+0.14) |
| `0x0b78daa1212b7a3e9df1de92c8a3a2ee76ff9992` | weizhengwei | Sports | 0.1982 | 1.87 | 0.1541 | 0.151 | 0.1737 | 5.0 | 5.99 | н/д | Sports / Basketball / price=0.50-0.70 (n=46, roi=+0.26) | Sports / price=0.50-0.70 (n=50, roi=+0.24) |
| `0xb75f808fd17210711157eaa9ee3800d05f56a70b` | wi53of | Sports | 0.2285 | 2.64 | 0.2136 | 0.2163 | 0.1743 | 7.0 | 40.7 | н/д | Sports (n=31, roi=+0.31) |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | Sports | 0.0859 | 2.08 | 0.1048 | 0.1235 | 0.0728 | 5.0 | 2.95 | 0.0 | Sports / Soccer (n=51, roi=+0.11) | Sports / Soccer / type=moneyline (n=49, roi=+0.11) |
| `0xe176d8e5178fc9ddbe6a2426f7cf83a999c259bf` |  | Sports | 0.1982 | 1.52 | 0.1389 | 0.1398 | 0.2433 | 4.0 | 11.03 | 0.0 | Sports / Soccer / type=moneyline (n=49, roi=+0.28) |
| `0x0b598417a05a6b0057c620843bd3f2bb0f9f977c` |  | Sports | 0.1492 | 2.07 | 0.1024 | 0.0946 | 0.176 | 7.0 | 12.26 | 0.0027 | все рынки |
| `0x2da245862be758df3908195772b1b06ef4808c2b` | vitbash | Esports | 0.0815 | 1.86 | 0.0796 | 0.0824 | 0.0924 | 3.0 | 3.88 | н/д | Esports / price=0.50-0.70 (n=108, roi=+0.14) | Esports / Esports / price=0.50-0.70 (n=108, roi=+0.14) |
| `0xd733f593f9a7f617f9444cf87d52ae8585ebb175` | Rasica3 | Sports | 0.1958 | 1.57 | 0.0798 | 0.0877 | 0.2521 | 8.0 | 10.28 | н/д | Sports / Soccer / La Liga 2025 (n=34, roi=+0.37) |
| `0x0d874197406ca18d05d49c453ca07731c8bce214` | SantosFC2026 | Esports | 0.1159 | 2.51 | 0.0643 | 0.0192 | 0.103 | 5.0 | 3.25 | н/д | Esports (n=424, roi=+0.13) | Esports / Esports (n=424, roi=+0.13) | Esports / Esports / League of Legends (n=424, roi=+0.13) | Esports / Esports / live (n=422, roi=+0.12) | Esports / price=0.30-0.50 (n=125, roi=+0.21) | Esports / Esports / price=0.30-0.50 (n=125, roi=+0.21) |
| `0x149a9ec31ae097faa33b2f2ae8df659889c149d0` | web3Boss | Esports | 0.0632 | 2.05 | 0.1076 | 0.1106 | 0.152 | 3.0 | 2.37 | н/д | Esports / Esports / type=child_moneyline (n=374, roi=+0.09) | Esports / price=0.30-0.50 (n=34, roi=+0.28) | Esports / Esports / price=0.30-0.50 (n=34, roi=+0.28) | Esports / Esports / live (n=453, roi=+0.07) | Esports / Esports (n=455, roi=+0.07) | Esports / Esports / Dota 2 (n=455, roi=+0.07) |
| `0x310579303783d1b3c2b33cd28d83af946e082e7e` |  | Esports | 0.1124 | 1.53 | 0.0853 | 0.0674 | 0.1551 | 4.0 | 4.88 | 0.0 | Sports / Soccer (n=32, roi=+0.27) |
| `0x971add7b52131edcc061529addeec1eb9d9d8e09` | beth94 | Sports | 0.0925 | 1.77 | 0.0269 | 0.03 | 0.0574 | 7.0 | 14.7 | н/д | Sports / Soccer / type=moneyline (n=49, roi=+0.09) |
| `0x31550df5402226b825f900a31659a05d809d268e` | tizzles | Sports | 0.1389 | 1.23 | 0.0904 | 0.0606 | 0.053 | 5.0 | 5.23 | н/д | Sports / MMA/Boxing / UFC (n=48, roi=+0.27) | Sports / MMA/Boxing / type=moneyline (n=47, roi=+0.27) | Sports / MMA/Boxing / pre (n=33, roi=+0.28) |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | Sports | 0.0337 | 1.85 | 0.1594 | 0.1628 | 0.1454 | 8.0 | 3.17 | н/д | Esports / price=0.50-0.70 (n=47, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.22) | Esports / Esports / Counter Strike (n=138, roi=+0.10) |
| `0x91eaa8ee801ecc6a6ec4094f2ac69c5f89013d79` | stdx3906 | Sports | 0.0883 | 0.93 | 0.0425 | 0.0441 | 0.0939 | 5.0 | 5.02 | 0.0042 | Sports / price=0.50-0.70 (n=65, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=65, roi=+0.18) |
| `0x3689ca03139f0c48947534ab2e919f5300e909aa` | 0x3689cA03139f0C48947534aB2E919F5300E909aA-1781798427541 | Sports | 0.0657 | 1.02 | 0.0534 | 0.0602 | 0.05 | 6.0 | 2.68 | н/д | Sports / price=0.70-0.90 (n=100, roi=+0.09) |
| `0x0f903bf898c30d42c455613ae7102ac1ba1ca39f` | 0X037 | Esports | 0.058 | 1.32 | 0.0292 | 0.0114 | 0.0507 | 3.0 | 3.91 | н/д | Esports / price=0.70-0.90 (n=47, roi=+0.10) | Esports / Esports / price=0.70-0.90 (n=47, roi=+0.10) |
| `0xf34bbd65039f653889d863729b419cc974ffbcb3` | margin-wise | Esports | 0.0827 | 1.88 | 0.0626 | 0.077 | 0.1406 | 7.0 | 2.93 | н/д | Esports / Esports / type=child_moneyline (n=466, roi=+0.10) |
| `0xdd517b727b1445d9744d23bba5856dd06e5f1041` | 0xdd517b727B1445d9744D23BBa5856dd06E5F1041-1776442164856 | Sports | 0.0821 | 1.42 | 0.1247 | 0.1227 | 0.1735 | 5.0 | 5.93 | н/д | Sports / Soccer / La Liga 2025 (n=33, roi=+0.32) |
| `0xaab18830506d45d582007ff27cb35f3038d29678` | veys | Sports | 0.1252 | 1.12 | 0.0926 | 0.0864 | 0.0504 | 8.0 | 2.46 | н/д | Sports / Basketball / type=moneyline (n=31, roi=+0.15) | Sports / Basketball / price=0.70-0.90 (n=43, roi=+0.12) |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | Sports | -0.0179 | -1.69 | 0.0284 | 0.0202 | 0.0378 | 8.0 | 3.7 | н/д | Sports / Other sport / Japan J League (n=31, roi=+0.03) |
| `0x565bedc122552e6824098088c9158ec8179bfa9b` | Piter | Sports | 0.0187 | 0.66 | 0.0596 | 0.059 | 0.0525 | 8.0 | 4.65 | н/д | Sports / Soccer / La Liga 2025 (n=66, roi=+0.17) | Sports / American Football / NFL (n=30, roi=+0.16) |
| `0x1e00e729011c7fbb977cd3c05b1d0a06a6381a29` | flexmrkrn | Sports | 0.0231 | 0.36 | 0.0141 | 0.0244 | 0.0146 | 4.0 | 3.38 | н/д | Sports / price=0.50-0.70 (n=69, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=68, roi=+0.17) |
| `0x49463c64d09380378fd56979c43805fd3292e041` | Ex10Ded | Esports | 0.0005 | 0.02 | 0.0144 | 0.0083 | 0.0529 | 4.0 | 3.15 | н/д | Sports / Hockey / pre (n=126, roi=+0.14) |
| `0x974091fbc1dcd95cad40cf75ae142e6d89fa38af` | aminmb21 | Sports | 0.4164 | 1.37 | 0.0191 | 0.0121 | 0.067 | 7.0 | 3.28 | н/д | Sports / Soccer / pre (n=171, roi=+0.23) |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | Sports | 0.0632 | 0.87 | 0.0122 | 0.0098 | 0.0333 | 7.0 | 2.56 | 0.0 | Sports / Tennis / ATP (n=49, roi=+0.21) | Sports / Tennis / price=0.50-0.70 (n=48, roi=+0.21) |
| `0x78faa0de5df50bfb32e645a905ac66643735d5c3` | GudNNN | Esports | 0.0466 | 0.87 | 0.0535 | 0.0577 | 0.2494 | 5.0 | 2.62 | н/д | Esports / price=0.30-0.50 (n=119, roi=+0.17) | Esports / Esports / price=0.30-0.50 (n=119, roi=+0.17) |
| `0x423f0b745b2952951b4a7d785c7a96e520c63993` | longyi97 | Sports | 0.0586 | 0.71 | 0.0033 | 0.0131 | 0.0935 | 5.0 | 4.85 | н/д | Sports / price=0.50-0.70 (n=73, roi=+0.19) | Sports / Soccer / price=0.50-0.70 (n=73, roi=+0.19) |
| `0xbf39c303bb8b7f061e3721fa14bf781a590f3394` | parlq | Sports | 0.0166 | 0.56 | 0.0212 | 0.0458 | 0.0337 | 7.0 | 1.67 | н/д | Esports / price=0.70-0.90 (n=67, roi=+0.08) | Esports / Esports / price=0.70-0.90 (n=67, roi=+0.08) |
| `0x61a81cff39f833a84cdff8cb68b86b08733c519d` | jean01101 | Esports | 0.0676 | 1.35 | 0.0585 | 0.0316 | 0.1728 | 7.0 | 3.41 | н/д | Esports / Esports / League of Legends (n=248, roi=+0.17) | Sports / Tennis / League of Legends (n=32, roi=+0.28) |
| `0x791e45264c99eecaeb095caea9ad863740d29bda` | easymoneysniperzz | Esports | 0.0423 | 0.91 | 0.0301 | 0.0324 | 0.1506 | 5.0 | 5.13 | н/д | Esports / Esports / type=map_handicap (n=130, roi=+0.21) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xf6683d202f76fc9b79e5be716ce8519dab5b5c69` | 0xf6683D202f76FC9B79E5BE716CE8519DAb5b5c69-1765800503123 | 0.1634 | Sports (n=574, roi=+0.17) | Sports / Basketball (n=460, roi=+0.16) | Sports / Basketball / pre (n=455, roi=+0.16) | Sports / Basketball / NBA 2026 (n=408, roi=+0.16) | Sports / Basketball / type=spreads (n=292, roi=+0.17) | Sports / price=0.50-0.70 (n=334, roi=+0.14) | segment_only:drawdown |
| `0x0b78daa1212b7a3e9df1de92c8a3a2ee76ff9992` | weizhengwei | 0.1982 | Sports / Basketball / price=0.50-0.70 (n=46, roi=+0.26) | Sports / price=0.50-0.70 (n=50, roi=+0.24) | segment_only:t<2.0 |
| `0xb75f808fd17210711157eaa9ee3800d05f56a70b` | wi53of | 0.2285 | Sports (n=31, roi=+0.31) | segment_only:unstable_halves |
| `0x17e2e9176973fa604091bf5ed692bc1f566cd472` |  | -0.0872 | Sports / Soccer / price=0.30-0.50 (n=197, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe176d8e5178fc9ddbe6a2426f7cf83a999c259bf` |  | 0.1982 | Sports / Soccer / type=moneyline (n=49, roi=+0.28) | segment_only:t<2.0 |
| `0x0d874197406ca18d05d49c453ca07731c8bce214` | SantosFC2026 | 0.1159 | Esports (n=424, roi=+0.13) | Esports / Esports (n=424, roi=+0.13) | Esports / Esports / League of Legends (n=424, roi=+0.13) | Esports / Esports / live (n=422, roi=+0.12) | Esports / price=0.30-0.50 (n=125, roi=+0.21) | Esports / Esports / price=0.30-0.50 (n=125, roi=+0.21) | segment_only:drawdown |
| `0x2da245862be758df3908195772b1b06ef4808c2b` | vitbash | 0.0815 | Esports / price=0.50-0.70 (n=108, roi=+0.14) | Esports / Esports / price=0.50-0.70 (n=108, roi=+0.14) | segment_only:t<2.0 |
| `0xd733f593f9a7f617f9444cf87d52ae8585ebb175` | Rasica3 | 0.1958 | Sports / Soccer / La Liga 2025 (n=34, roi=+0.37) | segment_only:t<2.0 |
| `0x8e1e5929e33e43aaa4fca52512f7169fdeddaeac` | Sandcastle | 0.0943 | Sports / price=0.50-0.70 (n=80, roi=+0.15) | segment_only:t<2.0 |
| `0x310579303783d1b3c2b33cd28d83af946e082e7e` |  | 0.1124 | Sports / Soccer (n=32, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x971add7b52131edcc061529addeec1eb9d9d8e09` | beth94 | 0.0925 | Sports / Soccer / type=moneyline (n=49, roi=+0.09) | segment_only:t<2.0 |
| `0xcadf378244dfabfff774b2dae791d87aaa820029` | 0xCADF378244DFAbfFf774B2DAe791D87AAa820029-1768429966318 | 0.0795 | Esports / price=0.50-0.70 (n=189, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=189, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.0402 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x31550df5402226b825f900a31659a05d809d268e` | tizzles | 0.1389 | Sports / MMA/Boxing / UFC (n=48, roi=+0.27) | Sports / MMA/Boxing / type=moneyline (n=47, roi=+0.27) | Sports / MMA/Boxing / pre (n=33, roi=+0.28) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | 0.0337 | Esports / price=0.50-0.70 (n=47, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.22) | Esports / Esports / Counter Strike (n=138, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x91eaa8ee801ecc6a6ec4094f2ac69c5f89013d79` | stdx3906 | 0.0883 | Sports / price=0.50-0.70 (n=65, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=65, roi=+0.18) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1651 | Esports / price=0.10-0.30 (n=88, roi=+0.49) | Esports / Esports / price=0.10-0.30 (n=88, roi=+0.49) | Esports (n=549, roi=+0.17) | Esports / Esports (n=549, roi=+0.17) | Esports / Esports / Dota 2 (n=549, roi=+0.17) | Esports / Esports / type=child_moneyline (n=474, roi=+0.18) | segment_only:drawdown |
| `0x3689ca03139f0c48947534ab2e919f5300e909aa` | 0x3689cA03139f0C48947534aB2E919F5300E909aA-1781798427541 | 0.0657 | Sports / price=0.70-0.90 (n=100, roi=+0.09) | segment_only:t<2.0 |
| `0xf34bbd65039f653889d863729b419cc974ffbcb3` | margin-wise | 0.0827 | Esports / Esports / type=child_moneyline (n=466, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0x0f903bf898c30d42c455613ae7102ac1ba1ca39f` | 0X037 | 0.058 | Esports / price=0.70-0.90 (n=47, roi=+0.10) | Esports / Esports / price=0.70-0.90 (n=47, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0xdd517b727b1445d9744d23bba5856dd06e5f1041` | 0xdd517b727B1445d9744D23BBa5856dd06E5F1041-1776442164856 | 0.0821 | Sports / Soccer / La Liga 2025 (n=33, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.0928 | Sports / Soccer / pre (n=260, roi=+0.15) | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | Sports / Soccer (n=301, roi=+0.13) | Sports / Soccer / price=0.50-0.70 (n=116, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0179 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0239 | Sports / Soccer / Counter Strike (n=31, roi=+0.10) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xaab18830506d45d582007ff27cb35f3038d29678` | veys | 0.1252 | Sports / Basketball / type=moneyline (n=31, roi=+0.15) | Sports / Basketball / price=0.70-0.90 (n=43, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown |
| `0x565bedc122552e6824098088c9158ec8179bfa9b` | Piter | 0.0187 | Sports / Soccer / La Liga 2025 (n=66, roi=+0.17) | Sports / American Football / NFL (n=30, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x0dbe4798a1719b1fc08cd3acc2369dd77c069013` | brussssss | -0.0038 | Sports / Soccer / price=0.50-0.70 (n=166, roi=+0.13) | Sports / price=0.50-0.70 (n=168, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.011 | Sports / Soccer / Indian Premier League (n=97, roi=+0.07) | Sports / price=0.70-0.90 (n=127, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=63, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0034 | Sports / Hockey / live (n=30, roi=+0.22) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1e00e729011c7fbb977cd3c05b1d0a06a6381a29` | flexmrkrn | 0.0231 | Sports / price=0.50-0.70 (n=69, roi=+0.18) | Sports / Soccer / price=0.50-0.70 (n=68, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0316 | Sports / price=0.30-0.50 (n=67, roi=+0.22) | Sports (n=323, roi=+0.09) | Sports / Basketball / type=moneyline (n=32, roi=+0.20) | Sports / Basketball (n=35, roi=+0.16) | Sports / price=0.70-0.90 (n=75, roi=+0.10) | Sports / Basketball / live (n=30, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x758f40d5c4a76350096f3deaa0d016ed52efdfb7` | 0nglee | 0.0069 | Sports / Soccer (n=40, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0089 | Sports / Other sport / price=0.70-0.90 (n=45, roi=+0.10) | Sports / Other sport (n=56, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x49463c64d09380378fd56979c43805fd3292e041` | Ex10Ded | 0.0005 | Sports / Hockey / pre (n=126, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x974091fbc1dcd95cad40cf75ae142e6d89fa38af` | aminmb21 | 0.4164 | Sports / Soccer / pre (n=171, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown |
| `0x260246b2eafb577df64aaab33766f2dd4c47ba09` | Tiski | 0.1558 | Sports / price=0.30-0.50 (n=31, roi=+0.39) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | 0.0632 | Sports / Tennis / ATP (n=49, roi=+0.21) | Sports / Tennis / price=0.50-0.70 (n=48, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x722abb5460060870d46728bf45f66a6b1635d6ed` | SHSVHVD3 | 0.0468 | Sports / price=0.30-0.50 (n=65, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0xd9954ad6ac35f7913588067bd4cf77552260b354` | Po1yBot-Xr7EnrohZT | 0.0142 | Sports / Other sport / Elon Tweets 48H (n=104, roi=+0.15) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0747 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 830 | 0.3157 | 0.2347 | 9.4 | 0.74 | 8.0 | 1.07 | 36471 | delayed_roi<=0 |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 557 | 0.1957 | 0.1073 | 5.82 | 0.531 | 6.0 | 6.17 | 377288 | edge_decays_with_delay |
| `0x0b598417a05a6b0057c620843bd3f2bb0f9f977c` |  | Sports | 123 | 0.1492 | 0.1108 | 2.07 | 0.724 | 7.0 | 12.26 | 4091220 | прошёл |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | Sports | 76 | 0.0859 | 0.1058 | 2.08 | 0.724 | 5.0 | 2.95 | 2854508 | прошёл |
| `0x149a9ec31ae097faa33b2f2ae8df659889c149d0` | web3Boss | Esports | 507 | 0.0632 | 0.0568 | 2.05 | 0.716 | 3.0 | 2.37 | 173799 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 214 | 20.1735 | 18.723 | 4.01 | 0.495 |
| `0x8548f0fa…` | Esports / price=0.00-0.10 | 79 | 29.0759 | 23.3348 | 2.2 | 0.278 |
| `0x8548f0fa…` | Esports / Esports / price=0.00-0.10 | 79 | 29.0759 | 23.3348 | 2.2 | 0.278 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 207 | 13.4074 | 12.3507 | 5.9 | 0.222 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 92 | 21.528 | 18.2556 | 5.83 | 0.511 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8947 | 5.01 | 0.351 |
| `0xe8ca3f75…` | Sports | 1380 | 3.5573 | 3.5523 | 4.43 | 0.713 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.6594 | 4.16 | 0.626 |
| `0xe8ca3f75…` | Sports / Tennis / live | 118 | 11.9082 | 10.6466 | 4.23 | 0.542 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 89 | 12.228 | 10.4478 | 3.47 | 0.157 |
| `0xe8ca3f75…` | Sports / Tennis | 529 | 4.2018 | 4.1655 | 5.77 | 0.72 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 813 | 2.9949 | 2.9458 | 2.23 | 0.228 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 814 | 2.9906 | 2.9417 | 2.23 | 0.227 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 130 | 8.1694 | 7.2688 | 3.53 | 0.792 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.4663 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.4663 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 123 | 7.0342 | 6.4984 | 3.33 | 0.756 |
| `0x86c878cd…` | Sports / Tennis / live | 738 | 2.558 | 2.5279 | 4.63 | 0.659 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 248 | 4.4424 | 4.3499 | 3.99 | 0.73 |
| `0x86c878cd…` | Sports | 2169 | 1.463 | 1.4626 | 6.27 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 816 | 2.3792 | 2.3561 | 4.75 | 0.646 |
| `0xeda67a7f…` | Sports | 416 | 2.877 | 2.8609 | 3.64 | 0.543 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 34 | 14.1086 | 9.8188 | 2.29 | 0.176 |
| `0x9b979a06…` | Sports / price=0.00-0.10 | 50 | 11.0001 | 7.9339 | 2.53 | 0.32 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 81 | 7.2274 | 6.0764 | 2.59 | 0.136 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.326 | 7.86 | 0.681 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9925 | 8.06 | 0.75 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 102 | 6.0952 | 5.1532 | 2.56 | 0.118 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 102 | 6.0952 | 5.1532 | 2.56 | 0.118 |
| `0x1941ca5d…` | Sports / Other sport | 2807 | 0.9691 | 0.969 | 2.49 | 0.521 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2807 | 0.9691 | 0.969 | 2.49 | 0.521 |
| `0x1941ca5d…` | Sports | 2809 | 0.9685 | 0.9684 | 2.49 | 0.521 |
| `0xe8ca3f75…` | Esports / Esports / live | 147 | 3.9375 | 3.8495 | 2.8 | 0.571 |
| `0xe8ca3f75…` | Esports | 443 | 2.099 | 2.1466 | 4.21 | 0.65 |
| `0xe8ca3f75…` | Esports / Esports | 443 | 2.099 | 2.1466 | 4.21 | 0.65 |
| `0x86c878cd…` | Sports / Tennis / WTA | 195 | 3.4094 | 3.2239 | 2.73 | 0.667 |
| `0xef185339…` | Sports | 3751 | 0.7305 | 0.7305 | 22.51 | 0.695 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.932 | 2.43 | 0.3 |
| `0xf5fe759c…` | Sports / Tennis / pre | 123 | 4.1423 | 3.9248 | 6.86 | 0.748 |
| `0x13997bdb…` | Sports | 3980 | 0.6853 | 0.6853 | 22.22 | 0.688 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 127 | 4.0219 | 3.8267 | 6.78 | 0.654 |
| `0x6c64f666…` | Esports / price=0.00-0.10 | 38 | 10.3487 | 6.9076 | 2.06 | 0.184 |
| `0x6c64f666…` | Esports / Esports / price=0.00-0.10 | 38 | 10.3487 | 6.9076 | 2.06 | 0.184 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 411 | 1.9893 | 2.0456 | 4.73 | 0.771 |
| `0xd60c6fa3…` | Sports | 3473 | 0.695 | 0.695 | 20.65 | 0.691 |
| `0xeda67a7f…` | Sports / Tennis / live | 146 | 3.4962 | 3.3793 | 2.33 | 0.589 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 327 | 2.3298 | 2.2422 | 4.35 | 0.413 |
| `0xeda67a7f…` | Sports / Tennis | 154 | 3.2999 | 3.211 | 2.32 | 0.584 |
| `0xf5fe759c…` | Sports / Tennis | 158 | 3.203 | 3.1338 | 6.47 | 0.671 |
| `0xd970693a…` | Sports | 2324 | 0.811 | 0.811 | 10.07 | 0.659 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 361 | 2.1227 | 2.0308 | 3.33 | 0.288 |
| `0x8548f0fa…` | Esports / Esports / live | 3885 | 0.6166 | 0.6168 | 2.24 | 0.943 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 376 | 2.0622 | 1.9769 | 3.36 | 0.282 |
| `0x8548f0fa…` | Esports / Esports | 3920 | 0.6117 | 0.612 | 2.24 | 0.941 |
| `0x8548f0fa…` | Esports | 3938 | 0.6083 | 0.6085 | 2.24 | 0.94 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1018 | 1.2057 | 1.1966 | 16.97 | 0.601 |
| `0x86c878cd…` | Sports / Tennis / ATP | 390 | 1.9466 | 1.9207 | 3.11 | 0.628 |
| `0xeda67a7f…` | Sports / Soccer / live | 156 | 3.0802 | 3.0172 | 2.38 | 0.519 |
| `0xf5fe759c…` | Sports | 207 | 2.6049 | 2.6033 | 6.58 | 0.667 |
| `0xeda67a7f…` | Sports / Soccer | 160 | 2.9994 | 2.9468 | 2.37 | 0.519 |
