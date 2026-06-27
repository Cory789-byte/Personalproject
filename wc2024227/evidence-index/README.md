# Evidence Index — WC/2024/227

Searchable, curated index of the matter's evidence held across the cloud
(OneDrive / SharePoint, via the Microsoft 365 connector) and the repo. Built for
the `wc227-matter` skill's **evidence** sub-skill so the evidence-processor can
reason over the whole matter without the source binaries living in git.

## Curation rules (mirror `skill/SKILL.md` discipline — non-negotiable)

1. **WC/2024/227 only.** The QPS / DV / Alexia Negro criminal matter, any
   third-party criminal or health data, and unrelated matters (Sibley, etc.) are
   **EXCLUDED**, not indexed. The user's cloud co-mingles them; this index does not.
2. **Quarantine (discipline rule 2).** The ESU / PID **complaint form** and any
   "fraud" / collateral-purpose material (e.g. the 11 July 2024 email) are listed
   by **existence / location only** in a "parallel-track" section if encountered —
   their content is **never** pulled onto the WC track.
3. **Verified vs working (the cardinal habit).** A descriptive filename is the
   **user's characterisation = working / asserted**, NOT a verified fact, until the
   document's content is read against source. Files with **no extractable text**
   (image / screenshot PDFs) are marked `content-unverified`.

## Status legend

| Tag | Meaning |
|---|---|
| `[repo]` | already in the repo (`documents/…`) — content ingested |
| `[new-text]` | new to the project; text extracted and mirrored under `sources-text/` |
| `[new-image]` | new; **image-only** PDF — content NOT extractable via the connector (needs OCR or the original file) |
| `[dup]` | duplicate of another listed item |

## Layout

- `README.md` — this file.
- `01-FINISHED-APPEAL.md` — manifest + cross-references for the OneDrive
  `01 FINISHED APPEAL` folder.
- `sources-text/` — greppable plain-text mirrors of text-bearing cloud sources
  (the binaries stay in the cloud / `documents/`).

## Connector / provenance

Microsoft 365 account: `CoryShepherd@Trustandcollectiveco.onmicrosoft.com`
(org display name "Collective holdings and accounts"). Reachable stores: the
personal OneDrive (`…-my.sharepoint.com/personal/coryshepherd…/Documents/`) and
the team site (`trustandcollectiveco.sharepoint.com/Shared Documents/Saines legal/`).
The connector returns **extracted text only** — no raw binary / no OCR of
image-only PDFs.
