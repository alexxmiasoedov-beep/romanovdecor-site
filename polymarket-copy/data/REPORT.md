# Отчёт воронки, 2026-10-10 07:04 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 52963 |
| 0. Из них не только 5-мин крипта | 50792 |
| 1. Прошли дешёвые отсечки | 4042 из 13407 |
| 2. Прошли по полной истории | 2 + сегментом 53 из 4042 |
| 3. Прошли реалистичный вход | 7 из 55 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 5956 |
| closed<50 | 5151 |
| top1_concentration | 4636 |
| entries>=0.90 | 2993 |
| history<90d | 2170 |
| short_crypto | 852 |
| profit_from<0.10 | 490 |
| open_now>10 | 452 |
| positions>5000 | 17 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3616 |
| concurrency_p95>8 | 3169 |
| drawdown | 3116 |
| unstable_halves | 2626 |
| roi_copy<=0 | 1586 |
| silent | 657 |
| low_liquidity | 656 |
| both_sides | 601 |
| history<90d | 306 |
| top1_concentration | 274 |
| closed<50 | 220 |
| hold<1h | 169 |
| entries>=0.90 | 148 |
| short_crypto | 87 |
| profit_from<0.10 | 55 |
| sniping | 52 |
| segment_only:t<2.0 | 51 |
| segment_only:drawdown | 43 |
| segment_only:unstable_halves | 28 |
| segment_only:roi_copy<=0 | 12 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 45 |
| edge_decays_with_delay | 3 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x9cde12fb942486019ed19e505806715a8761b413` | jrf96 | Sports | 0.1577 | 2.51 | 0.1583 | 0.1632 | 0.0984 | 5.0 | 18.01 | 0.0 | Sports / price=0.50-0.70 (n=35, roi=+0.29) | Sports / Soccer / price=0.50-0.70 (n=33, roi=+0.28) | Sports / Soccer (n=92, roi=+0.16) | Sports (n=95, roi=+0.16) | Sports / Soccer / type=moneyline (n=87, roi=+0.15) | Sports / Soccer / pre (n=88, roi=+0.14) |
| `0x4eb8f3538c86bd47a57e24c6f071285d67f7a474` | cryptopsihoz | Sports | 0.1686 | 1.79 | 0.1111 | 0.1266 | 0.1787 | 5.0 | 6.42 | н/д | Sports / Soccer / pre (n=74, roi=+0.29) | Sports / Soccer (n=101, roi=+0.21) | Sports / Soccer / price=0.30-0.50 (n=30, roi=+0.32) |
| `0x88cf4a6cd2dc68cbb3b31893c1ed3a11692060f2` |  | Sports | 0.2065 | 1.96 | 0.0744 | 0.0963 | 0.2417 | 5.0 | 4.14 | 0.0 | Sports / Soccer (n=97, roi=+0.22) | Sports / price=0.70-0.90 (n=37, roi=+0.17) | Sports / Soccer / price=0.70-0.90 (n=37, roi=+0.17) |
| `0xa4e37c28e82775164a1523ed96b98365a40b34e6` | cryptocrazySR | Sports | 0.1031 | 1.25 | 0.0527 | 0.0703 | 0.1008 | 5.0 | 8.43 | н/д | Sports / price=0.30-0.50 (n=63, roi=+0.27) |
| `0x3daaab16fb3ad3ce660b881a0700c458a972524b` | 0x3daAaB16fb3Ad3cE660b881A0700c458A972524b-1781488757957 | Sports | 0.0985 | 1.38 | 0.034 | 0.0546 | 0.0961 | 5.0 | 3.66 | 0.0 | Sports / Tennis / price=0.50-0.70 (n=44, roi=+0.20) |
| `0x733b2ffa4ebfd125ee71e8b673bd08273abd7260` | tony1919 | Esports | 0.0401 | 0.83 | 0.0462 | 0.0656 | 0.0375 | 3.0 | 5.21 | н/д | Esports (n=76, roi=+0.11) | Esports / Esports / pre (n=39, roi=+0.15) | Esports / Esports (n=71, roi=+0.11) | Esports / Esports / type=moneyline (n=57, roi=+0.10) |
| `0xdfe23feed07253802f68688506218be25cc97e2b` | Slimshabi | Sports | 0.0283 | 0.37 | 0.0005 | 0.0127 | -0.04 | 4.0 | 2.9 | н/д | Sports / Soccer / pre (n=30, roi=+0.20) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0x4eb8f3538c86bd47a57e24c6f071285d67f7a474` | cryptopsihoz | 0.1686 | Sports / Soccer / pre (n=74, roi=+0.29) | Sports / Soccer (n=101, roi=+0.21) | Sports / Soccer / price=0.30-0.50 (n=30, roi=+0.32) | segment_only:t<2.0 |
| `0x88cf4a6cd2dc68cbb3b31893c1ed3a11692060f2` |  | 0.2065 | Sports / Soccer (n=97, roi=+0.22) | Sports / price=0.70-0.90 (n=37, roi=+0.17) | Sports / Soccer / price=0.70-0.90 (n=37, roi=+0.17) | segment_only:t<2.0 |
| `0xbc52fdc1a96f9cc2b9d61fad6088ef09d50fa021` | LinusM | -0.0592 | Crypto / price=0.70-0.90 (n=47, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0609 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0617 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1016 | Sports / Soccer / price=0.50-0.70 (n=92, roi=+0.25) | Sports / Soccer / type=moneyline (n=51, roi=+0.26) | segment_only:t<2.0;segment_only:drawdown |
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.0374 | Sports / price=0.50-0.70 (n=99, roi=+0.17) | Sports / Tennis / price=0.50-0.70 (n=74, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa4e37c28e82775164a1523ed96b98365a40b34e6` | cryptocrazySR | 0.1031 | Sports / price=0.30-0.50 (n=63, roi=+0.27) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.17 | Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / type=child_moneyline (n=577, roi=+0.19) | Esports (n=671, roi=+0.17) | Esports / Esports (n=671, roi=+0.17) | Esports / Esports / Dota 2 (n=671, roi=+0.17) | segment_only:drawdown |
| `0x73da1e371be9c623b3d80b86c42eacd92977b7ac` | ZOFGK | -0.0566 | Esports / Esports / pre (n=37, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3daaab16fb3ad3ce660b881a0700c458a972524b` | 0x3daAaB16fb3Ad3cE660b881A0700c458A972524b-1781488757957 | 0.0985 | Sports / Tennis / price=0.50-0.70 (n=44, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0x1f9e0fa8e8780246d637f40af24b331044c23d5d` |  | -0.0343 | Sports / price=0.50-0.70 (n=173, roi=+0.11) | Sports / Soccer / price=0.50-0.70 (n=123, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x89879980a13fb82269cc489154fafbad8241d5b9` | soocas | 0.0611 | Esports / price=0.70-0.90 (n=43, roi=+0.11) | Esports / Esports / price=0.70-0.90 (n=43, roi=+0.11) | segment_only:t<2.0 |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.02 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x733b2ffa4ebfd125ee71e8b673bd08273abd7260` | tony1919 | 0.0401 | Esports (n=76, roi=+0.11) | Esports / Esports / pre (n=39, roi=+0.15) | Esports / Esports (n=71, roi=+0.11) | Esports / Esports / type=moneyline (n=57, roi=+0.10) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x2413e8801d3cad6fb21560fca2b5822684122442` | 2KairoStrike2 | 0.0579 | Crypto / price=0.50-0.70 (n=54, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown |
| `0x3740f38cb19308b573d4cf550d1865e0f6f9a935` | tiltedinv | -0.0155 | Sports / Hockey / price=0.70-0.90 (n=30, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x22957dbac6ca3a8dd78535546850efda6f778f0f` | BudMine | -0.0065 | Esports / price=0.50-0.70 (n=703, roi=+0.06) | Esports / Esports / price=0.50-0.70 (n=703, roi=+0.06) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0232 | Sports (n=90, roi=+0.07) | Sports / Soccer / Counter Strike (n=34, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0855 | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0149 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0026 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.0226 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0 |
| `0x4c03038d1056d87c198bbedb73634e5f9a52f8be` | jonesy91 | 0.0081 | Sports / American Football / NFL 2025 (n=81, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe8312a9a5ac2181317901e401e5b370b85d9a42a` | amused267 | 0.1435 | Sports / Basketball (n=71, roi=+0.38) | Sports / Basketball / NBA 2026 (n=71, roi=+0.38) | Sports / Basketball / type=moneyline (n=71, roi=+0.38) | Sports / Basketball / pre (n=67, roi=+0.39) | Sports / price=0.30-0.50 (n=58, roi=+0.39) | segment_only:t<2.0;segment_only:drawdown |
| `0xdfe23feed07253802f68688506218be25cc97e2b` | Slimshabi | 0.0283 | Sports / Soccer / pre (n=30, roi=+0.20) | segment_only:t<2.0 |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | 0.0133 | Sports / Soccer (n=38, roi=+0.24) | Sports / Soccer / pre (n=38, roi=+0.24) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0092 | Sports / Soccer / pre (n=167, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=145, roi=+0.09) | Sports / price=0.70-0.90 (n=174, roi=+0.07) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x335130d21de5bee3e4cf38dd4d6dc0df4da44e2d` | 0x335130d21de5BEe3e4cF38Dd4D6dc0DF4da44E2d-1762054911518 | 0.0465 | Sports / Basketball / price=0.50-0.70 (n=31, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0338 | Sports / American Football (n=156, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0126 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0068 | Esports / price=0.50-0.70 (n=112, roi=+0.11) | Esports / Esports / price=0.50-0.70 (n=112, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0584 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0296 | Esports / price=0.50-0.70 (n=45, roi=+0.21) | Esports / Esports / price=0.50-0.70 (n=45, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbbac81bb1c0e3ec89ea86f1067ecdbb93bc838d0` | josephsmithlds | 0.0171 | Sports / American Football / CFB 2026 (n=37, roi=+0.09) | Sports / American Football / live (n=31, roi=+0.09) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.024 | Esports / price=0.50-0.70 (n=44, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=44, roi=+0.18) | segment_only:t<2.0 |
| `0x0146df0b18f6faf92e814904edef6bf441694d51` | yndaa | 0.0514 | Sports / price=0.50-0.70 (n=47, roi=+0.17) | Sports / price=0.70-0.90 (n=30, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3cc501d94675f449c753be69232c162a987b5fcb` | Mikey22 | 0.0647 | Sports / American Football / pre (n=49, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x9cde12fb942486019ed19e505806715a8761b413` | jrf96 | Sports | 95 | 0.1577 | 0.1662 | 2.51 | 0.8 | 5.0 | 18.01 | 956857 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 724 | 0.1188 | 0.0559 | 3.45 | 0.721 | 8.0 | 2.81 | 396955 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 213 | 13.1189 | 12.1107 | 5.93 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8862 | 5.01 | 0.351 |
| `0x465ace6e…` | Sports / price=0.00-0.10 | 51 | 26.3798 | 20.151 | 5.11 | 0.569 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.105 | 4.18 | 0.329 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7088 | 4.03 | 0.362 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9628 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9628 | 3.45 | 0.324 |
| `0x465ace6e…` | Sports / Tennis | 134 | 7.999 | 7.5144 | 3.99 | 0.716 |
| `0x465ace6e…` | Sports | 313 | 4.9191 | 4.8799 | 4.94 | 0.716 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 821 | 2.955 | 2.9065 | 2.23 | 0.228 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 822 | 2.9508 | 2.9024 | 2.23 | 0.227 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2168 | 3.53 | 0.794 |
| `0x465ace6e…` | Sports / Tennis / WTA | 36 | 17.6494 | 12.8701 | 2.99 | 0.778 |
| `0x86c878cd…` | Sports / Tennis / live | 756 | 2.4966 | 2.4677 | 4.63 | 0.661 |
| `0x465ace6e…` | Sports / Tennis / live | 55 | 10.8553 | 9.0986 | 2.79 | 0.818 |
| `0x86c878cd…` | Sports | 2260 | 1.4179 | 1.4175 | 6.33 | 0.637 |
| `0x86c878cd…` | Sports / Tennis | 835 | 2.3247 | 2.3024 | 4.75 | 0.649 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 105 | 6.8439 | 5.807 | 2.77 | 0.124 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 105 | 6.8439 | 5.807 | 2.77 | 0.124 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 84 | 6.9336 | 5.8643 | 2.57 | 0.131 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7434 | 3.14 | 0.246 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3172 | 7.86 | 0.681 |
| `0xe9f5c75e…` | Sports / Basketball / live | 463 | 2.5051 | 2.436 | 4.18 | 0.62 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9822 | 8.06 | 0.75 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9835 | 2.51 | 0.519 |
| `0x465ace6e…` | Sports / Tennis / pre | 79 | 6.0105 | 5.6583 | 2.94 | 0.646 |
| `0x1941ca5d…` | Sports / Other sport | 2904 | 0.9306 | 0.9305 | 2.47 | 0.542 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2904 | 0.9306 | 0.9305 | 2.47 | 0.542 |
| `0x1941ca5d…` | Sports | 2906 | 0.9301 | 0.93 | 2.47 | 0.542 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.612 | 2.86 | 0.07 |
| `0x465ace6e…` | Sports / Tennis / ATP | 56 | 6.9698 | 6.2586 | 2.62 | 0.732 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 157 | 4.0258 | 3.6276 | 2.69 | 0.115 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1869 | 2.73 | 0.665 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9283 | 2.43 | 0.3 |
| `0xf5fe759c…` | Sports / Tennis / pre | 125 | 4.0799 | 3.8687 | 6.85 | 0.752 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5455 | 2.39 | 0.133 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7988 | 6.78 | 0.656 |
| `0xda0f4e3f…` | Sports / price=0.00-0.10 | 113 | 4.6241 | 4.0405 | 2.38 | 0.204 |
| `0xd60c6fa3…` | Sports | 3567 | 0.6924 | 0.6924 | 21.02 | 0.688 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 332 | 2.2888 | 2.2041 | 4.34 | 0.41 |
| `0xd970693a…` | Sports | 2423 | 0.7987 | 0.7987 | 10.32 | 0.665 |
| `0xf5fe759c…` | Sports / Tennis | 160 | 3.166 | 3.0974 | 6.47 | 0.675 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 386 | 2.0534 | 1.9737 | 3.42 | 0.288 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 538 | 1.6869 | 1.6564 | 3.62 | 0.586 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 390 | 2.0221 | 1.9447 | 3.41 | 0.285 |
| `0x4afbb658…` | Sports | 166 | 3.1455 | 2.9779 | 2.37 | 0.416 |
| `0xda0f4e3f…` | Sports / Soccer / price=0.00-0.10 | 91 | 4.7017 | 3.9885 | 2.18 | 0.22 |
| `0x86c878cd…` | Sports / Tennis / ATP | 398 | 1.9064 | 1.8809 | 3.1 | 0.631 |
| `0xe9f5c75e…` | Sports / Basketball | 974 | 1.2079 | 1.2004 | 4.19 | 0.563 |
| `0xd60c6fa3…` | Sports / price=0.10-0.30 | 894 | 1.2551 | 1.2428 | 16.29 | 0.597 |
| `0xf5fe759c…` | Sports | 210 | 2.5652 | 2.5638 | 6.56 | 0.667 |
| `0x1985327e…` | Sports | 1315 | 1.022 | 1.022 | 2.67 | 0.719 |
| `0xb569eb4f…` | Esports | 3473 | 0.6185 | 0.6182 | 2.06 | 0.916 |
| `0xb569eb4f…` | Esports / Esports | 3473 | 0.6185 | 0.6182 | 2.06 | 0.916 |
| `0xb569eb4f…` | Esports / Esports / live | 3309 | 0.6333 | 0.6329 | 2.01 | 0.926 |
| `0x1985327e…` | Sports / Soccer / live | 855 | 1.2262 | 1.2215 | 2.09 | 0.705 |
| `0x1985327e…` | Sports / Soccer | 865 | 1.212 | 1.2077 | 2.09 | 0.704 |
| `0xf5fe759c…` | Sports / Tennis / ATP | 91 | 3.8374 | 3.6051 | 6.47 | 0.758 |
| `0xe9f5c75e…` | Sports | 1689 | 0.8355 | 0.8355 | 4.67 | 0.583 |
| `0xd60c6fa3…` | Sports / Soccer | 2414 | 0.695 | 0.695 | 16.7 | 0.688 |
