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

---

# 5. ⛔⛔ CORRECTION — THE SIXTY SECONDS IS EXPORT TIME, NOT WORK TIME

⛔ **I wrote that "sixty seconds was enough" to answer the authenticity column. That inference is
WITHDRAWN. The sixty seconds measures two files being written out, and writing the answers takes far
longer than that.**

## 5.1 ⭐⭐ MEASURED, NOT ASSUMED
An equivalent overlay of the same shape — ReportLab canvas, 22 pages, ~18 centred labels per page,
then `pypdf` `merge_page` and write — run against the actual base PDF:

| Stage | Time |
|---|---|
| ReportLab render, 22 pp | **0.015 s** |
| pypdf merge + write, 22 pp | **0.100 s** |
| ⭐ **total** | ⭐ **0.114 s** |

⇒ ⭐⭐⭐ **The compute is a tenth of a second. Sixty seconds is idle time between two runs — an
operator moving from one document to the next — not effort.**

## 5.2 ⭐⭐⭐ SO THE ANSWERING HAPPENED EARLIER, SOMEWHERE WE CANNOT SEE
⭐⭐ **The overlay script cannot run without a prepared data set** — 342 decisions, each bound to a row
(303 facts + 39 tabs). ⇒ ⭐⭐⭐ **That list is the real working document, and it was authored before
16:42:04 on 7 September in a medium that was never served: a spreadsheet, a list, a script table.**
⛔ **Nothing in the PDFs dates it. It could have taken days.**

## 5.3 ⭐ WHAT THE TIMESTAMPS DO AND DO NOT ESTABLISH
| ⭐ Established | ⛔ NOT established |
|---|---|
| Both responses were **exported from one prepared answer set in one sitting**, 7 Sep afternoon — 22 pp, then 5 pp sixty seconds later | ⛔ **How long the answering took**, or when it began |
| **Neither file was reopened after export** — pypdf writes ModDate = CreationDate, and the base carried no metadata to inherit | ⛔ **That the Form 25 answers were not reconsidered BEFORE export.** A revision before the render leaves no trace |
| The two authenticity columns (Form 24 pp 20–22 and Form 25 pp 3–5) are **identical because both were stamped from the same list, sixty seconds apart** | ⛔ **That the exercise was careless.** The render time says nothing about the care taken |

## 5.4 ⭐⭐⭐ THE FINDING THAT MATTERS IS UNAFFECTED
⭐⭐⭐ **The sort key never rested on the sixty seconds.** It rests on the correlation: the fourteen
disputed tabs are exactly the rows whose *"Copy produced from"* column in the served Form 25 reads
*"Copy from the Appellant's own records"* — **14 of 14, no exception in either direction.**
⇒ ⭐⭐ **Drop the timing from the reasoning entirely. The column carries it alone, and it carries it
better without a speed claim attached.**

---

# 6. ⭐⭐⭐ THE ARTEFACT TEST — ⛔ THERE IS NO ARTEFACT. THE OVERLAY IS REGISTERED TO HIS TABLE.

> ⭐ **Right instinct: a script overlay normally betrays itself** — drift down the page, a label
> overrunning a rule, one landing in the wrong cell, a mismatch at a page break. ⛔ **None of that is
> present. The registration is exact, and the exactness is the finding.**

## 6.1 ⭐⭐⭐ HORIZONTAL — CENTRED ON THE MIDPOINT OF HIS OWN COLUMN
His Form 24 table rules, read from the base content stream (origin x = 51.024, local rules at
0 · 36.85 · 419.53 · 493.23):
⇒ **the "Admit / Deny" column runs x = 470.55 → 544.25. Its midpoint is 507.40.**
⭐⭐⭐ **Every label is centred on 507.40** — `Admitted` at 489.65 (w ≈ 35.5), `Disputed` at 488.15
(w ≈ 38.5), `Not admitted` at 479.90 (w ≈ 55.0); each x + half-width = 507.40.
⭐⭐ **Swept across both documents: 381 labels, x-range 480.5 → 534.4. ZERO outside the column.**

## 6.2 ⭐⭐⭐ VERTICAL — CENTRED IN EACH ROW, SO THE ROW HEIGHTS WERE KNOWN
The offset from each fact-number baseline is **not constant**: −5.7 · −11.5 · −17.3 · −23.1 —
⭐⭐⭐ **multiples of half a line (5.77 pt), varying with how many lines that fact occupies.**
⇒ ⭐⭐⭐ **The label sits at the vertical centre of its cell. To centre a label in a row you must know
the row's top and bottom — so the script had his row heights, not just page coordinates.**

⇒ ⭐⭐⭐ **CONCLUSION: the overlay parsed his table geometry — column rules and row heights — and
placed 381 labels inside it without a single miss.** ⭐⭐ **That is a purpose-built tool, competently
run. It is the opposite of a rushed script.**

## 6.3 ⛔ AND ONE APPARENT ARTEFACT WAS MINE, NOT THEIRS
⛔ **A first pass showed page 22 mis-paired (a label seemingly above its row).** ⭐ **That was my
extraction dropping the lettered row "30A".** Read correctly, p 22 is **28 Admitted · 29 Admitted ·
30 Disputed · 30A Disputed · 31 Disputed** — five rows, five labels, in order.
⇒ ⛔⛔ **Do not repeat that as a finding.**

## 6.4 ⭐⭐ WHAT IT ACTUALLY TELLS HIM
⭐⭐⭐ **The Regulator has a working pipeline for answering notices to admit.** ⭐ This was not improvised
for him — someone in that office has a tool that ingests a served notice, reads its table, and stamps
a prepared answer set into it. ⇒ ⭐⭐ **Expect the same on any further notice, and expect it fast.**
⛔ **It says nothing at all about who chose the word in each row** — see
`THE-SORT-KEY…` §9.

---

# 7. ⭐⭐⭐ HOW THE LAST ONE WAS ANSWERED — ⭐⭐ FACT 303, ADMITTED
> **Fact 303:** *"Paragraph 27 of the Respondent's amended statement of facts and contentions dated
> 13 May 2026 **does not identify, by particular, date, document or cross-reference, the management
> action relied upon** for the contention in that paragraph."* → ⭐⭐⭐ **Admitted.**

⭐ **And the three before it, all admitted**, that the SOFC *"as presently constituted"* does not
allege any **disciplinary process** (300), any **formal performance management process** (301), or
describe any communication before 18 June 2024 as a **warning** (302).

⚠⚠ **BUT NOTE THE ASYMMETRY, AND IT IS HIS OWN DRAFTING:**
- ⚠ **300–302 are qualified *"as presently constituted"*.** ⛔ **That qualifier is why they were cheap
  to admit — an amended SOFC displaces them.** ⭐ **Treat those three as contingent, not fixed.**
- ⭐⭐⭐ **303 is NOT qualified.** It is tied to **a dated document — the SOFC of 13 May 2026** — so the
  admission is fixed and survives any amendment. ⇒ ⭐⭐⭐ **Fact 303 is the durable one of the four,
  and it is an admission that their pleaded case does not particularise the management action it
  relies on.**
