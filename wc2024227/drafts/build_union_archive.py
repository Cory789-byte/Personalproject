import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak, KeepTogether

D='../documents/'
H1=PS('h1',fontName='Helvetica-Bold',fontSize=14,leading=17,spaceAfter=4)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.8,leading=14,spaceBefore=11,spaceAfter=4)
B=PS('b',fontName='Helvetica',fontSize=9.3,leading=12.6,spaceAfter=6)
BL=PS('bl',fontName='Helvetica',fontSize=9.3,leading=12.6,spaceAfter=4,leftIndent=9*mm,firstLineIndent=-5*mm)
SM=PS('sm',fontName='Helvetica',fontSize=8.2,leading=10.4)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.4)

ARCHIVE=[
 (D+'2025-hughes-history/2025-10-04_Cory_COMPLAINT_about_Hughes_to_Roberts_cc_Moran.pdf','4 Oct 2025','Shepherd → Roberts, cc Moran','Complaint concerning the manager, copied to Together'),
 (D+'2025-11-03_Together_Moran_delegate_endorsement_Shepherd_Jeffrey_Conaghan.pdf','3 Nov 2025','Moran → Shepherd, Jeffrey, Conaghan','⭐ Endorsement as a Together WORKPLACE DELEGATE; switchboard roster feedback and the Consultation Paper'),
 (D+'2026-07-15_Together_Heath-Moran_thread_urgent-industrial-referral.pdf','14–15 Jul 2026','Moran ↔ Shepherd','⭐ "VERY SERIOUS" — urgent referral to Together\'s industrial team'),
 (D+'2026-07-17_Heath_still-reviewing_industrial-team.pdf','17 Jul 2026','Moran → Shepherd','Brief delivered in full; industrial team engaged and still reviewing'),
 (D+'correspondence-2026/2026-07-28_1739_Cory_to_HR_incorrect_application_EB12_Award_policies.pdf','28 Jul 2026, 5:39 pm','Shepherd → Injury Management, cc Moran','⭐ Incorrect application of EB12, the Award and QH policies — 8 instruments; special leave applied for (point 4); psychosocial risk assessment demanded under cl 7.2; task-by-task match of the role description demanded'),
 (D+'correspondence-2026/2026-07-29_1610_MSH_reply_to_28July_letter.pdf','29 Jul 2026, 4:10 pm','MSH → Shepherd, cc Moran','Reply: further medical information required. Special leave not addressed'),
 (D+'correspondence-2026/2026-07-30_1125_Cory_reply_to_MSH_29July.pdf','30 Jul 2026, 11:25 am','Shepherd → MSH, cc Moran','Roster, pay and leave "remain live in parallel"; ad hoc payment first requested'),
 (D+'correspondence-2026/2026-07-30_1433_MSH_holding_reply_delegate_approval.pdf','30 Jul 2026, 2:33 pm','MSH → Shepherd, cc Moran','Holding reply — RFMI with the delegate for approval. Special leave not addressed'),
 (D+'sent-2026-08-03/2026-08-03_1138_SENT_Email1_RFMI_Response_to_IM_cc_HR_Moran.pdf','3 Aug 2026, 11:38 am','Shepherd → Injury Management, cc HR, Moran','RFMI response'),
 (D+'sent-2026-08-03/2026-08-03_1138_SENT_Email2_Request_cl10.3_to_IM_and_HR_cc_Moran.pdf','3 Aug 2026, 11:38 am','Shepherd → Injury Management, HR, cc Moran','Request under cl 10.3'),
 (D+'sent-2026-08-03/2026-08-03_1138_SENT_Email3_Dispute_cl1.11_to_Taylor_IM_HR_cc_Moran.pdf','3 Aug 2026, 11:38 am','Shepherd → Taylor, IM, HR, cc Moran','Notice of dispute under cl 1.11 — Stage 1'),
 (D+'correspondence-2026/2026-08-05_0730_SENT_Stage1_reply_cover_email.pdf','5 Aug 2026, 7:30 am','Shepherd → Taylor, IM, HR','Stage 1 reply — recreation leave not consented to; special leave on full pay sought instead'),
 (D+'2026-08-11_1631_Petering_ack_s89_letter_forwarded.pdf','11 Aug 2026, 4:31 pm','Petering → Shepherd','⭐ Petering acknowledges the s 89 letter forwarded — first written engagement'),
 (D+'2026-08-18_1047_Roberts_FollowUpOnEnquiries_RESENT_personal_email.pdf','18 Aug 2026, 10:47 am','Roberts → Shepherd, cc Petering','"Follow up on Enquiries" re-sent after recall'),
 (D+'correspondence-2026/2026-08-18_to_28_Roberts_FollowUpOnEnquiries_FULL_THREAD.pdf','18–28 Aug 2026','Roberts ↔ Shepherd, cc Petering','Meeting arranged; 24 Aug leave and AVAC requested; 28 Aug AVAC update sought'),
 (D+'correspondence-2026/2026-08-25_1508_Roberts_Teams_invite.pdf','25 Aug 2026, 3:08 pm','Roberts → Shepherd, McQuillan, Petering','Teams invitation continuing the 21 August conference'),
 (D+'correspondence-2026/2026-08-31_FULL_THREAD_v2_Taylor_LSL_AVAC_incl_1606_correction.pdf','31 Aug 2026','Shepherd ↔ Taylor, cc Roberts, Petering','⭐ The formal application (LSL from 13 Jul, annual leave on exhaustion, AVAC today, under protest); 3:34 pm one fortnight at "0.5 FTE", LSL blocked; 4:06 pm the four-point correction'),
 (D+'correspondence-2026/2026-09-03_1027_Taylor_Payroll_LSL_eligibility_04SEP_thread_2-3Sep.pdf','2–3 Sep 2026','Shepherd ↔ Taylor ↔ Payroll, cc Roberts, Petering','⭐ Ad hoc payment requested 2 Sep; process 24926366; 3 Sep Payroll "LSL eligibility only from 04/09/2026", leave audit opened; 10:27 no backdating, no ad hoc before 9 Sep'),
 (D+'correspondence-2026/2026-09-03_1330_Cory_to_Roberts_Taylor_Payroll_TWO_PARTS_coding_and_payment_SENT.pdf','3 Sep 2026, 1:30 pm','Shepherd → Roberts, Taylor, Payroll, cc Petering','⭐ The two-part response: the coding since 3 July, and payment under HR Policy C13 §§2, 6, 8 and 9; long service leave from 13 July; special leave under Directive 12/24'),
 (D+'correspondence-2026/2026-09-03_1452_Together_Beetham_WPSS_referral_and_Petering_holding_reply.pdf','3 Sep 2026','Together → Shepherd','⭐ Petering 2:10 pm: reviewing 14 emails, reply by end of week. Beetham 2:52 pm: referral to the Workers\' Psychological Support Service'),
 ('out/UNION_BRIEF_pay_and_exclusion_2JUL-31AUG2026.pdf','31 Aug 2026','Prepared for Together','The two-page brief: the position in five lines, and every written request for payment'),
]

def para(t,s=B): return P(t,s)

flow=[]
flow.append(P('THE UNION FILE — THE WHOLE PICTURE AND THE ARCHIVE',H1))
flow.append(P('Cory Shepherd, employee number 388372 · AO3, Switchboard Services, Logan Hospital, Metro South Health · Together Queensland member and endorsed workplace delegate · prepared 3 September 2026',SM))
flow.append(Spacer(1,9))

flow.append(P('1. THE POSITION AS AT 3 SEPTEMBER 2026',H2))
flow.append(para('I am employed on a permanent full-time basis, 76 hours per fortnight. My employment commenced on 25 March 2019 and my reinstatement under the agreement of February 2025 preserved continuity of service. Metro South Health described my employment in its own Request for Medical Information of 31 July 2026 as "Permanent Full-time (76 hours per fortnight)".'))
flow.append(para('I have been held out of the workplace since 3 July 2026, and I have received no wages since 13 July 2026 — fifty-two days and four pay days at nil. As a consequence I have given up my accommodation.'))
flow.append(para('On 3 July 2026 Dr Ma completed the Employee Capability Checklist on Metro South\'s own form. It certifies me fit with restrictions and records, in terms: <b>"Usual switchboard operational duties remain suitable; complaint-handling duties are excluded as below."</b> The only duty excluded is complaint handling, and even then complaints are to be "logged and redirected, not actioned or resolved". The recommended pattern is six eight-hour shifts per fortnight, which the checklist records as <b>"the pattern Mr Shepherd has in fact worked and tolerated over the past twelve months"</b>.'))
flow.append(para('<b>No instrument authorising the exclusion has ever been identified.</b> I first asked for it in the Stage 1 process on 4 August 2026 and have asked repeatedly since. No written decision either returning me to work or refusing to has ever been issued.'))

flow.append(P('2. THE CODING, AND WHAT IT HAS COST',H2))
flow.append(para('On 2 July 2026 my manager wrote that unless I advised otherwise, shifts I had not worked would be processed as sick leave. On 3 July at 2:49 pm she wrote that she would continue to process them as "Sick leave / Sick leave no pay" because the leave type had not been confirmed. At 3:18 pm the same day I confirmed it in writing: annual leave, not sick leave without pay.'))
flow.append(para('"Sick Leave – No Pay" has been applied to my record every day since. I have asked for it to be corrected on 10 July, 13 July, 28 July, 5 August, 24 August, 31 August and 3 September. The myHR record of 20 July shows leave of the type "Income Protection – No Pay" requested by my line manager on my behalf. My pay advice of 12 August records "NP Sick Leave" for 76.00 hours at $0.00 gross.'))
flow.append(para('Queensland Health\'s HR Policy C13 (QH-POL-188), section 6, permits a line manager to submit leave on an employee\'s behalf <b>only</b> where the employee\'s request for leave is documented in writing and the supporting documents are retained. My written request of 3 July was for annual leave.'))
flow.append(para('<b>The coding has now become the obstacle.</b> On 3 September Payroll advised that my long service leave eligibility date is "only from 04/09/2026". On the service dates recorded in the agreement under which I was reinstated, seven years\' continuous service fell due on 25 March 2026. Payroll\'s date is 163 days later, and unpaid periods are excluded from continuous service. The largest of those is the "Sick Leave – No Pay" applied since 3 July, which I never applied for and contradicted in writing on the day. The employer\'s own coding has deferred the entitlement now being cited against me, and it moves a day further out for every day it continues.'))

flow.append(PageBreak())
flow.append(P('3. THE REASONS GIVEN FOR NOT PAYING ME — EACH IN THE ARCHIVE',H2))
rows=[[P('<b>Date</b>',SMB),P('<b>What was said</b>',SMB),P('<b>Tab</b>',SMB)]]
for d,w,t in [('2 Jul','Unworked shifts to be processed as sick leave unless otherwise advised','—'),
 ('15 Jul','Pay "sits with your QSuper Claim Manager"; interim duties refused "in any capacity"; accommodation "remains at the discretion of the Employer"','—'),
 ('29 Jul','Further medical information required before capacity can be determined','6'),
 ('30 Jul','The Request for Medical Information is with the delegate for approval','8'),
 ('31 Aug','Leave applied for one fortnight only, "as you are on reduced roster 0.5 FTE"','17'),
 ('3 Sep','Long service leave "cannot be backdated"; the ad hoc payment "cannot be processed prior to Wednesday 9th September"','18')]:
    rows.append([P(d,SM),P(w,SM),P(t,SM)])
tb=Table(rows,colWidths=[20*mm,132*mm,14*mm],repeatRows=1)
tb.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))
flow.append(tb)
flow.append(Spacer(1,5))
flow.append(para('Six positions across nine weeks. None of them identifies a power to direct a fit and available employee away from the workplace without pay, and none of them answers the question asked on 4 August.'))

flow.append(P('4. WHAT TOGETHER HAS HELD, AND WHEN',H2))
for t in ['<b>4 October 2025</b> — my complaint concerning the manager, copied to Heath Moran.',
 '<b>3 November 2025</b> — endorsed by Heath Moran as a Together workplace delegate, alongside Carolyn Jeffrey and Patricia Conaghan, and working the switchboard roster and consultation issues with him from that date.',
 '<b>14–15 July 2026</b> — Heath Moran: the matter is "VERY SERIOUS" and is an <b>urgent referral to Together\'s industrial team</b>.',
 '<b>17 July 2026</b> — Heath Moran: the brief has been delivered in full and the industrial team is engaged and reviewing.',
 '<b>28 July – 3 August 2026</b> — the instrument-anchored letter to HR and the three Stage 1 emails, each copied to Heath Moran.',
 '<b>11 August 2026</b> — Emily Petering acknowledges the s 89 letter and engages by telephone.',
 '<b>13–28 August 2026</b> — the Roberts correspondence, copied to Emily Petering throughout.',
 '<b>21 August 2026</b> — a two-hour conference with Jacqui Roberts and Terry McQuillan, <b>Emily Petering present</b>, across five agenda items. No outcome was reached; the meeting was cut short.',
 '<b>25 August 2026</b> — Teams invitation to continue that conference, Emily Petering included.',
 '<b>31 August – 3 September 2026</b> — the leave application, the correction, the ad hoc payment request and the two-part response, each copied to Emily Petering.',
 '<b>2 September 2026</b> — six asks put to Emily Petering and Heath Moran in writing.',
 '<b>3 September 2026, 2:10 pm</b> — Emily Petering: reviewing the fourteen emails received this week; a reply on the specific questions by the end of the week.',
 '<b>3 September 2026, 2:52 pm</b> — Matthew Beetham, Member Assist: a referral to the Workers\' Psychological Support Service, which is described as assisting with work-related injury including "a lack of support from management", and which provides financial counselling.']:
    flow.append(P(t,BL))
flow.append(Spacer(1,3))
flow.append(para('<b>Seven weeks have passed since the urgent referral to the industrial team of 14 July 2026, and no industrial officer has been identified to me as having carriage of the matter.</b>'))

flow.append(PageBreak())
flow.append(P('5. WHAT REMAINS UNANSWERED',H2))
rows=[[P('<b>#</b>',SMB),P('<b>The question</b>',SMB),P('<b>Asked</b>',SMB),P('<b>Status</b>',SMB)]]
for n,q,a,s in [('1','The instrument authorising the exclusion','4 Aug 2026, repeatedly since','No answer'),
 ('2','A written decision returning me to work within the 3 July restrictions, or declining to, identifying the instrument and the officer','4 Aug 2026','Never issued'),
 ('3','Special leave on full pay under Directive 12/24 cl 6.1 (applied through EB12 cl 9.12)','28 Jul and 5 Aug 2026','Never determined — neither granted nor refused'),
 ('4','A workplace psychosocial risk assessment under EB12 cl 7.2 and the Psychosocial Code 2022','28 Jul 2026','Not conducted'),
 ('5','A task-by-task match of the AO3 role description against the Employee Capability Checklist','28 Jul 2026','Not produced'),
 ('6','Payroll enquiry 4438861','22 Jul 2026','"Pending Investigation"; later shown resolved in myHR, never communicated'),
 ('7','Ad hoc payment, enquiry 4471091, for the fortnight 3–16 August paid at nil on 26 August','2 Sep 2026','Pending'),
 ('8','The basis for applying leave at "0.5 FTE" — the last reduced-hours arrangement expired 28 June 2026','31 Aug 2026','No instrument produced'),
 ('9','The long service leave eligibility calculation, and correction of the coding before it is recalculated','31 Aug and 3 Sep 2026','Leave audit opened 3 Sep; conductor and timeframe unknown'),
 ('10','Who at Together has carriage of the matter','14 Jul 2026','No industrial officer identified')]:
    rows.append([P(n,SM),P(q,SM),P(a,SM),P(s,SM)])
tb=Table(rows,colWidths=[8*mm,86*mm,32*mm,40*mm],repeatRows=1)
tb.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))
flow.append(tb)

flow.append(P('6. WHAT I AM ASKING THE UNION TO DO',H2))
flow.append(P('<b>1. Carriage.</b> Confirm in writing who holds this matter and whether an industrial officer is assigned. The referral was made on 14 July. I ask this as an endorsed delegate as well as a member.',BL))
flow.append(P('<b>2. The payroll escalation.</b> EB12 cl 3.8.2 provides a single payroll point of contact for union officials to escalate payroll errors to, following reasonable steps locally. Those steps are exhausted: on 3 September I wrote to the line manager, to Human Resources, to Payroll as a team and to the Payroll officer by name. I ask that Together make that call.',BL))
flow.append(P('<b>3. The risk assessment.</b> The psychosocial risk assessment sought under EB12 cl 7.2 on 28 July has never been conducted. That is a workplace matter rather than a personal one, and I ask that Together take it up as its own item for Switchboard Services.',BL))
flow.append(Spacer(1,5))
flow.append(para('My appeal in the Queensland Industrial Relations Commission is a separate proceeding and nothing in this document forms part of it.'))
flow.append(para('Cory Shepherd · employee number 388372 · 0417 400 227 · coryshepherd1@hotmail.com',SM))

flow.append(PageBreak())
flow.append(P('7. THE ARCHIVE — EVERY DOCUMENT TOGETHER HAS BEEN SENT OR COPIED ON',H2))
flow.append(para('Each tab is the original document as sent or received. Nothing has been retyped.'))
srcs=[]; counts=[]
for path,_,_,_ in ARCHIVE:
    d=pikepdf.open(path); srcs.append(d); counts.append(len(d.pages))
rows=[[P('<b>Tab</b>',SMB),P('<b>Date</b>',SMB),P('<b>Between</b>',SMB),P('<b>What it is</b>',SMB),P('<b>Pages</b>',SMB)]]
PRE=6  # picture pages before the index page; corrected after first build

# Build the picture first to learn its page count, then lay the index page numbers on top of it.
def build_front(index_rows_pagestart):
    f=list(flow)
    rr=[list(rows[0])]
    pg=index_rows_pagestart
    for (path,date,between,what),n in zip(ARCHIVE,counts):
        rr.append([P(str(len(rr)),SM),P(date,SM),P(between,SM),P(what,SM),P(f'{pg}–{pg+n-1}' if n>1 else str(pg),SM)])
        pg+=n
    t=Table(rr,colWidths=[9*mm,24*mm,36*mm,85*mm,16*mm],repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    f.append(t)
    f.append(Spacer(1,5))
    f.append(P(f'Total: {sum(counts)} pages of original correspondence across {len(ARCHIVE)} tabs, 4 October 2025 to 3 September 2026.',SM))
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=15*mm,title='',author='')
    doc.build(f); buf.seek(0)
    return pikepdf.open(buf)

# pass 1 — learn the length of the front matter
front=build_front(1)
front_pages=len(front.pages)
# pass 2 — archive starts on the page after the front matter
front=build_front(front_pages+1)
if len(front.pages)!=front_pages:
    front=build_front(len(front.pages)+1)
print('front matter pages:',len(front.pages))

out=pikepdf.new()
out.pages.extend(front.pages)
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
out.save('out/UNION_FILE_whole_picture_and_archive_3SEP2026.pdf',fix_metadata_version=False)
print('TOTAL PAGES',len(out.pages))
