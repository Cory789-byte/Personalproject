import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, HRFlowable, KeepTogether)

OUT = "/home/user/Personalproject/wc2024227/drafts/out/ANNOTATED_SCHEDULE_MSH-INJ-5795.pdf"
RAW = "/tmp/_sched_raw.pdf"

INK  = colors.HexColor("#111111")
MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#9a9a9a")
BAND = colors.HexColor("#ECECEC")
LITE = colors.HexColor("#F7F7F7")

def P(n, **kw):
    base = dict(fontName="Helvetica", fontSize=9.0, leading=12.4, textColor=INK)
    base.update(kw); return ParagraphStyle(n, **base)

S = {
 "title": P("t", fontName="Helvetica-Bold", fontSize=13, leading=16, spaceAfter=1),
 "sub":   P("s", fontSize=9.6, leading=12.6, textColor=MUTE, spaceAfter=9),
 "meta":  P("m", fontSize=8.7, leading=12),
 "h1":    P("h1", fontName="Helvetica-Bold", fontSize=10.2, leading=13, spaceBefore=13, spaceAfter=5),
 "h2":    P("h2", fontName="Helvetica-Bold", fontSize=9.2, leading=12, spaceBefore=9, spaceAfter=3),
 "body":  P("b", alignment=TA_JUSTIFY, spaceAfter=6),
 "quote": P("q", fontName="Helvetica-Oblique", fontSize=8.7, leading=12,
            leftIndent=13, rightIndent=8, spaceAfter=5),
 "cell":  P("c", fontSize=8.2, leading=11.0),
 "cellb": P("cb", fontName="Helvetica-Bold", fontSize=8.2, leading=11.0),
 "cellq": P("cq", fontName="Helvetica-Oblique", fontSize=8.0, leading=10.6),
 "note":  P("n", fontSize=8.3, leading=11.4, textColor=MUTE, spaceAfter=5),
}

def para(t, s="body"): return Paragraph(t, S[s])
def rule(): return HRFlowable(width="100%", thickness=0.6, color=RULE,
                              spaceBefore=4, spaceAfter=7)

# ---------------- allocation table ----------------
HDR = ["Q", "The question as put", "Properly answered by", "Basis"]
ROWS = [
 ("1(a)", "When was Mr Shepherd first diagnosed with MDD?",
  "<b>Answered below</b> — and confirmed by Dr Ma",
  "Fact within my knowledge; clinical record confirms."),
 ("1(b)", "The clinical basis for identifying these specific workplace stressors as contributing to the exacerbation.",
  "<b>Withdrawal requested</b>",
  "Clinical opinion on causation. Causation is in issue in WC/2024/227 and is not a matter for a workplace adjustment process."),
 ("1(c)", "Whether the stressors are based solely on self-report, clinical assessment, or other reports.",
  "Dr Ma — from his own file",
  "Methodology of the assessing clinician. I do not answer it."),
 ("1(d)", "Foreseeable risk on return, and what workplace controls or adjustments are medically necessary.",
  "<b>Split.</b> Risk: treating psychiatrist. <b>Controls: the Health Service</b>",
  "Identifying and implementing controls is the PCBU's function — WHS Reg 2011 ss 34–36, 55C."),
 ("2", "Whether Mr Shepherd can follow a reasonable and lawful direction, and participate in discussions about performance/conduct.",
  "<b>Answered below — not a medical question</b>",
  "ECC records instruction-following as Normal. Whether directions have been lawful and reasonable is for the Health Service to state."),
 ("3", "Whether he is medically fit to return under the existing reporting arrangements.",
  "<b>Split.</b> Fitness: treating practitioners. <b>Safety of the arrangements: the Health Service</b>",
  "Whether a work arrangement is safe is a s 19 duty on the PCBU, discharged under Reg Part 3.1."),
 ("4", "Restrictions or adjustments recommended, clinical basis in functional terms, duration and review date.",
  "Dr Ma",
  "Already answered by the ECC: 3–6 months, 8-weekly review, next review 28 August 2026."),
 ("5", "What activities are encompassed within “complaint handling”.",
  "<b>Answered below</b>, then Dr Ma",
  "Operational. The Role Description contains no complaint-handling duty; the letter states the escalation process itself."),
 ("6", "Whether he can fulfil the full inherent requirements of the role <i>without restrictions or modifications</i>.",
  "<b>The Health Service</b> — see below",
  "The test applied is not the test under HR Policy G03 or AD Act s 34, which ask about genuine occupational requirements <i>with</i> reasonable adjustment."),
 ("7", "What “working memory is affected under stress” means in functional terms.",
  "Treating psychiatrist",
  "The phrase is drawn from the treating psychiatrist's report of 13 February 2025."),
 ("8", "Tasks, situations or environments that may exacerbate the condition.",
  "<b>Split.</b> Clinical: psychiatrist. <b>Workplace features: addressed below</b>",
  "I am entitled to raise work health and safety matters — WHS Act s 48(1)(b)(i)."),
 ("9", "If the Health Service cannot accommodate the restrictions, can he safely return?",
  "<b>The Health Service</b> — see below",
  "G03 cl 2 places the onus on Queensland Health to prove an adjustment unreasonable, tested against the whole organisation."),
]

def alloc_table():
    data = [[Paragraph(h, S["cellb"]) for h in HDR]]
    for q, ques, who, basis in ROWS:
        data.append([Paragraph("<b>%s</b>" % q, S["cell"]),
                     Paragraph(ques, S["cellq"]),
                     Paragraph(who, S["cell"]),
                     Paragraph(basis, S["cell"])])
    t = Table(data, colWidths=[13*mm, 54*mm, 40*mm, 63*mm], repeatRows=1)
    st = [("GRID",(0,0),(-1,-1),0.4,RULE),
          ("BACKGROUND",(0,0),(-1,0),BAND),
          ("VALIGN",(0,0),(-1,-1),"TOP"),
          ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
          ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]
    for i in range(1, len(data)):
        if i % 2 == 0: st.append(("BACKGROUND",(0,i),(-1,i),LITE))
    t.setStyle(TableStyle(st))
    return t

# ---------------- document ----------------
F = []
F.append(para("ANNOTATED SCHEDULE — REQUEST FOR MEDICAL INFORMATION", "title"))
F.append(para("Response to the correspondence of Metro South Health dated 31 July 2026 &nbsp;·&nbsp; "
              "Ref MSH-INJ-5795 &nbsp;·&nbsp; CLM-317073", "sub"))
F.append(Table([[Paragraph("<b>Prepared by:</b> Cory Shepherd, Administration Officer (AO3), "
                           "Switchboard Services, Logan Hospital", S["meta"]),
                 Paragraph("<b>Date:</b> 31 July 2026", S["meta"])]],
               colWidths=[125*mm, 45*mm],
               style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                 ("LEFTPADDING",(0,0),(-1,-1),0),
                                 ("BOTTOMPADDING",(0,0),(-1,-1),2)])))
F.append(rule())

F.append(para("This schedule sets out each of the nine questions as put, identifies who is properly "
              "placed to answer it, and provides my response to those which are not medical questions. "
              "It is prepared by me and is not a document of the Health Service.", "body"))
F.append(para("I have made appointments with my general practitioner and my treating psychiatrist and "
              "will provide the medical responses on receipt. Costs are being incurred in reliance on the "
              "Health Service's advice that it \"will meet your reasonable costs of preparing this report\".", "body"))

F.append(para("PART A — ALLOCATION", "h1"))
F.append(alloc_table())
F.append(Spacer(1, 4))
F.append(para("Four of the nine questions are not medical questions. They are addressed at Part B. "
              "One question — 1(b) — is the only question I ask be withdrawn.", "note"))

F.append(para("PART B — RESPONSES TO THE NON-MEDICAL QUESTIONS", "h1"))

F.append(para("B1 &nbsp; Question 1(a) — date of first diagnosis", "h2"))
F.append(para("I was first diagnosed on <b>24 October 2024</b>. I answer this openly. Dr Ma can confirm "
              "it from his records.", "body"))

F.append(para("B2 &nbsp; Question 2 — lawful and reasonable directions; performance and conduct", "h2"))
F.append(para("I am able to follow a reasonable and lawful direction and to participate in discussions "
              "about performance or conduct. The Employee Capabilities Checklist of 3 July 2026 records "
              "\"Understanding instructions: <b>Normal</b>\" and \"Carrying out instructions accurately: "
              "<b>Normal</b>\".", "body"))
F.append(para("The record of compliance is as follows: the Checklist was requested on 5 May 2026; I "
              "advised on 21 May 2026 that an appointment was booked for 5 June; the completed Checklist "
              "was provided to Injury Management on 3 July 2026; and on 3 July 2026 I asked the Health "
              "Service to confirm whether I was to attend. I have complied with each request made of me.", "body"))
F.append(para("As to the premise that \"the Health Service is not aware of any concerns being raised for "
              "appropriate management\": the Health Service's objection of 5 June 2026, signed by the "
              "Chief Executive, refers to a public interest disclosure by its reference number. A complaint "
              "was made on 4 October 2025 and a further complaint in February 2026.", "body"))
F.append(para("Whether the directions given have been lawful and reasonable is a matter for the Health "
              "Service to state, together with the instrument relied on. I have asked for that instrument "
              "and it has not been identified.", "body"))

F.append(para("B3 &nbsp; Question 5 — the meaning of “complaint handling”", "h2"))
F.append(para("The Role Description provided as Attachment 2 contains no complaint-handling "
              "responsibility. The letter itself states the position: \"established process for client "
              "complaints received by Switchboard employees is for immediate escalation and management by "
              "the Health Service Client Liaison Officer and/or Manager, Switchboard Services\".", "body"))
F.append(para("The restriction asks that complaints be logged and redirected rather than actioned, "
              "resolved or absorbed. That is the process the Health Service describes as its own.", "body"))

F.append(para("B4 &nbsp; Question 6 — the inherent requirements test", "h2"))
F.append(para("The question asks whether I can fulfil the requirements of the role \"without restrictions "
              "or modifications to duties\". That is not the test under the policy the same letter cites.", "body"))
F.append(para("HR Policy G03 (QH-POL-210) exists \"to assist employees … to meet the <b>genuine "
              "occupational requirements</b> of their role by applying <b>principles of reasonable "
              "adjustment</b>\", and cl 3 provides that adjustments \"should support the employee to "
              "undertake the genuine occupational requirements of their role\". Section 34 of the "
              "<i>Anti-Discrimination Act 1991</i> is to the same effect.", "quote"))
F.append(para("I ask the Health Service to identify the genuine occupational requirements of the role "
              "which it says are not met, and the adjustment considered in respect of each. The Checklist "
              "records that \"usual switchboard operational duties remain suitable\".", "body"))

F.append(para("B5 &nbsp; Question 9 — accommodation and onus", "h2"))
F.append(para("The question assumes an inability to accommodate which has not been assessed or "
              "communicated. G03 cl 2 provides:", "body"))
F.append(para("unjustifiable hardship \"is tested against <b>the whole organisation, not a division or "
              "unit within the organisation</b> … the <b>onus is on Queensland Health, as the employer, to "
              "prove an adjustment is unreasonable</b>, not on the person to prove that it is reasonable\".", "quote"))
F.append(para("I ask the Health Service to identify what adjustment has been assessed, by whom, against "
              "what part of the organisation, and on what basis it was found unreasonable.", "body"))

F.append(para("PART C — THE CONSULTATION FRAMEWORK", "h1"))
F.append(para("The Checklist identifies, among the matters relevant to a return, \"unresolved workplace "
              "matters involving line management\". Under s 55A of the <i>Work Health and Safety "
              "Regulation 2011</i> a psychosocial hazard is one arising from or relating to \"the design or "
              "management of work\" or \"workplace interactions or behaviours\". Matters of that kind are "
              "assessed and controlled under Part 3.1 of the Regulation.", "body"))
F.append(para("Section 55C(1) provides that a person conducting a business or undertaking \"<b>must manage "
              "psychosocial risks under part 3.1</b>\". Section 36(3) requires that risks be minimised by "
              "substituting the hazard, <b>isolating the hazard from any person exposed to it</b>, or "
              "engineering controls, before administrative controls are considered.", "quote"))
F.append(para("Section 47(1) of the <i>Work Health and Safety Act 2011</i> requires consultation with "
              "workers directly affected by a matter relating to work health or safety, and s 48(1) "
              "requires that information be shared, that workers have a reasonable opportunity "
              "<b>to contribute to the decision-making process</b>, that their views be taken into account, "
              "and that they be advised of the outcome.", "body"))
F.append(para("My position is that the matters I have raised — changes to work arrangements made without "
              "consultation, responsibility for patient safety without corresponding input, and the "
              "handling of concerns once raised — fall within the hazard categories described in the "
              "<i>Managing the risk of psychosocial hazards at work Code of Practice 2022</i>: poor "
              "organisational change management, low job control, poor support, and poor organisational "
              "justice. Each is a feature of the work. I ask that they be assessed as such.", "body"))
F.append(para("I have raised consultation as a patient safety matter since 2024. Switchboard Services "
              "routes emergency and after-hours calls on a continuous 24/7 roster. My concern is that "
              "changes to those arrangements made without consulting the operators who action them carry "
              "risk. That concern is unchanged and it is the reason I seek to be included in decisions "
              "affecting the work for which I am accountable.", "body"))

F.append(para("PART D — WHAT IS ASKED OF THE HEALTH SERVICE", "h1"))
for n, t in [
 ("1", "The psychosocial risk assessment conducted for the AO3 Switchboard Services role and work unit, "
       "any hazard register, the control measures currently in place, and the record under s 55D(2) of the "
       "Regulation of the matters had regard to in determining them."),
 ("2", "The date of the last psychosocial risk assessment for Switchboard Services, and the date of the "
       "last such assessment that included input from the workers in that unit, together with the record "
       "of that consultation under s 48(1)(c) and (d) of the Act."),
 ("3", "The genuine occupational requirements of the role which are said not to be met, and the "
       "adjustment considered in respect of each."),
 ("4", "What adjustment has been assessed and found unreasonable, by whom, and against what part of the "
       "organisation."),
 ("5", "The name and position of the delegate who approved this request, the instrument under which that "
       "delegation is held, and the date on which approval was given."),
 ("6", "Whether a health and safety representative is in place for the work unit, and a copy of the "
       "Health Service's public interest disclosure procedures published under s 28(2) of the "
       "<i>Public Interest Disclosure Act 2010</i>."),
 ("7", "Confirmation that medical information provided will be held by the Injury Management team, "
       "Human Resources. My consent under the Queensland Privacy Principles extends to that team and not "
       "to Corporate Services."),
 ("8", "Confirmation of the date by which the completed responses are required, having regard to the "
       "earliest available specialist appointment. The Checklist was requested on 5 May 2026 and provided "
       "on 3 July 2026 without objection."),
 ("9", "The record of shifts rostered and worked by me over the twelve months preceding the Employee "
       "Capabilities Checklist, including the average shifts per fortnight and the average expressed as a "
       "proportion of the full-time equivalent for the role. The Checklist refers to “the pattern "
       "Mr Shepherd has in fact worked and tolerated over the past twelve months without deterioration”. "
       "That data is held by the Health Service and not by me or by my practitioners. My understanding is "
       "that the average was materially below full-time. I ask that the Health Service produce its own "
       "record so that question 6 can be answered against what was in fact required of me, rather than "
       "against an assumption."),
]:
    F.append(para("<b>%s.</b>&nbsp; %s" % (n, t), "body"))

F.append(para("PART E — FOR COMPLETION BY THE HEALTH SERVICE", "h1"))
F.append(para("The correspondence of 31 July 2026 records that a decision will be made regarding my "
              "ability to perform my role. So that the decision-maker is identified on the record, and "
              "having regard to the matters raised at Part 6 of my response of today's date, I ask that "
              "the officer exercising the delegation complete the following.", "body"))
_rows = [
 [Paragraph("<b>Name of delegate</b>", S["cell"]), "", Paragraph("<b>Position</b>", S["cell"]), ""],
 [Paragraph("<b>Instrument or schedule of delegation relied on</b>", S["cell"]), "", "", ""],
 [Paragraph("<b>Date approval given</b>", S["cell"]), "",
  Paragraph("<b>Directorate</b>", S["cell"]), ""],
 [Paragraph("<b>Signature</b>", S["cell"]), "", Paragraph("<b>Date</b>", S["cell"]), ""],
]
_t = Table(_rows, colWidths=[46*mm, 44*mm, 26*mm, 54*mm],
           rowHeights=[11*mm, 13*mm, 11*mm, 13*mm])
_t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#BBBBBB")),
                        ("SPAN",(1,1),(3,1)),
                        ("VALIGN",(0,0),(-1,-1),"TOP"),
                        ("LEFTPADDING",(0,0),(-1,-1),4),
                        ("TOPPADDING",(0,0),(-1,-1),4)]))
F.append(_t)
F.append(Spacer(1, 4))
F.append(para("I make no assumption as to who holds the delegation. I ask only that it be identified.", "note"))

F.append(rule())
F.append(para("This schedule is provided so that the questions may be directed to the practitioners "
              "properly placed to answer them, and so that the matters which are not medical questions "
              "may be addressed by the Health Service. I remain willing to return to work.", "note"))

def deco(c, d):
    c.saveState(); c.setFont("Helvetica", 7.6); c.setFillColor(MUTE)
    c.drawString(20*mm, 12*mm, "Cory Shepherd  ·  Annotated Schedule  ·  MSH-INJ-5795")
    c.drawRightString(190*mm, 12*mm, "Page %d" % d.page)
    c.restoreState()

doc = BaseDocTemplate(RAW, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                      topMargin=18*mm, bottomMargin=20*mm, title="Annotated Schedule MSH-INJ-5795")
doc.addPageTemplates([PageTemplate(id="n",
        frames=[Frame(20*mm, 20*mm, 170*mm, 259*mm, id="f")], onPage=deco)])
doc.build(F)
subprocess.run(["qpdf","--linearize","--",RAW,OUT], check=False)
subprocess.run(["exiftool","-overwrite_original","-all=","-Title=Annotated Schedule MSH-INJ-5795",OUT],
               check=False, capture_output=True)
print("built:", OUT)
