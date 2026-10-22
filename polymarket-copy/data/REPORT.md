# Отчёт воронки, 2026-10-22 07:10 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 57911 |
| 0. Из них не только 5-мин крипта | 55858 |
| 1. Прошли дешёвые отсечки | 4351 из 17760 |
| 2. Прошли по полной истории | 6 + сегментом 56 из 4351 |
| 3. Прошли реалистичный вход | 6 из 62 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 8409 |
| closed<50 | 7765 |
| top1_concentration | 6357 |
| history<90d | 3606 |
| entries>=0.90 | 3529 |
| short_crypto | 1214 |
| open_now>10 | 861 |
| profit_from<0.10 | 788 |
| positions>5000 | 26 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3966 |
| concurrency_p95>8 | 3441 |
| drawdown | 3295 |
| unstable_halves | 2903 |
| roi_copy<=0 | 1666 |
| silent | 804 |
| low_liquidity | 624 |
| both_sides | 593 |
| top1_concentration | 327 |
| history<90d | 291 |
| closed<50 | 260 |
| hold<1h | 169 |
| entries>=0.90 | 148 |
| short_crypto | 80 |
| segment_only:t<2.0 | 54 |
| segment_only:drawdown | 45 |
| profit_from<0.10 | 44 |
| sniping | 34 |
| segment_only:unstable_halves | 29 |
| segment_only:roi_copy<=0 | 12 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 53 |
| edge_decays_with_delay | 3 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x6ea678e7e079a93c357a5e86e4b67f7d4a663565` | hldisco | Sports | 0.2093 | 1.87 | 0.1972 | 0.2064 | 0.2359 | 6.0 | 6.28 | н/д | Sports / Soccer / pre (n=53, roi=+0.24) | Sports / Soccer (n=55, roi=+0.23) | Sports / Soccer / price=0.50-0.70 (n=40, roi=+0.27) | Sports / price=0.50-0.70 (n=42, roi=+0.25) |
| `0xe688b2495fe76655f9254d582110951cb8464d80` | lawson999 | Sports | 0.0949 | 3.16 | 0.0932 | 0.099 | 0.0599 | 5.0 | 2.25 | н/д | Esports (n=44, roi=+0.14) | Esports / Esports (n=44, roi=+0.14) | Esports / Esports / type=moneyline (n=44, roi=+0.14) | Esports / Esports / League of Legends (n=39, roi=+0.13) |
| `0xf7992c630ea811693b20cc83cff7f7b8dd1a6255` | marquitos-pedofilo-racista | Sports | 0.1391 | 2.04 | 0.1284 | 0.1174 | 0.1107 | 3.0 | 2.09 | н/д | Sports / Soccer / live (n=30, roi=+0.22) | Sports (n=63, roi=+0.15) | Sports / Soccer (n=60, roi=+0.14) |
| `0xa6f592f15388fa7ea879dc61a0de21ed6ffd4653` | eastwoodgrain | Sports | 0.1066 | 1.7 | 0.0755 | 0.0688 | 0.1088 | 5.0 | 2.82 | н/д | Sports / price=0.70-0.90 (n=41, roi=+0.12) |
| `0xfe4202f23959137f8705b6b9e45e2bc027d96eb9` | 0xFe4202f23959137F8705b6B9E45E2bc027d96EB9-1781793515161 | Sports | 0.1153 | 1.22 | 0.0571 | 0.0875 | 0.1188 | 3.0 | 3.97 | 0.0 | Sports / Soccer (n=61, roi=+0.25) | Sports / Soccer / type=moneyline (n=58, roi=+0.23) | Sports / Soccer / price=0.50-0.70 (n=30, roi=+0.24) |
| `0x67a8dd1c146d6ac9e5d220dba3985c9676feb281` | santacar | Sports | 0.0206 | 0.38 | 0.0242 | 0.0374 | 0.0682 | 7.0 | 4.65 | 0.2213 | Sports / Soccer / type=moneyline (n=101, roi=+0.15) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x6ea678e7e079a93c357a5e86e4b67f7d4a663565` | hldisco | 0.2093 | Sports / Soccer / pre (n=53, roi=+0.24) | Sports / Soccer (n=55, roi=+0.23) | Sports / Soccer / price=0.50-0.70 (n=40, roi=+0.27) | Sports / price=0.50-0.70 (n=42, roi=+0.25) | segment_only:t<2.0 |
| `0xa6f592f15388fa7ea879dc61a0de21ed6ffd4653` | eastwoodgrain | 0.1066 | Sports / price=0.70-0.90 (n=41, roi=+0.12) | segment_only:t<2.0 |
| `0x7ad71d79a3bb90d0a87a06500fa0fe11663842aa` | theowalcott | 0.1308 | Sports / Soccer / price=0.30-0.50 (n=96, roi=+0.25) | Sports / price=0.30-0.50 (n=106, roi=+0.22) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0542 | Sports / Soccer / price=0.50-0.70 (n=65, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0534 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfe4202f23959137f8705b6b9e45e2bc027d96eb9` | 0xFe4202f23959137F8705b6B9E45E2bc027d96EB9-1781793515161 | 0.1153 | Sports / Soccer (n=61, roi=+0.25) | Sports / Soccer / type=moneyline (n=58, roi=+0.23) | Sports / Soccer / price=0.50-0.70 (n=30, roi=+0.24) | segment_only:t<2.0 |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0446 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0963 | Esports / Esports / Valorant (n=55, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0558 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1539 | Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / type=child_moneyline (n=614, roi=+0.18) | Esports (n=712, roi=+0.16) | Esports / Esports (n=712, roi=+0.16) | Esports / Esports / Dota 2 (n=712, roi=+0.16) | segment_only:drawdown |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0247 | Sports (n=102, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0086 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0512 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=84, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0118 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0081 | Sports / Soccer / price=0.50-0.70 (n=61, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.0261 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0 |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0111 | Sports / Soccer / pre (n=40, roi=+0.23) | Sports / Soccer (n=41, roi=+0.21) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | -0.0029 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x5d68ae7869c19cb27deb63ae8d911d59d6a7ff40` | 0x5D68ae7869C19Cb27DEB63Ae8d911D59D6a7Ff40-1782738338244 | 0.0093 | Sports / Other sport / type=totals (n=82, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0031 | Sports / Other sport / price=0.70-0.90 (n=75, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0219 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xefbb277c49e92bf109425fdd636156050954d067` | Canadaaa | 0.0052 | Sports / Soccer / La Liga 2025 (n=34, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0053 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x828a17f571c08b3a201e94b4480f0dda2daebef1` | arcowin | -0.0164 | Sports / Other sport / live (n=64, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x332fb63ddf2478a64a9b090db07bb2a1b3ee80a4` | Fulc | 0.0459 | Sports / price=0.30-0.50 (n=86, roi=+0.27) | Crypto (n=65, roi=+0.23) | Crypto / price=0.50-0.70 (n=41, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xdefdba677384e28a8c3e6e6fa6303a9e29193f9d` | chet1101 | 0.0364 | Esports / Esports / League of Legends (n=46, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0135 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x67a8dd1c146d6ac9e5d220dba3985c9676feb281` | santacar | 0.0206 | Sports / Soccer / type=moneyline (n=101, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.137 | Sports / Basketball (n=72, roi=+0.38) | Sports / Basketball / NBA 2026 (n=72, roi=+0.38) | Sports / Basketball / type=moneyline (n=72, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0244 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0x75219ed7915022cba1ecd8ae0a9ade07b748c083` | Ronnydon15 | 0.0195 | Sports / Soccer / type=both_teams_to_score (n=62, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x75708a00a833a58a1dd7bc00d433df94d42505a0` | bucodiculo | 0.0559 | Sports / price=0.50-0.70 (n=34, roi=+0.25) | segment_only:t<2.0 |
| `0xffe290a74a57db36b06cc88692b16f1cda322957` | sfst | 0.0241 | Sports / price=0.50-0.70 (n=30, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0412 | Esports / price=0.50-0.70 (n=47, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0 |
| `0x66db92250e63e86365eec54fce57dcec7a90370f` | koei73 | 0.0496 | Sports / Soccer / type=totals (n=123, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x7dbd29d5755057480c465a8ed1178feddc10e1e3` | Ivolama | 0.0293 | Sports / Soccer / type=moneyline (n=88, roi=+0.23) | Sports / Soccer (n=95, roi=+0.22) | Sports / Soccer / live (n=73, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x880dbf161120207d47aef05ec774b331bcec39bc` | akulaxl | 0.0231 | Esports / Esports / type=moneyline (n=53, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe688b2495fe76655f9254d582110951cb8464d80` | lawson999 | Sports | 100 | 0.0949 | 0.1076 | 3.16 | 0.84 | 5.0 | 2.25 | 736540 | прошёл |
| `0xf7992c630ea811693b20cc83cff7f7b8dd1a6255` | marquitos-pedofilo-racista | Sports | 72 | 0.1391 | 0.1357 | 2.04 | 0.819 | 3.0 | 2.09 | 639462 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0xd670301420f6011e8136b07c50d7f4002bcee98f` | Mrpitter | Culture | 91 | 0.5248 | 0.1216 | 2.05 | 0.549 | 8.0 | 23.31 | 70640 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 792 | 0.1089 | 0.0466 | 3.31 | 0.711 | 8.0 | 2.71 | 398156 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1471 | 0.2366 | 0.0385 | 6.17 | 0.549 | 8.0 | 2.38 | 59430 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 253 | 23.3322 | 21.9003 | 4.03 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0735 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0523 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1520 | 4.3059 | 4.2992 | 4.37 | 0.709 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8804 | 5.01 | 0.351 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2873 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7646 | 4.16 | 0.626 |
| `0x31121402…` | Sports / price=0.00-0.10 | 103 | 12.5922 | 10.585 | 3.71 | 0.136 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1041 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 554 | 4.2085 | 4.1938 | 5.87 | 0.72 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7077 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3925 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3925 | 3.78 | 0.177 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 804 | 3.4235 | 3.3652 | 2.39 | 0.221 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 805 | 3.4187 | 3.3605 | 2.39 | 0.221 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 55 | 15.3636 | 11.3328 | 3.05 | 0.164 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2132 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 251 | 5.4325 | 5.1107 | 3.97 | 0.135 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4797 | 3.61 | 0.17 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6087 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6087 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4404 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3374 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 768 | 2.4598 | 2.4315 | 4.63 | 0.659 |
| `0x86c878cd…` | Sports | 2308 | 1.3947 | 1.3943 | 6.35 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 848 | 2.2912 | 2.2694 | 4.75 | 0.647 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.7818 | 3.06 | 0.279 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 108 | 6.7828 | 5.7789 | 2.81 | 0.13 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 108 | 6.7828 | 5.7789 | 2.81 | 0.13 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 90 | 7.5731 | 6.2883 | 3.05 | 0.4 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6177 | 2.81 | 0.636 |
| `0x1941ca5d…` | Sports / Other sport | 2906 | 1.0427 | 1.0425 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2906 | 1.0427 | 1.0425 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports | 2908 | 1.042 | 1.0419 | 2.63 | 0.549 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7937 | 2.57 | 0.129 |
| `0xe9f5c75e…` | Sports / Basketball / live | 465 | 2.4973 | 2.4286 | 4.19 | 0.622 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9748 | 2.51 | 0.519 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.4799 | 2.64 | 0.31 |
| `0xe8ca3f75…` | Esports / Esports / live | 149 | 3.9107 | 3.896 | 2.82 | 0.57 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6124 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 458 | 2.0644 | 2.1365 | 4.28 | 0.657 |
| `0xe8ca3f75…` | Esports / Esports | 458 | 2.0644 | 2.1365 | 4.28 | 0.657 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 160 | 3.9316 | 3.547 | 2.68 | 0.113 |
| `0x86c878cd…` | Sports / Tennis / WTA | 200 | 3.3218 | 3.1421 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0197 | 5.01 | 0.567 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.525 | 4.77 | 0.568 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.723 | 4.71 | 0.561 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 92 | 5.3041 | 4.4409 | 2.38 | 0.13 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7702 | 4.55 | 0.538 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 111 | 4.5856 | 3.9378 | 2.85 | 0.541 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 434 | 1.9055 | 1.9884 | 4.78 | 0.767 |
| `0xb209ec04…` | Sports | 1607 | 1.0243 | 1.0249 | 4.63 | 0.516 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1708 | 2.41 | 0.526 |
| `0xd60c6fa3…` | Sports | 3594 | 0.6849 | 0.6849 | 20.88 | 0.684 |
| `0xb209ec04…` | Sports / Soccer | 896 | 1.375 | 1.3684 | 4.03 | 0.512 |
| `0x1941ca5d…` | Sports / Other sport / live | 2208 | 0.8669 | 0.8683 | 3.34 | 0.593 |
| `0xb209ec04…` | Esports / Esports / live | 969 | 1.3076 | 1.3029 | 3.76 | 0.507 |
| `0xb209ec04…` | Sports / Soccer / live | 618 | 1.6434 | 1.6256 | 3.4 | 0.479 |
