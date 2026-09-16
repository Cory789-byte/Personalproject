import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle
H1=PS('h1',fontName='Helvetica-Bold',fontSize=11.5,leading=14,spaceAfter=2)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=8.8,leading=11,spaceBefore=7,spaceAfter=2)
SM=PS('sm',fontName='Helvetica',fontSize=7.1,leading=8.7)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=7.1,leading=8.7)
TINY=PS('t',fontName='Helvetica',fontSize=6.8,leading=8.4)
def tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#aaaaaa')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#ececec')),
      ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),
      ('TOPPADDING',(0,0),(-1,-1),1.6),('BOTTOMPADDING',(0,0),(-1,-1),1.6)])); return t
def R(a,b): return [P(a,SM),P(b,SM)]
s=[P('WHERE THE MATERIAL SITS AGAINST THE THREE MATTERS IN ISSUE',H1),
   P('Cory Shepherd · WC/2024/227 · accompanying my email of 4 September 2026 · the three matters are those written on the Notice of Non-Party Disclosure requested by the Workers\' Compensation Regulator and sealed 4 July 2025, a copy of which is enclosed again with this page.',TINY),
   Spacer(1,3),
   P('This page locates material already provided with my letter of 17 August 2026. It is a finding aid only. It makes no submission about what any item shows, and nothing in it is intended to bear on your opinion. Attachment and schedule references are to that letter and its schedule of assumed facts.',TINY),
   Spacer(1,4)]

s.append(P('MATTER 1 — DID MR SHEPHERD SUSTAIN A PERSONAL INJURY?',H2))
rows=[[P('<b>Material</b>',SMB),P('<b>Where</b>',SMB)]]
for a,b in [
 ('Your own clinical file for me, from 24 October 2024','Attachment 4'),
 ('Your report of 13 February 2025','Attachment 4d'),
 ('General-practice records, Our Medical Ashmore — including the entries of 26.10.2022 ("ADHD", "Anxiety", in the Past Medical History list of the referral of 16.05.2024); 16.11.2023 (Dr Nanayakkara); 16.05.2024 (renewal of psychiatric referral); 28.06.2024 (Dr Slawinski); 01.07.2024 (Dr Hawes)','Attachment 4a · schedule E'),
 ('Workers\' compensation medical certificate of Dr Hawes, signed 8 September 2024','Attachment 4b'),
 ('Employee Capability Checklist, 3 July 2026','Attachment 4c'),
 ('The Regulator accepts that your report of 13 February 2025 states Major Depressive Disorder — as what the report says; its accuracy is not accepted','schedule A item 38'),
 ('The Regulator does not accept the accuracy of the entry of 16 November 2023, and asserts a past medical history of anxiety and ADHD from 26 October 2022','schedule B items 34, 35')]:
    rows.append(R(a,b))
s.append(tbl(rows,[126*mm,44*mm]))

s.append(P('MATTER 2 — DID THE INJURY ARISE OUT OF, OR IN THE COURSE OF, THE EMPLOYMENT?',H2))
rows=[[P('<b>Material</b>',SMB),P('<b>Where</b>',SMB)]]
for a,b in [
 ('The requirements of the position as the employer describes them — continuous shift work over the full 24-hour period, 7 days a week; participation in the Emergency Response process "strictly adhering to protocols and timeframes"; "maintain call queues to minimum at all times"; multitasking and operating under pressure with "high volume call traffic"; judgement "in situations where precedence have not been set and procedures not defined"; "limited supervision"','Attachment 3 · schedule D'),
 ('Accepted: on 17–18 March 2024 rostered to finish at 23:00 and commence at 06:00 — a break of 7 hours','schedule A item 1'),
 ('Accepted: the fatigue policy and the Award require a minimum of 10 hours, or 8 hours by written agreement','schedule A item 3'),
 ('The Regulator\'s document of 13 May 2026: "only a 7-hour break (rather than an 8-hour break) … a result of human error and not intentional or repeated"; and that leave was taken on 19 March 2024, paid','schedule A2 22(a), 22(c)'),
 ('Recorded by the Chief Executive: the requested fatigue risk management training records and register entries do not exist, such training applying only to health practitioners and clinical assistants; and fatigue risk management assessment at that Switchboard was implemented only after 30 June 2024','Attachment 2 · schedule C items 4, 5, 7'),
 ('Recorded by the Chief Executive: a spreadsheet of recorded MET calls is available for the period 17–18 March 2024; and employee complaints about operational errors are "managed solely via email or verbally with the complainant"','schedule C items 1–2, 3(a)'),
 ('Accepted: Ms Reese, 7 August 2023 — "a rostering error that was accidentally made by Chloe with regards to night shifts"','schedule A item 5'),
 ('Accepted: maintaining accurate contact details for medical staff is "a critical function of the Switchboard to ensure effective clinical handover and patient safety"','schedule A item 8'),
 ('The Regulator\'s document of 13 May 2026 on the leave of 20–27 February 2024: "a review indicates that in fact, the attachments were present"; "a matter of human error"','schedule A2 14(e), 14(f)'),
 ('Accepted: payroll instruction to correct the shifts issued 3 May 2024; "I am waiting payroll confirmation" 21 May 2024; correction submitted 28 May 2024','schedule A items 40, 46, 41'),
 ('Changes to working hours approved during 2026 by Mr Hughes as delegate — 27 February, 17 April, 9 June','Attachment 5 · schedule F'),
 ('The three stressors identified in the Employee Capability Checklist of 3 July 2026 — complaint handling; being held accountable and blamed for the failures of others; unpredictable rostering','Attachment 4c')]:
    rows.append(R(a,b))
s.append(tbl(rows,[126*mm,44*mm]))

s.append(P('MATTER 3 — WAS THE EMPLOYMENT A SIGNIFICANT CONTRIBUTING FACTOR TO THE INJURY?',H2))
rows=[[P('<b>Material</b>',SMB),P('<b>Where</b>',SMB)]]
for a,b in [
 ('All of the material listed above','Matters 1 and 2'),
 ('Your report of 13 February 2025 referred to multiple life stressors including relationship breakdown, job loss and bereavement','Attachment 4d'),
 ('Your clinical relationship with me began on 24 October 2024, and my partner attended that consultation with me. Each of those matters arose while I was under your care and is recorded in your own file','Attachment 4'),
 ('The sequence, from sources other than my account: onset pleaded at or about 18 June 2024 · application for compensation lodged 1 July 2024 · rejected 13 September 2024 · correspondence as to abandonment 8 October 2024 · review decision 24 October 2024 · your report 13 February 2025 · reinstatement effective 20 September 2024, agreement executed 21 February 2025 · Employee Capability Checklist 3 July 2026','schedules A, B, C · Attachments 4, 5')]:
    rows.append(R(a,b))
s.append(tbl(rows,[126*mm,44*mm]))
s.append(Spacer(1,4))
s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com',TINY))

buf=io.BytesIO()
doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=13*mm,bottomMargin=12*mm,title='',author='')
doc.build(s); buf.seek(0)
out=pikepdf.open(buf)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/LOCATOR_three_matters_4SEP2026.pdf',fix_metadata_version=False)
print('pages',len(out.pages))
