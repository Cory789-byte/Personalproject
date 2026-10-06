#!/usr/bin/env python3
"""WC/2024/227 - Request to the Regulator to admit the authenticity of the Role Description for Manager of
Switchboard Services enclosed by Metro South Health with its letter of 5 June 2026 (Tab 32A). Tab 32B is the
delegation already admitted at Tab 29. Then: strip all metadata from the letter and from Tab 32, and verify.
Usage (from wc2024227/drafts): python3 build_letter_regulator_tab32.py "[date]" "[reply-by]"
"""
import io, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv) > 1 else "[  ] October 2026"
REPLY_BY = sys.argv[2] if len(sys.argv) > 2 else "Friday 16 October 2026"
OUT = "out/TAB32/WC2024227_Letter_to_Regulator_Tab32_Manager_Role_Description.pdf"
TAB32 = "out/TAB32/WC2024227_Tab32_MSH_enclosures_ManagerRole_and_Delegation.pdf"

B = ParagraphStyle('B', fontName='Helvetica', fontSize=9.6, leading=12.6, spaceAfter=6)
I = ParagraphStyle('I', parent=B, leftIndent=8*mm, spaceAfter=3)
P = lambda t, s=B: Paragraph(t, s)
sig = RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); sig.hAlign = 'LEFT'

s = [P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com"),
     Spacer(1, 2*mm),
     P("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>"
       "150 Mary Street, Brisbane QLD 4000<br/>By email: Renee.Matheson@oir.qld.gov.au"),
     Spacer(1, 2*mm), P(f"Dated {DATE}"), Spacer(1, 2*mm),
     P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
       "<b>Request: the Role Description for Manager of Switchboard Services enclosed with Metro South Health's "
       "letter of 5 June 2026</b>"),
     Spacer(1, 1*mm), P("Dear Ms Matheson,"),
     P("I refer to Metro South Health's letter of 5 June 2026 to Commissioner Dwyer, reference K-LM26/729 "
       "(Annexure A, Tab 20), which the Respondent confirmed by email of 24 September 2026. With that letter, in "
       "response to the notice of non-party disclosure, Metro South Health enclosed under Item 6 &ldquo;the attached "
       "Role Description for Manager of Switchboard Services&rdquo;, and under Item 13 the HR delegation for COVID-19 "
       "Paid Special Pandemic Leave signed 23 November 2022."),
     P("The Appellant intends to rely on and tender both documents at the hearing. Copies are attached as Tab 32, "
       "reproduced as Metro South Health produced them, with identification headers only:"),
     P("<b>Tab 32A</b> &nbsp; Role Description, Manager Switchboard Services, Logan Hospital (AO4), RD 30478699 "
       "(Item 6), 6 pages.", I),
     P("<b>Tab 32B</b> &nbsp; Instrument of Human Resource Sub-Delegation, COVID-19 Pandemic Event &ndash; Paid "
       "Special Pandemic Leave, signed 23 November 2022 (Item 13), 1 page. This instrument is also at Annexure A, "
       "Tab 29, the authenticity of which the Respondent admitted on 8 September 2026. No further admission is "
       "sought for it.", I),
     Spacer(1, 1*mm),
     P(f"Could the Respondent please, by {REPLY_BY}, or before the conference if it is listed earlier, admit under "
       "rule 49 of the <i>Industrial Relations (Tribunals) Rules 2011</i> that the copy at Tab 32A is a true copy of the "
       "Role Description that Metro South Health enclosed with its letter of 5 June 2026, so that it may be tendered "
       "without further proof. If the Respondent does not admit it, I would be grateful if it would state the ground."),
     P("If the Respondent would prefer this request to be put as a notice to admit documents, please let me know and "
       "I will serve it in that form."),
     P("Yours faithfully,"), Spacer(1, 1*mm), sig, Spacer(1, 1*mm),
     P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented"),
     Spacer(1, 3*mm), P("Attachment: Tab 32 (8 pages, with index)")]

buf = io.BytesIO()
d = BaseDocTemplate(buf, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=14*mm, bottomMargin=14*mm)
d.addPageTemplates([PageTemplate(id='n', frames=[Frame(22*mm, 14*mm, A4[0]-44*mm, A4[1]-28*mm,
                    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
d.build(s); buf.seek(0)
open(OUT + ".tmp", "wb").write(buf.read())

def scrub(path_in, path_out):
    pdf = pikepdf.open(path_in)
    for key in ("/Metadata", "/PieceInfo", "/Names", "/OpenAction", "/AA"):
        if key in pdf.Root: del pdf.Root[key]
    for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
    for obj in pdf.objects:
        if isinstance(obj, (pikepdf.Dictionary, pikepdf.Stream)):
            for key in ("/Metadata", "/PieceInfo", "/LastModified"):
                if key in obj: del obj[key]
    for pg in pdf.pages:
        if "/Annots" in pg:
            keep = [a for a in pg.Annots if a.get("/Subtype") == "/Link"]
            if keep: pg.Annots = pikepdf.Array(keep)
            else: del pg["/Annots"]
    pdf.remove_unreferenced_resources()
    pdf.save(path_out, fix_metadata_version=False, deterministic_id=True,
             object_stream_mode=pikepdf.ObjectStreamMode.generate)

import os
scrub(OUT + ".tmp", OUT); os.remove(OUT + ".tmp")
scrub(TAB32, TAB32 + ".tmp"); os.replace(TAB32 + ".tmp", TAB32)

# verify
for f in (OUT, TAB32):
    p = pikepdf.open(f)
    leftovers = [k for k in ("/Metadata", "/PieceInfo", "/Names") if k in p.Root]
    deep = sum(1 for o in p.objects if isinstance(o, (pikepdf.Dictionary, pikepdf.Stream))
               and any(k in o for k in ("/Metadata", "/PieceInfo", "/LastModified")))
    raw = open(f, "rb").read()
    hits = [w for w in (b"Ruttan", b"Dawson", b"Microsoft", b"ReportLab", b"PyMuPDF", b"pikepdf", b"xmpmeta",
                        b"/Author", b"/Creator", b"/Producer", b"/CreationDate", b"/ModDate") if w in raw]
    print(f, "pages", len(p.pages), "docinfo", dict(p.docinfo), "root", leftovers, "deep", deep, "raw-hits", hits)
