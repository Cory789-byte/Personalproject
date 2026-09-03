import pickle, re, io, pikepdf
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak, KeepTogether
S='/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/thread'
M=pickle.load(open(f'{S}/messages.pkl','rb'))
SUBJ={'2026-07-03':'Cory - ECC/Leave Type','2026-07_Cory':'Cory Shepherd_ECC further information (MSH-INJ-5795)',
 '2026-07-15':'Cory Shepherd_ECC further information (MSH-INJ-5795)','2026-07-28':'Response to 2-15 July 2026 correspondence - incorrect application of EB12, Award and QH policies - ECC 3 July 2026 (MSH-INJ-5795)',
 '2026-07-29':'RE: Response to 2-15 July 2026 correspondence (MSH-INJ-5795)','2026-07-30':'RE: Response to 2-15 July 2026 correspondence (MSH-INJ-5795)',
 '2026-08-05':'Stage 1 — roster, leave and pay (MSH-INJ-5795)','2026-08-13_1548':'RE: consent and EAF (MSH-INJ-5795)',
 '2026-08-13_1642':'Follow up on Enquiries — RECALL NOTICE','2026-08-18_1047':'Follow up on Enquiries','2026-08-18_to':'Follow up on Enquiries',
 '2026-08-25':'Meeting - Cory Shepherd (Teams invitation)','2026-08-31':'Cory Shepherd (388372) — application for long service leave and annual leave, and request for AVAC to be processed today','2026-09_Manager':'RE: Cory Shepherd (388372) — application for long service leave and annual leave, and request for AVAC to be processed today','2026-09-02_Outlook':'Cory Shepherd (388372) RE: Please respond to Chloe Taylor regarding long service leave and why it can not be actioned'}
def subj(m):
    if m['subj']: return m['subj']
    for k,v in SUBJ.items():
        if m['src'].startswith(k): return v
    return ''
for m in M:
    if m['when'].strftime('%Y-%m-%d %H:%M')=='2026-08-31 10:59': m['to']='Chloe Taylor'; m['cc']='Jacqui Roberts; Emily Petering (Together Qld)'
    if m['when'].strftime('%Y-%m-%d %H:%M')=='2026-08-13 16:42': m['frm']='Jacqui Roberts (via LBH Injury Management) — recall notice'
    if not m['to'] and m['when'].strftime('%Y-%m-%d')=='2026-07-13' and m['frm'].startswith('Cory'): m['to']='LBH Injury Management'
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3)
SM=PS('sm',fontName='Helvetica',fontSize=8,leading=10); SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8,leading=10)
B=PS('b',fontName='Helvetica',fontSize=9,leading=11.6); MH=PS('mh',fontName='Helvetica-Bold',fontSize=10.5,leading=13)
HD=PS('hd',fontName='Helvetica',fontSize=8.6,leading=10.8,textColor=colors.HexColor('#333333'))
buf=io.BytesIO()
doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=15*mm,bottomMargin=14*mm,title='',author='')
s=[P('THE CORRESPONDENCE, MESSAGE BY MESSAGE — 2 JULY TO 3 SEPTEMBER 2026',H1),
   P('Cory Shepherd (388372), AO3, Switchboard Services, Logan Hospital · every email reproduced once, in date order, from the original exports · compiled 3 September 2026',SM),Spacer(1,4),
   P('Each message appears once, in the form it was sent. Quoted copies repeated inside later threads have been removed. Standard email boilerplate (external-sender banners, disclaimers, acknowledgements, app footers) has been omitted; nothing else has been altered. Text messages are not included.',B),Spacer(1,6)]
rows=[[P('<b>#</b>',SMB),P('<b>When</b>',SMB),P('<b>From</b>',SMB),P('<b>To</b>',SMB),P('<b>Subject</b>',SMB)]]
for i,m in enumerate(M,1):
    rows.append([P(str(i),SM),P(m['when'].strftime('%a %d %b, %H:%M'),SM),P(escape(m['frm']),SM),P(escape(re.sub(r'<.*?>','',m['to']))[:60],SM),P(escape(subj(m))[:95],SM)])
t=Table(rows,colWidths=[8*mm,28*mm,42*mm,40*mm,58*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),
 ('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),('TOPPADDING',(0,0),(-1,-1),1.6),('BOTTOMPADDING',(0,0),(-1,-1),1.6)]))
s.append(t); s.append(PageBreak())
for i,m in enumerate(M,1):
    hdr=[P(f'{i}.  {m["when"]:%A %d %B %Y, %H:%M}',MH),
         P(f'<b>From:</b> {escape(m["frm"])}',HD), P(f'<b>To:</b> {escape(re.sub(r"<.*?>","",m["to"]).strip() or "—")}',HD)]
    if m['cc']: hdr.append(P(f'<b>Cc:</b> {escape(re.sub(r"<.*?>","",m["cc"]).strip())}',HD))
    hdr.append(P(f'<b>Subject:</b> {escape(subj(m))}',HD))
    hdr.append(Spacer(1,3))
    s.append(KeepTogether(hdr))
    for ln in m['body']:
        s.append(P(escape(ln) if ln.strip() else '&nbsp;',B))
    s.append(Spacer(1,6)); s.append(P('— end of message —',SM)); s.append(PageBreak())
doc.build(s); buf.seek(0)
pdf=pikepdf.open(buf)
with pdf.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out='out/CORRESPONDENCE_THREAD_reproduced_2JUL-3SEP2026.pdf'; pdf.save(out); print('pages',len(pdf.pages),'messages',len(M))
