"""Screenshot-specific Claude analysis with strict QLD interpretation.

Reads a manifest from `local_ingest.py` (or `gdrive_ingest.py`), filters to
images, and runs each screenshot through Claude Opus 4.7 with the
strict-interpretation framework. Output schema is screenshot-shaped:
category, tags, participants, temporal data, verbatim transcript, engaged
statutes with interpretive step, authentication and privilege concerns.

Run:
    python scripts/screenshot_analysis.py \
        --manifest C:/Evidence/CO-25-2722/screenshots/incoming/manifest.json \
        --framework prompts/screenshot_strict_interpretation.md \
        --output   C:/Evidence/CO-25-2722/output/screenshot_analysis
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"
MODEL = "claude-opus-4-7"
MAX_TOKENS = 8000
MAX_IMAGE_BYTES = 4_500_000
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

PRIMARY_CATEGORIES = [
    "comm.whatsapp", "comm.sms", "comm.email", "comm.dm", "comm.call_log",
    "social.public", "social.story",
    "doc.court", "doc.legal", "doc.financial", "doc.medical", "doc.gov",
    "scene.injury", "scene.property", "scene.location",
    "web.news", "web.profile",
    "app.location", "app.payment",
    "meta.system",
    "unclear",
]

SECONDARY_TAGS = [
    "threat", "coercion", "economic_abuse", "monitoring", "harassment",
    "gaslighting", "derogation", "admission", "denial", "contradiction",
    "corroboration", "identification", "timestamp_visible",
    "metadata_visible", "redaction_required", "chain_of_custody_concern",
    "authenticity_concern", "third_party_present", "pattern_one_of_n",
    "single_utterance_sufficient", "quoted_or_forwarded", "voice_note",
]

INTERPRETIVE_STEPS = [
    "literal",
    "golden",
    "mischief",
    "purposive_AIA_s14A",
    "strict_construction_penal",
    "presumption_common_law_rights",
    "presumption_against_retrospectivity",
    "ejusdem_generis",
    "expressio_unius",
]

CONFIDENCE = ["high", "medium", "low"]

SCREENSHOT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "primary_category": {"type": "string", "enum": PRIMARY_CATEGORIES},
        "secondary_tags": {
            "type": "array",
            "items": {"type": "string", "enum": SECONDARY_TAGS},
        },
        "source_detection": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "platform": {"type": "string"},
                "ui_version_hints": {"type": "string"},
                "device_hints": {"type": "string"},
            },
            "required": ["platform"],
        },
        "participants": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "label": {"type": "string"},
                    "identifier": {"type": "string"},
                    "role": {"type": "string"},
                    "redaction_required": {"type": "boolean"},
                },
                "required": ["label", "redaction_required"],
            },
        },
        "temporal": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "value": {"type": "string"},
                    "kind": {
                        "type": "string",
                        "enum": ["platform_ui", "device_clock", "metadata_overlay", "handwritten", "other"],
                    },
                    "context": {"type": "string"},
                },
                "required": ["value", "kind"],
            },
        },
        "content_transcript": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "speaker": {"type": "string"},
                    "text": {"type": "string"},
                    "timestamp": {"type": "string"},
                },
                "required": ["text"],
            },
        },
        "statutory_engagement": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "citation": {"type": "string"},
                    "quoted_utterance": {"type": "string"},
                    "speaker": {"type": "string"},
                    "addressee": {"type": "string"},
                    "context_relied_on": {"type": "string"},
                    "meaning_in_context": {"type": "string"},
                    "element_engaged": {"type": "string"},
                    "test_applied": {"type": "string"},
                    "pattern_or_single": {
                        "type": "string",
                        "enum": ["single", "pattern_contributor"],
                    },
                    "interpretive_step": {"type": "string", "enum": INTERPRETIVE_STEPS},
                    "interpretive_reasoning": {"type": "string"},
                    "alternative_construction": {"type": "string"},
                    "confidence": {"type": "string", "enum": CONFIDENCE},
                },
                "required": [
                    "citation",
                    "quoted_utterance",
                    "speaker",
                    "context_relied_on",
                    "meaning_in_context",
                    "element_engaged",
                    "test_applied",
                    "pattern_or_single",
                    "interpretive_step",
                    "interpretive_reasoning",
                    "confidence",
                ],
            },
        },
        "authentication_concerns": {
            "type": "array",
            "items": {"type": "string"},
        },
        "privilege_publication_concerns": {
            "type": "array",
            "items": {"type": "string"},
        },
        "priority": {"type": "string", "enum": ["H", "M", "L"]},
        "notes": {"type": "string"},
    },
    "required": [
        "primary_category",
        "secondary_tags",
        "source_detection",
        "participants",
        "temporal",
        "content_transcript",
        "statutory_engagement",
        "authentication_concerns",
        "privilege_publication_concerns",
        "priority",
        "notes",
    ],
}


@dataclass
class ImageInput:
    record_id: str
    name: str
    local_path: Path
    drive_path: str


def _load_client():
    try:
        import anthropic  # type: ignore
    except ImportError as e:
        print("Missing anthropic SDK. pip install anthropic", file=sys.stderr)
        raise SystemExit(1) from e
    return anthropic.Anthropic()


def _iter_manifest(manifest_path: Path) -> list[ImageInput]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    out: list[ImageInput] = []
    for f in data.get("files", []):
        local = Path(f["local_path"])
        if local.suffix.lower() not in IMAGE_EXTS:
            continue
        if not local.exists():
            continue
        out.append(
            ImageInput(
                record_id=f.get("drive_id") or f.get("sha256", local.stem)[:24],
                name=f["name"],
                local_path=local,
                drive_path=f.get("drive_path", f["name"]),
            )
        )
    return out


def _build_user_content(img: ImageInput) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    try:
        data = img.local_path.read_bytes()
    except Exception as e:
        return (
            [{"type": "text", "text": f"[IMAGE UNREADABLE: {e}] {img.drive_path}"}],
            [f"read failed: {e}"],
        )
    if len(data) > MAX_IMAGE_BYTES:
        warnings.append(
            f"image is {len(data)} bytes; over {MAX_IMAGE_BYTES} threshold — sending anyway"
        )
    mime = mimetypes.guess_type(str(img.local_path))[0] or "image/jpeg"
    if mime == "image/heic":
        warnings.append("HEIC may not be accepted — convert to JPEG first")
    b64 = base64.standard_b64encode(data).decode("ascii")
    header = (
        f"SCREENSHOT METADATA\n"
        f"  record_id: {img.record_id}\n"
        f"  filename: {img.name}\n"
        f"  relative_path: {img.drive_path}\n"
        f"Apply the strict-interpretation framework. Return strict JSON only — "
        f"no prose outside the schema."
    )
    return (
        [
            {"type": "text", "text": header},
            {
                "type": "image",
                "source": {"type": "base64", "media_type": mime, "data": b64},
            },
        ],
        warnings,
    )


def analyse_one(client, img: ImageInput, framework: str) -> dict[str, Any]:
    import anthropic  # type: ignore

    content, warnings = _build_user_content(img)
    system = [
        {
            "type": "text",
            "text": framework,
            "cache_control": {"type": "ephemeral"},
        }
    ]
    last_err: Exception | None = None
    for attempt in range(3):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                thinking={"type": "adaptive"},
                output_config={
                    "effort": "high",
                    "format": {"type": "json_schema", "schema": SCREENSHOT_SCHEMA},
                },
                system=system,
                messages=[{"role": "user", "content": content}],
            )
            break
        except anthropic.RateLimitError as e:
            last_err = e
            time.sleep(min(2 ** attempt * 5, 60))
        except anthropic.APIStatusError as e:
            last_err = e
            if e.status_code and e.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            raise
    else:
        raise RuntimeError(f"API failed after retries: {last_err}")

    text_block = next((b for b in response.content if b.type == "text"), None)
    parsed: dict[str, Any] = {}
    parse_error: str | None = None
    if text_block:
        try:
            parsed = json.loads(text_block.text)
        except json.JSONDecodeError as e:
            parse_error = f"model output not valid JSON: {e}"
            parsed = {"raw": text_block.text}

    usage = response.usage
    return {
        "header": HEADER,
        "record_id": img.record_id,
        "name": img.name,
        "drive_path": img.drive_path,
        "local_path": str(img.local_path),
        "model": MODEL,
        "stop_reason": response.stop_reason,
        "usage": {
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", 0),
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", 0),
        },
        "warnings": warnings,
        "parse_error": parse_error,
        "analysis": parsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run strict-interpretation analysis on every screenshot in a manifest."
    )
    parser.add_argument("--manifest", required=True, help="Manifest JSON from local_ingest.py")
    parser.add_argument("--framework", required=True, help="Path to screenshot_strict_interpretation.md")
    parser.add_argument("--output", required=True, help="Output dir for per-image analyses")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set.")

    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    framework = Path(args.framework).read_text(encoding="utf-8")
    images = _iter_manifest(Path(args.manifest))
    print(f"{len(images)} screenshots to analyse")

    client = _load_client()
    done = 0
    cache_reads = 0
    errors = 0
    for img in images:
        out_path = output_dir / f"{img.record_id}.screenshot.json"
        if args.resume and out_path.exists():
            continue
        print(f"[{done + 1}/{len(images)}] {img.drive_path}")
        try:
            result = analyse_one(client, img, framework)
            out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
            cache_reads += result["usage"]["cache_read_input_tokens"]
        except Exception as e:
            errors += 1
            print(f"    ERROR: {e}", file=sys.stderr)
            (output_dir / f"{img.record_id}.error.json").write_text(
                json.dumps(
                    {"header": HEADER, "record_id": img.record_id, "error": str(e)},
                    indent=2,
                ),
                encoding="utf-8",
            )
        done += 1
        if args.limit and done >= args.limit:
            break

    print(
        f"\n{done} analysed, {errors} errors. Cache-read tokens: {cache_reads:,} "
        f"(higher = framework prompt is being cached)."
    )


if __name__ == "__main__":
    main()
