#!/usr/bin/env python3
"""
clock_ocr.py — Burnt-in clock OCR / timeline-regression demonstrator for Axon BWC clips.

Purpose
-------
Some body-worn-camera exports carry a burnt-in (pixel-rendered) date/time stamp.
When two officer clips that are labelled as consecutive actually OVERLAP on the
camera's own continuous timeline, the burnt-in clock visibly counts *backwards*
across the cut between them. This tool renders the boundary frames of two clips,
OCRs the burnt-in clock region, and prints the read timecodes so the regression
can be shown frame-by-frame in court.

It is media-agnostic and contains no matter-specific data — safe to commit.

Typical use (QPS v Shepherd, the verified 17.26 s arrest -> Tom regression):
    python3 clock_ocr.py \
        --clip-a "Exhibit_#4_DAVIES_BWCF_-_arrest_of_SHEPHERD.mp4" \
        --clip-b "Exhibit_#4_DAVIES_BWCF_-_Speaking_to_Tom_where_Tom_lies_about_deleting_footage.mp4" \
        --tail-seconds 20 --head-seconds 5 \
        --outdir ./clock_frames

Dependencies (already used elsewhere in this repo):
    pip install av rapidocr-onnxruntime pillow numpy
(`av` bundles its own ffmpeg libraries, so no ffmpeg binary is required.)

Outputs
-------
- PNG frames for the tail of clip A and head of clip B (so you can eyeball them).
- A CSV (clock_ocr_results.csv) of: clip, frame_pts_seconds, ocr_text, parsed_time.
- A console summary of the first/last parsed clock value per clip and, if both
  clips parse, the apparent regression in seconds across the boundary.
"""
import argparse
import csv
import os
import re
import sys

try:
    import av
except ImportError:
    sys.exit("Missing dependency: pip install av")
try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("Missing dependency: pip install pillow numpy")

# OCR is loaded lazily so --no-ocr (frame dump only) works without rapidocr.
_OCR = None


def get_ocr():
    global _OCR
    if _OCR is None:
        try:
            from rapidocr_onnxruntime import RapidOCR
        except ImportError:
            sys.exit("Missing dependency: pip install rapidocr-onnxruntime "
                     "(or pass --no-ocr to only dump frames)")
        _OCR = RapidOCR()
    return _OCR


# Matches HH:MM:SS (optionally with date prefix or fractional seconds) in OCR text.
TIME_RE = re.compile(r'(\d{1,2}):(\d{2}):(\d{2})')


def parse_clock(text):
    m = TIME_RE.search(text.replace(' ', ''))
    if not m:
        return None
    h, mn, s = (int(x) for x in m.groups())
    if h > 23 or mn > 59 or s > 59:
        return None
    return h * 3600 + mn * 60 + s, f"{h:02d}:{mn:02d}:{s:02d}"


def crop_region(img, crop):
    """crop = (left, top, right, bottom) as fractions 0..1, or None for full frame."""
    if not crop:
        return img
    w, h = img.size
    l, t, r, b = crop
    return img.crop((int(l * w), int(t * h), int(r * w), int(b * h)))


def iter_window_frames(path, side, seconds, fps_sample):
    """Yield (pts_seconds, PIL.Image) for a window at the start or end of a clip.

    side='head' -> first `seconds`; side='tail' -> last `seconds`.
    fps_sample = how many frames per second to sample (1 keeps it light).
    """
    container = av.open(path)
    stream = container.streams.video[0]
    duration = float(stream.duration * stream.time_base) if stream.duration else None
    if duration is None:
        # Fall back to container duration.
        duration = float(container.duration) / 1_000_000 if container.duration else None
    if duration is None:
        raise RuntimeError(f"Could not determine duration for {path}")

    if side == 'head':
        lo, hi = 0.0, min(seconds, duration)
    else:
        lo, hi = max(0.0, duration - seconds), duration

    # Seek near the window start to avoid decoding the whole file.
    if lo > 0:
        container.seek(int(lo / stream.time_base), stream=stream, any_frame=False, backward=True)

    last_emit = -1.0
    step = 1.0 / fps_sample if fps_sample > 0 else 0.0
    for frame in container.decode(stream):
        pts = float(frame.pts * stream.time_base) if frame.pts is not None else None
        if pts is None:
            continue
        if pts < lo:
            continue
        if pts > hi:
            break
        if step and pts - last_emit < step:
            continue
        last_emit = pts
        yield pts, frame.to_image()
    container.close()


def process_clip(path, side, seconds, fps_sample, crop, outdir, do_ocr, writer, label):
    ocr = get_ocr() if do_ocr else None
    parsed = []
    base = os.path.splitext(os.path.basename(path))[0][:40]
    for pts, img in iter_window_frames(path, side, seconds, fps_sample):
        fname = os.path.join(outdir, f"{label}_{base}_{pts:08.3f}.png")
        crop_region(img, crop).save(fname)
        text, ptime = "", ""
        if do_ocr:
            arr = np.array(crop_region(img, crop).convert("RGB"))
            result, _ = ocr(arr)
            text = " ".join(r[1] for r in result) if result else ""
            pc = parse_clock(text)
            if pc:
                parsed.append((pts, pc[0], pc[1]))
                ptime = pc[1]
        writer.writerow([label, f"{pts:.3f}", text, ptime])
        print(f"  [{label}] pts={pts:8.3f}s  ocr='{text[:50]}'  clock={ptime}")
    return parsed


def parse_crop(crop_str):
    """Turn a 'left,top,right,bottom' string into a 4-tuple, or None if empty."""
    if not crop_str:
        return None
    crop = tuple(float(x) for x in crop_str.split(","))
    if len(crop) != 4:
        raise ValueError("--crop needs 4 comma-separated fractions: left,top,right,bottom")
    return crop


def run_pair(clip_a, clip_b, tail_seconds=20.0, head_seconds=5.0, fps_sample=2.0,
             crop=None, outdir="./clock_frames", do_ocr=True):
    """Render + OCR the boundary frames of two clips; returns (pa, pb, regression).

    `regression` is clip_A_last_clock - clip_B_first_clock in seconds (positive =
    the burnt-in clock runs backwards across the cut), or None if not computable.
    Reusable entry point for orchestrators (see fetch_and_clock_ocr.py).
    """
    os.makedirs(outdir, exist_ok=True)
    csv_path = os.path.join(outdir, "clock_ocr_results.csv")
    with open(csv_path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["clip", "frame_pts_seconds", "ocr_text", "parsed_clock"])
        print(f"== Clip A (tail {tail_seconds}s): {clip_a}")
        pa = process_clip(clip_a, "tail", tail_seconds, fps_sample,
                          crop, outdir, do_ocr, writer, "A")
        print(f"== Clip B (head {head_seconds}s): {clip_b}")
        pb = process_clip(clip_b, "head", head_seconds, fps_sample,
                          crop, outdir, do_ocr, writer, "B")

    print(f"\nFrames + CSV written to: {outdir}")
    regression = None
    if do_ocr and pa and pb:
        a_last = max(pa, key=lambda x: x[0])      # latest-pts frame of clip A
        b_first = min(pb, key=lambda x: x[0])     # earliest-pts frame of clip B
        print(f"\nClip A last burnt-in clock read : {a_last[2]} (at file pts {a_last[0]:.3f}s)")
        print(f"Clip B first burnt-in clock read: {b_first[2]} (at file pts {b_first[0]:.3f}s)")
        regression = a_last[1] - b_first[1]
        if regression > 0:
            print(f"\n*** BURNT-IN CLOCK REGRESSION: clip B's clock starts ~{regression}s "
                  f"BEFORE clip A's clock ends — the timecode runs BACKWARDS across the cut. ***")
        else:
            print(f"\nNo backward regression detected at the sampled frames "
                  f"(delta {regression}s). Widen --tail-seconds/--head-seconds or set --crop "
                  f"to the clock region and re-run.")
    elif do_ocr:
        print("\nOCR did not parse a clock in one or both clips. "
              "Set --crop to the burnt-in clock region (bottom strip) and re-run, "
              "or inspect the dumped PNGs manually.")
    return pa, pb, regression


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clip-a", required=True, help="First clip (the one that ENDS at the boundary)")
    ap.add_argument("--clip-b", required=True, help="Second clip (the one that STARTS at the boundary)")
    ap.add_argument("--tail-seconds", type=float, default=20.0,
                    help="Seconds from the END of clip A to sample (default 20)")
    ap.add_argument("--head-seconds", type=float, default=5.0,
                    help="Seconds from the START of clip B to sample (default 5)")
    ap.add_argument("--fps-sample", type=float, default=2.0,
                    help="Frames/sec to sample in each window (default 2)")
    ap.add_argument("--crop", default="",
                    help="Clock region as 'left,top,right,bottom' fractions 0..1 "
                         "(e.g. '0.55,0.92,1.0,1.0' for bottom-right). Empty = full frame.")
    ap.add_argument("--outdir", default="./clock_frames")
    ap.add_argument("--no-ocr", action="store_true", help="Only dump frames, skip OCR")
    args = ap.parse_args()

    try:
        crop = parse_crop(args.crop)
    except ValueError as e:
        sys.exit(str(e))

    run_pair(args.clip_a, args.clip_b, args.tail_seconds, args.head_seconds,
             args.fps_sample, crop, args.outdir, do_ocr=not args.no_ocr)


if __name__ == "__main__":
    main()
