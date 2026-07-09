---
title: "Slides: Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter"
category: "slides"
video_id: "84Vtz2IL1Ug"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter

## Source Video
[Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter](https://www.youtube.com/watch?v=84Vtz2IL1Ug)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/84Vtz2IL1Ug/slide-001.jpg]]

OCR text:

> aWS
> 
> eee)
> @®Graphite WW Windsurf 4 MoneobB
> Mdaily £3 augment code WorkOS

![[assets/slides/84Vtz2IL1Ug/slide-002.jpg]]

OCR text:

> vee ere Inference may be the largest market ever in software
> ee K
> Weltn? Vo1
> ve
> 
> mney i a
> 
> iN
> 
> IN
> 
> Avice ALEX ATALLAH < OpenRouter

![[assets/slides/84Vtz2IL1Ug/slide-003.jpg]]

OCR text:

> January,2023:Moderation
> r/ChatGPT.2yr.ago
> Noobrage2112
> OpenAlBanningaccounts.
> Gone Wild
> Hithere,
> After a thoroughinvestigation,we have determined thatyou oramemberofyourorganization are usingthe
> OpenAl APlinways thatviolate ourpolicies.
> Dueto thisbreach we arehalting accessto theAPlimmediately for theorganizationPersonal.Commonreasons
> forbreachincludeviolationsofourcontentpolicy,repeated attemptsatdisallowed use-cases,oraccessing the
> API from anunsupported location.Youmay also wish toreviewourTermsof Use.
> appealswithin onebusiness day andwillcontactyou ifwereinstateaccess to theAPl.
> Best,
> TheOpenAl team
> That was theE-mail lreceivedjusta couple of minutesearlier.
> It seemsOpenAl doesnotappreciate people usingit'sprogramforD&D/ Textbased/Roleplaying/Fictional based
> adventuregames thatmight entail formsofViolence/Gore/Fantasy/Erotic/Fictionalgameplay.
> Ihadjustpurchased anaccountfortheBetaPlayground andshortly afterI wasremoved.I'mnotgoing to be
> supporting OpenAl anymore after this action.I don't appreciate the weights and aggression theyhave placed on
> thefilterprecautions,andIfeel thisishighlyunfair.

![[assets/slides/84Vtz2IL1Ug/slide-004.jpg]]

OCR text:

> World'sFair AIEnginee January,2023:Moderation
> OpenAl Banning accounts. Noobrage2112 r/ChatGPT-2yr.ago
> orld's AEngin Hithere, OpenAl APlin ways that violate our policies. Gone Wid
> for breachncludevioltionsofourontenlicy,repeated attemptsatisallweducasesoraccessingthe APifromanunsuportedlocation.Youmayalsowishtoreview ourTermsof Use.
> Worl AII appeals within one business dayand will contactyouif wereinstateaccess to theAPi.
> The OpenAl team Best,
> That was the E-mailreceived just a couple of minutes earlier.
> orl A 1had just purchased an account for the Beta Playground and shortly after I was removed.I'mnot going to be supporting OpenAl anymore after this action.I don't appreciate the weights and aggression they have placed on adventure games thatmight entailforms of Violence/Gore/Fantasy/Erotic/Fictional gameplay the filter precautions, and I feel this is highly unfair. Itseems OpenAl does not appreciate people usingit's program for D&DyText based/ Roleplaying/Fictio
> World'sFair AEng Engineering thefuture ofAl

![[assets/slides/84Vtz2IL1Ug/slide-005.jpg]]

OCR text:

> World'sFair AIEnginee February,2023:OpenSourceracebegins...
> [D]ListofLargeLanguageModelstoplaywith. r/MachineLearning-2yr.ago sinavski
> orld'sFair AlEng a the landscape sinceIhaven't worked in thisfieldbefore.I'm trying torun them“from the largest to the smallest" Discussion
> By“relatively easy”,Imean doesn'trequire to setup aGPU cluster or costsmore than$20:)
> gm AI Here are someexamplesIhave foundso far: 2.QpenAlaoi to access GPT-3s(from ada (0.5B) to davinci(175B)).Also CodeX ChatGPT (obviously)-175Bparams
> orld'sF AlEngk 4.OPT-175B（FacebookLLM),the hostingworks surprisingly fast,but slower than ChatGPT 5.Several modelsonHuggingFace thatlmade torunwith ColabPro subscription:GPT-NeoX20B,Elan-t5-xxl Hugging faceAPl interfaces/spaces didn't workforme:(.Here is anexample notebookImade forNeox. 11B,Xlm-roberta-xxl10.7B,GPT-j6B.1spent about$20 totalonrunning themodelsbelow.Noneof the
> World'sFair AIEng Engineering the future of Al

![[assets/slides/84Vtz2IL1Ug/slide-006.jpg]]

OCR text:

> Cee: errs
> ed fy Ratt Raz et Ory) renee i MT ft Te ee a
> ea iia g Micros Viords Faw
> elk) iE: ~
> ue [ccc eee ocr ee en ae
> a a
> Peer ICI) yO an ao (cd
> Neod| rere. _ i: Tee oa
> i |
> —— Sree nrnen e
> rr mid Paces Riad io j - = an
> See eel a 2 7
> Fr i

![[assets/slides/84Vtz2IL1Ug/slide-007.jpg]]

OCR text:

> February, 2023: ... and Llama wins, almost
> LLaMA: Open and Efficient Foundation Language Models
> Hugo Touvron; Thibaut Lavril; Gautier Izacard; Xavier Martinet
> Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozitre, Naman Goyal
> Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin
> Edouard Grave; Guillaume Lample*
> Meta Al
> 
> Abstract performance, a smaller one trained longer will
> Wei ' ultimately be cheaper at inference. For instance,
> we introduce LLaMA. arcollection of founda- although Hoffmann et al. (2022) recommends
> tion language models ranging from 7B to 65B -
> parameters. We train our models on trillions training a 10B model on 200B tokens, we find
> of tokens, and show that it is possible to train that the performance of a 7B model continues to
> state-of-the-art models using publicly avail- improve even after IT tokens.
> able datasets exclusively, without resorting
> to proprietary and inaccessible datasets. Ip The focus of this work is to train a series of
> pesticular, LLaMA-13B outperforms GPT-3 language models that achieve the best possible per-
> (1758) on most benchmerks, and LLaMA- formance at various inference budgets, by training
> 65B is competitive with the best models, on more tokens than what is typically used. The
> Chinchilla-70B and Pal.M-540B. We release resulting fels, called LLaMA, ranges from 7B
> all our models to the research communily’. . we
> 
> to 65B parameters with compctitive performance

![[assets/slides/84Vtz2IL1Ug/slide-008.jpg]]

OCR text:

> enn February, 2023: .. and Llama wins, almost
> World's Fair
> LLaMA: Open and Efficient Foundation Language Models
> aws Hugo Touvron; Thibeut Lavril; Gautier Izacard; Xavier Martinet
> el Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozitre, Naman Goyal
> Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin
> 4 Edouard Grave; Guillaume Lample"
> ; Meta Al
> Tent as A Abstract performance, a smaller one wained longer will
> , , _ ultimately be cheaper at inference. For instance,
> We introduce Ls MA. « collection of founda: although Hoffmann et al. (2022) recommends
> 5 bon language models ranging from 7B to 6$B - ep
> , ; parameters. We train cur models oa tnitions training a 10B model on 2008 tokens, we find
> a of tokens, and show that it ts powsble to train that the performance of a 7B modet continues to
> ntl Masc-of-the-an models using publicly avail- improve even after IT tokens.
> able datasets caclusively, without resorting
> ‘au to propnetasy and inaccessible datasets fe The focus of this work is to train a series of
> ba) particular, LLaMA-138 outperforms GPT-3 language models that achieve the best possible per-
> (1758) om most benchmarks, and LLaMA- formance at various inference budgets, by training
> “ compas ee rapes on more tokens than what is typically used. The
> inchalla- LM-S40B. We release
> all ous models to the research community |. resulting models, called ee from 7B
> AlEngmoce > é
> ‘ a
> Tet Engineering the future of Al

![[assets/slides/84Vtz2IL1Ug/slide-009.jpg]]

OCR text:

> World'sFair AIEngin March,2023:Thefirstdistillationsuccess
> Alpaca:AStrong.ReplicableInstruction-FollowingModel
> VS Authors: Rohan Taori and Tianyi Zhangand Yann Duboisand Xuechen Tatsunori B.Hashimoto
> Wetroduce Apac 7Ba moder fine-tuned fro Ie LLaMA78modef n52K dsuqd (6o0S).Ceckout our code release ont
> Update:Thepubilicdemoisnow disabiedThe origin mostiyachieved nisgoaandgiventhe hosting wedecided tobring cownthedemo rch in an accessible way. We foe/ thit we nave
> 4j Stanford Alpaca
> Overview
> World'sFair AEn Microsoft

![[assets/slides/84Vtz2IL1Ug/slide-010.jpg]]

OCR text:

> April, 2023: Window.ai and BYOM (bring your own model)
> window.ai ,
> Use your own Al models on the web oa
> ; . =
> a Pry

![[assets/slides/84Vtz2IL1Ug/slide-011.jpg]]

OCR text:

> World'sFair AIEnginee May,2023:0penRouter
> aws Betterprices,betteruptime,nosubscripton. InterfaceForLLMs TheUnified Featured Models Gemini 2.5ProPreview 6c06 215.0B Tokens/ek 2.4s +7.02%
> Fair Starta message uadofa GPT-4.1 49.1B 815ms +4.23%
> ClaudeSonnet4
> 04j 242.8B 1.7s +47.29%
> World'sFair AEng Microsoft aws smolo

![[assets/slides/84Vtz2IL1Ug/slide-012.jpg]]

OCR text:

> LLMRankings
> Comparemodelsforall prompts
> AllCategories
> Programming
> Roleplay
> Marketing
> Marketing/Seo
> Technology
> Science
> Translation
> Finance
> Health
> Trivia
> Academia
> 2.6T
> 1.95T
> 10to100%growth
> MoMforthelast2y
> Mar17
> Leaderboard
> Token usage across models
> Top thisweek
> OpenAl:GPT-40-mini>
> 443Btokens
> GPT-4o mnis OpenA's newest model after [GPT-4 Omn]models
> Google:Gemini 2.0Flash>
> 239B tokens
> Anthropic:ClaudeSonnet4>
> 207Btokens
> Claude Sonnet 4 signiicanty enhances the ca
> Google:Gemini 2.5ProPreview>
> 183B tokens
> Gemni 2.5 Prois Googe's state-of-the-art Ai model des

![[assets/slides/84Vtz2IL1Ug/slide-013.jpg]]

OCR text:

> Themostmodels,providers,andtokens
> 8.4T
> 2.5M+
> MonthlyTokens
> Global Users
> Active Providers
> Models
> Signup
> Buycredits
> GetyourAPlkey
> Create anaccount toget started.You
> Creditscanbeused withanymodel or
> Create anAPIkeyand startmaking
> can setupanorgforyourteamlater.
> provider.
> requests.FullyOpenAlcompatible.
> OPENROUTER_APILKEY
> Apr1
> Mar30

![[assets/slides/84Vtz2IL1Ug/slide-014.jpg]]

OCR text:

> World'sFair AIEngine Anthropic:Claude3.7Sonnet antzop1c/elaude-3.7-sonet0 Chat
> Fair aws Overview Providers Versions Apps Activity Uptime API
> Closed-sourcemodels didn'tkeepupwith Uptime statsforClaude3.7Sonnet Uptie satsfor Claude 3.7 Sonet ac
> 'sFair demand...
> Fair neo4j
> on
> World'sFair Engineering the future of Al

![[assets/slides/84Vtz2IL1Ug/slide-015.jpg]]

OCR text:

> YourActivity
> Seehowyou've beenusing modelsonOpenRouter.Privacy
> Spend
> Tokens
> Requests
> Last
> Last
> Lastday 499
> Lastwek4.35K
> Last day3
> Lastwk12
> day
> From:
> To:
> Filters
> Export
> Timestamp
> Provider/Model
> App
> Tokens
> Cost
> Speed
> Finish
> O
> Jun3,10:11PM
> Claude 3.7.Sonnet
> OpenRouter:Chatroom
> 79.0tps
> stop
> Jun3,10:11PM
> Claude37.Soonet
> OpenRouter:Chatroom
> s
> 66.0tps
> stop
> Jun3,10:11PM
> Claude.3.7Sonnet
> OpenRouter:Chatroom
> s69
> stop

![[assets/slides/84Vtz2IL1Ug/slide-016.jpg]]

OCR text:

> World'sFair AIEngineer Will intelligencebewinner-take-all?
> TokenMarketsharebyModelAuthor
> WS 100% une1.2025 OpenRouter
> 34.6%
> 22.9%
> shropic 16.7%
> ode %09 meta-llama 14.7% 3.9%
> 2.8%
> 30% 1.5% 1.3%
> 04j 0.7% 0.5%
> 0% Jun2,2024 Jut21 Sep8 Oct27 Dec15 Feb 2 Mar 23 May 11 Total ousresearch 100.0% 0.4%
> H'eFair
> World'sFair AIEn Microsoft aws smolo

![[assets/slides/84Vtz2IL1Ug/slide-017.jpg]]

OCR text:

> World's Fair
> elere dime ol hem anele Lacs
> ; ees
> —?
> Making an
> increasingly
> a heterogeneous
> J ,
> mS <" ecosystem
> B homogeneous
> nro!)
> N
> ~~ coed
> Ce here
> World's Fair MTV Iacetvo 1 Cade ES 19900

![[assets/slides/84Vtz2IL1Ug/slide-018.jpg]]

OCR text:

> INT erated WS AlEngincer
> xe) it | rita | ey 2, WV vilekw alle |
> we A
> 7 1 ;
> ma WorkoO: 7 - & tambo
> Ba ad eal ome " Ps Sd
> ust | eval Rd rl | 7 fers] | tae Rl |
> Ne
> ~ | hacatean  < Wo” fekair| DISTRIBUTIONAL]

![[assets/slides/84Vtz2IL1Ug/slide-019.jpg]]

OCR text:

> rosoft World'sFair AlEngineer aws World'sFair AIlEngineer
> sFair Work AIEngineer ld'sFair tambo
> trust World's Fair AIEngineer neo4j World'sFair AIEngineer
> AIEngineer

![[assets/slides/84Vtz2IL1Ug/slide-020.jpg]]

OCR text:

> oo a ay cr ee / - rd
> en
> Ls
> Technical challenge: a ne
> Ih Arcee Tue Ue ete ; ; ,
> [Peres Te ree ~, Porraan fa a ron
> ee ~ oo |:

![[assets/slides/84Vtz2IL1Ug/slide-021.jpg]]

OCR text:

> We built a middleware for inference called “Plugins”
> aa ee ee cieistal Cerone at
> complete
> [cco [01 oo-0 Gaal or>)0 111 Stak rN Co
> i eer oe een
> 2 gh I Pal Comer O Lae ar Cores Bee
> .1isDisabled
> next.complete(requestFragment);
> foe Oe AL i es wae at o2 010 i 0G ol tole
> lisMessagesInput(te:.ecues!) |]
> Pie Zeno] a he Fara 0X0 Rear =o 000 Np cit aoe cea gE |

![[assets/slides/84Vtz2IL1Ug/slide-022.jpg]]

OCR text:

> Unlike MCPs, plugins allow transformations
> on both inputs and outputs
> , (cena
> oe 5 an = addAnnotationsToOutput (
> folvnaslehan aan
> annotations: .fcachedAnnotations,
> );
> oka 2 at
> peek tel aa ee elie ees Fi Proll ae
> . mont ars tT at 1 (rt a a8 acerca mele
> peyote ere meen a ead F

![[assets/slides/84Vtz2IL1Ug/slide-023.jpg]]

OCR text:

> World's Fair
> WELCOME
> TO THE TEAM
> BS Robert .
> ne, ; 1 J
> More modalities... eo
> q ; @ oy
> d OpenRouter
> _ 4
> Co 7 -
> "me Cate |
> [WortdsFair] Microsoft 2S aypai

![[assets/slides/84Vtz2IL1Ug/slide-024.jpg]]

OCR text:

> World'sFair AIEngine Bettermodeldiscoverability/routing. Betterpromptobservability.
> openai/gpt-4o-mini0
> Starting at $o.6O/M output tokens $0.217/K input imgs
> Technology（#1) Science（#1) Marketing/Seo (#6) Programming（#6) Translation(#6) +3categories
> GPT-4ominiisOpenAl'snewestmodel after GPT-4 Omni supporting both textand image inputs wit Asthelrmost acvanced smallmodelis.many Trivia(#9) Finance (#7) perthanGPT-3.5
> Academia(#10)
> Overview Providers Apps Activity Uptime API
> World'sFair AEnc Engineering the future of Al

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
