import pikepdf, io
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, Image, PageBreak
from PIL import Image as PILImage

D='../documents'; C=D+'/correspondence-2026'
ITEMS=[  # (tab, date, from -> to, description, path or None for the SMS image)
 (1,'2 – 3 Jul 2026','Taylor ↔ Shepherd','ECC / leave type — the origin: exclusion pending ECC; sick-leave default; leave type confirmed as ANNUAL at 3:18 pm 3 Jul (4 messages)',C+'/2026-07-03_1518_Cory_to_Taylor_ECC_LeaveType_reply.pdf'),
 (2,'7 – 13 Jul 2026','Forrest / Harrison ↔ Shepherd','ECC further information — paid-time request 10 Jul; QSuper deflection 13 Jul 3:53 pm; "I ask again" + interim duties offer 13 Jul 4:39 pm (4 messages)',C+'/2026-07_Cory_to_InjuryMgmt_ECC_further_information_FULL_THREAD_12pp.pdf'),
 (3,'15 Jul 2026','Harrison → Shepherd (and Zappia)','Pay refused — "sits with your QSuper Claim Manager"; interim duties refused "in any capacity"; the discretion paragraph',D+'/2026-07-15_Harrison_reply_pay_refused_discretion.pdf'),
 (4,'22 Jul 2026','Shepherd → Payroll','Payroll Enquiry 4438861 — "Pending Investigation"',D+'/2026-07-22_Payroll_Enquiry_4438861_PendingInvestigation.pdf'),
 (5,'28 Jul 2026, 5:39 pm','Shepherd → Injury Management (cc union, fund)','Incorrect application of EB12, Award and QH policies — contests the sick-leave-no-pay coding and the QSuper basis',C+'/2026-07-28_1739_Cory_to_HR_incorrect_application_EB12_Award_policies.pdf'),
 (6,'29 Jul 2026, 4:10 pm','MSH → Shepherd','Reply to the 28 July letter',C+'/2026-07-29_1610_MSH_reply_to_28July_letter.pdf'),
 (7,'30 Jul 2026, 11:25 am','Shepherd → MSH','Reply — roster, pay and leave "remain live in parallel" (with attachments)',C+'/2026-07-30_1125_Cory_reply_to_MSH_29July.pdf'),
 (8,'30 Jul 2026, 2:33 pm','MSH → Shepherd','Holding reply — delegate approval (with attachments)',C+'/2026-07-30_1433_MSH_holding_reply_delegate_approval.pdf'),
 (9,'5 Aug 2026, 7:30 am','Shepherd → Taylor / IM / HR','Stage 1 reply — cover email (pay restoration and leave re-credit sought)',C+'/2026-08-05_0730_SENT_Stage1_reply_cover_email.pdf'),
 (10,'12 Aug 2026','Payslip','Pay advice, fortnight 20 Jul – 2 Aug 2026: "NP Sick Leave" 76.00 hours, gross $0.00',D+'/2026-08-12_Payslip_ZERO_NPSickLeave_76hrs.pdf'),
 (11,'13 Aug 2026, 3:48 pm','Harrison → Shepherd','Reply — consent and EAF',D+'/2026-08-13_1548_Harrison_reply_consent_and_EAF.pdf'),
 (12,'18 – 28 Aug 2026','Roberts ↔ Shepherd (cc Petering, McQuillan)','"Follow up on Enquiries" — meeting arranged; 24 Aug: leave and AVAC requested, authority provided; 28 Aug: Stage 2 referral withdrawn, AVAC update sought, psychiatrist unanswered',C+'/2026-08-18_to_28_Roberts_FollowUpOnEnquiries_FULL_THREAD.pdf'),
 (13,'Aug 2026','SMS — Roberts ↔ Shepherd','Text thread: the move, "hand my keys over", partner attended consults, prior work history',None),
 (14,'25 Aug 2026, 3:08 pm','Roberts → Shepherd, McQuillan, Petering','Teams invitation to continue the 21 Aug meeting',C+'/2026-08-25_1508_Roberts_Teams_invite.pdf'),
 (15,'31 Aug 2026','Shepherd ↔ Taylor (cc Roberts, Petering)','10:59 application (LSL from 13 Jul, A/L on exhaustion, AVAC today, under protest, re-credit) → 3:34 pm Taylor: one fortnight, PRN 249 863 66, "0.5 FTE", LSL blocked → 4:06 pm four-point correction',C+'/2026-08-31_FULL_THREAD_v2_Taylor_LSL_AVAC_incl_1606_correction.pdf'),
]
SMS=C+'/2026-08_SMS_Cory_Roberts_thread_screenshot.jpg'

H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3)
SM=PS('sm',fontName='Helvetica',fontSize=8.2,leading=10.2)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.2)
B=PS('b',fontName='Helvetica',fontSize=9,leading=11.5)

def front():
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=15*mm,bottomMargin=14*mm,title='',author='')
    s=[P('CORRESPONDENCE BUNDLE — PAY AND THE EXCLUSION',H1),
       P('Cory Shepherd (388372), AO3, Switchboard Services, Logan Hospital · original emails, payslip and messages, 2 July – 31 August 2026, in date order · compiled 2 September 2026',SM),
       Spacer(1,5),
       P('Each tab is the original document as sent or received. Nothing has been retyped. The two-page brief "Pay and the exclusion — the record" summarises this bundle and cross-refers to it.',B),
       Spacer(1,6)]
    rows=[[P('<b>Tab</b>',SMB),P('<b>Date</b>',SMB),P('<b>From / to</b>',SMB),P('<b>What it is</b>',SMB),P('<b>Pages</b>',SMB)]]
    return doc,s,rows,buf

# page counts
counts=[]
for it in ITEMS:
    counts.append(1 if it[4] is None else len(pikepdf.open(it[4]).pages))
doc,s,rows,buf=front()
start=2
for it,n in zip(ITEMS,counts):
    rows.append([P(str(it[0]),SM),P(it[1],SM),P(it[2],SM),P(it[3],SM),P(f'{start}–{start+n-1}' if n>1 else str(start),SM)])
    start+=n
t=Table(rows,colWidths=[9*mm,27*mm,38*mm,88*mm,16*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),
 ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t)
s.append(Spacer(1,6))
s.append(P(f'Total: {sum(counts)+1} pages including this index. Prepared for Together Queensland. Employment matter only.',SM))
doc.build(s)
buf.seek(0); index_pdf=pikepdf.open(buf)
if len(index_pdf.pages)!=1:
    raise SystemExit(f'index ran to {len(index_pdf.pages)} pages — page numbers in the table assume 1')

# SMS image page
ib=io.BytesIO()
im=PILImage.open(SMS); w,h=im.size
idoc=SimpleDocTemplate(ib,pagesize=A4,leftMargin=14*mm,rightMargin=14*mm,topMargin=12*mm,bottomMargin=12*mm,title='',author='')
maxw,maxh=A4[0]-28*mm,A4[1]-40*mm
sc=min(maxw/w,maxh/h)
idoc.build([P('TAB 13 — SMS thread, Roberts ↔ Shepherd, August 2026 (screenshot as captured)',SMB),Spacer(1,3),Image(SMS,width=w*sc,height=h*sc)])
ib.seek(0); sms_pdf=pikepdf.open(ib)

out=pikepdf.new()
out.pages.extend(index_pdf.pages)
for it in ITEMS:
    src=sms_pdf if it[4] is None else pikepdf.open(it[4])
    out.pages.extend(src.pages)
with out.open_metadata() as m:
    for k in list(m): del m[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/CORRESPONDENCE_BUNDLE_pay_and_exclusion_2JUL-31AUG2026.pdf')
print('pages:',len(out.pages))
