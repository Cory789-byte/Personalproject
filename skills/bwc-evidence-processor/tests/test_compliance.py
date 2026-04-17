"""Tests for procedural compliance and bias analysis."""

from __future__ import annotations

import csv
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from procedural_compliance import check, save_findings  # noqa: E402
from bias_analysis import (  # noqa: E402
    detect_interruptions,
    infer_role,
    save_bias_csv,
    save_bias_summary,
    score_segments,
    summarise,
)
from word_review import build as build_word_review  # noqa: E402


def mk(index, start, end, text, words=None):
    return {
        "index": index, "start": start, "end": end,
        "text": text, "words": words or [],
    }


class ComplianceTests(unittest.TestCase):
    def test_missing_caution_flagged(self):
        segs = [
            mk(0, 0, 2, "What were you doing at the park?"),
            mk(1, 2, 4, "I was walking."),
        ]
        f = check(segs)
        cats = {x.category for x in f}
        self.assertIn("missing_caution", cats)
        self.assertIn("missing_right_to_counsel", cats)

    def test_caution_before_questioning_no_late_flag(self):
        segs = [
            mk(0, 0, 3, "You do not have to say anything. Anything you do say may be used in evidence."),
            mk(1, 3, 5, "You have the right to a lawyer."),
            mk(2, 5, 7, "Where were you at nine pm?"),
        ]
        cats = {x.category for x in check(segs)}
        self.assertNotIn("missing_caution", cats)
        self.assertNotIn("late_caution", cats)
        self.assertNotIn("missing_right_to_counsel", cats)

    def test_questioning_after_invocation(self):
        segs = [
            mk(0, 0, 2, "You do not have to say anything."),
            mk(1, 2, 3, "You have the right to a lawyer."),
            mk(2, 3, 5, "I want a lawyer."),
            mk(3, 5, 7, "Where were you last night?"),
        ]
        cats = {x.category for x in check(segs)}
        self.assertIn("questioning_after_invocation", cats)

    def test_arrest_without_grounds(self):
        segs = [
            mk(0, 0, 2, "You are under arrest."),
            mk(1, 2, 4, "Get in the car."),
        ]
        cats = {x.category for x in check(segs)}
        self.assertIn("arrest_without_stated_grounds", cats)

    def test_search_without_warrant_or_consent(self):
        segs = [
            mk(0, 0, 2, "I'm going to search your bag."),
            mk(1, 2, 4, "Stand there."),
        ]
        cats = {x.category for x in check(segs)}
        self.assertIn("search_without_warrant_or_consent", cats)

    def test_inducement_detected(self):
        segs = [mk(0, 0, 3, "If you cooperate it'll be easier for you.")]
        cats = {x.category for x in check(segs)}
        self.assertIn("possible_inducement", cats)

    def test_leading_question_detected(self):
        segs = [mk(0, 0, 3, "You did it, didn't you?")]
        cats = {x.category for x in check(segs)}
        self.assertIn("leading_question", cats)

    def test_save_findings_has_header_and_rows(self):
        segs = [mk(0, 0, 2, "You are under arrest.")]
        with TemporaryDirectory() as tmp:
            dest = Path(tmp) / "compliance.csv"
            save_findings(check(segs), dest)
            text = dest.read_text()
            self.assertIn("MACHINE-GENERATED", text)
            rows = list(csv.DictReader(text.splitlines()[1:]))
            self.assertTrue(rows)
            for r in rows:
                self.assertEqual(r["human_verified"], "")


class BiasTests(unittest.TestCase):
    def test_role_inference(self):
        self.assertEqual(infer_role("You are under arrest, mate."), "OFFICER")
        self.assertEqual(infer_role("I didn't do anything."), "SUBJECT")
        self.assertEqual(infer_role("The weather is nice."), "UNKNOWN")

    def test_scores_and_summary(self):
        segs = [
            mk(0, 0, 3, "You are under arrest. Stop resisting."),
            mk(1, 3, 5, "I didn't do anything, please."),
            mk(2, 5, 8, "Just admit you did it, you might as well admit it."),
        ]
        scored = score_segments(segs)
        roles = {s.speaker_role for s in scored}
        self.assertIn("OFFICER", roles)
        self.assertIn("SUBJECT", roles)
        summary = summarise(scored)
        self.assertGreater(summary["officer_talk_seconds"], 0)
        self.assertGreater(summary["officer_confirmation_bias_density"], 0)
        self.assertGreater(summary["officer_aggressive_density"], 0)

    def test_interruption_detection(self):
        segs = [
            mk(0, 0.0, 3.0, "You are under arrest, mate."),
            mk(1, 2.5, 4.0, "I didn't do anything."),
        ]
        scored = score_segments(segs)
        interruptions = detect_interruptions(scored)
        self.assertTrue(interruptions)
        self.assertGreater(interruptions[0]["overlap_seconds"], 0)

    def test_save_files(self):
        segs = [
            mk(0, 0, 3, "You are under arrest."),
            mk(1, 3, 5, "I want a lawyer."),
        ]
        scored = score_segments(segs)
        with TemporaryDirectory() as tmp:
            csvp = Path(tmp) / "b.csv"
            summaryp = Path(tmp) / "b.json"
            save_bias_csv(scored, csvp)
            save_bias_summary(scored, summaryp)
            self.assertIn("MACHINE-GENERATED", csvp.read_text())
            data = json.loads(summaryp.read_text())
            self.assertIn("summary", data)


class WordReviewTests(unittest.TestCase):
    def test_word_review_rows(self):
        segs = [
            {
                "index": 0, "start": 0, "end": 2,
                "text": "You are under arrest.",
                "words": [
                    {"start": 0.0, "end": 0.3, "text": "You", "probability": 0.99},
                    {"start": 0.3, "end": 0.6, "text": "are", "probability": 0.98},
                    {"start": 0.6, "end": 1.1, "text": "under", "probability": 0.2},
                    {"start": 1.1, "end": 2.0, "text": "arrest", "probability": 0.95},
                ],
            },
        ]
        with TemporaryDirectory() as tmp:
            trans = Path(tmp) / "t.json"
            trans.write_text(json.dumps({"header": "X", "segments": segs}))
            out = Path(tmp) / "w.csv"
            build_word_review(trans, out, low_conf_threshold=0.5)
            rows = list(csv.DictReader(out.read_text().splitlines()[1:]))
            self.assertEqual(len(rows), 4)
            low = [r for r in rows if r["low_confidence"] == "yes"]
            self.assertEqual(len(low), 1)
            self.assertEqual(low[0]["word"], "under")
            self.assertIn("arrest_language", rows[0]["flagged_categories"])


if __name__ == "__main__":
    unittest.main()
