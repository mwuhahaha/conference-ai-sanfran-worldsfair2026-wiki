---
type: orchestration-current
scope: project-local
status: active
updated: 2026-07-16T22:14:28Z
---

# AI Engineer World's Fair 2026 Project State

The completed AIE-specific conversion plan remains closed. Follow-up public navigation work now lives in `.ops/plans/worldsfair-static-navigation-followup.md`.

## E11 Unified Maker Integration

- `.wiki-maker.json` is now the project profile and orchestration contract for
  incremental wiki maintenance.
- The authoritative official-media update is:

  ```bash
  wiki-from-topic-maker update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --json
  ```

- The official YouTube monitor invokes that update once after admitting new
  event media. Direct generator, enricher, normalizer, and exporter calls are
  stage-level debugging tools only.
- Run `update-20260716T215951Z-e366f7cbd6` completed validation and promoted
  locally. Its machine receipt is
  `.ops/state/runs/wiki-maker-update-20260716T215951Z-e366f7cbd6-attempt-001.json`;
  the operator summary is
  `.ops/state/runs/20260716T215951Z-e11-maker-integration.md`.
- Its agent snapshot is
  `snapshot:2c83d7569c73047af50d86924ca8eaf7ca073fb6894af029cfc6450fda9e22bd`.
  Repeating the same update returns a no-op because its inputs, profile, and
  promoted output digests are unchanged.
- The run performed no external deployment. Publication remains a separate,
  explicit operation.
- The official-media manifest remains at 22 admitted WF26 items: 17 recordings,
  2 scheduled premieres, and 3 event livestreams.
- The transcript layer contains 114 pages: 18 primary-event transcripts and 96
  supporting-context transcripts. Transcript, video, OCR, slide, and synthesis
  roles remain labeled separately.
- Private review-policy bootstrap data lives only at ignored
  `.ops/state/cache/wiki-maker/private-policy.json`, as declared by the profile.
  Its contents must never enter tracked or public outputs.

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
- Entity neighborhoods now overlay the separately labeled wiki-navigation
  layer, center the selected article with a distinct color, arrange each hop in
  radial rings, reveal deeper labels through zoom, and make Fit recompute the
  radial organization before resetting the camera.
- Radial/navigation implementation: commit `bc5f296e`, GitHub Actions run
  `29429936213`, successful. The live Corey Gallon direct scene contains 31
  edges across 30 articles, including linked companies, highlights, resources,
  slides, talks, tools, topics, and transcripts. Desktop/mobile checks passed
  without page errors, failed requests, or document overflow.
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
- Official schedule, people, companies, talks, resources, transcripts, slides, reconstructed slides, dense slides, topic pages, tools, questions, harnesses, playbooks, evaluations, and source-boundary resources are all linked from `wiki/index.md`.
- Exhaustive generated listings remain reachable through category pages and registries instead of dominating the main index.

## Automation Update
Future native YouTube import receipts now include `slideScanMode` through:
- `/garage/obsidian/scripts/native_youtube_slide_scan.py`
- `/garage/obsidian/plugins/agent-workbench/skills/youtube-url-import-orchestrator/scripts/run_youtube_import_orchestrator.py`

The receipt payload records Tesseract primary OCR, RapidOCR fallback availability/usage, and explicit reconstructed-crop/dense-scene status.

The project-local official YouTube monitor was hardened in commit `324e0e2c`:
- RSS network and XML parse failures retry three times and now leave a durable degraded receipt if exhausted.
- systemd retries failed runs after 10 minutes, bounded to three starts per hour.
- unchanged RSS metadata no longer creates snapshot-only commits, and runs with no new event videos skip enrichment and static rebuilding.
- `--dry-run` no longer mutates the tracked RSS snapshot.
- the auto-push path refuses to run in a dirty worktree so it cannot commit unrelated operator changes.

The updated user unit was installed and verified at `2026-07-16T07:47:25Z`. The controlled systemd run exited successfully with `state: active`, six recent confirmed WF2026 event entries, zero new entries, and a clean `main` checkout synchronized with `origin/main`. The timer remains enabled on its six-hour cadence.

The official-video ingest was expanded on 2026-07-16 from RSS-only discovery to a bounded scan of the latest 100 official-channel uploads, with exact schedule/speaker evidence required before admission. The durable verified manifest now contains 22 WF26 media items: 17 recordings, 2 scheduled premieres, and 3 event livestreams. This run added six previously missing official items:
- Four playable recordings with cached transcripts, transcript pages, slide/OCR pages, resource pages, and talk synthesis: Pauline Brunet, Addy Osmani, Erik Meijer, and Alex Bauer.
- Two verified scheduled premieres with pending media status: Daniel Han and Pablo Castro. The monitor now revisits manifest premieres and imports captions/slides after they become playable instead of permanently skipping known IDs.
- Three older official recordings that had been treated as supporting context were corrected to primary WF26 event-video status after schedule verification.

Validation at `2026-07-16T08:44:32Z`: the live 100-video scan found no additional unprocessed verified WF26 uploads, all 43 tests passed, and the static export completed with 2,408 pages.

## Next Step

Implement S3 in `.ops/plans/worldsfair-static-navigation-followup.md`: generate build-time backlinks, outgoing links, and nearby-page sections for rendered pages. Keep this separate from category landing-page improvements and talk/source-bundle panels.
