---
title: "Google Photos Slides: The Dark Arts of Web Automation"
category: "slides"
import_id: "aie-slides-9gWZzS1EpXM1C5eK6"
author: "boxofchocolates"
sourceLabels: ["Google Photos share", "Phone photo slide evidence", "RapidOCR text"]
confidence: "high"
---

# Google Photos Slides: The Dark Arts of Web Automation

## Source
- Author: boxofchocolates
- Source type: Google Photos album import supplied to the wiki builder.
- Imported source layer: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/`
- OCR engine: RapidOCR over downloaded Google Photos images.

## Relationship To World's Fair 2026
These photos are matched to the following scheduled session(s):
- [[2026-06-30-corey-gallon-the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans]] - The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans

## Match Confidence
- Confidence: high
- OCR names CDP browser, Sense/Act/Verify, Meatbag Ladder, Demazon, Cloudflare Turnstile, MTCaptcha, chrome-agent, @coreygallon, and Runlayer.
- The slide content uniquely matches the Dark Arts of Web Automation talk.
- Timestamp note: Photo timestamp aligns with the Day 3 12:05 computer-use slot; the generated talk page is the canonical schedule page.

## Photo Slides
### Photo 028
- Captured at UTC: 2026-07-01T19:06:52.268000+00:00
- Captured local clock: 2026-07-01T12:06:52.268000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-028.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-028.jpg]]

OCR text:

> meatbag with a mouse. A CDP browser is just a
> as far as Google, Cloudflare et al. can tell -June 2026
> Runlayer

### Photo 029
- Captured at UTC: 2026-07-01T19:10:39.585000+00:00
- Captured local clock: 2026-07-01T12:10:39.585000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-029.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-029.jpg]]

OCR text:

> Sense →Act →Verify. Repeat until it closes. I/ THE 3RD THING
> aim DOM.ally tree SENSE ACT Bu uoo aclick·akeystroke·anav sense again -a different channel VERIFY confirm
> never trust the click's own “success.
> When the loop won't close on a rung - that's the signal to climb. LOOP+LADDER
> rfeung

### Photo 030
- Captured at UTC: 2026-07-01T19:11:46.018000+00:00
- Captured local clock: 2026-07-01T12:11:46.018000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-030.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-030.jpg]]

OCR text:

> The Meatbag Ladder. I/ THE 3RD THING
> Climb only as high as the page forces you.
> RUNG3 HUMAN - the narrow frontier trusted input +behaviour:mouse path,dwell,jitter,vision CAPTCHA
> RUNG 2 a trusted click through the native pipeline · Input.dispatchMouseEvent REAL- the workhorse Demazon
> RUNG1 don't act human at all - be a program, or fake the click FAkE -the smart default Outlook

### Photo 031
- Captured at UTC: 2026-07-01T19:13:06.209000+00:00
- Captured local clock: 2026-07-01T12:13:06.209000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-031.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-031.jpg]]

OCR text:

> Explore,then automate. /THE TWO PHASES
> these rungs. known-working solution: this exact sequence, on climb rungs until it works - you end holding a run the loop by hand PHASE 1·EXPLORE write it down PHASE 2· AUTOMATE AGENT SKILL- reptays & adapts to UI changes, like a human CoDE-deterministic·fast,-so/run·no agent
> when it's extra tricksy = do both,
> →Explore once, automate forever. That's the whole method.

### Photo 032
- Captured at UTC: 2026-07-01T19:16:00.790000+00:00
- Captured local clock: 2026-07-01T12:16:00.790000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-032.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-032.jpg]]

OCR text:

> RUNG2·REAL Demazon -trusted click a Js click is a function
> rung2 add to cart.py
> box = iframe_coord('#add-to-cart') # SENSE #[RUNG 2] real, trusted click·Input.dispatchMouseEvent
> assert cart ==1 # VERIFY #ACT -trusted native pipeline Input.dispatchMouseEvent（box) #/ ACCEPTED #event.isTrusted = false el.dispatchEvent(evt) # REJECTED el.click() #REJECTED demazon.com Whatyou see SWITCH KVM Dual Monitor,USB TESmart2-PortKVMSwitch $26995 InSt SYNTHETIC JSCLICK el.click() Add toCart
> time step trusted decision
> No attemptsyet
> the gate is event.isTrusted. the server log is the X-ray.

### Photo 033
- Captured at UTC: 2026-07-01T19:17:53.897000+00:00
- Captured local clock: 2026-07-01T12:17:53.897000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-033.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-033.jpg]]

OCR text:

> RUNG 3·HUMAN Cloudflare Turnstile a checkbox behind 3 nested boundaric turnstile
> read PoST /verify/turnstile # VERIFY await_cfSolved #/token #Chrome hit-tests down through all3 Input.dispatchMouseEvent(cb) # ACT trusted DOM.getBoxModel(iframe) # SENSE checkbox=（box.x+30,box.y+h/2) #find the Turnstile <iframe> node DOM.getDocumentpierce} # SENSE =[RUNG 3] reach the buried checkbox·click the glass solve.py interaction (the cross-origin-iframe trusted test secret always-passes,so this proves the interactive) time,so it'sa reliable on-camera target.The 'verify you are human' checkbox shows every Turnstile (test key Cloudflare's force-interactive TEsT key: the -always Cloudflare EMBEDDABLEWIDGET
> click),not a real token.
> CLOUDFLARE
> For testing only.If seen, report to site owner Privory·Helo
> Check
> areal click lands on the glass-Chrome does the rest.
> Runlayer Runlayer

### Photo 034
- Captured at UTC: 2026-07-01T19:19:34.695000+00:00
- Captured local clock: 2026-07-01T12:19:34.695000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-034.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-034.jpg]]

OCR text:

> RUNG 3·HUMAN MTCaptcha read it with vision · type it
> solve.py
> #[RUNG 3] read with vision · type trusted keys MTCaptcha VENDORACCOUNT
> for ch in answer: dispatchKeyEvent # ACT Input.dispatchMouseEvent(field) # ACT screenshot crop - read chars #vision #iframe -its own CDP session Target.setAutoAttach flatten } # SENSE challenge. Verified via MTCaptcha's checktoken APl. GDPR-focused checkbox+image/text
> await verified == true # VERIFY # trusted keystrokes into the OoPIF YYOR
> YYOR
> Verified Successfully
> Chgck
> real challenge, really read and typed. Captcha passed successfully!

### Photo 035
- Captured at UTC: 2026-07-01T19:25:44.101000+00:00
- Captured local clock: 2026-07-01T12:25:44.101000+00:00
- Raw OCR: `raw/sources/google-photos-slides/aie-slides-9gWZzS1EpXM1C5eK6/ocr/photo-035.txt`

![[assets/slides/google-photos-aie-slides-9gWZzS1EpXM1C5eK6/photo-035.jpg]]

OCR text:

> A meatbag with a mouse.
> Everything today came from that one idea. Teach an agent CDP and it moves through the web on the very same path you do.
> s uv tool install chrome-agent
> follow me on x @coreygallon
> ~/chrome-agent s happy hacking
> Runlayer
