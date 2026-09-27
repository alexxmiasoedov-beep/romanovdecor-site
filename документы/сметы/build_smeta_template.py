#!/usr/bin/env python3
# Шаблон локальной сметы на ремонт квартиры «под ключ» (Минск, срез 27.09.2026)
# с примером расчёта под профиль: штукатурка только новых перегородок,
# шпаклёвка Q3 по существующим стенам, самонивелир 5 мм + клеевой кварцвинил.
import csv, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

ROOT = '/home/user/romanovdecor-site/документы'
OUT = f'{ROOT}/сметы/смета-ремонт-под-ключ-шаблон.xlsx'
CSV = f'{ROOT}/памятки/смета-источники/ставки-минск-2026.csv'

F = 'Arial'
fn = Font(name=F, size=10)
fb = Font(name=F, size=10, bold=True)
fh = Font(name=F, size=10, bold=True, color='FFFFFF')
fin = Font(name=F, size=10, color='0000FF')            # ввод
flink = Font(name=F, size=10, color='008000')           # ссылка на другой лист
ftitle = Font(name=F, size=14, bold=True)
fnote = Font(name=F, size=9, italic=True, color='666666')
fill_h = PatternFill('solid', fgColor='2C2C2C')
fill_sec = PatternFill('solid', fgColor='F5EFE2')
fill_in = PatternFill('solid', fgColor='FFFF99')
fill_tot = PatternFill('solid', fgColor='F5E2BB')
thin = Side(style='thin', color='CBBF9F')
box = Border(left=thin, right=thin, top=thin, bottom=thin)
NUM = '#,##0.00'
NUM0 = '#,##0'
PCT = '0.0%'

wb = Workbook()

# ---------------------------------------------------------------- Параметры
P = wb.active
P.title = 'Параметры'
P.column_dimensions['A'].width = 52
P.column_dimensions['B'].width = 14
P.column_dimensions['C'].width = 70
P['A1'] = 'Параметры расчёта'; P['A1'].font = ftitle
params = [
    ('Курс НБ РБ, BYN за €', 3.4487, 'api.nbrb.by, 27.09.2026. Для справочного евро-эквивалента.'),
    ('Запас на смеси и штучные материалы', 0.10, 'Практика: смеси 5–10 %, холст 10 %. Применяется к строке «Материалы» сметы.'),
    ('Запас на напольное покрытие (LVT палуба)', 0.07, '5–7 % палуба, 10–12 % ёлка/диагональ. Уже учтён в цене материала узла LVT.'),
    ('Непредвиденные, % от работ и материалов', 0.05, 'Официально 1,5 % (пост. № 116 п. 33.5, текущий ремонт); вторичка 5–10 %.'),
    ('Накладные и прибыль подрядчика, % от работ', 0.20, 'Компании 15–30 % к работам; бригады 0–10 %. Официально ОХР 83,83 % + ПП 45,82 %×1,115 от ФОТ (пост. № 146).'),
    ('Доставка и подъём материалов, BYN (фикс)', 400, 'Газель 160–220/рейс, подъём 1–1,7 руб./место·этаж без лифта.'),
    ('Стоимость чел.-ч 4 разряда (пост. № 145), BYN', 16.96, 'С 01.01.2026. Справочно для ресурсного расчёта.'),
    ('Полная «официальная» стоимость чел.-ч, BYN', '=B8*(1+0.8383+0.4582*1.115+0.34)', '16,96 × (1 + ОХР 83,83 % + ПП 45,82 %×1,115 + страховые 34 %) ≈ 45,6.'),
]
P['A2'] = 'Показатель'; P['B2'] = 'Значение'; P['C2'] = 'Источник / пояснение'
for c in 'ABC':
    P[f'{c}2'].font = fh; P[f'{c}2'].fill = fill_h
for i, (name, val, note) in enumerate(params, start=3):
    P[f'A{i}'] = name; P[f'A{i}'].font = fn
    P[f'B{i}'] = val
    P[f'B{i}'].font = fin if not str(val).startswith('=') else fn
    if not str(val).startswith('='):
        P[f'B{i}'].fill = fill_in
    P[f'B{i}'].number_format = PCT if isinstance(val, float) and val < 1 else NUM
    P[f'C{i}'] = note; P[f'C{i}'].font = fnote
    P[f'C{i}'].alignment = Alignment(wrap_text=True, vertical='top')
P['A12'] = 'Жёлтые ячейки с синим шрифтом — ввод. Чёрные — формулы, зелёные — ссылки на другой лист.'
P['A12'].font = fnote
PR = {  # адреса параметров
    'rate': "Параметры!$B$3", 'res_mat': "Параметры!$B$4", 'unf': "Параметры!$B$6",
    'ovh': "Параметры!$B$7", 'deliv': "Параметры!$B$8",
}

# ---------------------------------------------------------------- Ставки
S = wb.create_sheet('Ставки')
hdr = ['Код', 'Раздел', 'Работа', 'Ед.', 'Мин', 'Типично', 'Макс', 'С материалом', 'Примечание']
widths = [12, 14, 58, 10, 8, 10, 8, 13, 40]
for i, (h, w) in enumerate(zip(hdr, widths), start=1):
    c = S.cell(row=1, column=i, value=h); c.font = fh; c.fill = fill_h
    S.column_dimensions[get_column_letter(i)].width = w
sec_code = {'демонтаж': 'D', 'стены': 'W', 'потолки': 'C', 'полы': 'F', 'электрика': 'E',
            'сантехника': 'S', 'плитка': 'T', 'чистовая': 'X', 'сопутствующее': 'O', 'комплекс': 'K'}
counters = {}
code_of = {}
with open(CSV, encoding='utf-8') as f:
    rows = list(csv.DictReader(f, delimiter=';'))
for r_i, r in enumerate(rows, start=2):
    sc = sec_code[r['раздел']]
    counters[sc] = counters.get(sc, 0) + 1
    code = f'{sc}{counters[sc]:02d}'
    code_of[r['работа']] = code
    vals = [code, r['раздел'], r['работа'], r['ед'], float(r['мин']), float(r['типично']),
            float(r['макс']), r['с_материалом'], r['примечание']]
    for c_i, v in enumerate(vals, start=1):
        c = S.cell(row=r_i, column=c_i, value=v); c.font = fn
        if c_i in (5, 6, 7):
            c.number_format = NUM; c.font = fin
S.freeze_panes = 'A2'
S_LAST = len(rows) + 1
S.cell(row=S_LAST + 2, column=1, value='Источник: документы/памятки/смета-источники/01-цены-работы.md, '
       'прайсы минских компаний, срез 27.09.2026. Столбец «Типично» — медиана; синие числа можно править.').font = fnote

# ---------------------------------------------------------------- Узлы (материал на единицу)
U = wb.create_sheet('Узлы')
uh = ['Код узла', 'Узел', 'Ед.', 'Состав и расход на единицу', 'Материал, BYN/ед.', 'Код ставки работы', 'Работа, BYN/ед.', 'Источник цен']
uw = [12, 46, 8, 70, 14, 14, 14, 30]
for i, (h, w) in enumerate(zip(uh, uw), start=1):
    c = U.cell(row=1, column=i, value=h); c.font = fh; c.fill = fill_h
    U.column_dimensions[get_column_letter(i)].width = w
# (код, узел, ед, состав, материал, работа по ставке)
nodes = [
    ('N01', 'Демонтаж обоев', 'м²', 'вода, размывка; без материала', 0, 'Обои'),
    ('N02', 'Демонтаж плинтуса', 'м.п.', 'без материала', 0, None),
    ('N03', 'Вынос мусора, мешок', 'мешок', 'мешок 0,6–0,8 руб.', 0.7, 'Вынос мусора (мешок, с лифтом)'),
    ('N04', 'Вывоз мусора, Газель', 'рейс', 'услуга с грузчиками', 0, 'Газель 4–5 м3, рейс'),
    ('N05', 'Перегородка газосиликат 100 мм', 'м²', '6,4 блока (0,1 м³ × 174 поддоном) + клей 3 кг × 0,42 + анкеры, сетка', 22, 'Перегородка газосиликат до 150 мм'),
    ('N06', 'Перегородка ПГП 80 мм', 'м²', '3 плиты × 15,35 + клей 1,5 кг + прокладка, анкеры', 49, 'Перегородка ПГП 80 мм'),
    ('N07', 'Штукатурка гипсовая 15 мм по маякам (новые перегородки)', 'м²', 'Rotband/ilmax 12,8 кг × 0,63 + грунт 0,12 кг + маяки 0,9 м + сетка на стыках 0,2 м²', 9.5, 'Штукатурка стен гипс по маякам до 20–30 мм'),
    ('N08', 'Откосы штукатурные', 'м.п.', 'смесь ≈ 4 кг + уголок 1 м', 4.5, 'Откосы штукатурные'),
    ('N09', 'Шпаклёвка стен под покраску Q3 (по существующей штукатурке/бетону)', 'м²', 'старт 2,2 кг × 1,0 + финиш 1,1 кг × 1,5 + грунт 0,4 кг × 4 + сетка стыков 0,3 м² + шкурка 0,12 м²', 8.3, 'Шпаклёвка под покраску (комплекс, без стеклохолста)'),
    ('N10', 'Стеклохолст 40 г/м² на клей', 'м²', 'холст 1,1 м² × 1,5 + клей 0,25 кг × 6', 3.2, 'Стеклохолст (поклейка)'),
    ('N11', 'Шпаклёвка потолка под покраску Q3', 'м²', 'как N09, труд ×1,17', 8.3, None),
    ('N12', 'Окраска стен 2 слоя + грунт', 'м²', 'краска 0,3 л × 15 (Alpina/Condor) + грунт 0,1 л × 4 + скотч, плёнка', 5.4, 'Покраска стен 2 слоя'),
    ('N13', 'Окраска потолка 2 слоя + грунт', 'м²', 'как N12', 5.4, 'Покраска потолка 2 слоя'),
    ('N14', 'Подготовка существующей стяжки: шлифовка, пылесос, ремонт трещин', 'м²', 'ремсостав, диски ≈ 0,5', 0.5, None),
    ('N15', 'Самонивелир 5 мм с грунтом ×2 и демпфером', 'м²', 'смесь 9,5 кг × 0,8 (CN 68 / ilmax 6705) + грунт 0,25 кг × 4 + демпферная лента', 9.0, 'Наливной пол / самонивелир до 15 мм'),
    ('N16', 'Кварцвинил клеевой, палуба (с запасом 7 %)', 'м²', 'LVT 53 × 1,07 (Alpine Floor 48–51, FineFloor 59) + клей 0,3 кг × 10 (оценка)', 60, 'Кварцвинил клеевой'),
    ('N17', 'Плинтус МДФ', 'м.п.', '1,05 м × 5,5 + крепёж, герметик', 6.5, 'Плинтус МДФ/дюрополимер'),
    ('N18', 'Порожек', 'шт', 'алюминиевый порожек 15–30', 22, 'Порожек/компенсационный шов'),
    ('N19', 'Электроточка полная (штроба + 6 м кабеля + подрозетник + механизм)', 'точка', 'ВВГнг-LS 6 м × 4 + гофра 6 м × 0,55 + подрозетник 1 + механизм 10', 40, 'Полная точка (штроба+кабель+подрозетник+механизм)'),
    ('N20', 'Щит квартирный 24 модуля, IEK/ABB', 'шт', 'корпус 58 + 12 автоматов × 7–24 + 4 УЗО/дифа × 54–168', 700, 'Щит квартирный собранный'),
    ('N21', 'Точка водоснабжения PPR/PEX', 'точка', 'труба 3–4 м + фитинги + кран', 20, 'Точка водоснабжения'),
    ('N22', 'Точка канализации', 'точка', 'труба 50 2 м × 4,2 + фитинги', 12, 'Точка канализации'),
    ('N23', 'Гидроизоляция цементная 2 слоя (CR 65)', 'м²', '3 кг × 1,84 + лента 0,6 м × 5', 8.5, 'Гидроизоляция обмазочная 2 слоя'),
    ('N24', 'Плитка на стены 30×60 (плитка 30 руб./м²)', 'м²', 'клей 4 кг × 0,6 + затирка 0,4 кг × 5 + грунт + плитка 30 × 1,08', 37, 'Плитка керамическая стандарт'),
    ('N25', 'Керамогранит 60×60 на пол (плитка 55 руб./м²)', 'м²', 'клей 5 кг × 0,6 + затирка 0,5 кг × 5 + СВП + грунт + плитка 55 × 1,08', 66, 'Керамогранит средний формат'),
    ('N26', 'Дверь межкомнатная, установка блока', 'шт', 'пена, крепёж ≈ 15; само полотно с коробкой 232–890 — отдельной строкой', 15, 'Дверь межкомнатная установка'),
    ('N27', 'Уборка после ремонта', 'м²', 'услуга', 0, 'Уборка после ремонта'),
]
for r_i, (code, name, unit, comp, mat, rate_name) in enumerate(nodes, start=2):
    U.cell(row=r_i, column=1, value=code).font = fn
    U.cell(row=r_i, column=2, value=name).font = fn
    U.cell(row=r_i, column=3, value=unit).font = fn
    c = U.cell(row=r_i, column=4, value=comp); c.font = fnote; c.alignment = Alignment(wrap_text=True, vertical='top')
    c = U.cell(row=r_i, column=5, value=mat); c.font = fin; c.fill = fill_in; c.number_format = NUM
    if rate_name:
        rc = code_of[rate_name]
        U.cell(row=r_i, column=6, value=rc).font = fn
        c = U.cell(row=r_i, column=7, value=f'=INDEX(Ставки!$F$2:$F${S_LAST},MATCH(F{r_i},Ставки!$A$2:$A${S_LAST},0))')
        c.font = flink; c.number_format = NUM
    else:
        # ставки, которых нет в прайсах: ввод вручную
        manual = {'N02': 3, 'N11': 37, 'N14': 4}
        U.cell(row=r_i, column=6, value='ввод').font = fnote
        c = U.cell(row=r_i, column=7, value=manual[code]); c.font = fin; c.fill = fill_in; c.number_format = NUM
    U.cell(row=r_i, column=8, value='розница Минск 27.09.2026, 02-цены-материалы.md').font = fnote
U_LAST = len(nodes) + 1
U.freeze_panes = 'A2'
U.cell(row=U_LAST + 2, column=1, value='Материал на единицу — расчёт по розничным ценам и расходу из техкарт '
       '(04-техкарты-узлов.md), без запаса. Запас добавляется в смете параметром. Цены плитки и LVT в составе — условные, замените на выбранные.').font = fnote

# ---------------------------------------------------------------- Объёмы
V = wb.create_sheet('Объёмы')
V['A1'] = 'Ведомость объёмов по помещениям (пример — квартира 55 м², высота 2,65; замените на свои замеры)'
V['A1'].font = fb
vh = ['Помещение', 'Длина, м', 'Ширина, м', 'Высота, м', 'Пол, м²', 'Периметр, м',
      'Стены брутто, м²', 'Проёмы, м²', 'Стены нетто, м²', 'Потолок, м²', 'Откосы, м.п.', 'Плинтус, м.п.', 'Примечание']
vw = [18, 10, 10, 10, 10, 12, 14, 11, 14, 12, 12, 13, 40]
for i, (h, w) in enumerate(zip(vh, vw), start=1):
    c = V.cell(row=2, column=i, value=h); c.font = fh; c.fill = fill_h
    c.alignment = Alignment(wrap_text=True, vertical='center')
    V.column_dimensions[get_column_letter(i)].width = w
rooms = [
    ('Гостиная', 5.2, 3.6, 2.65, 3.6, 5.0, 4.6, 'стены шпаклёвка, пол LVT'),
    ('Спальня', 4.0, 3.2, 2.65, 3.6, 5.0, 4.6, 'стены шпаклёвка, пол LVT'),
    ('Кухня', 3.4, 3.0, 2.65, 3.6, 5.0, 3.6, 'стены шпаклёвка, пол LVT; фартук отдельно'),
    ('Коридор', 4.5, 1.4, 2.65, 7.2, 0, 4.0, 'четыре дверных проёма'),
    ('Санузел', 2.2, 1.8, 2.65, 1.6, 0, 0, 'стены плитка, пол керамогранит — считаются в смете отдельно'),
]
for r_i, (nm, L, W, H, op, otk, minus_pl, note) in enumerate(rooms, start=3):
    V.cell(row=r_i, column=1, value=nm).font = fn
    for c_i, v in zip((2, 3, 4), (L, W, H)):
        c = V.cell(row=r_i, column=c_i, value=v); c.font = fin; c.fill = fill_in; c.number_format = NUM
    V.cell(row=r_i, column=5, value=f'=B{r_i}*C{r_i}').number_format = NUM
    V.cell(row=r_i, column=6, value=f'=2*(B{r_i}+C{r_i})').number_format = NUM
    V.cell(row=r_i, column=7, value=f'=F{r_i}*D{r_i}').number_format = NUM
    c = V.cell(row=r_i, column=8, value=op); c.font = fin; c.fill = fill_in; c.number_format = NUM
    V.cell(row=r_i, column=9, value=f'=G{r_i}-H{r_i}').number_format = NUM
    V.cell(row=r_i, column=10, value=f'=E{r_i}').number_format = NUM
    c = V.cell(row=r_i, column=11, value=otk); c.font = fin; c.fill = fill_in; c.number_format = NUM
    c = V.cell(row=r_i, column=12, value=f'=F{r_i}-{minus_pl}'); c.number_format = NUM
    V.cell(row=r_i, column=13, value=note).font = fnote
V_LAST = 2 + len(rooms)
tr = V_LAST + 1
V.cell(row=tr, column=1, value='Итого').font = fb
for col in (5, 7, 8, 9, 10, 11, 12):
    L = get_column_letter(col)
    c = V.cell(row=tr, column=col, value=f'=SUM({L}3:{L}{V_LAST})'); c.font = fb; c.number_format = NUM; c.fill = fill_tot
# итоги без санузла (для шпаклёвки/LVT)
tr2 = tr + 1
V.cell(row=tr2, column=1, value='Итого без санузла').font = fb
for col in (5, 9, 10, 12):
    L = get_column_letter(col)
    c = V.cell(row=tr2, column=col, value=f'=SUM({L}3:{L}{V_LAST-1})'); c.font = fb; c.number_format = NUM; c.fill = fill_tot
V.cell(row=tr2 + 2, column=1, value='Проёмы вычитаются по наружному обводу коробок (окно ≈ 1,5×1,4 = 2,1 м², дверь 0,9×2,1 ≈ 1,9 м²). '
       'Откосы считаются отдельно в м.п. Плинтус = периметр минус дверные проёмы. Для микроцемента действуют правила обмера из CLAUDE.md.').font = fnote
VOL = {
    'walls': f"Объёмы!$I${tr2}", 'floor': f"Объёмы!$E${tr2}", 'ceil': f"Объёмы!$J${tr2}",
    'plinth': f"Объёмы!$L${tr2}", 'otk': f"Объёмы!$K${tr}", 'floor_all': f"Объёмы!$E${tr}",
}

# ---------------------------------------------------------------- Смета
M = wb.create_sheet('Смета', 0)
M['A1'] = 'ЛОКАЛЬНАЯ СМЕТА на ремонт квартиры «под ключ» — шаблон с примером'
M['A1'].font = ftitle
M['A2'] = ('Объект: ПРИМЕР, квартира 55 м², Минск. Профиль: штукатурка только новых перегородок, '
           'шпаклёвка Q3 по существующим стенам, самонивелир 5 мм + клеевой кварцвинил. '
           'Цены: розница Минска и ставки «типично», срез 27.09.2026, BYN без НДС.')
M['A2'].font = fnote
M['A3'] = ('Как пользоваться: объёмы (жёлтые ячейки) — с листа «Объёмы» или вручную; цены тянутся по коду узла '
           'с листа «Узлы» (материал) и «Ставки» (работа). Класс отделки, объёмы и цены согласовать с заказчиком '
           'письменно до старта (ст. 663 ГК, ст. 34 ЗПП).')
M['A3'].font = fnote
mh = ['№', 'Код узла', 'Наименование работ и затрат', 'Ед.', 'Объём', 'Работа, BYN/ед.', 'Материал, BYN/ед.',
      'Работа, BYN', 'Материал, BYN', 'Всего, BYN', 'Обоснование / примечание']
mw = [5, 9, 62, 8, 10, 13, 14, 13, 14, 14, 46]
HR = 5
for i, (h, w) in enumerate(zip(mh, mw), start=1):
    c = M.cell(row=HR, column=i, value=h); c.font = fh; c.fill = fill_h
    c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    M.column_dimensions[get_column_letter(i)].width = w
M.row_dimensions[HR].height = 30
M.freeze_panes = f'A{HR+1}'

# структура: (раздел, [(код узла, объём или формула, примечание)])
sections = [
    ('1. Подготовка и демонтаж', [
        ('N01', f"={VOL['walls']}", 'снятие старых обоев со всех существующих стен'),
        ('N02', f"={VOL['plinth']}", ''),
        ('N03', 40, 'оценка 0,7 мешка на м² при косметическом демонтаже'),
        ('N04', 1, 'Газель 4–5 м³'),
    ]),
    ('2. Перегородки и штукатурка новых стен', [
        ('N05', 12, 'новая перегородка 4,5×2,65 газосиликат 100 мм (пример)'),
        ('N07', 24, 'штукатурка обеих сторон новой перегородки; ПГП/ГКЛ не штукатурятся'),
        ('N08', f"={VOL['otk']}", 'оконные и дверные откосы'),
    ]),
    ('3. Шпаклёвка и окраска (стены — по существующей штукатурке, класс «улучшенная», Q3)', [
        ('N09', f"={VOL['walls']}+24", 'существующие стены + новая перегородка после штукатурки'),
        ('N10', f"={VOL['walls']}+24+{VOL['ceil']}", 'стеклохолст на стены и потолки под покраску'),
        ('N11', f"={VOL['ceil']}", 'потолки под покраску; если натяжные — обнулить'),
        ('N12', f"={VOL['walls']}+24", ''),
        ('N13', f"={VOL['ceil']}", ''),
    ]),
    ('4. Полы: самонивелир + клеевой кварцвинил', [
        ('N14', f"={VOL['floor']}", 'обязательно: CM-тест влажности ≤ 2 %, ровность ≤ 2 мм/2 м — акт'),
        ('N15', f"={VOL['floor']}", 'средняя толщина 5 мм; при перепадах 8–10 мм ×1,6 к материалу'),
        ('N16', f"={VOL['floor']}", 'сушка самонивелира 7 суток до укладки'),
        ('N17', f"={VOL['plinth']}", ''),
        ('N18', 4, 'порожки в дверных проёмах'),
    ]),
    ('5. Электрика', [
        ('N19', 45, '≈ 0,8 точки на м² квартиры; уточнить по проекту электрики'),
        ('N20', 1, ''),
    ]),
    ('6. Сантехника и санузел', [
        ('N21', 8, 'ХВС/ГВС: раковина, ванна/душ, унитаз, стиральная, кухня'),
        ('N22', 4, ''),
        ('N23', 6, 'пол санузла + заход на стены 300 мм'),
        ('N24', 22, 'стены санузла; цена плитки 30 руб./м² условная'),
        ('N25', 4, 'пол санузла; керамогранит 55 руб./м² условный'),
    ]),
    ('7. Двери и завершение', [
        ('N26', 4, 'сами дверные блоки (232–890 руб.) — добавить строкой закупки'),
        ('N27', f"={VOL['floor_all']}", ''),
    ]),
]
node_row = {code: i + 2 for i, (code, *_ ) in enumerate(nodes)}
r = HR + 1
n = 0
sec_total_rows = []
for sec_name, items in sections:
    c = M.cell(row=r, column=3, value=sec_name); c.font = fb
    for col in range(1, 12):
        M.cell(row=r, column=col).fill = fill_sec
    r += 1
    first = r
    for code, vol, note in items:
        n += 1
        nr = node_row[code]
        M.cell(row=r, column=1, value=n).font = fn
        M.cell(row=r, column=2, value=code).font = fn
        c = M.cell(row=r, column=3, value=f'=INDEX(Узлы!$B$2:$B${U_LAST},MATCH(B{r},Узлы!$A$2:$A${U_LAST},0))'); c.font = flink
        c = M.cell(row=r, column=4, value=f'=INDEX(Узлы!$C$2:$C${U_LAST},MATCH(B{r},Узлы!$A$2:$A${U_LAST},0))'); c.font = flink
        c = M.cell(row=r, column=5, value=vol); c.number_format = NUM
        if isinstance(vol, str):
            c.font = flink
        else:
            c.font = fin; c.fill = fill_in
        c = M.cell(row=r, column=6, value=f'=INDEX(Узлы!$G$2:$G${U_LAST},MATCH(B{r},Узлы!$A$2:$A${U_LAST},0))'); c.font = flink; c.number_format = NUM
        c = M.cell(row=r, column=7, value=f'=INDEX(Узлы!$E$2:$E${U_LAST},MATCH(B{r},Узлы!$A$2:$A${U_LAST},0))'); c.font = flink; c.number_format = NUM
        M.cell(row=r, column=8, value=f'=E{r}*F{r}').number_format = NUM
        M.cell(row=r, column=9, value=f'=E{r}*G{r}').number_format = NUM
        M.cell(row=r, column=10, value=f'=H{r}+I{r}').number_format = NUM
        M.cell(row=r, column=11, value=note).font = fnote
        for col in range(1, 12):
            M.cell(row=r, column=col).border = box
        r += 1
    last = r - 1
    M.cell(row=r, column=3, value=f'Итого по разделу').font = fb
    for col, L in ((8, 'H'), (9, 'I'), (10, 'J')):
        c = M.cell(row=r, column=col, value=f'=SUM({L}{first}:{L}{last})'); c.font = fb; c.number_format = NUM; c.fill = fill_tot
    sec_total_rows.append(r)
    r += 2

# итоги
r += 1
def total_line(label, work=None, mat=None, tot=None, bold=True, note=''):
    global r
    M.cell(row=r, column=3, value=label).font = fb if bold else fn
    if work is not None:
        c = M.cell(row=r, column=8, value=work); c.number_format = NUM; c.font = fb if bold else fn
    if mat is not None:
        c = M.cell(row=r, column=9, value=mat); c.number_format = NUM; c.font = fb if bold else fn
    if tot is not None:
        c = M.cell(row=r, column=10, value=tot); c.number_format = NUM; c.font = fb if bold else fn; c.fill = fill_tot
    if note:
        M.cell(row=r, column=11, value=note).font = fnote
    r += 1

sum_h = '+'.join(f'H{x}' for x in sec_total_rows)
sum_i = '+'.join(f'I{x}' for x in sec_total_rows)
R_BASE = r
total_line('Итого прямые затраты', f'={sum_h}', f'={sum_i}', f'=H{r}+I{r}')
R_RES = r
total_line('Запас на материалы', None, f'=I{R_BASE}*{PR["res_mat"]}', f'=I{r}', False, 'параметр «Запас на смеси»; в LVT запас уже учтён')
R_OVH = r
total_line('Накладные и прибыль подрядчика', f'=H{R_BASE}*{PR["ovh"]}', None, f'=H{r}', False, 'параметр; официально — % от ФОТ по пост. № 146')
R_DEL = r
total_line('Доставка и подъём материалов', None, f'={PR["deliv"]}', f'=I{r}', False, 'параметр (фикс)')
R_UNF = r
total_line('Непредвиденные', None, None, f'=(J{R_BASE}+J{R_RES}+J{R_OVH}+J{R_DEL})*{PR["unf"]}', False, 'параметр; официально 1,5 % для текущего ремонта')
R_TOT = r
total_line('ИТОГО К ОПЛАТЕ, BYN', f'=H{R_BASE}+H{R_OVH}', f'=I{R_BASE}+I{R_RES}+I{R_DEL}', f'=J{R_BASE}+J{R_RES}+J{R_OVH}+J{R_DEL}+J{R_UNF}')
M.cell(row=R_TOT, column=3).font = Font(name=F, size=12, bold=True)
M.cell(row=R_TOT, column=10).font = Font(name=F, size=12, bold=True)
total_line('Справочно: эквивалент в €', None, None, f'=J{R_TOT}/{PR["rate"]}', False, 'по курсу НБ РБ из «Параметров»; только как валютная оговорка договора')
total_line('Справочно: на м² общей площади, BYN', None, None, f'=J{R_TOT}/{VOL["floor_all"]}', False, 'сравнить с рыночным диапазоном капремонта 350–600 (работа) / 700–1 100 (с материалами)')
total_line('Справочно: доля работ в итоге', None, None, f'=H{R_TOT}/J{R_TOT}', False, 'типично 40–60 %')
M.cell(row=r - 1, column=10).number_format = PCT
r += 1
notes = [
    'Пример иллюстративный: объёмы взяты с листа «Объёмы» для условной квартиры 55 м². Для реального объекта заменить замеры, состав разделов и цены материалов (плитка, LVT, двери, сантехприборы).',
    'Не включено: сами дверные блоки, сантехприборы, светильники, кухня, натяжные потолки, микроцемент (считается по модели студии из CLAUDE.md / costs.py).',
    'Ставки «типично» — медиана прайсов минских компаний с договором; агрегаторы частников дают на 30–50 % ниже, см. «Ставки» (мин/макс).',
    'Гарантия на пол возможна только при протоколе влажности основания CM ≤ 2,0 % и ровности ≤ 2 мм на 2 м (акт скрытых работ).',
    'Источники и техкарты: документы/памятки/смета-ремонт-под-ключ-Минск.md и смета-источники/.',
]
for t in notes:
    M.cell(row=r, column=3, value=t).font = fnote
    r += 1

M.sheet_view.zoomScale = 90
os.makedirs(os.path.dirname(OUT), exist_ok=True)
wb.save(OUT)
print('saved', OUT, 'rows', r)
