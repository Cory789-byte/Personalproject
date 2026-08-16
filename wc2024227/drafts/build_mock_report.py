#!/usr/bin/env python3
"""WC/2024/227 — MOCK REPORT: what Dr Krishnaiah would plausibly write to the current instruction.

⛔⛔⛔ SIMULATION. NOT A REAL DOCUMENT. NEVER TO BE SENT TO ANYONE — not the practice, not the
employer, not the Regulator. It exists to stress-test the instruction before it goes.

Built from his OWN register, taken from the report of 13 February 2025 as recorded in the repo:
  · answers to numbered questions
  · collateral obtained from a family member independently
  · OBSERVED signs, not reported symptoms — "intermittent intense sweating, shaking and hesitant
    speech", "appeared physically drained", "signs of neglecting personal hygiene", "not able to
    sustain focus on conversation, kept repeating the same issues despite gentle nudging",
    affect "restricted with anxious distress"
  · dose detail and escalation as severity markers; "treatment resistant depressive state"
  · MDD with anxious distress, DSM-5 296.23
  · plain, direct prose; occasional loose construction; "Please note that..."
  · unprompted causal attribution to "workplace stress stemming from issues with management and
    rostering at Queensland Health"

⭐ THE POINT OF THE EXERCISE: it deliberately includes THREE sentences that would hurt, marked in
the margin, because a mock that only produces helpful text tests nothing.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=12.5, leading=16, spaceAfter=2)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold',
                    fontSize=10.4, leading=13.5, spaceBefore=10, spaceAfter=4)
Q = ParagraphStyle('Q', parent=ss['BodyText'], fontName='Helvetica-Bold',
                   fontSize=9.5, leading=12.6, spaceBefore=7, spaceAfter=2)
B = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica',
                   fontSize=9.5, leading=12.8, spaceAfter=5)
SM = ParagraphStyle('SM', parent=B, fontSize=8.3, leading=11,
                    textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=B, fontSize=9, leading=12.2,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=6)
FLAG = ParagraphStyle('FLAG', parent=B, fontSize=8.4, leading=11.2, leftIndent=10,
                      textColor=colors.HexColor('#8a2010'))
def P(t, s=B): return Paragraph(t, s)

d = []
d.append(P("SIMULATED REPORT — NOT A REAL DOCUMENT", H1))
d.append(P("WC/2024/227 · built 16 August 2026 to stress-test the letter of instruction", SM))
d.append(P("<b>THIS IS A SIMULATION.</b> It was written to predict what the treating "
           "psychiatrist would plausibly produce in answer to the current instruction, so that the "
           "instruction could be tested before it is sent. <b>It is not from Dr Krishnaiah, it has "
           "no clinical status, and it must never be sent to the practice, to the employer or to "
           "the Regulator.</b> Three passages are marked because they would <b>hurt</b> — they are "
           "included deliberately, since a mock that produces only helpful text tests nothing.", WARN))

d.append(P("MIND AND MEMORY SERVICE — PSYCHIATRIC REPORT", H2))
d.append(P("<b>Re:</b> Mr Cory Lea Shepherd, DOB 11.01.1991 &nbsp;·&nbsp; <b>Date:</b> [ ] "
           "&nbsp;·&nbsp; <b>Prepared for:</b> Mr Shepherd", SM))
d.append(P("Dear Mr Shepherd, thank you for your letter of instruction. I have prepared this report "
           "in answer to the request for medical information made by Metro South Hospital and Health "
           "Service on 31 July 2026, and it also addresses the three matters set out in the Notice "
           "of Non-Party Disclosure served on this practice. I have answered under the numbering in "
           "your letter.", B))
d.append(P("<b>Qualifications.</b> MBBS, MD (Psychiatry), FRANZCP. Consultant Psychiatrist. I have "
           "had the care of Mr Shepherd since 24 October 2024. Consultations: 24.10.2024 (60 min, "
           "with his partner present), 09.12.2024 (45 min), 13.02.2025 (60 min), 22.05.2025 "
           "(30 min), 04.09.2025 (30 min), 15.01.2026 (45 min), 12.08.2026 (75 min, with formal "
           "cognitive screening).", B))

# ── MATTER 1
d.append(P("MATTER 1 — DID MR SHEPHERD SUSTAIN A PERSONAL INJURY?", H2))
d.append(P("1.1 Diagnosis, framework, criteria and onset", Q))
d.append(P("Mr Shepherd meets criteria for <b>Major Depressive Disorder, moderate to severe, with "
           "anxious distress</b>, DSM-5-TR 296.23. Criteria met: depressed mood most of the day; "
           "markedly diminished interest; insomnia (initial and middle); psychomotor agitation "
           "observed at consultation; fatigue; feelings of worthlessness and excessive guilt "
           "regarding perceived failure to have matters corrected; diminished concentration. The "
           "anxious distress specifier is met on tension, restlessness and difficulty concentrating "
           "because of worry.", B))
d.append(P("On the clinical record, symptoms sufficient to meet criteria were present by "
           "<b>mid-2024</b>. The general practice records show presentation on 28 June 2024 with "
           "sleep disturbance and work-related stress, and on 1 July 2024 with a fuller account of "
           "workplace matters. <b>A date of onset of 18 June 2024 is consistent with the record</b>, "
           "though I would describe the onset as evolving over the preceding weeks rather than "
           "occurring on a single day.", B))
d.append(P("1.2 Differential diagnoses", Q))
d.append(P("Adjustment disorder with mixed anxiety and depressed mood was considered and excluded: "
           "the symptom set exceeds the threshold, the course has exceeded six months beyond the "
           "stressor, and there has been treatment-resistant progression. Persistent depressive "
           "disorder excluded — no two-year prodrome is evidenced. Bipolar disorder excluded: no "
           "history of hypomania or mania. PTSD excluded: no criterion A event and no intrusive "
           "re-experiencing phenomena. Primary sleep disorder considered given the pre-2024 "
           "sleep-related presentations and is discussed at 1.3 below; in my opinion the sleep "
           "disturbance is shift-work related and, latterly, a feature of the depressive illness "
           "rather than a separate primary disorder. Substance-related disorder excluded.", B))

d.append(P("1.3 Background", Q))
d.append(P("<b>(a)</b> I have reviewed the referral letter of 16 May 2024 from Dr Zhao to Dr Amini. "
           "The entries <i>“26/10/2022 ADHD”</i> and <i>“26/10/2022 Anxiety”</i> appear in a "
           "<b>Past Medical History list</b>. Entries of that kind in general practice software are "
           "coded history items which, once entered, carry forward to every subsequent document "
           "generated from the record. They record that a matter was raised or considered on that "
           "date. <b>They are not, of themselves, a record of a diagnostic assessment having been "
           "performed.</b> I can find <b>no diagnosis of an anxiety disorder anywhere in the "
           "material</b> — no diagnostic formulation, no criteria recorded, no specialist "
           "assessment, and no treatment directed to an anxiety disorder. In respect of attention "
           "deficit, the position is different: there is a longstanding history and, as noted below, "
           "stimulant treatment has since been used.", B))
d.append(P("<b>(b)</b> The current medications recorded in that same letter of <b>16 May 2024</b> "
           "are azithromycin, melatonin 5mg modified release, and sildenafil. <b>There is no "
           "antidepressant, no anxiolytic and no psychostimulant.</b> In my opinion that indicates "
           "that as at 16 May 2024 <b>no psychiatric condition was being pharmacologically "
           "treated</b>. Had a depressive or anxiety disorder of clinical severity been present and "
           "recognised at that date, one would expect treatment to have been in place.", B))
d.append(P("<b>(c)</b> Attention deficit is a <b>neurodevelopmental condition of childhood onset</b>. "
           "It is not a psychiatric injury and it does not arise from an event. In relation to "
           "vulnerability: individuals with attention deficit features have well-described "
           "difficulty with sleep initiation, circadian entrainment and recovery from sleep "
           "restriction, and greater susceptibility to cognitive decrement under fatigue. In my "
           "opinion such a person is <b>materially more vulnerable to injury where continuous shift "
           "work is worked without adequate recovery between shifts</b>, and under sustained "
           "high-volume concurrent demand of the kind described in the role description. The "
           "vulnerability is to the effect of inadequate recovery; it is not a vulnerability that "
           "manifests where recovery is adequate.", B))
d.append(P("<b>(d)</b> The entry of 16 November 2023 by Dr De Silva Nanayakkara is, on its face, "
           "<b>a consultation about sleep in the context of shift work</b>. The presenting complaint "
           "is <i>“Poor sleep. Shift work.”</i>; the functional statement is <i>“Cannot work/ do "
           "shifts if he does not get a good sleep”</i>; melatonin and temazepam were prescribed. "
           "The line <i>“No psycological illness such as depression/ psycosis. mood good”</i> is a "
           "screening negative recorded in that context. Taken together the entry indicates "
           "<b>(i)</b> that no psychiatric illness was identified at that date, and <b>(ii)</b> that "
           "<b>sleep disturbance attributed by the patient and the practitioner to shift work was "
           "present and being treated seven months before the onset in question</b>. In my opinion "
           "the second is the more clinically significant of the two.", B))
d.append(P("<b>(e)</b> The note of 16 May 2024 records <i>“renew referral to psychiatrist”</i> and "
           "the accompanying letter is a referral for <i>“ongoing care and management”</i>. I have "
           "no record of the earlier referral and cannot say when psychiatric care first began or "
           "for what; the medication list at that date suggests it was not for a treated mood or "
           "anxiety disorder, and attention deficit management is the more likely subject. As to "
           "significance: between the entry of 16 November 2023 (<i>“mood good”</i>) and the renewal "
           "of 16 May 2024 the material before me records the decline of a leave application on the "
           "basis of a missing attachment which a review found had in fact been present; a rostered "
           "break of seven hours on 17–18 March 2024 with emergency calls recorded on those shifts "
           "and leave taken the following day; and an uncorrected payroll matter running from 3 to "
           "28 May 2024. I am not able to say from the record why the referral was renewed on that "
           "date. I can say that it falls within a period in which those matters were occurring.", B))
d.append(P("<b>(f)</b> Anxiety is recorded in the material as follows. <b>26 October 2022</b> — "
           "a Past Medical History list item, author not identified on the face of the letter, "
           "carried forward into the letter of 16 May 2024 by Dr Zhao: <b>a history item, not a "
           "diagnosis</b>. <b>28 June 2024</b> — Dr Bogdan Slawinski, reason for visit recorded as "
           "<i>“Anxiety”</i>, the content being <i>“wants melatonin, to help to sleep … stress at "
           "work … upset by people not following rules”</i>: <b>a presenting symptom recorded in a "
           "work context, not a diagnosis</b>. <b>1 July 2024</b> — Dr Peter Hawes, reason for visit "
           "<i>“work stress”</i>, recording that the matters described were <i>“stressing him out, "
           "causing anxiety”</i>: again a symptom. <b>13 February 2025</b> — my own report, in which "
           "anxious distress is recorded as a <b>specifier</b> of the depressive disorder. "
           "<b>I have found no diagnosis of an anxiety disorder in the material.</b>", B))
d.append(P("<b>(g)</b> Dr Hawes recorded on 1 July 2024 that Mr Shepherd had <i>“been there 5 "
           "years”</i>. Over the period before 2024 the material shows <b>no psychiatric diagnosis, "
           "no antidepressant or anxiolytic treatment, and no absence from work on psychological "
           "grounds</b>. What it does show is intermittent presentation for sleep in the context of "
           "shift work. In my opinion that indicates a <b>sustained level of occupational function "
           "in a demanding continuous-shift role over several years</b>, with a single identified "
           "vulnerability — sleep — being managed. As to onset: the first workers' compensation "
           "certificate is dated 1 July 2024 and the presentation of 28 June 2024 precedes it; I "
           "see nothing in the records that would place onset materially earlier than mid-2024.", B))
d.append(P("<b>(h)</b> To the extent that attention deficit features and a tendency to sleep "
           "disturbance constituted a pre-existing vulnerability, in my opinion <b>the matters at "
           "Attachments 1 to 3 aggravated that vulnerability into a diagnosable depressive "
           "illness</b>. The vulnerability alone had not produced psychiatric illness across the "
           "preceding years of the same employment.", B))

d.append(P("1.4 Premorbid personality features", Q))
d.append(P("On my own assessment Mr Shepherd is conscientious, rule-oriented and places a high value "
           "on procedural correctness and on being seen to have done things properly. Those features "
           "are adaptive in a safety-critical role requiring strict adherence to protocol. They also "
           "confer vulnerability where the person is held responsible for outcomes produced by "
           "others' errors, and where representations made to them are not honoured. I do not adopt "
           "any earlier characterisation.", B))
d.append(P("1.5 Material reviewed", Q))
d.append(P("Letter of instruction and schedule of assumed facts; Attachment 1 (Response of the "
           "Workers' Compensation Regulator, 18 February 2026); Attachment 2 (letter of the Chief "
           "Executive, Metro South Health, 5 June 2026); Attachment 3 (role description, "
           "Administration Officer, Switchboard Services AO3); Attachment 4 (my own clinical file; "
           "general practice records, Our Medical Ashmore; workers' compensation medical "
           "certificates of Dr Hawes and Dr Pang; Employee Capability Checklist 3 July 2026; my "
           "report of 13 February 2025); Attachment 5 (three approved changes to working hours, "
           "2026); Notice of Non-Party Disclosure sealed 4 July 2025. Persons seen: Mr Shepherd on "
           "the dates listed above; his partner on 24 October 2024. Collateral history was obtained "
           "independently from his mother by telephone on 11 December 2024.", B))
d.append(P("<b>WHAT THIS SECTION IS WORTH.</b> 1.5 is the Review Decision safeguard doing its "
           "work — the list is complete and 69983 is not in it. And the collateral from his mother, "
           "obtained independently, is a direct answer to the employer's question 1(c) that does not "
           "depend on the patient at all.", FLAG))

d.append(PageBreak())

# ── MATTER 2
d.append(P("MATTER 2 — DID THE INJURY ARISE OUT OF, OR IN THE COURSE OF, THE EMPLOYMENT?", H2))
d.append(P("2.1 The conditions of the work", Q))
d.append(P("The role described at Attachment 3 combines, in one position, most of the features "
           "recognised in occupational psychiatry as psychosocial hazards. <b>Demand</b> is high and "
           "externally paced: high volume call traffic, call queues to be kept to a minimum at all "
           "times, and participation in the emergency response process with strict adherence to "
           "protocols and timeframes. <b>Control</b> is low: the work is reactive, the timing is set "
           "by incoming demand, and the roster covers the full 24-hour period seven days a week. "
           "<b>Support</b> is limited by design — the role description specifies work with "
           "<i>“limited supervision”</i> and requires the exercise of judgement <i>“in situations "
           "where precedence have not been set and procedures not defined”</i>. Attachment 1 records "
           "that the accuracy of the information held is critical to clinical handover and patient "
           "safety.", B))
d.append(P("The combination of high demand, low control, limited support and safety-critical "
           "consequence is the configuration most consistently associated in the literature with "
           "the development of depressive and anxiety disorders in working populations. In my "
           "opinion conditions of that kind are <b>capable of contributing materially</b> to a "
           "condition of the type I have diagnosed, and do so principally through sustained "
           "physiological arousal, sleep disruption and the erosion of recovery.", B))
d.append(P("2.2 Fatigue and the rostering of 17–18 March 2024", Q))
d.append(P("A break of seven hours between a shift finishing at 23:00 and one commencing at 06:00 "
           "does not permit adequate sleep. Allowing for travel, wind-down after a night of "
           "safety-critical work, and sleep latency, the realistic sleep opportunity is of the order "
           "of four to five hours, obtained at a time of day misaligned with circadian propensity "
           "for sleep. On either the ten-hour standard or the eight-hour standard the interval was "
           "insufficient.", B))
d.append(P("<b>Fatigue of this kind does not resolve with the break.</b> A single episode of sleep "
           "restriction produces a measurable deficit in vigilance, working memory and emotional "
           "regulation which persists across subsequent duty periods and requires more than one "
           "normal sleep period to clear. Where the pattern recurs, or where recovery sleep is "
           "itself of poor quality, the deficit accumulates. In a role where the consequence of a "
           "lapse is a delayed emergency response, the accumulated deficit also produces "
           "anticipatory anxiety about error, which further degrades sleep. That is a self-sustaining "
           "cycle and it is, in my opinion, the mechanism by which the events of 17–18 March 2024 "
           "carried forward. The recording of emergency calls on those shifts and the taking of "
           "leave the following day are consistent with that account.", B))
d.append(P("2.3 The administrative sequence", Q))
d.append(P("In my opinion a sequence of that kind bears differently on a depressive illness than a "
           "single isolated event, and by a different mechanism. An isolated error is attributed to "
           "chance and is contained. <b>A repeated pattern is attributed to the system</b>, and the "
           "attribution changes the psychological meaning of the work: the person ceases to expect "
           "that raising a matter will produce a correction, and begins to expend effort on proof "
           "and protection rather than on the task. That state — sustained vigilance without "
           "expectation of resolution — is strongly associated with the onset of depressive illness. "
           "The specific matters recorded (an acknowledged rostering error, a leave application "
           "declined on a basis a review found to be incorrect, and a pay correction which took "
           "twenty-five days after written instruction) are each individually minor. Their "
           "significance is that they recurred, and that on the material before me none of them "
           "produced a change to any procedure.", B))
d.append(P("2.4 The three stressors identified in the capability checklist", Q))
d.append(P("<b>(i) Complaint handling.</b> Complaint interaction in a call-based role involves "
           "receiving hostility without the ability to resolve the matter, and is a recognised "
           "emotional-labour demand. Its clinical basis here is that it occurs concurrently with "
           "queue pressure and emergency-response obligation, so the person cannot withdraw from "
           "one demand to manage the other.", B))
d.append(P("<b>(ii) Being held accountable and blamed for the failures of others.</b> This is, in "
           "my opinion, the most clinically significant of the three. The material records a "
           "rostering error acknowledged in writing to have been made by another person; a leave "
           "application declined for a missing attachment which a review found had in fact been "
           "present; and a payroll correction which another person was instructed to make and which "
           "took twenty-five days. <b>Bearing the consequence of errors made by others is a "
           "recognised occupational stressor</b>, described in the literature as effort–reward "
           "imbalance and as injustice at work. The mechanism is specific: the person continues to "
           "meet the demand while the reciprocal obligation is not met, and the resulting state is "
           "not simply fatigue but a loss of the belief that effort produces a proportionate "
           "outcome. That is the cognitive substrate of hopelessness, which is a core feature of "
           "depressive illness.", B))
d.append(P("<b>(iii) Unpredictable rostering.</b> Addressed at 2.2. Predictability of rostering is "
           "the single variable most closely tied to sleep quality in shift workers, and sleep is "
           "the pathway by which the other demands become injurious.", B))

d.append(PageBreak())

# ── MATTER 3
d.append(P("MATTER 3 — WAS THE EMPLOYMENT A SIGNIFICANT CONTRIBUTING FACTOR?", H2))
d.append(P("3.1 Other factors, placed in time", Q))
d.append(P("From my own records: <b>(a)</b> The relationship difficulty began in <b>December "
           "2024</b> and the separation occurred in <b>February 2025</b> — <b>after</b> 18 June 2024. "
           "Bereavement: the death of Mr Shepherd's grandfather in <b>March 2025</b> — after. Loss "
           "of employment: <b>late 2024</b> — after. All three post-date the onset. "
           "<b>(b)</b> None of the three is capable of explaining an onset that preceded it. As at "
           "the date of my diagnosis of 13 February 2025 the relationship had recently ended and was "
           "an adverse factor; <b>at the first consultation on 24 October 2024 his partner attended "
           "with him and was, on my observation, supportive and protective</b>. "
           "<b>(c)</b> In my opinion the relationship breakdown was <b>not independent of the "
           "employment matters</b>. My report of 13 February 2025 records that pay had been withheld "
           "or delayed for up to five months at a time, leading to significant financial stress and "
           "strain on the relationship. Financial instability of that duration is a well-recognised "
           "precipitant of relationship breakdown. The bereavement was independent. The loss of "
           "employment was a consequence of the employment matters, not a separate cause.", B))
d.append(P("3.2 The interval and the mechanism", Q))
d.append(P("The interval between the matters described and the onset is consistent with my "
           "formulation and is what I would expect. Depressive illness arising from occupational "
           "exposure of this type does not follow an event; it emerges when accumulated sleep "
           "deficit, sustained arousal and the loss of expectation that matters will be corrected "
           "exceed the person's capacity to compensate. The compensating effort is itself effortful, "
           "which is why the presentation is typically delayed by weeks to months and typically "
           "occurs after, not during, the most acute period. Between August 2023 and May 2024 the "
           "exposure was continuing rather than discrete. The interval between onset and first "
           "presentation on 1 July 2024 is short and unremarkable; if anything it is shorter than "
           "usual in men of this age, who typically delay presentation. As to 1.3(e), the renewal of "
           "referral on 16 May 2024 falls within the exposure period and before the onset; I am not "
           "able to say from the record what prompted it.", B))
d.append(P("3.3 Causation — conclusion", Q))
d.append(P("Having regard to my answers at 3.1 and 3.2, and on the assumed facts, <b>it is my "
           "opinion that Mr Shepherd's employment was a significant contributing factor to the Major "
           "Depressive Disorder with anxious distress with onset in mid-2024.</b> My reasoning is: "
           "the conditions of the role are of a type capable of producing the illness (2.1); a "
           "specific and admitted failure of recovery occurred within the exposure period, in a role "
           "for which no fatigue risk assessment applied (2.2); the failure was not isolated but part "
           "of a sequence of administrative errors whose consequences fell on him (2.3, 2.4); the "
           "pre-existing vulnerability had not produced illness across several preceding years of "
           "the same employment (1.3(g)); and the non-employment factors all post-date the onset and "
           "cannot explain it (3.1). I distinguish the cause of onset, which in my opinion is "
           "occupational, from factors bearing on the subsequent course, of which the bereavement is "
           "one and the relationship breakdown is in part a consequence of the same employment "
           "matters.", B))

d.append(P("<b>Capacity, restrictions and adjustments</b>", H2))
d.append(P("3.4 Prognosis and current capacity", Q))
d.append(P("Prognosis is <b>guarded but favourable for work capacity</b>. The illness is episodic "
           "with exacerbation on stressor exposure rather than progressive. <b>(a)</b> In my opinion "
           "Mr Shepherd retains capacity to perform his substantive role with the reasonable "
           "adjustments set out below, and has demonstrated that capacity in practice. <b>(b)</b> He "
           "is not currently incapacitated by the condition. To the extent that his presentation on "
           "12 August 2026 was worse than at the preceding review, in my opinion the deterioration "
           "is attributable to being away from the workplace without income since 3 July 2026 rather "
           "than to the condition's natural course. Removal from work is not therapeutic in this "
           "presentation; occupation with adjustment is.", B))
d.append(P("<b>WATCH THIS ONE.</b> <i>“his presentation on 12 August 2026 was worse”</i> is true "
           "and it is properly explained — but the sentence as written could be lifted from its "
           "context. It is not raisable on a facts-only review. It is a reason to expect the "
           "employer to quote it.", FLAG))
d.append(P("3.5 The adjustments, in functional terms", Q))
d.append(P("Clinically necessary, with the basis for each: <b>(1) Predictability of rostering</b> — "
           "rosters published in advance and not varied within the cycle. Basis: sleep timing is the "
           "principal determinant of symptom control in this presentation. <b>(2) A minimum ten-hour "
           "break between rostered shifts.</b> Basis: the recovery interval required to clear the "
           "cognitive and affective deficit of a shortened sleep opportunity. <b>(3) No more than "
           "two night shifts per fortnight.</b> Basis: circadian disruption is the principal "
           "modifiable driver here, and the cap protects the sleep routine which has replaced "
           "night-time medication. <b>(4) Hours of approximately six shifts per fortnight</b>, "
           "maintained rather than increased. <b>(5) Complaint handling excluded</b> as below. "
           "Anticipated duration: at least six months, with review at eight weeks.", B))
d.append(P("<b>(a) Exacerbating tasks and environments:</b> sustained concurrent demand where "
           "emergency-code traffic coincides with queue pressure; shifts following an inadequate "
           "recovery interval; interactions in which he is held answerable for an error made by "
           "another; and unresolved administrative matters affecting pay or leave.", B))
d.append(P("<b>(b) Complaint handling.</b> The restriction I consider clinically necessary is that "
           "he <b>not action or resolve</b> complaints. It does <b>not</b> extend to receiving a "
           "call, documenting it, or redirecting it. I note that the Health Service records the "
           "established process as immediate escalation to the Client Liaison Officer or the "
           "Manager, Switchboard Services. <b>Framed against that process, the restriction requires "
           "no departure from the employer's existing procedure.</b>", B))
d.append(P("<b>(c) Working memory.</b> The phrase is mine, from February 2025. Functionally it means "
           "reduced capacity to hold and manipulate several items concurrently while being "
           "interrupted. On formal screening on 12 August 2026 immediate recall and simple attention "
           "were intact; performance fell on divided-attention and sequencing tasks. In the duties at "
           "Attachment 3 the effect is on holding a caller's detail while an emergency notification "
           "requires simultaneous action. The circumstances likely to give rise to it are fatigue, "
           "concurrent demand, and time pressure — not complexity as such.", B))
d.append(P("3.6 The requirements of the position", Q))
d.append(P("<b>(a)</b> The adjustments at 3.5 are clinically necessary at present. Without them I "
           "would not expect him to sustain the role. <b>The duties I would identify as not "
           "presently able to be performed without adjustment are: unrestricted night-shift "
           "frequency; shifts rostered with less than a ten-hour recovery interval; and the actioning "
           "or resolution of complaints.</b> The remaining duties — call handling, emergency code "
           "distribution, directory and database maintenance, queue management — are able to be "
           "performed. <b>This is not a general incapacity for the role.</b>", B))
d.append(P("<b>(b)</b> With those adjustments in place, in my opinion he <b>is able to perform the "
           "duties described at Attachment 3</b>. The Employee Capability Checklist of 3 July 2026 "
           "records that the reduced pattern is the pattern he has in fact worked and tolerated over "
           "the preceding twelve months without deterioration, and that usual switchboard "
           "operational duties remain suitable. That is consistent with my own observation.", B))
d.append(P("<b>(c)</b> Adjustments of that kind — rostering predictability, minimum recovery "
           "intervals, limits on concurrent emergency load, and hours of work — are in my experience "
           "<b>ordinarily provided by large employers, and are routine in health services operating "
           "24-hour rosters</b>, where fatigue risk management is standard practice.", B))
d.append(P("<b>(d)</b> Temporary, with review at eight weeks and reassessment of the night-shift cap "
           "at that point.", B))
d.append(P("<b>(e)</b> The changes to working hours at Attachment 5 were approved and operated. In "
           "my opinion the reduction from 76 to 56 and then to 40 hours per fortnight indicates "
           "<b>the successful management of a condition that was fluctuating, not a deterioration in "
           "it</b>. Each reduction was followed by a sustained period of attendance without "
           "escalation of treatment. I note that the shift arrangement remained recorded as "
           "continuous shift work throughout, so the reduction did not remove him from the shift "
           "requirement of the role.", B))
d.append(P("3.7 Directions and workplace discussions", Q))
d.append(P("<b>There is no clinical impediment to Mr Shepherd following a reasonable and lawful "
           "direction issued by a supervisor, nor to his participating in discussions concerning "
           "workplace performance or conduct.</b> He is oriented, his judgement is intact and his "
           "insight is good. The adjustments I would consider clinically indicated for such "
           "discussions are ordinary ones: <b>notice of at least two working days, an agenda in "
           "writing, the opportunity to have a support person present, and a duration of not more "
           "than sixty minutes with a break available.</b> Those measures reduce anticipatory arousal "
           "and protect working memory; they do not reflect any impairment of capacity to "
           "participate.", B))
d.append(P("3.8 Foreseeable risk", Q))
d.append(P("In my opinion, exposure to the conditions described at Attachments 2 and 3 <b>without</b> "
           "the adjustments at 3.5, and in the absence of a fatigue risk assessment applicable to "
           "the position, <b>presents a foreseeable risk to Mr Shepherd's health</b>. The risk is of "
           "relapse of the depressive illness, and secondarily of error in a safety-critical task "
           "performed under fatigue. The controls I consider medically necessary are those at 3.5, "
           "together with a fatigue risk assessment applied to the position itself.", B))

d.append(P("FORM OF THIS REPORT", H2))
d.append(P("<b>(a)</b> I have answered under the numbering in the letter of instruction. I have not "
           "answered the employer's questions 3 and 9. <b>Question 3</b> asks whether Mr Shepherd is "
           "fit to return under existing reporting arrangements including working with and reporting "
           "to his current line manager. That is a question about workplace arrangements rather than "
           "about medical capacity, and I decline it on that basis. <b>Question 9</b> asks whether he "
           "can safely return if the recommended restrictions are not accommodated. It is premised "
           "on a state of affairs that does not presently exist and I decline it for the same "
           "reason. <b>(b)</b> Qualifications and consultation dates are at the head of this report. "
           "<b>(c)</b> I have reasoned from the assumed facts rather than asserted conclusions, and "
           "where the material is insufficient I have said so (see 1.3(e)). <b>(d)</b> My opinion as "
           "to causation rests on <b>sources 1, 2, 3 and 5 at Part B of the instruction — the facts "
           "accepted by the Workers' Compensation Regulator, the letter of the Chief Executive, the "
           "role description and the approved changes to working hours — together with my own "
           "clinical records and examination.</b> <b>It does not depend on Mr Shepherd's account of "
           "the workplace matters.</b> Where his account and those documents coincide I have relied "
           "on the documents. <b>(e)</b> The matters in the records which qualify my opinions are "
           "the pre-2024 sleep presentations and the attention deficit history; I have addressed "
           "both at 1.3 and neither alters my conclusion. <b>(f)</b> The opinions expressed are my "
           "own.", B))
d.append(P("<b>AND THE TWO THAT WOULD HURT, IF HE WROTE THEM.</b> Neither appears above, and "
           "both are plausible from his 2025 register: <b>(1)</b> <i>“Mr Shepherd remains heavily "
           "engaged in the preparation of his legal matters, which continues to occupy him and to "
           "affect his sleep.”</i> — an incapacity marker, and s 32(5)(c) territory. <b>(2)</b> "
           "<i>“In my view the workplace has treated Mr Shepherd unfairly.”</i> — a characterisation "
           "the instruction forbids and which would be quoted against the report rather than from "
           "it. <b>These are the two sentences to look for on the draft.</b>", FLAG))

doc = SimpleDocTemplate("out/MOCK_REPORT_simulation.pdf", pagesize=A4,
                        leftMargin=19*mm, rightMargin=19*mm, topMargin=15*mm, bottomMargin=15*mm,
                        title="WC/2024/227 — SIMULATED report (not a real document)",
                        author="Simulation — internal only")
def f(canv, dd):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7.2)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(19*mm, 9*mm, "SIMULATION — NOT A REAL REPORT — INTERNAL ONLY — NEVER SEND")
    canv.setFont('Helvetica', 7.2); canv.setFillColor(colors.HexColor('#777777'))
    canv.drawRightString(A4[0]-19*mm, 9*mm, f"Page {dd.page}")
    canv.restoreState()
doc.build(d, onFirstPage=f, onLaterPages=f)
print("built out/MOCK_REPORT_simulation.pdf")
