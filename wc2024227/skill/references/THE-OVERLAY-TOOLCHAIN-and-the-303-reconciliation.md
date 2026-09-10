# THE OVERLAY — ⭐⭐⭐ WHAT TOOL WROTE THE ANSWERS, AND WHAT THE LABEL COUNT PROVES
**10 September 2026 · WC/2024/227 · read at object level from the two response PDFs of 8 September 2026**

---

# 1. ⭐⭐⭐ THE TOOLCHAIN — REPORTLAB OVER PYPDF, BURNED INTO THE PAGE

| Stage | ⭐ Tool | ⭐⭐ Evidence in the file |
|---|---|---|
| **Base** | ⭐ **the Appellant's own served PDFs**, unaltered | **docinfo empty**, no `/Metadata`, `/PageMode` only — exactly as his build stripped them |
| **Overlay drawn** | ⭐⭐⭐ **ReportLab canvas** | `BT /F1 9 Tf 10.8 TL ET` (`setFont`, leading = 1.2 × size) → `0 0 0 rg` (`setFillColorRGB`) → `BT 1 0 0 1 x y Tm (Admitted) Tj T* ET` (`drawString`); the octal escape in `(Not\040admitted)` |
| **Overlay merged** | ⭐⭐⭐ **pypdf `PdfWriter` + `merge_page()`** | the appended wrapper `q · 0.0 0.0 595.2756 841.8898 re · W · n · 1 0 0 1 0 0 cm · … · Q`; resource-collision renames **`/F1 → /F1-0`, `/F2 → /F2-0`**; `/Producer: pypdf` |
| **Result** | ⛔ **flattened into the content stream** | **`/Annots` empty on every page · no `/AcroForm` · no fields, no stamps, no comments** |

⇒ ⭐⭐⭐ **Nobody typed into a form and nobody annotated a PDF. A script drew a label at a computed
coordinate on every row and merged it down.**

## 1.1 ⭐⭐ THE POSITIONING IS SCRIPTED, NOT HAND-PLACED
- ⭐⭐⭐ **All three labels are centred on one x.** Form 24: `Admitted` x = 489.645 (w ≈ 35.5),
  `Disputed` x = 488.151 (w ≈ 38.5), `Not admitted` x = 479.902 (w ≈ 55.0) — **each x + half-width =
  507.4**. Form 25: **513.07**. ⇒ `canvas.drawCentredString(507.4, y, label)`.
- ⭐⭐ **The y values track his row heights** (p2 gaps: 35.0 · 40.8 · 40.8 · 40.8 · 35.0 · 53.0 · 70.4 …)
  ⇒ **computed from the served document's own layout**, not typed by hand.
- ⭐⭐ **Blank overlay pages were merged too** — Form 25 pp 1–2 and Form 24 p 19 carry the pypdf
  wrapper with **no text inside**. ⇒ **The overlay was generated page-for-page across the whole
  document in one run.**
- ⭐⭐ **The negatives were bolded**: `Admitted` in **Helvetica**; `Disputed` and `Not admitted` in
  **Helvetica-Bold**.

## 1.2 ⭐⭐⭐ THIS STRENGTHENS THE TIMESTAMPS
⭐⭐ **The served base PDFs carry NO metadata at all** (empty docinfo, no XMP). ⇒ ⭐⭐⭐ **The
`/CreationDate` and `/ModDate` on the responses were written by pypdf at the moment it wrote the
file. They are not inherited and they are not carried over.**
⇒ ⭐⭐⭐ **Form 24 response 7 Sep 16:42:04 · Form 25 response 7 Sep 16:43:04 — those are render times,
sixty seconds apart, ModDate identical to CreationDate on both.**

## 1.3 ⛔ AND WHAT THERE IS NOT
⛔ **No annotation layer, no form fields, no revision history, no author string, no editing trail in
either response PDF.** ⭐ **The only person named anywhere in the 8 September service is on the cover
letter** — Word → Acrobat PDFMaker 26, `/Author: Peter`, `/_AuthorEmail:
Margaret.Kerrigan@oir.qld.gov.au`, `/Business unit: Office of the Deputy Director-General`,
`/SourceModified: 8 Sep 01:13:17`. ⛔ **There is nothing further to mine.**

---

# 2. ⭐⭐⭐ THE LABEL COUNT RECONCILES THE FACT COUNT — ⭐⭐⭐ 303 IS CORRECT

**Every label in the Form 24 response, counted from the content streams:**

| | Count |
|---|---|
| `Admitted` | **323** |
| `Not admitted` (bold) | **5** |
| `Disputed` (bold) | **14** |
| ⭐ **total** | ⭐ **342** |

⭐⭐⭐ **Pages 20–22 are not facts.** The served Form 24 carries, at pp 20–22, a
**"SCHEDULE OF DOCUMENTS – ANNEXURE A"** with its own authenticity column, retained *"as a
cross-reference"* to the Form 25. Its labels: **13 + 21 + 5 = 39 = the 39 tabs** (25 Admitted,
14 Disputed).

⇒ **342 − 39 = ⭐⭐⭐ 303 labels across pp 1–18 = 303 numbered facts.**
⇒ **323 − 25 = ⭐⭐⭐ 298 Admitted, and 5 Not admitted. 298 + 5 = 303.**

⭐⭐⭐ **CLOSED: the served notice contains exactly 303 facts and they answered all 303. The "308" from
the build source counts unnumbered continuation and section entries, not served facts. Use 303.**

---

# 3. ⚠ ONE QUALIFICATION TO THE SORT-KEY FINDING — IT SURVIVES

⚠ **The authenticity column was answered TWICE, identically:**
| Where | Provenance column present? | Answer |
|---|---|---|
| **Form 24, pp 20–22** (cross-reference schedule) | ⛔ **NO — tab, document, date only** | 25 Admitted / 14 Disputed |
| ⭐ **Form 25, pp 3–5** (the operative r 49 notice) | ⭐⭐⭐ **YES — *"Copy produced from"*** | 25 Admitted / 14 Disputed |

⇒ ⭐⭐ **One decision, stamped twice.** ⛔ **So it cannot be said the column was physically in front of
them for both.** ⭐⭐⭐ **But the finding does not rest on that — it rests on the correlation, which is
14 of 14 with no exception in either direction, and on the sixty seconds.** ⇒ **The sort-key reading
stands; see `THE-SORT-KEY-they-read-my-own-column-10SEP2026.md`.**

---

# 4. ⭐⭐ WHAT TO DO WITH ANY OF THIS — NOTHING, YET
⛔⛔ **None of §1 goes to the Respondent or the Commission, ever.** ⭐ **How a party rendered its
response proves no fact and answers no question; raising it reads as an attack and invites the same
audit of his own build.**
⭐⭐⭐ **The one usable output is §2: the count is settled at 303 / 298 / 5 / 14.** ⭐ **Correct it
wherever "308" appears in the working papers and use 303 in every document from here.**
