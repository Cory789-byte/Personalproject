#!/usr/bin/env python3
"""WC/2024/227 - 17 MARCH TO 31 OCTOBER 2024, DAY BY DAY. Roster, attendance, every dated event in the
served notice, and the medical, WorkCover and employment milestones. INTERNAL. Not for filing or service."""
import io, pikepdf, json, re, sys, datetime as dt, collections, openpyxl
sys.path.insert(0,'.'); from roster_data import R, cells
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer
PS=landscape(A4); W=PS[0]-20*mm
HD=ParagraphStyle('HD',fontName='Helvetica-Bold',fontSize=8.2,leading=10.2,textColor=colors.HexColor('#333333'))
T=ParagraphStyle('T',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=2)
SUB=ParagraphStyle('S',fontName='Helvetica-Oblique',fontSize=7.6,leading=10,textColor=colors.HexColor('#555555'),spaceAfter=6)
H1=ParagraphStyle('H1',fontName='Helvetica-Bold',fontSize=10.5,leading=13.5,spaceBefore=7,spaceAfter=4)
B=ParagraphStyle('B',fontName='Helvetica',fontSize=8.6,leading=11,spaceAfter=4)
C=ParagraphStyle('C',parent=B,fontSize=7.0,leading=8.6,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
def c(t,st=C): return Paragraph(t,st)
LO,HI=dt.date(2024,3,17),dt.date(2024,10,31)
COL={'EMPLOYER':colors.HexColor('#FBE5D6'),'ME':colors.HexColor('#DEEBF7'),'PAY':colors.HexColor('#FFF2CC'),
     'CLINICAL':colors.HexColor('#E2EFDA'),'ABSENCE':colors.HexColor('#F8CBAD'),'RECORD':colors.HexColor('#F2F2F2'),
     'MEDICAL':colors.HexColor('#D9E1F2'),'WORKCOVER':colors.HexColor('#E4DFEC'),'EMPLOYMENT':colors.HexColor('#F4CCCC')}
# curated milestones: (date, lane, text, source)
M=[
 (dt.date(2024,3,17),'ROSTER','Rostered 15:00&ndash;23:00, the last shift of the fortnight 4&ndash;17 March 2024. Finish 23:00.','published roster PP20'),
 (dt.date(2024,3,18),'ROSTER','Commenced 06:00. A break of seven hours, admitted by the Respondent. The published roster for 18&ndash;31 March 2024 contains no line for the Appellant. Six emergency codes between 06:00 and 14:00, including two neonatal MET calls.','roster PP21; code register; SOFC &para;22(a)'),
 (dt.date(2024,3,19),'ABSENCE','Sick leave, 7.6 hours, approved.','Leave Takings Report; Item 15'),
 (dt.date(2024,4,8),'ME','Emailed Ms Taylor requesting a review of payment and noting the Award requires a minimum 10-hour break.','Review Decision'),
 (dt.date(2024,4,9),'EMPLOYER','Ms Taylor replied, said she had escalated the fatigue leave enquiry to Human Resources, and directed the older dates to MyHR payroll enquiries.','Review Decision'),
 (dt.date(2024,4,24),'ME','Emailed that it had been "more than 2 weeks without any response".','Review Decision'),
 (dt.date(2024,5,1),'EMPLOYER','Fatigue leave refused, 23 days after the request, "due to the existing 8-hour agreement signed by you on 17 June 2020".','Review Decision'),
 (dt.date(2024,6,3),'ROSTER','Rostered 15:00&ndash;23:00 and worked. <b>The last shift actually worked.</b>','roster PP26; Leave Takings Report'),
 (dt.date(2024,6,10),'MEDICAL','Great-grandfather died. Leave without pay this day; bereavement leave 11 and 12 June.','family record; Leave Takings Report'),
 (dt.date(2024,6,18),'MEDICAL','<b>Onset of injury as pleaded.</b> Rostered 14:00&ndash;22:00 but recorded as leave without pay. Ms Taylor emailed the team at 8:58 am: "I am taking today off" and "I am sorry I haven\'t been there for you all over the past week".','Leave Takings Report; Notice &para;&para;85&ndash;87'),
 (dt.date(2024,6,28),'MEDICAL','General practice, Dr Bogdan Slawinski. Reason for visit "Anxiety". Note records "stress at work" and "upset by people not following rules". Melatonin prescribed.','GP records'),
 (dt.date(2024,7,1),'MEDICAL','General practice, Dr Peter Hawes. Reason for visit "work stress". Note records "ethical complaint about manager and director", "they withhold pay at times, no overtime- not processed, manipulate his roster- so he works lates then earlies", "they don\'t listen to his complaints", "all this is stressing him out, causing anxiety". Work capacity certificate issued: injury date 18/06/2024, first seen for this injury 01/07/2024, diagnoses "anxiety, stress", no functional capacity.','GP records; certificate'),
 (dt.date(2024,7,1),'WORKCOVER','<b>Application for compensation lodged</b>, claim S23LW142013.','Review Decision; LOD item 1'),
 (dt.date(2024,7,12),'EMPLOYMENT','Meeting scheduled by the employer while the Appellant was on certified leave. Email to WorkCover with initial information and an undated "Event overview".','Amended 9A &para;3(a); LOD item 12'),
 (dt.date(2024,7,16),'EMPLOYMENT','Second meeting scheduled while on certified leave.','Amended 9A &para;3(a)'),
 (dt.date(2024,7,18),'WORKCOVER','Emails to WorkCover regarding pay issues, and forwarding a witness statement of Ms Carolyn Jeffrey.','LOD items 13, 14'),
 (dt.date(2024,8,7),'MEDICAL','Work capacity certificate, Dr Ki Pang. Injury date 18/06/2024, first seen 01/07/2024, no functional capacity to 09/08/2024.','LOD item 8; certificate'),
 (dt.date(2024,8,9),'WORKCOVER','Two responses to the review, including that the 7-hour break "did not include travel time" and that with travel the break "would have been less than 5 hours".','Review Decision'),
 (dt.date(2024,8,11),'MEDICAL','Work capacity certificate, Dr Hawes. No functional capacity to 08/09/2024.','LOD item 7; certificate'),
 (dt.date(2024,9,2),'MEDICAL','<b>Dr Hawes told WorkCover that work events were the sole cause of the psychological injury</b>, and the certificates maintained that there was no pre-existing factor or condition.','Review Decision, p 17'),
 (dt.date(2024,9,6),'EMPLOYMENT','Employer\'s response to the review: no evidence pay was withheld; corrective action taken per internal process; confirms a change to the employment contract and adjustments in working hours since June 2020.','Review Decision'),
 (dt.date(2024,9,8),'MEDICAL','Work capacity certificate, Dr Hawes, signed 08/09/2024. No functional capacity to 06/10/2024. <b>Referral to a psychiatrist recorded.</b>','LOD item 7; certificate'),
 (dt.date(2024,9,13),'WORKCOVER','<b>WorkCover rejected the application.</b>','LOD item 2'),
 (dt.date(2024,9,16),'WORKCOVER','Application for review lodged with the Workers\' Compensation Regulator.','LOD item 3; Review Decision'),
 (dt.date(2024,9,18),'RECORD','The review record closes. Nothing in the 28 pages of the review decision post-dates this day.','Review Decision, evidence list'),
 (dt.date(2024,9,20),'EMPLOYMENT','<b>Separation date</b> later recorded in the deed of settlement as the date of the Dismissal.','Deed of settlement, recital D, cl 1'),
 (dt.date(2024,9,26),'EMPLOYMENT','Metro South show cause letter, abandonment of employment, ref K-CF24-3196.','repository document'),
 (dt.date(2024,9,30),'ROSTER','<b>Published roster for 30 September to 13 October 2024 lists the Appellant as FT, payroll 388372, and rosters him on early, late and afternoon shifts across the fortnight.</b>','published roster PP09'),
 (dt.date(2024,10,9),'EMPLOYMENT','Metro South letter confirming abandonment of employment, ref K-CF24-3270. The deed records the correspondence as received on 8 October 2024.','repository document; Deed recital C'),
 (dt.date(2024,10,11),'ME','Reply to the abandonment letter sent.','repository document'),
 (dt.date(2024,10,14),'ROSTER','<b>Published roster for 14 to 27 October 2024 again lists the Appellant as FT, payroll 388372, and rosters him on shifts including three consecutive night shifts</b>, in a fortnight beginning after the letter confirming abandonment.','published roster PP10'),
 (dt.date(2024,10,22),'WORKCOVER','Review decision made.','Review Decision, p 1'),
 (dt.date(2024,10,24),'MEDICAL','<b>11:45 am</b> &ndash; first consultation with Dr Ravikumar Bangalore Krishnaiah. The practice confirmed in writing that day: "you are suffering from psychological injury of Major Depressive Disorder with anxiety state and obsessive preoccupation about work cover claim and perceived injustice to an extent that your selfcare and daily activities have been neglected." Fluoxetine increased to two capsules "from today"; Seroquel 25 mg commenced at night.','LOD item 9; practice email'),
 (dt.date(2024,10,24),'WORKCOVER','<b>Review Decision 69983</b>, reasons dated this day. Finds a personal injury of a psychological nature; finds employment a significant contributing factor as to factors 2, 3 and 4; finds the rostering of 17&ndash;18 March 2024 amounted to unreasonable management action; and excludes the injury on a global evaluation.','Review Decision, pp 16&ndash;17, 26&ndash;27'),
 (dt.date(2024,10,24),'ME','<b>5:12 pm</b> &ndash; emailed QSuper: "I have finally been able to see a psychiatrist today", attaching a medical certificate, and reporting "a lot of financial distress".','QSuper correspondence bundle'),
 (dt.date(2024,10,25),'EMPLOYMENT','Application for reinstatement filed in the Commission, TD/2024/110, stamped 25 October 2024.','related matters'),
]
EVJ=json.load(open('/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/f24events.json'))
def lane(t):
    tl=t.lower()
    if re.search(r'\bavac\b|payroll|prn |wages|public holiday|penalty|top up|toping up|validation of claims',tl): return 'PAY'
    if re.search(r"the appellant (sent|wrote|replied|asked|emailed|made|submitted|lodged|gave|applied|recorded|forwarded)|appellant's (email|application|request|reply)|email of the appellant",tl): return 'ME'
    if re.search(r'ms taylor|ms reese|ms stibbard|ms forrest|metro south|the employer|human resources|lbh_hr|pritchard',tl): return 'EMPLOYER'
    if re.search(r'kwok|masper|marriott|dr wong|respiratory|met call|emergency code|code blue|code grey|parry',tl): return 'CLINICAL'
    return 'RECORD'
def tidy(t):
    t=re.sub(r'\s+',' ',t).strip(); t=re.sub(r'^(On|That|The) ','',t)
    return (t[:225]+'…') if len(t)>225 else t
rows=collections.defaultdict(list)
for e in EVJ:
    d=dt.date.fromisoformat(e['date'])
    if not (LO<=d<=HI): continue
    if re.search(r'amended statement of facts and contentions|amended List of Documents|does not allege|as presently constituted|Respondent admitted on 18 February', e['text']): continue
    rows[d].append((lane(e['text']), (f"<b>{e['time']}</b> &ndash; " if e['time'] else "")+tidy(e['text']), str(e['n'])))
for d,ln,txt,src in M:
    if LO<=d<=HI: rows[d].append((ln, txt+f" <i>[{src}]</i>", ''))
L={}
for st,(lab,line,unc) in R.items(): L.update(cells(st,line))
wb=openpyxl.load_workbook('../documents/2026-09-04_Leave_Takings_Report_25MAR2019-04SEP2026_FULL.xlsx',read_only=True,data_only=True)
lv=collections.defaultdict(list)
for ws in wb.worksheets:
    for r in ws.iter_rows(values_only=True):
        if r and len(r)>8 and r[1]=='00388372' and r[6]:
            rng=str(r[6]).split(' - ')
            d0=dt.datetime.strptime(rng[0].strip(),'%d/%m/%Y').date()
            d1=dt.datetime.strptime(rng[-1].strip(),'%d/%m/%Y').date()
            for k in range((d1-d0).days+1):
                dd=d0+dt.timedelta(k)
                if LO<=dd<=HI: lv[dd].append(str(r[4]))
# collapse long unbroken LWOP runs
alld=sorted(set(list(rows.keys())+list(lv.keys())))
s=[P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",HD),
   P("Matter No. WC/2024/227 | Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)",HD),
   P("17 MARCH TO 31 OCTOBER 2024 &ndash; THE FULL SEQUENCE",T),
   P("From the seven-hour break to the diagnosis. Roster from the published Switchboard rosters; attendance from the Payroll "
     "leave takings report of 4 September 2026; events from the notice to admit facts served 28 August 2026 with paragraph "
     "numbers; medical, WorkCover and employment milestones sourced against each entry. Unbroken runs of leave without pay are "
     "collapsed to a single line. Prepared 6 September 2026. INTERNAL working chronology, not for filing or service.",SUB)]
data=[[c(x,CB) for x in ["Date","Roster","Lane","What happened","&para;"]]]
style=[('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#AAAAAA')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DDDDDD')),
       ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
       ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]
ri=1; i=0
while i < len(alld):
    d=alld[i]
    if d in lv and d not in rows and set(lv[d])=={'Leave Without Pay'}:
        j=i
        while j+1<len(alld) and alld[j+1] not in rows and alld[j+1] in lv and set(lv[alld[j+1]])=={'Leave Without Pay'}: j+=1
        if j>i:
            data.append([c(f"<b>{alld[i].strftime('%d %b')} &ndash; {alld[j].strftime('%d %b %y')}</b>"),c('&mdash;'),c("<b>ABSENCE</b>"),
                         c(f"Leave without pay on every rostered day, {(alld[j]-alld[i]).days+1} days."),c('')])
            style.append(('BACKGROUND',(2,ri),(2,ri),COL['ABSENCE'])); style.append(('LINEABOVE',(0,ri),(-1,ri),0.7,colors.HexColor('#666666')))
            ri+=1; i=j+1; continue
    cell=L.get(d); ros='&mdash;' if cell in (None,'-') else ('off' if cell=='x' else cell)
    items=[]
    if d in lv: items.append(('ABSENCE', ', '.join(sorted(set(lv[d]))), ''))
    items += rows.get(d,[])
    for k,(ln,txt,ref) in enumerate(items):
        data.append([c(d.strftime('%a %d %b %y') if k==0 else ''), c(ros if k==0 else ''), c(f"<b>{ln}</b>"), c(txt), c(ref)])
        style.append(('BACKGROUND',(2,ri),(2,ri),COL.get(ln,colors.HexColor('#F2F2F2'))))
        if k==0: style.append(('LINEABOVE',(0,ri),(-1,ri),0.7,colors.HexColor('#666666')))
        ri+=1
    i+=1
t=Table(data,colWidths=[23*mm,18*mm,21*mm,W-74*mm,12*mm],repeatRows=1)
t.setStyle(TableStyle(style)); s.append(t)
buf=io.BytesIO(); doc=BaseDocTemplate(buf,pagesize=PS,leftMargin=10*mm,rightMargin=10*mm,topMargin=10*mm,bottomMargin=12*mm)
def footer(cv,dd):
    cv.saveState(); cv.setFont('Helvetica',7); cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(10*mm,6*mm,"WC/2024/227 - 17 March to 31 October 2024 - INTERNAL, NOT FOR SERVICE")
    cv.drawRightString(PS[0]-10*mm,6*mm,f"Page {dd.page}"); cv.restoreState()
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(10*mm,12*mm,PS[0]-20*mm,PS[1]-22*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
doc.build(s); buf.seek(0); pdf=pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/CHRONOLOGY_17Mar-31Oct2024_INTERNAL.pdf"; pdf.save(out,linearize=True)
print("built",out,len(pdf.pages),"pages |",len(data)-1,"rows")
