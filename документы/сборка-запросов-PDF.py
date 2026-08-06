# -*- coding: utf-8 -*-
"""Формирует два PDF-запроса поставщикам сырья: общий и специальный."""

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
    "th": ParagraphStyle("th", fontName="DJ-B", fontSize=8.6, leading=11.5, textColor=INK),
    "td": ParagraphStyle("td", fontName="DJ", fontSize=8.6, leading=11.5, textColor=INK),
    "tdn": ParagraphStyle("tdn", fontName="DJ", fontSize=8.6, leading=11.5, textColor=MUTED),
    "sig": ParagraphStyle("sig", fontName="DJ", fontSize=9.5, leading=14.5, textColor=INK),
}


def rule(sb=4, sa=8):
    return HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=sb, spaceAfter=sa)


def table(rows):
    data = [[Paragraph("№", S["th"]),
             Paragraph("Материал", S["th"]),
             Paragraph("Какие характеристики прошу указать", S["th"])]]
    for n, pos, ask in rows:
        data.append([Paragraph(str(n), S["tdn"]),
                     Paragraph(pos, S["td"]),
                     Paragraph(ask, S["td"])])
    t = Table(data, colWidths=[9 * mm, 54 * mm, 107 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BAND),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
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
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
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


def signature():
    return KeepTogether([
        Spacer(1, 10), rule(0, 8),
        Paragraph("С уважением,<br/><b>Мясоедов Алексей Владимирович</b><br/>"
                  "индивидуальный предприниматель<br/>"
                  "+375 33 628-04-86 &nbsp;·&nbsp; miasoedov95@gmail.com", S["sig"]),
    ])


COMMON_REQ = [
    "Точное торговое наименование и завод-изготовитель.",
    "Цену за килограмм при трёх объёмах: до 100 кг, до 500 кг, от 1 тонны.",
    "Минимальную партию отгрузки и вид фасовки.",
    "Срок поставки: со склада и под заказ отдельно.",
    "Техническое описание (TDS) и паспорт безопасности (SDS) — файлами.",
    "Возможность отгрузки пробной партии 5–25 кг.",
    "Гарантируется ли поставка одной и той же марки одного завода-изготовителя "
    "на постоянной основе, с паспортом качества на каждую партию.",
]

ORG_Q = [
    "Есть ли у вас технический специалист, к которому можно обращаться по "
    "вопросам совместимости и дозировок?",
    "Отпускаете ли образцы бесплатно или по символической цене?",
    "Какие позиции складские, а какие под заказ — с минимальным объёмом и сроком.",
    "Работаете ли с индивидуальными предпринимателями или только с юридическими лицами?",
    "Условия оплаты: предоплата или возможна отсрочка?",
]


def build(out, title, intro, sections, footer_note=None):
    story = [header(), rule(2, 12), Paragraph(title, S["title"])]
    story.append(Paragraph("Добрый день!", S["body"]))
    for p in intro:
        story.append(Paragraph(p, S["body"]))
    story.append(Paragraph("Что прошу указать по каждой позиции", S["h2"]))
    story.append(numbered(COMMON_REQ))
    for name, rows in sections:
        story.append(Paragraph(name, S["h2"]))
        story.append(table(rows))
    story.append(Paragraph("Организационные вопросы", S["h2"]))
    story.append(numbered(ORG_Q))
    if footer_note:
        story.append(Spacer(1, 10))
        story.append(Paragraph(footer_note, S["body"]))
    story.append(signature())

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

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                          topMargin=18 * mm, bottomMargin=20 * mm,
                          title=title, author="Мясоедов Алексей Владимирович",
                          subject="Запрос коммерческого предложения на сырьё")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=decorate)])
    doc.build(story)
    print("OK:", out)


# ==================================================== ДОКУМЕНТ 1 — ОБЩИЙ
build(
    "/home/user/romanovdecor-site/документы/Запрос-сырья-общий.pdf",
    "Запрос коммерческого предложения и технической документации на сырьё",
    [
        "Закупаем сырьё для производства сухих строительных смесей и составов "
        "для полов и стен. Подбираем постоянных поставщиков.",
        "Прошу дать коммерческое предложение по тем позициям перечня, которые "
        "есть в вашем ассортименте. Если какой-то группы нет — достаточно это "
        "отметить.",
    ],
    [
        ("1. Вяжущее и наполнители", [
            (1, "Белый портландцемент CEM I 52,5 R",
             "Белизна и метод её измерения; завод-изготовитель; содержание "
             "C<sub>3</sub>A; стабильность оттенка от партии к партии."),
            (2, "Песок кварцевый, фракция 0,1–0,3 мм",
             "Содержание SiO<sub>2</sub> и Fe<sub>2</sub>O<sub>3</sub>; влажность; "
             "месторождение; форма зерна — окатанное или дроблёное."),
            (3, "Песок кварцевый, фракция 0,06–0,15 мм", "Те же характеристики."),
            (4, "Мука кварцевая",
             "d<sub>50</sub>, d<sub>10</sub> и доля частиц мельче 4 мкм; полное "
             "распределение по лазерной дифракции."),
            (5, "Микрокальцит 2–20 мкм",
             "d<sub>50</sub> и верхний срез; белизна; маслоёмкость."),
        ]),
        ("2. Полимерная часть", [
            (6, "Порошок полимерный редиспергируемый",
             "Химическая основа и температура стеклования плёнки; MFFT; тип "
             "защитного коллоида; гидрофобизирован ли; состав антиблокинг-агента "
             "и зольность; марка и завод-изготовитель."),
            (7, "Дисперсия акриловая или стирол-акриловая для минеральных вяжущих",
             "Сухой остаток, T<sub>g</sub>, MFFT, размер частиц, pH, вязкость; тип "
             "эмульгаторной системы; APEO-free или нет; стойкость к "
             "замораживанию-оттаиванию; марка и завод-изготовитель. Если "
             "подходящих марок несколько — прошу дать все."),
        ]),
        ("3. Реология и водоудержание", [
            (8, "Эфир целлюлозы MHEC, 20 000–30 000 мПа·с",
             "Метод и концентрация замера вязкости; степень замещения; влияние на "
             "сроки схватывания; обработан ли для отложенного растворения."),
            (9, "Эфир крахмала гидроксипропиловый",
             "Марка; рекомендуемая изготовителем дозировка."),
            (10, "Загуститель для водных систем",
             "Химия — HEUR, HASE или целлюлозный; есть ли неионные марки."),
        ]),
        ("4. Функциональные добавки", [
            (11, "Пеногаситель порошковый",
             "Химическая основа. Требуется безсиликоновый; прошу подтвердить "
             "документально."),
            (12, "Пеногаситель жидкий для водных систем",
             "Химическая основа; наличие минерального масла; содержит ли силикон."),
            (13, "Смачиватель низкопенный", "Ионность. Требуются неионные."),
            (14, "Стеарат кальция или стеарат Ca/Zn", "Марка; тонкость помола."),
            (15, "Фибра полиакрилонитрильная, 3,2 мм", "Длина; титр."),
            (16, "Микрофибра целлюлозная", "Длина."),
            (17, "Биоцид внутритарный",
             "Действующее вещество: BIT, CIT/MIT или их смесь. Требуется стойкость "
             "при pH 8–9,5 и совместимость с аминовыми буферами."),
            (18, "Буфер аминовый AMP-95 или аналог",
             "Марка; содержание активного вещества."),
            (19, "Коалесцент (Texanol, DPnB или аналог)",
             "Точное наименование; температура кипения."),
        ]),
        ("5. Пигменты", [
            (20, "Диоксид титана, рутильная форма",
             "Хлоридный или сульфатный процесс; вид поверхностной обработки; "
             "марка и завод-изготовитель."),
            (21, "Пасты пигментные водные для минеральных вяжущих",
             "Тип диспергатора; щёлочестойкость и стойкость к ионам "
             "Ca<super>2+</super>; наличие гликолей; APEO-free или нет; чем "
             "консервированы."),
            (22, "Пигменты железооксидные и прочие неорганические",
             "Щёлочестойкость; светостойкость; форма поставки — порошок или "
             "гранулят."),
        ]),
    ],
    "Готов приехать в офис для очного обсуждения в удобное для вас время.",
)

# ================================================ ДОКУМЕНТ 2 — СПЕЦИАЛЬНЫЙ
build(
    "/home/user/romanovdecor-site/документы/Запрос-сырья-специальный.pdf",
    "Запрос коммерческого предложения на специальные позиции",
    [
        "В дополнение к ранее направленному перечню прошу дать предложение по "
        "позициям ниже. Часть из них может отсутствовать на складе — прошу "
        "указать возможность и срок поставки под заказ.",
    ],
    [
        ("1. Специальные вяжущие", [
            (1, "Цемент глинозёмистый, около 40 % Al<sub>2</sub>O<sub>3</sub>",
             "Содержание Al<sub>2</sub>O<sub>3</sub> и Fe<sub>2</sub>O<sub>3</sub>; тонкость "
             "помола по Блейну; марка и завод-изготовитель."),
            (2, "Ангидрит II тонкомолотый",
             "Чистота по CaSO<sub>4</sub>; тонкость помола; природный или синтетический."),
            (3, "α-полугидрат сульфата кальция",
             "Чистота; тонкость помола; природный или синтетический."),
            (4, "Метакаолин белый",
             "Белизна; d<sub>50</sub>; пуццолановая активность; остаток на сите 45 мкм."),
        ]),
        ("2. Специальные наполнители", [
            (5, "Сульфат бария микронизированный (бланфикс)",
             "Осаждённый или молотый; d<sub>50</sub>; белизна; маслоёмкость; "
             "содержание водорастворимых солей бария."),
            (6, "Волластонит игольчатый",
             "Соотношение сторон кристалла; длина иглы; есть ли марки с "
             "аминосилановой обработкой поверхности."),
            (7, "Микросферы стеклянные сплошные, 5–50 мкм",
             "Фракция; обработка поверхности."),
        ]),
        ("3. Химические реагенты", [
            (8, "Суперпластификатор PCE, порошковый",
             "Содержание активного вещества; воздухововлечение; совместимость с "
             "быстротвердеющими вяжущими."),
            (9, "Кислота винная", "Квалификация и чистота."),
            (10, "Карбонат лития", "Чистота."),
            (11, "Сульфоалюминат кальция",
             "Какие марки есть; содержание свободной извести; рекомендуемая дозировка."),
            (12, "Неопентилгликоль", "Чистота; фасовка."),
        ]),
        ("4. Эпоксидная система", [
            (13, "Дисперсия эпоксидная водная",
             "Сухой остаток; эпоксидный эквивалент EEW в поставляемом виде; "
             "размер частиц; наличие и вид сорастворителя."),
            (14, "Отвердитель аминный водный",
             "Сухой остаток; аминный эквивалент AHEW; жизнеспособность смеси; "
             "есть ли видимая индикация её окончания."),
        ]),
    ],
    "По позициям 13–14: если такого направления в ассортименте нет — прошу "
    "сообщить, работаете ли вы с производителями водных эпоксидных систем в "
    "принципе.",
)
