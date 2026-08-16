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
           "Commission proceeding WC/2024/227, together with the four attachments it refers to and a "
           "copy of the Notice of Non-Party Disclosure served on your practice in that proceeding.", BODY))
e.append(P("The letter asks you to assume the facts recorded in Attachments 1 to 3, which are "
           "documents of the respondent and of my employer. My own account of the workplace is "
           "provided as context only and is not the basis on which I ask you to reason.", BODY))
e.append(P("Could you please confirm your fee for the report and the time you would require. If any "
           "part of the instruction is unclear, or if you require further material before you can "
           "report, please tell me and I will provide it.", BODY))
e.append(P("As the report is prepared for use in proceedings before the Commission and may be "
           "provided to my employer, I would be grateful if it could be issued without the standard "
           "restriction on medico-legal use that appears on correspondence from the practice.", BODY))
e.append(P("Kind regards,<br/><br/>Cory Lea Shepherd<br/>0417 400 227 · coryshepherd1@hotmail.com", BODY))
e.append(Spacer(1, 5*mm))
e.append(P("<b>Attached:</b> letter of instruction · Attachment 1 (Response to Notice to Admit Facts, "
           "18 February 2026) · Attachment 2 (letter of the Chief Executive, Metro South Health, "
           "5 June 2026) · Attachment 3 (role description, Administration Officer, Switchboard "
           "Services) · Attachment 4 (clinical records) · Notice of Non-Party Disclosure, sealed "
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
c.append(P("<b>1. Was Review Decision 69983 put in front of him on 12 August 2026?</b><br/>"
           "⭐ If <b>no</b> — send as it stands.<br/>"
           "⛔ If <b>yes</b> — two lines must be added to the instruction before sending: an express "
           "direction not to adopt any finding, characterisation or conclusion in it; and a question "
           "whether his opinion would differ if he disregarded it entirely. <b>Unaddressed, it is "
           "the first thing an opposing expert will find.</b>", ITEM))
c.append(P("<b>2. The fee.</b> Confirm before instructing. The covering email asks for it. The "
           "benchmark on file is the PsychGroup indicative range of $10,000–$30,000 for a full "
           "medico-legal report; ⭐ <b>this instruction asks a narrower question than that</b>, and "
           "should be priced accordingly.", ITEM))
c.append(P("<b>3. The practice footer.</b> The report of 13 February 2025 carries "
           "<i>“disclosed for Qsuper and not for medico-legal use”</i> on every page. ⛔ <b>If that "
           "appears on this report it is compromised on its face.</b> The covering email raises it; "
           "confirm it has been understood.", ITEM))
c.append(P("<b>4. Insert the date</b> in the instruction where marked.", ITEM))

c.append(P("STILL MISSING FROM THE PACK — AND WHY IT MATTERS", SEC))
c.append(P("<b>5. ⭐⭐ The three movement forms</b> — reduced hours approved by the Director on "
           "27.02.2026, 17.04.2026 and 09.06.2026. <b>Without them, question 3.6 (inherent "
           "requirements) cannot be answered safely</b>, because the role description makes 24/7 shift "
           "work mandatory. They are the employer's own documents and they prove the adjustment was "
           "granted three times and operated.", ITEM))
c.append(P("<b>6. ⭐ The April 2025 individual monthly statistics</b> — 269 to 444 calls per shift at "
           "about 29% of full time. Without them the clinician cannot address why reduced hours did "
           "not reduce intensity, and <i>“he kept working for fourteen months”</i> goes unanswered.", ITEM))
c.append(P("<b>7. ⚠ Who is performing the duties, which shifts, from when</b> — in writing. Currently "
           "colleague report only. Load-bearing for 3.6 and for the employer's accommodation "
           "question.", ITEM))

c.append(P("SEQUENCING", SEC))
c.append(P("<b>8. ⭐⭐ Serve the AO3 role description on the Regulator as continuing disclosure "
           "BEFORE the report is commissioned.</b> She does not hold it — the amended List of "
           "Documents has 52 items and no role description of any kind. If the report relies on a "
           "document she has never seen, it surfaces through an expert rather than through "
           "disclosure. ⛔ <b>Serve the document, not its provenance:</b> no mention of the request "
           "for medical information, the exclusion, or 31 July 2026.", ITEM))
c.append(P("<b>9. ⚠ Assume everything sent to the practice is produced to the Regulator</b> under the "
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
