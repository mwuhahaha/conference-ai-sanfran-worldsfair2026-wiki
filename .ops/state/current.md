---
type: orchestration-current
scope: project-local
status: active
updated: 2026-08-03T16:02:05Z
---

# AI Engineer World's Fair 2026 Project State

The completed AIE-specific conversion plan remains closed. Follow-up public navigation work now lives in `.ops/plans/worldsfair-static-navigation-followup.md`.

## 2026-07-30 Lower-Model Official-Video Evidence Import Handoff

### Status

- Active chapter: official WF26 media refresh.
- Completed story: lower-model evidence acquisition/import for newly found
  official AI Engineer channel WF26 videos.
- Attempted story: the higher-model project-authoritative media update was run
  exactly once as `update-20260730T140125Z-f9ef425b3a`. It failed at required
  stage `talk_synthesis`; no validation, agent-product build, local promotion,
  external deployment, commit, push, or cache cleanup occurred.
- Completed story: the nested Codex runtime failure was traced to command
  routing drift. The plain executable loaded a different editable maker
  checkout on sandbox contract v1 instead of the clean project pin at
  `c5bc782956d85fdf5d3347858eb2ce49b6054f6a`. Manual authoritative update
  instructions now use `scripts/run_pinned_wiki_maker.py`, which validates and
  loads that immutable v2 runtime.
- Attempted story: pinned run `update-20260730T143918Z-7b6cd997b3` completed
  every media adapter, static export, and agent-product build, then failed
  closed at `public_validation`. No local promotion occurred.
- Completed story: the three rollback directories were preserved intact under
  ignored recovery state, removed from Git-visible publishable inventory, and
  the retained candidate passed the exact targeted public-boundary and agent
  snapshot checks.
- Attempted story: exact resume of
  `update-20260730T143918Z-7b6cd997b3` failed closed before execution with
  `resume target does not exist`. The run row and candidate exist, but exact
  resume rejects the repaired source root's new ChangeSet/snapshot identity.
  No validation, promotion, or canonical mutation occurred.
- Completed story: repaired-inventory run
  `update-20260730T162008Z-e60b50a78d` completed all 20 stages, passed maker
  validation, and locally promoted the synthesized wiki, static export, agent
  product, and private credibility output as
  `promotion:eb25ce31d2aab680c4581954856fb3bdfcbcc90757b3d6a985bcc74a150bebad`.
- Completed story: a read-only higher-model editorial and source-boundary
  review verified the 15 newly synthesized matched talks and found one primary
  unmatched-resource classification defect plus ten secondary claim/excerpt
  alignment issues. No generated content was edited.
- Completed story: the unmatched-resource classification generator now derives
  a distinct description-backed/unmatched role from the manifest and has
  focused regression coverage. No canonical or static output was regenerated.
- Completed story: one pinned read-only maker plan established a ChangeSet
  containing only the `classify_media` implementation change and left maker
  state byte-identical. The authoritative execution scope is still the full
  18-adapter media DAG.
- Completed story: locked authoritative run
  `update-20260730T201356Z-7c35a974d1` completed and locally promoted the
  corrected canonical/static unmatched-resource boundary.
- Completed story: a read-only cache-lineage diagnosis proved that cross-talk
  map batch 1 invalidated its own otherwise valid completed partition on
  reload. The resulting reducer miss and 86-file synthesis delta are
  nondeterministic drift, not new evidence.
- Completed story: the topic-map cache loader now admits a source-bound
  completed partition up to the candidate count while retaining the raw-model
  60-cluster ceiling, with focused round-trip and invalid-cache regressions.
- Completed story: a read-only recovery preflight revalidated the exact
  preserved 15-cluster lineage and one pinned maker plan bounded the code
  correction to `talk_synthesis` and `synthesis_layers` implementation changes.
- Completed story: a reversible seeded-plan derivation produced the exact
  post-seed recovery lock, restored the current cache files byte-for-byte, and
  left maker state unchanged.
- Completed story: one locked pinned authoritative recovery update reseeded the
  exact preserved map/reducer artifacts, completed all 20 pipeline stages,
  passed validation, and locally promoted the restored synthesis, static site,
  agent product, and private credibility output as
  `promotion:ef295ef8ddd9adff9f8fef0111fa8979f246b9142dbf2ba4ed4bc26091c5d647`.
- Completed story: a read-only reconciliation of the separately discovered
  2026-08-03 official-media delta produced a bounded, evidence-preserving
  acquisition proposal. No video, caption, slide, manifest, maker, or static
  artifact was changed.
- Completed story: lower-model acquisition/import processed all 31 approved
  playable recordings (28 schedule-matched, 3 resource-only) with captions,
  transcripts, scene-aware slides, OCR, resource pages, and approved talk links.
- Attempted story: pinned higher-model media update
  `update-20260803T105122Z-f1a9863813` ran exactly once and failed closed at
  `talk_media_map`; all 31 new playlist records then lacked required
  `playlistIndex` values. No canonical promotion occurred and no retry ran.
- Completed story: the 31 missing positions were restored exactly from the
  retained 93-item official-playlist snapshot. Contract validation exposed 46
  older rows whose pre-insertion indices are now stale; 29 collide with the
  restored values, so `talk_media_map --check` still fails closed.
- Completed story: the 46 stale existing indices were reconciled against the
  same retained snapshot. All 77 playlist-annotated manifest rows now match
  their captured positions with no duplicates, and read-only talk-media-map
  validation passes its input contract.
- Next single story: after a new explicit operator decision, run exactly one
  pinned authoritative maker media update, then validate canonical transcript
  pages, synthesis, source boundaries, static/agent output, and promotion.

### Current-State Proof

- Disk preflight before import showed `/garage` had 55G available on a 422G
  ext4 filesystem, with inode headroom. After import, `/garage` still has 55G
  available and remains 87% used.
- `raw/video-cache` is 7.9G after import; `raw/slide-frames-tmp` is 611M;
  `.ops/state/cache` is 63G.
- `raw/sources/official-wf26-video-manifest.json` now contains 83 records:
  76 `talk_recording`, 3 `event_livestream`, 1 `scheduled_premiere`, and
  3 `unavailable_playlist_item`.
- Manifest artifact statuses after the manual import: 76 cached transcripts,
  75 cached slide sets, 1 evidence-backed `no_slides`, 3 unavailable playlist
  items, and 1 pending scheduled premiere. The 3 event livestream rows do not
  carry the same transcript/slide status fields.
- Local artifact counts: 280 YouTube resource pages, 474 YouTube slide pages,
  and 170 cached raw YouTube transcript text files.

### Completed Evidence Import

Fifteen exact schedule-title recordings were imported with official-channel
metadata, captions, transcript text, slide extraction, slide OCR, resource
pages, slide pages, and talk-page media links:

- `z0sh8HyTrDo` — Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI.
- `o6U_2vd967Y` — Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft.
- `Tt2kX2sgQio` — How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh.
- `Owb8g3yDyzo` — Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit.
- `wpOA-UXynoM` — How Forward Deployed Engineering is done at Factory — Eno Reyes.
- `l0FLhNqBOic` — AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents.
- `RVxym6mmIns` — How Forward Deployed Engineering is done at Cognition — Jia Wu.
- `ITMXwI6QL6A` — How Forward Deployed Engineering is done at Ramp — Leo Mehr.
- `Byv311hdoHE` — The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra.
- `7wu2hsRfvV0` — How Forward Deployed Engineering is done at Decagon — Sunny Rekhi.
- `1OMHGsUZiqA` — How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh.
- `KwhgfwOSToQ` — Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE.
- `lyL5QhgIOxc` — Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub — Arek Borucki, Hugging Face.
- `xIt_mTQp6mY` — Loop Engineering from First Principles — Kyle Mistele, HumanLayer.
- `b_PmGocP4rc` — Evaling Video Slop — Maor Bril, Character.ai.

One additional generic-title recording was imported as unmatched official WF26
media:

- `2xJoimgoqBg` — Security Track Intro — Randall Degges, Snyk.
  The official AI Engineer YouTube metadata explicitly says Randall Degges is
  opening the World's Fair's first Security Track. The local official schedule
  has `Security Track intro` attributed to Manoj Nair, so this resource is not
  assigned to a schedule page. It uses
  `associationEvidence: official_channel_explicit_wf26_description` and
  `matchedTalks: []`.

Receipts:

- `.ops/state/runs/manual-exact-video-import-2026-07-30-lower-model.json`
  records the first 16-candidate run. Its `processed` array contains 15 items
  with `status: processed` and one item, `2xJoimgoqBg`, with
  `status: skipped_match_safety`.
- `.ops/state/runs/manual-security-track-intro-import-2026-07-30-lower-model.json`
  records the separate Security Track import decision and validated artifacts.

### Validation Evidence

- Direct artifact validation confirmed all 16 imported videos have:
  manifest row, resource page, slide page, raw transcript text, and slide OCR
  directory.
- `2xJoimgoqBg` validation confirmed:
  13 slide references, 13 OCR text files, and 672 transcript words.
- The first 15 exact-match imports produced 244 total extracted slide image
  references across their slide pages.
- `git status --short` shows expected modified/generated source and wiki
  artifacts only. It also shows three small rollback backup directories created
  by the writer:
  `.wiki.rollback-97c3250986734954a94f43b08459ed08/`,
  `raw/sources/.attendance-calibration.rollback-1ba57319d3574051a978e9ac9e669ee2/`,
  and
  `raw/sources/.attendance-calibration.rollback-b2aa9f9d979148d8b430f96b9eaa5e3c/`.
  They were left in place for recoverability.

### Hard Boundaries For Next Story

- Use the new transcript/resource/slide evidence as input; do not treat official
  schedule metadata and video-derived claims as the same evidence layer.
- Do not attach `2xJoimgoqBg` to the Manoj Nair schedule page unless a stronger
  official schedule correction or manual operator decision resolves the speaker
  mismatch.
- Do not rerun video discovery, caption import, or slide extraction unless a
  concrete validation failure identifies a missing or corrupt artifact.
- Do not delete `raw/video-cache` or `raw/slide-frames-tmp` until after
  higher-model synthesis and review. They are rebuildable media/frame caches,
  but keeping them avoids repeated downloads if an extraction issue is found.
- Do not run external deployment or publish from this state without explicit
  approval.

### Successor-Run Proof And Release Risk

- The higher-model successor invocation ran exactly once:

  ```bash
  wiki-from-topic-maker update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --json
  ```

- Run `update-20260730T140125Z-f9ef425b3a` failed at required stage
  `talk_synthesis`. Its nested Codex invocations for all 15 new schedule-matched
  recordings returned `failed to initialize in-process app-server client:
  Read-only file system (os error 30)`.
- Seven prerequisite stages succeeded in the private candidate:
  `classify_media`, `credibility_provider_checks`, `transcript_pages`,
  `credibility_policy`, `talk_media_map`, `company_profiles`, and
  `slide_ai_admission_check`.
- The candidate contains 176 transcript Markdown pages, including transcript
  evidence for all 16 imported recordings. Those pages were not promoted:
  canonical `wiki/transcripts/` remains at 160 Markdown pages and contains none
  of the 16 new video IDs. Each directory also contains one `registry.json`,
  making the corresponding all-file counts 177 and 161.
- Every stage after `talk_synthesis` was blocked, including source enrichment,
  synthesis layers, normalization, static export, agent product, public
  validation, and promotion. The run receipt has `promotion: null`,
  `validation: null`, and `agent_product: null`.
- The resumable candidate and valid completed digests were retained at
  `.ops/state/cache/wiki-maker/candidates/update-20260730T140125Z-f9ef425b3a/`.
  The authoritative receipt is
  `.ops/state/runs/wiki-maker-update-20260730T140125Z-f9ef425b3a-attempt-001.json`.
- Canonical source-boundary proof remains safe: manifest record `2xJoimgoqBg`
  still has `matchedTalks: []` and
  `associationEvidence: official_channel_explicit_wf26_description`; its
  resource page still says no exact schedule-page match is assigned.
- The protected caches remain in place: `raw/video-cache` is 7.9G and
  `raw/slide-frames-tmp` is 611M. `/garage` has 51G available after the failed
  candidate run.
- Root cause proof: `/home/dylan/.local/bin/wiki-from-topic-maker` is an
  editable install sourced from `/garage/obsidian/wiki-from-topic-maker`, whose
  active checkout exposed `bubblewrap-read-only-authority-v1`. The project pin
  under `.ops/runtime/wiki-from-topic-maker-c5bc782956d8/` is clean at the
  documented commit and exposes `bubblewrap-read-only-authority-v2`, including
  an ephemeral writable `CODEX_HOME` with read-only `auth.json`.
- Repair proof:
  - the pinned runtime test
    `test_nested_codex_runtime_is_ephemeral_and_auth_is_read_only` passed;
  - the project monitor tests proving pinned-runner preference and fail-closed
    override behavior passed;
  - a bounded sandbox-equivalent synthesis for Arek Borucki recording
    `lyL5QhgIOxc` passed under Codex 0.146.0 and returned the complete structured
    result shape with six claims;
  - the proof used temporary Bubblewrap state only and did not mutate or
    promote canonical wiki/static outputs.
- `AGENTS.md` and `README.md` now define the authoritative manual command as:

  ```bash
  python3 scripts/run_pinned_wiki_maker.py update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --json
  ```

- Pinned successor run `update-20260730T143918Z-7b6cd997b3`:
  - succeeded through all 18 profile adapters, including `talk_synthesis`,
    source enrichment, synthesis layers, normalization, page assessments, and
    validated static export;
  - built candidate agent snapshot
    `snapshot:6b13f01f80822ff9b3ab309cffd30cbb8f24ec994cda0acb3680948f410bc1d9`
    with 2,769 pages, 3,940 evidence records, 468 resources, 1,576 entities,
    1,652 relationships, 72 claims, and 12 patterns;
  - produced 176 candidate transcript Markdown pages, including exactly one for
    each of the 16 new recordings;
  - added synthesis evidence to each of the 15 schedule-matched talk pages;
  - kept `2xJoimgoqBg` out of every talk page and retained its explicit
    no-exact-schedule-match resource boundary;
  - aligned the workspace agent index, static agent index, and agent manifest
    to the same candidate snapshot;
  - failed only at `public_validation`, with three `invalid_json` findings from
    zero-byte JSON files under the previously preserved attendance rollback
    directories.
- The first reported validation path was
  `raw/sources/.attendance-calibration.rollback-1ba57319d3574051a978e9ac9e669ee2/video-attendance-evidence.json`.
  The other zero-byte JSON files are
  `raw/sources/.attendance-calibration.rollback-b2aa9f9d979148d8b430f96b9eaa5e3c/room-calibration-evidence.json`
  and
  `raw/sources/.attendance-calibration.rollback-b2aa9f9d979148d8b430f96b9eaa5e3c/video-attendance-evidence.json`.
  At the time of the failed run, Git confirmed both attendance rollback directories and
  `.wiki.rollback-97c3250986734954a94f43b08459ed08/` are untracked and
  nonignored, so publishable-inventory validation sees them. Ignored
  `.ops/state/cache/` is the appropriate recovery-state boundary. The later
  preservation story moved them there intact as documented below.
- The authoritative receipt is
  `.ops/state/runs/wiki-maker-update-20260730T143918Z-7b6cd997b3-attempt-001.json`;
  it records `public_validation: failed`, `promotion: null`, and
  `external_deployment: false`. Canonical `wiki/transcripts/` remains at 160
  Markdown pages and contains none of the 16 new transcript pages. Canonical
  static and agent artifacts remain unchanged.
- The successful unpromoted candidate is retained at
  `.ops/state/cache/wiki-maker/candidates/update-20260730T143918Z-7b6cd997b3/`.
  `/garage` has 47G available; `raw/video-cache` remains 7.9G and
  `raw/slide-frames-tmp` remains 611M.
- Recurrence proof for the six-hour monitor was not refreshed in this manual
  story. The sandbox defect and synthesis path are proven, but the imported
  recordings are still not present in canonical transcript, static, or agent
  products because public validation blocked promotion.

### Rollback Preservation And Targeted Validation Proof

- The three rollback directories were moved intact into ignored recovery root
  `.ops/state/cache/recovery/wf26-public-boundary-rollbacks-20260730/`.
  Nothing was deleted or rewritten.
- `.wiki.rollback-97c3250986734954a94f43b08459ed08/` retained 35 files,
  271,388 bytes, and tree digest
  `sha256:a8fae261e23f14907cf66da743eb2a01599216b42ebb55308ec2fd0a50e73183`.
- Attendance rollback `1ba57319d3574051a978e9ac9e669ee2` retained 24 files,
  1,064,209 bytes, and tree digest
  `sha256:49722dbd7bc1cb567d6c52373baceff7154aaf78a0a7864ecd564b9c9964fa4a`.
- Attendance rollback `b2aa9f9d979148d8b430f96b9eaa5e3c` retained 6 files,
  8,211 bytes, and tree digest
  `sha256:f7da61f20681e6cb9bc760233454c6d3d4fe5fb744b27d56e81e1bd6794b8f18`.
- Source and destination counts, byte counts, and content-relative tree digests
  matched before and after. All three original paths are absent, and Git
  confirms the recovery root is ignored by `.gitignore`.
- The targeted check used the pinned maker implementation at
  `c5bc782956d85fdf5d3347858eb2ce49b6054f6a` and the exact roots used by
  `public_validation`: the retained candidate wiki, retained candidate site,
  and canonical `raw/sources`.
- It checked 10,452 publishable Markdown, JSON, JSONL, and HTML files with zero
  issues. It also loaded agent snapshot
  `snapshot:6b13f01f80822ff9b3ab309cffd30cbb8f24ec994cda0acb3680948f410bc1d9`
  successfully.
- The first read-only harness invocation stopped before scanning because it
  imported `load_snapshot` from the wrong module. The corrected invocation used
  the exact pinned maker import and passed. Neither invocation resumed or
  reran the maker pipeline.
- Durable receipt:
  `.ops/state/runs/wf26-rollback-preservation-public-boundary-20260730T154838Z.json`.
- No full maker rerun, local promotion, external deployment, commit, push,
  cache deletion, or schedule-speaker correction occurred.

### Exact Resume Failure And Replanned Identity

- The documented exact resume command was issued once. It exited 1 immediately
  with `resume target does not exist`; no second resume was attempted.
- SQLite proves run `update-20260730T143918Z-7b6cd997b3` still exists with
  status `failed`. It is bound to ChangeSet
  `changeset:eb1233b7726473ca4d3014a0c918eabfb02d7d50eeb83fa90ba555c185fd7a66`
  and target snapshot
  `snapshot:faefe82255b310d8c7702354e098ee5fb5449a21d4334c24f6e0178a3b9545fd`.
- The maker's resume guard recomputes the deterministic plan before reopening a
  failed run. Removing the invalid rollback directories from admitted
  `raw/sources` correctly changed the source-root digest, so the repaired state
  now plans ChangeSet
  `changeset:3566f6688d6e0931bd66d12ae1799f2d9c2b7a73d250ea4593cee071ae2c2d21`
  and target snapshot
  `snapshot:eb25ce31d2aab680c4581954856fb3bdfcbcc90757b3d6a985bcc74a150bebad`.
  The generic error refers to this ChangeSet/snapshot mismatch, not a missing
  candidate directory.
- A pinned read-only `--plan --json` confirmed the new identity and left
  `.ops/state/cache/wiki-maker/state.sqlite3` byte-for-byte unchanged at
  `sha256:80fbc617409730f361286a818927ebb084b9b6173816744a3a7d410d2a906740`.
- The original maker still has only attempt-001 and remains unpromoted.
  Candidate transcript count remains 176 Markdown pages, canonical remains
  160, and `2xJoimgoqBg` remains in zero candidate and canonical talk pages.
- Durable operator receipt:
  `.ops/state/runs/wf26-retained-run-resume-attempt-20260730T161126Z.json`.
- No new full update, local promotion, external deployment, commit, push,
  cache deletion, schedule correction, or recurrence test occurred.

### Successful Repaired-Inventory Promotion

- Exactly one locked repaired-inventory update ran:

  ```bash
  python3 scripts/run_pinned_wiki_maker.py update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --change-set changeset:3566f6688d6e0931bd66d12ae1799f2d9c2b7a73d250ea4593cee071ae2c2d21 \
    --json
  ```

- Run `update-20260730T162008Z-e60b50a78d` completed all 20 stages. Every
  execution record is `succeeded`, including transcript pages, talk media map,
  `talk_synthesis`, source enrichment, synthesis layers, page assessments,
  static export, agent product, and `public_validation`.
- Maker validation passed `agent.snapshot`, `public.boundary`, and
  `wiki.shape`. Candidate wiki digest is
  `sha256:55bb567b2f704a9011c3929ff3fc0fa0ce379ca080f77be5d95260b4147551f8`;
  candidate static digest is
  `sha256:ed317b026187233af8420d8ddc6163e70cc93f5b04e1233616dabb380759c73e`.
- Local promotion
  `promotion:eb25ce31d2aab680c4581954856fb3bdfcbcc90757b3d6a985bcc74a150bebad`
  is committed in its promotion journal and `promoted` in SQLite. It changed
  the wiki, site, and private credibility root. External deployment is false.
- Canonical `wiki/transcripts/` now contains 176 Markdown pages, exactly 16
  more than the pre-promotion baseline. Each imported video ID has exactly one
  transcript Markdown page, and all 16 corresponding static transcript routes
  exist.
- Each of the 15 schedule-matched video IDs appears on exactly one canonical
  talk page. Every such page has a `Synthesis` section with a
  `Transcript-Backed Summary` and `Claims From The Talk`, plus exactly one
  structured digest under `wiki/resources/talk-digests/`.
- `2xJoimgoqBg` appears on zero canonical talk pages. Its manifest record still
  has `associationEvidence: official_channel_explicit_wf26_description` and
  `matchedTalks: []`; its canonical resource still says no exact schedule-page
  match is assigned and links its transcript Markdown.
- Agent snapshot
  `snapshot:ab676ddd2ccc3fa63b4f8f98bc650dd76ea7a1b85102e9d7ac9f4cb6a80abe77`
  contains 2,771 pages, 3,940 evidence records, 468 resources, 1,578 entities,
  1,771 relationships, 72 claims, and 12 patterns. Root and static
  `agent-index.json` files are byte-identical and point to that same manifest
  snapshot.
- Authoritative maker receipt:
  `.ops/state/runs/wiki-maker-update-20260730T162008Z-e60b50a78d-attempt-001.json`.
  Promotion journal:
  `.ops/state/cache/wiki-maker/promotion-journals/promotion:eb25ce31d2aab680c4581954856fb3bdfcbcc90757b3d6a985bcc74a150bebad.json`.
- A subsequent pinned read-only plan is a no-op because inputs, profile, and
  promoted output digests are unchanged. It left the state database unchanged
  at
  `sha256:e8724ece55691059ff376beb39c88b15acef90a48fc7b4b152e956efe2f6c8ed`.
- `/garage` has 45G available. Protected caches remain in place:
  `raw/video-cache` is 7.9G and `raw/slide-frames-tmp` is 611M.
- No discovery, caption import, slide extraction, external deployment, commit,
  push, cache deletion, schedule-speaker correction, or monitor recurrence run
  occurred in this story.

### Higher-Model Editorial And Source-Boundary Review

- All 15 schedule-matched manifest rows have one exact `matchedTalks` value and
  `associationEvidence: official_channel_plus_schedule_text`. Each digest's
  `videoId` and `talkId` agree with the manifest mapping and the canonical talk
  title.
- All 15 structured digests have the correct raw transcript SHA-256. A
  deterministic reconstruction of their bounded transcript segments verified
  all 408 selected segment IDs and copied evidence excerpts byte for byte.
- The 15 summaries are distinct and substantive: their lengths range from 620
  to 988 characters, and the highest pairwise summary token Jaccard score is
  0.162. Manual review found speaker-attributed, talk-specific summaries rather
  than duplicated or shallow synthesis. No schedule-to-recording identity error
  was found.
- Primary actionable source-boundary defect: canonical resource
  `wiki/resources/youtube-2xJoimgoqBg.md` lines 12 and 16 say the recording was
  verified against a scheduled session and against schedule title/speaker
  evidence. That contradicts line 20, the manifest's
  `associationEvidence: official_channel_explicit_wf26_description`, and
  `matchedTalks: []`. The same unsafe classification is rendered in
  `dist/resources/youtube-2xJoimgoqBg/index.html`.
- The unmatched recording otherwise remains safely isolated: `2xJoimgoqBg`
  occurs in no talk page, talk-video transcript map, structured talk digest,
  generated claim, or generated highlight. Its transcript identifies the
  speaker as Randall, describes the World's Fair security track, and does not
  identify Manoj Nair.
- Secondary editorial findings: ten generated claims are supported by the
  corresponding transcript overall, but their single selected evidence segment
  supports only part of the claim while an adjacent segment supplies the
  omitted support:
  - `Owb8g3yDyzo` line 32: customer/vendor concentration is in S0022; the
    selected S0023 supports the price recommendation.
  - `Tt2kX2sgQio` line 40: differing ratio definitions are in S0086-S0087; the
    selected S0088 supports the verification chain.
  - `Byv311hdoHE` line 32: data integration and broader ontology-modeling
    context are in S0041-S0046; selected S0045 only partially supports the
    combined claim. The related takeaway and ontology-method item have the same
    narrow-segment issue.
  - `7wu2hsRfvV0` line 32: S0049 explicitly names restraint as the scarce
    skill; selected S0048 only establishes the temptation.
  - `KwhgfwOSToQ` line 40: S0076 supports easier customization; selected S0075
    establishes that platforms are becoming agentic.
  - `lyL5QhgIOxc` line 40: S0037 supplies the regex scaling/latency reason;
    selected S0038 supports the switch to Atlas.
  - `lyL5QhgIOxc` line 56: S0071 states the HPA-to-KEDA migration plan;
    selected S0072 only compares their metrics.
  - `xIt_mTQp6mY` line 48: S0103-S0106 support the one-open-PR guard; selected
    S0102 only discusses labels and junk cleanup.
  - `b_PmGocP4rc` line 24: S0025-S0027 support the generic-LLM-judge
    limitation; selected S0014 supports frame metrics.
  - `b_PmGocP4rc` line 48: S0050 states the smaller-model choice and latency
    tradeoff; selected S0049 only says the larger model was better but slower.
- These ten findings are evidence-selection precision issues, not unsupported
  talk identities or fabricated transcript claims. A later remediation should
  retarget a sufficient adjacent segment where possible or narrow/split a claim
  whose full meaning spans multiple segments.
- This story was read-only except for this handoff update. It did not edit
  generated wiki/static content, rerun discovery, captions, slide extraction,
  maker synthesis, or promotion, attach `2xJoimgoqBg` to a schedule page,
  deploy, commit, push, clean caches, or exercise monitor recurrence.

### Unmatched Description-Backed Resource Generator Correction

- `scripts/classify_video_resource_sources.py` now selects
  `primary event description-backed recording` only for playable
  `talk_recording` manifest rows with
  `associationEvidence: official_channel_explicit_wf26_description` and exactly
  `matchedTalks: []`.
- The role remains playable primary event media for recording, transcript, and
  slide evidence, but its `What It Is` and source-classification text say event
  association comes from explicit official-channel description metadata, that
  no exact schedule-page match is assigned, and that schedule fields must not
  be inferred.
- Matched cut-video, playlist, livestream, premiere, unavailable, and
  supporting roles retain their existing classification paths. The new role is
  also included in playable-primary source-layer reconciliation.
- Focused regression
  `test_event_resource_classifier_preserves_description_backed_unmatched_boundary`
  constructs the exact manifest contract and proves the generated page contains
  the description boundary without either schedule-verification phrase.
- Validation passed:
  - all 37 tests in `tests/test_generator_argument_safety.py`;
  - the five focused event-resource classifier tests;
  - Python compilation for the changed generator and test;
  - Ruff for the changed generator and test;
  - `git diff --check` for the two implementation files.
- A read-only projection against canonical `youtube-2xJoimgoqBg.md` selected
  the new role, removed both unsafe schedule-verification phrases, retained the
  explicit no-exact-match relationship section, and produced only the expected
  `What It Is` plus three-line source-classification diff.
- The implementation diff is confined to
  `scripts/classify_video_resource_sources.py` and
  `tests/test_generator_argument_safety.py`: 127 inserted lines with no
  deletion. Canonical wiki/static resources were not written.
- This story did not run a maker plan or update, regenerate or promote
  canonical/static output, address the ten secondary digest findings, attach
  `2xJoimgoqBg` to Manoj Nair, rerun media acquisition or synthesis, deploy,
  commit, push, delete caches, or exercise monitor recurrence.

### Read-Only Remediation Maker Plan

- Exactly one pinned planning invocation ran:

  ```bash
  python3 scripts/run_pinned_wiki_maker.py update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --plan \
    --json
  ```

- The result was `status: planned`, `ok: true`, with `run_id: null`,
  `execution: null`, `validation: null`, `promotion: null`,
  `receipt_path: null`, and `external_deployment: false`.
- Planned ChangeSet:
  `changeset:dde10a7c01734b720371f6ed9a72139d027a36171a6bc35f24878c74d43ab1fe`.
  Base snapshot:
  `snapshot:eb25ce31d2aab680c4581954856fb3bdfcbcc90757b3d6a985bcc74a150bebad`.
  Target snapshot:
  `snapshot:69b590fa353a5a5aad41a0540541fcee48c3e6b8a6b02191667f3047575e66b1`.
- The ChangeSet has exactly one entry:
  `adapter:3175efd87faa655ed87f9dc96e10430aef6c262027aa139a348ca44239321008`,
  which is `sha256("classify_media")`. Its disposition is
  `stage_version_changed`, from
  `sha256:ca79589afb7fa671b2cac764201b9c07759768901bcea0b9e5baa998359427b0`
  to
  `sha256:83b4db938d4be203fe8cc03f8b498d96c71a040fb78ab556c1136049f512e2b5`.
  No source-root, manifest, profile, private-input, or other adapter change
  appears in the ChangeSet.
- The planned identity is therefore bounded to the intended classifier
  implementation change. Execution is not classifier-only: the `media` trigger
  selects the authoritative 18-adapter DAG, including `talk_synthesis`,
  synthesis layers, assessments, static export, and maker validation/promotion.
- The maker state database was byte-identical before and after planning:
  8,048,640 bytes, modification time
  `2026-07-30 13:02:45.747529244 -0400`, and
  `sha256:e8724ece55691059ff376beb39c88b15acef90a48fc7b4b152e956efe2f6c8ed`.
- The manifest boundary remains
  `mediaType: talk_recording`,
  `associationEvidence: official_channel_explicit_wf26_description`, and
  `matchedTalks: []` for `2xJoimgoqBg`. Canonical resource digest remains
  `sha256:c79c67346a0d3c8203159c90ec979360e1de407c691f77dd98d78e18159ff546`;
  the correction has not yet been generated or promoted.
- No update stages executed, no receipt or candidate was created, and no
  canonical/static, private, manifest, or cache artifact was changed. This
  story did not address the ten secondary digest findings, attach
  `2xJoimgoqBg` to Manoj Nair, acquire media, deploy, commit, push, delete
  caches, or exercise monitor recurrence.

### Locked Boundary-Remediation Update And Unrelated Synthesis Delta

- Exactly one locked authoritative update ran:

  ```bash
  python3 scripts/run_pinned_wiki_maker.py update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --change-set changeset:dde10a7c01734b720371f6ed9a72139d027a36171a6bc35f24878c74d43ab1fe \
    --json
  ```

- Run `update-20260730T201356Z-7c35a974d1` completed from
  `2026-07-30T20:13:56.231Z` through `2026-07-30T20:45:02.123Z`.
  All 20 execution records succeeded, including all 18 adapters,
  `agent_product`, and `public_validation`.
- Maker validation passed `agent.snapshot`, `public.boundary`, and
  `wiki.shape`. Candidate wiki digest is
  `sha256:a685e104376524b4a33bb2b275b7e82b76110b4eda41c2d5a37bc1f039620697`;
  candidate site digest is
  `sha256:8eceeb931adcdd078cd51a8e95e89ab77e8abb9a030f0b36d5796a2f485c5507`.
- Local promotion
  `promotion:69b590fa353a5a5aad41a0540541fcee48c3e6b8a6b02191667f3047575e66b1`
  is `promoted`. Its journal is
  `.ops/state/cache/wiki-maker/promotion-journals/promotion:69b590fa353a5a5aad41a0540541fcee48c3e6b8a6b02191667f3047575e66b1.json`.
  External deployment is false.
- Authoritative receipt:
  `.ops/state/runs/wiki-maker-update-20260730T201356Z-7c35a974d1-attempt-001.json`.
- The intended correction is present in canonical and static output:
  `wiki/resources/youtube-2xJoimgoqBg.md` and
  `dist/resources/youtube-2xJoimgoqBg/index.html` identify the recording as
  official description-backed WF26 media, say no exact schedule-page match is
  assigned, and prohibit inferring schedule fields. Neither contains either
  unsafe schedule-verification phrase.
- The source boundary remains intact: manifest row `2xJoimgoqBg` still has
  `associationEvidence: official_channel_explicit_wf26_description` and
  `matchedTalks: []`. It occurs in zero talk pages, structured talk digests,
  generated claims, generated highlights, or talk-video transcript-map entries.
- Focused classifier regression tests passed after promotion, as did changed-file
  Ruff and `git diff --check`. Root and static `agent-index.json` are
  byte-identical.
- The run also produced an unrelated cross-talk synthesis delta that blocks
  clean acceptance of the promoted result:
  - all 69 structured talk digests were cache hits and zero digests were
    generated; the entire `wiki/resources/talk-digests/` tree is byte-identical
    to the pre-promotion backup;
  - canonical transcripts, generated claims, and generated highlights are also
    byte-identical to the backup;
  - cross-talk map batch 1 was regenerated even though its
    `inputSha256`
    `sha256:cc31e7806f184fd4edeb31f1a399903dda6a85e1eee3fd0c483998f6113df77a`
    and contract SHA-256 are unchanged; five other map batches were cache hits;
  - the reduce stage was a cache miss and changed the rollup from 15 clusters
    to 13;
  - the resulting wiki content delta contains 86 files: 61 talk pages,
    5 resources, 1 tool, 17 changed/added topic files, and 2 deleted topic
    files. Five topic pages were added and two were deleted;
  - talk-page changes are derived topic-link/materialization changes and
    normalization, not structured digest or transcript changes;
  - agent snapshot changed from
    `snapshot:ab676ddd2ccc3fa63b4f8f98bc650dd76ea7a1b85102e9d7ac9f4cb6a80abe77`
    to
    `snapshot:617af825c8f21a6abfff0b42a23b7f9892eaa15de0a05fadfc2201753100db9d`.
    Counts changed from 2,771 to 2,768 pages, 1,578 to 1,575 entities, and
    1,771 to 1,504 relationships; claims remain 72, evidence 3,940, resources
    468, and patterns 12.
- The exact pre-promotion canonical wiki/site remain recoverable under
  `.ops/state/cache/wiki-maker/promotion-backups/8639437800ea61c7/`. Do not
  delete or alter this backup until the synthesis delta is resolved.
- Protected acquisition caches remain intact:
  `raw/video-cache` is 7.9G and `raw/slide-frames-tmp` is 611M. `/garage` has
  43G available.
- No deployment, commit, push, schedule attachment, acquisition rerun, cache
  cleanup, secondary digest remediation, rollback, or manual mixed-state edit
  occurred.

### Cross-Talk Cache-Lineage Diagnosis

- The cache miss is a self-invalidating round-trip defect in
  `scripts/generate_talk_synthesis.py`, not a source, digest, taxonomy, model,
  or contract change.
- `topic_map_schema()` correctly limits raw model output to 60 clusters.
  `validate_topic_map_payload()` then filters and deduplicates those clusters
  and appends a singleton for every uncovered candidate. The post-validation
  completed partition can therefore exceed 60 clusters.
- `run_topic_map_batch()` writes that expanded completed partition to cache,
  while `load_cached_topic_map()` passes the stored expansion back through the
  same raw-output validator. An otherwise valid cache entry is rejected on the
  next identical run solely when singleton completion took it above 60.
- The preserved prior batch 1 at
  `.ops/state/cache/wiki-maker/promotion-backups/8639437800ea61c7/wiki/resources/topic-synthesis-batches/batch-01.json`
  has 66 candidates and 64 stored clusters: 62 singleton and 2 multi-talk
  clusters. Every candidate appears exactly once.
- Its stored and recomputed input SHA-256 are both
  `sha256:cc31e7806f184fd4edeb31f1a399903dda6a85e1eee3fd0c483998f6113df77a`;
  its contract SHA-256 remains
  `sha256:17b8e63c132062ed52e1829b57b7fdf9b1b0932724ce9fb94a913b5864c43339`;
  its payload hash is valid; and its schema, generator, algorithm, model,
  candidate membership, and complete-partition checks all agree.
- The only rejection is
  `ValueError: topic map clusters violate the bounded schema`, caused by
  applying the raw 60-cluster ceiling to the stored 64-cluster completed
  partition. All five other preserved map batches pass the same cache loader.
  The old and current 16-item taxonomies are byte-equivalent by taxonomy hash.
- Batch 1 was therefore regenerated against the same 66 candidates and
  contract. The current valid result contains 22 clusters: 4 singleton and 18
  multi-talk clusters. This changed the combined reducer input from 250 to 208
  proto-clusters.
- The preserved reducer is internally valid and binds the old map envelopes
  with input
  `sha256:afef7e7126e35c15538f65a06acb06af9ca4f2569d860ecd1a1affd4c3589e5e`;
  it yields the prior 15-cluster result. The current reducer correctly binds
  the changed map envelopes with input
  `sha256:9a3e61aebe2dbb26178a7e78a2db3b214a06d00a502ca724016b403f01aec12d`
  and yields 13 clusters. Its miss is the expected downstream consequence of
  batch 1 changing, not a second cache defect.
- Both the prior 15-cluster and current 13-cluster products pass final
  source-bound validation. The newer state is not shown to be editorially
  better: it was regenerated nondeterministically without any new talk digest
  or transcript evidence. The prior 15-cluster state remains the accepted
  baseline and should be recovered only through a later controlled maker run.
- The relationship reduction follows the changed topic memberships:
  `presented_at_talk_about` fell from 875 to 788,
  `co_occurs_in_talk` from 582 to 421, and
  `represented_at_talk_about` from 314 to 295. Five prior concepts disappeared
  and two new concepts appeared, explaining the net three-page/entity drop.
- Existing tests cover per-talk cache reuse but mock the cross-topic layer; no
  test exercises a valid raw map that expands above 60 clusters and is then
  loaded from cache. The affected map cache design entered in commit
  `8040c8c2`.
- Safest recovery sequence:
  1. first correct only cache admission so raw model output remains capped at
     60 while a stored completed partition may contain at most the candidate
     count, and add round-trip plus invalid-partition regressions;
  2. in a separately approved recovery story, seed the exact preserved prior
     batch 1 and reducer cache artifacts and run the authoritative maker
     pipeline so all derived wiki/static/agent products are rebuilt together
     while the corrected unmatched-resource classifier remains active.
- Do not perform a full promotion-backup rollback because that would also
  revert the corrected `2xJoimgoqBg` boundary and private outputs. Do not
  manually copy the 86 generated files. The implementation correction should
  keep the existing contract hash because it aligns stored cache admission with
  the existing `map-complete-partition-v1` result contract rather than changing
  semantic output; this is the recommended judgment for the next code review.
- This story was read-only except for this handoff update. It did not edit the
  generator or tests, seed or replace caches, restore or accept generated
  output, rerun synthesis or maker, address secondary digest findings, attach
  `2xJoimgoqBg` to Manoj Nair, acquire media, deploy, commit, push, delete
  caches or the promotion backup, or exercise monitor recurrence.

### Topic-Map Cache Round-Trip Correction

- `validate_topic_map_payload()` now has an explicit
  `stored_complete_partition` admission mode. Raw model output retains the
  existing maximum of 60 clusters and the existing cleanup/singleton-completion
  behavior.
- The cache loader uses the stored-complete mode. A completed cached partition
  may contain at most one cluster per bound candidate, must cover every
  candidate exactly once, and fails closed on duplicate, cross-cluster reused,
  unknown, missing, or over-count membership.
- The semantic contract remains unchanged at
  `sha256:17b8e63c132062ed52e1829b57b7fdf9b1b0932724ce9fb94a913b5864c43339`.
  The correction aligns cache admission with the existing
  `map-complete-partition-v1` contract; it does not change the raw model schema
  or accepted semantic output.
- Focused round-trip coverage creates 66 candidates and a valid 60-cluster raw
  response that covers 62 candidates. Deterministic singleton completion writes
  64 clusters. A second identical `obtain_topic_maps()` call returns one cache
  hit, generates zero maps, and makes no second model call.
- Focused invalid-cache coverage rejects both a four-cluster partition for
  three candidates and a partition containing an unknown candidate ID.
- All 11 tests in `tests/test_generate_talk_synthesis.py` pass. Python
  compilation and `git diff --check` pass for the changed generator and test.
  Ruff passes for both changed files with the unrelated `F841` rule excluded.
- Full focused-file Ruff still reports one pre-existing
  `topic_map = existing_slug_map("topics")` unused assignment in
  `scripts/generate_talk_synthesis.py`. The same `F841` is present in `HEAD`;
  it was not introduced or changed by this story and remains outside this
  cache-lineage slice.
- A read-only replay against the exact preserved
  `batch-01.json`, using its recorded zero-based `batchIndex: 1`, admits all 64
  clusters for its 66 bound candidates and returns a byte-equivalent payload.
  The first replay harness incorrectly selected batch index 0 and failed before
  mutation; the corrected harness used the envelope's recorded index and
  passed.
- The implementation diff is limited to
  `scripts/generate_talk_synthesis.py` and
  `tests/test_generate_talk_synthesis.py`: 20 insertions and 2 deletions in the
  generator, plus 136 test insertions.
- No canonical wiki/static/agent product, manifest, map cache, reducer cache,
  promotion backup, or protected acquisition cache was changed by this story.
  No maker plan or update, synthesis, cache seed, generated-output recovery,
  secondary digest remediation, schedule attachment, acquisition, deployment,
  commit, push, cache deletion, or monitor recurrence occurred.

### Read-Only Recovery Preflight And Maker Plan

- All six preserved topic-map batches validate against the current 69 structured
  digests, 393 candidates, and unchanged synthesis contract
  `sha256:17b8e63c132062ed52e1829b57b7fdf9b1b0932724ce9fb94a913b5864c43339`.
  They produce 250 proto-clusters, and the preserved reducer validates as the
  complete 15-cluster result.
- Exact preserved recovery artifacts remain:
  - map source
    `.ops/state/cache/wiki-maker/promotion-backups/8639437800ea61c7/wiki/resources/topic-synthesis-batches/batch-01.json`,
    SHA-256
    `1254dcf38720db8689cfd284c5abd93a3e00d33e04e43746e601f076ba0542f6`;
  - reducer source
    `.ops/state/cache/wiki-maker/promotion-backups/8639437800ea61c7/wiki/resources/cross-talk-topic-synthesis.json`,
    SHA-256
    `dadadb7768091091ab353d0e8704edce385cc9c8e241ce58babf84a3b1cf27bf`.
- Their eventual seed targets are only
  `wiki/resources/topic-synthesis-batches/batch-01.json` and
  `wiki/resources/cross-talk-topic-synthesis.json`. The current 13-cluster
  target files remain untouched at SHA-256
  `2a9c99b3fd3338379c5a13d058aec3c4c35da5be38d67b555a7441ccb12fd455`
  and
  `33ad8b61c1601af2e82d3fa813126ece6eb0f4d78508b7b1939901742d675a4a`.
- `2xJoimgoqBg` remains
  `associationEvidence: official_channel_explicit_wf26_description` with
  `matchedTalks: []`. It occurs in no talk, digest, generated claim, or
  generated highlight. Canonical and static resources say no exact
  schedule-page match is assigned and prohibit inferring schedule fields.
- Protected state is intact: `raw/video-cache` is 7.9G,
  `raw/slide-frames-tmp` is 611M, the promotion backup is 1.6G, and `/garage`
  has 42.6G available.
- Exactly one pinned read-only plan ran:

  ```bash
  python3 scripts/run_pinned_wiki_maker.py update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --plan \
    --json
  ```

- It returned `status: planned`, `ok: true`, with no run ID, execution,
  validation, agent product, receipt, private candidate, promotion, or external
  deployment. Planned ChangeSet is
  `changeset:2589de98a411cea93a4ea87524876741c6d1ec42b159b7a68aa4db64e09f544b`;
  base snapshot is
  `snapshot:69b590fa353a5a5aad41a0540541fcee48c3e6b8a6b02191667f3047575e66b1`;
  target snapshot is
  `snapshot:f280cde73521f194797ec0a6bb0bd15bcccc3364a0c4fc8a19bf912bcb506b32`.
- The ChangeSet contains exactly two `stage_version_changed` entries:
  `talk_synthesis` and `synthesis_layers`. Both correctly declare
  `scripts/generate_talk_synthesis.py` as an implementation input. No source
  root, manifest, profile, classifier, private input, canonical wiki/static, or
  other adapter entry appears.
- Maker state remained byte-identical before and after planning: 8,241,152
  bytes, modification time `2026-07-30 16:45:24.144530432 -0400`, and SHA-256
  `8ff8de2f60cd964b2d44868a7d068167d7206d351e5a35023ad1fcaba1a6f0cb`.
- The current ChangeSet must not be used after seeding. The pinned maker includes
  the canonical wiki digest in deterministic-plan currency checks, so replacing
  the two target cache files changes the plan and would make this pre-seed lock
  stale. A safe recovery therefore needs a separately approved reversible
  seeded-plan derivation before a locked execution can be named.
- A separate read-only 2026-08-03 official-media audit found 30 new public
  playlist recordings with English captions, two existing manifest items that
  are now playable, and one new unavailable playlist placeholder. None was
  imported or added to the manifest. Keep that evidence batch separate until
  the existing synthesis lineage is recovered; importing it first would make
  the current recovery plan obsolete and mix new-evidence changes with the
  unrelated 86-file drift.
- This story changed only this handoff. It did not seed or replace caches,
  restore generated output, execute maker or synthesis stages, import newly
  discovered media, address secondary digest findings, attach `2xJoimgoqBg` to
  Manoj Nair, deploy, commit, push, delete caches or the promotion backup, fix
  the unrelated Ruff finding, or exercise monitor recurrence.

### Reversible Seeded-Plan Derivation

- The current canonical targets were preserved under ignored recovery state at
  `.ops/state/cache/recovery/wf26-synthesis-current-20260803/`:
  `batch-01.json` retained SHA-256
  `2a9c99b3fd3338379c5a13d058aec3c4c35da5be38d67b555a7441ccb12fd455`, and
  `cross-talk-topic-synthesis.json` retained SHA-256
  `33ad8b61c1601af2e82d3fa813126ece6eb0f4d78508b7b1939901742d675a4a`.
- Only those two canonical targets were temporarily seeded from the exact
  preserved 15-cluster sources. No other wiki, static, raw, private, or cache
  path was seeded or changed.
- Exactly one pinned read-only plan ran against that temporary seeded state. It
  returned `status: planned`, `ok: true`, with no run, execution, validation,
  candidate, receipt, promotion, or external deployment. Its post-seed
  ChangeSet is
  `changeset:077cc7271bd6e80c5f7fb5b9a97aacabc4124774177f49bbd99366ad9f418f34`;
  base snapshot remains
  `snapshot:69b590fa353a5a5aad41a0540541fcee48c3e6b8a6b02191667f3047575e66b1`;
  target snapshot is
  `snapshot:ef295ef8ddd9adff9f8fef0111fa8979f246b9142dbf2ba4ed4bc26091c5d647`.
- The post-seed ChangeSet contains exactly three entries: stage-version changes
  for `talk_synthesis` and `synthesis_layers`, plus the intentional
  `canonical:wiki` cache replacement. It contains no source-root, manifest,
  profile, classifier, private-input, static, or other adapter change.
- The post-seed canonical wiki digest was
  `sha256:891c67d7fdea0bb05d871303515f1d4e56cad040f6355d380512b04254772b9b`;
  canonical static remained
  `sha256:8eceeb931adcdd078cd51a8e95e89ab77e8abb9a030f0b36d5796a2f485c5507`.
- The two current target files were restored and hash-verified to their exact
  pre-seed values. Maker state remained
  `sha256:8ff8de2f60cd964b2d44868a7d068167d7206d351e5a35023ad1fcaba1a6f0cb`.
- Safe locked recovery command after a separate approval is:

  ```bash
  python3 scripts/run_pinned_wiki_maker.py update . \
    --change-type media \
    --source raw/sources/official-wf26-video-manifest.json \
    --change-set changeset:077cc7271bd6e80c5f7fb5b9a97aacabc4124774177f49bbd99366ad9f418f34 \
    --json
  ```

  It is valid only when the two preserved files are reseeded exactly immediately
  before execution and the post-seed hashes/inputs still agree. If any preflight
  check differs, replan instead of forcing this ChangeSet.
- This story changed only ignored recovery state and this handoff; canonical
  targets were restored. No maker stage, synthesis, new-media import, static
  export, promotion, deployment, commit, push, cache cleanup, schedule
  attachment, secondary digest remediation, or monitor recurrence occurred.

### Locked Recovery Update

- After exact preflight of the two current drifted targets, the preserved
  15-cluster map/reducer sources, manifest, and maker state, only the two
  canonical synthesis files were reseeded. Their post-seed hashes exactly
  matched `1254dcf38720db8689cfd284c5abd93a3e00d33e04e43746e601f076ba1`
  and `dadadb7768091091ab353d0e8704edce385cc9c8e241ce58babf84a3b1cf27bf`.
- Exactly one locked pinned maker invocation ran as
  `update-20260803T074541Z-bcb4adf333`, using
  `changeset:077cc7271bd6e80c5f7fb5b9a97aacabc4124774177f49bbd99366ad9f418f34`.
  It completed successfully (`status: completed`, `ok: true`) with all 20
  required records succeeding; it was not retried.
- Candidate validation passed `agent.snapshot`, `public.boundary`, and
  `wiki.shape`. Candidate digests were canonical wiki
  `sha256:ab4d6b6d378fb1125ce1f333b5eb7b779a7dd5fbf3c61822ed037b378fc23619`
  and static site
  `sha256:e9df093e62b87bda237b38f034bcae0470ddb83736493365407cbdc28e8bb591`.
- Local promotion committed `wiki`, `site`, and the permitted private
  credibility cache under
  `promotion:ef295ef8ddd9adff9f8fef0111fa8979f246b9142dbf2ba4ed4bc26091c5d647`;
  its binding digest is
  `sha256:b97d514de3cccbeffa73724bafa4f2307884ac6e89373e856e77bffaa4175ffe`.
  Its journal is
  `.ops/state/cache/wiki-maker/promotion-journals/promotion:ef295ef8ddd9adff9f8fef0111fa8979f246b9142dbf2ba4ed4bc26091c5d647.json`,
  and its run receipt is
  `.ops/state/runs/wiki-maker-update-20260803T074541Z-bcb4adf333-attempt-001.json`.
- The canonical map restored 64 non-overlapping groups across 66 candidates;
  the cross-talk reducer restored exactly 15 clusters from 250 proto-clusters
  for 69 talks, retaining contract
  `sha256:17b8e63c132062ed52e1829b57b7fdf9b1b0932724ce9fb94a913b5864c43339`.
- `2xJoimgoqBg` remains an explicit-description-associated unmatched resource:
  it has a cached transcript and resource/registry entries, `matchedTalks: []`,
  no talk-page reference, and the public resource page explicitly prohibits
  inferred schedule fields. No Manoj Nair attachment was made.
- The agent snapshot is
  `snapshot:cfd78f738455fcb97eba37c6ffa27fa046ba49d1c76a2e5d8bb53f79ae58bf4a`.
  `agent-index.json` and `dist/agent-index.json` both name it, and
  `dist/agent/manifest.json` names the same snapshot. No external deployment,
  commit, push, cache cleanup, new-media import, secondary-digest remediation,
  or monitor recurrence occurred.

### 2026-08-03 Delta Reconciliation (Read-Only)

- The retained audit evidence has 30 newly public official-playlist recordings
  with English captions, two existing manifest rows that are now playable, and
  one newly unavailable playlist placeholder. This story did not rerun video
  discovery, download captions, import media, extract slides, or modify the
  manifest.
- Proposed lower-model acquisition scope after a separate approval: 28
  schedule-matched recordings: 27 of the newly public playlist records plus
  `hacEQHHhu2Q` (Cormac Brick), whose existing exact official schedule mapping
  is already in the manifest. The 27 new schedule-matched IDs are
  `-jY2T2PiJBE`, `s4r6nk5WsZw`, `-npY6XjM8CQ`, `2aS7aKoXn64`,
  `cJ0EOzey--o`, `_PdK6x7PQNM`, `k35LeKZEhiE`, `ewtOo0scUh0`,
  `2bvtay8wGYI`, `zkX03APVj0M`, `xbPriQWXtWM`, `3ZMUiFaQ3qg`,
  `lCBf9slCanI`, `jWq-aZIU0kM`, `AQv3qRCG6Gw`, `AVMr9PMINyo`,
  `AMiyLItEtLA`, `pWXUkLP9uWM`, `tJFjeMBKbIY`, `s67bE2Ur3bY`,
  `iKQ78wyJEXU`, `KMR_RBoCa4M`, `7jjudsEhBtM`, `kiqubc5b5Yo`,
  `BInpv7lGp1o`, `KhYifX22yhE`, and `Ib5t2RLtxvM`.
- Correct the prior automatic Thais ambiguity during that import:
  `lCBf9slCanI` may attach only to `Ending AI Slop`, never `Training Taste`.
  The 9 additional local schedule confirmations were Cornelia Davis,
  Ross/Chengxi Taylor, Shawn Chan, Sai Krishna Rallabandi, Lucas Palma,
  Aman Gupta/Shreya Rajpal, Yogendra Miraje, Brendan Rappazzo/AlphaLab, and
  Rustem Feyzkhanov.
- Proposed resource-only import scope: `ZFxh7sqbUZo` (David Brumley),
  `CgsWxRUY5Eo` (Rajat Shah), and `Yk87oUPVaxU` (James Shi). Their official
  playlist membership supports WF26 media association, but David's generic
  schedule title is not an exact title match and no official schedule rows were
  found for Rajat or James. Keep them resource-only with no inferred schedule
  fields.
- Hold `O72p-rBb2bA` (Akele Reed/Dave Revere) out of the proposal until a
  fresh exact official-title/schedule match is recorded: its current manifest
  row remains an unavailable unmatched placeholder even though the audit saw a
  playable recording. Exclude the newly unavailable `sJHg0mC5Png` and still
  unavailable `Z3fP-eMEx-8` / `PXXNCtfKZs0` from acquisition.
- The proposal therefore has 31 playable recordings: 28 schedule-matched and
  3 resource-only. It deliberately defers one playable legacy row and all
  unavailable placeholders. `2xJoimgoqBg` remains unrelated to this batch and
  must remain unmatched from Manoj Nair.

### 2026-08-03 Lower-Model Acquisition

- Transaction-backed acquisition completed as
  `.ops/state/runs/manual-official-video-import-2026-08-03-lower-model.json`:
  31 processed, 28 schedule-matched, and 3 resource-only. It imported English
  captions/transcript text, scene-aware slide frames and OCR, resource pages,
  and only the approved talk links; transient 403 slide fetches recovered on
  the built-in second attempt.
- Manifest now has 113 records, with 107 cached transcripts and 106 cached
  slide sets. All 31 have resource, transcript, and slide artifacts. The three
  resource-only IDs have no talk-page reference; `lCBf9slCanI` maps only to
  `2026-06-29-thais-castello-branco-ending-ai-slop`.
- No maker run, static export, promotion, deployment, commit, push, cache
  cleanup, monitor recurrence, `O72p-rBb2bA` import, unavailable placeholder
  import, or `2xJoimgoqBg` schedule attachment occurred.

### 2026-08-03 Higher-Model Media Update Attempt

- After explicit operator approval on Sol medium, the pinned authoritative media
  update was invoked exactly once as `update-20260803T105122Z-f1a9863813`.
  Its durable receipt is
  `.ops/state/runs/wiki-maker-update-20260803T105122Z-f1a9863813-attempt-001.json`.
- `classify_media`, `credibility_provider_checks`, `transcript_pages`, and
  `credibility_policy` succeeded in the retained candidate. Required stage
  `talk_media_map` then failed closed because manifest item `Ib5t2RLtxvM` has
  official `playlistId` metadata but no valid positive `playlistIndex`.
  Read-only validation found the same missing `playlistIndex` on all 31 records
  from the lower-model acquisition; `Ib5t2RLtxvM` was only the first item
  rejected by input validation.
- The retained candidate contains transcript markdown for all 31 new records,
  but canonical contains none of those 31 transcript pages because promotion
  did not occur. Talk synthesis, downstream enrichment, registries/static
  export, agent-product build, public validation, and promotion were blocked.
  The receipt records `promotion: null`, `validation: null`,
  `agent_product: null`, and `external_deployment: false`.
- Canonical source boundaries remain intact: `ZFxh7sqbUZo`, `CgsWxRUY5Eo`,
  and `Yk87oUPVaxU` occur on zero talk pages; `lCBf9slCanI` occurs only on
  `2026-06-29-thais-castello-branco-ending-ai-slop`; and `2xJoimgoqBg`
  occurs on zero talk pages. `agent-index.json`, `dist/agent-index.json`, and
  `dist/agent/manifest.json` still agree on pre-run snapshot
  `snapshot:cfd78f738455fcb97eba37c6ffa27fa046ba49d1c76a2e5d8bb53f79ae58bf4a`.
- No retry, discovery, caption import, slide extraction, canonical promotion,
  deployment, commit, push, cache cleanup, monitor recurrence, or unrelated
  fix was performed. The failed candidate and promotion backups remain
  preserved for diagnosis/recovery.

### 2026-08-03 Playlist-Index Repair

- The retained read-only reconciliation log contains the complete 93-item
  official playlist snapshot captured at `2026-08-03T06:40Z`. Its positions
  were recovered locally without querying YouTube or rerunning discovery.
- Exactly the 31 lower-model acquisition records received their missing
  positive `playlistIndex` values. A direct expected-map check confirms all 31
  IDs match the captured positions; JSON parsing and `git diff --check` pass.
- Read-only `python3 scripts/generate_talk_video_transcript_map.py --check`
  advanced beyond the original missing-index error but failed closed on
  `duplicate playlistIndex: 44`. Full snapshot comparison found 46 existing
  indexed manifest rows still carrying older pre-insertion positions; 29 of
  those positions collide with the restored 31. Updating those older rows was
  outside this story's explicit 31-field boundary and was not performed.
- The snapshot also contains 15 existing manifest videos with no playlist
  metadata and unavailable `sJHg0mC5Png`, which remains absent by the existing
  exclusion boundary. Neither is required to resolve the current duplicate
  validator failure, and neither was changed or imported in this story.
- No maker update or retry, discovery, caption import, slide extraction,
  synthesis, static export, promotion, deployment, commit, push, cleanup,
  schedule attachment, or monitor recurrence occurred.

### 2026-08-03 Stale Playlist-Index Reconciliation

- Exactly the 46 existing playlist rows identified by the prior validation
  received their current positions from the retained 93-item official-playlist
  snapshot. The 31 newly repaired rows were not changed again.
- Snapshot comparison now reports 77 indexed playlist rows, 77 exact matches,
  zero stale indexed rows, and zero duplicate positions. JSON parsing and
  `git diff --check` pass.
- Read-only
  `python3 scripts/generate_talk_video_transcript_map.py --check` no longer
  raises an input exception. It reports `changed: true` because the canonical
  generated map has intentionally not been rebuilt in this no-maker story;
  both slide and topic change counts are zero.
- The 15 snapshot-known existing videos without playlist metadata remain
  untouched, and unavailable `sJHg0mC5Png` remains absent. Existing
  `O72p-rBb2bA` remains an unavailable unmatched placeholder; only its stale
  playlist position changed from 44 to 45.
- Source boundaries remain intact: the three resource-only records occur on
  zero talk pages, `lCBf9slCanI` occurs only on `Ending AI Slop`, and
  `2xJoimgoqBg` occurs on zero talk pages. All three canonical agent pointers
  remain on
  `snapshot:cfd78f738455fcb97eba37c6ffa27fa046ba49d1c76a2e5d8bb53f79ae58bf4a`.
- No maker update or retry, discovery, caption import, slide extraction,
  synthesis, static export, promotion, deployment, commit, push, cleanup,
  schedule attachment, or monitor recurrence occurred.

### 2026-08-03 GitHub Checkpoint Publication

- At `2026-08-03T17:18:58Z`, the operator explicitly approved publishing the
  accumulated official-media refresh to GitHub as a checkpoint.
- Publication is isolated on `agent/wf26-official-media-refresh` as a draft PR
  to `main`; it is not merge-ready because the one authorized authoritative
  maker retry, validation, canonical promotion, and higher-model review remain
  pending.
- Content checkpoint `fae30867` was pushed and opened as draft PR
  `https://github.com/mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki/pull/1`.
  A following continuity-only commit records this readback on the same branch.
- Focused pre-publication validation passed 60 tests. The only failure is the
  expected checked-in talk/video map mismatch: the read-only generator reports
  `changed: true`, with zero slide-page and topic-page changes, because this
  checkpoint does not run or substitute for the maker promotion.
- No deployment, merge, cache cleanup, monitor recurrence, or additional maker
  invocation is authorized by this checkpoint publication.

### Deferred Cleanup Gate

- The operator requested a deliberate cleanup story once the media refresh is
  at a safe stopping point. Do not perform it during manifest repair, maker
  retry, or higher-model editorial/source-boundary review.
- The cleanup gate opens only after a repaired authoritative run has completed,
  maker validation has passed, canonical promotion and agent snapshot readback
  are verified, and the higher-model review no longer needs recovery artifacts.
- At that point, first inventory and size the rebuildable/superseded candidates:
  `raw/video-cache`, `raw/slide-frames-tmp`, failed or superseded maker
  candidate workspaces, and promotion backups. Present exact targets and obtain
  explicit approval before deletion; then verify before/after disk usage.
- Preserve canonical wiki/static/agent outputs, official manifests and raw
  sources, transcripts/subtitles, published slide assets and OCR evidence,
  run/stage/promotion receipts, journals still needed for recovery, and the
  minimum state required to prove the promoted generation. Never treat all of
  `.ops/state/cache` as one deletion target without an approved retention map.

### Next Thin Slice

After a new explicit operator decision, run the pinned authoritative media
update exactly once against
`raw/sources/official-wf26-video-manifest.json`. Validate canonical transcript
markdown for the 31 new recordings, synthesis for the 28 schedule-matched
talks, resource-only treatment for the three unmatched recordings, refreshed
registries/static export, aligned agent snapshot, maker validation, and local
promotion receipts. Do not rerun discovery, caption import, slide extraction,
or monitor recurrence; import `sJHg0mC5Png`; import `O72p-rBb2bA` as new media;
attach `2xJoimgoqBg` to Manoj Nair; deploy, commit, push, clean protected
caches/backups, or fix unrelated Ruff. If the single maker run fails, inspect
and stop without retrying.

## Next-thread introduction

Retired because its former next action is complete. Follow the current
`Status`, `Next Thin Slice`, hard boundaries, and deferred cleanup gate above.

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
