---
type: orchestration-current
scope: project-local
status: active
updated: 2026-07-17T05:27:22Z
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
- Run `update-20260717T051453Z-43aefe0a3d` completed all 16 stages, validated,
  and promoted locally. Its machine receipt is
  `.ops/state/runs/wiki-maker-update-20260717T051453Z-43aefe0a3d-attempt-001.json`;
  the operator summary is
  `.ops/state/runs/20260717T052722Z-playlist-credibility-article-migration.md`.
- The promoted target snapshot is
  `snapshot:b00976ab3a3272e1f2532a9db296cb97c522bed892725c8b4258b63c54be5711`;
  its agent snapshot is
  `snapshot:521c817de54118bbd2190c616edb5991f0355859040dcbcc9e663f10eb1c74c2`.
  Repeating the identical update returns a planning no-op with no execution,
  validation, promotion, or receipt.
- The run performed no external deployment. Publication remains a separate,
  explicit operation.
- The official-media union contains 34 WF26 items: 26 recordings, 3 scheduled
  premieres, 2 unavailable playlist placeholders, and 3 event livestreams.
  All 29 official-playlist entries are represented; its 24 playable recordings
  have cached transcripts.
- The transcript layer contains 123 pages: 28 primary-event transcripts and 95
  supporting-context transcripts. Transcript, video, OCR, slide, and synthesis
  roles remain labeled separately. Playlist slide outcomes are 23 cached, 1
  `no_slides`, 3 pending, and 2 unavailable.
- Private review-policy bootstrap data lives only at ignored
  `.ops/state/cache/wiki-maker/private-policy.json`, as declared by the profile.
  Provider/browser receipts, claim assessments, candidate profiles, and writing
  decisions remain under ignored `.ops/state/cache/wiki-maker/credibility-v2/`.
  Their contents must never enter tracked or public outputs.

## Relationship Explorer Release

- Canonical plan: `.ops/plans/worldsfair-relationship-explorer-plan.md`.
- Status: implementation, deployment, and live verification complete.
- Primary templates: Vendor-Concept, Person-Concept, and Concept-Concept.
- Current local corpus: 75 explicit vendors, 555 people, 16 concepts, and 1,598
  exact evidence-path relationship records: 308 Vendor-Concept, 813
  Person-Concept, and 477 Concept-Concept.
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

The updated user unit was installed and verified at `2026-07-16T07:47:25Z`.
For the bounded playlist/maker migration, the timer was disabled before source
acquisition and remains disabled and inactive. This branch is intentionally
dirty and the installed auto-push service requires a clean `main` checkout;
restore the six-hour timer only after review/commit returns operations to that
safe state.

The official-video ingest was expanded on 2026-07-16 from RSS-only discovery to
a bounded official-channel scan, then on 2026-07-17 to complete reconciliation
against the official WF26 playlist. Playlist membership now establishes event
association while the schedule remains canonical for session facts. The final
union contains 34 records and preserves separately admitted event livestreams
and recordings outside the playlist.
The earlier channel-scan slice had added or corrected:
- Four playable recordings with cached transcripts, transcript pages, slide/OCR pages, resource pages, and talk synthesis: Pauline Brunet, Addy Osmani, Erik Meijer, and Alex Bauer.
- Two verified scheduled premieres with pending media status: Daniel Han and Pablo Castro. The monitor now revisits manifest premieres and imports captions/slides after they become playable instead of permanently skipping known IDs.
- Three older official recordings that had been treated as supporting context were corrected to primary WF26 event-video status after schedule verification.

Validation at `2026-07-17T05:27:22Z`: all 29 playlist items have typed outcomes,
all 24 playable playlist recordings have primary-event transcript coverage,
229 project tests pass, article normalization is idempotent, and the static
export contains 2,438 Markdown-identical pages.

## Next Step

Review and commit the maker/WF26 changes before restoring the local six-hour
monitor. Push/deployment remain separate explicit operations. The monitor will
revisit the three scheduled premieres and run the same unified update when
their media becomes playable.
