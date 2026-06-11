# WC/2024/227 MATTER THREAD — Workers Compensation Appeals

> **SCOPE NOTE — read first.** This is the **WC/2024/227 thread** — the Workers
> Compensation appeals proceedings — and it is **distinct from the QPS HR
> matter** (the QHRC Human Rights Complaint EDR19098 / CRM:0270704, *Shepherd v
> QPS*) that the rest of this repository documents. Material from the two
> matters must not be conflated: WC/2024/227 has its own forum, its own
> respondent agency (Workers' Compensation Regulatory Services / OIR), and its
> own complaint trail. The threads intersect only at the level of pattern
> evidence (reprisal / Model Litigant Principles), noted in Section 5.

---

## 1. Matter identifiers

| Field | Value |
|---|---|
| Proceeding | WC/2024/227 — Workers Compensation appeals |
| Appellant | Cory Lea Shepherd |
| Respondent agency | Workers' Compensation Regulatory Services (Office of Industrial Relations, QLD) |
| Officer complained of | Ms Renee Matheson — Senior Appeals Officer, Workers Compensation Regulatory Services |
| OIR complaint reference | Issue 4712 — "Complaint by Cory Shepherd" |
| OIR Complaints Manager | "…Neill" (recorded in source as "Sacha O…" / "Neill (OIR Complaints Manager)" — full name to be confirmed from primary correspondence) |
| Related tooling repo | `Cory789-byte/wc-extractor` — "Cloud Run extractor for WC2024227 evidence" |

## 2. What this thread is

Cory is the **Appellant** in WC/2024/227. Within those proceedings he lodged a
formal written complaint headed:

> **URGENT: NOTICE OF STATUTORY REPRISAL & BREACH OF MODEL LITIGANT PRINCIPLES — WC/2024/227**

opening:

> "I am the Appellant in the above-mentioned proceedings. I write to formally
> record a complaint regarding conduct of Ms Renee Matheson [Senior Appeals
> Officer, Workers Compensation Regulatory Services]…"

The complaint thus raises two heads within the WC matter itself:

1. **Statutory reprisal** — conduct alleged against the Senior Appeals Officer
   handling the appeal.
2. **Breach of Model Litigant Principles** — by the State party to the WC
   proceedings.

## 3. Known chronology (from this repository's corpus)

| Date | Event | Source |
|---|---|---|
| 2024 | WC/2024/227 appeal proceedings on foot (Cory as Appellant) | matter number; `2026-05-04_CShepherd_DOC_Every_Aspect_Findings.docx` |
| (date TBC) | Formal complaint lodged re Ms Renee Matheson — "URGENT: NOTICE OF STATUTORY REPRISAL & BREACH OF MODEL LITIGANT PRINCIPLES — WC/2024/227" | `…Every_Aspect_Findings.docx` |
| (date TBC) | OIR acknowledges contact; complaint registered as **Issue 4712** | `…Annexure_Key_Findings.docx` ("Thank you for your contact with OIR"; "Issue 4712: Complaint by Cory Shepherd… I have been advised by OIR") |
| 2026-02-23 | OIR Complaints Manager ("…Neill") responds: ES Privacy and Ethical Standards Units took [carriage / the decision] | `…Every_Aspect_Findings.docx` |
| post-2026-02-23 | Procedural-fairness defect identified: the Privacy/ES decision **did not engage the Complaints Management process** — the OIR formal complaint pathway was offered only **after** the ES decision was already made | `…Every_Aspect_Findings.docx` |

## 4. The procedural-fairness point (core of the complaint trail)

The corpus records this sequencing defect explicitly:

> "The Privacy/ES decision did not engage the Complaints Management process —
> Cory was offered the OIR formal complaint pathway only after the ES decision
> was already made."

That is, the substantive decision (Privacy / Ethical Standards) was reached
**before** the formal Complaints Management pathway was opened to the
complainant — the pathway offered could not have influenced the decision it
nominally reviews. This mirrors a pattern documented elsewhere in the corpus
(decisions made first, process offered after), but the WC/2024/227 instance
stands on its own record.

## 5. Relationship to (and separation from) the QPS HR matter

| | WC/2024/227 thread | QPS HR matter |
|---|---|---|
| Forum | Workers Compensation appeals / OIR complaints | QHRC — EDR19098 (CRM:0270704) |
| Respondent | Workers' Compensation Regulatory Services (OIR) | Queensland Police Service (Commissioner of Police) & Alexia Negro |
| Subject conduct | Conduct of Senior Appeals Officer (Matheson); reprisal; Model Litigant Principles in the WC appeal | Lockout, arrest, property/dog seizure, address change, charges — see rest of this repo |
| Complaint trail | OIR Issue 4712 → ES/Privacy decision → Complaints Management offered late | QHRC priority assessment, 14-day pre-conference |

**Why the corpus flags it at all:** the source analysis itself warns —
*"This is the WC2024227 thread — Workers Compensation appeals, NOT the QPS HR
matter directly."* (`…Annexure_Key_Findings.docx`). The relevance to the QPS
matter is limited to **pattern evidence**: both threads allege statutory
reprisal against a protected discloser and breaches of Model Litigant
Principles by Queensland state agencies. Both appear in the
"proper-channel-engagement" register (alongside FSQ, LSC 71025243, RTA:0055411,
CCC, OIC 318762) that establishes Cory's multi-year pattern of using lawful
regulatory channels.

## 6. Where the evidence lives

- **In this repository:** only secondary references, all in
  `source_documents/SUBMISSION_QUOTE_DIFF.md` (quote-diff rows sourced from
  `2026-05-04_CShepherd_DOC_Annexure_Key_Findings.docx` and
  `2026-05-04_CShepherd_DOC_Every_Aspect_Findings.docx`) and the corresponding
  entries in `legal_system/output/data.json` (`quote_diffs` 109–111, 169–172).
- **Primary evidence corpus:** the `Cory789-byte/wc-extractor` repository
  ("Cloud Run extractor for WC2024227 evidence") is the dedicated tooling/
  evidence pipeline for this matter. Primary documents (the reprisal notice,
  Issue 4712 correspondence, the ES/Privacy decision, the Matheson complaint)
  are **not** held in this repository.

## 7. Gaps / to-do for this thread

- [ ] Obtain and file the full text of the "URGENT: NOTICE OF STATUTORY
      REPRISAL…" complaint (date of lodgement, full particulars of the
      Matheson conduct alleged).
- [ ] Confirm the OIR Complaints Manager's full name (source truncates to
      "Sacha O…" / "…Neill").
- [ ] Obtain the 23 February 2026 OIR response in full, and the underlying
      ES/Privacy decision it relies on.
- [ ] Establish current status of WC/2024/227 itself (listed? decided?
      adjourned pending the complaint?).
- [ ] Decide whether WC/2024/227 primary documents should be consolidated into
      a dedicated matter repository (the `wc-extractor` repo is tooling, not a
      document archive), mirroring this repository's
      `EVIDENCE_FOLDER_README_TEMPLATE.md` structure.
