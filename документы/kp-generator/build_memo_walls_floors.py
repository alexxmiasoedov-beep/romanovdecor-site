#!/usr/bin/env python3
# Памятка по ценам: стены и полы. Готовые суммы, чтобы считать в трубку.
import os
SC = os.environ.get('SC', '/tmp/kp')
RATE = 2.9133

PKG   = {'wm': 800, 'ww': 500, 'fm': 1000, 'fw': 500}     # первые 20 м², пакетом
BANDS = [(20, 45), (45, 80), (80, 10**9)]
R = {'wm': [40, 38, 36], 'ww': [24, 22, 20],
     'fm': [50, 48, 46], 'fw': [25, 23, 21]}

def price(a, k):
    if a <= 20: return PKG[k]
    return PKG[k] + sum(max(0.0, min(a, hi) - lo) * r for (lo, hi), r in zip(BANDS, R[k]))

def a2(v): return f'{v:.2f}'.replace('.', ',')
def d(v):  return '$' + f'{v:,.0f}'.replace(',', ' ')
def byn(v): return f'{round(v * RATE):,}'.replace(',', ' ')

B = '#cbbf9f'; GRID = f'border:1px solid {B}'
TD  = f'{GRID};padding:2.5px 7px;font-size:9px;line-height:1.25;vertical-align:middle'
TDN = f'{TD};text-align:center;white-space:nowrap;font-variant-numeric:tabular-nums'
TH  = f'{GRID};padding:4px 7px;font-size:8px;letter-spacing:1.4px;text-transform:uppercase;font-weight:700;text-align:center;vertical-align:middle'
H3  = 'font-size:9px;letter-spacing:2.4px;text-transform:uppercase;margin:0 0 4px;color:#b8965a;font-weight:600'
TBL = 'width:100%;border-collapse:collapse;margin-bottom:9px'
GREEN, AMBER, BEIGE, DARK = '#f0f5e0', '#fdeed2', '#f5efe2', '#2c2c2c'

def th(t, bg=DARK, c='#fff'): return f'<th style="{TH};background:{bg};color:{c}">{t}</th>'
def td(t, s=TD, bg=None):     return f'<td style="{s}{";background:"+bg if bg else ""}">{t}</td>'

# ── 1. Шкала по слоям ─────────────────────────────────────────────────────
scale_rows = ''
for label, km, kw, pkg, bg in (('Стены', 'wm', 'ww', 1300, GREEN), ('Полы', 'fm', 'fw', 1500, AMBER)):
    cells = ''.join(td(f'${R[km][i]} + ${R[kw][i]}<br><b>${R[km][i] + R[kw][i]}</b>', TDN, bg) for i in range(3))
    scale_rows += ('<tr>' + td(f'<b>{label}</b>', TD, BEIGE)
                   + td(f'<b>{d(pkg)}</b><br>пакетом', TDN, BEIGE) + cells + '</tr>')
scale = (f'<table style="{TBL}"><tr>{th("")}{th("0–20 м²","#1f1b14","#b8965a")}'
         f'{th("21–45 м²")}{th("46–80 м²")}{th("81 м² и выше")}</tr>{scale_rows}</table>')

# ── 2. Готовые суммы ──────────────────────────────────────────────────────
AREAS = [20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 150, 200, 250, 300]
BIG = ';font-size:11px;font-weight:700'
sum_rows = ''
for a in AREAS:
    w = price(a, 'wm') + price(a, 'ww')
    f = price(a, 'fm') + price(a, 'fw')
    sum_rows += ('<tr>'
        + td(f'<b>{a} м²</b>', TDN, BEIGE)
        + td(f'${a2(w/a)}', TDN + BIG, GREEN) + td(d(w), TDN, GREEN) + td(byn(w), TDN, GREEN)
        + td(f'${a2(f/a)}', TDN + BIG, AMBER) + td(d(f), TDN, AMBER) + td(byn(f), TDN, AMBER)
        + '</tr>')
sums = (f'<table style="{TBL}"><tr>'
        f'<th rowspan="2" style="{TH};background:{DARK};color:#fff">Площадь</th>'
        f'<th colspan="3" style="{TH};background:#5a7236;color:#fff">Стены</th>'
        f'<th colspan="3" style="{TH};background:#a07a32;color:#fff">Полы</th></tr>'
        f'<tr>{th("Цена за м²","#3d4a2e","#cfe0a8")}{th("Всего $","#3d4a2e","#cfe0a8")}{th("Всего руб","#3d4a2e","#cfe0a8")}'
        f'{th("Цена за м²","#4a3a1f","#e8c88a")}{th("Всего $","#4a3a1f","#e8c88a")}{th("Всего руб","#4a3a1f","#e8c88a")}</tr>'
        f'{sum_rows}</table>')

# ── 3. Надбавки ───────────────────────────────────────────────────────────
EXTRA = [('Потолок', 'работа +20% к ставке стен'),
         ('Лестница', 'работа +20% к ставке полов'),
         ('Дверь', '$100 за штуку + материал по площади полотна'),
         ('Мебель, столешница', 'плоскости $20/м², кромка $10/м.п.'),
         ('Гидроизоляционная лента', '$100 фиксированно'),
         ('Малярные расходники', '$100 фиксированно')]
FLOOR_EXTRA = [('Уклон к трапу в одну сторону', '$200'), ('Конверт к трапу', '$300'),
               ('Герметизация трапа', '$50'), ('Уклон в котельной', '$200'),
               ('Примыкание стена/пол без плинтуса', '$3 / пог. м'),
               ('Примыкание с паркетом, ламинатом', '$10 / пог. м'),
               ('Примыкание с плиткой', '$7 / пог. м'), ('Ремонт трещин', '$5 / пог. м')]

def two_col(items, bg):
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    rows = ''
    for i in range(half):
        l = left[i]; r = right[i] if i < len(right) else ('', '')
        rows += ('<tr>' + td(l[0], TD, bg) + td(f'<b>{l[1]}</b>', TDN, BEIGE)
                 + td(r[0], TD, bg) + td(f'<b>{r[1]}</b>' if r[1] else '', TDN, BEIGE) + '</tr>')
    return f'<table style="{TBL}">{rows}</table>'

logo = ('<svg width="40" height="40" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="32" height="32" rx="6" fill="#2c2c2c"/><text x="50%" y="54%" '
        'font-family="Geologica,Arial,sans-serif" font-size="20" font-weight="700" fill="#b8965a" '
        'text-anchor="middle" dominant-baseline="middle">r</text></svg>')

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:210mm}}</style></head><body>
<div style="width:100%;min-height:1123px;padding:14px 30px 12px;background:#fff;color:#2c2c2c;font-family:Geologica,Arial,sans-serif;display:flex;flex-direction:column">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;border-bottom:2px solid #b8965a;padding-bottom:5px">
  <div style="display:flex;align-items:center;gap:10px">{logo}
    <div><div style="font-size:15px;letter-spacing:2px;font-weight:500;text-transform:lowercase;line-height:1.1">romanov <span style="color:#b8965a">decor</span> studio</div>
    <div style="font-size:8.5px;color:#888;margin-top:3px;letter-spacing:1px;text-transform:uppercase">микроцемент на немецких компонентах</div></div></div>
  <div style="text-align:right;font-size:9px;color:#666;letter-spacing:1px">
    <div style="font-weight:600;color:#2c2c2c;font-size:11px">Цены: стены и полы</div>
    <div style="margin-top:2px">внутренний документ · август 2026</div></div>
</div>

<h3 style="{H3}">1 · Шкала по объёму — считается по слоям</h3>
{scale}
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-6px 0 12px">
Первые 20 м² идут пакетом. Метры с 21-го по 45-й — по базовой цене, с 46-го дешевеют, с 81-го действует нижняя ставка.
<b>Скидка достаётся только тем метрам, что выше порога</b> — клиент не переезжает в дешёвую категорию целиком.
Цена никогда не падает при росте объёма: заказать 21 м² вместо 20 бессмысленно.
</div>

<h3 style="{H3}">2 · Цена за м² и сумма под ключ — чтобы не считать в уме</h3>
{sums}
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-6px 0 12px">
<b style="color:#2c2c2c">Отсчёт с 20 м².</b> Всё, что меньше, стоит столько же, сколько 20: {d(1300)} стены и {d(1500)} полы.
Это минимальный выезд — бригада, замес и расходники одинаковы хоть на 8 м², хоть на 20.<br>
Цена за м² — под ключ, материал плюс работа. Рубли — по курсу НБ РБ {a2(RATE)} BYN/USD, пересчитывать на день оплаты.
Промежуточные площади считаются по слоям из первой таблицы; между строками можно прикидывать на глаз, шаг цены мелкий.
</div>

<h3 style="{H3}">3 · Как считается объём</h3>
<div style="font-size:9px;line-height:1.5;padding:7px 12px;background:#faf6ef;border:1px solid #ece2d2;border-radius:5px;margin-bottom:12px">
<b>Материал</b> — вся чистая площадь поверхности, без вычетов.<br>
<b>Работа</b> — стороны от 0,5 м считаются в квадратных метрах; стороны меньше 0,5 м — в погонных метрах по большей стороне.
Это откосы, ниши, бортики, подступенки: нанесение на них идёт медленнее, чем на сплошной стене, поэтому метр там стоит как квадрат.
</div>

<h3 style="{H3}">4 · Надбавки и фиксы</h3>
{two_col(EXTRA, GREEN)}

<h3 style="{H3}">5 · Дополнительные работы по полам</h3>
{two_col(FLOOR_EXTRA, AMBER)}

<h3 style="{H3}">6 · Предел скидки</h3>
<div style="display:flex;gap:10px;margin-bottom:10px">
  <div style="flex:1;padding:8px 12px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">Прайс</div>
    Шкала выше — публичная цена, её печатаем в КП и в калькуляторе.
    Она сама даёт до 4% скидки на 100 м², до 8% на 200 м², до 10% на 300 м².
  </div>
  <div style="flex:1;padding:8px 12px;background:{DARK};color:#efece7;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#b8965a;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">Резерв торга</div>
    Сверх прайса — только при встречном условии: клиент сравнивает с конкурентом, вносит предоплату сразу или даёт портфолийный объект.
    <b style="color:#b8965a">Предел: $34–35 по стенам, $44–45 по полам.</b> Ниже — отказываемся от сделки.
  </div>
</div>
<div style="font-size:8.2px;color:#666;line-height:1.45;margin-bottom:10px">
<b style="color:#2c2c2c">Почему скидка неглубокая.</b> Метраж задан квартирой — скидка не увеличит заказ, она лишь выигрывает сделку у конкурента.
Каждые 10% скидки требуют в полтора раза больше объектов, чтобы вернуть ту же прибыль. Маржа в деньгах одинакова по стенам и полам на каждой ступени: $25 → $23 → $21 с метра.
</div>

<div style="margin-top:auto;padding-top:8px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:8.5px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Внутренний документ — клиенту не отдаём</div>
</div>

</div></body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/memo-walls-floors.html', 'w').write(html)
for a in (20, 50, 100, 150, 200, 300):
    w = price(a, 'wm') + price(a, 'ww'); f = price(a, 'fm') + price(a, 'fw')
    print(f'{a:3d} м²  стены {d(w):>8} ({a2(w/a):>6} за м²)   полы {d(f):>8} ({a2(f/a):>6} за м²)')
