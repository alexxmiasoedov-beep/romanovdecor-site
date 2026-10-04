# Отчёт воронки, 2026-10-04 05:56 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 8479 |
| 0. Из них не только 5-мин крипта | 7216 |
| 1. Прошли дешёвые отсечки | 1017 из 7216 |
| 2. Прошли по полной истории | 2 + сегментом 27 из 1017 |
| 3. Прошли реалистичный вход | 12 из 29 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3626 |
| history<90d | 2026 |
| open_now>10 | 1565 |
| closed<50 | 1526 |
| top1_concentration | 1252 |
| entries>=0.90 | 1152 |
| short_crypto | 608 |
| profit_from<0.10 | 421 |
| positions>5000 | 105 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 852 |
| t<2.0 | 843 |
| concurrency_p95>8 | 814 |
| unstable_halves | 639 |
| roi_copy<=0 | 410 |
| low_liquidity | 213 |
| both_sides | 207 |
| history<90d | 129 |
| hold<1h | 74 |
| entries>=0.90 | 37 |
| segment_only:t<2.0 | 26 |
| short_crypto | 23 |
| segment_only:drawdown | 20 |
| top1_concentration | 18 |
| closed<50 | 15 |
| sniping | 15 |
| profit_from<0.10 | 12 |
| segment_only:unstable_halves | 9 |
| segment_only:roi_copy<=0 | 4 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 13 |
| edge_decays_with_delay | 4 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x83b89593ff4dc69543ee87bdd2717e4c22c1c300` | 0x83b89593fF4Dc69543Ee87BDD2717e4c22C1c300-1759035755012 | Sports | 0.6022 | 1.83 | 0.2971 | 0.3075 | 0.4967 | 6.0 | 1.99 | н/д | Sports / MMA/Boxing (n=42, roi=+0.80) | Sports / MMA/Boxing / UFC (n=42, roi=+0.80) | Sports (n=51, roi=+0.70) |
| `0xe478d4ca1c959e78f4ad9e563b134c54363128ea` | gmomoney | Sports | 0.1388 | 2.18 | 0.131 | 0.1694 | 0.1569 | 8.0 | 6.39 | 0.0 | Sports / price=0.50-0.70 (n=106, roi=+0.21) | Sports (n=174, roi=+0.15) | Sports / Baseball / type=moneyline (n=40, roi=+0.29) | Sports / American Football / price=0.50-0.70 (n=33, roi=+0.31) |
| `0x1a3d2bfc95e79a6fa8baf0716f4feddc8c12a116` | Moo11 | Sports | 0.2079 | 1.98 | 0.0774 | 0.0855 | 0.1921 | 6.0 | 11.96 | 0.0 | Sports / Soccer / pre (n=104, roi=+0.23) |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | Sports | 0.1109 | 1.87 | 0.0729 | 0.0682 | 0.1156 | 3.0 | 4.23 | н/д | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) |
| `0xfd8ff771a52c22a8a29a3156572d9b3e47fd761d` |  | Sports | 0.2055 | 1.52 | 0.0484 | 0.0536 | 0.1949 | 6.0 | 4.03 | н/д | Sports / American Football / pre (n=54, roi=+0.28) | Sports / American Football / type=spreads (n=42, roi=+0.30) |
| `0x097bc96aa01bdc70705b8bdc86c9527265582907` | acey17 | Sports | 0.1061 | 1.17 | 0.0239 | 0.0108 | 0.1072 | 6.0 | 2.35 | н/д | Sports / price=0.30-0.50 (n=42, roi=+0.30) |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | Sports | 0.0252 | 1.38 | 0.0768 | 0.0897 | 0.0909 | 8.0 | 3.17 | н/д | Esports / price=0.50-0.70 (n=50, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=50, roi=+0.19) | Esports / Esports / Counter Strike (n=146, roi=+0.09) |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | Esports | -0.028 | -0.56 | 0.0446 | 0.0529 | 0.1934 | 5.0 | 5.83 | 0.0 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | Sports | 0.0599 | 1.3 | 0.0472 | 0.066 | 0.1708 | 6.0 | 4.2 | н/д | Sports / price=0.50-0.70 (n=206, roi=+0.14) |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | Sports | 0.0352 | 0.77 | 0.0384 | 0.0584 | 0.0383 | 4.0 | 5.9 | 0.0 | Sports / price=0.70-0.90 (n=36, roi=+0.11) |
| `0x339a9ace6a1950797b8e0a50a125b5b4e23c6a00` | superlarry | Sports | 0.0133 | 0.28 | 0.042 | 0.06 | 0.0361 | 6.0 | 6.0 | 0.0 | Sports / Tennis / pre (n=33, roi=+0.19) |
| `0x224b16b3c67ad51f6302eab010a9e8f540a88927` | hitaobicho | Esports | 0.1148 | 1.67 | 0.2025 | 0.1907 | 0.2444 | 7.0 | 3.81 | 0.0 | Esports / Esports / pre (n=123, roi=+0.48) | Esports / Esports / type=map_handicap (n=37, roi=+0.30) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x83b89593ff4dc69543ee87bdd2717e4c22c1c300` | 0x83b89593fF4Dc69543Ee87BDD2717e4c22C1c300-1759035755012 | 0.6022 | Sports / MMA/Boxing (n=42, roi=+0.80) | Sports / MMA/Boxing / UFC (n=42, roi=+0.80) | Sports (n=51, roi=+0.70) | segment_only:t<2.0 |
| `0x1a3d2bfc95e79a6fa8baf0716f4feddc8c12a116` | Moo11 | 0.2079 | Sports / Soccer / pre (n=104, roi=+0.23) | segment_only:t<2.0 |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | 0.1109 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) | segment_only:t<2.0 |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1117 | Sports / Soccer / price=0.50-0.70 (n=89, roi=+0.27) | Sports / Soccer / type=moneyline (n=44, roi=+0.30) | segment_only:t<2.0;segment_only:drawdown |
| `0x6fe306bbc57d7586cea47730985a3ecce5f5da66` | BanditMarket | -0.0679 | Sports / Other sport / type=moneyline (n=98, roi=+0.23) | Sports / Other sport (n=117, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd8ff771a52c22a8a29a3156572d9b3e47fd761d` |  | 0.2055 | Sports / American Football / pre (n=54, roi=+0.28) | Sports / American Football / type=spreads (n=42, roi=+0.30) | segment_only:t<2.0 |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.052 | Sports / price=0.70-0.90 (n=80, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x093506de4a173bd4ea393a7cf5393495df14d9ef` | xxyr | 0.0226 | Sports / price=0.70-0.90 (n=50, roi=+0.07) | segment_only:t<2.0 |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.028 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x097bc96aa01bdc70705b8bdc86c9527265582907` | acey17 | 0.1061 | Sports / price=0.30-0.50 (n=42, roi=+0.30) | segment_only:t<2.0;segment_only:drawdown |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` |  | 0.0618 | Sports / price=0.50-0.70 (n=115, roi=+0.14) | segment_only:t<2.0 |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | 0.0252 | Esports / price=0.50-0.70 (n=50, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=50, roi=+0.19) | Esports / Esports / Counter Strike (n=146, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | 0.0599 | Sports / price=0.50-0.70 (n=206, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | 0.0352 | Sports / price=0.70-0.90 (n=36, roi=+0.11) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0543 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | 0.0085 | Sports / Other sport (n=116, roi=+0.06) | Sports / Other sport / price=0.70-0.90 (n=73, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | -0.0014 | Sports / Soccer / price=0.70-0.90 (n=141, roi=+0.09) | Sports / price=0.70-0.90 (n=170, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x339a9ace6a1950797b8e0a50a125b5b4e23c6a00` | superlarry | 0.0133 | Sports / Tennis / pre (n=33, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0104 | Esports / price=0.50-0.70 (n=107, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=107, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0571 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x224b16b3c67ad51f6302eab010a9e8f540a88927` | hitaobicho | 0.1148 | Esports / Esports / pre (n=123, roi=+0.48) | Esports / Esports / type=map_handicap (n=37, roi=+0.30) | segment_only:t<2.0;segment_only:drawdown |
| `0x85f031d069de300055900c4055c1baeb6bde3f67` | RJW1 | 0.0751 | Sports / price=0.50-0.70 (n=76, roi=+0.20) | Sports / Soccer / price=0.50-0.70 (n=53, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x43fe17cf68eb58be1d40514be0e52674b71d26ee` | 0x43fE17Cf68EB58BE1d40514Be0e52674B71d26eE-1768993726139 | 0.0556 | Sports / Basketball / price=0.30-0.50 (n=42, roi=+0.27) | Sports / Cricket / price=0.50-0.70 (n=149, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x70d8a64b823ae3843fc6c99c6c4ff1bdd911d2ba` |  | 0.1269 | Esports / price=0.30-0.50 (n=50, roi=+0.36) | Esports / Esports / price=0.30-0.50 (n=50, roi=+0.36) | segment_only:t<2.0;segment_only:drawdown |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.1088 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x7ce336595687024c9ebf620f2dcb3b71269b1689` | 0x7Ce336595687024C9ebF620F2dCb3b71269B1689-1774766944047 | 0.0916 | Sports / Other sport / live (n=734, roi=+0.16) | Sports / Other sport / Hong Kong Daily Weather (n=475, roi=+0.19) | Sports / Other sport / type=binary (n=836, roi=+0.14) | Sports / Other sport / price=0.10-0.30 (n=351, roi=+0.21) | Sports / Other sport (n=840, roi=+0.13) | Sports / price=0.10-0.30 (n=367, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x1ea824aa13c35960a46fce3a33497a39e8d3b821` | BepiJr | 0.4146 | Sports (n=584, roi=+0.41) | Sports / price=0.10-0.30 (n=111, roi=+0.42) | Sports / price=0.30-0.50 (n=75, roi=+0.40) | Sports / Soccer / price=0.30-0.50 (n=59, roi=+0.34) | Sports / price=0.70-0.90 (n=96, roi=+0.14) | segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 944 | 0.3361 | 0.2501 | 10.45 | 0.746 | 8.0 | 1.16 | 33212 | delayed_roi<=0 |
| `0xe478d4ca1c959e78f4ad9e563b134c54363128ea` | gmomoney | Sports | 192 | 0.1388 | 0.1289 | 2.18 | 0.641 | 8.0 | 6.39 | 254878 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x465ace6e…` | Sports / price=0.00-0.10 | 50 | 26.926 | 20.4881 | 5.14 | 0.58 |
| `0x465ace6e…` | Sports | 303 | 5.079 | 5.0365 | 4.94 | 0.713 |
| `0x465ace6e…` | Sports / Tennis | 133 | 8.0667 | 7.5865 | 4.0 | 0.722 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 817 | 2.969 | 2.9201 | 2.23 | 0.225 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 818 | 2.9647 | 2.916 | 2.23 | 0.225 |
| `0x465ace6e…` | Sports / Tennis / WTA | 36 | 17.6494 | 12.9151 | 2.99 | 0.778 |
| `0x465ace6e…` | Sports / Tennis / live | 55 | 10.8553 | 9.1322 | 2.79 | 0.818 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3981 | 2.85 | 0.269 |
| `0x465ace6e…` | Sports / Tennis / pre | 78 | 6.1004 | 5.752 | 2.95 | 0.654 |
| `0x1941ca5d…` | Sports / Other sport | 2865 | 0.9424 | 0.9423 | 2.47 | 0.534 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2865 | 0.9424 | 0.9423 | 2.47 | 0.534 |
| `0x1941ca5d…` | Sports | 2867 | 0.9419 | 0.9417 | 2.47 | 0.534 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.9502 | 2.72 | 0.209 |
| `0x465ace6e…` | Sports / Tennis / ATP | 56 | 6.9698 | 6.2918 | 2.62 | 0.732 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9292 | 2.43 | 0.3 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 375 | 2.1295 | 2.0426 | 3.45 | 0.291 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 390 | 2.0709 | 1.99 | 3.48 | 0.285 |
| `0x1985327e…` | Sports | 1296 | 1.0206 | 1.0206 | 2.63 | 0.718 |
| `0x1985327e…` | Sports / Soccer / live | 844 | 1.2257 | 1.2209 | 2.06 | 0.705 |
| `0x1985327e…` | Sports / Soccer | 854 | 1.2113 | 1.2069 | 2.06 | 0.704 |
| `0x1941ca5d…` | Sports / Other sport / live | 2170 | 0.7261 | 0.7279 | 3.59 | 0.576 |
| `0xbfeceb41…` | Sports / price=0.00-0.10 | 423 | 1.6357 | 1.5828 | 2.47 | 0.076 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 58 | 5.3155 | 4.058 | 2.18 | 0.603 |
| `0x5f612351…` | Sports / Other sport / price=0.00-0.10 | 560 | 1.2943 | 1.2675 | 4.41 | 0.237 |
| `0x5f612351…` | Sports / price=0.00-0.10 | 561 | 1.2902 | 1.2636 | 4.41 | 0.237 |
| `0xdf804b17…` | Sports / price=0.00-0.10 | 88 | 3.8291 | 3.1657 | 2.12 | 0.136 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8087 | 2.81 | 0.664 |
| `0xdf804b17…` | Sports / Soccer / price=0.00-0.10 | 83 | 3.9192 | 3.2061 | 2.06 | 0.133 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 141 | 2.6392 | 2.3401 | 2.43 | 0.333 |
| `0x5f612351…` | Sports / Other sport / live | 2220 | 0.5794 | 0.5788 | 7.2 | 0.446 |
| `0x5f612351…` | Sports / Other sport | 2264 | 0.5634 | 0.563 | 7.14 | 0.447 |
| `0x5f612351…` | Sports / Other sport / type=binary | 2264 | 0.5634 | 0.563 | 7.14 | 0.447 |
| `0x5f612351…` | Sports | 2278 | 0.5598 | 0.5594 | 7.13 | 0.447 |
| `0x41558102…` | Sports / price=0.10-0.30 | 330 | 1.5243 | 1.4556 | 11.78 | 0.6 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 183 | 2.141 | 1.9463 | 2.4 | 0.126 |
| `0xd84d970b…` | Sports / Soccer / price=0.00-0.10 | 32 | 7.1213 | 4.6263 | 2.25 | 0.406 |
| `0x164cb85e…` | Sports / Other sport / type=binary | 3017 | 0.4664 | 0.466 | 5.86 | 0.554 |
| `0x164cb85e…` | Sports / Other sport | 3040 | 0.4631 | 0.4628 | 5.86 | 0.554 |
| `0x41558102…` | Sports | 6073 | 0.3235 | 0.3235 | 10.37 | 0.851 |
| `0x164cb85e…` | Sports | 3242 | 0.4326 | 0.4325 | 5.81 | 0.549 |
| `0x465ace6e…` | Sports / Other sport | 41 | 3.5682 | 3.8388 | 2.55 | 0.634 |
| `0x76697d10…` | Sports / Basketball / live | 954 | 0.7974 | 0.7932 | 3.84 | 0.577 |
| `0x76697d10…` | Sports / Basketball | 955 | 0.7955 | 0.7914 | 3.83 | 0.576 |
| `0x76697d10…` | Sports / Basketball / type=totals | 630 | 0.9776 | 0.9658 | 3.19 | 0.557 |
| `0x164cb85e…` | Sports / Other sport / Shanghai Daily Lowest Temperature | 297 | 1.4505 | 1.385 | 2.22 | 0.556 |
| `0x56f4f054…` | Sports / Soccer / price=0.00-0.10 | 215 | 1.7242 | 1.5931 | 2.03 | 0.088 |
| `0xa991049a…` | Sports | 1904 | 0.528 | 0.5258 | 6.88 | 0.717 |
| `0x164cb85e…` | Sports / Other sport / live | 2796 | 0.4316 | 0.4315 | 5.88 | 0.561 |
| `0x76697d10…` | Sports | 1421 | 0.5959 | 0.5959 | 4.23 | 0.604 |
| `0xbfeceb41…` | Sports | 1582 | 0.5654 | 0.5641 | 3.13 | 0.422 |
| `0x91feec8a…` | Sports / Soccer / price=0.00-0.10 | 299 | 1.3632 | 1.2933 | 3.02 | 0.12 |
| `0x465ace6e…` | Sports / Tennis / type=moneyline | 54 | 2.5183 | 3.0251 | 2.83 | 0.685 |
| `0x56f4f054…` | Sports / price=0.00-0.10 | 260 | 1.4434 | 1.3534 | 2.03 | 0.088 |
| `0x91feec8a…` | Sports / price=0.00-0.10 | 308 | 1.2942 | 1.2304 | 2.95 | 0.117 |
| `0x91feec8a…` | Sports / Soccer / live | 2555 | 0.4238 | 0.4224 | 7.11 | 0.58 |
| `0x88eec58b…` | Sports / price=0.00-0.10 | 157 | 1.8085 | 1.7025 | 2.38 | 0.325 |
| `0x88eec58b…` | Sports / Other sport / price=0.00-0.10 | 157 | 1.8085 | 1.7025 | 2.38 | 0.325 |
| `0x1985327e…` | Sports / price=0.10-0.30 | 269 | 1.2688 | 1.2515 | 8.87 | 0.591 |
| `0xa991049a…` | Sports / price=0.10-0.30 | 257 | 1.3415 | 1.2674 | 11.07 | 0.638 |
| `0xc66ab53d…` | Sports / price=0.10-0.30 | 268 | 1.3001 | 1.2347 | 11.16 | 0.735 |
