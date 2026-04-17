"""Tests for the validation module."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validation import save, validate_matter  # noqa: E402


def _write_all_artefacts(out: Path, stem: str, sha: str, segments_ok: bool = True) -> None:
    (out / f"{stem}.transcript.json").write_text(
        json.dumps({
            "header": "MACHINE-GENERATED - UNVERIFIED",
            "segments": [
                {"index": 0, "start": 0, "end": 1, "text": "hello", "words": []}
            ] if segments_ok else [],
        }), encoding="utf-8",
    )
    (out / f"{stem}.integrity.json").write_text(
        json.dumps({
            "header": "MACHINE-GENERATED - UNVERIFIED",
            "source": "fake",
            "sha256": sha,
            "format": {}, "streams": [],
            "scene_cuts": [], "black_frames": [], "freeze_frames": [],
            "anomalies": [], "ocr_samples": [],
        }), encoding="utf-8",
    )
    (out / f"{stem}.srt").write_text("1\n00:00:00,000 --> 00:00:01,000\nhello\n", encoding="utf-8")
    (out / f"{stem}.vtt").write_text("WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nhello\n", encoding="utf-8")
    (out / f"{stem}.evidence_matrix.csv").write_text(
        "# MACHINE-GENERATED - UNVERIFIED\nrow,timestamp_hms,utterance\n1,00:00:00.000,hello\n",
        encoding="utf-8",
    )
    (out / f"{stem}.viewing_log.md").write_text("# Viewing Log\n\nhello\n", encoding="utf-8")
    (out / f"{stem}.contradictions.csv").write_text(
        "# MACHINE-GENERATED - UNVERIFIED\nrow,start,end,similarity\n",
        encoding="utf-8",
    )
    (out / f"{stem}.compliance.csv").write_text(
        "# MACHINE-GENERATED - UNVERIFIED\nrow,category,severity\n",
        encoding="utf-8",
    )
    (out / f"{stem}.bias.csv").write_text(
        "# MACHINE-GENERATED - UNVERIFIED\nindex,speaker_role\n0,OFFICER\n",
        encoding="utf-8",
    )
    (out / f"{stem}.bias_summary.json").write_text(
        json.dumps({
            "header": "MACHINE-GENERATED - UNVERIFIED",
            "summary": {}, "interruptions": [],
        }), encoding="utf-8",
    )
    (out / f"{stem}.word_review.csv").write_text(
        "# MACHINE-GENERATED - UNVERIFIED\nrow,word,confidence\n1,hello,0.99\n",
        encoding="utf-8",
    )
    (out / f"{stem}.master_report.md").write_text(
        "# Master Report\n\nMACHINE-GENERATED - UNVERIFIED\n",
        encoding="utf-8",
    )


def _write_matter_wide(out: Path) -> None:
    for name in ["MATTER_INDEX.md", "CASE_THEORY.md",
                 "DEEP_CONTRADICTIONS.md", "COMPETENCY_FINDINGS.md"]:
        (out / name).write_text("placeholder", encoding="utf-8")
    for name in ["DEEP_CONTRADICTIONS.csv", "COMPETENCY_FINDINGS.csv"]:
        (out / name).write_text("row,kind\n", encoding="utf-8")


class ValidationTests(unittest.TestCase):
    def test_pass_when_all_artefacts_present(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "source"
            src.mkdir()
            media = src / "exhibit1.mp4"
            media.write_bytes(b"\x00\x01\x02")
            sha = hashlib.sha256(media.read_bytes()).hexdigest()
            out = root / "output"
            out.mkdir()
            (root / "sworn").mkdir()
            (root / "sworn" / "corpus.txt").write_text("some sworn text", encoding="utf-8")
            _write_all_artefacts(out, "exhibit1", sha)
            _write_matter_wide(out)
            r = validate_matter(root)
            self.assertEqual(r["overall"], "PASS")
            self.assertEqual(r["status_counts"]["PASS"], 1)

    def test_fail_on_sha_mismatch(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "source"
            src.mkdir()
            media = src / "ex.mp4"
            media.write_bytes(b"\x00\x01\x02")
            out = root / "output"
            out.mkdir()
            _write_all_artefacts(out, "ex", "a" * 64)  # wrong sha
            _write_matter_wide(out)
            (root / "sworn").mkdir()
            (root / "sworn" / "corpus.txt").write_text("x", encoding="utf-8")
            r = validate_matter(root)
            self.assertEqual(r["overall"], "FAIL")
            self.assertIn("chain_of_custody", " ".join(
                c.target for e in r["exhibits"] for c in e.checks
            ))

    def test_warn_on_missing_segments(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "source"; src.mkdir()
            media = src / "quiet.mp4"; media.write_bytes(b"\x00")
            sha = hashlib.sha256(media.read_bytes()).hexdigest()
            out = root / "output"; out.mkdir()
            _write_all_artefacts(out, "quiet", sha, segments_ok=False)
            _write_matter_wide(out)
            (root / "sworn").mkdir()
            (root / "sworn" / "corpus.txt").write_text("x", encoding="utf-8")
            r = validate_matter(root)
            self.assertIn(r["overall"], {"WARN", "FAIL"})

    def test_uncovered_media_warns(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "source"; src.mkdir()
            (src / "processed.mp4").write_bytes(b"\x00")
            (src / "unprocessed.mp4").write_bytes(b"\x00")
            out = root / "output"; out.mkdir()
            sha = hashlib.sha256(b"\x00").hexdigest()
            _write_all_artefacts(out, "processed", sha)
            _write_matter_wide(out)
            (root / "sworn").mkdir()
            (root / "sworn" / "corpus.txt").write_text("x", encoding="utf-8")
            r = validate_matter(root)
            self.assertEqual(len(r["uncovered"]), 1)
            self.assertEqual(r["uncovered"][0].name, "unprocessed.mp4")

    def test_save_writes_md_and_csv(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source").mkdir()
            (root / "output").mkdir()
            (root / "sworn").mkdir()
            (root / "sworn" / "corpus.txt").write_text("x", encoding="utf-8")
            _write_matter_wide(root / "output")
            r = validate_matter(root)
            csv_p, md_p = save(r, root / "output")
            self.assertTrue(csv_p.is_file())
            self.assertTrue(md_p.is_file())
            self.assertIn("MACHINE-GENERATED", md_p.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
