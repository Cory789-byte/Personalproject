#!/usr/bin/env python3
"""WC/2024/227 - ANNEXURE A to the second notice to admit facts.
The documents referred to in Schedule B, stitched in one bundle behind a one-page index.
No document is annotated, highlighted or altered. All metadata stripped.
"""
import io, os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)
D = "../documents"
OUT = "out/FORM24_ANNEXURE_A.pdf"
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=16, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=12.4, spaceAfter=4)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
def P(t, s=C): return Paragraph(t, s)

# tab, description, date, path, first, last
ITEMS = [
 (1, "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital",
    "undated", "AO3_Switchboard_Role_Description_MSH.pdf", 1, None),
 (2, "Email thread, \"Corey Shepherd 388372 Pay issues\" - Payroll to the Line Manager copied to "
    "the Appellant; the Appellant to Payroll; Payroll to the Appellant",
    "3 to 13 May 2024", "disclosure-2025-07/Disclosure_witness_conferencing_QldHealth_Payroll.pdf", 5, 6),
 (3, "Same thread continued - the Line Manager to the Appellant, 21 May 2024; and \"Validation of "
    "Claims older than 3 months - Please sign\", 28 May 2024",
    "21 and 28 May 2024", "disclosure-2025-07/Disclosure_from_witnesses_part_FRMS_content.pdf", 46, 47),
 (4, "myHR submissions report for the Appellant, produced by Metro South Health as Item 11",
    "1 February to 31 May 2024", "Item_11_myHR_report_Leave_submissions_Feb-May_2024.pdf", 1, None),
 (5, "QH Leave Takings Report for the Appellant, produced by Metro South Health as Item 15",
    "19 March 2024",
    "disclosure-2026-06_MSH_production/Item 15 QH Leave Takings Report_Cory Shepherd_19 March 2024.pdf", 1, None),
 (6, "Letter, Metro South Hospital and Health Service to Commissioner Dwyer, reference "
    "K-LM26/729, signed by Ms N Cridland, Chief Executive",
    "5 June 2026", "2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", 1, 5),
 (7, "Letter, Ms L Forrest, Senior Consultant Human Resources, to the Appellant",
    "7 July 2026", "2026-07-07_Forrest_ECC_further_information_FULL.pdf", 1, None),
 (8, "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital",
    "November 2024", "2024-11-14_MSH_Consultation_Paper_Proposed_Rosters_LH_Switchboard.pdf", 1, None),
 (9, "Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital",
    "December 2024", "2024-12_MSH_Consultation_Outcome_Proposed_Rosters_LH_Switchboard.pdf", 1, None),
 (10, "Email, Mr H Moran, Organiser, Together Queensland, to Ms C Jeffrey, Ms P Conaghan and the "
     "Appellant, \"Switchboard Roster Feedback - For Delegates\"",
     "3 November 2025", "2025-11-03_Together_Moran_delegate_endorsement_Shepherd_Jeffrey_Conaghan.pdf", 1, None),
 (11, "Review Decision 69983, Workers' Compensation Regulator",
     "24 October 2024", "Review_Decision_69983_24.10.2024.pdf", 1, None),
]

built, errs, idx_rows = [], [], []
pdf = pikepdf.Pdf.new()
pages = []
for tab, desc, date, rel, p1, p2 in ITEMS:
    path = os.path.join(D, rel)
    if not os.path.exists(path):
        errs.append(f"tab {tab}: MISSING {rel}"); continue
    try:
        sp = pikepdf.open(path)
        end = p2 if p2 else (len(sp.pages) if p1 == 1 else p1)
        end = min(end, len(sp.pages))
        pages.append((tab, desc, date, sp, p1, end))
    except Exception as e:
        errs.append(f"tab {tab}: {e}")

start = 2
for tab, desc, date, sp, p1, end in pages:
    n = end - p1 + 1
    idx_rows.append((tab, desc, date, n, start, start + n - 1))
    start += n

st = [P("Annexure A to the notice to admit facts - the documents", H1),
      P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; the documents "
        "referred to in Schedule B, in the order there listed", SUB)]
rows = [[P("Tab", CH), P("Document", CH), P("Date", CH), P("Pages", CH), P("At", CH)]]
for tab, desc, date, n, a, b in idx_rows:
    rows.append([P(str(tab)), P(desc), P(date), P(str(n)), P(f"{a}-{b}" if b > a else str(a))])
t = Table(rows, colWidths=[10*mm, 108*mm, 26*mm, 14*mm, 20*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5)]))
st.append(t); st.append(Spacer(1, 4*mm))
st.append(P("The documents follow in the order listed. No document has been annotated, highlighted "
            "or altered. Where only part of a document is reproduced, the balance is available on "
            "request.", B))
buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=16*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, A4[0]-32*mm, A4[1]-32*mm)])])
doc.build(st); buf.seek(0)
pdf.pages.extend(pikepdf.open(buf).pages)
for tab, desc, date, sp, p1, end in pages:
    pdf.pages.extend(sp.pages[p1-1:end])

try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
print(f"built {OUT} - {len(idx_rows)} tabs, {len(pdf.pages)} pages")
for e in errs: print("  !", e)
