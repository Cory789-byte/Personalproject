#!/usr/bin/env python3
"""WC/2024/227 — Review Decision 69983: the file metadata, on one page.

⛔ INTERNAL WORKING RECORD. Not for service or filing in this form. Two reasons:

  1. The authoritative file (`f59eb0c1-Review_Decision_69983.pdf`, sha256 d0b2a514…, 258,752 bytes)
     is NOT in this repository. The metadata below is transcribed from the object-level examination
     recorded at skill/references/RD69983-OBJECT-LEVEL-FORENSICS.md (8 August 2026). The only copy
     held here (documents/Review_Decision_69983_24.10.2024.pdf, sha256 29379f1c…, 353,479 bytes) is
     a LATER RE-SAVE and its metadata is not the original's.
     ⇒ Re-supply the original before this sheet is used for anything outside this file.
  2. A metadata sheet states fields and dates. It draws no inference, and none is drawn here.
     What the fields mean is a matter for evidence, not for a table.

Output: out/RD69983_FILE_METADATA_1PAGE.pdf
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle)
import pikepdf

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
OUT = "out/RD69983_FILE_METADATA_1PAGE.pdf"

HD  = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8, leading=10.2,
                     textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=7)
TT  = ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=11, leading=13.5, spaceAfter=3)
WARN= ParagraphStyle('WARN', fontName='Helvetica-Bold', fontSize=6.9, leading=8.8,
                     textColor=colors.HexColor('#8a2010'), spaceAfter=5)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=6.9, leading=8.8, spaceAfter=4)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=7.8, leading=10, spaceBefore=3.5, spaceAfter=2)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=6.4, leading=8.0, spaceAfter=0)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
CM  = ParagraphStyle('CM', parent=C, fontName='Courier', fontSize=6.0, leading=7.8)

W = A4[0] - 30*mm

def tbl(rows, widths, mono_col=None, head=True):
    data=[]
    for i,r in enumerate(rows):
        st = CB if (head and i==0) else C
        data.append([Paragraph(c, CM if (mono_col is not None and j==mono_col and not (head and i==0)) else st)
                     for j,c in enumerate(r)])
    t=Table(data, colWidths=widths, repeatRows=1 if head else 0)
    s=[('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#9a9a9a')),
       ('VALIGN',(0,0),(-1,-1),'TOP'),
       ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
       ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]
    if head: s.append(('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EDEDED')))
    t.setStyle(TableStyle(s)); return t

story=[
 Paragraph("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION &nbsp;·&nbsp; Matter No. WC/2024/227", HD),
 Paragraph("Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)", HD2),
 Paragraph("REVIEW DECISION 69983 — FILE METADATA", TT),
 Paragraph("⛔ INTERNAL WORKING RECORD — NOT FOR SERVICE OR FILING IN THIS FORM. "
   "The metadata below is transcribed from the object-level examination of the original file recorded "
   "on 8 August 2026. That original is not held in the working repository; the copy held there is a "
   "later re-save with a different hash. Re-obtain the original before this sheet is used for any "
   "purpose outside the working file. This sheet records fields and dates only and draws no inference "
   "from them.", WARN),

 Paragraph("1.  File identity", SEC),
 tbl([["Field","Value"],
      ["File examined","f59eb0c1-Review_Decision_69983.pdf"],
      ["SHA-256","d0b2a514524690557eac52ace21d5864b7004d90ab5d83cd0fd474f25f9e5e9a"],
      ["Size","258,752 bytes"],
      ["PDF version / structure","1.6 · linearized · 673 objects · 28 pages · MediaBox 595.32 × 841.92 pt (A4) on every page"],
      ["Encryption / forms / JavaScript","None · none · none"],
      ["Revision history","⭐ None. One write. The two %%EOF / startxref pairs are the linearization cross-reference, not an incremental update"],
      ["⚠ Other copy in the repository","documents/Review_Decision_69983_24.10.2024.pdf · sha256 29379f1c99ae1ac2… · 353,479 bytes · a later re-save, NOT this file"],
     ], [34*mm, W-34*mm], mono_col=1),

 Paragraph("2.  ⭐ Dates recorded in the file", SEC),
 tbl([["Field","Value","Reads as"],
      ["/CreationDate","D:20241024101652+10'00'","24 October 2024, 10:16:52 AEST"],
      ["/ModDate","D:20241024101701+10'00'","24 October 2024, 10:17:01 AEST"],
      ["xmp:MetadataDate","2024-10-24T10:17:01+10:00","24 October 2024, 10:17:01 AEST"],
      ["Elapsed, creation to last write","—","9 seconds"],
      ["⭐ /hgDMSDate","09.10.2024","9 October 2024"],
      ["⭐ /hgSaveDescription","Reasons for decision - WCR reject - Worker applicant - Mr Cory Shepherd - 09.10.2024","—"],
      ["Date on the face of the decision","—","24 October 2024"],
     ], [30*mm, 78*mm, W-30*mm-78*mm], mono_col=1),

 Paragraph("3.  Toolchain", SEC),
 tbl([["Field","Value"],
      ["/Creator","Acrobat PDFMaker 24 for Word"],
      ["/Producer","Adobe PDF Library 24.3.212"],
      ["x:xmptk","Adobe XMP Core 9.1-c001 79.675d0f7, 2023/06/11-19:21:16"],
      ["/Lang","EN-AU"],
      ["/MarkInfo","/Marked true (tagged PDF)"],
      ["Structure tree","Standard Microsoft Word PDFMaker RoleMap, 15 entries"],
      ["Fonts","4 embedded subsets — ArialMT, Arial-BoldMT, Arial-ItalicMT, Wingdings-Regular (bullet glyphs)"],
     ], [30*mm, W-30*mm], mono_col=1),

 Paragraph("4.  Document-management properties (present in both /Info and the XMP pdfx: namespace)", SEC),
 tbl([["Field","Value"],
      ["/Author","HopgoodGanim Lawyers"],
      ["/Company","HopgoodGanim Lawyers"],
      ["/hgDMSMatter","2440758"],
      ["/hgDMSDocumentId","29218845v1"],
      ["/hgDMSAuthorName","hendry8286"],
      ["/hgDMSAddressee","Worker applicant - Mr Cory Shepherd"],
      ["/hgDMSDescription","Reasons for decision - WCR reject"],
      ["/hgDMSDocType","DOCUMENT"],
      ["/hgDMSDate","09.10.2024"],
      ["Unresolved placeholders","/hgDMSMatter_Original, /hgDMSDate_Original, /hgDMSAddressee_Original, /hgDMSDescription_Original, /hgDMSAuthorName_Original — each an unresolved DOCPROPERTY merge field (&lt;mcDMSMatter&gt;, &lt;mcDMSDate&gt; …)"],
      ["Empty fields","/Title, /Subject, /Keywords, /Comments, /SourceModified — all empty"],
     ], [30*mm, W-30*mm], mono_col=1),

 Paragraph("5.  Timestamps of the adjacent employer correspondence, for the same period", SEC),
 tbl([["Document","Ref","Date on its face","PDF /CreationDate = /ModDate","Producer"],
      ["Show cause — abandonment of employment, signed Ms A Coccetti, Executive Director LBHS","K-CF24/3196","26 September 2024","27 September 2024, 08:23:12 AEST","Microsoft Word for Microsoft 365"],
      ["Confirmation of abandonment of employment, enquiries Ms F Firoz, Consultant HR; nominates the separation date as 20 September 2024","K-CF24/3270","9 October 2024","9 October 2024, 16:08:05 AEST","Microsoft Word for Microsoft 365"],
      ["Review Decision 69983","69983","24 October 2024","24 October 2024, 10:16:52 AEST","Adobe PDF Library 24.3.212"],
     ], [58*mm, 17*mm, 24*mm, 40*mm, W-58*mm-17*mm-24*mm-40*mm]),
 Paragraph("⚠ Both employer letters carry /Author \"-\" and a single write. The confirmation of abandonment "
   "of 9 October 2024 describes the show cause letter as dated 27 September 2024; the letter itself is "
   "signed 26/09/2024 and its file was written on 27 September 2024 at 08:23:12.", B),

 Spacer(1, 2*mm),
 Paragraph("6.  What this sheet does and does not record", SEC),
 Paragraph("<b>Records:</b> the fields present in the files and the values in them. <b>Does not record:</b> what any "
   "field means. A document-management date field is evidence of what that system recorded against the "
   "document; it is not, without more, evidence of when a document was drafted, settled or decided. "
   "A /CreationDate is the date the PDF was written, not the date the underlying document was made. "
   "No conclusion is drawn here from the presence, absence or value of any field.", B),
 Spacer(1, 3*mm),
 Paragraph("Prepared 9 September 2026 &nbsp;·&nbsp; Cory Lea Shepherd, Appellant, self-represented &nbsp;·&nbsp; "
   "working record", HD),
]

doc=BaseDocTemplate(OUT, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                    topMargin=12*mm, bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(15*mm,12*mm,W,A4[1]-24*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
doc.build(story)

p=pikepdf.open(OUT, allow_overwriting_input=True)
try: del p.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
for pg in p.pages:
    for k in ('/Metadata','/PieceInfo','/Annots'):
        if k in pg.obj: del pg.obj[k]
p.save(OUT+'.tmp', linearize=True); os.replace(OUT+'.tmp', OUT)
chk=pikepdf.open(OUT)
n=len(chk.pages)
print(f"built {OUT} — {n} page{'s' if n!=1 else ''}, "
      f"{'clean' if not dict(chk.docinfo) and '/Metadata' not in chk.Root else 'METADATA SURVIVED'}")
if n != 1: raise SystemExit(f"ran to {n} pages; it must be one")
