from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_static_site  # noqa: E402


def page(title: str, excerpt: str, slug: str) -> export_static_site.Page:
    return export_static_site.Page(
        id=f"companies/{slug}",
        source=Path(f"wiki/companies/{slug}.md"),
        title=title,
        category="companies",
        body=f"# {title}\n\n{excerpt}",
        excerpt=excerpt,
    )


def search_parts(rendered: str) -> tuple[list[dict[str, str]], str]:
    index_match = re.search(
        r'<script id="search-index" type="application/json">(.*?)</script>',
        rendered,
        re.S,
    )
    runtime_match = re.search(
        r'<script id="search-runtime">(.*?)</script>', rendered, re.S
    )
    assert index_match is not None
    assert runtime_match is not None
    return json.loads(index_match.group(1)), runtime_match.group(1)


def test_search_index_is_safe_for_inline_embedding() -> None:
    title = '</script><img src=x onerror="alert(1)">'
    excerpt = "AT&T <strong>research</strong>"

    rendered = export_static_site.render_search([page(title, excerpt, "unsafe")])
    index, _runtime = search_parts(rendered)

    assert title not in rendered
    assert excerpt not in rendered
    assert index == [
        {
            "title": title,
            "url": "/companies/unsafe/",
            "category": "companies",
            "excerpt": excerpt,
        }
    ]


def test_search_runtime_applies_sidebar_query_and_renders_text_safely() -> None:
    rendered = export_static_site.render_search(
        [
            page("Anthropic", "AI safety company", "anthropic"),
            page("OpenAI", "AI research company", "openai"),
        ]
    )
    index, runtime = search_parts(rendered)
    node_program = f"""
class Element {{
  constructor(tag = "") {{
    this.tag = tag;
    this.value = "";
    this.children = [];
    this.textContent = "";
    this.className = "";
    this.href = "";
  }}
  append(...children) {{ this.children.push(...children); }}
  replaceChildren(...children) {{ this.children = children; }}
  addEventListener() {{}}
}}
const inputElement = new Element("input");
const sidebarElement = new Element("input");
const resultsElement = new Element("div");
const indexElement = {{ textContent: {json.dumps(json.dumps(index))} }};
globalThis.window = {{ location: {{ search: "?q=anthropic" }} }};
globalThis.document = {{
  querySelector(selector) {{
    return {{
      "#search-index": indexElement,
      "#search-input": inputElement,
      "#search-results": resultsElement,
      'form.search input[name="q"]': sidebarElement,
    }}[selector] || null;
  }},
  createElement(tag) {{ return new Element(tag); }},
}};
{runtime}
const first = results.children[0];
console.log(JSON.stringify({{
  query: input.value,
  sidebarQuery: sidebarInput.value,
  resultCount: results.children.length,
  firstHref: first.href,
  firstTitle: first.children[0].textContent,
}}));
"""

    result = subprocess.run(
        ["node", "--input-type=module", "-e", node_program],
        check=True,
        capture_output=True,
        text=True,
    )

    assert json.loads(result.stdout) == {
        "query": "anthropic",
        "sidebarQuery": "anthropic",
        "resultCount": 1,
        "firstHref": "/companies/anthropic/",
        "firstTitle": "Anthropic",
    }
    assert "innerHTML" not in runtime
