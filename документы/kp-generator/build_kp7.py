#!/usr/bin/env python3
# КП — спальня + санузел (стены), стиль калькулятора сайта
SC = '/tmp/claude-0/-home-user-romanovdecor-site/22c3148d-250b-5717-947a-9e939509d679/scratchpad'
MW, WW = 40, 24
RATE = 2.9133

def u(v):
    s = f'{v:,.2f}'.replace(',', ' ').replace('.', ',')
    return '$' + (s[:-3] if s.endswith(',00') else s)
def a2(v): return f'{v:.2f}'.replace('.', ',')
def pf(v): return f'{v:g}'.replace('.', ',') if v == int(v) else a2(v)

B = '#cbbf9f'
GRID = f'border:1px solid {B}'
NUM  = 'font-variant-numeric:tabular-nums'
CELL = f'padding:5.5px 6px;{GRID};vertical-align:middle;font-size:10px;line-height:1.25;height:19px'
THB  = f'{GRID};font-size:9px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:5px 6px;vertical-align:middle;text-align:center'
THS  = f'{GRID};font-weight:500;letter-spacing:1px;font-size:9px;padding:4px 6px;vertical-align:middle;text-align:center'
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
 td_tot=f'{CELL};{NUM};text-align:right;white-space:nowrap;background:#f5efe2;font-weight:700;color:#2c2c2c',
)
ZONE_TD = f'background:#2c2c2c;color:#b8965a;font-weight:600;letter-spacing:2px;text-transform:uppercase;font-size:8.5px;padding:4.2px 10px;{GRID}'
SUBB = f'{GRID};{NUM};font-weight:700;font-size:10px;padding:5.5px 6px;text-align:right;white-space:nowrap;height:19px;vertical-align:middle'
SUB_TD_NAME = f'background:#eae0cb;{GRID};font-weight:700;font-size:10px;color:#3a3a3a;padding:5.5px 10px;vertical-align:middle'
SUB_TD_MAT = f'background:#e2ecc8;color:#3a4a1c;{SUBB}'
SUB_TD_WORK = f'background:#f8ddb0;color:#6a4a14;{SUBB}'
SUB_TD_TOT = f'background:#eae0cb;color:#7a5614;{SUBB}'

def zone(label): return f'<tr><td colspan="8" style="{ZONE_TD}">{label}</td></tr>'
def row(name, mO, mP, mS, wO, wP, wS, tot):
    return (f'<tr><td style="{STY["td_name"]}">{name}</td>'
            f'<td style="{STY["td_mat"]}">{mO}</td><td style="{STY["td_matp"]}">{mP}</td><td style="{STY["td_mat"]}">{mS}</td>'
            f'<td style="{STY["td_work"]}">{wO}</td><td style="{STY["td_workp"]}">{wP}</td><td style="{STY["td_work"]}">{wS}</td>'
            f'<td style="{STY["td_tot"]}">{tot}</td></tr>')
def sub(name, mO, mP, mS, wO, wP, wS, tot):
    return (f'<tr><td style="{SUB_TD_NAME}">{name}</td>'
            f'<td style="{SUB_TD_MAT}">{mO}</td><td style="{SUB_TD_MAT};text-align:center">{mP}</td><td style="{SUB_TD_MAT}">{mS}</td>'
            f'<td style="{SUB_TD_WORK}">{wO}</td><td style="{SUB_TD_WORK};text-align:center">{wP}</td><td style="{SUB_TD_WORK}">{wS}</td>'
            f'<td style="{SUB_TD_TOT}">{tot}</td></tr>')

rowsHtml = ''
TM = TW = 0.0
def wall(name, m2, sq, lin):
    global TM, TW, rowsHtml
    m = m2 * MW; w = (sq + lin) * WW
    TM += m; TW += w
    parts = []
    if sq:  parts.append(f'{a2(sq)} м²')
    if lin: parts.append(f'{a2(lin)} м.п.<sup>*</sup>')
    rowsHtml += row(name, f'{a2(m2)} м²', f'${MW}', u(m), ' + '.join(parts), f'${WW}', u(w), u(m + w))
    return m, w

# --- Спальня ---
rowsHtml += zone('Спальня')
m1, w1 = wall('Стены', 24.13, 20.61, 24.35)
rowsHtml += sub('Итого Спальня', '24,13 м²', '', u(m1), '20,61 м² + 24,35 м.п.', '', u(w1), u(m1 + w1))

# --- Санузел ---
rowsHtml += zone('Санузел')
m2_, w2 = wall('Стены', 8.73, 5.91, 15.08)
rowsHtml += sub('Итого Санузел', '8,73 м²', '', u(m2_), '5,91 м² + 15,08 м.п.', '', u(w2), u(m2_ + w2))

# --- Двери ---
rowsHtml += zone('Двери')
dm = 4.00 * MW; dw = 2 * 100
TM += dm; TW += dw
rowsHtml += row('Двери', '4,00 м²', f'${MW}', u(dm), '2 шт', '$100', u(dw), u(dm + dw))
rowsHtml += sub('Итого Двери', '4,00 м²', '', u(dm), '2 дв.', '', u(dw), u(dm + dw))

# --- Мебель ---
rowsHtml += zone('Мебель')
F_A, F_E, F_R, F_RE = 0.826, 3.98, 20, 10
fm = F_A * MW
fw = F_A * F_R + F_E * F_RE
TM += fm; TW += fw
rowsHtml += row('Мебель', f'{a2(F_A)} м²', f'${MW}', u(fm),
                f'{a2(F_A)} м² + {a2(F_E)} м.п.<sup>*</sup>', f'${F_R} / ${F_RE}', u(fw), u(fm + fw))
rowsHtml += sub('Итого Мебель', f'{a2(F_A)} м²', '', u(fm), f'{a2(F_A)} м² + {a2(F_E)} м.п.', '', u(fw), u(fm + fw))

# --- Прочее ---
rowsHtml += zone('Прочее')
MISC = 100
TM += MISC
rowsHtml += row('Малярные расходники, валики', 'компл.', '—', u(MISC), '—', '—', '—', u(MISC))
rowsHtml += sub('Итого Прочее', 'компл.', '', u(MISC), '—', '', '—', u(MISC))

TOT = TM + TW
tot_m2 = 24.13 + 8.73 + 4.00 + F_A
rowsHtml += sub('Всего по проекту', f'{a2(tot_m2)} м²', '', u(TM), '—', '', u(TW), u(TOT))

byn = lambda v: f'{round(v*RATE):,}'.replace(',', ' ')
logoSvg = ('<svg width="44" height="44" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
           '<rect width="32" height="32" rx="6" fill="#2c2c2c"/>'
           '<text x="50%" y="54%" font-family="Geologica,Arial,sans-serif" font-size="20" font-weight="700" fill="#b8965a" text-anchor="middle" dominant-baseline="middle">r</text></svg>')

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:210mm}}</style></head><body>
<div style="width:100%;min-height:1123px;padding:14px 32px 12px;background:#fff;color:#2c2c2c;font-family:Geologica,Arial,sans-serif;display:flex;flex-direction:column">

<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;border-bottom:2px solid #b8965a;padding-bottom:5px">
  <div style="display:flex;align-items:center;gap:10px">{logoSvg}
    <div><div style="font-size:16px;letter-spacing:2px;font-weight:500;text-transform:lowercase;line-height:1.1">romanov <span style="color:#b8965a">decor</span> studio</div>
    <div style="font-size:9px;color:#888;margin-top:3px;letter-spacing:1px;text-transform:uppercase">микроцемент на немецких компонентах</div></div>
  </div>
  <div style="text-align:right;font-size:10px;color:#666;letter-spacing:1px">
    <div>12 августа 2026 г.</div>
    <div style="margin-top:2px;font-weight:600;color:#2c2c2c">КП № 12082026</div>
  </div>
</div>

<div style="font-size:16px;font-weight:700;letter-spacing:2px;margin:9px 0 7px">Коммерческое предложение</div>
<div style="display:flex;gap:10px;margin-bottom:6px">
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#faf6ef;border:1px solid #ece2d2">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Заказчик</div>
    <div><b>ФИО:</b> Владимир</div>
    <div><b>Телефон:</b> +375 (29) 552-39-09</div>
    <div><b>Адрес объекта:</b> объект «Миля 4»</div>
    <div><b>Площадь по материалам:</b> {a2(tot_m2)} м²</div>
  </div>
  <div style="flex:1;padding:6px 12px;border-radius:6px;font-size:10px;line-height:1.42;background:#2c2c2c;color:#efece7">
    <div style="font-size:8px;text-transform:uppercase;letter-spacing:2px;color:#b8965a;font-weight:600;margin-bottom:2px">Исполнитель</div>
    <div><b>Romanov Decor Studio</b></div>
    <div>Алексей — менеджер проекта</div>
    <div>+375 (33) 628-04-86</div>
    <div style="color:#a09a92">info@romanovdecor.by · romanovdecor.by</div>
  </div>
</div>

<h3 style="font-size:10px;letter-spacing:3px;text-transform:uppercase;margin:9px 0 4px;color:#b8965a;font-weight:700">Спецификация материалов и работ</h3>
<table style="width:100%;border-collapse:collapse;font-size:10px">
<colgroup><col style="width:21%"><col style="width:8.5%"><col style="width:10.5%"><col style="width:10%"><col style="width:15%"><col style="width:10.5%"><col style="width:10%"><col style="width:14.5%"></colgroup>
<thead>
<tr><th rowspan="2" style="{STY['th_top_name']}">Наименование</th><th colspan="3" style="{STY['th_top_mat']}">Материалы</th><th colspan="3" style="{STY['th_top_work']}">Работы</th><th rowspan="2" style="{STY['th_top_tot']}">Итого, $</th></tr>
<tr><th style="{STY['th_sub_mat']}">Объём</th><th style="{STY['th_sub_mat']};white-space:nowrap">Цена за м²</th><th style="{STY['th_sub_mat']}">Сумма, $</th><th style="{STY['th_sub_work']}">Объём</th><th style="{STY['th_sub_work']};white-space:nowrap">Цена за м²</th><th style="{STY['th_sub_work']}">Сумма, $</th></tr>
</thead>
<tbody>{rowsHtml}</tbody>
</table>

<div style="text-align:right;margin:8px 0 0;letter-spacing:1px"><span style="font-size:11px;font-weight:600">ИТОГО К ОПЛАТЕ:</span> <span style="font-size:17px;font-weight:700;color:#b8965a">{u(TOT)}</span></div>
<div style="text-align:right;font-size:9px;color:#888;letter-spacing:1px;margin:3px 0 0">≈ {byn(TOT)} руб по курсу НБ РБ {a2(RATE)} BYN/USD на день оплаты</div>

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0 0">
  <div style="padding:10px 14px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px">
    <div style="color:#8a7346;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Материалы</div>
    <div style="font-size:17px;font-weight:700;color:#2c2c2c;margin-top:3px">{u(TM)}</div>
  </div>
  <div style="padding:10px 14px;background:#f5efe2;border:1px solid #e3d7bd;border-radius:5px">
    <div style="color:#8a7346;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Работы</div>
    <div style="font-size:17px;font-weight:700;color:#2c2c2c;margin-top:3px">{u(TW)}</div>
  </div>
  <div style="padding:10px 14px;background:#2c2c2c;border-radius:5px">
    <div style="color:#b8965a;letter-spacing:2px;text-transform:uppercase;font-size:8px;font-weight:600">Всего</div>
    <div style="font-size:18px;font-weight:700;color:#b8965a;margin-top:3px">{u(TOT)}</div>
  </div>
</div>

<div style="margin-top:9px;padding:6px 12px;background:#f7f5f0;border-left:2px solid #b8965a;border-radius:3px;font-size:8.4px;color:#666;line-height:1.45">
<b style="color:#2c2c2c"><sup>*</sup> м.п.</b> — погонные метры: поверхности со стороной менее 0,5 м (откосы, ниши, бортики) нормируются по длине, так как нанесение на них идёт медленнее, чем на сплошной стене.<br>
<b style="color:#2c2c2c">Двери:</b> материал считается по площади полотна, работа — фиксированно $100 за штуку.<br>
<b style="color:#2c2c2c">Мебель:</b> плоскости $20/м², кромка (торцы) $10 за погонный метр.<br>
<b style="color:#2c2c2c">Условия:</b> микроцемент на немецких компонентах, толщина 1–1,5 мм, эффекты Vintage / Natural / Metallic на выбор. Грунт + 1–2 слоя микроцемента + 2 слоя защитного лака. Оплата в белорусских рублях по курсу НБ РБ на день оплаты. <b>Срок действия КП — 14 дней.</b>
</div>

<div style="margin-top:auto;padding-top:8px;border-top:1px solid #eee;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#888;letter-spacing:1px">
  <div>romanovdecor.by · info@romanovdecor.by · +375 (33) 628-04-86 · Минск</div>
  <div style="color:#b8965a;font-weight:600">Спасибо за доверие!</div>
</div>

</div></body></html>'''
open(SC + '/kp/kp-spalnya.html', 'w').write(html)
print(f'материал {u(TM)} | работа {u(TW)} | ИТОГО {u(TOT)} ≈ {byn(TOT)} руб')
