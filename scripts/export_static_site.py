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
DIST = ROOT / "dist"
SITE_TITLE = "AI Engineer World's Fair 2026 Wiki"
SITE_SUBTITLE = "Standalone conference intelligence wiki for AI Engineer World's Fair 2026."
PREFERRED_CATEGORIES = ["talks", "slides", "people", "companies", "topics", "resources", "events"]


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


def build_link_maps(pages: list[Page]) -> tuple[dict[str, Page], dict[str, Page]]:
    by_id = {page.id: page for page in pages}
    by_stem: dict[str, Page] = {}
    for page in pages:
        by_stem.setdefault(Path(page.id).name, page)
    return by_id, by_stem


def resolve_wikilink(target: str, by_id: dict[str, Page], by_stem: dict[str, Page]) -> str | None:
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    page = by_id.get(target) or by_stem.get(Path(target).name)
    return page.url if page else None


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
    body = f"""<article class="page">
  {render_markdown(page.body, by_id, by_stem)}
</article>"""
    return render_layout(page.title, body, pages, page.category if page.category != "root" else page.id)


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
@media (max-width: 880px) {
  .sidebar { position: static; width: auto; border-right: 0; border-bottom: 1px solid var(--line); }
  main { margin-left: 0; padding: 24px 16px; }
  .main-nav { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
""".strip()
        + "\n",
        encoding="utf-8",
    )


def export() -> None:
    pages = [parse_page(path) for path in sorted(WIKI.rglob("*.md"))]
    by_id, by_stem = build_link_maps(pages)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    write_styles()

    assets = WIKI / "assets"
    if assets.exists():
        shutil.copytree(assets, DIST / "assets")

    for page in pages:
        out = page_output_path(page)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(page, pages, by_id, by_stem), encoding="utf-8")

    categories = sorted({page.category for page in pages if page.category != "root"}, key=category_sort_key)
    for category in categories:
        category_pages = [page for page in pages if page.category == category]
        out = DIST / category / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_category(category, category_pages, pages), encoding="utf-8")

    search_dir = DIST / "search"
    search_dir.mkdir()
    (search_dir / "index.html").write_text(render_search(pages), encoding="utf-8")

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
