#!/usr/bin/env python3
"""WC/2024/227 — SIMULATED report: what the pack can and cannot produce.

⛔⛔⛔ THIS IS NOT A REPORT. It is a stress-test of the instruction and the four attachments,
written in the register of the treating psychiatrist's report of 13 February 2025, to establish
whether every question can be answered from the attached material.

⛔ IT MUST NEVER BE SENT TO THE PRACTICE, SHOWN TO THE PRACTICE, OR DISCLOSED. Putting a drafted
report in front of a clinician is steering, and steering is the one defect the whole design exists
to avoid. Internal file only.

The value is in the FLAGS: every place the simulated clinician cannot answer is a gap in the pack.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

OUT = "out/SIMULATED_REPORT_stress_test.pdf"
ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=13, leading=16, spaceAfter=3)
SEC = ParagraphStyle('SEC', parent=ss['Heading2'], fontName='Helvetica-Bold',
                     fontSize=10.4, leading=13.5, spaceBefore=11, spaceAfter=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.5, leading=13.2, spaceAfter=6)
QH = ParagraphStyle('QH', parent=BODY, fontName='Helvetica-Bold', spaceBefore=8, spaceAfter=2)
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=9, leading=12.5,
                      textColor=colors.HexColor('#8a2010'), backColor=colors.HexColor('#fdf1ef'),
                      borderPadding=6, spaceAfter=8)
GAP = ParagraphStyle('GAP', parent=BODY, fontSize=8.8, leading=12,
                     textColor=colors.HexColor('#8a2010'), leftIndent=8, spaceBefore=2)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))

def P(t, s=BODY): return Paragraph(t, s)
s = []

s.append(P("SIMULATED REPORT — STRESS TEST OF THE INSTRUCTION AND THE FOUR ATTACHMENTS", H1))
s.append(P("WC/2024/227 · prepared 15 August 2026 · internal", SMALL))
s.append(P("⛔⛔⛔ <b>THIS IS NOT A REPORT AND IT IS NOT EVIDENCE.</b> It is a simulation, written in "
           "the register of the treating psychiatrist's report of 13 February 2025, to test whether "
           "each question in the instruction can be answered from the attached material alone.<br/>"
           "⛔ <b>It must never be sent to, or shown to, the practice.</b> Putting a drafted report in "
           "front of a clinician is steering — the one defect the entire design exists to avoid. "
           "Internal file only.<br/>"
           "⭐ <b>The value of this document is the red flags.</b> Every place the simulated clinician "
           "cannot answer is a gap in the pack, and those gaps are listed at the end.", WARN))

s.append(P("PRESENTATION AND CLINICAL COURSE", SEC))
s.append(P("Mr Cory Shepherd (11-Jan-1991) was first assessed by me on 24 October 2024 on referral "
           "following a workplace psychological injury. He has remained under my care since that "
           "date. I have undertaken clinical assessment, reviewed my own clinical file, his "
           "general-practice records, the workers' compensation medical certificates, his "
           "certificate of capacity of 3 July 2026, and the documents provided to me by him and "
           "described below. Based on the above I am able to provide an opinion on diagnosis, "
           "causation, and current capacity.", BODY))
s.append(P("<b>Diagnosis:</b> Major Depressive Disorder with anxious distress (DSM-5 296.23).", BODY))

s.append(P("MATTER 1 — DID MR SHEPHERD SUSTAIN A PERSONAL INJURY?", SEC))
s.append(P("<b>1.1 Diagnosis, criteria and onset.</b> Mr Shepherd meets DSM-5 criteria for a Major "
           "Depressive Episode with the anxious distress specifier. At first assessment he described "
           "persistent low mood, anhedonia, sleep disturbance, impaired concentration, feelings of "
           "worthlessness and marked rumination, of more than two weeks' duration and representing a "
           "change from prior functioning. As to onset, the clinical record establishes first "
           "attendance for this injury on 1 July 2024 (Work Capacity Certificate, Dr Hawes), with a "
           "second certificate on 7 August 2024 (Dr Ki Pang). The records are consistent with onset "
           "shortly before that first attendance. My own assessment postdates onset by some months.",
           BODY))
s.append(P("<b>1.2 Differential diagnoses.</b> I considered adjustment disorder with mixed anxiety "
           "and depressed mood, and excluded it on the basis of the number and persistence of "
           "depressive criteria met and the degree of functional impairment. I considered a primary "
           "anxiety disorder and a substance-related presentation, and excluded both. Attention "
           "deficit features are addressed at 1.3.", BODY))
s.append(P("<b>1.3 Psychiatric background.</b> The general-practice records record an entry of "
           "26 October 2022 referring to anxiety and attention deficit features with stimulant "
           "(lisdexamfetamine) prescribing. The same records contain an entry of 16 November 2023 "
           "recording <i>“no psychological illness such as depression/psychosis”</i>. I place weight "
           "on that entry: it is contemporaneous, it is approximately seven months before the "
           "pleaded onset, and it records the absence of a depressive illness at that time. On the "
           "material available, attention deficit features and prior anxiety were present before "
           "2024; a depressive disorder was not. To the extent a pre-existing vulnerability existed, "
           "the matters described in the documents provided operated to produce a distinct depressive "
           "illness, and in the alternative aggravated that vulnerability materially.", BODY))
s.append(P("<b>1.4 Premorbid personality.</b> On my own assessment Mr Shepherd presents as "
           "conscientious and detail-oriented, with a marked orientation to procedural correctness. "
           "Those features are not of themselves pathological and do not displace the diagnosis. "
           "They are relevant to mechanism only in that an individual so oriented is likely to "
           "experience sustained distress where a system does not respond to procedural concerns.",
           BODY))
s.append(P("<b>1.5 Sources.</b> [A complete list would follow — the four attachments, the clinical "
           "file, and the consultation dates and durations.]", BODY))

s.append(P("MATTER 2 — DID THE INJURY ARISE OUT OF, OR IN THE COURSE OF, THE EMPLOYMENT?", SEC))
s.append(P("<b>2.1 The conditions of the work.</b> The role description provided records that the "
           "position requires continuous shift work across the full 24-hour period, seven days a "
           "week; participation in the Emergency Response process, distributing emergency "
           "notifications in accordance with code procedures and strictly adhering to protocols and "
           "timeframes; maintaining call queues to a minimum at all times; multitasking under "
           "pressure with high volume call traffic; the exercise of judgement where precedent has not "
           "been set and procedures are not defined; and work with limited supervision. The "
           "Regulator's response records that the accuracy of Switchboard information is critical to "
           "clinical handover and patient safety.", BODY))
s.append(P("Taken together these describe a role of <b>high psychological demand</b> combined with "
           "<b>low task control</b> — the occupant is required to exercise judgement in circumstances "
           "where procedures are not defined — and <b>limited supervisory support</b> by design. That "
           "combination is a recognised psychosocial hazard and is associated in the literature with "
           "the development of depressive and anxiety disorders. The requirement to act on emergency "
           "notifications within fixed timeframes, where error carries consequences for patient "
           "safety, adds a sustained element of anticipatory anxiety that is not typical of "
           "administrative work generally.", BODY))
s.append(P("<b>2.2 Fatigue and its management.</b> The letter of the Chief Executive records that no "
           "fatigue risk assessment applied to the position; that fatigue risk management was "
           "implemented at the Switchboard only after 30 June 2024; that complaints were managed "
           "solely by email or verbally; and that no consequential changes to operating procedures "
           "were made over the relevant period. Continuous rotating shift work across a 24-hour "
           "period produces circadian disruption and cumulative sleep debt. Where no fatigue "
           "management system operates, that burden is not identified, not measured and not "
           "controlled, and falls to be managed by the individual. Sustained unmanaged fatigue of "
           "that kind impairs emotional regulation, concentration and working memory, and is a "
           "recognised contributor to depressive illness.", BODY))
s.append(P("<b>2.3 The rostering of 17 to 18 March 2024.</b> The Regulator's response records a "
           "rostered break of 7 hours against a 10-hour minimum, described as a rostering error "
           "accidentally made. The Chief Executive's letter records that emergency (MET) calls were "
           "recorded on those shifts, and that leave was taken on 19 March 2024. A 7-hour interval "
           "between shifts permits, after travel and sleep latency, materially less than the sleep "
           "opportunity required for recovery. That the following day was taken as leave is "
           "consistent with an acute recovery requirement. I note that this episode occurred in a "
           "setting where, on the employer's own account, no fatigue assessment existed to identify "
           "it and no procedural change followed it.", BODY))

s.append(PageBreak())

s.append(P("MATTER 3 — WAS THE EMPLOYMENT A SIGNIFICANT CONTRIBUTING FACTOR?", SEC))
s.append(P("<b>3.1 Causation.</b> In my opinion, on the facts I have been asked to assume, "
           "Mr Shepherd's employment was <b>a significant contributing factor</b> to the Major "
           "Depressive Disorder with anxious distress from which he suffers, with onset in about "
           "mid-June 2024. My reasoning is as follows. First, the work as described by the employer "
           "carried a sustained combination of high demand, low control and limited support. Second, "
           "on the employer's own account the principal identified hazard of such work — fatigue — "
           "was neither assessed nor managed at any time before 30 June 2024. Third, the "
           "contemporaneous record establishes an absence of depressive illness in November 2023 and "
           "presentation with such illness by 1 July 2024. Fourth, the symptom picture at "
           "presentation and at my own assessment is of a kind produced by sustained occupational "
           "stress rather than by an endogenous process.", BODY))
s.append(P("I distinguish between the cause of onset and the subsequent course. The matters above "
           "bear on onset. Matters arising after October 2024, addressed at 3.3, bear on the course "
           "of the condition and on its persistence, not on its causation.", BODY))
s.append(P("<b>3.2 The interval.</b> I am asked whether the interval between the rostering of March "
           "2024 and onset in June 2024 is consistent with my formulation. It is. I do not regard "
           "the March episode as the cause of the condition. It is one documented instance of a "
           "continuing exposure — continuous shift work without any fatigue management — which on "
           "the employer's own account persisted unchanged until after 30 June 2024. Cumulative "
           "exposures of that kind do not produce illness on a fixed latency; they produce it when "
           "the individual's capacity to compensate is exceeded. On that analysis there is no "
           "interval requiring explanation. As to the interval between onset and first presentation, "
           "it is of the order of two weeks, which is short.", BODY))
s.append(P("<b>3.3 Other factors, placed in time.</b> My report of 13 February 2025 referred to "
           "multiple life stressors including relationship breakdown, job loss and bereavement. I am "
           "able to place these from my own file rather than by assumption, my clinical relationship "
           "with Mr Shepherd having commenced on 24 October 2024. Each of those matters arose after "
           "that date and therefore after the diagnosis was made and after onset. In my opinion they "
           "bear on the course and persistence of the condition and did not cause it. I note further "
           "that the cessation of employment was itself a consequence of the condition and its "
           "handling, and was subsequently reversed.", BODY))
s.append(P("[GAP — the file must in fact date these events. If it does not, the answer weakens to "
           "“after October 2024” without particulars.]", GAP))

s.append(P("<b>3.4 Prognosis and current capacity.</b> Prognosis is conditional. Mr Shepherd has "
           "shown capacity to work in his substantive role where predictable arrangements were in "
           "place. He is presently certified fit with restrictions. In my opinion any current "
           "incapacity is attributable in material part to the consequences of his exclusion from "
           "the workplace since 3 July 2026 — loss of income, loss of occupational role and absence "
           "of an end date — rather than to the condition operating alone.", BODY))
s.append(P("<b>3.5 Adjustments.</b> I consider the following clinically necessary: predictability of "
           "rostering, with rosters issued in advance and not altered without notice; a minimum "
           "recovery interval between consecutive shifts consistent with the applicable standard; "
           "limitation of sustained concurrent emergency-code load; and day-time hours during the "
           "period of recovery, with review at three months.", BODY))
s.append(P("<b>3.6 Inherent requirements.</b> ", QH))
s.append(P("[⛔⛔ THE PACK CANNOT ANSWER THIS AS IT STANDS. The role description states that the "
           "position <i>is a continuous shift working role</i> and that the occupant <i>must</i> be "
           "able to work a roster covering multiple shifts over a 24/7 period. If day hours and "
           "predictable rostering are clinically necessary, a clinician confined to the four "
           "attachments may be unable to say the inherent requirements can be met — which is the "
           "answer that supports a capacity separation.]", GAP))
s.append(P("[⭐ WHAT WOULD FIX IT — and it is all the employer's own material: the three "
           "reduced-hours arrangements approved by the Director on 27.02.2026, 17.04.2026 and "
           "09.06.2026; and the certificate of capacity of 3 July 2026, which records the "
           "arrangement as a <i>continuation of existing arrangement … worked and tolerated … "
           "without deterioration</i>. With those, the clinician can say the adjustment is not "
           "theoretical: it was granted three times and it worked.]", GAP))
s.append(P("<b>3.7–3.10 Exacerbating conditions, complaint handling, working memory, foreseeable "
           "risk.</b> [Answerable from the role description, the Chief Executive's letter and the "
           "13 February 2025 report. Working memory in particular is addressed in that report and "
           "can be expressed in functional terms against the duties described.]", BODY))

s.append(P("WHAT THE EXERCISE ESTABLISHES", SEC))
s.append(P("<b>The design works for Matters 1 and 2 and for questions 3.1 to 3.5.</b> Every element "
           "of the causation opinion above is drawn from the Regulator's admissions, the employer's "
           "two documents, or the clinical record. None of it requires Mr Shepherd's account of the "
           "workplace. The sentence <i>“my opinion does not depend on Mr Shepherd's account of these "
           "matters”</i> is available on this pack.", BODY))

s.append(P("⛔ THE THREE GAPS THE EXERCISE FOUND", SEC))
s.append(P("<b>1. The inherent-requirements question (3.6) cannot be answered safely.</b> The role "
           "description makes 24/7 shift work mandatory. ⭐ <b>ADD the three movement forms approved "
           "27.02, 17.04 and 09.06.2026.</b> They are the employer's own documents and they prove the "
           "adjustment was granted three times. Without them the strongest question in the pack is "
           "the weakest answered.", BODY))
s.append(P("<b>2. The intensity point is unavailable.</b> Nothing in the four attachments records "
           "call volumes. ⭐ <b>ADD the individual monthly statistics (April 2025)</b> — 269 to 444 "
           "calls per shift at approximately 29% of full time. Without them the clinician cannot "
           "address why reduced hours did not reduce intensity, and the “he kept working” point goes "
           "unanswered.", BODY))
s.append(P("<b>3. Nothing evidences that the duties are presently performed by another employee.</b> "
           "That rests on colleague report. ⚠ It is load-bearing for 3.6 and for the employer's own "
           "question about accommodation. <b>Obtain it in writing, or do not rely on it.</b>", BODY))
s.append(P("⚠ A fourth, smaller: 3.3 assumes the clinical file dates the personal matters. Confirm "
           "that it does.", BODY))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=16*mm, bottomMargin=16*mm,
                        title="WC/2024/227 — simulated report (internal stress test)",
                        author="Internal working document")

def footer(canv, d):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7.4)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(20*mm, 10*mm, "SIMULATION — NOT A REPORT — INTERNAL ONLY — NEVER TO BE SENT TO THE PRACTICE")
    canv.setFont('Helvetica', 7.4); canv.setFillColor(colors.HexColor('#777777'))
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()

doc.build(s, onFirstPage=footer, onLaterPages=footer)
print("built", OUT)
