import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.6,leading=14,spaceBefore=11,spaceAfter=4)
B=PS('b',fontName='Helvetica',fontSize=9.5,leading=13,spaceAfter=7)
BL=PS('bl',fontName='Helvetica',fontSize=9.5,leading=13,spaceAfter=6,leftIndent=9*mm,firstLineIndent=-5*mm)
SM=PS('sm',fontName='Helvetica',fontSize=8.3,leading=10.5)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.3,leading=10.5)
s=[]
s.append(P('NOTICE OF DISPUTE — STAGE 2',H1))
s.append(P('Clause 1.11.2(b), Queensland Public Health Sector Certified Agreement (No. 12) 2025',SM))
s.append(Spacer(1,7))
r=[[P('<b>To</b>',SMB),P('Ms Noelle Cridland, Health Service Chief Executive, Metro South Health — as the appropriate management representative under clause 1.11.2(b), for the reasons at paragraph 2',SM)],
   [P('<b>Copied to</b>',SMB),P('Ms Jacqui Roberts, Principal Consultant, Human Resources, Logan and Beaudesert Health Service · Ms Emily Petering, Together Queensland · Metro South Correspondence',SM)],
   [P('<b>Employee</b>',SMB),P('Cory Shepherd, employee number 388372 — AO3, Switchboard Services, Logan Hospital. Permanent full-time, 76 hours per fortnight. Together Queensland member and endorsed workplace delegate.',SM)],
   [P('<b>Date</b>',SMB),P('3 September 2026',SM)],
   [P('<b>Matter</b>',SMB),P('Attendance, roster, leave and pay from 26 June 2026 (MSH-INJ-5795)',SM)]]
t=Table(r,colWidths=[24*mm,146*mm])
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))
s.append(t)

s.append(P('1. THE REFERRAL',H2))
s.append(P('I refer this dispute to Stage 2 under clause 1.11.2(b) of the Agreement, and ask that a conference of the parties be arranged. I ask that Together Queensland attend with me.',B))
s.append(P('A Stage 1 notice was given on 3 August 2026. On 4 August 2026 Ms Taylor acknowledged that the 24-hour requirement in clause 1.11.2(a) "will not be achieved", confirmed the dispute was under review, and undertook that I would be contacted on completion of the review. The seven days allowed by clause 1.11.2(a) expired on 10 August 2026. No outcome of Stage 1 has ever been communicated to me.',B))
s.append(P('I earlier referred the matter to Stage 2 and withdrew that referral on 28 August 2026, in order to work through the issues directly with Ms Roberts. In doing so I withdrew the referral only, and recorded that my concerns regarding pay, the leave debited since 3 July 2026 and the adjustments in the Employee Capability Checklist of 3 July 2026 remained unresolved and in dispute. They remain unresolved, and the position has worsened since.',B))

s.append(P('<b>The matter can be put shortly.</b> I have been absent from the workplace since 3 July 2026 because I was directed not to attend. On each day of that absence a leave type has been selected and entered on my record on my behalf. Of the leave types available, three produce a payment and one does not. The one that does not has been selected on every day since 3 July 2026 — after I instructed in writing on that day that annual leave was to be applied, and after every objection I have made since. That is why I have not been paid.',B))
s.append(P('2. WHY THIS REFERRAL IS MADE TO YOU',H2))
s.append(P('Clause 1.11.2(b) requires the matter to be referred to "the appropriate management representative". Stage 1 was conducted with my immediate supervisor, as clause 1.11.2(a) provides. I refer Stage 2 to you because two of the matters in dispute cannot be decided below your office.',B))
s.append(P('<b>Special leave is a chief executive\'s power.</b> Directive 12/24, which applies to every employee covered by the Agreement through clause 9.12, provides at clause 6.1 that "a chief executive may approve paid leave for employees for any purpose", and at clause 6.5 that "in determining an application for leave under clause 6.1 or clause 6.2, a chief executive must consider" the reason for the leave, its duration, and the impact on the employee if it is not approved. Section 6 of HR Policy C13 records that the delegate for a decision of this kind is the officer listed in the HR Delegations Manual. I applied for special leave on full pay on 28 July and again on 5 August 2026. It has never been determined. No officer below your office, or your delegate under the HR Delegations Manual, is able to determine it.',B))
s.append(P('<b>A decision on special leave would resolve the immediate position on its own.</b> It is paid at full pay, and under Directive 12/24 it is not debited from any leave account. Granting it would therefore restore my income and leave my accrued entitlements intact. It would not require the Health Service to determine the leave coding, the hours at which leave has been applied, the long service leave eligibility date, or the basis of the direction that I not attend — each of which would remain in dispute and can be dealt with at the conference. It is the one decision in this matter that can be made now, by one office, and it requires no view to be taken on any of the others.',B))
s.append(P('<b>No instrument or officer has ever been identified for the direction that I not attend.</b> I asked for both in the Stage 1 process on 4 August 2026 and have asked since. The identification of the delegate and the instrument, or the making of a decision, sits at executive level.',B))
s.append(P('I do not ask that you convene the conference personally. If you nominate a representative to hold it and to decide the matters within their delegation, I will attend with them, and I ask only that the matters reserved to the chief executive be determined by you or by your delegate under the HR Delegations Manual.',B))
s.append(P('3. THE MATTERS IN DISPUTE',H2))
for n,txt in [('1','<b>Pay.</b> I have received no wages since 13 July 2026 — fifty-two days, and three pay days at nil: 29 July, 12 August and 26 August 2026. I have been ready, willing and available throughout, and certified fit with restrictions on the Health Service\'s own form since 3 July 2026.'),
 ('2','<b>The direction not to attend.</b> I have been held out of the workplace since 3 July 2026. I asked in the Stage 1 process on 4 August 2026 for the instrument authorising that direction, and have asked repeatedly since. It has never been identified, and no written decision returning me to work or declining to has ever been issued.'),
 ('3','<b>The leave coding, and how the payment became nil.</b> Each "Sick Leave – No Pay" entry is a positive act — a leave type selected from those available and submitted on my behalf. The alternatives were available, and they were known to the officer entering them: on 4 August 2026 Ms Taylor identified my recreation leave balance at 41.21 hours and undertook that, absent a response, she would apply it "to ensure you receive the available paid leave entitlement for this period". The pay advice for that fortnight records "NP Sick Leave" 76.00 hours and gross pay of $0.00. Section 6 of HR Policy C13 permits leave to be submitted on an employee\'s behalf only where the employee\'s request for leave "is documented in writing" and the supporting documents "are sourced and retained". My written requests are for annual leave (3 July 2026) and special leave on full pay (5 August 2026). There is no written request for sick leave without pay, and on 31 August 2026 I confirmed in terms that I was not applying for personal leave. I have at no point declined to be paid: on 5 August 2026 I declined only that the absence be funded out of my own accrued recreation leave, and asked in the same sentence that special leave on full pay be applied instead.'),
 ('4','<b>Special leave.</b> My application for special leave on full pay under Directive 12/24, made on 28 July and 5 August 2026, has been neither granted nor refused.'),
 ('5','<b>Hours.</b> Leave was applied on 31 August 2026 at "0.5 FTE". The last reduced-hours arrangement expired on 28 June 2026 and nothing replaced it. The Health Service\'s own Request for Medical Information of 31 July 2026 describes my employment as "Permanent Full-time (76 hours per fortnight)".'),
 ('6','<b>Long service leave.</b> Payroll advised on 3 September 2026 that eligibility arises "only from 04/09/2026". On the service dates recorded in the agreement under which I was reinstated in February 2025, seven years\' continuous service fell due on 25 March 2026. Unpaid periods are excluded from continuous service, and the coding in dispute is the largest of them.'),
 ('7','<b>Consultation and risk.</b> The workplace psychosocial risk assessment sought under clause 7.2 on 28 July 2026 has not been conducted, and the task-by-task match of the role description against the Employee Capability Checklist, sought the same day, has not been produced.')]:
    s.append(P(f'<b>{n}.</b>&nbsp;&nbsp;{txt}',BL))

s.append(P('4. THE AGREEMENT\'S REQUIREMENTS',H2))
s.append(P('<b>Clause 1.11.4</b> provides that "the status quo existing before the emergence of a dispute is to continue whilst the procedure is being followed". The status quo before 3 August 2026 was that I was employed, at 76 hours per fortnight, and paid. That has not been maintained: since the dispute was notified, my absence has been coded to a leave type that pays nothing, leave has been applied at half my hours, and my long service leave eligibility has been deferred.',B))
s.append(P('<b>Clause 1.11.5</b> provides that "no party shall act in a manner unreasonably or intentionally delay the timely resolution of a dispute".',B))
s.append(P('<b>Clause 1.11.2(b)</b> provides that the Stage 2 process "should not extend beyond seven days". I ask that the conference be arranged and held on or before <b>Wednesday 10 September 2026</b>.',B))

s.append(P('5. WHAT I SEEK',H2))
SEEK=[
 '''A determination of my application for special leave on full pay from 3 July 2026, by you or by your delegate under the HR Delegations Manual, in writing, with reasons addressing the considerations in clause 6.5 of Directive 12/24.''',
 '''Payment of the wages withheld since 13 July 2026; alternatively, the leave I have applied for entered without debit to my accrued credits, and the ad hoc payment pending under enquiry 4471091 processed against it.''',
 '''Correction of the leave coding from the first date it was applied, and before long service leave eligibility is recalculated in the leave audit opened on 3 September 2026.''',
 '''Leave and pay applied at 76 hours per fortnight, or the instrument relied on for any lesser figure.''',
 '''A written decision either returning me to work within the restrictions recorded on 3 July 2026 by a stated date, or declining to, identifying the instrument relied on and the officer who decided it.''',
 '''A copy of the written request and supporting documents on which each "Sick Leave – No Pay" entry since 3 July 2026 was made, as required by section 6 of HR Policy C13.''',
 '''The workplace psychosocial risk assessment sought under clause 7.2 on 28 July 2026, and the task-by-task match of the role description against the Employee Capability Checklist sought the same day.''',
]
for i,txt in enumerate(SEEK,1):
    s.append(P(f'<b>{i}.</b>&nbsp;&nbsp;{txt}',BL))
s.append(P('6. IF THE DISPUTE REMAINS UNRESOLVED',H2))
s.append(P('If the dispute is not resolved at Stage 2, I reserve my position under clause 1.11.2(c) to refer the matter to the EB12 Implementation Group, and under clause 1.11.2(d) to refer it to the Queensland Industrial Relations Commission.',B))
s.append(P('Everything I have applied for remains on the basis set out at paragraph 4 of my application of 31 August 2026 — under protest and subject to re-credit. I remain certified fit with restrictions and available to work.',B))
s.append(P('This notice concerns my employment only. My appeal in the Queensland Industrial Relations Commission is a separate proceeding and nothing in this notice forms part of it.',B))
s.append(Spacer(1,6))
s.append(P('<b>Attached, and forming part of this notice:</b> "The employment record — analysis, complete chronology and original documents". It sets out what the record shows, a chronology of every communication event on this matter from February to 3 September 2026, and behind it, in fifty-one tabs, the original documents themselves — the movement forms, the Employee Capability Checklist, the Request for Medical Information and its attachments, the Stage 1 notice and its acknowledgement, the pay advice, the payroll and leave records, and the whole of the correspondence. Nothing in it has been retyped.',B))
s.append(Spacer(1,8))
s.append(P('Cory Shepherd',B))
s.append(P('Employee number 388372 · 0417 400 227 · coryshepherd1@hotmail.com',SM))

buf=io.BytesIO()
doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=16*mm,bottomMargin=15*mm,title='',author='')
doc.build(s); buf.seek(0)
out=pikepdf.open(buf)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r2=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r2: del r2[k]
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/NOTICE_OF_DISPUTE_STAGE2_to_CE_3SEP2026.pdf',fix_metadata_version=False)
print('dispute notice pages',len(out.pages))
