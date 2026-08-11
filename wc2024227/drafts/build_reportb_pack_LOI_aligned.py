#!/usr/bin/env python3
"""Report B doctor's pack — LOI-aligned build (v6).
Question pages verbatim from the letter of instruction; enclosure-letter labelling;
Hawes merged as Enclosure F; Enclosure A marker page; Form 20 removed; 9A scope-only."""
import subprocess, re, os
import pikepdf
from pikepdf import Name, Dictionary, Array
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white

SRC = 'REPORT_B_LEAN_DOCTOR_PACK.pdf'
OUT = 'REPORT_B_DOCTOR_PACK_LOI_ALIGNED_11AUG.pdf'
W, H = A4
INK = HexColor('#1a1a1a'); BLUE = HexColor('#1552a0'); GREY = HexColor('#555555')

def rng(a,b): return [('S',p) for p in range(a,b+1)]
BODY=[]; BLOCKS={}
def block(key, pages, title):
    BLOCKS[key]={'start':len(BODY),'n':len(pages),'title':title}
    BODY.extend(pages)
# ---- body order ----
block('E05',  [('S',13)],   'Enclosure D · Form 24 KEY ADMISSIONS extract (the admitted facts)')
block('F24N', rng(14,19),   'Form 24 · original notice to admit facts (as filed · completeness)')
block('F24R', rng(20,25),   '18 Feb 2026 · Regulator · Form 24 response (admit / not-admit map)')
block('E04MAP',[('S',26)],  'Enclosure C · Amended Form 9A · stressor map (reference aid)')
block('E04',  rng(27,31),   'Enclosure C · Amended Form 9A · 7 Apr 2026 · scope and context only (5 pp)')
block('E01',  rng(34,37),   'Letter of instruction · Report B (questions 6.1–6.11)')
block('ENCLA',[('X','encl_a.pdf')], 'Enclosure A · signed statement — note (provided separately)')
block('E02',  [('S',38)],   'Enclosure B · chronology of the relevant events')
block('E03',  rng(39,40),   'Fatigue raised · contemporaneous dates from/to (supplementary)')
block('E07',  rng(56,57),   '17-18 Mar 2024 · roster · the admitted 7-hour break pairing')
block('E38',  [('S',159)],  '10 May 2024 · Reese/Taylor · FRMS risk-matrix email · rating 11')
block('E08',  rng(58,59),   'Mar 2024 · Att 6 · fatigue leave / pairing / June 2020 agreement emails')
block('E09',  rng(60,64),   '5 Jun 2026 · Chief Executive · letter K-LM26/729 (no Switchboard FRMS assessment in period)')
block('E10',  rng(65,67),   'QH-GDL-401-3.3 · FRMS guideline (extract)')
block('E30',  rng(108,111), 'Apr-May 2024 · rostering concerns correspondence (8 Apr · 9 Apr · 24 Apr)')
block('E31',  rng(112,113), 'Rostering FRMS communication and EB11 process emails')
block('E32',  [('S',114)],  'Reese · developing rosters / FRMS awareness email')
block('E33',  [('S',115)],  '20 Apr 2023 · Reese · rostering change email')
block('R1MAY',rng(126,129), '26 Apr - 8 May 2024 · Roster Concerns · the 1 May 2024 refusal')
block('RDRAFT',rng(132,138),'Draft rotational rosters · 6 sheets (Shepherd proposal)')
block('RPP',  rng(139,143), 'Mar-Apr 2024 · management pay-period rosters')
block('RATT4',rng(144,145), 'Mar 2024 · Att 4 face roster · pairing period')
block('RPHOT',rng(146,154), 'Phone photographs · rosters and pay sheets')
block('E19',  [('S',87)],   '31 Aug 2023 · Shepherd · CS-3 application 0.8 to full-time')
block('E39',  [('S',160)],  '27 Sep 2023 · Taylor · Permanent Full-Time APPROVED (from 16 Oct 2023)')
block('E21',  rng(93,95),   'Enclosure E · GP records (Our Medical Ashmore) · 26 Oct 2022 · 16 Nov 2023')
block('HAWES',[('S',96),('S',161)], 'Enclosure F · Hawes Work Capacity Certificate · first attendance 1 Jul 2024 · signed 8 Sep 2024')
block('E23',  rng(97,100),  'Enclosure H · your report of 13 Feb 2025 (QSuper · Ings)')
block('E24',  [('S',101)],  'Enclosure G · certificate of capacity 3 Jul 2026 (fit · substantive role · adjustments)')
block('E25',  rng(102,103), '2 Jul 2026 · MSH email · exclusion context')
block('E26',  [('S',104)],  '2026 · Mind and Memory clinic correspondence')
block('E11',  rng(68,71),   '9-15 May 2024 · CS-1 · MASPER call-handling course')
block('E12',  rng(72,74),   'Jun 2023 · communication book / page-removal strand')
block('BK23', [('S',130)],  '6 Jun 2023 · communication book page')
block('BK24', [('S',131)],  '21 May 2024 · communication book page')
block('E13',  rng(75,77),   'Feb-Mar 2024 · COVID leave texts')
block('E14',  rng(78,80),   '24 Dec 2024 · PID outcome letter · 24-ESU-1130')
block('E15',  [('S',81)],   '13 May 2024 · ESU complaint face')
block('E16',  rng(82,84),   '15-16 May 2024 · CS-4 complaint / HR disclosure')
block('E17',  rng(85,86),   '15-17 May 2024 · office-hours email and retract strand')
block('E27',  [('S',105)],  '18 Jul 2023 · Ellen · database access removal email')
block('E35',  [('S',123)],  'Ellen · Switchboard after-hours on-call manager email')
block('E36',  [('S',124)],  'Taylor · after-hours on-call self-delegation email')
block('E37',  [('S',125)],  '17 May 2024 · Taylor · on-call and hours all-staff email')
block('HRS',  rng(155,158), 'Hours requests and responses · sequence of four')
block('E20',  rng(88,92),   '3-28 May 2024 · payroll AVAC / underpayment correspondence')
block('E28',  rng(106,107), '21 May 2024 · Taylor · "still waiting payroll" / AVAC next run')
block('E34',  rng(116,122), 'Qld Health payroll disclosure package (NNPD originals)')
block('E41',  [('S',162)],  '19 Mar 2024 · Item 15 · QH Leave Takings Report (system record)')
block('E42',  [('S',163)],  'Feb-May 2024 · Item 11 · myHR leave submissions (system record)')
block('E43',  rng(166,174), '24 Oct 2024 · Review Decision 69983 (completeness of sources · de novo)')

N_FRONT = 12
def fp(key): return N_FRONT + BLOCKS[key]['start'] + 1

# ---- question definitions: verbatim LOI text ----
QS = [
 ('Q6.1 Diagnosis, criteria and onset',
  'Please state the diagnosis; the classificatory framework you apply (e.g. DSM-5, with the code); the specific diagnostic criteria met, and when each was met; and the date of onset as best the clinical record establishes it.',
  [('Enclosure B · chronology','E02'),('Enclosure E · GP records (Ashmore) · 26 Oct 2022 · 16 Nov 2023','E21'),('Enclosure F · Hawes WCC · first attendance 1 Jul 2024 · signed 8 Sep 2024','HAWES'),('Enclosure H · your report of 13 Feb 2025','E23'),('Enclosure D · admitted facts extract','E05'),('CS-3 application 31 Aug 2023 (record)','E19'),('Full-time approval 27 Sep 2023 (record)','E39')]),
 ('Q6.2 Differential diagnoses',
  'Please identify the differential diagnoses you considered, and your reasons for including or excluding each.',
  [('Enclosure H · your report of 13 Feb 2025','E23'),('Enclosure E · GP records (Ashmore)','E21'),('Enclosure B · chronology','E02')]),
 ('Q6.3 Psychiatric background',
  'Please address my background psychiatric history. In particular, please address the entries of 26 October 2022 referring to anxiety and ADHD (Enclosure E), and any earlier stimulant (Vyvanse) use, and state: whether there was any relevant pre-existing condition; and, if so, whether the employment matters described in the enclosures aggravated any such condition and, if so, to what extent. (I note the aggravation provisions at paragraph 3 of the letter of instruction.)',
  [('Enclosure E · GP records (Ashmore) · 26 Oct 2022 entries','E21'),('Enclosure H · your report of 13 Feb 2025','E23'),('Enclosure D · admitted facts extract','E05'),('Enclosure B · chronology','E02'),('CS-3 application 31 Aug 2023 (record)','E19'),('Full-time approval 27 Sep 2023 (record)','E39')]),
 ('Q6.4 Sources',
  'Please include in the report a complete list of every document you reviewed and every person you saw, with the dates and the duration of each examination. I ask for this specifically because the completeness of the source list is the first thing tested.',
  [('Letter of instruction · section 6.4','E01'),('NOTE','E43')]),
 ('Q6.5 Causation (s 32(1))',
  'On the assumed facts, please state whether my employment — and in particular the pleaded matters, including the rostering and fatigue sequence of 17 March – 1 May 2024 (the consecutive shifts, the admitted 7-hour break, my requests for fatigue relief, the refusal, and my consequent use of my own leave), the conditions of the Switchboard role as described in the assumed facts, and the handling of the concerns I raised — was a significant contributing factor to the injury of which onset is pleaded at 18 June 2024. Please give your clinical reasoning, and please distinguish between the cause of onset and any factors bearing only on the subsequent course of the condition.',
  [('Enclosure A · signed statement — the assumed facts (see note page)','ENCLA'),('Enclosure B · chronology (corroborating)','E02'),('Enclosure D · admitted facts extract (corroborating)','E05'),('Enclosure C · Amended Form 9A · scope and context only','E04MAP'),('March 2024 roster · the admitted 7-hour break','E07'),('Att 6 · fatigue leave / pairing emails','E08'),('Rostering concerns correspondence · Apr 2024','E30'),('Roster Concerns · the 1 May 2024 refusal','R1MAY')]),
 ('Q6.6 The April–May 2024 material and the interval before presentation',
  'The contemporaneous record shows that on 8 April 2024 I raised, in writing, the shift pairing and the minimum-break provision; that my manager escalated it to Human Resources on 9 April 2024; that I wrote again on 24 April 2024 recording more than two weeks without response; and that the request was refused on 1 May 2024. What, if anything, do you make of the reports of fatigue recorded in April and May 2024, in the context of the diagnosis you made subsequently? Separately, from a clinical perspective, what significance (if any) do you attach to the interval between the pleaded onset (18 June 2024) and the first medical presentation for this injury? (The Work Capacity Certificate at Enclosure F records first attendance for this injury on 1 July 2024; please take the presentation dates from the records themselves.)',
  [('Rostering concerns correspondence · 8 Apr · 9 Apr · 24 Apr 2024','E30'),('Roster Concerns · the 1 May 2024 refusal','R1MAY'),('Att 6 · fatigue leave / pairing emails','E08'),('Employer FRMS risk-matrix email · rating 11 · 10 May 2024','E38'),('Enclosure F · Hawes WCC · first attendance 1 Jul 2024','HAWES'),('Fatigue raised · dates from/to','E03'),('Enclosure B · chronology','E02')]),
 ('Q6.7 Competing (non-employment) causes, placed in time',
  'Please identify any non-employment factors you consider relevant to (a) the onset of the condition at or about 18 June 2024, and (b) its subsequent course. Your report of 13 February 2025 referred to "multiple life stressors, including relationship breakdown, job loss and bereavement". For each factor, please state when in time it arose relative to 18 June 2024, and address the significance, if any, of that timing for (a) the cause of onset and (b) the subsequent course. To assist with timing, please assume the following as facts: the cessation of my employment occurred in about October 2024 (and was later reversed by reinstatement); and the personal and relationship matters commenced from about December 2024. (I note the test does not require any competing cause to be outweighed.)',
  [('Enclosure H · your report of 13 Feb 2025','E23'),('Enclosure B · chronology','E02')]),
 ('Q6.8 Premorbid personality',
  'Please address, from your own clinical assessment, whether any premorbid personality features bear on (a) the diagnosis and (b) the causation question at 6.5, and if so how — including whether such features are consistent with, or instead displace, the diagnosis you have made. I do not ask you to adopt or repeat any earlier characterisation; please reason from your own current assessment.',
  [('Enclosure H · your report of 13 Feb 2025','E23'),('Enclosure E · GP records (Ashmore)','E21')]),
 ('Q6.9 Mechanism',
  'From a clinical perspective, please explain whether, and if so how, conditions of the kind described in the assumed facts — including sustained demand, the degree of control or autonomy, the adequacy of support, and fatigue arising from the rostering — can contribute to a condition of the kind you have diagnosed.',
  [('Enclosure A · signed statement — the assumed facts (see note page)','ENCLA'),('Enclosure B · chronology','E02'),('Enclosure D · admitted facts extract','E05'),('Employer FRMS risk-matrix email · rating 11 · 10 May 2024','E38'),('CE letter K-LM26/729 · no FRMS assessment in period','E09'),('FRMS guideline extract','E10'),('CS-1 MASPER course · 9-15 May 2024','E11')]),
 ('Q6.10 Prognosis and capacity',
  'Please state your prognosis. As to capacity, please express your opinion on your own clinical judgment. In particular, please distinguish between (a) my capacity to perform the substantive role with reasonable adjustments, and (b) any current incapacity; and if there is any current incapacity, please state your opinion as to its cause — including whether it is attributable to the condition itself, to the consequences of my exclusion from the workplace since 3 July 2026, or to other factors. My certificate of capacity dated 3 July 2026 (Enclosure G) certifies me fit for my substantive role with adjustments; I provide it for your review and ask only that your opinion be your own. (The detailed assessment of adjustments is the subject of the separate Metro South report.)',
  [('Enclosure G · certificate of capacity 3 Jul 2026','E24'),('Enclosure H · your report of 13 Feb 2025','E23'),('MSH email 2 Jul 2026 · exclusion context','E25'),('Clinic correspondence 2026','E26')]),
 ('Q6.11 Change in capacity over time',
  'Your report of 13 February 2025 (Enclosure H) addressed my capacity at that time. From a clinical perspective, please explain how my capacity has evolved between that assessment and the present, and the reasons for any change.',
  [('Enclosure H · your report of 13 Feb 2025','E23'),('Enclosure G · certificate of capacity 3 Jul 2026','E24'),('Enclosure B · chronology','E02'),('MSH email 2 Jul 2026 · exclusion context','E25'),('Clinic correspondence 2026','E26')]),
]

# ---- helpers ----
def wrap(c, text, x, y, wmax, size, leading, font='Helvetica'):
    c.setFont(font, size)
    words = text.split(); line=''
    while words:
        t=(line+' '+words[0]).strip()
        if c.stringWidth(t,font,size)<=wmax: line=t; words.pop(0)
        else: c.drawString(x,y,line); y-=leading; line=words.pop(0)
    if line: c.drawString(x,y,line); y-=leading
    return y
def make_stamp(fn, draw):
    cc=canvas.Canvas(fn,pagesize=A4); draw(cc); cc.save()

# ---- Enclosure A note page ----
c = canvas.Canvas('encl_a.pdf', pagesize=A4)
c.setFillColor(HexColor('#1b1b2f')); c.rect(0,824,W,18,stroke=0,fill=1)
c.setFillColor(white); c.setFont('Helvetica-Bold',9)
c.drawString(10,829,'Enclosure A · signed statement (provided separately)')
c.setFillColor(INK); c.setFont('Helvetica-Bold',13)
c.drawString(57,H-90,'Enclosure A — signed statement of Cory Lea Shepherd')
y = wrap(c,'The signed statement is provided separately with the letter of instruction. '
 'Per paragraph 4 of the letter, the assumed facts for this report are those set out in '
 'the signed statement (Enclosure A), as corroborated by the chronology (Enclosure B) and '
 'the admitted facts (Enclosure D). The Amended Form 9A (Enclosure C) is provided for '
 'scope and context only and is not facts you are asked to assume.',57,H-120,480,10.5,14.5)
c.setFillColor(GREY); c.setFont('Helvetica',8)
c.drawString(57,40,'Shepherd · WC/2024/227 · confidential')
c.save()

# ---- front matter ----
LINKS=[]
c = canvas.Canvas('front.pdf', pagesize=A4)
c.setFillColor(INK)
c.setFont('Helvetica-Bold',15); c.drawString(57,H-70,'WC/2024/227')
c.setFont('Helvetica-Bold',13)
c.drawString(57,H-92,'Report B — Letter of instruction, enclosures and source documents')
c.setFont('Helvetica',10.5); c.setFillColor(GREY)
c.drawString(57,H-108,'Dr Krishnaiah · Cory Shepherd · Confidential')
c.setFillColor(INK); y=H-140
y = wrap(c,'Navigate by the bookmarks panel — every document has its own dated bookmark. '
 'Page references appear on each question page. Blue lines are links.',57,y,480,10,13); y-=8
c.setFont('Helvetica-Bold',10.5); c.drawString(57,y,'READ IN THIS ORDER:'); y-=16
ORDER=[
 ('1.  The questions (Q6.1–6.11, as put in the letter of instruction)','QSTART'),
 ('2.  Enclosure D — the admitted facts (extract, then the full Form 24)','E05'),
 ('3.  Enclosure C — Amended Form 9A (7 Apr 2026) — scope and context only','E04MAP'),
 ('4.  The letter of instruction · Enclosure A note · Enclosure B chronology','E01'),
 ('5.  Fatigue and rostering documents, incl. the employer’s 10 May 2024 risk-matrix email','E07'),
 ('6.  Rosters (proposals · pay-period rosters · photographs)','RDRAFT'),
 ('7.  Enclosures E–H — GP records · Hawes certificate · prior report · certificate of capacity','E19'),
 ('8.  Governance, May 2024, and the hours sequence','E11'),
 ('9.  Pay and leave records (correspondence and system records)','E20'),
 ('10. Review Decision 69983 (included last, for completeness of sources)','E43'),
]
c.setFillColor(BLUE)
for txt,key in ORDER:
    c.setFont('Helvetica',10.5); c.drawString(66,y,txt)
    LINKS.append((0,(60,y-3,545,y+11),key)); y-=16
c.setFillColor(INK); y-=10
c.setFont('Helvetica-Bold',10.5); c.drawString(57,y,'THE BASIS OF THE REPORT (letter of instruction, paragraph 4):'); y-=15
y = wrap(c,'The assumed facts are those in the signed statement (Enclosure A), corroborated by '
 'the chronology (Enclosure B) and the admitted facts (Enclosure D). The Amended Form 9A '
 '(Enclosure C) shows the matters in issue and is not facts to assume. The case pleaded is a '
 'course of management conduct in relation to rostering, fatigue, pay and the handling of '
 'concerns raised; it is not a case of bullying or harassment.',57,y,480,10,13.5); y-=14
c.setFont('Helvetica-Bold',10.5); c.drawString(57,y,'DATES AS THE DOCUMENTS SHOW THEM:'); y-=15
y = wrap(c,'Full-time applied for 31 Aug 2023 · approved 27 Sep 2023 · commenced 16 Oct 2023 · '
 'GP entry 16 Nov 2023 · attendance difficulty from 13–15 May 2024 (recorded in the '
 'Respondent’s pleading) · pleaded onset 18 Jun 2024 · first attendance for this injury '
 '1 Jul 2024 (Enclosure F) · claim 1 Jul 2024.',57,y,480,10,13.5); y-=14
c.setFont('Helvetica-Bold',10.5); c.drawString(57,y,'YOUR OPINION IS YOURS ALONE.'); y-=15
y = wrap(c,'The questions are those in the letter of instruction, reproduced verbatim on the '
 'following pages. Clinical conclusions, diagnosis, causation and capacity are matters for '
 'your independent judgment; legal questions (including the reasonableness of management '
 'action) are not asked of you.',57,y,480,10,13.5)
c.setFillColor(GREY); c.setFont('Helvetica',8)
c.drawString(57,40,'Private · confidential · Shepherd WC/2024/227')
c.showPage()
for qi,(title,body,items) in enumerate(QS):
    c.setFillColor(INK)
    y = wrap(c,title,57,H-70,480,12.5,16,'Helvetica-Bold'); y-=8
    c.setFont('Helvetica-Oblique',9.5); c.setFillColor(GREY)
    c.drawString(57,y,'From the letter of instruction (verbatim):'); y-=15
    c.setFillColor(INK)
    y = wrap(c,body,57,y,480,10,13.8); y-=12
    c.setFont('Helvetica-Bold',10); c.drawString(57,y,'Documents for this question (blue lines are links):'); y-=15
    for label,key in items:
        if label=='NOTE':
            c.setFillColor(INK); c.setFont('Helvetica',9.5)
            y = wrap(c,'Note: the Review Decision 69983 is included, last, so your sources list may record that it was reviewed.',57,y,470,9.5,12.5)
            LINKS.append((1+qi,(57,y-2,540,y+26),'E43')); y-=4
            continue
        c.setFillColor(BLUE); c.setFont('Helvetica',10)
        c.drawString(63,y,f'·  {label}  —  p.{fp(key)}')
        LINKS.append((1+qi,(57,y-3,545,y+11),key)); y-=14.5
    c.setFillColor(GREY); c.setFont('Helvetica',8)
    c.drawString(57,40,f'Shepherd · WC/2024/227 · {title.split(" ")[0]}')
    c.showPage()
c.save()

# ---- stamps ----
def pill(cc,x0,x1,label):
    cc.setFillColor(HexColor('#222222')); cc.roundRect(x0,824,x1-x0,15,4,stroke=0,fill=1)
    cc.setFillColor(white); cc.setFont('Helvetica-Bold',8)
    cc.drawCentredString((x0+x1)/2,828.5,label)
make_stamp('st_ret.pdf', lambda cc: pill(cc,498,585,'◂ Questions'))
def strip_retitle(fn,label):
    def draw(cc):
        cc.setFillColor(HexColor('#1b1b2f')); cc.rect(0,822,W,20,stroke=0,fill=1)
        cc.setFillColor(white); cc.setFont('Helvetica-Bold',9)
        cc.drawString(10,828,label)
    make_stamp(fn,draw)
strip_retitle('st_f1.pdf','Enclosure F · Hawes Work Capacity Certificate · first attendance 1 Jul 2024 · signed 8 Sep 2024 · p.1 of 2')
strip_retitle('st_f2.pdf','Enclosure F · Hawes Work Capacity Certificate · first attendance 1 Jul 2024 · signed 8 Sep 2024 · p.2 of 2')
def banner_fix(src_page, keys, label, fn):
    xml = subprocess.run(['pdftotext','-bbox','-f',str(src_page),'-l',str(src_page),SRC,'-'],
                         capture_output=True,text=True).stdout
    words=[(float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4)),m.group(5))
           for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>',xml)]
    bands=sorted({round(w[1]) for w in words if any(k in w[4].lower() for k in keys)})
    if not bands: return None
    def draw(cc):
        for by in bands:
            line=[w for w in words if abs(w[1]-by)<2]
            y0=min(w[1] for w in line); y1=max(w[3] for w in line)
            ry0=H-y1-2; rh=y1-y0+4; dark=y1<25
            cc.setFillColor(HexColor('#1b1b2f') if dark else white)
            cc.rect(0 if dark else 24, ry0, W if dark else 548, rh, stroke=0, fill=1)
            cc.setFillColor(white if dark else HexColor('#1a1a1a'))
            cc.setFont('Helvetica-Bold' if dark else 'Helvetica', min(9,rh-2))
            cc.drawString(10 if dark else 28, ry0+2.5, label)
    make_stamp(fn,draw); return fn
BFIX={}
for sp in (75,76,77): BFIX[sp]=banner_fix(sp,['obstruction'],'COVID leave texts · Feb-Mar 2024',f'st_b{sp}.pdf')
BFIX[130]=banner_fix(130,['pattern'],'Communication book · 6 Jun 2023','st_b130.pdf')
BFIX[131]=banner_fix(131,['pattern'],'Communication book · 21 May 2024','st_b131.pdf')
for j,sp in enumerate((155,156,157,158)):
    who=['Ellen · all-department','Taylor · all-department','Shepherd · office-hours request','Reese · retract (to Shepherd only)'][j]
    BFIX[sp]=banner_fix(sp,['double'],f'Hours requests and responses · {j+1} of 4 · {who}',f'st_h{sp}.pdf')
def _map26(cc):
    ry0=H-308.863-2; ry1=H-300.538+2
    cc.setFillColor(white); cc.rect(26,ry0,545,ry1-ry0,stroke=0,fill=1)
    cc.setFillColor(INK); cc.setFont('Helvetica',8.3)
    cc.drawString(28,ry0+3.2,'· Hours sequence: managers’ all-staff hours emails; his hours request; the retract sent to him only.')
make_stamp('st_map26.pdf',_map26)
def _foot(cc):
    cc.setFillColor(white); cc.rect(20,18,555,50,stroke=0,fill=1)
    cc.setFillColor(GREY); cc.setFont('Helvetica',7)
    cc.drawString(30,30,'Shepherd · WC/2024/227 · confidential')
make_stamp('st_foot.pdf',_foot)

# ---- assemble ----
src = pikepdf.open(SRC)
front = pikepdf.open('front.pdf')
pdf = pikepdf.new()
for p in front.pages: pdf.pages.append(p)
EXT_CACHE={}
for kind,val in BODY:
    if kind=='S': pdf.pages.append(src.pages[val-1])
    else:
        if val not in EXT_CACHE: EXT_CACHE[val]=pikepdf.open(val)
        pdf.pages.append(EXT_CACHE[val].pages[0])
assert len(pdf.pages)==N_FRONT+len(BODY)
ret=pikepdf.open('st_ret.pdf')
for i in range(N_FRONT,len(pdf.pages)): pdf.pages[i].add_overlay(ret.pages[0])
def src_final(sp):
    for i,(k,v) in enumerate(BODY):
        if k=='S' and v==sp: return N_FRONT+i+1
    return None
st26=pikepdf.open('st_map26.pdf'); pdf.pages[fp('E04MAP')-1].add_overlay(st26.pages[0])
for sp,fn in BFIX.items():
    if fn:
        st=pikepdf.open(fn); pdf.pages[src_final(sp)-1].add_overlay(st.pages[0])
stf=pikepdf.open('st_foot.pdf')
for k in range(4): pdf.pages[fp('HRS')-1+k].add_overlay(stf.pages[0])
f1=pikepdf.open('st_f1.pdf'); f2=pikepdf.open('st_f2.pdf')
pdf.pages[fp('HAWES')-1].add_overlay(f1.pages[0])
pdf.pages[fp('HAWES')].add_overlay(f2.pages[0])
def add_link(page,rect,target):
    annot=Dictionary(Type=Name.Annot,Subtype=Name.Link,
        Rect=Array(list(rect)),Border=Array([0,0,0]),
        A=Dictionary(S=Name.GoTo,D=Array([target.obj,Name.Fit])))
    if '/Annots' not in page: page.Annots=pdf.make_indirect(Array())
    page.Annots.append(pdf.make_indirect(annot))
for fpg,rect,key in LINKS:
    tgt=pdf.pages[1] if key=='QSTART' else pdf.pages[fp(key)-1]
    add_link(pdf.pages[fpg],rect,tgt)
q1=pdf.pages[1]
for i in range(N_FRONT,len(pdf.pages)): add_link(pdf.pages[i],(498,822,585,841),q1)

# ---- bookmarks ----
from pikepdf import OutlineItem
def oi(title,key=None,page=None):
    pg=pdf.pages[(fp(key)-1) if key else page]
    return OutlineItem(title,destination=Array([pg.obj,Name.Fit]))
with pdf.open_outline() as ol:
    r=ol.root
    r.append(oi('Cover — reading order (links live)',page=0))
    a=oi('A. The questions (letter of instruction, verbatim)',page=1)
    for i,(title,_,_2) in enumerate(QS): a.children.append(oi(title,page=1+i))
    r.append(a)
    def sec(title,fk,items):
        s=oi(title,key=fk)
        for k in items: s.children.append(oi(BLOCKS[k]['title'],key=k))
        r.append(s)
    sec('B. Enclosure D — the admitted facts + full Form 24','E05',['E05','F24N','F24R'])
    sec('C. Enclosure C — Amended Form 9A (7 Apr 2026 · scope only)','E04MAP',['E04MAP','E04'])
    sec('D. Letter of instruction · Enclosures A and B','E01',['E01','ENCLA','E02','E03'])
    sec('E. Fatigue and rostering documents','E07',['E07','E38','E08','E09','E10','E30','E31','E32','E33','R1MAY'])
    sec('F. Rosters','RDRAFT',['RDRAFT','RPP','RATT4','RPHOT'])
    sec('G. Enclosures E–H — medical and baseline','E19',['E19','E39','E21','HAWES','E23','E24','E25','E26'])
    sec('H. Governance · May 2024 · hours','E11',['E11','E12','BK23','BK24','E13','E14','E15','E16','E17','E27','E35','E36','E37','HRS'])
    sec('I. Pay and leave records','E20',['E20','E28','E34','E41','E42'])
    sec('J. Review Decision 69983 — completeness (last)','E43',['E43'])
    jl=oi('K. Jump list (alphabetical)',key='E05')
    for k in sorted([k for k in BLOCKS if k not in ('F24N','F24R')],key=lambda k:BLOCKS[k]['title'].lower()):
        jl.children.append(oi(BLOCKS[k]['title'],key=k))
    r.append(jl)

# ---- metadata ----
with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta['dc:title']='Report B — Letter of instruction, enclosures and source documents — WC/2024/227'
    meta['dc:creator']=['Cory Shepherd']
di=pdf.docinfo
for k in list(di.keys()): del di[k]
di['/Title']='Report B — Letter of instruction, enclosures and source documents — WC/2024/227'
di['/Author']='Cory Shepherd'; di['/Creator']='Cory Shepherd'; di['/Producer']='Cory Shepherd'
pdf.save('_v6_raw.pdf')

# ---- rasterize label pages (purge stale text layers) ----
RAST=[fp('E04MAP')] + [src_final(sp) for sp in BFIX if BFIX[sp]] + [fp('HAWES'),fp('HAWES')+1]
RAST=sorted(set(RAST))
for pn in RAST:
    subprocess.run(['pdftoppm','-r','150','-jpeg','-jpegopt','quality=88','-f',str(pn),'-l',str(pn),'_v6_raw.pdf','r6_%d'%pn],check=True)
rpdf=pikepdf.open('_v6_raw.pdf')
for pn in RAST:
    img=[f for f in os.listdir('.') if f.startswith('r6_%d-'%pn) and f.endswith('.jpg')][0]
    cc=canvas.Canvas('ip6_%d.pdf'%pn,pagesize=A4); cc.drawImage(img,0,0,W,H); cc.save()
    ip=pikepdf.open('ip6_%d.pdf'%pn)
    annots=rpdf.pages[pn-1].get('/Annots')
    rpdf.pages[pn-1]=ip.pages[0]
    if annots is not None: rpdf.pages[pn-1].Annots=annots
rpdf.save('_v6_rast.pdf')
subprocess.run(['qpdf','--linearize','_v6_rast.pdf',OUT],check=True)
print('BUILT',OUT,len(rpdf.pages),'pages | Hawes at',fp('HAWES'),'| EnclA note at',fp('ENCLA'))
