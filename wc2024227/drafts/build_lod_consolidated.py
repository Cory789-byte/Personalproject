#!/usr/bin/env python3
"""WC/2024/227 - Appellant's CONSOLIDATED List of Documents (Form 23 structure),
with a stressor map, built 22 August 2026. Supersedes the list of 5 Aug and the supplement of 17 Aug.

Two outputs:
  out/LIST_OF_DOCUMENTS_CONSOLIDATED_22AUG2026.pdf  - servable
  out/BUNDLES/  + out/WC2024227_BUNDLES.zip         - the documents, grouped to follow the list
"""
import os, shutil, pikepdf
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle)

ROOT = ".."
ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=11.5, leading=15, alignment=1, spaceAfter=2)
H2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=9.6, leading=12.6, spaceBefore=9,
                    spaceAfter=3, backColor=colors.HexColor('#e8e8e8'), borderPadding=3)
B = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=8.2, leading=10.8, spaceAfter=4)
CEN = ParagraphStyle('CEN', parent=B, alignment=1, fontSize=8.6)
C = ParagraphStyle('C', parent=B, fontSize=7.4, leading=9.6, spaceAfter=0)
CH = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
SM = ParagraphStyle('SM', parent=B, fontSize=7.2, leading=9.4, textColor=colors.HexColor('#555555'))
def P(t, s=C): return Paragraph(t, s)

# (item, date, description, author, recipient, pages, status, stressors, source_path_or_None)
D = [
 ("PART 1", "DOCUMENTS IN THE APPELLANT'S POSSESSION OR CONTROL, PRODUCED WITH THIS LIST"),
 (1,"8 Sep 2024","Work Capacity Certificate for the injury of 18 June 2024","Dr P Hawes","WorkCover Queensland","1","Produced","3(a)","documents/medical/Hawes_Work_Capacity_Certificate_signed_08.09.2024_full.jpg"),
 (2,"3 Jul 2026","Employee Capability Checklist - certifying fit for work with restrictions","Dr D H Ma, My Doctor Clinic","MSH Injury Management","5","Produced","3(a) 3(c)","documents/medical/Employee_Capability_Checklist_CShepherd_03-07-2026.pdf"),
 (3,"3 Jul 2026","Invoice 574370 - completion of the Employee Capability Checklist","My Doctor Clinic","Appellant","1","Produced","-",None),
 (4,"2020-2026","Monthly call statistics authored by the Appellant (volume only)","Appellant","-","[n]","Produced","1(a) 3(a)",None),
 (5,"Apr 2025","Individual monthly statistics, April 2025","Appellant","-","1","Produced","1(a)",None),
 (6,"FY2025-26","Payslips and fortnightly hours analysis, 7 Apr 2025 - 14 Jun 2026","Queensland Health Payroll","Appellant","[n]","Produced","2(a) 2(b)","documents/financial/Shepherd_Payslips_FY2025-26_Work_Leave_Super.xlsx"),
 (7,"2025","Return to work analysis - seven fortnights, FTE","Appellant","-","[n]","Produced","3(a)",None),
 (8,"4 Apr 2023-","Text messages between the Appellant and the Line Manager, including the roster board image of 4 April 2023","Appellant / C Taylor","-","3","Produced","1(a) 2(a)","documents/evidence/Chloe_Work_text_messages_incl_2023-04-04_roster_board.pdf"),
 (9,"2020-2026","Correspondence pack 01 - Logan Switchboard","Various","Various","103","Produced","1(a)-(g)","documents/correspondence-packs/01_CS_Logan_Switch_PACK_103pp_2020-2026.pdf"),
 (10,"2020-2026","Correspondence pack 02 - C Taylor","Various","Various","462","Produced","1(a)-(g) 2 3","documents/correspondence-packs/02_Chloe_Taylor_PACK_462pp.pdf"),
 (11,"2025-2026","Correspondence pack 03 - S Hughes","Various","Various","376","Produced","-","documents/correspondence-packs/03_Scott_Hughes_PACK_376pp_196sections.pdf"),
 (12,"31 Jul 2026","Correspondence pack 04 - Human Resources","Various","Various","21","Produced","-","documents/correspondence-packs/04_Human_Resources_PACK_21pp_2026-07-31.pdf"),
 (13,"2025","Correspondence pack 05 - J Roberts","Various","Various","64","Produced","-","documents/correspondence-packs/05_Jacqui_Roberts_PACK_64pp.pdf"),
 (14,"2024-2026","Correspondence pack 10 - WorkCover Queensland","Various","Various","84","Produced","1(a)-(g) 2 3","documents/correspondence-packs/10_Amy_Mo_WorkCover_EMAILS_PACK_84pp.pdf"),
 (15,"Undated","Role description - Administration Officer, Switchboard Services (AO3), Logan Hospital","MSH","-","4","Produced 17 Aug 2026","1(a) 3(a)","documents/instruments/ATT14_AO3_Switchboard_Role_Description.pdf"),
 (16,"11 Aug 2026","Stressor 1(a) particulars support bundle - six tabs, indexed","Appellant","Respondent","30","Served 11 Aug 2026","1(a)","documents/2026-08-11_Stressor1a_Particulars_Bundle_SERVED_on_Matheson.pdf"),
 (17,"7 Jul 2026","Letter of Ms L Forrest, Senior Consultant HR, LBH - records that the roster provides more than 10-hour breaks and that the 2020 eight-hour agreement is applied only to staff-initiated shift swaps","L Forrest, MSH","Appellant","4","Produced herewith","3(a) 3(b)","documents/2026-07-07_MSH_HR_Forrest_ECC_further_information.pdf"),
 (18,"27 Feb - 9 Jun 2026","Three movement forms recording approved changes to the Appellant's working hours, each approved by Mr S Hughes as delegate","MSH","Appellant","13","Produced herewith","3(a)","drafts/out/ATTACHMENT_5_Movement_Forms_2026.pdf"),
 (19,"19 Mar 2024","QH Leave Takings Report - records the leave of 19 March 2024 as Sick Leave, 7.60 hours, approved","MSH","-","1","Produced herewith","3(c)","documents/disclosure-2026-06_MSH_production/Item 15 QH Leave Takings Report_Cory Shepherd_19 March 2024.pdf"),
 (20,"4 Feb 2025","Logan Hospital Switchboard Sick Leave Process, version 1.1","C Taylor, MSH","-","1","Produced herewith","1(f)",None),
 ("PART 2", "DOCUMENTS ALREADY BEFORE THE COMMISSION OR PREVIOUSLY EXCHANGED"),
 (21,"18 Jun 2026","Affidavit of Cory Lea Shepherd (Form 20) with exhibit index","Appellant","Commission","-","Filed 23 Jun 2026","1(a)-(g) 2 3",None),
 (22,"9 May 2024","Exhibit CS-1 - email chain concerning the MASPER directive","Various","-","4","Annexed to the Form 20","1(a)",None),
 (23,"18-20 May 2024","Exhibit CS-2 - correspondence with Together Queensland","Appellant / Together","-","3","Annexed to the Form 20","1(g)",None),
 (24,"31 Aug 2023","Exhibit CS-3 - application to increase to full time","Appellant","MSH","2","Annexed to the Form 20","1(c) 1(g)",None),
 (25,"11 Jun 2026","Exhibit CS-4 - the Respondent's disclosure of 11 June 2026","Respondent","Appellant","2","Annexed to the Form 20","1(f)",None),
 (26,"5 Jun 2026","Letter of Metro South Hospital and Health Service responding to the Notice of Non-Party Disclosure (ref K-LM26/729), with enclosures","N Cridland, Chief Executive","Commissioner Dwyer","5 + enc","Before the Commission","1(a) 3(a) 3(b)","documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf"),
 (27,"24 Oct 2024","Review Decision 69983","Workers' Compensation Regulator","Appellant","28","Before the Commission","all","documents/Review_Decision_69983_24.10.2024.pdf"),
 (28,"18 Feb 2026","Notice to admit facts (Form 24) and the Respondent's response","Appellant / Respondent","-","10","Exchanged","all","documents/2026-02-18_Form24_Response_and_email_communication.pdf"),
 ("PART 3", "DOCUMENTS FOR WHICH PRIVILEGE OR STATUTORY PROTECTION IS CLAIMED"),
 (29,"2024-2025","Communications between the Appellant and Saines Legal for the purpose of obtaining legal advice in this proceeding","Appellant / Saines Legal","-","-","PRIVILEGE CLAIMED - legal professional privilege","-",None),
 (30,"13 May - 24 Dec 2024","Documents recording the fact or content of a public interest disclosure and the determination made in respect of it","Appellant / Ethical Standards Unit","-","-","s 65 Public Interest Disclosure Act 2010","1(e)",None),
 ("PART 4", "DOCUMENTS ONCE IN, OR NEVER IN, THE APPELLANT'S POSSESSION"),
 (31,"6 Jun 2023","Entry made by the Appellant in the Switchboard communication book","Appellant","-","1","No longer in the Appellant's possession - removal admitted (Form 24, para 6)","1(b)",None),
 (32,"17-18 Mar 2024","SPOK emergency-code and paging records for the shifts pleaded","MSH system record","-","-","Never in the Appellant's possession","3(a)",None),
 (33,"17-18 Mar 2024","Spreadsheet of recorded MET calls, which Metro South Health states is available","MSH","-","-","Never in the Appellant's possession - see item 26, Items 1-2","3(a)",None),
 ("PART 5", "DOCUMENTS NOT YET IN EXISTENCE"),
 (34,"-","Report of the Appellant's treating psychiatrist addressing diagnosis, causation and chronology, and any further medical certificate or capacity advice issued after the date of this list","Dr R B Krishnaiah","-","-","To be disclosed upon receipt","all",None),
]

s = []
s.append(P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", H1))
s.append(P("<i>Workers' Compensation and Rehabilitation Act 2003</i> &nbsp;|&nbsp; Matter No. WC/2024/227", CEN))
s.append(P("BETWEEN: <b>CORY LEA SHEPHERD</b> (Appellant) AND: <b>WORKERS' COMPENSATION REGULATOR</b> (Respondent)", CEN))
s.append(Spacer(1, 3*mm))
s.append(P("APPELLANT'S CONSOLIDATED LIST OF DOCUMENTS", H1))
s.append(P("Served on the Respondent &nbsp;|&nbsp; [DATE] 2026", CEN))
s.append(Spacer(1, 2*mm))
s.append(P("This consolidated list is given in continuation of the Appellant's disclosure obligation. "
           "It restates and supersedes the List of Documents served on 5 August 2026 and the "
           "Supplementary List served on 17 August 2026, and lists further documents that have since "
           "come into the Appellant's possession. Disclosure remains continuing. The final column "
           "identifies, for convenience of reference only, the stressor or stressors pleaded in the "
           "Amended Statement of Facts and Contentions filed 7 April 2026 to which each document is "
           "directly relevant; that column forms no part of the disclosure and is not a pleading.", B))

rows = [[P("<b>Item</b>", CH), P("<b>Date</b>", CH), P("<b>Description</b>", CH),
         P("<b>Author / From</b>", CH), P("<b>To</b>", CH), P("<b>Pp</b>", CH),
         P("<b>Status</b>", CH), P("<b>Stressor</b>", CH)]]
spans = []
for d in D:
    if d[0].__class__ is str and d[0].startswith("PART"):
        spans.append(len(rows))
        rows.append([P(f"<b>{d[0]}</b>", CH), P(f"<b>{d[1]}</b>", CH), P("",C), P("",C), P("",C), P("",C), P("",C), P("",C)])
    else:
        i, dt, desc, au, to, pp, st, ss_, _ = d
        rows.append([P(f"<b>{i}</b>",C), P(dt,C), P(desc,C), P(au,C), P(to,C), P(pp,C), P(st,C), P(f"<b>{ss_}</b>",C)])
t = Table(rows, colWidths=[10*mm,20*mm,96*mm,29*mm,22*mm,9*mm,32*mm,17*mm], repeatRows=1)
stl = [('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),
       ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
for i in spans:
    stl += [('BACKGROUND',(0,i),(-1,i),colors.HexColor('#efefef')), ('SPAN',(1,i),(7,i))]
t.setStyle(TableStyle(stl))
s.append(t)

s.append(PageBreak())
s.append(P("SCHEDULE - THE DOCUMENTS ARRANGED BY PLEADED STRESSOR", H1))
s.append(P("For convenience of reference only. Item numbers refer to the list above.", CEN))
s.append(Spacer(1, 3*mm))
STRESSORS = [
 ("1(a)","Erratic physical presence and unilateral directives without consultation","5, 8, 9, 10, 14, 15, 16, 21, 22, 26"),
 ("1(b)","The Switchboard communication book","10, 14, 21, 31"),
 ("1(c)","The matters raised on 7 August 2023 and the response to them","10, 14, 21, 24"),
 ("1(d)","The special pandemic leave applications of February 2024","10, 14, 21"),
 ("1(e)","The complaint of 13 May 2024 and its determination as a public interest disclosure (ADMITTED)","30"),
 ("1(f)","The events of 13 to 15 May 2024 and the direction to retract","10, 14, 20, 21, 25"),
 ("1(g)","The union delegate matters","21, 23, 24"),
 ("2(a)","Remuneration - the distribution of shifts and penalties","6, 8, 10, 14, 21"),
 ("2(b)","The payroll correction of 3 to 28 May 2024","6, 10, 14, 21"),
 ("3(a)","The consecutive shifts of 17 and 18 March 2024 and the seven-hour break","1, 2, 4, 7, 15, 17, 18, 21, 26, 32, 33"),
 ("3(b)","The absence of any fatigue risk assessment or framework","17, 26"),
 ("3(c)","The leave taken on 19 March 2024","2, 19, 21"),
]
srows = [[P("<b>Stressor</b>",CH), P("<b>As pleaded</b>",CH), P("<b>Items</b>",CH)]]
for a,b_,c_ in STRESSORS:
    srows.append([P(f"<b>{a}</b>",C), P(b_,C), P(c_,C)])
st2 = Table(srows, colWidths=[16*mm,150*mm,69*mm], repeatRows=1)
st2.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
s.append(st2)
s.append(Spacer(1, 6*mm))
s.append(P("Disclosure remains continuing and this list will be further supplemented as documents "
           "come into the Appellant's possession.", B))
s.append(Spacer(1, 6*mm))
s.append(P("Cory Lea Shepherd<br/>Appellant (self-represented) &nbsp;|&nbsp; [DATE] 2026", B))

OUT = "out/LIST_OF_DOCUMENTS_CONSOLIDATED_22AUG2026.pdf"
doc = SimpleDocTemplate(OUT, pagesize=landscape(A4), leftMargin=12*mm, rightMargin=12*mm,
                        topMargin=12*mm, bottomMargin=14*mm)
def f(c, d):
    c.saveState(); c.setFont('Helvetica', 7)
    c.setFillColor(colors.HexColor('#777777'))
    c.drawString(12*mm, 8*mm, "C Shepherd · WC/2024/227 · Appellant's Consolidated List of Documents")
    c.drawRightString(landscape(A4)[0]-12*mm, 8*mm, f"Page {d.page}")
    c.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
p = pikepdf.open(OUT, allow_overwriting_input=True)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save("out/_l.pdf"); p.close(); os.replace("out/_l.pdf", OUT)
print("built", OUT)

# ---------------- BUNDLES ----------------
BASE = "out/BUNDLES"
if os.path.exists(BASE): shutil.rmtree(BASE)
copied, missing = 0, []
for d in D:
    if d[0].__class__ is str: continue
    i, dt, desc, au, to, pp, st, ss_, src = d
    if not src: continue
    full = os.path.join(ROOT, src) if not src.startswith("drafts/") else src.replace("drafts/","",1)
    if not os.path.exists(full):
        missing.append(src); continue
    expand = (ss_.replace("1(a)-(g)", "1(a) 1(b) 1(c) 1(d) 1(e) 1(f) 1(g)")
                 .replace(" 2 ", " 2(a) 2(b) ").replace(" 3 ", " 3(a) 3(b) 3(c) "))
    tags = [x.strip() for x in expand.split() if x.strip() not in ("-", "")]
    if not tags:
        continue
    if "all" in tags:
        tags = ["00_ALL_STRESSORS"]
    for tag in tags:
        if tag == "2": tag = "2(a)"
        if tag == "3": tag = "3(a)"
        folder = os.path.join(BASE, tag.replace("(", "").replace(")", ""))
        os.makedirs(folder, exist_ok=True)
        dest = os.path.join(folder, f"item{i:02d}_{os.path.basename(src)}")
        if not os.path.exists(dest):
            shutil.copy2(full, dest); copied += 1
print(f"bundles: {copied} files copied; missing sources: {missing}")
shutil.make_archive("out/WC2024227_BUNDLES", "zip", BASE)
print("wrote out/WC2024227_BUNDLES.zip")
