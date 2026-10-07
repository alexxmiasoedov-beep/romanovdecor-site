#!/usr/bin/env python3
# Технологическая карта: микроцемент на пол. Нейтральная, без марок
# материалов и названия фирмы (просьба владельца).
# Порядок операций и слоёв — со слов владельца (07.10.2026). Нормы условий
# и сроки — типовые для эпоксидных систем, точные интервалы по ТДС материалов.
import os

SC = os.environ.get('SC', '/tmp/kp')
DOC_DATE = 'октябрь 2026'

STAGES = [
    ('А', 'Подготовка основания', 1, 4),
    ('Б', 'Эпоксидное выравнивание', 5, 8),
    ('В', 'Армирующий слой', 9, 10),
    ('Г', 'Декоративное покрытие', 11, 14),
]

# номер, название, что делаем, инструмент и материал, контроль, переход к следующей операции
STEPS = [
    (1, 'Шлифовка основания',
     'Снимаем цементное молочко, слабый верхний слой и загрязнения. Открываем поры стяжки, чтобы грунт впитался.',
     'шлифмашина с алмазными сегментами, у стен — болгарка с чашкой',
     'поверхность равномерно матовая, без глянцевых пятен и рыхлых участков',
     'сразу'),
    (2, 'Обеспыливание',
     'Убираем пыль с поверхности, из пор и трещин.',
     'промышленный пылесос',
     'на ладони, проведённой по полу, нет пыли',
     'сразу'),
    (3, 'Ремонт выбоин и трещин',
     'Расшиваем трещины, выбоины вычищаем до прочного основания. Заполняем ремонтным составом на эпоксидной смоле с кварцевым песком, после отверждения шлифуем заподлицо.',
     'болгарка, шпатель, эпоксидная смола, кварцевый песок',
     'ремонтные места вровень с полом, при простукивании нет пустот',
     'после отверждения смолы'),
    (4, 'Пропитка и укрепление стяжки эпоксидным грунтом',
     'Пропитываем стяжку грунтом до насыщения, без луж. Грунт укрепляет верхний слой, связывает остатки пыли и даёт сцепление следующим слоям.',
     'эпоксидный грунт, валик, ракля',
     'поверхность пропитана равномерно; впитавшиеся сухие пятна — второй проход',
     'по ТДС грунта'),
    (5, 'Первый выравнивающий эпоксидный слой',
     'Наносим эпоксидную смолу с наполнителем раклей или шпателем. Закрываем поры и мелкие неровности.',
     'эпоксидная смола, кварцевый наполнитель, ракля, шпатель',
     'сплошная плёнка без пропусков и открытых пор',
     'по ТДС смолы'),
    (6, 'Второй выравнивающий эпоксидный слой',
     'Вторым проходом выводим плоскость и перекрываем следы первого слоя.',
     'эпоксидная смола, ракля, шпатель',
     'ровная плоскость без перепадов и наплывов',
     'по ТДС смолы'),
    (7, 'Полировка пола',
     'Шлифуем эпоксидный слой: снимаем наплывы, сор и глянец, создаём сцепление для следующего слоя.',
     'шлифмашина с абразивом',
     'поверхность равномерно матовая',
     'сразу'),
    (8, 'Обеспыливание',
     'Убираем шлифовальную пыль со всей площади.',
     'промышленный пылесос',
     'на ладони нет пыли',
     'сразу'),
    (9, 'Эпоксидная «шуба»',
     'Протягиваем смолу валиком или раклей и сразу присыпаем кварцевым песком фракции 0,4–0,6 мм до избытка. Слой армирует систему и даёт шероховатость для сцепления с микроцементом.',
     'эпоксидная смола, кварцевый песок 0,4–0,6 мм, валик, ракля',
     'песок лёг сплошным ковром, без проплешин',
     'после отверждения сметаем излишки песка'),
    (10, 'Шлифовка и обеспыливание',
     'Сбиваем острые зёрна и непрочно сидящий песок, убираем пыль.',
     'шлифмашина, промышленный пылесос',
     'шероховатость равномерная, зёрна не осыпаются',
     'сразу'),
    (11, 'Финишное декоративное покрытие',
     'Наносим декоративный микроцемент в цвете проекта и формируем фактуру.',
     'декоративный микроцемент, кельма из нержавеющей стали, шпатели',
     'цвет и фактура совпадают с согласованной выкраской, нет непрокрасов',
     'по ТДС микроцемента'),
    (12, 'Шлифовка и обеспыливание',
     'Мелким абразивом снимаем заусенцы и выравниваем фактуру, убираем пыль.',
     'шлифмашина или ручной шлифблок, пылесос',
     'поверхность гладкая на ощупь',
     'сразу'),
    (13, 'Прозрачный укрепляющий декоративный слой',
     'Пропитываем микроцемент прозрачным составом: он закрепляет поверхность, проявляет глубину цвета и готовит основу под лак.',
     'прозрачный укрепляющий состав, валик',
     'тон ровный, без пятен и потёков',
     'по ТДС состава'),
    (14, 'Запечатка финишным полиуретановым лаком',
     'Наносим 2К полиуретановый лак в два слоя. Лак защищает пол от истирания, воды и пятен и задаёт степень блеска.',
     '2К полиуретановый лак, велюровый валик',
     'блеск сплошной и равномерный, без пузырей и пропусков',
     'эксплуатация — по срокам ниже'),
]

CONDITIONS = [
    ('Основание', 'цементная стяжка, прочность от М150, полностью выдержанная'),
    ('Влажность основания', 'не более 4%'),
    ('Температура воздуха и основания', '+15…+25 °C'),
    ('Влажность воздуха', 'не более 75%'),
    ('Точка росы', 'основание теплее точки росы минимум на 3 °C'),
    ('Помещение', 'без сквозняков и прямого солнца, посторонние работы остановлены'),
]

RULES = [
    'Каждый следующий слой — только на чистую, обеспыленную и сухую поверхность.',
    'Эпоксидные составы замешиваем миксером и вырабатываем до начала загустевания.',
    'Не ходим по свежему слою; заходить можно только когда слой не липнет.',
    'Инструмент отмываем сразу после работы, пока состав не встал.',
    'Работаем в перчатках, очках и респираторе; помещение проветриваем.',
    'Каждую операцию отмечаем в карте: что сделано, дата, подпись мастера.',
]

AFTER = [
    ('24 часа', 'можно ходить в чистой обуви'),
    ('3 суток', 'можно расставлять мебель на мягких подпятниках'),
    ('7 суток', 'полная нагрузка и влажная уборка'),
]

GOLD, DARK, LIGHT, BEIGE, LINE = '#b8965a', '#2c2c2c', '#efece7', '#f5efe2', '#cbbf9f'

def header(page, total):
    return f'''<div class="hd">
  <div class="dt">Технологическая карта</div>
  <div class="pg">микроцемент на пол · лист {page} из {total}</div>
</div>'''


FOOTER = ('<div class="ft"><div>Технологическая карта · микроцемент на пол</div>'
          f'<div class="gold">{DOC_DATE}</div></div>')


def layers_svg():
    # разрез системы снизу вверх: (подпись, толщина на рисунке, заливка, номера операций)
    L = [
        ('Стяжка — основание', 58, '#a8a196', '1–3'),
        ('Эпоксидный грунт, пропитка', 7, '#c9a96a', '4'),
        ('Выравнивающий эпоксидный слой', 13, '#d9cfbb', '5'),
        ('Второй выравнивающий слой', 13, '#cfc4ad', '6–8'),
        ('Эпоксидная «шуба» с кварцем', 15, '#bdb29b', '9–10'),
        ('Декоративный микроцемент', 18, '#8d8780', '11–12'),
        ('Прозрачный укрепляющий слой', 7, '#e8e2d4', '13'),
        ('Полиуретановый лак, 2 слоя', 6, GOLD, '14'),
    ]
    W, H = 728, 268
    x0, x1, step = 20, 430, 46
    y = 238
    shapes, labels = [], []
    n = len(L)
    label_ys = [y - 8 - i * 29 for i in range(n)]
    for i, (name, h, fill, ops) in enumerate(L):
        left = x0 + i * step
        top = y - h
        shapes.append(f'<rect x="{left}" y="{top}" width="{x1 - left}" height="{h}" fill="{fill}" '
                      f'stroke="#2c2c2c" stroke-opacity=".18" stroke-width="1"/>')
        if i == 0:
            for k in range(60):
                cx = left + 8 + (k * 37) % (x1 - left - 16)
                cy = top + 8 + (k * 23) % (h - 14)
                shapes.append(f'<circle cx="{cx}" cy="{cy}" r="{1.2 + (k % 3) * 0.6}" fill="#6f6a62" fill-opacity=".45"/>')
        if i == 4:
            for k in range(90):
                cx = left + 4 + (k * 13) % (x1 - left - 8)
                cy = top + 3 + (k * 7) % (h - 6)
                shapes.append(f'<circle cx="{cx}" cy="{cy}" r="1.3" fill="#f4efe4"/>')
        if i == 7:
            shapes.append(f'<rect x="{left}" y="{top}" width="{x1 - left}" height="2" fill="#ffffff" fill-opacity=".55"/>')
        ly = label_ys[i]
        cy = top + h / 2
        shapes.append(f'<polyline points="{x1},{cy:.1f} {x1 + 22},{cy:.1f} {x1 + 46},{ly} {x1 + 54},{ly}" '
                      f'fill="none" stroke="#b8965a" stroke-width="1"/>')
        shapes.append(f'<circle cx="{x1}" cy="{cy:.1f}" r="2.2" fill="#b8965a"/>')
        labels.append(f'<text x="{x1 + 60}" y="{ly + 4}" font-size="11" fill="#2c2c2c" font-weight="600">{name}</text>'
                      f'<text x="{W - 4}" y="{ly + 4}" font-size="9.5" fill="#8a7346" text-anchor="end" '
                      f'letter-spacing="1">оп. {ops}</text>')
        y = top
    return (f'<svg width="100%" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Geologica, Arial, sans-serif">' + ''.join(shapes) + ''.join(labels) +
            f'<text x="{x0}" y="{H - 6}" font-size="9" fill="#888" letter-spacing="1">РАЗРЕЗ СИСТЕМЫ · ТОЛЩИНЫ СЛОЁВ УСЛОВНЫЕ</text></svg>')


def stage_of(num):
    for code, name, a, b in STAGES:
        if a <= num <= b:
            return code, name


def card(s):
    num, title, what, tools, control, nxt = s
    return f'''<div class="card">
  <div class="num">{num:02d}</div>
  <div class="body">
    <div class="ttl">{title}</div>
    <div class="what">{what}</div>
    <div class="meta">
      <div><span class="k">Инструмент и материал</span>{tools}</div>
      <div><span class="k">Контроль</span>{control}</div>
    </div>
    <div class="row">
      <span class="next">Дальше: {nxt}</span>
      <span class="sign">☐ выполнено · дата ________ · подпись ________</span>
    </div>
  </div>
</div>'''


def stage_title(code):
    for c, name, a, b in STAGES:
        if c == code:
            return f'<div class="stage"><span class="sc">Этап {c}</span>{name}<span class="sr">операции {a}–{b}</span></div>'


def steps_block(nums):
    out, cur = [], None
    for s in STEPS:
        if s[0] not in nums:
            continue
        code, _ = stage_of(s[0])
        if code != cur:
            out.append(stage_title(code))
            cur = code
        out.append(card(s))
    return '\n'.join(out)


CSS = f'''
@page{{size:A4;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:794px;font-family:Geologica,Arial,sans-serif;color:{DARK};background:#fff}}
.page{{width:794px;height:1123px;padding:16px 34px 14px;display:flex;flex-direction:column;overflow:hidden;page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto;break-after:auto}}
.hd{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid {GOLD};padding-bottom:8px}}
.dt{{font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase}}
.pg{{font-size:9px;color:#888;letter-spacing:1.5px;margin-top:3px;text-transform:uppercase}}
.ft{{margin-top:auto;padding-top:7px;border-top:1px solid #eee;display:flex;justify-content:space-between;font-size:9px;color:#888;letter-spacing:1px}}
.gold{{color:{GOLD};font-weight:600}}
h1{{font-size:26px;letter-spacing:1px;font-weight:700;margin:18px 0 4px}}
.lead{{font-size:11.5px;color:#555;line-height:1.5;max-width:640px}}
h3{{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:700;margin:16px 0 7px}}
.fig{{border:1px solid #e3d7bd;border-radius:6px;padding:12px 12px 6px;background:#fcfaf6}}
.fig svg{{display:block;height:auto}}
.rules{{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:5px 18px;font-size:9.8px;line-height:1.45;color:#3a3a3a}}
.rules li{{padding-left:12px;position:relative}}
.rules li:before{{content:'';position:absolute;left:0;top:6px;width:5px;height:5px;background:{GOLD};border-radius:50%}}
.stages{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}
.st{{background:{BEIGE};border:1px solid #e3d7bd;border-radius:6px;padding:9px 11px}}
.st .c{{font-size:8px;letter-spacing:2px;text-transform:uppercase;color:{GOLD};font-weight:700}}
.st .n{{font-size:11.5px;font-weight:700;margin:3px 0 5px;line-height:1.25}}
.st ol{{font-size:9.2px;color:#555;line-height:1.45;padding-left:0;list-style:none}}
.st li b{{color:{DARK};font-weight:600;margin-right:3px}}
table{{width:100%;border-collapse:collapse;font-size:10px}}
td{{border:1px solid {LINE};padding:6px 9px;vertical-align:top;line-height:1.35}}
td.ck{{background:{BEIGE};font-weight:600;width:34%}}
.stage{{display:flex;align-items:baseline;gap:10px;margin:12px 0 6px;font-size:13px;font-weight:700;letter-spacing:.5px}}
.stage .sc{{background:{DARK};color:{GOLD};font-size:8.5px;letter-spacing:2px;text-transform:uppercase;padding:4px 8px;border-radius:3px}}
.stage .sr{{margin-left:auto;font-size:8.5px;color:#888;letter-spacing:1.5px;text-transform:uppercase;font-weight:500}}
.card{{display:flex;gap:12px;border:1px solid #e6dcc6;border-radius:6px;padding:9px 12px 8px 10px;margin-bottom:7px;background:#fff}}
.num{{flex:0 0 38px;height:38px;border-radius:50%;background:{DARK};color:{GOLD};font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;letter-spacing:.5px}}
.body{{flex:1;min-width:0}}
.ttl{{font-size:12.5px;font-weight:700;margin-bottom:3px}}
.what{{font-size:10px;line-height:1.45;color:#3a3a3a}}
.meta{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:5px;font-size:9.4px;line-height:1.4;color:#555}}
.k{{display:block;font-size:7.8px;letter-spacing:1.6px;text-transform:uppercase;color:{GOLD};font-weight:700;margin-bottom:1px}}
.row{{display:flex;justify-content:space-between;align-items:center;margin-top:6px;font-size:8.8px}}
.next{{background:#f8ecd3;color:#6a4a14;padding:2px 8px;border-radius:10px;font-weight:600}}
.sign{{color:#999;letter-spacing:.3px}}
.after{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}
.af{{background:{DARK};color:{LIGHT};border-radius:6px;padding:9px 12px}}
.af b{{display:block;color:{GOLD};font-size:15px;margin-bottom:2px}}
.af span{{display:block;font-size:9.6px;color:#d9d4cc;line-height:1.4}}
.note{{margin-top:9px;padding:7px 12px;background:#f7f5f0;border-left:2px solid {GOLD};border-radius:3px;font-size:8.8px;color:#666;line-height:1.5}}
.obj{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:8px;margin-top:9px;font-size:9.4px;color:#555}}
.obj div{{border-bottom:1px solid {LINE};padding:12px 0 3px}}
'''

stage_cards = ''.join(
    f'<div class="st"><div class="c">Этап {c} · оп. {a}–{b}</div><div class="n">{n}</div><ol>' +
    ''.join(f'<li><b>{s[0]}.</b>{s[1]}</li>' for s in STEPS if a <= s[0] <= b) +
    '</ol></div>' for c, n, a, b in STAGES)

cond_rows = ''.join(f'<tr><td class="ck">{k}</td><td>{v}</td></tr>' for k, v in CONDITIONS)
rules = ''.join(f'<li>{r}</li>' for r in RULES)
after_cards = ''.join(f'<div class="af"><b>{t}</b><span>{d}</span></div>' for t, d in AFTER)

P1 = f'''<div class="page">
{header(1, 3)}
<h1>Микроцемент на пол</h1>
<div class="lead">Система на эпоксидной основе: 14 операций в 4 этапа, 8 слоёв от стяжки до лака. Карта для мастера на объекте — каждую операцию отмечаем выполненной с датой и подписью.</div>
<h3>Слои системы</h3>
<div class="fig">{layers_svg()}</div>
<h3>Этапы и операции</h3>
<div class="stages">{stage_cards}</div>
<h3>Условия производства работ</h3>
<table>{cond_rows}</table>
<h3>Общие правила на объекте</h3>
<ul class="rules">{rules}</ul>
{FOOTER}
</div>'''

P2 = f'''<div class="page">
{header(2, 3)}
{steps_block(range(1, 9))}
{FOOTER}
</div>'''

P3 = f'''<div class="page">
{header(3, 3)}
{steps_block(range(9, 15))}
<h3>После завершения работ (при +20 °C)</h3>
<div class="after">{after_cards}</div>
<div class="note"><b style="color:#2c2c2c">Интервалы между слоями</b> зависят от температуры и влажности: точные сроки перекрытия и расход берём из технических листов (ТДС) материалов. При температуре ниже +15 °C отверждение замедляется, работы не ведём.</div>
<div class="obj"><div>Объект:</div><div>Площадь, м²:</div><div>Мастер:</div></div>
{FOOTER}
</div>'''

html = f'''<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
{P1}
{P2}
{P3}
</body></html>'''

os.makedirs(SC + '/kp', exist_ok=True)
open(SC + '/kp/techcard-floor.html', 'w').write(html)
print('ok')
