#!/usr/bin/env python3
"""WC/2024/227 — SETTLEMENT GUARD: what to protect if the approach comes from the Chief Executive.

⛔ INTERNAL. Built 17 August 2026 on Cory's read that the Health Service will settle and that it
comes from the Chief Executive herself.

⭐⭐⭐ THE POINT OF THIS DOCUMENT. There is ALREADY a Deed of Release on this file, from the
reinstatement/abandonment settlement. It expressly carved out the WCRA claim — which is why
WC/2024/227 survived — but it also carries NON-DISPARAGEMENT and CONFIDENTIALITY clauses whose
scope has never been factored into the standing advice.
⇒ A SECOND deed, drafted from the same template, is the live risk. The question is no longer
whether they settle. It is what the deed releases.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=12.6, leading=16, spaceAfter=3)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.4, leading=13.4, spaceBefore=10, spaceAfter=4)
B  = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.4, leading=12.6, spaceAfter=5)
SM = ParagraphStyle('SM', parent=B, fontSize=8.2, leading=10.9, textColor=colors.HexColor('#555555'))
FL = ParagraphStyle('FL', parent=B, fontSize=8.8, leading=11.8, leftIndent=5,
                    textColor=colors.HexColor('#7a2018'), backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
def P(t, s=B): return Paragraph(t, s)
def T(rows, w, shade=()):
    t = Table(rows, colWidths=w, repeatRows=1)
    c = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#bbbbbb')),
         ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eeeeee')),
         ('VALIGN',(0,0),(-1,-1),'TOP'),
         ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
         ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
    for r in shade: c.append(('BACKGROUND',(0,r),(-1,r),colors.HexColor('#f4f4f4')))
    t.setStyle(TableStyle(c)); return t

d = [P("SETTLEMENT GUARD — what to protect if the approach comes from the Chief Executive", H1),
     P("WC/2024/227 · 17 August 2026 · INTERNAL", SM)]

d.append(P("1 · WHY THE READ IS WELL-FOUNDED ON THE RECORD", H2))
d.append(T([
 [P("<b>Fact</b>", SM), P("<b>Why it points at the Chief Executive</b>", SM)],
 [P("She signed the letter of <b>5 June 2026</b> (ref K-LM26/729)", SM),
  P("That letter certifies <b>no fatigue risk assessment, no register, nothing implemented until "
    "after 30 June 2024, no consequential changes to procedures</b>, and that complaints are managed "
    "<i>“solely via email or verbally”</i>. <b>She is the one person in the organisation who has "
    "personally certified the absence.</b> A chief executive who signed that knows what it says", SM)],
 [P("The Health Service is funding the report", SM),
  P("Confirmed directly with the practice. ⇒ <b>It will hold a causation opinion about its own "
    "rostering, obtained on its own request form, at its own cost</b>", SM)],
 [P("The letter to her of <b>3 August 2026</b> was acknowledged", SM),
  P("Acknowledgement at that level, with no substantive answer, is consistent with the matter having "
    "been taken up rather than deflected", SM)],
 [P("<b>Public Sector Act 2022 s 89</b>", SM),
  P("Conflict of interest — an officer must not take further action <b>unless authorised by the "
    "chief executive</b>. If she is engaged, that provision is live", SM)],
], [56*mm, 110*mm]))
d.append(P("<b>And structurally it fits the model.</b> Settlement correlates with the appeal outcome "
           "at <b>r = 0.40</b> — second only to causation, and ahead of the s 32(5)(a) contest. It "
           "was always going to run on the employer's appetite rather than the Regulator's change of "
           "mind.", B))

d.append(P("2 · WHAT I WILL NOT DO, AND WHAT WOULD COUNT AS EVIDENCE", H2))
d.append(P("<b>The model is not being moved on an expectation.</b> The settlement node stays at 47% "
           "until something happens that is not an inference. <b>What would count:</b> a written "
           "approach from her office or from a legal representative instructed by it · a request for "
           "a without-prejudice discussion · the capacity process being paused or transferred out of "
           "Corporate Services · pay or leave restored without a decision letter · or the Regulator's "
           "posture changing without the Regulator having any new material. ⚠ <b>An acknowledgement "
           "is not an offer, and silence at that level is as consistent with delegation as with "
           "resolution.</b>", FL))

d.append(P("3 · ⭐⭐⭐ THE THING THAT NOW MATTERS MORE — THERE IS ALREADY A DEED", H2))
d.append(P("A Deed of Release exists on this file from the reinstatement and abandonment settlement. "
           "<b>Two things about it govern everything that happens next.</b>", B))
d.append(T([
 [P("<b>Clause</b>", SM), P("<b>What it does</b>", SM)],
 [P("<b>The carve-out</b>", SM),
  P("The release excludes <i>“any statutory claim under the <b>Workers' Compensation and "
    "Rehabilitation Act 2003</b> or any claim that cannot be excluded at law”</i>. ⭐⭐⭐ <b>That is "
    "why WC/2024/227 survived — and it is proof they know how to draft a carve-out, because they "
    "drafted this one</b>", SM)],
 [P("<b>Non-disparagement</b>", SM),
  P("No adverse comment <i>“publicly or otherwise”</i> about the <b>Beneficiaries</b> — the Health "
    "Service, <b>every other HHS, the Department of Health, the State of Queensland</b>, related "
    "bodies, and <b>current and former officers and employees</b> — regarding <b>the matters recited: "
    "the employment, the Abandonment Process and the Reinstatement Application</b>", SM)],
 [P("<b>Confidentiality</b>", SM),
  P("The deed and the settlement kept strictly confidential, save as required by law, to enforce it, "
    "for professional advice, by consent, or to the ATO", SM)],
], [38*mm, 128*mm], shade=(1,)))
d.append(P("⛔⛔⛔ <b>A SECOND DEED IS THE RISK, NOT THE SETTLEMENT.</b> Drafted from the same "
           "template it would, unless resisted: <b>release the 2026 employment claims</b> — the "
           "exclusion since 3 July, the unpaid wages, the debited leave, the flexible-working "
           "refusal, and the <b>AD Act window that runs to 2027</b>; <b>extend non-disparagement</b> "
           "to the 2026 matters; and <b>capture the PID and reprisal track</b>, which has never been "
           "deployed and is being held deliberately behind the compensation claim.", FL))

d.append(P("4 · THE FIVE THINGS TO HOLD OUT FOR", H2))
d.append(T([
 [P("", SM), P("<b>Term</b>", SM), P("<b>Why</b>", SM)],
 [P("<b>1</b>", SM), P("<b>The employment claims are carved out</b>, in the same form as the WCRA "
   "carve-out in the existing deed", SM),
   P("⭐⭐⭐ <b>The appeal does not reach the 2026 wages.</b> A deed that settles the appeal and "
     "releases the employment claims settles the smaller of the two", SM)],
 [P("<b>2</b>", SM), P("<b>The PID and reprisal track is expressly preserved</b>", SM),
   P("Never deployed, sequenced behind the compensation claim. ⛔ A general release ends it silently", SM)],
 [P("<b>3</b>", SM), P("<b>Non-disparagement is confined</b> to the matters actually settled, and "
   "does not extend to statutory disclosures or to evidence given in any proceeding", SM),
   P("⚠ The existing clause reaches <b>the State of Queensland and every current and former "
     "officer</b>. A second one on those terms would be very wide", SM)],
 [P("<b>4</b>", SM), P("<b>Return to the substantive position with the adjustments</b>, or a stated "
   "alternative — plus <b>pay restored and leave recredited from 3 July 2026</b>", SM),
   P("The report is what makes this askable. ⭐ It is also the component the appeal cannot deliver at "
     "all", SM)],
 [P("<b>5</b>", SM), P("<b>Confidentiality does not prevent</b> compliance with a statutory "
   "obligation, or the use of payroll and employment records", SM),
   P("⭐ The existing deed already shows the safe route: <b>prove the payment from the payslip; do "
     "not tender the deed</b>", SM)],
], [8*mm, 74*mm, 84*mm]))

d.append(P("5 · SEQUENCING — NOTHING CHANGES ON MONDAY", H2))
d.append(P("<b>Send the pack.</b> If they are moving, the report is what sets the price; if they are "
           "not, it is what makes them. ⭐ <b>It is the mechanism, not an alternative to it.</b>", B))
d.append(P("<b>And 24 August still runs.</b> The deemed refusal is a documented failure at the level "
           "<i>below</i> the Chief Executive, and it costs nothing to record. ⚠ <b>Do not let the "
           "capacity process reach a decision first</b> — a Corporate Services decision on capacity, "
           "taken before any resolution, is much harder to unwind than a deemed refusal is to rely "
           "on.", B))
d.append(P("⛔ <b>AND THE STANDING RULES DO NOT RELAX BECAUSE A SETTLEMENT IS IN PROSPECT.</b> "
           "Nothing about the December 2024 matter, its outcome or the separation document. No "
           "conspiracy framing. No use of the word fraud in this track. <b>The parallel tracks stay "
           "sequenced behind the compensation claim until the deed scope is settled — which is "
           "precisely the point of everything above.</b>", FL))

doc = SimpleDocTemplate("out/SETTLEMENT_GUARD_17AUG2026.pdf", pagesize=A4,
                        leftMargin=19*mm, rightMargin=19*mm, topMargin=15*mm, bottomMargin=15*mm,
                        title="WC/2024/227 — settlement guard", author="Internal working document")
def f(canv, dd):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7.2)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(19*mm, 9*mm, "INTERNAL — NOT FOR ANY OTHER PARTY")
    canv.setFont('Helvetica', 7.2); canv.setFillColor(colors.HexColor('#777777'))
    canv.drawRightString(A4[0]-19*mm, 9*mm, f"WC/2024/227 · settlement guard · Page {dd.page}")
    canv.restoreState()
doc.build(d, onFirstPage=f, onLaterPages=f)
print("built out/SETTLEMENT_GUARD_17AUG2026.pdf")
