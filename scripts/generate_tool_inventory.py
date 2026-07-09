#!/usr/bin/env python3
"""Generate high-confidence tool pages from the World's Fair corpus."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


TOOLS = [
    {"title": "Claude", "slug": "claude", "aliases": ["Claude"]},
    {"title": "Claude Agent SDK", "slug": "claude-agent-sdk", "aliases": ["Claude Agent SDK"]},
    {"title": "Codex", "slug": "codex", "aliases": ["Codex"]},
    {"title": "Model Context Protocol", "slug": "mcp", "aliases": ["MCP", "Model Context Protocol"]},
    {"title": "MCP Apps", "slug": "mcp-apps", "aliases": ["MCP Apps", "MCP UI", "MCP-UI"]},
    {"title": "mcpc", "slug": "mcpc", "aliases": ["mcpc"]},
    {"title": "DSPy", "slug": "dspy", "aliases": ["DSPy"]},
    {"title": "LangGraph", "slug": "langgraph", "aliases": ["LangGraph"]},
    {"title": "LangChain", "slug": "langchain", "aliases": ["LangChain"]},
    {"title": "GitHub Copilot", "slug": "github-copilot", "aliases": ["GitHub Copilot"]},
    {"title": "Azure", "slug": "azure", "aliases": ["Azure"]},
    {"title": "Microsoft IQ", "slug": "microsoft-iq", "aliases": ["Microsoft IQ", "Foundry IQ", "Fabric IQ", "Work IQ"]},
    {"title": "VS Code", "slug": "vs-code", "aliases": ["VS Code", "VSC-Bench"]},
    {"title": "Cursor", "slug": "cursor", "aliases": ["Cursor"]},
    {"title": "Windsurf", "slug": "windsurf", "aliases": ["Windsurf"]},
    {"title": "Google Antigravity", "slug": "google-antigravity", "aliases": ["Google Antigravity", "Antigravity"]},
    {"title": "Sourcegraph Amp", "slug": "sourcegraph-amp", "aliases": ["Sourcegraph", "Amp"]},
    {"title": "Arize", "slug": "arize", "aliases": ["Arize"]},
    {"title": "Braintrust", "slug": "braintrust", "aliases": ["Braintrust"]},
    {"title": "Langfuse", "slug": "langfuse", "aliases": ["Langfuse"]},
    {"title": "Zep", "slug": "zep", "aliases": ["Zep"]},
    {"title": "Neo4j", "slug": "neo4j", "aliases": ["Neo4j"]},
    {"title": "GraphRAG", "slug": "graphrag", "aliases": ["GraphRAG", "CrabRAG"]},
    {"title": "Tailscale", "slug": "tailscale", "aliases": ["Tailscale"]},
    {"title": "Tailscale Aperture", "slug": "tailscale-aperture", "aliases": ["Aperture", "Tailscale Aperture"]},
    {"title": "Browserbase", "slug": "browserbase", "aliases": ["Browserbase"]},
    {"title": "chrome-agent", "slug": "chrome-agent", "aliases": ["chrome-agent", "Chrome Agent", "Chrome DevTools Protocol", "CDP"]},
    {"title": "Arrakis", "slug": "arrakis", "aliases": ["Arrakis"]},
    {"title": "Docker", "slug": "docker", "aliases": ["Docker"]},
    {"title": "Temporal", "slug": "temporal", "aliases": ["Temporal"]},
    {"title": "Dagger", "slug": "dagger", "aliases": ["Dagger"]},
    {"title": "Modal", "slug": "modal", "aliases": ["Modal"], "exclude": [r"multi-modal", r"multimodal", r"unexpected modal"], "markdown_title_only": True},
    {"title": "OpenRouter", "slug": "openrouter", "aliases": ["OpenRouter"]},
    {"title": "Hugging Face Hub", "slug": "hugging-face-hub", "aliases": ["Hugging Face Hub", "Hugging Face"]},
    {"title": "Gemini", "slug": "gemini", "aliases": ["Gemini", "Gemini Live"]},
    {"title": "Amazon Bedrock", "slug": "amazon-bedrock", "aliases": ["Amazon Bedrock", "Bedrock AgentCore", "Bedrock Agents"]},
    {"title": "Amazon Nova Act", "slug": "amazon-nova-act", "aliases": ["Amazon Nova Act", "Nova Act"]},
    {"title": "Azure AI Foundry", "slug": "azure-ai-foundry", "aliases": ["Azure AI Foundry", "Microsoft Foundry"]},
    {"title": "Twilio Agent Connect", "slug": "twilio-agent-connect", "aliases": ["Twilio Agent Connect"]},
    {"title": "Strands Agents", "slug": "strands-agents", "aliases": ["Strands Agents", "Strands"]},
    {"title": "NVIDIA Data Designer", "slug": "nvidia-data-designer", "aliases": ["NVIDIA Data Designer", "Data Designer"]},
    {"title": "GLM-5.2", "slug": "glm-5-2", "aliases": ["GLM-5.2", "GLM 5.2", "Z.ai GLM"]},
    {"title": "Prime Intellect Stack", "slug": "prime-intellect", "aliases": ["Prime Intellect", "Prime Intellect Stack", "prime-rl", "verifiers"]},
    {"title": "vLLM", "slug": "vllm", "aliases": ["vLLM"]},
    {"title": "TokenSpeed", "slug": "tokenspeed", "aliases": ["TokenSpeed"]},
    {"title": "Spin", "slug": "spin", "aliases": ["Spin"], "exclude": [r"Spin at the Gate", r"spin up", r"spinning"]},
    {"title": "WebAssembly", "slug": "webassembly", "aliases": ["WebAssembly", "WASM"]},
    {"title": "x402", "slug": "x402", "aliases": ["x402"]},
    {"title": "Krea 2", "slug": "krea-2", "aliases": ["Krea 2"]},
    {"title": "Pydantic", "slug": "pydantic", "aliases": ["Pydantic"]},
    {"title": "Prefect", "slug": "prefect", "aliases": ["Prefect"]},
    {"title": "Daytona", "slug": "daytona", "aliases": ["Daytona"]},
    {"title": "Manus", "slug": "manus", "aliases": ["Manus"]},
    {"title": "OpenHands", "slug": "openhands", "aliases": ["OpenHands"]},
    {"title": "Factory AI", "slug": "factory-ai", "aliases": ["Factory AI"]},
    {"title": "Snowflake", "slug": "snowflake", "aliases": ["Snowflake"]},
    {"title": "LlamaIndex", "slug": "llamaindex", "aliases": ["LlamaIndex"]},
    {"title": "Exa", "slug": "exa", "aliases": ["Exa", "Exa.ai"]},
    {"title": "Reducto", "slug": "reducto", "aliases": ["Reducto"]},
    {"title": "SonarQube", "slug": "sonarqube", "aliases": ["SonarQube"]},
]


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-") or "untitled"


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


def pattern_for(alias: str) -> re.Pattern:
    escaped = re.escape(alias)
    if re.search(r"[A-Za-z0-9]$", alias) and re.search(r"^[A-Za-z0-9]", alias):
        return re.compile(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", re.I)
    return re.compile(escaped, re.I)


def matches_any(text: str, tool: dict) -> bool:
    for exclude in tool.get("exclude", []):
        text = re.sub(exclude, "", text, flags=re.I)
    return any(pattern_for(alias).search(text) for alias in tool["aliases"])


def searchable_markdown(text: str, tool: dict) -> str:
    if tool.get("markdown_title_only"):
        return "\n".join(text.splitlines()[:20])
    return text


def load_sessions() -> list[dict]:
    blob = json.loads((ROOT / "raw" / "sources" / "official-sessions.json").read_text())
    return blob.get("sessions", blob) if isinstance(blob, dict) else blob


def load_youtube_entries(path: Path) -> list[dict]:
    if not path.exists():
        return []
    blob = json.loads(path.read_text())
    return blob.get("entries", []) if isinstance(blob, dict) else []


def collect_evidence(tool: dict) -> dict:
    evidence = {
        "schedule": [],
        "youtube": [],
        "slides": [],
        "resources": [],
        "topics": [],
        "transcripts": [],
    }

    for session in load_sessions():
        haystack = "\n".join([session.get("title", ""), session.get("description", "")])
        if matches_any(haystack, tool):
            evidence["schedule"].append(session)

    for source in [
        ROOT / "raw" / "sources" / "aidotengineer-channel-videos-latest.json",
        ROOT / "raw" / "sources" / "aidotengineer-channel-streams-latest.json",
    ]:
        for entry in load_youtube_entries(source):
            title = entry.get("title", "")
            if matches_any(title, tool):
                evidence["youtube"].append({"title": title, "id": entry.get("id")})

    for folder, key in [(WIKI / "slides", "slides"), (WIKI / "resources", "resources"), (WIKI / "topics", "topics")]:
        for path in sorted(folder.glob("*.md")):
            text = path.read_text(errors="ignore")
            if matches_any(searchable_markdown(text, tool), tool):
                evidence[key].append(path)

    for folder in [ROOT / "raw" / "sources" / "youtube-transcripts", ROOT / "raw" / "sources" / "youtube-livestream-transcripts"]:
        if folder.exists():
            for path in sorted(folder.glob("*.txt")):
                text = path.read_text(errors="ignore")
                if matches_any(text, tool):
                    evidence["transcripts"].append(path)

    return evidence


def source_labels(evidence: dict) -> list[str]:
    labels = []
    if evidence["schedule"]:
        labels.append("Official schedule")
    if evidence["youtube"] or evidence["resources"]:
        labels.append("Public YouTube metadata")
    if evidence["transcripts"]:
        labels.append("Transcript evidence")
    if evidence["slides"]:
        labels.append("Local slide OCR")
    if evidence["topics"]:
        labels.append("Topic synthesis")
    return labels


def existing_frontmatter(text: str) -> dict[str, list[str] | str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fields: dict[str, list[str] | str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            try:
                fields[key.strip()] = json.loads(raw)
            except json.JSONDecodeError:
                fields[key.strip()] = []
        else:
            fields[key.strip()] = raw.strip().strip('"')
    return fields


def preserve_existing_tool_page(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(errors="ignore")
    fields = existing_frontmatter(text)
    if fields.get("highlighted") == "true" or fields.get("highlightPriority"):
        return True
    manual_markers = ["## What It Is", "## Public Sources", "## Evidence Boundary"]
    return sum(1 for marker in manual_markers if marker in text) >= 2


def unique_values(values) -> list[str]:
    seen = set()
    out = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def schedule_tracks(evidence: dict) -> list[str]:
    return unique_values(session.get("track") for session in evidence["schedule"])


def schedule_rooms(evidence: dict) -> list[str]:
    return unique_values(session.get("room") for session in evidence["schedule"])


def page_link_for_session(session: dict) -> str:
    date = day_to_date(session.get("day", ""))
    slug = slugify(f"{date}-{session.get('speakers', [''])[0]}-{session.get('title', '')}") if session.get("speakers") else slugify(f"{date}-{session.get('title', '')}")
    path = WIKI / "talks" / f"{slug}.md"
    if not path.exists():
        matches = list((WIKI / "talks").glob(f"*{slugify(session.get('title', ''))[:60]}*.md"))
        path = matches[0] if matches else path
    return f"[[{path.stem}]]"


def day_to_date(day: str) -> str:
    if "June 28" in day or "Day 0" in day:
        return "2026-06-28"
    if "June 29" in day or "Day 1" in day:
        return "2026-06-29"
    if "June 30" in day or "Day 2" in day:
        return "2026-06-30"
    if "July 1" in day or "Day 3" in day:
        return "2026-07-01"
    if "July 2" in day or "Day 4" in day:
        return "2026-07-02"
    return "2026-06-29"


def evidence_strength(evidence: dict) -> int:
    return sum(min(len(items), 5) for items in evidence.values())


def render_tool_page(tool: dict, evidence: dict) -> str:
    labels = source_labels(evidence)
    body = [
        frontmatter(
            {
                "title": tool["title"],
                "category": "tools",
                "aliases": tool["aliases"],
                "sourceLabels": labels,
                "scheduleTracks": schedule_tracks(evidence),
                "scheduleRooms": schedule_rooms(evidence),
            }
        ),
        f"# {tool['title']}",
        "",
        "## Why It Belongs",
        f"{tool['title']} appears as a high-confidence tool, platform, model, protocol, product, or service in the AI Engineer World's Fair 2026 corpus.",
        "",
        "This page records confirmed mentions and keeps them separate from broader inferred relevance.",
        "",
        "## Confirmed Evidence",
    ]

    if evidence["schedule"]:
        body.extend(["", "### Official Schedule"])
        for session in evidence["schedule"][:10]:
            body.append(
                f"- {page_link_for_session(session)} — {session.get('title')} "
                f"({session.get('track') or 'track TBD'} / {session.get('room') or 'room TBD'})"
            )

    if evidence["youtube"]:
        body.extend(["", "### Public YouTube Metadata"])
        for item in evidence["youtube"][:10]:
            if item.get("id"):
                body.append(f"- [YouTube {item['id']}](https://www.youtube.com/watch?v={item['id']}) — {item['title']}")
            else:
                body.append(f"- {item['title']}")

    if evidence["resources"]:
        body.extend(["", "### Resource Pages"])
        for path in evidence["resources"][:10]:
            body.append(f"- [[{path.stem}]]")

    if evidence["slides"]:
        body.extend(["", "### Slide/OCR Pages"])
        for path in evidence["slides"][:10]:
            body.append(f"- [[{path.stem}]]")

    if evidence["topics"]:
        body.extend(["", "### Topic Pages"])
        for path in evidence["topics"][:10]:
            body.append(f"- [[{path.stem}]]")

    if evidence["transcripts"]:
        body.extend(["", "### Transcript Files"])
        for path in evidence["transcripts"][:10]:
            body.append(f"- `{path.relative_to(ROOT)}`")

    body.extend(
        [
            "",
            "## Confidence",
            "High confidence for presence in the corpus. Interpret broader importance through the linked schedule, transcript, slide, and topic evidence.",
        ]
    )
    return "\n".join(body)


def render_index(records: list[dict]) -> str:
    lines = [
        frontmatter({"title": "Tools", "category": "tools"}),
        "# Tools",
        "",
        "This category indexes software, models, frameworks, protocols, devices, and services that appear in the AI Engineer World's Fair 2026 corpus.",
        "",
        "Tool pages distinguish confirmed mentions from inferred relevance and cite the source layer for each claim.",
        "",
        "## Inventory",
    ]
    for record in records:
        labels = ", ".join(record["sourceLabels"])
        lines.append(f"- [[{record['id']}]] — {record['title']} ({labels})")
    return "\n".join(lines)


def main() -> int:
    records = []
    for tool in TOOLS:
        evidence = collect_evidence(tool)
        if evidence_strength(evidence) < 1:
            continue
        labels = source_labels(evidence)
        path = WIKI / "tools" / f"{tool['slug']}.md"
        existing_fields: dict[str, list[str] | str] = {}
        if preserve_existing_tool_page(path):
            existing_fields = existing_frontmatter(path.read_text(errors="ignore"))
            labels = existing_fields.get("sourceLabels", labels) if isinstance(existing_fields.get("sourceLabels"), list) else labels
        else:
            path.write_text(render_tool_page(tool, evidence).rstrip() + "\n")
        records.append(
            {
                "id": tool["slug"],
                "title": tool["title"],
                "path": f"wiki/tools/{tool['slug']}.md",
                "aliases": tool["aliases"],
                "sourceLabels": labels,
                "scheduleTracks": existing_fields.get("scheduleTracks", schedule_tracks(evidence))
                if isinstance(existing_fields.get("scheduleTracks"), list)
                else schedule_tracks(evidence),
                "scheduleRooms": existing_fields.get("scheduleRooms", schedule_rooms(evidence))
                if isinstance(existing_fields.get("scheduleRooms"), list)
                else schedule_rooms(evidence),
                "evidenceCounts": {key: len(value) for key, value in evidence.items()},
            }
        )

    records.sort(key=lambda item: item["title"].lower())
    (WIKI / "tools" / "registry.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    index_text = render_index(records).rstrip() + "\n"
    (WIKI / "tools" / "index.md").write_text(index_text)
    (WIKI / "tools" / "tools.md").write_text(index_text)
    print(json.dumps({"tool_pages": len(records)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
