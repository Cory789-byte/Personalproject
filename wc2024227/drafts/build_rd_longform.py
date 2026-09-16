#!/usr/bin/env python3
"""WC/2024/227 - Review Decision 69983: the reasoning re-run long form, 22 August 2026.

INTERNAL WORKING DOCUMENT. Not for service, not for filing, not for circulation.

Re-runs the question "does the dissection, taken with the drafting question, make a clear case?"
from first principles, and corrects an argument advanced in conversation on 22 August 2026 that
had already been tested and downgraded in HOPGOODGANIM-QUESTION.md Part 8.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/RD69983_REASONING_LONGFORM.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13.5, leading=17, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11, leading=14,
                     spaceBefore=10, spaceAfter=4)
H3  = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=9.4, leading=12,
                     spaceBefore=6, spaceAfter=2)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.1, leading=12.8, spaceAfter=5)
Q   = ParagraphStyle('Q', parent=B, leftIndent=8*mm, rightIndent=6*mm,
                     textColor=colors.HexColor('#222222'), fontName='Helvetica-Oblique')
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

def box(title, body, bg='#fbeaea', line='#a33'):
    rows = [[P(title, ParagraphStyle('bt', parent=B, fontName='Helvetica-Bold',
                                     textColor=colors.HexColor('#7a1414')))],
            [P(body, ParagraphStyle('bb', parent=B, fontSize=8.7))]]
    t = Table(rows, colWidths=[178*mm])
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.8,colors.HexColor(line)),
        ('BACKGROUND',(0,0),(-1,-1),colors.HexColor(bg)),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return t

st = [P("Review Decision 69983 &mdash; the reasoning, re-run long form", H1),
      P("WC/2024/227 &middot; 22 August 2026 &middot; internal working document &middot; not for "
        "service, filing or circulation", SUB)]

# ---------------------------------------------------------------- Part 1
st.append(P("Part 1 &mdash; A correction, made first", H2))
st.append(box("An argument I ran on 22 August 2026 was already tested and downgraded in this file",
  "In conversation I argued that the thinness of the decision cuts <i>against</i> external "
  "drafting: that a commercial firm being paid to produce reasons would have cited current "
  "authority and would have insisted on documentary foundations, because appeal risk is its "
  "professional exposure. <b>That argument had already been made in this file and already "
  "weakened, at HOPGOODGANIM-QUESTION.md &sect;8.3, for a reason I did not take into account.</b>"))
st.append(P("The reason is the <b>identity of the authorities selected</b>, not their age. "
            "<i>Delaney</i> [2005] QIC 11, <i>Prizeman</i> [2005] QIC 53, <i>Bowers</i> [2002] QIC "
            "18 and <i>Rowe</i> [2009] QIRC 9 are all management-action cases in the "
            "insurer-favourable line. <b><i>Mahaffey</i> [2016] ICQ 10 &mdash; the leading "
            "appellate authority on s 32(5)(a), and the one most useful to a worker on the "
            "whole-course-of-conduct point &mdash; is absent.</b>", B))
st.append(P("A selection of older insurer-favourable authorities with the leading worker-favourable "
            "case missing is not proof of anything. But it is not the exculpatory fact I treated it "
            "as. <b>A precedent bank is exactly what a firm working to a fixed fee would use.</b> "
            "The competence argument does not survive in the form I put it.", B))
st.append(P("The file's own honest position, at &sect;8.5, is: <b>&ldquo;I no longer have a strong "
            "argument against his theory. What I have is no proof of it.&rdquo;</b> That remains "
            "the position. What follows re-runs the question from there rather than from where I "
            "restarted it.", B))

# ---------------------------------------------------------------- Part 2
st.append(P("Part 2 &mdash; The two findings, stated at their exact limits", H2))
rows = [[P("", CH), P("What is established", CH), P("What is not", CH)]]
rows.append([P("<b>A</b><br/>The provenance finding", C),
  P("The Word file from which this PDF was generated was saved at least once on a workstation "
    "running HopgoodGanim's document management integration, and was profiled to matter 2440758 "
    "with a description accurate to this document. The unresolved merge placeholders exclude both "
    "a stale template and manual typing. You cannot PDFMaker-for-Word an incoming PDF, so the "
    "source was held in Word in that environment.", C),
  P("<b>Who drafted it. Who paid. Whether Ms Squires exercised her own judgment.</b> The metadata "
    "fixes where the file was profiled and when it became a PDF. It does not fix authorship and "
    "nothing in the file will.", C)])
rows.append([P("<b>B</b><br/>The evidence audit", C),
  P("Six findings rest on an assertion by the employer with no underlying document identified in "
    "the reasons. Three of the Appellant's own assertions were rejected expressly for want of "
    "documents. Four of the six are now answered or materially qualified by documents the employer "
    "or the Respondent produced in 2026, none before the reviewer.", C),
  P("That the review was unlawful, or that the decision is invalid. Thin fact-finding is not "
    "invalidity, and on a de novo appeal it is not a ground of anything.", C)])
t = Table(rows, colWidths=[26*mm, 84*mm, 68*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
st.append(t)

# ---------------------------------------------------------------- Part 3
st.append(P("Part 3 &mdash; The hypothesis under test, at its strongest", H2))
st.append(P("Stated as strongly as the material allows, the proposition is not &ldquo;a law firm "
            "wrote the decision.&rdquo; It is this:", B))
st.append(P("&ldquo;A document produced in a firm's Word environment, profiled to that firm's "
            "matter number thirteen days before the decision issued, decided six central questions "
            "on the employer's unverified word, cited four authorities all in the insurer-favourable "
            "line, omitted the one leading authority that would have defeated the result, conceded "
            "generously at factor level, and then preserved the rejection at the aggregation "
            "step.&rdquo;", Q))
st.append(P("That is a coherent hypothesis and it deserves to be tested rather than dismissed. What "
            "follows tests it.", B))

# ---------------------------------------------------------------- Part 4
st.append(P("Part 4 &mdash; The aggregation step, which is where the outcome was actually decided", H2))
st.append(P("This is the part of the reasoning that matters most, and it is independent of who "
            "drafted anything.", B))
st.append(P("The Conclusion at p 27 records four determinations: a personal injury of a "
            "psychological nature was sustained; it arose out of employment to the extent it arose "
            "out of <b>factors 2, 3 and 4</b>, where employment was <b>&ldquo;a significant "
            "contributing factor&rdquo;</b>; factors 2 and 3 amounted to reasonable management "
            "action; and <b>factor 4 amounted to unreasonable management action</b>. <i>Delaney</i> "
            "is then applied and the rejection confirmed &mdash; <b>&ldquo;it was only the one "
            "incident which amounted to unreasonable management action.&rdquo;</b>", B))
st.append(P("Two features of that step are worth isolating.", B))
st.append(P("(i) The concessions cost nothing", H3))
st.append(P("Factor 3 was substantiated where WorkCover had found it not substantiated. Factor 4 "
            "was found unreasonable where WorkCover had found it reasonable. Both departures went "
            "against WorkCover &mdash; and <b>neither altered the result</b>, because the result "
            "was preserved at the aggregation step. Conceding at component level while protecting "
            "the outcome at the aggregation step is not, by itself, evidence of anything; but it is "
            "not evidence of independence either, which is how it was read in this file before "
            "8 August 2026.", B))
st.append(P("(ii) Factor 2 was substantiated <i>against</i> him, and still counted", H3))
st.append(P("The factor 2 finding at p 12 is: <b>&ldquo;this factor is able to be substantiated to "
            "the extent that you lodged a complaint, and some action was taken by management to "
            "review it, <i>but not to the extent that there was no response to it</i>.&rdquo;</b> "
            "That is a finding that rejects the allegation. It was nonetheless carried into the "
            "Conclusion as one of the factors the injury arose out of, and so into the pool across "
            "which the global evaluation was performed.", B))
st.append(P("<b>The effect is arithmetic.</b> A factor decided against the worker enlarges the "
            "denominator. One unreasonable act among three sounds smaller than one among two. The "
            "sentence &ldquo;only the one incident&rdquo; is doing the work of the decision, and it "
            "is measured against a pool that includes a factor which was not made out.", B))

# ---------------------------------------------------------------- Part 5
st.append(P("Part 5 &mdash; Where the evidence audit joins the aggregation step", H2))
st.append(P("This is the connection that was not visible until today, and it is the reason the "
            "audit matters.", B))
st.append(P("The two factors that made the aggregation work &mdash; factors 2 and 3, both found "
            "<b>reasonable</b> &mdash; are the two carried by the assertion-based findings. Factor "
            "2 rests on the employer's account of the Ethical Standards Unit process and of the "
            "Appellant's asserted refusal to participate, with no Unit file and no record of the "
            "contact attempts obtained. Factor 3 rests on the employer's statement that corrective "
            "action was taken, from which the reviewer found the pay issues <b>&ldquo;ultimately "
            "were all resolved&rdquo;</b> and management <b>&ldquo;always encouraging&hellip; "
            "attentive&rdquo;</b> &mdash; with no payroll correspondence, no claim record and no "
            "payslip obtained.", B))
st.append(P("Both are now met by documents in hand. Payroll wrote to the Appellant on <b>13 May "
            "2024</b>: <i>&ldquo;I cannot see that any of the issues below have been "
            "corrected.&rdquo;</i> The employer's own myHR report records the correction claim of "
            "28 May 2024 as <b>&ldquo;Part Completed&rdquo;</b>, the only one of five not "
            "completed. Ms Forrest's letter of 7 July 2026 states the 2020 agreement <b>&ldquo;is "
            "only applied where staff initiated shift swaps have occurred&rdquo;</b> &mdash; and "
            "the shifts of 17 and 18 March 2024 were rostered.", B))
st.append(box("The proposition that actually follows, and it needs no theory of authorship",
  "The rejection was preserved at the aggregation step. The aggregation step counted three "
  "factors. One of the three was decided against the Appellant. The other two were found "
  "reasonable on the employer's unverified word, and the documents that answer them were produced "
  "in 2026 and were not before the reviewer. <b>That is a complete account of why the review "
  "reaching a rejection does not dispose of the appeal &mdash; and it does not require anyone to "
  "have drafted anything.</b>", '#eef3ee', '#4a7'))

# ---------------------------------------------------------------- Part 6
st.append(P("Part 6 &mdash; The chain of inference, tested link by link", H2))
rows = [[P("Theory", CH), P("Link", CH), P("Holds?", CH)]]
CHAIN = [
 ("Drafting", "1. The Word file passed through the firm's DMS", "YES - established"),
 ("Drafting", "2. Therefore the firm drafted the reasons", "NO - equally consistent with the firm holding, receiving or assisting with the file; not distinguishable from the artefacts"),
 ("Drafting", "3. Therefore the decision-maker did not apply her own mind", "NO - not established, and metadata cannot establish it"),
 ("Drafting", "4. Therefore the decision is invalid", "NO - requires link 3"),
 ("Drafting", "5. Therefore the Appellant is better off", "NO - de novo under s 550(4); invalidity gains nothing the appeal does not already offer"),
 ("Audit", "1. Six findings rest on employer assertion with no document identified", "YES - on the face of the reasons"),
 ("Audit", "2. Four are now answered by documents produced since", "YES - documents held, all from the employer or the Respondent"),
 ("Audit", "3. Those findings carried factors 2 and 3, which carried the aggregation", "YES - Conclusion p 27 and the Delaney passage"),
 ("Audit", "4. Therefore the appeal proceeds on a materially different record", "YES - which is what a hearing de novo is for"),
]
for a, b, c in CHAIN:
    rows.append([P(a, C), P(b, C), P(c, C)])
t = Table(rows, colWidths=[20*mm, 74*mm, 84*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
for i,(a,b,c) in enumerate(CHAIN, start=1):
    if c.startswith('NO'): sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#fbeaea')))
    else: sty.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#eef3ee')))
t.setStyle(TableStyle(sty))
st.append(t)
st.append(Spacer(1,2*mm))
st.append(P("<b>One chain breaks at link 2 and never recovers. The other holds at every link.</b> "
            "They are not additive: joining an unproven premise to a proven one does not strengthen "
            "the unproven one, it imports its weakness into the proven one.", B))

# ---------------------------------------------------------------- Part 7
st.append(P("Part 7 &mdash; What survives, and the reliance argument that works either way", H2))
st.append(P("The finding the Appellant relies on is safe on <b>either</b> account of who drafted "
            "the reasons, and that is the reason to stop testing the question:", B))
st.append(P("If the decision was the Regulator's own work, then the Regulator's own delegate found "
            "the rostering of 17 and 18 March 2024 amounted to unreasonable management action, that "
            "the Appellant sustained a personal injury of a psychological nature, and that "
            "employment was <b>a significant contributing factor</b>. <b>And if it was drafted with "
            "assistance retained in the insurer's interest, then even that document conceded those "
            "three things.</b>", B))
st.append(P("The second cannot be proved. So the first is what is run. But the concession is good "
            "on either footing, which is precisely why it should be relied on and the decision not "
            "attacked.", B))

# ---------------------------------------------------------------- Part 8
st.append(P("Part 8 &mdash; What would actually move it", H2))
st.append(P("Not further inference from the artefacts. Two things, in order of cost:", B))
st.append(P("<b>1. Queensland Government contract disclosure.</b> OIR publishes awarded contracts "
            "over $10,000 on data.qld.gov.au. Public, free, asks nobody, creates no exposure. A "
            "small drafting engagement may fall below the threshold, so a nil result proves nothing "
            "&mdash; but a positive result would be decisive and costs an afternoon.", B))
st.append(P("<b>2. The one neutral question</b>, already settled in this file at &sect;7.8 and still "
            "unsent: <i>&ldquo;For completeness of the record, please confirm whether any external "
            "legal service provider was engaged in connection with review 69983 &mdash; as distinct "
            "from this appeal &mdash; and if so, by which entity and under which panel or "
            "procurement arrangement.&rdquo;</i> No firm named, no allegation, answerable without "
            "waiving privilege.", B))
st.append(P("&#9888; Neither is a priority before 4.00 pm on 9 September 2026. The witness outlines "
            "decide this appeal. Nothing in Parts 1 to 7 does.", W))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - RD69983 reasoning long form - internal, not for service")
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
