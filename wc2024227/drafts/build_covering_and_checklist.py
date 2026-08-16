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
c.append(P("⛔⛔ <b>INTERNAL. This page never goes to the practice, to the employer, or to the "
           "Regulator.</b> Everything else in the pack is written to be produced; this is not.", WARN))

c.append(P("BEFORE ANYTHING IS SENT", SEC))
c.append(P("<b>0. ⭐⭐⭐ THE DRAFT.</b> Part D asks to be provided with a draft to identify factual "
           "error. <b>When it arrives, the review is FACTS ONLY.</b> ⛔ Do not comment on any "
           "opinion, do not suggest a conclusion, do not ask for anything to be strengthened — "
           "the letter promises it and the promise is the protection. Check: dates · names · which "
           "document said what · attachment references · whether every document reviewed is listed "
           "· whether it states which Part B sources the causation opinion rests on · whether it "
           "uses <i>“unfair dismissal”</i> or <i>“bullying”</i> · whether the <i>“not for "
           "medico-legal use”</i> footer appears.", ITEM))
c.append(P("<b>1. ✅ FUNDING IS CLOSED — MSH contacted the practice directly and confirmed it will "
           "meet the cost.</b> ⭐ That is the strongest form it could take: not a promise to Cory "
           "but a commitment made directly to a third party, of which the practice holds the "
           "record. Two small follow-ups remain, and <b>neither involves contacting MSH</b>:<br/>"
           "⭐ <b>(a) The quantum.</b> <i>“Will meet the cost”</i> is not <i>“will meet the cost up "
           "to $X”</i>. Confirm the practice's figure with the practice when booking. The "
           "PsychGroup benchmark on file is $10,000–$30,000 for a full medico-legal report; this "
           "instruction asks a narrower question and should be priced well below it.<br/>"
           "⭐⭐ <b>(b) What ELSE did the Health Service say to the practice?</b> If it framed a "
           "scope, or sent its own questions, the doctor may believe he is answering MSH's brief "
           "rather than this instruction. <b>Ask the practice one neutral question when booking: "
           "what has the Health Service provided to you, or asked of you?</b> ⛔ The letter of "
           "instruction must be the only instruction. ⭐ And question 1.5 catches it either way — "
           "anything MSH sent will appear in the list of documents reviewed.", ITEM))
c.append(P("<b>1a. ⛔⛔ THE ONE THING TO WATCH FOR ON THE DRAFT — HIS OWN 2025 REPORT CODED THE "
           "PREPARATION AS A SYMPTOM.</b> The report of 13 February 2025 lists, <b>under "
           "symptoms</b>: <i>“obsessive rumination, fear driven thoughts, <b>extensive researching, "
           "and planning on fact findings for work-related issues including reading up on policies, "
           "procedures, and legislations</b>”</i>, and records that the proceedings <i>“have "
           "consumed his whole life severely affecting his functioning.”</i><br/>"
           "⇒ ⭐⭐⭐ <b>A seven-page forensic instruction, a schedule of assumed facts and five "
           "attachments, prepared personally by the patient, is on its face the very behaviour that "
           "clinician has already recorded as pathology.</b> ⚠ Watch for any sentence in the new "
           "report that treats the preparation of the case as a symptom, or the litigation as the "
           "barrier to return. <b>It is an incapacity marker, it is directly usable by the "
           "employer, and s 32(5)(c) excludes injury from action taken in connection with the "
           "compensation application.</b> ⭐ The covering email now states that he is "
           "self-represented and prepared the instruction himself, which explains the authorship as "
           "a necessity of his position rather than as a symptom.", ITEM))
c.append(P("<b>2. The practice footer.</b> The report of 13 February 2025 carries "
           "<i>“disclosed for Qsuper and not for medico-legal use”</i> on every page. ⛔ <b>If that "
           "appears on this report it is compromised on its face.</b> The covering email raises it; "
           "confirm it has been understood.", ITEM))
c.append(P("<b>3. Insert the date</b> in the instruction where marked.", ITEM))
c.append(P("<b>4. ⭐⭐ The commencement date at question 1.3(c) is now <i>“since 2019”</i></b> — "
           "more than five years of continuous shift work before the pleaded onset. ⚠ <b>Have a "
           "document for it</b> (first payslip, letter of appointment, or service record) before "
           "the answer is relied on in the appeal. ⛔ <b>The casual-to-full-time change stays out "
           "of the letter</b> — it is a contractual question, not a clinical one, and it has "
           "already been run and answered.", ITEM))
c.append(P("<b>5. ✅ The capacity wording is VERIFIED and locked</b> — read from the Employee "
           "Capability Checklist of 3 July 2026. ⛔ The old paraphrase <i>“continuation of existing "
           "arrangement”</i> <b>does not appear in the document</b> and has been removed everywhere. "
           "The correct words are <i>“approximately <b>six shifts per fortnight</b> … the pattern "
           "Mr Shepherd <b>has in fact worked and tolerated over the past twelve months without "
           "deterioration</b> … <b>Usual switchboard operational duties remain suitable</b>.”</i>",
           ITEM))
c.append(P("<b>6. ⛔ Say nothing about which exhibit holds what, or about the span of the "
           "production.</b> The letter and the schedule state only what the respondent asserts — a "
           "history from 26 October 2022 — and nothing about what the file does or does not "
           "contain. <b>Do not add it back in correspondence.</b> It is their assertion to prove.", ITEM))

c.append(P("STILL MISSING FROM THE PACK — AND WHY IT MATTERS", SEC))
c.append(P("<b>7. ✅ The three movement forms are IN the pack</b> — Attachment 5, stitched with an "
           "index page: 27.02.2026 · 17.04.2026 · 09.06.2026, delegate-approved, 56/56/40 hours "
           "against a 76-hour fortnight, <b>each recording “Continuous Shift Worker”</b>. ⭐⭐⭐ <b>The "
           "delegate on all three is Scott Hughes — who signed the request of 31 July 2026 asking "
           "whether Mr Shepherd can fulfil the inherent requirements “without restrictions or "
           "modifications to duties”.</b> ⛔ That point is NOT put to the clinician. It belongs in "
           "the covering note to the employer and in the employment track.", ITEM))
c.append(P("<b>8. ⭐ The April 2025 individual monthly statistics</b> — 269 to 444 calls per shift at "
           "about 29% of full time. Without them the clinician cannot address why reduced hours did "
           "not reduce intensity, and <i>“he kept working for fourteen months”</i> goes unanswered.", ITEM))
c.append(P("<b>9. ⚠ Who is performing the duties, which shifts, from when</b> — in writing. Currently "
           "colleague report only. Load-bearing for 3.6 and for the employer's accommodation "
           "question.", ITEM))

c.append(P("SEQUENCING", SEC))
c.append(P("<b>10. ⭐⭐ Serve the AO3 role description on the Regulator as continuing disclosure "
           "BEFORE the report is commissioned.</b> She does not hold it — the amended List of "
           "Documents has 52 items and no role description of any kind. If the report relies on a "
           "document she has never seen, it surfaces through an expert rather than through "
           "disclosure. ⛔ <b>Serve the document, not its provenance:</b> no mention of the request "
           "for medical information, the exclusion, or 31 July 2026.", ITEM))
c.append(P("<b>11. ⚠ Assume everything sent to the practice is produced to the Regulator</b> under the "
           "notice it holds. That is why the instruction and the covering email carry no strategy, no "
           "characterisations, and nothing from the parallel tracks.", ITEM))

c.append(P("⭐⭐⭐ WHEN THE REPORT GOES TO MSH — CITE THEIR OWN POLICY", SEC))
c.append(P("The adjustments the report specifies are measured against <b>HR Policy G3 / QH-POL-210, "
           "Reasonable Adjustment</b>, which MSH itself invoked in the request of 31 July 2026. "
           "⭐ <b>Its own words, verified:</b>", ITEM))
c.append(P("<i>“The question of whether an adjustment is unreasonable or would cause "
           "&lsquo;unjustifiable hardship&rsquo; is <b>tested against the whole organisation, not a "
           "division or unit within the organisation</b>. <b>The onus is on Queensland Health, as the "
           "employer, to prove an adjustment is unreasonable</b>, not on the person to prove that it "
           "is reasonable.”</i>", ITEM))
c.append(P("⇒ ⭐⭐⭐ <b>The test is not whether the Logan Switchboard roster can absorb the "
           "adjustment. It is whether Metro South Health can — and the onus of showing it cannot is "
           "theirs.</b> The same policy adds that failure to provide reasonable adjustment <i>“may "
           "constitute unlawful discrimination.”</i>", ITEM))
c.append(P("⛔ <b>This goes in the covering note to MSH, not to the clinician.</b> A psychiatrist does "
           "not apply an HR policy. Question 3.6(c) is framed so that his answer — whether adjustments "
           "of that kind are ordinarily provided by large employers and by 24-hour health services — "
           "maps onto the whole-organisation test without his being asked to apply it.", ITEM))

c.append(P("WHAT THE REPORT MUST NOT DO", SEC))
c.append(P("⛔ Say he cannot fulfil the inherent requirements · ⛔ answer the accommodation question "
           "in the negative · ⛔ opine on working with any named person or reporting line · ⛔ express "
           "any view on whether management action was reasonable · ⛔ attribute the injury to a course "
           "of management conduct generally rather than to the rostering and fatigue strand "
           "specifically.", BODY))

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
