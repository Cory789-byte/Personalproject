#!/usr/bin/env python3
"""WC/2024/227 — SCHEDULE OF ASSUMED FACTS, for the clinician pack.

Why a schedule and not a highlighted document: marking up the other side's documents is advocacy
inside the evidence. The practice holds a Form 29, so a marked-up copy would be produced to the
Regulator with the appellant's emphasis on her own admissions — and invites the question
"the document you were given had passages marked by Mr Shepherd, didn't it?"

A separate schedule does the same navigational job, is orthodox, and cannot be characterised as
marking evidence. It is also what the letter of instruction has always described as the extract of
admitted facts.

────────────────────────────────────────────────────────────────────────────────────────────────
VERIFICATION, 16 AUGUST 2026 — every Form 24 line below has now been read from the rendered
source (pdftoppm -r 150; the text layer is incomplete and must not be used). Notice ¶¶1–50 at
render pages 1–5; Respondent's Response at render pages 7–10.

⛔ THE NUMBERING DRIFT IS REAL AND WAS CONFIRMED AGAIN: after Notice ¶25 the Response renumbers.
   Response ¶26 answers Notice ¶¶26–29; thereafter Response ¶N answers Notice ¶(N+3)
   (e.g. Response ¶31 → Notice ¶34; Response ¶41 → Notice ¶47).

⭐ FOUR ERRORS IN THE PREVIOUS VERSION OF THIS SCHEDULE WERE FOUND AND FIXED:
   1. ⛔⛔ Notice ¶35 (no contemporaneous pre-2024 medical evidence contradicting the 16 Nov 2023
      entry) was listed as ADMITTED. It is **DENIED** — Response ¶32 asserts a past history of
      anxiety and ADHD **from 26 October 2022**. Presenting that to a psychiatrist as an admitted
      fact would have been the single most damaging thing in the pack.
      ⛔ **State only what the respondent asserts: a history from 26 October 2022. Say nothing
      about which exhibit holds what, and nothing about the span of the production.** Any statement
      about what the file does or does not contain is an argument about him rather than about their
      proof — and it is their assertion to prove.
   2. Notice ¶34 (the 16 Nov 2023 entry) is admitted only as **listed in the record**; accuracy
      is expressly not admitted (Response ¶31).
   3. Notice ¶38 (MDD, 13 Feb 2025) is admitted only as **what the report says**; accuracy not
      admitted (Response ¶35).
   4. Notice ¶47 (instruction held since 3 May) is **DENIED** (Response ¶41). ¶¶40 and 46 — the
      two emails themselves — are admitted, and they carry the point without the characterisation.

⭐ And ¶5 is re-dated: the words "a rostering error that was accidentally made by Chloe" are
   Ms Reese's, in her own email of **7 August 2023** — seven months before the March 2024 break.
────────────────────────────────────────────────────────────────────────────────────────────────
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=12.5, leading=16, spaceAfter=3)
SEC = ParagraphStyle('SEC', parent=ss['Heading2'], fontName='Helvetica-Bold',
                     fontSize=10.2, leading=13.5, spaceBefore=11, spaceAfter=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.4, leading=13, spaceAfter=5)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))
def P(t, s=BODY): return Paragraph(t, s)
def T(rows, w):
    t = Table(rows, colWidths=w, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
    return t

s = []
s.append(P("Schedule of assumed facts", H1))
s.append(P("WC/2024/227 · Shepherd · accompanying the letter of instruction · 17 August 2026", SMALL))
s.append(P("This schedule identifies, by source and paragraph, the facts referred to in Part B of the "
           "letter of instruction — <b>the facts you are asked to assume</b>. <b>The documents themselves "
           "accompany it, complete and unmarked.</b> "
           "Where a passage is quoted, the quotation is exact. <b>Section B records the matters the "
           "Workers' Compensation Regulator does <i>not</i> accept, so that the position is "
           "complete.</b>", BODY))

s.append(P("A · ACCEPTED BY THE WORKERS' COMPENSATION REGULATOR — RESPONSE SIGNED BY "
           "MS RENEE MATHESON, SENIOR APPEALS OFFICER, 18 FEBRUARY 2026", SEC))
s.append(P("Item numbers are those of the list to which that document responds; the cross-references "
           "have been checked against it. These are facts the Regulator accepts.", SMALL))
s.append(T([
 [P("<b>Item</b>", SMALL), P("<b>Fact accepted</b>", SMALL)],
 [P("1", SMALL), P("On <b>17–18 March 2024</b> the appellant was rostered to finish at 23:00 and "
   "commence his next shift at 06:00, <b>a break of only 7 hours</b>.", SMALL)],
 [P("3", SMALL), P("The employer's fatigue risk management policy and the relevant Award require a "
   "<b>minimum break of 10 hours between shifts, or 8 hours by written agreement</b>.", SMALL)],
 [P("5", SMALL), P("Ms Tammy Reese stated in an email of <b>7 August 2023</b>: <i>“I do realise in this "
   "instance there was a <b>rostering error that was accidentally made by Chloe</b> with regards to "
   "night shifts.”</i>", SMALL)],
 [P("8", SMALL), P("<b>Maintaining accurate contact details for medical staff is a critical function "
   "of the Switchboard to ensure effective clinical handover and patient safety.</b> It adds that "
   "<i>“there was a procedure in place for this to occur.”</i>", SMALL)],
 [P("20", SMALL), P("On <b>24 December 2024</b> the Ethical Standards Unit determined that the "
   "appellant's complaint regarding Ms Taylor and Ms Reese <b>constituted a Public Interest "
   "Disclosure</b>.", SMALL)],
 [P("33", SMALL), P("The clinical records contain a consultation record dated <b>16 November 2023</b> "
   "authored by Dr Priyal De Silva Nanayakkara. <i>(Accepted as being in the record; its accuracy "
   "is not accepted — see B.)</i>", SMALL)],
 [P("38", SMALL), P("The report of Dr Ravikumar Krishnaiah <b>states that the appellant was suffering "
   "from Major Depressive Disorder</b>, diagnosed 13 February 2025. <i>(Accepted as what the report "
   "says; its accuracy is not accepted.)</i>", SMALL)],
 [P("40", SMALL), P("On <b>3 May 2024</b> Payroll Officer Elaine Grant emailed the line manager "
   "instructing her to <i>“submit an AVAC to correct these shifts”</i> for the appellant.", SMALL)],
 [P("41", SMALL), P("The <b>AVAC was submitted on 28 May 2024</b>. It adds that on 21 May the line "
   "manager had said she was waiting on payroll confirmation.", SMALL)],
 [P("46", SMALL), P("On <b>21 May 2024 at 12:33pm</b> the line manager emailed the appellant: <i>“I am "
   "waiting payroll confirmation… as soon as I do get that confirmation, I will submit an AVAC.”</i>",
   SMALL)],
], [12*mm, 154*mm]))

s.append(P("A2 · FROM A FURTHER DOCUMENT OF THE WORKERS' COMPENSATION REGULATOR, 13 MAY 2026", SEC))
s.append(P("These are its own positive statements in that document.", SMALL))
s.append(T([
 [P("<b>Item</b>", SMALL), P("<b>What it records</b>", SMALL)],
 [P("14(e)<br/>14(f)", SMALL), P("On the special pandemic leave application (leave of <b>20–27 "
   "February 2024</b>), which was declined for want of an attached statutory declaration: "
   "<i>“says that a review indicates that <b>in fact, the attachments were present</b> on the "
   "appellant's submission”</i> · <i>“says this was a matter of <b>human error by Ms Taylor</b> on the "
   "background of high work demands surrounding the management of staff with COVID-19”</i>.", SMALL)],
 [P("22(a)", SMALL), P("On the rostering of 17–18 March 2024: <i>“says the shift was separated by only "
   "a <b>7-hour break (rather than an 8-hour break)</b> says that this was a result of <b>human "
   "error</b> and not intentional or repeated”</i>.", SMALL)],
 [P("22(c)", SMALL), P("<i>“says the appellant took <b>leave on 19 March 2024</b>”</i>, and says this "
   "was paid leave.", SMALL)],
], [16*mm, 150*mm]))

s.append(P("B · NOT ACCEPTED — AND WHAT THE REGULATOR SAYS INSTEAD", SEC))
s.append(P("Recorded so that no fact in section A is read as broader than it is.", SMALL))
s.append(T([
 [P("<b>Item</b>", SMALL), P("<b>Its position</b>", SMALL)],
 [P("4", SMALL), P("<b>Not accepted</b> that there was no written agreement: <i>“in June 2020, the Appellant "
   "signed an agreement allowing an <b>8 hour break</b> between shifts.”</i> <b>On that case the "
   "applicable minimum was 8 hours, and the break given was 7.</b>", SMALL)],
 [P("34", SMALL), P("Accepts the 16 November 2023 entry (<i>“No psychological illness such as "
   "depression/ psychosis”</i>) <b>is in the record, but does not accept its accuracy</b>.",
   SMALL)],
 [P("35", SMALL), P("<b>Not accepted.</b> It asserts <b>a past medical history of anxiety and ADHD "
   "from 26 October 2022</b>.", SMALL)],
 [P("47", SMALL), P("<b>Not accepted</b> that the line manager had simply held the instruction: it "
   "says <i>“Ms Taylor needed confirmation from payroll and then she needed to be satisfied that "
   "the AVAC was accurate.”</i> <i>(The two emails at items 40 and 46 are accepted.)</i>", SMALL)],
], [12*mm, 154*mm]))

s.append(P("C · FROM THE LETTER OF THE CHIEF EXECUTIVE, METRO SOUTH HEALTH, 5 JUNE 2026", SEC))
s.append(P("Item numbers are those of the letter. Read from source.", SMALL))
s.append(T([
 [P("<b>Item</b>", SMALL), P("<b>What the letter records</b>", SMALL)],
 [P("1–2", SMALL), P("Pre-upgrade SPOK records were not retained. <b>“However, a spreadsheet of "
   "recorded MET calls is available for the period 17-18 March 2024.”</b>", SMALL)],
 [P("3(a)", SMALL), P("<i>“All employee complaints relating to Logan Hospital Switchboard "
   "operational errors are made directly to the Line Manager of Switch Board and managed <b>solely "
   "via email or verbally</b> with the complainant.”</i>", SMALL)],
 [P("3(c)", SMALL), P("<i>“there have been <b>no ‘consequential’ changes to operating procedures</b> "
   "over the period requested.”</i>", SMALL)],
 [P("4", SMALL), P("The requested fatigue risk assessment records <b>do not exist</b>. <i>“Mandatory "
   "Fatigue Risk Management System training only applies to health practitioners and clinical "
   "assistants. The Logan Hospital Switchboard staff are non-clinical staff…”</i>", SMALL)],
 [P("5", SMALL), P("<i>“The implementation of fatigue risk management assessment at Switchboard "
   "Logan Hospital occurred <b>after 30 June 2024</b> in connection with an organisational change "
   "related to the reporting lines for Switchboard.”</i>", SMALL)],
 [P("7", SMALL), P("The requested fatigue risk management register entries <b>do not exist</b>.", SMALL)],
 [P("15", SMALL), P("Enclosed: <b>leave takings report for the Applicant, 19 March 2024</b>.", SMALL)],
], [14*mm, 152*mm]))

s.append(P("D · FROM THE ROLE DESCRIPTION — ADMINISTRATION OFFICER, SWITCHBOARD SERVICES (AO3)", SEC))
s.append(P("Quoted from the employer's own document. Read from source.", SMALL))
s.append(T([
 [P("<b>Under</b>", SMALL), P("<b>The position requires</b>", SMALL)],
 [P("Purpose", SMALL), P("<i>“The occupant of this position is required to work <b>continuous shift "
   "work over the full 24-hour period, 7 days a week</b>.”</i>", SMALL)],
 [P("Key<br/>responsibilities", SMALL), P("<i>“<b>Participate in the Emergency Response process</b> "
   "by receiving emergency response notifications and distributing them to the appropriate response "
   "groups, dependent on the category of emergency, as per emergency code procedures, <b>strictly "
   "adhering to protocols and timeframes</b>.”</i>", SMALL)],
 [P("", SMALL), P("<i>“<b>Maintain call queues to minimum at all times</b>.”</i> · <i>“The ability to "
   "<b>multitask and operate under pressure</b>, particularly where <b>high volume call traffic</b> "
   "is concerned.”</i>", SMALL)],
 [P("", SMALL), P("<i>“Maintain discretion and <b>exercise judgement</b> where necessary to resolve "
   "problems within the scope of your role; <b>in situations where precedence have not been set and "
   "procedures not defined</b>.”</i>", SMALL)],
 [P("", SMALL), P("<i>“Ability to work effectively as an individual with <b>limited supervision</b>…”</i>",
   SMALL)],
 [P("", SMALL), P("<i>“<b>Collate information and maintain Omnivista database and SharePoint</b> to "
   "ensure information held within Switchboard Services is accurate and appropriate.”</i>", SMALL)],
 [P("Mandatory<br/>requirements", SMALL), P("<i>“The position is a <b>continuous shift working "
   "role</b>. You must be able to work a roster which covers multiple shifts over a 24/7 period.”</i>",
   SMALL)],
], [26*mm, 140*mm]))

s.append(P("E · FROM THE EMPLOYEE CAPABILITY CHECKLIST, 3 JULY 2026", SEC))
s.append(P("Read from source. Quotations exact.", SMALL))
s.append(T([
 [P("<b>Question</b>", SMALL), P("<b>What the checklist records</b>", SMALL)],
 [P("1", SMALL), P("<i>“<b>Major Depressive Disorder with anxious distress (DSM-5 296.23)</b>, a "
   "<b>work-related psychological injury with onset 18 June 2024</b>… Residual symptoms most "
   "relevant to work capacity are <b>reduced concentration and working memory under sustained "
   "high-demand load, fatigue sensitivity</b>, and symptom exacerbation on exposure to the "
   "identified workplace stressors (<b>complaint handling; being held accountable and blamed for "
   "the failures of others; unpredictable rostering</b>).”</i>", SMALL)],
 [P("2", SMALL), P("<i>“<b>Episodic</b>, with symptom exacerbation linked to stressor exposure. The "
   "restrictions below are expected to remain necessary for at least the next <b>3–6 months</b>, "
   "subject to treatment response and <b>8-weekly review</b>.”</i>", SMALL)],
 [P("3", SMALL), P("<b>Six 8-hour shifts per fortnight</b> (of ten in a full-time fortnight) — no more "
   "than two weekday day/afternoon, two weekend day, two night. ⭐ <i>“This reduced pattern of "
   "approximately six shifts per fortnight is the pattern Mr Shepherd <b>has in fact worked and "
   "tolerated over the past twelve months without deterioration</b>… <b>Usual switchboard "
   "operational duties remain suitable</b>; complaint-handling duties are excluded as below.”</i>",
   SMALL)],
 [P("4", SMALL), P("<i>“(a) <b>No complaint-handling duties</b> — complaints received at the "
   "Switchboard to be <b>logged and redirected</b>, not actioned or resolved by Mr Shepherd; "
   "(b) <b>predictable rostering published in advance, with a minimum 10-hour break between shifts "
   "consistent with the Award and fatigue risk management standards</b>; (c) return-to-work "
   "coordination through the Injury Management team; (d) access to EAP; (e) review in approximately "
   "8 weeks.”</i>", SMALL)],
 [P("Meds", SMALL), P("<b>Fluoxetine 60mg mane</b> · <b>lisdexamfetamine 30mg mane</b> for cognitive "
   "symptoms and focus · quetiapine 25mg nocte <b>ceased</b>. <i>“maintaining a regular sleep "
   "routine remains central to symptom management following cessation of the night-time "
   "medication.”</i>", SMALL)],
], [17*mm, 149*mm]))

s.append(P("F · FROM THE APPROVED CHANGES TO WORKING HOURS, 2026 — ATTACHMENT 5", SEC))
s.append(P("Fields copied from the employer's own forms. Full-time fortnight for the position: "
           "76 hours.", SMALL))
s.append(T([
 [P("<b>Delegate approval</b>", SMALL), P("<b>Effective period</b>", SMALL),
  P("<b>Hours / fortnight</b>", SMALL), P("<b>Shift arrangements</b>", SMALL)],
 [P("<b>27.02.2026</b>", SMALL), P("01.03.2026 – 15.03.2026", SMALL), P("<b>56.00</b>", SMALL),
  P("<b>Continuous Shift Worker</b>", SMALL)],
 [P("<b>17.04.2026</b>", SMALL), P("16.03.2026 – 26.04.2026", SMALL), P("<b>56.00</b>", SMALL),
  P("<b>Continuous Shift Worker</b>", SMALL)],
 [P("<b>09.06.2026</b>", SMALL), P("25.05.2026 – 28.06.2026", SMALL), P("<b>40.00</b>", SMALL),
  P("<b>Continuous Shift Worker</b>", SMALL)],
], [32*mm, 46*mm, 28*mm, 60*mm]))
s.append(P("Each form records the movement task as <i>“Change to Working Conditions (Temporary)”</i> "
           "and the position as <b>AO Switchboard, AO3, Level 04</b>.", SMALL))

doc = SimpleDocTemplate("out/SCHEDULE_OF_ASSUMED_FACTS.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — schedule of assumed facts", author="Cory Lea Shepherd")
def f(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm, "WC/2024/227 · Shepherd · schedule of assumed facts")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
print("built out/SCHEDULE_OF_ASSUMED_FACTS.pdf")
