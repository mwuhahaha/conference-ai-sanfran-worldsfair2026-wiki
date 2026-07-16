#!/usr/bin/env python3
"""Build the static, evidence-bearing relationship explorer dataset.

The extractor deliberately keeps ordinary wiki navigation separate from the
three supported semantic templates. It has no network or model dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
DEFAULT_PROFILE = ROOT / "raw" / "sources" / "relationship-explorer-profile.json"
DEFAULT_OUTPUT = ROOT / "dist" / "relationship-data.json"
DEFAULT_INTERNAL_AUDIT = ROOT / ".ops" / "state" / "cache" / "relationship-explorer" / "audit.json"
FORBIDDEN_PUBLIC_KEY_PARTS = ("score", "ranking", "calibration", "weight")
FORBIDDEN_PUBLIC_VALUE_PHRASES = (
    "internal score",
    "internal review score",
    "ranking score",
    "credibility score",
    "credibility weight",
    "calibration fixture",
    "calibration value",
    "calibration score",
    "candidate rank",
)
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")


@dataclass(frozen=True)
class PageRecord:
    id: str
    title: str
    category: str
    body: str
    excerpt: str
    url: str
    source: str = ""


def _value(page: object, key: str, default: Any = "") -> Any:
    if isinstance(page, Mapping):
        return page.get(key, default)
    return getattr(page, key, default)


def normalize_pages(pages: Iterable[object]) -> list[PageRecord]:
    """Normalize exporter Page objects or equivalent generic dictionaries."""
    records: list[PageRecord] = []
    for page in pages:
        page_id = str(_value(page, "id")).strip().strip("/")
        if not page_id:
            raise ValueError("Every relationship page requires a non-empty id")
        url = _value(page, "url", f"/{page_id}/")
        if callable(url):
            url = url()
        source = _value(page, "source", "")
        records.append(
            PageRecord(
                id=page_id,
                title=str(_value(page, "title", page_id)),
                category=str(_value(page, "category", "root")),
                body=str(_value(page, "body", "")),
                excerpt=str(_value(page, "excerpt", "")),
                url=str(url),
                source=str(source),
            )
        )
    ids = [record.id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("Relationship pages contain duplicate ids")
    return sorted(records, key=lambda item: item.id)


def _frontmatter_and_body(raw: str) -> tuple[dict[str, str], str]:
    frontmatter: dict[str, str] = {}
    body = raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end >= 0:
            for line in raw[4:end].splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    frontmatter[key.strip()] = value.strip().strip('"')
            body = raw[end + 5 :]
    return frontmatter, body.strip()


def _first_heading(body: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, flags=re.M)
    return re.sub(r"[*_`]", "", match.group(1)).strip() if match else ""


def _excerpt(body: str) -> str:
    text = re.sub(r"```.*?```", " ", body, flags=re.S)
    text = WIKILINK_RE.sub(lambda match: match.group(1).partition("|")[2] or match.group(1).partition("|")[0], text)
    text = re.sub(r"[#*_`>|\[\]():-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()[:220]


def load_wiki_pages(wiki_root: Path = WIKI) -> list[PageRecord]:
    pages: list[PageRecord] = []
    for path in sorted(wiki_root.rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        frontmatter, body = _frontmatter_and_body(raw)
        rel = path.relative_to(wiki_root).with_suffix("")
        page_id = rel.as_posix()
        category = frontmatter.get("category") or (rel.parts[0] if len(rel.parts) > 1 else "root")
        title = frontmatter.get("title") or _first_heading(body) or path.stem.replace("-", " ").title()
        pages.append(PageRecord(page_id, title, category, body, _excerpt(body), "/" if page_id == "overview" else f"/{page_id}/", str(path)))
    return pages


def load_profile(path: Path = DEFAULT_PROFILE) -> dict[str, Any]:
    profile = json.loads(path.read_text(encoding="utf-8"))
    required = {"id", "version", "roleCategories", "organizationRoles"}
    missing = sorted(required - profile.keys())
    if missing:
        raise ValueError(f"Relationship profile missing keys: {', '.join(missing)}")
    return profile


def _resolve_target(target: str, by_id: Mapping[str, PageRecord], by_stem: Mapping[str, PageRecord]) -> PageRecord | None:
    cleaned = target.split("|", 1)[0].split("#", 1)[0].strip().strip("/")
    return by_id.get(cleaned) or by_stem.get(Path(cleaned).name)


def _navigation_only(page: PageRecord, profile: Mapping[str, Any]) -> bool:
    if page.category in set(profile.get("navigationOnlyCategories", [])):
        return True
    if page.id in set(profile.get("navigationOnlyIds", [])):
        return True
    if Path(page.id).name in {"index", page.category}:
        return True
    title = page.title.casefold()
    return any(pattern.casefold() in title for pattern in profile.get("navigationOnlyTitlePatterns", []))


def _role(page: PageRecord, profile: Mapping[str, Any]) -> tuple[str, dict[str, Any] | None]:
    categories = profile["roleCategories"]
    if page.category in categories.get("people", []):
        return "person", None
    if page.category in categories.get("concepts", []):
        return "concept", None
    if page.category in categories.get("organizations", []):
        classification = profile["organizationRoles"].get(page.id)
        if classification and classification.get("role") == "vendor":
            return "vendor", classification
        return "organization", classification
    return "evidence", None


def _stable_relationship_id(record: Mapping[str, Any]) -> str:
    evidence_ids = sorted({evidence["id"] for evidence in record["evidence"]})
    identity = "\x1f".join(
        [record["template"], record["relationType"], record["source"], record["target"], *evidence_ids]
    )
    return "rel-" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:20]


def _relationship_sort_key(record: Mapping[str, Any]) -> tuple[str, ...]:
    return (record["template"], record["source"], record["target"], record["relationType"], record["id"])


def _add_candidate(
    candidates: dict[tuple[str, str, str, str, tuple[tuple[str, str], ...]], dict[str, Any]],
    *,
    template: str,
    relation_type: str,
    source: str,
    target: str,
    direction: str,
    reason: str,
    evidence: Iterable[tuple[str, str]],
    source_layers: Iterable[str],
    boundary: str,
) -> None:
    if direction == "undirected" and target < source:
        source, target = target, source
    evidence_path = tuple(sorted(set(evidence)))
    key = (template, relation_type, source, target, evidence_path)
    candidate = candidates.setdefault(
        key,
        {
            "template": template,
            "relationType": relation_type,
            "source": source,
            "target": target,
            "direction": direction,
            "derivation": "derived",
            "publicReason": reason,
            "evidence": set(),
            "sourceLayers": set(),
            "boundary": boundary,
        },
    )
    candidate["evidence"].update(evidence_path)
    candidate["sourceLayers"].update(source_layers)


def _finalize_candidates(
    candidates: Mapping[
        tuple[str, str, str, str, tuple[tuple[str, str], ...]], dict[str, Any]
    ]
) -> list[dict[str, Any]]:
    relationships: list[dict[str, Any]] = []
    for candidate in candidates.values():
        record = {key: value for key, value in candidate.items() if key not in {"evidence", "sourceLayers"}}
        record["evidence"] = [
            {"id": evidence_id, "sourceLayer": source_layer}
            for evidence_id, source_layer in sorted(candidate["evidence"])
        ]
        record["sourceLayers"] = sorted(candidate["sourceLayers"])
        record["id"] = _stable_relationship_id(record)
        relationships.append(record)
    return sorted(relationships, key=_relationship_sort_key)


def _build_matrix(relationships: list[dict[str, Any]], template: str, rows: list[str], columns: list[str]) -> dict[str, Any]:
    grouped: dict[tuple[str, str], list[str]] = defaultdict(list)
    for relationship in relationships:
        if relationship["template"] == template:
            grouped[(relationship["source"], relationship["target"])].append(relationship["id"])
    return {
        "rows": rows,
        "columns": columns,
        "cells": [
            {"source": source, "target": target, "count": len(ids), "relationshipIds": sorted(ids)}
            for (source, target), ids in sorted(grouped.items())
        ],
    }


def _find_forbidden_keys(value: Any, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_folded = key.casefold()
            if any(part in key_folded for part in FORBIDDEN_PUBLIC_KEY_PARTS):
                findings.append(f"{path}.{key}")
            findings.extend(_find_forbidden_keys(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(_find_forbidden_keys(child, f"{path}[{index}]"))
    return findings


def _find_forbidden_values(value: Any, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            findings.extend(_find_forbidden_values(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(_find_forbidden_values(child, f"{path}[{index}]"))
    elif isinstance(value, str):
        folded = value.casefold()
        if any(phrase in folded for phrase in FORBIDDEN_PUBLIC_VALUE_PHRASES):
            findings.append(path)
    return findings


def audit_dataset(dataset: Mapping[str, Any], profile: Mapping[str, Any] | None = None) -> dict[str, Any]:
    errors: list[str] = []
    review_candidates: list[dict[str, str]] = []
    node_ids = {node.get("id") for node in dataset.get("nodes", [])}
    vendor_ids = set(dataset.get("roles", {}).get("vendors", []))
    people_ids = set(dataset.get("roles", {}).get("people", []))
    concept_ids = set(dataset.get("roles", {}).get("concepts", []))
    navigation_only_ids = {node.get("id") for node in dataset.get("nodes", []) if node.get("navigationOnly")}
    allowed_layers = set((profile or {}).get("sourceLayers", []))
    profile_vendors = {
        page_id for page_id, value in (profile or {}).get("organizationRoles", {}).items() if value.get("role") == "vendor"
    }

    for path in _find_forbidden_keys(dataset):
        errors.append(f"Forbidden internal scoring/ranking key in public dataset: {path}")
    for path in _find_forbidden_values(dataset):
        errors.append(f"Forbidden internal scoring/ranking detail in public dataset: {path}")
    for relationship in dataset.get("relationships", []):
        for key in ("source", "target"):
            if relationship.get(key) not in node_ids:
                errors.append(f"Relationship {relationship.get('id')} has missing {key}: {relationship.get(key)}")
        if not relationship.get("evidence"):
            errors.append(f"Relationship {relationship.get('id')} has no evidence")
        evidence_ids = {evidence.get("id") for evidence in relationship.get("evidence", [])}
        if evidence_ids and evidence_ids <= {relationship.get("source"), relationship.get("target")}:
            errors.append(f"Relationship {relationship.get('id')} has only circular endpoint evidence")
        for evidence in relationship.get("evidence", []):
            if evidence.get("id") not in node_ids:
                errors.append(f"Relationship {relationship.get('id')} has missing evidence endpoint: {evidence.get('id')}")
            if allowed_layers and evidence.get("sourceLayer") not in allowed_layers:
                errors.append(f"Relationship {relationship.get('id')} has unsupported source layer: {evidence.get('sourceLayer')}")
            if evidence.get("id") in navigation_only_ids:
                errors.append(f"Relationship {relationship.get('id')} uses navigation-only evidence: {evidence.get('id')}")
        for source_layer in relationship.get("sourceLayers", []):
            if allowed_layers and source_layer not in allowed_layers:
                errors.append(f"Relationship {relationship.get('id')} declares unsupported source layer: {source_layer}")
        template = relationship.get("template")
        source, target = relationship.get("source"), relationship.get("target")
        if template == "vendor_concept" and (source not in vendor_ids or target not in concept_ids):
            errors.append(f"Vendor-concept relationship {relationship.get('id')} has invalid endpoint roles")
        if template == "person_concept" and (source not in people_ids or target not in concept_ids):
            errors.append(f"Person-concept relationship {relationship.get('id')} has invalid endpoint roles")
        if template == "concept_concept" and (source not in concept_ids or target not in concept_ids or source == target):
            errors.append(f"Concept-concept relationship {relationship.get('id')} has invalid endpoint roles")
        if relationship.get("template") == "vendor_concept" and relationship.get("source") not in vendor_ids:
            errors.append(f"Vendor relationship {relationship.get('id')} uses an unclassified organization")
        if all(key in relationship for key in ("template", "relationType", "source", "target", "evidence")):
            expected_id = _stable_relationship_id(relationship)
            if relationship.get("id") != expected_id:
                errors.append(f"Relationship {relationship.get('id')} does not have its deterministic id {expected_id}")
    for node in dataset.get("nodes", []):
        if node.get("role") != "vendor":
            continue
        if not node.get("roleReason") or not node.get("roleSourceRefs"):
            errors.append(f"Public vendor role lacks a reason or source reference: {node.get('id')}")
    unsupported_vendors = sorted(vendor_ids - profile_vendors) if profile else []
    errors.extend(f"Public vendor role lacks explicit profile classification: {page_id}" for page_id in unsupported_vendors)
    if profile:
        organization_categories = set(profile.get("roleCategories", {}).get("organizations", []))
        classified = set(profile.get("organizationRoles", {}))
        review_candidates = [
            {"type": "unclassified_organization", "id": node["id"], "reason": "No explicit organization role is recorded."}
            for node in dataset.get("nodes", [])
            if node.get("category") in organization_categories and node.get("id") not in classified
        ]
    return {"errors": sorted(set(errors)), "reviewCandidates": sorted(review_candidates, key=lambda item: item["id"])}


def build_relationship_dataset(
    pages: Iterable[object],
    profile: Mapping[str, Any],
    *,
    company_profiles: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a deterministic public relationship dataset.

    ``company_profiles`` may confirm references declared by the adapter, but it
    never classifies a vendor. Only ``profile.organizationRoles`` can do so.
    """
    records = normalize_pages(pages)
    by_id = {page.id: page for page in records}
    if company_profiles is not None:
        for page_id, classification in profile.get("organizationRoles", {}).items():
            if classification.get("role") != "vendor":
                continue
            slug = page_id.partition("/")[2]
            if any("company-profiles.json#" in ref for ref in classification.get("sourceRefs", [])) and slug not in company_profiles:
                raise ValueError(f"Vendor classification references a missing company profile: {page_id}")
    by_stem: dict[str, PageRecord] = {}
    for page in records:
        by_stem.setdefault(Path(page.id).name, page)

    outgoing: dict[str, set[str]] = {page.id: set() for page in records}
    for page in records:
        for match in WIKILINK_RE.finditer(page.body):
            linked = _resolve_target(match.group(1), by_id, by_stem)
            if linked and linked.id != page.id:
                outgoing[page.id].add(linked.id)
    adjacency: dict[str, set[str]] = {page.id: set() for page in records}
    for source, targets in outgoing.items():
        for target in targets:
            adjacency[source].add(target)
            adjacency[target].add(source)

    navigation_only = {page.id for page in records if _navigation_only(page, profile)}
    nodes: list[dict[str, Any]] = []
    roles: dict[str, list[str]] = {"vendors": [], "people": [], "concepts": []}
    role_by_id: dict[str, str] = {}
    for page in records:
        role, classification = _role(page, profile)
        role_by_id[page.id] = role
        node: dict[str, Any] = {
            "id": page.id,
            "title": page.title,
            "category": page.category,
            "role": role,
            "url": page.url,
            "excerpt": page.excerpt,
            "navigationOnly": page.id in navigation_only,
        }
        if classification:
            node["roleReason"] = str(classification.get("reason", ""))
            node["roleSourceRefs"] = sorted(map(str, classification.get("sourceRefs", [])))
        nodes.append(node)
        if role == "vendor":
            roles["vendors"].append(page.id)
        elif role == "person":
            roles["people"].append(page.id)
        elif role == "concept":
            roles["concepts"].append(page.id)
    for values in roles.values():
        values.sort()

    talks = sorted(
        page.id for page in records if page.category in set(profile.get("connectorCategories", ["talks"])) and page.id not in navigation_only
    )
    talk_people = {talk: sorted(adjacency[talk] & set(roles["people"])) for talk in talks}
    talk_concepts = {talk: sorted(adjacency[talk] & set(roles["concepts"])) for talk in talks}
    talk_vendors = {talk: sorted(adjacency[talk] & set(roles["vendors"])) for talk in talks}

    # Affiliation uses reciprocal wiki links. This avoids treating a one-sided
    # mention or a third-party URL as proof of employment/event association.
    vendor_people: dict[str, set[str]] = defaultdict(set)
    for vendor in roles["vendors"]:
        for person in roles["people"]:
            if person in outgoing[vendor] and vendor in outgoing[person]:
                vendor_people[vendor].add(person)

    candidates: dict[
        tuple[str, str, str, str, tuple[tuple[str, str], ...]], dict[str, Any]
    ] = {}
    title = {page.id: page.title for page in records}
    for talk in talks:
        represented_vendors = {
            vendor
            for person in talk_people[talk]
            for vendor, affiliated_people in vendor_people.items()
            if person in affiliated_people
        }
        for person in talk_people[talk]:
            for concept in talk_concepts[talk]:
                _add_candidate(
                    candidates,
                    template="person_concept",
                    relation_type="presented_at_talk_about",
                    source=person,
                    target=concept,
                    direction="directed",
                    reason=f"{title[person]} is connected to {title[concept]} through the scheduled talk {title[talk]}.",
                    evidence=[(talk, "official_schedule")],
                    source_layers=["official_schedule", "synthesis"],
                    boundary="The schedule establishes the speaker and session; the topic connection is labeled synthesis.",
                )
        for vendor in talk_vendors[talk]:
            if vendor in represented_vendors:
                continue
            for concept in talk_concepts[talk]:
                _add_candidate(
                    candidates,
                    template="vendor_concept",
                    relation_type="featured_in_talk_about",
                    source=vendor,
                    target=concept,
                    direction="directed",
                    reason=f"{title[vendor]} is connected to {title[concept]} through the scheduled talk {title[talk]}.",
                    evidence=[(talk, "official_schedule"), (vendor, "curated_public_source")],
                    source_layers=["official_schedule", "curated_public_source", "synthesis"],
                    boundary="The vendor role is explicitly classified; the schedule and linked topic provide the conference connection.",
                )

    talks_by_person: dict[str, set[str]] = defaultdict(set)
    for talk, people in talk_people.items():
        for person in people:
            talks_by_person[person].add(talk)
    for vendor, people in vendor_people.items():
        for person in sorted(people):
            for talk in sorted(talks_by_person[person]):
                for concept in talk_concepts[talk]:
                    _add_candidate(
                        candidates,
                        template="vendor_concept",
                        relation_type="represented_at_talk_about",
                        source=vendor,
                        target=concept,
                        direction="directed",
                        reason=f"{title[vendor]} is represented by {title[person]} in the scheduled talk {title[talk]}, which is connected to {title[concept]}.",
                        evidence=[(person, "official_schedule"), (talk, "official_schedule"), (vendor, "curated_public_source")],
                        source_layers=["official_schedule", "curated_public_source", "synthesis"],
                        boundary="Derived from explicit vendor classification, reciprocal affiliation links, the official schedule, and labeled topic synthesis.",
                    )

    for talk in talks:
        concepts = talk_concepts[talk]
        for index, left in enumerate(concepts):
            for right in concepts[index + 1 :]:
                _add_candidate(
                    candidates,
                    template="concept_concept",
                    relation_type="co_occurs_in_talk",
                    source=left,
                    target=right,
                    direction="undirected",
                    reason=f"{title[left]} and {title[right]} are both connected to the scheduled talk {title[talk]}.",
                    evidence=[(talk, "official_schedule")],
                    source_layers=["official_schedule", "synthesis"],
                    boundary="Co-occurrence is a labeled association, not causation, dependency, agreement, or endorsement.",
                )

    relationships = _finalize_candidates(candidates)
    evidence_node_ids = {
        evidence["id"]
        for relationship in relationships
        for evidence in relationship["evidence"]
    }
    nodes = [
        node
        for node in nodes
        if node["role"] in {"vendor", "organization", "person", "concept"} or node["id"] in evidence_node_ids
    ]
    facets = {
        "templates": dict(sorted(Counter(item["template"] for item in relationships).items())),
        "relationTypes": dict(sorted(Counter(item["relationType"] for item in relationships).items())),
        "sourceLayers": dict(sorted(Counter(layer for item in relationships for layer in item["sourceLayers"]).items())),
    }
    dataset: dict[str, Any] = {
        "schemaVersion": 1,
        "profile": {"id": profile["id"], "version": profile["version"]},
        "roles": roles,
        "nodes": nodes,
        "relationships": relationships,
        "facets": facets,
        "matrix": {
            "vendorConcept": _build_matrix(relationships, "vendor_concept", roles["vendors"], roles["concepts"]),
            "personConcept": _build_matrix(relationships, "person_concept", roles["people"], roles["concepts"]),
            "conceptConcept": _build_matrix(relationships, "concept_concept", roles["concepts"], roles["concepts"]),
        },
    }
    return dataset


def validate_dataset(dataset: Mapping[str, Any], profile: Mapping[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    required = {"schemaVersion", "profile", "roles", "nodes", "relationships", "facets", "matrix"}
    missing = sorted(required - dataset.keys())
    if missing:
        errors.append(f"Dataset missing keys: {', '.join(missing)}")
        return errors
    if dataset.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    node_ids = [node.get("id") for node in dataset.get("nodes", [])]
    if len(node_ids) != len(set(node_ids)):
        errors.append("Node ids are not unique")
    relationship_ids = [item.get("id") for item in dataset.get("relationships", [])]
    if len(relationship_ids) != len(set(relationship_ids)):
        errors.append("Relationship ids are not unique")
    for relationship in dataset.get("relationships", []):
        required_relationship = {"id", "template", "relationType", "source", "target", "direction", "derivation", "publicReason", "evidence", "sourceLayers", "boundary"}
        missing_relationship = required_relationship - relationship.keys()
        if missing_relationship:
            errors.append(f"Relationship {relationship.get('id')} missing keys: {', '.join(sorted(missing_relationship))}")
        if relationship.get("template") not in {"vendor_concept", "person_concept", "concept_concept"}:
            errors.append(f"Relationship {relationship.get('id')} has unsupported template")
    audit = audit_dataset(dataset, profile)
    errors.extend(audit["errors"])
    return sorted(set(errors))


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n").encode("utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Build and validate without writing public output")
    parser.add_argument("--validate", type=Path, metavar="PATH", help="Validate an existing relationship dataset")
    parser.add_argument("--write-internal-audit", action="store_true", help="Write the audit under ignored project-local state")
    args = parser.parse_args(argv)
    if args.check and args.write_internal_audit:
        parser.error("--write-internal-audit cannot be combined with --check")

    profile = load_profile(args.profile)
    if args.validate:
        dataset = json.loads(args.validate.read_text(encoding="utf-8"))
    else:
        company_profiles_path = ROOT / "raw" / "sources" / "company-profiles.json"
        company_profiles = json.loads(company_profiles_path.read_text(encoding="utf-8")) if company_profiles_path.exists() else None
        dataset = build_relationship_dataset(load_wiki_pages(), profile, company_profiles=company_profiles)

    errors = validate_dataset(dataset, profile)
    if args.write_internal_audit:
        DEFAULT_INTERNAL_AUDIT.parent.mkdir(parents=True, exist_ok=True)
        DEFAULT_INTERNAL_AUDIT.write_bytes(_json_bytes(audit_dataset(dataset, profile)))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if not args.check and not args.validate:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(_json_bytes(dataset))
        print(f"Wrote {args.output}")
    print(
        json.dumps(
            {
                "nodes": len(dataset["nodes"]),
                "relationships": len(dataset["relationships"]),
                "vendors": len(dataset["roles"]["vendors"]),
                "people": len(dataset["roles"]["people"]),
                "concepts": len(dataset["roles"]["concepts"]),
                "reviewCandidates": len(audit_dataset(dataset, profile)["reviewCandidates"]),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
