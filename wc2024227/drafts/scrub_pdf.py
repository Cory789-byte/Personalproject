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
    for k in ('/Metadata', '/PieceInfo', '/Lang', '/StructTreeRoot', '/MarkInfo',
              '/Threads', '/AcroForm', '/OpenAction', '/AA', '/SpiderInfo'):
        if k in pdf.Root:
            del pdf.Root[k]
    if '/Names' in pdf.Root and '/EmbeddedFiles' in pdf.Root.Names:
        del pdf.Root.Names['/EmbeddedFiles']
    # images carrying their own embedded XMP/EXIF (e.g. JPEGs from design tools): re-encode
    # the pixels without metadata; dimensions, colour space and bit depth are preserved.
    removed += strip_image_metadata(pdf)
    return removed

def strip_image_metadata(pdf):
    import io
    n = 0
    seen = set()
    for pg in pdf.pages:
        res = pg.obj.get('/Resources')
        xo = res.get('/XObject') if res is not None else None
        if xo is None:
            continue
        for name in list(xo.keys()):
            x = xo[name]
            if x.get('/Subtype') != '/Image' or x.objgen in seen:
                continue
            seen.add(x.objgen)
            try:
                raw = x.read_raw_bytes()
            except Exception:
                continue
            if b'xmpmeta' not in raw and b'Exif' not in raw and b'xpacket' not in raw:
                continue
            from PIL import Image
            try:
                im = pikepdf.PdfImage(x).as_pil_image()
            except Exception:
                continue
            buf = io.BytesIO()
            if str(x.get('/Filter')) == '/DCTDecode':
                im.save(buf, format='JPEG', quality=95, optimize=True)
                x.write(buf.getvalue(), filter=pikepdf.Name('/DCTDecode'))
            else:
                im.save(buf, format='PNG')
                x.write(buf.getvalue(), filter=pikepdf.Name('/FlateDecode'))
            for k in ('/DecodeParms', '/Metadata'):
                if k in x:
                    del x[k]
            n += 1
    return n

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
