#!/usr/bin/env python3
"""WC/2024/227 - Medical documents relied upon: the schedule, then the pages relied on, by tab.
Originals only. Pages not relied upon are omitted whole and identified on each tab sheet. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.pdfgen import canvas
from PIL import Image

D='../documents/'
HD  = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11, textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=10)
TAB = ParagraphStyle('TAB', fontName='Helvetica-Bold', fontSize=20, leading=24, spaceAfter=4)
TT  = ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=11.5, leading=14.5, spaceAfter=8)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.6, leading=12.8, spaceAfter=5)
LAB = ParagraphStyle('LAB', parent=B, fontName='Helvetica-Bold', spaceAfter=1)
def P(t,s=B): return Paragraph(t,s)

HEADER=("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",
        "Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent) "
        "&nbsp;|&nbsp; Appellant's schedule of medical documents relied upon &ndash; the documents")

TABS=[
 dict(n=1, title="General-practice records, Our Medical Ashmore, 1 January 2023 to 1 July 2024",
      held="Respondent's amended List of Documents item 11. Obtained by the Respondent under the Form 29 signed 4 July 2025. The complete record is Exhibit A5, sealed by the Commission on 13 March 2026; these are extracts of it.",
      incl="Pages 5, 6, 7, 10, 11, 12 and 13 of the 14-page practice export: the consultation of 16 November 2023 (Dr Nanayakkara); the consultations of 16 May 2024 (Dr Zhao, referral renewed) and 28 June 2024 (Dr Slawinski); the consultation of 1 July 2024 (Dr Hawes); the referral letter to Dr Amini of 16 May 2024 with the past medical history; the medical certificate of 28 June 2024; and the work capacity certificate of 1 July 2024.",
      omit="Pages 1 to 4 (patient details, medication and prescription lists, consultations of 2023 for unrelated conditions); page 8 (Gold Coast University Hospital discharge letter of 6 June 2024, dental); page 9 (medical certificate of 3 July 2023, unrelated); page 14 (blank). None is relied upon. REDACTIONS: on source pages 5, 6 and 10, entries concerning private medical matters unrelated to the injury have been blacked out by the Appellant and are marked as such on the page. Nothing relied upon has been redacted. The Respondent holds the unredacted record at item 11.",
      src=('pdf', D+'medical/2025-07-22_OurMedicalAshmore_GP_records_via_Saines.PDF', [5,6,7,10,11,12,13]),
      redacted={5:'/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/gp150-5-REDACTED.png',
                6:'/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/gp150-6-REDACTED.png',
                10:'/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/gp150-10-REDACTED.png'}),
 dict(n=2, title="Work capacity certificates: Dr Ki Pang, 7 August 2024; Dr Peter Hawes, 11 August 2024 and 8 September 2024",
      held="Respondent's amended List of Documents items 7 (Hawes, 1 July, 11 August and 8 September 2024) and 8 (Pang, 7 August 2024).",
      incl="The certificates of 7 August 2024 (Dr Pang), 11 August 2024 and 8 September 2024 (Dr Hawes), reproduced from the scanned copies annexed to the Appellant's application in TD/2024/110 filed 25 October 2024. Together with the certificate of 1 July 2024 at Tab 1 (bundle page 9), they certify no capacity for any work continuously from 1 July to 6 October 2024, each recording the stated date of injury as 18 June 2024 and first presentation on 1 July 2024; the certificate of 8 September 2024 records the referral to a psychiatrist.",
      omit="None. The medication box on each certificate is unticked; nothing is relied upon as to medication from these certificates.",
      src=('pdf', D+'related-matters/TD2024-110_Form12_Application_for_reinstatement_stamped_25.10.2024.pdf', [22,24,23])),
 dict(n=3, title="Email from the practice of Dr Ravikumar Bangalore Krishnaiah to the Appellant, 24 October 2024 at 11:45 am, \"Medications\"; and the Appellant's email to QSuper at 5:12 pm the same day",
      held="The practice email: Respondent's amended List of Documents item 9; Appellant's List item 22. The QSuper email: from the QSuper income-protection correspondence bundle held by the Appellant; served herewith.",
      incl="Page 1 of the practice email, as forwarded from the Appellant's mailbox on 25 November 2024 and bearing the original header of 24 October 2024 11:45 am. Then the page of the QSuper correspondence bundle carrying the Appellant's email of 24 October 2024 at 5:12 pm (\"I have finally been able to see a psychiatrist today\"), which fixes the date of first consultation from a second, contemporaneous document.",
      omit="Page 2 of the practice email (the continuation of the sender's signature block and a list of helpline numbers). The remainder of the QSuper bundle. Neither is relied upon.",
      srcs=[('pdf', D+'medical/2024-10-24_1145_Krishnaiah_email_Medications_MDD_with_anxiety_state_fluoxetine_increase_Seroquel_LODitem9.pdf', [1]),
            ('pdf', D+'2026-07-14_QSuper_IP_RTW_Correspondence_Bundle.pdf', [4])]),
 dict(n=4, title="Report of Dr Krishnaiah, Mind and Memory Service, 13 February 2025, prepared for QSuper",
      held="Respondent's amended List of Documents item 10.",
      incl="All four pages. The report is reproduced whole so that nothing relied upon is read out of its context.",
      omit="None.",
      src=('pdf', D+'medical/2025-02-13_MindAndMemory_report_QSuper_LouiseIngs.pdf', [1,2,3,4])),
 dict(n=5, title="Clinical records of Dr Krishnaiah from 24 October 2024",
      held="Offered by the practice on 5 September 2026 and requested. Not yet received.",
      incl="None at the date of service. The records will be served on receipt, and any direction required for reliance on them will be sought.",
      omit="Not applicable.",
      src=None),
 dict(n=6, title="Employee Capability Checklist completed by Dr Day Hong Ma, 3 July 2026",
      held="Not on the Respondent's list. Served with this bundle.",
      incl="All five pages.",
      omit="None.",
      src=('pdf', D+'medical/Employee_Capability_Checklist_CShepherd_03-07-2026.pdf', [1,2,3,4,5])),
 dict(n=7, title="Review Decision 69983, reasons for decision dated 24 October 2024, pages 17, 26 and 27 of 28",
      held="Respondent's amended List of Documents item 4. Contents admitted by the Respondent on 18 February 2026.",
      incl="Page 17 (the medical evidence and the finding that employment was a significant contributing factor), and pages 26 and 27 (the findings on management action and the conclusion).",
      omit="The remaining 25 pages, which the Respondent holds and which are not relied upon for the purposes stated in the schedule.",
      src=('pdf', D+'Review_Decision_69983_24.10.2024.pdf', [17,26,27])),
 dict(n=8, title="The Respondent's responses of 18 February 2026 to the Appellant's first notice to admit, so far as they concern the medical documents",
      held="The Respondent's own document, served by it on 18 February 2026.",
      incl="Page 4 of the notice (items 32 to 38: the 16 November 2023 entry, the Hawes certificate, the Review Decision finding and the Krishnaiah diagnosis) and page 9 of the response (rows 30 to 36, answering paragraphs 33 to 39), in which the Respondent admits that each document exists and says what it says, admits the contents of the Review Decision, and reserves only accuracy and relevance.",
      omit="The remaining pages of the notice and response, which concern other subjects.",
      src=('pdf', D+'2026-02-18_Form24_Response_and_email_communication.pdf', [4,9])),
 dict(n=9, title="The question put to the treating psychiatrist, his answer, the notice the question came from, and the report he identified: 5 to 8 September 2026",
      held="Not on the Respondent's list, except the notice at item 3, which is the Respondent's own Form 29. Served with this bundle.",
      incl="Four documents, in this order. (1) The Appellant's email to Dr Krishnaiah of 5 September 2026 at 10:49 am, asking him to address the three matters in issue named in the Respondent's notice of non-party disclosure - whether the Appellant sustained a personal injury, whether it arose out of or in the course of employment, and whether employment was a significant contributing factor - from his own assessments and records (pages 5 to 7 of the chain as printed). (2) Dr Krishnaiah's reply of 8 September 2026 at 7:18 am: that he had attached \"the report that captures the relevant information you have requested\" (page 1 of the chain). (3) The Respondent's Form 29 notice of non-party disclosure to the Mind and Memory Service, sealed 4 July 2025, pages 1 and 2, being the sealed cover and the page stating the three matters in issue. (4) The report he attached, of 13 February 2025, which is the report at Tab 4 and is reproduced here so that the exchange is complete. No report has been prepared for this proceeding.",
      omit="Pages 2 to 4 of the email chain, being the intervening messages of 5 September 2026, which are not relied upon; and pages 3 to 6 of the Form 29, being the schedule of documents sought and the remaining form pages.",
      srcs=[('pdf', D+'correspondence-2026/2026-09-08_0718_Krishnaiah_staff_sickness_records_not_sent_report_attached.pdf', [5,6,7]),
            ('pdf', D+'correspondence-2026/2026-09-08_0718_Krishnaiah_staff_sickness_records_not_sent_report_attached.pdf', [1]),
            ('pdf', D+'2025-07-04_NNPD_Regulator_to_MindAndMemory_SEALED.pdf', [1,2]),
            ('pdf', D+'medical/2025-02-13_MindAndMemory_report_QSuper_LouiseIngs.pdf', [1,2,3,4])])
]

def tab_sheet(t):
    buf=io.BytesIO()
    doc=BaseDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm)
    doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(18*mm,16*mm,A4[0]-36*mm,A4[1]-32*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
    s=[P(HEADER[0],HD),P(HEADER[1],HD2),P(f"TAB {t['n']}",TAB),P(t['title'],TT),
       P("Where the Respondent holds it",LAB),P(t['held']),
       P("Pages included",LAB),P(t['incl']),
       P("Pages omitted, and why",LAB),P(t['omit']),
       Spacer(1,4*mm),P({8:"This tab is added so that the Respondent's own position on the documents at Tabs 1, 2, 4 and 7 sits with them.",
         9:"This tab is added so that the question, the answer, the notice the question came from and the report the author pointed to can be read together. Schedule row 4 states what the report is, and is not, relied upon for."}.get(t['n'], "Schedule row "+str(t['n'])+" states what this document is, and is not, relied upon for."),B)]
    doc.build(s); buf.seek(0); return pikepdf.open(buf)

def scan_page(path):
    buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=A4); c.drawImage(path,0,0,A4[0],A4[1]); c.showPage(); c.save(); buf.seek(0); return pikepdf.open(buf)

def img_page(path):
    im=Image.open(path).convert('RGB'); w,h=im.size
    buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=A4)
    maxw,maxh=A4[0]-30*mm,A4[1]-40*mm; sc=min(maxw/w,maxh/h); dw,dh=w*sc,h*sc
    c.drawImage(path,(A4[0]-dw)/2,(A4[1]-dh)/2+5*mm,dw,dh,preserveAspectRatio=True)
    c.setFont('Helvetica-Oblique',8); c.setFillColor(colors.HexColor('#555555'))
    c.drawCentredString(A4[0]/2,14*mm,"Photograph of the signed original as held by the Appellant; reproduced at the resolution held.")
    c.showPage(); c.save(); buf.seek(0); return pikepdf.open(buf)

out=pikepdf.Pdf.new()
def add(pdf, pages=None):
    for i,pg in enumerate(pdf.pages):
        if pages is None or (i+1) in pages: out.pages.append(pg)

add(pikepdf.open('out/SCHEDULE_OF_MEDICAL_DOCUMENTS_RELIED_UPON.pdf'))
stamps=[('Schedule',None)]  # per output page: (label)
for t in TABS:
    ts=tab_sheet(t); add(ts); stamps.append((f"Tab {t['n']}", 'sheet'))
    srcs=t.get('srcs') or ([t['src']] if t.get('src') else [])
    for (kind,path,pages) in srcs:
      if kind=='pdf':
        src=pikepdf.open(path); red=t.get('redacted',{})
        for pno in pages:
            if pno in red: add(scan_page(red[pno]))
            else: add(src,[pno])
            stamps.append((f"Tab {t['n']}", pno))
      else:
        add(img_page(path)); stamps.append((f"Tab {t['n']}", 'image'))

N=len(out.pages)
# footer stamp overlay on every page except the schedule
for idx,pg in enumerate(out.pages):
    if idx==0: continue
    lab,orig=stamps[idx]
    buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=(float(pg.mediabox[2])-float(pg.mediabox[0]), float(pg.mediabox[3])-float(pg.mediabox[1])))
    c.setFont('Helvetica',7); c.setFillColor(colors.HexColor('#444444'))
    txt=f"WC/2024/227 · Medical documents relied upon · {lab}"+(f" · source page {orig}" if isinstance(orig,int) else "")+f" · page {idx+1} of {N}"
    c.drawRightString(float(pg.mediabox[2])-10*mm, 5*mm, txt); c.showPage(); c.save(); buf.seek(0)
    ov=pikepdf.open(buf); pg.add_overlay(ov.pages[0])

try: del out.Root.Metadata
except (AttributeError,KeyError): pass
with out.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del out.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(out.docinfo.keys()): del out.docinfo[k]
dest='out/MEDICAL_DOCUMENTS_RELIED_UPON_schedule_and_pages.pdf'
out.save(dest,linearize=True); print("built",dest,N,"pages")
import scrub_pdf as _sc
print('scrub:', _sc.scrub_file(dest if 'dest' in dir() else out_path), 'annotation(s) removed')
