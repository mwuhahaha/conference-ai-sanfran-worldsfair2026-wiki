# WF26 Playlist, Credibility, And Article Migration

Status: completed locally; not pushed or deployed
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
11. [ ] Restore the timer only after the worktree and branch are operationally safe.

The timer intentionally remains disabled and inactive while this feature branch
is dirty. The installed auto-push service requires a clean `main` checkout, so
restoring it before review/commit would create an unsafe operating state.

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
  validation, promotion, or a new receipt. No push or deployment occurred.
