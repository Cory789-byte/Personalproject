#!/usr/bin/env python3
"""WC/2024/227 - Review Decision 69983: what was found on assertion, and what document now answers it.

INTERNAL WORKING DOCUMENT. Not for service.

Every quotation is taken from Review Decision 69983 at the page stated, read from the source PDF.
Every answering document is one already disclosed in this proceeding.

The point is NOT that the review was defective - the appeal is de novo and that is not a ground.
The point is that six findings rest on the employer's own assertion, and documents produced since
answer five of them. That is a cross-examination map, not an appeal ground.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/RD69983_EVIDENCE_AUDIT.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.4, leading=13,
                     spaceBefore=8, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=12.4, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.1, leading=10.8)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

# n, the finding (quoted), page, source relied on, the answering document, weight
ROWS = [
 ("1", "Factor 1 &mdash; the Line Manager's attendance",
  "&ldquo;the employer wrote this was incorrect and Ms Taylor <b>consistently fulfilled her "
  "contracted hours each week</b> and adhered to the employer's flexible working arrangement "
  "policy&hellip; <b>there were no concerns regarding her punctuality or attendance</b>.&rdquo;",
  "p 11", "The employer's letter of 15 August 2024. <b>No timesheet, roster or attendance record "
  "for Ms Taylor is identified anywhere in the reasons.</b>",
  "Letter of the Chief Executive, 5 June 2026 (K-LM26/729): the Line Manager was <b>not issued a "
  "Queensland Health mobile device</b> until about the third quarter of 2024, and the SMS in issue "
  "was sent from her personal device. Ms Stibbard's email of 18 July 2023.", 2),
 ("2", "Factor 1 &mdash; recruitment",
  "&ldquo;With respect to the hire of employees, <b>I find the employer did not breach the rules "
  "and adhered to their policies</b>.&rdquo;",
  "p 11", "The employer's letter of 15 August 2024. No recruitment file, expression-of-interest "
  "record or selection documentation is identified.",
  "Not answered by any document now held. <b>Leave it alone.</b>", 0),
 ("3", "Factor 1 &mdash; process and structural changes",
  "&ldquo;you did not provide evidence in support of your submission that changes made to "
  "processes and structures were in violation of rules, and <b>the employer confirmed the changes "
  "were valid</b>.&rdquo;",
  "p 11", "The employer's letter. No consultation record is identified.",
  "Letter of the Chief Executive, 5 June 2026: <b>&ldquo;no &lsquo;consequential&rsquo; changes to "
  "operating procedures over the period requested&rdquo;</b> (Item 3(c)) &mdash; which sits against "
  "the directives of 15 April and 19 April 2024 and the restriction of directory updates on "
  "18 July 2023.", 1),
 ("4", "Factor 2 &mdash; the complaint process",
  "&ldquo;<b>The employer conceded this was true</b> [that no formal investigation was undertaken], "
  "but submitted this was because they required further information from you and <b>despite "
  "requesting it, you refused to participate</b>&hellip; I find Ms Reese contacted you twice in an "
  "attempt to schedule a meeting&hellip;&rdquo;",
  "pp 17-18", "The employer's letter of 15 August 2024. <b>No Ethical Standards Unit file, no email "
  "from the Unit requesting information, and no record of Ms Reese's contact attempts is "
  "identified.</b>",
  "The Ethical Standards Unit's own determination of <b>24 December 2024</b> &mdash; two months "
  "after this decision &mdash; that the matter constituted a public interest disclosure "
  "(admitted, notice to admit facts para 20). &#9888; Verify whether that determination attaches to "
  "the complaint of 13 May 2024 or to the later complaint of 30 August 2024 before this is used.", 3),
 ("5", "Factor 3 &mdash; the pay issues",
  "&ldquo;<b>the pay issues ultimately were all resolved</b>. Ms Taylor, payroll and Human "
  "Resources were <b>always encouraging</b> of you expressing your issues as soon as possible, were "
  "<b>attentive</b> to the issues you expressed and undertook necessary reviews and corrective "
  "actions to resolve them.&rdquo;",
  "pp 21-22", "The employer's letter of 6 September 2024 (&ldquo;corrective action was taken by Ms "
  "Taylor as per internal processes&rdquo;). <b>No payroll correspondence, no AVAC record and no "
  "payslip is identified.</b>",
  "&#9733; The email thread <i>&ldquo;Corey Shepherd 388372 Pay issues&rdquo;</i>, from the "
  "Respondent's own July 2025 disclosure: <b>13 May 2024, payroll to the Appellant &mdash; &ldquo;I "
  "cannot see that any of the issues below have been corrected&rdquo;</b>; 21 May, the Line Manager "
  "&mdash; &ldquo;I am still I am waiting payroll confirmation&rdquo;. And the myHR submissions "
  "report produced as Item 11: five claims, <b>all initiated by the Line Manager</b>; the claim of "
  "15 May completed in <b>one day</b>; the correction claim of 28 May recorded <b>&ldquo;Part "
  "Completed&rdquo;</b> &mdash; the only one of the five not completed.", 3),
 ("6", "Factor 4 &mdash; the 2020 agreement",
  "&ldquo;<b>The employer also confirmed you did not formally rescind the 8-hour agreement</b> "
  "signed by you on 17 June 2020 and the change to your employment contract and adjustments in "
  "your working hours did not automatically invalidate the agreement. <b>That meant it remained "
  "current.</b>&rdquo;",
  "p 15", "The employer's letter. The agreement's own <b>scope</b> is not analysed.",
  "&#9733; Letter of Ms L Forrest, 7 July 2026: the 2020 agreement <b>&ldquo;is only applied where "
  "staff initiated shift swaps have occurred&rdquo;</b>. The shifts of 17 and 18 March 2024 were "
  "<b>rostered</b>, not swapped. That is the employer's own later position, and it is not the "
  "position it put to the reviewer.", 3),
]

st = [P("Review Decision 69983 &mdash; what was found on assertion, and what answers it now", H1),
      P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; internal working "
        "document, 22 August 2026 &middot; not for service", SUB)]

st.append(P("Every quotation below is from Review Decision 69983 at the page stated, read from the "
            "source. Every answering document is one already disclosed in this proceeding.", B))

st.append(P("The count", H2))
st.append(P("<b>Six findings rest on an assertion by the employer with no underlying document "
            "identified in the reasons.</b> Against that, the reviewer three times rejected the "
            "Appellant's assertions for want of documents:", B))
st.append(P("&bull; &ldquo;<b>No evidence has been provided</b> in support of your assertion that "
            "management did not keep employees accountable&rdquo; (p 11)<br/>"
            "&bull; &ldquo;<b>you did not provide evidence</b> in support of your submission that "
            "changes made to processes and structures were in violation of rules&rdquo; (p 11)<br/>"
            "&bull; &ldquo;<b>No evidence has been provided</b> in support of the remainder of your "
            "assertions made in relation to the rostering&rdquo; (p 15)", C))
st.append(Spacer(1, 2*mm))
st.append(P("<b>Of the six, four are now answered or materially qualified by documents the employer "
            "or the Respondent has itself produced since.</b> None of those documents was before "
            "the reviewer.", B))

rows = [[P("#", CH), P("The finding, and what it rested on", CH), P("What answers it now", CH)]]
for n, head, quote, page, rested, answer, wt in ROWS:
    left = (f"<b>{n}. {head}</b> &nbsp;<font size=7 color='#666666'>({page})</font><br/>"
            f"<i>{quote}</i><br/><br/><font size=7.4>Rested on: {rested}</font>")
    rows.append([P(f"<b>{n}</b>", C), P(left, C), P(answer, C)])
t = Table(rows, colWidths=[7*mm, 92*mm, 79*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]
for i,(n,h,q,pg,r,a,wt) in enumerate(ROWS, start=1):
    if wt == 3: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif wt == 2: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f4f4f4')))
t.setStyle(TableStyle(sty))
st += [t, Spacer(1,3*mm)]

st.append(P("What the rosters covered, and what they did not", H2))
st.append(P("The reviewer did examine rosters &mdash; and should be given credit for it. She "
            "records the switchboard roster for 19 September to 2 October 2022, and for 4 to "
            "17 March, 18 to 31 March, 15 to 28 April and 29 April to 12 May 2024 (pp 14-15). "
            "<b>The roster examination stops on 12 May 2024.</b> The five weeks from 13 May to the "
            "date of injury on 18 June 2024 &mdash; which carry the MASPER direction of 9 May and "
            "its consequence on 15 May, the events of 13 to 15 May, and the direction to retract "
            "&mdash; are not covered by any roster in the reasons.", B))

st.append(P("What this is, and what it is not", H2))
st.append(P("<b>It is not a ground of appeal.</b> The appeal is de novo under s 550(4): the "
            "Commission decides the claim afresh and does not review these reasons for error. "
            "Saying the review was thin gains nothing before Commissioner Dwyer and risks reading "
            "as grievance.", W))
st.append(P("<b>It is a cross-examination map.</b> The employer will make the same six assertions "
            "again, because they are its case. This records which of them were accepted without a "
            "document, and which document now answers each. That is worth having in hand when the "
            "witnesses give evidence, and it is worth nothing at all in a submission.", B))
st.append(P("<b>And it answers one question the Respondent will ask.</b> If it is put that the "
            "Regulator has already considered these matters, the answer is not that the review was "
            "deficient. It is that the documents which answer four of its central findings were "
            "produced in 2026, by the employer and by the Respondent, and were not before the "
            "reviewer in October 2024.", B))

st.append(P("Before any of this is used", H2))
st.append(P("&#9888; <b>Item 4 needs verification.</b> The public interest disclosure determination "
            "of 24 December 2024 is admitted, but the file records it as made on the complaint of "
            "30 August 2024 referred back by the Crime and Corruption Commission on 22 November "
            "2024 &mdash; not necessarily on the complaint of 13 May 2024. Establish which before "
            "the point is put to anyone.", W))
st.append(P("&#9888; <b>Item 2 is not answered and should be left alone.</b> Nothing now held "
            "addresses the recruitment finding.", W))
st.append(P("&#9888; <b>Do not adopt the reviewer's language.</b> Her reasons repeat the "
            "Appellant's own words back at him &mdash; &ldquo;malicious intent&rdquo;, "
            "&ldquo;maliciously&rdquo;, and at p 23 &ldquo;an act of control and abuse&rdquo;. Those "
            "are on the record as history. They go to the worker's perception of management action, "
            "which is the excluded limb the Respondent has not pleaded, and they raise his own "
            "standard of persuasion. Quote the findings, never the characterisations.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - RD69983 evidence audit - internal working document, not for service")
    cv.drawRightString(PW-16*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=15*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, PW-32*mm, PH-31*mm)],
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
