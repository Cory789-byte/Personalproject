#!/usr/bin/env python3
"""WC/2024/227 - letter to the Regulator of 13 September 2026: agreeing to the extension to
25 September 2026 and recording the position on the fourteen disputed tabs. Metadata stripped.

⚠ PARAGRAPH 5 embodies a decision: it foreshadows service of the Second Amended Form 9A.
   Set FORESHADOW=0 to build without it."""
import io, os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.platypus import Image as RLImage

FORESHADOW = os.environ.get('FORESHADOW','1') != '0'
B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.0, leading=11.4, spaceAfter=3.5)
HB = ParagraphStyle('HB', parent=B, fontName='Helvetica-Bold', spaceAfter=2)
SM = ParagraphStyle('SM', parent=B, fontSize=8.3, leading=10.4, leftIndent=5*mm, spaceAfter=2)
def P(t,s=B): return Paragraph(t,s)
def SIG():
    i=RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); i.hAlign='LEFT'; return i

s=[P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com",B),
   Spacer(1,2*mm),
   P("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>"
     "150 Mary Street, Brisbane QLD 4000<br/>By email: Renee.Matheson@oir.qld.gov.au",B),
   Spacer(1,2*mm),
   P("Dated 13 September 2026",B),
   Spacer(1,2*mm),
   P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
     "<b>Your email of 10 September 2026 &ndash; extension to 25 September 2026</b>",B),
   Spacer(1,1*mm),
   P("Dear Ms Matheson,",B),

   P("1. The extension is agreed",HB),
   P("Thank you for your email of 10 September 2026. The extension to <b>Friday 25 September 2026</b> is agreed, "
     "without qualification. I am sorry to have set a date that fell in a hearing week.",B),

   P("2. The request offers an alternative that requires no document",HB),
   P("For each item the request offers two courses: produce a copy, <i>or</i> admit the authenticity of the copy "
     "served under rule 49. The second requires no document to be obtained from anyone. The contents of every "
     "document in the schedule other than Tab 31 are already admitted in the Respondent's response of "
     "8 September 2026, at the facts noted against each tab.",B),

   P("3. Why the copies served are copies from my records",HB),
   P("The response records the ground of dispute as the source of the copy. So that the position is clear, and not "
     "by way of any complaint: each of those documents is in my records because Metro South Health or its officers "
     "sent it to me, and the Respondent has admitted the sending. Taking the schedule in order:",B),
   P("Tab 1 &ndash; the role description &ndash; was served on me by Metro South Health as Attachment 2 to the "
     "Request for Medical Information of 31 July 2026; its contents are admitted at facts 1 to 13. "
     "Tab 5 was sent to me (facts 36 to 38). "
     "Tab 6 was sent to Logan Switch and copied to Switchboard staff including me (fact 49). "
     "Tabs 17 to 19 are Metro South Health's own movement forms recording changes to my hours, each approved by "
     "Mr Hughes as delegate (facts 14 and 15). "
     "Tab 21 was written to me by Ms Forrest (fact 224). "
     "Tabs 22 and 23 were released to affected staff for consultation, of whom I was one (facts 169 to 176). "
     "Tab 30 was sent to Logan Switch and copied to Switchboard staff including me (fact 71). "
     "Tab 30A was sent to Logan Switch (facts 85 to 87).", SM),

   P("4. Three items that may not require any enquiry of Metro South Health",HB),
   P("If it assists, three of the documents may be capable of being dealt with separately, and sooner, without any "
     "enquiry of Metro South Health:",B),
   P("<b>Tab 6</b> &ndash; the Respondent's amended List of Documents of 14 August 2026 lists at item 25 an "
     "attachment described as \"Email: After hours on call process\". That is this document (fact 277).<br/>"
     "<b>Tab 20</b> &ndash; Metro South Health's letter of 5 June 2026 is addressed to Commissioner Dwyer and is "
     "on the Commission's file (facts 263 to 268).<br/>"
     "<b>Tab 30</b> &ndash; Review Decision 69983 records and quotes this email (fact 70).", SM),
   P("Only Tab 31 appears to require a copy held by Metro South Health, and the request in respect of that tab is "
     "for the spreadsheet of recorded MET calls for 17 to 18 March 2024 that Metro South Health has said is "
     "available (fact 268).",B),

   P("5. Nothing further is reserved",HB),
   P("This letter adds no reservation. The position set out in my letters of 9 September 2026 is unchanged, and I "
     "raise the matters above only so that the record is complete.",B),
]
if FORESHADOW:
    s += [P("6. The Appellant's statement of facts and contentions",HB),
          P("So that the Respondent is not taken by surprise before its material is due on 30 September 2026, I "
            "give notice that I propose to serve a Second Amended Statement of Facts and Contentions shortly. It "
            "pleads the same case on the same events; the substance of the amendment is that the matters "
            "previously pleaded are now particularised to the paragraphs admitted on 8 September 2026, and that "
            "characterisation has been removed throughout. I will seek the leave the Commission requires in the "
            "ordinary way. If the Respondent wishes to be heard as to the timing, please let me know.",B)]
s += [P("Yours faithfully,",B), Spacer(1,1*mm), SIG(), Spacer(1,1*mm),
      P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented",B)]

buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=22*mm,rightMargin=22*mm,topMargin=12*mm,bottomMargin=12*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(22*mm,12*mm,A4[0]-44*mm,A4[1]-24*mm,
                    leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/LETTER_TO_REGULATOR_extension_agreed_13SEP2026.pdf"
pdf.save(out,linearize=True); print("built",out,n,"page(s)")
