#!/usr/bin/env python3
"""WC/2024/227 - SECOND AMENDED FORM 9A, RESTRUCTURED, WITH THE ADMISSIONS OVERLAID.

The pleading rebuilt on the chain established from the documents: the duty, the means, the
repair path, the latency, the consequence. Characterising vocabulary removed throughout.

Black  = pleaded text.
Blue   = the text of a fact admitted 8 September 2026, word for word, with its paragraph number.
Red    = material not yet admitted; it becomes fact once agreed or proved.

Facts are the 303 paragraphs as served and answered, read via served_facts.py.
⛔ DRAFT. Leave to amend is required; the application cannot be made before 30 September 2026
and must be made not less than 7 days before the hearing (Appeal Guide Part 4.6).
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from served_facts import FACT as F, NOT_ADMITTED, TOTAL
assert TOTAL == 303

BLUE = colors.HexColor('#123f8c'); GREY = colors.HexColor('#6b6b6b'); RED = colors.HexColor('#9b1c1c')
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=15, spaceAfter=2)
H2  = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.2, leading=10.2, textColor=GREY, spaceAfter=4)
KEY = ParagraphStyle('KEY', fontName='Helvetica', fontSize=7.5, leading=9.2, spaceAfter=2)
PART= ParagraphStyle('PART', fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceBefore=9,
                     spaceAfter=3)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=8.9, leading=11, spaceBefore=5,
                     spaceAfter=2)
PLD = ParagraphStyle('PLD', fontName='Helvetica', fontSize=8.3, leading=10.4, leftIndent=4*mm,
                     spaceAfter=2)
ADM = ParagraphStyle('ADM', fontName='Helvetica', fontSize=7.9, leading=9.7, leftIndent=8*mm,
                     textColor=BLUE, spaceAfter=1.1)
PEN = ParagraphStyle('PEN', fontName='Helvetica', fontSize=7.9, leading=9.7, leftIndent=8*mm,
                     textColor=RED, spaceAfter=1.1)
NOTE= ParagraphStyle('NOTE', fontName='Helvetica-Oblique', fontSize=7.6, leading=9.3,
                     leftIndent=8*mm, textColor=RED, spaceAfter=3)
SCH = ParagraphStyle('SCH', fontName='Helvetica', fontSize=7.8, leading=9.6, leftIndent=4*mm,
                     spaceAfter=1.6)
def P(t, s): return Paragraph(t, s)
def q(ns):
    out = []
    for n in ns:
        st = PEN if n in NOT_ADMITTED else ADM
        tag = ' <b>[NOT YET ADMITTED]</b>' if n in NOT_ADMITTED else ''
        out.append(P(f"<b>[{n}]</b> {F[n]}{tag}", st))
    return out
def rng(a, b): return f"<i>Admitted: paragraphs {a} to {b}.</i>"

s = [P("SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS &ndash; RESTRUCTURED DRAFT", H1),
 P("WC/2024/227 &ndash; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator "
   "(Respondent). Section 550(4), Workers' Compensation and Rehabilitation Act 2003.", H2),
 P("<b>Black</b> is pleaded text. <font color='#123f8c'><b>Blue</b> is the text of a fact the "
   "Respondent admitted on 8 September 2026 in answer to the notice to admit facts served "
   "28 August 2026, word for word, with its paragraph number in brackets. Of 303 paragraphs, 298 "
   "were admitted, five were not admitted, and none was denied. Admissions are for this proceeding "
   "only, under rule 49 of the Industrial Relations (Tribunals) Rules 2011.</font> "
   "<font color='#9b1c1c'><b>Red is material not yet admitted. It becomes fact once agreed or "
   "proved.</b></font>", KEY),
 P("⛔ <b>DRAFT.</b> Leave to amend is required. The application cannot be made before "
   "30 September 2026 and must be made not less than seven days before the hearing "
   "(Workers' Compensation Appeal Guide, Part 4.6). No characterisation of any person appears in "
   "this pleading; every adjective in it belongs to a document.", KEY),
 Spacer(1, 2*mm),

 P("PART A &ndash; THE POSITION, AND WHAT IT REQUIRED", PART),
 P("1. &nbsp;The Appellant was employed by Metro South Hospital and Health Service as an "
   "Administration Officer, Switchboard Services, Logan Hospital, classification AO3. The position "
   "is a continuous shift working role over a 24-hour period, seven days a week. It reports to the "
   "Switchboard Manager, and the contact named for the position is Ms Chloe Taylor.", PLD)]
s += q([1, 2, 3, 4, 13, 14, 15, 16])
s += [P("2. &nbsp;Three key responsibilities of the position are relied on. They are the duties the "
   "matters pleaded below bear upon.", PLD)]
s += q([5, 6, 7, 8, 10])

s += [P("PART B &ndash; STRESSOR 1: THE CONDITIONS IN WHICH THE WORK WAS CARRIED ON", PART),
 P("<b>B1. The duty to keep the directory accurate, and the removal of the means of doing it</b>", SEC),
 P("3. &nbsp;On 18 July 2023 access to the database was removed from all operators, the Contact "
   "and Number Changes book was taken out of the room, and a correction sought after hours was to "
   "wait until one of two named persons returned. The Respondent does not allege that access was "
   "restored at any time before 18 June 2024. The duty at paragraph 2 remained on the position "
   "throughout.", PLD)]
s += q([39, 40, 41, 42, 43, 44, 45, 55])

s += [P("<b>B2. The repair path, and how long a wrong entry stayed wrong</b>", SEC),
 P("4. &nbsp;From 18 July 2023 an incorrect entry could be corrected only by Ms Stibbard, whose "
   "stated working hours were one and a half days a fortnight in a temporary project role, or by "
   "Ms Taylor. The Appellant does not plead any characterisation of Ms Taylor. He pleads the hours "
   "she stated to the Switchboard, because they determine how long an incorrect entry remained "
   "uncorrected. Between 23 August 2023 and 17 May 2024 no fixed office hours were stated to the "
   "staff.", PLD)]
s += q([39, 41, 70, 71, 72, 73, 81, 82, 83, 84, 85, 86, 87, 88])
s += [P("5. &nbsp;From 15 April 2024 the same two persons were also the after-hours contact, and "
   "from 14 May 2024 the same person was also the route for notifying unavailability for a "
   "rostered shift.", PLD)]
s += q([49, 50, 51, 52, 53, 111, 112, 113, 162, 163, 164, 165, 166])

s += [P("<b>B3. What then arrived at the console</b>", SEC),
 P("6. &nbsp;On 3 and 8 May 2024 the MASPER Registrar reported to Ms Taylor nine occasions on "
   "which calls reached the wrong medical team. Those occasions fell while the arrangement notified "
   "on 15 April 2024 was in force. The first reply was sent five days, eighteen hours and fourteen "
   "minutes after the first report, and sought the reporting clinician's business hours. The "
   "Respondent does not allege that anything was communicated to the Switchboard staff about those "
   "occasions before 10:15 am on 9 May 2024.", PLD)]
s += q([56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69])
s += [P("7. &nbsp;On 15 and 20 May 2024 the Integrated Respiratory Service asked the Switchboard to "
   "amend a directory entry and reported that it continued to receive misdirected calls. The "
   "Appellant escalated the cause within three hours and two minutes of the second email, "
   "identifying a modification made to the contact-details document on 22 February 2024 and "
   "recommending a review. The reply stated the task was being actioned and had been discussed that "
   "morning. The Respondent's List of Documents records no document of that discussion, no "
   "communication to the Service, no amendment to the document, and no notification to the "
   "Switchboard staff of the modification.", PLD)]
s += q(list(range(89, 111)))

s += [P("<b>B4. The obligation to consult, and its absence</b>", SEC),
 P("8. &nbsp;Clause 3.2 of the Queensland Public Health Sector Certified Agreement (No. 11) 2022 "
   "requires that consultation be more than a mere exchange of information, that participants "
   "contribute to the decision-making process \"not only in appearance, but in fact\", and that the "
   "exchange of information occur so that there is \"an actual and genuine opportunity to influence "
   "the outcome, before a final decision is made\". Clause 4.1.4 requires a business case tabled "
   "for consultation for significant organisational change including major alterations to service "
   "delivery arrangements. The change notified on 15 April 2024 was stated to be effective the same "
   "day, and the Respondent's List of Documents records no document of any consultation with "
   "Switchboard operators before it.", PLD)]
s += q([51, 54, 273])
s += [P("9. &nbsp;The employer conducted that process on other occasions. In November and December "
   "2024 it issued a Consultation Paper and a Consultation outcome for the Switchboard rosters, in "
   "which agreement is defined as the consent of a majority of affected employees.", PLD)]
s += q(list(range(167, 182)))
s += [P("10. &nbsp;On 20 May 2024 the manager wrote that updated procedures could be put to the team "
   "for consultation before implementing.", PLD)]
s += q([101])

s += [P("<b>B5. What the Appellant raised, and what followed</b>", SEC),
 P("11. &nbsp;On 6 June 2023 a reminder placed in the Communication Book concerning the monthly "
   "update of medical contact numbers was removed. The Respondent admits the removal in its "
   "pleading and again on 8 September 2026. It does not allege that the removed page has been "
   "located or that any copy exists, and the Communication Book is not listed in its List of "
   "Documents.", PLD)]
s += q([143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154])
s += [P("12. &nbsp;The Appellant raised matters concerning hours and workplace issues in August and "
   "September 2023.", PLD)]
s += q(list(range(26, 39)) + list(range(155, 162)))
s += [P("12A. &nbsp;On 13 May 2024 the Appellant made a complaint to the Metro South Health Ethical "
   "Standards Unit, which that Unit determined on 24 December 2024 constituted a public interest "
   "disclosure, reference 24-ESU-1130. <b>The content of the disclosure is not set out, and no "
   "connection between it and any subsequent conduct is pleaded or relied upon in this appeal.</b> "
   "The fact is pleaded only to complete the sequence of matters the Appellant raised.", PLD),
 P("[⚠ SOURCING &mdash; this paragraph is NOT supported by the notice to admit facts served "
   "28 August 2026. None of the 303 paragraphs refers to the Ethical Standards Unit, to a public "
   "interest disclosure, or to a complaint of 13 May 2024. It must be proved from the Unit's "
   "determination and the Respondent's response of 18 February 2026 at Annexure A, Tab 27, or "
   "carried into a further notice to admit.]", NOTE),
 P("<b>B5A. The distribution lists</b>", SEC),
 P("12B. &nbsp;The recipients of the relevant communications are admitted. The Appellant's email of "
   "15 May 2024 went to the manager and to Logan Switch, copied to the Switchboard staff, the "
   "Director and LBH_HR. The Director's reply that evening was copied to the manager and marked of "
   "High importance. The manager's email of 17 May 2024 went to Logan Switch, copied to the "
   "Director and the Switchboard staff, and included Mr Richard Parry, as did the on-call roster "
   "email of 13 May 2024. These facts are pleaded as to the distribution of departmental "
   "communications and the consultation obligation at paragraph 8, and for no other purpose.", PLD)]
s += q([74, 76, 81, 111, 112, 113])
s += [P("13. &nbsp;On 15 May 2024 the Appellant asked that directives and changes be made in "
   "consultation and asked for the manager's office hours. He was asked that evening to retract "
   "that email. Two days later the office hours were sent to the whole department. On 21 May he was "
   "asked which particular changes or directives had concerned him.", PLD)]
s += q([74, 75, 76, 77, 78, 79, 80])
s += [P("14. &nbsp;In February 2024 a special pandemic leave application was submitted three times "
   "and declined twice before being approved on the same material.", PLD)]
s += q(list(range(114, 143)))

s += [P("<b>B6. What the employer states about its own systems</b>", SEC),
 P("15. &nbsp;By letter of 5 June 2026 to the Commission, Metro South Hospital and Health Service "
   "stated that the fatigue risk management records do not exist, that the mandatory training "
   "applies only to health practitioners and clinical assistants, that fatigue risk management "
   "assessment at the Switchboard was implemented only after 30 June 2024, that there had been no "
   "consequential changes to operating procedures over the period, and that employee complaints "
   "are made to the line manager and \"managed solely via email or verbally with the complainant\".", PLD)]
s += q(list(range(263, 273)))

s += [P("PART C &ndash; STRESSOR 2: REMUNERATION", PART),
 P("16. &nbsp;Between February and May 2024 the Appellant's pay required correction. On 3 May 2024 "
   "Payroll identified four fortnights and asked the manager to submit an Attendance Variation and "
   "Allowance Claim for each. On 13 May Payroll directed the Appellant to his line manager. On "
   "21 May the manager was awaiting payroll confirmation. On 28 May the Appellant was asked to sign "
   "a validation of claims older than three months. The correction could be submitted only by the "
   "manager, and the myHR submissions report records her as the initiator of each of the five such "
   "claims in the period and the Appellant as the initiator of none.", PLD)]
s += q(list(range(182, 207)))
s += [P("17. &nbsp;The Respondent pleads that any discrepancies were remedied in a timely manner "
   "and that there are no outstanding underpayments. The myHR submissions report records the claim "
   "submitted on 28 May 2024 with a status of \"Part Completed\", and neither of the two claim "
   "reference numbers identified by Payroll on 3 May 2024 appears in that report at all.", PLD)]
s += q([203, 204, 207, 208, 209, 210])

s += [P("PART D &ndash; STRESSOR 3: THE ROSTER AND FATIGUE", PART),
 P("18. &nbsp;Rostering errors on the Appellant's line were acknowledged by the Director in "
   "writing. On 10 May 2024 she wrote to Human Resources that the Appellant's roster would not be "
   "considered and that he was not yet aware of it. On 21 May she asked him to identify the changes "
   "and directives about which he had concerns.", PLD)]
s += q(list(range(211, 224)) + [80])
s += [P("19. &nbsp;The Appellant worked consecutive shifts on 17 and 18 March 2024 separated by a "
   "seven-hour break. The 8-hour agreement of 17 June 2020 applies only where staff-initiated shift "
   "swaps have occurred, and the Respondent does not allege these shifts arose from such a swap.", PLD)]
s += q(list(range(17, 26)) + list(range(224, 228)))
s += [P("20. &nbsp;The emergency workload carried on those two shifts is recorded in the employer's "
   "own register. The Respondent has not admitted those paragraphs and has given no reason. Metro "
   "South Health has stated in writing that a spreadsheet of recorded MET calls is available for "
   "that period.", PLD)]
s += q([228, 229, 230, 231])
s += [P("[TO BE ADMITTED &mdash; the four paragraphs above are the 2024 Emergency Code Register, a "
   "Metro South Hospital and Health Service workbook kept at Logan Hospital Switchboard, produced "
   "at Tab 31. They were not admitted on 8 September 2026 and no reason was given; the authenticity "
   "of Tab 31 is disputed on the Form 25 while the contents of the other tabs are admitted. "
   "Production was requested of the Respondent on 9 September 2026; the reply of 10 September 2026 "
   "seeks until 25 September 2026. Paragraph 268 above is the employer's own statement that the "
   "record is available.]", NOTE)]
s += [P("21. &nbsp;On 8 April 2024 the Appellant requested a review of payment and raised fatigue. "
   "The enquiry was escalated to Human Resources on 9 April. No response is alleged between 9 April "
   "and 1 May, an interval of 23 days, when the payment was refused.", PLD)]
s += q(list(range(242, 257)))
s += [P("22. &nbsp;The Respondent's own review decision of 24 October 2024 makes the following "
   "findings.", PLD)]
s += q(list(range(257, 263)))

s += [P("PART E &ndash; CONTENTIONS", PART),
 P("23. &nbsp;<b>Section 32(1).</b> The Respondent's own review decision finds that the Appellant "
   "sustained a personal injury of a psychological nature, that it arose out of employment, and "
   "that employment was <b>a significant contributing factor</b>. Those findings are admitted at "
   "paragraphs 261 and 262.", PLD),
 P("24. &nbsp;<b>Section 32(5)(a), first limb &mdash; the matters at B1 to B3 are not management "
   "action.</b> A directory an operator is required to keep accurate but cannot correct; emergency "
   "notifications reaching the wrong team; a clinical service unable to assist patients because a "
   "directory entry is wrong &mdash; these are the conditions in which the work was carried on. "
   "They are not action taken by the employer against the worker. One decision was taken, on "
   "18 July 2023, for a stated project reason. What followed is a state of the system, and "
   "subsection (5) does not reach it.", PLD),
 P("25. &nbsp;<b>Section 32(5)(a), second limb &mdash; where the matters pleaded are management "
   "action, it was not taken in a reasonable way.</b> The change of 15 April 2024 was effective the "
   "day it was notified, with no record of prior consultation, against an instrument requiring a "
   "genuine opportunity to influence the outcome before a final decision. The remuneration "
   "correction was returned to the only person able to make it across four fortnights and is "
   "recorded as Part Completed. The fatigue enquiry drew no response for 23 days. On the employer's "
   "own statements, no assessment, investigation or consequential change followed any complaint "
   "before 30 June 2024.", PLD),
 P("26. &nbsp;<b>Delaney.</b> A global evaluation is an evaluation of management actions. It "
   "cannot absorb a causative factor that is not management action, and the presence of reasonable "
   "management action among the causes does not exclude an injury to which a non-excluded factor "
   "was a significant contributing factor.", PLD),
 P("27. &nbsp;<b>Mahaffey.</b> A single unreasonable stressor suffices. The rostering of the shifts "
   "of 17 and 18 March 2024 is found by the Respondent's own decision to have amounted to "
   "unreasonable management action.", PLD),
 P("28. &nbsp;<b>The effect of the admissions.</b> By letter of 8 September 2026 the Respondent "
   "states that an admission of a document is \"an admission of the existence and wording of that "
   "document only\", and not of the truth of any statement, opinion or finding recorded in it, "
   "including any statement by a treating medical practitioner, any finding in Review Decision "
   "69983, or any statement by an officer of Metro South Hospital and Health Service. That "
   "qualification is accepted so far as it goes. It does not reach four classes of admitted fact "
   "relied on in this pleading: (i) facts as to what the Respondent's statement of facts and "
   "contentions does not allege; (ii) facts as to what the Respondent's List of Documents does not "
   "list; (iii) computed intervals of time; and (iv) the identity of the recipients of a "
   "communication. None of those involves the truth of a statement recorded in a document. The "
   "Respondent has not identified any admitted fact it contends is irrelevant.", PLD),
 P("29. &nbsp;<b>The hearing de novo.</b> The Respondent says that no finding in Review Decision "
   "69983 binds the Commission. That is accepted, and it applies to the whole of the decision. The "
   "conclusion under appeal is a conclusion of that decision, reached upon the findings recorded in "
   "it and set out at paragraphs 257 to 262 above.", PLD),
 P("30. &nbsp;<b>The Respondent's pleaded case.</b> Paragraph 27 of the amended statement of facts "
   "and contentions does not identify, by particular, date, document or cross-reference, the "
   "management action relied upon. The Respondent does not allege any disciplinary process, any "
   "formal performance management, or any communication described as a warning before 18 June 2024.", PLD)]
s += q([300, 301, 302, 303])

s += [P("PART F &ndash; SCHEDULES: EVERY ADMITTED PARAGRAPH, BY CATEGORY", PART),
 P("Every one of the 303 paragraphs is placed below. Numbers in <font color='#9b1c1c'>red</font> "
   "are not yet admitted.", KEY)]
CATS = [
 ("F1 &nbsp;The position and its duties", list(range(1, 17))),
 ("F2 &nbsp;Acts &ndash; the decisions taken, and the documents announcing them",
  list(range(39, 56)) + [66, 67, 273] + list(range(111, 114)) + list(range(162, 167))),
 ("F3 &nbsp;Emails &ndash; what arrived at the console, and what was sent from it",
  list(range(56, 66)) + [68] + list(range(70, 111))),
 ("F4 &nbsp;Delay &ndash; the measured intervals",
  [62, 63, 64, 69, 90, 92, 93, 97, 98, 102, 103, 124, 125, 213, 216, 249, 250]),
 ("F5 &nbsp;Contemporaneous documentation &ndash; what the Appellant wrote at the time",
  [74, 75, 78, 94, 95, 96, 214, 215] + list(range(274, 283))),
 ("F6 &nbsp;Reports and findings", list(range(257, 273))),
 ("F7 &nbsp;Remuneration", list(range(182, 211))),
 ("F8 &nbsp;Roster, the two shifts and fatigue",
  list(range(17, 26)) + list(range(211, 257))),
 ("F9 &nbsp;What was raised, and the Communication Book",
  list(range(26, 39)) + list(range(143, 162)) + list(range(167, 182))),
 ("F10 &nbsp;Special pandemic leave", list(range(114, 143))),
 ("F11 &nbsp;Work feedback &ndash; the four negatives", list(range(300, 304))),
 ("F12 &nbsp;Facts already admitted on 18 February 2026", list(range(283, 300))),
]
placed = set()
for title, ns in CATS:
    ns = [n for n in ns if 1 <= n <= 303]
    placed |= set(ns)
    cells = []
    for n in sorted(set(ns)):
        cells.append(f"<font color='#9b1c1c'><b>{n}</b></font>" if n in NOT_ADMITTED else str(n))
    s.append(P(f"<b>{title}</b> &nbsp;&nbsp;{', '.join(cells)}", SCH))
missing = sorted(set(range(1, 304)) - placed)
if missing:
    s.append(P(f"<b>F13 &nbsp;Not otherwise categorised</b> &nbsp;&nbsp;"
               f"{', '.join(str(n) for n in missing)}", SCH))

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=12*mm, bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(15*mm, 11*mm, A4[0]-30*mm, A4[1]-23*mm, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0)])])
doc.build(s); buf.seek(0)
pdf = pikepdf.open(buf)
n = len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "INTERNAL/2026-09-12_FORM9A_RESTRUCTURED_with_admissions_overlay.pdf"
pdf.save(out, linearize=True)
print(f"built {out} - {n} page(s); schedules place {len(placed)} of 303; uncategorised: {missing}")
