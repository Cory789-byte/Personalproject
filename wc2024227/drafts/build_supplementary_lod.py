#!/usr/bin/env python3
"""WC/2024/227 — SUPPLEMENTARY LIST OF DOCUMENTS + one-line covering email to Matheson.

⭐ WHY THIS EXISTS, AND WHY IT GOES FIRST (before the pack goes to the practice on Monday):
The letter of instruction asks the psychiatrist to reason from the AO3 role description
(Attachment 3). The Regulator's amended List of Documents (14 Aug 2026) has 52 items and no role
description of any kind. If the report reasons from a document she has never seen, it surfaces
through an expert instead of through disclosure.

⛔⛔ THE MOVEMENT FORMS ARE DELIBERATELY NOT LISTED (Cory, 17 Aug) — AND THE RELEVANCE LINE
SUPPORTS HIM:
  · The ROLE DESCRIPTION is directly relevant to the appeal's matters in issue — the nature and
    conditions of the employment go to causation. It is disclosed now.
  · The MOVEMENT FORMS are 2026 capacity documents. Capacity is the EMPLOYER'S question, not a
    matter in issue in the appeal — and the appeal's own disclosure scope stops at 30 June 2024
    (the Form 29 ranges). Serving 2026 employment-file documents unprompted would open a field
    the appellant has himself said the appeal does not reach, and would hand the Regulator the
    76→56→40 trend BEFORE the clinician's 3.6(e) answer exists to meet it.
  · Their relevance in the appeal arises, if at all, THROUGH the report. So they are produced
    WITH the report at delivery, as part of the expert's materials — the ordinary course. If she
    asks sooner, they are provided on request without argument.

⛔ THE DISCIPLINE (standing, and non-negotiable):
  · Serve the DOCUMENTS, not their provenance. No mention of the request for medical information,
    the psychiatrist, the exclusion, or 31 July 2026.
  · One line. No argument, no commentary, no ask. Disclosure is the one category of communication
    that carries no ask and spends no standing.
  · Written only (discipline rule 4). To Matheson, cc the OIR appeals registry — the same routing
    as the 5 August list.
  · The 5 August list stated on its face that disclosure is continuing and would be supplemented.
    This is that supplement. Nothing about it is novel or explicable — which is the point.
  · ⛔ Nothing else rides along. Not the schedule, not the instruction, not the capability
    checklist (already listed 5 Aug as item 2). Two documents, listed and produced.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=11.5,
                    leading=15, spaceAfter=2, alignment=1)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.2,
                    leading=13.2, spaceBefore=9, spaceAfter=4)
B  = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.4,
                    leading=12.6, spaceAfter=5)
SM = ParagraphStyle('SM', parent=B, fontSize=8.2, leading=10.9,
                    textColor=colors.HexColor('#555555'))
CEN = ParagraphStyle('CEN', parent=B, alignment=1, fontSize=9.2, leading=12.2)
INT = ParagraphStyle('INT', parent=B, fontSize=8.7, leading=11.6, leftIndent=5,
                     textColor=colors.HexColor('#7a2018'),
                     backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
def P(t, s=B): return Paragraph(t, s)

d = []
d.append(P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", H1))
d.append(P("Matter No. WC/2024/227 · <i>Workers' Compensation and Rehabilitation Act 2003</i> (Qld)", CEN))
d.append(P("BETWEEN: <b>CORY LEA SHEPHERD</b> (Appellant) AND: <b>WORKERS' COMPENSATION "
           "REGULATOR</b> (Respondent)", CEN))
d.append(Spacer(1, 3*mm))
d.append(P("APPELLANT'S SUPPLEMENTARY LIST OF DOCUMENTS", H1))
d.append(P("Served on the Respondent · 17 August 2026", CEN))
d.append(P("This supplementary list is given in continuation of the Appellant's disclosure "
           "obligation, supplementing the List of Documents served on 5 August 2026, which stated "
           "that disclosure is continuing. It lists a further document in the Appellant's possession "
           "that is directly relevant to a matter in issue in this proceeding.", B))

rows = [
 [P("<b>Item</b>", SM), P("<b>Date</b>", SM), P("<b>Description</b>", SM),
  P("<b>Author / From</b>", SM), P("<b>Pages</b>", SM), P("<b>Status</b>", SM)],
 [P("S1", SM), P("Undated", SM),
  P("<b>Role description — Administration Officer, Switchboard Services (AO3)</b>, Logan Hospital, "
    "Metro South Hospital and Health Service. Records the position as a continuous shift working "
    "role over the full 24-hour period, 7 days a week; participation in the Emergency Response "
    "process; maintenance of call queues; and maintenance of the Omnivista database and SharePoint.",
    SM),
  P("Metro South Hospital and Health Service", SM), P("[n]", SM), P("Produced herewith", SM)],
]
t = Table(rows, colWidths=[11*mm, 20*mm, 78*mm, 30*mm, 12*mm, 19*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3.5), ('RIGHTPADDING', (0,0), (-1,-1), 3.5),
    ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
d.append(t)
d.append(Spacer(1, 4*mm))
d.append(P("Disclosure remains continuing and this list will be further supplemented as documents "
           "come into the Appellant's possession.", B))
d.append(Spacer(1, 5*mm))
d.append(P("Cory Lea Shepherd<br/>Appellant &nbsp;·&nbsp; 17 August 2026", B))

# ── the servable list ends here; the email + discipline go to a SEPARATE internal file
doc = SimpleDocTemplate("out/SUPPLEMENTARY_LOD_17AUG2026.pdf", pagesize=A4,
                        leftMargin=17*mm, rightMargin=17*mm, topMargin=15*mm, bottomMargin=15*mm,
                        title="WC/2024/227 — Appellant's supplementary list of documents",
                        author="Cory Lea Shepherd")
def f(canv, dd):
    canv.saveState(); canv.setFont('Helvetica', 7.2)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(17*mm, 9*mm, "WC/2024/227 · Appellant's supplementary list of documents · 17 August 2026")
    canv.drawRightString(A4[0]-17*mm, 9*mm, f"Page {dd.page}")
    canv.restoreState()
doc.build(d, onFirstPage=f, onLaterPages=f)
print("built out/SUPPLEMENTARY_LOD_17AUG2026.pdf  (SERVABLE — this file goes to Matheson)")

d = []
d.append(P("SERVICE SHEET — supplementary disclosure to the Regulator", H1))
d.append(P("INTERNAL — this page is not sent", CEN))
d.append(P("COVERING EMAIL — the whole of it", H2))
d.append(P("<b>To:</b> Renee.Matheson@oir.qld.gov.au &nbsp;·&nbsp; <b>Cc:</b> the OIR appeals "
           "registry<br/><b>Subject:</b> WC/2024/227 — Shepherd — supplementary disclosure", SM))
d.append(P("Dear Ms Matheson,<br/><br/>By way of continuing disclosure, I attach a supplementary "
           "list of documents together with the document it lists.<br/><br/>Kind regards,"
           "<br/>Cory Lea Shepherd<br/>Appellant, WC/2024/227", B))
d.append(P("<b>NOTHING FURTHER.</b> No mention of the request for medical information, the "
           "psychiatrist, the report, the exclusion, or any date in July 2026. No explanation of "
           "why these documents or why now — the 5 August list already said disclosure was "
           "continuing, and an explanation is the one thing that would make this email "
           "interesting. <b>Send before the pack goes to the practice.</b>", INT))

d.append(P("THE TWO ATTACHMENTS TO THE EMAIL", H2))
d.append(P("1 · <b>SUPPLEMENTARY_LOD_17AUG2026.pdf</b> — the list itself<br/>"
           "2 · the <b>role description</b> — the document alone, no index page", B))
d.append(P("<b>THE MOVEMENT FORMS ARE NOT SERVED NOW — decided 17 August.</b> They are 2026 "
           "capacity documents; capacity is the employer's question, not a matter in issue in the "
           "appeal, and the appeal's disclosure scope stops at 30 June 2024. Their relevance in the "
           "appeal arises, if at all, through the report — so they are produced <b>with the report "
           "at delivery</b>, as part of the expert's materials, which is the ordinary course. If "
           "the Regulator asks for them sooner (the letter of instruction and schedule she receives "
           "with the report describe them), <b>provide them on request, without argument</b>.", INT))
d.append(P("<b>SEQUENCE.</b> Send this FIRST on Monday morning, then the pack to the practice. "
           "Same-day is sufficient; the order is what matters — the Regulator must hold the role "
           "description before the practice holds an instruction that reasons from it.", INT))
d.append(P("<b>AND AFTERWARDS:</b> when the report is later disclosed, the covering note already "
           "says the same report went to both parties. Nothing in this service sheet is ever "
           "referred to again — a supplement to a continuing-disclosure list needs no follow-up.", B))

doc2 = SimpleDocTemplate("out/SUPPLEMENTARY_LOD_service_sheet_INTERNAL.pdf", pagesize=A4,
                        leftMargin=17*mm, rightMargin=17*mm, topMargin=15*mm, bottomMargin=15*mm,
                        title="WC/2024/227 — service sheet (internal)",
                        author="Internal working document")
def f2(canv, dd):
    canv.saveState(); canv.setFont('Helvetica-Bold', 7.2)
    canv.setFillColor(colors.HexColor('#8a2010'))
    canv.drawString(17*mm, 9*mm, "INTERNAL — NOT FOR SERVICE")
    canv.restoreState()
doc2.build(d, onFirstPage=f2, onLaterPages=f2)
print("built out/SUPPLEMENTARY_LOD_service_sheet_INTERNAL.pdf  (INTERNAL)")
