# Отчёт воронки, 2026-09-29 06:08 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 8646 |
| 0. Из них не только 5-мин крипта | 7312 |
| 1. Прошли дешёвые отсечки | 863 из 7312 |
| 2. Прошли по полной истории | 3 + сегментом 20 из 863 |
| 3. Прошли реалистичный вход | 5 из 23 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 3712 |
| entries>=0.90 | 2012 |
| history<90d | 1985 |
| open_now>10 | 1562 |
| closed<50 | 1512 |
| top1_concentration | 1483 |
| short_crypto | 573 |
| profit_from<0.10 | 427 |
| positions>5000 | 80 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 727 |
| drawdown | 725 |
| concurrency_p95>8 | 713 |
| unstable_halves | 558 |
| roi_copy<=0 | 348 |
| low_liquidity | 193 |
| both_sides | 171 |
| history<90d | 130 |
| hold<1h | 45 |
| entries>=0.90 | 39 |
| segment_only:t<2.0 | 19 |
| segment_only:drawdown | 18 |
| top1_concentration | 17 |
| short_crypto | 17 |
| closed<50 | 16 |
| sniping | 15 |
| segment_only:unstable_halves | 13 |
| profit_from<0.10 | 6 |
| segment_only:roi_copy<=0 | 6 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 17 |
| edge_decays_with_delay | 1 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x508d9f65761f8f4369d41e50feb9abbb57f5a6f9` | ArbJohn | Sports | 0.4139 | 2.64 | 0.3832 | 0.4006 | 0.3384 | 7.0 | 10.56 | н/д | Sports (n=50, roi=+0.41) | Sports / Baseball (n=46, roi=+0.40) | Sports / Baseball / MLB (n=46, roi=+0.40) | Sports / Baseball / type=moneyline (n=46, roi=+0.40) | Sports / price=0.30-0.50 (n=46, roi=+0.40) | Sports / Baseball / price=0.30-0.50 (n=46, roi=+0.40) |
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | Esports | 0.1615 | 1.87 | 0.0946 | 0.0887 | 0.1775 | 3.0 | 2.29 | н/д | Esports / Esports / live (n=99, roi=+0.28) | Esports / Esports / Counter Strike (n=90, roi=+0.27) | Esports (n=112, roi=+0.24) | Esports / Esports (n=112, roi=+0.24) | Esports / price=0.30-0.50 (n=44, roi=+0.35) | Esports / Esports / price=0.30-0.50 (n=44, roi=+0.35) |
| `0xcb7ff0ad390ca732ff9d54f5f6da58888046824b` | silentvector10 | Sports | 0.1035 | 1.27 | 0.0516 | 0.0676 | 0.1258 | 6.0 | 4.66 | н/д | Sports / price=0.50-0.70 (n=71, roi=+0.17) | Sports / American Football / type=moneyline (n=31, roi=+0.25) |
| `0x13ce0f6f73a83a2be1eb484c91169c2bd5b935f0` | mozak | Sports | -0.0295 | -1.04 | 0.0683 | 0.0704 | 0.0419 | 8.0 | 6.85 | н/д | Sports / Tennis / price=0.70-0.90 (n=31, roi=+0.09) |
| `0x776713e6791578ffa93fb6cc81da941dd4334fb2` | 0x776713E6791578FFA93Fb6cc81da941dD4334fB2-1769702052456 | Esports | 0.0522 | 1.05 | 0.0557 | 0.0702 | 0.0985 | 5.0 | 3.25 | н/д | Esports / Esports / type=moneyline (n=76, roi=+0.26) | Esports (n=184, roi=+0.15) | Esports / Esports (n=184, roi=+0.15) | Esports / Esports / live (n=171, roi=+0.15) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xa64b1bc8f8fd581f9609b7fbe55c96f2ab9fe453` | 101dalmatians | 0.1615 | Esports / Esports / live (n=99, roi=+0.28) | Esports / Esports / Counter Strike (n=90, roi=+0.27) | Esports (n=112, roi=+0.24) | Esports / Esports (n=112, roi=+0.24) | Esports / price=0.30-0.50 (n=44, roi=+0.35) | Esports / Esports / price=0.30-0.50 (n=44, roi=+0.35) | segment_only:t<2.0 |
| `0xa80cdd95c7d68e38e5b9e8a5ff6a8b65afa75a6d` | chasing500k | 0.1564 | Esports / Esports / pre (n=32, roi=+0.29) | segment_only:unstable_halves |
| `0xcdfb7564a5731d30713c91943ae395d5f815980c` | ImSmart | -0.0697 | Sports / Basketball / price=0.50-0.70 (n=37, roi=+0.15) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.0572 | Sports / price=0.70-0.90 (n=72, roi=+0.08) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcb7ff0ad390ca732ff9d54f5f6da58888046824b` | silentvector10 | 0.1035 | Sports / price=0.50-0.70 (n=71, roi=+0.17) | Sports / American Football / type=moneyline (n=31, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown |
| `0x13ce0f6f73a83a2be1eb484c91169c2bd5b935f0` | mozak | -0.0295 | Sports / Tennis / price=0.70-0.90 (n=31, roi=+0.09) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x12ec6d71325afac2b4d25b3de94185e2c48d41ae` | olegio | -0.0153 | Sports / Hockey / live (n=30, roi=+0.21) | Sports / Hockey / NHL 2026 (n=33, roi=+0.17) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd13e1585ab393467fe2351e6a9b4801f5b19f2d6` | Elia12 | -0.0179 | Sports / Other sport / Japan J League (n=31, roi=+0.03) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x776713e6791578ffa93fb6cc81da941dd4334fb2` | 0x776713E6791578FFA93Fb6cc81da941dD4334fB2-1769702052456 | 0.0522 | Esports / Esports / type=moneyline (n=76, roi=+0.26) | Esports (n=184, roi=+0.15) | Esports / Esports (n=184, roi=+0.15) | Esports / Esports / live (n=171, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xe906e2dea1be382fb877884e16083c460b3fdb88` | maplestory079 | -0.0021 | Sports / Soccer / price=0.70-0.90 (n=137, roi=+0.09) | Sports / price=0.70-0.90 (n=166, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd1e0c0db26fb636fb557704f05f7cd8ae4148913` | DjPonyboots | 0.0198 | Sports / Basketball / price=0.50-0.70 (n=43, roi=+0.19) | Sports / Basketball / NBA 2026 (n=62, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |
| `0xfb1226909799baad50e0eb61226c84c5b0f06a81` | starryxd | 0.035 | Sports (n=31, roi=+0.24) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xf3b1c96cc1e7f4fa6a4a916dae26535eff24979a` | GenoMachino | 0.0318 | Sports / price=0.30-0.50 (n=79, roi=+0.22) | Sports / Basketball / type=moneyline (n=32, roi=+0.20) | Sports / Basketball (n=35, roi=+0.16) | Sports / Basketball / live (n=30, roi=+0.16) | segment_only:t<2.0;segment_only:drawdown |
| `0x3a4f2d28f884a5d7bfab73956792bc1c931ac4f2` | arunannaveni | 0.0024 | Sports / Soccer / price=0.30-0.50 (n=45, roi=+0.45) | Sports / Soccer / live (n=74, roi=+0.29) | Sports / Soccer (n=123, roi=+0.18) | Sports / Soccer / type=binary (n=85, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x0dbe4798a1719b1fc08cd3acc2369dd77c069013` | brussssss | 0.0031 | Sports / price=0.50-0.70 (n=181, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0081 | Esports / price=0.50-0.70 (n=106, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=106, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0342 | Sports / American Football (n=148, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0734 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x670d76669e567a24a9876f92310436d029020825` | ebglyss | 0.0382 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.25) | Sports / price=0.50-0.70 (n=54, roi=+0.18) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x7e3a1f95c558f39a51ff334d789e3e039b553246` | KaneAnalytics | 0.1062 | Sports / Basketball / live (n=367, roi=+0.15) | segment_only:t<2.0;segment_only:drawdown |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0x508d9f65761f8f4369d41e50feb9abbb57f5a6f9` | ArbJohn | Sports | 51 | 0.4139 | 0.3985 | 2.64 | 0.627 | 7.0 | 10.56 | 413558 | прошёл |
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 898 | 0.3304 | 0.2446 | 9.99 | 0.744 | 8.0 | 1.07 | 33916 | delayed_roi<=0 |
| `0x12ed45d2b45259d27a7fb593e564cd269c4fc9b4` | sazzaa | Sports | 529 | 0.1868 | 0.0964 | 5.38 | 0.529 | 5.0 | 6.07 | 355295 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x4f87cf20…` | Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8644 | 2.77 | 0.125 |
| `0x4f87cf20…` | Esports / Esports / price=0.00-0.10 | 104 | 6.9193 | 5.8644 | 2.77 | 0.125 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.4011 | 2.85 | 0.269 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 65 | 7.8118 | 6.1162 | 2.73 | 0.215 |
| `0xef185339…` | Sports | 3799 | 0.7313 | 0.7313 | 22.6 | 0.695 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9295 | 2.43 | 0.3 |
| `0xef185339…` | Sports / price=0.10-0.30 | 1032 | 1.198 | 1.1891 | 16.91 | 0.596 |
| `0xef185339…` | Sports / Soccer | 2567 | 0.7043 | 0.7045 | 18.77 | 0.693 |
| `0xef185339…` | Sports / Soccer / live | 2533 | 0.7046 | 0.7048 | 18.57 | 0.691 |
| `0x09b045ba…` | Sports | 1601 | 0.8006 | 0.8005 | 9.66 | 0.717 |
| `0xef185339…` | Sports / Soccer / price=0.10-0.30 | 673 | 1.2226 | 1.2084 | 13.89 | 0.606 |
| `0xbfeceb41…` | Sports / price=0.00-0.10 | 378 | 1.6188 | 1.5613 | 2.34 | 0.077 |
| `0x76697d10…` | Sports / Basketball / NCAA CBB | 265 | 1.9003 | 1.8094 | 2.81 | 0.664 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 118 | 2.9929 | 2.675 | 2.95 | 0.398 |
| `0xef185339…` | Sports / price=0.00-0.10 | 231 | 1.9473 | 1.8504 | 5.24 | 0.485 |
| `0xef185339…` | Sports / Other sport / live | 1225 | 0.7824 | 0.7816 | 12.59 | 0.697 |
| `0xef185339…` | Sports / Other sport | 1226 | 0.781 | 0.7802 | 12.58 | 0.697 |
| `0xd84d970b…` | Sports / Soccer / price=0.00-0.10 | 31 | 7.3833 | 4.7378 | 2.27 | 0.419 |
| `0x76b8356b…` | Culture / price=0.00-0.10 | 286 | 1.6299 | 1.5575 | 2.01 | 0.325 |
| `0x0df758f3…` | Sports / price=0.00-0.10 | 183 | 2.141 | 1.946 | 2.4 | 0.126 |
| `0x41558102…` | Sports / price=0.10-0.30 | 327 | 1.5188 | 1.4499 | 11.69 | 0.599 |
| `0x09b045ba…` | Sports / price=0.10-0.30 | 386 | 1.3179 | 1.2923 | 11.42 | 0.596 |
| `0x41558102…` | Sports | 6001 | 0.3242 | 0.3242 | 10.27 | 0.851 |
| `0x09b045ba…` | Sports / Soccer / live | 1014 | 0.7822 | 0.7826 | 6.69 | 0.711 |
| `0x09b045ba…` | Sports / Soccer | 1020 | 0.7767 | 0.7771 | 6.68 | 0.711 |
| `0x76697d10…` | Sports / Basketball / live | 948 | 0.8039 | 0.7998 | 3.84 | 0.578 |
| `0x76697d10…` | Sports / Basketball | 949 | 0.802 | 0.7979 | 3.84 | 0.577 |
| `0x76697d10…` | Sports / Basketball / type=totals | 627 | 0.9826 | 0.971 | 3.19 | 0.558 |
| `0xef185339…` | Sports / Soccer / type=moneyline | 518 | 1.0163 | 1.0057 | 9.69 | 0.739 |
| `0x76697d10…` | Sports | 1387 | 0.6067 | 0.6067 | 4.2 | 0.606 |
| `0x4f87cf20…` | Esports / Esports / type=map_handicap | 556 | 0.9739 | 0.9532 | 2.45 | 0.734 |
| `0x09b045ba…` | Sports / Soccer / price=0.00-0.10 | 68 | 3.2871 | 2.7217 | 2.03 | 0.353 |
| `0xef185339…` | Sports / price=0.30-0.50 | 1293 | 0.5901 | 0.5923 | 21.57 | 0.711 |
| `0x037305f4…` | Other | 241 | 1.4605 | 1.3645 | 15.86 | 0.846 |
| `0x037305f4…` | Other / ? | 241 | 1.4605 | 1.3645 | 15.86 | 0.846 |
| `0x037305f4…` | Other / ? / ? | 241 | 1.4605 | 1.3645 | 15.86 | 0.846 |
| `0x037305f4…` | Other / ? / type=binary | 241 | 1.4605 | 1.3645 | 15.86 | 0.846 |
| `0xbfeceb41…` | Sports | 1345 | 0.5759 | 0.5744 | 2.91 | 0.407 |
| `0xef185339…` | Sports / Other sport / price=0.10-0.30 | 357 | 1.1326 | 1.1113 | 9.5 | 0.574 |
| `0x09b045ba…` | Sports / Other sport / live | 568 | 0.8592 | 0.8571 | 8.23 | 0.734 |
| `0x09b045ba…` | Sports / Other sport | 578 | 0.8426 | 0.8412 | 8.2 | 0.727 |
| `0xef185339…` | Sports / Soccer / price=0.00-0.10 | 159 | 1.6992 | 1.591 | 4.17 | 0.478 |
| `0xa991049a…` | Sports / price=0.10-0.30 | 240 | 1.3713 | 1.2834 | 10.81 | 0.637 |
| `0x41558102…` | Sports / Other sport / live | 1818 | 0.4666 | 0.465 | 5.69 | 0.843 |
| `0x41558102…` | Sports / Other sport | 1827 | 0.4649 | 0.4634 | 5.7 | 0.843 |
| `0xef185339…` | Sports / Other sport / type=moneyline | 323 | 1.0931 | 1.072 | 9.06 | 0.774 |
| `0x09b045ba…` | Sports / Soccer / price=0.10-0.30 | 246 | 1.2524 | 1.2183 | 8.64 | 0.573 |
| `0xd84d970b…` | Sports / Soccer | 178 | 1.5099 | 1.4218 | 2.51 | 0.517 |
| `0xef185339…` | Sports / Soccer / type=totals | 1650 | 0.4631 | 0.4663 | 12.95 | 0.667 |
| `0xa42f3648…` | Sports | 971 | 0.5994 | 0.5994 | 10.19 | 0.68 |
| `0x09b045ba…` | Sports / Other sport / type=moneyline | 420 | 0.8985 | 0.894 | 6.91 | 0.731 |
| `0x76b8356b…` | Culture | 928 | 0.6007 | 0.5991 | 2.38 | 0.555 |
| `0xef185339…` | Sports / Other sport / price=0.00-0.10 | 72 | 2.4952 | 2.1116 | 3.19 | 0.5 |
| `0x41558102…` | Sports / Other sport / price=0.10-0.30 | 137 | 1.7037 | 1.5279 | 8.53 | 0.642 |
| `0x4f87cf20…` | Esports / Esports | 2076 | 0.3917 | 0.3916 | 3.01 | 0.688 |
| `0x4f87cf20…` | Esports | 2077 | 0.391 | 0.3909 | 3.01 | 0.688 |
| `0x4f87cf20…` | Esports / Esports / live | 2067 | 0.3917 | 0.3916 | 3.0 | 0.688 |
| `0x41558102…` | Sports / Soccer / price=0.10-0.30 | 190 | 1.3854 | 1.2843 | 8.11 | 0.568 |
| `0xef185339…` | Sports / Soccer / price=0.30-0.50 | 874 | 0.5876 | 0.5908 | 17.76 | 0.708 |
| `0x501c9ecc…` | Sports / price=0.00-0.10 | 352 | 0.9657 | 0.9265 | 2.91 | 0.256 |
