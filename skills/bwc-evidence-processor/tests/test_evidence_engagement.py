"""Tests for evidence engagement analyzer."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evidence_engagement import analyze, save  # noqa: E402
from visual_sweep import run as run_sweep  # noqa: E402


def _transcript(stem: str, segments: list[dict], out: Path) -> None:
    (out / f"{stem}.transcript.json").write_text(
        json.dumps({"header": "X", "segments": segments}),
        encoding="utf-8",
    )


def mk(i, s, e, text):
    return {"index": i, "start": s, "end": e, "text": text, "words": []}


class EvidenceEngagementTests(unittest.TestCase):
    def test_offered_and_ignored(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex", [
                mk(0, 0, 3, "Here's my lease, you can see I live here."),
                mk(1, 4, 7, "Get in the car."),
                mk(2, 8, 12, "You're going to the station."),
            ], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "OFFERED_AND_IGNORED" for x in f))

    def test_offered_and_acknowledged_only(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex", [
                mk(0, 0, 3, "Here's my lease."),
                mk(1, 4, 6, "Okay thanks."),
                mk(2, 8, 11, "Let's get moving."),
            ], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "OFFERED_ACKNOWLEDGED_ONLY" for x in f))

    def test_offered_and_discussed_is_informational(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex", [
                mk(0, 0, 3, "Here's my lease, take a look."),
                mk(1, 4, 8, "Let me see. When was this signed?"),
            ], out)
            f = analyze(out)
            kinds = [x.kind for x in f]
            self.assertIn("OFFERED_AND_DISCUSSED", kinds)

    def test_physical_reference_unexamined(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex", [
                mk(0, 0, 3, "Look at the mail at the front door."),
                mk(1, 5, 8, "Let's keep moving."),
            ], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "PHYSICAL_REFERENCE_UNEXAMINED" for x in f))

    def test_residency_evidence_ignored(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex", [
                mk(0, 0, 3, "My mail is on the bench, I live here."),
                mk(1, 4, 7, "You're under arrest."),
            ], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "RESIDENCY_EVIDENCE_IGNORED"
                                and x.severity == "critical" for x in f))

    def test_save_writes_files(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex", [mk(0, 0, 3, "Here's my lease.")], out)
            findings = analyze(out)
            csvp, mdp = save(findings, out)
            self.assertTrue(csvp.is_file())
            self.assertTrue(mdp.is_file())
            self.assertIn("MACHINE-GENERATED", csvp.read_text(encoding="utf-8"))


class VisualSweepTests(unittest.TestCase):
    def test_dry_run_catalogues_without_extracting(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source").mkdir()
            out = root / "output"; out.mkdir()
            _transcript("ex1", [
                mk(0, 0, 3, "The mail at the front door."),
                mk(1, 10, 12, "They're upstairs now in the kitchen."),
            ], out)
            idx = run_sweep(root, dry_run=True)
            self.assertTrue(idx.is_file())
            text = idx.read_text(encoding="utf-8")
            self.assertIn("visual evidence sweep", text.lower())
            self.assertIn("front door", text)
            self.assertIn("upstairs", text)


if __name__ == "__main__":
    unittest.main()
