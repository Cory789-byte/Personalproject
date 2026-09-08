#!/usr/bin/env python3
"""WC/2024/227 - SECOND AMENDED Form 9A (draft for application for leave to amend). Same structure and
wording as the Amended 9A filed 7 April 2026, with the corrections listed in the Schedule of Amendments.
Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle

H1=ParagraphStyle('H1',fontName='Helvetica-Bold',fontSize=11.5,leading=14,alignment=1,spaceAfter=1)
H2=ParagraphStyle('H2',fontName='Helvetica',fontSize=9.5,leading=12,alignment=1,spaceAfter=1)
HP=ParagraphStyle('HP',fontName='Helvetica-Bold',fontSize=10.5,leading=13,alignment=1,spaceAfter=1)
HR=ParagraphStyle('HR',fontName='Helvetica',fontSize=9.5,leading=12,alignment=1,spaceAfter=1)
T =ParagraphStyle('T',fontName='Helvetica-Bold',fontSize=12,leading=15,alignment=1,spaceBefore=6,spaceAfter=1)
TS=ParagraphStyle('TS',fontName='Helvetica-Oblique',fontSize=9,leading=11.5,alignment=1,spaceAfter=8)
PART=ParagraphStyle('PART',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=4)
SEC=ParagraphStyle('SEC',fontName='Helvetica-Bold',fontSize=10,leading=12.5,spaceBefore=5,spaceAfter=3)
B =ParagraphStyle('B',fontName='Helvetica',fontSize=9.6,leading=12.4,spaceAfter=4)
N =ParagraphStyle('N',parent=B,leftIndent=10*mm,firstLineIndent=-10*mm)
L =ParagraphStyle('L',parent=B,leftIndent=22*mm,firstLineIndent=-8*mm)
S =ParagraphStyle('S',parent=B,fontSize=8.6,leading=10.8,spaceAfter=0)
SB=ParagraphStyle('SB',parent=S,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)

s=[P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",H1),
   P("Workers' Compensation and Rehabilitation Act 2003 (Qld)",H2),
   P("Matter No: WC/2024/227",H2), Spacer(1,2*mm),
   P("BETWEEN:",HR), P("CORY LEA SHEPHERD",HP), P("(Appellant)",HR), P("and",HR),
   P("WORKERS' COMPENSATION REGULATOR",HP), P("(Respondent)",HR),
   P("SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS",T),
   P("(Proposed; to be filed pursuant to leave of the Commission. Amends the Amended Statement filed 7 April 2026 in the "
     "respects listed in the Schedule of Amendments at the end of this document.)",TS),

   P("PART A &mdash; IDENTIFYING INFORMATION",PART),
   Table([[P("Appellant:",B),P("Cory Lea Shepherd",B)],
          [P("Employer:",B),P("State of Queensland (Queensland Health) &ndash; Logan Hospital Switchboard",B)],
          [P("Role:",B),P("Administration Officer (AO3)",B)],
          [P("Injury:",B),P("Major Depressive Disorder with Anxious Distress (DSM-5 296.23)",B)],
          [P("Date of Injury Onset:",B),P("18 June 2024",B)]],colWidths=[45*mm,A4[0]-44*mm-45*mm],
         style=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),1),('TOPPADDING',(0,0),(-1,-1),1)])),

   P("PART B &mdash; STATEMENT OF MATERIAL FACTS",PART),
   P("References in the form \"(admitted: fact N)\" are to the facts admitted by the Respondent on 8 September 2026 in "
     "answer to the Appellant's notice to admit facts served 28 August 2026. References to \"the response of 18 February "
     "2026\" are to the Respondent's response to the Appellant's first notice to admit, by row.",S), Spacer(1,2*mm),

   P("1. The Worker and the Baseline",SEC),
   P("1.1&nbsp;&nbsp;At all material times, the Appellant was employed by the Employer in the Switchboard Department at Logan "
     "Hospital, coordinating life-safety emergency clinical codes (Code Blue, MET calls), in a position required to work "
     "continuous shift work over the full 24-hour period (admitted: facts 1 to 13).",N),
   P("1.2&nbsp;&nbsp;Before 18 June 2024 the Appellant had not been diagnosed with or treated for depression. The general "
     "practice record of 16 November 2023 records poor sleep with shift work, that the Appellant could not do shifts without "
     "a good sleep, \"No psychological illness such as depression/psychosis\", and mood good, with melatonin and temazepam "
     "prescribed (the Respondent admits that entry is listed in the record: response of 18 February 2026, row 31). The "
     "Appellant's history lists \"ADHD\" and \"Anxiety\" entered on 26 October 2022. The referral letter of 16 May 2024 "
     "records the medications then current, which include no antidepressant, anxiolytic or other psychotropic medication.",N),
   P("1.3&nbsp;&nbsp;On 18 June 2024, the Appellant suffered the onset of a psychiatric injury, subsequently diagnosed by Dr "
     "Ravikumar Krishnaiah, consultant psychiatrist, as Major Depressive Disorder with anxious distress (the Respondent admits "
     "that the report of 13 February 2025 so states: response of 18 February 2026, row 35). Dr Krishnaiah's report states that "
     "\"premature exposure to the workplace is more likely result in significant deterioration\" (admitted that the report so "
     "states: row 36). The diagnosis and its cause will be the subject of the oral evidence of Dr Krishnaiah and Dr Hawes.",N),
   P("1.4&nbsp;&nbsp;The Appellant's treating General Practitioner, Dr Hawes, recorded at the first presentation on 1 July 2024 "
     "\"work stress\", that \"they withhold pay at times, no overtime- not processed, manipulate his roster- so he works lates "
     "then earlies\", and \"causing anxiety\"; and in the work capacity certificate of the same date recorded the mechanism as "
     "\"ongoing breaking of workplace rules by bosses, victimizing him\" (the Respondent admits the certificate so states: "
     "response of 18 February 2026, row 33). The events so recorded are the facts admitted at 185 to 203 and 211 to 221.",N),

   P("2. The Causative Stressors",SEC),
   P("The Appellant's psychological injury was caused by a course of management conduct occurring between approximately "
     "June 2023 and June 2024, the events of which are established by the facts admitted on 8 September 2026:",B),
   P("<b>Stressor 1: A Hostile Course of Management Conduct, Reprisal, and Suppression of Rights</b>",B),
   P("(a)&nbsp;&nbsp;<b>Dereliction of Clinical Governance:</b> Throughout 2023 and 2024, the Appellant's Line Manager, Ms Chloe "
     "Taylor, maintained an erratic physical presence and imposed unassessed unilateral directives (extra administrative "
     "checks/paging) without consultation. From 18 July 2023 operators could no longer correct database entries, and "
     "after-hours corrections had to \"wait until either Chloe or myself are back\" (admitted: facts 39 to 48). The after-hours "
     "on-call arrangement of 15 April 2024 was introduced without any consultation record or ballot (admitted: facts 49, 181, "
     "273). In the week of 3 to 9 May 2024 the MASPER Registrar reported nine calls reaching the wrong team, including the MET "
     "call team ringing because \"switchboard could not tell them where VHUB was\"; Ms Taylor's first reply came five days and "
     "eighteen hours later, asking for the registrar's hours because they were \"not provided on the rosters\" (admitted: facts "
     "56 to 68). The Integrated Respiratory Service wrote on 15 and 20 May 2024 that \"we can not help patients or other clinical "
     "staff\" (admitted: facts 89 to 104). These directives bottlenecked emergency workflows and caused delays to the "
     "communication of urgent clinical information to clinical staff. The Appellant's attempts to mitigate these clinical risks "
     "were followed by the conduct described at (b), (c) and (f).",L),
   P("(b)&nbsp;&nbsp;<b>Unilateral Removal of a WHS Record:</b> On or about 6 June 2023, the Appellant recorded in the "
     "communication book a reminder regarding the necessity of updating medical on-call contact numbers. Ms Taylor removed "
     "the entry. When questioned, Ms Taylor subjected the Appellant to a hostile and verbally aggressive reprimand at the "
     "commencement of a shift in the presence of a colleague. Ms Taylor later recorded the removal in writing: \"I took it out "
     "last week\", and described the book as being used as a \"burn book\" (admitted: facts 143 to 149; the Respondent's own "
     "pleading admits the removal at paragraph 12(a)).",L),
   P("(c)&nbsp;&nbsp;<b>Refusal to Investigate WHS &amp; Fatigue Complaints:</b> On 7 August 2023, the Appellant submitted a "
     "grievance regarding Ms Taylor's conduct, raising WHS concerns regarding unsafe rostering practices and fatigue management "
     "risks. Ms Tammy Reese (Director) replied on 8 August 2023 without any investigation and the Appellant continued to report "
     "directly to Ms Taylor (admitted: facts 26 to 38). Metro South Health has since stated that complaints of this kind were "
     "\"managed solely via email or verbally\" and that no consequential change to operating procedures followed (admitted: "
     "facts 266 to 267).",L),
   P("(d)&nbsp;&nbsp;<b>Disparate Treatment &amp; Statutory Leave Obstruction (COVID):</b> Between 20 February and 1 March "
     "2024, Ms Taylor required the actively ill Appellant to self-administer COVID-19 Special Pandemic Leave via myHR, a "
     "facilitation she routinely exercised directly for other staff. The system records the Appellant's upload at 11:41:27 am "
     "on 20 February 2024. Ms Taylor declined the application twice, stating that evidence was \"not attached\", before "
     "approving it on the identical original evidence (admitted: facts 114 to 142). Requiring an incapacitated employee to "
     "repeatedly navigate an administrative portal to overcome factually incorrect declines constitutes unreasonable management "
     "action.",L),
   P("(e)&nbsp;&nbsp;<b>Public Interest Disclosure (PID):</b> On 13 May 2024, the Appellant lodged a complaint regarding "
     "clinical risks. The Ethical Standards Unit determined that this constituted a Public Interest Disclosure (admitted: "
     "response of 18 February 2026, row 20).",L),
   P("(f)&nbsp;&nbsp;<b>Immediate Reprisal:</b> Within 48 hours of the complaint being lodged, on 15 May 2024 at 6:23 pm, Ms "
     "Reese directed the Appellant to retract a routine workplace email asking for Ms Taylor's office hours. Two days later, "
     "on 17 May 2024, Ms Taylor sent the whole department an email stating her hours, the information the Appellant had asked "
     "for (admitted: facts 74 to 84). A comparable email sent by Ms Taylor attracted no such direction (admitted: response of "
     "18 February 2026, row 21).",L),
   P("(g)&nbsp;&nbsp;<b>Suppression of Industrial Representation During Roster Disputes:</b> On 11 August 2023 the Appellant "
     "notified Ms Taylor of his intention to become the Switchboard union delegate (the Respondent admits the text was sent: "
     "response of 18 February 2026, row 18; admitted: fact 294). The Union Encouragement Policy QH-POL-248 requires managers to "
     "take a \"positive, supportive role\" (admitted: fact 293). No ballot or vote for the position was held before "
     "18 June 2024; the Appellant was endorsed as a workplace delegate only on 3 November 2025 (admitted: fact 179). This left "
     "the department without local delegate representation during the period in which the Appellant was disputing unsafe "
     "rostering practices and fatigue risks.",L),
   P("<b>Stressor 2: Systemic Failure to Discharge Remuneration Obligations</b>",B),
   P("(a)&nbsp;&nbsp;<b>Persistent Payroll Failures and Public Holiday Rostering:</b> Between February and April 2024 the "
     "Appellant was not paid his correct entitlements. The fortnights from 5 February 2024 carried top-ups and reductions "
     "arising from 7-hour shifts and unprocessed overtime (admitted: facts 185 to 189), and the two February corrections "
     "never appeared in the myHR submissions report (admitted: fact 210). Over Easter 2024 the Appellant was rostered on for "
     "Good Friday, 29 March, and Easter Sunday, 31 March, and rostered off on Easter Saturday, 30 March 2024, and worked the "
     "06:00 shift on Monday 1 April 2024 following the 14:00 to 22:00 shift of Easter Sunday (Review Decision 69983, contents "
     "admitted). As a continuous shift worker in receipt of the additional week's leave, the Appellant was entitled under "
     "clause 23(h) of the Award to an additional day's wage or a day in lieu for Easter Saturday (admitted: fact 241); "
     "colleagues rostered on that day were paid at double time and one-half under clause 23(c). No payment was made for "
     "Easter Saturday until, following the Appellant's request of 8 April 2024, Ms Taylor submitted an AVAC for \"public "
     "holiday not required\" on 9 April 2024 (admitted: facts 242 to 245); the older dates the Appellant raised were referred "
     "to a payroll enquiry, and as at 1 May 2024 payroll was \"still reviewing your entitlements regarding public holidays "
     "not required\" (admitted: fact 255). By way of background, the decision under appeal records the same pattern at "
     "Easter 2023: on 4 April 2023 the Appellant told Ms Taylor the roster gave him 1 of 5 public holidays and reduced his "
     "pay by $1,500 for the fortnight, and on 26 April 2023 that he had not been paid for the Easter Monday public holiday "
     "(Review Decision 69983, contents admitted). The Appellant will give evidence of the rosters and pay advices for those "
     "periods and of the colleagues rostered on the public holidays on which he was rostered off.",L),
   P("(b)&nbsp;&nbsp;<b>Unreasonable Delay:</b> On 3 May 2024 Queensland Health Payroll identified the errors and directed Ms "
     "Taylor: \"Please submit an AVAC to correct these shifts for each fortnight so Cory is paid corrected\" (admitted: fact "
     "190). On 13 May 2024 Payroll wrote that it could not see that any of the issues had been corrected (admitted: fact 193). "
     "On 21 May 2024 Ms Taylor was \"still waiting payroll confirmation\" (admitted: fact 195). Ms Taylor submitted the AVAC on "
     "28 May 2024 (admitted: fact 209), 25 days after the direction; its status is recorded as \"Part Completed\" (admitted: "
     "fact 203).",L),
   P("<b>Stressor 3: Breaches of Fatigue Management</b>",B),
   P("(a)&nbsp;&nbsp;<b>The 7-hour break:</b> On 17-18 March 2024, the Employer rostered the Appellant to work consecutive "
     "shifts, finishing at 23:00 and commencing at 06:00, separated by a 7-hour break (admitted on the Respondent's own "
     "pleading at paragraph 22(a); facts 224 to 235). Factoring in the Appellant's commute, the Appellant was subjected to "
     "16 hours of wakefulness and work and 4 hours of commuting, leaving approximately 4 hours of actual sleep.",L),
   P("(b)&nbsp;&nbsp;<b>Bypass of the fatigue safety requirement despite prior warnings:</b> The Award and the Employer's "
     "Fatigue Risk Management Policy require a minimum break of 10 hours between shifts, or 8 hours by written agreement "
     "(admitted: fact 285). The written agreement of 17 June 2020 applied only where staff-initiated shift swaps had occurred "
     "(admitted: facts 224 to 225); the shifts of 17-18 March 2024 were not a swap. No fatigue risk assessment was made for the "
     "position, no fatigue risk management training was provided, and Metro South Health has stated that fatigue risk "
     "management assessment at the Switchboard occurred only after 30 June 2024 (admitted: facts 263 to 271). Despite the "
     "Appellant having previously raised explicit complaints to management regarding these fatigue risks, the Employer "
     "proceeded to roster the Appellant on a 7-hour break. Operating under that exhaustion, the Appellant was required to "
     "manage life-safety emergency codes and doctor pages through the SPOK system, including a MET call and a Code Blue to the "
     "same bed four minutes apart on the evening of 17 March and six emergency code entries between 06:00 and 14:00 on 18 March. "
     "Requiring an exhausted operator to control emergency clinical coordination while prior fatigue warnings stood "
     "unactioned was unreasonable.",L),
   P("(c)&nbsp;&nbsp;<b>Unjustified Administrative Detriment:</b> When the Appellant required recovery time, he requested "
     "fatigue leave on 8 April 2024; Ms Taylor escalated the enquiry to Human Resources on 9 April \"to confirm policies around "
     "this\"; no response was made until 1 May 2024, when the request was refused \"after a consultation with payroll and Human "
     "Resources\" on the basis of the 8-hour agreement signed on 17 June 2020, when the Appellant was a casual employee "
     "(admitted: facts 242 to 250). The Appellant funded the recovery day of 19 March 2024 from his own accrued personal leave. "
     "This shifted the financial detriment of the Employer's fatigue breach onto the injured worker.",L),
   P("(d)&nbsp;&nbsp;<b>The Regulator's own finding:</b> The Regulator's Review Unit, in Review Decision 69983 (24 October "
     "2024, pages 26 to 27), found that the rostering of these two shifts \"amounted to unreasonable management action given that "
     "it was in direct contradiction to the award and the 8-hour agreement\" (admitted: facts 257 to 261; the contents of the "
     "decision admitted in the response of 18 February 2026, row 34). The finding is relied upon as the Regulator's own review "
     "on the evidence then before it, not as binding the Commission.",L),

   P("3. Subsequent Aggravating Conduct (Post-Injury)",SEC),
   P("(a)&nbsp;&nbsp;On 12 and 16 July 2024, while the Appellant was on certified leave, the Employer scheduled meetings "
     "regarding his complaint.",L),
   P("(b)&nbsp;&nbsp;On 9 October 2024, the Employer confirmed that it treated the Appellant's employment as abandoned, despite "
     "his holding continuous medical certificates. The Appellant was subsequently reinstated to his employment with an "
     "effective date of 20 September 2024.",L),
   P("(c)&nbsp;&nbsp;Before serving any Form 29 notice of non-party disclosure, the Respondent obtained the Appellant's primary "
     "medical records (admitted: response of 18 February 2026, row 25). Form 29 notices were later issued on 4 July 2025.",L),
   P("The matters in this section are relied upon as the course of the injury after its onset, not as its cause.",B),

   P("PART C &mdash; LEGAL CONTENTIONS",PART),
   P("<b>Contention 1: The Injury is Compensable (s 32(1) WCRA)</b>",B),
   P("The Appellant sustained a \"personal injury\", being a psychiatric disorder, arising out of or in the course of his "
     "employment, to which his employment was a significant contributing factor.",B),
   P("<b>Contention 2: The Section 32(5) Exclusion Does Not Apply</b>",B),
   P("The Appellant accepts that he bears the onus, and discharges it on the facts admitted on 8 September 2026 and the "
     "evidence to be given.",B),
   P("(a)&nbsp;&nbsp;<b>Global Evaluation (Delaney):</b> The clinical governance dereliction, the removal of the WHS record, the "
     "25-day AVAC delay and the retraction direction form a course of conduct that was not reasonable management action, and "
     "was not taken in a reasonable way.",L),
   P("(b)&nbsp;&nbsp;<b>Single Unreasonable Stressor (Mahaffey):</b> The 7-hour break, found unreasonable by the Regulator's own "
     "Review Unit, was a significant contributing factor to the injury and independently takes the injury outside s 32(5).",L),
   P("<b>Contention 3: Evidentiary Contradiction</b>",B),
   P("The Respondent's pleading that all management action was reasonable is in direct contradiction with the finding of its "
     "own Review Unit, made on the same medical evidence, that the rostering of 17-18 March 2024 was unreasonable management "
     "action and that the Appellant's employment was a significant contributing factor to his psychological injury (admitted: "
     "facts 257 to 262).",B),

   P("PART D &mdash; ORDERS SOUGHT",PART),
   P("1.&nbsp;&nbsp;Appeal allowed; Decision set aside and replaced with claim acceptance.",N),
   P("2.&nbsp;&nbsp;A declaration that the Appellant's psychological injury is a compensable injury.",N),
   P("3.&nbsp;&nbsp;Costs reserved.",N),
   P("4.&nbsp;&nbsp;Such further or other orders as the Commission considers appropriate.",N),
   Spacer(1,4*mm),
   P("<b>FILED BY:</b><br/>Cory Lea Shepherd<br/>Appellant (Self-Represented)<br/>DATE: ____ September 2026 (subject to leave)",B),

   PageBreak(),
   P("SCHEDULE OF AMENDMENTS",T),
   P("Amended Statement filed 7 April 2026 &rarr; this Second Amended Statement",TS),
]
rows=[["Where","Was","Now","Why"],
 ["Part A, Role","Administration Officer (OO3)","Administration Officer (AO3)","The admitted role description states the classification as \"A03\" (fact 1)"],
 ["1.1","No reference","Continuous 24-hour shift work; facts 1 to 13","Admitted on 8 September 2026"],
 ["1.2","\"clean psychiatric baseline\"; \"(Admitted Fact: Form 24, Para 34)\"","The 16 November 2023 entry as recorded; the October 2022 history lines; the May 2024 medication list; correct citation (entry listed, accuracy not admitted)","Para 34 was admitted only as an entry listed in the record; para 35 (absence of contrary history) was denied on the 26 October 2022 entries. Pleading a clean baseline against a known contrary record is withdrawn; the actual record is pleaded"],
 ["1.3","\"(Admitted Fact: Paras 38, 39)\"","\"the report so states\" (rows 35, 36); diagnosis and cause for the oral evidence of the doctors","The response admitted the report says so, not its accuracy"],
 ["1.4","Mechanism pleaded as an admitted fact (Para 36)","The 1 July 2024 note quoted; the certificate wording as recorded (row 33); the events referred to facts 185 to 203, 211 to 221","The response admitted the certificate says so and denied it as a fact; the events are now admitted"],
 ["2 (chapeau)","\"composite course\"","\"course of management conduct ... established by the facts admitted on 8 September 2026\"","\"Composite\" removed; facts anchored"],
 ["1(a)","No fact citations; \"delayed urgent pathology results\"","Dated events with fact citations 39 to 68, 89 to 104, 181, 273; \"urgent clinical information\"","Particularised on admitted facts"],
 ["1(b)","\"Destruction\"; \"destroyed\"; Para 14","\"Removal\"; \"removed\"; the entry identified as the reminder; \"burn book\" added; facts 143 to 149 and SOFC 12(a)","The document shows removal, not destruction; the reminder's subject is now in evidence"],
 ["1(c)","\"dismissed the complaint the same day\"; Para 5","Ms Reese replied on 8 August 2023; facts 26 to 38; Metro South's \"managed solely via email or verbally\" (266, 267)","The reply was the following day; the absence of investigation is now Metro South's own statement"],
 ["1(d)","\"capriciously\"; \"factually false denials\"","\"declined the application twice, stating that evidence was 'not attached'\"; \"factually incorrect declines\"; facts 114 to 142","Same facts, admitted; characterisation reduced to what the documents show"],
 ["1(e)","\"corrupt conduct complaint\"","\"complaint regarding clinical risks\"; row 20","Content of the disclosure not pleaded"],
 ["1(f)","Para 21 only","The 15 May 6:23 pm direction, the 17 May hours email, facts 74 to 84; row 21 retained","Sequence now admitted with dates"],
 ["1(g)","\"April 2023\"; \"suppressed ... for 13 months\"; Paras 17, 18","11 August 2023; no ballot before 18 June 2024; endorsed 3 November 2025; facts 179, 293, 294; row 18","The notification was 11 August 2023 (the Appellant's own affidavit and the Respondent's admission of the text); the duration is stated by dates"],
 ["2(a)","\"documented 42% pay disparity\"","The February fortnights (185 to 189, 210); Easter 2024 day by day from the Review Decision: on for Good Friday and Easter Sunday, off Easter Saturday 30 March, the Monday 06:00 shift after the Sunday 14:00 to 22:00 shift; Award cl 23(h) and (c) (fact 241); the AVAC for Easter Saturday submitted only on 9 April (242 to 245); payroll still reviewing at 1 May (255); the Easter 2023 pattern as recorded in the decision","The 42% comparator pleaded in February was denied (paras 42 to 45) and the comparator data is not held; the dates, the Award entitlement and the difference in what was paid are pleaded from the decision's own record and the Award, with the rosters and pay advices to be given in evidence"],
 ["2(b)","\"IMMEDIATELY\" (Para 40); \"admitted 25-day delay (Para 41)\"","The 3 May email quoted as written (fact 190); 13 May and 21 May (193, 195); AVAC 28 May (209); \"Part Completed\" (203); 25 days as arithmetic","The 3 May email does not contain \"IMMEDIATELY\"; para 41 was denied; the dates are now admitted"],
 ["3, heading","\"Admitted Breaches of Statutory Fatigue Management\"","\"Breaches of Fatigue Management\"","The breach is contended, not admitted"],
 ["3(a)","\"(Admitted Fact: Para 1)\"","SOFC paragraph 22(a); facts 224 to 235","Anchored to the Respondent's own pleading of the 7-hour break"],
 ["3(b)","\"mandate a minimum 10-hour rest break (Para 3)\"; the \"Neville Report\" sentence","10 hours or 8 by written agreement (fact 285); the agreement applied only to staff-initiated swaps (224, 225); no assessment or training (263 to 271); the March codes","Para 3 admitted the 10-or-8 rule; the Neville Report reference has no source and is removed; \"non-delegable\" and \"objectively reckless\" removed"],
 ["3(c)","\"misapplied a superseded 2020 casual agreement to deny statutory paid fatigue leave\"","The 8 April request, the 9 April escalation, no response to 1 May, refusal after consultation, the agreement signed as a casual (242 to 250)","Sequence admitted; \"superseded\" and \"statutory\" removed as contentions not facts"],
 ["3(d)","\"Independent Review Office (IRO)\"; Para 37","The Regulator's Review Unit, Review Decision 69983, pages 26 to 27, quoted; facts 257 to 261; row 34","No body called the IRO exists; the finding is quoted and admitted"],
 ["3(b) post-injury","\"8 October 2024 ... terminated\"","9 October 2024, treated as abandoned; reinstated with an effective date of 20 September 2024","Date corrected to the letter; reinstatement stated in the deed's terms"],
 ["3(c) post-injury","\"without issuing the mandatory Form 29 Notice (Rule 64C)\"","Records obtained before any Form 29 (row 25); notices later issued 4 July 2025","Accurate sequence; no rule breach asserted"],
 ["Part C, Contention 2","\"The Respondent bears the onus under Prizeman v Q-Comp\"","The Appellant accepts the onus and discharges it on the admitted facts","The Commission's Guide, Part 7.3, places the onus on the Appellant"],
 ["Contention 2(a)","\"composite, hostile course of conduct\"","\"course of conduct that was not reasonable management action, and was not taken in a reasonable way\"","Section 32(5) test stated in its terms"],
 ["Contention 3","\"its own IRO finding\"","The Review Unit's findings on unreasonable management action and on significant contributing factor (257 to 262)","Both findings now admitted as the decision's contents"],
]
data=[[P(c,SB) for c in rows[0]]]+[[P(c,S) for c in r] for r in rows[1:]]
W=A4[0]-44*mm
t=Table(data,colWidths=[22*mm,46*mm,54*mm,W-122*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#888888')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),
                       ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t)

class Doc(BaseDocTemplate):
    pass
def footer(canvas,doc):
    canvas.saveState(); canvas.setFont('Helvetica',8.5)
    canvas.drawString(22*mm,10*mm,"Matter No: WC/2024/227"); canvas.drawRightString(A4[0]-22*mm,10*mm,f"Page {doc.page}")
    canvas.restoreState()
buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=22*mm,rightMargin=22*mm,topMargin=16*mm,bottomMargin=16*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(22*mm,16*mm,A4[0]-44*mm,A4[1]-32*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
d.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/SECOND_AMENDED_FORM9A_DRAFT_for_leave.pdf"; pdf.save(out,linearize=True); print("built",out,n,"page(s)")
