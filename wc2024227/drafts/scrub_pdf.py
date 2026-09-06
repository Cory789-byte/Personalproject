#!/usr/bin/env python3
"""Scrub a PDF for service: remove all annotations (including third-party markup carrying
author names and timestamps), document and page metadata, and embedded files.
Usage: python3 scrub_pdf.py FILE [FILE...]"""
import sys, pikepdf

def scrub(pdf):
    removed = 0
    for pg in pdf.pages:
        if '/Annots' in pg.obj:
            removed += len(pg.obj['/Annots'])
            del pg.obj['/Annots']
        for k in ('/Metadata', '/PieceInfo', '/LastModified', '/StructParents', '/Tabs', '/B', '/Trans', '/AA'):
            if k in pg.obj:
                del pg.obj[k]
    try:
        with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
            m.clear()
    except Exception:
        pass
    for k in list(pdf.docinfo.keys()):
        del pdf.docinfo[k]
    for k in ('/Metadata', '/PieceInfo', '/Lang', '/Outlines', '/StructTreeRoot', '/MarkInfo',
              '/Threads', '/AcroForm', '/OpenAction', '/AA', '/SpiderInfo'):
        if k in pdf.Root:
            del pdf.Root[k]
    if '/Names' in pdf.Root and '/EmbeddedFiles' in pdf.Root.Names:
        del pdf.Root.Names['/EmbeddedFiles']
    return removed

def scrub_file(path):
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    n = scrub(pdf)
    # linearize forces a full rewrite, which drops objects no longer referenced
    # (e.g. structure-tree nodes orphaned by deleting /StructTreeRoot)
    pdf.save(path, fix_metadata_version=False, linearize=True)
    return n

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'{path}: removed {scrub_file(path)} annotation(s)')
