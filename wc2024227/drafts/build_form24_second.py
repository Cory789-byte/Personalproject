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
 (1, "Metro South Hospital and Health Service produced a role description for the position of Administration Officer, Switchboard Services, classification AO3, Logan Hospital.",
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
 (11, "That role description states, as a key responsibility: \"Ability to work effectively as an individual with limited supervision to meet deadlines and establish work priorities\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (12, "That role description states, as a key responsibility: \"Follow defined service quality standards, occupational health and safety policies and procedures relating to the work being undertaken to ensure high quality, safe services and workplaces\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (13, "That role description states, under mandatory requirements: \"The position is a continuous shift working role. You must be able to work a roster which covers multiple shifts over a 24/7 period\".",
     "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital - produced by Metro South Hospital and Health Service"),
 (14, "The Appellant has been employed by Metro South Hospital and Health Service since 2019.",
     "Appellant's amended statement of facts and contentions"),
 ("B", "THE HOURS THE APPELLANT SOUGHT, AND OBTAINED"),
 (15, "On 7 August 2023 at 12:21 pm the Appellant sent an email to Ms Chloe Taylor, Ms Tammy Reese, Ms Patricia Conaghan and Ms Tracey Smith, marked of High importance, which states: \"Furthermore, to meet the demands and the additional hours of the department both Patricia Conaghan and I would like to formally adhoc an additional 2 shifts per fortnight.\"",
     "R_REESE"),
 (16, "That email sets out clause 11.7 of the applicable agreement, headed \"Additional Permanent Hours for Part-time Employees\".",
     "R_REESE"),
 (17, "On 8 August 2023 at 6:06 pm the Appellant sent an email to Ms Reese which states: \"I can confirm that I will be in tomorrow 0700-1500 9th August. I was also looking to pick up another shift if possible.\"",
     "R_REESE"),
 (18, "On 8 August 2023 at 4:15 pm Ms Reese sent an email to the Appellant which states: \"can I ask were you looking for another shift on top of those 8 to replace the shift missed today also?\"",
     "R_REESE"),
 (19, "On 31 August 2023 the Appellant provided to Ms Taylor a written application headed \"Request to Increase Working Hours to Full Time Rotational Roster\".",
     "R_REESE"),
 (20, "That application states: \"I have also expressed my willingness to take on additional night shifts as part of the roster.\"",
     "R_REESE"),
 (21, "On 4 September 2023 the Appellant sent an email to Ms Reese which states: \"I confirm that I am able and willing to work any roster that is presented to me, including the current schedule with full 24-hour availability.\"",
     "R_REESE"),
 (22, "That email states: \"I have no issues with shift work.\"",
     "R_REESE"),
 (23, "That email attached a draft roster spreadsheet prepared by the Appellant.",
     "R_REESE"),
 (24, "On 8 September 2023 at 11:42 am Ms Reese sent an email to the Appellant which states: \"I am glad to hear things seem to be going well with Chloe and I am also glad to hear you applied for the additional shifts through the recent EOI.\"",
     "R_REESE"),
 (25, "On 27 September 2023 at 1:52 pm Ms Taylor sent an email to the Appellant with the subject \"Approved - Permanent Full Time FTE\" which states: \"Just giving you an update on your application for Permanent Fulltime hours, I am very pleased to advise you that this has been approved.\"",
     "Email of Ms C Taylor, 27 September 2023"),
 (26, "That email states: \"happy to commence Full-time hours from the 16th October 2023\".",
     "As above"),
 ("C", "STRESSOR 1(a) - THE DATABASE, AND THE DIRECTIVES ISSUED WITHOUT CONSULTATION"),
 (27, "Review Decision 69983 records: \"Ms Ellen Stibbard, Switchboard Telecommunications Coordinator, emailed the staff members on 18 July 2023 to provide an update with respect to her role.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (28, "That decision records: \"She explained her role was a project role, which was a temporary position that focused on fixing the database used by the switchboard.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (29, "That decision records: \"She informed that while she fixed it, she would be removing everyone's access to it, and asked for anyone who needed to amend, add or remove entries, to directly contact her or Ms Taylor.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (30, "That decision records: \"On 19 April 2024, Ms Taylor emailed the team and expressed that due to errors being made with respect to data entry, a new process was to be followed which included more checks to ensure accuracy of data entry.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (31, "The Respondent does not allege that the role description for the position of Administration Officer, Switchboard Services was amended at any time after 18 July 2023.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (32, "The Respondent does not allege that access to the database used by the Switchboard was restored to the Appellant at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (33, "On 15 April 2024 at 12:39 pm Ms Taylor sent an email to Logan Switch, copied to Ms Reese and to Switchboard staff including the Appellant, with the subject \"Afterhours Oncall Process - Switchboard\".",
     "Respondent's amended List of Documents, item 25 (email of 29 August 2024, attachment \"Email: After hours on call process\")"),
 (34, "That email states: \"Process during office hours remains the same, please contact myself through switch/office or mobile unless otherwise advised.\"",
     "As above"),
 (35, "That email states: \"This new process is effective from today.\"",
     "As above"),
 (36, "That email states: \"You will see that Ellen and myself have added Afterhours on call, the days that are highlighted in purple show who is on call after hours.\"",
     "As above"),
 (37, "Ms Taylor signed that email as \"A/Switchboard Manager\".",
     "As above"),
 (38, "Ms Taylor's email to all Switchboard staff of 17 May 2024 at 9:30 am states: \"My office hours can vary due to having to take my girls to school in the morning, on the days that I do have school drop off I always let switch know that I will be in later between 0800-830am. Otherwise my hours are from 06:30-14:30.\"",
     R_TAYLOR),
 (39, "That email states: \"Moving forward so communication is clear for the team, I will be sending an email to switch to advise of any change to my office hours for the week.\"",
     R_TAYLOR),
 (40, "On 17 May 2024 at 1:20 pm Ms Taylor sent an email to Ms Adriana McNamee with the subject \"FW: Office Hours and Departmental Directives\", which states: \"when staff call in for any leave to please contact me either via switch, office or my mobile.\"",
     R_TAYLOR),
 ("D", "STRESSOR 1(a) - THE DELAY IN COMMUNICATION AND THE MATTERS RAISED IN MAY 2024"),
 (41, "On 15 May 2024 at 11:47 am Ms Sue Marriott, Administration Officer, Integrated Respiratory Service, sent an email to Logan Switch, marked of High importance, which states: \"Could you please amend your number registry/directory to show #8768 belongs to the Integrated Respiratory Service... We are not Respiratory Medical OPD and we do not have any doctors working out of this area.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (42, "On 20 May 2024 at 11:03 am Ms Marriott sent a further email to Logan Switch, marked of High importance, which states: \"Just a courtesy reminder, we continue to get calls put through to us for Respiratory Medical Outpatients... we can not help patients or other clinical staff with OPD issues.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (43, "The email of Ms Marriott of 20 May 2024 at 11:03 am was sent five days after her email of 15 May 2024 at 11:47 am.",
     "Respondent's disclosure - the Integrated Respiratory Service email chain, 15-20 May 2024"),
 (44, "The Appellant's rostered shift on 20 May 2024 concluded at 2:00 pm.",
     "Switchboard services roster for the fortnight commencing 13 May 2024"),
 (45, "On 20 May 2024 at 2:05 pm the Appellant sent an email to Ms Taylor, marked of High importance, which states: \"switchboard staff may not be aware of the clinics due to modifications to the Document: Outpatients Department - Clinic contact Details. on the 22nd of February 2024. I recommend a modification and review of the document.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (46, "That email of the Appellant was sent five minutes after the conclusion of his rostered shift on that day.",
     "Respondent's disclosure - the Integrated Respiratory Service email chain, 15-20 May 2024"),
 (47, "That email of the Appellant was sent from the Logan Switch account.",
     "Respondent's disclosure - the Integrated Respiratory Service email chain, 15-20 May 2024"),
 (48, "On 20 May 2024 at 4:30 pm Ms Taylor replied to the Appellant, stating: \"Thank you for bringing this to my attention however this task was being actioned. I had discussed with Richard this morning about the update of outpatients respiratory/medical.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (49, "That reply of Ms Taylor states: \"Taking note of your recommendation, we can also put the updated procedures out to the team for consultation before implementing.\"",
     "Stressor 1(a) particulars bundle served on the Respondent 11 August 2026, Tab 4; and the Respondent's own disclosure"),
 (50, "Mr Richard Parry was at that time a member of the Switchboard staff at Logan Hospital.",
     "Email of the Appellant of 15 May 2024 at 1:15 pm, Respondent's disclosure of 11 June 2026"),
 (51, "The Respondent has not disclosed any document recording a communication sent by Ms Taylor to Ms Marriott, or to the Integrated Respiratory Service, on 20 May 2024.",
     "The Respondent's disclosure in this proceeding"),
 (52, "The Respondent has not disclosed any document recording a communication sent by Mr Parry to Ms Marriott, or to the Integrated Respiratory Service, on 20 May 2024.",
     "The Respondent's disclosure in this proceeding"),
 (53, "The Respondent does not allege that any response was made to the email of Ms Marriott of 20 May 2024 at 11:03 am before 2:05 pm on that day.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (54, "The Respondent does not allege that any response was made to the email of Ms Marriott of 15 May 2024 at 11:47 am at any time before 20 May 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (55, "On 17 May 2024 at 9:30 am Ms Taylor sent an email to Logan Switch and Switchboard staff, copied to Ms Reese, which states: \"regardless of my start/finish times next week you are to please contact me through the day/afterhours either via switch, office or mobile.\"",
     R_TAYLOR),
 ("E", "STRESSOR 1(c) - THE MATTERS RAISED IN AUGUST AND SEPTEMBER 2023, AND THE RESPONSE"),
 (56, "The Appellant's email of 7 August 2023 at 12:21 pm states: \"Please give me some space and stop with any further communication as I have had enough of it.\"",
     "R_REESE"),
 (57, "On 7 August 2023 at 1:43 pm Ms Taylor replied to the Appellant, copied to Ms Reese and Ms Smith, stating: \"My sincere apologises about your rostered Monday 7th 0700-1500 shift, I can confirm this was an oversight.\"",
     "R_REESE"),
 (58, "That email of Ms Taylor states: \"Would you like me to roster you off tomorrow Tuesday 8th 0700-1500 to give you the required rest period\".",
     "R_REESE"),
 (59, "On 7 August 2023 at 3:13 pm Ms Reese replied to the Appellant stating: \"As Chloe is your current line manager and as such you are required to continue to communicate with Chloe for work related issues, shift concerns, leave, etc.\"",
     "R_REESE"),
 (60, "On 7 August 2023 at 5:11 pm Ms Reese sent an email to Ms Taylor attaching a document titled \"Rostered shifts Cory S. past 8 months.xlsx\", which states: \"can I ask if you can send me an email of your recent communication with Cory about contacting yourself about missed shifts, as I could not find a copy of this email.\"",
     "R_REESE"),
 (61, "On 29 August 2023 at 6:57 pm Ms Reese sent the Appellant an email attaching HR Policy E12 - Individual Employee Grievances, and setting out how a grievance could be submitted.",
     "R_REESE"),
 (62, "On 4 September 2023 the Appellant replied to Ms Reese stating: \"I have also spoken to Chloe. We are seemingly on the path to working in a beneficial way and hopefully will not need to go through this process.\"",
     "R_REESE"),
 (63, "The Appellant did not submit a grievance under HR Policy E12 in 2023.",
     "R_REESE"),
 ("F", "THE PROCESS FOR NOTIFYING UNAVAILABILITY FOR A ROSTERED SHIFT"),
 (64, "On 14 May 2024 at 12:08 pm Ms Taylor sent an email to the Appellant, copied to Ms Reese, with the subject \"Sick leave 14.05.24\", which states: \"in business hours you are to follow the correct process and speak to me directly if its regarding emergent leave, you can contact me either through switch or my office/mobile.\"",
     R_TAYLOR),
 (65, "On 13, 14 and 15 May 2024 the Appellant notified his unavailability for his rostered shift by telephoning the Switchboard.",
     "Ms Taylor's email to Ms McNamee, 17 May 2024, which records each of those three calls"),
 (66, "The document entitled \"Logan Hospital Switchboard Sick Leave Process\", version 1.1, is dated 4 February 2025.",
     "Attachment to the letter of Mr Scott Hughes dated 8 September 2025, page 1"),
 (67, "The Respondent does not allege that any written procedure governing the notification of unavailability for a rostered shift at Logan Hospital Switchboard existed before 4 February 2025.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 ("G", "STRESSOR 2 - THE PAY CORRECTION, AND THE THREAD \"COREY SHEPHERD 388372 PAY ISSUES\""),
 (68, "The Respondent's disclosure contains an email thread with the subject \"Corey Shepherd 388372 Pay issues\".",
     "R_PAY"),
 (69, "The first message in that thread is dated 3 May 2024, is from PayrollMetroSouth, is addressed to Ms C Taylor, and is copied to the Appellant.",
     "R_PAY"),
 (70, "That message is signed \"Elaine Grant, Client Service Officer, Metro South Payroll Team, Payroll Transactional Services, Corporate Enterprise Solutions, Corporate Services, Queensland Health\".",
     "R_PAY"),
 (71, "That message states: \"Corey has wages top up on fortnight 05.02.24 for 0.95mins as he is under his contracted hours so it is toping up the missing wages from his RDO balance.\"",
     "R_PAY"),
 (72, "That message states: \"This will be due to having a 7hr shift on 09.02.24 instead of an 8hr shift. AVAC PRN 15397775.\"",
     "R_PAY"),
 (73, "That message states: \"The same has happened for the next fortnight 19.02.24 due to 28.02.24 shift AVAC PRN 15605601 has this shift as 7hrs topping up 0.95 for missing hour.\"",
     "R_PAY"),
 (74, "That message states: \"Fortnight 18.03.24 is the opposite and has too many ordinary shifts for the fortnight resulting in wage reduction of 7.55hrs as one of the shifts needs to be overtime.\"",
     "R_PAY"),
 (75, "That message states: \"Fortnight 01.04.24 is the same, 0.95hrs over contracted 76hrs needs to be overtime.\"",
     "R_PAY"),
 (76, "That message states: \"Please submit an AVAC to correct these shifts for each fortnight so Cory is paid corrected and his RDO balance will then be amended.\"",
     "R_PAY"),
 (77, "The thread contains a message dated 10 May 2024 at 2:21 pm from the Appellant, addressed to PayrollMetroSouth and to Ms E Grant.",
     "R_PAY"),
 (78, "The thread contains a message dated 13 May 2024 at 8:21 am from PayrollMetroSouth, addressed to the Appellant.",
     "R_PAY"),
 (79, "That message of 13 May 2024 states: \"I cannot see that any of the issues below have been corrected. Please speak to your Line Manager to have them corrected with an AVAC submitted through My HR as this will also be affecting your RDO balances as well as your pay.\"",
     "R_PAY"),
 (80, "The thread contains a message dated 21 May 2024 at 12:33 pm from Ms C Taylor, addressed to the Appellant, with the subject \"RE: Corey Shepherd 388372 Pay issues\".",
     R_TAYLOR),
 (81, "That message of 21 May 2024 states: \"Just letting you know that I am still I am waiting payroll confirmation about a few of these payroll issues and as soon as I do get that confirmation, I will submit an AVAC for next pay run. I will let you know PRN once it has been submitted.\"",
     R_TAYLOR),
 (82, "The Respondent's disclosure contains a message dated 28 May 2024 at 8:36 am from Ms C Taylor, addressed to the Appellant and copied to Ms T Reese, with the subject \"Validation of Claims older than 3 months - Please sign\".",
     R_TAYLOR),
 (83, "That message of 28 May 2024 states: \"Please find attached Validation of claims older than 3 months, please sign and return to be as soon as possible so I can escalate for delegate approval.\"",
     R_TAYLOR),
 (84, "The myHR submissions report produced as Item 11 records seven submissions for the Appellant in the period 1 February 2024 to 31 May 2024.",
     "HR11"),
 (85, "That report records five of those seven submissions as an \"Attendance Variation and Allowance Claim (AVAC)\".",
     "HR11"),
 (86, "That report records the initiator of each of those five Attendance Variation and Allowance Claims as \"Donovan-Taylor, Chloe\".",
     "HR11"),
 (87, "That report records the initiator of no Attendance Variation and Allowance Claim in that period as the Appellant.",
     "HR11"),
 (88, "That report records a submission with process number 16328886 as an Attendance Variation and Allowance Claim submitted on 15 May 2024, with a processing date of 16 May 2024, and a status of \"Completed\".",
     "HR11"),
 (89, "That report records a submission with process number 16450619 as an Attendance Variation and Allowance Claim submitted on 28 May 2024, with an effective date of 30 March 2024, a processing date of 30 May 2024, and a status of \"Part Completed\".",
     "HR11"),
 (90, "That report records the status of every other Attendance Variation and Allowance Claim in the period as \"Completed\".",
     "HR11"),
 (91, "That report records the following process numbers with the following submission dates: 15325947, submitted 6 February 2024; 15480560, submitted 20 February 2024; 15848692, submitted 27 March 2024; 15849573, submitted 27 March 2024; 15969838, submitted 9 April 2024; 16328886, submitted 15 May 2024; and 16450619, submitted 28 May 2024.",
     "HR11"),
 (92, "In that report, process numbers increase as submission dates increase.",
     "HR11"),
 (93, "The number 15397775 falls between 15325947 and 15480560.",
     "Arithmetic"),
 (94, "The number 15605601 falls between 15480560 and 15848692.",
     "Arithmetic"),
 (95, "Neither AVAC PRN 15397775 nor AVAC PRN 15605601 appears in that report.",
     "HR11"),
 ("H", "STRESSOR 3 - THE ROSTER, AND THE EMPLOYER'S KNOWLEDGE OF FATIGUE BEFORE 18 JUNE 2024"),
 (96, "On 26 April 2024 at 1:52 pm Ms Reese sent an email to the Appellant with the subject \"Roster Concerns\", referring to a meeting on 16 April 2024 at which the Appellant raised a roster line ending with night shifts followed by three days off and then returning to night shifts.",
     "R_REESE"),
 (97, "That email states that Ms Taylor \"was working to fix this error and would get in touch with you about what alternative shifts she could offer\".",
     "R_REESE"),
 (98, "On 1 May 2024 at 1:18 pm the Appellant sent an email to Ms Reese with the subject \"Roster Concerns\" referring to section 4, clause 10.4.1 of the Operations Manual and stating: \"This section includes a toolkit required by management to manage fatigue and implement appropriate protocols and adhere to the workplace health and safety act.\"",
     "R_REESE"),
 (99, "That email states: \"I forwarded the toolkit to Chloe last week for review and action but have yet to receive feedback\".",
     "R_REESE"),
 (100, "On 8 May 2024 at 9:08 am Ms Reese replied to the Appellant stating: \"Thanks for raising these observations and concerns. I am following up with regards to these with HR for further advice and I will get back to you asap with a response.\"",
     "R_REESE"),
 (101, "On 10 May 2024 at 2:08 pm Ms Reese sent an email to Mr Mackenzie Pritchard of Human Resources forwarding the Appellant's email of 1 May 2024, which states: \"I think he is trying to raise that he has concerns over how his manager is rostering for the Switchboard team and how it is impacting on staff fatigue, or more specifically his fatigue.\"",
     "R_FRMS"),
 (102, "That email states: \"as per Cory's second extract detailing the Roster Risk assessment Matrix, Chloe and I have run thought this and we say at best there would be a rating of 11 which is moderate\".",
     "R_FRMS"),
 (103, "That email states: \"I acknowledge there has been a few rostering errors made by Chloe with regards to Cory's line in past rosters\".",
     "R_FRMS"),
 (104, "That email attached the document \"qh-gdl-401-3.3\", being the Queensland Health Fatigue Risk Management Systems Implementation Guideline.",
     "R_FRMS"),
 (105, "On 20 May 2024 at 4:07 pm Ms Reese sent an email to LBH_HR which states: \"I am just following up on this query I raised a little while ago in relation to a email I had received from a staff member about our rostering practices. Thus if someone might be able to give me a call regarding these staff concerns, that would be great.\"",
     "R_FRMS"),
 ("I", "STRESSOR 3 - THE BREAK OF 17-18 MARCH 2024, THE 2020 AGREEMENT, AND THE LEAVE OF 19 MARCH 2024"),
 (106, "By letter dated 7 July 2026 Ms Lyndelle Forrest, Senior Consultant, Human Resources, Logan and Beaudesert Health Service, wrote to the Appellant stating that the roster \"provides more than 10-hour breaks between shifts\".",
     "Letter of Ms L Forrest, Senior Consultant HR, 7 July 2026"),
 (107, "That letter states: \"acknowledge you also signed an 8 hour agreement on 17 June 2020, which allows you to work with only an 8 hour break, however this is only applied where staff initiated shift swaps have occurred.\"",
     "Letter of Ms L Forrest, Senior Consultant HR, 7 July 2026"),
 (108, "The Respondent does not allege that the consecutive shifts of 17 and 18 March 2024 arose from a staff initiated shift swap.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (109, "The Leave Takings Report produced by Metro South Hospital and Health Service in respect of 19 March 2024 records the Leave Category as \"Sick\", the Leave Type as \"Sick Leave\", the Time Code as \"SCK\", the Leave Taken as 7.60 hours, and the Leave Status as \"APPROVED\".",
     "Item 15 QH Leave Takings Report, produced by Metro South Health"),
 (110, "The Respondent's amended statement of facts and contentions dated 13 May 2026 states at paragraph 24(a): \"says that the appellant took leave on 19 March 2024 but says this was paid leave\".",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (111, "That amended statement of facts and contentions states at paragraph 24(b): \"says that pursuant to clause 18.10 of the Award, the appellant is not entitled to fatigue leave, because he was not performing overtime\".",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (112, "That amended statement of facts and contentions states at paragraph 27: \"The respondent contends that any management action involved in the causation of any injury to the Plaintiff was reasonable management action taken in a reasonable way pursuant to s 32(5) WCRA.\"",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (113, "No fatigue leave was available to the Appellant under clause 18.10 of the Award in respect of the consecutive shifts of 17 and 18 March 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026, paragraph 24(b)"),
 ("J", "THE EMPLOYER'S OWN STATEMENTS ABOUT ITS SYSTEMS AND RECORDS"),
 (114, "By letter dated 5 June 2026, reference K-LM26/729, signed by Ms Noelle Cridland as Chief Executive of Metro South Hospital and Health Service and addressed to Commissioner Dwyer, Metro South Health stated in relation to Item 4: \"the requested documents do not exist. Mandatory Fatigue Risk Management System training only applies to health practitioners and clinical assistants. The Logan Hospital Switchboard staff are non-clinical staff, and therefore there is no mandatory requirement for them to complete Fatigue Risk Management System training.\"",
     "CE"),
 (115, "That letter states in relation to Item 5: \"The implementation of fatigue risk management assessment at Switchboard Logan Hospital occurred after 30 June 2024 in connection with an organisational change related to the reporting lines for Switchboard.\"",
     "CE"),
 (116, "That letter states in relation to Item 7: \"the requested documents do not exist. Mandatory Fatigue Risk Management System training only applies to health practitioners and clinical assistants.\"",
     "CE"),
 (117, "That letter states in relation to Item 3(c): \"there have been no 'consequential' changes to operating procedures over the period requested.\"",
     "CE"),
 (118, "That letter states in relation to Item 3(a): \"All employee complaints relating to Logan Hospital Switchboard operational errors are made directly to the Line Manager of Switch Board and managed solely via email or verbally with the complainant.\"",
     "CE"),
 (119, "That letter states in relation to Items 1 and 2: \"a spreadsheet of recorded MET calls is available for the period 17-18 March 2024.\"",
     "CE"),
 ("K", "MATTERS NOT DONE, AND MATTERS NOT AVAILABLE"),
 (120, "The Respondent does not allege that any fatigue risk assessment was conducted in respect of the Appellant's position at any time before 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (121, "The Respondent does not allege that any fatigue risk management training was provided to the Appellant in respect of his position at any time before 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (122, "The Respondent does not allege that fatigue risk management assessment was implemented at Logan Hospital Switchboard at any time before 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (123, "The Respondent does not allege that any change was made to the operating procedures of Logan Hospital Switchboard as a consequence of any employee complaint over the period 1 December 2023 to 30 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (124, "The Respondent has not disclosed any document recording consultation with Switchboard operators before the change communicated by the email of 15 April 2024.",
     "Respondent's amended List of Documents dated 14 August 2026"),
 ("L", "STRESSOR 3(d) - THE RESPONDENT'S OWN REVIEW DECISION OF 24 OCTOBER 2024"),
 (125, "Review Decision 69983 dated 24 October 2024 records that in its response the employer included an extract of the Hospital and Health Services General Employees (Queensland Health) Award which \"stated that employees must be provided with a break of not less than 10 hours between the termination of one shift and the commencement of another shift, and 8 hours applied instead of 10 only in specific circumstances\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (126, "That decision states: \"The break between the shift on 17 March 2024 and 18 March 2024 equated to 7 hours.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (127, "That decision states: \"Even if you were allowed to leave early on 17 March 2024 as suggested by the employer, you left a maximum of 30 minutes early, which meant you still did not receive a minimum 8-hour break.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (128, "That decision states: \"Based on this, I find the rostering of these two shifts amounted to unreasonable management action given that it was in direct contradiction to the award and the 8-hour agreement.\"",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (129, "That decision states, under the heading \"Conclusion\": \"you sustained a personal injury of a psychological nature\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 (130, "That decision states, under the heading \"Conclusion\": \"your injury arose out of employment, to the extent that it arose out of factors 2, 3 and 4, where employment was a significant contributing factor\".",
     "Review Decision 69983 dated 24 October 2024 - the Respondent's own decision"),
 ("M", "THE APPELLANT'S CONTEMPORANEOUS ACCOUNT, AND THE DOCUMENTS THE RESPONDENT LISTS"),
 (131, "The Respondent's amended List of Documents dated 14 August 2026 lists at item 12 an email from the Appellant to WorkCover Queensland dated 12 July 2024 with the attachment described as \"Event overview - undated\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (132, "That amended List of Documents lists at item 14 an email from the Appellant to WorkCover Queensland dated 18 July 2024 with the attachment described as \"Witness statement - Carolyn Jeffrey\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (133, "That amended List of Documents lists at item 16 an email from Ms Carolyn Jeffrey to WorkCover Queensland dated 1 August 2024 described as a follow up statement.",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (134, "That amended List of Documents lists at item 25 an email from the Appellant to WorkCover Queensland dated 29 August 2024 described as regarding the after hours on call change, with the attachment described as \"Email: After hours on call process\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (135, "That amended List of Documents lists at item 26 an email from the Appellant to WorkCover Queensland dated 30 August 2024 described as regarding failure to consult, with the attachment described as \"Email: Task change switchboard - 19/04/2024\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (136, "That amended List of Documents lists at item 27 an email from the Appellant to WorkCover Queensland dated 30 August 2024 described as regarding failure to consult, with the attachment described as \"Email: MASPER process - 09/05/2024\".",
     "Respondent's amended List of Documents (Form 23) dated 14 August 2026"),
 (137, "The Appellant provided the document described at item 12 to WorkCover Queensland on 12 July 2024.",
     "As above; and the Appellant's email of that date"),
 (138, "On 11 August 2026 the Appellant served on the Respondent a bundle titled \"Stressor 1(a) - Particulars support bundle\", comprising 30 pages and six tabs, each stating a particular of Stressor 1(a) of the Amended Form 9A and enclosing the documents recording it.",
     "The bundle, and the Appellant's covering email of 11 August 2026"),
 ("N", "MATTERS THE RESPONDENT DOES NOT ALLEGE"),
 (139, "The Respondent does not allege that the Appellant was subject to any disciplinary process at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (140, "The Respondent does not allege that the Appellant's work performance was the subject of any formal performance management process at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (141, "The Respondent does not allege that the Appellant was the subject of any warning, whether written or oral, at any time before 18 June 2024.",
     "Respondent's amended statement of facts and contentions, 13 May 2026"),
 (142, "The Respondent's amended statement of facts and contentions does not identify the management action referred to in paragraph 27.",
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
 ("Document, \"Logan Hospital Switchboard Sick Leave Process\", version 1.1", "4 February 2025"),
 ("Letter, Metro South Hospital and Health Service to Commissioner Dwyer, reference K-LM26/729, "
  "signed by Ms N Cridland, Chief Executive", "5 June 2026"),
 ("Document, QH Leave Takings Report for the Appellant, produced by Metro South Health as item 15 "
  "of the Notice of non-party disclosure", "19 March 2024"),
 ("Letter, Ms L Forrest, Senior Consultant Human Resources, Logan and Beaudesert Health Service, "
  "to the Appellant", "7 July 2026"),
 ("Review Decision 69983, Workers' Compensation Regulator", "24 October 2024"),
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
          "letter of Ms L Forrest dated 7 July 2026; the QH Leave Takings Report for 19 March 2024; "
          "the \"Logan Hospital Switchboard Sick Leave Process\" version 1.1 dated 4 February 2025; "
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
print(f"built out/FORM24_SECOND_NOTICE_DRAFT.pdf - {nf} facts + 27 documents")
