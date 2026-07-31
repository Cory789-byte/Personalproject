# METADATA REGISTER — documents examined 31 July 2026

> Extracted with `pdfinfo` + `pikepdf` XMP. All UTC timestamps converted to **AEST (UTC+10)**.
> ⚠️ **CRITICAL DISTINCTION:** some metadata belongs to **MSH's originals**; most belongs to
> **Cory's own exports** and says nothing about MSH. Marked throughout.
> Tools used: **`pdfinfo`**, **`pikepdf`**, **`exiftool` 12.76** (installed 31 Jul), **`qpdf`**,
> **`pdfimages`**, and **manual incremental-revision recovery** by truncation at each `%%EOF`.

---

## PART 1 — ⭐ MSH-ORIGIN METADATA (the evidentially significant set)

### 1.1 THE TWO 31 JULY LETTERS — PRODUCED 32 MINUTES BEFORE SENDING

| Document | PDF created (AEST) | PDF modified (AEST) | Creator |
|---|---|---|---|
| **GP letter** (5 pp, 9 questions) | **31 Jul 2026 11:10:27** | 11:11:42 | Microsoft® Word for Microsoft 365 |
| **Employee letter** (2 pp) | **31 Jul 2026 11:11:02** | 11:11:27 | Microsoft® Word for Microsoft 365 |
| *Email sent* | — | **11:43** | — |

**What this establishes:**
- The two letters were exported to PDF **35 seconds apart** (11:10:27 and 11:11:02)
- Each was created and last-modified within **25–75 seconds** — a single export action, no
  subsequent editing
- The email went **32 minutes** after the second export

⇒ **Finalisation to transmission: 32 minutes.** Whatever preceded it, the letters were exported and
sent in one sitting. This corroborates the drafting-evidence finding that the request was **not
legally settled** — nothing was reviewed, circulated or amended between export and send.

⚠️ **WHAT IT DOES NOT ESTABLISH.** A Word→PDF export timestamp records when the **PDF** was made,
not when the Word document was drafted. The underlying document may have existed for days. This
fixes the **finalisation** window, not the drafting or decision window.

⚠️ **Author field is blank** (`dc:creator = '-'`) on both. No individual is named in the metadata.
The letters cannot be attributed to a drafter from this source.

### 1.1A ⭐ BOTH HUGHES LETTERS WERE MODIFIED AFTER CREATION — AND ONLY THOSE TWO

| | Employee letter | GP letter | Role Description | Authorisation Form |
|---|---|---|---|---|
| Created | 11:11:02 | 11:10:27 | 5 May 2026 14:29:55 | 20 Jan 2026 11:39:39 |
| Modified | **11:11:27** | **11:11:42** | 14:29:55 (same) | 12:01:20 |
| Gap | **25 sec** | **75 sec** | none | 22 min |
| `/Root` has `/ADBE_FillSignInfo` | **YES** | **YES** | no | no |
| Trailer `/ID` original vs current | **DIFFER** | **DIFFER** | identical | identical |
| `xmpMM:DocumentID` vs `InstanceID` | **differ** | **differ** | identical | differ |

**Two independent indicators that the two letters were altered after generation:**
1. **`/ADBE_FillSignInfo`** in `/Root` — an artefact of Adobe Acrobat's **Fill & Sign** tool. Its
   presence means that feature touched the file. Absent from the other two documents.
2. **The trailer `/ID` array** holds an original and a current value. **They differ on both Hughes
   letters and are identical on the Role Description and Authorisation Form.** A differing pair means
   the file changed after creation.

⇒ **Consistent with a stored signature image applied via Fill & Sign within 25–75 seconds of the PDF
being generated.**

### 1.1B ✅ INCREMENTAL REVISIONS RECOVERED — AND NOTHING WAS HIDDEN

Both letters carry **3 `%%EOF` markers and 2 `/Prev` entries** = three saved generations. Each was
recovered by truncating at the byte offset of each `%%EOF`. All opened cleanly.

| Step | Change | Significant? |
|---|---|---|
| **rev1 → rev2** | +185 bytes; adds `/StructTreeRoot`. **Text identical.** | **NO** — standard Word output. The Role Description does exactly the same (2 EOF, 1 `/Prev`) |
| **rev2 → rev3** | **+99,121 bytes** (employee) / **+101,021** (GP); adds `/OCProperties` **and** `/ADBE_FillSignInfo`; ModDate advances 25s / 75s. **Text identical.** | **YES — and only on the two letters** |

**What rev3 added, per `pdfimages` on the recovered revisions:**
> A **1000 × 398 px JPEG at 624 dpi** plus its transparency mask (~87 KB together, matching the size
> increase), placed on the page carrying the signature block in each letter.
> **1000 ÷ 624 = 1.60 in wide · 398 ÷ 624 = 0.64 in high.**
> **Identical dimensions and byte sizes in both files** — the same stored signature image, applied to
> both documents.

### ⇒ WHAT IS NOW ESTABLISHED
1. **The text of both letters was FINAL at PDF creation.** Identical across all three revisions.
2. A **stored signature image** was applied **25 seconds** (employee) and **75 seconds** (GP) after
   creation, via Adobe Fill & Sign.
3. **Nothing was edited between signing and transmission.**
4. The Role Description has **no third revision** — the signing step is what distinguishes the two
   letters from every other document in the bundle.

### ⚠️ THIS IS A NEGATIVE FINDING ON CONCEALMENT — RECORD IT AS SUCH
The incremental updates were flagged as potentially revealing earlier drafts. **They were recovered,
and they show nothing was changed.** There is no hidden or superseded text. The letters as sent are
the letters as generated.

**It cuts both ways and both should be recorded:**
- **Against MSH** — the whole production (generate → sign → send) occupied ~33 minutes, and the
  signing was a stored image dropped in within 75 seconds. Not a document drafted, reviewed,
  circulated and wet-signed.
- **Against any suggestion of alteration** — there is none. If that was ever a line of attack, it is
  closed. Do not advance it.

⚠️ **STILL NOT ESTABLISHED:** who applied the signature (`/ADBE_FillSignInfo` does not record it),
and when the underlying Word document was drafted.

**Full document identifiers, for the record:**
- Employee letter — `DocumentID uuid:CC55D510-74D3-4FFE-A46B-5F84A422D1F1` ·
  `InstanceID uuid:54bc187e-8e1e-439d-b047-6edc6334202d` ·
  trailer `/ID` `10d555ccd374fe4fa46b5f84a422d1f1` | `fe2037327737af43badc3219693489de`
- GP letter — `DocumentID uuid:9398CC9E-5304-430E-9507-F6ACAE75D11A` ·
  `InstanceID uuid:4cc5e3fb-d3ec-4ec3-a78d-28fcd33a4618` ·
  trailer `/ID` `9ecc989304530e439507f6acae75d11a` | `ce48830372c190438e1983dff2e19a19`
- Both: PDF 1.7, Tagged, XMP toolkit `Adobe XMP Core 5.6-c018 91.98c2f96, 2021/06/15`,
  `/Root` = `/MarkInfo /StructTreeRoot /Metadata /ADBE_FillSignInfo /Type /Lang /ViewerPreferences
  /OCProperties /Pages`, `/Author = "-"`, no Title, no Keywords

### 1.2 THE ROLE DESCRIPTION (their Attachment 2)

| | |
|---|---|
| Created | **5 May 2026, 14:29:55 AEST** |
| Modified | 5 May 2026, 14:29:55 (unchanged) |
| Creator | Microsoft® Word for Microsoft 365 |
| Author | blank |

⚠️ Note the date: **5 May 2026** sits between service of the Form 29 (22 April 2026) and MSH's
objection (5 June 2026), which enclosed a Role Description for Item 6. Role descriptions are
routinely refreshed — **do not over-read this** — but the version relied on against Cory was created
in that window, not years earlier.
[ ] Worth comparing against ATT14 (the RD already in the instruments folder) for any difference.

### 1.3 THE AUTHORISATION FORM (option 2 — unsigned)

| | |
|---|---|
| **Author** | **Katie Ketter** |
| Title | `Microsoft Word - MSH worker-authorisation-form RRTW_Printable` |
| Created | 20 Jan 2026, 11:39:39 AEST · modified 12:01:20 |
| Producer | Microsoft: Print To PDF |

⇒ **Confirms it is a standard MSH template**, not bespoke. "RRTW" = Rehabilitation and Return to
Work. Supports the template-plus-customisation reading of the whole request.

### 1.4 THE ECC (their Attachment 1) — COMPLETELY STRIPPED

**No `/Info` dictionary at all. No XMP stream.** No author, creator, producer, title or dates.
`/Root` contains only `/Type` and `/Pages`. **PDF version 1.3** against 1.7 for every other document
in the bundle. Trailer `/ID` pair identical (`be66735d…` twice) — unmodified since creation.
⇒ A flat scan carrying nothing. Nothing to extract, and nothing to infer beyond that it was scanned
rather than generated.

---

## PART 2 — CORY-ORIGIN METADATA (his own exports — proves nothing about MSH)

These record **his handling**, not MSH's. Useful for establishing when he assembled material, and
nothing else.

| Document | Created (AEST) | Tool |
|---|---|---|
| Outlook email PDFs (Taylor 2 Jul, Calderbank service proof, Roberts, complaint, holding reply) | various, 30–31 Jul 2026 | **Chromium / Skia** — his browser |
| Att B (12 Mar 2025 chain) | **25 Sep 2025, 18:23:43** | Edge 140 print-to-PDF |
| Att C (28 Mar 2025 response) | **25 Sep 2025, 18:23:08** | Edge 140 print-to-PDF |
| Att E (27 Aug 2025 cancellation) | **25 Sep 2025, 18:53:33** | Edge 140 print-to-PDF |
| Att D (court Form 44) | **28 May 2025, 11:53:48**; re-saved 4 Oct 2025 09:13:51 | Microsoft Print To PDF. **Author: Cory Shepherd.** Title: `(D) 2. Verdict Judgement temp PPO TPO.PDF` |
| Att A (DV Aggrieved form) | **4 Oct 2025, 09:14:49** | Adobe Acrobat 25.1 Image Conversion |
| Att F (Hughes 8 Sep 2025 letter, 32 pp) | **4 Oct 2025, 09:04:04** | **KONICA MINOLTA bizhub C300i** (scanner). Title `SKM_C300i25100409030` |

### ⭐ WHAT THIS SHOWS ABOUT HIS OWN PREPARATION

**25 September 2025, ~18:23–18:53** — he saved the three email chains (Att B, C, E) in a single
half-hour session, seventeen days after Hughes signed the attendance letter.

**4 October 2025 morning** — he assembled the bundle:
- **09:04:04** scanned the Hughes letter (32 pp)
- **09:13:51** re-saved the court Form 44
- **09:14:49** converted the DV Aggrieved form
- **12:43** sent the complaint to Jacquie Roberts, cc Heath Moran

⇒ **A documented three-and-a-half-hour assembly on the morning of the complaint.** This corroborates
that the complaint was prepared deliberately from source documents, not written from recollection —
useful if the complaint's provenance is ever questioned.

⚠️ It also means **Att B, C and E are his browser exports, not MSH originals.** They are faithful
renderings of emails, but if native artefacts are ever required (headers, true send times, routing),
these will not suffice. The originals sit in his mailbox.

---

## PART 3 — WHAT THE METADATA DOES AND DOES NOT SUPPORT

| Proposition | Metadata says |
|---|---|
| The 31 July request was rushed | **Supports it** — exported 11:10/11:11, sent 11:43 |
| The letters were modified after generation | **Establishes it** — `/ADBE_FillSignInfo` present and trailer `/ID` pairs differ on both letters, and on neither of the other two documents |
| The signature was applied digitally, in seconds | **ESTABLISHED** — revision 3 adds a 1000×398 px signature image at 624 dpi via Fill & Sign, 25s/75s after creation, identical image in both letters |
| The letters were altered or earlier drafts concealed | **DISPROVED** — all three revisions recovered; text identical throughout |
| Who applied the signature | **Not established** — the artefact does not record it |
| It was not legally reviewed | **Consistent** — no revision cycle between export and transmission |
| Hughes drafted it | **Silent** — author field blank on both letters |
| The decision was made that morning | **Does not establish** — export ≠ drafting. The Word file may predate 31 July |
| The WP letter to Matheson triggered it | **Does not establish** — nothing in the metadata bears on it |
| The authorisation form is a template | **Supports it** — "RRTW_Printable", authored Jan 2026 by Katie Ketter |
| The complaint was deliberately assembled | **Supports it** — 3.5 hours of document preparation on 4 Oct 2025 |

---

## PART 4 — FOLLOW-UPS

- [ ] Compare the 5 May 2026 Role Description against ATT14 for any material difference
- [ ] Preserve the **native** emails for Att B, C, E — the browser exports lack headers
- [ ] If the 31 July Word originals are ever produced, their metadata would show the true drafting
      window and the author. **They have not been produced.**
- [ ] `exiftool` not installed — if deeper extraction is needed later, install it; `pdfinfo` +
      `pikepdf` were sufficient here
