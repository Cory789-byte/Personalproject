"""Per-matter corrections + vocabulary system.

Every analyzer reads from two small JSON files stored in the matter's
config directory:

  <matter_root>/config/vocabulary.json   - names, places, legal terms,
                                           misheard word fixes. Used as
                                           the Whisper initial_prompt AND
                                           for post-transcription swap.
  <matter_root>/config/corrections.json  - accumulated user feedback:
                                           role overrides, false-positive
                                           suppressions, per-segment
                                           speaker labels.

Both files are optional. When missing, the skill behaves as before.
When present, the skill progressively improves: each time you mark a
CSV row as false-positive or correct a misheard word, the next batch
run will apply that knowledge automatically.

The companion tool scripts/learn.py reads the human_verified columns
across every CSV and updates these files.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


VOCAB_FILENAME = "vocabulary.json"
CORRECTIONS_FILENAME = "corrections.json"

DEFAULT_VOCABULARY: dict = {
    "names": [],
    "places": [],
    "legal_terms": [
        "PPRA", "OPM", "QPS", "Form 24", "Form 29", "QPP",
        "PID", "ESU", "CO-", "WC/",
    ],
    "word_corrections": {},
}


DEFAULT_CORRECTIONS: dict = {
    "role_overrides": {},
    "suppressions": [],
    "speaker_labels": {},
}


@dataclass
class MatterCorrections:
    matter_root: Path
    vocabulary: dict = field(default_factory=lambda: dict(DEFAULT_VOCABULARY))
    corrections: dict = field(default_factory=lambda: dict(DEFAULT_CORRECTIONS))

    @classmethod
    def load(cls, matter_root: Path) -> "MatterCorrections":
        matter_root = Path(matter_root).resolve()
        cfg = matter_root / "config"
        vocab: dict = dict(DEFAULT_VOCABULARY)
        corr: dict = dict(DEFAULT_CORRECTIONS)
        vp = cfg / VOCAB_FILENAME
        if vp.is_file():
            try:
                data = json.loads(vp.read_text(encoding="utf-8", errors="replace"))
                for k in DEFAULT_VOCABULARY:
                    vocab[k] = data.get(k, DEFAULT_VOCABULARY[k])
            except Exception:
                pass
        cp = cfg / CORRECTIONS_FILENAME
        if cp.is_file():
            try:
                data = json.loads(cp.read_text(encoding="utf-8", errors="replace"))
                for k in DEFAULT_CORRECTIONS:
                    corr[k] = data.get(k, DEFAULT_CORRECTIONS[k])
            except Exception:
                pass
        return cls(matter_root=matter_root, vocabulary=vocab, corrections=corr)

    def save(self) -> None:
        cfg = self.matter_root / "config"
        cfg.mkdir(parents=True, exist_ok=True)
        (cfg / VOCAB_FILENAME).write_text(
            json.dumps(self.vocabulary, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        (cfg / CORRECTIONS_FILENAME).write_text(
            json.dumps(self.corrections, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    # ---- Vocabulary use ---------------------------------------------------

    def whisper_prompt(self) -> str:
        """Return a Whisper initial_prompt biasing the model toward
        matter-specific terms and names."""
        parts: list[str] = []
        for key in ("names", "places", "legal_terms"):
            vals = [v for v in self.vocabulary.get(key, []) if v]
            if vals:
                parts.append(", ".join(vals))
        return " ".join(parts).strip()[:244]  # Whisper prompt cap ~ 224 tokens

    def apply_word_corrections(self, text: str) -> str:
        out = text
        for wrong, right in (self.vocabulary.get("word_corrections") or {}).items():
            if not wrong or not right:
                continue
            # Whole-word, case-insensitive swap
            out = re.sub(
                rf"\b{re.escape(wrong)}\b",
                right,
                out,
                flags=re.IGNORECASE,
            )
        return out

    # ---- Corrections use --------------------------------------------------

    def role_for(self, exhibit: str, segment_index: int) -> str | None:
        """Return a forced role for a segment (or None)."""
        overrides = (self.corrections.get("role_overrides") or {}).get(exhibit) or {}
        return overrides.get(str(segment_index))

    def speaker_for(self, exhibit: str, segment_index: int) -> str | None:
        speakers = (self.corrections.get("speaker_labels") or {}).get(exhibit) or {}
        return speakers.get(str(segment_index))

    def is_suppressed(
        self,
        exhibit: str,
        kind: str,
        category: str = "",
        timestamp: str = "",
    ) -> bool:
        for rule in self.corrections.get("suppressions") or []:
            if rule.get("exhibit") and rule["exhibit"] != exhibit:
                continue
            if rule.get("kind") and rule["kind"] != kind:
                continue
            if rule.get("category") and rule["category"] != category:
                continue
            if rule.get("timestamp") and rule["timestamp"] != timestamp:
                continue
            return True
        return False

    # ---- Mutation helpers for learn.py -----------------------------------

    def add_word_correction(self, wrong: str, right: str) -> None:
        wc = self.vocabulary.setdefault("word_corrections", {})
        wc[wrong] = right

    def add_name(self, name: str) -> None:
        names = self.vocabulary.setdefault("names", [])
        if name not in names:
            names.append(name)

    def add_role_override(self, exhibit: str, segment_index: int, role: str) -> None:
        overrides = self.corrections.setdefault("role_overrides", {}).setdefault(
            exhibit, {}
        )
        overrides[str(segment_index)] = role

    def add_speaker_label(self, exhibit: str, segment_index: int, speaker: str) -> None:
        labels = self.corrections.setdefault("speaker_labels", {}).setdefault(
            exhibit, {}
        )
        labels[str(segment_index)] = speaker

    def add_suppression(self, **rule) -> None:
        rules = self.corrections.setdefault("suppressions", [])
        if rule not in rules:
            rules.append(rule)
