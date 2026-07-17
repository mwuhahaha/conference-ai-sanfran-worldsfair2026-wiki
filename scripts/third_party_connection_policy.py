#!/usr/bin/env python3
"""Internal-only gates for validating third-party entity connections."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
INTERNAL_DIR = ROOT / ".ops" / "state" / "cache" / "third-party-connections"
POLICY_PATH = INTERNAL_DIR / "policy.json"

# Internal calibration only. Scores prioritize review after hard gates; they do
# not establish identity, event association, publication approval, or endorsement.
WEIGHTS = {
    "official_exact_source": 45,
    "primary_owner_metadata": 30,
    "independent_corroboration": 20,
    "official_event_evidence": 35,
    "curator_approved": 15,
    "exact_name_only": -25,
    "identity_conflict": -100,
    "event_conflict": -80,
}


def normalize_url(value: str) -> str:
    value = value.strip().rstrip("/.,;:#")
    if not value:
        return ""
    parts = urlsplit(value if "://" in value else f"https://{value}")
    host = (parts.hostname or "").lower().removeprefix("www.")
    if not host:
        return value.lower()
    port = f":{parts.port}" if parts.port else ""
    path = parts.path.rstrip("/") or ""
    return urlunsplit(("https", host + port, path, parts.query, ""))


def assess_connection(
    signals: dict[str, bool],
    *,
    identity_required: bool = True,
    event_claim: bool = False,
) -> dict:
    score = max(0, min(100, 40 + sum(WEIGHTS[key] for key, present in signals.items() if present and key in WEIGHTS)))
    if signals.get("identity_conflict"):
        identity = "conflict"
    elif signals.get("official_exact_source") or signals.get("primary_owner_metadata"):
        identity = "verified"
    elif signals.get("independent_corroboration"):
        identity = "probable"
    else:
        identity = "unverified"

    if signals.get("event_conflict"):
        event = "conflict"
    elif signals.get("official_event_evidence"):
        event = "verified"
    elif event_claim:
        event = "unverified"
    else:
        event = "not_claimed"

    # Publication approval and endorsement are independent decisions. A curator
    # can approve source-backed context without endorsing its subject.
    endorsement = "endorsed" if signals.get("explicit_endorsement") else "not_endorsed"
    if identity == "conflict" or event == "conflict":
        disposition = "reject"
    elif identity_required and identity == "unverified":
        disposition = "hold_for_review"
    elif event_claim and event != "verified":
        disposition = "hold_for_review"
    elif signals.get("curator_approved"):
        disposition = "approved_connection"
    else:
        disposition = "context_only"
    return {
        "identity_status": identity,
        "event_status": event,
        "endorsement_status": endorsement,
        "disposition": disposition,
        "internal_score": score,
    }


def policy_document() -> dict:
    return {
        "schemaVersion": 2,
        "visibility": "internal-only",
        "note": "Numeric calibration prioritizes review only. Hard identity and event gates cannot be overridden by score.",
        "separateStates": [
            "source_quality",
            "identity_status",
            "event_status",
            "publication_disposition",
            "endorsement_status",
        ],
        "hardGates": [
            "A shared name, repository name, domain guess, or popularity signal never proves identity.",
            "A verified entity identity does not prove a World's Fair 2026 event association.",
            "Publication as supporting context does not imply endorsement.",
            "Curator publication approval does not imply endorsement.",
            "Conflicting primary evidence forces rejection regardless of score.",
        ],
        "weights": WEIGHTS,
    }


def write_internal_policy() -> Path:
    INTERNAL_DIR.mkdir(parents=True, exist_ok=True)
    POLICY_PATH.write_text(json.dumps(policy_document(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return POLICY_PATH
