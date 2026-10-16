# Отчёт воронки, 2026-10-16 07:27 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 56545 |
| 0. Из них не только 5-мин крипта | 54335 |
| 1. Прошли дешёвые отсечки | 4344 из 15840 |
| 2. Прошли по полной истории | 6 + сегментом 53 из 4344 |
| 3. Прошли реалистичный вход | 5 из 59 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 7102 |
| closed<50 | 6735 |
| top1_concentration | 5502 |
| entries>=0.90 | 2966 |
| history<90d | 2922 |
| short_crypto | 1031 |
| profit_from<0.10 | 676 |
| open_now>10 | 595 |
| positions>5000 | 14 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3926 |
| concurrency_p95>8 | 3404 |
| drawdown | 3323 |
| unstable_halves | 2843 |
| roi_copy<=0 | 1700 |
| silent | 742 |
| low_liquidity | 647 |
| both_sides | 614 |
| top1_concentration | 323 |
| history<90d | 289 |
| closed<50 | 268 |
| hold<1h | 166 |
| entries>=0.90 | 153 |
| short_crypto | 86 |
| segment_only:t<2.0 | 50 |
| profit_from<0.10 | 49 |
| sniping | 44 |
| segment_only:drawdown | 43 |
| segment_only:unstable_halves | 27 |
| segment_only:roi_copy<=0 | 8 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 48 |
| edge_decays_with_delay | 6 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x49bceb9fa38ae72bf16d645b12c9dc76c7348e3c` | casituancui | Sports | 0.2201 | 3.06 | 0.1895 | 0.1909 | 0.1948 | 8.0 | 7.67 | н/д | Sports / Soccer / FIFA World Cup (n=130, roi=+0.23) | Sports (n=155, roi=+0.21) | Sports / Soccer (n=155, roi=+0.21) | Sports / price=0.50-0.70 (n=86, roi=+0.26) | Sports / Soccer / price=0.50-0.70 (n=86, roi=+0.26) | Sports / Soccer / pre (n=140, roi=+0.19) |
| `0xe4cbe31ee2fbe6a98946e20b9c964e3ea9bfea19` | 0xE4cBe31eE2fBE6a98946E20b9C964E3ea9BFea19-1771289534227 | Sports | 0.1069 | 2.33 | 0.1273 | 0.1379 | 0.1166 | 2.0 | 4.09 | 0.0 | Sports / price=0.70-0.90 (n=37, roi=+0.15) | Sports (n=60, roi=+0.11) |
| `0x1e52bbdf389526f57abc62641d518868f4c5eb43` | dsasdaas | Esports | 0.1669 | 2.36 | 0.083 | 0.0973 | 0.1846 | 6.0 | 2.29 | н/д | Esports (n=170, roi=+0.21) | Esports / Esports (n=169, roi=+0.21) | Esports / Esports / pre (n=56, roi=+0.36) | Esports / Esports / Counter Strike (n=129, roi=+0.20) | Esports / price=0.30-0.50 (n=41, roi=+0.35) | Esports / Esports / price=0.30-0.50 (n=41, roi=+0.35) |
| `0x725b01530fac8233c73596b864026cd80a64f26b` |  | Sports | 0.1144 | 1.25 | 0.087 | 0.098 | 0.1556 | 6.0 | 12.57 | 0.0 | Sports / Soccer / type=moneyline (n=48, roi=+0.17) |
| `0xa00bf96e28b156b1b14617ca9bd0431328e0eae1` | pitochico | Esports | 0.182 | 1.33 | 0.0339 | 0.0054 | 0.0745 | 3.0 | 4.7 | н/д | Esports (n=85, roi=+0.31) | Esports / Esports (n=85, roi=+0.31) | Esports / Esports / League of Legends (n=85, roi=+0.31) | Esports / Esports / type=moneyline (n=85, roi=+0.31) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0662 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0563 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x725b01530fac8233c73596b864026cd80a64f26b` |  | 0.1144 | Sports / Soccer / type=moneyline (n=48, roi=+0.17) | segment_only:t<2.0 |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.0833 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0xb0e3fcbe0d7f17168fdce93f89c0168d3fa329eb` | gagarin59 | 0.0992 | Sports / price=0.50-0.70 (n=48, roi=+0.21) | segment_only:t<2.0 |
| `0x93159a717f382318a7dbed96cfc4d61ab6a3afc1` |  | 0.0519 | Sports / Soccer / Club Friendlies (n=32, roi=+0.15) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1576 | Esports / price=0.10-0.30 (n=110, roi=+0.50) | Esports / Esports / price=0.10-0.30 (n=110, roi=+0.50) | Esports / Esports / type=child_moneyline (n=599, roi=+0.18) | Esports (n=696, roi=+0.16) | Esports / Esports (n=696, roi=+0.16) | Esports / Esports / Dota 2 (n=696, roi=+0.16) | segment_only:drawdown |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0552 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0947 | Esports / Esports / Valorant (n=51, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0xa00bf96e28b156b1b14617ca9bd0431328e0eae1` | pitochico | 0.182 | Esports (n=85, roi=+0.31) | Esports / Esports (n=85, roi=+0.31) | Esports / Esports / League of Legends (n=85, roi=+0.31) | Esports / Esports / type=moneyline (n=85, roi=+0.31) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0177 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0267 | Sports (n=92, roi=+0.07) | Sports / Soccer / Counter Strike (n=36, roi=+0.09) | Sports / price=0.70-0.90 (n=66, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6359c6166737be02eb0103d938c893493818f32f` | Gqjbvaod | 0.0403 | Sports (n=55, roi=+0.16) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0144 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0087 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xce041dc32d338cf0a44d7a1b860e793fbdd0dbf6` |  | -0.009 | Sports / price=0.70-0.90 (n=43, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0037 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=142, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0095 | Sports / Other sport / price=0.70-0.90 (n=48, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.0189 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0087 | Sports / Soccer / pre (n=182, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=161, roi=+0.09) | Sports / price=0.70-0.90 (n=190, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0292 | Sports / American Football (n=163, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.0085 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0438 | Sports / Basketball / price=0.50-0.70 (n=33, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0162 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0121 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0174 | Esports / price=0.50-0.70 (n=46, roi=+0.17) | Esports / Esports / price=0.50-0.70 (n=46, roi=+0.17) | segment_only:t<2.0 |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0281 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x332d40ed4b0cb313059f4fc037dbe520bf2f7b0e` | NJ100DOLLAR | 0.0129 | Sports / Soccer / type=moneyline (n=236, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x45361ff76a9308998703e0acb658691eca9af41b` | russeN1 | 0.035 | Esports / price=0.30-0.50 (n=76, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=76, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1352 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0567 | Sports / American Football / pre (n=53, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbcf51140fd48e69c6e6d4bd09d38a629059856a1` | bqy0301 | 0.2005 | Sports / price=0.30-0.50 (n=36, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0xffe290a74a57db36b06cc88692b16f1cda322957` | sfst | 0.0362 | Sports / price=0.50-0.70 (n=30, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.0817 | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | Sports / Soccer (n=370, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c68066fe7466ad3048a4adff9ad18cfecdab7b` | lucianow34 | 0.0258 | Esports / price=0.50-0.70 (n=448, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=448, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0xc755231db154c8c6a7ee63413a2655781eb17c5d` | FGMYT | 0.0577 | Sports / Baseball / live (n=37, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xeef382e6c8cb7adde63551043659b381b1c00547` | xiaomikang | 0.048 | Esports / price=0.10-0.30 (n=42, roi=+0.45) | Esports / Esports / price=0.10-0.30 (n=42, roi=+0.45) | Esports / Esports / type=child_moneyline (n=228, roi=+0.18) | Esports (n=318, roi=+0.15) | Esports / Esports (n=318, roi=+0.15) | Esports / Esports / League of Legends (n=310, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x1d169955b78ad2885e725717e5928eec33c9212e` | HONGKONGPEACH | 0.0519 | Sports / Basketball (n=39, roi=+0.24) | Sports / Soccer / price=0.50-0.70 (n=47, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x5e5175106a7dbbd92b10f1b56458fc8c1bdd42ce` | 0x5E5175106a7Dbbd92B10f1b56458Fc8c1Bdd42ce-1730865746538 | 0.0488 | Esports / price=0.30-0.50 (n=131, roi=+0.24) | Esports / Esports / price=0.30-0.50 (n=131, roi=+0.24) | Esports / Esports / live (n=421, roi=+0.12) | Esports / Esports / type=moneyline (n=124, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x49bceb9fa38ae72bf16d645b12c9dc76c7348e3c` | casituancui | Sports | 178 | 0.2201 | 0.1814 | 3.06 | 0.663 | 8.0 | 7.67 | 4637287 | прошёл |
| `0xe4cbe31ee2fbe6a98946e20b9c964e3ea9bfea19` | 0xE4cBe31eE2fBE6a98946E20b9C964E3ea9BFea19-1771289534227 | Sports | 60 | 0.1069 | 0.1438 | 2.33 | 0.917 | 2.0 | 4.09 | 256427 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0x1e52bbdf389526f57abc62641d518868f4c5eb43` | dsasdaas | Esports | 186 | 0.1669 | 0.1124 | 2.36 | 0.672 | 6.0 | 2.29 | 602454 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 759 | 0.1184 | 0.0554 | 3.5 | 0.715 | 8.0 | 2.74 | 401911 | edge_decays_with_delay |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1391 | 0.2447 | 0.0463 | 6.18 | 0.563 | 8.0 | 2.54 | 55874 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 253 | 23.3322 | 21.9014 | 4.03 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0762 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0534 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1513 | 4.3261 | 4.3193 | 4.37 | 0.71 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8831 | 5.01 | 0.351 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2894 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7673 | 4.16 | 0.626 |
| `0x31121402…` | Sports / price=0.00-0.10 | 93 | 14.233 | 11.7557 | 3.82 | 0.161 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1043 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 552 | 4.2226 | 4.2079 | 5.87 | 0.719 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7079 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3939 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3939 | 3.78 | 0.177 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9624 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9624 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8091 | 3.23 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 814 | 2.9622 | 2.9127 | 2.21 | 0.222 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 815 | 2.9579 | 2.9086 | 2.21 | 0.222 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2149 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 247 | 5.5366 | 5.2031 | 3.98 | 0.138 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4809 | 3.61 | 0.17 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6124 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6124 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4425 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3385 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 763 | 2.4757 | 2.4472 | 4.63 | 0.661 |
| `0x86c878cd…` | Sports | 2286 | 1.4037 | 1.4033 | 6.33 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 842 | 2.3072 | 2.2852 | 4.75 | 0.648 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.8031 | 3.06 | 0.279 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 106 | 6.7699 | 5.7517 | 2.76 | 0.123 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 106 | 6.7699 | 5.7517 | 2.76 | 0.123 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6209 | 2.81 | 0.636 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7961 | 2.57 | 0.129 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3861 | 2.85 | 0.269 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 57 | 9.2715 | 6.9975 | 2.73 | 0.456 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.4358 | 4.18 | 0.62 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 62 | 8.6662 | 6.6489 | 3.13 | 0.242 |
| `0x1941ca5d…` | Sports / Other sport | 2931 | 0.9157 | 0.9156 | 2.46 | 0.547 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2931 | 0.9157 | 0.9156 | 2.46 | 0.547 |
| `0x1941ca5d…` | Sports | 2933 | 0.9152 | 0.9151 | 2.46 | 0.547 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8614 | 2.71 | 0.206 |
| `0xe8ca3f75…` | Esports / Esports / live | 149 | 3.9107 | 3.8978 | 2.82 | 0.57 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6121 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 456 | 2.0622 | 2.1353 | 4.25 | 0.656 |
| `0xe8ca3f75…` | Esports / Esports | 456 | 2.0622 | 2.1353 | 4.25 | 0.656 |
| `0xef185339…` | Sports | 3846 | 0.7295 | 0.7295 | 22.68 | 0.691 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1855 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0257 | 5.01 | 0.567 |
| `0x41558102…` | Sports / price=0.00-0.10 | 41 | 9.9583 | 6.7976 | 2.42 | 0.293 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5297 | 4.77 | 0.568 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7278 | 4.71 | 0.561 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7743 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 432 | 1.9129 | 1.9965 | 4.77 | 0.766 |
| `0xb209ec04…` | Sports | 1582 | 1.0416 | 1.0421 | 4.64 | 0.517 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1725 | 2.41 | 0.526 |
| `0xb209ec04…` | Sports / Soccer | 888 | 1.3829 | 1.3763 | 4.01 | 0.511 |
| `0xb209ec04…` | Esports / Esports / live | 967 | 1.308 | 1.3034 | 3.76 | 0.506 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.628 | 3.4 | 0.478 |
| `0xb209ec04…` | Esports | 1223 | 1.1398 | 1.1389 | 4.05 | 0.5 |
| `0xb209ec04…` | Esports / Esports | 1223 | 1.1398 | 1.1389 | 4.05 | 0.5 |
