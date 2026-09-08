#!/usr/bin/env python3
"""WC/2024/227 - INTERNAL assessment model: the reasoning of the case, the medical as it stands,
and whether lay witnesses on effect should be called. Not for service. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether

T =ParagraphStyle('T',fontName='Helvetica-Bold',fontSize=13,leading=16,alignment=1,spaceAfter=1)
TS=ParagraphStyle('TS',fontName='Helvetica-Oblique',fontSize=8.6,leading=11,alignment=1,textColor=colors.HexColor('#555555'),spaceAfter=7)
PT=ParagraphStyle('PT',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3)
SB=ParagraphStyle('SB',fontName='Helvetica-Bold',fontSize=9.3,leading=11.6,spaceBefore=4,spaceAfter=2)
B =ParagraphStyle('B',fontName='Helvetica',fontSize=9.1,leading=11.5,spaceAfter=4)
L =ParagraphStyle('L',parent=B,leftIndent=6*mm,firstLineIndent=-6*mm)
C =ParagraphStyle('C',fontName='Helvetica',fontSize=8.0,leading=9.9,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
W=A4[0]-36*mm
def tbl(rows,widths,repeat=1):
    data=[[P(c,CB) for c in rows[0]]]+[[P(c,C) for c in r] for r in rows[1:]]
    t=Table(data,colWidths=widths,repeatRows=repeat)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
        ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return t

s=[P("WC/2024/227 &mdash; ASSESSMENT MODEL",T),
   P("The reasoning of the case as it now stands; the medical if Dr Krishnaiah is called and if he is not; "
     "and whether any lay witness on effect should be called. INTERNAL. Not for service. 9 September 2026.",TS),

   P("PART 1 &mdash; THE REASONING MODEL: FIVE GATES",PT),
   P("The appeal succeeds only if every gate is passed. Gates 1 to 4 are s 32(1). Gate 5 is s 32(5). The onus is on the "
     "Appellant at every gate (Guide, Part 7.3), to the Briginshaw standard.",B),
   tbl([["Gate","What must be found","What carries it now","What is missing","Risk"],
        ["1. Worker","s 11 worker","Employment admitted; role description admitted (facts 1 to 13)","Nothing","None"],
        ["2. Personal injury","A psychiatric or psychological disorder","Dr Krishnaiah's diagnosis of MDD with anxious distress; work capacity certificates; Review Decision finding of \"a personal injury of a psychological nature\" (facts 257 to 261)","The Regulator admits the report <i>says</i> so, not its accuracy. Proof of the disorder itself needs a doctor in the box","Medium; low if Dr Krishnaiah attends"],
        ["3. Arose out of or in the course of employment","Connection between the injury and the employment","298 admitted facts; onset 18 June 2024 while employed; first presentation 28 June 2024 attributing symptoms to work","Nothing of substance","Low"],
        ["4. Employment a significant contributing factor","Employment was <b>a</b> significant contributing factor, not the only one","Dr Hawes 1 July 2024; Dr Krishnaiah's account of origin; the Regulator's own reviewer so found on the same certificates (facts 257 to 261); no pre-existing factor on the certificate","The doctors' oral evidence. The competing-cause argument at Part 4 below","Medium; the contest lives here"],
        ["5. s 32(5) does not exclude","Either the contributor was not management action, or the management action was not reasonable or not reasonably taken","Limb (i): the conditions of work are not management action. Limb (ii): errors admitted, no consultation record, no fatigue assessment, the reviewer's finding of unreasonable management action","Their witnesses' explanations, if they call any","Low to medium"]],
       [22*mm,38*mm,W-22*mm-38*mm-30*mm-22*mm,30*mm,22*mm]),
   P("<b>Where the case is won or lost:</b> gates 2 and 4, and both are medical. Gates 1, 3 and 5 are now carried by the "
     "admissions and by the documents. That is the whole effect of 8 September 2026: the factual contest has been replaced "
     "by a medical one.",B),

   P("PART 2 &mdash; SCENARIO A: DR KRISHNAIAH ATTENDS",PT),
   P("Gate 2 closes. He states the diagnosis, its basis and its date. Gate 4 closes if he says employment was a significant "
     "contributing factor, and his 13 February 2025 report already attributes the presentation to \"workplace stress stemming "
     "from issues with management and rostering at Queensland Health\".",B),
   P("<b>What he will be cross-examined on, and the answer:</b>",SB),
   tbl([["Line of attack","Answer already on the record"],
        ["\"Your history came from the patient\"","Every event in the history is a fact the Regulator admitted on 8 September 2026"],
        ["\"These issues began approximately one year ago when a new manager was appointed\" is wrong; Ms Taylor was manager by June 2023","It is an approximation in a clinical record. The documents give the exact dates and they are admitted"],
        ["The 26 October 2022 ADHD and anxiety history entries","Two lines in a history list. No psychotropic medication on the 16 May 2024 list. \"No psychological illness such as depression or psychosis\", mood good, 16 November 2023"],
        ["The Q6(b) sentence: \"multiple life stressors, including relationship breakdown, job loss, and bereavement\"","Every one of them post-dates the onset. See Part 4"],
        ["The footer, \"not for medico-legal use\"","His email of 8 September 2026 identifies the report as answering the three matters in issue, and his email of 5 September 2026 releases his records for use in the legal issues"],
        ["\"You did not see the full records\"","Answerable only if he has been shown the 26 October 2022 entry before he gives evidence. See Part 6"]],
       [52*mm,W-52*mm]),

   P("PART 3 &mdash; SCENARIO B: HE DOES NOT ATTEND",PT),
   P("Guide 7.6.5: a report on its own cannot be considered without its author available for cross-examination. Tabs M3 and M4 "
     "then carry little weight and the diagnosis is not proved by a psychiatrist.",B),
   P("<b>The fallback, in order of strength:</b>",SB),
   P("1.&nbsp;&nbsp;<b>Dr Hawes.</b> The treating GP at the date of injury. He proves the first presentation, the mechanism as "
     "recorded, the certification of no capacity from 1 July 2024, that there was no pre-existing factor or condition, and the "
     "referral to a psychiatrist on 8 September 2024. A GP can give evidence of a psychological injury and of its work "
     "connection. He cannot give a specialist diagnosis of Major Depressive Disorder.",L),
   P("2.&nbsp;&nbsp;<b>The Review Decision.</b> Admitted as to contents. The Regulator's own reviewer found a personal injury of "
     "a psychological nature and that employment was a significant contributing factor, on the same certificates. De novo means "
     "it does not bind the Commission, but the Commission is entitled to ask what evidence now displaces it, and the Regulator "
     "will have none unless it calls an expert.",L),
   P("3.&nbsp;&nbsp;<b>The Appellant's own evidence</b> of symptoms and their effect, with the contemporaneous records.",L),
   P("<b>Assessment:</b> gate 2 is still passable on Dr Hawes plus the Review Decision, because the Regulator has admitted its "
     "own finding of a psychological injury and has no contrary medical evidence unless it briefs an expert by 30 September. "
     "Gate 4 becomes materially harder without the psychiatrist. Scenario B is survivable; it is not the case to choose.",B),
   P("&rArr; <b>The single highest-value action left in the appeal is a confirmed hearing date from Dr Krishnaiah, or an "
     "attendance notice.</b> Nothing else available moves the odds as much.",B),

   P("PART 4 &mdash; THE LIFE-EVENTS DEFENCE, AND THE SEQUENCE THAT ANSWERS IT",PT),
   P("The report's Q6(b) sentence is the Regulator's best available competing-cause material, and it is in the Appellant's own "
     "bundle. It must be met head on, and it is met by dates.",B),
   tbl([["Date","Event","Position relative to onset"],
        ["16 Nov 2023","No psychological illness; mood good","7 months before"],
        ["16 May 2024","Psychiatrist referral renewed; melatonin the only medication","1 month before"],
        ["<b>18 Jun 2024</b>","<b>ONSET</b>","<b>Causation is assessed here</b>"],
        ["1 Jul 2024","First certificate; no pre-existing factor or condition","2 weeks after"],
        ["9 Oct 2024","Employment treated as abandoned &mdash; the \"job loss\"","<b>4 months after; and it is the employer's act</b>"],
        ["24 Oct 2024","Diagnosis. His partner attended the consultation and was recorded as supportive","<b>4 months after; the relationship was intact</b>"],
        ["~Dec 2024","Personal and relationship matters commence","<b>6 months after</b>"],
        ["Feb 2025","Separation &mdash; the \"relationship breakdown\"","<b>8 months after</b>"],
        ["Mar 2025","Bereavement &mdash; the death of his grandfather","<b>9 months after</b>"],
        ["7 Apr 2025","Return to work at about 29 per cent of full time","10 months after"]],
       [24*mm,W-24*mm-46*mm,46*mm]),
   P("<b>Three propositions follow, and each is provable from the record:</b>",SB),
   P("(a)&nbsp;&nbsp;<b>Not one of the three life stressors existed at onset.</b> The nearest is six months late. A condition "
     "diagnosed in October 2024 cannot have been caused by a separation in February 2025 or a death in March 2025.",L),
   P("(b)&nbsp;&nbsp;<b>Two of the three are not independent.</b> The \"job loss\" was the employer treating the employment as "
     "abandoned while the Appellant held current certificates, later reversed by reinstatement. The relationship strain is "
     "attributed by the report itself, at pages 1 and 2, to the financial stress caused by pay withheld or delayed \"for up to "
     "five months at a time\" &mdash; the same admitted pay conduct. The report's own causal account runs: workplace &rarr; "
     "withheld pay &rarr; financial stress &rarr; relationship strain.",L),
   P("(c)&nbsp;&nbsp;<b>Only the bereavement is genuinely independent, and it is nine months post-onset.</b> On the record it "
     "is also the leave the abandonment letter counted against him.",L),
   P("<b>Why this is a strength, not a weakness:</b> the sentence is at the end of the report, in the section on whether "
     "occupational rehabilitation was appropriate in February 2025. It is an explanation of why he was too unwell to be "
     "rehabilitated then. It is not an aetiology. Read with the dated sequence, it shows the injury spreading into the rest of "
     "his life, which is the opposite of what the Regulator needs it to show.",B),

   P("PART 5 &mdash; SHOULD ANY LAY WITNESS ON EFFECT BE CALLED",PT),
   P("<b>What is already proved on the effect, without any family witness:</b>",SB),
   P("Certified no capacity from 1 July 2024. Fluoxetine increased and quetiapine added on 24 October 2024. By 13 February "
     "2025 a treatment-resistant depressive state, and the psychiatrist's own clinical observation on examination: "
     "\"Appeared physically drained and showed signs of neglecting personal hygiene, reporting a decrease in his usual "
     "self-care routine. He was anxious throughout the interview with intermittent intense sweating.\" Reduced self-care and "
     "impaired social functioning recorded. Continuing restrictions in the Employee Capability Checklist of 3 July 2026. "
     "The deterioration curve is documented at 2 weeks, 4 months, 8 months and 2 years, by clinicians, in documents the "
     "Regulator holds.",B),
   tbl([["Witness","What they would add","What they would open","Verdict"],
        ["His mother","Observation of change over time; appearance; self-care","Her account is <b>already in the medical evidence</b> &mdash; Dr Krishnaiah records that he \"obtained collateral information from his mother independently\" and relied on it. Calling her puts an untested lay version beside the psychiatrist's; and she can be asked about the bereavement, which is her family's","<b>Do not call.</b> Her evidence is already before the Commission, filtered through a psychiatrist, which is stronger"],
        ["His partner (former)","Observation of change; the household; appearance","Directly opens the separation, its timing and its causes, and the \"sugar mommy\" passage. Hands the Regulator its competing cause through the Appellant's own witness, and requires the Appellant to litigate his private life in a public hearing","<b>Do not call.</b> The cost is certain and the gain is marginal"],
        ["A colleague on effect","Change observed at work before June 2024","Mr Harrison-Jones and Ms Conaghan are already listed and their outlines include what they observed of the Appellant at work, offered without opinion as to diagnosis or cause","<b>Already covered.</b> No further witness needed"]],
       [30*mm,44*mm,W-30*mm-44*mm-30*mm,30*mm]),
   P("<b>The general principle:</b> a lay witness on effect is worth calling when the effect is disputed and no clinician "
     "recorded it. Here the effect is recorded by three clinicians in contemporaneous documents, and the Regulator has not "
     "disputed that the Appellant was unwell. Its case is about <i>cause</i>, not about severity. A witness who adds nothing "
     "to cause, but whose cross-examination goes to the separation and the bereavement, is a net loss.",B),
   P("<b>The one contingency:</b> if Dr Krishnaiah does not attend and Scenario B is run, the effect evidence carries more of "
     "the load. Even then the better answer is Dr Hawes and the records, not family, for the same reason.",B),

   P("PART 6 &mdash; WHAT REMAINS TO BE DONE, IN ORDER OF VALUE",PT),
   P("1.&nbsp;&nbsp;<b>Dr Krishnaiah's attendance confirmed in writing,</b> or an attendance notice applied for. Highest value "
     "action available.",L),
   P("2.&nbsp;&nbsp;<b>Obtain the 26 October 2022 record</b> that the Regulator says is \"missing from Exhibit A5\", and put it "
     "in front of Dr Krishnaiah before he gives evidence. He cannot be asked about a document he has not seen, and the "
     "Regulator will ask.",L),
   P("3.&nbsp;&nbsp;<b>Dr Krishnaiah's clinical records</b> (schedule item 5), served on receipt.",L),
   P("4.&nbsp;&nbsp;<b>Fix the bereavement date</b> in the internal chronology &mdash; it is recorded as March 2025 but the exact "
     "date has been outstanding since August. It will be asked.",L),
   P("5.&nbsp;&nbsp;<b>Dr Hawes's attendance,</b> as the fallback that makes Scenario B survivable.",L),
   P("6.&nbsp;&nbsp;<b>The register (Tab M31 of Annexure A)</b> through the request of today's date.",L),

   P("PART 7 &mdash; THE DECISION FOR TODAY",PT),
   P("The list of witnesses is filed today. It names five: the Appellant, Dr Krishnaiah, Dr Hawes, Mr Harrison-Jones and "
     "Ms Conaghan. On this assessment <b>no family member should be added,</b> and the list as prepared is correct. Nothing "
     "in the package requires change.",B),
   P("If that assessment is rejected and a family member is to be called, the name must go on the list before 4.00 pm today; "
     "adding a witness afterwards requires an application and an explanation, and the Regulator would be entitled to ask why "
     "the evidence was not foreshadowed.",B),
]
def footer(canvas,doc):
    canvas.saveState(); canvas.setFont('Helvetica',7.6); canvas.setFillColor(colors.HexColor('#666666'))
    canvas.drawString(18*mm,9*mm,"WC/2024/227 · Assessment model · INTERNAL — not for service")
    canvas.drawRightString(A4[0]-18*mm,9*mm,"Page %d"%doc.page); canvas.restoreState()
buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=14*mm,bottomMargin=14*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(18*mm,14*mm,A4[0]-36*mm,A4[1]-28*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
d.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="INTERNAL/2026-09-09_CASE_ASSESSMENT_MODEL_medical_and_witnesses.pdf"; pdf.save(out,linearize=True); print("built",out,n,"page(s)")
