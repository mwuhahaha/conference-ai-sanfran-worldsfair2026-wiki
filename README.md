# AI Engineer World's Fair 2026 Clean Wiki

Clean AIE-specific World’s Fair 2026 wiki built from the upgraded local project.

This directory keeps:
- generated official schedule pages
- people/company/talk/resource pages
- slide decks and reconstructed slide decks
- RapidOCR-improved OCR text
- livestream transcript bundles
- source summaries and audit receipts
- local scripts needed to rebuild or extend the wiki

This directory intentionally excludes heavyweight regeneration caches:
- `raw/video-cache/`
- `raw/slide-frames-tmp/`
- `raw/experiments/`
- `raw/tmp/`

Use the original `conference-ai-sanfran-worldsfair2026` directory if full video/frame regeneration caches are needed.

## Current Focus

This clean copy is meant to become the AIE-specific conference intelligence version of the World’s Fair wiki: not a generic personal wiki and not only a generated schedule archive.

Read:
- `.ops/plans/worldsfair-static-navigation-followup.md`
- `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
- `.ops/state/current.md`

## Validation

From this directory:

```bash
npm run build
```

The build sanitizes public text, refreshes the agent index, normalizes article section shapes by page type, then writes the deployable static site to `dist/`. The export includes the complete wiki-link dataset at `dist/graph-data.json`, an evidence-bearing semantic dataset at `dist/relationship-data.json`, the relationship explorer at `dist/graph/index.html`, and the full advanced graph at `dist/graph/all/index.html`.

## Unified Wiki Update

`.wiki-maker.json` is the project profile for ordered, trigger-aware wiki
maintenance. From this repository, the authoritative official-media update is
one pipeline command:

```bash
wiki-from-topic-maker update . \
  --change-type media \
  --source raw/sources/official-wf26-video-manifest.json \
  --json
```

The maker computes a deterministic plan from the source change and profile,
runs the configured adapters in a private candidate workspace, validates the
public boundary, and promotes the validated wiki and static agent product
locally. It does not deploy the site externally. The official YouTube monitor
invokes this same update entry point once when it has admitted new event media;
it does not maintain a separate generator chain.

The reconciled official-media union contains 34 items: 29 playable recordings
or livestreams, 3 scheduled premieres, and 2 unavailable playlist
placeholders. All 29 official-playlist entries are represented; five other
official WF26 recordings or livestreams were admitted through the separately
labeled official-event boundary. Cached transcripts cover 25 of the 29
playable items, and the four gaps remain explicit. The generated transcript
layer contains 123 pages, labeled as 28 primary-event transcripts and 95
supporting-context transcripts. Typed slide outcomes exist for all 29 playable
items.

Final local run `update-20260717T151153Z-c726308cdf` completed all 18 adapters
and both maker runtime stages, then promoted target snapshot
`snapshot:7eb9e7909f90fe52706542953a7daa1d3b0009380f93b09f32361d5c868340de`.
Its 2,437-page agent product is
`snapshot:62900940db784a1c6b68bb19a4a20c0bc14bcd87dae2ef27ee28cbbab0edd1ab`.
The identical follow-up request returned a planning no-op. No external
deployment was performed. Publishable inventory follows Git visibility, so an
ignored untracked local overlay is excluded from wiki, static, agent, graph,
and relationship products without being deleted from the operator workspace.

Private review-policy bootstrap data lives only at the ignored local path
`.ops/state/cache/wiki-maker/private-policy.json`, referenced through
`.wiki-maker.json`. Never copy that file or its contents into `wiki/`,
`raw/sources/`, `dist/`, the agent index, or another publishable artifact.
The deeper provider, browser, evidence, and writing-policy state follows the
same boundary under `.ops/state/cache/wiki-maker/credibility-v2/`; only
reviewed, attributed source context may be projected into public articles.

## Diagnostic Toolkit

Input acquisition and repair tools can still prepare source artifacts. Direct
generator, enricher, normalizer, and exporter invocations are stage-level
debugging tools only; they are not a completed production update and must not
replace the maker command above.

The external video discovery tool searches YouTube beyond the official AI Engineer channel, requires conservative corroboration against the official schedule, treats admitted matches as secondary sources only, and writes its audit report to `wiki/resources/external-video-discovery.md`.

The talk synthesis tool adds transcript/source-backed sections to talk pages. The highlight generator publishes both the normal highlights index and the grouped `Highlighted Concepts, People, And Talks` map. Invoke either directly only to diagnose its stage in isolation.

The synthesis layer generator publishes claims, patterns, harnesses, playbooks, evaluations, topic evidence tables, and livestream thematic anchors. It must not emit private review-policy artifacts into public wiki pages, public raw sources, or the agent index.

The evolution-context enricher adds reviewed `How This Theme Evolved`, `Why This Matters Now`, and `Practical Lesson` sections to configured topic or synthesis pages. Its portable profile lives at `raw/sources/evolution-context-profile.json`. Earlier wikis are comparison context only; a section is emitted only when the target page already links to the profile's required local evidence. The maker applies this stage. `python3 scripts/enrich_evolution_context.py --all --dry-run` is available only for a bounded diagnostic preview.

The article shape normalizer keeps page types consistent without forcing every article into the same outline. Talks use a session-article shape, people use a profile shape, companies use an organization shape, topics use a concept-article shape, and question/harness/playbook/evaluation pages use synthesis shapes. It folds explicit "what/why/how" style headings into more agent-friendly sections such as `Overview`, `Conference Context`, `Significance`, `Technical Model`, `Applied Use`, `Connections`, and `Evidence Graph`. `npm run build` runs this normalizer before export.

The slide OCR pipeline rereads weak or suspicious slide frames with local OCR engines, crop detection, OpenCV preprocessing, and high-contrast variants. It compares those outputs with existing Tesseract/RapidOCR/reconstructed/dense OCR artifacts, updates canonical slide OCR only when quality improves, refreshes slide markdown, regenerates dependent tool/topic indexes, and writes an audit report. For a narrow debug run, use `python3 scripts/run_slide_ocr_pipeline.py --limit 50 --no-build`.

For a fuller quality pass, run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --internal-eval-log`. The five free/local improvement paths now supported by the toolkit are: OpenCV crop/threshold preprocessing, RapidOCR live rereads, PaddleOCR rescue reads, EasyOCR/docTR adapter hooks for CPU/GPU installs that provide Torch cleanly, and Surya as an explicit opt-in after checking model-weight license terms. PaddleOCR is available as a targeted rescue engine, but it is too slow for default whole-corpus runs on this host. Operator-verified text belongs under `raw/sources/slide-ocr-operator-verified/`; run `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --no-live-ocr --internal-eval-log` to merge those corrections without rerunning live OCR. Internal eval logs are written under `.ops/state/cache/` and are intentionally ignored by git.

When OCR is visibly bad, use the AI vision rescue layer instead of only adding OCR engines: `python3 scripts/run_slide_ocr_pipeline.py --all --skip-perfect --engine rapidocr --vision-rescue --vision-provider codex-cli --internal-eval-log`. The rescue tool reads low-confidence/manual-queue slide frames with a vision model, writes accepted text to `raw/sources/slide-ocr-ai-vision/`, and then reruns a no-live merge. It can resume from existing accepted files in `raw/sources/slide-ocr-ai-vision/`; use `--vision-jobs 2` or `--vision-jobs 3` for a bounded parallel Codex CLI pass. It can use free local Ollama vision, Codex CLI via the existing local login, or the OpenAI Responses API only when `OPENAI_API_KEY` is set or `--vision-provider openai` is chosen. Codex CLI vision rescue defaults to `gpt-5.4-mini`; override it with `CODEX_VISION_MODEL` or `--vision-codex-model`. The OpenAI model is configurable with `OPENAI_VISION_MODEL`.

Future video slide extraction can use scene-change frame sampling and sharpness replacement with `python3 scripts/extract_video_slides.py --scene-detect --video-id <id>`.

## Static Site Export

This repository can be deployed as a static Cloudflare Pages site.

Local build:

```bash
npm run build
```

The build normalizes article shapes and writes a pre-rendered static site to `dist/`, including `/graph/`, `/graph/all/`, `/relationship-data.json`, `/graph-data.json`, and the standalone `/agent-index.md` contract.

Cloudflare Pages Git integration settings:

- Repository: `mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki`
- Production branch: `main`
- Build command: `npm run build`
- Build output directory: `dist`
- Root directory: repository root
