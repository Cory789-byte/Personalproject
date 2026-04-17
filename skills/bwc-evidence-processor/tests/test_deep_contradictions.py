"""Tests for the deep contradictions analyzer."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from deep_contradictions import analyze, save  # noqa: E402


def _doc(stem: str, text: str, out_dir: Path) -> None:
    docs = out_dir / "documents"
    docs.mkdir(parents=True, exist_ok=True)
    (docs / f"{stem}.doc.json").write_text(
        json.dumps({
            "header": "MACHINE-GENERATED - UNVERIFIED",
            "stem": stem, "path": f"<fake>/{stem}.pdf",
            "kind": "pdf", "sha256": "x" * 64, "size": 1,
            "text": text, "pages": 1, "sheets": [], "warnings": [],
        }, ensure_ascii=False),
        encoding="utf-8",
    )


def _transcript(stem: str, segments: list[dict], out_dir: Path) -> None:
    (out_dir / f"{stem}.transcript.json").write_text(
        json.dumps({
            "header": "MACHINE-GENERATED - UNVERIFIED",
            "segments": segments,
        }),
        encoding="utf-8",
    )


def _integrity(stem: str, creation: str, out_dir: Path) -> None:
    (out_dir / f"{stem}.integrity.json").write_text(
        json.dumps({
            "header": "MACHINE-GENERATED - UNVERIFIED",
            "source": "<fake>",
            "sha256": "x" * 64,
            "format": {"tags": {"creation_time": creation}},
            "streams": [],
            "scene_cuts": [], "black_frames": [],
            "freeze_frames": [], "anomalies": [],
            "ocr_samples": [],
        }),
        encoding="utf-8",
    )


class DeepTests(unittest.TestCase):
    def test_identity_variant_flags_name_spelling(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _doc("statement_a", "Mr Shepherd was present. DOB: 01/02/1990.", out)
            _doc("statement_b", "Mr Sheppard attended the scene. DOB: 01/02/1990.", out)
            findings = analyze(out)
            kinds = [f.kind for f in findings]
            self.assertIn("IDENTITY_VARIANT", kinds)
            self.assertTrue(any("Shepherd" in f.evidence and "Sheppard" in f.evidence
                                for f in findings if f.kind == "IDENTITY_VARIANT"))

    def test_dob_variant_flags(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _doc("a", "DOB: 01/02/1990", out)
            _doc("b", "Date of birth 02/01/1990", out)
            findings = analyze(out)
            self.assertTrue(any(f.kind == "IDENTITY_VARIANT" and "dob" in f.detail
                                for f in findings))

    def test_procedural_claim_without_transcript(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _doc("officer_statement", "I cautioned the accused at the scene.", out)
            _transcript("bwc_exhibit", [
                {"index": 0, "start": 0, "end": 2, "text": "Get in the car.",
                 "words": []},
            ], out)
            findings = analyze(out)
            self.assertTrue(any(f.kind == "PROCEDURAL_CLAIM_UNSUPPORTED"
                                for f in findings))

    def test_procedural_claim_with_supporting_caution(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _doc("statement", "I cautioned the accused.", out)
            _transcript("bwc", [
                {"index": 0, "start": 0, "end": 2,
                 "text": "You do not have to say anything. Anything you do say may be used in evidence.",
                 "words": []},
            ], out)
            findings = analyze(out)
            # Should NOT flag procedural for a supported caution
            self.assertFalse(any(f.kind == "PROCEDURAL_CLAIM_UNSUPPORTED"
                                 and f.source == "statement"
                                 for f in findings))

    def test_save_writes_csv_and_md(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _doc("a", "Mr Shepherd.", out)
            _doc("b", "Mr Sheppard.", out)
            findings = analyze(out)
            csv_path, md_path = save(findings, out)
            self.assertTrue(csv_path.is_file())
            self.assertTrue(md_path.is_file())
            self.assertIn("MACHINE-GENERATED", csv_path.read_text(encoding="utf-8"))
            self.assertIn("IDENTITY_VARIANT", md_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
