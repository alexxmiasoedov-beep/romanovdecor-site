# Отчёт воронки, 2026-10-05 06:34 UTC

## Воронка

| Стадия | Кошельков |
|---|---|
| 0. Торговали сегодня | 17903 |
| 0. Из них не только 5-мин крипта | 15990 |
| 1. Прошли дешёвые отсечки | 1991 из 15990 |
| 2. Прошли по полной истории | 4 + сегментом 42 из 1991 |
| 3. Прошли реалистичный вход | 15 из 46 |

## Причины отсева, стадия 1

| Причина | Кошельков |
|---|---|
| roi<=0 | 8538 |
| history<90d | 4365 |
| closed<50 | 4115 |
| top1_concentration | 3590 |
| open_now>10 | 3127 |
| entries>=0.90 | 2475 |
| short_crypto | 1494 |
| profit_from<0.10 | 1049 |
| positions>5000 | 126 |

## Причины отсева, стадия 2

| Причина | Кошельков |
|---|---|
| t<2.0 | 1703 |
| drawdown | 1663 |
| concurrency_p95>8 | 1607 |
| unstable_halves | 1254 |
| roi_copy<=0 | 755 |
| low_liquidity | 395 |
| both_sides | 372 |
| history<90d | 203 |
| hold<1h | 103 |
| top1_concentration | 63 |
| entries>=0.90 | 61 |
| short_crypto | 47 |
| segment_only:t<2.0 | 42 |
| closed<50 | 37 |
| segment_only:drawdown | 28 |
| sniping | 27 |
| profit_from<0.10 | 25 |
| segment_only:unstable_halves | 15 |
| segment_only:roi_copy<=0 | 4 |

## Причины отсева, стадия 3

| Причина | Кошельков |
|---|---|
| delayed_roi<=0 | 25 |
| edge_decays_with_delay | 6 |

## Финалисты

| Кошелёк | Имя | Категория | ROI/ставку | t | ROI задерж. 30 с | ROI задерж. 5 мин | Маркаут 24ч | Одноврем. p95 | Удерж., ч | Проскальз. | Утверждённые сегменты |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xf34f16e0aa20d5abb576bd373e460347d8c5b829` | Fitor | Sports | 0.4147 | 2.11 | 0.2609 | 0.2085 | 0.3803 | 5.0 | 2.86 | 0.0 | все рынки |
| `0x3c14d6729861ea0dd9a7cd246a79280a0ceca20a` | KVBA7 | Sports | 0.1115 | 2.63 | 0.119 | 0.1281 | 0.1003 | 6.0 | 16.33 | 0.0182 | Sports (n=79, roi=+0.18) | Sports / Other sport (n=41, roi=+0.18) | Sports / Other sport / type=binary (n=41, roi=+0.18) | Sports / Other sport / live (n=41, roi=+0.18) | Sports / Soccer (n=36, roi=+0.17) | Sports / price=0.70-0.90 (n=46, roi=+0.14) |
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | Sports | 0.1084 | 1.85 | 0.0717 | 0.0663 | 0.1072 | 3.0 | 4.2 | н/д | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | Sports | 0.057 | 1.47 | 0.0719 | 0.0944 | 0.0593 | 5.0 | 3.3 | 0.0 | Sports / Soccer (n=62, roi=+0.09) | Sports / Soccer / pre (n=40, roi=+0.10) |
| `0x084fccc33d7f6dec43ec6565d095c07e76eb737e` |  | Sports | 0.0751 | 1.59 | 0.0579 | 0.0647 | 0.0715 | 3.0 | 8.2 | н/д | Sports (n=61, roi=+0.10) | Sports / Soccer (n=40, roi=+0.11) |
| `0xe3015c631605e328b39f5888da942b3078ab9bd9` | Miami222 | Sports | 0.2032 | 1.09 | 0.0361 | 0.041 | 0.0982 | 6.0 | 16.72 | 0.0 | Sports / price=0.50-0.70 (n=30, roi=+0.24) |
| `0x097bc96aa01bdc70705b8bdc86c9527265582907` | acey17 | Sports | 0.1078 | 1.24 | 0.0318 | 0.0242 | 0.1239 | 6.0 | 2.34 | н/д | Sports / price=0.30-0.50 (n=47, roi=+0.29) |
| `0x6f5ce61d6f49ad5d6f8a93a28af2807fe083bf79` | 0x6f5Ce61D6F49ad5D6F8a93A28Af2807fE083bF79-1782228615289 | Sports | 0.0961 | 1.19 | 0.0379 | 0.0424 | 0.122 | 6.0 | 5.05 | 0.0 | Sports / price=0.50-0.70 (n=32, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=32, roi=+0.21) |
| `0x1073cb696e3265bdabc8bafbfd818f0cd3f79b1f` | 0x1073Cb696E3265bDABC8BafbFD818F0Cd3f79b1f-1774760477935 | Esports | 0.0625 | 0.85 | 0.0343 | 0.0353 | 0.1047 | 5.0 | 15.43 | 0.0 | Esports / Esports / type=moneyline (n=73, roi=+0.16) | Esports / Esports / pre (n=69, roi=+0.14) |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | Sports | 0.029 | 1.59 | 0.0822 | 0.0952 | 0.0984 | 8.0 | 3.16 | 0.0 | Esports / price=0.50-0.70 (n=51, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=51, roi=+0.19) | Esports / Esports / Counter Strike (n=148, roi=+0.10) |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | Esports | -0.031 | -0.62 | 0.059 | 0.0674 | 0.2059 | 5.0 | 5.85 | н/д | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | Sports | 0.0989 | 1.15 | 0.0199 | 0.0368 | 0.0892 | 4.0 | 4.35 | 0.0694 | Sports / price=0.50-0.70 (n=51, roi=+0.17) | Sports / Soccer / price=0.50-0.70 (n=51, roi=+0.17) |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | Sports | 0.0531 | 1.15 | 0.0327 | 0.0513 | 0.1575 | 6.0 | 4.17 | н/д | Sports / price=0.50-0.70 (n=207, roi=+0.14) |
| `0xa70ff0f435600e9779627ff1b6906fcc1691143d` | 0xA70ff0F435600e9779627fF1b6906fCC1691143D-1775659489890 | Sports | 0.0595 | 1.07 | 0.0718 | 0.0821 | 0.0689 | 7.0 | 3.97 | 0.0 | Sports / price=0.50-0.70 (n=66, roi=+0.17) |
| `0x776713e6791578ffa93fb6cc81da941dd4334fb2` | 0x776713E6791578FFA93Fb6cc81da941dD4334fB2-1769702052456 | Esports | 0.0299 | 0.61 | 0.0226 | 0.0317 | 0.0675 | 5.0 | 3.2 | н/д | Esports / Esports / type=moneyline (n=80, roi=+0.20) |

## Кандидаты только на сегмент

| Кошелёк | Имя | ROI общий | Утверждённые сегменты | Причины |
|---|---|---|---|---|
| `0xac14ffd60705eb2c3311334f1809bc406332fcaa` | 0xaC14ffD60705eb2C3311334F1809bC406332FcAa-1770484111054 | 0.1084 | Sports / Soccer / Indian Premier League (n=43, roi=+0.31) | segment_only:t<2.0 |
| `0xf68aa71cb5187d1e3ceb22fa07ca40aae7e25b13` |  | 0.057 | Sports / Soccer (n=62, roi=+0.09) | Sports / Soccer / pre (n=40, roi=+0.10) | segment_only:t<2.0 |
| `0x084fccc33d7f6dec43ec6565d095c07e76eb737e` |  | 0.0751 | Sports (n=61, roi=+0.10) | Sports / Soccer (n=40, roi=+0.11) | segment_only:t<2.0 |
| `0xd3911bd5e070c9ad9a9519c966347802d8f3b109` | lfg100k | -0.0603 | Sports / price=0.70-0.90 (n=80, roi=+0.07) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xfd8ff771a52c22a8a29a3156572d9b3e47fd761d` |  | 0.1908 | Sports / American Football / pre (n=58, roi=+0.26) | Sports / American Football / type=spreads (n=44, roi=+0.28) | segment_only:t<2.0 |
| `0xc7ff72c4e9bcb104faaffe1cb19fdf968c698a60` | zhengzh09 | 0.1026 | Sports / Soccer / price=0.50-0.70 (n=91, roi=+0.26) | Sports / Soccer / type=moneyline (n=47, roi=+0.28) | Sports / Soccer / pre (n=97, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xcb7ff0ad390ca732ff9d54f5f6da58888046824b` | silentvector10 | 0.098 | Sports / price=0.50-0.70 (n=74, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0xe3015c631605e328b39f5888da942b3078ab9bd9` | Miami222 | 0.2032 | Sports / price=0.50-0.70 (n=30, roi=+0.24) | segment_only:t<2.0 |
| `0x097bc96aa01bdc70705b8bdc86c9527265582907` | acey17 | 0.1078 | Sports / price=0.30-0.50 (n=47, roi=+0.29) | segment_only:t<2.0;segment_only:drawdown |
| `0x67b6ccabe5f6c01a7a9ecad5d420ea0cdc7f00bc` | forget4 | -0.031 | Sports / Basketball / price=0.30-0.50 (n=53, roi=+0.25) | Sports / Basketball / pre (n=45, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x6f5ce61d6f49ad5d6f8a93a28af2807fe083bf79` | 0x6f5Ce61D6F49ad5D6F8a93A28Af2807fE083bF79-1782228615289 | 0.0961 | Sports / price=0.50-0.70 (n=32, roi=+0.21) | Sports / Soccer / price=0.50-0.70 (n=32, roi=+0.21) | segment_only:t<2.0 |
| `0x1073cb696e3265bdabc8bafbfd818f0cd3f79b1f` | 0x1073Cb696E3265bDABC8BafbFD818F0Cd3f79b1f-1774760477935 | 0.0625 | Esports / Esports / type=moneyline (n=73, roi=+0.16) | Esports / Esports / pre (n=69, roi=+0.14) | segment_only:t<2.0 |
| `0x19f3ab1ed7c34f6e389ea267f27e83b87b2f4a8d` | brigandine1 | 0.0989 | Sports / price=0.50-0.70 (n=51, roi=+0.17) | Sports / Soccer / price=0.50-0.70 (n=51, roi=+0.17) | segment_only:t<2.0 |
| `0x5f4a0508541e6930f13bc679851dedeb18699484` | rubenoved | 0.029 | Esports / price=0.50-0.70 (n=51, roi=+0.19) | Esports / Esports / price=0.50-0.70 (n=51, roi=+0.19) | Esports / Esports / Counter Strike (n=148, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x32212e3afae7ed032e2bd5cbf6221942723912b2` | 0x32212e3AfaE7Ed032e2BD5cbF6221942723912b2-1782914196295 | 0.0784 | Sports / price=0.70-0.90 (n=33, roi=+0.12) | Sports / Soccer / price=0.70-0.90 (n=33, roi=+0.12) | segment_only:t<2.0 |
| `0x89879980a13fb82269cc489154fafbad8241d5b9` | soocas | 0.0524 | Esports / price=0.70-0.90 (n=41, roi=+0.11) | Esports / Esports / price=0.70-0.90 (n=41, roi=+0.11) | segment_only:t<2.0 |
| `0x87b51dda6918015dd1cf9837be13bf604f698395` | 0x87b51DdA6918015dD1Cf9837bE13BF604f698395-1772022034279 | 0.0093 | Sports / Other sport / price=0.70-0.90 (n=77, roi=+0.08) | Sports / Other sport (n=123, roi=+0.06) | Sports / Other sport / type=totals (n=36, roi=+0.10) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xd38ad20037839959d89165cf448568d584b28d26` | johnny234 | 0.0531 | Sports / price=0.50-0.70 (n=207, roi=+0.14) | segment_only:t<2.0;segment_only:drawdown |
| `0xa538af775227c7add77418ba079ea3ae6a9212c3` | WinsonEnterpriseCorp | -0.0214 | Sports (n=58, roi=+0.19) | Sports / price=0.50-0.70 (n=35, roi=+0.22) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xa70ff0f435600e9779627ff1b6906fcc1691143d` | 0xA70ff0F435600e9779627fF1b6906fCC1691143D-1775659489890 | 0.0595 | Sports / price=0.50-0.70 (n=66, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x3c2bcfde4caff0b4dd00d75d1b0e8f5fe2ddaf40` |  | -0.0045 | Sports / Soccer / price=0.50-0.70 (n=53, roi=+0.14) | segment_only:roi_copy<=0;segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x079a39f6d15ef5607ab19f27e75a06aa8a46d3df` | Mohammad463 | 0.0023 | Sports / Soccer / Indian Premier League (n=97, roi=+0.06) | Sports / price=0.70-0.90 (n=136, roi=+0.05) | Sports / Soccer / price=0.70-0.90 (n=65, roi=+0.07) | segment_only:t<2.0;segment_only:unstable_halves |
| `0xd5ad2f7f97be8852d87e0cec4568ef279ba65a42` | fxcougar | 0.0342 | Sports / American Football (n=153, roi=+0.17) | segment_only:t<2.0;segment_only:drawdown |
| `0x50f97e9c24050ca2cd7f0fef900df984e1d0c327` | 0x50f97e9C24050cA2cd7f0fEf900Df984e1d0c327-1759622213387 | 0.0085 | Esports / price=0.50-0.70 (n=107, roi=+0.12) | Esports / Esports / price=0.50-0.70 (n=107, roi=+0.12) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x1d2a24c3c963c45b481ee5f1da90fa0efddb8f8f` | 0x1d2A24C3c963C45B481ee5F1Da90Fa0EFDDB8F8F-1772559011215 | 0.082 | Sports / Soccer / live (n=45, roi=+0.29) | segment_only:t<2.0 |
| `0x776713e6791578ffa93fb6cc81da941dd4334fb2` | 0x776713E6791578FFA93Fb6cc81da941dD4334fB2-1769702052456 | 0.0299 | Esports / Esports / type=moneyline (n=80, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x67c6db64633f4af39509030a30cfcf215acbb6c1` | RoloMatic | 0.0554 | Sports / American Football / NFL (n=31, roi=+0.21) | segment_only:t<2.0 |
| `0x322e713038d4174394c7302aa42e04db60b2ef2c` | Gladiator02 | 0.0489 | Sports / Soccer (n=34, roi=+0.25) | Sports / Soccer / pre (n=34, roi=+0.25) | segment_only:t<2.0 |
| `0xf7dbb3d567fea98e1bf59538e1461f741eb0d23a` | Brian88888 | 0.0758 | Sports / Tennis / price=0.50-0.70 (n=49, roi=+0.19) | segment_only:t<2.0;segment_only:drawdown |
| `0x670d76669e567a24a9876f92310436d029020825` | ebglyss | 0.0374 | Sports / Basketball / price=0.50-0.70 (n=32, roi=+0.25) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x37e944c698f533d3144d1175f3e846dcafb9eede` | GaoJin-GamblingGod | 0.0609 | Sports / Soccer / FIFA World Cup (n=76, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x7714c16f86bcfdba47bfcb161dc39a2a1ff2b814` | llllllIIIIIIlIllllllIIIIIIlIllllllIIIIIIlI | 0.0361 | Sports / Soccer (n=62, roi=+0.35) | Sports (n=95, roi=+0.24) | Sports / Soccer / live (n=36, roi=+0.35) | Sports / Soccer / type=moneyline (n=34, roi=+0.31) | Sports / Soccer / price=0.50-0.70 (n=31, roi=+0.23) | Sports / price=0.50-0.70 (n=33, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0xad6a849b0139699f370d1d467c00503c8fef9dbd` | stillachance | 0.0106 | Sports / MMA/Boxing / live (n=30, roi=+0.34) | segment_only:t<2.0;segment_only:drawdown |
| `0x8e48477d8466e5c83f5ba23a8db0edc8f2939c5f` | hapiness | 0.0467 | Sports / Basketball / NBA 2026 (n=37, roi=+0.48) | Sports / Basketball (n=38, roi=+0.45) | Sports / Basketball / type=moneyline (n=38, roi=+0.45) | Sports / Basketball / pre (n=38, roi=+0.45) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0xbafa197f7eecfc2fd2fe348cb995bba6812402e0` | Sylas | 0.0402 | Esports / price=0.50-0.70 (n=447, roi=+0.08) | Esports / Esports / price=0.50-0.70 (n=447, roi=+0.08) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |
| `0x5e5175106a7dbbd92b10f1b56458fc8c1bdd42ce` | 0x5E5175106a7Dbbd92B10f1b56458Fc8c1Bdd42ce-1730865746538 | 0.04 | Esports / price=0.30-0.50 (n=122, roi=+0.26) | Esports / Esports / price=0.30-0.50 (n=122, roi=+0.26) | Esports / Esports / type=moneyline (n=118, roi=+0.24) | Esports / Esports / live (n=388, roi=+0.11) | segment_only:t<2.0;segment_only:drawdown |
| `0x85f031d069de300055900c4055c1baeb6bde3f67` | RJW1 | 0.0639 | Sports / price=0.50-0.70 (n=77, roi=+0.19) | Sports / Soccer / price=0.50-0.70 (n=54, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0x751be7122f148fba5aa2021ace98edc2001873fd` | Caishenbaoyouwo888 | 0.0624 | Esports / Esports / League of Legends (n=153, roi=+0.20) | segment_only:t<2.0;segment_only:drawdown |
| `0x791e45264c99eecaeb095caea9ad863740d29bda` | easymoneysniperzz | 0.0457 | Esports / Esports / type=map_handicap (n=130, roi=+0.21) | segment_only:t<2.0;segment_only:drawdown |
| `0x0e9781eec995a96a253291a2a20b282336a48ffa` | Peupo012 | 0.129 | Sports / Soccer / price=0.50-0.70 (n=129, roi=+0.14) | Sports / price=0.50-0.70 (n=133, roi=+0.13) | segment_only:t<2.0;segment_only:drawdown;segment_only:unstable_halves |

## Прошедшие стадию 2 целиком, по скору

| Кошелёк | Имя | Категория | Закрытых | ROI/ставку | ROI trimmed | t | Винрейт | Одноврем. p95 | Удерж., ч | Мед. объём | Стадия 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0xe0ec87e9b079493d0dbb1080d79650c7bfdaa9c4` | ATL777 | Sports | 954 | 0.3383 | 0.2497 | 10.49 | 0.745 | 8.0 | 1.16 | 32842 | delayed_roi<=0 |
| `0xf34f16e0aa20d5abb576bd373e460347d8c5b829` | Fitor | Sports | 67 | 0.4147 | 0.2629 | 2.11 | 0.552 | 5.0 | 2.86 | 1673726 | прошёл |
| `0x3c14d6729861ea0dd9a7cd246a79280a0ceca20a` | KVBA7 | Sports | 106 | 0.1115 | 0.128 | 2.63 | 0.821 | 6.0 | 16.33 | 177313 | прошёл |
| `0xb31e41965df4ab8014de4c4d8da9deff0a6ac120` | C63AMG | Sports | 698 | 0.1211 | 0.0593 | 3.47 | 0.726 | 8.0 | 2.87 | 396955 | delayed_roi<=0 |

## Утверждённые сегменты, топ по n × ROI

| Кошелёк | Сегмент | n | ROI | ROI сжатый | t | Винрейт |
|---|---|---|---|---|---|---|
| `0x86c878cd…` | Sports / price=0.00-0.10 | 213 | 13.1189 | 12.1112 | 5.93 | 0.225 |
| `0x86c878cd…` | Sports / Tennis / price=0.00-0.10 | 77 | 23.4349 | 18.8873 | 5.01 | 0.351 |
| `0x465ace6e…` | Sports / price=0.00-0.10 | 50 | 26.926 | 20.4687 | 5.14 | 0.58 |
| `0xeda67a7f…` | Sports / price=0.00-0.10 | 97 | 15.2607 | 13.1744 | 4.13 | 0.186 |
| `0xe9f5c75e…` | Sports / price=0.00-0.10 | 85 | 13.5213 | 11.1056 | 4.18 | 0.329 |
| `0xe9f5c75e…` | Sports / Basketball / price=0.00-0.10 | 69 | 14.8604 | 11.7095 | 4.03 | 0.362 |
| `0xb209ec04…` | Esports / price=0.00-0.10 | 128 | 9.6829 | 8.5245 | 3.79 | 0.18 |
| `0xb209ec04…` | Esports / Esports / price=0.00-0.10 | 128 | 9.6829 | 8.5245 | 3.79 | 0.18 |
| `0x465ace6e…` | Sports / Tennis | 133 | 8.0667 | 7.5776 | 4.0 | 0.722 |
| `0x465ace6e…` | Sports | 309 | 4.9858 | 4.9457 | 4.95 | 0.718 |
| `0x1941ca5d…` | Sports / Other sport / price=0.00-0.10 | 818 | 2.9671 | 2.9183 | 2.23 | 0.226 |
| `0x1941ca5d…` | Sports / price=0.00-0.10 | 819 | 2.9629 | 2.9143 | 2.23 | 0.226 |
| `0x86c878cd…` | Sports / Tennis / type=tennis_match_totals | 131 | 8.109 | 7.2176 | 3.53 | 0.794 |
| `0xb209ec04…` | Sports / price=0.00-0.10 | 244 | 5.617 | 5.2756 | 3.99 | 0.139 |
| `0xb209ec04…` | Sports / Soccer / price=0.00-0.10 | 147 | 7.2153 | 6.4842 | 3.61 | 0.17 |
| `0x465ace6e…` | Sports / Tennis / WTA | 36 | 17.6494 | 12.8908 | 2.99 | 0.778 |
| `0xeda67a7f…` | Sports | 462 | 3.4419 | 3.4258 | 4.17 | 0.545 |
| `0x86c878cd…` | Sports / Tennis / live | 754 | 2.5027 | 2.4736 | 4.63 | 0.66 |
| `0x465ace6e…` | Sports / Tennis / live | 55 | 10.8553 | 9.114 | 2.79 | 0.818 |
| `0x86c878cd…` | Sports | 2247 | 1.4233 | 1.4229 | 6.32 | 0.636 |
| `0x86c878cd…` | Sports / Tennis | 833 | 2.3297 | 2.3074 | 4.75 | 0.648 |
| `0xeda67a7f…` | Sports / Tennis / price=0.00-0.10 | 36 | 13.2693 | 9.6214 | 2.28 | 0.167 |
| `0xb209ec04…` | Sports / Soccer / type=soccer_second_half_team_totals | 44 | 12.0471 | 8.6293 | 2.81 | 0.636 |
| `0x9b979a06…` | Sports / price=0.00-0.10 | 50 | 11.0001 | 7.9326 | 2.53 | 0.32 |
| `0x86c878cd…` | Sports / Soccer / price=0.00-0.10 | 84 | 6.9336 | 5.8654 | 2.57 | 0.131 |
| `0x76697d10…` | Sports / Basketball / price=0.00-0.10 | 52 | 10.0148 | 7.393 | 2.85 | 0.269 |
| `0xe9f5c75e…` | Sports / Basketball / live | 458 | 2.5298 | 2.4591 | 4.18 | 0.618 |
| `0xeda67a7f…` | Sports / Soccer / price=0.00-0.10 | 31 | 13.5161 | 9.4139 | 2.17 | 0.161 |
| `0x465ace6e…` | Sports / Tennis / pre | 78 | 6.1004 | 5.7381 | 2.95 | 0.654 |
| `0x1941ca5d…` | Sports / Other sport | 2875 | 0.9401 | 0.94 | 2.47 | 0.537 |
| `0x1941ca5d…` | Sports / Other sport / type=binary | 2875 | 0.9401 | 0.94 | 2.47 | 0.537 |
| `0x1941ca5d…` | Sports | 2877 | 0.9396 | 0.9395 | 2.47 | 0.537 |
| `0x76697d10…` | Sports / price=0.00-0.10 | 67 | 7.5488 | 5.946 | 2.72 | 0.209 |
| `0x465ace6e…` | Sports / Tennis / ATP | 56 | 6.9698 | 6.2739 | 2.62 | 0.732 |
| `0x86c878cd…` | Sports / Tennis / WTA | 197 | 3.371 | 3.1874 | 2.73 | 0.665 |
| `0x41558102…` | Sports / price=0.00-0.10 | 40 | 10.2323 | 6.9292 | 2.43 | 0.3 |
| `0xb209ec04…` | Sports | 1535 | 1.0685 | 1.069 | 4.62 | 0.517 |
| `0xb209ec04…` | Esports / Esports / live | 946 | 1.3458 | 1.341 | 3.78 | 0.508 |
| `0xb209ec04…` | Sports / Soccer / type=second_half_totals | 97 | 4.8095 | 4.1771 | 2.41 | 0.526 |
| `0xb209ec04…` | Sports / Soccer | 888 | 1.3829 | 1.3769 | 4.01 | 0.511 |
| `0xb209ec04…` | Sports / Soccer / live | 617 | 1.6456 | 1.6288 | 3.4 | 0.478 |
| `0xb209ec04…` | Esports | 1201 | 1.1668 | 1.1659 | 4.07 | 0.501 |
| `0xb209ec04…` | Esports / Esports | 1201 | 1.1668 | 1.1659 | 4.07 | 0.501 |
| `0xd970693a…` | Sports / price=0.00-0.10 | 332 | 2.2888 | 2.2042 | 4.34 | 0.41 |
| `0x09b045ba…` | Sports / price=0.00-0.10 | 123 | 4.0143 | 3.575 | 2.9 | 0.407 |
| `0x164cb85e…` | Sports / Other sport / price=0.00-0.10 | 377 | 2.1144 | 2.029 | 3.45 | 0.289 |
| `0x164cb85e…` | Sports / price=0.00-0.10 | 391 | 2.0645 | 1.9844 | 3.48 | 0.284 |
| `0xd970693a…` | Sports | 2406 | 0.7993 | 0.7993 | 10.26 | 0.664 |
| `0xb209ec04…` | Esports / Esports / Valorant | 199 | 2.9053 | 2.7414 | 2.41 | 0.482 |
| `0xeda67a7f…` | Sports / Tennis / live | 176 | 2.891 | 2.9078 | 2.32 | 0.574 |
| `0xe9f5c75e…` | Sports / Basketball / NBA 2026 | 533 | 1.7005 | 1.6693 | 3.62 | 0.583 |
| `0xeda67a7f…` | Sports / Tennis | 186 | 2.7226 | 2.7549 | 2.31 | 0.57 |
| `0x86c878cd…` | Sports / Tennis / ATP | 398 | 1.9064 | 1.8812 | 3.1 | 0.631 |
| `0xe9f5c75e…` | Sports / Basketball | 969 | 1.2129 | 1.2054 | 4.18 | 0.561 |
| `0xeda67a7f…` | Sports / Soccer / live | 166 | 2.8893 | 2.9072 | 2.37 | 0.524 |
| `0xeda67a7f…` | Sports / Soccer | 170 | 2.8177 | 2.8427 | 2.36 | 0.524 |
| `0x1985327e…` | Sports | 1300 | 1.0239 | 1.0239 | 2.65 | 0.717 |
| `0x1985327e…` | Sports / Soccer / live | 848 | 1.2299 | 1.2251 | 2.08 | 0.704 |
| `0x1985327e…` | Sports / Soccer | 858 | 1.2155 | 1.2111 | 2.08 | 0.703 |
| `0x09b045ba…` | Sports | 1641 | 0.8746 | 0.8746 | 7.91 | 0.715 |
