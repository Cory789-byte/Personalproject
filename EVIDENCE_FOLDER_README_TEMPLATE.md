# Evidence Folder — CO-25-2722

**Matter:** Shepherd v QPS
**Folder:** `C:\Evidence\CO-25-2722`
**Last updated:** <<FILL IN: date>>
**Prepared by:** <<FILL IN: name / role>>

> This README is the entry point for the CO-25-2722 evidence folder. Read this
> first. It explains what is here, how it is organised, and where to find the
> analysis. For the underlying case theory, see
> `output/CASE_THEORY.md`. For the asymmetric evidence index, see
> `output/SHEPHERD_v_QPS_ASYMMETRIC_EVIDENCE_INDEX.md`.

---

## 1. What this folder contains

This folder holds the full evidence set for the CO-25-2722 matter, together
with the processed outputs from the `bwc-evidence-processor` pipeline:

- **41 Body-Worn Camera (BWC) exhibits** — raw footage plus generated
  transcripts, frame extractions, and per-exhibit analysis.
- **300+ supporting documents** — QPS records, correspondence, court filings,
  affidavits, medical records, and third-party material.
- **5 themes of asymmetric investigation** — cross-cutting evidentiary
  threads identified across the BWC and document corpus.
- **Processed outputs** — case theory, triangulation, contradictions,
  procedural-compliance checks, psychological profile, WhatsApp tone
  analysis, FCFCOA application set, and the asymmetric evidence index.

All primary source material is preserved unmodified. All derived artefacts
live under `output/`.

---

## 2. How it is organised

```
C:\Evidence\CO-25-2722\
├── README.md                          # this file
├── bwc\                               # 41 BWC exhibits (source)
│   ├── BWC-001\ ... BWC-041\          # one folder per exhibit
│   │   ├── original\                  # untouched source video
│   │   ├── frames\                    # extracted frames
│   │   ├── transcripts\               # Whisper transcripts + SRT
│   │   └── metadata.json              # provenance + hashes
├── documents\                         # 300+ supporting documents
│   ├── qps\                           # QPS records
│   ├── correspondence\                # emails, letters, WhatsApp exports
│   ├── court\                         # filings, orders, transcripts
│   ├── medical\                       # medical records
│   └── third-party\                   # third-party material
├── keywords\                          # matter-specific keyword sets
└── output\                            # all processed artefacts (see §5)
```

> **Hashing / chain of custody:** every file under `bwc/` and `documents/`
> has a SHA-256 recorded in `output/PROVENANCE.json`. Do not move or rename
> source files — rerun the pipeline instead.

---

## 3. The 41 BWC Exhibits

Full exhibit table lives in `output/BWC_EXHIBIT_INDEX.md`. Summary:

| # | Exhibit ID | Officer | Date | Duration | Location | Key issue |
|---|------------|---------|------|----------|----------|-----------|
| 1 | BWC-001    | <<FILL IN>> | <<FILL IN>> | <<FILL IN>> | <<FILL IN>> | <<FILL IN>> |
| … | …          | …       | …    | …        | …        | …         |
| 41| BWC-041    | <<FILL IN>> | <<FILL IN>> | <<FILL IN>> | <<FILL IN>> | <<FILL IN>> |

<<FILL IN: copy the exhibit rows from `output/BWC_EXHIBIT_INDEX.md` here, or
leave the pointer and keep the authoritative list in the output file.>>

Each exhibit has been processed for:
- transcription (speaker-diarised where possible),
- keyword matching against `keywords/matter_*.json`,
- frame extraction at scene-change cuts,
- visual keyword sweep,
- officer identification and engagement scoring,
- procedural-compliance flags (QPS OPM references).

---

## 4. The 300+ Supporting Documents

Authoritative index: `output/DOCUMENT_INDEX.md`.

Document categories and approximate counts:

| Category | Count | Notes |
|----------|-------|-------|
| QPS records (QPRIME, OPM refs, running sheets) | <<FILL IN>> | <<FILL IN>> |
| Correspondence (email / letter / WhatsApp) | <<FILL IN>> | see WhatsApp Tone Analysis |
| Court filings and orders | <<FILL IN>> | <<FILL IN>> |
| Medical records | <<FILL IN>> | <<FILL IN>> |
| Third-party / open-source | <<FILL IN>> | <<FILL IN>> |
| **Total** | **300+** | |

Every document is OCR'd where required and indexed into the keyword and
triangulation passes.

---

## 5. The 5 Themes of Asymmetric Investigation

These are the cross-cutting evidentiary threads identified in
`output/SHEPHERD_v_QPS_ASYMMETRIC_EVIDENCE_INDEX.md`. Each theme triangulates
BWC footage, documents, and third-party material to expose asymmetry between
what QPS recorded and what the other evidence shows.

1. **<<FILL IN: Theme 1 name>>** — <<FILL IN: 1–2 sentence description>>
   Primary exhibits: <<FILL IN>>. Key documents: <<FILL IN>>.
2. **<<FILL IN: Theme 2 name>>** — <<FILL IN>>
3. **<<FILL IN: Theme 3 name>>** — <<FILL IN>>
4. **<<FILL IN: Theme 4 name>>** — <<FILL IN>>
5. **<<FILL IN: Theme 5 name>>** — <<FILL IN>>

For the full evidentiary map per theme, open
`output/SHEPHERD_v_QPS_ASYMMETRIC_EVIDENCE_INDEX.md`.

---

## 6. Navigating the `output/` folder

Everything under `output/` is generated by the pipeline and can be rebuilt by
rerunning `skills/bwc-evidence-processor/run_all.ps1`. Do not hand-edit these
files; edit the source and rerun.

| File | What it is | When to read it |
|------|------------|-----------------|
| `CASE_THEORY.md` | Canonical case theory | **Start here** after this README |
| `SHEPHERD_v_QPS_ASYMMETRIC_EVIDENCE_INDEX.md` | 5-theme evidentiary map | Understanding the asymmetry argument |
| `BWC_EXHIBIT_INDEX.md` | Authoritative 41-exhibit table | Looking up any BWC exhibit |
| `DOCUMENT_INDEX.md` | Authoritative document index | Looking up any document |
| `MASTER_ISSUES_LOG.md` | Every flagged issue, ranked | Triage / prioritisation |
| `TRIANGULATION.md` | Cross-officer / cross-source consistency | Checking corroboration |
| `DEEP_CONTRADICTIONS.md` | Direct contradictions between sources | Drafting cross-examination |
| `PROCEDURAL_COMPLIANCE.md` | QPS OPM / PPRA compliance flags | Regulatory argument |
| `QPS_COMPETENCY.md` | Officer competency analysis | Credit / training argument |
| `EVIDENCE_ENGAGEMENT.md` | Officer engagement scoring | Demeanour / conduct argument |
| `EVIDENCE_LEFT_AT_SCENE.md` | Items not collected / logged | Evidence-handling argument |
| `WHATSAPP_TONE_ANALYSIS.md` | Tone / sentiment of WhatsApp corpus | Communications context |
| `PSYCHOLOGICAL_PROFILE.md` | Psychological profile artefact | <<FILL IN: scope>> |
| `FCFCOA_APPLICATION_SET/` | 6-document FCFCOA application bundle | Federal Circuit filing |
| `MOBILE_SUMMARY.md` | Mobile-friendly brief | Quick review on phone |
| `MASTER_REPORT.md` | Full consolidated report | Reading everything at once |
| `PROVENANCE.json` | SHA-256 hashes + pipeline version | Chain of custody |
| `corrections/` | Self-improving correction history | Auditing pipeline changes |

---

## 7. How to use this folder

**If you are reviewing the case for the first time:**
1. Read this README.
2. Read `output/CASE_THEORY.md`.
3. Read `output/SHEPHERD_v_QPS_ASYMMETRIC_EVIDENCE_INDEX.md`.
4. Drill into `output/MASTER_ISSUES_LOG.md` for prioritised issues.

**If you are drafting a submission:**
1. Start from `output/CASE_THEORY.md`.
2. Pull exhibits from `output/BWC_EXHIBIT_INDEX.md` and documents from
   `output/DOCUMENT_INDEX.md`.
3. Cross-reference against `output/TRIANGULATION.md` and
   `output/DEEP_CONTRADICTIONS.md` before asserting any fact.
4. Cite using the exhibit ID (e.g. `BWC-017 @ 00:12:34`) and the document
   ID from `DOCUMENT_INDEX.md`.

**If new evidence arrives:**
1. Drop source files into `bwc/` or `documents/` under the correct category.
2. Run `skills/bwc-evidence-processor/run_all.ps1`.
3. Re-verify `output/PROVENANCE.json`.
4. Update this README's §3 / §4 counts if they changed.

---

## 8. Legal / handling notes

- **Privilege:** <<FILL IN: note anything covered by legal professional
  privilege or prepared in contemplation of litigation.>>
- **Suppression / non-publication:** <<FILL IN: any orders affecting
  material in this folder.>>
- **Access:** <<FILL IN: who may access this folder.>>
- **Retention:** <<FILL IN: retention period and disposal procedure.>>

---

*Generated as a template. Populate every `<<FILL IN: …>>` marker against the
authoritative `output/CASE_THEORY.md` and
`output/SHEPHERD_v_QPS_ASYMMETRIC_EVIDENCE_INDEX.md` before distributing.*
