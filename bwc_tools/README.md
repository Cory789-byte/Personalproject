# bwc_tools — body-worn-camera forensic helpers

Generic, matter-agnostic tooling for analysing Axon / body-worn-camera exports.
No client data lives here (matter-specific artefacts stay in the gitignored
`analysis_output/`).

## clock_ocr.py — burnt-in clock regression demonstrator

Renders the boundary frames of two clips (the tail of clip A, the head of clip
B), OCRs the burnt-in date/time stamp, and reports the read timecodes. When two
clips labelled as consecutive actually overlap on the camera's continuous
timeline, the burnt-in clock counts **backwards** across the cut — this tool
turns that into a frame-by-frame, courtroom-ready exhibit.

It complements the **arithmetic** proof (which stands on the container
`creation_time` + duration metadata alone): for QPS v Shepherd the DAVIES
"arrest" clip (creation 02:34:21 AEST + 271.256 s → ends 02:38:52.26) and the
"Tom lies about deleting footage" clip (creation 02:38:35 AEST) overlap by
**17.26 s**, so the burnt-in clock jumps back ~17 s at the boundary.

### Install
```
pip install av rapidocr-onnxruntime pillow numpy
```
(`av` bundles ffmpeg libraries; no ffmpeg binary needed.)

### Run
```
python3 clock_ocr.py \
  --clip-a "Exhibit_#4_DAVIES_BWCF_-_arrest_of_SHEPHERD.mp4" \
  --clip-b "Exhibit_#4_DAVIES_BWCF_-_Speaking_to_Tom_where_Tom_lies_about_deleting_footage.mp4" \
  --tail-seconds 20 --head-seconds 5 --outdir ./clock_frames
```

If OCR doesn't pick up the clock, set `--crop` to the burnt-in stamp region as
fractions `left,top,right,bottom` (Axon usually burns it into the bottom strip),
e.g. `--crop 0.0,0.93,1.0,1.0`, and re-run.

### Why it can't run in the cloud session
The source MP4s (44–138 MB each) live in Drive/OneDrive; the Drive connector
session-expires on binary downloads that large, so the frames must be rendered
where the media is local. Pull the clips with `../onedrive_tools/onedrive_fetch.py`
(or download from Drive in a browser), then run this script against the files.
