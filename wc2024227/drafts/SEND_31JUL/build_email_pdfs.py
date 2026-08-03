#!/usr/bin/env python3
"""Render the five 3 Aug 2026 email bodies as individual PDFs, then stitch the six
outgoing documents into one combined attachments PDF. Metadata scrubbed like build_letters."""
import os, re, subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")

def read(p):
    with open(os.path.join(HERE, p)) as f:
        return f.read()

def block(paste, start, end):
    t = read("EMAILS_TO_PASTE_3AUG.txt")
    i = t.index(start); j = t.index(end, i)
    seg = t[i:j]
    m = re.search(r"^-{40,}\n(.*?)\n-{40,}", seg, re.S | re.M)
    return m.group(1)

EMAILS = [
    ("EMAIL_1_Response_HR_3Aug2026.pdf", "Email 1 — Response (RFMI) — to Human Resources", read("RFMI_RESPONSE_EMAIL.txt")),
    ("EMAIL_2_Request_HR_3Aug2026.pdf", "Email 2 — Request under clause 10.3.2 — to Human Resources",
     "TO: LBH.HRTeam1@health.qld.gov.au\nCC: Emily Petering; Heath Moran\nSUBJECT: Request under clause 10.3.2 — change in the way I work — C Shepherd, MSH-INJ-5795\n\n" + block(None, "EMAIL 2", "EMAIL 3")),
    ("EMAIL_3_Dispute_Taylor_HR_3Aug2026.pdf", "Email 3 — Notice of dispute — to C Taylor and Human Resources",
     "TO: chloe.taylor3@health.qld.gov.au; LBH.HRTeam1@health.qld.gov.au\nCC: Emily Petering; Heath Moran\nSUBJECT: Notice of dispute — clause 1.11 — attendance, roster, leave and pay from 26 June 2026\n\n" + block(None, "EMAIL 3", "EMAIL 4")),
    ("EMAIL_4_CE_3Aug2026.pdf", "Email 4 — The Chief Executive, Metro South Health",
     "TO: MetroSouthCorro@health.qld.gov.au (Office of the Chief Executive) — no Cc\nSUBJECT: Attention Ms Noelle Cridland, Chief Executive — Conflict of interest and information handling — C Shepherd, MSH-INJ-5795\n\n" + block(None, "EMAIL 4", "BEFORE YOU SEND")),
]

def render(fname, title, body):
    path = os.path.join(OUT, fname)
    c = canvas.Canvas(path, pagesize=A4)
    w, h = A4
    margin = 22 * mm
    y = h - margin
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin, y, title)
    y -= 6 * mm
    c.setFont("Helvetica", 8.5)
    c.drawString(margin, y, "Sent Monday 3 August 2026 — record copy of the email body as sent")
    y -= 8 * mm
    c.setFont("Courier", 8.6)
    for raw in body.splitlines():
        line = raw.rstrip()
        while True:
            if y < margin:
                c.showPage(); y = h - margin; c.setFont("Courier", 8.6)
            if len(line) <= 100:
                c.drawString(margin, y, line); y -= 4.1 * mm; break
            cut = line.rfind(" ", 0, 100)
            cut = cut if cut > 0 else 100
            c.drawString(margin, y, line[:cut]); y -= 4.1 * mm
            line = "  " + line[cut:].lstrip()
    c.setTitle(title); c.setAuthor(""); c.setSubject(""); c.setCreator(""); c.setProducer("")
    c.save()
    print("built", path)
    return path

built = [render(*e) for e in EMAILS]

DOCS = ["RFMI_Response_and_Allocation_MSH-INJ-5795.pdf",
        "PROPOSAL_Return_to_Work_MSH-INJ-5795.pdf",
        "NOTICE_Appointments_and_Costs_MSH-INJ-5795.pdf",
        "REQUEST_Change_in_the_way_I_work_cl10.3_MSH-INJ-5795.pdf",
        "NOTICE_OF_DISPUTE_cl1.11_Stage1.pdf",
        "LETTER_Conflict_and_Information_Handling_MSH-INJ-5795.pdf"]
stitched = os.path.join(OUT, "Shepherd_Documents_MSH-INJ-5795_3Aug2026.pdf")
subprocess.run(["qpdf", "--empty", "--pages"] + [os.path.join(OUT, d) for d in DOCS] + ["--", stitched], check=True)

import pikepdf
for p in built + [stitched]:
    pdf = pikepdf.open(p, allow_overwriting_input=True)
    with pdf:
        try:
            del pdf.Root.Metadata
        except (AttributeError, KeyError):
            pass
        try:
            del pdf.docinfo
        except (AttributeError, KeyError):
            pass
        pdf.trailer["/Info"] = pdf.make_indirect(pikepdf.Dictionary())
        pdf.save(p)
print("stitched", stitched)
