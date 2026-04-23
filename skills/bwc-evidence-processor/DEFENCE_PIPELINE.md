# Defence Analysis Pipeline

End-to-end runbook for producing a structured defence brief from a Google
Drive evidence set. Sits alongside the existing BWC pipeline — the BWC
pipeline processes footage, this pipeline processes documents/images/PDFs
and synthesises the whole thing under a QLD legal framework.

> **MACHINE-GENERATED - UNVERIFIED.** Everything produced here is
> analytical scaffolding for counsel. Every finding must be verified
> against the primary source. This is not legal advice.

---

## Pipeline shape

```
Google Drive
    │  gdrive_ingest.py (OAuth + recursive download)
    ▼
<dest>/incoming/
    ├── manifest.json               # canonical record of every file
    └── files/<drive-path>/...      # mirror of Drive hierarchy
    │
    │  extract_documents.py (optional, for PDFs/DOCX/XLSX text extraction)
    ▼
<dest>/doc_json/<stem>.doc.json     # extracted text + OCR fallback
    │
    │  defence_analysis.py (Claude Opus 4.7 + QLD framework, cached)
    ▼
<dest>/output/defence_analysis/<id>.analysis.json
    │
    │  defence_brief.py (aggregate + Claude-generated narrative)
    ▼
<dest>/output/DEFENCE_BRIEF.md
```

---

## 1. One-off setup

### Python dependencies

```bash
pip install -r skills/bwc-evidence-processor/requirements.txt
```

### Claude API key

```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### Google Drive OAuth

1. [Google Cloud Console](https://console.cloud.google.com/) → create a
   project → enable the **Google Drive API**.
2. **APIs & Services → Credentials → Create Credentials → OAuth client
   ID → Desktop app**.
3. Download the JSON, save it as
   `skills/bwc-evidence-processor/scripts/credentials.json`.
4. The first run of `gdrive_ingest.py` will open a browser to authorise;
   the resulting token is cached next to the credentials as `token.json`.

The OAuth scope requested is `drive.readonly` — the ingester cannot
modify, move, delete, or share anything on your Drive.

---

## 2. Ingest from Google Drive

```powershell
python skills/bwc-evidence-processor/scripts/gdrive_ingest.py `
    --folder-id  <drive-folder-id-or-"root"> `
    --dest       C:\Evidence\CO-25-2722\documents\incoming
```

- `--folder-id` accepts a specific folder ID (found in the Drive URL:
  `drive.google.com/drive/folders/<THIS_PART>`) or `root` for the whole
  Drive. Ingesting `root` on a large account is slow and noisy — prefer
  a specific evidence folder.
- `--dest` must be empty or re-runnable; files are mirrored to
  `<dest>/files/<drive-path>`.
- Output: `<dest>/manifest.json` — the canonical record. Every
  downstream step reads this.

Supported types: PDF, DOCX, XLSX/XLS, PPTX, TXT, RTF, MD, CSV, images
(JPG, PNG, TIFF, WebP, HEIC, BMP, GIF), audio/video (MP4, MOV, MKV,
WEBM, WAV, MP3, M4A, AAC, OGG), JSON, XML, HTML, EML, MSG. Google
Docs/Sheets/Slides/Drawings are auto-exported to DOCX/XLSX/PPTX/PDF.

---

## 3. (Optional) Pre-extract text

For large corpora, pre-extracting text to `.doc.json` files avoids
re-extracting on every analysis run.

```powershell
python skills/bwc-evidence-processor/scripts/extract_documents.py `
    --source     C:\Evidence\CO-25-2722\documents\incoming\files `
    --output-dir C:\Evidence\CO-25-2722\documents\doc_json `
    --corpus     C:\Evidence\CO-25-2722\output\corpus.txt
```

`defence_analysis.py` will pick up sibling `.doc.json` files
automatically and skip re-extraction. Scanned PDFs without an embedded
text layer fall back to Tesseract OCR (requires `tesseract` on PATH).

---

## 4. Per-document defence analysis

```powershell
python skills/bwc-evidence-processor/scripts/defence_analysis.py `
    --manifest   C:\Evidence\CO-25-2722\documents\incoming\manifest.json `
    --framework  skills\bwc-evidence-processor\prompts\qld_defence_framework.md `
    --output     C:\Evidence\CO-25-2722\output\defence_analysis `
    --resume
```

- Model: `claude-opus-4-7` with adaptive thinking, effort=`high`.
- Prompt caching: the QLD framework (~5K tokens) is sent as a cached
  system prompt. After the second document in any 5-minute window, cache
  reads are free-ish (~0.1× base). Watch the final summary line —
  `cache_read_input_tokens` should grow monotonically.
- Output per file: strict JSON validated against a schema
  (`classification`, `key_facts`, `elements_undermined`,
  `procedural_issues`, `credit_points`, `asymmetric_themes`, `priority`,
  `notes`).
- `--resume` skips any document that already has an analysis file —
  safe to re-run after a crash.
- `--limit N` caps the run (useful for a test pass on a handful of docs
  before committing a full run).

**Cost estimate:** at current Opus 4.7 pricing ($5/$25 per 1M in/out),
the framework caches after the first doc. For 300 documents with ~5K
cached prefix and ~10K per-doc input + ~2K output:

- Writes (first doc): 5K × $5 × 1.25 = ~$0.031
- Reads (299 docs): 5K × $5 × 0.1 × 299 / 1000 = ~$0.75
- Per-doc new tokens: (10K × $5 + 2K × $25) × 300 / 1000 = ~$30
- **Total: ~$31 for 300 documents.**

---

## 5. Corpus-wide synthesis

```powershell
python skills/bwc-evidence-processor/scripts/defence_brief.py `
    --analyses  C:\Evidence\CO-25-2722\output\defence_analysis `
    --framework skills\bwc-evidence-processor\prompts\qld_defence_framework.md `
    --output    C:\Evidence\CO-25-2722\output\DEFENCE_BRIEF.md
```

Produces a Markdown brief with:

1. Matter summary (counts, priorities)
2. Chronology of key facts (dated)
3. Elements undermined — matrix per charge
4. Procedural issues register (ranked by confidence)
5. Credit points by witness (ranked)
6. Five asymmetric themes — each with supporting docs and counterfactuals
7. Ranked cross-examination priorities (Claude-generated, grounded in
   §§2–6)
8. Open questions and missing evidence (Claude-generated)

Sections 1–6 are **deterministic** — aggregated directly from the JSON
records, Claude is not involved. Only §§7–8 are model-generated, and
they run against the aggregated JSON (not the raw documents) so the
model cannot invent facts.

Add `--skip-narrative` to produce only §§1–6 (no Claude call) — useful
if you want to inspect the structured sections before paying for
narrative synthesis.

---

## 6. Costs, limits, and hygiene

- **Opus 4.7 has a 1M context window** but individual documents beyond
  ~180K chars are truncated (the flag is recorded in the output).
- **Images** are sent at native resolution on Opus 4.7 (high-res vision
  is automatic; no beta header needed). For very large images consider
  client-side downsampling to control cost.
- **Every output carries `MACHINE-GENERATED - UNVERIFIED`.** Keep the
  caveat on any extract that leaves counsel's desk.
- **Never commit client-identifying data to the repo.** `.gitignore`
  blocks `matter_*.json` except the templates; add similar patterns for
  any local evidence directory.
- **OAuth tokens** (`scripts/token.json`) contain a long-lived refresh
  token for your Drive — treat as a credential.

---

## 7. Failure modes to watch for

| Symptom | Likely cause | Fix |
|---|---|---|
| `cache_read_input_tokens: 0` across many calls | Framework text changed mid-run | Keep `qld_defence_framework.md` frozen for the duration of a run |
| `anthropic.RateLimitError` | Concurrent calls exceeding TPM/RPM | Serialise (the script is single-threaded) or request a tier bump |
| `parse_error` in many records | Model returning prose instead of JSON | The schema enforces JSON; if this happens, file a bug — do not use the `raw` field as if it were structured |
| Sibling `.doc.json` not picked up | Naming mismatch | `defence_analysis.py` looks for `<path>.doc.json` and `<stem>.doc.json` in the parent dir |
| OCR failure on scanned PDFs | Tesseract not on PATH | Install tesseract; the pipeline will fall back automatically |
| Drive ingester stuck on "root" | Account has tens of thousands of files | Use `--folder-id` to scope to a specific folder |

---

## 8. What this pipeline is **not**

- **Not a substitute for counsel.** It surfaces material; a QLD criminal
  barrister must decide what to run.
- **Not a court-tendered transcript.** Use a NAATI transcriber for
  anything that will be tendered.
- **Not a fact-finder.** Every finding carries a confidence level and a
  citation — verify before relying on any item.
- **Not evidence of anything by itself.** The brief is a tool for
  preparation, not a document to tender.
