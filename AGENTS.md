# AGENTS

Project-local instructions for the clean AI Engineer World’s Fair 2026 wiki.

Read first:
1. `.ops/state/current.md`
2. `.ops/plans/worldsfair-static-navigation-followup.md`
3. `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
4. `README.md`
5. The public standalone repo: `https://github.com/mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki`
6. `wiki/resources/agent-source-index.md`

## Update Workflow

`.wiki-maker.json` is the orchestration contract for this project. For an
official-media change, run the single authoritative update from this repository:

```bash
wiki-from-topic-maker update . \
  --change-type media \
  --source raw/sources/official-wf26-video-manifest.json \
  --json
```

This is the production entry point for classification, transcript pages, talk
synthesis, source enrichment, synthesis layers, evolution context,
normalization, static export, relationship data, the agent product, validation,
and local promotion. Direct generator or exporter scripts are for bounded
stage-level debugging only and do not constitute a completed update. Source
acquisition and audit tools may prepare inputs, but the resulting change must
still pass through the maker.

The media profile has 18 ordered adapters. Preserve its fail-closed tail:
`sanitize_public_text` -> `agent_source_index` -> `normalize_articles` ->
`page_assessments` -> `static_export`. `build:validated` performs the candidate
slide gate and static export; the maker runtime builds and validates the agent
product separately before promotion. Do not add a second agent-product build to
the candidate static-export command.

The official YouTube monitor invokes this maker update once after admitting new
event media. Keep that single-call boundary intact; do not restore a second
monitor-specific generator chain.

Recurring monitor runs must owner-validate and reconcile the complete official
WF26 playlist before unioning strictly year/date-gated official-channel
discovery. Preserve scheduled and unavailable playlist members. The monitor's
mutation journal and post-push local-sync journal are distinct crash-recovery
contracts: roll back failed local/publication mutations, but never roll back a
remote commit after its publication has been verified.

The profile's private input is bootstrapped locally at the ignored path
`.ops/state/cache/wiki-maker/private-policy.json`. Never publish that file or
any of its contents to `wiki/`, `raw/sources/`, `dist/`, the agent index, or
another tracked/public artifact. Provider/browser receipts, acquisition
candidates, evidence assessments, and writing decisions likewise remain under
ignored `.ops/state/cache/wiki-maker/credibility-v2/` state. Public adapters may
project only reviewed, attributed context and categorical provenance.

Assess every canonical entity/article page, including official primary-source
pages. Assessment never excludes official event evidence. Public Markdown and
agent records may carry categorical evidence-coverage capsules; human HTML may
show fixed friendly notices only for configured edge states. Never publish
numeric scores, signed line items, weights, thresholds, calibration, ranking
order, or the construction of the private receipt.

Slide AI cache hits must bind the exact source image, model, prompt,
configuration, input, and output. Publish classifier/OCR outcomes atomically;
stale or partial results must fail closed. Codex processing of untrusted web or
media content defaults to read-only execution without local tools.

## Public Repo Structure

This clean checkout and the public GitHub repo are the canonical references for the publishable markdown structure. Before a visiting agent adds categories, changes frontmatter, reshapes page sections, or writes new generator output, it should inspect existing pages in this repo and follow the established markdown shape.

Keep new pages compatible with the public repo conventions:
- YAML frontmatter with `title`, `category`, and source/status fields where applicable.
- Section names and ordering that match existing pages in the same category.
- The maker's normalization stage preserves type-specific shapes: talks are session articles, people are profile articles, companies are organization articles, topics are concept articles, and question/harness/playbook/evaluation pages are synthesis articles. Prefer agent-friendly section names such as `Overview`, `Conference Context`, `Significance`, `Technical Model`, `Applied Use`, `Connections`, and `Evidence Graph` over visible `What/Why/How` outlines.
- Evidence links as wikilinks to local source pages, not unsourced prose.
- Agent-facing wiki navigation belongs in `wiki/resources/agent-source-index.md`; the static build also publishes it without the site frame at `/agent-index.md`.
- Every rendered wiki page must have an agent-readable markdown backing file under `/md/`. Keep this exporter behavior enabled for all wiki-maker builds.
- Pages that deserve extra operator attention belong in `raw/sources/highlighted-targets.json`; the configured update should publish the resulting highlight changes. Expand the target page itself with recording/source status, related people, companies, tools, and evidence boundaries.
- When a talk introduces a novel concept, hack, method, or unusually useful framing, create or update the corresponding topic/tool page and add it to `raw/sources/highlighted-targets.json`; the highlight generator publishes the grouped map at `wiki/highlights/highlighted-concepts-people-talks.md`.
- Cached YouTube and livestream transcript text should be exposed as linkable wiki markdown. After transcript imports, run the maker update; its transcript stage creates `wiki/transcripts/`, adds bottom `## Transcript Markdown` links to matching resource and talk pages, and refreshes the transcript registry.
- Talk pages should not stop at official descriptions when transcript or strong source context exists. The maker's talk-synthesis stage adds transcript-backed `## Synthesis` sections with speaker/company context, topic links, derived links, and highlighted concept signals.
- After source enrichment, topic generation, company enrichment, talk synthesis, or slide-evidence imports, run the maker update before building or committing. Direct normalization and export commands are diagnostic checks; `npm run build` also normalizes before static export.
- High-level event-evolution context belongs in `raw/sources/evolution-context-profile.json` and is applied by the maker. Keep the profile portable, require linked local evidence before emitting current-event synthesis, and treat prior-event wikis as labeled comparison context rather than primary current-event evidence.
- Weak or suspicious slide OCR should be reread through the full slide OCR pipeline. Run `python3 scripts/run_slide_ocr_pipeline.py`; it calls the OCR merge tool with crop/high-contrast/OpenCV variants, refreshes slide pages, regenerates dependent tool/topic/word-cloud indexes, and rebuilds the static site. For a fuller non-perfect-slide pass, run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --internal-eval-log`. Optional engines are feature-detected; use PaddleOCR, EasyOCR, docTR, or Surya as targeted rescue engines rather than default whole-corpus readers on this host. Do not enable Surya unless its model-weight license terms have been checked for the use case. When OCR remains visibly bad, use AI vision rescue: `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --vision-rescue --vision-provider codex-cli --internal-eval-log`. It writes accepted model-read text to `raw/sources/slide-ocr-ai-vision/`, resumes from existing accepted files there, and can run bounded parallel Codex CLI reads with `--vision-jobs 2` or `--vision-jobs 3`. It prefers free local Ollama vision when available, then Codex CLI through the existing local login, and uses OpenAI only when configured. Codex CLI vision rescue defaults to `gpt-5.4-mini`; override it with `CODEX_VISION_MODEL` or `--vision-codex-model`. If a human operator can read slide text that tools cannot, add a backing text file under `raw/sources/slide-ocr-operator-verified/<video-id>/<slide>.txt`, then run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --no-live-ocr --internal-eval-log`. The audits live at `raw/sources/slide-ocr-rapidmerge-audit.json`, `raw/sources/slide-ocr-ai-vision-audit.json`, `wiki/resources/slide-ocr-rapidmerge-audit.md`, and `wiki/resources/slide-ocr-ai-vision-audit.md`; ignored operator/tool comparison logs live under `.ops/state/cache/`.
- New video slide imports should prefer scene-aware frame selection when possible: `python3 scripts/extract_video_slides.py --scene-detect --video-id <id>` samples both interval and scene-change frames, then keeps sharper duplicates.
- External/non-official YouTube discovery belongs in `scripts/discover_external_event_videos.py` and is supporting-source investigation only. Keep candidate review material private, do not infer an event association from the tool alone, label any accepted public source as supporting context, and pass resulting source changes through the maker update.
- Registry files such as `wiki/tools/registry.json`, `wiki/questions/registry.json`, and category indexes when a category has generated pages.
- Private review and trust-assessment material belongs only under ignored project-local state. Do not publish internal policy, candidate-prioritization, calibration, or audit artifacts into `wiki/`, `raw/sources/`, `dist/`, or the agent index.
- Third-party connections must pass separate identity and event-association gates before private review can influence publication. A shared name, repository name, guessed domain, exact shared profile URL, or popularity signal is never sufficient proof. Publication as labeled comparison/context also does not mean the wiki endorses the source or its claims.
- Run `python3 scripts/audit_third_party_connections.py` to write the internal candidate report under ignored `.ops/state/cache/third-party-connections/`; use `--check` for a no-write audit. The audit reports candidates and must not rewrite public wiki relationships automatically.
- Person-connection discovery runs through `python3 scripts/link_individuals.py`. It compares every local person pair, treats external profiles and repositories as evidence leads rather than automatic proof, and stores private review material only under ignored `.ops/state/cache/person-linking/`.
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

For company-page enrichment, acquisition candidates default to ignored
`.ops/state/cache/wiki-maker/credibility-v2/company-profile-candidates.json`.
`scripts/enrich_company_pages.py` may project only the private policy's accepted,
attributed subset and must not overwrite curated prose. The legacy
`raw/sources/company-profiles.json` path is explicit-only compatibility input,
not the default acquisition destination.

`wiki/topics/agentic-web.md` is a generated schedule-specific topic page for talks about agent-facing web surfaces, browser/web automation, computer-use web navigation, agent-readable catalogs, and HTML/web substrates for agents. It should remain a topic, not a top-level standalone category.
