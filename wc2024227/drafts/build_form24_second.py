#!/usr/bin/env python3
"""WC/2024/227 - SECOND NOTICE TO ADMIT FACTS (r 49), v2, built 20 August 2026.
Schedule of facts for the approved Form 24. Every item is a fact ABOUT A DOCUMENT the Respondent
already holds. No conclusions, no characterisations, no compound items. Metadata stripped.
"""
import pikepdf, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=12,
                    leading=15.5, spaceAfter=3, alignment=1)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.2,
                      leading=12.2, spaceAfter=5)
CEN = ParagraphStyle('CEN', parent=BODY, alignment=1)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.1, leading=10.7,
                       textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=8.6, leading=11.8,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
ITEM = ParagraphStyle('ITEM', parent=BODY, leftIndent=10, spaceBefore=3, spaceAfter=3)
def P(t, s=BODY): return Paragraph(t, s)

R_TAYLOR = "Respondent's disclosure from witness conferencing (C Taylor)"
R_REESE  = "Respondent's disclosure from witness conferencing (T Reese)"
R_FRMS   = "Respondent's disclosure from witnesses (fatigue risk management content)"
CE       = "Letter of Metro South Health, 5 June 2026 (ref K-LM26/729)"
R_PAY    = "Respondent's disclosure from witness conferencing (Queensland Health Payroll)"
HR11     = "myHR submissions report for the Appellant, 1 February to 31 May 2024, produced by Metro South Health as Item 11 of the notice of non-party disclosure"

FACTS = [
 ("A", "THE ROLE, AND WHAT IT REQUIRED"),
 (1, "Metro South Hospital and Health Service produced a role description for the position of Administration Officer, Switchboard Services, Logan Hospital, which states the classification as \"A03\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (2, "That role description states: \"The occupant of this position is required to work continuous shift work over the full 24-hour period, 7 days a week\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (3, "That role description states: \"This position reports to the Switchboard Manager, Corporate Services, Logan Hospital\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (4, "That role description names the contact for the position as \"Chloe Taylor\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (5, "That role description states, as a key responsibility: \"Maintain call queues to minimum at all times\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (6, "That role description states, as a key responsibility: \"Collate information and maintain Omnivista database and SharePoint to ensure information held within Switchboard Services is accurate and appropriate\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (7, "That role description states, as a key responsibility: \"Provide a service to support hospital staff in the allocation, coordination, and fault repair of all pager units for the hospital. This includes allocating pagers to hospital staff and submitting paging units for repair, maintaining database and registers with accurate and current information\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (8, "That role description states, as a key responsibility: \"Participate in the Emergency Response process by receiving emergency response notifications and distributing them to the appropriate response groups, dependent on the category of emergency, as per emergency code procedures, strictly adhering to protocols and timeframes\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (9, "That role description states, as a key responsibility: \"Maintain discretion and exercise judgement where necessary to resolve problems within the scope of your role; in situations where precedence have not been set and procedures not defined\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (10, "That role description states, as a key responsibility: \"The ability to multitask and operate under pressure, particularly where high volume call traffic is concerned\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (11, "That role description states, as a key responsibility: \"Ability to work effectively as an individual with limited supervision to meet deadlines and establish work priorities, and work as a member of a multi-disciplinary team in a changing environment\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (12, "That role description states, as a key responsibility: \"Follow defined service quality standards, occupational health and safety policies and procedures relating to the work being undertaken to ensure high quality, safe services and workplaces\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (13, "That role description states, under mandatory requirements: \"The position is a continuous shift working role. You must be able to work a roster which covers multiple shifts over a 24/7 period\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (14, "Metro South Hospital and Health Service approved three movement forms recording changes to the Appellant's working hours, dated 27 February 2026, 17 April 2026 and 9 June 2026, each approved by Mr Scott Hughes as delegate.",
     "Movement forms recording approved changes to working hours, approved by Mr S Hughes as delegate"),
 (15, "Each of those three movement forms records the Appellant's shift arrangements as \"Continuous Shift Worker\".",
     "Movement forms recording approved changes to working hours, approved by Mr S Hughes as delegate"),
 (16, "The Respondent does not allege that the Appellant ceased to be a continuous shift worker at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 ("B", "THE HOURS THE APPELLANT SOUGHT, AND OBTAINED"),
 (18, "On 7 August 2023 at 12:21 pm the Appellant sent an email to Ms Chloe Taylor, Ms Tammy Reese, Ms Patricia Conaghan and Ms Tracey Smith, marked of High importance, which states: \"Furthermore, to meet the demands and the additional hours of the department both Patricia Conaghan and I would like to formally adhoc an additional 2 shifts per fortnight.\"",
     "R_REESE"),
 (19, "That email sets out clause 11.7 of the applicable agreement, headed \"Additional Permanent Hours for Part-time Employees\".",
     "R_REESE"),
 (20, "On 8 August 2023 at 6:06 pm the Appellant sent an email to Ms Reese which states: \"I can confirm that I will be in tomorrow 0700-1500 9th August. I was also looking to pick up another shift if possible.\"",
     "R_REESE"),
 (21, "On 8 August 2023 at 4:15 pm Ms Reese sent an email to the Appellant which states: \"can I ask were you looking for another shift on top of those 8 to replace the shift missed today also?\"",
     "R_REESE"),
 (22, "On 31 August 2023 the Appellant provided to Ms Taylor a written application headed \"Request to Increase Working Hours to Full Time Rotational Roster\".",
     "R_REESE"),
 (23, "That application states: \"I have also expressed my willingness to take on additional night shifts as part of the roster and advocacy to become a union representative for the switchboard department.\"",
     "R_REESE"),
 (24, "That application of 31 August 2023 records the Appellant's intention to become the Switchboard union delegate, in the same sentence as his willingness to take on additional night shifts.",
     "R_REESE"),
 (25, "On 4 September 2023 the Appellant sent an email to Ms Reese which states: \"I confirm that I am able and willing to work any roster that is presented to me, including the current schedule with full 24-hour availability.\"",
     "R_REESE"),
 (26, "That email states: \"I have no issues with shift work.\"",
     "R_REESE"),
 (27, "That email attached a draft roster spreadsheet prepared by the Appellant.",
     "R_REESE"),
 (28, "On 8 September 2023 at 11:42 am Ms Reese sent an email to the Appellant which states: \"I am glad to hear things seem to be going well with Chloe and I am also glad to hear you applied for the additional shifts through the recent EOI.\"",
     "R_REESE"),
 (29, "On 27 September 2023 at 1:52 pm Ms Taylor sent an email to the Appellant with the subject \"Approved - Permanent Full Time FTE\" which states: \"Just giving you an update on your application for Permanent Fulltime hours, I am very pleased to advise you that this has been approved.\"",
     "Email of Ms C Taylor, 27 September 2023"),
 (30, "That email states: \"happy to commence Full-time hours from the 16th October 2023\".",
     "As above"),
 ("C", "STRESSOR 1(a) - THE DATABASE, AND THE DIRECTIVES ISSUED WITHOUT CONSULTATION"),
 (31, "On 18 July 2023 at 12:56 pm Ms Ellen Stibbard, Switchboard Telecommunications Coordinator, sent an email to the Appellant and the Switchboard team, subject \"Hello & Update\", which states: \"My current role is a project role for the Switchboard team. It is a temporary position that predominantly focuses on fixing up the database that switchboard utilises.\"",
     "Email of Ms E Stibbard, 18 July 2023, produced under Tab 1 of the Stressor 1(a) particulars bundle served 11 August 2026"),
 (32, "That email states: \"While I am fixing up the database and all of its entries, I will be removing everyone's access to the database.\"",
     "As above"),
 (33, "That email states that Ms Stibbard's working hours for that purpose were \"every Tuesday and second Monday, 8:00 - 16:00\", that any entry was to be requested from her directly at any time, that an urgent entry needed on a day she was not there was to be sent to Ms Taylor instead, and that a request made \"after hours (overnights, on the weekend or public holiday)\" would \"have to wait until either Chloe or myself are back\".",
     "As above"),
 (34, "That email states: \"I have also removed the Contact & Number Changes book out of the room, as I would prefer, for now, to be sent all changes to my email.\"",
     "As above"),
 (35, "Review Decision 69983 records: \"On 19 April 2024, Ms Taylor emailed the team and expressed that due to errors being made with respect to data entry, a new process was to be followed which included more checks to ensure accuracy of data entry.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (35, "The Respondent does not allege that the role description for the position of Administration Officer, Switchboard Services was amended at any time after 18 July 2023.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (36, "The Respondent does not allege that access to the database used by the Switchboard was restored to the Appellant at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (37, "On 16 June 2023 the Appellant wrote raising, among other workplace issues: \"No consultation of the team members or the department when making major changes such as additional shift... commence/finish [times].\"",
     "Affidavit of the Appellant (Form 20) filed 23 June 2026"),
 (38, "The Respondent's amended List of Documents dated 14 August 2026 lists at item 26 an attachment described as \"Email: Task change switchboard - 19/04/2024\", and at item 27 an attachment described as \"Email: MASPER process - 09/05/2024\".",
     "Respondent's amended List of Documents dated 14 August 2026"),
 (39, "On 9 May 2024 at 9:20 am Ms Taylor sent an email to Dr Vivian Kwok and Dr Pan Jane Wong, subject \"RE: Switchboard issues 5 May, 7 May, and 8 May\", which states: \"Can I please confirm your business hours so we can have this for our reference, it is not provided on the rosters. I have noticed your dect phone number #5997 is currently switched off.\"",
     "MASPER register email records, 9-15 May 2024, produced under Tab 3 of the Stressor 1(a) particulars bundle served 11 August 2026"),
 (40, "On 9 May 2024 at 10:15 am Ms Taylor sent an email to Logan Switch, copied to Switchboard staff including the Appellant, subject \"MASPER process\", directing that \"all calls that switch transfer to the MASPER phone #5223 are being introduced\".",
     "MASPER register email records, 9-15 May 2024, produced under Tab 3 of the Stressor 1(a) particulars bundle served 11 August 2026"),
 (41, "On 21 May 2024 Ms Reese asked the Appellant to identify the directives about which he had consultation concerns.",
     "Affidavit of the Appellant (Form 20) filed 23 June 2026"),
 (42, "On 15 April 2024 at 12:39 pm Ms Taylor sent an email to Logan Switch, copied to Ms Reese and to Switchboard staff including the Appellant, with the subject \"Afterhours Oncall Process - Switchboard\".",
     "Email of Ms C Taylor, 15 April 2024, 12:39 pm, \"Afterhours Oncall Process - Switchboard\", produced at Annexure A Tab 6"),
 (43, "That email states: \"Process during office hours remains the same, please contact myself through switch/office or mobile unless otherwise advised.\"",
     "Email of Ms C Taylor, 15 April 2024, 12:39 pm, \"Afterhours Oncall Process - Switchboard\", produced at Annexure A Tab 6"),
 (44, "That email states: \"This new process is effective from today.\"",
     "Email of Ms C Taylor, 15 April 2024, 12:39 pm, \"Afterhours Oncall Process - Switchboard\", produced at Annexure A Tab 6"),
 (45, "That email states: \"You will see that Ellen and myself have added Afterhours on call, the days that are highlighted in purple show who is on call after hours.\"",
     "Email of Ms C Taylor, 15 April 2024, 12:39 pm, \"Afterhours Oncall Process - Switchboard\", produced at Annexure A Tab 6"),
 (46, "Ms Taylor signed that email as \"A/Switchboard Manager\".",
     "Email of Ms C Taylor, 15 April 2024, 12:39 pm, \"Afterhours Oncall Process - Switchboard\", produced at Annexure A Tab 6"),
 (47, "Ms Taylor's email to all Switchboard staff of 17 May 2024 at 9:30 am states: \"My office hours can vary due to having to take my girls to school in the morning, on the days that I do have school drop off I always let switch know that I will be in later between 0800-830am. Otherwise my hours are from 06:30-14:30.\"",
     "R_TAYLOR"),
 (48, "That email states: \"Moving forward so communication is clear for the team, I will be sending an email to switch to advise of any change to my office hours for the week.\"",
     "R_TAYLOR"),
 (49, "On 17 May 2024 at 1:20 pm Ms Taylor sent an email to Ms Adriana McNamee with the subject \"FW: Office Hours and Departmental Directives\", which states: \"when staff call in for any leave to please contact me either via switch, office or my mobile.\"",
     "R_TAYLOR"),
 (0, "On 15 May 2024 at 1:15 pm the Appellant sent an email to Ms Taylor and Logan Switch, copied to Switchboard staff, Ms Reese and LBH_HR, with the subject \"Office Hours and Departmental Directives\", which states: \"could you please share your office hours so the entire department can be aware of your regular schedule? There has been some noted inconsistency in your arrival and departure times\".",
     "R_FRMS"),
 (0, "That email of the Appellant states: \"please ensure that any directives and changes within the department is made in consultation with the team to ensure that any concerns can be appropriately addressed.\"",
     "R_FRMS"),
 (0, "On 15 May 2024 at 6:23 pm Ms Reese replied to the Appellant, copied to Ms Taylor and marked of High importance, stating that his email \"did not demonstrate our iCARE2 value of Respect and did not comply with our Code of conduct\".",
     "R_FRMS"),
 (0, "That reply of Ms Reese asked the Appellant to retract his email.",
     "R_FRMS"),
 (0, "On 15 May 2024 at 7:09 pm the Appellant replied to Ms Reese stating: \"Requesting clarity on business hours is a reasonable question, especially when no one in the department can provide a definitive answer in response to directives to contact Chloe during office hours.\"",
     "R_FRMS"),
 (0, "On 21 May 2024 at 2:53 pm Ms Reese replied to the Appellant stating: \"With regards to your concerns about having more clarity as to what are Chole's business hours I will follow up on the issues raised.\"",
     "R_FRMS"),
 (0, "That reply of Ms Reese states: \"can I ask was there one or more particular changes and/or directives where you had concerns about consultation and communication?\"",
     "R_FRMS"),
 (0, "The email of Ms Taylor to Ms McNamee of 17 May 2024 at 1:20 pm states, of the Appellant's telephone call of 13 May 2024: \"I told him I am more than happy to cover his shift and if he was unwell, it would be preferred for him not to come into work.\"",
     "R_FRMS"),
 (0, "That email of Ms Taylor states: \"I sent an email (attached) to advise Cory again of the call process and a query about his leave. I also sent a follow up text, advised by the last HR rep to also follow up with a text to Cory\".",
     "R_FRMS"),
 (0, "That email of Ms Taylor records that on each of 13, 14 and 15 May 2024 the Appellant notified his unavailability by telephoning the Switchboard.",
     "R_FRMS"),
 (0, "The Respondent has not disclosed any document recording that Ms McNamee sought the Appellant's account of the matters described in Ms Taylor's email of 17 May 2024 at 1:20 pm.",
     "The Respondent's disclosure in this proceeding"),
 ("D", "STRESSOR 1(a) - THE DELAY IN COMMUNICATION AND THE MATTERS RAISED IN MAY 2024"),
 (50, "On 15 May 2024 at 11:47 am Ms Sue Marriott, Administration Officer, Integrated Respiratory Service, sent an email to Logan Switch, marked of High importance, which states: \"Could you please amend your number registry/directory to show #8768 belongs to the Integrated Respiratory Service... We are not Respiratory Medical OPD and we do not have any doctors working out of this area.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (51, "On 20 May 2024 at 11:03 am Ms Marriott sent a further email to Logan Switch, marked of High importance, which states: \"Just a courtesy reminder, we continue to get calls put through to us for Respiratory Medical Outpatients... we can not help patients or other clinical staff with OPD issues.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (52, "The email of Ms Marriott of 20 May 2024 at 11:03 am was sent five days after her email of 15 May 2024 at 11:47 am.",
     "Respondent's disclosure - the Integrated Respiratory Service email chain, 15-20 May 2024"),
 (53, "The office hours stated by Ms Taylor in her email of 17 May 2024 at 9:30 am concluded at 2:30 pm.",
     "R_TAYLOR"),
 (54, "On 20 May 2024 at 2:05 pm the Appellant sent an email to Ms Taylor, marked of High importance, which states: \"switchboard staff may not be aware of the clinics due to modifications to the Document: Outpatients Department - Clinic contact Details. on the 22nd of February 2024. I recommend a modification and review of the document.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (55, "That email of the Appellant was sent within the office hours Ms Taylor had stated to all Switchboard staff on 17 May 2024, and twenty-five minutes before the conclusion of those hours.",
     "R_TAYLOR"),
 (56, "That email of the Appellant was sent from the Logan Switch account.",
     "Respondent's disclosure - the Integrated Respiratory Service email chain, 15-20 May 2024"),
 (57, "On 20 May 2024 at 4:30 pm Ms Taylor replied to the Appellant, stating: \"Thank you for bringing this to my attention however this task was being actioned. I had discussed with Richard this morning about the update of outpatients respiratory/medical.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (58, "That reply of Ms Taylor states: \"Taking note of your recommendation, we can also put the updated procedures out to the team for consultation before implementing.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (0, "That reply of Ms Taylor was sent two hours after the conclusion of the office hours she had stated to all Switchboard staff on 17 May 2024.",
     "R_TAYLOR; and the Respondent's own disclosure"),
 (59, "Mr Richard Parry was at that time a member of the Switchboard staff at Logan Hospital, and was addressed as such in Ms Stibbard's on-call roster email of 13 May 2024 and Ms Taylor's \"Switchboard Manager - On call and Hours\" email of 17 May 2024.",
     "R_FRMS"),
 (60, "The Respondent has not disclosed any document recording a communication sent by Ms Taylor to Ms Marriott, or to the Integrated Respiratory Service, on 20 May 2024.",
     "The Respondent's disclosure in this proceeding"),
 (61, "The Respondent has not disclosed any document recording a communication sent by Mr Parry to Ms Marriott, or to the Integrated Respiratory Service, on 20 May 2024.",
     "The Respondent's disclosure in this proceeding"),
 (62, "The Respondent does not allege that any response was made to the email of Ms Marriott of 20 May 2024 at 11:03 am before 2:05 pm on that day.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (63, "The Respondent does not allege that any response was made to the email of Ms Marriott of 15 May 2024 at 11:47 am at any time before 20 May 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (64, "On 17 May 2024 at 9:30 am Ms Taylor sent an email to Logan Switch, copied to Ms Reese and to Switchboard staff, which states: \"regardless of my start/finish times next week you are to please contact me through the day/afterhours either via switch, office or mobile.\"",
     "R_TAYLOR"),
 ("E", "STRESSOR 1(c) - THE MATTERS RAISED IN AUGUST AND SEPTEMBER 2023, AND THE RESPONSE"),
 (65, "The Appellant's email of 7 August 2023 at 12:21 pm states: \"Please give me some space and stop with any further communication as I have had enough of it.\"",
     "R_REESE"),
 (66, "On 7 August 2023 at 1:43 pm Ms Taylor replied to the Appellant, copied to Ms Reese and Ms Smith, stating: \"My sincere apologises about your rostered Monday 7th 0700-1500 shift, I can confirm this was an oversight.\"",
     "R_REESE"),
 (67, "That email of Ms Taylor states: \"Would you like me to roster you off tomorrow Tuesday 8th 0700-1500 to give you the required rest period\".",
     "R_REESE"),
 (68, "On 7 August 2023 at 3:13 pm Ms Reese replied to the Appellant stating: \"As Chloe is your current line manager and as such you are required to continue to communicate with Chloe for work related issues, shift concerns, leave, etc.\"",
     "R_REESE"),
 (69, "On 7 August 2023 at 5:11 pm Ms Reese sent an email to Ms Taylor attaching a document titled \"Rostered shifts Cory S. past 8 months.xlsx\", which states: \"can I ask if you can send me an email of your recent communication with Cory about contacting yourself about missed shifts, as I could not find a copy of this email.\"",
     "R_REESE"),
 (70, "On 29 August 2023 at 6:57 pm Ms Reese sent the Appellant an email attaching HR Policy E12 - Individual Employee Grievances, and setting out how a grievance could be submitted.",
     "R_REESE"),
 (71, "On 4 September 2023 the Appellant replied to Ms Reese stating: \"I have also spoken to Chloe. We are seemingly on the path to working in a beneficial way and hopefully will not need to go through this process.\"",
     "R_REESE"),
 (72, "The Appellant did not submit a grievance under HR Policy E12 in 2023.",
     "R_REESE"),
 ("F", "THE PROCESS FOR NOTIFYING UNAVAILABILITY FOR A ROSTERED SHIFT"),
 (73, "On 14 May 2024 at 12:08 pm Ms Taylor sent an email to the Appellant, copied to Ms Reese, with the subject \"Sick leave 14.05.24\", which states: \"in business hours you are to follow the correct process and speak to me directly if its regarding emergent leave, you can contact me either through switch or my office/mobile.\"",
     "R_TAYLOR"),
 (74, "On 13, 14 and 15 May 2024 the Appellant notified his unavailability for his rostered shift by telephoning the Switchboard.",
     "Ms Taylor's email to Ms McNamee, 17 May 2024, which records each of those three calls"),
 (75, "The Respondent has not disclosed any document recording a process for notifying unavailability for a rostered shift at Logan Hospital Switchboard which was in force in May 2024.",
     "Respondent's amended List of Documents dated 14 August 2026; and the Respondent's disclosure in this proceeding"),
 (76, "The Respondent does not allege that any written procedure governing the notification of unavailability for a rostered shift at Logan Hospital Switchboard existed before 4 February 2025.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 ("O", "STRESSOR 1(g) - THE UNION DELEGATE, AND THE CONSULTATION ON ROSTERS"),
 (77, "The Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, December 2024, states: \"In accordance with Clause 6.2 of the Hospital and Health Service General Employees (Queensland Health) Award - State 2015, agreement between MSH and the union, or MSH and the majority of employees affected must occur prior to changes to a shift roster.\"",
     "Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health, December 2024"),
 (78, "That document states: \"Agreement is defined as obtaining consent from the majority (50+1%) of affected employees, with all affected employees invited to cast their vote via an online Ballot Form.\"",
     "Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health, December 2024"),
 (79, "The Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital states: \"On 22 July 2021, Metro South Health (MSH) management, affected staff and Together Queensland representatives commenced negotiating a new roster for Switchboard Services, Logan Hospital.\"",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (80, "That Consultation Paper states: \"In August 2024, Switchboard Services, Logan Hospital was realigned from Health Information Management Services (HIMS), MSH to Corporate Services, LBHS, MSH.\"",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (81, "That Consultation Paper states that the proposed roster \"is intended to introduce a more equitable roster for Switchboard Services, Logan Hospital staff\".",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (82, "That Consultation Paper states that the proposed roster includes: \"Redistribution of nights for greater equity based on FTE.\"",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (83, "That Consultation Paper states that the proposed roster includes: \"Rotational roster for predictability and equity to all staff ensuring fair distribution of penalties.\"",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (84, "That Consultation Paper states that the proposed roster includes: \"An additional eight (8) hour shift (0700-1500) on Saturdays, to assist with call volume.\"",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (85, "That Consultation Paper states that the proposed roster includes: \"Extension of the current weekday (Mon-Fri) 0900-1400 five (5) hour shift to a 0700-1500 eight (8) hour shift.\"",
     "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health"),
 (86, "The Consultation outcome document states that on 14 November 2024 a consultation document and proposed roster for Switchboard Services, Logan Hospital was released for consultation, and that affected staff, unions and stakeholders were invited to provide feedback by 8 December 2024.",
     "Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health, December 2024"),
 (87, "That document states that seventeen affected employees were invited to cast a vote, that seventeen votes were received, that fourteen \"Yes\" votes and three \"No\" votes were received, and that the proposed rosters were approved with a date effective of 20 January 2025.",
     "Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South Health, December 2024"),
 (88, "On 3 November 2025 Mr Heath Moran, Organiser, Together Queensland, sent an email to Ms Carolyn Jeffrey, Ms Patricia Conaghan and the Appellant which states: \"Firstly, congratulations to you all on being endorsed to become workplace delegates!\"",
     "Email of Mr Heath Moran, Organiser, Together Queensland, 3 November 2025 at 10:57 am"),
 (89, "The Appellant was endorsed as a workplace delegate on or about 3 November 2025.",
     "Email of Mr Heath Moran, Organiser, Together Queensland, 3 November 2025 at 10:57 am"),
 (90, "The period between April 2023, when the Appellant expressed interest in assuming the role of union delegate, and 3 November 2025, when he was endorsed as a workplace delegate, is approximately thirty-one months.",
     "Email of Mr Heath Moran, Organiser, Together Queensland, 3 November 2025 at 10:57 am"),
 (91, "The Respondent does not allege that agreement under clause 6.2 of the Hospital and Health Service General Employees (Queensland Health) Award - State 2015 was obtained before the rostering of the Appellant's shifts on 17 and 18 March 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (92, "The Respondent does not allege that a ballot of affected employees was conducted before the change to after-hours on-call arrangements notified by Ms Taylor on 15 April 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 ("G", "STRESSOR 2 - THE PAY CORRECTION, AND THE THREAD \"COREY SHEPHERD 388372 PAY ISSUES\""),
 (93, "The Respondent's disclosure contains an email thread with the subject \"Corey Shepherd 388372 Pay issues\".",
     "R_PAY"),
 (94, "The first message in that thread is dated 3 May 2024, is from PayrollMetroSouth, is addressed to Ms C Taylor, and is copied to the Appellant.",
     "R_PAY"),
 (95, "That message is signed \"Elaine Grant, Client Service Officer, Metro South Payroll Team, Payroll Transactional Services, Corporate Enterprise Solutions, Corporate Services | Queensland Health\".",
     "R_PAY"),
 (96, "That message states: \"Corey has wages top up on fortnight 05.02.24 for 0.95mins as he is under his contracted hours so it is toping up the missing wages from his RDO balance.\"",
     "R_PAY"),
 (97, "That message states: \"This will be due to having a 7hr shift on 09.02.24 instead of an 8hr shift. AVAC PRN 15397775.\"",
     "R_PAY"),
 (98, "That message states: \"The same has happened for the next fortnight 19.02.24 due to 28.02.24 shift AVAC PRN 15605601 has this shift as 7hrs topping up 0.95 for missing hour.\"",
     "R_PAY"),
 (99, "That message states: \"Fortnight 18.03.24 is the opposite and has too many ordinary shifts for the fortnight resulting in wage reduction of 7.55hrs as one of the shifts needs to be overtime.\"",
     "R_PAY"),
 (100, "That message states: \"Fortnight 01.04.24 is the same, 0.95hrs over contracted 76hrs needs to be overtime.\"",
     "R_PAY"),
 (101, "That message states: \"Please submit an AVAC to correct these shifts for each fortnight so Cory is paid corrected and his RDO balance will then be amended.\"",
     "R_PAY"),
 (102, "The thread contains a message dated 10 May 2024 at 2:21 pm from the Appellant, addressed to PayrollMetroSouth and to Ms E Grant.",
     "R_PAY"),
 (103, "The thread contains a message dated 13 May 2024 at 8:21 am from PayrollMetroSouth, addressed to the Appellant.",
     "R_PAY"),
 (104, "That message of 13 May 2024 states: \"I cannot see that any of the issues below have been corrected. Please speak to your Line Manager to have them corrected with an AVAC submitted through My HR as this will also be affecting your RDO balances as well as your pay.\"",
     "R_PAY"),
 (105, "The thread contains a message dated 21 May 2024 at 12:33 pm from Ms C Taylor, addressed to the Appellant, with the subject \"RE: Corey Shepherd 388372 Pay issues\".",
     "R_TAYLOR"),
 (106, "That message of 21 May 2024 states: \"Just letting you know that I am still I am waiting payroll confirmation about a few of these payroll issues and as soon as I do get that confirmation, I will submit an AVAC for next pay run. I will let you know PRN once it has been submitted.\"",
     "R_TAYLOR"),
 (107, "The Respondent's disclosure contains a message dated 28 May 2024 at 8:36 am from Ms C Taylor, addressed to the Appellant and copied to Ms T Reese, with the subject \"Validation of Claims older than 3 months - Please sign\".",
     "R_TAYLOR"),
 (108, "That message of 28 May 2024 states: \"Please find attached Validation of claims older than 3 months, please sign and return to be as soon as possible so I can escalate for delegate approval.\"",
     "R_TAYLOR"),
 (109, "The myHR submissions report produced as Item 11 records seven submissions for the Appellant in the period 1 February 2024 to 31 May 2024.",
     "HR11"),
 (110, "That report records five of those seven submissions as an \"Attendance Variation and Allowance Claim (AVAC)\".",
     "HR11"),
 (111, "That report records the initiator of each of those five Attendance Variation and Allowance Claims as \"Donovan-Taylor, Chloe\".",
     "HR11"),
 (112, "That report records the initiator of no Attendance Variation and Allowance Claim in that period as the Appellant.",
     "HR11"),
 (113, "That report records a submission with process number 16328886 as an Attendance Variation and Allowance Claim submitted on 15 May 2024, with a processing date of 16 May 2024, and a status of \"Completed\".",
     "HR11"),
 (114, "That report records a submission with process number 16450619 as an Attendance Variation and Allowance Claim submitted on 28 May 2024, with an effective date of 30 March 2024, a processing date of 30 May 2024, and a status of \"Part Completed\".",
     "HR11"),
 (115, "That report records the status of every other Attendance Variation and Allowance Claim in the period as \"Completed\".",
     "HR11"),
 (116, "That report records the following process numbers with the following submission dates: 15325947, submitted 6 February 2024; 15480560, submitted 20 February 2024; 15848692, submitted 27 March 2024; 15849573, submitted 27 March 2024; 15969838, submitted 9 April 2024; 16328886, submitted 15 May 2024; and 16450619, submitted 28 May 2024.",
     "HR11"),
 (117, "In that report, process numbers increase as submission dates increase.",
     "HR11"),
 (118, "The number 15397775 falls between 15325947 and 15480560.",
     "Arithmetic"),
 (119, "The number 15605601 falls between 15480560 and 15848692.",
     "Arithmetic"),
 (120, "Neither AVAC PRN 15397775 nor AVAC PRN 15605601 appears in that report.",
     "HR11"),
 ("H", "STRESSOR 3 - THE ROSTER, AND THE EMPLOYER'S KNOWLEDGE OF FATIGUE BEFORE 18 JUNE 2024"),
 (121, "On 26 April 2024 at 1:52 pm Ms Reese sent an email to the Appellant with the subject \"Roster Concerns\", referring to a meeting on 16 April 2024 at which the Appellant raised a roster line ending with night shifts followed by three days off and then returning to night shifts.",
     "R_REESE"),
 (122, "That email states that Ms Taylor \"was working to fix this error and would get in touch with you about what alternative shifts she could offer\".",
     "R_REESE"),
 (123, "On 1 May 2024 at 1:18 pm the Appellant sent an email to Ms Reese with the subject \"Re: Roster Concerns\" referring to section 4, clause 10.4.1 of the Operations Manual and stating: \"This section includes a toolkit required by management to manage fatigue and implement appropriate protocols and adhere to the workplace health and safety act.\"",
     "R_REESE"),
 (124, "That email states: \"I forwarded the toolkit to Chloe last week for review and action but have yet to receive feedback\".",
     "R_REESE"),
 (0, "That email of Ms Reese also states: \"I asked Chloe to follow upon what should be the interpretation of this section with HR\".",
     "R_REESE"),
 (125, "On 8 May 2024 at 9:08 am Ms Reese replied to the Appellant stating: \"Thanks for raising these observations and concerns. I am following up with regards to these with HR for further advice and I will get back to you asap with a response.\"",
     "R_REESE"),
 (126, "On 10 May 2024 at 2:08 pm Ms Reese sent an email to Mr Mackenzie Pritchard of Human Resources forwarding the Appellant's email of 1 May 2024, which states: \"I think he is trying to raise that he has concerns over how his manager is rostering for the Switchboard team and how it is impacting on staff fatigue, or more specifically his fatigue.\"",
     "R_FRMS"),
 (127, "That email states: \"as per Cory's second extract detailing the Roster Risk assessment Matrix, Chloe and I have run thought this and we say at best there would be a rating of 11 which is moderate\".",
     "R_FRMS"),
 (128, "That email states: \"I acknowledge there has been a few rostering errors made by Chloe with regards to Cory's line in past rosters\".",
     "R_FRMS"),
 (130, "On 20 May 2024 at 4:07 pm Ms Reese sent an email to LBH_HR which states: \"I am just following up on this query I raised a little while ago in relation to a email I had received from a staff member about our rostering practices. Thus if someone might be able to give me a call regarding these staff concerns, that would be great.\"",
     "R_FRMS"),
 (129, "That email of Ms Reese to LBH_HR attached the document \"qh-gdl-401-3.3\", being the Queensland Health Fatigue Risk Management Systems Implementation Guideline.",
     "R_FRMS"),
 ("I", "STRESSOR 3 - THE BREAK OF 17-18 MARCH 2024, THE 2020 AGREEMENT, AND THE LEAVE OF 19 MARCH 2024"),
 (131, "By email dated 7 July 2026 Ms Lyndelle Forrest, Senior Consultant, Human Resources, Logan and Beaudesert Health Service, wrote to the Appellant stating that the roster \"provides more than 10-hour breaks between shifts\".",
     "Email of Ms L Forrest, Senior Consultant HR, 7 July 2026"),
 (132, "That email states: \"acknowledge you also signed an 8 hour agreement on 17 June 2020, which allows you to work with only an 8 hour break, however this is only applied where staff initiated shift swaps have occurred.\"",
     "Email of Ms L Forrest, Senior Consultant HR, 7 July 2026"),
 (133, "The Respondent does not allege that the consecutive shifts of 17 and 18 March 2024 arose from a staff initiated shift swap.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (134, "The Leave Takings Report produced by Metro South Hospital and Health Service in respect of 19 March 2024 records the Leave Category as \"Sick\", the Leave Type as \"Sick Leave\", the Time Code as \"SCK\", the Leave Taken as 7.60 hours, and the Leave Status as \"APPROVED\".",
     "Item 15 QH Leave Takings Report, produced by Metro South Health"),
 (135, "The Respondent's amended statement of facts and contentions dated 13 May 2026 states at paragraph 24(a): \"says that the appellant took leave on 19 March 2024 but says this was paid leave\".",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (136, "That amended statement of facts and contentions states at paragraph 24(b): \"says that pursuant to clause 18.10 of the Award, the appellant is not entitled to fatigue leave, because he was not performing overtime\".",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (137, "That amended statement of facts and contentions states at paragraph 27: \"The respondent contends that any management action involved in the causation of any injury to the Plaintiff was reasonable management action taken in a reasonable way pursuant to s 32(5) WCRA.\"",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (138, "Applying paragraph 24(b) of the Respondent's amended statement of facts and contentions to the shifts of 17 and 18 March 2024 identified in Review Decision 69983, no fatigue leave was available to the Appellant under clause 18.10 of the Award in respect of those shifts.",
     "Respondent's amended statement of facts and contentions, 13 May 2026, paragraph 24(b); and Review Decision 69983 dated 24 October 2024"),
 (139, "Review Decision 69983 records that the policy regarding fatigue leave following weekends and rostered days off is dated June 2020.",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (140, "That decision records: \"The policy notes that many problems can be overcome regarding fatigue leave by either not rostering the employee who is on call for the first shift of the following day and not rostering on call an officer who is rostered for the first shift on the following day.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (141, "That decision records that section 23 of the Hospital and Health Service General Employees (Queensland Health) Award provides that \"where an employee is in receipt of the additional week's leave as prescribed in clause 19.2(a) and is rostered off on Easter Saturday, Easter Sunday, Show Day or Labour Day, such employee shall be paid an additional day's wage or be granted a day's holiday in lieu at a time to be mutually arranged, but this is not applicable where an employee is not ordinarily required to work on a Saturday or Sunday\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 ("J", "THE EMPLOYER'S OWN STATEMENTS ABOUT ITS SYSTEMS AND RECORDS"),
 (142, "By letter dated 5 June 2026, reference K-LM26/729, signed by Ms Noelle Cridland as Chief Executive of Metro South Hospital and Health Service and addressed to Commissioner Dwyer, Metro South Health stated in relation to Item 4: \"the requested documents do not exist. Mandatory Fatigue Risk Management System training only applies to health practitioners and clinical assistants. The Logan Hospital Switchboard staff are non-clinical staff, and therefore there is no mandatory requirement for them to complete Fatigue Risk Management System training.\"",
     "CE"),
 (143, "That letter states in relation to Item 5: \"The implementation of fatigue risk management assessment at Switchboard Logan Hospital occurred after 30 June 2024 in connection with an organisational change related to the reporting lines for Switchboard.\"",
     "CE"),
 (144, "That letter states in relation to Item 7: \"the requested documents do not exist. Mandatory Fatigue Risk Management System training only applies to health practitioners and clinical assistants.\"",
     "CE"),
 (145, "That letter states in relation to Item 3(c): \"there have been no 'consequential' changes to operating procedures over the period requested.\"",
     "CE"),
 (146, "That letter states in relation to Item 3(a): \"All employee complaints relating to Logan Hospital Switchboard operational errors are made directly to the Line Manager of Switch Board and managed solely via email or verbally with the complainant.\"",
     "CE"),
 (147, "That letter states in relation to Items 1 and 2: \"a spreadsheet of recorded MET calls is available for the period 17-18 March 2024.\"",
     "CE"),
 ("K", "MATTERS NOT DONE, AND MATTERS NOT AVAILABLE"),
 (148, "The Respondent does not allege that any fatigue risk assessment was conducted in respect of the Appellant's position at any time before 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (149, "The Respondent does not allege that any fatigue risk management training was provided to the Appellant in respect of his position at any time before 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (150, "The Respondent does not allege that fatigue risk management assessment was implemented at Logan Hospital Switchboard at any time before 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (151, "The Respondent does not allege that any change was made to the operating procedures of Logan Hospital Switchboard as a consequence of any employee complaint over the period 1 December 2023 to 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (152, "The Respondent has not disclosed any document recording consultation with Switchboard operators before the change communicated by the email of 15 April 2024.",
     "Respondent's amended List of Documents dated 14 August 2026"),
 ("L", "STRESSOR 3(d) - THE RESPONDENT'S OWN REVIEW DECISION OF 24 OCTOBER 2024"),
 (153, "Review Decision 69983 dated 24 October 2024 records that in its response the employer included an extract of the Hospital and Health Services General Employees (Queensland Health) Award which \"stated that employees must be provided with a break of not less than 10 hours between the termination of one shift and the commencement of another shift, and 8 hours applied instead of 10 only in specific circumstances\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (154, "That decision states: \"The break between the shift on 17 March 2024 and 18 March 2024 equated to 7 hours.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (155, "That decision states: \"Even if you were allowed to leave early on 17 March 2024 as suggested by the employer, you left a maximum of 30 minutes early, which meant you still did not receive a minimum 8-hour break.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (156, "That decision states: \"Based on this, I find the rostering of these two shifts amounted to unreasonable management action given that it was in direct contradiction to the award and the 8-hour agreement.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (157, "That decision states, under the heading \"Conclusion\": \"you sustained a personal injury of a psychological nature\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (158, "That decision states, under the heading \"Conclusion\": \"your injury arose out of employment, to the extent that it arose out of factors 2, 3 and 4, where employment was a significant contributing factor\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 ("M", "THE APPELLANT'S CONTEMPORANEOUS ACCOUNT, AND THE DOCUMENTS THE RESPONDENT LISTS"),
 (159, "The Respondent's amended List of Documents dated 14 August 2026 lists at item 12 an email from the Appellant to WorkCover Queensland dated 12 July 2024 with the attachment described as \"Event overview - undated\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (160, "That amended List of Documents lists at item 14 an email from the Appellant to WorkCover Queensland dated 18 July 2024 with the attachment described as \"Witness statement - Carolyn Jeffrey\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (161, "That amended List of Documents lists at item 16 an email from Ms Carolyn Jeffrey to WorkCover Queensland dated 1 August 2024 described as a follow up statement.",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (162, "That amended List of Documents lists at item 25 an email from the Appellant to WorkCover Queensland dated 29 August 2024 described as regarding the after hours on call change, with the attachment described as \"Email: After hours on call process\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (163, "That amended List of Documents lists at item 26 an email from the Appellant to WorkCover Queensland dated 30 August 2024 described as regarding failure to consult, with the attachment described as \"Email: Task change switchboard - 19/04/2024\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (164, "That amended List of Documents lists at item 27 an email from the Appellant to WorkCover Queensland dated 30 August 2024 described as regarding failure to consult, with the attachment described as \"Email: MASPER process - 09/05/2024\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (165, "The Appellant provided the document described at item 12 to WorkCover Queensland on 12 July 2024.",
     "As above; and the Appellant's email of that date"),
 (166, "On 11 August 2026 the Appellant served on the Respondent a bundle titled \"Stressor 1(a) - Particulars support bundle\", comprising 30 pages and six tabs, each stating a particular of Stressor 1(a) of the Amended Form 9A and enclosing the documents recording it.",
     "The bundle, and the Appellant's covering email of 11 August 2026"),
 ("N", "MATTERS THE RESPONDENT DOES NOT ALLEGE"),
 (167, "The Respondent does not allege that the Appellant was subject to any disciplinary process at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (168, "The Respondent does not allege that the Appellant's work performance was the subject of any formal performance management process at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (169, "The Respondent does not allege that the Appellant was the subject of any warning, whether written or oral, at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (170, "The Respondent's amended statement of facts and contentions does not identify the management action referred to in paragraph 27.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
]

FORMH = ParagraphStyle('FORMH', parent=BODY, fontName='Helvetica-Bold', fontSize=15, leading=18)
FLD = ParagraphStyle('FLD', parent=BODY, fontName='Helvetica-Bold', fontSize=9, leading=12)
VAL = ParagraphStyle('VAL', parent=BODY, fontSize=10, leading=13)

def fieldrow(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.6, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f4f4f4')),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    return t

s = []
# ---------- FORM 24 COVER (mirrors the approved form; transcribe onto the official form) ----------
s.append(P("<b>INDUSTRIAL COURT OF QUEENSLAND<br/>QUEENSLAND INDUSTRIAL RELATIONS COMMISSION</b>",
           ParagraphStyle('HD', parent=BODY, fontSize=9.5, leading=12.5,
                          textColor=colors.HexColor('#7a4a10'))))
s.append(fieldrow([[P("Matter Number:", FLD), P("<b>WC / 2024 / 227</b>", VAL)]], [34*mm, 60*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Form 24 - Notice to admit facts", FORMH))
s.append(P("<i>Industrial Relations Act 2016</i>, section 989<br/>"
           "<i>Industrial Relations (Tribunals) Rules 2011</i>, rules 41, 49, 108 and 113", SMALL))
s.append(Spacer(1, 5*mm))
s.append(fieldrow([[P("Applicant/Appellant:", FLD), P("Cory Lea Shepherd", VAL)]], [40*mm, 120*mm]))
s.append(P("v", CEN))
s.append(fieldrow([[P("Respondent:", FLD), P("Workers' Compensation Regulator", VAL)]], [40*mm, 120*mm]))
s.append(Spacer(1, 3*mm))
s.append(fieldrow([[P("To:", FLD), P("The Workers' Compensation Regulator<br/>"
                                     "Attention: Ms Renee Matheson, Senior Appeals Officer", VAL)]],
                  [40*mm, 120*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Take notice that the <b>appellant</b> in this proceeding proposes to prove the facts "
           "specified below, and if you do not within <b>14 days</b> serve a notice on the appellant "
           "disputing the facts, you are taken to admit, for this proceeding only, the facts "
           "specified in this notice.", BODY))
s.append(P("<b>NOTE - TRANSCRIBE ONTO THE OFFICIAL FORM.</b> This page reproduces the layout of the "
           "approved Form 24 so the schedule can be settled and checked. Download the current "
           "Form 24 from the Commission's website and transcribe the schedule into it before "
           "service. Sign, print your name, state the office held (\"Appellant\") and date it.", WARN))
s.append(PageBreak())
s.append(P("SCHEDULE OF FACTS - SECOND NOTICE TO ADMIT FACTS", H1))
s.append(P("<i>Industrial Relations (Tribunals) Rules 2011, rule 49</i>", CEN))
s.append(P("WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation "
           "Regulator (Respondent)", CEN))
s.append(P("<b>DRAFT - 20 August 2026.</b> Schedule of facts for insertion in the approved Form 24. "
           "<b>Verify each quotation against the source before service.</b> The Source column is "
           "for the Appellant's own verification and is DELETED BEFORE SERVICE. Sections are "
           "headings only and are not numbered items.", WARN))
s.append(P("TAKE NOTICE that the Appellant proposes to prove the facts specified below, and that if "
           "the Respondent does not, within 14 days after receiving this notice, serve a notice on "
           "the Appellant disputing those facts, the Respondent is taken to admit them for this "
           "proceeding only.", BODY))

rows = [[P("<b>No.</b>", SMALL), P("<b>Fact to be admitted</b>", SMALL),
         P("<b>Admit / Deny</b>", SMALL), P("<b>Source (delete before service)</b>", SMALL)]]
for f in FACTS:
    if isinstance(f[0], str):
        rows.append([P(f"<b>{f[0]}</b>", SMALL), P(f"<b>{f[1]}</b>", SMALL), P("", SMALL), P("", SMALL)])
    else:
        rows.append([P(f"<b>{f[0]}</b>", SMALL), P(f[1], SMALL), P("", SMALL), P(f[2], SMALL)])
t = Table(rows, colWidths=[9*mm, 99*mm, 19*mm, 39*mm], repeatRows=1)
st = [('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
      ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')),
      ('VALIGN', (0,0), (-1,-1), 'TOP'),
      ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
      ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 3.5)]
for i, f in enumerate(FACTS, start=1):
    if isinstance(f[0], str):
        st.append(('BACKGROUND', (0,i), (-1,i), colors.HexColor('#f0f0f0')))
        st.append(('SPAN', (1,i), (3,i)))
t.setStyle(TableStyle(st))
s.append(t)
s.append(Spacer(1, 5*mm))
s.append(P("Cory Lea Shepherd<br/>Appellant (self-represented) &nbsp;|&nbsp; [date]", BODY))

# ---------------- SCHEDULE B - DOCUMENTS (r 49 "or documents" / authenticity limb) ----------------
s.append(PageBreak())
s.append(P("SCHEDULE B - DOCUMENTS", H1))
s.append(P("Authenticity to be admitted &nbsp;|&nbsp; <i>Industrial Relations (Tribunals) Rules "
           "2011, rule 49</i>", CEN))
s.append(P("<b>WHY THIS SCHEDULE EXISTS - internal note, delete before service.</b> Rule 49(1) "
           "permits a party to ask another party to admit \"the facts <b>or documents</b> stated in "
           "the notice\", and rule 49(2) deems admission if the other party does not within 14 days "
           "serve a notice disputing \"the facts or <b>the authenticity of the documents</b>\". "
           "Admitted authenticity means each document below can be tendered at the hearing without "
           "being formally proved. For a self-represented appellant that removes a whole category "
           "of work and a whole category of objection.", WARN))
s.append(P("TAKE NOTICE that the Appellant also asks the Respondent to admit, for this proceeding "
           "only, the authenticity of the documents specified below, and that if the Respondent "
           "does not within 14 days after receiving this notice serve a notice on the Appellant "
           "disputing the authenticity of those documents, the Respondent is taken to admit their "
           "authenticity for this proceeding only.", BODY))


_n = 0
_new = []
for _f in FACTS:
    if isinstance(_f[0], str):
        _new.append(_f)
    else:
        _n += 1
        _new.append((_n,) + tuple(_f[1:]))
FACTS = _new
del _n, _new

DOCS = [
 ("Email, the Appellant to Ms C Taylor, Ms T Reese, Ms P Conaghan and Ms T Smith, \"Increase of "
  "hours and Workplace issues\"", "7 August 2023, 12:21 pm"),
 ("Email, Ms C Taylor to the Appellant, reply in the same chain", "7 August 2023, 1:43 pm"),
 ("Email, Ms T Reese to the Appellant, reply in the same chain", "7 August 2023, 3:13 pm"),
 ("Email, Ms T Reese to Ms C Taylor, with attachment \"Rostered shifts Cory S. past 8 "
  "months.xlsx\"", "7 August 2023, 5:11 pm"),
 ("Email, Ms T Reese to the Appellant, attaching HR Policy E12 - Individual Employee Grievances",
  "29 August 2023"),
 ("Document, the Appellant to Ms C Taylor, \"Request to Increase Working Hours to Full Time "
  "Rotational Roster\"", "31 August 2023"),
 ("Email, the Appellant to Ms T Reese, with attached draft roster", "4 September 2023"),
 ("Email, Ms T Reese to the Appellant", "8 September 2023, 11:42 am"),
 ("Email, Ms C Taylor to the Appellant, \"Approved - Permanent Full Time FTE\"",
  "27 September 2023, 1:52 pm"),
 ("Email, Ms C Taylor to Logan Switch and Switchboard staff, \"Afterhours Oncall Process - "
  "Switchboard\"", "15 April 2024, 12:39 pm"),
 ("Email, Ms T Reese to the Appellant, \"Roster Concerns\"", "26 April 2024, 1:52 pm"),
 ("Email, the Appellant to Ms T Reese, \"Re: Roster Concerns\"", "1 May 2024, 1:18 pm"),
 ("Email, Ms T Reese to the Appellant, \"RE: Roster Concerns\"", "8 May 2024, 9:08 am"),
 ("Email, Ms T Reese to Mr M Pritchard, \"FW: Roster Concerns\", with attachment "
  "\"qh-gdl-401-3.3\"", "10 May 2024, 2:08 pm"),
 ("Email, Ms C Taylor to the Appellant, \"Sick leave 14.05.24\"", "14 May 2024, 12:08 pm"),
 ("Email, Ms S Marriott to Logan Switch, \"Respiratory Nurse Educators\"", "15 May 2024, 11:47 am"),
 ("Email, Ms C Taylor to Logan Switch and Switchboard staff, \"Switchboard Manager - On call and "
  "Hours.\"", "17 May 2024, 9:30 am"),
 ("Email, Ms C Taylor to Ms A McNamee, \"FW: Office Hours and Departmental Directives\"",
  "17 May 2024, 1:20 pm"),
 ("Email, Ms S Marriott to Logan Switch, \"FW: Respiratory Nurse Educators\"",
  "20 May 2024, 11:03 am"),
 ("Email, the Appellant (Logan Switch) to Ms C Taylor, \"FW: Respiratory Nurse Educators\"",
  "20 May 2024, 2:05 pm"),
 ("Email, Ms C Taylor to the Appellant, \"RE: Respiratory Nurse Educators\"",
  "20 May 2024, 4:30 pm"),
 ("Email, Ms T Reese to LBH_HR, \"FW: Roster Concerns\"", "20 May 2024, 4:07 pm"),
 ("Letter, Metro South Hospital and Health Service to Commissioner Dwyer, reference K-LM26/729, "
  "signed by Ms N Cridland, Chief Executive", "5 June 2026"),
 ("Document, QH Leave Takings Report for the Appellant, produced by Metro South Health as item 15 "
  "of the Notice of non-party disclosure", "19 March 2024"),
 ("Email, Ms L Forrest, Senior Consultant Human Resources, Logan and Beaudesert Health Service, "
  "to the Appellant", "7 July 2026"),
 ("Review Decision 69983, Workers' Compensation Regulator", "24 October 2024"),
 ("Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital",
  "undated"),
 ("Email thread, \"Corey Shepherd 388372 Pay issues\" - PayrollMetroSouth to Ms C Taylor copied "
  "to the Appellant; the Appellant to Payroll; Payroll to the Appellant; Ms C Taylor to the "
  "Appellant", "3 to 21 May 2024"),
 ("Email, Ms C Taylor to the Appellant copied to Ms T Reese, \"Validation of Claims older than 3 "
  "months - Please sign\"", "28 May 2024, 8:36 am"),
 ("myHR submissions report for the Appellant, produced by Metro South Health as Item 11",
  "1 February to 31 May 2024"),
 ("Movement forms recording approved changes to working hours, approved by Mr S Hughes as "
  "delegate", "27 February, 17 April and 9 June 2026"),
 ("Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South "
  "Health", "November 2024"),
 ("Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, Metro South "
  "Health", "December 2024"),
 ("Email, Mr H Moran, Organiser, Together Queensland, to Ms C Jeffrey, Ms P Conaghan and the "
  "Appellant, \"Switchboard Roster Feedback - For Delegates\"", "3 November 2025, 10:57 am"),
 ("Email chain, \"Office Hours and Departmental Directives\" - the Appellant to Ms C Taylor and "
  "Logan Switch copied to Switchboard staff, Ms T Reese and LBH_HR; the reply of Ms Reese; the "
  "reply of the Appellant", "15 May 2024"),
 ("Email, Ms T Reese to the Appellant, \"RE: Office Hours and Departmental Directives\"",
  "21 May 2024, 2:53 pm"),
 ("Email, Ms C Taylor to Ms A McNamee, \"FW: Office Hours and Departmental Directives\"",
  "17 May 2024, 1:20 pm"),
 ("Document, Fatigue risk management systems - Implementation guideline QH-GDL-401-3.3:2021, "
  "being the attachment to the email of Ms T Reese of 10 May 2024", "2021"),
 ("MASPER register email records - Ms Taylor to Dr Kwok and Dr Wong, \"RE: Switchboard issues "
  "5 May, 7 May, and 8 May\"; Ms Taylor to Logan Switch and Switchboard staff, \"MASPER process\"; "
  "and the underlying switchboard issue logs of 2 to 8 May 2024",
  "9 May 2024 (issues logged 2-8 May 2024)"),
 ("Email, Ms E Stibbard to the Appellant and the Switchboard team, \"Hello & Update\"",
  "18 July 2023, 12:56 pm"),
]
drows = [[P("<b>No.</b>", SMALL), P("<b>Document</b>", SMALL), P("<b>Date</b>", SMALL),
          P("<b>Authenticity admitted / disputed</b>", SMALL)]]
for i, (d, dt) in enumerate(DOCS, start=1):
    drows.append([P(f"<b>{i}</b>", SMALL), P(d, SMALL), P(dt, SMALL), P("", SMALL)])
dt_ = Table(drows, colWidths=[9*mm, 92*mm, 30*mm, 35*mm], repeatRows=1)
dt_.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 3.5)]))
s.append(dt_)
s.append(Spacer(1, 4*mm))
s.append(P("Cory Lea Shepherd<br/>Appellant (self-represented) &nbsp;|&nbsp; [date]", BODY))

# ---------------- COVERING LETTER ----------------
s.append(PageBreak())
s.append(P("Covering email - to accompany service", H1))
s.append(P("<b>To:</b> Renee.Matheson@oir.qld.gov.au &nbsp;<b>Cc:</b> the OIR appeals registry<br/>"
           "<b>Subject:</b> WC/2024/227 - Shepherd - notice to admit facts and documents", SMALL))
s.append(Spacer(1, 3*mm))
for t in ["Dear Ms Matheson,",
          "I attach a notice to admit facts and documents under rule 49 of the <i>Industrial "
          "Relations (Tribunals) Rules 2011</i>.",
          "Schedule A sets out facts. Schedule B sets out documents, and asks that their "
          "authenticity be admitted. The documents are those already exchanged between the parties "
          "or listed in the Respondent's amended List of Documents dated 14 August 2026.",
          "Copies of the following are enclosed, as they may not be in the Respondent's possession: the "
          "email of Ms L Forrest dated 7 July 2026; the QH Leave Takings Report for 19 March 2024; "
          "the myHR submissions report for 1 February to 31 May 2024; "
          "and the Stressor 1(a) particulars bundle served on 11 August 2026. I am content to "
          "provide a copy of any other document listed.",
          "Kind regards,<br/>Cory Lea Shepherd<br/>Appellant (self-represented), WC/2024/227"]:
    s.append(P(t, ITEM))
s.append(P("<b>NOTHING FURTHER.</b> No argument, no explanation of why the notice is being served, "
           "no reference to the Further Directions Order, the withdrawn application, the report or "
           "settlement. A notice to admit speaks for itself and any covering commentary only gives "
           "something to respond to. The offer to provide copies is included because it removes the "
           "\"does not have a copy\" answer in advance.", WARN))

doc = SimpleDocTemplate("out/FORM24_SECOND_NOTICE_DRAFT.pdf", pagesize=A4,
                        leftMargin=14*mm, rightMargin=14*mm, topMargin=13*mm, bottomMargin=13*mm)
def f_(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(14*mm, 8*mm, "DRAFT - SECOND NOTICE TO ADMIT FACTS - VERIFY EVERY QUOTATION BEFORE SERVICE")
    c.setFont('Helvetica', 7); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-14*mm, 8*mm, f"Page {d.page}")
    c.restoreState()
doc.build(s, onFirstPage=f_, onLaterPages=f_)

pdf = pikepdf.open("out/FORM24_SECOND_NOTICE_DRAFT.pdf", allow_overwriting_input=True)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save("out/_t.pdf"); pdf.close(); os.replace("out/_t.pdf", "out/FORM24_SECOND_NOTICE_DRAFT.pdf")
nf = len([f for f in FACTS if not isinstance(f[0], str)])
print(f"built out/FORM24_SECOND_NOTICE_DRAFT.pdf - {nf} facts + {len(DOCS)} documents")
