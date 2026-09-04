# Chronology content, shared by the standalone PDF and the bundle.
# J(key) -> link markup when rendering inside the bundle; plain text standalone.
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import Paragraph as P, Spacer, Table, TableStyle, PageBreak

H1=PS('c_h1',fontName='Helvetica-Bold',fontSize=11.5,leading=14,spaceAfter=2)
H2=PS('c_h2',fontName='Helvetica-Bold',fontSize=8.6,leading=10.5,spaceBefore=6,spaceAfter=2)
SM=PS('c_sm',fontName='Helvetica',fontSize=6.9,leading=8.2)
SMB=PS('c_smb',fontName='Helvetica-Bold',fontSize=6.9,leading=8.2)
TINY=PS('c_t',fontName='Helvetica',fontSize=6.4,leading=7.8)

# (date, event, source-text, doc-key or None)
ROWS=[
 ('17 Jun 2020','I signed a written agreement permitting a minimum break of 8 hours between shifts instead of 10. Whether it applied to rostered shifts is disputed.','Agreement, 17 Jun 2020',None),
 ('26 Oct 2022','General-practice record. "ADHD" and "Anxiety" appear in the Past Medical History list carried in the referral of 16 May 2024.','General-practice records','A4a'),
 ('16 Nov 2023','General-practice consultation, Dr Priyal De Silva Nanayakkara. The note records: "Poor sleep. Shift work. Takes melatonin 2 mg to help to go to sleep … but does not help much. <b>Cannot work/ do shifts if he does not get a good sleep.</b> … <b>No psycological illness such as depression/ psycosis. mood good.</b>" Melatonin and temazepam prescribed. (Spelling as in the record.)','General-practice records','A4a'),
 ('20–27 Feb 2024','Leave declined for want of an attached statutory declaration. The Respondent now records "a review indicates that in fact, the attachments were present" and "a matter of human error".','Schedule, 14(e), 14(f)','SCH'),
 ('17–18 Mar 2024','Rostered to finish at 23:00 and to commence at 06:00 — a break of 7 hours. The fatigue policy and the Award require a minimum of 10 hours, or 8 by written agreement. MET calls were recorded over that period.','Accepted — schedule items 1, 3','SCH'),
 ('19 Mar 2024','<b>The day after those shifts I was absent, and I funded it myself.</b> The employer’s own leave record shows 7.60 hours of Sick Leave, approved. Paid fatigue leave was not provided; the Regulator’s own pleaded case is that no fatigue leave was available under cl 18.10 of the Award, no overtime having been performed.','Employer leave record; Regulator’s pleading 24(b); accepted — schedule 22(c)','SCH'),
 ('15 Apr 2024','A change to Switchboard working arrangements communicated by email. The Respondent lists no document recording consultation before it.','Respondent’s List of Documents',None),
 ('3 May 2024','Payroll instructed to correct the shifts.','Accepted — schedule item 40','SCH'),
 ('16 May 2024','General-practice note records "renew referral to psychiatrist".','General-practice records','A4a'),
 ('21 May 2024','"I am waiting payroll confirmation."','Accepted — schedule item 46','SCH'),
 ('28 May 2024','The correction was submitted — 8 weeks after the shifts.','Accepted — schedule item 41','SCH'),
 ('<b>10 Jun 2024</b>','<b>My great-grandfather, George Stevens Boland, died at Moree in his ninety-third year</b> (born 27 March 1932). Eight days before the onset pleaded below.','Family record',None),
 ('11–12 Jun 2024','Bereavement leave, 15.2 hours, approved — the only bereavement leave recorded in my employment across five and a half years.','Employer leave record',None),
 ('17 Jun 2024 onwards','Leave without pay, every rostered day from 17 June onwards.','Employer leave record',None),
 ('<b>18 Jun 2024</b>','<b>Onset of the injury, as pleaded in the appeal.</b>','Form 9A, as pleaded',None),
 ('28 Jun 2024','General-practice consultation, Dr Bogdan Slawinski. Reason for visit recorded as "Anxiety". The note records "wants melatonin, to help to sleep … <b>stress at work</b> … upset by people not following rules".','General-practice records','A4a'),
 ('30 Jun 2024','Fatigue risk management assessment was implemented at Logan Hospital Switchboard only after this date. No fatigue risk management training records or register entries exist for the position, such training applying only to health practitioners and clinical assistants.','Chief Executive’s letter, 5 Jun 2026','A2'),
 ('1 Jul 2024','General-practice consultation, Dr Peter Hawes. Reason for visit "<b>work stress</b>". The note records "ethical complaint about manager and director … been there 5 years … they withhold pay at times, no overtime- not processed, <b>manipulate his roster- so he works lates then earlies</b> … all this is stressing him out, causing anxiety". Application for compensation lodged the same day.','General-practice records','A4a'),
 ('12 Jul 2024','"Event overview" provided by me to WorkCover Queensland.','Respondent’s List of Documents, item 12',None),
 ('8 Sep 2024','Workers’ compensation medical certificate signed by Dr Hawes.','Medical certificate','A4b'),
 ('Sep 2024','<b>Referred to Dr Krishnaiah by Dr Hawes.</b>','Referral, Dr Hawes',None),
 ('13 Sep 2024','WorkCover Queensland rejected the application for compensation.','WorkCover reasons, 13 Sep 2024',None),
 ('20 Sep 2024','Separation date nominated by the employer in the agreement later executed.','Deed, recital D',None),
 ('<b>8/9 Oct 2024</b>','<b>Dismissal.</b> The letter from the Acting Executive Director treating the employment as abandoned. It was forwarded to me at 4:10 pm on 9 October 2024; my own earlier filing gives the date as 8 October. I replied in writing.','Employer letter, 8/9 Oct 2024',None),
 ('<b>24 Oct 2024</b>','<b>First consultation with Dr Krishnaiah. My partner attended that consultation with me.</b>','Your file',None),
 ('<b>24 Oct 2024</b>','<b>The review confirmed the rejection</b> — Review Decision 69983, issued the same day; the appointment was that day and the decision arrived after it. In doing so the reviewer determined that I "sustained a personal injury of a psychological nature", that my injury "arose out of employment … where employment was a significant contributing factor", and that the rostering of the 17 and 18 March 2024 shifts "amounted to unreasonable management action". The rejection was confirmed on the statutory exclusion alone, on a global evaluation of the management action.','Review Decision 69983, pp. 26–27',None),
 ('13 Feb 2025','Dr Krishnaiah’s report to QSuper. It records workplace stress arising from management and rostering, and refers to relationship breakdown, job loss and bereavement.','Your file',None),
 ('Feb – Mar 2025','My relationship with my partner ended.','My account',None),
 ('<b>11 Jan 2025</b>','<b>My great-grandmother, Gwendoline Zena Boland (born Johnston), died</b> seven days after her ninety-fourth birthday (born 4 January 1931). Seven months and a day after her husband. It was my own birthday.','Family record',None),
 ('21 Feb 2025','The agreement with the employer was executed.','Deed',None),
 ('1 Jul 2025','<b>After the onset.</b> Fatigue leave I had submitted was declined in writing: "I have just checked MyHR and noticed your leave has been submitted as Fatigue leave … I have declined this please submit correct leave either S/L or A/L."','Email, Ms Taylor, 1 Jul 2025',None),
 ('3 Jul 2026','Employee Capability Checklist completed by the employer. It identifies three stressors for the position — complaint handling; being blamed for the failures of others; unpredictable rostering.','Capability Checklist','A4c'),
]

NOTES=[
 ('A date I cannot give','The day of Dr Hawes’ referral in September 2024. I have not estimated it; your own file or the general-practice record may show it.'),
 ('Any psychological diagnosis before 24 October 2024','None is recorded in the material I hold. The general-practice record of 26 October 2022 lists "ADHD" and "Anxiety" in a past medical history; I make no assertion about what that entry represents.'),
 ('The separation date','The documents differ — the agreement records 20 September 2024, an earlier filing of mine 8 October, the abandonment correspondence 9 October. All three fall after 18 June 2024. I have not resolved the difference and nothing here depends on it.'),
 ('What is left out','Physical health matters arising in 2026 — not within the three questions. The two deaths, the relationship ending and the loss of the job all appear above at the dates the record gives. I draw no conclusion from their order or their weight, and question 4 of my email asks you to address them.'),
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
    s.append(PageBreak())
    s.append(P('MATTERS NOT ESTABLISHED, AND MATTERS I CANNOT DATE',H2))
    r=[[P('<b>Item</b>',SMB),P('<b>Position</b>',SMB)]]
    for a,b in NOTES: r.append([P(a,SM),P(b,SM)])
    s.append(_tbl(r,[38*mm,132*mm]))
    if jumpbar:
        s.append(Spacer(1,3)); s.append(jumpbar())
    s.append(Spacer(1,3))
    s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com',TINY))
    return s
