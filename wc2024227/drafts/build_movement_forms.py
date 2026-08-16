#!/usr/bin/env python3
"""WC/2024/227 — ATTACHMENT 5: the three approved movement forms, stitched with an index page.

Builds drafts/out/ATTACHMENT_5_Movement_Forms_2026.pdf (1 index page + 3 forms x 4pp = 13pp).

⭐⭐⭐ WHY THEY GO IN — read from the forms themselves, 16 August 2026.

1. THE SHIFT ARRANGEMENT NEVER CHANGED. Every one of the three records
   "Shift Arrangements: Continuous Shift Worker" — including the 40-hour one. The hours were
   reduced; the continuous-shift requirement was retained and worked. ⇒ That is the answer to
   question 3.6: an adjustment to hours did not remove him from the mandatory requirement of the
   role, because the employer's own forms say it did not.

2. THE DELEGATE WHO APPROVED ALL THREE IS SCOTT HUGHES — 27.02.2026, 17.04.2026, 09.06.2026 —
   and Scott Hughes signed the request of 31 July 2026 asking whether Mr Shepherd can fulfil the
   full inherent requirements of the role "without restrictions or modifications to duties".
   ⛔ THAT POINT IS NOT PUT TO THE CLINICIAN. It belongs in the covering note to the employer and
   in the employment track. The forms go to the doctor as operational fact only.

3. THEY CORROBORATE THE CAPABILITY CHECKLIST from a different author: the checklist records the
   reduced pattern as "worked and tolerated over the past twelve months without deterioration";
   the forms show the same pattern approved and operating.

⚠ AND THE TREND CUTS BOTH WAYS — 76 → 56 → 56 → 40 hours. An opposing reader calls that declining
capacity. ⇒ Question 3.6(e) now asks the clinician directly whether the reduction indicates
deterioration or the successful management of a stable condition. Better answered in the report
than argued afterwards.

⛔ The index page is purely descriptive — every field is copied from the forms. No commentary, no
totals, no argument. Same standard as the schedule of assumed facts.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

SRC = "../documents/"
FORMS = ["2026-02-27_Movement_56hrs_1Mar-15Mar_HughesApproved.pdf",
         "2026-04-17_Movement_56hrs_16Mar-26Apr_HughesApproved.pdf",
         "2026-06-09_Movement_40hrs_25May-28Jun_HughesApproved.pdf"]
OUT = "out/ATTACHMENT_5_Movement_Forms_2026.pdf"

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=12.5, leading=16, spaceAfter=3)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.4, leading=13, spaceAfter=6)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))
def P(t, s=BODY): return Paragraph(t, s)

s = [P("Attachment 5 — approved changes to working hours, 2026", H1),
     P("WC/2024/227 · Shepherd · three forms of the employer, reproduced in full and unmarked", SMALL),
     P("This index page lists the fields recorded on the three forms that follow. Every entry is "
       "taken from the form itself.", BODY)]

rows = [[P("<b>Field</b>", SMALL), P("<b>Form 1</b>", SMALL), P("<b>Form 2</b>", SMALL),
         P("<b>Form 3</b>", SMALL)],
 [P("Delegate approval", SMALL), P("<b>27.02.2026</b>", SMALL), P("<b>17.04.2026</b>", SMALL),
  P("<b>09.06.2026</b>", SMALL)],
 [P("Effective period", SMALL), P("01.03.2026 –<br/>15.03.2026", SMALL),
  P("16.03.2026 –<br/>26.04.2026", SMALL), P("25.05.2026 –<br/>28.06.2026", SMALL)],
 [P("Movement task", SMALL), P("Change to Working Conditions (Temporary)", SMALL),
  P("Change to Working Conditions (Temporary)", SMALL),
  P("Change to Working Conditions (Temporary)", SMALL)],
 [P("Position", SMALL), P("AO Switchboard<br/>AO3, Level 04", SMALL),
  P("AO Switchboard<br/>AO3, Level 04", SMALL), P("AO Switchboard<br/>AO3, Level 04", SMALL)],
 [P("<b>Fortnightly hours</b>", SMALL), P("<b>56.00</b>", SMALL), P("<b>56.00</b>", SMALL),
  P("<b>40.00</b>", SMALL)],
 [P("Employment basis", SMALL), P("Part Time", SMALL), P("Part Time", SMALL), P("Part Time", SMALL)],
 [P("<b>Shift arrangements</b>", SMALL), P("<b>Continuous Shift Worker</b>", SMALL),
  P("<b>Continuous Shift Worker</b>", SMALL), P("<b>Continuous Shift Worker</b>", SMALL)],
 [P("Working arrangement", SMALL), P("Standard Hours", SMALL), P("Standard Hours", SMALL),
  P("Standard Hours", SMALL)],
 [P("Comments, as recorded", SMALL),
  P("<i>“Cory Shepherd to extend reduce hours contract - 1.03.26 - 15.03.26 possible "
    "extension”</i>", SMALL),
  P("<i>“Cory Shepherd reduced hours from 1FTE to 0.7fte per fortnight 16.03.2026 - 26.04.2026 "
    "with possible extension after review.”</i>", SMALL),
  P("<i>“Cory Shepherd request to reduce contracted hours from 1.0FTE - 0.5TE 40hrs per "
    "fortnight. Temp request until 28.06.26 until further review and documentation to be "
    "provided to support request.”</i>", SMALL)],
]
t = Table(rows, colWidths=[30*mm, 45*mm, 45*mm, 46*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f7f7f7')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
s.append(t)
s.append(P("The full-time fortnight for the position is 76 hours. Each form was certified by the "
           "line manager, agreed by me, and approved by the delegate on the date shown. The three "
           "forms follow, complete and unmarked.", BODY))

buf = io.BytesIO()
doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                        topMargin=16*mm, bottomMargin=16*mm,
                        title="WC/2024/227 — Attachment 5, movement forms 2026",
                        author="Cory Lea Shepherd")
def f(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(18*mm, 10*mm, "WC/2024/227 · Shepherd · Attachment 5 · approved changes to working hours, 2026")
    canv.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
buf.seek(0)

out = pikepdf.Pdf.open(buf)
for name in FORMS:
    with pikepdf.Pdf.open(SRC + name) as src:
        out.pages.extend(src.pages)
with out.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta['dc:title'] = "WC/2024/227 — Attachment 5 — approved changes to working hours, 2026"
out.save(OUT)
print("built", OUT, "pages:", len(out.pages))
