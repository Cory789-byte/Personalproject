#!/usr/bin/env python3
"""WC/2024/227 - request to the Respondent for copies of listed documents, 22 August 2026.

Addressed to Ms R Matheson, Senior Appeals Officer, Workers' Compensation Regulator.
Every item requested is on the Respondent's own amended list of documents of
14 August 2026, verified against that document. Part 2 asks about documents
referred to inside disclosed documents. Nothing is alleged and nothing is characterised.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/REQUEST_FOR_COPIES_OF_LISTED_DOCUMENTS_22Aug2026.pdf"
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=11.5, leading=15, spaceAfter=2)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10, leading=13,
                     spaceBefore=8, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=9, leading=12,
                     textColor=colors.HexColor('#444444'), spaceAfter=3)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.4, leading=13.2, spaceAfter=5)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.6, leading=11.4)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
def P(t, s=B): return Paragraph(t, s)

# item no., description as it appears on the Respondent's list, date
ITEMS = [
 ("1",  "Claim summary", "WorkCover Queensland", "&mdash;"),
 ("8",  "Workers' compensation medical certificate", "Dr Ki Pang", "7 August 2024"),
 ("9",  "Email Dr Krishnaiah &ndash; noting injury and medication",
        "Dr Ravikumar Krishnaiah", "24 October 2024"),
 ("14", "The attachment only: <i>Witness statement &ndash; Carolyn Jeffrey</i>",
        "Carolyn Jeffrey", "18 July 2024"),
 ("16", "Email WIT C Jeffrey to WorkCover with follow up statement",
        "Carolyn Jeffrey", "1 August 2024"),
 ("23", "The attachment only: <i>Email: Request for review and adjustment of payment "
        "&ndash; 08/04/2024 to 23/08/2024</i>", "Various", "26 August 2024"),
 ("44", "Communications report", "WorkCover Queensland", "Various dates"),
 ("45", "Payments/recoveries report", "WorkCover Queensland", "&mdash;"),
 ("49", "WorkCover Queensland reasons for decision", "Amy Mo", "25 July 2024"),
 ("52", "Worker Claim history", "&mdash;", "&mdash;"),
]

st = [P("WC/2024/227 &mdash; Shepherd v Workers' Compensation Regulator", H1),
      P("Request for copies of documents listed in the Respondent's amended list of documents "
        "dated 14 August 2026", SUB),
      P("22 August 2026", SUB)]

st.append(Spacer(1, 3*mm))
st.append(P("Ms R Matheson<br/>Senior Appeals Officer<br/>Workers' Compensation Regulator", B))
st.append(P("Dear Ms Matheson", B))

st.append(P("I refer to the Respondent's amended list of documents dated 14 August 2026, and to the "
            "Further Directions Order (3) of 19 August 2026, which requires the Appellant to file and "
            "serve a list of witnesses and to serve outlines of evidence and any expert reports by "
            "4.00 pm on 9 September 2026.", B))
st.append(P("Paragraph 1 of the Respondent's list offers inspection at 347 Ann Street, Brisbane. "
            "Given the timetable, and that I am presently not attending my workplace, I ask that "
            "copies of the items below be provided electronically instead of by attendance. If any "
            "item is more convenient to provide by another means, I am content with whatever suits "
            "the Respondent.", B))

st.append(P("Part 1 &mdash; items listed by the Respondent", H2))
rows = [[P("Item", CH), P("As described in the Respondent's list", CH),
         P("Person who made document", CH), P("Date", CH)]]
for n, d, mk, dt in ITEMS:
    rows.append([P(f"<b>{n}</b>", C), P(d, C), P(mk, C), P(dt, C)])
t = Table(rows, colWidths=[12*mm, 100*mm, 36*mm, 30*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]))
st.append(t)
st.append(Spacer(1, 2*mm))
st.append(P("Where an item is listed as an email with attachments, I ask for the attachment "
            "identified rather than the whole item, so as to keep the request as narrow as "
            "possible.", B))

st.append(P("Part 2 &mdash; documents referred to within documents already disclosed", H2))
st.append(P("The following are referred to in documents that are already before the Commission or "
            "have been disclosed in this proceeding. I ask whether each is in the Respondent's "
            "possession or control and, if so, for a copy. If it is not, that answer is equally "
            "useful to me and no further step is required.", B))
p2 = [
 ("(a)", "The payroll-system export for <b>AVAC PRN 15397775</b> and <b>AVAC PRN 15605601</b>. Both "
         "references are identified in the email of PayrollMetroSouth to the Line Manager of 3 May "
         "2024, copied to me, which forms part of the Respondent's disclosure of the Queensland "
         "Health Payroll witness conferencing. Neither reference appears in the myHR submissions "
         "report for 1 February to 31 May 2024 produced by Metro South Health as Item 11."),
 ("(b)", "The spreadsheet of recorded MET calls for the period 17 to 18 March 2024. The letter of "
         "the Chief Executive of Metro South Health of 5 June 2026, reference K-LM26/729, states "
         "that such a spreadsheet is available."),
 ("(c)", "Any communication from Human Resources, Logan and Beaudesert Health Service, to me between "
         "13 May 2024 and 9 October 2024."),
 ("(d)", "Any document recording the outcome of, or the steps taken in respect of, the complaint I "
         "sent to MetroSouthESU, CO_Complaints and LBH_HR on 15 May 2024."),
]
rows2 = [[P("", CH), P("", CH)]]
rows2 = []
for a, b in p2:
    rows2.append([P(f"<b>{a}</b>", C), P(b, C)])
t2 = Table(rows2, colWidths=[10*mm, 168*mm])
t2.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
    ('LINEBELOW',(0,0),(-1,-2),0.3,colors.HexColor('#cccccc'))]))
st.append(t2)

st.append(P("Reciprocal disclosure", H2))
st.append(P("I enclose my own list of documents in Form 23. Any of the documents in it may be "
            "inspected or copied on request, and I will provide copies electronically in the same "
            "way I have asked for the Respondent's.", B))

st.append(P("Timing", H2))
st.append(P("So that the material can be considered before the outlines are due, I would be grateful "
            "to receive the Part 1 copies by <b>Friday 29 August 2026</b>. If that is not "
            "practicable for any item, please let me know which items and by when they can be "
            "provided, and I will work to that. Nothing in this letter is intended to require any "
            "step beyond ordinary inspection.", B))

st.append(Spacer(1, 4*mm))
st.append(P("Yours faithfully", B))
st.append(Spacer(1, 8*mm))
st.append(P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(18*mm, 10*mm, "WC/2024/227 - request for copies of listed documents - 22 August 2026")
    cv.drawRightString(A4[0]-18*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=16*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(18*mm, 16*mm, A4[0]-36*mm, A4[1]-32*mm)],
                                   onPage=foot)])
doc.build(st)
buf.seek(0)
p = pikepdf.open(buf)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(p.pages)}")
