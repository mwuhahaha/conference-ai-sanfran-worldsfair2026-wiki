import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import jsonschema

from scripts import build_relationship_dataset as relationship_module
from scripts.build_relationship_dataset import (
    audit_dataset,
    build_relationship_dataset,
    main,
    validate_dataset,
)


def page(page_id, title, category, body="", frontmatter=None):
    record = {
        "id": page_id,
        "title": title,
        "category": category,
        "body": body,
        "excerpt": title,
        "url": f"/{page_id}/",
    }
    if frontmatter is not None:
        record["frontmatter"] = frontmatter
    return record


class RelationshipDatasetTests(unittest.TestCase):
    def setUp(self):
        self.profile = {
            "id": "fixture-event-vendor-concept",
            "version": 1,
            "roleCategories": {
                "people": ["people"],
                "concepts": ["topics"],
                "organizations": ["companies"],
            },
            "connectorCategories": ["talks"],
            "sourceLayers": ["official_schedule", "curated_public_source", "synthesis"],
            "navigationOnlyCategories": ["root"],
            "navigationOnlyIds": ["resources/everything-map"],
            "navigationOnlyTitlePatterns": ["transcript map"],
            "organizationRoles": {
                "companies/acme": {
                    "role": "vendor",
                    "reason": "Commercial product vendor on the official roster.",
                    "sourceRefs": [
                        "wiki/companies/acme.md",
                        "raw/sources/official-speakers.json",
                    ],
                },
                "companies/university": {
                    "role": "organization",
                    "reason": "University, not a vendor.",
                    "sourceRefs": ["wiki/companies/university.md"],
                },
            },
        }
        self.pages = [
            page("companies/acme", "Acme", "companies", "[[alice]] [[talk-one]]"),
            page("companies/university", "University", "companies", "[[alice]] [[security]]"),
            page("companies/ambiguous", "Ambiguous Lab", "companies", "[[alice]] [[security]]"),
            page("people/alice", "Alice", "people", "[[acme]] [[university]] [[talk-one]]"),
            page("talks/talk-one", "Secure Agents", "talks", "[[alice]] [[acme]] [[security]] [[evals]]"),
            page("topics/security", "Agent Security", "topics", "[[talk-one]]"),
            page("topics/evals", "Agent Evaluations", "topics", "[[talk-one]]"),
            page("resources/everything-map", "Transcript Map", "resources", "[[ambiguous]] [[security]] [[evals]]"),
            page("resources/non-event-video", "Unrelated Video", "resources", "[[ambiguous]] [[security]]"),
        ]

    def build(self):
        return build_relationship_dataset(self.pages, self.profile)

    def test_emits_three_templates_with_evidence_and_matrices(self):
        dataset = self.build()
        templates = {item["template"] for item in dataset["relationships"]}
        self.assertEqual({"vendor_concept", "person_concept", "concept_concept"}, templates)
        self.assertTrue(all(item["evidence"] for item in dataset["relationships"]))
        self.assertTrue(dataset["matrix"]["vendorConcept"]["cells"])
        self.assertTrue(dataset["matrix"]["personConcept"]["cells"])
        self.assertTrue(dataset["matrix"]["conceptConcept"]["cells"])
        co_occurrence = next(
            item for item in dataset["relationships"] if item["relationType"] == "co_occurs_in_talk"
        )
        self.assertEqual(
            {"talks/talk-one"}, {item["id"] for item in co_occurrence["evidence"]}
        )

    def test_only_explicit_vendor_can_emit_vendor_relationship(self):
        dataset = self.build()
        self.assertEqual(["companies/acme"], dataset["roles"]["vendors"])
        sources = {item["source"] for item in dataset["relationships"] if item["template"] == "vendor_concept"}
        self.assertEqual({"companies/acme"}, sources)
        ambiguous = next(node for node in dataset["nodes"] if node["id"] == "companies/ambiguous")
        self.assertEqual("organization", ambiguous["role"])

    def test_vendor_classification_does_not_depend_on_private_profile_candidates(self):
        dataset = build_relationship_dataset(self.pages, self.profile)
        self.assertEqual(["companies/acme"], dataset["roles"]["vendors"])

    def test_navigation_hubs_and_non_event_resources_cannot_create_semantics(self):
        dataset = self.build()
        evidence_ids = {evidence["id"] for item in dataset["relationships"] for evidence in item["evidence"]}
        self.assertNotIn("resources/everything-map", evidence_ids)
        self.assertNotIn("resources/non-event-video", evidence_ids)
        self.assertNotIn("navigationLinks", dataset)

    def test_structured_talk_ignores_backlinks_and_non_claim_sections(self):
        pages = [
            page("people/alice", "Alice", "people", "[[talk-one]]"),
            page("people/bob", "Bob", "people", "[[talk-one]]"),
            page(
                "talks/talk-one",
                "Secure Agents",
                "talks",
                "## Conference Context\n[[alice]]\n\n"
                "## Synthesis\n[[security]]\n\n"
                "## Connections\n[[evals]] [[bob]]\n",
            ),
            page("topics/security", "Agent Security", "topics", "[[talk-one]]"),
            page("topics/evals", "Agent Evaluations", "topics", "[[talk-one]]"),
        ]

        dataset = build_relationship_dataset(pages, self.profile)
        person_concepts = {
            item["target"]
            for item in dataset["relationships"]
            if item["template"] == "person_concept"
        }

        self.assertEqual({"topics/security"}, person_concepts)
        self.assertEqual(
            {"people/alice"},
            {
                item["source"]
                for item in dataset["relationships"]
                if item["template"] == "person_concept"
            },
        )
        self.assertFalse(
            any(
                item["template"] == "concept_concept"
                for item in dataset["relationships"]
            )
        )

    def test_schedule_speaker_and_reciprocal_affiliation_emit_reviewed_relationships(self):
        pages = [
            page("companies/acme", "Acme", "companies", "[[alice]]"),
            page("people/alice", "Alice", "people", "[[acme]]"),
            page(
                "talks/talk-one",
                "MCP in Production",
                "talks",
                "## Conference Context\n"
                "- Speaker(s): Alice\n\n"
                "## Synthesis\n"
                "### Topics Covered\n"
                "- [[mcp]]\n",
                {"speakers": ["Alice"]},
            ),
            page("topics/mcp", "Model Context Protocol", "topics"),
            page("tools/mcp", "Model Context Protocol", "tools"),
        ]

        dataset = build_relationship_dataset(pages, self.profile)
        endpoints = {
            (item["template"], item["source"], item["target"])
            for item in dataset["relationships"]
        }

        self.assertIn(
            ("person_concept", "people/alice", "topics/mcp"),
            endpoints,
        )
        self.assertIn(
            ("vendor_concept", "companies/acme", "topics/mcp"),
            endpoints,
        )
        self.assertFalse(any(target == "tools/mcp" for _, _, target in endpoints))
        vendor_relationship = next(
            item
            for item in dataset["relationships"]
            if item["template"] == "vendor_concept"
        )
        self.assertEqual(
            {
                "companies/acme": "curated_public_source",
                "people/alice": "curated_public_source",
                "talks/talk-one": "official_schedule",
            },
            {
                evidence["id"]: evidence["sourceLayer"]
                for evidence in vendor_relationship["evidence"]
            },
        )

    def test_conference_context_speaker_fallback_resolves_without_wikilink(self):
        pages = [
            page("people/alice", "Alice", "people"),
            page(
                "talks/talk-one",
                "Secure Agents",
                "talks",
                "## Conference Context\n"
                "- Speaker(s): Alice\n\n"
                "## Synthesis\n"
                "- [[security]]\n",
            ),
            page("topics/security", "Agent Security", "topics"),
        ]

        dataset = build_relationship_dataset(pages, self.profile)

        self.assertTrue(
            any(
                item["template"] == "person_concept"
                and item["source"] == "people/alice"
                and item["target"] == "topics/security"
                for item in dataset["relationships"]
            )
        )

    def test_schedule_name_ambiguity_and_one_sided_affiliation_fail_closed(self):
        pages = [
            page("companies/acme", "Acme", "companies"),
            page("people/alice-one", "Alice", "people", "[[acme]]"),
            page("people/alice-two", "Alice", "people"),
            page(
                "talks/talk-one",
                "Secure Agents",
                "talks",
                "## Conference Context\n"
                "- Speaker(s): Alice\n\n"
                "## Synthesis\n"
                "- [[security]]\n",
                {"speakers": ["Alice"]},
            ),
            page("topics/security", "Agent Security", "topics"),
        ]

        dataset = build_relationship_dataset(pages, self.profile)

        self.assertFalse(
            any(
                item["template"] in {"person_concept", "vendor_concept"}
                for item in dataset["relationships"]
            )
        )

    def test_unclassified_organization_is_review_only(self):
        dataset = self.build()
        audit = audit_dataset(dataset, self.profile)
        self.assertIn(
            {"type": "unclassified_organization", "id": "companies/ambiguous", "reason": "No explicit organization role is recorded."},
            audit["reviewCandidates"],
        )
        self.assertEqual([], audit["errors"])
        self.assertNotIn("audit", dataset)

    def test_output_is_deterministic_and_has_no_public_scoring_keys(self):
        first = self.build()
        second = build_relationship_dataset(reversed(self.pages), self.profile)
        self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))
        public = json.dumps(first).casefold()
        for forbidden in ("credibilityscore", "rankingscore", "internalscore", "calibration", "weight"):
            self.assertNotIn(forbidden, public)

    def test_repeated_endpoint_connections_keep_exact_evidence_paths(self):
        pages = self.pages + [
            page(
                "talks/talk-two",
                "Secure Agents Follow-up",
                "talks",
                "[[alice]] [[security]]",
            )
        ]
        dataset = build_relationship_dataset(pages, self.profile)
        records = [
            item
            for item in dataset["relationships"]
            if item["template"] == "person_concept"
            and item["source"] == "people/alice"
            and item["target"] == "topics/security"
        ]

        self.assertEqual(2, len(records))
        self.assertEqual(
            {"talks/talk-one", "talks/talk-two"},
            {item["evidence"][0]["id"] for item in records},
        )

    def test_schema_and_validator_accept_positive_fixture(self):
        dataset = self.build()
        schema_path = Path(__file__).resolve().parents[1] / "raw" / "sources" / "relationship-data.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator(schema).validate(dataset)
        self.assertEqual([], validate_dataset(dataset, self.profile))

    def test_validator_rejects_score_leak_and_missing_endpoint(self):
        dataset = self.build()
        dataset["internalScore"] = 0.9
        dataset["relationships"][0]["target"] = "topics/missing"
        dataset["relationships"][0]["publicReason"] = "Internal score calibration value: 0.9"
        errors = validate_dataset(dataset, self.profile)
        self.assertTrue(any("Forbidden internal" in error for error in errors))
        self.assertTrue(any("missing target" in error for error in errors))

    def test_cli_validates_existing_fixture(self):
        dataset = self.build()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "relationship-data.json"
            path.write_text(json.dumps(dataset), encoding="utf-8")
            profile_path = Path(directory) / "profile.json"
            profile_path.write_text(json.dumps(self.profile), encoding="utf-8")
            self.assertEqual(0, main(["--profile", str(profile_path), "--validate", str(path)]))

    def test_check_builds_without_writing_public_or_internal_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profile_path = root / "profile.json"
            output_path = root / "relationship-data.json"
            audit_path = root / "audit.json"
            profile_path.write_text(json.dumps(self.profile), encoding="utf-8")

            with patch.object(relationship_module, "ROOT", root), patch.object(
                relationship_module, "DEFAULT_INTERNAL_AUDIT", audit_path
            ), patch.object(relationship_module, "load_wiki_pages", return_value=self.pages), redirect_stdout(io.StringIO()):
                self.assertEqual(
                    0,
                    relationship_module.main(
                        ["--profile", str(profile_path), "--output", str(output_path), "--check"]
                    ),
                )

            self.assertFalse(output_path.exists())
            self.assertFalse(audit_path.exists())

    def test_check_rejects_internal_audit_write_before_generation(self):
        with patch.object(relationship_module, "load_profile") as generator, redirect_stderr(io.StringIO()), self.assertRaises(
            SystemExit
        ) as raised:
            relationship_module.main(["--check", "--write-internal-audit"])

        self.assertEqual(2, raised.exception.code)
        generator.assert_not_called()

    def test_help_and_unknown_arguments_do_not_build_relationships(self):
        for argv in (["--help"], ["--unknown"], ["--chec"]):
            with self.subTest(argv=argv), patch.object(relationship_module, "load_profile") as generator:
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    relationship_module.main(argv)
                generator.assert_not_called()


if __name__ == "__main__":
    unittest.main()
