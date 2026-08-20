#!/usr/bin/env python3
"""WC/2024/227 - FURTHER DIRECTIONS ORDER (3) PACK, built 20 August 2026.

Three outputs:
  out/FDO3_ACTION_PACK_INTERNAL.pdf        - the whole plan. INTERNAL, never served.
  out/FDO3_WITNESS_LIST_DRAFT.pdf          - direction 1. FILE + SERVE (once finalised).
  out/FDO3_OUTLINE_Shepherd_DRAFT.pdf      - direction 2. SERVE ONLY, DO NOT FILE.

House style: A4, Helvetica, red internal footers on internal documents, metadata stripped.
No emoji in rendered strings (they render as black boxes in Helvetica).
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, KeepTogether)

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=13,
                    leading=16.5, spaceAfter=3)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.6,
                    leading=13.8, spaceBefore=11, spaceAfter=4,
                    backColor=colors.HexColor('#eeeeee'), borderPadding=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.6,
                      leading=13.2, spaceAfter=6)
ITEM = ParagraphStyle('ITEM', parent=BODY, leftIndent=10, spaceBefore=3, spaceAfter=3)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=9.2, leading=12.6,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=6)
QUOTE = ParagraphStyle('QUOTE', parent=BODY, leftIndent=12, rightIndent=8, fontSize=9.2,
                       leading=12.6, textColor=colors.HexColor('#1a3a5c'),
                       backColor=colors.HexColor('#f2f6fa'), borderPadding=5)
CEN = ParagraphStyle('CEN', parent=BODY, alignment=1)
def P(t, s=BODY): return Paragraph(t, s)

def tbl(rows, widths, head=True):
    t = Table(rows, colWidths=widths, repeatRows=1 if head else 0)
    style = [('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
             ('VALIGN', (0,0), (-1,-1), 'TOP'),
             ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
             ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]
    if head: style.append(('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')))
    t.setStyle(TableStyle(style))
    return t

def strip(path):
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    try: del pdf.Root.Metadata
    except (AttributeError, KeyError): pass
    with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
    try: del pdf.Root.Metadata
    except (AttributeError, KeyError): pass
    for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
    pdf.save(path + '.tmp'); pdf.close()
    import os; os.replace(path + '.tmp', path)

# =============================================================== 1. INTERNAL ACTION PACK
s = []
s.append(P("Further Directions Order (3) - the action pack", H1))
s.append(P("WC/2024/227 Shepherd v Workers' Compensation Regulator &nbsp;|&nbsp; order dated "
           "19 August 2026, received 20 August 2026 &nbsp;|&nbsp; built 20 August 2026", SMALL))
s.append(P("<b>INTERNAL. This document is never filed, never served, and never shown to the "
           "practice, the Regulator, the employer or the union.</b> Every quotation from the QIRC "
           "Workers' Compensation Appeal Guide (version 2.10, 11 March 2025) and the Industrial "
           "Relations (Tribunals) Rules 2011 below was verified from source on 20 August 2026.", WARN))

s.append(P("THE ORDER, IN ONE TABLE", H2))
s.append(tbl([
    [P("<b>Dir.</b>", SMALL), P("<b>Who</b>", SMALL), P("<b>What</b>", SMALL), P("<b>By</b>", SMALL)],
    [P("1", SMALL), P("<b>Appellant</b>", SMALL),
     P("<b>File in the Registry AND serve</b> a list of names of all witnesses", SMALL),
     P("<b>4pm Wed 9 Sept 2026</b>", SMALL)],
    [P("2", SMALL), P("<b>Appellant</b>", SMALL),
     P("<b>Serve, do NOT file</b> - an outline of evidence per lay witness (one A4 page each), "
       "<b>as well as any expert reports relied upon</b>", SMALL),
     P("<b>4pm Wed 9 Sept 2026</b>", SMALL)],
    [P("3", SMALL), P("Respondent", SMALL), P("File and serve its witness list", SMALL),
     P("4pm Wed 30 Sept 2026", SMALL)],
    [P("4", SMALL), P("Respondent", SMALL), P("Serve, not file - outlines and expert reports", SMALL),
     P("4pm Wed 30 Sept 2026", SMALL)],
    [P("5", SMALL), P("<b>Appellant</b>", SMALL),
     P("Contact the Registry to proceed to a <b>second s 552A conference, or to hearing</b>. "
       "Warning that inaction may lead to abeyance and lapse under rule 230", SMALL),
     P("after directions complete", SMALL)],
], [12*mm, 22*mm, 92*mm, 30*mm]))
s.append(Spacer(1, 2*mm))
s.append(P("Opening recital: <i>\"FURTHER TO the correspondence of the Appellant dated 10 August "
           "2026\"</i> - i.e. the order issues in response to the withdrawal of the rule 64G "
           "application. Nine days from withdrawal to order. Signed J.C. Dwyer, Industrial "
           "Commissioner; sealed.", BODY))

s.append(P("WHAT THE ORDER DOES NOT SAY - AND IT IS ALL FAVOURABLE", H2))
s.append(P("No mention of the rule 64G application, the Form 29, Metro South Health, the mention "
           "of 7 August 2026, any concession made at it, or costs. This is the safe form: recite "
           "the letter, characterise nothing. <b>Nothing adverse about that hour exists on the "
           "record, and the non-party is simply gone from the matter.</b>", BODY))

s.append(P("[1] THE FIRST PROBLEM IS NOT THE DEADLINE - IT IS THE PRECONDITION", H2))
s.append(P("The working record of the consultation of <b>12 August 2026</b> states: <i>\"Dr K will "
           "not produce the report responding to the employer's medical inquiry until the employer "
           "identifies WHY the information was requested.\"</i> The same entry flagged an open "
           "question - whether that precondition extends to the causation report on Cory's own "
           "instruction - and <b>that question was never closed</b> before the instruction was sent "
           "on 17 August. The 17 August redesign merged both reports into one.", BODY))
s.append(P("<b>RISK: the appeal's causation evidence may be gated on Metro South Health answering "
           "a basis question it has not answered in seven weeks.</b> Resolve it with one neutral "
           "question to the practice today - do not name the precondition, do not argue it, simply "
           "ask what is outstanding.", WARN))

s.append(P("THE CRITICAL PATH", H2))
s.append(tbl([
    [P("<b>Date</b>", SMALL), P("<b>Do</b>", SMALL)],
    [P("<b>Thu 20 Aug</b>", SMALL), P("<b>Email the practice</b> - timeframe, and what is "
        "outstanding at their end. The only thing that must go today.", SMALL)],
    [P("Thu 20 Aug", SMALL), P("Begin the witness list and the outlines - the half entirely "
        "within your control.", SMALL)],
    [P("Fri 21 Aug", SMALL), P("Roberts / Petering meeting. The appeal timetable does NOT enter "
        "that room - unless the practice says the report is gated on MSH, in which case put the "
        "basis question in writing the same day.", SMALL)],
    [P("Mon 24 Aug", SMALL), P("Employment track: cl 10.3.6 deemed refusal. Verify the EB12 clause "
        "numbering before citing it.", SMALL)],
    [P("Wed 26 Aug", SMALL), P("If the report date is after ~2 Sept: consent email to Ms Matheson, "
        "asking her attitude by Fri 28 Aug.", SMALL)],
    [P("Fri 28 Aug", SMALL), P("If the practice is silent: telephone, ask the same question, then "
        "record the answer in a one-line email.", SMALL)],
    [P("Mon 31 Aug", SMALL), P("Registry extension email.", SMALL)],
    [P("<b>Wed 2 Sept</b>", SMALL), P("<b>HARD BACKSTOP for the registry email. Never later.</b>", SMALL)],
    [P("<b>Wed 9 Sept 4pm</b>", SMALL), P("<b>FILE + SERVE</b> the witness list. <b>SERVE</b> the "
        "outlines and any expert report.", SMALL)],
    [P("Wed 9 Sept", SMALL), P("Calderbank #3 - only if the report is in hand. 21 days, expiring "
        "about 30 Sept.", SMALL)],
    [P("<b>Wed 30 Sept</b>", SMALL), P("<b>The Respondent's list lands. Check it for Ms Taylor and "
        "Ms Reese.</b>", SMALL)],
    [P("Early Oct", SMALL), P("Decide direction 5: second conference or hearing.", SMALL)],
], [26*mm, 130*mm]))

s.append(PageBreak())
s.append(P("[2] THE TRAP THAT GOVERNS THE WITNESS LIST", H2))
s.append(P("QIRC Workers' Compensation Appeal Guide, Part 7.6.2, verbatim:", BODY))
s.append(P("\"After the examination-in-chief has finished, <b>the party who did not call the "
           "witness</b> will conduct the cross-examination.\"", QUOTE))
s.append(P("<b>If you list Ms Taylor, you call her. You then conduct examination-in-chief - no "
           "leading questions, no confrontation - and Ms Willson cross-examines her.</b> The route "
           "the Commission itself identified on 7 August (put it to her, and the Regulator must "
           "then displace it) <b>exists only if the Respondent calls her</b>.", WARN))
s.append(P("The hearing plan at skill/references/HEARING-PLAN.md section 4.0 previously said the "
           "opposite - that if they do not call her, she should be listed and summonsed. That has "
           "been corrected in the file. Listing and summonsing gets her into the room; it does not "
           "get you cross-examination.", BODY))
s.append(P("Guide Part 4.9 also sets the test for who belongs on the list: the persons listed "
           "<i>\"should be reflected in the facts set out in your Statement of Facts and "
           "Contentions\"</i>; and <i>\"If you fail to call someone who could provide relevant "
           "evidence to your matter it may count against your case.\"</i> That warning is answered "
           "by the reservation paragraph in the covering letter, not by listing people.", BODY))

s.append(P("[3] THE EXTENSION - SHAPE OF THE ASK", H2))
s.append(P("Guide Part 4.4, verbatim: <i>\"An extension can be sought by submitting the request in "
           "writing to qirc.registry@qirc.qld.gov.au and explaining why the extension is sought. "
           "<b>A brief email will be sufficient.</b> You should also ask the other party, or "
           "parties, whether they consent to the extension of time. Within your request for "
           "extension you <b>must</b> inform the Registry or the Commission of the other party or "
           "parties' attitude to the extension, if known.\"</i>", QUOTE))
for t in [
  "<b>Extension, never vacation.</b> Direction 5 makes progress an affirmative duty. Asking to "
  "unwind a timetable days after it was set reads as retreat.",
  "<b>Direction 2, expert reports only.</b> Comply in full with direction 1 and with the lay "
  "outlines - both are entirely within your control.",
  "<b>Never touch directions 3 or 4.</b>",
  "<b>Propose 4pm 30 September 2026</b> - the date the Commission has already fixed by directions "
  "3 and 4. Nothing moves, and the Respondent loses not one day. Lighter alternative to offer in "
  "the same letter: serve any expert report within seven days of receipt and in any event by that date.",
  "<b>The strongest paragraph is already on the record.</b> The List of Documents served 5 August "
  "2026 states at Part 5, verbatim: <i>\"The Appellant will disclose, upon receipt, the report of "
  "his treating psychiatrist addressing diagnosis, causation and chronology.\"</i> The Respondent "
  "has been on notice for a fortnight. This is not late notice.",
  "<b>Precedent in this matter:</b> on 22 August 2025 this registry vacated a directions order on "
  "the appellant's own written correspondence, the next day.",
]: s.append(P("- " + t, ITEM))

s.append(P("[4] DIRECTION 5 - WHAT A SECOND s 552A CONFERENCE ACTUALLY IS", H2))
s.append(P("<b>Correction to an earlier working assumption.</b> Guide Part 5.1, boxed, verbatim:", BODY))
s.append(P("\"<b>No commercial settlement is possible at the conference. Conferences for workers' "
           "compensation matters are not intended to facilitate conciliations.</b> Following the "
           "conference, the Respondent may decide to review its position or <b>consider conceding "
           "the appeal where new information is presented that they may not have yet "
           "considered.</b>\"", QUOTE))
s.append(P("So it is not a settlement vehicle - it is a <b>concession opportunity</b>, and the new "
           "information is the report. Guide 5.1 also states: <i>\"The Member of the Commission who "
           "chairs such a conference will not be the Member who hears the appeal\"</i> - so "
           "<b>Commissioner Dwyer will not hear this appeal</b>, and would chair a second conference.", BODY))
s.append(P("<b>Decide in early October, not now</b>, on two inputs: what the report says, and what "
           "the Respondent serves on 30 September. Recommended shape when the time comes: request "
           "the conference and, in the alternative, ask that if the Commission considers a "
           "conference would not assist, the matter be listed for hearing. That converts the fork "
           "into a single request that cannot produce a null result.", BODY))
s.append(P("<b>Rule 230</b> (Industrial Relations (Tribunals) Rules 2011, p 138) requires "
           "<i>\"no action ... for at least 1 year since the last action was taken by the "
           "applicant\"</i>. The abeyance warning is boilerplate, not a near-term threat - but it "
           "is why every step from here should look like progression.", BODY))

s.append(PageBreak())
s.append(P("[5] MECHANICS - THE THINGS THAT ARE EASY TO GET WRONG", H2))
for t in [
  "<b>Direction 1 is FILE AND SERVE. Direction 2 is SERVE ONLY - do not file the outlines or the "
  "report.</b> This is the commonest self-represented error.",
  "No prescribed form for the list. Guide 4.9: <i>\"there is no set form for this\"</i>.",
  "Filing: qirc.registry@qirc.qld.gov.au, business hours, under 30 pages (Practice Direction 3/2021).",
  "Outlines: Guide 4.10 - <i>\"You do not need to fill the entire A4 page, it is just a brief "
  "overview of the material they will cover.\"</i> Brevity is compliance, not weakness.",
  "<b>Experts go on the direction 1 list as well.</b> Direction 1 says \"all witnesses\"; direction "
  "2 merely substitutes the report for the one-page outline in an expert's case.",
  "Guide 7.6.5, boxed: <i>\"presenting a medical report on its own cannot be considered without "
  "having the expert witness give evidence orally to support that document and being available for "
  "cross-examination by the other party.\"</i> The report alone is worth little - Dr Krishnaiah must "
  "be available.",
  "Witness costs, Guide 10.1: travel plus conduct money at the Supreme Court civil rate, and "
  "<i>\"Expert witnesses are entitled to a higher rate\"</i>. No wages since 13 July 2026 - an "
  "independent reason for a two or three name list.",
  "Attendance notices (Form 32 and 32A/B/C) come later, after hearing dates are set - Guide 7.6.4. "
  "Nothing to do about compulsion now.",
  "<b>WCRA s 554</b>, separate from this order: exchange every document to be adduced at least "
  "<b>10 business days</b> before the hearing, or lose the right to rely on it.",
]: s.append(P("- " + t, ITEM))

s.append(P("[6] CALDERBANK #3 - TIMING", H2))
for t in [
  "Serve the report <b>alone</b> the moment it arrives, as continuing disclosure, with no offer "
  "attached. Disclosure carries no ask; an offer bundled with it contaminates it.",
  "Make the offer <b>on 9 September or the next business day</b>, open 21 days, expiring about "
  "30 September - the Respondent's own directions date. Their authorisation loop ran 15 days on "
  "offer #2, so a 10 September send expires 1 October: one day too late.",
  "<b>If the report has not arrived by early September, do not make the offer.</b> Its entire "
  "value is a function of the new material. Hold it.",
  "Reserve window: about seven days after a second s 552A conference - the last cheap moment "
  "before hearing preparation costs land.",
  "Scope: the compensation appeal only. The parallel tracks are expressly reserved. Regulator only; "
  "never to the employer.",
  "Offers #1 and #2 were rejected when the causation field was empty, and both rejections were "
  "defensible on that basis. What makes #3 different must be visible in its first three lines.",
]: s.append(P("- " + t, ITEM))

s.append(P("[7] THE LEAKAGE RULE - THE HIGHEST-CONSEQUENCE DISCIPLINE FROM NOW TO OCTOBER", H2))
s.append(P("The two tracks share one document - the report - and nothing else. Between now and "
           "9 September you will be drafting employment-track and appeal-track material on the same "
           "days.", BODY))
s.append(P("<b>Employment vocabulary</b> - psychosocial hazard, exclusion, conflict of interest, "
           "Stage 1 and Stage 2, reasonable adjustment, the public interest disclosure - <b>must "
           "not appear anywhere in the 9 September package.</b><br/>"
           "<b>Appeal vocabulary</b> - the statutory exclusion, reasonable management action, the "
           "Regulator's admissions, the seven-hour break as a pleaded breach - <b>must not appear "
           "in anything sent to HR, the union or the practice.</b><br/><br/>"
           "<b>The test, on every document before it leaves: could this sentence be quoted back at "
           "me in the other matter?</b>", WARN))

s.append(P("[8] OPEN ITEMS", H2))
for i, t in enumerate([
  "<b>The precondition boundary.</b> The whole plan branches on it. Answered by the practice email.",
  "<b>Full legal names</b> for the list, verified from a primary source. The record carries "
  "\"Chloe Taylor\", \"Chloe Jane Taylor\" and \"Chloe Donovan-Taylor\"; and there is a different "
  "person, Chloe Tyler, in 2025 correspondence - do not confuse them. Verify Dr Krishnaiah's full "
  "name from his own letterhead.",
  "<b>Whether Metro South ever served a notice of its reasonable expenses of production</b> under "
  "rule 64I - due about 11 July 2026. If none was served the point is spent by effluxion of time. "
  "Do not raise it with them.",
  "<b>Ms Carolyn Jeffrey.</b> Your decision. Recommendation: do not name her on 9 September.",
  "<b>Paragraph 7 of the outline</b> - whether the complaint of 13 May 2024 gets a bare factual line.",
], 1): s.append(P(f"<b>{i}.</b> {t}", ITEM))

doc = SimpleDocTemplate("out/FDO3_ACTION_PACK_INTERNAL.pdf", pagesize=A4,
                        leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm)
def f_int(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7.2)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(18*mm, 9*mm, "INTERNAL - NOT FOR FILING, SERVICE, THE PRACTICE, THE EMPLOYER OR THE UNION")
    c.setFont('Helvetica', 7.2); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-18*mm, 9*mm, f"Page {d.page}")
    c.restoreState()
doc.build(s, onFirstPage=f_int, onLaterPages=f_int)
strip("out/FDO3_ACTION_PACK_INTERNAL.pdf")
print("built out/FDO3_ACTION_PACK_INTERNAL.pdf")

# =============================================================== 2. WITNESS LIST (direction 1)
TITLE = ParagraphStyle('TITLE', parent=H1, alignment=1, fontSize=12)
SUB = ParagraphStyle('SUB', parent=BODY, alignment=1, fontSize=9.4)

w = []
w.append(P("DRAFT FOR FINALISATION - NOT YET FILED. Verify every full legal name from a primary "
           "source, close the bracketed choice at item 3, insert the date, then delete this box.",
           WARN))
w.append(P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", TITLE))
w.append(P("<i>Workers' Compensation and Rehabilitation Act 2003</i>", SUB))
w.append(Spacer(1, 3*mm))
w.append(P("<b>CORY LEA SHEPHERD</b><br/>Appellant", SUB))
w.append(P("v", SUB))
w.append(P("<b>WORKERS' COMPENSATION REGULATOR</b><br/>Respondent", SUB))
w.append(P("<i>Matter No. WC/2024/227</i>", SUB))
w.append(Spacer(1, 4*mm))
w.append(P("APPELLANT'S LIST OF NAMES OF ALL WITNESSES", TITLE))
w.append(P("Filed and served pursuant to direction 1 of the Further Directions Order (3) dated "
           "19 August 2026", SUB))
w.append(Spacer(1, 5*mm))
w.append(P("The Appellant will call the following witnesses at the hearing:", BODY))
w.append(tbl([
    [P("<b>No.</b>", SMALL), P("<b>Name</b>", SMALL), P("<b>Capacity</b>", SMALL)],
    [P("1", BODY), P("<b>Cory Lea Shepherd</b>", BODY), P("Appellant", BODY)],
    [P("2", BODY), P("<b>Dr Ravikumar Bangalore Krishnaiah</b>", BODY),
     P("Consultant Psychiatrist, Mind and Memory Service - the Appellant's treating psychiatrist", BODY)],
    [P("3", BODY), P("[<b>Dr Peter Hawes</b>]", BODY),
     P("[General Practitioner - the Appellant's treating general practitioner at the date of "
       "injury]", BODY)],
], [14*mm, 60*mm, 90*mm]))
w.append(Spacer(1, 8*mm))
w.append(P("Cory Lea Shepherd<br/>Appellant (self-represented)<br/>[date]", BODY))
w.append(PageBreak())

w.append(P("Covering letter - to accompany the filing", H1))
w.append(P("To: qirc.registry@qirc.qld.gov.au &nbsp;|&nbsp; Copy to: Renee.Matheson@oir.qld.gov.au",
           SMALL))
w.append(Spacer(1, 3*mm))
w.append(P("Dear Registrar,", BODY))
w.append(P("<b>WC/2024/227 - Cory Lea Shepherd v Workers' Compensation Regulator</b>", BODY))
w.append(P("In accordance with direction 1 of the Further Directions Order (3) dated 19 August "
           "2026, I file and serve the Appellant's list of names of all witnesses. In accordance "
           "with direction 2, I have today served on the Respondent an outline of the evidence of "
           "each lay witness. [<i>Expert reports - insert per the position actually reached.</i>]", BODY))
w.append(P("For completeness, and so that the position is clear on the record: the Appellant does "
           "not presently propose to call Ms Chloe Taylor or Ms Tammy Reese. Their evidence is "
           "material to the matters pleaded, and the Appellant proceeds on the basis that the "
           "Respondent will call them. If the Respondent's list filed by 30 September 2026 does not "
           "include them, the Appellant will apply promptly for leave to amend this list and to "
           "serve the necessary outlines.", BODY))
w.append(P("Yours sincerely,<br/><br/>Cory Lea Shepherd<br/>Appellant (self-represented), "
           "WC/2024/227", BODY))

w.append(P("WHY THIS LIST IS SHORT - INTERNAL NOTE, DELETE BEFORE FILING", H2))
w.append(P("<b>Ms Taylor and Ms Reese are deliberately not listed.</b> Guide 7.6.2: the party who "
           "did not call the witness conducts the cross-examination. Listing them means examining "
           "them in chief and handing their cross-examination to the Regulator - which destroys the "
           "route the Commission identified on 7 August. It would also require serving a one-page "
           "outline of Ms Taylor's evidence on 9 September, three weeks before the Regulator "
           "discloses, telegraphing the cross-examination to the people preparing her. And under "
           "Guide 10.1 the party calling a witness pays their travel and conduct money.", SMALL))
w.append(P("<b>They are very likely to be called by the Respondent</b>, whose pleading repeatedly "
           "characterises their conduct as reasonable - a characterisation of a person's conduct is "
           "not provable on documents alone - and which conferenced with both of them in July 2025, "
           "as its own amended List of Documents records. <b>Diarise 30 September</b> and check.", SMALL))
w.append(P("<b>Not listed, and why:</b> Switchboard colleagues, union officers, Ethical Standards "
           "Unit officers, the WorkCover and Review Unit decision-makers, and family members. Most "
           "go to facts already admitted; several are current employees exposed to detriment; each "
           "costs conduct money; and a witness who is off-pleading invites the objection that the "
           "case being run is not the case pleaded. <b>Ms Carolyn Jeffrey is a decision for Cory</b> "
           "- recommendation: do not name her on 9 September.", SMALL))

docw = SimpleDocTemplate("out/FDO3_WITNESS_LIST_DRAFT.pdf", pagesize=A4,
                         leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=16*mm)
def f_w(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7.2)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(20*mm, 9*mm, "DRAFT - direction 1 - FILE IN THE REGISTRY AND SERVE ON THE RESPONDENT")
    c.setFont('Helvetica', 7.2); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-20*mm, 9*mm, f"Page {d.page}")
    c.restoreState()
docw.build(w, onFirstPage=f_w, onLaterPages=f_w)
strip("out/FDO3_WITNESS_LIST_DRAFT.pdf")
print("built out/FDO3_WITNESS_LIST_DRAFT.pdf")

# =============================================================== 3. OUTLINE OF EVIDENCE (direction 2)
o = []
o.append(P("DRAFT FOR FINALISATION - SERVE ON THE RESPONDENT ONLY, DO NOT FILE. Close paragraph 7, "
           "insert the date, then delete this box. Sources are on page 2 for verification and are "
           "NOT part of the served document.", WARN))
o.append(P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", TITLE))
o.append(P("<b>CORY LEA SHEPHERD</b> (Appellant) v <b>WORKERS' COMPENSATION REGULATOR</b> "
           "(Respondent) &nbsp;|&nbsp; <i>Matter No. WC/2024/227</i>", SUB))
o.append(Spacer(1, 3*mm))
o.append(P("OUTLINE OF EVIDENCE - CORY LEA SHEPHERD", TITLE))
o.append(P("Served pursuant to direction 2 of the Further Directions Order (3) dated 19 August 2026", SUB))
o.append(Spacer(1, 4*mm))
for n, t in [
 ("1. Employment.", "I have been employed by Metro South Hospital and Health Service since 2019, as "
  "an Administration Officer (AO3), Switchboard Services, Logan Hospital. I moved from casual to "
  "part-time hours and then, on the approval of my line manager dated 27 September 2023, to "
  "permanent full-time hours commencing 16 October 2023."),
 ("2. The work.", "The position is a continuous shift working role covering the full 24-hour "
  "period, seven days a week. My duties included participation in the hospital's Emergency Response "
  "process and the distribution of emergency code notifications, maintaining call queues, and "
  "maintaining the Omnivista database and SharePoint. I handled approximately 200 to 300 calls per "
  "shift."),
 ("3. Rostering, 17 to 19 March 2024.", "I was rostered to finish at 23:00 on 17 March 2024 and to "
  "commence again at 06:00 on 18 March 2024, an interval of seven hours. Emergency (MET) calls were "
  "recorded on those shifts. I took leave on 19 March 2024. I will give evidence of the effect of "
  "that sequence on my sleep and on my functioning."),
 ("4. Fatigue management.", "No fatigue risk assessment applied to my position at any time before "
  "30 June 2024, and I received no fatigue risk management training for it."),
 ("5. Rostering, leave and pay administration.", "I will give evidence of: an email of 7 August "
  "2023 in which my line manager confirmed a rostering error as an oversight; a leave application "
  "for 20 to 27 February 2024 declined for a missing attachment, which a later review found had in "
  "fact been attached; and a payroll instruction issued on 3 May 2024 to correct my shifts, with "
  "the correction submitted on 28 May 2024."),
 ("6. Raising the matters.", "I will give evidence of raising rostering, fatigue, leave and pay "
  "matters with my line manager and with the Director between August 2023 and May 2024, including "
  "my email of 7 August 2023, my email of 1 May 2024 concerning rostering and the fatigue toolkit, "
  "and the responses I received."),
 ("7. May 2024.", "[<i>CLOSE THIS PARAGRAPH - see the note on page 2.</i>]"),
 ("8. Onset and presentation.", "I will give evidence of the onset of my symptoms, of my inability "
  "to attend rostered shifts on 13, 14 and 15 May 2024, and of first presenting to my general "
  "practitioner on 1 July 2024 in relation to work-related stress."),
 ("9. Since.", "I will give evidence of my treatment since 2024, of the hours I have in fact "
  "worked, and of my present capacity."),
]:
    o.append(P(f"<b>{n}</b> {t}", BODY))
o.append(Spacer(1, 5*mm))
o.append(P("Cory Lea Shepherd<br/>Appellant (self-represented)<br/>[date]", BODY))

o.append(PageBreak())
o.append(P("Sources and drafting notes - NOT part of the served document", H1))
o.append(P("Each proposition above, with the source to verify it against before service.", SMALL))
o.append(tbl([
    [P("<b>Para</b>", SMALL), P("<b>Verify against</b>", SMALL)],
    [P("1", SMALL), P("Full-time approval email, C Taylor, 27 September 2023", SMALL)],
    [P("2", SMALL), P("AO3 Switchboard Services role description (served on the Respondent 17 August 2026)", SMALL)],
    [P("3", SMALL), P("Notice to admit facts item 1 and the Respondent's response; Respondent's "
                      "statement of facts and contentions at paragraph 22(a); Chief Executive's "
                      "letter of 5 June 2026, items 1 and 2; leave takings report, 19 March 2024", SMALL)],
    [P("4", SMALL), P("Chief Executive's letter of 5 June 2026, items 4, 5 and 7", SMALL)],
    [P("5", SMALL), P("Taylor email 7 August 2023; notice to admit facts paragraph 14 and the "
                      "response; notice to admit facts paragraphs 40 and 41", SMALL)],
    [P("6", SMALL), P("Email chains of 7 August 2023 and 1 May 2024, in the Respondent's disclosure", SMALL)],
    [P("8", SMALL), P("Respondent's statement of facts and contentions, paragraph 16(b)(i); work "
                      "capacity certificate of Dr P Hawes, 1 July 2024", SMALL)],
], [14*mm, 150*mm]))
o.append(P("PARAGRAPH 7 - THE ONE DECISION", H2))
o.append(P("Stressor 1(e) is pleaded, and the Respondent has <b>admitted it in full</b>: the "
           "complaint of 13 May 2024 and the Ethical Standards Unit's determination that it "
           "constituted a public interest disclosure. Two options:", BODY))
o.append(P("<b>(a) One factual line</b> - \"I will give evidence that on 13 May 2024 I made a "
           "complaint concerning conduct in my workplace, and that on 24 December 2024 the Ethical "
           "Standards Unit determined that it constituted a Public Interest Disclosure.\"<br/>"
           "<b>(b) Omit the paragraph entirely</b>, on the footing that the fact is admitted and "
           "needs no evidence.", ITEM))
o.append(P("<b>Recommendation: (a), bare fact only.</b> It is pleaded, and the Guide warns that "
           "failing to call evidence on a pleaded matter may count against you. Under neither "
           "option does any word of motive, reprisal or consequence appear.", BODY))
o.append(P("DRAFTING DISCIPLINE", H2))
for t in [
 "<b>No adjectives.</b> Not \"erratic\", not \"unreasonable\", not \"unfair\". Dates and events only.",
 "<b>Nothing about your perception of management action.</b> That is the door the Respondent has "
 "not pleaded and must not be opened.",
 "<b>Nothing about the employment dispute</b> - the 2026 exclusion, the request for medical "
 "information, the union, or pay since July 2026. None of it is in this appeal.",
 "<b>Admitted facts need no evidence.</b> What is above is there to frame your own account, not to "
 "prove twice what the Respondent has already conceded.",
 "<b>Brevity is compliance.</b> Guide 4.10: \"You do not need to fill the entire A4 page, it is "
 "just a brief overview of the material they will cover.\" Serving three weeks before the "
 "Respondent, the outline should convey the shape and leave the detail to oral evidence.",
]: o.append(P("- " + t, ITEM))

doco = SimpleDocTemplate("out/FDO3_OUTLINE_Shepherd_DRAFT.pdf", pagesize=A4,
                         leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=16*mm)
def f_o(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7.2)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(20*mm, 9*mm, "DRAFT - direction 2 - SERVE ON THE RESPONDENT ONLY, DO NOT FILE")
    c.setFont('Helvetica', 7.2); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-20*mm, 9*mm, f"Page {d.page}")
    c.restoreState()
doco.build(o, onFirstPage=f_o, onLaterPages=f_o)
strip("out/FDO3_OUTLINE_Shepherd_DRAFT.pdf")
print("built out/FDO3_OUTLINE_Shepherd_DRAFT.pdf")

# =============================================================== 4. THE THREE EMAILS
e = []
e.append(P("The three emails - FDO(3)", H1))
e.append(P("WC/2024/227 &nbsp;|&nbsp; built 20 August 2026", SMALL))
e.append(P("<b>INTERNAL. These are templates to TYPE FROM. This PDF is never attached to anything.</b> "
           "Email 1 goes today. Emails 2 and 3 are held and sent only per the branch table.", WARN))

e.append(P("EMAIL 1 - TO THE PRACTICE. SEND TODAY (Thursday 20 August).", H2))
e.append(P("Send as a <b>reply on the 17 August thread</b>. Do not re-attach the pack. Assume it is "
           "produced to the Regulator under the notice the practice holds - nothing strategic is in "
           "it. This is within the standing rule (nothing further to the practice unless they ask), "
           "because the covering email of 17 August already asked for a timeframe: this is a chase "
           "on an unanswered administrative question.", SMALL))
e.append(P("<b>Subject:</b> (reply on the 17 August thread) - expected timeframe", SMALL))
e.append(Spacer(1, 2*mm))
for t in [
 "Dear Dr Krishnaiah,",
 "I refer to the letter of instruction and attachments I sent on 17 August 2026, and to my request "
 "in that email that you confirm the time you would require.",
 "Could you please let me know the timeframe you expect. I ask only so that I can give an accurate "
 "answer to the Queensland Industrial Relations Commission, which has asked the parties to identify "
 "any expert report by 9 September 2026. If the report will not be ready by then, that is not a "
 "difficulty - I will tell the Commission the date you give me and ask for that time. The date is a "
 "procedural matter for me to manage. It has no bearing on the content of the report, and I do not "
 "ask you to work to it.",
 "It would also assist if you could confirm:",
 "(a) whether any further consultation, record or other material is required before the report can "
 "be prepared; and",
 "(b) whether anything remains outstanding at your end, including anything you may be awaiting from "
 "Metro South Hospital and Health Service.",
 "If it is easier, a one-line reply with an approximate number of weeks is all I need.",
 "Kind regards,<br/>Cory Lea Shepherd<br/>0417 400 227 &middot; coryshepherd1@hotmail.com",
]: e.append(P(t, ITEM))
e.append(P("<b>Why it is worded this way.</b> It gives the doctor the date without giving him a "
           "deadline, and expressly removes the pressure - a report written to a litigation deadline "
           "is attackable, and this email is the answer to that attack. <b>Question (b) is the "
           "important one</b>: it surfaces the 12 August precondition without naming it or arguing "
           "about it. If the answer is that the practice is waiting on Metro South, act the same "
           "day. Do not mention the withdrawal, the mention, the Respondent, settlement, cost or "
           "the fee - funding is closed and re-opening it invites a cap. If no reply by Friday "
           "28 August, telephone, ask the same question, and record the answer in a one-line email.",
           SMALL))

e.append(PageBreak())
e.append(P("EMAIL 2 - TO THE RESPONDENT (consent). HOLD.", H2))
e.append(P("The Guide requires the Registry to be told the other party's attitude, so this goes "
           "first. Send Wednesday 26 August if the report date is after about 2 September, or "
           "Monday 31 August if the practice is silent.", SMALL))
e.append(P("<b>To:</b> Renee.Matheson@oir.qld.gov.au &nbsp;<b>Cc:</b> the OIR appeals registry<br/>"
           "<b>Subject:</b> WC/2024/227 - Shepherd - Further Directions Order (3) - extension of "
           "direction 2 (expert report)", SMALL))
e.append(Spacer(1, 2*mm))
for t in [
 "Dear Ms Matheson,",
 "I refer to the Further Directions Order (3) dated 19 August 2026.",
 "I will comply with direction 1, and with direction 2 so far as it concerns the outlines of the "
 "evidence of lay witnesses, by 4.00 pm on 9 September 2026.",
 "On 17 August 2026 I instructed my treating psychiatrist to prepare a report addressing the "
 "matters in issue in the appeal. The report has not yet been provided and I am not presently able "
 "to say that it will be available by 9 September 2026. As my list of documents served on 5 August "
 "2026 recorded at Part 5, I will disclose it upon receipt.",
 "Before writing to the Industrial Registry I would be grateful to know whether the Regulator "
 "consents to an extension of direction 2, so far as it concerns expert reports, to 4.00 pm on "
 "30 September 2026 - the date already fixed by directions 3 and 4 - or alternatively to a "
 "direction that I serve any expert report within seven days of receiving it and in any event by "
 "that date. No other date would be affected and I do not seek any change to directions 3 or 4.",
 "I would be grateful for the Regulator's attitude by Friday 28 August 2026 so that I can inform "
 "the Commission accurately.",
 "Kind regards,<br/>Cory Lea Shepherd<br/>Appellant (self-represented), WC/2024/227",
]: e.append(P(t, ITEM))

e.append(P("EMAIL 3 - TO THE REGISTRY (extension). HOLD.", H2))
e.append(P("Send Monday 31 August. <b>Hard backstop Wednesday 2 September - never on 9 September.</b> "
           "Guide 4.4: \"A brief email will be sufficient.\" Keep it to one page. Square brackets "
           "are choices to close before sending.", SMALL))
e.append(P("<b>To:</b> qirc.registry@qirc.qld.gov.au - Attention: Chambers of Industrial "
           "Commissioner Dwyer &nbsp;<b>Cc:</b> Renee.Matheson@oir.qld.gov.au<br/>"
           "<b>Subject:</b> WC/2024/227 - Shepherd v Workers' Compensation Regulator - request for "
           "extension of time, direction 2 (expert reports only)", SMALL))
e.append(Spacer(1, 2*mm))
for t in [
 "Dear Registrar",
 "<b>WC/2024/227 - Cory Lea Shepherd v Workers' Compensation Regulator</b>",
 "1. I refer to the Further Directions Order (3) dated 19 August 2026.",
 "2. I will file and serve the list of names of all witnesses required by direction 1, and serve "
 "the outline of the evidence of each lay witness required by direction 2, by 4.00 pm on "
 "9 September 2026.",
 "3. I ask for an extension of time in respect of direction 2 only so far as it concerns expert "
 "reports. On 17 August 2026 I instructed my treating psychiatrist, Dr Ravikumar Bangalore "
 "Krishnaiah, Consultant Psychiatrist, to prepare a report addressing the matters in issue in this "
 "appeal. The report has not yet been provided. [<i>The practice has advised that it expects to "
 "provide the report by [date].</i> / <i>The practice has not yet been able to confirm a date, and "
 "I did not wish to delay this request until it does.</i>] I am not in a position to serve by "
 "9 September 2026 a report that does not yet exist.",
 "4. The list of documents I served on the Respondent on 5 August 2026 recorded, at Part 5, that "
 "the report of my treating psychiatrist addressing diagnosis, causation and chronology would be "
 "disclosed upon receipt. The Respondent has been on notice of the report since that date.",
 "5. I ask that direction 2 be extended, so far as it concerns expert reports, to 4.00 pm on "
 "30 September 2026; or alternatively that I be directed to serve any expert report within seven "
 "days of receiving it and in any event by 4.00 pm on 30 September 2026. The extension sought does "
 "not disturb directions 3 and 4, and I seek no change to any other date. [<i>If it would assist "
 "the Respondent, I do not oppose a corresponding extension of directions 3 and 4.</i>]",
 "6. I have asked the Respondent whether it consents. [<i>The Respondent consents. / The Respondent "
 "does not consent. / The Respondent has not yet indicated its attitude and I will inform the "
 "Commission as soon as it does.</i>]",
 "7. I will continue to progress the matter and will contact the Industrial Registry under "
 "direction 5 once the directions have been finalised.",
 "Yours sincerely<br/>Cory Lea Shepherd<br/>Appellant (self-represented), WC/2024/227",
]: e.append(P(t, ITEM))
e.append(P("<b>Paragraph 4 is the strongest paragraph</b> - the Respondent has been on notice since "
           "5 August. <b>Paragraph 7 answers direction 5 before it is asked.</b> Deliberately absent "
           "and to stay absent: the employment dispute, the exclusion, non-payment, the employer's "
           "funding of the report, the request for medical information, the precondition, the union, "
           "the disclosure, the withdrawn application, the mention, cost, settlement, and any "
           "adjective. Nothing else is the Commission's business.", SMALL))

doce = SimpleDocTemplate("out/FDO3_EMAILS_INTERNAL.pdf", pagesize=A4,
                         leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=16*mm)
doce.build(e, onFirstPage=f_int, onLaterPages=f_int)
strip("out/FDO3_EMAILS_INTERNAL.pdf")
print("built out/FDO3_EMAILS_INTERNAL.pdf")
