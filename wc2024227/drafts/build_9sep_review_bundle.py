#!/usr/bin/env python3
"""WC/2024/227 — one PDF of the whole 9 September 2026 set, for reading and printing.

⛔ REVIEW COPY. Not for service and not for filing. What is served and filed are the separate
files in out/FINAL_9SEP2026/. Every page of this bundle carries a footer saying so, and a divider
precedes each document naming it and where it goes, so a page pulled out of it cannot be mistaken
for a served document.

Run build_9sep_final.py first; this reads its output.
"""
import io, os
import pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

F = "out/FINAL_9SEP2026"
OUT = "out/REVIEW_BUNDLE_9SEP2026.pdf"

HD = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11,
                    textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=10)
BIG = ParagraphStyle('BIG', fontName='Helvetica-Bold', fontSize=15, leading=19, spaceAfter=4)
WARN = ParagraphStyle('WARN', fontName='Helvetica-Bold', fontSize=9.6, leading=13,
                      textColor=colors.HexColor('#8a2010'), spaceAfter=8)
B = ParagraphStyle('B', fontName='Helvetica', fontSize=9.4, leading=12.6, spaceAfter=5)
LAB = ParagraphStyle('LAB', parent=B, fontName='Helvetica-Bold', spaceBefore=6, spaceAfter=1)
DIV = ParagraphStyle('DIV', fontName='Helvetica-Bold', fontSize=17, leading=21, spaceAfter=6)

HEADER = ("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",
          "Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' "
          "Compensation Regulator (Respondent)")

# file, divider title, where it goes
DOCS = [
    (f"{F}/1_COMMISSION/Appellant_List_of_Witnesses_WC2024227.pdf",
     "Appellant's list of names of all witnesses",
     "Direction 1. FILED in the Industrial Registry and served on the Respondent. Email 1, attachment 1."),
    (f"{F}/1_COMMISSION/Covering_Letter_to_Industrial_Registrar_WC2024227.pdf",
     "Covering letter to the Industrial Registrar",
     "Filed with the witness list. Email 1, attachment 2. The Respondent receives it on the copy to her."),
    (f"{F}/2_REGULATOR/Letter_to_Regulator_re_letter_of_8_September_2026_WC2024227.pdf",
     "Letter to the Regulator on its letter of 8 September 2026",
     "SERVED on the Respondent only. Email 2, attachment 2."),
    (f"{F}/2_REGULATOR/Outline_of_Evidence_Cory_Lea_Shepherd_WC2024227.pdf",
     "Outline of evidence — Mr Cory Lea Shepherd",
     "Direction 2. SERVED on the Respondent. NOT filed. Email 2, attachment 3."),
    (f"{F}/2_REGULATOR/Outline_of_Evidence_Cory_Harrison-Jones_WC2024227.pdf",
     "Outline of evidence — Mr Cory Harrison-Jones",
     "Direction 2. SERVED on the Respondent. NOT filed. Email 2, attachment 4."),
    (f"{F}/2_REGULATOR/Outline_of_Evidence_Patricia_Conaghan_WC2024227.pdf",
     "Outline of evidence — Ms Patricia Conaghan",
     "Direction 2. SERVED on the Respondent. NOT filed. Email 2, attachment 5."),
    (f"{F}/2_REGULATOR/Schedule_of_Medical_Documents_Relied_Upon_WC2024227.pdf",
     "Schedule of medical documents relied upon",
     "Direction 2, expert limb. SERVED on the Respondent. NOT filed. Email 2, attachment 6. One page."),
    (f"{F}/2_REGULATOR/Medical_Documents_Relied_Upon_Tabs_M1_to_M9_WC2024227.pdf",
     "Medical documents relied upon — Tabs M1 to M9",
     "The pages behind the schedule. SERVED on the Respondent. NOT filed. Email 2, attachment 7. 42 pages."),
    (f"{F}/2_REGULATOR/Request_to_Regulator_documents_not_admitted_WC2024227.pdf",
     "Request: the documents not admitted on 8 September 2026",
     "SERVED on the Respondent. Email 3, sole attachment. Reply sought by Friday 18 September 2026."),
]


def _page(story, margin=20*mm):
    buf = io.BytesIO()
    d = BaseDocTemplate(buf, pagesize=A4, leftMargin=margin, rightMargin=margin,
                        topMargin=18*mm, bottomMargin=18*mm)
    d.addPageTemplates([PageTemplate(id='n', frames=[
        Frame(margin, 18*mm, A4[0]-2*margin, A4[1]-36*mm, leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)])])
    d.build(story)
    buf.seek(0)
    return pikepdf.open(buf)


def cover():
    s = [Paragraph(HEADER[0], HD), Paragraph(HEADER[1], HD2),
         Paragraph("THE 9 SEPTEMBER 2026 SET", BIG),
         Paragraph("Review copy. Not for service and not for filing.", WARN),
         Paragraph("This one file gathers everything going out on 9 September 2026 so it can be read "
                   "and printed in one pass. What is actually served and filed are the separate files "
                   "in FINAL_9SEP2026. Each document below is preceded by a divider saying where it "
                   "goes, and every page carries a footer marking this as the review copy.", B),
         Paragraph("The deadline", LAB),
         Paragraph("4.00 pm Wednesday 9 September 2026, under directions 1 and 2 of the Further "
                   "Directions Order (3) dated 19 August 2026. The Respondent's list of witnesses and "
                   "outlines are due by 4.00 pm on 30 September 2026.", B),
         Paragraph("What is filed, and what is only served", LAB),
         Paragraph("Only the list of witnesses and its covering letter are filed in the Industrial "
                   "Registry. Direction 2 requires the outlines and the medical material to be served "
                   "on the Respondent and <b>not</b> filed. The three letters are correspondence "
                   "between the parties and are not filed either.", B),
         Paragraph("The four emails", LAB),
         Paragraph("1. To the Industrial Registry, copied to the Regulator: the witness list and the "
                   "covering letter.<br/>"
                   "2. To the Regulator: the witness list, the letter on its 8 September letter, the "
                   "three outlines and the medical schedule with Tabs M1 to M9.<br/>"
                   "3. To the Regulator: the request about the documents not admitted.<br/>"
                   "4. To Dr Krishnaiah: the clinical records and his attendance at the hearing.<br/>"
                   "The text of each is in FINAL_9SEP2026/3_EMAILS. Send from the personal address, "
                   "not the Queensland Health account.", B),
         Paragraph("Held back", LAB),
         Paragraph("The Form 24 and Form 25 notices and the Regulator's responses are filed together "
                   "<b>after</b> the response date of Friday 11 September 2026, using the draft held "
                   "in SEND_9SEP2026. The long service leave email is employment-track and is kept in "
                   "a separate folder so it cannot be attached to an appeal email.", B),
         Spacer(1, 6*mm),
         Paragraph("Dated 9 September 2026 &nbsp;·&nbsp; Cory Lea Shepherd, Appellant, self-represented",
                   HD)]
    return _page(s)


def divider(n, title, where):
    s = [Paragraph(HEADER[0], HD), Paragraph(HEADER[1], HD2), Spacer(1, 40*mm),
         Paragraph(f"{n}.&nbsp;&nbsp;{title}", DIV),
         Paragraph(where, B)]
    return _page(s)


out = pikepdf.Pdf.new()
for pg in cover().pages:
    out.pages.append(pg)
for i, (path, title, where) in enumerate(DOCS, start=1):
    if not os.path.exists(path):
        raise SystemExit(f"missing: {path} — run build_9sep_final.py first")
    for pg in divider(i, title, where).pages:
        out.pages.append(pg)
    for pg in pikepdf.open(path).pages:
        out.pages.append(pg)

N = len(out.pages)
_overlays = []
for idx, pg in enumerate(out.pages, start=1):
    w = float(pg.mediabox[2]) - float(pg.mediabox[0])
    h = float(pg.mediabox[3]) - float(pg.mediabox[1])
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFont('Helvetica', 7)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawRightString(w - 10*mm, 5*mm,
                      f"WC/2024/227 · review copy, not for service or filing · page {idx} of {N}")
    c.showPage()
    c.save()
    buf.seek(0)
    ov = pikepdf.open(buf)
    _overlays.append(ov)          # keep alive: add_overlay needs the source Pdf to outlive the call
    pg.add_overlay(ov.pages[0])

try:
    del out.Root.Metadata
except (AttributeError, KeyError):
    pass
with out.open_metadata(set_pikepdf_as_editor=False) as m:
    m.clear()
try:
    del out.Root.Metadata
except (AttributeError, KeyError):
    pass
for k in list(out.docinfo.keys()):
    del out.docinfo[k]
out.save(OUT, linearize=True)
print(f"built {OUT} — {N} pages, {os.path.getsize(OUT)/1048576:.2f} MB")
