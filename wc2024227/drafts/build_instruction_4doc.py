#!/usr/bin/env python3
"""WC/2024/227 — REVISED INSTRUCTION to Dr Krishnaiah. Four-document spine, single report.

Builds drafts/out/INSTRUCTION_Krishnaiah_4DOC_DRAFT.pdf.
Attachments at the head. Assumed facts = the other side's documents only.
One report: causation (the appeal) and capacity (the RFMI) in one breath.
⛔ DRAFT — three bracketed items require Cory's confirmation before sending.
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
                      fontSize=11, leading=14, spaceBefore=12, spaceAfter=5,
                      textColor=colors.HexColor('#111111'))
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.7, leading=13.6, spaceAfter=6)
Q = ParagraphStyle('Q', parent=BODY, spaceBefore=7, spaceAfter=3)
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
story.append(P("⛔ <b>DRAFT.</b> Three bracketed items require confirmation before sending.", FLAG))
story.append(Spacer(1, 4*mm))

# ── PART A — ATTACHMENTS AT THE HEAD
story.append(P("PART A — THE ATTACHMENTS", PART))
story.append(P("Four documents accompany this letter. <b>Three of them were written by the other "
               "parties to my matter.</b> That is deliberate, and it is the point of Part B.", BODY))

rows = [[P("<b>No.</b>", SMALL), P("<b>Document</b>", SMALL), P("<b>Author</b>", SMALL),
         P("<b>Status</b>", SMALL)],
 [P("<b>1</b>", SMALL),
  P("<b>Response to Notice to Admit Facts</b>, 18 February 2026 — the Workers' Compensation "
    "Regulator's admissions in this appeal.", SMALL),
  P("The <b>Regulator</b><br/>(the respondent)", SMALL), P("<b>Assumed fact</b>", SMALL)],
 [P("<b>2</b>", SMALL),
  P("<b>Letter of the Chief Executive, Metro South Hospital and Health Service</b>, 5 June 2026 "
    "(ref K-LM26/729), to the Commission.", SMALL),
  P("The <b>employer's<br/>Chief Executive</b>", SMALL), P("<b>Assumed fact</b>", SMALL)],
 [P("<b>3</b>", SMALL),
  P("<b>Role description — Administration Officer, Switchboard Services (AO3)</b>, Logan Hospital.",
    SMALL),
  P("The <b>employer</b>", SMALL), P("<b>Assumed fact</b>", SMALL)],
 [P("<b>4</b>", SMALL),
  P("<b>The clinical record</b> — your own file for me from 24 October 2024; my general-practice "
    "records (Our Medical Ashmore), including the entries of 26 October 2022 and 16 November 2023; "
    "the Work Capacity Certificate of Dr Hawes; and my certificate of capacity of 3 July 2026.",
    SMALL),
  P("<b>Clinicians</b>", SMALL), P("<b>Clinical record</b>", SMALL)],
]
t = Table(rows, colWidths=[11*mm, 92*mm, 33*mm, 30*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(t)

# ── PART B — THE BASIS
story.append(P("PART B — THE BASIS ON WHICH I ASK YOU TO WRITE", PART))
story.append(P("I ask you to assume, for the purpose of your opinion, <b>only</b> the facts recorded "
               "in Attachments 1 to 3. I do not ask you to assume anything on my account of the "
               "workplace.", BODY))
story.append(P("Attachment 1 records facts admitted by the respondent in the proceeding. Attachments "
               "2 and 3 are the employer's own documents. Where your own history from me differs "
               "from any of those facts, <b>please say so expressly</b> rather than resolve the "
               "difference. Attachment 4 is the clinical record, provided for your clinical review "
               "and not as facts about the workplace.", BODY))
story.append(P("Please do not adopt, or treat as established, any conclusion, characterisation or "
               "finding of any other decision-maker. <b>Your opinion is yours alone.</b> The legal "
               "questions in the appeal are not asked of you, and I do not ask you to express any "
               "view on whether any management action was reasonable — that is a question for the "
               "Commission.", BODY))
story.append(P("<b>What the appeal is about, in two sentences.</b> I appeal the rejection of a "
               "claim for a psychological injury with onset on 18 June 2024. The matters in issue "
               "concern rostering and fatigue, remuneration, and the handling of concerns I raised; "
               "it is <b>not</b> a case of bullying or harassment, and I ask that the report describe "
               "the matter accordingly.", BODY))

# ── PART C — CAUSATION
story.append(P("PART C — DIAGNOSIS, CAUSATION AND MECHANISM", PART))
story.append(P("<b>1. Diagnosis, criteria and onset.</b> The diagnosis; the classificatory framework "
               "applied and the code; the specific diagnostic criteria met and when each was met; and "
               "the date of onset as best the clinical record establishes it.", Q))
story.append(P("<b>2. Differential diagnoses.</b> Those considered, and your reasons for including or "
               "excluding each.", Q))
story.append(P("<b>3. Psychiatric background.</b> Please address the entries of 26 October 2022 "
               "referring to anxiety and ADHD, any earlier stimulant use, and the entry of "
               "16 November 2023. Whether there was any relevant pre-existing condition; and if so, "
               "whether the matters at Attachments 1 to 3 aggravated it, and to what extent.", Q))
story.append(P("<b>4. Sources.</b> A complete list of every document you reviewed and every person "
               "you saw, with the dates and duration of each examination.", Q))
story.append(P("<b>5. The exposure.</b> Attachment 3 records that the position requires continuous "
               "shift work across the full 24-hour period, seven days a week; participation in the "
               "Emergency Response process, distributing emergency notifications in accordance with "
               "code procedures and strictly adhering to protocols and timeframes; maintaining call "
               "queues to a minimum at all times; multitasking and operating under pressure with high "
               "volume call traffic; exercising judgement where precedent has not been set and "
               "procedures are not defined; and working with limited supervision. Attachment 1 "
               "records that the accuracy of Switchboard information is critical to clinical handover "
               "and patient safety. Attachment 2 records that no fatigue risk assessment applied to "
               "the position, that fatigue risk management was implemented at the Switchboard only "
               "after 30 June 2024, that complaints were managed solely by email or verbally, and "
               "that no consequential changes to operating procedures were made over the period.<br/>"
               "<b>From a clinical perspective, whether and how conditions of that kind — the level of "
               "demand, the degree of control, the adequacy of support, and fatigue arising from the "
               "rostering — can contribute to a condition of the kind you have diagnosed.</b>", Q))
story.append(P("<b>6. The rostering of 17 to 18 March 2024.</b> Attachment 1 records a rostered break "
               "of 7 hours against a 10-hour minimum, described as a rostering error accidentally "
               "made. Attachment 2 records that emergency (MET) calls were in fact recorded on those "
               "shifts, and that leave was taken on 19 March 2024. Please state what clinical "
               "significance, if any, you attach to that sequence.", Q))
story.append(P("<b>7. Causation.</b> On the assumed facts, whether my employment was "
               "<b>a significant contributing factor</b> to the injury with onset on 18 June 2024. "
               "Please give your clinical reasoning, and please distinguish between the cause of "
               "onset and any factors bearing only on the subsequent course of the condition.", Q))
story.append(P("<b>8. The interval.</b> The rostering matters at question 6 occurred in March 2024 "
               "and onset is pleaded at 18 June 2024. From a clinical perspective, is that interval "
               "consistent with, or inconsistent with, your formulation — and if consistent, by what "
               "mechanism? Separately, what significance, if any, do you attach to the interval "
               "between onset and first presentation, the Work Capacity Certificate recording first "
               "attendance for this injury on 1 July 2024?", Q))

# ── PART C2 — competing causes
story.append(P("<b>9. Competing causes, placed in time.</b> Please identify any non-employment "
               "factors relevant to (a) onset at or about 18 June 2024, and (b) the subsequent "
               "course. Your report of 13 February 2025 referred to multiple life stressors including "
               "relationship breakdown, job loss and bereavement.", Q))
story.append(P("<b>Your clinical relationship with me began on 24 October 2024.</b> Each of those "
               "matters therefore arose while I was under your care and is recorded in your own file. "
               "I ask you to place each factor in time <b>from your own records rather than by "
               "assumption</b>, and to state, for each, its significance to (a) the cause of onset "
               "and (b) the subsequent course.", BODY))
story.append(P("[CONFIRM: the events of 24 October 2024 and what, precisely, is to be said about "
               "support from that date — Cory to settle before sending.]", FLAG))
story.append(P("<b>10. Premorbid personality.</b> Whether any premorbid personality features bear on "
               "the diagnosis and on causation, and if so how — from your own current clinical "
               "assessment. I do not ask you to adopt or repeat any earlier characterisation.", Q))

story.append(PageBreak())

# ── PART D — CAPACITY / RFMI
story.append(P("PART D — CURRENT CAPACITY, RESTRICTIONS AND ADJUSTMENTS", PART))
story.append(P("My employer has asked me for medical information about my capacity. I ask you to "
               "address the following so that this report answers those matters as well. My "
               "certificate of capacity of 3 July 2026 certifies me fit for my substantive role with "
               "adjustments; I ask only that your opinion be your own.", BODY))
story.append(P("<b>11. Prognosis and current capacity.</b> Your prognosis; and, distinguishing "
               "(a) my capacity to perform the substantive role <b>with reasonable adjustments</b> "
               "from (b) any current incapacity. If there is current incapacity, its cause — the "
               "condition itself, the consequences of my exclusion from the workplace since "
               "3 July 2026, or other factors.", Q))
story.append(P("<b>12. The adjustments, in functional terms.</b> Please specify the adjustments you "
               "consider clinically necessary, the clinical basis for each, and the anticipated "
               "duration and review date. Please address, among anything else you consider relevant: "
               "predictability of rostering; adequate recovery between shifts; sustained concurrent "
               "emergency-code load; hours of work; and reporting arrangements.", Q))
story.append(P("<b>13. Inherent requirements.</b> Whether, <b>with the adjustments at question 12</b>, "
               "I am able to fulfil the requirements of the position described at Attachment 3; and "
               "whether those adjustments are ordinary and available in a workplace of that kind.", Q))
story.append(P("<b>14. Exacerbating conditions.</b> Whether there are specific tasks, situations or "
               "environments that may exacerbate the condition or its symptoms.", Q))
story.append(P("<b>15. Complaint handling.</b> If you consider a restriction on complaint handling "
               "clinically necessary, please state what activities it encompasses in functional "
               "terms — receiving, documenting, redirecting or resolving complaints, or all "
               "complaint-related interaction.", Q))
story.append(P("<b>16. Working memory.</b> Your report of 13 February 2025 records that my working "
               "memory is affected under stress. Please clarify what that means in functional terms "
               "in a workplace, including how it may affect performance of the duties at Attachment 3 "
               "and the circumstances likely to give rise to the difficulty.", Q))
story.append(P("<b>17. Foreseeable risk.</b> Whether exposure to the conditions described at "
               "Attachments 2 and 3, without the adjustments at question 12, presents a foreseeable "
               "risk to my health or safety; and if so, what controls you consider medically "
               "necessary to manage it.", Q))
story.append(P("<b>18. Questions I do not ask of you.</b> I do not ask you to express a view on "
               "whether my employer is able to accommodate the adjustments you recommend, or on my "
               "capacity to work under any particular reporting line or with any particular person. "
               "Those are workplace questions, not medical ones. If you are asked either question, "
               "I ask that you say so.", Q))

# ── PART E — FORM
story.append(P("PART E — THE FORM OF THE REPORT", PART))
story.append(P("Please reason from the assumed facts to your conclusions rather than assert "
               "conclusions. Please state where the material is insufficient for you to express an "
               "opinion, rather than qualifying an opinion you would not otherwise give.", BODY))
story.append(P("<b>Please state expressly the material on which your opinion as to causation rests, "
               "and whether that opinion depends on my account of the workplace matters.</b>", BODY))
story.append(P("The report is prepared for use in proceedings in the Queensland Industrial Relations "
               "Commission and may be provided to my employer. [CONFIRM: the standard practice "
               "footer restricting use must not appear on this report.]", BODY))
story.append(P("[CONFIRM: fee, and whether Review Decision 69983 was provided at the consultation of "
               "12 August 2026 — if it was, an express direction not to adopt any finding in it, and "
               "a question whether the opinion would differ if it were disregarded, must be added.]",
               FLAG))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — Letter of instruction (draft)",
                        author="Cory Lea Shepherd")

def footer(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm, "WC/2024/227 · Letter of instruction · DRAFT — not for sending")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("built", OUT)
