#!/usr/bin/env python3
"""WC/2024/227 — PREDICTION: the appeal and the employment track, with the report in hand.

⛔ INTERNAL. Structured judgement, not measurement. Every number is a reasoned estimate stated with
its basis; the simulation propagates uncertainty, it does not create knowledge. Read the movement,
not the decimals.

Built on the mock report at out/MOCK_REPORT_simulation.pdf — i.e. this predicts the world in which
the psychiatrist writes approximately what the instruction asks for.
"""
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle)

# ─────────────────────────────────────────── the model
rng = np.random.default_rng(20260816); N = 200_000
def beta(m, n): return rng.beta(m*n, (1-m)*n, N)
u = lambda: rng.random(N)

p_report          = beta(0.90, 25)   # funding closed; practice engaged; he has written one before
p_causation       = beta(0.82, 20)   # his own 2025 attribution + assumed facts + no competing onset
p_capacity        = beta(0.84, 20)   # ECC + movement forms + "worked and tolerated"
p_no_bad_sentence = beta(0.72, 12)   # the two sentences at Part 28/30 — draft review catches most
p_s32_5a          = beta(0.62, 14)   # THE contest: absence-of-management vs "blemish" answer
p_settle_pre      = beta(0.45, 12)   # Regulator settles once causation is proved

report   = u() < p_report
caus     = report & (u() < p_causation)
cap      = report & (u() < p_capacity)
clean    = report & (u() < p_no_bad_sentence)
exclusion_survived = caus & (u() < p_s32_5a)
settle   = caus & (u() < p_settle_pre)
appeal_ok = settle | (exclusion_survived & ~settle)
pay_back  = cap & clean & (u() < beta(0.66, 14)) | (~cap & (u() < beta(0.28, 10)))
sep_risk  = (~clean) & (u() < beta(0.35, 10))

def pc(x): return f"{x.mean()*100:.0f}%"

# ─────────────────────────────────────────── the document
ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=13, leading=16.5, spaceAfter=3)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.6, leading=14, spaceBefore=11, spaceAfter=4)
B  = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.5, leading=12.9, spaceAfter=5)
SM = ParagraphStyle('SM', parent=B, fontSize=8.3, leading=11, textColor=colors.HexColor('#555555'))
FL = ParagraphStyle('FL', parent=B, fontSize=8.7, leading=11.8, leftIndent=6,
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

d = []
d.append(P("PREDICTION — the appeal and the employment track, with the report in hand", H1))
d.append(P("WC/2024/227 · 16 August 2026 · 200,000 runs · INTERNAL", SM))
d.append(P("<b>STRUCTURED JUDGEMENT, NOT MEASUREMENT.</b> Every input is a reasoned estimate "
           "stated with its basis. The simulation propagates uncertainty; it does not create "
           "knowledge. <b>Read the movement, not the decimals.</b>", FL))

d.append(P("1 · THE NODES, AND WHY EACH SITS WHERE IT DOES", H2))
d.append(T([
 [P("<b>Node</b>", SM), P("<b>p</b>", SM), P("<b>Basis</b>", SM)],
 [P("Report obtained", SM), P("<b>90%</b>", SM),
  P("Funding closed directly with the practice · he has written a structured report on this patient "
    "before · the instruction supplies the facts. Residual: illness, workload, or he declines the "
    "medico-legal footer request", SM)],
 [P("Causation supported", SM), P("<b>82%</b>", SM),
  P("His own Feb 2025 report already attributes to <i>“workplace stress stemming from issues with "
    "management and rostering”</i> · every non-employment factor post-dates onset · the assumed "
    "facts are third-party. Residual: he hedges, or the 2022 history moves him", SM)],
 [P("Capacity answered favourably", SM), P("<b>84%</b>", SM),
  P("The checklist already says <i>“worked and tolerated… without deterioration”</i> · the movement "
    "forms show the adjustment approved three times with the shift requirement retained", SM)],
 [P("<b>No damaging sentence</b>", SM), P("<b>72%</b>", SM),
  P("<b>The single most underrated risk.</b> His 2025 register coded the preparation as a "
    "symptom and called the litigation a barrier to return. The draft review catches most of it — "
    "but only the factual half is raisable", SM)],
 [P("<b>s 32(5)(a) does not defeat it</b>", SM), P("<b>62%</b>", SM),
  P("<b>THE CONTEST.</b> Absence of management is not management action — no fatigue "
    "assessment, no register, nothing implemented until after 30 June 2024, no consequential "
    "changes. Against: the <b>flattening</b> attempt (<i>“reasonable in all respects”</i> ×6), "
    "the blemish concession at ¶22(a), and Taylor and Reese have not given oral evidence", SM)],
 [P("Regulator settles once causation is proved", SM), P("<b>45%</b>", SM),
  P("Calderbank #2 rejected 16 July · but a causation opinion in MSH's own hands changes MSH's "
    "interest in resolution, and MSH is not the Regulator", SM)],
], [46*mm, 14*mm, 106*mm]))

d.append(P("2 · THE OUTPUT", H2))
d.append(T([
 [P("<b>Outcome</b>", SM), P("<b>With the pack as built</b>", SM), P("<b>If no report</b>", SM)],
 [P("<b>Report obtained and usable</b>", SM), P("<b>"+pc(report & clean)+"</b>", SM), P("—", SM)],
 [P("Causation supported in the report", SM), P("<b>"+pc(caus)+"</b>", SM), P("—", SM)],
 [P("<b>APPEAL resolves favourably</b>", SM), P("<b>"+pc(appeal_ok)+"</b>", SM), P("<b>30%</b>", SM)],
 [P("— by settlement before hearing", SM), P(pc(settle), SM), P("~10%", SM)],
 [P("— by decision after hearing", SM), P(pc(exclusion_survived & ~settle), SM), P("~20%", SM)],
 [P("<b>PAY restored / return within ~3 months</b>", SM), P("<b>"+pc(pay_back)+"</b>", SM), P("<b>30%</b>", SM)],
 [P("<b>Medical-separation attempt gains traction</b>", SM), P("<b>"+pc(sep_risk)+"</b>", SM), P("~25%", SM)],
 [P("<b>Both appeal and pay</b>", SM), P("<b>"+pc(appeal_ok & pay_back)+"</b>", SM), P("~12%", SM)],
 [P("<b>Neither</b>", SM), P("<b>"+pc(~appeal_ok & ~pay_back)+"</b>", SM), P("~49%", SM)],
], [72*mm, 47*mm, 47*mm], shade=(3,6,7)))

d.append(P("<b>THE MOVEMENT IS THE POINT.</b> The appeal goes from <b>30%</b> to <b>"
           + pc(appeal_ok) + "</b>, and <i>neither outcome</i> falls from about half to <b>"
           + pc(~appeal_ok & ~pay_back) + "</b>. <b>And the medical-separation risk does not go to "
           "zero — it is driven almost entirely by the one damaging sentence, not by the merits.</b>", FL))

d.append(PageBreak())

d.append(P("3 · THE LONGFORM REASONING — THE APPEAL", H2))
d.append(P("<b>Where the appeal actually stands.</b> There is no factual dispute worth having. The "
           "Regulator has accepted the 7-hour break, the 10-hour minimum, the Director's "
           "acknowledgement of a rostering error, the patient-safety criticality of the work, the "
           "payroll instruction and the correction, the retraction direction and the PID "
           "determination. What it denies is <b>meaning</b>: no correlation, the roster was "
           "equitable, not false or misleading, she needed confirmation. <b>Every fact admitted, "
           "every inference denied.</b>", B))
d.append(P("<b>What the report changes.</b> Until now the appellant could prove what happened and "
           "could not prove that it caused an injury. The medical opinion closes that gap and it "
           "closes it from third-party material — which means the Regulator cannot answer it by "
           "attacking the appellant's credit. <b>The appeal moves from <i>unproved on causation</i> "
           "to <i>proved on the medical, contested on the characterisation</i>.</b>", B))
d.append(P("<b>What remains, and it is one thing.</b> Section 32(5)(a): reasonable management action "
           "taken in a reasonable way. The Regulator's answer is that this was an isolated human "
           "error and that management action need not be perfect. <b>The answer to the answer is "
           "the Chief Executive's own letter</b> — no fatigue risk assessment existed, no register "
           "existed, fatigue risk management was implemented at that Switchboard only after 30 June "
           "2024, and there were <i>“no consequential changes to operating procedures.”</i> "
           "<b>s 32(5)(a) protects action. It has nothing to attach to where the answer is that "
           "nothing was in place and nothing changed.</b> And it was not isolated: two admitted "
           "errors by the same manager in successive months.", B))
d.append(P("<b>The two ways it still loses.</b> <b>(1) <i>Delaney</i>.</b> If the case is run as a "
           "global course of management conduct it is evaluated globally, and globally the employer "
           "did many ordinary things competently. <b>The discipline is to run one mechanism and one "
           "proven instance</b> — rostering and fatigue — and to let the rest be context. "
           "<b>(2) Oral evidence.</b> Taylor and Reese have not been cross-examined. A sympathetic "
           "and organised manager explaining a busy period can convert <i>“human error”</i> into "
           "<i>“reasonable in the circumstances”</i> in the Commissioner's mind. <b>The documents "
           "cannot be shaken; the witnesses can be rehabilitated.</b>", B))
d.append(P("<b>The settlement read.</b> A causation opinion sitting in the employer's hands, on "
           "the employer's own request form, funded by the employer, is exactly what makes the "
           "employer want the appeal resolved — and the employer's appetite is transmitted to the "
           "Regulator through the Health Service's instructions, not through the appeal. <b>That is "
           "the mechanism by which this settles, and it is why the dual-purpose report is worth more "
           "than two separate ones.</b>", B))

d.append(P("4 · THE LONGFORM REASONING — THE WORKPLACE", H2))
d.append(P("<b>The employment track is where the money is, and the appeal does not reach it.</b> "
           "The appeal decides compensation for the injury. It does not restore 2026 wages, it does "
           "not recredit the leave debited since 3 July 2026, and it does not put him back in the "
           "role. Only the employment track does that, and it runs on its own clocks.", B))
d.append(P("<b>What the report does there.</b> It removes the only answer the Health Service has "
           "left. Its request of 31 July asked whether he could fulfil the inherent requirements "
           "<i>without restrictions or modifications</i>. <b>The answer will be: with these "
           "adjustments, yes — and the same Director approved modifications to those duties three "
           "times in the five months before asking.</b> Once that is in writing, the question is no "
           "longer whether adjustments are possible; it is whether the Health Service will provide "
           "them, and under its own policy <b>the onus of showing it cannot is the Health "
           "Service's, tested against the whole organisation and not the Logan roster.</b>", B))
d.append(P("<b>The separation risk, honestly.</b> The pathway to medical separation requires a "
           "medical opinion that he cannot perform the inherent requirements. <b>Nothing in the pack "
           "supplies one</b> — 3.6(a) requires any negative to be itemised by duty so it cannot be "
           "read as global incapacity, and 3.6(b) and (e) point the other way. <b>The only way "
           "it arrives is by a sympathetic sentence: the preparation described as a symptom, the "
           "litigation described as the barrier to return, or a protective recommendation that he "
           "not be exposed.</b> That is why the residual separation risk in the model tracks the "
           "damaging-sentence node and almost nothing else.", B))
d.append(P("<b>The clocks that do not wait for the report.</b> <b>24 August 2026</b> — the "
           "flexible-working request of 3 August reaches the end of its period. If no written "
           "decision issues, record the deemed refusal in one line on the day. Verify the clause "
           "numbering against EB12 before citing it, and check whether the deemed refusal is itself "
           "appealable with a short limitation. <b>That is the only live route to the 2026 wages, "
           "and it runs regardless of what the psychiatrist writes.</b>", B))

d.append(P("5 · WHAT WOULD MOVE THE NUMBERS MOST", H2))
d.append(T([
 [P("<b>Action</b>", SM), P("<b>Effect</b>", SM)],
 [P("<b>Catch the damaging sentence on the draft</b>", SM),
  P("The largest single lever. It moves the appeal a few points and it <b>halves the "
    "medical-separation risk</b>. Costs nothing — the review is already promised", SM)],
 [P("<b>Serve the role description on the Regulator before commissioning</b>", SM),
  P("Removes the one procedural attack available on the report's foundation", SM)],
 [P("<b>The 24 August record</b>", SM),
  P("Independent of the report and the only route to the 2026 wages", SM)],
 [P("<b>The April 2025 call statistics</b>", SM),
  P("Answers <i>“he kept working for fourteen months”</i> — the one question the capability "
    "checklist does not reach", SM)],
 [P("<b>Run one mechanism — refuse the flattening</b>", SM),
  P("Not a retreat from the course: the composite is the <b>standing fatigue condition</b>, with "
    "the rest as context. A drafting decision in the outline, worth more than further evidence", SM)],
], [62*mm, 104*mm]))

d.append(P("6 · WHAT THIS MODEL DOES NOT KNOW", H2))
d.append(P("It does not know what Dr Krishnaiah will actually write. It does not know how Taylor and "
           "Reese present under cross-examination — the single largest unmodelled variable. It does "
           "not know the Commissioner. It assumes the pack is sent substantially as built. And it "
           "treats the two tracks as loosely coupled when in practice a settlement on one usually "
           "resolves the other. <b>Every number here is a prior, and the first real evidence — "
           "the draft report — will move all of them at once.</b>", B))

doc = SimpleDocTemplate("out/PREDICTION_appeal_and_workplace.pdf", pagesize=A4,
                        leftMargin=19*mm, rightMargin=19*mm, topMargin=15*mm, bottomMargin=15*mm,
                        title="WC/2024/227 — prediction", author="Internal working document")
def f(canv, dd):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7.2)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(19*mm, 9*mm, "INTERNAL — STRUCTURED JUDGEMENT, NOT MEASUREMENT")
    canv.setFont('Helvetica', 7.2); canv.setFillColor(colors.HexColor('#777777'))
    canv.drawRightString(A4[0]-19*mm, 9*mm, f"Page {dd.page}")
    canv.restoreState()
doc.build(d, onFirstPage=f, onLaterPages=f)
print("built out/PREDICTION_appeal_and_workplace.pdf")
print(f"  report+clean {pc(report&clean)} | causation {pc(caus)} | APPEAL {pc(appeal_ok)} "
      f"| PAY {pc(pay_back)} | separation risk {pc(sep_risk)} | neither {pc(~appeal_ok & ~pay_back)}")
