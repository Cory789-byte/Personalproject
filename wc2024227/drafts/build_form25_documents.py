#!/usr/bin/env python3
"""WC/2024/227 - Form 25: Notice to admit documents (r 49, authenticity limb).

Served ALONGSIDE the second Form 24 notice to admit facts. The approved form for
document authenticity is Form 25 - Notice to admit documents (Version 4.1); the
schedule in the Form 24 remains as a cross-reference only.

The schedule below is generated from the Annexure A ITEMS in
build_form24_annexureA.py, so the two documents can never drift apart.

⛔ BEFORE SERVICE: download the current Form 25 from the QIRC website and
transcribe this content onto it. The QIRC site was unreachable from the build
environment (HTTP 503), so the field layout below follows the Version 4.1 field
list (inspection where/when; originals distinguished from copies - when, how and
by whom served) and MUST be verified against the live form before service.
"""
import io, re, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer, PageBreak)

OUT = "out/FORM25_NOTICE_TO_ADMIT_DOCUMENTS.pdf"

# ---- pull the annexure schedule so Form 25 and Annexure A cannot drift ----
_src = open('build_form24_annexureA.py').read()
_blk = _src[_src.index('ITEMS = ['):_src.index('\n]\n', _src.index('ITEMS = [')) + 2]
_g = {}
exec(_blk, _g, _g)
ITEMS = _g['ITEMS']

def provenance(rel):
    if rel.startswith('disclosure-2025-07/'):
        return "Copy as produced by the Respondent (disclosure, July 2025)"
    if rel.startswith('disclosure-2026-06_MSH_production/') or rel.startswith('Item_11_myHR'):
        return ("Copy as produced by Metro South Health under the notice of "
                "non-party disclosure (June 2026)")
    if rel.startswith('Review_Decision'):
        return "Copy of the Respondent's own review decision, as served on the Appellant"
    if rel.startswith('2026-02-18_Form24'):
        return "Copy from the parties' correspondence in this proceeding"
    if rel.startswith('2026-08-11_Stressor1a'):
        return ("Copy of the bundle served by the Appellant on the Respondent "
                "on 11 August 2026")
    return "Copy from the Appellant's own records"

BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=10, leading=13.6, spaceAfter=5)
H1   = ParagraphStyle('H1', parent=BODY, fontName='Helvetica-Bold', fontSize=15, leading=18)
CEN  = ParagraphStyle('CEN', parent=BODY, alignment=1)
SMALL= ParagraphStyle('SMALL', parent=BODY, fontSize=8.4, leading=11.2, spaceAfter=2)
WARN = ParagraphStyle('WARN', parent=SMALL, textColor=colors.HexColor('#8a1f1f'))
FLD  = ParagraphStyle('FLD', parent=BODY, fontName='Helvetica-Bold', fontSize=9, leading=12)
VAL  = ParagraphStyle('VAL', parent=BODY, fontSize=10, leading=13)
def P(t, s=BODY): return Paragraph(t, s)

def fieldrow(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.6, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f4f4f4')),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    return t

s = []
s.append(P("<b>INDUSTRIAL COURT OF QUEENSLAND<br/>QUEENSLAND INDUSTRIAL RELATIONS COMMISSION</b>",
           ParagraphStyle('HD', parent=BODY, fontSize=9.5, leading=12.5,
                          textColor=colors.HexColor('#7a4a10'))))
s.append(fieldrow([[P("Matter Number:", FLD), P("<b>WC / 2024 / 227</b>", VAL)]], [34*mm, 60*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Form 25 - Notice to admit documents", H1))
s.append(P("<i>Industrial Relations Act 2016</i>, section 989<br/>"
           "<i>Industrial Relations (Tribunals) Rules 2011</i>, rules 41, 49, 108 and 113", SMALL))
s.append(Spacer(1, 5*mm))
s.append(fieldrow([[P("Applicant/Appellant:", FLD), P("Cory Lea Shepherd", VAL)]], [40*mm, 120*mm]))
s.append(P("v", CEN))
s.append(fieldrow([[P("Respondent:", FLD), P("Workers' Compensation Regulator", VAL)]], [40*mm, 120*mm]))
s.append(Spacer(1, 3*mm))
s.append(fieldrow([[P("To:", FLD), P("The Workers' Compensation Regulator<br/>"
                                     "Attention: Ms Renee Matheson, Senior Appeals Officer", VAL)]],
                  [40*mm, 120*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Take notice that the <b>appellant</b> in this proceeding proposes to prove the "
           "documents specified in the schedule to this notice, and if you do not within "
           "<b>14 days</b> serve a notice on the appellant disputing the authenticity of the "
           "documents, you are taken to admit, for this proceeding only, the authenticity of the "
           "documents specified in this notice.", BODY))
s.append(Spacer(1, 3*mm))
s.append(fieldrow([[P("Where and when the documents may be inspected:", FLD),
                    P("A complete copy of every document specified is annexed to this notice as "
                      "<b>Annexure A</b> (the same Annexure A served with the appellant's Form 24 "
                      "notice to admit facts of even date) and is served with this notice, so that "
                      "inspection may be made from the annexed copies at any time. The documents "
                      "may in addition be inspected electronically, by appointment made in writing "
                      "to the appellant's address for service, within business hours on any "
                      "business day within 14 days after service of this notice.", VAL)]],
                  [55*mm, 105*mm]))
s.append(Spacer(1, 2*mm))
s.append(fieldrow([[P("Originals and copies - when, how and by whom served:", FLD),
                    P("Each document specified is served as a <b>copy</b>, annexed to this notice "
                      "as Annexure A, served by the appellant on the respondent's representative "
                      "by email together with this notice on the date of service appearing below. "
                      "No original is served. The schedule identifies, for each document, the "
                      "source from which the annexed copy was produced.", VAL)]],
                  [55*mm, 105*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("<b>NOTE - TRANSCRIBE ONTO THE OFFICIAL FORM.</b> This page reproduces the field "
           "content required by the approved Form 25 (Version 4.1) so the schedule can be settled "
           "and checked. The QIRC website was unreachable when this draft was built - download the "
           "current Form 25 from the Commission's website, verify the field layout, and transcribe "
           "this content into it before service. DELETE THIS NOTE BEFORE SERVICE.", WARN))
s.append(PageBreak())

s.append(P("SCHEDULE - THE DOCUMENTS WHOSE AUTHENTICITY IS TO BE ADMITTED", H1))
s.append(P("WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation "
           "Regulator (Respondent)", CEN))
s.append(P("The documents are annexed in full as Annexure A, behind the tabs numbered below, in "
           "the order listed. The description, date and page count of each document are as stated "
           "in the index to Annexure A.", BODY))

rows = [[P("<b>Tab</b>", SMALL), P("<b>Document</b>", SMALL), P("<b>Date</b>", SMALL),
         P("<b>Copy produced from</b>", SMALL), P("<b>Admit / Dispute authenticity</b>", SMALL)]]
for tab, desc, date, rel, p1, p2 in ITEMS:
    rows.append([P(f"<b>{tab}</b>", SMALL), P(desc, SMALL), P(date, SMALL),
                 P(provenance(rel), SMALL), P("", SMALL)])
t = Table(rows, colWidths=[10*mm, 68*mm, 24*mm, 40*mm, 24*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 3.5)]))
s.append(t)
s.append(Spacer(1, 6*mm))
s.append(P("Signature: ______________________ &nbsp;&nbsp; Print name: Cory Lea Shepherd "
           "&nbsp;&nbsp; Title of office held: Appellant (self-represented) &nbsp;&nbsp; "
           "Date: ____ / ____ / ________", BODY))
s.append(P("Address for service: as stated in the appellant's notice of address for service on "
           "the file. Service of this notice: by email to Renee.Matheson@oir.qld.gov.au.", SMALL))

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=16*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, A4[0]-32*mm, A4[1]-32*mm)])])
doc.build(s); buf.seek(0)
pdf = pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
print(f"built {OUT} - {len(ITEMS)} documents, {len(pdf.pages)} pages")
