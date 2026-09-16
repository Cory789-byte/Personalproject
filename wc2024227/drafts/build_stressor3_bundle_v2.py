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
 dict(
  out='STRESSOR_3_FATIGUE_ROSTERING_BUNDLE_11AUG.pdf',
  title='Stressor 3 — fatigue and rostering · the admitted 7-hour break · particulars support bundle',
  intro='This bundle collects the records for Stressor 3 of the Amended Form 9A (7 April '
   '2026). The central event is admitted: the shifts of 17 and 18 March 2024 were separated '
   'by a 7-hour break, described in the Respondent\u2019s pleading as "a result of human error" '
   '(SOFC \u00b622(a)). The Award default break is 10 hours; the June 2020 agreement relied on '
   'provides for 8, and was signed on 17 June 2020 \u2014 some four years before the shifts in '
   'question. The documents below record the break, the written requests and replies, the '
   'employer\u2019s own contemporaneous risk assessment, and the state of the fatigue risk '
   'management framework in the material period.',
  note='The rostering-concerns correspondence of April-May 2024 (8 April to the 1 May 2024 '
   'refusal) is collected in the Stressor 1(a) particulars support bundle and is not '
   'duplicated here. Several documents are drawn from the Respondent\u2019s own disclosure.',
  tabs=[
   ('TAB 1','The roster · 17-18 March 2024 · the admitted 7-hour break',
    'The roster for March 2024 records the consecutive shifts of 17 and 18 March 2024 ending '
    'at 23:00 and recommencing at 06:00. The break of 7 hours is admitted (SOFC \u00b622(a)).',
    [56,57]),
   ('TAB 2','Raised in writing · 8 and 24 April 2024 · "a minimum of a ten-hour break between shifts" · the reply: the on-call role and the part-time review',
    'On 8 April 2024 at 3:56pm the appellant requested in writing, marked High importance, a '
    'review of payment for the pay period 8-31 March 2024, enclosing "policies that delineate '
    'both public holiday payments and additional payments applicable in cases where employees '
    'are not rostered a minimum of a ten-hour break between shifts." He followed up on 24 '
    'April 2024 at 3:15pm, also marked High importance. Ms Taylor\u2019s reply recorded that a '
    'Payroll investigation was underway, that entitlements were being reviewed for "your '
    'tenure as a part-time employee," attached an after-hours protocol, and stated: "As the '
    'Switchboard Manager, it is part of my role to be on call after hours for urgent matters, '
    'which include emergencies like any general codes (Code Red, Yellow, Purple, Brown, and '
    'Orange), system outages or staffing issues due to illness." The documents behind this '
    'tab are that exchange (Att 6).',
    [58,59]),
   ('TAB 3','Recovery leave · 19 March 2024 · the system record · the agreement of 17 June 2020 relied on',
    'Following the shifts of 17-18 March 2024, the appellant took leave on 19 March 2024 '
    '(SOFC \u00b622(c)). Paid fatigue leave was declined by reference to the agreement of 17 June '
    '2020 (SOFC \u00b622(e)) \u2014 an agreement signed some four years before the shifts in '
    'question. The document behind this tab is the QH Leave Takings Report of 19 March 2024 '
    '(system record). [The written refusal and the appellant\u2019s correspondence concerning '
    'travel time are held in the complete Att 6 records and will be provided in the '
    'appellant\u2019s statement annexures.]',
    [162]),
   ('TAB 4','"a rating of 11 which is moderate" · the employer\u2019s own risk assessment · 10 May 2024 (Respondent\u2019s disclosure)',
    'On 10 May 2024 the appellant\u2019s risk matrix was applied to the Switchboard roster by '
    'Ms Reese and Ms Taylor. The email records "at best there would be a rating of 11 which '
    'is moderate", refers to "a few rostering errors ... in past rosters", and records Ms '
    'Reese\u2019s enquiry to Human Resources of 10 May 2024, followed up on 20 May 2024. The '
    'document behind this tab is that email, from the Respondent\u2019s disclosure.',
    [159]),
   ('TAB 5','No Switchboard fatigue risk assessment in the material period · the Chief Executive\u2019s letter · the guideline that applied',
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
