#!/usr/bin/env python3
"""WC/2024/227 - Stressor 2 as mechanism, not quantum: the recurring unresolved error.

INTERNAL WORKING DOCUMENT. Not for service.
Objective features only in the left column; the effect is the treating psychiatrist's to
characterise. Built 23 August 2026 from Cory's own formulation.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/STRESSOR2_AS_MECHANISM.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.6, leading=13.5,
                     spaceBefore=9, spaceAfter=4)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.1, leading=12.6, spaceAfter=4)
Q   = ParagraphStyle('Q', parent=B, leftIndent=8*mm, rightIndent=6*mm, fontName='Helvetica-Oblique')
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

st = [P("Stressor 2 as mechanism, not quantum", H1),
      P("WC/2024/227 &middot; 23 August 2026 &middot; internal working document, not for service", SUB)]

st.append(P("The formulation", H2))
st.append(P("&ldquo;It is not the money. It is the consistent vigilance of it being wrong.&rdquo;", Q))
st.append(P("That is not a new theory. <b>It is the case theory of this matter applied to the pay "
            "sequence</b> &mdash; recorded in the working method as: <i>one mechanism, "
            "<b>responsibility imposed and the means to discharge it withheld</b></i>, with one "
            "admitted instance in the seven-hour break. The pay sequence is <b>a second instance of "
            "the same mechanism</b>.", B))

rows=[[P("", CH), P("Responsibility imposed", CH), P("Means to discharge it withheld", CH)]]
for a,b,c in [
 ("<b>Stressor 3</b><br/>the fatigue breach",
  "Operating a 24/7 safety-critical switchboard, running emergency codes, on a 7-hour break",
  "No fatigue risk management framework existed. The Chief Executive confirms it began <b>after 30 June 2024</b>"),
 ("<b>Stressor 2</b><br/>the pay sequence",
  "Detecting the error, reporting it, evidencing it, chasing it, and checking each fortnight whether it had been fixed",
  "<b>He could not submit an AVAC.</b> Five were submitted in the period, <b>every one by the Line Manager</b>. He initiated none"),
]:
    rows.append([P(a, C), P(b, C), P(c, C)])
t=Table(rows, colWidths=[34*mm, 70*mm, 74*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
st.append(t)
st.append(Spacer(1,2*mm))
st.append(P("&#9733; <b>That unification matters.</b> Two stressors sharing one mechanism is "
            "<i>Mahaffey</i> reasoning &mdash; a course of conduct with an identifiable structure. "
            "Thirteen unrelated grievances is <i>Delaney</i> reasoning, and <i>Delaney</i> is the "
            "Respondent's authority.", B))

st.append(P("The objective features that generate it &mdash; all provable, none characterised", H2))
rows=[[P("Feature", CH), P("Established by", CH)]]
for a,b in [
 ("The error was <b>recurring, not single</b> &mdash; four affected fortnights: commencing 5 Feb, 19 Feb, 18 Mar and 1 Apr 2024",
  "Payroll's own email of 3 May 2024"),
 ("It ran <b>109 days</b> from the shift that caused it to the correction being submitted, and was <b>still not complete</b> when he stopped working",
  "Payroll email &middot; myHR Item 11 &ldquo;Part Completed&rdquo;"),
 ("<b>He made eight approaches. He received six responses.</b>",
  "The pay contact log; the emails held and those recited in the Review Decision"),
 ("<b>He had no authority to correct it.</b> Five AVACs in the period, all initiated by the Line Manager; he initiated none",
  "myHR submissions report, MSH Item 11"),
 ("He was <b>directed to a process he could not complete</b> &mdash; to MyHR on 9 April, and payroll directed him back to her on 24 April and again on 13 May",
  "Review Decision p 21 &middot; the email of 13 May 2024"),
 ("<b>The reason given for the delay was overtaken by a document he held.</b> Told on 1 and 21 May that payroll was awaited; payroll had asked her to act on 3 May, on a thread he was copied on",
  "The thread <i>Corey Shepherd 388372 Pay issues</i>"),
 ("<b>The machinery was never slow.</b> Other claims completed in one to five days; one completed in a single day on 15&ndash;16 May 2024",
  "myHR submissions report"),
 ("<b>Each fortnight was a fresh check.</b> The pay cycle is fortnightly, so the question of whether it had been fixed recurred every fourteen days",
  "The payslips; the pay-cycle derivation"),
]:
    rows.append([P(a, C), P(b, C)])
t=Table(rows, colWidths=[112*mm, 66*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]))
st.append(t)

st.append(P("Where it sits in the frameworks already on the file", H2))
st.append(P("The three-construct mechanism recorded for the psychiatric report &mdash; <b>job strain, "
            "effort&ndash;reward imbalance, organisational justice</b> &mdash; takes this without "
            "modification:", B))
rows=[[P("Construct", CH), P("The objective features that answer to it", CH)]]
for a,b in [
 ("<b>Job strain</b><br/><font size=7>demand with low control</font>",
  "High demand &mdash; monitor every fortnight, detect, report, evidence, chase. <b>Nil control</b> &mdash; the corrective instrument was not his to use"),
 ("<b>Effort&ndash;reward imbalance</b>",
  "Eight approaches over four and a half months. The return was redirection to a process he could not complete, and a correction that never completed"),
 ("<b>Organisational justice</b>",
  "The <i>Managing the risk of psychosocial hazards at work Code of Practice 2022</i> &mdash; which HR Policy G03 cl 1 obliges MSH to apply &mdash; defines <b>poor organisational justice</b> as a lack of procedural, <b>informational</b> and interpersonal fairness, arising from <b>&ldquo;inconsistent application of procedures across workers or over time&rdquo;</b> and <b>&ldquo;failing to follow agreed policies, guidelines and procedures&rdquo;</b>"),
]:
    rows.append([P(a, C), P(b, C)])
t=Table(rows, colWidths=[42*mm, 136*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
    ('BACKGROUND',(0,3),(-1,3),colors.HexColor('#eef3ee'))]))
st.append(t)
st.append(Spacer(1,2*mm))
st.append(P("&#9733; <b>Informational fairness is the limb that fits closest</b> &mdash; &ldquo;keeping "
            "relevant people informed&rdquo;. He was told payroll was awaited when payroll had "
            "already instructed; he was not told when the claim went in; and he was not told it had "
            "not completed. And <b>inconsistent application over time</b> is proved by the employer's "
            "own record: four claims completed in days, the corrective one did not.", B))

st.append(P("&#9888; The line that must not be crossed", H2))
st.append(P("Section 32(5)(b) excludes injury connected with the worker's <b>expectation or "
            "perception</b> of management action. The Respondent has not pleaded it. <b>Vigilance "
            "describes an internal state, so the word itself should not appear in anything filed.</b>", W))
st.append(P("<b>Split it.</b> The <b>facts</b> are objective and belong to him: the error recurred, "
            "it ran four months, he approached eight times, he had no authority to correct it, and it "
            "never completed. The <b>effect of those facts on him</b> is a clinical question and "
            "belongs to Dr Krishnaiah. Say the first. Never say the second in his own voice.", B))
st.append(P("<b>Safe formulation for a witness outline:</b>", B))
st.append(P("&ldquo;Between February and May 2024 my pay was incorrect across four fortnights. I "
            "raised it on 8 April, 24 April, 10 May and 15 May 2024. Payroll advised me on 24 April "
            "and again on 13 May that the correction had to be made by my line manager. I was not "
            "able to submit the correcting form myself. The correction was submitted on 28 May 2024 "
            "and is recorded in the employer's system as part completed. I last attended work on "
            "3 June 2024.&rdquo;", Q))

st.append(P("For 27 August &mdash; what to put to Dr Krishnaiah", H2))
st.append(P("Describe it as lived experience, dated, without naming a construct. <b>Do not use the "
            "words job strain, effort-reward imbalance, organisational justice or vigilance</b> "
            "&mdash; if the patient supplies the framework, the report reads as built to order. "
            "Give him the facts and the experience: what checking each payslip was like, what it was "
            "like to be told to go to payroll and then be sent back, and what it was like on 21 May "
            "to be told she was waiting on payroll when the instruction had been in the thread since "
            "3 May.", B))
st.append(P("<b>The characterisation is his to make.</b> A recurring, unresolved demand that the "
            "person cannot themselves resolve is the pattern the allostatic-load literature "
            "describes as a failure of the stress response to switch off between demands &mdash; but "
            "that connection is for the clinician to draw, if he considers it clinically apt, and "
            "not for the Appellant to hand him.", B))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - Stressor 2 as mechanism - internal, not for service")
    cv.drawRightString(PW-16*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=15*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, PW-32*mm, PH-31*mm)],
                                   onPage=foot)])
doc.build(st); buf.seek(0)
p = pikepdf.open(buf)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(p.pages)}")
