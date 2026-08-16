#!/usr/bin/env python3
"""WC/2024/227 — SCHEDULE OF ASSUMED FACTS, for the clinician pack.

Why a schedule and not a highlighted document: marking up the other side's documents is advocacy
inside the evidence. The practice holds a Form 29, so a marked-up copy would be produced to the
Regulator with the appellant's emphasis on her own admissions — and invites the question
"the document you were given had passages marked by Mr Shepherd, didn't it?"

A separate schedule does the same navigational job, is orthodox, and cannot be characterised as
marking evidence. It is also what the letter of instruction has always described as the extract of
admitted facts.

⚠ Lines marked [CONFIRM] have not been read from the rendered source in this session. The Form 24
text layer is incomplete and its numbering drifts after Notice ¶25 — check every one before sending.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=12.5, leading=16, spaceAfter=3)
SEC = ParagraphStyle('SEC', parent=ss['Heading2'], fontName='Helvetica-Bold',
                     fontSize=10.2, leading=13.5, spaceBefore=11, spaceAfter=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.4, leading=13, spaceAfter=5)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))
def P(t, s=BODY): return Paragraph(t, s)
def T(rows, w):
    t = Table(rows, colWidths=w, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
    return t

s = []
s.append(P("Schedule of assumed facts", H1))
s.append(P("WC/2024/227 · Shepherd · accompanying the letter of instruction · [DATE]", SMALL))
s.append(P("This schedule identifies, by source and paragraph, the facts referred to in Part B of the "
           "letter of instruction. <b>The documents themselves accompany it, complete and unmarked.</b> "
           "Where a passage is quoted, the quotation is exact.", BODY))

s.append(P("A · FROM THE RESPONDENT'S RESPONSE TO THE NOTICE TO ADMIT FACTS, 18 FEBRUARY 2026", SEC))
s.append(P("Paragraph numbers are those of the <b>Notice</b>. These are facts admitted by the "
           "respondent in the proceeding.", SMALL))
s.append(T([
 [P("<b>¶</b>", SMALL), P("<b>Admitted fact</b>", SMALL)],
 [P("1", SMALL), P("The break rostered between the shifts of <b>17 and 18 March 2024 was 7 hours</b>. "
   "<font color='#8a2010'>[CONFIRM]</font>", SMALL)],
 [P("3", SMALL), P("The applicable <b>minimum break is 10 hours</b>, or 8 hours by written agreement. "
   "<font color='#8a2010'>[CONFIRM]</font>", SMALL)],
 [P("5", SMALL), P("The rostering was <i>“a rostering error that was accidentally made”</i>. "
   "<font color='#8a2010'>[CONFIRM]</font>", SMALL)],
 [P("8", SMALL), P("The accuracy of Switchboard contact information is <b>critical to clinical "
   "handover and patient safety</b>. <font color='#8a2010'>[CONFIRM]</font>", SMALL)],
 [P("34", SMALL), P("The general-practice entry of <b>16 November 2023</b> states: <i>“No "
   "psychological illness such as depression/ psychosis.”</i>", SMALL)],
 [P("35", SMALL), P("The respondent holds <b>no contemporaneous medical evidence prior to 2024</b> "
   "contradicting that entry.", SMALL)],
 [P("38", SMALL), P("<b>Major Depressive Disorder</b> was diagnosed on <b>13 February 2025</b>.", SMALL)],
 [P("40", SMALL), P("On <b>3 May 2024</b> payroll instructed the line manager to <i>“submit an AVAC "
   "to correct these shifts.”</i>", SMALL)],
 [P("41", SMALL), P("The AVAC was <b>not submitted until 28 May 2024 — a delay of 25 days</b>.", SMALL)],
 [P("46", SMALL), P("On <b>21 May 2024</b> the line manager stated <i>“I am waiting payroll "
   "confirmation… as soon as I do get that confirmation, I will submit an AVAC.”</i>", SMALL)],
 [P("47", SMALL), P("She had held the written payroll instruction <b>since 3 May 2024</b>.", SMALL)],
], [12*mm, 154*mm]))

s.append(P("B · FROM THE LETTER OF THE CHIEF EXECUTIVE, METRO SOUTH HEALTH, 5 JUNE 2026", SEC))
s.append(P("Item numbers are those of the letter. Read from source.", SMALL))
s.append(T([
 [P("<b>Item</b>", SMALL), P("<b>What the letter records</b>", SMALL)],
 [P("1–2", SMALL), P("Pre-upgrade SPOK records were not retained. <b>“However, a spreadsheet of "
   "recorded MET calls is available for the period 17-18 March 2024.”</b>", SMALL)],
 [P("3(a)", SMALL), P("<i>“All employee complaints relating to Logan Hospital Switchboard "
   "operational errors are made directly to the Line Manager of Switch Board and managed <b>solely "
   "via email or verbally</b> with the complainant.”</i>", SMALL)],
 [P("3(c)", SMALL), P("<i>“there have been <b>no ‘consequential’ changes to operating procedures</b> "
   "over the period requested.”</i>", SMALL)],
 [P("4", SMALL), P("The requested fatigue risk assessment records <b>do not exist</b>. <i>“Mandatory "
   "Fatigue Risk Management System training only applies to health practitioners and clinical "
   "assistants. The Logan Hospital Switchboard staff are non-clinical staff…”</i>", SMALL)],
 [P("5", SMALL), P("<i>“The implementation of fatigue risk management assessment at Switchboard "
   "Logan Hospital occurred <b>after 30 June 2024</b> in connection with an organisational change "
   "related to the reporting lines for Switchboard.”</i>", SMALL)],
 [P("7", SMALL), P("The requested fatigue risk management register entries <b>do not exist</b>.", SMALL)],
 [P("15", SMALL), P("Enclosed: <b>leave takings report for the Applicant, 19 March 2024</b>.", SMALL)],
], [14*mm, 152*mm]))

s.append(P("C · FROM THE ROLE DESCRIPTION — ADMINISTRATION OFFICER, SWITCHBOARD SERVICES (AO3)", SEC))
s.append(P("Quoted from the employer's own document. Read from source.", SMALL))
s.append(T([
 [P("<b>Under</b>", SMALL), P("<b>The position requires</b>", SMALL)],
 [P("Purpose", SMALL), P("<i>“The occupant of this position is required to work <b>continuous shift "
   "work over the full 24-hour period, 7 days a week</b>.”</i>", SMALL)],
 [P("Key<br/>responsibilities", SMALL), P("<i>“<b>Participate in the Emergency Response process</b> "
   "by receiving emergency response notifications and distributing them to the appropriate response "
   "groups, dependent on the category of emergency, as per emergency code procedures, <b>strictly "
   "adhering to protocols and timeframes</b>.”</i>", SMALL)],
 [P("", SMALL), P("<i>“<b>Maintain call queues to minimum at all times</b>.”</i> · <i>“The ability to "
   "<b>multitask and operate under pressure</b>, particularly where <b>high volume call traffic</b> "
   "is concerned.”</i>", SMALL)],
 [P("", SMALL), P("<i>“Maintain discretion and <b>exercise judgement</b> where necessary to resolve "
   "problems within the scope of your role; <b>in situations where precedence have not been set and "
   "procedures not defined</b>.”</i>", SMALL)],
 [P("", SMALL), P("<i>“Ability to work effectively as an individual with <b>limited supervision</b>…”</i>",
   SMALL)],
 [P("", SMALL), P("<i>“<b>Collate information and maintain Omnivista database and SharePoint</b> to "
   "ensure information held within Switchboard Services is accurate and appropriate.”</i>", SMALL)],
 [P("Mandatory<br/>requirements", SMALL), P("<i>“The position is a <b>continuous shift working "
   "role</b>. You must be able to work a roster which covers multiple shifts over a 24/7 period.”</i>",
   SMALL)],
], [26*mm, 140*mm]))

s.append(P("D · FROM THE CERTIFICATE OF CAPACITY, 3 JULY 2026", SEC))
s.append(P("The arrangement then in place is recorded as a <i>“continuation of existing arrangement … "
           "<b>worked and tolerated … without deterioration</b>.”</i> <font color='#8a2010'>[CONFIRM "
           "the exact wording against the certificate]</font>", BODY))

doc = SimpleDocTemplate("out/SCHEDULE_OF_ASSUMED_FACTS.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — schedule of assumed facts", author="Cory Lea Shepherd")
def f(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm, "WC/2024/227 · Shepherd · schedule of assumed facts")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
print("built out/SCHEDULE_OF_ASSUMED_FACTS.pdf")
