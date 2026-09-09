#!/usr/bin/env python3
"""WC/2024/227 — the Appellant's List of Documents, organised by the matters in issue.

The list served 5 August 2026 was organised by disclosure STATUS (in possession / before the
Commission / privileged / not in possession). This one is organised by the MATTER IN ISSUE as
pleaded in the Amended Statement of Facts and Contentions filed 7 April 2026, with the status
carried in its own column. Same documents, plus everything served since; a different spine.

⛔ TWO DRAFTING RULES, both deliberate:

1. **The section headings cite the SOFC paragraph; they do not repeat its characterisations.**
   A list of documents identifies documents against issues. It is not a place to re-plead, and
   importing words like "hostile", "reprisal" or "capricious" into a disclosure list would put
   them in a document that does not need them and cannot carry them.
2. **Every description is neutral and physical** — what the document is, who made it, when.
   No document is described by what it proves.

Output: out/LIST_OF_DOCUMENTS_BY_SOFC_WC2024227.pdf
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)
import pikepdf

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
OUT = "out/LIST_OF_DOCUMENTS_BY_SOFC_WC2024227.pdf"
DATE = "9 September 2026"

HD  = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11,
                     textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=10)
TT  = ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=12.5, leading=16, spaceAfter=4)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=8.2, leading=10.8, spaceAfter=4)
PART= ParagraphStyle('PART', fontName='Helvetica-Bold', fontSize=9.6, leading=12.5,
                     spaceBefore=8, spaceAfter=3)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=8.4, leading=10.8,
                     spaceBefore=6, spaceAfter=2, textColor=colors.HexColor('#111111'))
SECN= ParagraphStyle('SECN', fontName='Helvetica-Oblique', fontSize=7.4, leading=9.4,
                     spaceAfter=2, textColor=colors.HexColor('#444444'))
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=7.3, leading=9.1, spaceAfter=0)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')

# ── the inventory ───────────────────────────────────────────────────────────────
# (section heading, SOFC pinpoint, note) then rows: (date, document, source, status)
SECTIONS = [
 ("1.  The role, the employment and the baseline", "SOFC Part B, ¶¶1.1–1.4", None, [
  ("undated", "Role description, Administration Officer (AO3), Switchboard Services, Logan Hospital",
   "Metro South Health", "Annexure A Tab 1. Authenticity not admitted 8 Sep 2026"),
  ("27 Sep 2023", "Email, Ms C Taylor to the Appellant, 1:52 pm, \"Approved - Permanent Full Time FTE\"",
   "Ms C Taylor", "Annexure A Tab 5. Authenticity not admitted 8 Sep 2026"),
  ("27 Feb, 17 Apr and 9 Jun 2026", "Movement forms recording approved changes to working hours, approved by Mr S Hughes as delegate",
   "Metro South Health", "Annexure A Tabs 17–19. Authenticity not admitted 8 Sep 2026"),
  ("2020–2026", "Monthly call statistics authored by the Appellant (volume only — calls handled and emergency codes activated)",
   "Appellant", "Produced 5 Aug 2026 (item 4)"),
  ("Apr 2025", "Individual monthly statistics, April 2025", "Appellant", "Produced 5 Aug 2026 (item 5)"),
 ]),

 ("2.  Stressor 1(a) — the directives, the manager's attendance, and the Switchboard workflow",
  "SOFC Part B, ¶2, Stressor 1(a)", None, [
  ("23 Aug 2023", "Email, Ms C Taylor to Logan Switch and Switchboard staff, 2:18 pm, \"What's Chloe's Hours?!\"",
   "Ms C Taylor", "Annexure A Tab 30. Authenticity not admitted 8 Sep 2026"),
  ("18 Jul 2023", "Email, Ms E Stibbard to the Appellant and the Switchboard team, 12:56 pm, \"Hello &amp; Update\"",
   "Ms E Stibbard", "Annexure A Tab 1A. Served 11 Aug 2026; authenticity admitted"),
  ("15 Apr 2024", "Email, Ms C Taylor to Logan Switch and Switchboard staff, 12:39 pm, \"Afterhours Oncall Process - Switchboard\"",
   "Ms C Taylor", "Annexure A Tab 6. Authenticity not admitted 8 Sep 2026. Named at item 25 of the Respondent's amended List of Documents"),
  ("9 May 2024 (logs 2–8 May)", "MASPER register emails — Ms Taylor to the MASPER Registrar and Dr Wong; \"MASPER process\" to Switchboard staff; and the underlying switchboard issue logs",
   "Ms C Taylor / MASPER Registrar", "Annexure A Tab 8B. Served 11 Aug 2026; authenticity admitted"),
  ("9 May 2024", "Exhibit CS-1 — email chain concerning the MASPER directive, including the Line Manager's email of 9 May 2024",
   "Various", "Annexed to the Form 20 affidavit, filed 23 Jun 2026 (4pp)"),
  ("13 May 2024", "Email, Ms E Stibbard to the Switchboard team, 4:29 pm, \"Switchboard After Hours On Call Manager PP24 13/5/24 - 26/5/24\"",
   "Ms E Stibbard", "Annexure A Tab 8C. Authenticity admitted"),
  ("17 May 2024", "Email, Ms C Taylor to Logan Switch and Switchboard staff, 9:30 am, \"Switchboard Manager - On call and Hours.\"",
   "Ms C Taylor", "Annexure A Tab 9. Authenticity admitted"),
  ("15 and 20 May 2024", "Emails, Ms S Marriott to Logan Switch \"Respiratory Nurse Educators\"; the Appellant to Ms Taylor; and Ms Taylor's reply",
   "Ms S Marriott / Ms C Taylor", "Annexure A Tab 11. Authenticity admitted"),
  ("18 Jun 2024", "Email, Ms C Taylor to Logan Switch copied to Ms T Reese and Ms E Stibbard, 8:58 am, \"Good morning Team.\"",
   "Ms C Taylor", "Annexure A Tab 30A. Authenticity not admitted 8 Sep 2026"),
 ]),

 ("3.  Stressor 1(b) — the Communication Book entry of 6 June 2023",
  "SOFC Part B, ¶2, Stressor 1(b)", None, [
  ("6 Jun 2023", "Email, Ms C Taylor to Ms T Reese, 4:05 pm, \"Fwd: Communication Book Update\", with Ms Taylor's email to Logan Switch of 6 June 2023 at 9:57 am beneath it",
   "Ms C Taylor", "Annexure A Tab 1B. Produced by the Respondent (disclosure, Jul 2025); authenticity admitted"),
  ("6 Jun 2023", "Entry made by the Appellant in the Switchboard Communication Book concerning the verification and updating of doctors' on-call contact details",
   "Appellant", "⛔ Not in the Appellant's possession. Its removal is admitted. Sought at Item 18 of the Form 29 notice"),
 ]),

 ("4.  Stressor 1(c) — the matters raised in August and September 2023 and the response",
  "SOFC Part B, ¶2, Stressor 1(c)", None, [
  ("7–10 Aug 2023", "Email chain, the Appellant to Ms C Taylor, Ms T Reese, Ms P Conaghan and Ms T Smith, \"Increase of hours and Workplace issues\", and Ms Reese's replies in the same chain",
   "Appellant / Ms T Reese", "Annexure A Tab 2. Produced by the Respondent (Jul 2025); authenticity admitted"),
  ("7 and 31 Aug 2023", "Document, the Appellant to Ms C Taylor, \"Request to Increase Working Hours to Full Time Rotational Roster\"; Ms Taylor's reply of 7 Aug 1:43 pm; Ms Reese to Ms Taylor 7 Aug 5:11 pm",
   "Appellant / Ms C Taylor / Ms T Reese", "Annexure A Tab 4. Authenticity admitted"),
  ("29 Aug – 8 Sep 2023", "Email, Ms T Reese to the Appellant attaching HR Policy E12; and the emails of 4 and 8 September 2023",
   "Ms T Reese", "Annexure A Tab 3. Authenticity admitted"),
 ]),

 ("5.  Stressor 1(d) — pandemic leave, 20 February to 1 March 2024",
  "SOFC Part B, ¶2, Stressor 1(d)", None, [
  ("20 Feb – 1 Mar 2024", "myHR leave request history for Process Reference 15480560",
   "Metro South Health", "Annexure A Tab 28. Produced by MSH under the Form 29 notice (Jun 2026), Item 11; authenticity admitted"),
  ("effective 5 Dec 2022", "Instrument of Human Resource Sub-Delegation, COVID-19 Pandemic Event — Paid Special Pandemic Leave, signed Ms N Cridland",
   "Metro South Health", "Annexure A Tab 29. Produced by MSH under the Form 29 notice, Item 13; authenticity admitted"),
  ("1 Feb – 31 May 2024", "myHR submissions report for the Appellant",
   "Metro South Health", "Annexure A Tab 15. Produced by MSH under the Form 29 notice, Item 11; authenticity admitted"),
 ]),

 ("6.  Stressor 1(e) and 1(f) — the disclosure of 13 May 2024 and the direction of 15 May 2024",
  "SOFC Part B, ¶2, Stressor 1(e)–(f)", None, [
  ("15 May 2024", "Email chain, \"Office Hours and Departmental Directives\" — the Appellant to Ms C Taylor and Logan Switch copied to Switchboard staff, Ms T Reese and LBH_HR at 1:15 pm; Ms Reese's reply at 6:23 pm; the Appellant's reply at 7:09 pm",
   "Appellant / Ms T Reese", "Annexure A Tab 9A. Produced by the Respondent (Jul 2025); authenticity admitted"),
  ("21 May 2024", "Email, Ms T Reese to the Appellant, 2:53 pm, \"RE: Office Hours and Departmental Directives\"",
   "Ms T Reese", "Annexure A Tab 9B. Authenticity admitted"),
  ("11 Jun 2026", "Exhibit CS-4 — the Respondent's disclosure of 11 June 2026 (correspondence of 15–16 May 2024)",
   "Respondent", "Annexed to the Form 20 affidavit (2pp)"),
  ("13 May – 24 Dec 2024", "Documents recording the fact or content of a public interest disclosure and the determination made in respect of it",
   "Appellant / Ethical Standards Unit", "⛔ Statutory protection claimed — s 65 Public Interest Disclosure Act 2010. Non-publication sought at order 6 of the draft order"),
 ]),

 ("7.  Stressor 1(g) — industrial representation",
  "SOFC Part B, ¶2, Stressor 1(g)", None, [
  ("31 Aug 2023", "Exhibit CS-3 — the Appellant's application to increase to full time, recording the intention to become the Switchboard union delegate",
   "Appellant", "Annexed to the Form 20 affidavit (2pp)"),
  ("18–20 May 2024", "Exhibit CS-2 — correspondence with Together Queensland (Ms H Hayes) and the union's confirmation of 20 May 2024",
   "Appellant / Together Queensland", "Annexed to the Form 20 affidavit (3pp)"),
  ("3 Nov 2025", "Email, Mr H Moran, Organiser, Together Queensland, to Ms C Jeffrey, Ms P Conaghan and the Appellant, \"Switchboard Roster Feedback - For Delegates\"",
   "Together Queensland", "Annexure A Tab 24. Authenticity not admitted 8 Sep 2026"),
 ]),

 ("8.  Stressor 2 — remuneration, February to May 2024",
  "SOFC Part B, ¶2, Stressor 2(a)–(b)", None, [
  ("3–13 May 2024", "Email thread, \"Corey Shepherd 388372 Pay issues\" — Payroll to the Line Manager copied to the Appellant; the Appellant to Payroll; Payroll to the Appellant",
   "QH Payroll / Appellant", "Annexure A Tab 12. Produced by the Respondent (Jul 2025); authenticity admitted"),
  ("21 May 2024", "The same thread continued — the Line Manager to the Appellant, 12:33 pm",
   "Ms C Taylor", "Annexure A Tab 13. Authenticity admitted"),
  ("28 May 2024", "Email, Ms C Taylor to the Appellant copied to Ms T Reese, 8:36 am, \"Validation of Claims older than 3 months - Please sign\"",
   "Ms C Taylor", "Annexure A Tab 14. Authenticity admitted"),
  ("FY2025–26", "Payslips and fortnightly hours analysis, 7 April 2025 to 14 June 2026",
   "QH Payroll", "Produced 5 Aug 2026 (item 6)"),
  ("2025", "Return to work analysis — seven fortnights, FTE", "Appellant", "Produced 5 Aug 2026 (item 7)"),
 ]),

 ("9.  Stressor 3 — the shifts of 17 and 18 March 2024, and fatigue management",
  "SOFC Part B, ¶2, Stressor 3(a)–(d)",
  "⛔ The native workbook at the first item is on Metro South Health's systems. The Appellant has been "
  "excluded from the workplace since 3 July 2026 and cannot retrieve it. It is sought from the "
  "Respondent by the request of 9 September 2026 and, failing that, by notice of non-party disclosure.", [
  ("March 2024", "Screen capture of the workbook \"2024 Emergency Code Register.xlsx\" (MARCH 2024 sheet), showing the entries recorded for 16 to 20 March 2024. The register was authored and maintained by the Appellant at the Switchboard console",
   "Appellant", "⭐ Annexure A Tab 31. Authenticity not admitted 8 Sep 2026. <b>Added to this list by way of ongoing disclosure.</b> The native workbook is not in the Appellant's possession"),
  ("26 Apr – 8 May 2024", "Email chain, \"Roster Concerns\" — Ms T Reese to the Appellant 26 Apr 1:52 pm; the Appellant to Ms Reese 1 May 1:18 pm; Ms Reese to the Appellant 8 May 9:08 am",
   "Ms T Reese / Appellant", "Annexure A Tab 7. Produced by the Respondent (Jul 2025); authenticity admitted"),
  ("10 and 20 May 2024", "Emails, Ms T Reese to Mr M Pritchard \"FW: Roster Concerns\", and Ms T Reese to LBH_HR attaching \"qh-gdl-401-3.3\"",
   "Ms T Reese", "Annexure A Tab 8. Authenticity admitted"),
  ("2021", "Cover page of that attachment — Fatigue risk management systems, Implementation guideline QH-GDL-401-3.3:2021",
   "Queensland Health", "Annexure A Tab 8A. Authenticity admitted"),
  ("19 Mar 2024", "QH Leave Takings Report for the Appellant",
   "Metro South Health", "Annexure A Tab 16. Produced by MSH under the Form 29 notice, Item 15; authenticity admitted"),
  ("14 and 15 May 2024", "Email, Ms C Taylor to the Appellant, \"Sick leave 14.05.24\"; and Ms Taylor's forward to Ms T Reese of 15 May 2024 at 1:07 pm",
   "Ms C Taylor", "Annexure A Tab 10. Authenticity admitted"),
  ("7 Jul 2026", "Email, Ms L Forrest, Senior Consultant Human Resources, to the Appellant",
   "Ms L Forrest", "Annexure A Tab 21. Authenticity not admitted 8 Sep 2026"),
  ("17–18 Mar 2024", "SPOK emergency-code and paging records for the shifts pleaded",
   "Metro South Health system record", "⛔ Never in the Appellant's possession. Sought at Items 1–2 of the Form 29 notice. Metro South Health states the records were not retained but that a spreadsheet of recorded MET calls exists for 17–18 March 2024"),
  ("4 Apr 2023 onwards", "Text messages between the Appellant and the Line Manager, including the roster board image of 4 April 2023",
   "Appellant / Ms C Taylor", "Produced 5 Aug 2026 (item 8)"),
 ]),

 ("10.  Conduct after 18 June 2024",
  "SOFC Part B, ¶3(a)–(c)", None, [
  ("Nov 2024", "Consultation Paper — Proposed Rosters for Switchboard Services, Logan Hospital",
   "Metro South Health", "Annexure A Tab 22. Authenticity not admitted 8 Sep 2026"),
  ("Dec 2024", "Consultation outcome — Proposed Rosters for Switchboard Services, Logan Hospital",
   "Metro South Health", "Annexure A Tab 23. Authenticity not admitted 8 Sep 2026"),
  ("26 Sep 2024", "Letter, Metro South Health to the Appellant, ref K-CF24/3196 — show cause, abandonment of employment under clause 9.6 of the Award, signed Ms A Coccetti, Executive Director, Logan and Beaudesert Health Service",
   "Ms A Coccetti, MSH", "In the Appellant's possession. Produced with this list"),
  ("9 Oct 2024", "Letter, Metro South Health to the Appellant, ref K-CF24/3270 — confirmation of abandonment of employment, made under section 31.2 of the MSH Human Resources Sub-Delegations Manual, nominating the separation date as 20 September 2024; enquiries Ms F Firoz, Consultant, Human Resources",
   "Metro South Health", "⭐ In the Appellant's possession. Produced with this list. The termination and the subsequent reinstatement are pleaded at SOFC ¶3(b)"),
  ("9 Oct 2024", "The Appellant's draft reply to the letter of 9 October 2024",
   "Appellant", "In the Appellant's possession. Produced with this list"),
  ("11 Oct 2024", "The Appellant's reply to the letter of 9 October 2024, as sent",
   "Appellant", "In the Appellant's possession. Produced with this list"),
  ("stamped 25 Oct 2024", "Form 12 application for reinstatement, TD/2024/110, Shepherd v State of Queensland (Queensland Health)",
   "Appellant", "Filed in TD/2024/110, a separate proceeding. Listed because the reinstatement is pleaded at SOFC ¶3(b). No relief in that proceeding is relied upon here"),
  ("Oct 2024 – Jul 2026", "Return to work and income protection correspondence bundle, CLM-317073 / MSH-INJ-5795, assembled 14 July 2026 (30pp)",
   "Various / QSuper", "In the Appellant's possession. Produced with this list"),
  ("3 Aug 2026", "Proposal for Return to Work, MSH-INJ-5795, accompanying the response to the Request for Medical Information (3pp)",
   "Appellant", "Served on Metro South Health 3 August 2026"),
  ("5 Aug 2026", "QSuper advice of graduated return to work payment, CLM-317073, covering 25 to 31 May 2026",
   "QSuper / ART", "In the Appellant's possession. Produced with this list"),
  ("3 Jul 2026", "Employee Capability Checklist completed by Dr Day Hong Ma — capacity and restrictions",
   "Dr D H Ma, My Doctor Clinic", "Produced 5 Aug 2026 (item 2). Also Tab M7 of the medical schedule served 9 Sep 2026"),
  ("3 Jul 2026", "Invoice 574370 — completion of the Employee Capability Checklist",
   "My Doctor Clinic", "Produced 5 Aug 2026 (item 3)"),
 ]),

 ("11.  Medical evidence — the injury, its onset and its continuing effect",
  "SOFC Part B, ¶¶1.2–1.4 and Part C, Contention 1 (s 32(1) WCRA)",
  "Served on the Respondent on 9 September 2026 under direction 2, behind the Appellant's schedule of "
  "medical documents relied upon. That schedule states, for each document, what it is and is not relied "
  "upon for. No report has been prepared for the purposes of this proceeding.", [
  ("1 Jan 2023 – 1 Jul 2024", "General-practice records, Our Medical Ashmore",
   "Our Medical Ashmore", "Tab M1. Held by the Respondent at its item 11 (obtained under the Form 29 signed 4 Jul 2025). Pages not relied upon are omitted; entries unrelated to the injury are redacted"),
  ("1 Jul, 7 Aug, 11 Aug and 8 Sep 2024", "Work capacity certificates of Dr P Hawes and Dr K Pang",
   "Dr P Hawes / Dr K Pang", "Tab M2. Respondent's items 7 and 8. The certificate of 8 Sep 2024 also produced 5 Aug 2026 (item 1)"),
  ("24 Oct 2024", "Email from the practice of Dr R B Krishnaiah to the Appellant, 11:45 am, \"Medications\", with the Appellant's email to QSuper of 5:12 pm the same day",
   "Mind and Memory Service", "Tab M3. Respondent's item 9"),
  ("13 Feb 2025", "Report of Dr R B Krishnaiah, Mind and Memory Service, prepared for QSuper",
   "Dr R B Krishnaiah", "Tab M4. Respondent's item 10"),
  ("5–8 Sep 2026", "Exchange with Dr Krishnaiah as to the use of his records and report",
   "Dr R B Krishnaiah / Appellant", "Tab M5"),
  ("from 24 Oct 2024", "Clinical records of Dr Krishnaiah",
   "Mind and Memory Service", "Tab M6 (tab sheet only). ⛔ Not yet received. Offered by the practice 5 Sep 2026 and requested. To be served on receipt"),
  ("24 Oct 2024", "Review Decision 69983, reasons — pages 17 and 26 to 27",
   "Workers' Compensation Regulator", "Tab M8 / Annexure A Tab 25. Respondent's item 4. Authenticity admitted; contents admitted 18 Feb 2026"),
 ]),

 ("12.  The proceeding itself",
  "Documents relied upon procedurally rather than as evidence of a matter in issue", None, [
  ("23 Jun 2026", "Affidavit of Cory Lea Shepherd (Form 20) with exhibit index, filed in support of the Form 4 application under rule 64G",
   "Appellant", "Filed and sealed 23 Jun 2026"),
  ("5 Jun 2026", "Letter, Metro South Hospital and Health Service to Commissioner Dwyer, ref K-LM26/729, signed Ms N Cridland, Chief Executive, responding to the Form 29 notice, with enclosures to Items 6, 11, 12, 13, 15 and 16",
   "Ms N Cridland, MSH", "Annexure A Tab 20. Already before the Commission. Authenticity not admitted 8 Sep 2026"),
  ("served before 18 Feb 2026", "Notice to admit facts served by the Appellant on the Respondent",
   "Appellant", "Annexure A Tab 26. Authenticity admitted"),
  ("18 Feb 2026", "The Respondent's response to that notice, signed by Ms R Matheson, Senior Appeals Officer",
   "Respondent", "Annexure A Tab 27, and Tab M9 of the medical schedule. Authenticity admitted"),
  ("28 Aug 2026", "Form 24 notice to admit facts (303 facts), Form 25 notice to admit documents (39 documents) and Annexure A (133pp)",
   "Appellant", "Served on the Respondent 28 Aug 2026, 1:47 pm"),
  ("8 Sep 2026", "The Respondent's responses to those notices, and its covering letter",
   "Respondent", "Served on the Appellant 8 Sep 2026, 11:24 am"),
  ("9 Sep 2026", "The Appellant's list of names of all witnesses; outlines of evidence; schedule of medical documents relied upon; and two letters of that date",
   "Appellant", "Filed and/or served 9 Sep 2026 under directions 1 and 2"),
 ]),
]

# correspondence packs, kept together
PACKS = [
  ("2020–2026", "Correspondence pack 01 — Logan Switchboard", "Various", "103", "Produced 5 Aug 2026 (item 9)"),
  ("2020–2026", "Correspondence pack 02 — C Donovan-Taylor", "Various", "462", "Produced 5 Aug 2026 (item 10)"),
  ("2025–2026", "Correspondence pack 03 — S Hughes", "Various", "376", "Produced 5 Aug 2026 (item 11)"),
  ("31 Jul 2026", "Correspondence pack 04 — Human Resources", "Various", "21", "Produced 5 Aug 2026 (item 12)"),
  ("2025", "Correspondence pack 05 — J Roberts", "Various", "64", "Produced 5 Aug 2026 (item 13)"),
  ("2024–2026", "Correspondence pack 10 — WorkCover Queensland", "Various", "84", "Produced 5 Aug 2026 (item 14)"),
]

PRIV = [
  ("2024–2025", "Communications between the Appellant and Saines Legal for the purpose of obtaining legal advice in this proceeding",
   "Appellant / Saines Legal", "PRIVILEGE CLAIMED — legal professional privilege"),
  ("13 May – 24 Dec 2024", "Documents recording the fact or content of a public interest disclosure and the determination made in respect of it",
   "Appellant / Ethical Standards Unit", "s 65 Public Interest Disclosure Act 2010 — non-publication sought at order 6 of the draft order"),
]

W = A4[0] - 34*mm
COLS = [10*mm, 26*mm, W - 10*mm - 26*mm - 32*mm - 44*mm, 32*mm, 44*mm]


def table(rows, start):
    data = [[Paragraph(x, CB) for x in ("No.", "Date", "Document", "Source / author", "Status and where it is")]]
    for i, (d, doc, src, st) in enumerate(rows):
        data.append([Paragraph(str(start + i), C), Paragraph(d, C), Paragraph(doc, C),
                     Paragraph(src, C), Paragraph(st, C)])
    t = Table(data, colWidths=COLS, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.35, colors.HexColor('#9a9a9a')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EDEDED')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
    ]))
    return t, start + len(rows)


story = [
    Paragraph("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", HD),
    Paragraph("Matter No. WC/2024/227 &nbsp;·&nbsp; Workers' Compensation and Rehabilitation Act 2003 (Qld)<br/>"
              "BETWEEN: <b>CORY LEA SHEPHERD</b> (Appellant) &nbsp;AND: <b>WORKERS' COMPENSATION REGULATOR</b> (Respondent)", HD2),
    Paragraph("APPELLANT'S LIST OF DOCUMENTS, ORGANISED BY THE MATTERS IN ISSUE", TT),
    Paragraph(f"Served on the Respondent &nbsp;·&nbsp; {DATE}", B),
    Paragraph(
        "This list is given in discharge of the Appellant's disclosure obligation. It supersedes and consolidates the "
        "list served on 5 August 2026, and adds the documents served since. It lists documents in the Appellant's "
        "possession or under his control that are directly relevant to a matter in issue, together with documents no "
        "longer or never in his possession and those for which privilege or statutory protection is claimed.", B),
    Paragraph(
        "<b>How it is organised.</b> The list of 5 August 2026 was organised by disclosure status. This list is organised "
        "by the <b>matter in issue</b>, in the order those matters are pleaded in the Amended Statement of Facts and "
        "Contentions filed 7 April 2026, so that each document can be found against the matter to which it goes. The "
        "disclosure status of each document is carried in the last column. Section headings identify the pleaded "
        "paragraph and do not repeat its terms; each document is described by what it is, not by what it is said to prove.", B),
    Paragraph(
        "<b>Disclosure is continuing.</b> This list will be supplemented as further documents come into the Appellant's "
        "possession, including the clinical records at section 11 and any further medical certificate or capacity advice.", B),
    Spacer(1, 2*mm),
]

n = 1
story.append(Paragraph("PART A — DOCUMENTS BY MATTER IN ISSUE", PART))
for head, pin, note, rows in SECTIONS:
    blk = [Paragraph(head, SEC), Paragraph(pin, SECN)]
    if note:
        blk.append(Paragraph(note, SECN))
    t, n = table(rows, n)
    blk.append(t)
    story.append(KeepTogether(blk) if len(rows) <= 4 else blk[0])
    if len(rows) > 4:
        story.append(blk[1])
        if note:
            story.append(blk[2])
        story.append(t)
    story.append(Spacer(1, 1.5*mm))

story.append(Paragraph("PART B — CORRESPONDENCE PACKS (relevant to more than one matter in issue)", PART))
story.append(Paragraph("Produced in full on 5 August 2026. Listed here as packs because each spans several of the "
                       "matters at Part A; the Appellant will identify individual documents within a pack on request.", SECN))
prows = [(d, doc, src, f"{st} &nbsp;·&nbsp; {pp}pp") for d, doc, src, pp, st in PACKS]
t, n = table(prows, n)
story.append(t)

story.append(Paragraph("PART C — DOCUMENTS FOR WHICH PRIVILEGE OR STATUTORY PROTECTION IS CLAIMED", PART))
t, n = table(PRIV, n)
story.append(t)

story.append(Paragraph("PART D — DOCUMENTS NOT YET IN EXISTENCE", PART))
story.append(Paragraph(
    "The Appellant will disclose, upon receipt, the clinical records of Dr Krishnaiah from 24 October 2024 "
    "(section 11), and any further medical certificate or capacity advice issued after the date of this list. "
    "The Appellant reserves the position as to any further report; if one is to be relied upon, directions will "
    "be sought before it is served.", B))

story += [Spacer(1, 5*mm),
          Paragraph("Dated " + DATE, B),
          Paragraph("<b>Cory Lea Shepherd</b>, Appellant (Self-Represented)<br/>"
                    "15 Edmond Street, Coomera QLD 4209 &nbsp;·&nbsp; 0417 400 227 &nbsp;·&nbsp; coryshepherd1@hotmail.com", B)]

TOTAL = n - 1


def foot(cv, doc):
    cv.saveState()
    cv.setFont('Helvetica', 7)
    cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(17*mm, 10*mm, f"C Shepherd · WC/2024/227 · Appellant's List of Documents (by matter in issue) · {DATE}")
    cv.drawRightString(A4[0]-17*mm, 10*mm, f"Page {cv.getPageNumber()}")
    cv.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=17*mm, rightMargin=17*mm,
                      topMargin=14*mm, bottomMargin=15*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(17*mm, 15*mm, W, A4[1]-29*mm, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0)], onPage=foot)])
doc.build(story)

# scrub
p = pikepdf.open(OUT, allow_overwriting_input=True)
try:
    del p.Root.Metadata
except (AttributeError, KeyError):
    pass
for k in list(p.docinfo.keys()):
    del p.docinfo[k]
for pg in p.pages:
    for k in ('/Metadata', '/PieceInfo', '/Annots'):
        if k in pg.obj:
            del pg.obj[k]
p.save(OUT + '.tmp', linearize=True)
os.replace(OUT + '.tmp', OUT)

chk = pikepdf.open(OUT)
clean = (not dict(chk.docinfo)) and '/Metadata' not in chk.Root
print(f"built {OUT} — {len(chk.pages)} pages, {TOTAL} numbered items, {'clean' if clean else 'METADATA SURVIVED'}")
if not clean:
    raise SystemExit("metadata survived — do not serve")
