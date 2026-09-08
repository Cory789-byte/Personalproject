import pikepdf
notice=pikepdf.open('out/NOTICE_OF_DISPUTE_STAGE2_to_CE_3SEP2026.pdf')
record=pikepdf.open('out/EMPLOYMENT_RECORD_analysis_chronology_originals_3SEP2026.pdf')
out=pikepdf.new()
out.pages.extend(notice.pages)
out.pages.extend(record.pages)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
if '/Names' in r and '/EmbeddedFiles' in r.Names: del r.Names['/EmbeddedFiles']
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/STAGE2_TO_CHIEF_EXECUTIVE_notice_and_full_record_3SEP2026.pdf',fix_metadata_version=False)
print('notice',len(notice.pages),'+ record',len(record.pages),'= TOTAL',len(out.pages))
