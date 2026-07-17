import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_static_site  # noqa: E402
from build_relationship_dataset import load_wiki_pages  # noqa: E402


class StaticExportGitVisibilityTests(unittest.TestCase):
    def init_repository(self, root: Path, ignore: str) -> Path:
        subprocess.run(
            ["git", "init", "--quiet"], cwd=root, check=True, capture_output=True
        )
        (root / ".gitignore").write_text(ignore, encoding="utf-8")
        wiki = root / "wiki"
        wiki.mkdir()
        return wiki

    def test_canonical_tree_excludes_only_ignored_untracked_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = self.init_repository(
                root,
                "wiki/private/\nwiki/assets/private/\n",
            )
            private = wiki / "private"
            assets = wiki / "assets"
            private.mkdir()
            (assets / "private").mkdir(parents=True)
            (wiki / "generated.md").write_text("generated", encoding="utf-8")
            (private / "local.md").write_text("local", encoding="utf-8")
            (private / "tracked.md").write_text("tracked", encoding="utf-8")
            (assets / "public.txt").write_text("public", encoding="utf-8")
            (assets / "private" / "local.txt").write_text(
                "private", encoding="utf-8"
            )
            (assets / "private" / "tracked.txt").write_text(
                "tracked", encoding="utf-8"
            )
            subprocess.run(
                [
                    "git",
                    "add",
                    "-f",
                    "wiki/private/tracked.md",
                    "wiki/assets/private/tracked.txt",
                ],
                cwd=root,
                check=True,
                capture_output=True,
            )

            excluded = export_static_site.ignored_untracked_wiki_paths(wiki)
            markdown = {
                path.relative_to(wiki)
                for path in export_static_site.public_wiki_markdown_paths(
                    wiki, excluded
                )
            }
            output = root / "output"
            export_static_site.copy_public_wiki_assets(
                assets,
                output,
                wiki_root=wiki,
                excluded_paths=excluded,
            )

            self.assertEqual(
                excluded,
                frozenset(
                    {
                        Path("private/local.md"),
                        Path("assets/private/local.txt"),
                    }
                ),
            )
            self.assertEqual(
                markdown,
                {Path("generated.md"), Path("private/tracked.md")},
            )
            self.assertTrue((output / "public.txt").exists())
            self.assertTrue((output / "private" / "tracked.txt").exists())
            self.assertFalse((output / "private" / "local.txt").exists())

    def test_non_git_tree_preserves_filesystem_export_behavior(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = root / "wiki"
            private = wiki / "private"
            private.mkdir(parents=True)
            (root / ".gitignore").write_text("wiki/private/\n", encoding="utf-8")
            (private / "local.md").write_text("local", encoding="utf-8")

            excluded = export_static_site.ignored_untracked_wiki_paths(wiki)
            markdown = export_static_site.public_wiki_markdown_paths(wiki, excluded)

            self.assertEqual(excluded, frozenset())
            self.assertEqual(markdown, [private / "local.md"])

    def test_candidate_uses_canonical_logical_ignore_policy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.init_repository(
                root,
                ".ops/state/cache/\nknowledge/private/\nknowledge/assets/private/\n",
            )
            canonical_wiki = root / "knowledge"
            tracked_page = canonical_wiki / "private" / "tracked.md"
            tracked_asset = canonical_wiki / "assets" / "private" / "tracked.txt"
            tracked_page.parent.mkdir(parents=True)
            tracked_asset.parent.mkdir(parents=True)
            tracked_page.write_text("canonical", encoding="utf-8")
            tracked_asset.write_text("canonical", encoding="utf-8")
            subprocess.run(
                [
                    "git",
                    "add",
                    "-f",
                    "knowledge/private/tracked.md",
                    "knowledge/assets/private/tracked.txt",
                ],
                cwd=root,
                check=True,
                capture_output=True,
            )
            candidate_wiki = (
                root
                / ".ops"
                / "state"
                / "cache"
                / "wiki-maker"
                / "candidates"
                / "candidate-1"
                / "workspace"
                / "wiki"
            )
            candidate_wiki.mkdir(parents=True)
            page = candidate_wiki / "topics" / "staged.md"
            page.parent.mkdir()
            page.write_text("staged", encoding="utf-8")
            ignored_page = candidate_wiki / "private" / "local.md"
            staged_tracked_page = candidate_wiki / "private" / "tracked.md"
            ignored_asset = candidate_wiki / "assets" / "private" / "local.txt"
            staged_tracked_asset = (
                candidate_wiki / "assets" / "private" / "tracked.txt"
            )
            ignored_page.parent.mkdir()
            ignored_asset.parent.mkdir(parents=True)
            ignored_page.write_text("local", encoding="utf-8")
            staged_tracked_page.write_text("staged tracked", encoding="utf-8")
            ignored_asset.write_text("local", encoding="utf-8")
            staged_tracked_asset.write_text("staged tracked", encoding="utf-8")

            with patch.dict(
                "os.environ",
                {
                    "WIKI_MAKER_SOURCE_POLICY_ROOT": str(root),
                    "WIKI_MAKER_SOURCE_POLICY_WIKI_ROOT": str(canonical_wiki),
                },
            ):
                excluded = export_static_site.ignored_untracked_wiki_paths(
                    candidate_wiki
                )
                markdown = export_static_site.public_wiki_markdown_paths(
                    candidate_wiki, excluded
                )
                output = root / "staged-assets"
                export_static_site.copy_public_wiki_assets(
                    candidate_wiki / "assets",
                    output,
                    wiki_root=candidate_wiki,
                    excluded_paths=excluded,
                )

            self.assertEqual(
                excluded,
                frozenset(
                    {Path("private/local.md"), Path("assets/private/local.txt")}
                ),
            )
            self.assertEqual(markdown, [staged_tracked_page, page])
            self.assertTrue((output / "private" / "tracked.txt").exists())
            self.assertFalse((output / "private" / "local.txt").exists())

    def test_candidate_excludes_ignored_page_from_all_public_projections(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            canonical_wiki = self.init_repository(
                root,
                ".ops/\nwiki/topics/local.md\n",
            )
            candidate_wiki = (
                root
                / ".ops"
                / "state"
                / "cache"
                / "wiki-maker"
                / "candidates"
                / "candidate-1"
                / "workspace"
                / "wiki"
            )
            topics = candidate_wiki / "topics"
            topics.mkdir(parents=True)
            (topics / "public.md").write_text(
                "---\ntitle: Public Concept\ncategory: topics\n---\n# Public Concept\n",
                encoding="utf-8",
            )
            (topics / "local.md").write_text(
                "---\ntitle: Local Note\ncategory: topics\n---\n# Local Note\n",
                encoding="utf-8",
            )
            raw = root / "raw" / "sources"
            raw.mkdir(parents=True)
            (raw / "relationship-explorer-profile.json").write_text(
                """{
  "id": "visibility-test",
  "version": 1,
  "roleCategories": {
    "people": [],
    "concepts": ["topics"],
    "organizations": []
  },
  "organizationRoles": {}
}
""",
                encoding="utf-8",
            )
            dist = root / "dist"
            environment = {
                "WIKI_MAKER_SOURCE_POLICY_ROOT": str(root),
                "WIKI_MAKER_SOURCE_POLICY_WIKI_ROOT": str(canonical_wiki),
            }

            with (
                patch.dict("os.environ", environment),
                patch.object(export_static_site, "WIKI", candidate_wiki),
                patch.object(export_static_site, "RAW", raw),
                patch.object(export_static_site, "DIST", dist),
            ):
                export_static_site.export()
                relationship_pages = load_wiki_pages(candidate_wiki)

            graph = json.loads(
                (dist / "graph-data.json").read_text(encoding="utf-8")
            )
            relationships = json.loads(
                (dist / "relationship-data.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                [page.id for page in relationship_pages],
                ["topics/public"],
            )
            self.assertEqual(
                [node["id"] for node in graph["nodes"]],
                ["topics/public"],
            )
            self.assertEqual(
                [node["id"] for node in relationships["nodes"]],
                ["topics/public"],
            )
            self.assertTrue((dist / "md" / "topics" / "public.md").exists())
            self.assertFalse((dist / "md" / "topics" / "local.md").exists())
            self.assertFalse((dist / "topics" / "local" / "index.html").exists())


if __name__ == "__main__":
    unittest.main()
