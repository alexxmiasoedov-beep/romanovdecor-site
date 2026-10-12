# Отчёт воронки, 2026-10-12 07:14 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 54425 |
| 0. Из них не только 5-мин крипта | 52121 |
| 1. Прошли дешёвые отсечки | 4285 из 14013 |
| 2. Прошли по полной истории | 5 + сегментом 59 из 4285 |
| 3. Прошли реалистичный вход | 4 из 64 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 6002 |
| closed<50 | 4799 |
| top1_concentration | 4175 |
| history<90d | 2581 |
| entries>=0.90 | 2534 |
| short_crypto | 992 |
| open_now>10 | 991 |
| profit_from<0.10 | 624 |
| positions>5000 | 28 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3861 |
| concurrency_p95>8 | 3308 |
| drawdown | 3305 |
| unstable_halves | 2813 |
| roi_copy<=0 | 1697 |
| silent | 656 |
| low_liquidity | 650 |
| both_sides | 578 |
| top1_concentration | 303 |
| history<90d | 277 |
| closed<50 | 246 |
| hold<1h | 192 |
| entries>=0.90 | 148 |
| short_crypto | 98 |
| segment_only:t<2.0 | 58 |
| profit_from<0.10 | 56 |
| sniping | 51 |
| segment_only:drawdown | 50 |
| segment_only:unstable_halves | 34 |
| segment_only:roi_copy<=0 | 14 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 54 |
| edge_decays_with_delay | 6 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x234ad7ad32980d1d73a6b9e99abc8498c845a559` | itisrdl | Sports | 0.1677 | 1.84 | 0.1118 | 0.1172 | 0.1727 | 4.0 | 12.2 | н/д | Sports / Soccer / type=moneyline (n=104, roi=+0.19) |
| `0x10c27abfd5561862bd99167b8e607fde0fd86406` | ANDRE888 | Sports | 0.1181 | 2.01 | 0.0944 | 0.1037 | 0.1645 | 8.0 | 7.37 | 0.0042 | все рынки |
| `0xf52427c34c4042665863515f89c5b3f638125b3a` | AgataNetwork | Sports | 0.0515 | 0.73 | 0.0269 | 0.036 | 0.0738 | 6.0 | 4.51 | н/д | Sports / Basketball / pre (n=37, roi=+0.16) |
| `0xe628f2663ad073f77c6ea67867f90d27fa2a0024` | thb9037 | Esports | -0.013 | -0.42 | 0.0262 | 0.0235 | 0.0183 | 6.0 | 4.4 | 0.0 | Esports / Esports / Valorant (n=39, roi=+0.14) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x234ad7ad32980d1d73a6b9e99abc8498c845a559` | itisrdl | 0.1677 | Sports / Soccer / type=moneyline (n=104, roi=+0.19) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0601 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0536 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.038 | Sports / price=0.50-0.70 (n=99, roi=+0.17) | Sports / Tennis / price=0.50-0.70 (n=74, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x667aea383f63409998631c024f95b4f3fa3801cf` | hugofgomes | 0.1546 | Sports (n=193, roi=+0.19) | segment_only:t<2.0 |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.085 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0x73da1e371be9c623b3d80b86c42eacd92977b7ac` | ZOFGK | -0.0566 | Esports / Esports / pre (n=37, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0426 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0837 | Sports / Soccer / type=moneyline (n=52, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca14f80a6daec5144052ee31403c01111cd85915` | 0xcA14F80a6dAeC5144052eE31403C01111CD85915-1772987358266 | 0.0673 | Sports / price=0.30-0.50 (n=30, roi=+0.35) | Sports / Tennis / live (n=34, roi=+0.27) | segment_only:t<2.0 |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0188 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0602 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=73, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0196 | Sports / Soccer / price=0.50-0.70 (n=54, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf6251c1ea571c3993bdc02d8e2d14e09eaf0b7c7` | football-king | 0.0335 | Sports / Soccer / price=0.50-0.70 (n=58, roi=+0.17) | Sports / Soccer / pre (n=140, roi=+0.10) | Sports / Soccer (n=211, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf52427c34c4042665863515f89c5b3f638125b3a` | AgataNetwork | 0.0515 | Sports / Basketball / pre (n=37, roi=+0.16) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0915 | Esports / Esports / Valorant (n=51, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3740f38cb19308b573d4cf550d1865e0f6f9a935` | tiltedinv | -0.0139 | Sports / Hockey / price=0.70-0.90 (n=31, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0ad213f647d6c512bf66f184e0281d70683b9401` | vk-soccer | 0.0666 | Sports / Soccer / Premier League 2025 (n=47, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe628f2663ad073f77c6ea67867f90d27fa2a0024` | thb9037 | -0.013 | Esports / Esports / Valorant (n=39, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0088 | Sports / Soccer / pre (n=38, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xca27292ae5f9c8e6d010e66f37c28928e8cb6f19` | underhaugsvei | 0.057 | Sports / Soccer / live (n=103, roi=+0.16) | Sports / Soccer / type=totals (n=50, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xce041dc32d338cf0a44d7a1b860e793fbdd0dbf6` |  | -0.0091 | Sports / price=0.70-0.90 (n=39, roi=+0.11) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0384 | Sports / price=0.30-0.50 (n=88, roi=+0.27) | Sports / Tennis / price=0.30-0.50 (n=36, roi=+0.30) | Sports (n=415, roi=+0.08) | Sports / Basketball / type=moneyline (n=34, roi=+0.22) | Sports / Basketball (n=37, roi=+0.19) | Sports / Basketball / live (n=32, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.012 | Sports / Other sport / price=0.70-0.90 (n=47, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0026 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0081 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x75e04cc2fff48a555afc5415053b2ac2636f5c67` | MOCKBA | 0.0496 | Sports / Other sport / Elon Tweets (n=35, roi=+0.19) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.008 | Sports / Soccer / pre (n=172, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=153, roi=+0.09) | Sports / price=0.70-0.90 (n=182, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0035 | Esports / price=0.50-0.70 (n=116, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=116, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.0159 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0305 | Sports / American Football (n=160, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1393 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0242 | Esports / price=0.50-0.70 (n=46, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=46, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0374 | Sports / Basketball / price=0.50-0.70 (n=31, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0147 | Esports / price=0.50-0.70 (n=44, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=44, roi=+0.18) | segment_only:t<2.0 |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | 0.0197 | Sports / American Football / CFB 2026 (n=40, roi=+0.09) | Sports / American Football / live (n=32, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0414 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x92d8a88f0a9fef812bdf5628770d6a0ecee39762` | pfk.bgd | Sports | 351 | 1.3562 | 0.2659 | 2.98 | 0.547 | 6.0 | 3.44 | 162733 | delayed_roi<=0 |
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 1030 | 0.3592 | 0.2614 | 11.12 | 0.743 | 8.0 | 1.17 | 30744 | delayed_roi<=0 |
| `0x6aaaf9ad887a4daa865f1b026dd755f4e1a8e611` | Shkrek | Esports | 112 | 0.3859 | 0.2304 | 2.83 | 0.562 | 3.0 | 1.58 | 64040 | edge_decays_with_delay |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 738 | 0.1176 | 0.0547 | 3.44 | 0.718 | 8.0 | 2.77 | 390348 | delayed_roi<=0 |
| `0x10c27abfd5561862bd99167b8e607fde0fd86406` | ANDRE888 | Sports | 352 | 0.1181 | 0.0554 | 2.01 | 0.545 | 8.0 | 7.37 | 355818 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 252 | 23.2304 | 21.8016 | 4.0 | 0.504 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0756 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0543 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1502 | 4.3223 | 4.3154 | 4.33 | 0.709 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8853 | 5.01 | 0.351 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.289 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7667 | 4.16 | 0.626 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1045 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 550 | 4.2364 | 4.2211 | 5.86 | 0.718 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7082 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.395 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.395 | 3.78 | 0.177 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9626 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9626 | 3.45 | 0.324 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2163 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 246 | 5.5632 | 5.227 | 3.99 | 0.138 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4819 | 3.61 | 0.17 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6115 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6115 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.442 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3383 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 758 | 2.4939 | 2.465 | 4.64 | 0.661 |
| `0x86c878cd…` | Sports | 2269 | 1.4137 | 1.4133 | 6.33 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 837 | 2.3226 | 2.3004 | 4.75 | 0.649 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.8144 | 3.06 | 0.279 |
| `0x2690fe45…` | Sports / price=0.00-0.10 | 56 | 10.294 | 8.5079 | 2.64 | 0.196 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8068 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8068 | 2.77 | 0.124 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6234 | 2.81 | 0.636 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7982 | 2.57 | 0.129 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3878 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7433 | 3.14 | 0.246 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.4358 | 4.18 | 0.62 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9817 | 2.51 | 0.519 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8627 | 2.71 | 0.206 |
| `0xe8ca3f75…` | Esports / Esports / live | 148 | 3.9439 | 3.9265 | 2.83 | 0.574 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6119 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 455 | 2.0689 | 2.1417 | 4.26 | 0.657 |
| `0xe8ca3f75…` | Esports / Esports | 455 | 2.0689 | 2.1417 | 4.26 | 0.657 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 157 | 4.0258 | 3.6269 | 2.69 | 0.115 |
| `0xef185339…` | Sports | 3846 | 0.728 | 0.728 | 22.69 | 0.692 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.8122 | 2.13 | 0.183 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1865 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0243 | 5.01 | 0.567 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9279 | 2.43 | 0.3 |
| `0x2690fe45…` | Sports | 189 | 3.1243 | 3.1609 | 2.61 | 0.471 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5286 | 4.77 | 0.568 |
| `0x13997bdb…` | Sports | 4126 | 0.674 | 0.6739 | 22.47 | 0.684 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5443 | 2.39 | 0.133 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7267 | 4.71 | 0.561 |
| `0xda0f4e3f…` | Sports / price=0.00-0.10 | 113 | 4.6241 | 4.0405 | 2.38 | 0.204 |
| `0xb209ec04…` | Sports | 1570 | 1.0514 | 1.052 | 4.65 | 0.518 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7733 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 430 | 1.9199 | 2.0034 | 4.77 | 0.765 |
| `0xd60c6fa3…` | Sports | 3573 | 0.6918 | 0.6918 | 20.99 | 0.687 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1739 | 2.41 | 0.526 |
| `0xb209ec04…` | Sports / Soccer | 888 | 1.3829 | 1.3765 | 4.01 | 0.511 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 124 | 4.1182 | 3.6686 | 2.99 | 0.411 |
| `0xb209ec04…` | Esports / Esports / live | 962 | 1.3166 | 1.312 | 3.76 | 0.506 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.6282 | 3.4 | 0.478 |
