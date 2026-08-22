#!/usr/bin/env python3
"""WC/2024/227 - the dated sequence of 3 to 28 May 2024.

INTERNAL WORKING DOCUMENT. Not for service, and not for a filing in this form.

Every entry is taken from a document in the Respondent's own disclosure, at the
source and page stated, or is an admitted fact. Nothing is reconstructed.

Read the risk section before this is used anywhere.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/MAY_2024_SEQUENCE.pdf"
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.2, leading=13,
                     spaceBefore=7, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=12.4, spaceAfter=3)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=10.8)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

# when, what, source, weight (2 = pay thread, 1 = the complaint track, 3 = both/critical)
SEQ = [
 ("Fri 3 May, 9:39 am", "Payroll (Ms E Grant) to the Line Manager, copied to the Appellant: "
  "&ldquo;Please submit an AVAC to correct these shifts for each fortnight&rdquo;",
  "Payroll disclosure p.5", 2),
 ("Fri 10 May, 2:21 pm", "The Appellant to Payroll, asking whether the Line Manager has responded",
  "Payroll disclosure p.5", 2),
 ("Mon 13 May", "The Appellant lodges the complaint with the Ethical Standards Unit. Later "
  "determined to be a public interest disclosure", "Admitted, Form 24 &para;20", 1),
 ("Mon 13 May", "Called the Switchboard 15 minutes before shift to advise he was unwell "
  "(the Line Manager's later account)", "FRMS p.36", 1),
 ("Mon 13 May, 8:21 am", "Payroll to the Appellant: &ldquo;I cannot see that any of the issues below "
  "have been corrected. Please speak to your Line Manager&hellip;&rdquo;", "Payroll disclosure p.5", 2),
 ("Tue 14 May, 12:08 pm", "The Line Manager to the Appellant, &ldquo;Sick leave 14.05.24&rdquo;",
  "FRMS", 1),
 ("Wed 15 May, 11:47 am", "Ms S Marriott to Logan Switch, &ldquo;Respiratory Nurse Educators&rdquo;",
  "Respondent's disclosure", 0),
 ("Wed 15 May, 1:07 pm", "<b>The Line Manager to the Director</b>, &ldquo;Cory Shepherd - emergent "
  "leave 15.05.24&rdquo;", "FRMS p.39", 1),
 ("Wed 15 May, 1:15 pm", "The Appellant to the Line Manager and Logan Switch, copied to the "
  "department, the Director and LBH_HR, &ldquo;Office Hours and Departmental Directives&rdquo;",
  "11 Jun disclosure", 1),
 ("Wed 15 May, 3:41 pm", "<b>LBH_HR to Mr B Punch, Ms E McGinley and Ms A McNamee</b>: &ldquo;Please "
  "see email from Corey Shephard to ESU and CO Complaints regarding Chloe Taylor&rdquo;",
  "11 Jun disclosure", 3),
 ("Wed 15 May, 6:23 pm", "The Director to the Appellant, copied to the Line Manager, directing that "
  "the email be retracted, with recall instructions", "FRMS p.37 &middot; admitted, Form 24 &para;21", 1),
 ("Wed 15 May, 7:09 pm", "The Appellant to the Director, attaching Ms Stibbard's business-hours email",
  "FRMS p.17", 1),
 ("Thu 16 May, 11:43 am", "Ms E McGinley to the Director and Ms T Smith, copied to Mr Punch, "
  "Mr Pritchard and Ms McNamee, attaching the complaint form", "11 Jun disclosure p.7", 1),
 ("Fri 17 May, 9:30 am", "The Line Manager to Logan Switch and Switchboard staff, "
  "&ldquo;Switchboard Manager - On call and Hours.&rdquo;", "Respondent's disclosure", 1),
 ("Fri 17 May, 1:20 pm", "<b>The Line Manager to Ms A McNamee, &ldquo;as requested&rdquo;</b> - her "
  "account of 13, 14 and 15 May, and of what she says staff had told her about the Appellant",
  "FRMS pp.36-37", 3),
 ("Wed 15 May", "Attendance Variation and Allowance Claim 16328886 submitted by the Line Manager. "
  "Completed 16 May 2024", "myHR, MSH Item 11", 2),
 ("Mon 20 May, 11:03 am", "Ms S Marriott to Logan Switch, &ldquo;FW: Respiratory Nurse Educators&rdquo;",
  "Respondent's disclosure", 0),
 ("Mon 20 May, 2:05 pm", "The Appellant to the Line Manager, providing his recommendations on the "
  "respiratory nurse educators", "Respondent's disclosure", 0),
 ("Mon 20 May, 4:07 pm", "The Director to LBH_HR, &ldquo;FW: Roster Concerns&rdquo;",
  "Respondent's disclosure", 1),
 ("Mon 20 May, 4:30 pm", "The Line Manager's reply to the Appellant on the respiratory nurse "
  "educators", "Respondent's disclosure", 0),
 ("Tue 21 May, 12:33 pm", "<b>The Line Manager to the Appellant: &ldquo;I am still I am waiting "
  "payroll confirmation&hellip; as soon as I do get that confirmation, I will submit an AVAC for "
  "next pay run&rdquo;</b>", "FRMS p.46 &middot; Form 24 &para;46", 3),
 ("Tue 21 May, 2:53 pm", "The Director to the Appellant, &ldquo;RE: Office Hours and Departmental "
  "Directives&rdquo;", "FRMS p.21", 1),
 ("Tue 28 May, 8:01 and 8:02 am", "The AVAC and the Validation of Claims form scanned one minute "
  "apart on the employer's device", "Scanner titles, employer's own files", 2),
 ("Tue 28 May, 8:36 am", "The Line Manager to the Appellant, copied to the Director: &ldquo;please "
  "sign and return&hellip; so I can escalate for delegate approval&rdquo;", "FRMS p.46", 2),
 ("Tue 28 May", "<b>Attendance Variation and Allowance Claim 16450619 submitted.</b> Effective "
  "30 March 2024. Recorded Part Completed, 30 May 2024",
  "myHR &middot; admitted, Response &para;38", 3),
]

st = [P("The dated sequence of 3 to 28 May 2024", H1),
      P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; internal working "
        "document, 22 August 2026 &middot; not for service, and not for a filing in this form", SUB)]
st.append(P("Every entry is taken from a document in the Respondent's own disclosure at the source "
            "stated, or is an admitted fact. The pay thread and the complaint track ran in the same "
            "twenty-five days. That is a matter of dates and nothing more is asserted here.", B))

rows = [[P("When", CH), P("What", CH), P("Source", CH)]]
for w, what, src, wt in SEQ:
    rows.append([P(f"<b>{w}</b>", C), P(what, C), P(src, C)])
t = Table(rows, colWidths=[32*mm, 108*mm, 38*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),3.5),('RIGHTPADDING',(0,0),(-1,-1),3.5),
       ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
for i,(w,what,src,wt) in enumerate(SEQ, start=1):
    if wt == 3: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif wt == 2: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f2f2f2')))
t.setStyle(TableStyle(sty))
st += [t, Spacer(1,3*mm)]

st.append(P("What the dates show", H2))
st.append(P("The answer to the question is yes. The Attendance Variation and Allowance Claim of "
            "<b>28 May 2024</b> came after the complaint to the Ethical Standards Unit of 13 May, "
            "after Human Resources circulated notice of that complaint on 15 May at 3:41 pm, after "
            "the direction to retract the email of 15 May at 6:23 pm, after the Line Manager's "
            "account to Human Resources of 17 May at 1:20 pm, and after the respiratory nurse "
            "educators exchange of 15 and 20 May. The payroll request it answered had been "
            "outstanding since 3 May.", B))
st.append(P("Two things sit inside that period and are worth holding on to, because neither requires "
            "anything to be alleged. <b>First</b>, an Attendance Variation and Allowance Claim was "
            "submitted on 15 May and completed on 16 May, six days before the Appellant was told that "
            "payroll confirmation was awaited before one could be submitted. <b>Second</b>, the "
            "request of 3 May was made to the Line Manager on a thread on which the Appellant was "
            "copied, so he could see, throughout, what had been asked of her.", B))

st.append(P("&#9888; Why this must not become a reprisal argument on the pay", H2))
st.append(P("The temptation is to say the pay was delayed <i>because</i> of the complaint. Do not. "
            "The cost is out of all proportion to the gain.", W))
st.append(P("<b>Motive is not an element.</b> Section 32(5)(a) asks whether the management action was "
            "reasonable and taken in a reasonable way, judged on what was done. The dated sequence "
            "produces whatever inference it produces on its own, and it cannot be answered. An "
            "assertion about why can be.", B))
st.append(P("<b>It opens section 32(5)(b).</b> Injuries connected with the worker's expectation or "
            "perception of management action are not compensable. The Respondent has not pleaded that "
            "limb. Language of punishment or retaliation about the pay would hand it over from the "
            "Appellant's own side.", B))
st.append(P("<b>It raises his own standard of persuasion.</b> An allegation of that seriousness "
            "attracts <i>Briginshaw</i>. The delay is admitted; the reason for it is not, and does not "
            "need to be.", B))
st.append(P("<b>And it brings in the email of 17 May 2024.</b> That document is the Line Manager's "
            "account to Human Resources of the three days of 13 to 15 May and of what she says other "
            "staff reported to her about the Appellant. It is adverse. It is presently a document "
            "nobody has any reason to open. Building an argument that depends on the events of that "
            "week is what gives them the reason.", W))
st.append(P("Reprisal is already pleaded, and confined, at Stressor 1(f) - the direction to retract, "
            "within 48 hours of the disclosure. That is where it belongs and it should stay there. "
            "Stressor 2 runs on the routing and the twenty-five days, which are admitted and need "
            "nothing else.", B))

st.append(P("How to use the sequence properly", H2))
st.append(P("State the dates. Put the 3 May request, the 13 May confirmation that nothing had been "
            "corrected, the 15 May claim completed in a day, the 21 May reply and the 28 May "
            "submission in one list, and stop. If the Commission draws something from what else "
            "appears on those dates, it will do so without being asked, and the Appellant will not "
            "have carried the burden of asking.", B))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - May 2024 sequence - internal working document, not for service")
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
