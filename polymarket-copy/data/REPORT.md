# Отчёт воронки, 2026-10-14 07:24 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 54789 |
| 0. Из них не только 5-мин крипта | 52556 |
| 1. Прошли дешёвые отсечки | 4127 из 27573 |
| 2. Прошли по полной истории | 1 + сегментом 61 из 4127 |
| 3. Прошли реалистичный вход | 7 из 62 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 13923 |
| closed<50 | 12096 |
| top1_concentration | 10746 |
| entries>=0.90 | 5716 |
| history<90d | 4681 |
| open_now>10 | 3526 |
| profit_from<0.10 | 1975 |
| short_crypto | 1897 |
| positions>5000 | 146 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3722 |
| concurrency_p95>8 | 3267 |
| drawdown | 3160 |
| unstable_halves | 2701 |
| roi_copy<=0 | 1627 |
| silent | 742 |
| low_liquidity | 637 |
| both_sides | 596 |
| top1_concentration | 308 |
| history<90d | 305 |
| closed<50 | 234 |
| hold<1h | 175 |
| entries>=0.90 | 146 |
| short_crypto | 87 |
| segment_only:t<2.0 | 57 |
| sniping | 54 |
| profit_from<0.10 | 53 |
| segment_only:drawdown | 47 |
| segment_only:unstable_halves | 34 |
| segment_only:roi_copy<=0 | 12 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 50 |
| edge_decays_with_delay | 5 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xf12b68709f37d769ca0a7b088020c053653beb45` | shinahan9 | Sports | 0.1123 | 1.51 | 0.0821 | 0.0971 | 0.1496 | 5.0 | 3.9 | н/д | Sports / Baseball (n=165, roi=+0.16) | Sports / Baseball / MLB (n=165, roi=+0.16) | Sports / Baseball / type=moneyline (n=165, roi=+0.16) |
| `0xf4435bf20e74ce1264951578e921e8d0ed0d1ea1` | zp8269 | Sports | 0.0886 | 1.01 | 0.0455 | 0.0559 | 0.0547 | 8.0 | 7.66 | н/д | Sports / Soccer (n=41, roi=+0.26) | Sports / Soccer / type=moneyline (n=31, roi=+0.26) | Sports / Soccer / pre (n=38, roi=+0.21) |
| `0x9246043ac062d160f1c8ee96872a3ccb2db59195` | 0x9246043AC062D160F1C8ee96872a3CCB2DB59195-1775834612409 | Sports | 0.0412 | 1.23 | 0.0435 | 0.087 | 0.0758 | 7.0 | 2.64 | н/д | Sports (n=187, roi=+0.10) | Sports / Soccer (n=138, roi=+0.10) | Sports / Soccer / type=moneyline (n=90, roi=+0.12) | Sports / price=0.50-0.70 (n=55, roi=+0.15) | Sports / Soccer / Premier League 2025 (n=38, roi=+0.17) | Sports / Soccer / price=0.50-0.70 (n=42, roi=+0.16) |
| `0x7757dca90c06ec501920344ee50d51764ae6120c` | 0x7757DcA90c06EC501920344EE50D51764Ae6120c-1766094952612 | Sports | 0.0474 | 1.11 | 0.0364 | 0.0522 | 0.0658 | 3.0 | 3.71 | н/д | Sports / Soccer / pre (n=57, roi=+0.14) |
| `0x622930bc54cfa884faac757fb8302b1b8ff10081` | demidovich | Sports | 0.0738 | 0.93 | 0.0331 | 0.0356 | 0.0567 | 4.0 | 3.59 | н/д | Sports / Soccer / pre (n=76, roi=+0.17) | Sports / price=0.50-0.70 (n=40, roi=+0.20) | Sports / Soccer / price=0.50-0.70 (n=39, roi=+0.19) |
| `0x30b71da3a01edcd3c3e5e2430048d80948ca1fb7` | uty76 | Sports | 0.0556 | 1.24 | 0.0866 | 0.0923 | 0.1112 | 6.0 | 4.56 | н/д | Sports / price=0.50-0.70 (n=43, roi=+0.17) | Sports / Tennis / price=0.70-0.90 (n=43, roi=+0.11) |
| `0xb7db546b96b94a2262c65baee257fbdc10a14019` | 0xB7db546B96b94A2262c65baEE257fbDc10a14019-1777909240541 | Sports | 0.0242 | 0.44 | 0.0293 | 0.0406 | 0.0201 | 5.0 | 2.25 | 0.0 | Sports / Tennis / live (n=37, roi=+0.11) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x83aff046e16309ef06ae86253a5adf13ea0b4084` | Hollow0329 | 0.1666 | Esports / price=0.50-0.70 (n=31, roi=+0.24) | Esports / Esports / price=0.50-0.70 (n=31, roi=+0.24) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0554 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.0397 | Sports / price=0.50-0.70 (n=100, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf12b68709f37d769ca0a7b088020c053653beb45` | shinahan9 | 0.1123 | Sports / Baseball (n=165, roi=+0.16) | Sports / Baseball / MLB (n=165, roi=+0.16) | Sports / Baseball / type=moneyline (n=165, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.085 | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0447 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1628 | Esports / price=0.10-0.30 (n=104, roi=+0.54) | Esports / Esports / price=0.10-0.30 (n=104, roi=+0.54) | Esports / Esports / type=child_moneyline (n=583, roi=+0.18) | Esports (n=677, roi=+0.16) | Esports / Esports (n=677, roi=+0.16) | Esports / Esports / Dota 2 (n=677, roi=+0.16) | segment_only:drawdown |
| `0x89879980a13fb82269cc489154fafbad8241d5b9` | soocas | 0.0611 | Esports / price=0.70-0.90 (n=43, roi=+0.11) | Esports / Esports / price=0.70-0.90 (n=43, roi=+0.11) | segment_only:t<2.0 |
| `0xf4435bf20e74ce1264951578e921e8d0ed0d1ea1` | zp8269 | 0.0886 | Sports / Soccer (n=41, roi=+0.26) | Sports / Soccer / type=moneyline (n=31, roi=+0.26) | Sports / Soccer / pre (n=38, roi=+0.21) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x9246043ac062d160f1c8ee96872a3ccb2db59195` | 0x9246043AC062D160F1C8ee96872a3CCB2DB59195-1775834612409 | 0.0412 | Sports (n=187, roi=+0.10) | Sports / Soccer (n=138, roi=+0.10) | Sports / Soccer / type=moneyline (n=90, roi=+0.12) | Sports / price=0.50-0.70 (n=55, roi=+0.15) | Sports / Soccer / Premier League 2025 (n=38, roi=+0.17) | Sports / Soccer / price=0.50-0.70 (n=42, roi=+0.16) | segment_only:t<2.0 |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0536 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x7757dca90c06ec501920344ee50d51764ae6120c` | 0x7757DcA90c06EC501920344EE50D51764Ae6120c-1766094952612 | 0.0474 | Sports / Soccer / pre (n=57, roi=+0.14) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd4f4ee5f2e93d503e5a1a0cbb5495586fd05bb68` | Auagmg | 0.0332 | Sports / price=0.70-0.90 (n=52, roi=+0.08) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0756 | Sports / Soccer / type=moneyline (n=52, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x622930bc54cfa884faac757fb8302b1b8ff10081` | demidovich | 0.0738 | Sports / Soccer / pre (n=76, roi=+0.17) | Sports / price=0.50-0.70 (n=40, roi=+0.20) | Sports / Soccer / price=0.50-0.70 (n=39, roi=+0.19) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0577 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=73, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0x30b71da3a01edcd3c3e5e2430048d80948ca1fb7` | uty76 | 0.0556 | Sports / price=0.50-0.70 (n=43, roi=+0.17) | Sports / Tennis / price=0.70-0.90 (n=43, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0158 | Sports / price=0.50-0.70 (n=170, roi=+0.09) | Sports / Soccer / price=0.50-0.70 (n=54, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0246 | Sports (n=92, roi=+0.07) | Sports / Soccer / Counter Strike (n=36, roi=+0.09) | Sports / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0863 | Esports / Esports / Valorant (n=51, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0087 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xfe37cfb53702f9d85ce5b04b516e000268ed911d` | mmsee26 | -0.0115 | Sports / price=0.70-0.90 (n=101, roi=+0.05) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0xce041dc32d338cf0a44d7a1b860e793fbdd0dbf6` |  | -0.0087 | Sports / price=0.70-0.90 (n=41, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0137 | Sports / Other sport / price=0.70-0.90 (n=48, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c5a66321fd29406669f00391b6689e6d80bf75` | FrankCastro21 | -0.0096 | Esports / Esports / Dota 2 (n=34, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0033 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=142, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=66, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x75e04cc2fff48a555afc5415053b2ac2636f5c67` | MOCKBA | 0.0516 | Sports / Other sport / Elon Tweets (n=36, roi=+0.19) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0145 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa0e16dbb5456cdd0c17c83b622178f20d932ba6d` | sunxiaochuan278 | 0.004 | Esports / Esports / Counter Strike (n=37, roi=+0.04) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0108 | Sports / Soccer / pre (n=176, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=154, roi=+0.09) | Sports / price=0.70-0.90 (n=183, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xb7db546b96b94a2262c65baee257fbdc10a14019` | 0xB7db546B96b94A2262c65baEE257fbDc10a14019-1777909240541 | 0.0242 | Sports / Tennis / live (n=37, roi=+0.11) | segment_only:t<2.0 |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.0139 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0173 | Esports / price=0.50-0.70 (n=47, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | 0.0202 | Sports / American Football / CFB 2026 (n=40, roi=+0.09) | Sports / American Football / live (n=32, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0361 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x45361ff76a9308998703e0acb658691eca9af41b` | russeN1 | 0.0668 | Esports / price=0.30-0.50 (n=69, roi=+0.26) | Esports / Esports / price=0.30-0.50 (n=69, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 749 | 0.1218 | 0.0583 | 3.58 | 0.718 | 8.0 | 2.75 | 395859 | edge_decays_with_delay |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 253 | 23.3322 | 21.9024 | 4.03 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0785 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0537 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1506 | 4.3424 | 4.3355 | 4.36 | 0.708 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8838 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 98 | 15.0948 | 13.0374 | 4.12 | 0.184 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2913 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7696 | 4.16 | 0.626 |
| `0x31121402…` | Sports / price=0.00-0.10 | 94 | 14.0709 | 11.6435 | 3.81 | 0.16 |
| `0xe8ca3f75…` | Sports / Tennis | 550 | 4.2364 | 4.2216 | 5.86 | 0.718 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9627 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9627 | 3.45 | 0.324 |
| `0x31121402…` | Sports / Other sport / price=0.00-0.10 | 60 | 15.6667 | 11.8086 | 3.23 | 0.167 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 817 | 2.9514 | 2.9025 | 2.21 | 0.224 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 818 | 2.9472 | 2.8984 | 2.21 | 0.224 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2153 | 3.53 | 0.794 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6156 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6156 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4442 | 3.33 | 0.754 |
| `0xeda67a7f…` | Sports | 477 | 3.3265 | 3.3116 | 4.16 | 0.541 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3395 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 761 | 2.482 | 2.4533 | 4.63 | 0.66 |
| `0x86c878cd…` | Sports | 2280 | 1.4064 | 1.406 | 6.33 | 0.635 |
| `0x86c878cd…` | Sports / Tennis | 840 | 2.3124 | 2.2903 | 4.75 | 0.648 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8066 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8066 | 2.77 | 0.124 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5859 | 2.28 | 0.167 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7968 | 2.57 | 0.129 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3143 | 7.86 | 0.681 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9789 | 8.06 | 0.75 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1753 | 2.16 | 0.156 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 50 | 9.8116 | 7.1675 | 2.55 | 0.42 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9805 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2923 | 0.9198 | 0.9197 | 2.46 | 0.546 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2923 | 0.9198 | 0.9197 | 2.46 | 0.546 |
| `0x1941ca5d…` | Sports | 2925 | 0.9193 | 0.9192 | 2.46 | 0.546 |
| `0xe8ca3f75…` | Esports / Esports / live | 148 | 3.9439 | 3.9285 | 2.83 | 0.574 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.612 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 455 | 2.0689 | 2.1424 | 4.26 | 0.657 |
| `0xe8ca3f75…` | Esports / Esports | 455 | 2.0689 | 2.1424 | 4.26 | 0.657 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 157 | 4.0258 | 3.6264 | 2.69 | 0.115 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.808 | 2.13 | 0.183 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1859 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0309 | 5.01 | 0.567 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5337 | 4.77 | 0.568 |
| `0xf5fe759c…` | Sports / Tennis / pre | 126 | 4.0477 | 3.8406 | 6.84 | 0.754 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7321 | 4.71 | 0.561 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5436 | 2.39 | 0.133 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7971 | 6.78 | 0.656 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7779 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 430 | 1.9199 | 2.0041 | 4.77 | 0.765 |
| `0xf5fe759c…` | Sports / Tennis | 161 | 3.1465 | 3.079 | 6.46 | 0.677 |
| `0x4afbb658…` | Sports | 166 | 3.1455 | 2.9762 | 2.37 | 0.416 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 88 | 4.9116 | 4.0703 | 2.51 | 0.534 |
| `0xeda67a7f…` | Sports / Tennis / live | 184 | 2.7667 | 2.7853 | 2.32 | 0.571 |
| `0x86c878cd…` | Sports / Tennis / ATP | 401 | 1.897 | 1.8716 | 3.11 | 0.628 |
| `0xf5fe759c…` | Sports | 212 | 2.5521 | 2.5507 | 6.59 | 0.67 |
| `0xeda67a7f…` | Sports / Tennis | 194 | 2.6117 | 2.6438 | 2.3 | 0.567 |
| `0xeda67a7f…` | Sports / Soccer / live | 172 | 2.773 | 2.7921 | 2.35 | 0.517 |
| `0xe8ca3f75…` | Esports / Esports / Counter Strike | 196 | 2.4677 | 2.5925 | 2.93 | 0.638 |
