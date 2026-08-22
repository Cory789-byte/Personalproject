#!/usr/bin/env python3
"""WC/2024/227 - STITCHED STRESSOR BUNDLES.

For each pleaded stressor, extracts the SPECIFIC pages of the SPECIFIC source documents already
verified in this matter (not whole 100-460pp packs), orders them chronologically, and stitches
them behind a one-page index into a single bundle PDF - the same design as the Stressor 1(a)
particulars bundle already served 11 August 2026.

Every page range below was located by grepping index/FULLTEXT.txt for verified quotations/dates
already used in the Form 24 and the case chronology. Source: verbatim page markers, not guesses.
"""
import os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import io

ROOT = ".."
OUTDIR = "out/STRESSOR_BUNDLES"
os.makedirs(OUTDIR, exist_ok=True)

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=17, alignment=1, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=9.5, leading=13, alignment=1,
                     textColor=colors.HexColor('#444444'), spaceAfter=8)
B = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.3, leading=12.6, spaceAfter=6)
CH = ParagraphStyle('CH', fontName='Helvetica-Bold', fontSize=8.4, leading=11)
C = ParagraphStyle('C', fontName='Helvetica', fontSize=8.4, leading=11.4)
WARN = ParagraphStyle('W', parent=B, fontSize=8.4, leading=11.4, textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
def P(t, s=C): return Paragraph(t, s)

def src(rel):
    return os.path.join(ROOT, rel)

# (tab_no, date, title, source_path, page_start, page_end [1-indexed, inclusive])
# page_end = None means single page. All page numbers verified against index/FULLTEXT.txt markers.
BUNDLES = {
 "1a": {
   "title": "Stressor 1(a) — erratic physical presence and unilateral directives without consultation",
   "note": "Already served on the Respondent as a standalone 30-page bundle, 11 August 2026. "
           "Reproduced here as item 16 for completeness of the stressor set; the served version "
           "governs.",
   "docs": [(1, "11 Aug 2026", "Stressor 1(a) particulars bundle (as served)",
             "documents/2026-08-11_Stressor1a_Particulars_Bundle_SERVED_on_Matheson.pdf", 1, 30)],
 },
 "1b": {
   "title": "Stressor 1(b) — the Switchboard communication book",
   "note": None,
   "docs": [
     (1, "6 Jun 2023", "Communication book removal chain - Chloe Taylor's own account",
      "documents/disclosure-2025-07/Disclosure_witness_conferencing_Tammy_Reese.pdf", 9, 11),
     (2, "10 May 2024", "Reference to the communication book in the FRMS bundle",
      "documents/disclosure-2025-07/Disclosure_from_witnesses_part_FRMS_content.pdf", 24, 24),
   ],
 },
 "1c": {
   "title": "Stressor 1(c) — the matters raised on 7 August 2023 and the response to them",
   "note": "This is the same chain that established the repair arc: the request for space, the "
           "manager's admitted oversight, the Director's direction to continue communicating, the "
           "grievance policy offered and declined, and the full-time approval that followed.",
   "docs": [
     (1, "7 Aug - 8 Sep 2023", "The Increase of hours / Workplace issues chain, in full",
      "documents/disclosure-2025-07/Disclosure_witness_conferencing_Tammy_Reese.pdf", 3, 11),
   ],
 },
 "1d": {
   "title": "Stressor 1(d) — the special pandemic leave applications of February 2024",
   "note": None,
   "docs": [
     (1, "Feb 2024", "myHR leave submission report, 1 Feb - 31 May 2024",
      "documents/disclosure-2026-06_MSH_production/Item 11 myHR report_Leave submissions_1 February 2024 to 31 May 2024.pdf", 1, None),
     (2, "20-27 Feb 2024", "Pandemic leave evidence and leave form, PRN 15480560",
      "documents/disclosure-2026-06_MSH_production/Item 11_Leave form PRN 15480560 Evidence pandemic leave.pdf", 1, None),
     (3, "Feb 2024", "AVAC PRN 15480560 history",
      "documents/disclosure-2026-06_MSH_production/Item 11 AVAC PRN 15480560 History.pdf", 1, None),
     (4, "Feb 2024", "Pandemic leave, Switchboard (redacted)",
      "documents/disclosure-2026-06_MSH_production/item 12 Pandemic leave switch_Redacted.pdf", 1, None),
   ],
 },
 "1e": {
   "title": "Stressor 1(e) — the complaint of 13 May 2024 and its determination as a public interest disclosure",
   "note": "NO DOCUMENTS ARE REPRODUCED IN THIS BUNDLE, and none are required. The Respondent "
           "ADMITS this stressor in full at paragraph 15 of its amended statement of facts and "
           "contentions dated 13 May 2026: \"With respect to stressor 1(e) of the appellant's "
           "statement, the respondent admits the allegation.\" An admitted fact requires no "
           "evidence. Separately, the documents recording the fact or content of the disclosure "
           "and the determination made in respect of it are the subject of a claim under s 65 of "
           "the Public Interest Disclosure Act 2010 (item 30 of the Appellant's Consolidated List "
           "of Documents), and are not produced.",
   "docs": [],
 },
 "1f": {
   "title": "Stressor 1(f) — the events of 13 to 15 May 2024 and the direction to retract",
   "note": None,
   "docs": [
     (1, "13-17 May 2024", "The office hours / retraction / on-call chain (FRMS bundle)",
      "documents/disclosure-2025-07/Disclosure_from_witnesses_part_FRMS_content.pdf", 17, 20),
   ],
 },
 "1g": {
   "title": "Stressor 1(g) — the union delegate matters",
   "note": None,
   "docs": [
     (1, "Aug 2024", "Union Delegate correspondence with WorkCover",
      "documents/correspondence-packs/10_Amy_Mo_WorkCover_EMAILS_PACK_84pp.pdf", 44, 45),
   ],
 },
 "2a": {
   "title": "Stressor 2(a) — remuneration: the distribution of shifts and penalties",
   "note": None,
   "docs": [
     (1, "4 Apr 2023", "Text messages with the Line Manager, including the $1,500 penalty-rate exchange and the roster board image",
      "documents/evidence/Chloe_Work_text_messages_incl_2023-04-04_roster_board.pdf", 1, None),
     (2, "10 May 2024", "The Roster Risk assessment matrix email (Reese to Pritchard)",
      "documents/disclosure-2025-07/Disclosure_from_witnesses_part_FRMS_content.pdf", 25, 26),
   ],
 },
 "2b": {
   "title": "Stressor 2(b) — the payroll correction of 3 to 28 May 2024",
   "note": None,
   "docs": [
     (1, "3-28 May 2024", "The AVAC correction delay chain",
      "documents/disclosure-2025-07/Disclosure_from_witnesses_part_FRMS_content.pdf", 46, 47),
   ],
 },
 "3a": {
   "title": "Stressor 3(a) — the consecutive shifts of 17-18 March 2024 and the seven-hour break",
   "note": None,
   "docs": [
     (1, "24 Oct 2024", "Review Decision 69983 - the 10-hour minimum, the seven-hour break, and the finding of unreasonable management action",
      "documents/Review_Decision_69983_24.10.2024.pdf", 24, 26),
     (2, "7 Jul 2026", "Letter of Ms L Forrest, HR - the 8-hour agreement applies only to staff-initiated shift swaps",
      "documents/2026-07-07_MSH_HR_Forrest_ECC_further_information.pdf", 1, None),
     (3, "5 Jun 2026", "Letter of Metro South Health (Cridland) - items 1, 2, 4, 5 (MET calls, fatigue assessment)",
      "documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", 1, None),
   ],
 },
 "3b": {
   "title": "Stressor 3(b) — the absence of any fatigue risk assessment or framework",
   "note": None,
   "docs": [
     (1, "5 Jun 2026", "Letter of Metro South Health (Cridland) - items 3(c), 4, 5, 7",
      "documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", 1, None),
   ],
 },
 "3c": {
   "title": "Stressor 3(c) — the leave taken on 19 March 2024",
   "note": None,
   "docs": [
     (1, "19 Mar 2024", "QH Leave Takings Report - Sick Leave, 7.60 hours, approved",
      "documents/disclosure-2026-06_MSH_production/Item 15 QH Leave Takings Report_Cory Shepherd_19 March 2024.pdf", 1, None),
   ],
 },
}

def strip_meta(path):
    p = pikepdf.open(path, allow_overwriting_input=True)
    try: del p.Root.Metadata
    except (AttributeError, KeyError): pass
    with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
    try: del p.Root.Metadata
    except (AttributeError, KeyError): pass
    for k in list(p.docinfo.keys()): del p.docinfo[k]
    tmp = path + ".tmp"
    p.save(tmp); p.close(); os.replace(tmp, path)

def build_index_page(tag, spec):
    s = []
    s.append(P(f"Stressor {tag} — supporting documents", H1))
    s.append(P("WC/2024/227 · Shepherd v Workers' Compensation Regulator · contemporaneous records, in date order", SUB))
    s.append(P(f"<b>{spec['title']}</b>", B))
    if spec.get("note"):
        s.append(P(spec["note"], WARN))
    rows = [[P("Tab", CH), P("Date", CH), P("Document", CH), P("Pages", CH)]]
    for tab, date, title, path, p1, p2 in spec["docs"]:
        pr = f"p.{p1}" if p2 is None or p2 == p1 else f"pp.{p1}-{p2}"
        rows.append([P(str(tab), C), P(date, C), P(title, C), P(pr, C)])
    t = Table(rows, colWidths=[10*mm, 26*mm, 130*mm, 20*mm], repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
    s.append(t)
    s.append(Spacer(1, 4*mm))
    s.append(P("The documents follow in the order listed above. Tab dividers are the page "
               "numbers stated; no document has been annotated, highlighted or altered.", B))
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=16*mm, bottomMargin=16*mm)
    doc.build(s)
    buf.seek(0)
    return pikepdf.open(buf)

built, errors = [], []
for tag, spec in BUNDLES.items():
    out = pikepdf.Pdf.new()
    idx = build_index_page(tag, spec)
    out.pages.extend(idx.pages)
    ok = True
    for tab, date, title, path, p1, p2 in spec["docs"]:
        full = src(path)
        if not os.path.exists(full):
            errors.append(f"{tag} tab {tab}: MISSING {path}")
            ok = False
            continue
        try:
            sp = pikepdf.open(full)
            end = p2 if p2 else p1
            if end > len(sp.pages):
                errors.append(f"{tag} tab {tab}: page range {p1}-{end} exceeds {len(sp.pages)}pp in {path}")
                end = len(sp.pages)
            out.pages.extend(sp.pages[p1-1:end])
        except Exception as e:
            errors.append(f"{tag} tab {tab}: ERROR opening {path}: {e}")
            ok = False
    outpath = f"{OUTDIR}/Stressor_{tag}_bundle.pdf"
    out.save(outpath)
    strip_meta(outpath)
    built.append((tag, len(out.pages), ok))

print(f"\n{'='*60}\nBUILT {len(built)} STRESSOR BUNDLES:")
for tag, n, ok in built:
    print(f"  {'OK ' if ok else 'WARN'} Stressor_{tag}_bundle.pdf  ({n}pp)")
if errors:
    print(f"\n{len(errors)} ISSUES TO VERIFY BEFORE USE:")
    for e in errors: print("  -", e)

# ---------------------------------------------------------------- master index
mi = []
mi.append(P("Stressor bundles — index", H1))
mi.append(P("WC/2024/227 · Shepherd v Workers' Compensation Regulator · assembled 22 August 2026", SUB))
mi.append(P("Each bundle collects the contemporaneous records for one stressor as pleaded in the "
            "Amended Statement of Facts and Contentions filed 7 April 2026, behind a one-page "
            "index, in date order. Page references in each index are to the source document. No "
            "document has been annotated, highlighted or altered. Where a bundle reproduces only "
            "part of a source document, the balance of that document is disclosed in the "
            "Appellant's Consolidated List of Documents and is available on request.", B))
mrows = [[P("Bundle", CH), P("Stressor as pleaded", CH), P("Pages", CH)]]
LABELS = {
 "1a": "Erratic physical presence and unilateral directives without consultation",
 "1b": "The Switchboard communication book",
 "1c": "The matters raised on 7 August 2023 and the response to them",
 "1d": "The special pandemic leave applications of February 2024",
 "1e": "The complaint of 13 May 2024 and its determination as a public interest disclosure — ADMITTED",
 "1f": "The events of 13 to 15 May 2024 and the direction to retract",
 "1g": "The union delegate matters",
 "2a": "Remuneration — the distribution of shifts and penalties",
 "2b": "The payroll correction of 3 to 28 May 2024",
 "3a": "The consecutive shifts of 17 and 18 March 2024 and the seven-hour break",
 "3b": "The absence of any fatigue risk assessment or framework",
 "3c": "The leave taken on 19 March 2024",
}
for tag, n, ok in built:
    mrows.append([P(f"<b>Stressor {tag}</b>", C), P(LABELS.get(tag, ""), C), P(str(n), C)])
mt = Table(mrows, colWidths=[24*mm, 140*mm, 16*mm], repeatRows=1)
mt.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
mi.append(mt)
mi.append(Spacer(1, 5*mm))
mi.append(P("The stressor arrangement is for convenience of reference only. It forms no part of "
            "the disclosure and is not a pleading. The Appellant's Consolidated List of Documents "
            "is the disclosure.", WARN))
midoc = SimpleDocTemplate(f"{OUTDIR}/00_INDEX_stressor_bundles.pdf", pagesize=A4,
                          leftMargin=16*mm, rightMargin=16*mm, topMargin=16*mm, bottomMargin=16*mm)
midoc.build(mi)
strip_meta(f"{OUTDIR}/00_INDEX_stressor_bundles.pdf")
print(f"\nwrote {OUTDIR}/00_INDEX_stressor_bundles.pdf")

import zipfile
zp = "out/WC2024227_STRESSOR_BUNDLES.zip"
if os.path.exists(zp): os.remove(zp)
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as zf:
    for fn in sorted(os.listdir(OUTDIR)):
        zf.write(os.path.join(OUTDIR, fn), fn)
print(f"wrote {zp} ({os.path.getsize(zp)/(1024*1024):.1f} MB)")
