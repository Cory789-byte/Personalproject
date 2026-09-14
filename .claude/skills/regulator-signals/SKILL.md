---
name: regulator-signals
description: >
  Read and score every communication that touches the Workers' Compensation Regulator
  (Matheson, OIR Appeals, panel counsel) or Metro South Health (Ruttan/MSH Legal, Harrison,
  Hughes, Forrest, Taylor, Reese, LBH HR, Injury Management) in WC/2024/227 and the employment
  track. Use whenever a letter, email, list, outline, transcript or order arrives from or is
  drafted to either of them; whenever Cory asks what a reply "means", why a date was chosen,
  what they will do next, whether a signal compounds, or to re-run the prediction / scenario /
  meta-analysis; and on 25 Sep, 30 Sep and 1 Oct 2026 without being asked. Also use before
  sending anything to them, to check the register and the disciplines.
---

# Regulator and MSH signals — read, ledger, score, predict

## Why this exists
The Regulator's behaviour in this matter is regular enough to be modelled, and it has been:
seven signal classes, a dated watchlist, five falsifiers, pre-committed conditional re-scores,
and eighteen predictions written to be scored. The failure this skill prevents is reading a new
letter from memory and impression instead of against the model, and forgetting to score what
the model already said.

## Canonical sources (read in this order)
1. `wc2024227/skill/references/REGULATOR-SIGNALS-the-full-data-set.md` — the seven classes:
   timing-by-consequence · register (operational / position / legal) · authorship & production ·
   selection · representation & appearance · sequencing · anchoring to the 13 May SOFC formula.
   §B watchlist, §C falsifiers, §D verified-vs-inferred.
2. `PREDICTIONS-13SEP2026-scoreable.md` — B1–B8, Part F (F1 re-scores, F2.1–F2.6), E1–E18.
   E18 holds Cory's prediction and the model's for the 25th, side by side.
3. `SCENARIO-MODEL-13SEP2026.md` — Addendum 2 §2: the pre-committed re-scores for each reading
   of the 25 September letter. Apply them, do not re-argue them.
4. `HOW-THE-REGULATOR-CONCEDES.md` — Guide 5.1 mechanism; §6 conference mechanics; FDO(3) points.
5. `MENTION-what-he-was-working-at.md` §9 — the map of Dwyer's sentences to the 9 Sep letters.
6. `index/COMMS_SIGNAL_LEDGER.tsv` — every dated communication with latency, register, formula,
   consequence, author field. `scripts/comms_signals.py report` prints the current read.

## Method — on every inbound communication
1. **Ledger first.** `python3 scripts/comms_signals.py add --id Rnn --date … --dir IN --party
   Regulator --track WC --doc "…" --kind reply|holding|position|legal|ack --answers Rxx
   --register … --formula Y|N --consequence "…" --author_field "…" --source …`. Latency is
   computed from the row it answers.
2. **Register.** `comms_signals.py register FILE.txt` on the pdftotext of the letter. Operational
   = a holding reply, the real answer is still coming. Position = the formula; check whether the
   16 Jul undertaking ("should our position change… we will advise") is engaged. Legal = the
   considered answer; read the author field (metadata is read-only — ⛔ never cited, never in
   correspondence).
3. **Anchor.** Is *"as outlined in our Statement of Facts and Contentions"* present, absent, or
   replaced? Absent = the anchor has moved (class 7).
4. **Selection.** What did they concede, maintain, chase, stay silent on? Thirteen tabs; Tab 31
   ("MSH has been asked" vs silence); footing (silence expected).
5. **Apply the pre-committed re-scores** (Scenario Addendum 2 §2; Predictions E18) and write the
   outcome into every prediction the letter scores (`comms_signals.py score` lists them).
   Replace `______` with the outcome and the date. Never revise a prediction after the fact;
   add a new numbered entry that says what was wrong and why.
6. **Watchlist.** Update §B of REGULATOR-SIGNALS: which items fired, which are next.
7. **Write the read** as a new E-entry in PREDICTIONS (verified layer first, inferred layer
   marked), and a one-paragraph note to Cory: what it means, what it does not, what to watch next.

## Method — before any outbound communication
- Register check: process, not grievance. Premise first. Ask, never allege. State the
  chronology, never the motive. Quote the Commissioner as "the Commissioner indicated", once.
- Disciplines (CLAUDE.md / ONBOARDING.md): ⛔ the never-voiced items; ⛔ "fraud"/"malicious"/
  "plot"/"corruption" never in the WC track; ⛔ "a significant contributing factor", never
  "major"; ⛔ reinstatement wording; ⛔ PID content never set out; metadata never used.
- Consequence: does the letter attach one (a date, a step that follows, a costs reservation)?
  Class 1 says a request without a consequence is answered at the limit or late.
- Timing: nothing to them before the 25th; the 1 Oct letter to the Registry is not optional
  (FDO(3) direction 5 — abeyance and lapse under r 230).

## Method — MSH (employment track)
Same ledger, `--track EMP`. MSH latencies are short (1–3 days) on operational matters and long
where money or a decision is involved (the 2024 pattern at Predictions A2). Anything MSH says to
the Commission (K-LM26/729) or to the Regulator is class 4 material and is admitted at ¶¶263–268.

## Outputs
- ledger row(s) · register verdict · scored predictions · E-entry · watchlist update · one
  paragraph to Cory. Commit with a message that names the communication and the predictions
  scored.
