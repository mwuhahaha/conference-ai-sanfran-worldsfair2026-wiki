---
title: "Dense Slides: Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind"
category: "slides"
video_id: "cVzf49yg0D8"
sourceLabels: ["Captured video frames", "Local OpenCV slide-region detection"]
---

# Dense Slides: Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind

## Source Video
[Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=cVzf49yg0D8)

## Method
This deck is slide-only. The existing captured video frame set supplies candidate frames, then local OpenCV rejects sponsor/title/speaker-only frames, crops visible slide surfaces, deduplicates, and saves the cropped slide images.

## Cropped Visible Slides
![[assets/dense-slides/cVzf49yg0D8/slide-001.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-001.html)
- AI slide classifier: `content_slide` confidence `0.97`
- Text source: advanced OCR `rapidocr-live/border-trim/opencv-adaptive`.
- OCR decision: ready — Dense product UI screenshot with many small labels and controls.

Slide text:

> D
> c Dashbordi Googke A Studo APl-Schlussel B Ap·Kurznetung
> APt:Schbusset Profektai.: Gruppiren rach Projokt:ofeld oy pto ltl:
> Nurung Schlise Projekt Erstellt' Abrichnurgsstute
> Rxanbtgrmrung
> Ausgabon
> :Abretchnung
> . Prolokolle Lnd Dslasett:
> K royooidsbunapuy
> Sie konnen itre APl Schhlsse hler nlcht finden?:
> :Coogit AL mudo ilapurett tuider. imporltltn slt thdte Pld'tit, In dHtts Lte wer don nut APtSchtbsce tor Profetut srgazeg, dle h' Ohae ehnn rhvin APi-Schplit eruteote. Wedhre kfomtonn Cn dit Zgthox LhTschlaLe ne tnteterL Sle torrh auch.
> Prafeita hmporteren
> Q' Sosrch"
> :e Ger Api key 'o whal's new
> o Settngt

![[assets/dense-slides/cVzf49yg0D8/slide-002.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-002.html)
- AI slide classifier: `title_card` confidence `0.99`
- Text source: agent_vision.

Slide text:

> One API to Rule Them All
> Building Agents with the Gemini Interactions API, from zero to a working agentic application in 60 minutes.
> 60 min · Live Coding · Philipp Schmid

![[assets/dense-slides/cVzf49yg0D8/slide-003.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-003.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Multi-panel slide with small code snippets and dense text; OCR is better suited than manual transcription.

Slide text:

> ? Part 1: The tnterections APl1 Core Primitives
> 9
> ®
> C Server-Side State Background Execution
> 12o clicnt.fnteroctions crcatc( orevious 2nteroction idi1.id mode1*gemini-3-flash-preview npuk= Follow up Question? 0 oclient fnteroctions.create( agento deep-research... bockgr ound:Iruo tnpuk= Roscarch topic.
> history. Chain turns with prevlous snteroction,ia. Server oums coriversation Fire-and-forget for lcng tasks. Pol with interoct lons.get(ia).
> Typed Output Blocks Streaming via SSE
> Flat arrby. teit, Iurt tlon_coll, Logo, thought. for O in interoction.outputs: motch o.type: Cuse text" @rint(o.text) coso Cfunction_coll: Rich events: content.delta, Interoctton.corptete. for chunk in cliont.finteroctions create( modee gemini-3-11ash..oo tnputr Helloo orint(chunk)
> 5717

![[assets/dense-slides/cVzf49yg0D8/slide-004.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-004.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Grid of tool cards with small text and code-like labels; OCR is suitable.

Slide text:

> Part 1: Tha hnteractiors AP1 Built-in Tools
> Q Google Search <> Code Execution URL Context
> (00ls=[[type" google seorch4)] tools=[ftype) "codo_cxecution")] (ools=[fcype Curl.context]
> Ground responses with real-time web results. Exocute Python code server-side in a sandbox. Fetch and read ful web page contenl
> Computer Use D File Search Remote MCP
> Browser Butomation via the APl. tools=[(type conputer use"}] Search uplosded files in RAG stores. tools=(ft ype" fi1e 6oorch- Cornect extema took via kCP protocol. tools=[f"type" https:/.. ] mcp-servorD
> Buh-ln toos execite server-aide, zero code needed. Mix with your onn funetion, tools freey.
> 6717

![[assets/dense-slides/cVzf49yg0D8/slide-005.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-005.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Two dense code panels with small text; OCR is appropriate.

Slide text:

> Part1:The Interactions API CodeComparison
> GENERATECONTENT INTERACTIONSAPI
> Stoteless:re-send history every turn Request1 r1-client.nodels.generate_content（ model-genini-3-flosh-preview" contents-[ ("role":"user" ("inline_doto”:（mime_type”: ("text*:"Describe this inoge) "porta":[ 'imoge/jpeg" "doto"：...")) i1-client.interoctions.creotec Request1 model-genini-3-flosh-preview* input-[ 0fou.:od.) ("typo":"text" （6od/5o.dou/:d.T,
> r2-client.nodels.generate_content( model-"gemini-3-flosh-preview" contents-[ ]:s1odosn.oo.) eot 2:MUST reend imoge ond nistory ("inline_dato”:（"mime_type”:"imoge/jpeg” "doto：...")) i2-client.interoctions.creote（ Request 2:Just.send npw input model-genini-3-flash-preview input-'Is there ony text?" previous_interaction_id-i1.id
> ["role":"model" ("role":"user" （ （[（2x）Au0o4sI.x.）]:10d （[（oo1do..x.）]1o
> Access:response.condidates[e] content.ports[e].function_col]
> 8/17

![[assets/dense-slides/cVzf49yg0D8/slide-006.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-006.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: agent_vision.

Slide text:

> Using the API: Basic Chat
> STATEFUL MULTI-TURN
> Create an interaction with a prompt
> Chain turns with previous_interaction_id
> Zero history: server manages all state

![[assets/dense-slides/cVzf49yg0D8/slide-007.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-007.html)
- AI slide classifier: `content_slide` confidence `0.99`
- Text source: advanced OCR `rapidocr-live/border-trim/opencv-adaptive`.
- OCR decision: ready — Dense code/editor screenshot with small text and UI chrome; OCR is more suitable than manual transcription.

Slide text:

> main.py x In Watthrcugh. Task tmpamentation Pliun 个日4 Crealing Agent Clats Structure x...@+
> workshop > d mnin.gy 49 37 EE write_fite_schew = { "phraooters":! "required- I"tile_path-, rcontents"l.. Noxt wo noed to odd a read_fbo and write_ fe tool.: Create a basic python kuolenentatlon and also the Fon tchems defition and map for the key: function, schems
> 59 51 52 53 55 56 58 60 62 64 65 66 67 69 70 71 72 74 75 76 57 61 63 77 8 3. Reo istry sapping tool naaes to functlons sed scheras tootsap = { class Agent: derrnaoo. det.run(selt, input_text:,str Illst) - str: "read_file"1. ("functlon"r resd_fite, "schea": resd_file_schea),: def _lnlt_iself, model_id: str i "gemini-3-flash-previtr. toots: dlct = Hon "urlte_file": ("function": vritc_fite,. -schees-i urite_file_schca),: 1. Prepore tools for the APl call' toot detinitions = [tt"schema-] for t in selt.toots.values()] if setf.toot Initinlizes the Agent vith o Geinl clieit, mooe v.twsniu-interetl self. toots.n tools or ( procesesnInputotrung neretonyihepobeire ponse7 untinirgcg Processes: on lnput, and rtturns tht model's.respoase, handling tool.,calts. se?t.client. genal.cllent() self.prtvious_lnteraction_id + None: self.sodel_id = nodel_1d' lnteraction rodelaso. Acctp! Chsrge xt a↑.x ↓: 0x0d Acotpt t?: Includas tho Pyhon irplemantotlona, JsON schemus, sind" Edhed 1 to v updsting the sgent's interaction ioop to hande tool calls.: t here created an Implemertation plan to sdd tha' Ask anything, e to minilon, I Ior worktiovs Gesd flle and Mrite tite toos to ine Agent. This. +. A Paving A Gemn S Flenh: ' Thought for 4s:: Anatyzod solution Edlted Implementation Plan - Anthyzed & sgent py nlt-i31.: schemu., Iirptamentatlons, the JSON scheru detindtions, and a map to connect each. toor's key to its functon snid. 1've got o sotd python examole n Defining New Yools. Hrp'ament resd_fite, and Write_fite: tools within arkshop/aain py., rm working on the Python Sotut fon/aaent.py, to oude mo. The tuask is to'.
> @ 邮 Ln 34; Col 10 (22 tolhcted}3 Spco1; 4 年 UTF-8 & LF $: {) Python 3.12.12 (ronr': venw) 甲 S+lect Python Intefprotor, Anugrrylty: Setng+ 高':

![[assets/dense-slides/cVzf49yg0D8/slide-008.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-008.html)
- AI slide classifier: `content_slide` confidence `0.95`
- Text source: advanced OCR `rapidocr-live/bright-screen/opencv-adaptive`.
- OCR decision: ready — Product UI screenshot with many small labels and embedded media panes; OCR can capture it more reliably.

Slide text:

> Google Al Studio:v: EPlayground
> puno6d 3
> x Bula. >
> @ Dnshboard
> : Documonbaton:. >:
> 田
> Volco
> : 0:00 / 0:08 xond
> W'hat do you think of rry out'h? Media resolulon 258 tokens/ wmage
> HDGY Thinvng kere!
> 0:00 / 0:09 BuuI 0N
> *.
> Wal now, you'ro lookin' vary smart so you arot That greon acket su'ts you woa, I must say. A grand casual look. Y'ere you th'nkin' of hesdin' out somewhere? Sesron Cortut
> Q Searth O vhat's naw. O Coogt L noot itry mule mhLhui, to douchtchdk cutput. Sream Is ive Dtrannta Yools Furction catng Ean.
> o Get APi koy QSrtingi thorsten.schaefeo...:Start typlng I prompt 丨：B Toous Grounding with Googte Search Automatc Function Rosponse

![[assets/dense-slides/cVzf49yg0D8/slide-009.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-009.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: advanced OCR `rapidocr-live/border-trim/opencv-adaptive`.
- OCR decision: ready — UI demo slide with small interface text and captions; OCR is appropriate for the dense screenshot content.

Slide text:

> Gemini Live APl Demo 'Corrcttd
> what this APl can do. Why not try out some fun features, Bke: Top o' the mornirg to yal fm GeminI Live, a Ettle dermo of? snother language? What do ya think?. heorin' mo speak Iin ditferent sccents, or see H I can chat in.:......
> Start camera to send video
> stog AY- *+.+F* Sart Camoo. Sh.re screen tcorract Type a mesisge... Bond:
> Live Caprion Top ot the Marto To, I'm Cemin ufe. O itlle damo o!

![[assets/dense-slides/cVzf49yg0D8/slide-010.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-010.html)
- AI slide classifier: `content_slide` confidence `0.96`
- Text source: agent_vision.
- OCR decision: ready — Chat/demo UI screenshot with multiple language bubbles and small controls; OCR will be more accurate than manual transcription here.

Slide text:

> Gemini Live API Demo

![[assets/dense-slides/cVzf49yg0D8/slide-011.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-011.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: advanced OCR `rapidocr-live/full`.
- OCR decision: ready — Dense configuration UI and console output with small text; OCR is the right capture method.

Slide text:

> RLO
> Connection wilbe established directly to the Gemini API Voice: API Configuration Connection Settings using an ephemeral token from the backend. ModelID: gemini-3.1-flash-live-p Gemini Behavior System Instructions: You are a helpful assistant.Be concise and friendly. Puck(Default Temperature:1.0 Microphone: Camera: Chat MediaStreaming Default Microphone %08 Default Camera StartVideo Share Screen StartAudio (（) loded gsiLipi.j displayer initalied SETP COLETE Servsce UR (vlalphal： lE/generatiyelan CreatedCeniai Line APIobjecti 3477155A vehseciet spesi getFunctionbefinitianscalled Geogle Grending enabled,removing cstoe Setup corplete: necting directly tei ratirie? le5/ /24565112645868722644 et（-） fncti alls if y. " rativelar ralivni odets/ge.xla.ta_tahe ai-d.l-flab-le-peie', ：ath./14565f Detault lev oeiniLeeJs437 AL.J31287 5/1424515 pesiniliet.is1315 stiat.tt:257
> Controls randomess（0.0-2.0].Highermore creative/diverse,Lower more predictable/focused Enable Google grounding（Enabling Google grounding will disable custom tools) Connect toGemini to startchatting SYSTEM:Ready!
> CustomTools
> Transcription Settings
> Activity Detection Setings
> Connect Disconnect
> Connected
> Setup Message JSON(raw config sent to Gemini API)
> Type a message. Send

![[assets/dense-slides/cVzf49yg0D8/slide-012.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-012.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.
- OCR decision: ready — Dense configuration UI plus devtools/network output and chat transcript; OCR is appropriate.

Slide text:

> API Configuration
> Media Streaming

![[assets/dense-slides/cVzf49yg0D8/slide-013.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-013.html)
- AI slide classifier: `content_slide` confidence `0.98`
- Text source: agent_vision.

Slide text:

> google-gemini/gemini-live-api-examples
> Gemini Live provides multimodal realtime agent capabilities. Build voice agents that can process vision and text in realtime.

![[assets/dense-slides/cVzf49yg0D8/slide-014.jpg]]

- Recreated text/layout view: [open HTML recreation](/assets/slide-recreations/dense/cVzf49yg0D8/slide-014.html)
- AI slide classifier: `content_slide` confidence `0.89`
- Text source: advanced OCR `rapidocr-live/border-trim/opencv-adaptive`.
- OCR decision: ready — Browser/UI screenshot with smaller embedded text is better suited to OCR than manual transcription.

Slide text:

> Google The Keyvord Bula reaTtre conrueora aoena wrh Gtmin Lll Pmn Lv
> Utng th+ GtTil L+ AP, Soich nou trhcites ht Ltnt to vb+ dttgy +ath trr voice. ha sgont Cin'het' de Carvt
> tnd ititcta torttnt nd ghe dngn csnomtr, bolu veretint tna cit.
> 。
> Build with an expanding ecosystem of
> blog google uses cocdes from Google to derrer ard enhanct lhe quairty of ite sermces and to analyze tratic. Leam,more:-+AM-+iAn. OKOOtR

Classification audit: `raw/sources/slide-ai-classification/dense/cVzf49yg0D8/audit.json`
