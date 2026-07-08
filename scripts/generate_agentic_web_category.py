#!/usr/bin/env python3
"""Generate the Agentic Web category from official schedule anchors."""

from __future__ import annotations

import json
from pathlib import Path

from build_worldsfair_wiki import ROOT, assign_talk_slugs, day_to_date, frontmatter, talk_slug


KEYWORDS = [
    "agentic web",
    "web for agents",
    "agentify the web",
    "html is all agents need",
    "search engine for the agentic web",
    "computer-use models will agentify the web",
    "agent-readable",
    "real-time web data",
    "web automation",
    "web data infrastructure",
    "websites like humans",
    "browser",
    "world wide web",
]


def load_sessions() -> list[dict]:
    blob = json.loads((ROOT / "raw" / "sources" / "official-sessions.json").read_text())
    sessions = blob.get("sessions", blob) if isinstance(blob, dict) else blob
    assign_talk_slugs(sessions)
    return sessions


def matches_agentic_web(session: dict) -> bool:
    haystack = session.get("title", "").lower()
    return any(keyword in haystack for keyword in KEYWORDS)


def session_line(session: dict) -> str:
    return (
        f"- [[{talk_slug(session)}]] - {session.get('title')} "
        f"({day_to_date(session.get('day', ''))}, {session.get('time') or 'time TBD'}; "
        f"{session.get('track') or 'track TBD'} / {session.get('room') or 'room TBD'})"
    )


def main() -> int:
    sessions = [session for session in load_sessions() if matches_agentic_web(session)]
    sessions.sort(key=lambda s: (day_to_date(s.get("day", "")), s.get("time", ""), s.get("title", "")))

    out_dir = ROOT / "wiki" / "agentic-web"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "id": talk_slug(session),
            "title": session.get("title"),
            "path": f"wiki/talks/{talk_slug(session)}.md",
            "date": day_to_date(session.get("day", "")),
            "time": session.get("time"),
            "track": session.get("track"),
            "room": session.get("room"),
            "speakers": session.get("speakers", []),
        }
        for session in sessions
    ]
    (out_dir / "registry.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        frontmatter(
            {
                "title": "Agentic Web",
                "category": "agentic-web",
                "sourceLabels": ["Official conference schedule", "Public YouTube metadata", "Local slide OCR"],
            }
        ),
        "# Agentic Web",
        "",
        "Agentic Web tracks the World's Fair sessions about making the web readable, searchable, actionable, and controllable by AI agents. It covers agent-facing HTML, computer-use models, search and retrieval for agents, browser/web automation, agent-readable catalogs, and the shift from human-only interfaces toward surfaces that agents can safely operate.",
        "",
        "## Schedule Anchors",
    ]
    if sessions:
        lines.extend(session_line(session) for session in sessions)
    else:
        lines.append("- No official schedule anchors matched the Agentic Web rule set.")
    lines.extend(
        [
            "",
            "## Why It Matters",
            "The Agentic Web category is a schedule-specific layer, not just a keyword topic. It groups talks where the official schedule points to web surfaces becoming agent interfaces: search engines for agents, rebuilding the web for agents, computer-use models acting through websites, and HTML or structured interfaces as the substrate for agent action.",
            "",
            "## Related Topics",
            "- [[agentic-search]]",
            "- [[coding-agents]]",
            "- [[ai-sandboxes]]",
            "- [[mcp]]",
            "",
            "## Evidence Boundary",
            "This category is generated from official schedule titles, with official track and room metadata preserved for each included talk. Related YouTube, transcript, and slide evidence can support the article, but official schedule metadata remains canonical for talk inclusion and labels.",
        ]
    )
    (out_dir / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"agentic_web_sessions": len(sessions)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
