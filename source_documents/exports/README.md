# Exports

Two sets of documents, each in three formats. Same content in all three formats within a set.

---

## Set 1 — Where my charges stand (13 August 2026)

The current charge position. Charge 2 discontinued, Charges 1 and 3 continuing, and the answer to each reason the prosecution gave. Written first person.

Covers: the three charges and where each stands · what Charge 1 actually requires · why the limb they chose matters · their first reason and the leasing manager on the police cameras · the later lease · the bond · their second reason · Romeo's purchase and Queensland registration · the circumstances the documents were signed in · Charge 3 · what the police did that they had no power to do · eleven supporting documents lettered A to K · ten things to chase.

| Format | File | Notes |
|---|---|---|
| PDF | `Shepherd_Charges_Position_2026-08-13.pdf` | A4, prints as-is |
| PowerPoint | `Shepherd_Charges_Position_2026-08-13.pptx` | 42 slides, 16:9 |
| HTML | `Shepherd_Charges_Position_2026-08-13.html` | single file, opens in any browser |

## Set 2 — What happened to me, and what the evidence shows (14 May 2026)

Prepared for the human rights conciliation. Opening · what happened across ten sections · twenty-one numbered exhibits with the verbatim quotes · what I am asking the Commission to do. Written first person.

| Format | File | Notes |
|---|---|---|
| PDF | `Shepherd_Conciliation_2026-05-14.pdf` | A4, prints as-is |
| PowerPoint | `Shepherd_Conciliation_2026-05-14.pptx` | 52 slides, 16:9 |
| HTML | `Shepherd_Conciliation_2026-05-14.html` | single file, opens in any browser |

---

## Getting them onto a phone

Open the link, then tap the download icon at the top right of the file view. PDFs and HTML preview in the browser; PowerPoint downloads straight to Files.

Replace `BRANCH` with the branch the files are on — currently `claude/southport-case-facts-6iJY6`.

```
https://github.com/Cory789-byte/Personalproject/blob/BRANCH/source_documents/exports/Shepherd_Charges_Position_2026-08-13.pdf
https://github.com/Cory789-byte/Personalproject/blob/BRANCH/source_documents/exports/Shepherd_Charges_Position_2026-08-13.pptx
https://github.com/Cory789-byte/Personalproject/blob/BRANCH/source_documents/exports/Shepherd_Charges_Position_2026-08-13.html

https://github.com/Cory789-byte/Personalproject/blob/BRANCH/source_documents/exports/Shepherd_Conciliation_2026-05-14.pdf
https://github.com/Cory789-byte/Personalproject/blob/BRANCH/source_documents/exports/Shepherd_Conciliation_2026-05-14.pptx
https://github.com/Cory789-byte/Personalproject/blob/BRANCH/source_documents/exports/Shepherd_Conciliation_2026-05-14.html
```

Or go to the pull request, open the Files changed tab, and download from there.

---

## Rebuilding after an edit

The content lives at the top of each script, in plain lists. Edit the text there and re-run; all three formats regenerate together.

```bash
pip install python-pptx reportlab

cd source_documents/exports
python3 build_charges_exports.py     # Set 1
python3 build_exports.py             # Set 2
```

`build_charges_exports.py` — content is in `OPENING`, `BODY`, `EXHIBITS` and `ASKS`.
`build_exports.py` — content is in `OPENING`, `WHAT_HAPPENED`, `THE_EXHIBITS` and `WHAT_I_ASK`.

Both use the same house styling: Georgia serif for print and HTML, Calibri for slides, bordered exhibit blocks, quotes in italics.
