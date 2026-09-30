#!/usr/bin/env python3
# КП № 300926A — ул. Цвирко, 67, кв. 140. Полы 124 м², потолок 5 м², стены по замерам заказчика,
# мебельная дверь. Правила обсчёта — CLAUDE.md («Правила обсчёта объёмов»):
# сторона меньше 0,5 м — работа погонными по длине, иначе квадратами;
# материал — вся площадь. Полы и стены — каждая по своей шкале.
import os

SC = os.environ.get('SC', '/tmp/kp')
RATE = 3.4323          # BYN/EUR, курс НБ РБ на 30.09.2026
KP_DATE = '30 сентября 2026 г.'
KP_NUM = '300926A'

MISC = 80                           # малярные расходники
FURN_M2, FURN_EDGE = 45.0, 5.0      # фасады: €/м² плоскости, €/м.п. торца
CEIL_K = 1.2                        # потолок: работа +20% к ставке стен

D_FROM, D_TO = 35, 100
WALLS = dict(mat_hi=35, mat_lo=30, wrk_hi=21, wrk_lo=18.50)
FLOOR = dict(mat_hi=43, mat_lo=39, wrk_hi=22, wrk_lo=19.50)

def curve(a, hi, lo):
    if a <= D_FROM: return float(hi)
    if a >= D_TO:   return float(lo)
    return hi - (hi - lo) * (a - D_FROM) / (D_TO - D_FROM)

def u(v):
    s = f'{v:,.2f}'.replace(',', ' ').replace('.', ',')
    return '€' + (s[:-3] if s.endswith(',00') else s)
def a2(v): return f'{v:.2f}'.replace('.', ',')

# ── объёмы ───────────────────────────────────────────────────────────────
FLOOR_M2 = 124.0
CEIL_M2 = 5.0
# стены: ширина × высота, как в замерах заказчика
# (строка «0,76*0*87» прочитана как 0,76 × 0,87)
WALL_LIST = [
    (0.07, 2.06), (0.07, 2.06), (0.07, 0.70), (0.05, 2.06), (0.56, 1.68),
    (0.94, 2.06), (0.43, 2.63), (0.74, 2.03), (1.25, 1.71), (0.56, 0.82),
    (1.17, 0.46), (1.17, 0.08), (1.17, 0.08), (0.34, 0.08), (0.34, 1.17),
    (0.66, 2.06), (0.10, 1.44), (0.10, 1.44), (1.00, 1.21), (0.22, 2.63),
    (0.23, 1.76), (0.76, 0.87), (1.81, 2.63), (0.47, 1.60), (0.10, 1.60),
    (0.10, 1.60),
    (0.20, 1.43), (0.20, 1.43), (0.80, 1.43), (0.80, 1.43),
]
FURN = (1.76, 0.53)    # мебельная дверь
DOOR_W, DOOR_H = 0.7, 2.0   # дверное полотно под микроцемент, одна сторона
DOOR_SIDES = 1
DOOR_WORK = 63.0             # 700×2000 — €63 за сторону

def measure(ps, thr=0.5):
    m2 = sq = lin = 0.0
    for a, b in ps:
        m2 += a * b
        if min(a, b) < thr: lin += max(a, b)
        else:               sq += a * b
    return m2, sq, lin

W_M2, W_SQ, W_LIN = measure(WALL_LIST)
FURN_AREA = FURN[0] * FURN[1]
FURN_MP = 2 * (FURN[0] + FURN[1])
DOOR_M2 = DOOR_W * DOOR_H * DOOR_SIDES

# шкала скидки — по общей площади объекта: все поверхности берут ставку
# той точки кривой, в которую попадает сумма площадей
TOT_M2 = FLOOR_M2 + CEIL_M2 + W_M2 + FURN_AREA + DOOR_M2
W_MAT = curve(TOT_M2, WALLS['mat_hi'], WALLS['mat_lo'])
W_WRK = curve(TOT_M2, WALLS['wrk_hi'], WALLS['wrk_lo'])
F_MAT = curve(TOT_M2, FLOOR['mat_hi'], FLOOR['mat_lo'])
F_WRK = curve(TOT_M2, FLOOR['wrk_hi'], FLOOR['wrk_lo'])
C_WRK = W_WRK * CEIL_K

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
 td_work=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#fdeed2',
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

fm, fw = FLOOR_M2 * F_MAT, FLOOR_M2 * F_WRK
TM += fm; TW += fw
rows += row('Пол', f'{a2(FLOOR_M2)} м²', u(F_MAT), u(fm), f'{a2(FLOOR_M2)} м²', u(F_WRK), u(fw), u(fm + fw))

wm, ww = W_M2 * W_MAT, (W_SQ + W_LIN) * W_WRK
TM += wm; TW += ww
rows += row('Стены', f'{a2(W_M2)} м²', u(W_MAT), u(wm),
            f'{a2(W_SQ)} м² + {a2(W_LIN)} м.п.<sup>*</sup>', u(W_WRK), u(ww), u(wm + ww))

cm, cw = CEIL_M2 * W_MAT, CEIL_M2 * C_WRK
TM += cm; TW += cw
rows += row('Потолок', f'{a2(CEIL_M2)} м²', u(W_MAT), u(cm), f'{a2(CEIL_M2)} м²', u(C_WRK), u(cw), u(cm + cw))

dm, dw = FURN_AREA * W_MAT, FURN_AREA * FURN_M2 + FURN_MP * FURN_EDGE
TM += dm; TW += dw
rows += row('Мебельная дверь (фасад)', f'{a2(FURN_AREA)} м²', u(W_MAT), u(dm),
            f'{a2(FURN_AREA)} м² + {a2(FURN_MP)} м.п.', f'{u(FURN_M2)}+{u(FURN_EDGE)}', u(dw), u(dm + dw))

pm, pw = DOOR_M2 * W_MAT, DOOR_SIDES * DOOR_WORK
TM += pm; TW += pw
rows += row('Дверь 700×2000', f'{a2(DOOR_M2)} м²', u(W_MAT), u(pm),
            f'{DOOR_SIDES} стор.', u(DOOR_WORK), u(pw), u(pm + pw))

TM += MISC
rows += row('Малярные расходники, валики', 'компл.', '—', u(MISC), '—', '—', '—', u(MISC))

TOT = TM + TW
rows += sub('Всего по проекту', f'{a2(TOT_M2)} м²', u(TM), '—', u(TW), u(TOT))

# экономия против базовых ставок — карточка «Скидка», как в эталоне
FULL = (FLOOR_M2 * (FLOOR['mat_hi'] + FLOOR['wrk_hi'])
        + W_M2 * WALLS['mat_hi'] + (W_SQ + W_LIN) * WALLS['wrk_hi']
        + CEIL_M2 * (WALLS['mat_hi'] + WALLS['wrk_hi'] * CEIL_K)
        + FURN_AREA * WALLS['mat_hi'] + FURN_AREA * FURN_M2 + FURN_MP * FURN_EDGE + MISC
        + DOOR_M2 * WALLS['mat_hi'] + DOOR_SIDES * DOOR_WORK)
SAVE = max(0.0, FULL - TOT)
SAVE_PCT = round(SAVE / FULL * 1000) / 10 if FULL else 0
CARD_COLS = 4 if SAVE > 0.01 else 3
SAVE_CARD = ('<div style="padding:10px 14px;background:#fdf1ec;border:1px solid #eccfc2;border-radius:5px">'
             '<div style="color:#b3402e;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Скидка</div>'
             f'<div style="font-size:17px;font-weight:700;color:#b3402e;margin-top:3px">−{u(SAVE)} '
             f'<span style="font-size:11px">(−{f"{SAVE_PCT:g}".replace(".", ",")}%)</span></div></div>'
             ) if SAVE > 0.01 else ''

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
    <div><b>Адрес объекта:</b> г. Минск, ул. Цвирко, 67, кв. 140 (5 этаж)</div>
    <div><b>Площадь по материалам:</b> {a2(TOT_M2)} м²</div>
  </div>
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#2c2c2c;color:#efece7">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Исполнитель</div>
    <div><b>UNICORE</b></div>
    <div>Алексей — менеджер проекта</div>
    <div>+375 (33) 628-04-86</div>
    <div style="color:#a09a92">г. Минск</div>
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

<div style="display:grid;grid-template-columns:repeat({CARD_COLS},1fr);gap:10px;margin:14px 0 0">
  <div style="padding:10px 14px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px">
    <div style="color:#8a7346;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Материалы</div>
    <div style="font-size:17px;font-weight:700;color:#2c2c2c;margin-top:3px">{u(TM)}</div></div>
  <div style="padding:10px 14px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px">
    <div style="color:#8a7346;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Работы</div>
    <div style="font-size:17px;font-weight:700;color:#2c2c2c;margin-top:3px">{u(TW)}</div></div>
  {SAVE_CARD}
  <div style="padding:10px 14px;background:#2c2c2c;border-radius:5px">
    <div style="color:#b8965a;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Всего</div>
    <div style="font-size:18px;font-weight:700;color:#b8965a;margin-top:3px">{u(TOT)}</div></div>
</div>

<div style="margin-top:9px;padding:6px 12px;background:#f7f5f0;border-left:2px solid #b8965a;border-radius:3px;font-size:8.4px;color:#666;line-height:1.45">
<b style="color:#2c2c2c"><sup>*</sup> м.п.</b> — стены меньше 0,5 м.<br>
<b style="color:#2c2c2c">Условия:</b> микроцемент UNICORE на немецких компонентах, толщина 1–1,5 мм, колеровка включена. Грунт + 1–2 слоя микроцемента + 2 слоя полиуретанового лака Remmers. Цены в евро, оплата в белорусских рублях по курсу НБ РБ на день оплаты. <b>Срок действия КП — 14 дней.</b>
</div>

<div style="margin-top:auto;padding-top:8px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#888;letter-spacing:1px">
  <div>UNICORE · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Спасибо за доверие!</div>
</div>

</div></body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/kp-300926A.html', 'w').write(html)
print(f'пол      мат {FLOOR_M2:7.2f} м² × {F_MAT}  раб × {F_WRK}')
print(f'стены    мат {W_M2:7.3f} м²   раб {W_SQ:.3f} м² + {W_LIN:.2f} м.п.  (ставки {W_MAT}/{W_WRK})')
print(f'потолок  мат {CEIL_M2:7.2f} м²   раб × {C_WRK:.2f}')
print(f'фасад    {FURN_AREA:.4f} м² + {FURN_MP:.2f} м.п. = раб {u(dw)}')
print(f'материалы {u(TM)} | работы {u(TW)} | скидка {u(SAVE)} | ИТОГО {u(TOT)} ≈ {byn(TOT)} руб')
