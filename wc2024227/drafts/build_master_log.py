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

def tbl(rows, h=("Date / time", "Event", "Source · significance")):
    d = [[P(h[0], hd), P(h[1], hd), P(h[2], hd)]]
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
 ("(late 2024 / early 2025)", "⛔ <b>DATE TO SUPPLY —</b> reinstatement following "
  "TD/2024/110; returned <b>directly under the same Director and Line Manager</b>",
  "Application stamped 25 Oct 2024. <b>The actual return date is not in the repo</b>"),
 ("⛔ TO SUPPLY", "<b>Relocation / isolation to another office</b>",
  "Raised by Cory 5 Aug 2026. <b>Not evidenced in any document held.</b> The 8 Apr 2025 "
  "Roberts email is NOT it (it records Cory in the security office offering to meet). "
  "Needs date + source before any use"),
 ("8 Apr 2025 14:19–14:21", "Reinstatement-process exchange with <b>J Roberts</b>, "
  "A/Director HR Business Partnering — Cory offers a face-to-face meeting; Roberts is "
  "in the Administration offices and will find a room", "Pack 05"),
 ("7 Apr 2025 → 14 Jun 2026", "⭐ <b>Fourteen months of reduced-hours work</b>, evidenced "
  "by payslips", "Contradicts “unable to accommodate a graduated return to work”"),
 ("⛔ TO SUPPLY", "<b>An additional full-time employee engaged in Switchboard</b>, and "
  "<b>subsequently removed</b>", "Raised by Cory 5 Aug 2026. <b>Not documented in the "
  "repo.</b> Needs dates, the position, and the source. Goes to whether the service "
  "could accommodate hours — and to the “unable to accommodate” statement"),
 ("⚠ 12 Mar 2025", "⚠ <b>RESTRICTED.</b> Confidential disclosure to the Director, "
  "Corporate Services of a personal crisis, with court documentation; <b>request for "
  "Domestic and Family Violence leave under PSC Directive 03/20</b>",
  "Source: Cory's complaint of 4 Oct 2025 (Attachments A and B). <b>Internal only. "
  "Do not reproduce the detail.</b>"),
 ("⚠ 28 Mar 2025", "⚠ <b>RESTRICTED.</b> Management responds that the leave may not be "
  "available, on the basis of how he is characterised in a court matter",
  "4 Oct 2025 complaint (Attachment C): described as “factually incorrect”, "
  "contravening the Directive, and contrary to advice he had received. <b>⛔ The "
  "characterisation itself is NEVER to be voiced forward — discipline rule 10</b>"),
 ("28 Mar 2025", "Hughes correspondence citing <b>Directive 03/20</b>, HR Policy C73, "
  "HR Policy E4", "None of those policies held; health.qld.gov.au returns 403"),
 ("(from ~Mar–Apr 2025)", "⭐ <b>“Punitive performance monitoring” begins</b> — "
  "attendance logged instance by instance",
  "Cory's own contemporaneous words, 4 Oct 2025 complaint ¶2. <b>The logging FOLLOWS "
  "the confidential disclosure</b>"),
 ("27 Aug 2025", "⭐ Cory <b>proactively offers Hughes' office documentation</b> before a "
  "scheduled meeting. <b>The meeting is cancelled immediately afterwards</b>",
  "Attachment E. Later relied on against him — see 10 Sep"),
 ("8 / 10 Sep 2025", "⭐⭐ <b>Hughes attendance letter — 34 occasions</b>, initiating a "
  "performance improvement process, and asserting that Cory's actions caused meetings "
  "not to proceed",
  "Repo file dated <b>8 Sep</b>; the complaint dates the letter <b>10 Sep</b> — "
  "⚠ reconcile. <b>The last time attendance was formally raised. Not raised since.</b> "
  "Attachment F"),
 ("29 Sep 2025 ~15:00", "Immediately after his shift, the Line Manager emails <b>both his "
  "personal and work addresses</b> “to follow up to see if I understand the on-call "
  "process”", "4 Oct 2025 complaint ¶3 — “intrusive and inappropriate”. The same "
  "on-call formulation reappears in 2026"),
 ("3 Oct 2025", "Formal written request for review to the A/Director, HR Business "
  "Partnering, concerning a process initiated by the officer who later signs the 31 Jul "
  "2026 RFMI; union copied",
  "Recorded at Part 2(d) of the 3 Aug 2026 letter to the Chief Executive"),
 ("4 Oct 2025 12:43", "⭐⭐ <b>FORMAL REQUEST FOR REVIEW to J Roberts, cc H Moran</b> — "
  "“Performance Management Process and Handling of Confidential Disclosure”. Seeks "
  "suspension of the performance process, an independent review of the handling of the "
  "confidential disclosure and the leave request against Directive 03/20, <b>a formal "
  "audit and correction of the leave balance “improperly coded”</b>, and an impartial "
  "HR intermediary",
  "⭐ <b>Cory raised every element himself, in writing, to HR, with the union copied — "
  "eleven months before the 2026 exclusion.</b> ⚠ Contains restricted material"),
]




PH_DISMISSAL = [
 ("18 Jun 2024", "Injury onset. Certified leave follows; work capacity certificates supplied "
  "to HR <b>through WorkCover</b>, as HR had been advised",
  "His account, draft reply: \u201cit has been advised to Ms Taylor that HR would receive "
  "information and updates through WorkCover, including a work capacity certificate\u201d"),
 ("12 &amp; 16 Jul 2024", "Required to attend meetings convened by management <b>while on "
  "certified leave</b>", "Form 20 ¶42"),
 ("30 Aug 2024", "<b>CCC complaint</b> lodged", "Referred back to MSH 22 Nov 2024"),
 ("8 Sep 2024", "Work Capacity Certificate <b>signed</b> (Dr Hawes)",
  "⚠ The Form 24 ¶36 says \u201cdated 1 July 2024\u201d. <b>The Respondent corrects it to "
  "8 September 2024.</b> Fix every citation"),
 ("8 Oct 2024", "⭐ <b>EMPLOYMENT TERMINATED</b> on the basis of \u201cabandonment of "
  "employment\u201d", "Form 20 ¶43"),
 ("9 Oct 2024 16:10", "⭐⭐ <b>THE LETTER IS TRANSMITTED.</b> LBH_HR \u2192 Cory at both his "
  "work and personal addresses: \u201cI have attempted to call you this afternoon \u2026 was "
  "unable to speak with you. Please find attached correspondence from <b>Mr Steven Johns, "
  "Acting Executive Director, Logan and Beaudesert Health Service</b> \u2026 regarding your "
  "employment at Logan Hospital.\u201d",
  "Sent by <b>Faiza Firoz, HR Consultant, Human Resources, LBHS</b> \u2014 ⭐ <b>TWO NEW "
  "ACTORS.</b> Note the letter is transmitted the <b>day after</b> the termination date"),
 ("(the disagreement)", "⭐ <b>HIS CONTEST, itemised</b> \u2014 draft reply to LBH_HR: "
  "<b>(1)</b> the <b>dates</b> in the letter are wrong \u2014 \u201cthe <b>false dates of "
  "contact</b> included in this letter\u201d; <b>(2)</b> he is <b>a protected employee who "
  "had provided a work capacity certificate</b> and was under medical treatment with a "
  "psychiatric appointment upcoming; <b>(3)</b> the letter was issued <b>\u201cwithout proper "
  "diligence and due process, aiming to avoid overturning liability\u201d</b>; <b>(4)</b> HR "
  "\u201c<b>purposely delayed and coerced the outcome of the WorkCover claim</b>, with "
  "correspondence <b>twice exceeding a month over the 5 days allowed</b>\u201d; <b>(5)</b> "
  "the directive breaches the <b>Fair Work Act, Industrial Relations Act, Human Rights and "
  "the EB11 HHS agreement</b>; <b>(6)</b> WorkCover had given Queensland Health an outcome "
  "letter acknowledging a personal injury \u201cwhile making <b>no accommodations</b> for me "
  "and disregarding any injury or work capacity certificates supplied\u201d; <b>(7)</b> ⚠ the "
  "letter <b>referred to leave he took when his grandfather died</b> \u2014 "
  "\u201cextremely offensive and inappropriate\u201d; <b>(8)</b> the <b>fatigue pay</b> "
  "request renewed \u2014 <b>7 hours, not including travel time</b>; <b>(9)</b> he had "
  "already lodged a <b>crime and corruption complaint</b>",
  "⚠ <b>STATUS: a DRAFT, saved 28 Jul 2026 19:45</b> \u2014 i.e. revisited during the current "
  "dispute. <b>Confirm whether any version was ever sent.</b> ⛔ It uses language "
  "(\u201cwage theft\u201d, \u201ccoerced\u201d, the CCC reference) that <b>must not "
  "travel into the WC track</b> \u2014 discipline rules 1 and 2"),
 ("25 Oct 2024", "<b>TD/2024/110 \u2014 Form 12 application for reinstatement</b>, stamped",
  "`related-matters/TD2024-110_Form12_Application_for_reinstatement_stamped_25.10.2024.pdf`"),
 ("24 Oct 2024", "⭐ <b>Review Decision 69983</b> \u2014 the 7-hour break \u201camounted to "
  "unreasonable management action\u201d; employment <b>a significant contributing "
  "factor</b>", "⚠ Contents <b>admitted</b>, relevance reserved (de novo). Persuasive, "
  "<b>not binding</b>"),
 ("24 Dec 2024", "<b>PID 24-ESU-1130 determined</b> (Loader, ESU)", "Admitted, Form 24 ¶20"),
 ("(2025)", "<b>Reinstated</b> following TD/2024/110",
  "⛔ <b>EXACT DATE STILL TO SUPPLY.</b> The 26 Mar 2025 payslip carries "
  "<b>$29,390.05</b> in prior-period adjustments with <b>Term loading, RL_Term and Life "
  "Benefit ETP</b> codes \u2014 the termination package"),
]

PH_SUPPLY = [
 ("14 Jan 2024 08:06", "Taylor → Reese, \u201cUrgent Leave and Roster Update for Sunday, "
  "January 14th\u201d: reports Cory unable to attend the 0700\u20131500 shift on 15 minutes\u2019 "
  "notice, that she called another staff member in, and <b>attaches his text messages</b> "
  "(IMG_0973, IMG_0974)", "The texts disclose a <b>family police matter concerning his sister, "
  "then 15</b>. ⚠ <b>Cory had NO party status \u2014 neither aggrieved nor respondent</b> "
  "(corrected on his instruction 31 Jul / 2 Aug 2026). <b>Wholly separate from the Feb\u2013Mar "
  "2025 matter</b>"),
 ("1 Jul 2025 10:03", "⭐ <b>Taylor forwards the 14 Jan 2024 chain TO HERSELF</b>, carrying "
  "IMG_0973 and IMG_0974", "Sixteen months later. The retrieval step"),
 ("4 Jul 2025", "<b>Medical-records Form 29 signed by a Senior Registry Officer</b> "
  "(Respondent\u2019s own Response ¶23)", "⭐ <b>Issued in the proceeding ⇒ r 24(1) required "
  "service on each other party.</b> Never served on Cory. See ATT27 and confirmed-record"),
 ("10 Jul 2025 14:48", "⭐⭐ <b>TAYLOR → MATHESON</b> (Senior Appeals Officer, OIR), subject "
  "\u201cWC/2024/227 \u2026 Request for documentation\u201d, marked <b>High importance</b>, "
  "attaching <b>eight items</b> \u2014 Communication Book Update · Increase of hours and "
  "Workplace issues · <b>Urgent Leave and Roster Update for Sunday January 14th (carrying the "
  "text images)</b> · Line Manager addressing Pay Concerns · Validation of Claims · Office "
  "Hours and Departmental Directives · Respiratory Nurse Educators",
  "⭐ <b>The private family-matter disclosure is supplied to the Regulator by the Line "
  "Manager</b>, in answer to a request about lateness. <b>Over-supply:</b> the material has no "
  "connection to any pleaded workplace event"),
 ("~before 16 Jul 2025", "Regulator receives the GP records from Our Medical Ashmore",
  "Exhibit A5. Response ¶23"),
 ("14 Jul 2025", "Matheson emails Cory directly saying she had \u201creceived last week\u201d "
  "documents", "Notice ¶32. Admitted as <b>sent in error</b> \u2014 should have gone to his "
  "solicitors; Respondent says the medical records were <b>not yet in its possession</b>"),
 ("22 Jul 2025", "Regulator serves the <b>unredacted</b> GP records on Cory\u2019s former "
  "solicitors", "Notice ¶30, <b>admitted</b>. Not notified the solicitors had ceased acting "
  "until <b>29 Jul 2025</b>"),
 ("13 May 2026", "⚠ <b>Regulator\u2019s amended SOFC ¶8:</b> does not admit the allegations "
  "\u201c<b>because medical records identify a past medical history of anxiety</b>\u201d",
  "⭐ <b>The supplied material lands in a file running a pre-existing / non-work line.</b> "
  "This is why the over-supply matters"),
 ("11 Jun 2026", "Regulator discloses the 15\u201316 May 2024 HR correspondence",
  "Exhibit CS-4. The disclosure that falsifies Item 20"),
]

PH_VERIFIED = [
 ("Form 24 ¶8", "⭐ <b>PINPOINT CONFIRMED.</b> Notice ¶8 IS the patient-safety criticality "
  "statement; Response ¶8 <b>\u201cadmits the facts contained therein\u201d</b>",
  "⚠ But <b>¶9 is DENIED</b> \u2014 the criticality is admitted, the consequence of the "
  "removal is not"),
 ("Form 24 text layer", "⛔ <b>pdftotext DROPS every exhibit reference, date and quoted "
  "phrase.</b> Render with pdftoppm", "Added to CLAUDE.md source-integrity rules. Full "
  "register at FORM24-VERIFICATION-5AUG.md"),
 ("Form 24 exhibits", "Sixteen exhibits recovered. <b>Only A1, A5 and B1 confirmed held.</b> "
  "Eight not held \u2014 C2, D1, D2, E3, F2, F3, H1, I2",
  "⚠ ¶¶42\u201345 (pay disparity) rest on <b>D1, not in hand</b>. <b>I2 the Respondent holds "
  "and we do not.</b> FORM24-EXHIBITS-AND-ADMISSION-LAW.md"),
 ("Admissions", "<b>\u201cFor this proceeding only.\u201d</b> None of them operate in the "
  "employment track, an AD Act complaint, or before the CE",
  "\u201cDoes not admit\u201d ≠ \u201cdenies as untrue\u201d. <b>¶4 is their affirmative "
  "case \u2014 make them produce the June 2020 agreement</b>"),
 ("⭐ r 24(1)", "⛔ <b>THE EARLIER \u201cNO DUTY TO SERVE\u201d CONCLUSION WAS WRONG.</b> "
  "<b>r 24(1):</b> the party by or for whom a document is <b>filed or issued in a "
  "proceeding</b> must serve it on <b>each other party</b>",
  "The 4 Jul 2025 Form 29 was Registry-issued ⇒ r 24(1) applied. r 64D(1)(a)\u2019s "
  "\u201cother than a party\u201d avoids duplication, not exemption. ⚠ They will run "
  "r 24(2)(b); <b>their ¶25 never mentions r 24</b>"),
 ("⭐ r 64B(2)", "<b>THRESHOLD PROHIBITION:</b> a party <b>may not</b> require production where "
  "<b>another reasonably simple and inexpensive way</b> of proving the matter is available",
  "He was a party, represented, and they are his own records. <b>Never answered by the "
  "Respondent</b>"),
 ("r 64E(2) + 64F", "<b>LIVE REMEDY:</b> a person affected who was not served may object "
  "<b>at any time with leave</b>; an objection <b>operates as a stay</b>",
  "Grounds: relevance · privilege · confidentiality · effect on any person · should have "
  "been served"),
 ("r 64I", "The party <b>pays the non-party\u2019s reasonable expenses</b> of production",
  "⭐ <b>Cuts against MSH\u2019s expense objections</b> at Items 3(a), 3(b), 8, 10, 19 \u2014 "
  "cost is compensable, not a reason to refuse"),
 ("April 2025 stats", "⭐⭐ <b>269\u2013444 calls per shift, averaging 360</b>, while working "
  "at <b>29.3% of full-time</b>",
  "<b>The reduced hours cut the NUMBER of shifts, not the INTENSITY of each one.</b> The "
  "within-shift fatigue mechanism, proved from his own data"),
 ("Payslip analysis", "FY2025\u201326: 150.86 work days over 26 fortnights (5.80/ft against a "
  "full-time 10); <b>34.33 unpaid days</b>; gross $82,664.20",
  "⛔ <b>STOPS at the fortnight ending 7 Jun 2026.</b> Obtain the payslips for pay dates "
  "~1 Jul and ~15 Jul 2026 \u2014 they contain the last-worked-shift answer"),
 ("26 Mar 2025 payslip", "<b>$29,390.05</b> prior-period gross adjustment carrying <b>Term "
  "loading, RL_Term, Life Benefit ETP</b> codes; plus $5,000 non-taxable allowance adjustment",
  "⚠ <b>Material to the ART overpayment review</b> \u2014 termination package vs back pay "
  "changes what is treated as income for a period"),
 ("Outline of Submissions", "Filed <b>1 May 2026</b>, opposing MSH\u2019s r 64E extension",
  "⭐ <b>NEW ACTOR: the Chief People and Partnerships Officer</b>, to whom Thorburn forwarded "
  "the Form 29 at 17:26 on 22 Apr 2026, <b>eighteen minutes after service</b>. Thorburn = "
  "<b>Executive Director, Clinical Governance, Risk and Legal</b>"),
]

PH_QIRC = [
 ("18 Jun 2024", "Injury. Claim → rejected → review",
  "WCRA s 32(1): employment must be <b>a significant</b> contributing factor. "
  "⛔ NEVER “major” — the 2013 test was repealed in 2019"),
 ("24 Oct 2024", "⭐ <b>Review Decision 69983</b> — the Reviewing Officer finds the 7-hour "
  "rostering “amounted to unreasonable management action” and is satisfied employment "
  "was a significant contributing factor",
  "⚠ <b>Admitted as a DOCUMENT, persuasive, NOT binding</b> (Notice ¶37 / Resp ¶34): "
  "relevance reserved because the appeal is de novo. <b>Do not overstate it as conclusive</b>"),
 ("(2024–25)", "Appeal filed — WC/2024/227, s 550(4) WCRA, Commissioner Dwyer", ""),
 ("Jul 2025", "Regulator's Statement of Facts and Contentions (Form 9C) — original and the "
  "13 May 2026 version", "`documents/2025-07_Regulator_SOFC_Form9C_original.pdf`; served via "
  "Saines 22 Jul 2025"),
 ("Aug 2025", "<b>Form 35 — withdrawal of Saines Legal (P Conrad)</b>. Self-represented from "
  "this point", "`documents/filings/2025-08_Form35_Withdrawal…`"),
 ("18 Feb 2026", "⭐⭐ <b>FORM 24 — Response to the Notice to Admit Facts</b>",
  "The admissions the whole case now rests on. See the ledger below. "
  "⚠ <b>Cite in NOTICE numbering</b> — Resp ¶N ≠ Notice ¶N after ¶25"),
 ("17 Feb 2026", "Counsel unavailability; the mention moves 26 → 27 Feb", "Willson"),
 ("27 Feb 2026", "Mention — <b>Willson appears</b>", ""),
 ("13 Mar 2026", "<b>s 552A conference</b> — Willson appears", ""),
 ("7 Apr 2026", "Mention — Willson appears; the <b>five-week response window</b> is set",
  "Anchors the Respondent's amended SOFC to 13 May — exactly 35 days after the amended 9A"),
 ("8 Apr 2026", "⭐ <b>AMENDED FORM 9A — Statement of Facts and Contentions</b> "
  "(the Neville pleading, Stressor 3(b))",
  "Stressors: 1 course of management conduct (a)–(g) · 2 remuneration · 3 statutory fatigue "
  "breach · post-injury aggravation. ⚠ <b>MSH says it never received the amended 9A</b> — "
  "5 Jun objection, opening paragraph"),
 ("22 Apr 2026", "<b>Form 29 — Notice of Non-Party Disclosure sealed</b>; served on Matheson "
  "and Thorburn", "20 Items. From this date MSH knows the categories sought"),
 ("13 May 2026", "Regulator files its <b>amended SOFC</b>", "Willson does not appear at the "
  "next listing"),
 ("22 May 2026", "Mention — MSH non-attendance noted; MSH directed to object by 4pm Fri 5 Jun", ""),
 ("(undated)", "<b>Outline of Submissions</b>", "`documents/WC2024227_Outline_of_Submissions.pdf` "
  "— ⚠ confirm the filing date"),
 ("18 Jun 2026", "<b>Form 4 + Form 20 + Form 21 certificates + draft order (v2)</b>",
  "Filed and sealed 23 Jun. Draft order 3 = verification affidavit by the <b>CE or a "
  "delegated Director</b>; order 6 = s 580 non-publication of the PID"),
 ("1 Jul 2026 12:16", "<b>Calderbank #2</b> served on Matheson and the OIR appeals registry",
  "s 545 IR Act costs consequence. <b>Rejected 16 Jul 2026 15:54</b>"),
 ("24 Jul 2026", "Appellant requests the Respondent's list of documents", "Still outstanding"),
 ("30–31 Jul 2026", "Without-prejudice “material development” letter to Matheson", ""),
 ("3 Aug 2026 07:17", "Matheson replies on the disclosure list and the NNPD commitment", ""),
]

F24_ADMIT = [
 ("¶1", "Rostered to finish 23:00 and recommence 06:00 — a <b>7-hour break</b>",
  "⭐ <b>ADMITTED</b>"),
 ("¶3", "Award / FRMS minimum <b>10 hours</b>, or 8 only by written agreement",
  "⭐ <b>ADMITTED</b>"),
 ("¶5", "The fatigue grievance; Reese's email acknowledging “a rostering error … "
  "accidentally made by Chloe with regards to night shifts”", "<b>ADMITTED</b>"),
 ("¶6", "The Line Manager <b>removed a page from the communication book</b>",
  "<b>ADMITTED</b> — but not that it bore Cory's handwriting (¶7, “no copy of the "
  "page”)"),
 ("¶8", "The Switchboard procedure fact — “there was a procedure in place for this to "
  "occur”. <b>The Form 20 ¶6 cites Para 8 for the patient-safety criticality admission</b>",
  "<b>ADMITTED</b> ⚠ <b>PINPOINT CHECK</b> — confirm the criticality words sit at Notice ¶8 "
  "before relying on them"),
 ("¶14", "The communication book / 6 June 2023", "<b>ADMITTED</b>"),
 ("¶17", "<b>QH-POL-248</b> Union Encouragement Policy requires a “positive, supportive "
  "role”", "<b>ADMITTED</b> — policy wording only"),
 ("¶20", "⭐ <b>The ESU determined the complaint to be a PID</b>", "⭐ <b>ADMITTED</b>"),
 ("¶21", "The Director directed retraction within 48 hours of the PID",
  "<b>ADMITTED</b> — but “<b>no correlation between the two events</b>”; a further "
  "retraction email 21 May; “all emails to be read as a whole”. "
  "<b>Event admitted, causation contested</b>"),
 ("¶25", "No Form 29 was served on the Appellant before the Respondent obtained his medical "
  "records", "<b>ADMITTED</b> — with the defence “no requirement … pursuant to s 64D”; "
  "denies breach of r 64E"),
 ("¶37", "⭐ The <b>Review Decision</b> and both findings",
  "<b>CONTENTS ADMITTED, relevance reserved</b> (de novo)"),
 ("¶40", "Payroll instructed the Line Manager to “submit an AVAC to correct these shifts”",
  "<b>ADMITTED</b>"),
 ("¶41", "The AVAC was not submitted until <b>28 May 2024 — a 25-day delay</b>",
  "<b>ADMITTED</b> (delay admitted; justification contested)"),
 ("¶46", "The Line Manager's 21 May “waiting payroll confirmation” email", "<b>ADMITTED</b>"),
]

F24_DENY = [
 ("¶2", "The 7-hour roster <b>as unreasonable management action</b>",
  "⚠ <b>DOES NOT ADMIT</b> — for the Commission. <b>Never tag ¶2 “admitted”</b>"),
 ("¶4", "That there was <b>no written agreement</b>",
  "⛔ <b>DENIED</b> — “in June 2020 the Appellant signed an agreement allowing an 8 hour "
  "break”. <b>LIVE CONTEST — the single most important denial in the case</b>"),
 ("¶9 / ¶19", "Failure to facilitate the delegate appointment for over 9 months",
  "⛔ <b>DENIED</b> on three grounds (no request; support given; information provided). "
  "<b>Stressor 1(g); Item 19's target</b>"),
 ("¶12", "The communication book characterisation",
  "DENIED — the Line Manager called it “a professional tool”"),
 ("¶16", "Yelling as not reasonable management action",
  "DENIED — “characterisation is for the Commission”"),
 ("¶18", "The delegate-intention text as notification",
  "Sending <b>admitted</b>; characterised “<b>not a formal notification</b>”"),
 ("¶22", "The comparator email sent by the Line Manager on 9 May attracting no direction",
  "⛔ <b>DENIED</b> — “circumstances were different”. <b>The disparate-treatment fact "
  "Items 8–10 target</b>"),
 ("¶¶42–45", "Pay disparity",
  "⛔ <b>DENIED</b> — “the comparator does not represent a true comparator … "
  "<b>the roster was equitable</b>”. ⭐ <b>THE contested fact Items 8/9/10 attack. "
  "Anchor relevance here</b>"),
 ("¶¶47–49", "Delay and a false or misleading statement",
  "DENIED — “needed payroll confirmation”; “not false or misleading”; “no "
  "lack of diligence”"),
 ("¶50", "The Review Unit decision and a misleading statement by the Line Manager",
  "Contents admitted, relevance reserved; <b>does not admit</b> a misleading statement"),
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
        ("⭐⭐ THE DISMISSAL, THE LETTER AND THE DISAGREEMENT (Jun 2024 – 2025)", PH_DISMISSAL),
        ("PHASE 5 — REINSTATEMENT AND THE GRADUATED ARRANGEMENT (2025 – Jun 2026)", PH5),
        ("⭐⭐ THE MATERIAL SUPPLY CHAIN — MSH → THE REGULATOR (Jan 2024 – Jun 2026)", PH_SUPPLY),
        ("⭐ THE QIRC FILE — PLEADINGS, ADMISSIONS AND SUBMISSIONS", PH_QIRC),
        ("⭐⭐ FORM 24 LEDGER (18 Feb 2026) — WHAT IS ADMITTED", F24_ADMIT),
        ("⛔ FORM 24 LEDGER — WHAT IS DENIED OR NOT ADMITTED (the live contests)", F24_DENY),
        ("PHASE 6 — THE FORM 29, THE OBJECTION AND THE 64G (Feb–Jun 2026)", PH6),
        ("PHASE 7 — ⭐ THE LOCKOUT AND WHAT FOLLOWED (26 Jun – 31 Jul 2026)", PH7),
        ("PHASE 8 — THE PACKAGE AND THE RESPONSE (3–5 Aug 2026)", PH8),
        ("PHASE 9 — THE FORWARD CALENDAR", PH9),
        ("⭐⭐ VERIFIED FROM SOURCE, 5 AUGUST 2026", PH_VERIFIED),
        ("OUTSTANDING", OUTSTANDING),
    ]:
        if rows in (F24_ADMIT, F24_DENY):
            s.append(P(title, h2))
            s.append(tbl(rows, ("Notice ¶", "What was pleaded",
                                "The Respondent's answer")))
        else:
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
