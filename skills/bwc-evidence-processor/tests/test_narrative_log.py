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


def _write(out: Path, stem: str, creation: str, segments: list[dict]) -> None:
    (out / f"{stem}.transcript.json").write_text(
        json.dumps({"header": "X", "segments": segments}), encoding="utf-8"
    )
    (out / f"{stem}.integrity.json").write_text(
        json.dumps({
            "header": "X", "source": "x", "sha256": "a" * 64,
            "format": {"tags": {"creation_time": creation},
                       "duration": "120.0"},
            "streams": [], "scene_cuts": [], "black_frames": [],
            "freeze_frames": [], "anomalies": [], "ocr_samples": [],
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


if __name__ == "__main__":
    unittest.main()
