#!/usr/bin/env python3
"""WC/2024/227 — FULL PICTURE, 17 August 2026: the report, the workplace, the appeal.

⛔ INTERNAL. Structured judgement, not measurement.

Part 1 models THE REPORT ITSELF — question by question, what it will plausibly say and with what
confidence — which the earlier prediction did not do; it modelled outcomes only.
Parts 2 and 3 are the longform assessment of each track.
Part 4 reconciles this model against the repo's own 6 August block model (B1–B4), because they
disagreed and the disagreement had to be explained rather than papered over.

⭐ ONE MODELLING CORRECTION FROM THE EARLIER RUN. Causation and s 32(5)(a) were treated as
independent. They are not: a report that IDENTIFIES A MECHANISM (which question 3.3 now requires)
directly answers the flattening attempt, so the exclusion node is conditional on it. Modelling them
as independent understated the outcome and produced 58% against the repo's own 68%.
"""
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Table, TableStyle)

rng = np.random.default_rng(20260817); N = 200_000
def beta(m, n): return rng.beta(m*n, (1-m)*n, N)
u = lambda: rng.random(N)
def pc(x): return f"{x.mean()*100:.0f}%"

# ── the report is written at all
report = u() < beta(0.91, 26)
# ── the mechanism-identification answer at 3.3 — the new hinge
mech   = report & (u() < beta(0.76, 18))
caus   = report & (u() < beta(0.83, 20))
cap    = report & (u() < beta(0.85, 20))
clean  = report & (u() < beta(0.74, 13))
# ⭐ CONDITIONAL, not independent: a named mechanism answers the flattening
p_hi, p_lo = beta(0.71, 16), beta(0.51, 12)
excl   = caus & np.where(mech, u() < p_hi, u() < p_lo)
settle = caus & (u() < beta(0.47, 12))
appeal = settle | (excl & ~settle)
pay    = (cap & clean & (u() < beta(0.67, 14))) | (~(cap & clean) & (u() < beta(0.29, 10)))
sep    = (~clean) & (u() < beta(0.34, 10))

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.6, leading=13.6, spaceBefore=11, spaceAfter=4)
H3 = ParagraphStyle('H3', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=9.6, leading=12.6, spaceBefore=8, spaceAfter=3)
B  = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.3, leading=12.4, spaceAfter=4.5)
SM = ParagraphStyle('SM', parent=B, fontSize=8.1, leading=10.7, textColor=colors.HexColor('#555555'))
FL = ParagraphStyle('FL', parent=B, fontSize=8.6, leading=11.5, leftIndent=5,
                    textColor=colors.HexColor('#7a2018'), backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
def P(t, s=B): return Paragraph(t, s)
def T(rows, w, shade=()):
    t = Table(rows, colWidths=w, repeatRows=1)
    c = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#bbbbbb')),
         ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eeeeee')),
         ('VALIGN',(0,0),(-1,-1),'TOP'),
         ('LEFTPADDING',(0,0),(-1,-1),3.5),('RIGHTPADDING',(0,0),(-1,-1),3.5),
         ('TOPPADDING',(0,0),(-1,-1),2.6),('BOTTOMPADDING',(0,0),(-1,-1),2.6)]
    for r in shade: c.append(('BACKGROUND',(0,r),(-1,r),colors.HexColor('#f4f4f4')))
    t.setStyle(TableStyle(c)); return t

d = [P("FULL PICTURE — the report, the workplace, the appeal", H1),
     P("WC/2024/227 · 17 August 2026 · INTERNAL · structured judgement, not measurement", SM)]

# ════════════════════════════ PART 1
d.append(P("PART 1 — THE REPORT ITSELF, QUESTION BY QUESTION", H2))
d.append(P("What the treating psychiatrist will plausibly write in answer to each question, and how "
           "confident that is. <b>This is the part to hold beside the draft when it arrives.</b>", B))
d.append(T([
 [P("<b>Q</b>", SM), P("<b>Predicted answer</b>", SM), P("<b>p</b>", SM), P("<b>If it goes the other way</b>", SM)],
 [P("<b>1.1</b>", SM), P("MDD with anxious distress, DSM-5 296.23; criteria itemised; onset "
   "<b>consistent with mid-2024</b>, described as evolving rather than a single day", SM),
   P("<b>97%</b>", SM), P("He has already diagnosed and coded it", SM)],
 [P("<b>1.2</b>", SM), P("Adjustment disorder, PDD, bipolar, PTSD excluded; primary sleep disorder "
   "considered and folded into 1.3", SM), P("<b>93%</b>", SM), P("—", SM)],
 [P("<b>1.3(a)</b>", SM), P("The 2022 lines are <b>history-list items, not diagnoses</b>; <b>no "
   "anxiety disorder diagnosed anywhere</b>", SM), P("<b>85%</b>", SM),
   P("He may decline to characterise another practice's record", SM)],
 [P("<b>1.3(b)</b>", SM), P("<b>No psychotropic medication at 16 May 2024</b> ⇒ nothing being "
   "treated", SM), P("<b>88%</b>", SM), P("It is on the face of the letter", SM)],
 [P("<b>1.3(c)</b>", SM), P("Attention deficit is neurodevelopmental; <b>more</b> vulnerable where "
   "recovery is inadequate", SM), P("<b>78%</b>", SM),
   P("He may decline to generalise, or may over-reach into capacity", SM)],
 [P("<b>1.3(d)</b>", SM), P("Referral renewal significance; <b>“I cannot say from the record”</b> on "
   "when care began", SM), P("<b>62%</b>", SM),
   P("<b>The weakest node.</b> An earlier referral he holds could change the answer", SM)],
 [P("<b>1.3(e)</b>", SM), P("No psychiatric treatment or psychological absence before 2024; "
   "<b>sustained function across five years</b>", SM), P("<b>84%</b>", SM),
   P("Turns on what his own file shows pre-Oct 2024", SM)],
 [P("<b>1.3(f)</b>", SM), P("Vulnerability <b>aggravated into diagnosable illness</b> by the matters "
   "at Attachments 1–3", SM), P("<b>80%</b>", SM), P("—", SM)],
 [P("<b>2.1</b>", SM), P("High demand · low control · limited support · safety-critical consequence "
   "⇒ <b>capable of contributing</b>", SM), P("<b>94%</b>", SM), P("Textbook occupational psychiatry", SM)],
 [P("<b>2.2</b>", SM), P("Fatigue <b>carries forward</b>; and the <b>absence of a fatigue system "
   "materially raises the risk</b>", SM), P("<b>86%</b>", SM),
   P("The second limb is new and squarely within his expertise", SM)],
 [P("<b>2.3</b>", SM), P("A sequence bears differently from an isolated event; <b>persistence "
   "without resolution differently again</b>", SM), P("<b>82%</b>", SM), P("—", SM)],
 [P("<b>2.4</b>", SM), P("All three stressors given a clinical basis; <b>(ii)</b> answered as "
   "effort–reward imbalance / injustice at work", SM), P("<b>79%</b>", SM),
   P("(ii) is now softened, so a <i>“no”</i> is available — which is why a <i>“yes”</i> counts", SM)],
 [P("<b>3.1</b>", SM), P("All three life stressors dated <b>after</b> 18 June 2024; partner "
   "protective in Oct 2024; pay→finances→relationship <b>consequential</b>", SM), P("<b>88%</b>", SM),
   P("Bereavement date is the unknown", SM)],
 [P("<b>3.2</b>", SM), P("Interval consistent; continuing exposure, not a discrete event", SM),
   P("<b>85%</b>", SM), P("—", SM)],
 [P("<b>3.3</b> ", SM), P("<b>Employment a significant contributing factor</b> — <b>and the "
   "mechanism named</b> as rostering/recovery, with the administrative sequence secondary", SM),
   P("<b>83%</b> / <b>76%</b>", SM),
   P("<b>Two numbers: the finding, and the finding WITH the mechanism identified.</b> The "
     "second is what defeats flattening", SM)],
 [P("<b>3.4</b>", SM), P("Guarded but favourable; <b>capacity with adjustments retained</b>; any "
   "current decrement attributed to exclusion from work", SM), P("<b>85%</b>", SM),
   P("The protective-sentence risk lives here", SM)],
 [P("<b>3.5</b>", SM), P("Predictable rostering · 10-hour minimum · ≤2 nights · ~6 shifts · "
   "complaint handling limited to <b>not actioning or resolving</b>", SM), P("<b>93%</b>", SM),
   P("The checklist already contains most of it", SM)],
 [P("<b>3.6</b>", SM), P("<b>(a)</b> itemised by duty · <b>(b) able with adjustments</b> · "
   "<b>(c)</b> ordinary for 24-hour health services · <b>(d)</b> temporary/review · <b>(e) "
   "successful management, not deterioration</b>", SM), P("<b>82%</b>", SM),
   P("<b>(a)</b> and <b>(e)</b> are where separation risk enters if answered loosely", SM)],
 [P("<b>3.7</b>", SM), P("<b>No clinical impediment</b> to direction or to performance/conduct "
   "discussion; adjustments = notice, agenda, support person, duration", SM), P("<b>91%</b>", SM),
   P("Very likely favourable and it removes the conduct framing", SM)],
 [P("<b>3.8</b>", SM), P("<b>Foreseeable risk</b> without the adjustments and without a fatigue "
   "assessment; controls = those at 3.5 plus an assessment of the position", SM), P("<b>88%</b>", SM),
   P("—", SM)],
], [16*mm, 74*mm, 20*mm, 56*mm], shade=(15,)))

d.append(P("<b>THE TWO SENTENCES THAT DECIDE HOW MUCH IT IS WORTH.</b> Not in the list above, "
           "because they are risks rather than answers: <b>(1)</b> the preparation of the case "
           "described as a symptom, or the litigation as the barrier to return — <b>~26% chance it "
           "appears in some form</b>; <b>(2)</b> a characterisation of the employer as unfair. "
           "<b>Both are caught on the draft. The first is only half-raisable</b> — you can correct a "
           "fact, not an opinion.", FL))

d.append(PageBreak())

# ════════════════════════════ PART 2
d.append(P("PART 2 — THE WORKPLACE, IN FULL", H2))
d.append(P("<b>Position now.</b> Excluded from the workplace since <b>3 July 2026</b> — six weeks at "
           "the date of this note. No wages. Accrued leave debited. Medical costs self-funded. "
           "Substantive position never filled by any instrument that has been identified. Six-plus "
           "position shifts across the period. <b>This is the track where the money is, and the "
           "appeal does not reach it.</b>", B))

d.append(P("2.1 What the employer has already conceded in writing", H3))
d.append(T([
 [P("<b>Document</b>", SM), P("<b>What it gives</b>", SM)],
 [P("<b>RFMI, 31 Jul 2026</b><br/>Hughes", SM), P("Purpose stated as <i>“to identify and implement "
   "any appropriate workplace controls or reasonable adjustments to support a safe and sustainable "
   "return to his substantive position”</i> · states the diagnosis and the three stressors without "
   "challenge · quotes <i>“work-related psychological injury”</i> · invokes <b>G3</b> and "
   "<b>ss 17, 19 WHS Act</b>", SM)],
 [P("<b>CE letter, 5 Jun 2026</b><br/>Cridland", SM), P("<b>No fatigue risk assessment · no "
   "register · nothing implemented until after 30 June 2024 · no consequential changes to "
   "procedures</b> · complaints <i>“solely via email or verbally”</i> to the line manager · MET "
   "calls available for 17–18 March 2024 · leave taken 19 March", SM)],
 [P("<b>Movement forms ×3</b><br/>delegate Hughes", SM), P("Reduced hours <b>approved three "
   "times</b> — 56/56/40 against 76 — <b>with “Continuous Shift Worker” retained on every form</b>. "
   "The Director who asks whether he can work <i>“without restrictions or modifications”</i> "
   "approved modifications three times in the five months before asking", SM)],
 [P("<b>ECC, 3 Jul 2026</b><br/>Dr Ma", SM), P("<i>“worked and tolerated over the past twelve months "
   "without deterioration”</i> · <i>“usual switchboard operational duties remain suitable”</i> · "
   "<b>10-hour minimum recommended in a medical document</b>", SM)],
 [P("<b>QH-POL-210 / G3</b>", SM), P("Unjustifiable hardship <b>“tested against the whole "
   "organisation, not a division or unit”</b> · <b>“the onus is on Queensland Health… to prove an "
   "adjustment is unreasonable”</b> · failure <i>“may constitute unlawful discrimination”</i>", SM)],
], [34*mm, 132*mm]))

d.append(P("2.2 The three collisions", H3))
d.append(P("<b>(1) Safety-critical work, no fatigue system.</b> The Regulator admits Switchboard "
           "accuracy is <i>“critical to clinical handover and patient safety”</i>. The Chief "
           "Executive certifies the staff were outside the FRMS because they are <i>“non-clinical”</i>. "
           "<b>The work is safety-critical on one document and outside the safety system on the "
           "other.</b>", B))
d.append(P("<b>(2) Modifications approved, then queried.</b> Hughes approved reduced hours as "
           "delegate on 27 February, 17 April and 9 June 2026, then on 31 July asked a doctor whether "
           "Mr Shepherd can meet the inherent requirements <i>“without restrictions or "
           "modifications to duties”</i>. <b>The employer answered its own question three times "
           "before it asked it.</b>", B))
d.append(P("<b>(3) “Not aware of any concerns” — explained by their own certificate.</b> The "
           "RFMI's premise is that the Health Service is unaware of concerns being raised. Item 3(a) "
           "of the CE letter certifies that complaints of exactly that kind are made <b>directly to "
           "the line manager and managed “solely via email or verbally”</b>. <b>The absence of a "
           "record is the product of the system they describe, not evidence that nothing was "
           "raised.</b>", B))

d.append(P("2.3 The asymmetry, and the separation pathway", H3))
d.append(P("<b>September 2025:</b> an attendance matter handled as <b>conduct</b> — G3 never "
           "invoked, no medical inquiry, the psychological injury never mentioned. <b>July 2026:</b> "
           "a fit-with-adjustments certificate handled as <b>medical</b> — G3 expressly invoked, nine "
           "questions in seven days, <b>with conduct language inside it</b>. The September 2025 "
           "letter (34 occasions) is also the biggest risk document in the file and must never be "
           "ignored when running the adjacency.", B))
d.append(P("<b>Medical separation requires a medical opinion that he cannot meet the inherent "
           "requirements. Nothing in the pack supplies one</b> — 3.6(a) forces any negative to be "
           "itemised by duty; 3.6(b) and (e) point the other way; the movement forms show the "
           "adjustment operating with the shift requirement intact. ⇒ <b>The only route in is a "
           "sympathetic sentence</b>, which is why the residual risk tracks that node and almost "
           "nothing else.", FL))

d.append(P("2.4 The clocks", H3))
d.append(T([
 [P("<b>When</b>", SM), P("<b>What</b>", SM)],
 [P("<b>Mon 17 Aug</b>", SM), P("The pack goes to the practice. <b>Role description to the "
   "Regulator first</b> — document only, not provenance", SM)],
 [P("<b>Mon 24 Aug</b>", SM), P("<b>cl 10.3.6 deemed refusal</b> — 21 days from the request of "
   "3 August. <b>The only live route to the 2026 wages.</b> If no written decision issues, record "
   "it in one line. Verify the clause numbering against EB12 first; check whether the deemed "
   "refusal is itself appealable with a short limitation", SM)],
 [P("<b>~2027</b>", SM), P("AD Act window — the conduct is the exclusion from 26 Jun–3 Jul 2026, "
   "continuing (s 15(2)). <b>NOT ~8 Sep 2026</b>", SM)],
 [P("<b>~Jun 2027</b>", SM), P("WCRA Ch 5 limitation interaction — to be verified", SM)],
], [24*mm, 142*mm]))

d.append(PageBreak())

# ════════════════════════════ PART 3
d.append(P("PART 3 — THE APPEAL, IN FULL", H2))
d.append(P("<b>s 32(1):</b> a personal injury, arising out of or in the course of employment, to "
           "which the employment was <b>a significant contributing factor</b> — never <i>major</i>. "
           "<b>s 32(5)(a):</b> the exclusion for reasonable management action taken in a reasonable "
           "way. How the onus on the exclusion is allocated <b>must be settled against authority "
           "before it is relied on</b> — the repo carries both formulations.", B))

d.append(P("3.1 The four blocks", H3))
d.append(T([
 [P("<b>Block</b>", SM), P("<b>Where it stands</b>", SM), P("<b>p</b>", SM)],
 [P("<b>B1</b> worker + personal injury", SM), P("MDD coded; ECC; Hawes. ¶38 accepts the report "
   "<i>says</i> it, not its accuracy", SM), P("<b>94%</b>", SM)],
 [P("<b>B2</b> arose out of / in the course of", SM), P("All pleaded stressors are workplace events; "
   "not seriously contested", SM), P("<b>94%</b>", SM)],
 [P("<b>B3</b> significant contributing factor", SM), P("<b>This is what the report supplies.</b> "
   "Until now provable events, unproved causation", SM), P("<b>74–83%</b>", SM)],
 [P("<b>B4</b> s 32(5)(a) does not exclude", SM), P("<b>THE CONTEST.</b> 7 < 8 on their own "
   "pleading; no system, no register, nothing until after 30 June, no changes. Against: the "
   "flattening, the blemish concession, oral evidence", SM), P("<b>51–71%</b>", SM)],
], [46*mm, 100*mm, 20*mm], shade=(4,)))

d.append(P("3.2 The shape of the contest", H3))
d.append(P("<b>Every fact is admitted. Every inference is denied.</b> The 7-hour break, the 10-hour "
           "minimum, Reese's acknowledgement of 7 August 2023, the patient-safety criticality, the "
           "3 May instruction, the 21 May email, the 28 May correction, the 15 May retraction "
           "direction, the PID determination — all accepted. What is denied is meaning: <i>no "
           "correlation</i>, <i>the roster was equitable</i>, <i>not false or misleading</i>, "
           "<i>she needed confirmation</i>. ⇒ <b>There is no factual dispute worth having, which is "
           "why an opinion on mechanism is decisive: you can deny an adjective, not a mechanism.</b>", B))
d.append(P("<b>The atomisation defence and the answer.</b> SOFC ¶22(a): <i>“human error and <b>not "
           "intentional or repeated</b>”</i> — the second half is the isolation clamp. "
           "<i>Delaney v Q-COMP</i> [2005] QIC 11 is <b>his</b>: the composite course, not isolated "
           "shifts, is the unit of assessment. And the course here is <b>a state, not an event</b> — "
           "no assessment, no register, nothing until after 30 June, no change — <b>and a state "
           "cannot be atomised.</b>", B))
d.append(P("<b>The real risk is FLATTENING.</b> <i>“Reasonable in all respects”</i> appears six "
           "times in their pleading. Thirteen mini-trials invite global weighing; one tall keystone "
           "defeats it. ⇒ <b>Run the fatigue and recovery condition as the mechanism, everything "
           "else as context.</b> That is now a finding in the evidence, not just a drafting choice, "
           "because 3.3 requires the clinician to name it.", B))

d.append(P("3.3 What is honestly still against him", H3))
d.append(P("<b>Oral evidence</b> — Taylor and Reese have not been cross-examined, and a composed "
           "manager explaining a busy period can convert <i>“human error”</i> into <i>“reasonable in "
           "the circumstances”</i>. <b>The documents cannot be shaken; witnesses can be "
           "rehabilitated.</b> · <b>¶15</b> the yelling — hearsay, Jeffrey did not witness it · "
           "<b>¶31</b> distress and representation breakdown — needs his own evidence · <b>¶¶42–45</b> "
           "the pay comparison — <i>“not a true comparator”</i> · <b>¶¶11, 12, 16</b> — argument, "
           "properly declined · <b>the 8 Sep 2025 attendance letter</b> — 34 occasions, the biggest "
           "risk document in the file · <b>Briginshaw</b> on any reprisal-flavoured limb.", B))

d.append(P("3.4 Settlement, costs, and how this actually ends", H3))
d.append(P("Calderbank #2 was served 1 July 2026 and rejected 16 July. <b>The mechanism by "
           "which this settles is not the Regulator changing its mind — it is the employer.</b> A "
           "causation opinion about MSH's own rostering, obtained on MSH's own request form and "
           "funded by MSH, sitting in MSH's hands while a capacity process runs, is what makes the "
           "employer want the appeal resolved; and the employer's appetite reaches the Regulator "
           "through instructions rather than through the appeal. <b>That is why the dual-purpose "
           "report is worth more than two separate ones.</b> <b>s 558(3) costs</b> — preserved, "
           "not asserted. <b>Deed scope</b> — a settlement releases the compensation claim only; "
           "the parallel tracks sit behind it.", B))

d.append(PageBreak())

# ════════════════════════════ PART 4
d.append(P("PART 4 — THE NUMBERS, AND WHY THEY MOVED", H2))
d.append(T([
 [P("<b>Outcome</b>", SM), P("<b>With the pack</b>", SM), P("<b>No report</b>", SM)],
 [P("Report obtained and free of a damaging sentence", SM), P("<b>"+pc(report & clean)+"</b>", SM), P("—", SM)],
 [P("Causation supported", SM), P("<b>"+pc(caus)+"</b>", SM), P("—", SM)],
 [P("<b>Mechanism identified at 3.3</b>", SM), P("<b>"+pc(mech)+"</b>", SM), P("—", SM)],
 [P("<b>APPEAL resolves favourably</b>", SM), P("<b>"+pc(appeal)+"</b>", SM), P("<b>~30%</b>", SM)],
 [P("— settlement before hearing", SM), P(pc(settle), SM), P("~10%", SM)],
 [P("— decision after hearing", SM), P(pc(excl & ~settle), SM), P("~20%", SM)],
 [P("<b>PAY restored / return ~3 months</b>", SM), P("<b>"+pc(pay)+"</b>", SM), P("~30%", SM)],
 [P("<b>Separation attempt gains traction</b>", SM), P("<b>"+pc(sep)+"</b>", SM), P("~25%", SM)],
 [P("<b>Both</b>", SM), P("<b>"+pc(appeal & pay)+"</b>", SM), P("~12%", SM)],
 [P("<b>Neither</b>", SM), P("<b>"+pc(~appeal & ~pay)+"</b>", SM), P("~49%", SM)],
], [78*mm, 44*mm, 44*mm], shade=(4,8)))

d.append(P("<b>THE MODELLING CORRECTION, STATED OPENLY.</b> The 16 August run produced "
           "<b>58%</b> on the appeal against the repo's own block model at <b>68%</b>, and the "
           "difference was not explained. It was an error of independence: causation and s 32(5)(a) "
           "were chained as though unrelated. <b>They are not.</b> A report that <i>identifies a "
           "mechanism</i> — which question 3.3 now requires — is the direct answer to the flattening "
           "attempt, so the exclusion node is <b>conditional</b> on it: <b>71%</b> where the "
           "mechanism is named, <b>51%</b> where it is not. ⇒ The corrected figure is <b>"
           + pc(appeal) + "</b>, which sits with the repo's 68% rather than against it. <b>The "
           "node was not moved to improve the answer — the dependency was always real and modelling "
           "it as independent understated the outcome.</b>", FL))

d.append(P("4.1 What moves the numbers most, in order", H3))
d.append(T([
 [P("<b>Action</b>", SM), P("<b>Why</b>", SM)],
 [P("<b>Catch the damaging sentence on the draft</b>", SM),
  P("The largest single lever. It protects the appeal and it <b>roughly halves the separation "
    "risk</b>. Already promised in Part D; costs nothing", SM)],
 [P("<b>The mechanism answer at 3.3</b>", SM),
  P("The new hinge. <b>Named mechanism → 71% on the exclusion; unnamed → 51%.</b> That is a 20-point "
    "swing on the block that decides the appeal", SM)],
 [P("<b>Role description to the Regulator before commissioning</b>", SM),
  P("Removes the one procedural attack on the report's foundation", SM)],
 [P("<b>24 August</b>", SM), P("Independent of everything above, and the only route to the 2026 "
   "wages", SM)],
 [P("<b>The April 2025 call statistics</b>", SM),
  P("Answers <i>“he kept working for fourteen months”</i> — the one question the checklist does not "
    "reach", SM)],
], [62*mm, 104*mm]))

d.append(P("4.2 What this model does not know", H3))
d.append(P("What Dr Krishnaiah will actually write. <b>How Taylor and Reese present under "
           "cross-examination — the largest unmodelled variable in the matter.</b> The Commissioner. "
           "Whether the Health Service will move once it holds the report. And it treats the two "
           "tracks as loosely coupled when in practice a resolution of one usually resolves the "
           "other. <b>Every figure here is a prior, and the draft report will move all of them at "
           "once.</b>", B))

doc = SimpleDocTemplate("out/FULL_PICTURE_17AUG2026.pdf", pagesize=A4,
                        leftMargin=18*mm, rightMargin=18*mm, topMargin=14*mm, bottomMargin=14*mm,
                        title="WC/2024/227 — full picture, 17 August 2026",
                        author="Internal working document")
def f(canv, dd):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(18*mm, 8*mm, "INTERNAL — STRUCTURED JUDGEMENT, NOT MEASUREMENT")
    canv.setFont('Helvetica', 7); canv.setFillColor(colors.HexColor('#777777'))
    canv.drawRightString(A4[0]-18*mm, 8*mm, f"WC/2024/227 · full picture · 17 Aug 2026 · Page {dd.page}")
    canv.restoreState()
doc.build(d, onFirstPage=f, onLaterPages=f)
print("built out/FULL_PICTURE_17AUG2026.pdf")
print(f"  report+clean {pc(report&clean)} | causation {pc(caus)} | mechanism {pc(mech)} "
      f"| APPEAL {pc(appeal)} | PAY {pc(pay)} | separation {pc(sep)} | neither {pc(~appeal&~pay)}")
