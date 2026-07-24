import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_profile() -> dict:
    return json.loads((ROOT / ".wiki-maker.json").read_text(encoding="utf-8"))


def selected_adapter_keys(profile: dict, change_type: str) -> list[str]:
    adapters = profile["adapters"]
    by_key = {adapter["key"]: adapter for adapter in adapters}
    selected = {
        adapter["key"]
        for adapter in adapters
        if "any" in adapter["triggers"] or change_type in adapter["triggers"]
    }
    pending = list(selected)
    while pending:
        key = pending.pop()
        for dependency in by_key[key].get("dependencies", []):
            if dependency not in selected:
                selected.add(dependency)
                pending.append(dependency)
    return [adapter["key"] for adapter in adapters if adapter["key"] in selected]


def ancestor_keys(profile: dict, key: str, selected: set[str]) -> set[str]:
    by_key = {adapter["key"]: adapter for adapter in profile["adapters"]}
    ancestors: set[str] = set()
    pending = [key]
    while pending:
        current = pending.pop()
        adapter = by_key[current]
        dependencies = adapter.get("dependencies", []) + adapter.get(
            "optional_dependencies", []
        )
        for dependency in dependencies:
            if dependency in selected and dependency not in ancestors:
                ancestors.add(dependency)
                pending.append(dependency)
    return ancestors


def test_media_update_dag_has_one_body_mutation_tail_before_assessment() -> None:
    profile = load_profile()
    keys = selected_adapter_keys(profile, "media")

    assert keys == [
        "classify_media",
        "transcript_pages",
        "talk_media_map",
        "credibility_provider_checks",
        "credibility_policy",
        "company_profiles",
        "slide_ai_admission_check",
        "talk_synthesis",
        "source_enrichment",
        "livestream_segment_projection",
        "attendance_evidence_sync",
        "synthesis_layers",
        "evolution_context",
        "sanitize_public_text",
        "agent_source_index",
        "normalize_articles",
        "page_assessments",
        "static_export",
    ]

    adapters = {adapter["key"]: adapter for adapter in profile["adapters"]}
    assert "livestream_segments" not in adapters
    assert all(
        adapter["command"][:2]
        != ["python3", "scripts/generate_livestream_talk_segments.py"]
        for adapter in adapters.values()
    )
    assert adapters["talk_media_map"]["dependencies"] == ["transcript_pages"]
    assert adapters["talk_synthesis"]["dependencies"] == [
        "transcript_pages",
        "credibility_policy",
        "talk_media_map",
        "slide_ai_admission_check",
    ]
    assert adapters["talk_synthesis"]["version"] == "v4"
    assert adapters["talk_synthesis"]["command"] == [
        "python3",
        "scripts/generate_talk_synthesis.py",
        "--all",
        "--model",
        "gpt-5.4-mini",
        "--workers",
        "3",
        "--timeout-seconds",
        "900",
    ]
    assert adapters["talk_synthesis"]["timeout_seconds"] == 6500
    assert "scripts/generate_talk_synthesis.py" in adapters["synthesis_layers"][
        "implementation_inputs"
    ]
    assert adapters["sanitize_public_text"].get("optional_dependencies") == [
        "evolution_context"
    ]
    assert adapters["livestream_segment_projection"]["dependencies"] == [
        "source_enrichment"
    ]
    assert adapters["livestream_segment_projection"]["triggers"] == ["any"]
    assert adapters["attendance_evidence_sync"]["dependencies"] == [
        "livestream_segment_projection"
    ]
    assert adapters["attendance_evidence_sync"]["triggers"] == ["any"]
    assert adapters["attendance_evidence_sync"]["command"] == [
        "python3",
        "scripts/generate_attendance_calibration.py",
        "--check-current",
    ]
    assert adapters["synthesis_layers"]["optional_dependencies"] == [
        "attendance_evidence_sync"
    ]
    assert adapters["agent_source_index"]["dependencies"] == [
        "sanitize_public_text"
    ]
    assert adapters["normalize_articles"]["dependencies"] == [
        "agent_source_index"
    ]
    assert adapters["normalize_articles"]["version"] == "v3"
    assert adapters["page_assessments"]["dependencies"] == [
        "normalize_articles"
    ]
    assert adapters["static_export"]["dependencies"] == ["page_assessments"]

    assessment_index = keys.index("page_assessments")
    assert ancestor_keys(profile, "page_assessments", set(keys)) == set(
        keys[:assessment_index]
    )
    for key in keys[assessment_index + 1 :]:
        assert "wiki" not in adapters[key]["mutates"]

    general_keys = selected_adapter_keys(profile, "general")
    assert "livestream_segment_projection" in general_keys
    assert "attendance_evidence_sync" in general_keys
    assert general_keys.index("source_enrichment") < general_keys.index(
        "livestream_segment_projection"
    ) < general_keys.index("attendance_evidence_sync")


def test_update_export_is_nonmutating_while_ci_build_remains_fail_closed() -> None:
    profile = load_profile()
    adapters = {adapter["key"]: adapter for adapter in profile["adapters"]}
    scripts = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))[
        "scripts"
    ]

    assert adapters["static_export"]["command"] == [
        "npm",
        "run",
        "build:validated",
    ]
    assert scripts["build:validated"].split(" && ") == [
        "npm run slide-ai-check",
        "npm run audit:segment-projection",
        "npm run export",
        "npm run audit:media-roles",
        "npm run audit:attendance",
    ]

    ci_build = scripts["build"].split(" && ")
    assert ci_build == [
        "npm run slide-ai-check",
        "npm run sanitize",
        "npm run agent-index",
        "npm run normalize",
        "npm run export",
        "npm run agent-product",
    ]
    assert "npm run assess" not in ci_build


def test_all_profile_dependencies_precede_their_consumers() -> None:
    profile = load_profile()
    positions = {
        adapter["key"]: index for index, adapter in enumerate(profile["adapters"])
    }
    for adapter in profile["adapters"]:
        dependencies = adapter.get("dependencies", []) + adapter.get(
            "optional_dependencies", []
        )
        for dependency in dependencies:
            assert positions[dependency] < positions[adapter["key"]]
