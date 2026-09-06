#!/usr/bin/env python3
"""WC/2024/227 - EVENT MAP, June 2023 to July 2024. Events and emails from the notice to admit facts
served 28 August 2026; attendance from the Payroll leave takings report; roster from the published
Switchboard rosters. INTERNAL working map. Not for filing or service. Metadata stripped."""
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
B=ParagraphStyle('B',fontName='Helvetica',fontSize=8.6,leading=11,spaceAfter=4)
C=ParagraphStyle('C',parent=B,fontSize=7.0,leading=8.6,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
def c(t,st=C): return Paragraph(t,st)

EVJ=json.load(open('/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/f24events.json'))
LO,HI=dt.date(2023,6,1),dt.date(2024,7,31)
PLEAD=(dt.date(2026,5,13),dt.date(2026,8,14),dt.date(2026,2,18))
def lane(t):
    tl=t.lower()
    if re.search(r'\bavac\b|payroll|prn |wages|pay is|public holiday|penalty|remunerat|underpay|top up|toping up|validation of claims',tl): return ('PAY',colors.HexColor('#FFF2CC'))
    if re.search(r"the appellant (sent|wrote|replied|asked|emailed|made|submitted|lodged|gave|applied|recorded|forwarded)|appellant's (email|application|request|reply|grievance)|email of the appellant|that email of the appellant",tl): return ('ME',colors.HexColor('#DEEBF7'))
    if re.search(r'ms taylor|ms reese|ms stibbard|ms forrest|ms cridland|metro south|the employer|human resources|lbh_hr|mr pritchard',tl): return ('EMPLOYER',colors.HexColor('#FBE5D6'))
    if re.search(r'kwok|masper|marriott|dr wong|respiratory|met call|emergency code|parry',tl): return ('CLINICAL',colors.HexColor('#E2EFDA'))
    return ('RECORD',colors.HexColor('#F2F2F2'))
def tidy(t):
    t=re.sub(r'\s+',' ',t).strip()
    t=re.sub(r'^(On|That|The) ','',t)
    return (t[:230]+'…') if len(t)>230 else t
rowsev=collections.defaultdict(list)
for e in EVJ:
    d=dt.date.fromisoformat(e['date'])
    if not (LO<=d<=HI): continue
    if d in PLEAD: continue
    if re.search(r'amended statement of facts and contentions|amended List of Documents|does not allege|as presently constituted|Respondent admitted on 18 February', e['text']): continue
    rowsev[d].append(e)
# attendance
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
alldates=sorted(set(list(rowsev.keys())+list(lv.keys())))
s=[P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",HD),
   P("Matter No. WC/2024/227 | Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)",HD),
   P("EVENT MAP &ndash; June 2023 to July 2024",T),
   P("Every dated event in the notice to admit facts served 28 August 2026, every day of recorded absence, and the roster for "
     "each day, in one stream. Lanes: EMPLOYER (what management did) · ME (what I did or asked for) · PAY (pay and "
     "entitlements) · CLINICAL (what came in from clinicians and what the Switchboard did) · ABSENCE (payroll leave coding) · "
     "RECORD (documents and registers). Paragraph numbers are to the notice. Prepared 6 September 2026. INTERNAL working map, "
     "not for filing or service. Each lane proves a different thing and they are tendered separately.",SUB)]
data=[[c(x,CB) for x in ["Date","Roster","Lane","What happened","&para;"]]]
style=[('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#AAAAAA')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DDDDDD')),
       ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
       ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]
ri=1
for d in alldates:
    cell=L.get(d)
    ros = '&mdash;' if cell in (None,'-') else ('off' if cell=='x' else cell)
    items=[]
    if d in lv: items.append(('ABSENCE', ', '.join(sorted(set(lv[d]))), '', colors.HexColor('#F8CBAD')))
    for e in sorted(rowsev.get(d,[]), key=lambda x:x['n']):
        ln,col=lane(e['text'])
        txt=(f"<b>{e['time']}</b> &ndash; " if e['time'] else "")+tidy(e['text'])
        items.append((ln,txt,str(e['n']),col))
    for k,(ln,txt,ref,col) in enumerate(items):
        data.append([c(d.strftime('%a %d %b %y') if k==0 else ''), c(ros if k==0 else ''), c(f"<b>{ln}</b>"), c(txt), c(ref)])
        style.append(('BACKGROUND',(2,ri),(2,ri),col))
        if k==0: style.append(('LINEABOVE',(0,ri),(-1,ri),0.7,colors.HexColor('#666666')))
        ri+=1
t=Table(data,colWidths=[21*mm,20*mm,20*mm,W-73*mm,12*mm],repeatRows=1)
t.setStyle(TableStyle(style)); s.append(t)
buf=io.BytesIO(); doc=BaseDocTemplate(buf,pagesize=PS,leftMargin=10*mm,rightMargin=10*mm,topMargin=10*mm,bottomMargin=12*mm)
def footer(cv,dd):
    cv.saveState(); cv.setFont('Helvetica',7); cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(10*mm,6*mm,"WC/2024/227 - Event map Jun 2023 to Jul 2024 - INTERNAL, NOT FOR SERVICE")
    cv.drawRightString(PS[0]-10*mm,6*mm,f"Page {dd.page}"); cv.restoreState()
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(10*mm,12*mm,PS[0]-20*mm,PS[1]-22*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
doc.build(s); buf.seek(0); pdf=pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/EVENT_MAP_Jun2023-Jul2024_INTERNAL.pdf"; pdf.save(out,linearize=True)
print("built",out,len(pdf.pages),"pages |",len(data)-1,"rows |",len(alldates),"dates")
