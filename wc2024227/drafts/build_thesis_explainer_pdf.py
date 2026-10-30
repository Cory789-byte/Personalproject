#!/usr/bin/env python3
"""Internal explainer: the concession thesis and its evidentiary spine.
Renders a self-contained PDF (no source .md) → INTERNAL/. NOT FOR SERVICE."""
import os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Table, TableStyle,
                                Spacer, HRFlowable)

OUT = os.path.join(os.path.dirname(__file__), "INTERNAL",
                   "CONCESSION_THESIS_and_EVIDENCE_14SEP2026.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def C(t):
    for k, v in {"—":" - ","–":"-","…":"...","‘":"'","’":"'",
                 "“":'"',"”":'"',"¶":"¶","×":"x","≈":"~","→":"->",
                 "⭐":"","⛔":"[!] ","s 32":"s 32"}.items():
        t = t.replace(k, v)
    t = t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    import re
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    try: t.encode("latin-1")
    except UnicodeEncodeError: t = t.encode("latin-1","replace").decode("latin-1")
    return t

TITLE = ParagraphStyle('t', fontName='Helvetica-Bold', fontSize=15, leading=18, spaceAfter=3)
SUB   = ParagraphStyle('s', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor('#666666'), spaceAfter=2)
H1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=12, leading=15, spaceBefore=12, spaceAfter=4, textColor=colors.HexColor('#1a1a1a'))
H2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceBefore=7, spaceAfter=3)
BODY = ParagraphStyle('b', fontName='Helvetica', fontSize=9, leading=12.5, spaceAfter=4)
LEAD = ParagraphStyle('l', parent=BODY, fontSize=9.5, leading=13.5, textColor=colors.HexColor('#111111'))
CELL = ParagraphStyle('c', fontName='Helvetica', fontSize=7.7, leading=9.8)
CELLB= ParagraphStyle('cb', parent=CELL, fontName='Helvetica-Bold')
CELLH= ParagraphStyle('ch', parent=CELL, fontName='Helvetica-Bold', textColor=colors.white)

def h1(t): return Paragraph(C(t), H1)
def h2(t): return Paragraph(C(t), H2)
def p(t, st=BODY): return Paragraph(C(t), st)
def rule(): return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#cccccc'), spaceBefore=4, spaceAfter=4)

def table(headers, rows, widths):
    data = [[Paragraph(C(h), CELLH) for h in headers]]
    for r in rows:
        data.append([Paragraph(C(c), CELLB if j==0 else CELL) for j,c in enumerate(r)])
    t = Table(data, colWidths=[w*mm for w in widths], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#33475b')),
        ('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#bbbbbb')),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
        ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#f3f5f7')]),
    ]))
    return t

S = []
S += [p("CORY LEA SHEPHERD v WORKERS' COMPENSATION REGULATOR - WC/2024/227", SUB),
      Paragraph(C("Why I conclude the appeal will be conceded - the thesis and its evidence"), TITLE),
      p("Internal analysis - 14 September 2026 - <b>NOT FOR SERVICE OR FILING</b> - "
        "prediction work only; nothing in this document is put to the Regulator, MSH or the Commission.", SUB),
      rule()]

# ---- The thesis ----
S += [h1("1. The thesis, in one paragraph"),
 p("Reading the correspondence and the material served on 9 September 2026 as a whole, the "
   "Regulator's rational move is to concede - and the concession will be legible not through the "
   "words of any letter but through <b>specific names</b> on the witness list it must file on "
   "30 September 2026. The reason is structural: by admitting 298 of 303 facts and denying none, "
   "the Regulator has already certified the record as genuine and closed the conduct case; the "
   "medical schedule closes the only remaining live element (causation); and the acts are proved "
   "on paper without witnesses. What is left to \"defend\" can only be defended by calling the very "
   "people whose own admitted documents would be put to them - a roster of caged witnesses that is, "
   "in substance, my own cross-examination list. A party does not assemble that. So the tell is "
   "<b>absence</b>: if Ms Reese and the clinicians are not named on the 30 September list, the "
   "conduct defence is over, whatever the 25 September letter says.", LEAD)]

S += [h2("What is fact and what is inference"),
 p("Everything in sections 2-6 is verified against the served PDFs and the responses on file. The "
   "single inference is whether the Regulator has <b>decided</b> to concede - which is not on the "
   "record and becomes visible only in the 25 September letter (register) and the 30 September "
   "list (decision). The thesis is that concession is the <b>rational</b> outcome this instrument "
   "engineers - not a decision I claim to have observed.")]

# ---- The evidence timeline ----
S += [h1("2. The evidentiary spine - the correspondence, in order"),
 p("Each row is a document on the file. The right column states what that document contributes to "
   "the thesis.")]
S += [table(
 ["Date", "Document / email / submission", "What it contributes"],
 [["Nov 2024","Form 9 - Notice of Appeal (s 549 WCRA), filed and sealed; DO(1) 3 Dec 2024 (Dwyer)",
   "The appeal is a hearing de novo. Dwyer has case-managed from the outset."],
  ["13 May 2026","Regulator's Statement of Facts and Contentions (SOFC)",
   "The anchor of the position formula (\"defend the appeal as outlined in our SOFC\"). It pre-dates the 303 facts and is not tested against them."],
  ["5 Jun 2026","MSH letter to Commissioner Dwyer, K-LM26/729 (signed Cridland, CE)",
   "MSH's own signed statement - later admitted at facts 263-268 (Tab 20). Every MSH witness must answer under it."],
  ["23 Jun 2026","Form 29 / rule 64G disclosure application, filed and sealed",
   "Establishes the record-compulsion posture and the filing discipline that makes my deadlines credible."],
  ["1 Jul 2026","Calderbank offer #2, served on Matheson and the OIR registry",
   "A documented, dated willingness to resolve. The reasonableness record if costs are argued."],
  ["16 Jul 2026","Regulator rejection of the offer",
   "Contains the undertaking: \"should our position change at any point, we will advise you.\" The 25 Sep letter is the first document that can be that advice."],
  ["31 Jul 2026","\"Material development\" letter to Matheson (without prejudice)",
   "Signals counsel and a hardening case; keeps the settlement door visible."],
  ["7 Aug 2026","Mention before Commissioner Dwyer (MSH required to attend; Ruttan present)",
   "Dwyer prescribes the ask-first process for MSH-held documents. MSH Legal hears the appeal's shape first-hand."],
  ["28 Aug 2026","Notice to admit - 303 facts (Form 24), authenticity notice (Form 25), served",
   "The demonstration: 303 facts marshalled, each tied to a proof path. Execution risk (\"can a self-rep run it?\") is put to the test."],
  ["8 Sep 2026","Regulator response: 298 admitted, 0 denied; 14 tabs disputed by a provenance column; cover letter (legal register, non-Matheson author)",
   "The certificate of genuineness. Conduct limb closes. The disputes are a mechanical rule, not a belief in fabrication."],
  ["9 Sep 2026","The package: witness list (filed), letter re 8 Sep (the acts footing), request letter, medical schedule Tabs M1-M9, three outlines",
   "The instrument. The reason to concede (schedule) inside a dignified frame (outline), with the defence roster named back to them."],
  ["10 Sep 2026, 14:42","Matheson: extension to Fri 25 Sep \"to review this request and if needed reach out to MSH\"",
   "Fastest reply in the file. \"If needed\" only parses as \"if defending\" - MSH is mandatory on any defend path. The 15 days = sign-off / consult window."],
  ["10-11 Sep 2026","Employment-track letters (information handling; LSL / RFMI forms) to LBH HR, IM, Payroll, Roberts",
   "The parallel track, still live and documented."],
  ["12 Sep 2026 on","MSH employment-track silence; its own deadline passed",
   "Legal hold: everything Shepherd-related routed through Legal pending the appeal. The appeal is now the master track."],
 ],
 [17, 63, 100])]

# ---- Why each pillar forces the conclusion ----
S += [h1("3. Why the material forces the conclusion - the five pillars"),
 p("<b>Pillar 1 - The admissions certify the record and close conduct.</b> 298 of 303 facts "
   "admitted, none denied (8 Sep response). A party cannot admit a document's contents word-for-word "
   "and believe the document is a fake; the 14-tab authenticity dispute is a provenance column "
   "(\"copy from the Appellant's own records\"), not a fabrication allegation. The disputes die at "
   "one question - \"does the Regulator allege the document was fabricated?\" - whose only truthful "
   "answer is no. The conduct case is closed on the admissions plus the admitted negatives plus the "
   "CE letter (facts 263-268)."),
 p("<b>Pillar 2 - The acts are proved on paper, without witnesses.</b> My letter of 9 September "
   "fixed the footing: where a document is itself the step taken - a roster published, a directive "
   "issued, a report made, a reply given - the admission establishes the step was taken on that date "
   "in those terms. Facts 49, 66, 74-77, 81; 182-205, 210; 211-223; 263-268; and the clinical "
   "reports at 56-68 and 89-104 are established now, on the record, calling no one."),
 p("<b>Pillar 3 - The disputed tabs are inert and independently held.</b> The request letter's own "
   "schedule shows every operative line of the thirteen tabs is admitted, and names an independent "
   "holder for each - the Respondent's own List (Tab 6, item 25), the Commission's file (Tab 20), "
   "the Regulator's claim file (Tab 30), MSH's own RFMI attachment (Tab 1). None needs the "
   "Respondent's consent. Only Tab 31 is a production question, and fact 268 admits the spreadsheet "
   "\"is available.\""),
 p("<b>Pillar 4 - The medical schedule closes the last live element.</b> Causation "
   "(s 32(1) - employment \"a significant contributing factor\", never \"major\") was the only "
   "element left after conduct closed. The schedule builds it: a clean pre-morbid baseline (no prior "
   "psychological injury), work-timed onset at 18 June 2024, physiological corroboration, an unbroken "
   "referral-and-certificate spine, treating records keyed to admitted facts, and the treating "
   "doctors (Krishnaiah, Hawes) called to give the opinion orally (\"no report prepared for the "
   "proceeding\"). The one counter - a competing cause - is foreclosed: the relationship breakdown, "
   "if it post-dates onset, is sequela not cause, and the \"a significant\" test means a competing "
   "stressor does not defeat the claim unless it displaces employment as significant. That material "
   "stays outside the case and is never led."),
 p("<b>Pillar 5 - The defence roster is my cross-examination list, named back to them.</b> To rebut "
   "the outline the Respondent must call the actors behind the admitted acts - Taylor, Reese, the "
   "clinicians, the MSH officers - and every one answers under the CE letter and the admissions: each "
   "answer adopts the admissions or contradicts their own employer's signed letter. My 9 September "
   "letter names the point for them: the documents \"were sent by Ms Taylor or Ms Reese, whom the "
   "Appellant expects the Respondent to call.\" A party does not assemble 10-12 caged witnesses to "
   "lose in public.")]

# ---- The extension and the silence ----
S += [h1("4. Why the extension and the silence point the same way"),
 p("<b>The 10 September extension.</b> Requested on day one - the fastest reply in the file - for the "
   "last Friday before the Respondent's own 30 September deadline. The stated reason was a hearing "
   "week (capacity), which places the real work in the back half, 21-25 September: the same days the "
   "outline must be drafted. The 25th and the 30th are one decision in two documents, made by the "
   "same hands in the same week. And \"if needed reach out to MSH\" only makes sense if a branch "
   "exists where MSH is not needed - which is the concession branch alone, because constructing any "
   "defence outline runs through MSH for instructions and the war-game of who survives the cage."),
 p("<b>The employment-track silence.</b> MSH went silent across the employment track from ~11-12 "
   "September and missed its own deadline. The parsimonious explanation is a legal hold - route "
   "everything Shepherd-related through Legal pending the appeal position - which subordinates the "
   "employment track to the appeal. Ruttan (MSH Principal Lawyer) sat in the 7 August mention, so "
   "MSH Legal needs no briefing on why the appeal turned dangerous. The silence confirms the appeal "
   "is the master track; it does not by itself prove concession, because a defence build would freeze "
   "the same track.")]

# ---- The name signals ----
S += [h1("5. Why it resolves on names - the 30 September scorecard"),
 p("A letter's wording can be softened; a <b>filed witness list cannot</b> - it is a commitment "
   "device, names you can put in a box, on the record, under direction. MSH contact happens on both "
   "branches, so the 25 September letter's register is weak evidence of the decision. The names on "
   "the 30 September list are where the decision becomes visible.")]
S += [table(
 ["Name", "If named on the 30 Sep list", "If absent"],
 [["Ms Reese","conduct defence is being attempted - very unlikely (most caged; ¶219-221; absent from every 2026 communication)","conduct limb ceded - the strongest single concede signal"],
  ["Ms Taylor","broad outline = defending conduct; narrow / causation-only = limited","conduct ceded"],
  ["Clinicians (MASPER Registrar; Integrated Respiratory Service)","contesting the occurrence - they will not","occurrence conceded; the findings stand on the admissions"],
  ["Counsel (Willson / Gray) named in an appearance or outline","gearing for a contested hearing","no re-engagement = concede / settle track"]],
 [26, 77, 62])]
S += [p("<b>The rule:</b> a list with Reese on it = defend; a list with no MSH conduct witness = the "
   "conduct war is over, whatever the letter says. The 25th gives the register; the 30 September "
   "names give the decision.")]

# ---- Honest limits ----
S += [h1("6. The honest limits of the thesis"),
 p("(1) Distinguish three things that share the same name-absence signature: the thirteen tabs "
   "conceded (near-certain by the 30th), the appeal conceded outright (the endgame branch), and a "
   "narrowed causation-only corridor (still a defence, one-day medical hearing). A conduct-witness-"
   "free list confirms the conduct war is over but does not by itself split outright concession from "
   "a causation-only defence - the letter's register and any position sentence break that tie."),
 p("(2) Read specific absence (no Reese, no clinicians), not mere thinness - a placeholder or "
   "\"to be confirmed\" list can be a defensive filing."),
 p("(3) \"Built\" is not \"found\": the record makes the Respondent's loss rational to predict; a "
   "tribunal has not made any finding. The thesis is that this instrument makes conceding the "
   "Respondent's best move - engineered, not observed."),
 p("(4) The relationship material and the DFV attachments stay outside the case entirely and are "
   "not the basis of any conclusion here; the causation point rests on chronology and the statutory "
   "test alone.")]

S += [rule(), p("Prediction and internal-analysis document. Not served, filed, or sent. "
   "Sources: the served PDFs of 9 September 2026, the Regulator's responses and letters of 8 and "
   "10 September 2026, and the correspondence on the file as listed in section 2.", SUB)]

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=16*mm, rightMargin=14*mm,
                        topMargin=14*mm, bottomMargin=14*mm,
                        title="", author="", subject="", creator="")
doc.build(S)

# strip metadata
pdf = pikepdf.open(OUT, allow_overwriting_input=True)
with pdf.open_metadata() as m:
    for k in list(m.keys()): del m[k]
di = pdf.docinfo
for k in list(di.keys()): del di[k]
pdf.save(OUT)
pdf.close()
print("wrote", OUT)
