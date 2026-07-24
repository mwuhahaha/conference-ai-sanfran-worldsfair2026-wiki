---
type: orchestration-current
scope: project-local
status: active
updated: 2026-07-24T23:40:38Z
---

# AI Engineer World's Fair 2026 Project State

The completed AIE-specific conversion plan remains closed. Follow-up public navigation work now lives in `.ops/plans/worldsfair-static-navigation-followup.md`.

## 2026-07-24 Official-Video Refresh And Semantic-Digestion Repair

- The pre-repair public corpus is preserved and pushed at checkpoint
  `766bf0f8412afaac5d0a35679d72b18bf637603f` on
  `checkpoint/wf26-pre-semantic-synthesis-2026-07-24`; no PR was opened.
- The monitor found seven additional official playlist entries and processed
  ten records including three unavailable placeholders. Six playable
  recordings were matched to exact scheduled talks and one Jason Liu workshop,
  `il1c1a2FufU`, remains an official resource-only item rather than receiving
  an invented talk association.
- The official-media manifest now contains 67 records: 60 talk recordings,
  3 event livestreams, 1 scheduled premiere, and 3 unavailable playlist
  placeholders. The playlist contains 46 entries: 43 available and 3
  unavailable. Sixty transcripts are cached; the single premiere is pending.
  The 60 talk recordings have typed slide outcomes: 59 cached slide sets and
  one evidence-backed `no_slides` result.
- Talk digestion is now semantic and fail closed. Every admitted digest is
  bound to the exact recording, talk, transcript SHA-256, transcript segment
  IDs, and copied evidence excerpts. Missing or short transcripts, malformed
  model output, and unsupported claims fail the required maker stage instead
  of silently producing template text.
- The canonical wiki contains 54 semantic talk digests, 54 generated claim
  pages, 54 generated highlight pages, and 17 cross-talk topic clusters. Each
  cluster spans at least two talks. The map/reduce and per-talk results use
  content-addressed public caches, so unchanged imports are not re-analyzed.
- Definitive maker run `update-20260724T230407Z-abe3bdf1cc` completed all 20
  stages and promoted
  `promotion:c1ab1f915a20c62fdfc571fa551e7ce8dc968d5d5580d83b0ba42e51adcf3ff0`.
  Public validation passed `agent.snapshot`, `public.boundary`, and
  `wiki.shape`. A subsequent read-only plan is a no-op and confirms canonical
  wiki digest
  `sha256:1f0377bf796962a83a43738f6b2e13fd6af3e505add9dd6566ddddc12c08d1a0`
  and static digest
  `sha256:90b7c137883f8dea7ec25c1d6b07acf588d7b12adf53289bb1a23b408e4fb61a`.
- The aligned agent snapshot is
  `snapshot:d5421cac4a7d4666007dad26e883b5fd84796d1f76db2e7c308298b025d569e0`:
  2,688 pages, 3,844 evidence records, 452 resources, 1,573 entities, 1,684
  relationships, 57 claims, and 12 patterns.
- The project pins wiki-from-topic-maker at
  `c5bc782956d85fdf5d3347858eb2ce49b6054f6a`. Nested Codex adapters now run
  with an ephemeral auth-only Codex home, preventing PATH alias, SQLite, and
  installation-state writes from failing inside the read-only adapter sandbox.
  The fix is pushed on `origin/agent/codex-adapter-runtime-sandbox`.
- `aie-wf2026-youtube-monitor.timer` is enabled and active. It runs every six
  hours via the pinned maker wrapper, with clean-main auto-push and a ten-minute
  failure retry. The first scheduled trigger after re-enablement is
  `2026-07-25T05:40:03Z`.
- Focused project tests, the 285-test non-network project suite, 82 targeted
  maker tests, static validation, full media-role, attendance, livestream,
  digest-binding, and post-promotion no-op checks pass. Receipt:
  `.ops/state/runs/wiki-maker-update-20260724T230407Z-abe3bdf1cc-attempt-001.json`.
  No external deployment was performed.

## 2026-07-20 Search And Official-Media Refresh

- Static search now hydrates both search fields from the `?q=` query string,
  filters immediately on page load, and renders the embedded index through
  text-only DOM APIs. Inline index JSON escapes HTML-sensitive characters.
- The owner-validated official playlist now contains all 43 entries. The
  complete official-media union contains 46 records: 33 playable playlist
  recordings, 3 admitted official event livestreams, 2 scheduled premieres,
  and 8 unavailable playlist placeholders.
- Seven newly playable playlist recordings were imported with transcripts,
  resource pages, slide outcomes, and conservative talk ownership:
  `2JX6JYyQG4Y`, `il1c1a2FufU`, `JvKO40CFq-s`, `8qWIPUia2O8`,
  `GgLQ02aO-hs`, `RGe6EjucbzI`, and `XV2oYi7kojc`.
- Local transcript coverage is 36/36 playable items and typed slide outcomes
  are complete for all 36. The transcript layer contains 132 pages: 36
  primary-event transcripts and 96 supporting-context transcripts.
- Opaque `yt-dlp` placeholders for private/unavailable videos now enter the
  existing unavailable path instead of aborting the whole monitor run.
- Unified maker run `update-20260720T094613Z-28ace9e80c` completed, validated,
  and promoted locally. It was the only maker update in this refresh. Two stale
  primary associations, `o-zkvb0iFDQ` and `sRpqPgKeXNk`, are now durable
  supporting-context records rather than exact-session evidence.
- `raw/sources/livestream-talk-segments.json` is the reviewed semantic
  authority for seven current broad-stream navigation segments (SHA-256
  `4b5a8a13744d23049b60371acf136a5f6b152fbb8933d0a426726271d85c56db`).
  Projection is deterministic, rejects demoted streams, non-high-confidence
  rows, malformed inputs, and cross-talk timestamp collisions, and removes a
  broad segment when a playable dedicated recording supersedes it.
- The matcher now parses valid YAML frontmatter, including the single-quoted
  and multiline forms produced by auto-summary. It computes and validates all
  matches before any write, but is intentionally excluded from the automatic
  maker DAG: ambiguous recomputation is an explicit candidate/operator-review
  workflow and cannot replace the reviewed registry during a media update.
  Attendance derives primary candidates from the raw manifest and reviewed
  segment authority rather than requiring their links to survive in Markdown;
  Main Stage remains calibrated from 2 primary videos and 12 stored evidence
  frames, including Mike Chambers at 03:14:28.
- The maker DAG deliberately keeps projection early but after source
  enrichment: `source_enrichment` -> `livestream_segment_projection` ->
  `attendance_evidence_sync` -> synthesis/evolution/sanitization -> agent index
  -> normalization -> assessment -> static export. Normalization has explicit
  preservation tests for the owned segment, appearance, and attendance
  sections.
- The monitor now performs canonical post-promotion segment, attendance, and
  full media-role gates. This catches the current generic maker limitation that
  candidate raw/source mutations are not promoted with wiki/static outputs.
  Durable match acquisition must remain in the monitor transaction unless the
  generic maker later gains transactional source-root promotion.
- A second external follow-up remains for the hub auto-summary service: it has
  no project opt-out and can rewrite whole pages. This repository now tolerates
  its valid YAML and restores/audits owned sections, but project exclusion or
  section-owned merging belongs in the hub rather than this repository.
- The final aligned agent snapshot is
  `snapshot:fda9f4494156e2236cca37770b54b1ee95d481cf8c2b4a4154aef00392134cd2`:
  2,469 pages, 3,693 evidence records, 431 resources, 1,540 entities, 1,670
  relationships, 3 claims, and 10 patterns. Full project validation passes 349
  tests; the 145-test media/segment/attendance/DAG slice, changed-file Ruff,
  Python compilation, static export, full media-role audit, attendance audit,
  and agent-product build are green. No external deployment was performed.

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
- Definitive run `update-20260717T151153Z-c726308cdf` completed the 18 adapters
  plus maker runtime stages, validated, and promoted locally. Its target
  snapshot is
  `snapshot:7eb9e7909f90fe52706542953a7daa1d3b0009380f93b09f32361d5c868340de`;
  the promoted agent snapshot is
  `snapshot:62900940db784a1c6b68bb19a4a20c0bc14bcd87dae2ef27ee28cbbab0edd1ab`.
- An earlier candidate run, `update-20260717T131302Z-bb9a6a529d`, failed
  before promotion because the agent product was redundantly rebuilt from a
  candidate symlink outside its apparent root. The duplicate build was removed;
  no output from the failed candidate was promoted. Repeating the corrected
  update returns `status: no_op` without execution, validation, promotion, or
  a receipt.
- Candidate run `update-20260717T142712Z-55dddbfd18` failed before promotion
  when attendance sync imported unavailable image libraries. Attendance sync
  now reuses stored detector counts without image dependencies, preserves an
  unchanged contact sheet only when the file still exists, and clears stale
  output fail closed.
- The publishable inventory now follows Git visibility. Ignored untracked local
  overlays are preserved in the operator workspace but excluded from wiki,
  static, agent, graph, and relationship products. Promoted root/static agent
  pointers are reconciled from the verified canonical manifest before every
  mutating update and agree on the configured `dist/` root.
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
- Final validation: 757 maker tests and 310 project tests pass; Ruff, compile,
  and diff checks are clean. All 7,382 publishable files plus 1,998 raw source
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
- The official-media union contains 46 WF26 items. The owner-validated playlist
  contains 43 entries: 33 playable recordings, 2 scheduled premieres, and 8
  unavailable placeholders. Three separately admitted official event
  livestreams complete the union. Local transcript coverage and typed slide
  outcomes are complete for all 36 playable items.
- The transcript layer contains 132 pages: 36 primary-event transcripts and 96
  supporting-context transcripts. Transcript, video, OCR, slide, and synthesis
  roles remain labeled separately.
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
- Latest local validation: 2,417 graph nodes, 9,703 graph links, 17 categories,
  zero broken link endpoints, and headless Chrome desktop/mobile home-page
  smoke coverage.

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
association while the schedule remains canonical for session facts. The latest
union contains 46 records and preserves three separately admitted event
livestreams outside the 43-item playlist.
The earlier channel-scan slice had added or corrected:
- Four playable recordings with cached transcripts, transcript pages, slide/OCR pages, resource pages, and talk synthesis: Pauline Brunet, Addy Osmani, Erik Meijer, and Alex Bauer.
- Two verified scheduled premieres with pending media status: Daniel Han and Pablo Castro. The monitor now revisits manifest premieres and imports captions/slides after they become playable instead of permanently skipping known IDs.
- Three older official recordings that had been treated as supporting context were corrected to primary WF26 event-video status after schedule verification.

Validation at `2026-07-20T12:15:07Z`: all 46 admitted items have typed outcomes,
all 36 playable items have transcripts and slide outcomes, the final agent
snapshot contains 2,469 pages, and the project suite passes 349 tests. Maker,
monitor, and local deterministic validation ran with external publishing
disabled.

## Next Step

Review the local search, monitor, media, and preservation-recovery changes.
Deployment remains a separate explicit operation. The monitor should revisit
the Tariq Shaukat and Lance Martin scheduled premieres and run the same unified
update when their media becomes playable. Return the installed monitor to a
clean `main` checkout before enabling the local six-hour timer.
