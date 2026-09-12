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
import io, os, pikepdf
SERVE = bool(os.environ.get('SERVE'))
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
PART_REF = ParagraphStyle('PART_REF', fontName='Helvetica-Oblique', fontSize=7.8, leading=9.6,
                          leftIndent=8*mm, spaceAfter=2.5)
def P(t, s): return Paragraph(t, s)
def _collapse(ns):
    ns = sorted(set(ns)); out=[]; i=0
    while i < len(ns):
        j=i
        while j+1 < len(ns) and ns[j+1]==ns[j]+1: j+=1
        out.append(str(ns[i]) if j==i else f"{ns[i]} to {ns[j]}")
        i=j+1
    return ", ".join(out)
def q(ns, st=ADM):
    if SERVE:
        if not ns: return []
        pend = [n for n in ns if n in NOT_ADMITTED]
        adm  = [n for n in ns if n not in NOT_ADMITTED]
        if not adm:
            return [P("Particulars: paragraphs " + _collapse(pend) +
                      " of the notice to admit facts served 28 August 2026.", PART_REF)]
        txt = "Particulars: paragraphs " + _collapse(adm) + \
              " of the notice to admit facts served 28 August 2026, admitted 8 September 2026."
        if pend:
            txt += " Paragraph" + ("s " if len(pend)>1 else " ") + _collapse(pend) + \
                   " of that notice " + ("are" if len(pend)>1 else "is") + " not admitted."
        return [P(txt, PART_REF)]
    out=[]
    for n in ns:
        stl = PEN if n in NOT_ADMITTED else st
        tag = ' <b>[NOT YET ADMITTED]</b>' if n in NOT_ADMITTED else ''
        out.append(P(f"<b>[{n}]</b> {F[n]}{tag}", stl))
    return out
def duty(ns):
    if SERVE:
        return [P("Duty engaged: paragraphs " + _collapse(ns) + " of that notice (the role description).",
                  PART_REF)]
    return [P("<b>Duty engaged &mdash; the role description states:</b>", DUTY)] + \
           [P(f"<b>[{n}]</b> {F[n]}", DUTY) for n in ns]
_P_orig = P
def P(t, st):
    if SERVE and st is NOTE: return None
    return _P_orig(t, st)

s=[P("SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS (FORM 9A)" if SERVE else
     "SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS (FORM 9A) &ndash; DRAFT", H1),
 P("WC/2024/227 &ndash; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator "
   "(Respondent). Section 550(4), Workers' Compensation and Rehabilitation Act 2003.", H2)]
if SERVE:
    s += [P("Particulars are given by reference to the paragraph numbers of the Appellant's notice to "
            "admit facts served on the Respondent on 28 August 2026, to which the Respondent responded "
            "on 8 September 2026.", KEY)]
else:
    s += [P("<b>Black</b> is pleaded text. <font color='#123f8c'><b>Blue</b> is a paragraph admitted by the "
      "Respondent on 8 September 2026, word for word, with its number on the notice served 28 August "
      "2026. 298 of 303 admitted; five not admitted; none denied. Rule 49, for this proceeding only.</font> "
      "<font color='#9b1c1c'><b>Red is not yet admitted, or not supported by the notice and to be "
      "proved otherwise.</b></font>", KEY),
     P("⛔ <b>DRAFT.</b> Leave required; not before 30 September 2026, and not less than seven days "
      "before the hearing. ⭐ <b>The onus is accepted as resting on the Appellant</b> &mdash; see Part C.1.", KEY)]
s += [
 Spacer(1,2*mm),

 P("PART A", PART),
 P("Appellant: Cory Lea Shepherd. Employer: State of Queensland (Queensland Health) &ndash; Logan "
   "Hospital Switchboard. Role: Administration Officer, Switchboard Services, classification AO3, a "
   "continuous shift working role.", PLD),
 P("<b>Injury:</b> major depressive disorder with anxious distress (DSM-5 296.23), diagnosed by "
   "the Appellant's treating psychiatrist on 24 October 2024.", PLD),
 P("<b>The injury is a diagnosed medical condition arising from the Appellant's employment over "
   "the course of conduct pleaded at Part B.2 below, between approximately June 2023 and June 2024. "
   "It is not pleaded as arising from an event occurring on a single day.</b> The date of injury "
   "recorded on the work capacity certificates of the treating general practitioner is 18 June 2024. "
   "That date is the practitioner's and is a matter for the medical evidence; the Appellant asserts "
   "no date of onset of his own.", PLD)]
s += q([1,2,3,4,13,14,15,16])

s += [P("PART B &mdash; MATERIAL FACTS", PART),
 P("The documentary facts identified below have been admitted to the extent recorded in the "
   "Respondent's response of 8 September 2026. Those admissions provide evidence from which the "
   "Commission is invited to determine the nature, reasonableness and causal significance of the "
   "relevant circumstances.", PLD),
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

s += [P("1.4 &nbsp;<b>Deterioration and first presentation.</b> The Appellant last worked a shift "
   "on 3 June 2024. On days in May 2024 and in the first week of June 2024 he drove to work, was "
   "unable to enter the building, and reported himself unfit from the car park. The date of injury "
   "recorded on the certificates is 18 June 2024. On 28 June 2024 (Dr Slawinski) the record shows \"stress at work\" and "
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
 P("<b>STRESSOR 1 &mdash; THE CONDITIONS IN WHICH THE WORK WAS CARRIED ON</b>", SEC),

 P("<b>S1.1 &nbsp;The duty to keep the contact information accurate.</b> A key responsibility of the "
   "position is to collate information and maintain the Omnivista database and SharePoint so that the "
   "information held within Switchboard Services is accurate and appropriate, and to maintain the "
   "database and registers of paging and contact information with accurate and current information. "
   "That duty is the duty by reference to which each of S1.2 to S1.8 below is pleaded.", SUBP)]
s += duty([6,7])

s += [P("<b>S1.2 &nbsp;The removal of the means of performing that duty, 18 July 2023.</b> On "
   "18 July 2023 the Switchboard Telecommunications Coordinator notified the Appellant and the "
   "Switchboard team that she would be removing everyone's access to the database, and that she had "
   "removed the Contact and Number Changes book from the room. The Respondent's own review decision "
   "records the same matters. The Respondent does not allege that access to the database was restored "
   "to the Appellant at any time before 18 June 2024. The duty at S1.1 remained on the position "
   "throughout that period.", SUBP)]
s += q([39,40,45,46,47,48,55])

s += [P("<b>S1.3 &nbsp;The repair path, and its availability.</b> From 18 July 2023 an operator who "
   "identified an incorrect or missing entry could not correct it. An amendment was to be sought "
   "directly from the Coordinator, whose stated working hours were every Tuesday and every second "
   "Monday between 8:00 and 16:00 in a temporary project role, or, if she was not present and the "
   "matter was urgent, from the Switchboard Manager. A request made after hours, overnight, on a "
   "weekend or on a public holiday was to wait until one of them returned. The Appellant pleads no "
   "characterisation of any person; the availability of those two persons is pleaded because it "
   "determined how long an incorrect entry remained uncorrected.", SUBP)]
s += q([41,42,43,44])

s += [P("<b>S1.4 &nbsp;The criticality of the function, as admitted by the Respondent.</b> On "
   "18 February 2026 the Respondent admitted that \"Maintaining accurate contact details for medical "
   "staff is a critical function of the Switchboard to ensure effective clinical handover and patient "
   "safety\", adding that there was a procedure in place for this to occur, and denied a further "
   "paragraph of that notice on the ground that there was already a procedure in place. The procedure "
   "in place from 18 July 2023 is the procedure pleaded at S1.3 above. Its operation between 2 and "
   "20 May 2024 is pleaded at S1.7 and S1.8 below.", SUBP)]
s += q([283,289,290,291])

s += [P("<b>S1.5 &nbsp;The further changes to process, April and May 2024.</b> On 15 April 2024 the "
   "Switchboard Manager notified Logan Switch, copied to the Director and the Switchboard staff, that "
   "she and the Coordinator had added themselves to an after-hours on-call arrangement, that the "
   "process during office hours remained the same and that staff were to contact her through the "
   "switchboard, the office or her mobile, and that the new process was effective from that day. On "
   "19 April 2024, as recorded in the review decision, she notified the team that due to errors being "
   "made with respect to data entry a new process was to be followed which included more checks to "
   "ensure accuracy of data entry. On 13 May 2024 the on-call roster for the following fortnight was "
   "circulated. On 14 May 2024 the process for notifying unavailability for a rostered shift was also "
   "directed through the same person.", SUBP)]
s += q([49,50,51,52,53,54,111,112,113,162,163,164,165,166])

s += [P("<b>S1.6 &nbsp;The obligation to consult, and the absence of any record of consultation.</b> "
   "Clause 3.2 of the Queensland Public Health Sector Certified Agreement (No. 11) 2022 provides that "
   "the requirement of consultation is never to be treated perfunctorily or as a mere formality, that "
   "consultation involves more than a mere exchange of information and requires participants to "
   "contribute to the decision-making process \"not only in appearance, but in fact\", and that the "
   "process requires the exchange of timely information so that the parties have \"an actual and "
   "genuine opportunity to influence the outcome, before a final decision is made\". Clause 4.1.4 "
   "requires a business case to be tabled for consultation for significant organisational change "
   "including major alterations to current service delivery arrangements. The change notified on "
   "15 April 2024 was stated to be effective the day it was notified, and the Respondent's amended "
   "List of Documents records no document of any consultation with Switchboard operators before it. "
   "The Respondent does not allege that agreement under clause 6.2 of the Award was obtained, or that "
   "a ballot of affected employees was conducted, before that change. The employer conducted a "
   "consultation process on other occasions, including in November and December 2024, under which "
   "agreement is defined as the consent of a majority of affected employees. On 20 May 2024 the "
   "Switchboard Manager wrote that updated procedures could be put to the team for consultation "
   "before implementing.", SUBP)]
s += duty([11])
s += q([273,167,168,169,170,176,177,180,181,101])

s += [P("<b>S1.7 &nbsp;What arrived at the console: the misdirected emergency calls, 2 to 9 May "
   "2024.</b> A key responsibility of the position is to participate in the Emergency Response "
   "process by receiving emergency response notifications and distributing them to the appropriate "
   "response groups, dependent on the category of emergency, as per emergency code procedures, "
   "strictly adhering to protocols and timeframes; to maintain call queues to a minimum at all times; "
   "and to operate under pressure where high volume call traffic is concerned. On 3 May 2024 at "
   "3:06 pm the MASPER Registrar wrote to the Switchboard Manager listing five occasions on 2 and "
   "3 May on which calls had reached the wrong destination, including an occasion at 14:46 recorded "
   "as \"MET call team called x5290 asking where MET call was located 'VHUB' - switchboard could not "
   "tell them where VHUB was. Had to be redirected by MASPER\". On 8 May at 5:28 pm she wrote again "
   "listing four further occasions. Those nine occasions fell while the arrangement notified on "
   "15 April 2024 was in force. The first reply was sent on 9 May at 9:20 am, five days, eighteen "
   "hours and fourteen minutes after the first email, and asked the reporting clinician to confirm "
   "her business hours because they were not provided on the rosters, noting that her handset was "
   "switched off. At 10:15 am the same day the Switchboard Manager wrote to Logan Switch introducing "
   "a new process and referring to \"many ongoing issues raised by the MASPER and the medical "
   "department about calls being transferred to the wrong medical teams\". The Respondent does not "
   "allege that any communication was sent to Logan Switch or to the Switchboard staff concerning "
   "those occasions at any time after 3 May 2024 and before 10:15 am on 9 May 2024.", SUBP)]
s += duty([8,5,10])
s += q(list(range(56,70)))

s += [P("<b>S1.8 &nbsp;What arrived at the console: the Integrated Respiratory Service, 15 to 20 May "
   "2024.</b> On 15 May 2024 at 11:47 am an Administration Officer of the Integrated Respiratory "
   "Service wrote to Logan Switch, marked of High importance, asking that the number registry or "
   "directory be amended to show that an extension belonged to that Service, and stating that it was "
   "not Respiratory Medical Outpatients and had no doctors working out of that area. No response is "
   "alleged before 20 May. On 20 May at 11:03 am she wrote again, marked of High importance, stating "
   "that calls continued to be put through and that \"we can not help patients or other clinical "
   "staff with OPD issues\". At 2:05 pm that day, from the Logan Switch account and within the office "
   "hours the Switchboard Manager had stated to all staff, the Appellant wrote identifying the cause "
   "as modifications made to the document \"Outpatients Department - Clinic contact Details\" on "
   "22 February 2024 and recommending a modification and review of that document. The reply at "
   "4:30 pm, sent two hours after the conclusion of those stated office hours, stated that the task "
   "was being actioned and that the matter had been discussed with a named colleague that morning. "
   "The Respondent's amended List of Documents records no document created on 20 May 2024 recording "
   "that discussion, no communication sent by either person to the Service on that day, and the "
   "Respondent does not allege that the contact-details document was amended on or before 20 May 2024 "
   "or that the Switchboard staff were notified of the modifications made to it on 22 February 2024.", SUBP)]
s += q(list(range(89,111)))

s += [P("<b>S1.9 &nbsp;The office hours of the manager to whom the position reports.</b> The position "
   "reports to the Switchboard Manager, and the role description names that person as the contact for "
   "the position. On 23 August 2023 she notified the Switchboard that she worked flex hours, that "
   "staff may have noticed she was starting and finishing at different times, and that her hours "
   "\"would range from starting between 6-9am and finishing 2-5pm\". The Respondent does not allege "
   "that fixed office hours were stated to the Switchboard staff at any time between 23 August 2023 "
   "and 17 May 2024. On 15 May 2024 at 1:15 pm the Appellant wrote asking that directives and changes "
   "be made in consultation with the team and asking that the office hours be shared so the "
   "department could be aware of the regular schedule, noting inconsistency in arrival and departure "
   "times. At 6:23 pm the Director replied, copied to the Manager and marked of High importance, "
   "stating that the email did not demonstrate the iCARE2 value of Respect and did not comply with "
   "the Code of Conduct, and asking the Appellant to retract it. At 7:09 pm the Appellant replied "
   "that requesting clarity on business hours was a reasonable question. On 17 May 2024 at 9:30 am "
   "the Manager wrote to the whole department stating that her hours could vary, that she would be in "
   "later between 0800 and 0830, that otherwise her hours were from 06:30 to 14:30, that she would "
   "not be in the office until around 11 am on Monday 20 May, and that moving forward she would send "
   "an email to switch to advise of any change to her office hours for the week. On 21 May the "
   "Director asked the Appellant whether there were one or more particular changes or directives "
   "about which he had concerns as to consultation and communication. On 18 June 2024 at 8:58 am the "
   "Manager wrote to Logan Switch stating that she was taking that day off and \"I am sorry I haven't "
   "been there for you all over the past week\".", SUBP)]
s += duty([3,4])
s += q(list(range(70,89)))

s += [P("<b>S1.10 &nbsp;The Communication Book, 6 June 2023.</b> A key responsibility of the position "
   "is to maintain discretion and exercise judgement where necessary to resolve problems within the "
   "scope of the role, in situations where precedence has not been set and procedures are not "
   "defined. A reminder concerning the monthly update of medical contact numbers was placed in the "
   "Communication Book and was removed. At 9:57 am on 6 June 2023 the Manager wrote to Logan Switch "
   "that the book was \"not used to simply put your point across or make any indirect comments "
   "towards the team\", and at 4:05 pm she wrote to the Director that she had taken the entry out the "
   "week before and that she felt the book was being used as a \"burn book\". The Respondent's "
   "pleading admits that pages were removed on or about 6 June 2023, and on 18 February 2026 the "
   "Respondent admitted that a page was removed and did not admit that it contained the Appellant's "
   "handwriting \"because the respondent does not have a copy of the page\". It also admitted that in "
   "an email to the Director of 6 June 2023 the Manager stated \"I did raise my voice and asked him "
   "to please stop talking over the top of me\". The Respondent does not identify the entry removed "
   "or its author, does not allege that the removed page has been located or that any copy exists, "
   "and does not list the Communication Book or any page or entry from it in its List of Documents.", SUBP)]
s += duty([9])
s += q(list(range(143,155))+[288,292])

s += [P("<b>S1.11 &nbsp;The matters raised in August and September 2023, and the response.</b> On "
   "7 August 2023 the Appellant raised matters concerning hours and workplace issues. The Manager "
   "acknowledged a rostering error and offered to roster him off the following day to give the "
   "required rest period, and the Director replied the same day. On 31 August 2023 he provided a "
   "written application headed \"Request to Increase Working Hours to Full Time Rotational Roster\", "
   "in which he expressed willingness to take on additional night shifts. On 4 September 2023 he "
   "confirmed in writing that he was able and willing to work any roster presented to him including "
   "the full 24-hour rotational schedule, and attached a draft roster spreadsheet. He was approved to "
   "commence full-time hours from 16 October 2023.", SUBP)]
s += q(list(range(26,39))+list(range(155,162)))

s += [P("<b>S1.12 &nbsp;The special pandemic leave application, February 2024.</b> The leave request "
   "history records the application as created, submitted, declined, resubmitted, declined again, "
   "resubmitted and approved, the Appellant being recorded as having submitted it on three occasions "
   "and the Manager as having declined it on two. The interval between the final submission and its "
   "approval was thirteen minutes and thirty-five seconds. The Instrument of Human Resource "
   "Sub-Delegation for paid special pandemic leave does not permit further sub-delegation of the "
   "powers it confers.", SUBP)]
s += q(list(range(114,143)))

s += [P("<b>S1.13 &nbsp;The complaint of 13 May 2024.</b> On 13 May 2024 the Appellant made a "
   "complaint to the Metro South Health Ethical Standards Unit, which that Unit determined on "
   "24 December 2024 constituted a public interest disclosure, reference 24-ESU-1130. <b>The content "
   "of the disclosure is not set out, and no connection between it and any subsequent conduct is "
   "pleaded or relied upon in this appeal.</b>", SUBP),
 P("[⚠ NOT IN THE NOTICE &mdash; none of the 303 paragraphs refers to the Ethical Standards Unit, a "
   "public interest disclosure, or a complaint of 13 May 2024. To be proved from the Unit's "
   "determination and the Respondent's response of 18 February 2026 at Annexure A, Tab 27, or carried "
   "into a further notice to admit.]", NOTE),

 P("<b>S1.14 &nbsp;Workplace representation.</b> The Appellant notified an interest in the Switchboard "
   "delegate role, and the Respondent has admitted that the Union Encouragement Policy QH-POL-248 "
   "requires managers to take a positive, supportive role in relation to workplace delegates. He was "
   "endorsed as a workplace delegate on or about 3 November 2025. <b>No allegation of deliberate "
   "suppression is made.</b>", SUBP)]
s += q([178,179,293,294])

s += [P("<b>S1.15 &nbsp;What the employer states about its own systems and records.</b> By letter of "
   "5 June 2026 to the Commission, Metro South Hospital and Health Service stated that the requested "
   "fatigue risk management documents do not exist, that mandatory Fatigue Risk Management System "
   "training applies only to health practitioners and clinical assistants and that Switchboard staff "
   "are non-clinical, that the implementation of fatigue risk management assessment at the "
   "Switchboard occurred after 30 June 2024, that there have been no consequential changes to "
   "operating procedures over the period requested, and that all employee complaints relating to "
   "Switchboard operational errors are made directly to the line manager and \"managed solely via "
   "email or verbally with the complainant\". The Respondent does not allege that any fatigue risk "
   "assessment was conducted, that any fatigue risk management training was provided, that fatigue "
   "risk management assessment was implemented at the Switchboard, or that any change was made to the "
   "operating procedures of the Switchboard as a consequence of any employee complaint, at any time "
   "before 30 June 2024.", SUBP)]
s += duty([12])
s += q(list(range(263,273)))

s += [P("<b>S1.16 &nbsp;Matters pleaded as context only.</b> The matters at S1.10, S1.11, S1.12, S1.13 and "
   "S1.14 above, and at paragraph 3 below, are pleaded as part of the sequence of matters the "
   "Appellant raised and the responses he received. They are not relied upon as independent causative "
   "circumstances, and no retaliatory or reprisal connection between any of them and any other "
   "conduct is alleged. The causative circumstances relied upon in Stressor 1 are those at S1.1 to "
   "S1.9 and S1.15.", SUBP)]

s += [P("<b>STRESSOR 2 &mdash; REMUNERATION</b>", SEC),
 P("<b>S2.1 &nbsp;The basis of the entitlement.</b> The position is a continuous shift working role "
   "over the full 24-hour period, seven days a week, and the occupant must be able to work a roster "
   "covering multiple shifts over a 24/7 period. The entitlements pleaded below arise from that "
   "arrangement.", SUBP)]
s += duty([2,13])

s += [P("<b>S2.2 &nbsp;Public holidays on which the Appellant was not required to work.</b> Section 23 "
   "of the Hospital and Health Service General Employees (Queensland Health) Award provides that "
   "where an employee in receipt of the additional week's leave prescribed by clause 19.2(a) is "
   "rostered off on Easter Saturday, Easter Sunday, Show Day or Labour Day, that employee is to be "
   "paid an additional day's wage or granted a day's holiday in lieu. The Appellant was rostered off "
   "on public holidays between February and April 2024. As at 1 May 2024 payroll was still reviewing "
   "his entitlements regarding public holidays not required arising while he was a part-time "
   "employee, while the Manager confirmed that since his commencement of full-time employment all "
   "payments for public holidays not required had been processed.", SUBP)]
s += q([241,255,256])

s += [P("<b>S2.3 &nbsp;The correction sought, and where each direction sent it.</b> On 8 April 2024 "
   "the Appellant asked the Manager to review his pay. On 9 April she directed him to raise the older "
   "dates through MyHR payroll enquiries. On 3 May 2024 Payroll wrote to the Manager, copying the "
   "Appellant, identifying four fortnights and asking her to \"submit an AVAC to correct these shifts "
   "for each fortnight so Cory is paid corrected and his contracted hours are correct\". On 10 May the "
   "Appellant wrote to Payroll. On 13 May 2024 Payroll replied to the Appellant: \"I cannot see that "
   "any of the issues below have been corrected. Please speak to your Line Manager to have them "
   "corrected with an AVAC submitted through My HR\". On 21 May the Manager wrote that she was still "
   "waiting for payroll confirmation. On 28 May she asked the Appellant to sign a validation of "
   "claims older than three months so that it could be escalated for delegate approval.", SUBP)]
s += q(list(range(182,198)))

s += [P("<b>S2.4 &nbsp;Who could submit the correction.</b> The myHR submissions report produced by "
   "Metro South Health records seven submissions for the Appellant in the period 1 February to "
   "31 May 2024, of which five were Attendance Variation and Allowance Claims. It records the "
   "initiator of each of those five as the Manager, and the initiator of no such claim in that period "
   "as the Appellant.", SUBP)]
s += q(list(range(198,203)))

s += [P("<b>S2.5 &nbsp;The state of the record, and the Respondent's pleaded position.</b> The report "
   "records the claim submitted on 28 May 2024, with an effective date of 30 March 2024 and a "
   "processing date of 30 May 2024, with a status of \"Part Completed\", and records the status of "
   "every other such claim in the period as \"Completed\". Neither of the two claim reference numbers "
   "identified by Payroll on 3 May 2024 appears in the report at all. The Respondent pleads that any "
   "discrepancies or errors were remedied in a timely manner and that there are no outstanding "
   "underpayments. On 18 February 2026 it admitted the Payroll instruction of 3 May 2024, the fact "
   "that the Manager submitted the claim on 28 May 2024, and the email of 21 May 2024.", SUBP)]
s += q(list(range(203,211))+[296,297,298])

s += [P("<b>S2.6 &nbsp;Rostering practices raised with Human Resources.</b> On 20 May 2024 at 4:07 pm "
   "the Director wrote to LBH_HR following up a query she had raised in relation to an email received "
   "from a staff member about the department's rostering practices, asking that someone call her "
   "regarding those staff concerns, and attaching the Queensland Health Fatigue Risk Management "
   "Systems Implementation Guideline.", SUBP)]
s += q([222,223])

s += [P("<b>STRESSOR 3 &mdash; THE ROSTER AND FATIGUE</b>", SEC),
 P("<b>S3.1 &nbsp;The rostering history, and the Appellant's proposals.</b> A rostering error in "
   "August 2023 was acknowledged by the Manager, who offered to roster the Appellant off the "
   "following day to give the required rest period, and by the Director, whose email of 7 August 2023 "
   "the Respondent admitted on 18 February 2026 as stating that there had been a rostering error that "
   "was accidentally made. The Appellant applied in writing to increase his hours to a full-time "
   "rotational roster, confirmed he was able and willing to work any roster presented to him, "
   "expressed willingness to take additional night shifts, and provided a draft roster spreadsheet. "
   "The Director requested a document recording his rostered shifts over the preceding eight months.", SUBP)]
s += q([28,30,31,33,35,156,157,159,287])

s += [P("<b>S3.2 &nbsp;The rostering errors acknowledged, and the decision withheld.</b> On "
   "26 April 2024 the Director wrote referring to a meeting on 16 April 2024 at which the Appellant "
   "had raised a roster line ending with night shifts followed by three days off and then returning "
   "to night shifts, and stated that the Manager was working to fix that error and would get in touch "
   "about alternative shifts. The Respondent does not allege that she did so. On 1 May 2024 the "
   "Appellant referred to section 4, clause 10.4.1 of the Operations Manual, which includes a toolkit "
   "required by management to manage fatigue, and stated that he had forwarded the toolkit to the "
   "Manager the previous week for review and action but had received no feedback; the Respondent does "
   "not allege that it was reviewed or that feedback was given before 18 June 2024. On 8 May the "
   "Director replied that she was following up with Human Resources. On 10 May 2024 at 2:08 pm she "
   "wrote to Human Resources forwarding his email, stating that she understood him to be raising "
   "concerns about how his manager was rostering and its impact on staff fatigue, that she and the "
   "Manager had run through the Roster Risk Assessment Matrix and put the rating at best at 11, "
   "moderate, that \"I acknowledge there has been a few rostering errors made by Chloe with regards "
   "to Cory's line in past rosters\", and that \"Cory's roster will not be considered, however Cory "
   "is not yet aware of this as we cannot advise what is the roster we are planning on going with "
   "before we send out the implementation plan for this business case for change\". On 21 May 2024 "
   "she asked the Appellant which particular changes or directives had concerned him.", SUBP)]
s += q(list(range(211,222))+[80])

s += [P("<b>S3.3 &nbsp;The Respondent's pleaded position on the roster.</b> On 18 February 2026 the "
   "Respondent denied paragraphs of the Appellant's earlier notice on the stated grounds \"because "
   "the comparator used does not represent a true comparator in the circumstances and because the "
   "roster was equitable\". In November 2024 the employer released a Consultation Paper stating that "
   "the proposed roster \"is intended to introduce a more equitable roster for Switchboard Services, "
   "Logan Hospital staff\", and that it included \"Redistribution of nights for greater equity based "
   "on FTE\", a \"Rotational roster for predictability and equity to all staff ensuring fair "
   "distribution of penalties\", an additional eight-hour Saturday shift to assist with call volume, "
   "and the extension of a five-hour weekday shift to eight hours.", SUBP)]
s += q([299,171,172,173,174,175])

s += [P("<b>S3.4 &nbsp;The shifts of 17 and 18 March 2024.</b> The Appellant was rostered to finish "
   "at 23:00 on 17 March 2024 and to commence at 06:00 on 18 March 2024, a break of seven hours. The "
   "shift commencing on 18 March fell on a Monday. The Respondent does not allege that those "
   "consecutive shifts arose from a staff-initiated shift swap.", SUBP)]
s += q(list(range(17,26))+list(range(224,228))+[234])

s += [P("<b>S3.5 &nbsp;The standard, as admitted.</b> The review decision records that the employer's "
   "own response included an extract of the Award stating that employees must be provided with a "
   "break of not less than ten hours between the termination of one shift and the commencement of "
   "another, and that eight hours applied instead of ten only in specific circumstances. On "
   "18 February 2026 the Respondent admitted that \"The Employer's 'Fatigue Risk Management Policy' "
   "and the relevant Award require a minimum break of 10 hours between shifts, or 8 hours by written "
   "agreement\", and admitted that the shifts of 17 and 18 March 2024 resulted in \"a break of only "
   "7 hours\". It denied a further paragraph of that notice on the ground that in June 2020 the "
   "Appellant signed an agreement allowing an 8-hour break.", SUBP)]
s += q([257,284,285,286])

s += [P("<b>S3.6 &nbsp;The agreement of 17 June 2020, and its scope.</b> By email of 7 July 2026 a "
   "Senior Consultant, Human Resources wrote that the 8-hour agreement signed on 17 June 2020 allows "
   "the Appellant to work with only an 8-hour break, \"however this is only applied where staff "
   "initiated shift swaps have occurred\". The Respondent pleads that in June 2020 the Appellant "
   "signed an agreement allowing an 8-hour break, and that the Appellant could refuse shifts at any "
   "time. The role description states, under mandatory requirements, that the position is a "
   "continuous shift working role and that the occupant must be able to work a roster which covers "
   "multiple shifts over a 24/7 period.", SUBP)]
s += duty([13])
s += q([232,233])

s += [P("<b>S3.7 &nbsp;The emergency workload carried on those shifts.</b> The emergency workload "
   "carried on those shifts is recorded in the employer's Emergency Code Register. Those paragraphs "
   "were not admitted by the Respondent and will be proved by the register and any other admissible "
   "evidence.", SUBP)]
s += q([228,229,230,231])
s += [P("[TO BE ADMITTED &mdash; the 2024 Emergency Code Register, a Metro South Hospital and Health "
   "Service workbook kept at Logan Hospital Switchboard, produced at Tab 31. Production was requested "
   "of the Respondent on 9 September 2026; the reply of 10 September 2026 seeks until 25 September "
   "2026. Paragraph 268 above is the employer's own statement that a spreadsheet of recorded MET "
   "calls is available for that period.]", NOTE),

 P("<b>S3.8 &nbsp;The leave of 19 March 2024.</b> The Leave Takings Report produced by Metro South "
   "Health in respect of 19 March 2024 records the Leave Category as \"Sick\", the Leave Type as "
   "\"Sick Leave\", the Time Code as \"SCK\", the Leave Taken as 7.60 hours and the Leave Status as "
   "approved. The Respondent pleads that the Appellant took leave on that day but that it was paid "
   "leave, and that pursuant to clause 18.10 of the Award he is not entitled to fatigue leave because "
   "he was not performing overtime.", SUBP)]
s += q([235,236,237])

s += [P("<b>S3.9 &nbsp;The enquiry of 8 April 2024, the delay, and the refusal of 1 May 2024.</b> On "
   "8 April 2024 the Appellant emailed the Manager requesting a review of his payment for the period "
   "8 to 31 March 2024, noting the Award requirement as to a minimum ten-hour break. On 9 April she "
   "replied that she had escalated his enquiry regarding fatigue leave to Human Resources to confirm "
   "policies around this, acknowledged the importance of communication, and requested that he raise "
   "concerns with her as soon as they arose so she could action them sooner. On 24 April he emailed "
   "expressing dissatisfaction that more than two weeks had passed without response or payment. The "
   "Respondent does not allege that any response was made between 9 April and 1 May 2024, an interval "
   "of 23 days. On 1 May she responded that after a consultation with payroll and Human Resources the "
   "request for fatigue payment for 18 March 2024 would not be processed, on the basis of the "
   "existing 8-hour agreement, noting that he was able to terminate that agreement going forward. The "
   "review decision records that payroll was, as at that date, still reviewing his entitlements; that "
   "the employer's response did not mention the shift of 18 March 2024; and that there was "
   "uncertainty between the Appellant and the employer as to whether the 8-hour agreement continued "
   "to apply.", SUBP)]
s += q(list(range(242,255)))

s += [P("<b>S3.10 &nbsp;The employer's own fatigue policy.</b> The review decision records that the "
   "policy regarding fatigue leave following weekends and rostered days off is dated June 2020, and "
   "that the policy notes that many problems can be overcome regarding fatigue leave by either not "
   "rostering the employee who is on call for the first shift of the following day, or not rostering "
   "on call an officer who is rostered for the first shift on the following day.", SUBP)]
s += q([239,240])

s += [P("<b>S3.11 &nbsp;The absence of fatigue risk management at the Switchboard.</b> The matters "
   "pleaded at S1.15 above are repeated. The employer states that the fatigue risk management records "
   "do not exist, that the mandatory training applies only to health practitioners and clinical "
   "assistants, and that fatigue risk management assessment at the Switchboard was implemented only "
   "after 30 June 2024.", SUBP),

 P("<b>S3.12 &nbsp;The findings in the decision under appeal.</b> The Respondent's own review "
   "decision of 24 October 2024 finds that the break between the shifts equated to seven hours; that "
   "even on the employer's own account the Appellant left a maximum of thirty minutes early and still "
   "did not receive a minimum eight-hour break; that the rostering of those two shifts amounted to "
   "unreasonable management action, given that it was in direct contradiction to the Award and the "
   "8-hour agreement; that the Appellant sustained a personal injury of a psychological nature; and "
   "that his injury arose out of employment, to the extent that it arose out of factors 2, 3 and 4, "
   "where employment was a significant contributing factor.", SUBP)]
s += q(list(range(258,263)))


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
   "being <b>a significant contributing factor</b>. The injury is the diagnosed condition identified at "
   "Part A, arising from the course of conduct pleaded at Part B.2 and not from an event on a single "
   "day. The Respondent's own review decision so finds.", PLD),
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
 P("<b>6. &nbsp;<i>Delaney</i>.</b> Where multiple management actions form a course of conduct, "
   "their reasonableness may be evaluated in context and as a whole. That evaluation must "
   "nevertheless first identify the circumstances that constitute management action. Operational "
   "conditions that are not management action do not become management action merely because they "
   "occurred alongside management decisions.", PLD),
 P("<b>7. &nbsp;<i>Mahaffey</i>.</b> The presence of reasonable management action among the "
   "circumstances contributing to an injury does not necessarily enliven the exclusion where an "
   "unreasonable management action, or a circumstance that is not management action, also had a "
   "sufficient causal connection to the disorder. The rostering of the shifts on 17 and 18 March "
   "2024 was found in the review decision to constitute unreasonable management action. The "
   "Appellant relies upon the medical and contemporaneous evidence to establish its contribution as "
   "part of the pleaded course of causative circumstances.", PLD),
 P("<b>8. &nbsp;The effect of the admissions.</b> The admissions are made for this proceeding "
   "under rule 49 and are relied upon as evidence of the existence and terms of the documents "
   "admitted, and of the matters the Respondent's statement of facts and contentions and List of "
   "Documents do not contain. The Appellant does not contend that any admission determines the "
   "reasonableness of any conduct; that is a matter for the Commission.", PLD),
 P("<b>9. &nbsp;The hearing de novo.</b> The Respondent says no finding in Review Decision 69983 "
   "binds the Commission. That is accepted, and it applies to the whole of the decision. The "
   "conclusion under appeal is a conclusion of that decision, reached upon the findings recorded in "
   "it.", PLD),
 P("<b>10. &nbsp;The Respondent's pleaded case.</b> Paragraph 27 of the amended statement of facts "
   "and contentions does not identify, by particular, date, document or cross-reference, the "
   "management action relied upon. No disciplinary process, formal performance management or "
   "communication described as a warning before 18 June 2024 is alleged.", PLD)]
s += q([238,295,300,301,302,303])

s += [P("PART D &mdash; ORDERS SOUGHT", PART),
 P("1. The appeal be allowed. 2. The decision of the Respondent dated 24 October 2024 be set aside. "
   "3. It be declared that the Appellant sustained an injury within the meaning of section 32 of the "
   "Workers' Compensation and Rehabilitation Act 2003. 4. The Appellant's application for "
   "compensation be accepted. 5. Costs reserved.", PLD)]

s = [x for x in s if x is not None]
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
out = ("out/FORM9A_SECOND_AMENDED_FOR_FILING.pdf" if SERVE else
       "INTERNAL/2026-09-12_FORM9A_SECOND_AMENDED_original_architecture_onus_accepted.pdf")
pdf.save(out,linearize=True)
print(f"built {out} - {n} page(s)")
