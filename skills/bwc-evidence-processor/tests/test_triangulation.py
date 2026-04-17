"""Tests for triangulation analyzer."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from triangulation import analyze, save  # noqa: E402


def _doc(stem: str, text: str, out: Path) -> None:
    docs = out / "documents"
    docs.mkdir(parents=True, exist_ok=True)
    (docs / f"{stem}.doc.json").write_text(
        json.dumps({"header": "X", "stem": stem, "path": f"x/{stem}.pdf",
                    "kind": "pdf", "sha256": "x" * 64, "size": 1,
                    "text": text, "pages": 1, "sheets": [], "warnings": []}),
        encoding="utf-8",
    )


def _transcript(stem: str, segments: list[dict], out: Path) -> None:
    (out / f"{stem}.transcript.json").write_text(
        json.dumps({"header": "X", "segments": segments}),
        encoding="utf-8",
    )


def _integrity(stem: str, out: Path, creation: str = "",
               cuts: list[float] | None = None,
               turnoff_segments: list[dict] | None = None) -> None:
    (out / f"{stem}.integrity.json").write_text(
        json.dumps({
            "header": "X", "source": "x", "sha256": "x" * 64,
            "format": {"tags": {"creation_time": creation},
                       "duration": "120.0"},
            "streams": [],
            "scene_cuts": cuts or [],
            "black_frames": [], "freeze_frames": [],
            "anomalies": [], "ocr_samples": [],
        }),
        encoding="utf-8",
    )


def mk(i, s, e, text):
    return {"index": i, "start": s, "end": e, "text": text, "words": []}


class TriangulationTests(unittest.TestCase):
    def test_extracts_arrival_arrest_across_sources(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "output"
            out.mkdir()
            _doc("EASTHOPE_statement", "At about 0806 I arrived at the front door. "
                 "I then cautioned the accused and placed him under arrest.", out)
            _transcript("Exhibit_#3_EASTHOPE_BWCF_arrest", [
                mk(0, 0, 3, "We arrived at the property."),
                mk(1, 60, 63, "You are under arrest."),
                mk(2, 62, 66, "You do not have to say anything."),
            ], out)
            _integrity("Exhibit_#3_EASTHOPE_BWCF_arrest", out,
                       creation="2025-03-22T08:13:00Z")
            rep = analyze(root)
            events = {m.event for m in rep["mentions"]}
            self.assertIn("arrival", events)
            self.assertIn("arrest", events)
            self.assertIn("caution", events)

    def test_tampering_tally_scores_increase_with_cuts_and_turnoff(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "output"
            out.mkdir()
            _transcript("A_BWC", [
                mk(0, 0, 3, "I'll turn this off for a minute."),
            ], out)
            _integrity("A_BWC", out, cuts=[1, 2, 3, 4, 5])
            _integrity("B_BWC", out, cuts=[])
            _transcript("B_BWC", [mk(0, 0, 2, "All good here.")], out)
            rep = analyze(root)
            by_name = {t.exhibit: t for t in rep["tally"]}
            self.assertGreater(by_name["A_BWC"].score, by_name["B_BWC"].score)
            self.assertEqual(by_name["A_BWC"].scene_cuts, 5)
            self.assertEqual(by_name["A_BWC"].turn_off_mentions, 1)

    def test_save_writes_three_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            out = root / "output"
            out.mkdir()
            _doc("stmt", "I arrested him at 0806.", out)
            _transcript("ex", [mk(0, 0, 2, "You are under arrest.")], out)
            _integrity("ex", out, cuts=[1.0])
            rep = analyze(root)
            csvp, mdp, tmp_md = save(rep, out)
            self.assertTrue(csvp.is_file())
            self.assertTrue(mdp.is_file())
            self.assertTrue(tmp_md.is_file())
            self.assertIn("Triangulation", mdp.read_text(encoding="utf-8"))
            self.assertIn("Tampering Tally", tmp_md.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
