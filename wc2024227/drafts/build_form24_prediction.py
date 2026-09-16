#!/usr/bin/env python3
"""WC/2024/227 - predicted response to the second notice to admit facts. INTERNAL. 20 August 2026."""
import pikepdf, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=13, leading=17, spaceAfter=3)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.5, leading=13.6,
                    spaceBefore=11, spaceAfter=4, backColor=colors.HexColor('#eeeeee'), borderPadding=4)
BODY = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.4, leading=12.8, spaceAfter=6)
ITEM = ParagraphStyle('I', parent=BODY, leftIndent=10, spaceBefore=3, spaceAfter=3)
SMALL = ParagraphStyle('S', parent=BODY, fontSize=8.3, leading=11.2, textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('W', parent=BODY, fontSize=9, leading=12.4, textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=6)
def P(t, s=BODY): return Paragraph(t, s)
def tbl(rows, w):
    t = Table(rows, colWidths=w, repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#aaaaaa')),
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eeeeee')),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    return t

s=[]
s.append(P("Predicted response to the second notice to admit facts", H1))
s.append(P("WC/2024/227 &nbsp;|&nbsp; 76 facts, 26 documents &nbsp;|&nbsp; prediction made 20 August 2026, "
           "before service", SMALL))
s.append(P("<b>INTERNAL. A structured judgement, not a measurement.</b> Built from the Respondent's "
           "actual answering patterns in its response of 18 February 2026. The ranking of the "
           "sections is more reliable than any individual percentage.", WARN))

s.append(P("SECTION BY SECTION", H2))
s.append(tbl([
 [P("<b>Section</b>",SMALL),P("<b>Items</b>",SMALL),P("<b>Predicted answer</b>",SMALL),P("<b>Admitted</b>",SMALL)],
 [P("<b>A</b> Hours sought, 2023",SMALL),P("1-13",SMALL),
  P("Admitted, with a relevance reservation attached - her pattern at &para;44 (\"admits the "
    "contents... and says that this fact is not relevant\"). The reservation does not undo the "
    "admission.",SMALL),P("~90%",SMALL)],
 [P("<b>B</b> Aug-Sep 2023",SMALL),P("14-21",SMALL),
  P("Admitted, several qualified (\"admits... and says that...\"). Item 21 (no grievance submitted) "
    "may draw a non-admission for want of knowledge.",SMALL),P("~85%",SMALL)],
 [P("<b>C</b> The call-in process",SMALL),P("22-31",SMALL),
  P("22-29 admitted; the 15 April email is now sourced to her own List of Documents. <b>Item 30 is "
    "her one pleaded fight</b> - she alleges non-compliance at &para;16(b)(i), so expect a qualified "
    "admission at best. Item 31 admitted now that a copy is enclosed.",SMALL),P("~80%",SMALL)],
 [P("<b>D</b> Fatigue knowledge",SMALL),P("32-41",SMALL),
  P("Admitted. Every document is her own witness-conferencing disclosure. There is no available "
    "move.",SMALL),P("~92%",SMALL)],
 [P("<b>E</b> The Chief Executive's letter",SMALL),P("42-47",SMALL),
  P("Contents admitted, probably with \"a document of a non-party which the Respondent does not "
    "adopt\". That still admits what the letter says.",SMALL),P("~88%",SMALL)],
 [P("<b>F</b> Her own List of Documents",SMALL),P("48-54",SMALL),
  P("Admitted. She filed the list. Nothing to dispute.",SMALL),P("~98%",SMALL)],
 [P("<b>G</b> Stressor 1(a) documents",SMALL),P("55-62",SMALL),
  P("Admitted - the Respiratory chain sits in her own Taylor bundle, and the \"no particulars\" "
    "objection at &para;11 is spent since 11 August.",SMALL),P("~90%",SMALL)],
 [P("<b>H</b> The break and the leave",SMALL),P("63-69",SMALL),
  P("<b>Items 63-64 (the Forrest letter) are the real contest</b> - see below. 65-69 admitted: they "
    "are facts about her own pleading.",SMALL),P("~75%",SMALL)],
 [P("<b>I</b> The negatives",SMALL),P("70-76",SMALL),
  P("Admitted, now that 70-72, 74 and 75 are framed as \"the Respondent does not allege...\". "
    "Item 73 comes from her own &para;24(b). Item 76 may draw a non-admission.",SMALL),P("~85%",SMALL)],
],[38*mm,14*mm,96*mm,18*mm]))
s.append(Spacer(1,3*mm))
s.append(P("<b>AGGREGATE: about 62 to 66 of the 76 facts admitted, and 22 to 24 of the 26 documents "
           "admitted as to authenticity.</b> Call it 85 per cent.", BODY))

s.append(P("THE ONE REAL FIGHT - ITEMS 63 AND 64", H2))
s.append(P("The Forrest letter of 7 July 2026 states that the roster \"provides more than 10-hour "
           "breaks between shifts\" and that the 2020 eight-hour agreement \"is only applied where "
           "staff initiated shift swaps have occurred\". Admitting it costs her paragraph 22(e), "
           "which relies on that agreement. Denying it means the Regulator disputing the employer's "
           "own senior HR consultant's written statement about the employer's own agreement - with a "
           "copy of the letter enclosed with the notice.", BODY))
s.append(P("<b>Prediction: she does not deny it outright.</b> The likely answers are (a) admits the "
           "letter states those words but does not admit the underlying fact because it is a "
           "non-party document (~45%); (b) admits (~30%); (c) does not admit for want of relevance "
           "to the matters in issue (~20%); (d) denies (~5%). <b>On (a), (b) or (c) the words are "
           "on the record.</b> Only (d) is a positive dispute, and it is the answer that reads "
           "worst.", BODY))

s.append(P("HOW SHE RESPONDS PROCEDURALLY", H2))
s.append(tbl([
 [P("<b>Branch</b>",SMALL),P("<b>Likelihood</b>",SMALL),P("<b>What follows</b>",SMALL)],
 [P("Seeks an extension of the 14 days first",SMALL),P("<b>~55%</b>",SMALL),
  P("Consent in writing to a specific date. It costs nothing and it is returned when you need your "
    "own extension for the expert report.",SMALL)],
 [P("Answers substantially and on time",SMALL),P("<b>~60%</b>",SMALL),
  P("The predicted outcome above. Record the admissions in one short letter; no commentary.",SMALL)],
 [P("Answers minimally or globally",SMALL),P("~15%",SMALL),
  P("A general non-admission is not a proper answer under rule 49. That is the rule 41(2)(g) moment "
    "- an order requiring a response.",SMALL)],
 [P("Silence past the 14 days",SMALL),P("~10%",SMALL),
  P("<b>All 76 facts and 26 documents deemed admitted</b>, and leave required to withdraw any of "
    "it. Record it in one letter and move on.",SMALL)],
 [P("Denies heavily",SMALL),P("~10%",SMALL),
  P("Every denial of a document from her own disclosure is a cross-examination opening, and feeds "
    "the costs argument under s 558(3) that makes the Calderbank bite.",SMALL)],
],[52*mm,20*mm,94*mm]))

s.append(PageBreak())
s.append(P("WHAT IT CHANGES - THE HONEST NUMBERS", H2))
s.append(tbl([
 [P("<b>Question</b>",SMALL),P("<b>Before</b>",SMALL),P("<b>After</b>",SMALL),P("<b>Why</b>",SMALL)],
 [P("Can the factual matrix be <i>proved</i> at hearing?",SMALL),P("~75%",SMALL),P("<b>~93%</b>",SMALL),
  P("The largest single gain. A self-represented appellant proving two years of documents through "
    "witnesses is the biggest execution risk in the case, and admissions remove it.",SMALL)],
 [P("Does the s 32(5)(a) exclusion fail?",SMALL),P("~60%",SMALL),P("<b>~72%</b>",SMALL),
  P("\"Reasonable in all respects\" must now be argued against an admitted record of no assessment, "
    "no training, no system, no remedy and a three-hour breach.",SMALL)],
 [P("Is the appeal resolved favourably?",SMALL),P("~65-70%",SMALL),P("<b>~70-73%</b>",SMALL),
  P("A modest lift only - because causation is untouched. The report still decides the appeal.",SMALL)],
 [P("Does it settle before hearing?",SMALL),P("~45%",SMALL),P("<b>~55%</b>",SMALL),
  P("She must fix her position on the record about 4 September, blind to the medical evidence and "
    "three weeks before her own material is due.",SMALL)],
 [P("Length of the hearing",SMALL),P("3-4 days",SMALL),P("<b>2-3 days</b>",SMALL),
  P("Fewer documents to prove, fewer witnesses needed, narrower contest.",SMALL)],
],[46*mm,18*mm,18*mm,84*mm]))

s.append(P("THE SINGLE MOST VALUABLE EFFECT", H2))
s.append(P("<b>Timing.</b> Served now, the fourteen days expire about 4 September. Her own material "
           "is not due until 30 September, and the psychiatric report may not exist until later. "
           "<b>She must commit, in writing, to a position on the entire documentary record while "
           "blind to the medical evidence.</b> Every other benefit follows from that one.", BODY))

s.append(P("WHAT IT DOES NOT DO", H2))
for t in ["It proves nothing about causation. The Respondent does not admit the injury at &para;9 "
          "and refuses the clean baseline at &para;8. <b>The report still decides the appeal.</b>",
          "Admitted facts are not admitted conclusions. She can admit every word and still contend "
          "the management action was reasonable.",
          "It does not stop her calling Ms Taylor and Ms Reese to explain the documents orally.",
          "It does not insure against a weak report. If causation fails, the appeal fails whatever "
          "is admitted."]:
    s.append(P("- "+t, ITEM))

s.append(P("THE PREDICTION IN ONE LINE", H2))
s.append(P("<b>About 85 per cent of the notice is admitted or deemed admitted by early September; "
           "the Respondent's defence is reduced to one unparticularised sentence and one contested "
           "letter; the hearing shortens by a day; and the appeal moves from \"can he prove what "
           "happened\" to \"does the doctor say it caused the injury\" - which is exactly where the "
           "last two years of work were aimed.</b>", WARN))

OUT="out/FORM24_PREDICTION_INTERNAL.pdf"
doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm)
def f(c,d):
    c.saveState();c.setFont('Helvetica-Bold',7.2);c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(18*mm,9*mm,"INTERNAL - PREDICTION - NEVER FILED OR SERVED")
    c.setFont('Helvetica',7.2);c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-18*mm,9*mm,f"Page {d.page}");c.restoreState()
doc.build(s,onFirstPage=f,onLaterPages=f)
pdf=pikepdf.open(OUT,allow_overwriting_input=True)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save("out/_p.pdf"); pdf.close(); os.replace("out/_p.pdf",OUT)
print("built",OUT)
