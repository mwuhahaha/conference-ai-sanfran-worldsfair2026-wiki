import argparse
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import process_slide_corpus_ai as corpus
from scripts import quarantine_stale_slide_ai as quarantine


def valid_audit(
    *,
    video_id: str,
    kind: str,
    image: Path,
    recreation: Path,
    args: argparse.Namespace,
) -> dict:
    item = {"video_id": video_id, "deck_kind": kind, "images": 1}
    image_digest = hashlib.sha256(image.read_bytes()).hexdigest()
    manifest = [{"filename": image.name, "sha256": image_digest}]
    manifest_digest = hashlib.sha256(
        json.dumps(manifest, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()
    recreation_bytes = recreation.read_bytes()
    recreation_digest = hashlib.sha256(recreation_bytes).hexdigest()
    root = image.parents[4]
    recreation_manifest = [
        {
            "path": str(recreation.relative_to(root)),
            "sha256": recreation_digest,
            "size_bytes": len(recreation_bytes),
        }
    ]
    recreation_manifest_digest = hashlib.sha256(
        json.dumps(
            recreation_manifest, separators=(",", ":"), sort_keys=True
        ).encode()
    ).hexdigest()
    cache_policy = corpus.expected_cache_policy(item, args)
    record = {
        "image": str(image),
        "image_sha256": image_digest,
        "cache_schema_version": corpus.CACHE_SCHEMA_VERSION,
        "cache_status": "succeeded",
        "policy_version": corpus.POLICY_VERSION,
        "prompt_contract_sha256": corpus.PROMPT_CONTRACT_SHA256,
        "cache_policy": cache_policy,
        "model": args.model,
        "deck_kind": kind,
        "confidence": 0.9,
        "is_content_slide": True,
        "recreation": str(recreation),
        "recreation_sha256": recreation_digest,
        "recreation_size_bytes": len(recreation_bytes),
    }
    return {
        "status": "succeeded",
        "cache_schema_version": corpus.CACHE_SCHEMA_VERSION,
        "video_id": video_id,
        "deck_kind": kind,
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
        "publication_schema_version": 1,
        "publication_status": "succeeded",
        "recreation_manifest": recreation_manifest,
        "recreation_manifest_sha256": recreation_manifest_digest,
    }


class SlideAiQuarantineTests(unittest.TestCase):
    def fixture(self, root: Path):
        pages = root / "wiki" / "slides"
        recreations = root / "wiki" / "assets" / "slide-recreations"
        classifications = root / "raw" / "sources" / "slide-ai-classification"
        deck = root / "wiki" / "assets" / "dense-slides"
        pages.mkdir(parents=True)
        recreations.mkdir(parents=True)
        classifications.mkdir(parents=True)
        deck.mkdir(parents=True)
        return pages, recreations, classifications, deck

    def patches(
        self,
        *,
        pages: Path,
        recreations: Path,
        classifications: Path,
        deck: Path,
    ):
        def path_for(video_id: str, kind: str) -> Path:
            return classifications / kind / video_id / "audit.json"

        return (
            patch.object(quarantine, "ROOT", pages.parents[1]),
            patch.object(quarantine, "SLIDE_PAGES", pages),
            patch.object(quarantine, "RECREATION_ROOT", recreations),
            patch.object(quarantine, "CLASSIFICATION_ROOT", classifications),
            patch.object(corpus, "audit_path", side_effect=path_for),
            patch.dict(corpus.DECKS, {"dense": deck}),
        )

    def test_current_bound_audit_can_surface_section_and_recreation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages, recreations, classifications, deck = self.fixture(root)
            video_id = "video-1"
            image = deck / video_id / "slide-001.jpg"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            recreation = recreations / "dense" / video_id / "slide-001.html"
            recreation.parent.mkdir(parents=True)
            recreation.write_text("current", encoding="utf-8")
            args = quarantine.contract_args(model="classifier-test")
            audit = valid_audit(
                video_id=video_id,
                kind="dense",
                image=image,
                recreation=recreation,
                args=args,
            )
            audit_path = classifications / "dense" / video_id / "audit.json"
            audit_path.parent.mkdir(parents=True)
            audit_path.write_text(json.dumps(audit), encoding="utf-8")
            (pages / "youtube-video-1-dense-slides.md").write_text(
                "# Deck\n\n## Cropped Visible Slides\n"
                "- AI slide classifier: `content_slide` confidence `0.9`\n"
                "- [open HTML recreation]"
                "(/assets/slide-recreations/dense/video-1/slide-001.html)\n\n"
                "Classification audit: "
                "`raw/sources/slide-ai-classification/dense/video-1/audit.json`\n",
                encoding="utf-8",
            )
            patches = self.patches(
                pages=pages,
                recreations=recreations,
                classifications=classifications,
                deck=deck,
            )
            with (
                patches[0],
                patches[1],
                patches[2],
                patches[3],
                patches[4],
                patches[5],
            ):
                cache: dict[tuple[str, str], list[str]] = {}
                page_report = quarantine.scan_pages(args, cache)
                asset_report = quarantine.scan_recreations(args, cache)
                pages_changed = quarantine.quarantine_pages(args, cache)

            self.assertEqual([], page_report["stale_sections"])
            self.assertEqual(1, page_report["current_sections"])
            self.assertEqual([], asset_report["stale_assets"])
            self.assertEqual(1, asset_report["current_assets"])
            self.assertEqual(0, pages_changed)

    def test_stale_section_is_withheld_and_stale_asset_is_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pages, recreations, classifications, deck = self.fixture(root)
            video_id = "video-1"
            image = deck / video_id / "slide-001.jpg"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"image")
            audit_path = classifications / "dense" / video_id / "audit.json"
            audit_path.parent.mkdir(parents=True)
            audit_path.write_text(
                json.dumps(
                    {
                        "video_id": video_id,
                        "deck_kind": "dense",
                        "policy_version": "historical-v2",
                        "accepted": [],
                    }
                ),
                encoding="utf-8",
            )
            page = pages / "youtube-video-1-dense-slides.md"
            page.write_text(
                "# Deck\n\n## Cropped Visible Slides\n"
                "- AI slide classifier: `content_slide` confidence `0.9`\n"
                "- [open HTML recreation]"
                "(/assets/slide-recreations/dense/video-1/slide-001.html)\n\n"
                "Classification audit: "
                "`raw/sources/slide-ai-classification/dense/video-1/audit.json`\n",
                encoding="utf-8",
            )
            recreation = recreations / "dense" / video_id / "slide-001.html"
            recreation.parent.mkdir(parents=True)
            recreation.write_text("stale", encoding="utf-8")
            args = quarantine.contract_args(model="classifier-test")
            patches = self.patches(
                pages=pages,
                recreations=recreations,
                classifications=classifications,
                deck=deck,
            )
            with (
                patches[0],
                patches[1],
                patches[2],
                patches[3],
                patches[4],
                patches[5],
            ):
                self.assertEqual(1, quarantine.quarantine_pages(args, {}))
                self.assertEqual(1, quarantine.quarantine_recreations(args, {}))
                report = quarantine.scan_pages(args, {})

            updated = page.read_text(encoding="utf-8")
            self.assertIn(quarantine.WITHHELD_MARKER, updated)
            self.assertNotIn("Classification audit:", updated)
            self.assertNotIn("/assets/slide-recreations/", updated)
            self.assertFalse(recreation.exists())
            self.assertEqual([], report["stale_sections"])
            self.assertEqual(1, report["withheld_sections"])

    def test_repository_pages_and_assets_do_not_surface_unbound_classifier_artifacts(self):
        report = quarantine.scan(quarantine.contract_args())

        self.assertEqual([], report["pages"]["stale_sections"])
        self.assertEqual([], report["recreations"]["stale_assets"])


if __name__ == "__main__":
    unittest.main()
