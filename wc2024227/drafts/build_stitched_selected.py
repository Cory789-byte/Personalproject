import io, re, pickle, pikepdf, sys
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, PageBreak, KeepTogether
S='/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/thread'
M=pickle.load(open(f'{S}/messages.pkl','rb'))
SEL=[1,3,4,6,9,13,19,28,31,32,33,34,35,36,39,40,41]
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3); B=PS('b',fontName='Helvetica',fontSize=9.2,leading=12)
SM=PS('sm',fontName='Helvetica',fontSize=8.4,leading=10.6); MH=PS('mh',fontName='Helvetica-Bold',fontSize=10.5,leading=13); HD=PS('hd',fontName='Helvetica',fontSize=8.6,leading=10.8,textColor=colors.HexColor('#333333'))
SUBJ={1:'Cory - ECC/Leave Type',3:'RE: Cory - ECC/Leave Type',4:'Re: Cory - ECC/Leave Type',6:'Re: Cory Shepherd_ECC further information (MSH-INJ-5795)',9:'Re: Cory Shepherd_ECC further information (MSH-INJ-5795)',13:'Response to 2-15 July 2026 correspondence - incorrect application of EB12, Award and QH policies (MSH-INJ-5795)',19:'Stage 1 — roster, leave and pay (MSH-INJ-5795)',28:'Re: Follow up on Enquiries',31:'Re: Follow up on Enquiries',32:'Cory Shepherd (388372) — application for long service leave and annual leave, and request for AVAC to be processed today',33:'RE: (as above)',34:'Re: (as above)',35:'Re: (as above)',36:'RE: (as above)',39:'Cory Shepherd (388372) RE: Please respond to Chloe Taylor regarding long service leave and why it can not be actioned',40:'RE: (as above)',41:'RE: (as above)'}
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=15*mm,title='',author='')
s=[P('THE EMAILS — LEAVE REQUESTED FROM 3 JULY 2026, AND THE ELIGIBILITY EXCHANGE OF 2–3 SEPTEMBER',H1),
   P('Cory Shepherd (388372) · seventeen emails, each reproduced once as sent, in date order · standard email boilerplate omitted, nothing else altered · 3 September 2026',SM),Spacer(1,6)]
for n in SEL:
    m=M[n-1]; s.append(P(f'{n}.  {m["when"]:%a %d %b %Y, %H:%M} — {escape(m["frm"])} → {escape(re.sub(r"<.*?>","",m["to"]).strip()[:48])}',SM))
s.append(PageBreak())
for n in SEL:
    m=M[n-1]; hdr=[P(f'{n}.  {m["when"]:%A %d %B %Y, %H:%M}',MH),P(f'<b>From:</b> {escape(m["frm"])}',HD),P(f'<b>To:</b> {escape(re.sub(r"<.*?>","",m["to"]).strip() or "—")}',HD)]
    if m['cc']: hdr.append(P(f'<b>Cc:</b> {escape(re.sub(r"<.*?>","",m["cc"]).strip())}',HD))
    hdr.append(P(f'<b>Subject:</b> {escape(SUBJ[n])}',HD)); hdr.append(Spacer(1,3)); s.append(KeepTogether(hdr))
    for ln in m['body']: s.append(P(escape(ln) if ln.strip() else '&nbsp;',B))
    s.append(Spacer(1,5)); s.append(P('— end of message —',SM)); s.append(Spacer(1,8))
doc.build(s); buf.seek(0); out=pikepdf.open(buf)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
out.save('out/EMAILS_leave_requests_from_3JUL_and_eligibility_3SEP2026.pdf'); print('pages',len(out.pages))
