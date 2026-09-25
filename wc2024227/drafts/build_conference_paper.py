#!/usr/bin/env python3
"""WC/2024/227 - Appellant's conference paper for the second s 552A conference: what is settled, what can be
closed at the conference, and questions for the Respondent arising from its outlines of evidence of
24 September 2026, each set against the admitted facts. States facts, not motives. Metadata stripped."""
import io, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv) > 1 else "25 September 2026"

B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.2, leading=11.8, spaceAfter=4)
T  = ParagraphStyle('T', parent=B, fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceAfter=2)
H  = ParagraphStyle('H', parent=B, fontName='Helvetica-Bold', spaceBefore=4, spaceAfter=2, keepWithNext=1)
L  = ParagraphStyle('L', parent=B, leftIndent=6*mm, firstLineIndent=-4*mm, spaceAfter=2)
C  = ParagraphStyle('C', parent=B, fontSize=8.1, leading=10.0, spaceAfter=0)
CB = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
N  = ParagraphStyle('N', parent=B, fontSize=8.2, leading=10.2)
SH = ParagraphStyle('SH', parent=N, keepWithNext=1)
def P(t, s=B): return Paragraph(t, s)
def SIG():
    i = RLImage('assets/SIGNATURE_CoryShepherd.png', width=26*mm, height=13.4*mm); i.hAlign = 'LEFT'; return i

W = A4[0] - 40*mm
def table(rows, widths, bold_first_col=False):
    data = [[P(c, CB) for c in rows[0]]] + [[P(c, CB if (bold_first_col and j == 0) else C) for j, c in enumerate(r)] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#888888')),
                           ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EEEEEE')),
                           ('VALIGN', (0,0), (-1,-1), 'TOP'),
                           ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
                           ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    return t

CLOSE = [["", "Matter", "What would close it"],
 ["A", "The ten documents not yet admitted or confirmed (Tabs 1, 5, 17 to 19, 21, 22, 23, 24 and 31)",
  "An agreed list of documents to be tendered without further proof, once Metro South Health provides its copies. The contents of all of them except Tab 31 are already admitted"],
 ["B", "Facts 228 to 231: the 2024 Emergency Code Register entries for 17 to 19 March 2024",
  "Production of the MET call spreadsheet that Metro South Health, in its letter of 5 June 2026, states \"is available for the period 17-18 March 2024\" (fact 268)"],
 ["C", "The medical evidence",
  "The Respondent to indicate whether it requires Dr Krishnaiah and Dr Hawes to attend for cross-examination"],
 ["D", "SOFC [27]: the management action said to be reasonable",
  "The Respondent to state its settled position on each admitted action listed in section 6. Fact 303 admits that SOFC [27] does not identify them"],
]

QA = [["", "Question for the Respondent", "The admitted record"],
 ["1", "Does the Respondent maintain that no directives were issued without consultation or assessment "
       "(SOFC [11]; outline of Ms Taylor)?",
  "Ms Taylor's email of 15 April 2024: \"This new process is effective from today\" (facts 49 to 53; Tab 6, confirmed "
  "23 September 2026). A further new process from 19 April 2024 (fact 54). No clause 6.2 agreement or ballot is "
  "alleged (facts 180, 181). The Chief Executive's letter of 5 June 2026: fatigue risk assessment at the switchboard "
  "\"occurred after 30 June 2024\" (fact 264; Tab 20, confirmed)"],
 ["2", "Does the Respondent maintain that on 13 to 15 May 2024 the Appellant failed to follow the on-call notification "
       "process (SOFC [16(b)]; outline of Ms Taylor)?",
  "Ms Taylor's email of 15 April 2024: contact her \"through switch/office or mobile\" (fact 163). Her email of 14 May "
  "2024: \"either through switch or my office/mobile\" (facts 164, 165). It is not alleged that the Appellant was told, "
  "before 14 May 2024, that notifying his unavailability by telephoning the Switchboard did not comply (fact 166)"],
 ["3", "Does the Respondent maintain that the Appellant's email of 15 May 2024 was an accusation "
       "(outline of Ms Reese)?",
  "Ms Taylor's email of 23 August 2023, \"What's Chloe's Hours?!\": start \"between 6-9am\", finish \"2-5pm\" "
  "(facts 71, 72; Tab 30, confirmed). No fixed hours stated to May 2024 (fact 73). Ms Reese, 21 May 2024: \"I will "
  "follow up on the issues raised\" (fact 79). Ms Taylor published her hours on 17 May 2024 (facts 81 to 84)"],
 ["4", "Who exercised the delegated power to decide the Special Pandemic Leave application, process 15480560?",
  "SOFC [14] states the attachments were present. Ms Taylor had noted the statutory declaration \"was sufficient "
  "evidence\" (fact 138) and declined the application twice (facts 116, 118, 123). It was approved by Ms Taylor as "
  "reviewer on 29 February and Ms Reese as manager on 1 March 2024 (facts 120, 121). The power was sub-delegated to "
  "Band 9 and could not be sub-delegated further (facts 127, 128); it is not alleged that Ms Taylor or Ms Reese held "
  "it (facts 129 to 131)"],
 ["5", "Does the Respondent maintain that pay errors were \"remedied in a timely manner\" and that there are no "
       "outstanding underpayments (SOFC [20(c)], [20(f)]; outline of Ms Wright)?",
  "Payroll asked the line manager for AVACs on 3 May 2024 (facts 183 to 190). On 13 May payroll could not see that any "
  "had been corrected (facts 192, 193). The AVAC was submitted on 28 May 2024 (fact 297), with claims \"older than 3 "
  "months\" (fact 197), and is recorded as \"Part Completed\" (fact 203). Two AVAC process numbers cited by payroll do "
  "not appear in the myHR report (fact 210)"],
]

DUTIES = [["Duty (role description, Administration Officer, Switchboard Services, Tab 1)", "Fact"],
 ["\"Collate information and maintain Omnivista database and SharePoint to ensure information held within Switchboard "
  "Services is accurate and appropriate\"", "6"],
 ["\"Participate in the Emergency Response process by receiving emergency response notifications and distributing them to "
  "the appropriate response groups... strictly adhering to protocols and timeframes\"", "8"],
 ["Pager allocation and repair, \"maintaining database and registers with accurate and current information\"", "7"],
 ["\"Maintain call queues to minimum at all times\"", "5"],
 ["\"Maintain discretion and exercise judgement... in situations where precedence have not been set and procedures not "
  "defined\"", "9"],
 ["\"Follow defined service quality standards, occupational health and safety policies and procedures\"", "12"],
 ["Continuous shift work \"over the full 24-hour period, 7 days a week\"", "2, 13"],
]

FEEDBACK = [["When", "What the admitted record shows", "Facts", "Interval"],
 ["2 and 3 May 2024", "Five misrouted calls (2 May 14:47; 3 May 10:00, 10:22, 11:43, 14:46), including a MET call: "
  "\"switchboard could not tell them where VHUB was. Had to be redirected by MASPER\"", "57, 58", ""],
 ["3 May, 3:06 pm", "Vivian Kwok, MASPER Registrar, reports them to Ms Taylor, copied to Dr Pan Jane Wong: \"I've been "
  "requested to email you with the list of switchboard issues\"", "56", "First report"],
 ["5 to 8 May", "Four further occasions (5 May 14:45; 7 May 07:45; 8 May 8:53, 9:59); on 8 May each call "
  "\"incorrectly put through to MASPER\"", "60, 61", ""],
 ["8 May, 5:28 pm", "Second report to Ms Taylor, copied to Dr Wong", "59, 62", "Fifth calendar day"],
 ["9 May, 9:20 am", "Ms Taylor replies to the Registrar and Dr Wong", "63 to 65", "5 days 18 h 14 min after the first report"],
 ["9 May, 10:15 am", "First communication to Switchboard staff (\"MASPER process\"): \"There have been many ongoing issues "
  "raised by the MASPER and the medical department about calls being transferred to the wrong medical teams\"",
  "66, 67, 69", "None alleged before this"],
 ["", "Every occasion occurred while the after-hours arrangement of 15 April 2024 was in force", "68", ""],
 ["15 May, 11:47 am", "Integrated Respiratory Service asks for the directory to be amended", "89, 90", "No response alleged before 20 May"],
 ["20 May, 11:03 am", "Reminder: \"we continue to get calls put through to us\"", "91 to 93", "Fifth day; no response alleged before 2:05 pm"],
 ["20 May, 2:05 pm", "The Appellant escalates to Ms Taylor, within her stated office hours", "94 to 98",
  "3 h 2 min after the reminder; 5 days 2 h 18 min after the first request"],
 ["20 May, 4:30 pm", "Ms Taylor: \"this task was being actioned\"", "100 to 104", "2 h 25 min later; 2 h after her stated hours"],
 ["", "No document of that discussion is listed. The directory is not alleged to have been amended by 20 May, nor staff "
  "notified of its modification on 22 February 2024", "105 to 110", ""],
]

RESTRICT = [["When", "What the admitted record shows", "Facts"],
 ["18 Jul 2023, 12:56 pm", "Database access removed from all Switchboard staff while the coordinator fixes the database: "
  "\"I will be removing everyone's access to the database\"", "39, 40"],
 ["18 Jul 2023", "The \"Contact & Number Changes\" book removed from the room", "45"],
 ["From 18 Jul 2023", "Changes only through Ms Stibbard, whose hours were \"every Tuesday and second Monday, 8:00 - 16:00\", "
  "or through Ms Taylor if Ms Stibbard was absent and the change urgent", "41 to 43"],
 ["From 18 Jul 2023", "After hours (\"overnights, on the weekend or public holiday\"), requests \"have to wait until either "
  "Chloe or myself are back\"", "44"],
 ["15 Apr 2024, 12:39 pm", "New after-hours on-call process, \"effective from today\"; during office hours, contact Ms Taylor",
  "49 to 52"],
 ["To 18 Jun 2024", "The Respondent does not allege that database access was restored to the Appellant", "55"],
]

QB = [["", "Question for the Respondent", "The admitted record"],
 ["6", "Does the Respondent maintain its non-admission of Stressor 1(a) (SOFC [11])?",
  "Sections 4.1 to 4.3, every entry admitted. The duties to maintain the database (fact 6) and to distribute emergency "
  "notifications \"strictly adhering to protocols and timeframes\" (fact 8) fell to be performed after database access "
  "was removed on 18 July 2023 (fact 40), and the Respondent does not allege it was restored (fact 55)"],
 ["7", "What action does the Respondent say was taken on the reports of 3, 8, 15 and 20 May 2024 before the Appellant's "
       "email of 20 May 2024 at 2:05 pm, and what document records it?",
  "No communication to staff is alleged before 9 May at 10:15 am (fact 69). No response to either Integrated Respiratory "
  "Service email is alleged before the Appellant's escalation (facts 90, 93). No document of the 20 May discussion is "
  "listed (fact 105)"],
 ["8", "Does the Respondent rely on Metro South Health's statement that there were \"no 'consequential' changes to "
       "operating procedures\" (fact 266)?",
  "New processes of 15 April (facts 49 to 53), 19 April (fact 54) and 9 May 2024 (fact 66). Complaints were \"managed "
  "solely via email or verbally\" (fact 267)"],
]

S3_AGREE = [["When", "What the admitted record shows", "Facts"],
 ["Standing rule", "The Award and the employer's policy require a minimum break of 10 hours between shifts, or 8 hours by "
  "written agreement", "285, 257"],
 ["17 Jun 2020", "The Appellant signs an agreement allowing an 8-hour break", "17"],
 ["Jun 2020", "The fatigue leave policy: problems \"can be overcome... by not rostering the employee who is on call for the "
  "first shift of the following day\"", "239, 240"],
 ["Sep to Oct 2023", "The Appellant moves to permanent full-time hours from 16 October 2023; the employer confirms a "
  "\"change to your employment contract and adjustments in your working hours\"", "37, 38, 20"],
 ["To 18 Mar 2024", "No review, re-execution or re-confirmation of the agreement is alleged; nor that he was told, before "
  "1 May 2024, that it could be terminated", "21, 22"],
 ["7 Jul 2026", "Metro South Health Human Resources: the agreement \"is only applied where staff initiated shift swaps have "
  "occurred\". No swap is alleged for 17 and 18 March 2024", "225, 234"],
]

S3_PAIR = [["When", "What the record shows", "Facts"],
 ["17 Mar 2024 (Sunday)", "Rostered to finish at 23:00. No clause 6.2 agreement is alleged for this rostering", "284, 180"],
 ["17 Mar 2024 (the day of the shift ending at 23:00)", "The Emergency Code Register records eight codes: 03:57 CODE GREY ED "
  "LOUNGE; 05:19 MET CALL WARD 5A BED 27; 07:48 ED CODE GREY CORRIDOR NEAR SHORT STAY; 13:48 MET CALL WARD 3B BED 2; 14:13 "
  "CODE GREY ED ADULT ACUTE BED 15; <b>19:16 MET CALL WARD 2H BED 7; 19:20 CODE BLUE WARD 2H BED 7; 21:16 MET CALL WARD 2Q "
  "BED 5</b>", "228 (not admitted); Tab 31; 268"],
 ["18 Mar 2024 (Monday)", "Rostered to start at 06:00. A break of 7 hours. Leaving up to 30 minutes early would still not "
  "give 8 hours", "284, 227, 258, 259"],
 ["18 Mar, 06:00 to 14:00", "Six codes: 08:48 CODE GREY QAS TRIAGE AIRLOCK; 09:20 MET CALL WARD 6A BED 8; 11:31 MET CALL "
  "WARD 3DR BED 14; 11:32 CANCELLED MET CALL WARD 3DR BED 14; 11:35 NEONATAL MET CALL THEATRE 2; 13:09 NEONATAL MET CALL "
  "BIRTH SUITES 5", "229, 230 (not admitted); Tab 31; 268"],
 ["18 Mar, after 14:00", "Five further codes: 14:38 MET CALL WARD 3DR BED 11; 14:45 and 14:55 CODE GREY QAS TRIAGE; 19:15 and "
  "19:34 CODE GREY ED QAS RAMP", "Tab 31"],
 ["Travel", "The 7 hours did not include travel; with travel, the break \"would have been less than 5 hours\" (the "
  "Appellant's account, as recorded by the Review Unit)", "251"],
 ["19 Mar 2024", "Sick leave, 7.6 hours, approved", "235"],
]

S3_RESP = [["When", "What the admitted record shows", "Facts", "Interval"],
 ["8 Apr 2024", "The Appellant asks Ms Taylor to review his pay for 8 to 31 March 2024, citing the 10-hour minimum",
  "242, 243", ""],
 ["9 Apr 2024", "Ms Taylor escalates the fatigue leave enquiry to Human Resources, and asks him to raise concerns as soon as "
  "they arise", "244, 245", ""],
 ["24 Apr 2024", "The Appellant: \"more than 2 weeks without any response or overtime payment\"", "246",
  "No response alleged between 9 April and 1 May (fact 250)"],
 ["1 May 2024", "Ms Taylor: after consulting payroll and Human Resources, the fatigue payment \"would not be processed due to "
  "the existing 8-hour agreement\"; \"you are able to terminate this agreement going forward\"", "247, 248",
  "23 days after the request (fact 249)"],
 ["1 May 2024, 1:18 pm", "The Appellant sends Ms Reese the fatigue toolkit in the Operations Manual", "214", ""],
 ["10 May 2024", "Ms Reese to Human Resources: his concern is \"how it is impacting on staff fatigue, or more specifically "
  "his fatigue\"; the roster risk rating is \"at best... 11 which is moderate\"", "218, 219", ""],
 ["20 May 2024", "Ms Reese follows up with Human Resources, attaching the Fatigue Risk Management Systems guideline", "222, 223", ""],
 ["24 Oct 2024", "The Respondent's Review Unit: \"uncertainty\" whether the agreement applied; the rostering \"amounted to "
  "unreasonable management action given that it was in direct contradiction to the award and the 8-hour agreement\"",
  "254, 260", ""],
 ["To 30 Jun 2024", "No fatigue risk assessment, training or implementation at the Switchboard is alleged. The Chief "
  "Executive: the assessment \"occurred after 30 June 2024\"", "264, 269 to 271", ""],
]

QC = [["", "Question for the Respondent", "The admitted record"],
 ["9", "Does the Respondent maintain that the 2020 eight-hour agreement applied to the shifts of 17 and 18 March 2024 "
       "(SOFC [22(e)]; outlines of Ms Taylor, Ms Reese and Ms Wright)?",
  "Section 5.1. No swap is alleged (fact 234); Human Resources limits the agreement to staff-initiated swaps (fact 225). "
  "The break was seven hours, less than eight on any view (facts 258, 259, 284)"],
 ["10", "Does the Respondent maintain that the break was \"not intentional or repeated\" in the sense that no other "
        "rostering error affected the Appellant (SOFC [22(a)]; outline of Ms Taylor)?",
  "Ms Reese, 7 August 2023: \"a rostering error that was accidentally made by Chloe with regards to night shifts\" (fact 287). "
  "Ms Taylor, 7 August 2023: \"this was an oversight\" (fact 156). Ms Reese, 26 April 2024: Ms Taylor \"was working to fix "
  "this error\" (facts 211, 212). Ms Reese to Human Resources, 10 May 2024: \"I acknowledge there has been a few rostering "
  "errors made by Chloe with regards to Cory's line in past rosters\" (fact 220)"],
 ["11", "On what basis does the Respondent say the fatigue payment for 18 March 2024 was declined: the 2020 agreement, or "
        "clause 18.10 of the Award?",
  "The reason given on 1 May 2024 was \"the existing 8-hour agreement\" (fact 247). SOFC [24(b)] pleads clause 18.10, "
  "\"because he was not performing overtime\" (fact 237)"],
 ["12", "Which management action does the Respondent say was reasonable in respect of the break, the 23-day response, and "
        "the advice that the agreement could be terminated \"going forward\"?",
  "The Review Unit found the rostering \"unreasonable management action\" (fact 260). Payroll's advice, in the outline of "
  "Ms Wright: \"a rostering practice issue for the line manager\". SOFC [27] identifies no action (fact 303)"],
]

RMA = [["", "Action (admitted facts)", "Management action? (yes / no)", "Reasonable and taken in a reasonable way? (yes / no)"],
 ["A", "Removal of database access from all Switchboard staff, and of the \"Contact & Number Changes\" book, "
       "18 July 2023, without restoration alleged (facts 40, 45, 55)", "", ""],
 ["B", "Changes routed only through Ms Stibbard or Ms Taylor, with after-hours requests to \"wait until either Chloe or "
       "myself are back\" (facts 41 to 44)", "", ""],
 ["C", "The after-hours on-call process \"effective from today\", 15 April 2024 (facts 49 to 52, 180, 181)", "", ""],
 ["D", "The response to the MASPER Registrar's reports of 3 and 8 May 2024 (facts 56 to 69)", "", ""],
 ["E", "The response to the Integrated Respiratory Service, 15 to 20 May 2024 (facts 89 to 110)", "", ""],
 ["F", "Removal of the Communication Book entry, June 2023 (facts 143 to 147)", "", ""],
 ["G", "The rostering of 17 and 18 March 2024 with a seven-hour break. The Respondent's review decision found it "
       "\"unreasonable management action\" (facts 226, 258 to 260, 284)", "", ""],
 ["H", "The response of 1 May 2024 declining the fatigue payment, 23 days after the request, and the advice that the "
       "agreement could be terminated \"going forward\" (facts 242 to 250)", "", ""],
 ["I", "The two declines of the Special Pandemic Leave application, February 2024 (facts 116 to 123, 127 to 131; SOFC [14])", "", ""],
 ["J", "The timing of the AVAC corrections, 3 to 28 May 2024 (facts 183 to 197, 297)", "", ""],
 ["K", "The request of 15 May 2024 that the Appellant retract his email (facts 74 to 79)", "", ""],
]

RESP = [["Q", "Matter", "Respondent's position"],
 ["1", "Directives issued without consultation or assessment (SOFC [11])", ""],
 ["2", "The on-call notification process, 13 to 15 May 2024 (SOFC [16(b)])", ""],
 ["3", "The Appellant's email of 15 May 2024 as an accusation (outline of Ms Reese)", ""],
 ["4", "The delegate who decided the Special Pandemic Leave application (SOFC [14])", ""],
 ["5", "Pay errors \"remedied in a timely manner\"; no outstanding underpayments (SOFC [20])", ""],
 ["6", "Non-admission of Stressor 1(a) (SOFC [11])", ""],
 ["7", "Action taken on the reports of 3, 8, 15 and 20 May 2024 before 2:05 pm on 20 May, and the document recording it", ""],
 ["8", "Reliance on \"no 'consequential' changes to operating procedures\" (fact 266)", ""],
 ["9", "Application of the 2020 eight-hour agreement to 17 and 18 March 2024 (SOFC [22(e)])", ""],
 ["10", "The break as \"not intentional or repeated\" (SOFC [22(a)])", ""],
 ["11", "The basis on which the fatigue payment was declined: the agreement or clause 18.10 (SOFC [24(b)])", ""],
 ["12", "The management action said to be reasonable in Stressor 3 (SOFC [27])", ""],
]

s = [P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", N),
     P("WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator", T),
     P("<b>Appellant's conference paper</b> &nbsp;|&nbsp; Second conference under section 552A of the <i>Industrial "
       f"Relations Act 2016</i> &nbsp;|&nbsp; Provided to the Respondent on {DATE}", B),
     P("This paper is provided to the Respondent for the purposes of the conference. The Appellant asks the Respondent to "
       "indicate, before the conference, its position on each question in sections 3, 4 and 5 (using the response schedule "
       "at section 7) and its settled position on each action listed in section 6. Fact numbers are those of the "
       "Appellant's notice to admit facts of 28 August 2026, as answered by the Respondent on 8 September 2026. Tab "
       "numbers are those of Annexure A to that notice. \"SOFC\" is the Respondent's amended statement of facts and "
       "contentions dated 13 May 2026.", N),

     P("1. What is settled", H),
     P("The Respondent admitted 298 of the 303 facts. The other five were not admitted, and none was denied. 29 of "
       "the 39 documents annexed to the notices are admitted or confirmed. No admission has been withdrawn. The "
       "Respondent has served outlines of evidence for four lay witnesses and no medical or expert evidence.", B),

     P("2. What can be closed at this conference", H),
     table(CLOSE, [8*mm, 58*mm, W - 66*mm]),
     Spacer(1, 3*mm),

     P("3. Questions arising from the Respondent's outlines of evidence of 24 September 2026", H),
     P("Each question below arises where a passage in the Respondent's outlines sits beside a fact the Respondent "
       "has admitted. The Appellant asks the Respondent to indicate its position on each, so that the issues for any "
       "hearing can be confined to those genuinely in dispute.", B),
     table(QA, [8*mm, 62*mm, W - 70*mm]),
     Spacer(1, 3*mm),

     P("4. Stressor 1(a): the duties, the doctors' reports, and the restrictions", H),
     P("None of the Respondent's outlines of evidence addresses the Appellant's database and emergency response duties, "
       "the reports of the MASPER Registrar or the Integrated Respiratory Service, or the restrictions on access to the "
       "database. The admitted record is as follows.", B),
     P("<b>4.1 The Appellant's duties</b>", SH),
     table(DUTIES, [W - 16*mm, 16*mm]),
     Spacer(1, 3*mm),
     P("<b>4.2 The doctors' reports of misrouted calls, and the response</b>", SH),
     table(FEEDBACK, [26*mm, W - 26*mm - 20*mm - 38*mm, 20*mm, 38*mm]),
     Spacer(1, 3*mm),
     P("<b>4.3 The restrictions on access to the database and on after-hours changes</b>", SH),
     table(RESTRICT, [30*mm, W - 30*mm - 20*mm, 20*mm]),
     Spacer(1, 3*mm),
     table(QB, [8*mm, 62*mm, W - 70*mm]),
     Spacer(1, 3*mm),

     P("5. Stressor 3: the break of 17 to 18 March 2024, as one sequence", H),
     P("The seven-hour break is admitted by both parties (facts 226, 284). The sequence around it, from the agreement relied "
       "on to the response to the Appellant's request, is set out below. The emergency codes are shown from Tab 31, the "
       "Appellant's capture of Metro South Health's \"2024 Emergency Code Register\". Facts 228 to 230 are not admitted; Metro "
       "South Health states that the MET call spreadsheet for 17 and 18 March 2024 is available (fact 268), and its "
       "production would settle them.", B),
     P("<b>5.1 The rule and the agreement</b>", SH), table(S3_AGREE, [28*mm, W - 28*mm - 26*mm, 26*mm]),
     Spacer(1, 3*mm),
     P("<b>5.2 The shift pairing, the emergency calls, and travel</b>", SH), table(S3_PAIR, [30*mm, W - 30*mm - 34*mm, 34*mm]),
     Spacer(1, 3*mm),
     P("<b>5.3 The request, the response, and what followed</b>", SH),
     table(S3_RESP, [24*mm, W - 24*mm - 20*mm - 36*mm, 20*mm, 36*mm]),
     Spacer(1, 3*mm),
     table(QC, [8*mm, 62*mm, W - 70*mm]),
     Spacer(1, 3*mm),

     P("6. The Respondent's settled position under section 32(5)", H),
       P("SOFC [27] contends that any management action involved in the causation of any injury was reasonable management "
         "action taken in a reasonable way. It does not identify the action relied on (fact 303). As particulars of that "
         "contention, the Respondent is asked to state its settled position on each action below: whether it says the "
         "action was management action, and, if so, whether it says the action was reasonable and taken in a reasonable "
         "way. Where the answer is yes to both, the Respondent is asked to identify the facts relied on.", B),
       table(RMA, [8*mm, W - 8*mm - 30*mm - 36*mm, 30*mm, 36*mm]),
     Spacer(1, 3*mm),

     P("7. Response schedule for the Respondent", H),
       P("For each question, the Respondent is asked to indicate whether the position is maintained or not maintained or, "
         "for questions 4, 7, 11 and 12, to answer it. A matter not maintained can be recorded at the conference as no "
         "longer in issue.", B),
       table(RESP, [10*mm, 88*mm, W - 98*mm]),
     Spacer(1, 3*mm),

     KeepTogether([
       P("8. The Appellant's position", H),
       P("On the admitted record, the Appellant considers that the primary facts are settled and that the matters "
         "remaining are the application of the law to those facts and the medical evidence. The Appellant invites "
         "the Respondent to consider its position on the admitted record. Where a position is maintained, the "
         "Appellant will address it at any hearing by reference to the admitted facts identified in this paper. If the "
         "matter does not resolve, the Appellant is ready to proceed to a hearing on the issues that remain.", B),
       Spacer(1, 1*mm), SIG(),
       P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B)]),
]

buf = io.BytesIO()
d = BaseDocTemplate(buf, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=11*mm, bottomMargin=11*mm)
d.addPageTemplates([PageTemplate(id='n', frames=[Frame(20*mm, 11*mm, A4[0]-40*mm, A4[1]-22*mm,
                    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf = pikepdf.open(buf); n = len(pdf.pages)
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "out/CONFERENCE_PAPER_s552A_Appellant.pdf"; pdf.save(out, linearize=True); print("built", out, n, "page(s)")
