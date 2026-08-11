#!/usr/bin/env python3
"""Stressor 1(a) particulars support bundle — tabs, headers, explainers."""
import subprocess
import pikepdf
from pikepdf import Name, Dictionary, Array
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
W,H = A4
INK=HexColor('#1a1a1a'); GREY=HexColor('#555555'); BAR=HexColor('#1b1b2f')
SRC='REPORT_B_LEAN_DOCTOR_PACK.pdf'

TABS = [
 ('TAB 1','Particular (i) — “Hello & Update” · database access removed · 18 July 2023',
  'On 18 July 2023, the appellant’s access to the switchboard database was removed by '
  'email ("Hello & Update"), while the duties requiring that access remained assigned to the appellant. '
  'The document behind this tab is the email of 18 July 2023.',
  [('S',105)]),
 ('TAB 2','Particular (ii) — On-call self-delegated · office hours never stated to the team · May 2024 (PP24)',
  'In about May 2024 (pay period 13–26 May 2024), after-hours on-call manager arrangements '
  'were changed and communicated by list, without consultation with switchboard operators. '
  'The documents behind this tab are: the after-hours on-call manager email (Ellen); the '
  'on-call self-delegation email (Ms Taylor); and the on-call and hours all-staff email of '
  '17 May 2024 (Ms Taylor).',
  [('S',123),('S',124),('S',125)]),
 ('TAB 3','Particular (iii) — The pleaded “erratic physical presence” · the MASPER register (urgent clinical call routing) · six days of errors while contact attempts went unanswered · 9–15 May 2024',
  'The MASPER register is used by switchboard to route urgent clinical calls to the responsible medical registrars; the criticality of the Switchboard function is among the admitted facts (Enclosure D to the letter of instruction). Between 9 and 15 May 2024, following the direction of 9 May 2024 concerning business-hours '
  'contact, errors accumulated in the MASPER register while switchboard remained responsible '
  'for call routing. On 15 May 2024 a pathologist was unable to hand over critical results for '
  'approximately two hours; the registrar’s return call criticised switchboard’s '
  'performance (witnessed by Ms P. Co). The documents behind this tab are the CS-1 MASPER '
  'course records, 9–15 May 2024. These records, with Tabs 2 and 6, particularise the “erratic physical presence” pleaded at Stressor 1(a).',
  [('S',68),('S',69),('S',70),('S',71)]),
 ('TAB 4','Particulars (iv)–(v) — “we can not help patients” · five days of misdirected clinical calls · the 2:05pm recommendation and the 4:30pm reply',
  'On 22 February 2024 the document "Outpatients Department – Clinic contact Details" was '
  'modified without notice to switchboard operators. On 15 May 2024 at 11:47am the Integrated '
  'Respiratory Service requested in writing, marked High importance, that the directory be '
  'corrected; on 20 May 2024 at 11:03am it wrote again, recording that misdirected clinical '
  'calls were continuing ("we continue to get calls… we can not help patients"). At 2:05pm '
  'on 20 May 2024 the appellant identified the modification of 22 February 2024 as the cause '
  'and recommended in writing a modification and review of the document. At 4:30pm Ms Taylor '
  'replied that "this task was being actioned," that she "had discussed with Richard this '
  'morning," and that "I believe you were aware of that." No record of any action preceding '
  'the appellant’s recommendation has been disclosed. The documents behind this tab are '
  'the "Respiratory Nurse Educators" email chain, 15–20 May 2024, from the Respondent’s '
  'disclosure.',
  [('X','resp_1.pdf'),('X','resp_2.pdf'),('X','resp_3.pdf')]),
 ('TAB 5','Particular (vi) — “more than two weeks without response” · 8 April – 1 May 2024',
  'The appellant’s written requests concerning the roster of 8 April 2024 received no '
  'substantive response until 1 May 2024; the appellant’s email of 24 April 2024 recorded more than two '
  'weeks without response; the request was refused on 1 May 2024. The documents behind this '
  'tab are the rostering concerns correspondence (April 2024) and the Roster Concerns chain '
  'of 26 April – 8 May 2024, including the 1 May 2024 refusal.',
  [('S',108),('S',109),('S',110),('S',111),('S',126),('S',127),('S',128),('S',129)]),
 ('TAB 6','Particular (vii) — Office hours asked in writing · the retract sent to the appellant only · 9–17 May 2024',
  'On 9 May 2024 Ms Taylor directed that she be contacted during business hours. During '
  '9–15 May 2024, repeated attempts to contact Ms Taylor during business hours went '
  'unanswered, and her office hours had not been stated to the team; on 15 May 2024 the '
  'appellant asked in writing that they be stated. The documents behind this tab are the '
  'hours sequence of four: the all-department hours emails (Ellen; Ms Taylor), the '
  'appellant’s office-hours request, and the retract email sent to the appellant only. '
  '(See also Tab 3 for the CS-1 records of the same period.)',
  [('S',155),('S',156),('S',157),('S',158)]),
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

c = canvas.Canvas('bundle_front.pdf', pagesize=A4)
# --- cover ---
c.setFillColor(INK)
c.setFont('Helvetica-Bold',15); c.drawString(57,H-70,'WC/2024/227')
c.setFont('Helvetica-Bold',13)
c.drawString(57,H-92,'Stressor 1(a) — Particulars support bundle')
c.setFont('Helvetica',10.5); c.setFillColor(GREY)
c.drawString(57,H-108,'Prepared in support of the appellant’s statement of evidence · Confidential')
c.setFillColor(INK); y=H-140
y=wrap(c,'This bundle collects the documents supporting the particulars of Stressor 1(a) of the '
 'Amended Form 9A (7 April 2026). Each tab carries one particular, stated in the terms in '
 'which it would be given, followed by the documents that record it. All documents are '
 'contemporaneous records; several are drawn from the Respondent’s own disclosure.',57,y,480,10,13.5)
y-=12
c.setFont('Helvetica-Bold',10.5); c.drawString(57,y,'INDEX'); y-=16
rows=[('Tab 1','(i) “Hello & Update” · database access removed','18 Jul 2023'),
      ('Tab 2','(ii) On-call self-delegated · hours never stated','May 2024 (PP24)'),
      ('Tab 3','(iii) “Erratic physical presence” · MASPER urgent-call routing · six days','9–15 May 2024'),
      ('Tab 4','(iv)–(v) “we can not help patients” · the 20 May exchange','22 Feb · 15–20 May 2024'),
      ('Tab 5','(vi) “more than two weeks without response”','8 Apr – 8 May 2024'),
      ('Tab 6','(vii) Office hours asked · retract to the appellant only','9–17 May 2024')]
c.setFont('Helvetica',10)
for t,d,dt in rows:
    c.setFont('Helvetica-Bold',10); c.drawString(60,y,t)
    c.setFont('Helvetica',10); c.drawString(110,y,d); c.drawString(430,y,dt); y-=15
y-=10
c.setFillColor(GREY)
y=wrap(c,'Note: each particular is pleaded under the categories of Stressor 1(a) as filed. The '
 'wording on each tab is the form in which further and better particulars would be given if '
 'required.',57,y,480,9,12)
c.setFillColor(GREY); c.setFont('Helvetica',8)
c.drawString(57,40,'Shepherd · WC/2024/227 · Stressor 1(a) particulars bundle')
c.showPage()
# --- tab dividers ---
for tab,(tabno,title,expl,_pages) in enumerate(TABS):
    c.setFillColor(BAR); c.rect(0,H-120,W,60,stroke=0,fill=1)
    c.setFillColor(white); c.setFont('Helvetica-Bold',22)
    c.drawString(57,H-98,tabno)
    c.setFillColor(INK)
    y=wrap(c,title,57,H-150,480,12.5,16,'Helvetica-Bold'); y-=10
    c.setFont('Helvetica-Oblique',9.5); c.setFillColor(GREY)
    c.drawString(57,y,'The particular, as it would be given:'); y-=16
    c.setFillColor(INK)
    y=wrap(c,expl,57,y,480,10.5,14.5)
    c.setFillColor(GREY); c.setFont('Helvetica',8)
    c.drawString(57,40,f'Shepherd · WC/2024/227 · Stressor 1(a) · {tabno}')
    c.showPage()
c.save()

src=pikepdf.open(SRC)
front=pikepdf.open('bundle_front.pdf')
pdf=pikepdf.new()
pdf.pages.append(front.pages[0])
tabstart=[]
EXT={}
for i,(tabno,title,expl,pages) in enumerate(TABS):
    tabstart.append(len(pdf.pages)+1)
    pdf.pages.append(front.pages[1+i])
    for kind,val in pages:
        if kind=='S': pdf.pages.append(src.pages[val-1])
        else:
            if val not in EXT: EXT[val]=pikepdf.open(val)
            pdf.pages.append(EXT[val].pages[0])
# strip inherited junk annots from resp pages
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
# bookmarks
from pikepdf import OutlineItem
with pdf.open_outline() as ol:
    ol.root.append(OutlineItem('Cover — index',destination=Array([pdf.pages[0].obj,Name.Fit])))
    for i,(tabno,title,_e,_p) in enumerate(TABS):
        ol.root.append(OutlineItem(f'{tabno} · {title}',destination=Array([pdf.pages[tabstart[i]-1].obj,Name.Fit])))
with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta['dc:title']='Stressor 1(a) — Particulars support bundle — WC/2024/227'
    meta['dc:creator']=['Cory Shepherd']
di=pdf.docinfo
for k in list(di.keys()): del di[k]
di['/Title']='Stressor 1(a) — Particulars support bundle — WC/2024/227'
di['/Author']='Cory Shepherd'; di['/Creator']='Cory Shepherd'; di['/Producer']='Cory Shepherd'
pdf.save('_1a_raw.pdf')
subprocess.run(['qpdf','--linearize','_1a_raw.pdf','STRESSOR_1A_PARTICULARS_BUNDLE_11AUG.pdf'],check=True)
print('BUILT', len(pdf.pages),'pages; tabs at',tabstart)
