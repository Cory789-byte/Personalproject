import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3); H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3)
B=PS('b',fontName='Helvetica',fontSize=9.2,leading=12); SM=PS('sm',fontName='Helvetica',fontSize=8.2,leading=10.3); SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.3)
def tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)])); return t
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('TABLE 1 — LEAVE REQUESTED FROM 3 JULY 2026: EVERY REQUEST, WITH THE EMAIL IT IS IN',H1),
   P('Cory Shepherd (388372) · email numbers refer to the attached “The emails — leave requested from 3 July 2026” · 3 September 2026',SM),Spacer(1,5)]
rows=[[P('<b>Email</b>',SMB),P('<b>Date</b>',SMB),P('<b>To</b>',SMB),P('<b>What was asked</b>',SMB),P('<b>What happened</b>',SMB)]]
data=[('1','2 Jul, 2:38 pm','(from Ms Taylor)','“Unless you advise me otherwise, I will process your shifts that you have not worked as Sick Leave – please confirm by Friday 3rd July before 2:00pm”','the coding is created'),
 ('3','3 Jul, 2:49 pm','(from Ms Taylor)','“As you have not confirmed leave type … I will continue to process as Sick leave / Sick leave no pay”','—'),
 ('4','3 Jul, 3:18 pm','Ms Taylor','“could you please process the balance as ANNUAL LEAVE rather than sick leave without pay” — 29 minutes later','Sick Leave – No Pay applied every day since'),
 ('6','10 Jul, 8:35 am','Ms Forrest','shifts to be “treated as PAID TIME and … not deducted from my leave”','unanswered'),
 ('9','13 Jul, 4:39 pm','Injury Mgmt','“I ask again” — paid time; the basis in writing if refused','15 Jul: pay refused'),
 ('13','28 Jul, 5:39 pm','Injury Mgmt','contests the sick-leave-no-pay coding','holding replies'),
 ('19','5 Aug, 7:30 am','Stage 1','pay restoration; re-credit of leave debited since 3 July','none'),
 ('28','24 Aug, 11:13 am','Ms Roberts','“the appropriate LEAVE BE APPLIED and … an AVAC be submitted”','“speaking with Chloe this afternoon”'),
 ('31','28 Aug, 2:18 pm','Ms Roberts','AVAC update','none'),
 ('32','31 Aug, 10:59 am','Ms Taylor','application: LSL from 13 Jul; annual leave on exhaustion; AVAC today; “I confirm I am not applying for personal leave”; under protest, subject to re-credit','one fortnight at “0.5 FTE”, with sick leave; LSL enquiry 4469554'),
 ('34','31 Aug, 4:06 pm','Ms Taylor','76 hours, not 0.5 FTE; no sick leave; the period from 13 Jul; service dates','—'),
 ('35','2 Sep, 11:07 am','Ms Taylor','ad hoc payment today','“cannot be processed prior to 9 September”'),
 ('40–41','3 Sep','(from Payroll / Ms Taylor)','eligibility date “04/09/2026”; leave audit opened; no backdating; no ad hoc before 9 Sep','—')]
for r in data: rows.append([P(x,SM) for x in r])
s.append(tbl(rows,[13*mm,25*mm,26*mm,72*mm,38*mm]))
s.append(P('The leave type was confirmed at 3:18 pm on 3 July, twenty-nine minutes after the message saying it had not been. The objection to the “Sick Leave – No Pay” coding was made that day and on every occasion since — before any question of long service leave eligibility arose.',B))
s.append(PageBreak())
s.append(P('TABLE 2 — PAYMENT: WHAT IS TO BE ACTIONED, BY PAY PERIOD',H1)); s.append(Spacer(1,5))
rows=[[P('<b>Fortnight</b>',SMB),P('<b>What applies</b>',SMB),P('<b>Hours</b>',SMB),P('<b>Action</b>',SMB),P('<b>Pay date</b>',SMB)]]
data=[('3 Jul – 2 Aug','“Sick Leave – No Pay” applied from 3 Jul (and to shifts before it, per the email of 2 Jul) against the instruction of 3 Jul 3:18 pm. Paid nil on 15 Jul, 29 Jul and 12 Aug','76','Correct the coding from the first date it was applied; AVAC to be submitted (C13 §2); review of pay entitlements from 3 Jul (C13 §9), with the leave audit; long service leave from 13 Jul on the agreement’s dates','missed'),
 ('3 – 16 Aug','Paid nil on Wed 26 Aug — the “most recent prior pay period” in the C13 definition of an ad hoc payment','76','AD HOC PAYMENT NOW — enquiry 4471091, lodged Wed 2 Sep (C13 §8). Coded as long service leave from 13 Jul; failing that, recreation leave 51.31 hrs without prejudice, re-credited when LSL is applied. AVAC to be submitted today','missed — pay today'),
 ('17 – 30 Aug','AVAC processed — process no. 24926366. Applied at “0.5 FTE” with “S/L and A/L in lieu of S/L”','should be 76','Confirm in writing: gross, hours, leave types. If at 0.5 FTE, adjust in the next run','Wed 9 Sep'),
 ('31 Aug – 3 Sep','Pre-eligibility on Payroll’s date; currently “Sick Leave – No Pay”','76','Audit; long service leave from 13 Jul covers it; wages for the held-out period remain claimed','Wed 23 Sep'),
 ('4 – 13 Sep','LONG SERVICE LEAVE, full pay, from Thu 4 Sep at the latest — Payroll’s own eligibility date','76 (38/wk)','Enter now; no further “Sick Leave – No Pay” from 4 Sep','Wed 23 Sep'),
 ('14 Sep on','Long service leave continuing until further notice','76','Continuing','Wed 7 Oct …')]
for r in data: rows.append([P(x,SM) for x in r])
s.append(tbl(rows,[24*mm,66*mm,20*mm,46*mm,18*mm]))
s.append(P('An ad hoc payment “enables employees to request a payment that was missed or requires correction outside of the regular pay day schedule without waiting for the next pay cycle” (HR Policy C13, QH-POL-188, §8). One was processed on 11 Mar 2025 (log 4045255). A line manager notified of an incorrect wage payment “must take all steps to rectify the error” (§2).',B))
s.append(P('All leave applied for is applied for under protest and subject to re-credit, on the basis set out in the application of 31 August (email 32, paragraph 4). Certified fit with restrictions since 3 July 2026; ready and available to work throughout.',B))
doc.build(s); buf.seek(0); out=pikepdf.open(buf)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/TABLES_leave_requests_and_payment_3SEP2026.pdf'); print('pages',len(out.pages))
