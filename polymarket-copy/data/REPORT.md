# Отчёт воронки, 2026-10-18 07:04 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 53657 |
| 0. Из них не только 5-мин крипта | 51610 |
| 1. Прошли дешёвые отсечки | 4278 из 14810 |
| 2. Прошли по полной истории | 4 + сегментом 66 из 4278 |
| 3. Прошли реалистичный вход | 7 из 70 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 6449 |
| closed<50 | 5061 |
| top1_concentration | 4360 |
| history<90d | 2785 |
| entries>=0.90 | 2545 |
| short_crypto | 1089 |
| open_now>10 | 981 |
| profit_from<0.10 | 658 |
| positions>5000 | 30 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3839 |
| concurrency_p95>8 | 3307 |
| drawdown | 3240 |
| unstable_halves | 2736 |
| roi_copy<=0 | 1635 |
| silent | 657 |
| low_liquidity | 624 |
| both_sides | 578 |
| top1_concentration | 289 |
| history<90d | 265 |
| closed<50 | 245 |
| hold<1h | 182 |
| entries>=0.90 | 150 |
| short_crypto | 73 |
| segment_only:t<2.0 | 61 |
| segment_only:drawdown | 55 |
| profit_from<0.10 | 51 |
| sniping | 44 |
| segment_only:unstable_halves | 32 |
| segment_only:roi_copy<=0 | 13 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 62 |
| edge_decays_with_delay | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x91b6c3be35634d8bc9639997db5b1d35f7ead2c9` | knopen | Sports | 0.4171 | 2.86 | 0.2769 | 0.2817 | 0.3522 | 7.0 | 12.77 | н/д | Sports (n=112, roi=+0.42) | Sports / Soccer / FIFA World Cup (n=71, roi=+0.47) | Sports / Soccer / pre (n=69, roi=+0.46) | Sports / Soccer / type=moneyline (n=72, roi=+0.45) | Sports / Soccer (n=73, roi=+0.43) |
| `0x46c5aa9e0e3afea63874dd609414250eb3c73188` | Wristony | Sports | 0.2008 | 1.69 | 0.1303 | 0.1255 | 0.1562 | 6.0 | 4.92 | 0.0 | Sports / price=0.50-0.70 (n=40, roi=+0.24) |
| `0xfd30944271c1dee78cb098ef2ea011cce474a990` |  | Sports | 0.1217 | 1.7 | 0.0575 | 0.067 | 0.0903 | 7.0 | 8.79 | 0.0 | Sports / Baseball / price=0.30-0.50 (n=44, roi=+0.28) |
| `0x27b9133c56eb72f5b23ca7eefb31540a40405564` |  | Sports | 0.2391 | 1.48 | 0.072 | 0.1194 | 0.5105 | 5.0 | 10.15 | н/д | Sports / Soccer (n=33, roi=+0.40) |
| `0xad1c106e6a6a30fda1c10629d2f953a83ba16016` | neeyo7777777 | Sports | 0.1025 | 1.09 | 0.0723 | 0.0829 | 0.067 | 4.0 | 9.2 | н/д | Sports / price=0.50-0.70 (n=40, roi=+0.21) |
| `0x8342720db0862f72861ada9c74778b3449d06dc8` | gys-bot | Esports | 0.0521 | 1.72 | 0.0594 | 0.081 | 0.1221 | 8.0 | 2.92 | н/д | Esports / price=0.50-0.70 (n=392, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=392, roi=+0.08) |
| `0xb003fb2e40237facd252cd84190faa0b969dd962` | 0xB003fb2e40237faCd252Cd84190FAA0b969DD962-1765488305296 | Esports | 0.0346 | 1.22 | 0.0585 | 0.0548 | 0.1425 | 7.0 | 3.55 | н/д | Sports / Soccer / price=0.50-0.70 (n=47, roi=+0.17) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xfd30944271c1dee78cb098ef2ea011cce474a990` |  | 0.1217 | Sports / Baseball / price=0.30-0.50 (n=44, roi=+0.28) | segment_only:t<2.0 |
| `0x27b9133c56eb72f5b23ca7eefb31540a40405564` |  | 0.2391 | Sports / Soccer (n=33, roi=+0.40) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0546 | Sports / Soccer / price=0.50-0.70 (n=64, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x46c5aa9e0e3afea63874dd609414250eb3c73188` | Wristony | 0.2008 | Sports / price=0.50-0.70 (n=40, roi=+0.24) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0552 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.0838 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0xb04e697128f8f1dfcf9c913d81c310c0a7421acf` | longriich | 0.1341 | Sports (n=201, roi=+0.16) | Sports / Other sport / price=0.70-0.90 (n=33, roi=+0.14) | Sports / price=0.70-0.90 (n=36, roi=+0.13) | segment_only:drawdown |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0447 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1598 | Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / type=child_moneyline (n=611, roi=+0.19) | Esports (n=709, roi=+0.17) | Esports / Esports (n=709, roi=+0.17) | Esports / Esports / Dota 2 (n=709, roi=+0.17) | segment_only:drawdown |
| `0xad1c106e6a6a30fda1c10629d2f953a83ba16016` | neeyo7777777 | 0.1025 | Sports / price=0.50-0.70 (n=40, roi=+0.21) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x17d3c81eae22badd6c6f31202d7c629e25a5586b` | Buzz-lightyear | -0.0476 | Esports / price=0.70-0.90 (n=30, roi=+0.08) | Esports / Esports / price=0.70-0.90 (n=30, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0557 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0935 | Esports / Esports / Valorant (n=54, roi=+0.28) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0195 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0613 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=77, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0xd4f4ee5f2e93d503e5a1a0cbb5495586fd05bb68` | Auagmg | 0.0238 | Sports / price=0.70-0.90 (n=53, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x93159a717f382318a7dbed96cfc4d61ab6a3afc1` |  | 0.041 | Sports / Soccer / Club Friendlies (n=32, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0128 | Sports / Soccer / price=0.50-0.70 (n=58, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0232 | Sports (n=97, roi=+0.07) | Sports / price=0.70-0.90 (n=70, roi=+0.06) | Sports / Soccer / Counter Strike (n=41, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0579 | Sports / Soccer / type=moneyline (n=54, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0141 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3a4f2d28f884a5d7bfab73956792bc1c931ac4f2` | arunannaveni | -0.0032 | Sports / Soccer / price=0.30-0.50 (n=45, roi=+0.44) | Sports / Soccer / live (n=74, roi=+0.29) | Sports / Soccer (n=123, roi=+0.18) | Sports / Soccer / type=binary (n=85, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0087 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0141 | Sports / Other sport / price=0.70-0.90 (n=54, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6046a68e87c83b1bd9477985b302a0104c58afc3` | Itsmakingyoucry | -0.0057 | Sports / Soccer / pre (n=34, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0012 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0145 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8342720db0862f72861ada9c74778b3449d06dc8` | gys-bot | 0.0521 | Esports / price=0.50-0.70 (n=392, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=392, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0325 | Sports / price=0.30-0.50 (n=93, roi=+0.23) | Sports / Tennis / price=0.30-0.50 (n=38, roi=+0.29) | Sports / Basketball / type=moneyline (n=34, roi=+0.22) | Sports / Basketball (n=37, roi=+0.18) | Sports / Basketball / live (n=32, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.0092 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0094 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0045 | Esports / price=0.50-0.70 (n=116, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=116, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x67a8dd1c146d6ac9e5d220dba3985c9676feb281` | santacar | 0.0103 | Sports / Soccer / type=moneyline (n=97, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x191267f5c2074ccbfe4fe3d6996797148fdfdef8` | heal1god | 0.0509 | Sports / Hockey (n=35, roi=+0.31) | Sports / Hockey / NHL 2026 (n=35, roi=+0.31) | Sports / Hockey / type=moneyline (n=30, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0389 | Sports / Basketball / price=0.50-0.70 (n=33, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0142 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0322 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x91b6c3be35634d8bc9639997db5b1d35f7ead2c9` | knopen | Sports | 113 | 0.4171 | 0.2752 | 2.86 | 0.619 | 7.0 | 12.77 | 5086456 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 769 | 0.1155 | 0.0526 | 3.45 | 0.714 | 8.0 | 2.73 | 398156 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1421 | 0.2463 | 0.0434 | 6.22 | 0.557 | 8.0 | 2.51 | 56300 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 99 | 14.9322 | 12.9112 | 4.12 | 0.182 |
| `0x31121402…` | Sports / price=0.00-0.10 | 94 | 14.9574 | 12.3779 | 3.94 | 0.16 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 815 | 3.3743 | 3.3178 | 2.39 | 0.222 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 816 | 3.3696 | 3.3132 | 2.39 | 0.222 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9624 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9624 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8135 | 3.23 | 0.167 |
| `0xeda67a7f…` | Sports | 486 | 3.2686 | 3.2543 | 4.16 | 0.545 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.7862 | 3.06 | 0.279 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8328 | 2.82 | 0.131 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8328 | 2.82 | 0.131 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5686 | 2.28 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport | 2925 | 1.0358 | 1.0356 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2925 | 1.0358 | 1.0356 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports | 2927 | 1.0352 | 1.035 | 2.63 | 0.549 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3849 | 2.85 | 0.269 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3135 | 7.86 | 0.681 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 62 | 8.6662 | 6.6489 | 3.13 | 0.242 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9779 | 8.06 | 0.75 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1567 | 2.16 | 0.156 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 66 | 8.061 | 6.297 | 2.72 | 0.424 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9763 | 2.51 | 0.519 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.4805 | 2.64 | 0.31 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8604 | 2.71 | 0.206 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6122 | 2.86 | 0.07 |
| `0xef185339…` | Sports | 3849 | 0.7297 | 0.7297 | 22.69 | 0.69 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 158 | 3.994 | 3.5987 | 2.69 | 0.114 |
| `0x7bbb2a27…` | Esports / price=0.00-0.10 | 114 | 4.9036 | 4.2341 | 2.32 | 0.088 |
| `0x13997bdb…` | Sports | 4152 | 0.6764 | 0.6764 | 22.5 | 0.683 |
| `0x7bbb2a27…` | Esports / Esports / price=0.00-0.10 | 111 | 4.7629 | 4.0995 | 2.21 | 0.081 |
| `0xf5fe759c…` | Sports / Tennis / pre | 127 | 4.0296 | 3.8258 | 6.86 | 0.756 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5408 | 2.39 | 0.133 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 129 | 3.9768 | 3.7828 | 6.8 | 0.659 |
| `0xda0f4e3f…` | Sports / price=0.00-0.10 | 113 | 4.6241 | 4.0406 | 2.38 | 0.204 |
| `0xd60c6fa3…` | Sports | 3584 | 0.6917 | 0.6917 | 20.92 | 0.684 |
| `0x1941ca5d…` | Sports / Other sport / live | 2225 | 0.8604 | 0.8618 | 3.34 | 0.592 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 97 | 4.7486 | 3.9951 | 2.67 | 0.546 |
| `0xf5fe759c…` | Sports / Tennis | 162 | 3.1378 | 3.0712 | 6.48 | 0.679 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1047 | 1.2152 | 1.2061 | 17.26 | 0.599 |
| `0x4afbb658…` | Sports | 166 | 3.1455 | 2.9774 | 2.37 | 0.416 |
| `0xda0f4e3f…` | Sports / Soccer / price=0.00-0.10 | 91 | 4.7017 | 3.9886 | 2.18 | 0.22 |
| `0x7a0ca89b…` | Sports | 237 | 2.506 | 2.4697 | 2.89 | 0.667 |
| `0xeda67a7f…` | Sports / Tennis / live | 186 | 2.7496 | 2.7649 | 2.33 | 0.575 |
| `0x70feb53b…` | Sports | 339 | 2.0335 | 2.0195 | 3.35 | 0.72 |
| `0xf5fe759c…` | Sports | 213 | 2.5483 | 2.5469 | 6.61 | 0.671 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 905 | 1.2432 | 1.2313 | 16.21 | 0.592 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 376 | 1.9884 | 1.9089 | 3.25 | 0.279 |
| `0xeda67a7f…` | Sports / Tennis | 196 | 2.597 | 2.6257 | 2.32 | 0.571 |
| `0x13997bdb…` | Sports / Soccer | 2892 | 0.6834 | 0.6834 | 18.46 | 0.687 |
| `0x13997bdb…` | Sports / Soccer / live | 2850 | 0.6865 | 0.6865 | 18.32 | 0.687 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 380 | 1.957 | 1.8799 | 3.23 | 0.276 |
| `0xeda67a7f…` | Sports / Soccer / live | 173 | 2.7614 | 2.7765 | 2.36 | 0.52 |
| `0xeda67a7f…` | Sports / Soccer | 177 | 2.6955 | 2.717 | 2.35 | 0.52 |
| `0xef185339…` | Sports / Soccer | 2587 | 0.7018 | 0.702 | 18.78 | 0.689 |
| `0xef185339…` | Sports / Soccer / live | 2553 | 0.702 | 0.7022 | 18.58 | 0.687 |
| `0x13997bdb…` | Sports / price=0.10-0.30 | 1152 | 1.0423 | 1.0361 | 16.29 | 0.564 |
| `0xf5fe759c…` | Sports / Tennis / ATP | 91 | 3.8374 | 3.6022 | 6.47 | 0.758 |
| `0xd60c6fa3…` | Sports / Soccer | 2414 | 0.691 | 0.691 | 16.48 | 0.683 |
| `0xbd938b88…` | Sports | 3721 | 0.5548 | 0.5548 | 2.06 | 0.7 |
| `0xd60c6fa3…` | Sports / Soccer / live | 2371 | 0.6923 | 0.6923 | 16.27 | 0.682 |
