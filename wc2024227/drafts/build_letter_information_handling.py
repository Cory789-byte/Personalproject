# -*- coding: utf-8 -*-
import os, re, html, datetime, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer

OUT = 'out/LETTER_Information_Handling_and_Authorities_11SEP2026.pdf'
AUTHOR = 'Cory Shepherd'
TITLE  = 'Handling of personal, health and public interest disclosure information'

NAME  = ParagraphStyle('N', fontName='Times-Bold', fontSize=12.5, leading=15, spaceAfter=1)
ADDR  = ParagraphStyle('A', fontName='Times-Roman', fontSize=8.8, leading=11.6,
                       textColor=colors.HexColor('#444444'), spaceAfter=10)
TO    = ParagraphStyle('T', fontName='Times-Roman', fontSize=10, leading=13, spaceAfter=1)
DATE  = ParagraphStyle('D', fontName='Times-Roman', fontSize=10, leading=13, spaceBefore=8, spaceAfter=8)
SUBJ  = ParagraphStyle('S', fontName='Times-Bold', fontSize=10, leading=13.5, spaceAfter=9)
BODY  = ParagraphStyle('B', fontName='Times-Roman', fontSize=10, leading=14.2, spaceAfter=7, alignment=4)
BULL  = ParagraphStyle('U', parent=BODY, leftIndent=11, bulletIndent=2, spaceAfter=5)
HEAD  = ParagraphStyle('H', fontName='Times-Bold', fontSize=10.4, leading=14,
                       spaceBefore=13, spaceAfter=6)
SIGN  = ParagraphStyle('G', fontName='Times-Roman', fontSize=10, leading=13.6, spaceAfter=0)

def furniture(c, d):
    c.saveState(); c.setFont('Times-Roman', 7.5); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-25*mm, 13*mm, 'Page %d' % c.getPageNumber()); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=25*mm, rightMargin=25*mm,
                      topMargin=20*mm, bottomMargin=20*mm)
doc.addPageTemplates([PageTemplate('n', [Frame(25*mm, 20*mm, A4[0]-50*mm, A4[1]-40*mm, id='f')],
                                   onPage=furniture)])

P  = lambda t: Paragraph(t, BODY)
B  = lambda t: Paragraph(t, BULL, bulletText='–')
H  = lambda t: Paragraph(t, HEAD)

S = [Paragraph('CORY SHEPHERD', NAME),
     Paragraph('Administration Officer, Switchboard Services, Logan Hospital &nbsp;|&nbsp; '
               'Employee no. 388372<br/>coryshepherd1@hotmail.com &nbsp;|&nbsp; 0417 400 227', ADDR),
     Paragraph('Injury Management, and Human Resources', TO),
     Paragraph('Logan and Beaudesert Health Service', TO),
     Paragraph('Metro South Hospital and Health Service', TO),
     Paragraph('Dated 11 September 2026', DATE),
     Paragraph('Handling of my personal, health and public interest disclosure information, '
               'and the authorities relied upon &nbsp;&ndash;&nbsp; MSH-INJ-5795', SUBJ),
     P('Dear Jacqui, Injury Management and HR,'),
     P('This letter is separate from my email yesterday on long service leave coding and Dr Krishnaiah. '
       'It deals only with how my personal, health and public interest disclosure information has been '
       'handled, and with the authorities Metro South Health has treated as giving it standing to do so. '
       'It does not ask anyone to decide the matters in that other email, and nothing here should delay them.'),
     P('The concern is not any single email. It is the handling of my personal and health information: '
       'who it is distributed to, on what authority, and whether anything has changed after it was raised.'),
     B('In May 2024 the matters I had raised were referred to human resources, and human resources advice '
       'was obtained and acted on.'),
     B('On 3 August 2026 I wrote to the Chief Executive about conflict of interest and information handling. '
       'Metro South Executive Services acknowledged that letter the same day. It has not been answered in substance.'),
     B('On 13 July 2026 my Employee Capability Checklist, which records my medical restrictions, was sent to '
       'an external insurer and to Solv. On 13 August 2026 a statement about my claim and my income, with a '
       'screenshot of my leave balances, was sent to a group human resources list.'),
     P('The same handling has recurred after it was raised. I am notifying Metro South Health of those events '
       'and of what followed. I ask that the Service communicate with the appropriate officer, confine the '
       'people and the lists being used, respect its own privacy policies, procedures and practices, and, if '
       'any of my information or disclosures is to be shared, act in accordance with the '
       '<i>Information Privacy Act 2009</i>, Queensland Health privacy policy and section 65 of the '
       '<i>Public Interest Disclosure Act 2010</i>.'),
     P('I ask for written confirmation of the matters in part E by Friday 18 September 2026.'),
     P('For a reader coming to this without the history: I am an Administration Officer at Logan Hospital '
       'Switchboard, employee number 388372. I sustained a psychological injury in June 2024. Since 3 July 2026 '
       'I have been certified fit for duties with restrictions, I have been available, and Metro South Health '
       'has not provided me with work.'),

     H('A. &nbsp;The authorities relied on do not reach what has been done'),
     P('There are three different instruments. They are not one open licence.'),
     Paragraph('<b>1. &nbsp;The QSuper income protection application declaration</b>', BODY),
     P('On 15 July 2026 Michelle Harrison wrote that I had signed the declaration and authorisation on page 7 '
       'of the Income Protection Application, and that this permits QSuper to request relevant information '
       'from the employer in relation to the claim.'),
     P('That instrument is the fund&rsquo;s authorisation. It authorises the fund and the insurer to collect '
       'information from the employer to assess and manage the income protection claim. It is not an '
       'authorisation given to Metro South Health. The published process is that the fund requests Part B. '
       'For Queensland Government employees the member is not required to hand Part B to HR.'),
     P('It does not authorise Metro South Health to send health information to Australian Retirement Trust '
       'after I had advised that the claim was not in payment; to copy Solv; to attach my Employee Capability '
       'Checklist to a claims email; to tell a group list that I have a current open QSuper claim and that my '
       'income may be reported to the fund; or to treat that signature as a reason to withhold wages or refuse '
       'interim duties.'),
     P('Employer wage obligations sit in the Award, the Agreement and the leave directives. They are not '
       'displaced by a fund-facing collection consent.'),
     Paragraph('<b>2. &nbsp;The August medical authorities</b>', BODY),
     P('On 12 August 2026 I gave Injury Management written consent so Mind and Memory Service could confirm '
       'Dr Krishnaiah&rsquo;s two requirements for the 31 July Request for Medical Information (MSH-INJ-5795).'),
     P('On 24 August 2026 at 11:13 am I sent you, Jacqui, my agreement to the sharing of medical information '
       'with my treating psychiatrist. I required prior notice of what would be shared and what questions '
       'would be asked. You acknowledged that email at 12:19 pm.'),
     P('Those authorities were for contact with Dr Krishnaiah about the RFMI. They did not exist on 13 July. '
       'They cannot be applied backwards. They do not authorise contact with Australian Retirement Trust, '
       'Solv or a group HR list.'),
     P('The one authority I have given has not been acted on. Dr Krishnaiah has recorded that he contacted '
       'Logan Hospital and that Queensland Health did not respond. I told LBH HR that on 28 August 2026 and '
       'wrote again to Injury Management on 4 September 2026. I still have no written confirmation that any '
       'request has been sent to him, what it contained, or when. The authorities Metro South Health did not '
       'have were acted on within hours. The authority it did have, given for a single purpose and on a '
       'condition of prior notice, remains unused.'),
     Paragraph('<b>3. &nbsp;My public interest disclosure &mdash; file 24-ESU-1130</b>', BODY),
     P('On 13 May 2024 I made a complaint to the Metro South Health Ethical Standards Unit. The Ethical '
       'Standards Unit determined on 24 December 2024 that it constituted a public interest disclosure, and '
       'the determination bears reference PID 24-ESU-1130.'),
     P('On 15 May 2024 at 3:35 pm I sent LBH HR my email to the Ethical Standards Unit and to CO Complaints. '
       'I have never been told what was then done with it: to whom within Metro South Health it was sent, when, '
       'in what form, or whether the complaint form itself was attached and forwarded.'),
     P('I was not asked, and I was not informed.'),
     P('There is no authority from me that permits Injury Management or LBH HR to circulate that disclosure, '
       'the determination, or the outcome as operational material. Section 65 of the '
       '<i>Public Interest Disclosure Act 2010</i> makes that information confidential by default.'),
     P('The exceptions are narrow. A group HR email is not one of them. I do not set out the content of the '
       'disclosure here. That content is now documented. In the appeal those events are agreed facts. I will '
       'not go over them in this letter, and I am not asking anyone here to revisit them. The point is confined '
       'to how the information has been handled since.'),
     P('I have not added anyone to Metro South Health&rsquo;s distribution list. Anyone who holds material '
       'about that disclosure from an Injury Management or LBH HR email holds it from Metro South Health, '
       'not from me.'),
     P('To the extent any of those instruments is still being treated as current authority for any use beyond '
       'its original purpose, that implied reliance is withdrawn.'),

     H('B. &nbsp;I had already advised the fund. Payroll already reports income. Any overpayment is not a '
       'Queensland Health matter'),
     P('I have been corresponding directly with Australian Retirement Trust and QSuper about claim CLM-317073 '
       'throughout 2026:'),
     B('16 March 2026 &mdash; I emailed ART Life advising that I had returned to work and asking that benefit '
       'payments cease. Australian Retirement Trust acknowledged that email in its letter to me of 4 August 2026.'),
     B('12 April 2026 &mdash; I wrote to Jennifer Chen at ART about the claim.'),
     B('13 April 2026 &mdash; ART lodged a formal complaint on my behalf (cf15866300-446968946). QSuper '
       'acknowledged it the same day.'),
     B('28 May 2026 &mdash; QSuper Resolutions issued the complaint outcome, recording Mr Zappia as claims '
       'manager and that benefits had stopped. I provided that letter to you on 24 August 2026.'),
     B('23 June 2026 &mdash; further claim correspondence from QSuper on CLM-317073.'),
     B('13 July 2026, 3:53 pm &mdash; I told Injury Management the claim was not an active open paying claim. '
       'That was before Ms Harrison emailed Mr Zappia.'),
     B('13 July 2026, 4:56 pm &mdash; I wrote to Injury Management, copied Mr Zappia, and asked what had been '
       'given to the fund, on what dates, and on what authority.'),
     B('28 July, 29 July, 31 July and 12 August 2026 &mdash; I wrote again to Mr Zappia. On 31 July I marked a '
       'forward &ldquo;FYI for the file only &mdash; No ART action requested.&rdquo;'),
     B('4 August 2026 &mdash; Mr Zappia confirmed that ART&rsquo;s review of an overpayment was not complete.'),
     P('Any overpayment is a matter between me and the fund. It arises from the interaction of my voluntary '
       'member contributions and any repayments on the income protection file. Queensland Health is not a party '
       'to that reconciliation. Payroll&rsquo;s only role is the ordinary SuperStream reporting of those both '
       'nominal and voluntary contributions when they are deducted from pay. That function does not give Injury '
       'Management standing to circulate my Employee Capability Checklist, to join the overpayment review, or to '
       'treat the review as a reason to withhold wages.'),
     P('Each paid fortnight, Employer Direct reports employer contributions, standard member contributions and '
       'any voluntary contributions I have arranged, and from 1 July 2026 Single Touch Payroll also reports '
       'qualifying earnings. That reporting has occurred for every date on which Metro South Health has paid me '
       'wages. It does not involve the Employee Capability Checklist.'),
     P('If I am paid, the next contribution file shows it. If I am not paid, the file shows nothing. There is '
       'then no income for Injury Management to advise the fund about.'),
     P('Against that background, Injury Management had no remaining authority to attach my Employee Capability '
       'Checklist to an email to Australian Retirement Trust and Solv.'),

     H('C. &nbsp;Sequence'),
     B('13 July 2026, 3:53 pm &mdash; I corrected the claim status and asked for paid treatment of rostered '
       'time, a prompt Request for Medical Information, and interim duties within the 3 July Employee '
       'Capability Checklist.'),
     B('13 July 2026, 4:20 pm &mdash; Ms Harrison emailed Mr Zappia, copied notes@solv.com.au and me, attached '
       'the Employee Capability Checklist, and recorded that Metro South Health could not facilitate my return.'),
     B('13 July 2026, 4:56 pm &mdash; I asked for the disclosure particulars, still copying Mr Zappia.'),
     B('15 July 2026 &mdash; Injury Management answered, still copying Mr Zappia and Solv, that the 13 July '
       'email was what had been supplied; that conversations had treated me as holding a current claim; and '
       'that because of that claim Metro South Health was not responsible for my pay. Pay and interim duties '
       'were refused.'),
     B('13 August 2026, 4:42 pm &mdash; an email from the LBH Injury Management mailbox, signed in your name, '
       'was sent to me and copied to Emily Petering and LBH HR Team 1. It stated that I had a current open '
       'QSuper claim and that Metro South Health may need to advise QSuper of any income I receive. It attached '
       'a screenshot of leave balances.'),
     B('13 August 2026, 4:45 pm &mdash; the same mailbox issued a recall. A recall is not a correction. The '
       'statement was already on a group list. I still have the original. I have not received a written withdrawal.'),
     B('18 August 2026 &mdash; I again recorded that I have received no income protection payments since '
       '31 May 2026, and that superannuation contributions continue to be reported through payroll in the '
       'ordinary course.'),
     B('24 August 2026, 11:13 am &mdash; I sent you the QSuper letter and the limited agreement for the '
       'psychiatrist. You acknowledged receipt at 12:19 pm.'),

     H('D. &nbsp;What followed'),
     P('Separately from the disclosure, I raised operational concerns about the restrictions placed on the '
       'Switchboard database and about the delays in management actioning updates to it with a then new on-call '
       'feature and restrictions to the department. On Metro South Health&rsquo;s own statements, no safety '
       'assessment, investigation or change of procedure followed any complaint I made about misdirected calls, '
       'emergency codes, directory accuracy or fatigue before 30 June 2024.'),
     P('What the records of that period do contain is correspondence about my conduct. The operational and '
       'human-resources response to the matters I had raised in May 2024 was directed at me, and not at the '
       'restrictions and delays I had raised.'),
     P('The sequence is:'),
     B('13 May 2024 &mdash; I made the complaint to the Ethical Standards Unit.'),
     B('15 May 2024 &mdash; that ESU disclosure, concerning among other things delay in patient care, was '
       'distributed to a group list.'),
     B('16 May 2024 &mdash; I was referred to a psychiatrist for psychological treatment.'),
     B('17 May 2024 &mdash; the substance of the disclosure was directed at me. There was no investigation of '
       'the functions raised, other than that response.'),
     B('18 June 2024 &mdash; psychological injury, followed by certified incapacity from 1 July 2024.'),
     B('24 October 2024 &mdash; diagnosis of major depressive disorder with anxiety state.'),
     B('24 December 2024 &mdash; the Ethical Standards Unit determination.'),
     B('24 February 2025 &mdash; a return to work was confirmed for 7:00 am that day and did not proceed.'),
     B('Since then &mdash; the cost to my health, the loss of my housing, and the cost of the matters '
       'set out in this letter, over more than a year.'),
     B('13 July 2026 &mdash; Metro South Health has paid me no wages for work since that date.'),
     P('I am not asking LBH HR to assess a claim against those costs and or place the figure on any of it. '
       'I record the human cost so that the handling is not treated as one missed pay. I am notifying the '
       'Service of the events and of those consequences.'),

     H('E. &nbsp;What I ask of Metro South Health'),
     P('I ask that, by Friday 18 September 2026, LBH HR and Injury Management confirm in writing that:'),
     Paragraph('(a) &nbsp;further communication about my health, my claim and my disclosure will be with the '
               'appropriate officer, not with a group list;', BULL),
     Paragraph('(b) &nbsp;Metro South Health will respect its own privacy policies, procedures and practices, '
               'and the <i>Information Privacy Act 2009</i> and section 65 of the <i>Public Interest Disclosure '
               'Act 2010</i>. If any of my information or disclosures is to be shared, that sharing is to be in '
               'accordance with those rules. Injury Management and LBH HR will not initiate contact with '
               'Australian Retirement Trust, QSuper or Solv about my health or my claim. If the fund requests '
               'information in the ordinary Part B process, that is the fund&rsquo;s request; and', BULL),
     Paragraph('(c) &nbsp;the statement of 13 August 2026 at 4:42 pm is withdrawn in writing to every person '
               'who received it.', BULL),
     P('I am not asking, in this letter, for a decision on long service leave or the SNP forms. Those matters '
       'were raised in my separate email yesterday.'),
     P('Ms Petering at Together Queensland is copied so that the union has the same notice.'),
     Spacer(1, 10),
     Paragraph('Kind regards,', SIGN), Spacer(1, 16),
     Paragraph('<b>Cory Shepherd</b>', SIGN),
     Paragraph('Employee no. 388372', SIGN),
     Paragraph('coryshepherd1@hotmail.com', SIGN),
     Paragraph('0417 400 227', SIGN)]

doc.build(S)

# ---- metadata: scrub everything, then set only author, title and the dates
# Queensland has no daylight saving: AEST is always UTC+10.
now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)
stamp = now.strftime("D:%Y%m%d%H%M%S+10'00'")
pdf = pikepdf.open(OUT, allow_overwriting_input=True)
if '/Metadata' in pdf.Root: del pdf.Root['/Metadata']
for k in ('/PieceInfo', '/Names', '/AcroForm', '/OpenAction', '/AA', '/StructTreeRoot', '/MarkInfo', '/Lang'):
    if k in pdf.Root: del pdf.Root[k]
for pg in pdf.pages:
    for k in ('/Metadata', '/PieceInfo', '/Annots', '/AA'):
        if k in pg.obj: del pg.obj[k]
for k in list(dict(pdf.docinfo)):
    del pdf.docinfo[k]
pdf.docinfo['/Author'] = AUTHOR
pdf.docinfo['/Title'] = TITLE
pdf.docinfo['/CreationDate'] = stamp
pdf.docinfo['/ModDate'] = stamp
pdf.save(OUT, linearize=False, fix_metadata_version=False,
         object_stream_mode=pikepdf.ObjectStreamMode.generate)
print('built', OUT)
