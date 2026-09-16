# CORRECTIONS TO APPLY IN THE OTHER WORKING SET
> ⚠️ **This sheet is for `workcover-matter\03_ARGUMENT\drafts\CLAUDE_CODE_FINAL_EMAIL` — the OneDrive
> folder. NOT this repository.** That folder is not reachable from this environment; these are the
> exact edits to make there.
> Built 1 August 2026 from three external audits, **each of which was tested against the primary
> sources here.** Everything below is verified.

---

# P0 — THE ONE HARD ERROR

## The map and CLAUDE.md: E12 is **not** EB12 cl 3.9.1

**FIND (anywhere):** *"HR Policy E12 … named in EB12 cl 3.9.1"* / *"EB12 3.9.1 = E12"*

**REPLACE WITH:**
> **HR Policy E12 (Individual employee grievances)** and **E13 (Workplace Harassment)** are
> **preserved Human Resources policies listed in EB12 Schedule 2**, and are therefore incorporated
> into the certified agreement. The grievance chain is **EB12 cl 1.12.1 → cl 7.2 of the Hospital and
> Health Service General Employees (Queensland Health) Award – State 2015**.

**WHY — verified against the EB12 PDF:** cl 3.9.1 sits **between the SCHEDULE 3 and SCHEDULE 4
headings**. It is a clause of **Schedule 3 — Variable Working Hours Arrangement**, not of the main
agreement, and binds only employees on a VWHA. ⛔ **A 24/7 rostered switchboard operator is very
unlikely to be on one, so it should not be cited for "work now, grieve later" either.**

⭐ **Bonus from the same check:** Schedule 2 also lists **E13 Workplace Harassment**. Both E12 and
E13 are inside cl 1.11 scope — **unlike the AD Act, which is not.**

---

# P0 — "E12 NOT OBTAINED"
Update the notes **in that folder** to record that the E12 PDF is held there.
⚠️ **Do not copy this fix into this repository** — here **E12 and E13 are genuinely not held**, and
both are requested at **§4(e) of the Stage 1 notice.**

---

# P1 — ATT09 (QH-IMP-401-5): DON'T DEMOTE IT. VERIFY IT.
The audit is right that the PDF has **no usable text layer** — 28 pages, ~1,250 characters of bullet
artifacts. ⛔ **But the quotes are correct.** Verified 1 August 2026 by rendering:

```
pdftoppm -r 150 -png -f 4 -l 4 ATT09_QH-IMP-401-5_Workplace_Rehabilitation.pdf out
```

**Page 4 of 28 contains, verbatim:**
- **§2.2** *"The immediate line manager is best placed to be the primary contact for the worker
  wherever possible and facilitate the injured workers on-going connection with the workplace."*
- **§2.2** *"Where alternate work duties are required, identify and actively seek, with support from
  the RRTWC if needed, meaningful suitable duties, and ensure suitable duties are made available
  wherever reasonably practicable."*
- **§2.2** *"Inform the worker of the appropriate dispute resolution process to follow in such cases
  where the worker does not agree with elements of a proposed workplace rehabilitation plan or
  suitable duties program."*
- ⭐ **§2.3** *"Ensure that an injured/ill worker who requires workplace rehabilitation for **either a
  work or non-work-related injury/illness**, is contacted for workplace rehabilitation support…"*

⇒ ⭐ **§2.3 is the "applies without an accepted claim" point.** It is an **RRTWC** duty, at **§2.3** —
**not §2.1**. Fix the pinpoint rather than demoting the instrument.

⚠️ **Two provisions on that page NOT to use:**
- *"Ensure suitable duties considerations are documented"* — ⛔ **limited to accepted WC cases.**
- *"Request the injured/ill workers signed authorisation…"* — ⚠️ relevant to the **option 1 / option
  2 election**, because the standard contemplates the **coordinator** seeking an authorisation, not a
  Director sending nine questions to the worker's own GP. **Use it there, not as a rehab duty.**

---

# P1 — ATT16 / IME GUIDELINE "CANNOT DIRECT NOT TO ATTEND"
⚠️ **The audit is right to say it is over-strong as a bar on this hold-out — and there is a reason
that is not obvious.** The full passage, verified:

> *"It is **not limited to a voluntary absence** such as sick leave and **may include involuntary
> absence such as suspension** in the context of a genuine workplace health or safety concern.
> **However, a chief executive cannot direct an employee not to attend the workplace for the purpose
> of requiring an employee to submit to a medical examination.**"*

⇒ ⛔ **The sentence before it cuts against you.** It says an absence the employer caused **may still
count as "absent from duty"** for the PS Act s 103 gateway. **So do not run "the absence is theirs,
so s 103 is not enlivened" as a clean argument.**
⭐ **The argument that survives is narrower and better:** **s 103(b)** requires the chief executive to
suspect the absence is ***caused by* the illness** — and on MSH's own account the stated cause is the
pending medical information.
⭐ **Keep the "cannot direct" sentence banked. Deploy only if MSH moves to a formal IME.** It governs
IMEs, not a treating-practitioner request.

---

# P1 — THE POST-RFMI LAYER
⭐ **Built. It is not in that folder — it is here**, at `wc2024227/drafts/SEND_31JUL/` →
`wc2024227/drafts/out/`, **sending Monday 3 August 2026**: five documents, 28pp — the RFMI response
with the Q1–Q9 allocation, the appointments and costs notice, the **cl 10.3.2 request** (21-day
clock), the **cl 1.11.2(a) Stage 1 dispute notice**, and the **PS Act s 89 conflict letter to the
Chief Executive**. ⛔ **Do not rebuild it in the OneDrive folder — point to it.**

---

# P2 — CURRENT.md
⭐ **Built here** at `wc2024227/CURRENT.md`. **Copy the same pattern into the OneDrive folder**, and
mark every pre-31-July FINAL there as superseded **inside the file**, as has been done here.

---

# ⚠️ BEFORE ACTING ON ANY FURTHER AUDIT OF THIS MATTER
**The attachment numbering differs between the two sets. Check which one an audit is describing.**

| | The OneDrive / audit set | ⭐ **This repository** |
|---|---|---|
| ATT16 | the IME Guideline | **Anti-Discrimination Act 1991** |
| ATT18 | psychosocial material | **IME Guideline** |
| ATT20 | an older DoH-framed policy | **AD Act, current to 19 May 2025** |
| ATT21 | HR Policy E12 | **Information Privacy Act 2009** |
| ATT24 | HR Policy E12 / QH-POL-140 | **WHS Regulation 2011** |

⛔ **An audit finding about "ATT24" means different documents in the two sets.** Three audits have now
been reconciled on that basis; the record is at `wc2024227/CURRENT.md`.

## ⭐ AND THE SEARCH RULE THAT CAUSED A REAL ERROR
Grepping a PDF **as a binary** silently misses compressed text and returns confident false negatives.
⇒ **Always `pdftotext` first.** An earlier search here concluded the AD Act had never been raised.
**It had — twice, on 17 and 30 July 2026.**
