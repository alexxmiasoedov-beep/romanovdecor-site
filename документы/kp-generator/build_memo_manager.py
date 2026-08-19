#!/usr/bin/env python3
# Прайс для менеджера: цены под ключ за м² в евро. Без курса и себестоимости —
# этот лист можно давать в руки и показывать клиенту.
import os

SC = os.environ.get('SC', '/tmp/kp')

MIN_M2 = 20
D_FROM, D_TO = 35, 100
PRICE = {'стены': dict(hi=35, lo=30), 'полы': dict(hi=43, lo=39)}
WORK = {'стены': dict(hi=21, lo=18.50), 'полы': dict(hi=22, lo=19.50)}


def curve(a, s):
    a = max(a, MIN_M2)
    if a <= D_FROM: return float(s['hi'])
    if a >= D_TO:   return float(s['lo'])
    return s['hi'] - (s['hi'] - s['lo']) * (a - D_FROM) / (D_TO - D_FROM)


def mat(a, k):  return curve(a, PRICE[k])
def work(a, k): return curve(a, WORK[k])
def key(a, k):  return mat(a, k) + work(a, k)
def a2(v):      return f'{v:.2f}'.replace('.', ',')
def eur(v):     return '€' + f'{v:,.0f}'.replace(',', ' ')

B = '#cbbf9f'; GRID = f'border:1px solid {B}'
TD  = f'{GRID};padding:3.2px 7px;font-size:9.5px;line-height:1.28;vertical-align:middle'
TDN = f'{TD};text-align:center;white-space:nowrap;font-variant-numeric:tabular-nums'
TH  = f'{GRID};padding:4.5px 7px;font-size:8.5px;letter-spacing:1.6px;text-transform:uppercase;font-weight:700;text-align:center;vertical-align:middle'
H3  = 'font-size:9px;letter-spacing:2.4px;text-transform:uppercase;margin:0 0 5px;color:#b8965a;font-weight:600'
TBL = 'width:100%;border-collapse:collapse;margin-bottom:10px'
GREEN, AMBER, BEIGE, DARK = '#f0f5e0', '#fdeed2', '#f5efe2', '#2c2c2c'
BIG = ';font-size:12px;font-weight:700'

def th(t, bg=DARK, c='#fff'): return f'<th style="{TH};background:{bg};color:{c}">{t}</th>'
def td(t, s=TD, bg=None):     return f'<td style="{s}{";background:"+bg if bg else ""}">{t}</td>'

AREAS = [20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]
rows = ''
for a in AREAS:
    label = f'до {a} м²' if a == MIN_M2 else (f'{a} м²' if a < D_TO else f'{a} м² и выше')
    cells = td(f'<b>{label}</b>', TDN, BEIGE)
    for k, bg in (('стены', GREEN), ('полы', AMBER)):
        val = (f'€{a2(key(a, k))}' if a > MIN_M2
               else f'<span style="font-size:9px;font-weight:600">фикс</span> {eur(key(a, k) * MIN_M2)}')
        cells += (td(f'€{a2(mat(a, k))}', TDN, bg) + td(f'€{a2(work(a, k))}', TDN, bg)
                  + td(val, TDN + BIG, bg))
    rows += f'<tr>{cells}</tr>'

table = (f'<table style="{TBL}"><tr>'
         f'<th rowspan="2" style="{TH};background:{DARK};color:#fff">Площадь</th>'
         f'<th colspan="3" style="{TH};background:#5a7236;color:#fff">Стены</th>'
         f'<th colspan="3" style="{TH};background:#a07a32;color:#fff">Полы</th></tr><tr>'
         + ''.join(th(t, '#3d4a2e', '#cfe0a8') for t in ('Материал', 'Работа', 'Под ключ'))
         + ''.join(th(t, '#4a3a1f', '#e8c88a') for t in ('Материал', 'Работа', 'Под ключ'))
         + f'</tr>{rows}</table>')

FIX = [('Дверь межкомнатная', '€90 за штуку + материал по площади полотна'),
       ('Потолок', 'работа +20% к ставке стен'),
       ('Лестница', 'работа +20% к ставке полов'),
       ('Мебель, столешницы', '€17,50 за м² плоскостей, €9 за пог. м кромки'),
       ('Гидроизоляционная лента', '€90 фиксированно на объект'),
       ('Малярные расходники, валики', '€90 фиксированно на объект'),
       ('Уклон к трапу в одну сторону', '€175'),
       ('Конверт к трапу', '€260'),
       ('Герметизация трапа', '€45'),
       ('Уклон в котельной', '€175'),
       ('Примыкание стена/пол без плинтуса', '€2,50 за пог. м'),
       ('Примыкание с паркетом, ламинатом', '€9 за пог. м'),
       ('Примыкание с плиткой', '€6 за пог. м'),
       ('Ремонт трещин в основании', '€4,50 за пог. м')]

RULES = [('До 20 м²', 'фикс за выезд: €1 120 стены, €1 300 полы'),
         ('20–35 м²', 'базовая цена за м², скидки нет'),
         ('35–100 м²', 'скидка растёт плавно, по формуле'),
         ('От 100 м²', 'дно: €48,50 стены, €58,50 полы')]

AREA_RULES = [('Материал', 'вся чистая поверхность, без вычетов'),
              ('Двери', 'по площади полотна — обе стороны и торцы'),
              ('Откосы, ниши, бортики', 'вся развёрнутая площадь'),
              ('Мебель, столешницы', 'плоскости по площади, кромка 0,1 м² за пог. м'),
              ('Запас на подрезку и бой', 'плюс 5% к расчётной площади')]

def pairs_tbl(items, bg):
    out = ''
    for a, b in items:
        out += '<tr>' + td(a, TD, bg) + td(f'<b>{b}</b>', TD + ';text-align:right') + '</tr>'
    return f'<table style="{TBL}">{out}</table>'


def two_col(items, bg):
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    out = ''
    for i in range(half):
        l = left[i]; r = right[i] if i < len(right) else ('', '')
        out += ('<tr>' + td(l[0], TD, bg) + td(f'<b>{l[1]}</b>', TD + ';text-align:right')
                + td(r[0], TD, bg) + td(f'<b>{r[1]}</b>' if r[1] else '', TD + ';text-align:right') + '</tr>')
    return f'<table style="{TBL}">{out}</table>'

logo = ('<svg width="44" height="44" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="32" height="32" rx="6" fill="#2c2c2c"/><text x="50%" y="54%" '
        'font-family="Geologica,Arial,sans-serif" font-size="20" font-weight="700" fill="#b8965a" '
        'text-anchor="middle" dominant-baseline="middle">r</text></svg>')

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:210mm}}</style></head><body>
<div style="width:100%;min-height:1123px;padding:18px 30px 14px;background:#fff;color:#2c2c2c;font-family:Geologica,Arial,sans-serif;display:flex;flex-direction:column">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:2px solid #b8965a;padding-bottom:8px">
  <div style="display:flex;align-items:center;gap:12px">{logo}
    <div><div style="font-size:18px;letter-spacing:2px;font-weight:500;text-transform:lowercase;line-height:1.1">romanov <span style="color:#b8965a">decor</span> studio</div>
    <div style="font-size:9px;color:#888;margin-top:4px;letter-spacing:1px;text-transform:uppercase">микроцемент на немецких компонентах</div></div></div>
  <div style="text-align:right;font-size:10px;color:#666;letter-spacing:1px">
    <div style="font-weight:600;color:#2c2c2c;font-size:13px">Прайс под ключ</div>
    <div style="margin-top:3px">евро за м² · август 2026</div></div>
</div>

<div style="display:flex;gap:10px;margin-bottom:11px">
  <div style="flex:1;padding:9px 14px;background:{DARK};color:#efece7;border-radius:6px;font-size:10px;line-height:1.5">
    <div style="color:#b8965a;letter-spacing:1.8px;text-transform:uppercase;font-size:8px;font-weight:700;margin-bottom:3px">Минимальный выезд</div>
    Объект до 20 м² считается фиксом, сколько бы ни было по факту:
    <b style="color:#b8965a">€1&nbsp;120</b> по стенам, <b style="color:#b8965a">€1&nbsp;300</b> по полам.
    Замес, фасовка, доставка и день бригады одинаковы хоть на 8 м², хоть на 20.
  </div>
  <div style="flex:1;padding:9px 14px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:6px;font-size:10px;line-height:1.5">
    <div style="color:#8a7346;letter-spacing:1.8px;text-transform:uppercase;font-size:8px;font-weight:700;margin-bottom:3px">Если поверхностей две</div>
    Стены и полы на одном объекте считаются вместе. Если суммарно вышло меньше
    20 м², добираем до двадцати по той поверхности, которой больше.
  </div>
</div>

<h3 style="{H3}">Цены</h3>
{table}

<h3 style="{H3}">Формулы для любой площади S от 35 до 100 м²</h3>
<div style="padding:9px 14px;background:{DARK};color:#efece7;border-radius:6px;margin-bottom:10px;
            font-size:10.5px;line-height:1.75;font-family:'Geologica',monospace;letter-spacing:0.3px">
  Материал стен&nbsp;&nbsp;= 35 − <b style="color:#b8965a">5</b> &times; (S − 35) ÷ 65<br>
  Работа стен&nbsp;&nbsp;&nbsp;&nbsp;= 21 − <b style="color:#b8965a">2,5</b> &times; (S − 35) ÷ 65<br>
  <span style="display:inline-block;height:4px"></span><br>
  Материал полов = 43 − <b style="color:#b8965a">4</b> &times; (S − 35) ÷ 65<br>
  Работа полов&nbsp;&nbsp;&nbsp;= 22 − <b style="color:#b8965a">2,5</b> &times; (S − 35) ÷ 65
</div>
<div style="font-size:9px;color:#666;line-height:1.45;margin:-6px 0 10px">
Кривая ровная, без ступеней: каждые 10 м² объекта снимают 77 центов с метра стен
и 62 цента с метра полов по материалу, и по 38 центов по работе.
Промежуточные площади можно брать на глаз между строками таблицы.
</div>

<div style="display:flex;gap:14px">
  <div style="flex:1">
    <h3 style="{H3}">Границы</h3>
    {pairs_tbl(RULES, BEIGE)}
  </div>
  <div style="flex:1.35">
    <h3 style="{H3}">Как считается площадь</h3>
    {pairs_tbl(AREA_RULES, GREEN)}
  </div>
</div>

<h3 style="{H3}">Фиксированные позиции — сверх цены за м²</h3>
{two_col(FIX, AMBER)}

<div style="margin-top:auto;padding-top:10px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:9.5px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Цены в евро, оплата по курсу на день оплаты</div>
</div>

</div></body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/memo-manager.html', 'w').write(html)
for a in AREAS:
    print(f'{a:3d} м²  стены €{a2(key(a, "стены")):>6} ({a2(mat(a, "стены"))} + {a2(work(a, "стены"))})   '
          f'полы €{a2(key(a, "полы")):>6} ({a2(mat(a, "полы"))} + {a2(work(a, "полы"))})')
