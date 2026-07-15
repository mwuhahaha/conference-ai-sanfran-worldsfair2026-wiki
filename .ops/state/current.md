---
type: orchestration-current
scope: project-local
status: active
updated: 2026-07-15T11:05:04-04:00
---

# AI Engineer World's Fair 2026 Project State

The completed AIE-specific conversion plan remains closed. Follow-up public navigation work now lives in `.ops/plans/worldsfair-static-navigation-followup.md`.

## Relationship Explorer Release

- Canonical plan: `.ops/plans/worldsfair-relationship-explorer-plan.md`.
- Status: implementation, deployment, and live verification complete.
- Primary templates: Vendor-Concept, Person-Concept, and Concept-Concept.
- Current corpus: 75 explicit vendors, 555 people, 16 concepts, and 3,063 exact evidence-path relationship records.
- `/graph/` is the search-first explorer; `/graph/all/` preserves the complete wiki-link graph.
- `relationship-data.json` is separate from `graph-data.json`; internal review candidates remain under ignored `.ops/state/cache/` only.
- The reusable implementation and conservative Worldsfair profile producer live in `/garage/obsidian/wiki-from-topic-maker`.
- Deployment: commit `7fabb4c4`, GitHub Actions run `29426268484`, successful.
- Live verification passed on desktop and mobile for all three templates, exact matrix/list totals, evidence drawers, zoom, relation filters, and the advanced dataset.
- Post-release neighborhood refinement is complete: selected entities now link
  to their canonical wiki pages below the graph, and focused scenes support
  URL-restored one-, two-, and three-step expansion with progressive caps up to
  100 nodes and 200 relationships.
- Refinement implementation: commit `995fb20c`, GitHub Actions run
  `29427893690`, successful. Live desktop/mobile checks passed with no page
  errors, failed requests, or document overflow.
- `Entity neighborhood` is now the cross-template person/vendor/concept lookup
  mode. It unions only existing evidence-bearing semantic records: step 1 is
  strictly direct to the selected entity, while the progressive graph action
  adds role-balanced connections-of-connections.
- Entity-neighborhood implementation: commit `d17f7768`, GitHub Actions run
  `29428779987`, successful. The live Corey Gallon check shows 8 direct
  relationships across 9 entities at step 1, then a bounded 50-entity/100-edge
  step-2 scene, with the canonical `/people/corey-gallon/` link intact.
- Next single story returns to S3 in `.ops/plans/worldsfair-static-navigation-followup.md`.

## Latest Completed Follow-Up Stories

- S1: static knowledge graph.
- `scripts/export_static_site.py` now emits the complete resolved wiki-link graph to `dist/graph-data.json`.
- `/graph/` provides category filtering, search, a category legend, node detail, and nearby-page links without adding a server or write path.
- The shared sidebar now includes Graph.
- S2: conference-native home.
- `/` now renders a static event/source dashboard instead of the long article-first overview.
- The S2 design was refined after review: the home page now uses a clearer event brief, compact fact panel, start-here strip, source-boundary guidance, count summary, and row-based event/source lists instead of many equal-weight cards.
- Latest local validation: 2,412 graph nodes, 10,971 graph links, 21 categories, zero broken link endpoints, and headless Chrome desktop/mobile home-page smoke coverage.

The AIE-specific conversion plan is complete. The active plan remains `.ops/plans/worldsfair-aie-specific-conversion-plan.md`, but S1-S9 are now checked off and should not be reopened unless the user explicitly asks to revise that plan.

## Current Shape
- The clean wiki is a publishable AIE conference intelligence vault, not only a generated schedule archive.
- Official schedule, people, companies, talks, resources, transcripts, slides, reconstructed slides, dense slides, topic pages, tools, questions, harnesses, playbooks, evaluations, policies, and source-boundary resources are all linked from `wiki/index.md`.
- Exhaustive generated listings remain reachable through category pages and registries instead of dominating the main index.

## Latest Completed Run
- Receipt: `.ops/state/runs/20260710T014441Z-synthesis-layers.md`
- Generator: `scripts/generate_synthesis_layers.py`
- Outputs:
  - `wiki/harnesses/` with 5 seeded harness pages and `registry.json`
  - `wiki/playbooks/` with 3 seeded playbooks and `registry.json`
  - `wiki/evaluations/` with 6 comparative/policy evaluation pages and `registry.json`
  - `wiki/policies/` with 5 topic-specific credibility policy pages and `registry.json`
  - `raw/sources/credibility-policies/` with one JSON policy per topic
  - `raw/sources/credibility-policy-evals.json` with 10 passing high-exemplar fixtures
  - `wiki/resources/livestream-thematic-anchors.md`
  - `raw/sources/topic-evidence-table-summary.json`

## Credibility Policy Boundary
- Credibility scoring is topic-specific. Do not use a single global credibility score across coding agents, evals, search, sandboxes, and inference.
- Some topics give public attention or view count meaningful weight; others treat it as weak context. The policy file must explain which case applies.
- Change one policy JSON at a time under `raw/sources/credibility-policies/`, add or adjust eval fixtures, then rerun `python3 scripts/generate_synthesis_layers.py`.
- `wiki/evaluations/credibility-policy-evals.md` is the human-readable eval report; all 10 fixtures passed in the latest run.

## Automation Update
Future native YouTube import receipts now include `slideScanMode` through:
- `/garage/obsidian/scripts/native_youtube_slide_scan.py`
- `/garage/obsidian/plugins/agent-workbench/skills/youtube-url-import-orchestrator/scripts/run_youtube_import_orchestrator.py`

The receipt payload records Tesseract primary OCR, RapidOCR fallback availability/usage, and explicit reconstructed-crop/dense-scene status.

## Next Step

Implement S3 in `.ops/plans/worldsfair-static-navigation-followup.md`: generate build-time backlinks, outgoing links, and nearby-page sections for rendered pages. Keep this separate from category landing-page improvements and talk/source-bundle panels.
