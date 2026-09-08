#!/usr/bin/env python3
"""WC/2024/227 - estimated Respondent expenditure on defending the appeal, to 23 August 2026.

INTERNAL WORKING DOCUMENT. Not for service.
No document ties any expenditure to this matter. The estimate is built from (a) the procedural
steps actually taken, verified from the file, and (b) rates observable in the Office of Industrial
Relations' own published contract disclosure for October-December 2024.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/RESPONDENT_SPEND_ESTIMATE.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.6, leading=13.5,
                     spaceBefore=9, spaceAfter=4)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.1, leading=12.6, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
R   = ParagraphStyle('R', parent=C, alignment=2)
RH  = ParagraphStyle('RH', parent=CH, alignment=2)
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

st = [P("Estimated Respondent expenditure on defending WC/2024/227, to 23 August 2026", H1),
      P("Internal working document &middot; 23 August 2026 &middot; an ESTIMATE, not a finding "
        "&middot; not for service", SUB)]

st.append(P("&#9888; <b>No document ties any expenditure to this matter.</b> This is built from the "
            "procedural steps actually taken, priced against rates observable in the Office of "
            "Industrial Relations' own published contract disclosure for the quarter containing the "
            "review decision. Every figure is a range, and the ranges are wide on purpose.", W))

st.append(P("The rates, from the Regulator's own disclosure", H2))
st.append(P("OIR's October to December 2024 contract disclosure records what it actually pays for "
            "legal services. The pattern is <b>individual barristers briefed direct</b>:", B))
rows = [[P("Supplier", CH), P("Engagement", RH), P("Note", CH)]]
RATES = [
 ("Junior / mid barristers (Sapsford, Rashleigh, Marxson, McMillan, O'Connor, Cartledge, Cooper, Clark, McLeod, Gunn, O'Neill)",
  "$10,100 &ndash; $20,000", "Typical single engagement. Sapsford appears 8 times in one quarter"),
 ("<b>Stephen Gray</b>", "$17,205.02", "<b>PDF author of the Form 24 response in this matter</b>"),
 ("<b>Lisa Willson</b>", "$18,298.60", "<b>Respondent's counsel in this appeal</b>"),
 ("Glen Rice QC", "$38,500.00", "Silk"),
 ("Ruth O'Gorman KC", "$20,625.00", "Silk"),
 ("Crown Law", "$129,879.75", "In-house government legal"),
]
for a,b,c in RATES: rows.append([P(a, C), P(b, R), P(c, C)])
t = Table(rows, colWidths=[76*mm, 32*mm, 70*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
    ('BACKGROUND',(0,2),(-1,3),colors.HexColor('#f6ecec'))]))
st.append(t)

st.append(P("The steps actually taken, and what each plausibly cost", H2))
rows = [[P("Step", CH), P("Date", CH), P("Low", RH), P("High", RH)]]
STEPS = [
 ("File opened; Notice of Appeal reviewed; first list of documents settled", "Nov&ndash;Dec 2024", 1500, 3500),
 ("Statement of Facts and Contentions (Form 9C) drafted and served", "Jul 2025", 3000, 8000),
 ("Notices of non-party disclosure &times;3 (Mind and Memory, Our Medical Ashmore, Queensland Health); records obtained and reviewed", "Jul 2025", 2500, 6000),
 ("<b>Witness conferencing &times;3</b> (Ms Reese 8 Jul, Ms Taylor 10 Jul, Ms Christesen 11 Jul), and the disclosure produced from it", "Jul 2025", 5000, 12000),
 ("Three amended directions orders &mdash; correspondence and compliance", "Jun&ndash;Aug 2025", 1500, 4000),
 ("<b>Response to the notice to admit facts (Form 24)</b> &mdash; 46 paragraphs answered", "Feb 2026", 6000, 17000),
 ("Section 552A conference &mdash; preparation and attendance", "Mar 2026", 3000, 8000),
 ("Amended Statement of Facts and Contentions", "May 2026", 3000, 7000),
 ("Further notice of non-party disclosure (Queensland Health payroll)", "Apr 2026", 1000, 3000),
 ("Supplementary disclosure to the Appellant assembled and served", "Jun 2026", 1500, 4000),
 ("Two Calderbank offers considered and answered", "Jul 2026", 2000, 5000),
 ("<b>Application under rule 64G &mdash; response, and the mention before Commissioner Dwyer</b> (counsel briefed)", "Jun&ndash;Aug 2026", 6000, 15000),
 ("Amended list of documents (52 items)", "Aug 2026", 1500, 4000),
 ("Further Directions Order (3) &mdash; correspondence, programming", "Aug 2026", 500, 1500),
]
lo=hi=0
for a,b,l,h in STEPS:
    lo+=l; hi+=h
    rows.append([P(a, C), P(b, C), P(f"${l:,}", R), P(f"${h:,}", R)])
rows.append([P("<b>Sub-total &mdash; identifiable steps</b>", CH), P("", C),
             P(f"<b>${lo:,}</b>", RH), P(f"<b>${hi:,}</b>", RH)])
t = Table(rows, colWidths=[104*mm, 26*mm, 24*mm, 24*mm], repeatRows=1)
sty=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
     ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
     ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
     ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
     ('BACKGROUND',(0,len(STEPS)+1),(-1,len(STEPS)+1),colors.HexColor('#e4e4e4'))]
t.setStyle(TableStyle(sty)); st.append(t)
st.append(Spacer(1,2*mm))
st.append(P("<b>Not included above:</b> the appeals officer's own time. Ms Matheson has had carriage "
            "for twenty-one months across four directions orders, two amended pleadings, two lists "
            "of documents, three witness conferences, four notices of non-party disclosure, a "
            "conference, a notice to admit facts, an application under rule 64G and two Calderbank "
            "offers. At a Senior Appeals Officer's fully-loaded cost of roughly $80 to $95 an hour, "
            "<b>150 to 250 hours is conservative: $12,000 to $24,000.</b>", B))

st.append(P("The estimate", H2))
rows=[[P("", CH), P("Low", RH), P("Mid", RH), P("High", RH)]]
rows.append([P("External legal (counsel, briefs, advice)", C), P(f"${lo:,}", R),
             P(f"${(lo+hi)//2:,}", R), P(f"${hi:,}", R)])
rows.append([P("Appeals officer time", C), P("$12,000", R), P("$18,000", R), P("$24,000", R)])
rows.append([P("<b>TOTAL TO DATE</b>", CH), P(f"<b>${lo+12000:,}</b>", RH),
             P(f"<b>${(lo+hi)//2+18000:,}</b>", RH), P(f"<b>${hi+24000:,}</b>", RH)])
t=Table(rows, colWidths=[86*mm, 30*mm, 30*mm, 32*mm])
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
    ('BACKGROUND',(0,3),(-1,3),colors.HexColor('#eef3ee'))]))
st.append(t)
st.append(Spacer(1,2*mm))
st.append(P(f"⇒ <b>Most likely in the order of ${(lo+hi)//2+18000:,}</b>, on a range of roughly "
            f"<b>${lo+12000:,} to ${hi+24000:,}</b>, to 23 August 2026.", B))

st.append(P("And what a hearing adds", H2))
st.append(P("A contested two to three day hearing in the Commission &mdash; counsel's brief on "
            "hearing, refreshers, preparation, the witnesses, written closing submissions &mdash; "
            "adds on these rates <b>$20,000 to $45,000</b> in counsel fees alone, before the "
            "appeals officer's own preparation. <b>The Respondent's exposure roughly doubles by "
            "running it.</b>", B))

st.append(P("Why this matters, and the two places it bites", H2))
st.append(P("<b>1. Settlement economics.</b> The question for the Respondent is not what it has "
            "already spent &mdash; that is sunk &mdash; but what the <i>remaining</i> hearing costs "
            "it against the value of the claim. When the marginal cost of running a hearing "
            "approaches or exceeds the cost of accepting the claim, settlement becomes rational "
            "regardless of the merits. <b>That crossover is what a second section 552A conference "
            "exists to find.</b>", B))
st.append(P("<b>2. Section 558(3) WCRA.</b> Costs of the hearing are in the appeal body's "
            "discretion, and section 560 makes an order an enforceable debt. <b>The Calderbank "
            "offer of 1 July 2026 was rejected on 16 July 2026.</b> If the Appellant obtains an "
            "outcome at hearing at least as favourable as that offer, the rejection is precisely "
            "the material a costs application is built on &mdash; and the figures above are the "
            "order of magnitude at stake.", B))
st.append(P("&#9888; <b>Do not put any of this to the Respondent, and do not raise expenditure at a "
            "conference.</b> It reads as pressure rather than merit, and the numbers are estimates "
            "that could be corrected against the Respondent's actual records to the Appellant's "
            "embarrassment. It is a private planning input only.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - estimated Respondent expenditure - internal, not for service")
    cv.drawRightString(PW-16*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=15*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, PW-32*mm, PH-31*mm)],
                                   onPage=foot)])
doc.build(st); buf.seek(0)
p = pikepdf.open(buf)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(p.pages)} | range ${lo+12000:,} - ${hi+24000:,} | mid ${(lo+hi)//2+18000:,}")
