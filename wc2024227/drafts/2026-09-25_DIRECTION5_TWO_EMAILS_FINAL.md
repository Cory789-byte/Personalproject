# DIRECTION 5: ONE EMAIL, BOTH DOCUMENTS (letter + the admitted record and questions), TO THE COMMISSION AND THE RESPONDENT (FINAL, NOT SENT)

**Revised 25 September 2026 on Cory's instruction:** both documents go to Commissioner Dwyer (through the
Registry) and to the Regulator, together. This replaces the earlier two-email split.

**When to send: the morning of Thursday 1 October 2026, within Registry business hours.** (Revised 25 September
on Cory's decision to wait out the Respondent's time.) Both PDFs are dated 1 October 2026 and say that the time
for the Respondent's material under directions 3 and 4 expired at 4.00 pm on 30 September 2026, and that no
medical or expert evidence was served.

**Alternative:** send after 4.00 pm on Wednesday 30 September. First rebuild both PDFs with that date:
`python3 build_letter_registry_direction5.py "30 September 2026"` and
`python3 build_conference_paper.py "30 September 2026"`. The "expired" wording stays, because it applies
from 30 September. **Never send a 30 September version before 4.00 pm.**

**Before sending, check the inbox** for anything from the Regulator, OIR, the Registry or Metro South Health
since 24 September:
- **An expert or medical report has arrived:** do NOT send. The letter (section 2, last paragraph) and the
  paper (section 1) both say none was served. Both must be revised first.
- **An amended list of witnesses, further outlines, an MSH document, or an extension request:** stop and
  re-check both documents first.
- **Nothing has arrived:** send as built.

**Pre-send check (re-run 25 September 2026 on the 1 October build):**
- all quotations in the paper audited against the served notice;
- the figures match the Form 25 response (39 / 25 / 14; 4 confirmed; 10 remaining);
- the dates are consistent across the letter, the schedule and the paper;
- no discipline words (fraud, reprisal, hostile and the like);
- no held-for-cross-examination points (1:07 pm, "last week", "raise my voice", the date of the eight-month
  spreadsheet);
- nothing from the never-voiced list;
- metadata stripped: letter 2 pages, paper 10 pages.

---

```
TO:      qirc.registry@qirc.qld.gov.au
CC:      Renee.Matheson@oir.qld.gov.au
SUBJECT: WC/2024/227 - Shepherd v Workers' Compensation Regulator - direction 5, progressing the matter, and questions for the Respondent
ATTACH:  LETTER_TO_REGISTRY_direction5.pdf
         ADMITTED_RECORD_AND_QUESTIONS_for_the_Respondent.pdf
```

Dear Registrar,

In accordance with direction 5 of the Further Directions Order (3) dated 19 August 2026, I attach my
letter to progress the matter, with a schedule of the documents that remain to be confirmed, and the
paper referred to in it, setting out the admitted record and questions for the Respondent.

The Respondent is copied to this email, and by this email I provide the paper to the Respondent. I
would be grateful if the Respondent could indicate its position on the questions in the paper, and its
settled position under section 32(5) at section 6, by 15 October 2026.

Yours faithfully,

Cory Lea Shepherd
Appellant, self-represented
0417 400 227
