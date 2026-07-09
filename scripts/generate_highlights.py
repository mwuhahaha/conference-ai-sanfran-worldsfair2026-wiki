#!/usr/bin/env python3
"""Generate highlighted target pages for extra-expanded wiki coverage."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
TARGETS = ROOT / "raw" / "sources" / "highlighted-targets.json"


CATEGORY_BY_TYPE = {
    "talk": "talks",
    "person": "people",
    "company": "companies",
    "topic": "topics",
    "tool": "tools",
    "resource": "resources",
}


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in items) + "]"


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: {yaml_list(value)}")
        elif value is None:
            continue
        else:
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def title_from_page(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if line.startswith("title:"):
                    return line.split(":", 1)[1].strip().strip('"')
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback


def target_path(target: dict) -> Path:
    category = CATEGORY_BY_TYPE.get(target["targetType"], target["targetType"])
    return WIKI / category / f"{target['slug']}.md"


def target_wikilink(target: dict) -> str:
    path = target_path(target)
    label = title_from_page(path, target.get("title") or target["slug"])
    return f"[[{path.stem}|{label}]]"


def render_highlight(target: dict) -> str:
    related = target.get("relatedTargets", [])
    title = target.get("title") or target["slug"]
    body = [
        frontmatter(
            {
                "title": title,
                "category": "highlights",
                "targetType": target.get("targetType"),
                "targetSlug": target.get("slug"),
                "priority": target.get("priority"),
                "sourceLabels": ["Highlight registry", "Wiki navigation"],
            }
        ),
        f"# {title}",
        "",
        "## Page",
        f"- {target_wikilink(target)}",
        "",
        "## Related Highlight Targets",
    ]
    if related:
        for slug in related:
            body.append(f"- [[{slug}]]")
    else:
        body.append("- No related highlight targets listed.")
    return "\n".join(body).rstrip() + "\n"


def render_index(targets: list[dict]) -> str:
    lines = [
        frontmatter({"title": "Highlights", "category": "highlights", "sourceLabels": ["Highlight registry"]}),
        "# Highlights",
        "",
        "## Index",
    ]
    for target in sorted(targets, key=lambda item: (item.get("priority") != "critical", item.get("title", item["slug"]).lower())):
        lines.append(f"- {target_wikilink(target)}")
    lines.extend(["", "## By Type", "- [[highlighted-concepts-people-talks|Concepts, People, And Talks]]"])
    return "\n".join(lines).rstrip() + "\n"


def render_grouped_map(targets: list[dict]) -> str:
    groups = [
        ("Concepts And Topics", {"topic", "tool"}),
        ("People", {"person"}),
        ("Talks", {"talk"}),
        ("Companies And Resources", {"company", "resource"}),
    ]
    lines = [
        frontmatter({"title": "Highlighted Concepts, People, And Talks", "category": "highlights", "sourceLabels": ["Highlight registry", "Wiki navigation"]}),
        "# Highlighted Concepts, People, And Talks",
    ]
    for heading, types in groups:
        rows = [target for target in targets if target.get("targetType") in types]
        if not rows:
            continue
        lines.extend(["", f"## {heading}"])
        for target in sorted(rows, key=lambda item: (item.get("priority") != "critical", item.get("title", item["slug"]).lower())):
            lines.append(f"- {target_wikilink(target)}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    targets = json.loads(TARGETS.read_text(encoding="utf-8"))
    out_dir = WIKI / "highlights"
    out_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for target in targets:
        path = out_dir / f"highlight-{target['id']}.md"
        path.write_text(render_highlight(target), encoding="utf-8")
        records.append(
            {
                "id": f"highlight-{target['id']}",
                "title": target.get("title") or target["slug"],
                "path": str(path.relative_to(ROOT)),
                "targetType": target.get("targetType"),
                "targetSlug": target.get("slug"),
                "priority": target.get("priority"),
            }
        )
    (out_dir / "index.md").write_text(render_index(targets), encoding="utf-8")
    (out_dir / "highlighted-concepts-people-talks.md").write_text(render_grouped_map(targets), encoding="utf-8")
    records.append(
        {
            "id": "highlighted-concepts-people-talks",
            "title": "Highlighted Concepts, People, And Talks",
            "path": "wiki/highlights/highlighted-concepts-people-talks.md",
            "targetType": "index",
            "targetSlug": "highlighted-concepts-people-talks",
            "priority": "critical",
        }
    )
    records.sort(key=lambda item: item["title"].lower())
    (out_dir / "registry.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"highlights": len(records)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
