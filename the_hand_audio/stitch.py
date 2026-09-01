#!/usr/bin/env python3
"""
Stitch the per-episode MP3s into a small number of listenable files,
with embedded chapter markers so a single long file is still navigable.

  ./venv/bin/python stitch.py

Writes into audio/:
  The-Hand-Complete.mp3    every episode in order, one chapter each
  The-Hand-Questions.mp3   the sitting episodes only, for use in the room
"""
import json, os, re, subprocess, tempfile
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
HERE   = os.path.dirname(os.path.abspath(__file__))
EPISODES = os.path.join(HERE, "audio", "episodes")
AUDIO    = os.path.join(HERE, "audio")
ALBUM  = "The Hand — What the Work Was Worth (Second Assembly)"
ARTIST = "The Hand — Second Assembly"

# Kept in two parts: a single file of the whole book is ~46 MB, which is over
# the limit on most things you would send it through. The seam is the natural
# one — the narrative ends and the apparatus begins.
BUILDS = [
    {"out": "The-Hand-Part-1-The-Story.mp3",
     "title": "The Hand — Part 1: The Story",
     "episodes": range(0, 12),
     "desc": "How to listen, Point 209, and the ten grounds"},
    {"out": "The-Hand-Part-2-The-Record.mp3",
     "title": "The Hand — Part 2: The Record and the Questions",
     "episodes": range(12, 22),
     "desc": "Annexures A-E: the lines, the timeline, the searches, the forty questions"},
    {"out": "The-Hand-Questions.mp3",
     "title": "The Hand — The Questions",
     "episodes": range(16, 22),
     "desc": "Annexure E on its own: how to run a sitting, and the forty questions"},
    {"out": "The-Hand-Complete.mp3",
     "title": "The Hand — Complete",
     "episodes": range(0, 22),
     "desc": "The whole book in one file: ten grounds, five annexures, forty questions"},
]

def duration(path):
    err = subprocess.run([FFMPEG, "-i", path, "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    for line in err.splitlines()[::-1]:
        if "time=" in line:
            t = line.split("time=")[1].split(" ")[0]
            h, m, s = t.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"could not read duration of {path}")

def fmt(sec):
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def esc(s):
    """Escape ffmetadata special characters."""
    return re.sub(r"([=;#\\\n])", r"\\\1", s)

def main():
    manifest = json.load(open(os.path.join(HERE, "manifest.json"), encoding="utf-8"))
    by_num = {int(e["number"]): e for e in manifest}

    for spec in BUILDS:
        eps = [by_num[n] for n in spec["episodes"] if n in by_num]
        if not eps:
            print(f"skip {spec['out']}: no episodes found")
            continue

        work = tempfile.mkdtemp(prefix="stitch_")
        listfile = os.path.join(work, "list.txt")
        meta     = os.path.join(work, "meta.txt")

        with open(listfile, "w", encoding="utf-8") as f:
            for e in eps:
                f.write(f"file '{os.path.join(EPISODES, e['file'])}'\n")

        lines = [";FFMETADATA1",
                 f"title={esc(spec['title'])}",
                 f"album={esc(ALBUM)}",
                 f"artist={esc(ARTIST)}",
                 f"album_artist={esc(ARTIST)}",
                 "genre=Audiobook",
                 f"comment={esc(spec['desc'])}", ""]
        t = 0.0
        for e in eps:
            d = duration(os.path.join(EPISODES, e["file"]))
            start, end = int(t * 1000), int((t + d) * 1000)
            lines += ["[CHAPTER]", "TIMEBASE=1/1000",
                      f"START={start}", f"END={end}",
                      f"title={esc(e['number'] + '. ' + e['title'])}", ""]
            t += d
        open(meta, "w", encoding="utf-8").write("\n".join(lines))

        out = os.path.join(AUDIO, spec["out"])
        r = subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", listfile,
                            "-i", meta, "-map_metadata", "1", "-map", "0:a",
                            "-c", "copy", "-id3v2_version", "3", "-write_id3v1", "1",
                            out], capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(r.stderr[-1500:])
        print(f"  ✓ {spec['out']:26s} {fmt(t):>8s}  "
              f"{os.path.getsize(out)//1024//1024:>3d} MB  {len(eps)} chapters")

if __name__ == "__main__":
    main()
