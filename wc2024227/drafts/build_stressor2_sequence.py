#!/usr/bin/env python3
"""WC/2024/227 - Stressor 2: the sequence of instructions about the pay correction.

INTERNAL WORKING DOCUMENT. Not for service.

Every entry is taken verbatim or in close paraphrase from Review Decision 69983
of 24 October 2024, pages 21 to 23, and from the response to the notice to admit
facts. Page cites are given on each entry. Nothing here is reconstructed.

The point is not the amount. It is the routing: the person who held the power to
correct the record directed the worker to a party that had none, and then gave
that party as the reason for her own inaction.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/STRESSOR_2_SEQUENCE_OF_INSTRUCTIONS.pdf"
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.2, leading=13,
                     spaceBefore=7, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=12.4, spaceAfter=3)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.3, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

# date, direction, what the document records, source, weight
SEQ = [
 ("8 Apr 2024", "Appellant &rarr; Line Manager",
  "Requests a review of payment for 8 to 31 March 2024: the Saturday public holiday not paid, and "
  "the penalty rates for the Monday shift following a Sunday shift. Cites the Award, part 5 "
  "section 15 - a minimum ten-hour break unless there is mutual agreement on regular rosters.",
  "RD p 21", 0),
 ("9 Apr 2024", "Line Manager &rarr; Appellant",
  "An AVAC is submitted for the public holiday of 30 March 2024, to be processed in the next pay "
  "run. <b>For the other dates she asks him to submit an enquiry through MyHR payroll enquiries so "
  "they can investigate his entitlements</b>, the claims being older than three months, and notes "
  "that <b>if payroll decided he was entitled, she would happily submit a validation of claims "
  "older than 3 months form</b>. She asks him to raise concerns as soon as they arise so she could "
  "action them sooner.",
  "RD p 21", 2),
 ("24 Apr 2024", "Appellant &rarr; Line Manager",
  "He has been in touch with payroll, <b>who advised him to notify the Line Manager that payments "
  "for public holidays not worked would need to be processed as overtime in the fortnightly pay "
  "cycle</b>. He asks her to take the necessary action and provide a PRN. Records that it has been "
  "<b>more than two weeks without any response or overtime payment</b>.",
  "RD p 21", 2),
 ("1 May 2024", "Line Manager &rarr; Appellant",
  "The fatigue payment for 18 March 2024 will not be processed, on the 2020 agreement. As to the "
  "top-up and reduction of hours, <b>an investigation is currently underway by payroll</b>; the "
  "system generates the adjustments automatically and <b>she is unable to view them directly</b>. "
  "<b>Payroll is also still reviewing</b> the public holidays not required and the overtime.",
  "RD pp 21-22", 2),
 ("3 May 2024", "Payroll &rarr; Line Manager",
  "Ms E Grant sets out precisely what is wrong, fortnight by fortnight: a 7-hour shift on 9 "
  "February instead of 8, topping up from the RDO balance; the same the following fortnight; the "
  "fortnight commencing 18 March carrying too many ordinary shifts, giving a wage reduction of 7.55 "
  "hours because one shift had to be overtime; overtime again in the fortnight commencing 1 April. "
  "<b>She requests the Line Manager submit an AVAC to correct the shifts for each fortnight</b> so "
  "he is paid correctly and the RDO balance amended.",
  "RD p 22 &middot; admitted, notice to admit facts &para;40", 3),
 ("10 May 2024", "Appellant &rarr; Payroll",
  "He emails payroll raising his concern about the Line Manager and the outstanding payments.",
  "RD p 22", 0),
 ("13 May 2024", "Payroll &rarr; Appellant",
  "Payroll <b>confirm they cannot see any issues have been corrected</b> and <b>instruct him to "
  "speak with his manager</b> to correct the issues through the submission of an AVAC.",
  "RD p 14", 3),
 ("21 May 2024", "Line Manager &rarr; Appellant",
  "<b>&ldquo;I am waiting payroll confirmation&hellip; as soon as I do get that confirmation, I "
  "will submit an AVAC&rdquo;</b> - for the next pay run.",
  "RD p 14 &middot; notice to admit facts &para;46", 3),
 ("28 May 2024", "Line Manager",
  "The AVAC is submitted. Twenty-five days after the request of 3 May 2024.",
  "Admitted, response to the notice to admit facts &para;38", 2),
]

st = [P("Stressor 2 - the sequence of instructions about the pay correction", H1),
      P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; internal working "
        "document, 22 August 2026 &middot; not for service", SUB)]
st.append(P("Every entry below is recorded in Review Decision 69983 of 24 October 2024 at the pages "
            "cited, or is an admitted fact. The Respondent's own decision is the source. The question "
            "is not how much was unpaid. It is who was told to do what, and by whom.", B))

rows = [[P("Date", CH), P("Direction", CH), P("What the document records", CH), P("Source", CH)]]
for d, dirn, what, src, wt in SEQ:
    rows.append([P(f"<b>{d}</b>", C), P(dirn, C), P(what, C), P(src, C)])
t = Table(rows, colWidths=[18*mm, 30*mm, 100*mm, 30*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]
for i,(d,dirn,what,src,wt) in enumerate(SEQ, start=1):
    if wt == 3: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif wt == 2: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f4f4f4')))
t.setStyle(TableStyle(sty))
st += [t, Spacer(1,3*mm)]

st.append(P("One thread, and he is on all of it", H2))
st.append(P("The correspondence of 3 to 21 May 2024 is a single email thread with the subject "
            "<b>&ldquo;Corey Shepherd 388372 Pay issues&rdquo;</b>, disclosed by the Respondent in the "
            "Queensland Health Payroll witness conferencing and again in the FRMS material. The "
            "Appellant is a named recipient of every message in it. Read from the source.", B))
EM = [
 ("3 May 2024, 9:39/9:40 am",
  "<b>From</b> PayrollMetroSouth &nbsp;<b>To</b> Chloe Taylor &nbsp;<b>Cc</b> Cory Shepherd<br/>"
  "&ldquo;Corey has wages top up on fortnight 05.02.24 for 0.95mins as he is under his contracted "
  "hours so it is toping up the missing wages from his RDO balance. This will be due to having a "
  "7hr shift on 09.02.24 instead of an 8hr shift. <b>AVAC PRN 15397775</b>&hellip; The same has "
  "happened for the next fortnight 19.02.24 due to 28.02.24 shift <b>AVAC PRN 15605601</b>&hellip; "
  "Fortnight 18.03.24 is the opposite and has too many ordinary shifts for the fortnight resulting "
  "in wage reduction of 7.55hrs&hellip; <b>Please submit an AVAC to correct these shifts for each "
  "fortnight so Cory is paid corrected and his RDO balance will then be amended.</b>&rdquo; "
  "&mdash; Ms Elaine Grant, Client Service Officer, Metro South Payroll Team"),
 ("10 May 2024, 2:21 pm",
  "<b>From</b> Cory Shepherd &nbsp;<b>To</b> PayrollMetroSouth; Elaine Grant<br/>"
  "&ldquo;I am writing to follow up on a matter concerning Chloe&hellip; I was wondering if you have "
  "received any response or updates from her regarding these issues. In case Chloe has already "
  "responded or managed to process the missing payments, I would appreciate it if you could keep me "
  "informed.&rdquo;"),
 ("13 May 2024, 8:21 am",
  "<b>From</b> PayrollMetroSouth &nbsp;<b>To</b> Cory Shepherd<br/>"
  "&ldquo;<b>I cannot see that any of the issues below have been corrected. Please speak to your "
  "Line Manager to have them corrected with an AVAC submitted through My HR</b> as this will also be "
  "affecting your RDO balances as well as your pay.&rdquo; &mdash; Ms Elaine Grant"),
 ("21 May 2024, 12:33 pm",
  "<b>From</b> Chloe Taylor &nbsp;<b>To</b> Cory Shepherd &nbsp;<b>Subject</b> "
  "<b>RE: Corey Shepherd 388372 Pay issues</b><br/>"
  "&ldquo;Just letting you know that I am still I am waiting payroll confirmation about a few of "
  "these payroll issues and as soon as I do get that confirmation, I will submit an AVAC for next "
  "pay run. I will let you know PRN once it has been submitted.&rdquo;"),
 ("28 May 2024, 8:36 am",
  "<b>From</b> Chloe Taylor &nbsp;<b>To</b> Cory Shepherd &nbsp;<b>Cc</b> Tammy Reese &nbsp;"
  "<b>Subject</b> Validation of Claims older than 3 months - Please sign &nbsp;<i>Importance: "
  "High</i><br/>&ldquo;Please find attached Validation of claims older than 3 months, <b>please sign "
  "and return</b> to be as soon as possible <b>so I can escalate for delegate approval</b>. Once "
  "this is processed you will be paid correctly and RDO balance will be amended.&rdquo;"),
]
rows3 = [[P("When", CH), P("The message", CH)]]
for w, m in EM:
    rows3.append([P(f"<b>{w}</b>", C), P(m, C)])
t3 = Table(rows3, colWidths=[30*mm, 148*mm], repeatRows=1)
t3.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
    ('BACKGROUND',(0,1),(-1,1),colors.HexColor('#f6ecec')),
    ('BACKGROUND',(0,3),(-1,4),colors.HexColor('#f6ecec'))]))
st += [t3, Spacer(1,3*mm)]
st.append(P("<b>The reply of 21 May 2024 was sent on the thread that carried the request of 3 May "
            "2024, and the Appellant was a recipient of both.</b> The message saying that payroll "
            "confirmation was awaited sits, in the same thread, above payroll's request that an AVAC "
            "be submitted. Nothing needs to be said about that beyond the two headers. The subject "
            "line does the work: <i>RE: Corey Shepherd 388372 Pay issues</i>.", B))
st.append(P("<b>Two AVAC references were already identified on 3 May.</b> The email names "
            "<b>AVAC PRN 15397775</b> and <b>AVAC PRN 15605601</b> as the claims carrying the wrong "
            "shift data. Neither appears in the myHR submissions report below. Those are the two "
            "references sought at Item 16 of the notice of non-party disclosure.", B))
st.append(P("&#9888; The timestamp of the 3 May email reads <b>9:39 am</b> in the Payroll disclosure "
            "and <b>9:40 am</b> in the FRMS copy of the same message. Both are the Respondent's own "
            "documents. Use whichever page is being tendered and do not assert a single time.", W))

st.append(P("The shape of it", H2))
st.append(P("On <b>9 April</b> she directed him to payroll. On <b>24 April</b> payroll directed him "
            "back to her, because the action required - processing the payments through the pay cycle - "
            "was hers. On <b>1 May</b> she told him payroll was investigating and that she could not "
            "see the adjustments. On <b>3 May</b> payroll told her, in detail and fortnight by "
            "fortnight, exactly what to submit. On <b>10 May</b> he went to payroll again. On "
            "<b>13 May</b> payroll told him nothing had been corrected and that he had to go to his "
            "manager. On <b>21 May</b> she told him she was waiting on payroll - <b>eighteen days "
            "after payroll had told her what to do</b>. She submitted it on <b>28 May</b>.", B))
st.append(P("Two things follow, and neither depends on the amount.", B))
st.append(P("<b>First, the AVAC was never his to submit.</b> Payroll said so on 13 May in terms. The "
            "3 May request was addressed to her, not to him. Directing him to MyHR and to payroll "
            "directed him to a process he had no authority to complete.", B))
st.append(P("<b>Second, the reason given for the delay was overtaken by a document she held.</b> On "
            "1 May and again on 21 May the delay was attributed to payroll. From 3 May payroll had "
            "asked her to act. The chronology says this on its own; it does not need to be "
            "characterised.", B))

st.append(P("The employer's own system record", H2))
st.append(P("Metro South produced, as Item 11 of the notice of non-party disclosure, the myHR "
            "submissions report for 1 February to 31 May 2024 - the &ldquo;Search Results (7)&rdquo; "
            "screen. Read from the page (the file has no text layer). AVAC is an "
            "<i>Attendance Variation and Allowance Claim</i>.", B))
rows2 = [[P("Process", CH), P("Type", CH), P("Submitted", CH), P("Effective", CH), P("Status", CH),
          P("Processed", CH), P("Initiator", CH)]]
MYHR = [
 ("15325947","AVAC","06.02.2024","22.01.2024","Completed","08.02.2024","Donovan-Taylor, Chloe",0),
 ("15480560","Smart Leave Request","20.02.2024","20.02.2024","Completed","01.03.2024","<b>Shepherd, Cory</b>",1),
 ("15848692","Smart Leave Request","27.03.2024","25.03.2024","Completed","27.03.2024","Donovan-Taylor, Chloe",0),
 ("15849573","AVAC","27.03.2024","18.03.2024","Completed","01.04.2024","Donovan-Taylor, Chloe",0),
 ("15969838","AVAC","09.04.2024","30.03.2024","Completed","11.04.2024","Donovan-Taylor, Chloe",0),
 ("16328886","AVAC","<b>15.05.2024</b>","07.05.2024","<b>Completed</b>","<b>16.05.2024</b>","Donovan-Taylor, Chloe",2),
 ("16450619","AVAC","<b>28.05.2024</b>","30.03.2024","<b>Part Completed</b>","30.05.2024","Donovan-Taylor, Chloe",2),
]
for r in MYHR:
    rows2.append([P(r[0], C), P(r[1], C), P(r[2], C), P(r[3], C), P(r[4], C), P(r[5], C), P(r[6], C)])
t2 = Table(rows2, colWidths=[20*mm, 33*mm, 21*mm, 21*mm, 25*mm, 21*mm, 37*mm], repeatRows=1)
sty2 = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
        ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
for i, r in enumerate(MYHR, start=1):
    if r[7] == 2: sty2.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f6ecec')))
    elif r[7] == 1: sty2.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f4f4f4')))
t2.setStyle(TableStyle(sty2))
st += [t2, Spacer(1,3*mm)]

st.append(P("<b>Every AVAC in the period was initiated by the Line Manager.</b> Five of them. The only "
            "thing the Appellant initiated was a leave request. An AVAC is not a form he could submit, "
            "and the record shows he never did. That is the answer to any suggestion that the pay "
            "correction was his to pursue with payroll.", B))
st.append(P("<b>The machinery was never slow.</b> Processing ran two days, five days, two days, one "
            "day and two days. The delay of 3 to 28 May 2024 was in the submitting, not the "
            "processing.", B))
st.append(P("<b>An AVAC was submitted on 15 May 2024 and completed on 16 May 2024</b> - process "
            "16328886, one day. On <b>21 May 2024</b> the Appellant was told that an AVAC would be "
            "submitted once payroll confirmation was received. The record shows an AVAC submitted and "
            "completed in the week before that email. The two sit side by side without needing to be "
            "characterised, and the question they raise can be put in one line.", B))
st.append(P("<b>The correction AVAC is the only one not marked Completed.</b> Process 16450619, "
            "submitted 28 May 2024 with an effective date of 30 March 2024, is recorded as "
            "<b>&ldquo;Part Completed&rdquo;</b>. Every other AVAC in the period reads "
            "&ldquo;Completed&rdquo;.", B))
st.append(P("&#9888; <b>Do not assert what &ldquo;Part Completed&rdquo; means.</b> It is a myHR status "
            "and its meaning is not established anywhere on this record. It may mean the claim was "
            "processed in part only; it may be routine. It is a question, and a good one, for the "
            "employer or for Ms Grant - not a conclusion. Establish the meaning before it is relied on "
            "anywhere.", W))
st.append(P("Note also that <b>PRN 15397775 and PRN 15605601 do not appear</b> in this report at all. "
            "Those are the two references the AVAC payroll export was sought for at Item 16 of the "
            "notice of non-party disclosure.", B))

st.append(P("How this is run", H2))
st.append(P("Section 32(5)(a) asks whether management action was reasonable and <b>taken in a "
            "reasonable way</b>. The second half is the one this goes to. The Review Unit found the "
            "pay factor substantiated but reasonable; that finding was made on the same pages set out "
            "above, so the material is already before the Commission and nothing new has to be proved "
            "to open it.", B))
st.append(P("Run it as the routing, not the arrears. The quantum is not in issue, is not admitted, and "
            "the comparator figure pleaded at Stressor 2(a) should not be run at all - it depends on a "
            "document not held, and it asserts too few rostered hours while the fatigue case is that "
            "the recovery interval was too short.", B))

st.append(P("Words that must not be used", H2))
st.append(P("The Review Decision at page 23 records the Appellant's own account in the words "
            "<i>&ldquo;an act of control and abuse&rdquo;</i>, <i>&ldquo;forcing you to fight&rdquo;</i> "
            "and <i>&ldquo;falsely&rdquo;</i>. Those are already on the record and cannot be unsaid, but "
            "they are not to be repeated or adopted. They go to the worker's perception of management "
            "action, which is section 32(5)(b) territory and is not pleaded against him; and an "
            "allegation of that kind raises his own standard of persuasion. The dated sequence carries "
            "the point without any of them.", W))

st.append(P("What would strengthen it", H2))
st.append(P("<b>The four emails themselves.</b> The sequence above is recited in the Review Decision. "
            "The underlying emails of 8, 9 and 24 April, 1, 3, 10, 13 and 21 May 2024 are better "
            "evidence than a recital of them. The 3 May email of Ms Grant is the single most useful: "
            "it is the instruction, it is addressed to the Line Manager, and it is admitted. Check the "
            "correspondence packs and the Respondent's disclosure of 11 June 2026 before assuming any "
            "of them is absent.", B))
st.append(P("<b>Ms E Grant.</b> Payroll's own officer wrote the 3 May instruction and is the person "
            "who can say what was asked of the Line Manager and what would have happened had it been "
            "done. Consider her for the witness list due 4.00 pm on 9 September 2026.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - Stressor 2 sequence - internal working document, not for service")
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
