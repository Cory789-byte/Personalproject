#!/usr/bin/env python3
"""WC/2024/227 — Psychiatrist instruction: THE QUESTIONS and THE DOCUMENTS, separated.

Builds drafts/out/QUESTIONS_AND_DOCUMENTS_Krishnaiah.pdf — an internal working reference
setting out (Part 1) every question asked of Dr Krishnaiah, (Part 2) every document provided
and its status, and (Part 3) the defects found on review at 14 Aug 2026.

⛔ INTERNAL. Not for service. Not for the practice. Part 3 is working analysis.
Source: drafts/out/CEILING_SET/01_Letter_of_Instruction_Report_B.md
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle)

OUT = "out/QUESTIONS_AND_DOCUMENTS_Krishnaiah.pdf"

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=15, leading=19, spaceAfter=4, textColor=colors.HexColor('#111111'))
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold',
                    fontSize=11.5, leading=15, spaceBefore=11, spaceAfter=4,
                    textColor=colors.HexColor('#1a1a1a'))
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.6, leading=13.4, spaceAfter=5, alignment=0)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.4, leading=11.6,
                       textColor=colors.HexColor('#444444'))
QNUM = ParagraphStyle('QNUM', parent=BODY, fontName='Helvetica-Bold',
                      fontSize=10, leading=13.5, spaceBefore=9, spaceAfter=2)
NOTE = ParagraphStyle('NOTE', parent=BODY, fontSize=8.8, leading=12,
                      leftIndent=8, textColor=colors.HexColor('#7a2018'))

def P(t, s=BODY):
    return Paragraph(t, s)

# ─────────────────────────────────────────────── PART 1 — THE QUESTIONS
QUESTIONS = [
 ("6.1", "Diagnosis, criteria and onset",
  "The diagnosis; the classificatory framework applied (e.g. DSM-5, with the code); "
  "<b>the specific diagnostic criteria met, and when each was met</b>; and the date of onset "
  "as best the clinical record establishes it."),
 ("6.2", "Differential diagnoses",
  "The differential diagnoses considered, and the reasons for including or excluding each."),
 ("6.3", "Psychiatric background",
  "Background psychiatric history — in particular <b>the entries of 26 October 2022 referring to "
  "anxiety and ADHD</b> (Enclosure E) and any earlier stimulant (Vyvanse) use. Whether there was "
  "any relevant pre-existing condition; and if so, <b>whether the employment matters aggravated "
  "it, and to what extent</b>."),
 ("6.4", "Sources",
  "A <b>complete list of every document reviewed and every person seen</b>, with dates and the "
  "duration of each examination. Asked for specifically because the completeness of the source "
  "list is the first thing tested."),
 ("6.5", "Causation — s 32(1)",
  "On the assumed facts, whether employment — and in particular the rostering and fatigue "
  "sequence of 17 March to 1 May 2024 (the consecutive shifts, the admitted 7-hour break, the "
  "requests for fatigue relief, the refusal, and the consequent use of his own leave), the "
  "conditions of the Switchboard role as described in the assumed facts, and the handling of the "
  "concerns raised — was <b>a significant contributing factor</b> to the injury with onset "
  "pleaded at 18 June 2024. With clinical reasoning, distinguishing the <b>cause of onset</b> "
  "from factors bearing only on the <b>subsequent course</b>."),
 ("6.6", "The April–May 2024 material, and the interval before presentation",
  "What, if anything, he makes of the reports of fatigue recorded in April and May 2024 in the "
  "context of the diagnosis made subsequently. Separately, what clinical significance attaches to "
  "the interval between pleaded onset (18 June 2024) and first medical presentation — the Hawes "
  "certificate recording first attendance for this injury on 1 July 2024."),
 ("6.7", "Competing (non-employment) causes, placed in time",
  "Any non-employment factors relevant to (a) onset at or about 18 June 2024 and (b) subsequent "
  "course. For each, <b>when in time it arose relative to 18 June 2024</b>. Assumed as facts: "
  "employment ceased about October 2024 (later reversed by reinstatement); personal and "
  "relationship matters commenced from about December 2024."),
 ("6.8", "Premorbid personality",
  "Whether any premorbid personality features bear on (a) the diagnosis and (b) causation at 6.5 "
  "— <b>from his own clinical assessment</b>, not by adopting any earlier characterisation."),
 ("6.9", "Mechanism",
  "<b>Whether, and if so how</b>, conditions of the kind described in the assumed facts — "
  "sustained demand, the degree of control or autonomy, the adequacy of support, and fatigue "
  "arising from the rostering — can contribute to a condition of the kind diagnosed."),
 ("6.10", "Prognosis and capacity",
  "Prognosis. On capacity, distinguishing (a) capacity to perform the substantive role <b>with "
  "reasonable adjustments</b> from (b) any current incapacity; and if there is current incapacity, "
  "its cause — the condition itself, the consequences of exclusion from the workplace since "
  "3 July 2026, or other factors."),
 ("6.11", "Change in capacity over time",
  "How capacity has evolved between the assessment of 13 February 2025 and the present, and the "
  "reasons for any change."),
]

# ─────────────────────────────────────────────── PART 2 — THE DOCUMENTS
DOCS = [
 ("A", "Signed statement", "His own signed statement.",
  "ASSUMED FACT", "His account. Signed — but still his."),
 ("B", "Chronology", "A chronology of the relevant events.",
  "ASSUMED FACT", "Corroborative of Enclosure A."),
 ("C", "Amended Form 9A (7 April 2026)", "The pleaded case.",
  "SCOPE / CONTEXT ONLY",
  "Expressly <b>NOT</b> facts he is asked to assume. Provided so the matters in issue are visible. "
  "The case is a course of management conduct as to rostering, fatigue, pay and the handling of "
  "concerns — <b>not</b> bullying or harassment."),
 ("D", "Form 24 admitted-facts extract (18 Feb 2026)",
  "The Regulator's admissions: the rostered break of 7 hours between the shifts of 17 and "
  "18 March 2024; the criticality of the Switchboard function; the admitted delay in handling.",
  "ASSUMED FACT — ADMITTED",
  "⭐ The only basket the Respondent has conceded. This is what carries the sentence that the "
  "opinion does not depend on his account."),
 ("E", "GP records — Our Medical Ashmore",
  "Including the entries of 26 October 2022 (anxiety, ADHD), earlier Vyvanse use, and the entry "
  "of 16 November 2023.", "CLINICAL RECORD",
  "The 2022 pages are IN and visible. Disclosure is credibility."),
 ("F", "Work Capacity Certificate — Dr Peter Hawes",
  "Records first attendance for this injury on 1 July 2024. Signed 8 September 2024.",
  "CLINICAL RECORD",
  "Use for <b>timing</b>. ⛔ Not for mechanism — the recorded mechanism words are his own account."),
 ("G", "Certificate of capacity, 3 July 2026",
  "Certifies him fit for the substantive role with adjustments.", "CLINICAL RECORD", ""),
 ("H", "Report of 13 February 2025", "His own earlier report (MDD diagnosis).",
  "CLINICAL RECORD",
  "⚠ Every page stamped “disclosed for Qsuper and <b>not for medico-legal use</b>”."),
 ("I", "His own clinical records", "The treating file.", "CLINICAL RECORD", ""),
]

story = []
story.append(P("WC/2024/227 — Shepherd v Workers' Compensation Regulator", H1))
story.append(P("THE QUESTIONS AND THE DOCUMENTS — psychiatric instruction, as it currently stands",
               ParagraphStyle('sub', parent=BODY, fontSize=10.5, leading=14,
                              spaceAfter=8, textColor=colors.HexColor('#333333'))))
story.append(P("Dr Ravikumar Bangalore Krishnaiah, Consultant Psychiatrist, Mind and Memory Service. "
               "Source: <i>01_Letter_of_Instruction_Report_B</i>. Reviewed 14 August 2026.", SMALL))
story.append(P("⛔ <b>INTERNAL WORKING DOCUMENT.</b> Not for service, and not for the practice in this "
               "form. Part 3 is working analysis.", SMALL))
story.append(Spacer(1, 7*mm))

# PART 1
story.append(P("PART 1 — THE QUESTIONS ASKED", H2))
story.append(P("Eleven questions. Each stands alone; none combines the clinical question with the "
               "statutory one.", SMALL))
for num, title, text in QUESTIONS:
    story.append(P(f"{num} &nbsp; {title}", QNUM))
    story.append(P(text, BODY))

story.append(PageBreak())

# PART 2
story.append(P("PART 2 — THE DOCUMENTS PROVIDED", H2))
story.append(P("Nine enclosures, in three classes. <b>The class matters more than the content</b> — "
               "only the admitted-facts basket can support an opinion said not to depend on his "
               "account.", SMALL))
story.append(Spacer(1, 3*mm))

rows = [[P("<b>Encl.</b>", SMALL), P("<b>Document</b>", SMALL),
         P("<b>What it is</b>", SMALL), P("<b>Status</b>", SMALL)]]
for code, name, what, status, note in DOCS:
    body = f"<b>{name}</b><br/>{what}"
    if note:
        body += f"<br/><font color='#7a2018'>{note}</font>"
    rows.append([P(f"<b>{code}</b>", SMALL), P(body, SMALL), P("", SMALL), P(f"<b>{status}</b>", SMALL)])

# collapse the empty third column
rows = [[r[0], r[1], r[3]] for r in rows]
t = Table(rows, colWidths=[14*mm, 116*mm, 36*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(t)

story.append(Spacer(1, 4*mm))
story.append(P("The three classes", H2))
story.append(P("<b>1 · ASSUMED FACTS (A, B, D)</b> — the facts he is asked to take as established. "
               "⭐ Only <b>D</b> is admitted by the Respondent; A and B are the appellant's own.", BODY))
story.append(P("<b>2 · SCOPE AND CONTEXT ONLY (C)</b> — provided to show the matters in issue, "
               "expressly not to be assumed.", BODY))
story.append(P("<b>3 · CLINICAL RECORD (E–I)</b> — for clinical review, not as facts about the "
               "workplace.", BODY))

story.append(PageBreak())

# PART 3
story.append(P("PART 3 — WHAT REVIEW ON 14 AUGUST FOUND", H2))

story.append(P("⛔⛔ 1. The letter still carries the superseded TWO-REPORT structure", QNUM))
story.append(P("Question <b>6.10</b> ends: <i>“(The detailed assessment of adjustments is the subject "
               "of the separate Metro South report.)”</i> — and section 2 is headed <i>“how it differs "
               "from the report for Metro South”</i>.", BODY))
story.append(P("<b>There is one report</b> (settled 6 August, <i>confirmed-record.md</i>). If the "
               "clinician is told the adjustments are someone else's job, <b>the report will not "
               "contain them</b> — and RFMI Q6 and Q9 both depend on them. This is the most "
               "consequential defect on the page.", NOTE))
story.append(P("<b>FIX:</b> delete the parenthesis; rewrite 6.10 to ask for the adjustments in "
               "functional terms — predictable rostering; adequate recovery between shifts; not "
               "sustained concurrent emergency-code load; day hours; reporting line outside the "
               "directorate concerned — and whether each is ordinary and available.", BODY))

story.append(P("⛔⛔ 2. Review Decision 69983 — three documents, two positions", QNUM))
story.append(P("<i>confirmed-record.md</i> (6 Aug) lists it among documents reviewed; the letter-of-"
               "instruction verification (9 Aug) removed it entirely as a critical defect; the "
               "bundle (12 Aug) calls it the most important document in the pack.", BODY))
story.append(P("<b>Establish first: was it put in front of him on 12 August?</b> Nothing further goes "
               "to the practice until that is answered.", NOTE))

story.append(P("⭐⭐ 3. Enclosure D is far smaller than the available admitted record", QNUM))
story.append(P("It is currently the Form 24 extract alone. Available now, with nothing served: the "
               "SOFC admissions register of 10 August (the PID admitted in full; the break and "
               "“human error”; the COVID attachments “in fact present”; the AVAC chain; the May "
               "prodrome); and the <b>negatives</b>, now pleadable against the certified list of "
               "documents of 14 August.", BODY))

story.append(P("⭐⭐⭐ 4. Two documents are missing and should be added", QNUM))
story.append(P("<b>The Chief Executive's letter of 5 June 2026</b> — no fatigue risk assessment "
               "existed; fatigue management implemented only after 30 June 2024; complaints managed "
               "solely by email or verbally; <b>no consequential changes to operating procedures</b>; "
               "MET calls recorded on the shifts of 17–18 March 2024; the leave takings report for "
               "19 March 2024. The employer's own account of the absent controls.", BODY))
story.append(P("<b>The AO3 Switchboard role description</b> — continuous shift work over the full "
               "24-hour period, 7 days a week; Emergency Response duties strictly adhering to "
               "protocols and timeframes; call queues to minimum at all times; judgement exercised "
               "where procedures are not defined; limited supervision. The employer's own account of "
               "the demands.", BODY))
story.append(P("⭐ Together these supply demand, control and support from the employer's own hand — "
               "and they replace Review Decision 69983 without any of its contamination.", NOTE))

story.append(P("⭐⭐⭐ 5. The single highest-value question is not yet asked", QNUM))
story.append(P("<i>“Please state whether your opinion at 6.5 would differ if you were to assume "
               "<b>only</b> the facts at Enclosure D — being facts admitted by the Respondent — and "
               "to disregard Enclosure A entirely.”</i>", BODY))
story.append(P("If the answer is “no difference”, the opinion cannot be met with the self-report "
               "attack and survives any challenge to him as a witness.", NOTE))

story.append(P("⚠ 6. One-report consequence for the schedule", QNUM))
story.append(P("The report goes to Metro South in full and is disclosed in the appeal; it cannot be "
               "redacted. <b>The assumed-facts schedule travels to both audiences.</b> Admissions, "
               "employer documents, dates and arithmetic only — no parallel-track content, no "
               "characterisations.", BODY))

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — Questions and Documents (psychiatric instruction)",
                        author="Cory Lea Shepherd")

def footer(canv, d):
    canv.saveState()
    canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm,
                    "WC/2024/227 · Questions and documents — psychiatric instruction · internal working document")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("built", OUT)
