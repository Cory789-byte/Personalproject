import io, re, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle
from xml.sax.saxutils import escape

H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.5,leading=14,spaceBefore=10,spaceAfter=4)
B=PS('b',fontName='Helvetica',fontSize=9.6,leading=13.2,spaceAfter=7)
BI=PS('bi',fontName='Helvetica',fontSize=9.6,leading=13.2,spaceAfter=7,leftIndent=10*mm,firstLineIndent=-5*mm)
SM=PS('sm',fontName='Helvetica',fontSize=8.4,leading=10.6)
SIG=PS('sig',fontName='Helvetica',fontSize=9.6,leading=13)

# ---------- 1. Render the covering letter EXACTLY as supplied ----------
raw = open('/tmp/letter_final.txt').read()
body = raw[raw.index('Dear Jacqui, Chloe and Payroll,'):]
paras = re.split(r'\n\s*\n', body.strip())

flow = [P('CORY SHEPHERD (388372) — LOGAN HOSPITAL SWITCHBOARD, METRO SOUTH HEALTH',H1),
        P('Part 1: the sick-leave coding since 3 July · Part 2: payment &nbsp;·&nbsp; 3 September 2026',SM),
        P('To: Jacqui Roberts &nbsp;&middot;&nbsp; Cc: Chloe Taylor; PayrollMetroSouth; Emily Petering',SM),
        Spacer(1,8)]

def render_para(para):
    lines = para.split('\n')
    text = ' '.join(l.strip() for l in lines)
    text = escape(text)
    m = re.match(r'^(\d+)\.\s+(.*)$', text)
    if m:
        return P(f'<b>{m.group(1)}.</b>&nbsp;&nbsp;{m.group(2)}', BI)
    if text.strip('=').isupper() and len(text) < 60 and ('PART' in text):
        return P(text, H2)
    return P(text, B)

for para in paras:
    if not para.strip():
        continue
    if para.strip() == 'Kind regards,':
        flow.append(Spacer(1,4)); flow.append(P('Kind regards,', SIG)); continue
    if para.strip().startswith('Cory Shepherd'):
        for ln in para.split('\n'):
            flow.append(P(escape(ln.strip()), SIG))
        continue
    flow.append(render_para(para))

buf = io.BytesIO()
doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=16*mm, title='', author='')
doc.build(flow)
buf.seek(0)
letter_pdf = pikepdf.open(buf)
print('letter pages:', len(letter_pdf.pages))

# ---------- 2. Assemble to match the letter's own description ----------
parts = [
    ('LETTER', letter_pdf, 'Covering letter — Part 1: the sick-leave coding since 3 July · Part 2: payment'),
    ('out/EMAILS_leave_requests_from_3JUL_and_eligibility_3SEP2026.pdf', None, 'The seventeen emails referred to in the letter, each reproduced once as sent, numbered 1–41 in date order (email 1, email 3 … as cited)'),
    ('out/TABLES_leave_requests_and_payment_3SEP2026.pdf', None, 'Table 1: every leave request from 3 July, with the email it is in · Table 2: payment, what is to be actioned by pay period'),
    ('../documents/instruments/QH-POL-188_HR_Policy_C13_Payment_of_salaries_and_wages_23JUN2025.pdf', None, 'Queensland Health HR Policy C13, Payment of salaries and wages (QH-POL-188), Chief Human Resources Officer, 23 June 2025 (8 pages)'),
    ('../documents/instruments/ATT12_Directive_12-24_Special_Leave.pdf', None, 'Minister for Industrial Relations Directive 12/24: Special Leave, effective 30 September 2024 (12 pages)'),
]
srcs=[]; counts=[]
for path,pre,_ in parts:
    if pre is not None:
        srcs.append(pre); counts.append(len(pre.pages))
    else:
        d = pikepdf.open(path); srcs.append(d); counts.append(len(d.pages))

ibuf = io.BytesIO()
idoc = SimpleDocTemplate(ibuf, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=15*mm, bottomMargin=15*mm, title='', author='')
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.2)
s=[P('CORY SHEPHERD (388372) — COMPLETE PACKAGE',H1),
   P('To Jacqui Roberts, Chloe Taylor and Payroll · leave and payment, 3 July – 3 September 2026',SM),
   Spacer(1,8)]
rows=[[P('<b>Pages</b>',SMB),P('<b>Contents</b>',SMB)]]
pg=2
for (_,_,desc),n in zip(parts,counts):
    rows.append([P(f'{pg}–{pg+n-1}' if n>1 else str(pg), SM), P(desc, SM)]); pg+=n
t = Table(rows, colWidths=[24*mm,146*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),
    ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]))
s.append(t)
idoc.build(s)
ibuf.seek(0)
idx_pdf = pikepdf.open(ibuf)
assert len(idx_pdf.pages) == 1

out = pikepdf.new()
out.pages.extend(idx_pdf.pages)
for d in srcs: out.pages.extend(d.pages)

with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r = out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
if '/Names' in r and '/EmbeddedFiles' in r.Names:
    del r.Names['/EmbeddedFiles']
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]

out.save('out/CORY_SHEPHERD_388372_TO_JACQUI_LEAVE_PAYMENT_3SEP2026.pdf', fix_metadata_version=False)
print('TOTAL PAGES', len(out.pages))
