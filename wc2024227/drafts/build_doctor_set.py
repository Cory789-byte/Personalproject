#!/usr/bin/env python3
"""Doctor-facing set for 12 Aug 2026: four stressor bundles (doctor clothing),
covering letter, question-and-evidence index. Sources: REPORT_B_LEAN_DOCTOR_PACK.pdf
(page numbers as in the served-bundle builds) + resp_1..3.pdf."""
import subprocess
import pikepdf
from pikepdf import Name, Array, OutlineItem
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
W,H = A4
INK=HexColor('#1a1a1a'); GREY=HexColor('#555555'); BAR=HexColor('#1b1b2f')
SRC='REPORT_B_LEAN_DOCTOR_PACK.pdf'
SUB='Supporting documents · organised by the stressors pleaded in the Amended Form 9A (Enclosure C to the letter of instruction)'
WHO='Cory Lea Shepherd · Appellant (self-represented) · AO3 Switchboard Services, Logan Hospital'
CONTACT='0417 400 227 · coryshepherd1@hotmail.com · 12 August 2026'
ADM='admitted on the Respondent’s pleadings'

BUNDLES = [
 # ---------------- STRESSOR 1(a) ----------------
 dict(
  out='STRESSOR_1A_BUNDLE_DR_12AUG.pdf',
  title='Stressor 1(a) — management conduct · supporting documents',
  qline='Bears on questions 6.5, 6.6 and 6.9 of the letter of instruction.',
  intro='This bundle collects the contemporaneous records for the events pleaded at '
   'Stressor 1(a) of the Amended Form 9A (7 April 2026, Enclosure C to the letter of '
   'instruction). Each tab states what the documents behind it record. All documents are '
   'contemporaneous; several are drawn from the Respondent’s own disclosure.',
  note='The tab wording is descriptive only; the documents speak for themselves.',
  tabs=[
   ('TAB 1','“Hello & Update” · database access removed · 18 July 2023',
    'On 18 July 2023, the appellant’s access to the switchboard database was removed by '
    'email ("Hello & Update"), while the duties requiring that access remained assigned to '
    'the appellant. The document behind this tab is the email of 18 July 2023.',
    [('S',105)]),
   ('TAB 2','On-call arrangements changed · office hours not stated to the team · May 2024',
    'In about May 2024 (pay period 13–26 May 2024), after-hours on-call manager arrangements '
    'were changed and communicated by list, without consultation with switchboard operators. '
    'The documents behind this tab are: the after-hours on-call manager email (Ellen); the '
    'on-call self-delegation email (Ms Taylor); and the on-call and hours all-staff email of '
    '17 May 2024 (Ms Taylor).',
    [('S',123),('S',124),('S',125)]),
   ('TAB 3','The MASPER register (urgent clinical call routing) · errors accumulating while contact attempts went unanswered · 9–15 May 2024',
    'The MASPER register is used by switchboard to route urgent clinical calls to the '
    'responsible medical registrars; the criticality of the Switchboard function is among '
    'the admitted facts (Enclosure D to the letter of instruction). Between 9 and 15 May '
    '2024, following the direction of 9 May 2024 concerning business-hours contact, errors '
    'accumulated in the MASPER register while switchboard remained responsible for call '
    'routing. On 15 May 2024 a pathologist was unable to hand over critical results for '
    'approximately two hours; the registrar’s return call criticised switchboard’s '
    'performance (witnessed by Ms P. Co). The documents behind this tab are the CS-1 MASPER '
    'course records, 9–15 May 2024.',
    [('S',68),('S',69),('S',70),('S',71)]),
   ('TAB 4','“we can not help patients” · misdirected clinical calls · the 20 May 2024 exchange',
    'On 22 February 2024 the document "Outpatients Department – Clinic contact Details" was '
    'modified without notice to switchboard operators. On 15 May 2024 at 11:47am the '
    'Integrated Respiratory Service requested in writing, marked High importance, that the '
    'directory be corrected; on 20 May 2024 at 11:03am it wrote again, recording that '
    'misdirected clinical calls were continuing ("we continue to get calls… we can not help '
    'patients"). At 2:05pm on 20 May 2024 the appellant identified the modification of '
    '22 February 2024 as the cause and recommended in writing a modification and review of '
    'the document. At 4:30pm Ms Taylor replied that "this task was being actioned," that she '
    '"had discussed with Richard this morning," and that "I believe you were aware of that." '
    'The documents behind this tab are the "Respiratory Nurse Educators" email chain, '
    '15–20 May 2024, from the Respondent’s disclosure.',
    [('X','resp_1.pdf'),('X','resp_2.pdf'),('X','resp_3.pdf')]),
   ('TAB 5','Written requests · “more than two weeks without response” · 8 April – 1 May 2024',
    'The appellant’s written requests concerning the roster of 8 April 2024 received no '
    'substantive response until 1 May 2024; the appellant’s email of 24 April 2024 recorded '
    'more than two weeks without response; the request was refused on 1 May 2024. The '
    'documents behind this tab are the rostering concerns correspondence (April 2024) and '
    'the Roster Concerns chain of 26 April – 8 May 2024, including the 1 May 2024 refusal.',
    [('S',108),('S',109),('S',110),('S',111),('S',126),('S',127),('S',128),('S',129)]),
   ('TAB 6','Office hours asked in writing · the retract sent to the appellant only · 9–17 May 2024',
    'On 9 May 2024 Ms Taylor directed that she be contacted during business hours. During '
    '9–15 May 2024, repeated attempts to contact Ms Taylor during business hours went '
    'unanswered, and her office hours had not been stated to the team. The four documents '
    'behind this tab are the sequence of 15–17 May 2024, in order: at 1:15pm on 15 May 2024 '
    'the appellant asked in writing that the office hours be stated; at 6:23pm the '
    'retraction email was sent to the appellant only; at 7:09pm the appellant replied, '
    'attaching Ellen’s hours email; on 17 May 2024 Ms Taylor stated her hours to all staff. '
    '(See also Tab 3 for the CS-1 records of the same period.)',
    [('S',157),('S',158),('S',155),('S',156)]),
  ]),
 # ---------------- STRESSOR 1 COURSE (1(b)-1(f)) ----------------
 dict(
  out='STRESSOR_1_COURSE_BUNDLE_DR_12AUG.pdf',
  title='Stressor 1 — course documents · 1(b), 1(d), 1(e), 1(f) · supporting documents',
  qline='Bears on questions 6.5, 6.6 and 6.9 of the letter of instruction.',
  intro='This bundle collects the contemporaneous records for the events pleaded at '
   'particulars 1(b), 1(d), 1(e) and 1(f) of Stressor 1 of the Amended Form 9A (7 April '
   '2026, Enclosure C). Particular 1(a) is the subject of its own bundle. Several events '
   'below are admitted in whole or in part on the Respondent’s pleadings, as noted tab by tab.',
  note='The tab wording is descriptive only; the documents speak for themselves.',
  tabs=[
   ('TAB 1','1(b) — Communication book · pages removed · 6 June 2023 (removal admitted)',
    'Ms Taylor removed pages from the Communication Book on or about 6 June 2023; the '
    'removal is '+ADM+'. The documents behind this tab are the communication book strand '
    'and the book pages of 6 June 2023 and 21 May 2024.',
    [('S',72),('S',73),('S',74),('S',130),('S',131)]),
   ('TAB 2','1(d) — COVID leave declined · “the attachments were in fact present” · Feb–Mar 2024',
    'The appellant’s Special Pandemic Leave submission was declined on the stated basis that '
    'the required declaration was not attached. The Respondent’s pleading records that a '
    'review indicates the attachments were in fact present, and describes the decline as '
    'human error. The documents behind this tab are the contemporaneous text messages of '
    'February–March 2024 and the myHR leave submission system records.',
    [('S',75),('S',76),('S',77),('S',163)]),
   ('TAB 3','1(e) — the public interest disclosure · lodged 13 May 2024 · determined 24 December 2024 (admitted)',
    'On 13 May 2024 the appellant lodged a complaint regarding clinical risks. The Ethical '
    'Standards Unit formally determined it constituted a Public Interest Disclosure; the '
    'event is '+ADM+'. The documents behind this tab are the ESU complaint face of '
    '13 May 2024 and the PID outcome letter (24-ESU-1130).',
    [('S',81),('S',78),('S',79),('S',80)]),
   ('TAB 4','1(f) — the retraction · “the email was ultimately removed from the server” · 15–17 May 2024',
    'On 15 May 2024 the appellant sent an email concerning office hours; a retraction was '
    'directed within approximately 48 hours, and the Respondent’s pleading records that the '
    'email was ultimately removed from the server. The documents behind this tab are the '
    'complaint and HR disclosure of 15–16 May 2024 (CS-4) and the office-hours and retract '
    'strand of 15–17 May 2024.',
    [('S',82),('S',83),('S',84),('S',85),('S',86)]),
  ]),
 # ---------------- STRESSOR 2 (pay) ----------------
 dict(
  out='STRESSOR_2_PAY_BUNDLE_DR_12AUG.pdf',
  title='Stressor 2 — pay · supporting documents',
  qline='Bears on questions 6.5 and 6.9 of the letter of instruction.',
  intro='This bundle collects the records for Stressor 2 of the Amended Form 9A (7 April '
   '2026, Enclosure C). The matter pleaded is the delay in the remediation of raised pay '
   'issues, not the quantum. The pleaded sequence is substantially admitted on the '
   'Respondent’s pleadings: pay issues raised over 2023–2024; the payroll officer’s AVAC '
   'instruction of 3 May 2024; "waiting for payroll confirmation" on 21 May 2024; '
   'submission on 28 May 2024 — twenty-five days after the instruction.',
  note='The tab wording is descriptive only; the documents speak for themselves.',
  tabs=[
   ('TAB 1','“submit an AVAC” · the payroll instruction of 3 May 2024 and the correspondence to 28 May 2024',
    'On 3 May 2024 the payroll officer instructed Ms Taylor in writing to submit an AVAC to '
    'correct the appellant’s shift payments. The AVAC was submitted on 28 May 2024. The '
    'documents behind this tab are the payroll and underpayment correspondence of that period.',
    [('S',88),('S',89),('S',90),('S',91),('S',92)]),
   ('TAB 2','“waiting for payroll confirmation” · 21 May 2024 · eighteen days after the instruction',
    'On 21 May 2024 Ms Taylor advised the appellant she was still waiting on payroll '
    'confirmation and would submit an AVAC for the next pay run. The documents behind this '
    'tab are that exchange.',
    [('S',106),('S',107)]),
   ('TAB 3','Queensland Health payroll disclosure package · the original records',
    'The original payroll correspondence and AVAC records produced in disclosure, behind '
    'this tab for completeness of the sequence.',
    [('S',116),('S',117),('S',118),('S',119),('S',120),('S',121),('S',122)]),
  ]),
 # ---------------- STRESSOR 3 (fatigue/rostering) ----------------
 dict(
  out='STRESSOR_3_FATIGUE_BUNDLE_DR_12AUG.pdf',
  title='Stressor 3 — fatigue and rostering · the admitted 7-hour break · supporting documents',
  qline='Bears on questions 6.5, 6.6 and 6.9 of the letter of instruction.',
  intro='This bundle collects the records for Stressor 3 of the Amended Form 9A (7 April '
   '2026, Enclosure C). The central event is admitted on the Respondent’s pleadings: the '
   'shifts of 17 and 18 March 2024 were separated by a 7-hour break, described in the '
   'pleading as a result of human error. The Award default break is 10 hours; the agreement '
   'relied on provides for 8, and was signed on 17 June 2020 — some four years before the '
   'shifts in question. The documents below record the break, the written requests and '
   'replies, the employer’s own contemporaneous risk assessment, and the state of the '
   'fatigue risk management framework in the material period.',
  note='The rostering-concerns correspondence of April–May 2024 (8 April to the 1 May 2024 '
   'refusal) is collected in the Stressor 1(a) bundle provided with this set and is not '
   'duplicated here. Several documents are drawn from the Respondent’s own disclosure.',
  tabs=[
   ('TAB 1','The roster · 17–18 March 2024 · the admitted 7-hour break',
    'The roster for March 2024 records the consecutive shifts of 17 and 18 March 2024 '
    'ending at 23:00 and recommencing at 06:00. The break of 7 hours is '+ADM+'.',
    [('S',56),('S',57)]),
   ('TAB 2','Raised in writing · 8 and 24 April 2024 · “a minimum of a ten-hour break between shifts” · the reply',
    'On 8 April 2024 at 3:56pm the appellant requested in writing, marked High importance, '
    'a review of payment for the pay period 8–31 March 2024, enclosing "policies that '
    'delineate both public holiday payments and additional payments applicable in cases '
    'where employees are not rostered a minimum of a ten-hour break between shifts." He '
    'followed up on 24 April 2024 at 3:15pm, also marked High importance. Ms Taylor’s reply '
    'recorded that a Payroll investigation was underway, that entitlements were being '
    'reviewed for "your tenure as a part-time employee," attached an after-hours protocol, '
    'and stated: "As the Switchboard Manager, it is part of my role to be on call after '
    'hours for urgent matters, which include emergencies like any general codes (Code Red, '
    'Yellow, Purple, Brown, and Orange), system outages or staffing issues due to illness." '
    'The documents behind this tab are that exchange (Att 6).',
    [('S',58),('S',59)]),
   ('TAB 3','Recovery leave · 19 March 2024 · the system record · the agreement of 17 June 2020 relied on',
    'Following the shifts of 17–18 March 2024, the appellant took leave on 19 March 2024. '
    'Paid fatigue leave was declined by reference to the agreement of 17 June 2020 — an '
    'agreement signed some four years before the shifts in question. The document behind '
    'this tab is the QH Leave Takings Report of 19 March 2024 (system record).',
    [('S',162)]),
   ('TAB 4','“a rating of 11 which is moderate” · the employer’s own risk assessment · 10 May 2024 (Respondent’s disclosure)',
    'On 10 May 2024 the appellant’s risk matrix was applied to the Switchboard roster by '
    'Ms Reese and Ms Taylor. The email records "at best there would be a rating of 11 which '
    'is moderate", refers to "a few rostering errors ... in past rosters", and records Ms '
    'Reese’s enquiry to Human Resources of 10 May 2024, followed up on 20 May 2024. The '
    'document behind this tab is that email, from the Respondent’s disclosure.',
    [('S',159)]),
   ('TAB 5','No Switchboard fatigue risk assessment in the material period · the Chief Executive’s letter · the guideline that applied',
    'The letter of 5 June 2026 under the hand of the Chief Executive (K-LM26/729) records '
    'the position concerning fatigue risk management in the Switchboard in the material '
    'period, with implementation of the framework after 30 June 2024. The guideline '
    'QH-GDL-401-3.3 is extracted for the standard that applied. Both documents are behind '
    'this tab.',
    [('S',60),('S',61),('S',62),('S',63),('S',64),('S',65),('S',66),('S',67)]),
  ]),
]

def wrap(c,text,x,y,wmax,size,leading,font='Helvetica'):
    c.setFont(font,size)
    words=text.split(); line=''
    while words:
        t=(line+' '+words[0]).strip()
        if c.stringWidth(t,font,size)<=wmax: line=t; words.pop(0)
        else: c.drawString(x,y,line); y-=leading; line=words.pop(0)
    if line: c.drawString(x,y,line); y-=leading
    return y

def scrub(pdf,title):
    with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
        meta['dc:title']=title+' — WC/2024/227'
        meta['dc:creator']=['Cory Lea Shepherd']
        meta['dc:description']='Shepherd v Workers’ Compensation Regulator · WC/2024/227'
    di=pdf.docinfo
    for k in list(di.keys()): del di[k]
    di['/Title']=title+' — WC/2024/227'
    di['/Author']='Cory Lea Shepherd'; di['/Creator']='Cory Lea Shepherd'
    di['/Producer']='Cory Lea Shepherd'
    di['/Subject']='Shepherd v Workers’ Compensation Regulator · WC/2024/227'

src = pikepdf.open(SRC)
EXT={}
for B in BUNDLES:
    front_fn = B['out'].replace('.pdf','_front.pdf')
    c = canvas.Canvas(front_fn, pagesize=A4)
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold',15); c.drawString(57,H-70,'WC/2024/227 · Shepherd v Workers’ Compensation Regulator')
    y = wrap(c,B['title'],57,H-94,480,13,17,'Helvetica-Bold')
    c.setFillColor(GREY)
    y = wrap(c,SUB,57,y-2,480,9.5,12.5)
    c.setFont('Helvetica-Bold',9.5); c.setFillColor(INK)
    y = wrap(c,B['qline'],57,y-4,480,9.5,12.5,'Helvetica-Bold')
    c.setFont('Helvetica',9.5); c.setFillColor(GREY)
    c.drawString(57,y-8,WHO); c.drawString(57,y-21,CONTACT)
    c.setFillColor(INK); y = y-46
    y = wrap(c,B['intro'],57,y,480,10,13.5); y-=12
    c.setFont('Helvetica-Bold',10.5); c.drawString(57,y,'INDEX'); y-=16
    for i,(tabno,title,_e,_p) in enumerate(B['tabs']):
        c.setFont('Helvetica-Bold',10); c.drawString(60,y,tabno)
        c.setFont('Helvetica',9.5)
        short = title if len(title)<95 else title[:92]+'…'
        y = wrap(c,short,110,y,440,9.5,12); y-=4
    y-=8
    c.setFillColor(GREY)
    y = wrap(c,'Note: '+B['note'],57,y,480,9,12)
    c.setFont('Helvetica',8)
    c.drawString(57,40,'Shepherd · WC/2024/227 · '+B['title'].split(' —')[0])
    c.showPage()
    for tabno,title,expl,_p in B['tabs']:
        c.setFillColor(BAR); c.rect(0,H-120,W,60,stroke=0,fill=1)
        c.setFillColor(white); c.setFont('Helvetica-Bold',22)
        c.drawString(57,H-98,tabno)
        c.setFillColor(INK)
        y = wrap(c,title,57,H-150,480,12.5,16,'Helvetica-Bold'); y-=10
        c.setFont('Helvetica-Oblique',9.5); c.setFillColor(GREY)
        c.drawString(57,y,'What the documents record:'); y-=16
        c.setFillColor(INK)
        y = wrap(c,expl,57,y,480,10.5,14.5)
        c.setFillColor(GREY); c.setFont('Helvetica',8)
        c.drawString(57,40,f'Shepherd · WC/2024/227 · {tabno}')
        c.showPage()
    c.save()
    front = pikepdf.open(front_fn)
    pdf = pikepdf.new()
    pdf.pages.append(front.pages[0])
    tabstart=[]
    for i,(tabno,title,_e,pages) in enumerate(B['tabs']):
        tabstart.append(len(pdf.pages)+1)
        pdf.pages.append(front.pages[1+i])
        for kind,val in pages:
            if kind=='S': pdf.pages.append(src.pages[val-1])
            else:
                if val not in EXT: EXT[val]=pikepdf.open(val)
                pdf.pages.append(EXT[val].pages[0])
    pagemap={p.obj.unparse():i+1 for i,p in enumerate(pdf.pages)}
    for p in pdf.pages:
        if '/Annots' in p:
            keep=pikepdf.Array()
            for a in p.Annots:
                ok=False
                try:
                    if a.get('/Subtype')==pikepdf.Name.Link and a.A.S==pikepdf.Name.GoTo:
                        if a.A.D[0].unparse() in pagemap: ok=True
                except Exception: ok=False
                if ok: keep.append(a)
            p.Annots=pdf.make_indirect(keep)
    with pdf.open_outline() as ol:
        ol.root.append(OutlineItem('Cover — index',destination=Array([pdf.pages[0].obj,Name.Fit])))
        for i,(tabno,title,_e,_p) in enumerate(B['tabs']):
            ol.root.append(OutlineItem(f'{tabno} · {title[:90]}',destination=Array([pdf.pages[tabstart[i]-1].obj,Name.Fit])))
    scrub(pdf,B['title'])
    raw=B['out'].replace('.pdf','_raw.pdf')
    pdf.save(raw)
    subprocess.run(['qpdf','--linearize',raw,B['out']],check=True)
    print('BUILT',B['out'],len(pdf.pages),'pages')

# ---------------- QUESTION-AND-EVIDENCE INDEX (one page) ----------------
c = canvas.Canvas('_qindex.pdf', pagesize=A4)
c.setFillColor(INK)
c.setFont('Helvetica-Bold',14); c.drawString(57,H-64,'WC/2024/227 · Questions and evidence — where the documents sit')
c.setFillColor(GREY); c.setFont('Helvetica',9.5)
c.drawString(57,H-80,'One-page index to the letter of instruction (questions 6.1–6.11), the indexed source pack, and the four stressor bundles.')
c.drawString(57,H-93,WHO)
ROWS=[
 ('6.1','Diagnosis, criteria and onset','Source pack: chronology · CS-3 full-time application (31 Aug 2023) · GP entry 16 Nov 2023 · Hawes certificate (Enclosure F).'),
 ('6.2','Differential diagnoses','Clinical — your own assessment.'),
 ('6.3','Psychiatric background / aggravation','Ashmore GP records incl. 2022 entries (Enclosure E) · CS-3 · full-time approval 27 Sep 2023 · GP entry 16 Nov 2023.'),
 ('6.4','Sources list','All materials provided: the letter of instruction and enclosures · the indexed source pack · the four stressor bundles · your own records.'),
 ('6.5','Causation — s 32(1)','All four stressor bundles, organised as pleaded: Stressor 1(a) · Stressor 1 course 1(b)–(f) · Stressor 2 (pay) · Stressor 3 (fatigue and rostering) · the Amended Form 9A (Enclosure C).'),
 ('6.6','April–May 2024 material · presentation interval','Stressor 3 bundle Tabs 2–4 (8 Apr · 24 Apr · risk assessment) · Stressor 1(a) bundle Tabs 3–6 (MASPER 9–15 May · 20 May exchange · hours and retract) · Stressor 1 course Tabs 3–4 (13 May · 15–17 May) · Hawes certificate (Enclosure F).'),
 ('6.7','Competing non-employment causes, timed','Source pack: chronology — post-onset events with dates (employment ended Oct 2024, later reversed · personal matters from about Dec 2024).'),
 ('6.8','Premorbid personality','Clinical — your own current assessment.'),
 ('6.9','Mechanism','Stressor 3 bundle Tabs 1 and 5 (the roster · the framework position) · Stressor 1(a) bundle Tabs 3–4 (MASPER · the respiratory chain) · Stressor 2 bundle (the remediation delay).'),
 ('6.10','Prognosis and capacity','Employee Capacity Checklist 3 Jul 2026 (Enclosure G), for review — the opinion remains yours.'),
 ('6.11','Change in capacity over time','The 13 February 2025 report (Enclosure H) · the 2025–26 course in the source pack chronology.'),
]
y=H-118
for q,t,srctxt in ROWS:
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold',10); c.drawString(57,y,q)
    c.drawString(88,y,t)
    y-=13
    c.setFillColor(GREY)
    y=wrap(c,srctxt,88,y,445,9,11.5)
    y-=7
c.setFillColor(GREY); c.setFont('Helvetica',8)
c.drawString(57,40,'Shepherd · WC/2024/227 · Questions and evidence index')
c.showPage(); c.save()
qp=pikepdf.open('_qindex.pdf'); scrub(qp,'Questions and evidence index')
qp.save('_qindex_m.pdf')
subprocess.run(['qpdf','--linearize','_qindex_m.pdf','QUESTIONS_EVIDENCE_INDEX_DR_12AUG.pdf'],check=True)
print('BUILT QUESTIONS_EVIDENCE_INDEX_DR_12AUG.pdf')

# ---------------- COVERING LETTER (one page) ----------------
c = canvas.Canvas('_letter.pdf', pagesize=A4)
c.setFillColor(INK)
c.setFont('Helvetica',10.5)
y=H-70
for line in ['Cory Lea Shepherd','0417 400 227 · coryshepherd1@hotmail.com','12 August 2026']:
    c.drawString(57,y,line); y-=14
y-=10
c.drawString(57,y,'Dr Krishnaiah'); y-=14
c.drawString(57,y,'Consultant Psychiatrist'); y-=24
c.setFont('Helvetica-Bold',11)
y=wrap(c,'Re: Medico-legal report — Shepherd v Workers’ Compensation Regulator, QIRC matter WC/2024/227',57,y,480,11,14,'Helvetica-Bold')
y-=8
c.setFont('Helvetica',10.5)
paras=[
 'Dear Dr Krishnaiah,',
 'Thank you for seeing me today. This letter records what I am providing for the report, '
 'and the practical matters we should confirm.',
 'I am providing: (1) the letter of instruction, with its enclosures, setting out the '
 'questions (6.1–6.11) and the assumed facts; (2) an indexed and bookmarked source pack '
 '(PDF) containing the documents behind the chronology; (3) four bundles of supporting '
 'documents, organised by the stressors as pleaded in the Amended Form 9A — Stressor 1(a), '
 'Stressor 1 course (1(b)–(f)), Stressor 2 (pay) and Stressor 3 (fatigue and rostering) — '
 'each with a one-page index and tab notes describing what the documents record; and (4) a '
 'one-page index mapping each question to where the relevant documents sit.',
 'Your opinion is yours alone. The documents are provided for reference and for your '
 'sources list; the tab notes are for convenience of navigation only. Legal questions — '
 'including the reasonableness of any management action — are not asked of you.',
 'May I ask that we confirm the following in writing: (1) the report is prepared for use '
 'in Queensland Industrial Relations Commission proceeding WC/2024/227, and will not carry '
 'a restriction against medico-legal use; (2) the report will include a complete list of '
 'documents reviewed and attendances, with dates and durations; (3) the questions in the '
 'letter of instruction will each be answered with reasons; (4) you are available to give '
 'oral evidence if required (telephone or video is available), and your fee estimate for '
 'the report and any attendance; and (5) your expected timeframe for delivery of the report.',
 'Thank you again for your time.',
 'Yours sincerely,',
 'Cory Lea Shepherd',
]
for p in paras:
    y=wrap(c,p,57,y,480,10.5,14)
    y-=8
c.showPage(); c.save()
lp=pikepdf.open('_letter.pdf'); scrub(lp,'Covering letter to Dr Krishnaiah')
lp.save('_letter_m.pdf')
subprocess.run(['qpdf','--linearize','_letter_m.pdf','LETTER_TO_DR_KRISHNAIAH_12AUG.pdf'],check=True)
print('BUILT LETTER_TO_DR_KRISHNAIAH_12AUG.pdf')
