#!/usr/bin/env python3
"""WC/2024/227 - Letter to the Regulator: matters that may be agreed before the s 552A conference, with Part 1 of
the 1 October 2026 Schedule updated, and facts 228-231 mapped to the rows of the native register file the
Regulator provided on 12 October 2026. Ask, never allege. Metadata stripped. Run with python3.13 (reportlab).

Usage: python3.13 build_preconference_positions_letter.py ["22 October 2026"] ["Friday 30 October 2026"]
"""
import io, sys, os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv) > 1 else "22 October 2026"
REPLY_BY = sys.argv[2] if len(sys.argv) > 2 else "Friday 30 October 2026"

B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.4, leading=12.2, spaceAfter=5)
C  = ParagraphStyle('C', parent=B, fontSize=8.2, leading=10.2, spaceAfter=0)
CB = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
def P(t, s=B): return Paragraph(t, s)
def SIG():
    i = RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); i.hAlign = 'LEFT'; return i
def grid(data, widths):
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#888888')),
                           ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EEEEEE')),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3),
                           ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    return t

W = A4[0] - 44*mm

# ---- Schedule Part 1, updated. (tab, document, date, 8 Sep, since, position now)
ADM, TND = "Admitted", "Admitted; tender"
rows = [
 ("1A", "Stibbard to the Switchboard team, \"Hello &amp; Update\"", "18 Jul 2023, 12:56 pm", ADM, "-", TND),
 ("1B", "Taylor to Reese, \"Fwd: Communication Book Update\", with her email to Logan Switch of 9:57 am that day", "6 Jun 2023, 4:05 pm", ADM, "-", TND),
 ("2", "\"Increase of hours and Workplace issues\" chain and Reese's replies", "7-10 Aug 2023", ADM, "-", TND),
 ("3", "Reese attaching HR Policy E12; emails of 4 and 8 Sep 2023", "29 Aug-8 Sep 2023", ADM, "-", TND),
 ("4", "\"Request to Increase Working Hours to Full Time Rotational Roster\"; emails of 7 Aug 2023, 1:43 pm and 5:11 pm", "7 and 31 Aug 2023", ADM, "-", TND),
 ("7", "\"Roster Concerns\" chain", "26 Apr-8 May 2024", ADM, "-", TND),
 ("8", "Reese to Pritchard, \"FW: Roster Concerns\"; Reese to LBH_HR attaching qh-gdl-401-3.3", "10 and 20 May 2024", ADM, "-", TND),
 ("8A", "Cover page, Fatigue risk management systems implementation guideline QH-GDL-401-3.3:2021", "2021", ADM, "-", TND),
 ("8B", "MASPER emails (Taylor to Kwok and Wong; \"MASPER process\") and issue logs", "9 May 2024 (logs 2-8 May)", ADM, "-", TND),
 ("8C", "Stibbard, \"Switchboard After Hours On Call Manager PP24\"", "13 May 2024, 4:29 pm", ADM, "-", TND),
 ("9", "Taylor, \"Switchboard Manager - On call and Hours.\"", "17 May 2024, 9:30 am", ADM, "-", TND),
 ("9A", "\"Office Hours and Departmental Directives\" chain (1:15 pm, 6:23 pm, 7:09 pm)", "15 May 2024", ADM, "-", TND),
 ("9B", "Reese, \"RE: Office Hours and Departmental Directives\"", "21 May 2024, 2:53 pm", ADM, "-", TND),
 ("10", "Taylor, \"Sick leave 14.05.24\", and its forwarding to Reese", "14-15 May 2024", ADM, "-", TND),
 ("11", "Marriott (Integrated Respiratory Service) to Logan Switch; the Appellant to Taylor; Taylor's reply", "15 and 20 May 2024", ADM, "-", TND),
 ("12", "\"Corey Shepherd 388372 Pay issues\" thread", "3-13 May 2024", ADM, "-", TND),
 ("13", "Same thread, Taylor to the Appellant", "21 May 2024, 12:33 pm", ADM, "-", TND),
 ("14", "Taylor, \"Validation of Claims older than 3 months - Please sign\"", "28 May 2024, 8:36 am", ADM, "-", TND),
 ("15", "myHR submissions report (MSH Item 11)", "1 Feb-31 May 2024", ADM, "-", TND),
 ("16", "QH Leave Takings Report (MSH Item 15)", "19 Mar 2024", ADM, "-", TND),
 ("25", "Review Decision 69983", "24 Oct 2024", ADM, "-", TND),
 ("26", "Appellant's first notice to admit facts", "before 18 Feb 2026", ADM, "-", TND),
 ("27", "Respondent's response to that notice", "18 Feb 2026", ADM, "-", TND),
 ("28", "myHR leave request history, Process Reference 15480560 (MSH Item 11)", "20 Feb-1 Mar 2024", ADM, "-", TND),
 ("29", "Instrument of Human Resource Sub-Delegation, Paid Special Pandemic Leave (MSH Item 13)", "eff. 5 Dec 2022", ADM, "-", TND),
 ("6", "Taylor, \"Afterhours Oncall Process - Switchboard\"", "15 Apr 2024, 12:39 pm", "Disputed", "Confirmed 24 Sep 2026", TND),
 ("20", "Metro South Health to Commissioner Dwyer, K-LM26/729, signed by the Chief Executive", "5 Jun 2026", "Disputed", "Confirmed 24 Sep 2026", TND),
 ("30", "Taylor, \"What's Chloe's Hours?!\"", "23 Aug 2023, 2:18 pm", "Disputed", "Confirmed 24 Sep 2026", TND),
 ("30A", "Taylor, \"Good morning Team.\"", "18 Jun 2024, 8:58 am", "Disputed", "Confirmed 24 Sep 2026", TND),
 ("1", "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital", "undated", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("5", "Taylor, \"Approved - Permanent Full Time FTE\"", "27 Sep 2023, 1:52 pm", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("17", "Movement form, approved by Mr Hughes as delegate, recording \"Continuous Shift Worker\"", "27 Feb 2026", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("18", "Movement form, approved by Mr Hughes, recording \"Continuous Shift Worker\"", "17 Apr 2026", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("19", "Movement form, approved by Mr Hughes, recording \"Continuous Shift Worker\"", "9 Jun 2026", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("21", "Forrest, Senior Consultant Human Resources, to the Appellant", "7 Jul 2026", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("22", "Consultation Paper, Proposed Rosters for Switchboard Services, signed by Mr Hughes 12 Nov 2024", "Nov 2024", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("23", "Consultation outcome, Proposed Rosters, signed by Mr Hughes 12 Dec 2024", "Dec 2024", "Disputed", "Confirmed 12 Oct 2026 (MSH copy)", TND),
 ("31", "\"2024 Emergency Code Register\", March 2024 sheet, entries 16-20 Mar 2024", "Mar 2024", "Disputed", "Confirmed 12 Oct 2026 (native file)", "Copy confirmed; facts 228-231 not yet admitted (see the table below)"),
 ("24", "Moran, Organiser, Together Queensland, to Jeffrey, Conaghan and the Appellant, \"Switchboard Roster Feedback - For Delegates\"", "3 Nov 2025", "Disputed", "Not yet addressed", "Outstanding; contents admitted (facts 178-179)"),
]
assert len(rows) == 39, len(rows)
hdr = ["Tab", "Document", "Date", "8 Sep 2026", "Since 8 Sep 2026", "Position now"]
data = [[P(c, CB) for c in hdr]] + [[P(c, C) for c in r] for r in rows]
sched = grid(data, [11*mm, W-11*mm-24*mm-16*mm-30*mm-30*mm, 24*mm, 16*mm, 30*mm, 30*mm])

extra = grid([[P(c, CB) for c in ["Tab", "Document", "Date", "Status"]],
              [P("32A", C), P("Role Description, Manager Switchboard Services, Logan Hospital (AO4), RD 30478699, as enclosed by Metro South Health with its letter of 5 June 2026 (Item 6)", C), P("as at 2021", C), P("Confirmed 16 Oct 2026; tender", C)],
              [P("32B", C), P("Instrument of Human Resource Sub-Delegation, COVID-19 Paid Special Pandemic Leave (Item 13); the same document as Tab 29", C), P("23 Nov 2022", C), P("Admitted (as Tab 29)", C)]],
             [11*mm, W-11*mm-24*mm-40*mm, 24*mm, 40*mm])

facts = grid([[P(c, CB) for c in ["Fact", "What the fact records", "Rows of sheet \"MARCH 2024\" in the native file provided on 12 October 2026"]],
              [P("228", C), P("17 March 2024: eight entries, including \"MET CALL WARD 2H BED 7\" at 19:16, \"CODE BLUE WARD 2H BED 7\" at 19:20 and \"MET CALL WARD 2Q BED 5\" at 21:16", C), P("Rows 9 to 16 (03:57, 05:19, 07:48, 13:48, 14:13, 19:16, 19:20, 21:16)", C)],
              [P("229", C), P("18 March 2024: \"CODE GREY QAS TRIAGE AIRLOCK\" at 8:48; \"MET CALL WARD 6A BED 8\" at 9:20; \"MET CALL WARD 3DR BED 14\" at 11:31; \"CANCELLED MET CALL WARD 3DR BED 14\" at 11:32; \"NEONATAL MET CALL THEATRE 2\" at 11:35; \"NEONATAL MET CALL BIRTH SUITES 5\" at 13:09", C), P("Rows 17 to 22", C)],
              [P("230", C), P("Six of the entries for 18 March 2024 bear times between 6:00 and 14:00", C), P("Rows 17 to 22; the next entry, row 23, is at 14:38", C)],
              [P("231", C), P("19 March 2024, 11:34: \"MET CALL WARD 2I BED 20\" with the notation \"CALLED VIA SWITRCHBOARD\" [sic]", C), P("Row 33 (the notation is in column E, \"EXTRA INFORMATION\")", C)]],
             [12*mm, W-12*mm-58*mm, 58*mm])

s = [P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com", B),
     Spacer(1, 2*mm),
     P("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>150 Mary Street, Brisbane QLD 4000<br/>By email: Renee.Matheson@oir.qld.gov.au", B),
     Spacer(1, 2*mm),
     P(f"Dated {DATE}", B),
     Spacer(1, 2*mm),
     P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
       "<b>Matters that may be agreed before the section 552A conference</b>", B),
     Spacer(1, 1*mm),
     P("Dear Ms Matheson,", B),
     P("Thank you for the Regulator's emails of 12 and 16 October 2026 confirming the veracity of the documents at Tabs 1, 5, "
       "17 to 19, 21 to 23 and 31 of Annexure A and of the role description at Tab 32A, and for your email of 19 October 2026 "
       "with counsel's availability for the conference.", B),
     P("With those confirmations, 38 of the 39 documents at Annexure A to the notices to admit served on 28 August 2026 are "
       "admitted or confirmed. Only Tab 24 is outstanding. Part 1 of the Schedule of 1 October 2026, updated to today's date, "
       "is attached.", B),
     P(f"So that the conference can be used efficiently, and without delaying it, could the Regulator please indicate its "
       f"position on the following matters by 4.00 pm on {REPLY_BY}? Any that are agreed can then simply be noted at the "
       f"conference.", B),
     P("<b>1. Facts 228 to 231.</b> These facts record entries in the Emergency Code Register and were not admitted on "
       "8 September 2026. Each reproduces entries in the native file \"2024 Emergency Code Register_16 to 20 March 2024.xlsx\" "
       "that the Regulator provided on 12 October 2026 and whose veracity it confirmed. The attached table identifies the "
       "entries by row. Does the Regulator now admit facts 228 to 231?", B),
     P("<b>2. Tender.</b> Does the Regulator agree that the 38 admitted or confirmed documents at Annexure A, and the document "
       "at Tab 32A, may be tendered at any hearing without further proof?", B),
     P("<b>3. Relevance and admissibility.</b> The Regulator's letter of 8 September 2026 and its email of 16 October 2026 "
       "reserve the right to object to the relevance or admissibility of any fact or document at the hearing. So that any "
       "such objection can be identified at the conference rather than at the hearing, could the Regulator please identify "
       "any admitted fact, or any document at Annexure A or Tab 32A, whose relevance or admissibility it intends to dispute, "
       "and the ground? Most of those documents were disclosed by the Respondent itself or produced by Metro South Health.", B),
     P("For clarity, the Appellant relies on the admitted documents as evidence that they exist, of their terms and dates, and "
       "of what the Respondent's statement of facts and contentions and List of Documents do and do not contain. He does not "
       "contend that the admission of a document is an admission of the truth of any statement in it, or that any admission "
       "decides whether any conduct was reasonable. Those are matters for the Commission.", B),
     P("<b>4. Section 32(1).</b> Review Decision 69983 found that the Appellant sustained a personal injury of a psychological "
       "nature and that his employment was a significant contributing factor to it (facts 261 and 262), and the claim was "
       "rejected under section 32(5) of the Act. Does the Regulator agree that the elements of section 32(1) are not in "
       "issue, so that the issue for any hearing is confined to section 32(5)?", B),
     P("<b>5. Leave.</b> Does the Regulator consent to leave to file the proposed Second Amended Statement of Facts and "
       "Contentions provided on 1 October 2026? If it intends to amend its own statement in response, how much time does "
       "it seek? I intend to provide, before the conference, a corrected version of the proposed statement with a one-page "
       "list of the changes. The corrections add no new stressor or allegation.", B),
     P("<b>6. Paragraph 27.</b> At the conference I will ask which management action the Regulator relies on for the "
       "contention in paragraph 27 of its amended statement of facts and contentions, so that the issues for any hearing "
       "can be identified.", B),
     P("To the extent these matters are not agreed, I will ask the Commission at the conference to deal with them and, if "
       "necessary, to make directions or to list the matter for mention.", B),
     P("Yours faithfully,", B), Spacer(1, 1*mm), SIG(), Spacer(1, 1*mm),
     P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B),
     PageBreak(),
     P(f"<b>WC/2024/227 &ndash; Schedule, Part 1, updated to {DATE}: the 39 documents at Annexure A (notices to admit served "
       f"28 August 2026) and their status</b>", B),
     P("On 8 September 2026 the Respondent admitted the authenticity of 25 of the 39 documents and disputed 14. It confirmed "
       "four of the 14 on 24 September 2026, nine on 12 October 2026 from the copies provided by Metro South Health, and the "
       "additional document at Tab 32A on 16 October 2026. Tab 24 has not yet been addressed. Of the 303 facts in the notice "
       "to admit facts, 298 were admitted on 8 September 2026; the five not admitted are fact 154, which is not relied upon "
       "in the proposed Second Amended Statement of Facts and Contentions, and facts 228 to 231.", B),
     Spacer(1, 1*mm), sched, Spacer(1, 3*mm),
     KeepTogether([P("<b>Additional document</b>", B), extra]), Spacer(1, 3*mm),
     KeepTogether([P("<b>Facts 228 to 231 and the native file provided by the Regulator on 12 October 2026</b>", B), facts])]

buf = io.BytesIO()
d = BaseDocTemplate(buf, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=11*mm, bottomMargin=11*mm)
d.addPageTemplates([PageTemplate(id='n', frames=[Frame(22*mm, 11*mm, A4[0]-44*mm, A4[1]-22*mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf = pikepdf.open(buf); n = len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
os.makedirs("out/PRECONF_22OCT2026", exist_ok=True)
out = "out/PRECONF_22OCT2026/LETTER_TO_REGULATOR_matters_to_agree_before_conference_DRAFT.pdf"
pdf.save(out, linearize=True); print("built", out, n, "page(s)")
