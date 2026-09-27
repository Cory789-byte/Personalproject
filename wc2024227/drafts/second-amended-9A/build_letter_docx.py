"""Minimal dependency-free DOCX builder for the Registry letter (same content as build_letter.py)."""
import zipfile
from xml.sax.saxutils import escape
from letter_content import *
def E(s): return escape(s).replace('"','&quot;')
def run(t,bold=False,size=20):
    b='<w:b/>' if bold else ''
    return f'<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>{b}<w:sz w:val="{size}"/></w:rPr><w:t xml:space="preserve">{E(t)}</w:t></w:r>'
def para(text,bold_lead='',bold=False,after=100,indent=0):
    ind=f'<w:ind w:left="{indent}"/>' if indent else ''
    lead=run(bold_lead+' ',True) if bold_lead else ''
    return f'<w:p><w:pPr><w:spacing w:after="{after}"/>{ind}</w:pPr>{lead}{run(text,bold)}</w:p>'
body=[para(DATE)]+[para(l,after=0) for l in TO]+[para(''),para(CC),para(TITLE,bold=True),para(SUBJECT,bold=True)]
for b,t in BODY: body.append(para(t,bold_lead=b))
for l in CLOSE: body.append(para(l))
body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
body.append(para(SCHEDULE_TITLE,bold=True))
for h,items in SCHEDULE:
    body.append(para(h,bold=True,after=40))
    for it in items: body.append(para('Tab '+it,after=20,indent=284))
body.append(para('')); body.append(para('Enclosure: Second Amended Statement of Facts and Contentions (Form 9A), 19 pages.'))
doc=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>{''.join(body)}<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1000" w:right="1000" w:bottom="900" w:left="1000" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr></w:body></w:document>'''
ct='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'''
rels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'''
out='2026-10_LETTER_to_Registry_leave_to_amend_and_documents.docx'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml',ct); z.writestr('_rels/.rels',rels); z.writestr('word/document.xml',doc)
print('docx built',out)
