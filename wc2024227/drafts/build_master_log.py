#!/usr/bin/env python3
"""MASTER LOG — WC/2024/227 + employment track. INTERNAL WORKING DOCUMENT.
Not for service, not for disclosure. Contains PID-referable and restricted entries.
"""
import pikepdf
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)

OUT = "/home/user/Personalproject/wc2024227/drafts/out/MASTER_LOG_PID_to_5Aug2026.pdf"
TMP = "/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/_log_raw.pdf"
PW, PH = landscape(A4)
F, B = "Helvetica", "Helvetica-Bold"

body = ParagraphStyle("b", fontName=F, fontSize=7.2, leading=9.0)
bb   = ParagraphStyle("bb", fontName=B, fontSize=7.2, leading=9.0)
hd   = ParagraphStyle("hd", fontName=B, fontSize=7.2, leading=9.0, textColor=colors.white)
h1   = ParagraphStyle("h1", fontName=B, fontSize=13.5, leading=16)
h2   = ParagraphStyle("h2", fontName=B, fontSize=9.5, leading=12.5,
                      spaceBefore=8, spaceAfter=3, textColor=colors.HexColor("#1f2a44"))
mt   = ParagraphStyle("mt", fontName=F, fontSize=8, leading=11)
nt   = ParagraphStyle("nt", fontName=F, fontSize=7.2, leading=9.4,
                      textColor=colors.HexColor("#444444"))
warn = ParagraphStyle("warn", fontName=B, fontSize=8, leading=11,
                      textColor=colors.HexColor("#8a1b1b"))


class Numbered(pdfcanvas.Canvas):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self._p = []
    def showPage(self):
        self._p.append(dict(self.__dict__)); self._startPage()
    def save(self):
        n = len(self._p)
        for st in self._p:
            self.__dict__.update(st); self._f(n); super().showPage()
        super().save()
    def _f(self, n):
        self.setFont(F, 6.6); self.setFillColor(colors.HexColor("#555555"))
        self.drawString(13*mm, 9*mm, "C Shepherd · WC/2024/227 · MASTER LOG · "
                        "INTERNAL WORKING DOCUMENT — NOT FOR SERVICE OR DISCLOSURE")
        self.drawRightString(PW-13*mm, 9*mm, "Page %d of %d" % (self._pageNumber, n))
        self.setStrokeColor(colors.HexColor("#bbbbbb")); self.setLineWidth(0.4)
        self.line(13*mm, 12*mm, PW-13*mm, 12*mm)


def P(t, s=body): return Paragraph(t, s)

COLS = [30*mm, 118*mm, 116*mm]
TS = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#2f3b52")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#9aa3b0")),
    ("LEFTPADDING", (0,0), (-1,-1), 3), ("RIGHTPADDING", (0,0), (-1,-1), 3),
    ("TOPPADDING", (0,0), (-1,-1), 2.2), ("BOTTOMPADDING", (0,0), (-1,-1), 2.2),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f2f4f7")]),
])

def tbl(rows):
    d = [[P("Date / time", hd), P("Event", hd), P("Source · significance", hd)]]
    for r in rows:
        d.append([P(r[0], bb), P(r[1]), P(r[2])])
    t = Table(d, colWidths=COLS, repeatRows=1); t.setStyle(TS); return t


PH1 = [
 ("6 Jun 2023", "Communication book entry by the Appellant re verifying and updating doctors' "
  "on-call contact details; the page is removed by the Line Manager",
  "Removal <b>admitted</b> — Form 24 ¶6. Contents not admitted (¶7). Item 18"),
 ("16 Jun 2023", "Appellant raises “No consultation of the team members or the department "
  "when making major changes”", "Form 20 ¶28"),
 ("18 Jul 2023", "Stibbard: “removing everyone's access to the database”; directory "
  "updates restricted to the Telecommunications Coordinator role",
  "Form 20 ¶22 — the operational change that drove complaint volume"),
 ("7 Aug 2023", "Grievance re the Line Manager's conduct, raising WHS concerns about unsafe "
  "rostering and fatigue. Not upheld; directed to continue reporting to her",
  "Reese acknowledges a rostering error — <b>admitted</b>, Form 24 ¶5"),
 ("11 Aug 2023", "Text to the Line Manager notifying intention to become Switchboard delegate",
  "Sending admitted; characterised “not a formal notification” — Form 24 ¶18"),
 ("31 Aug 2023", "Full-time application, recording the delegate intention",
  "Exhibit CS-3. Approved 27 Sep; commenced 16 Oct 2023"),
 ("15 Nov 2023", "Business case minutes", "Item 18 of the Notice"),
]

PH2 = [
 ("20 Feb 2024 11:24", "COVID pandemic leave form 15480560 drafted; submitted 11:41:27",
  "Exact timestamps from the myHR audit trail produced at Item 11"),
 ("21 Feb 2024 12:23", "<b>Declined</b> (Donovan-Taylor)", "Item 11 audit trail"),
 ("28 Feb 2024 06:07", "Resubmitted", "Item 11"),
 ("29 Feb 2024 09:06", "<b>Declined</b> a second time", "Item 11"),
 ("29 Feb 2024 11:07", "Resubmitted; <b>approved 11:21:03</b> on the same supporting evidence",
  "Item 11. Manager + Delegate approved by Reese 1 Mar 16:05:08"),
 ("17–18 Mar 2024", "<b>Consecutive shifts ending 23:00 and recommencing 06:00 — a "
  "7-hour break</b>, against the 10-hour minimum (8 only by written agreement)",
  "Both <b>admitted</b> — Form 24 ¶1 and ¶3. Stressor 3"),
 ("19 Mar 2024", "Fatigue leave refused in reliance on the 8-hour agreement signed 17 Jun 2020; "
  "personal leave exhausted instead", "Form 20 ¶40. Item 15 leave ledger"),
 ("3 May 2024", "Payroll (E Grant) instructs the Line Manager to “submit an AVAC to correct "
  "these shifts”", "<b>Admitted</b> — Form 24 ¶40"),
 ("9 May 2024", "Line Manager's MASPER email — a doctor's hours “not provided on the "
  "rosters” and the contact number “switched off”",
  "Exhibit CS-1. Form 20 ¶27 — a roster problem answered by changing call handling"),
]

PH3 = [
 ("13 May 2024", "⭐ <b>PID complaint lodged with the Ethical Standards Unit</b>",
  "ESU complaint form. Determined a PID 24 Dec 2024 — <b>admitted</b>, Form 24 ¶20"),
 ("15 May 2024 13:15", "“Office Hours and Departmental Directives” email — to the "
  "Line Manager + Logan Switch, cc 17 staff <b>+ LBH_HR</b>",
  "11 Jun 2026 disclosure, p 6"),
 ("15 May 2024 15:35", "PID email — to MetroSouthESU; CO_Complaints; <b>LBH_HR</b>",
  "11 Jun 2026 disclosure, p 8"),
 ("15 May 2024 15:41", "⭐ <b>M Harrison (Support Officer, HR) forwards from LBH_HR → "
  "B Punch, E McGinley, A McNamee</b> — “email from Corey Shephard to ESU and CO "
  "Complaints regarding Chloe Taylor”",
  "11 Jun 2026 disclosure, <b>p 7</b>. Routed within HR — not to the Line Manager, not to "
  "the Director. Harrison is the officer who refuses pay in 2026"),
 ("15 May 2024 18:23", "<b>The Director directs the Appellant to retract</b> an email inquiring "
  "about office hours; the email carries Recall-This-Message instructions",
  "<b>Admitted</b> — Form 24 ¶21. A comparable email by the Line Manager on 9 May "
  "attracted no such direction (denied, ¶22)"),
 ("16 May 2024 11:43", "⭐ <b>E McGinley (A/Senior Consultant, HR) → T Reese and "
  "T Smith; cc Punch, Pritchard, McNamee</b>, attaching “Chloe Taylor "
  "scc-complaint-form.docx”: “Cory sent his complaint directly to the Ethical "
  "Standards Unit who are currently awaiting further documentation… Once ESU have "
  "… finalised their assessment we will reach out to discuss next steps”",
  "11 Jun 2026 disclosure, p 7. <b>This is the operational HR response MSH later tells the "
  "Commission does not exist</b> (Item 20)"),
 ("18–20 May 2024", "Request to Together Queensland (H Hayes); union confirms it passed the "
  "correspondence to the Health team", "Exhibit CS-2"),
 ("21 May 2024", "The Director asks the Appellant to identify the directives about which he had "
  "consultation concerns", "Form 20 ¶28"),
 ("28 May 2024", "AVAC submitted — <b>a 25-day delay</b> from the payroll instruction",
  "<b>Admitted</b> — Form 24 ¶41"),
]

PH4 = [
 ("18 Jun 2024", "⭐ <b>ONSET OF INJURY</b> — Major Depressive Disorder with anxious "
  "distress", "Amended Form 9A. WCRA s 32(1): employment must be <b>a significant</b> "
  "contributing factor"),
 ("after 30 Jun 2024", "⭐ <b>Fatigue risk management implemented at Logan Switchboard</b>, "
  "“in connection with an organisational change related to the reporting lines”",
  "MSH's own words, Item 5, 5 Jun 2026 letter. <b>Twelve days after the injury</b>"),
 ("12 &amp; 16 Jul 2024", "Required to attend meetings convened by management while on certified "
  "leave", "Form 20 ¶42"),
 ("30 Aug 2024", "CCC complaint", "Referred back to MSH 22 Nov 2024"),
 ("8 Sep 2024", "Work Capacity Certificate signed (Dr Hawes)", "First certificate for the injury"),
 ("8 Oct 2024", "<b>Employment terminated</b> on the basis of “abandonment of "
  "employment”", "Form 20 ¶43. Reinstatement application TD/2024/110, stamped 25 Oct"),
 ("24 Oct 2024", "⭐ <b>Review Decision 69983</b> — the Regulator's own Reviewing "
  "Officer finds the 7-hour break “amounted to unreasonable management action” and is "
  "satisfied employment was <b>a significant contributing factor</b>",
  "Contents <b>admitted</b> — Form 24 ¶37, relevance reserved on the de novo"),
 ("22 Nov 2024", "CCC refers the complaint back to MSH", "PID track"),
 ("24 Dec 2024", "⭐ <b>J Loader, Director ESU, determines PID 24-ESU-1130</b>",
  "<b>Admitted</b> — Form 24 ¶20. s 65 PID Act protection; order 6 of the draft order"),
]

PH5 = [
 ("(2025)", "Reinstated following TD/2024/110", "Related matter"),
 ("7 Apr 2025 → 14 Jun 2026", "⭐ <b>Fourteen months of reduced-hours work</b>, "
  "evidenced by payslips",
  "Contradicts “unable to accommodate a graduated return to work”"),
 ("8 Apr 2025", "Reinstatement process correspondence with J Roberts", "Pack 05"),
 ("(Mar 2025)", "⚠ RESTRICTED CATEGORY — leave request chain and response involving "
  "the Director, Corporate Services", "Scope decision required before any use. Not for service"),
 ("28 Mar 2025", "Hughes correspondence citing Directive 03/20, HR Policy C73, HR Policy E4",
  "None of those policies held; health.qld.gov.au returns 403"),
 ("27 Aug 2025", "Scheduled meeting cancelled — Hughes unwell", "Pack 03"),
 ("8 Sep 2025", "⭐ <b>Hughes attendance letter — 34 occasions</b>",
  "The last time attendance was formally raised. Not raised again since"),
 ("3 Oct 2025", "Formal written request for review to the A/Director, HR Business Partnering, "
  "concerning a process initiated by the officer who later signs the 31 Jul 2026 RFMI; union "
  "copied", "Recorded at Part 2(d) of the 3 Aug 2026 letter to the Chief Executive"),
 ("4 Oct 2025", "Complaint about Hughes to J Roberts, cc Moran", "Pack 03 / 05"),
]

PH6 = [
 ("17 Feb 2026", "Counsel unavailability; mention moved 26 → 27 Feb", "Willson"),
 ("18 Feb 2026", "Form 24 response and email communication", "The admissions relied on throughout"),
 ("27 Feb 2026", "Mention — <b>Willson appears</b>", "Appearance pattern"),
 ("13 Mar 2026", "s 552A conference — <b>Willson appears</b>", ""),
 ("7 Apr 2026", "Mention — <b>Willson appears</b>; the 5-week response window is set", ""),
 ("8 Apr 2026", "<b>Amended Form 9A filed</b> (the Neville pleading, Stressor 3(b))",
  "Respondent's amended SOFC due 13 May — exactly 35 days"),
 ("22 Apr 2026", "⭐ <b>FORM 29 — Notice of Non-Party Disclosure sealed</b>; served on "
  "Matheson (Affected Party 1) and Thorburn (MSH)",
  "20 Items. <b>From this date MSH knows precisely which categories are sought</b>"),
 ("30 Apr 2026 15:59", "⭐ <b>L Griffin, Director Employment Relations MSH HR, forwards MSH "
  "correspondence to the QIRC Registry</b>, copying the Appellant “by way of service”, "
  "cc Ruttan, Matheson, Tribunal Matters",
  "HR's ER Director personally effecting service in the appeal"),
 ("5 May 2026", "Medical information requested from the Appellant",
  "Referred back to in the 26 Jun email"),
 ("13 May 2026", "Regulator files its amended SOFC", ""),
 ("22 May 2026 13:45", "Mention. Commissioner <b>notes the non-attendance of the Health "
  "Service</b>; MSH directed to provide objections by 4:00pm Friday 5 June. <b>Willson does NOT "
  "appear</b> — first listing after the amended SOFC",
  "Registry email to Cory, Matheson, OIR-Appeals, Ruttan, <b>Tribunalmatters (QH central)</b>, "
  "Thorburn, <b>Griffin</b>"),
 ("5 Jun 2026", "⭐⭐ <b>MSH OBJECTION K-LM26/729 — signed Noelle Cridland, Chief "
  "Executive</b>; enquiries Myla Ruttan, Principal Lawyer. Complied 6, 11, 12, 13, 15, 16. "
  "Non-existence 1–2, 3(c), 4, 5, 7, 14, 20. Objections 3(a), 3(b), 8, 9, 10, 17, 18, 19",
  "Key admissions: complaints “managed <b>solely via email or verbally</b>”; Switchboard "
  "<b>non-clinical</b> so no FRMS; fatigue management <b>after 30 Jun 2024</b>; “no "
  "consequential changes”; SPOK <b>not retained</b>; personal mobile outside the retention "
  "policy; 20,006 headcount. States <b>three times</b> that compliance requires <b>CE "
  "approval</b>"),
 ("11 Jun 2026", "⭐ <b>The Regulator discloses 10pp</b> — the 15–16 May 2024 "
  "correspondence, the leave-form walkthrough and the ESU PID form",
  "Exhibit CS-4. <b>Falsifies the Item 20 answer</b>; p 7 carries Harrison and McGinley"),
 ("18 Jun 2026", "<b>Form 4 and Form 20 affirmed.</b> ¶47 answers the two-shift premise; "
  "¶49 quotes the objection back; ¶50 seeks SPOK verification on oath; ¶52 uses "
  "the Regulator's disclosure against Item 20", "Draft order 3 — verification affidavit by "
  "the <b>CE or a delegated Director</b>"),
 ("23 Jun 2026", "<b>64G filed and sealed</b>", ""),
 ("25 Jun 2026 08:31", "⭐ <b>SERVED ON M RUTTAN</b> — Postmaster delivery receipt", ""),
]

PH7 = [
 ("26 Jun 2026 10:42", "⭐⭐ <b>THE ORIGIN DOCUMENT.</b> C Taylor, “Cory Shepherd "
  "— ECC”: opens with a welfare check and the EAP brochure; notes the 5 May request "
  "outstanding; then — “<b>Until we receive appropriate medical clearance, including a "
  "completed Employee Capacity Certificate (ECC), we are unable to facilitate your return to "
  "work</b>… As your employer, we have a legal obligation under <b>section 19 of the "
  "Queensland Work Health and Safety Act 2011</b>”",
  "⚠ <b>s 19 is a duty owed TO the worker, operating “while the workers are at "
  "work”.</b> Cited <b>before anything was challenged</b> — MSH's own first, "
  "unpressured characterisation of its authority. <b>One day after service on Ruttan</b> "
  "— recorded, never asserted as a cause"),
 ("29 Jun 2026", "Appellant texts the Line Manager regarding a doctor's appointment", "Referred "
  "to in the 2 Jul email (misdated there as “Monday 29th July”)"),
 ("1 Jul 2026", "Doctor's appointment", ""),
 ("2 Jul 2026 14:38", "Taylor recycles 26 Jun near-verbatim; adds the <b>2:00pm Friday 3 July "
  "deadline</b>; “I will process <b>your shifts that you have not worked</b> as Sick "
  "Leave”", "⭐ <b>The legal basis is DROPPED — no instrument cited</b>"),
 ("3 Jul 2026", "⭐ <b>ECC completed by Dr Ma — FIT WITH RESTRICTIONS</b>; "
  "“continuation of existing arrangement… worked and tolerated… without "
  "deterioration”. To Injury Management 2:30pm; resubmitted 3:06pm",
  "<b>MSH's own stated condition is satisfied. The bar does not lift.</b> Invoice 574370"),
 ("3 Jul 2026 15:18", "Appellant replies to Taylor on the ECC and leave type", ""),
 ("7 Jul 2026 10:54", "L Forrest: the ECC “has now been reviewed and carefully "
  "considered”, but “the Health Service <b>does not have sufficient information</b> "
  "to understand the nature of these matters or assess whether they present any psychosocial "
  "hazards”. Seven calendar days, consequence attached",
  "⭐ Invokes “obligations under work health and safety legislation” — "
  "<b>no Act, no section</b>. A new condition replaces the satisfied one"),
 ("13 Jul 2026", "⭐ <b>WAGES CEASE</b>", "Accrued leave debited without agreement — "
  "IR Act s 33 requires agreement or 8 weeks' notice"),
 ("15 Jul 2026", "M Harrison: <b>pay refused</b>; interim duties declined <b>in any capacity</b>; "
  "“unable to commit to a timeframe”",
  "⭐ <b>NO INSTRUMENT CITED.</b> Against G03 cl 1.1 and QH-IMP-401-5 (suitable duties "
  "“actively sought” and “made available wherever reasonably practicable”)"),
 ("~15 Jul 2026", "⭐ MSH to the insurer: “<b>currently unable to accommodate a "
  "graduated return to work</b>”",
  "Surfaced via the ART letter of 4 Aug. Contradicted by 14 months of payslips and MSH's own ECC"),
 ("15 Jul 2026", "Together — urgent industrial referral (Heath / Moran)",
  "“Still reviewing / industrial team” 17 Jul"),
 ("16 Jul 2026 15:54", "Matheson rejects Calderbank #2", "Served 1 Jul 12:16"),
 ("24 Jul 2026", "Appellant requests the Respondent's disclosure list", "Still outstanding"),
 ("28 Jul 2026 17:39", "Appellant: incorrect application of EB12, the Award and HR policies", ""),
 ("29 Jul 2026 16:10", "Harrison, EAF reply", "⭐ <b>The WHS Act returns — first "
  "citation since 26 June</b>"),
 ("30 Jul 2026 14:33", "Harrison holding reply; “unable to guarantee my return”",
  "<b>No instrument.</b> All EB12/Award/policy text in that PDF is the Appellant's own 28 July "
  "letter quoted beneath"),
 ("31 Jul 2026 11:43", "⭐ <b>S Hughes, Director Corporate Services — Request for "
  "Medical Information</b>, nine questions to the GP, written in the first person of the "
  "decision-maker. Q3 asks whether fit to return “under the existing reporting "
  "arrangements, including working with and reporting to [the] current line manager”",
  "Cites HR Policy G3 and WHS ss 17, 19. cc <b>notes@solv.com.au</b> — a third-party system"),
 ("31 Jul 2026 15:15", "Harrison — reimbursement practice-confirmation gate", ""),
]

PH8 = [
 ("3 Aug 2026 07:17", "Matheson replies on the disclosure list and the NNPD commitment", ""),
 ("3 Aug 2026 11:38", "⭐ <b>FOUR EMAILS SENT.</b> RFMI response + allocation · "
  "cl 10.3.2 request (<b>21-day clock → 24 Aug</b>) · cl 1.11 Stage 1 dispute · "
  "<b>s 89 letter to the Chief Executive</b>",
  "Part 2A closes the 7 July information gap in four numbered items and records that ss 47–49 "
  "consultation “has not occurred at any point since 26 June 2026”"),
 ("3 Aug 2026 12:45", "⭐ MSH Executive Services: “I have been asked by <b>Noelle "
  "Cridland, Health Service Chief Executive</b>, to acknowledge receipt”",
  "<b>67 minutes.</b> Personal knowledge documented and dated — s 27(5)(d) WHS Act"),
 ("4 Aug 2026 13:35", "⭐ Taylor, Stage 1 acknowledgement — <b>admits cl 1.11.2(a) "
  "24 hours “not achieved”</b>", "An admission against interest, volunteered"),
 ("4 Aug 2026 16:40", "ART / J Zappia — overpayment review and employer disclosures",
  "Surfaces the “unable to accommodate” statement"),
 ("5 Aug 2026 07:30", "⭐ <b>Stage 1 response sent (v16)</b> — seven questions; written "
  "answers sought by 10 August", ""),
 ("5 Aug 2026 11:45", "The clinic telephones Harrison regarding the invoice",
  "Third-party proof of cooperation"),
 ("5 Aug 2026 16:12", "QSuper reclassifies 25–31 May as a <b>graduated return to work "
  "payment</b>", "The scheme funds the arrangement MSH told the insurer it could not accommodate"),
 ("5 Aug 2026 20:53", "Occupational psychology provider — indicative proposal, $10–30k",
  "Independent assessment, to be commissioned and funded by the Health Service"),
]

PH9 = [
 ("6 Aug 2026", "Union industrial officer returns; submission and delegate email to go", "Drafted"),
 ("7 Aug 2026", "⭐⭐ <b>64G MENTION BEFORE COMMISSIONER DWYER</b>",
  "Watch: whether the first word is “consent”; who appears for MSH; whether Willson "
  "reappears. Press verification on oath — if resisted, ask that it be <b>reserved, not "
  "refused</b>"),
 ("10 Aug 2026", "<b>Stage 2 referral</b> (does not self-execute) · <b>RTI + IP Act "
  "applications</b> · written answers to the seven questions fall due",
  "The IP Act application is the only route to the 2026 employment file — the Form 29 date "
  "ranges stop at 30 Jun 2024"),
 ("17 Aug 2026", "Stage 2 concludes (if referred 10 Aug)", "cl 1.11.2(b) — the employer "
  "<b>shall</b> arrange a conference"),
 ("24 Aug 2026", "⭐ <b>cl 10.3.6 DEEMED REFUSAL</b>", "Self-executing. Running now"),
]

OUTSTANDING = [
 ("⚠ OPEN", "<b>The last shift actually worked before 26 June 2026 is unverified.</b> "
  "Settle from the payslips and roster", "CLAUDE.md immediate task 6. Decides how the whole "
  "chronology reads"),
 ("⛔ NOT SENT", "<b>Preservation request.</b> Form 29 categories, employment records since "
  "26 Jun, custodian mailboxes, the Appellant's own QH mailbox, and Solv",
  "Send before 7 Aug. Costs nothing, cannot be objected to"),
 ("⛔ UNKNOWN", "Whether <b>Cory.Shepherd@health.qld.gov.au</b> remains accessible",
  "Taylor cc'd the personal address on both 26 Jun and 2 Jul"),
]


def build():
    doc = BaseDocTemplate(TMP, pagesize=landscape(A4), leftMargin=13*mm, rightMargin=13*mm,
                          topMargin=12*mm, bottomMargin=16*mm,
                          title="Master Log — WC/2024/227",
                          author="Cory L Shepherd", subject="", creator="", producer="")
    doc.addPageTemplates([PageTemplate(id="p", frames=[
        Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")])])
    s = []
    s.append(P("MASTER LOG — THE PID, THE ACTORS, THE FORM 29, THE 64G, "
               "THE LOCKOUT AND WHAT FOLLOWED", h1))
    s.append(P("WC/2024/227 · Shepherd v Workers' Compensation Regulator · "
               "compiled 5 August 2026", mt))
    s.append(Spacer(1, 3))
    s.append(P("⚠ INTERNAL WORKING DOCUMENT. NOT FOR SERVICE AND NOT FOR DISCLOSURE. "
               "Contains entries referable to a public interest disclosure (s 65 PID Act) and "
               "one restricted category. Nothing in this log is an allegation of coordination "
               "or improper purpose; entries are recorded in date order only.", warn))
    s.append(Spacer(1, 5))

    for title, rows in [
        ("PHASE 1 — THE STANDING CONDITION (2023)", PH1),
        ("PHASE 2 — THE PLEADED PERIOD (Feb–May 2024)", PH2),
        ("PHASE 3 — ⭐ THE PID AND THE SHARED HR MAILBOX (13–28 May 2024)", PH3),
        ("PHASE 4 — INJURY, TERMINATION, REVIEW, DETERMINATION (Jun–Dec 2024)", PH4),
        ("PHASE 5 — REINSTATEMENT AND THE GRADUATED ARRANGEMENT (2025 – Jun 2026)", PH5),
        ("PHASE 6 — THE FORM 29, THE OBJECTION AND THE 64G (Feb–Jun 2026)", PH6),
        ("PHASE 7 — ⭐ THE LOCKOUT AND WHAT FOLLOWED (26 Jun – 31 Jul 2026)", PH7),
        ("PHASE 8 — THE PACKAGE AND THE RESPONSE (3–5 Aug 2026)", PH8),
        ("PHASE 9 — THE FORWARD CALENDAR", PH9),
        ("OUTSTANDING", OUTSTANDING),
    ]:
        s.append(P(title, h2)); s.append(tbl(rows))

    s.append(Spacer(1, 7))
    s.append(P("Compiled from source documents. Admissions are cited to the Form 24; MSH's "
               "statements to the objection of 5 June 2026 (ref K-LM26/729); the 15–16 May "
               "2024 entries to the Respondent's disclosure of 11 June 2026.", nt))
    doc.build(s, canvasmaker=Numbered)

    with pikepdf.open(TMP, allow_overwriting_input=True) as pdf:
        for k in list(pdf.docinfo.keys()):
            del pdf.docinfo[k]
        pdf.docinfo["/Author"] = "Cory L Shepherd"
        pdf.docinfo["/Title"] = "Master Log — WC/2024/227"
        if pdf.Root.get("/Metadata") is not None:
            del pdf.Root["/Metadata"]
        pdf.save(OUT, encryption=pikepdf.Encryption(
            owner="", user="", allow=pikepdf.Permissions(
                modify_other=False, modify_annotation=False, modify_assembly=False,
                modify_form=False, extract=True, print_lowres=True, print_highres=True)))
    print("built:", OUT)


build()
