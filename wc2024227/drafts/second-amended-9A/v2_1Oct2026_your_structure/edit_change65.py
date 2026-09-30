import zipfile,re,shutil,os
F='2026-10_LETTER_to_Registry_FINAL.docx'
z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
x=dict((i.filename,d) for i,d in items)['word/document.xml'].decode()
def txt(p): return ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p))
ps=re.findall(r'<w:p[ >].*?</w:p>',x,re.S)
def find(start):
    m=[p for p in ps if txt(p).startswith(start)]; assert len(m)==1,(start,len(m)); return m[0]
PPR='<w:pPr><w:spacing w:before="0" w:after="80" w:line="264" w:lineRule="auto"/></w:pPr>'
RB='<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
RN='<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b w:val="0"/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
def para(label,body):
    return f'<w:p>{PPR}<w:r>{RB}<w:t xml:space="preserve">{label}</w:t></w:r><w:r>{RN}<w:t xml:space="preserve">{body}</w:t></w:r></w:p>'
def sub(old,new):
    global x; assert x.count(old)==1; x=x.replace(old,new)
# 1 application
sub(find('The application, and what the amendment does.'), para('The application. ',
 "The Appellant was an Administration Officer on the Logan Hospital Switchboard; the Respondent admits that maintaining accurate contact details for medical staff is a critical function of the Switchboard to ensure effective clinical handover and patient safety (fact 289). "
 "The Appellant applies for leave to file and serve the enclosed Second Amended Statement of Facts and Contentions (Form 9A), under section 451(2) of the Industrial Relations Act 2016. A copy goes to the Respondent with this letter, and its consent is sought. "
 "Since the Amended Form 9A of 7 April 2026, the Respondent has admitted 298 of the 303 facts in the Appellant's notice of 28 August 2026, and has admitted or since confirmed 29 of the 39 documents behind them. "
 "The amendment accepts that the onus of proof is on the Appellant, withdraws the descriptions of conduct used in the earlier pleading, and adds no new stressor or allegation. "
 "No hearing date has been set, so the amendment is sought before either party prepares for hearing on the earlier pleading. The Appellant does not oppose the Respondent having time to amend its own statement of facts and contentions."))
# 2,3,4 delete
for s in ['The matter, in summary.','The Respondent\'s evidence.','Where the Appellant stands.']:
    sub(find(s),'')
# 5 point (3)
old='(3) It has named no medical or expert witness and served no expert report.'
assert x.count(old)==1
x=x.replace(old,'(3) It has named no medical or expert witness and served no expert report: its list of 24 September 2026 names four witnesses, Ms Taylor, Ms Reese, Ms Wright and Ms Earl, described as "lay" witnesses, and it served outlines of their evidence.')
# 6 record: drop duplicate "will proceed" sentence (kept in the closing paragraph)
old=' The Appellant will proceed on whatever orders and directions the Commissioner gives on this application, on the documents, and on the further conduct of the appeal.'
assert x.count(old)==1; x=x.replace(old,'')
# 7 Part 1 note
p=find('The Appellant asked the Respondent on 9 September 2026')
old=txt(p); assert p.count(old)==1
new=("The Appellant asked the Respondent on 9 September 2026 to confirm the ten outstanding documents; the Respondent's email of 23 September 2026 gives no date by which the copies are expected. "
 "The copies of Tabs 1, 5, 17 to 19, 21 to 24 and 31 came from the Appellant's own records; Tabs 17 to 19, 22 and 23 bear the signature of the employer's Director, Corporate Services. "
 "Tab 24 is a Together Queensland document, which the email of 23 September 2026 does not address.")
sub(p,p.replace(old,new))
out=F+'.tmp'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as w:
    for i,d in items: w.writestr(i, x.encode() if i.filename=='word/document.xml' else d)
os.replace(out,F); print('ok')
