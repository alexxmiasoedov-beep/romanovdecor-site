#!/usr/bin/env python3
# Система цен и скидок: конечный клиент, мастер, дилер, регион.
# Принцип — скидка считается в марже на метр, а не в процентах от цены.
from costs import cost, WALL, FLOOR, RATE

MAT = {'стены': cost(WALL), 'полы': cost(FLOOR)}   # себестоимость материала, $/м²

# ── розница под ключ, «Памятка: цены стены и полы» ────────────────────────
MIN_M2 = 20
D_FROM, D_TO = 35, 120
RETAIL = {'стены': dict(name='стены', hi=40, lo=34, work=24),
          'полы':  dict(name='полы', hi=50, lo=45, work=25)}

# Предложение: второй участок кривой для крупных объектов. Себестоимость
# его выдерживает — на дне остаётся $17,4 по стенам и $17,5 по полам.
BIG_TO = 500
BIG_LO = {'стены': 28, 'полы': 39}

# ── уровни продажи материала ──────────────────────────────────────────────
# target — целевая маржа в $ на метр, одинаковая для стен и полов.
# price  — назначенная цена, округлённая от target.
TIERS = [
    ('Конечный клиент', 'внутри цены под ключ',      None, {'стены': 34, 'полы': 45}),
    ('Мастер',          'наносит сам, от 50 м²',     12.0, {'стены': 23, 'полы': 34}),
    ('Дилер',           'перепродаёт, от 300 м²/кв', 8.0,  {'стены': 19, 'полы': 30}),
    ('Регион, опт',     'от 1000 м²/год',            5.5,  {'стены': 16, 'полы': 27}),
]

# ставка бригады за единицу работы, $ — сколько платим за нанесение
BRIGADE = (10, 12, 14, 16)
# на объектах единиц работы больше, чем площади: откосы, ниши, бортики
UNITS_PER_M2 = 1.42   # факт по объекту Лосика 53: 214,77 ед на 151,14 м²


def d(v): return f'${v:,.2f}'.replace(',', ' ')


def mat_rate(a, s, big=False):
    """Цена материала в рознице. big=True — с предложенным вторым участком."""
    if a <= D_FROM: return float(s['hi'])
    if a < D_TO:    return s['hi'] - (s['hi'] - s['lo']) * (a - D_FROM) / (D_TO - D_FROM)
    if not big:     return float(s['lo'])
    lo2 = BIG_LO[s['name']]
    if a >= BIG_TO: return float(lo2)
    return s['lo'] - (s['lo'] - lo2) * (a - D_TO) / (BIG_TO - D_TO)


def tiers_table():
    print('УРОВНИ ЦЕН НА МАТЕРИАЛ, $/м²')
    print(f'  {"уровень":<17}{"условие":<26}{"стены":>8}{"маржа":>9}{"×":>6}'
          f'{"полы":>8}{"маржа":>9}{"×":>6}')
    print(f'  {"себестоимость":<17}{"наша закупка, скидка 40%":<26}'
          f'{MAT["стены"]:>8.2f}{"":>9}{"":>6}{MAT["полы"]:>8.2f}')
    for name, cond, target, price in TIERS:
        row = f'  {name:<17}{cond:<26}'
        for k in ('стены', 'полы'):
            m = price[k] - MAT[k]
            row += f'{price[k]:>8}{m:>9.2f}{price[k] / MAT[k]:>6.2f}'
        print(row + (f'   цель ${target:.0f}' if target else ''))


def retail_ladder():
    print('\nПОД КЛЮЧ: КАК ТАЕТ ЦЕНА ПО ОБЪЁМУ')
    print('  (действующая шкала | предложение со вторым участком до 500 м²)')
    print(f'  {"м²":>5}' + ''.join(f'{k + ", мат":>13}{"маржа":>9}' for k in RETAIL))
    for a in (20, 35, 50, 80, 100, 120, 200, 300, 500, 800):
        row = f'  {a:>5}'
        for k, s in RETAIL.items():
            now = mat_rate(max(a, MIN_M2), s)
            big = mat_rate(max(a, MIN_M2), s, big=True)
            cell = f'{now:.0f}' if abs(now - big) < 0.01 else f'{now:.0f}|{big:.1f}'
            row += f'{cell:>13}{big - MAT[k]:>9.2f}'
        print(row)


def brigade_grid():
    print('\nЧТО ОСТАЁТСЯ ПОД КЛЮЧ НА ДНЕ ШКАЛЫ (120 м²+), $/м² поверхности')
    print(f'  единиц работы на метр площади: {UNITS_PER_M2}')
    print(f'  {"ставка бригады":<16}' + ''.join(f'{k:>12}' for k in RETAIL))
    for b in BRIGADE:
        row = f'  ${b} за единицу  '
        for k, s in RETAIL.items():
            rev = s['lo'] + s['work'] * UNITS_PER_M2
            left = rev - MAT[k] - b * UNITS_PER_M2
            row += f'{left:>12.2f}'
        print(row)
    print('  Из этого остатка платятся доставка, бой, переделки, гарантия,')
    print('  аренда, реклама, налог и прибыль.')


def channels():
    print('\nСРАВНЕНИЕ КАНАЛОВ, валовая маржа с метра')
    b = 14
    for k, s in RETAIL.items():
        rev = s['lo'] + s['work'] * UNITS_PER_M2
        own = rev - MAT[k] - b * UNITS_PER_M2
        deal = TIERS[2][3][k] - MAT[k]
        print(f'  {k:<7} под ключ {own:>7.2f}   дилер {deal:>6.2f}   '
              f'соотношение ×{own / deal:.1f}')
    print(f'  (бригада взята ${b} за единицу — подставь свою)')


def protect():
    print('\nЗАЩИТА РОЗНИЦЫ: во что материал превращается у покупателя')
    print(f'  {"уровень":<17}' + ''.join(f'{k + " под ключ":>18}' for k in RETAIL))
    for name, cond, target, price in TIERS[1:]:
        row = f'  {name:<17}'
        for k, s in RETAIL.items():
            row += f'{price[k] + s["work"] * UNITS_PER_M2:>18.2f}'
        print(row)
    row = f'  {"наша розница":<17}'
    for k, s in RETAIL.items():
        row += f'{s["lo"] + s["work"] * UNITS_PER_M2:>18.2f}'
    print(row)
    print('  Считано при работе по нашей ставке. Кто ставит работу дешевле —')
    print('  падает ниже, поэтому нужна РРЦ и закреплённая территория.')


if __name__ == '__main__':
    tiers_table()
    retail_ladder()
    brigade_grid()
    channels()
    protect()
