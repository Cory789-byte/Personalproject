#!/usr/bin/env python3
"""APPELLANT'S LIST OF DOCUMENTS — WC/2024/227
Landscape A4 schedule for service on the Respondent (Regulator).
Scrubbed metadata, Author = Cory L Shepherd, AES-256, print/extract allowed, no editing.
"""
import pikepdf
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                               Spacer, Table, TableStyle, KeepTogether)

OUT = "/home/user/Personalproject/wc2024227/drafts/out/LIST_OF_DOCUMENTS_WC2024227.pdf"
TMP = "/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/_lod_raw.pdf"

PW, PH = landscape(A4)
FONT, BOLD = "Helvetica", "Helvetica-Bold"

body  = ParagraphStyle("body",  fontName=FONT, fontSize=7.4, leading=9.4)
bodyb = ParagraphStyle("bodyb", fontName=BOLD, fontSize=7.4, leading=9.4)
head  = ParagraphStyle("head",  fontName=BOLD, fontSize=7.4, leading=9.4,
                       textColor=colors.white)
h1    = ParagraphStyle("h1",    fontName=BOLD, fontSize=13, leading=16, spaceAfter=2)
h2    = ParagraphStyle("h2",    fontName=BOLD, fontSize=9.2, leading=12,
                       spaceBefore=7, spaceAfter=3)
meta  = ParagraphStyle("meta",  fontName=FONT, fontSize=8, leading=11)
note  = ParagraphStyle("note",  fontName=FONT, fontSize=7.2, leading=9.4,
                       textColor=colors.HexColor("#444444"))


class Numbered(pdfcanvas.Canvas):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self._pages = []

    def showPage(self):
        self._pages.append(dict(self.__dict__)); self._startPage()

    def save(self):
        n = len(self._pages)
        for st in self._pages:
            self.__dict__.update(st); self._foot(n); super().showPage()
        super().save()

    def _foot(self, n):
        self.setFont(FONT, 6.8)
        self.setFillColor(colors.HexColor("#555555"))
        self.drawString(14 * mm, 9 * mm,
                        "C Shepherd · WC/2024/227 · Appellant's List of Documents "
                        "· 5 August 2026")
        self.drawRightString(PW - 14 * mm, 9 * mm,
                             "Page %d of %d" % (self._pageNumber, n))
        self.setStrokeColor(colors.HexColor("#bbbbbb")); self.setLineWidth(0.4)
        self.line(14 * mm, 12 * mm, PW - 14 * mm, 12 * mm)


def P(t, s=body):
    return Paragraph(t, s)


COLS = [12 * mm, 22 * mm, 104 * mm, 40 * mm, 34 * mm, 14 * mm, 34 * mm]
HEADERS = ["Item", "Date", "Description", "Author / From", "Recipient / To",
           "Pages", "Status"]

TSTYLE = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2f3b52")),
    ("VALIGN",     (0, 0), (-1, -1), "TOP"),
    ("GRID",       (0, 0), (-1, -1), 0.35, colors.HexColor("#9aa3b0")),
    ("LEFTPADDING",(0, 0), (-1, -1), 3),
    ("RIGHTPADDING",(0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 2.5),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 2.5),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1),
     [colors.white, colors.HexColor("#f2f4f7")]),
])


def table(rows):
    data = [[P(h, head) for h in HEADERS]]
    for r in rows:
        data.append([P(str(c)) for c in r])
    t = Table(data, colWidths=COLS, repeatRows=1)
    t.setStyle(TSTYLE)
    return t


# ------------------------------------------------------------------ CONTENT
PART1 = [
    ("1", "8 Sep 2024", "Work Capacity Certificate for the injury of 18 June 2024, signed",
     "Dr P Hawes", "WorkCover Queensland", "1", "Produced herewith"),
    ("2", "3 Jul 2026", "Employee Capacity Certificate — certifying fit to return with "
     "restrictions; records the arrangement as a continuation of an existing arrangement, "
     "worked and tolerated, without deterioration",
     "Dr D H Ma, My Doctor Clinic", "MSH Injury Management", "2", "Produced herewith"),
    ("3", "3 Jul 2026", "Invoice 574370 — completion of the Employee Capacity Certificate",
     "My Doctor Clinic", "Appellant", "1", "Produced herewith"),
    ("4", "2020–2026", "Monthly call statistics authored by the Appellant "
     "(volume only — calls handled and emergency codes activated)",
     "Appellant", "—", "[n]", "Produced herewith"),
    ("5", "Apr 2025", "Individual monthly statistics, April 2025",
     "Appellant", "—", "1", "Produced herewith"),
    ("6", "FY2025–26", "Payslips and fortnightly hours analysis, 7 Apr 2025 to 14 Jun 2026",
     "Queensland Health Payroll", "Appellant", "[n]", "Produced herewith"),
    ("7", "2025", "Return to work analysis — seven fortnights, FTE",
     "Appellant", "—", "[n]", "Produced herewith"),
    ("8", "4 Apr 2023–", "Text messages between the Appellant and the Line Manager, "
     "including the roster board image of 4 April 2023",
     "Appellant / C Donovan-Taylor", "—", "[n]", "Produced herewith"),
    ("9", "2020–2026", "Correspondence pack 01 — Logan Switchboard",
     "Various", "Various", "103", "Produced herewith"),
    ("10", "2020–2026", "Correspondence pack 02 — C Donovan-Taylor",
     "Various", "Various", "462", "Produced herewith"),
    ("11", "2025–2026", "Correspondence pack 03 — S Hughes",
     "Various", "Various", "376", "Produced herewith"),
    ("12", "31 Jul 2026", "Correspondence pack 04 — Human Resources",
     "Various", "Various", "21", "Produced herewith"),
    ("13", "2025", "Correspondence pack 05 — J Roberts",
     "Various", "Various", "64", "Produced herewith"),
    ("14", "2024–2026", "Correspondence pack 10 — WorkCover Queensland",
     "Various", "Various", "84", "Produced herewith"),
]

PART2 = [
    ("15", "18 Jun 2026", "Affidavit of Cory Lea Shepherd (Form 20) with exhibit index",
     "Appellant", "Commission", "—", "Filed 23 Jun 2026"),
    ("16", "9 May 2024", "Exhibit CS-1 — email chain concerning the MASPER directive, "
     "including the Line Manager's email of 9 May 2024",
     "Various", "—", "4", "Annexed to the Form 20"),
    ("17", "18–20 May 2024", "Exhibit CS-2 — correspondence with Together Queensland "
     "and the union's confirmation of 20 May 2024",
     "Appellant / Together", "—", "3", "Annexed to the Form 20"),
    ("18", "31 Aug 2023", "Exhibit CS-3 — application to increase to full time, recording "
     "the intention to become the Switchboard union delegate",
     "Appellant", "MSH", "2", "Annexed to the Form 20"),
    ("19", "11 Jun 2026", "Exhibit CS-4 — the Respondent's disclosure of 11 June 2026 "
     "(correspondence of 15–16 May 2024)",
     "Respondent", "Appellant", "2", "Annexed to the Form 20"),
    ("20", "5 Jun 2026", "Letter of Metro South Hospital and Health Service responding to the "
     "Notice of Non-Party Disclosure (ref K-LM26/729), with enclosures to Items 6, 11, 12, "
     "13, 15 and 16", "N Cridland, Chief Executive, MSH", "Commissioner Dwyer",
     "5 + enc", "Already before the Commission"),
    ("21", "24 Oct 2024", "Review Decision 69983", "Workers' Compensation Regulator",
     "Appellant", "—", "Already before the Commission"),
]

PART3 = [
    ("22", "2024–2025", "Communications between the Appellant and Saines Legal for the "
     "purpose of obtaining legal advice in this proceeding",
     "Appellant / Saines Legal", "—", "—",
     "PRIVILEGE CLAIMED — legal professional privilege"),
    ("23", "13 May 2024 – 24 Dec 2024", "Documents recording the fact or content of a "
     "public interest disclosure and the determination made in respect of it",
     "Appellant / Ethical Standards Unit", "—", "—",
     "s 65 Public Interest Disclosure Act 2010 — non-publication sought at order 6 of "
     "the draft order"),
]

PART4 = [
    ("24", "6 Jun 2023", "Entry made by the Appellant in the Switchboard communication book "
     "concerning the verification and updating of doctors' on-call contact details",
     "Appellant", "—", "1",
     "No longer in the Appellant's possession — the removal of the page is admitted "
     "(Form 24, para 6). Sought at Item 18 of the Notice"),
    ("25", "17–18 Mar 2024", "SPOK emergency-code and paging records for the shifts "
     "pleaded", "MSH system record", "—", "—",
     "Never in the Appellant's possession. Sought at Items 1–2 of the Notice"),
]


def build():
    doc = BaseDocTemplate(TMP, pagesize=landscape(A4),
                          leftMargin=14 * mm, rightMargin=14 * mm,
                          topMargin=13 * mm, bottomMargin=16 * mm,
                          title="Appellant's List of Documents — WC/2024/227",
                          author="Cory L Shepherd", subject="", creator="", producer="")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame])])

    s = []
    s.append(P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", meta))
    s.append(P("Matter No. WC/2024/227 · <i>Workers' Compensation and Rehabilitation "
               "Act 2003</i> (Qld)", meta))
    s.append(Spacer(1, 3))
    s.append(P("BETWEEN: CORY LEA SHEPHERD (Appellant) &nbsp;&nbsp;AND: "
               "WORKERS' COMPENSATION REGULATOR (Respondent)", meta))
    s.append(Spacer(1, 7))
    s.append(P("APPELLANT'S LIST OF DOCUMENTS", h1))
    s.append(P("Served on the Respondent · 5 August 2026", meta))
    s.append(Spacer(1, 5))
    s.append(P("This list is given in discharge of the Appellant's disclosure obligation in "
               "this proceeding. It lists documents in the Appellant's possession or under "
               "his control that are directly relevant to a matter in issue. Disclosure is "
               "continuing: this list will be supplemented as further documents come into "
               "the Appellant's possession, including the medical reports referred to at "
               "Part 5.", note))
    s.append(Spacer(1, 4))

    s.append(P("PART 1 — DOCUMENTS IN THE APPELLANT'S POSSESSION, PRODUCED WITH THIS LIST", h2))
    s.append(table(PART1))

    s.append(P("PART 2 — DOCUMENTS ALREADY BEFORE THE COMMISSION OR PREVIOUSLY EXCHANGED", h2))
    s.append(table(PART2))

    s.append(P("PART 3 — DOCUMENTS FOR WHICH PRIVILEGE OR STATUTORY PROTECTION IS CLAIMED", h2))
    s.append(table(PART3))

    s.append(P("PART 4 — DOCUMENTS ONCE IN, OR NEVER IN, THE APPELLANT'S POSSESSION", h2))
    s.append(table(PART4))

    s.append(P("PART 5 — DOCUMENTS NOT YET IN EXISTENCE", h2))
    s.append(P("The Appellant will disclose, upon receipt, the report of his treating "
               "psychiatrist addressing diagnosis, causation and chronology, and any further "
               "medical certificate or capacity advice issued after the date of this list.",
               body))

    s.append(Spacer(1, 8))
    s.append(P("Cory Lea Shepherd, Appellant (Self-Represented)", bodyb))
    s.append(P("15 Edmond Street, Coomera QLD 4209 · 0417 400 227 · "
               "coryshepherd1@hotmail.com", body))
    doc.build(s, canvasmaker=Numbered)

    with pikepdf.open(TMP, allow_overwriting_input=True) as pdf:
        for k in list(pdf.docinfo.keys()):
            del pdf.docinfo[k]
        pdf.docinfo["/Author"] = "Cory L Shepherd"
        pdf.docinfo["/Title"] = "Appellant's List of Documents — WC/2024/227"
        if pdf.Root.get("/Metadata") is not None:
            del pdf.Root["/Metadata"]
        pdf.save(OUT, encryption=pikepdf.Encryption(
            owner="", user="", allow=pikepdf.Permissions(
                modify_other=False, modify_annotation=False, modify_assembly=False,
                modify_form=False, extract=True, print_lowres=True, print_highres=True)))
    print("built:", OUT)


build()
