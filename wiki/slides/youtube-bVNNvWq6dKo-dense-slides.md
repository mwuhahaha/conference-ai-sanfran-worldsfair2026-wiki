---
title: "Dense Slides: How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf"
category: "slides"
video_id: "bVNNvWq6dKo"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf

## Source Video
[How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=bVNNvWq6dKo)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/bVNNvWq6dKo/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/bVNNvWq6dKo/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> Principle
> Trajectories
> Related features
> • "Continue my work"
> • Terminal Turbo mode
> • Agentic diff review UX

![[assets/dense-slides/bVNNvWq6dKo/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/bVNNvWq6dKo/slide-002.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: none.
- OCR decision: ready — Dense UI screenshot and small terminal text are better suited for OCR than manual transcription.
![[assets/dense-slides/bVNNvWq6dKo/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/bVNNvWq6dKo/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Contains multiple small embedded tweet screenshots and dense quoted text; OCR is the cheaper, more reliable pass.

Slide text:

> We are the first and only company to replace Chat
> with Agents
> *and people love that
> MIChaLO Follow
> fesure before coding it Yery coo! lan Nuttall O Whether it wntes code or helps you spec o Yep. they cal t Cascade and you can tog Shao1少紫0 Follow dtling feels nore natural ano butn thole orocess of the code generauon and tave tested both ard my pck is Windsurt
> are the same. The deep context awareness of Those who know, know. Not all Al based editors
> windsurf is truly remarkable. lt even knows the
> erico compared to from compose/ 3gent mode to chat vhile one subtle ux diff I apprechte in maintaining thc conversaton s the abiity to sy cursor location, the changes so far,other files1 didn't mention, and it doesn't have the arbitrary separation of composer vs chat in UX. Scott Forsyth o Grenlrsvieo tve ucd Windhurt nlesn Hhs he Couplr ol wrerke inel I snctely reler l vre. Cukor R fect morc inievhRid hrd nntvh

![[assets/dense-slides/bVNNvWq6dKo/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/bVNNvWq6dKo/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Product UI screenshot and nested sidebar/chat text are small and OCR-suitable.

Slide text:

> 6 p $t-ou+p > > C pubsc $ C tnoxt' +>. C noda_modules. Iy ca sre/apo Yta Images: O eulhrconngmp' e page.tsx I pat-my.dts. S psckaga-lock.json: G package json. 1l globalscss Douoneo postcss.contig.mft. READMEmd: byuospumn mindsurfriles: N. net.config.ts K rxt.corigjs T thconig.Jton' 鲁layout.rgx Clricon.lico ' roure.tsx n Code mith Csscada Windsurf Dev: Edil codo intno. ' Let rmo chock tho offcisl Naxt.js documentation frst.:sesrch for relevant documentation..: Let mo chock anbther chunk to seo if thore't' sny addrtlonaf irmportant information. I'l hclp you fnd Iniormation about genaating dynam'c OG Images in Nextjs. Let me: Let me check the docurmentetion about generating lmages using code, which hs most: I + Croited ouuina a rextjt org' rtevant to yotr request. +:Arulyzed contert. a Cemerot4 + Dynamicaity Generated OG hmagos in NerLS:- Jomes Shoplnd? Optimiing: Motsdote - Next js *o Searchid wsb: Neitje dynamic Og Imsge genration route.tsx documentston +Hoir to generate dynamic OG imago using new Naxts with App directory d?.. Look up the NeaUS dacumenttion for me to ginerate't dynamle Oo imsgt d route.tx: Metsdats ller: opengraph-imsge snd twtter-lmage - Next.js 0 Dymamleatty Generatng Cpen Graoh rnsg+s n Nexat.js 14 0 imoges using coct (ss..to...tsx)! Veiw Psoe
> 'syura t m yueyos pazAleuy' o
> generation at route.ts. Here's whst... Based on the Next.ja documontatlon, I can help you Implement a dynomic CG ima ga Sd a tmiow.
> supanos meation E Add irugm A Clud 15 Sonmel: At snyihurg (xl), e to smention code brocks C Hite

Classification audit: `raw/sources/slide-ai-classification/dense/bVNNvWq6dKo/audit.json`
