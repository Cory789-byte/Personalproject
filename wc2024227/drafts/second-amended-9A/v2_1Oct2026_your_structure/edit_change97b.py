exec(open('edit_change95.py').read())
import re
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
d.rep("Before the escalation the Respondent alleges no response to the Service, and in that time it alleges no amendment of the document, and no notice to the staff of the change made to it on 22 February 2024.",
      "The Respondent alleges no response to the Service before the escalation, and no amendment of the document, or notice to the staff of the change made to it on 22 February 2024, on or before 20 May 2024.")
# 5.3 bold split
old='5.3 As to the office hours. That the Manager stated fixed office hours to the Switchboard staff</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:t xml:space="preserve"> at any time'
new='5.3 As to the office hours. </w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:t xml:space="preserve">That the Manager stated fixed office hours to the Switchboard staff at any time'
assert d.x.count(old)==1; d.x=d.x.replace(old,new)
# signature name paragraph: last paragraph whose text is exactly 'Cory Lea Shepherd'
T=lambda p:''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p))
ps=[p for p in d.paras() if T(p).strip()=='Cory Lea Shepherd']
print('sig paras',len(ps)); p=ps[-1]; print(p[:400])
np_=re.sub(r'<w:jc w:val="both"/>','<w:jc w:val="left"/>',p) if '<w:jc w:val="both"/>' in p else p.replace('<w:pPr>','<w:pPr><w:jc w:val="left"/>',1)
d.x=d.x.replace(p,np_,1)
d.save(); print('ok')
