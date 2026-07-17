# WF26 Playlist, Credibility, And Article Migration

Status: completed on feature branch; not deployed
Depends on: `wiki-from-topic-maker/.ops/plans/credibility-v2-and-article-contracts.md`
Checkpoint: `origin/checkpoint/pre-wf26-playlist-credibility-20260716`

## Goal

Reconcile every entry in the official WF26 playlist, make every currently
available recording pass through the unified maker update as primary event
evidence, keep unavailable items honest, then restructure affected articles
through reusable category contracts and private claim-scoped evidence policy.

Official playlist:
`https://www.youtube.com/playlist?list=PLDyBmFH9HlVc`

## Admission Contract

- Playlist owner must be the configured official AI Engineer channel.
- Membership in the named official WF26 playlist establishes event-media
  association, even when an item is unlisted or does not title-match a session.
- Official schedule remains canonical for talk identity, title, date, time,
  room, track, speakers, and affiliations. Missing schedule matches remain
  empty; YouTube metadata never fills those fields.
- Playable recordings are first-class video/transcript/slide evidence.
- Upcoming premieres are admitted association records and revisited after
  release; they are not content evidence yet.
- Private/unavailable items are retained as playlist placeholders with no title,
  transcript, slide, topic, or claim inference.
- Existing official event livestreams and independently admitted event cuts
  remain in the union manifest even when absent from the playlist.

## Frozen Inventory

Observed and reconciled through 2026-07-17: 29 playlist entries. The final
union contains 34 items: 26 recordings, 3 scheduled premieres, 3 event
livestreams, and 2 unavailable items. The playlist itself contains 24 playable
recordings, 3 scheduled premieres, and 2 unavailable placeholders.

New playable or reclassified IDs:

`iCj_ATyThvc`, `uU5Gv2h8-9g`, `c35YoMdnI78`, `1P1hJ36rxM0`,
`Cz4v1WHVyZc`, `ZyIoTOAbRfs`, `xUnRQ9vLXxo`, `Z2Erdirpudo`,
`eBUyTS7SzV4`.

Pending premiere IDs:

`uIiA6DquRiE`, `RGSFUqzqErE`, `VrpEyglYgeU`.

Unavailable/private IDs:

`Z3fP-eMEx-8`, `PXXNCtfKZs0`.

Availability can change between inventory and execution. The importer must
re-read current metadata and record the observed state rather than forcing the
frozen classification.

## One-Shot Run

1. [x] Disable the user timer for the bounded manual run and record its prior state.
2. [x] Run playlist-only dry-run reconciliation with zero writes.
3. [x] Run focused monitor, article-contract, credibility, and public-policy tests.
4. [x] Run playlist-only acquisition without auto-push.
5. [x] Acquire captions/transcripts and slide/OCR layers for every currently
   playable admitted item; record typed pending/unavailable outcomes otherwise.
6. [x] Invoke one unified maker media update over the changed source set.
7. [x] Apply private claim-scoped writing decisions inside the candidate only.
8. [x] Normalize through category/subtype schemas, export static and agent products,
   and validate public-policy boundaries.
9. [x] Promote the validated candidate atomically.
10. [x] Repeat the same playlist and maker update and require a no-op.
11. [ ] After review and merge, return to a clean `main` and restore the timer.

The timer intentionally remains disabled and inactive while this feature branch
is under review. The installed auto-push service requires a clean `main`
checkout, so restoring it on the feature branch would create an unsafe
operating state.

## Required Validation

- All 29 playlist IDs exist in the reconciled state, with no deletion of prior
  independent event-media admissions.
- Every currently playable item has an explicit acquisition outcome.
- Upcoming/private entries produce no content-derived claims.
- `xUnRQ9vLXxo` is primary official event evidence, not supporting context.
- Exactly one unified maker invocation follows changed acquisition.
- Transcript, video, slide/OCR, schedule, supporting, and synthesis layers remain
  labeled and independently traceable.
- No public artifact contains credibility scores, ranking logic, weights,
  thresholds, calibration, review priority, or private canary data.
- Article order passes the category schema check and remains byte-identical on
  a second normalizer pass.
- The second end-to-end update reports no content changes.
- No deploy occurs without separate approval.

## Final Result

- Run `update-20260717T051453Z-43aefe0a3d` completed all 16 stages and promoted
  target snapshot
  `snapshot:b00976ab3a3272e1f2532a9db296cb97c522bed892725c8b4258b63c54be5711`.
- All 24 playable playlist recordings have cached primary-event transcripts.
  Playlist slide outcomes are 23 cached, 1 `no_slides`, 3 pending, and 2
  unavailable.
- The transcript registry contains 123 pages: 28 primary-event and 95
  comparison/supporting-context transcripts.
- Category normalization reports zero changes and zero issues on its second
  pass. All 2,438 wiki Markdown pages are byte-identical to `dist/md`.
- The relationship exporter and direct structured rebuild are exactly equal:
  1,280 nodes and 1,598 relationships, comprising 813 Person-Concept, 308
  Vendor-Concept, and 477 Concept-Concept records.
- The agent product contains 2,438 pages, 1,540 entities, 3,658 evidence
  records, 1,585 deduplicated relationships, and 418 resources.
- The identical maker request returned `status: no_op` without execution,
  validation, promotion, or a new receipt. No automatic push or deployment
  occurred during the run.
- The final 18-adapter profile run,
  `update-20260717T132348Z-4d6cb4d754`, promoted target snapshot
  `snapshot:81f654182c28bd0eec179d4cf0c5a303c55b825b1366cdca8cf0292d78e7ce35`.
  Its agent product contains 2,438 pages, 1,540 entities, 3,634 evidence
  records, 1,585 relationships, 418 resources, 10 patterns, and 3 claims.
- An earlier profile candidate failed at static export because it redundantly
  invoked agent-product construction through a candidate symlink. It did not
  promote. The build contract now performs static validation once and delegates
  the separately validated agent product to the maker runtime; a repeat of the
  corrected update returned a planning no-op.
- A live recurring monitor dry-run owner-validated all 29 playlist members and
  found no new playlist IDs. The 34-record union has 29 playable, 3 scheduled,
  and 2 unavailable items. Transcript coverage is 25/29 playable items and
  slide outcomes are complete for 29/29; four transcript gaps remain explicit.

## Media-Ingest Hardening Closure

- Completion status is derived from typed transcript, slide, availability, and
  enrichment outcomes; no branch hard-codes a successful completion state.
- Slide OCR and classifier caches bind the exact image, model, prompt,
  configuration, input, and output. Publication is atomic, and stale or partial
  results cannot satisfy later cache checks.
- Codex processing of untrusted web/media content defaults to read-only mode
  without local tools.
- Official-channel discovery enforces configured channel identity, event year,
  and date boundaries. Owner-validated official playlist membership remains the
  canonical event-association exception, while the schedule stays canonical for
  session facts.
- The monitor journals both pre-publish mutations and post-push local sync. It
  restores local state on failed publication but never rolls back content after
  the corresponding remote commit has been verified.
- Historical repair restored 599 exact OCR backups, confirmed 2 already-correct
  records, quarantined 200 stale audits, withheld 108 unsupported sections, and
  removed 1,498 stale generated HTML assets.

## Auditable Credibility Closure

- The private scoring policy now emits exact signed line-item receipts for one
  claim, subject, domain, use, time, jurisdiction, and assessment snapshot.
  Rulesets, source versions, observations, evidence manifests, receipts, and
  line items are content-addressed and append-only.
- Receipt replay is mandatory before finalization. The operator audit reports
  arithmetic replay, append-only store provenance, and live-source rehashing as
  separate facts so a local verification cannot overclaim source authenticity.
- Correction and remediation entries reverse a finalized prior line exactly,
  without factors or caps. A prior line can be reversed only once globally.
- Evidence kinds have fixed stance, source-role, procedural-status, polarity,
  recency, independent-origin, and dimension contracts. Production values and
  ranking internals remain ignored private state and never enter public output.
- Initial run `update-20260717T090944Z-918c7703dc` failed before promotion
  because rediscovery time was incorrectly compared with the authoritative
  append-only observation time. The adapter now reuses the first stored
  observation for a stable observation ID, and a regression test covers it.
- Run `update-20260717T091359Z-64299f4e6a` then completed the migration. After
  the final adversarial reversal and public-leak audit fixes, definitive run
  `update-20260717T093151Z-67650b7fd3` completed all 14 selected stages.
- A final fail-closed audit found one held non-HTTPS company candidate with no
  explicit writing decision. The adapter now emits an auditable `omit` decision
  with no public source projection for that path, and the third-party audit
  treats any future held candidate without `omit` as a high-severity finding.
  Run `update-20260717T094843Z-76cef8004f` completed all 14 stages with this
  closure. Public validation passed and promotion was a no-op because canonical
  wiki and site digests were unchanged.
- Repeating the definitive request returned `status: no_op` with no execution,
  validation, promotion, or receipt. No external deployment occurred.
- Final validation: 750 maker tests, 302 WF26 tests, Ruff, compile, and diff
  checks pass; 7,384 publishable files plus 1,998 raw source files contain zero
  private-ranking boundary findings. A
  real WF26 receipt replays successfully and has valid append-only provenance;
  its source bytes were intentionally not re-fetched by the local audit.
- All 300 held company-profile candidates have explicit `omit` decisions and
  all 300 are verified absent from public artifacts.
- Every canonical entity/article page is assessed without using the result as
  an exclusion gate for official primary evidence. Public records carry only
  categorical evidence coverage; exact numerical construction remains in
  ignored, replayable operator receipts.
