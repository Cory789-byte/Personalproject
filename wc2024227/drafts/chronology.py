# Chronology content, shared by the standalone PDF and the bundle.
# J(key) -> link markup when rendering inside the bundle; plain text standalone.
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import Paragraph as P, Spacer, Table, TableStyle

H1=PS('c_h1',fontName='Helvetica-Bold',fontSize=11.5,leading=14,spaceAfter=2)
H2=PS('c_h2',fontName='Helvetica-Bold',fontSize=8.6,leading=10.5,spaceBefore=6,spaceAfter=2)
SM=PS('c_sm',fontName='Helvetica',fontSize=6.9,leading=8.2)
SMB=PS('c_smb',fontName='Helvetica-Bold',fontSize=6.9,leading=8.2)
TINY=PS('c_t',fontName='Helvetica',fontSize=6.4,leading=7.8)

# (date, event, source-text, doc-key or None)
ROWS=[
 ('26 Oct 2022','General-practice record. "ADHD" and "Anxiety" appear in the Past Medical History list carried in the referral of 16 May 2024.','General-practice records','A4a'),
 ('16 Nov 2023','General-practice consultation, Dr Nanayakkara.','General-practice records','A4a'),
 ('14 Jan 2024','A family matter concerning my sister, then 15, attended at police direction. Not an intimate-partner matter. My line manager was told that morning.','My account; manager’s reply in the record',None),
 ('20–27 Feb 2024','Period of leave, later the subject of a dispute about whether attachments had been supplied. The Respondent now records "a review indicates that in fact, the attachments were present" and "a matter of human error".','Schedule of assumed facts, 14(e), 14(f)','SCH'),
 ('17–18 Mar 2024','Rostered to finish at 23:00 and to commence at 06:00 — a break of 7 hours. The fatigue policy and the Award require a minimum of 10 hours, or 8 by written agreement. MET calls were recorded over that period.','Accepted — schedule items 1, 3','SCH'),
 ('19 Mar 2024','Leave taken, paid.','Accepted — schedule 22(c)','SCH'),
 ('15 Apr 2024','A change to Switchboard working arrangements communicated to operators by email. The Respondent lists no document recording consultation before it.','Respondent’s List of Documents, 14 Aug 2026',None),
 ('3 May 2024','Payroll instructed to correct the shifts.','Accepted — schedule item 40','SCH'),
 ('16 May 2024','General-practice note records "renew referral to psychiatrist".','General-practice records','A4a'),
 ('21 May 2024','"I am waiting payroll confirmation."','Accepted — schedule item 46','SCH'),
 ('28 May 2024','The correction was submitted — 8 weeks after the shifts.','Accepted — schedule item 41','SCH'),
 ('<b>18 Jun 2024</b>','<b>Onset of the injury, as pleaded in the appeal.</b>','Form 9A, as pleaded',None),
 ('28 Jun 2024','General-practice consultation, Dr Slawinski.','General-practice records','A4a'),
 ('30 Jun 2024','Fatigue risk management assessment was implemented at Logan Hospital Switchboard only after this date. No fatigue risk management training records or register entries exist for the position, such training applying only to health practitioners and clinical assistants.','Chief Executive’s letter, 5 Jun 2026','A2'),
 ('1 Jul 2024','General-practice consultation, Dr Hawes. Application for compensation lodged with WorkCover Queensland.','General-practice records','A4a'),
 ('12 Jul 2024','"Event overview" provided by me to WorkCover Queensland.','Respondent’s List of Documents, item 12',None),
 ('8 Sep 2024','Workers’ compensation medical certificate signed by Dr Hawes.','Medical certificate','A4b'),
 ('Sep 2024','<b>Referred to Dr Krishnaiah by Dr Hawes.</b> The referral document and its exact date are not in my possession — see the note at the foot.','Referral — to be obtained',None),
 ('13 Sep 2024','WorkCover Queensland rejected the application for compensation.','WorkCover reasons, 13 Sep 2024',None),
 ('20 Sep 2024','Separation date nominated by the employer in the agreement later executed.','Deed, recital D',None),
 ('late Sep / early Oct 2024','My grandfather died. <b>Exact date to be confirmed — see the note at the foot.</b>','To be confirmed',None),
 ('<b>9 Oct 2024</b>','<b>Dismissal.</b> The letter from the Acting Executive Director treating the employment as abandoned was forwarded to me at 4:10 pm. I replied in writing.','Employer letter, 9 Oct 2024',None),
 ('<b>24 Oct 2024</b>','<b>First consultation with Dr Krishnaiah. My partner attended that consultation with me.</b>','Your file',None),
 ('<b>24 Oct 2024</b>','<b>The review was rejected</b> — Review Decision 69983 issued the same day, confirming the rejection of the application for compensation. The appointment was that day; the decision arrived after it.','Review Decision 69983',None),
 ('13 Feb 2025','Dr Krishnaiah’s report to QSuper. It records workplace stress arising from management and rostering, and refers to relationship breakdown, job loss and bereavement.','Your file',None),
 ('Feb – Mar 2025','My relationship with my partner ended.','My account',None),
 ('21 Feb 2025','The agreement with the employer was executed.','Deed',None),
 ('3 Jul 2026','Employee Capability Checklist completed by the employer. It identifies three stressors for the position — complaint handling; being held accountable and blamed for the failures of others; unpredictable rostering.','Employee Capability Checklist','A4c'),
]

NOTES=[
 ('The date of my grandfather’s death','Not established from any document I hold. It was in or about the period covered by the leave immediately before the correspondence of 9 October 2024. I have not estimated it. If it matters to your answer, it may be in your own file or the general-practice record.'),
 ('Any psychological diagnosis before 24 October 2024','No psychological or psychiatric diagnosis is recorded in the material I hold as at any date before 24 October 2024. The general-practice record of 26 October 2022 lists "ADHD" and "Anxiety" in a past medical history; I make no assertion about what that entry represents.'),
 ('The date of the referral to your practice','Dr Hawes referred me in September 2024. I do not hold the referral document and cannot give the day. It may be in your own file or the general-practice record.'),
 ('The separation date','The documents differ. The agreement records 20 September 2024; an earlier filing of mine records 8 October 2024; the correspondence treating the employment as abandoned was sent on 9 October 2024. All three fall after 18 June 2024. I have not resolved the difference and nothing here depends on it.'),
 ('Physical health matters arising later','Matters arising in 2026 are not included here. They are not within the three questions and I have not asked you to address them.'),
 ('The order of events after the onset','The relationship ending, the loss of the job and the bereavement are each recorded above at the date the record gives. I draw no conclusion from the order and leave that entirely to you.'),
]

def _tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#aaaaaa')),
      ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#ececec')),('VALIGN',(0,0),(-1,-1),'TOP'),
      ('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),
      ('TOPPADDING',(0,0),(-1,-1),1.8),('BOTTOMPADDING',(0,0),(-1,-1),1.8)])); return t

def flowables(J=None, jumpbar=None):
    """J(key, label) -> markup for a link, or None for a plain chronology."""
    linked = J is not None
    s=[P('CHRONOLOGY — FOR EASE OF REFERENCE ONLY, NOT A SUBMISSION',H1),
       P('Cory Shepherd, date of birth 11 January 1991 · WC/2024/227 · prepared 4 September 2026. '
         'This page records dated events and where each is recorded. It draws no conclusion from any of '
         'them, and it is not intended to bear on your opinion. Where the record is unclear or a date is '
         'not established, that is said so in terms rather than estimated.'
         + (' <b>The page references in the right-hand column are clickable.</b>' if linked else ''),TINY),
       Spacer(1,4)]
    r=[[P('<b>Date</b>',SMB),P('<b>Event</b>',SMB),P('<b>Where it is recorded</b>',SMB)]]
    for date,ev,src,key in ROWS:
        cell = src if not (linked and key) else src+' · '+J(key)
        r.append([P(date,SM),P(ev,SM),P(cell,SM)])
    s.append(_tbl(r,[26*mm,98*mm,46*mm]))
    s.append(P('MATTERS NOT ESTABLISHED, AND MATTERS I CANNOT DATE',H2))
    r=[[P('<b>Item</b>',SMB),P('<b>Position</b>',SMB)]]
    for a,b in NOTES: r.append([P(a,SM),P(b,SM)])
    s.append(_tbl(r,[38*mm,132*mm]))
    if jumpbar:
        s.append(Spacer(1,3)); s.append(jumpbar())
    s.append(Spacer(1,3))
    s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com',TINY))
    return s
