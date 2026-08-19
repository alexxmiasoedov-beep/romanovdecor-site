#!/usr/bin/env python3
# Себестоимость материала на 1 м². Расход — фактическая рецептура студии.
# Цены — розница по Минску, август 2026, в евро. Закупка в BYN, курс в RATE.

RATE = 3.5093  # BYN/EUR, курс НБ РБ на 19.08.2026 (доллар — 3,0313)
CUR = '\u20ac'  # считаем в евро: компоненты немецкие, закупка привязана к евро

# Дилерская скидка студии на позиции Remmers. Кварцевый песок берётся
# не у дилера, поэтому идёт по рознице.
DISCOUNT = 0.40
NO_DISCOUNT = {'песок'}

# (цена за фасовку в BYN, вес фасовки в кг, источник)
PRICES = {
    'bs3000': (2372.89, 25, 'Epoxy BS 3000 SG, Боден-Системс, Минск'),
    'primer': (1987.20, 30, 'Epoxy Primer PF New, Inshi, Минск'),
    'aqua':   (1517.76, 10, 'PUR Aqua Top 500 2K M, Боден-Системс'),
    'tx':     (3108.00, 10, 'PUR Top TX, Боден-Системс'),
    'мука':   (39.00,   25, 'Silverbond 30 EW, Боден-Системс'),
    'песок':  (16.00,   25, 'кварцевый песок 0,4–0,6, Dorbox, Минск'),
}

# Переход с Primer PF на другую смолу — 20 BYN за кг. Цена уже конечная,
# дилерская скидка к ней не применяется. Поставь False, чтобы вернуться
# к расчёту на Primer PF.
USE_RESIN = True
if USE_RESIN:
    PRICES['primer'] = (20.00, 1, 'смола на замену Primer PF, 20 BYN/кг')
    NO_DISCOUNT.add('primer')

# Альтернатива, если остаёмся на Primer PF: у Боден-Системс Epoxy Primer PF
# Neutral 30 кг стоит 1432,44 BYN против 1987,20 у Inshi.
# PRICES['primer'] = (1432.44, 30, 'Epoxy Primer PF Neutral, Боден-Системс')

# кг на 1 м² готовой поверхности
WALL = {'bs3000': 0.380, 'песок': 0.168, 'мука': 0.112, 'aqua': 0.100}
FLOOR = {'primer': 0.700, 'bs3000': 0.280, 'песок': 0.168, 'мука': 0.112, 'tx': 0.100}

NAMES = {'bs3000': 'BS 3000', 'песок': 'песок кварцевый', 'мука': 'мука кварцевая',
         'primer': 'Primer PF', 'aqua': 'лак PUR Aqua 500', 'tx': 'лак PUR TX'}
if USE_RESIN: NAMES['primer'] = 'смола (грунт-слой)'

# публичная цена из памятки: строка «материал» и «работа», €/м²
MEMO = {'стены': dict(mat_hi=35, mat_lo=30, work=21),
        'полы':  dict(mat_hi=43, mat_lo=39, work=22)}


def usd_kg(key, net=True):
    """€/кг. net=True — со скидкой студии, False — розница."""
    byn, kg, _ = PRICES[key]
    p = byn / kg / RATE
    return p * (1 - DISCOUNT) if net and key not in NO_DISCOUNT else p


def cost(recipe, net=True):
    return sum(kg * usd_kg(k, net) for k, kg in recipe.items())


def prices_table():
    print(f'ЗАКУПКА: РОЗНИЦА МИНСК И СКИДКА {DISCOUNT:.0%}')
    print(f'  {"материал":<18}{"фасовка":>10}{"BYN":>10}{"розн €/кг":>11}{"со скидкой":>12}   источник')
    for k in ('bs3000', 'primer', 'aqua', 'tx', 'мука', 'песок'):
        byn, kg, src = PRICES[k]
        mark = '' if k not in NO_DISCOUNT else '  (без скидки)'
        print(f'  {NAMES[k]:<18}{kg:>7} кг{byn:>10.2f}{usd_kg(k, False):>11.2f}'
              f'{usd_kg(k):>12.2f}   {src}{mark}')


def table(recipe, title, areas=(20, 35, 50, 80, 100, 120, 150)):
    print(f'\n{title}')
    print(f'  {"компонент":<18}{"г/м²":>7}{"€/кг":>8}{"€/м²":>8}{"доля":>7}{"розница":>10}')
    c, gross = cost(recipe), cost(recipe, net=False)
    for k, kg in recipe.items():
        line = kg * usd_kg(k)
        print(f'  {NAMES[k]:<18}{kg * 1000:>7.0f}{usd_kg(k):>8.2f}{line:>8.2f}'
              f'{line / c * 100:>6.0f}%{kg * usd_kg(k, False):>10.2f}')
    print(f'  {"итого":<18}{sum(recipe.values()) * 1000:>7.0f}{"":>8}{c:>8.2f}{"":>7}{gross:>10.2f}')
    print('\n  закупка и деньги на объём:')
    print(f'  {"м²":>5}{"кг":>9}{"€":>10}{"BYN":>10}')
    for a in areas:
        print(f'  {a:>5}{sum(recipe.values()) * a:>9.1f}{c * a:>10.0f}{c * a * RATE:>10.0f}')


def margin(name, recipe):
    c = cost(recipe)
    m = MEMO[name]
    for tag, mat in (('20–35 м²', m['mat_hi']), ('100 м²+', m['mat_lo'])):
        full = mat + m['work']
        print(f'  {name:<6}{tag:<10} материал €{mat}  себестоимость €{c:>6.2f}  '
              f'наценка ×{mat / c:.2f}  остаток €{mat - c:>6.2f}  '
              f'под ключ €{full} → €{full - c:>6.2f} на работу и всё остальное')


if __name__ == '__main__':
    prices_table()
    table(WALL, 'СТЕНЫ')
    table(FLOOR, 'ПОЛЫ')
    print('\nСТРОКА «МАТЕРИАЛ» В ПАМЯТКЕ ПРОТИВ РОЗНИЦЫ')
    margin('стены', WALL)
    margin('полы', FLOOR)
