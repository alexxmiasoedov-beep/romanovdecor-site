# Отчёт воронки, 2026-09-25 05:42 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 7620 |
| 0. Из них не только 5-мин крипта | 6307 |
| 1. Прошли дешёвые отсечки | 847 из 6307 |
| 2. Прошли по полной истории | 2 + сегментом 18 из 847 |
| 3. Прошли реалистичный вход | 8 из 20 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3162 |
| history<90d | 1795 |
| open_now>10 | 1460 |
| closed<50 | 1136 |
| entries>=0.90 | 1132 |
| top1_concentration | 985 |
| short_crypto | 537 |
| profit_from<0.10 | 440 |
| positions>5000 | 86 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| drawdown | 746 |
| concurrency_p95>8 | 714 |
| t<2.0 | 707 |
| unstable_halves | 527 |
| roi_copy<=0 | 347 |
| low_liquidity | 198 |
| both_sides | 158 |
| history<90d | 123 |
| hold<1h | 64 |
| entries>=0.90 | 47 |
| short_crypto | 31 |
| sniping | 21 |
| segment_only:t<2.0 | 18 |
| segment_only:drawdown | 13 |
| profit_from<0.10 | 9 |
| top1_concentration | 9 |
| closed<50 | 8 |
| segment_only:unstable_halves | 8 |
| segment_only:roi_copy<=0 | 2 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 10 |
| edge_decays_with_delay | 2 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe478d4ca1c959e78f4ad9e563b134c54363128ea` | gmomoney | Sports | 0.1437 | 2.23 | 0.1416 | 0.1799 | 0.1657 | 7.0 | 6.49 | н/д | Sports / price=0.50-0.70 (n=106, roi=+0.21) | Sports (n=172, roi=+0.16) | Sports / Baseball / type=moneyline (n=40, roi=+0.29) | Sports / American Football / price=0.50-0.70 (n=33, roi=+0.32) |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | Sports | 0.0736 | 1.77 | 0.0933 | 0.1081 | 0.0631 | 5.0 | 2.95 | 0.0 | Sports / Soccer / pre (n=33, roi=+0.11) |
| `0x56dc1f57f224d88fc988444d765ffda09c78d397` | attract | Sports | 0.0674 | 1.81 | 0.1096 | 0.1265 | 0.0882 | 5.0 | 9.75 | 0.0 | Sports / Soccer / pre (n=170, roi=+0.15) | Sports / Soccer / type=both_teams_to_score (n=34, roi=+0.33) | Sports / Soccer (n=187, roi=+0.13) | Sports (n=198, roi=+0.11) | Sports / Soccer / price=0.50-0.70 (n=78, roi=+0.15) | Sports / price=0.50-0.70 (n=80, roi=+0.14) |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | Sports | 0.126 | 1.29 | 0.0372 | 0.0543 | 0.133 | 4.0 | 4.11 | 0.0019 | Sports / price=0.50-0.70 (n=35, roi=+0.20) | Sports / Soccer / price=0.50-0.70 (n=35, roi=+0.20) |
| `0x31550df5402226b825f900a31659a05d809d268e` | tizzles | Sports | 0.1608 | 1.46 | 0.0626 | 0.0783 | 0.0917 | 5.0 | 5.36 | 0.0 | Sports / MMA/Boxing / UFC (n=54, roi=+0.29) | Sports / MMA/Boxing / type=moneyline (n=53, roi=+0.29) | Sports / MMA/Boxing (n=61, roi=+0.26) | Sports / MMA/Boxing / pre (n=37, roi=+0.29) |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | Sports | 0.0321 | 1.76 | 0.1155 | 0.1309 | 0.1218 | 8.0 | 3.18 | 0.0 | Esports / price=0.50-0.70 (n=49, roi=+0.21) | Esports / Esports / price=0.50-0.70 (n=49, roi=+0.21) | Esports / Esports / Counter Strike (n=145, roi=+0.10) |
| `0xaab18830506d45d582007ff27cb35f3038d29678` | veys | Sports | 0.1181 | 1.08 | 0.0262 | 0.0471 | 0.0321 | 8.0 | 2.44 | н/д | Sports / Basketball / type=moneyline (n=35, roi=+0.13) |
| `0x7714c16f86bcfdba47bfcb161dc39a2a1ff2b814` | llllllIIIIIIlIllllllIIIIIIlIllllllIIIIIIlI | Esports | 0.0444 | 1.46 | 0.0918 | 0.1101 | 0.1411 | 8.0 | 3.25 | 0.0 | Sports / Soccer (n=62, roi=+0.35) | Sports (n=89, roi=+0.25) | Sports / Soccer / live (n=36, roi=+0.35) | Sports / Soccer / type=moneyline (n=34, roi=+0.32) | Sports / Soccer / price=0.50-0.70 (n=31, roi=+0.23) | Sports / price=0.50-0.70 (n=32, roi=+0.20) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | 0.0736 | Sports / Soccer / pre (n=33, roi=+0.11) | segment_only:t<2.0 |
| `0x56dc1f57f224d88fc988444d765ffda09c78d397` | attract | 0.0674 | Sports / Soccer / pre (n=170, roi=+0.15) | Sports / Soccer / type=both_teams_to_score (n=34, roi=+0.33) | Sports / Soccer (n=187, roi=+0.13) | Sports (n=198, roi=+0.11) | Sports / Soccer / price=0.50-0.70 (n=78, roi=+0.15) | Sports / price=0.50-0.70 (n=80, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0x31550df5402226b825f900a31659a05d809d268e` | tizzles | 0.1608 | Sports / MMA/Boxing / UFC (n=54, roi=+0.29) | Sports / MMA/Boxing / type=moneyline (n=53, roi=+0.29) | Sports / MMA/Boxing (n=61, roi=+0.26) | Sports / MMA/Boxing / pre (n=37, roi=+0.29) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xffcb2a10ff14a1060e7767c40a7a10ea7a0ad630` |  | 0.0442 | Esports / price=0.50-0.70 (n=98, roi=+0.14) | Esports / Esports / price=0.50-0.70 (n=98, roi=+0.14) | Esports / Esports / League of Legends (n=170, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | 0.126 | Sports / price=0.50-0.70 (n=35, roi=+0.20) | Sports / Soccer / price=0.50-0.70 (n=35, roi=+0.20) | segment_only:t<2.0 |
| `0x84ec5c73977668d5a140e01b0f78e4381f3f5696` | hartemma30 | 0.0821 | Sports / price=0.70-0.90 (n=32, roi=+0.16) | segment_only:t<2.0 |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | 0.0321 | Esports / price=0.50-0.70 (n=49, roi=+0.21) | Esports / Esports / price=0.50-0.70 (n=49, roi=+0.21) | Esports / Esports / Counter Strike (n=145, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0302 | Sports / Baseball / type=moneyline (n=39, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0185 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbbf94447dc1543d2c5fda33e29c89c2ae712d602` | EthanKoon | 0.0159 | Sports / Soccer / FIFA World Cup (n=97, roi=+0.03) | segment_only:t<2.0 |
| `0xaab18830506d45d582007ff27cb35f3038d29678` | veys | 0.1181 | Sports / Basketball / type=moneyline (n=35, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0083 | Esports / price=0.50-0.70 (n=105, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=105, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x191267f5c2074ccbfe4fe3d6996797148fdfdef8` | heal1god | 0.0494 | Sports / Hockey (n=35, roi=+0.31) | Sports / Hockey / NHL 2026 (n=35, roi=+0.31) | Sports / Hockey / type=moneyline (n=30, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x7714c16f86bcfdba47bfcb161dc39a2a1ff2b814` | llllllIIIIIIlIllllllIIIIIIlIllllllIIIIIIlI | 0.0444 | Sports / Soccer (n=62, roi=+0.35) | Sports (n=89, roi=+0.25) | Sports / Soccer / live (n=36, roi=+0.35) | Sports / Soccer / type=moneyline (n=34, roi=+0.32) | Sports / Soccer / price=0.50-0.70 (n=31, roi=+0.23) | Sports / price=0.50-0.70 (n=32, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0x43fe17cf68eb58be1d40514be0e52674b71d26ee` | 0x43fE17Cf68EB58BE1d40514Be0e52674B71d26eE-1768993726139 | 0.0421 | Sports / Cricket / price=0.50-0.70 (n=146, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.1223 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0x82882d761b0d7f18b2cc286117d10cd8a15a5519` | Sugarina | 0.1184 | Sports / Other sport / price=0.70-0.90 (n=40, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0e9781eec995a96a253291a2a20b282336a48ffa` | Peupo012 | 0.1717 | Sports / Soccer / price=0.50-0.70 (n=112, roi=+0.14) | Sports / price=0.50-0.70 (n=115, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 550 | 0.1911 | 0.101 | 5.64 | 0.529 | 6.0 | 6.12 | 364530 | delayed_roi<=0 |
| `0xe478d4ca1c959e78f4ad9e563b134c54363128ea` | gmomoney | Sports | 189 | 0.1437 | 0.1342 | 2.23 | 0.64 | 7.0 | 6.49 | 276885 | прошёл |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 818 | 2.9941 | 2.945 | 2.25 | 0.229 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 819 | 2.9898 | 2.9409 | 2.25 | 0.228 |
| `0xb595d09c…` | Sports / price=0.00-0.10 | 35 | 19.7064 | 12.5906 | 2.81 | 0.257 |
| `0x70feb53b…` | Sports / price=0.00-0.10 | 41 | 11.7778 | 8.4552 | 2.87 | 0.268 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.4062 | 2.85 | 0.269 |
| `0x1941ca5d…` | Sports / Other sport | 2837 | 0.9575 | 0.9573 | 2.49 | 0.527 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2837 | 0.9575 | 0.9573 | 2.49 | 0.527 |
| `0x1941ca5d…` | Sports | 2839 | 0.9569 | 0.9568 | 2.49 | 0.527 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 64 | 7.9495 | 6.2053 | 2.74 | 0.219 |
| `0xef185339…` | Sports | 3784 | 0.7333 | 0.7333 | 22.58 | 0.695 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9307 | 2.43 | 0.3 |
| `0xd60c6fa3…` | Sports | 3518 | 0.6922 | 0.6922 | 20.79 | 0.69 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 367 | 2.1346 | 2.0444 | 3.4 | 0.286 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 382 | 2.0746 | 1.9908 | 3.43 | 0.28 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1032 | 1.2011 | 1.1922 | 16.96 | 0.598 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 883 | 1.2346 | 1.2225 | 15.94 | 0.597 |
| `0xef185339…` | Sports / Soccer | 2548 | 0.708 | 0.7082 | 18.74 | 0.693 |
| `0xef185339…` | Sports / Soccer / live | 2514 | 0.7084 | 0.7086 | 18.55 | 0.691 |
| `0x1941ca5d…` | Sports / Other sport / live | 2147 | 0.7449 | 0.7467 | 3.64 | 0.57 |
| `0xd60c6fa3…` | Sports / Soccer | 2357 | 0.6872 | 0.6873 | 16.34 | 0.69 |
| `0xd60c6fa3…` | Sports / Soccer / live | 2314 | 0.6885 | 0.6885 | 16.13 | 0.688 |
| `0x70feb53b…` | Sports | 309 | 1.8714 | 1.8575 | 3.2 | 0.735 |
| `0xef185339…` | Sports / Soccer / price=0.10-0.30 | 672 | 1.2287 | 1.2144 | 13.95 | 0.609 |
| `0xa06f5b95…` | Other | 106 | 3.5243 | 3.028 | 6.36 | 0.755 |
| `0xa06f5b95…` | Other / ? | 106 | 3.5243 | 3.028 | 6.36 | 0.755 |
| `0xa06f5b95…` | Other / ? / ? | 106 | 3.5243 | 3.028 | 6.36 | 0.755 |
| `0xa06f5b95…` | Other / ? / type=binary | 106 | 3.5243 | 3.028 | 6.36 | 0.755 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8107 | 2.81 | 0.664 |
| `0xd60c6fa3…` | Sports / Soccer / price=0.10-0.30 | 580 | 1.2395 | 1.2212 | 13.11 | 0.61 |
| `0xef185339…` | Sports / price=0.00-0.10 | 229 | 1.9632 | 1.8643 | 5.24 | 0.485 |
| `0x03c9e3c6…` | Sports | 980 | 0.8998 | 0.8998 | 6.99 | 0.701 |
| `0xef185339…` | Sports / Other sport / live | 1229 | 0.7801 | 0.7794 | 12.59 | 0.697 |
| `0xef185339…` | Sports / Other sport | 1230 | 0.7787 | 0.7779 | 12.57 | 0.697 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 180 | 2.1934 | 1.99 | 2.42 | 0.128 |
| `0x76b8356b…` | Culture / price=0.00-0.10 | 282 | 1.6563 | 1.5817 | 2.01 | 0.326 |
| `0x41558102…` | Sports / price=0.10-0.30 | 323 | 1.5466 | 1.4755 | 11.83 | 0.604 |
| `0x164cb85e…` | Sports / Other sport / type=binary | 2923 | 0.4741 | 0.4735 | 5.79 | 0.554 |
| `0x03c9e3c6…` | Sports / price=0.00-0.10 | 55 | 4.3797 | 3.4518 | 2.09 | 0.345 |
| `0x164cb85e…` | Sports / Other sport | 2947 | 0.4706 | 0.4701 | 5.79 | 0.555 |
| `0x482acc0c…` | Sports / Soccer / price=0.00-0.10 | 214 | 1.8619 | 1.7297 | 2.08 | 0.112 |
| `0x41558102…` | Sports | 5900 | 0.3279 | 0.3279 | 10.22 | 0.85 |
| `0x76697d10…` | Sports / Basketball / live | 948 | 0.8039 | 0.8002 | 3.84 | 0.578 |
| `0x76697d10…` | Sports / Basketball | 949 | 0.802 | 0.7983 | 3.84 | 0.577 |
| `0x164cb85e…` | Sports | 3219 | 0.4303 | 0.4301 | 5.75 | 0.551 |
| `0x76697d10…` | Sports / Basketball / type=totals | 627 | 0.9826 | 0.9715 | 3.19 | 0.558 |
| `0x164cb85e…` | Sports / Other sport / Shanghai Daily Lowest Temperature | 285 | 1.5091 | 1.4357 | 2.22 | 0.558 |
| `0xd60c6fa3…` | Sports / Other sport / live | 1156 | 0.7028 | 0.7026 | 13.02 | 0.69 |
| `0x03c9e3c6…` | Sports / Soccer / live | 660 | 0.93 | 0.9291 | 5.4 | 0.682 |
| `0xd60c6fa3…` | Sports / Other sport | 1157 | 0.7013 | 0.7012 | 13.0 | 0.69 |
| `0x03c9e3c6…` | Sports / Soccer | 669 | 0.9218 | 0.9212 | 5.42 | 0.685 |
| `0x03c9e3c6…` | Sports / price=0.10-0.30 | 271 | 1.4764 | 1.4368 | 10.21 | 0.653 |
| `0xef185339…` | Sports / Soccer / type=moneyline | 517 | 1.0173 | 1.0067 | 9.68 | 0.741 |
| `0x76697d10…` | Sports | 1322 | 0.625 | 0.6249 | 4.13 | 0.606 |
| `0x164cb85e…` | Sports / Other sport / live | 2710 | 0.4366 | 0.4362 | 5.79 | 0.561 |
| `0xd60c6fa3…` | Sports / price=0.00-0.10 | 197 | 1.6691 | 1.579 | 3.98 | 0.426 |
| `0x91feec8a…` | Sports / Soccer / price=0.00-0.10 | 263 | 1.4361 | 1.353 | 2.87 | 0.118 |
| `0x91feec8a…` | Sports / price=0.00-0.10 | 268 | 1.3907 | 1.3122 | 2.83 | 0.116 |
| `0x91feec8a…` | Sports / Soccer / live | 2206 | 0.4588 | 0.457 | 6.84 | 0.577 |
| `0xef185339…` | Sports / price=0.30-0.50 | 1290 | 0.586 | 0.5882 | 21.36 | 0.709 |
| `0xd60c6fa3…` | Sports / Soccer / type=moneyline | 450 | 1.0064 | 0.993 | 7.58 | 0.74 |
