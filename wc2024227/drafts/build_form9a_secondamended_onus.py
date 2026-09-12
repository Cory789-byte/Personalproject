#!/usr/bin/env python3
"""WC/2024/227 - SECOND AMENDED FORM 9A.

Same architecture as the Amended Form 9A filed 7 April 2026 - Part A, Part B (1 baseline,
2 stressors 1/2/3, 3 subsequent conduct), Part C contentions, Part D orders - with:
  * the role description opening each stressor at the duty it engages;
  * the 303 admitted paragraphs overlaid in blue;
  * red for material not yet admitted or not supported by the notice;
  * ⭐ the onus ACCEPTED as resting on the Appellant (Guide 7.3; Prizeman), not contested.

Facts via served_facts.py - the 303 as served 28 August 2026 and answered 8 September 2026.
⛔ DRAFT. Leave to amend required; not before 30 September 2026, and not less than 7 days
before the hearing (Appeal Guide Part 4.6).
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from served_facts import FACT as F, NOT_ADMITTED, TOTAL
assert TOTAL == 303

BLUE = colors.HexColor('#123f8c'); GREY = colors.HexColor('#6b6b6b'); RED = colors.HexColor('#9b1c1c')
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=15, spaceAfter=2)
H2  = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.2, leading=10.2, textColor=GREY, spaceAfter=4)
KEY = ParagraphStyle('KEY', fontName='Helvetica', fontSize=7.5, leading=9.2, spaceAfter=2)
PART= ParagraphStyle('PART', fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceBefore=9, spaceAfter=3)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=9, leading=11.2, spaceBefore=5, spaceAfter=2)
PLD = ParagraphStyle('PLD', fontName='Helvetica', fontSize=8.3, leading=10.4, leftIndent=4*mm, spaceAfter=2)
SUBP= ParagraphStyle('SUBP', parent=PLD, leftIndent=8*mm, spaceAfter=1.5)
ADM = ParagraphStyle('ADM', fontName='Helvetica', fontSize=7.9, leading=9.7, leftIndent=12*mm,
                     textColor=BLUE, spaceAfter=1.1)
DUTY= ParagraphStyle('DUTY', parent=ADM, leftIndent=8*mm, spaceBefore=1)
PEN = ParagraphStyle('PEN', parent=ADM, textColor=RED)
NOTE= ParagraphStyle('NOTE', fontName='Helvetica-Oblique', fontSize=7.6, leading=9.3,
                     leftIndent=8*mm, textColor=RED, spaceAfter=3)
def P(t, s): return Paragraph(t, s)
def q(ns, st=ADM):
    out=[]
    for n in ns:
        stl = PEN if n in NOT_ADMITTED else st
        tag = ' <b>[NOT YET ADMITTED]</b>' if n in NOT_ADMITTED else ''
        out.append(P(f"<b>[{n}]</b> {F[n]}{tag}", stl))
    return out
def duty(ns):
    return [P("<b>Duty engaged &mdash; the role description states:</b>", DUTY)] + \
           [P(f"<b>[{n}]</b> {F[n]}", DUTY) for n in ns]

s=[P("SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS (FORM 9A) &ndash; DRAFT", H1),
 P("WC/2024/227 &ndash; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator "
   "(Respondent). Same architecture as the Amended Form 9A filed 7 April 2026.", H2),
 P("<b>Black</b> is pleaded text. <font color='#123f8c'><b>Blue</b> is a paragraph admitted by the "
   "Respondent on 8 September 2026, word for word, with its number on the notice served 28 August "
   "2026. 298 of 303 admitted; five not admitted; none denied. Rule 49, for this proceeding only.</font> "
   "<font color='#9b1c1c'><b>Red is not yet admitted, or not supported by the notice and to be "
   "proved otherwise.</b></font>", KEY),
 P("⛔ <b>DRAFT.</b> Leave required; not before 30 September 2026, and not less than seven days "
   "before the hearing. ⭐ <b>The onus is accepted as resting on the Appellant</b> &mdash; see Part C.1.", KEY),
 Spacer(1,2*mm),

 P("PART A", PART),
 P("Appellant: Cory Lea Shepherd. Employer: State of Queensland (Queensland Health) &ndash; Logan "
   "Hospital Switchboard. Role: Administration Officer, Switchboard Services, classification AO3, a "
   "continuous shift working role. Injury: major depressive disorder with anxious distress. Date of "
   "onset: 18 June 2024.", PLD)]
s += q([1,2,3,4,13,14,15,16])

s += [P("PART B &mdash; MATERIAL FACTS", PART),
 P("<b>1. &nbsp;Baseline &mdash; the medical record</b>", SEC),
 P("1.1 &nbsp;The Switchboard receives emergency response notifications and distributes them to the "
   "response groups by category of emergency, and maintains the contact and paging information by "
   "which that is done.", PLD)]
s += duty([8,7,5,10])
s += [P("[⚠ THE MEDICAL IS NOT IN THE NOTICE &mdash; <b>no paragraph of the 303 refers to any medical "
   "record, practitioner, referral, certificate or diagnosis.</b> Everything at 1.2 to 1.10 is proved "
   "from the schedule of medical documents served 9 September 2026 (Tabs M1 to M9) and, as to clinical "
   "opinion, by the oral evidence of its author (Appeal Guide 7.6.5). The pinpoints carried in the "
   "Amended Form 9A of 7 April 2026 (\"Form 24, Para 34/36/38/39\") refer to the SUPERSEDED notice of "
   "February 2026 and must not be carried forward.]", NOTE),

 P("1.2 &nbsp;<b>Prior health.</b> Before 18 June 2024 the Appellant had not been diagnosed with or "
   "treated for depression. The general-practice record of 16 November 2023 (Dr Nanayakkara) records "
   "poor sleep with shift work, that the Appellant could not do shifts without a good sleep, "
   "\"no psychological illness such as depression or psychosis\", and mood good, with melatonin and "
   "temazepam prescribed that day. <b>[Tab M1 &mdash; general-practice records, Our Medical Ashmore, "
   "1 January 2023 to 1 July 2024, obtained by the Respondent under the Form 29 signed 4 July 2025; "
   "Respondent\'s item 11.]</b> Relied upon as the contemporaneous record that shift work was affecting "
   "the Appellant\'s sleep, and of what was prescribed for it, before any claim or proceeding. Its "
   "clinical significance is a matter for the treating doctors. Private entries unrelated to the injury "
   "are redacted on the extracted pages and marked as such.", SUBP)]
s += q([2,13,214,218] + list(range(263,266)) + list(range(269,272)))

s += [P("1.3 &nbsp;<b>The referral of 16 May 2024.</b> The referral letter of 16 May 2024 (Dr Zhao) "
   "renews a referral to a psychiatrist, Dr Amini, for \"ongoing care and management\". It lists the "
   "past medical history as the history-list items \"26/10/2022 ADHD\" and \"26/10/2022 Anxiety\", and "
   "lists the medications then current, <b>which include no antidepressant, no anxiolytic and no other "
   "psychotropic medication</b>. <b>[Tab M1.]</b> It was written the day after the email of "
   "15 May 2024 at 6:23 pm asking the Appellant to retract his email of that afternoon. That sequence "
   "is pleaded as to date only; no connection between the two is alleged. No appointment with the "
   "psychiatrist was obtained on that referral.", SUBP)]
s += q([76,77])

s += [P("1.4 &nbsp;<b>Onset and first presentation.</b> Onset 18 June 2024. The Appellant last worked "
   "a shift on 3 June 2024. On 28 June 2024 (Dr Slawinski) the record shows \"stress at work\" and "
   "\"upset by people not following rules\", reason for visit anxiety. On 1 July 2024 (Dr Hawes) the "
   "record shows \"work stress\", \"been there 5 years\", that \"they withhold pay at times, no "
   "overtime- not processed, manipulate his roster- so he works lates then earlies\", and \"causing "
   "anxiety\". <b>[Tab M1.]</b> The events those records name are the matters admitted on "
   "8 September 2026 and pleaded at Part B.2 below. The records are relied upon as the contemporaneous "
   "record of what was reported, before any claim decision, dismissal or proceeding; not as a finding "
   "of fact as to mechanism.", SUBP),

 P("1.5 &nbsp;<b>Certification.</b> The work capacity certificates of Dr Hawes dated 1 July, "
   "11 August and 8 September 2024, and of Dr Ki Pang dated 7 August 2024, state the date of injury as "
   "18 June 2024, that the Appellant was first seen for this injury on 1 July 2024, and certify no "
   "functional capacity continuously from 1 July to 6 October 2024. The referral to a psychiatrist is "
   "recorded on the certificate of 8 September 2024. Review Decision 69983 records at page 17 that the "
   "certificate of 1 July 2024 indicated \"there was no pre-existing factor or condition\", and that "
   "\"This was maintained in all later work capacity certificates\". <b>[Tab M2; Respondent\'s items 7 "
   "and 8.]</b> The medication box is unticked on each certificate.", SUBP),

 P("1.6 &nbsp;<b>Diagnosis, 24 October 2024.</b> At the first consultation, on the referral, the "
   "treating psychiatrist told the Appellant, and confirmed in writing at 11:45 am that day, that he "
   "was \"suffering from psychological injury of Major Depressive Disorder with anxiety state\"; that "
   "fluoxetine was increased to two capsules \"from today\" and Seroquel 25 mg commenced at night, "
   "\"to restore basic needs- sleep, eating and routine\". The Appellant\'s email of 5:12 pm that day "
   "reads \"I have finally been able to see a psychiatrist today\". <b>[Tab M3; Respondent\'s item 9.]</b> "
   "Read with 1.5, it records the progression from the injury certified as anxiety and stress on "
   "1 July 2024 to a depressive disorder by 24 October 2024.", SUBP),

 P("1.7 &nbsp;<b>The report of 13 February 2025.</b> Diagnosis: Major Depressive Disorder with "
   "anxious distress (DSM-5 296.23). Severity, functional effect and treatment (fluoxetine increased to "
   "three capsules daily; quetiapine 25 mg at night). The treating clinician records the origin as "
   "\"workplace stress stemming from issues with management and rostering\"; that the issues \"began "
   "approximately one year ago when a new manager was appointed\"; that pay was \"withheld or delayed "
   "for up to five months at a time, leading to significant financial stress\"; and that \"premature "
   "exposure to the workplace is more likely result in significant deterioration\". <b>[Tab M4; "
   "Respondent\'s item 10.]</b> The stressors so recorded correspond to matters admitted on 8 September "
   "2026: management and rostering, and the night-shift line; the shorter break; and pay withheld or "
   "delayed from the 5 February 2024 fortnight, uncorrected at 13 May, \"claims older than 3 months\" on "
   "28 May, a claim effective 30 March recorded \"Part Completed\" on 30 May, and the two February "
   "claims absent from the myHR report.", SUBP)]
s += q([211,212,220,258,259,260,193,196,197,203,210])
s += [P("1.8 &nbsp;<b>The report\'s footer, and the author\'s position.</b> The report bears a footer "
   "reading \"for the only reason of clinical information and not for medico-legal use\". The author\'s "
   "emails of 5 and 8 September 2026 state of his records \"You can use them according to the need to "
   "support your legal issues\", and identify the report of 13 February 2025 as \"the report that "
   "captures the relevant information you have requested\" on the matters in issue. <b>[Tab M5.]</b> The "
   "report is not relied upon for attribution among the individual events pleaded at Part B.2, nor for "
   "any matter after 24 October 2024 as a cause of the injury.", SUBP),

 P("1.9 &nbsp;<b>Current capacity.</b> The Employee Capability Checklist completed by Dr Day Hong Ma "
   "on 3 July 2026 records current capacity and restrictions and the continuing effect of the injury, "
   "including \"symptom exacerbation on exposure to the identified workplace stressors\". <b>[Tab M6.]</b> "
   "Relied upon for effect and capacity only, not for causation; it post-dates 1 July 2024.", SUBP),

 P("1.10 &nbsp;<b>Outstanding, and the finding in the decision under appeal.</b> The clinical records "
   "of the treating psychiatrist from 24 October 2024 were offered by the practice on 5 September 2026 "
   "and have been requested; they are not yet received and will be served on receipt. On the medical "
   "evidence then before it, the Respondent\'s review of 24 October 2024 found that the Appellant "
   "\"sustained a personal injury of a psychological nature\" and stated: \"Having regard to the medical "
   "evidence, I am satisfied your employment was <b>a significant contributing factor</b> to the "
   "psychological injury\". The claim was rejected under section 32(5), not section 32(1). "
   "<b>[Tabs M7 and M9.]</b> The hearing is de novo and that finding does not bind the Commission; it is "
   "relied upon as an admitted document.", SUBP)]
s += q([261,262])

s += [
 P("<b>2. &nbsp;Causative stressors (composite course, June 2023 &ndash; June 2024)</b>", SEC),
 P("<b>Stressor 1 &mdash; the conditions in which the work was carried on</b>", SEC),
 P("(a) &nbsp;<b>The directory, and the removal of the means of correcting it.</b> On 18 July 2023 "
   "access to the database was removed from all operators, the Contact and Number Changes book was "
   "taken out of the room, and an after-hours correction was to wait until one of two named persons "
   "returned. The Respondent does not allege access was restored before 18 June 2024. The duty to "
   "keep the information accurate remained on the position throughout. From 15 April 2024 the same "
   "two persons were also the after-hours contact, and from 14 May 2024 the same person was the route "
   "for notifying unavailability.", SUBP)]
s += duty([6,7])
s += q([39,40,41,42,43,44,45,55,49,50,51,52,53,54,111,112,113,162,163,164,165,166,273])
s += [P("(b) &nbsp;<b>The Communication Book entry of 6 June 2023.</b> A reminder concerning the "
   "monthly update of medical contact numbers was removed. The Respondent admits the removal in its "
   "pleading and again on 8 September 2026, does not allege the page has been located or copied, and "
   "does not list the Communication Book.", SUBP)]
s += duty([9])
s += q([143,144,145,146,147,148,149,150,151,152,153,154])
s += [P("(c) &nbsp;<b>The matters raised in August and September 2023, and the response.</b>", SUBP)]
s += q(list(range(26,39))+list(range(155,162)))
s += [P("(d) &nbsp;<b>The special pandemic leave application, February 2024.</b> Submitted three "
   "times, declined twice, approved on the same material.", SUBP)]
s += q(list(range(114,143)))
s += [P("(e) &nbsp;<b>The complaint of 13 May 2024.</b> The Appellant made a complaint to the Metro "
   "South Health Ethical Standards Unit, which that Unit determined on 24 December 2024 constituted a "
   "public interest disclosure, reference 24-ESU-1130. <b>The content is not set out, and no "
   "connection between it and any subsequent conduct is pleaded or relied upon in this appeal.</b>", SUBP),
 P("[⚠ NOT IN THE NOTICE &mdash; none of the 303 paragraphs refers to the Ethical Standards Unit, a "
   "public interest disclosure, or a complaint of 13 May 2024. To be proved from the Unit's "
   "determination and the Respondent's response of 18 February 2026 at Annexure A, Tab 27, or carried "
   "into a further notice to admit.]", NOTE),
 P("(f) &nbsp;<b>The office hours, the retraction request, and the answer.</b> On 15 May 2024 the "
   "Appellant asked that directives and changes be made in consultation and asked for the manager's "
   "office hours. He was asked that evening to retract that email. Two days later the hours were sent "
   "to the whole department. On 21 May he was asked which particular changes or directives had "
   "concerned him. Between 23 August 2023 and 17 May 2024 no fixed hours had been stated to staff. "
   "The Appellant pleads no characterisation of any person: the stated hours are pleaded because they "
   "determine how long an incorrect directory entry remained uncorrected.", SUBP)]
s += duty([3,4])
s += q([70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88])
s += [P("(g) &nbsp;<b>Workplace representation.</b> The Appellant notified an interest in the "
   "Switchboard delegate role; the Union Encouragement Policy QH-POL-248 requires managers to take a "
   "positive, supportive role; he was endorsed as a workplace delegate on or about 3 November 2025. "
   "<b>No allegation of deliberate suppression is made.</b>", SUBP)]
s += q([178,179,180,181,293,294])
s += [P("(h) &nbsp;<b>What arrived at the console, and the obligation to consult.</b> On 3 and 8 May "
   "2024 the MASPER Registrar reported nine occasions of calls reaching the wrong medical team; the "
   "first reply came five days, eighteen hours and fourteen minutes later and sought the reporting "
   "clinician's hours; nothing is alleged to have been sent to the Switchboard before 10:15 am on "
   "9 May. On 15 and 20 May the Integrated Respiratory Service asked twice for a directory amendment "
   "and reported it could not assist patients; the Appellant escalated the cause within three hours "
   "and two minutes; no document of the discussion, no communication to the Service, no amendment and "
   "no notification to staff is listed. Clause 3.2 of the Queensland Public Health Sector Certified "
   "Agreement (No. 11) 2022 requires contribution to decision-making \"not only in appearance, but in "
   "fact\" and \"an actual and genuine opportunity to influence the outcome, before a final decision "
   "is made\"; the change of 15 April 2024 was effective the day it was notified.", SUBP)]
s += duty([8,11,12])
s += q(list(range(56,70))+list(range(89,111))+list(range(167,182))+[101])
s += [P("(i) &nbsp;<b>What the employer states about its own systems.</b>", SUBP)]
s += q(list(range(263,273)))

s += [P("<b>Stressor 2 &mdash; remuneration</b>", SEC),
 P("(a) &nbsp;Between February and May 2024 the Appellant's pay required correction. On 3 May 2024 "
   "Payroll identified four fortnights and asked the manager to submit an Attendance Variation and "
   "Allowance Claim for each; on 13 May Payroll directed the Appellant to his line manager; on 21 May "
   "the manager was awaiting payroll confirmation; on 28 May the Appellant was asked to sign a "
   "validation of claims older than three months. The myHR submissions report records the manager as "
   "the initiator of each of the five such claims in the period and the Appellant as the initiator of "
   "none.", SUBP)]
s += duty([2,13])
s += q(list(range(182,207)))
s += [P("(b) &nbsp;The Respondent pleads that any discrepancies were remedied in a timely manner and "
   "that there are no outstanding underpayments. The claim submitted on 28 May 2024 is recorded as "
   "\"Part Completed\", and neither claim reference identified by Payroll on 3 May 2024 appears in the "
   "report.", SUBP)]
s += q([203,204,207,208,209,210])
s += [P("[⚠ CORRECTIONS TO THE AMENDED FORM 9A OF 7 APRIL 2026 &mdash; (i) the word \"IMMEDIATELY\" "
   "does not appear in the Payroll instruction of 3 May 2024; paragraph 195 records \"Please submit an "
   "AVAC to correct these shifts for each fortnight\". (ii) The \"42% pay disparity\" is not supported "
   "by any paragraph of the notice and must be proved by evidence or withdrawn. (iii) The \"admitted "
   "25-day delay\" is not a paragraph of the notice; the dates of 3 May and 28 May 2024 are admitted "
   "and the interval is arithmetic.]", NOTE)]

s += [P("<b>Stressor 3 &mdash; the roster and fatigue</b>", SEC),
 P("(a) &nbsp;Rostering errors on the Appellant's line were acknowledged in writing by the Director. "
   "On 10 May 2024 she wrote to Human Resources that the Appellant's roster would not be considered "
   "and that he was not yet aware of it. On 21 May she asked him to identify the changes and "
   "directives about which he had concerns.", SUBP)]
s += duty([2,13])
s += q(list(range(211,224)))
s += [P("(b) &nbsp;The shifts of 17 and 18 March 2024 were separated by a seven-hour break. The Award "
   "requires a break of not less than ten hours, and eight hours applies instead of ten only in "
   "specific circumstances. The 8-hour agreement of 17 June 2020 applies only where staff-initiated "
   "shift swaps have occurred, and the Respondent does not allege these shifts arose from such a swap.", SUBP)]
s += q(list(range(17,26))+list(range(224,228))+[257])
s += [P("[⚠ CORRECTION &mdash; the Amended Form 9A of 7 April 2026 pleaded a flat \"10-hour minimum\". "
   "The minimum is ten hours with eight applying only in specific circumstances (paragraph 257), and "
   "the agreement's scope is now answered by paragraphs 224, 225 and 234 rather than asserted.]", NOTE),
 P("(c) &nbsp;The emergency workload carried on those two shifts is recorded in the employer's own "
   "register. Those paragraphs were not admitted and no reason was given.", SUBP)]
s += q([228,229,230,231])
s += [P("[TO BE ADMITTED &mdash; the 2024 Emergency Code Register, a Metro South Hospital and Health "
   "Service workbook kept at Logan Hospital Switchboard, produced at Tab 31. Not admitted 8 September "
   "2026, no reason given; Tab 31 authenticity disputed on the Form 25 while the other tabs are "
   "admitted. Production requested 9 September 2026; reply of 10 September 2026 seeks until "
   "25 September 2026. Paragraph 268 is the employer's own statement that the record is available.]", NOTE),
 P("(d) &nbsp;On 8 April 2024 the Appellant requested a review of payment and raised fatigue. The "
   "enquiry was escalated to Human Resources on 9 April. No response is alleged between 9 April and "
   "1 May, an interval of 23 days, when the payment was refused. The leave of 19 March 2024 came from "
   "the Appellant's own leave.", SUBP)]
s += q(list(range(242,257)))
s += [P("(e) &nbsp;The Respondent's own review decision of 24 October 2024 finds that the break "
   "equated to seven hours, that the rostering of the two shifts amounted to unreasonable management "
   "action, that the Appellant sustained a personal injury of a psychological nature, and that his "
   "injury arose out of employment where employment was a significant contributing factor.", SUBP)]
s += q(list(range(257,263)))

s += [P("<b>3. &nbsp;Subsequent conduct</b>", SEC),
 P("(a) Meetings scheduled while the Appellant held current medical certificates. (b) Employment "
   "ended under abandonment provisions in October 2024 while certificates were current, and the "
   "Appellant was reinstated to his employment with an effective date of 20 September 2024, the "
   "reinstatement taking effect despite any payroll documentation. (c) The documents the Appellant "
   "provided to WorkCover Queensland in July and August 2024, and what the Respondent's amended List "
   "of Documents records of them.", PLD)]
s += q(list(range(274,283)))

s += [P("PART C &mdash; CONTENTIONS", PART),
 P("<b>1. &nbsp;⭐ The onus, accepted.</b> The Appellant accepts that he bears the onus of proving "
   "every element of his case on the balance of probabilities, including that his injury did not "
   "arise out of, or in the course of, reasonable management action taken in a reasonable way "
   "(Workers' Compensation Appeal Guide, Part 7.3; <i>Prizeman v Q-COMP</i> [2005] ICQ 43, where "
   "Hall P held that the onus is on the worker to establish that management action was unreasonable "
   "or taken in an unreasonable way, and that in the absence of evidence to support that assertion "
   "management action must be considered reasonable). The Appellant does not contend that the "
   "Respondent bears that onus, and the contrary contention in the Amended Form 9A filed 7 April 2026 "
   "is withdrawn.", PLD),
 P("<b>2. &nbsp;How the onus is discharged.</b> <i>Prizeman</i> presumes reasonableness only in the "
   "absence of evidence. The evidence is now on the record and is not in dispute. In particular the "
   "Respondent admits, as to its own documents and its own pleading: that access to the database was "
   "removed and is not alleged to have been restored before 18 June 2024; that no document recording "
   "consultation with Switchboard operators before the change of 15 April 2024 is listed; that nine "
   "occasions of misdirected calls were reported by a clinician and nothing is alleged to have been "
   "sent to the Switchboard about them for six days; that no document of the discussion of 20 May "
   "2024, no communication to the Integrated Respiratory Service, and no amendment to the "
   "contact-details document is listed; that the fatigue records do not exist, that the training "
   "applied only to health practitioners and clinical assistants, that fatigue assessment at the "
   "Switchboard began only after 30 June 2024, and that there were no consequential changes to "
   "operating procedures; and that complaints were managed solely by email or verbally with the "
   "complainant.", PLD),
 P("<b>3. &nbsp;Compensable injury &mdash; section 32(1).</b> The Appellant sustained a personal "
   "injury of a psychological nature arising out of, or in the course of, his employment, employment "
   "being <b>a significant contributing factor</b>. The Respondent's own review decision so finds.", PLD),
 P("<b>4. &nbsp;Section 32(5)(a), first limb &mdash; the matters at Stressor 1(a) and 1(h) are not "
   "management action.</b> A directory the occupant of the position is required to keep accurate but "
   "cannot correct; emergency notifications reaching the wrong team; a clinical service unable to "
   "assist patients because a directory entry is wrong &mdash; these are the conditions in which the "
   "work was carried on, not action taken by the employer against the worker. One decision was taken, "
   "on 18 July 2023, for a stated project reason; what followed is a state of the system, and "
   "subsection (5) does not reach it.", PLD),
 P("<b>5. &nbsp;Section 32(5)(a), second limb &mdash; where the matters pleaded are management "
   "action, it was not taken in a reasonable way.</b> The change of 15 April 2024 was effective the "
   "day it was notified, with no record of prior consultation, against an instrument requiring a "
   "genuine opportunity to influence the outcome before a final decision. The remuneration correction "
   "was returned across four fortnights to the only person able to make it and is recorded as Part "
   "Completed. The fatigue enquiry drew no response for 23 days.", PLD),
 P("<b>6. &nbsp;<i>Delaney</i>.</b> A global evaluation is an evaluation of management actions. It "
   "cannot absorb a causative factor that is not management action.", PLD),
 P("<b>7. &nbsp;<i>Mahaffey</i>.</b> A single unreasonable stressor suffices. The rostering of the "
   "shifts of 17 and 18 March 2024 is found by the Respondent's own decision to have amounted to "
   "unreasonable management action.", PLD),
 P("<b>8. &nbsp;The effect of the admissions.</b> The Respondent states that an admission of a "
   "document is an admission of existence and wording only. That is accepted, and does not reach four "
   "classes of admitted fact relied on: what the statement of facts and contentions does not allege; "
   "what the List of Documents does not list; computed intervals of time; and the identity of the "
   "recipients of a communication. The Respondent has not identified any admitted fact it contends is "
   "irrelevant.", PLD),
 P("<b>9. &nbsp;The hearing de novo.</b> The Respondent says no finding in Review Decision 69983 "
   "binds the Commission. That is accepted, and it applies to the whole of the decision. The "
   "conclusion under appeal is a conclusion of that decision, reached upon the findings recorded in "
   "it.", PLD),
 P("<b>10. &nbsp;The Respondent's pleaded case.</b> Paragraph 27 of the amended statement of facts "
   "and contentions does not identify, by particular, date, document or cross-reference, the "
   "management action relied upon. No disciplinary process, formal performance management or "
   "communication described as a warning before 18 June 2024 is alleged.", PLD)]
s += q([300,301,302,303])

s += [P("PART D &mdash; ORDERS SOUGHT", PART),
 P("1. The appeal be allowed. 2. The decision of the Respondent dated 24 October 2024 be set aside. "
   "3. It be declared that the Appellant sustained an injury within the meaning of section 32 of the "
   "Workers' Compensation and Rehabilitation Act 2003. 4. The Appellant's application for "
   "compensation be accepted. 5. Costs reserved.", PLD)]

buf=io.BytesIO()
doc=BaseDocTemplate(buf,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=12*mm,bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(15*mm,11*mm,A4[0]-30*mm,A4[1]-23*mm,
    leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
doc.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="INTERNAL/2026-09-12_FORM9A_SECOND_AMENDED_original_architecture_onus_accepted.pdf"
pdf.save(out,linearize=True)
print(f"built {out} - {n} page(s)")
