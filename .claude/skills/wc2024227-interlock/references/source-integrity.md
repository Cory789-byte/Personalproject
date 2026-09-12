# Source integrity

## ⛔ Documents that lie when extracted with pdftotext
| Document | Problem | Method |
|---|---|---|
| `2026-02-18_Form24_Response_and_email_communication.pdf` | Text layer **omits every exhibit reference, date and quoted phrase** in the Notice. Returns `( , p. 27)` where the page reads `(Exhibit B1, p. 27)` | **`pdftoppm -r 150 -png`.** 13pp; Response is render pages 7–10 |
| `2025-hughes-history/AttF_..._34_occasions.pdf` | **No text layer at all.** 32pp, returns nothing | **Render.** Letter is pp 1–5 of 5 at render pages 2–6 |
| `documents/orders/*.pdf` | No text layer | **Render** |
| `ATT09` (QH-IMP-401-5) | No text layer, no OCR installed | **Render.** Verified extracts at `documents/instruments/ATT09_VERIFIED_EXTRACTS.md` |

## Other traps
- ⛔ **The 8 September 2026 response TSV was wrong for facts 1-31 until 9 Sep 2026.**
  `documents/regulator-response-2026-09-08/FORM24_RESPONSE_parsed_fact_by_fact.tsv` had the Form 25
  **tab** statuses interleaved into the fact rows, so facts 5, 6, 17-24, 30 and 31 read "Disputed"
  when all of them were **Admitted**, and it showed 12 disputed tabs when there are **14**. It has
  been rebuilt (303 rows, `fact_no / status / fact_text`, full text not a tail) and the tab
  statuses now live separately in `FORM25_RESPONSE_tab_authenticity.tsv`.
  ⭐ **The response is 298 Admitted, 5 Not admitted — 154, 228, 229, 230, 231. Nothing else.**
  ⭐ **Authenticity disputed at 14 tabs: 1, 5, 6, 17, 18, 19, 20, 21, 22, 23, 24, 30, 30A, 31** —
  precisely the 14 sourced from the Appellant's own records.

- ⛔ **Grep a PDF only after `pdftotext`.** Grepping the binary silently misses compressed text
  and produces confident false negatives.
- ⛔ **`evidence-index/sources-text/Amended_Form_9A_07.04.2026.txt` is a condensed SUMMARY**, not
  the pleading. Diff and quote from `documents/filings/2026-04-08_Amended_Form9A_SOFC_Appellant.pdf`.
- ⛔ **"Dwyer" in QIRC search results returns PARTY names** — *Dwyer v WCR* [2025] QIRC 119 and
  *Loquias v The Star and John Dwyer* [2026] QIRC 23 are not his decisions.
- ⛔ **`corpus/FULL_CORPUS.md` times are UTC** (+10 for AEST). Nothing is quoted into a filing from
  the corpus — only from the source PDF.

## Verified law — do not re-derive
- **s 32(1): "A SIGNIFICANT contributing factor."** ⛔ Never "major" — that test was repealed in 2019.
- **Onus is on the appellant**, including showing the injury was not connected to reasonable
  management action — QIRC Workers' Compensation Appeal Guide v2.10, Part 7.3, which also names
  **Briginshaw**.
- **r 64D(1)(a)** requires service on a person *"other than a party"* — he is a party and is
  carved out. ⛔ **There is no service breach to plead.**
- **r 64E(1)** — 7 days after service, or a later time **with leave**. **r 64E(3)(b)** — the
  objection must be served **on the party**.
- **s 310 IR Act** — **six years** for non-dismissal general protections conduct, not 21 days.

## ⛔ Unverified — do not use until read to source
*Davis v Blackwood* [2014] ICQ 009 · *Bowers* (Hall P) · *Q-COMP v Hochen* (C/2009/47 — a file
number, not a medium-neutral citation) · *Mahaffey* [2016] ICQ 10 pinpoints · *Adams* [2015] ICQ 1
at [23] · *Delaney* [2005] QIC 11 · *Carr* [2022] QIRC 059 · *Read* [2017] QIRC 72 · *Allwood*
[2017] QIRC 88 · **Award cl 18.10** · **the "2006 Ombudsman Neville Report"** (asserted in a
redraft, unsupported anywhere in the repo — the second *"Independent Review Office"* if it isn't real)
⭐ Only **Prizeman** is held: `documents/Prizeman_v_QComp_2005_QIC_53.pdf`
