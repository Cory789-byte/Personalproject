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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

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
def P(t, s=BODY): return Paragraph(t, s)

R_TAYLOR = "Respondent's disclosure from witness conferencing (C Taylor)"
R_REESE  = "Respondent's disclosure from witness conferencing (T Reese)"
R_FRMS   = "Respondent's disclosure from witnesses (fatigue risk management content)"
CE       = "Letter of Metro South Health, 5 June 2026 (ref K-LM26/729)"

FACTS = [
 ("A", "THE EMPLOYMENT, AND THE HOURS THE APPELLANT SOUGHT"),
 (1, "The Appellant has been employed by Metro South Hospital and Health Service since 2019.",
     "Appellant's amended statement of facts and contentions"),
 (2, "On 7 August 2023 at 12:21 pm the Appellant sent an email to Ms Chloe Taylor, Ms Tammy Reese, "
     "Ms Patricia Conaghan and Ms Tracey Smith, marked of High importance, which states: "
     "\"Furthermore, to meet the demands and the additional hours of the department both Patricia "
     "Conaghan and I would like to formally adhoc an additional 2 shifts per fortnight.\"", R_REESE),
 (3, "That email sets out clause 11.7 of the applicable agreement, headed \"Additional Permanent "
     "Hours for Part-time Employees\".", R_REESE),
 (4, "On 8 August 2023 at 6:06 pm the Appellant sent an email to Ms Reese which states: \"I can "
     "confirm that I will be in tomorrow 0700-1500 9th August. I was also looking to pick up "
     "another shift if possible.\"", R_REESE),
 (5, "On 8 August 2023 at 4:15 pm Ms Reese sent an email to the Appellant which states: \"can I ask "
     "were you looking for another shift on top of those 8 to replace the shift missed today "
     "also?\"", R_REESE),
 (6, "On 31 August 2023 the Appellant provided to Ms Taylor a written application headed \"Request "
     "to Increase Working Hours to Full Time Rotational Roster\".", R_REESE),
 (7, "That application states: \"I have also expressed my willingness to take on additional night "
     "shifts as part of the roster.\"", R_REESE),
 (8, "On 4 September 2023 the Appellant sent an email to Ms Reese which states: \"I confirm that I "
     "am able and willing to work any roster that is presented to me, including the current "
     "schedule with full 24-hour availability.\"", R_REESE),
 (9, "That email states: \"I have no issues with shift work.\"", R_REESE),
 (10, "That email attached a draft roster spreadsheet prepared by the Appellant.", R_REESE),
 (11, "On 8 September 2023 at 11:42 am Ms Reese sent an email to the Appellant which states: \"I am "
      "glad to hear things seem to be going well with Chloe and I am also glad to hear you applied "
      "for the additional shifts through the recent EOI.\"", R_REESE),
 (12, "On 27 September 2023 at 1:52 pm Ms Taylor sent an email to the Appellant with the subject "
      "\"Approved - Permanent Full Time FTE\" which states: \"Just giving you an update on your "
      "application for Permanent Fulltime hours, I am very pleased to advise you that this has been "
      "approved.\"", "Email of Ms C Taylor, 27 September 2023"),
 (13, "That email states: \"happy to commence Full-time hours from the 16th October 2023\".",
      "As above"),
 ("B", "THE MATTERS RAISED IN AUGUST AND SEPTEMBER 2023, AND THE RESPONSE TO THEM"),
 (14, "The Appellant's email of 7 August 2023 at 12:21 pm states: \"Please give me some space and "
      "stop with any further communication as I have had enough of it.\"", R_REESE),
 (15, "On 7 August 2023 at 1:43 pm Ms Taylor replied to the Appellant, copied to Ms Reese and "
      "Ms Smith, stating: \"My sincere apologises about your rostered Monday 7th 0700-1500 shift, I "
      "can confirm this was an oversight.\"", R_REESE),
 (16, "That email of Ms Taylor states: \"Would you like me to roster you off tomorrow Tuesday 8th "
      "0700-1500 to give you the required rest period\".", R_REESE),
 (17, "On 7 August 2023 at 3:13 pm Ms Reese replied to the Appellant stating: \"As Chloe is your "
      "current line manager and as such you are required to continue to communicate with Chloe for "
      "work related issues, shift concerns, leave, etc.\"", R_REESE),
 (18, "On 7 August 2023 at 5:11 pm Ms Reese sent an email to Ms Taylor attaching a document titled "
      "\"Rostered shifts Cory S. past 8 months.xlsx\", which states: \"can I ask if you can send me "
      "an email of your recent communication with Cory about contacting yourself about missed "
      "shifts, as I could not find a copy of this email.\"", R_REESE),
 (19, "On 29 August 2023 at 6:57 pm Ms Reese sent the Appellant an email attaching HR Policy E12 - "
      "Individual Employee Grievances, and setting out how a grievance could be submitted.", R_REESE),
 (20, "On 4 September 2023 the Appellant replied to Ms Reese stating: \"I have also spoken to "
      "Chloe. We are seemingly on the path to working in a beneficial way and hopefully will not "
      "need to go through this process.\"", R_REESE),
 (21, "The Appellant did not submit a grievance under HR Policy E12 in 2023.", R_REESE),
 ("C", "THE PROCESS FOR NOTIFYING UNAVAILABILITY FOR A ROSTERED SHIFT"),
 (22, "On 15 April 2024 at 12:39 pm Ms Taylor sent an email to Logan Switch, copied to Ms Reese and "
      "to Switchboard staff including the Appellant, with the subject \"Afterhours Oncall Process - "
      "Switchboard\".",
      "Appellant's email to WorkCover Queensland, 29 August 2024, enclosing the email"),
 (23, "That email states: \"Process during office hours remains the same, please contact myself "
      "through switch/office or mobile unless otherwise advised.\"", "As above"),
 (24, "That email states: \"This new process is effective from today.\"", "As above"),
 (25, "That email states: \"You will see that Ellen and myself have added Afterhours on call, the "
      "days that are highlighted in purple show who is on call after hours.\"", "As above"),
 (26, "Ms Taylor signed that email as \"A/Switchboard Manager\".", "As above"),
 (27, "On 14 May 2024 at 12:08 pm Ms Taylor sent an email to the Appellant, copied to Ms Reese, "
      "with the subject \"Sick leave 14.05.24\", which states: \"in business hours you are to "
      "follow the correct process and speak to me directly if its regarding emergent leave, you can "
      "contact me either through switch or my office/mobile.\"", R_TAYLOR),
 (28, "On 17 May 2024 at 9:30 am Ms Taylor sent an email to Logan Switch and Switchboard staff, "
      "copied to Ms Reese, which states: \"regardless of my start/finish times next week you are to "
      "please contact me through the day/afterhours either via switch, office or mobile.\"", R_TAYLOR),
 (29, "On 17 May 2024 at 1:20 pm Ms Taylor sent an email to Ms Adriana McNamee with the subject "
      "\"FW: Office Hours and Departmental Directives\", which states: \"when staff call in for any "
      "leave to please contact me either via switch, office or my mobile.\"", R_TAYLOR),
 (30, "On 13, 14 and 15 May 2024 the Appellant notified his unavailability for his rostered shift "
      "by telephoning the Switchboard.",
      "Ms Taylor's email to Ms McNamee, 17 May 2024, which records each of those three calls"),
 (31, "The document entitled \"Logan Hospital Switchboard Sick Leave Process\", version 1.1, is "
      "dated 4 February 2025.",
      "Attachment to the letter of Mr Scott Hughes dated 8 September 2025, page 1"),
 ("D", "ROSTER CONCERNS AND THE EMPLOYER'S KNOWLEDGE OF FATIGUE BEFORE 18 JUNE 2024"),
 (32, "On 26 April 2024 at 1:52 pm Ms Reese sent an email to the Appellant with the subject "
      "\"Roster Concerns\", referring to a meeting on 16 April 2024 at which the Appellant raised a "
      "roster line ending with night shifts followed by three days off and then returning to night "
      "shifts.", R_REESE),
 (33, "That email states that Ms Taylor \"was working to fix this error and would get in touch with "
      "you about what alternative shifts she could offer\".", R_REESE),
 (34, "On 1 May 2024 at 1:18 pm the Appellant sent an email to Ms Reese with the subject \"Roster "
      "Concerns\" referring to section 4, clause 10.4.1 of the Operations Manual and stating: "
      "\"This section includes a toolkit required by management to manage fatigue and implement "
      "appropriate protocols and adhere to the workplace health and safety act.\"", R_REESE),
 (35, "That email states: \"I forwarded the toolkit to Chloe last week for review and action but "
      "have yet to receive feedback\".", R_REESE),
 (36, "On 8 May 2024 at 9:08 am Ms Reese replied to the Appellant stating: \"Thanks for raising "
      "these observations and concerns. I am following up with regards to these with HR for further "
      "advice and I will get back to you asap with a response.\"", R_REESE),
 (37, "On 10 May 2024 at 2:08 pm Ms Reese sent an email to Mr Mackenzie Pritchard of Human "
      "Resources forwarding the Appellant's email of 1 May 2024, which states: \"I think he is "
      "trying to raise that he has concerns over how his manager is rostering for the Switchboard "
      "team and how it is impacting on staff fatigue, or more specifically his fatigue.\"", R_FRMS),
 (38, "That email states: \"as per Cory's second extract detailing the Roster Risk assessment "
      "Matrix, Chloe and I have run thought this and we say at best there would be a rating of 11 "
      "which is moderate\".", R_FRMS),
 (39, "That email states: \"I acknowledge there has been a few rostering errors made by Chloe with "
      "regards to Cory's line in past rosters\".", R_FRMS),
 (40, "That email attached the document \"qh-gdl-401-3.3\", being the Queensland Health Fatigue "
      "Risk Management Systems Implementation Guideline.", R_FRMS),
 (41, "On 20 May 2024 at 4:07 pm Ms Reese sent an email to LBH_HR which states: \"I am just "
      "following up on this query I raised a little while ago in relation to a email I had received "
      "from a staff member about our rostering practices. Thus if someone might be able to give me "
      "a call regarding these staff concerns, that would be great.\"", R_FRMS),
 ("E", "THE EMPLOYER'S OWN STATEMENTS ABOUT ITS SYSTEMS AND RECORDS"),
 (42, "By letter dated 5 June 2026, reference K-LM26/729, signed by Ms Noelle Cridland as Chief "
      "Executive of Metro South Hospital and Health Service and addressed to Commissioner Dwyer, "
      "Metro South Health stated in relation to Item 4: \"the requested documents do not exist. "
      "Mandatory Fatigue Risk Management System training only applies to health practitioners and "
      "clinical assistants. The Logan Hospital Switchboard staff are non-clinical staff, and "
      "therefore there is no mandatory requirement for them to complete Fatigue Risk Management "
      "System training.\"", CE),
 (43, "That letter states in relation to Item 5: \"The implementation of fatigue risk management "
      "assessment at Switchboard Logan Hospital occurred after 30 June 2024 in connection with an "
      "organisational change related to the reporting lines for Switchboard.\"", CE),
 (44, "That letter states in relation to Item 7: \"the requested documents do not exist. Mandatory "
      "Fatigue Risk Management System training only applies to health practitioners and clinical "
      "assistants.\"", CE),
 (45, "That letter states in relation to Item 3(c): \"there have been no 'consequential' changes to "
      "operating procedures over the period requested.\"", CE),
 (46, "That letter states in relation to Item 3(a): \"All employee complaints relating to Logan "
      "Hospital Switchboard operational errors are made directly to the Line Manager of Switch "
      "Board and managed solely via email or verbally with the complainant.\"", CE),
 (47, "That letter states in relation to Items 1 and 2: \"a spreadsheet of recorded MET calls is "
      "available for the period 17-18 March 2024.\"", CE),
]

s = []
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
    if f[0] in ("A", "B", "C", "D", "E"):
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
    if f[0] in ("A", "B", "C", "D", "E"):
        st.append(('BACKGROUND', (0,i), (-1,i), colors.HexColor('#f0f0f0')))
        st.append(('SPAN', (1,i), (3,i)))
t.setStyle(TableStyle(st))
s.append(t)
s.append(Spacer(1, 5*mm))
s.append(P("Cory Lea Shepherd<br/>Appellant (self-represented) &nbsp;|&nbsp; [date]", BODY))

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
print("built out/FORM24_SECOND_NOTICE_DRAFT.pdf - 47 facts")
