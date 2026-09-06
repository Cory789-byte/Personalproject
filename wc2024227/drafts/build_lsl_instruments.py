#!/usr/bin/env python3
"""MSH-INJ-5795 - Long service leave: the instruments. Index page + originals, page extracts.
Serve with the email to the Switchboard Manager and Payroll. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer
from reportlab.pdfgen import canvas as _canvas

INST = '../documents/instruments/'
HD   = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11, textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2  = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=3)
TITLE= ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=11.5, leading=14, spaceAfter=3)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=8.2, leading=9.6, spaceAfter=3)
CELL = ParagraphStyle('CELL', parent=BODY, fontSize=7.6, leading=9.0, spaceAfter=0)
CELLB= ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')
def C(t): return Paragraph(t, CELL)

# (file, [source pages], instrument label, what it carries, what is omitted)
TABS = [
 ('ATT22_Industrial_Relations_Act_2016_Qld.pdf', [(115,'113'),(117,'115'),(146,'144'),(147,'145')],
  'Industrial Relations Act 2016 (Qld), reprint current as at 1 January 2026',
  'Section 90(2) (page 113): parental leave "not to be taken into account in working out the employee\'s period of '
  'service". Section 94 (page 115): "the provisions of part 4 apply for working out an employee\'s rights and '
  'entitlements to long service leave under this division". Section 134(3) (pages 144 to 145): continuity of service '
  '"is not broken by an absence, including through illness or injury - (a) on paid leave approved by the employer; or '
  '(b) on unpaid leave approved by the employer".',
  'The remainder of the reprint. Section 134(3) runs across two pages and both are included. Page numbers are the reprint\'s own.'),
 ('ATT03_HHS_General_Employees_Award_2015.pdf', [(1,'title page'),(5,'5'),(16,'16'),(40,'40'),(51,'51')],
  'Hospital and Health Service General Employees (Queensland Health) Award - State 2015',
  'Clause 4.1 (page 5): the Award applies to "those employees described in Schedules 2, 3, 4, 5 and 6" and to "each '
  'hospital and health service, in their capacity as the employer". Clause 12.1(a) (page 16): the administrative '
  'stream. Schedule 3 (page 51): Administrative Officer Level 3 (AO3). Clause 22(a) (page 40): long service leave "is '
  'provided for in Division 9 of the QES". Clause 22(c) (same page): "Employees who have completed 7 years\' '
  'continuous service are entitled to take long service leave on full pay or half pay."',
  'The remainder of the Award. The title page is included to identify the instrument; pages 5, 16 and 51 to show '
  'that it covers an Administration Officer AO3 employed by a hospital and health service.'),
 ('ATT02_EB12_CA_No12_2025.pdf', [(1,'certificate of approval'),(37,'35')],
  'Queensland Public Health Sector Certified Agreement No. 12',
  'Clause 9.10.1 (page 35): "Long service leave entitlements and conditions are outlined in HR Policy C38 Long Service '
  'Leave."',
  'The remainder of the Agreement. The certificate of approval is included to identify the instrument.'),
 ('ATT28_HR_Policy_C38_Long_Service_Leave_QH-POL-163_Dec2021.pdf', None,
  'HR Policy C38, Long Service Leave (QH-POL-163), December 2021',
  'Section 1 (page 2): employees "may apply for pro rata long service leave on full pay, or half pay, after completing '
  'seven years continuous service". Attachment One: requests for leave "are not to be unreasonably refused" and the '
  'employee "is to be given timely advice as to whether or not leave is approved".',
  'Nothing. The policy is reproduced in full.'),
 ('ATT29_Directive_10-24_Long_Service_Leave_CURRENT_eff30SEP2024.pdf', None,
  'Directive 10/24, Long Service Leave, effective 30 September 2024',
  'Clause 8.1 (page 3): "employees are entitled to take pro rata long service leave after 7 years continuous service". '
  'Clause 7.4 (page 3): "The employer must respond to a request to take long service leave in a timely manner '
  'indicating whether the leave applied for has been approved or not." Clause 25 (page 7): the definition of '
  'continuous service.',
  'Nothing. The Directive is reproduced in full.'),
 ('QH-POL-188_HR_Policy_C13_Payment_of_salaries_and_wages_23JUN2025.pdf', None,
  'HR Policy C13, Payment of salaries and wages (QH-POL-188), 23 June 2025',
  'Section 6 (page 5): a line manager may submit leave on an employee\'s behalf only where the employee\'s request '
  'for leave "is documented in writing" and any supporting documents "are sourced and retained"; and for leave types '
  'requiring mutual agreement, naming annual and long service leave, line managers "must not unilaterally place '
  'employees on leave". Section 2 (page 2): line managers notified of an incorrect wage payment "must take all steps '
  'to rectify the error". Section 8 (page 6): the ad hoc payment process.',
  'Nothing. The policy is reproduced in full.'),
 ('ATT31_Directive_15-24_Leave_Without_Salary_Credited_As_Service_eff30SEP2024.pdf', None,
  'Directive 15/24, Leave without Salary Credited as Service, effective 30 September 2024',
  'Clause 4.1(b)(ii) (page 1): the directive applies to employees of Hospital and Health Services. Clause 5.1 (page 1): "Employees are to have leave without salary credited as service for leave and salary purposes as provided in this directive." The table "Leave credited as service" (pages 1 to 3) states, for each type of leave without salary, the period recognised for long service leave. For <b>special leave to claim workers&rsquo; compensation</b> (page 3) the period recognised is <b>"Any period."</b> For sick leave without salary (page 1) it is "The first 3 months of any continuous period."',
  'Nothing. The directive is reproduced in full. It supersedes Directive 01/19, which is not held.'),
 ('ATT32_Directive_01-19_Leave_Without_Salary_Credited_As_Service_SUPERSEDED.pdf', None,
  'Directive 01/19, Leave without Salary Credited as Service, effective 13 September 2019, superseded 30 September 2024',
  'The directive in force before Directive 15/24. Its table carries the same row: for <b>special leave to claim workers&rsquo; compensation</b> the period recognised for long service leave is <b>"Any period."</b> Its application clause (page 1) names public service officers and employees engaged under sections 147(2)(a) and 148(2)(a) of the <i>Public Service Act 2008</i>, and does not name Hospital and Health Services.',
  'Nothing. Reproduced in full, as published by the Office of Industrial Relations and marked superseded.'),
]

s = [Paragraph('METRO SOUTH HOSPITAL AND HEALTH SERVICE', HD),
     Paragraph('MSH-INJ-5795 &nbsp;|&nbsp; Cory Shepherd, employee number 388372', HD2),
     Paragraph('LONG SERVICE LEAVE &ndash; THE INSTRUMENTS', TITLE),
     Paragraph('Provided with my email of 7 September 2026 to the Switchboard Manager and Payroll. Tabs 1 to 5, 7 and 8 are the '
               'instruments bearing on whether periods of leave without salary are credited as service for long service leave. '
               'Tab 6 is the policy governing what may be submitted on my behalf. '
               'Each page carries a footer identifying the instrument and its page number in the source '
               'document.', BODY)]
data=[[Paragraph('Tab',CELLB),Paragraph('Instrument',CELLB),Paragraph('The provisions it carries',CELLB),
       Paragraph('Pages omitted',CELLB)]]
for i,(f,pp,label,carries,omit) in enumerate(TABS,1):
    data.append([C(str(i)),C(label),C(carries),C(omit)])
W=A4[0]-30*mm
t=Table(data, colWidths=[7*mm, W*0.24, W*0.51, W*0.25-7*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
 ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),
 ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
 ('TOPPADDING',(0,0),(-1,-1),1.6),('BOTTOMPADDING',(0,0),(-1,-1),1.6)]))
s.append(t)
buf=io.BytesIO()
doc=BaseDocTemplate(buf,pagesize=A4,leftMargin=15*mm,rightMargin=15*mm,topMargin=12*mm,bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(15*mm,12*mm,A4[0]-30*mm,A4[1]-24*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
doc.build(s); buf.seek(0)

out=pikepdf.new()
out.pages.extend(pikepdf.open(buf).pages)
stamps=[None]
for f,pp,label,_,_ in TABS:
    src=pikepdf.open(INST+f)
    pairs = pp if pp else [(i+1, str(i+1)) for i in range(len(src.pages))]
    for pnum, printed in pairs:
        out.pages.append(src.pages[pnum-1])
        stamps.append((label, printed))
total=len(out.pages)
# footer stamps
_keep=[]
for n,info in enumerate(stamps):
    if info is None: continue
    label,printed=info
    txt=(f'MSH-INJ-5795 · Cory Shepherd 388372 · Long service leave – the instruments · '
         f'{label} · at page {printed} · page {n+1} of {total}')
    _pg=out.pages[n]
    _bx=_pg.obj.get('/CropBox') or _pg.obj.get('/MediaBox')
    _x0,_y0,_x1,_y1=[float(v) for v in _bx]
    PW,PH=_x1-_x0,_y1-_y0
    b=io.BytesIO(); c=_canvas.Canvas(b,pagesize=(PW,PH))
    FS=6.0
    avail=PW-16*mm
    while c.stringWidth(txt,'Helvetica',FS) > avail and FS > 4.0:
        FS -= 0.1
    c.setFont('Helvetica',FS)
    w=c.stringWidth(txt,'Helvetica',FS); x=PW-8*mm-w; y=4.0*mm
    c.setFillColorRGB(1,1,1)
    c.rect(x-1.5*mm, y-1.2*mm, w+3*mm, FS+1.8, stroke=0, fill=1)
    c.setFillColorRGB(.35,.35,.35); c.setFont('Helvetica',FS)
    c.drawString(x, y, txt)
    c.save(); b.seek(0)
    _sp=pikepdf.open(b); _keep.append(_sp)
    out.pages[n].add_overlay(_sp.pages[0])
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in out.Root: del out.Root[k]
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
# bookmarks: index page + one per tab, so a reader can jump straight to a provision
_starts=[]; _n=1
for f,pp,label,_,_ in TABS:
    _src=pikepdf.open(INST+f)
    _cnt=len(pp) if pp else len(_src.pages)
    _starts.append((label,_n)); _n+=_cnt
with out.open_outline() as _ol:
    _ol.root.append(pikepdf.OutlineItem('Index - what each tab carries', 0))
    for _i,(_lab,_pg) in enumerate(_starts,1):
        _ol.root.append(pikepdf.OutlineItem(f'Tab {_i} - {_lab}', _pg))

dest='out/LSL_THE_INSTRUMENTS.pdf'
out.save(dest,fix_metadata_version=False)
print('built',dest,total,'pages')
import scrub_pdf as _sc
print('scrub:', _sc.scrub_file(dest if 'dest' in dir() else out_path), 'annotation(s) removed')
