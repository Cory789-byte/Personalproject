#!/usr/bin/env python3
"""WC/2024/227 - one-page element grid for the second s 552A conference.
Guide 7.3.2 elements, what proves each, and what is in issue. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle

BLUE = colors.HexColor('#123f8c'); GREY = colors.HexColor('#5a5a5a')
H1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=11.5, leading=14, spaceAfter=1)
H2 = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.0, leading=10, textColor=GREY, spaceAfter=5)
SEC= ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=8.6, leading=10.6, spaceBefore=5, spaceAfter=2)
B  = ParagraphStyle('B', fontName='Helvetica', fontSize=7.5, leading=9.2)
BB = ParagraphStyle('BB', parent=B, fontName='Helvetica-Bold')
SM = ParagraphStyle('SM', fontName='Helvetica', fontSize=7.2, leading=8.8, spaceAfter=2)
def P(t,s=B): return Paragraph(t,s)

rows=[[P("<b>Element</b>",BB), P("<b>What must be shown</b>",BB), P("<b>What proves it</b>",BB), P("<b>In issue?</b>",BB)],
 [P("<b>(a)</b> Worker",BB),
  P("a worker within the meaning of s 11 of the Act"),
  P("Employment records; role description (Notice &para;&para; 1 to 13, admitted); movement forms (&para;&para; 14 to 15, admitted)"),
  P("<b>No</b>")],
 [P("<b>(b)</b> Personal injury",BB),
  P("that a personal injury was sustained"),
  P("Dr Krishnaiah, diagnosis 24 Oct 2024 (Tab M3) and report 13 Feb 2025 (Tab M4); Dr Hawes, certificates 1 Jul to 6 Oct 2024 (Tab M2). "
    "<font color='#123f8c'><b>Review Decision 69983 found &quot;a personal injury of a psychological nature&quot; &mdash; &para; 261, admitted.</b></font>"),
  P("<b>Should not be</b>")],
 [P("<b>(c)</b> Arose out of, or in the course of, employment",BB),
  P("the connection between the injury and the employment"),
  P("The course of conduct at Part B.2 of the statement of facts and contentions, on the admitted paragraphs; treating records Tabs M1 to M4. "
    "<font color='#123f8c'><b>The decision so found &mdash; &para; 262, admitted.</b></font>"),
  P("<b>Should not be</b>")],
 [P("<b>(d)</b> Employment <b>a significant contributing factor</b>",BB),
  P("that employment was <b>a</b> significant contributing factor &mdash; <b>not the major one, and not the only one</b>"),
  P("Dr Krishnaiah and Dr Hawes <b>orally</b> (Guide 7.6.5); report of 13 Feb 2025, origin &quot;workplace stress stemming from issues with "
    "management and rostering&quot;; the baseline at Part B.1 &mdash; no diagnosis or treatment for depression before 18 Jun 2024, and no "
    "antidepressant, anxiolytic or other psychotropic medication as at 16 May 2024. "
    "<font color='#123f8c'><b>The decision so found &mdash; &para; 262, admitted.</b></font>"),
  P("<b>Possibly</b>")],
 [P("<b>s 32(5)(a)</b><br/>The additional requirement for a psychological injury",BB),
  P("that the injury was <b>not connected to management action that was reasonable in the circumstances and/or taken in a reasonable way</b> "
    "(Guide 7.3.2)"),
  P("<b>Contention 4</b> &mdash; circumstances that are <b>not management action</b> at all: the duty imposed while the means of discharging it "
    "was held by others; the emergency notifications; the directory entry; the complaints. <b>Contention 5</b> &mdash; if and to the extent they are "
    "management action, it was not taken in a reasonable way, measured against EB11 cl 3.2, 9.13.1, 9.14, 7.1.5 and Award cl 15.2, 11, 6.2. "
    "<font color='#123f8c'><b>The decision found the rostering of 17 and 18 March 2024 to be unreasonable management action &mdash; &para; 260, admitted.</b></font>"),
  P("<b>YES &mdash;<br/>the only<br/>live issue</b>",BB)],
]
t=Table(rows, colWidths=[27*mm, 40*mm, 82*mm, 17*mm], repeatRows=1)
t.setStyle(TableStyle([
 ('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#9aa4b5')),
 ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8ecf3')),
 ('BACKGROUND',(0,5),(-1,5),colors.HexColor('#fdf3e3')),
 ('VALIGN',(0,0),(-1,-1),'TOP'),
 ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
 ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))

s=[P("ELEMENTS OF SECTION 32 &mdash; WHAT IS, AND IS NOT, IN ISSUE", H1),
   P("WC/2024/227 &ndash; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent). "
     "Prepared for the second conference under s 552A of the <i>Workers' Compensation and Rehabilitation Act 2003</i>. "
     "Elements as stated at Part 7.3.2 of the Workers' Compensation Appeal Guide. The onus is on the Appellant (Guide 7.3); the standard is "
     "the balance of probabilities, applying <i>Briginshaw</i>.", H2),
   t, Spacer(1,3*mm),
   P("What the Appellant proposes", SEC),
   P("<b>That elements (a), (b), (c) and (d) be agreed, and that the hearing be confined to section 32(5)(a).</b> "
     "Each of (b), (c) and (d) was found by the Respondent's own review officer on 24 October 2024, and the Respondent admitted on "
     "8 September 2026 that the decision so records (&para;&para; 260 to 262). The Appellant accepts that the hearing is <i>de novo</i> and that "
     "those findings do not bind the Commission; they are relied upon as an admitted document. If any of (a) to (d) is in issue, the Appellant "
     "asks that it be identified now so that the evidence can be directed to it.", B),
   Spacer(1,2*mm),
   P("Notes", SEC),
   P("<b>1. &nbsp;“a significant contributing factor”.</b> Section 32(1) requires employment to be <b>a</b> significant contributing factor. "
     "The “major significant” test for psychiatric injury was repealed in 2019. Competing causes need not be outweighed; they need only leave "
     "employment as a significant contributor.", SM),
   P("<b>2. &nbsp;Section 32(5)(b) is not in issue.</b> The Respondent has not pleaded that the injury is connected to the Appellant's "
     "expectation or perception of reasonable management action, and the Appellant does not rely on any such matter.", SM),
   P("<b>3. &nbsp;Clinical opinion.</b> The Appellant does not rely on the opinion in any medical document otherwise than through the oral "
     "evidence of its author (Guide 7.6.5). Dr Ravikumar Bangalore Krishnaiah and Dr Peter Hawes are named at items 2 and 3 of the "
     "Appellant's list of witnesses filed 9 September 2026 and will be called.", SM),
   P("<b>4. &nbsp;The admitted record.</b> References to &para; are to the notice to admit facts served 28 August 2026, of which 298 of 303 "
     "paragraphs were admitted, and none denied, in the Respondent's response of 8 September 2026. The admissions are made for this "
     "proceeding only under rule 49 of the <i>Industrial Relations (Tribunals) Rules 2011</i>.", SM)]

buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=14*mm,rightMargin=14*mm,topMargin=11*mm,bottomMargin=11*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(14*mm,11*mm,A4[0]-28*mm,A4[1]-22*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
assert n==1, f"element grid must be ONE page, got {n}"
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/ELEMENT_GRID_s32_for_conference.pdf"; pdf.save(out,linearize=True); print("built",out,n,"page")
