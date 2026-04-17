"""Offline unit tests. No ffmpeg or Whisper required."""

from __future__ import annotations

import csv
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evidence_map import (  # noqa: E402
    KeywordBank,
    build_contradictions,
    build_evidence_matrix,
    build_viewing_log,
)
from generate_srt import write_srt, write_vtt  # noqa: E402


FIXTURE = {
    "header": "MACHINE-GENERATED - UNVERIFIED",
    "segments": [
        {
            "index": 0,
            "start": 0.0,
            "end": 2.5,
            "text": "You are under arrest for the purpose of questioning.",
            "words": [],
        },
        {
            "index": 1,
            "start": 2.6,
            "end": 5.0,
            "text": "I admit I was there on the night in question.",
            "words": [],
        },
        {
            "index": 2,
            "start": 5.1,
            "end": 7.0,
            "text": "Reference PID 24-ESU-1130 on file.",
            "words": [],
        },
    ],
}


class EvidenceMapTests(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.transcript = self.dir / "t.json"
        self.transcript.write_text(json.dumps(FIXTURE))
        self.bank = KeywordBank(
            categories={
                "arrest_statement": ["you are under arrest"],
                "admission": ["I admit"],
            },
            matter_refs=["PID 24-ESU-1130"],
            annexure_map={"arrest_statement": "Annexure C"},
            fuzzy_threshold=85,
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_matrix_matches_expected_rows(self):
        dest = self.dir / "matrix.csv"
        build_evidence_matrix(self.transcript, self.bank, dest)
        content = dest.read_text().splitlines()
        self.assertTrue(content[0].startswith("# MACHINE-GENERATED"))
        reader = csv.DictReader(content[1:])
        rows = list(reader)
        categories = sorted({r["category"] for r in rows})
        self.assertIn("arrest_statement", categories)
        self.assertIn("admission", categories)
        self.assertIn("matter_identifier", categories)
        for r in rows:
            self.assertEqual(r["human_verified"], "")

    def test_contradictions_empty_when_no_corpus(self):
        dest = self.dir / "c.csv"
        build_contradictions(self.transcript, None, dest)
        text = dest.read_text()
        self.assertIn("MACHINE-GENERATED", text)
        self.assertIn("row,start,end", text)

    def test_contradictions_detects_partial_divergence(self):
        sworn = self.dir / "sworn.txt"
        sworn.write_text(
            "The officer said you are arrested for questioning about the matter."
        )
        dest = self.dir / "c.csv"
        build_contradictions(self.transcript, sworn, dest, threshold=60)
        rows = list(csv.DictReader(dest.read_text().splitlines()[1:]))
        self.assertTrue(any(r["contradiction_type"] for r in rows))

    def test_viewing_log_has_header_and_rows(self):
        dest = self.dir / "log.md"
        build_viewing_log(self.transcript, dest, "sample.mp4")
        text = dest.read_text()
        self.assertIn("MACHINE-GENERATED", text)
        self.assertIn("sample.mp4", text)
        self.assertIn("under arrest", text)
        self.assertIn("PID 24-ESU-1130", text)
        data_rows = [l for l in text.splitlines() if l.startswith("| ") and "---" not in l]
        # header row + 3 segment rows
        self.assertEqual(len(data_rows), 4)

    def test_srt_and_vtt_render(self):
        srt_path = self.dir / "out.srt"
        vtt_path = self.dir / "out.vtt"
        write_srt(self.transcript, srt_path)
        write_vtt(self.transcript, vtt_path)
        self.assertIn("MACHINE-GENERATED", srt_path.read_text())
        self.assertIn("WEBVTT", vtt_path.read_text())
        self.assertIn("under arrest", srt_path.read_text())


if __name__ == "__main__":
    unittest.main()
