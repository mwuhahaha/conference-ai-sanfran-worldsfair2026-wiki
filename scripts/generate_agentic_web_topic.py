#!/usr/bin/env python3
"""Generate the Agentic Web topic from official schedule anchors and local resources."""

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

GROUPS = [
    (
        "Search, Catalogs, And Web Data",
        [
            "search engine",
            "real-time web data",
            "agent-readable",
            "web data infrastructure",
        ],
    ),
    (
        "Browser And Computer-Use Web",
        [
            "browser agents",
            "agentify the web",
            "world wide web",
            "web automation",
            "websites like humans",
        ],
    ),
    (
        "Agent-Facing Interfaces And Web Substrates",
        [
            "web for agents",
            "html is all agents need",
        ],
    ),
]

RESOURCE_STEMS = [
    ("talk-video-transcript-map", "Talk/video/transcript relation map"),
    ("youtube-xnXqpUW_Kp8", "Will Bryk related YouTube evidence"),
    ("youtube-o-zkvb0iFDQ", "Liad Yosef related YouTube evidence"),
    ("youtube-YRGjll7uu5w", "Paul Klein IV related YouTube evidence"),
    ("slide-library", "Extracted slide library"),
    ("reconstructed-slide-library", "Reconstructed slide library"),
    ("dense-slide-library", "Dense slide library"),
    ("worldsfair-2026-livestreams", "World's Fair livestream source page"),
]

RELATED_PEOPLE = [
    "will-bryk",
    "liad-yosef",
    "yohan-raju",
    "derek-meegan",
    "dhruv-batra",
    "nixon-dinh",
    "paul-klein-iv",
    "corey-gallon",
    "patricija-emaityt",
    "james-russo",
    "ido-salomon",
    "shubhankar-srivastava",
]

RELATED_COMPANIES_AND_TOOLS = [
    "exa",
    "ora",
    "browserbase",
    "bright-data",
    "mcp",
    "mcp-apps",
    "html",
]


def load_sessions() -> list[dict]:
    blob = json.loads((ROOT / "raw" / "sources" / "official-sessions.json").read_text())
    sessions = blob.get("sessions", blob) if isinstance(blob, dict) else blob
    assign_talk_slugs(sessions)
    return sessions


def matches_agentic_web(session: dict) -> bool:
    haystack = session.get("title", "").lower()
    return any(keyword in haystack for keyword in KEYWORDS)


def group_for(session: dict) -> str:
    haystack = session.get("title", "").lower()
    for group, keywords in GROUPS:
        if any(keyword in haystack for keyword in keywords):
            return group
    return "Adjacent Schedule Anchors"


def session_line(session: dict) -> str:
    speakers = ", ".join(session.get("speakers", [])) or "speaker TBD"
    return (
        f"- [[{talk_slug(session)}]] - {session.get('title')} "
        f"({day_to_date(session.get('day', ''))}, {session.get('time') or 'time TBD'}; "
        f"{session.get('track') or 'track TBD'} / {session.get('room') or 'room TBD'}; {speakers})"
    )


def wiki_page_exists(stem: str) -> bool:
    return any((ROOT / "wiki").glob(f"**/{stem}.md"))


def existing_wikilinks(stems: list[str]) -> list[str]:
    return [f"- [[{stem}]]" for stem in stems if wiki_page_exists(stem)]


def resource_lines() -> list[str]:
    lines: list[str] = []
    for stem, label in RESOURCE_STEMS:
        if wiki_page_exists(stem):
            lines.append(f"- [[{stem}]] - {label}.")
    for path in sorted((ROOT / "wiki" / "slides").glob("youtube-*-slides.md")):
        if path.stem in {
            "youtube-xnXqpUW_Kp8-slides",
            "youtube-o-zkvb0iFDQ-slides",
            "youtube-YRGjll7uu5w-slides",
            "youtube-JnubYCYunk8-slides",
        }:
            lines.append(f"- [[{path.stem}]] - slide evidence for an Agentic Web-adjacent related video.")
    if (ROOT / "raw" / "sources" / "youtube-transcripts" / "JnubYCYunk8.txt").exists():
        lines.append(
            "- `raw/sources/youtube-transcripts/JnubYCYunk8.txt` - transcript evidence on browser-agent representation tradeoffs, including DOM, screenshot, and markdown views."
        )
    return lines


def main() -> int:
    sessions = [session for session in load_sessions() if matches_agentic_web(session)]
    sessions.sort(key=lambda s: (day_to_date(s.get("day", "")), s.get("time", ""), s.get("title", "")))

    grouped: dict[str, list[dict]] = {group: [] for group, _ in GROUPS}
    grouped["Adjacent Schedule Anchors"] = []
    for session in sessions:
        grouped[group_for(session)].append(session)

    lines = [
        frontmatter(
            {
                "title": "Agentic Web",
                "category": "topics",
                "sourceLabels": [
                    "Official conference schedule",
                    "Public YouTube metadata",
                    "YouTube transcript evidence",
                    "Local slide OCR",
                    "Topic synthesis",
                ],
            }
        ),
        "# Agentic Web",
        "",
        "Agentic Web is the conference theme around making the public web usable by AI agents as an action surface, retrieval surface, interface layer, and data substrate. In this wiki it is a topic, not a standalone section: it connects scheduled talks, people, companies, videos, transcripts, slide evidence, and adjacent concepts such as agentic search, browser agents, MCP, sandboxes, catalogs, and agent-facing HTML.",
        "",
        "A practical definition: the Agentic Web is what exists when an agent can discover a relevant web resource, understand the page or catalog well enough to choose an action, operate safely through the available interface, verify the result, and leave enough evidence for a human or system to audit what happened.",
        "",
        "## Why It Matters",
        "The web was built primarily for people reading pages and clicking controls. Agents now need to search, compare, fill forms, inspect docs, use dashboards, purchase, schedule, and operate across services that may not expose clean APIs. That turns web pages, search engines, catalogs, HTML, screenshots, DOM trees, browser sandboxes, and identity controls into infrastructure for AI engineering.",
        "",
        "For builders, this changes the product surface. A site is no longer only a human UX; it can become an agent-readable contract. A search index is no longer just a ranked list for people; it can become a planning substrate. A browser is no longer just a rendering engine; it becomes an execution environment with credentials, permissions, safety boundaries, and observability requirements.",
        "",
        "## How It Works",
        "- Search and retrieval layer: agents need current, source-grounded discovery across web pages, docs, catalogs, and product data before they can reason or act.",
        "- Representation layer: the agent must see the web through some mix of HTML, DOM, markdown, screenshots, accessibility trees, structured feeds, or agent-readable catalogs.",
        "- Action layer: browser automation, computer-use models, MCP tools, APIs, and form workflows turn understanding into clicks, text entry, navigation, and transactions.",
        "- Safety and identity layer: credentials, payment authority, user intent, rate limits, sandboxing, and audit trails decide what the agent is allowed to do.",
        "- Verification layer: transcripts, screenshots, traces, browser events, retrieved sources, and result checks are needed so actions can be reviewed and failures can be corrected.",
        "",
        "## When To Use It",
        "Use Agentic Web patterns when the work depends on public or semi-public web context, when the target service does not expose a sufficient API, when a human workflow must be automated through an existing UI, when agents need current facts beyond a private corpus, or when products want to be discoverable and usable by agents. Prefer direct APIs or MCP tools when the action is high-risk, repetitive, privileged, or available through a more stable machine interface.",
        "",
        "## Where It Is Useful",
        "The pattern is most useful for research agents, shopping and catalog agents, browser-based operations, competitive intelligence, lead and company research, support workflows, data extraction, web-grounded coding assistants, documentation agents, and products that want AI systems to evaluate or recommend them. It is also relevant to agentic commerce, where identity, authority, and settlement become part of the web contract rather than an afterthought.",
        "",
        "## Origins In This Conference",
        "The World's Fair schedule frames this as a multi-track theme rather than a single product category. Search talks emphasize finding the right live web context. Browser and computer-use talks emphasize operating existing websites. Catalog and HTML talks emphasize making web surfaces more legible to agents. MCP and sandbox talks add tool contracts and execution boundaries around those actions.",
        "",
        "## Related Scheduled Sessions",
    ]

    for group, group_sessions in grouped.items():
        if not group_sessions:
            continue
        lines.extend(["", f"### {group}"])
        lines.extend(session_line(session) for session in group_sessions)

    lines.extend(
        [
            "",
            "## Related Resources",
            *resource_lines(),
            "",
            "## Related Topics",
            *existing_wikilinks(
                [
                    "agentic-search",
                    "ai-sandboxes",
                    "mcp",
                    "agent-security",
                    "coding-agents",
                    "agent-evaluations",
                    "inference-engineering",
                ]
            ),
            "",
            "## Related People",
            *existing_wikilinks(RELATED_PEOPLE),
            "",
            "## Related Companies And Tools",
            *existing_wikilinks(RELATED_COMPANIES_AND_TOOLS),
            "",
            "## Design Patterns",
            "- Agent-readable catalogs: expose structured product, documentation, pricing, capability, or availability data so agents do not have to infer everything from visual pages.",
            "- Browser execution sandboxes: isolate web actions, credentials, screenshots, downloads, and traces so agent browsing can be observed and constrained.",
            "- Dual human/agent pages: keep the human page usable, but include enough semantic structure, stable labels, and machine-readable metadata for agents to act reliably.",
            "- Retrieval before action: require the agent to cite or log the page, catalog, or transcript evidence it used before taking a consequential web action.",
            "- Representation fallback: try structured sources first, then HTML or accessibility trees, then screenshots/OCR when the page is only visually understandable.",
            "- Post-action verification: check page state, confirmation messages, generated artifacts, or external records after the action instead of trusting the click path.",
            "",
            "## Risks And Failure Modes",
            "- Visual ambiguity: screenshots can miss hidden state, modals, disabled controls, or off-screen context.",
            "- DOM overload: raw page structure can be too large or noisy for models without summarization and filtering.",
            "- Stale retrieval: search results and cached pages may lag the current site state.",
            "- Authority confusion: an agent may not know whether it is allowed to submit, purchase, message, or change settings.",
            "- Prompt injection: pages and documents can include attacker-controlled instructions that target the agent rather than the human reader.",
            "- Fragile automation: selectors, layouts, bot defenses, and login flows can break browser agents even when the human workflow still works.",
            "",
            "## Open Questions",
            "- Which agent-facing web contract wins: richer HTML, MCP servers, APIs, catalog feeds, browser-use conventions, or a mix of all of them?",
            "- How should websites declare which actions are safe for an agent to perform and which require explicit human confirmation?",
            "- What is the right default representation for an agent: DOM, accessibility tree, markdown, screenshot, structured catalog, or task-specific extraction?",
            "- How should products measure agent experience separately from human UX?",
            "- What evidence should a browser agent preserve so that a user, auditor, or downstream system can trust the result?",
            "",
            "## Evidence Boundary",
            "Official schedule data is canonical for talk titles, speakers, dates, tracks, rooms, and inclusion in the schedule anchor list. YouTube videos, transcripts, local Whisper output, OCR, and reconstructed slide crops are supporting evidence. Treat transcript and OCR-derived claims as reviewable evidence, and verify important slide claims against the embedded slide image or reconstructed crop when available.",
        ]
    )

    out = ROOT / "wiki" / "topics" / "agentic-web.md"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"agentic_web_topic": str(out.relative_to(ROOT)), "schedule_anchors": len(sessions)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
