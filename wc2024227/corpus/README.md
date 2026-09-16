# CORPUS — the whole correspondence record, in one place

> Built 31 July 2026 from the six mailbox packs at `documents/correspondence-packs/`.
> **154 unique messages, 2020–2026.** Deduplicated across packs on (date, subject, sender).

| File | What it is |
|---|---|
| **`FULL_CORPUS.md`** | ⭐ **Every message, full text, chronological.** Grouped by month. This is the pull-from file. |
| **`MESSAGE_INDEX.tsv`** | One row per message: `date · pack · page · from · to · cc · subject`. Sort or filter it. |

## How to use it

**Search the text:**
```
grep -n -i "on call"      wc2024227/corpus/FULL_CORPUS.md
grep -n -B2 -A20 "26 June" wc2024227/corpus/FULL_CORPUS.md
```
**Find every message from one person, or in a window:**
```
grep -i "hughes"   wc2024227/corpus/MESSAGE_INDEX.tsv
grep "^2025-03"    wc2024227/corpus/MESSAGE_INDEX.tsv
```

## ⚠️ Read these before quoting anything

1. **Times are UTC as exported. Add 10 hours for AEST.** The 26 June email shows `00:42:50` — that
   is **10:42 AEST**. Every time in the corpus and the index needs the same conversion.
2. **Never quote from the corpus into a filing.** Every entry cites `pack NN p.NNN` — **open the PDF
   and verify the words there.** The corpus is a finding aid, not a source. This is the cardinal
   habit in `CLAUDE.md`.
3. **Bodies are truncated at 6,000 characters.** Long items are complete in the PDF only.
4. **Attachments are not here.** Where an item is attachment-only, the body reads
   `(no body captured)` — 4 messages. Several missing attachments matter:
   MSH's employer responses of **16 Aug** and **6 Sep 2024**; Cory's WorkCover statements of
   **12 and 15 July 2024**.
5. **Images are not here.** Screenshots and text-message captures carry content no grep will find —
   the 14 Jan 2024 DFV thread is the example. **Render the PDF page** where an item mentions
   `IMG_*`, a screenshot, or a text message.
6. **Boilerplate was stripped** — disclaimers, acknowledgements of country, "Get Outlook for iOS",
   external-sender warnings. Nothing substantive was removed, but the PDF is authoritative.

## What the shape of it shows

| Year | Messages |
|---|---|
| 2020 | 2 |
| 2021 | 1 |
| 2022 | 15 |
| 2023 | 3 |
| **2024** | **37** |
| **2025** | **78** |
| **2026** | 17 |

Two years of low-volume roster traffic, then **37 messages in 2024** (the claim year) and
**78 in 2025** — the year of the return, the DFV leave, the attendance letter and the complaint.

## Coverage — be honest about it
The corpus contains **every message the packs captured**. It does **not** contain: the attachments,
the images, anything from OneDrive, or packs **06–09**, which have never been supplied.
