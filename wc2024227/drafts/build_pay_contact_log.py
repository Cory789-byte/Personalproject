#!/usr/bin/env python3
"""WC/2024/227 - log of every recorded contact about pay, February to September 2024.

INTERNAL WORKING DOCUMENT. Not for service.
Source key:  [E] the email itself, held   ·  [RD] recited in Review Decision 69983
             [HR] myHR submissions report, MSH Item 11  ·  [A] admitted, Form 24 response
             [S] scanner metadata, employer's own device  ·  [L] Respondent's list of documents
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/PAY_CONTACT_LOG_2024.pdf"
PW, PH = landscape(A4)
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.4, leading=13,
                     spaceBefore=8, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.4, leading=11,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=8.8, leading=12, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=7.9, leading=10.4)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=C): return Paragraph(t, s)

# n, when, from, to, what, source, dir  (dir: O=out(Cory) I=in P=payroll->mgr M=myHR action)
LOG = [
 (1,"6 Feb 2024","Ms C Taylor","myHR","AVAC 15325947 submitted, effective 22 Jan 2024. Completed 8 Feb","[HR]","M"),
 (2,"<b>9 Feb 2024</b>","&mdash;","&mdash;","<b>The 7-hour shift that causes the first error.</b> Fortnight commencing 5 Feb topped up 0.95 from the RDO balance. AVAC PRN 15397775","[E] 3 May email","M"),
 (3,"28 Feb 2024","&mdash;","&mdash;","The same error repeats, fortnight commencing 19 Feb. AVAC PRN 15605601","[E] 3 May email","M"),
 (4,"27 Mar 2024","Ms C Taylor","myHR","AVAC 15849573 submitted, effective 18 Mar. Completed 1 Apr","[HR]","M"),
 (5,"<b>8 Apr 2024</b>","<b>Appellant</b>","Ms C Taylor","<b>FIRST RECORDED APPROACH.</b> Requests formal review of pay for 8&ndash;31 March: unpaid Saturday public holiday, and penalty rates for the Monday shift after a Sunday. Cites the Award, part 5 s 15 &mdash; minimum 10-hour break","[RD] p 21 &middot; [L] item 23","O"),
 (6,"9 Apr 2024","Ms C Taylor","Appellant","AVAC submitted for the 30 March public holiday. <b>For the other dates, directs him to submit an enquiry through MyHR payroll enquiries</b>, the claims being over 3 months old, and says that <b>if payroll decided he was entitled she would happily submit a validation of claims form</b>. Escalates the fatigue-leave query to HR. Asks him to raise concerns as soon as they arise","[RD] p 21","I"),
 (7,"9 Apr 2024","Ms C Taylor","myHR","AVAC 15969838 submitted, effective 30 Mar. Completed 11 Apr","[HR]","M"),
 (8,"<b>24 Apr 2024</b>","<b>Appellant</b>","Ms C Taylor","Has been in touch with payroll, <b>who advised him to notify Ms Taylor that the payments must be processed as overtime in the fortnightly pay cycle</b>. Asks her to act and provide a PRN. Records <b>&ldquo;more than 2 weeks without any response or overtime payment&rdquo;</b>","[RD] p 21","O"),
 (9,"1 May 2024","Ms C Taylor","Appellant","Fatigue payment for 18 March refused on the 2020 agreement. As to top-up and reduction of hours, <b>&ldquo;an investigation is currently underway by payroll&rdquo;</b>; the system generates adjustments automatically and <b>she is &ldquo;unable to view them directly&rdquo;</b>. Payroll also <b>&ldquo;still reviewing&rdquo;</b> the public holidays and overtime","[RD] pp 21&ndash;22","I"),
 (10,"<b>3 May 2024, 9:39 am</b>","<b>Payroll &mdash; Ms E Grant</b>","<b>Ms C Taylor</b><br/><b>cc Appellant</b>","<b>THE INSTRUCTION.</b> Sets out four affected fortnights in detail. <b>&ldquo;Please submit an AVAC to correct these shifts for each fortnight so Cory is paid corrected and his RDO balance will then be amended.&rdquo;</b> Names AVAC PRN 15397775 and 15605601","[E] &middot; [A] &para;40 &middot; [L] item 13","P"),
 (11,"<b>10 May 2024, 2:21 pm</b>","<b>Appellant</b>","Payroll; Ms E Grant","<b>&ldquo;I was wondering if you have received any response or updates from her regarding these issues. In case Chloe has already responded or managed to process the missing payments, I would appreciate it if you could keep me informed.&rdquo;</b>","[E] &middot; [L] item 15","O"),
 (12,"<b>13 May 2024, 8:21 am</b>","<b>Payroll &mdash; Ms E Grant</b>","<b>Appellant</b>","<b>&ldquo;I cannot see that any of the issues below have been corrected. Please speak to your Line Manager to have them corrected with an AVAC submitted through My HR as this will also be affecting your RDO balances as well as your pay.&rdquo;</b>","[E] &middot; [L] item 15","I"),
 (13,"<b>15 May 2024, 1:15 pm</b>","Appellant","Ms C Taylor, Logan Switch, department, Director, LBH_HR","&ldquo;Office Hours and Departmental Directives&rdquo; &mdash; raises, among other matters, <b>&ldquo;addressing payroll concerns and ensuring managerial responsiveness&rdquo;</b>","[E] 11 Jun disclosure","O"),
 (14,"<b>15 May 2024</b>","<b>Ms C Taylor</b>","<b>myHR</b>","&#9733;&#9733; <b>AVAC 16328886 SUBMITTED. COMPLETED 16 MAY 2024 &mdash; ONE DAY.</b> Effective 7 May","[HR]","M"),
 (15,"<b>21 May 2024, 12:33 pm</b>","<b>Ms C Taylor</b>","<b>Appellant</b>","Same thread, <i>RE: Corey Shepherd 388372 Pay issues</i>: <b>&ldquo;Just letting you know that I am still I am waiting payroll confirmation about a few of these payroll issues and as soon as I do get that confirmation, I will submit an AVAC for next pay run. I will let you know PRN once it has been submitted.&rdquo;</b>","[E] &middot; [A] &para;46","I"),
 (16,"28 May 2024, 8:01 / 8:02 am","&mdash;","&mdash;","The AVAC and the Validation of Claims form scanned <b>one minute apart</b> on the employer's own device","[S]","M"),
 (17,"<b>28 May 2024, 8:36 am</b>","<b>Ms C Taylor</b>","<b>Appellant</b><br/>cc Ms T Reese","<i>&ldquo;Validation of Claims older than 3 months - Please sign&rdquo;</i>, Importance High: <b>&ldquo;please sign and return&hellip; so I can escalate for delegate approval. Once this is processed you will be paid correctly and RDO balance will be amended.&rdquo;</b>","[E]","I"),
 (18,"<b>28 May 2024</b>","<b>Ms C Taylor</b>","<b>myHR</b>","&#9733;&#9733;&#9733; <b>AVAC 16450619 SUBMITTED. Effective 30 Mar 2024. Recorded PART COMPLETED, 30 May 2024</b> &mdash; the only one of five in the period not completed","[HR] &middot; [A] &para;38","M"),
 (19,"<b>3 Jun 2024</b>","&mdash;","&mdash;","<b>LAST DAY OF ATTENDANCE AT A ROSTERED SHIFT</b>","MSH confirmation letter, 9 Oct 2024","M"),
 (20,"<b>18 Jun 2024</b>","&mdash;","&mdash;","<b>DATE OF INJURY</b>","Amended SOFC","M"),
 (21,"12 Jul 2024","Appellant","WorkCover","Overview of events listing pay issues still outstanding: recognised-education payment, pandemic-leave income, a cancelled shift, fatigue pay denied on the 2020 agreement","[RD] p 22 &middot; [L] item 12","O"),
 (22,"18 Jul 2024","Appellant","WorkCover","<b>&ldquo;Ms Taylor had been withholding payments for overtime you completed.&rdquo;</b> Recounts being directed to payroll, payroll including both of them, and being told twice she was waiting on payroll","[RD] pp 22&ndash;23 &middot; [L] items 13, 15","O"),
 (23,"9 Aug 2024","Appellant","Review Unit","Fatigue pay for the 7-hour break; and that the dates requiring adjustment against the dates actioned are <b>&ldquo;concerning&rdquo;</b>","[RD] p 15","O"),
 (24,"26 Aug 2024","Appellant","WorkCover","Attaches the chain <i>&ldquo;Request for review and adjustment of payment &mdash; 08/04/2024 to 23/08/2024&rdquo;</i>","[L] item 23","O"),
 (25,"4 Sep 2024","Ms C Taylor","Mr M Pritchard","Forwards the validation of claims older than 3 months into the employer's WorkCover response","[E] &middot; [L]","M"),
 (26,"6 Sep 2024","Employer","WorkCover","<b>&ldquo;no evidence to suggest pay was withheld&hellip; corrective action was taken by Ms Taylor as per internal processes&rdquo;</b>","[RD] p 22 &middot; [L] item 31","I"),
]

st = [P("Log of every recorded contact about pay &mdash; February to September 2024", H1),
      P("WC/2024/227 &middot; 23 August 2026 &middot; internal working document, not for service &middot; "
        "sources: [E] the email itself, held &middot; [RD] recited in Review Decision 69983 &middot; "
        "[HR] myHR submissions report (MSH Item 11) &middot; [A] admitted in the Form 24 response "
        "&middot; [S] scanner metadata &middot; [L] Respondent's list of documents", SUB)]

rows = [[P("#", CH), P("When", CH), P("From", CH), P("To", CH), P("What", CH), P("Source", CH)]]
for n, when, frm, to, what, src, d in LOG:
    rows.append([P(str(n)), P(when), P(frm), P(to), P(what), P(src)])
t = Table(rows, colWidths=[7*mm, 26*mm, 26*mm, 26*mm, 145*mm, 32*mm], repeatRows=1)
sty=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
     ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
     ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
     ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]
for i,(n,when,frm,to,what,src,d) in enumerate(LOG, start=1):
    if n in (10,12,14,15,18,19,20): sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif d=="O": sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f1f5f9')))
t.setStyle(TableStyle(sty)); st.append(t)

st.append(P("The counts", H2))
out = sum(1 for x in LOG if x[6]=="O"); inn = sum(1 for x in LOG if x[6]=="I")
rows=[[P("", CH), P("Count", CH), P("", CH)]]
for a,b,c in [
 ("<b>Approaches made BY the Appellant</b> about pay", str(out),
  "8 Apr &middot; 24 Apr &middot; 10 May &middot; 15 May &middot; 12 Jul &middot; 18 Jul &middot; 9 Aug &middot; 26 Aug"),
 ("<b>Responses received</b> from the Line Manager, payroll or the employer", str(inn),
  "9 Apr &middot; 1 May &middot; 13 May &middot; 21 May &middot; 28 May &middot; 6 Sep"),
 ("Payroll to the Line Manager, copied to the Appellant", "1", "<b>3 May 2024 &mdash; the instruction</b>"),
 ("<b>AVACs submitted in the period &mdash; every one by the Line Manager</b>", "5",
  "6 Feb &middot; 27 Mar &middot; 9 Apr &middot; <b>15 May (completed in 1 day)</b> &middot; <b>28 May (Part Completed)</b>"),
 ("<b>AVACs initiated by the Appellant</b>", "<b>0</b>", "He initiated one leave request in the period and nothing else"),
]:
    rows.append([P(a, C), P(f"<b>{b}</b>", CH), P(c, C)])
t=Table(rows, colWidths=[92*mm, 18*mm, 152*mm])
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
    ('BACKGROUND',(0,4),(-1,5),colors.HexColor('#f6ecec'))]))
st.append(t)
st.append(Spacer(1,2*mm))
st.append(P("<b>Eight approaches by him over four and a half months. Six responses. And the one "
            "instruction that mattered went to her, not to him, on 3 May 2024 &mdash; with him copied "
            "in, so he could see it.</b>", B))

st.append(P("&#9888; Gaps in the log", H2))
st.append(P("<b>1.</b> The emails of <b>8 and 24 April and 1 May 2024</b> are recited in the Review "
            "Decision but <b>not held</b>. They form part of the chain <i>&ldquo;Request for review "
            "and adjustment of payment &mdash; 08/04/2024 to 23/08/2024&rdquo;</i> at item 23 of the "
            "Respondent's list, and are requested in the letter of 22 August 2026.", B))
st.append(P("<b>2.</b> The chain at item 23 runs to <b>23 August 2024</b>. This log ends the "
            "correspondence at 26 August. <b>There may be further pay contacts between 9 August and "
            "23 August 2024 that are not recorded anywhere held.</b>", W))
st.append(P("<b>3.</b> Nothing records a pay contact between <b>28 May and 12 July 2024</b> &mdash; "
            "the period covering the last day worked and the injury. That silence is itself worth "
            "noting and should be checked against his own sent items.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(14*mm, 8*mm, "WC/2024/227 - pay contact log 2024 - internal, not for service")
    cv.drawRightString(PW-14*mm, 8*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=landscape(A4), leftMargin=14*mm, rightMargin=14*mm,
                      topMargin=13*mm, bottomMargin=14*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(14*mm, 14*mm, PW-28*mm, PH-27*mm)],
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
