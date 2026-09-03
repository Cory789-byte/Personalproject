import io, re, pickle, pikepdf
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak, KeepTogether
S='/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/thread'
M=pickle.load(open(f'{S}/messages.pkl','rb'))
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3); H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3)
B=PS('b',fontName='Helvetica',fontSize=9.2,leading=12); SM=PS('sm',fontName='Helvetica',fontSize=8.1,leading=10.2); SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.1,leading=10.2)
MH=PS('mh',fontName='Helvetica-Bold',fontSize=10.5,leading=13); HD=PS('hd',fontName='Helvetica',fontSize=8.6,leading=10.8,textColor=colors.HexColor('#333333'))
def tbl(rows,widths):
    t=Table(rows,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return t
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('SERVICE DATE AND LEAVE CREDITS UNDER THE REINSTATEMENT AGREEMENT OF FEBRUARY 2025 — FOR THE LEAVE AUDIT',H1),
   P('Cory Shepherd (388372), AO3, Switchboard Services, Logan Hospital · 3 September 2026 · the agreement is held by the Health Service and is not reproduced here',SM),Spacer(1,4),
   P('1. WHAT THE AGREEMENT PROVIDES, AND WHAT THE RECORD SHOULD SHOW',H2)]
rows=[[P('<b>#</b>',SMB),P('<b>Under the agreement</b>',SMB),P('<b>The record should show</b>',SMB),P('<b>What the record shows (2–3 Sep 2026)</b>',SMB),P('<b>Verification requested</b>',SMB)]]
data=[('1','Employment commenced 25 March 2019 (recited in the agreement)','Commencement 25.03.2019','Not stated by Payroll','Confirm the commencement date held'),
 ('2','Reinstatement effective 20 September 2024, continuity of service preserved — effective “despite any documents the Health Service may require … for payroll purposes”','Continuous service unbroken from 25.03.2019 through 20.09.2024','LSL eligibility given as 04.09.2026 (msg 40)','Confirm the continuous service date held and correct it if it differs'),
 ('3','54.16 hours annual leave, paid out 23 October 2024, to be credited on execution','Credit of 54.16 hrs recreation leave, Feb–Mar 2025','Recreation leave balance 51.31 hrs at 02.09.2026 (exhibit A)','Confirm the credit was applied, with date; if not, apply it'),
 ('4','54.16 hours leave loading to be credited on execution','Credit of 54.16 hrs leave loading, Feb–Mar 2025','Not visible','Confirm the credit was applied, with date; if not, apply it'),
 ('5','Personal leave balances reinstated as at the separation date','Sick leave balance restored to the 20.09.2024 figure','Sick leave balance 14.66 hrs at 02.09.2026 (exhibit A)','Confirm the balance restored and the figure used'),
 ('6','The value of the credits at 3–5 was deducted from the amount paid under the agreement','The credits were paid for by me','—','Confirm items 3–5 accordingly'),
 ('7','13 December 2024 – 23 February 2025 treated as leave without pay (72 days)','Whether excluded from continuous service, and on what basis','Unknown','State whether excluded, and the basis, given continuity was preserved'),
 ('8','Seven years’ continuous service on the dates at 1–2 fell due 25 March 2026 (Award cl 22(c))','LSL eligibility 25.03.2026','Payroll: 04.09.2026 — 163 days later','Provide the calculation: every period excluded, with dates and leave type'),
 ('9','— (2026 coding, not the agreement)','Leave from 3 July 2026 coded as confirmed in writing at 3:18 pm on 3 July: annual leave (msgs 3–4)','“Sick Leave – No Pay” entered daily on my behalf and approved (exhibit B); 61 days to 2 Sep','Correct the coding from 3 July before eligibility is recalculated; cease the daily entries')]
for r in data: rows.append([P(r[0],SM)]+[P(escape(x),SM) for x in r[1:]])
s.append(tbl(rows,[7*mm,50*mm,40*mm,42*mm,35*mm]))
s.append(P('If the days since 3 July 2026 are among the periods excluded, the 163-day deferral has been produced by a leave coding I did not apply for and contradicted in writing on the day it was first applied, and it moves out by a day for every day the coding continues. On Payroll’s own date I am eligible from 4 September 2026 and have applied for long service leave from that date forward at 76 hours per fortnight, under protest and subject to re-credit.',B))
s.append(P('2. THE COMMUNICATIONS THAT BEAR ON THIS, INCLUDING EVERY REQUEST FOR LEAVE OR PAY SINCE 3 JULY (reproduced in part 3)',H2))
SEL=[1,3,4,6,9,10,12,13,19,20,28,31,32,33,34,35,36,37,38,39,40,41]
WHY={6:'REQUEST — shifts to be treated as paid time, not deducted from leave; return to be facilitated',9:'REQUEST — “I ask again”; if refused, the basis in writing; interim duties offered',10:'REQUEST — second email of 13 July to Injury Management',12:'REQUEST — Payroll Enquiry 4438861, type “Leave” (now shown “Resolved”, never communicated)',13:'REQUEST — contests the sick-leave-no-pay coding and the QSuper basis',19:'REQUEST — Stage 1: pay restoration and re-credit of leave debited since 3 July',20:'REQUEST — wages and hardship; no income from any source',28:'REQUEST — “the appropriate leave be applied and … an AVAC be submitted”',31:'REQUEST — AVAC update',35:'REQUEST — ad hoc payment today',37:'REQUEST — Payroll to resolve the long service leave issue',38:'REQUEST — copies of the enquiry and records; MyHR access regained',1:'the exclusion and the sick-leave default are created',3:'sick-leave processing “as you have not confirmed leave type”',4:'leave type confirmed: annual leave — 29 minutes later',32:'formal application: LSL from 13 Jul; “I confirm I am not applying for personal leave”; under protest, re-credit',33:'one fortnight, “0.5 FTE”, “S/L and A/L in lieu of S/L”; LSL blocked',34:'76 hours; no sick leave; service dates 25.03.2019 / 20.09.2024 given for Payroll',36:'PRN processed for 9 Sep; balances as at 2 Sep; LSL still blocked',39:'process no. corrected to 24926366; LSL enquiry 4469554 lodged 31 Aug',40:'Payroll: eligibility date 04/09/2026; leave audit log created',41:'no backdating; ad hoc not before 9 Sep'}
rows=[[P('<b>Msg</b>',SMB),P('<b>When</b>',SMB),P('<b>From → to</b>',SMB),P('<b>What it establishes</b>',SMB)]]
for n in SEL:
    m=M[n-1]; rows.append([P(str(n),SM),P(m['when'].strftime('%a %d %b, %H:%M'),SM),P(escape(m['frm']+' → '+re.sub(r'<.*?>','',m['to']).strip()[:40]),SM),P(WHY[n],SM)])
s.append(tbl(rows,[10*mm,28*mm,60*mm,76*mm]))
s.append(P('3. THE COMMUNICATIONS, REPRODUCED',H2)); s.append(P('Each message as sent; standard email boilerplate omitted; nothing else altered.',SM)); s.append(PageBreak())
SUBJ={6:'Re: Cory Shepherd_ECC further information (MSH-INJ-5795)',9:'Re: Cory Shepherd_ECC further information (MSH-INJ-5795)',10:'Re: Cory Shepherd_ECC further information (MSH-INJ-5795)',12:'Payroll Enquiry 4438861 — Leave',13:'Response to 2-15 July 2026 correspondence - incorrect application of EB12, Award and QH policies (MSH-INJ-5795)',19:'Stage 1 — roster, leave and pay (MSH-INJ-5795)',20:'RE: (MSH-INJ-5795) — wages and hardship',28:'Re: Follow up on Enquiries',31:'Re: Follow up on Enquiries',35:'Re: Cory Shepherd (388372) — application for long service leave and annual leave',37:'Fw: Cory Shepherd (388372) RE: Please respond to Chloe Taylor regarding long service leave',38:'Re: Cory Shepherd (388372) RE: Please respond to Chloe Taylor regarding long service leave',1:'Cory - ECC/Leave Type',3:'RE: Cory - ECC/Leave Type',4:'Re: Cory - ECC/Leave Type',32:'Cory Shepherd (388372) — application for long service leave and annual leave, and request for AVAC to be processed today',33:'RE: (as above)',34:'Re: (as above)',36:'RE: (as above)',39:'Cory Shepherd (388372) RE: Please respond to Chloe Taylor regarding long service leave and why it can not be actioned',40:'RE: (as above)',41:'RE: (as above)'}
for n in SEL:
    m=M[n-1]
    hdr=[P(f'Message {n}.  {m["when"]:%A %d %B %Y, %H:%M}',MH),P(f'<b>From:</b> {escape(m["frm"])}',HD),P(f'<b>To:</b> {escape(re.sub(r"<.*?>","",m["to"]).strip() or "—")}',HD)]
    if m['cc']: hdr.append(P(f'<b>Cc:</b> {escape(re.sub(r"<.*?>","",m["cc"]).strip())}',HD))
    hdr.append(P(f'<b>Subject:</b> {escape(SUBJ[n])}',HD)); hdr.append(Spacer(1,3)); s.append(KeepTogether(hdr))
    for ln in m['body']: s.append(P(escape(ln) if ln.strip() else '&nbsp;',B))
    s.append(Spacer(1,5)); s.append(P('— end of message —',SM)); s.append(Spacer(1,8))
s.append(PageBreak()); s.append(P('4. EXHIBITS — A: leave balances 02.09.2026 · B: “Sick Leave – No Pay” request overview · C: my payroll enquiries',H2))
doc.build(s); buf.seek(0); out=pikepdf.open(buf)
for ex in ['../documents/correspondence-2026/2026-09_Leave1.pdf','../documents/correspondence-2026/2026-09_Leave.pdf','../documents/correspondence-2026/2026-09_My_payroll_enquiries.pdf']:
    out.pages.extend(pikepdf.open(ex).pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/AGREEMENT_CREDITS_and_service_date_pack_3SEP2026.pdf'); print('pages',len(out.pages))
