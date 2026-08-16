#!/usr/bin/env python3
"""WC/2024/227 — the covering email to the practice, and the internal pre-send checklist.

Two outputs:
  out/COVERING_EMAIL_to_practice.pdf   — goes to the practice. ⚠ Assume it is produced under the
                                          Notice of Non-Party Disclosure. Nothing strategic in it.
  out/PRE_SEND_CHECKLIST_internal.pdf  — ⛔ INTERNAL. Never leaves the file.
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
e.append(P("⚠ Assume this email is produced to the Regulator under the Notice of Non-Party "
           "Disclosure served on the practice. Nothing in it may be strategic.", SMALL))
e.append(Spacer(1, 4*mm))
e.append(P("<b>To:</b> Mind and Memory Service &nbsp;·&nbsp; <b>Attention:</b> Dr Ravikumar Bangalore "
           "Krishnaiah<br/><b>Subject:</b> Letter of instruction — psychiatric report — Cory Shepherd "
           "(DOB 11/01/1991)", SMALL))
e.append(Spacer(1, 4*mm))
e.append(P("Dear Dr Krishnaiah,", BODY))
e.append(P("I attach a letter of instruction for a report in my Queensland Industrial Relations "
           "Commission proceeding WC/2024/227, together with the five attachments it refers to and a "
           "copy of the Notice of Non-Party Disclosure served on your practice in that proceeding.", BODY))
e.append(P("<b>I am self-represented in this proceeding and have prepared the instruction myself.</b> "
           "I have set it out in the way I understand an expert is ordinarily instructed: the facts "
           "I ask you to assume are identified by their source, and the matters the Regulator does "
           "not accept are identified as well, so that you have the position complete rather than "
           "one side of it.", BODY))
e.append(P("The letter asks you to assume the facts recorded in Attachments 1 to 3 and 5, which are "
           "documents of the Workers' Compensation Regulator and of my employer. My own account of "
           "the workplace is "
           "provided as context only and is not the basis on which I ask you to reason.", BODY))
e.append(P("I understand the cost of the report is being met by Metro South Hospital and Health "
           "Service. <b>For completeness: the report is instructed by me, and I ask that it be "
           "addressed to me.</b> Could you please confirm the time you would require. If any part of "
           "the instruction is unclear, or if you require further material before you can report, "
           "please tell me and I will provide it.", BODY))
e.append(P("As the report is prepared for use in proceedings before the Commission and may be "
           "provided to my employer, I would be grateful if it could be issued without the standard "
           "restriction on medico-legal use that appears on correspondence from the practice.", BODY))
e.append(P("Kind regards,<br/><br/>Cory Lea Shepherd<br/>0417 400 227 · coryshepherd1@hotmail.com", BODY))
e.append(Spacer(1, 5*mm))
e.append(P("<b>Attached:</b> letter of instruction · schedule of assumed facts · Attachment 1 "
           "(Response of the Workers' Compensation Regulator, 18 February 2026) · Attachment 2 (letter of the Chief Executive, Metro South Health, "
           "5 June 2026) · Attachment 3 (role description, Administration Officer, Switchboard "
           "Services) · Attachment 4 (clinical records) · Attachment 5 (approved changes to working "
           "hours, 2026) · Notice of Non-Party Disclosure, sealed "
           "4 July 2025.", SMALL))

doc = SimpleDocTemplate("out/COVERING_EMAIL_to_practice.pdf", pagesize=A4,
                        leftMargin=22*mm, rightMargin=22*mm, topMargin=18*mm, bottomMargin=18*mm,
                        title="WC/2024/227 — covering email to the practice",
                        author="Cory Lea Shepherd")
doc.build(e)
print("built out/COVERING_EMAIL_to_practice.pdf")

# ─────────────────────────────────────── 2. PRE-SEND CHECKLIST (INTERNAL)
c = []
c.append(P("PRE-SEND CHECKLIST — the psychiatric instruction", H1))
c.append(P("⛔⛔ <b>INTERNAL. This never goes to the practice, to the employer or to the Regulator, "
           "and it is not in the pack.</b> Everything else built for this is written to be "
           "produced; this is not. Rewritten and renumbered 16 August 2026.", WARN))

c.append(P("A · BEFORE THE INSTRUCTION IS SENT", SEC))
c.append(P("<b>1. Insert the date.</b> It is the only bracket left in the letter.", ITEM))
c.append(P("<b>2. ✅ Funding is closed</b> — Metro South Health contacted the practice directly and "
           "confirmed it will meet the cost. ⭐ Not a promise to Cory but a commitment to a third "
           "party, of which the practice holds the record. <b>Two follow-ups, and neither involves "
           "contacting MSH:</b> ⭐ <b>(a)</b> confirm the <b>figure</b> with the practice when "
           "booking — <i>“will meet the cost”</i> is not <i>“up to $X”</i>, and re-opening it with "
           "MSH invites a cap; ⭐⭐ <b>(b)</b> ask the practice one neutral question: <b>what has the "
           "Health Service provided to you, or asked of you?</b> If MSH framed a scope or sent its "
           "own questions, the doctor may think he is answering their brief. <b>The letter of "
           "instruction must be the only instruction</b> — and question 1.5 catches it either way.", ITEM))
c.append(P("<b>3. The practice footer.</b> The report of 13 February 2025 carries <i>“disclosed for "
           "Qsuper and not for medico-legal use”</i> on every page. ⛔ <b>If that appears on this "
           "report it is compromised on its face.</b> The covering email raises it; confirm it has "
           "been understood.", ITEM))
c.append(P("<b>4. ⭐⭐ SEQUENCE: serve the AO3 role description on the Regulator BEFORE the report is "
           "commissioned.</b> Her amended List of Documents has 52 items and no role description of "
           "any kind. If the report reasons from a document she has never seen, it surfaces through "
           "an expert instead of through disclosure. ⛔ <b>Serve the document, not its "
           "provenance</b> — no mention of the request for medical information, the exclusion, or "
           "31 July 2026.", ITEM))
c.append(P("<b>5. ⭐ The commencement date.</b> Question 1.3(g) says <i>“from 2019”</i>. <b>Have a "
           "document for it</b> — first payslip, letter of appointment, or service record — before "
           "it is relied on in the appeal.", ITEM))

c.append(P("B · WHEN THE DRAFT ARRIVES — FACTS ONLY", SEC))
c.append(P("<b>6. ⛔⛔ THE REVIEW IS FACTS ONLY.</b> Part D promises it and the promise is the "
           "protection. <b>Do not comment on any opinion, do not suggest a conclusion, do not ask "
           "for anything to be strengthened.</b> Check: dates · names · which document said what · "
           "attachment references.", ITEM))
c.append(P("<b>7. ⛔⛔ THE PREPARATION AS A SYMPTOM — the first thing to look for.</b> His report of "
           "13 February 2025 lists, <b>under symptoms</b>: <i>“obsessive rumination, fear driven "
           "thoughts, <b>extensive researching, and planning on fact findings for work-related "
           "issues including reading up on policies, procedures, and legislations</b>”</i>, and "
           "records that the proceedings <i>“have consumed his whole life severely affecting his "
           "functioning.”</i> ⇒ ⭐⭐⭐ <b>A seven-page instruction, a schedule and five attachments, "
           "prepared by the patient, is on its face the behaviour he already coded as pathology.</b> "
           "Watch for any sentence treating the preparation of the case as a symptom, or the "
           "litigation as the barrier to return. <b>It is an incapacity marker, it is usable by the "
           "employer, and s 32(5)(c) excludes injury from action taken in connection with the "
           "compensation application.</b> ⭐ The covering email now states he is self-represented and "
           "prepared the instruction himself.", ITEM))
c.append(P("<b>8. ⛔ “AGGRAVATING” MUST NOT BE USED OF THE APPEAL OR THE EMPLOYMENT PROCESS.</b> "
           "<i>Aggravation</i> is statutory: s 32 makes it a compensable injury in its own right, "
           "and <b>s 32(5)(c) then excludes it</b>. In the capacity process the same word reads as "
           "<b>deterioration</b>. ⭐ The correct register is <b>“perpetuating”</b> or "
           "<b>“maintaining”</b> — persistence, not worsening, and it does not compete with "
           "causation of onset.", ITEM))
c.append(P("<b>9. ⭐⭐⭐ PROTECT THE SLEEP STRAND.</b> Sleep runs the length of the case and it runs "
           "from <b>shift work</b>: <b>16 Nov 2023</b> <i>“Poor sleep. Shift work. Cannot work/ do "
           "shifts if he does not get a good sleep”</i> → the 7-hour break → <b>3 Jul 2026</b> "
           "<i>“maintaining a regular sleep routine remains central to symptom management.”</i> "
           "⛔ <b>Any sentence attributing current sleep disturbance to the appeal cuts that thread "
           "at its strongest point.</b>", ITEM))
c.append(P("<b>10. THE FIVE POSITIVE CHECKS.</b> Does it <b>list every document reviewed</b> "
           "(1.5 — the Review Decision safeguard) · <b>state which Part B sources</b> the causation "
           "opinion rests on (Part D(d)) · <b>answer under the letter's numbering</b> (Part D(a)) · "
           "avoid <i>“unfair dismissal”</i> and <i>“bullying”</i> — his own 2025 register · and "
           "avoid the practice footer.", ITEM))
c.append(P("<b>11. ⚠ WHAT IS RAISABLE AND WHAT IS NOT.</b> Terminology and factual error are "
           "raisable — <i>“aggravating”</i>, a wrong date, a misattributed document. ⛔ <b>Anything "
           "that is opinion is not</b>, unless it misstates the record. <b>The line in Part D is the "
           "line.</b>", ITEM))

c.append(P("C · STANDING DISCIPLINES", SEC))
c.append(P("<b>12. ⛔ Say nothing about which exhibit holds what, or about the span of the "
           "production.</b> The letter and the schedule state only what the Regulator asserts — a "
           "history from 26 October 2022 — and nothing about what the file does or does not contain. "
           "<b>Do not add it back in correspondence.</b> It is their assertion to prove.", ITEM))
c.append(P("<b>13. ⚠ Assume everything sent to the practice is produced to the Regulator</b> under "
           "the notice it holds. That is why the instruction and the covering email carry no "
           "strategy and no characterisations.", ITEM))
c.append(P("<b>14. ⛔ The employer-facing material goes in the covering note, not to the "
           "clinician:</b> QH-POL-210's whole-organisation test and onus · that the Director who "
           "asks about <i>“restrictions or modifications”</i> approved three · that Item 3(a) "
           "explains why the Health Service is <i>“not aware of any concerns”</i> · the September "
           "2025 conduct/July 2026 medical asymmetry.", ITEM))
c.append(P("<b>15. WHAT THE REPORT MUST NOT DO.</b> ⛔ Say he cannot fulfil the inherent "
           "requirements · answer the accommodation question in the negative · opine on working with "
           "any named person or reporting line · express any view on whether management action was "
           "reasonable · attribute the injury to a course of management conduct generally rather "
           "than to the rostering and fatigue strand specifically.", ITEM))

c.append(P("D · STILL OUTSTANDING", SEC))
c.append(P("<b>16. ✅ The three movement forms are IN</b> — Attachment 5, stitched with an index "
           "page. Nothing further needed.", ITEM))
c.append(P("<b>17. ⭐ The April 2025 individual monthly statistics</b> — 269 to 444 calls per shift "
           "at about 29% of full time. They answer <i>“he kept working for fourteen months”</i>, "
           "which the capability checklist does not reach.", ITEM))
c.append(P("<b>18. ⚠ Who is performing the duties, which shifts, from when</b> — in writing. "
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
