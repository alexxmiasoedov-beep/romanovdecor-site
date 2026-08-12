# -*- coding: utf-8 -*-
"""Формирует PDF-запрос в Алвентус по цементной линейке (оптимизированный перечень)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, KeepTogether, HRFlowable,
)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DJ", FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJ-B", FONT_DIR + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJ-B",
                              italic="DJ", boldItalic="DJ-B")

INK = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#5a5a5a")
RULE = colors.HexColor("#c8c8c8")
BAND = colors.HexColor("#eef1f4")

S = {
    "head": ParagraphStyle("head", fontName="DJ-B", fontSize=10.5, leading=14, textColor=INK),
    "headr": ParagraphStyle("headr", fontName="DJ", fontSize=9, leading=13,
                            textColor=MUTED, alignment=TA_RIGHT),
    "title": ParagraphStyle("title", fontName="DJ-B", fontSize=14.5, leading=19,
                            textColor=INK, spaceBefore=2, spaceAfter=10),
    "body": ParagraphStyle("body", fontName="DJ", fontSize=9.5, leading=14,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=7),
    "h2": ParagraphStyle("h2", fontName="DJ-B", fontSize=11, leading=15,
                         textColor=INK, spaceBefore=13, spaceAfter=6),
    "th": ParagraphStyle("th", fontName="DJ-B", fontSize=8.2, leading=11, textColor=INK),
    "td": ParagraphStyle("td", fontName="DJ", fontSize=8.2, leading=11, textColor=INK),
    "tdn": ParagraphStyle("tdn", fontName="DJ", fontSize=8.2, leading=11, textColor=MUTED),
    "sig": ParagraphStyle("sig", fontName="DJ", fontSize=9.5, leading=14.5, textColor=INK),
}

OUT = "/home/user/romanovdecor-site/документы/Запрос-Алвентус-цементная-линейка.pdf"
TITLE = "Запрос коммерческого предложения и технической документации на сырьё"


def rule(sb=4, sa=8):
    return HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=sb, spaceAfter=sa)


def table(rows):
    data = [[Paragraph("№", S["th"]),
             Paragraph("Материал", S["th"]),
             Paragraph("Требуемые характеристики", S["th"]),
             Paragraph("Что прошу уточнить", S["th"])]]
    for n, pos, spec, ask in rows:
        data.append([Paragraph(str(n), S["tdn"]),
                     Paragraph(pos, S["td"]),
                     Paragraph(spec, S["td"]),
                     Paragraph(ask, S["td"])])
    t = Table(data, colWidths=[8 * mm, 38 * mm, 52 * mm, 72 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, RULE),
        ("INNERGRID", (0, 1), (-1, -1), 0.35, colors.HexColor("#e2e2e2")),
        ("BOX", (0, 0), (-1, -1), 0.6, RULE),
    ]))
    return t


def numbered(items):
    t = Table([[Paragraph(f"{i}.", S["tdn"]), Paragraph(x, S["td"])]
               for i, x in enumerate(items, 1)], colWidths=[8 * mm, 162 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]))
    return t


def header():
    hdr = Table([[
        Paragraph("Индивидуальный предприниматель<br/>"
                  "<font size=12>Мясоедов Алексей Владимирович</font>", S["head"]),
        Paragraph("Минский район, д. Копище,<br/>ул. Авиационная, 27–116<br/>"
                  "+375 33 628-04-86<br/>miasoedov95@gmail.com", S["headr"]),
    ]], colWidths=[100 * mm, 70 * mm])
    hdr.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return hdr


COMMON_REQ = [
    "Точное торговое наименование и завод-изготовитель.",
    "Цену за килограмм при трёх объёмах: до 100 кг, до 500 кг, от 1 тонны.",
    "Минимальную партию отгрузки и вид фасовки.",
    "Срок поставки: со склада и под заказ отдельно.",
    "Техническое описание (TDS) и паспорт безопасности (SDS) — файлами.",
    "Возможность отгрузки пробной партии 5–25 кг.",
]

ORG_Q = [
    "Есть ли у вас технический специалист, к которому можно обращаться по "
    "вопросам совместимости и дозировок?",
    "Отпускаете ли образцы бесплатно или по символической цене?",
    "Какие позиции складские, а какие под заказ — с минимальным объёмом и сроком.",
    "Работаете ли с индивидуальными предпринимателями или только с юридическими лицами?",
    "Условия оплаты: предоплата или возможна отсрочка?",
]

SECTIONS = [
    ("1. Вяжущие", [
        (1, "Портландцемент белый",
         "CEM I 52,5 R, белизна не менее 85 %",
         "Белизна и метод её измерения; содержание C<sub>3</sub>A; стабильность "
         "оттенка от партии к партии; завод-изготовитель."),
        (2, "Цемент глинозёмистый",
         "Al<sub>2</sub>O<sub>3</sub> около 40 %, светлый",
         "Фактическое содержание Al<sub>2</sub>O<sub>3</sub> и "
         "Fe<sub>2</sub>O<sub>3</sub>; тонкость помола по Блейну; марка."),
        (3, "Ангидрит II тонкомолотый",
         "синтетический",
         "Чистота по CaSO<sub>4</sub>; тонкость помола; природный или синтетический."),
        (4, "Метакаолин",
         "белый",
         "Белизна; d50; остаток на сите 45 мкм; пуццолановая активность."),
    ]),
    ("2. Заполнители", [
        (5, "Песок кварцевый",
         "фракция 0,1–0,3 мм",
         "Содержание SiO<sub>2</sub> и Fe<sub>2</sub>O<sub>3</sub>; влажность; "
         "форма зерна — окатанное или дроблёное; месторождение."),
        (6, "Песок кварцевый",
         "фракция 0,06–0,15 мм",
         "То же, что по позиции 5."),
        (7, "Мука кварцевая",
         "d50 около 45 мкм",
         "<b>d10 / d50 / d90 по лазерной дифракции</b>; доля частиц мельче "
         "4 мкм; маслоёмкость."),
        (8, "Микрокальцит",
         "фракция 2–20 мкм, белизна не менее 93",
         "d50 и верхний срез; белизна и метод её измерения; маслоёмкость."),
    ]),
    ("3. Добавки в сухую смесь", [
        (9, "Эфир целлюлозы MHEC",
         "вязкость 20 000–30 000 мПа·с",
         "Метод и концентрация замера вязкости; степень замещения; влияние на "
         "сроки схватывания; есть ли марки с отложенным растворением."),
        (10, "Суперпластификатор PCE",
         "порошковый",
         "Содержание активного вещества; воздухововлечение; <b>совместимость с "
         "глинозёмистым цементом</b>."),
        (11, "Кислота винная",
         "—",
         "Квалификация и чистота."),
        (12, "Пеногаситель порошковый",
         "<b>без силикона</b>",
         "Химическая основа. Силиконовые не подходят: покрытие перекрывается "
         "несколькими слоями и лакируется, миграция силикона разрушает "
         "межслойную адгезию. Прошу подтвердить отсутствие силикона в "
         "предлагаемой марке."),
    ]),
    ("4. Жидкость затворения", [
        (13, "Дисперсия стирол-акриловая или акриловая",
         "сухой остаток 50–58 %; T<sub>g</sub> от −10 до +5 °C; MFFT 0–5 °C; "
         "размер частиц 150–350 нм; pH 7–9,5",
         "<b>Предназначена ли производителем для двухкомпонентных цементных "
         "составов</b>; есть ли данные по устойчивости в насыщенном растворе "
         "Ca(OH)<sub>2</sub>; тип эмульгаторной системы, APEO-free; вязкость."),
        (14, "Пеногаситель жидкий для водных систем",
         "—",
         "Химическая основа; наличие минерального масла; наличие силикона."),
        (15, "Биоцид внутритарный",
         "стойкость при pH 8–9,5",
         "Действующее вещество — BIT, CIT/MIT или смесь; рекомендуемая дозировка."),
    ]),
    ("5. Прочее", [
        (16, "Сетка стеклотканевая",
         "щёлочестойкая, 145–160 г/м<super>2</super>",
         "Если позиция есть в ассортименте — размер ячейки и ширина рулона."),
    ]),
]

INTRO = [
    "ИП Мясоедов Алексей Владимирович, г. Минск. Организуем производство "
    "тонкослойных декоративно-защитных покрытий для полов и стен на цементном "
    "вяжущем. Материал двухкомпонентный: сухая смесь и жидкость затворения на "
    "полимерной дисперсии.",
    "Находимся на стадии отработки рецептуры. Прошу дать коммерческое "
    "предложение и техническую документацию по перечню ниже. Если какой-то "
    "позиции нет в ассортименте — достаточно это отметить.",
]

FOOTER = ("Отдельно прошу подтвердить, <b>гарантируется ли поставка одной и той же "
          "марки одного завода-изготовителя на постоянной основе</b>, с паспортом "
          "качества на каждую партию. Для нас это ключевой критерий выбора "
          "поставщика: рецептура калибруется под конкретное сырьё, и смена завода "
          "означает её переработку.")


def main():
    story = [header(), rule(2, 12), Paragraph(TITLE, S["title"])]
    story.append(Paragraph("Добрый день!", S["body"]))
    for p in INTRO:
        story.append(Paragraph(p, S["body"]))
    story.append(Paragraph("Что прошу указать по каждой позиции", S["h2"]))
    story.append(numbered(COMMON_REQ))
    for name, rows in SECTIONS:
        story.append(Paragraph(name, S["h2"]))
        story.append(table(rows))
    story.append(Spacer(1, 10))
    story.append(Paragraph(FOOTER, S["body"]))
    story.append(Paragraph("Организационные вопросы", S["h2"]))
    story.append(numbered(ORG_Q))
    story.append(KeepTogether([
        Spacer(1, 10), rule(0, 8),
        Paragraph("С уважением,<br/><b>Мясоедов Алексей Владимирович</b><br/>"
                  "индивидуальный предприниматель<br/>"
                  "+375 33 628-04-86 &nbsp;·&nbsp; miasoedov95@gmail.com", S["sig"]),
    ]))

    def decorate(canvas, doc):
        canvas.saveState()
        canvas.setFont("DJ", 7.8)
        canvas.setFillColor(MUTED)
        canvas.drawString(20 * mm, 12 * mm, "ИП Мясоедов А. В.  ·  запрос сырья")
        canvas.drawRightString(A4[0] - 20 * mm, 12 * mm, "%d" % doc.page)
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.4)
        canvas.line(20 * mm, 15.5 * mm, A4[0] - 20 * mm, 15.5 * mm)
        canvas.restoreState()

    doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                          topMargin=18 * mm, bottomMargin=20 * mm,
                          title=TITLE, author="Мясоедов Алексей Владимирович",
                          subject="Запрос коммерческого предложения на сырьё")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=decorate)])
    doc.build(story)
    print("OK:", OUT)


if __name__ == "__main__":
    main()
