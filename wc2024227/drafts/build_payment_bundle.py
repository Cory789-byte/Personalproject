#!/usr/bin/env python3
"""MSH-INJ-5795 - Payment: the documents relied on. Front sheet + originals. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle
from reportlab.pdfgen import canvas as _canvas

D='../documents/'
HD   = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11, textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2  = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=3)
TITLE= ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=11.5, leading=14, spaceAfter=3)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=8.2, leading=9.8, spaceAfter=4)
CELL = ParagraphStyle('CELL', parent=BODY, fontSize=7.7, leading=9.2, spaceAfter=0)
CELLB= ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')
def C(t): return Paragraph(t, CELL)

TABS=[
 (D+'medical/Employee_Capability_Checklist_CShepherd_03-07-2026.pdf', None,
  'Employee Capability Checklist, 3 July 2026',
  'Completed by Dr Day Hong Ma on the Health Service&rsquo;s own form, on the day I was held out of the workplace. '
  'It certifies me fit for work with restrictions.'),
 (D+'2026-08-12_Payslip_ZERO_NPSickLeave_76hrs.pdf', None,
  'Pay advice, 12 August 2026',
  '&quot;NP Sick Leave&quot; 76.00 hours, and gross pay of $0.00 for the fortnight.'),
 (D+'correspondence-2026/2026-08-31_FULL_THREAD_v2_Taylor_LSL_AVAC_incl_1606_correction.pdf', None,
  'My application of 31 August 2026, and Ms Taylor&rsquo;s reply of the same day',
  'The application: long service leave on full pay from 13 July 2026, being the date from which I have received no '
  'wages, and on its exhaustion annual leave. The reply: sick leave and annual leave in lieu applied for 17 to '
  '30 August 2026 under PRN 249 863 66, and that &quot;the system is currently not allowing me to apply LSL&quot;.'),
 (D+'correspondence-2026/2026-09-04_1030_Taylor_ADHOC_PROCESSED_PRN24973005_LSL_not_eligible.pdf', [1,2,8,9],
  'Ms Taylor&rsquo;s email of 4 September 2026, and Payroll&rsquo;s advice within it',
  'That ad hoc PRN 24973005 was processed for the fortnight 6 to 17 July 2026 from available sick leave and annual '
  'leave balances; and Payroll&rsquo;s advice that long service leave cannot be entered because of the eligibility date.'),
 (D+'correspondence-2026/2026-09-04_1429_Taylor_fwd_Payroll_Strachan_LSL_calculation_29SEP2026.pdf', None,
  'Payroll&rsquo;s long service leave calculation, 4 September 2026',
  'Commencement 25 March 2019; eligibility arising ordinarily on 25 March 2026; corrected to 29 September 2026 after '
  'excluding three periods of leave without pay. Each of those three periods is recorded on the leave takings report '
  'produced with it as <b>approved</b> leave without pay.'),
 ('out/LSL_THE_INSTRUMENTS.pdf', None,
  'Long service leave &ndash; the instruments',
  'The Industrial Relations Act 2016, the Award, the Agreement, HR Policies C38 and C13, and Directive 10/24. The '
  'first page of that tab lists what each carries. These pages carry their own footers.'),
]

s=[Paragraph('METRO SOUTH HOSPITAL AND HEALTH SERVICE', HD),
   Paragraph('MSH-INJ-5795 &nbsp;|&nbsp; Cory Shepherd, employee number 388372', HD2),
   Paragraph('PAYMENT &ndash; THE DOCUMENTS RELIED ON', TITLE),
   Paragraph('Provided with my email of 7 September 2026 to the Switchboard Manager and Payroll. '
             '<b>What I am asking for:</b> that my application of 31 August 2026 be determined and, if there is no '
             'provision excluding approved leave without pay from continuous service, that my long service leave be '
             'applied from 13 July 2026 and paid. Nothing below has been retyped; each page carries a footer '
             'identifying its source.', BODY)]
data=[[Paragraph('Tab',CELLB),Paragraph('Document',CELLB),Paragraph('What it shows',CELLB)]]
for i,(f,pp,label,shows) in enumerate(TABS,1):
    data.append([C(str(i)),C(label),C(shows)])
W=A4[0]-30*mm
t=Table(data,colWidths=[8*mm,W*0.32,W*0.68-8*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
 ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),
 ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
 ('TOPPADDING',(0,0),(-1,-1),1.8),('BOTTOMPADDING',(0,0),(-1,-1),1.8)]))
s.append(t)
s.append(Paragraph('I am unaware of the provision under which approved leave without pay is excluded from continuous '
                   'service, and have asked to be advised of it. If there is one I will accept it. If there is not, '
                   'my eligibility arose on 25 March 2026.', BODY))
buf=io.BytesIO()
doc=BaseDocTemplate(buf,pagesize=A4,leftMargin=15*mm,rightMargin=15*mm,topMargin=12*mm,bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(15*mm,12*mm,A4[0]-30*mm,A4[1]-24*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
doc.build(s); buf.seek(0)

out=pikepdf.new(); out.pages.extend(pikepdf.open(buf).pages)
stamps=[None]
for f,pp,label,_ in TABS:
    src=pikepdf.open(f)
    idx=[p-1 for p in pp] if pp else range(len(src.pages))
    for k in idx:
        out.pages.append(src.pages[k])
        stamps.append(None if f.startswith('out/') else (label,k+1))
total=len(out.pages); _keep=[]
for n,info in enumerate(stamps):
    if info is None: continue
    label,sp=info
    b=io.BytesIO(); c=_canvas.Canvas(b,pagesize=A4)
    c.setFont('Helvetica',6.2); c.setFillColorRGB(.35,.35,.35)
    import re as _re
    plain=_re.sub(r'&[a-z]+;',"'",label)
    c.drawRightString(A4[0]-14*mm,7*mm,
        f'MSH-INJ-5795 · Cory Shepherd 388372 · Payment – the documents relied on · {plain} · source page {sp} · page {n+1} of {total}')
    c.save(); b.seek(0)
    sp_pdf=pikepdf.open(b); _keep.append(sp_pdf)
    out.pages[n].add_overlay(sp_pdf.pages[0])
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in out.Root: del out.Root[k]
if '/Names' in out.Root and '/EmbeddedFiles' in out.Root.Names: del out.Root.Names['/EmbeddedFiles']
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
dest='out/PAYMENT_THE_DOCUMENTS_RELIED_ON.pdf'
out.save(dest,fix_metadata_version=False)
print('built',dest,total,'pages')
