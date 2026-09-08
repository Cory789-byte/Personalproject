#!/usr/bin/env python3
"""WC/2024/227 - Appellant's schedule of medical documents relied upon (direction 2, expert-report limb).
ONE A4 PAGE. Serve on the Respondent with the outlines by 4.00 pm 9 September 2026. Not filed. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer

HD   = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11, textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2  = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=3)
TITLE= ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=11.5, leading=14, spaceAfter=2)
SUB  = ParagraphStyle('SUB', fontName='Helvetica-Oblique', fontSize=7.8, leading=10, textColor=colors.HexColor('#555555'), spaceAfter=3)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=7.9, leading=9.1, spaceAfter=1.6)
CELL = ParagraphStyle('CELL', parent=BODY, fontSize=7.2, leading=8.15, spaceAfter=0)
CELLB= ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')
INTROSTY = ParagraphStyle('INTROSTY', fontName='Helvetica', fontSize=7.6, leading=8.65, spaceAfter=1.2)
FOOT = ParagraphStyle('FOOT', parent=SUB, spaceBefore=2, spaceAfter=0)
def P(t, s=BODY): return Paragraph(t, s)
from reportlab.platypus import Image as RLImage
SIGW, SIGH = 38*mm, 20*mm
def SIG(w=None,h=None):
    _i = RLImage('assets/SIGNATURE_CoryShepherd.png', width=w or SIGW, height=h or SIGH)
    _i.hAlign = 'LEFT'
    return _i

def C(t): return Paragraph(t, CELL)

HEADER = ("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",
          "Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)")
TITLE_T = "APPELLANT'S SCHEDULE OF MEDICAL DOCUMENTS RELIED UPON"
SERVED = ("Served on the Respondent with the outlines of evidence under direction 2 of the Further Directions Order (3) "
          "dated 19 August 2026. Not filed in the Industrial Registry.")
INTRO = [
 ("Purpose and service.", "Served on the Respondent with the outlines of evidence under direction 2 of the Further Directions "
  "Order (3) dated 19 August 2026; not filed in the Industrial Registry. No report has been prepared for the purposes "
  "of this proceeding; this schedule and the pages behind it are served as the expert and treating material relied "
  "upon. Each document is already held by the Respondent at the item of its amended List of Documents dated 14 August "
  "2026 stated, except item 6, served herewith."),
 ("Use at hearing.", "Against each document is stated what it is, and is not, relied upon for. Items 3, 4 and 5 contain "
  "clinical opinion; the Appellant does not rely upon that opinion otherwise than through the oral evidence of its "
  "author. Dr Ravikumar Bangalore Krishnaiah and Dr Peter Hawes are named at items 2 and 3 of the Appellant's list of "
  "names of all witnesses filed today. Tabs 1 to 7 contain the pages relied upon; those omitted are identified on each tab sheet. Tabs 8 and 9 add the Respondent's responses of 18 February 2026 and the exchange with the author of 5 to 8 September 2026."),
 ("The sequence these documents record.", "No psychological illness before June 2024 (item 1); first presentation "
  "attributing symptoms to work, 28 June 2024 (item 1); certification of no capacity from 1 July 2024 (item 2); "
  "diagnosis of Major Depressive Disorder with anxiety state, 24 October 2024 (item 3); the treating psychiatrist's "
  "account of origin, 13 February 2025 (item 4); continuing effect, 3 July 2026 (item 6)."),
]

ROWS = [
 ("1", "General-practice records, Our Medical Ashmore, 1 January 2023 to 1 July 2024 (Respondent's item 11; "
       "obtained by the Respondent under the Form 29 signed 4 July 2025).",
  "Prior health: the entry of 16 November 2023 (Dr Nanayakkara) recording poor sleep with shift work, that the "
  "Appellant could not do shifts without a good sleep, no psychological illness such as depression or psychosis, "
  "and mood good, with melatonin and temazepam prescribed. The referral letter of 16 May 2024 (Dr Zhao), renewing a referral to a psychiatrist, Dr Amini, for \"ongoing care and management\", which lists the past medical history as the history-list items \"26/10/2022 ADHD\" and \"26/10/2022 Anxiety\", and lists the medications then current, which include no antidepressant, no anxiolytic and no other psychotropic medication. "
  "First presentation after onset: 28 June 2024 (Dr Slawinski) recording \"stress at work\" and \"upset by people "
  "not following rules\", reason for visit anxiety; and 1 July 2024 (Dr Hawes) recording \"work stress\", \"been there 5 years\", that "
  "\"they withhold pay at times, no overtime- not processed, manipulate his roster- so he works lates then "
  "earlies\", and \"causing anxiety\" (facts 185 to 203 and 211 to 221, admitted 8 September 2026). Relied upon as the "
  "contemporaneous record of what was reported before any claim decision, dismissal or proceeding.",
  "Entries unrelated to the injury. Private medical entries unrelated to the injury are redacted on the extracted pages and marked as such. The entry of 16 November 2023 is relied upon as the contemporaneous record that shift work was affecting the Appellant's sleep, and of what was prescribed for it, before any claim or proceeding (facts 2, 13, 214, 218, 263 to 265 and 269 to 271, admitted 8 September 2026); its clinical significance is a matter for the treating doctors."),
 ("2", "Work capacity certificates of Dr Peter Hawes dated 1 July, 11 August and 8 September 2024, and of Dr Ki "
       "Pang dated 7 August 2024 (Respondent's items 7 and 8).",
  "The stated date of injury, 18 June 2024; that the Appellant was first seen for this injury on 1 July 2024; "
  "continuous certification of no functional capacity from 1 July to 6 October 2024; and the referral to a "
  "psychiatrist recorded on 8 September 2024. Review Decision 69983 records at page 17 that the certificate of 1 July 2024 indicated \"there was no pre-existing factor or condition\", and that \"This was maintained in all later work capacity certificates\".",
  "The recorded mechanism as a finding of fact. The events are proved by the facts admitted on "
  "8 September 2026, not by the certificates. Nothing as to medication; the medication box is unticked on each."),
 ("3", "Email from the practice of Dr Ravikumar Bangalore Krishnaiah to the Appellant, 24 October 2024 at "
       "11:45 am, \"Medications\" (Respondent's item 9; Appellant's List item 22).",
  "That on the morning of 24 October 2024, at the first consultation, the treating psychiatrist told the "
  "Appellant, and confirmed in writing at 11:45 am that day, that he was \"suffering from psychological injury of "
  "Major Depressive Disorder with anxiety state\"; that fluoxetine was increased to two capsules \"from today\" and "
  "Seroquel 25 mg commenced at night, \"to restore basic needs- sleep, eating and routine\". Read with item 2, it "
  "records the progression of the injury certified as \"anxiety, stress\" on 1 July 2024 to a depressive "
  "disorder by 24 October 2024. The Appellant's email to QSuper at 5:12 pm that day (\"I have finally been able "
  "to see a psychiatrist today\") is reproduced with it.",
  "The reference to preoccupation with the claim as a cause of the injury. The injury relied upon is that of "
  "18 June 2024; the email records its state four months later."),
 ("4", "Report of Dr Krishnaiah, Mind and Memory Service, 13 February 2025, prepared for QSuper "
       "(Respondent's item 10).",
  "Diagnosis: Major Depressive Disorder with anxious distress (DSM-5 296.23). Severity and functional effect, "
  "and treatment (fluoxetine increased to three capsules daily; quetiapine 25 mg at night). The treating "
  "clinician's account of origin: \"workplace stress stemming from issues with management and rostering\"; that "
  "the issues \"began approximately one year ago when a new manager was appointed\"; pay \"withheld or delayed for "
  "up to five months at a time, leading to significant financial stress\"; and that \"premature exposure to the "
  "workplace is more likely result in significant deterioration\". The stressors so recorded correspond to facts admitted by the Respondent on 8 September 2026: management and rostering, and the night-shift line, at facts 211, 212 and 220; the shorter break, at facts 258 to 260; and pay withheld or delayed from the 5 February 2024 fortnight (facts 185 to 190), uncorrected at 13 May (fact 193), \"claims older than 3 months\" on 28 May (facts 196, 197), a claim effective 30 March \"Part Completed\" on 30 May (fact 203), and the two February claims absent from the myHR report (fact 210).",
  "Attribution among the individual events at paragraphs 2 to 7 of the Appellant's outline of evidence; any "
  "matter after 24 October 2024 as a cause of the injury. Prepared for QSuper; tendered as "
  "a treating record, not as a report for this proceeding. The report bears the footer that the information was disclosed \"for the only reason of clinical information and not for medico-legal use\"."),
 ("5", "Clinical records of Dr Krishnaiah from 24 October 2024 (offered by the practice on 5 September 2026 and "
       "requested; not yet received).",
  "What was reported at the first consultation and when; diagnosis and prescribing over time. To be served on "
  "receipt. If any direction is required for reliance on them, the Appellant will apply for it.",
  "Nothing until received."),
 ("6", "Employee Capability Checklist completed by Dr Day Hong Ma, 3 July 2026 (copy served herewith).",
  "Current capacity and restrictions, and the continuing effect of the injury, including \"symptom exacerbation "
  "on exposure to the identified workplace stressors\".",
  "Causation. It post-dates 1 July 2024 and is relied upon for effect and capacity only."),
 ("7", "Review Decision 69983, reasons dated 24 October 2024, pages 17 and 26 to 27 (Respondent's item 4; "
       "contents admitted 18 February 2026).",
  "That the Respondent's own review recorded Dr Hawes's statement to WorkCover of 2 September 2024 that work events "
  "were the sole cause, found \"a personal injury of a psychological nature\", found employment \"was a significant "
  "contributing factor\" as to factors 2, 3 and 4, and found the March 2024 rostering to be unreasonable management action (facts 257 to 261, admitted).",
  "As a binding determination. The hearing is de novo; the finding is relied upon as an admitted document."),
]

s = [P(HEADER[0], HD), P(HEADER[1], HD2), P(TITLE_T, TITLE)]
for _lab, _txt in INTRO:
    s.append(P('<b>' + _lab + '</b> ' + _txt, INTROSTY))
data = [[Paragraph("No.", CELLB), Paragraph("Document, and where the Respondent holds it", CELLB),
         Paragraph("Relied upon for", CELLB), Paragraph("Not relied upon for", CELLB)]]
for n, d, r, nr in ROWS:
    data.append([C(n), C(d), C(r), C(nr)])
W = A4[0] - 30*mm
t = Table(data, colWidths=[7*mm, W*0.26, W*0.47, W*0.27 - 7*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EEEEEE')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 1.1), ('BOTTOMPADDING', (0,0), (-1,-1), 1.1),
]))
s.append(t)
s.append(P("<b>The finding on section 32(1) in the decision under appeal.</b> On the medical evidence then before it \u2014 the work capacity certificates at item 2 and Dr Hawes's statement to WorkCover of 2 September 2024 \u2014 the Respondent's review of 24 October 2024 found that the Appellant \"sustained a personal injury of a psychological nature\", and stated: \"Having regard to the medical evidence, I am satisfied your employment was a significant contributing factor to the psychological injury\" (pages 17 and 26; item 7). The claim was rejected under section 32(5), not section 32(1). The hearing is de novo and that finding does not bind the Commission; it is relied upon as an admitted document.", INTROSTY))
s.append(P("The Appellant reserves the position as to any further report; if one is to be relied upon, directions will be sought before it is served.", FOOT))
sig = Table([[SIG(21*mm,11*mm),
              P("Dated: 9 September 2026<br/><b>Cory Lea Shepherd</b>, Appellant, self-represented", BODY)]],
            colWidths=[34*mm, W-34*mm])
sig.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'BOTTOM'),
                         ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
                         ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
s.append(sig)
buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=9*mm, bottomMargin=8*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(15*mm, 8*mm, A4[0]-30*mm, A4[1]-17*mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
doc.build(s); buf.seek(0)
pdf = pikepdf.open(buf); n = len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "out/SCHEDULE_OF_MEDICAL_DOCUMENTS_RELIED_UPON.pdf"
pdf.save(out, linearize=True)
print(f"built {out} - {n} page(s)", "OK" if n <= 2 else "⛔ EXCEEDS TWO PAGES")
if n > 2: raise SystemExit(1)
