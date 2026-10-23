# Disclosure of 12 October 2026: the nine documents checked against Annexure A (13 Oct 2026)

**Source:** Matheson's email of Mon 12 Oct 2026, 8:30 am, with the attachments as provided by Cory
on 13 Oct. "The regulator confirms the veracity of the attached documents."
- **Files:** `disclosure_12OCT2026/` (hashes in `SHA256SUMS.txt`).
- **Email prints:** `email_prints/` (Outlook prints of the three emails). They match the Gmail
  records word for word.

**Method**
- Each disclosed file was compared with the Annexure A source file listed in
  `drafts/build_form24_annexureA.py`, by:
  - byte hash;
  - text diff (normalised for ligatures and line wrapping);
  - word counts;
  - for image-only files, rendered pages read field by field.
- Tab 31 (`.xlsx`) was parsed cell by cell and checked against facts 228–231 and against the Annexure
  screen capture.

## Result: every document matches

| Tab | Document | Disclosed file | Against Annexure A |
|---|---|---|---|
| 1 | AO3 Switchboard role description | PDF, 4 pp | **Text identical.** Same source PDF (same creation time, 5 May 2026 04:29:55 UTC); re-saved 24 Sep 2026, 11:15 am AEST |
| 5 | Taylor to Shepherd, "Approved – Permanent Full Time FTE", 27 Sep 2023 1:52 pm | PDF, 2 pp | **Text identical.** Same source PDF (created 5 Sep 2024 23:34:33 UTC); re-saved 28 Sep 2026, 10:59 am AEST |
| 17 | Movement form, 1–15 Mar 2026, 56 hrs | Image-only print, 4 pp | **Every field matches:** period, hours, comment, Donovan-Taylor 19.02.2026, Shepherd 26.02.2026, Ianna 27.02.2026, Hughes 27.02.2026 |
| 18 | Movement form, 16 Mar–26 Apr 2026, 56 hrs | Image-only print, 4 pp | **Every field matches:** comment "1FTE to 0.7fte … with possible extension after review"; Donovan-Taylor 09.04.2026, Shepherd 13.04.2026, Ianna 15.04.2026, Hughes 17.04.2026 |
| 19 | Movement form, 25 May–28 Jun 2026, 40 hrs | Image-only print, 4 pp | **Every field matches:** comment "1.0FTE - 0.5TE 40hrs … until further review and documentation"; Donovan-Taylor 27.05.2026, Shepherd 05.06.2026, Spink 08.06.2026, Hughes 09.06.2026 |
| 21 | Forrest to Shepherd, "ECC further information", 7 Jul 2026 10:54 am | PDF, 3 pp | **Body identical, word for word.** It is the Injury Management mailbox's copy, so the header differs and carries that mailbox's tags ("Categories: 1. Michelle (Team1)"; "Notes & Actions: FYI - saved"). The disclaimer is absent |
| 22 | Consultation Paper, proposed rosters (signed Hughes 12/11/2024) | Scanned PDF, 8 pp | **Byte-identical** (same file: Konica Minolta scan, 12 Nov 2024) |
| 23 | Consultation outcome (signed Hughes 12/12/2024) | Scanned PDF, 7 pp | **Byte-identical** (same file: Ricoh scan, 12 Dec 2024) |
| 31 | 2024 Emergency Code Register, MARCH 2024 sheet, 16–20 Mar 2024 | `.xlsx` extract, one sheet, 60 entries | **All 53 entries visible in the Annexure capture (rows 184–236) match exactly,** in the same order: time, code, location, pager and the note "CALLED VIA SWITRCHBOARD". The extract adds 3 earlier entries on 16 Mar and 4 later entries on 20 Mar |

## Tab 31 against facts 228–231 (the facts not admitted on 8 Sep)

| Fact | Asserts | Disclosed extract |
|---|---|---|
| 228 | 17 Mar 2024: eight entries, incl. MET CALL WARD 2H BED 7 at 19:16, CODE BLUE WARD 2H BED 7 at 19:20, MET CALL WARD 2Q BED 5 at 21:16 | **Eight entries** (03:57, 05:19, 07:48, 13:48, 14:13, 19:16, 19:20, 21:16). All three quoted entries are present |
| 229 | 18 Mar 2024: entries at 8:48, 9:20, 11:31, 11:32, 11:35 and 13:09 as quoted | **All six present, wording exact** |
| 230 | Six 18 Mar entries bear times between 6:00 and 14:00 | **Six** (08:48, 09:20, 11:31, 11:32, 11:35, 13:09). The next is 14:38 |
| 231 | 19 Mar 2024 at 11:34, MET CALL WARD 2I BED 20, "CALLED VIA SWITRCHBOARD" [sic] | **Present, exact,** including the misspelling |

**Effect**
- The only facts tied to a document that were not admitted (228–231) are now established by a
  document the Regulator has disclosed and vouched for.
- Of the five facts not admitted, only fact 154 is left. It says the Respondent's list of documents
  does not list the Communication Book.
- The count of Annexure A documents admitted or confirmed is **38 of 39**. Tab 24 is not addressed;
  its facts, 178–179, were admitted.

## File metadata (chronology only)

| When (AEST) | What the files record |
|---|---|
| 31 Dec 2021 | Code Register workbook created; creator "Logan Switch" |
| 24 Sep 2026, 9:28–9:39 am | Tabs 17, 18, 19 and 21 printed to PDF; author "Estelle Bain". The same name appears as the myHR session user on MSH's June 2026 production |
| 24 Sep 2026, 9:51 am | Matheson to Cory: the documents "requested … to be disclosed from MSH" |
| 24 Sep 2026, 11:15 am | Tab 1 PDF re-saved |
| 28 Sep 2026, 10:59 am | Tab 5 PDF re-saved |
| 28 Sep 2026, 11:04 am | Code Register extract saved; last modified by "Estelle Bain" |
| 30 Sep 2026 | Respondent's time for witnesses, outlines and experts expires |
| 1 Oct 2026 | Election and directions; direction 4 covers these ten documents |
| 12 Oct 2026, 8:30 am | Nine documents disclosed; veracity confirmed |

- **What the metadata shows:** the disclosed files were prepared at MSH between 24 and 28 Sep 2026.
- **What it does not show:** when MSH sent them to the Regulator.
- **Further notes:**
  - The Code Register file is an extract, not the native workbook. Its sheet records a used range to
    row 540 (`A1:Y540`), and the Annexure capture shows the native workbook with month tabs from
    MARCH 2024 onward.
  - Tabs 17–19 are image-only, so `pdftotext` returns nothing on them. Render with `pdftoppm` to
    read them.
