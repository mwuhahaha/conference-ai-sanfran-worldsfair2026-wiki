import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

enrichment = importlib.import_module("enrich_all_articles_from_sources")
corpus = importlib.import_module("process_slide_corpus_ai")
quarantine = importlib.import_module("quarantine_stale_slide_ai")
ocr_pipeline = importlib.import_module("run_slide_ocr_pipeline")


VIDEO_ID = "AAAAAAAAAAA"


@pytest.fixture(autouse=True)
def clear_classifier_validation_cache():
    enrichment.classification_audit_violations.cache_clear()
    yield
    enrichment.classification_audit_violations.cache_clear()


def bound_audit(image: Path, *, text: str) -> dict[str, object]:
    args = quarantine.contract_args()
    item = {"video_id": VIDEO_ID, "deck_kind": "dense", "images": 1}
    digest = hashlib.sha256(image.read_bytes()).hexdigest()
    manifest = [{"filename": image.name, "sha256": digest}]
    manifest_digest = hashlib.sha256(
        json.dumps(manifest, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()
    cache_policy = corpus.expected_cache_policy(item, args)
    record = {
        "image": str(image),
        "image_sha256": digest,
        "cache_schema_version": corpus.CACHE_SCHEMA_VERSION,
        "cache_status": "succeeded",
        "policy_version": corpus.POLICY_VERSION,
        "prompt_contract_sha256": corpus.PROMPT_CONTRACT_SHA256,
        "cache_policy": cache_policy,
        "model": args.model,
        "deck_kind": "dense",
        "confidence": 0.95,
        "is_content_slide": True,
        "text": text,
    }
    return {
        "status": "succeeded",
        "cache_schema_version": corpus.CACHE_SCHEMA_VERSION,
        "video_id": VIDEO_ID,
        "deck_kind": "dense",
        "model": args.model,
        "policy_version": corpus.POLICY_VERSION,
        "prompt_contract_sha256": corpus.PROMPT_CONTRACT_SHA256,
        "cache_policy": cache_policy,
        "input_manifest": manifest,
        "input_manifest_sha256": manifest_digest,
        "min_confidence": args.min_confidence,
        "hide_rejected": False,
        "accepted_count": 1,
        "rejected_count": 0,
        "accepted": [record],
        "rejected": [],
    }


def classifier_fixture(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    raw = tmp_path / "raw" / "sources"
    wiki = tmp_path / "wiki"
    deck_root = wiki / "assets" / "dense-slides"
    image = deck_root / VIDEO_ID / "slide-001.jpg"
    image.parent.mkdir(parents=True)
    image.write_bytes(b"exact slide image bytes")
    audit = raw / "slide-ai-classification" / "dense" / VIDEO_ID / "audit.json"
    audit.parent.mkdir(parents=True)

    monkeypatch.setattr(enrichment, "RAW", raw)
    monkeypatch.setattr(enrichment, "WIKI", wiki)
    monkeypatch.setattr(enrichment, "TRANSCRIPT_DIRS", [])
    monkeypatch.setattr(
        corpus,
        "audit_path",
        lambda video_id, kind: (
            raw / "slide-ai-classification" / kind / video_id / "audit.json"
        ),
    )
    monkeypatch.setitem(corpus.DECKS, "dense", deck_root)
    return audit, image


def test_current_bound_classifier_text_is_admitted(tmp_path, monkeypatch):
    audit, image = classifier_fixture(tmp_path, monkeypatch)
    expected = "Fresh retrieval evidence improves context quality"
    audit.write_text(json.dumps(bound_audit(image, text=expected)), encoding="utf-8")

    assert enrichment.classification_text(VIDEO_ID) == [expected]


def test_stale_classifier_text_contributes_zero_synthesis_text(
    tmp_path,
    monkeypatch,
):
    audit, image = classifier_fixture(tmp_path, monkeypatch)
    stale_text = "Dangerous classifier evidence changes synthesis"
    payload = bound_audit(image, text=stale_text)
    payload["policy_version"] = "historical-policy"
    audit.write_text(json.dumps(payload), encoding="utf-8")

    assert "policy_version_mismatch" in enrichment.classification_audit_violations(
        "dense", VIDEO_ID
    )
    assert enrichment.classification_text(VIDEO_ID) == []
    assert enrichment.classification_text(VIDEO_ID) == []

    evidence = enrichment.evidence_for_video(VIDEO_ID)
    rendered = enrichment.render_evidence_section([VIDEO_ID])
    assert evidence["slide_lines"] == []
    assert evidence["slide_keywords"] == []
    assert stale_text not in rendered


def test_public_entry_points_run_check_only_before_consumers(
    tmp_path,
    monkeypatch,
):
    commands: list[list[str]] = []

    def record(command: list[str]) -> subprocess.CompletedProcess:
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(ocr_pipeline, "run", record)
    monkeypatch.setattr(ocr_pipeline, "AUDIT_PATH", tmp_path / "missing-audit.json")
    monkeypatch.setattr(
        sys,
        "argv",
        ["run_slide_ocr_pipeline.py", "--classify-video-id", VIDEO_ID],
    )

    assert ocr_pipeline.main() == 0

    check_index = next(
        index
        for index, command in enumerate(commands)
        if "scripts/quarantine_stale_slide_ai.py" in command
    )
    classify_index = next(
        index
        for index, command in enumerate(commands)
        if "scripts/classify_and_recreate_slides.py" in command
    )
    first_index_consumer = next(
        index
        for index, command in enumerate(commands)
        if "scripts/generate_tool_inventory.py" in command
    )
    build_index = commands.index(["npm", "run", "build"])
    assert classify_index < check_index < first_index_consumer < build_index
    assert "--apply" not in commands[check_index]

    profile = json.loads((ROOT / ".wiki-maker.json").read_text(encoding="utf-8"))
    adapters = {adapter["key"]: adapter for adapter in profile["adapters"]}
    positions = {
        adapter["key"]: index for index, adapter in enumerate(profile["adapters"])
    }
    check = adapters["slide_ai_admission_check"]
    assert check["command"] == [
        "python3",
        "scripts/quarantine_stale_slide_ai.py",
    ]
    assert "--apply" not in check["command"]
    assert "slide_ai_admission_check" in adapters["talk_synthesis"]["dependencies"]
    assert "slide_ai_admission_check" in adapters["source_enrichment"]["dependencies"]
    for adapter in profile["adapters"]:
        for dependency in (
            adapter.get("dependencies", [])
            + adapter.get("optional_dependencies", [])
        ):
            assert positions[dependency] < positions[adapter["key"]]

    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    scripts = package["scripts"]
    assert scripts["slide-ai-check"] == "python3 scripts/quarantine_stale_slide_ai.py"
    assert scripts["build"].split(" && ")[0] == "npm run slide-ai-check"
