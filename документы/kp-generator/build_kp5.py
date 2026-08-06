#!/usr/bin/env python3
# КП Евгений — на ОРИГИНАЛЬНОМ шаблоне калькулятора сайта (buildPdfHtml) + скидка по объёму как в «Миля»
import openpyxl

SC = '/tmp/claude-0/-home-user-romanovdecor-site/22c3148d-250b-5717-947a-9e939509d679/scratchpad'
wb = openpyxl.load_workbook(SC + '/kp/замеры-Евгений-v2.xlsx', data_only=True)
rows_x = list(wb.active.iter_rows(values_only=True))
def num(v): return isinstance(v, (int, float))

MW0, WW0 = 40, 24
MW,  WW  = 40, 24          # в таблице считаем по базовым ценам
MW_DISC  = 31              # цена материала стен со скидкой за объём
MF_DISC  = 45              # цена материала полов со скидкой за объём
MF,  WF  = 50, 25
RATE = 2.9133

def split(pairs):
    mat = sq = lin = 0.0
    for w, h in pairs:
        mat += w * h
        if min(w, h) < 0.5: lin += max(w, h)
        else: sq += w * h
    return mat, sq, lin

s1  = split([(r[0], r[1])  for r in rows_x[1:32] if num(r[0])  and num(r[1])])
s2  = split([(r[3], r[4])  for r in rows_x[1:17] if num(r[3])  and num(r[4])])
kor = split([(r[6], r[7])  for r in rows_x[1:10] if num(r[6])  and num(r[7])])
lst = split([(r[9], r[10]) for r in rows_x[1:]   if num(r[9])  and num(r[10])])
top = split([(r[12], r[13]) for r in rows_x[1:]  if len(r) > 13 and num(r[12]) and num(r[13])])
DOORS = [(0.9, 2.6, 1, 'с/у 1'), (0.9, 2.7, 1, 'с/у 2'), (0.8, 2.7, 3, 'коридор')]
doors_area = sum(w*h*n for w, h, n, _ in DOORS)

def u(v):  # $1 234,56 без хвоста ,00
    s = f'{v:,.2f}'.replace(',', ' ').replace('.', ',')
    return '$' + (s[:-3] if s.endswith(',00') else s)
def a2(v): return f'{v:.2f}'.replace('.', ',')
def pf(v):  # цена: целое без нулей, дробное — с копейками
    return f'{v:g}'.replace('.', ',') if v == int(v) else a2(v)

# === СТИЛИ: единая бежевая сетка 1px по всем строкам и колонкам ===
B = '#cbbf9f'
GRID = f'border:1px solid {B}'
# единая типографика: заголовки 9px, тело 10px, зоны 8.5px
NUM  = 'font-variant-numeric:tabular-nums'
CELL = f'padding:5.5px 6px;{GRID};vertical-align:middle;font-size:10px;line-height:1.25;height:19px'
THB  = f'{GRID};font-size:9px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:5px 6px;vertical-align:middle;text-align:center'
THS  = f'{GRID};font-weight:500;letter-spacing:1px;font-size:9px;padding:4px 6px;vertical-align:middle;text-align:center'
STY = dict(
 th_top_mat=f'background:#5a7236;color:#fff;{THB};text-align:center',
 th_top_work=f'background:#a07a32;color:#fff;{THB};text-align:center',
 th_top_tot=f'background:#1f1b14;color:#b8965a;{THB}',
 th_top_name=f'background:#2c2c2c;color:#fff;{GRID};padding:5px 10px;text-align:center;font-weight:600;letter-spacing:2px;text-transform:uppercase;font-size:9px;vertical-align:middle',
 th_sub_mat=f'background:#3d4a2e;color:#cfe0a8;{THS}',
 th_sub_work=f'background:#4a3a1f;color:#e8c88a;{THS}',
 td_name=f'{CELL};padding-left:10px;background:#f5efe2',
 td_mat=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#f0f5e0',
 td_matp=f'{CELL};{NUM};text-align:center;white-space:nowrap;background:#f0f5e0',
 td_mat2=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#f0f5e0',
 td_work=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#fdeed2',
 td_workp=f'{CELL};{NUM};text-align:center;white-space:nowrap;background:#fdeed2',
 td_work2=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#fdeed2',
 td_tot=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#f5efe2;font-weight:700;color:#2c2c2c',
)
ZONE_TD = f'background:#2c2c2c;color:#b8965a;font-weight:600;letter-spacing:2px;text-transform:uppercase;font-size:8.5px;padding:4.2px 10px;border:1px solid {B}'
SUBB = f'{GRID};{NUM};font-weight:700;font-size:10px;padding:5.5px 6px;text-align:right;white-space:nowrap;height:19px;vertical-align:middle'
SUB_TD_NAME = f'background:#eae0cb;{GRID};font-weight:700;font-size:10px;color:#3a3a3a;padding:5.5px 10px;vertical-align:middle'
SUB_TD_MAT = f'background:#e2ecc8;color:#3a4a1c;{SUBB}'
SUB_TD_WORK = f'background:#f8ddb0;color:#6a4a14;{SUBB}'
SUB_TD_TOT = f'background:#eae0cb;color:#7a5614;{SUBB}'
BADGE = 'display:inline-block;font-size:9px;letter-spacing:1px;padding:2px 6px;border-radius:3px;margin-right:6px;background:#e8e8f0;color:#4a4a7a'
STRIKE = 'text-decoration:line-through;color:#999;font-size:9px'
NEWP = 'color:#c0392b;font-weight:700'
OLDSUM = 'display:block;font-size:8px;color:#999;text-decoration:line-through;font-weight:400'

def zone(label):
    return f'<tr><td colspan="8" style="{ZONE_TD}">{label}</td></tr>'

def row(name, mObj, mPr, mSum, wObj, wPr, wSum, tot):
    return (f'<tr><td style="{STY["td_name"]}">{name}</td>'
            f'<td style="{STY["td_mat"]}">{mObj}</td>'
            f'<td style="{STY["td_matp"]}">{mPr}</td>'
            f'<td style="{STY["td_mat2"]}">{mSum}</td>'
            f'<td style="{STY["td_work"]}">{wObj}</td>'
            f'<td style="{STY["td_workp"]}">{wPr}</td>'
            f'<td style="{STY["td_work2"]}">{wSum}</td>'
            f'<td style="{STY["td_tot"]}">{tot}</td></tr>')

def sub(name, mObj, mPr, mSum, wObj, wPr, wSum, tot):
    return (f'<tr><td style="{SUB_TD_NAME}">{name}</td>'
            f'<td style="{SUB_TD_MAT}">{mObj}</td>'
            f'<td style="{SUB_TD_MAT};text-align:center">{mPr}</td>'
            f'<td style="{SUB_TD_MAT}">{mSum}</td>'
            f'<td style="{SUB_TD_WORK}">{wObj}</td>'
            f'<td style="{SUB_TD_WORK};text-align:center">{wPr}</td>'
            f'<td style="{SUB_TD_WORK}">{wSum}</td>'
            f'<td style="{SUB_TD_TOT}">{tot}</td></tr>')

TM = TW = TM0 = TW0 = 0.0
rowsHtml = ''

def price2(new, old):
    return new
def obj_work(sq, lin):
    parts = []
    if sq: parts.append(f'{a2(sq)} м²')
    if lin: parts.append(f'{a2(lin)} м.п.<sup>*</sup>')
    return ' + '.join(parts)
def wsum(v, v0):
    return u(v)

walls_m2 = s1[0] + s2[0] + kor[0] + 18 + doors_area

zM = zW = zM0 = zW0 = zMm2 = zSq = zLin = zDoors = 0.0
def zreset():
    global zM, zW, zM0, zW0, zMm2, zSq, zLin, zDoors
    zM = zW = zM0 = zW0 = zMm2 = zSq = zLin = zDoors = 0.0

def wall_price_row(name, m2, sq, lin, mult=1.0):
    global TM, TW, TM0, TW0, zM, zW, zM0, zW0, zMm2, zSq, zLin, rowsHtml
    m, m0 = m2*MW, m2*MW0
    r, r0 = WW*mult, WW0*mult
    w, w0 = (sq+lin)*r, (sq+lin)*r0
    TM += m; TW += w; TM0 += m0; TW0 += w0
    zM += m; zW += w; zM0 += m0; zW0 += w0; zMm2 += m2; zSq += sq; zLin += lin
    rowsHtml += row(name, f'{a2(m2)} м²', f'${MW}', wsum(m, m0),
                    obj_work(sq, lin), f'${pf(r)}', wsum(w, w0), u(m+w))

def floor_price_row(name, m2, sq, lin, mult=1.0):
    global TM, TW, TM0, TW0, zM, zW, zM0, zW0, zMm2, zSq, zLin, rowsHtml
    m = m2*MF; r = WF*mult
    w = (sq+lin)*r
    TM += m; TW += w; TM0 += m; TW0 += w
    zM += m; zW += w; zM0 += m; zW0 += w; zMm2 += m2; zSq += sq; zLin += lin
    rowsHtml += row(name, f'{a2(m2)} м²', f'${MF}', u(m),
                    obj_work(sq, lin), f'${pf(r)}', u(w), u(m+w))

def door_row(name, area, n):
    global TM, TW, TM0, TW0, zM, zW, zM0, zW0, zMm2, zDoors, rowsHtml
    dm, dm0 = area*MW, area*MW0
    TM += dm; TW += 100*n; TM0 += dm0; TW0 += 100*n
    zM += dm; zW += 100*n; zM0 += dm0; zW0 += 100*n; zMm2 += area; zDoors += n
    rowsHtml += row(name, f'{a2(area)} м²', f'${MW}', wsum(dm, dm0),
                    f'{n} шт', '$100', u(100*n), u(dm+100*n))

def fix_row(name, amount, mat='—', mat_sum='—'):
    global TW, TW0, zW, zW0, rowsHtml
    TW += amount; TW0 += amount
    zW += amount; zW0 += amount
    rowsHtml += row(name, '—', mat, mat_sum, '—', 'фикс', u(amount), u(amount))

def zone_total(label):
    global rowsHtml
    parts = []
    if zSq: parts.append(f'{a2(zSq)} м²')
    if zLin: parts.append(f'{a2(zLin)} м.п.')
    if zDoors: parts.append(f'{int(zDoors)} дв.')
    wobj = ' + '.join(parts) if parts else '—'
    msum = wsum(zM, zM0) if zM0 > zM else u(zM)
    wsum_ = wsum(zW, zW0) if zW0 > zW else u(zW)
    rowsHtml += sub(f'Итого {label}', f'{a2(zMm2)} м²', '', msum, wobj, '', wsum_, u(zM+zW))
    zreset()

rowsHtml += zone('Санузел 1')
floor_price_row('Пол', 10, 10, 0)
wall_price_row('Стены', s1[0], s1[1], s1[2])
wall_price_row('Потолок', 10, 10, 0, 1.2)
door_row('Дверь', 0.9*2.6, 1)
fix_row('Трап', 200, 'по факту', 'по факту')
zone_total('Санузел 1')

rowsHtml += zone('Санузел 2')
floor_price_row('Пол', 8, 8, 0)
wall_price_row('Стены', s2[0], s2[1], s2[2])
wall_price_row('Потолок', 8, 8, 0, 1.2)
door_row('Дверь', 0.9*2.7, 1)
zone_total('Санузел 2')

rowsHtml += zone('Коридор')
wall_price_row('Стены', kor[0], kor[1], kor[2])
door_row('Двери', 3*0.8*2.7, 3)
zone_total('Коридор')

rowsHtml += zone('Лестница')
floor_price_row('Лестница', lst[0], lst[1], lst[2], 1.2)
zone_total('Лестница')

rowsHtml += zone('Гостиная')
floor_price_row('Пол', 108, 108, 0)
floor_price_row('Столешница-остров', top[0], top[1], top[2])
zone_total('Гостиная')

rowsHtml += zone('Прочее')
fix_row('Гидроизоляция', 100)
zreset()

fl_m2 = 18 + 108 + lst[0] + top[0]
TOT0 = TM + TW
ECON = walls_m2 * (MW - MW_DISC) + fl_m2 * (MF - MF_DISC)   # скидка только на материал
TOT  = TOT0 - ECON
tot_m2 = walls_m2 + fl_m2
rowsHtml += sub('Всего по проекту', f'{a2(tot_m2)} м²', '', u(TM), '—', '', u(TW), u(TOT0))

logoSvg = ('<svg width="44" height="44" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
           '<rect width="32" height="32" rx="6" fill="#2c2c2c"/>'
           '<text x="50%" y="54%" font-family="Geologica,Arial,sans-serif" font-size="20" font-weight="700" fill="#b8965a" text-anchor="middle" dominant-baseline="middle">r</text></svg>')

byn = lambda v: f'{round(v*RATE):,}'.replace(',', ' ')

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:210mm}}</style></head><body>
<div style="width:100%;min-height:1123px;padding:14px 32px 12px 32px;background:#fff;color:#2c2c2c;font-family:Geologica,Arial,sans-serif;box-sizing:border-box;display:flex;flex-direction:column">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;border-bottom:2px solid #b8965a;padding-bottom:5px">
  <div style="display:flex;align-items:center;gap:10px">{logoSvg}
    <div><div style="font-size:16px;letter-spacing:2px;font-weight:500;text-transform:lowercase;line-height:1.1">romanov <span style="color:#b8965a">decor</span> studio</div>
    <div style="font-size:9px;color:#888;margin-top:3px;letter-spacing:1px;text-transform:uppercase">микроцемент на немецких компонентах</div></div>
  </div>
  <div style="text-align:right;font-size:10px;color:#666;letter-spacing:1px">
    <div>3 августа 2026 г.</div>
    <div style="margin-top:2px;font-weight:600;color:#2c2c2c">КП № 03082026</div>
    <div style="margin-top:4px"><span style="display:inline-block;background:#f5efe2;color:#8a6a2a;border:1px solid #d9c9a5;font-weight:600;font-size:8px;letter-spacing:1.2px;padding:3px 8px;border-radius:4px">СПЕЦИАЛЬНАЯ ЦЕНА ПО ОБЪЁМУ</span></div>
  </div>
</div>

<div style="font-size:16px;font-weight:600;letter-spacing:2px;margin:9px 0 7px;color:#2c2c2c">Коммерческое предложение</div>
<div style="display:flex;gap:10px;margin-bottom:6px">
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#faf6ef;border:1px solid #ece2d2">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Заказчик</div>
    <div><b>ФИО:</b> Евгений ________________</div>
    <div><b>Телефон:</b> ________________</div>
    <div><b>Адрес объекта:</b> ________________________________</div>
    <div><b>Площадь по материалам:</b> 313,15 м²</div>
  </div>
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#2c2c2c;color:#efece7">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Исполнитель</div>
    <div><b>Romanov Decor Studio</b></div>
    <div>________________ — менеджер проекта</div>
    <div>+375 (33) 628-04-86</div>
    <div style="color:#a09a92">info@romanovdecor.by · romanovdecor.by</div>
  </div>
</div>

<h3 style="font-size:10px;letter-spacing:3px;text-transform:uppercase;margin:9px 0 4px;color:#b8965a;font-weight:600">Спецификация материалов и работ</h3>
<table style="width:100%;border-collapse:collapse;font-size:10px">
<colgroup><col style="width:21%"><col style="width:8.5%"><col style="width:10.5%"><col style="width:10%"><col style="width:15%"><col style="width:10.5%"><col style="width:10%"><col style="width:14.5%"></colgroup>
<thead>
<tr><th rowspan="2" style="{STY['th_top_name']}">Наименование</th><th colspan="3" style="{STY['th_top_mat']}">Материалы</th><th colspan="3" style="{STY['th_top_work']}">Работы</th><th rowspan="2" style="{STY['th_top_tot']}">Итого, $</th></tr>
<tr><th style="{STY['th_sub_mat']}">Объём</th><th style="{STY['th_sub_mat']};white-space:nowrap">Цена за м²</th><th style="{STY['th_sub_mat']}">Сумма, $</th><th style="{STY['th_sub_work']}">Объём</th><th style="{STY['th_sub_work']};white-space:nowrap">Цена за м²</th><th style="{STY['th_sub_work']}">Сумма, $</th></tr>
</thead>
<tbody>{rowsHtml}</tbody>

</table>

<div style="text-align:right;margin:7px 0 0;font-size:10px;color:#2c2c2c;letter-spacing:1px">Скидка на материал <b style="color:#c0392b">{u(ECON)}</b></div>
<div style="text-align:right;margin:3px 0 0;letter-spacing:1px"><span style="font-size:11px;font-weight:600;color:#2c2c2c">ИТОГО К ОПЛАТЕ:</span> <span style="font-size:17px;font-weight:700;color:#b8965a">{u(TOT)}</span></div>
<div style="text-align:right;font-size:9px;color:#888;letter-spacing:1px;margin:3px 0 0">≈ {byn(TOT)} руб по курсу НБ РБ {a2(RATE)} BYN/USD на день оплаты</div>

<div style="margin-top:5px;padding:5px 12px;background:#f7f5f0;border-left:2px solid #b8965a;border-radius:3px;font-size:8.2px;color:#666;line-height:1.35">
<b style="color:#2c2c2c"><sup>*</sup> м.п.</b> — погонные метры: поверхности со стороной менее 0,5 м (откосы, ниши, бортики, подступенки) нормируются по длине, так как нанесение на них идёт медленнее, чем на сплошной стене.<br>
<b style="color:#2c2c2c">Цена:</b> в таблице всё по базовым ценам. За объём действует скидка на материал: стены $31 вместо $40, полы $45 вместо $50. На работы скидка не распространяется, потолки и лестница — работа +20%.<br>
<b style="color:#2c2c2c">Условия:</b> микроцемент на немецких компонентах, толщина 1–1,5 мм, эффекты Vintage / Natural / Metallic на выбор. Грунт + 1–2 слоя микроцемента + 2 слоя лака Remmers PUR Top TX. Оплата в белорусских рублях по курсу НБ РБ на день оплаты. <b>Срок действия КП — 14 дней.</b>
</div>

<div style="margin-top:auto;padding-top:8px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Спасибо за доверие!</div>
</div>

</div></body></html>'''

open(SC + '/kp/kp-evgeniy5.html', 'w').write(html)
print('База:', u(TOT0), '| Со скидкой:', u(TOT), '| Экономия:', u(ECON))
