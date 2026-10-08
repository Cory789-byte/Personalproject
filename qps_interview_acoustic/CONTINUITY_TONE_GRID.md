# RECORDING CONTINUITY — 2-MINUTE TONE GRID

**Matter** Shepherd v QPS — CO2500030466
**File** `Exhibit__1_BICKERY_BWCF_-_SHEPHERD_interview_at_SOUWH.wav`
**SHA-256** `f832c3af5eecd356ec82d07ed3a9ce91febe1451c3c4d0c11d10c9c41ec0923e`
**Bytes** 254,491,598 · **Duration** 3,976.4 s (1 h 06 m 16 s) · 16 kHz 16-bit stereo, channels bit-identical
**Analysed** 17 September 2026

> ⚠ **MACHINE-GENERATED — UNVERIFIED.** Surfaces a measurement for counsel to
> verify. Makes no legal determination.

## The finding

The recording carries a **periodic 177 Hz tone every 120 seconds**, audible
across the whole file. Detected by narrowband matched filter (177 Hz energy
against 140 Hz / 220 Hz reference bands, 200 ms window, 50 ms hop).

| | |
|---|---|
| Tones on the grid | **33** — 00:29.9 through 64:29.9 |
| Fitted period | **120.0038 s** (nominal 120 s; error **+3.8 ms**) |
| Residual RMS about the fitted grid | **0.128 s** |
| Largest single residual | 0.269 s (at 50.5 min) |
| Consecutive intervals | min 119.65 s · max 120.40 s · mean 120.003 s · **sd 0.205 s** |
| **Missing tones** | **0** |

Residual scatter of ±0.27 s is the detector's own temporal resolution
(50 ms hop, 200 ms analysis window, peak-picked against overlapping speech).
The underlying grid is regular to within milliseconds.

## What it supports

Between the first tone (00:29.9) and the last (64:29.9) — **64 minutes of the
66-minute file** — every 120-second interval is present and none deviates from
120 s by more than 0.40 s.

⇒ **No excision longer than approximately 0.4 s occurred anywhere in that span.**
A cut of any greater length would either have removed a tone (the count would
fall and a 240 s interval would appear) or shortened the interval containing it
(no interval is short).

## What it does NOT support

1. **The first 29.9 s and the final 106 s are outside the grid** and are not
   tested by this method.
2. This tests **continuity of the audio stream as exported**. If the exported
   WAV was produced from an already-edited source, a splice upstream of the
   export would not appear here.
3. It says nothing about the **video** track, or about any other exhibit.
4. The tone's origin is not established. Its regularity and fixed 0.7 s
   duration are machine-like, but whether it is a recorder "still recording"
   marker, a room device or something else is **not determined by this analysis**
   and should be confirmed against the device documentation.

## Method

```
narrowband energy E(f) over 200 ms windows, 50 ms hop
score = E(177) / mean(E(140), E(220))
events = local maxima where score > 3.0
grid    = least-squares fit of event time against event index
```

Reproduce with the scripts at `skills/bwc-evidence-processor/scripts/`.
