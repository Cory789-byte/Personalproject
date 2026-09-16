#!/usr/bin/env python3
"""WC/2024/227 — Attachment 7: the employer's request for medical information, 31 July 2026.

Built 17 August 2026 for the SEVEN-ATTACHMENT letter of instruction (Cory's revision of 17 Aug):
the letter now encloses the request itself — "It is enclosed as Attachment 7, including the
nine-question schedule" — so the request must exist as one file.

Contents (8 pages):
  p1     index page, in the style of the new Attachment 2 and Attachment 5 index pages —
         "written on each document" only; no commentary, no characterisation.
  pp2–3  letter of Mr Scott Hughes to Mr Shepherd, 31 July 2026 (2 pp) — the request.
  pp4–8  letter of Mr Scott Hughes to Dr Day Hong Ma with the nine-question schedule (5 pp).

Both are the employer's own documents, signed "Scott Hughes, Director, Corporate Services,
Logan Beaudesert Health Service, Metro South Health, 31/07/2026" (verified from source, 17 Aug).
Reproduced complete and unmarked. All metadata stripped, as with Attachment 1.
"""
import io, pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle

SRC_EMP = "../documents/2026-07-31_ScottHughes_RFMI_letter_to_EMPLOYEE.pdf"
SRC_GP  = "../documents/2026-07-31_ScottHughes_RFMI_letter_to_GP_DrMa_9questions.pdf"
OUT     = "out/07_ATTACHMENT_7_Request_for_Medical_Information_31Jul2026.pdf"
PW, PH = A4

H1   = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=16, spaceAfter=2)
SUB  = ParagraphStyle('SUB', fontName='Helvetica', fontSize=9.5, leading=13,
                      textColor=colors.HexColor('#444444'))
CELL = ParagraphStyle('CELL', fontName='Helvetica', fontSize=9.6, leading=13)
KEY  = ParagraphStyle('KEY', parent=CELL, fontName='Helvetica-Bold')
def C(t, s=CELL): return Paragraph(t, s)

rows = [
 [C("Written on the documents", KEY), C("", CELL)],
 [C("Document 1", KEY),
  C("Letter to Mr Cory Shepherd — the request for medical information (2 pages)")],
 [C("Document 2", KEY),
  C("Letter to Dr Day Hong Ma with the nine-question schedule — <i>“Request for Medical "
    "Information”</i> (5 pages)")],
 [C("Signed by", KEY),
  C("Mr Scott Hughes, Director, Corporate Services, Logan Beaudesert Health Service, "
    "Metro South Health — on each document")],
 [C("Date", KEY), C("31 July 2026")],
 [C("Made under", KEY),
  C("HR Policy G3: Reasonable Adjustment; sections 17 and 19 of the <i>Work Health and "
    "Safety Act 2011</i> — as stated in Document 1")],
]
tbl = Table(rows, colWidths=[38*mm, 128*mm])
tbl.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('SPAN', (0,0), (1,0)),
    ('BACKGROUND', (0,0), (1,0), colors.HexColor('#eeeeee')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 6), ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))

buf = io.BytesIO()
cv = canvas.Canvas(buf, pagesize=A4)
y = PH - 22*mm
for para, sty in [("Attachment 7 — request for medical information, 31 July 2026", H1),
                  ("WC/2024/227 · Shepherd v Workers' Compensation Regulator · two documents of "
                   "the employer, reproduced in full and unmarked.", SUB)]:
    p = Paragraph(para, sty)
    w, h = p.wrapOn(cv, PW - 40*mm, PH)
    y -= h
    p.drawOn(cv, 20*mm, y)
    y -= 3*mm
y -= 4*mm
w, h = tbl.wrapOn(cv, PW - 40*mm, PH)
tbl.drawOn(cv, 20*mm, y - h)
p = Paragraph("The two documents follow.", CELL)
w2, h2 = p.wrapOn(cv, PW - 40*mm, PH)
p.drawOn(cv, 20*mm, y - h - 8*mm - h2)
cv.setFont('Helvetica', 7.4); cv.setFillColor(colors.HexColor('#777777'))
cv.drawString(20*mm, 10*mm, "WC/2024/227 · Attachment 7")
cv.drawRightString(PW - 20*mm, 10*mm, "Page 1")
cv.showPage(); cv.save(); buf.seek(0)

out = pikepdf.Pdf.new()
idx = pikepdf.open(buf)
out.pages.extend(idx.pages)
for src in (SRC_EMP, SRC_GP):
    s = pikepdf.open(src)
    out.pages.extend(s.pages)

# all metadata removed (same routine as Attachment 1)
try: del out.Root.Metadata
except (AttributeError, KeyError): pass
with out.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta.clear()
try: del out.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(out.docinfo.keys()):
    del out.docinfo[k]
out.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(out.pages)} — metadata stripped")
