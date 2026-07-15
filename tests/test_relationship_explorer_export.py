import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_static_site


class RelationshipExplorerExportTests(unittest.TestCase):
    def test_relationship_page_is_search_first_and_keeps_advanced_dataset(self):
        with tempfile.TemporaryDirectory() as directory:
            dist = Path(directory)
            (dist / "relationship.js").write_text("export {};", encoding="utf-8")
            with patch.object(export_static_site, "DIST", dist):
                rendered = export_static_site.render_relationship_explorer([])

        self.assertIn("Relationship explorer", rendered)
        self.assertIn('data-relationship-template="vendor_concept"', rendered)
        self.assertIn('data-relationship-template="entity_neighborhood"', rendered)
        self.assertIn('data-relationship-template="person_concept"', rendered)
        self.assertIn('data-relationship-template="concept_concept"', rendered)
        self.assertIn('data-relationship-view="landscape"', rendered)
        self.assertIn('data-relationship-view="graph"', rendered)
        self.assertIn('data-relationship-view="list"', rendered)
        self.assertIn('data-relationship-view="matrix"', rendered)
        self.assertIn('href="/graph/all/"', rendered)
        self.assertIn('id="relationship-selected-link"', rendered)
        self.assertIn('data-relationship-depth="3"', rendered)
        self.assertIn("Wiki link", rendered)
        self.assertNotIn('id="graph-canvas"', rendered)

    def test_advanced_page_retains_full_graph_controls(self):
        with tempfile.TemporaryDirectory() as directory:
            dist = Path(directory)
            (dist / "graph.js").write_text("export {};", encoding="utf-8")
            with patch.object(export_static_site, "DIST", dist):
                rendered = export_static_site.render_advanced_graph([])

        self.assertIn("Advanced dataset", rendered)
        self.assertIn('id="graph-canvas"', rendered)
        self.assertIn('id="graph-category"', rendered)
        self.assertIn('href="/graph/"', rendered)

    def test_client_bounds_initial_scene_and_uses_public_relationship_fields(self):
        script = (ROOT / "scripts" / "relationship_explorer.js").read_text(encoding="utf-8")

        self.assertIn("const depthLimits = {1: [26, 60], 2: [50, 100], 3: [80, 160]}", script)
        self.assertIn("reachableIds.has(relationship.source) && reachableIds.has(relationship.target)", script)
        self.assertIn('selectedEntityLink.href = node.url', script)
        self.assertIn('if (activeTemplate === "entity_neighborhood") return relationships', script)
        self.assertIn("Show connections' connections", script)
        self.assertIn('fetch("/graph-data.json")', script)
        self.assertIn("organizeFocusedGraph", script)
        self.assertIn("FOCUS_COLOR", script)
        self.assertIn('derivation: "navigation"', script)
        self.assertIn("relationship-expand", script)
        self.assertIn("relationship-type", script)
        self.assertIn("relationship.publicReason", script)
        self.assertIn("relationship.sourceLayers", script)
        self.assertIn("relationship.evidence", script)
        self.assertNotIn("credibilityScore", script)
        self.assertNotIn("rankingScore", script)
        self.assertNotIn("internalScore", script)


if __name__ == "__main__":
    unittest.main()
