# -*- coding: utf-8 -*-
import datetime, io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as _canvas
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image)
from pypdf import PdfReader, PdfWriter

OUT = 'out/SNP_supporting_statement_two_periods_11SEP2026.pdf'
AUTHOR = 'Cory Shepherd'
TITLE = 'Supporting statement - two applications for sick leave without pay'

NAME = ParagraphStyle('N', fontName='Times-Bold', fontSize=11.5, leading=13.5, spaceAfter=1)
ADDR = ParagraphStyle('A', fontName='Times-Roman', fontSize=8.2, leading=10.4,
                      textColor=colors.HexColor('#444444'), spaceAfter=6)
SUBJ = ParagraphStyle('S', fontName='Times-Bold', fontSize=10.4, leading=13, spaceAfter=2)
DATE = ParagraphStyle('D', fontName='Times-Roman', fontSize=8.6, leading=11, spaceAfter=7,
                      textColor=colors.HexColor('#444444'))
BODY = ParagraphStyle('B', fontName='Times-Roman', fontSize=9.4, leading=12.4, spaceAfter=5, alignment=4)
CELLH = ParagraphStyle('CH', fontName='Times-Bold', fontSize=9, leading=11.5)
CELL = ParagraphStyle('C', fontName='Times-Roman', fontSize=9, leading=11.5)
SIGN = ParagraphStyle('G', fontName='Times-Roman', fontSize=9.2, leading=12, spaceAfter=0)

def furniture(c, d):
    c.saveState(); c.setFont('Times-Roman', 7.2); c.setFillColor(colors.HexColor('#777777'))
    c.drawString(20*mm, 11*mm, 'C Shepherd, employee no. 388372 - supporting statement, sick leave without pay')
    c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                      topMargin=16*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate('n', [Frame(20*mm, 16*mm, A4[0]-40*mm, A4[1]-32*mm, id='f')],
                                   onPage=furniture)])
P = lambda t: Paragraph(t, BODY)
W = A4[0]-40*mm

S = [Paragraph('CORY SHEPHERD', NAME),
     Paragraph('Administration Officer, Switchboard Services, Logan Hospital &nbsp;|&nbsp; '
               'Employee no. 388372 &nbsp;|&nbsp; coryshepherd1@hotmail.com &nbsp;|&nbsp; 0417 400 227', ADDR),
     Paragraph('Supporting statement &ndash; two applications for sick leave without pay', SUBJ),
     Paragraph('Recoding of two periods presently recorded as leave without pay, at the request of '
               'Metro South Payroll &nbsp;&middot;&nbsp; 11 September 2026', DATE),

     P('I apply for <b>sick leave without pay</b> for the two periods identified by Metro South '
       'Payroll on 7 and 8 September 2026. The dates below are Payroll&rsquo;s own and are not varied.'),
     Table([[Paragraph('<b>Application</b>', CELLH), Paragraph('<b>Period</b>', CELLH),
             Paragraph('<b>Days (inclusive)</b>', CELLH)],
            [Paragraph('1', CELL), Paragraph('<b>21 June 2024 &ndash; 20 September 2024</b>', CELL), Paragraph('92', CELL)],
            [Paragraph('2', CELL), Paragraph('<b>13 December 2024 &ndash; 23 February 2025</b>', CELL), Paragraph('73', CELL)]],
           colWidths=[22*mm, W-22*mm-30*mm, 30*mm], hAlign='LEFT',
           style=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
             ('LINEBELOW',(0,0),(-1,0),0.6,colors.HexColor('#555555')),
             ('LINEBELOW',(0,1),(-1,-2),0.25,colors.HexColor('#CCCCCC')),
             ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
             ('LEFTPADDING',(0,0),(0,-1),0)])),
     Spacer(1, 6),
     P('Both periods are presently recorded as leave without pay. No other period is affected.'),
     P('<b>Payroll has already identified the correction.</b> On 8 September 2026 Ms Grace Strachan, '
       'Senior Payroll Officer, wrote that these periods &ldquo;should have been booked as Sick No Pay '
       '(SNP) rather than Leave Without Pay (LWOP)&rdquo;, that &ldquo;new leave forms will be required '
       'for both periods&rdquo;, and that once the forms are received and the leave updated, &ldquo;we '
       'can recognise the first three months of each period towards your LSL date.&rdquo; These two '
       'applications supply the leave forms Payroll requires. I am not asking anyone to accept a new '
       'position; the position is Payroll&rsquo;s own.'),
     P('<b>Both absences were medical.</b> Four work capacity certificates are attached &ndash; '
       'Dr Peter Hawes 1 July 2024, Dr Ki Pang 7 August 2024, and Dr Peter Hawes 11 August and '
       '8 September 2024. They record the stated date of injury as 18 June 2024, first presentation on '
       '1 July 2024, no pre-existing factor or condition, and <b>no functional capacity for any type of '
       'work over the period 1 July to 6 October 2024</b>. The second period was a continuation of the '
       'same condition, under the care of a treating specialist from 24 October 2024, and it ends on '
       '23 February 2025 &ndash; the day before my return to work at 7:00 am on 24 February 2025. If '
       'anything further is required, please tell me what it is and I will provide it.'),
     P('<b>Effect.</b> Payroll records commencement on 25 March 2019 and 189 days presently excluded, '
       'moving the long service leave date to 29 September 2026. Each of these two periods falls '
       'entirely within its own first three months, so on Payroll&rsquo;s stated approach 165 of those '
       '189 days return. The calculation is of course Payroll&rsquo;s to make.'),
     P('<b>Reservation.</b> I have received no wages for work since 13 July 2026. Any leave applied '
       'for, taken or paid since that date is applied for and taken under protest and without prejudice '
       'to my claim for wages, and I reserve the right to seek reinstatement of the leave taken. These '
       'two applications relate to 2024 and 2025 and are made solely to give effect to the recoding '
       'Payroll has identified.'),
     Spacer(1, 6),
     Paragraph('<b>Signed</b>', SIGN),
     Image('assets/SIGNATURE_CoryShepherd.png', width=40*mm, height=21*mm, hAlign='LEFT'),
     Paragraph('______________________________________', SIGN),
     Paragraph('Cory Lea Shepherd &nbsp;&middot;&nbsp; Administration Officer, Switchboard Services, '
               'Logan Hospital &nbsp;&middot;&nbsp; Employee no. 388372', SIGN),
     Paragraph('Date: &nbsp;11 September 2026', SIGN),
     Spacer(1, 6),
     Paragraph('<i>Attached: work capacity certificates of Dr Peter Hawes dated 1 July 2024, Dr Ki Pang '
               'dated 7 August 2024, and Dr Peter Hawes dated 11 August and 8 September 2024.</i>', ADDR)]

doc.build(S)

CERTS = ['assets/certs/redacted/cert_1_hawes_01jul2024.png',
         'assets/certs/redacted/cert_2_pang_07aug2024.png',
         'assets/certs/redacted/cert_3_hawes_11aug2024.png',
         'assets/certs/redacted/cert_4_hawes_08sep2024.png']
buf = io.BytesIO(); c = _canvas.Canvas(buf, pagesize=A4)
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
print('built', OUT)
