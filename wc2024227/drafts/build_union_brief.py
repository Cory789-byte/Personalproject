from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_LEFT

H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=4)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3)
B=PS('b',fontName='Helvetica',fontSize=9.3,leading=12.2,alignment=TA_LEFT)
SM=PS('sm',fontName='Helvetica',fontSize=8.4,leading=10.6)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.4,leading=10.6)
Q=PS('q',fontName='Helvetica-Oblique',fontSize=9.0,leading=11.8,leftIndent=6*mm,spaceBefore=1,spaceAfter=1)

doc=SimpleDocTemplate('out/UNION_BRIEF_pay_and_exclusion_2JUL-31AUG2026.pdf',pagesize=A4,
    leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm,
    title='Pay and exclusion - the record, 2 July to 31 August 2026',author='')
s=[]
s.append(P('PAY AND THE EXCLUSION — THE RECORD',H1))
s.append(P('Cory Shepherd (388372), AO3, Switchboard Services, Logan Hospital · 2 July – 31 August 2026 · prepared for Together Queensland',SM))
s.append(Spacer(1,4))

s.append(P('THE POSITION IN FIVE LINES',H2))
for t in [
 'I have been held out of the workplace since 3 July 2026 and have received no wages since 13 July 2026.',
 'On 3 July 2026 Dr Ma certified me fit with restrictions on Metro South’s own Employee Capability Checklist; it records that usual switchboard operational duties remain suitable. I have been ready, willing and available throughout.',
 'No instrument for the exclusion has ever been identified, although I asked in the Stage 1 process on 4 August 2026.',
 'My pay advice of 12 August 2026 records me on “NP Sick Leave” for 76.00 hours, gross $0.00. I never applied for sick leave.',
 'As a consequence of the non-payment I have given up my accommodation.']:
    s.append(P('•  '+t,B))

s.append(P('EVERY WRITTEN REQUEST FOR PAYMENT — ELEVEN IN 59 DAYS',H2))
rows=[[P('<b>#</b>',SMB),P('<b>Date</b>',SMB),P('<b>To</b>',SMB),P('<b>The ask</b>',SMB),P('<b>The answer</b>',SMB)]]
data=[
 ('1','3 Jul, 3:18 pm','Ms Taylor','“process the balance as annual leave rather than sick leave without pay”; confirm right to attend','continued processing as “Sick leave / Sick leave no pay”'),
 ('2','10 Jul, 8:35 am','Ms Forrest / IM','“confirm that these shifts will be treated as paid time and will not be deducted from my leave”; return be facilitated','unanswered'),
 ('3','13 Jul, 4:39 pm','Injury Mgmt','“I ask again” — paid time; if refused, the basis in writing. Interim duties offered (finance; scanning/records)','15 Jul: pay refused — “sits with your QSuper Claim Manager”; duties refused “in any capacity”'),
 ('4','22 Jul','Payroll','Payroll Enquiry 4438861','“Pending Investigation” — still, 40 days on'),
 ('5','28 Jul, 5:39 pm','IM, cc union','contests the coding; QSuper is “an insurance arrangement which is not a source of wages”','29–30 Jul holding replies'),
 ('6','5 Aug','Stage 1 reply','pay restoration and re-credit of leave debited since 3 July','closed without either'),
 ('7','12 Aug','LBH / Harrison','§3 Wages and hardship — “no income from any source”','13 Aug reply; no pay'),
 ('8','21 Aug','Conference (verbal)','pay and leave raised (Ms Roberts, Ms Petering present)','24 Aug: “speaking with Chloe this afternoon”'),
 ('9','24 Aug, 11:13 am','Ms Roberts','“the appropriate leave be applied and … an AVAC be submitted … to facilitate the processing of my entitlements”','no AVAC followed'),
 ('10','28 Aug, 2:18 pm','Ms Roberts','AVAC update sought','none'),
 ('11','31 Aug, 10:59 am','Ms Taylor','formal application — LSL from 13 July, annual leave on exhaustion, AVAC today, under protest and subject to re-credit','3:34 pm: one fortnight only (17–30 Aug), PRN 249 863 66, at “0.5 FTE”, leave type including sick leave; LSL blocked “by the system”, referred to Payroll'),
 ('12','31 Aug, 4:06 pm','Ms Taylor','correction — substantive 76 hours; no sick leave; the full period from 13 July; urgent processing','pending'),
]
for r in data: rows.append([P(r[0],SM),P(r[1],SM),P(r[2],SM),P(r[3],SM),P(r[4],SM)])
t=Table(rows,colWidths=[8*mm,24*mm,24*mm,63*mm,55*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
 ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),
 ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
 ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))
s.append(t)
s.append(P('The first payment action in 59 days came at request 11 — four and a half hours after a same-day deadline with the union copied — and was one fortnight, at half rate.',B))

s.append(P('FOUR PAIRINGS FROM THE DOCUMENTS — VERBATIM, WITH TIMESTAMPS',H2))
s.append(P('1. The sick-leave coding lost its stated basis on day one.',SMB))
s.append(P('3 July, 2:49 pm, Ms Taylor: “As you have not confirmed leave type for the past pay period – I will continue to process as Sick leave / Sick leave no pay.”',Q))
s.append(P('3 July, 3:18 pm, Mr Shepherd: “could you please process the balance as annual leave rather than sick leave without pay.”',Q))
s.append(P('The leave type was confirmed 29 minutes later. “NP Sick Leave” was nevertheless carried into the August payslip.',SM))
s.append(P('2. The stated pay basis was corrected within 46 minutes — and relied on anyway.',SMB))
s.append(P('13 July, 3:53 pm, Injury Management: “As you currently have an active open QSuper Income Protection claim, any payments … would be facilitated by them.”',Q))
s.append(P('13 July, 4:39 pm, Mr Shepherd: “I no longer have an active open QSuper Income Protection claim; that claim is now closed … There is no income protection payment that could respond to the present situation.”',Q))
s.append(P('15 July, Ms Harrison: pay refused — “we are not responsible for your payments whilst on this claim … sits with your QSuper Claim Manager.”',Q))
s.append(P('3. Alternative duties were offered on day ten and refused in any capacity.',SMB))
s.append(P('13 July, Mr Shepherd: “I am ready and willing to perform suitable interim duties of that kind [finance; scanning/records], within my certified capacity, as an alternative to remaining off work unpaid.” — 15 July: interim duties refused “in any capacity”.',Q))
s.append(P('4. The 0.5 FTE applied on 31 August has no current instrument.',SMB))
s.append(P('The reduced-hours arrangements of 2026 were each a “Change to Working Conditions (Temporary)”; the last (approved 9 June 2026) had an effective period of 25 May to 28 June 2026 and was not extended. The exclusion began five days after it expired. The 12 August payslip itself records 76.00 hours.',SM))

s.append(P('WHAT I ASK THE UNION TO TAKE UP',H2))
for i,t in enumerate([
 'PAY, as a matter in its own right: I have been ready, willing and able within the certified restrictions since 3 July. The wages question does not depend on the medical process and should not wait behind it.',
 'THE CODING AND THE RATE: the absence recoded from “NP Sick Leave” in accordance with my application; leave applied at substantive hours (76/fortnight), not “0.5 FTE”; and the full period from 13 July adjusted, not one fortnight.',
 'LONG SERVICE LEAVE: the system “will not allow” LSL. My employment commenced 25 March 2019 and my 2025 reinstatement preserved continuity — seven years fell due 25 March 2026. If Payroll’s recorded service date says otherwise, it was not corrected on reinstatement and needs to be.',
 'A DECISION: that the Health Service either return me to work within the 3 July restrictions by a stated date, or provide a written decision declining to, identifying the instrument relied on and the decision-maker.'],1):
    s.append(P(f'{i}.  '+t,B))
s.append(Spacer(1,3))
s.append(P('Everything above is documented; source emails and payslips are available on request. All leave applied for on 31 August was applied for under protest and subject to re-credit, in the application itself.',SM))
s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com · 31 August 2026',SM))
doc.build(s)
print('built')
