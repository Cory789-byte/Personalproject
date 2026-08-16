#!/usr/bin/env python3
"""WC/2024/227 — THE PICTURE: what the report will be, what it answers, where it goes.

The closing synthesis of the 15 August work. Internal, but written so that nothing in it would
embarrass if read — the assessments are marked as assessments.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle)

ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold',
                    fontSize=13.5, leading=17, spaceAfter=3)
PART = ParagraphStyle('PART', parent=ss['Heading2'], fontName='Helvetica-Bold',
                      fontSize=10.8, leading=14, spaceBefore=12, spaceAfter=5)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica',
                      fontSize=9.6, leading=13.3, spaceAfter=6)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.3, leading=11.2,
                       textColor=colors.HexColor('#555555'))
NOTE = ParagraphStyle('NOTE', parent=BODY, fontSize=8.8, leading=12,
                      leftIndent=6, textColor=colors.HexColor('#7a2018'))
def P(t, s=BODY): return Paragraph(t, s)
def T(rows, w):
    t = Table(rows, colWidths=w, repeatRows=1)
    t.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eeeeee')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
    return t

s = []
s.append(P("THE PICTURE — what the report will be, what it answers, where it goes", H1))
s.append(P("WC/2024/227 · 15 August 2026 · the closing position after the day's work", SMALL))

s.append(P("PART 1 — WHAT IT WILL LOOK LIKE", PART))
s.append(P("One report. One attendance. Roughly 8 to 15 pages, in the register of his report of "
           "13 February 2025. Fourteen questions across three matters, built on four attachments — "
           "three of which the other side wrote.", BODY))
s.append(T([
 [P("<b>Section</b>", SMALL), P("<b>Content</b>", SMALL)],
 [P("Opening", SMALL), P("First seen <b>24 October 2024</b>, continuous care since; what he "
   "reviewed; what he was instructed to assume", SMALL)],
 [P("<b>Matter 1</b><br/>1.1–1.5", SMALL), P("Diagnosis, framework, criteria met and when · onset · "
   "differentials excluded · background: the 16 November 2023 entry <i>and the temazepam "
   "prescribed the same day</i>, and the respondent's asserted 2022 anxiety and ADHD history, which "
   "is outside the span of the records he holds · premorbid features from his own assessment · the "
   "complete source list", SMALL)],
 [P("<b>Matter 2</b><br/>2.1–2.3", SMALL), P("The conditions of the work, quoted from the role "
   "description and the Chief Executive's letter — whether and how such conditions can contribute · "
   "fatigue and the rostering of 17–18 March 2024, with the MET calls and the leave of 19 March · "
   "<b>the administrative sequence</b>: the August 2023 rostering error, the February 2024 leave "
   "decline where the attachments were in fact present, and the May 2024 pay correction", SMALL)],
 [P("<b>Matter 3</b><br/>3.1–3.3", SMALL), P("<b>Reasoning before conclusion.</b> Other factors "
   "placed in time from his own file — the partner present and protective on 24 October, the "
   "breakdown running December to February, and bereavement dated at last · then the interval, "
   "answered as a continuing exposure · <b>then</b> causation, expressly built on both: "
   "<b>a significant contributing factor</b>", SMALL)],
 [P("<b>Matter 3</b><br/>3.4–3.7", SMALL), P("Prognosis and current capacity · the adjustments in "
   "functional terms, with exacerbating conditions, complaint handling and working memory · the "
   "requirements of the position in four parts · foreseeable risk", SMALL)],
 [P("Closing", SMALL), P("⭐ Whether the opinion <b>depends on his account</b> · ⭐ whether anything "
   "in the records <b>qualifies</b> it", SMALL)],
], [26*mm, 140*mm]))

s.append(P("PART 2 — WHAT IT ANSWERS: BOTH INSTRUMENTS, ONE DOCUMENT", PART))
s.append(P("<b>The Notice of Non-Party Disclosure</b> states the matters in issue in three numbered "
           "lines. Those are the report's spine — so it answers the Regulator's own framing, in the "
           "notice she served on his practice.", BODY))
s.append(P("<b>The Request for Medical Information</b> asks nine questions. <b>Seven are answered. "
           "Three are declined by design. One is answered on his terms.</b>", BODY))
s.append(T([
 [P("<b>RFMI</b>", SMALL), P("<b>Answered by</b>", SMALL), P("", SMALL)],
 [P("1(a) diagnosis date", SMALL), P("1.1", SMALL), P("✔", SMALL)],
 [P("1(b) clinical basis for the stressors", SMALL), P("2.1–2.3 + 3.3", SMALL), P("✔", SMALL)],
 [P("<b>1(c) self-report, own assessment, or other?</b>", SMALL),
  P("<b>Part B + the closing statement</b>", SMALL), P("⭐", SMALL)],
 [P("1(d) foreseeable risk and controls", SMALL), P("3.7", SMALL), P("✔", SMALL)],
 [P("2 lawful direction · conduct discussions", SMALL), P("—", SMALL), P("declined", SMALL)],
 [P("3 fit under existing reporting arrangements", SMALL), P("—", SMALL), P("declined", SMALL)],
 [P("4 restrictions, basis, duration, review", SMALL), P("3.5", SMALL), P("✔", SMALL)],
 [P("5 complaint handling", SMALL), P("3.5(b)", SMALL), P("✔", SMALL)],
 [P("6 inherent requirements <i>without restrictions</i>", SMALL), P("3.6(a)–(d)", SMALL),
  P("on his terms", SMALL)],
 [P("7 working memory", SMALL), P("3.5(c)", SMALL), P("✔", SMALL)],
 [P("8 exacerbating tasks and environments", SMALL), P("3.5(a)", SMALL), P("✔", SMALL)],
 [P("9 if we cannot accommodate", SMALL), P("—", SMALL), P("declined", SMALL)],
], [72*mm, 66*mm, 28*mm]))
s.append(P("⭐⭐⭐ <b>1(c) is the one that pays.</b> They offered three options — self-report, his own "
           "assessment, or other medical information. <b>The answer is a fourth: documents authored by "
           "the employer and facts admitted by the Regulator.</b> They wrote the question that "
           "produces it.", NOTE))
s.append(P("⚠ <b>The three declined are the three that could hurt</b> — all workplace questions "
           "dressed as medical ones. Part D declines them expressly and offers to say so if asked.", NOTE))

s.append(PageBreak())

s.append(P("PART 3 — HOW IT IS POSITIONED", PART))
s.append(P("<b>What it is:</b> a treating psychiatrist's report, obtained by the patient, answering "
           "the matters in issue in his proceeding, and provided to his employer in answer to its "
           "request for medical information. <b>One report, two recipients, two purposes, both "
           "declared.</b>", BODY))
s.append(P("<b>Funded by Metro South Health</b>, which required the information. ⭐ That makes the "
           "causation opinion harder to attack, not easier — it cannot be said to have been bought by "
           "him. ⚠ It is <b>instructed by him and addressed to him</b>; the covering email states both "
           "on its face.", BODY))
s.append(T([
 [P("<b>To</b>", SMALL), P("<b>The covering note does</b>", SMALL)],
 [P("<b>The Regulator</b>", SMALL), P("⭐ <b>One line.</b> Continuing disclosure, and that the same "
   "report has gone to the employer. ⛔ No argument, no commentary, no request — a report argues for "
   "itself, and anything added subtracts from it", SMALL)],
 [P("<b>The employer</b>", SMALL), P("It answers the request of 31 July · <b>the scope line</b>, "
   "identifying which questions are workplace rather than medical · <b>their own policy</b> — "
   "unjustifiable hardship tested against the <b>whole organisation</b>, onus on Queensland Health · "
   "the ask: implement the adjustments, restore pay · the 3 August questions, folded in · and that "
   "the Regulator holds the same report", SMALL)],
], [30*mm, 136*mm]))
s.append(P("<b>Sent simultaneously.</b> No sequencing inference available to anyone. ⭐⭐ And each is "
           "told the other holds the identical document — one sentence that forecloses any suggestion "
           "of two versions or selective provision.", BODY))

s.append(P("PART 4 — WHAT IT CHANGES", PART))
s.append(T([
 [P("", SMALL), P("<b>No report</b>", SMALL), P("<b>⭐ With it</b>", SMALL)],
 [P("Appeal resolves favourably", SMALL), P("30%", SMALL), P("<b>62%</b>", SMALL)],
 [P("Pay restored / return ~3 months", SMALL), P("30%", SMALL), P("<b>51%</b>", SMALL)],
 [P("<b>Neither outcome</b>", SMALL), P("<b>49%</b>", SMALL), P("<b>20%</b>", SMALL)],
], [80*mm, 43*mm, 43*mm]))
s.append(P("⚠ <b>Structured judgement, not measurement.</b> Read the movement, not the decimals.", SMALL))
s.append(P("<b>On the appeal:</b> it moves from <i>unproved on causation</i> to <i>proved on the "
           "medical, contested on the characterisation</i> — the only contest the Regulator has left, "
           "and the one where the Chief Executive's letter hurts her. <b>On the employment track:</b> "
           "it removes <i>“we cannot accommodate”</i> and puts the adjustments into a framework whose "
           "onus is theirs.", BODY))

s.append(P("PART 5 — ⚠ WHAT IT STILL DOES NOT DO", PART))
s.append(P("1. <b>It does not decide the appeal.</b> s 32(5)(a) remains argument on an agreed factual "
           "base, and Taylor and Reese have not given oral evidence.<br/>"
           "2. <b>It does not reach the 2026 wages.</b> Only the employment track does — and the "
           "deemed refusal of <b>24 August</b> is the live route there.<br/>"
           "3. <b>It may not say what is hoped.</b> He declined once already. The instruction asks him "
           "to say where the material is insufficient rather than qualify — so a <i>“cannot say”</i> "
           "returns as a clean answer, not a damaged one.<br/>"
           "4. ⚠ <b>Question 3.6 is still short of its best evidence</b> — the three movement forms and "
           "the April 2025 call statistics are not in the pack.", BODY))

doc = SimpleDocTemplate("out/THE_PICTURE_report_answers_positioning.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=17*mm, bottomMargin=17*mm,
                        title="WC/2024/227 — the picture", author="Cory Lea Shepherd")
def f(canv, d):
    canv.saveState(); canv.setFont('Helvetica', 7.4)
    canv.setFillColor(colors.HexColor('#777777'))
    canv.drawString(20*mm, 10*mm, "WC/2024/227 · the report: shape, answers, positioning · 15 Aug 2026")
    canv.drawRightString(A4[0]-20*mm, 10*mm, f"Page {d.page}")
    canv.restoreState()
doc.build(s, onFirstPage=f, onLaterPages=f)
print("built out/THE_PICTURE_report_answers_positioning.pdf")
