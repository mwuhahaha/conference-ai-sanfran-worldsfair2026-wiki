# World's Fair Static Navigation Follow-Up

## Purpose

Apply the strongest public-navigation lessons from the Miami wiki without changing the World's Fair source boundaries or read-only deployment contract.

## Hard Boundaries

- Keep the site fully static and read-only.
- Derive graph relationships from existing public wikilinks at build time.
- Do not delete or flatten generated schedule and media evidence pages.
- Keep official schedule facts distinct from transcript, video, OCR, slide, and inferred synthesis layers.
- Work one reversible story at a time.

## Stories

### S1 - Static Knowledge Graph

- [x] Generate a complete JSON node/link dataset from resolved public wikilinks.
- [x] Publish a `/graph/` page with category filtering, search, a category legend, node detail, and nearby-page navigation.
- [x] Add Graph to the shared static-site navigation.
- [x] Keep rendering bounded for browser responsiveness while leaving the full dataset available at `/graph-data.json`.

Validation:

- `npm run build`
- `node --check dist/graph.js`
- JSON integrity check for node/link endpoints

### S2 - Conference-Native Home

- [x] Replace the long article-first home presentation with event/source panels.
- [x] Surface useful category and source-layer counts.
- [x] Explain the official schedule versus supporting media/synthesis boundary.
- [x] Keep primary event, schedule, livestream/video, agent-index, and graph links prominent.

Validation:

- `npm run build`
- `python3 -m py_compile scripts/export_static_site.py`
- `node --check dist/graph.js`
- JSON integrity check for graph node/link endpoints
- Headless Chrome DOM/screenshot smoke check for the new home page

### S3 - Build-Time Local Navigation

- [ ] Generate consistent backlinks, outgoing links, and nearby-page sections at build time.
- [ ] Keep the sections static and read-only.
- [ ] Preserve source-boundary language on talk, resource, transcript, slide, and synthesis pages.
- [ ] Avoid reshaping category landing pages in this story.

## Next Thin Slice

Implement S3 only: build-time backlinks, outgoing links, and nearby-page sections for rendered pages.
