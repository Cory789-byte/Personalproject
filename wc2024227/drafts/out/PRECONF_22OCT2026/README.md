# Pre-conference package (drafts, 19 Oct 2026)

⚠ **SENT 19 Oct 2026, 16:04, as one email** (the dates and the letter together, to Matheson only). The as-sent copy
is in `documents/sent-2026-10-19/`. It is the **13:14 build** (commit `2033216`), with "Now admitted; tender" and no
de novo sentence in item 4. The files in this folder are the later 13:18 revision, which was **not sent**. Do not
circulate them as the 19 Oct schedule. Use them only as the base for any further update. Ledger R37; Predictions E40.

**Order of sending**
1. `EMAIL_1_REPLY_DATES_send_19-20OCT.txt`: dates only, s 552B agreed, copied on the Registry email. Send now.
2. **Then the letter**, now dated **19 October 2026** (Cory, 19 Oct): send `EMAIL_2_COVER_…` with
   `LETTER_TO_REGULATOR_with_updated_Schedule_DRAFT.pdf`, renamed as the email says. Send it as a separate email after
   the dates reply, so the dates can go to the Registry on their own. The reply date stays 4.00 pm, Fri 30 Oct.

**The files**
- `LETTER_TO_REGULATOR_with_updated_Schedule_DRAFT.docx` / `.pdf` (10 pp): the letter (pp 1–2), then the
  Schedule of 1 October 2026, updated (pp 3–10). This is the one to send.
- `SCHEDULE_of_1Oct2026_updated_DRAFT.docx` / `.pdf` (8 pp): the updated Schedule alone, for the Registry agenda or
  the conference bundle.
- Built by `drafts/build_letter_and_updated_schedule.js` (Times New Roman 11, A4, the 1 Oct layout). To rebuild with
  other dates, run from `drafts/`: `node build_letter_and_updated_schedule.js "20 October 2026" "Friday 30 October 2026"`.
  That writes the .docx files and the stripped .pdf copies. The container has no Times New Roman, so its PDFs use
  Liberation Serif, which has the same metrics. A PDF exported from Word gives true Times New Roman with the same
  layout.

**The Schedule: what changed from 1 Oct, and what did not**
- **Checked against the as-sent PDF, cell by cell.** Parts 2 and 3 are identical, and so are the Part 1 columns Tab,
  Document, Date, 8 Sep 2026 and 24 Sep 2026.
- **Part 1, changed:**
  - **Introduction.** The first four sentences and the "facts recorded in 13 of the 14" sentence are kept. Added: the
    12 Oct confirmation, quoted ("The regulator confirms the veracity of the attached documents."), and 38 of 39
    confirmed. Dropped: "For the other 13, what remains in dispute is the authenticity of the copies, not their
    content."
  - **New column "12 Oct 2026":** "Copy provided; confirmed" for Tabs 1, 5, 17–19 and 21–23; "Spreadsheet provided;
    confirmed" for Tab 31; "Not mentioned" for Tab 24.
  - **Position now (whole column revised, Cory 19 Oct):**
    - "Admitted; tender proposed" for the 25 documents admitted on 8 Sep.
    - "Veracity confirmed; tender proposed" for the twelve the Respondent later confirmed (Tabs 6, 20, 30 and 30A on
      24 Sep; Tabs 1, 5, 17–19 and 21–23 on 12 Oct). This replaces "Now admitted; tender", including the 1 Oct wording
      for the four 24 Sep rows.
    - Tab 31: "Veracity of the spreadsheet confirmed; tender proposed. Facts 228-231 not admitted".
    - Tab 24 is unchanged.
    - Why: "veracity" is Matheson's own word. "Tender proposed" implies no agreement to tender and no concession on
      admissibility; tender is letter item 2. The Tab 32 table uses the same wording.
  - **The note after the table:** the "no date by which the copies are expected" clause is removed. Added: on 12 Oct
    the Respondent provided its own copy of each of the ten except Tab 24.
- **Added after Part 1:**
  - Tab 32A/32B, with the 16 Oct "veracity" quote and the rule 49 request.
  - Facts 228–231, verbatim as served, mapped to rows of the sheet "MARCH 2024": rows 9–16, 17–22 (with row 23 at
    14:38), and 33 (column E). Verified against the native file.

**What the letter asks** (ask, never allege; reply by 4.00 pm, Fri 30 Oct):
1. **Facts 228–231:** now that the spreadsheet is confirmed, admit them.
2. **Tender** of the 38 Annexure A documents and Tab 32A without further proof, in the Annexure A form or the
   12 Oct form. Also: whether Tab 24's authenticity dispute is maintained, and on what ground.
3. **Relevance and admissibility:** identify any objection and its ground now, not at the hearing.
   - On "truth", it quotes 9A Part C ¶8: the admissions are evidence that the documents exist and of what they say,
     and of what the SOFC and LOD do not contain.
   - Agreeing to tender or relevance does not require the Regulator to accept the truth of any statement. Weight and
     reasonableness stay with the Commission.
   - It deliberately does **not** say the documents are relied on "only" for existence, which would have narrowed C 8.
4. **Section 32(1):** quotes facts 261–262 and asks whether s 32(1) is not in issue to that extent (factors 2, 3 and
   4), so the hearing is confined to s 32(5). It is a question, not a settled concession.
   - It states that the Appellant accepts the hearing is de novo and that no finding binds the Commission. 9A Part C
     ¶9 already says so, and the Respondent took that point in its 18 Feb response (fact 295).
   - That leaves only whether the elements can be agreed. A "no" then has to say which element is contested.
5. **Leave:** consent, and the time sought for their amendment. It then says (Cory's wording, 19 Oct) that once
   facts 228–231 are admitted, he may provide a completed 9A with any changes from the 1 Oct version noted, adding no
   new stressor or allegation. "May" makes it conditional, with no date: it is not a promise to deliver before the
   conference.
6. **¶27:** notice only (fact 303), to be asked at the conference.

Consequence: whatever is not agreed goes to the Commission at the conference, then directions or a mention.

⛔ Nothing on metadata, the folder, Bain, employment, money, the deed or motive. The only file facts used are the
spreadsheet's name as sent, its sheet name, its column headings and its rows: content, not metadata.
