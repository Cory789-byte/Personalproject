# The Hand — Second Assembly · Audio Edition

A 22-episode spoken-word series covering the whole of *The Hand: What the Work Was
Worth (Second Assembly)* — all ten grounds, all five annexures, and all forty
questions for Tom.

Everything here is generated from plain-text scripts by `build.py`, so any line can
be corrected and that episode re-rendered on its own.

---

## Listen

`audio/` holds the finished files. They are stitched, not 22 separate tracks, and
each carries **chapter markers** — so one long file still lets a player jump
straight to a ground.

| File | Runtime | Size | Contents |
|---|---|---|---|
| `The-Hand-Part-1-The-Story.mp3` | 1:00:38 | 28 MB | Episodes 0–11 — how to listen, Point 209, the ten grounds |
| `The-Hand-Part-2-The-Record.mp3` | 39:40 | 18 MB | Episodes 12–21 — the annexures, and the forty questions |
| `The-Hand-Complete.mp3` | 1:40:19 | 46 MB | All 22 chapters in one file |
| `The-Hand-Questions.mp3` | 18:19 | 8 MB | Annexure E alone, for the room |
| `00_name-check.mp3` | 3:56 | 2 MB | Pronunciation audit — see below |

Two parts rather than one file because a single 46 MB attachment is over the limit
on most things you would send it through. The seam is the natural one: the
narrative ends, the apparatus begins.

`audio/episodes/` holds the 22 per-episode renders. They are regenerable build
output and are not tracked — run `build.py` to recreate them.

### The chapters

| # | Episode | Covers |
|---|---------|--------|
| 0 | How to Listen | Preface, the evidence grades, the promise |
| 1 | Point 209 | Prologue — Tunisia, 27 March 1943 |
| 2 | Balslev | Ground one — Funen, and the war of 1864 |
| 3 | Levendale | Ground two — Tasmania, 1873 |
| 4 | Launceston | Ground three — Mabel, and the discrepancy |
| 5 | Turakina | Ground four — the crossing, and the two Gordons |
| 6 | Pākaraka | Ground five — the woolshed and the title underneath |
| 7 | The River | Ground six — Whanganui, and 24 years of litigation |
| 8 | Tebaga Gap | Ground seven — the signatures, and two hands |
| 9 | The Shed and the Works | Ground eight — shearer, knife hand |
| 10 | 1966 | Ground nine — where the lines meet |
| 11 | The Gold Coast | Ground ten — ten places, three crossings |
| 12 | The Lines | Annexure A — every person, with its grade |
| 13 | A Timeline | Annexure B — the book as dates |
| 14 | What Is Record and What Is Not | Annexure C — including the four corrections |
| 15 | The Searches | Annexure D — twelve searches, and what each costs |
| 16 | How to Run a Sitting | Annexure E — the method |
| 17 | Sitting One — Tame | Questions 1–12 |
| 18 | Sitting Two — The Marae and the Land | Questions 13–21 |
| 19 | Sitting Three — Harriet, Maria, the Seven | Questions 22–28 |
| 20 | Sitting Four — The Balsley Side | Questions 29–35 |
| 21 | Sitting Five — You, Kiel, Now | Questions 36–40 |

### The five question episodes

Episodes 17–21 read the forty questions of Annexure E one at a time, with a gap
after each. They work two ways:

- **Before a sitting** — listen alone, so on the day you can look at Tom instead of
  reading off a page.
- **In the room** — let them ask. The built-in gap is deliberately *too short*.
  Hit pause after each question and let the real silence run. The pause is where
  the good material lives.

---

## The editorial rules this series keeps

The book's own discipline had to survive the move into audio, because a voice
reading aloud makes everything sound settled:

- **The grades are spoken.** RECORDED, UNVERIFIED, INFERRED, NOT ESTABLISHED and
  BROKEN are read out loud wherever the book marks them, not quietly dropped for
  the sake of flow.
- **Nothing is put in anybody's mouth.** No invented dialogue, no invented interior
  life, no dramatisation. Where a scene is described, the document it comes from is
  named in the narration.
- **The distinction is never used as an exit.** The Levendale and Maxwell passages
  keep the book's exact position: nobody in these pages did the removing, everybody
  in these pages ate off it.
- **The whakapapa boundary is stated, twice.** The Tamou line beyond the whānau's
  own sheet is not this book's to write. Episode 0 says so; episode 16 says so
  again before the questions begin.
- **The corrections are read out.** All four of them, in episode 14.

---

## Pronunciation — read this before you share it

The narrator is a neural New Zealand voice. It is clear and it is natural, but it
is synthetic, and **it does not speak te reo Māori.** Two specific limits:

1. **Macrons are stripped by the engine before synthesis.** `Pākaraka` and
   `Pakaraka` produce byte-identical audio (verified by measurement). Long vowels
   are therefore short unless respelled in `pronunciation.json`.
2. **A word-initial `ng` is not in English phonology,** so `Ngā`, `Ngāti` and
   `Ngārimu` are approximations no respelling can fully fix in this engine.

**So: listen to `audio/00_name-check.mp3` first.** It reads all 56 difficult names
once each, numbered. Note the ones that are wrong, add spoken forms to
`pronunciation.json`, and re-run the build for the affected episodes.

If any of this is going to the whānau or to the marae, the honest recommendation is
to re-record at least the names — and ideally episodes 6, 7, 16 and 17–21 — in a
human voice, preferably a whānau voice. A synthetic voice mispronouncing this
family's own names is not a detail in a book that argues names were the only thing
that got passed down.

---

## Building

```bash
python3 -m venv venv
./venv/bin/pip install edge-tts imageio-ffmpeg

./venv/bin/python build.py            # render all 22 episodes -> audio/episodes/
./venv/bin/python build.py 06 17      # only episodes 06 and 17
./venv/bin/python build.py --check    # the name-check track
./venv/bin/python stitch.py           # stitch into the files in audio/
```

Edit a script, re-render just that episode, re-run `stitch.py`. Nothing else has
to be rebuilt.

`build.py` synthesises each block, inserts real silence for every `[[PAUSE n]]`,
concatenates, applies `loudnorm` so all episodes sit at the same level, and writes
ID3 tags. `manifest.json` records every episode's runtime, and `stitch.py` reads it to
place the chapter marks.

Voice, pace and pitch are the constants at the top of `build.py`:

```python
VOICE = "en-NZ-MitchellNeural"   # try en-AU-WilliamNeural for an Australian read
RATE  = "-7%"                    # slower = more measured
PITCH = "-2Hz"
```

### Script format

`scripts/*.md` are plain text with a small header. Blank lines separate spoken
blocks; `[[PAUSE 1.5]]` inserts 1.5 seconds of silence.

```
TITLE: Launceston
NUMBER: 4
SUBTITLE: Ground three — a two-hundred-kilometre discrepancy
---
The Hand. Episode four.

[[PAUSE 1.2]]

Two hundred kilometres of discrepancy.
```

Edit the prose, re-run that episode, done. The scripts are the master; the MP3s are
build output.
