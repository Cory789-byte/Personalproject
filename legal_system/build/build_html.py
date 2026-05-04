"""Generate a static, deep-linkable HTML site from case.db.

Output layout under legal_system/output/site/:
    index.html               — top-level dashboard + navigation
    timeline.html            — master chronology (all phases combined)
    phases/<id>.html         — per-phase pages (Phase 0.5 ... Phase 10)
    events/<id>.html         — per-event pages
    charges/<id>.html        — per-charge pages
    elements.html            — element-by-element table for every charge
    statements/<id>.html     — witness-statement pages
    paragraphs/<id>.html     — per-statement-paragraph pages
    actors/<id>.html         — actor cards
    evidence/<id>.html       — evidence anchor cards
    evidence/index.html      — full searchable evidence ledger
    corrections.html         — speaker correction register
    quote_diff.html          — submission-quote drift report (filterable)
    iterations.html          — three-iteration field-changes table
    ware.html                — Ware schedule (33 items)
    validation.html          — internal validation findings
    lockout_night.html       — 14-row lockout-night card
    cite/<id>.txt            — citation-string snippets ready to paste

Every entity has a stable URL fragment, so submissions can deep-link with
e.g. file://.../events/lockout-row-09.html or
http://.../events/lockout-row-09.html.

Run:
    python -m legal_system.build.build_html
"""
from __future__ import annotations

import html
import json
import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DB_PATH = ROOT / "legal_system" / "db" / "case.db"
OUT_DIR = ROOT / "legal_system" / "output" / "site"
SRC_DIR = ROOT / "source_documents"


def _deterministic_timestamp() -> str:
    """Return a generation timestamp tied to source-document mtimes so the
    generator is idempotent — re-running on unchanged inputs yields
    byte-identical HTML and git stays clean."""
    if SRC_DIR.exists():
        mtimes = [p.stat().st_mtime for p in SRC_DIR.iterdir() if p.is_file()]
        if mtimes:
            return datetime.utcfromtimestamp(max(mtimes)).strftime("%Y-%m-%d %H:%M UTC")
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")


GENERATED_AT = _deterministic_timestamp()


# ---------------------------------------------------------------------------
# HTML scaffolding
# ---------------------------------------------------------------------------

CSS = """
:root {
  --bg:#0e1116; --panel:#161b22; --panel2:#1c232c; --fg:#e6edf3;
  --muted:#8b949e; --accent:#7ee787; --warn:#f0883e; --danger:#ff7b72;
  --link:#58a6ff; --border:#30363d;
  --mono: 'SFMono-Regular','Consolas','Liberation Mono','Menlo','monospace';
  --sans: 'Inter','SF Pro Display','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','sans-serif';
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);line-height:1.45}
a{color:var(--link);text-decoration:none}
a:hover{text-decoration:underline}
header.topbar{position:sticky;top:0;background:var(--panel);border-bottom:1px solid var(--border);padding:.6rem 1rem;z-index:5;display:flex;gap:1rem;align-items:center;flex-wrap:wrap}
header.topbar .brand{font-weight:700;color:var(--accent)}
header.topbar nav a{margin-right:.6rem;font-size:.92rem;color:var(--muted)}
header.topbar nav a:hover{color:var(--fg)}
main{max-width:1280px;margin:0 auto;padding:1.4rem 1.2rem 4rem}
h1,h2,h3,h4{font-weight:600;letter-spacing:-0.01em}
h1{margin:.6rem 0 .8rem;font-size:1.6rem}
h2{margin:1.6rem 0 .6rem;font-size:1.25rem;border-bottom:1px solid var(--border);padding-bottom:.3rem}
h3{margin:1.1rem 0 .4rem;font-size:1.05rem;color:var(--accent)}
.muted{color:var(--muted)}
.tag{display:inline-block;padding:.06rem .42rem;border-radius:8px;font-size:.7rem;background:var(--panel2);border:1px solid var(--border);color:var(--muted);margin-right:.25rem}
.tag.ok{color:var(--accent);border-color:var(--accent)}
.tag.warn{color:var(--warn);border-color:var(--warn)}
.tag.danger{color:var(--danger);border-color:var(--danger)}
.tag.info{color:var(--link);border-color:var(--link)}
table{width:100%;border-collapse:collapse;font-size:.92rem;margin:.4rem 0 1rem}
th,td{padding:.45rem .6rem;border-bottom:1px solid var(--border);vertical-align:top;text-align:left}
th{color:var(--muted);font-weight:600;background:var(--panel)}
tr:hover td{background:#1a2330}
tr.row-dispositive td{background:#1a2a1a}
tr.row-disputed td{background:#2a1a1a}
.card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:.9rem 1rem;margin:.6rem 0}
.card.bordered{border-left:3px solid var(--accent)}
.card.bordered.warn{border-left-color:var(--warn)}
.card.bordered.danger{border-left-color:var(--danger)}
.card.bordered.info{border-left-color:var(--link)}
.kv{display:grid;grid-template-columns:max-content 1fr;gap:.2rem 1rem;font-size:.92rem;margin:.4rem 0}
.kv .k{color:var(--muted)}
blockquote{border-left:3px solid var(--accent);padding:.4rem .8rem;margin:.4rem 0;color:#dbe1e6;background:var(--panel2)}
code{font-family:var(--mono);background:var(--panel2);padding:.05rem .35rem;border-radius:4px;font-size:.86rem}
pre{font-family:var(--mono);background:var(--panel2);padding:.7rem .9rem;border-radius:8px;overflow-x:auto}
ul,ol{padding-left:1.4rem}
.grid{display:grid;gap:1rem}
.grid.cols-2{grid-template-columns:1fr 1fr}
.grid.cols-3{grid-template-columns:repeat(3,1fr)}
.grid.cols-4{grid-template-columns:repeat(4,1fr)}
@media (max-width:900px){.grid.cols-2,.grid.cols-3,.grid.cols-4{grid-template-columns:1fr}}
.search-box{width:100%;max-width:540px;padding:.5rem .7rem;background:var(--panel2);border:1px solid var(--border);color:var(--fg);border-radius:6px;font-family:var(--sans);font-size:.95rem}
details{margin:.4rem 0}
summary{cursor:pointer;color:var(--link)}
.banner{background:#3a2f10;border:1px solid var(--warn);color:#f0c584;padding:.7rem 1rem;border-radius:8px;margin:1rem 0;font-size:.92rem}
.copy{cursor:pointer;font-size:.78rem;color:var(--muted)}
.copy:hover{color:var(--accent)}
.crumbs{font-size:.85rem;margin:.2rem 0 .8rem}
.crumbs a{color:var(--muted)}
.status-badge{display:inline-block;padding:.1rem .5rem;border-radius:6px;font-size:.78rem;font-weight:600}
.status-disputed{background:#3a1a1a;color:#ff9b9b;border:1px solid #ff7b72}
.status-agreed{background:#1a3a1a;color:#9bff9b;border:1px solid #7ee787}
.status-partial{background:#3a2f10;color:#f0c584;border:1px solid var(--warn)}
.status-dispositive{background:#0d2640;color:#9bd0ff;border:1px solid var(--link);font-weight:700}
"""

JS_SEARCH = """
function tableSearch(tableId, inputId){
  const inp=document.getElementById(inputId);
  if(!inp)return;
  inp.addEventListener('input',()=>{
    const q=inp.value.toLowerCase().trim();
    const tbl=document.getElementById(tableId);
    if(!tbl)return;
    [...tbl.tBodies[0].rows].forEach(r=>{
      r.style.display = r.innerText.toLowerCase().includes(q) ? '' : 'none';
    });
  });
}
function copyText(t){navigator.clipboard.writeText(t);}
"""


def _esc(s) -> str:
    return html.escape(str(s) if s is not None else "")


def _href(rel: str) -> str:
    """Relative href — site is fully relative, so depth-aware."""
    return rel


def _depth_prefix(out_path: Path) -> str:
    """Return '../' * (depth from site root) for relative links from this page."""
    rel = out_path.relative_to(OUT_DIR)
    depth = len(rel.parts) - 1
    return "../" * depth


def _page(title: str, body_html: str, out_path: Path, *, breadcrumb: list[tuple[str, str]] | None = None) -> None:
    """Write a page. breadcrumb is list of (label, href_relative_to_site_root)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = _depth_prefix(out_path)
    nav = [
        ("Index", "index.html"),
        ("Timeline", "timeline.html"),
        ("Charges", "charges/index.html"),
        ("Lockout night", "lockout_night.html"),
        ("Statements", "statements/index.html"),
        ("Evidence", "evidence/index.html"),
        ("Corrections", "corrections.html"),
        ("Quote diff", "quote_diff.html"),
        ("Iterations", "iterations.html"),
        ("Ware schedule", "ware.html"),
        ("Validation", "validation.html"),
        ("Actors", "actors/index.html"),
    ]
    nav_html = "".join(f'<a href="{prefix}{href}">{_esc(label)}</a>' for label, href in nav)
    crumbs_html = ""
    if breadcrumb:
        crumbs_html = '<div class="crumbs">' + " &raquo; ".join(
            f'<a href="{prefix}{h}">{_esc(l)}</a>' if h else _esc(l)
            for l, h in breadcrumb
        ) + "</div>"

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{_esc(title)} — Shepherd v QPS</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
</head>
<body>
<header class="topbar">
  <span class="brand">Shepherd v QPS</span>
  <nav>{nav_html}</nav>
</header>
<main>
{crumbs_html}
{body_html}
<footer class="muted" style="margin-top:3rem;border-top:1px solid var(--border);padding-top:1rem;font-size:.8rem">
  Generated {GENERATED_AT} from <code>case.db</code>.
  Built by <code>legal_system/build/build_html.py</code> over the 7 ingested source documents.
</footer>
</main>
<script>{JS_SEARCH}</script>
</body>
</html>
"""
    out_path.write_text(html_doc, encoding="utf-8")


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------

def build_index(conn: sqlite3.Connection):
    cur = conn.cursor()
    counts = {}
    for table in (
        "events", "evidence", "actors", "charges", "charge_failures",
        "corrections", "quote_diffs", "statements", "statement_paragraphs",
        "iteration_field_changes", "ware_schedule", "validation_findings",
    ):
        counts[table] = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]

    outstanding = cur.execute(
        "SELECT COUNT(*) FROM ware_schedule WHERE current_status LIKE '%OUTSTANDING%'"
    ).fetchone()[0]
    drift_quotes = cur.execute(
        "SELECT COUNT(*) FROM quote_diffs WHERE bucket='drift'"
    ).fetchone()[0]

    body = f"""
<h1>Shepherd v QPS — Evidence Management System</h1>
<div class="banner">
  <strong>Disclaimer.</strong> This site is an internal navigation aid built from the 7 ingested source
  documents (auto-generated case-file artefacts). It does <em>not</em> constitute legal advice.
  Cory Shepherd is self-represented; for the QHRC conciliation on 14 May 2026 and any continuing
  prosecution, retain a Queensland-admitted lawyer (LawRight, Caxton, or counsel of choice).
</div>

<div class="grid cols-4">
  <a class="card bordered" href="timeline.html">
    <h3>Timeline</h3>
    <p class="muted">{counts['events']} events across 12 phases</p>
  </a>
  <a class="card bordered danger" href="charges/index.html">
    <h3>Charges</h3>
    <p class="muted">{counts['charges']} charges · {counts['charge_failures']} per-element failures</p>
  </a>
  <a class="card bordered warn" href="ware.html">
    <h3>Ware schedule</h3>
    <p class="muted">{counts['ware_schedule']} items · <strong style="color:var(--warn)">{outstanding} OUTSTANDING</strong></p>
  </a>
  <a class="card bordered info" href="iterations.html">
    <h3>Iteration changes</h3>
    <p class="muted">{counts['iteration_field_changes']} field changes across 3 iterations</p>
  </a>
  <a class="card bordered" href="evidence/index.html">
    <h3>Evidence ledger</h3>
    <p class="muted">{counts['evidence']} anchor refs</p>
  </a>
  <a class="card bordered" href="statements/index.html">
    <h3>Witness paragraphs</h3>
    <p class="muted">{counts['statement_paragraphs']} paragraphs across {counts['statements']} statements</p>
  </a>
  <a class="card bordered info" href="corrections.html">
    <h3>Speaker corrections</h3>
    <p class="muted">{counts['corrections']} entries</p>
  </a>
  <a class="card bordered warn" href="quote_diff.html">
    <h3>Submission quote drift</h3>
    <p class="muted">{counts['quote_diffs']} quotes · <strong style="color:var(--warn)">{drift_quotes} drifted</strong></p>
  </a>
  <a class="card bordered" href="actors/index.html">
    <h3>Actor catalogue</h3>
    <p class="muted">{counts['actors']} people / agencies</p>
  </a>
  <a class="card bordered" href="lockout_night.html">
    <h3>Lockout-night card</h3>
    <p class="muted">14-row chronological exhibit</p>
  </a>
  <a class="card bordered danger" href="validation.html">
    <h3>Validation</h3>
    <p class="muted">{counts['validation_findings']} cross-doc findings</p>
  </a>
  <a class="card bordered" href="phases/index.html">
    <h3>Phases</h3>
    <p class="muted">12 chronological compartments</p>
  </a>
</div>

<h2>How to cite</h2>
<p>Every page has a stable URL fragment. To deep-link an event in a submission, copy its href:</p>
<ul>
<li><code>events/lockout-row-09.html</code> — the 1:54 AM Constable warning</li>
<li><code>charges/charge-co-25-2722.html</code> — DV breach charge teardown</li>
<li><code>statements/stmt-negro-25feb2025.html</code> — Negro 25 Feb 2025 paragraph-by-paragraph</li>
<li><code>ware.html#A4</code> — outstanding Davies 5-page statement</li>
</ul>

<h2>Sources ingested</h2>
<table id="sources-table"><thead><tr><th>ID</th><th>File</th><th>Title</th><th>SHA-256 (first 12)</th><th>Bytes</th></tr></thead><tbody>
"""
    for row in cur.execute("SELECT id,filename,title,sha256,bytes FROM source_documents"):
        body += f"<tr><td><code>{_esc(row[0])}</code></td><td>{_esc(row[1])}</td><td>{_esc(row[2])}</td><td><code>{_esc(row[3][:12])}</code></td><td>{row[4]:,}</td></tr>"
    body += "</tbody></table>"
    _page("Index", body, OUT_DIR / "index.html")


def build_timeline(conn: sqlite3.Connection):
    cur = conn.cursor()
    rows = cur.execute(
        """SELECT e.id, p.id, p.ordinal, p.title, e.event_date, e.event_time,
                  e.date_label, e.description, e.source_doc_id, e.defeats
           FROM events e LEFT JOIN phases p ON p.id = e.phase_id
           ORDER BY p.ordinal, e.event_date IS NULL, e.event_date, e.event_time, e.id"""
    ).fetchall()
    body = """
<h1>Master timeline</h1>
<p class="muted">All events from ALTERNATIVE_CASE.md + LOCKOUT_NIGHT_TIMELINE_CARD.md, ordered by phase then date.</p>
<input id="tl-q" class="search-box" placeholder="Filter events…">
<table id="tl"><thead>
<tr><th>Phase</th><th>Date</th><th>Time</th><th>Event</th><th>Defeats</th><th>Source</th></tr>
</thead><tbody>
"""
    for ev_id, phase_id, _ord, phase_title, date, time, label, desc, src, defeats in rows:
        phase_short = (phase_title or "").split("—", 1)[0].strip() or (phase_id or "")
        body += (
            f"<tr><td><a href='phases/{_esc(phase_id)}.html'>{_esc(phase_short)}</a></td>"
            f"<td>{_esc(date or label or '')}</td>"
            f"<td>{_esc(time or '')}</td>"
            f"<td><a href='events/{_esc(ev_id)}.html'>{_esc((desc or '')[:140])}</a></td>"
            f"<td class='muted'>{_esc((defeats or '')[:120])}</td>"
            f"<td><span class='tag'>{_esc(src)}</span></td></tr>"
        )
    body += "</tbody></table>\n<script>tableSearch('tl','tl-q');</script>"
    _page("Timeline", body, OUT_DIR / "timeline.html")


def build_phases(conn: sqlite3.Connection):
    cur = conn.cursor()
    phases = cur.execute("SELECT id, ordinal, title, summary FROM phases ORDER BY ordinal").fetchall()
    # Index page
    body = "<h1>Phases</h1><table><thead><tr><th>#</th><th>Phase</th><th>Events</th></tr></thead><tbody>"
    for pid, ordinal, title, summary in phases:
        n = cur.execute("SELECT COUNT(*) FROM events WHERE phase_id=?", (pid,)).fetchone()[0]
        body += f"<tr><td>{ordinal}</td><td><a href='{_esc(pid)}.html'>{_esc(title)}</a><br><span class='muted'>{_esc((summary or '')[:200])}</span></td><td>{n}</td></tr>"
    body += "</tbody></table>"
    _page("Phases", body, OUT_DIR / "phases" / "index.html")

    for pid, ordinal, title, summary in phases:
        events = cur.execute(
            "SELECT id, event_date, event_time, date_label, description, defeats, source_doc_id "
            "FROM events WHERE phase_id=? ORDER BY event_date IS NULL, event_date, event_time, id",
            (pid,),
        ).fetchall()
        body = f"<h1>{_esc(title)}</h1>"
        if summary:
            body += f"<p class='muted'><em>{_esc(summary)}</em></p>"
        body += f"<p class='muted'>{len(events)} event(s)</p>"
        for ev_id, date, time, label, desc, defeats, src in events:
            body += "<div class='card'>"
            body += f"<div class='kv'><span class='k'>id</span><span><code>{_esc(ev_id)}</code></span>"
            body += f"<span class='k'>date</span><span>{_esc(date or label or '?')}</span>"
            if time:
                body += f"<span class='k'>time</span><span>{_esc(time)}</span>"
            body += f"<span class='k'>source</span><span><span class='tag'>{_esc(src)}</span></span>"
            body += "</div>"
            body += f"<p>{_esc(desc)}</p>"
            if defeats:
                body += f"<p><strong>Defeats:</strong> <span class='muted'>{_esc(defeats)}</span></p>"
            # Evidence list
            ev_anchors = cur.execute(
                "SELECT e.id, e.ref, e.text, e.kind FROM event_evidence ee "
                "JOIN evidence e ON e.id=ee.evidence_id WHERE ee.event_id=?",
                (ev_id,),
            ).fetchall()
            if ev_anchors:
                body += "<details><summary>Evidence anchors (" + str(len(ev_anchors)) + ")</summary><ul>"
                for eid, ref, text, kind in ev_anchors:
                    body += f"<li><span class='tag info'>{_esc(kind)}</span><a href='../evidence/{_esc(eid)}.html'>{_esc(ref)}</a> — {_esc(text)}</li>"
                body += "</ul></details>"
            body += f"<p style='margin-top:.4rem'><a href='../events/{_esc(ev_id)}.html'>open event page →</a></p>"
            body += "</div>"
        _page(f"Phase {ordinal} — {title}", body, OUT_DIR / "phases" / f"{pid}.html",
              breadcrumb=[("Index", "index.html"), ("Phases", "phases/index.html"), (title, "")])


def build_events(conn: sqlite3.Connection):
    cur = conn.cursor()
    events = cur.execute(
        "SELECT id, phase_id, event_date, event_time, date_label, description, defeats, source_doc_id "
        "FROM events"
    ).fetchall()
    for ev_id, phase_id, date, time, label, desc, defeats, src in events:
        ev_anchors = cur.execute(
            "SELECT e.id, e.ref, e.text, e.kind FROM event_evidence ee "
            "JOIN evidence e ON e.id=ee.evidence_id WHERE ee.event_id=?",
            (ev_id,),
        ).fetchall()
        actors = cur.execute(
            "SELECT a.id, a.display_name, a.role FROM event_actors ea "
            "JOIN actors a ON a.id=ea.actor_id WHERE ea.event_id=?",
            (ev_id,),
        ).fetchall()
        body = f"<h1>{_esc(desc)}</h1>"
        body += "<div class='card'><div class='kv'>"
        body += f"<span class='k'>id</span><span><code>{_esc(ev_id)}</code></span>"
        body += f"<span class='k'>phase</span><span><a href='../phases/{_esc(phase_id)}.html'>{_esc(phase_id)}</a></span>"
        body += f"<span class='k'>date</span><span>{_esc(date or label or '')}</span>"
        if time:
            body += f"<span class='k'>time</span><span>{_esc(time)}</span>"
        body += f"<span class='k'>source</span><span><span class='tag'>{_esc(src)}</span></span>"
        if defeats:
            body += f"<span class='k'>defeats</span><span>{_esc(defeats)}</span>"
        body += "</div></div>"
        if actors:
            body += "<h2>Actors</h2><ul>"
            for aid, name, role in actors:
                body += f"<li><a href='../actors/{_esc(aid)}.html'>{_esc(name)}</a> <span class='tag'>{_esc(role)}</span></li>"
            body += "</ul>"
        if ev_anchors:
            body += f"<h2>Evidence anchors ({len(ev_anchors)})</h2><ul>"
            for eid, ref, text, kind in ev_anchors:
                body += f"<li><span class='tag info'>{_esc(kind)}</span><a href='../evidence/{_esc(eid)}.html'>{_esc(ref)}</a> — {_esc(text)}</li>"
            body += "</ul>"
        body += f"<h2>Citation</h2><pre>events/{_esc(ev_id)}.html</pre>"
        _page(desc[:60], body, OUT_DIR / "events" / f"{ev_id}.html",
              breadcrumb=[("Index", "index.html"), ("Timeline", "timeline.html"), (ev_id, "")])


def build_evidence(conn: sqlite3.Connection):
    cur = conn.cursor()
    rows = cur.execute("SELECT id, ref, text, kind FROM evidence ORDER BY ref").fetchall()
    body = """
<h1>Evidence anchor ledger</h1>
<p class="muted">Every distinct evidence anchor referenced anywhere across the 7 source documents.</p>
<input id="ev-q" class="search-box" placeholder="Filter evidence…">
<table id="ev-tbl"><thead><tr><th>Kind</th><th>Ref</th><th>Text</th><th>Citations</th></tr></thead><tbody>
"""
    for eid, ref, text, kind in rows:
        n_events = cur.execute("SELECT COUNT(*) FROM event_evidence WHERE evidence_id=?", (eid,)).fetchone()[0]
        n_paras = cur.execute("SELECT COUNT(*) FROM statement_para_evidence WHERE evidence_id=?", (eid,)).fetchone()[0]
        body += (
            f"<tr><td><span class='tag info'>{_esc(kind)}</span></td>"
            f"<td><a href='{_esc(eid)}.html'>{_esc(ref)}</a></td>"
            f"<td>{_esc(text)}</td>"
            f"<td>{n_events} events · {n_paras} paragraphs</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('ev-tbl','ev-q');</script>"
    _page("Evidence ledger", body, OUT_DIR / "evidence" / "index.html",
          breadcrumb=[("Index", "index.html"), ("Evidence", "")])

    for eid, ref, text, kind in rows:
        body = f"<h1>{_esc(ref)}</h1>"
        body += f"<div class='card'><div class='kv'>"
        body += f"<span class='k'>id</span><span><code>{_esc(eid)}</code></span>"
        body += f"<span class='k'>kind</span><span>{_esc(kind)}</span>"
        body += "</div></div>"
        body += f"<blockquote>{_esc(text)}</blockquote>"
        # Linked events
        events = cur.execute(
            "SELECT e.id, e.description, e.event_date FROM event_evidence ee "
            "JOIN events e ON e.id=ee.event_id WHERE ee.evidence_id=?", (eid,)
        ).fetchall()
        if events:
            body += "<h2>Cited from events</h2><ul>"
            for evid, desc, date in events:
                body += f"<li><a href='../events/{_esc(evid)}.html'>{_esc(date or '')} — {_esc(desc[:100])}</a></li>"
            body += "</ul>"
        # Linked paragraphs
        paras = cur.execute(
            "SELECT sp.id, sp.para_label, sp.statement_id FROM statement_para_evidence spe "
            "JOIN statement_paragraphs sp ON sp.id=spe.paragraph_id WHERE spe.evidence_id=?", (eid,)
        ).fetchall()
        if paras:
            body += "<h2>Cited from witness paragraphs</h2><ul>"
            for pid, plabel, sid in paras:
                body += f"<li><a href='../paragraphs/{_esc(pid)}.html'>{_esc(plabel)}</a> in <a href='../statements/{_esc(sid)}.html'>{_esc(sid)}</a></li>"
            body += "</ul>"
        _page(ref[:60], body, OUT_DIR / "evidence" / f"{eid}.html",
              breadcrumb=[("Index", "index.html"), ("Evidence", "evidence/index.html"), (ref[:40], "")])


def build_charges(conn: sqlite3.Connection):
    cur = conn.cursor()
    charges = cur.execute(
        "SELECT id, matter_id, title, court, status, alleged_summary FROM charges"
    ).fetchall()
    body = "<h1>Charges</h1><div class='grid cols-2'>"
    for cid, matter, title, court, status, _alleged in charges:
        n_fail = cur.execute("SELECT COUNT(*) FROM charge_failures WHERE charge_id=?", (cid,)).fetchone()[0]
        n_el = cur.execute("SELECT COUNT(*) FROM charge_elements WHERE charge_id=?", (cid,)).fetchone()[0]
        body += f"""<a class='card bordered danger' href='{_esc(cid)}.html'>
<h3>{_esc(matter)}</h3>
<p>{_esc(title)}</p>
<p class='muted'><strong>{_esc(court or '')}</strong></p>
<p class='muted'>{_esc(status or '')}</p>
<p><span class='tag'>{n_el} elements</span><span class='tag warn'>{n_fail} failures</span></p>
</a>"""
    body += "</div>"
    _page("Charges", body, OUT_DIR / "charges" / "index.html",
          breadcrumb=[("Index", "index.html"), ("Charges", "")])

    # Cross-charge element grid
    body = "<h1>Element-by-element grid (all charges)</h1><table><thead><tr><th>Charge</th><th>Element</th><th>Failure / Notes</th></tr></thead><tbody>"
    for cid, matter, title, *_ in charges:
        elements = cur.execute(
            "SELECT ordinal, text FROM charge_elements WHERE charge_id=? ORDER BY ordinal", (cid,)
        ).fetchall()
        for ordinal, text in elements:
            related_failures = cur.execute(
                "SELECT element_ref, reason FROM charge_failures "
                "WHERE charge_id=? AND element_ref LIKE ?", (cid, f"Element {ordinal}%")
            ).fetchall()
            failure_html = "<br>".join(
                f"<strong>{_esc(ref)}</strong> — {_esc(reason)}" for ref, reason in related_failures
            ) or "<span class='muted'>—</span>"
            body += (
                f"<tr><td><a href='{_esc(cid)}.html'>{_esc(matter)}</a></td>"
                f"<td>({ordinal}) {_esc(text)}</td>"
                f"<td>{failure_html}</td></tr>"
            )
    body += "</tbody></table>"
    _page("Elements grid", body, OUT_DIR / "elements.html",
          breadcrumb=[("Index", "index.html"), ("Elements grid", "")])

    # Per-charge pages
    for cid, matter, title, court, status, alleged in charges:
        elements = cur.execute(
            "SELECT id, ordinal, text FROM charge_elements WHERE charge_id=? ORDER BY ordinal", (cid,)
        ).fetchall()
        failures = cur.execute(
            "SELECT element_ref, reason, notes FROM charge_failures WHERE charge_id=?", (cid,)
        ).fetchall()
        displacing = cur.execute(
            "SELECT ref FROM charge_displacing_documents WHERE charge_id=?", (cid,)
        ).fetchall()
        body = f"<h1>{_esc(matter)} — {_esc(title)}</h1>"
        body += "<div class='card'><div class='kv'>"
        body += f"<span class='k'>court</span><span>{_esc(court or '')}</span>"
        body += f"<span class='k'>status</span><span>{_esc(status or '')}</span>"
        body += f"<span class='k'>id</span><span><code>{_esc(cid)}</code></span>"
        body += "</div></div>"
        if alleged:
            body += f"<h2>What QPS alleges</h2><p>{_esc(alleged)}</p>"
        body += "<h2>Elements the prosecution must prove</h2><ol>"
        for _eid, ordinal, text in elements:
            body += f"<li id='el-{ordinal}'>{_esc(text)}</li>"
        body += "</ol>"
        body += "<h2>Why each element fails on the record</h2>"
        for ref, reason, notes in failures:
            cls = "danger" if "fail" in (reason or "").lower() else "warn"
            body += f"<div class='card bordered {cls}'><strong>{_esc(ref)}</strong> — {_esc(reason)}"
            if notes:
                body += "<ul>"
                for line in (notes or "").split(" | "):
                    body += f"<li>{_esc(line)}</li>"
                body += "</ul>"
            body += "</div>"
        if displacing:
            body += "<h2>Displacing documents on the case file</h2><ul>"
            for (ref,) in displacing:
                body += f"<li>{_esc(ref)}</li>"
            body += "</ul>"
        _page(matter, body, OUT_DIR / "charges" / f"{cid}.html",
              breadcrumb=[("Index", "index.html"), ("Charges", "charges/index.html"), (matter, "")])


def build_statements(conn: sqlite3.Connection):
    cur = conn.cursor()
    statements = cur.execute(
        "SELECT id, taken_date, taking_officer_id, qprime_ref, source_path FROM statements"
    ).fetchall()
    body = "<h1>Witness paragraphs (UNDERLYING_FACTS_REBUTTAL)</h1>"
    body += '<input id="st-q" class="search-box" placeholder="Filter statements…"><table id="st-tbl">'
    body += "<thead><tr><th>Statement / topic</th><th>Date</th><th>QPRIME</th><th>Paragraphs</th></tr></thead><tbody>"
    for sid, taken_date, _ofc, qprime, _path in statements:
        n = cur.execute("SELECT COUNT(*) FROM statement_paragraphs WHERE statement_id=?", (sid,)).fetchone()[0]
        body += (
            f"<tr><td><a href='{_esc(sid)}.html'>{_esc(sid)}</a></td>"
            f"<td>{_esc(taken_date or '')}</td>"
            f"<td>{_esc(qprime or '')}</td>"
            f"<td>{n}</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('st-tbl','st-q');</script>"
    _page("Statements", body, OUT_DIR / "statements" / "index.html",
          breadcrumb=[("Index", "index.html"), ("Statements", "")])

    for sid, taken_date, _ofc, qprime, source_path in statements:
        paras = cur.execute(
            "SELECT id, para_label, status, status_emoji, verbatim, legal_effect "
            "FROM statement_paragraphs WHERE statement_id=? ORDER BY ordinal",
            (sid,),
        ).fetchall()
        body = f"<h1>{_esc(sid)}</h1>"
        body += "<div class='card'><div class='kv'>"
        if taken_date:
            body += f"<span class='k'>taken</span><span>{_esc(taken_date)}</span>"
        if qprime:
            body += f"<span class='k'>qprime</span><span>{_esc(qprime)}</span>"
        if source_path:
            body += f"<span class='k'>source</span><span><code>{_esc(source_path)}</code></span>"
        body += "</div></div>"
        body += "<h2>Paragraphs</h2><table><thead><tr><th>¶</th><th>Status</th><th>Verbatim / topic</th><th>Effect</th></tr></thead><tbody>"
        for pid, plabel, status, status_emoji, verbatim, legal_effect in paras:
            cls = f"row-{status}" if status in ("disputed", "dispositive") else ""
            body += (
                f"<tr class='{cls}'><td><a href='../paragraphs/{_esc(pid)}.html'>{_esc(plabel)}</a></td>"
                f"<td><span class='status-badge status-{_esc(status)}'>{_esc(status_emoji)} {_esc(status)}</span></td>"
                f"<td>{_esc((verbatim or '')[:200])}</td>"
                f"<td class='muted'>{_esc((legal_effect or '')[:160])}</td></tr>"
            )
        body += "</tbody></table>"
        _page(sid, body, OUT_DIR / "statements" / f"{sid}.html",
              breadcrumb=[("Index", "index.html"), ("Statements", "statements/index.html"), (sid, "")])

    # Per-paragraph pages
    paragraphs = cur.execute(
        "SELECT id, statement_id, para_label, status, status_emoji, verbatim, legal_effect "
        "FROM statement_paragraphs"
    ).fetchall()
    for pid, sid, plabel, status, status_emoji, verbatim, legal_effect in paragraphs:
        evid_rows = cur.execute(
            "SELECT e.id, e.ref, e.text FROM statement_para_evidence spe "
            "JOIN evidence e ON e.id=spe.evidence_id WHERE spe.paragraph_id=?", (pid,)
        ).fetchall()
        body = f"<h1>{_esc(sid)} — {_esc(plabel)}</h1>"
        body += f"<p><span class='status-badge status-{_esc(status)}'>{_esc(status_emoji)} {_esc(status)}</span></p>"
        if verbatim:
            body += f"<h2>Verbatim</h2><blockquote>{_esc(verbatim)}</blockquote>"
        if evid_rows:
            body += "<h2>Displacing evidence</h2><ul>"
            for eid, ref, text in evid_rows:
                body += f"<li><a href='../evidence/{_esc(eid)}.html'>{_esc(ref)}</a> — {_esc(text)}</li>"
            body += "</ul>"
        if legal_effect:
            body += f"<h2>Legal effect</h2><p>{_esc(legal_effect)}</p>"
        body += f"<p><a href='../statements/{_esc(sid)}.html'>← back to statement</a></p>"
        _page(plabel, body, OUT_DIR / "paragraphs" / f"{pid}.html",
              breadcrumb=[("Index", "index.html"), ("Statements", "statements/index.html"),
                          (sid, f"statements/{sid}.html"), (plabel, "")])


def build_actors(conn: sqlite3.Connection):
    cur = conn.cursor()
    actors = cur.execute("SELECT id, display_name, role, reg_number, organisation, notes FROM actors ORDER BY role, display_name").fetchall()
    body = "<h1>Actor catalogue</h1>"
    body += '<input id="ac-q" class="search-box" placeholder="Filter actors…"><table id="ac-tbl">'
    body += "<thead><tr><th>Role</th><th>Name</th><th>Reg #</th><th>Org</th><th>Events</th></tr></thead><tbody>"
    for aid, name, role, reg, org, _notes in actors:
        n = cur.execute("SELECT COUNT(*) FROM event_actors WHERE actor_id=?", (aid,)).fetchone()[0]
        body += (
            f"<tr><td><span class='tag'>{_esc(role)}</span></td>"
            f"<td><a href='{_esc(aid)}.html'>{_esc(name)}</a></td>"
            f"<td>{_esc(reg or '')}</td>"
            f"<td>{_esc(org or '')}</td>"
            f"<td>{n}</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('ac-tbl','ac-q');</script>"
    _page("Actors", body, OUT_DIR / "actors" / "index.html",
          breadcrumb=[("Index", "index.html"), ("Actors", "")])

    for aid, name, role, reg, org, notes in actors:
        events = cur.execute(
            "SELECT e.id, e.event_date, e.description FROM event_actors ea "
            "JOIN events e ON e.id=ea.event_id WHERE ea.actor_id=? "
            "ORDER BY e.event_date IS NULL, e.event_date",
            (aid,),
        ).fetchall()
        body = f"<h1>{_esc(name)}</h1>"
        body += "<div class='card'><div class='kv'>"
        body += f"<span class='k'>id</span><span><code>{_esc(aid)}</code></span>"
        body += f"<span class='k'>role</span><span>{_esc(role or '')}</span>"
        if reg:
            body += f"<span class='k'>reg</span><span>{_esc(reg)}</span>"
        if org:
            body += f"<span class='k'>org</span><span>{_esc(org)}</span>"
        body += "</div></div>"
        if notes:
            body += f"<p>{_esc(notes)}</p>"
        if events:
            body += f"<h2>Events involving {_esc(name)} ({len(events)})</h2><ul>"
            for evid, date, desc in events:
                body += f"<li>{_esc(date or '')} — <a href='../events/{_esc(evid)}.html'>{_esc((desc or '')[:140])}</a></li>"
            body += "</ul>"
        _page(name, body, OUT_DIR / "actors" / f"{aid}.html",
              breadcrumb=[("Index", "index.html"), ("Actors", "actors/index.html"), (name, "")])


def build_corrections(conn: sqlite3.Connection):
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT id, status, quote, original_speaker, corrected_speaker, anchor, category, legal_effect "
        "FROM corrections ORDER BY id"
    ).fetchall()
    body = "<h1>Correction register — speaker mis-attributions</h1>"
    body += '<input id="co-q" class="search-box" placeholder="Filter corrections…"><table id="co-tbl">'
    body += "<thead><tr><th>ID</th><th>Status</th><th>Quote</th><th>Original</th><th>Corrected</th><th>Effect</th></tr></thead><tbody>"
    for cid, status, quote, orig, corr, anchor, cat, effect in rows:
        body += (
            f"<tr id='{_esc(cid)}'><td><a href='#{_esc(cid)}'>{_esc(cid)}</a></td>"
            f"<td>{_esc(status)}</td>"
            f"<td>{_esc((quote or '')[:140])}</td>"
            f"<td class='muted'>{_esc(orig or '')}</td>"
            f"<td><strong>{_esc(corr or '')}</strong></td>"
            f"<td>{_esc((effect or '')[:160])}</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('co-tbl','co-q');</script>"
    _page("Corrections", body, OUT_DIR / "corrections.html",
          breadcrumb=[("Index", "index.html"), ("Corrections", "")])


def build_quote_diff(conn: sqlite3.Connection):
    cur = conn.cursor()
    body = "<h1>Submission quote diff</h1>"
    body += "<p class='muted'>Each row shows a quoted line in the user's submission docs and the closest large-v3 BWC transcript line.</p>"
    body += '<input id="qd-q" class="search-box" placeholder="Filter… (try "drift" or a phrase)"><table id="qd-tbl">'
    body += "<thead><tr><th>Bucket</th><th>Ratio</th><th>Submission</th><th>large-v3 BWC</th><th>Source doc</th></tr></thead><tbody>"
    for row in cur.execute(
        "SELECT id, bucket, ratio, submission_text, largev3_text, largev3_file, source_doc_file FROM quote_diffs ORDER BY bucket DESC, ratio"
    ):
        qid, bucket, ratio, sub, lv3, lv3_file, src = row
        cls = {"drift": "warn", "exact": "ok", "no_match": "info"}.get(bucket, "")
        body += (
            f"<tr><td><span class='tag {cls}'>{_esc(bucket)}</span></td>"
            f"<td>{ratio if ratio is not None else ''}</td>"
            f"<td>{_esc((sub or '')[:160])}</td>"
            f"<td>{_esc((lv3 or '')[:160])}<br><span class='muted'>{_esc(lv3_file or '')}</span></td>"
            f"<td class='muted'>{_esc(src or '')}</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('qd-tbl','qd-q');</script>"
    _page("Quote diff", body, OUT_DIR / "quote_diff.html",
          breadcrumb=[("Index", "index.html"), ("Quote diff", "")])


def build_iterations(conn: sqlite3.Connection):
    cur = conn.cursor()
    its = cur.execute("SELECT id, ordinal, document, date_metadata, author, producer, pages, occasion FROM iterations ORDER BY ordinal").fetchall()
    body = "<h1>Three iterations of the prosecution disclosure</h1><table><thead><tr><th>#</th><th>Doc</th><th>Date</th><th>Author</th><th>Producer</th><th>Pages</th><th>Occasion</th></tr></thead><tbody>"
    for row in its:
        body += "<tr>" + "".join(f"<td>{_esc(c)}</td>" for c in row[1:]) + "</tr>"
    body += "</tbody></table>"
    body += "<h2>Field-by-field changes (30 fields)</h2>"
    body += '<input id="it-q" class="search-box" placeholder="Filter…"><table id="it-tbl">'
    body += "<thead><tr><th>#</th><th>Field</th><th>Iter 1</th><th>Iter 2</th><th>Iter 3</th><th>Who</th><th>When</th><th>Significance</th></tr></thead><tbody>"
    for row in cur.execute(
        "SELECT ordinal, field, iter1_value, iter2_value, iter3_value, who_changed, when_changed, legal_significance "
        "FROM iteration_field_changes ORDER BY ordinal"
    ):
        body += f"<tr id='fc-{row[0]:02d}'>" + "".join(f"<td>{_esc(c)}</td>" for c in row) + "</tr>"
    body += "</tbody></table><script>tableSearch('it-tbl','it-q');</script>"
    _page("Iterations", body, OUT_DIR / "iterations.html",
          breadcrumb=[("Index", "index.html"), ("Iterations", "")])


def build_ware(conn: sqlite3.Connection):
    cur = conn.cursor()
    body = "<h1>Ware disclosure schedule (33 items)</h1>"
    body += "<p class='muted'>From Nick Ware's letter to QPS Prosecutions, 25 September 2025. Status as at 4 May 2026 (per the forensic analysis).</p>"
    body += '<input id="w-q" class="search-box" placeholder="Filter…"><table id="w-tbl">'
    body += "<thead><tr><th>ID</th><th>Part</th><th>Description</th><th>Status now</th><th>Days out</th><th>Legal consequence</th></tr></thead><tbody>"
    for row in cur.execute(
        "SELECT id, part, description, current_status, days_out, legal_consequence FROM ware_schedule ORDER BY part, id"
    ):
        wid, part, desc, status, days, conseq = row
        outstanding = "OUTSTANDING" in (status or "")
        cls = "row-disputed" if outstanding else ""
        body += (
            f"<tr id='{_esc(wid)}' class='{cls}'><td><a href='#{_esc(wid)}'>{_esc(wid)}</a></td>"
            f"<td>{_esc(part)}</td>"
            f"<td>{_esc(desc)}</td>"
            f"<td><strong>{_esc(status or '')}</strong></td>"
            f"<td>{_esc(days or '')}</td>"
            f"<td>{_esc(conseq or '')}</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('w-tbl','w-q');</script>"
    _page("Ware schedule", body, OUT_DIR / "ware.html",
          breadcrumb=[("Index", "index.html"), ("Ware schedule", "")])


def build_lockout_night(conn: sqlite3.Connection):
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT row_no, event_id, time_label, actor, event_text, defeats FROM lockout_rows ORDER BY row_no"
    ).fetchall()
    body = "<h1>Lockout-night card — 14 rows</h1>"
    body += "<table><thead><tr><th>#</th><th>Time</th><th>Actor</th><th>Event</th><th>Defeats</th></tr></thead><tbody>"
    for row_no, ev_id, time, actor, text, defeats in rows:
        body += (
            f"<tr id='row-{row_no:02d}'><td>{row_no}</td>"
            f"<td>{_esc(time)}</td>"
            f"<td>{_esc(actor)}</td>"
            f"<td><a href='events/{_esc(ev_id)}.html'>{_esc(text)}</a></td>"
            f"<td class='muted'>{_esc(defeats)}</td></tr>"
        )
    body += "</tbody></table>"
    _page("Lockout night", body, OUT_DIR / "lockout_night.html",
          breadcrumb=[("Index", "index.html"), ("Lockout night", "")])


def build_validation(conn: sqlite3.Connection):
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT severity, category, entity_table, entity_id, message, detail FROM validation_findings "
        "ORDER BY severity, category"
    ).fetchall()
    body = "<h1>Validation findings</h1>"
    body += "<p class='muted'>Internal-consistency checks across the 7 ingested source documents.</p>"
    counts: dict[tuple[str, str], int] = {}
    for sev, cat, *_ in rows:
        counts[(sev, cat)] = counts.get((sev, cat), 0) + 1
    body += "<table><thead><tr><th>Severity</th><th>Category</th><th>#</th></tr></thead><tbody>"
    for (sev, cat), n in sorted(counts.items()):
        cls = {"error": "danger", "warning": "warn", "info": "info"}.get(sev, "")
        body += f"<tr><td><span class='tag {cls}'>{_esc(sev)}</span></td><td>{_esc(cat)}</td><td>{n}</td></tr>"
    body += "</tbody></table>"
    body += '<h2>All findings</h2><input id="v-q" class="search-box" placeholder="Filter…"><table id="v-tbl">'
    body += "<thead><tr><th>Sev</th><th>Cat</th><th>Entity</th><th>Message</th><th>Detail</th></tr></thead><tbody>"
    for sev, cat, tbl, eid, msg, detail in rows:
        cls = {"error": "danger", "warning": "warn", "info": "info"}.get(sev, "")
        body += (
            f"<tr><td><span class='tag {cls}'>{_esc(sev)}</span></td>"
            f"<td>{_esc(cat)}</td>"
            f"<td><code>{_esc(tbl)}/{_esc(eid)}</code></td>"
            f"<td>{_esc(msg)}</td>"
            f"<td class='muted'>{_esc((detail or '')[:200])}</td></tr>"
        )
    body += "</tbody></table><script>tableSearch('v-tbl','v-q');</script>"
    _page("Validation", body, OUT_DIR / "validation.html",
          breadcrumb=[("Index", "index.html"), ("Validation", "")])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    print("building index...")
    build_index(conn)
    print("building timeline...")
    build_timeline(conn)
    print("building phases...")
    build_phases(conn)
    print("building events...")
    build_events(conn)
    print("building evidence...")
    build_evidence(conn)
    print("building charges...")
    build_charges(conn)
    print("building statements + paragraphs...")
    build_statements(conn)
    print("building actors...")
    build_actors(conn)
    print("building corrections...")
    build_corrections(conn)
    print("building quote diff...")
    build_quote_diff(conn)
    print("building iterations...")
    build_iterations(conn)
    print("building ware schedule...")
    build_ware(conn)
    print("building lockout night...")
    build_lockout_night(conn)
    print("building validation...")
    build_validation(conn)

    conn.close()

    n_files = sum(1 for _ in OUT_DIR.rglob("*.html"))
    print(f"\nWrote {n_files} HTML files to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
