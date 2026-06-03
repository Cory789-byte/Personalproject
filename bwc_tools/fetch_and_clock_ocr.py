#!/usr/bin/env python3
"""
fetch_and_clock_ocr.py — one command: pull two BWC clips from OneDrive and run
the burnt-in clock regression OCR end-to-end.

This wires ../onedrive_tools/onedrive_fetch.py (MSAL device-code auth + Microsoft
Graph streaming download — which writes straight to disk, so it sidesteps the
inline-base64 throttle that blocks large media over other connectors) into
clock_ocr.run_pair().

Why OneDrive: the source MP4s are 44-138 MB. Graph's /content endpoint streams to
disk in chunks, so the clips land locally and PyAV can decode their boundary
frames — no ffmpeg binary required.

Setup (one-off): see ../onedrive_tools/README.md (Azure app registration), then:
    pip install -r ../onedrive_tools/requirements.txt
    pip install av rapidocr-onnxruntime pillow numpy
    export ONEDRIVE_CLIENT_ID=<your-azure-app-client-id>

Usage (defaults target the verified QPS v Shepherd arrest -> Tom boundary):
    python3 fetch_and_clock_ocr.py
    # or specify your own search terms / boundary:
    python3 fetch_and_clock_ocr.py \
        --clip-a-query "arrest_of_SHEPHERD" \
        --clip-b-query "Tom_lies_about_deleting_footage" \
        --tail-seconds 20 --head-seconds 5 --crop 0.0,0.93,1.0,1.0

The first run opens a device-code prompt (sign in once; token is cached).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Make the sibling onedrive_tools package importable regardless of CWD.
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent / "onedrive_tools"))

try:
    import onedrive_fetch as od
except ImportError:
    sys.exit("Could not import onedrive_fetch. Expected it at "
             f"{_HERE.parent / 'onedrive_tools' / 'onedrive_fetch.py'}")

import clock_ocr  # same directory


def find_video(g: "od.Graph", query: str) -> dict:
    """Return the best video/mp4 OneDrive item matching `query` (by name)."""
    from urllib.parse import quote
    url = f"/me/drive/root/search(q='{quote(query)}')"
    candidates = []
    for item in g.paged(url):
        if "file" not in item:
            continue
        mime = item.get("file", {}).get("mimeType", "")
        name = item.get("name", "")
        is_video = mime.startswith("video/") or name.lower().endswith((".mp4", ".mov", ".mkv"))
        if is_video:
            candidates.append(item)
    if not candidates:
        raise SystemExit(f"No video file matched '{query}' in OneDrive. "
                         f"Try a different --clip-*-query, or run "
                         f"`onedrive_fetch.py search '{query}'` to see matches.")
    # Prefer an exact-ish name hit; otherwise the largest (full clip vs excerpt).
    q = query.lower().replace(" ", "_")
    candidates.sort(key=lambda it: (q in it.get("name", "").lower().replace(" ", "_"),
                                    it.get("size", 0)), reverse=True)
    return candidates[0]


def download_item(g: "od.Graph", item: dict, outdir: Path) -> Path:
    name = item.get("name", item.get("id"))
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / name
    item_url = f"/me/drive/items/{item['id']}"
    print(f"  downloading {name}  ({item.get('size', 0):,} bytes) ...")
    with g.get(item_url + "/content", stream=True) as r:
        with open(dest, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    print(f"  saved -> {dest}  ({dest.stat().st_size:,} bytes)")
    return dest


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--client-id", default=os.environ.get("ONEDRIVE_CLIENT_ID", ""),
                    help="Azure app (client) ID; or set ONEDRIVE_CLIENT_ID")
    ap.add_argument("--clip-a-query", default="arrest_of_SHEPHERD",
                    help="OneDrive name search for clip A (ends at the boundary)")
    ap.add_argument("--clip-b-query", default="Tom_lies_about_deleting_footage",
                    help="OneDrive name search for clip B (starts at the boundary)")
    ap.add_argument("--workdir", default="./bwc_media",
                    help="Where to download the clips (default ./bwc_media)")
    ap.add_argument("--outdir", default="./clock_frames",
                    help="Where to write frames + CSV (default ./clock_frames)")
    ap.add_argument("--tail-seconds", type=float, default=20.0)
    ap.add_argument("--head-seconds", type=float, default=5.0)
    ap.add_argument("--fps-sample", type=float, default=2.0)
    ap.add_argument("--crop", default="",
                    help="Clock region 'left,top,right,bottom' (fractions). "
                         "Axon usually burns the clock into the bottom strip, "
                         "e.g. 0.0,0.93,1.0,1.0")
    ap.add_argument("--no-ocr", action="store_true", help="Only dump frames, skip OCR")
    ap.add_argument("--reuse", action="store_true",
                    help="Skip download if the files already exist in --workdir")
    args = ap.parse_args()

    if not args.client_id:
        sys.exit("No client id. Register an Azure app (see ../onedrive_tools/README.md) "
                 "and set ONEDRIVE_CLIENT_ID or pass --client-id.")

    try:
        crop = clock_ocr.parse_crop(args.crop)
    except ValueError as e:
        sys.exit(str(e))

    workdir = Path(args.workdir)
    g = od.Graph(od.get_token(args.client_id))

    paths = []
    for label, query in (("A", args.clip_a_query), ("B", args.clip_b_query)):
        print(f"[{label}] searching OneDrive for: {query!r}")
        item = find_video(g, query)
        dest = workdir / item.get("name", item["id"])
        if args.reuse and dest.exists() and dest.stat().st_size == item.get("size", -1):
            print(f"  reusing existing {dest}")
        else:
            dest = download_item(g, item, workdir)
        paths.append(dest)

    print("\n== Running clock OCR on the boundary ==")
    clock_ocr.run_pair(str(paths[0]), str(paths[1]),
                       tail_seconds=args.tail_seconds, head_seconds=args.head_seconds,
                       fps_sample=args.fps_sample, crop=crop, outdir=args.outdir,
                       do_ocr=not args.no_ocr)


if __name__ == "__main__":
    main()
