import argparse
import hashlib
import importlib.util
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from scripts import classify_and_recreate_slides as classifier
from scripts import improve_slide_ocr_rapidmerge as rapidmerge
from scripts import monitor_official_youtube as monitor
from scripts import process_slide_corpus_ai as process_corpus
from scripts import repair_unreceipted_ai_vision_ocr as ocr_repair


VISION_SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "interpret_slide_text_with_vision.py"
)
VISION_DEPENDENCY = types.ModuleType("improve_slide_ocr_rapidmerge")
VISION_DEPENDENCY.AUDIT_PATH = Path("/nonexistent-rapidmerge-audit.json")
VISION_DEPENDENCY.PROVENANCE_REPAIR_SUMMARY = Path(
    "/nonexistent-provenance-repair-summary.json"
)
VISION_DEPENDENCY.Candidate = object
VISION_DEPENDENCY.is_weak = lambda _text: True
VISION_DEPENDENCY.text_path = (
    lambda base, slide: base / slide.parent.name / f"{slide.stem}.txt"
)


def _write_fixture_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


VISION_DEPENDENCY.write_text = _write_fixture_text
VISION_SPEC = importlib.util.spec_from_file_location(
    "interpret_slide_text_hardening_test", VISION_SCRIPT
)
VISION = importlib.util.module_from_spec(VISION_SPEC)
assert VISION_SPEC.loader
with patch.dict(sys.modules, {"improve_slide_ocr_rapidmerge": VISION_DEPENDENCY}):
    VISION_SPEC.loader.exec_module(VISION)


def video(
    video_id: str, published: str, title: str = "Reliable Agents by Ada Example"
) -> monitor.VideoEntry:
    return monitor.VideoEntry(
        video_id=video_id,
        title=title,
        published=f"{published}T12:00:00+00:00",
        updated=f"{published}T12:00:00+00:00",
        url=f"https://www.youtube.com/watch?v={video_id}",
        channel_id=monitor.CHANNEL_ID,
        availability="public",
    )


TALK = {
    "id": "2026-06-29-ada-example-reliable-agents",
    "title": "Reliable Agents",
    "speakers": json.dumps(["Ada Example"]),
    "description": "",
    "text": "",
}


def vision_args(**overrides):
    values = {
        "skip_existing": True,
        "min_confidence": 0.72,
        "openai_model": "vision-test",
        "codex_model": "codex-test",
        "ollama_model": "ollama-test",
        "timeout": 30,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def classifier_args(**overrides):
    values = {
        "model": "classifier-test",
        "deck_kind": "slides",
        "no_advanced_ocr": True,
        "no_ocr_reconcile": True,
        "ocr_engine": [],
        "ocr_max_suspicious_ratio": 0.08,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def corpus_args(**overrides):
    values = {
        "model": "classifier-test",
        "min_confidence": 0.72,
        "ocr_max_suspicious_ratio": 0.08,
        "no_ocr_reconcile": False,
        "no_advanced_ocr": False,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class MediaIngestHardeningTests(unittest.TestCase):
    def test_non_playlist_matching_rejects_recycled_wrong_year_upload(self):
        old = video("old-video", "2025-07-15")
        current = video("current-video", "2026-07-15")

        self.assertEqual([], monitor.event_entries([old], [TALK]))
        self.assertEqual([(current, [TALK])], monitor.event_entries([current], [TALK]))

    def test_delayed_explicit_wf26_title_is_admitted_without_schedule_inference(self):
        delayed = video(
            "delayed-video",
            "2027-02-10",
            "WF26: Agent Systems Talk Recording",
        )

        self.assertEqual([(delayed, [])], monitor.event_entries([delayed], []))
        self.assertTrue(monitor.non_playlist_media_date_allowed(delayed))

    def test_explicit_wf26_title_cannot_override_a_conflicting_event_year(self):
        conflicting = video(
            "conflicting-video",
            "2026-07-15",
            "WF26: Highlights from AI Engineer World's Fair 2025",
        )

        self.assertFalse(monitor.non_playlist_media_date_allowed(conflicting))
        self.assertEqual([], monitor.event_entries([conflicting], []))

    def test_playlist_membership_remains_admissible_outside_non_playlist_window(self):
        old = video("playlist-old", "2025-07-15")
        entry = monitor.PlaylistEntry(
            video_id=old.video_id,
            playlist_index=1,
            playlist_title=old.title,
            availability="public",
            video=old,
            matched_talks=(TALK,),
        )
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "official-videos.json"
            manifest.write_text('{"schemaVersion": 1, "videos": []}', encoding="utf-8")
            with patch.object(monitor, "OFFICIAL_VIDEO_MANIFEST", manifest):
                changed = monitor.update_official_video_manifest([], playlist_entries=[entry])
            payload = json.loads(manifest.read_text(encoding="utf-8"))

        self.assertTrue(changed)
        self.assertEqual(["playlist-old"], [item["id"] for item in payload["videos"]])
        self.assertEqual(
            "official_wf26_playlist_membership",
            payload["videos"][0]["associationEvidence"],
        )

    def test_vision_cache_is_bound_to_image_ocr_provider_model_and_prompt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide = root / "wiki" / "assets" / "slides" / "video-1" / "slide-001.jpg"
            canonical = root / "canonical"
            output = root / "vision"
            slide.parent.mkdir(parents=True)
            slide.write_bytes(b"image-v1")
            _write_fixture_text(canonical / "video-1" / "slide-001.txt", "old OCR")
            args = vision_args()

            with patch.object(VISION, "ROOT", root), patch.object(
                VISION, "CANONICAL_OCR", canonical
            ), patch.object(VISION, "AI_VISION_OCR", output), patch.object(
                VISION,
                "interpret",
                return_value={"text": "verified text", "confidence": 0.9, "notes": "read"},
            ) as interpret:
                first = VISION.process_slide("openai", slide, args)
                second = VISION.process_slide("openai", slide, args)
                slide.write_bytes(b"image-v2")
                third = VISION.process_slide("openai", slide, args)
                receipt_path = VISION.cache_receipt_path(slide)

            self.assertEqual(2, interpret.call_count)
            self.assertFalse(first.get("skippedExisting", False))
            self.assertTrue(second["skippedExisting"])
            self.assertFalse(third.get("skippedExisting", False))
            self.assertTrue(receipt_path.is_file())

    def test_vision_failure_cannot_leave_an_unreceipted_success_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide = root / "wiki" / "assets" / "slides" / "video-1" / "slide-001.jpg"
            output = root / "vision"
            slide.parent.mkdir(parents=True)
            slide.write_bytes(b"image")
            stale = output / "video-1" / "slide-001.txt"
            _write_fixture_text(stale, "unverified stale text")

            with patch.object(VISION, "ROOT", root), patch.object(
                VISION, "CANONICAL_OCR", root / "canonical"
            ), patch.object(VISION, "AI_VISION_OCR", output), patch.object(
                VISION, "interpret", side_effect=RuntimeError("provider failed")
            ):
                record = VISION.process_slide("openai", slide, vision_args())

            self.assertIn("provider failed", record["error"])
            self.assertFalse(stale.exists())
            self.assertFalse(VISION.cache_receipt_path(slide).exists())

    def test_rapidmerge_rejects_unreceipted_or_stale_ai_vision_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide = root / "wiki" / "assets" / "slides" / "video-1" / "slide-001.jpg"
            canonical = root / "canonical"
            vision = root / "vision"
            slide.parent.mkdir(parents=True)
            slide.write_bytes(b"image-v1")
            canonical_text = "baseline OCR"
            vision_text = "receipt-bound vision text"
            _write_fixture_text(canonical / "video-1" / "slide-001.txt", canonical_text)
            output = vision / "video-1" / "slide-001.txt"
            _write_fixture_text(output, vision_text)

            with patch.object(rapidmerge, "CANONICAL_OCR", canonical):
                self.assertIsNone(rapidmerge.read_candidate("ai-vision", vision, slide))
                receipt = {
                    "schemaVersion": rapidmerge.AI_VISION_CACHE_SCHEMA_VERSION,
                    "status": "accepted",
                    "imageSha256": hashlib.sha256(b"image-v1").hexdigest(),
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
                output.with_suffix(".receipt.json").write_text(
                    json.dumps(receipt), encoding="utf-8"
                )
                accepted = rapidmerge.read_candidate("ai-vision", vision, slide)
                self.assertIsNotNone(accepted)
                self.assertEqual(vision_text, accepted.text)

                slide.write_bytes(b"image-v2")
                self.assertIsNone(rapidmerge.read_candidate("ai-vision", vision, slide))

    def test_historical_ocr_repair_only_accepts_exact_unreceipted_copies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "wiki" / "assets" / "slides" / "video-1" / "slide-001.jpg"
            canonical = root / "canonical"
            vision = root / "vision"
            backup = root / "backup"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            _write_fixture_text(canonical / "video-1" / "slide-001.txt", "unverified text")
            _write_fixture_text(vision / "video-1" / "slide-001.txt", "unverified text")
            _write_fixture_text(backup / "video-1" / "slide-001.txt", "prior OCR")
            row = {
                "image": str(image.relative_to(root)),
                "bestSource": "ai-vision",
                "updatedCanonical": True,
            }

            with patch.object(ocr_repair, "ROOT", root), patch.object(
                ocr_repair, "CANONICAL_OCR", canonical
            ), patch.object(ocr_repair, "AI_VISION_OCR", vision), patch.object(
                ocr_repair, "PRE_MERGE_OCR", backup
            ):
                self.assertEqual(
                    "repairable_unreceipted_copy", ocr_repair.inspect_row(row)["status"]
                )
                _write_fixture_text(
                    canonical / "video-1" / "slide-001.txt", "operator correction"
                )
                self.assertEqual(
                    "canonical_already_diverged", ocr_repair.inspect_row(row)["status"]
                )
                (backup / "video-1" / "slide-001.txt").unlink()
                self.assertEqual(
                    "canonical_already_diverged", ocr_repair.inspect_row(row)["status"]
                )

    def test_historical_ocr_repair_restores_original_backup_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "wiki/assets/slides/video-1/slide-001.jpg"
            canonical = root / "canonical/video-1/slide-001.txt"
            vision = root / "vision/video-1/slide-001.txt"
            backup = root / "backup/video-1/slide-001.txt"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            original = b"Heading  \n\nValue , with spacing\n"
            _write_fixture_text(vision, "unverified AI text")
            backup.parent.mkdir(parents=True)
            backup.write_bytes(original)
            _write_fixture_text(canonical, ocr_repair.normalize_text(original.decode()))
            row = {
                "image": str(image.relative_to(root)),
                "bestSource": "ai-vision",
                "updatedCanonical": True,
            }
            with patch.object(ocr_repair, "ROOT", root), patch.object(
                ocr_repair, "CANONICAL_OCR", root / "canonical"
            ), patch.object(ocr_repair, "AI_VISION_OCR", root / "vision"), patch.object(
                ocr_repair, "PRE_MERGE_OCR", root / "backup"
            ):
                self.assertEqual(
                    "normalized_restore_needs_exact_backup",
                    ocr_repair.inspect_row(row)["status"],
                )
                ocr_repair.atomic_restore(canonical, backup.read_bytes())
                self.assertEqual(
                    "restored_from_pre_merge_backup",
                    ocr_repair.inspect_row(row)["status"],
                )
            self.assertEqual(original, canonical.read_bytes())

    def test_historical_ocr_repair_does_not_trust_summary_without_backup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "wiki/assets/slides/video-1/slide-001.jpg"
            canonical = root / "canonical/video-1/slide-001.txt"
            vision = root / "vision/video-1/slide-001.txt"
            summary = root / "summary.json"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            _write_fixture_text(canonical, "same historical text")
            _write_fixture_text(vision, "same historical text")
            summary.write_text(
                json.dumps(
                    {
                        "verifiedEqualWithoutBackup": [
                            {
                                "canonicalPath": "canonical/video-1/slide-001.txt",
                                "canonicalSha256": hashlib.sha256(
                                    canonical.read_bytes()
                                ).hexdigest(),
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            row = {
                "image": str(image.relative_to(root)),
                "bestSource": "ai-vision",
                "updatedCanonical": True,
            }
            with patch.object(ocr_repair, "ROOT", root), patch.object(
                ocr_repair, "PUBLIC_SUMMARY", summary
            ), patch.object(
                ocr_repair, "CANONICAL_OCR", root / "canonical"
            ), patch.object(ocr_repair, "AI_VISION_OCR", root / "vision"), patch.object(
                ocr_repair, "PRE_MERGE_OCR", root / "missing-backup"
            ):
                self.assertEqual(
                    "missing_pre_merge_backup",
                    ocr_repair.inspect_row(row)["status"],
                )

    def test_historical_ocr_summary_keeps_restore_and_noop_counts_separate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            audit = root / "raw/sources/slide-ocr-rapidmerge-audit.json"
            summary = root / "raw/sources/slide-ocr-provenance-repair-summary.json"
            audit.parent.mkdir(parents=True)
            audit.write_text('{"records": []}', encoding="utf-8")
            rows = [
                {"status": "restored_from_pre_merge_backup"} for _ in range(599)
            ] + [
                {"status": "already_matches_pre_merge_backup"} for _ in range(2)
            ]
            with patch.object(ocr_repair, "ROOT", root), patch.object(
                ocr_repair, "AUDIT_PATH", audit
            ), patch.object(ocr_repair, "PUBLIC_SUMMARY", summary):
                ocr_repair.write_public_summary(
                    now=ocr_repair.datetime(2026, 7, 17, tzinfo=ocr_repair.timezone.utc),
                    postcheck=rows,
                )
                first = json.loads(summary.read_text(encoding="utf-8"))
                ocr_repair.write_public_summary(
                    now=ocr_repair.datetime(2026, 7, 18, tzinfo=ocr_repair.timezone.utc),
                    postcheck=rows,
                )
                second = json.loads(summary.read_text(encoding="utf-8"))

            for payload in (first, second):
                self.assertEqual(601, payload["historicalUnreceiptedAiVisionUpdates"])
                self.assertEqual(599, payload["restoredFromBackupFiles"])
                self.assertEqual(599, payload["restoredCanonicalFiles"])
                self.assertEqual(2, payload["alreadyMatchedBackupFiles"])
                self.assertEqual(0, payload["historicalAiVisionAuditRecordedReceipts"])
                self.assertEqual(
                    0, payload["historicalAiVisionUpdatesAcceptedByCurrentPolicy"]
                )
                self.assertNotIn("verifiedEqualWithoutBackup", payload)

    def test_public_rapidmerge_audit_marks_historical_ai_run_superseded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "audit.md"
            summary = root / "repair.json"
            audit_path = root / "audit.json"
            audit = {
                "records": [],
                "canonicalUpdated": 601,
                "engineStatus": {},
            }
            audit_path.write_text(json.dumps(audit), encoding="utf-8")
            summary.write_text(
                json.dumps(
                    {
                        "historicalAuditSuperseded": True,
                        "sourceAuditSha256": hashlib.sha256(
                            audit_path.read_bytes()
                        ).hexdigest(),
                        "restoredCanonicalFiles": 599,
                        "restoredFromBackupFiles": 599,
                        "alreadyMatchedBackupFiles": 2,
                        "remainingExactUnreceiptedCopies": 0,
                        "ambiguousRecords": 0,
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(rapidmerge, "AUDIT_PATH", audit_path), patch.object(
                rapidmerge, "AUDIT_PAGE", page
            ), patch.object(
                rapidmerge, "PROVENANCE_REPAIR_SUMMARY", summary
            ):
                rapidmerge.write_audit_page(audit)

            rendered = page.read_text(encoding="utf-8")
            self.assertIn("## Provenance Repair", rendered)
            self.assertIn("restored 599 canonical OCR files", rendered)
            self.assertIn("Historical RapidMerge Run (Superseded)", rendered)
            self.assertIn("not current trusted evidence", rendered)

            summary.write_text(
                json.dumps(
                    {
                        "historicalAuditSuperseded": True,
                        "sourceAuditSha256": "stale",
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(rapidmerge, "AUDIT_PATH", audit_path), patch.object(
                rapidmerge, "AUDIT_PAGE", page
            ), patch.object(rapidmerge, "PROVENANCE_REPAIR_SUMMARY", summary):
                rapidmerge.write_audit_page(audit)
            self.assertIn("## Latest Run", page.read_text(encoding="utf-8"))
            self.assertNotIn("## Provenance Repair", page.read_text(encoding="utf-8"))

    def test_public_ocr_audits_mark_historical_ai_cache_untrusted(self):
        root = Path(__file__).resolve().parents[1]
        rapidmerge_page = (
            root / "wiki/resources/slide-ocr-rapidmerge-audit.md"
        ).read_text(encoding="utf-8")
        ai_vision_page = (
            root / "wiki/resources/slide-ocr-ai-vision-audit.md"
        ).read_text(encoding="utf-8")
        classifier_status = (
            root / "wiki/resources/slide-ai-classifier-status.md"
        ).read_text(encoding="utf-8")

        self.assertIn("restored 599 files", rapidmerge_page)
        self.assertIn("other 2 files already matched", rapidmerge_page)
        self.assertIn("current RapidMerge policy accepts 0", rapidmerge_page)
        self.assertIn("## Current Trust Status", ai_vision_page)
        self.assertIn("Current provenance receipts recorded", ai_vision_page)
        self.assertIn("accepted by current RapidMerge policy: 0", ai_vision_page)
        self.assertNotIn("Minimum confidence", ai_vision_page)
        self.assertNotIn("below operator-verified", ai_vision_page)
        for private_value in (
            classifier.POLICY_VERSION,
            classifier.PROMPT_CONTRACT_SHA256,
            classifier.DEFAULT_CODEX_MODEL,
            str(classifier.MIN_CLASSIFICATION_CONFIDENCE),
        ):
            self.assertNotIn(private_value, classifier_status)
        self.assertNotIn("Required cache schema", classifier_status)
        self.assertNotIn("prompt contract SHA", classifier_status)
        self.assertNotIn("minimum confidence", classifier_status.lower())

    def test_ai_vision_writer_preserves_superseded_trust_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "vision.md"
            summary = root / "repair.json"
            audit_path = root / "rapidmerge.json"
            audit_path.write_text("{}", encoding="utf-8")
            summary.write_text(
                json.dumps(
                    {
                        "historicalAuditSuperseded": True,
                        "sourceAuditSha256": hashlib.sha256(
                            audit_path.read_bytes()
                        ).hexdigest(),
                        "historicalUnreceiptedAiVisionUpdates": 601,
                        "restoredCanonicalFiles": 599,
                        "alreadyMatchedBackupFiles": 2,
                        "historicalAiVisionAuditRecordedReceipts": 0,
                        "historicalAiVisionUpdatesAcceptedByCurrentPolicy": 0,
                    }
                ),
                encoding="utf-8",
            )
            audit = {
                "provider": "codex-cli",
                "model": "allowed-provenance-model",
                "minConfidence": 0.731234,
                "records": [{"written": "old.txt"}],
                "visionFilesAvailable": 1,
            }
            with patch.object(VISION, "AUDIT_PATH", audit_path), patch.object(
                VISION, "PROVENANCE_REPAIR_SUMMARY", summary
            ), patch.object(VISION, "AI_VISION_PAGE", page):
                VISION.write_audit_page(audit)

            rendered = page.read_text(encoding="utf-8")
            self.assertIn("## Current Trust Status", rendered)
            self.assertIn("affected: 601", rendered)
            self.assertIn("accepted by current RapidMerge policy: 0", rendered)
            self.assertIn("Historical AI Vision Run (Superseded)", rendered)
            self.assertIn("Model: allowed-provenance-model", rendered)
            self.assertNotIn("Minimum confidence", rendered)
            self.assertNotIn("0.731234", rendered)
            self.assertNotIn("below operator-verified", rendered)

    def test_classifier_cache_rejects_changed_image_model_and_failed_status(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slide = root / "wiki" / "assets" / "slides" / "video-1" / "slide-001.jpg"
            cache = root / "result.json"
            slide.parent.mkdir(parents=True)
            slide.write_bytes(b"image-v1")
            args = classifier_args()
            result = {
                "is_content_slide": True,
                "confidence": 0.9,
                "frame_type": "content_slide",
                "text": "visible",
                "ocr_ready": False,
            }
            classifier.bind_cache_provenance(result, slide, args)
            cache.write_text(json.dumps(result), encoding="utf-8")

            self.assertIsNotNone(classifier.cached_result(cache, slide, args))
            self.assertIsNone(
                classifier.cached_result(cache, slide, classifier_args(model="other-model"))
            )
            slide.write_bytes(b"image-v2")
            self.assertIsNone(classifier.cached_result(cache, slide, args))
            slide.write_bytes(b"image-v1")
            result["cache_status"] = "failed"
            cache.write_text(json.dumps(result), encoding="utf-8")
            self.assertIsNone(classifier.cached_result(cache, slide, args))

    def test_fresh_model_outputs_reject_invalid_confidence(self):
        for value in ("NaN", "Infinity", 1.2, -0.1, True):
            payload = json.dumps({"confidence": value})
            with self.assertRaisesRegex(ValueError, "confidence"):
                classifier.parse_json(payload)
            with self.assertRaisesRegex(ValueError, "confidence"):
                VISION.parse_json(payload)

    def test_classifier_requires_literal_json_booleans(self):
        base = {
            "confidence": 0.9,
            "is_content_slide": True,
            "ocr_ready": False,
            "direct_read_ready": False,
        }
        for field in ("is_content_slide", "ocr_ready", "direct_read_ready"):
            with self.assertRaisesRegex(ValueError, "non-boolean"):
                classifier.parse_json(json.dumps({**base, field: "false"}))

    def test_classifier_rejects_unsafe_thresholds_and_empty_requested_deck(self):
        for value in (-1, 0.71, 1.01, float("nan"), True):
            with self.assertRaisesRegex(ValueError, "min confidence"):
                classifier.validate_min_confidence(value)
        with tempfile.TemporaryDirectory() as directory:
            args = argparse.Namespace(
                deck_kind="slides",
                slide=[],
                limit=0,
                min_confidence=0.72,
            )
            with patch.dict(
                classifier.DECKS,
                {"slides": {"asset_dir": Path(directory)}},
                clear=True,
            ), self.assertRaisesRegex(ValueError, "no slides images"):
                classifier.classify_video("missing-video", args)

    def test_batch_results_must_bind_one_to_one_to_requested_slides(self):
        slides = [Path("slide-001.jpg"), Path("slide-002.jpg")]
        valid = [
            {"filename": "slide-001.jpg", "image_index": 1},
            {"filename": "slide-002.jpg", "image_index": 2},
        ]
        duplicate = [
            {"filename": "slide-001.jpg", "image_index": 1},
            {"filename": "slide-001.jpg", "image_index": 1},
        ]

        self.assertEqual(
            [(slides[0], valid[0]), (slides[1], valid[1])],
            classifier.resolve_batch_results(slides, valid),
        )
        with self.assertRaisesRegex(RuntimeError, "uniquely identify"):
            classifier.resolve_batch_results(slides, duplicate)

    def test_corpus_completion_requires_successful_current_cache_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            deck = root / "slides"
            image_dir = deck / "video-1"
            image_dir.mkdir(parents=True)
            images = [image_dir / "slide-001.jpg", image_dir / "slide-002.jpg"]
            images[0].write_bytes(b"image-1")
            images[1].write_bytes(b"image-2")
            audit = root / "audit.json"
            item = {"video_id": "video-1", "deck_kind": "slides", "images": 2}
            args = corpus_args()
            manifest = [
                {"filename": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                for path in images
            ]
            digest = hashlib.sha256(
                json.dumps(manifest, separators=(",", ":"), sort_keys=True).encode()
            ).hexdigest()
            cache_policy = process_corpus.expected_cache_policy(item, args)
            records = [
                {
                    "image": str(path),
                    "image_sha256": row["sha256"],
                    "cache_schema_version": process_corpus.CACHE_SCHEMA_VERSION,
                    "cache_status": "succeeded",
                    "policy_version": process_corpus.POLICY_VERSION,
                    "prompt_contract_sha256": process_corpus.PROMPT_CONTRACT_SHA256,
                    "cache_policy": cache_policy,
                    "model": args.model,
                    "deck_kind": "slides",
                    "confidence": 0.9 if index == 0 else 0.2,
                    "is_content_slide": index == 0,
                }
                for index, (path, row) in enumerate(
                    zip(images, manifest, strict=True)
                )
            ]
            base = {
                "video_id": "video-1",
                "deck_kind": "slides",
                "model": "classifier-test",
                "policy_version": process_corpus.POLICY_VERSION,
                "prompt_contract_sha256": process_corpus.PROMPT_CONTRACT_SHA256,
                "hide_rejected": False,
                "accepted_count": 1,
                "rejected_count": 1,
                "accepted": records[:1],
                "rejected": records[1:],
                "min_confidence": args.min_confidence,
                "cache_policy": cache_policy,
                "input_manifest": manifest,
                "input_manifest_sha256": digest,
            }
            with patch.object(process_corpus, "audit_path", return_value=audit), patch.dict(
                process_corpus.DECKS, {"slides": deck}
            ):
                audit.write_text(json.dumps(base), encoding="utf-8")
                self.assertFalse(process_corpus.completed(item, args))

                audit.write_text(
                    json.dumps(
                        {
                            **base,
                            "status": "succeeded",
                            "cache_schema_version": process_corpus.CACHE_SCHEMA_VERSION,
                        }
                    ),
                    encoding="utf-8",
                )
                self.assertTrue(process_corpus.completed(item, args))
                self.assertFalse(
                    process_corpus.completed(item, corpus_args(min_confidence=0.8))
                )
                images[0].write_bytes(b"changed-image")
                self.assertFalse(process_corpus.completed(item, args))

    def test_codex_slide_agents_are_ephemeral_and_read_only_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "video-1" / "slide-001.jpg"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"image")

            def completed(command, **_kwargs):
                output = Path(command[command.index("-o") + 1])
                output.write_text(
                    '{"text":"visible","confidence":0.9,"notes":"read"}',
                    encoding="utf-8",
                )
                return Mock(returncode=0, stdout="", stderr="")

            with patch.object(VISION, "ROOT", root), patch.object(
                VISION.shutil, "which", return_value="/usr/bin/codex"
            ), patch.object(VISION.subprocess, "run", side_effect=completed) as run:
                VISION.codex_cli(image, "", "model", 30)

            command = run.call_args.args[0]
            self.assertIn("--ephemeral", command)
            self.assertIn("--ignore-user-config", command)
            self.assertIn("--ignore-rules", command)
            self.assertIn("--skip-git-repo-check", command)
            self.assertEqual("read-only", command[command.index("-s") + 1])
            disabled = {
                command[index + 1]
                for index, value in enumerate(command[:-1])
                if value == "--disable"
            }
            self.assertTrue(
                {"shell_tool", "browser_use", "apps", "plugins"}.issubset(disabled)
            )

            classifier_output = {
                "is_content_slide": True,
                "confidence": 0.9,
                "ocr_ready": False,
                "direct_read_ready": True,
            }

            def classifier_completed(command, **_kwargs):
                output = Path(command[command.index("-o") + 1])
                output.write_text(json.dumps(classifier_output), encoding="utf-8")
                return Mock(returncode=0, stdout="", stderr="")

            with patch.object(classifier, "ROOT", root), patch.object(
                classifier.shutil, "which", return_value="/usr/bin/codex"
            ), patch.object(
                classifier.subprocess,
                "run",
                side_effect=classifier_completed,
            ) as classifier_run:
                classifier.codex_cli(image, "model", 30)
            classifier_command = classifier_run.call_args.args[0]
            classifier_disabled = {
                classifier_command[index + 1]
                for index, value in enumerate(classifier_command[:-1])
                if value == "--disable"
            }
            self.assertTrue(
                {"shell_tool", "browser_use", "apps", "plugins"}.issubset(
                    classifier_disabled
                )
            )
            self.assertIn("--ignore-user-config", classifier_command)
            self.assertIn("--ignore-rules", classifier_command)
            self.assertEqual(
                "read-only", classifier_command[classifier_command.index("-s") + 1]
            )
            self.assertNotEqual(
                str(root), classifier_command[classifier_command.index("-C") + 1]
            )
            self.assertNotEqual(str(root), command[command.index("-C") + 1])
            self.assertEqual(Path(command[command.index("-C") + 1]), run.call_args.kwargs["cwd"])
            self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", command)


if __name__ == "__main__":
    unittest.main()
