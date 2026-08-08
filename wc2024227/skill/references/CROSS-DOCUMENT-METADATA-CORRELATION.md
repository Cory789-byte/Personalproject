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
