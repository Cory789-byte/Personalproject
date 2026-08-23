#!/usr/bin/env python3
"""WC/2024/227 - the abandonment sequence, September to November 2024.

Built 23 August 2026 from the source documents supplied that day:
  LTR_Abandonment_of_Employment_Show_Cause_Shepherd_Cory.pdf   (ref K-CF24/3196)
  LTR_Confirmation_of_Abandonment_of_Employment_Cory_Shepherd.pdf (ref K-CF24/3270)
  Re_Correspondence_from_the_Executive_Director....eml          (his reply, 11 Oct 2024)
INTERNAL WORKING DOCUMENT. Not for service.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/ABANDONMENT_SEQUENCE_2024.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.6, leading=13.5,
                     spaceBefore=9, spaceAfter=4)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.1, leading=12.6, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

st = [P("The abandonment sequence &mdash; June to November 2024", H1),
      P("WC/2024/227 &middot; built 23 August 2026 from the show cause letter (K-CF24/3196), the "
        "confirmation letter (K-CF24/3270) and the reply email &middot; internal working document, "
        "not for service", SUB)]

# when, what, source, weight
SEQ = [
 ("Mon 3 Jun 2024", "<b>Last day of attendance at a rostered shift.</b> &ldquo;Your last day of "
  "attendance for a rostered shift was 3 June 2024&rdquo;", "Confirmation letter", 3),
 ("7&ndash;12 Jun 2024", "Approved leave: 7 Jun recreation in lieu of sick; 8 Jun sick and "
  "recreation in lieu; 9 Jun sick; 10 Jun leave without pay; <b>11&ndash;12 Jun bereavement</b>",
  "Confirmation letter", 1),
 ("from 13 Jun 2024", "Placed on leave without pay", "Confirmation letter", 0),
 ("Tue 18 Jun 2024", "<b>Pleaded date of injury</b>", "Amended SOFC", 2),
 ("Fri 21 Jun 2024", "Last correspondence Ms Taylor records receiving from him", "Confirmation letter", 1),
 ("Mon 1 Jul 2024", "Application for compensation; first medical certificate, Dr P Hawes", "Repo", 0),
 ("Mon 15 Jul 2024", "Text to the Line Manager's personal phone &mdash; &ldquo;the last reported "
  "contact&rdquo; on the employer's account", "Show cause letter", 1),
 ("Fri 13 Sep 2024", "WorkCover Queensland reasons for decision", "Repo &middot; Respondent's list item 2", 2),
 ("Thu 19 Sep 2024", "&#9888; The employer's letters twice state the claim was declined on this "
  "date, and the show cause letter states the last day of work &ldquo;will be considered to "
  "be&rdquo; <b>19 September 2024</b>", "Both letters", 3),
 ("Fri 20 Sep 2024, 8:38 am", "Line Manager emails re the work capacity checklist and leave balances",
  "Show cause letter", 0),
 ("Tue 24 Sep 2024, 11:16 am", "Line Manager text", "Show cause letter", 0),
 ("Wed 25 Sep 2024, 8:32 / 8:43 am", "Line Manager telephone call, unanswered; then email",
  "Show cause letter", 0),
 ("Thu 26 Sep 2024, 10:58 / 11:18 am", "Line Manager telephone call, unanswered; then text",
  "Show cause letter", 0),
 ("Thu 26 Sep 2024", "<b>SHOW CAUSE LETTER signed by Ms Anne Coccetti, Executive Director</b> "
  "(K-CF24/3196). Seven calendar days to respond. Quotes Award clause 9.6", "Show cause letter", 3),
 ("Mon 16 Sep 2024", "Application for review lodged with the Regulator", "Repo", 0),
 ("Wed 2 Oct 2024", "HopgoodGanim engaged <b>by the Office of Industrial Relations</b>, $13,200",
  "OIR contract disclosure", 1),
 ("Thu 3 Oct 2024", "<b>His response received by Human Resources</b>", "Confirmation letter", 2),
 ("Wed 9 Oct 2024, 4:10 pm", "<b>CONFIRMATION LETTER transmitted</b> by Ms Faiza Firoz, signed "
  "<b>Mr Steven Johns, A/Executive Director</b> (K-CF24/3270). <b>Nominates the separation date as "
  "20 September 2024</b>", "Confirmation letter &middot; email header", 3),
 ("Fri 11 Oct 2024, 3:15 pm", "<b>His reply sent</b> &mdash; contests the letter, asserts protected "
  "status, work capacity certificate provided, upcoming psychiatric appointment, requests leave and "
  "entitlements be actioned", "Reply email", 2),
 ("Tue 22 Oct 2024", "Review decision made &mdash; day 25 of the 25 business days", "Review Decision", 1),
 ("Thu 24 Oct 2024", "Reasons for decision dated and issued", "Review Decision", 1),
 ("Fri 25 Oct 2024", "Reinstatement application TD/2024/110 stamped", "Repo", 0),
 ("Tue 26 Nov 2024", "Notice of Appeal filed", "Repo", 0),
]
rows = [[P("When", CH), P("What", CH), P("Source", CH)]]
for w, what, src, wt in SEQ:
    rows.append([P(f"<b>{w}</b>", C), P(what, C), P(src, C)])
t = Table(rows, colWidths=[34*mm, 110*mm, 34*mm], repeatRows=1)
sty=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
     ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
     ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
     ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
for i,(w,what,src,wt) in enumerate(SEQ, start=1):
    if wt==3: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif wt==2: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f2f2f2')))
t.setStyle(TableStyle(sty)); st.append(t)

st.append(P("&#9733; The structural problem &mdash; on the employer's own quoted clause", H2))
st.append(P("The show cause letter sets out Award clause 9.6(c) in full:", B))
st.append(P("<i>&ldquo;Termination of employment by abandonment in accordance with clause 9.6 will "
            "operate as from the date of the employee's: (i) last attendance at work; or (ii) last "
            "absence in respect of which consent was granted by the employer; or (iii) last absence "
            "in respect of which the notification was given to the employer by the employee, "
            "<b>whichever is the latter</b>.&rdquo;</i>",
            ParagraphStyle('q', parent=B, leftIndent=8*mm, fontName='Helvetica-Oblique')))
st.append(P("On the employer's own findings the three candidate dates are: <b>3 June 2024</b> (last "
            "attendance), <b>12 June 2024</b> (last consented absence), and the last notified "
            "absence &mdash; on their account either <b>21 June</b> or <b>15 July 2024</b>.", B))
st.append(P("<b>The separation date nominated is 20 September 2024. That is none of the three, and "
            "it is not the latter of them.</b> It is the day after the date the letters give for the "
            "WorkCover decline. Clause 9.6(c) does not provide for it.", W))

st.append(P("&#9888; Four further date conflicts on the face of the documents", H2))
rows=[[P("#", CH), P("Conflict", CH)]]
CON=[
 ("1","The show cause letter is <b>signed and dated 26/09/2024</b>. The confirmation letter refers "
  "to it as <i>&ldquo;the letter from Ms Anne Coccetti&hellip; <b>dated 27 September 2024</b>&rdquo;</i>. "
  "The seven-day response period runs from a date the two documents state differently."),
 ("2","The show cause letter says the last day of work <b>&ldquo;will be considered to be 19 "
  "September 2024&rdquo;</b>. The confirmation letter nominates the separation date as <b>20 "
  "September 2024</b>. One day apart, and neither is a clause 9.6(c) date."),
 ("3","Both letters state the claim was declined on <b>19 September 2024</b>. The repository and "
  "the Respondent's own list of documents record WorkCover's reasons for decision as <b>13 "
  "September 2024</b>. &#9888; Pin which is correct before either is relied on."),
 ("4","The Amended Statement of Facts and Contentions at paragraph 43 pleads <i>&ldquo;On <b>8 "
  "October 2024</b> my employment was terminated&rdquo;</i>. <b>No document supports 8 October.</b> "
  "The letter is transmitted 9 October and nominates 20 September. &#9888; <b>This is the "
  "Appellant's own pleading and it should be corrected or explained before 9 September 2026.</b>"),
]
for a,b in CON: rows.append([P(f"<b>{a}</b>", C), P(b, C)])
t=Table(rows, colWidths=[8*mm, 170*mm])
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
    ('BACKGROUND',(0,4),(-1,4),colors.HexColor('#f6ecec'))]))
st.append(t)

st.append(P("What this closes, and what it opens", H2))
st.append(P("<b>CLOSED &mdash; the last day worked.</b> Recorded in the working papers as "
            "&ldquo;about 3 June 2024&rdquo; and unverified. It is now confirmed in writing by the "
            "employer: <b>3 June 2024</b>. &#9733; That changes the pay-cycle analysis: the pay run "
            "of <b>19 June 2024</b> covered no worked days, so the correction of 28 May 2024 had "
            "<b>only one</b> opportunity to reach him while working &mdash; <b>5 June 2024</b>, not "
            "two.", B))
st.append(P("<b>OPENED &mdash; a documented Regulator-to-employer channel.</b> The confirmation "
            "letter records: <i>&ldquo;MSH has received correspondence from the <b>Office of "
            "Industrial Relations</b> regarding your application to review the decision made by "
            "WorkCover Queensland&hellip;&rdquo;</i> Ordinary &mdash; the employer was a party and "
            "made submissions on 15 August and 6 September 2024 &mdash; but it is the first "
            "documented instance of that channel, and it is in their own letter.", B))
st.append(P("<b>USEFUL &mdash; their own dating of last contact.</b> <i>&ldquo;Ms Reece and Ms "
            "Taylor have confirmed the last correspondence they have received from you was on 15 "
            "May 2024 and 21 June 2024 respectively.&rdquo;</i> The 21 June date is <b>after</b> the "
            "last shift and <b>after</b> the pleaded injury, which sits against the "
            "no-contact framing.", B))

st.append(P("&#9888; Handling", H2))
st.append(P("This is employment-track material. The abandonment is pleaded in the appeal only at "
            "Part B item 3 as subsequent aggravating conduct, and the Respondent contends at "
            "paragraph 25 of its own pleading that post-injury matters are not relevant. <b>Use the "
            "3 June date, which is squarely relevant to the pay cycle. Fix the paragraph 43 "
            "discrepancy because it is the Appellant's own. Do not run the clause 9.6(c) point in "
            "the appeal</b> &mdash; it belongs to the reinstatement matter, which succeeded, and "
            "raising it here invites the relevance objection the Respondent has already flagged.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - abandonment sequence 2024 - internal, not for service")
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
print(f"built {OUT} pages: {len(p.pages)}")
