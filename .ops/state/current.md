---
type: orchestration-current
scope: project-local
status: active
updated: 2026-07-17T13:47:04Z
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
- The media profile now has 18 ordered adapters. Its fail-closed tail is
  `sanitize_public_text` -> `agent_source_index` -> `normalize_articles` ->
  `page_assessments` -> `static_export`; the maker then builds and validates
  the agent product before promotion.
- Definitive run `update-20260717T132348Z-4d6cb4d754` completed the 18 adapters
  plus maker runtime stages, validated, and promoted locally. Its target
  snapshot is
  `snapshot:81f654182c28bd0eec179d4cf0c5a303c55b825b1366cdca8cf0292d78e7ce35`;
  the promoted agent snapshot is
  `snapshot:c7e4ef0e07ffb79d4d158cf9e8664d8770e8c7ef546de4769b5742c41ab639bc`.
- An earlier candidate run, `update-20260717T131302Z-bb9a6a529d`, failed
  before promotion because the agent product was redundantly rebuilt from a
  candidate symlink outside its apparent root. The duplicate build was removed;
  no output from the failed candidate was promoted. Repeating the corrected
  update returns `status: no_op` without execution, validation, promotion, or
  a receipt.
- The run performed no external deployment. Publication remains a separate,
  explicit operation.
- Auditable credibility-v2 closure is complete. Definitive run
  `update-20260717T094843Z-76cef8004f` completed all 14 selected third-party
  stages, passed public and article-shape validation, and produced a no-op
  promotion because the public wiki/site digests were unchanged. The identical
  follow-up request returned a planning no-op without a run or receipt.
- Private receipts now bind exact signed line items to immutable evidence and
  ruleset snapshots, replay before finalization, and distinguish arithmetic
  replay, append-only provenance, and live-source rehashing. Exact correction
  and remediation reversals are uncapped, unfactored, and globally single-use.
- Final validation: 750 maker tests and 302 project tests pass; Ruff, compile,
  and diff checks are clean. All 7,384 publishable files plus 1,998 raw source
  files pass the private-ranking boundary. Numeric values, weights, thresholds,
  and ranking internals remain ignored private state.
- Every held company-profile candidate now has an explicit `omit` decision.
  The internal audit verifies all 300 held candidates are absent from public
  artifacts and fails on any future held candidate lacking that decision.
- All 975 canonical entity/article pages have evidence-coverage assessments:
  953 are `limited`, 22 are `pending`, and none currently meet `strong` or
  `contested`. Official primary-source pages are never omitted because of an
  assessment. Public Markdown carries categorical evidence capsules; the human
  site shows fixed friendly notices only at configured edge states and does not
  expose ordinary limited-state notices or numeric scores.
- The official-media union contains 34 WF26 items. A live owner-validated
  playlist dry-run found no new playlist IDs: 29 are playable, 3 scheduled, and
  2 unavailable. Local transcript coverage is 25/29 playable items and slide
  outcomes are complete for 29/29; four playable items retain explicit
  transcript gaps rather than fabricated or misclassified content.
- The transcript layer contains 123 pages: 28 primary-event transcripts and 95
  supporting-context transcripts. Transcript, video, OCR, slide, and synthesis
  roles remain labeled separately. Playlist slide outcomes are 23 cached, 1
  `no_slides`, 3 pending, and 2 unavailable.
- Private review-policy bootstrap data lives only at ignored
  `.ops/state/cache/wiki-maker/private-policy.json`, as declared by the profile.
  Provider/browser receipts, claim assessments, candidate profiles, and writing
  decisions remain under ignored `.ops/state/cache/wiki-maker/credibility-v2/`.
  Their contents must never enter tracked or public outputs. Full signed +/-
  receipts remain replayable there for operator audit.

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
- A 2026-07-17 local release check reconfirmed graph data, connection lines,
  node selection, canonical wiki links, zoom, Fit, and step expansion. It also
  found a separate presentation follow-up: entity-neighborhood labels collide
  or clip at the graph boundary, especially on mobile, and the mobile expansion
  control can obscure the legend. The graph also requires its current `esm.sh`
  Sigma/Graphology dependency at runtime and does not initialize offline.
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

The current monitor adds two durable transaction boundaries. A mutation journal
restores wiki, raw, static, and root agent-index state after pre-publish failure;
a separate post-push local-sync journal closes the remote-published/local-HEAD
crash window without rolling back content already verified on the remote. Normal
recurring runs owner-validate and reconcile the complete official playlist, then
union it with strictly year/date-gated official-channel discovery. Scheduled and
unavailable playlist members stay represented and wrong-year media fails closed.

Slide AI publication is now content-addressed against the exact image, model,
prompt, configuration, input, and output. Classifier or OCR failures cannot
publish partial state or poison a later cache hit. Historical repair restored
599 exact backups, confirmed 2 already-correct records, quarantined 200 stale
audits, withheld 108 unsupported sections, and removed 1,498 stale HTML assets.
Codex-based reads of untrusted media default to read-only execution without local
tools. Public classifier status remains categorical; exact gate reports remain
ignored private state.

The updated user unit was installed and verified at `2026-07-16T07:47:25Z`.
For the bounded playlist/maker migration, the timer was disabled before source
acquisition and remains disabled and inactive. Its prior failed status came
from the expected feature-branch/dirty-checkout preflight refusal,
not a media-processing failure, and has been cleared without starting the
service. The service and timer are now inactive and the timer remains disabled.
The installed auto-push service requires a clean `main` checkout; restore the
six-hour timer only after the feature branch is reviewed and merged into that
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

Validation at `2026-07-17T13:42:36Z`: the live recurring dry-run found no new
playlist IDs and left the worktree unchanged. The union has typed outcomes for
all 34 admitted items; the static and agent builds contain 2,438
Markdown-identical pages, and article normalization is idempotent.

## Next Step

Review and merge the pushed maker and WF26 feature branches, return the installed
monitor to a clean `main` checkout, then enable the local six-hour timer.
Deployment remains a separate explicit operation. The monitor will
revisit scheduled premieres and run the same unified update when their media
becomes playable.
