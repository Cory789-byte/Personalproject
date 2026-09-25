#!/usr/bin/env python3
"""WC/2024/227 - WHAT I AM PROVING. Internal working map of the elements, the evidence and the gaps.
Not for filing or service. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer, PageBreak
PS=landscape(A4); W=PS[0]-24*mm
HD=ParagraphStyle('HD',fontName='Helvetica-Bold',fontSize=8.4,leading=10.5,textColor=colors.HexColor('#333333'))
T=ParagraphStyle('T',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=2)
SUB=ParagraphStyle('S',fontName='Helvetica-Oblique',fontSize=8,leading=10.5,textColor=colors.HexColor('#555555'),spaceAfter=7)
H1=ParagraphStyle('H1',fontName='Helvetica-Bold',fontSize=11,leading=14,spaceBefore=7,spaceAfter=4)
B=ParagraphStyle('B',fontName='Helvetica',fontSize=8.9,leading=11.4,spaceAfter=4)
C=ParagraphStyle('C',parent=B,fontSize=7.6,leading=9.4,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
WARN=ParagraphStyle('W',parent=B,fontName='Helvetica-Bold',textColor=colors.HexColor('#8B0000'))
def P(t,s=B): return Paragraph(t,s)
def c(t): return Paragraph(t,C)
def tbl(rows,widths):
    t=Table(rows,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),
      ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
      ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return t

s=[P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",HD),
   P("Matter No. WC/2024/227 | Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)",HD),
   P("WHAT I AM PROVING",T),
   P("Working map of the elements, the evidence that goes to each, and the gaps. Prepared 6 September 2026. "
     "INTERNAL. Not for filing or service. Sources: Workers' Compensation Appeal Guide v2.10 (11 March 2025); "
     "WCRA ss 11, 32, 549, 550, 558; Industrial Relations Act 2016 s 531; Industrial Relations (Tribunals) Rules 2011.",SUB)]

s.append(P("A. What the Commission requires of me",H1))
s.append(P("The appeal is heard <b>de novo</b>: Guide Part 5.1, \"workers' compensation appeals before the Commission are heard "
  "over again from the beginning\", and \"even though the Regulator may have previously accepted an element of s 32 of the Act, "
  "it does not mean that this element will be accepted by the Respondent at the appeal stage\". "
  "<b>The onus is mine</b>: Guide Part 7.3, \"the onus of proof is on the Appellant\", to the balance of probabilities and, on "
  "<i>Briginshaw</i>, \"to a comfortable degree, based on clear and cogent evidence\". The Respondent's own pleading puts it the "
  "same way at paragraph 5.",B))
s.append(P("For a psychiatric or psychological disorder, Guide Part 7.3.2 requires me to prove that I was a worker under s 11; "
  "that I sustained a personal injury; that the injury arose out of, or in the course of, the employment; and that employment "
  "was a significant contributing factor to it. In addition I must show that the injury \"was not connected to management "
  "action that was reasonable in the circumstances and/or conducted in a reasonable way\", and that it was not connected to my "
  "\"expectation or perception of reasonable management action being taken\".",B))

s.append(P("B. The map",H1))
rows=[[Paragraph(x,CB) for x in ["Element","Status","What proves it","Through whom","Where it is"]]]
R=[
("s 11 &ndash; worker","<b>Admitted</b>","The Respondent admits at paragraph 26 of its amended statement of facts and contentions that the Appellant is a worker within s 11.","&mdash;","SOFC &para;26"),
("s 32(1) &ndash; personal injury, being a psychiatric or psychological disorder","Contested as to accuracy only",
 "Diagnosis of Major Depressive Disorder with anxious distress (DSM-5 296.23). The practice email of 24 October 2024 at 11:45 am records the diagnosis on the day of first consultation. The report of 13 February 2025 records it in writing. The four work capacity certificates certify anxiety and stress and no capacity from 1 July to 6 October 2024. Review Decision 69983 finds \"you sustained a personal injury of a psychological nature\".",
 "Dr Krishnaiah (orally); Dr Hawes (orally); Appellant tenders the Review Decision","Medical bundle Tabs 2, 3, 4, 7"),
("s 32(1) &ndash; arose out of or in the course of employment","Not admitted",
 "The contemporaneous general-practice notes of 28 June 2024 (\"stress at work\", \"upset by people not following rules\") and 1 July 2024 (\"work stress\"; \"they withhold pay at times, no overtime- not processed, manipulate his roster- so he works lates then earlies\"), both written before any claim decision, dismissal or proceeding. The Appellant's own account of the events. Review Decision 69983 so finds.",
 "Dr Hawes; Appellant","Medical bundle Tab 1 (bundle pp 5, 7) and Tab 7"),
("s 32(1) &ndash; employment a significant contributing factor","Denied at &para;22(f)",
 "Dr Krishnaiah: \"workplace stress stemming from issues with management and rostering\"; the issues \"began approximately one year ago when a new manager was appointed\"; pay \"withheld or delayed for up to five months at a time, leading to significant financial stress\"; \"premature exposure to the workplace is more likely result in significant deterioration\". Dr Hawes told WorkCover on 2 September 2024 that work events were the sole cause and certified no pre-existing factor. Review Decision: \"I am satisfied your employment was a significant contributing factor to the psychological injury\". The test is <i>a</i> significant factor, not the main one.",
 "Dr Krishnaiah (orally); Dr Hawes (orally); Appellant","Medical bundle Tabs 4, 2, 7"),
("s 32(5)(a) &ndash; the injury did not arise out of reasonable management action taken in a reasonable way","The whole contest",
 "The 303 admitted facts and Annexure A served 28 August 2026. The rostering of 17&ndash;18 March 2024: a seven-hour break, admitted; the Award requires ten hours; Ms Forrest's email of 7 July 2026 says the eight-hour agreement applies \"only where staff initiated shift swaps have occurred\" and the Respondent does not allege a swap; the roster record shows the break is unique in 368 rostered shifts and appears on no published roster. The fatigue response: request 8 April, escalation 9 April, follow-up 24 April, refusal 1 May, on an agreement signed as a casual in 2020. The Chief Executive's letter of 5 June 2026: no fatigue risk assessment records, no register, training \"only applies to health practitioners and clinical assistants\", assessment at the Switchboard \"occurred after 30 June 2024\", \"no 'consequential' changes to operating procedures\". Ms Reese, 10 May 2024: \"a few rostering errors made by Chloe with regards to Cory's line in past rosters\". The pay loop of 3 to 28 May 2024 and the myHR record that only the manager could initiate an AVAC. The directory restriction of 18 July 2023 and the misdirected clinical calls of 2 to 8 May 2024.",
 "Appellant; Ms Jeffrey; Mr Harrison-Jones; Ms Conaghan","Notice to admit facts and Annexure A; roster record; CE letter"),
("s 32(5)(b) &ndash; not the expectation or perception of reasonable management action","Pleaded at &para;6(d)(ii)",
 "Under <i>Prizeman v Q-COMP</i> [2005] QIC 53 it is the reality of the employer's conduct, not the employee's perception of it, that is assessed. Every event relied upon is an admitted document, not a perception. A clinician's use of the word \"perceived\" to describe a patient's report does not convert a seven-hour break, a twenty-five day pay correction or eleven months without directory access into perceptions.",
 "Appellant (submissions)","Notice to admit facts"),
("s 32(5)(c) &ndash; not action by WorkCover","Not in issue",
 "The injury was sustained on 18 June 2024. The application for compensation was lodged on 1 July 2024. Nothing WorkCover did can have caused an injury that preceded the claim.","Appellant","Chronology"),
]
for e,st,pr,wh,wr in R: rows.append([c("<b>"+e+"</b>"),c(st),c(pr),c(wh),c(wr)])
s.append(tbl(rows,[42*mm,26*mm,W-42*mm-26*mm-40*mm-32*mm,40*mm,32*mm]))

s.append(PageBreak())
s.append(P("C. How each document actually gets into evidence",H1))
for t_ in [
 "<b>Nothing is evidence until it is tendered.</b> Guide Part 7.5: documents \"must be tendered 'through a witness'. This means "
 "that you ask a particular witness questions about a document that they have knowledge of, and then you have the document "
 "tendered and it will become an exhibit\". Part 7.6.1: \"documents not tendered at the hearing will not be considered as "
 "evidence and the Member of the Commission hearing the appeal will not take them into consideration when making the decision\". "
 "The admitted facts are not self-executing at the hearing; the Notice, the response and Annexure A are tendered like anything else.",
 "<b>All evidence is oral, and there are no witness statements.</b> Guide Part 7.6: \"In workers' compensation matters, all "
 "witness evidence is provided orally. There are generally no affidavits or witness statements. Therefore, the Directions Order "
 "only requires that you provide a one-page outline of evidence for each of the witnesses to each of the parties.\" That is why "
 "the outlines state topics and not sentences, and why the June 2026 affidavit is not evidence in the appeal.",
 "<b>A medical report cannot stand alone.</b> Guide Part 7.6.5: \"presenting a medical report on its own cannot be considered "
 "without having the expert witness give evidence orally to support that document and being available for cross-examination by "
 "the other party.\" This is the single most important procedural fact in the appeal. Unless Dr Krishnaiah and Dr Hawes give "
 "oral evidence, their reports and certificates carry no opinion, and the causation case rests on the contemporaneous notes, "
 "the admitted Review Decision findings and the Appellant's own evidence.",
 "<b>Reluctant witnesses are compelled, not persuaded.</b> Guide Part 6.2.2: \"In workers' compensation appeals, medical "
 "witnesses may require a notice which requires that they attend the Commission and produce a copy of their report\", by Form 32 "
 "with Form 32A, 32B or 32C, approved by a Member or the Registrar. Dr Krishnaiah wrote on 5 September 2026 that he does not "
 "have time for medico-legal work. An attendance notice is the mechanism, and it also protects a current employee who would "
 "rather be compelled than seen to volunteer. Expert witnesses are entitled to conduct money at a higher rate (Part 10.1).",
 "<b>The Commission is not bound by the rules of evidence</b> (Industrial Relations Act 2016 s 531), which is why treating "
 "records written for clinical purposes can be received. That does not displace Part 7.6.5 for opinion evidence.",
 "<b>What the Commission may do.</b> WCRA s 558: confirm the decision, vary it, or set it aside and substitute another decision. "
 "Costs are in the Commission's discretion and, per Guide Part 10, generally follow the event, assessed under WCRA s 558(3) and section 191 of "
 "the Workers' Compensation and Rehabilitation Regulation 2025 (UCPR sch 2 pt 2 scale C; from 1 Sep 2025). The Calderbank offer of 1 July 2026, rejected on 16 July 2026, "
 "is relevant to costs.",
]: s.append(P(t_))

s.append(P("D. What is not yet in evidence, and what to do about it",H1))
rows=[[Paragraph(x,CB) for x in ["Gap","Why it matters","Next step","By when"]]]
G=[("Dr Krishnaiah's attendance","Without him the 13 February 2025 report carries no opinion (Guide 7.6.5).","Ask him in writing whether he will attend if given notice; if no answer or a refusal, file Form 32 with Form 32A.","Early October, well before the hearing"),
("Dr Hawes's attendance","He recorded the 1 July 2024 mechanism and told WorkCover work events were the sole cause. That statement currently reaches the Commission only through the Review Decision.","Same: written request, then Form 32 and 32A.","Early October"),
("Clinical records of Dr Krishnaiah from 24 October 2024","They fix what was reported at the first consultation, before the claim was rejected and before the dismissal.","Offered by the practice on 5 September 2026 and requested. Serve on receipt.","On receipt"),
("Confirmation from Ms Jeffrey, Mr Harrison-Jones and Ms Conaghan","Their outlines are served on Wednesday. If any will not attend or gives different evidence, that is a problem at hearing.","Speak to each; offer an attendance notice so that appearance is compelled rather than voluntary.","Within two weeks"),
("General-practice records after 1 July 2024","The Regulator's Form 29 to the practice stopped at 1 July 2024, so the antidepressant prescribing is in no document either party holds.","Request the record from 1 July to 31 October 2024 from the practice as the patient.","This week"),
("The 18&ndash;31 March 2024 roster version history","The published version held contains no line for the Appellant, although the 06:00 start on 18 March is admitted.","Ask the Respondent, and if necessary Metro South, for all versions of that roster.","With the disclosure request"),
("Switchboard team leave data for the stressor year","Published rosters record two sick-leave cells in 4,662 staff-days; team absence cannot be counted from them.","Seek de-identified or aggregate leave data for the cost centre.","With the disclosure request"),
("Rosters after 29 March 2026","The only documents that could test compliance with Dr Ma's restrictions of 3 July 2026.","Request from Metro South.","When convenient"),
]
for g,w,n,b in G: rows.append([c("<b>"+g+"</b>"),c(w),c(n),c(b)])
s.append(tbl(rows,[46*mm,W*0.30,W*0.34,32*mm]))

s.append(PageBreak())
s.append(P("E. The package served on 9 September 2026, and what each document does",H1))
rows=[[Paragraph(x,CB) for x in ["Document","Direction","Filed or served","What it does"]]]
D=[("Appellant's list of names of all witnesses","1","Filed in the Registry and served on the Respondent","Names the six witnesses. A witness not listed cannot be called without leave, which is why both doctors and the three colleagues are on it."),
("Covering letter to the Industrial Registrar","1","Filed with the list","Records compliance with both directions, and puts on the record that the Appellant does not presently propose to call Ms Taylor or Ms Reese and proceeds on the basis that the Respondent will."),
("Outline of evidence &ndash; Mr Cory Lea Shepherd","2","Served only","One A4 page. Ten topics in the order the medical record tells them, each cross-referenced to the paragraphs of the notice to admit facts."),
("Outlines &ndash; Ms Jeffrey, Mr Harrison-Jones, Ms Conaghan","2","Served only","One A4 page each. Topics only, no placeholders, no words put in their mouths."),
("Schedule of medical documents relied upon","2","Served only","States that no report was prepared for the proceeding, identifies every treating record and report relied upon, and states for each what it is and is not relied upon for."),
("Medical documents relied upon &ndash; schedule and pages (35 pp)","2","Served only","The pages themselves under eight tabs, with omitted pages identified, private entries redacted and marked, and the Respondent's own February 2026 responses at Tab 8."),
]
for d,dr,f,wd in D: rows.append([c("<b>"+d+"</b>"),c(dr),c(f),c(wd)])
s.append(tbl(rows,[62*mm,16*mm,52*mm,W-62*mm-16*mm-52*mm]))
s.append(Spacer(1,3*mm))
s.append(P("Direction 2 is served on the Respondent and <b>not filed in the Registry</b> (Guide Part 4.11 and the terms of the "
  "Further Directions Order). Direction 1 is filed and served. Both are due by 4.00 pm on Wednesday 9 September 2026. If any "
  "part cannot be met, an extension must be sought in writing from qirc.registry@qirc.qld.gov.au before the deadline, and the "
  "Respondent asked whether it consents (Guide Part 4.4). Rule 230 of the Industrial Relations (Tribunals) Rules 2011 and the "
  "Commission's own practice on non-compliance make a missed direction the one avoidable way to lose ground in this appeal.",WARN))

buf=io.BytesIO(); doc=BaseDocTemplate(buf,pagesize=PS,leftMargin=12*mm,rightMargin=12*mm,topMargin=11*mm,bottomMargin=13*mm)
def footer(cv,d):
    cv.saveState(); cv.setFont('Helvetica',7); cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(12*mm,7*mm,"WC/2024/227 - What I am proving - INTERNAL, NOT FOR SERVICE")
    cv.drawRightString(PS[0]-12*mm,7*mm,f"Page {d.page}"); cv.restoreState()
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(12*mm,13*mm,PS[0]-24*mm,PS[1]-24*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
doc.build(s); buf.seek(0)
pdf=pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/WHAT_I_AM_PROVING_INTERNAL.pdf"; pdf.save(out,linearize=True); print("built",out,len(pdf.pages),"pages")
