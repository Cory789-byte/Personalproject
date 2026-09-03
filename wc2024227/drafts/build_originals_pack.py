import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle
C='../documents/correspondence-2026'
ITEMS=[ # (original file, emails it contains (reproduction numbers), description)
 (C+'/2026-07-03_1518_Cory_to_Taylor_ECC_LeaveType_reply.pdf','1, 3, 4','2–3 Jul 2026 — Taylor ↔ Shepherd, "Cory - ECC/Leave Type": 2 Jul 2:38 pm sick-leave default; 3 Jul 2:49 pm "Sick leave / Sick leave no pay"; 3 Jul 3:18 pm ANNUAL LEAVE confirmed'),
 (C+'/2026-07_Cory_to_InjuryMgmt_ECC_further_information_FULL_THREAD_12pp.pdf','6, 9','7–13 Jul 2026 — Forrest / Injury Management ↔ Shepherd, "ECC further information (MSH-INJ-5795)": 10 Jul 8:35 am paid time, not leave; 13 Jul 4:39 pm "I ask again"'),
 (C+'/2026-07-28_1739_Cory_to_HR_incorrect_application_EB12_Award_policies.pdf','13','28 Jul 2026, 5:39 pm — Shepherd → Injury Management (cc union): incorrect application of EB12, Award and QH policies; special leave applied for (point 4); coding contested'),
 (C+'/2026-08-05_0730_SENT_Stage1_reply_cover_email.pdf','19','5 Aug 2026, 7:30 am — Shepherd → Taylor / Injury Management: Stage 1 reply; recreation leave not consented to; special leave on full pay asked for instead'),
 (C+'/2026-08-18_to_28_Roberts_FollowUpOnEnquiries_FULL_THREAD.pdf','28, 31','18–28 Aug 2026 — Roberts ↔ Shepherd (cc Petering), "Follow up on Enquiries": 24 Aug 11:13 am leave to be applied and AVAC submitted; 28 Aug 2:18 pm AVAC update sought'),
 (C+'/2026-09-03_1027_Taylor_Payroll_LSL_eligibility_04SEP_thread_2-3Sep.pdf','32, 33, 34, 35, 36, 39, 40, 41','31 Aug – 3 Sep 2026 — Shepherd ↔ Taylor ↔ Payroll (cc Roberts, Petering): 31 Aug 10:59 am application (LSL from 13 Jul, A/L on exhaustion, AVAC today, under protest); 3:34 pm one fortnight at "0.5 FTE"; 4:06 pm correction; 2 Sep 11:07 am ad hoc payment; 12:42 pm "paid 9 September"; 4:16 pm process 24926366; 3 Sep 9:05 am Payroll "eligibility 04/09/2026"; 10:27 am "cannot be processed prior to 9 September"'),
]
H1=PS('h1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=3); SM=PS('sm',fontName='Helvetica',fontSize=8.2,leading=10.2); SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8.2,leading=10.2); B=PS('b',fontName='Helvetica',fontSize=9,leading=11.5)
srcs=[pikepdf.open(f) for f,_,_ in ITEMS]; counts=[len(s.pages) for s in srcs]
buf=io.BytesIO(); doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=15*mm,bottomMargin=14*mm,title='',author='')
s=[P('THE ORIGINAL EMAILS — LEAVE REQUESTED FROM 3 JULY 2026, AND THE ELIGIBILITY EXCHANGE OF 2–3 SEPTEMBER',H1),
   P('Cory Shepherd (388372) · six original email documents as sent or received, in date order, containing the seventeen emails referred to · nothing retyped · 3 September 2026',SM),Spacer(1,5),
   P('Each tab is the original document. Where an original is a thread, the earlier emails appear beneath the later ones in the usual way. The "Email" column gives the number used for that email in the covering email and in the numbered reproduction that follows this section.',B),Spacer(1,6)]
rows=[[P('<b>Tab</b>',SMB),P('<b>Email</b>',SMB),P('<b>What it is</b>',SMB),P('<b>Pages</b>',SMB)]]
pg=2
for i,((f,nums,desc),n) in enumerate(zip(ITEMS,counts),1):
    rows.append([P(str(i),SM),P(nums,SM),P(desc,SM),P(f'{pg}–{pg+n-1}',SM)]); pg+=n
t=Table(rows,colWidths=[9*mm,22*mm,131*mm,16*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t); s.append(Spacer(1,6)); s.append(P(f'Total: {sum(counts)+1} pages including this index.',SM))
doc.build(s); buf.seek(0); idx=pikepdf.open(buf); assert len(idx.pages)==1
out=pikepdf.new(); out.pages.extend(idx.pages)
for sp in srcs: out.pages.extend(sp.pages)
def scrub(pdf):
    with pdf.open_metadata() as md:
        for k in list(md): del md[k]
    for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
    r=pdf.Root
    for k in ('/Metadata','/PieceInfo','/Lang'):
        if k in r: del r[k]
    if '/Names' in r and '/EmbeddedFiles' in r.Names: del r.Names['/EmbeddedFiles']
    for pg in pdf.pages:
        for k in ('/Metadata','/PieceInfo'):
            if k in pg.obj: del pg.obj[k]
scrub(out)
out.save('out/EMAILS_ORIGINALS_leave_requests_from_3JUL_3SEP2026.pdf',fix_metadata_version=False); print('originals pages',len(out.pages),counts)
