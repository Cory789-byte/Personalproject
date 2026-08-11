#!/usr/bin/env python3
"""Stressor bundles 1-course, 2 and 3 — same template as the 1(a) bundle."""
import subprocess
import pikepdf
from pikepdf import Name, Array
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
W,H = A4
INK=HexColor('#1a1a1a'); GREY=HexColor('#555555'); BAR=HexColor('#1b1b2f')
SRC='REPORT_B_LEAN_DOCTOR_PACK.pdf'

BUNDLES = [
 # ---------------- STRESSOR 1 COURSE (1(b)-1(f)) ----------------
 dict(
  out='STRESSOR_1_COURSE_BUNDLE_1b-1f_11AUG.pdf',
  title='Stressor 1 — course documents · particulars 1(b), 1(d), 1(e), 1(f)',
  intro='This bundle collects the contemporaneous records for the pleaded particulars 1(b), '
   '1(d), 1(e) and 1(f) of Stressor 1 of the Amended Form 9A (7 April 2026). Particular 1(a) '
   'is the subject of its own bundle. Each event below is admitted in whole or in part on the '
   'Respondent’s pleadings, as noted tab by tab.',
  note='Particulars 1(c) and 1(g) rest on events admitted on the pleadings (SOFC ¶¶13, 17) '
   'and are carried in the appellant’s statement of evidence with their annexures.',
  tabs=[
   ('TAB 1','Particular 1(b) — Communication book · pages removed · 6 June 2023 (removal admitted)',
    'Ms Taylor removed pages from the Communication Book on or about 6 June 2023; the removal '
    'is admitted (SOFC ¶12(a)). The documents behind this tab are the communication book '
    'strand and the book pages of 6 June 2023 and 21 May 2024.',
    [72,73,74,130,131]),
   ('TAB 2','Particular 1(d) — COVID leave declined · "the attachments were in fact present" · Feb-Mar 2024',
    'The appellant’s Special Pandemic Leave submission was declined on the stated basis that '
    'the required declaration was not attached. The Respondent’s pleading records that "a '
    'review indicates that in fact, the attachments were present" and describes the decline as '
    'human error (SOFC ¶14(e)-(f)). The documents behind this tab are the contemporaneous '
    'text messages of February-March 2024 and the myHR leave submission system records.',
    [75,76,77,163]),
   ('TAB 3','Particular 1(e) — the public interest disclosure · lodged 13 May 2024 · determined 24 December 2024 (admitted)',
    'On 13 May 2024 the appellant lodged a complaint regarding clinical risks. The Ethical '
    'Standards Unit formally determined it constituted a Public Interest Disclosure; the '
    'particular is admitted in full (SOFC ¶15). The documents behind this tab are the ESU '
    'complaint face of 13 May 2024 and the PID outcome letter (24-ESU-1130).',
    [81,78,79,80]),
   ('TAB 4','Particular 1(f) — the retraction · "the email was ultimately removed from the server" · 15-17 May 2024',
    'On 15 May 2024 the appellant sent an email concerning office hours; a retraction was '
    'directed within approximately 48 hours, and the Respondent’s pleading records that '
    '"the email was ultimately removed from the server" (SOFC ¶16(b)(vii)). The documents '
    'behind this tab are the complaint and HR disclosure of 15-16 May 2024 (CS-4) and the '
    'office-hours and retract strand of 15-17 May 2024.',
    [82,83,84,85,86]),
  ]),
 # ---------------- STRESSOR 2 (pay) ----------------
 dict(
  out='STRESSOR_2_PAY_BUNDLE_11AUG.pdf',
  title='Stressor 2 — pay · particulars support bundle',
  intro='This bundle collects the records for the particulars of Stressor 2 of the Amended '
   'Form 9A (7 April 2026). The matter pleaded is the delay in the remediation of raised pay '
   'issues, not the quantum. The pleaded sequence is substantially admitted: pay issues raised '
   'over 2023-2024 (SOFC ¶20(a)); the payroll officer’s AVAC instruction of 3 May 2024 '
   '(¶21(a)); "waiting for payroll confirmation" on 21 May 2024 (¶21(b)); submission on '
   '28 May 2024 (¶21(c)) — twenty-five days after the instruction.',
  note='The text message of 4 April 2023 raising a pay issue is admitted (SOFC ¶19(a)) and '
   'is carried in the appellant’s statement annexures.',
  tabs=[
   ('TAB 1','"submit an AVAC" · the payroll instruction of 3 May 2024 and the correspondence to 28 May 2024',
    'On 3 May 2024 the payroll officer instructed Ms Taylor in writing to submit an AVAC to '
    'correct the appellant’s shift payments. The AVAC was submitted on 28 May 2024. The '
    'documents behind this tab are the payroll and underpayment correspondence of that period.',
    [88,89,90,91,92]),
   ('TAB 2','"waiting for payroll confirmation" · 21 May 2024 · eighteen days after the instruction',
    'On 21 May 2024 Ms Taylor advised the appellant she was still waiting on payroll '
    'confirmation and would submit an AVAC for the next pay run. The documents behind this '
    'tab are that exchange.',
    [106,107]),
   ('TAB 3','Queensland Health payroll disclosure package · the original records',
    'The original payroll correspondence and AVAC records produced in disclosure, behind this '
    'tab for completeness of the sequence.',
    [116,117,118,119,120,121,122]),
  ]),
 # ---------------- STRESSOR 3 (keystone) ----------------
 dict(
  out='STRESSOR_3_KEYSTONE_BUNDLE_11AUG.pdf',
  title='Stressor 3 — fatigue and rostering · the admitted 7-hour break · particulars support bundle',
  intro='This bundle collects the records for Stressor 3 of the Amended Form 9A (7 April '
   '2026). The central event is admitted: the shifts of 17 and 18 March 2024 were separated '
   'by a 7-hour break, described in the Respondent’s pleading as "a result of human error" '
   '(SOFC ¶22(a)). The Award default break is 10 hours; the June 2020 agreement relied on '
   'provides for 8. The documents below record the break, the requests for relief, the '
   'employer’s own contemporaneous risk assessment, and the state of the fatigue risk '
   'management framework in the material period.',
  note='Several documents are drawn from the Respondent’s own disclosure, as noted.',
  tabs=[
   ('TAB 1','The roster · 17-18 March 2024 · the admitted 7-hour break',
    'The roster for March 2024 records the consecutive shifts of 17 and 18 March 2024 ending '
    'at 23:00 and recommencing at 06:00. The break of 7 hours is admitted (SOFC ¶22(a)).',
    [56,57]),
   ('TAB 2','Att 6 · fatigue leave sought · the June 2020 agreement relied on · 19 March 2024',
    'Following the shifts of 17-18 March 2024, the appellant sought recovery leave. Paid '
    'fatigue leave was declined by reference to the agreement of June 2020, and the appellant '
    'used his own personal leave on 19 March 2024. The documents behind this tab are the Att 6 '
    'emails and the QH Leave Takings Report of 19 March 2024 (system record).',
    [58,59,162]),
   ('TAB 3','"a rating of 11 which is moderate" · the employer’s own risk assessment · 10 May 2024 (Respondent’s disclosure)',
    'On 10 May 2024 the appellant’s risk matrix was applied to the Switchboard roster by '
    'Ms Reese and Ms Taylor. The email records "at best there would be a rating of 11 which '
    'is moderate", refers to "a few rostering errors ... in past rosters", and records Ms '
    'Reese’s enquiry to Human Resources of 10 May 2024, followed up on 20 May 2024. The '
    'document behind this tab is that email, from the Respondent’s disclosure.',
    [159]),
   ('TAB 4','Raised in writing · 8 April - 1 May 2024 · "more than two weeks without response" · refused',
    'The appellant raised the shift pairing and minimum-break provision in writing on 8 April '
    '2024; it was escalated to Human Resources on 9 April 2024; his email of 24 April 2024 '
    'recorded more than two weeks without response; the request was refused on 1 May 2024. '
    'The documents behind this tab are the rostering concerns correspondence and the Roster '
    'Concerns chain including the 1 May 2024 refusal.',
    [108,109,110,111,112,113,126,127,128,129]),
   ('TAB 5','No Switchboard fatigue risk assessment in the material period · the Chief Executive’s letter · the guideline that applied',
    'The letter of 5 June 2026 under the hand of the Chief Executive (K-LM26/729) records the '
    'position concerning fatigue risk management in the Switchboard in the material period, '
    'with implementation of the framework after 30 June 2024. The guideline QH-GDL-401-3.3 '
    'is extracted for the standard that applied. Both documents are behind this tab.',
    [60,61,62,63,64,65,66,67]),
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

src = pikepdf.open(SRC)
for B in BUNDLES:
    front_fn = B['out'].replace('.pdf','_front.pdf')
    c = canvas.Canvas(front_fn, pagesize=A4)
    # cover
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold',15); c.drawString(57,H-70,'WC/2024/227')
    y = wrap(c,B['title'],57,H-92,480,13,17,'Helvetica-Bold')
    c.setFont('Helvetica',10.5); c.setFillColor(GREY)
    c.drawString(57,y-2,'Prepared in support of the appellant’s statement of evidence')
    c.setFont('Helvetica',9.5)
    c.drawString(57,y-16,'Cory Lea Shepherd · Appellant (self-represented) · AO3 Switchboard Services, Logan Hospital')
    c.drawString(57,y-29,'0417 400 227 · coryshepherd1@hotmail.com · 11 August 2026')
    c.setFillColor(INK); y = y-55
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
    # dividers
    for tabno,title,expl,_p in B['tabs']:
        c.setFillColor(BAR); c.rect(0,H-120,W,60,stroke=0,fill=1)
        c.setFillColor(white); c.setFont('Helvetica-Bold',22)
        c.drawString(57,H-98,tabno)
        c.setFillColor(INK)
        y = wrap(c,title,57,H-150,480,12.5,16,'Helvetica-Bold'); y-=10
        c.setFont('Helvetica-Oblique',9.5); c.setFillColor(GREY)
        c.drawString(57,y,'The particular, as it would be given:'); y-=16
        c.setFillColor(INK)
        y = wrap(c,expl,57,y,480,10.5,14.5)
        c.setFillColor(GREY); c.setFont('Helvetica',8)
        c.drawString(57,40,f'Shepherd · WC/2024/227 · {tabno}')
        c.showPage()
    c.save()
    # assemble
    front = pikepdf.open(front_fn)
    pdf = pikepdf.new()
    pdf.pages.append(front.pages[0])
    tabstart=[]
    for i,(tabno,title,_e,pages) in enumerate(B['tabs']):
        tabstart.append(len(pdf.pages)+1)
        pdf.pages.append(front.pages[1+i])
        for sp in pages: pdf.pages.append(src.pages[sp-1])
    # strip inherited junk annots
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
    from pikepdf import OutlineItem
    with pdf.open_outline() as ol:
        ol.root.append(OutlineItem('Cover — index',destination=Array([pdf.pages[0].obj,Name.Fit])))
        for i,(tabno,title,_e,_p) in enumerate(B['tabs']):
            ol.root.append(OutlineItem(f'{tabno} · {title[:90]}',destination=Array([pdf.pages[tabstart[i]-1].obj,Name.Fit])))
    with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
        meta['dc:title']=B['title']+' — WC/2024/227'
        meta['dc:creator']=['Cory Lea Shepherd']
        meta['dc:description']='Shepherd v Workers’ Compensation Regulator · WC/2024/227'
    di=pdf.docinfo
    for k in list(di.keys()): del di[k]
    di['/Title']=B['title']+' — WC/2024/227'
    di['/Author']='Cory Lea Shepherd'; di['/Creator']='Cory Lea Shepherd'; di['/Producer']='Cory Lea Shepherd'
    di['/Subject']='Shepherd v Workers’ Compensation Regulator · WC/2024/227'
    raw=B['out'].replace('.pdf','_raw.pdf')
    pdf.save(raw)
    subprocess.run(['qpdf','--linearize',raw,B['out']],check=True)
    print('BUILT',B['out'],len(pdf.pages),'pages')
