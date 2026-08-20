#!/usr/bin/env python3
"""WC/2024/227 - SECOND NOTICE TO ADMIT FACTS (r 49), built 20 August 2026.
Schedule of facts for the approved Form 24. Every item is a fact ABOUT A DOCUMENT the Respondent
holds - not a conclusion, not a characterisation. Metadata stripped.
"""
import pikepdf, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle)

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=12,
                    leading=15.5, spaceAfter=3, alignment=1)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10,
                    leading=13, spaceBefore=10, spaceAfter=4,
                    backColor=colors.HexColor('#eeeeee'), borderPadding=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.3,
                      leading=12.4, spaceAfter=5)
CEN = ParagraphStyle('CEN', parent=BODY, alignment=1)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.2, leading=10.9,
                       textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=8.8, leading=12,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
ITEM = ParagraphStyle('ITEM', parent=BODY, leftIndent=9, spaceBefore=3, spaceAfter=3)
def P(t, s=BODY): return Paragraph(t, s)

# (number, fact, source)
FACTS = [
 ("A", "THE PROCESS FOR NOTIFYING UNAVAILABILITY FOR A ROSTERED SHIFT"),
 (1, "On 15 April 2024 at 12:39 pm Ms Chloe Taylor sent an email to Logan Switch, copied to "
     "Ms Tammy Reese and to Switchboard staff including the Appellant, with the subject "
     "\"Afterhours Oncall Process - Switchboard\".",
     "Appellant's email to WorkCover Queensland, 29 August 2024, enclosing the email"),
 (2, "That email states: \"Process during office hours remains the same, please contact myself "
     "through switch/office or mobile unless otherwise advised.\"", "As above"),
 (3, "That email states: \"This new process is effective from today.\"", "As above"),
 (4, "That email states: \"You will see that Ellen and myself have added Afterhours on call, the "
     "days that are highlighted in purple show who is on call after hours.\"", "As above"),
 (5, "Ms Taylor signed that email as \"A/Switchboard Manager\".", "As above"),
 (6, "On 14 May 2024 at 12:08 pm Ms Taylor sent an email to the Appellant, copied to Ms Reese, "
     "with the subject \"Sick leave 14.05.24\", which states: \"in business hours you are to follow "
     "the correct process and speak to me directly if its regarding emergent leave, you can contact "
     "me either through switch or my office/mobile.\"",
     "Respondent's disclosure from witness conferencing (Chloe Taylor)"),
 (7, "On 17 May 2024 at 1:20 pm Ms Taylor sent an email to Ms Adriana McNamee with the subject "
     "\"FW: Office Hours and Departmental Directives\", which states: \"when staff call in for any "
     "leave to please contact me either via switch, office or my mobile.\"",
     "Respondent's disclosure from witness conferencing (Chloe Taylor)"),
 (8, "On 13, 14 and 15 May 2024 the Appellant notified his unavailability for his rostered shift by "
     "telephoning the Switchboard.",
     "Ms Taylor's email to Ms McNamee of 17 May 2024, which records each of those three calls"),
 (9, "The document entitled \"Logan Hospital Switchboard Sick Leave Process\", version 1.1, is "
     "dated 4 February 2025.",
     "Attachment to the letter of Mr Scott Hughes dated 8 September 2025, page 1"),
 ("B", "THE MATTERS RAISED IN AUGUST 2023 AND THE RESPONSE TO THEM"),
 (10, "On 7 August 2023 at 12:21 pm the Appellant sent an email to Ms Taylor, Ms Reese, "
      "Ms Patricia Conaghan and Ms Tracey Smith, marked of High importance, which states: \"Please "
      "give me some space and stop with any further communication as I have had enough of it.\"",
      "Respondent's disclosure from witness conferencing (Tammy Reese)"),
 (11, "On 7 August 2023 at 1:43 pm Ms Taylor replied to the Appellant, copied to Ms Reese and "
      "Ms Smith, stating: \"My sincere apologises about your rostered Monday 7th 0700-1500 shift, I "
      "can confirm this was an oversight.\"", "As above"),
 (12, "On 7 August 2023 at 3:13 pm Ms Reese replied to the Appellant stating: \"As Chloe is your "
      "current line manager and as such you are required to continue to communicate with Chloe for "
      "work related issues, shift concerns, leave, etc.\"", "As above"),
 (13, "On 7 August 2023 at 5:11 pm Ms Reese sent an email to Ms Taylor attaching a document titled "
      "\"Rostered shifts Cory S. past 8 months.xlsx\", which states: \"can I ask if you can send me "
      "an email of your recent communication with Cory about contacting yourself about missed "
      "shifts, as I could not find a copy of this email.\"", "As above"),
 (14, "On 29 August 2023 Ms Reese sent the Appellant an email attaching HR Policy E12 - Individual "
      "Employee Grievances, and setting out how a grievance could be lodged.", "As above"),
 (15, "On 4 September 2023 the Appellant replied to Ms Reese stating: \"I have also spoken to "
      "Chloe. We are seemingly on the path to working in a beneficial way and hopefully will not "
      "need to go through this process.\"", "As above"),
 (16, "The Appellant did not lodge a grievance under HR Policy E12 in 2023.", "As above"),
 (17, "On 8 September 2023 Ms Reese replied to the Appellant stating: \"I am glad to hear things "
      "seem to be going well with Chloe.\"", "As above"),
 (18, "On 27 September 2023 Ms Taylor advised the Appellant that his application for permanent "
      "full-time hours had been approved.",
      "Email of Ms Chloe Taylor to the Appellant, 27 September 2023"),
 ("C", "THE EMPLOYER'S KNOWLEDGE OF ROSTERING AND FATIGUE BEFORE 18 JUNE 2024"),
 (19, "On 10 May 2024 at 2:08 pm Ms Reese sent an email to Mr Mackenzie Pritchard of Human "
      "Resources, forwarding the Appellant's email of 1 May 2024 entitled \"Roster Concerns\".",
      "Respondent's disclosure from witnesses (fatigue risk management content)"),
 (20, "That email states: \"I think he is trying to raise that he has concerns over how his manager "
      "is rostering for the Switchboard team and how it is impacting on staff fatigue, or more "
      "specifically his fatigue.\"", "As above"),
 (21, "That email states: \"as per Cory's second extract detailing the Roster Risk assessment "
      "Matrix, Chloe and I have run thought this and we say at best there would be a rating of 11 "
      "which is moderate.\"", "As above"),
 (22, "That email states: \"I acknowledge there has been a few rostering errors made by Chloe with "
      "regards to Cory's line in past rosters.\"", "As above"),
 (23, "On 20 May 2024 at 4:07 pm Ms Reese sent an email to LBH_HR stating: \"I am just following up "
      "on this query I raised a little while ago in relation to a email I had received from a staff "
      "member about our rostering practices. Thus if someone might be able to give me a call "
      "regarding these staff concerns, that would be great.\"", "As above"),
 ("D", "THE EMPLOYER'S OWN STATEMENTS ABOUT SYSTEMS AND RECORDS"),
 (24, "By letter dated 5 June 2026, reference K-LM26/729, signed by Ms Noelle Cridland as Chief "
      "Executive of Metro South Hospital and Health Service and addressed to Commissioner Dwyer, "
      "Metro South Health stated in relation to Item 4 of the Notice of non-party disclosure: "
      "\"the requested documents do not exist. Mandatory Fatigue Risk Management System training "
      "only applies to health practitioners and clinical assistants. The Logan Hospital Switchboard "
      "staff are non-clinical staff, and therefore there is no mandatory requirement for them to "
      "complete Fatigue Risk Management System training.\"",
      "Letter of Metro South Health, 5 June 2026, page 2"),
 (25, "That letter states in relation to Item 5: \"The implementation of fatigue risk management "
      "assessment at Switchboard Logan Hospital occurred after 30 June 2024 in connection with an "
      "organisational change related to the reporting lines for Switchboard.\"", "As above"),
 (26, "That letter states in relation to Item 3(c): \"there have been no 'consequential' changes to "
      "operating procedures over the period requested.\"", "As above"),
 (27, "That letter states in relation to Item 3(a): \"All employee complaints relating to Logan "
      "Hospital Switchboard operational errors are made directly to the Line Manager of Switch "
      "Board and managed solely via email or verbally with the complainant.\"", "As above"),
 (28, "That letter states in relation to Items 1 and 2: \"a spreadsheet of recorded MET calls is "
      "available for the period 17-18 March 2024.\"", "As above"),
]

s = []
s.append(P("SCHEDULE OF FACTS - SECOND NOTICE TO ADMIT FACTS", H1))
s.append(P("<i>Industrial Relations (Tribunals) Rules 2011, rule 49</i>", CEN))
s.append(P("WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation "
           "Regulator (Respondent)", CEN))
s.append(P("<b>DRAFT - 20 August 2026.</b> This is the schedule of facts to be inserted in the "
           "approved Form 24 - Notice to admit facts. <b>Verify each quotation against the source "
           "document before service.</b> Delete this box and the \"Source\" column before service - "
           "the source column is for the Appellant's own verification only.", WARN))
s.append(P("TAKE NOTICE that the Appellant proposes to prove the facts specified below, and that if "
           "the Respondent does not, within 14 days after receiving this notice, serve a notice on "
           "the Appellant disputing those facts, the Respondent is taken to admit them for this "
           "proceeding only.", BODY))

rows = [[P("<b>No.</b>", SMALL), P("<b>Fact to be admitted</b>", SMALL),
         P("<b>Admit / Deny</b>", SMALL), P("<b>Source (delete before service)</b>", SMALL)]]
for f in FACTS:
    if f[0] in ("A","B","C","D"):
        rows.append([P(f"<b>{f[0]}</b>", SMALL), P(f"<b>{f[1]}</b>", SMALL), P("", SMALL), P("", SMALL)])
    else:
        rows.append([P(f"<b>{f[0]}</b>", SMALL), P(f[1], SMALL), P("", SMALL), P(f[2], SMALL)])
t = Table(rows, colWidths=[10*mm, 96*mm, 20*mm, 40*mm], repeatRows=1)
st = [('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
      ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')),
      ('VALIGN', (0,0), (-1,-1), 'TOP'),
      ('LEFTPADDING', (0,0), (-1,-1), 3.5), ('RIGHTPADDING', (0,0), (-1,-1), 3.5),
      ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]
for i, f in enumerate(FACTS, start=1):
    if f[0] in ("A","B","C","D"):
        st.append(('BACKGROUND', (0,i), (-1,i), colors.HexColor('#f0f0f0')))
        st.append(('SPAN', (1,i), (3,i)))
t.setStyle(TableStyle(st))
s.append(t)
s.append(Spacer(1, 5*mm))
s.append(P("Cory Lea Shepherd<br/>Appellant (self-represented) &nbsp;|&nbsp; [date]", BODY))

doc = SimpleDocTemplate("out/FORM24_SECOND_NOTICE_DRAFT.pdf", pagesize=A4,
                        leftMargin=15*mm, rightMargin=15*mm, topMargin=14*mm, bottomMargin=14*mm)
def f_(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(15*mm, 8*mm, "DRAFT - SECOND NOTICE TO ADMIT FACTS - VERIFY EVERY QUOTATION BEFORE SERVICE")
    c.setFont('Helvetica', 7); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-15*mm, 8*mm, f"Page {d.page}")
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
print("built out/FORM24_SECOND_NOTICE_DRAFT.pdf")
