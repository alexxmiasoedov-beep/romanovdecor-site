# Отчёт воронки, 2026-10-09 06:50 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 52273 |
| 0. Из них не только 5-мин крипта | 49625 |
| 1. Прошли дешёвые отсечки | 3997 из 14584 |
| 2. Прошли по полной истории | 3 + сегментом 48 из 3997 |
| 3. Прошли реалистичный вход | 4 из 51 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 6621 |
| closed<50 | 5744 |
| top1_concentration | 5120 |
| entries>=0.90 | 3000 |
| history<90d | 2380 |
| short_crypto | 922 |
| profit_from<0.10 | 708 |
| open_now>10 | 670 |
| positions>5000 | 17 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3591 |
| concurrency_p95>8 | 3144 |
| drawdown | 3032 |
| unstable_halves | 2640 |
| roi_copy<=0 | 1587 |
| silent | 713 |
| low_liquidity | 610 |
| both_sides | 570 |
| history<90d | 315 |
| top1_concentration | 299 |
| closed<50 | 245 |
| hold<1h | 160 |
| entries>=0.90 | 139 |
| short_crypto | 83 |
| profit_from<0.10 | 50 |
| sniping | 48 |
| segment_only:t<2.0 | 44 |
| segment_only:drawdown | 42 |
| segment_only:unstable_halves | 25 |
| segment_only:roi_copy<=0 | 10 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 42 |
| edge_decays_with_delay | 5 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe990e8a448f937cd24c07f204fa33b92750bd17b` | petryan-639 | Esports | 0.1442 | 2.8 | 0.2109 | 0.2062 | 0.2381 | 7.0 | 2.24 | н/д | Esports / Esports / live (n=308, roi=+0.14) | Esports (n=309, roi=+0.14) | Esports / Esports (n=309, roi=+0.14) | Esports / Esports / Dota 2 (n=309, roi=+0.14) | Esports / Esports / type=moneyline (n=52, roi=+0.28) |
| `0x7f816f5263e107c7995eac8cfbce4920161c6083` |  | Esports | 0.0986 | 1.41 | 0.0603 | 0.0638 | 0.0947 | 8.0 | 8.55 | 0.0 | Esports / Esports / Dota 2 (n=48, roi=+0.20) |
| `0x0f992a479833c8d76ad2bc31d59b735a1086cc23` | tshelby23 | Sports | 0.0703 | 1.41 | 0.0857 | 0.131 | 0.0971 | 4.0 | 2.0 | н/д | Sports (n=95, roi=+0.14) | Sports / Soccer (n=83, roi=+0.15) | Sports / Soccer / pre (n=46, roi=+0.17) | Sports / price=0.50-0.70 (n=35, roi=+0.18) |
| `0xb569786bcb19be651f97d420dd956c5f27f56fe0` | SemperFi2k | Esports | 0.051 | 0.88 | 0.0309 | 0.0482 | 0.1123 | 5.0 | 4.2 | н/д | Esports / Esports / type=child_moneyline (n=95, roi=+0.25) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xe990e8a448f937cd24c07f204fa33b92750bd17b` | petryan-639 | 0.1442 | Esports / Esports / live (n=308, roi=+0.14) | Esports (n=309, roi=+0.14) | Esports / Esports (n=309, roi=+0.14) | Esports / Esports / Dota 2 (n=309, roi=+0.14) | Esports / Esports / type=moneyline (n=52, roi=+0.28) | segment_only:drawdown |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0604 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0543 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0587 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x7f816f5263e107c7995eac8cfbce4920161c6083` |  | 0.0986 | Esports / Esports / Dota 2 (n=48, roi=+0.20) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1729 | Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / type=child_moneyline (n=573, roi=+0.19) | Esports (n=666, roi=+0.17) | Esports / Esports (n=666, roi=+0.17) | Esports / Esports / Dota 2 (n=666, roi=+0.17) | segment_only:drawdown |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0975 | Sports / Soccer / price=0.50-0.70 (n=91, roi=+0.26) | Sports / Soccer / type=moneyline (n=47, roi=+0.27) | Sports / Soccer / pre (n=97, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd20658e25171b902cbd90e8b9b292d72735bbd2a` | 0xd20658e25171b902cbd90E8B9b292d72735bbd2a-1776901841772 | -0.0338 | Esports / price=0.70-0.90 (n=44, roi=+0.09) | Esports / Esports / price=0.70-0.90 (n=44, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd4f4ee5f2e93d503e5a1a0cbb5495586fd05bb68` | Auagmg | 0.0372 | Sports / price=0.70-0.90 (n=52, roi=+0.08) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x0f992a479833c8d76ad2bc31d59b735a1086cc23` | tshelby23 | 0.0703 | Sports (n=95, roi=+0.14) | Sports / Soccer (n=83, roi=+0.15) | Sports / Soccer / pre (n=46, roi=+0.17) | Sports / price=0.50-0.70 (n=35, roi=+0.18) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0162 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0146 | Sports / Soccer / price=0.50-0.70 (n=53, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0238 | Sports (n=90, roi=+0.07) | Sports / Soccer / Counter Strike (n=34, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.0894 | Sports / Soccer / pre (n=299, roi=+0.14) | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | Sports / Soccer (n=344, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0034 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=138, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.0226 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0 |
| `0xf3d3c029eea604047526d5615cf19795eb6e77a0` | llicius | -0.0005 | Sports / Other sport (n=52, roi=+0.10) | Sports / Other sport / type=moneyline (n=52, roi=+0.10) | Sports / Other sport / live (n=52, roi=+0.10) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0081 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0091 | Sports / Soccer / pre (n=166, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=143, roi=+0.09) | Sports / price=0.70-0.90 (n=172, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0354 | Sports / American Football (n=155, roi=+0.18) | Sports / American Football / pre (n=146, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0xdefdba677384e28a8c3e6e6fa6303a9e29193f9d` | chet1101 | 0.0393 | Esports / Esports / League of Legends (n=35, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x868315c41ace0c1df527f2f76b73d37ca2ac56c7` | nbanoob | 0.0345 | Sports / price=0.30-0.50 (n=81, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0078 | Esports / price=0.50-0.70 (n=112, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=112, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0368 | Esports / price=0.50-0.70 (n=45, roi=+0.21) | Esports / Esports / price=0.50-0.70 (n=45, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | 0.016 | Sports / American Football / CFB 2026 (n=36, roi=+0.09) | Sports / American Football / live (n=31, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0x83d4422857882eff55f881b295d668b85420ad01` | djdjdjsdjsdjs | 0.0179 | Sports / Basketball (n=104, roi=+0.24) | Sports / Basketball / price=0.30-0.50 (n=51, roi=+0.30) | Sports / Basketball / type=spreads (n=52, roi=+0.27) | Sports / Basketball / pre (n=39, roi=+0.30) | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0278 | Esports / price=0.50-0.70 (n=43, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=43, roi=+0.18) | segment_only:t<2.0 |
| `0x332d40ed4b0cb313059f4fc037dbe520bf2f7b0e` | NJ100DOLLAR | 0.0173 | Sports / Soccer / type=moneyline (n=236, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0146df0b18f6faf92e814904edef6bf441694d51` | yndaa | 0.0497 | Sports / price=0.50-0.70 (n=47, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0617 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0647 | Sports / American Football / pre (n=49, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xb569786bcb19be651f97d420dd956c5f27f56fe0` | SemperFi2k | 0.051 | Esports / Esports / type=child_moneyline (n=95, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown |
| `0x5e5175106a7dbbd92b10f1b56458fc8c1bdd42ce` | 0x5E5175106a7Dbbd92B10f1b56458Fc8c1Bdd42ce-1730865746538 | 0.0397 | Esports / price=0.30-0.50 (n=126, roi=+0.26) | Esports / Esports / price=0.30-0.50 (n=126, roi=+0.26) | Esports / Esports / type=moneyline (n=120, roi=+0.23) | Esports / Esports / live (n=400, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0399 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x62c68066fe7466ad3048a4adff9ad18cfecdab7b` | lucianow34 | 0.024 | Esports / price=0.50-0.70 (n=438, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=438, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0xbcf51140fd48e69c6e6d4bd09d38a629059856a1` | bqy0301 | 0.1945 | Sports / price=0.30-0.50 (n=36, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0xeef382e6c8cb7adde63551043659b381b1c00547` | xiaomikang | 0.0471 | Esports / price=0.10-0.30 (n=42, roi=+0.45) | Esports / Esports / price=0.10-0.30 (n=42, roi=+0.45) | Esports / Esports / type=child_moneyline (n=220, roi=+0.19) | Esports (n=304, roi=+0.16) | Esports / Esports (n=304, roi=+0.16) | Esports / Esports / League of Legends (n=299, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x6aaaf9ad887a4daa865f1b026dd755f4e1a8e611` | Shkrek | Esports | 110 | 0.3835 | 0.2247 | 2.79 | 0.564 | 3.0 | 1.48 | 64040 | edge_decays_with_delay |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 719 | 0.1203 | 0.0577 | 3.48 | 0.722 | 8.0 | 2.82 | 396955 | delayed_roi<=0 |
| `0xbc9bd0866e97ae4725fcd72c1c851f51c72b4238` | 0xBc9bd0866E97ae4725fCD72C1C851f51C72B4238-1768225848002 | Sports | 334 | 0.1275 | 0.0179 | 2.24 | 0.335 | 5.0 | 2.39 | 33101 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 250 | 23.4242 | 21.9716 | 4.0 | 0.508 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0782 | 5.97 | 0.516 |
| `0x86c878cd…` | Sports / price=0.00-0.10 | 213 | 13.1189 | 12.1108 | 5.93 | 0.225 |
| `0xe8ca3f75…` | Sports | 1494 | 4.3452 | 4.3381 | 4.33 | 0.71 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8865 | 5.01 | 0.351 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 97 | 15.2607 | 13.1686 | 4.13 | 0.186 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2911 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7693 | 4.16 | 0.626 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1052 | 4.18 | 0.329 |
| `0xe8ca3f75…` | Sports / Tennis | 550 | 4.2364 | 4.2216 | 5.86 | 0.718 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7091 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3955 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3955 | 3.78 | 0.177 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9627 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9627 | 3.45 | 0.324 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 818 | 2.967 | 2.9181 | 2.23 | 0.227 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 819 | 2.9628 | 2.914 | 2.23 | 0.227 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.217 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 245 | 5.59 | 5.2508 | 3.99 | 0.139 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4824 | 3.61 | 0.17 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6152 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6152 | 3.47 | 0.468 |
| `0xeda67a7f…` | Sports | 468 | 3.399 | 3.3836 | 4.17 | 0.545 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.444 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.3393 | 4.0 | 0.73 |
| `0x86c878cd…` | Sports / Tennis / live | 755 | 2.4997 | 2.4707 | 4.63 | 0.661 |
| `0x86c878cd…` | Sports | 2258 | 1.4195 | 1.4191 | 6.33 | 0.637 |
| `0x86c878cd…` | Sports / Tennis | 834 | 2.3272 | 2.3049 | 4.75 | 0.649 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8072 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.8072 | 2.77 | 0.124 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.6094 | 2.28 | 0.167 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6246 | 2.81 | 0.636 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 84 | 6.9336 | 5.8646 | 2.57 | 0.131 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3912 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7443 | 3.14 | 0.246 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.436 | 4.18 | 0.62 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 31 | 13.5161 | 9.4007 | 2.17 | 0.161 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.985 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2897 | 0.934 | 0.9339 | 2.48 | 0.541 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2897 | 0.934 | 0.9339 | 2.48 | 0.541 |
| `0x1941ca5d…` | Sports | 2899 | 0.9335 | 0.9333 | 2.48 | 0.541 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.9444 | 2.72 | 0.209 |
| `0xe8ca3f75…` | Esports / Esports / live | 147 | 3.9375 | 3.9226 | 2.8 | 0.571 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6119 | 2.86 | 0.07 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 156 | 4.0581 | 3.6545 | 2.7 | 0.115 |
| `0xe8ca3f75…` | Esports | 454 | 2.0627 | 2.1366 | 4.24 | 0.656 |
| `0xe8ca3f75…` | Esports / Esports | 454 | 2.0627 | 2.1366 | 4.24 | 0.656 |
| `0x7bbb2a27…` | Esports / price=0.00-0.10 | 114 | 4.9036 | 4.2346 | 2.32 | 0.088 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.187 | 2.73 | 0.665 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0302 | 5.01 | 0.567 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9285 | 2.43 | 0.3 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 39 | 8.5701 | 6.9576 | 4.77 | 0.564 |
| `0xe8ca3f75…` | Sports / American Football / pre | 43 | 7.924 | 6.619 | 4.77 | 0.558 |
| `0x7bbb2a27…` | Esports / Esports / price=0.00-0.10 | 111 | 4.7629 | 4.1 | 2.21 | 0.081 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5465 | 2.39 | 0.133 |
| `0x3803425e…` | Sports / Soccer / price=0.00-0.10 | 155 | 3.8022 | 3.4226 | 2.89 | 0.194 |
| `0xe8ca3f75…` | Sports / American Football | 50 | 6.7917 | 5.9407 | 4.59 | 0.54 |
| `0xb209ec04…` | Sports | 1557 | 1.0566 | 1.0571 | 4.63 | 0.518 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 430 | 1.9199 | 2.004 | 4.77 | 0.765 |
| `0x3803425e…` | Sports / price=0.00-0.10 | 162 | 3.5947 | 3.2525 | 2.85 | 0.185 |
