# EVENT_LEDGER.tsv — the join that did not exist

One row per **dated** paragraph of the notice to admit facts served 28 August 2026, sorted
chronologically, carrying on the same line the things that were previously in four different files:

| column | what it is |
|---|---|
| `date`, `time` | the first date, and first time, stated in the fact |
| `kind` | `event` = something happened; `document-date` = the date belongs to a pleading or list, not to an event |
| `para` | the paragraph number of the notice — ⭐ **this is the citation** |
| `verdict` | Admitted / Not admitted, from the response of 8 September 2026 |
| `actors` | named persons appearing in the fact |
| `tabs` | Annexure A tab(s) |
| `text` | the fact, verbatim |

## Why it exists
Before this, an answer to "what happened on 20 May 2024, and which of it is admitted?" required
grepping `index/FULLTEXT.txt`, opening `SERVED_303_facts_and_verdicts.json`, cross-checking
`corpus/MESSAGE_INDEX.tsv` and reading `COMPLETE-MASTER-TIMELINE.md` — four shapes of the same
events, none of them joined. **Re-deriving that join is where the errors in this matter have come
from** (the outline citations that shifted by four; the May/December referral confusion).

## Limits — read before relying on it
- **122 of the 303 facts carry no date** and are absent from this file. They are the negatives
  ("does not allege", "does not list"), the role-description duties and the instrument facts.
  ⛔ **This ledger is not the notice. It is an index to the dated part of it.**
- Only the **first** date and time in each fact are extracted. Facts stating an interval between
  two dates appear under the earlier one.
- `kind=document-date` rows cluster on 13 May 2026 and 14 August 2026 because that is when the
  Respondent's statement of facts and contentions and its amended List of Documents are dated.
  **Those are not events on those days.**
- Actor matching is by surname, so a fact that merely mentions a person is tagged with them.

## Rebuild
`python3 scripts/build_event_ledger.py` from `wc2024227/`. Re-run whenever the response JSON changes.
