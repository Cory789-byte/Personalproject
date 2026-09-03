import io, re, pickle, pikepdf
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak, KeepTogether
S='/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/thread'
M=pickle.load(open(f'{S}/messages.pkl','rb'))
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3); H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3)
B=PS('b',fontName='Helvetica',fontSize=9.2,leading=12); SM=PS('sm',fontName='Helvetica',fontSize=8.2,leading=10.3); SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.3)
MH=PS('mh',fontName='Helvetica-Bold',fontSize=10.5,leading=13); HD=PS('hd',fontName='Helvetica',fontSize=8.6,leading=10.8,textColor=colors.HexColor('#333333'))
def tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)])); return t
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('PAYMENT AND LEAVE — WHAT IS TO BE ACTIONED, BY PAY PERIOD',H1),
   P('Cory Shepherd (388372), AO3, Switchboard Services, Logan Hospital · 3 September 2026 · for Ms Taylor and Payroll',SM),Spacer(1,5),
   P('1. THE PAY PERIODS',H2)]
rows=[[P('<b>Fortnight</b>',SMB),P('<b>What applies</b>',SMB),P('<b>Hours</b>',SMB),P('<b>Status</b>',SMB),P('<b>Pay date</b>',SMB)]]
data=[('17 – 30 Aug','AVAC processed — process no. 24926366 (msg 39). Applied as “S/L and A/L in lieu of S/L” at “0.5 FTE” (msg 33)','should be 76 — substantive full time; the last reduced-hours arrangement ended 28 Jun','Confirm in writing: gross amount, hours, leave types. If processed at 0.5 FTE, adjust in the next run','Wed 9 Sep'),
 ('31 Aug – 3 Sep','Pre-eligibility on Payroll’s date. Currently “Sick Leave – No Pay” — not applied for; contrary to my instruction of 3 Jul 3:18 pm (msg 4)','76','Leave audit (Payroll) to correct the coding; wages for the held-out period remain claimed','Wed 23 Sep'),
 ('4 – 13 Sep','LONG SERVICE LEAVE, full pay, from Thu 4 Sep 2026 — Payroll’s own eligibility date (msg 40)','76 (38/week)','TO BE ENTERED NOW so it is in this run. No further “Sick Leave – No Pay” from 4 Sep','Wed 23 Sep'),
 ('14 Sep onward','Long service leave continuing until further notice','76','Continuing','Wed 7 Oct …'),
 ('Ad hoc','Enquiry 4471091 (2 Sep) pending. An ad hoc payment was processed for me on 11 Mar 2025 (log 4045255)','—','Payroll: please action, or give the written reason and the officer','As soon as possible')]
for r in data: rows.append([P(escape(x),SM) for x in r])
s.append(tbl(rows,[24*mm,62*mm,26*mm,44*mm,18*mm]))
s.append(P('2. THREE THINGS TO ACTION TODAY',H2))
for x in ['Enter long service leave from Thursday 4 September 2026 at 76 hours per fortnight, continuing, so that it is in the fortnight ending 13 September (paid 23 September). Cease the daily “Sick Leave – No Pay” entries from that date.',
          'Confirm in writing what will be paid on 9 September under process 24926366: gross amount, hours, and the leave types debited — and whether it was processed at 76 hours or at 0.5 FTE.',
          'Payroll: action ad hoc payment enquiry 4471091, or provide the reason in writing.']:
    s.append(P('•  '+x,B))
s.append(P('All leave applied for is applied for under protest and subject to re-credit, on the basis set out in my application of 31 August (msg 32, paragraph 4), which continues to apply. I remain certified fit with restrictions and ready and available to work.',B))
s.append(P('3. THE MESSAGES THIS REFERS TO',H2)); s.append(P('The application, the replies and the corrections of 31 August – 3 September, reproduced as sent. Standard email boilerplate omitted; nothing else altered.',SM)); s.append(PageBreak())
SEL=[32,33,34,35,36,39,40,41]
SUBJ={32:'Cory Shepherd (388372) — application for long service leave and annual leave, and request for AVAC to be processed today',33:'RE: (as above)',34:'Re: (as above)',35:'Re: (as above) — ad hoc payment',36:'RE: (as above)',39:'Cory Shepherd (388372) RE: Please respond to Chloe Taylor regarding long service leave and why it can not be actioned',40:'RE: (as above)',41:'RE: (as above)'}
for n in SEL:
    m=M[n-1]; hdr=[P(f'Message {n}.  {m["when"]:%A %d %B %Y, %H:%M}',MH),P(f'<b>From:</b> {escape(m["frm"])}',HD),P(f'<b>To:</b> {escape(re.sub(r"<.*?>","",m["to"]).strip() or "—")}',HD)]
    if m['cc']: hdr.append(P(f'<b>Cc:</b> {escape(re.sub(r"<.*?>","",m["cc"]).strip())}',HD))
    hdr.append(P(f'<b>Subject:</b> {escape(SUBJ[n])}',HD)); hdr.append(Spacer(1,3)); s.append(KeepTogether(hdr))
    for ln in m['body']: s.append(P(escape(ln) if ln.strip() else '&nbsp;',B))
    s.append(Spacer(1,5)); s.append(P('— end of message —',SM)); s.append(Spacer(1,8))
doc.build(s); buf.seek(0); out=pikepdf.open(buf)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/TAYLOR_PAYROLL_action_sheet_3SEP2026.pdf'); print('pages',len(out.pages))
