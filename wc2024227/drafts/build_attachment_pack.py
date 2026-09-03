import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=4); B=PS('b',fontName='Helvetica',fontSize=9.6,leading=13); SM=PS('sm',fontName='Helvetica',fontSize=8.4,leading=10.6)
parts=[('out/EMAILS_ORIGINALS_leave_requests_from_3JUL_3SEP2026.pdf','Section A — The original emails, as sent and received: six original email documents in date order, with an index (Tabs 1–6)'),
       ('out/TABLES_leave_requests_and_payment_3SEP2026.pdf','Section B — Table 1: every leave request from 3 July, with the tab it is in · Table 2: payment, what is to be actioned by pay period'),
       ('../documents/instruments/QH-POL-188_HR_Policy_C13_Payment_of_salaries_and_wages_23JUN2025.pdf','Section C — Queensland Health HR Policy C13, Payment of salaries and wages (QH-POL-188), Chief Human Resources Officer, 23 June 2025 (8 pages) — see §2, §6, §8, §9 and the definition of “ad hoc payments”'),
       ('../documents/instruments/ATT12_Directive_12-24_Special_Leave.pdf','Section D — Minister for Industrial Relations Directive 12/24: Special Leave, effective 30 September 2024 (12 pages) — see cl 4.1(b)(ii), cl 6.1, cl 6.5 and Schedule Two, category 11')]
docs=[pikepdf.open(p) for p,_ in parts]; counts=[len(d.pages) for d in docs]
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('ATTACHMENT — Cory Shepherd (388372) — Part 1: the sick-leave coding since 3 July · Part 2: payment',H1),P('3 September 2026 · to Chloe Taylor and PayrollMetroSouth · cc Jacqui Roberts, Emily Petering',SM),Spacer(1,10)]
pg=2
for (_,title),n in zip(parts,counts):
    s.append(P(f'<b>pp {pg}–{pg+n-1}</b> &nbsp; {title}',B)); s.append(Spacer(1,6)); pg+=n
s.append(Spacer(1,10)); s.append(P('Section A is unaltered. Sections C and D are reproduced as published.',SM))
doc.build(s); buf.seek(0); out=pikepdf.open(buf)
for d in docs: out.pages.extend(d.pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
if '/Names' in r and '/EmbeddedFiles' in r.Names: del r.Names['/EmbeddedFiles']
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/ATTACHMENT_PACK_Taylor_Payroll_3SEP2026.pdf'); print('pages',len(out.pages),counts)
