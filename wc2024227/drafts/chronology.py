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
 ('25 Mar 2019','Employment with Metro South commenced — Administration Officer, Switchboard Services, Logan Hospital — <b>as a casual</b>.','Deed, recital B',None),
 ('17 Jun 2020','I signed a written agreement permitting a minimum break of 8 hours instead of 10 — <b>at that time a casual</b>. Whether it survived my move to permanent full-time hours is disputed: the employer’s position, stated on 6 September 2024, is that the change of contracts and adjustments in working hours did not invalidate it.','Agreement, 17 Jun 2020; employer’s response, 6 Sep 2024',None),
 ('26 Oct 2022','General-practice record. "ADHD" and "Anxiety" appear in the Past Medical History list carried in the referral of 16 May 2024.','General-practice records','A4a'),
 ('27 Sep 2023','My line manager approved permanent full-time hours.','Approval email, 27 Sep 2023',None),
 ('<b>16 Oct 2023</b>','<b>Permanent full-time hours commenced</b>, having moved from casual to part-time before this. Continuous shift work across the full 24 hours, seven days a week. <b>I handled roughly 200 to 300 calls per shift</b> — urgent clinical handover, distressed patients and family, callers in conflict or in crisis, and general complaints — and was frequently the first person a caller reached in an emergency. The role description requires participation in the Emergency Response process "strictly adhering to protocols and timeframes", and the ability to "multitask and operate under pressure" where "high volume call traffic" is involved.','My outline; role description','A3'),
 ('16 Nov 2023','General-practice consultation, Dr Priyal De Silva Nanayakkara. The note records: "Poor sleep. Shift work. Takes melatonin 2 mg to help to go to sleep … but does not help much. <b>Cannot work/ do shifts if he does not get a good sleep.</b> … <b>No psycological illness such as depression/ psycosis. mood good.</b>" Melatonin and temazepam prescribed. (Spelling as in the record.)','General-practice records','A4a'),
 ('20–27 Feb 2024','Leave declined for want of an attached statutory declaration. The Respondent now records "a review indicates that in fact, the attachments were present" and "a matter of human error".','Schedule, 14(e), 14(f)','SCH'),
 ('<b>17–18 Mar 2024</b>','Rostered to finish at 23:00 and to commence at 06:00 — <b>a break of 7 hours, which does not include travel time. With travel, the break between the shifts was less than 5 hours.</b> The fatigue policy and the Award require a minimum of 10 hours, or 8 by written agreement. MET calls were recorded over that period.','Accepted — schedule items 1, 3; travel time as recorded in Review Decision 69983, pp. 16 and 26','SCH'),
 ('19 Mar 2024','<b>The day after those shifts I was absent, and I funded it myself</b> — 7.60 hours of Sick Leave, approved. Paid fatigue leave was not provided; the Regulator’s own pleaded case is that none was available under cl 18.10, no overtime having been performed.','Leave record; Regulator’s pleading 24(b); schedule 22(c)','SCH'),
 ('8 – 24 Apr 2024','<b>I raised the breaks in writing, and followed it up.</b> On 8 April at 3:56 pm, marked High importance, I asked for a review of payment for 8–31 March 2024, enclosing the policies covering "a minimum of a ten-hour break between shifts". My manager escalated it to Human Resources on 9 April. On 24 April at 3:15 pm I wrote again, also High importance, recording more than two weeks without response. The request was refused on 1 May 2024.','My emails of 8 and 24 Apr 2024; the reply',None),
 ('15 Apr 2024','A change to Switchboard working arrangements communicated by email. The Respondent lists no document recording consultation before it.','Respondent’s List of Documents',None),
 ('3 May 2024','Payroll instructed to correct the shifts.','Accepted — schedule item 40','SCH'),
 ('<b>10 – 20 May 2024</b>','<b>The employer assessed the roster internally, and I was not told.</b> The email of 10 May 2024 between Ms Reese and Ms Taylor records the rostering as "impacting on staff fatigue, or more specifically his fatigue", puts it at "a rating of 11 which is moderate", and refers to "a few rostering errors made by Chloe" in past rosters. Ms Reese enquired of Human Resources that day and followed the enquiry up on 20 May. Nothing of it reached me at the time. Over 9–15 May the register records errors on six days while my attempts to make contact went unanswered.','Respondent’s disclosure — email of 10 May 2024; MASPER register',None),
 ('13 May 2024','I made a complaint to the Ethical Standards Unit concerning Ms Taylor and Ms Reese.','ESU complaint form, 13 May 2024',None),
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
 ('20 Sep 2024','The separation date later nominated by the abandonment correspondence — the deed calls it "the Dismissal". It became the effective date of my reinstatement.','Deed, recital D',None),
 ('<b>8 Oct 2024</b>','<b>Dismissal.</b> I received correspondence from the Acting Executive Director treating me as absent without approved leave and as having abandoned my employment. It nominated a separation date of 20 September 2024. It was forwarded to me by email at 4:10 pm on 9 October. I replied in writing.','Deed, recital C; employer letter',None),
 ('<b>24 Oct 2024</b>','<b>First consultation with Dr Krishnaiah. My partner attended that consultation with me.</b>','Your file',None),
 ('<b>24 Oct 2024</b>','<b>The review confirmed the rejection</b> — issued the same day, after the appointment. The reviewer nonetheless determined that I "sustained a personal injury of a psychological nature", that my injury "arose out of employment … where employment was a significant contributing factor", and that the rostering of the 17 and 18 March shifts "amounted to unreasonable management action". The rejection rested on the statutory exclusion alone.','Review Decision 69983, pp. 26–27',None),
 ('13 Feb 2025','Dr Krishnaiah’s report to QSuper. It records workplace stress arising from management and rostering, and refers to relationship breakdown, job loss and bereavement.','Your file',None),
 ('Feb – Mar 2025','My relationship with my partner ended.','My account',None),
 ('24 Dec 2024','<b>The Ethical Standards Unit determined that my complaint constituted a Public Interest Disclosure</b> (24-ESU-1130). No suspicion of corrupt conduct was formed; other administrative issues were identified and referred to Human Resources.','Accepted — schedule item 20; ESU letter, 24 Dec 2024','SCH'),
 ('<b>11 Jan 2025</b>','<b>My great-grandmother, Gwendoline Zena Boland (born Johnston), died</b> seven days after her ninety-fourth birthday (born 4 January 1931). Seven months and a day after her husband. It was my own birthday.','Family record',None),
 ('25 Oct 2024','I applied to the Commission for reinstatement, matter TD/2024/110.','Deed, recital E',None),
 ('<b>21 Feb 2025</b>','<b>The deed was executed, and it undid the dismissal.</b> The Health Service reinstated me "with an effective date of 20 September 2024", that reinstatement taking effect "despite any documents that the Health Service may require the Applicant to execute". Wages were payable for 20 September to 13 December 2024; the period from 13 December 2024 to 23 February 2025 was treated as leave without pay.','Deed, cll. 1, 2, 4',None),
 ('1 Jul 2025','<b>After the onset.</b> Fatigue leave I had submitted was declined in writing: "I have just checked MyHR and noticed your leave has been submitted as Fatigue leave … I have declined this please submit correct leave either S/L or A/L."','Email, Ms Taylor, 1 Jul 2025',None),
 ('3 Jul 2026','Employee Capability Checklist completed by the employer. It identifies three stressors for the position — complaint handling; being blamed for the failures of others; unpredictable rostering.','Capability Checklist','A4c'),
]

NOTES=[
 ('A date I cannot give','The day of Dr Hawes’ referral in September 2024. I have not estimated it; your own file or the general-practice record may show it.'),
 ('Any psychological diagnosis before 24 October 2024','None is recorded in the material I hold. The general-practice record of 26 October 2022 lists "ADHD" and "Anxiety" in a past medical history; I make no assertion about what that entry represents.'),
 ('What is left out','Physical health matters arising in 2026 — not within the three questions. The two deaths, the relationship ending and the loss of the job all appear above at the dates the record gives. I draw no conclusion from their order or their weight, and question 4 of my email asks you to address them.'),
]


import re as _re
_MON={m:i+1 for i,m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])}
def _key(label):
    """Sort key from a row's date label. Rows are authored in any order; the table is
    always rendered in date order, so an inserted row cannot land in the wrong place."""
    s=_re.sub(r'<[^>]+>','',label)
    year=int(_re.search(r'\b(19|20)\d{2}\b',s).group(0))
    mon=_MON[_re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b',s).group(0)]
    d=_re.match(r'\s*(\d{1,2})\b',s)          # leading day number, if the label has one
    return (year,mon,int(d.group(1)) if d else 0)

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
       P('Cory Shepherd, date of birth 11 January 1991 · WC/2024/227 · prepared 5 September 2026. '
         'Dated events, and where each is recorded. It draws no conclusion from any of them, and is not '
         'intended to bear on your opinion. Nothing is estimated: where the record gives no date, none is given.'
         + (' <b>The page references in the right-hand column are clickable.</b>' if linked else ''),TINY),
       Spacer(1,4)]
    r=[[P('<b>Date</b>',SMB),P('<b>Event</b>',SMB),P('<b>Where it is recorded</b>',SMB)]]
    for date,ev,src,key in sorted(ROWS,key=lambda r:_key(r[0])):
        cell = src if not (linked and key) else src+' · '+J(key)
        r.append([P(date,SM),P(ev,SM),P(cell,SM)])
    s.append(_tbl(r,[26*mm,98*mm,46*mm]))
    if jumpbar:
        s.append(Spacer(1,3)); s.append(jumpbar())
    s.append(Spacer(1,3))
    s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com',TINY))
    return s
