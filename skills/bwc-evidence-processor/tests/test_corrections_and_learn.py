"""Tests for corrections system + learn.py CSV feedback extractor."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from corrections import MatterCorrections  # noqa: E402
from learn import run as run_learn  # noqa: E402
from evidence_engagement import analyze  # noqa: E402


class CorrectionsTests(unittest.TestCase):
    def test_load_empty_when_no_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            mc = MatterCorrections.load(root)
            self.assertEqual(mc.vocabulary["names"], [])
            self.assertEqual(mc.corrections["suppressions"], [])

    def test_save_and_reload_roundtrip(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "config").mkdir()
            mc = MatterCorrections.load(root)
            mc.add_name("Cory Shepherd")
            mc.add_word_correction("Sheppard", "Shepherd")
            mc.add_role_override("ex1", 3, "OFFICER")
            mc.add_suppression(exhibit="ex1", category="missing_caution")
            mc.save()
            mc2 = MatterCorrections.load(root)
            self.assertIn("Cory Shepherd", mc2.vocabulary["names"])
            self.assertEqual(mc2.vocabulary["word_corrections"]["Sheppard"], "Shepherd")
            self.assertTrue(mc2.is_suppressed("ex1", "whatever", "missing_caution"))
            self.assertEqual(mc2.role_for("ex1", 3), "OFFICER")

    def test_word_corrections_applied_whole_word(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            mc = MatterCorrections.load(root)
            mc.add_word_correction("Sheppard", "Shepherd")
            out = mc.apply_word_corrections("Mr Sheppard said Mr Sheppardson is there.")
            # Whole-word swap only (so Sheppardson is untouched)
            self.assertEqual(out, "Mr Shepherd said Mr Sheppardson is there.")

    def test_whisper_prompt_length_capped(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            mc = MatterCorrections.load(root)
            mc.vocabulary["names"] = ["Name" + str(i) for i in range(200)]
            p = mc.whisper_prompt()
            self.assertLessEqual(len(p), 244)


class LearnTests(unittest.TestCase):
    def test_learn_extracts_false_positive_and_word_correction(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "config").mkdir()
            out = root / "output"
            out.mkdir()
            # A compliance CSV with a false_positive row
            (out / "ex1.compliance.csv").write_text(
                "# X\n"
                "row,category,severity,start,end,timestamp_hms,utterance,detail,human_verified\n"
                "1,missing_caution,high,10.0,12.0,00:00:10.000,noise,reason,false_positive\n"
                "2,possible_inducement,critical,20.0,22.0,00:00:20.000,real,genuine,true\n",
                encoding="utf-8",
            )
            # An ISSUES_LOG.csv with a correct: feedback and role override
            (out / "ISSUES_LOG.csv").write_text(
                "# X\n"
                "row,exhibit,kind,category,severity,start_seconds,end_seconds,"
                "timestamp_hms,absolute_datetime,detail,evidence,counter_evidence,"
                "video_path,vlc_command,ffplay_command,explorer_uri,notes,human_verified\n"
                "1,ex1,qps_competency,UNCERTAINTY,medium,5.0,7.0,00:00:05.000,,det,utt,,/x/ex1.mp4,v,f,u,"
                "correct:\"Sheppard\" -> \"Shepherd\",true\n",
                encoding="utf-8",
            )
            # A bias CSV with a role override
            (out / "ex1.bias.csv").write_text(
                "# X\n"
                "index,start,end,speaker_role,is_question,word_count,"
                "aggressive,dehumanising,presumptive,confirmation_bias,one_sided,"
                "utterance,human_verified\n"
                "4,0.0,2.0,UNKNOWN,False,3,,,,,,something,role:OFFICER\n",
                encoding="utf-8",
            )
            counts = run_learn(root)
            self.assertGreaterEqual(counts.get("suppressions", 0), 1)
            self.assertGreaterEqual(counts.get("word_corrections", 0), 1)
            self.assertGreaterEqual(counts.get("role_overrides", 0), 1)
            # Verify files were written
            vocab = json.loads((root / "config" / "vocabulary.json").read_text(encoding="utf-8"))
            corr = json.loads((root / "config" / "corrections.json").read_text(encoding="utf-8"))
            self.assertEqual(vocab["word_corrections"].get("Sheppard"), "Shepherd")
            self.assertTrue(any(
                s.get("exhibit") == "ex1" and s.get("category") == "missing_caution"
                for s in corr["suppressions"]
            ))
            self.assertEqual(corr["role_overrides"]["ex1"]["4"], "OFFICER")


class EvidenceLeftAtSceneTests(unittest.TestCase):
    def test_flags_when_offer_followed_by_departure_no_seizure(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "ex.transcript.json").write_text(
                json.dumps({
                    "header": "X",
                    "segments": [
                        {"index": 0, "start": 0, "end": 3,
                         "text": "Here's the lease documents.", "words": []},
                        {"index": 1, "start": 4, "end": 7,
                         "text": "Alright.", "words": []},
                        {"index": 2, "start": 8, "end": 12,
                         "text": "We're leaving, take care.", "words": []},
                    ],
                }),
                encoding="utf-8",
            )
            f = analyze(out)
            self.assertTrue(any(x.kind == "EVIDENCE_LEFT_AT_SCENE"
                                and x.severity == "critical" for x in f))

    def test_not_flagged_when_officer_seizes(self):
        with TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "ex.transcript.json").write_text(
                json.dumps({
                    "header": "X",
                    "segments": [
                        {"index": 0, "start": 0, "end": 3,
                         "text": "Here's the lease documents.", "words": []},
                        {"index": 1, "start": 4, "end": 7,
                         "text": "I'll take these as evidence. Property receipt will follow.",
                         "words": []},
                    ],
                }),
                encoding="utf-8",
            )
            f = analyze(out)
            self.assertFalse(any(x.kind == "EVIDENCE_LEFT_AT_SCENE" for x in f))


if __name__ == "__main__":
    unittest.main()
