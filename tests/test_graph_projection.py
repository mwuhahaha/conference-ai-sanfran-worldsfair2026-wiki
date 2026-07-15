import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from export_static_site import (
    GRAPH_PROJECTION_MAX_FANOUT,
    Page,
    build_category_projections,
    build_link_maps,
    extract_graph,
)


def node(node_id: str, category: str, title: str | None = None) -> dict:
    return {"id": node_id, "category": category, "title": title or node_id}


class GraphProjectionTests(unittest.TestCase):
    def test_exported_graph_excludes_root_and_category_indexes_and_deduplicates_links(self):
        pages = [
            Page("overview", Path("overview.md"), "Overview", "root", "[[people/a]]", ""),
            Page("people/index", Path("index.md"), "People", "people", "[[people/a]]", ""),
            Page("people/a", Path("a.md"), "A", "people", "[[people/b]] [[people/b]]", ""),
            Page("people/b", Path("b.md"), "B", "people", "[[people/a]]", ""),
        ]
        by_id, by_stem = build_link_maps(pages)

        graph = extract_graph(pages, by_id, by_stem)

        self.assertEqual([item["id"] for item in graph["nodes"]], ["people/a", "people/b"])
        self.assertEqual(graph["links"], [{"source": "people/a", "target": "people/b"}])

    def test_people_projection_uses_company_and_talk_not_topic_hubs(self):
        nodes = [
            node("people/a", "people", "A"),
            node("people/b", "people", "B"),
            node("people/c", "people", "C"),
            node("companies/acme", "companies", "Acme"),
            node("talks/panel", "talks", "Panel"),
            node("topics/agents", "topics", "Agents"),
        ]
        links = [
            {"source": "people/a", "target": "companies/acme"},
            {"source": "people/b", "target": "companies/acme"},
            {"source": "people/b", "target": "talks/panel"},
            {"source": "people/c", "target": "talks/panel"},
            {"source": "people/a", "target": "topics/agents"},
            {"source": "people/c", "target": "topics/agents"},
        ]

        projections = build_category_projections(nodes, links)["people"]

        self.assertEqual(
            [(row["source"], row["target"]) for row in projections],
            [("people/a", "people/b"), ("people/b", "people/c")],
        )
        self.assertEqual(projections[0]["connectors"][0]["id"], "companies/acme")
        self.assertEqual(projections[1]["connectors"][0]["id"], "talks/panel")

    def test_projection_does_not_duplicate_a_direct_source_link(self):
        nodes = [
            node("people/a", "people"),
            node("people/b", "people"),
            node("companies/acme", "companies"),
        ]
        links = [
            {"source": "people/a", "target": "people/b"},
            {"source": "people/a", "target": "companies/acme"},
            {"source": "people/b", "target": "companies/acme"},
        ]

        self.assertEqual(build_category_projections(nodes, links)["people"], [])

    def test_high_fanout_connector_cannot_create_a_clique(self):
        people = [node(f"people/{index}", "people") for index in range(GRAPH_PROJECTION_MAX_FANOUT + 1)]
        company = node("companies/large", "companies")
        links = [
            {"source": person["id"], "target": company["id"]}
            for person in people
        ]

        self.assertEqual(build_category_projections([*people, company], links)["people"], [])


if __name__ == "__main__":
    unittest.main()
