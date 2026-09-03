import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak, Image
from PIL import Image as PILImage
from timeline_data import EVENTS

H1=PS('h1',fontName='Helvetica-Bold',fontSize=14,leading=17,spaceAfter=4)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=10.8,leading=14,spaceBefore=11,spaceAfter=4)
B=PS('b',fontName='Helvetica',fontSize=9.3,leading=12.6,spaceAfter=6)
BL=PS('bl',fontName='Helvetica',fontSize=9.3,leading=12.6,spaceAfter=5,leftIndent=9*mm,firstLineIndent=-5*mm)
SM=PS('sm',fontName='Helvetica',fontSize=7.9,leading=9.9)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=7.9,leading=9.9)

# ---- assign tab numbers and open sources ----
tabs=[]           # (tabno, path)
seen={}
for e in EVENTS:
    p=e[4]
    if p and p not in seen:
        seen[p]=len(tabs)+1
        tabs.append((len(tabs)+1,p))
def tabno(p): return seen.get(p)

def img_page(path,caption):
    b=io.BytesIO(); im=PILImage.open(path); w,h=im.size
    d=SimpleDocTemplate(b,pagesize=A4,leftMargin=14*mm,rightMargin=14*mm,topMargin=12*mm,bottomMargin=12*mm,title='',author='')
    sc=min((A4[0]-28*mm)/w,(A4[1]-42*mm)/h)
    d.build([P(caption,SMB),Spacer(1,3),Image(path,width=w*sc,height=h*sc)])
    b.seek(0); return pikepdf.open(b)

srcs=[]; counts=[]
for n,p in tabs:
    d = img_page(p, f'TAB {n} — SMS, 2 September 2026') if p.lower().endswith(('.jpg','.jpeg','.png')) else pikepdf.open(p)
    srcs.append(d); counts.append(len(d.pages))

FINDINGS=[
 ('1. No instrument has ever been identified.','From 3 July 2026 Mr Shepherd was directed away from the workplace. He asked for the source of that power in the Stage 1 process on 4 August 2026 and repeatedly afterwards. Six positions have been advanced in nine weeks — sick leave by default (2 July); the QSuper claim manager (15 July); further medical information (29 July); the delegate\'s approval of the RFMI (30 July); "reduced roster 0.5 FTE" (31 August); and the pay cycle (3 September). None identifies a power to direct a fit and available employee away from work, and none of them is a decision.'),
 ('2. No decision has ever been made.','No written decision returning Mr Shepherd to work within the restrictions of 3 July 2026, or declining to, identifying the instrument and the officer, has ever been issued. The application for special leave on full pay made on 28 July and 5 August 2026 has been neither granted nor refused.'),
 ('3. The employer\'s own medical document contradicts the exclusion.','The Employee Capability Checklist of 3 July 2026 was completed on Metro South Health\'s own form. It certifies fitness with restrictions and records that "usual switchboard operational duties remain suitable", excluding only complaint handling — and even then complaints are to be "logged and redirected, not actioned or resolved". It records the recommended pattern as one Mr Shepherd "has in fact worked and tolerated over the past twelve months". The task-by-task match of the role description against that document, demanded on 28 July 2026, has never been produced.'),
 ('4. The employer\'s own delegate contradicts the hours.','Scott Hughes approved reduced part-time hours on 27 February, 17 April and 9 June 2026, and then described the employment as "Permanent Full-time (76 hours per fortnight)" in the RFMI of 31 July 2026. The last reduced-hours arrangement expired on 28 June 2026 by its own terms and nothing replaced it. The leave applied on 31 August 2026 was nevertheless applied at "0.5 FTE".'),
 ('5. The leave type was chosen, not defaulted to.','Each "Sick Leave – No Pay" entry is a positive act — a leave type selected from those available and submitted on the employee\'s behalf. The alternatives were available and known to the person entering them: on 4 August 2026 the recreation leave balance was identified as 41.21 hours and an undertaking given to apply it "to ensure you receive the available paid leave entitlement for this period". Of the leave types in play, three produce a payment and one does not. The one that does not was selected, and selected again on each subsequent day, after the written instruction of 3 July 2026 and after every objection since.'),
 ('6. The entries were unauthorised on the employer\'s own policy.','HR Policy C13 (QH-POL-188) section 6 permits a line manager to submit leave on an employee\'s behalf only where "the employee\'s request for leave is documented in writing" and supporting documents "are sourced and retained". The written requests on the record are annual leave (3 July) and special leave on full pay (5 August). There is no written request for sick leave without pay, and on 31 August 2026 Mr Shepherd confirmed in terms that he was not applying for personal leave.'),
 ('7. Payment was never declined — only its source.','The email of 5 August 2026 declines recreation leave and in the same sentence nominates special leave on full pay instead, which under Directive 12/24 is not debited from any leave account. What was declined was the funding of an employer-directed absence out of the employee\'s own accrued credits.'),
 ('8. The obligation to correct was mandatory and was not discharged.','HR Policy C13 section 2 provides that a line manager notified of an incorrect wage payment "must take all steps to rectify the error including … preparing and submitting further forms … liaising with Payroll to correct the error". Notice was given on 3 July 2026 and on fourteen occasions since. The corrective form was submitted once, for one fortnight, on 31 August 2026.'),
 ('9. The dispute procedure has not been followed.','The Stage 1 notice was given on 3 August 2026. Clause 1.11.2(a) requires Stage 1 discussions within 24 hours and provides that the procedure "should not extend beyond seven days". The 24-hour requirement was conceded on 4 August 2026 as not achieved. The seven days expired on 10 August 2026. No outcome has ever been communicated. Clause 1.11.4 provides that "the status quo existing before the emergence of a dispute is to continue whilst the procedure is being followed"; the status quo before 3 August 2026 has not been maintained. Clause 1.11.5 provides that "no party shall act in a manner unreasonably or intentionally delay the timely resolution of a dispute".'),
 ('10. The defect now supplies its own justification.','Periods recorded as leave without pay are excluded from continuous service. On 3 September 2026 Payroll advised that long service leave eligibility arises "only from 04/09/2026" — 163 days after the date on which seven years\' continuous service fell due on the service dates recorded in the agreement under which Mr Shepherd was reinstated. The coding objected to since 3 July has deferred the entitlement now relied on to refuse the leave, and it moves a day further out for each day it continues.'),
 ('11. The loss.','Four pay days have passed with nil paid: 29 July, 12 August and 26 August 2026, and 15 July for the balance of the period. At the substantive 76 hours per fortnight and the base rate of $44.46 per hour, a fortnight is $3,378.96 gross. Three full fortnights unpaid is $10,136.88, and the shortfall on the fortnight 17–30 August, processed at half hours, is a further $1,689.48 — approximately $11,800 gross to 30 August 2026, exclusive of shift penalties, superannuation and leave accrual. The consequence, stated to the employer in writing on 31 August and 2 September 2026, is the loss of accommodation.'),
]

def build_front(start):
    s=[P('THE EMPLOYMENT RECORD — ANALYSIS, COMPLETE CHRONOLOGY AND ORIGINAL DOCUMENTS',H1),
       P('Cory Shepherd, employee number 388372 · AO3, Switchboard Services, Logan Hospital, Metro South Health · February to 3 September 2026 · compiled 3 September 2026',SM),
       Spacer(1,8),
       P('PART A — WHAT THE RECORD SHOWS',H2)]
    for h,b in FINDINGS: s.append(P(f'<b>{h}</b> {b}',BL))
    s.append(PageBreak())
    s.append(P('PART B — THE COMPLETE CHRONOLOGY',H2))
    s.append(P('Every communication event on the employment matter, in date order. The Tab column gives the page range of the original document in Part C. Events without a tab are recorded from the correspondence itself or from contemporaneous note.',B))
    rows=[[P('<b>Date</b>',SMB),P('<b>Time</b>',SMB),P('<b>Between</b>',SMB),P('<b>What happened</b>',SMB),P('<b>Tab</b>',SMB)]]
    # page start per tab
    pg=start; pages={}
    for (n,p),c in zip(tabs,counts):
        pages[n]=(pg,pg+c-1); pg+=c
    for d,t,a,w,p in EVENTS:
        tn=tabno(p) if p else None
        cell=f'{tn}<br/><font size="6.5">pp {pages[tn][0]}–{pages[tn][1]}</font>' if tn else '—'
        rows.append([P(d,SM),P(t,SM),P(a,SM),P(w,SM),P(cell,SM)])
    tb=Table(rows,colWidths=[19*mm,14*mm,30*mm,93*mm,14*mm],repeatRows=1)
    tb.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    s.append(tb)
    s.append(PageBreak())
    s.append(P('PART C — THE ORIGINAL DOCUMENTS',H2))
    s.append(P('Each tab is the original document as sent or received. Nothing has been retyped.',B))
    rows=[[P('<b>Tab</b>',SMB),P('<b>Document</b>',SMB),P('<b>Pages</b>',SMB)]]
    for (n,p),c in zip(tabs,counts):
        rows.append([P(str(n),SM),P(p.replace('../documents/',''),SM),P(f'{pages[n][0]}–{pages[n][1]}' if c>1 else str(pages[n][0]),SM)])
    tb=Table(rows,colWidths=[10*mm,144*mm,16*mm],repeatRows=1)
    tb.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    s.append(tb)
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=15*mm,bottomMargin=14*mm,title='',author='')
    doc.build(s); buf.seek(0); return pikepdf.open(buf)

fr=build_front(1)
for _ in range(3):
    n=len(fr.pages); fr2=build_front(n+1)
    if len(fr2.pages)==n: fr=fr2; break
    fr=fr2
print('front pages',len(fr.pages))
out=pikepdf.new(); out.pages.extend(fr.pages)
for d in srcs: out.pages.extend(d.pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
if '/Names' in r and '/EmbeddedFiles' in r.Names: del r.Names['/EmbeddedFiles']
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/EMPLOYMENT_RECORD_analysis_chronology_originals_3SEP2026.pdf',fix_metadata_version=False)
print('TOTAL PAGES',len(out.pages),'| tabs',len(tabs))
