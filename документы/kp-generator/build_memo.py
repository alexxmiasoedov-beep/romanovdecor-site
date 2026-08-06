#!/usr/bin/env python3
# Памятка по ценам Romanov Decor Studio — A4, фирменный стиль КП
SC = '/tmp/claude-0/-home-user-romanovdecor-site/22c3148d-250b-5717-947a-9e939509d679/scratchpad'

PKG = {'wm': 800, 'ww': 500, 'fm': 1000, 'fw': 500}
BANDS = [(20, 45), (45, 80), (80, 10**9)]
R = {'wm': [40, 38, 36], 'fm': [50, 48, 46],
     'ww': [24, 22, 20], 'fw': [25, 23, 21]}

def price(a, k):
    if a <= 20: return PKG[k]
    return PKG[k] + sum(max(0.0, min(a, hi) - lo) * r for (lo, hi), r in zip(BANDS, R[k]))

def a2(v): return f'{v:.2f}'.replace('.', ',')

B    = '#cbbf9f'
GRID = f'border:1px solid {B}'
TD   = f'{GRID};padding:3.4px 7px;font-size:9px;line-height:1.25;vertical-align:middle'
TDN  = f'{TD};text-align:center;white-space:nowrap;font-variant-numeric:tabular-nums'
TH   = f'{GRID};padding:4px 7px;font-size:8px;letter-spacing:1.4px;text-transform:uppercase;font-weight:700;text-align:center;vertical-align:middle'
H3   = 'font-size:9px;letter-spacing:2.4px;text-transform:uppercase;margin:0 0 5px;color:#b8965a;font-weight:600'
TBL  = 'width:100%;border-collapse:collapse;margin-bottom:11px'
GREEN, AMBER, BEIGE, DARK = '#f0f5e0', '#fdeed2', '#f5efe2', '#2c2c2c'

def th(txt, bg=DARK, color='#fff', extra=''):
    return f'<th style="{TH};background:{bg};color:{color};{extra}">{txt}</th>'
def td(txt, style=TD, bg=None, extra=''):
    return f'<td style="{style}{";background:"+bg if bg else ""};{extra}">{txt}</td>'

# ---------- 1. Базовые цены ----------
base_rows = ''
for name, mat, work, cost in (('Стены, потолки, двери', 40, 24, 15), ('Полы, лестницы, столешницы', 50, 25, 25)):
    base_rows += ('<tr>' + td(name, TD, BEIGE) + td(f'${mat}', TDN, GREEN) + td(f'${work}', TDN, AMBER)
                  + td(f'<b>${mat+work}</b>', TDN, BEIGE) + td(f'${cost}', TDN) + td(f'<b>${mat-cost}</b>', TDN) + '</tr>')
base = f'''<table style="{TBL}">
<tr>{th('Поверхность','#2c2c2c')}{th('Материал','#5a7236')}{th('Работа','#a07a32')}{th('Под ключ','#1f1b14','#b8965a')}{th('Себестоимость','#4a4a4a')}{th('Маржа с м²','#4a4a4a')}</tr>
{base_rows}</table>'''

# ---------- 2. Шкала по объёму ----------
scale_rows = ''
for label, km, kw, pkg, bg in (('Стены', 'wm', 'ww', 1300, GREEN), ('Полы', 'fm', 'fw', 1500, AMBER)):
    cells = ''.join(td(f'${R[km][i]} + ${R[kw][i]}<br><b>${R[km][i]+R[kw][i]}</b>', TDN, bg) for i in range(3))
    scale_rows += ('<tr>' + td(f'<b>{label}</b>', TD, BEIGE) + td(f'<b>${pkg:,}</b><br>пакетом'.replace(',',' '), TDN, BEIGE) + cells + '</tr>')
scale = f'''<table style="{TBL}">
<tr>{th('','#2c2c2c')}{th('0–20 м²','#1f1b14','#b8965a')}{th('21–45 м²','#2c2c2c')}{th('46–80 м²','#2c2c2c')}{th('81 м² и выше','#2c2c2c')}</tr>
{scale_rows}</table>'''

# ---------- 3. Эффективные ставки ----------
eff_rows = ''
for a in (30, 60, 100, 150, 200, 300):
    eff_rows += ('<tr>' + td(f'{a} м²', TDN, BEIGE)
                 + td(f'${a2(price(a,"wm")/a)}', TDN, GREEN) + td(f'${a2(price(a,"ww")/a)}', TDN, AMBER)
                 + td(f'${a2(price(a,"fm")/a)}', TDN, GREEN) + td(f'${a2(price(a,"fw")/a)}', TDN, AMBER) + '</tr>')
eff = f'''<table style="{TBL}">
<tr>{th('Площадь','#2c2c2c')}{th('Материал стен','#5a7236')}{th('Работа стен','#a07a32')}{th('Материал полов','#5a7236')}{th('Работа полов','#a07a32')}</tr>
{eff_rows}</table>'''

# ---------- 4. Надбавки и фиксы ----------
extra_items = [('Потолки', 'работа +20%'), ('Лестница', 'работа +20%'),
               ('Дверь', '$100 / шт + материал по площади'),
               ('Гидроизоляционная лента', '$100')]
add_items = [('Примыкание стена/пол (без плинтуса)', '$3 / пог. м'),
             ('Примыкание с паркетом, ламинатом', '$10 / пог. м'),
             ('Примыкание с плиткой', '$7 / пог. м'),
             ('Ремонт трещин', '$5 / пог. м'),
             ('Уклон к трапу в одну сторону', '$200'),
             ('Конверт к трапу', '$300'),
             ('Герметизация трапа', '$50'),
             ('Уклон в котельной', '$200')]
def kv_table(items):
    rows = ''.join('<tr>' + td(k, TD, BEIGE) + td(f'<b>{v}</b>', f'{TD};text-align:right;white-space:nowrap', AMBER) + '</tr>' for k, v in items)
    return f'<table style="{TBL}">{rows}</table>'

# ---------- 8. Пример расчёта ----------
ex_rows = ''; total = 0
steps = [('Первые 20 м² — пакетом', 20, None, 1300)]
for (lo, hi), rm, rw in zip(BANDS, R['wm'], R['ww']):
    n = max(0.0, min(100, hi) - lo)
    if n > 0: steps.append((f'Метры с {int(lo)+1}-го по {int(min(100,hi))}-й', n, rm+rw, n*(rm+rw)))
for name, n, rate, sm in steps:
    total += sm
    ex_rows += ('<tr>' + td(name, TD, BEIGE) + td(f'{n:.0f} м²', TDN)
                + td(f'${rate}' if rate else '—', TDN, AMBER) + td(f'<b>${sm:,.0f}</b>'.replace(',', ' '), TDN, GREEN) + '</tr>')
ex_rows += ('<tr>' + td('<b>Итого 100 м²</b>', f'{TD};font-weight:700', '#eae0cb') + td('100 м²', TDN, '#eae0cb')
            + td(f'<b>${total/100:.2f}</b>'.replace('.', ','), TDN, '#eae0cb') + td(f'<b>${total:,.0f}</b>'.replace(',', ' '), TDN, '#eae0cb') + '</tr>')
ex_rows += ('<tr>' + td('Без скидки: 100 × $64', TD, BEIGE) + td('', TDN) + td('$64', TDN, AMBER)
            + td(f'$6 400 &nbsp;→&nbsp; <b style="color:#c0392b">экономия ${6400-total:,.0f}</b>'.replace(',', ' '), f'{TD};text-align:center;white-space:nowrap', GREEN) + '</tr>')
example = f'<table style="{TBL}"><tr>{th("Слой","#2c2c2c")}{th("Объём","#2c2c2c")}{th("Цена за м²","#a07a32")}{th("Сумма","#5a7236")}</tr>{ex_rows}</table>'

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:210mm}}</style></head><body>
<div style="width:100%;min-height:1123px;padding:14px 32px 12px;background:#fff;color:#2c2c2c;font-family:Geologica,Arial,sans-serif;display:flex;flex-direction:column">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;border-bottom:2px solid #b8965a;padding-bottom:6px">
  <div style="display:flex;align-items:center;gap:10px">
    <svg width="42" height="42" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" rx="6" fill="#2c2c2c"/><text x="50%" y="54%" font-family="Geologica,Arial,sans-serif" font-size="20" font-weight="700" fill="#b8965a" text-anchor="middle" dominant-baseline="middle">r</text></svg>
    <div><div style="font-size:15px;letter-spacing:2px;font-weight:500;text-transform:lowercase;line-height:1.1">romanov <span style="color:#b8965a">decor</span> studio</div>
    <div style="font-size:8px;color:#888;margin-top:3px;letter-spacing:1px;text-transform:uppercase">микроцемент на немецких компонентах</div></div>
  </div>
  <div style="text-align:right;font-size:9px;color:#666;letter-spacing:1px">
    <div style="font-size:14px;font-weight:600;color:#2c2c2c;letter-spacing:2px">ПАМЯТКА ПО ЦЕНАМ</div>
    <div style="margin-top:3px">внутренний документ · август 2026</div>
  </div>
</div>

<h3 style="{H3};margin-top:8px">1 · Базовые цены</h3>
{base}

<h3 style="{H3}">2 · Шкала по объёму — считается по слоям</h3>
{scale}
<div style="font-size:8.4px;color:#555;line-height:1.45;margin:-6px 0 11px;padding:6px 10px;background:#f7f5f0;border-left:2px solid #b8965a">
Первые 20 м² — пакетом. Метры с 21-го по 45-й — по базовой цене. С 46-го метра цена снижается, с 81-го действует нижняя ставка.
<b>Скидка достаётся только тем метрам, что выше порога</b>, — клиент не переезжает в дешёвую категорию целиком.
Цена никогда не падает при росте объёма: заказать 21 м² вместо 20 бессмысленно.
</div>

<h3 style="{H3}">3 · Эффективная цена за м² — для быстрой прикидки</h3>
{eff}

<div style="display:flex;gap:14px">
  <div style="flex:1">
    <h3 style="{H3}">4 · Надбавки и фиксы</h3>
    {kv_table(extra_items)}
    <h3 style="{H3}">6 · Как считается объём</h3>
    <div style="font-size:8.4px;color:#555;line-height:1.5;padding:7px 10px;background:#f7f5f0;border-left:2px solid #b8965a">
      <b style="color:#2c2c2c">Материал</b> — вся чистая площадь поверхности, без вычетов.<br>
      <b style="color:#2c2c2c">Работа</b> — стороны от 0,5 м считаются в м², стороны меньше 0,5 м — в погонных метрах по большей стороне (откосы, ниши, бортики, подступенки).
    </div>
  </div>
  <div style="flex:1">
    <h3 style="{H3}">5 · Дополнительные работы</h3>
    {kv_table(add_items)}
  </div>
</div>

<h3 style="{H3}">7 · Правило скидки</h3>
<div style="display:flex;gap:8px;margin-bottom:8px">
  <div style="flex:1;padding:7px 11px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.5">
    <div style="font-size:8px;letter-spacing:2px;text-transform:uppercase;color:#b8965a;font-weight:600;margin-bottom:3px">Прайс</div>
    Шкала выше — публичная цена. Печатается в КП и в калькуляторе. Даёт до 4% скидки на 100 м², до 8% на 200 м², до 10% на 300 м².
  </div>
  <div style="flex:1;padding:7px 11px;background:#2c2c2c;color:#efece7;border-radius:5px;font-size:8.6px;line-height:1.5">
    <div style="font-size:8px;letter-spacing:2px;text-transform:uppercase;color:#b8965a;font-weight:600;margin-bottom:3px">Резерв торга</div>
    Сверх прайса — только при встречном условии: клиент сравнивает с конкурентом, вносит предоплату сразу или даёт портфолийный объект.
    <b style="color:#e8c88a">Предел: $34–35 по стенам, $44–45 по полам.</b> Ниже — отказываемся от сделки.
  </div>
</div>

<div style="font-size:8.4px;color:#555;line-height:1.5;padding:7px 10px;background:#fdf4e6;border:1px solid #e3d7bd;border-radius:4px">
<b style="color:#2c2c2c">Почему скидка неглубокая.</b> Метраж задан квартирой — скидка не увеличит заказ, она лишь выигрывает сделку у конкурента.
Каждые 10% скидки требуют в полтора раза больше объектов, чтобы вернуть ту же прибыль. Маржа в деньгах одинакова по стенам и полам на каждой ступени: $25 → $23 → $21 с метра.
</div>

<h3 style="{H3};margin-top:11px">8 · Пример: 100 м² стен под ключ</h3>
{example}

<div style="margin-top:auto;padding-top:8px;border-top:1px solid #eee;display:flex;justify-content:space-between;font-size:8.5px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Курс НБ РБ 2,9133 BYN/USD</div>
</div>

</div></body></html>'''

open(SC + '/kp/memo.html', 'w').write(html)
print('ok')
