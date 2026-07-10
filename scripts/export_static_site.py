#!/usr/bin/env python3
"""Export the World's Fair wiki as a static Cloudflare Pages site."""

from __future__ import annotations

import html
import json
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
    "policies",
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
    outgoing: dict[str, set[str]] = {page.id: set() for page in pages}
    backlinks: dict[str, set[str]] = {page.id: set() for page in pages}

    for page in pages:
        for raw_target in re.findall(r"(?<!!)\[\[([^\]]+)\]\]", page.body):
            target = raw_target.split("|", 1)[0]
            linked = resolve_wikilink_page(target, by_id, by_stem)
            if not linked or linked.id == page.id:
                continue
            outgoing[page.id].add(linked.id)
            backlinks[linked.id].add(page.id)

    nodes = []
    for page in pages:
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
    categories = sorted({page.category for page in pages if page.category != "root"}, key=category_sort_key)
    nav_items = []
    for category in categories:
        active = ' class="active"' if current == category else ""
        nav_items.append(f'<a href="/{category}/"{active}>{html.escape(titleize(category))}</a>')
    nav = "\n".join(nav_items)
    home_active = ' class="active"' if current == "overview" else ""
    index_active = ' class="active"' if current == "index" else ""
    quotes_active = ' class="active"' if current == "quotes" else ""
    graph_active = ' class="active"' if current == "graph" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · {html.escape(SITE_TITLE)}</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <aside class="sidebar">
    <p class="eyebrow">AI Engineer Conference Wiki</p>
    <a class="brand" href="/">{html.escape(SITE_TITLE)}</a>
    <p class="subtitle">{html.escape(SITE_SUBTITLE)}</p>
    <nav class="main-nav">
      <a href="/"{home_active}>Home</a>
      <a href="/index/"{index_active}>Index</a>
      <a href="/graph/"{graph_active}>Graph</a>
      <a href="/quotes/"{quotes_active}>Quotes</a>
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
    category_counts = {category: len([item for item in pages if item.category == category]) for category in {item.category for item in pages}}
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
        ("Speaker pages", category_counts.get("people", 0), "/people/"),
        ("Company pages", category_counts.get("companies", 0), "/companies/"),
        ("Source resources", category_counts.get("resources", 0), "/resources/"),
        ("Slide pages", category_counts.get("slides", 0), "/slides/"),
        ("Transcript pages", category_counts.get("transcripts", 0), "/transcripts/"),
        ("Topics", category_counts.get("topics", 0), "/topics/"),
        ("Graph links", f"{len(graph['links']):,}", "/graph/"),
    ]
    stats_html = "\n".join(
        f"""<a class="home-stat" href="{url}">
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
            f"""<a class="home-event-card" href="{event.url}">
  <strong>{html.escape(event.title)}</strong>
  <span>{linked_count} linked sessions or sources</span>
  <p>{html.escape(event.excerpt)}</p>
</a>"""
        )
    event_cards = "\n".join(event_card_items)

    source_layers = [
        ("Official schedule", f"{entry_count(sessions)} sessions and {entry_count(speakers)} roster speakers", "Dates, titles, speakers, organizations, rooms, tracks, and session status.", "/resources/official-sessions-json/"),
        ("AI Engineer media", f"{entry_count(videos)} channel videos and {entry_count(streams)} livestream rows", "Official channel uploads, livestream metadata, transcript status, and slide extraction outputs.", "/resources/worldsfair-2026-livestreams/"),
        ("Matched recordings", f"{entry_count(related_videos)} talk/video rows and {entry_count(livestream_segments)} livestream timestamp matches", "Speaker/title matching connects schedule pages to public recordings and transcript coverage.", "/resources/talk-video-transcript-map/"),
        ("Supporting discovery", f"{entry_count(external_discovery)} external video candidates", "External uploads remain secondary sources unless a page says otherwise.", "/resources/external-video-discovery/"),
        ("Cached transcripts", f"{count_files(RAW / 'youtube-transcripts', '*.txt')} cut-video, {count_files(RAW / 'youtube-livestream-transcripts', '*.txt')} livestream, {count_files(RAW / 'external-youtube-transcripts', '*.txt')} external", "Transcript pages are supporting evidence; important wording should be checked against the linked video/resource page.", "/transcripts/"),
        ("Synthesis layers", f"{category_counts.get('topics', 0)} topics, {category_counts.get('tools', 0)} tools, {category_counts.get('questions', 0)} questions", "Topic, tool, claim, harness, playbook, evaluation, and policy pages summarize patterns across evidence.", "/topics/"),
    ]
    source_html = "\n".join(
        f"""<a class="home-source-card" href="{url}">
  <small>{html.escape(kicker)}</small>
  <strong>{html.escape(count)}</strong>
  <span>{html.escape(description)}</span>
</a>"""
        for kicker, count, description, url in source_layers
    )

    primary_links = [
        ("Official event site", "https://www.ai.engineer/worldsfair/2026", "Original public event page."),
        ("Conference days", "/events/", "Day-level schedule anchors."),
        ("Talk schedule", "/talks/", "All generated official session pages."),
        ("Livestreams", "/resources/worldsfair-2026-livestreams/", "Official AI Engineer livestream sources."),
        ("Talk/video map", "/resources/talk-video-transcript-map/", "Recording and transcript coverage by talk."),
        ("Knowledge graph", "/graph/", "Build-time wikilink map."),
        ("Agent index", "/agent-index.md", "Standalone markdown navigation contract."),
        ("Source boundary", "/resources/source-boundary/", "Evidence confidence and corpus rules."),
    ]
    links_html = "\n".join(
        f"""<a class="home-link-card" href="{html.escape(url)}">
  <strong>{html.escape(label)}</strong>
  <span>{html.escape(description)}</span>
</a>"""
        for label, url, description in primary_links
    )

    body = f"""<section class="home-landing">
  <p class="page-tools"><a href="{html.escape(page.markdown_url)}">Markdown source</a></p>
  <p class="eyebrow">AI Engineer World's Fair 2026</p>
  <h1>Conference intelligence wiki</h1>
  <p class="home-lede">A static, read-only map of the San Francisco World&apos;s Fair built from the official schedule and speaker roster, then layered with public AI Engineer video, transcripts, slides, OCR, topics, tools, quotes, and source-bound synthesis.</p>
  <div class="home-hero-actions">
    <a href="/events/">Browse days</a>
    <a href="/talks/">Browse talks</a>
    <a href="/graph/">Open graph</a>
    <a href="/agent-index.md">Agent index</a>
  </div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">At a glance</p>
    <h2>Corpus counts</h2>
  </div>
  <div class="home-stat-grid">{stats_html}</div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">Primary navigation</p>
    <h2>Start with the event, then follow evidence</h2>
  </div>
  <div class="home-link-grid">{links_html}</div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">Source boundary</p>
    <h2>Official facts stay separate from supporting media and synthesis</h2>
  </div>
  <div class="home-boundary">
    <p><strong>Official schedule facts</strong> establish dates, titles, speakers, organizations, tracks, rooms, and session status.</p>
    <p><strong>Supporting media</strong> includes AI Engineer YouTube videos, livestreams, transcripts, slide frames, OCR, reconstructed slide crops, and external video candidates.</p>
    <p><strong>Synthesis pages</strong> such as topics, tools, claims, questions, harnesses, playbooks, evaluations, and policies are navigation and analysis layers. Follow their linked talk, resource, transcript, and slide pages before treating a claim as primary.</p>
  </div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">Conference days</p>
    <h2>Event panels</h2>
  </div>
  <div class="home-event-grid">{event_cards}</div>
</section>

<section class="home-section">
  <div class="home-section-heading">
    <p class="eyebrow">Source layers</p>
    <h2>What the wiki is built from</h2>
  </div>
  <div class="home-source-grid">{source_html}</div>
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
  <p>Explore the wiki links between talks, people, companies, tools, topics, and evidence pages. The graph is generated at build time and remains read-only.</p>
  <div class="graph-controls" aria-label="Graph filters">
    <label>Category<select id="graph-category"><option value="">All categories</option></select></label>
    <label>Search<input id="graph-search" type="search" placeholder="Find a page by title or text"></label>
  </div>
  <p id="graph-status" class="graph-status" aria-live="polite">Loading graph…</p>
  <div id="graph-legend" class="graph-legend" aria-label="Graph legend"></div>
  <div class="graph-workspace">
    <div class="graph-canvas-wrap">
      <svg id="graph-canvas" class="graph-canvas" viewBox="0 0 1200 760" role="img" aria-label="Wiki relationship graph"></svg>
    </div>
    <aside id="graph-detail" class="graph-detail">
      <p class="eyebrow">Node detail</p>
      <h2>Select a page</h2>
      <p>Choose a node to inspect its category, link counts, and nearby pages.</p>
    </aside>
  </div>
  <noscript><p>This interactive graph requires JavaScript. The underlying dataset remains available at <a href="/graph-data.json">/graph-data.json</a>.</p></noscript>
</section>
<script src="/graph.js" defer></script>"""
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
let graph = { nodes: [], links: [] };
let colors = new Map();

function el(name, attrs = {}) {
  const node = document.createElementNS(SVG_NS, name);
  Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
  return node;
}

function graphSubset() {
  const category = categorySelect.value;
  const query = searchInput.value.trim().toLowerCase();
  const filtered = graph.nodes.filter((node) => {
    if (category && node.category !== category) return false;
    if (!query) return true;
    return `${node.title} ${node.category} ${node.excerpt}`.toLowerCase().includes(query);
  });
  const ranked = [...filtered].sort((a, b) => b.degree - a.degree || a.title.localeCompare(b.title));
  const limit = query ? 80 : category ? 140 : 160;
  const primary = ranked.slice(0, limit);
  const ids = new Set(primary.map((node) => node.id));
  const links = graph.links.filter((link) => ids.has(link.source) && ids.has(link.target));
  return { nodes: primary, links, total: filtered.length, limited: filtered.length > primary.length };
}

function positions(nodes) {
  const grouped = new Map();
  nodes.forEach((node) => {
    if (!grouped.has(node.category)) grouped.set(node.category, []);
    grouped.get(node.category).push(node);
  });
  const categories = [...grouped.keys()].sort();
  const output = new Map();
  categories.forEach((category, categoryIndex) => {
    const angle = (Math.PI * 2 * categoryIndex) / Math.max(categories.length, 1) - Math.PI / 2;
    const centerX = 600 + Math.cos(angle) * (categories.length === 1 ? 0 : 320);
    const centerY = 380 + Math.sin(angle) * (categories.length === 1 ? 0 : 230);
    const items = grouped.get(category).sort((a, b) => b.degree - a.degree || a.title.localeCompare(b.title));
    items.forEach((node, index) => {
      const ring = Math.floor(Math.sqrt(index));
      const itemAngle = index * 2.399963;
      const radius = 22 + ring * 14;
      output.set(node.id, {
        x: centerX + Math.cos(itemAngle) * radius,
        y: centerY + Math.sin(itemAngle) * radius,
      });
    });
  });
  return output;
}

function showDetail(node) {
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
  const coords = positions(subset.nodes);
  canvas.replaceChildren();
  const defs = el("defs");
  const marker = el("marker", { id: "arrow", viewBox: "0 0 10 10", refX: "13", refY: "5", markerWidth: "5", markerHeight: "5", orient: "auto-start-reverse" });
  marker.append(el("path", { d: "M 0 0 L 10 5 L 0 10 z", fill: "#94a3b8" }));
  defs.append(marker);
  canvas.append(defs);
  const linksGroup = el("g", { class: "graph-links" });
  subset.links.forEach((link) => {
    const source = coords.get(link.source);
    const target = coords.get(link.target);
    if (!source || !target) return;
    linksGroup.append(el("line", { x1: source.x, y1: source.y, x2: target.x, y2: target.y, "marker-end": "url(#arrow)" }));
  });
  canvas.append(linksGroup);
  const nodesGroup = el("g", { class: "graph-nodes" });
  subset.nodes.forEach((node) => {
    const point = coords.get(node.id);
    const group = el("g", { class: "graph-node", tabindex: "0", role: "button", "aria-label": `${node.title}, ${node.category}` });
    group.append(el("circle", { cx: point.x, cy: point.y, r: Math.min(12, 5 + Math.sqrt(node.degree + 1)), fill: colors.get(node.category) }));
    const title = el("title");
    title.textContent = `${node.title} (${node.category})`;
    group.append(title);
    group.addEventListener("click", () => showDetail(node));
    group.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") { event.preventDefault(); showDetail(node); }
    });
    nodesGroup.append(group);
  });
  canvas.append(nodesGroup);
  status.textContent = `Showing ${subset.nodes.length.toLocaleString()} of ${subset.total.toLocaleString()} matching pages and ${subset.links.length.toLocaleString()} visible links${subset.limited ? "; highest-connected pages shown" : ""}. Full dataset: ${graph.nodes.length.toLocaleString()} pages, ${graph.links.length.toLocaleString()} links.`;
}

fetch("/graph-data.json")
  .then((response) => {
    if (!response.ok) throw new Error(`Graph request failed: ${response.status}`);
    return response.json();
  })
  .then((data) => {
    graph = data;
    const categories = [...new Set(graph.nodes.map((node) => node.category))].sort();
    colors = new Map(categories.map((category, index) => [category, palette[index % palette.length]]));
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
      legend.append(item);
    });
    categorySelect.addEventListener("change", render);
    searchInput.addEventListener("input", render);
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
  color: var(--muted);
}
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
.home-landing, .home-section {
  max-width: 1120px;
  margin-bottom: 18px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: clamp(22px, 4vw, 42px);
  box-shadow: 0 12px 35px rgba(16, 24, 40, 0.05);
}
.home-landing h1 { max-width: 820px; margin: 0; }
.home-lede { max-width: 88ch; color: #344054; font-size: 1.08rem; }
.home-hero-actions, .home-stat-grid, .home-link-grid, .home-event-grid, .home-source-grid {
  display: grid;
  gap: 12px;
}
.home-hero-actions {
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  margin-top: 24px;
}
.home-hero-actions a {
  padding: 12px 14px;
  border: 1px solid var(--accent);
  border-radius: 8px;
  background: #fff;
  color: var(--accent);
  font-weight: 800;
  text-align: center;
}
.home-section-heading h2 {
  margin: 0 0 16px;
  border: 0;
  padding: 0;
}
.home-stat-grid { grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); }
.home-link-grid, .home-event-grid, .home-source-grid { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.home-stat, .home-link-card, .home-event-card, .home-source-card {
  display: grid;
  gap: 7px;
  min-height: 100px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
}
.home-stat strong {
  font-size: 1.8rem;
  line-height: 1;
  color: var(--accent);
}
.home-stat span, .home-link-card span, .home-event-card span, .home-source-card span {
  color: var(--muted);
  font-size: 0.92rem;
}
.home-link-card strong, .home-event-card strong, .home-source-card strong { font-size: 1.03rem; line-height: 1.22; }
.home-event-card p { margin: 0; color: #344054; font-size: 0.92rem; }
.home-source-card small {
  color: var(--accent-2);
  font-weight: 800;
  text-transform: uppercase;
}
.home-boundary {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}
.home-boundary p {
  margin: 0;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
}
.graph-landing { max-width: 1200px; }
.graph-controls {
  display: grid;
  grid-template-columns: repeat(2, minmax(220px, 1fr));
  gap: 12px;
  margin: 24px 0 12px;
}
.graph-controls label { color: var(--muted); font-weight: 700; }
.graph-controls select, .graph-controls input {
  display: block;
  width: 100%;
  margin-top: 6px;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font: inherit;
}
.graph-status { color: var(--muted); font-size: 0.9rem; }
.graph-legend { display: flex; flex-wrap: wrap; gap: 6px 12px; margin: 14px 0; }
.graph-legend-item { display: inline-flex; align-items: center; gap: 5px; color: var(--muted); font-size: 0.78rem; text-transform: capitalize; }
.graph-legend-item i { width: 10px; height: 10px; border-radius: 50%; }
.graph-workspace { display: grid; grid-template-columns: minmax(0, 2fr) minmax(260px, 1fr); gap: 16px; align-items: start; }
.graph-canvas-wrap { min-height: 560px; overflow: hidden; border: 1px solid var(--line); border-radius: 8px; background: #f8fafc; }
.graph-canvas { display: block; width: 100%; min-height: 560px; }
.graph-links line { stroke: #cbd5e1; stroke-width: 1; opacity: 0.55; }
.graph-node { cursor: pointer; outline: none; }
.graph-node circle { stroke: #fff; stroke-width: 2; transition: stroke-width 120ms, r 120ms; }
.graph-node:hover circle, .graph-node:focus circle { stroke: var(--ink); stroke-width: 3; }
.graph-detail { min-height: 300px; padding: 18px; border: 1px solid var(--line); border-radius: 8px; background: #fbfcf8; }
.graph-detail h2 { margin-top: 0; padding-top: 0; border-top: 0; font-size: 1.35rem; }
.graph-detail h3 { margin-top: 1.5rem; }
.graph-counts { color: var(--muted); font-size: 0.88rem; }
.graph-open-page { display: inline-block; padding: 8px 11px; border-radius: 7px; background: var(--accent); color: #fff; font-weight: 750; }
.graph-nearby { display: grid; gap: 8px; padding-left: 1.1rem; }
.graph-nearby a, .graph-nearby small { display: block; }
.graph-nearby small { color: var(--muted); text-transform: capitalize; }
@media (max-width: 880px) {
  .sidebar { position: static; width: auto; border-right: 0; border-bottom: 1px solid var(--line); }
  main { margin-left: 0; padding: 24px 16px; }
  .main-nav { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .home-boundary { grid-template-columns: 1fr; }
  .graph-controls, .graph-workspace { grid-template-columns: 1fr; }
  .graph-canvas-wrap, .graph-canvas { min-height: 420px; }
}
""".strip()
        + "\n",
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
    write_graph_script()
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

    categories = sorted({page.category for page in pages if page.category != "root"}, key=category_sort_key)
    for category in categories:
        category_pages = [page for page in pages if page.category == category]
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
