#!/usr/bin/env python3
"""Gmail forwarded-case-file ingest helpers (15 Sep 2026).

  python3 gmail_ingest.py manifest-add <json-file>   # append thread/message rows from a search_threads JSON dump
  python3 gmail_ingest.py write-msg <json-file>      # write one PLAIN_TEXT message JSON to messages/ + manifest
  python3 gmail_ingest.py raw-attach <raw-json> <outdir>  # extract attachments from a RAW MIME message JSON
  python3 gmail_ingest.py overlap                    # compare manifest against corpus/MESSAGE_INDEX.tsv
"""
import sys, json, os, re, base64, email, hashlib, csv, html
from email import policy
ROOT = os.path.join(os.path.dirname(__file__), '..')
ING = os.path.join(ROOT, 'documents', 'gmail-ingest-2026-09-15')
MAN = os.path.join(ING, 'MANIFEST.tsv')
COLS = ['gmail_msg_id','thread_id','fwd_date_utc','orig_sent','orig_from','orig_to','subject','size_est','folder','has_attachments','attachments','file']

def parse_snippet(sn):
    """Pull original From/Sent/To out of the forward preamble."""
    sn = html.unescape(sn or '')
    m = re.search(r'\((Inbox|Sent)\)', sn); folder = m.group(1) if m else ''
    f = re.search(r'From:\s*(.+?)\s+Sent:', sn); frm = f.group(1).strip() if f else ''
    s = re.search(r'Sent:\s*(.+?)\s+To:', sn); sent = s.group(1).strip() if s else ''
    t = re.search(r'To:\s*(.+)$', sn); to = t.group(1).strip()[:120] if t else ''
    return folder, frm, sent, to

def load_man():
    rows = {}
    if os.path.exists(MAN):
        with open(MAN) as fh:
            for r in csv.DictReader(fh, delimiter='\t'):
                rows[r['gmail_msg_id']] = r
    return rows

def save_man(rows):
    with open(MAN,'w') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter='\t'); w.writeheader()
        for r in sorted(rows.values(), key=lambda r: (r.get('orig_sent',''), r['gmail_msg_id'])):
            w.writerow({c: r.get(c,'') for c in COLS})

def manifest_add(path):
    data = json.load(open(path)); rows = load_man(); n=0
    for th in data.get('threads', []):
        for m in th.get('messages', []):
            mid = m['id']
            if mid in rows: continue
            folder, frm, sent, to = parse_snippet(m.get('snippet',''))
            rows[mid] = dict(gmail_msg_id=mid, thread_id=th['id'], fwd_date_utc=m.get('date',''),
                             orig_sent=sent, orig_from=frm, orig_to=to,
                             subject=html.unescape(m.get('subject','')).replace('\t',' '),
                             size_est=str(m.get('sizeEstimate','')), folder=folder,
                             has_attachments='FULL' if 'Full message and attachments' in html.unescape(m.get('snippet','')) else '',
                             attachments='', file=''); n+=1
    save_man(rows); print(f'manifest: +{n} → {len(rows)} rows')

def safe(s): return re.sub(r'[^A-Za-z0-9._-]+','_', s)[:90].strip('_')

BOILER = [r"\*{10,}.*?\*{10,}", r"_{10,}\nThis email \(including any attached files\).*?_{10,}",
          r"Queensland Health acknowledges the Traditional Custodians.*?(?=\n\n|$)",
          r"Metro South Health recognises and pays respect.*?(?=\n\n|$)",
          r"CAUTION: This email originated from outside of OIR\..*?content is safe\.",
          r"This email originated from outside Queensland Health\..*?content is safe\.",
          r"\[cid:[^\]]+\]", r"<https?://[^>]+>", r"<mailto:[^>]+>"]
def strip_boiler(t):
    for pat in BOILER: t = re.sub(pat, '', t, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", t).strip()

def write_thread(path):
    d = json.load(open(path))
    for m in d.get('messages', []):
        tmp = path + '.' + m['id'] + '.json'; json.dump(m, open(tmp,'w')); write_msg(tmp); os.remove(tmp)

def write_msg(path):
    m = json.load(open(path)); rows = load_man()
    mid = m['id']; body = strip_boiler(m.get('plaintextBody') or m.get('plaintext_body') or '')
    atts = m.get('attachments') or []
    att_desc = '; '.join(f"{a.get('filename','?')} ({a.get('mimeType','?')},{a.get('size','?')})" for a in atts)
    folder, frm, sent, to = parse_snippet(m.get('snippet',''))
    subj = html.unescape(m.get('subject','')).replace('FW: ','',1)
    fname = f"{safe(sent[:40]) or 'undated'}__{safe(subj)}__{mid}.txt"
    out = os.path.join(ING,'messages',fname)
    with open(out,'w') as fh:
        fh.write(f"GMAIL_ID: {mid}\nTHREAD: {m.get('threadId','')}\nFORWARDED: {m.get('date','')}\nORIG_FOLDER: {folder}\nORIG_FROM: {frm}\nORIG_SENT: {sent}\nORIG_TO: {to}\nSUBJECT: {subj}\nATTACHMENTS: {att_desc}\n{'='*78}\n{body}\n")
    r = rows.get(mid) or dict(gmail_msg_id=mid, thread_id=m.get('threadId',''), fwd_date_utc=m.get('date',''), size_est=str(m.get('sizeEstimate','')))
    r.update(dict(orig_sent=sent or r.get('orig_sent',''), orig_from=frm or r.get('orig_from',''), orig_to=to or r.get('orig_to',''), subject=subj, folder=folder or r.get('folder',''), attachments=att_desc, file=os.path.relpath(out, ROOT)))
    rows[mid]=r; save_man(rows); print('wrote', fname, '| attachments:', att_desc or '(none)')

def raw_attach(path, outdir):
    m = json.load(open(path)); raw = m.get('raw') or m.get('rawContent') or m.get('raw_content') or ''
    data = base64.urlsafe_b64decode(raw + '=' * (-len(raw) % 4))
    msg = email.message_from_bytes(data, policy=policy.default); os.makedirs(outdir, exist_ok=True); n=0
    body = msg.get_body(preferencelist=('plain',)); txt = body.get_content() if body else ''
    open(os.path.join(outdir,'_message.txt'),'w').write(f"Subject: {msg.get('Subject')}\nDate: {msg.get('Date')}\nFrom: {msg.get('From')}\nTo: {msg.get('To')}\n{'='*70}\n{strip_boiler(txt)}\n")
    for part in msg.walk():
        fn = part.get_filename()
        if fn and part.get_content_disposition() in ('attachment','inline', None) and not re.match(r'(?i)(image0\d+\.|ATT0\d+\.|.*\.gif$)', fn):
            payload = part.get_payload(decode=True)
            if not payload: continue
            h = hashlib.md5(payload).hexdigest()[:8]
            out = os.path.join(outdir, f"{safe(fn)}"); 
            if os.path.exists(out) and hashlib.md5(open(out,'rb').read()).hexdigest()[:8]!=h: out = out.replace('.', f'_{h}.',1)
            open(out,'wb').write(payload); n+=1; print('attachment:', out, len(payload), 'bytes md5', h)
    print(f'{n} attachments extracted')

def overlap():
    rows = load_man(); idx = os.path.join(ROOT,'corpus','MESSAGE_INDEX.tsv'); corpus=[]
    with open(idx) as fh:
        for r in csv.DictReader(fh, delimiter='\t'): corpus.append(r)
    def norm(s): return re.sub(r'\W+',' ', (s or '').lower().replace('fw:','').replace('re:','')).strip()[:60]
    csubj = {norm(r['subject']) for r in corpus}
    new = [r for r in rows.values() if norm(r['subject']) not in csubj]
    print(f'manifest {len(rows)} | corpus {len(corpus)} | subject-new {len(new)}')
    for r in sorted(new, key=lambda r: r['orig_sent']): print(f"  NEW  {r['orig_sent'][:32]:32s} {r['orig_from'][:34]:34s} {r['subject'][:70]}")

if __name__=='__main__':
    cmd = sys.argv[1]
    {'manifest-add':lambda: manifest_add(sys.argv[2]), 'write-msg':lambda: write_msg(sys.argv[2]),
     'raw-attach':lambda: raw_attach(sys.argv[2], sys.argv[3]), 'write-thread':lambda: write_thread(sys.argv[2]), 'overlap':overlap}[cmd]()
