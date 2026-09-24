#!/usr/bin/env python3
"""WC/2024/227 - request for copies of documents referred to in the Respondent's outlines of
evidence served 24 September 2026. DRAFT - not sent. Ask, never allege. No comment on the outlines."""
import os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

OUTDIR = "out/REQUEST_COPIES_DRAFT"
DATE = "[date]"
DUE = "Thursday 8 October 2026"
SUBJECT = "WC/2024/227 - Shepherd - request for copies of documents referred to in the Respondent's outlines of evidence"

PARAS = [
 "I refer to the Respondent's list of witnesses and outlines of evidence served on 24 September 2026.",
 "The outlines refer to the matters below. I have not been provided with a copy of any document recording them, and apart from item 1 none is described in the Respondent's amended List of Documents dated 14 August 2026. Could the Respondent please provide a copy of:",
]
ITEMS = [
 "the documents produced in response to the notice of non-party disclosure to Queensland Health filed on 27 April 2026 (item 42 of the amended List of Documents);",
 "any document recording the advice of the \"internal Technical Support team\" of Queensland Health Payroll referred to in the outline of Ms Wright concerning the shifts of 17 and 18 March 2024, including the date of that advice;",
 "the email of Ms Reese to me of 15 May 2024 at 4:12 pm referred to in the outline of Ms Reese;",
 "any document recording the advice of Human Resources to Ms Taylor that the agreement of 17 June 2020 \"was on file and continued to apply\", referred to in the outline of Ms Taylor, and any document relied on for the statement in that outline that all switchboard staff had signed such an agreement. I do not seek any other employee's agreement form;",
 "page 1 of the eight-hour shift break agreement form produced by Queensland Health Payroll on 11 July 2025, of which only the page marked \"Page 2 of 2\" is in the Respondent's disclosure. Item 3 of the Respondent's notice to Queensland Health of 4 July 2025 sought the \"Complete\" agreement;",
 "any document recording the treatment for pay purposes of my shift of 10 April 2023, and my contracted hours for the fortnight that included 30 March 2024, referred to in the outline of Ms Earl; and",
 "any other document to which any of the Respondent's four witnesses will refer at the hearing and which is not described in the amended List of Documents.",
]
TAIL = [
 "If any of these documents does not exist, a statement to that effect is sufficient.",
 f"Could the documents please be provided by {DUE}. If any is not provided by that date, I will ask the Commission for a direction for its production, and I will refer to this letter if the costs of that step arise.",
 "Nothing in this letter affects the nine documents listed in your email of 24 September 2026, which I note the Regulator has requested from Metro South Health.",
]

def pdf():
    ss = getSampleStyleSheet()
    B = ParagraphStyle('B', parent=ss['BodyText'], fontName='Helvetica', fontSize=10.2, leading=14, spaceAfter=7)
    I = ParagraphStyle('I', parent=B, leftIndent=16, firstLineIndent=-12)
    s = [Paragraph("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 | coryshepherd1@hotmail.com", B), Spacer(1, 4*mm),
         Paragraph("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>150 Mary Street, Brisbane QLD 4000<br/>By email: Renee.Matheson@oir.qld.gov.au", B),
         Paragraph(f"Dated {DATE}", B), Spacer(1, 2*mm),
         Paragraph(f"<b>{SUBJECT}</b>", B), Paragraph("Dear Ms Matheson,", B)]
    s += [Paragraph(p, B) for p in PARAS]
    s += [Paragraph(f"{i}.&nbsp;&nbsp;{t}", I) for i, t in enumerate(ITEMS, 1)]
    s += [Paragraph(p, B) for p in TAIL]
    s += [Spacer(1, 4*mm), Paragraph("Yours faithfully,<br/><br/><br/>Cory Lea Shepherd<br/>Appellant, self-represented", B)]
    out = f"{OUTDIR}/Request_for_copies_outlines_documents_DRAFT.pdf"
    SimpleDocTemplate(out, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=18*mm).build(s)
    p = pikepdf.open(out, allow_overwriting_input=True)
    try: del p.Root.Metadata
    except (AttributeError, KeyError): pass
    with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
    for k in list(p.docinfo.keys()): del p.docinfo[k]
    p.save(out + ".tmp"); p.close(); os.replace(out + ".tmp", out)
    return out

def txt():
    lines = [f"To: Renee.Matheson@oir.qld.gov.au", f"Subject: {SUBJECT}", "", "Dear Ms Matheson,", ""]
    lines += [p for x in PARAS for p in (x, "")]
    lines += [f"{i}. {t}" for i, t in enumerate(ITEMS, 1)] + [""]
    lines += [p for x in TAIL for p in (x, "")]
    lines += ["Yours faithfully,", "", "Cory Lea Shepherd", "Appellant, self-represented"]
    out = f"{OUTDIR}/Request_for_copies_outlines_documents_DRAFT.txt"
    open(out, "w").write("\n".join(lines) + "\n"); return out

print(pdf()); print(txt())
