#!/usr/bin/env python3
"""WC/2024/227 - the 2024 pay cycle and where the AVAC correction had to land.

INTERNAL WORKING DOCUMENT. Not for service. It contains the Appellant's own
evidence and an inference, both marked as such, alongside documented facts.

The fortnight is derived from the FY2025-26 payslips: each period ends on a
Sunday and is paid the Wednesday 10 days later. Verified against three payslips
a year apart (02/07/2025, 16/07/2025, 17/06/2026), so the projection back to
2024 is arithmetic, not assumption. The AMOUNTS are not known - the repository
holds no 2024 payslip.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/PAY_CYCLE_2024_and_the_AVAC.pdf"
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.2, leading=13,
                     spaceBefore=6, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=4)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=12.4, spaceAfter=3)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.3, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

# pay date, period, what it covers, marker
ROWS = [
 ("14/02/2024","22/01 to 04/02/2024","",""),
 ("28/02/2024","05/02 to 18/02/2024","Underpayment period begins (SOFC 2(a): February to April 2024)","o"),
 ("13/03/2024","19/02 to 03/03/2024","",""),
 ("27/03/2024","04/03 to 17/03/2024","",""),
 ("10/04/2024","18/03 to 31/03/2024","Contains the shifts of 17-18 March and the leave of 19 March 2024","o"),
 ("24/04/2024","01/04 to 14/04/2024","",""),
 ("08/05/2024","15/04 to 28/04/2024","Underpayment period ends","o"),
 ("22/05/2024","29/04 to 12/05/2024","3 May: payroll identifies the errors and instructs an AVAC. "
  "10 May: the Appellant emails payroll. 13 May: payroll confirms nothing has been corrected","x"),
 ("05/06/2024","13/05 to 26/05/2024","<b>The next pay run after the AVAC of 28 May 2024</b> - the run "
  "the Line Manager's email of 21 May refers to","X"),
 ("19/06/2024","27/05 to 09/06/2024","<b>The last pay run covering days actually worked.</b> Last day "
  "worked about 3 June 2024; date of injury 18 June 2024","X"),
 ("03/07/2024","10/06 to 23/06/2024","No days worked","o"),
 ("17/07/2024","24/06 to 07/07/2024","12 and 18 July: the Appellant tells WorkCover that entitlements "
  "remain unpaid","x"),
]

st = [P("The 2024 pay cycle, and where the correction to the shifts had to land", H1),
      P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; internal working "
        "document, 22 August 2026 &middot; not for service", SUB)]

st.append(P("The fortnight is taken from the payslips: each period ends on a Sunday and is paid on "
            "the Wednesday ten days later. That interval is identical on the payslips of 2 July 2025, "
            "16 July 2025 and 17 June 2026, a year apart, so the projection back to 2024 is arithmetic. "
            "<b>The amounts are not known.</b> No 2024 payslip is held.", B))

rows = [[P("Pay date", CH), P("Period", CH), P("", CH)]]
for pd, per, note, mk in ROWS:
    rows.append([P(f"<b>{pd}</b>" if mk == "X" else pd, C), P(per, C), P(note, C)])
t = Table(rows, colWidths=[22*mm, 32*mm, 116*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]
for i,(pd,per,note,mk) in enumerate(ROWS, start=1):
    if mk == "X": sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif mk == "x": sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f4f4f4')))
t.setStyle(TableStyle(sty))
st += [t, Spacer(1,4*mm)]

st.append(P("What the two shaded pay runs mean", H2))
st.append(P("Payroll identified the errors on <b>3 May 2024</b> and instructed that an AVAC be "
            "submitted to correct the shifts. That is admitted (notice to admit facts, paragraph 40). "
            "The AVAC was submitted by the Line Manager on <b>28 May 2024</b>. That is also admitted "
            "(response to the notice to admit facts, paragraph 38), which adds that on 21 May she said "
            "she would submit an AVAC <i>“for the next pay run”</i>.", B))
st.append(P("On the cycle, the next pay run was <b>5 June 2024</b>. The only other run covering days "
            "actually worked was <b>19 June 2024</b> - the day after the pleaded date of injury, and "
            "about a fortnight after the last day worked. After that there were no worked days for a "
            "correction to attach to.", B))
st.append(P("&#9733; <b>CORRECTED 23 August 2026.</b> The employer's confirmation letter of 9 October 2024 states in terms: <i>&ldquo;Your last day of attendance for a rostered shift was 3 June 2024&rdquo;</i>. The pay run of <b>19 June 2024</b> therefore covers only 27 May to 3 June of its period, and nothing worked after that. <b>The correction had ONE clear opportunity to reach him on a full worked fortnight - 5 June 2024 - not two.</b>", B))

st.append(P("What is documented, and what is not", H2))
st.append(P("<b>Documented.</b> That the errors existed; that payroll identified them on 3 May and "
            "instructed a correction; that on 13 May payroll told the Appellant nothing had been "
            "corrected; that on 21 May the Line Manager was still waiting; that the AVAC went in on "
            "28 May; and that on <b>12 and 18 July 2024</b> - six and seven weeks after the AVAC - the "
            "Appellant was still telling WorkCover that entitlements were unpaid, including payment for "
            "recognised education, pandemic-leave income, a cancelled shift and overtime "
            "(Review Decision 69983, page 14).", B))
st.append(P("<b>Not documented.</b> Whether the correction was in fact paid on 5 or 19 June 2024. The "
            "repository holds no 2024 payslip. The employer told WorkCover on 6 September 2024 that "
            "<i>“corrective action was taken by Ms Taylor as per internal processes to correct the "
            "payroll and entitlement errors”</i>, and the review accepted that various actions were "
            "taken. That is the answer to be met.", B))
st.append(P("<b>The Appellant's evidence.</b> That he did not sign the AVAC, was not told it had been "
            "submitted, was never shown any calculation, and that pay continued on the ordinary "
            "fortnightly cycle with no correction appearing - so the money identified on 3 May 2024 was "
            "never in his hand while he was working. This is evidence for the witness outline. It is "
            "not in the schedule of events, which is confined to documents.", B))

st.append(P("What closes it", H2))
st.append(P("<b>The payslips for pay dates 5 June 2024 and 19 June 2024.</b> Two documents. If neither "
            "carries the correction, the employer's answer that corrective action was taken stops being "
            "an answer, and the stressor changes from a 25-day delay - admitted but small - to an "
            "identified underpayment that was still unpaid when the Appellant stopped work. Obtainable "
            "from myHR or by request to Queensland Health Payroll.", B))
st.append(P("Note that the route through the Commission has closed. Item 16 of the notice of non-party "
            "disclosure sought the AVAC payroll export for PRN 15397775 and PRN 15605601 for 1 to 31 May "
            "2024. Metro South produced daily staffing variance forms instead, and for February and "
            "March rather than May. Item 16 was pressed in the application under rule 64G, and that "
            "application was withdrawn on 10 August 2026. No order compels the export.", W))
st.append(P("<b>Also to be pinned:</b> the last day actually worked. It is recorded in the working "
            "papers as about 3 June 2024 and has never been verified against a roster or payslip. It "
            "decides which of the two pay runs is the last one that matters.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - pay cycle 2024 - internal working document, not for service")
    cv.drawRightString(A4[0]-16*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=15*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, A4[0]-32*mm, A4[1]-31*mm)],
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
