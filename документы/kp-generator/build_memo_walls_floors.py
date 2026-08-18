#!/usr/bin/env python3
# Памятка по ценам: стены и полы. Плавная скидка от 35 до 120 м².
import os
SC = os.environ.get('SC', '/tmp/kp')
RATE = 2.9133

MIN_M2 = 20          # минимальный объём к оплате
D_FROM, D_TO = 35, 120   # плавная скидка на этом отрезке
WALL = dict(mat_hi=40, mat_lo=34, work=24)   # -15% по материалу
FLOOR = dict(mat_hi=50, mat_lo=45, work=25)  # -10% по материалу

def mat(a, s):
    if a <= D_FROM: return s['mat_hi']
    if a >= D_TO:   return s['mat_lo']
    return s['mat_hi'] - (s['mat_hi'] - s['mat_lo']) * (a - D_FROM) / (D_TO - D_FROM)

def rate(a, s): return mat(a, s) + s['work']
def total(a, s): return max(a, MIN_M2) * rate(max(a, MIN_M2), s)

def a2(v): return f'{v:.2f}'.replace('.', ',')
def d(v):  return '$' + f'{v:,.0f}'.replace(',', ' ')
def byn(v): return f'{round(v * RATE):,}'.replace(',', ' ')

B = '#cbbf9f'; GRID = f'border:1px solid {B}'
TD  = f'{GRID};padding:2.6px 7px;font-size:9px;line-height:1.25;vertical-align:middle'
TDN = f'{TD};text-align:center;white-space:nowrap;font-variant-numeric:tabular-nums'
TH  = f'{GRID};padding:4px 7px;font-size:8px;letter-spacing:1.4px;text-transform:uppercase;font-weight:700;text-align:center;vertical-align:middle'
H3  = 'font-size:9px;letter-spacing:2.4px;text-transform:uppercase;margin:0 0 4px;color:#b8965a;font-weight:600'
TBL = 'width:100%;border-collapse:collapse;margin-bottom:9px'
GREEN, AMBER, BEIGE, DARK = '#f0f5e0', '#fdeed2', '#f5efe2', '#2c2c2c'
BIG = ';font-size:11px;font-weight:700'

def th(t, bg=DARK, c='#fff'): return f'<th style="{TH};background:{bg};color:{c}">{t}</th>'
def td(t, s=TD, bg=None):     return f'<td style="{s}{";background:"+bg if bg else ""}">{t}</td>'

# ── таблица ───────────────────────────────────────────────────────────────
AREAS = [20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 150, 200, 300]
rows = ''
for a in AREAS:
    w, f = total(a, WALL), total(a, FLOOR)
    wm, fm = mat(a, WALL), mat(a, FLOOR)
    mark = BEIGE if a in (35, 120) else None
    rows += ('<tr>'
        + td(f'<b>{a} м²</b>', TDN, mark or BEIGE)
        + td(f'${a2(rate(a, WALL))}', TDN + BIG, GREEN) + td(f'${a2(wm)}', TDN, GREEN) + td(d(w), TDN, GREEN) + td(byn(w), TDN, GREEN)
        + td(f'${a2(rate(a, FLOOR))}', TDN + BIG, AMBER) + td(f'${a2(fm)}', TDN, AMBER) + td(d(f), TDN, AMBER) + td(byn(f), TDN, AMBER)
        + '</tr>')
table = (f'<table style="{TBL}"><tr>'
         f'<th rowspan="2" style="{TH};background:{DARK};color:#fff">Площадь</th>'
         f'<th colspan="4" style="{TH};background:#5a7236;color:#fff">Стены</th>'
         f'<th colspan="4" style="{TH};background:#a07a32;color:#fff">Полы</th></tr><tr>'
         f'{th("Под ключ за м²","#3d4a2e","#cfe0a8")}{th("в т.ч. материал","#3d4a2e","#cfe0a8")}{th("Всего $","#3d4a2e","#cfe0a8")}{th("Всего руб","#3d4a2e","#cfe0a8")}'
         f'{th("Под ключ за м²","#4a3a1f","#e8c88a")}{th("в т.ч. материал","#4a3a1f","#e8c88a")}{th("Всего $","#4a3a1f","#e8c88a")}{th("Всего руб","#4a3a1f","#e8c88a")}'
         f'</tr>{rows}</table>')

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
    out = ''
    for i in range(half):
        l = left[i]; r = right[i] if i < len(right) else ('', '')
        out += ('<tr>' + td(l[0], TD, bg) + td(f'<b>{l[1]}</b>', TDN, BEIGE)
                + td(r[0], TD, bg) + td(f'<b>{r[1]}</b>' if r[1] else '', TDN, BEIGE) + '</tr>')
    return f'<table style="{TBL}">{out}</table>'

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

<h3 style="{H3}">1 · Как складывается цена</h3>
<div style="display:flex;gap:8px;margin-bottom:9px">
  <div style="flex:1;padding:7px 11px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">до 20 м²</div>
    Минимальный выезд. Считаем как <b>20 м²</b>, сколько бы ни было по факту.
    Бригада, замес и расходники одинаковы хоть на 8 м², хоть на 20.
  </div>
  <div style="flex:1;padding:7px 11px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">20–35 м²</div>
    Базовая цена без скидки: материал <b>$40</b> стены, <b>$50</b> полы.
    На таком объёме экономии не возникает, и мы это говорим прямо.
  </div>
  <div style="flex:1;padding:7px 11px;background:{DARK};color:#efece7;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#b8965a;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">35–120 м²</div>
    Скидка растёт плавно, без ступеней. К 120 м² материал доходит до
    <b style="color:#b8965a">$34</b> по стенам (−15%) и <b style="color:#b8965a">$45</b> по полам (−10%).
  </div>
  <div style="flex:1;padding:7px 11px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">120 м² и выше</div>
    Дальше цена не падает. Это дно: ниже начинается работа в убыток.
  </div>
</div>
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-4px 0 10px">
<b style="color:#2c2c2c">Работа скидке не подлежит</b> — $24 за м² по стенам и $25 по полам на любом объёме. Дешевеет только материал.<br>
<b style="color:#2c2c2c">Формула для любой площади S от 35 до 120 м²:</b>
материал стен = 40 − 6 × (S − 35) ÷ 85 · материал полов = 50 − 5 × (S − 35) ÷ 85.
</div>

<h3 style="{H3}">2 · Готовая таблица</h3>
{table}
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-4px 0 10px">
Цена под ключ — материал плюс работа. Рубли по курсу НБ РБ {a2(RATE)} BYN/USD, пересчитывать на день оплаты.
Промежуточные площади берите на глаз между строками или считайте по формуле выше — кривая ровная, без переломов.
</div>

<h3 style="{H3}">3 · Как считается объём</h3>
<div style="font-size:9px;line-height:1.5;padding:6px 12px;background:#faf6ef;border:1px solid #ece2d2;border-radius:5px;margin-bottom:10px">
<b>Материал</b> — вся чистая площадь поверхности, без вычетов.<br>
<b>Работа</b> — стороны от 0,5 м в квадратных метрах; стороны меньше 0,5 м — в погонных метрах по большей стороне.
Это откосы, ниши, бортики, подступенки: нанесение идёт медленнее, поэтому погонный метр там стоит как квадрат.
</div>

<h3 style="{H3}">4 · Надбавки и фиксы</h3>
{two_col(EXTRA, GREEN)}

<h3 style="{H3}">5 · Дополнительные работы по полам</h3>
{two_col(FLOOR_EXTRA, AMBER)}

<h3 style="{H3}">6 · Что дальше не отдаём</h3>
<div style="font-size:8.4px;line-height:1.5;padding:6px 12px;background:{DARK};color:#efece7;border-radius:5px;margin-bottom:9px">
Шкала выше — публичная цена, её печатаем в КП и в калькуляторе. <b style="color:#b8965a">Она уже отдаёт максимум: $34 по стенам и $45 по полам — это дно.</b>
Отдельного резерва торга сверх шкалы больше нет: на 120 м² и выше скидка уже выбрана целиком.
Если клиент давит дальше — торгуемся не ценой, а условиями: сроком, порядком оплаты, объёмом работ. Или отказываемся от сделки.
</div>

<div style="margin-top:auto;padding-top:7px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:8.5px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Внутренний документ — клиенту не отдаём</div>
</div>

</div></body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/memo-walls-floors.html', 'w').write(html)
for a in (20, 35, 50, 80, 100, 120, 200):
    print(f'{a:3d} м²  стены {a2(rate(a,WALL)):>6}/м² (мат {a2(mat(a,WALL)):>5}) {d(total(a,WALL)):>8}   '
          f'полы {a2(rate(a,FLOOR)):>6}/м² (мат {a2(mat(a,FLOOR)):>5}) {d(total(a,FLOOR)):>8}')
