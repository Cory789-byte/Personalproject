#!/usr/bin/env python3
"""
The Hand — Second Assembly : audio build.

Renders scripts/*.md into audio/*.mp3 using a neural New Zealand voice,
with real silences between beats, loudness normalisation and ID3 tags.

  ./venv/bin/python build.py            # build every episode
  ./venv/bin/python build.py 06 17      # build only those episode numbers
  ./venv/bin/python build.py --check    # build the pronunciation name-check track
"""
import asyncio, json, os, re, ssl, subprocess, sys, shutil, tempfile

import edge_tts, edge_tts.communicate as C
import imageio_ffmpeg

# --- environment ------------------------------------------------------------
CA_BUNDLE = "/root/.ccr/ca-bundle.crt"          # agent-proxy trust anchor
if os.path.exists(CA_BUNDLE):
    C._SSL_CTX = ssl.create_default_context(cafile=CA_BUNDLE)
PROXY = os.environ.get("HTTPS_PROXY") or None
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

VOICE = "en-NZ-MitchellNeural"   # New Zealand male; the book's centre of gravity
RATE  = "-7%"                    # measured documentary read, not a news read
PITCH = "-2Hz"
ALBUM  = "The Hand — What the Work Was Worth (Second Assembly)"
ARTIST = "The Hand — Second Assembly"

HERE    = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, "scripts")
OUT     = os.path.join(HERE, "audio", "episodes")   # per-episode renders (regenerable)
DELIV   = os.path.join(HERE, "audio")                # stitched deliverables live here
CONCURRENCY = 6

# --- pronunciation ----------------------------------------------------------
def load_map():
    p = os.path.join(HERE, "pronunciation.json")
    if not os.path.exists(p):
        return {}
    return json.load(open(p, encoding="utf-8")).get("map", {})

PRON = load_map()

def spoken(text):
    """Apply pronunciation overrides to engine-bound text only."""
    for src in sorted(PRON, key=len, reverse=True):
        text = re.sub(rf"(?<!\w){re.escape(src)}(?!\w)", PRON[src], text)
    return text

# --- script parsing ---------------------------------------------------------
PAUSE_RE = re.compile(r"^\[\[PAUSE\s+([0-9.]+)\]\]$")

def parse(path):
    raw = open(path, encoding="utf-8").read()
    head, body = raw.split("\n---\n", 1)
    meta = {}
    for line in head.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()

    blocks, buf = [], []
    def flush():
        if buf:
            blocks.append(("say", " ".join(buf).strip()))
            buf.clear()
    for line in body.splitlines():
        line = line.strip()
        m = PAUSE_RE.match(line)
        if m:
            flush()
            blocks.append(("pause", float(m.group(1))))
        elif not line:
            flush()
        else:
            buf.append(line)
    flush()
    return meta, blocks

# --- audio primitives -------------------------------------------------------
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg failed:\n{' '.join(cmd[:6])}...\n{r.stderr[-1500:]}")
    return r

def silence(seconds, path):
    run([FFMPEG, "-y", "-f", "lavfi", "-i",
         "anullsrc=channel_layout=mono:sample_rate=24000",
         "-t", f"{seconds:.3f}", "-c:a", "libmp3lame", "-b:a", "64k", "-ar", "24000",
         "-ac", "1", path])

async def synth(text, path, sem):
    async with sem:
        last = None
        for attempt in range(4):                       # network retry w/ backoff
            try:
                c = edge_tts.Communicate(spoken(text), VOICE, proxy=PROXY,
                                         rate=RATE, pitch=PITCH)
                await c.save(path)
                if os.path.getsize(path) > 0:
                    return
                raise RuntimeError("empty audio")
            except Exception as e:                     # noqa: BLE001
                last = e
                await asyncio.sleep(2 ** attempt)
        raise RuntimeError(f"TTS failed after retries: {last}")

def normalise_and_tag(concat_list, out_path, meta):
    tmp = f"{out_path}.{os.getpid()}.tmp.mp3"   # pid-scoped: concurrent builds cannot clash
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
         "-c", "copy", tmp])
    num = meta.get("number", "0")
    title = meta.get("title", "Untitled")
    tags = [
        "-metadata", f"title={num}. {title}",
        "-metadata", f"album={ALBUM}",
        "-metadata", f"artist={ARTIST}",
        "-metadata", f"album_artist={ARTIST}",
        "-metadata", f"track={num}",
        "-metadata", "genre=Audiobook",
        "-metadata", f"comment={meta.get('subtitle','')}",
    ]
    # loudnorm brings every episode to the same perceived level
    run([FFMPEG, "-y", "-i", tmp,
         "-af", "loudnorm=I=-18:TP=-2:LRA=11",
         "-c:a", "libmp3lame", "-b:a", "64k", "-ar", "24000", "-ac", "1",
         *tags, out_path])
    os.remove(tmp)

def duration(path):
    r = subprocess.run([FFMPEG, "-i", path, "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    for line in r.splitlines()[::-1]:
        if "time=" in line:
            t = line.split("time=")[1].split(" ")[0]
            h, m, s = t.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0

def fmt(sec):
    return f"{int(sec // 60)}:{int(sec % 60):02d}"

# --- episode build ----------------------------------------------------------
async def build(path, sem):
    meta, blocks = parse(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    out_path = os.path.join(OUT, f"{stem}.mp3")
    work = tempfile.mkdtemp(prefix=f"{stem}_")
    try:
        jobs, parts = [], []
        for i, (kind, val) in enumerate(blocks):
            p = os.path.join(work, f"{i:04d}.mp3")
            parts.append(p)
            if kind == "say":
                jobs.append(synth(val, p, sem))
            else:
                silence(val, p)
        await asyncio.gather(*jobs)

        listfile = os.path.join(work, "list.txt")
        with open(listfile, "w", encoding="utf-8") as f:
            for p in parts:
                if os.path.exists(p) and os.path.getsize(p) > 0:
                    f.write(f"file '{p}'\n")
        normalise_and_tag(listfile, out_path, meta)
        d = duration(out_path)
        print(f"  ✓ {stem:28s} {fmt(d):>6s}  {os.path.getsize(out_path)//1024:>5d} KB  "
              f"{meta.get('title','')}", flush=True)
        return stem, meta, d
    finally:
        shutil.rmtree(work, ignore_errors=True)

# --- pronunciation check track ---------------------------------------------
CHECK_TERMS = [
    "Balslev", "Balsley", "Kele Balsley", "Levendale", "Portmairremener",
    "Dybbøl", "Danevirke", "Schleswig", "Funen", "Rigsarkivet",
    "Turakina", "Rangitīkei", "Whanganui", "Pākaraka", "Maxwelltown",
    "whakapapa", "whānau", "hapū", "iwi", "marae", "Pākehā", "Māori",
    "Ngā Rauru Kītahi", "Ngāti Maika", "Ngāti Ruanui", "Ngāti Porou",
    "Tītokowaru", "Ihaka Takarangi", "Waitōtara", "Nukumaru", "Tauranga Ika Pā",
    "Hikurangi", "Te Moananui-a-Kiwa Ngārimu", "Tame Kimi Tamou", "Kimi", "Pare",
    "Harriet Te Pohe Matiu", "Pukehika", "Kaipo", "Rangiwaea", "Araukuku",
    "Paratupu", "Ātihau-Whanganui", "Parininihi ki Waitōtara", "Aotea",
    "He Whiritaunoka", "Ruruku Whakatupua", "Ngāti Hāua", "tūpuna", "Rātana",
    "Tebaga Gap", "Mareth", "Spandau", "Meisser", "Kippenberger", "Freyberg",
]

async def build_check(sem):
    work = tempfile.mkdtemp(prefix="check_")
    out_path = os.path.join(DELIV, "00_name-check.mp3")
    try:
        parts, jobs = [], []
        intro = ("Name check. Every difficult name in the book, once each, slowly. "
                 "Listen for any the voice gets wrong, and note the number.")
        p0 = os.path.join(work, "0000.mp3"); parts.append(p0)
        jobs.append(synth(intro, p0, sem))
        idx = 1
        for n, term in enumerate(CHECK_TERMS, 1):
            ps = os.path.join(work, f"{idx:04d}.mp3"); idx += 1
            silence(0.7, ps); parts.append(ps)
            pt = os.path.join(work, f"{idx:04d}.mp3"); idx += 1
            jobs.append(synth(f"{n}. {term}.", pt, sem)); parts.append(pt)
        await asyncio.gather(*jobs)
        listfile = os.path.join(work, "list.txt")
        with open(listfile, "w", encoding="utf-8") as f:
            for p in parts:
                if os.path.exists(p) and os.path.getsize(p) > 0:
                    f.write(f"file '{p}'\n")
        normalise_and_tag(listfile, out_path,
                          {"number": "0", "title": "Name Check",
                           "subtitle": "Pronunciation audit track"})
        print(f"  ✓ name-check  {fmt(duration(out_path))}")
    finally:
        shutil.rmtree(work, ignore_errors=True)

# --- main -------------------------------------------------------------------
async def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(DELIV, exist_ok=True)
    sem = asyncio.Semaphore(CONCURRENCY)
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    if "--check" in sys.argv:
        await build_check(sem)
        return

    files = sorted(f for f in os.listdir(SCRIPTS) if f.endswith(".md"))
    if args:
        files = [f for f in files if any(f.startswith(a.zfill(2)) for a in args)]

    print(f"Building {len(files)} episode(s) — voice {VOICE}, rate {RATE}\n")
    results = []
    for f in files:
        results.append(await build(os.path.join(SCRIPTS, f), sem))

    total = sum(r[2] for r in results)
    print(f"\nTotal runtime: {fmt(total)} across {len(results)} episodes")
    manifest = [{"file": f"{s}.mp3", "number": m.get("number"),
                 "title": m.get("title"), "subtitle": m.get("subtitle"),
                 "seconds": round(d, 1), "runtime": fmt(d)}
                for s, m, d in results]
    json.dump(manifest, open(os.path.join(HERE, "manifest.json"), "w"), indent=2,
              ensure_ascii=False)

asyncio.run(main())
