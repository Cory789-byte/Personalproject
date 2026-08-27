#!/usr/bin/env python3
"""WC/2024/227 - MOCK RESPONSE to the second notice to admit facts.

What the Respondent's Senior Appeals Officer would return if the notice were
served as it now stands. Built by asking, for each fact: can this be denied,
and on what document?  INTERNAL - never served, never filed.
"""
import json, io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer, KeepTogether)

OUT = "out/FORM24_MOCK_RESPONSE.pdf"
F = json.load(open('/tmp/f185.json'))

OWN = ['R_REESE','R_FRMS','R_TAYLOR','R_PAY','CE','HR11']

def cls(f):
    s, t = f['s'], f['t']
    if s in OWN:                              return 'A','Own disclosure - List items 37-42.'
    if s.startswith('R_TAYLOR;'):              return 'A','Own disclosure - List item 39.'
    if s.startswith('Review Decision 69983'):  return 'A','The Respondent\'s own decision - List item 4.'
    if s.startswith('Respondent') and 'statement of facts' in s:
        if t.startswith('The Respondent does not allege') or t.startswith("The Respondent's amended statement"):
            return 'A*','True of the pleading. Admitting it closes the topic for good.'
        return 'A','The Respondent\'s own pleading.'
    if 'List of Documents' in s and 'item 25' in s: return 'A','Own List, item 25 names this very email.'
    if 'List of Documents' in s:               return 'A','The Respondent\'s own document.'
    if s.startswith('MASPER'):                 return 'A','Own List, item 27 names this email.'
    if s.startswith('Email of Ms C Taylor, 15 April'): return 'A','Own List, item 25.'
    if s.startswith('Email of Ms C Taylor, 27 September'): return 'A','Own List, item 37.'
    if s.startswith('Arithmetic'):             return 'A','Arithmetic on admitted numbers.'
    if s.startswith('Item 15 QH Leave'):       return 'A','MSH production under the NNPD - List item 43.'
    if 'Stressor 1(a) particulars bundle' in s and 'Tab 4' in s:
                                               return 'A','Served on the Respondent; also its own disclosure.'
    if s.startswith('The bundle'):             return 'A','Served on the Respondent 11 August 2026.'
    if s.startswith('Role description'):       return 'N','Employer document reaching the Appellant through the 2026 employment file. Not in the Respondent\'s List and never held by it.'
    if s.startswith('Email of Ms E Stibbard to the Switchboard team'): return 'A','Own disclosure - the FRMS pack (List items 37-42).'
    if s.startswith('Email of Ms E Stibbard'): return 'N','Not itemised in the Respondent\'s List. Provenance is the Appellant\'s own mailbox.'
    if s.startswith('Movement forms'):         return 'N','2026 employer document, post-dating the claim.'
    if s.startswith('Consultation'):           return 'N','Employer document, not in the Respondent\'s List.'
    if s.startswith('Email of Mr Heath Moran'):return 'N','Union document, not in the Respondent\'s List.'
    if s.startswith('Email of Ms L Forrest'):  return 'N','2026 employer document, post-dating the claim.'
    if s.startswith("Respondent's response to the Appellant's notice"):
                                               return 'A!','Already admitted by the Respondent on 18 February 2026. Cannot be withdrawn without leave.'
    if s.startswith('Affidavit'):              return 'A','Filed in the proceeding.'
    if 'disclosure in this proceeding' in s:   return 'A~','A statement about the Respondent\'s own disclosure; it can check it. Expect admission, possibly qualified "as at the date of this response".'
    if s.startswith("Respondent's disclosure - the Integrated"): return 'A','Own disclosure.'
    if s.startswith("Ms Taylor's email to Ms McNamee"): return 'A','Own disclosure - List item 39 names this email.'
    return 'A','Own disclosure.'

# Facts where a defensive officer has a real argument, and it must be met.
CONTESTED = {}
for f in F:
    t = f['t']
    if t.startswith('The Respondent does not allege that the Appellant was the subject of any warning'):
        CONTESTED[f['n']] = ('D?','Real risk. The Respondent may point to the 14 November 2023 email (SOFC 13(f)) and the 14 May 2024 12:08 pm email (SOFC 16(b)(ii)) and call them warnings.')
    if t.startswith("The Respondent's amended statement of facts and contentions does not identify the management action"):
        CONTESTED[f['n']] = ('D?','Real risk. Expect "the management action is identified throughout the statement" rather than a clean admission.')
    if t.startswith('The Respondent does not allege that agreement under clause 6.2'):
        CONTESTED[f['n']] = ('A*','True, but expect a submission that cl 6.2 governs roster changes and not the rostering of two shifts.')

for f in F:
    v, r = cls(f)
    if f['n'] in CONTESTED: v, r = CONTESTED[f['n']]
    f['v'], f['r'] = v, r
json.dump(F, open('/tmp/f185v.json','w'), indent=2)

LABEL = {'A!':'Admitted','A':'Admitted','A*':'Admitted','A~':'Admitted','N':'Not admitted','D?':'Denied (likely)'}
FILL  = {'A!':'#cfe9cf','A':'#e8f4e8','A*':'#e8f4e8','A~':'#e8f4e8','N':'#fdf3e0','D?':'#fbe4e4'}

H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=16, spaceAfter=3)
SUB = ParagraphStyle('SUB',fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=6)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10, leading=13,
                     spaceBefore=7, spaceAfter=3)
B   = ParagraphStyle('B',  fontName='Helvetica', fontSize=9, leading=12.3, spaceAfter=4)
C   = ParagraphStyle('C',  fontName='Helvetica', fontSize=7.7, leading=10.2)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
def P(t,s=C): return Paragraph(t,s)

st=[P("Mock response to the notice to admit facts",H1),
    P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; what the Senior Appeals Officer "
      "would return, and why &middot; <b>INTERNAL WORKING DOCUMENT - NOT FOR SERVICE OR FILING</b>",SUB)]

from collections import Counter
c=Counter(f['v'] for f in F)
adm = c['A']+c['A*']+c['A~']+c['A!']
st.append(P(f"<b>{adm} of {len(F)} facts admitted</b> ({adm*100//len(F)}%). "
            f"{c['N']} not admitted. {c['D?']} likely denied. The admissions are forced because the "
            "documents behind them are the Respondent's own decision, its own pleading, its own List of "
            "Documents, or the witness-conferencing and non-party disclosure it produced itself.",B))

rows=[[P("<b>No.</b>",CB),P("<b>Fact</b>",CB),P("<b>Response</b>",CB),P("<b>Why</b>",CB)]]
spans=[]; tint=[]
cursec=None
for f in F:
    if f['sec']!=cursec:
        cursec=f['sec']; spans.append(len(rows))
        rows.append([P(f"<b>{cursec}</b>",CB),P("",C),P("",C),P("",C)])
    tint.append((len(rows), f['v']))
    txt=f['t'] if len(f['t'])<=210 else f['t'][:207].rsplit(' ',1)[0]+'...'
    rows.append([P(str(f['n'])),P(txt),P(f"<b>{LABEL[f['v']]}</b>"),P(f['r'])])

t=Table(rows,colWidths=[9*mm,86*mm,20*mm,63*mm],repeatRows=1)
sty=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
     ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),
     ('VALIGN',(0,0),(-1,-1),'TOP'),
     ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
     ('TOPPADDING',(0,0),(-1,-1),2.6),('BOTTOMPADDING',(0,0),(-1,-1),2.6)]
for i in spans:
    sty+=[('BACKGROUND',(0,i),(-1,i),colors.HexColor('#c9c9c9')),('SPAN',(0,i),(-1,i))]
for i,v in tint:
    sty.append(('BACKGROUND',(2,i),(2,i),colors.HexColor(FILL[v])))
t.setStyle(TableStyle(sty))
st.append(t)

buf=io.BytesIO()
doc=BaseDocTemplate(buf,pagesize=(A4[1],A4[0]),leftMargin=11*mm,rightMargin=11*mm,
                    topMargin=11*mm,bottomMargin=11*mm)
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(11*mm,11*mm,A4[1]-22*mm,A4[0]-22*mm)])])
doc.build(st); buf.seek(0)
pdf=pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
print(f"built {OUT} - {len(F)} facts, {len(pdf.pages)} pages")
print(f"  admitted {adm} | not admitted {c['N']} | denied {c['D?']}")
