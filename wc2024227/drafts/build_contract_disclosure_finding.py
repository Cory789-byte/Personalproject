#!/usr/bin/env python3
"""WC/2024/227 - the contract disclosure search, 23 August 2026.

Searched Queensland Government open data (data.qld.gov.au) for engagements between the Office of
Industrial Relations and HopgoodGanim Lawyers. Retrieved via the CKAN datastore API; direct file
downloads were blocked by the network proxy, which is why the WorkCover side could not be checked.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/CONTRACT_DISCLOSURE_FINDING_23Aug2026.pdf"
PW, PH = A4
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.6, leading=13.5,
                     spaceBefore=9, spaceAfter=4)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.1, leading=12.6, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.3, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
W   = ParagraphStyle('W', parent=B, textColor=colors.HexColor('#8a1c1c'))
def P(t, s=B): return Paragraph(t, s)

st = [P("Contract disclosure search &mdash; Office of Industrial Relations and HopgoodGanim Lawyers", H1),
      P("WC/2024/227 &middot; searched 23 August 2026 &middot; Queensland Government open data, "
        "data.qld.gov.au &middot; public record, no request made of anyone", SUB)]

st.append(P("The finding", H2))
st.append(P("<b>HopgoodGanim Lawyers is an established, continuing legal services supplier to the "
            "Office of Industrial Relations itself.</b> Across every published disclosure period "
            "there are <b>76 separate engagements totalling approximately $1.84 million</b>, each "
            "recorded with the supplier name &ldquo;HOPGOOD GANIM LAWYERS&rdquo;, address &ldquo;L 8 "
            "1 Eagle St Brisbane&rdquo;, agency &ldquo;Office of Industrial Relations&rdquo;, and "
            "description &ldquo;Legal Services&rdquo;.", B))

rows = [[P("Period", CH), P("Engagements", CH), P("Value", CH), P("", CH)]]
FY = [
 ("FY2020-21", "12", "$316,030.00", ""),
 ("FY2021-22", "6", "$125,840.00", ""),
 ("FY2022-23", "31", "$653,215.00", ""),
 ("FY2023-24 (Jul-Nov)", "19", "$492,660.30", ""),
 ("<b>FY2024-25 Jul-Sept</b>", "<b>6</b>", "<b>$196,580.00</b>",
  "<b>Includes 2 October 2024, $13,200 &mdash; 22 days before the review decision</b>"),
 ("<b>FY2024-25 Oct-Dec</b>", "<b>2</b>", "<b>$58,052.50</b>",
  "2 December and 12 December 2024 &mdash; after the decision"),
 ("<b>Total</b>", "<b>76</b>", "<b>$1,842,377.80</b>", ""),
]
for a,b,c,d in FY:
    rows.append([P(a, C), P(b, C), P(c, C), P(d, C)])
t = Table(rows, colWidths=[36*mm, 22*mm, 30*mm, 90*mm], repeatRows=1)
sty = [('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
       ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
       ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
       ('BACKGROUND',(0,5),(-1,5),colors.HexColor('#eef3ee')),
       ('BACKGROUND',(0,7),(-1,7),colors.HexColor('#eeeeee'))]
t.setStyle(TableStyle(sty))
st.append(t)

st.append(P("What it does to the question", H2))
st.append(P("The concern was structural: HopgoodGanim appearing on the Regulator's decision was "
            "read as the <i>insurer's</i> firm having had a hand in the review of the insurer's own "
            "decision, which would compromise the independence the process advertises at page 2 of "
            "the decision &mdash; <i>&ldquo;an independent administrative process&rdquo;</i>.", B))
st.append(P("<b>The public record answers that in the other direction.</b> HopgoodGanim is engaged "
            "by the Office of Industrial Relations directly, routinely, matter by matter, and was "
            "engaged in the weeks either side of this review. An engagement dated <b>2 October "
            "2024</b> sits one week before the document management record on the decision, which is "
            "dated <b>09.10.2024</b>, and twenty-two days before the decision issued on 24 October "
            "2024.", B))
st.append(P("On that footing the document management profile has an ordinary explanation with "
            "public documentary support: <b>the Regulator obtained legal assistance from its own "
            "regular supplier, and the file was produced in that supplier's Word environment.</b> "
            "That is lawful. A decision-maker may receive drafting assistance provided she applies "
            "her own mind; the delegate signed, and she is a public service employee, so the "
            "delegation under s 329 is proper on its face.", B))

st.append(P("The limits, stated exactly", H2))
st.append(P("<b>1. No engagement can be tied to review 69983.</b> Every entry is described only as "
            "&ldquo;Legal Services&rdquo;. None carries a matter reference, and none can be matched "
            "to matter 2440758 or to this review.", B))
st.append(P("<b>2. The WorkCover side could not be checked.</b> WorkCover Queensland publishes its "
            "own contract disclosure, but those resources have no datastore and the direct file "
            "downloads were blocked by the network proxy in this session. <b>Whether HopgoodGanim "
            "also acts for WorkCover is therefore still unknown.</b> If it does, a conflict question "
            "could still arise &mdash; but it would be a matter-specific question about this claim, "
            "not the structural one, and nothing in the metadata reaches it.", B))
st.append(P("<b>3. Engagements under $10,000 are not published</b>, so the absence of a particular "
            "entry proves nothing.", B))
st.append(P("<b>4. This still does not establish who decided.</b> The limit recorded throughout the "
            "file is unchanged: the metadata fixes where a Word file was profiled and when it became "
            "a PDF. It does not fix authorship, and the contract record does not either.", B))

st.append(P("Where this leaves the question", H2))
st.append(P("The strongest remaining form of the concern was that a firm acting in the insurer's "
            "interest had a hand in reviewing the insurer's decision. <b>That form of it is now "
            "substantially answered by the public record</b>, and answered by a source that cost "
            "nothing, asked nobody, and creates no exposure &mdash; which is why it was the step "
            "recommended in the file at HOPGOODGANIM-QUESTION.md &sect;8.7.", B))
st.append(P("The one thing that would close it completely is the same neutral question, still "
            "unsent: whether an external legal service provider was engaged in connection with "
            "<b>review 69983</b>, by which entity and under which arrangement. On this record the "
            "expected answer is now &ldquo;yes, by the Regulator, under its standing arrangement "
            "with HopgoodGanim&rdquo; &mdash; which is a complete and unremarkable answer.", B))
st.append(P("&#9888; <b>The reliance argument is unaffected and should be run unchanged.</b> The "
            "Regulator's own delegate found the rostering of 17 and 18 March 2024 amounted to "
            "unreasonable management action, that a personal injury of a psychological nature was "
            "sustained, and that employment was a significant contributing factor. That is worth "
            "more than anything in this document.", W))

st.append(P("Method, for the record", H2))
st.append(P("Retrieved 23 August 2026 from the Queensland Government open data portal via its CKAN "
            "API (<font face='Courier' size=7.6>datastore_search</font>), across the datasets "
            "&ldquo;Office of Industrial Relations Contracts Disclosure Report&rdquo; and the "
            "separate FY2024-25 quarterly datasets. Query term &ldquo;hopgood&rdquo;; results "
            "filtered on the supplier name field. Direct CSV and XLSX downloads returned HTTP 202 "
            "with an empty body through the session proxy, so the WorkCover Queensland disclosure "
            "could not be searched by the same method.", C))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "WC/2024/227 - contract disclosure finding - 23 August 2026")
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
