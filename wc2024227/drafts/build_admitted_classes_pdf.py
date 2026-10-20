#!/usr/bin/env python3
"""All 298 admitted facts, classified by whether the 8 Sep cover letter's
document qualification can reach them. Internal reference PDF."""
import io, os, re, sys, pikepdf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from served_facts import FACT as F, NOT_ADMITTED
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "INTERNAL",
                   "ADMITTED_FACTS_CLASSIFIED_14SEP2026.pdf")
WORLD = {14,62,63,64,68,88,92,96,102,103,124,125,179,227,249}

def classify(n, t):
    low = t.lower()
    if re.search(r'does not allege|does not list|does not identify|does not describe|nor does|does not state', low):
        return "B"
    if n in WORLD:
        return "A"
    if re.match(r'^(on |by (email|letter)|between )', low) and re.search(r'\b(sent|replied|wrote|forwarded|provided|approved|made|lodged|served)\b', low):
        return "C"
    if re.search(r'^that |states|records|recorded|quotes', low):
        return "D"
    return "E"

LABEL = {
 "A": ("A - FACTS ABOUT THE WORLD",
       "Events, acts, states and arithmetic, admitted as true in themselves. No document is asserted, so the cover letter's qualification ('admissions as to documents are limited to existence and wording') cannot reach them. Nothing to tender; taken as admitted."),
 "B": ("B - THE ADMITTED GAPS",
       "Facts about the state of the Respondent's own pleading and List of Documents. Not admissions as to documents; not touched by any reservation. The absences are themselves admitted."),
 "C": ("C - ACTS OF COMMUNICATION",
       "'On [date] X sent/wrote/replied...' Each admits the ACT - sender, recipient, date, time - which is an event. Where the fact also quotes words, the wording is admitted with it. The footing letter (9 Sep, para 2) rests on exactly this: the document is the step taken."),
 "D": ("D - CONTENTS OF DOCUMENTS",
       "'That email states... / That decision records...' Existence and wording admitted. This is the ONLY class the cover letter's qualification addresses, and the footing letter answers it: operative documents are relied on as the acts (para 2); documents recording others' statements come in with their authors (para 3)."),
 "E": ("E - DOCUMENT IDENTITY AND OTHER",
       "What a document IS (a role description, a register, a thread), plus residual facts. Identity admitted; pairs with class D."),
}

REPL = {"—":" - ", "–":"-", "…":"...", "‘":"'", "’":"'", "“":'"', "”":'"'}
def clean(t):
    for k, v in REPL.items(): t = t.replace(k, v)
    t = t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    try: t.encode("latin-1")
    except UnicodeEncodeError: t = t.encode("latin-1","replace").decode("latin-1")
    return t

H1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=12.5, leading=15, spaceAfter=4)
H2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceBefore=9, spaceAfter=2)
BODY = ParagraphStyle('b', fontName='Helvetica', fontSize=8.4, leading=11, spaceAfter=3)
NOTE = ParagraphStyle('n', parent=BODY, textColor=colors.HexColor('#555555'), fontSize=7.9)
CELL = ParagraphStyle('c', fontName='Helvetica', fontSize=7.4, leading=9.4)
CELLB = ParagraphStyle('cb', parent=CELL, fontName='Helvetica-Bold')

groups = {k: [] for k in "ABCDE"}
for n in sorted(F):
    if n in NOT_ADMITTED: continue
    groups[classify(n, F[n])].append(n)

story = [Paragraph("THE 298 ADMITTED FACTS, CLASSIFIED", H1),
         Paragraph("WC/2024/227 - which facts the Respondent's cover letter of 8 September 2026 can even address, and which it cannot. "
                   "Internal working document, 14 September 2026. <b>NOT FOR SERVICE OR FILING.</b>", NOTE),
         Spacer(1, 3),
         Paragraph("Classes A and B (%d facts) assert no document: no qualification reaches them and nothing is tendered - they are simply taken as admitted (r 49). "
                   "Class C (%d facts) admits acts of communication - events - with wording alongside. Classes D and E (%d facts) are the only ground the cover letter's "
                   "qualification addresses, and the footing letter of 9 September answers it in terms." % (
                   len(groups['A'])+len(groups['B']), len(groups['C']), len(groups['D'])+len(groups['E'])), BODY),
         Spacer(1, 5)]

for k in "ABCDE":
    title, desc = LABEL[k]
    story.append(Paragraph("%s (%d facts)" % (title, len(groups[k])), H2))
    story.append(Paragraph(desc, NOTE))
    rows = [[Paragraph("<b>&para;</b>", CELLB), Paragraph("<b>The admitted fact</b>", CELLB)]]
    for n in groups[k]:
        rows.append([Paragraph(str(n), CELL), Paragraph(clean(F[n]), CELL)])
    t = Table(rows, colWidths=[11*mm, 169*mm], repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#b5b5b5')),
                           ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef1f6')),
                           ('VALIGN',(0,0),(-1,-1),'TOP'),
                           ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
                           ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]))
    story += [t, Spacer(1, 4)]

story.append(Paragraph("THE POINT", H2))
story.append(Paragraph("%d of the 298 admitted facts (classes A, B and C) stand with no dependence on the cover letter's document qualification: "
    "they admit the world, the gaps and the acts. The qualification's whole territory is classes D and E - and there the footing letter has "
    "already stated the reliance (acts, not truth; authors called for the rest), so the reservation has nothing left to bite on. "
    "The authenticity dispute of fourteen tabs touches none of this: facts are taken as admitted without any tender at all." % (
    len(groups['A'])+len(groups['B'])+len(groups['C'])), BODY))

buf = io.BytesIO()
SimpleDocTemplate(buf, pagesize=A4, leftMargin=13*mm, rightMargin=13*mm,
                  topMargin=12*mm, bottomMargin=12*mm).build(story)
buf.seek(0)
pdf = pikepdf.open(buf)
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
print("built", OUT, len(pikepdf.open(OUT).pages), "pages",
      {k: len(v) for k, v in groups.items()})
