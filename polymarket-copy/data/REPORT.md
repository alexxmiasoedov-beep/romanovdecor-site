# Отчёт воронки, 2026-10-20 07:16 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 55252 |
| 0. Из них не только 5-мин крипта | 53123 |
| 1. Прошли дешёвые отсечки | 3875 из 24259 |
| 2. Прошли по полной истории | 5 + сегментом 39 из 3875 |
| 3. Прошли реалистичный вход | 1 из 44 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 11956 |
| closed<50 | 10007 |
| top1_concentration | 8898 |
| entries>=0.90 | 5053 |
| history<90d | 4188 |
| open_now>10 | 3358 |
| short_crypto | 1745 |
| profit_from<0.10 | 1742 |
| positions>5000 | 151 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3502 |
| concurrency_p95>8 | 3068 |
| drawdown | 2922 |
| unstable_halves | 2571 |
| roi_copy<=0 | 1510 |
| silent | 714 |
| low_liquidity | 631 |
| both_sides | 546 |
| top1_concentration | 300 |
| history<90d | 285 |
| closed<50 | 245 |
| hold<1h | 159 |
| entries>=0.90 | 143 |
| short_crypto | 91 |
| profit_from<0.10 | 47 |
| sniping | 37 |
| segment_only:t<2.0 | 37 |
| segment_only:drawdown | 33 |
| segment_only:unstable_halves | 23 |
| segment_only:roi_copy<=0 | 11 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 39 |
| edge_decays_with_delay | 4 |
| slippage | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xf0ecc3bc923b08652336f7e8f8a130943c1dfea4` |  | Sports | 0.2796 | 2.14 | 0.2084 | 0.2445 | 0.3817 | 4.0 | 4.34 | н/д | Sports / Soccer (n=50, roi=+0.33) | Sports / Soccer / type=moneyline (n=50, roi=+0.33) | Sports (n=54, roi=+0.29) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xbc52fdc1a96f9cc2b9d61fad6088ef09d50fa021` | Fox72 | -0.0481 | Crypto / price=0.70-0.90 (n=73, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0577 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.0358 | Sports / price=0.50-0.70 (n=101, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x96d9da943660be27aed7230166eaac467c5718a0` | uw0tm8 | -0.0469 | Sports / Soccer / Bundesliga 2025 (n=30, roi=+0.20) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5966e14a24015bdf52da7b1cd35a7afc7febaf5d` | betwithconvic | 0.0568 | Esports / price=0.50-0.70 (n=42, roi=+0.22) | Esports / Esports / price=0.50-0.70 (n=42, roi=+0.22) | segment_only:t<2.0;segment_only:drawdown |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0963 | Esports / Esports / Valorant (n=55, roi=+0.29) | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1554 | Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / price=0.10-0.30 (n=112, roi=+0.51) | Esports / Esports / type=child_moneyline (n=614, roi=+0.18) | Esports (n=712, roi=+0.16) | Esports / Esports (n=712, roi=+0.16) | Esports / Esports / Dota 2 (n=712, roi=+0.16) | segment_only:drawdown |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0335 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0158 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0578 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | Sports / Soccer / price=0.70-0.90 (n=82, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x20255f1ed1e9db14d2c663b588cbcc41306113c0` | 182837282 | -0.0165 | Sports / Tennis / price=0.70-0.90 (n=61, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0187 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0119 | Sports / Soccer / price=0.50-0.70 (n=59, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd2e740480d0f864d8520fc0627ab94c49322131` | 0xFd2e740480D0F864d8520FC0627ab94c49322131-1769035449764 | 0.0194 | Sports / Baseball (n=38, roi=+0.13) | Sports / Baseball / MLB (n=38, roi=+0.13) | Sports / Baseball / type=moneyline (n=38, roi=+0.13) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | -0.0018 | Sports / Soccer / pre (n=39, roi=+0.23) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.022 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x6876472b48f488a144c79e51cba56f9527598dc9` | Magnabelli | -0.0039 | Sports / Other sport / price=0.70-0.90 (n=61, roi=+0.10) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa236024a7acfc8f32f850ba72b68664ed1564cbb` | ganzarolli | 0.001 | Sports / Soccer / price=0.70-0.90 (n=64, roi=+0.11) | Sports / price=0.70-0.90 (n=72, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0086 | Esports / price=0.50-0.70 (n=48, roi=+0.20) | Esports / Esports / price=0.50-0.70 (n=48, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf45719992a8b4515da551a4f8b75cb735220d1a6` | krokozaur | 0.011 | Esports / Esports / type=child_moneyline (n=85, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1d2a24c3c963c45b481ee5f1da90fa0efddb8f8f` | 0x1d2A24C3c963C45B481ee5F1Da90Fa0EFDDB8F8F-1772559011215 | 0.082 | Sports / Soccer / live (n=45, roi=+0.29) | segment_only:t<2.0 |
| `0x67a8dd1c146d6ac9e5d220dba3985c9676feb281` | santacar | 0.0103 | Sports / Soccer / type=moneyline (n=97, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0218 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0157 | Sports / Baseball / type=totals (n=36, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1264dc2f4d22bcf4e2e3ade2c859e9f3476625f1` | 0x1264DC2f4d22BCF4E2E3ADE2C859e9F3476625f1-1760612464589 | 0.2039 | Sports / Basketball (n=51, roi=+0.28) | Sports / Basketball / NBA 2026 (n=51, roi=+0.28) | segment_only:t<2.0 |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1352 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.38) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0412 | Esports / price=0.50-0.70 (n=47, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=47, roi=+0.18) | segment_only:t<2.0 |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0528 | Sports / American Football / pre (n=57, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbcf51140fd48e69c6e6d4bd09d38a629059856a1` | bqy0301 | 0.199 | Sports / price=0.30-0.50 (n=36, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0x9cbb674bdacc27020e6adb549461e45ade24a2e1` | Tentm1 | 0.0346 | Sports / American Football / NFL (n=41, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown |
| `0x880dbf161120207d47aef05ec774b331bcec39bc` | akulaxl | 0.0289 | Esports / Esports / type=moneyline (n=53, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0397 | Sports / Basketball / NBA 2026 (n=37, roi=+0.47) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x66db92250e63e86365eec54fce57dcec7a90370f` | koei73 | 0.0476 | Sports / Soccer / type=totals (n=121, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown |
| `0x1d169955b78ad2885e725717e5928eec33c9212e` | HONGKONGPEACH | 0.0445 | Sports / Basketball (n=42, roi=+0.23) | Sports / Soccer / price=0.50-0.70 (n=50, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xbafa197f7eecfc2fd2fe348cb995bba6812402e0` | Sylas | 0.0367 | Esports / price=0.50-0.70 (n=460, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=460, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe23cd5fb6bee7b1c9f60f5d9969ac7ba52cc5ae7` | apprentice15 | 0.2214 | Sports / Soccer / type=totals (n=89, roi=+0.79) | Sports / Soccer / live (n=529, roi=+0.26) | Sports / Soccer (n=541, roi=+0.26) | Sports (n=657, roi=+0.22) | Sports / price=0.10-0.30 (n=136, roi=+0.37) | Sports / Soccer / price=0.30-0.50 (n=178, roi=+0.21) | segment_only:drawdown |
| `0x739d1e72481dafd777bf4e57f7b89a6a73abd2ff` | 0x739D1e72481dAfd777Bf4e57f7b89A6a73Abd2fF-1761571315579 | 0.088 | Sports / Soccer / Serie A 2025 (n=79, roi=+0.43) | segment_only:t<2.0;segment_only:drawdown |
| `0x7ce336595687024c9ebf620f2dcb3b71269b1689` | 0x7Ce336595687024C9ebF620F2dCb3b71269B1689-1774766944047 | 0.0863 | Sports / Other sport / live (n=748, roi=+0.15) | Sports / Other sport / Hong Kong Daily Weather (n=489, roi=+0.18) | Sports / Other sport / type=binary (n=856, roi=+0.13) | Sports / Other sport / price=0.10-0.30 (n=354, roi=+0.20) | Sports / Other sport (n=860, roi=+0.13) | Sports / price=0.10-0.30 (n=370, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x0e9781eec995a96a253291a2a20b282336a48ffa` | Peupo012 | 0.2188 | Sports / price=0.50-0.70 (n=145, roi=+0.15) | Sports / Soccer / price=0.50-0.70 (n=140, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xf0ecc3bc923b08652336f7e8f8a130943c1dfea4` |  | Sports | 59 | 0.2796 | 0.2242 | 2.14 | 0.576 | 4.0 | 4.34 | 939739 | прошёл |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 518 | 0.1815 | 0.0915 | 5.13 | 0.525 | 5.0 | 5.96 | 328932 | delayed_roi<=0 |
| `0xd670301420f6011e8136b07c50d7f4002bcee98f` | Mrpitter | Culture | 90 | 0.5276 | 0.1197 | 2.03 | 0.544 | 8.0 | 23.31 | 70640 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 781 | 0.1125 | 0.0497 | 3.39 | 0.713 | 8.0 | 2.73 | 396955 | delayed_roi<=0 |
| `0x87909a89ee551c8616e5bff9089c81545bfd010b` | Castolo | Sports | 1452 | 0.2414 | 0.0419 | 6.22 | 0.554 | 8.0 | 2.44 | 58136 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 253 | 23.3322 | 21.901 | 4.03 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 19.0751 | 5.97 | 0.516 |
| `0xe8ca3f75…` | Sports | 1516 | 4.3169 | 4.3101 | 4.37 | 0.709 |
| `0x465ace6e…` | Sports / price=0.00-0.10 | 53 | 27.2334 | 20.9943 | 5.25 | 0.566 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 99 | 14.9322 | 12.9051 | 4.12 | 0.182 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2885 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.7661 | 4.16 | 0.626 |
| `0xe8ca3f75…` | Sports / Tennis | 552 | 4.2226 | 4.2077 | 5.87 | 0.719 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3936 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3936 | 3.78 | 0.177 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 810 | 3.3971 | 3.3397 | 2.39 | 0.221 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 811 | 3.3923 | 3.3351 | 2.39 | 0.221 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9622 | 3.45 | 0.324 |
| `0x465ace6e…` | Sports | 319 | 5.1335 | 5.0938 | 5.03 | 0.712 |
| `0x465ace6e…` | Sports / Tennis | 136 | 7.8667 | 7.43 | 3.98 | 0.706 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 247 | 5.5366 | 5.2029 | 3.98 | 0.138 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4807 | 3.61 | 0.17 |
| `0x465ace6e…` | Sports / Tennis / WTA | 36 | 17.6494 | 12.9392 | 2.99 | 0.778 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6108 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.6108 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.4416 | 3.33 | 0.754 |
| `0xeda67a7f…` | Sports | 494 | 3.2216 | 3.2079 | 4.17 | 0.549 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 252 | 4.3811 | 4.338 | 4.0 | 0.73 |
| `0x465ace6e…` | Sports / Tennis / live | 57 | 10.4394 | 8.8865 | 2.77 | 0.789 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8327 | 2.82 | 0.131 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 107 | 6.8555 | 5.8327 | 2.82 | 0.131 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.5554 | 2.28 | 0.167 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6201 | 2.81 | 0.636 |
| `0x231034fb…` | Sports / price=0.00-0.10 | 80 | 7.8545 | 6.3839 | 2.89 | 0.4 |
| `0x1941ca5d…` | Sports / Other sport | 2928 | 1.0354 | 1.0352 | 2.63 | 0.55 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2928 | 1.0354 | 1.0352 | 2.63 | 0.55 |
| `0x1941ca5d…` | Sports | 2930 | 1.0348 | 1.0346 | 2.63 | 0.55 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3843 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 62 | 8.6662 | 6.648 | 3.13 | 0.242 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 32 | 13.0625 | 9.1425 | 2.16 | 0.156 |
| `0x465ace6e…` | Sports / Tennis / pre | 79 | 6.0105 | 5.6974 | 2.94 | 0.646 |
| `0x41558102…` | Sports / price=0.00-0.10 | 42 | 10.8879 | 7.4801 | 2.64 | 0.31 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 68 | 7.4231 | 5.8599 | 2.71 | 0.206 |
| `0xe8ca3f75…` | Esports / Esports / live | 149 | 3.9107 | 3.897 | 2.82 | 0.57 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.6123 | 2.86 | 0.07 |
| `0x465ace6e…` | Sports / Tennis / ATP | 56 | 6.9698 | 6.3095 | 2.62 | 0.732 |
| `0xe8ca3f75…` | Esports | 457 | 2.0659 | 2.1384 | 4.27 | 0.656 |
| `0xe8ca3f75…` | Esports / Esports | 457 | 2.0659 | 2.1384 | 4.27 | 0.656 |
| `0xef185339…` | Sports | 3853 | 0.7306 | 0.7306 | 22.73 | 0.69 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 8.0232 | 5.01 | 0.567 |
| `0xe8ca3f75…` | Sports / American Football / pre | 44 | 7.7696 | 6.5277 | 4.77 | 0.568 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 41 | 8.1552 | 6.7258 | 4.71 | 0.561 |
| `0xc9ccb64f…` | Sports / price=0.00-0.10 | 108 | 4.7059 | 4.026 | 2.85 | 0.537 |
| `0xe8ca3f75…` | Sports / American Football | 52 | 6.5329 | 5.7725 | 4.55 | 0.538 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 432 | 1.9129 | 1.9962 | 4.77 | 0.766 |
| `0xb209ec04…` | Sports | 1586 | 1.0375 | 1.0381 | 4.63 | 0.516 |
| `0xd60c6fa3…` | Sports | 3592 | 0.6862 | 0.6862 | 20.89 | 0.685 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1721 | 2.41 | 0.526 |
| `0xb209ec04…` | Sports / Soccer | 892 | 1.3741 | 1.3677 | 4.01 | 0.51 |
| `0x1941ca5d…` | Sports / Other sport / live | 2228 | 0.8592 | 0.8606 | 3.34 | 0.593 |
| `0xb209ec04…` | Esports / Esports / live | 968 | 1.3078 | 1.3033 | 3.76 | 0.506 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.6279 | 3.4 | 0.478 |
| `0xb209ec04…` | Esports | 1224 | 1.1399 | 1.1389 | 4.05 | 0.5 |
| `0xb209ec04…` | Esports / Esports | 1224 | 1.1399 | 1.1389 | 4.05 | 0.5 |
