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
   "note": "One email thread, subject \"Corey Shepherd 388372 Pay issues\". The Appellant is a "
           "recipient of every message in it.",
   "messages": [
     ("3 May 2024, 9:39 am<br/>(9:40 am on the copy at tab 2)", "PayrollMetroSouth<br/>Ms E Grant",
      "To: Ms C Taylor<br/><b>Cc: Mr C Shepherd</b>", "Corey Shepherd 388372 Pay issues",
      "Tab 1, p.1<br/>Tab 2, pp.1-2"),
     ("10 May 2024, 2:21 pm", "Mr C Shepherd",
      "To: PayrollMetroSouth;<br/>Ms E Grant", "Re: Corey Shepherd 388372 Pay issues", "Tab 1, p.1"),
     ("13 May 2024, 8:21 am", "PayrollMetroSouth<br/>Ms E Grant",
      "To: Mr C Shepherd", "RE: Corey Shepherd 388372 Pay issues", "Tab 1, p.1"),
     ("15 May 2024", "Ms C Taylor",
      "myHR", "Attendance Variation and Allowance Claim 16328886 submitted; completed 16 May 2024",
      "Tab 3"),
     ("21 May 2024, 12:33 pm", "Ms C Taylor",
      "To: Mr C Shepherd", "RE: Corey Shepherd 388372 Pay issues", "Tab 2, p.1"),
     ("28 May 2024, 8:36 am", "Ms C Taylor",
      "To: Mr C Shepherd<br/>Cc: Ms T Reese",
      "Validation of Claims older than 3 months - Please sign", "Tab 2, p.1"),
     ("28 May 2024", "Ms C Taylor",
      "myHR", "Attendance Variation and Allowance Claim 16450619 submitted; Part Completed 30 May 2024",
      "Tab 3"),
   ],
   "notheld": "Four earlier messages in the same subject matter are recited in Review Decision 69983 "
              "at page 21 but are not reproduced in this bundle, not being held: the Appellant to the "
              "Line Manager, 8 April 2024; the Line Manager to the Appellant, 9 April 2024; the "
              "Appellant to the Line Manager, 24 April 2024; and the Line Manager to the Appellant, "
              "1 May 2024. They are understood to form part of the chain \"Request for review and "
              "adjustment of payment - 08/04/2024 to 23/08/2024\" listed at item 23 of the "
              "Respondent's amended list of documents of 14 August 2026.",
   "docs": [
     (1, "13, 10 and 3 May 2024", "Email thread \"Corey Shepherd 388372 Pay issues\", from the "
      "Respondent's disclosure of the Queensland Health Payroll witness conferencing - "
      "3 May 2024, 9:39 am, PayrollMetroSouth (Ms E Grant) to Ms C Taylor, copied to the Appellant: "
      "\"Please submit an AVAC to correct these shifts for each fortnight so Cory is paid corrected "
      "and his RDO balance will then be amended\", identifying AVAC PRN 15397775 and AVAC PRN "
      "15605601; 10 May 2024, 2:21 pm, the Appellant to Payroll and Ms Grant; 13 May 2024, 8:21 am, "
      "Ms Grant to the Appellant: \"I cannot see that any of the issues below have been corrected. "
      "Please speak to your Line Manager to have them corrected with an AVAC submitted through My HR\"",
      "documents/disclosure-2025-07/Disclosure_witness_conferencing_QldHealth_Payroll.pdf", 5, None),
     (2, "21 and 28 May 2024", "Same thread continued, from the Respondent's disclosure - "
      "21 May 2024, 12:33 pm, Ms C Taylor to the Appellant, subject \"RE: Corey Shepherd 388372 Pay "
      "issues\": \"I am still I am waiting payroll confirmation about a few of these payroll issues "
      "and as soon as I do get that confirmation, I will submit an AVAC for next pay run\"; and "
      "28 May 2024, 8:36 am, Ms C Taylor to the Appellant copied to Ms T Reese, \"Validation of "
      "Claims older than 3 months - Please sign\"",
      "documents/disclosure-2025-07/Disclosure_from_witnesses_part_FRMS_content.pdf", 46, 47),
     (3, "1 Feb to 31 May 2024", "myHR submissions report for the Appellant, produced by Metro South "
      "Health as Item 11 - seven submissions, every Attendance Variation and Allowance Claim "
      "initiated by Ms C Taylor, processing between one and five days on each, the claim of "
      "15 May 2024 completed 16 May 2024, and the claim of 28 May 2024 recorded as Part Completed",
      "documents/Item_11_myHR_report_Leave_submissions_Feb-May_2024.pdf", 1, None),
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
     (3, "5 Jun 2026", "Letter of Metro South Health, signed by Ms N Cridland, Chief Executive (ref K-LM26/729), in full - Items 1 and 2 (the MET call spreadsheet), Item 3(c) (no consequential changes), Items 4, 5 and 7 (no fatigue risk assessment; fatigue risk management implemented only after 30 June 2024)",
      "documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", 1, 5),
   ],
 },
 "3b": {
   "title": "Stressor 3(b) — the absence of any fatigue risk assessment or framework",
   "note": None,
   "docs": [
     (1, "5 Jun 2026", "Letter of Metro South Health, signed by Ms N Cridland, Chief Executive (ref K-LM26/729), in full - Item 4: \"the requested documents do not exist ... Logan Hospital Switchboard staff are non-clinical staff\"; Item 5: fatigue risk management assessment \"occurred after 30 June 2024\"; Item 7: no mandatory requirement; Item 3(c): \"no 'consequential' changes to operating procedures over the period requested\"",
      "documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", 1, 5),
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
 "3d": {
   "title": "Stressor 3(d) - the finding made on review",
   "note": None,
   "docs": [
     (1, "24 Oct 2024", "Review Decision 69983 of the Workers' Compensation Regulator, pages 26 and 27 - "
      "the reasons and the Conclusion. Page 26: \"I find the rostering of these two shifts amounted to "
      "unreasonable management action given that it was in direct contradiction to the award and the "
      "8-hour agreement.\" Page 27 records the determinations made, including that the Appellant "
      "sustained a personal injury of a psychological nature, that it arose out of employment where "
      "employment was a significant contributing factor, and that factor 4 amounted to unreasonable "
      "management action. The decision on review nevertheless confirmed the rejection of the "
      "application. The decision is reproduced in full in the Appellant's List of Documents.",
      "documents/Review_Decision_69983_24.10.2024.pdf", 26, 27),
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
    if spec.get("messages"):
        s.append(Spacer(1, 4*mm))
        s.append(P("<b>Schedule of messages, in date order</b>", B))
        s.append(P("The documents at tabs 1 and 2 are prints of one email thread and carry the "
                   "messages in reverse order, as a thread print does. This schedule sets them out "
                   "forwards. Every message is reproduced at the tab and page stated.", C))
        mr = [[P("Date and time", CH), P("From", CH), P("To, and copied to", CH),
               P("Subject", CH), P("At", CH)]]
        for dt, fr, to, subj, at in spec["messages"]:
            mr.append([P(dt, C), P(fr, C), P(to, C), P(subj, C), P(at, C)])
        mt = Table(mr, colWidths=[27*mm, 27*mm, 44*mm, 55*mm, 33*mm], repeatRows=1)
        mt.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
            ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
        s.append(mt)
        if spec.get("notheld"):
            s.append(Spacer(1, 3*mm))
            s.append(P(spec["notheld"], WARN))
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
mi.append(P("Each bundle collects the contemporaneous records for one particular of one of the "
            "<b>three stressors</b> pleaded in the Amended Statement of Facts and Contentions dated "
            "7 April 2026, behind a one-page index, in date order. Stressor 1 is pleaded with "
            "particulars (a) to (g); Stressor 2 with particulars (a) and (b); and Stressor 3 with "
            "particulars (a) to (d). The lettered labels are the particulars of the pleaded "
            "stressors. They are not separate stressors. Page references in each index are to the source document. No "
            "document has been annotated, highlighted or altered. Where a bundle reproduces only "
            "part of a source document, the balance of that document is disclosed in the "
            "Appellant's Consolidated List of Documents and is available on request.", B))
mrows = [[P("Pleaded stressor", CH), P("Particular", CH), P("Subject matter", CH), P("Pages", CH)]]
LABELS = {
 "1a": "Erratic physical presence and unilateral directives without consultation",
 "1b": "The Switchboard communication book",
 "1c": "The matters raised on 7 August 2023 and the response to them",
 "1d": "The special pandemic leave applications of February 2024",
 "1e": "The complaint of 13 May 2024 and its determination as a public interest disclosure — ADMITTED",
 "1f": "The events of 13 to 15 May 2024 and the direction to retract",
 "1g": "The union delegate matters",
 "2a": "The payment of entitlements between February and April 2024",
 "2b": "The payroll correction of 3 to 28 May 2024",
 "3a": "The consecutive shifts of 17 and 18 March 2024 and the seven-hour break",
 "3b": "The ten-hour rest requirement and the fatigue risk management framework",
 "3c": "The leave taken on 19 March 2024",
 "3d": "The finding made on review — ADMITTED",
}
for tag, n, ok in built:
    mrows.append([P(f"<b>Stressor {tag[0]}</b>", C), P(f"({tag[1]})", C),
                  P(LABELS.get(tag, ""), C), P(str(n), C)])
mt = Table(mrows, colWidths=[24*mm, 22*mm, 118*mm, 16*mm], repeatRows=1)
mt.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
mi.append(mt)
mi.append(Spacer(1, 5*mm))
mi.append(P("The arrangement is for convenience of inspection and reference only. A document may "
            "appear in more than one bundle where it is relevant to more than one particular. The "
            "bundles do not amend, replace or add to the Amended Statement of Facts and Contentions, "
            "and the Appellant's List of Documents remains the disclosure.", WARN))
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
