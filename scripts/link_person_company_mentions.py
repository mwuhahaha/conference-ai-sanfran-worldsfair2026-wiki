#!/usr/bin/env python3
"""Link employer/company mentions in person articles to company pages."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str, dict[str, str]]:
    if not text.startswith("---\n"):
        return "", text, {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return text[: end + 5], text[end + 5 :].lstrip(), fields


def title_of(path: Path) -> str:
    _fm, body, fields = split_frontmatter(read(path))
    if fields.get("title"):
        return fields["title"]
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else path.stem.replace("-", " ").title()


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return re.sub(r"-+", "-", value)


def company_registry() -> tuple[dict[str, str], list[tuple[str, str]]]:
    by_key: dict[str, str] = {}
    aliases: list[tuple[str, str]] = []
    for path in sorted((WIKI / "companies").glob("*.md")):
        if path.name == "index.md":
            continue
        title = title_of(path)
        slug = path.stem
        for key in {title, slug.replace("-", " "), slug}:
            clean = key.strip()
            if clean:
                by_key[clean.lower()] = slug
        if len(title) > 2:
            aliases.append((title, slug))
    aliases.sort(key=lambda item: len(item[0]), reverse=True)
    return by_key, aliases


def company_names_from_field(raw: str, by_key: dict[str, str]) -> list[tuple[str, str]]:
    names: list[tuple[str, str]] = []
    raw = raw.strip()
    candidates = [raw]
    candidates.extend(part.strip() for part in re.split(r"\s+/\s+", raw) if part.strip())
    for candidate in candidates:
        slug = by_key.get(candidate.lower())
        if not slug:
            fallback = slugify(candidate)
            slug = fallback if (WIKI / "companies" / f"{fallback}.md").exists() else ""
        if slug:
            names.append((candidate, slug))
    return dedupe_pairs(names)


def dedupe_pairs(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen = set()
    out = []
    for name, slug in pairs:
        key = (name.lower(), slug)
        if key in seen:
            continue
        seen.add(key)
        out.append((name, slug))
    return out


def protected_spans(line: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    patterns = [
        r"\[\[[^\]]+\]\]",
        r"\[[^\]]+\]\([^)]+\)",
        r"`[^`]+`",
        r"https?://\S+",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, line):
            spans.append(match.span())
    spans.sort()
    return spans


def in_span(index: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= index < end for start, end in spans)


def link_name_in_line(line: str, name: str, slug: str) -> tuple[str, int]:
    if not name:
        return line, 0
    pattern = re.compile(rf"(?<![\w/-]){re.escape(name)}(?![\w/-])")
    pieces: list[str] = []
    last = 0
    count = 0
    spans = protected_spans(line)
    for match in pattern.finditer(line):
        if in_span(match.start(), spans):
            continue
        pieces.append(line[last : match.start()])
        pieces.append(f"[[{slug}|{match.group(0)}]]")
        last = match.end()
        count += 1
    if not count:
        return line, 0
    pieces.append(line[last:])
    return "".join(pieces), count


def unlink_company_links_in_session_line(line: str, company_slugs: set[str]) -> tuple[str, int]:
    if not line.startswith("- [["):
        return line, 0

    def replace(match: re.Match[str]) -> str:
        slug = match.group(1)
        label = match.group(2)
        return label if slug in company_slugs else match.group(0)

    new_line = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", replace, line)
    return new_line, int(new_line != line)


def link_people_page(path: Path, by_key: dict[str, str], aliases: list[tuple[str, str]], all_companies: bool) -> int:
    text = read(path)
    fm, body, fields = split_frontmatter(text)
    targets = company_names_from_field(fields.get("company", ""), by_key)
    if all_companies:
        lowered = body.lower()
        for title, slug in aliases:
            if title.lower() in lowered:
                targets.append((title, slug))
        targets = dedupe_pairs(targets)
    if not targets:
        return 0

    changed = 0
    in_fence = False
    lines = []
    company_slugs = {slug for _name, slug in targets}
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            lines.append(line)
            continue
        if in_fence:
            lines.append(line)
            continue
        new_line, cleanup_count = unlink_company_links_in_session_line(line, company_slugs)
        if line.startswith("- [["):
            changed += cleanup_count
            lines.append(new_line)
            continue
        new_line = line
        for name, slug in sorted(targets, key=lambda item: len(item[0]), reverse=True):
            new_line, count = link_name_in_line(new_line, name, slug)
            changed += count
        lines.append(new_line)
    if changed:
        write(path, fm + "\n".join(lines))
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-companies", action="store_true", help="Also link known company names found in the body, not just the declared company field.")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    by_key, aliases = company_registry()
    paths = sorted(p for p in (WIKI / "people").glob("*.md") if p.name != "index.md")
    if args.limit:
        paths = paths[: args.limit]
    changed_pages = 0
    replacements = 0
    for path in paths:
        count = link_people_page(path, by_key, aliases, args.all_companies)
        if count:
            changed_pages += 1
            replacements += count
    print(json.dumps({"processed": len(paths), "changed_pages": changed_pages, "links_added": replacements}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
