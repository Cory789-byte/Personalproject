#!/usr/bin/env python3
"""WC/2024/227 - the SECOND NOTICE TO ADMIT FACTS, plugged into the approved Form 24 layout.
Replicates Form 24 - Notice to admit facts, Version 4 (State of Queensland 2018).
Facts are imported from build_form24_second.py so there is one source of truth.
"""
import re, os, pikepdf
SERVE_CLEAN = os.environ.get('SERVE') == '1'
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, KeepTogether)

# ---- import the single source of truth for the facts + documents ----
src = open('build_form24_second.py').read()
_blk = src[src.index('R_TAYLOR ='):src.index('\n]\n', src.index('FACTS = ['))+2]
_renumber = src[src.index('import re as _re'):src.index('_L, _relab')+len('_L, _relab')]
ns = {}
exec(_blk, ns, ns)
exec(_renumber, ns, ns)
FACTS = ns['FACTS']
_a = open('build_form24_annexureA.py').read()
_i = _a.index('ITEMS = ['); _j = _a.index('\n]\n', _i) + 2
_ns = {}; exec(_a[_i:_j], _ns, _ns)
DOCS = [(str(t), d, dt) for t, d, dt, _p, _p1, _p2 in _ns['ITEMS']]

ss = getSampleStyleSheet()
ORG = colors.HexColor('#8a5a1a')
HEADORG = ParagraphStyle('HO', fontName='Helvetica-Bold', fontSize=9.5, leading=12.5, textColor=ORG)
TITLE = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=19, leading=23, spaceAfter=2)
LEG = ParagraphStyle('LEG', fontName='Helvetica-Oblique', fontSize=8.6, leading=11.4)
BODY = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.4,
                      spaceAfter=5)
FLD = ParagraphStyle('F', parent=BODY, fontName='Helvetica-Bold', fontSize=9)
VAL = ParagraphStyle('V', parent=BODY, fontSize=9.6, leading=12.6)
CELL = ParagraphStyle('C', parent=BODY, fontSize=8.6, leading=11.4, spaceAfter=0)
CH = ParagraphStyle('CH', parent=CELL, fontName='Helvetica-Bold', alignment=1)
SEC = ParagraphStyle('SEC', parent=CELL, fontName='Helvetica-Bold')
NOTE = ParagraphStyle('N', parent=BODY, fontSize=8.2, leading=11,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
CEN = ParagraphStyle('CEN', parent=BODY, alignment=1, fontName='Helvetica-Bold')
def P(t, s=BODY): return Paragraph(t, s)

def box(rows, widths, shade_first=True):
    t = Table(rows, colWidths=widths)
    st = [('GRID', (0,0), (-1,-1), 0.7, colors.black), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
          ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
          ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]
    if shade_first: st.append(('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f2f2f2')))
    t.setStyle(TableStyle(st)); return t

story = []
story.append(P("INDUSTRIAL COURT OF QUEENSLAND<br/>QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", HEADORG))
story.append(Spacer(1, 2*mm))
story.append(box([[P("Matter Number:", FLD), P("<b>WC</b>", VAL), P("/", VAL), P("<b>2024</b>", VAL),
                   P("/", VAL), P("<b>227</b>", VAL)]],
                 [30*mm, 18*mm, 5*mm, 18*mm, 5*mm, 18*mm], shade_first=False))
story.append(Spacer(1, 5*mm))
story.append(P("Form 24 &ndash; Notice to admit facts", TITLE))
story.append(P("<i>Industrial Relations Act 2016</i>, section 989<br/>"
               "<i>Industrial Relations (Tribunals) Rules 2011</i>, rules 41, 49, 108 and 113", LEG))
story.append(Spacer(1, 4*mm))
story.append(box([[P("Applicant/Appellant:", FLD), P("Cory Lea Shepherd", VAL)]], [40*mm, 118*mm]))
story.append(P("v", CEN))
story.append(box([[P("Respondent:", FLD), P("Workers' Compensation Regulator", VAL)]], [40*mm, 118*mm]))
story.append(Spacer(1, 2*mm))
story.append(P("<b>PLEASE NOTE:</b> If there are more than two parties to this application, please "
               "complete a <b>Form 1 &ndash; Parties list</b> and file it with this form.", BODY))
story.append(box([[P("To:", FLD), P("Workers' Compensation Regulator<br/>"
                                    "Attention: Ms Renee Matheson, Senior Appeals Officer<br/>"
                                    "150 Mary Street, Brisbane QLD 4001<br/>Renee.Matheson@oir.qld.gov.au", VAL)]],
                 [40*mm, 118*mm]))
story.append(Spacer(1, 3*mm))
story.append(P("Take notice that the [&nbsp;&nbsp;] applicant &nbsp; <b>[X] appellant</b> &nbsp; "
               "[&nbsp;&nbsp;] respondent in this proceeding proposes to prove the facts specified "
               "below, and if you do not within 14 days serve a notice on the [&nbsp;&nbsp;] "
               "applicant &nbsp; <b>[X] appellant</b> &nbsp; [&nbsp;&nbsp;] respondent disputing "
               "the facts you are taken to admit, for this proceeding only, the facts specified in "
               "this notice.", BODY))
story.append(Spacer(1, 2*mm))

rows = [[P("No.", CH), P("Fact to be Admitted (with Exhibit Reference)", CH), P("Admit / Deny", CH)]]
spans = []
for f in FACTS:
    if len(f) == 2:
        spans.append((len(rows), f[0] == '#'))
        _lab = "" if f[0] == '#' else f[0]
        rows.append([P(f"<b>{_lab}</b>", SEC), P(f"<b>{f[1]}</b>", SEC), P("", CELL)])
    else:
        _txt = f[1]
        _m = re.search(r'Annexure A Tabs? ([0-9A-Z]+(?:[,\-] ?[0-9A-Z]+)*)', f[2] if len(f) > 2 else '')
        if _m:
            _txt += f" <font size=8 color='#555555'>(Annexure A, Tab {_m.group(1)})</font>"
        rows.append([P(f"<b>{f[0]}</b>", CELL), P(_txt, CELL), P("", CELL)])
t = Table(rows, colWidths=[11*mm, 118*mm, 29*mm], repeatRows=1)
st = [('GRID', (0,0), (-1,-1), 0.7, colors.black), ('VALIGN', (0,0), (-1,-1), 'TOP'),
      ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#ffffff')),
      ('ALIGN', (0,0), (0,-1), 'CENTER'),
      ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
      ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]
for i, isbanner in spans:
    shade = '#bfbfbf' if isbanner else '#ececec'
    st += [('BACKGROUND', (0,i), (-1,i), colors.HexColor(shade)), ('SPAN', (1,i), (2,i))]
t.setStyle(TableStyle(st))
story.append(t)
story.append(Spacer(1, 6*mm))
story.append(box([[P("Signature:", FLD), P("<br/><br/>", VAL)],
                  [P("Print name:", FLD), P("Cory Lea Shepherd", VAL)],
                  [P("Title of office held:", FLD), P("Appellant (self-represented)", VAL)],
                  [P("Date:", FLD), P("_____ / _____ / __________", VAL)]], [45*mm, 113*mm]))

# ---- Annexure A: documents (r 49 authenticity limb) ----
story.append(Spacer(1, 8*mm))
story.append(P("SCHEDULE OF DOCUMENTS &ndash; ANNEXURE A", ParagraphStyle('AH', parent=TITLE, fontSize=13, leading=17)))
story.append(P("Authenticity to be admitted &ndash; <i>Industrial Relations (Tribunals) Rules "
               "2011</i>, rule 49", LEG))
story.append(Spacer(1, 3*mm))
story.append(P("Take notice that the appellant also asks the respondent to admit, for this "
               "proceeding only, the authenticity of the documents specified below, and that if "
               "the respondent does not within 14 days after receiving this notice serve a notice "
               "on the appellant disputing the authenticity of those documents, the respondent is "
               "taken to admit their authenticity for this proceeding only.", BODY))
drows = [[P("Tab", CH), P("Document", CH), P("Date", CH), P("Authenticity admitted / disputed", CH)]]
for tab, d, dt in DOCS:
    drows.append([P(f"<b>{tab}</b>", CELL), P(d, CELL), P(dt, CELL), P("", CELL)])
dt_ = Table(drows, colWidths=[11*mm, 89*mm, 26*mm, 32*mm], repeatRows=1)
dt_.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.7, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'TOP'), ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
story.append(dt_)
story.append(Spacer(1, 5*mm))
story.append(box([[P("Signature:", FLD), P("<br/><br/>", VAL)],
                  [P("Print name:", FLD), P("Cory Lea Shepherd", VAL)],
                  [P("Title of office held:", FLD), P("Appellant (self-represented)", VAL)],
                  [P("Date:", FLD), P("_____ / _____ / __________", VAL)]], [45*mm, 113*mm]))
story.append(Spacer(1, 5*mm))
if not SERVE_CLEAN:
    story.append(P("<b>BEFORE SERVICE - delete this note.</b> (1) Verify every quotation against its "
                   "source document. (2) Check the radio selections above: the appellant proposes to "
                   "prove the facts, and the notice is served on the respondent. (3) Confirm this is "
                   "the current version of Form 24 on the Commission's website before filing or "
                   "serving. (4) Sign and date both signature blocks.", NOTE))

OUT = "out/FORM24_PART_A_SERVE_CLEAN.pdf" if SERVE_CLEAN else "out/FORM24_COMPLETED_OFFICIAL_FORM.pdf"
doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=17*mm, rightMargin=17*mm,
                      topMargin=15*mm, bottomMargin=20*mm)
frame = Frame(17*mm, 20*mm, A4[0]-34*mm, A4[1]-35*mm, id='n',
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
def foot(c, d):
    c.saveState()
    c.setStrokeColor(colors.HexColor('#cccccc')); c.setLineWidth(0.5)
    c.line(17*mm, 16*mm, A4[0]-17*mm, 16*mm)
    c.setFont('Helvetica', 7.6); c.setFillColor(colors.black)
    c.drawString(17*mm, 12*mm, "© State of Queensland 2018")
    c.drawRightString(A4[0]-17*mm, 12*mm, "Form 24 – Notice to admit facts     Version 4")
    c.setFont('Helvetica', 8.6)
    c.drawString(17*mm, 6*mm, f"Page {d.page}")
    c.restoreState()
doc.addPageTemplates([PageTemplate(id='n', frames=[frame], onPage=foot)])
doc.build(story)

pdf = pikepdf.open(OUT, allow_overwriting_input=True)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as mt: mt.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save("out/_o.pdf"); pdf.close(); os.replace("out/_o.pdf", OUT)
print(f"built {OUT} - {len([f for f in FACTS if len(f)>2])} facts, {len(DOCS)} documents")
