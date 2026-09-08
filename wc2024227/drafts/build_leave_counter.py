import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3)
B=PS('b',fontName='Helvetica',fontSize=9.2,leading=12)
SM=PS('sm',fontName='Helvetica',fontSize=8.2,leading=10.3); SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.3)
Q=PS('q',fontName='Helvetica-Oblique',fontSize=8.8,leading=11.4,leftIndent=6*mm,spaceBefore=1,spaceAfter=1)
buf=io.BytesIO()
doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('LEAVE AND PAY — WHAT WAS ASKED FOR, AND WHEN',H1),
   P('Cory Shepherd (388372), AO3, Switchboard Services, Logan Hospital · in answer to the emails of 2–3 September 2026 · message numbers refer to the attached correspondence, reproduced message by message',SM),Spacer(1,4)]
s.append(P('1. THE LEAVE REQUESTS — FROM THE FIRST DAY OF THE ABSENCE',H2))
s.append(P('Every request below is in the attached correspondence, in the words used at the time.',B))
rows=[[P('<b>Msg</b>',SMB),P('<b>Date</b>',SMB),P('<b>To</b>',SMB),P('<b>What was asked</b>',SMB),P('<b>Outcome</b>',SMB)]]
data=[
 ('4','3 Jul, 3:18 pm','Ms Taylor','“could you please process the balance as ANNUAL LEAVE rather than sick leave without pay” — leave type confirmed 29 minutes after msg 3 said it had not been','sick leave / sick leave no pay applied anyway'),
 ('6','10 Jul, 8:35 am','Ms Forrest','shifts to be “treated as PAID TIME and … not deducted from my leave”','unanswered'),
 ('9','13 Jul, 4:39 pm','Injury Mgmt','“I ask again” — paid time; if refused, the basis in writing; interim duties offered','15 Jul (msg 11): pay refused; duties refused'),
 ('12','22 Jul','Payroll','Payroll Enquiry 4438861 — type “Leave”','now shows RESOLVED (exhibit C); no resolution ever communicated'),
 ('13','28 Jul, 5:39 pm','Injury Mgmt','contests the sick-leave-no-pay coding','holding replies'),
 ('19','5 Aug, 7:30 am','Stage 1','pay restoration; re-credit of leave debited since 3 July','none'),
 ('20','12 Aug, 6:21 pm','LBH / Harrison','wages and hardship','no pay'),
 ('28','24 Aug, 11:13 am','Ms Roberts','“that the appropriate LEAVE BE APPLIED and that an AVAC be submitted”','24 Aug 12:19: “speaking with Chloe this afternoon”'),
 ('31','28 Aug, 2:18 pm','Ms Roberts','AVAC update','none'),
 ('32','31 Aug, 10:59 am','Ms Taylor','formal application: LSL from 13 Jul; annual leave on exhaustion; AVAC today; under protest, subject to re-credit; “I confirm I am not applying for personal leave”','one fortnight, at “0.5 FTE”, with sick leave; LSL enquiry 4469554 lodged'),
 ('34','31 Aug, 4:06 pm','Ms Taylor','76 hours not 0.5 FTE; no sick leave; period from 13 Jul; service dates for Payroll','—'),
 ('35','2 Sep, 11:07 am','Ms Taylor','ad hoc payment today','3 Sep: “cannot be processed prior to 9 September”'),
 ('37–38','2 Sep, 1:00 & 2:05 pm','Payroll / Ms Taylor','resolve the LSL issue; copies of the enquiry and records','3 Sep: eligibility date “04/09/2026”; leave audit in progress'),
]
for r in data: rows.append([P(r[0],SM),P(r[1],SM),P(r[2],SM),P(r[3],SM),P(r[4],SM)])
t=Table(rows,colWidths=[11*mm,26*mm,22*mm,71*mm,44*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t)
s.append(P('Leave was asked for on the first day of the absence and on eleven further occasions before the formal application of 31 August. The leave type was confirmed as annual leave at 3:18 pm on 3 July, twenty-nine minutes after the message that said it had not been confirmed. “Sick Leave – No Pay” has been applied every day since, without any application by me (exhibit B).',B))

s.append(P('2. THE ELIGIBILITY DATE OF 4 SEPTEMBER 2026',H2))
s.append(P('Payroll advises (msg 40) that my long service leave eligibility date is 4 September 2026. The dates on my record are these:',B))
for x in ['Employment commenced 25 March 2019. Reinstated in February 2025 with effect from 20 September 2024 and continuity of service preserved.',
          'Seven years’ continuous service therefore fell due on 25 March 2026 (Award cl 22(c)).',
          'Payroll’s date of 4 September 2026 is 163 days later.']:
    s.append(P('•  '+x,B))
s.append(P('A deferral of that length can only arise if periods have been excluded from continuous service. The unpaid periods on my record are: leave without pay from 13 December 2024 to 23 February 2025 (72 days); unpaid leave recorded during 2025–26; and every day since 3 July 2026 coded “Sick Leave – No Pay” (61 days to 2 September). Together those are consistent with the 163-day deferral. I ask Payroll to show the calculation — the commencement date used and each period excluded, with dates and leave types — so that this can be confirmed rather than inferred.',B))
s.append(P('If the days since 3 July 2026 are among the periods excluded, then the deferral has been caused by a leave coding I did not apply for and contradicted in writing on the day it was first applied (msgs 3 and 4). It also means the eligibility date moves out by a further day for every day the coding continues. The leave audit now under way (msg 40) is the right place to correct this, and I ask that the coding from 3 July 2026 be corrected in accordance with my written instruction of that date before eligibility is recalculated.',B))
s.append(P('Without prejudice to that: on Payroll’s own date I am eligible from 4 September 2026, and I apply for long service leave from that date forward, at my substantive 76 hours per fortnight, continuing. That application is made on the same basis as my application of 31 August — under protest and subject to re-credit.',B))

s.append(P('3. THE PAYMENT',H2))
for x in ['The process number for the 17–30 August AVAC is 24926366 (corrected by Ms Taylor, msg 39). Payroll could not locate the earlier number by telephone on 2 September (msg 38). I ask for written confirmation of what will be paid on 9 September: gross amount, hours, and the leave types debited.',
          'An ad hoc payment is by definition an off-cycle payment; a statement that it “cannot be processed prior to 9 September” is a statement about the pay cycle, not about an ad hoc payment. An ad hoc payment was processed for me on 11 March 2025 (exhibit C, log 4045255). Enquiry 4471091 for an ad hoc payment was lodged on 2 September and is pending. If it is refused, I ask for the reason in writing and the officer who decided it.',
          'Enquiry 4438861 of 22 July 2026 (type “Leave”) now shows as “Resolved” (exhibit C). No resolution was communicated to me. I ask what the resolution was and when it was recorded.']:
    s.append(P('•  '+x,B))
s.append(P('4. EXHIBITS (following)',H2))
for x in ['A — Leave balances as at 2 September 2026: recreation leave 51.31 hours; sick leave 14.66 hours.',
          'B — Request overview: “SICK LEAVE – NO PAY”, entered daily on my behalf and approved, from 3 August 2026 onward.',
          'C — My payroll enquiries: 4471091 (ad hoc payment, 2 Sep 2026, pending); 4438861 (leave, 22 Jul 2026, “Resolved”); 4045255 (ad hoc payment, 11 Mar 2025, resolved).',
          'D — The correspondence, 2 July – 3 September 2026, reproduced message by message (41 messages).']:
    s.append(P(x,B))
s.append(Spacer(1,4)); s.append(P('Cory Shepherd · 388372 · 0417 400 227 · 3 September 2026',SM))
doc.build(s); buf.seek(0)
out=pikepdf.open(buf)
for ex in ['../documents/correspondence-2026/2026-09_Leave1.pdf','../documents/correspondence-2026/2026-09_Leave.pdf','../documents/correspondence-2026/2026-09_My_payroll_enquiries.pdf','out/CORRESPONDENCE_THREAD_reproduced_2JUL-3SEP2026.pdf']:
    out.pages.extend(pikepdf.open(ex).pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/RESPONSE_PACK_leave_and_pay_3SEP2026.pdf'); print('response pack pages:',len(out.pages))
