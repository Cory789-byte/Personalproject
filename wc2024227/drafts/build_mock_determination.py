#!/usr/bin/env python3
"""WC/2024/227 - MOCK DETERMINATION. Internal. Not for service or filing. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak

BODY = ParagraphStyle('B', fontName='Helvetica', fontSize=9.6, leading=12.6, spaceAfter=5)
HD   = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11, textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2  = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=6)
TITLE= ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
SUB  = ParagraphStyle('S', fontName='Helvetica-Oblique', fontSize=8.4, leading=11, textColor=colors.HexColor('#555555'), spaceAfter=8)
H1   = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=11, leading=14, spaceBefore=9, spaceAfter=4)
H2   = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=9.8, leading=12.6, spaceBefore=6, spaceAfter=3)
NUM  = ParagraphStyle('N', parent=BODY, leftIndent=9*mm, firstLineIndent=-9*mm)
CELL = ParagraphStyle('C', parent=BODY, fontSize=8.3, leading=10.4, spaceAfter=0)
CELLB= ParagraphStyle('CB', parent=CELL, fontName='Helvetica-Bold')
WARN = ParagraphStyle('W', parent=BODY, fontName='Helvetica-Bold', textColor=colors.HexColor('#8B0000'))
def P(t, s=BODY): return Paragraph(t, s)
n=[0]
def N(t):
    n[0]+=1; return Paragraph(f"<b>[{n[0]}]</b>&nbsp;&nbsp;{t}", NUM)
def C(t): return Paragraph(t, CELL)

s=[]
s += [P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", HD),
      P("Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)", HD2),
      P("MOCK DETERMINATION", TITLE),
      P("How the Commission would reason this appeal on the present record. Prepared 6 September 2026 for the Appellant's own "
        "preparation. INTERNAL. Not for filing or service. Every authority cited is to be verified against the primary report "
        "before any use in a filing; verification status is stated in Part H.", SUB),
      P("The Commissioner who hears the appeal will not be Commissioner Dwyer, who chaired the 13 March 2026 conference "
        "(QIRC Workers' Compensation Appeal Guide, 5.1). This determination is written as a Commissioner would write it, "
        "in the order the decided cases use: injury, significant contributing factor, section 32(5)(a), section 32(5)(b) and "
        "(c), orders. It assumes the evidence as it now stands: the served Notice admitted or deemed admitted under rule 49, "
        "the treating records, the Review Decision, the Appellant's outline of evidence, his filed affidavit of June 2026, "
        "and oral evidence from the Appellant, Ms Taylor and Ms Reese. It assumes no expert report on either side.", WARN)]

s.append(P("PART A. THE APPEAL AND THE ISSUES", H1))
s.append(N("Mr Shepherd appeals under s 549 of the <i>Workers' Compensation and Rehabilitation Act 2003</i> against Review "
  "Decision 69983 dated 24 October 2024, which confirmed WorkCover Queensland's rejection of his application for compensation "
  "lodged 1 July 2024. The hearing is de novo (s 550(4)). The Commission decides the matter afresh on the evidence before it; "
  "the review officer's reasoning binds no one, although her findings are before me as an admitted document."))
s.append(N("The Appellant bears the onus on the balance of probabilities of establishing that he sustained an injury within "
  "s 32, including that the injury is not excluded by s 32(5): <i>Davis v Blackwood</i> [2014] ICQ 9. The Respondent's own "
  "pleading at paragraph 5 puts it the same way, and the Appellant does not contest it. I note that the Appellant's filed "
  "affidavit of June 2026 at paragraph 2 asserts that the s 32(5)(a) exclusion is for the Respondent to establish. That is not "
  "the law, and nothing turns on it, because the Appellant has approached the hearing as though the onus were his."))
s.append(N("The issues, in the order the authorities require, are: (a) whether the Appellant suffered a personal injury that is "
  "a psychiatric or psychological disorder; (b) whether it arose out of, or in the course of, his employment; (c) whether "
  "employment was a significant contributing factor to it; (d) whether it arose out of reasonable management action taken in a "
  "reasonable way (s 32(5)(a)); (e) whether it arose out of his expectation or perception of reasonable management action "
  "(s 32(5)(b)); and (f) whether it arose out of action by WorkCover in connection with the application (s 32(5)(c))."))

s.append(P("PART B. THE EVIDENCE, AND HOW I APPROACH IT", H1))
s.append(N("<b>The admitted documents.</b> The Appellant served a notice to admit facts under r 49 on 28 August 2026 containing "
  "303 facts, each a fact about a document in an annexure of 133 pages, and a notice to admit documents. On the response, or "
  "on the deeming under r 49 in the absence of one, the great majority of those facts are admitted. They are facts about what "
  "documents say and when they were sent. They do not admit any characterisation, and the Appellant asked for none. I have "
  "treated them as what they are: an agreed documentary record. That record is unusually complete and unusually well ordered, "
  "and it has meant that the contest at hearing was about inference and law, not about what happened."))
s.append(N("<b>The Review Decision.</b> The Respondent admitted the contents of Review Decision 69983 in February 2026 while "
  "reserving its relevance. It is relevant in two ways. First, it records findings made by the Respondent's own delegate on the "
  "medical material then before her: that the Appellant sustained a personal injury of a psychological nature; that employment "
  "was a significant contributing factor; that Dr Hawes told WorkCover on 2 September 2024 that work events were the sole cause; "
  "and that the rostering of 17 and 18 March 2024 was unreasonable management action (pp 16, 26 to 27). Second, it records the "
  "reasoning by which she nonetheless excluded the injury, which I address in Part E. I am not bound by any of it. I give the "
  "findings the weight of a careful contemporaneous assessment made on a fuller medical file than the Regulator has chosen to "
  "put before me, and I note that the Respondent has called no medical witness to contradict them."))
s.append(N("<b>The treating records.</b> The general-practice file to 1 July 2024, the Hawes certificates of 1 July, 11 August "
  "and 8 September 2024, the practice email of 24 October 2024 at 11:45 am, Dr Krishnaiah's report of 13 February 2025 and the "
  "capability checklist of 3 July 2026 are all before me. None was prepared for this proceeding. That cuts both ways. They "
  "were not written to a legal test, so they do not use the statutory language, and the Krishnaiah report says on every page it "
  "was not prepared for medico-legal use. But they were written when they were written, for clinical purposes, before this "
  "appeal took its present shape, and that is what gives them their weight. The Commission is not bound by the rules of "
  "evidence (<i>Industrial Relations Act 2016</i>, s 531) and may act on treating records of this kind. What it must do is read "
  "them for what they say, and no more."))
s.append(N("<b>The lay evidence.</b> The Appellant gave evidence in accordance with his outline. I found him a careful and "
  "accurate witness on the documents, which is unsurprising since the documents are largely his own correspondence and the "
  "employer's replies to it. He was less comfortable when asked to describe what the events did to him, and gave that evidence "
  "briefly. I do not hold that against him; it is common in psychiatric injury cases. Ms Taylor and Ms Reese were called by "
  "the Respondent. Both were straightforward witnesses on the documents, which they did not dispute. Where their evidence "
  "went to why things were done, I have been careful to distinguish explanation from justification. [If Ms Jeffrey, Mr "
  "Harrison-Jones or Ms Conaghan are called, this paragraph would record their evidence as independent corroboration of the "
  "database restriction, the communication book and the console conditions; on Commissioner Dwyer's own approach in "
  "<i>McCool</i> [2021] QIRC 374 at [26], independent witnesses are weighted heavily.]"))
s.append(N("<b>No expert evidence.</b> Neither party tendered a report prepared for the proceeding. The Respondent, which "
  "pleads at paragraph 8 that medical records identify a past medical history of anxiety and at paragraph 22(f) that the "
  "March rostering was not causative, called no doctor to say either thing. On the approach the Commission has consistently "
  "taken, evidence that is not contradicted and is not inherently improbable will ordinarily be accepted. I have applied that "
  "approach to the treating records."))

s.append(P("PART C. FINDINGS OF FACT", H1))
s.append(P("The role", H2))
s.append(N("The Appellant commenced at Logan Hospital Switchboard on 25 March 2019 as a casual, became permanent on 3 March "
  "2021 and full time from 16 October 2023, on his own application of 31 August 2023, as a continuous shift worker (Notice "
  "paragraphs 1 to 16, 26 to 38). The role description requires continuous shift work over the full 24-hour period, "
  "participation in the emergency response process \"strictly adhering to protocols and timeframes\", maintenance of pager "
  "registers with \"accurate and current information\", and call queues kept \"to minimum at all times\". The Respondent "
  "admitted in February 2026 that maintaining accurate contact details for medical staff is \"a critical function of the "
  "Switchboard to ensure effective clinical handover and patient safety\". I find that the Appellant's role was the point at "
  "which the hospital's emergency response was activated, that its accuracy depended on records he was responsible for but, "
  "from July 2023, could not himself correct, and that he handled in the order of 200 to 300 calls a shift while doing so. "
  "The last figure is his own; it was not challenged and is consistent with the role description."))
s.append(P("Stressor 1(a): the database, the directives and the hours", H2))
s.append(N("On 18 July 2023 Ms Stibbard, in a temporary project role, removed operators' access to the database and removed "
  "the Contact and Number Changes book, so that after hours a correction would \"have to wait until either Chloe or myself "
  "are back\" (Notice 39 to 45). Access was not restored before 18 June 2024. On 15 April 2024 Ms Taylor notified that she "
  "and Ms Stibbard had placed themselves on after-hours call. Between 2 and 8 May 2024 the MASPER Registrar reported nine "
  "misdirected calls, including a MET call team ringing because \"switchboard could not tell them where VHUB was\". Ms "
  "Taylor's first response came on 9 May at 9:20 am, five days and eighteen hours later, asking Dr Wong for her business "
  "hours because they were \"not provided on the rosters\" and noting her phone was \"switched off\"; at 10:15 am she told the "
  "team of \"many ongoing issues\" about calls \"transferred to the wrong medical teams\" (Notice 56 to 67). The Integrated "
  "Respiratory Service wrote on 15 and 20 May that calls were still being put through to it and \"we can not help patients "
  "or other clinical staff\" (Notice 89 to 93). On 15 May 2024 the Appellant asked Ms Taylor to state her office hours and "
  "that changes be made in consultation; Ms Reese that evening asked him to retract the email, which he did; on 17 May Ms "
  "Taylor sent the department an email stating \"Otherwise my hours are from 06:30-14:30\" (Notice 74 to 88). Metro South's "
  "Chief Executive has stated in writing that there were no consequential changes to operating procedures over the period "
  "and that operational complaints were managed \"solely via email or verbally\" (Notice 266 to 267)."))
s.append(N("I find that from July 2023 the Appellant was responsible for the accuracy of a directory he could not edit; that "
  "the means of correction depended on two people whose hours were not known to the operators and, on Ms Taylor's own "
  "email of 9 May 2024, not known to her either in respect of the registrar; that misdirection of clinical calls resulted "
  "and was documented by clinicians; and that no procedure was changed in response."))
s.append(P("Stressors 1(b) to 1(g)", H2))
s.append(N("The removal of the communication book page on 6 June 2023 is admitted. The August 2023 concerns were met with a "
  "meeting on 10 August and Ms Reese's acknowledgement on 7 August of \"a rostering error that was accidentally made\". The "
  "special pandemic leave application of 20 February 2024 was declined twice on the stated ground that the statutory "
  "declaration was not attached, when the Respondent now admits it was, and approved on the same material on 29 February "
  "(Notice 114 to 142). The 13 May 2024 complaint was determined to be a public interest disclosure. The delegate interest "
  "expressed in April 2023 was not acted upon until endorsement in November 2025. I make findings on each of these where "
  "they matter to the exclusion, in Part E."))
s.append(P("Stressor 2: pay", H2))
s.append(N("Payroll wrote to Ms Taylor on 3 May 2024, copying the Appellant, identifying incorrect payments across four "
  "fortnights and asking her to \"submit an AVAC to correct these shifts for each fortnight\". On 13 May Payroll told the "
  "Appellant it could not see that any issue had been corrected and to \"speak to your Line Manager\". On 21 May Ms Taylor "
  "was \"still ... waiting payroll confirmation\". The AVAC was submitted on 28 May, together with a validation form for claims "
  "older than three months (Notice 182 to 210). The Review Decision records that on 9 April Ms Taylor had directed the "
  "Appellant to raise the older dates through MyHR payroll enquiries, and that on 24 April he told her Payroll had said the "
  "payments had to be processed by his manager (Review Decision pp 22 to 23). The myHR report records that every AVAC in the "
  "period was initiated by Ms Taylor and none by the Appellant. I find that the Appellant could not correct his own pay, that "
  "he was directed to Payroll and by Payroll back to his manager, and that the correction Payroll asked for on 3 May was made "
  "on 28 May."))
s.append(P("Stressor 3: the March break and fatigue", H2))
s.append(N("The Appellant was rostered to finish at 23:00 on Sunday 17 March 2024 and to start at 06:00 on Monday 18 March. "
  "The Respondent admits a seven-hour break. The Award requires ten hours; the agreement he signed as a casual on 17 June "
  "2020 permitted eight. The Respondent pleads human error. Ms Forrest of Human Resources wrote on 7 July 2026 that the "
  "eight-hour agreement \"is only applied where staff initiated shift swaps have occurred\"; the Respondent does not allege "
  "these shifts arose from a swap (Notice 224 to 234). The code register records, for the evening of 17 March, a MET call "
  "at 19:16 and a Code Blue on the same bed at 19:20 and a further MET call at 21:16, and for 18 March between 06:00 and "
  "14:00 a Code Grey, three MET call entries and two neonatal MET calls (Notice 228 to 230). The Appellant took sick leave on "
  "19 March. He requested a review of his pay and fatigue leave on 8 April; Ms Taylor escalated to Human Resources on 9 "
  "April; he followed up on 24 April; the request was refused on 1 May on the basis of the 2020 agreement, with a note that "
  "he could terminate it going forward (Notice 242 to 256). On 1 May he wrote that he had sent the Operations Manual "
  "fatigue toolkit to Ms Taylor \"for review and action\" with no feedback; the Respondent does not allege she reviewed it. "
  "On 10 May Ms Reese wrote to Human Resources that she acknowledged \"a few rostering errors made by Chloe with regards to "
  "Cory's line in past rosters\" (Notice 211 to 223). Metro South's Chief Executive has stated that the fatigue risk "
  "assessment records and register entries requested do not exist, that mandatory FRMS training applied only to clinical "
  "staff, and that fatigue risk management assessment at the Switchboard \"occurred after 30 June 2024\" (Notice 263 to 265)."))
s.append(N("I find that the March rostering breached both the Award and the agreement; that it was not an isolated error but "
  "one of a series on the Appellant's line, on the Director's own acknowledgement; that no fatigue risk assessment of the "
  "Appellant's rostering existed or was made; that the Appellant's request to have the breach recognised took 23 days to "
  "refuse and was refused on an agreement the employer's own Human Resources now says did not apply; and that the shifts in "
  "question carried the emergency code load the register records."))
s.append(P("Health and onset", H2))
s.append(N("The general-practice record of 16 November 2023 records poor sleep with shift work, that the Appellant could "
  "not do shifts without a good sleep, no psychological illness such as depression or psychosis, and mood good. The "
  "history records ADHD and anxiety noted in October 2022 and a referral to a psychiatrist renewed on 16 May 2024, for which "
  "no appointment could be obtained. On 28 June 2024 Dr Slawinski recorded \"stress at work\", \"upset by people not "
  "following rules\", reason for visit anxiety. On 1 July 2024 Dr Hawes recorded \"work stress\", that \"they withhold pay at "
  "times, no overtime- not processed, manipulate his roster- so he works lates then earlies\", and \"all this is stressing him "
  "out, causing anxiety\", and issued a work capacity certificate stating an injury date of 18 June 2024, diagnoses of "
  "anxiety and stress, and no capacity for work. The application for compensation was lodged the same day. Certificates "
  "followed on 11 August and 8 September 2024, the last recording a referral to a psychiatrist. On 24 October 2024 Dr "
  "Krishnaiah saw the Appellant and confirmed in writing at 11:45 am that he was \"suffering from psychological injury of "
  "Major Depressive Disorder with anxiety state\", increased fluoxetine and commenced quetiapine. His report of 13 February "
  "2025 diagnoses Major Depressive Disorder with anxious distress (DSM-5 296.23), records \"workplace stress stemming from "
  "issues with management and rostering\", that the issues \"began approximately one year ago when a new manager was "
  "appointed\", pay \"withheld or delayed for up to five months at a time, leading to significant financial stress\", and that "
  "\"premature exposure to the workplace is more likely result in significant deterioration\". The Appellant had no paid sick "
  "leave left at onset; every rostered day from 17 June to 20 September 2024 is coded leave without pay."))

s.append(P("PART D. INJURY, AND SIGNIFICANT CONTRIBUTING FACTOR", H1))
s.append(N("<b>Injury.</b> I find that the Appellant sustained a psychiatric injury, Major Depressive Disorder with anxious "
  "distress, with onset on or about 18 June 2024. The diagnosis is that of a treating consultant psychiatrist made after "
  "consultation on 24 October 2024 and maintained in a written report four months later. It is uncontradicted. The "
  "Respondent's pleading at paragraph 8 relies on a past history of anxiety. A note of anxiety in a history is not a "
  "diagnosis of a disorder, the record of 16 November 2023 is to the opposite effect seven months before onset, and the "
  "referral renewed in May 2024 is explained by the ADHD history and the later restarting of Vyvanse. If I were wrong about "
  "that, s 32 extends to the aggravation of a pre-existing condition where employment is a significant contributing factor "
  "to the aggravation, and the result would be the same. The Respondent's own review officer found a personal injury of a "
  "psychological nature on the July to September 2024 medical material, and nothing since has weakened that finding."))
s.append(N("<b>Arising out of employment, and significant contributing factor.</b> The test is whether employment was "
  "<i>a</i> significant contributing factor. It need not be the major or dominant one. Competing causes do not defeat the "
  "claim unless they reduce the employment contribution below significance. I find the test met, for four reasons that "
  "converge. First, the contemporaneous general-practice notes of 28 June and 1 July 2024, written before any claim decision, "
  "dismissal or proceeding, record the workplace as the presenting cause in terms that match the documentary record: rules, "
  "roster, pay, sleep. Second, Dr Hawes told WorkCover on 2 September 2024 that work events were the sole cause and certified "
  "no pre-existing factor. Third, Dr Krishnaiah's report attributes the condition to workplace stress \"stemming from\" "
  "management and rostering, dates its onset to the change of manager, and predicts deterioration on re-exposure, which is a "
  "causal statement in a clinician's register. Fourth, the Respondent's own delegate so found. The later stressors the "
  "Krishnaiah report lists, the dismissal, the litigation, the bereavement and the relationship breakdown, all post-date "
  "onset; the report itself attributes the relationship strain to the financial stress of withheld pay; and none of them "
  "was put to any witness as displacing the employment contribution. The Regulator called no evidence on the point."))

s.append(P("PART E. SECTION 32(5)(a): REASONABLE MANAGEMENT ACTION TAKEN IN A REASONABLE WAY", H1))
s.append(P("The approach", H2))
s.append(N("The exclusion applies where the injury arose out of reasonable management action taken in a reasonable way by "
  "the employer in connection with the employment. Three things follow from the text. First, the action must be management "
  "action. The ordinary demands of the work as it is organised, the call volume, the queue, the responsibility for an "
  "accurate directory, are the employment, not management action taken in connection with it. Second, the action must be "
  "both reasonable and taken in a reasonable way; a reasonable decision implemented unreasonably is not saved. Third, "
  "reasonable does not mean perfect. Management action \"need not be perfect or above criticism\" and blemishes do not "
  "make it unreasonable: <i>Bowers v WorkCover Queensland</i> (2002) and <i>Blackwood v Adams</i> [2015] ICQ 1. But the "
  "blemish principle describes flaws in the execution of otherwise reasonable action; it does not convert a breach of the "
  "instrument that governs the action into reasonable action."))
s.append(N("Where several stressors contributed, the Commission asks what the injury arose out of. <i>Delaney v Q-COMP</i> "
  "(2005) 178 QGIG 197 permits a global evaluation where management actions are joined by subject matter, time and "
  "personality. <i>Workers' Compensation Regulator v Mahaffey</i> [2016] ICQ 10 makes clear that the exclusion is not "
  "established merely because most of the stressors were reasonable; where unreasonable management action was itself a "
  "significant contributing factor to the injury, the injury did not arise out of reasonable management action, and the "
  "exclusion fails. <i>Carr v Workers' Compensation Regulator</i> [2022] QIRC 59 applied that approach stressor by stressor, "
  "one unreasonable stressor among nine sufficing. The review officer counted two reasonable factors against one "
  "unreasonable and concluded the injury \"mainly\" arose out of reasonable action. That is a dominant-cause test, and it "
  "is not the test. The question is not arithmetic but whether unreasonable management action was a significant contributor "
  "to the injury the Appellant actually sustained."))
s.append(P("Characterising each stressor", H2))
s.append(N("<b>The database restriction and the on-call arrangement (1(a)).</b> The decision to centralise directory "
  "corrections in a project role was management action and, as a decision, was within management's prerogative. It was not "
  "taken in a reasonable way. It removed the operators' means of correcting a safety-critical record for eleven months, "
  "without consultation (the Director's own 21 May 2024 email asks which directives the Appellant meant), with after-hours "
  "correction dependent on two people whose availability the operators did not know, and with no procedure changed after "
  "clinicians documented the consequences. Ms Taylor's own 9 May email records the same information gap from the manager's "
  "side. I find this action, as implemented, was not reasonable management action taken in a reasonable way."))
s.append(N("<b>The communication book (1(b)).</b> Removing a page from a shared book after a reminder about its use is "
  "management action. On the documents alone it is a blemish rather than an unreasonable act. [If Mr Harrison-Jones gives "
  "evidence of the manner in which the Appellant was addressed, the finding may move to unreasonable in the way it was "
  "taken. Absent that evidence, I would find it reasonable, if blunt.]"))
s.append(N("<b>The August 2023 concerns (1(c)).</b> A meeting was held within three days and a formal grievance path was "
  "offered. Reasonable management action reasonably taken."))
s.append(N("<b>The pandemic leave (1(d)).</b> Declining an application twice for want of an attachment that was in fact "
  "present is an error, admitted. It was corrected within nine days. On <i>Adams</i> it is a blemish. I would not find it "
  "unreasonable standing alone, although it is part of the picture of how this employee's entitlements were handled."))
s.append(N("<b>The retraction request (1(f)).</b> Ms Reese, on Human Resources advice, asked the Appellant to withdraw a "
  "department-wide email that questioned his manager's attendance. Asking that such a matter be raised privately rather "
  "on a group list is reasonable management action. The fact that Ms Taylor answered the question to the whole department "
  "two days later shows the question was legitimate; it does not make the request to withdraw the manner of asking "
  "unreasonable. I find this stressor within the exclusion."))
s.append(N("<b>The delegate role (1(g)).</b> Not shown to be management action directed to the Appellant. No finding "
  "either way is needed."))
s.append(N("<b>Pay (2(a) and (b)).</b> The correction of an employee's pay is management action. The errors themselves "
  "were blemishes. The manner of correction was not reasonable: the employee was sent to Payroll, Payroll sent him back, "
  "the instruction of 3 May was not acted on for 25 days while he was told his manager was waiting on Payroll, and only "
  "his manager could submit the form. The review officer found this factor \"blemished\" but reasonable because it was "
  "ultimately resolved. Resolution after 25 days of circular referral, during which the employee could do nothing, is not "
  "the same as reasonable action reasonably taken. I find the manner unreasonable."))
s.append(N("<b>The March rostering and the fatigue response (3(a) to (c)).</b> Rostering is management action. Rostering "
  "a seven-hour break, in breach of the Award and of the only agreement that could have reduced it, for an operator who "
  "activates emergency codes, is not reasonable management action. Human error is an explanation, not a justification; "
  "the question is the reasonableness of what was done, not the culpability of the person who did it. It was one of a series "
  "of errors on the Appellant's line, as the Director acknowledged. No fatigue risk assessment existed to catch it, on the "
  "employer's own statement. And the employer's response, when the Appellant raised it, was a 23-day delay and a refusal "
  "resting on an agreement its own Human Resources now says applied only to staff-initiated swaps. The review officer found "
  "the rostering unreasonable. I agree, and I go further: the way the breach was dealt with afterwards was also not "
  "reasonable. This stressor is outside the exclusion on both limbs."))
s.append(P("What the injury arose out of", H2))
s.append(N("The stressors here are joined by personality, the same manager, and by time, one year. They are not joined "
  "by subject matter in any meaningful sense: a directory system, a pay process and a roster are different things. A global "
  "evaluation is available but it does not assist the Respondent, because on my findings the unreasonable actions are not a "
  "minor part of the whole. The March rostering and its aftermath, the pay process and the directory restriction as "
  "implemented are, between them, the substance of what the treating records say the Appellant presented with: sleep and "
  "fatigue, lates then earlies, withheld pay, people not following rules. The reasonable actions, the meeting in August "
  "2023, the retraction request, the leave error corrected in nine days, are peripheral to that account. I find that "
  "unreasonable management action was a significant contributing factor to the injury. It follows on <i>Mahaffey</i> that "
  "the injury did not arise out of reasonable management action taken in a reasonable way, and s 32(5)(a) does not apply."))
s.append(N("I add that much of what the Appellant describes is not management action at all. Answering 200 to 300 calls a "
  "shift, carrying the emergency code load, and being responsible for a directory he could not edit are the conditions of "
  "the work as the employer structured it. The exclusion protects reasonable management action; it does not exclude an "
  "injury arising from the work itself. To the extent the injury arose from those conditions, s 32(5)(a) is not engaged."))

s.append(P("PART F. SECTIONS 32(5)(b) AND (c)", H1))
s.append(N("<b>Perception.</b> The Respondent pleads at paragraph 6(d)(ii) that the injury arose from the Appellant's "
  "expectation or perception of reasonable management action. The treating records use the word \"perceived\" several "
  "times. Under this limb it is the reality of the employer's conduct, not the employee's perception of it, that is "
  "assessed: <i>Prizeman v Q-COMP</i> [2005] QIC 53. The events on which I have found unreasonable action are admitted "
  "documentary events. A clinician's use of \"perceived\" to describe a patient's report does not convert a seven-hour break, "
  "a 25-day pay correction or eleven months without directory access into perceptions. This limb does not apply."))
s.append(N("<b>WorkCover action.</b> The 24 October 2024 email records preoccupation with the claim. That is the state of the "
  "injury four months after onset, when the claim had been rejected and the Appellant had received no income since June. The "
  "injury sustained in June 2024 did not arise out of anything WorkCover did. This limb does not apply."))

s.append(P("PART G. DETERMINATION AND ORDERS", H1))
s.append(N("The Appellant sustained an injury within s 32 of the Act. The appeal is allowed. The Review Decision of 24 "
  "October 2024 is set aside. The Appellant's application for compensation lodged 1 July 2024 is one for acceptance. Costs "
  "are reserved; the parties may make submissions, and the Appellant's Calderbank offer of 1 July 2026, rejected on 16 July "
  "2026, will be relevant to them."))

s.append(PageBreak())
s.append(P("PART H. THE AUTHORITIES THIS DETERMINATION RELIES ON, AND THEIR VERIFICATION STATUS", H1))
rows=[["Authority","Proposition used","Status"],
 ["Davis v Blackwood [2014] ICQ 9","De novo hearing; onus on the appellant including exclusion","Cited in repo notes; verify pinpoint"],
 ["WCR v Mahaffey [2016] ICQ 10","Exclusion fails where unreasonable action is a significant contributor; not a counting exercise","Cited at [51], [54]-[57] in repo; VERIFY from report before any use"],
 ["Delaney v Q-COMP (2005) 178 QGIG 197; [2005] QIC 11","Global evaluation where actions joined by subject, time, personality","Cited in Review Decision; verify"],
 ["Prizeman v Q-COMP [2005] QIC 53","Reality of employer conduct, not perception; onus on worker to show unreasonableness","In repo, read from source"],
 ["Bowers v WorkCover Queensland (2002)","Management action need not be perfect; blemishes","Cited in Review Decision; verify citation"],
 ["Blackwood v Adams [2015] ICQ 1","Reasonable does not mean perfect; not a dominant-cause test","Cited in repo at [23]; verify"],
 ["Carr v WCR [2022] QIRC 59","Stressor-by-stressor assessment; one unreasonable stressor sufficed","Cited in repo; verify"],
 ["Avis v WorkCover Queensland [2000] QIC 67","'Arising out of' requires causal connection, not proximate","Cited in Review Decision; verify"],
 ["McCool v WCR [2021] QIRC 374 (Dwyer IC)","Weight to independent witnesses; exclusion needs material to activate it; beneficial construction (s 194(3))","Read from PDF per repo; journey case, analogy only; Dwyer will not hear the appeal"],
 ["IR Act 2016 s 531; WCRA ss 32, 549, 550(4)","Rules of evidence not binding; the tests","Statute; check current reprint"],
]
t=Table([[C(a) if i else Paragraph(a,CELLB) for a in r] for i,r in enumerate(rows)], colWidths=[52*mm,78*mm,50*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t)
s.append(P("No authority above may be cited in a filing until its paragraph has been read in the authorised report. The "
  "Review Decision's own authorities are all 2009 or earlier and all on the insurer-favourable line; <i>Mahaffey</i>, the "
  "leading appellate authority on the subsection, is not mentioned in it. That omission is the single most useful legal "
  "point in the appeal and it must be made from the report itself.", WARN))

s.append(P("PART I. WHAT WOULD FLIP THIS RESULT", H1))
for t_ in [
 "<b>Attribution drifting to the reasonable stressors.</b> If the Appellant's oral evidence, or the clinical notes when produced, "
 "put the weight of the injury on the retraction request, the leave declines and the August 2023 handling, a Commissioner "
 "applying <i>Delaney</i> globally could find the injury arose mainly out of reasonable action. The evidence must keep the "
 "weight on rostering, pay and the directory, which is where the contemporaneous notes put it.",
 "<b>The March break treated as a single blemish.</b> If Ms Reese's 10 May 2024 acknowledgement of \"a few rostering errors\" "
 "is not put to her and the register is not tendered, the Respondent's \"human error, not repeated\" pleading gains ground and "
 "<i>Adams</i> does the Respondent's work. The sequence, 8 April to 1 May, and the Forrest email must be proved, not assumed.",
 "<b>The perception limb through the reports.</b> Four uses of \"perceived\" in the Krishnaiah report, \"perceived injustice\" "
 "in the 24 October email, and the personality paragraph. The answer is <i>Prizeman</i> and the admitted documents. If the "
 "Appellant argues motive or reprisal in the box, he hands the limb back.",
 "<b>The post-onset stressors.</b> Rejection, dismissal, bereavement, relationship breakdown, litigation. All after 1 July "
 "2024. If the causation account is allowed to run past 24 October 2024, the Respondent can say the February 2025 picture is "
 "not a workplace picture. The account must stop at onset and the first consultation.",
 "<b>The 'more night shifts' sentence.</b> The report records more night shifts and reduced penalty rates after complaints. "
 "No roster in evidence shows that. If it is put and cannot be supported, it costs credibility across the whole history.",
 "<b>No independent witness.</b> Without Ms Jeffrey, Mr Harrison-Jones or Ms Conaghan, the console conditions, the "
 "database restriction in practice and the communication book rest on the Appellant alone against two management witnesses. "
 "The documents carry most of it, but not the manner in which things were done.",
 "<b>The 16 May 2024 referral.</b> A psychiatric referral renewed a month before onset will be put as a pre-existing condition. "
 "One sentence, that it was the ADHD referral and no appointment was obtainable, answers it. Fumbling it does not.",
 "<b>Tab 26.</b> The served Tab 26 is the unfilled February 2026 template. Expect an authenticity dispute under the Form 25. "
 "Have the actually served notice ready; concede the tab; nothing turns on it since no fact cites Tab 26 alone.",
]: s.append(N(t_))
s.append(N("<b>Calibration.</b> On the record as it stands, with the Notice admitted or deemed admitted and no expert on either "
  "side, I put the prospect of the appeal succeeding at about two in three. The clinical notes from 24 October 2024, if they "
  "record what was reported at the first consultation, and a short treating letter of fact, would move that to about three in "
  "four. The single largest risk is not the law and not the documents. It is the attribution question at Part E, and it is "
  "decided by what the Appellant and the treating records say the injury came from."))

s.append(P("PART J. THE NEXT MENTION, AS IT WOULD RUN", H1))
s.append(P("The Commissioner's likely agenda after 30 September 2026, and the answer to each item.", BODY))
rows2=[["The Commissioner raises","The answer"],
 ["Witness lists: the Appellant has listed himself and Dr Krishnaiah [and Dr Hawes]; the Regulator has listed Ms Taylor and Ms Reese. Is the Appellant calling any other witness?",
  "State the position on Ms Jeffrey, Mr Harrison-Jones and Ms Conaghan plainly. If they are not called, say the documents carry the events and independent evidence goes to manner only."],
 ["Expert reports: direction 2 required any expert report by 9 September. None was served. Is the Appellant relying on medical evidence?",
  "The schedule of medical documents served 9 September lists every treating record relied on and what for. No report was prepared for the proceeding. The clinical notes from 24 October 2024 are awaited and will be served on receipt; leave is sought if required."],
 ["The Form 24 response: the Regulator has [admitted / not responded within 14 days]. What is the Appellant's position on the deemed admissions?",
  "Rule 49 operates by its terms. The facts are facts about documents in the Regulator's own hands. The Appellant will not oppose withdrawal of any admission the Regulator can show is wrong on the document."],
 ["Tab 26 of the annexure is the unfilled February 2026 form, not the notice served. The Regulator disputes authenticity.",
  "Conceded. The served February notice is produced. No fact in the Notice cites Tab 26 alone."],
 ["Hearing length. How many days?",
  "Two days. The Appellant's documentary evidence is by tender; his oral evidence in chief on the workplace is short; cross-examination is the Regulator's. Ms Taylor and Ms Reese half a day each."],
 ["Direction 5: conference or hearing?",
  "If the Regulator's list on 30 September shows no medical witness, elect the second s 552A conference. The Guide contemplates the Regulator reconsidering where new information is presented; the admitted Notice and the schedule are that information."],
 ["The parked Form 29 to Metro South.",
  "Not pressed for the fatigue records, which the Chief Executive says do not exist. A narrow request for the 2023 to 2024 rosters with version history may be sought; it is a category the 5 June letter did not address."],
]
t2=Table([[C(a) if i else Paragraph(a,CELLB) for a in r] for i,r in enumerate(rows2)], colWidths=[80*mm,100*mm], repeatRows=1)
t2.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t2)
s.append(Spacer(1,4*mm))
s.append(P("End of mock determination. Internal. Not for service.", SUB))

buf=io.BytesIO()
doc=BaseDocTemplate(buf,pagesize=A4,leftMargin=15*mm,rightMargin=15*mm,topMargin=13*mm,bottomMargin=13*mm)
def footer(c,d):
    c.saveState(); c.setFont('Helvetica',7.5); c.setFillColor(colors.HexColor('#666666'))
    c.drawString(15*mm,8*mm,"WC/2024/227 - Mock determination - INTERNAL, NOT FOR SERVICE"); c.drawRightString(A4[0]-15*mm,8*mm,f"Page {d.page}"); c.restoreState()
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(15*mm,13*mm,A4[0]-30*mm,A4[1]-26*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
doc.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n_=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/MOCK_DETERMINATION_WC2024227_6SEP2026_INTERNAL.pdf"; pdf.save(out,linearize=True); print("built",out,n_,"pages")
