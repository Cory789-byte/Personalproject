---
name: evidence-ingest
description: Pull documents into the WC/2024/227 repo from OneDrive/SharePoint or Google Drive instead of attaching them, then hash-dedupe, file, index, commit and push. Use whenever Cory says to add, upload, include, grab or push documents into the repo, refers to a local Windows path, says a file is too big to attach, or names a correspondence pack, disclosure bundle or mailbox export. Also use when asked how to get files from his PC to Claude.
---

# EVIDENCE INGEST — getting documents into the repo without attaching them

## 0. THE HARD LIMIT — state this plainly, never fudge it

**Claude cannot read Cory's PC.** Sessions run in an ephemeral cloud container with no view of
`C:\Users\corys\...` or any local drive. **No skill can change this** — a skill is an instruction
file, not network access. If a local Windows path is named, say so in one sentence and move
straight to the routes below.

## 1. THE THREE WORKING ROUTES — in order of preference

### ⭐ Route A — OneDrive / SharePoint (best; already set up)
The **Microsoft 365 connector is live** on `CoryShepherd@Trustandcollectiveco.onmicrosoft.com`, and
the case file already lives there:

```
Documents/SHEPHERD_v_QPS_MASTER_CASE_FILE/
  01_WORKCOVER_WC2024227/
    04_Exhibits/Correspondence_Emails/
    05_Correspondence/
  05_CIVIL_Property_Tenancy/04_Correspondence/
  07_CORRESPONDENCE_and_Communications/{01_QPS, 02_Armstrong_Legal, 03_Other}
```

**Cory drops files into any synced OneDrive folder; Claude reads them directly. No attaching, no
size limit.**

Tools (load via ToolSearch first):
- `mcp__Microsoft_365__sharepoint_folder_search` — find a folder by name; returns a `uri`
- `mcp__Microsoft_365__read_resource` — pass a folder `uri` to list contents, or a file `uri` to read
- `mcp__Microsoft_365__sharepoint_search` — search by filename/content across the drive

### Route B — Google Drive
Connector is live on `admin@australianlegal.org`.
- `mcp__Google_Drive__search_files` — structured query, e.g. `title contains 'PACK'`
- `mcp__Google_Drive__download_file_content` / `read_file_content`

⚠️ Drive holds many `.lnk` **Windows shortcuts** (1–2 KB) that are *not* the file. Check
`fileExtension` and `fileSize`; a `.lnk` means the real file is still only on the PC.

### ⭐ Route C — git from his PC (the durable one; unlimited size)
Best when there is a lot, or when it should be permanent. On his machine:
```
git clone <repo-url>
git checkout claude/workcover-matter-repo-krg8qg
copy files into wc2024227/documents/...
git add -A && git commit -m "add <what>" && git push
```
Then Claude runs `git pull origin claude/workcover-matter-repo-krg8qg` and everything is present.
**This is also the answer to "can you save this repo / copy it" — the repo IS the saved copy, and
cloning it puts a full copy on his PC.**

### Route D — attach in chat
Fine for one or two files. Zips are unpacked automatically. Large PDFs must be read with page
ranges. This is the fallback, not the default.

## 2. THE INGEST PROCEDURE — follow every step

1. **Hash first, always.** `md5sum` the incoming file against everything in
   `wc2024227/documents/correspondence-packs/` and the relevant `documents/` subfolder.
   **Duplicates have been sent three times in one session.** If the hash matches, say so plainly,
   confirm it is committed (`git log --oneline -1 -- <path>`), and **do not re-file it**.
2. **Unzip to the scratchpad**, never into the repo.
3. **File with a descriptive name** carrying date, author and extent:
   `NN_Name_PACK_<pages>pp.pdf` · `YYYY-MM-DD_Author_subject_STATUS.pdf`
4. **Extract the CONTENTS page** of any pack (`pdftotext -layout | sed -n '1,80p'`).
   ⚠️ **Section numbers in a pack's CONTENTS do not match PDF page numbers** — use the `p.` column,
   and locate sections by grepping their title text page by page when the offset drifts.
5. **Read the high-value items**, do not just index titles. Filing without reading has repeatedly
   missed findings that changed the record.
6. **Update `documents/correspondence-packs/INDEX.md`** — a section per pack, every item dated.
7. **Propagate corrections.** If something read today contradicts a finding, fix it **everywhere**:
   `MASTER.md`, the reference file, *and any summary table inside it*. A correction at the top of a
   file does not fix a stale table further down — that has happened.
8. **Commit and push** to `claude/workcover-matter-repo-krg8qg`. Never another branch.

## 3. WHAT THE PACKS ACTUALLY ARE — do not get this wrong

They are exports of **Cory's own mailbox, grouped by correspondent** — *not* the other person's
mailbox. Proven by pack 05, which contains his sent items and a non-delivery report.

⇒ **An absence in a pack proves "Cory never received it"** — which is the useful proposition —
**not "it was never written".** Say which one is being claimed.
⇒ The grouping is thematic, not a party filter: pack 02 (Taylor) contains his emails to WorkCover.

## 4. STANDING CAUTIONS

- **Attachments rarely survive the export.** `[Message has attachments — export with --attachments]`
  means the attachment is **absent**. Log it as a gap; several matter (MSH's employer responses of
  16 Aug and 6 Sep 2024; Cory's 12 and 15 July 2024 WorkCover statements).
- **Text-only extraction misses evidence.** Screenshots and images carry content no grep will find —
  the 14 Jan 2024 DFV text thread sat undiscovered in a text-searchable PDF for exactly this reason.
  **Render pages with `pdftoppm -r 200 -png` and read them as images** where an item is described as
  a screenshot, a text message, or `IMG_*`.
- **Grade every proposition** `[D]` / `[A]` / `[D/A]` / `[W]`, per `MASTER.md`.
- **State the limit of every finding in the same breath as the finding.**
