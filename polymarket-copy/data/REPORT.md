# Отчёт воронки, 2026-10-08 07:22 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 54106 |
| 0. Из них не только 5-мин крипта | 51766 |
| 1. Прошли дешёвые отсечки | 4256 из 33377 |
| 2. Прошли по полной истории | 2 + сегментом 49 из 4256 |
| 3. Прошли реалистичный вход | 7 из 51 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 17295 |
| closed<50 | 15732 |
| top1_concentration | 14173 |
| entries>=0.90 | 7531 |
| history<90d | 5837 |
| open_now>10 | 4016 |
| profit_from<0.10 | 2556 |
| short_crypto | 2278 |
| positions>5000 | 163 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 3820 |
| concurrency_p95>8 | 3383 |
| drawdown | 3233 |
| unstable_halves | 2813 |
| roi_copy<=0 | 1697 |
| silent | 787 |
| low_liquidity | 648 |
| both_sides | 626 |
| history<90d | 362 |
| top1_concentration | 334 |
| closed<50 | 260 |
| hold<1h | 161 |
| entries>=0.90 | 150 |
| short_crypto | 88 |
| profit_from<0.10 | 60 |
| sniping | 49 |
| segment_only:t<2.0 | 45 |
| segment_only:drawdown | 38 |
| segment_only:unstable_halves | 23 |
| segment_only:roi_copy<=0 | 10 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 39 |
| edge_decays_with_delay | 5 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe504ebaecb472a5860ea78b2171c1d19c0182f29` | AchanM | Esports | 0.2229 | 1.94 | 0.1532 | 0.1195 | 0.2662 | 5.0 | 4.24 | н/д | Esports / Esports / type=moneyline (n=57, roi=+0.27) | Esports (n=60, roi=+0.25) | Esports / Esports (n=60, roi=+0.25) | Esports / Esports / Counter Strike (n=60, roi=+0.25) |
| `0xd6f293e47e7d2745964e41bd7a3c7ff4676d1183` | YoungButOld | Esports | 1.6142 | 1.37 | 0.1791 | 0.0891 | 1.5914 | 5.0 | 5.5 | 0.0 | Esports / Esports / type=moneyline (n=40, roi=+1.02) |
| `0x0f1879b51ce62999d9685111c2505ff2fe7bae1f` |  | Esports | 0.0498 | 1.35 | 0.02 | 0.0314 | -0.0002 | 7.0 | 4.83 | 0.0 | Esports / Esports / Dota 2 (n=96, roi=+0.17) | Esports / Esports / live (n=154, roi=+0.11) | Esports / Esports / type=child_moneyline (n=95, roi=+0.12) |
| `0x837afd52d07051e143624c4dc876cbc8517c6c27` | remader | Esports | 0.0391 | 1.19 | 0.0358 | 0.0366 | 0.0353 | 3.0 | 2.63 | н/д | Esports / Esports / live (n=101, roi=+0.08) | Esports (n=115, roi=+0.07) | Esports / Esports (n=115, roi=+0.07) | Esports / Esports / Valorant (n=43, roi=+0.10) | Esports / Esports / type=child_moneyline (n=72, roi=+0.08) |
| `0x9a0382d40710ad33818307a4c9213bc424b786dc` | touxie | Politics | 0.0196 | 0.54 | 0.0236 | 0.0272 | -0.022 | 4.0 | 13.96 | н/д | Politics / price=0.70-0.90 (n=40, roi=+0.06) | Politics / Tweet Markets / price=0.70-0.90 (n=40, roi=+0.06) |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | Sports | 0.0115 | 0.89 | 0.0434 | 0.0749 | 0.0943 | 8.0 | 2.66 | 0.0 | Sports / Other sport / price=0.70-0.90 (n=80, roi=+0.08) | Sports / Other sport (n=128, roi=+0.06) | Sports / Other sport / type=totals (n=37, roi=+0.10) |
| `0x631d2473d077f0b9d17434564e9b3418c5ca02ff` | R2Eagle | Sports | 0.0266 | 0.59 | 0.0235 | 0.028 | 0.0456 | 8.0 | 55.67 | н/д | Sports / price=0.70-0.90 (n=31, roi=+0.10) | Sports / Soccer / price=0.70-0.90 (n=30, roi=+0.09) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xe504ebaecb472a5860ea78b2171c1d19c0182f29` | AchanM | 0.2229 | Esports / Esports / type=moneyline (n=57, roi=+0.27) | Esports (n=60, roi=+0.25) | Esports / Esports (n=60, roi=+0.25) | Esports / Esports / Counter Strike (n=60, roi=+0.25) | segment_only:t<2.0 |
| `0xd6f293e47e7d2745964e41bd7a3c7ff4676d1183` | YoungButOld | 1.6142 | Esports / Esports / type=moneyline (n=40, roi=+1.02) | segment_only:t<2.0 |
| `0x4dd25d80bec83bc40b6406acc5af78fc26099014` | skytrader123 | -0.0615 | Sports / Soccer / price=0.50-0.70 (n=62, roi=+0.12) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0609 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.16) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5374430a0e5a775af0480e5d1f9a434f31a0f7c` | JohnWhipples | -0.0555 | Sports / price=0.70-0.90 (n=33, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xadafdd00c50d98005b55b40355ffe43b7a47aefd` | pulse | -0.0402 | Sports / price=0.50-0.70 (n=99, roi=+0.16) | Sports / Tennis / price=0.50-0.70 (n=74, roi=+0.13) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0f1879b51ce62999d9685111c2505ff2fe7bae1f` |  | 0.0498 | Esports / Esports / Dota 2 (n=96, roi=+0.17) | Esports / Esports / live (n=154, roi=+0.11) | Esports / Esports / type=child_moneyline (n=95, roi=+0.12) | segment_only:t<2.0 |
| `0x6eacd4f7089d7c43a39153958192c4f8b02aed37` | ludka-minutka | 0.1714 | Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / price=0.10-0.30 (n=103, roi=+0.56) | Esports / Esports / type=child_moneyline (n=569, roi=+0.19) | Esports (n=661, roi=+0.17) | Esports / Esports (n=661, roi=+0.17) | Esports / Esports / Dota 2 (n=661, roi=+0.17) | segment_only:drawdown |
| `0x837afd52d07051e143624c4dc876cbc8517c6c27` | remader | 0.0391 | Esports / Esports / live (n=101, roi=+0.08) | Esports (n=115, roi=+0.07) | Esports / Esports (n=115, roi=+0.07) | Esports / Esports / Valorant (n=43, roi=+0.10) | Esports / Esports / type=child_moneyline (n=72, roi=+0.08) | segment_only:t<2.0 |
| `0x78fea75923d359a702e14c4fb9c4aff09f34df2f` | 0x78fea75923d359a702e14c4fb9c4aff09f34df2f | 0.0765 | Sports / price=0.50-0.70 (n=123, roi=+0.13) | segment_only:t<2.0 |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.0988 | Sports / Soccer / price=0.50-0.70 (n=91, roi=+0.26) | Sports / Soccer / type=moneyline (n=47, roi=+0.27) | Sports / Soccer / pre (n=97, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x807fcf8fbad55fb5121941ad7f37497e7db59615` |  | -0.0307 | Sports / Baseball / type=moneyline (n=41, roi=+0.24) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x9a0382d40710ad33818307a4c9213bc424b786dc` | touxie | 0.0196 | Politics / price=0.70-0.90 (n=40, roi=+0.06) | Politics / Tweet Markets / price=0.70-0.90 (n=40, roi=+0.06) | segment_only:t<2.0 |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | 0.0115 | Sports / Other sport / price=0.70-0.90 (n=80, roi=+0.08) | Sports / Other sport (n=128, roi=+0.06) | Sports / Other sport / type=totals (n=37, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa538af775227c7add77418ba079ea3ae6a9212c3` | WinsonEnterpriseCorp | -0.0291 | Sports (n=59, roi=+0.17) | Sports / price=0.50-0.70 (n=35, roi=+0.21) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbdd4059cb05cefceedff0a2d0b1f5834d33b9bcd` | 0xBDD4059Cb05CeFCeEdfF0A2D0B1F5834d33B9bcD-1777385662620 | -0.0252 | Sports (n=89, roi=+0.07) | Sports / Soccer / Counter Strike (n=33, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x631d2473d077f0b9d17434564e9b3418c5ca02ff` | R2Eagle | 0.0266 | Sports / price=0.70-0.90 (n=31, roi=+0.10) | Sports / Soccer / price=0.70-0.90 (n=30, roi=+0.09) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xfd80d58f9346659dd69a7b9d8d82aa705dd2393a` | Allen59 | -0.0151 | Crypto / Bitcoin / Bitcoin Neg Risk 4H (n=37, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0098 | Sports / Soccer / price=0.50-0.70 (n=53, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x453b09c371945b5c78adf6b37d34c5ce8eb0db4a` | fgdxsg | 0.0822 | Sports / Basketball / price=0.30-0.50 (n=32, roi=+0.33) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x660a4e3a52f4a7b116f88c5d02ce8a6b67733d22` | teeqkay | 0.1066 | Esports (n=72, roi=+0.27) | Esports / Esports (n=71, roi=+0.27) | Esports / Esports / type=moneyline (n=60, roi=+0.29) | Esports / Esports / pre (n=36, roi=+0.35) | segment_only:t<2.0 |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0032 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=138, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0x11fd479aa7861ebb2a4b5f9da2714ea21c210338` | kaydenlll | 0.0226 | Sports / Baseball / live (n=32, roi=+0.07) | segment_only:t<2.0 |
| `0xf3d3c029eea604047526d5615cf19795eb6e77a0` | llicius | -0.0012 | Sports / Other sport (n=43, roi=+0.11) | Sports / Other sport / type=moneyline (n=43, roi=+0.11) | Sports / Other sport / live (n=43, roi=+0.11) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | 0.0091 | Sports / Soccer / pre (n=166, roi=+0.09) | Sports / Soccer / price=0.70-0.90 (n=143, roi=+0.09) | Sports / price=0.70-0.90 (n=172, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0339 | Sports / American Football (n=154, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0x9534cf9c9692bfe14a75f468ad37962b1aec1fe8` | ThreeAxes | 0.0116 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6bd6057e8975af754da2365652d8e54309afbf96` | Gouqige | 0.0108 | Sports / Baseball / type=totals (n=35, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0084 | Esports / price=0.50-0.70 (n=111, roi=+0.10) | Esports / Esports / price=0.50-0.70 (n=111, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown |
| `0xd385bb420ad51200505d73526f16d20fd51234fb` | legalm0ney | 0.0348 | Esports / price=0.50-0.70 (n=44, roi=+0.23) | Esports / Esports / price=0.50-0.70 (n=44, roi=+0.23) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbae185ff7f75aca3abca60825944db511c05d8ab` | 0xbae185Ff7F75aca3abca60825944Db511c05D8AB-1768668883859 | 0.0789 | Sports / Soccer / FIFA World Cup (n=142, roi=+0.20) | Sports / Soccer / pre (n=296, roi=+0.13) | Sports / Soccer (n=339, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0xf184bff6a9217f1a76dcba7c0c4888351ebbc2d7` | drunkdegenerate | 0.0278 | Esports / price=0.50-0.70 (n=43, roi=+0.18) | Esports / Esports / price=0.50-0.70 (n=43, roi=+0.18) | segment_only:t<2.0 |
| `0xbcf51140fd48e69c6e6d4bd09d38a629059856a1` | bqy0301 | 0.1998 | Sports / price=0.30-0.50 (n=36, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown |
| `0xb569786bcb19be651f97d420dd956c5f27f56fe0` | SemperFi2k | 0.049 | Esports / Esports / type=child_moneyline (n=94, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0492 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x751be7122f148fba5aa2021ace98edc2001873fd` | aqzfssqkqzbcbr1994 | 0.0667 | Esports / Esports / League of Legends (n=157, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0facd3e5ced4b5dd53965d3e0508202b4833b89a` | artsonx | 0.0639 | Sports / Basketball / pre (n=40, roi=+0.27) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0468 | Sports / Basketball / NBA 2026 (n=37, roi=+0.48) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xeef382e6c8cb7adde63551043659b381b1c00547` | xiaomikang | 0.048 | Esports / price=0.10-0.30 (n=41, roi=+0.47) | Esports / Esports / price=0.10-0.30 (n=41, roi=+0.47) | Esports / Esports / type=child_moneyline (n=216, roi=+0.19) | Esports (n=298, roi=+0.16) | Esports / Esports (n=298, roi=+0.16) | Esports / Esports / League of Legends (n=296, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x173e8a681812cee182c8cc8041f8027b647f9ff4` | 0x50f161F7CD7aE6A7Df8E6E9a7A475EFa20f3e3b1-1757699966720 | 0.0673 | Esports / Esports / type=moneyline (n=121, roi=+0.28) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 521 | 0.185 | 0.0928 | 5.27 | 0.53 | 5.0 | 5.96 | 350156 | delayed_roi<=0 |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 714 | 0.1248 | 0.0622 | 3.6 | 0.725 | 8.0 | 2.83 | 395859 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0xe8ca3f75…` | Sports / price=0.00-0.10 | 249 | 19.5062 | 18.3016 | 4.47 | 0.506 |
| `0xe8ca3f75…` | Sports / Tennis / price=0.00-0.10 | 93 | 22.361 | 18.988 | 5.97 | 0.516 |
| `0xe8ca3f75…` | Sports | 1492 | 3.6808 | 3.6758 | 4.9 | 0.709 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 97 | 15.2607 | 13.1717 | 4.13 | 0.186 |
| `0xe8ca3f75…` | Sports / Tennis / live | 120 | 12.5374 | 11.2182 | 4.38 | 0.55 |
| `0xe8ca3f75…` | Sports / Tennis / type=tennis_match_totals | 91 | 14.7377 | 12.6775 | 4.16 | 0.626 |
| `0xe8ca3f75…` | Sports / Tennis | 549 | 4.2424 | 4.2094 | 5.86 | 0.718 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3962 | 3.78 | 0.177 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 130 | 9.5186 | 8.3962 | 3.78 | 0.177 |
| `0x5a05e30e…` | Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9628 | 3.45 | 0.324 |
| `0x5a05e30e…` | Esports / Esports / price=0.00-0.10 | 34 | 25.2548 | 15.9628 | 3.45 | 0.324 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 820 | 2.9584 | 2.9097 | 2.23 | 0.227 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 821 | 2.9541 | 2.9057 | 2.23 | 0.227 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 244 | 5.617 | 5.2749 | 3.99 | 0.139 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.483 | 3.61 | 0.17 |
| `0xe8ca3f75…` | Esports / price=0.00-0.10 | 62 | 11.4868 | 9.4908 | 3.47 | 0.468 |
| `0xe8ca3f75…` | Esports / Esports / price=0.00-0.10 | 62 | 11.4868 | 9.4908 | 3.47 | 0.468 |
| `0xeda67a7f…` | Sports | 465 | 3.422 | 3.4063 | 4.17 | 0.546 |
| `0xe8ca3f75…` | Sports / Tennis / WTA | 126 | 6.8616 | 6.3742 | 3.33 | 0.754 |
| `0xe8ca3f75…` | Sports / Tennis / ATP | 251 | 4.3947 | 4.3142 | 3.99 | 0.729 |
| `0x2690fe45…` | Sports / price=0.00-0.10 | 55 | 9.8933 | 8.1623 | 2.51 | 0.182 |
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8623 | 2.77 | 0.125 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8623 | 2.77 | 0.125 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.6159 | 2.28 | 0.167 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6263 | 2.81 | 0.636 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.3924 | 2.85 | 0.269 |
| `0x2e7c5460…` | Sports / price=0.00-0.10 | 61 | 8.8246 | 6.7443 | 3.14 | 0.246 |
| `0xf5fe759c…` | Sports / price=0.00-0.10 | 69 | 7.4096 | 6.3172 | 7.86 | 0.681 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 31 | 13.5161 | 9.4078 | 2.17 | 0.161 |
| `0xf5fe759c…` | Sports / Tennis / price=0.00-0.10 | 56 | 8.5658 | 6.9822 | 8.06 | 0.75 |
| `0x98689f59…` | Sports / Tennis / type=tennis_first_set_totals | 52 | 9.4766 | 6.9846 | 2.51 | 0.519 |
| `0x1941ca5d…` | Sports / Other sport | 2890 | 0.9335 | 0.9334 | 2.47 | 0.539 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2890 | 0.9335 | 0.9334 | 2.47 | 0.539 |
| `0x1941ca5d…` | Sports | 2892 | 0.9329 | 0.9328 | 2.47 | 0.539 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.9455 | 2.72 | 0.209 |
| `0x245e8692…` | Crypto / price=0.00-0.10 | 330 | 2.7543 | 2.612 | 2.86 | 0.07 |
| `0xe8ca3f75…` | Esports / Esports / live | 147 | 3.9375 | 3.8615 | 2.8 | 0.571 |
| `0x98689f59…` | Sports / price=0.00-0.10 | 156 | 4.0581 | 3.6543 | 2.7 | 0.115 |
| `0xe8ca3f75…` | Esports | 454 | 2.0627 | 2.1151 | 4.24 | 0.656 |
| `0xe8ca3f75…` | Esports / Esports | 454 | 2.0627 | 2.1151 | 4.24 | 0.656 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9286 | 2.43 | 0.3 |
| `0xf5fe759c…` | Sports / Tennis / pre | 125 | 4.0799 | 3.8687 | 6.85 | 0.752 |
| `0x98689f59…` | Sports / Tennis / price=0.00-0.10 | 90 | 5.4442 | 4.5462 | 2.39 | 0.133 |
| `0xf5fe759c…` | Sports / Tennis / type=moneyline | 128 | 3.9942 | 3.7988 | 6.78 | 0.656 |
| `0xe8ca3f75…` | Sports / American Football / price=0.00-0.10 | 30 | 10.8416 | 7.8263 | 5.01 | 0.567 |
| `0xe8ca3f75…` | Sports / American Football / CFB 2026 | 39 | 8.5701 | 6.7848 | 4.77 | 0.564 |
| `0xe8ca3f75…` | Sports / American Football / pre | 43 | 7.924 | 6.4571 | 4.77 | 0.558 |
| `0xb209ec04…` | Sports | 1547 | 1.0644 | 1.0649 | 4.64 | 0.518 |
| `0x2690fe45…` | Sports | 187 | 2.9902 | 3.03 | 2.49 | 0.471 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1755 | 2.41 | 0.526 |
| `0xe8ca3f75…` | Sports / Tennis / pre | 429 | 1.9221 | 1.9836 | 4.76 | 0.765 |
| `0xb209ec04…` | Sports / Soccer | 888 | 1.3829 | 1.3767 | 4.01 | 0.511 |
| `0xe8ca3f75…` | Sports / American Football | 50 | 6.7917 | 5.795 | 4.59 | 0.54 |
| `0xb209ec04…` | Esports / Esports / live | 958 | 1.3225 | 1.318 | 3.76 | 0.506 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.6285 | 3.4 | 0.478 |
| `0xb209ec04…` | Esports | 1213 | 1.1502 | 1.1494 | 4.05 | 0.5 |
| `0xb209ec04…` | Esports / Esports | 1213 | 1.1502 | 1.1494 | 4.05 | 0.5 |
| `0xf5fe759c…` | Sports / Tennis | 160 | 3.166 | 3.0974 | 6.47 | 0.675 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 382 | 2.0783 | 1.9963 | 3.43 | 0.288 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 389 | 2.0515 | 1.9722 | 3.44 | 0.285 |
