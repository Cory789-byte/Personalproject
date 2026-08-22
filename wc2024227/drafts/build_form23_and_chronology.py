#!/usr/bin/env python3
"""WC/2024/227 - Appellant's Form 23 List of Documents (mirroring the Respondent's own format)
plus a Schedule of Events and Payments.

The Respondent's amended List of Documents of 14 August 2026 uses Form 23 with a three-column
schedule (Description of document / Person who made document / Date), grouped under category
headings, Part 1 (documents disclosed) and Part 2 (privilege claimed). This mirrors that exactly,
so the two lists can be read side by side.
"""
import os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle)

ss = getSampleStyleSheet()
ORG = colors.HexColor('#8a5a1a')
HD = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=9, leading=11.5, textColor=ORG)
TT = ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=15, leading=19, spaceAfter=2)
LEG = ParagraphStyle('LEG', fontName='Helvetica-Oblique', fontSize=8.2, leading=10.8)
B = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=8.6, leading=11.4, spaceAfter=5)
FLD = ParagraphStyle('FLD', parent=B, fontName='Helvetica-Bold', fontSize=8.6)
VAL = ParagraphStyle('VAL', parent=B, fontSize=9)
C = ParagraphStyle('C', fontName='Helvetica', fontSize=8, leading=10.6)
CH = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
CAT = ParagraphStyle('CAT', parent=C, fontName='Helvetica-Bold', textColor=colors.HexColor('#333333'))
H2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceBefore=8, spaceAfter=4)
SM = ParagraphStyle('SM', parent=B, fontSize=7.6, leading=10, textColor=colors.HexColor('#555555'))
def P(t, s=C): return Paragraph(t, s)

def box(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.7,colors.black),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('BACKGROUND',(0,0),(0,-1),colors.HexColor('#f4f4f4')),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return t

# ("CAT", heading) or (n, description, maker, date)
SCHED = [
 ("CAT","Jurisdictional Documents"),
 (1,"Application for compensation","Cory Lea Shepherd","1 July 2024"),
 (2,"Claim summary","WorkCover Queensland","Various dates"),
 (3,"WorkCover Queensland reasons for decision","Ms Amy Mo, WorkCover Queensland","25 July 2024"),
 (4,"WorkCover Queensland reasons for decision","Ms Amy Mo, WorkCover Queensland","13 September 2024"),
 (5,"Application for review","Cory Lea Shepherd","16 September 2024"),
 (6,"Review Unit reasons for decision, Review Decision 69983","Ms Victoria Squires, Review Unit, Workers' Compensation Regulator","24 October 2024"),
 ("CAT","Court Documents"),
 (7,"Notice of Appeal","Cory Lea Shepherd","26 November 2024"),
 (8,"Directions orders and further directions orders","Queensland Industrial Relations Commission","3 December 2024<br/>3 June 2025<br/>16 July 2025<br/>22 August 2025<br/>7 April 2026<br/>19 August 2026"),
 (9,"Amended Statement of Facts and Contentions, setting out the three stressors and their particulars","Cory Lea Shepherd","7 April 2026"),
 (10,"Amended Statement of Facts and Contentions of the Respondent","Workers' Compensation Regulator","13 May 2026"),
 (11,"Notice to admit facts (Form 24)","Cory Lea Shepherd","11 February 2026"),
 (12,"Response to the notice to admit facts","Workers' Compensation Regulator","18 February 2026"),
 (13,"Affidavit of Cory Lea Shepherd (Form 20), with exhibit index and exhibits CS-1 to CS-4","Cory Lea Shepherd","18 June 2026"),
 (14,"Notice of non-party disclosure (Form 29), sealed, with the application under rule 64G","Cory Lea Shepherd","22 April 2026<br/>23 June 2026"),
 (15,"Stressor 1(a) particulars support bundle, six tabs, indexed, 30 pages","Cory Lea Shepherd","11 August 2026"),
 (16,"Stressor particulars supporting bundles, thirteen indexed bundles with a master index, arranged by reference to the particulars of the three stressors pleaded in the Amended Statement of Facts and Contentions","Cory Lea Shepherd","22 August 2026"),
 ("CAT","Medical Certificates"),
 (17,"Workers' compensation medical certificate","Dr Peter Hawes","1 July 2024<br/>11 August 2024<br/>8 September 2024"),
 (18,"Workers' compensation medical certificate","Dr Ki Pang","7 August 2024"),
 (19,"Medical certificate","Our Medical Ashmore","22 October 2025"),
 (20,"Employee Capability Checklist, certifying fitness for work with restrictions","Dr Day Hong Ma","3 July 2026"),
 (21,"Invoice 574370, completion of the Employee Capability Checklist","My Doctor Clinic","3 July 2026"),
 ("CAT","Medical"),
 (22,"Email of Dr Krishnaiah noting injury and medication","Dr Ravikumar Bangalore Krishnaiah","24 October 2024"),
 (23,"Report of Mind and Memory Service","Dr Ravikumar Bangalore Krishnaiah","13 February 2025"),
 (24,"Practice records","Our Medical Ashmore","Various dates"),
 ("CAT","Factual"),
 (25,"Disclosure through witness conferencing, produced by the Respondent","Ms Tammy Reese","8 July 2025"),
 (26,"Disclosure through witness conferencing, produced by the Respondent","Ms Chloe Taylor","10 July 2025"),
 (27,"Disclosure through witness conferencing, Queensland Health Payroll, produced by the Respondent","Ms Samantha Christesen","11 July 2025"),
 (28,"Disclosure of the Respondent to the Appellant","Workers' Compensation Regulator","11 June 2026"),
 (29,"Notices of non-party disclosure issued by the Respondent to Mind and Memory Service, Our Medical Ashmore and Queensland Health","Workers' Compensation Regulator","4 July 2025"),
 (30,"Notice of non-party disclosure to Queensland Health Payroll","Ms Nicole Earl","29 April 2026"),
 ("CAT","Employer documents"),
 (31,"Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital","Metro South Hospital and Health Service","Undated"),
 (32,"Letter responding to the Notice of Non-Party Disclosure, reference K-LM26/729, with enclosures to Items 6, 11, 12, 13, 15 and 16","Ms Noelle Cridland, Chief Executive, Metro South Hospital and Health Service","5 June 2026"),
 (33,"Letter regarding the Employee Capability Checklist and further information","Ms Lyndelle Forrest, Senior Consultant, Human Resources","7 July 2026"),
 (34,"Request for medical information, letter to the employee and nine-question schedule to the general practitioner","Mr Scott Hughes, Director, Corporate Services","31 July 2026"),
 (35,"Movement forms recording approved changes to working hours, approved by Mr S Hughes as delegate","Metro South Hospital and Health Service","27 February 2026<br/>17 April 2026<br/>9 June 2026"),
 (36,"QH Leave Takings Report for 19 March 2024","Metro South Hospital and Health Service","19 March 2024"),
 (37,"Logan Hospital Switchboard Sick Leave Process, version 1.1","Ms Chloe Taylor","4 February 2025"),
 ("CAT","Payroll and remuneration"),
 (38,"Payslips, pay dates 2 July 2025 to 17 June 2026, 26 fortnights","Queensland Health Payroll","2 July 2025 to 17 June 2026"),
 (39,"Payslip recording 76.00 hours as sick leave without pay, nil gross","Queensland Health Payroll","12 August 2026"),
 (40,"Monthly call statistics authored by the Appellant, recording call volume and emergency codes activated","Cory Lea Shepherd","2020 to 2026"),
 ("CAT","Correspondence"),
 (41,"Correspondence pack, Logan Switchboard, 103 pages","Various","2020 to 2026"),
 (42,"Correspondence pack, Ms C Taylor, 462 pages","Various","2020 to 2026"),
 (43,"Correspondence pack, Mr S Hughes, 376 pages","Various","2025 to 2026"),
 (44,"Correspondence pack, Human Resources, 21 pages","Various","31 July 2026"),
 (45,"Correspondence pack, Ms J Roberts, 64 pages","Various","2025"),
 (46,"Correspondence pack, WorkCover Queensland, 84 pages","Various","2024 to 2026"),
 (47,"Text messages between the Appellant and the Line Manager, including the roster board image","Cory Lea Shepherd / Ms C Taylor","4 April 2023 onwards"),
]
PART2 = [
 (48,"Communications between the Appellant and Saines Legal for the purpose of obtaining legal advice in this proceeding","Cory Lea Shepherd / Saines Legal","2024 to 2025","Legal professional privilege"),
 (49,"Documents recording the fact or content of a public interest disclosure and the determination made in respect of it","Cory Lea Shepherd / Ethical Standards Unit","13 May 2024 to 24 December 2024","Section 65, Public Interest Disclosure Act 2010"),
]

s = []
s.append(P("QUEENSLAND<br/>INDUSTRIAL RELATIONS<br/>COMMISSION", HD))
s.append(Spacer(1, 2*mm))
s.append(box([[P("Matter No:", FLD), P("<b>WC/2024/227</b>", VAL)]], [26*mm, 40*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Form 23 &ndash; List of documents", TT))
s.append(P("<i>Industrial Relations Act 2016</i>, section 989<br/>"
           "<i>Industrial Relations (Tribunals) Rules 2011</i>, rules 41(2)(o) and 113(2)(n)", LEG))
s.append(Spacer(1, 5*mm))
s.append(box([[P("Applicant/Appellant:", FLD), P("Cory Lea Shepherd", VAL)]], [40*mm, 126*mm]))
s.append(P("V", ParagraphStyle('V', parent=B, alignment=1, fontName='Helvetica-Bold')))
s.append(box([[P("Respondent:", FLD), P("Workers' Compensation Regulator", VAL)]], [40*mm, 126*mm]))
s.append(Spacer(1, 3*mm))
s.append(P("<b>PLEASE NOTE:</b> If there are more than two parties to this application, please "
           "complete a <b>Form 1 &ndash; Parties list</b> and file it with this form.", B))
s.append(P("The following is a list of the documents directly relevant to the allegations or "
           "matters in question in this proceeding which are in the possession or control of the "
           "<b>[X] applicant</b> &nbsp;[&nbsp;&nbsp;] respondent and is served in compliance with "
           "the directions order dated 3 December 2024 and the Further Directions Order (3) dated "
           "19 August 2026.", B))
s.append(P("The documents are listed in the attached schedule:", B))
s.append(box([[P("1. You may inspect the documents in the schedule as follows:", FLD), P("", VAL)],
              [P("Address:", FLD), P("By arrangement", VAL)],
              [P("Times:", FLD), P("Please contact me to make an appropriate time.", VAL)]],
             [55*mm, 111*mm]))
s.append(Spacer(1, 3*mm))
s.append(P("2. The <b>[X] applicant</b> &nbsp;[&nbsp;&nbsp;] respondent objects to produce the "
           "documents listed in part 2 of the schedule on the ground of privilege.", B))

s.append(PageBreak())
s.append(P("Schedule", TT))
s.append(P("Part 1", H2))
rows = [[P("Description of document", CH), P("Person who made document", CH), P("Date (if any)", CH)]]
cats = []
for r in SCHED:
    if r[0] == "CAT":
        cats.append(len(rows)); rows.append([P(f"<b>{r[1]}</b>", CAT), P("", C), P("", C)])
    else:
        n, d, mk, dt = r
        rows.append([P(f"<b>{n}.</b>&nbsp; {d}", C), P(mk, C), P(dt, C)])
t = Table(rows, colWidths=[104*mm, 44*mm, 30*mm], repeatRows=1)
stl = [('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#888888')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4e4e4')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]
for i in cats:
    stl += [('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f2f2f2')), ('SPAN',(0,i),(2,i))]
t.setStyle(TableStyle(stl))
s.append(t)

s.append(Spacer(1, 5*mm))
s.append(P("<b>Note as to the stressor bundles at item 16</b>", C))
s.append(Spacer(1, 2*mm))
s.append(P("For convenience of inspection and reference, documents disclosed in Part 1 are also "
           "arranged in indexed supporting bundles by reference to the particulars of the "
           "<b>three stressors</b> pleaded in the Appellant's Amended Statement of Facts and "
           "Contentions dated 7 April 2026. Stressor 1 is pleaded with particulars (a) to (g); "
           "Stressor 2 with particulars (a) and (b); and Stressor 3 with particulars (a) to (d). "
           "The lettered labels identify the particulars of, and the evidentiary material relating "
           "to, each pleaded stressor. They do not create separate stressors.", C))
s.append(Spacer(1, 2*mm))
s.append(P("A document may appear in more than one bundle where it is relevant to more than one "
           "particular. The bundles are aids to inspection and reference only. They do not amend, "
           "replace or add to the Amended Statement of Facts and Contentions, and this Schedule "
           "remains the Appellant's disclosure.", C))

s.append(Spacer(1, 6*mm))
s.append(P("Part 2 &ndash; documents for which privilege or statutory protection is claimed", H2))
p2 = [[P("Description of document", CH), P("Person who made document", CH), P("Date (if any)", CH), P("Ground", CH)]]
for n, d, mk, dt, g in PART2:
    p2.append([P(f"<b>{n}.</b>&nbsp; {d}", C), P(mk, C), P(dt, C), P(g, C)])
t2 = Table(p2, colWidths=[74*mm, 38*mm, 30*mm, 36*mm], repeatRows=1)
t2.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#888888')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4e4e4')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
s.append(t2)
s.append(Spacer(1, 5*mm))
s.append(P("Disclosure is continuing. This list will be supplemented as documents come into the "
           "Appellant's possession, including the report of the Appellant's treating psychiatrist "
           "addressing diagnosis, causation and chronology, which will be disclosed upon receipt.", B))
s.append(Spacer(1, 8*mm))
s.append(box([[P("Signature:", FLD), P("<br/><br/>", VAL)],
              [P("Print name:", FLD), P("Cory Lea Shepherd", VAL)],
              [P("Description of signatory:", FLD), P("Appellant (self-represented)", VAL)],
              [P("Date:", FLD), P("_____ / _____ / __________", VAL)]], [45*mm, 121*mm]))

OUT = "out/FORM23_LIST_OF_DOCUMENTS_Appellant.pdf"
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=17*mm, rightMargin=17*mm,
                        topMargin=15*mm, bottomMargin=18*mm)
def f(c, d):
    c.saveState(); c.setFont('Helvetica', 7.4); c.setFillColor(colors.black)
    c.drawRightString(A4[0]-17*mm, 10*mm, str(d.page))
    c.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
p = pikepdf.open(OUT, allow_overwriting_input=True)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save("out/_f.pdf"); p.close(); os.replace("out/_f.pdf", OUT)
print("built", OUT)

# ============================================================ SCHEDULE OF EVENTS AND PAYMENTS
import openpyxl
wb = openpyxl.load_workbook("../documents/financial/Shepherd_Payslips_FY2025-26_Work_Leave_Super.xlsx", data_only=True)
ws = wb["Fortnight detail"]
pay = [r for r in ws.iter_rows(min_row=2, values_only=True) if r[0] and "/" in str(r[0])]

e = []
e.append(P("SCHEDULE OF EVENTS AND PAYMENTS", TT))
e.append(P("WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd v Workers' Compensation Regulator", B))
e.append(P("Each entry is taken from a document listed in the Appellant's List of Documents or "
           "from a document of the Respondent or the employer. Dates only; no characterisation is "
           "intended and none should be inferred.", SM))

EV = [
 ("CAT","The employment"),
 ("2019","Employment with Metro South Hospital and Health Service commences"),
 ("17 June 2020","Agreement signed permitting an eight-hour break between shifts"),
 ("27 September 2023","Application for permanent full-time hours approved by the Line Manager"),
 ("16 October 2023","Full-time hours commence"),
 ("CAT","The matters pleaded"),
 ("6 June 2023","Pages removed from the Switchboard communication book (admitted, SOFC \u00b612(a))"),
 ("18 July 2023","Email of Ms E Stibbard recording the introduction of the Switchboard Telecommunications Coordinator role, that she would be \u201cremoving everyone's access to the database\u201d, and that any entry to be \u201camended, added or removed\u201d was to be sent to her directly. Updating of contact numbers in the Switchboard directory and the associated database restricted to that role"),
 ("7 August 2023","Email to the Line Manager and the Director raising rostering and workplace matters; rostering error acknowledged the same day as \u201can oversight\u201d"),
 ("29 August 2023","HR Policy E12, Individual Employee Grievances, provided to the Appellant"),
 ("20 to 27 February 2024","Special pandemic leave applications; a review later found the attachments \u201cwere in fact present\u201d"),
 ("17 to 18 March 2024","Consecutive shifts rostered to finish 23:00 and commence 06:00, a break of seven hours"),
 ("19 March 2024","Leave taken, recorded as Sick Leave, 7.60 hours, approved"),
 ("15 April 2024","After-hours on-call arrangements changed, \u201ceffective from today\u201d"),
 ("19 April 2024","Change to Switchboard tasks"),
 ("26 April 2024","Email of the Director to the Appellant, \u201cRoster Concerns\u201d"),
 ("1 May 2024","Email to the Director concerning rostering and the fatigue toolkit"),
 ("3 May 2024","Email of Ms E Grant, Client Service Officer, Queensland Health Payroll, to the Line Manager, identifying the errors and directing that an AVAC be submitted to correct the shifts"),
 ("8 May 2024","Email of the Director to the Appellant, \u201cRE: Roster Concerns\u201d"),
 ("9 May 2024","MASPER register: email of the Line Manager directing a change to the Switchboard's call-handling process, recording that a doctor's hours were \u201cnot provided on the rosters\u201d and that the contact number was \u201cswitched off\u201d"),
 ("10 May 2024","Email of the Appellant to Queensland Health Payroll raising the outstanding pay issues"),
 ("10 May 2024","Director's email to Human Resources recording a roster risk matrix rating of 11"),
 ("13 May 2024","Email of Queensland Health Payroll to the Appellant confirming they could not see any issues had been corrected, and directing that the matter be raised with the Line Manager for the submission of an AVAC"),
 ("13 May 2024","Complaint made concerning conduct in the workplace"),
 ("13 to 15 May 2024","Unavailable for three consecutive rostered shifts; notified by telephone to the Switchboard"),
 ("15 May 2024","Delay of approximately two hours in the handover of critical pathology results to the MASPER registrar, six days after the direction of 9 May 2024"),
 ("15 May 2024","Email of the Appellant requesting the Line Manager's office hours and consultation with the team before changes and directives"),
 ("15 May 2024, 11:47 am","Email of Ms S Marriott to Logan Switch, \u201cRespiratory Nurse Educators\u201d"),
 ("15 May 2024","Direction to retract the email concerning office hours"),
 ("17 May 2024, 9:30 am","Email of the Line Manager to Logan Switch and Switchboard staff, \u201cSwitchboard Manager - On call and Hours.\u201d"),
 ("20 May 2024, 11:03 am","Email of Ms S Marriott to Logan Switch, \u201cFW: Respiratory Nurse Educators\u201d"),
 ("20 May 2024, 2:05 pm","Email of the Appellant (Logan Switch) to the Line Manager, \u201cFW: Respiratory Nurse Educators\u201d, providing the Appellant's recommendations"),
 ("20 May 2024, 4:07 pm","Director's follow-up email to Human Resources"),
 ("20 May 2024, 4:30 pm","Reply of the Line Manager to the Appellant, \u201cRE: Respiratory Nurse Educators\u201d"),
 ("21 May 2024, 12:33 pm","Email of the Line Manager to the Appellant: \u201cI am waiting payroll confirmation\u2026 as soon as I do get that confirmation, I will submit an AVAC\u201d"),
 ("21 May 2024","Request of the Director that the Appellant identify the directives about which he had consultation concerns"),
 ("28 May 2024","AVAC submitted, 25 days after the payroll instruction of 3 May 2024"),
 ("Third quarter 2024","Line Manager issued with a Queensland Health mobile device. Until then no such device had been issued, and the SMS request in issue was made from the Line Manager's personal mobile (letter of the Chief Executive, ref K-LM26/729)"),
 ("CAT","The injury and the claim"),
 ("18 June 2024","Date of injury"),
 ("1 July 2024","First presentation; workers' compensation medical certificate, Dr P Hawes"),
 ("7 August 2024","Workers' compensation medical certificate, Dr K Pang"),
 ("25 July 2024","WorkCover Queensland reasons for decision"),
 ("13 September 2024","WorkCover Queensland reasons for decision"),
 ("16 September 2024","Application for review"),
 ("September 2024","Referral to a psychiatrist by Dr P Hawes"),
 ("24 October 2024","Email of Dr R B Krishnaiah, psychiatrist, noting injury and medication"),
 ("24 October 2024","Review Unit reasons for decision, Review Decision 69983"),
 ("26 November 2024","Notice of Appeal filed"),
 ("13 February 2025","Report of Mind and Memory Service, Dr R B Krishnaiah"),
 ("24 December 2024","Ethical Standards Unit determination (admitted, SOFC ¶15)"),
 ("CAT","The proceeding"),
 ("13 March 2026","Section 552A conference"),
 ("7 April 2026","Further Directions Order; Amended Statement of Facts and Contentions"),
 ("13 May 2026","Respondent's Amended Statement of Facts and Contentions"),
 ("5 June 2026","Letter of the Chief Executive, Metro South Health, ref K-LM26/729"),
 ("23 June 2026","Application under rule 64G filed"),
 ("7 August 2026","Mention before Industrial Commissioner Dwyer"),
 ("10 August 2026","Application under rule 64G withdrawn"),
 ("14 August 2026","Respondent's Amended List of Documents"),
 ("19 August 2026","Further Directions Order (3)"),
 ("9 September 2026","Appellant's witness list, outlines and expert reports due, 4.00 pm"),
 ("30 September 2026","Respondent's witness list, outlines and expert reports due, 4.00 pm"),
 ("CAT","Capacity and the cessation of payment"),
 ("27 February 2026","Movement form approved, 56 hours per fortnight, effective 1 to 15 March 2026"),
 ("17 April 2026","Movement form approved, 56 hours per fortnight, effective 16 March to 26 April 2026"),
 ("9 June 2026","Movement form approved, 40 hours per fortnight, effective 25 May to 28 June 2026"),
 ("13 June 2026","Last day worked"),
 ("26 June 2026","Advised that the position had changed and that attendance required medical clearance"),
 ("3 July 2026","Employee Capability Checklist provided, certifying fitness with restrictions; advised the same day that attendance was not permitted"),
 ("13 July 2026","Wages cease"),
 ("31 July 2026","Request for medical information, signed by the Director, Corporate Services"),
 ("12 August 2026","Payslip records 76.00 hours as sick leave without pay; nil gross"),
]
erows = [[P("Date or period", CH), P("Event", CH)]]
ecats = []
for r in EV:
    if r[0] == "CAT":
        ecats.append(len(erows)); erows.append([P(f"<b>{r[1]}</b>", CAT), P("", C)])
    else:
        erows.append([P(f"<b>{r[0]}</b>", C), P(r[1], C)])
et = Table(erows, colWidths=[42*mm, 136*mm], repeatRows=1)
estl = [('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#888888')),
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4e4e4')),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
        ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]
for i in ecats:
    estl += [('BACKGROUND',(0,i),(-1,i),colors.HexColor('#f2f2f2')), ('SPAN',(0,i),(1,i))]
et.setStyle(TableStyle(estl))
e.append(et)

e.append(PageBreak())
e.append(P("PAYMENTS &ndash; FORTNIGHTLY GROSS, PAY DATES 2 JULY 2025 TO 17 JUNE 2026", TT))
e.append(P("Taken from the payslips listed at item 20. Gross as shown on each payslip.", SM))
prows = [[P("Pay date", CH), P("Period", CH), P("Gross", CH)]]
tot = 0.0
for r in pay:
    g = float(r[25] or 0); tot += g
    prows.append([P(str(r[0]), C), P(f"{r[1]} to {r[2]}", C), P(f"${g:,.2f}", C)])
prows.append([P("<b>Total, 26 fortnights</b>", CH), P("", C), P(f"<b>${tot:,.2f}</b>", CH)])
prows.append([P("<b>12 August 2026</b>", CH), P("<b>20 July to 2 August 2026</b>", CH), P("<b>$0.00</b>", CH)])
pt = Table(prows, colWidths=[34*mm, 100*mm, 44*mm], repeatRows=1)
pt.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#888888')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4e4e4')),
    ('BACKGROUND',(0,-1),(-1,-1),colors.HexColor('#fdf1ef')),
    ('BACKGROUND',(0,-2),(-1,-2),colors.HexColor('#f2f2f2')),
    ('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(2,1),(2,-1),'RIGHT'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
e.append(pt)
e.append(Spacer(1, 4*mm))
e.append(P("No wages have been paid since 13 July 2026.", B))

OUT2 = "out/SCHEDULE_OF_EVENTS_AND_PAYMENTS.pdf"
doc2 = SimpleDocTemplate(OUT2, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                         topMargin=15*mm, bottomMargin=16*mm)
doc2.build(e, onFirstPage=f, onLaterPages=f)
p = pikepdf.open(OUT2, allow_overwriting_input=True)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save("out/_e.pdf"); p.close(); os.replace("out/_e.pdf", OUT2)
print("built", OUT2, f"({len(pay)} pay records, total ${tot:,.2f})")
