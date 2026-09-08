import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle

D='../documents/'
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=4)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.6,leading=14,spaceBefore=11,spaceAfter=4)
B=PS('b',fontName='Helvetica',fontSize=9.4,leading=12.8,spaceAfter=7)
BL=PS('bl',fontName='Helvetica',fontSize=9.4,leading=12.8,spaceAfter=6,leftIndent=9*mm,firstLineIndent=-5*mm)
SM=PS('sm',fontName='Helvetica',fontSize=8.3,leading=10.5)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.3,leading=10.5)

TABS=[
 (D+'correspondence-2026/2026-07-03_1518_Cory_to_Taylor_ECC_LeaveType_reply.pdf','2–3 July 2026','The leave type is raised and answered — sick leave by default; annual leave confirmed at 3:18 pm on 3 July'),
 (D+'2026-07-20_myHR_IncomeProtection_NoPay_requested_by_Taylor.pdf','20 July 2026','myHR record — leave type "Income Protection – No Pay", requested on the employee\'s behalf'),
 (D+'correspondence-2026/2026-08-04_1335_Taylor_Stage1_ack_24h_not_achieved_and_leave_request.pdf','4 August 2026, 1:35 pm','Stage 1 acknowledgement — the 24-hour timeframe conceded; leave to be processed on the employee\'s behalf; recreation balance 41.21 hours; the undertaking to apply it'),
 (D+'correspondence-2026/2026-08-05_0730_SENT_Stage1_reply_cover_email.pdf','5 August 2026, 7:30 am','The reply — recreation leave not consented to; special leave on full pay requested instead'),
 (D+'2026-08-12_Payslip_ZERO_NPSickLeave_76hrs.pdf','12 August 2026','Pay advice for the fortnight 20 July – 2 August 2026 — "NP Sick Leave" 76.00 hours, gross $0.00'),
]
SEQ=[('2 Jul, 2:38 pm','Ms Taylor: unless advised otherwise, shifts not worked will be processed as sick leave.'),
 ('3 Jul, 2:49 pm','Ms Taylor: "As you have not confirmed leave type … I will continue to process as Sick leave / Sick leave no pay".'),
 ('3 Jul, 3:18 pm','Mr Shepherd, twenty-nine minutes later: "could you please process the balance as <b>annual leave</b> rather than sick leave without pay".'),
 ('20 Jul','myHR records leave of the type <b>"Income Protection – No Pay"</b> requested on Mr Shepherd\'s behalf.'),
 ('4 Aug, 1:35 pm','Ms Taylor, Stage 1 acknowledgement: the EB12 cl 1.11.2(a) 24-hour timeframe "will not be achieved"; <b>"I am required to process leave on your behalf"</b> for 20 July – 2 August; recreation leave balance <b>41.21 hours</b>; the PP04 cut-off is today; and absent a response, <b>"I will apply your remaining recreation leave balance to ensure you receive the available paid leave entitlement for this period."</b>'),
 ('5 Aug, 7:30 am','Mr Shepherd: "I do not consent to my recreation leave being applied, and I have asked that the period be coded as <b>special leave on full pay</b> instead."'),
 ('12 Aug','Pay advice for the fortnight 20 July – 2 August 2026: <b>"NP Sick Leave", 76.00 hours, gross $0.00.</b>')]
WHY=[('(a) The leave type was chosen. It was not a default and it was not an omission.','Each "Sick Leave – No Pay" entry is a positive act — a leave type selected from those available in myHR and submitted on the employee\'s behalf. The alternatives were available, and they were known to the person making the entry: on 4 August 2026 the recreation leave balance was identified as 41.21 hours and an undertaking was given to apply it. Of the leave types in play, three produce a payment and one does not. The one that does not was selected — and selected again on each subsequent day, after the objection of 3 July and after every objection since.'),
 ('(b) Three leave types were in play, and the one applied is the only one nobody requested.','One was proposed by the employer — recreation leave. One was requested by the employee — annual leave on 3 July, and special leave on full pay on 5 August. A third was applied: sick leave without pay. It is the only one of the three that produces no payment.'),
 ('(c) The employee did not decline to be paid.','The email of 5 August states two things: that recreation leave is not consented to, and that the period is to be coded as <b>special leave on full pay instead</b>. Special leave on full pay under Directive 12/24 is not debited from any leave account. What was declined was the funding of an employer-directed absence out of the employee\'s own accrued credits. What was requested was payment, from the leave type that exists for that circumstance. The application for special leave made on 28 July and 5 August has never been determined — neither granted nor refused.'),
 ('(d) The employer\'s own policy required a written request for the leave type entered.','HR Policy C13, Payment of salaries and wages (QH-POL-188), section 6, permits a line manager to submit leave on an employee\'s behalf only where "the employee\'s request for leave is documented in writing" and any supporting documents "are sourced and retained". The written requests on the record are annual leave (3 July) and special leave on full pay (5 August). There is no written request for sick leave without pay. On 31 August Mr Shepherd confirmed in terms that he was not applying for personal leave.'),
 ('(e) The coding is inconsistent with the employer\'s own medical record.','The Employee Capability Checklist of 3 July 2026, completed on Metro South Health\'s own form, certifies fitness with restrictions and records that usual switchboard operational duties remain suitable. Sick leave records an employee as unfit for work.'),
 ('(f) On the employer\'s own stated default, the fortnight would have been paid in part.','41.21 hours of recreation leave at $44.46 per hour is <b>$1,832.20 gross</b>. The pay advice for that fortnight records nil.'),
 ('(g) The consequence is not confined to that fortnight.','Periods recorded as leave without pay are excluded from continuous service. The long service leave eligibility date of 4 September 2026, given by Payroll on 3 September 2026, falls 163 days after the date on which seven years\' continuous service fell due on the service dates recorded in the agreement under which Mr Shepherd was reinstated. The coding has deferred the entitlement now relied on to refuse the leave.')]
ASKS=['A copy of the written request, and the supporting documents, on which each "Sick Leave – No Pay" entry from 3 July 2026 was made, as required by section 6 of the policy.',
 'That the coding be corrected from the first date it was applied, and before long service leave eligibility is recalculated in the audit.',
 'That an attendance variation form be submitted for each affected fortnight with a leave type that pays, and that the ad hoc payment pending under enquiry 4471091 be processed against it.',
 'An explanation of the recreation leave balance, which was recorded at 41.21 hours on 4 August 2026 and 51.31 hours on 2 September 2026 — an increase of approximately ten hours across two fortnights, at the ordinary full-time accrual rate, which is inconsistent with a period recorded as leave without pay.',
 'Determination of the application for special leave on full pay made on 28 July and 5 August 2026, which has been neither granted nor refused.']

srcs=[pikepdf.open(p) for p,_,_ in TABS]
counts=[len(d.pages) for d in srcs]

def tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))
    return t

def build_front(start):
    s=[P('THE LEAVE TYPE FOR THE FORTNIGHT 20 JULY – 2 AUGUST 2026',H1),
       P('What was requested, what was undertaken, and what was applied · Cory Shepherd, employee number 388372 · AO3, Switchboard Services, Logan Hospital · 3 September 2026',SM),Spacer(1,8),
       P('1. THE SEQUENCE',H2)]
    r=[[P('<b>Date</b>',SMB),P('<b>What was said or done</b>',SMB)]]+[[P(d,SM),P(w,SM)] for d,w in SEQ]
    s.append(tbl(r,[26*mm,144*mm]))
    s.append(P('2. THE POSITION AS IT STANDS, AND WHY IT IS NOT CORRECT',H2))
    for h,body in WHY: s.append(P(f'<b>{h}</b> {body}',BL))
    s.append(P('3. WHAT IS ASKED',H2))
    for i,a in enumerate(ASKS,1): s.append(P(f'<b>{i}.</b>&nbsp;&nbsp;{a}',BL))
    s.append(Spacer(1,4))
    s.append(P('Everything applied for remains on the basis set out at paragraph 4 of the application of 31 August 2026 — under protest and subject to re-credit. Mr Shepherd remains certified fit with restrictions and available to work.',B))
    s.append(P('4. THE DOCUMENTS',H2))
    r=[[P('<b>Tab</b>',SMB),P('<b>Date</b>',SMB),P('<b>What it is</b>',SMB),P('<b>Pages</b>',SMB)]]
    pg=start
    for i,((_,date,what),n) in enumerate(zip(TABS,counts),1):
        r.append([P(str(i),SM),P(date,SM),P(what,SM),P(f'{pg}–{pg+n-1}' if n>1 else str(pg),SM)]); pg+=n
    s.append(tbl(r,[9*mm,30*mm,115*mm,16*mm]))
    s.append(Spacer(1,5))
    s.append(P('Each tab is the original document as sent or received. Nothing has been retyped.',SM))
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=15*mm,title='',author='')
    doc.build(s); buf.seek(0); return pikepdf.open(buf)

fr=build_front(1)
fr=build_front(len(fr.pages)+1)
print('front pages',len(fr.pages))
out=pikepdf.new(); out.pages.extend(fr.pages)
for d in srcs: out.pages.extend(d.pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
if '/Names' in r and '/EmbeddedFiles' in r.Names: del r.Names['/EmbeddedFiles']
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/LEAVE_TYPE_20JUL-2AUG_what_was_asked_and_what_was_applied.pdf',fix_metadata_version=False)
print('TOTAL',len(out.pages))
