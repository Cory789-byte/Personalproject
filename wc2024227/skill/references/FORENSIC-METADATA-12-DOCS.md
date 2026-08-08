# FORENSIC METADATA — the twelve documents, 8 August 2026
> Tools: `exiftool 12.76` (all tags, all groups) · `pdfinfo` · `qpdf --qdf` raw XMP · SHA-256 ·
> revision counting via `%%EOF` / `startxref`.
> ⛔ **Contains one serious finding. Read Part 2 in full before acting on any of it.**

---

# PART 1 — THE TABLE

| Document | Creator / Producer | Created (AEST) | Author / Company | Revs |
|---|---|---|---|---|
| **Att 1** — AVAC 09 Feb–01 Apr 2024 | **KONICA MINOLTA bizhub C300i** | **28 May 2024 08:01** · ⚠ **mod 6 Sep 08:36** | — | **2** |
| **Att 2** — Validation of Claim | **KONICA MINOLTA bizhub C300i** | **28 May 2024 08:02** | — | 1 |
| **Att 3** — LM addressing pay concerns | Acrobat PDFMaker 24 **for Outlook** | **6 Sep 2024 08:37** | — | 1 |
| **Att 4** — Roster 4–31 Mar 2024 | **KONICA MINOLTA bizhub C300i** | **4 Sep 2024 09:20** | — | 1 |
| **Att 5** — Full-time appointment | Acrobat PDFMaker 24 **for Outlook** | **6 Sep 2024 09:34** | — | 1 |
| **Att 6** — Email 3, rostering concerns | **Microsoft: Print To PDF** | **23 Aug 2024 12:46** | ⭐ **Cory Shepherd** | 1 |
| **Att 7** — Reese re ESU outcome | **KONICA MINOLTA bizhub C300i** | **5 Sep 2024 11:58** | — | 1 |
| **Att 8** — Change Management Guideline | PScript5.dll / Distiller 9.2.0 | **14 Sep 2018** | **Employment Relations** | 2 |
| **LTR** — Employer Response 6 Sep 2024 | **PDFTron office converter 7.1.0** · **PDF/A-2U** | **6 Sep 2024 13:26** | *(blank)* | 1 |
| **ICD03** | ⭐ **Windward Studios 20.0.0.106**, JVM 11, **Windows Server 2016** | **13 Sep 2024 16:59** | Windward Reports *(system)* | 1 |
| **WCRS Attachment 18.8.2022** | Acrobat PDFMaker 15 for Word | **18 Aug 2022 11:40** | ⭐ **DJAG** · `Angela.Sense@oir.qld.gov.au` | 2 |
| ⛔ **Review Decision 69983 — ORIGINAL** | **Acrobat PDFMaker 24 for Word** / Adobe PDF Library 24.3.212 | **24 Oct 2024 10:16:52 → 10:17:01** | ⛔⛔ **HopgoodGanim Lawyers** | 2 |

---

# PART 2 — ⛔⛔⛔ THE REVIEW DECISION: A FULL LAW-FIRM DMS PROFILE

**The original PDF — not his handling copy — carries these embedded custom fields:**

```
Author                : HopgoodGanim Lawyers
Company               : HopgoodGanim Lawyers
HgDMSMatter           : 2440758
HgDMSDocumentId       : 29218845v1
HgDMSAuthorName       : hendry8286
HgDMSAddressee        : Worker applicant - Mr Cory Shepherd
HgDMSDescription      : Reasons for decision - WCR reject
HgDMSDocType          : DOCUMENT
HgDMSDate             : 09.10.2024
HgSaveDescription     : Reasons for decision - WCR reject - Worker applicant -
                        Mr Cory Shepherd - 09.10.2024
Creator / CreatorTool : Acrobat PDFMaker 24 for Word
Created               : 2024-10-24 10:16:52 +10:00
Modified              : 2024-10-24 10:17:01 +10:00   (9 seconds later)
DocumentID            : uuid:35737479-d76b-4ec6-8357-3fa8772f432d
InstanceID            : uuid:63cfab6f-dcc1-48c7-8a10-5d7ee2ddf94b
```

**`Hg` = HopgoodGanim. `DMS` = document management system.** The paired `_Original` fields contain
unpopulated merge placeholders (`<mcDMSAddressee>` etc.) — **the profiling add-in's field
templates.**

## 2.1 ⛔ THIS EXCLUDES THE "STALE TEMPLATE" EXPLANATION

**Earlier today I assessed the Author string as most likely a stale template artefact. ⛔ That
assessment is now wrong and is withdrawn.**

⭐⭐⭐ **A stale template carries a stale name. It does not carry a matter number, a document ID, a
user ID, an addressee naming this worker, and a description naming this decision.** **The fields
are populated with this matter's specifics.**

## 2.2 ⭐⭐⭐ THE CONTROLLED COMPARISON — an authentic OIR document looks completely different

| | **WCRS Attachment, 18 Aug 2022** | **Review Decision, 24 Oct 2024** |
|---|---|---|
| **Company** | ⭐ **Department of Justice and Attorney-General** | ⛔ **HopgoodGanim Lawyers** |
| **Author** | Microsoft Office User | ⛔ **HopgoodGanim Lawyers** |
| **Author email tag** | ⭐ **`Angela.Sense@oir.qld.gov.au`** | — |
| **Other custom fields** | SharePoint `ContentTypeId`, `BusinessUnit`, `LandingPage` | ⛔ **A law firm's DMS profile** |

⇒ ⭐⭐⭐ **A genuine WCRS/OIR document carries DJAG, an @oir.qld.gov.au author, and SharePoint
fields. This decision carries a private firm's DMS profile.**

## 2.3 WHAT IS ESTABLISHED — and what is NOT

**Established, from the file:**
1. The PDF was produced by **Acrobat PDFMaker 24 for Word at 10:16:52 AEST on 24 October 2024**,
   finalised **9 seconds later** — a clean single-pass export.
2. **The source Word document carried HopgoodGanim's DMS profile, populated with this matter.**
3. An authentic OIR comparison document carries entirely different metadata.

**⛔⛔ NOT established — and he must not assert any of it:**
- **Who wrote the reasoning.**
- **Whom HopgoodGanim acted for** — the Regulator, WorkCover, or MSH.
- **What `hendry8286` did.**
- **What `HgDMSDate 09.10.2024` refers to** — it may be a matter or document-opening date, not a
  drafting date.
- **Whether anything improper occurred.**

⭐ **And there are lawful explanations.** A regulator may obtain external legal advice on a
difficult review, or engage assistance in preparing reasons. **The delegate remains the
decision-maker, and that is not unlawful.**

## 2.4 ⭐⭐⭐ THE STRATEGIC POINT — he benefits either way, and needs no allegation

**If the decision was prepared with external legal input, the favourable findings in it become
STRONGER, not weaker:**
- *"I am satisfied your employment was a significant contributing factor"*;
- *"factor 4 amounted to unreasonable management action"*;
- Dr Hawes recorded as saying **work events were the sole cause**, with **no pre-existing factor**.

⇒ ⭐⭐ **Findings like those, in a document prepared with legal input on the Regulator's own side,
are very hard to walk away from.** **He does not need impropriety. He is better off either way.**

## 2.5 ⛔⛔ WHAT TO DO — one neutral request, and nothing else

**Send this, and only this:**

> *"Please identify the role, if any, of HopgoodGanim Lawyers in the preparation of Review Decision
> 69983, and produce any related correspondence. Please also provide a copy of the decision as
> issued."*

**Why this and nothing else:**
- ⭐ **It is an ordinary question.** Asking who prepared a document alleges nothing.
- ⭐⭐ **It preserves the "their own delegate found for me" argument** — his best settlement asset.
- ⭐ **It answers itself.** They explain it, or they do not.
- ⛔ **It avoids *Briginshaw*, s 32(5)(b), s 32(5)(c), the vexatious characterisation, and any
  merging with the quarantined reprisal complaint.**

**⛔⛔ AND THE HARD LIMITS:**
1. ⛔ **The appeal is de novo. This cannot be a ground of appeal** — whatever the answer, the
   Commission decides afresh. **That has not changed.**
2. ⛔⛔ **Do not publish, post, forward or circulate this.** Naming a law firm in connection with a
   suggestion of impropriety, outside a proceeding, carries real defamation exposure. **File and
   disclosure request only.**
3. ⛔ **Do not allege. Ask.** The difference is the whole of his protection.

---

# PART 3 — ⭐⭐⭐ THE SCANNER CHAIN: safe, and genuinely valuable

**Four documents came off the same device — a `KONICA MINOLTA bizhub C300i` — and the Title field
encodes the scan timestamp:**

| Title | Decodes to | Document |
|---|---|---|
| `SKM_C300i` **24052808010** | ⭐ **2024-05-28, 08:01** | **Att 1 — the AVAC** |
| `SKM_C300i` **24052808020** | ⭐ **2024-05-28, 08:02** | **Att 2 — Validation of Claims** |
| `SKM_C300i` **24090409190** | 2024-09-04, 09:19 | Att 4 — the roster |
| `SKM_C300i` **24090511580** | 2024-09-05, 11:58 | Att 7 — Reese re ESU |

## ⭐⭐⭐ THE FINDING

**The AVAC and the Validation of Claims form were scanned ONE MINUTE APART, at 08:01 and 08:02 on
28 May 2024 — the very day the AVAC was submitted.**

⭐⭐ **Form 24 ¶41 admits the AVAC was submitted 28 May 2024, a 25-day delay after the 3 May
payroll instruction. The scanner has now pinned it to the minute, from the employer's own
device.**

⇒ ⭐ **Independent, device-generated, entirely safe corroboration.** **Use this. It requires no
allegation about anyone.**

⚠ **And Att 1 has TWO revisions** — modified **6 September 2024 at 08:36 AEST**, i.e. re-saved when
the employer assembled its response pack.

---

# PART 4 — THE EMPLOYER'S 6 SEPTEMBER 2024 RESPONSE PACK, ASSEMBLED IN FIVE HOURS

| Time (AEST) | Event |
|---|---|
| **08:36** | Att 1 (AVAC scan) re-saved |
| **08:37** | Att 3 created — **Acrobat PDFMaker for Outlook** |
| **09:34** | Att 5 created — same tool |
| **13:26** | **LTR — the covering letter** — **PDFTron converter, PDF/A-2U** |

⭐⭐ **Two different pipelines.** The attachments were converted from **Outlook by Acrobat**; ⭐ **the
covering letter came out of a records/document-management platform (PDFTron, PDF/A conformant)** —
not from a person's mailbox.

⇒ **The pack was built between 08:36 and 13:26 on 6 September 2024.**

---

# PART 5 — THE REMAINING DOCUMENTS

| Document | Finding |
|---|---|
| ⭐ **ICD03** | **Windward Studios**, JVM 11, **Windows Server 2016** — ⭐⭐ **system-generated from a claims platform** at **16:59 AEST, 13 September 2024**. **That is the date of WorkCover's rejection decision** ⇒ an automated attachment to it |
| ⭐ **Att 6** | **Author "Cory Shepherd"**, *Microsoft: Print To PDF*, *"Mail - Cory Shepherd - Outlook"* — **his own document, from his own mailbox**, 23 Aug 2024 12:46 |
| **Att 8** | **Author "Employment Relations"**, Distiller 9.2.0, **14 September 2018** — a Queensland Health corporate guideline, six years old at the time of the events |
| **WCRS 18.8.2022** | ⭐ **The authenticity benchmark** — DJAG, `Angela.Sense@oir.qld.gov.au`, SharePoint fields. **This is what an OIR document's metadata looks like** |

---

# PART 6 — THE PRIORITY ORDER

| | Finding | Use |
|---|---|---|
| **1** | ⭐⭐⭐ **The 08:01 / 08:02 scanner timestamps on 28 May 2024** | ⭐ **Deploy freely.** Device-generated corroboration of the admitted 25-day delay |
| **2** | ⭐⭐ **The 6 September pack assembly window** | Context; shows the response was compiled in one morning |
| **3** | ⭐ **ICD03 is system-generated** | Explains a document nobody had classified |
| **4** | ⛔⛔ **The HopgoodGanim DMS profile** | ⭐ **ONE neutral disclosure request (§2.5). Nothing else. No allegation, no publication, and it is not a ground of appeal** |

---

# PART 7 — DEEP EXTRACTION (pikepdf 10.10.0 / qpdf, object level)
> 8 August 2026. Everything above used exiftool and pdfinfo. **This part goes to the object
> structure, the raw dictionaries, the images, and the tampering indicators.**

## 7.0 ⛔ CORRECTION FIRST

**Part 1 recorded the Review Decision as having "2 revisions".** ⛔ **That was wrong.** The two
`%%EOF` markers are an artefact of **linearisation** (`/Linearized 1`, a 491-byte first-page stub).

⇒ ⭐ **There is NO incremental save and NO earlier revision hiding in the file. It is a
single-generation export.**

## 7.1 THE RAW `/Info` DICTIONARY — 25 fields, verbatim

```
/Author              HopgoodGanim Lawyers      /Producer     Adobe PDF Library 24.3.212
/Company             HopgoodGanim Lawyers      /Creator      Acrobat PDFMaker 24 for Word
/CreationDate        D:20241024101652+10'00'   /ModDate      D:20241024101701+10'00'
/Title /Subject /Keywords /Comments /SourceModified   — all empty
/hgDMSMatter         2440758        /hgDMSMatter_Original      <mcDMSMatter>
/hgDMSDocumentId     29218845v1
/hgDMSAuthorName     hendry8286     /hgDMSAuthorName_Original  <mcDMSAuthorName>
/hgDMSAddressee      Worker applicant - Mr Cory Shepherd   /…_Original <mcDMSAddressee>
/hgDMSDescription    Reasons for decision - WCR reject     /…_Original <mcDMSDescription>
/hgDMSDocType        DOCUMENT       /hgDMSDate  09.10.2024  /…_Original <mcDMSDate>
/hgSaveDescription   Reasons for decision - WCR reject - Worker applicant -
                     Mr Cory Shepherd - 09.10.2024
```

## 7.2 ⭐⭐⭐ THE `_Original` FIELDS ARE WORD MERGE-FIELD PLACEHOLDERS

Every `hgDMS*` field is paired with an `_Original` holding an **unresolved token** — `<mcDMSMatter>`,
`<mcDMSAddressee>`, `<mcDMSAuthorName>`, `<mcDMSDate>`, `<mcDMSDescription>`, `<mcDMSDocType>`.

⭐⭐⭐ **Those are DOCPROPERTY / merge fields in a Word template. The pairing shows the template's
placeholder AND the value the document management system substituted.**

⇒ ⛔⛔ **This is not a stale author string surviving in a template. It is a firm's document
automation resolving merge fields against matter 2440758.** **The "stale template" explanation is
now excluded twice over.**

## 7.3 ⭐⭐⭐ AND THE COUNTERWEIGHT — THE DOCUMENT'S FACE IS AUTHENTIC

**Images extracted from the file:**

| Page | Image | What it is |
|---|---|---|
| **1** | 130×188 PNG | ⭐⭐⭐ **The Queensland Government crest with *"Office of Industrial Relations"*** |
| **2–28** | 1627×134 JPEG, identical on every page | The running OIR banner |
| **28** | 443×276 greyscale JPEG | ⭐⭐ **A handwritten signature** |

⇒ ⭐⭐⭐ **Everything VISIBLE about the document is authentic Office of Industrial Relations. The
letterhead is genuine and it is signed. Only the invisible file metadata carries the firm.**

**That has to be given full weight. It is the strongest single fact against the alarming reading.**

## 7.4 ⭐ EVERY TAMPERING INDICATOR IS CLEAN

| Test | Result |
|---|---|
| **Invisible text** (`3 Tr` render mode) | ⭐ **0 operators, on 0 pages** |
| **Optional content / layers** (`/OCProperties`) | ⭐ **None** |
| **JavaScript** | ⭐ **None** |
| **AcroForm / form fields** | ⭐ **None** |
| **Embedded files / attachments** | ⭐ **None** |
| **Annotations** | 7 (links) |
| **Orphaned objects** | **18 — every one structural** (linearisation xref and object-stream leftovers). ⭐ **No deleted content survives** |
| **Digital signature** | ⚠ **None. The signature is an IMAGE** — the file is not cryptographically signed |

⇒ ⭐⭐ **The document has not been altered, redacted over, layered, or tampered with in any way. It
is a clean single-pass export from Word.**

⚠ **One consequence worth noting: because it is not digitally signed, its integrity rests entirely
on provenance** — which is precisely why the *"provide the decision as issued"* request matters.

## 7.5 FONT SUBSET FINGERPRINT — this specific export session

`MTJJWZ+ArialMT` · `USIFEJ+Arial-BoldMT` · `RTXIOP+Wingdings-Regular` · `DQWHAR+Arial-ItalicMT`

⭐ **Subset prefixes are randomly generated per export.** They identify **this export session
uniquely**, and would match any other PDF produced in the same session. **Recorded as a
fingerprint; nothing to compare it against yet.**

## 7.6 IMAGE-HASH COMPARISON ACROSS THE REGULATOR SET

| Finding | |
|---|---|
| ⭐ **The 2025 and 2026 Regulator SOFCs share 13 identical images** | Same QIRC Form 9C template, a year apart — **template continuity confirmed** |
| ⭐ One 169×71 image shared between the 2026 SOFC and the Form 24 Response | Both Regulator filings — expected |
| ⚠ **The Review Decision's three images appear in no other document** | ⛔ **INCONCLUSIVE — and it must be reported as such.** There is **no other OIR letterhead *letter*** in the set to compare against. The SOFCs are QIRC forms; the disclosure is a scan pack. **Different document types entirely** |

## 7.7 ⭐⭐⭐ WHAT THE DEEP EXTRACTION ACTUALLY CHANGED

**It made the picture MORE nuanced, not more alarming. Both columns are now established:**

| ⇒ Toward the firm's involvement being real | ⇒ Against the alarming reading |
|---|---|
| The DMS fields are **populated merge fields**, not stale properties | ⭐⭐⭐ **The letterhead is the genuine Queensland Government / OIR crest** |
| **Three identity fields** — Author, Company, `dc:creator` — all name the firm | ⭐⭐ **The decision bears a handwritten signature** |
| A **matter number**, a **document ID (v1)**, a **user ID**, an **addressee** and a **description** | ⭐⭐⭐ **It overturned WorkCover twice, against WorkCover** |
| **`hgDMSDate 09.10.2024`** — 15 days before the reasons | ⭐⭐ **The file is forensically clean** — no hidden text, no layers, no deleted content |

⇒ ⭐⭐⭐ **BEST SYNTHESIS, and it is where the evidence actually lands:**
> **The document was produced through a law firm's document management system, and it presents as
> an authentic Office of Industrial Relations decision. Both are true. The metadata cannot tell you
> who wrote the reasoning.**

⛔⛔ **The action is unchanged: ONE neutral disclosure request. No allegation. No publication.**
(`HOPGOODGANIM-QUESTION.md` §4.4.)
