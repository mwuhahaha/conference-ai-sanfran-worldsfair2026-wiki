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
- `.ops/plans/worldsfair-aie-specific-conversion-plan.md`
- `.ops/state/current.md`

## Validation

From this directory:

```bash
python3 /garage/obsidian/scripts/generate_calendar.py
```

For link/asset validation, use the command embedded in the conversion plan.

## Static Site Export

This repository can be deployed as a static Cloudflare Pages site.

Local build:

```bash
npm run build
```

The build writes a pre-rendered static site to `dist/`.

Cloudflare Pages Git integration settings:

- Repository: `mwuhahaha/conference-ai-sanfran-worldsfair2026-wiki`
- Production branch: `main`
- Build command: `npm run build`
- Build output directory: `dist`
- Root directory: repository root

Wrangler direct-upload deployment, after authenticating Wrangler:

```bash
npm run pages:deploy
```

Planned Pages project name: `aie-worldsfair2026`.

Planned custom domain: `aie-worldsfair2026.plusrobot.ai`.
