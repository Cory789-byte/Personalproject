import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle

H1=PS('h1',fontName='Helvetica-Bold',fontSize=11.5,leading=14,spaceAfter=2)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=8.6,leading=10.5,spaceBefore=6,spaceAfter=2)
SM=PS('sm',fontName='Helvetica',fontSize=7.2,leading=8.8)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=7.2,leading=8.8)
TINY=PS('t',fontName='Helvetica',fontSize=6.8,leading=8.4)

# (date, event, source)  — every row traceable. Nothing inferred.
ROWS=[
 ('26 Oct 2022','General-practice record. "ADHD" and "Anxiety" appear in the Past Medical History list carried in the referral of 16 May 2024.','GP records, Our Medical Ashmore'),
 ('16 Nov 2023','General-practice consultation, Dr Nanayakkara.','GP records'),
 ('14 Jan 2024','A family matter concerning my sister, then 15, attended at police direction. Not an intimate-partner matter. My line manager was told that morning.','My account; manager’s reply in the record'),
 ('20–27 Feb 2024','Period of leave, later the subject of a dispute about whether attachments had been supplied. The Respondent now records "a review indicates that in fact, the attachments were present" and "a matter of human error".','Respondent’s document, 13 May 2026, 14(e), 14(f)'),
 ('17–18 Mar 2024','Rostered to finish at 23:00 and to commence at 06:00 — a break of 7 hours. The fatigue policy and the Award require a minimum of 10 hours, or 8 by written agreement. MET calls were recorded over that period.','Accepted — schedule A items 1 and 3; Chief Executive’s letter, 5 Jun 2026'),
 ('19 Mar 2024','Leave taken, paid.','Accepted — Respondent’s document, 22(c)'),
 ('15 Apr 2024','A change to Switchboard working arrangements communicated to operators by email. The Respondent lists no document recording consultation before it.','Respondent’s amended List of Documents, 14 Aug 2026'),
 ('3 May 2024','Payroll instructed to correct the shifts.','Accepted — schedule A item 40'),
 ('16 May 2024','General practice renewed the psychiatric referral.','GP records'),
 ('21 May 2024','"I am waiting payroll confirmation."','Accepted — schedule A item 46'),
 ('28 May 2024','The correction was submitted — 8 weeks after the shifts.','Accepted — schedule A item 41'),
 ('<b>18 Jun 2024</b>','<b>Onset of the injury, as pleaded in the appeal.</b>','Form 9A, as pleaded'),
 ('28 Jun 2024','General-practice consultation, Dr Slawinski.','GP records'),
 ('30 Jun 2024','Fatigue risk management assessment was implemented at Logan Hospital Switchboard only after this date. No fatigue risk management training records or register entries exist for the position, such training applying only to health practitioners and clinical assistants.','Chief Executive’s letter, 5 Jun 2026'),
 ('1 Jul 2024','General-practice consultation, Dr Hawes. Application for compensation lodged with WorkCover Queensland.','GP records; WorkCover file'),
 ('12 Jul 2024','"Event overview" provided by me to WorkCover Queensland.','Respondent’s List of Documents, item 12'),
 ('8 Sep 2024','Workers’ compensation medical certificate signed by Dr Hawes.','Certificate'),
 ('13 Sep 2024','WorkCover Queensland rejected the application for compensation.','WorkCover reasons, 13 Sep 2024'),
 ('20 Sep 2024','Separation date nominated by the employer in the agreement later executed.','Deed, recital D'),
 ('late Sep / early Oct 2024','My grandfather died. <b>Exact date to be confirmed — see the note at the foot.</b>','To be confirmed'),
 ('9 Oct 2024','Correspondence from the Acting Executive Director treating the employment as abandoned was forwarded to me at 4:10 pm. I replied in writing.','Employer correspondence, 9 Oct 2024'),
 ('<b>24 Oct 2024</b>','<b>First consultation with Dr Krishnaiah. My partner attended that consultation with me.</b> The Regulator’s review decision issued the same day.','Your file; Review Decision 69983'),
 ('13 Feb 2025','Dr Krishnaiah’s report to QSuper. It records workplace stress arising from management and rostering, and refers to relationship breakdown, job loss and bereavement.','Your file'),
 ('Feb – Mar 2025','My relationship with my partner ended.','My account'),
 ('21 Feb 2025','The agreement with the employer was executed.','Deed'),
 ('3 Jul 2026','Employee Capability Checklist completed by the employer. It identifies three stressors for the position — complaint handling; being held accountable and blamed for the failures of others; unpredictable rostering.','Employee Capability Checklist'),
]

def tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#aaaaaa')),
      ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#ececec')),('VALIGN',(0,0),(-1,-1),'TOP'),
      ('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),
      ('TOPPADDING',(0,0),(-1,-1),1.8),('BOTTOMPADDING',(0,0),(-1,-1),1.8)])); return t

s=[P('CHRONOLOGY — FOR EASE OF REFERENCE ONLY, NOT A SUBMISSION',H1),
   P('Cory Shepherd, date of birth 11 January 1991 · WC/2024/227 · prepared 4 September 2026. '
     'This page records dated events and where each is recorded. It draws no conclusion from any of them, '
     'and it is not intended to bear on your opinion. Where the record is unclear or a date is not '
     'established, that is said so in terms rather than estimated.',TINY),
   Spacer(1,4)]
r=[[P('<b>Date</b>',SMB),P('<b>Event</b>',SMB),P('<b>Where it is recorded</b>',SMB)]]
for a,b,c in ROWS: r.append([P(a,SM),P(b,SM),P(c,SM)])
s.append(tbl(r,[26*mm,102*mm,42*mm]))

s.append(P('MATTERS NOT ESTABLISHED, AND MATTERS I CANNOT DATE',H2))
r=[[P('<b>Item</b>',SMB),P('<b>Position</b>',SMB)]]
for a,b in [
 ('The date of my grandfather’s death','Not established from any document I hold. It was in or about the period covered by the leave immediately before the correspondence of 9 October 2024. I have not estimated it. If it matters to your answer, it may be in your own file or the general-practice record.'),
 ('Any psychological diagnosis before 24 October 2024','No psychological or psychiatric diagnosis is recorded in the material I hold as at any date before 24 October 2024. The general-practice record of 26 October 2022 lists "ADHD" and "Anxiety" in a past medical history; I make no assertion about what that entry represents.'),
 ('The separation date','The documents differ. The agreement records 20 September 2024; an earlier filing of mine records 8 October 2024; the correspondence treating the employment as abandoned was sent on 9 October 2024. All three fall after 18 June 2024. I have not resolved the difference and nothing here depends on it.'),
 ('Physical health matters arising later','Matters arising in 2026 are not included here. They are not within the three questions and I have not asked you to address them.'),
 ('The order of events after the onset','The relationship ending, the loss of the job and the bereavement are each recorded above at the date the record gives. I draw no conclusion from the order and leave that entirely to you.')]:
    r.append([P(a,SM),P(b,SM)])
s.append(tbl(r,[38*mm,132*mm]))
s.append(Spacer(1,3))
s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com',TINY))

buf=io.BytesIO()
SimpleDocTemplate(buf,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=13*mm,
                  bottomMargin=12*mm,title='',author='').build(s)
buf.seek(0)
d=pikepdf.open(buf)
out=pikepdf.new(); out.pages.extend(d.pages)
with out.open_metadata() as md:
    for x in list(md): del md[x]
for x in list(out.docinfo.keys()): del out.docinfo[x]
for x in ('/Metadata','/PieceInfo','/Lang'):
    if x in out.Root: del out.Root[x]
for pg in out.pages:
    for x in ('/Metadata','/PieceInfo'):
        if x in pg.obj: del pg.obj[x]
out.save('out/SHEPHERD_03_Chronology_4Sep2026.pdf',fix_metadata_version=False)
print('chronology pages:',len(out.pages))
