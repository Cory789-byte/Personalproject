#!/usr/bin/env python3
"""WC/2024/227 — INSTRUCTION to Dr Krishnaiah, structured on the Form 29's own matters in issue.

Builds drafts/out/INSTRUCTION_Krishnaiah_4DOC_DRAFT.pdf.

Design: the Notice of Non-Party Disclosure served on the practice states the matters in issue in
three numbered lines. Those three lines are the report's spine. The employer's medical questions
are integrated beneath them rather than answered separately. Assumed facts are the other side's
documents only; the appellant's account is clinical context, not the factual basis.

⛔ DRAFT — bracketed items require confirmation before sending.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle)

OUT = "out/INSTRUCTION_Krishnaiah_4DOC_DRAFT.pdf"
ss = getSampleStyleSheet()

H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=13.5, leading=17, spaceAfter=3)
PART = ParagraphStyle('PART', parent=ss['Heading2'], fontName='Helvetica-Bold',
                      fontSize=10.8, leading=14, spaceBefore=12, spaceAfter=5)
ISSUE = ParagraphStyle('ISSUE', parent=ss['Heading2'], fontName='Helvetica-Bold',
                       fontSize=10.2, leading=13.5, spaceBefore=11, spaceAfter=4,
                       textColor=colors.HexColor('#1a1a1a'),
                       borderPadding=3, backColor=colors.HexColor('#f0f0f0'))
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.7, leading=13.5, spaceAfter=6)
Q = ParagraphStyle('Q', parent=BODY, spaceBefore=6, spaceAfter=3, leftIndent=6)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.4, leading=11.4,
                       textColor=colors.HexColor('#555555'))
FLAG = ParagraphStyle('FLAG', parent=BODY, fontSize=8.6, leading=11.8,
                      textColor=colors.HexColor('#8a2010'), leftIndent=6)

def P(t, s=BODY): return Paragraph(t, s)

story = []
story.append(P("Letter of instruction — psychiatric report", H1))
story.append(P("Dr Ravikumar Bangalore Krishnaiah, Consultant Psychiatrist, Mind and Memory Service<br/>"
               "From: Cory Lea Shepherd &nbsp;·&nbsp; WC/2024/227, Queensland Industrial Relations "
               "Commission &nbsp;·&nbsp; [DATE]", SMALL))
story.append(Spacer(1, 3*mm))

# PART A — ATTACHMENTS
story.append(P("PART A — THE ATTACHMENTS", PART))
story.append(P("Four documents accompany this letter. <b>Three were written by the other parties to "
               "my matter.</b>", BODY))
rows = [[P("<b>No.</b>", SMALL), P("<b>Document</b>", SMALL), P("<b>Author</b>", SMALL),
         P("<b>Status</b>", SMALL)],
 [P("<b>1</b>", SMALL),
  P("<b>Response to Notice to Admit Facts</b>, 18 February 2026 — the Regulator's admissions in "
    "this appeal.", SMALL),
  P("The <b>Regulator</b>", SMALL), P("<b>Assumed fact</b>", SMALL)],
 [P("<b>2</b>", SMALL),
  P("<b>Letter of the Chief Executive</b>, Metro South Hospital and Health Service, 5 June 2026 "
    "(ref K-LM26/729), to the Commission.", SMALL),
  P("The <b>employer's<br/>Chief Executive</b>", SMALL), P("<b>Assumed fact</b>", SMALL)],
 [P("<b>3</b>", SMALL),
  P("<b>Role description</b> — Administration Officer, Switchboard Services (AO3), Logan Hospital.",
    SMALL),
  P("The <b>employer</b>", SMALL), P("<b>Assumed fact</b>", SMALL)],
 [P("<b>4</b>", SMALL),
  P("<b>The clinical record</b> — your file for me from 24 October 2024; my general-practice "
    "records (Our Medical Ashmore, produced for 1 January 2023 to 1 July 2024); "
    "the Work Capacity Certificate of Dr Hawes; my certificate of capacity of 3 July 2026.", SMALL),
  P("<b>Clinicians</b>", SMALL), P("<b>Clinical record</b>", SMALL)]]
t = Table(rows, colWidths=[11*mm, 92*mm, 33*mm, 30*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
story.append(t)

# PART B — BASIS
story.append(P("PART B — THE BASIS ON WHICH I ASK YOU TO WRITE", PART))
story.append(P("I ask you to assume, for the purpose of your opinion, <b>the facts recorded in "
               "Attachments 1 to 3</b>. Attachment 1 records facts admitted by the respondent in the "
               "proceeding; Attachments 2 and 3 are the employer's own documents.", BODY))
story.append(P("<b>My own account of the workplace is provided as clinical context only, and is not "
               "the basis on which I ask you to reason.</b> Where your history from me differs from "
               "any fact in Attachments 1 to 3, please say so expressly rather than resolve the "
               "difference. Attachment 4 is the clinical record, for your clinical review.", BODY))
story.append(P("Please do not adopt, or treat as established, any conclusion, characterisation or "
               "finding of any other decision-maker. <b>Your opinion is yours alone.</b> I do not ask "
               "you to express any view on whether any management action was reasonable; that is a "
               "question for the Commission.", BODY))

story.append(P("<b>Dates.</b> So that the sequence is available to you from a source other than my "
               "own account, the following dates are taken from the Regulator's amended List of "
               "Documents dated 14 August 2026, by its item number.", BODY))
drows = [[P("<b>Item</b>", SMALL), P("<b>Date</b>", SMALL), P("<b>Document</b>", SMALL)],
 [P("46", SMALL), P("1 July 2024", SMALL), P("Text, WorkCover to me, noting the claim registered", SMALL)],
 [P("7", SMALL), P("1 July 2024<br/>11 August 2024<br/>8 September 2024", SMALL),
  P("Workers' compensation medical certificate — Dr Peter Hawes", SMALL)],
 [P("8", SMALL), P("7 August 2024", SMALL),
  P("Workers' compensation medical certificate — Dr Ki Pang", SMALL)],
 [P("2", SMALL), P("13 September 2024", SMALL), P("WorkCover Queensland reasons for decision", SMALL)],
 [P("3", SMALL), P("16 September 2024", SMALL), P("Application for review", SMALL)],
 [P("<b>9</b>", SMALL), P("<b>24 October 2024</b>", SMALL),
  P("<b>Email, Dr Krishnaiah — noting injury and medication</b>", SMALL)],
 [P("4", SMALL), P("24 October 2024", SMALL), P("Review Unit reasons for decision", SMALL)],
 [P("5", SMALL), P("26 November 2024", SMALL), P("Notice of Appeal", SMALL)],
 [P("10", SMALL), P("13 February 2025", SMALL), P("Report of Mind and Memory Service", SMALL)],
 [P("11", SMALL), P("Various", SMALL), P("Practice records — Our Medical Ashmore", SMALL)]]
dt = Table(drows, colWidths=[13*mm, 34*mm, 119*mm], repeatRows=1)
dt.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
story.append(dt)
story.append(P("A copy of the Notice of Non-Party Disclosure served on your practice accompanies "
               "this letter.", SMALL))
story.append(P("<b>The clinical records provided are the complete records held by the respondent in "
               "this proceeding.</b> They are provided in full and unedited, including entries that "
               "are unrelated to this matter and entries that may not assist me. I have not selected "
               "among them. <b>If any further records would assist you, please say so and I will "
               "obtain them.</b>", BODY))

story.append(P("PART B2 — WHAT IS ALREADY RECORDED, AND WHAT I AM NOT ASKING YOU TO ESTABLISH", PART))
story.append(P("Attachments 1 to 3 already record the nature of the work, what occurred, and what "
               "the employer says was and was not in place. <b>You are not asked to find any of "
               "that, and you are not asked to take any of it from me.</b>", BODY))
story.append(P("<b>Already recorded, by the Respondent or by my employer:</b> the requirements of "
               "the position · that the accuracy of Switchboard information is critical to clinical "
               "handover and patient safety · the applicable minimum break between shifts · the "
               "break in fact rostered on 17 to 18 March 2024 and its description as an error · that "
               "emergency (MET) calls were recorded on those shifts · that leave was taken on "
               "19 March 2024 · that no fatigue risk assessment applied to the position and that "
               "fatigue risk management was implemented only after 30 June 2024 · that no "
               "consequential changes to operating procedures followed · and that the "
               "general-practice entry of 16 November 2023 appears in the records, its accuracy "
               "not being admitted. ⭐ The certificate of capacity of 3 July 2026 also "
               "records the arrangement then in place as a <i>“continuation of existing "
               "arrangement … worked and tolerated … without deterioration.”</i>", BODY))
story.append(P("⭐ <b>What remains, and what I do ask you, is the clinical question: whether "
               "exposure of that kind bears on the condition you have diagnosed.</b>", BODY))

# PART C — THE THREE MATTERS
story.append(P("PART C — THE MATTERS IN ISSUE", PART))
story.append(P("You have been served with a Notice of Non-Party Disclosure in this proceeding. That "
               "notice states the matters in issue as follows:", BODY))
story.append(P("<i>“1. Did Mr Shepherd sustain a personal injury<br/>"
               "2. Did the personal injury arise out of or in the course of Mr Shepherd's "
               "employment<br/>"
               "3. Was Mr Shepherd's employment a significant contributing factor to the injury”</i>",
               ParagraphStyle('quote', parent=BODY, leftIndent=14, rightIndent=10,
                              fontSize=9.4, leading=13, textColor=colors.HexColor('#222222'))))
story.append(P("I ask you to address those three matters, in that order. My employer has separately "
               "asked for medical information about my capacity for work; <b>those matters are taken "
               "up within question 3 below</b>, so that one report answers both.", BODY))

story.append(P("MATTER 1 — DID MR SHEPHERD SUSTAIN A PERSONAL INJURY?", ISSUE))
story.append(P("<b>1.1</b> The diagnosis; the classificatory framework applied and the code; the "
               "specific diagnostic criteria met and when each was met; and the date of onset as "
               "best the clinical record establishes it.", Q))
story.append(P("<b>1.2</b> The differential diagnoses considered, and your reasons for including or "
               "excluding each.", Q))
story.append(P("<b>1.3</b> My psychiatric background. The general-practice records provided include "
               "<b>the entry of 16 November 2023</b>, and any earlier entries referring to anxiety, "
               "attention deficit features or stimulant prescribing. Please address them. Whether "
               "there was any relevant pre-existing condition; and if so, whether the matters at "
               "Attachments 1 to 3 aggravated it, and to what extent.", Q))
story.append(P("<b>1.4</b> Whether any premorbid personality features bear on the diagnosis, and if "
               "so how — from your own current clinical assessment. I do not ask you to adopt or "
               "repeat any earlier characterisation.", Q))
story.append(P("<b>1.5</b> A complete list of every document you reviewed and every person you saw, "
               "with the dates and duration of each examination.", Q))

story.append(P("MATTER 2 — DID THE INJURY ARISE OUT OF, OR IN THE COURSE OF, THE EMPLOYMENT?", ISSUE))
story.append(P("<b>2.1 The conditions of the work, and fatigue.</b> Attachment 3 records that the position "
               "requires continuous shift work across the full 24-hour period, seven days a week; "
               "participation in the Emergency Response process, distributing emergency notifications "
               "in accordance with code procedures and strictly adhering to protocols and timeframes; "
               "maintaining call queues to a minimum at all times; multitasking and operating under "
               "pressure with high volume call traffic; exercising judgement where precedent has not "
               "been set and procedures are not defined; and working with limited supervision. "
               "Attachment 1 records that the accuracy of Switchboard information is critical to "
               "clinical handover and patient safety.<br/>"
               "<b>From a clinical perspective, whether and how conditions of that kind — the level "
               "of demand, the degree of control, and the adequacy of support — can contribute to a "
               "condition of the kind you have diagnosed.</b>", Q))
story.append(P("<b>2.2 The rostering of 17 to 18 March 2024.</b> Attachment 1 records a rostered "
               "break of 7 hours against a 10-hour minimum, described as a rostering error "
               "accidentally made. Attachment 2 records that emergency (MET) calls were recorded on "
               "those shifts, and that leave was taken on 19 March 2024. What clinical significance, "
               "if any, do you attach to that sequence?", Q))

story.append(PageBreak())

story.append(P("MATTER 3 — WAS THE EMPLOYMENT A SIGNIFICANT CONTRIBUTING FACTOR?", ISSUE))
story.append(P("<b>3.1 Causation.</b> On the assumed facts, whether my employment was "
               "<b>a significant contributing factor</b> to the injury with onset on 18 June 2024. "
               "Please give your clinical reasoning, and distinguish between the cause of onset and "
               "any factors bearing only on the subsequent course.", Q))
story.append(P("<b>3.2 The interval.</b> The rostering matters at 2.3 occurred in March 2024 and "
               "onset is pleaded at 18 June 2024. Is that interval consistent with, or inconsistent "
               "with, your formulation — and if consistent, by what mechanism? Separately, what "
               "significance, if any, attaches to the interval between onset and first presentation, "
               "the Work Capacity Certificate recording first attendance for this injury on "
               "1 July 2024?", Q))
story.append(P("<b>3.3 Other factors, placed in time.</b> Please identify any non-employment factors "
               "relevant to (a) onset at or about 18 June 2024 and (b) the subsequent course. Your "
               "report of 13 February 2025 referred to multiple life stressors including relationship "
               "breakdown, job loss and bereavement.", Q))
story.append(P("<b>Your clinical relationship with me began on 24 October 2024, and my partner "
               "attended that consultation with me.</b> Each of the matters above arose while I was "
               "under your care and is recorded in your own file. I ask you:", BODY))
story.append(P("<b>(a)</b> to place each factor in time <b>from your own records rather than by "
               "assumption</b>;", Q))
story.append(P("<b>(b)</b> to state whether, <b>as at the date of your diagnosis</b>, my relationship "
               "was a protective factor or an adverse one; and", Q))
story.append(P("<b>(c)</b> for each factor, whether in your opinion it was <b>independent of the "
               "employment matters, or a consequence of them</b> — noting that your report of "
               "13 February 2025 records that my pay was <i>“withheld or delayed for up to five "
               "months at a time, leading to significant financial stress and strain on his "
               "relationship”</i>.", Q))

story.append(P("<b>Capacity, restrictions and adjustments</b> — the matters my employer has asked "
               "about. My certificate of capacity of 3 July 2026 certifies me fit for my substantive "
               "role with adjustments; I ask only that your opinion be your own.",
               ParagraphStyle('sub2', parent=BODY, fontName='Helvetica-Bold', spaceBefore=8)))
story.append(P("<b>3.4 Prognosis and current capacity.</b> Your prognosis; and, distinguishing "
               "(a) my capacity to perform the substantive role <b>with reasonable adjustments</b> "
               "from (b) any current incapacity. If there is current incapacity, its cause — the "
               "condition itself, the consequences of my exclusion from the workplace since "
               "3 July 2026, or other factors.", Q))
story.append(P("<b>3.5 The adjustments, in functional terms.</b> The adjustments you consider "
               "clinically necessary, the clinical basis for each, and the anticipated duration and "
               "review date — addressing, among anything else you consider relevant: predictability "
               "of rostering; adequate recovery between shifts; sustained concurrent emergency-code "
               "load; hours of work; and reporting arrangements.<br/>"
               "Please also address, in functional terms: (a) any tasks, situations or environments "
               "likely to exacerbate the condition; (b) if you consider a restriction on complaint "
               "handling clinically necessary, what activities it encompasses — receiving, "
               "documenting, redirecting or resolving complaints, or all complaint-related "
               "interaction; and (c) your report of 13 February 2025 records that my working memory "
               "is affected under stress — what that means for performance of the duties at "
               "Attachment 3, and the circumstances likely to give rise to it.", Q))
story.append(P("<b>3.6 The requirements of the position.</b> Attachment 3 describes the duties "
               "of the position and states that it is a continuous shift working role. Please "
               "address, in order:", Q))
story.append(P("<b>(a)</b> whether the adjustments at 3.5 are <b>clinically necessary at "
               "present</b> — that is, whether I am presently able to perform the duties "
               "without them;", Q))
story.append(P("<b>(b)</b> whether, <b>with those adjustments in place</b>, I am able to "
               "perform the duties described at Attachment 3;", Q))
story.append(P("<b>(c)</b> whether adjustments of that kind — predictability of rostering, "
               "minimum recovery intervals between shifts, limits on sustained concurrent "
               "emergency-code load, and hours of work — are <b>of a kind ordinarily provided "
               "by large employers, and in particular by health services operating 24-hour "
               "services</b>; and", Q))
story.append(P("<b>(d)</b> whether the adjustments are <b>permanent, or temporary with a "
               "review date</b>.", Q))
story.append(P("I note that the certificate of capacity of 3 July 2026 at Attachment 4 records "
               "the arrangement then in place as a <i>“continuation of existing arrangement … "
               "worked and tolerated … without deterioration.”</i> Please take that record into "
               "account in answering (b) and (c).", BODY))
story.append(P("<b>3.7 Foreseeable risk.</b> Whether exposure to the conditions at Attachments 2 "
               "and 3, without the adjustments at 3.5, presents a foreseeable risk to my health or "
               "safety; and if so, what controls you consider medically necessary to manage it.", Q))

# PART D
story.append(P("PART D — WHAT I DO NOT ASK, AND THE FORM OF THE REPORT", PART))
story.append(P("I do not ask you to express a view on whether my employer is able to accommodate the "
               "adjustments you recommend, or on my capacity to work under any particular reporting "
               "line or with any particular person. Those are workplace questions, not medical ones. "
               "If you are asked either question, I ask that you say so.", BODY))
story.append(P("Please reason from the assumed facts to your conclusions rather than assert "
               "conclusions, and state where the material is insufficient for you to express an "
               "opinion rather than qualifying an opinion you would not otherwise give.", BODY))
story.append(P("<b>Please state expressly the material on which your opinion as to causation rests, "
               "and whether that opinion depends on my account of the workplace matters.</b>", BODY))
story.append(P("<b>Please also state whether anything in the clinical records provided is "
               "inconsistent with, or qualifies, the opinions you express — and if so, how you have "
               "taken it into account.</b> I ask this so that the report addresses the whole of the "
               "material rather than part of it.", BODY))
story.append(P("The report is prepared for use in proceedings in the Queensland Industrial Relations "
               "Commission and may be provided to my employer.", BODY))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — Letter of instruction",
                        author="Cory Lea Shepherd")

def footer(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm, "WC/2024/227 · Shepherd · Letter of instruction to Dr R B Krishnaiah")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("built", OUT)
