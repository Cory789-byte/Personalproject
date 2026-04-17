"""Tests for the QPS competency analyzer."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from qps_competency import analyze, save  # noqa: E402


def _transcript(stem: str, segments: list[dict], out_dir: Path) -> None:
    (out_dir / f"{stem}.transcript.json").write_text(
        json.dumps({"header": "X", "segments": segments}),
        encoding="utf-8",
    )


def _integrity(stem: str, out_dir: Path, **kwargs) -> None:
    payload = {
        "header": "X", "source": "x", "sha256": "x" * 64,
        "format": {}, "streams": [],
        "scene_cuts": [], "black_frames": [], "freeze_frames": [],
        "anomalies": [], "ocr_samples": [],
    }
    payload.update(kwargs)
    (out_dir / f"{stem}.integrity.json").write_text(
        json.dumps(payload), encoding="utf-8",
    )


def mk(i, start, end, text):
    return {"index": i, "start": start, "end": end, "text": text, "words": []}


class CompetencyTests(unittest.TestCase):
    def test_uncertainty_flagged(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 2, "I think it's section 365, hang on, let me check."),
            ], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "UNCERTAINTY" for x in f))

    def test_rush_to_judgment(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 3, "We know you did it. No point lying."),
            ], out)
            self.assertTrue(any(x.kind == "RUSH_TO_JUDGMENT"
                                for x in analyze(out)))

    def test_escalation_against_compliant_subject(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 3, "Okay officer, I am cooperating, not resisting."),
                mk(1, 5, 8, "Get on the ground now. Stop resisting."),
            ], out)
            self.assertTrue(any(x.kind == "ESCALATION_FAILURE"
                                for x in analyze(out)))

    def test_ignored_exculpation(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 3, "But I didn't do it, let me explain."),
                mk(1, 3, 5, "You're going to the station."),
                mk(2, 5, 7, "Get in the car."),
            ], out)
            self.assertTrue(any(x.kind == "IGNORED_EXCULPATION"
                                for x in analyze(out)))

    def test_charge_confusion_multiple_sections(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 3, "This is section 365 of the PPRA."),
                mk(1, 3, 5, "Actually I think it's s. 391, hmm."),
            ], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "CHARGE_CONFUSION" for x in f))

    def test_bwc_compliance_gap_turnoff(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [mk(0, 0, 3, "I'll turn this off for a minute.")], out)
            f = analyze(out)
            self.assertTrue(any(x.kind == "BWC_COMPLIANCE_GAP"
                                and x.severity == "critical" for x in f))

    def test_bwc_compliance_gap_many_scene_cuts(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [mk(0, 0, 3, "Walking.")], out)
            _integrity("ex1", out, scene_cuts=[1.0, 2.0, 3.0, 4.0, 5.0])
            f = analyze(out)
            self.assertTrue(any(x.kind == "BWC_COMPLIANCE_GAP" for x in f))

    def test_supervisor_absent_on_arrest(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            segs = [mk(i, i, i + 1, "walking around the scene.") for i in range(70)]
            segs.append(mk(70, 70, 72, "You are under arrest."))
            _transcript("ex1", segs, out)
            self.assertTrue(any(x.kind == "SUPERVISOR_ABSENT"
                                for x in analyze(out)))

    def test_dv_context_no_referral(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 3, "This is a domestic incident involving the partner."),
                mk(1, 3, 5, "You need to leave the property."),
            ], out)
            self.assertTrue(any(x.kind == "DV_HANDLING_FAILURE"
                                for x in analyze(out)))

    def test_mental_health_distress_no_response(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [
                mk(0, 0, 3, "I can't breathe, I'm having a panic attack."),
                mk(1, 4, 7, "Get in the car."),
            ], out)
            self.assertTrue(any(x.kind == "MENTAL_HEALTH_UNCONSIDERED"
                                for x in analyze(out)))

    def test_save_writes_outputs(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            _transcript("ex1", [mk(0, 0, 3, "I think, maybe, hang on.")], out)
            findings = analyze(out)
            csv_path, md_path = save(findings, out)
            self.assertTrue(csv_path.is_file())
            self.assertTrue(md_path.is_file())
            self.assertIn("MACHINE-GENERATED", csv_path.read_text(encoding="utf-8"))
            self.assertIn("QPS Competency", md_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
