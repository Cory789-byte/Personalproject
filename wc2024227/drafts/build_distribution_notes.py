#!/usr/bin/env python3
"""WC/2024/227 — THE TWO DISTRIBUTION NOTES, for the day the report lands.

Builds drafts/out/DISTRIBUTION_NOTES_report.pdf — both notes in one file, for review and copying.

⭐ CORY'S INSTRUCTION, 16 AUGUST: "the letter I give to both I am forth coming."
So both notes state the SAME FOUR FACTS on their face:
  1. what the report is, and who wrote it;
  2. that it answers BOTH the three matters in issue in the appeal AND the employer's request of
     31 July 2026;
  3. that the identical report has gone to the other recipient, the same day;
  4. that Metro South Health met the cost, and that the report was instructed by, and addressed
     to, Mr Shepherd.

⭐⭐⭐ THE NOTES ARE NOT IDENTICAL, AND THAT IS NOT CONCEALMENT — IT IS FUNCTION.
Disclosure carries no ask, so the Regulator's note asks for nothing. The employer's note must ask
for something, because a medical answer to a capacity request is useless unless it is acted on.
Neither recipient is told anything the other is not.

⭐⭐ AND THE LETTER OF INSTRUCTION AND SCHEDULE GO TO BOTH.
That is the forthcoming posture, and it is also the strongest available move: the instruction shows
on its face that the assumed facts are the Regulator's own accepted facts and the employer's own
documents — not Mr Shepherd's account. An expert report whose instruction is disclosed is worth far
more than one whose instruction is withheld and then demanded.

⛔ SEND SIMULTANEOUSLY. No sequencing inference is then available to anyone.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle)

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=13, leading=16.5, spaceAfter=3)
NOTE = ParagraphStyle('NOTE', parent=ss['Heading2'], fontName='Helvetica-Bold',
                      fontSize=11, leading=14, spaceBefore=10, spaceAfter=5,
                      borderPadding=4, backColor=colors.HexColor('#eeeeee'))
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=10, leading=14, spaceAfter=8)
NUM = ParagraphStyle('NUM', parent=BODY, leftIndent=14, spaceBefore=4, spaceAfter=4)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.4, leading=11.4,
                       textColor=colors.HexColor('#555555'))
INT = ParagraphStyle('INT', parent=BODY, fontSize=8.8, leading=12,
                     textColor=colors.HexColor('#7a2018'), leftIndent=6,
                     backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
def P(t, s=BODY): return Paragraph(t, s)

s = []
s.append(P("The two distribution notes — for the day the report is provided", H1))
s.append(P("WC/2024/227 · Shepherd · sent <b>simultaneously</b> · both enclose the report, the "
           "letter of instruction and the schedule of assumed facts", SMALL))
s.append(P("<b>INTERNAL HEADER ONLY — this page is not sent.</b> Each note below is sent as the "
           "body of its own email. Insert the report's date where marked. <b>Send both within the "
           "same minutes</b>: simultaneous provision leaves no sequencing inference available to "
           "anyone.", INT))

# ══════════════════════════════════════════ NOTE 1
s.append(P("NOTE 1 — TO THE WORKERS' COMPENSATION REGULATOR", NOTE))
s.append(P("<b>To:</b> Renee.Matheson@oir.qld.gov.au &nbsp;·&nbsp; <b>Cc:</b> the OIR appeals "
           "registry<br/><b>Subject:</b> WC/2024/227 — Shepherd — continuing disclosure — report of "
           "Dr R B Krishnaiah", SMALL))
s.append(Spacer(1, 3*mm))
s.append(P("Dear Ms Matheson,", BODY))
s.append(P("I enclose, by way of continuing disclosure, the report of <b>Dr Ravikumar Bangalore "
           "Krishnaiah, Consultant Psychiatrist, dated [DATE OF REPORT]</b>, together with my "
           "letter of instruction and the schedule of assumed facts provided with it.", BODY))
s.append(P("The report addresses the three matters in issue as stated in the Notice of Non-Party "
           "Disclosure served on the practice in this proceeding. It also answers the request for "
           "medical information made by my employer on 31 July 2026.", BODY))
s.append(P("<b>The same report has today been provided to Metro South Hospital and Health "
           "Service.</b> The cost of the report has been met by Metro South Hospital and Health "
           "Service; it was instructed by me and is addressed to me.", BODY))
s.append(P("Kind regards,<br/><br/>Cory Lea Shepherd<br/>Appellant, WC/2024/227", BODY))
s.append(P("<b>NOTHING FURTHER.</b> No argument, no commentary, no request, no explanation of "
           "what the report establishes. A report is evidence — it argues for itself, and "
           "anything added to it subtracts from it. This is disclosure, which is the one category "
           "of communication that carries no ask.", INT))

s.append(PageBreak())

# ══════════════════════════════════════════ NOTE 2
s.append(P("NOTE 2 — TO METRO SOUTH HOSPITAL AND HEALTH SERVICE", NOTE))
s.append(P("<b>To:</b> lbh_InjuryManagement@health.qld.gov.au &nbsp;·&nbsp; <b>Cc:</b> "
           "lbh_hr@health.qld.gov.au; Scott Hughes, Director Corporate Services<br/>"
           "<b>Subject:</b> Request for medical information, 31 July 2026 — response — Mr Cory "
           "Shepherd", SMALL))
s.append(Spacer(1, 3*mm))
s.append(P("Dear Ms Harrison,", BODY))
s.append(P("<b>1.</b> I enclose the report of <b>Dr Ravikumar Bangalore Krishnaiah, Consultant "
           "Psychiatrist, dated [DATE OF REPORT]</b>, in answer to the Health Service's request for "
           "medical information of 31 July 2026. I also enclose my letter of instruction and the "
           "schedule of assumed facts provided with it, so that the basis of the opinion is "
           "apparent.", NUM))
s.append(P("<b>2. Scope.</b> The report addresses the matters raised in the request. Where a "
           "question goes to workplace arrangements rather than to medical capacity, the report "
           "identifies it as such and says so rather than answering it. <b>If any clinical matter "
           "remains outstanding, please identify it and I will put it to Dr Krishnaiah.</b>", NUM))
s.append(P("<b>3. The framework the Health Service has invoked.</b> The request is made under HR "
           "Policy G3 / QH-POL-210, <i>Reasonable Adjustment</i>. That policy provides that whether "
           "an adjustment is unreasonable or would cause <i>“unjustifiable hardship”</i> is "
           "<b>“tested against the whole organisation, not a division or unit within the "
           "organisation”</b>, and that <b>“the onus is on Queensland Health, as the employer, to "
           "prove an adjustment is unreasonable, not on the person to prove that it is "
           "reasonable.”</b> The same policy records that a failure to provide reasonable "
           "adjustment <i>“may constitute unlawful discrimination.”</i>", NUM))
s.append(P("<b>4. What I ask.</b> That the adjustments identified in the report be implemented, and "
           "that I be returned to my substantive position on that basis; and that my pay be "
           "restored, and the leave debited since 3 July 2026 be recredited.", NUM))
s.append(P("<b>5.</b> The matters raised in my correspondence of <b>3 August 2026</b> remain "
           "undetermined, including the request made that day under the flexible working provisions "
           "of the Enterprise Agreement, in respect of which the period for a decision expires on "
           "<b>24 August 2026</b>.", NUM))
s.append(P("<b>6.</b> <b>The same report has today been provided to the Workers' Compensation "
           "Regulator</b> by way of continuing disclosure in QIRC proceeding WC/2024/227. The cost "
           "of the report has been met by the Health Service; it was instructed by me and is "
           "addressed to me.", NUM))
s.append(P("Kind regards,<br/><br/>Cory Lea Shepherd<br/>Administration Officer, Switchboard "
           "Services, Logan Hospital", BODY))

s.append(P("<b>WHAT MUST NOT ACCOMPANY EITHER NOTE:</b> no reference to the Public Interest "
           "Disclosure or to reprisal · no reference to any conflict of interest · no "
           "characterisation of anyone's conduct · nothing from the parallel tracks. <b>And "
           "nothing about the December 2024 matter, its outcome, or the separation document</b> — "
           "standing rule 10.", INT))
s.append(P("<b>BEFORE SENDING NOTE 2:</b> verify the flexible-working clause numbering against "
           "EB12 if the clause is to be cited; the note above deliberately refers to <i>“the "
           "flexible working provisions of the Enterprise Agreement”</i> without a clause number, "
           "which is safe as it stands.", INT))

doc = SimpleDocTemplate("out/DISTRIBUTION_NOTES_report.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — distribution notes", author="Cory Lea Shepherd")
def f(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm, "WC/2024/227 · Shepherd · the two distribution notes · send simultaneously")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
print("built out/DISTRIBUTION_NOTES_report.pdf")
