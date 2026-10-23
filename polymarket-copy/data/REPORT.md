# Отчёт воронки, 2026-10-23 07:12 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 57421 |
| 0. Из них не только 5-мин крипта | 55302 |
| 1. Прошли дешёвые отсечки | 4257 из 16653 |
| 2. Прошли по полной истории | 3 + сегментом 52 из 4257 |
| 3. Прошли реалистичный вход | 2 из 55 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 7423 |
| closed<50 | 6852 |
| top1_concentration | 5683 |
| entries>=0.90 | 3670 |
| history<90d | 3081 |
| short_crypto | 1077 |
| open_now>10 | 975 |
| profit_from<0.10 | 646 |
| positions>5000 | 15 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3883 |
| concurrency_p95>8 | 3312 |
| drawdown | 3187 |
| unstable_halves | 2824 |
| roi_copy<=0 | 1642 |
| silent | 785 |
| both_sides | 603 |
| low_liquidity | 563 |
| top1_concentration | 318 |
| history<90d | 280 |
| closed<50 | 266 |
| hold<1h | 168 |
| entries>=0.90 | 130 |
| short_crypto | 69 |
| segment_only:t<2.0 | 50 |
| profit_from<0.10 | 45 |
| segment_only:drawdown | 45 |
| sniping | 32 |
| segment_only:unstable_halves | 30 |
| segment_only:roi_copy<=0 | 14 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 50 |
| edge_decays_with_delay | 3 |
| slippage | 2 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x0206ffc3c09c37e0073e705ebae4c0011bf4bf76` | Cosmos99 | Sports | 0.0884 | 1.3 | 0.0578 | 0.0716 | 0.0433 | 4.0 | 5.56 | н/д | Sports / Tennis (n=74, roi=+0.15) | Sports / Tennis / WTA (n=39, roi=+0.17) |
| `0xfec2354068ceed5766379c53180449e9070c08af` | Akareim | Sports | -0.0198 | -0.95 | 0.0561 | 0.0802 | -0.0062 | 6.0 | 4.3 | н/д | Sports / Soccer / UEFA Europa League 2025 (n=30, roi=+0.16) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0564 | Sports / Soccer / price=0.50-0.70 (n=65, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0603 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0519 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0568fa4512d53dfaf47f57898f8624798700dc48` | BatyaZahara | 0.124 | Sports (n=83, roi=+0.17) | Sports / price=0.70-0.90 (n=31, roi=+0.19) | Sports / Soccer / price=0.70-0.90 (n=30, roi=+0.19) | segment_only:t<2.0 |
| `0x762ee19681f0482dfe3e44ca42e9a26b34564bf0` | metski29 | -0.0511 | Sports / American Football (n=48, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0457 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca14f80a6daec5144052ee31403c01111cd85915` | UQ147 | 0.0718 | Sports / price=0.30-0.50 (n=33, roi=+0.41) | Sports / Tennis / live (n=36, roi=+0.26) | segment_only:t<2.0 |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0574 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0963 | Esports / Esports / Valorant (n=55, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0xfec2354068ceed5766379c53180449e9070c08af` | Akareim | -0.0198 | Sports / Soccer / UEFA Europa League 2025 (n=30, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0206ffc3c09c37e0073e705ebae4c0011bf4bf76` | Cosmos99 | 0.0884 | Sports / Tennis (n=74, roi=+0.15) | Sports / Tennis / WTA (n=39, roi=+0.17) | segment_only:t<2.0 |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0247 | Sports (n=103, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0086 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0134 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.148 | Esports / price=0.10-0.30 (n=115, roi=+0.48) | Esports / Esports / price=0.10-0.30 (n=115, roi=+0.48) | Esports / Esports / type=child_moneyline (n=618, roi=+0.18) | Esports (n=716, roi=+0.15) | Esports / Esports (n=716, roi=+0.15) | Esports / Esports / Dota 2 (n=716, roi=+0.15) | segment_only:drawdown |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0111 | Sports / Soccer / pre (n=40, roi=+0.23) | Sports / Soccer (n=41, roi=+0.21) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0055 | Sports / price=0.50-0.70 (n=203, roi=+0.09) | Sports / Soccer / price=0.50-0.70 (n=61, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd2e740480d0f864d8520fc0627ab94c49322131` | 0xFd2e740480D0F864d8520FC0627ab94c49322131-1769035449764 | 0.0259 | Sports / Baseball (n=38, roi=+0.13) | Sports / Baseball / MLB (n=38, roi=+0.13) | Sports / Baseball / type=moneyline (n=38, roi=+0.13) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | -0.006 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0219 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0324 | Sports / American Football (n=172, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0053 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x828a17f571c08b3a201e94b4480f0dda2daebef1` | arcowin | -0.0154 | Sports / Other sport / live (n=64, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x757ac68fdcd4c21ce005ba42f5bb6d96c4f11f84` | steadyhodl | 0.0395 | Sports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xdefdba677384e28a8c3e6e6fa6303a9e29193f9d` | chet1101 | 0.0422 | Esports / Esports / League of Legends (n=46, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x191267f5c2074ccbfe4fe3d6996797148fdfdef8` | heal1god | 0.0518 | Sports / Hockey (n=35, roi=+0.31) | Sports / Hockey / NHL 2026 (n=35, roi=+0.31) | Sports / Hockey / type=moneyline (n=30, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.137 | Sports / Basketball (n=72, roi=+0.38) | Sports / Basketball / NBA 2026 (n=72, roi=+0.38) | Sports / Basketball / type=moneyline (n=72, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0155 | Sports / Baseball / type=totals (n=37, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.023 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0x66db92250e63e86365eec54fce57dcec7a90370f` | koei73 | 0.0589 | Sports / Soccer / type=totals (n=125, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0412 | Esports / price=0.50-0.70 (n=47, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0 |
| `0x880dbf161120207d47aef05ec774b331bcec39bc` | akulaxl | 0.0167 | Esports / Esports / type=moneyline (n=53, roi=+0.32) | Esports / price=0.70-0.90 (n=176, roi=+0.07) | Esports / Esports / price=0.70-0.90 (n=176, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0459 | Sports / American Football / pre (n=58, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8007ad03470539b924f93d3d263981c39d05a8f4` | OstapP | 0.0131 | Sports / Other sport / price=0.70-0.90 (n=90, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.051 | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9cbb674bdacc27020e6adb549461e45ade24a2e1` | Tentm1 | 0.0368 | Sports / American Football / NFL (n=41, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xe0b01fa337f48b3792ae9e76f3665bfc4f3a5294` | tnns1 | 0.0106 | Sports / Tennis / WTA (n=142, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x6aaaf9ad887a4daa865f1b026dd755f4e1a8e611` | Shkrek | Esports | 118 | 0.3531 | 0.2032 | 2.66 | 0.551 | 3.0 | 1.8 | 62786 | edge_decays_with_delay |
| `0xd670301420f6011e8136b07c50d7f4002bcee98f` | Mrpitter | Culture | 93 | 0.5085 | 0.1132 | 2.02 | 0.548 | 8.0 | 23.49 | 72055 | delayed_roi<=0;slippage |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 793 | 0.1099 | 0.0477 | 3.34 | 0.711 | 8.0 | 2.71 | 398156 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0522 | 5.92 | 0.224 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8802 | 5.01 | 0.351 |
| `0x31121402…` | Sports / price=0.00-0.10 | 103 | 12.5922 | 10.5855 | 3.71 | 0.136 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3924 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3924 | 3.78 | 0.177 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 804 | 3.4186 | 3.3602 | 2.39 | 0.221 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 805 | 3.4138 | 3.3555 | 2.39 | 0.221 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 55 | 15.3636 | 11.3335 | 3.05 | 0.164 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.213 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 251 | 5.4325 | 5.1107 | 3.97 | 0.135 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4796 | 3.61 | 0.17 |
| `0x86c878cd…` | Sports / Tennis / live | 769 | 2.4567 | 2.4285 | 4.63 | 0.659 |
| `0x86c878cd…` | Sports | 2311 | 1.3941 | 1.3937 | 6.36 | 0.637 |
| `0x86c878cd…` | Sports / Tennis | 849 | 2.2886 | 2.2669 | 4.75 | 0.648 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 108 | 6.7828 | 5.7787 | 2.81 | 0.13 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 108 | 6.7828 | 5.7787 | 2.81 | 0.13 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 90 | 7.5731 | 6.2874 | 3.05 | 0.4 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6174 | 2.81 | 0.636 |
| `0x1941ca5d…` | Sports / Other sport | 2905 | 1.0417 | 1.0415 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2905 | 1.0417 | 1.0415 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports | 2907 | 1.041 | 1.0408 | 2.63 | 0.549 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7934 | 2.57 | 0.129 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9737 | 2.51 | 0.519 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.4796 | 2.64 | 0.31 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6124 | 2.86 | 0.07 |
| `0xef185339…` | Sports | 3857 | 0.732 | 0.732 | 22.79 | 0.69 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.8028 | 2.13 | 0.183 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 161 | 3.901 | 3.5214 | 2.68 | 0.112 |
| `0x86c878cd…` | Sports / Tennis / WTA | 200 | 3.3218 | 3.142 | 2.73 | 0.665 |
| `0x13997bdb…` | Sports | 4167 | 0.6768 | 0.6768 | 22.58 | 0.683 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 92 | 5.3041 | 4.4402 | 2.38 | 0.13 |
| `0xd60c6fa3…` | Sports | 3597 | 0.6849 | 0.6849 | 20.9 | 0.684 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1706 | 2.41 | 0.526 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 113 | 4.4868 | 3.8633 | 2.83 | 0.531 |
| `0xb209ec04…` | Sports | 1608 | 1.023 | 1.0236 | 4.63 | 0.516 |
| `0xb209ec04…` | Sports / Soccer | 896 | 1.375 | 1.3683 | 4.03 | 0.512 |
| `0x33ae5c5d…` | Sports / price=0.00-0.10 | 263 | 2.6863 | 2.5161 | 3.32 | 0.43 |
| `0x1941ca5d…` | Sports / Other sport / live | 2207 | 0.8672 | 0.8685 | 3.34 | 0.593 |
| `0xb209ec04…` | Esports / Esports / live | 969 | 1.3076 | 1.3029 | 3.76 | 0.507 |
| `0xb209ec04…` | Sports / Soccer / live | 618 | 1.6434 | 1.6255 | 3.4 | 0.479 |
| `0xb209ec04…` | Esports | 1225 | 1.1398 | 1.1387 | 4.05 | 0.5 |
| `0xb209ec04…` | Esports / Esports | 1225 | 1.1398 | 1.1387 | 4.05 | 0.5 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1050 | 1.2243 | 1.2151 | 17.43 | 0.601 |
| `0xb209ec04…` | Esports / Esports / Valorant | 199 | 2.9053 | 2.7379 | 2.41 | 0.482 |
| `0x4afbb658…` | Sports | 167 | 3.1326 | 2.9666 | 2.38 | 0.419 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 366 | 2.047 | 1.9622 | 3.26 | 0.281 |
| `0x86c878cd…` | Sports / Tennis / ATP | 404 | 1.883 | 1.8576 | 3.11 | 0.626 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 370 | 2.0141 | 1.9318 | 3.24 | 0.278 |
| `0x80cd8310…` | Crypto / Ethereum / price=0.00-0.10 | 105 | 4.2204 | 3.6159 | 2.05 | 0.105 |
| `0x13997bdb…` | Sports / Soccer | 2906 | 0.6832 | 0.6832 | 18.53 | 0.687 |
| `0x13997bdb…` | Sports / Soccer / live | 2864 | 0.6863 | 0.6862 | 18.38 | 0.686 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 906 | 1.2306 | 1.2188 | 16.19 | 0.594 |
| `0xef185339…` | Sports / Soccer | 2601 | 0.7047 | 0.7049 | 18.92 | 0.689 |
| `0xef185339…` | Sports / Soccer / live | 2567 | 0.705 | 0.7052 | 18.73 | 0.687 |
| `0x13997bdb…` | Sports / price=0.10-0.30 | 1156 | 1.0466 | 1.0403 | 16.4 | 0.566 |
| `0x6b60d61e…` | Sports / price=0.00-0.10 | 105 | 3.9888 | 3.3988 | 2.64 | 0.524 |
| `0xc9ccb64f…` | Sports / Soccer / price=0.00-0.10 | 71 | 5.1089 | 4.0609 | 2.44 | 0.521 |
| `0xd60c6fa3…` | Sports / Soccer | 2432 | 0.6863 | 0.6863 | 16.54 | 0.684 |
