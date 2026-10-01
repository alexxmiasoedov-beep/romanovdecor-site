# Отчёт воронки, 2026-10-01 05:57 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 8078 |
| 0. Из них не только 5-мин крипта | 6636 |
| 1. Прошли дешёвые отсечки | 888 из 6636 |
| 2. Прошли по полной истории | 1 + сегментом 25 из 888 |
| 3. Прошли реалистичный вход | 6 из 26 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3242 |
| history<90d | 1940 |
| open_now>10 | 1565 |
| entries>=0.90 | 1343 |
| closed<50 | 1089 |
| top1_concentration | 1077 |
| short_crypto | 601 |
| profit_from<0.10 | 458 |
| positions>5000 | 104 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 718 |
| concurrency_p95>8 | 709 |
| t<2.0 | 707 |
| unstable_halves | 521 |
| roi_copy<=0 | 334 |
| low_liquidity | 228 |
| both_sides | 200 |
| history<90d | 138 |
| hold<1h | 68 |
| entries>=0.90 | 34 |
| short_crypto | 29 |
| segment_only:t<2.0 | 25 |
| top1_concentration | 23 |
| closed<50 | 20 |
| segment_only:drawdown | 18 |
| sniping | 16 |
| profit_from<0.10 | 10 |
| segment_only:unstable_halves | 9 |
| segment_only:roi_copy<=0 | 3 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 18 |
| edge_decays_with_delay | 2 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x63808949537e0a49ada6e63a9ef54a3334f7e633` |  | Sports | 0.0763 | 1.98 | 0.0742 | 0.0818 | 0.0834 | 5.0 | 3.02 | н/д | Sports / Soccer / price=0.50-0.70 (n=39, roi=+0.25) | Sports / price=0.50-0.70 (n=42, roi=+0.22) | Sports / Soccer (n=163, roi=+0.09) | Sports / Soccer / type=moneyline (n=81, roi=+0.13) | Sports / Soccer / pre (n=117, roi=+0.10) |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | Esports | 0.1498 | 1.78 | 0.0769 | 0.0823 | 0.1674 | 4.0 | 2.28 | н/д | Esports / Esports / live (n=105, roi=+0.27) | Esports / Esports / Counter Strike (n=96, roi=+0.25) | Esports (n=118, roi=+0.22) | Esports / Esports (n=118, roi=+0.22) | Esports / price=0.30-0.50 (n=48, roi=+0.30) | Esports / Esports / price=0.30-0.50 (n=48, roi=+0.30) |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | Sports | 0.1321 | 1.44 | 0.0508 | 0.0662 | 0.1245 | 4.0 | 4.34 | 0.0 | Sports / price=0.50-0.70 (n=41, roi=+0.24) | Sports / Soccer / price=0.50-0.70 (n=41, roi=+0.24) |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | Sports | 0.0538 | 1.14 | 0.0608 | 0.0827 | 0.0522 | 4.0 | 5.29 | 0.0 | Sports / price=0.70-0.90 (n=31, roi=+0.12) |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | Sports | 0.1119 | 1.72 | 0.0726 | 0.0668 | 0.1175 | 3.0 | 4.38 | 0.0 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) |
| `0x13ce0f6f73a83a2be1eb484c91169c2bd5b935f0` | mozak | Sports | -0.0308 | -1.09 | 0.059 | 0.061 | 0.0334 | 8.0 | 6.84 | 0.0 | Sports / Tennis / price=0.70-0.90 (n=31, roi=+0.09) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x63808949537e0a49ada6e63a9ef54a3334f7e633` |  | 0.0763 | Sports / Soccer / price=0.50-0.70 (n=39, roi=+0.25) | Sports / price=0.50-0.70 (n=42, roi=+0.22) | Sports / Soccer (n=163, roi=+0.09) | Sports / Soccer / type=moneyline (n=81, roi=+0.13) | Sports / Soccer / pre (n=117, roi=+0.10) | segment_only:t<2.0 |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | 0.1498 | Esports / Esports / live (n=105, roi=+0.27) | Esports / Esports / Counter Strike (n=96, roi=+0.25) | Esports (n=118, roi=+0.22) | Esports / Esports (n=118, roi=+0.22) | Esports / price=0.30-0.50 (n=48, roi=+0.30) | Esports / Esports / price=0.30-0.50 (n=48, roi=+0.30) | segment_only:t<2.0 |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1174 | Sports / Soccer / price=0.50-0.70 (n=85, roi=+0.28) | Sports / price=0.50-0.70 (n=130, roi=+0.21) | Sports / Soccer / type=moneyline (n=43, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | 0.1321 | Sports / price=0.50-0.70 (n=41, roi=+0.24) | Sports / Soccer / price=0.50-0.70 (n=41, roi=+0.24) | segment_only:t<2.0 |
| `0x9fd0170e55c00ffb1bf7218ccdbfc4d9048afe4f` | 0x9Fd0170e55C00FFb1bF7218CCDbFC4D9048afe4F-1780308598736 | 0.0538 | Sports / price=0.70-0.90 (n=31, roi=+0.12) | segment_only:t<2.0 |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | 0.1119 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.0517 | Sports / price=0.70-0.90 (n=75, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x366e29d46f9b2cac238eff1e0ac13a2ed08bcb0c` | jieshi1 | 0.0704 | Esports / Esports / type=moneyline (n=72, roi=+0.19) | segment_only:t<2.0 |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0627 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown |
| `0x13ce0f6f73a83a2be1eb484c91169c2bd5b935f0` | mozak | -0.0308 | Sports / Tennis / price=0.70-0.90 (n=31, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0177 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0053 | Sports / price=0.70-0.90 (n=131, roi=+0.06) | Sports / Soccer / Indian Premier League (n=97, roi=+0.07) | Sports / Soccer / price=0.70-0.90 (n=64, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0736 | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.32) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0123 | Esports / price=0.50-0.70 (n=106, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=106, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | 0.0065 | Sports / price=0.50-0.70 (n=137, roi=+0.11) | Sports / Soccer / price=0.50-0.70 (n=51, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0xaa9737b3db5d88aefcee007717a7c00b0df48c9c` | 0xf2cbF139C52b66c568dA19EF028f085289597B0e-1777085067547 | 0.1647 | Sports / Soccer (n=52, roi=+0.40) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2c50b0b2992ea5cb444a6097b68bcd9fb09589b6` | greenmachineofcsrjsdis | 0.0442 | Esports / Esports / type=map_handicap (n=36, roi=+0.20) | Esports / price=0.70-0.90 (n=30, roi=+0.13) | Esports / Esports / price=0.70-0.90 (n=30, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x51c7d30511ed096b39a9392bad97e0dc76c298aa` | Chopperyyy | 0.0174 | Esports / Esports / Counter Strike (n=298, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0xeef382e6c8cb7adde63551043659b381b1c00547` | xiaomikang | 0.0494 | Esports / price=0.10-0.30 (n=41, roi=+0.47) | Esports / Esports / price=0.10-0.30 (n=41, roi=+0.47) | Esports / Esports / type=child_moneyline (n=214, roi=+0.20) | Esports (n=296, roi=+0.17) | Esports / Esports (n=296, roi=+0.17) | Esports / Esports / League of Legends (n=294, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0xe70ce7a94ee228d75c97b0bdbf2a5eb0e3e11512` | 666CosmicOwl | 0.0177 | Sports / Tennis (n=106, roi=+0.11) | Sports / Tennis / type=moneyline (n=101, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x43fe17cf68eb58be1d40514be0e52674b71d26ee` | 0x43fE17Cf68EB58BE1d40514Be0e52674B71d26eE-1768993726139 | 0.0599 | Sports / Basketball / price=0.30-0.50 (n=42, roi=+0.28) | Sports / Cricket / price=0.50-0.70 (n=148, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x12d3cbfc0b5e095d03cb2a04f0676e46615d16c5` |  | 0.1213 | Sports / price=0.70-0.90 (n=34, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x70d8a64b823ae3843fc6c99c6c4ff1bdd911d2ba` |  | 0.1211 | Esports / price=0.30-0.50 (n=49, roi=+0.34) | Esports / Esports / price=0.30-0.50 (n=49, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown |
| `0x0e9781eec995a96a253291a2a20b282336a48ffa` | Peupo012 | 0.1449 | Sports / Soccer / price=0.50-0.70 (n=120, roi=+0.13) | Sports / price=0.50-0.70 (n=124, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbb360c54a7f8135407954450592f47d6bc940d51` | PiThree14 | 0.2252 | Sports / price=0.00-0.10 (n=45, roi=+1.82) | Sports / Other sport / Elon Tweets (n=114, roi=+0.80) | Sports (n=227, roi=+0.55) | Sports / price=0.50-0.70 (n=45, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 917 | 0.3309 | 0.2467 | 10.18 | 0.746 | 8.0 | 1.11 | 33916 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 210 | 13.2015 | 12.1736 | 5.88 | 0.219 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8876 | 5.01 | 0.351 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 823 | 2.9529 | 2.9048 | 2.23 | 0.225 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 824 | 2.9487 | 2.9007 | 2.23 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2178 | 3.53 | 0.794 |
| `0x86c878cd…` | Sports / Tennis / live | 750 | 2.517 | 2.4875 | 4.63 | 0.66 |
| `0x86c878cd…` | Sports | 2227 | 1.4251 | 1.4247 | 6.27 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 829 | 2.3418 | 2.3192 | 4.75 | 0.648 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 83 | 7.0292 | 5.9323 | 2.58 | 0.133 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3995 | 2.85 | 0.269 |
| `0x1941ca5d…` | Sports / Other sport | 2862 | 0.942 | 0.9419 | 2.47 | 0.53 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2862 | 0.942 | 0.9419 | 2.47 | 0.53 |
| `0x1941ca5d…` | Sports | 2864 | 0.9414 | 0.9413 | 2.47 | 0.53 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 65 | 7.8118 | 6.1149 | 2.73 | 0.215 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1876 | 2.73 | 0.665 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9293 | 2.43 | 0.3 |
| `0x86c878cd…` | Sports / Tennis / ATP | 396 | 1.9184 | 1.8926 | 3.11 | 0.631 |
| `0x1985327e…` | Sports | 1281 | 1.0219 | 1.0219 | 2.6 | 0.718 |
| `0x1985327e…` | Sports / Soccer / live | 832 | 1.2283 | 1.2234 | 2.04 | 0.706 |
| `0x1985327e…` | Sports / Soccer | 842 | 1.2136 | 1.2092 | 2.04 | 0.704 |
| `0x1941ca5d…` | Sports / Other sport / live | 2164 | 0.7281 | 0.7299 | 3.59 | 0.573 |
| `0x09b045ba…` | Sports | 1613 | 0.7953 | 0.7952 | 9.67 | 0.715 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.809 | 2.81 | 0.664 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 119 | 2.9631 | 2.651 | 2.94 | 0.395 |
| `0x86c878cd…` | Sports / Tennis / ITF | 179 | 2.2427 | 2.156 | 2.04 | 0.659 |
| `0xe337f5a2…` | Sports / price=0.00-0.10 | 135 | 2.8009 | 2.4697 | 2.47 | 0.348 |
| `0x03c9e3c6…` | Sports | 1017 | 0.8844 | 0.8844 | 7.11 | 0.698 |
| `0x86c878cd…` | Sports / Other sport / live | 149 | 2.4302 | 2.306 | 2.14 | 0.752 |
| `0xaa930fdc…` | Sports / price=0.00-0.10 | 804 | 0.9823 | 0.9665 | 2.27 | 0.098 |
| `0xaa930fdc…` | Sports / Other sport / price=0.00-0.10 | 793 | 0.9884 | 0.9722 | 2.25 | 0.097 |
| `0x482acc0c…` | Sports / Soccer / price=0.00-0.10 | 224 | 1.9301 | 1.7981 | 2.23 | 0.116 |
| `0x86c878cd…` | Sports / Other sport | 191 | 1.9639 | 1.9086 | 2.21 | 0.749 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 183 | 2.141 | 1.946 | 2.4 | 0.126 |
| `0x41558102…` | Sports / price=0.10-0.30 | 328 | 1.5216 | 1.4528 | 11.74 | 0.601 |
| `0x09b045ba…` | Sports / price=0.10-0.30 | 391 | 1.299 | 1.2745 | 11.35 | 0.591 |
| `0x41558102…` | Sports | 6029 | 0.3237 | 0.3237 | 10.3 | 0.851 |
| `0x86c878cd…` | Sports / Soccer | 908 | 0.82 | 0.8321 | 3.17 | 0.629 |
| `0x03c9e3c6…` | Sports / price=0.00-0.10 | 58 | 4.1111 | 3.2837 | 2.06 | 0.328 |
| `0x86c878cd…` | Sports / Soccer / live | 743 | 0.8995 | 0.9121 | 2.85 | 0.598 |
| `0x09b045ba…` | Sports / Soccer / live | 1025 | 0.7748 | 0.7751 | 6.69 | 0.708 |
| `0x09b045ba…` | Sports / Soccer | 1031 | 0.7693 | 0.7698 | 6.68 | 0.708 |
| `0x76697d10…` | Sports / Basketball / live | 951 | 0.7982 | 0.7941 | 3.83 | 0.576 |
| `0x76697d10…` | Sports / Basketball | 952 | 0.7963 | 0.7923 | 3.82 | 0.576 |
| `0x122b758a…` | Sports / price=0.00-0.10 | 302 | 1.4727 | 1.4035 | 2.51 | 0.162 |
| `0x76697d10…` | Sports / Basketball / type=totals | 628 | 0.9795 | 0.9677 | 3.19 | 0.557 |
| `0x03c9e3c6…` | Sports / price=0.10-0.30 | 281 | 1.4744 | 1.4352 | 10.4 | 0.655 |
| `0x482acc0c…` | Sports / price=0.00-0.10 | 262 | 1.5685 | 1.4799 | 2.11 | 0.115 |
| `0x03c9e3c6…` | Sports / Soccer / live | 692 | 0.9092 | 0.9085 | 5.52 | 0.681 |
| `0x03c9e3c6…` | Sports / Soccer | 701 | 0.9016 | 0.9011 | 5.54 | 0.683 |
| `0x3968f7c9…` | Sports | 986 | 0.7478 | 0.7478 | 6.49 | 0.734 |
| `0x91feec8a…` | Sports / Soccer / price=0.00-0.10 | 289 | 1.4378 | 1.3615 | 3.08 | 0.121 |
| `0x153a9a2f…` | Sports | 999 | 0.7116 | 0.7116 | 11.53 | 0.689 |
| `0x91feec8a…` | Sports / price=0.00-0.10 | 297 | 1.3721 | 1.3019 | 3.02 | 0.118 |
| `0x76697d10…` | Sports | 1392 | 0.6009 | 0.6009 | 4.18 | 0.603 |
| `0x09b045ba…` | Sports / Soccer / price=0.00-0.10 | 69 | 3.2315 | 2.6838 | 2.03 | 0.348 |
| `0x820a0e91…` | Sports / Tennis / pre | 102 | 2.5178 | 2.1872 | 2.75 | 0.422 |
| `0x91feec8a…` | Sports / Soccer / live | 2469 | 0.4385 | 0.4371 | 7.12 | 0.58 |
| `0x3968f7c9…` | Sports / Soccer | 687 | 0.8184 | 0.8163 | 5.03 | 0.718 |
| `0x037305f4…` | Other | 245 | 1.4525 | 1.3584 | 15.97 | 0.845 |
| `0x037305f4…` | Other / ? | 245 | 1.4525 | 1.3584 | 15.97 | 0.845 |
