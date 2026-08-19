#!/usr/bin/env python3
# Памятка: цены на материал за м². Продаём микроцемент, работы не выполняем.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from costs import cost, WALL, FLOOR

SC = os.environ.get('SC', '/tmp/kp')
RATE = 2.9133
VAT, PROFIT_TAX = 0.20, 0.20

MIN_M2 = 20
D_FROM, D_TO = 35, 100
PRICE = {'стены': dict(hi=40, lo=34), 'полы': dict(hi=50, lo=45)}
# Работа дешевеет вдвое медленнее материала: материал −15% и −10%,
# работа −7,5% и −5%. Ставку бригадам диктуем сами.
WORK = {'стены': dict(hi=24, lo=22), 'полы': dict(hi=25, lo=23.50)}
MAT = {'стены': cost(WALL), 'полы': cost(FLOOR)}


def curve(a, s):
    a = max(a, MIN_M2)
    if a <= D_FROM: return float(s['hi'])
    if a >= D_TO:   return float(s['lo'])
    return s['hi'] - (s['hi'] - s['lo']) * (a - D_FROM) / (D_TO - D_FROM)


def rate(a, k):  return curve(a, PRICE[k])
def work(a, k):  return curve(a, WORK[k])
def turnkey(a, k): return rate(a, k) + work(a, k)
def total(a, k): return max(a, MIN_M2) * turnkey(a, k)
def net(p, k):   return (p - MAT[k]) / (1 + VAT) * (1 - PROFIT_TAX)

def a2(v):  return f'{v:.2f}'.replace('.', ',')
def d(v):   return '$' + f'{v:,.0f}'.replace(',', ' ')
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

# ── основная таблица ──────────────────────────────────────────────────────
AREAS = [20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 120, 150, 200, 300]
rows = ''
for a in AREAS:
    mark = BEIGE if a in (35, 120) else BEIGE
    cells = td(f'<b>{a} м²</b>', TDN, mark)
    for k, bg in (('стены', GREEN), ('полы', AMBER)):
        cells += (td(f'${a2(rate(a, k))}', TDN, bg) + td(f'${a2(work(a, k))}', TDN, bg)
                  + td(f'${a2(turnkey(a, k))}', TDN + BIG, bg) + td(byn(total(a, k)), TDN, bg))
    rows += f'<tr>{cells}</tr>'

table = (f'<table style="{TBL}"><tr>'
         f'<th rowspan="2" style="{TH};background:{DARK};color:#fff">Площадь</th>'
         f'<th colspan="4" style="{TH};background:#5a7236;color:#fff">Стены</th>'
         f'<th colspan="4" style="{TH};background:#a07a32;color:#fff">Полы</th></tr><tr>'
         + ''.join(th(t, '#3d4a2e', '#cfe0a8') for t in
                   ('Материал', 'Работа', 'Под ключ за м²', 'Всего руб'))
         + ''.join(th(t, '#4a3a1f', '#e8c88a') for t in
                   ('Материал', 'Работа', 'Под ключ за м²', 'Всего руб'))
         + f'</tr>{rows}</table>')

# ── внутренний блок: себестоимость и маржа ────────────────────────────────
mrows = ''
for k, bg in (('стены', GREEN), ('полы', AMBER)):
    hi, lo = PRICE[k]['hi'], PRICE[k]['lo']
    mrows += ('<tr>' + td(f'<b>{k.capitalize()}</b>', TD, BEIGE)
              + td(f'${a2(MAT[k])}', TDN, bg)
              + td(f'${hi} → ${lo}', TDN, bg)
              + td(f'${a2(hi - MAT[k])} → ${a2(lo - MAT[k])}', TDN, bg)
              + td(f'<b>${a2(net(hi, k))} → ${a2(net(lo, k))}</b>', TDN, bg)
              + td(f'×{hi / MAT[k]:.1f} → ×{lo / MAT[k]:.1f}', TDN, bg) + '</tr>')
margin_tbl = (f'<table style="{TBL}"><tr>'
              + th('') + th('Себестоимость', '#3d3d3d') + th('Цена за м²', '#3d3d3d')
              + th('Валовая маржа', '#3d3d3d') + th('Чистыми после налогов', '#3d3d3d')
              + th('Наценка', '#3d3d3d') + f'</tr>{mrows}</table>')

# ── расход и фасовки ──────────────────────────────────────────────────────
PACKS = [('BS 3000, связующее', '380 г', '280 г', '25 кг', '65,8 м² стен · 89,3 м² полов'),
         ('Смола, грунт-слой', '—', '700 г', '30 кг', '42,9 м² полов'),
         ('Лак PUR Aqua 500', '100 г', '—', '10 кг', '100 м² стен'),
         ('Лак PUR TX', '—', '100 г', '10 кг', '100 м² полов'),
         ('Песок кварцевый 0,4–0,6', '168 г', '168 г', '25 кг', '148,8 м²'),
         ('Мука кварцевая', '112 г', '112 г', '25 кг', '223,2 м²'),
         ('<b>Итого на м²</b>', '<b>760 г</b>', '<b>1360 г</b>', '', '')]

prows = ''
for name, w, f, pack, cov in PACKS:
    prows += ('<tr>' + td(name, TD, BEIGE) + td(w, TDN, GREEN) + td(f, TDN, AMBER)
              + td(pack, TDN) + td(cov, TD + ';text-align:center') + '</tr>')
packs_tbl = (f'<table style="{TBL}"><tr>' + th('Компонент') + th('Стены, г/м²', '#3d4a2e', '#cfe0a8')
             + th('Полы, г/м²', '#4a3a1f', '#e8c88a') + th('Фасовка') + th('Хватает на')
             + f'</tr>{prows}</table>')

EXTRA = [('Двери', 'по площади полотна, обе стороны и торцы'),
         ('Откосы, ниши, бортики', 'вся развёрнутая площадь, без вычетов'),
         ('Мебель, столешницы', 'плоскости по площади, кромка по 0,1 м² за пог. м'),
         ('Запас на подрезку и бой', 'плюс 5% к расчётной площади'),
         ('Минимальный объект', '20 м² — меньше считаем как 20'),
         ('Оплата', 'рубли по курсу НБ РБ на день оплаты')]

def two_col(items, bg):
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    out = ''
    for i in range(half):
        l = left[i]; r = right[i] if i < len(right) else ('', '')
        out += ('<tr>' + td(l[0], TD, bg) + td(f'<b>{l[1]}</b>', TD + ';text-align:right', BEIGE)
                + td(r[0], TD, bg) + td(f'<b>{r[1]}</b>' if r[1] else '', TD + ';text-align:right', BEIGE) + '</tr>')
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
    <div style="font-weight:600;color:#2c2c2c;font-size:11px">Цены под ключ</div>
    <div style="margin-top:2px">внутренний документ · август 2026</div></div>
</div>

<h3 style="{H3}">1 · Как складывается цена</h3>
<div style="display:flex;gap:8px;margin-bottom:9px">
  <div style="flex:1;padding:7px 11px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">до 20 м²</div>
    Минимальная поставка. Считаем как <b>20 м²</b>, сколько бы ни было по факту:
    замес, фасовка и доставка одинаковы хоть на 8 м², хоть на 20.
  </div>
  <div style="flex:1;padding:7px 11px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">20–35 м²</div>
    Базовая цена без скидки: <b>$64</b> стены, <b>$75</b> полы под ключ.
    На таком объёме экономии не возникает, и мы это говорим прямо.
  </div>
  <div style="flex:1;padding:7px 11px;background:{DARK};color:#efece7;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#b8965a;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">35–100 м²</div>
    Скидка растёт плавно, без ступеней. К 100 м² под ключ доходит до
    <b style="color:#b8965a">$56</b> по стенам и <b style="color:#b8965a">$68,50</b> по полам.
  </div>
  <div style="flex:1;padding:7px 11px;background:{BEIGE};border:1px solid #e3d7bd;border-radius:5px;font-size:8.6px;line-height:1.45">
    <div style="color:#8a7346;letter-spacing:1.6px;text-transform:uppercase;font-size:7.6px;font-weight:700;margin-bottom:3px">100 м² и выше</div>
    Дальше цена не падает. <b>$56 и $68,50 — дно</b>, ниже начинается
    работа в убыток. Отдельного резерва торга нет.
  </div>
</div>
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-4px 0 10px">
<b style="color:#2c2c2c">Формула для любой площади S от 35 до 100 м²:</b>
материал стен = 40 − 6 × (S − 35) ÷ 65 · материал полов = 50 − 5 × (S − 35) ÷ 65 ·
работа стен = 24 − 2 × (S − 35) ÷ 65 · работа полов = 25 − 1,5 × (S − 35) ÷ 65.<br>
<b style="color:#2c2c2c">Работа дешевеет вдвое медленнее материала:</b> материал теряет 15% и 10%, работа — 7,5% и 5%.
В материале наценка тройная, там есть откуда давать; в работе — часы бригады, ставку которым диктуем мы.
</div>

<h3 style="{H3}">2 · Таблица</h3>
{table}
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-4px 0 10px">
Рубли по курсу НБ РБ {a2(RATE)} BYN/USD, пересчитывать на день оплаты.
Промежуточные площади берите на глаз между строками или считайте по формуле — кривая ровная, без переломов.
</div>

<h3 style="{H3}">3 · Как считается объём и что входит</h3>
{two_col(EXTRA, GREEN)}

<h3 style="{H3}">4 · Расход и фасовки</h3>
{packs_tbl}
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-4px 0 10px">
Узкое место партии — лак: ведро 10 кг закрывает ровно 100 м², а двухкомпонентный состав после смешивания
живёт часы и между заказами не дробится. Поэтому <b style="color:#2c2c2c">базовый комплект — 100 м², дальше кратно</b>.
</div>

<h3 style="{H3}">5 · Себестоимость материала и маржа — не отдавать</h3>
{margin_tbl}
<div style="font-size:8.2px;color:#666;line-height:1.45;margin:-4px 0 10px">
Себестоимость — фактическая рецептура по нашим закупочным ценам. Чистая маржа посчитана после НДС 20%
и налога на прибыль 20%, но до логистики, аренды и рекламы. <b style="color:#2c2c2c">Здесь только материал.</b>
Маржа по работе — это ставка клиенту минус ставка бригаде, и считается отдельно.
</div>

<div style="margin-top:auto;padding-top:7px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:8.5px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Внутренний документ — клиенту не отдаём</div>
</div>

</div></body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/memo-material.html', 'w').write(html)
print(f'себестоимость: стены ${MAT["стены"]:.2f}  полы ${MAT["полы"]:.2f}\n')
for a in (20, 35, 50, 80, 100, 120, 200):
    print(f'{a:3d} м²  стены ${a2(rate(a, "стены")):>6}/м²  {d(total(a, "стены")):>8}  '
          f'{byn(total(a, "стены")):>7} руб   |   полы ${a2(rate(a, "полы")):>6}/м²  '
          f'{d(total(a, "полы")):>8}  {byn(total(a, "полы")):>7} руб')
