#!/usr/bin/env python3
"""WC/2024/227 - SECOND NOTICE TO ADMIT FACTS: the strategic plan. INTERNAL. 20 August 2026."""
import pikepdf, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=13,
                    leading=16.5, spaceAfter=3)
H2 = ParagraphStyle('H2', parent=ss['Heading2'], fontName='Helvetica-Bold', fontSize=10.5,
                    leading=13.6, spaceBefore=11, spaceAfter=4,
                    backColor=colors.HexColor('#eeeeee'), borderPadding=4)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.5,
                      leading=13, spaceAfter=6)
ITEM = ParagraphStyle('ITEM', parent=BODY, leftIndent=10, spaceBefore=3, spaceAfter=3)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=9, leading=12.4,
                      textColor=colors.HexColor('#8a2010'),
                      backColor=colors.HexColor('#fdf1ef'), borderPadding=6)
QUOTE = ParagraphStyle('QUOTE', parent=BODY, leftIndent=12, rightIndent=8, fontSize=9.1,
                       leading=12.4, textColor=colors.HexColor('#1a3a5c'),
                       backColor=colors.HexColor('#f2f6fa'), borderPadding=5)
def P(t, s=BODY): return Paragraph(t, s)
def tbl(rows, widths, spans=None):
    t = Table(rows, colWidths=widths, repeatRows=1)
    st = [('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#aaaaaa')),
          ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
          ('VALIGN', (0,0), (-1,-1), 'TOP'),
          ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
          ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]
    t.setStyle(TableStyle(st)); return t

s = []
s.append(P("The second notice to admit facts - the strategic plan", H1))
s.append(P("WC/2024/227 Shepherd v Workers' Compensation Regulator &nbsp;|&nbsp; 20 August 2026 "
           "&nbsp;|&nbsp; companion to FORM24_SECOND_NOTICE_DRAFT.pdf", SMALL))
s.append(P("<b>INTERNAL. Never filed, never served, never shown to any other party.</b> The notice "
           "itself is the only document that leaves your hands.", WARN))

s.append(P("1. THE INSTRUMENT, AND WHY IT IS WORTH USING NOW", H2))
s.append(P("Rule 49 of the <i>Industrial Relations (Tribunals) Rules 2011</i>:", BODY))
s.append(P("\"(1) A party to a proceeding (the first party) may, by notice in the approved form "
           "served on <b>another party</b>, ask the other party to admit, for the proceeding only, "
           "the facts or documents stated in the notice. (2) If the other party does not, within "
           "<b>14 days</b> after receiving a notice under subrule (1), serve a notice on the first "
           "party disputing the facts or the authenticity of the documents, the other party <b>is "
           "taken to admit</b>, for the proceeding only, the stated facts... (3) The other party "
           "may, <b>with the leave</b> of the court, commission or registrar, withdraw an admission "
           "taken to have been made under subrule (2).\"", QUOTE))
for t in [
 "<b>The default is admission.</b> Silence for fourteen days converts every unanswered item into a "
 "fact proved for this proceeding. No hearing, no witness, no argument.",
 "<b>Withdrawal requires leave.</b> An admission made by default is not casually undone.",
 "<b>The Commission can compel a response.</b> Rule 41(2)(g) permits a directions order "
 "\"requiring a party to respond to a notice to admit facts or documents\".",
 "<b>Parties only.</b> Rule 49 permits service on \"another party\". The only other party is the "
 "Regulator. It cannot be served on a witness, on the employer, or on any non-party.",
 "<b>Nothing limits you to one.</b> The first notice was served 11 February 2026. Everything in "
 "sections A, B and D of this notice comes from documents obtained since - principally the "
 "Regulator's own witness-conferencing disclosure and the Chief Executive's letter of 5 June 2026.",
]: s.append(P("- " + t, ITEM))

s.append(P("2. THE DRAFTING RULE, LEARNED FROM FEBRUARY 2026", H2))
s.append(P("The first notice produced a clear empirical lesson, and this notice is built on it.", BODY))
s.append(tbl([
    [P("<b>What was asked</b>", SMALL), P("<b>What came back</b>", SMALL)],
    [P("Admit a <b>characterisation</b> - that conduct was misleading, that it demonstrated a lack "
       "of diligence, that a failure occurred", SMALL),
     P("<b>Denied</b> - \"denies as untrue because...\"; or not admitted - \"the appeal is a "
       "hearing de novo and it is for the Commission to determine\"", SMALL)],
    [P("Admit <b>what a document says or records</b> - a date, an author, a quotation, a "
       "system-generated footer", SMALL),
     P("<b>Admitted</b>, sometimes with an added explanation, which is still an admission", SMALL)],
], [78*mm, 88*mm]))
s.append(P("<b>Every one of the 47 items is therefore a fact about a document.</b> There is no "
           "conclusion anywhere in the notice for her to dispute. Either the email says the words "
           "or it does not - and in every case her office disclosed the email.", BODY))
s.append(P("<b>The pressure is real but it is entirely legitimate.</b> It does not come from "
           "complexity or from anything designed to confuse. It comes from the rule: forty-seven "
           "precise items, each answerable only by opening the document, all due within fourteen "
           "days, with default admission as the consequence of doing nothing. That is the burden "
           "rule 49 places on a respondent. Confusion would help her; precision does not.", BODY))

s.append(P("3. THE FOUR ESCAPES, AND HOW EACH IS CLOSED", H2))
s.append(tbl([
    [P("<b>Her February escape</b>", SMALL), P("<b>How this notice forecloses it</b>", SMALL)],
    [P("\"does not admit... because the Respondent does not have a copy of the document\"", SMALL),
     P("Every document is from <b>her own disclosure</b> - the witness-conferencing bundles for "
       "Ms Taylor and Ms Reese, the fatigue-risk-management bundle - or is the Chief Executive's "
       "letter filed in this proceeding, or is already in her amended List of Documents.", SMALL)],
    [P("\"the appeal is a hearing de novo and it is for the Commission to determine\"", SMALL),
     P("Nothing asks her to determine anything. <b>What a document says is not a matter for the "
       "Commission.</b>", SMALL)],
    [P("\"denies as untrue, because [reason]\"", SMALL),
     P("Items are atomic and quoted verbatim. There is no proposition for a \"because\" to attach "
       "to.", SMALL)],
    [P("\"admits... and says that...\" (a qualified admission)", SMALL),
     P("Entirely acceptable. <b>A qualified admission is still an admission.</b> The fact is proved "
       "and she may add whatever context she wishes.", SMALL)],
], [62*mm, 104*mm]))

s.append(PageBreak())
s.append(P("4. WHAT IS IN, SECTION BY SECTION, AND WHAT EACH SECTION DOES", H2))
s.append(tbl([
    [P("<b>Section</b>", SMALL), P("<b>Items</b>", SMALL), P("<b>What it establishes</b>", SMALL)],
    [P("<b>A</b> The employment and the hours sought", SMALL), P("1-13", SMALL),
     P("<b>The trajectory.</b> Through 2023 the appellant repeatedly sought more shifts and more "
       "hours, applied in writing for full-time, volunteered for night shifts, stated unqualified "
       "24-hour availability, submitted draft rosters, and was approved to full-time on 27 "
       "September 2023. Set against sections C and D, the inversion in 2024 requires no argument.", SMALL)],
    [P("<b>B</b> August-September 2023", SMALL), P("14-21", SMALL),
     P("The matters raised and the response: the manager's own \"oversight\" and \"the required "
       "rest period\"; the Director's written direction that he was <b>required to continue to "
       "communicate</b> with the manager; the eight-month roster audit and \"I could not find a "
       "copy\"; the grievance policy offered and <b>not used</b>, because he repaired it instead.", SMALL)],
    [P("<b>C</b> The call-in process", SMALL), P("22-31", SMALL),
     P("The manager's own four statements of the process, each listing <b>switch</b> as an "
       "authorised channel; the three calls of 13-15 May 2024 made through it; and the written "
       "sick-leave process dated <b>4 February 2025</b> - nine months after the events.", SMALL)],
    [P("<b>D</b> Roster concerns and fatigue knowledge", SMALL), P("32-41", SMALL),
     P("<b>The strongest section.</b> On 10 May 2024 - five weeks before onset - the Director wrote "
       "to Human Resources that the concern was rostering \"impacting on staff fatigue, or more "
       "specifically his fatigue\"; that she and the manager had applied the roster risk matrix and "
       "\"at best there would be a rating of 11 which is moderate\"; and that she acknowledged \"a "
       "few rostering errors made by Chloe with regards to Cory's line in past rosters\". She "
       "attached the Fatigue Risk Management guideline, and chased again on 20 May.", SMALL)],
    [P("<b>E</b> The employer's own statements", SMALL), P("42-47", SMALL),
     P("The Chief Executive's letter: no fatigue assessment existed; fatigue risk management was "
       "implemented only after 30 June 2024; no consequential changes to operating procedures; "
       "complaints went to the line manager and were managed by her; and a spreadsheet of MET calls "
       "exists for 17-18 March 2024.", SMALL)],
], [42*mm, 14*mm, 110*mm]))

s.append(P("5. WHAT IS DELIBERATELY LEFT OUT, AND WHY", H2))
s.append(P("<b>(a) The dismissal.</b> It occurred in October 2024 - after the injury of 18 June "
           "2024 and after the decision under appeal. The matters in issue are whether an injury "
           "was sustained, whether it arose out of the employment, whether the employment was a "
           "significant contributing factor, and whether management action taken <b>before</b> the "
           "injury was reasonable. A later dismissal proves none of them. It also carries three "
           "risks: it sits close to the exclusion for injury arising from action taken in "
           "connection with the compensation application; the deed contains confidentiality and "
           "non-disparagement clauses; and the employer is not a party, so the Regulator can simply "
           "decline to admit facts about a deed to which it was not a party.", BODY))
s.append(P("<b>The decisive reason is contamination.</b> If forty-six items are unanswerable and "
           "one is objectionable, her response leads with the objection, and the notice reads as "
           "overreach rather than as forty-six facts she could not deny. The value of this "
           "instrument is that it is unimpeachable. <b>One weak item costs more than it adds.</b> "
           "The dismissal belongs in the medical evidence - the 2025 return to work against medical "
           "advice is already recorded in the insurer's file - and in quantum at settlement.", WARN))
s.append(P("<b>(b) A catalogue of absences.</b> Only the three calls of 13-15 May 2024 appear, and "
           "those dates are already admitted on the pleadings. Building out a pattern of absence "
           "invites the employer's letter of 8 September 2025 and its 34 alleged attendance-process "
           "failures, and offers a competing story: an employee with an attendance problem, cause "
           "unproven. <b>The notice proves the dates. The psychiatrist proves the meaning.</b>", BODY))
s.append(P("<b>(c) 2026 capacity material</b> - the movement forms, the capability checklist, the "
           "request for medical information. Capacity is not a matter in issue in this appeal, and "
           "that material belongs to the parallel employment matter. Keeping it out also keeps the "
           "two tracks sealed from each other.", BODY))

s.append(PageBreak())
s.append(P("6. TIMING", H2))
s.append(tbl([
    [P("<b>When</b>", SMALL), P("<b>What</b>", SMALL)],
    [P("Before service", SMALL), P("Verify every quotation against its source document. Delete the "
        "Source column. Transcribe into the approved Form 24.", SMALL)],
    [P("<b>Service (e.g. Fri 21 Aug)</b>", SMALL), P("Email to Ms Matheson, copied to the OIR "
        "appeals registry. Keep proof of service.", SMALL)],
    [P("<b>14 days later (~4 Sept)</b>", SMALL), P("<b>Every item not disputed is taken to "
        "admit.</b> Five days before the outlines are due.", SMALL)],
    [P("Immediately after", SMALL), P("Write one short letter recording which facts are admitted "
        "and which are disputed. No argument.", SMALL)],
    [P("<b>Wed 9 Sept 4pm</b>", SMALL), P("Witness list filed and served; outlines served. "
        "<b>Admitted facts come out of the outlines</b> - they need no evidence.", SMALL)],
    [P("On or about 9 Sept", SMALL), P("Calderbank offer, if the psychiatric report is in hand.", SMALL)],
], [40*mm, 126*mm]))

s.append(P("7. THE RESPONSE DECISION TREE - WHAT TO DO WITH EACH ANSWER", H2))
s.append(tbl([
    [P("<b>Her answer</b>", SMALL), P("<b>What it means</b>", SMALL), P("<b>What you do</b>", SMALL)],
    [P("<b>Admits</b>", SMALL), P("Proved for this proceeding.", SMALL),
     P("Remove it from your outline and from your oral evidence. Cite it as admitted. Each "
       "admission shortens the hearing and strengthens the offer.", SMALL)],
    [P("<b>Admits with an explanation</b>", SMALL), P("Still an admission of the fact.", SMALL),
     P("Treat as admitted. Note the explanation - it discloses the position she will run.", SMALL)],
    [P("<b>Denies</b>", SMALL), P("She disputes what her own disclosed document says.", SMALL),
     P("Do nothing now. At hearing, put the document to the witness. A denial of a document's "
       "contents is a strong cross-examination opening.", SMALL)],
    [P("<b>\"Does not have a copy\"</b>", SMALL), P("Answerable, because she does.", SMALL),
     P("One short letter identifying where the document sits in her own disclosure or List of "
       "Documents, enclosing a copy, and inviting reconsideration within 7 days.", SMALL)],
    [P("<b>\"A matter for the Commission\"</b>", SMALL),
     P("A non-answer - the item asks what a document says.", SMALL),
     P("Note it. If it recurs across many items, that is the moment to consider an application "
       "under rule 41(2)(g) for an order requiring a response.", SMALL)],
    [P("<b>Silence past 14 days</b>", SMALL), P("<b>All items taken to admit.</b>", SMALL),
     P("Write the short letter recording the deemed admissions. Do not gloat and do not argue - "
       "record it and move on.", SMALL)],
    [P("<b>Asks for more time</b>", SMALL), P("Ordinary and expected.", SMALL),
     P("Consent, in writing, to a specific date. Reasonableness costs nothing and it is returned "
       "when you need your own extension for the expert report.", SMALL)],
], [34*mm, 52*mm, 80*mm]))

s.append(P("8. RISKS, HONESTLY", H2))
for t in [
 "<b>You disclose which documents you are using.</b> Serving this reveals that you hold the emails "
 "of 10 and 20 May 2024 and understand what they establish, so you lose surprise on them. <b>The "
 "trade favours serving:</b> if admitted you never need the cross-examination at all, and if denied "
 "you have a refusal to admit the contents of a document from her own disclosure - which is worth "
 "more than surprise.",
 "<b>It invites preparation.</b> She may take the material to her witnesses. But most of these "
 "documents came from those witnesses in the first place, so the surprise was always limited.",
 "<b>Volume could be read as pressure for its own sake.</b> It is answered by the content: every "
 "item is short, sourced and necessary, and the sections are organised so the notice reads as an "
 "orderly document rather than an assault.",
 "<b>A misquotation would be worse than an omission.</b> It would be denied and would damage "
 "credibility across the whole notice. This is why every quotation must be checked against the "
 "source before service, and why anything you cannot verify comes out.",
]: s.append(P("- " + t, ITEM))

s.append(P("9. PRE-SERVICE CHECKLIST", H2))
for i, t in enumerate([
 "Every quotation checked word for word against the source document.",
 "The Source column deleted.",
 "The schedule transcribed into the approved Form 24 (available from the Commission's website).",
 "Facts and documents only - no conclusion, no characterisation, no adjective anywhere.",
 "Nothing about motive, nothing about how you felt about management action, nothing about the "
 "public interest disclosure as a reason for anything.",
 "Nothing from the parallel employment matter.",
 "Served on the Regulator, copied to the OIR appeals registry. Proof of service kept.",
 "Diarised: fourteen days from service.",
], 1): s.append(P(f"<b>{i}.</b> {t}", ITEM))

doc = SimpleDocTemplate("out/FORM24_STRATEGY_INTERNAL.pdf", pagesize=A4,
                        leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm)
def f_(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7.2)
    c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(18*mm, 9*mm, "INTERNAL - STRATEGIC PLAN - NEVER FILED OR SERVED")
    c.setFont('Helvetica', 7.2); c.setFillColor(colors.HexColor('#777777'))
    c.drawRightString(A4[0]-18*mm, 9*mm, f"Page {d.page}")
    c.restoreState()
doc.build(s, onFirstPage=f_, onLaterPages=f_)
pdf = pikepdf.open("out/FORM24_STRATEGY_INTERNAL.pdf", allow_overwriting_input=True)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save("out/_s.pdf"); pdf.close(); os.replace("out/_s.pdf", "out/FORM24_STRATEGY_INTERNAL.pdf")
print("built out/FORM24_STRATEGY_INTERNAL.pdf")
