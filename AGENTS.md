# AGENTS

Project-local instructions for the clean AI Engineer World’s Fair 2026 wiki.

Read first:
1. `.ops/state/current.md`
2. `.ops/plans/worldsfair-static-navigation-followup.md`
3. `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
4. `README.md`
5. The public standalone repo: `https://github.com/mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki`
6. `wiki/resources/agent-source-index.md`

## Public Repo Structure

This clean checkout and the public GitHub repo are the canonical references for the publishable markdown structure. Before a visiting agent adds categories, changes frontmatter, reshapes page sections, or writes new generator output, it should inspect existing pages in this repo and follow the established markdown shape.

Keep new pages compatible with the public repo conventions:
- YAML frontmatter with `title`, `category`, and source/status fields where applicable.
- Section names and ordering that match existing pages in the same category.
- Run `python3 scripts/normalize_article_shapes.py` after broad generation or enrichment. It preserves type-specific shapes: talks are session articles, people are profile articles, companies are organization articles, topics are concept articles, and question/harness/playbook/evaluation pages are synthesis articles. Prefer agent-friendly section names such as `Overview`, `Conference Context`, `Significance`, `Technical Model`, `Applied Use`, `Connections`, and `Evidence Graph` over visible `What/Why/How` outlines.
- Evidence links as wikilinks to local source pages, not unsourced prose.
- Agent-facing wiki navigation belongs in `wiki/resources/agent-source-index.md`; the static build also publishes it without the site frame at `/agent-index.md`.
- Every rendered wiki page must have an agent-readable markdown backing file under `/md/`. Keep this exporter behavior enabled for all wiki-maker builds.
- Pages that deserve extra operator attention belong in `raw/sources/highlighted-targets.json`; run `python3 scripts/generate_highlights.py` and expand the target page itself with recording/source status, related people, companies, tools, and evidence boundaries.
- When a talk introduces a novel concept, hack, method, or unusually useful framing, create or update the corresponding topic/tool page and add it to `raw/sources/highlighted-targets.json`; the highlight generator publishes the grouped map at `wiki/highlights/highlighted-concepts-people-talks.md`.
- Cached YouTube and livestream transcript text should be exposed as linkable wiki markdown. After transcript imports, run `python3 scripts/generate_transcript_markdown_pages.py`; it creates `wiki/transcripts/`, adds bottom `## Transcript Markdown` links to matching resource and talk pages, and refreshes the transcript registry.
- Talk pages should not stop at official descriptions when transcript or strong source context exists. Run `python3 scripts/generate_talk_synthesis.py --speaker "Name"` or `--all` to add `## Synthesis` sections with transcript-backed breakdowns, speaker/company context, topic links, derived links, and highlighted concept signals.
- After source enrichment, topic generation, company enrichment, talk synthesis, or slide-evidence imports, run `python3 scripts/normalize_article_shapes.py` before building or committing. `npm run build` also runs the normalizer before static export.
- High-level event-evolution context belongs in `raw/sources/evolution-context-profile.json` and is applied with `python3 scripts/enrich_evolution_context.py --all`. Keep the profile portable, require linked local evidence before emitting current-event synthesis, and treat prior-event wikis as labeled comparison context rather than primary current-event evidence.
- Weak or suspicious slide OCR should be reread through the full slide OCR pipeline. Run `python3 scripts/run_slide_ocr_pipeline.py`; it calls the OCR merge tool with crop/high-contrast/OpenCV variants, refreshes slide pages, regenerates dependent tool/topic/word-cloud indexes, and rebuilds the static site. For a fuller non-perfect-slide pass, run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --internal-eval-log`. Optional engines are feature-detected; use PaddleOCR, EasyOCR, docTR, or Surya as targeted rescue engines rather than default whole-corpus readers on this host. Do not enable Surya unless its model-weight license terms have been checked for the use case. When OCR remains visibly bad, use AI vision rescue: `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --vision-rescue --vision-provider codex-cli --internal-eval-log`. It writes accepted model-read text to `raw/sources/slide-ocr-ai-vision/`, resumes from existing accepted files there, and can run bounded parallel Codex CLI reads with `--vision-jobs 2` or `--vision-jobs 3`. It prefers free local Ollama vision when available, then Codex CLI through the existing local login, and uses OpenAI only when configured. Codex CLI vision rescue defaults to `gpt-5.4-mini`; override it with `CODEX_VISION_MODEL` or `--vision-codex-model`. If a human operator can read slide text that tools cannot, add a backing text file under `raw/sources/slide-ocr-operator-verified/<video-id>/<slide>.txt`, then run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --no-live-ocr --internal-eval-log`. The audits live at `raw/sources/slide-ocr-rapidmerge-audit.json`, `raw/sources/slide-ocr-ai-vision-audit.json`, `wiki/resources/slide-ocr-rapidmerge-audit.md`, and `wiki/resources/slide-ocr-ai-vision-audit.md`; ignored operator/tool comparison logs live under `.ops/state/cache/`.
- New video slide imports should prefer scene-aware frame selection when possible: `python3 scripts/extract_video_slides.py --scene-detect --video-id <id>` samples both interval and scene-change frames, then keeps sharper duplicates.
- External/non-official YouTube discovery belongs in `scripts/discover_external_event_videos.py`. Run `python3 scripts/discover_external_event_videos.py --write-wiki --import-high-confidence --update-talk-pages` to find high-confidence secondary-source candidates, cache captions when available, update `wiki/resources/external-video-discovery.md`, and add explicit secondary-source links to matched talk pages.
- Registry files such as `wiki/tools/registry.json`, `wiki/questions/registry.json`, and category indexes when a category has generated pages.
- Internal scoring artifacts belong only under ignored project-local state. Do not publish weights, calibration fixtures, score reports, or scoring-policy pages into `wiki/`, `raw/sources/`, `dist/`, or the agent index.
- No local-only workspace notes, private caches, or unpublishable files in the clean/public wiki.

## Purpose

This is an AIE-specific conference intelligence wiki for AI Engineer World’s Fair 2026 in San Francisco.

It should preserve the official schedule/media evidence layer while adding Miami-style synthesis:
- tools and protocols as first-class entities
- content-derived topics and graph clusters
- questions raised by the conference
- claims grounded in official schedule, transcripts, slide OCR, reconstructed slides, or resources
- reusable AI engineering patterns, harnesses, playbooks, and evaluations when evidence supports them

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

`wiki/topics/agentic-web.md` is a generated schedule-specific topic page for talks about agent-facing web surfaces, browser/web automation, computer-use web navigation, agent-readable catalogs, and HTML/web substrates for agents. It should remain a topic, not a top-level standalone category.
