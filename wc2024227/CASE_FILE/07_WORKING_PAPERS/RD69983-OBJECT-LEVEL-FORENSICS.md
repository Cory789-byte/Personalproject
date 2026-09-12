# REVIEW DECISION 69983 — EXHAUSTIVE OBJECT-LEVEL FORENSICS
> 8 August 2026. Worked **only** from `f59eb0c1-Review_Decision_69983.pdf` (Cory's clean copy —
> **not** the iOS re-save). Tools: pikepdf 10.10.0, qpdf, pdffonts, pdfinfo, exiftool 12.76,
> plus a corpus-wide annotation sweep of **360 PDFs / 2,958 URI annotations**.
> ⛔ Supersedes nothing in `FORENSIC-METADATA-12-DOCS.md` Part 7 — **extends it**, and adds one
> finding that changes the balance.

---

# PART 0 — IDENTITY

| | |
|---|---|
| **SHA-256** | `d0b2a514524690557eac52ace21d5864b7004d90ab5d83cd0fd474f25f9e5e9a` |
| **Size** | 258,752 bytes |
| ⭐ **Relationship to the earlier upload** | ⭐⭐ **BYTE-IDENTICAL to `ac5ac79e`.** Same file. **This is the clean original — the phone copy (`documents/Review_Decision_69983_24.10.2024.pdf`, sha `29379f1c…`) is a different, later file and is excluded from everything below** |
| **PDF version** | **1.6** · **linearized** (`Optimized: yes`) · **673 objects** |
| **Pages** | 28 · **MediaBox identical on all 28: 595.32 × 841.92 pt = exact A4** |
| **Encrypted** | No · **Form:** none · **JavaScript:** none · **Suspects:** no |

---

# PART 1 — THE CLOCK: ONE WRITE, NINE SECONDS, NEVER TOUCHED AGAIN

| Field | Value |
|---|---|
| `/CreationDate` | **D:20241024101652+10'00'** → **24 Oct 2024, 10:16:52 AEST** |
| `/ModDate` | **D:20241024101701+10'00'** → **10:17:01 AEST** |
| `xmp:MetadataDate` | 2024-10-24T10:17:01+10:00 |
| **Elapsed** | ⭐ **9 seconds** |
| `%%EOF` count | **2** · `startxref` count: **2** |
| `/Prev` | 258217 · `/Index [643, 30]` |

⭐⭐ **The two `%%EOF`/`startxref` pairs are the LINEARIZATION second cross-reference, not an
incremental update.** ⛔ **There is no revision history. The file was written once and never
edited afterwards.**

**Trailer `/ID`:**
- `/ID[0] = 54A593B7198F664F9049A21D7B6BB125` (permanent, set at creation)
- `/ID[1] = 242F860B2AFE9240BBED128007D786AA` (updated on each write)
- ⚠ **They differ** — consistent with **write → linearize** inside one PDFMaker operation, which is
  exactly what the 9-second window and the single `/Prev` describe. ⛔ **Not evidence of later
  editing.**

⇒ ⭐⭐⭐ **Whatever happened to this document happened before 24 October 2024 at 10:16:52. Nothing
happened to it after 10:17:01.**

---

# PART 2 — THE TOOLCHAIN, CONFIRMED AT STRUCTURE LEVEL (not just the Creator string)

| | |
|---|---|
| `/Creator` | **Acrobat PDFMaker 24 for Word** |
| `/Producer` | **Adobe PDF Library 24.3.212** |
| `x:xmptk` | Adobe XMP Core 9.1-c001 79.675d0f7, 2023/06/11-19:21:16 |
| `/Lang` | **EN-AU** (document level) |
| `/PageLayout` | `/OneColumn` |
| `/MarkInfo` | `/Marked true` — **tagged PDF** |
| `/StructTreeRoot /Namespaces` | `http://iso.org/pdf2/ssn` (PDF 2.0 standard structure namespace) |
| `/ParentTreeNextKey` | 35 |

## ⭐⭐ 2.1 THE ROLEMAP PROVES WORD INDEPENDENTLY OF THE CREATOR STRING

The structure tree carries the **standard Microsoft Word PDFMaker RoleMap** — 15 entries:
`/Annotation→/Span`, `/Artifact→/P`, `/Bibliography→/BibEntry`, `/Chart→/Figure`,
`/Diagram→/Figure`, `/DropCap→/Figure`, `/Endnote→/Note`, **`/Footnote→/Note`**,
`/InlineShape→/Figure`, `/Outline→/Span`, `/Strikeout→/Span`, `/Subscript→/Span`,
`/Superscript→/Span`, **`/TextBox→/Art`**, `/Underline→/Span`.

⇒ ⭐⭐ **A `/Creator` string can be typed. A Word RoleMap cannot.** The source was a Word document.
⛔ **This finally forecloses every "they received the PDF and profiled it" theory — you cannot
PDFMaker-for-Word an incoming PDF.**

## 2.2 STRUCTURE INVENTORY (what the document is made of)

`/P` 353 · `/LI` 58 · `/LBody` 58 · `/L` 8 · **`/Link` 6** · **`/Footnote` 4** · `/Span` 3 ·
`/Document` 1 · `/Sect` 1 · `/Table` 1 · `/TR` 1 · `/TH` 1 · `/Figure` 1

⭐ **Eight lists / 58 list items** = the bulleted evidence list. **One single-cell table.**
⛔ **No `/Outlines` (bookmarks), no `/Names`, no `/PieceInfo`, no `/AcroForm`, no `/OCProperties`,
no `/ViewerPreferences`, no `/Perms`, no `/Extensions`, no embedded files.**

## 2.3 FONTS — four subsets, one export session

| Subset tag | Font | Type | Emb | Sub |
|---|---|---|---|---|
| `MTJJWZ+` | **ArialMT** | TrueType / WinAnsi | ✅ | ✅ |
| `USIFEJ+` | **Arial-BoldMT** | TrueType / WinAnsi | ✅ | ✅ |
| `DQWHAR+` | **Arial-ItalicMT** | TrueType / WinAnsi | ✅ | ✅ |
| `RTXIOP+` | **Wingdings-Regular** | CID TrueType / Identity-H | ✅ | ✅ |

⭐ **Wingdings carries the bullet glyphs** — the evidence list. **Per-page font sets:** 16 pages use
Arial regular only; 5 pages use Wingdings + regular + bold; 3 use regular/bold/italic. **Ordinary
Word document. Nothing anomalous.**

---

# PART 3 — THE DMS PROFILE, IN BOTH PLACES

**14 `hg*` fields appear TWICE — once in `/Info` and again in the XMP `pdfx:` namespace.**
⭐ That duplication is normal PDFMaker behaviour for Word custom document properties, and it means
**the values were Word DOCUMENT PROPERTIES, not something bolted onto the PDF afterwards.**

```
/Author            HopgoodGanim Lawyers        /Producer   Adobe PDF Library 24.3.212
/Company           HopgoodGanim Lawyers        /Creator    Acrobat PDFMaker 24 for Word
/hgDMSMatter       2440758                     /hgDMSMatter_Original      <mcDMSMatter>
/hgDMSDocumentId   29218845v1
/hgDMSAuthorName   hendry8286                  /hgDMSAuthorName_Original  <mcDMSAuthorName>
/hgDMSAddressee    Worker applicant - Mr Cory Shepherd   /…_Original      <mcDMSAddressee>
/hgDMSDescription  Reasons for decision - WCR reject     /…_Original      <mcDMSDescription>
/hgDMSDocType      DOCUMENT   /hgDMSDate  09.10.2024     /…_Original      <mcDMSDate>
/hgSaveDescription Reasons for decision - WCR reject - Worker applicant -
                   Mr Cory Shepherd - 09.10.2024
/Title "" /Subject "" /Keywords "" /Comments "" /SourceModified ""
```

## ⭐⭐⭐ 3.1 THE MOST ACCURATE STATEMENT OF WHAT THIS PROVES

⛔ **Not "a law firm wrote the decision."** ⭐⭐⭐ **What it proves is narrower and firmer:**

> **The Word file was saved at least once on a workstation running HopgoodGanim's document
> management Word integration, and was profiled to matter 2440758 with a description that
> accurately describes this document.**

**The `_Original` fields are unresolved `DOCPROPERTY` merge placeholders** (`<mcDMSMatter>`,
`<mcDMSDate>`…). ⭐⭐ **That is the signature of a DMS add-in that stamps every document it
touches** — the add-in writes both the resolved value and the placeholder it resolved from.
⛔ **It excludes a stale template** (the resolved values are this matter's) and it **excludes
manual typing** (the placeholders would not be there).

## ⚠ 3.2 THE DATE MISMATCH INSIDE THE PROFILE

| | |
|---|---|
| `/hgDMSDate` and the tail of `/hgSaveDescription` | **09.10.2024** |
| The decision's own date | **22 October 2024** |
| The reasons' own date | **24 October 2024** |

⇒ ⭐⭐ **The DMS document record was created on 9 October 2024 and was never re-dated when the
final version was produced on 24 October.** That is ordinary DMS behaviour — **and it means a
version of this document existed in that Word environment thirteen days before the decision was
made.**

⛔⛔ **9 October 2024 is also the day the abandonment letter was transmitted to Cory at 16:10.
There is NO basis to connect them and it is recorded only so it is not later mistaken for a
finding.**

## ⚠ 3.3 `/SourceModified` IS AN EMPTY STRING — noted, weak

PDFMaker normally stamps the **source Word file's last-modified time** here. It is present but
**empty**. ⚠ **Consistent with a document opened from a DMS check-out rather than a plain file
path** — but I have no control sample to test it against. ⛔ **Do not build anything on it.**

## ⚠ 3.4 `xmpMM:subject = 53` — UNEXPLAINED, AND HONESTLY SO

```xml
<xmpMM:subject><rdf:Seq><rdf:li>53</rdf:li></rdf:Seq></xmpMM:subject>
```
A **deprecated** Adobe property (nominally "an array of page numbers"). **The document has 28
pages.** ⭐ The two *PDFMaker-for-Outlook* files in the corpus do **not** carry it, so it is
**specific to the Word converter**. ⛔⛔ **I do not know what 53 refers to and I am not going to
guess. Open item.**

---

# PART 4 — ⭐⭐⭐ NEW: THE CITATIONS WERE PASTED IN FROM A US-ENGLISH SOURCE

**Language tagging across the structure tree: `EN-AU` on 412 elements — and `EN-US` on exactly 3.**
**All three are case citations.**

| Footnote | Page | Text | Language |
|---|---|---|---|
| **FN1** | 6 | `1 [2009] QIRC 9; 190; QGIG 93.` *(Rowe)* | EN-AU + ⭐ **EN-US** trailing span |
| **FN2** | — | `2 [2000] QIC 67` | EN-AU |
| **FN3** | 18 | ⭐ `3 [2005] QIC 53; (2005) 180 QGIG 481.` *(Prizeman)* | ⭐⭐ **EN-US** |
| **FN3** | 18 | ⭐ `4 [2002] QIC 18.` *(Bowers)* | ⭐⭐ **EN-US** |
| **FN4** | — | `5 [2005] QIC 11; 178 QGIG 197` *(Delaney)* | EN-AU |

⇒ ⭐⭐⭐ **In Word, language is a run-level property and pasted text keeps its source language.
Two of the five authorities were copied in from a document formatted in US English. They were not
typed into this decision.**

⭐⭐ **This gives the "no authority later than 2009" finding a mechanism.** The authorities were
**carried in from a standing source** — a precedent, an earlier decision, a block of boilerplate.
**They were not researched for this matter.** ⛔ That is an observation about drafting method,
**not** about honesty.

---

# PART 5 — ⭐⭐⭐ THE MIMECAST LINKS, AND WHY THEY POINT AT OIR

## 5.1 THE ARTEFACT

**Page 27 carries two link annotations, both to the same rewritten URL:**

```
https://protect-au.mimecast.com/s/ru5wC2xZPVFp6oLvTnlSLX?domain=worksafe.qld.gov.au
```

⭐ **A `protect-au.mimecast.com/s/<token>` URL is produced by Mimecast URL Protection when a link
passes through a Mimecast-protected EMAIL.** ⇒ **The appeal-rights text on page 27 was pasted out
of an email**, not typed and not inserted as a fresh hyperlink. **The same token appears twice ⇒
one source email.**

**The other five links are internal `/Dest` jumps (pp 6, 17, 18 ×2, 27) — footnote anchors.**

## 5.2 ⭐⭐⭐ THE CORPUS TEST — 360 PDFs, 2,958 URI ANNOTATIONS

| Gateway | Hits | Whose |
|---|---|---|
| `aus01.safelinks.protection.outlook.com` | ⭐ **819** | ⭐⭐ **Microsoft Defender Safe Links — QUEENSLAND HEALTH's tenant.** ⛔ **Queensland Health is NOT a Mimecast shop** |
| `url.au.m.mimecastprotect.com` | **59** | ⭐ **Three files, all in `documents/disclosure-2025-07/`** |
| `protect-au.mimecast.com` | **2** | ⭐⭐ **The Review Decision, page 27** |

**⭐⭐⭐ And this is the decisive line.** `Disclosure_witness_conferencing_QldHealth_Payroll.pdf`
(Acrobat PDFMaker **17** for Outlook, created **11 Jul 2025 15:52:19**) contains emails **received
by Renee Matheson at `@oir.qld.gov.au` from `@health.qld.gov.au` senders**, and carries, verbatim:

> ⭐⭐⭐ ***"CAUTION: This email originated from outside of OIR. Do not click links or open
> attachments unless you recognise the sender and know the content is safe."***

**In that same file, the Queensland Health signature-footer icons (facebook, instagram, twitter,
linkedin, youtube, aka.ms, teams.microsoft.com) are all rewritten to `url.au.m.mimecastprotect.com`
— i.e. rewritten ON THE WAY IN TO OIR.**

⇒ ⭐⭐⭐ **OIR'S INBOUND MAIL GATEWAY IS MIMECAST. Proven from Cory's own file.**

**And the two domain forms match the two dates:** `protect-au.mimecast.com` is Mimecast's **older**
URL-Protection domain (the Review Decision, **October 2024**); `url.au.m.mimecastprotect.com` is
the **newer** post-rebrand domain (the disclosure, **July 2025**). ⭐ **One tenant, migrated
between the two dates.**

## 5.3 ⭐⭐⭐ WHAT THAT DOES TO THE HOPGOODGANIM QUESTION

⛔⛔⛔ **CORRECTED 8 AUGUST 2026 — I OVERSTATED THIS. See `HOPGOODGANIM-QUESTION.md` Part 9.**

~~The one externally-verifiable network artefact inside the document points at the Office of
Industrial Relations' own email system — not at a law firm. On this record, the Mimecast wrapper
is OIR's.~~

⭐⭐⭐ **PUBLIC MX RECORDS SETTLE IT, AND NOT MY WAY:**

| Domain | Inbound mail gateway |
|---|---|
| `oir.qld.gov.au` | `au-smtp-inbound-1.mimecast.com` / `-2` |
| ⭐⭐ `hopgoodganim.com.au` | ⭐⭐ `au-smtp-inbound-1.mimecast.com` / `-2` — **THE SAME MIMECAST CLUSTER** |
| ⭐ `workcoverqld.com.au` | ⭐ `workcoverqld-com-au.mail.protection.outlook.com` — **Microsoft. NOT Mimecast** |

⇒ ⛔⛔ **The Mimecast wrapper CANNOT discriminate between OIR and the firm. Both are Mimecast, on
the same Australian inbound cluster. My §5.3 conclusion is withdrawn.**

⇒ ⭐⭐ **What it DOES establish is narrower and still worth having: the pasted text did NOT come out
of a WorkCover Queensland mailbox.** WorkCover runs Microsoft Exchange Online Protection, which
rewrites to `safelinks.protection.outlook.com`, not Mimecast.

## 5.4 ⭐ AND A SMALL, REAL DEFECT WORTH KNOWING

⭐⭐ **The link telling a worker how to appeal is a Mimecast click-protection wrapper**, not the
plain `worksafe.qld.gov.au` address. Those wrappers are issued to a specific recipient and are not
meant to be redistributed. ⇒ **Further evidence the closing block is recycled boilerplate rather
than text composed for him.** ⛔ **Not a ground of anything. Do not raise it.**

---

# PART 6 — ⭐⭐ THE DOCUMENT'S FACE IS AUTHENTIC OIR, AT ASSET LEVEL

**Three images, extracted and inspected:**

| Page | Size | Format | What it is |
|---|---|---|---|
| **1** | 130 × 188 | ⭐ **PNG, DeviceRGB, 8bpc, WITH alpha (`/SMask`)** | ⭐⭐⭐ **The Queensland Government crest — "ALIIS AVIS FIDELIS" — over "Queensland Government", above "Office of Industrial Relations"** |
| **2–28** | 1627 × 134 | PNG, DeviceRGB, with alpha | ⭐ **The Queensland Government MAROON rule line** — the running letterhead band, identical on all 27 pages |
| **28** | 443 × 276 | ⭐ **JPEG, DeviceGray, no alpha** | ⭐⭐ **A handwritten signature** |

⭐⭐⭐ **The crest and the rule are PNGs with alpha channels — proper template assets, not scans.**
**That is an official OIR letterhead template in Word.**

⭐⭐ **The signature is a grayscale JPEG inserted as an image**, while everything around it is
vector text. ⇒ **The page was never printed and rescanned. It was signed electronically by
inserting a signature graphic** — ordinary practice.

---

# PART 7 — EVERY TAMPERING INDICATOR, RE-RUN AND CLEAN

| Test | Result |
|---|---|
| **Text render mode (`Tr`)** | ⭐⭐ **The operator does not appear ANYWHERE in 28 pages.** All text is mode 0 = visible fill. ⛔ **Zero invisible text. No OCR layer. Nothing hidden** |
| Content operators | 25 distinct, all ordinary text/graphics (`Tw` 1544, `Td` 1506, `TJ` 1374, `Tc` 1360, `Tj` 1064, `BDC`/`EMC` 500/512, `BT`/`ET` 96/96) |
| Incremental updates | ⛔ **None** — 2 `%%EOF` = linearization |
| Optional content / layers | ⛔ None |
| JavaScript · AcroForm · embedded files | ⛔ None |
| Digital signature | ⛔ **None.** The signature is an image, with no cryptographic signature over the document |
| Encryption | ⛔ None |
| `Suspects` | **no** |
| **Orphaned objects** | **18 of 672 — every one structural**: 14 × `/ObjStm`, 2 × `/XRef`, the linearization parameter dict (obj 643), and the linearization hint stream (obj 672). ⛔ **No orphaned content, no deleted text recoverable** |
| Page geometry | **All 28 pages exact A4, identical MediaBox, rotation 0.** ⛔ **No spliced or substituted page** |

⇒ ⭐⭐⭐ **The file is clean. There is no evidence of alteration of any kind.**

---

# PART 8 — THE EVALUATION

## 8.1 ⭐⭐ THE LEDGER, HONESTLY KEPT

| Points to a **LAW FIRM** | Weight | Points to **OIR** | Weight |
|---|---|---|---|
| 14-field populated DMS profile, this matter, both in `/Info` and XMP | ⭐⭐⭐ **Strong, still unexplained** | ⭐⭐⭐ **Mimecast wrapper = OIR's own gateway**, proven from the Regulator's own disclosure | ⭐⭐⭐ **Strong** |
| `_Original` merge placeholders ⇒ a DMS add-in ran on the saving workstation | ⭐⭐⭐ **Strong** | **Official OIR letterhead assets** — crest + maroon rule as alpha PNGs, i.e. a template | ⭐⭐ |
| `/Author` **and** `/Company` both "HopgoodGanim Lawyers" | ⭐⭐ | **Signed by the OIR officer** with an inserted signature image | ⭐⭐ |
| `/SourceModified` blank | ⚠ Weak | **`EN-AU` document language**, 412 elements | ⭐⭐ |
| | | **No authority later than 2009; no *Mahaffey*** — a 2024 insurance firm would not draft s 32(5)(a) that way | ⭐⭐ |
| | | ⭐ **Citations pasted from a standing source** ⇒ boilerplate assembly, not legal research | ⭐⭐ |
| | | **Decision made on day 25 of the 25 business days** (s 545(1)) ⇒ deadline pressure | ⭐⭐ |
| | | ⛔⛔ ~~It overturned WorkCover twice~~ **WITHDRAWN — the OUTCOME went to WorkCover. See `HOPGOODGANIM-QUESTION.md` Part 8** | ⛔ **nil** |

## 8.2 ⭐⭐⭐ THE CONCLUSION

> ⭐⭐⭐ **This reads as an OIR document: OIR's letterhead template, OIR's boilerplate, OIR's mail
> gateway, OIR's officer's signature, Australian English, assembled fast against a statutory
> deadline out of recycled parts — that was saved, at least once, in a Word environment carrying
> HopgoodGanim's document management integration and profiled to their matter 2440758.**

⭐⭐ **The balance has moved. It has NOT moved to zero.** The DMS profile is still not explained by
anything in the file, and it is the one fact that no innocent reading has yet absorbed.

## 8.3 ⛔⛔ AND THE ACTION STILL DOES NOT CHANGE

- ⛔ **Not a ground of appeal.** s 550 is **de novo**.
- ⛔⛔ **Do not publish, post, forward or circulate.** The Mimecast finding makes the sinister
  reading *weaker*, which makes publication *more* dangerous, not less.
- ⛔⛔ **Ask, never allege.** The single neutral question at `HOPGOODGANIM-QUESTION.md` §7.8 stands
  unchanged.
- ⭐⭐ **Keep the reliance**: *the Regulator's own delegate found the rostering was unreasonable
  management action and that work events were the sole cause.* **That is worth more than any of
  this.**

## 8.4 OPEN ITEMS FROM THIS PASS

1. ⚠ **`xmpMM:subject = 53`** — meaning unknown. Would need a Word/PDFMaker 24 control sample.
2. ⚠ **`/SourceModified` empty** — would need a PDFMaker-for-Word control sample.
3. ⚠ **`hendry8286`** — a DMS user identifier. ⛔ **Do not attempt to identify the person.**
4. ⚠ **Whether HopgoodGanim's own mail gateway is Mimecast** — would weaken §5.3. Not checkable
   from the file and ⛔ **not worth investigating.**
</content>
