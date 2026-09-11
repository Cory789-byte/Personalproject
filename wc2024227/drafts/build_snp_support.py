# -*- coding: utf-8 -*-
import datetime, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image)
from pypdf import PdfReader, PdfWriter

OUT = 'out/SNP_supporting_statement_two_periods_11SEP2026.pdf'
AUTHOR = 'Cory Shepherd'
TITLE = 'Supporting statement - two applications for sick leave without pay'

NAME = ParagraphStyle('N', fontName='Times-Bold', fontSize=12.5, leading=15, spaceAfter=1)
ADDR = ParagraphStyle('A', fontName='Times-Roman', fontSize=8.8, leading=11.6,
                      textColor=colors.HexColor('#444444'), spaceAfter=9)
SUBJ = ParagraphStyle('S', fontName='Times-Bold', fontSize=11, leading=14.5, spaceAfter=3)
DATE = ParagraphStyle('D', fontName='Times-Roman', fontSize=9.5, leading=13, spaceAfter=9,
                      textColor=colors.HexColor('#444444'))
BODY = ParagraphStyle('B', fontName='Times-Roman', fontSize=10, leading=14.2, spaceAfter=7, alignment=4)
BULL = ParagraphStyle('U', parent=BODY, leftIndent=12, bulletIndent=2, spaceAfter=4)
QUOT = ParagraphStyle('Q', parent=BODY, leftIndent=12, rightIndent=8, fontName='Times-Italic',
                      spaceBefore=3, spaceAfter=7)
HEAD = ParagraphStyle('H', fontName='Times-Bold', fontSize=10.4, leading=14,
                      spaceBefore=12, spaceAfter=5)
CELLH = ParagraphStyle('CH', fontName='Times-Bold', fontSize=9.5, leading=12.5)
CELL = ParagraphStyle('C', fontName='Times-Roman', fontSize=9.5, leading=12.5)
SIGN = ParagraphStyle('G', fontName='Times-Roman', fontSize=10, leading=13.6, spaceAfter=0)

def furniture(c, d):
    c.saveState(); c.setFont('Times-Roman', 7.5); c.setFillColor(colors.HexColor('#777777'))
    c.drawString(22*mm, 12*mm, 'C Shepherd, employee no. 388372 - supporting statement, sick leave without pay')
    c.drawRightString(A4[0]-22*mm, 12*mm, 'Page %d' % c.getPageNumber()); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm,
                      topMargin=20*mm, bottomMargin=20*mm)
doc.addPageTemplates([PageTemplate('n', [Frame(22*mm, 20*mm, A4[0]-44*mm, A4[1]-40*mm, id='f')],
                                   onPage=furniture)])
P = lambda t: Paragraph(t, BODY)
B = lambda t: Paragraph(t, BULL, bulletText='–')
Q = lambda t: Paragraph(t, QUOT)
H = lambda t: Paragraph(t, HEAD)

def tbl(rows, widths):
    t = Table(rows, colWidths=widths, hAlign='LEFT')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LINEBELOW',(0,0),(-1,0),0.6,colors.HexColor('#555555')),
        ('LINEBELOW',(0,1),(-1,-2),0.25,colors.HexColor('#CCCCCC')),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(0,-1),0)]))
    return t

W = A4[0]-44*mm
S = [Paragraph('CORY SHEPHERD', NAME),
     Paragraph('Administration Officer, Switchboard Services, Logan Hospital &nbsp;|&nbsp; '
               'Employee no. 388372<br/>coryshepherd1@hotmail.com &nbsp;|&nbsp; 0417 400 227', ADDR),
     Paragraph('Supporting statement &ndash; two applications for sick leave without pay', SUBJ),
     Paragraph('Recoding of two periods presently recorded as leave without pay, at the request of '
               'Metro South Payroll &nbsp;&middot;&nbsp; 11 September 2026', DATE),

     H('1. &nbsp;What is applied for'),
     P('Two applications for <b>sick leave without pay</b>, for the two periods identified by Metro '
       'South Payroll on 7 and 8 September 2026. The dates are Payroll&rsquo;s own and are not varied.'),
     tbl([[Paragraph('<b>Application</b>', CELLH), Paragraph('<b>Period</b>', CELLH),
           Paragraph('<b>Days (inclusive)</b>', CELLH)],
          [Paragraph('1', CELL), Paragraph('<b>21 June 2024 &ndash; 20 September 2024</b>', CELL), Paragraph('92', CELL)],
          [Paragraph('2', CELL), Paragraph('<b>13 December 2024 &ndash; 23 February 2025</b>', CELL), Paragraph('73', CELL)]],
         [22*mm, W-22*mm-32*mm, 32*mm]),
     Spacer(1, 6),
     P('The periods are presently recorded as leave without pay. Nothing else is sought by these '
       'applications, and no other period is affected.'),

     H('2. &nbsp;Payroll has already identified the correction and the step required'),
     P('On 7 September 2026 at 1:28 pm Metro South Payroll wrote to the line manager:'),
     Q('&ldquo;Could I please confirm with you whether the following periods were intended to be '
       'recorded as Sick No Pay rather than Leave Without Pay? 21.06.2024 - 20.09.2024 / 13.12.2024 - '
       '23.02.2025. This will affect the employee&rsquo;s LSL date&hellip; we would require a leave '
       'form to be submitted for both periods. Could you please confirm?&rdquo;'),
     P('On 8 September 2026 at 2:24 pm Ms Grace Strachan, Senior Payroll Officer, wrote to me:'),
     Q('&ldquo;We believe that the periods 21/06/2024 - 20/09/2024 and 13/12/2024 - 23/02/2025 '
       '<b>should have been booked as Sick No Pay (SNP) rather than Leave Without Pay (LWOP)</b>&hellip; '
       'If these periods need to be changed to Sick No Pay, new leave forms will be required for both '
       'periods. Once the leave forms are received and the leave is updated accordingly, '
       '<b>we can recognise the first three months of each period towards your LSL date.</b>&rdquo;'),
     P('These applications are made so that the leave forms Payroll requires are on foot. I am not '
       'asking anyone to accept a new position; the position is Payroll&rsquo;s own.'),

     H('3. &nbsp;Application 1 &ndash; 21 June 2024 to 20 September 2024'),
     P('The absence was medical from the outset and is documented throughout:'),
     B('My leave record shows <b>sick leave on 7, 8 and 9 June 2024</b>, including sick leave without '
       'pay on 9 June, and leave without pay from 10 June 2024.'),
     B('A <b>medical certificate was issued on 28 June 2024</b>.'),
     B('The <b>work capacity certificate of Dr Peter Hawes dated 1 July 2024</b> records the date of '
       'injury as <b>18 June 2024</b> and that I was first seen for that injury on 1 July 2024.'),
     B('That certificate certifies <b>no functional capacity for any type of work over the period '
       '1 July to 6 October 2024</b> &ndash; a period which contains the whole of this application '
       'from 1 July onward.'),
     B('Further work capacity certificates were issued on <b>7 August 2024 (Dr Ki Pang)</b> and on '
       '<b>11 August and 8 September 2024 (Dr Hawes)</b>.'),
     B('Each certificate records that there was <b>no pre-existing factor or condition</b>.'),
     B('The certificates record the stated date of injury as <b>18 June 2024</b> and first '
       'presentation on <b>1 July 2024</b>.'),

     H('4. &nbsp;Application 2 &ndash; 13 December 2024 to 23 February 2025'),
     P('The absence was a continuation of the same medical condition:'),
     B('<b>On 24 October 2024</b> my treating psychiatrist, Dr Ravikumar Bangalore Krishnaiah, '
       'diagnosed <b>Major Depressive Disorder with anxiety state</b> at the first consultation, and '
       'confirmed that diagnosis in writing the same day.'),
     B('<b>On 13 February 2025</b> &ndash; within this period &ndash; Dr Krishnaiah provided a report '
       'recording the continuing diagnosis, its severity and functional effect, and the treatment then '
       'in place.'),
     B('The period ends on <b>23 February 2025</b>, being the day before a return to work was '
       'confirmed for <b>7:00 am on 24 February 2025</b>.'),
     P('If a work capacity certificate specific to this period is required in addition to what is '
       'already held, please let me know and I will obtain it from the treating practice. I would '
       'rather be told what is missing than have the application held.'),

     H('4A. &nbsp;The medical evidence, and where it is held'),
     P('Four work capacity certificates are attached to this statement: <b>Dr Peter Hawes, 1 July '
       '2024</b>; <b>Dr Ki Pang, 7 August 2024</b>; and <b>Dr Peter Hawes, 11 August and '
       '8 September 2024</b>. Together they certify <b>no capacity for any work over the period '
       '1 July to 6 October 2024</b>, each recording the stated date of injury as 18 June 2024 and '
       'first presentation on 1 July 2024.'),
     P('Certificates for these absences were provided at the time. If anything further is required, '
       'please tell me what it is and I will provide it.'),
     P('The question of how these periods came to be recorded as leave without pay rather than sick '
       'leave without pay is the question I raised with Payroll on 7 September 2026, and it remains '
       'open. <b>Nothing in these two applications depends on that question being answered</b>, and I '
       'do not ask that it be answered before the recoding is effected.'),

     H('5. &nbsp;The effect, on Payroll&rsquo;s own figures'),
     P('Payroll&rsquo;s calculation of 4 September 2026 records my commencement with Queensland Health '
       'as <b>25 March 2019</b>, and that eligibility would ordinarily arise on <b>25 March 2026</b>. '
       'Payroll has identified <b>189 days presently excluded</b>, being 24 days (18 May &ndash; '
       '10 June 2022), 92 days (21 June &ndash; 20 September 2024) and 73 days (13 December 2024 '
       '&ndash; 23 February 2025), which moves the date to <b>29 September 2026</b>.'),
     P('On Payroll&rsquo;s stated approach &ndash; that on recoding &ldquo;the first three months of '
       'each period&rdquo; are recognised &ndash; each of these two periods falls <b>entirely</b> '
       'within its own first three months: three months from 21 June 2024 ends 21 September 2024, and '
       'the period closes on 20 September; three months from 13 December 2024 ends 13 March 2025, and '
       'the period closes on 23 February. On that arithmetic <b>165 of the 189 days return</b>, '
       'leaving only the 24 days of 2022, and the resulting date falls in <b>April 2026</b>. '
       'The calculation is of course Payroll&rsquo;s to make.'),

     H('6. &nbsp;Reservation'),
     P('I have received no wages for work since 13 July 2026. Since 3 July 2026 I have been certified '
       'fit for duties with restrictions on the Employee Capability Checklist completed by Metro South '
       'Health, I have remained available, and I have not been provided with work. What I have been '
       'paid since 13 July has been drawn from my own leave accruals and not paid as wages.'),
     P('<b>Any leave applied for, taken or paid in that period is applied for and taken under protest '
       'and without prejudice to my claim for wages for the period I have not been provided work, and '
       'I reserve the right to seek reinstatement of the leave taken.</b> These two applications relate '
       'to 2024 and 2025 and are made solely to give effect to the recoding Payroll has identified; '
       'they are not an acceptance of any position about 2026.'),
     Spacer(1, 14),
     Paragraph('<b>Signed</b>', SIGN),
     Spacer(1, 4),
     Image('assets/SIGNATURE_CoryShepherd.png', width=44*mm, height=23*mm, hAlign='LEFT'),
     Paragraph('______________________________________', SIGN),
     Spacer(1, 3),
     Paragraph('Cory Lea Shepherd', SIGN),
     Paragraph('Administration Officer, Switchboard Services, Logan Hospital', SIGN),
     Paragraph('Employee no. 388372', SIGN),
     Spacer(1, 8),
     Paragraph('Date: &nbsp;11 September 2026', SIGN),
     Spacer(1, 14),
     Paragraph('<i>Attached: work capacity certificates of Dr Peter Hawes dated 1 July 2024, Dr Ki Pang dated '
               '7 August 2024, and Dr Peter Hawes dated 11 August and 8 September 2024.</i>', ADDR)]

doc.build(S)

now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)
stamp = now.strftime("D:%Y%m%d%H%M%S+10'00'")
pdf = pikepdf.open(OUT, allow_overwriting_input=True)
if '/Metadata' in pdf.Root: del pdf.Root['/Metadata']
for k in ('/PieceInfo','/Names','/AcroForm','/OpenAction','/AA','/StructTreeRoot','/MarkInfo','/Lang'):
    if k in pdf.Root: del pdf.Root[k]
for pg in pdf.pages:
    for k in ('/Metadata','/PieceInfo','/Annots','/AA'):
        if k in pg.obj: del pg.obj[k]
for k in list(dict(pdf.docinfo)): del pdf.docinfo[k]
pdf.docinfo['/Author'] = AUTHOR
pdf.docinfo['/Title'] = TITLE
pdf.docinfo['/CreationDate'] = stamp
pdf.docinfo['/ModDate'] = stamp
pdf.save(OUT, linearize=False, fix_metadata_version=False,
         object_stream_mode=pikepdf.ObjectStreamMode.generate)

# append the four certificates, rebuilt at stencil resolution on clean A4 pages
from reportlab.pdfgen import canvas as _canvas
from reportlab.lib.utils import ImageReader
import io as _io
CERTS = ['assets/certs/cert_1_hawes_01jul2024.png',
         'assets/certs/cert_2_pang_07aug2024.png',
         'assets/certs/cert_3_hawes_11aug2024.png',
         'assets/certs/cert_4_hawes_08sep2024.png']
buf = _io.BytesIO(); c = _canvas.Canvas(buf, pagesize=A4)
PW, PH = A4; M = 12*mm
for path in CERTS:
    ir = ImageReader(path); iw, ih = ir.getSize()
    sc = min((PW-2*M)/iw, (PH-2*M)/ih)
    w_, h_ = iw*sc, ih*sc
    c.drawImage(ir, (PW-w_)/2, (PH-h_)/2, w_, h_, preserveAspectRatio=True)
    c.showPage()
c.save(); buf.seek(0)
w = PdfWriter()
for pg in PdfReader(OUT).pages: w.add_page(pg)
for pg in PdfReader(buf).pages: w.add_page(pg)
with open(OUT,'wb') as fh: w.write(fh)

# scrub again after the merge
pdf = pikepdf.open(OUT, allow_overwriting_input=True)
if '/Metadata' in pdf.Root: del pdf.Root['/Metadata']
for k in ('/PieceInfo','/Names','/AcroForm','/OpenAction','/AA','/StructTreeRoot','/MarkInfo','/Lang'):
    if k in pdf.Root: del pdf.Root[k]
for pg in pdf.pages:
    for k in ('/Metadata','/PieceInfo','/Annots','/AA'):
        if k in pg.obj: del pg.obj[k]
for k in list(dict(pdf.docinfo)): del pdf.docinfo[k]
pdf.docinfo['/Author'] = AUTHOR
pdf.docinfo['/Title'] = TITLE
pdf.docinfo['/CreationDate'] = stamp
pdf.docinfo['/ModDate'] = stamp
pdf.save(OUT, linearize=False, fix_metadata_version=False,
         object_stream_mode=pikepdf.ObjectStreamMode.generate)
print('built', OUT)
