"""Shared producer/consumer contract for accepted slide-vision cache entries."""

from __future__ import annotations

import hashlib


CACHE_SCHEMA_VERSION = 2
PROMPT_CONTRACT_VERSION = "slide-vision-exact-text-v2"
MIN_ACCEPTED_CONFIDENCE = 0.72

try:
    from slide_codex_safety import UNTRUSTED_MEDIA_PREAMBLE
except ModuleNotFoundError:  # Imported as scripts.slide_vision_cache_contract.
    from scripts.slide_codex_safety import UNTRUSTED_MEDIA_PREAMBLE


VISION_PROMPT = UNTRUSTED_MEDIA_PREAMBLE + """Read the visible text on this conference slide or video frame.

Return only JSON with this shape:
{"text":"line 1\\nline 2","confidence":0.0,"notes":"brief reason"}

Rules:
- Preserve exact visible wording, capitalization, punctuation, product names, and dates.
- Put each distinct visual line on its own newline.
- Do not infer hidden text.
- If the frame is mostly a person/stage/photo with no useful slide text, return an empty text string and low confidence.
- If existing OCR is close but has obvious character errors, correct it from the image.

Existing OCR to compare:
"""

CODEX_PROMPT_PREFIX = (
    UNTRUSTED_MEDIA_PREAMBLE
    + "Inspect only the attached image. Return only compact JSON with keys text, confidence, notes. "
    "text must be the exact visible slide/frame text with line breaks. Prefer meaningful slide text "
    "over background sponsor-wall fragments. If no useful visible text, use empty string. Do not use tools.\n\n"
    "Existing OCR to compare:\n"
)

PROMPT_CONTRACT_SHA256 = hashlib.sha256(
    f"{PROMPT_CONTRACT_VERSION}\n{VISION_PROMPT}\n{CODEX_PROMPT_PREFIX}".encode(
        "utf-8"
    )
).hexdigest()
