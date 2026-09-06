#!/usr/bin/env python3
"""WC/2024/227 - ROSTER RECORD, 20 March 2023 to 1 September 2024. Internal working analysis from the published
rosters held (documents/rosters/2023-24_published). Read by eye from scans; verify against the page before service."""
import io, pikepdf, datetime as dt, sys, collections, openpyxl
sys.path.insert(0,'.'); from roster_data import R, UPDATED, cells, kind
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer, PageBreak
PS=landscape(A4)
B=ParagraphStyle('B',fontName='Helvetica',fontSize=8.8,leading=11.4,spaceAfter=4)
H1=ParagraphStyle('H1',fontName='Helvetica-Bold',fontSize=11,leading=14,spaceBefore=6,spaceAfter=4)
HD=ParagraphStyle('HD',fontName='Helvetica-Bold',fontSize=8.4,leading=10.5,textColor=colors.HexColor('#333333'))
T=ParagraphStyle('T',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=2)
SUB=ParagraphStyle('S',fontName='Helvetica-Oblique',fontSize=8,leading=10.5,textColor=colors.HexColor('#555555'),spaceAfter=6)
C=ParagraphStyle('C',parent=B,fontSize=7.2,leading=8.8,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
def c(t): return Paragraph(t,C)
def code(x):
    k=kind(x)
    if k in ('N','E','L'): return k+x[:2]
    return {'-':'·','x':'x','RDO':'RDO','A/L':'AL','?':'?'}[k]
s=[P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",HD),P("Matter No. WC/2024/227 | Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)",HD),
   P("ROSTER RECORD, 20 March 2023 to 1 September 2024",T),
   P("Working analysis of the published Switchboard rosters held by the Appellant (documents/rosters/2023-24_published), prepared 6 September 2026. "
     "INTERNAL. Cell entries were read by eye from scanned rosters and must be checked against the page before any use in a filing. "
     "Codes: E = early (start 06:00 or 07:00), L = late (14:00 or 15:00), N = night (22:00 or 23:00), x = marked off, · = blank, AL = annual leave, RDO. "
     "Uncovered = shifts shown in the roster's own Uncovered Shifts row.",SUB)]
s.append(P("A. Your line, fortnight by fortnight",H1))
hdr=["Fortnight","Roster","Mo","Tu","We","Th","Fr","Sa","Su","Mo","Tu","We","Th","Fr","Sa","Su","Unc.","Note"]
notes={dt.date(2023,4,3):"Easter 7-10 Apr: rostered Sun 9 (E07) and Mon 10 (N23) only",
 dt.date(2023,5,1):"Labour Day 1 May worked L15",
 dt.date(2023,9,18):"first fortnight held after the 10 Jul-17 Sep gap; 5 uncovered shifts",
 dt.date(2023,10,2):"5 uncovered shifts; full time from 16 Oct 2023",
 dt.date(2023,10,30):"issued as v2.0 (a reissue)",
 dt.date(2023,11,13):"GP 16 Nov (poor sleep) falls inside five early starts 15-19 Nov; sick 21-22 Nov",
 dt.date(2023,12,25):"Christmas night and New Year night; sick 2 Jan after E06 then N23",
 dt.date(2024,1,22):"annual leave block; 26 Jan on leave",
 dt.date(2024,2,5):"9 Feb: the 7-hour shift Payroll later corrected",
 dt.date(2024,2,19):"COVID; pandemic leave 20 Feb; declined twice, approved 29 Feb",
 dt.date(2024,3,4):"ends Sun 17 Mar L15 (finish 23:00); 6 uncovered shifts",
 dt.date(2024,3,18):"PUBLISHED ROSTER HAS NO LINE FOR SHEPHERD; the 06:00 start on 18 Mar is not on it; sick 19 Mar",
 dt.date(2024,4,1):"1 Apr L14 then 2 Apr N23; 8 Apr pay/fatigue email",
 dt.date(2024,4,15):"(a) nights 23-25 then off 26-28 then nights 29 Apr: the pattern raised 16 Apr",
 dt.date(2024,4,29):"(a) four earlies 5-8 May, RDO, then earlies; sick 7 May",
 dt.date(2024,5,13):"13-14 May sick (PID 13 May; retraction request 15 May)",
 dt.date(2024,5,27):"31 May sick; 7-9 Jun lates all taken as sick; 10 Jun LWOP; 11-12 Jun bereavement",
 dt.date(2024,6,10):"nights 10-12 Jun on bereavement/LWOP; 17 Jun onward LWOP; onset 18 Jun",
}
rows=[[Paragraph(h,CB) for h in hdr]]
for st,(lab,line,unc) in R.items():
    cl=[code(x) for x in line.split()]
    rows.append([c(f"{st.strftime('%d %b %y')} - {(st+dt.timedelta(13)).strftime('%d %b %y')}"),c(lab)]+[c(x) for x in cl]+[c(str(unc)),c(notes.get(st,''))])
    if st in UPDATED:
        lab2,line2=UPDATED[st]; cl2=[code(x) for x in line2.split()]
        rows.append([c(''),c(lab2)]+[c(x) for x in cl2]+[c(''),c("(b) nights moved to 26-28 Apr: six consecutive nights 26 Apr-2 May" if st==dt.date(2024,4,15) else "(b) earlies then lates 10-12 May; on-call rows for Ms Taylor and Ms Stibbard added")])
W=PS[0]-24*mm
t=Table(rows,colWidths=[24*mm,30*mm]+[9.2*mm]*14+[9*mm,W-24*mm-30*mm-9.2*mm*14-9*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),
  ('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]))
s.append(t)
s.append(P("Fortnights not held: 10 Jul to 17 Sep 2023; 16 to 29 Oct 2023; 27 Nov to 10 Dec 2023; 8 to 21 Jan 2024. Reissued or duplicated fortnights in the pack: 30 Oct to 12 Nov 2023 (v2.0), 15 to 28 Apr 2024 (two files, both labelled v1.0), 29 Apr to 12 May 2024 (two files, both v1.0), 19 Aug to 1 Sep 2024 (v2.0). The 18 to 31 Mar 2024 roster as published carries no line for the Appellant.",B))
s.append(PageBreak())
s.append(P("B. Sick and other leave against the rostered shift",H1))
s.append(P("From the Payroll leave takings report of 4 September 2026, matched to the published roster for the day and the two days before it. Only leave in the roster window is shown. 'n/h' = fortnight not held.",B))
L={}
for st,(lab,line,unc) in R.items():
    L.update(cells(st, UPDATED[st][1] if st in UPDATED else line))
wb=openpyxl.load_workbook('../documents/2026-09-04_Leave_Takings_Report_25MAR2019-04SEP2026_FULL.xlsx',read_only=True,data_only=True)
lv=[]
for ws in wb.worksheets:
    for r in ws.iter_rows(values_only=True):
        if r and len(r)>8 and r[1]=='00388372' and r[6]:
            d=dt.datetime.strptime(str(r[6]).split(' - ')[0].strip(),'%d/%m/%Y').date(); lv.append((d,str(r[4]),float(r[7] or 0)))
agg=collections.OrderedDict()
for d,typ,h in sorted(lv):
    if not (dt.date(2023,3,20)<=d<=dt.date(2024,6,23)): continue
    if not any(k in typ for k in ('Sick','Bereave','Pandemic','Without','Exceptional')): continue
    key=(d,typ); agg[key]=agg.get(key,0)+h
rows=[[Paragraph(h,CB) for h in ["Date","Leave","Hrs","Rostered","Day -2","Day -1","Day +1"]]]
for (d,typ),h in agg.items():
    g=lambda x: code(L[x]) if x in L else 'n/h'
    rows.append([c(d.strftime('%a %d %b %y')),c(typ),c(f"{h:.1f}"),c(g(d)),c(g(d-dt.timedelta(2))),c(g(d-dt.timedelta(1))),c(g(d+dt.timedelta(1)))])
t2=Table(rows,colWidths=[26*mm,60*mm,12*mm,20*mm,20*mm,20*mm,20*mm],repeatRows=1)
t2.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1)]))
s.append(t2)
s.append(PageBreak())
s.append(P("C. What the record shows",H1))
for t_ in [
 "<b>No published roster held shows a break under ten hours.</b> Across 25 fortnights the shortest break between consecutive rostered shifts is a late (finishing 22:00 or 23:00) followed by a night starting 22:00 or 23:00 the next day. The seven-hour break of 17 to 18 March 2024 is therefore not a roster the Appellant was published on. The 4 to 17 March roster ends on Sunday 17 March with a 15:00 to 23:00 shift. The 18 to 31 March roster as published has no line for the Appellant at all. The 06:00 start on Monday 18 March came from somewhere other than the published roster.",
 "<b>The rosters were reissued.</b> The fortnight of 30 October to 12 November 2023 was issued as v2.0. The fortnights of 15 to 28 April and 29 April to 12 May 2024 each exist in two different versions with the same v1.0 label. The April change moved the Appellant's nights from 23 to 25 April to 26 to 28 April, which with the following fortnight produced six consecutive night shifts from 26 April to 2 May. The May change replaced earlies on 10 to 12 May with lates. The updated versions also add 'After Hours Oncall' rows for Ms Taylor and Ms Stibbard, consistent with the 15 April 2024 email. Ms Reese's 10 May 2024 email acknowledging 'a few rostering errors made by Chloe with regards to Cory's line in past rosters' sits between the two reissues.",
 "<b>Consecutive shifts.</b> Runs of six or more consecutive rostered shifts occur eight times in the fortnights held (seven runs of six and one of seven), and runs of five a further eight times. From 16 October 2023 (full time) the pattern is nights, three days marked off, then earlies, then lates, in rotation.",
 "<b>Uncovered shifts.</b> 31 shifts appear in the rosters' own Uncovered Shifts row across the fortnights held: ten in the two fortnights of 18 September to 15 October 2023, six in 4 to 17 March 2024, three each in 1 to 14 May 2023 and 25 December to 7 January, and single shifts elsewhere. A roster published with an uncovered row is a roster that will be filled from the operators on it.",
 "<b>Sick leave sits at the end of runs and at the turn of the pattern.</b> 12 May 2023 on the third early; 15 June 2023 on the third late with a night to follow; 26 to 28 June 2023 on three consecutive nights; 21 to 22 November 2023 after five consecutive early starts (15 to 19 November), inside which falls the 16 November 2023 consultation recording poor sleep with shift work; 2 January 2024 on a night that followed an early; 19 March 2024 after the seven-hour break; 7 May 2024 on the third of four consecutive earlies; 13 to 14 May 2024 on lates following lates; 31 May 2024 on an early after a late; and 7 to 9 June 2024, the last three shifts before the bereavement, all lates, all taken as sick. Every rostered day from 17 June 2024 is leave without pay.",
 "<b>What the record does not show.</b> Sick leave of colleagues does not appear on published rosters; the team's leave management is visible only in the annual leave blocks, the N/A markings for casuals and the uncovered rows. The 2025 to 2026 working rosters in the same pack (22 scanned pages dated 22 March 2026) are annotated by hand with S/L, LWOP and shift changes across the team; three were read for this note and the remainder appear to be the same annotated series. They post-date the injury and are not analysed here.",
 "<b>Caveats.</b> Four fortnights in the window are not held. Cells were read from scanned images and two cells in the 19 February to 3 March 2024 fortnight were read from a skewed scan. The 18 to 31 March 2024 finding rests on the file as held; the employer's rostering system may hold a later version that includes the Appellant, and that version should be sought.",
]: s.append(P(t_))
buf=io.BytesIO(); doc=BaseDocTemplate(buf,pagesize=PS,leftMargin=12*mm,rightMargin=12*mm,topMargin=11*mm,bottomMargin=11*mm)
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(12*mm,11*mm,PS[0]-24*mm,PS[1]-22*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
doc.build(s); buf.seek(0); pdf=pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out='out/ROSTER_RECORD_20Mar2023-1Sep2024_INTERNAL.pdf'; pdf.save(out,linearize=True); print('built',out,len(pdf.pages),'pages')
