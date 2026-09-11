# -*- coding: utf-8 -*-
"""Memorandum: what the Deed of Release provides, and what follows for
continuous service and the long service leave date."""
import datetime, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

OUT = 'out/DEED_OF_RELEASE_service_and_LSL_position_11SEP2026.pdf'
AUTHOR = 'Cory Shepherd'
TITLE = 'Deed of Release - continuous service and the long service leave date'

NAME = ParagraphStyle('N', fontName='Times-Bold', fontSize=12, leading=14.5, spaceAfter=1)
ADDR = ParagraphStyle('A', fontName='Times-Roman', fontSize=8.4, leading=10.8,
                      textColor=colors.HexColor('#444444'), spaceAfter=8)
SUBJ = ParagraphStyle('S', fontName='Times-Bold', fontSize=11.2, leading=14.5, spaceAfter=3)
DATE = ParagraphStyle('D', fontName='Times-Roman', fontSize=9, leading=12, spaceAfter=4,
                      textColor=colors.HexColor('#444444'))
NOTE = ParagraphStyle('NT', fontName='Times-Italic', fontSize=8.6, leading=11.4,
                      textColor=colors.HexColor('#555555'), spaceAfter=10,
                      borderPadding=0)
BODY = ParagraphStyle('B', fontName='Times-Roman', fontSize=10, leading=12.9, spaceAfter=4.5, alignment=4)
HEAD = ParagraphStyle('H', fontName='Times-Bold', fontSize=10.6, leading=14,
                      spaceBefore=9.5, spaceAfter=3.5)
# the agreement's own words - set apart, so the document reads as the deed
CL = ParagraphStyle('CL', fontName='Times-Roman', fontSize=9.8, leading=12.8,
                    leftIndent=0, rightIndent=0, spaceBefore=0, spaceAfter=0,
                    alignment=4)
CLH = ParagraphStyle('CLH', fontName='Times-Bold', fontSize=9.2, leading=12,
                     leftIndent=16, spaceBefore=7, spaceAfter=1,
                     textColor=colors.HexColor('#333333'))
CELLH = ParagraphStyle('CH', fontName='Times-Bold', fontSize=8.8, leading=11.5)
CELL = ParagraphStyle('C', fontName='Times-Roman', fontSize=8.8, leading=11.5)
CELLR = ParagraphStyle('CR', parent=CELL, alignment=2)


def furniture(c, d):
    c.saveState()
    c.setFont('Times-Roman', 7.4)
    c.setFillColor(colors.HexColor('#777777'))
    c.drawString(20*mm, 11*mm, 'Deed of Release executed 14 and 21 February 2025 '
                               '- continuous service and the long service leave date')
    c.drawRightString(A4[0]-20*mm, 11*mm, 'Page %d' % c.getPageNumber())
    c.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                      topMargin=18*mm, bottomMargin=18*mm)
doc.addPageTemplates([PageTemplate('n', [Frame(20*mm, 18*mm, A4[0]-40*mm, A4[1]-36*mm, id='f')],
                                   onPage=furniture)])
P = lambda t: Paragraph(t, BODY)
H = lambda t: Paragraph(t, HEAD)
def C(t):
    """A passage quoted from the executed Deed, ruled at the left margin so the
    agreement's own words are visibly distinct from everything around them."""
    return Table([[Paragraph(t, CL)]], colWidths=[W-20*mm], hAlign='RIGHT',
                 style=TableStyle([
                     ('LINEBEFORE', (0, 0), (0, -1), 1.1, colors.HexColor('#8A8A8A')),
                     ('LEFTPADDING', (0, 0), (-1, -1), 9),
                     ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                     ('TOPPADDING', (0, 0), (-1, -1), 3),
                     ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5)]))
CH = lambda t: Paragraph(t, CLH)
W = A4[0]-40*mm

ACCRUAL = [[Paragraph('<b>Period</b>', CELLH),
            Paragraph('<b>Accrues?</b>', CELLH),
            Paragraph('<b>LSL hours accrued</b>', CELLH)],
           [Paragraph('25/03/2019 &ndash; 17/05/2022', CELL), Paragraph('Yes', CELL), Paragraph('155.508', CELLR)],
           [Paragraph('18/05/2022 &ndash; 10/06/2022', CELL), Paragraph('No', CELL), Paragraph('0.000', CELLR)],
           [Paragraph('11/06/2022 &ndash; 20/06/2024', CELL), Paragraph('Yes', CELL), Paragraph('100.153', CELLR)],
           [Paragraph('21/06/2024 &ndash; 20/09/2024', CELL), Paragraph('No', CELL), Paragraph('0.000', CELLR)],
           [Paragraph('<b>21/09/2024 &ndash; 12/12/2024</b>', CELL), Paragraph('<b>Yes</b>', CELL), Paragraph('<b>11.233</b>', CELLR)],
           [Paragraph('13/12/2024 &ndash; 23/02/2025', CELL), Paragraph('No', CELL), Paragraph('0.000', CELLR)],
           [Paragraph('23/02/2025 &ndash; 04/09/2026', CELL), Paragraph('Yes', CELL), Paragraph('75.656', CELLR)],
           [Paragraph('<b>Balance total</b>', CELL), Paragraph('', CELL), Paragraph('<b>342.5518</b>', CELLR)]]

accrual_tbl = Table(ACCRUAL, colWidths=[W-34*mm-32*mm, 34*mm, 32*mm], hAlign='LEFT',
                    style=TableStyle([
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LINEBELOW', (0, 0), (-1, 0), 0.6, colors.HexColor('#555555')),
                        ('LINEBELOW', (0, 1), (-1, -3), 0.25, colors.HexColor('#CCCCCC')),
                        ('LINEABOVE', (0, -1), (-1, -1), 0.6, colors.HexColor('#555555')),
                        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
                        ('LEFTPADDING', (0, 0), (0, -1), 0)]))

S = [
    Paragraph('CORY SHEPHERD', NAME),
    Paragraph('Administration Officer, Switchboard Services, Logan Hospital &nbsp;|&nbsp; '
              'Employee no. 388372', ADDR),
    Paragraph('The Deed of Release &ndash; continuous service and the long service leave date',
              SUBJ),
    Paragraph('Deed of Release between Mr Cory Shepherd and Metro South Hospital and Health '
              'Service, executed by the Applicant on 14 February 2025 and by the Health Service '
              'Chief Executive on 21 February 2025 &nbsp;&middot;&nbsp; 11 September 2026', DATE),
    Paragraph('Confidential. Prepared and held under clause 12 of the Deed, which permits '
              'disclosure to obtain professional legal or accounting advice and to enforce the '
              'Deed. Every passage set in the indented text below is quoted from the executed '
              'Deed itself.', NOTE),

    H('1. &nbsp;What the Deed records'),
    P('The Deed recites the separation and the reinstatement:'),
    CH('Recital D'),
    C('&ldquo;The correspondence nominated a separation date being 20 September 2024 (the '
      '<b>Dismissal</b>). On 23 October 2024, the Health Service paid out the Applicant&rsquo;s '
      'entitlements in accordance with relevant legislation.&rdquo;'),
    CH('Recital F'),
    C('&ldquo;The Health Service by this deed, reinstates the Applicant to his former Employment '
      'effective 20 September 2024.&rdquo;'),
    CH('Clause 1'),
    C('&ldquo;The Health Service reinstates the Applicant to his Employment with an effective date '
      'of 20 September 2024. The Reinstatement takes effect despite any documents that the Health '
      'Service may require the Applicant to execute (for example, for payroll purposes).&rdquo;'),
    P('The employment commenced on 25 March 2019 (recital B) and was permanent full-time at '
      '76 hours per fortnight (recital A).'),

    H('2. &nbsp;What the Health Service agreed to credit'),
    CH('Clause 2'),
    C('&ldquo;Upon execution of this Deed by both parties the Health Service agrees to:<br/>'
      '(a) Credit leave balances paid out to the Applicant on 23 October 2024 as follows;<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;(i) annual leave: 54.16 hours.<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;(ii) leave loading: 54.16 hours<br/>'
      '(b) Reinstate the Applicant&rsquo;s personal leave balances as at the date of '
      'separation.<br/>'
      '(c) Pay to the Applicant:<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;(i) The amount the applicant would have been paid in wages for the '
      'period of 20 September 2024 to 13 December 2024.<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;(ii) An amount of $5,000 by way of legal expenses.<br/>'
      '&nbsp;&nbsp;&nbsp;&nbsp;(the <b>Settlement Sum</b>)<br/>'
      '(d) Deduct from the Settlement Sum the gross amount of the credited leave balances, as '
      'calculated by the Health Service (inclusive of any taxable deductions paid by the Health '
      'Service, including but not limited to income tax withheld).&rdquo;'),
    P('Clause 2(a) has two subparagraphs and no more: the first page of the Deed closes at (ii) '
      'and the second page opens at (b). <b>Long service leave is not mentioned in clause 2, or '
      'anywhere else in the Deed.</b> None had been paid out on 23 October 2024, so there was no '
      'long service leave balance to credit back. The Health Service&rsquo;s own payroll record '
      'confirms it: long service leave previously paid out <b>0.0000</b> and taken <b>0.00</b>.'),
    P('What clause 2(d) deducted from the Settlement Sum was therefore the credited '
      '<b>annual leave and leave loading</b>, taken at their gross value.'),

    H('3. &nbsp;What the reinstatement produced &ndash; on the Health Service&rsquo;s own ledger'),
    P('Reinstatement effective 20 September 2024 restored continuous service from that date. The '
      'long service leave accrual record provided by Metro South Payroll on 4 September 2026 for '
      'employee 388372 shows the result:'),
    accrual_tbl,
    Spacer(1, 7),
    P('<b>The reinstatement period accrued.</b> 21 September to 12 December 2024 carries 11.233 '
      'hours and is marked as accruing service. The Deed did what clause 1 said it would do.'),

    H('4. &nbsp;What the parties agreed about 13 December 2024 to 23 February 2025'),
    CH('Clause 4'),
    C('&ldquo;The period from 13 December 2024 to 23 February 2025 will be treated as leave '
      'without pay.&rdquo;'),
    CH('Clause 5'),
    C('&ldquo;If the Applicant is not fit to return to the workplace on executing this deed, he '
      'will apply for leave using the usual application process.&rdquo;'),
    P('Those two clauses are consecutive and are to be read together. Clause 4 fixes that the '
      'period is <b>unpaid</b>. Clause 5 provides for the Applicant to <b>apply for leave in the '
      'ordinary way</b> if he was not then fit to return &ndash; which he was not, and which the '
      'medical certificates on the file establish.'),
    P('<b>Clause 4 says nothing about continuous service and nothing about long service leave.</b> '
      'It is four lines long and its whole content is that the period is leave without pay. The '
      'exclusion of the period from the long service leave calculation is a consequence of the '
      'leave <b>code</b> subsequently applied to it, not of anything the parties agreed.'),

    H('5. &nbsp;The position that follows'),
    P('On 8 September 2026 Metro South Payroll wrote that the periods 21 June to 20 September 2024 '
      'and 13 December 2024 to 23 February 2025 <b>&ldquo;should have been booked as Sick No Pay '
      '(SNP) rather than Leave Without Pay (LWOP)&rdquo;</b>, that new leave forms would be '
      'required for both, and that once the leave is updated <b>&ldquo;we can recognise the first '
      'three months of each period towards your LSL date.&rdquo;</b>'),
    P('That recoding is consistent with the Deed on the Deed&rsquo;s own words:'),
    P('&nbsp;&nbsp;&nbsp;&nbsp;<b>(a)</b> Sick leave without pay is leave without pay. Recoding the '
      'period to sick leave without pay leaves it unpaid, and so leaves clause 4 satisfied '
      'exactly as written.'),
    P('&nbsp;&nbsp;&nbsp;&nbsp;<b>(b)</b> Clause 5 expressly contemplated a leave application for '
      'that period, made through the usual process, on the footing that the Applicant was not fit '
      'to return. Applying for sick leave without pay is that application, made through that '
      'process.'),
    P('&nbsp;&nbsp;&nbsp;&nbsp;<b>(c)</b> Neither clause 4 nor any other clause bargained away '
      'continuous service or long service leave. Nothing in the recoding alters a term of the '
      'Deed; it records the absence as what the medical evidence shows it was.'),
    P('&nbsp;&nbsp;&nbsp;&nbsp;<b>(d)</b> The period 21 June to 20 September 2024 ends on the '
      'reinstatement effective date and is <b>outside the Deed altogether</b>. Nothing in the Deed '
      'bears on it.'),
    Spacer(1, 4),
    P('<b>Accordingly:</b> the two applications for sick leave without pay give effect to what '
      'Payroll has identified, and they are consistent with clauses 4 and 5 of the Deed. The '
      'Deed credited annual leave, leave loading and personal leave balances, and restored '
      'service from 20 September 2024. It made no provision about long service leave, because '
      'none had been paid out and none was in issue.'),

    Spacer(1, 8),
    Paragraph('Cory Lea Shepherd &nbsp;&middot;&nbsp; Employee no. 388372 '
              '&nbsp;&middot;&nbsp; 11 September 2026', ADDR),
]

doc.build(S)

now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)
stamp = now.strftime("D:%Y%m%d%H%M%S+10'00'")
p = pikepdf.open(OUT, allow_overwriting_input=True)
if '/Metadata' in p.Root: del p.Root['/Metadata']
for k in ('/PieceInfo', '/Names', '/AcroForm', '/OpenAction', '/AA',
          '/StructTreeRoot', '/MarkInfo', '/Lang'):
    if k in p.Root: del p.Root[k]
for pg in p.pages:
    for k in ('/Metadata', '/PieceInfo', '/Annots', '/AA'):
        if k in pg.obj: del pg.obj[k]
for k in list(dict(p.docinfo)): del p.docinfo[k]
p.docinfo['/Author'] = AUTHOR
p.docinfo['/Title'] = TITLE
p.docinfo['/CreationDate'] = stamp
p.docinfo['/ModDate'] = stamp
p.save(OUT, linearize=False, fix_metadata_version=False,
       object_stream_mode=pikepdf.ObjectStreamMode.generate)
print('built', OUT)
