#!/usr/bin/env python3
# Себестоимость материала на 1 м². Расход — фактический, по рецептуре студии.
# Цены закупки поставь в PRICES, всё остальное посчитается само.

# $/кг франко-склад в Минске. None — цену ещё не подставили.
PRICES = {
    'bs3000':  None,   # связующее BS 3000
    'песок':   0.20,   # кварцевый песок, рыночный ориентир
    'мука':    0.35,   # кварцевая мука, рыночный ориентир
    'primer':  None,   # Remmers Primer PF
    'aqua':    None,   # лак PUR Aqua 500m (стены)
    'tx':      None,   # лак PUR TX (полы)
}

# кг на 1 м² готовой поверхности
WALL = {'bs3000': 0.380, 'песок': 0.168, 'мука': 0.112, 'aqua': 0.100}
FLOOR = {'primer': 0.700, 'bs3000': 0.280, 'песок': 0.168, 'мука': 0.112, 'tx': 0.100}

NAMES = {'bs3000': 'BS 3000', 'песок': 'песок кварцевый', 'мука': 'мука кварцевая',
         'primer': 'Primer PF Remmers', 'aqua': 'лак PUR Aqua 500m', 'tx': 'лак PUR TX'}

# публичная цена из памятки: строка «материал», $/м²
PRICE_LINE = {'стены': (40, 34), 'полы': (50, 45)}


def cost(recipe):
    """Себестоимость $/м² и список неизвестных позиций."""
    total, unknown = 0.0, []
    for k, kg in recipe.items():
        p = PRICES.get(k)
        if p is None:
            unknown.append(k)
        else:
            total += kg * p
    return total, unknown


def table(recipe, title, areas=(20, 35, 50, 80, 100, 120, 150)):
    print(f'\n{title}')
    print('  расход на 1 м²:')
    for k, kg in recipe.items():
        print(f'    {NAMES[k]:<22} {kg * 1000:>6.0f} г')
    print(f'    {"итого":<22} {sum(recipe.values()) * 1000:>6.0f} г')
    print('\n  закупка на объём, кг:')
    head = '   м²  ' + ''.join(f'{NAMES[k][:14]:>16}' for k in recipe) + f'{"всего":>10}'
    print(head)
    for a in areas:
        line = f'  {a:>3}  ' + ''.join(f'{kg * a:>16.1f}' for kg in recipe.values())
        print(line + f'{sum(recipe.values()) * a:>10.1f}')
    c, unknown = cost(recipe)
    if unknown:
        print(f'\n  себестоимость: не считается — нет цены на {", ".join(NAMES[k] for k in unknown)}')
        print(f'  посчитанная часть: ${c:.2f}/м²')
    else:
        print(f'\n  себестоимость материала: ${c:.2f}/м²')


def margin(name, recipe):
    c, unknown = cost(recipe)
    if unknown:
        return
    hi, lo = PRICE_LINE[name]
    print(f'  {name}: себестоимость ${c:.2f} · цена ${hi}–{lo} · '
          f'маржа ${hi - c:.2f}–{lo - c:.2f} (×{hi / c:.1f}–{lo / c:.1f})')


if __name__ == '__main__':
    table(WALL, 'СТЕНЫ')
    table(FLOOR, 'ПОЛЫ')
    print('\nСТРОКА «МАТЕРИАЛ» В ПАМЯТКЕ')
    margin('стены', WALL)
    margin('полы', FLOOR)
