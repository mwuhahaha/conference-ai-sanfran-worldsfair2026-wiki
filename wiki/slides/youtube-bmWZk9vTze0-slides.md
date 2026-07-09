---
title: "Slides: MCP is all you need — Samuel Colvin, Pydantic"
category: "slides"
video_id: "bmWZk9vTze0"
sourceLabels: ["Public YouTube video frames", "Public YouTube metadata"]
---

# Slides: MCP is all you need — Samuel Colvin, Pydantic

## Source Video
[MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0)

## Relationship To World's Fair 2026
These slides are extracted from a public AI Engineer YouTube video connected to World's Fair 2026. Speaker-matched clips are supporting context unless later confirmed as exact session recordings; official livestream recordings are day-level/event-level source material.

## Related Scheduled Sessions
- No individual scheduled session mapping has been assigned yet; treat this as an event livestream deck.

## Extracted Slides
![[assets/slides/bmWZk9vTze0/slide-001.jpg]]

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

![[assets/slides/bmWZk9vTze0/slide-002.jpg]]

OCR text:

> aily Worle'- AlEngineer Graphite Wor
> d'sFair Wrld' Eair AlEngineer
> World's Fair AIEngineer
> ngbase PRESENTED BY Microsoft Wor

![[assets/slides/bmWZk9vTze0/slide-003.jpg]]

OCR text:

> stone an
> Recs Da iene a) i=) | Wo
> an
> oie Wot | | j |
> | World's Fair |

![[assets/slides/bmWZk9vTze0/slide-004.jpg]]

OCR text:

> what
> MCP is all you need
> Inspired by Jason Liu's talk*Pydantic is all you needand“Pydantic is still all you need*
> Same idea:that lots ofpeople are over complicating things
> AIE
> Same unrealistic title-no one is seriously claiming MCP can do everything
> What I an saying is:
> HCP can do a lot of multi-agent communications-specifically autonomous agents.
> World'sFair
> rite
> Wo
> Weights
> Microsoft
> aws
> smol?
> World'sFair

![[assets/slides/bmWZk9vTze0/slide-005.jpg]]

OCR text:

> 非 McP for multi-agent communication
> The way most people describe it:
> MCP
> tool
> AIE
> Agent
> tool
> tool
> World'sFair
> World:
> SEI
> Microsoft
> aws
> smol?
> World'sFair

![[assets/slides/bmWZk9vTze0/slide-006.jpg]]

OCR text:

> # sampling
> Give MCP servers the ability to make requests to LLMs via the client.
> （Powerfulfeature of McP,but not widely supported)
> AIE
> LLR
> RCPclient
> MCPserver
> LUNCall
> LLN tool call response
> toolcall
> saapling'createmessage*
> LURcall
> LLK text response
> sanpling response
> toolcall response
> RCPclient
> World'e
> daily
> Wor
> lndd'
> cair
> Microsoft
> aws
> smol?
> World'sFair

![[assets/slides/bmWZk9vTze0/slide-007.jpg]]

OCR text:

> meu MCP client MCP server
> LLM call
> a EEEEEEEEEEEUUEE EEE EEIEEEEEE EERE URE EERE NUE
> LLM tool call response
> tool call
> sampling "create message"
> scar EEE IETE EEE En
> LLM call
> Sa 4 —— eee
> LLM text response
> 4]
> sampling response
> tool call response
> ey ————— ——t

![[assets/slides/bmWZk9vTze0/slide-008.jpg]]

OCR text:

> # sampling
> Give MCP servers the ability to make requests to LLMs via the client.
> (Powerful feature of MCP,but not widely supported*)
> LLM
> MCPclient
> HCP server
> LLM call
> LLMtoolcallresponse
> toolcall
> sanpling*createmessage*
> LLM call
> LLN text response
> osuodsax Bugtdaes
> toolcallresponse
> LLM
> HCPclient
> MCP server

![[assets/slides/bmWZk9vTze0/slide-009.jpg]]

OCR text:

> G ledPrevee ft fii Selection ew Oo Widow Map Q &@ © Reet © m © A Qe wstan ics
> eo
> wo a ce oy mands)
> EP are (re a
> is an ee 2 Sat es a ae ea car
> vbr ts gee 5 ae Sey ge A ar mae
> Pe
> ae ee
> 2 sid ge agg eer tar eC eee ae ec ee eee
> eet ae ee
> rey
> B a on eer OP ae re one rca a a
> f 5 3
> 3G O&

![[assets/slides/bmWZk9vTze0/slide-010.jpg]]

OCR text:

> ited Proview! {te Cai) Seiscuan Wires ie Wires hae, Ce Ot Sm Gs matric
> ar
> PTs ory
> * eee ee ae ee eK re ee ee ee
> Cn es ata
> Been
> aoe a aes a | ae UG eee oem oo ae ki MEL OE
> ger * 9 hoe gel) “og a a Pa ee a eee en a ee sre a?
> et | Pe i a arr a ar ae
> on ee crea cc a
> ee ee ee en co
> % ; at F
> H 5 FI
> . _O& uw

![[assets/slides/bmWZk9vTze0/slide-011.jpg]]

OCR text:

> ZedPrevien Fle tdt Go
> README.md settings
> 118
> 120 121 119 122 123 async def run_query(ctx:RunContext[Deps],sql:str)→str: @pypi_agent.output_validator m=re.search（r ifm: remove sql.. \w*\n(.*?)...,,sql,flags=re.S)
> 124 sql=m.group（1).strip（)
> 125
> 126 logfire.info('running{sql}',sql=sql）
> 127 128 129 await ctx.deps.mcp_context.log（'info','runningquery') iff'from{table_name}'not in sql.lower(）: raise ModelRetry（f'Query must be against the{table_name?table')
> 132 130 131 try: rows=query_job.result（) query_job=client.query（sql)
> 133 except BadRequest as e:
> 134
> 135 136 await ctx.deps.mcp_context.log('info','query successful') raise ModelRetry（f'Invalid query:{e}')from e
> 1L

![[assets/slides/bmWZk9vTze0/slide-012.jpg]]

OCR text:

> G ledPrevwe ft fai Selection ew Oo Wridow Map Q @ © Rt © mw F A Qe wesaans sto
> oad
> es Peg t
> ates OCs eee MO LESSEE 0
> oa ara whe 4
> vA . i ore bre eae OR
> ors ee oy ,
> end Ca cone 5
> . peg et 2 btu. der.ig, ee) oe ees
> ert aan Fa Lear 5 7 7 A A , s
> al Se a er me ey a
> ee ene re 9g co *, 9 8 5
> wat Syl oe :
> ' im ; : a Ed
> aC a): oe,

![[assets/slides/bmWZk9vTze0/slide-013.jpg]]

OCR text:

> ZedPrevien Fle tdt
> README.md setings
> class Deps
> 124 123 125 ifm: sql=m.group（1).strip（）
> 126 logfire.info('running {sql}',sql=sql）
> 127 128 await ctx.deps.mcp_context.log（'info','runningquery') iff'from{table_name}'notin sql.lower(）:
> 129
> 132 130 131 133 134 135 try: except BadRequest as e: rows=query_job.result（) query_job=client.query(sql) await ctx.deps.mcp_context.log（'warning','query error retrying') raise ModelRetry（f'Invalid query:{e}')from e
> 136 await ctx.deps.mcp_context.log('info',‘query successful')
> 137 data=[dict（row) for row in rows] #type:ignore
> 138 return format_as_xml（data,item_tag='row',include_root_tag=False)
> 139
> 140
> 141 mcp=FastMCP（'PyPI query',log_level='WARNING'）
> 1L

![[assets/slides/bmWZk9vTze0/slide-014.jpg]]

OCR text:

> ZedPreview Fle Edt 四
> READMEmd setings
> pypi_ncp_setves.py 138 139 137 data=[dict（row）for row inrows]type:ignore return format_as_xml（data,item_tag='row',include_root_tag=False)
> 140
> 141 142 mcp =FastMCP（'PyPI query',log_level='WARNING'）
> 143
> 144 145 146 async def pypi_downloads(question:str,ctx:Context[ServerSession,None]) → str: @mcp.tool() aboutpackagedownloads."""
> 147 result=await pypi_agent.run(question,model=MCPSamplingModel（session=ctx.session),
> 148 deps=Deps(ctx)) return result.output
> 149
> 150 152 151 153 if_name #from devtoolsimport debug mcp.run() main
> 1L

![[assets/slides/bmWZk9vTze0/slide-015.jpg]]

OCR text:

> data=[dict（row)for row in rows]# type:ignore
> return format_as_xml（data,item_tag='row'.include_root_tag=False)
> mcp=FastMCP（'PyPI query',1og_level='WARNING'）
> AIE
> @mcp.tool()
> async def pypi_downloads(question:str,ctx:Context[ServerSession,None])→ str:
> ""Analyze downloads of packages from the Python package index PyPI to answer questions
> about package downloads."*"I
> result = await pypi_agent.run(question,model=McPSamplingModel（session=ctx.session),
> deps=Deps(ctx))
> return result.output
> if
> name
> main
> run()
> om devtoolsimport debug
> World's
> vellum
> W
> Microsoft
> aws
> Alndun
> Cal
> smol?
> World'sFair

![[assets/slides/bmWZk9vTze0/slide-016.jpg]]

OCR text:

> de-add_date()
> 2Bdefaddetiarhef'Today is{date.today():%Y-%m-%d}
> return f'Today is{date.today():%Y-%m-%d3
> AIE
> async def main():
> asyncwith libs_agent.run_mcp_servers():
> Samuel Colvin,6 houzs ago
> 33aSync def result（await libs_agent.run(How many times has pydantic been downloaded this year）
> asprintixesultpusputgent.run_mcp_servers(
> result= await libs_agent.run('How many times has pydantic been
> if
> naownlaadedathis:year')
> prindorteasyhtiooutput)
> asyncio.run（main())
> nama
> libs agent run
> MCP request:tools/list
> chat gpt-4o
> World's
> ThvellumgepydWichas been down1oaded 1,687,008,160
> 1L
> times
> this year
> Vdone
> Microsoft
> aws
> Cair
> smol"
> World'sFair
> 1L

![[assets/slides/bmWZk9vTze0/slide-017.jpg]]

OCR text:

> LS coveene: re, shas, irom rooms Demernarees <fonfere: 7am mm ee OSG me tanets
> oe me eee
> a ee fie : i
> a Coe ee ee ee ee ee ee F a oe
> “rie cer'] MCP request: initialize
> Sree] WRB Lads agent run cangang?s
> (8) RP request. initialize
> face oc} B20 tide agent tun
> iN] tT PCP request: tools/list
> MCP soreer handle request: toolaclist
> fre ay chat gpt-4o
> feet DHCP request. toolsslist
> SCP server Race request tools list
> ira aes} WD running 1 tool
> Se] BW curing tool. pypi_dvaniaads
> Cray ae GO mP request tools/call oypr downloads
> BB *CP server Nandle request: tools/call
> @? pyps agent rua
> QB chat aco sanoling
> Bl CP request: sampling’ crestemessege
> 2 BY MCP client handle request: sampling/createnessage
> foe eet] chat gnt-40
> turning SELECT COAMTI¢] AS sue _doeslosds FROM Digquery-public-data... project + ‘pydantic ANO EXTRACT YEA@ FROM tinestal
> Bigtvory JOD begis
> BigQwery getQreryPosults
> 2 P request toolsslist
> Megan — | 5 CP server haccile request’ tools/ist
> oe ah ie as) ons
> i
> /
> Pn el A
> i IN - c an al H . aws at
> es Mra sinol
> ents Ley | a)

![[assets/slides/bmWZk9vTze0/slide-018.jpg]]

OCR text:

> Thankyou
> AIE Slidesat I'm at the Pydantic booth，ifyou have any questions, com and say hi.
> World'sF- Graphite
> World'sFair AEno iadd~Eair Microsoft aws smol?

## Slide-Derived Subjects To Review
Subject extraction uses video title, related session titles/descriptions, transcript context, and OCR text when available. OCR is best-effort and should be reviewed against the embedded slide images.
