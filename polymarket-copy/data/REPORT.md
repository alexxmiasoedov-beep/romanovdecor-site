# Отчёт воронки, 2026-10-02 06:06 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 8581 |
| 0. Из них не только 5-мин крипта | 7290 |
| 1. Прошли дешёвые отсечки | 983 из 7290 |
| 2. Прошли по полной истории | 4 + сегментом 22 из 983 |
| 3. Прошли реалистичный вход | 9 из 26 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3777 |
| history<90d | 1938 |
| open_now>10 | 1573 |
| closed<50 | 1500 |
| entries>=0.90 | 1384 |
| top1_concentration | 1251 |
| short_crypto | 615 |
| profit_from<0.10 | 469 |
| positions>5000 | 98 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 852 |
| t<2.0 | 809 |
| concurrency_p95>8 | 797 |
| unstable_halves | 610 |
| roi_copy<=0 | 401 |
| low_liquidity | 212 |
| both_sides | 211 |
| history<90d | 138 |
| hold<1h | 54 |
| entries>=0.90 | 37 |
| short_crypto | 28 |
| top1_concentration | 21 |
| segment_only:t<2.0 | 21 |
| sniping | 20 |
| segment_only:drawdown | 18 |
| closed<50 | 13 |
| segment_only:unstable_halves | 10 |
| profit_from<0.10 | 8 |
| segment_only:roi_copy<=0 | 2 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 15 |
| edge_decays_with_delay | 2 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x1a3d2bfc95e79a6fa8baf0716f4feddc8c12a116` | Moo11 | Sports | 0.2475 | 2.31 | 0.1147 | 0.1231 | 0.2222 | 6.0 | 11.76 | 0.0 | Sports / Soccer / pre (n=99, roi=+0.27) | Sports / Soccer / type=moneyline (n=92, roi=+0.28) | Sports (n=113, roi=+0.25) | Sports / Soccer (n=108, roi=+0.25) |
| `0x63808949537e0a49ada6e63a9ef54a3334f7e633` |  | Sports | 0.0807 | 2.16 | 0.0771 | 0.0856 | 0.0883 | 5.0 | 3.01 | н/д | Sports / Soccer / price=0.50-0.70 (n=39, roi=+0.26) | Sports / price=0.50-0.70 (n=42, roi=+0.22) | Sports / Soccer (n=163, roi=+0.09) | Sports / Soccer / type=moneyline (n=81, roi=+0.13) | Sports (n=193, roi=+0.08) | Sports / Soccer / pre (n=117, roi=+0.10) |
| `0xaa903818f3f2d6fb6790cc55672bb99ab734c709` | Giannis34x | Sports | 0.1031 | 1.82 | 0.0884 | 0.0953 | 0.106 | 7.0 | 2.26 | н/д | Sports / price=0.50-0.70 (n=57, roi=+0.22) |
| `0x3930b0a4ab9b69cc28ee9d071233324eeb64fbeb` |  | Esports | 0.0601 | 1.51 | 0.0654 | 0.0704 | 0.0852 | 3.0 | 4.64 | 0.2974 | Esports / Esports / Dota 2 (n=45, roi=+0.14) |
| `0x7472de5417d6fbfa4a432721a9bf7cf006175349` | muyou813 | Esports | 0.1564 | 1.65 | 0.0234 | 0.0206 | 0.1406 | 8.0 | 3.24 | 0.0 | Esports / Esports / live (n=116, roi=+0.31) | Esports (n=137, roi=+0.27) | Esports / Esports (n=137, roi=+0.27) | Esports / Esports / League of Legends (n=121, roi=+0.26) |
| `0x310579303783d1b3c2b33cd28d83af946e082e7e` |  | Esports | 0.1072 | 1.49 | 0.0487 | 0.0524 | 0.1419 | 4.0 | 4.92 | 0.0156 | Sports / Soccer (n=34, roi=+0.28) |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | Sports | 0.1136 | 1.8 | 0.0742 | 0.0692 | 0.119 | 3.0 | 4.37 | н/д | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | Sports | 0.0298 | 0.62 | 0.0337 | 0.0547 | 0.0283 | 4.0 | 5.9 | 0.0 | Sports / price=0.70-0.90 (n=34, roi=+0.10) |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | Sports | 0.0556 | 1.2 | 0.0232 | 0.0414 | 0.1486 | 6.0 | 4.2 | н/д | Sports / price=0.50-0.70 (n=202, roi=+0.14) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xaa903818f3f2d6fb6790cc55672bb99ab734c709` | Giannis34x | 0.1031 | Sports / price=0.50-0.70 (n=57, roi=+0.22) | segment_only:t<2.0 |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1261 | Sports / Soccer / price=0.50-0.70 (n=86, roi=+0.29) | Sports / price=0.50-0.70 (n=132, roi=+0.22) | Sports / Soccer (n=167, roi=+0.17) | Sports / Soccer / type=moneyline (n=43, roi=+0.29) | segment_only:drawdown |
| `0x3930b0a4ab9b69cc28ee9d071233324eeb64fbeb` |  | 0.0601 | Esports / Esports / Dota 2 (n=45, roi=+0.14) | segment_only:t<2.0 |
| `0x7472de5417d6fbfa4a432721a9bf7cf006175349` | muyou813 | 0.1564 | Esports / Esports / live (n=116, roi=+0.31) | Esports (n=137, roi=+0.27) | Esports / Esports (n=137, roi=+0.27) | Esports / Esports / League of Legends (n=121, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | 0.1136 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x310579303783d1b3c2b33cd28d83af946e082e7e` |  | 0.1072 | Sports / Soccer (n=34, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.0286 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0566 | Esports / price=0.50-0.70 (n=34, roi=+0.25) | Esports / Esports / price=0.50-0.70 (n=34, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | 0.0556 | Sports / price=0.50-0.70 (n=202, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | 0.0298 | Sports / price=0.70-0.90 (n=34, roi=+0.10) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | 0.0104 | Sports / Other sport / price=0.70-0.90 (n=71, roi=+0.06) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0151 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0108 | Esports / price=0.50-0.70 (n=106, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=106, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x670d76669e567a24a9876f92310436d029020825` | ebglyss | 0.0343 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.25) | Sports / price=0.50-0.70 (n=54, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x61a81cff39f833a84cdff8cb68b86b08733c519d` | jean01101 | 0.0548 | Esports / Esports / League of Legends (n=250, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe70ce7a94ee228d75c97b0bdbf2a5eb0e3e11512` | 666CosmicOwl | 0.0167 | Sports / Tennis (n=108, roi=+0.11) | Sports / Tennis / type=moneyline (n=103, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0xc13f2a97dd2a68061c1b382568b7bd711a08c93b` | 0xc13f2A97dD2A68061C1B382568B7bD711A08c93b-1733488832713 | 0.0181 | Sports / Basketball / pre (n=225, roi=+0.17) | Sports / price=0.30-0.50 (n=224, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x92c9077e85bca0d7d31cffe1b585c3907d2dc500` | TPPKP | 0.0563 | Sports / Other sport / Taipei Daily Weather (n=70, roi=+0.56) | Sports / Other sport / live (n=81, roi=+0.44) | Sports / Other sport (n=98, roi=+0.37) | Sports / Other sport / type=binary (n=98, roi=+0.37) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x82882d761b0d7f18b2cc286117d10cd8a15a5519` | Sugarina | 0.1142 | Sports / Other sport / price=0.70-0.90 (n=43, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5b20e906232c334290d7740064efeadcc9b8a8e0` | caput.mund | 0.0481 | Sports / price=0.70-0.90 (n=131, roi=+0.10) | Sports / Soccer / price=0.70-0.90 (n=59, roi=+0.10) | Sports / Tennis / price=0.70-0.90 (n=61, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.1114 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x7ce336595687024c9ebf620f2dcb3b71269b1689` | 0x7Ce336595687024C9ebF620F2dCb3b71269B1689-1774766944047 | 0.0916 | Sports / Other sport / live (n=734, roi=+0.16) | Sports / Other sport / Hong Kong Daily Weather (n=475, roi=+0.19) | Sports / Other sport / type=binary (n=836, roi=+0.14) | Sports / Other sport / price=0.10-0.30 (n=351, roi=+0.21) | Sports / Other sport (n=840, roi=+0.13) | Sports / price=0.10-0.30 (n=367, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 922 | 0.3346 | 0.2482 | 10.27 | 0.745 | 8.0 | 1.12 | 33592 | delayed_roi<=0 |
| `0x1a3d2bfc95e79a6fa8baf0716f4feddc8c12a116` | Moo11 | Sports | 113 | 0.2475 | 0.1251 | 2.31 | 0.69 | 6.0 | 11.76 | 425954 | прошёл |
| `0x63808949537e0a49ada6e63a9ef54a3334f7e633` |  | Sports | 194 | 0.0807 | 0.1003 | 2.16 | 0.809 | 5.0 | 3.01 | 719836 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 688 | 0.1183 | 0.0591 | 3.4 | 0.728 | 8.0 | 2.88 | 390348 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 822 | 2.9485 | 2.9004 | 2.22 | 0.224 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 823 | 2.9443 | 2.8963 | 2.22 | 0.224 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3984 | 2.85 | 0.269 |
| `0x1941ca5d…` | Sports / Other sport | 2868 | 0.9403 | 0.9402 | 2.47 | 0.531 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2868 | 0.9403 | 0.9402 | 2.47 | 0.531 |
| `0x1941ca5d…` | Sports | 2870 | 0.9397 | 0.9396 | 2.47 | 0.531 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 65 | 7.8118 | 6.114 | 2.73 | 0.215 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9293 | 2.43 | 0.3 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 372 | 2.154 | 2.0651 | 3.47 | 0.293 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 387 | 2.0941 | 2.0113 | 3.5 | 0.287 |
| `0x1941ca5d…` | Sports / Other sport / live | 2167 | 0.7271 | 0.7289 | 3.59 | 0.575 |
| `0xbfeceb41…` | Sports / price=0.00-0.10 | 405 | 1.722 | 1.6645 | 2.49 | 0.077 |
| `0xb595d09c…` | Sports / Tennis / type=tennis_completed_match | 66 | 5.3324 | 4.1224 | 2.02 | 1.0 |
| `0xdf804b17…` | Sports / price=0.00-0.10 | 87 | 3.8846 | 3.2059 | 2.13 | 0.138 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8088 | 2.81 | 0.664 |
| `0xdf804b17…` | Sports / Soccer / price=0.00-0.10 | 82 | 3.9792 | 3.2487 | 2.07 | 0.134 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 137 | 2.7454 | 2.4254 | 2.45 | 0.343 |
| `0x122b758a…` | Sports / price=0.00-0.10 | 307 | 1.6436 | 1.5669 | 2.75 | 0.166 |
| `0xd84d970b…` | Sports / Soccer / price=0.00-0.10 | 31 | 7.3833 | 4.7374 | 2.27 | 0.419 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 183 | 2.141 | 1.946 | 2.4 | 0.126 |
| `0x41558102…` | Sports / price=0.10-0.30 | 328 | 1.5216 | 1.4528 | 11.74 | 0.601 |
| `0x164cb85e…` | Sports / Other sport / type=binary | 2983 | 0.4744 | 0.474 | 5.89 | 0.555 |
| `0x164cb85e…` | Sports / Other sport | 3007 | 0.471 | 0.4706 | 5.89 | 0.556 |
| `0x41558102…` | Sports | 6042 | 0.3238 | 0.3238 | 10.33 | 0.851 |
| `0x164cb85e…` | Sports | 3244 | 0.4381 | 0.4379 | 5.89 | 0.552 |
| `0x122b758a…` | Sports / Soccer / price=0.00-0.10 | 250 | 1.6473 | 1.554 | 2.67 | 0.164 |
| `0x76697d10…` | Sports / Basketball / live | 951 | 0.7982 | 0.794 | 3.83 | 0.576 |
| `0x76697d10…` | Sports / Basketball | 952 | 0.7963 | 0.7922 | 3.82 | 0.576 |
| `0x76697d10…` | Sports / Basketball / type=totals | 628 | 0.9795 | 0.9676 | 3.19 | 0.557 |
| `0x164cb85e…` | Sports / Other sport / Shanghai Daily Lowest Temperature | 293 | 1.4715 | 1.4037 | 2.22 | 0.56 |
| `0xbfeceb41…` | Sports | 1450 | 0.6125 | 0.611 | 3.12 | 0.414 |
| `0x3b4484b6…` | Politics | 362 | 1.2194 | 1.2128 | 2.58 | 0.685 |
| `0x164cb85e…` | Sports / Other sport / live | 2766 | 0.4385 | 0.4383 | 5.91 | 0.563 |
| `0x91feec8a…` | Sports / Soccer / price=0.00-0.10 | 293 | 1.4045 | 1.3311 | 3.05 | 0.119 |
| `0x76697d10…` | Sports | 1397 | 0.5971 | 0.5971 | 4.17 | 0.603 |
| `0x91feec8a…` | Sports / price=0.00-0.10 | 302 | 1.3328 | 1.266 | 2.98 | 0.116 |
| `0x91feec8a…` | Sports / Soccer / live | 2513 | 0.4332 | 0.4318 | 7.15 | 0.581 |
| `0x037305f4…` | Other | 250 | 1.4473 | 1.355 | 16.17 | 0.844 |
| `0x037305f4…` | Other / ? | 250 | 1.4473 | 1.355 | 16.17 | 0.844 |
| `0x037305f4…` | Other / ? / ? | 250 | 1.4473 | 1.355 | 16.17 | 0.844 |
| `0x037305f4…` | Other / ? / type=binary | 250 | 1.4473 | 1.355 | 16.17 | 0.844 |
| `0x88eec58b…` | Sports / price=0.00-0.10 | 155 | 1.7494 | 1.6476 | 2.29 | 0.323 |
| `0x88eec58b…` | Sports / Other sport / price=0.00-0.10 | 155 | 1.7494 | 1.6476 | 2.29 | 0.323 |
| `0xa991049a…` | Sports / price=0.10-0.30 | 253 | 1.3569 | 1.2749 | 11.05 | 0.64 |
| `0xc66ab53d…` | Sports / price=0.10-0.30 | 267 | 1.3052 | 1.2393 | 11.17 | 0.738 |
| `0x41558102…` | Sports / Other sport / live | 1822 | 0.466 | 0.4644 | 5.7 | 0.843 |
| `0x41558102…` | Sports / Other sport | 1831 | 0.4643 | 0.4628 | 5.71 | 0.844 |
| `0x88eec58b…` | Sports / Other sport / live | 472 | 0.9035 | 0.9016 | 3.49 | 0.468 |
| `0x88eec58b…` | Sports / Other sport / Chengdu Daily Weather | 218 | 1.3449 | 1.304 | 2.61 | 0.495 |
| `0x88eec58b…` | Sports | 494 | 0.8603 | 0.8602 | 3.48 | 0.466 |
| `0x88eec58b…` | Sports / Other sport | 494 | 0.8603 | 0.8602 | 3.48 | 0.466 |
| `0x88eec58b…` | Sports / Other sport / type=binary | 494 | 0.8603 | 0.8602 | 3.48 | 0.466 |
| `0xc66ab53d…` | Sports / Soccer / price=0.10-0.30 | 228 | 1.3357 | 1.257 | 10.23 | 0.737 |
| `0xd84d970b…` | Sports / Soccer | 181 | 1.4911 | 1.4061 | 2.52 | 0.519 |
| `0x1c0f3e4c…` | Sports / Other sport / type=binary | 1353 | 0.5142 | 0.5132 | 2.81 | 0.337 |
| `0x1c0f3e4c…` | Sports / Other sport | 1354 | 0.5131 | 0.5121 | 2.81 | 0.337 |
| `0xbfeceb41…` | Sports / Soccer / live | 847 | 0.6371 | 0.634 | 2.45 | 0.406 |
| `0xbfeceb41…` | Sports / Soccer | 899 | 0.6066 | 0.6043 | 2.46 | 0.4 |
| `0x1c0f3e4c…` | Sports / Other sport / price=0.00-0.10 | 770 | 0.658 | 0.6526 | 2.07 | 0.157 |
| `0x1c0f3e4c…` | Sports / price=0.00-0.10 | 772 | 0.6537 | 0.6485 | 2.06 | 0.157 |
