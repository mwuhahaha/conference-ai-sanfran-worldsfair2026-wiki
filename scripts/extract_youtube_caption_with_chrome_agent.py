#!/usr/bin/env python3
"""Extract a YouTube transcript through the local Chrome browser agent.

This is a fallback for cases where YouTube blocks direct caption APIs or yt-dlp
with 429 / bot-check responses. It uses the browser-use project at
/garage/projects/agents/chrome-agent-python to render the public YouTube watch
page, opens the visible transcript panel, and writes cleaned transcript text.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
from pathlib import Path

from browser_use.browser import BrowserSession


def clean_panel_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^\s*(?:In this video\s+Chapters\s+)?Transcript\s+Search transcript\s+", "", text, flags=re.I)
    text = re.sub(r"^\s*Search transcript\s+", "", text, flags=re.I)
    text = re.sub(r"\bChapter\s+\d+:\s+[^.?!]{3,90}(?=\s+[A-Z\[])", " ", text)
    text = re.sub(
        r"\b\d{1,2}:\d{2}(?::\d{2})?\s+(?:\d+\s+hours?(?:,\s*)?)?(?:\d+\s+minutes?(?:,\s*)?)?(?:\d+\s+seconds?)?",
        " ",
        text,
    )
    text = re.sub(r"\b\d{1,2}:\d{2}(?::\d{2})?\b", " ", text)
    return re.sub(r"\s+", " ", text).strip()


EXTRACT_JS = r"""
(...args) => (async () => {
 const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 const norm=s=>(s||'').replace(/\s+/g,' ').trim();
 const all=()=>[...document.querySelectorAll('button,tp-yt-paper-button,yt-button-shape button,ytd-button-renderer button')];
 const more=all().find(el=>/\.\.\.more|more$/i.test(norm(el.innerText||el.textContent||el.getAttribute('aria-label'))));
 if(more){more.click(); await sleep(1200)}
 for(let i=0;i<8;i++){
   const btn=all().find(el=>/show transcript/i.test(norm(el.innerText||el.textContent||el.getAttribute('aria-label'))));
   if(btn){btn.click(); break;}
   window.scrollBy(0,450); await sleep(700);
 }
 await sleep(6000);
 let panel=[...document.querySelectorAll('ytd-engagement-panel-section-list-renderer')].find(el=>el.getAttribute('visibility')==='ENGAGEMENT_PANEL_VISIBILITY_EXPANDED' && /Transcript/i.test(norm(el.innerText||el.textContent||'')));
 if(!panel){ panel=[...document.querySelectorAll('ytd-engagement-panel-section-list-renderer')].find(el=>/Search transcript/i.test(norm(el.innerText||el.textContent||''))); }
 return JSON.stringify({
   url: location.href,
   title: document.title,
   panelFound: !!panel,
   panelText: norm(panel ? (panel.innerText||panel.textContent||'') : ''),
   bodySample: norm(document.body ? document.body.innerText : '').slice(0, 1200)
 });
})()
"""


async def extract(video_id: str, *, headless: bool) -> dict[str, object]:
    browser = BrowserSession(
        headless=headless,
        allowed_domains=["youtube.com", "www.youtube.com", "*.youtube.com", "google.com", "*.google.com"],
        wait_for_network_idle_page_load_time=3,
        viewport={"width": 1440, "height": 1000},
    )
    await browser.start()
    try:
        await browser.navigate_to(f"https://www.youtube.com/watch?v={video_id}")
        await asyncio.sleep(9)
        page = await browser.get_current_page()
        return json.loads(await page.evaluate(EXTRACT_JS))
    finally:
        await browser.stop()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--headless", action="store_true")
    args = parser.parse_args()

    headless = args.headless or not bool(os.environ.get("DISPLAY"))
    data = asyncio.run(extract(args.video_id, headless=headless))
    cleaned = clean_panel_text(str(data.get("panelText", "")))
    report = {
        "id": args.video_id,
        "status": "no_transcript_found",
        "word_count": len(cleaned.split()),
        "panel_found": data.get("panelFound"),
        "page_title": data.get("title"),
        "sample": (cleaned or str(data.get("bodySample", "")))[:260],
    }
    if len(cleaned.split()) >= 120 and "Premieres in" not in str(data.get("bodySample", "")):
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(cleaned + "\n", encoding="utf-8")
        report["status"] = "written"
        report["path"] = str(output)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["status"] == "written" else 2


if __name__ == "__main__":
    raise SystemExit(main())
