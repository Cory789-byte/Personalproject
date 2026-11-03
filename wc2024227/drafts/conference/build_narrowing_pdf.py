#!/usr/bin/env python3
import io, os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NARROWING_HYPOTHESIS_25SEP_DRAFT.pdf")
BAN = ParagraphStyle('ban', fontName='Helvetica-Bold', fontSize=9, leading=12,
                     textColor=colors.HexColor('#9b1c1c'), spaceAfter=6)
LH  = ParagraphStyle('lh', fontName='Helvetica-Bold', fontSize=11, leading=13)
LHS = ParagraphStyle('lhs', fontName='Helvetica', fontSize=8.5, leading=11, spaceAfter=8)
B   = ParagraphStyle('b', fontName='Helvetica', fontSize=9.6, leading=13.2, spaceAfter=5)
NUM = ParagraphStyle('num', parent=B, spaceAfter=4)
SUB = ParagraphStyle('sub', parent=B, leftIndent=7*mm, spaceAfter=3)
H   = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceBefore=6, spaceAfter=4)
CTR = ParagraphStyle('ctr', parent=H, alignment=1, fontSize=10)
NOTE= ParagraphStyle('note', fontName='Helvetica', fontSize=8.2, leading=10.6,
                     textColor=colors.HexColor('#555555'), spaceAfter=3)

s=[]
s.append(Paragraph("DRAFT ON THE HYPOTHESIS THAT THE RESPONSE OF 25 SEPTEMBER 2026 CONCEDES THE "
    "AUTHENTICITY OF THE DISPUTED TABS AND FORESHADOWS PRODUCTION OF THE REGISTER. NOT SENT. "
    "CONFORM EVERY BRACKET TO THE ACTUAL LETTER BEFORE ANY USE. Window: 26&ndash;30 September 2026, "
    "to Ms Matheson only, no cc.", BAN))
s.append(HRFlowable(width='100%', thickness=0.6, color=colors.HexColor('#9b1c1c'), spaceAfter=8))
s.append(Paragraph("CORY LEA SHEPHERD", LH))
s.append(Paragraph("15 Edmond Street, Coomera QLD 4209 | coryshepherd1@hotmail.com", LHS))
s.append(Paragraph("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>"
                   "By email: Renee.Matheson@oir.qld.gov.au", B))
s.append(Paragraph("Dated [26&ndash;30] September 2026", B))
s.append(Paragraph("<b>WC/2024/227 &ndash; proposed narrowing of issues for the second conference</b>", B))
s.append(Paragraph("Dear Ms Matheson,", B))
s.append(Paragraph("Thank you for the Respondent's response of 25 September 2026.", B))
s.append(Paragraph("Before I write to the Industrial Registry under direction 5, I attach what I intend to "
    "propose at the second conference, so that any matters the Regulator can agree are recorded with its "
    "agreement rather than around it. If the Regulator wishes to suggest amendments, I will consider them "
    "before 1 October 2026.", B))
s.append(Paragraph("Kind regards,<br/>Cory Lea Shepherd<br/>Appellant, self-represented", B))
s.append(PageBreak())

s.append(Paragraph("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", CTR))
s.append(Paragraph("WC/2024/227 &ndash; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)", CTR))
s.append(Paragraph("APPELLANT'S PROPOSED NARROWING OF THE ISSUES FOR HEARING", CTR))
s.append(Spacer(1,6))
P=lambda t: s.append(Paragraph(t, NUM)); Q=lambda t: s.append(Paragraph(t, SUB))
P("<b>1.&nbsp;&nbsp;Purpose.</b> This note is provided to assist the second conference to identify, under "
  "Part 5.2 of the Workers' Compensation Appeal Guide, the elements of section 32 that can be agreed, the "
  "evidence to be led, and the length of hearing required. It makes no submission on the merits, and nothing "
  "in it limits the Commission.")
P("<b>2.&nbsp;&nbsp;Matters the Appellant proposes be recorded as not requiring evidence at the hearing:</b>")
Q("(a)&nbsp;&nbsp;the 298 facts admitted by the Respondent on 8 September 2026 in response to the notice to "
  "admit facts served 28 August 2026, admitted for this proceeding under rule 49 of the <i>Industrial "
  "Relations (Tribunals) Rules 2011</i>;")
Q("(b)&nbsp;&nbsp;the authenticity of the documents at Tabs [1, 5, 6, 17, 18, 19, 20, 21, 22, 23, 30 and "
  "30A] [and 24] of Annexure A to that notice, conceded by the Respondent's response of 25 September 2026, "
  "so that each may be tendered without further proof of what it is;")
Q("(c)&nbsp;&nbsp;the matters of employment and role (paragraphs 1 to 16 of the notice).")
P("<b>3.&nbsp;&nbsp;The register.</b> The Respondent's response of 25 September 2026 states that [the March "
  "2024 sheet of the workbook \"2024 Emergency Code Register.xlsx\" will be produced / Metro South Health "
  "has been asked to provide it]. On production, the Appellant will ask the Respondent to confirm within "
  "seven days whether the entries at paragraphs 228 to 231 of the notice are then admitted, so that the "
  "register can be dealt with at the conference in the same way as the matters at 2.")
P("<b>4.&nbsp;&nbsp;Matters that may remain in dispute</b>, on which the parties' positions can be confirmed "
  "at the conference:")
Q("(a)&nbsp;&nbsp;whether the Appellant sustained an \"injury\" within section 32(1) (element (b)) &ndash; "
  "the treating practitioners are listed and will be called;")
Q("(b)&nbsp;&nbsp;whether employment was a significant contributing factor (element (d));")
Q("(c)&nbsp;&nbsp;whether, and to what extent, the Respondent contends that any matter pleaded is management "
  "action within section 32(5)(a), and the evidence relied on for that contention.")
P("<b>5.&nbsp;&nbsp;Proposed programming</b>, if the matters at 4 remain in dispute:")
Q("(a)&nbsp;&nbsp;hearing estimate: one day;")
Q("(b)&nbsp;&nbsp;witnesses for the Appellant: the Appellant; Dr P Hawes; Dr R B Krishnaiah. Mr C "
  "Harrison-Jones and Ms P Conaghan are maintained on the filed list and would be required only if any "
  "matter at 2 is not recorded as agreed;")
Q("(c)&nbsp;&nbsp;any medical examination the Respondent seeks under section 556 to be raised at the "
  "conference, so that it can be programmed without delaying a listing;")
Q("(d)&nbsp;&nbsp;exchange of the documents to be relied on in accordance with section 554.")
P("<b>6.</b>&nbsp;&nbsp;The Appellant is ready for hearing dates to be set at the conference.")
s.append(Spacer(1,8))
s.append(Paragraph("Dated [26&ndash;30] September 2026<br/><br/>____________________________<br/>"
                   "Cory Lea Shepherd, Appellant", B))
s.append(Spacer(1,10))
s.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#999999'), spaceAfter=5))
s.append(Paragraph("<b>CONFORMING NOTES (internal &ndash; remove before sending):</b> &para;2(b) list only "
  "the tabs their letter concedes, in its own terms; include 24 only if the concession covers all fourteen; "
  "if conceded by category, mirror the category phrase. &para;3 mirror their register sentence exactly; if "
  "produced with the letter, substitute the short form. If the 30 Sep list names an expert, add its report "
  "timing at 5(c); if it names no MSH officer, add at 4(c) \"including whether the Respondent intends to "
  "lead any evidence of the reasons for the matters pleaded.\" No costs anywhere in this document; the "
  "reservation lives in the letter of 9 September and is not repeated.", NOTE))

buf=io.BytesIO()
SimpleDocTemplate(buf, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                  topMargin=16*mm, bottomMargin=16*mm).build(s)
buf.seek(0)
pdf=pikepdf.open(buf)
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
print("built", OUT, len(pikepdf.open(OUT).pages), "pages")
