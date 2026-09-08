#!/usr/bin/env python3
"""WC/2024/227 - Appellant's letter to the Regulator responding to its letter of 8 September 2026,
served with the direction 2 material on 9 September 2026. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.platypus import Image as RLImage

B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.0, leading=11.4, spaceAfter=3.5)
HB  = ParagraphStyle('HB', parent=B, fontName='Helvetica-Bold', spaceAfter=2)
def P(t,s=B): return Paragraph(t,s)
def SIG(): 
    i=RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); i.hAlign='LEFT'; return i

s=[P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com",B),
   Spacer(1,2*mm),
   P("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>150 Mary Street, Brisbane QLD 4000<br/>By email: Renee.Matheson@oir.qld.gov.au",B),
   Spacer(1,2*mm),
   P("Dated 9 September 2026",B),
   Spacer(1,2*mm),
   P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
     "<b>Your letter of 8 September 2026 and the responses to the Form 24 and Form 25 notices</b>",B),
   Spacer(1,1*mm),
   P("Dear Ms Matheson,",B),
   P("Thank you for the responses of 8 September 2026 and the letter that accompanied them. I note the matters "
     "the letter sets out, and I set out below the basis on which the Appellant proceeds, so that the two positions "
     "sit together on the record with the material served today.",B),

   P("1. Matters not in contest",HB),
   P("The admissions are made for this proceeding only, under rule 49 of the Industrial Relations (Tribunals) Rules "
     "2011. The hearing is de novo. Relevance, admissibility and weight are for the Commission. The Appellant does "
     "not contend otherwise, and draws no characterisation, conclusion or inference from any admitted fact beyond "
     "the fact admitted.",B),

   P("2. What the admitted facts are",HB),
   P("Each fact in the notice states that a named document was sent, published, submitted, recorded, approved or "
     "received on a stated date, and what it says. The admissions establish those facts. Where the document is "
     "itself the step taken &ndash; a roster as published, a directive as issued by email, a payroll instruction or "
     "claim as recorded, a request as made and the reply as given, each on the date recorded &ndash; the Appellant "
     "relies on the admission as establishing that the step was taken on that date in those terms. The Appellant "
     "does not rely on those documents as statements about some other event. That is the footing on which facts "
     "49, 66, 74 to 77 and 81 (the directives and the replies to them), 182 to 205 and 210 (the payroll thread and "
     "the myHR report), 211 to 223 (the rostering correspondence) and 263 to 271 (Metro South Health's statements "
     "to the Commission in answer to the notice of non-party disclosure) are relied upon. The same footing applies to the reports made "
     "to the Switchboard manager by the MASPER Registrar on 3 and 8 May 2024 and by the Integrated Respiratory Service on "
     "15 and 20 May 2024, and to the replies to them (facts 56 to 68 and 89 to 104): each report of calls reaching the wrong "
     "team, or that \"we can not help patients or other clinical staff\", was made, and each reply given, on the date and in "
     "the terms recorded. Several of the documents in those ranges were sent by Ms Taylor or Ms Reese, whom the Appellant "
     "expects the Respondent to call.",B),

   P("3. Documents recording the statements of others",HB),
   P("Where an admitted document records a statement, finding or opinion of another person &ndash; the treating "
     "practitioners' records, the report of 13 February 2025 and Review Decision 69983 &ndash; the Appellant relies "
     "on the admission for the existence and wording of the document and on the oral evidence of its author for "
     "the rest. Dr Ravikumar Bangalore Krishnaiah and Dr Peter Hawes are named at items 2 and 3 of the witness "
     "list and will be called. Review Decision 69983 is not relied upon as binding the Commission; it is relied "
     "upon as an admitted document recording the Regulator's own review on the medical evidence then before it.",B),

   P("4. The material served today",HB),
   P("Under direction 2 of the Further Directions Order (3): outlines of evidence for the Appellant and for two lay "
     "witnesses, and the Appellant's schedule of medical documents relied upon with the documents at Tabs M1 to "
     "M9. The schedule states, for each document, what it is and is not relied upon for, and identifies at rows 1, "
     "4 and 7 the admitted facts to which the treating records correspond. No report has been prepared for the "
     "purposes of this proceeding.",B),

   P("5. Filing",HB),
   P("So that the record is complete, the Appellant will deliver to the Industrial Registry in person this week the "
     "Form 24 and Form 25 notices as served, the Respondent's responses, your letter of 8 September 2026 and "
     "Annexure A. If the Respondent objects to that course, please let me know by Friday 11 September 2026.",B),

   P("6. The documents not admitted",HB),
   P("The facts and documents not admitted are the subject of a separate request today.",B),

   P("Yours faithfully,",B), Spacer(1,1*mm), SIG(), Spacer(1,1*mm),
   P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented",B)]

buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=22*mm,rightMargin=22*mm,topMargin=12*mm,bottomMargin=12*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(22*mm,12*mm,A4[0]-44*mm,A4[1]-24*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/LETTER_TO_REGULATOR_re_8SEP_letter_9SEP2026.pdf"; pdf.save(out,linearize=True); print("built",out,n,"page(s)")
