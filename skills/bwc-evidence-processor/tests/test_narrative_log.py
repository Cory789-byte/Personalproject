"""Tests for the narrative log builder."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from narrative_log import build, _officer_from_exhibit  # noqa: E402


def _write(out: Path, stem: str, creation: str, segments: list[dict],
           scene_cuts: list[float] | None = None,
           black_frames: list[list[float]] | None = None,
           freeze_frames: list[list[float]] | None = None) -> None:
    (out / f"{stem}.transcript.json").write_text(
        json.dumps({"header": "X", "segments": segments}), encoding="utf-8"
    )
    (out / f"{stem}.integrity.json").write_text(
        json.dumps({
            "header": "X", "source": "x", "sha256": "a" * 64,
            "format": {"tags": {"creation_time": creation},
                       "duration": "120.0"},
            "streams": [],
            "scene_cuts": scene_cuts or [],
            "black_frames": black_frames or [],
            "freeze_frames": freeze_frames or [],
            "anomalies": [], "ocr_samples": [],
        }), encoding="utf-8",
    )


def mk(i, start, end, text):
    return {"index": i, "start": start, "end": end, "text": text, "words": []}


class NarrativeTests(unittest.TestCase):
    def test_officer_from_exhibit_parses_filename(self):
        self.assertEqual(
            _officer_from_exhibit("Exhibit_#3_EASTHOPE_BWCF_-_SHEPHERD_arrest"),
            "Easthope",
        )
        self.assertEqual(
            _officer_from_exhibit("CONTACOS_BWC_-_Seizure_of_dog"),
            "Contacos",
        )

    def test_build_produces_all_sections(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source").mkdir()
            out = root / "output"
            out.mkdir()
            (root / "sworn").mkdir()
            _write(out, "Exhibit_#3_EASTHOPE_BWCF_-_SHEPHERD_arrest",
                   "2025-03-22T08:06:10Z", [
                       mk(0, 0, 3, "You are under arrest."),
                       mk(1, 3, 6, "I'll turn this off for a minute."),
                       mk(2, 6, 9, "You do not have to say anything. Anything you do say may be used in evidence."),
                   ])
            _write(out, "CONTACOS_BWC_-_Seizure_of_dog",
                   "2025-03-22T09:06:10Z", [
                       mk(0, 0, 2, "I'm seizing the dog."),
                   ])
            p = build(root)
            text = p.read_text(encoding="utf-8")
            self.assertIn("MACHINE-GENERATED", text)
            self.assertIn("## 1. Dramatis personae", text)
            self.assertIn("## 2. Unified chronological feed", text)
            self.assertIn("## 3. Per-exhibit scene notes", text)
            self.assertIn("## 5. Integrity and tampering concerns", text)
            self.assertIn("Easthope", text)
            self.assertIn("Contacos", text)
            # Camera-off mention surfaced
            self.assertIn("turn this off", text.lower())

    def test_chronology_interleaves_exhibits(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source").mkdir()
            out = root / "output"
            out.mkdir()
            _write(out, "a_exhibit",
                   "2025-03-22T08:00:00Z",
                   [mk(0, 0, 2, "first event")])
            _write(out, "b_exhibit",
                   "2025-03-22T07:00:00Z",
                   [mk(0, 0, 2, "earlier event")])
            p = build(root)
            text = p.read_text(encoding="utf-8")
            # Earlier-timed exhibit should come first in the chronology
            first_idx = text.find("earlier event")
            second_idx = text.find("first event")
            self.assertGreater(first_idx, 0)
            self.assertGreater(second_idx, 0)
            self.assertLess(first_idx, second_idx)


    def test_top_integrity_summary_counts_cuts(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source").mkdir()
            out = root / "output"
            out.mkdir()
            _write(out, "ex_a", "2025-03-22T08:00:00Z",
                   [mk(0, 0, 10, "Before the cut."),
                    mk(1, 30, 35, "After the cut.")],
                   scene_cuts=[20.0],
                   black_frames=[[15.0, 1.5]],
                   freeze_frames=[[25.0, 2.0]])
            _write(out, "ex_b", "2025-03-22T10:00:00Z",
                   [mk(0, 5, 10, "I'll turn this off for a minute.")],
                   scene_cuts=[12.0, 18.0])
            p = build(root)
            text = p.read_text(encoding="utf-8")
            # Top-line summary present and counts match
            self.assertIn("BWC integrity summary", text)
            self.assertIn("Total scene cuts across all exhibits | **3**", text)
            self.assertIn("Total black-frame intervals | **1**", text)
            self.assertIn("Total freeze-frame intervals | **1**", text)
            self.assertIn("Audible camera-off / stop-recording mentions | **1**", text)
            # Creation-time gap between 08:00 and 10:00 (same day, > 30 min)
            self.assertIn("Creation-time gaps > 30 min same day | **1**", text)
            # Per-cut context section
            self.assertIn("## 2b. Per-cut context", text)
            self.assertIn("Before the cut.", text)
            self.assertIn("After the cut.", text)


if __name__ == "__main__":
    unittest.main()
