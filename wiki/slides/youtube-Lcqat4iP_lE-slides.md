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

> Graphite Microsoft d'sFair aw
> Vorld'sFair AlEngineer World'sF AlEngineer World's NEngin
> World'sFair AlEngineer
> xpander.ai PRESENTEDBY Microsoft ec

![[assets/slides/Lcqat4iP_lE/slide-004.jpg]]

OCR text:

> AIE
> MCPsareblackboxes
> *forobservability
> aphite Worir oft Word'sFair aws
> fsFair ander.ai WordsFar Moasot Word'sFair se04j Microsoft aws smol?

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

> Fiterbyopnan
> run_client In31s Inputs 小色
> MCPClient.connect_to_server Path
> MCPClient.interactive_sess.. self <mcp.client.session.ClientSession object at 0x12a45a1c28d0>
> AIE MCPClient.cal_tool VMCPClient.call_ool add calculate_bmi arguments name weighukg ClientTraces 70
> MCPClient.demo_all_tools MCPClient.call_tool D height_m W&BWeave-MCPClient/Server 1.75
> MCPClient.call_tool MCPClient.call_tool add calculate_bmi Output Path content supportwith@weave.op 小
> MCPClient.call_tool create_thumbnail MCPtool calls text 42858
> orld'sFair ellum Wo g://app isError annotations nut1 false Docs:wandb.me/mcpop
> Fair Microsoft aws smol?

![[assets/slides/Lcqat4iP_lE/slide-007.jpg]]

OCR text:

> https:/lobservable.tools
> ObservableTools
> AIE Let'smakeMCPolstanspanent and observabl
> AVAVAFRI
> SEET SEE ERR
> 'orld'sFair m Wo
> Microsoft aws smol?

![[assets/slides/Lcqat4iP_lE/slide-008.jpg]]

OCR text:

> OpenTelemetry - primitives
> Traces
> AIE POST/api/checkout
> getcarto caleulateFraudlScore() performCheckout() renderJson)
> dlb-select cart... db-upclate cart...
> Microsot World'sFai
> Microsoft aws smol?

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
> AIE |mcp-agent-client 7chat.turn 7.60s
> 4chat.model_call
> mcp-agent-client 2.53s
> mcp-agent-client POST 2.13s
> |mcp-agent-client 2tool.fetch mcp-fetch-server fetch.operation 378.03ms 374.52ms
> >2chat.model_call
> -client 5.07s
> Norld'sFair daily Wo Mi
> SFNTDV Work
> World'sFair PHUNTIST Microsoft W brair Microsoft aws smol?

![[assets/slides/Lcqat4iP_lE/slide-012.jpg]]

OCR text:

> SameDomains
> |mcp-agent-client 15chat.turn 22.53s
> AIE |mcp-agent-cllent 6chat.modeLcall 2.49s
> POST
> mcp-agent-client 2.05s
> |mcp-agent-client 4tool.fetch 401.04ms
> mcp-fetch-server 3fetch.operation 397.04ms
> fetch.http_request mcp-fetch-server 363.21ms
> fetch.markdown_conversion mcp-fetch-server 32.90ms
> Microsoft orld'sFair -agent-cllent chat.model_call 3.00s
> World's AEngrer Microsoft aws smol?

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

> param usingOTELand_meta ObservableMcPToOLS MCPCLIENTTRACES
> AIE
> MCPSERVERTRACES
> Vorld'sFair Graphite World'sFair Mi
> Weights Vorid
> World'sFair Microsoft Word'sFa brain Microsoft aws smol?

![[assets/slides/Lcqat4iP_lE/slide-016.jpg]]

OCR text:

> WeaveOTel exampleaswell
> AIE.local.env.example
> #OpenTelemetry endpoint （optional, defaults to http://locaLhost:4318) OTLP_ENDPoINT=https://trace.wandb.ai/oteL/v1/traces
> #Weights & Biases API Key for Weave tracing （optionaL） #Get your API key from:https://wandb.ai/authorize
> WANDB_API_KEY=
> #W&B project in format "entity/project"（e.g.,"myteam/myproject") WANDB_PRoJECT_ID=your_entity/your_project
> lorld'sFair raphite World'sFair Mic
> Weights baz
> Worid'sFair Microsoft Word'sFair rain Microsoft aws 5 smol?

![[assets/slides/Lcqat4iP_lE/slide-017.jpg]]

OCR text:

> withOpus4&Windsurf MagicMcPmoment
> AIE
> sFair.um Word'sFair Microsc
> SENTR Norld'sFai
> World'sFair Microsoft World'sFair braintrus Microsoft aws smol?

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

> Magic MCP moment Ican see the attributes are being set with inguts.and outputs.
> withOpus4&Windsurf level nputs and output fieldsin Weave.Thismight be because Weave expects a specific format.Let me check the Weave documentation again for the exactformat:
> MCPToolwandb/query_wandb_support_bot
> AIE sent toWeave and then checkif the inputs/outputsare now properly mapped: Great!The testisworking.Letmewaita moment for the tracestobe Ran with these arguments:
> Ran terminalcommand
> //mcp-otelSsleep10 Auto-run Output
> MCPTool:wandb/query_weave_traces_tool "sources":[ "https://github.com/wandb/weave/tree/naster/weave-js
> the attributes are being properly set by looking at the fulltrace data: Inotice that the inputs and output fields are stillempty.Letme check if
> sFair lum Worid'sFair licroscments: db/query_weave_traces_tool Ah! The support botindicates that Weave expects wondb.inputs.and the code touse the correctprefixes: wondb.outputs.prefixes,notjust inputs.and outputs..Letme update
> SENTRY
> World'sFair Microsoft World'sFair trus Microsoft aws smol?

![[assets/slides/Lcqat4iP_lE/slide-020.jpg]]

OCR text:

> mcp.run - Profiles & Tasks
> Example:A"WorkAssistant”Profile
> AIE Cursor,Claude Desktog.Winds urforyourownAlageet canalmanage GiHubissuessend Slack messagesand update Notion pages-allthrough Slack+ your one proliel Noton WorkAssistant
> Inbound LeadRouter
> 2/13/202510:31:25AM
> Instructions Settings Triggers
> Editor
> This nev contact just submitted their information through our web form,indicating interest in
> assign this lead contact to soneone on our tean,please analyze the contact with the goal of
> other indicators.
> Mic World'sFair Here*s what I suggest doing1 New contact submission: (（firstNase）{（lastNane））<（（email}）>
> Microsoft aws smol?

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
