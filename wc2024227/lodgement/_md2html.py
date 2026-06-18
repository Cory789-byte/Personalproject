#!/usr/bin/env python3
"""Minimal Markdown -> HTML for the WC/2024/227 lodgement docs.
Handles: headings, bold/italic, blockquotes, hr, pipe tables,
ordered/unordered lists (with 4-space nested bullets)."""
import re, sys, html

def inline(t):
    t = html.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)', r'<em>\1</em>', t)
    return t

def render(md):
    lines = md.split('\n')
    out, i = [], 0
    n = len(lines)
    pending_cols = None
    pending_break = False
    while i < n:
        ln = lines[i]
        # column-width hint for the next table, e.g. <!--cols:6,28,16,26,24-->
        mcols = re.match(r'^\s*<!--\s*cols:\s*([\d,\s.]+)\s*-->\s*$', ln)
        if mcols:
            pending_cols = [w.strip() for w in mcols.group(1).split(',') if w.strip()]
            i += 1; continue
        # forced page break — applied to the next block element
        if re.match(r'^\[newpage\]\s*$', ln):
            pending_break = True; i += 1; continue
        # table block
        if ln.strip().startswith('|') and i+1 < n and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i+1]):
            header = [c.strip() for c in ln.strip().strip('|').split('|')]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            ncol = len(header)
            widths = pending_cols if (pending_cols and len(pending_cols) == ncol) else None
            pending_cols = None
            if widths is None:
                widths = ['6', '28', '16', '26', '24'] if ncol == 5 else [str(round(100 / ncol, 2))] * ncol
            colgroup = '<colgroup>' + ''.join(f'<col style="width:{w}%">' for w in widths) + '</colgroup>'
            out.append('<table>' + colgroup + '<thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in header) + '</tr></thead><tbody>')
            for r in rows:
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            out.append('</tbody></table>')
            continue
        # headings
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            lvl = len(m.group(1))
            brk = ' style="page-break-before:always"' if pending_break else ''
            pending_break = False
            out.append(f'<h{lvl}{brk}>{inline(m.group(2))}</h{lvl}>'); i += 1; continue
        # hr
        if re.match(r'^---+\s*$', ln):
            out.append('<hr>'); i += 1; continue
        # blockquote
        if ln.strip().startswith('>'):
            buf = []
            while i < n and lines[i].strip().startswith('>'):
                buf.append(inline(re.sub(r'^\s*>\s?', '', lines[i]))); i += 1
            out.append('<blockquote>' + '<br>'.join(buf) + '</blockquote>'); continue
        # numbered paragraph — preserve the LITERAL number (legal affidavit / grounds
        # paragraphs must keep their authored numbers; do NOT auto-renumber via <ol>)
        m2 = re.match(r'^(\d+[A-Z]?)\.\s+(.*)$', ln)
        if m2:
            num, item = m2.group(1), m2.group(2)
            i += 1
            sub = []
            while i < n and re.match(r'^\s{2,}[-*]\s+', lines[i]):
                sub.append(inline(re.sub(r'^\s+[-*]\s+', '', lines[i]))); i += 1
            out.append(f'<p class="num"><span class="n">{num}.</span> {inline(item)}</p>')
            if sub:
                out.append('<ul class="sub">' + ''.join(f'<li>{s}</li>' for s in sub) + '</ul>')
            continue
        # unordered list
        if re.match(r'^[-*]\s+', ln):
            out.append('<ul>')
            while i < n and re.match(r'^[-*]\s+', lines[i]):
                txt = re.sub(r'^[-*]\s+', '', lines[i])
                out.append('<li>' + inline(txt) + '</li>'); i += 1
            out.append('</ul>'); continue
        # blank
        if ln.strip() == '':
            i += 1; continue
        # paragraph (gather until blank)
        buf = [ln]; i += 1
        while i < n and lines[i].strip() != '' and not re.match(r'^(#{1,6}\s|>|---+\s*$|\d+[A-Z]?\.\s|[-*]\s|\|)', lines[i]):
            buf.append(lines[i]); i += 1
        out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)

CSS = """
@page { size: A4; margin: 2cm 2cm; }
body { font-family: 'Liberation Serif','Times New Roman',serif; font-size: 11pt; line-height: 1.3; color:#000; }
h1 { font-size: 14pt; text-align:center; border-bottom:2px solid #000; padding-bottom:4pt; }
h2 { font-size: 12.5pt; border-bottom:1px solid #888; padding-bottom:2pt; margin-top:12pt; margin-bottom:4pt; }
h3 { font-size: 11pt; margin-top:9pt; margin-bottom:3pt; }
p, li { text-align: justify; }
blockquote { border-left:3px solid #999; margin:6pt 0; padding:4pt 10pt; background:#f4f4f4; font-size:10pt; }
hr { border:0; border-top:1px solid #000; margin:9pt 0; }
table { border-collapse: collapse; width:100%; font-size:8.5pt; margin:6pt 0; border:1.5pt solid #000; table-layout: fixed; }
th, td { border:0.75pt solid #000; padding:3pt 5pt; vertical-align:top; text-align:left; word-wrap:break-word; overflow-wrap:break-word; line-height:1.2; }
th { background:#e8e8e8; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
ol, ul { margin:4pt 0; padding-left:20pt; }
li { margin-bottom:2.5pt; }
strong { font-weight:bold; }
p.num { margin:4pt 0; padding-left:2.2em; text-indent:-2.2em; text-align:justify; }
p.num .n { font-weight:bold; }
ul.sub { margin:2pt 0 4pt 0; }
.newpage { page-break-before: always; }
.sig { margin-top:14pt; }
"""

src, dst = sys.argv[1], sys.argv[2]
md = open(src, encoding='utf-8').read()
body = render(md)
doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
open(dst, 'w', encoding='utf-8').write(doc)
print('wrote', dst)
