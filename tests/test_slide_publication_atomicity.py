import argparse
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import classify_and_recreate_slides as classifier
from scripts import improve_slide_ocr_rapidmerge as rapidmerge
from scripts import process_slide_corpus_ai as corpus
from scripts import quarantine_stale_slide_ai as quarantine


def rapidmerge_args(**overrides):
    values = {
        "all": False,
        "limit": 0,
        "no_live_ocr": True,
        "engine": [],
        "enable_surya": False,
        "skip_perfect": True,
        "no_variants": True,
        "deep_variants": False,
        "variant_max_old_score": 50.0,
        "min_gain": 10_000.0,
        "log_manual_queue": False,
        "manual_score_threshold": 95.0,
        "internal_eval_log": False,
        "internal_eval_limit": 20,
        "backup": True,
        "progress": 0,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class SlidePublicationAtomicityTests(unittest.TestCase):
    def test_classifier_interruption_restores_old_set_and_withholds_page(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            recreations = root / "wiki/assets/slide-recreations"
            classifications = root / "raw/sources/slide-ai-classification"
            pages = root / "wiki/slides"
            live = recreations / "dense/video-1"
            live.mkdir(parents=True)
            old_asset = live / "slide-001.html"
            old_asset.write_bytes(b"old recreation\n")
            audit_path = classifications / "dense/video-1/audit.json"
            audit_path.parent.mkdir(parents=True)
            old_audit = b'{"old": true}\n'
            audit_path.write_bytes(old_audit)
            page = pages / "youtube-video-1-dense-slides.md"
            page.parent.mkdir(parents=True)
            page.write_text(
                "# Deck\n\n## Cropped Visible Slides\n"
                "- AI slide classifier: `content_slide` confidence `0.9`\n"
                "- [open HTML recreation](/assets/slide-recreations/dense/"
                "video-1/slide-001.html)\n\n"
                "Classification audit: `raw/sources/slide-ai-classification/"
                "dense/video-1/audit.json`\n",
                encoding="utf-8",
            )
            args = argparse.Namespace(deck_kind="dense")
            output_data = b"new recreation\n"
            record = {"recreation": str(old_asset)}

            with patch.object(classifier, "ROOT", root):
                classifier.bind_recreation_output(record, old_asset, output_data)
                manifest = classifier.recreation_manifest([record])
            audit = {
                "publication_schema_version": classifier.PUBLICATION_SCHEMA_VERSION,
                "publication_status": "succeeded",
                "accepted": [record],
                "recreation_manifest": manifest,
                "recreation_manifest_sha256": classifier._manifest_sha256(manifest),
            }
            calls = 0
            original_validate = classifier.validate_recreation_publication

            def fail_after_directory_swap(*args_, **kwargs):
                nonlocal calls
                calls += 1
                if calls == 3:
                    raise RuntimeError("simulated interruption")
                return original_validate(*args_, **kwargs)

            deck = {
                "asset_dir": root / "unused",
                "ocr_dir": root / "unused-ocr",
                "page_suffix": "dense-slides",
                "visible_heading": "Cropped Visible Slides",
            }
            with (
                patch.object(classifier, "ROOT", root),
                patch.object(classifier, "RECREATION_ASSETS", recreations),
                patch.object(classifier, "CLASSIFICATION_ROOT", classifications),
                patch.object(classifier, "SLIDE_PAGES", pages),
                patch.dict(classifier.DECKS, {"dense": deck}, clear=True),
                patch.object(
                    classifier,
                    "validate_recreation_publication",
                    side_effect=fail_after_directory_swap,
                ),
                self.assertRaisesRegex(RuntimeError, "simulated interruption"),
            ):
                classifier.publish_classification(
                    "video-1",
                    audit,
                    [(old_asset, output_data)],
                    args,
                    (page, "# Deck\n\n## Cropped Visible Slides\nnew public view\n"),
                )

            self.assertEqual(b"old recreation\n", old_asset.read_bytes())
            self.assertEqual(old_audit, audit_path.read_bytes())
            page_text = page.read_text(encoding="utf-8")
            self.assertIn(classifier.PUBLICATION_PENDING_MARKER, page_text)
            self.assertNotIn("new public view", page_text)

    def test_quarantine_rejects_tampered_recreation_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            recreations = root / "wiki/assets/slide-recreations"
            classifications = root / "raw/sources/slide-ai-classification"
            image = root / "wiki/assets/dense-slides/video-1/slide-001.jpg"
            recreation = recreations / "dense/video-1/slide-001.html"
            image.parent.mkdir(parents=True)
            recreation.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            recreation.write_bytes(b"bound recreation\n")
            digest = hashlib.sha256(recreation.read_bytes()).hexdigest()
            record = {
                "image": str(image),
                "recreation": str(recreation),
                "recreation_sha256": digest,
                "recreation_size_bytes": recreation.stat().st_size,
            }
            manifest = [
                {
                    "path": str(recreation.relative_to(root)),
                    "sha256": digest,
                    "size_bytes": recreation.stat().st_size,
                }
            ]
            audit = {
                "publication_schema_version": 1,
                "publication_status": "succeeded",
                "accepted": [record],
                "rejected": [],
                "recreation_manifest": manifest,
                "recreation_manifest_sha256": hashlib.sha256(
                    json.dumps(
                        manifest, separators=(",", ":"), sort_keys=True
                    ).encode()
                ).hexdigest(),
            }
            audit_path = classifications / "dense/video-1/audit.json"
            audit_path.parent.mkdir(parents=True)
            audit_path.write_text(json.dumps(audit), encoding="utf-8")

            with (
                patch.object(quarantine, "ROOT", root),
                patch.object(quarantine, "RECREATION_ROOT", recreations),
                patch.object(corpus, "audit_path", return_value=audit_path),
            ):
                self.assertEqual(
                    [], quarantine.recreation_contract_violations("dense", "video-1")
                )
                recreation.write_bytes(b"tampered\n")
                violations = quarantine.recreation_contract_violations(
                    "dense", "video-1"
                )

            self.assertIn(
                "recreation_asset_digest_mismatch:slide-001.html", violations
            )

    def test_operator_verified_text_is_absolute_and_forces_update(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slides = root / "wiki/assets/slides"
            canonical = root / "raw/sources/slide-ocr"
            operator = root / "raw/sources/slide-ocr-operator-verified"
            merged = root / "raw/sources/slide-ocr-rapidmerge"
            image = slides / "video-1/slide-001.jpg"
            canonical_path = canonical / "video-1/slide-001.txt"
            operator_path = operator / "video-1/slide-001.txt"
            image.parent.mkdir(parents=True)
            canonical_path.parent.mkdir(parents=True)
            operator_path.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            canonical_path.write_text(
                " ".join(f"baseline{i}" for i in range(40)) + "\n",
                encoding="utf-8",
            )
            operator_path.write_text("Correct title\n", encoding="utf-8")
            audit_path = root / "raw/sources/rapidmerge-audit.json"

            with (
                patch.object(rapidmerge, "ROOT", root),
                patch.object(rapidmerge, "SLIDE_ASSETS", slides),
                patch.object(rapidmerge, "CANONICAL_OCR", canonical),
                patch.object(rapidmerge, "MERGED_OCR", merged),
                patch.object(rapidmerge, "AUDIT_PATH", audit_path),
                patch.object(rapidmerge, "AUDIT_PAGE", root / "audit.md"),
                patch.object(
                    rapidmerge,
                    "PROVENANCE_REPAIR_SUMMARY",
                    root / "missing-repair.json",
                ),
                patch.object(
                    rapidmerge,
                    "RECOVERY_ROOT",
                    root / ".ops/state/cache/recovery",
                ),
                patch.object(
                    rapidmerge,
                    "SOURCE_DIRS",
                    [("operator-verified", operator), ("canonical", canonical)],
                ),
            ):
                rapidmerge.improve(rapidmerge_args())

            self.assertEqual("Correct title\n", canonical_path.read_text())
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            self.assertEqual("operator-verified", audit["records"][0]["bestSource"])
            self.assertTrue(audit["records"][0]["updatedCanonical"])
            receipt = json.loads(
                (merged / "video-1/slide-001.receipt.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual("committed", receipt["status"])

    def test_ai_candidate_carries_complete_validated_receipt_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide = root / "wiki/assets/slides/video-1/slide-001.jpg"
            canonical = root / "canonical"
            vision = root / "vision"
            slide.parent.mkdir(parents=True)
            slide.write_bytes(b"image")
            canonical_text = "baseline OCR"
            vision_text = "receipt bound output"
            canonical_path = canonical / "video-1/slide-001.txt"
            output = vision / "video-1/slide-001.txt"
            canonical_path.parent.mkdir(parents=True)
            output.parent.mkdir(parents=True)
            canonical_path.write_text(canonical_text, encoding="utf-8")
            output.write_text(vision_text, encoding="utf-8")
            receipt = {
                "schemaVersion": rapidmerge.AI_VISION_CACHE_SCHEMA_VERSION,
                "status": "accepted",
                "imageSha256": hashlib.sha256(b"image").hexdigest(),
                "ocrSha256": hashlib.sha256(canonical_text.encode()).hexdigest(),
                "provider": "codex-cli",
                "model": "vision-test",
                "promptContractVersion": rapidmerge.AI_VISION_PROMPT_CONTRACT_VERSION,
                "promptContractSha256": rapidmerge.AI_VISION_PROMPT_CONTRACT_SHA256,
                "minimumAcceptedConfidence": rapidmerge.AI_VISION_MIN_ACCEPTED_CONFIDENCE,
                "confidence": 0.9,
                "textSha256": hashlib.sha256(vision_text.encode()).hexdigest(),
                "writtenAtEpoch": 1.0,
            }
            receipt_path = output.with_suffix(".receipt.json")
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

            with (
                patch.object(rapidmerge, "ROOT", root),
                patch.object(rapidmerge, "CANONICAL_OCR", canonical),
            ):
                candidate = rapidmerge.read_candidate("ai-vision", vision, slide)

            self.assertIsNotNone(candidate)
            provenance = candidate.provenance
            self.assertEqual(receipt["imageSha256"], provenance["imageSha256"])
            self.assertEqual(receipt["ocrSha256"], provenance["inputOcrSha256"])
            self.assertEqual(receipt["textSha256"], provenance["outputTextSha256"])
            self.assertEqual(receipt["model"], provenance["model"])
            self.assertEqual(
                hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
                provenance["receiptSha256"],
            )

            audit_path = root / "raw/sources/rapidmerge-audit.json"
            merged = root / "raw/sources/slide-ocr-rapidmerge"
            with (
                patch.object(rapidmerge, "ROOT", root),
                patch.object(
                    rapidmerge,
                    "SLIDE_ASSETS",
                    root / "wiki/assets/slides",
                ),
                patch.object(rapidmerge, "CANONICAL_OCR", canonical),
                patch.object(rapidmerge, "MERGED_OCR", merged),
                patch.object(rapidmerge, "AUDIT_PATH", audit_path),
                patch.object(rapidmerge, "AUDIT_PAGE", root / "audit.md"),
                patch.object(
                    rapidmerge,
                    "PROVENANCE_REPAIR_SUMMARY",
                    root / "missing-repair.json",
                ),
                patch.object(
                    rapidmerge,
                    "RECOVERY_ROOT",
                    root / ".ops/state/cache/recovery",
                ),
                patch.object(
                    rapidmerge,
                    "SOURCE_DIRS",
                    [("ai-vision", vision), ("canonical", canonical)],
                ),
            ):
                rapidmerge.improve(
                    rapidmerge_args(all=True, skip_perfect=False, min_gain=0)
                )

            decision = json.loads(audit_path.read_text(encoding="utf-8"))[
                "records"
            ][0]
            self.assertEqual(provenance, decision["aiVisionProvenance"])
            self.assertEqual(
                provenance["receiptSha256"],
                decision["decisionInputs"]["aiVisionReceiptSha256"],
            )
            self.assertEqual(
                provenance["inputOcrSha256"],
                decision["decisionInputs"]["aiVisionInputOcrSha256"],
            )

    def test_incomplete_rapidmerge_publication_rolls_back_exact_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slides = root / "wiki/assets/slides"
            canonical = root / "raw/sources/slide-ocr"
            merged = root / "raw/sources/slide-ocr-rapidmerge"
            recovery = root / ".ops/state/cache/recovery"
            audit_path = root / "raw/sources/rapidmerge-audit.json"
            slide = slides / "video-1/slide-001.jpg"
            canonical_path = canonical / "video-1/slide-001.txt"
            receipt_path = merged / "video-1/slide-001.receipt.json"
            backup = recovery / "run-1/video-1/slide-001.txt"
            old_bytes = b"old exact bytes  \n\n"
            new_bytes = b"new bytes\n"
            slide.parent.mkdir(parents=True)
            canonical_path.parent.mkdir(parents=True)
            receipt_path.parent.mkdir(parents=True)
            backup.parent.mkdir(parents=True)
            slide.write_bytes(b"image")
            canonical_path.write_bytes(new_bytes)
            backup.write_bytes(old_bytes)
            receipt_path.write_text(
                json.dumps({"runId": "run-1", "status": "prepared"}),
                encoding="utf-8",
            )
            audit = {
                "publicationSchemaVersion": 1,
                "status": "publishing",
                "runId": "run-1",
                "records": [
                    {
                        "videoId": "video-1",
                        "slide": "slide-001.jpg",
                        "updatedCanonicalPlanned": True,
                        "previousCanonicalExisted": True,
                        "previousCanonicalSha256": hashlib.sha256(old_bytes).hexdigest(),
                        "replacementCanonicalSha256": hashlib.sha256(new_bytes).hexdigest(),
                    }
                ],
            }
            audit_path.parent.mkdir(parents=True, exist_ok=True)
            audit_path.write_text(json.dumps(audit), encoding="utf-8")

            with (
                patch.object(rapidmerge, "ROOT", root),
                patch.object(rapidmerge, "SLIDE_ASSETS", slides),
                patch.object(rapidmerge, "CANONICAL_OCR", canonical),
                patch.object(rapidmerge, "MERGED_OCR", merged),
                patch.object(rapidmerge, "RECOVERY_ROOT", recovery),
                patch.object(rapidmerge, "AUDIT_PATH", audit_path),
            ):
                recovered = rapidmerge.recover_incomplete_publication()

            self.assertEqual(old_bytes, canonical_path.read_bytes())
            self.assertEqual("rolled_back", recovered["status"])
            self.assertEqual(
                "rolled_back",
                json.loads(receipt_path.read_text(encoding="utf-8"))["status"],
            )

    def test_classifier_status_page_must_match_current_contract_and_counts(self):
        with tempfile.TemporaryDirectory() as directory:
            note = Path(directory) / "slide-ai-classifier-status.md"
            private_report = Path(directory) / "private/classifier-scan.json"
            note.write_text("stale v4 report\n", encoding="utf-8")
            report = {
                "contract": {
                    "policy_version": "private-policy-v5",
                    "cache_schema_version": 73,
                    "prompt_contract_sha256": "a" * 64,
                    "model": "private-model-id",
                    "min_confidence": 0.731234,
                },
                "audits": {
                    "total": 1,
                    "current": 0,
                    "stale": 1,
                    "policy_versions": {"v4": 1},
                    "stale_recreation_records": 2,
                },
                "pages": {
                    "current_sections": 0,
                    "withheld_sections": 1,
                    "stale_sections": [],
                },
                "recreations": {"current_assets": 0, "stale_assets": []},
                "status_page": {"violations": []},
            }
            with (
                patch.object(quarantine, "RESOURCE_NOTE", note),
                patch.object(quarantine, "PRIVATE_REPORT_JSON", private_report),
            ):
                self.assertEqual(
                    ["classifier_status_page_stale_or_unbound"],
                    quarantine.status_page_violations(report),
                )
                quarantine.write_resource_note(report, quarantined_assets=3)
                self.assertEqual([], quarantine.status_page_violations(report))
                quarantine.write_private_report(report)

            public = note.read_text(encoding="utf-8")
            for private_value in (
                "private-policy-v5",
                "73",
                "a" * 64,
                "private-model-id",
                "0.731234",
                "v4",
            ):
                self.assertNotIn(private_value, public)
            self.assertNotIn("prompt contract SHA", public)
            self.assertNotIn("minimum confidence", public.lower())

            console = json.dumps(quarantine.concise(report), sort_keys=True)
            for private_value in (
                "private-policy-v5",
                "a" * 64,
                "private-model-id",
                "0.731234",
                "v4",
            ):
                self.assertNotIn(private_value, console)

            private = json.loads(private_report.read_text(encoding="utf-8"))
            self.assertEqual(report, private["report"])
            self.assertEqual("private-policy-v5", private["report"]["contract"]["policy_version"])
            self.assertEqual("a" * 64, private["report"]["contract"]["prompt_contract_sha256"])
            self.assertEqual(0.731234, private["report"]["contract"]["min_confidence"])


if __name__ == "__main__":
    unittest.main()
