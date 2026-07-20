"""Dependency-free reconciliation for slide-derived topic/session projections."""

from __future__ import annotations

import re
from pathlib import Path


SLIDE_DECK_TARGET = re.compile(r"youtube-[A-Za-z0-9_-]{11}-slides")


def markdown_section(text: str, heading: str) -> str | None:
    match = re.search(
        rf"\n## {re.escape(heading)}\n(.*?)(?=\n## |\Z)", text, re.S
    )
    return match.group(1) if match else None


def replace_markdown_section(text: str, heading: str, body: str | None) -> str:
    pattern = re.compile(rf"\n## {re.escape(heading)}\n.*?(?=\n## |\Z)", re.S)
    if body is None:
        return pattern.sub("", text).rstrip() + "\n"
    block = f"\n## {heading}\n{body.rstrip()}\n"
    if pattern.search(text):
        return pattern.sub(lambda _match: block, text)
    return text.rstrip() + block


def session_identifier(session: dict) -> str:
    return str(session.get("slug") or session.get("id") or "").strip()


def reconcile_topic_slide_session_signals(
    talks: list[dict],
    *,
    slides_dir: Path,
    topics_dir: Path,
    write: bool,
) -> list[Path]:
    """Rebuild only slide-owned topic/session edges from every listed deck."""

    talks_by_slug = {
        session_identifier(talk): talk
        for talk in talks
        if session_identifier(talk)
    }
    changed: list[Path] = []
    for topic_path in sorted(topics_dir.glob("*.md")):
        current = topic_path.read_text(encoding="utf-8")
        deck_section = markdown_section(current, "Slide-Derived Supporting Decks")
        if deck_section is None:
            continue
        deck_targets: list[str] = []
        for raw_target in re.findall(r"\[\[([^\]]+)", deck_section):
            target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
            if SLIDE_DECK_TARGET.fullmatch(target) and target not in deck_targets:
                deck_targets.append(target)

        expected: dict[str, dict] = {}
        for target in deck_targets:
            slide_page = slides_dir / f"{target}.md"
            if not slide_page.exists():
                raise ValueError(
                    f"topic {topic_path.stem} references missing slide page: {target}"
                )
            session_section = markdown_section(
                slide_page.read_text(encoding="utf-8"),
                "Related Scheduled Sessions",
            )
            if session_section is None:
                raise ValueError(
                    f"slide page {target} has no Related Scheduled Sessions section"
                )
            for raw_slug in re.findall(r"\[\[([^\]]+)", session_section):
                slug = raw_slug.split("|", 1)[0].split("#", 1)[0].strip()
                talk = talks_by_slug.get(slug)
                if talk is None:
                    raise ValueError(
                        f"slide page {target} references missing talk: {slug}"
                    )
                expected[slug] = talk

        lines = sorted(
            (
                f"- [[{slug}]] — {talk.get('title') or slug}"
                for slug, talk in expected.items()
            ),
            key=str.casefold,
        )
        rendered = replace_markdown_section(
            current,
            "Slide-Derived Scheduled Session Signals",
            "\n".join(lines) if lines else None,
        )
        if rendered == current:
            continue
        changed.append(topic_path)
        if write:
            topic_path.write_text(rendered, encoding="utf-8")
    return changed
