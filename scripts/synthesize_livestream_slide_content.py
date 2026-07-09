#!/usr/bin/env python3
"""Turn livestream dense-slide OCR into readable resource/topic support."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sources"
WIKI = ROOT / "wiki"
RESOURCES = WIKI / "resources"
TOPICS = WIKI / "topics"
SLIDES = WIKI / "slides"


INSIGHT_RULES = [
    {
        "topics": ["agent-evaluations", "inference-engineering"],
        "needles": ["choosing a model", "accuracy/quality", "quality dominates", "model for production"],
        "summary": "Model selection is framed as a production tradeoff where accuracy and output quality dominate, with agentic capabilities, cost, privacy controls, reliability, enterprise support, latency, fine-tuning, and open weights as secondary considerations.",
    },
    {
        "topics": ["agent-evaluations", "coding-agents"],
        "needles": ["rlpipeline", "anomaly", "self-healing", "remediation", "validate"],
        "summary": "The stream includes an end-to-end RL pipeline pattern for self-healing data workflows: observe logs/schema/data quality, diagnose the likely failure family, estimate operational risk, choose a bounded remediation, and validate recovery.",
    },
    {
        "topics": ["agent-security", "agent-evaluations"],
        "needles": ["safetyoverride", "critical anomaly", "passive action", "escalate"],
        "summary": "The anomaly-remediation slide treats safety override as part of the intelligence layer, escalating high-risk anomalies instead of letting an agent blindly act.",
    },
    {
        "topics": ["agent-memory", "coding-agents"],
        "needles": ["one conversation has to do everything", "contextwindow", "database", "file system", "reasoningspace"],
        "summary": "One slide names a common agent design failure: forcing one conversation/context window to act as database, filesystem, memory, and reasoning space at once.",
    },
    {
        "topics": ["agent-memory"],
        "needles": ["narrative state", "worldmood", "attitude inference", "world remembers"],
        "summary": "A memory-oriented game-agent slide argues for tracking narrative state and attitude rather than brittle numeric state when the model is better at qualitative continuity.",
    },
    {
        "topics": ["agent-memory", "inference-engineering"],
        "needles": ["hiddenrambill", "kv cache", "short-term", "memory", "context length"],
        "summary": "The KV-cache slide makes context memory concrete: every token an agent reads or writes creates cached state, so long-context agents can carry a hidden RAM bill that grows into tens of gigabytes.",
    },
    {
        "topics": ["inference-engineering"],
        "needles": ["turboquant", "3to4bits", "embeddings", "kvcache", "polarquant"],
        "summary": "TurboQuant is presented as a compression approach for embeddings and KV cache, using low-bit storage to reduce memory pressure without retraining.",
    },
    {
        "topics": ["coding-agents", "ai-sandboxes"],
        "needles": ["whatpeoplethinktheagentis", "runtime/sandbox", "tools", "loop", "framework"],
        "summary": "The agent-architecture slide separates the agent from any single model: the production agent also includes runtime or sandbox, tools, loop, and framework.",
    },
    {
        "topics": ["coding-agents", "agent-memory"],
        "needles": ["simplifiedloop", "reconstruct_from_log", "append(result)", "session_has_work"],
        "summary": "The simplified loop slide shows a log-reconstructable agent pattern: rebuild state from the session log, ask the model for the next step, append model/tool results, and continue.",
    },
]


def read_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(errors="ignore"))


def upsert_section(path: Path, heading: str, body: str) -> bool:
    text = path.read_text(errors="ignore") if path.exists() else ""
    block = f"\n\n## {heading}\n{body.rstrip()}\n"
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        next_text = pattern.sub(block, text)
    else:
        next_text = text.rstrip() + block
    if next_text != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(next_text.rstrip() + "\n", encoding="utf-8")
        return True
    return False


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def slide_blocks(page: Path) -> list[dict]:
    text = page.read_text(errors="ignore")
    chunks = re.split(r"\n(?=!\[\[assets/dense-slides/)", text)
    blocks = []
    for chunk in chunks:
        image_match = re.search(r"!\[\[(assets/dense-slides/[^]]+)\]\]", chunk)
        if not image_match:
            continue
        lines = [line[2:].strip() for line in chunk.splitlines() if line.startswith("> ")]
        ocr = "\n".join(lines).strip()
        blocks.append({"image": image_match.group(1), "ocr": ocr, "normalized": normalize(ocr)})
    return blocks


def infer_insights(blocks: list[dict]) -> list[dict]:
    insights = []
    seen = set()
    for block in blocks:
        hay = block["normalized"]
        for rule in INSIGHT_RULES:
            if any(normalize(needle) in hay for needle in rule["needles"]):
                key = rule["summary"]
                if key in seen:
                    continue
                seen.add(key)
                insights.append({**rule, "image": block["image"]})
    return insights


def livestream_rows() -> list[dict]:
    audit = read_json(RAW / "livestream-corpus-audit.json", {})
    rows = audit.get("streams") or []
    return [row for row in rows if row.get("year") == "2026" and row.get("worldsfair")]


def resource_body(video_id: str, insights: list[dict]) -> str:
    lines = [
        "Dense slide OCR adds the following content signals. Treat these as reviewed summaries of slide evidence, with the linked slide page remaining the visual source of truth.",
        "",
        f"- Dense slide deck: [[youtube-{video_id}-dense-slides]]",
        f"- Standard frame deck: [[youtube-{video_id}-slides]]",
    ]
    for insight in insights:
        topics = ", ".join(f"[[{topic}]]" for topic in insight["topics"])
        lines.append(f"- {insight['summary']} Related topics: {topics}.")
    return "\n".join(lines)


def topic_body(topic: str, items: list[dict]) -> str:
    lines = [
        "Livestream slide OCR provides supporting evidence for this topic. These notes are source-linked summaries; inspect the dense slide pages before treating OCR text as exact wording.",
    ]
    for item in items:
        lines.append(f"- [[youtube-{item['video_id']}]] / [[youtube-{item['video_id']}-dense-slides]]: {item['summary']}")
    return "\n".join(lines)


def main() -> int:
    topic_items: dict[str, list[dict]] = defaultdict(list)
    updated_resources = 0
    processed = []
    for row in livestream_rows():
        video_id = row["video_id"]
        dense_page = SLIDES / f"youtube-{video_id}-dense-slides.md"
        if not dense_page.exists():
            continue
        insights = infer_insights(slide_blocks(dense_page))
        if not insights:
            continue
        if upsert_section(RESOURCES / f"youtube-{video_id}.md", "Slide-Derived Content Notes", resource_body(video_id, insights)):
            updated_resources += 1
        for insight in insights:
            for topic in insight["topics"]:
                topic_items[topic].append({"video_id": video_id, "summary": insight["summary"]})
        processed.append({"video_id": video_id, "insights": len(insights)})

    updated_topics = 0
    for topic, items in sorted(topic_items.items()):
        path = TOPICS / f"{topic}.md"
        if path.exists() and upsert_section(path, "Livestream Slide Support", topic_body(topic, items)):
            updated_topics += 1

    report = {
        "processed": processed,
        "updated_resources": updated_resources,
        "updated_topics": updated_topics,
    }
    (RAW / "livestream-slide-content-synthesis.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
