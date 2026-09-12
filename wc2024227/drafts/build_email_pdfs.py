#!/usr/bin/env python3
"""WC/2024/227 — render the 9 September emails as clean PDFs.

Each email in FINAL_9SEP2026/3_EMAILS is rendered exactly as written: the routing block
(TO / CC / SUBJECT) at the head, then the body, then the ATTACH list. Nothing is added and
nothing is reworded, so the PDF and the text you paste into Outlook say the same thing.

These are reference and file copies. The emails themselves are sent as email; the PDFs are
for printing, for the matter file, and for anyone who needs the wording on paper.

All metadata is stripped and the build fails if any survives.
"""
import io, os, re
import pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

MAIL = "out/FINAL_9SEP2026/3_EMAILS"
DEST = "out/FINAL_9SEP2026/4_EMAILS_AS_PDF"

HD = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11,
                    textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=8)
TITLE = ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=12, leading=15, spaceAfter=6)
ROUTE = ParagraphStyle('ROUTE', fontName='Helvetica', fontSize=9.0, leading=12.4, spaceAfter=1.5)
B = ParagraphStyle('B', fontName='Helvetica', fontSize=9.6, leading=13.2, spaceAfter=7)
BULL = ParagraphStyle('BULL', parent=B, leftIndent=7*mm, firstLineIndent=-4*mm)
ATT = ParagraphStyle('ATT', fontName='Helvetica', fontSize=9.0, leading=12.4,
                     leftIndent=18*mm, firstLineIndent=-18*mm, spaceAfter=1.5)

EMAILS = [
    ("Email_1_to_Industrial_Registry_cc_Regulator.txt",
     "EMAIL 1 — TO THE INDUSTRIAL REGISTRY, COPIED TO THE RESPONDENT"),
    ("Email_2_to_Regulator_directions_and_request.txt",
     "EMAIL 2 — TO THE RESPONDENT: DIRECTIONS 1 AND 2, AND THE DOCUMENTS NOT ADMITTED"),
    ("Email_4_to_Dr_Krishnaiah_records_still_needed.txt",
     "EMAIL 4 — TO DR KRISHNAIAH: THE RECORDS AND HIS ATTENDANCE"),
]

HEADER = ("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",
          "Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' "
          "Compensation Regulator (Respondent)")

ROUTE_KEYS = re.compile(r'^(TO|CC|BCC|SUBJECT|To|Cc|Subject|From)\s*:', re.I)


def render(src, title, dest):
    raw = open(os.path.join(MAIL, src)).read().rstrip()

    # split into: routing lines at the head, body, ATTACH block at the tail
    lines = raw.split("\n")
    route, body_lines, attach = [], [], []
    i = 0
    while i < len(lines) and (ROUTE_KEYS.match(lines[i]) or
                              (route and lines[i].startswith((" ", "\t")) and lines[i].strip())):
        route.append(lines[i]); i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    rest = lines[i:]
    for j, ln in enumerate(rest):
        if ln.startswith("ATTACH:"):
            body_lines, attach = rest[:j], rest[j:]
            break
    else:
        body_lines = rest

    s = [Paragraph(HEADER[0], HD), Paragraph(HEADER[1], HD2), Paragraph(title, TITLE)]

    for ln in route:
        k, _, v = ln.partition(":")
        if v.strip():
            s.append(Paragraph(f"<b>{escape(k.strip().title())}:</b> &nbsp;{escape(v.strip())}", ROUTE))
        else:
            s.append(Paragraph("&nbsp;" * 12 + escape(ln.strip()), ROUTE))
    s.append(Spacer(1, 4*mm))

    para, i = [], 0
    def flush():
        if not para:
            return
        txt = " ".join(x.strip() for x in para)
        style = BULL if txt.startswith(("- ", "• ")) else B
        if txt.startswith("- "):
            txt = "&mdash;&nbsp;&nbsp;" + txt[2:]
        s.append(Paragraph(escape(txt).replace("&amp;mdash;", "&mdash;").replace("&amp;nbsp;", "&nbsp;"), style))
        para.clear()

    SIGNOFF = re.compile(r'^\s*(Yours faithfully|Yours sincerely|Kind regards|Regards|Thank you)\b.*,\s*$', re.I)
    in_signature = False
    for ln in body_lines:
        if in_signature:
            # a signature block is addresses and numbers: keep every line where it was written
            if ln.strip():
                s.append(Paragraph(escape(ln.strip()), ROUTE))
            else:
                s.append(Spacer(1, 2*mm))
            continue
        if SIGNOFF.match(ln):
            flush()
            s.append(Paragraph(escape(ln.strip()), B))
            in_signature = True
            continue
        if not ln.strip():
            flush()
        elif ln.lstrip().startswith("- ") and para:
            flush(); para.append(ln)
        else:
            para.append(ln)
    flush()

    if attach:
        s.append(Spacer(1, 3*mm))
        first = True
        for ln in attach:
            v = ln.replace("ATTACH:", "").strip()
            if not v:
                continue
            s.append(Paragraph(("<b>Attach:</b> &nbsp;" if first else "&nbsp;" * 8) + escape(v), ATT))
            first = False

    buf = io.BytesIO()
    doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm,
                          topMargin=16*mm, bottomMargin=16*mm)
    doc.addPageTemplates([PageTemplate(id='n', frames=[
        Frame(22*mm, 16*mm, A4[0]-44*mm, A4[1]-32*mm, leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)])])
    doc.build(s)
    buf.seek(0)

    pdf = pikepdf.open(buf)
    n = len(pdf.pages)
    try:
        del pdf.Root.Metadata
    except (AttributeError, KeyError):
        pass
    with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
        m.clear()
    try:
        del pdf.Root.Metadata
    except (AttributeError, KeyError):
        pass
    for k in list(pdf.docinfo.keys()):
        del pdf.docinfo[k]
    for pg in pdf.pages:
        for k in ('/Metadata', '/PieceInfo', '/Annots'):
            if k in pg.obj:
                del pg.obj[k]
    pdf.save(dest, linearize=True)

    chk = pikepdf.open(dest)
    clean = (not dict(chk.docinfo)) and '/Metadata' not in chk.Root and \
            not any('/Annots' in p.obj for p in chk.pages)
    return n, clean


os.makedirs(DEST, exist_ok=True)
bad = []
for src, title in EMAILS:
    if not os.path.exists(os.path.join(MAIL, src)):
        bad.append(f"{src}: missing"); continue
    out = os.path.join(DEST, src.replace(".txt", ".pdf"))
    n, clean = render(src, title, out)
    print(f"  {n}pp  {'clean' if clean else 'METADATA SURVIVED'}  {os.path.basename(out)}")
    if not clean:
        bad.append(f"{out}: metadata survived")
if bad:
    raise SystemExit("\n".join("⛔ " + b for b in bad))
print(f"\nbuilt {len(EMAILS)} email PDFs in {DEST}")
