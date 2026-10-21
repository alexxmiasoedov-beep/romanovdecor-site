# Отчёт воронки, 2026-10-21 07:02 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 57135 |
| 0. Из них не только 5-мин крипта | 55110 |
| 1. Прошли дешёвые отсечки | 4183 из 18880 |
| 2. Прошли по полной истории | 5 + сегментом 47 из 4183 |
| 3. Прошли реалистичный вход | 5 из 52 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 9091 |
| closed<50 | 7893 |
| top1_concentration | 6478 |
| entries>=0.90 | 3875 |
| history<90d | 3533 |
| short_crypto | 1373 |
| open_now>10 | 1138 |
| profit_from<0.10 | 911 |
| positions>5000 | 24 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3811 |
| concurrency_p95>8 | 3322 |
| drawdown | 3182 |
| unstable_halves | 2749 |
| roi_copy<=0 | 1604 |
| silent | 752 |
| low_liquidity | 627 |
| both_sides | 556 |
| top1_concentration | 295 |
| history<90d | 285 |
| closed<50 | 249 |
| hold<1h | 173 |
| entries>=0.90 | 141 |
| short_crypto | 95 |
| profit_from<0.10 | 46 |
| segment_only:t<2.0 | 45 |
| sniping | 38 |
| segment_only:drawdown | 36 |
| segment_only:unstable_halves | 22 |
| segment_only:roi_copy<=0 | 10 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 43 |
| edge_decays_with_delay | 4 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x27b3ccddae0cb2bcfb6ce52c545f0e182904183d` | 1020004 | Sports | 0.2544 | 1.89 | 0.2074 | 0.2185 | 0.2676 | 1.0 | 10.84 | н/д | Sports / price=0.30-0.50 (n=34, roi=+0.37) |
| `0x239ef5c5c7ebcb8385a85da06d973c47e882ef98` | kusok | Sports | 0.2585 | 2.2 | 0.1305 | 0.1398 | 0.2592 | 4.0 | 19.45 | н/д | Sports / Basketball / NBA 2026 (n=45, roi=+0.54) | Sports (n=121, roi=+0.29) | Sports / Basketball (n=53, roi=+0.44) | Sports / Basketball / pre (n=53, roi=+0.44) | Sports / Basketball / type=moneyline (n=49, roi=+0.41) | Sports / price=0.50-0.70 (n=46, roi=+0.25) |
| `0x4ebff032ca2b58e4e03ee413b361f829c1b8d10d` | getdragon | Sports | 0.2104 | 1.54 | 0.1337 | 0.1369 | 0.1093 | 8.0 | 60.78 | 0.0 | Sports / Soccer / type=moneyline (n=39, roi=+0.30) |
| `0xb228951bb2a0995fef1a01a03092cbc3becfc358` | 0xB228951bb2a0995Fef1a01a03092cBc3beCFc358-1768599868142 | Sports | 0.0353 | 1.25 | 0.054 | 0.0646 | 0.0608 | 4.0 | 5.53 | н/д | Sports / Basketball (n=86, roi=+0.08) | Sports / Basketball / NBA 2026 (n=86, roi=+0.08) | Sports / Basketball / type=moneyline (n=86, roi=+0.08) | Sports / Basketball / pre (n=58, roi=+0.07) | Sports / Basketball / price=0.70-0.90 (n=47, roi=+0.08) |
| `0x5e89386d743b166016521775dc5a127189e8bb0c` | Amir1966 | Sports | 0.0516 | 0.49 | 0.0249 | 0.0489 | 0.1028 | 3.0 | 9.64 | н/д | Sports / Soccer / FIFA World Cup (n=53, roi=+0.18) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x27b3ccddae0cb2bcfb6ce52c545f0e182904183d` | 1020004 | 0.2544 | Sports / price=0.30-0.50 (n=34, roi=+0.37) | segment_only:t<2.0 |
| `0x4ebff032ca2b58e4e03ee413b361f829c1b8d10d` | getdragon | 0.2104 | Sports / Soccer / type=moneyline (n=39, roi=+0.30) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0584 | Sports / Soccer / price=0.50-0.70 (n=64, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0607 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9d00ccafd0e2ef61e962c8102036b4528bc75d52` | luebos1 | 0.1102 | Sports / Tennis (n=33, roi=+0.26) | Sports / Tennis / type=moneyline (n=33, roi=+0.26) | Sports / Tennis / live (n=32, roi=+0.26) | segment_only:t<2.0 |
| `0xb228951bb2a0995fef1a01a03092cbc3becfc358` | 0xB228951bb2a0995Fef1a01a03092cBc3beCFc358-1768599868142 | 0.0353 | Sports / Basketball (n=86, roi=+0.08) | Sports / Basketball / NBA 2026 (n=86, roi=+0.08) | Sports / Basketball / type=moneyline (n=86, roi=+0.08) | Sports / Basketball / pre (n=58, roi=+0.07) | Sports / Basketball / price=0.70-0.90 (n=47, roi=+0.08) | segment_only:t<2.0 |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0457 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca14f80a6daec5144052ee31403c01111cd85915` | 0xcA14F80a6dAeC5144052eE31403C01111CD85915-1772987358266 | 0.0747 | Sports / price=0.30-0.50 (n=32, roi=+0.39) | Sports / Tennis / live (n=35, roi=+0.28) | Sports / Tennis (n=40, roi=+0.20) | Sports / Tennis / type=moneyline (n=40, roi=+0.20) | segment_only:t<2.0 |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0963 | Esports / Esports / Valorant (n=55, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1554 | Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / type=child_moneyline (n=614, roi=+0.18) | Esports (n=712, roi=+0.16) | Esports / Esports (n=712, roi=+0.16) | Esports / Esports / Dota 2 (n=712, roi=+0.16) | segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5e89386d743b166016521775dc5a127189e8bb0c` | Amir1966 | 0.0516 | Sports / Soccer / FIFA World Cup (n=53, roi=+0.18) | segment_only:t<2.0 |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0106 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0165 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0076 | Sports / Soccer / price=0.50-0.70 (n=60, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0007 | Sports / Soccer / pre (n=40, roi=+0.23) | Sports / Soccer (n=41, roi=+0.21) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | -0.0022 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0027 | Sports / Other sport / price=0.70-0.90 (n=67, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa236024a7acfc8f32f850ba72b68664ed1564cbb` | ganzarolli | 0.0005 | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.11) | Sports / price=0.70-0.90 (n=73, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0219 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0356 | Sports / price=0.30-0.50 (n=96, roi=+0.24) | Sports / Tennis / price=0.30-0.50 (n=39, roi=+0.30) | Sports / Basketball / type=moneyline (n=34, roi=+0.22) | Sports / Basketball (n=37, roi=+0.18) | Sports / Basketball / live (n=32, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0086 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.011 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x67a8dd1c146d6ac9e5d220dba3985c9676feb281` | santacar | 0.0171 | Sports / Soccer / type=moneyline (n=100, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0136 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x15366fec3c72731622619329ec93a0474b5a3ca5` | Peach-ATP | 0.0137 | Sports / Soccer / price=0.70-0.90 (n=35, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1352 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0x2910f8ba835a9db6bec4aabcf342fde67d00faef` | Kass1xamm | 0.0706 | Sports / Soccer / live (n=32, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0412 | Esports / price=0.50-0.70 (n=47, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0 |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0528 | Sports / American Football / pre (n=57, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x880dbf161120207d47aef05ec774b331bcec39bc` | akulaxl | 0.0242 | Esports / Esports / type=moneyline (n=53, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9cbb674bdacc27020e6adb549461e45ade24a2e1` | Tentm1 | 0.0346 | Sports / American Football / NFL (n=41, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c68066fe7466ad3048a4adff9ad18cfecdab7b` | lucianow34 | 0.0253 | Esports / price=0.50-0.70 (n=450, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=450, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0xe3ca22c1bb6f3b637a9baff915d363422f945ed4` | Rubadub | 0.0285 | Sports / Soccer / Serie A 2025 (n=33, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe0b01fa337f48b3792ae9e76f3665bfc4f3a5294` | tnns1 | 0.0126 | Sports / Tennis / WTA (n=139, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x228090cc64ff9dfb8173ac5c46f4c60b9e2531cb` | 0x228090Cc64Ff9dfB8173AC5c46f4c60b9E2531cB-1769517977854 | 0.0343 | Esports / Esports / live (n=167, roi=+0.15) | Esports / Esports / type=moneyline (n=92, roi=+0.19) | Esports / Esports / Counter Strike (n=176, roi=+0.13) | Esports (n=180, roi=+0.13) | Esports / Esports (n=180, roi=+0.13) | Crypto / price=0.70-0.90 (n=57, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0x173e8a681812cee182c8cc8041f8027b647f9ff4` | 0x50f161F7CD7aE6A7Df8E6E9a7A475EFa20f3e3b1-1757699966720 | 0.0584 | Esports / Esports / type=moneyline (n=127, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1d169955b78ad2885e725717e5928eec33c9212e` | HONGKONGPEACH | 0.0453 | Sports / Basketball (n=43, roi=+0.24) | Sports / Soccer / price=0.50-0.70 (n=51, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x239ef5c5c7ebcb8385a85da06d973c47e882ef98` | kusok | Sports | 126 | 0.2585 | 0.1382 | 2.2 | 0.579 | 4.0 | 19.45 | 1017106 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0xd670301420f6011e8136b07c50d7f4002bcee98f` | Mrpitter | Culture | 90 | 0.5276 | 0.1197 | 2.03 | 0.544 | 8.0 | 23.31 | 70640 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 785 | 0.1139 | 0.0515 | 3.44 | 0.713 | 8.0 | 2.72 | 396955 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1459 | 0.2391 | 0.0404 | 6.19 | 0.552 | 8.0 | 2.41 | 58320 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 253 | 23.3322 | 21.9008 | 4.03 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0746 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0526 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1517 | 4.3147 | 4.3079 | 4.37 | 0.709 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8811 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 99 | 14.9322 | 12.9026 | 4.12 | 0.182 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2882 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7656 | 4.16 | 0.626 |
| `0x31121402…` | Sports / price=0.00-0.10 | 94 | 14.9574 | 12.3792 | 3.94 | 0.16 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1041 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 552 | 4.2226 | 4.2076 | 5.87 | 0.719 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7078 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3936 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3936 | 3.78 | 0.177 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 810 | 3.3971 | 3.3398 | 2.39 | 0.221 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 811 | 3.3923 | 3.3351 | 2.39 | 0.221 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8154 | 3.23 | 0.167 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2136 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 248 | 5.5103 | 5.1798 | 3.98 | 0.137 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4807 | 3.61 | 0.17 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6102 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6102 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4412 | 3.33 | 0.754 |
| `0xeda67a7f…` | Sports | 498 | 3.2023 | 3.189 | 4.17 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3378 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 768 | 2.4598 | 2.4316 | 4.63 | 0.659 |
| `0x86c878cd…` | Sports | 2299 | 1.3962 | 1.3958 | 6.34 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 848 | 2.2912 | 2.2695 | 4.75 | 0.647 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 85 | 8.0483 | 6.6152 | 3.08 | 0.412 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8325 | 2.82 | 0.131 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8325 | 2.82 | 0.131 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5502 | 2.28 | 0.167 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6202 | 2.81 | 0.636 |
| `0x1941ca5d…` | Sports / Other sport | 2918 | 1.0378 | 1.0376 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2918 | 1.0378 | 1.0376 | 2.63 | 0.549 |
| `0x1941ca5d…` | Sports | 2920 | 1.0372 | 1.037 | 2.63 | 0.549 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7943 | 2.57 | 0.129 |
| `0xe9f5c75e…` | Sports / Basketball / live | 464 | 2.5019 | 2.4329 | 4.19 | 0.621 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 62 | 8.6662 | 6.6473 | 3.13 | 0.242 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1369 | 2.16 | 0.156 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9751 | 2.51 | 0.519 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.48 | 2.64 | 0.31 |
| `0xe8ca3f75…` | Esports / Esports / live | 149 | 3.9107 | 3.8967 | 2.82 | 0.57 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6124 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 458 | 2.0644 | 2.1367 | 4.28 | 0.657 |
| `0xe8ca3f75…` | Esports / Esports | 458 | 2.0644 | 2.1367 | 4.28 | 0.657 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 160 | 3.9316 | 3.5471 | 2.68 | 0.113 |
| `0x86c878cd…` | Sports / Tennis / WTA | 200 | 3.3218 | 3.1424 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0221 | 5.01 | 0.567 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5268 | 4.77 | 0.568 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7249 | 4.71 | 0.561 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 92 | 5.3041 | 4.4411 | 2.38 | 0.13 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 110 | 4.6364 | 3.9774 | 2.85 | 0.545 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7718 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 432 | 1.9129 | 1.9961 | 4.77 | 0.766 |
| `0xb209ec04…` | Sports | 1588 | 1.038 | 1.0385 | 4.64 | 0.516 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1722 | 2.41 | 0.526 |
| `0xb209ec04…` | Sports / Soccer | 893 | 1.3768 | 1.3703 | 4.02 | 0.511 |
| `0x1941ca5d…` | Sports / Other sport / live | 2218 | 0.8615 | 0.8629 | 3.34 | 0.592 |
| `0xb209ec04…` | Esports / Esports / live | 968 | 1.3078 | 1.3033 | 3.76 | 0.506 |
