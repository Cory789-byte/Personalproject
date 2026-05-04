"""Shared parsing helpers."""
from __future__ import annotations

import hashlib
import re
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Iterable

# ---------------------------------------------------------------------------
# Slug / id helpers
# ---------------------------------------------------------------------------

_slug_strip_re = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_len: int = 80) -> str:
    """Lowercase, ascii-only, hyphen-separated. Stable for ids."""
    if not text:
        return "x"
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = _slug_strip_re.sub("-", text).strip("-")
    if not text:
        return "x"
    return text[:max_len]


def short_hash(text: str, n: int = 8) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:n]


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Date / time parsing
# ---------------------------------------------------------------------------

_iso_date_re = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_iso_partial_re = re.compile(r"\b(\d{4})-(\d{2})\b")
_time_re = re.compile(r"\b(\d{1,2}):(\d{2})(?::(\d{2}))?\b")
_iso_dt_re = re.compile(r"\b(\d{4}-\d{2}-\d{2})[T\s](\d{2}):(\d{2})\b")


def extract_date(label: str) -> str | None:
    """Return ISO date 'YYYY-MM-DD' or partial 'YYYY-MM' from a label, else None."""
    if not label:
        return None
    m = _iso_date_re.search(label)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = _iso_partial_re.search(label)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    return None


def extract_time(label: str) -> str | None:
    if not label:
        return None
    # prefer HH:MM at end of label or after the date
    m = _time_re.search(label)
    if m:
        h = int(m.group(1))
        mins = int(m.group(2))
        if 0 <= h <= 23 and 0 <= mins <= 59:
            return f"{h:02d}:{mins:02d}"
    return None


def now_iso() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

H_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
ANCHOR_RE = re.compile(r'<a\s+id="([^"]+)"\s*>\s*</a>')
BWC_TS_RE = re.compile(r"\[(\d{1,2}:\d{2}(?:[:.]\d{1,2})?(?:\s*[-–]\s*\d{1,2}:\d{2}(?:[:.]\d{1,2})?)?)\]")
QPS_REG_RE = re.compile(r"Reg\s+(\d{4,8})", re.IGNORECASE)


def split_markdown_sections(md_text: str, level: int = 2) -> list[tuple[str, str, str]]:
    """Split a markdown string into sections at headings of the given level.

    Returns list of (heading_text, anchor_id_or_None, body_text). The first
    chunk before any heading at the requested level is returned with empty
    heading + empty anchor.
    """
    lines = md_text.splitlines()
    sections: list[tuple[str, str | None, list[str]]] = []
    current_heading = ""
    current_anchor: str | None = None
    current_body: list[str] = []
    for ln in lines:
        m = H_RE.match(ln)
        if m and len(m.group(1)) == level:
            # flush current
            sections.append((current_heading, current_anchor, current_body))
            heading = m.group(2).strip()
            anchor_match = ANCHOR_RE.search(heading)
            anchor = anchor_match.group(1) if anchor_match else None
            heading_clean = ANCHOR_RE.sub("", heading).strip()
            current_heading = heading_clean
            current_anchor = anchor
            current_body = []
        else:
            current_body.append(ln)
    sections.append((current_heading, current_anchor, current_body))
    return [(h, a or "", "\n".join(b).strip()) for h, a, b in sections]


def iter_subsections(body: str, level: int = 3) -> Iterable[tuple[str, str]]:
    """Yield (heading, body) pairs for sub-headings of the given level."""
    sections = split_markdown_sections(body, level=level)
    for heading, _anchor, sub in sections:
        if heading:
            yield heading, sub


def extract_bullets(body: str, after_marker: str) -> list[str]:
    """Return list of bullet lines under a marker like '**Evidence anchors:**'.

    Bullets start with '- '. Stops at the next blank line or next bold marker.
    """
    out: list[str] = []
    capture = False
    for ln in body.splitlines():
        s = ln.strip()
        if after_marker in s and s.endswith(":**"):
            capture = True
            continue
        if capture:
            if not s:
                # tolerate single blank between marker and bullets
                if not out:
                    continue
                break
            if s.startswith("- "):
                out.append(s[2:].strip())
            elif s.startswith("**"):
                break
            else:
                # continuation of last bullet
                if out:
                    out[-1] += " " + s
                else:
                    break
    return out


def first_paragraph_after(body: str, after_marker: str) -> str:
    """Return the text immediately following a bold marker line."""
    capture = False
    out: list[str] = []
    for ln in body.splitlines():
        s = ln.strip()
        if after_marker in s and s.endswith(":**"):
            capture = True
            continue
        if capture:
            if not s:
                if out:
                    break
                else:
                    continue
            if s.startswith("**") or s.startswith("- "):
                if out:
                    break
                else:
                    continue
            out.append(s)
    return " ".join(out).strip()


def strip_md_emphasis(text: str) -> str:
    text = re.sub(r"_([^_]+)_", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text


def extract_blockquote(body: str) -> str:
    """Return joined blockquote lines from a section."""
    out: list[str] = []
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith("> "):
            out.append(s[2:].strip())
        elif s.startswith(">"):
            out.append(s[1:].strip())
    return " ".join(out).strip()


# ---------------------------------------------------------------------------
# Evidence categorisation
# ---------------------------------------------------------------------------

def classify_evidence(text: str) -> str:
    t = text.lower()
    if "bwc" in t or "axon body" in t or "body-worn" in t:
        return "bwc"
    if "aff" in t and any(c.isdigit() for c in t.split("aff", 1)[1][:4]):
        return "affidavit"
    if "email" in t or "@" in t:
        return "email"
    if "form 9" in t or "form 13" in t or "form 5" in t or "form 25" in t or "form 18a" in t:
        return "form"
    if "rti" in t:
        return "rti"
    if "qprime" in t or "qp24" in t or "qp25" in t or "occurrence" in t:
        return "qprime"
    if "magistrate" in t or "court" in t or "form 44" in t:
        return "court_order"
    if "whatsapp" in t:
        return "whatsapp"
    if "ccc " in t or "ccc submission" in t:
        return "ccc"
    if "fsq" in t or "specimen" in t:
        return "forensic_specimen"
    if "statement" in t:
        return "statement"
    if "ppra" in t or "torum" in t:
        return "statute"
    return "other"


# ---------------------------------------------------------------------------
# Tiny ID generator with collision suffix
# ---------------------------------------------------------------------------

class IdMinter:
    def __init__(self, prefix: str = ""):
        self.prefix = prefix
        self.seen: dict[str, int] = {}

    def mint(self, *parts: str) -> str:
        base = "-".join(p for p in (self.prefix, *parts) if p).strip("-")
        base = slugify(base)
        n = self.seen.get(base, 0)
        self.seen[base] = n + 1
        return base if n == 0 else f"{base}-{n+1}"
