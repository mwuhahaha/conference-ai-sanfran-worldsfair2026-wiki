---
title: "Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso"
category: "slides"
video_id: "Lcqat4iP_lE"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso

## Source Video
[The State of MCP observability: Observable.tools — Alex Volkov and Benjamin Eckel, W&B and Dylibso](https://www.youtube.com/watch?v=Lcqat4iP_lE)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/Lcqat4iP_lE/slide-001.jpg]]

OCR text:

> INNOVATIONPARTNER
> aws
> PLATINUMSPONSORS
> Graphite
> WWindsurf
> MongoDB
> daily
> augment code
> WorkOs

![[assets/slides/Lcqat4iP_lE/slide-002.jpg]]

OCR text:

> NT ger ; aera
> eae CY a Ks eos
> Y Wwe
> "Y )
> , ar
> | Weights i a § baz
> | World's Fair |

![[assets/slides/Lcqat4iP_lE/slide-003.jpg]]

OCR text:

> ) Graphite > _ ra a MV Ce Celso) a asl aW
> 
> — ngoee —— _ S. — ae
> 
> ea \ See ae
> 
> wi K anion
> ae PE
> 
> eee AL Aes net

![[assets/slides/Lcqat4iP_lE/slide-004.jpg]]

OCR text:

> MCPs are black boxes*
> : "for observability
> ry » a a Prone
> es ern Doser Cas ES 000 OO

![[assets/slides/Lcqat4iP_lE/slide-005.jpg]]

OCR text:

> Why do we care about this
> ES * Both build tools that need MCP observability
> * Care about DevEx
> *« Bad developer and user experience is threat to adoption
> « CTOs/CISOs - Familiar observability is necessary for production
> reer EN Hacerseis
> INES) ree | nae
> wd Ceikes se) SE hk ES 600 OO

![[assets/slides/Lcqat4iP_lE/slide-006.jpg]]

OCR text:

> ‘Clientglraces)
> ct th em el LUA
> "support with @weave.op
> Pt)
> ere ae Co -« Docs: wandb.me/mcpop
> peat bs &: mMicrosoft OWS gral?

![[assets/slides/Lcqat4iP_lE/slide-007.jpg]]

OCR text:

> https://observable:to0|S _i
> Observable Tools
> \ a
> i | ee
> t Ce Hi na , , 5 iD
> TAM NTT
> a a Real We +
> | y
> aaa SS 1 (e110) | a ES O00 OO
> rere

![[assets/slides/Lcqat4iP_lE/slide-008.jpg]]

OCR text:

> OpentTelemetry - primitives
> Traces
> a Parente! 7 | | ear along | eager Stee , ee
> [ee | i
> _ ; , Si pehoaden
> a 7 NM iCecekse) ae
> | my aws 0
> . = Microsoft Simol
> 
> wd [ae | al <a ee ‘

![[assets/slides/Lcqat4iP_lE/slide-009.jpg]]

OCR text:

> OpentTelemetry - primitives
> Sink - Observability Platforms
> Fhoaracos WO %¢ clastic splunk > XQ Sentry
> a Nieree a penne
> we u Microsoft AWS ec
> ree | 2c 2 aw

![[assets/slides/Lcqat4iP_lE/slide-010.jpg]]

OCR text:

> Two Deployment Scenarios
> for MCP enabled agents
> ok Beers renee a
> \ |. . Po AV aS fai ]
> ne ee a Microsoft a> Ssimol

![[assets/slides/Lcqat4iP_lE/slide-011.jpg]]

OCR text:

> Different Domains
> | _ au
> reed oy er el
> a :
> i Semeey an cae on ec
> aed mT aws es
> en Pe Ble cecxe)at ES (nol

![[assets/slides/Lcqat4iP_lE/slide-012.jpg]]

OCR text:

> Same Domains
> | ane ——————————
> oiee 4 ao eal : 7
> E POST ;
> | Dikeoe
> tes fetch o
> . g + kine ———, chat mode.cal
> PA ete ho ame nt | a
> on
> Vi aws fs)
> Soa icrosoft
> ree ae a AWS mae)

![[assets/slides/Lcqat4iP_lE/slide-013.jpg]]

OCR text:

> Context Propagation
> recs cee: thas client es
> name tcovilee. nane
> arguments toallisr.argunents
> _neta {
> __traceContext {
> traceld spar Q).traceld
> spanId  spen ().spanid
> traceFlags span ().traceFlags
> be3. sik eee ee
> }
> iH
> Bae a });
> TAD LCe\*) CS
> LY
> ss w Microsoft @WS ary?
> a Saad all ad Pre Ya) [We wee)
> Beas 4

![[assets/slides/Lcqat4iP_lE/slide-014.jpg]]

OCR text:

> Acknowledge prior work
> « MCP Spec Github had several proposals and code examples
> ES * RFC #246 by Sam Spencer proposes contextPropagation
> « Justin from the Steering Committee suggested a community convention
> rather than integrating into spec
> * Openinference group started adapters
> rE iliuwccananeae yen #25 LA Te place where
> ee a Tee om
> (Ay panienonivaiany
> nealing ene a 5 Reo
> vero a
> me | ro |: A ©
> ‘awn aCe colon a Ssimol

![[assets/slides/Lcqat4iP_lE/slide-015.jpg]]

OCR text:

> Observable|MCPATOOLS
> usingJOTELandmmeta Pe |
> _ ,
> / MCEISERVERRACES
> reat om Biren en 0
> a |
> ee a
> De ha ae
> ccom wit’ ~—trom = Microsoft SWS aaa®

![[assets/slides/Lcqat4iP_lE/slide-016.jpg]]

OCR text:

> Weave OTel example as well
> a Reena eee. ae
> WANOB_API_KEY
> WANOB PROJECT _ID ,
> part ae a Pree ri
> fh
> cen A ew iG
> Sirah g
> ee 1100-00 OO

![[assets/slides/Lcqat4iP_lE/slide-017.jpg]]

OCR text:

> Magic MCP moment
> with Opus 4 & Windsurf
> “ an os . oe RNS! eer
> Tn ee EY [Tol goto SMES ero?

![[assets/slides/Lcqat4iP_lE/slide-018.jpg]]

OCR text:

> MagicMcPmoment
> withOpus4&Windsurf
> AIE
> Great! The test is working.Letme wait a moment for the traces to be
> sent to Weave and then checkif the inputs/outputs arenow properly
> mapped:
> Ranterminalcommand
> /mcp-otelSsleep10
> Auto-run
> MCPTool:wandb/query_weave_traces_tool
> orld'sFair
> um
> Wo
> Microsoft
> aws
> smol°
> Aladd'Eain

![[assets/slides/Lcqat4iP_lE/slide-019.jpg]]

OCR text:

> Magic MCP moment |
> with Opus 4 & Windsurf
> ae mera) etd a ticrose 7
> a ona ; a PSSA Riaa7 Pe
> ee a enV [ecesseyit eS Sinol

![[assets/slides/Lcqat4iP_lE/slide-020.jpg]]

OCR text:

> mcp.run - Profiles & Tasks
> Example: A “Work Assistant™ Profile
> , . 3 ed it = pad 4 rh eke abe
> a Nie ”. renee .
> on -
> _ : |. P4 Pa AV aSy at]
> Ce D1 as ES SOD

![[assets/slides/Lcqat4iP_lE/slide-021.jpg]]

OCR text:

> Recap & Call to action
> EG * MCP observability is possible today!
> * OTel to the rescue with contextPropagation
> * mcp.run will support OTel exports
> « W&B support both bespoke and via OTel
> ne ee Jaity ce ais
> \\
> yy . .
> aS hte h aad it nd Bee S , rns
> Sete eta g
> mY aws = semac®
> iia Pee LU L(ceto) 1 z

![[assets/slides/Lcqat4iP_lE/slide-022.jpg]]

OCR text:

> Call to Action
> Al Engineers:
> * Think about observability
> « Work on high level SDK adapters like Openinference
> * Work on conventions (genai semantic conventions)
> Platform Builders:
> * Add OTel support
> 1w RFCs
> coos - ery ule talk to us about your ideas about MCP observability
> Wl
> _* 7 | 4
> apatite’ <3 m Microsoft OWS a?
> Wiartielle Eaivr

![[assets/slides/Lcqat4iP_lE/slide-023.jpg]]

OCR text:

> mae / Alen ;
> orid'sFair|. - Mdaily [World *~ ::] am Mic
> eT |
> f | Se
> San a ore | rae
> Es a °° Lael
> | elite karl |
> PE caeons | Woit | brain

![[assets/slides/Lcqat4iP_lE/slide-024.jpg]]

OCR text:

> | eee aE
> eee ed ed
> ) H . - " . a | 0
> Reed . PN | World's Fair | _ > 3 Microsof
> “ ’ ie :
> 2 ae 3
> Vi ee of _ PP Ita ne aaa
> S SENTD vege TT Me Ae a SET d's Fair
> | World's Fair |
> aa ed Ne | ) ;
> Ld Microsoft | World's Fair | sintrust

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
