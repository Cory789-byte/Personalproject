#!/usr/bin/env python3
"""WC/2024/227 — the covering email to the practice, and the internal pre-send checklist.

Two outputs:
  out/COVERING_EMAIL_to_practice.pdf   — ⛔ A TEMPLATE TO TYPE FROM. It is NOT attached and is NOT
                                          in the pack (17 Aug). The page opens with a production
                                          note addressed to Cory — "assume this is produced to the
                                          Regulator; nothing in it may be strategic" — and if the
                                          practice filed the PDF, Ms Matheson would read that note
                                          with it. The BODY of the email is sent as written,
                                          including the Metro South 31 July subject line. ⚠ Assume
                                          the typed email is produced under the Notice of Non-Party
                                          Disclosure. Nothing strategic in it.
  out/PRE_SEND_CHECKLIST_internal.pdf  — ⛔ INTERNAL. Never leaves the file.

⭐ 17 AUGUST — NO DRAFT IS REQUESTED. The letter of instruction previously offered to review a
draft on the facts. That paragraph is struck: offering a draft still looks like a chance to shape
the report. If a fact in the report is wrong, it is corrected by writing to Dr Krishnaiah after it
issues. Section B of the checklist is written for the report as issued, not for a draft.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=12.5, leading=16, spaceAfter=4)
SEC = ParagraphStyle('SEC', parent=ss['Heading2'], fontName='Helvetica-Bold',
                     fontSize=10.4, leading=13.5, spaceBefore=11, spaceAfter=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=10, leading=14, spaceAfter=8)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.4, leading=11.4,
                       textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=9, leading=12.5,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=6)
ITEM = ParagraphStyle('ITEM', parent=BODY, spaceBefore=6, spaceAfter=3, leftIndent=6)

def P(t, s=BODY): return Paragraph(t, s)

# ─────────────────────────────────────── 1. COVERING EMAIL
e = []
e.append(P("Covering email — to the practice", H1))
e.append(P("TYPE THIS INTO THE EMAIL. THIS PDF IS NOT AN ATTACHMENT AND IS NOT IN THE PACK. "
           "The line below is a note to Cory, not to the practice: if the PDF were attached and "
           "the practice filed it, the Regulator would read the note along with the email.", WARN))
e.append(P("Assume this email is produced to the Regulator under the Notice of Non-Party "
           "Disclosure served on the practice. Nothing in it may be strategic.", SMALL))
e.append(Spacer(1, 4*mm))
e.append(P("<b>To:</b> Mind and Memory Service &nbsp;·&nbsp; <b>Attention:</b> Dr Ravikumar Bangalore "
           "Krishnaiah<br/><b>Subject:</b> Request for medical information, Metro South Health, 31 July "
           "2026 — instruction for report — Cory Shepherd "
           "(DOB 11/01/1991)", SMALL))
e.append(Spacer(1, 4*mm))
e.append(P("Dear Dr Krishnaiah,", BODY))
e.append(P("On 31 July 2026 Metro South Hospital and Health Service asked for medical information "
           "about my condition and my capacity for work. That request is signed by Mr Scott Hughes, "
           "Director, Corporate Services. I attach a letter of instruction for one report answering "
           "that request.", BODY))
e.append(P("The report is also to answer the three matters written on the Form 29 Notice of "
           "Non-Party Disclosure served on your practice. That notice is signed by Ms Renee "
           "Matheson, Senior Appeals Officer, Workers' Compensation Regulator, and was sealed on "
           "4 July 2025.", BODY))
e.append(P("I ask you to reason from the documents attached, and not from my account of the "
           "workplace. Those documents are:", BODY))
e.append(P("Attachment 1 — the notice to admit facts (Form 24) and the Regulator's response to it, "
           "signed by Ms Renee Matheson on 18 February 2026;<br/>"
           "Attachment 2 — the letter of Ms Noelle Cridland, Chief Executive, Metro South Hospital "
           "and Health Service, 5 June 2026;<br/>"
           "Attachment 3 — the role description for Administration Officer, Switchboard Services;<br/>"
           "Attachment 5 — the movement forms approved by Mr Scott Hughes;<br/>"
           "Attachment 6 — the Form 29 signed by Ms Matheson; and<br/>"
           "Attachment 7 — the request and nine-question schedule signed by Mr Hughes on "
           "31 July 2026.", BODY))
e.append(P("Attachment 4 is the clinical record. Attachments 6 and 7 state the questions the report "
           "answers. None of those three is assumed fact. My own account of the workplace is "
           "context only.", BODY))
e.append(P("The facts I ask you to assume are identified by source in the enclosed schedule. What "
           "the Regulator does not accept is identified there as well.", BODY))
e.append(P("I am self-represented. Metro South Hospital and Health Service is meeting the cost of "
           "the report. The report is instructed by me and is to be provided to me on completion, "
           "prepared as a standalone report in the form the letter of instruction describes. The "
           "same report will be given to the Regulator and to Metro South Hospital and Health "
           "Service on the same day.", BODY))
e.append(P("Please confirm the time you would require. If any part of the instruction is unclear, "
           "or if you need further material, please tell me.", BODY))
e.append(P("As the report may be used in the Commission and provided to my employer, I would be "
           "grateful if it could be issued without the standard restriction on medico-legal use.", BODY))
e.append(P("Kind regards,<br/><br/>Cory Lea Shepherd<br/>0417 400 227 · coryshepherd1@hotmail.com", BODY))
e.append(Spacer(1, 5*mm))
e.append(P("<b>The twelve attachments</b> (the pack — this covering email is typed, not attached): "
           "letter of instruction · schedule of assumed facts · Attachment 1 (notice to admit facts "
           "and the Regulator's response, 18 February 2026) · Attachment 2 (letter of the Chief "
           "Executive, 5 June 2026) · Attachment 3 (role description) · Attachment 4 in four files "
           "(GP records · Hawes certificate 8 September 2024 · capability checklist 3 July 2026 · "
           "your report 13 February 2025) · Attachment 5 (movement forms, 2026) · Attachment 6 "
           "(Form 29, sealed 4 July 2025) · Attachment 7 (request for medical information, "
           "31 July 2026).", SMALL))

doc = SimpleDocTemplate("out/COVERING_EMAIL_to_practice.pdf", pagesize=A4,
                        leftMargin=22*mm, rightMargin=22*mm, topMargin=18*mm, bottomMargin=18*mm,
                        title="WC/2024/227 — covering email to the practice",
                        author="Cory Lea Shepherd")
doc.build(e)
print("built out/COVERING_EMAIL_to_practice.pdf")

# ─────────────────────────────────────── 2. PRE-SEND CHECKLIST (INTERNAL)
c = []
c.append(P("PRE-SEND CHECKLIST — the psychiatric instruction", H1))
c.append(P("<b>INTERNAL. This never goes to the practice, to the employer or to the Regulator, "
           "and it is not in the pack.</b> Everything else built for this is written to be "
           "produced; this is not. Rewritten and renumbered 16 August 2026; items 0 and 6 "
           "rewritten 17 August 2026.", WARN))

c.append(P("A · BEFORE THE INSTRUCTION IS SENT", SEC))
c.append(P("<b>0. TYPE THE COVERING EMAIL. DO NOT ATTACH IT.</b> "
           "<i>COVERING_EMAIL_to_practice.pdf</i> is a template to type from, and it is <b>not in "
           "the pack</b>. It opens with a production note — <i>“assume this email is produced to "
           "the Regulator under the Notice of Non-Party Disclosure; nothing in it may be "
           "strategic”</i> — which is a note to you. <b>If the practice files the PDF, Ms Matheson "
           "reads the note with it.</b> The body of the email goes as written, subject line "
           "included. Then check the attachment list against the pack before sending: <b>twelve "
           "files, and no covering email among them</b> — letter · schedule · Attachments 1, 2, 3 · "
           "the four Attachment 4 files · Attachment 5 · Attachment 6 (the sealed Form 29) · "
           "Attachment 7 (the 31 July request).", ITEM))
c.append(P("<b>1. Insert the date.</b> It is the only bracket left in the letter.", ITEM))
c.append(P("<b>2. Funding is closed</b> — Metro South Health contacted the practice directly and "
           "confirmed it will meet the cost. Not a promise to Cory but a commitment to a third "
           "party, of which the practice holds the record. <b>Two follow-ups, and neither involves "
           "contacting MSH:</b> <b>(a)</b> confirm the <b>figure</b> with the practice when "
           "booking — <i>“will meet the cost”</i> is not <i>“up to $X”</i>, and re-opening it with "
           "MSH invites a cap; <b>(b)</b> ask the practice one neutral question: <b>what has the "
           "Health Service provided to you, or asked of you?</b> If MSH framed a scope or sent its "
           "own questions, the doctor may think he is answering their brief. <b>The letter of "
           "instruction must be the only instruction</b> — and question 1.5 catches it either way.", ITEM))
c.append(P("<b>3. The practice footer.</b> The report of 13 February 2025 carries <i>“disclosed for "
           "Qsuper and not for medico-legal use”</i> on every page. <b>If that appears on this "
           "report it is compromised on its face.</b> The covering email raises it; confirm it has "
           "been understood.", ITEM))
c.append(P("<b>4. SEQUENCE: serve the AO3 role description on the Regulator BEFORE the report is "
           "commissioned.</b> Her amended List of Documents has 52 items and no role description of "
           "any kind. If the report reasons from a document she has never seen, it surfaces through "
           "an expert instead of through disclosure. <b>Serve the document, not its "
           "provenance</b> — no mention of the request for medical information, the exclusion, or "
           "31 July 2026.", ITEM))
c.append(P("<b>5. The commencement date.</b> Question 1.3(g) says <i>“from 2019”</i>. <b>Have a "
           "document for it</b> — first payslip, letter of appointment, or service record — before "
           "it is relied on in the appeal.", ITEM))

c.append(P("B · WHEN THE REPORT ARRIVES", SEC))
c.append(P("<b>6. NO DRAFT WAS REQUESTED — struck 17 August.</b> Offering to review a draft still "
           "looks like a chance to shape the report, so the report arrives issued. <b>If a fact in "
           "it is wrong — a date, a name, which document said what, an attachment reference — "
           "correct it by writing to Dr Krishnaiah after it issues, facts only, and keep the "
           "letter.</b> Do not comment on any opinion, do not suggest a conclusion, do not ask for "
           "anything to be strengthened.", ITEM))
c.append(P("<b>7. THE PREPARATION AS A SYMPTOM — the first thing to look for.</b> His report of "
           "13 February 2025 lists, <b>under symptoms</b>: <i>“obsessive rumination, fear driven "
           "thoughts, <b>extensive researching, and planning on fact findings for work-related "
           "issues including reading up on policies, procedures, and legislations</b>”</i>, and "
           "records that the proceedings <i>“have consumed his whole life severely affecting his "
           "functioning.”</i> ⇒ <b>A seven-page instruction, a schedule and seven attachments, "
           "prepared by the patient, is on its face the behaviour he already coded as pathology.</b> "
           "Watch for any sentence treating the preparation of the case as a symptom, or the "
           "litigation as the barrier to return. <b>It is an incapacity marker, it is usable by the "
           "employer, and s 32(5)(c) excludes injury from action taken in connection with the "
           "compensation application.</b> The covering email now states he is self-represented and "
           "prepared the instruction himself.", ITEM))
c.append(P("<b>8. “AGGRAVATING” MUST NOT BE USED OF THE APPEAL OR THE EMPLOYMENT PROCESS.</b> "
           "<i>Aggravation</i> is statutory: s 32 makes it a compensable injury in its own right, "
           "and <b>s 32(5)(c) then excludes it</b>. In the capacity process the same word reads as "
           "<b>deterioration</b>. The correct register is <b>“perpetuating”</b> or "
           "<b>“maintaining”</b> — persistence, not worsening, and it does not compete with "
           "causation of onset.", ITEM))
c.append(P("<b>9. PROTECT THE SLEEP STRAND.</b> Sleep runs the length of the case and it runs "
           "from <b>shift work</b>: <b>16 Nov 2023</b> <i>“Poor sleep. Shift work. Cannot work/ do "
           "shifts if he does not get a good sleep”</i> → the 7-hour break → <b>3 Jul 2026</b> "
           "<i>“maintaining a regular sleep routine remains central to symptom management.”</i> "
           "<b>Any sentence attributing current sleep disturbance to the appeal cuts that thread "
           "at its strongest point.</b>", ITEM))
c.append(P("<b>10. THE FIVE POSITIVE CHECKS.</b> Does it <b>list every document reviewed</b> "
           "(1.5 — the Review Decision safeguard) · <b>state which Part B sources</b> the causation "
           "opinion rests on (Part D(d)) · <b>answer under the letter's numbering</b> (Part D(a)) · "
           "avoid <i>“unfair dismissal”</i> and <i>“bullying”</i> — his own 2025 register · and "
           "avoid the practice footer.", ITEM))
c.append(P("<b>11. WHAT IS RAISABLE AND WHAT IS NOT.</b> Terminology and factual error are "
           "raisable — <i>“aggravating”</i>, a wrong date, a misattributed document. <b>Anything "
           "that is opinion is not</b>, unless it misstates the record.", ITEM))

c.append(P("C · STANDING DISCIPLINES", SEC))
c.append(P("<b>12. Say nothing about which exhibit holds what, or about the span of the "
           "production.</b> The letter and the schedule state only what the Regulator asserts — a "
           "history from 26 October 2022 — and nothing about what the file does or does not contain. "
           "<b>Do not add it back in correspondence.</b> It is their assertion to prove.", ITEM))
c.append(P("<b>13. Assume everything sent to the practice is produced to the Regulator</b> under "
           "the notice it holds. That is why the instruction and the covering email carry no "
           "strategy and no characterisations.", ITEM))
c.append(P("<b>14. The employer-facing material goes in the covering note, not to the "
           "clinician:</b> QH-POL-210's whole-organisation test and onus · that the Director who "
           "asks about <i>“restrictions or modifications”</i> approved three · that Item 3(a) "
           "explains why the Health Service is <i>“not aware of any concerns”</i> · the September "
           "2025 conduct/July 2026 medical asymmetry.", ITEM))
c.append(P("<b>15. WHAT THE REPORT MUST NOT DO.</b> Say he cannot fulfil the inherent "
           "requirements · answer the accommodation question in the negative · opine on working with "
           "any named person or reporting line · express any view on whether management action was "
           "reasonable · attribute the injury to a course of management conduct generally rather "
           "than to the rostering and fatigue strand specifically.", ITEM))

c.append(P("D · STILL OUTSTANDING", SEC))
c.append(P("<b>16. The three movement forms are IN</b> — Attachment 5, stitched with an index "
           "page. Nothing further needed.", ITEM))
c.append(P("<b>17. The April 2025 individual monthly statistics</b> — 269 to 444 calls per shift "
           "at about 29% of full time. They answer <i>“he kept working for fourteen months”</i>, "
           "which the capability checklist does not reach.", ITEM))
c.append(P("<b>18. Who is performing the duties, which shifts, from when</b> — in writing. "
           "Currently colleague report only.", ITEM))

doc2 = SimpleDocTemplate("out/PRE_SEND_CHECKLIST_internal.pdf", pagesize=A4,
                         leftMargin=20*mm, rightMargin=20*mm, topMargin=17*mm, bottomMargin=17*mm,
                         title="WC/2024/227 — pre-send checklist (internal)",
                         author="Internal working document")

def footer(canv, d):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7.4)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(20*mm, 10*mm, "INTERNAL — NOT FOR THE PRACTICE, THE EMPLOYER OR THE REGULATOR")
    canv.restoreState()

doc2.build(c, onFirstPage=footer, onLaterPages=footer)
print("built out/PRE_SEND_CHECKLIST_internal.pdf")
