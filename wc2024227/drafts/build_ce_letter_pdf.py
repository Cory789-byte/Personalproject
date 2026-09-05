import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph as P, Spacer, Table,
                                TableStyle, KeepTogether)
from xml.sax.saxutils import escape as esc

BODY = PS('b', fontName='Helvetica', fontSize=10.2, leading=14.4, alignment=TA_JUSTIFY,
          spaceAfter=7)
HEAD = PS('h', fontName='Helvetica-Bold', fontSize=10.2, leading=13, spaceBefore=13,
          spaceAfter=5)
SUB  = PS('s', fontName='Helvetica', fontSize=10.2, leading=14.4, alignment=TA_JUSTIFY,
          leftIndent=11*mm, spaceAfter=7)
SUBH = PS('sh', fontName='Helvetica', fontSize=10.2, leading=14.4, alignment=TA_JUSTIFY,
          leftIndent=11*mm, firstLineIndent=-5*mm, spaceAfter=7)
META = PS('m', fontName='Helvetica', fontSize=9.2, leading=12.4)
METB = PS('mb',fontName='Helvetica-Bold', fontSize=9.2, leading=12.4)
SUBJ = PS('sj',fontName='Helvetica-Bold', fontSize=10.2, leading=13.6, spaceBefore=8, spaceAfter=10)
SMALL= PS('sm',fontName='Helvetica', fontSize=8.9, leading=11.6)

def para(t, st=BODY): return P(t, st)

REQUESTS = [
 ('3 July 2026, 3:18 pm','that the balance be processed as annual leave rather than sick leave without pay'),
 ('10 July 2026, 8:35 am','that the shifts be treated as paid time and not deducted from my leave, and that my return be facilitated — unanswered'),
 ('13 July 2026, 4:39 pm','the same request again; the basis in writing if refused; interim duties offered'),
 ('22 July 2026','Payroll Enquiry 4438861 lodged'),
 ('28 July 2026, 5:39 pm','special leave on full pay applied for'),
 ('30 July 2026, 11:25 am','that the shifts from 3 July be processed by ad hoc payment and the leave re-credited'),
 ('3 August 2026, 11:38 am','Stage 1 notice of dispute under EB12 cl 1.11, covering leave and pay'),
 ('5 August 2026, 7:30 am','that my recreation leave not be applied, and that the period be coded as special leave on full pay'),
 ('31 August 2026, 10:59 am','formal application for long service leave on full pay from 13 July 2026, with annual leave on its exhaustion'),
 ('2 September 2026, 11:07 am','ad hoc payment requested to be processed that day'),
 ('3 September 2026, 1:30 pm','the coding applied since 3 July, and payment under HR Policy C13'),
 ('3 September 2026, 2:04 pm','who within Payroll had authority to action an ad hoc payment that day'),
]

def reqtable():
    rows=[[P('<b>'+esc(d)+'</b>',SMALL), P(esc(w),SMALL)] for d,w in REQUESTS]
    t=Table(rows, colWidths=[44*mm, 116*mm])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),4),
        ('TOPPADDING',(0,0),(-1,-1),2.2),('BOTTOMPADDING',(0,0),(-1,-1),2.2),
        ('LINEBELOW',(0,0),(-1,-2),0.25,colors.HexColor('#dddddd')),
    ]))
    return t

def hdr(c, d):
    c.saveState()
    c.setFont('Helvetica',8); c.setFillColor(colors.HexColor('#666666'))
    c.drawString(25*mm, 12*mm, 'Cory Shepherd · employee number 388372 · MSH-INJ-5795')
    c.drawRightString(185*mm, 12*mm, 'Page %d' % c.getPageNumber())
    c.restoreState()

def build(flow, out):
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf, pagesize=A4, leftMargin=25*mm, rightMargin=25*mm,
                          topMargin=20*mm, bottomMargin=20*mm, title='', author='')
    doc.build(flow, onFirstPage=hdr, onLaterPages=hdr)
    buf.seek(0)
    src=pikepdf.open(buf); pdf=pikepdf.new(); pdf.pages.extend(src.pages)
    with pdf.open_metadata() as md:
        for x in list(md): del md[x]
    for x in list(pdf.docinfo.keys()): del pdf.docinfo[x]
    for x in ('/Metadata','/PieceInfo','/Lang'):
        if x in pdf.Root: del pdf.Root[x]
    for pg in pdf.pages:
        for x in ('/Metadata','/PieceInfo'):
            if x in pg.obj: del pg.obj[x]
    pdf.save(out, fix_metadata_version=False)
    return len(pdf.pages)

# ─────────────────────────────────── THE LETTER ───────────────────────────────────
f=[]
f.append(P('Cory Shepherd', METB))
f.append(P('Employee number 388372<br/>0417 400 227<br/>coryshepherd1@hotmail.com', META))
f.append(Spacer(1,9))
f.append(P('5 September 2026', META))
f.append(Spacer(1,9))
f.append(P('Ms Noelle Cridland<br/>Chief Executive<br/>Metro South Hospital and Health Service', META))
f.append(Spacer(1,4))
f.append(P('By email. Copy to Ms Jacqui Roberts and Ms Michelle Harrison, Injury Management '
           'Consultant, Logan and Beaudesert Health Service.', SMALL))
f.append(P('Determination of my application for special leave on full pay, and related matters '
           '&#8212; MSH-INJ-5795', SUBJ))
f.append(P('Dear Ms Cridland,', BODY))
f.append(para('I write to you because my application for special leave on full pay, made on '
  '28 July 2026 and renewed on 5 August 2026, has not been determined, and because clause 6.1 of '
  'Directive 12/24 places the power to approve such leave with the chief executive. The other '
  'matters below bear on that decision, and one of them concerns a Deed of Settlement to which you '
  'and I are the parties.'))

f.append(P('1.&#160;&#160;THE POSITION', HEAD))
f.append(para('I am absent from the workplace at the Health Service&#8217;s direction. I have held '
  'an Employee Capability Checklist since 3 July 2026 certifying me fit for my role with '
  'restrictions, and I have remained available to work under the arrangement the Health Service '
  'itself approved on 9 June 2026. The Health Service has said it requires clarification of my '
  'medical position. It has held my signed authority to obtain that clarification directly from my '
  'treating psychiatrist since 24 August 2026. My psychiatrist put four questions to Injury '
  'Management on 19 August 2026, and confirmed to me on 5 September 2026 that he is still waiting '
  'for a response before he provides the report.'))
f.append(para('I have received no wages for work since 13 July 2026. Throughout that period I have '
  'funded the absence myself. My paid sick leave was exhausted, then my recreation leave, then half '
  'pay, and the absence has since been recorded as leave without pay.'))
f.append(para('A payment was made to me on 4 September 2026. It followed a series of requests, each '
  'of which is documented:'))
f.append(reqtable()); f.append(Spacer(1,9))
f.append(para('The payment made on 4 September 2026 was of my own leave entitlements. It was not '
  'wages. I am now told that I must wait until 29 September 2026 to fund the absence from seven '
  'years of service.'))
f.append(para('I do not accept that I should be funding this absence at all. Every application I '
  'have made for leave has been made under protest and subject to re-credit, and this letter is '
  'written on the same basis.'))

f.append(P('2.&#160;&#160;THE MEDICAL INFORMATION', HEAD))
f.append(para('On 13 August 2026 Dr Krishnaiah wrote to Injury Management. Ms Harrison replied the '
  'same afternoon, acknowledged that I had given permission, and wrote: &#8220;Happy to provide you '
  'with this information and to assist you with this.&#8221; She recorded the reason for the '
  'request as being that I &#8220;had requested a reduction in hours and advised this request was '
  'due to medical reasons&#8221;.'))
f.append(para('On 19 August 2026 Dr Krishnaiah put four questions to Injury Management. He asked on '
  'what basis my earlier reductions in hours were accepted without medical certification; what has '
  'changed in the administrative position that warrants an in-depth psychiatric assessment; what '
  'the policy is on disclosure of sensitive mental health information and the grounds for it; and '
  'what concerns or risks observed or reported at the workplace warrant disclosure. He wrote that '
  'this &#8220;will help before I undertake detailed assessment to provide my professional '
  'opinion&#8221;.'))
f.append(para('Those questions have not been answered. The correspondence is enclosed.'))
f.append(para('I am not asking the Health Service to answer to me. I am asking that it answer the '
  'clinician, so that the report it says it requires can be produced.'))

f.append(P('3.&#160;&#160;THE APPLICATION FOR SPECIAL LEAVE, WHICH REMAINS UNDETERMINED', HEAD))
f.append(para('I applied for special leave on full pay on 28 July 2026, and again on 5 August 2026. '
  'Neither application has been determined. I ask that you determine it.'))
f.append(para('Clause 9.12.1 of EB12 provides that Directive 12/24: Special Leave applies to all '
  'employees covered by the Agreement. Clause 6.1 of that Directive provides that &#8220;a chief '
  'executive may approve paid leave for employees for any purpose, with duration appropriate to the '
  'purpose of the leave&#8221;, and clause 6.1(a) provides that leave may exceed five working days '
  'per year per reason &#8220;where the chief executive considers that circumstances warrant the '
  'granting of additional paid leave&#8221;, such leave being &#8220;reasonable and proportionate '
  'to the circumstances&#8221;.'))
f.append(para('Clause 6.5 requires that in determining an application under clause 6.1 a chief '
  'executive must consider the reason the leave is requested, its duration, and the impact on the '
  'employee if it is not approved. On each of those:'))
f.append(P('<b>The reason.</b> I am absent from the workplace at the direction of the Health '
  'Service, pending medical information the Health Service has sought and has not yet obtained. I '
  'am certified fit for my role with restrictions and I have remained available to work.', SUB))
f.append(P('<b>The duration.</b> I ask for a period ending on the earlier of the conclusion of the '
  'medical process or the date my long service leave becomes available. The request is bounded, and '
  'one of the two end points is within the Health Service&#8217;s own control.', SUB))
f.append(P('<b>The impact if it is not approved.</b> I have had no wages for work since 13 July '
  '2026, and I have lost my housing. Beyond that, since 3 July 2026 I have made two applications '
  'for special leave, an application for long service leave and a Stage 1 dispute notification, and '
  'I have corresponded separately with my line manager, Payroll Services, Injury Management and '
  'Human Resources on each of them. Each has required me to identify the instrument, make the '
  'application, follow it up and, in most cases, follow it up again. The Stage 1 notification '
  'lapsed without outcome. On 28 August 2026 I withdrew the Stage 2 referral, so that these matters '
  'could be worked through collaboratively, expressly reserving the questions of pay, the leave '
  'debited since 3 July 2026 and the adjustments identified in the Employee Capability Checklist as '
  'unresolved and in dispute. I have not renewed that referral. I have done all of this without '
  'income, and while certified fit and available to work. I ask that the burden of conducting these '
  'matters at arm&#8217;s length, over this period and in these circumstances, be weighed as part '
  'of the impact under clause 6.5(d).', SUB))
f.append(para('I ask that this application be determined whichever course is taken under paragraph '
  '4 below. Even if Dr Krishnaiah&#8217;s questions were answered today, his report, its '
  'consideration and any return to work would take further time, and I have no income during that '
  'time. The determination of the special leave application does not depend on the medical process '
  'concluding; it is what makes the medical process survivable.'))
f.append(para('If the power under clause 6.1 has been delegated, could you please tell me to whom, '
  'and by when the application will be determined. In the five weeks since it was made, no '
  'decision-maker has been identified to me.'))
f.append(para('If the application is refused, I ask for the decision and the reasons in writing.'))

f.append(P('4.&#160;&#160;WHAT WOULD BRING THE ABSENCE TO AN END', HEAD))
f.append(para('Separately, and in addition, I ask that you decide one of the following and tell me '
  'which:'))
f.append(P('(a)&#160;&#160;&#160;that Dr Krishnaiah&#8217;s questions of 19 August 2026 be '
  'answered, so that the report the Health Service says it requires can be produced; or', SUBH))
f.append(P('(b)&#160;&#160;&#160;that I return to work under the arrangement approved on 9 June '
  '2026.', SUBH))
f.append(para('Either would end the absence. Neither, by itself, addresses the period already '
  'elapsed or the period until a return takes effect, which is what paragraph 3 concerns.'))

f.append(P('5.&#160;&#160;LONG SERVICE LEAVE', HEAD))
f.append(para('This is a separate matter, and I put it differently, because it is an entitlement '
  'rather than a request.'))
f.append(para('Clause 22(c) of the Hospital and Health Service General Employees (Queensland '
  'Health) Award &#8211; State 2015 provides that &#8220;employees who have completed 7 '
  'years&#8217; continuous service are entitled to take long service leave on full pay or half '
  'pay&#8221;. Clause 8.1 of Directive 10/24 provides that &#8220;employees are entitled to take '
  'pro rata long service leave after 7 years continuous service&#8221;. Section 1 of HR Policy C38 '
  'is to the same effect.'))
f.append(para('Recital B of the Deed records that my employment commenced on 25 March 2019. Seven '
  'years of continuous service therefore fell on 25 March 2026.'))
f.append(para('On 3 September 2026 Payroll advised an eligibility date of 4 September 2026. On '
  '4 September 2026 I was advised of 29 September 2026. The difference between 25 March 2026 and '
  '29 September 2026 is 188 days, and it is made up of three periods recorded as leave without pay '
  '&#8212; 8 May to 19 June 2022, 21 June to 20 September 2024, and 13 December 2024 to '
  '23 February 2025.'))
f.append(para('Could you please:'))
f.append(P('1.&#160;&#160;&#160;identify the provision under which periods of approved leave '
  'without pay are excluded from continuous service for long service leave purposes. I have read '
  'the <i>Industrial Relations Act 2016</i>, the Award, EB12, HR Policy C38 and Directive 10/24, '
  'and I have not been able to identify it;', SUBH))
f.append(P('2.&#160;&#160;&#160;tell me on what basis access at seven years is refused; and', SUBH))
f.append(P('3.&#160;&#160;&#160;determine my application of 31 August 2026. Clause 7.4 of Directive '
  '10/24 requires the employer to respond to a request to take long service leave in a timely '
  'manner, indicating whether the leave applied for has been approved or not.', SUBH))
f.append(para('I ask questions 1 and 2 while maintaining that I should not be funding this absence '
  'from my own entitlements at all. The two matters are separate: whether the eligibility date is '
  'correct, and whether I should be required to reach it.'))
f.append(para('The calculation appears to have been made by reference to leave codes alone. It does '
  'not appear to take account of the Deed, under which I was reinstated with an effective date of '
  '20 September 2024, and by which the Health Service reserved the matters of my absence rather '
  'than determining them. I ask that the calculation be reviewed with the Deed before the reviewer.'))

f.append(P('6.&#160;&#160;THE DEED', HEAD))
f.append(para('Clause 6 of the Deed reserved to the Health Service the right to deal with the '
  'outstanding matters of my absence. Clause 7 reserves my rights in relation to any future '
  'management action taken pursuant to clause 6.'))
f.append(para('Could you please tell me whether the process commenced on 3 July 2026 is management '
  'action under clause 6 of the Deed.'))

f.append(P('7.&#160;&#160;ENCLOSURES', HEAD))
for n,txt in [('1','Dr Krishnaiah&#8217;s email of 27 August 2026, forwarding his correspondence '
   'with Injury Management of 13 and 19 August 2026 (9 pages)'),
  ('2','Limited Scope Authorisation for Disclosure of Medical Information, signed 24 August 2026'),
  ('3','Dr Krishnaiah&#8217;s email of 5 September 2026'),
  ('4','Schedule of the provisions relied on (one page). I have not enclosed the instruments '
       'themselves, which the Health Service holds.')]:
    f.append(P(n+'.&#160;&#160;&#160;'+txt, SUBH))
f.append(Spacer(1,4))
f.append(para('I remain certified fit for my role with restrictions, and available to work. I would '
  'be grateful for a decision.'))
f.append(Spacer(1,14))
f.append(P('Kind regards', BODY))
f.append(Spacer(1,20))
f.append(P('<b>Cory Shepherd</b>', META))
f.append(P('Employee number 388372', META))

n=build(f, 'out/LETTER_TO_CHIEF_EXECUTIVE_5SEP2026.pdf')
print('letter pages:', n)
