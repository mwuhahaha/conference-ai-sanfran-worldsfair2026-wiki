#!/usr/bin/env python3
"""Export the World's Fair wiki as a static Cloudflare Pages site."""

from __future__ import annotations

import html
import hashlib
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw" / "sources"
DIST = ROOT / "dist"
SITE_TITLE = "AI Engineer World's Fair 2026 Wiki"
SITE_SUBTITLE = "Standalone conference intelligence wiki for AI Engineer World's Fair 2026."
ASSET_VERSION = (os.environ.get("GITHUB_SHA") or "local-dev")[:12]
PREFERRED_CATEGORIES = [
    "talks",
    "slides",
    "people",
    "companies",
    "topics",
    "highlights",
    "claims",
    "conversations",
    "patterns",
    "questions",
    "harnesses",
    "playbooks",
    "evaluations",
    "resources",
    "transcripts",
    "events",
]


@dataclass
class Page:
    id: str
    source: Path
    title: str
    category: str
    body: str
    excerpt: str

    @property
    def url(self) -> str:
        if self.id == "overview":
            return "/"
        return f"/{self.id}/"

    @property
    def markdown_url(self) -> str:
        return f"/md/{self.id}.md"


def parse_page(path: Path) -> Page:
    raw = path.read_text(encoding="utf-8")
    frontmatter: dict[str, str] = {}
    body = raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end != -1:
            for line in raw[4:end].splitlines():
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip().strip('"')
            body = raw[end + 5 :]

    rel = path.relative_to(WIKI).with_suffix("")
    page_id = rel.as_posix()
    title = frontmatter.get("title") or first_heading(body) or titleize(path.stem)
    category = frontmatter.get("category") or (rel.parts[0] if len(rel.parts) > 1 else "root")
    excerpt = build_excerpt(body)
    return Page(id=page_id, source=path, title=title, category=category, body=body.strip(), excerpt=excerpt)


def first_heading(markdown: str) -> str:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+)$", line.strip())
        if match:
            return clean_inline(match.group(1))
    return ""


def build_excerpt(markdown: str) -> str:
    body = re.sub(r"```.*?```", " ", markdown, flags=re.S)
    body = re.sub(r"!\[\[[^\]]+\]\]", " ", body)
    body = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), body)
    body = re.sub(r"^#+\s+", "", body, flags=re.M)
    body = re.sub(r"[*_`>#|\-\[\]():]", " ", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body[:220]


def titleize(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("-", " ").replace("_", " ")).strip().title()


def clean_inline(value: str) -> str:
    return re.sub(r"[*_`]", "", value).strip()


def page_output_path(page: Page) -> Path:
    if page.id == "overview":
        return DIST / "index.html"
    return DIST / page.id / "index.html"


def page_markdown_output_path(page: Page) -> Path:
    return DIST / "md" / f"{page.id}.md"


def is_category_index(page: Page) -> bool:
    return page.category != "root" and page.source.name in {"index.md", f"{page.category}.md"}


def is_public_category_content(page: Page) -> bool:
    return page.category != "root" and not is_category_index(page)


def public_categories(pages: list[Page]) -> list[str]:
    return sorted({page.category for page in pages if is_public_category_content(page)}, key=category_sort_key)


def build_link_maps(pages: list[Page]) -> tuple[dict[str, Page], dict[str, Page]]:
    by_id = {page.id: page for page in pages}
    by_stem: dict[str, Page] = {}
    for page in pages:
        by_stem.setdefault(Path(page.id).name, page)
    return by_id, by_stem


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def entry_count(blob) -> int | str:
    if isinstance(blob, list):
        return len(blob)
    if isinstance(blob, dict):
        for key in ("sessions", "speakers", "entries", "results"):
            if isinstance(blob.get(key), list):
                return len(blob[key])
    return "unknown"


def count_files(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    return len(list(path.glob(pattern)))


def resolve_wikilink(target: str, by_id: dict[str, Page], by_stem: dict[str, Page]) -> str | None:
    page = resolve_wikilink_page(target, by_id, by_stem)
    return page.url if page else None


def resolve_wikilink_page(target: str, by_id: dict[str, Page], by_stem: dict[str, Page]) -> Page | None:
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    return by_id.get(target) or by_stem.get(Path(target).name)


def extract_graph(pages: list[Page], by_id: dict[str, Page], by_stem: dict[str, Page]) -> dict[str, list[dict]]:
    graph_pages = [page for page in pages if not is_category_index(page)]
    graph_page_ids = {page.id for page in graph_pages}
    outgoing: dict[str, set[str]] = {page.id: set() for page in graph_pages}
    backlinks: dict[str, set[str]] = {page.id: set() for page in graph_pages}

    for page in graph_pages:
        for raw_target in re.findall(r"(?<!!)\[\[([^\]]+)\]\]", page.body):
            target = raw_target.split("|", 1)[0]
            linked = resolve_wikilink_page(target, by_id, by_stem)
            if not linked or linked.id == page.id or linked.id not in graph_page_ids:
                continue
            outgoing[page.id].add(linked.id)
            backlinks[linked.id].add(page.id)

    nodes = []
    for page in graph_pages:
        nodes.append(
            {
                "id": page.id,
                "title": page.title,
                "category": page.category,
                "url": page.url,
                "excerpt": page.excerpt,
                "outgoingCount": len(outgoing[page.id]),
                "backlinkCount": len(backlinks[page.id]),
                "degree": len(outgoing[page.id] | backlinks[page.id]),
            }
        )

    links = [
        {"source": source, "target": target}
        for source in sorted(outgoing)
        for target in sorted(outgoing[source])
    ]
    return {"nodes": nodes, "links": links}


def render_inline(text: str, by_id: dict[str, Page], by_stem: dict[str, Page]) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def image_embed(match: re.Match[str]) -> str:
        target = match.group(1).split("|", 1)[0].strip()
        src = "/" + target.removeprefix("wiki/").removeprefix("/")
        alt = Path(target).name
        return stash(f'<img class="wiki-image" src="{html.escape(src)}" alt="{html.escape(alt)}" loading="lazy">')

    def wikilink(match: re.Match[str]) -> str:
        raw = match.group(1)
        target, _, label = raw.partition("|")
        label = label or Path(target).name.replace("-", " ")
        href = resolve_wikilink(target, by_id, by_stem)
        if href:
            return stash(f'<a href="{html.escape(href)}">{html.escape(label)}</a>')
        return html.escape(label)

    def markdown_link(match: re.Match[str]) -> str:
        label, href = match.group(1), match.group(2)
        return stash(f'<a href="{html.escape(href)}">{html.escape(label)}</a>')

    text = re.sub(r"!\[\[([^\]]+)\]\]", image_embed, text)
    text = re.sub(r"\[\[([^\]]+)\]\]", wikilink, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", markdown_link, text)
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    for index, value in enumerate(placeholders):
        escaped = escaped.replace(f"\u0000{index}\u0000", value)
    return escaped


def render_markdown(markdown: str, by_id: dict[str, Page], by_stem: dict[str, Page]) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    in_code = False
    code_lines: list[str] = []
    in_list = False
    in_quote = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(f"<p>{render_inline(' '.join(paragraph), by_id, by_stem)}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append("</ul>")
            in_list = False

    def close_quote() -> None:
        nonlocal in_quote
        if in_quote:
            output.append("</blockquote>")
            in_quote = False

    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith("```"):
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_paragraph()
                close_list()
                close_quote()
                in_code = True
            continue
        if in_code:
            code_lines.append(stripped)
            continue
        if not stripped:
            flush_paragraph()
            close_list()
            close_quote()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            close_quote()
            level = len(heading.group(1))
            output.append(f"<h{level}>{render_inline(heading.group(2), by_id, by_stem)}</h{level}>")
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            close_list()
            close_quote()
            output.append(f'<pre class="table-fallback">{html.escape(stripped)}</pre>')
            continue
        if stripped.startswith(">"):
            flush_paragraph()
            close_list()
            if not in_quote:
                output.append("<blockquote>")
                in_quote = True
            output.append(f"<p>{render_inline(stripped.lstrip('> ').strip(), by_id, by_stem)}</p>")
            continue
        item = re.match(r"^[-*]\s+(.+)$", stripped)
        if item:
            flush_paragraph()
            close_quote()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{render_inline(item.group(1), by_id, by_stem)}</li>")
            continue
        paragraph.append(stripped)

    flush_paragraph()
    close_list()
    close_quote()
    if in_code:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(output)


def category_sort_key(category: str) -> tuple[int, str]:
    if category in PREFERRED_CATEGORIES:
        return (PREFERRED_CATEGORIES.index(category), category)
    return (len(PREFERRED_CATEGORIES), category)


def render_layout(title: str, body: str, pages: list[Page], current: str = "") -> str:
    nav_items = []
    for category in public_categories(pages):
        active = ' class="active"' if current == category else ""
        nav_items.append(f'<a href="/{category}/"{active}>{html.escape(titleize(category))}</a>')
    nav = "\n".join(nav_items)
    home_active = ' class="active"' if current == "overview" else ""
    index_active = ' class="active"' if current == "index" else ""
    graph_active = ' class="active"' if current == "graph" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · {html.escape(SITE_TITLE)}</title>
  <link rel="stylesheet" href="/styles.css?v={html.escape(ASSET_VERSION)}">
</head>
<body class="page-{html.escape(current or 'article')}">
  <aside class="sidebar">
    <p class="eyebrow">AI Engineer Conference Wiki</p>
    <a class="brand" href="/">{html.escape(SITE_TITLE)}</a>
    <p class="subtitle">{html.escape(SITE_SUBTITLE)}</p>
    <nav class="main-nav">
      <a href="/"{home_active}>Home</a>
      <a href="/index/"{index_active}>Index</a>
      <a href="/graph/"{graph_active}>Graph</a>
      {nav}
    </nav>
    <form class="search" action="/search/" method="get">
      <label for="q">Search</label>
      <input id="q" name="q" type="search" placeholder="Search pages">
    </form>
  </aside>
  <main>
    {body}
  </main>
</body>
</html>
"""


def render_page(page: Page, pages: list[Page], by_id: dict[str, Page], by_stem: dict[str, Page]) -> str:
    if page.id == "overview":
        return render_home(page, pages, by_id, by_stem)
    body = f"""<article class="page">
  <p class="page-tools"><a href="{html.escape(page.markdown_url)}">Markdown source</a></p>
  {render_markdown(page.body, by_id, by_stem)}
</article>"""
    return render_layout(page.title, body, pages, page.category if page.category != "root" else page.id)


def render_home(page: Page, pages: list[Page], by_id: dict[str, Page], by_stem: dict[str, Page]) -> str:
    category_counts = {
        category: len([item for item in pages if item.category == category and not is_category_index(item)])
        for category in {item.category for item in pages}
    }
    graph = extract_graph(pages, by_id, by_stem)
    sessions = load_json(RAW / "official-sessions.json", {})
    speakers = load_json(RAW / "official-speakers.json", {})
    videos = load_json(RAW / "aidotengineer-channel-videos-latest.json", [])
    streams = load_json(RAW / "aidotengineer-channel-streams-latest.json", [])
    related_videos = load_json(RAW / "speaker-video-map.json", [])
    livestream_segments = load_json(RAW / "livestream-talk-segments.json", [])
    external_discovery = load_json(RAW / "external-video-discovery-latest.json", {})

    stats = [
        ("Schedule sessions", entry_count(sessions), "/talks/"),
        ("Speakers", entry_count(speakers), "/people/"),
        ("Companies", category_counts.get("companies", 0), "/companies/"),
        ("Talk/video rows", entry_count(related_videos), "/resources/talk-video-transcript-map/"),
        ("Transcript pages", category_counts.get("transcripts", 0), "/transcripts/"),
        ("Slide pages", category_counts.get("slides", 0), "/slides/"),
        ("Topics", category_counts.get("topics", 0), "/topics/"),
        ("Graph links", f"{len(graph['links']):,}", "/graph/"),
    ]
    stats_html = "\n".join(
        f"""<a class="home-metric" href="{url}">
  <strong>{html.escape(str(value))}</strong>
  <span>{html.escape(label)}</span>
</a>"""
        for label, value, url in stats
    )

    event_pages = sorted([item for item in pages if item.category == "events"], key=lambda item: item.id)
    event_card_items = []
    for event in event_pages:
        linked_count = len(re.findall(r"(?<!!)\[\[([^\]]+)\]\]", event.body))
        event_card_items.append(
            f"""<a class="home-row" href="{event.url}">
  <span class="home-row-kicker">{event.id.split('/', 1)[-1][:10]}</span>
  <strong>{html.escape(event.title)}</strong>
  <span>{linked_count} linked sessions or sources</span>
  <span class="home-row-arrow" aria-hidden="true">Open →</span>
</a>"""
        )
    event_cards = "\n".join(event_card_items)

    source_layers = [
        ("Official schedule", f"{entry_count(sessions)} sessions and {entry_count(speakers)} roster speakers", "Dates, titles, speakers, organizations, rooms, tracks, and session status.", "/resources/official-sessions-json/"),
        ("AI Engineer media", f"{entry_count(videos)} channel videos and {entry_count(streams)} livestream rows", "Official channel uploads, livestream metadata, transcript status, and slide extraction outputs.", "/resources/worldsfair-2026-livestreams/"),
        ("Matched recordings", f"{entry_count(related_videos)} talk/video rows and {entry_count(livestream_segments)} livestream timestamp matches", "Speaker/title matching connects schedule pages to public recordings and transcript coverage.", "/resources/talk-video-transcript-map/"),
        ("Supporting discovery", f"{entry_count(external_discovery)} external video candidates", "External uploads remain secondary sources unless a page says otherwise.", "/resources/external-video-discovery/"),
        ("Cached transcripts", f"{count_files(RAW / 'youtube-transcripts', '*.txt')} cut-video, {count_files(RAW / 'youtube-livestream-transcripts', '*.txt')} livestream, {count_files(RAW / 'external-youtube-transcripts', '*.txt')} external", "Transcript pages are supporting evidence; important wording should be checked against the linked video/resource page.", "/transcripts/"),
        ("Synthesis layers", f"{category_counts.get('topics', 0)} topics, {category_counts.get('tools', 0)} tools, {category_counts.get('questions', 0)} questions", "Topic, tool, claim, pattern, harness, playbook, and evaluation pages summarize patterns across evidence.", "/topics/"),
    ]
    source_html = "\n".join(
        f"""<a class="home-row home-source-row" href="{url}">
  <span class="home-row-kicker">{html.escape(kicker)}</span>
  <strong>{html.escape(count)}</strong>
  <span>{html.escape(description)}</span>
  <span class="home-row-arrow" aria-hidden="true">Open →</span>
</a>"""
        for kicker, count, description, url in source_layers
    )

    primary_links = [
        ("Explore schedule", "/talks/", "Start from official sessions, speakers, tracks, rooms, and conference days."),
        ("Open graph", "/graph/", "See how talks, people, companies, tools, topics, quotes, and resources connect."),
        ("Check media", "/resources/talk-video-transcript-map/", "Audit which sessions have matched recordings, transcripts, livestream segments, or slides."),
        ("Use as agent", "/agent-index.md", "Give another agent a stable, read-only markdown contract for the public wiki."),
    ]
    links_html = "\n".join(
        f"""<a class="home-start-link" href="{html.escape(url)}">
  <strong>{html.escape(label)}</strong>
  <span>{html.escape(description)}</span>
  <em aria-hidden="true">Open →</em>
</a>"""
        for label, url, description in primary_links
    )

    body = f"""<section class="home-landing">
  <div class="home-hero-copy">
    <p class="page-tools"><a href="{html.escape(page.markdown_url)}">Markdown source</a></p>
    <p class="eyebrow">Static public wiki</p>
    <h1>AI Engineer World&apos;s Fair 2026</h1>
    <p class="home-deck">A public, read-only intelligence map for AI Engineer World&apos;s Fair 2026 in San Francisco. It starts with the official schedule, then layers in public recordings, transcripts, slides, topics, tools, source notes, and cross-page links so readers and agents can inspect the conference without guessing where evidence came from.</p>
    <div class="home-intro">
      <p>Use this as a navigation surface, not a polished news article. The schedule and roster are the primary layer; media and synthesis pages are supporting layers that should point back to concrete sources.</p>
      <p>The fastest paths are below: schedule for the program, graph for relationships, media map for transcript/video coverage, and agent index for a single markdown entry point.</p>
    </div>
  </div>
  <dl class="home-facts">
    <div><dt>When</dt><dd>June 28-July 2, 2026</dd></div>
    <div><dt>Where</dt><dd>Moscone West, San Francisco</dd></div>
    <div><dt>Core source</dt><dd>Official schedule and speaker roster</dd></div>
    <div><dt>Contract</dt><dd>Static, read-only, markdown-backed</dd></div>
  </dl>
  <div class="home-start">
    <p class="eyebrow">Start here</p>
    <div class="home-start-grid">{links_html}</div>
  </div>
</section>

<section class="home-split">
  <div class="home-panel home-boundary-panel">
    <p class="eyebrow">Source boundary</p>
    <h2>What is official?</h2>
    <ol class="home-boundary-list">
      <li><strong>Official schedule facts</strong> are dates, titles, speakers, organizations, rooms, tracks, and status.</li>
      <li><strong>Media evidence</strong> is supporting context from videos, livestreams, transcripts, slides, OCR, and external candidates.</li>
      <li><strong>Synthesis pages</strong> summarize patterns; follow their linked evidence before treating a claim as primary.</li>
    </ol>
  </div>
</section>

<section class="home-section home-stats-section">
  <div class="home-section-heading">
    <p class="eyebrow">Corpus</p>
    <h2>At a glance</h2>
  </div>
  <div class="home-metric-grid">{stats_html}</div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">Conference days</p>
    <h2>Day-level entry points</h2>
  </div>
  <div class="home-row-list">{event_cards}</div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">Source layers</p>
    <h2>What the wiki is built from</h2>
  </div>
  <div class="home-row-list">{source_html}</div>
</section>"""
    return render_layout(page.title, body, pages, "overview")


def render_category(category: str, category_pages: list[Page], all_pages: list[Page]) -> str:
    cards = "\n".join(
        f"""<a class="card" href="{page.url}">
  <strong>{html.escape(page.title)}</strong>
  <span>{html.escape(page.excerpt)}</span>
</a>"""
        for page in sorted(category_pages, key=lambda page: page.title.lower())
    )
    body = f"""<section class="landing">
  <p class="eyebrow">Category</p>
  <h1>{html.escape(titleize(category))}</h1>
  <p>{len(category_pages)} pages in this section.</p>
  <div class="card-grid">{cards}</div>
</section>"""
    return render_layout(titleize(category), body, all_pages, category)


def render_search(pages: list[Page]) -> str:
    index = [
        {"title": page.title, "url": page.url, "category": page.category, "excerpt": page.excerpt}
        for page in pages
        if not is_category_index(page)
    ]
    body = f"""<section class="landing">
  <p class="eyebrow">Search</p>
  <h1>Search the wiki</h1>
  <input id="search-input" class="search-input" type="search" placeholder="Type to filter pages" autofocus>
  <div id="search-results" class="card-grid"></div>
</section>
<script>
const pages = {json.dumps(index)};
const input = document.querySelector("#search-input");
const results = document.querySelector("#search-results");
function render() {{
  const q = input.value.trim().toLowerCase();
  const hits = pages.filter((page) => !q || [page.title, page.category, page.excerpt].join(" ").toLowerCase().includes(q)).slice(0, 100);
  results.innerHTML = hits.map((page) => `<a class="card" href="${{page.url}}"><strong>${{page.title}}</strong><small>${{page.category}}</small><span>${{page.excerpt || ""}}</span></a>`).join("");
}}
input.addEventListener("input", render);
render();
</script>"""
    return render_layout("Search", body, pages, "search")


def render_graph(pages: list[Page]) -> str:
    body = """<section class="landing graph-landing">
  <p class="eyebrow">Conference map</p>
  <h1>Knowledge graph</h1>
  <p class="graph-intro">Explore every wiki relationship in one view. Search highlights matching pages without removing the surrounding network.</p>
  <div class="graph-canvas-wrap">
    <div id="graph-canvas" class="graph-canvas" role="img" aria-label="Wiki relationship graph"></div>
    <div class="graph-controls" aria-label="Graph filters">
      <label>Category<select id="graph-category"><option value="">All categories</option></select></label>
      <label class="graph-search-label">Search<input id="graph-search" type="search" placeholder="Find a page by title or text" autocomplete="off"><span id="graph-search-results" class="graph-search-results"></span></label>
    </div>
    <div id="graph-legend" class="graph-legend" aria-label="Graph legend"></div>
    <div class="graph-zoom-controls" aria-label="Graph zoom controls">
      <button type="button" id="graph-zoom-in" title="Zoom in" aria-label="Zoom in">+</button>
      <button type="button" id="graph-zoom-out" title="Zoom out" aria-label="Zoom out">-</button>
      <button type="button" id="graph-zoom-reset" title="Show entire graph" aria-label="Show entire graph">All</button>
    </div>
    <p id="graph-status" class="graph-status" aria-live="polite">Loading graph…</p>
    <aside id="graph-detail" class="graph-detail">
      <p class="eyebrow">Node detail</p>
      <h2>Select a page</h2>
      <p>Choose a node to inspect its category, link counts, and nearby pages.</p>
    </aside>
  </div>
  <noscript><p>This interactive graph requires JavaScript. The underlying dataset remains available at <a href="/graph-data.json">/graph-data.json</a>.</p></noscript>
</section>
<script type="module" src="/graph.js?v=__ASSET_VERSION__"></script>"""
    graph_version = hashlib.sha256((DIST / "graph.js").read_bytes()).hexdigest()[:12]
    body = body.replace("__ASSET_VERSION__", graph_version)
    return render_layout("Knowledge graph", body, pages, "graph")


def write_graph_script() -> None:
    (DIST / "graph.js").write_text(
        r"""const SVG_NS = "http://www.w3.org/2000/svg";
const palette = ["#0f766e", "#9a3412", "#1d4ed8", "#7c3aed", "#be123c", "#4d7c0f", "#0369a1", "#a16207", "#475569", "#047857", "#c2410c", "#6d28d9"];
const categorySelect = document.querySelector("#graph-category");
const searchInput = document.querySelector("#graph-search");
const status = document.querySelector("#graph-status");
const legend = document.querySelector("#graph-legend");
const canvas = document.querySelector("#graph-canvas");
const detail = document.querySelector("#graph-detail");
const zoomIn = document.querySelector("#graph-zoom-in");
const zoomOut = document.querySelector("#graph-zoom-out");
const zoomReset = document.querySelector("#graph-zoom-reset");
let graph = { nodes: [], links: [] };
let colors = new Map();
let selectedNodeId = "";
let viewport = null;
let transform = { x: 0, y: 0, scale: 1 };
let drag = null;

function el(name, attrs = {}) {
  const node = document.createElementNS(SVG_NS, name);
  Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
  return node;
}

function graphSubset() {
  const category = categorySelect.value;
  const query = searchInput.value.trim().toLowerCase();
  const nodes = graph.nodes.filter((node) => {
    if (node.category === "root") return false;
    if (category && node.category !== category) return false;
    if (!query) return true;
    return `${node.title} ${node.category} ${node.excerpt}`.toLowerCase().includes(query);
  }).sort((a, b) => b.degree - a.degree || a.title.localeCompare(b.title));
  const ids = new Set(nodes.map((node) => node.id));
  const links = graph.links.filter((link) => ids.has(link.source) && ids.has(link.target));
  return { nodes, links, total: nodes.length };
}

function positions(nodes) {
  const grouped = new Map();
  nodes.forEach((node) => {
    if (!grouped.has(node.category)) grouped.set(node.category, []);
    grouped.get(node.category).push(node);
  });
  const categories = [...grouped.keys()].sort();
  const output = new Map();
  const singleCategory = categories.length === 1;
  const columns = singleCategory ? 1 : Math.min(4, Math.max(1, categories.length));
  const cellWidth = singleCategory ? 1040 : 280;
  const cellHeight = singleCategory ? 720 : 250;
  const startX = singleCategory ? 80 : 50;
  const startY = singleCategory ? 70 : 50;
  categories.forEach((category, categoryIndex) => {
    const col = categoryIndex % columns;
    const row = Math.floor(categoryIndex / columns);
    const centerX = startX + col * cellWidth + cellWidth / 2;
    const centerY = startY + row * cellHeight + cellHeight / 2;
    const items = grouped.get(category).sort((a, b) => b.degree - a.degree || a.title.localeCompare(b.title));
    items.forEach((node, index) => {
      const ring = Math.floor(Math.sqrt(index + 1));
      const itemAngle = index * 2.399963;
      const radius = singleCategory ? 18 + ring * 13 : 12 + ring * 12;
      output.set(node.id, {
        x: Math.max(startX + col * cellWidth + 18, Math.min(startX + (col + 1) * cellWidth - 18, centerX + Math.cos(itemAngle) * radius)),
        y: Math.max(startY + row * cellHeight + 34, Math.min(startY + (row + 1) * cellHeight - 18, centerY + Math.sin(itemAngle) * radius)),
      });
    });
  });
  return { points: output, grouped, columns, cellWidth, cellHeight, startX, startY };
}

function applyTransform() {
  if (!viewport) return;
  viewport.setAttribute("transform", `translate(${transform.x} ${transform.y}) scale(${transform.scale})`);
}

function setCategory(category) {
  categorySelect.value = category;
  selectedNodeId = "";
  const url = new URL(window.location.href);
  if (category) url.searchParams.set("category", category);
  else url.searchParams.delete("category");
  window.history.replaceState({}, "", url);
  resetZoom(false);
  render();
}

function zoomAt(factor, clientX = null, clientY = null) {
  const box = canvas.getBoundingClientRect();
  const px = clientX === null ? box.width / 2 : clientX - box.left;
  const py = clientY === null ? box.height / 2 : clientY - box.top;
  const svgX = px * 1200 / box.width;
  const svgY = py * 900 / box.height;
  const nextScale = Math.max(0.35, Math.min(5, transform.scale * factor));
  const ratio = nextScale / transform.scale;
  transform.x = svgX - (svgX - transform.x) * ratio;
  transform.y = svgY - (svgY - transform.y) * ratio;
  transform.scale = nextScale;
  applyTransform();
}

function resetZoom(apply = true) {
  transform = { x: 0, y: 0, scale: 1 };
  if (apply) applyTransform();
}

function showDetail(node) {
  selectedNodeId = node.id;
  const neighbors = new Map();
  graph.links.forEach((link) => {
    if (link.source === node.id) neighbors.set(link.target, "Outgoing");
    if (link.target === node.id && !neighbors.has(link.source)) neighbors.set(link.source, "Backlink");
  });
  const byId = new Map(graph.nodes.map((item) => [item.id, item]));
  const nearby = [...neighbors.entries()]
    .map(([id, direction]) => ({ ...byId.get(id), direction }))
    .filter((item) => item.id)
    .sort((a, b) => b.degree - a.degree || a.title.localeCompare(b.title))
    .slice(0, 18);
  detail.replaceChildren();
  const eyebrow = document.createElement("p");
  eyebrow.className = "eyebrow";
  eyebrow.textContent = node.category;
  const heading = document.createElement("h2");
  heading.textContent = node.title;
  const summary = document.createElement("p");
  summary.textContent = node.excerpt || "No excerpt available.";
  const counts = document.createElement("p");
  counts.className = "graph-counts";
  counts.textContent = `${node.outgoingCount} outgoing · ${node.backlinkCount} backlinks · ${node.degree} connected pages`;
  const open = document.createElement("a");
  open.className = "graph-open-page";
  open.href = node.url;
  open.textContent = "Open page";
  detail.append(eyebrow, heading, summary, counts, open);
  if (nearby.length) {
    const nearbyHeading = document.createElement("h3");
    nearbyHeading.textContent = "Nearby pages";
    const list = document.createElement("ul");
    list.className = "graph-nearby";
    nearby.forEach((item) => {
      const li = document.createElement("li");
      const link = document.createElement("a");
      link.href = item.url;
      link.textContent = item.title;
      const meta = document.createElement("small");
      meta.textContent = `${item.category} · ${item.direction}`;
      li.append(link, meta);
      list.append(li);
    });
    detail.append(nearbyHeading, list);
  }
}

function render() {
  const subset = graphSubset();
  const layout = positions(subset.nodes);
  const coords = layout.points;
  if (selectedNodeId && !subset.nodes.some((node) => node.id === selectedNodeId)) selectedNodeId = "";
  canvas.replaceChildren();
  viewport = el("g", { class: "graph-viewport" });
  const clustersGroup = el("g", { class: "graph-clusters" });
  [...layout.grouped.keys()].sort().forEach((category, index) => {
    const col = index % layout.columns;
    const row = Math.floor(index / layout.columns);
    const x = layout.startX + col * layout.cellWidth;
    const y = layout.startY + row * layout.cellHeight;
    clustersGroup.append(el("rect", { x, y, width: layout.cellWidth - 18, height: layout.cellHeight - 18, rx: "10" }));
    const label = el("text", { x: x + 13, y: y + 23 });
    label.textContent = `${category.replaceAll("-", " ")} (${layout.grouped.get(category).length})`;
    label.setAttribute("tabindex", "0");
    label.setAttribute("role", "button");
    label.setAttribute("aria-label", `Open ${category.replaceAll("-", " ")} graph`);
    label.addEventListener("click", () => setCategory(category));
    label.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") { event.preventDefault(); setCategory(category); }
    });
    clustersGroup.append(label);
  });
  viewport.append(clustersGroup);
  const linksGroup = el("g", { class: "graph-links" });
  const selectedLinks = selectedNodeId
    ? subset.links.filter((link) => link.source === selectedNodeId || link.target === selectedNodeId).slice(0, 80)
    : subset.links;
  selectedLinks.forEach((link) => {
    const source = coords.get(link.source);
    const target = coords.get(link.target);
    if (!source || !target) return;
    linksGroup.append(el("line", { x1: source.x, y1: source.y, x2: target.x, y2: target.y }));
  });
  viewport.append(linksGroup);
  const nodesGroup = el("g", { class: "graph-nodes" });
  const showLabels = Boolean(categorySelect.value || searchInput.value.trim()) || subset.nodes.length <= 220;
  subset.nodes.forEach((node) => {
    const point = coords.get(node.id);
    const group = el("g", { class: `graph-node${node.id === selectedNodeId ? " selected" : ""}`, tabindex: "0", role: "button", "aria-label": `${node.title}, ${node.category}` });
    group.append(el("circle", { cx: point.x, cy: point.y, r: Math.min(9, 4 + Math.sqrt(node.degree + 1) * 0.55), fill: colors.get(node.category) || "#64748b" }));
    if (showLabels || node.degree >= 35 || node.id === selectedNodeId) {
      const label = el("text", { x: point.x + 9, y: point.y + 4, class: "graph-node-label" });
      label.textContent = node.title.length > 44 ? `${node.title.slice(0, 41)}...` : node.title;
      label.addEventListener("click", (event) => { event.stopPropagation(); selectedNodeId = node.id; render(); showDetail(node); });
      group.append(label);
    }
    const title = el("title");
    title.textContent = `${node.title} (${node.category})`;
    group.append(title);
    group.addEventListener("click", () => { selectedNodeId = node.id; render(); showDetail(node); });
    group.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") { event.preventDefault(); selectedNodeId = node.id; render(); showDetail(node); }
    });
    nodesGroup.append(group);
  });
  viewport.append(nodesGroup);
  canvas.append(viewport);
  applyTransform();
  status.textContent = `Showing all ${subset.nodes.length.toLocaleString()} matching pages and ${subset.links.length.toLocaleString()} matching links${selectedNodeId ? `; highlighted ${selectedLinks.length.toLocaleString()} direct selected links` : ""}. Full dataset: ${graph.nodes.length.toLocaleString()} pages, ${graph.links.length.toLocaleString()} links. Wheel or buttons zoom; drag to pan; click a category label or legend label to open that category graph.`;
}

fetch("/graph-data.json")
  .then((response) => {
    if (!response.ok) throw new Error(`Graph request failed: ${response.status}`);
    return response.json();
  })
  .then((data) => {
    graph = data;
    const categories = [...new Set(graph.nodes.map((node) => node.category).filter((category) => category !== "root"))].sort();
    colors = new Map(categories.map((category, index) => [category, palette[index % palette.length]]));
    const allItem = document.createElement("span");
    allItem.className = "graph-legend-item graph-legend-all";
    allItem.textContent = "All categories";
    allItem.tabIndex = 0;
    allItem.setAttribute("role", "button");
    allItem.setAttribute("aria-label", "Open all categories graph");
    allItem.addEventListener("click", () => setCategory(""));
    allItem.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") { event.preventDefault(); setCategory(""); }
    });
    legend.append(allItem);
    categories.forEach((category) => {
      const option = document.createElement("option");
      option.value = category;
      option.textContent = `${category.replaceAll("-", " ")} (${graph.nodes.filter((node) => node.category === category).length})`;
      categorySelect.append(option);
      const item = document.createElement("span");
      item.className = "graph-legend-item";
      const swatch = document.createElement("i");
      swatch.style.background = colors.get(category);
      item.append(swatch, document.createTextNode(category.replaceAll("-", " ")));
      item.tabIndex = 0;
      item.setAttribute("role", "button");
      item.setAttribute("aria-label", `Open ${category.replaceAll("-", " ")} graph`);
      item.addEventListener("click", () => setCategory(category));
      item.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") { event.preventDefault(); setCategory(category); }
      });
      legend.append(item, document.createTextNode(" "));
    });
    const requestedCategory = new URLSearchParams(window.location.search).get("category");
    if (requestedCategory && categories.includes(requestedCategory)) categorySelect.value = requestedCategory;
    categorySelect.addEventListener("change", () => setCategory(categorySelect.value));
    searchInput.addEventListener("input", () => { selectedNodeId = ""; render(); });
    zoomIn.addEventListener("click", () => zoomAt(1.25));
    zoomOut.addEventListener("click", () => zoomAt(0.8));
    zoomReset.addEventListener("click", () => resetZoom());
    canvas.addEventListener("wheel", (event) => {
      event.preventDefault();
      zoomAt(event.deltaY < 0 ? 1.12 : 0.89, event.clientX, event.clientY);
    }, { passive: false });
    canvas.addEventListener("pointerdown", (event) => {
      if (event.target.closest(".graph-node")) return;
      canvas.setPointerCapture(event.pointerId);
      drag = { x: event.clientX, y: event.clientY, startX: transform.x, startY: transform.y };
    });
    canvas.addEventListener("pointermove", (event) => {
      if (!drag) return;
      const box = canvas.getBoundingClientRect();
      transform.x = drag.startX + (event.clientX - drag.x) * 1200 / box.width;
      transform.y = drag.startY + (event.clientY - drag.y) * 900 / box.height;
      applyTransform();
    });
    canvas.addEventListener("pointerup", () => { drag = null; });
    canvas.addEventListener("pointercancel", () => { drag = null; });
    render();
  })
  .catch((error) => { status.textContent = `Unable to load graph: ${error.message}`; });
""",
        encoding="utf-8",
    )


def strip_frontmatter(markdown: str) -> str:
    if not markdown.startswith("---\n"):
        return markdown
    end = markdown.find("\n---\n", 4)
    if end == -1:
        return markdown
    return markdown[end + 5 :].lstrip()


def write_styles() -> None:
    (DIST / "styles.css").write_text(
        """
:root {
  color-scheme: light;
  --bg: #f7f8f4;
  --panel: #ffffff;
  --ink: #17202a;
  --muted: #667085;
  --line: #d9ded6;
  --accent: #0f766e;
  --accent-2: #9a3412;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 16px/1.55 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.sidebar {
  position: fixed;
  inset: 0 auto 0 0;
  width: 320px;
  overflow: auto;
  padding: 28px 24px;
  border-right: 1px solid var(--line);
  background: #fbfcf8;
}
.eyebrow {
  margin: 0 0 8px;
  color: var(--accent-2);
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.brand {
  display: block;
  color: var(--ink);
  font-size: 1.45rem;
  font-weight: 800;
  line-height: 1.15;
}
.subtitle { color: var(--muted); margin: 12px 0 24px; }
.main-nav { display: grid; gap: 8px; margin: 0 0 24px; }
.main-nav a {
  display: block;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font-weight: 650;
}
.main-nav a.active { border-color: var(--accent); color: var(--accent); }
.search label { display: block; margin-bottom: 6px; color: var(--muted); font-weight: 650; }
.search input, .search-input {
  width: 100%;
  padding: 11px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  font: inherit;
}
main { max-width: 1080px; margin-left: 320px; padding: 42px clamp(24px, 5vw, 72px); }
.page, .landing {
  max-width: 860px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: clamp(24px, 4vw, 44px);
  box-shadow: 0 12px 35px rgba(16, 24, 40, 0.06);
}
.page-tools {
  margin: 0 0 1.25rem;
  font-size: 0.86rem;
}
.page-tools a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: #fbfcf8;
  color: var(--muted);
  font-weight: 700;
}
.page-tools a::after { content: "↗"; color: var(--accent); }
h1, h2, h3 { line-height: 1.18; margin: 1.4em 0 0.45em; }
h1:first-child, h2:first-child, h3:first-child { margin-top: 0; }
h1 { font-size: clamp(2rem, 4vw, 3.4rem); }
h2 { font-size: 1.65rem; border-top: 1px solid var(--line); padding-top: 1.1em; }
h3 { font-size: 1.2rem; }
p, li { max-width: 76ch; }
code { background: #eef2ec; border-radius: 5px; padding: 0.1em 0.35em; }
pre {
  overflow: auto;
  padding: 14px;
  border-radius: 8px;
  background: #101828;
  color: #f9fafb;
}
blockquote {
  margin: 1rem 0;
  padding: 0.2rem 0 0.2rem 1rem;
  border-left: 4px solid var(--accent);
  color: #344054;
}
.wiki-image {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 18px 0;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 12px;
  margin-top: 22px;
}
.card {
  display: grid;
  gap: 8px;
  padding: 16px;
  min-height: 130px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
}
.card strong { font-size: 1.02rem; line-height: 1.25; }
.card small { color: var(--accent-2); font-weight: 750; text-transform: uppercase; }
.card span { color: var(--muted); font-size: 0.92rem; }
.home-landing, .home-panel, .home-section {
  max-width: 1120px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
}
.home-landing {
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) minmax(260px, 0.8fr);
  gap: 24px;
  padding: clamp(24px, 4vw, 40px);
  margin-bottom: 18px;
}
.home-hero-copy h1 {
  max-width: 780px;
  margin: 0;
  font-size: clamp(2rem, 3.6vw, 3.45rem);
  letter-spacing: 0;
}
.home-deck {
  max-width: 72ch;
  margin: 18px 0 0;
  color: #344054;
  font-size: 1.06rem;
}
.home-intro {
  display: grid;
  gap: 10px;
  max-width: 74ch;
  margin-top: 18px;
  padding-left: 16px;
  border-left: 4px solid #c7ddd8;
  color: #344054;
}
.home-intro p {
  margin: 0;
  max-width: none;
}
.home-facts {
  display: grid;
  gap: 0;
  align-self: start;
  margin: 0;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fbfcf8;
}
.home-facts div {
  padding: 13px 14px;
  border-bottom: 1px solid var(--line);
}
.home-facts div:last-child { border-bottom: 0; }
.home-facts dt {
  margin: 0 0 2px;
  color: var(--accent-2);
  font-size: 0.72rem;
  font-weight: 850;
  text-transform: uppercase;
}
.home-facts dd {
  margin: 0;
  color: var(--ink);
  font-weight: 700;
}
.home-start {
  grid-column: 1 / -1;
  padding-top: 18px;
  border-top: 1px solid var(--line);
}
.home-start-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
}
.home-start-link {
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: 8px;
  min-height: 132px;
  padding: 16px;
  border: 1px solid #cfd8d1;
  border-radius: 10px;
  color: var(--ink);
  background: #fff;
  box-shadow: 0 8px 20px rgba(16, 24, 40, 0.04);
  transition: border-color 140ms, box-shadow 140ms, transform 140ms, background 140ms;
}
.home-start-link:first-child {
  border-color: var(--accent);
  background: #f1f8f6;
}
.home-start-link:hover, .home-start-link:focus {
  text-decoration: none;
  border-color: var(--accent);
  background: #f6fbf9;
  box-shadow: 0 12px 28px rgba(16, 24, 40, 0.08);
  transform: translateY(-1px);
}
.home-start-link strong { line-height: 1.2; font-size: 1.03rem; }
.home-start-link span, .home-row span, .home-metric span {
  color: var(--muted);
  font-size: 0.88rem;
}
.home-start-link em {
  color: var(--accent);
  font-style: normal;
  font-size: 0.82rem;
  font-weight: 850;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.home-split {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 18px;
  max-width: 1120px;
  margin-bottom: 18px;
}
.home-panel, .home-section {
  padding: clamp(20px, 3vw, 30px);
  margin-bottom: 18px;
}
.home-split .home-panel { margin-bottom: 0; }
.home-section-heading {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
}
.home-section-heading h2, .home-panel h2 {
  margin: 0;
  border: 0;
  padding: 0;
  font-size: 1.35rem;
}
.home-boundary-list {
  display: grid;
  gap: 10px;
  margin: 14px 0 0;
  padding-left: 1.25rem;
}
.home-boundary-list li { max-width: none; }
.home-metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 12px;
  margin-top: 14px;
}
.home-metric {
  display: grid;
  gap: 7px;
  min-height: 92px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: #fbfcf8;
  color: var(--ink);
  box-shadow: 0 6px 18px rgba(16, 24, 40, 0.03);
  transition: border-color 140ms, box-shadow 140ms, transform 140ms, background 140ms;
}
.home-metric:hover, .home-metric:focus {
  text-decoration: none;
  border-color: var(--accent);
  background: #f6fbf9;
  box-shadow: 0 10px 24px rgba(16, 24, 40, 0.06);
  transform: translateY(-1px);
}
.home-metric strong {
  color: var(--accent);
  font-size: 1.65rem;
  line-height: 1;
}
.home-metric span {
  color: var(--muted);
  font-size: 0.9rem;
  line-height: 1.25;
}
.home-row-list {
  display: grid;
  gap: 10px;
}
.home-row {
  display: grid;
  grid-template-columns: minmax(92px, 0.42fr) minmax(190px, 1fr) minmax(240px, 1.2fr) auto;
  gap: 16px;
  align-items: start;
  padding: 15px 16px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: #fff;
  color: var(--ink);
  box-shadow: 0 6px 18px rgba(16, 24, 40, 0.035);
  transition: border-color 140ms, box-shadow 140ms, transform 140ms, background 140ms;
}
.home-row:hover, .home-row:focus {
  text-decoration: none;
  border-color: var(--accent);
  background: #fbfdfb;
  box-shadow: 0 10px 24px rgba(16, 24, 40, 0.07);
  transform: translateY(-1px);
}
.home-row strong { line-height: 1.25; }
.home-row-kicker {
  color: var(--accent-2);
  font-size: 0.74rem;
  font-weight: 850;
  text-transform: uppercase;
}
.home-row-arrow {
  justify-self: end;
  color: var(--accent) !important;
  font-size: 0.78rem !important;
  font-weight: 850;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  white-space: nowrap;
}
.home-source-row { grid-template-columns: minmax(130px, 0.55fr) minmax(210px, 0.9fr) minmax(280px, 1.4fr) auto; }
.graph-landing { max-width: 1400px; }
.graph-landing h1 { margin-bottom: 8px; }
.graph-intro { margin: 0 0 16px; color: var(--muted); }
.graph-controls {
  display: grid;
  grid-template-columns: minmax(170px, 0.65fr) minmax(260px, 1.35fr);
  gap: 8px;
  position: absolute;
  z-index: 5;
  top: 12px;
  left: 12px;
  width: min(620px, calc(100% - 84px));
  padding: 8px;
  border: 1px solid rgba(208, 213, 221, 0.9);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.94);
  box-shadow: 0 4px 14px rgba(16, 24, 40, 0.12);
}
.graph-controls label { position: relative; color: var(--muted); font-size: 0.74rem; font-weight: 800; }
.graph-controls select, .graph-controls input {
  display: block;
  width: 100%;
  margin-top: 3px;
  padding: 8px 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font: inherit;
}
.graph-zoom-controls {
  display: grid;
  gap: 4px;
  align-items: center;
  position: absolute;
  z-index: 2;
  top: 12px;
  right: 12px;
  padding: 5px;
  border: 1px solid rgba(208, 213, 221, 0.9);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.94);
  box-shadow: 0 4px 14px rgba(16, 24, 40, 0.12);
}
.graph-zoom-controls button {
  min-width: 40px;
  min-height: 38px;
  padding: 7px 9px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font: inherit;
  font-weight: 800;
  cursor: pointer;
}
.graph-zoom-controls button:hover, .graph-zoom-controls button:focus {
  border-color: var(--accent);
  color: var(--accent);
}
.graph-status { position: absolute; z-index: 4; left: 14px; bottom: 51px; max-width: calc(100% - 150px); margin: 0; padding: 5px 8px; border-radius: 6px; background: rgba(255,255,255,.88); color: var(--muted); font-size: 0.76rem; }
.graph-legend {
  display: flex;
  gap: 5px;
  position: absolute;
  z-index: 4;
  right: 0;
  bottom: 0;
  left: 0;
  overflow-x: auto;
  padding: 8px 10px;
  border-top: 1px solid rgba(208,213,221,.8);
  background: rgba(255,255,255,.93);
}
.graph-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  flex: 0 0 auto;
  padding: 5px 7px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: #fff;
  color: var(--muted);
  font-size: 0.78rem;
  line-height: 1;
  text-transform: capitalize;
  white-space: nowrap;
  cursor: pointer;
}
.graph-legend-item:hover, .graph-legend-item:focus {
  border-color: var(--accent);
  color: var(--accent);
  outline: none;
}
.graph-legend-all {
  color: var(--ink);
  font-weight: 800;
}
.graph-legend-item i {
  flex: 0 0 auto;
  width: 9px;
  height: 9px;
  border-radius: 50%;
}
.graph-search-results { display: none; position: absolute; z-index: 8; top: calc(100% + 5px); right: 0; left: 0; max-height: 300px; overflow-y: auto; padding: 5px; border: 1px solid var(--line); border-radius: 7px; background: #fff; box-shadow: 0 10px 24px rgba(16,24,40,.16); }
.graph-search-results.open { display: grid; }
.graph-search-results button { padding: 8px 9px; border: 0; border-radius: 5px; background: transparent; color: var(--ink); font: inherit; text-align: left; cursor: pointer; }
.graph-search-results button:hover, .graph-search-results button:focus { background: #eef4f1; }
.graph-canvas-wrap { position: relative; height: max(680px, calc(100vh - 245px)); min-height: 680px; overflow: hidden; border: 1px solid var(--line); border-radius: 8px; background: #f8fafc; touch-action: none; }
.graph-canvas { display: block; width: 100%; height: 100%; cursor: grab; user-select: none; }
.graph-canvas:active { cursor: grabbing; }
.graph-viewport { transform-origin: 0 0; }
.graph-clusters rect {
  fill: #ffffff;
  stroke: #dbe3dd;
  stroke-width: 1;
}
.graph-clusters text {
  fill: #667085;
  font-size: 13px;
  font-weight: 800;
  text-transform: capitalize;
  cursor: pointer;
  outline: none;
}
.graph-clusters text:hover, .graph-clusters text:focus {
  fill: var(--accent);
}
.graph-links line {
  stroke: #64748b;
  stroke-width: 0.8;
  opacity: 0.16;
}
.graph-node { cursor: pointer; outline: none; }
.graph-node circle { stroke: #fff; stroke-width: 2; transition: stroke-width 120ms, r 120ms; }
.graph-node:hover circle, .graph-node:focus circle { stroke: var(--ink); stroke-width: 3; }
.graph-node.selected circle { stroke: #111827; stroke-width: 4; }
.graph-node-label {
  fill: #334155;
  paint-order: stroke;
  stroke: #fff;
  stroke-width: 3px;
  stroke-linejoin: round;
  font-size: 8px;
  font-weight: 750;
  pointer-events: auto;
}
.graph-node:hover .graph-node-label, .graph-node:focus .graph-node-label { fill: var(--ink); }
.graph-detail { display: none; position: absolute; z-index: 6; top: 92px; right: 12px; width: min(340px, calc(100% - 24px)); max-height: calc(100% - 160px); overflow-y: auto; padding: 16px; border: 1px solid var(--line); border-radius: 8px; background: rgba(251,252,248,.97); box-shadow: 0 12px 30px rgba(16,24,40,.18); }
.graph-detail.open { display: block; }
.graph-detail-close { float: right; width: 32px; height: 32px; border: 1px solid var(--line); border-radius: 6px; background: #fff; color: var(--ink); font-size: 1.25rem; cursor: pointer; }
.graph-detail h2 { margin-top: 0; padding-top: 0; border-top: 0; font-size: 1.35rem; }
.graph-detail h3 { margin-top: 1.5rem; }
.graph-counts { color: var(--muted); font-size: 0.88rem; }
.graph-open-page { display: inline-block; padding: 8px 11px; border-radius: 7px; background: var(--accent); color: #fff; font-weight: 750; }
.graph-nearby { display: grid; gap: 8px; padding-left: 1.1rem; }
.graph-nearby a, .graph-nearby small { display: block; }
.graph-nearby small { color: var(--muted); text-transform: capitalize; }
@media (max-width: 880px) {
  .sidebar { position: static; width: auto; border-right: 0; border-bottom: 1px solid var(--line); padding: 22px 20px; }
  .brand { font-size: 1.28rem; }
  .subtitle { margin: 10px 0 16px; font-size: 0.95rem; }
  main { margin-left: 0; padding: 24px 16px; }
  .main-nav { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px; }
  .main-nav a { padding: 8px 9px; font-size: 0.9rem; }
  .home-landing, .home-split, .home-start-grid, .home-row, .home-source-row { grid-template-columns: 1fr; }
  .home-metric-grid { grid-template-columns: 1fr; }
  .home-start { grid-column: auto; }
  .graph-controls { grid-template-columns: 1fr; width: calc(100% - 88px); }
  .graph-canvas-wrap { height: 72vh; min-height: 520px; }
  .graph-status { bottom: 49px; max-width: calc(100% - 86px); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .graph-detail { top: auto; right: 8px; bottom: 52px; left: 8px; width: auto; max-height: 48%; }
  .page-graph .sidebar { padding: 12px 16px; }
  .page-graph .sidebar > .eyebrow, .page-graph .sidebar > .subtitle, .page-graph .sidebar > .search { display: none; }
  .page-graph .brand { display: block; margin-bottom: 10px; font-size: 1rem; }
  .page-graph .main-nav { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .page-graph .main-nav a:nth-child(n+4) { display: none; }
  .page-graph main { padding-top: 14px; }
  .page-graph .graph-landing { padding: 18px 14px; }
  .page-graph .graph-landing > .eyebrow { margin-bottom: 8px; }
  .page-graph .graph-landing h1 { margin-top: 0; font-size: 2rem; }
}
""".strip()
        + "\n",
        encoding="utf-8",
    )


def write_sigma_graph_script() -> None:
    """Write the WebGL graph client used by the public static graph page."""
    (DIST / "graph.js").write_text(
        r"""import Graph from 'https://esm.sh/graphology@0.26.0';
import Sigma from 'https://esm.sh/sigma@3.0.3';
import FA2Layout from 'https://esm.sh/graphology-layout-forceatlas2@0.10.1/worker';

const colors=['#0f766e','#c2410c','#2563eb','#7c3aed','#be123c','#4d7c0f','#0891b2','#a16207','#475569','#047857','#dc2626','#4338ca'];
const canvas=document.querySelector('#graph-canvas'),category=document.querySelector('#graph-category'),search=document.querySelector('#graph-search'),searchResults=document.querySelector('#graph-search-results'),legend=document.querySelector('#graph-legend'),status=document.querySelector('#graph-status'),detail=document.querySelector('#graph-detail');
const data=await fetch('/graph-data.json').then(r=>r.ok?r.json():Promise.reject(new Error(`Graph request failed: ${r.status}`)));
const graph=new Graph({type:'undirected'}),categories=[...new Set(data.nodes.map(n=>n.category).filter(c=>c!=='root'))].sort(),palette=new Map(categories.map((c,i)=>[c,colors[i%colors.length]]));
const seed=(id,category)=>{let h=2166136261;for(const char of `${category}:${id}`){h^=char.charCodeAt(0);h=Math.imul(h,16777619)}const a=(h>>>0)/4294967296*Math.PI*2,r=2+((h>>>8)&1023)/150,g=categories.indexOf(category)/Math.max(categories.length,1)*Math.PI*2;return{x:Math.cos(g)*18+Math.cos(a)*r,y:Math.sin(g)*18+Math.sin(a)*r}};
data.nodes.filter(n=>n.category!=='root').forEach(n=>{const p=seed(n.id,n.category);graph.addNode(n.id,{...n,...p,label:n.title,size:Math.min(15,3+Math.sqrt(n.degree+1)),color:palette.get(n.category)||'#64748b'})});
data.links.forEach((e,i)=>{if(graph.hasNode(e.source)&&graph.hasNode(e.target)&&!graph.hasEdge(e.source,e.target))graph.addEdgeWithKey(`e${i}`,e.source,e.target,{size:.3,color:'#94a3b8'})});
const addLabel=(name,label,color='')=>{const item=document.createElement('button');item.type='button';item.className=`graph-legend-item${name?'':' graph-legend-all'}`;if(color){const swatch=document.createElement('i');swatch.style.background=color;item.append(swatch)}item.append(document.createTextNode(label));item.onclick=()=>setCategory(name);legend.append(item)};
addLabel('','All categories');categories.forEach(name=>{const option=document.createElement('option');option.value=name;option.textContent=`${name.replaceAll('-',' ')} (${data.nodes.filter(n=>n.category===name).length})`;category.append(option);addLabel(name,name.replaceAll('-',' '),palette.get(name))});
let selected='',hovered='';
const renderer=new Sigma(graph,canvas,{labelDensity:.06,labelGridCellSize:110,labelRenderedSizeThreshold:9,zIndex:true,nodeReducer(node,a){const q=search.value.trim().toLowerCase(),matches=!q||`${a.label} ${a.excerpt}`.toLowerCase().includes(q),hidden=Boolean(category.value&&a.category!==category.value),active=node===(selected||hovered);return{...a,hidden,size:active?a.size*1.75:a.size,zIndex:active||matches&&q?2:1,color:active?'#111827':q&&!matches?'#cbd5e1':a.color,forceLabel:active||Boolean(q&&matches||category.value)}},edgeReducer(edge,a){const focus=selected||hovered;if(!focus)return{...a,hidden:false,color:search.value.trim()?'#e2e8f0':'#cbd5e1',size:.18};const active=graph.extremities(edge).includes(focus);return{...a,hidden:!active,color:'#475569',size:active?1.5:.2,zIndex:active?1:0}}});
function matches(){const q=search.value.trim().toLowerCase();return q?data.nodes.filter(n=>n.category!=='root'&&(!category.value||n.category===category.value)&&`${n.title} ${n.excerpt}`.toLowerCase().includes(q)):[]}
function update(){const found=matches(),visible=data.nodes.filter(n=>n.category!=='root'&&(!category.value||n.category===category.value)).length;status.textContent=search.value.trim()?`${found.length.toLocaleString()} matches highlighted within ${visible.toLocaleString()} visible pages. The surrounding graph remains in view.`:`${visible.toLocaleString()} pages and ${graph.size.toLocaleString()} resolved links. Drag to pan, scroll to zoom, and click any label to explore.`}
function focusNode(node){selected=node;const a=graph.getNodeAttributes(node),neighbors=graph.neighbors(node).sort((x,y)=>graph.degree(y)-graph.degree(x)).slice(0,18);detail.classList.add('open');detail.innerHTML=`<button class="graph-detail-close" type="button" aria-label="Close details">×</button><p class="eyebrow">${a.category}</p><h2>${a.label}</h2><p>${a.excerpt||''}</p><p class="graph-counts">${graph.degree(node)} connected pages</p><a class="graph-open-page" href="${a.url}">Open page</a>${neighbors.length?'<h3>Nearby pages</h3><ul class="graph-nearby">'+neighbors.map(id=>`<li><a href="${graph.getNodeAttribute(id,'url')}">${graph.getNodeAttribute(id,'label')}</a><small>${graph.getNodeAttribute(id,'category')}</small></li>`).join('')+'</ul>':''}`;detail.querySelector('.graph-detail-close').onclick=()=>{selected='';detail.classList.remove('open');renderer.refresh()};renderer.refresh();const p=renderer.getNodeDisplayData(node);if(p)renderer.getCamera().animate({x:p.x,y:p.y,ratio:.3},{duration:500})}
function fitCategory(){if(!category.value){renderer.getCamera().animatedReset({duration:500});return}const points=graph.filterNodes((node,a)=>a.category===category.value).map(node=>renderer.getNodeDisplayData(node)).filter(Boolean);if(!points.length)return;const x=points.reduce((sum,p)=>sum+p.x,0)/points.length,y=points.reduce((sum,p)=>sum+p.y,0)/points.length,ratio=Math.min(1,Math.max(.52,.42+Math.sqrt(points.length)/35));renderer.getCamera().animate({x,y,ratio},{duration:500})}
function setCategory(name){category.value=name;selected='';detail.classList.remove('open');const url=new URL(location.href);name?url.searchParams.set('category',name):url.searchParams.delete('category');history.replaceState({},'',url);renderer.refresh();requestAnimationFrame(fitCategory);update()}
const requested=new URLSearchParams(location.search).get('category');if(requested&&categories.includes(requested))category.value=requested;
category.onchange=()=>setCategory(category.value);search.oninput=()=>{selected='';const found=matches().slice(0,8);searchResults.replaceChildren(...found.map(item=>{const button=document.createElement('button');button.type='button';button.textContent=item.title;button.onclick=()=>{searchResults.replaceChildren();focusNode(item.id)};return button}));searchResults.classList.toggle('open',Boolean(found.length));renderer.refresh();update()};search.onkeydown=event=>{if(event.key==='Enter'){const first=matches()[0];if(first){event.preventDefault();searchResults.replaceChildren();focusNode(first.id)}}};renderer.on('enterNode',({node})=>{hovered=node;renderer.refresh()});renderer.on('leaveNode',()=>{hovered='';renderer.refresh()});renderer.on('clickNode',({node})=>focusNode(node));
document.querySelector('#graph-zoom-in').onclick=()=>renderer.getCamera().animatedZoom({duration:250});document.querySelector('#graph-zoom-out').onclick=()=>renderer.getCamera().animatedUnzoom({duration:250});document.querySelector('#graph-zoom-reset').onclick=()=>{category.value='';search.value='';searchResults.replaceChildren();selected='';detail.classList.remove('open');renderer.refresh();renderer.getCamera().animatedReset({duration:400});update()};
const layout=new FA2Layout(graph,{settings:{gravity:1,scalingRatio:10,slowDown:5,barnesHutOptimize:true}});layout.start();setTimeout(()=>{layout.stop();fitCategory()},4500);update();
""",
        encoding="utf-8",
    )


def export() -> None:
    pages = [parse_page(path) for path in sorted(WIKI.rglob("*.md"))]
    by_id, by_stem = build_link_maps(pages)
    graph = extract_graph(pages, by_id, by_stem)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    write_styles()
    write_sigma_graph_script()
    (DIST / "graph-data.json").write_text(json.dumps(graph, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    assets = WIKI / "assets"
    if assets.exists():
        shutil.copytree(assets, DIST / "assets")

    for page in pages:
        out = page_output_path(page)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(page, pages, by_id, by_stem), encoding="utf-8")
        md_out = page_markdown_output_path(page)
        md_out.parent.mkdir(parents=True, exist_ok=True)
        md_out.write_text(page.source.read_text(encoding="utf-8"), encoding="utf-8")

    for category in public_categories(pages):
        category_pages = [page for page in pages if page.category == category and not is_category_index(page)]
        out = DIST / category / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_category(category, category_pages, pages), encoding="utf-8")

    search_dir = DIST / "search"
    search_dir.mkdir()
    (search_dir / "index.html").write_text(render_search(pages), encoding="utf-8")

    graph_dir = DIST / "graph"
    graph_dir.mkdir()
    (graph_dir / "index.html").write_text(render_graph(pages), encoding="utf-8")

    (DIST / "_headers").write_text(
        """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
/assets/*
  Cache-Control: public, max-age=31536000, immutable
""",
        encoding="utf-8",
    )
    (DIST / "_redirects").write_text(
        """/agentic-web/ /topics/agentic-web/ 301
/agentic-web /topics/agentic-web/ 301
""",
        encoding="utf-8",
    )
    agent_index = WIKI / "resources" / "agent-source-index.md"
    if agent_index.exists():
        raw_agent_index = strip_frontmatter(agent_index.read_text(encoding="utf-8"))
        (DIST / "agent-index.md").write_text(raw_agent_index, encoding="utf-8")
        (DIST / "agent-source-index.md").write_text(raw_agent_index, encoding="utf-8")

    print(f"Exported {len(pages)} pages to {DIST}")


if __name__ == "__main__":
    export()
