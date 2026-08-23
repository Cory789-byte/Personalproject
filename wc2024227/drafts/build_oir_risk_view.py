#!/usr/bin/env python3
"""WC/2024/227 - the provenance question assessed from the Regulator's side of the table.

INTERNAL WORKING DOCUMENT. Not for service, filing or circulation.
Written in the Regulator's voice as a risk assessment: what OIR would fear, what OIR knows that
the Appellant does not, and what OIR would do if the question were ventilated at hearing.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/OIR_RISK_VIEW_provenance_at_hearing.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.6, leading=13.5,
                     spaceBefore=9, spaceAfter=4)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.1, leading=12.6, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

st = [P("The provenance question, assessed from the Regulator's side", H1),
      P("WC/2024/227 &middot; 22 August 2026 &middot; internal working document &middot; written in "
        "the Regulator's voice as a risk assessment &middot; not for service", SUB)]

st.append(P("1. The asymmetry that governs everything", H2))
st.append(P("The Regulator knows the answer. It knows whether an external provider was engaged in "
            "connection with review 69983, by whom, and under what arrangement. The Appellant does "
            "not, and cannot find out from the artefacts. <b>Every assessment below turns on which "
            "of three states of the world is true, and only the Regulator knows which.</b>", B))

rows = [[P("If the truth is&hellip;", CH), P("The Regulator's exposure", CH), P("The Regulator's posture", CH)]]
SCEN = [
 ("<b>A.</b> No external provider was engaged. The DMS profile has some other explanation - the "
  "file passed through the firm on some other footing.",
  "<b>Nil.</b> One sentence disposes of it. The Appellant is left having implied something that is "
  "not so, on the record.",
  "Answer plainly and early. Invite the question. The answer is free and it closes a line of "
  "attack permanently.", 0),
 ("<b>B.</b> An engagement existed, procured through a whole-of-government panel, properly "
  "authorised, the Regulator instructing.",
  "<b>Low, and legal exposure nil.</b> Receiving drafting assistance is orthodox. The delegate "
  "signed; s 329 is satisfied on the face. Mild institutional embarrassment only.",
  "Answer if asked directly, in writing, in neutral terms. Do not volunteer. There is nothing to "
  "concede because nothing was done wrong.", 1),
 ("<b>C.</b> An engagement existed on a footing that is awkward - a provider also acting in the "
  "insurer's interest, or an arrangement not disclosed, or structured below the $10,000 "
  "publication threshold.",
  "<b>Material, and it is not legal - it is institutional.</b> The exposure is a public transcript, "
  "a precedent for every other appellant to ask the same question, and scrutiny of procurement "
  "practice. None of it decides this appeal.",
  "Resist ventilation at hearing on relevance. Answer correspondence at the highest level of "
  "generality consistent with accuracy. Settle if the cost of settling is lower than the cost of "
  "the question being asked in open session.", 2),
]
for a, b, c, _wt in SCEN:
    rows.append([P(a, C), P(b, C), P(c, C)])
t = Table(rows, colWidths=[58*mm, 60*mm, 60*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]
sty.append(('BACKGROUND',(0,3),(-1,3),colors.HexColor('#f6ecec')))
t.setStyle(TableStyle(sty))
st.append(t)
st.append(Spacer(1,2*mm))
st.append(P("<b>The Regulator's silence is therefore not evidence of scenario C.</b> A body in "
            "scenario B has no reason to volunteer an answer to a question nobody has formally put, "
            "and a body in scenario A has no reason to answer a question that has not been asked "
            "either. Only a direct, answerable question discriminates between the three.", B))

st.append(P("2. How the question could actually reach the hearing, and what happens to it", H2))
rows = [[P("Route", CH), P("What the Regulator does", CH), P("Outcome", CH)]]
ROUTES = [
 ("Tendering the document properties as an exhibit",
  "Objection: relevance. The appeal is de novo under s 550(4). The manner in which the reasons "
  "below were produced is not a fact in issue in determining whether the Appellant sustained an "
  "injury under s 32.",
  "<b>Objection almost certainly upheld.</b> The metadata is not probative of any element."),
 ("Cross-examination of a Regulator witness",
  "The Regulator is unlikely to call a witness to whom the question could be put. The review "
  "decision is a document; it proves itself. There may be no witness available to cross-examine on "
  "its production at all.",
  "<b>No vehicle.</b> The question needs a witness and there may not be one."),
 ("Submissions",
  "Object, or simply respond that it goes to no issue and invite the Commission to decide the "
  "matter on the evidence.",
  "<b>Rejected as a ground.</b> There is no ground for it to attach to."),
 ("Correspondence before hearing",
  "Answer, decline, or answer at a level of generality. Whatever is written becomes a record.",
  "<b>The only route that produces anything.</b> An answer closes it; a refusal in writing is "
  "itself a document."),
]
for a, b, c in ROUTES:
    rows.append([P(a, C), P(b, C), P(c, C)])
t2 = Table(rows, colWidths=[46*mm, 76*mm, 56*mm], repeatRows=1)
t2.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
    ('BACKGROUND',(0,4),(-1,4),colors.HexColor('#eef3ee'))]))
st.append(t2)

st.append(P("3. What the Regulator would want the Appellant to do", H2))
st.append(P("Assessed candidly from the other side of the table, an experienced appeals officer "
            "would not fear this line. She would prefer it were run, for four reasons:", B))
st.append(P("<b>(a) It is a relevance objection she wins</b>, in front of the Commissioner, early, "
            "and it sets the tone for everything after it.", B))
st.append(P("<b>(b) It converts a documentary case into a character impression.</b> A "
            "self-represented appellant advancing a theory about how the decision below was "
            "produced reads as grievance rather than proof, whatever the merits.", B))
st.append(P("<b>(c) It opens the reliance contradiction.</b> The Appellant pleads the review "
            "finding at Stressor 3(d) and relies on it as the considered conclusion of the "
            "Regulator's own delegate. If he also says the decision was produced elsewhere, the "
            "answer writes itself: <i>the Appellant does not accept the independence of the very "
            "finding he asks the Commission to adopt.</i>", B))
st.append(P("<b>(d) It opens two documents that presently sit unread.</b> Putting the review's "
            "integrity in issue invites the Respondent to put the Appellant's own characterisations "
            "back to him - his email of 15 May 2024 alleging <i>&ldquo;fraudulent practices&rdquo;</i>, "
            "and the Line Manager's account to Human Resources of 17 May 2024. Both are already in "
            "the Respondent's disclosure. Neither has any reason to be opened unless the Appellant "
            "supplies one.", W))

st.append(P("4. What is actually exposed, and what is not", H2))
rows = [[P("", CH), P("At hearing", CH)]]
EXP = [
 ("The document properties", "Exposed only if tendered, and objectionable if tendered. They prove "
  "where a Word file was profiled. They do not prove authorship, payment, or that the delegate did "
  "not decide."),
 ("Whether an engagement existed", "<b>Not exposed at hearing.</b> Exposed only by a written "
  "question answered in writing, or by contract disclosure on data.qld.gov.au."),
 ("The identity of hendry8286", "<b>Not exposed, and probably anticlimactic.</b> A document "
  "management username records who was logged in when a file was saved - in a law firm that is "
  "routinely support staff."),
 ("Procurement and panel arrangements", "Not exposed at hearing. Exposed by contract disclosure or "
  "a Right to Information application, neither of which is a hearing process."),
 ("The Appellant's own characterisations", "<b>Exposed the moment the review's integrity is put in "
  "issue</b>, and not before."),
]
for a, b in EXP:
    rows.append([P(f"<b>{a}</b>", C), P(b, C)])
t3 = Table(rows, colWidths=[52*mm, 126*mm], repeatRows=1)
t3.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
    ('BACKGROUND',(0,5),(-1,5),colors.HexColor('#f6ecec'))]))
st.append(t3)

st.append(P("5. The one place the Regulator is genuinely exposed", H2))
st.append(P("Not the hearing. <b>Correspondence.</b> A single neutral question, properly framed, "
            "must be answered, declined, or deflected - and each of those is a written record that "
            "did not exist before. That is the only mechanism in this matter that compels the "
            "Regulator to convert its private knowledge into something on the file.", B))
st.append(P("The question already settled for this purpose, unsent:", B))
st.append(P("<i>&ldquo;For completeness of the record, please confirm whether any external legal "
            "service provider was engaged in connection with review 69983 - as distinct from this "
            "appeal - and if so, by which entity and under which panel or procurement "
            "arrangement.&rdquo;</i>",
            ParagraphStyle('q', parent=B, leftIndent=8*mm, fontName='Helvetica-Oblique')))
st.append(P("It names no firm, alleges nothing, and can be answered without waiving privilege - so "
            "a refusal to answer it is harder to justify than a refusal to answer an accusatory "
            "one. <b>In scenario A it is answered in a line. In scenario B it is answered in two. "
            "A non-answer is the only outcome that tells the Appellant anything, and it tells him "
            "only that the question is worth having asked.</b>", B))

st.append(P("6. Settlement, from the Regulator's side", H2))
st.append(P("A regulator does not settle to avoid procedural embarrassment the way a commercial "
            "party might; it has no shareholders and its officers are not personally exposed. The "
            "realistic assessment is that this question moves settlement <b>little on its own</b>.", B))
st.append(P("What moves settlement is the merits: an admitted seven-hour break, an admitted "
            "twenty-five day delay, the employer's own Chief Executive confirming no fatigue "
            "framework existed before 30 June 2024, and the Regulator's own delegate having found "
            "unreasonable management action and employment a significant contributing factor. "
            "<b>Those are strong and they are unanswerable. The provenance question is neither.</b>", B))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - OIR risk view - internal working document, not for service")
    cv.drawRightString(PW-16*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=15*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, PW-32*mm, PH-31*mm)],
                                   onPage=foot)])
doc.build(st)
buf.seek(0)
p = pikepdf.open(buf)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(p.pages)}")
