"""Transcribe a court recording with faster-whisper large-v3, word timestamps.

Writes segments in the same field layout as MENTION_7AUG2026_segments.jsonl
(start, end, text, avg_logprob, no_speech_prob, compression_ratio,
words: [{w, s, e, p}]) so the existing prosody / diarisation tools apply.

Usage: python -I transcribe_court.py AUDIO OUT.jsonl LOG
"""
import json, sys, time

audio, out, logp = sys.argv[1], sys.argv[2], sys.argv[3]
log = open(logp, "a", buffering=1)
from faster_whisper import WhisperModel

t0 = time.time()
model = WhisperModel("large-v3", device="cpu", compute_type="int8", cpu_threads=4)
log.write(f"model loaded {time.time()-t0:.0f}s\n")
segments, info = model.transcribe(
    audio, language="en", beam_size=5, word_timestamps=True,
    vad_filter=True, vad_parameters={"min_silence_duration_ms": 400},
    condition_on_previous_text=False,
)
log.write(f"duration {info.duration:.1f}s  lang {info.language}\n")
n = 0
with open(out, "w", encoding="utf-8") as fh:
    for s in segments:
        fh.write(json.dumps({
            "start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
            "avg_logprob": s.avg_logprob, "no_speech_prob": s.no_speech_prob,
            "compression_ratio": s.compression_ratio,
            "words": [{"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2), "p": w.probability}
                      for w in (s.words or [])],
        }, ensure_ascii=False) + "\n")
        fh.flush()
        n += 1
        log.write(f"  seg {n}  t={s.end:.1f}s  elapsed {time.time()-t0:.0f}s\n")
log.write(f"DONE {n} segments {time.time()-t0:.0f}s\n")
