import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, HRFlowable)

INK  = colors.HexColor("#111111"); MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#9a9a9a"); BAND = colors.HexColor("#ECECEC")
BOX  = colors.HexColor("#BBBBBB")

def P(n, **kw):
    b = dict(fontName="Helvetica", fontSize=9.2, leading=12.8, textColor=INK); b.update(kw)
    return ParagraphStyle(n, **b)
S = {
 "title": P("t", fontName="Helvetica-Bold", fontSize=12.5, leading=15.5, spaceAfter=1),
 "sub":   P("s", fontSize=9.4, leading=12.4, textColor=MUTE, spaceAfter=8),
 "meta":  P("m", fontSize=8.7, leading=12),
 "h1":    P("h1", fontName="Helvetica-Bold", fontSize=10, leading=13, spaceBefore=12, spaceAfter=5),
 "body":  P("b", alignment=TA_JUSTIFY, spaceAfter=6),
 "q":     P("q", fontName="Helvetica-Bold", fontSize=9.2, leading=12.6,
            leftIndent=15, firstLineIndent=-15, spaceBefore=8, spaceAfter=4),
 "qs":    P("qs", fontSize=9.0, leading=12.4, leftIndent=15, spaceAfter=4),
 "note":  P("n", fontSize=8.4, leading=11.5, textColor=MUTE, spaceAfter=5),
 "cell":  P("c", fontSize=8.6, leading=11.6),
}
def para(t, s="body"): return Paragraph(t, S[s])
def rule(): return HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=4, spaceAfter=7)

def answerbox(h=26*mm):
    t = Table([[""]], colWidths=[170*mm], rowHeights=[h])
    t.setStyle(TableStyle([("BOX",(0,0),(-1,-1),0.5,BOX),
                           ("BACKGROUND",(0,0),(-1,-1),colors.white)]))
    return t

def signblock():
    rows = [[Paragraph("<b>Practitioner name</b>", S["cell"]), "",
             Paragraph("<b>Provider no.</b>", S["cell"]), ""],
            [Paragraph("<b>Signature</b>", S["cell"]), "",
             Paragraph("<b>Date</b>", S["cell"]), ""],
            [Paragraph("<b>Practice details / stamp</b>", S["cell"]), "", "", ""]]
    t = Table(rows, colWidths=[34*mm, 60*mm, 22*mm, 54*mm],
              rowHeights=[11*mm, 11*mm, 24*mm])
    t.setStyle(TableStyle([("GRID",(0,0),(-1,-1),0.5,BOX),
                           ("SPAN",(1,2),(3,2)),
                           ("VALIGN",(0,0),(-1,-1),"TOP"),
                           ("LEFTPADDING",(0,0),(-1,-1),4),
                           ("TOPPADDING",(0,0),(-1,-1),4)]))
    return t

def header(F, who, addr, formref):
    F.append(para("REQUEST FOR MEDICAL INFORMATION — %s" % formref, "title"))
    F.append(para("Questions arising from the correspondence of Metro South Health dated 31 July 2026 "
                  "&nbsp;·&nbsp; Ref MSH-INJ-5795 &nbsp;·&nbsp; CLM-317073", "sub"))
    F.append(Table([[Paragraph("<b>Patient:</b> Mr Cory Shepherd &nbsp; <b>DOB:</b> 11 January 1991<br/>"
                               "<b>Employer:</b> Metro South Health — Logan and Beaudesert Health Service<br/>"
                               "<b>Role:</b> Administration Officer (AO3), Switchboard Services, Logan Hospital "
                               "(permanent full-time, 76 hours per fortnight)", S["meta"]),
                     Paragraph("<b>To:</b> %s<br/>%s<br/><br/><b>Date:</b> [DATE]" % (who, addr), S["meta"])]],
                   colWidths=[100*mm, 70*mm],
                   style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0)])))
    F.append(rule())
    F.append(para("<b>This form is provided by the patient, Mr Cory Shepherd. It is not a document of "
                  "Metro South Health.</b> The Health Service issued nine questions on 31 July 2026. Four "
                  "of those are not medical questions and have been returned to the Health Service. The "
                  "questions below are those properly within your field. They are reproduced as the Health "
                  "Service put them.", "note"))
    F.append(para("Metro South Health has advised in writing that it \"will meet your reasonable costs of "
                  "preparing this report\". Invoices are to be sent to Ms Michelle Harrison, Injury "
                  "Management Consultant, Human Resources, Logan and Beaudesert Health Service, "
                  "lbh_InjuryManagement@health.qld.gov.au.", "note"))

def build(path, who, addr, formref, intro, questions, closing):
    F = []
    header(F, who, addr, formref)
    F.append(para(intro, "h1"))
    for label, text, hint, h in questions:
        F.append(para("%s&nbsp;&nbsp;%s" % (label, text), "q"))
        if hint: F.append(para(hint, "qs"))
        F.append(answerbox(h)); F.append(Spacer(1, 5))
    F.append(para(closing, "note"))
    F.append(Spacer(1, 6))
    F.append(signblock())
    def deco(c, d):
        c.saveState(); c.setFont("Helvetica", 7.6); c.setFillColor(MUTE)
        c.drawString(20*mm, 12*mm, "Provided by Cory Shepherd  ·  MSH-INJ-5795  ·  %s" % formref)
        c.drawRightString(190*mm, 12*mm, "Page %d" % d.page); c.restoreState()
    raw = "/tmp/_form_%s.pdf" % formref.replace(" ","_")
    doc = BaseDocTemplate(raw, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                          topMargin=18*mm, bottomMargin=20*mm, title=formref)
    doc.addPageTemplates([PageTemplate(id="n",
        frames=[Frame(20*mm, 20*mm, 170*mm, 259*mm, id="f")], onPage=deco)])
    doc.build(F)
    subprocess.run(["qpdf","--linearize","--",raw,path], check=False)
    subprocess.run(["exiftool","-overwrite_original","-all=","-Title=%s" % formref, path],
                   check=False, capture_output=True)
    print("built:", path)

OUT = "/home/user/Personalproject/wc2024227/drafts/out/"

build(OUT+"FORM_A_GP_DrMa_MSH-INJ-5795.pdf",
      "Dr Day Hong Ma", "My Doctors Clinic<br/>16/3221 Surfers Paradise Boulevard<br/>Surfers Paradise QLD 4217",
      "FORM A — General Practitioner",
      "Questions for the treating general practitioner",
      [("1(a)", "When was Mr Shepherd first diagnosed with Major Depressive Disorder?",
        "Mr Shepherd states this was 24 October 2024 and asks that you confirm from your records.", 20*mm),
       ("1(c)", "Whether the workplace stressors identified in the Employee Capabilities Checklist are "
                "based solely on Mr Shepherd's self-report, your own clinical assessment, or other medical "
                "information/reports available to you.",
        "You may wish to identify the specialist reports held on file, including the treating "
        "psychiatrist's report of 13 February 2025.", 30*mm),
       ("4", "If Mr Shepherd is not able to return to his substantive role under the existing reporting "
             "arrangements, please specify any restrictions or adjustments you recommend, the clinical "
             "basis for those recommendations in functional terms, and the anticipated duration and "
             "review date.",
        "The Employee Capabilities Checklist of 3 July 2026 records 3–6 months with 8-weekly review, "
        "next review 28 August 2026. Please confirm whether that remains your opinion.", 34*mm),
       ("5", "The Checklist recommends that Mr Shepherd not undertake complaint-handling duties. Please "
             "clarify what specific activities are encompassed within “complaint handling” — receiving, "
             "documenting, redirecting, resolving, or all complaint-related interactions.",
        "The Health Service has advised that its established process is immediate escalation to the "
        "Client Liaison Officer and/or Manager, Switchboard Services, and the Role Description records "
        "no complaint-handling duty.", 30*mm),
       ("6", "Please confirm the medical records and specialist reports you hold in respect of "
             "Mr Shepherd, and whether the Employee Capabilities Checklist you completed on 3 July 2026 "
             "remains your opinion.", None, 26*mm)],
      "Questions concerning the clinical basis of causation, functional effects of working memory, and "
      "the specific tasks or environments said to exacerbate the condition have been directed to the "
      "treating psychiatrist.")

build(OUT+"FORM_B_Psychiatrist_MSH-INJ-5795.pdf",
      "The Treating Psychiatrist", "[practice name]<br/>[address]",
      "FORM B — Treating Psychiatrist",
      "Questions for the treating psychiatrist",
      [("1(d)", "Whether exposure to the identified workplace stressors presents a foreseeable risk to "
                "Mr Shepherd's health or safety if he were to return to work, and if so, what specific "
                "workplace controls or adjustments you consider medically necessary to manage that risk.",
        "Mr Shepherd notes that identifying and implementing controls is a function of the employer "
        "under Part 3.1 of the Work Health and Safety Regulation 2011. Your opinion is sought on what is "
        "medically necessary.", 40*mm),
       ("7", "The report of 13 February 2025 states that Mr Shepherd's “working memory is affected under "
             "stress”. Please clarify what this means in functional terms in the workplace, including "
             "(a) how this may affect capacity to perform substantive duties under normal workplace "
             "demands, and (b) the types of circumstances likely to cause this difficulty.", None, 40*mm),
       ("8", "Are there specific tasks, situations or environments (for example high-pressure settings, "
             "shift work, patient acuity) that may exacerbate Mr Shepherd's condition or symptoms?",
        "The role is a continuous shift working role covering multiple shifts over a 24/7 period.", 36*mm)],
      "This report is sought in respect of current capacity, functional restrictions and workplace "
      "controls. It is not sought on the aetiology of the injury, which is a separate matter.")
