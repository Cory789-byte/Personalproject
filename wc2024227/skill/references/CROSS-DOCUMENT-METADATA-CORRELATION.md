# CROSS-DOCUMENT METADATA CORRELATION — 359 PDFs, repo + uploads
> 8 August 2026. `exiftool 12.76` batch extraction across every PDF in the repository and the
> upload set. Looking for **fingerprints shared between sources that should be independent**, and
> **authors that do not match a document's purported origin**.

---

# ⭐⭐⭐ THE HEADLINE

**Across 359 documents there is exactly ONE cross-source anomaly — and it is the one already
found.**

⭐⭐ **Everything else in the corpus matches its purported source.** That cuts both ways:
- **The corpus is clean.** No hidden metadata linkage between MSH, WorkCover and the Regulator.
- ⇒ ⭐⭐⭐ **Which makes the Review Decision's anomaly stand out MORE, not less. It is not part of a
  pattern of sloppy metadata. It is the only one.**

---

# PART 1 — ⭐⭐⭐ THE DMS FIELDS APPEAR ON EXACTLY ONE DOCUMENT

**Tested every PDF for `HgDMSMatter`, `HgDMSAuthorName`, `HgDMSDescription`:**

| File | Matter | Author | Description | Company |
|---|---|---|---|---|
| **`Review_Decision_69983.pdf`** | **2440758** | **hendry8286** | **Reasons for decision - WCR reject** | **HopgoodGanim Lawyers** |

**Nothing else. Not one MSH production. Not one WorkCover document. Not one Regulator pleading.**

⇒ ⭐⭐⭐ **Two consequences, and both matter:**
1. ⭐ **The firm's system did not touch MSH's disclosure or the Regulator's pleadings.** ⇒ **They
   were not MSH's lawyers on the production, and they were not the Regulator's general drafters.**
2. ⛔ **The single footprint is on the review decision itself** — the most important document in
   the matter.

---

# PART 2 — ⭐⭐ THE REGULATOR'S OWN FINGERPRINTS, AND THE ANOMALY

| Document | Author | Company |
|---|---|---|
| **Regulator SOFC** ×4 (2025 · 2026) | **QIRC** | ⭐ **Workers' Compensation Regulator** |
| **WCRS attachment to decision** (18 Aug 2022) | Microsoft Office User | ⭐ **Department of Justice and Attorney-General** |
| Regulator disclosure to Appellant (11 Jun 2026) | Microsoft Office User | — |
| Form 24 Response (18 Feb 2026) | ⚠ **"Stephen Gray"** | — |
| ⛔⛔ **Review Decision 69983** (24 Oct 2024) | **HopgoodGanim Lawyers** | ⛔ **HopgoodGanim Lawyers** |

⇒ ⭐⭐⭐ **Three distinct authentic Regulator/OIR fingerprints exist in the corpus — DJAG (2022),
Workers' Compensation Regulator (2025–26), and Microsoft Office User. The review decision matches
none of them.**

⚠ **HONEST GAP:** there is **no other 2024 Regulator document** in the corpus to compare directly.
The nearest are 2022 and 2025. ⭐ **Neither is a law firm.**

⚠ **"Stephen Gray"** — the Form 24 Response's PDF Author. **The name appears nowhere in the matter
record.** ⭐ Most likely a Regulator officer or a stale Word property. **Recorded for completeness;
not remarkable on its own.**

---

# PART 3 — ⭐⭐⭐ DEVICE ATTRIBUTION: THREE SCANNERS, THREE SOURCES

**This is the strongest safe finding in the whole correlation.**

| Device | Documents | ⇒ Source |
|---|---|---|
| ⭐⭐⭐ **KM_C300i** | Att 1 (AVAC) · Att 2 (Validation) · Att 4 (Roster) · Att 7 (Reese/ESU) — **the Sept 2024 WorkCover response pack** — **PLUS the 8 Sep 2025 Hughes attendance letter (the 34 occasions)** and the **Performance Plan initiation letter** | **METRO SOUTH HEALTH / Logan Hospital** |
| ⭐⭐ **KM_C658** | **Every directions order** (3 Jun 2025 · 16 Jul 2025 · 22 Aug 2025 · 7 Apr 2026) · **the sealed Form 29** · the **stamped Form 4 and affidavits** | **THE QIRC REGISTRY** |
| **KonicaC368e** | Our Medical Ashmore GP records via Saines | The practice / former solicitors |

## ⭐⭐⭐ THE FINDING — a match that IS legitimate, and that is why it is useful

**The same MSH device produced both:**
- **the attachments sent to WorkCover in September 2024** to defeat the compensation claim, **and**
- **the 8 September 2025 attendance letter** used against him on the employment track.

⇒ ⭐⭐ **One physical scanner links the compensation defence and the employment action.**

⛔ **This is NOT sinister — it is the Logan Hospital scanner.** ⭐⭐ **Its value is authentication:
it establishes the MSH document set as a single, verifiable provenance chain, and it lets any MSH
document be tested against the device fingerprint.**

⭐ **And the KM_C658 finding is separately useful:** it identifies **the Registry's own scanner**,
which authenticates sealed and stamped filings.

---

# PART 4 — SHARED DOCUMENT IDs (derivation links)

**Three genuine matches, all explicable — but one is worth acting on:**

| Shared ID | Files | Meaning |
|---|---|---|
| ⭐⭐ `uuid:195D99DC-…AD05` | **`2026-07-31_RFMI_Attachment2_AO3_Switchboard_Role_Description.pdf`** ↔ **`ATT14_AO3_Switchboard_Role_Description.pdf`** | ⭐⭐⭐ **The role description MSH attached to the 31 July 2026 RFMI is the IDENTICAL FILE already in the repo.** ⇒ **They re-sent a document he already held rather than a current one** |
| `uuid:beb98788-…` | The two Regulator SOFC copies | Same file, two filenames |
| `uuid:0c60ecfb-…` | 25 Feb affidavit ↔ 26 Feb stamped version | Stamped copy derived from the same source |

⚠ ⭐ **Act on the first one.** If MSH's RFMI relied on a role description that is **not current**,
that is directly relevant to the RFMI response and to the adjustments question.

---

# PART 5 — ⚠ ITEM 11: THE myHR AUDIT TRAIL IS AUTHORED BY MSH'S LAWYER

**Every Item 11 document MSH produced carries `Author: Myla Ruttan`:**
- `Item_11_myHR_report_Leave_submissions_Feb-May_2024.pdf`
- `Item_11_AVAC_PRN_15480560_History.pdf`
- `Item 11_Leave form PRN 15480560 Evidence pandemic leave.pdf`
- `Item 6 Role description Switchboard manager as at 2021.pdf`
- `2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf`

⇒ ⭐⭐ **The myHR audit trail is NOT a raw system export. It was saved through the employer's
solicitor.**

⚠ **This matters for the pending Item 11 verification** (`THE-FATIGUE-SEQUENCE.md` §13.5). It is
not fatal — a lawyer compiling a production is ordinary — ⛔ **but it means the COVID upload
timestamp is not self-authenticating, and "how was this generated?" is the first question if he
relies on it.**

⭐ **Better source available:** the **Review Decision p 24 already records the upload time as
20 February 2024** and that he showed her the declaration on his phone. **That recital is in the
Regulator's own decision and needs no MSH provenance at all.**

---

# PART 6 — EVERYTHING ELSE MATCHES ITS SOURCE

| Author | Documents | Verdict |
|---|---|---|
| **Chief Human Resources Officer** / **…, Queensland Health** | ATT09, ATT10, ATT13 — QH policies | ✅ Normal |
| **Employment Relations** | Change Management Guideline (2018) | ✅ Normal |
| **Office of the Queensland Parliamentary Counsel** ×11 | Authorised legislation | ✅ Normal |
| **Office of Industrial Relations** ×4 | Psychosocial Code of Practice 2022 | ✅ Normal |
| **QIRC** ×19 | Commission documents | ✅ Normal |
| **Katie Ketter** ×3 | RFMI authorisation form | ✅ MSH staff |
| **Jillian Apps** ×2 | QSuper complaint response | ✅ QSuper staff |
| **Myla Ruttan** ×7 | MSH objection + productions | ✅ MSH's lawyer |
| **Cory Shepherd** ×9 + **Cory L Shepherd** ×4 | His own filings and emails | ✅ His |
| **Windward Reports** | ICD03 | ✅ System-generated |

⭐ **No cross-party contamination anywhere else.**

---

# PART 7 — WHAT TO DO WITH THIS

| # | Finding | Action |
|---|---|---|
| **1** | ⭐⭐⭐ **KM_C300i links the Sept 2024 WorkCover pack to the Sept 2025 attendance letter** | ⭐ **Safe and useful.** Authenticates the MSH document set. **No allegation** |
| **2** | ⭐⭐ **The RFMI role description is an identical file to the one already held** | ⭐ **Raise it in the RFMI response** — was a current role description used? |
| **3** | ⚠ **Item 11 is authored by MSH's solicitor** | **Prefer the Review Decision p 24 recital** for the COVID upload timestamp |
| **4** | ⭐ **KM_C658 = the QIRC Registry scanner** | Authenticates sealed filings |
| **5** | ⛔⛔ **The HopgoodGanim DMS profile — one document, no pattern** | ⭐ **The single neutral disclosure request already drafted** (`HOPGOODGANIM-QUESTION.md` §4.4). **Nothing more. Do not publish. Do not allege** |

⭐⭐ **And note what the correlation did NOT find, because it matters: no shared identifiers between
MSH, WorkCover and the Regulator; no duplicated document IDs across parties; no evidence of any
document passing between opposing sides.** ⛔ **A single anomaly is not a network.**

---

# PART 8 — RESTRICTED TO THE INBOUND SET: what MSH, the Regulator and WorkCover sent HIM

> Everything below was **sent to him, about him**, by one of the three. His own documents,
> legislation and policies are excluded.

## 8.1 ⭐⭐⭐ THE COMPARISON, NOW CLEAN

| Document | From | Author | Company | Producer |
|---|---|---|---|---|
| Regulator SOFC (22 Jul 2025) | **Regulator** | **QIRC** | ⭐ **Workers' Compensation Regulator** | Adobe PDF Library **17.11.238** |
| Regulator SOFC (13 May 2026) | **Regulator** | **QIRC** | ⭐ **Workers' Compensation Regulator** | Adobe PDF Library 26.1.25 |
| Disclosure to Appellant (11 Jun 2026) | **Regulator** | Microsoft Office User | — | Adobe PDF Library **17.11.238** |
| WCRS attachment (18 Aug 2022) | **Regulator/WCRS** | Microsoft Office User | ⭐ **Dept of Justice and Attorney-General** | Adobe PDF Library 15.0 |
| Form 24 Response (18 Feb 2026) | **Regulator** | ⚠ **Stephen Gray** | — | Adobe PDF Library 25.1.192 |
| ICD03 (13 Sep 2024) | **WorkCover** | Windward *(system)* | — | Windward Studios |
| Employer response letter (6 Sep 2024) | **MSH** | *(stripped)* | — | **PDFTron office converter** |
| MSH objection (5 Jun 2026) | **MSH** | **Myla Ruttan** | — | Microsoft: Print To PDF |
| RFMI letter (31 Jul 2026) | **MSH** | — | — | Microsoft® Word 365 |
| ⛔⛔ **Review Decision 69983 (24 Oct 2024)** | **Regulator** | ⛔ **HopgoodGanim Lawyers** | ⛔ **HopgoodGanim Lawyers** | Adobe PDF Library 24.3.212 |

⇒ ⭐⭐⭐ **Of every document the Regulator or WorkCover has ever sent him, exactly ONE carries a
private law firm's identity — and it is the decision itself.**

⭐⭐ **And on that one the firm's name appears in THREE fields: `Author`, `Company`, and the XMP
`dc:creator`.** Not one stray property — the document's whole identity block.

⭐ **Note also the internal consistency of the genuine Regulator documents:** the 2025 SOFC and the
2026 disclosure share **Adobe PDF Library 17.11.238** — the same OIR pipeline, a year apart.

---

## 8.2 ⭐⭐⭐ NEW — THE MSH OBJECTION'S TITLE IS A LEAD

**`2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf` carries an embedded Title:**

> **`Attachment 4 Letter to Court response to Non production order Shepherd FINAL.PDF`**

**Four things fall out of that filename:**
1. ⭐⭐⭐ **"Attachment 4"** ⇒ **it was the fourth attachment to something larger. There are at least
   attachments 1, 2 and 3 that he has never seen.**
2. ⭐ **"Letter to Court"** ⇒ internally, MSH treats the Commission as a court.
3. ⭐⭐ **"response to Non production order"** ⇒ **their internal characterisation of the objection.**
4. **"FINAL"** ⇒ there were earlier drafts.

⇒ ⭐⭐ **ACTIONABLE: ask MSH what Attachments 1–3 were.** The objection he received was part of an
internal pack, and he holds only one item from it. ⭐ **That is an ordinary, neutral question.**

---

## 8.3 ⭐⭐ NEW — THE 11 JUNE DISCLOSURE WAS BUILT ON 6 MAY

| | |
|---|---|
| **Created** | **6 May 2026, 13:31:59** |
| **Modified / disclosed** | **11 June 2026, 10:56:12** |

⇒ ⭐⭐ **The container existed on 6 May and was expanded and sent on 11 June — five weeks later.**
**This confirms the repo's earlier note** (4 pp at creation, 10 pp at the 11 June re-save).

⭐ **It shows the Regulator held that material — including the Reese retraction email and the
McGinley routing chain — from at least 6 May 2026.**

---

## 8.4 ⚠ NEW — THE FORM 24 RESPONSE WAS RE-SAVED ON THE MENTION DATE

| | |
|---|---|
| **Created** | **18 February 2026, 13:05:31** |
| **Modified** | ⚠ **26 February 2026, 16:48:09** — eight days later |

⚠ **26–27 February 2026 is the mention** (relisted 26 → 27 Feb at Ms Matheson's request).

⇒ ⚠ **The Response was re-saved on the original mention date.** ⭐ **Most likely compiled, printed
or re-served for the listing. Recorded, not asserted.**

---

## 8.5 ⚠ THE 34-OCCASIONS LETTER WAS SCANNED FOUR WEEKS AFTER ITS DATE

**`AttF_2025-09-08_Hughes_attendance_letter_34_occasions.pdf`**
- **Letter date: 8 September 2025**
- **Scanner Title `SKM_C300i25100409030` ⇒ scanned 4 October 2025, 09:03** on the **KM_C300i**

⚠⚠ **DO NOT OVER-READ THIS.** He was working at Logan Hospital in October 2025 and had access to
that scanner. ⭐ **The most likely explanation is that HE scanned it.**

⭐ **What is worth recording, neutrally: the letter entered the document record on 4 October 2025 —
the day after the 3 October 2025 review request that bounced as spam.** ⛔ **A date, nothing more.**

---

## 8.6 ⭐ THE INBOUND SET IN ONE LINE

**Every inbound document matches a plausible source — MSH's lawyer, MSH's scanner, MSH's Word, the
Regulator's QIRC template, WorkCover's report engine — with one exception.**

⇒ ⛔ **The exception is the review decision, and the action remains unchanged: the single neutral
disclosure request. No allegation. No publication.**
