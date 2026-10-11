# Отчёт воронки, 2026-10-11 07:15 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 52040 |
| 0. Из них не только 5-мин крипта | 50047 |
| 1. Прошли дешёвые отсечки | 4373 из 14502 |
| 2. Прошли по полной истории | 4 + сегментом 70 из 4373 |
| 3. Прошли реалистичный вход | 15 из 74 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 6564 |
| closed<50 | 5216 |
| top1_concentration | 4501 |
| history<90d | 3021 |
| entries>=0.90 | 2600 |
| short_crypto | 969 |
| open_now>10 | 654 |
| profit_from<0.10 | 541 |
| positions>5000 | 18 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3923 |
| drawdown | 3382 |
| concurrency_p95>8 | 3359 |
| unstable_halves | 2861 |
| roi_copy<=0 | 1707 |
| low_liquidity | 638 |
| both_sides | 600 |
| silent | 592 |
| history<90d | 295 |
| top1_concentration | 270 |
| closed<50 | 216 |
| hold<1h | 208 |
| entries>=0.90 | 133 |
| short_crypto | 95 |
| segment_only:t<2.0 | 67 |
| segment_only:drawdown | 64 |
| profit_from<0.10 | 52 |
| sniping | 51 |
| segment_only:unstable_halves | 43 |
| segment_only:roi_copy<=0 | 12 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 52 |
| edge_decays_with_delay | 7 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x461ba1d1354d3e71ea3ec8e76cd4297498a938ff` | adfswdh | Esports | 0.2798 | 2.01 | 0.1769 | 0.3019 | 0.2526 | 8.0 | 3.56 | н/д | все рынки |
| `0x3d962248fd1c8b5ca3a266dc72420b690fa3b432` | DiigG | Esports | 0.1956 | 1.81 | 0.0998 | 0.0798 | 0.177 | 7.0 | 3.03 | н/д | Esports (n=63, roi=+0.25) |
| `0xaf7a1d2ba33c03a91bb2854dd35248d407e6c69f` | mexicanhero | Sports | 0.083 | 1.06 | 0.0488 | 0.0516 | 0.1167 | 4.0 | 10.85 | н/д | Sports / price=0.70-0.90 (n=34, roi=+0.12) | Sports / Soccer / price=0.70-0.90 (n=32, roi=+0.12) |
| `0x9438993c2dee5269b59db70eab3a04abd1243d6a` | dddxdd | Sports | 0.0923 | 1.06 | 0.0455 | 0.0539 | 0.0856 | 8.0 | 10.24 | н/д | Sports / price=0.50-0.70 (n=73, roi=+0.21) |
| `0x68ccc7ba9c7137d854a24585e6b26a00c4b3d976` | hardriversz | Sports | 0.0848 | 1.28 | 0.0946 | 0.1007 | 0.1126 | 3.0 | 5.45 | н/д | Sports / price=0.30-0.50 (n=42, roi=+0.35) | Sports / Soccer / price=0.30-0.50 (n=42, roi=+0.35) |
| `0x44f6ee918b166a82b0f5f06db40f397e759f2c1e` | poxxiy | Sports | 0.0759 | 1.04 | 0.0568 | 0.0632 | 0.0713 | 3.0 | 5.21 | н/д | Sports / price=0.30-0.50 (n=36, roi=+0.33) | Sports / Soccer / price=0.30-0.50 (n=36, roi=+0.33) |
| `0xd5e46e732603449341b037b7d059d385b7002c05` | KaninchenRn | Esports | 0.01 | 0.75 | 0.0677 | 0.0707 | 0.0479 | 8.0 | 2.37 | н/д | Esports / price=0.70-0.90 (n=404, roi=+0.04) | Esports / Esports / price=0.70-0.90 (n=404, roi=+0.04) |
| `0xa906e4dee4c8e67e77aca6efe36ba06d2039ff14` | mugendivincent312 | Sports | 0.0643 | 0.89 | 0.0344 | 0.0404 | 0.0497 | 3.0 | 5.26 | н/д | Sports / price=0.30-0.50 (n=36, roi=+0.28) | Sports / Soccer / price=0.30-0.50 (n=36, roi=+0.28) |
| `0xacfff0dfbd37a70b35b213ecfcdf4526e67a4176` | sotamiz1122 | Sports | 0.0576 | 0.79 | 0.0367 | 0.0382 | 0.0524 | 3.0 | 5.26 | н/д | Sports / Soccer / FIFA World Cup (n=46, roi=+0.21) |
| `0xa0961a0809562ca384a5ac8f9e6acbc2109b31d6` | szpengbobob | Sports | 0.0544 | 0.75 | 0.0372 | 0.0423 | 0.0515 | 3.0 | 4.98 | н/д | Sports / price=0.30-0.50 (n=35, roi=+0.30) | Sports / Soccer / price=0.30-0.50 (n=35, roi=+0.30) | Sports / Soccer / FIFA World Cup (n=49, roi=+0.19) |
| `0xd523d04220b43a41555424346fb088342751ce65` | lalji2h | Sports | 0.0473 | 0.66 | 0.0253 | 0.0255 | 0.0337 | 3.0 | 5.27 | н/д | Sports / price=0.30-0.50 (n=35, roi=+0.26) | Sports / Soccer / price=0.30-0.50 (n=35, roi=+0.26) |
| `0x43e510779f7944eddf67a64fd8bf523e51ec118c` | kwa632462 | Sports | 0.0455 | 0.63 | 0.0176 | 0.0275 | 0.0336 | 3.0 | 5.19 | н/д | Sports / price=0.30-0.50 (n=34, roi=+0.29) | Sports / Soccer / price=0.30-0.50 (n=34, roi=+0.29) |
| `0x45e0891e84cdcbf2451cad0100b8787aaeda9586` | tulaevyoqub06 | Sports | 0.0443 | 0.6 | 0.0201 | 0.029 | 0.0387 | 3.0 | 5.17 | н/д | Sports / price=0.30-0.50 (n=37, roi=+0.29) | Sports / Soccer / price=0.30-0.50 (n=37, roi=+0.29) |
| `0x65d4d905958b418a30c9f72046208689ae094e71` | bo0xts | Sports | 0.0019 | 0.09 | 0.0287 | 0.0373 | 0.0478 | 4.0 | 3.06 | н/д | Sports / price=0.70-0.90 (n=257, roi=+0.05) |
| `0x6170dc7e7b7db8676d37edc3843304d2e49af3fd` | lustra123 | Sports | 0.0357 | 0.95 | 0.0367 | 0.05 | 0.0882 | 6.0 | 4.61 | 0.0 | Sports / Tennis / price=0.30-0.50 (n=91, roi=+0.29) | Sports / price=0.30-0.50 (n=124, roi=+0.25) | Sports / Tennis / ATP (n=316, roi=+0.13) | Sports / Tennis (n=346, roi=+0.12) | Sports (n=475, roi=+0.08) | Sports / Tennis / live (n=95, roi=+0.17) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x3d962248fd1c8b5ca3a266dc72420b690fa3b432` | DiigG | 0.1956 | Esports (n=63, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0605 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0592 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1041 | Sports / Soccer / price=0.50-0.70 (n=94, roi=+0.24) | Sports / Soccer / type=moneyline (n=52, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.0381 | Sports / price=0.50-0.70 (n=99, roi=+0.17) | Sports / Tennis / price=0.50-0.70 (n=74, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` | 0x78fea75923d359a702e14c4fb9c4aff09f34df2f | 0.0927 | Sports / price=0.50-0.70 (n=131, roi=+0.13) | Sports / Tennis / price=0.50-0.70 (n=95, roi=+0.15) | segment_only:t<2.0 |
| `0x9438993c2dee5269b59db70eab3a04abd1243d6a` | dddxdd | 0.0923 | Sports / price=0.50-0.70 (n=73, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x73da1e371be9c623b3d80b86c42eacd92977b7ac` | ZOFGK | -0.0566 | Esports / Esports / pre (n=37, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xaf7a1d2ba33c03a91bb2854dd35248d407e6c69f` | mexicanhero | 0.083 | Sports / price=0.70-0.90 (n=34, roi=+0.12) | Sports / Soccer / price=0.70-0.90 (n=32, roi=+0.12) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1668 | Esports / price=0.10-0.30 (n=104, roi=+0.54) | Esports / Esports / price=0.10-0.30 (n=104, roi=+0.54) | Esports / Esports / type=child_moneyline (n=579, roi=+0.19) | Esports (n=673, roi=+0.16) | Esports / Esports (n=673, roi=+0.16) | Esports / Esports / Dota 2 (n=673, roi=+0.16) | segment_only:drawdown |
| `0x68ccc7ba9c7137d854a24585e6b26a00c4b3d976` | hardriversz | 0.0848 | Sports / price=0.30-0.50 (n=42, roi=+0.35) | Sports / Soccer / price=0.30-0.50 (n=42, roi=+0.35) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1f9e0fa8e8780246d637f40af24b331044c23d5d` |  | -0.0355 | Sports / price=0.50-0.70 (n=177, roi=+0.11) | Sports / Soccer / price=0.50-0.70 (n=124, roi=+0.11) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x44f6ee918b166a82b0f5f06db40f397e759f2c1e` | poxxiy | 0.0759 | Sports / price=0.30-0.50 (n=36, roi=+0.33) | Sports / Soccer / price=0.30-0.50 (n=36, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5e46e732603449341b037b7d059d385b7002c05` | KaninchenRn | 0.01 | Esports / price=0.70-0.90 (n=404, roi=+0.04) | Esports / Esports / price=0.70-0.90 (n=404, roi=+0.04) | segment_only:t<2.0 |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0181 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0ad213f647d6c512bf66f184e0281d70683b9401` | vk-soccer | 0.093 | Sports / Soccer / Premier League 2025 (n=44, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa906e4dee4c8e67e77aca6efe36ba06d2039ff14` | mugendivincent312 | 0.0643 | Sports / price=0.30-0.50 (n=36, roi=+0.28) | Sports / Soccer / price=0.30-0.50 (n=36, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0196 | Sports / Soccer / price=0.50-0.70 (n=54, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xacfff0dfbd37a70b35b213ecfcdf4526e67a4176` | sotamiz1122 | 0.0576 | Sports / Soccer / FIFA World Cup (n=46, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa0961a0809562ca384a5ac8f9e6acbc2109b31d6` | szpengbobob | 0.0544 | Sports / price=0.30-0.50 (n=35, roi=+0.30) | Sports / Soccer / price=0.30-0.50 (n=35, roi=+0.30) | Sports / Soccer / FIFA World Cup (n=49, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf6251c1ea571c3993bdc02d8e2d14e09eaf0b7c7` | football-king | 0.0342 | Sports / Soccer / price=0.50-0.70 (n=54, roi=+0.17) | Sports / Soccer / pre (n=136, roi=+0.10) | Sports / Soccer (n=205, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3740f38cb19308b573d4cf550d1865e0f6f9a935` | tiltedinv | -0.0153 | Sports / Hockey / price=0.70-0.90 (n=30, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd523d04220b43a41555424346fb088342751ce65` | lalji2h | 0.0473 | Sports / price=0.30-0.50 (n=35, roi=+0.26) | Sports / Soccer / price=0.30-0.50 (n=35, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0233 | Sports (n=91, roi=+0.07) | Sports / Soccer / Counter Strike (n=35, roi=+0.09) | Sports / price=0.70-0.90 (n=65, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x43e510779f7944eddf67a64fd8bf523e51ec118c` | kwa632462 | 0.0455 | Sports / price=0.30-0.50 (n=34, roi=+0.29) | Sports / Soccer / price=0.30-0.50 (n=34, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc3bf0fab39b14fa676bc0b4789d738713f6f762d` | uuiicxc | -0.0263 | Sports / price=0.70-0.90 (n=58, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=55, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x45e0891e84cdcbf2451cad0100b8787aaeda9586` | tulaevyoqub06 | 0.0443 | Sports / price=0.30-0.50 (n=37, roi=+0.29) | Sports / Soccer / price=0.30-0.50 (n=37, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xca27292ae5f9c8e6d010e66f37c28928e8cb6f19` | underhaugsvei | 0.061 | Sports / Soccer / live (n=103, roi=+0.16) | Sports / Soccer / type=totals (n=50, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x4dffc112821735459209b050f1b582250382d2d1` | closealiclose | 0.0337 | Sports / price=0.30-0.50 (n=34, roi=+0.28) | Sports / Soccer / price=0.30-0.50 (n=34, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x65d4d905958b418a30c9f72046208689ae094e71` | bo0xts | 0.0019 | Sports / price=0.70-0.90 (n=257, roi=+0.05) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0357 | Sports / price=0.30-0.50 (n=85, roi=+0.25) | Sports / Tennis / price=0.30-0.50 (n=36, roi=+0.30) | Sports (n=407, roi=+0.08) | Sports / Basketball / type=moneyline (n=34, roi=+0.22) | Sports / Basketball (n=37, roi=+0.18) | Sports / Basketball / live (n=32, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | 0.0021 | Sports / Soccer / pre (n=38, roi=+0.24) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0081 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x06a0402a3b327f2eaec00400a72c6813a0395804` | JeanValjean7 | 0.004 | Sports / Soccer / price=0.30-0.50 (n=142, roi=+0.21) | Sports / price=0.30-0.50 (n=162, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0066 | Sports / Soccer / pre (n=171, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=149, roi=+0.09) | Sports / price=0.70-0.90 (n=178, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa0e16dbb5456cdd0c17c83b622178f20d932ba6d` | sunxiaochuan278 | 0.0086 | Esports / Esports / Counter Strike (n=32, roi=+0.04) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0353 | Sports / American Football (n=157, roi=+0.18) | Sports / American Football / pre (n=148, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 1012 | 0.3575 | 0.2581 | 10.89 | 0.741 | 8.0 | 1.17 | 32162 | delayed_roi<=0 |
| `0x461ba1d1354d3e71ea3ec8e76cd4297498a938ff` | adfswdh | Esports | 71 | 0.2798 | 0.1997 | 2.01 | 0.563 | 8.0 | 3.56 | 80070 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 734 | 0.1181 | 0.0555 | 3.45 | 0.719 | 8.0 | 2.78 | 390348 | delayed_roi<=0 |
| `0x522f77e63f087115ee51c7cfda1d34c0b46e1415` | Chernogor | Sports | 289 | 0.0896 | 0.0611 | 2.17 | 0.775 | 8.0 | 4.51 | 93886 | edge_decays_with_delay |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 252 | 23.2304 | 21.8017 | 4.0 | 0.504 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0758 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 214 | 13.0529 | 12.0544 | 5.92 | 0.224 |
| `0xe8ca3f75…` | Sports | 1501 | 4.325 | 4.3181 | 4.33 | 0.709 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8856 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 98 | 15.0948 | 13.0406 | 4.12 | 0.184 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2891 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7669 | 4.16 | 0.626 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1052 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 550 | 4.2364 | 4.2211 | 5.86 | 0.718 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.709 | 4.03 | 0.362 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9628 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9628 | 3.45 | 0.324 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 818 | 2.9613 | 2.9124 | 2.22 | 0.225 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 819 | 2.9571 | 2.9083 | 2.22 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2165 | 3.53 | 0.794 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6119 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6119 | 3.47 | 0.468 |
| `0xeda67a7f…` | Sports | 474 | 3.35 | 3.3348 | 4.16 | 0.542 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4422 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3384 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 756 | 2.4966 | 2.4676 | 4.63 | 0.661 |
| `0x86c878cd…` | Sports | 2264 | 1.4148 | 1.4144 | 6.32 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 835 | 2.3247 | 2.3024 | 4.75 | 0.649 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 43 | 13.509 | 9.8144 | 3.06 | 0.279 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8071 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8071 | 2.77 | 0.124 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5926 | 2.28 | 0.167 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 85 | 6.8402 | 5.7984 | 2.57 | 0.129 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3889 | 2.85 | 0.269 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3145 | 7.86 | 0.681 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.436 | 4.18 | 0.62 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9791 | 8.06 | 0.75 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1826 | 2.16 | 0.156 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9832 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2911 | 0.9279 | 0.9277 | 2.47 | 0.544 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2911 | 0.9279 | 0.9277 | 2.47 | 0.544 |
| `0x1941ca5d…` | Sports | 2913 | 0.9273 | 0.9272 | 2.47 | 0.544 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.9425 | 2.72 | 0.209 |
| `0xe8ca3f75…` | Esports / Esports / live | 147 | 3.9375 | 3.921 | 2.8 | 0.571 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.612 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports | 454 | 2.0627 | 2.136 | 4.24 | 0.656 |
| `0xe8ca3f75…` | Esports / Esports | 454 | 2.0627 | 2.136 | 4.24 | 0.656 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 157 | 4.0258 | 3.6275 | 2.69 | 0.115 |
| `0x7bbb2a27…` | Esports / price=0.00-0.10 | 114 | 4.9036 | 4.2346 | 2.32 | 0.088 |
| `0x5ad5c460…` | Sports / Soccer / price=0.00-0.10 | 60 | 5.6245 | 5.8225 | 2.13 | 0.183 |
| `0xef185339…` | Sports | 3842 | 0.7269 | 0.7269 | 22.63 | 0.692 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1867 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0248 | 5.01 | 0.567 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.928 | 2.43 | 0.3 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.529 | 4.77 | 0.568 |
| `0x13997bdb…` | Sports | 4118 | 0.674 | 0.674 | 22.43 | 0.684 |
| `0x7bbb2a27…` | Esports / Esports / price=0.00-0.10 | 111 | 4.7629 | 4.1 | 2.21 | 0.081 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5453 | 2.39 | 0.133 |
| `0xf5fe759c…` | Sports / Tennis / pre | 126 | 4.0477 | 3.8407 | 6.84 | 0.754 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7271 | 4.71 | 0.561 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7972 | 6.78 | 0.656 |
| `0xda0f4e3f…` | Sports / price=0.00-0.10 | 113 | 4.6241 | 4.0405 | 2.38 | 0.204 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7737 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 430 | 1.9199 | 2.0034 | 4.77 | 0.765 |
