# WC/2024/227 — the 9 September 2026 set

**Deadline: 4.00 pm Wednesday 9 September 2026** (directions 1 and 2, Further Directions Order (3)
dated 19 August 2026).

⛔ **Every document in this set is dated 9 September 2026. Send it on 9 September.** If it goes out on
another day, rebuild first: `python3 drafts/build_9sep_final.py` after changing the date in
`build_direction_pack.py`, `build_medical_schedule.py`, `build_letter_regulator_8sep_response.py` and
`build_letter_regulator_further_request.py`.

⛔ **Direction 2 material is SERVED, NOT FILED.** Only the list of witnesses and its covering letter go
to the Industrial Registry. The outlines and the medical schedule go to the Regulator only.

---

## Send order

| # | Email | To | Cc | Attach |
|---|---|---|---|---|
| 1 | `3_EMAILS/Email_1_to_Industrial_Registry_cc_Regulator.txt` | qirc.registry@qirc.qld.gov.au | Renee.Matheson@oir.qld.gov.au | both files in `1_COMMISSION/` |
| 2 | `3_EMAILS/Email_2_to_Regulator_direction_2_material.txt` | Renee.Matheson@oir.qld.gov.au | — | the six files its ATTACH block names, from `2_REGULATOR/` |
| 3 | `3_EMAILS/Email_3_to_Regulator_request_documents_not_admitted.txt` | Renee.Matheson@oir.qld.gov.au | — | `2_REGULATOR/Request_to_Regulator_documents_not_admitted_WC2024227.pdf` |
| 4 | `3_EMAILS/Email_4_to_Dr_Krishnaiah_records_still_needed.txt` | ravikumar@mindandmemoryservice.com.au | info@mindandmemoryservice.com.au | none |

Send from **coryshepherd1@hotmail.com**.

## What each document is

**`1_COMMISSION/` — filed in the Industrial Registry, and served on the Regulator by the cc on email 1**

| File | Direction | pp |
|---|---|---|
| `Appellant_List_of_Witnesses_WC2024227.pdf` | direction 1 — file and serve | 1 |
| `Covering_Letter_to_Industrial_Registrar_WC2024227.pdf` | covering letter to the Registrar | 1 |

**`2_REGULATOR/` — served on the Respondent only**

| File | Direction | pp |
|---|---|---|
| `Appellant_List_of_Witnesses_WC2024227.pdf` | direction 1 — the served copy | 1 |
| `Covering_Letter_to_Industrial_Registrar_WC2024227.pdf` | the copy she receives on the cc to email 1 | 1 |
| `Letter_to_Regulator_re_letter_of_8_September_2026_WC2024227.pdf` | reply to the Regulator's letter of 8 September | 1 |
| `Outline_of_Evidence_Cory_Lea_Shepherd_WC2024227.pdf` | direction 2 — serve, do not file | 1 |
| `Outline_of_Evidence_Cory_Harrison-Jones_WC2024227.pdf` | direction 2 — serve, do not file | 1 |
| `Outline_of_Evidence_Patricia_Conaghan_WC2024227.pdf` | direction 2 — serve, do not file | 1 |
| `Schedule_of_Medical_Documents_Relied_Upon_Tabs_M1_to_M9_WC2024227.pdf` | direction 2 — the schedule and Tabs M1 to M9 | 43 |
| `Request_to_Regulator_documents_not_admitted_WC2024227.pdf` | request arising from the 8 September response | 2 |

## Held, not sent today

- `SEND_9SEP2026/HOLD_AFTER_11SEP_EMAIL_REGISTRY_FILE_FORM24_FORM25_WITH_RESPONSE.txt` — file the
  Form 24, Form 25 and the Regulator's response together **after** the response date of Friday
  11 September 2026. Attach the exact files served on 28 August.
- `SEND_EMPLOYMENT_9SEP2026/Email_5_...long_service_leave.txt` — **employment track, not the appeal.**
  Kept out of this folder so it cannot be attached to an appeal email by mistake.

## The two combined PDFs

| File | What it is | Use |
|---|---|---|
| `WITNESS_LIST_AND_OUTLINES_9SEP2026.pdf` | 5 pages: a contents page, then the witness list and the three outlines exactly as served | Serve on the Respondent in place of four separate attachments if you prefer one file. ⛔ It carries direction 2 material, so it is **not** filed. The Registry gets the witness list on its own. |
| `REVIEW_BUNDLE_9SEP2026.pdf` | 60 pages: everything going out today | Reading and printing only. Every page is stamped "not for service or filing". |

Build them with `python3 drafts/build_9sep_outlines_bundle.py` and
`python3 drafts/build_9sep_review_bundle.py`, after `build_9sep_final.py`.

## Rebuilding

`python3 drafts/build_9sep_final.py` rebuilds every document from source, verifies that no metadata,
annotation or embedded file survives in any PDF, enforces the one-A4-page limit on each outline, and
rewrites `FINAL_9SEP2026/`, `SEND_9SEP2026/` and `SEND_9SEP2026/TO_MATHESON_9SEP2026/` from the same
build so no superseded copy of a served document can survive anywhere. The build fails rather than
producing a set that breaches direction 2.

⛔ The redacted pages of the general-practice records at Tab M1 are held at
`drafts/assets/redacted/`. They are the only copy. If they are lost, the bundle will rebuild with the
**unredacted** private medical entries in it.
