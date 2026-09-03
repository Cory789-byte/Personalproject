import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=4); B=PS('b',fontName='Helvetica',fontSize=9.6,leading=13); SM=PS('sm',fontName='Helvetica',fontSize=8.4,leading=10.6)
parts=[('out/EMAILS_leave_requests_from_3JUL_and_eligibility_3SEP2026.pdf','Section A — The emails: leave requested from 3 July 2026, and the eligibility exchange of 2–3 September (seventeen emails, each reproduced once as sent, in date order)'),
       ('out/TABLES_leave_requests_and_payment_3SEP2026.pdf','Section B — Table 1: every leave request from 3 July, with the email it is in · Table 2: payment, what is to be actioned by pay period'),
       ('../documents/instruments/QH-POL-188_HR_Policy_C13_Payment_of_salaries_and_wages_23JUN2025.pdf','Section C — Queensland Health HR Policy C13, Payment of salaries and wages (QH-POL-188), Chief Human Resources Officer, 23 June 2025 (8 pages) — see §2, §6, §8, §9 and the definition of “ad hoc payments”')]
docs=[pikepdf.open(p) for p,_ in parts]; counts=[len(d.pages) for d in docs]
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('ATTACHMENT — Cory Shepherd (388372) — Part 1: the sick-leave coding since 3 July · Part 2: payment',H1),P('3 September 2026 · to Chloe Taylor and PayrollMetroSouth · cc Jacqui Roberts, Emily Petering',SM),Spacer(1,10)]
pg=2
for (_,title),n in zip(parts,counts):
    s.append(P(f'<b>pp {pg}–{pg+n-1}</b> &nbsp; {title}',B)); s.append(Spacer(1,6)); pg+=n
s.append(Spacer(1,10)); s.append(P('Nothing in Sections A and B has been altered other than the omission of standard email boilerplate. Section C is reproduced as published by Queensland Health.',SM))
doc.build(s); buf.seek(0); out=pikepdf.open(buf)
for d in docs: out.pages.extend(d.pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/ATTACHMENT_PACK_Taylor_Payroll_3SEP2026.pdf'); print('pages',len(out.pages),counts)
