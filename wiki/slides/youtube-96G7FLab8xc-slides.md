---
title: "Slides: Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect"
category: "slides"
video_id: "96G7FLab8xc"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect

## Source Video
[Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](https://www.youtube.com/watch?v=96G7FLab8xc)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/96G7FLab8xc/slide-001.jpg]]

OCR text:

> Your MCP Server Is
> (and you should feel bad)
> Jeremiah Lowin
> Al Engineer Code Summit
> November 22. 2025
> PREFECT PLS eee)

![[assets/slides/96G7FLab8xc/slide-002.jpg]]

OCR text:

> S whoami
> 
> a Prefect Technologies
> 
> r Prefect, Marvin, FastMCP
> 
> | Slightly overwhelmed
> Rd 2025-11-22 13:14:39

![[assets/slides/96G7FLab8xc/slide-003.jpg]]

OCR text:

> I've seen of MCPs
> Daily Download Quantity of fastmcp package - Overall
> 30d 60d 90d 1200 all
> 
> 1,500,000
> 3 1,000,000
> 9 —® With_Mirrors
> = —@— Without_Mirrors
> °
> 3
> 500,000
> 0 PEPE USES S
> AD AD CV DAS AD ON DAD ND DAV AD DAD AV OO 4
> BEST NE V7 OLNEY PONT NE AV? OY OPN? AEA OPN? AP A! SO? SN
> SEH HH MN NP PPM MKK IP PMP MG OL Sy vyy
> Date
> Rd 2025-11-22 13:15:54

![[assets/slides/96G7FLab8xc/slide-004.jpg]]

OCR text:

> Objective:
> Bulld for agentic
> product design

![[assets/slides/96G7FLab8xc/slide-005.jpg]]

OCR text:

> “Ifa human can use an API.

![[assets/slides/96G7FLab8xc/slide-006.jpg]]

OCR text:

> Agents can find a
> needle in a haystack
> But only by examining
> everypiece ofhay

![[assets/slides/96G7FLab8xc/slide-007.jpg]]

OCR text:

> Product Intuition:
> How to the smallest
> effective surface area for
> autonomous users?

![[assets/slides/96G7FLab8xc/slide-008.jpg]]

OCR text:

> y
> in ; .
> H if
> 7 f
> _ ~s
> I
> y fan
> iin .
> 2025-11-22 13:22:59
> JFK 27-81.302

![[assets/slides/96G7FLab8xc/slide-009.jpg]]

OCR text:

> @ Saeed
> ‘ron fastmcp ane
> mcp = | ranean tre ere eee |
> “mep.tool
> ae ~ () > bool:
> a
> > 2025-11-22 13:23:49

![[assets/slides/96G7FLab8xc/slide-010.jpg]]

OCR text:

> Ng
> a
> i
> rn J 2025-11-22 13:24:39
> JFK 27-B1.302

![[assets/slides/96G7FLab8xc/slide-011.jpg]]

OCR text:

> x ele How to build secure and scalable
> 
> ee. ° as remote MCP servers
> DESIGNING oy] °°
> HIGH “ x
> QUALITY jo <2 AD
> MCPs ‘ °
> 
> _s xo |
> 
> #
> Bd 2025-11-22 13:25:54

![[assets/slides/96G7FLab8xc/slide-012.jpg]]

OCR text:

> e ee oserverpy
> 
> -mep.tool
> 
> tet Cemail: str} 2 dict: ...
> 
> mep.tool
> 
> a (user_id: str, query: dict) -% list: ...
> Nien neerene
> 
> Lee Corder_id: str) —- dict: ...
> 
> ‘ 2025-11-22 13:26:44

![[assets/slides/96G7FLab8xc/slide-013.jpg]]

OCR text:

> Step 1: Logic and Naming
> , Not operations
> ° 2025-11-22 13:27:59

![[assets/slides/96G7FLab8xc/slide-014.jpg]]

OCR text:

> , NOt operations
> The Trap V The Fix
> td e
> e One tool —- one agent story
> e Agent-as-glue e = =6Servernandies composition. not
> the agent
> t Mea t- 101] (mane) heme 10s] ROL Are 1101S)
> e Name tools for agents (verb +
> hasaeiaye)
> R) 2025-11-22 13:28:49

![[assets/slides/96G7FLab8xc/slide-015.jpg]]

OCR text:

> ;
> ,
> a)
> Hl
> el ]
> i 2025-11-22 13:31:44
> JFK 27-B1.302

![[assets/slides/96G7FLab8xc/slide-016.jpg]]

OCR text:

> ri Peer
> 
> A
> fab anKG) Literal
> 
> "icp.toel
> 
> bos 7 i
> email: str,
> include cancelled: bool a
> format: Literal! ;
> 
> a? one
> 
> ae 2025-11-22 13:34:14

![[assets/slides/96G7FLab8xc/slide-017.jpg]]

OCR text:

> server.py
> The"GoldenTool
> @mcp.tool（annotations={"readonlyHint":True})
> async def track_latest_order(
> email:str,
> include_cancelled:bool =False
> →str:
> Locates a user's Lastorder and returns status.
> Use when user asks“Where is my stuff?"
> Example:
> User:"Check bob@example.com"
> Call:track_latest_order(email="bob@example.com")

![[assets/slides/96G7FLab8xc/slide-018.jpg]]

OCR text:

> An average LLM context holds 200.000 tokens.
> That means ~250 tokens for each of your 800 endpoints.
> So if eacn tool's description was approximately as long as the
> text on this slide. then you would have taken up about 1/4 of
> the chent LLMs memory...
> just by saying .
> Nd 2025-11-22 13:42:09

![[assets/slides/96G7FLab8xc/slide-019.jpg]]

OCR text:

> yo.
> an
> ;
> a a
> : it yee eye EY TED
> JFK 27-81.302

![[assets/slides/96G7FLab8xc/slide-020.jpg]]

OCR text:

> Medium aS 1 Medium a '
> Building a Fivetran MCP Server: What | Learned Building MCP
> From Concept to 25+ Fivetran Tools Servers: Unifying My Entire Data
> (and beyond) Stack into a Single, Intelligent UI
> .— ~~. Diego
> Building a Fivetran MCP Server:
> From Concept to 25+ Fivetran MCP
> Tools (and beyond) es
> R 2025-11-22 13:50:29

![[assets/slides/96G7FLab8xc/slide-021.jpg]]

OCR text:

> converting REST APIs
> to MCP servers

![[assets/slides/96G7FLab8xc/slide-022.jpg]]

OCR text:

> Yes,
> 7 cf @ es
> noe tree Fal? commmrerety” Mosty Harmiess ee Ae
> FASTMC?P 3
> Openann tees
> neon ' Stop Converting Your REST
> OpenAP!. FastMCP ee APIs to MCP
> Caeriev att MAP ser very om any OpenaPl spececaton " Le % oe, ea 7 “ gh, ow
> Fae 8 Fo cae acetate Ate peri ate AT wat te oe ay op 4 . b Y
> ADEE AE wey A NBR Arar tet pene AOE cn me ME oo .
> phe a oa end ie enh onarany eva RATHER On wt fea ~, il
> coun wgeen | | ie
> ee a ar B
> Nd 2025-11-22 13:52:09

![[assets/slides/96G7FLab8xc/slide-023.jpg]]

OCR text:

> af :
> ; i
> f
> x
> iy fl By ‘
> / a
> Y i
> 7 7 / ~~
> _— am io an ,
> an ee
> %, a 2025-11-22 13:54:39
> ORES Ly)

![[assets/slides/96G7FLab8xc/slide-024.jpg]]

OCR text:

> "|
> 7
> ry |
> 
> os , i |
> 
> ae i] ~
> Me Pd
> 
> ne 2025-11-22 13:55:04
> JFK 27-81.302

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
