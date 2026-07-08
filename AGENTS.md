# AGENTS

Project-local instructions for the clean AI Engineer World’s Fair 2026 wiki.

Read first:
1. `.ops/state/current.md`
2. `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
3. `README.md`
4. The public standalone repo: `https://github.com/mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki`
5. `wiki/resources/agent-source-index.md`

## Public Repo Structure

This clean checkout and the public GitHub repo are the canonical references for the publishable markdown structure. Before a visiting agent adds categories, changes frontmatter, reshapes page sections, or writes new generator output, it should inspect existing pages in this repo and follow the established markdown shape.

Keep new pages compatible with the public repo conventions:
- YAML frontmatter with `title`, `category`, and source/status fields where applicable.
- Section names and ordering that match existing pages in the same category.
- Evidence links as wikilinks to local source pages, not unsourced prose.
- Agent-facing source navigation belongs in `wiki/resources/agent-source-index.md`; update it when new source layers or source-link rules are added.
- Registry files such as `wiki/tools/registry.json`, `wiki/questions/registry.json`, and category indexes when a category has generated pages.
- No local-only workspace notes, private caches, or unpublishable files in the clean/public wiki.

## Purpose

This is an AIE-specific conference intelligence wiki for AI Engineer World’s Fair 2026 in San Francisco.

It should preserve the official schedule/media evidence layer while adding Miami-style synthesis:
- tools and protocols as first-class entities
- content-derived topics and graph clusters
- questions raised by the conference
- claims grounded in official schedule, transcripts, slide OCR, reconstructed slides, or resources
- reusable AI engineering patterns/playbooks when evidence supports them

## Boundaries

- Keep official schedule facts distinct from supporting YouTube videos, transcripts, OCR, and inferred synthesis.
- Treat useful public "sources of sources" as part of normal wiki enrichment when they clarify the conference graph: speaker-provided social/profile links, official company sites, public professional profiles, product docs, and related public source pages are allowed when directly relevant.
- Label source layers clearly. Do not blend company/profile-site context into official schedule facts.
- Save available LinkedIn, X/Twitter, website, and blog links from the official speaker roster on people pages near the role/company section.
- Company pages should be full articles whenever possible: explain what the company does, why it matters to the conference, which people and scheduled sessions connect to it, and which public company/profile sources support the context.
- Do not delete generated schedule/media evidence pages.
- Do not promote OCR-only text into confident claims without labeling the source.
- Prefer content-derived topic/knowledge graph organization over copying Miami’s exact category set.
- Keep this AIE-specific; do not mix unrelated personal/local wiki material into this project.

## Clean Copy Note

This clean directory excludes heavy regeneration caches such as downloaded videos and temporary frame samples. Use source artifacts under `raw/sources/`, wiki assets, and scripts first. If full media regeneration is needed, use the original non-clean project directory.

For company-page enrichment, use `raw/sources/company-profiles.json` for curated public company-site/profile context and `scripts/enrich_company_pages.py` for conservative updates that avoid overwriting already curated pages.

`wiki/agentic-web/` is a generated schedule-specific category for talks about agent-facing web surfaces, browser/web automation, computer-use web navigation, agent-readable catalogs, and HTML/web substrates for agents.
