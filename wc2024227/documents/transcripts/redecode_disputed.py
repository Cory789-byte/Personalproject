#!/usr/bin/env python3
"""
redecode_disputed.py — targeted high-effort re-decode of the WC/2024/227 mention
segments whose wording is in issue.

⛔ REQUIRES THE AUDIO. It is not in the repo. Supply:
     PRF0466309_20260807_QIRCOIR_Brisbane  (64 kbps MP3, 3,875.9 s)

Why this differs from the original whole-file run (diarise_inferential.py):
  * beam 10 / best_of 10 (was beam 5) — affordable because we decode ~4 minutes, not 65
  * temperature=0.0 ONLY, no fallback. Temperature fallback is the main source of
    plausible-but-wrong wording; on a short window we would rather fail than drift.
  * condition_on_previous_text run BOTH ways and compared. Context helps fluency and
    hurts fidelity; disagreement between the two passes is itself the signal.
  * VAD OFF. Silero VAD can clip a quiet word at a window edge — exactly the class of
    word we are chasing.
  * A domain-primed initial_prompt carrying the real vocabulary of this hearing, so the
    decoder is not guessing at "MASPER", "stressor", "Form 29", "suppressed".
  * ±6 s of padding either side of each target so no word sits on a boundary.
  * Every pass reports PER-WORD probability; the report flags any word that changes
    between passes, or stays below the threshold in all of them.

Install:  pip install faster-whisper
Run:      python3 redecode_disputed.py /path/to/audio.mp3 [--model large-v3] [--out report.json]
"""
import argparse, json, statistics, sys

# (label, start_s, end_s, what is in issue)
TARGETS = [
    ("N1  16:29 'I guess I did request'",        985.0, 1000.0,
     "small.en renders 'I didn't request' — OPPOSITE meaning on whether the Regulator was asked first"),
    ("N2  23:37-24:12 the filters answer",      1415.0, 1455.0,
     "the criterion 'effective immediately' and 'I basically just want the count'"),
    ("29:17 the nine words",                    1750.0, 1782.0,
     "'cardiac arrest' / 'respiratory distress' — the only definition of a code in the case"),
    ("A1  29:45-30:20 the amended line",        1780.0, 1825.0,
     "'Yeah,' p=0.37 — the interjection whose ATTRIBUTION was amended (A1). Check speaker change too"),
    ("N3  45:55-46:55 'actively spread'",       2750.0, 2818.0,
     "⭐ 'spread' p=0.23 surrounded by 0.98-1.00. Test 'suppressed'. THE PRIORITY TARGET"),
    ("N4  51:20-52:10 the comparator",          3080.0, 3130.0,
     "'over a six week' — 'week' p=0.44. The period over which the 42% is computed"),
]

PROMPT = (
    "Queensland Industrial Relations Commission mention. Commissioner Dwyer and the appellant "
    "Mr Shepherd. Workers' compensation appeal. Terms used: stressor, statement of facts and "
    "contentions, Form 9A, Form 24, Form 29, notice of non-party disclosure, rule 64G, disclosure, "
    "produce or swear, de novo, reasonable management action, Switchboard, MASPER registrar, "
    "Code Blue, MET call, on-call roster, directive, effective immediately, filters, retraction, "
    "union delegate, actively suppressed, fatigue, roster, AVAC, payroll."
)
LOW = 0.50

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--out", default="redecode_report.json")
    ap.add_argument("--device", default="auto")
    a = ap.parse_args()
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("faster-whisper not installed:  pip install faster-whisper")

    compute = "float16" if a.device == "cuda" else "int8"
    model = WhisperModel(a.model, device=a.device, compute_type=compute)
    report = []

    for label, s0, s1, why in TARGETS:
        clip = (max(0.0, s0 - 6.0), s1 + 6.0)
        passes = {}
        for tag, cond in (("nocontext", False), ("context", True)):
            segs, _ = model.transcribe(
                a.audio, language="en", beam_size=10, best_of=10,
                temperature=[0.0],                  # no fallback, deliberately
                condition_on_previous_text=cond,
                vad_filter=False,                   # do not let VAD clip a quiet word
                word_timestamps=True,
                initial_prompt=PROMPT,
                clip_timestamps=[clip[0], clip[1]],
            )
            passes[tag] = [{
                "start": sg.start, "end": sg.end, "text": sg.text,
                "avg_logprob": sg.avg_logprob,
                "words": [{"w": w.word, "s": w.start, "e": w.end, "p": w.probability}
                          for w in (sg.words or [])],
            } for sg in segs]

        def flat(t):
            return [w for sg in passes[t] for w in sg["words"]]
        wn, wc = flat("nocontext"), flat("context")
        tn = "".join(w["w"] for w in wn).strip()
        tc = "".join(w["w"] for w in wc).strip()

        low_both = [w["w"].strip() for w in wn if w["p"] < LOW]
        entry = {
            "label": label, "why_in_issue": why, "window": clip,
            "text_nocontext": tn, "text_context": tc,
            "passes_agree": tn == tc,
            "low_confidence_words_nocontext": low_both,
            "mean_word_p_nocontext": round(statistics.fmean([w["p"] for w in wn]), 4) if wn else None,
            "words_nocontext": wn,
        }
        report.append(entry)

        print("=" * 78)
        print(label)
        print("  why:", why)
        print("  AGREEMENT between passes:", "YES" if tn == tc else "⚠ NO — treat as unresolved")
        if tn != tc:
            print("   no-context :", tn[:300])
            print("   context    :", tc[:300])
        else:
            print("   text       :", tn[:300])
        if low_both:
            print("  ⚠ still below", LOW, ":", ", ".join(low_both[:14]))

    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("\nwrote", a.out)
    print("\n⛔ A re-decode is still MACHINE OUTPUT. Where a word carries legal weight, "
          "listen to the audio at the timestamp before amending the transcript, and log it "
          "in the AMENDMENT LOG with a confidence class.")

if __name__ == "__main__":
    main()
