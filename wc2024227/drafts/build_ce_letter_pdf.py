import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle)

TITLE = PS('t', fontName='Helvetica-Bold', fontSize=15, leading=18.5, spaceAfter=3)
SUBT  = PS('st',fontName='Helvetica', fontSize=10, leading=13, spaceAfter=10,
           textColor=colors.HexColor('#555555'))
BLK   = PS('bk',fontName='Helvetica', fontSize=9.2, leading=12.4)
HEAD  = PS('h', fontName='Helvetica-Bold', fontSize=10.4, leading=13, spaceBefore=14, spaceAfter=5)
BODY  = PS('b', fontName='Helvetica', fontSize=9.7, leading=13.4, alignment=TA_JUSTIFY, spaceAfter=7)
SUBH  = PS('sh',fontName='Helvetica', fontSize=9.7, leading=13.4, alignment=TA_JUSTIFY,
           leftIndent=9*mm, firstLineIndent=-5.5*mm, spaceAfter=6)
SMALL = PS('sm',fontName='Helvetica', fontSize=8.6, leading=11.4)
FOOT_T='Cory Lea Shepherd · MSH-INJ-5795 · Determination of my application for special leave'

def rule(w=160*mm, c='#333333', h=0.7):
    t=Table([['']], colWidths=[w], rowHeights=[h])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(c))])); return t

def foot(c, d):
    c.saveState(); c.setFont('Helvetica',7.6); c.setFillColor(colors.HexColor('#777777'))
    c.setStrokeColor(colors.HexColor('#cccccc')); c.setLineWidth(0.4)
    c.line(25*mm, 15*mm, 185*mm, 15*mm)
    c.drawString(25*mm, 11*mm, FOOT_T)
    c.drawRightString(185*mm, 11*mm, 'Page %d' % c.getPageNumber())
    c.restoreState()

def build(flow, out, foot_fn=foot):
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf, pagesize=A4, leftMargin=25*mm, rightMargin=25*mm,
                          topMargin=20*mm, bottomMargin=22*mm, title='', author='')
    doc.build(flow, onFirstPage=foot_fn, onLaterPages=foot_fn)
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

REQ=[('3 Jul 2026, 3:18 pm','that the balance be processed as annual leave rather than sick leave without pay'),
 ('10 Jul 2026, 8:35 am','that the shifts be treated as paid time and not deducted from my leave — unanswered'),
 ('13 Jul 2026, 4:39 pm','the same request again; the basis in writing if refused; interim duties offered'),
 ('22 Jul 2026','Payroll Enquiry 4438861 lodged'),
 ('28 Jul 2026, 5:39 pm','special leave on full pay applied for'),
 ('30 Jul 2026, 11:25 am','that the shifts from 3 July be paid by ad hoc payment and the leave re-credited'),
 ('3 Aug 2026, 11:38 am','Stage 1 notice of dispute under EB12 cl 1.11, covering leave and pay'),
 ('5 Aug 2026, 7:30 am','that my recreation leave not be applied; the period coded as special leave on full pay'),
 ('31 Aug 2026, 10:59 am','formal application for long service leave on full pay from 13 July 2026'),
 ('2 Sep 2026, 11:07 am','ad hoc payment requested to be processed that day'),
 ('3 Sep 2026, 1:30 pm','the coding applied since 3 July, and payment under HR Policy C13'),
 ('3 Sep 2026, 2:04 pm','who within Payroll had authority to action an ad hoc payment that day')]

def reqtable():
    rows=[[P('<b>'+d+'</b>',SMALL),P(w,SMALL)] for d,w in REQ]
    t=Table(rows,colWidths=[38*mm,122*mm])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
      ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),3),
      ('TOPPADDING',(0,0),(-1,-1),1.8),('BOTTOMPADDING',(0,0),(-1,-1),1.8),
      ('LINEBELOW',(0,0),(-1,-2),0.25,colors.HexColor('#dddddd'))]))
    return t


if __name__=='__main__':
    f=[P('Determination of my application for special leave on full pay', TITLE),
       P('Directive 12/24 clause 6.1 &#183; long service leave &#183; the Deed of 21 February 2025', SUBT),
       P('Cory Lea Shepherd', BLK),
       P('AO3, Switchboard Services, Logan Hospital, Metro South Health', BLK),
       P('Employee number 388372 &#183; Employee reference MSH-INJ-5795', BLK),
       P('To:&#160;&#160;&#160;&#160;&#160;Ms Noelle Cridland, Chief Executive, Metro South Health', BLK),
       P('Copy: Ms Jacqui Roberts', BLK),
       P('Date:&#160;&#160;5 September 2026', BLK),
       Spacer(1,7), rule(), Spacer(1,4)]

    f+=[P('1. WHAT I AM ASKING', HEAD),
     P('I ask that you determine my application for special leave on full pay. It was made on 28 July '
       '2026 and renewed on 5 August 2026, and it has not been determined. Clause 6.1 of Directive '
       '12/24 places the power to approve such leave with the chief executive.', BODY),
     P('Separately, I ask that you decide either that Dr Krishnaiah&#8217;s questions of 19 August 2026 '
       'be answered, or that I return to work under the arrangement approved on 9 June 2026. Either '
       'would end the absence. Neither addresses the period already elapsed, which is what the '
       'application concerns.', BODY),
     P('I also ask three questions about my long service leave eligibility date, and one about clause 6 '
       'of the Deed.', BODY),
     P('I make no allegation against any individual, and I ask for no finding to be made about anyone.',
       BODY)]

    f+=[P('2. THE POSITION', HEAD),
     P('I am absent from the workplace at the Health Service&#8217;s direction. I have held an Employee '
       'Capability Checklist since 3 July 2026 certifying me fit for my role with restrictions, and I '
       'have remained available to work under the arrangement the Health Service itself approved on '
       '9 June 2026.', BODY),
     P('I have received no wages for work since 13 July 2026. I have funded the absence myself: paid '
       'sick leave exhausted, then recreation leave, then half pay, and since then leave without pay. '
       'I have lost my housing.', BODY),
     P('A payment was made to me on 4 September 2026. It followed these requests:', BODY),
     reqtable(), Spacer(1,8),
     P('That payment was of my own leave entitlements. It was not wages. I am now told I must wait '
       'until 29 September 2026 to fund the absence from seven years of service.', BODY),
     P('I do not accept that I should be funding this absence at all. Every application I have made has '
       'been made under protest and subject to re-credit, and this letter is written on the same basis.',
       BODY)]

    f+=[P('3. THE MEDICAL INFORMATION', HEAD),
     P('The Health Service has said it requires clarification of my medical position. It has held my '
       'signed authority to obtain that clarification directly from my treating psychiatrist since '
       '24 August 2026.', BODY),
     P('On 13 August 2026 Dr Krishnaiah wrote to Injury Management. Ms Harrison replied the same '
       'afternoon, acknowledged that I had given permission, and wrote: &#8220;Happy to provide you '
       'with this information and to assist you with this.&#8221; She recorded the reason for the '
       'request as being that I &#8220;had requested a reduction in hours and advised this request was '
       'due to medical reasons&#8221;.', BODY),
     P('On 19 August 2026 Dr Krishnaiah put four questions to Injury Management: on what basis my '
       'earlier reductions in hours were accepted without medical certification; what has changed in '
       'the administrative position that warrants an in-depth psychiatric assessment; what the policy '
       'is on disclosure of sensitive mental health information and the grounds for it; and what '
       'concerns or risks observed or reported at the workplace warrant disclosure. He wrote that this '
       '&#8220;will help before I undertake detailed assessment to provide my professional '
       'opinion&#8221;. He confirmed to me on 5 September 2026 that he is still waiting.', BODY),
     P('I am not asking the Health Service to answer to me. I am asking that it answer the clinician, '
       'so that the report it says it requires can be produced.', BODY)]

    f+=[P('4. THE APPLICATION FOR SPECIAL LEAVE', HEAD),
     P('Clause 9.12.1 of EB12 applies Directive 12/24. Clause 6.1 permits a chief executive to approve '
       'paid leave &#8220;for any purpose, with duration appropriate to the purpose&#8221;, and clause '
       '6.1(a) permits more than five days per reason &#8220;where the chief executive considers that '
       'circumstances warrant&#8221;. Clause 6.5 requires the reason, the duration and the impact of '
       'refusal to be considered. On each:', BODY),
     P('(a)&#160;&#160;&#160;<b>The reason.</b> I am absent at the direction of the Health Service, '
       'pending medical information it has sought and not yet obtained, while certified fit with '
       'restrictions and available to work.', SUBH),
     P('(b)&#160;&#160;&#160;<b>The duration.</b> A period ending on the earlier of the conclusion of '
       'the medical process or the date my long service leave becomes available. The request is '
       'bounded, and one of the two end points is within the Health Service&#8217;s own control.', SUBH),
     P('(c)&#160;&#160;&#160;<b>The impact if refused.</b> No wages for work since 13 July 2026, and my '
       'housing lost. Since 3 July I have made two special leave applications, a long service leave '
       'application and a Stage 1 notice, and corresponded separately with my line manager, Payroll '
       'Services, Injury Management and Human Resources on each. The Stage 1 notice lapsed without '
       'outcome. On 28 August 2026 I withdrew the Stage 2 referral so these matters could be worked '
       'through collaboratively, reserving pay, the leave debited since 3 July and the Checklist '
       'adjustments as unresolved and in dispute. I have not renewed it.', SUBH),
     P('I ask that the application be determined whichever course is taken. Even if Dr '
       'Krishnaiah&#8217;s questions were answered today, the report, its consideration and any return '
       'would take further time, and I have no income during it.', BODY),
     P('If the power under clause 6.1 has been delegated, could you please tell me to whom and by when '
       'the application will be determined. In the five weeks since it was made, no decision-maker has '
       'been identified to me. If it is refused, I ask for the decision and reasons in writing.', BODY)]

    f+=[P('5. LONG SERVICE LEAVE', HEAD),
     P('I put this differently, because it is an entitlement rather than a request. Clause 22(c) of the '
       'Award provides that employees who have completed seven years&#8217; continuous service '
       '&#8220;are entitled to take long service leave on full pay or half pay&#8221;. Clause 8.1 of '
       'Directive 10/24 and section 1 of HR Policy C38 are to the same effect. Recital B of the Deed '
       'records that my employment commenced on 25 March 2019, so seven years fell on 25 March 2026.',
       BODY),
     P('On 3 September 2026 Payroll advised an eligibility date of 4 September 2026. On 4 September I '
       'was advised of 29 September 2026. The difference from 25 March 2026 is 188 days, made up of '
       'three periods recorded as leave without pay &#8212; 8 May to 19 June 2022, 21 June to '
       '20 September 2024, and 13 December 2024 to 23 February 2025. Could you please:', BODY),
     P('(a)&#160;&#160;&#160;identify the provision under which periods of approved leave without pay '
       'are excluded from continuous service. I have read the <i>Industrial Relations Act 2016</i>, the '
       'Award, EB12, HR Policy C38 and Directive 10/24, and I have not been able to identify it;', SUBH),
     P('(b)&#160;&#160;&#160;tell me on what basis access at seven years is refused; and', SUBH),
     P('(c)&#160;&#160;&#160;determine my application of 31 August 2026. Clause 7.4 of Directive 10/24 '
       'requires a timely response indicating whether the leave is approved or not.', SUBH),
     P('The calculation appears to have been made by reference to leave codes alone. It does not appear '
       'to take account of the Deed, under which I was reinstated with an effective date of '
       '20 September 2024 and by which the Health Service reserved the matters of my absence rather '
       'than determining them. I ask that it be reviewed with the Deed before the reviewer. I ask '
       'questions (a) and (b) while maintaining that I should not be funding this absence at all.',
       BODY)]

    f+=[P('6. THE DEED', HEAD),
     P('Clause 6 reserved to the Health Service the right to deal with the outstanding matters of my '
       'absence, and clause 7 reserves my rights in relation to any future management action taken '
       'pursuant to clause 6. Could you please tell me whether the process commenced on 3 July 2026 is '
       'management action under clause 6.', BODY)]

    f+=[P('7. ENCLOSURES', HEAD)]
    for n,t in [('1','Dr Krishnaiah&#8217;s email of 27 August 2026, forwarding his correspondence with '
       'Injury Management of 13 and 19 August 2026 (9 pages)'),
      ('2','Limited Scope Authorisation for Disclosure of Medical Information, signed 24 August 2026'),
      ('3','Dr Krishnaiah&#8217;s email of 5 September 2026'),
      ('4','Schedule of the provisions relied on. The instruments themselves are not enclosed, as the '
           'Health Service holds them.')]:
        f.append(P(n+'.&#160;&#160;&#160;'+t, SUBH))
    f.append(Spacer(1,6))
    f.append(P('I remain certified fit for my role with restrictions, and available to work. I would be '
               'grateful for a decision.', BODY))

    print('letter pages:', build(f,'out/LETTER_TO_CHIEF_EXECUTIVE_5SEP2026.pdf'))
