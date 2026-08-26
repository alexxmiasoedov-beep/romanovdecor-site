#!/usr/bin/env python3
# КП — ул. Нововиленская, 61-217 (дизайн-проект Е. Варкович, лист 25).
# Микроцемент в двух мокрых зонах: душевая (микроцемент 1) и санузел
# (микроцемент 2). Объёмы сняты ПОСТЕНОЧНО с разверток листа 25 и
# согласованы с заказчиком стенка за стенкой (аудит 26.08.2026):
#  - поверхности шире 0,5 м — работа квадратами, ровно 0,50 м — тоже квадраты;
#  - уже 0,5 м — работа погонными метрами по длине;
#  - санузел: зоны за зеркалом, тумбами и навесным — считаются; короб
#    инсталляции (гипсокартон) отделывается микроцементом; МДФ-фасады
#    люков — тариф мебели (€17,50/м² + €9/м.п. кромки), материал фасадов
#    входит в общую квадратуру;
#  - душевая: крупное зеркало (32-23) и встроенные шкафы (белая штриховка)
#    не считаются; полосы 175 и 90 мм — покраска по проекту (не наши);
#    полоса 75 мм (28-29) — микроцемент, погонными;
#  - двери-невидимки: полотно отдельной позицией, откосы проёмов ~0,1 м.
import os

SC = os.environ.get('SC', '/tmp/kp')
RATE = 3.5185          # BYN/EUR, курс НБ РБ на 26.08.2026
KP_DATE = '26 августа 2026 г.'
KP_NUM = '260826A'

DOOR_RATE = 45                      # €/м² стороны полотна
DOOR_W, DOOR_H = 0.7, 2.2
DOOR_SIDE = DOOR_W * DOOR_H         # 1,54 м² сторона полотна
DOOR_WORK = DOOR_SIDE * DOOR_RATE   # € за сторону
MISC = 80                           # малярные расходники
FURN_M2, FURN_EDGE = 17.50, 9.0     # мебель: €/м² плоскости, €/м.п. кромки

MIN_M2 = 20
D_FROM, D_TO = 35, 100
MAT_HI, MAT_LO = 35, 30
WRK_HI, WRK_LO = 21, 18.50

def curve(a, hi, lo):
    if a <= D_FROM: return float(hi)
    if a >= D_TO:   return float(lo)
    return hi - (hi - lo) * (a - D_FROM) / (D_TO - D_FROM)

def u(v):
    s = f'{v:,.2f}'.replace(',', ' ').replace('.', ',')
    return '€' + (s[:-3] if s.endswith(',00') else s)
def a2(v): return f'{v:.2f}'.replace('.', ',')

# ── объёмы постеночно, лист 25 ───────────────────────────────────────────
# ДУШЕВАЯ (высота 2,665):
#   материал: стена 23-24 2,19 + стена у 32 (373+823) 3,20 +
#             за/под столешницей 32-23 1,60 + полоса 75 мм 0,20 + откосы 0,51
#   работа м²: слева от короба 0,50×2,665=1,33 + 3,20 + 1,60
#   работа м.п.: над дверью 0,80 + полоска 50 мм у короба 2,20 +
#                полоса 75 мм 2,67 + откосы 5,10
# САНУЗЕЛ (высота 2,625):
#   материал: 33-34 1,76 + 34-35 (вкл. за зеркалом/тумбой) 2,31 +
#             35-36 1,27 + 36-37 0,86 + короб инсталляции 0,93 +
#             38-33 3,46 + фасады МДФ 1,10 + откосы 0,51
#   работа м²: 33-34 справа 0,51×2,625=1,34 + 34-35 2,31 +
#              инсталляция 0,93 + 38-33 3,46
#   работа м.п.: полоска 50 мм 2,20 + над дверью 0,80 +
#                35-36 (485) 2,63 + 36-37 (330) 2,63 + откосы 5,10
ZONES = [
    # имя, материал м², работа-квадраты м², работа-погонные м.п.
    ('Душевая — стены и откосы',
     2.19 + 3.20 + 1.60 + 0.20 + 0.51,
     1.33 + 3.20 + 1.60,
     0.80 + 2.20 + 2.67 + 5.10),
    ('Санузел — стены, инсталляция, откосы',
     1.76 + 2.31 + 1.27 + 0.86 + 0.93 + 3.46 + 0.51,
     1.34 + 2.31 + 0.93 + 3.46,
     2.20 + 0.80 + 2.63 + 2.63 + 5.10),
]
FURN_AREA = 1.10        # МДФ-фасады люков инсталляции, 2×388×1425
FURN_MP = 7.25          # кромки фасадов, все стороны
ND = 2                  # дверей-невидимок (по полотну на комнату)

W_M2 = sum(z[1] for z in ZONES)
W_UN = sum(z[2] + z[3] for z in ZONES)
D_M2 = ND * DOOR_SIDE                 # полотна, одна сторона каждое
TOT_M2 = W_M2 + D_M2 + FURN_AREA

BILL_M2 = max(TOT_M2, MIN_M2)
EFF_MAT = curve(BILL_M2, MAT_HI, MAT_LO)
EFF_WRK = curve(BILL_M2, WRK_HI, WRK_LO)

# ── вёрстка (эталон build_kp_losika.py) ──────────────────────────────────
B = '#cbbf9f'; GRID = f'border:1px solid {B}'; NUM = 'font-variant-numeric:tabular-nums'
CELL = f'padding:5.5px 6px;{GRID};vertical-align:middle;font-size:10px;line-height:1.25;height:19px'
THB = f'{GRID};font-size:9px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:5px 6px;vertical-align:middle;text-align:center'
THS = f'{GRID};font-weight:500;letter-spacing:1px;font-size:9px;padding:4px 6px;vertical-align:middle;text-align:center'
STY = dict(
 th_top_mat=f'background:#5a7236;color:#fff;{THB}',
 th_top_work=f'background:#a07a32;color:#fff;{THB}',
 th_top_tot=f'background:#1f1b14;color:#b8965a;{THB}',
 th_top_name=f'background:#2c2c2c;color:#fff;{GRID};padding:5px 10px;text-align:center;font-weight:600;letter-spacing:2px;text-transform:uppercase;font-size:9px;vertical-align:middle',
 th_sub_mat=f'background:#3d4a2e;color:#cfe0a8;{THS}',
 th_sub_work=f'background:#4a3a1f;color:#e8c88a;{THS}',
 td_name=f'{CELL};padding-left:10px;background:#f5efe2',
 td_mat=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#f0f5e0',
 td_matp=f'{CELL};{NUM};text-align:center;white-space:nowrap;background:#f0f5e0',
 td_work=f'{CELL};{NUM};text-align:right;background:#fdeed2',
 td_workp=f'{CELL};{NUM};text-align:center;white-space:nowrap;background:#fdeed2',
 td_tot=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#f5efe2;font-weight:700;color:#2c2c2c')
SUBB = f'{GRID};{NUM};font-weight:700;font-size:10px;padding:5.5px 6px;text-align:right;white-space:nowrap;height:19px;vertical-align:middle'
S_NAME = f'background:#eae0cb;{GRID};font-weight:700;font-size:10px;color:#3a3a3a;padding:5.5px 10px;vertical-align:middle'
S_MAT = f'background:#e2ecc8;color:#3a4a1c;{SUBB}'
S_WORK = f'background:#f8ddb0;color:#6a4a14;{SUBB}'
S_TOT = f'background:#eae0cb;color:#7a5614;{SUBB}'

def row(n, a, b, c, d, e, f, g):
    return (f'<tr><td style="{STY["td_name"]}">{n}</td>'
            f'<td style="{STY["td_mat"]}">{a}</td><td style="{STY["td_matp"]}">{b}</td><td style="{STY["td_mat"]}">{c}</td>'
            f'<td style="{STY["td_work"]}">{d}</td><td style="{STY["td_workp"]}">{e}</td><td style="{STY["td_work"]}">{f}</td>'
            f'<td style="{STY["td_tot"]}">{g}</td></tr>')
def sub(n, a, c, d, f, g):
    return (f'<tr><td style="{S_NAME}">{n}</td>'
            f'<td style="{S_MAT}">{a}</td><td style="{S_MAT}"></td><td style="{S_MAT}">{c}</td>'
            f'<td style="{S_WORK}">{d}</td><td style="{S_WORK}"></td><td style="{S_WORK}">{f}</td>'
            f'<td style="{S_TOT}">{g}</td></tr>')

rows = ''
TM = TW = 0.0
for name, mat_m2, wide_m2, mp in ZONES:
    m = mat_m2 * EFF_MAT; w = (wide_m2 + mp) * EFF_WRK
    TM += m; TW += w
    vol = f'{a2(wide_m2)} м² + {a2(mp)} м.п.<sup>*</sup>'
    rows += row(name, f'{a2(mat_m2)} м²', u(EFF_MAT), u(m), vol, u(EFF_WRK), u(w), u(m + w))
rows += sub('Итого стены', f'{a2(W_M2)} м²', u(TM),
            f'{a2(sum(z[2] for z in ZONES))} м² + {a2(sum(z[3] for z in ZONES))} м.п.', u(TW), u(TM + TW))

fw = FURN_AREA * FURN_M2 + FURN_MP * FURN_EDGE
fm = FURN_AREA * EFF_MAT
TM += fm; TW += fw
rows += row('Фасады МДФ инсталляции (мебель)', f'{a2(FURN_AREA)} м²', u(EFF_MAT), u(fm),
            f'{a2(FURN_AREA)} м² + {a2(FURN_MP)} м.п. кромки',
            f'{u(FURN_M2)}+{u(FURN_EDGE)}', u(fw), u(fm + fw))

dm = D_M2 * EFF_MAT; dw = ND * DOOR_WORK
TM += dm; TW += dw
rows += row('Двери-невидимки 700×2200', f'{a2(D_M2)} м²', u(EFF_MAT), u(dm),
            f'{ND} стор.', u(DOOR_WORK), u(dw), u(dm + dw))
rows += sub('Итого двери и фасады', f'{a2(D_M2 + FURN_AREA)} м²', u(dm + fm), '—', u(dw + fw), u(dm + fm + dw + fw))

TM += MISC
rows += row('Малярные расходники, валики', 'компл.', '—', u(MISC), '—', '—', '—', u(MISC))

TOT = TM + TW
rows += sub('Всего по проекту', f'{a2(TOT_M2)} м²', u(TM), '—', u(TW), u(TOT))

byn = lambda v: f'{round(v * RATE):,}'.replace(',', ' ')
logo = ('<svg width="44" height="44" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="32" height="32" rx="6" fill="#2c2c2c"/>'
        '<path d="M 9.6 8 L 9.6 15.5 A 6.4 6.4 0 0 0 22.4 15.5 L 22.4 8" '
        'fill="none" stroke="#b8965a" stroke-width="4"/></svg>')

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:210mm}}</style></head><body>
<div style="width:100%;min-height:1123px;padding:14px 32px 12px;background:#fff;color:#2c2c2c;font-family:Geologica,Arial,sans-serif;display:flex;flex-direction:column">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;border-bottom:2px solid #b8965a;padding-bottom:5px">
  <div style="display:flex;align-items:center;gap:10px">{logo}
    <div><div style="font-size:16px;letter-spacing:3px;font-weight:600;line-height:1.1">UNI<span style="color:#b8965a">CORE</span></div>
    <div style="font-size:9px;color:#888;margin-top:3px;letter-spacing:1px;text-transform:uppercase">микроцемент</div></div>
  </div>
  <div style="text-align:right;font-size:10px;color:#666;letter-spacing:1px">
    <div>{KP_DATE}</div>
    <div style="margin-top:2px;font-weight:600;color:#2c2c2c">КП № {KP_NUM}</div>
  </div>
</div>

<div style="font-size:16px;font-weight:700;letter-spacing:2px;margin:9px 0 7px">Коммерческое предложение</div>
<div style="display:flex;gap:10px;margin-bottom:6px">
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#faf6ef;border:1px solid #ece2d2">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Заказчик</div>
    <div><b>Адрес объекта:</b> г. Минск, ул. Нововиленская, 61-217</div>
    <div><b>Основание:</b> дизайн-проект (шифр 01/25, лист 25), постеночный обмер разверток</div>
    <div><b>Состав работ:</b> микроцемент в душевой и санузле — стены, откосы, короб инсталляции, фасады, полотна дверей-невидимок</div>
    <div><b>Площадь по материалам:</b> {a2(TOT_M2)} м² (два состава: микроцемент 1 и 2)</div>
  </div>
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#2c2c2c;color:#efece7">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Исполнитель</div>
    <div><b>UNICORE</b></div>
    <div>Алексей — менеджер проекта</div>
    <div>+375 (33) 628-04-86</div>
    <div style="color:#a09a92">info@romanovdecor.by · romanovdecor.by</div>
  </div>
</div>

<h3 style="font-size:10px;letter-spacing:3px;text-transform:uppercase;margin:9px 0 4px;color:#b8965a;font-weight:700">Спецификация материалов и работ</h3>
<table style="width:100%;border-collapse:collapse;font-size:10px">
<colgroup><col style="width:23%"><col style="width:8.5%"><col style="width:10%"><col style="width:10%"><col style="width:15%"><col style="width:10%"><col style="width:9.5%"><col style="width:14%"></colgroup>
<thead>
<tr><th rowspan="2" style="{STY['th_top_name']}">Наименование</th><th colspan="3" style="{STY['th_top_mat']}">Материалы</th><th colspan="3" style="{STY['th_top_work']}">Работы</th><th rowspan="2" style="{STY['th_top_tot']}">Итого, €</th></tr>
<tr><th style="{STY['th_sub_mat']}">Объём</th><th style="{STY['th_sub_mat']};white-space:nowrap">Цена</th><th style="{STY['th_sub_mat']}">Сумма, €</th><th style="{STY['th_sub_work']}">Объём</th><th style="{STY['th_sub_work']};white-space:nowrap">Цена</th><th style="{STY['th_sub_work']}">Сумма, €</th></tr>
</thead>
<tbody>{rows}</tbody>
</table>

<div style="text-align:right;margin:8px 0 0;letter-spacing:1px"><span style="font-size:11px;font-weight:600">ИТОГО К ОПЛАТЕ:</span> <span style="font-size:17px;font-weight:700;color:#b8965a">{u(TOT)}</span></div>
<div style="text-align:right;font-size:9px;color:#888;letter-spacing:1px;margin:3px 0 0">≈ {byn(TOT)} руб по курсу НБ РБ {f'{RATE:.4f}'.replace('.', ',')} BYN/EUR на день оплаты</div>

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0 0">
  <div style="padding:10px 14px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px">
    <div style="color:#8a7346;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Материалы</div>
    <div style="font-size:17px;font-weight:700;color:#2c2c2c;margin-top:3px">{u(TM)}</div></div>
  <div style="padding:10px 14px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px">
    <div style="color:#8a7346;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Работы</div>
    <div style="font-size:17px;font-weight:700;color:#2c2c2c;margin-top:3px">{u(TW)}</div></div>
  <div style="padding:10px 14px;background:#2c2c2c;border-radius:5px">
    <div style="color:#b8965a;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Всего</div>
    <div style="font-size:18px;font-weight:700;color:#b8965a;margin-top:3px">{u(TOT)}</div></div>
</div>

<div style="margin-top:9px;padding:6px 12px;background:#f7f5f0;border-left:2px solid #b8965a;border-radius:3px;font-size:8.4px;color:#666;line-height:1.45">
<b style="color:#2c2c2c"><sup>*</sup> м.п.</b> — погонные метры: поверхности со стороной менее 0,5 м нормируются по длине (ровно 0,50 м — уже квадратами). Это полосы у скрытых коробов и над проёмами, полоса 75 мм в душевой, стены 330 и 485 мм в санузле и откосы двух проёмов ~0,1 м (10,20 м.п.).<br>
<b style="color:#2c2c2c">Двери-невидимки:</b> полотно покрывается заподлицо со стеной; материал по площади стороны ({a2(DOOR_SIDE)} м² на дверь), работа — {u(DOOR_WORK)} за сторону.<br>
<b style="color:#2c2c2c">Инсталляция и фасады:</b> гипсовый короб инсталляции отделывается микроцементом как стена; МДФ-фасады люков — материал по ставке стен, работа по тарифу мебели ({u(FURN_M2)}/м² + {u(FURN_EDGE)}/м.п. кромки).<br>
<b style="color:#2c2c2c">Объёмы</b> сняты постеночно с разверток листа 25 и согласованы: зоны за зеркалом и тумбами санузла включены; крупное зеркало и встроенные шкафы душевой исключены; полосы 175 и 90 мм — покраска по проекту. Запас материала 5% учтён в закупке и в цену не входит. Финальные объёмы уточняются бесплатным замером.<br>
<b style="color:#2c2c2c">Вне сметы</b> (по результатам замера): гидроизоляция мокрых зон, герметизация трапа (€45), примыкания к плитке и керамогранитной полке, ремонт основания при дефектах.<br>
<b style="color:#2c2c2c">Условия:</b> микроцемент UNICORE на немецких компонентах, толщина 1–1,5 мм; два состава/цвета по проекту (микроцемент 1 и 2), колеровка включена. Грунт + 1–2 слоя микроцемента + 2 слоя полиуретанового лака Remmers. Цены в евро, оплата в белорусских рублях по курсу НБ РБ на день оплаты. <b>Срок действия КП — 14 дней.</b>
</div>

<div style="margin-top:auto;padding-top:8px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Спасибо за доверие!</div>
</div>

</div></body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/kp-novovilenskaya.html', 'w').write(html)
for name, mat_m2, wide_m2, mp in ZONES:
    print(f'{name:40s} мат {mat_m2:6.2f} м²   раб {wide_m2:6.2f} м² + {mp:5.2f} м.п.')
print(f'{"фасады":40s} раб {FURN_AREA:.2f} м² + {FURN_MP:.2f} м.п. кромки = {u(FURN_AREA * FURN_M2 + FURN_MP * FURN_EDGE)}')
print(f'{"двери":40s} мат {D_M2:6.2f} м²   {ND} стор.')
print(f'площадь для шкалы {a2(TOT_M2)} м² | материал {u(EFF_MAT)}/м² | работа {u(EFF_WRK)}/ед.')
print(f'материалы {u(TM)} | работы {u(TW)} | ИТОГО {u(TOT)} ≈ {byn(TOT)} руб')
