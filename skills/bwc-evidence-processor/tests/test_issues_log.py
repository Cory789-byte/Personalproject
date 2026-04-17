"""Tests for issues_log and frame_extract timestamp parsing."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from issues_log import build  # noqa: E402
from frame_extract import parse_timestamp  # noqa: E402


def _write_integrity(out: Path, stem: str, creation: str, **kwargs) -> None:
    payload = {
        "header": "X", "source": f"C:/fake/{stem}.mp4",
        "sha256": "x" * 64,
        "format": {"tags": {"creation_time": creation},
                   "duration": "120.0"},
        "streams": [],
        "scene_cuts": [], "black_frames": [], "freeze_frames": [],
        "anomalies": [], "ocr_samples": [],
    }
    payload.update(kwargs)
    (out / f"{stem}.integrity.json").write_text(json.dumps(payload), encoding="utf-8")


class FrameTimestampTests(unittest.TestCase):
    def test_parse_seconds(self):
        self.assertAlmostEqual(parse_timestamp("83.5"), 83.5)
        self.assertAlmostEqual(parse_timestamp(120), 120.0)

    def test_parse_hms(self):
        self.assertAlmostEqual(parse_timestamp("01:23"), 83.0)
        self.assertAlmostEqual(parse_timestamp("01:23.500"), 83.5)
        self.assertAlmostEqual(parse_timestamp("00:02:05"), 125.0)
        self.assertAlmostEqual(parse_timestamp("00:02:05.25"), 125.25)


class IssuesLogTests(unittest.TestCase):
    def test_collects_compliance_and_writes_seek_commands(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "source"; src.mkdir()
            out = root / "output"; out.mkdir()

            media = src / "ex.mp4"
            media.write_bytes(b"\x00")

            _write_integrity(out, "ex", "2025-03-22T08:00:00Z",
                             scene_cuts=[12.0, 45.0],
                             black_frames=[[30.0, 2.0]])
            (out / "ex.compliance.csv").write_text(
                "# X\n"
                "row,category,severity,start,end,timestamp_hms,utterance,detail,human_verified\n"
                "1,arrest_without_stated_grounds,high,10.0,12.5,00:00:10.000,You are under arrest,arrest without grounds,\n",
                encoding="utf-8",
            )
            csv_p, md_p = build(root)
            csv_text = csv_p.read_text(encoding="utf-8")
            md_text = md_p.read_text(encoding="utf-8")
            self.assertIn("MACHINE-GENERATED", csv_text)
            self.assertIn("arrest_without_stated_grounds", csv_text)
            # Seek commands rendered in both CSV and MD
            self.assertIn("vlc --start-time=10.000", csv_text)
            self.assertIn("ffplay -ss 10.000", csv_text)
            self.assertIn("Seek (VLC)", md_text)
            # Frame extract helper rendered for issue with video
            self.assertIn("frame_extract.py", md_text)
            # Scene cuts and black frames picked up as integrity anomalies
            self.assertIn("scene_cut", csv_text)
            self.assertIn("black_frames", csv_text)


if __name__ == "__main__":
    unittest.main()
