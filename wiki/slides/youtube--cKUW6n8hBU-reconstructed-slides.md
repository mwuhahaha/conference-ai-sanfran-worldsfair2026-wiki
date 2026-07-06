---
title: "Reconstructed Slides: DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners"
category: "slides"
video_id: "-cKUW6n8hBU"
sourceLabels: ["Cropped public YouTube video frames", "Local OpenCV slide-region detection", "Local RapidOCR"]
---

# Reconstructed Slides: DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners

## Source Video
[DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](https://www.youtube.com/watch?v=-cKUW6n8hBU)

## Method
This deck is reconstructed from the existing video frame captures by detecting likely slide regions with OpenCV, cropping/upscaling those regions, deduplicating similar crops, and OCRing the cropped slide images locally. It is a cleaner companion to the full-stage frame deck.

## Reconstructed Slides
![[assets/reconstructed-slides/-cKUW6n8hBU/slide-001.jpg]]

- Source frame: `slide-001.jpg`
- Crop: `full` `[0, 0, 960, 540]` score `174.3`
![[assets/reconstructed-slides/-cKUW6n8hBU/slide-002.jpg]]

- Source frame: `slide-002.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `158.15`

OCR text:

> DSPy
> Overview
> DSPy is a declarative framework for building modular AI software.
> It allows you to iterate fast on structured code, rather than brittle strings, and
> offers algorithms that compile AI programs into effective prompts and
> weights for your language models
> https://dspy.ai

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-003.jpg]]

- Source frame: `slide-003.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `162.04`

OCR text:

> Taking:NYC(NYT)46.17Centra
> Use Cases Lighting Round
> What we'll cover:
> Simple sentiment classifier
> Structured information from a PDF
> Multimodal extraction
> Web research agent (using Tools)
> Detectboundaries of a document
> github.com/kmad/aie
> Recursivelysummarize an arbitrary-length document
> GEPA example

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-004.jpg]]

- Source frame: `slide-004.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `172.64`

OCR text:

> Taing:NYC(NYT)46.17Centra
> DSPy allows you to decompose logic into a
> program that treats LLMs as a first class citizen
> without having to tweak prompts (unless you
> want to)

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-005.jpg]]

- Source frame: `slide-005.jpg`
- Crop: `full` `[0, 0, 960, 540]` score `175.76`

OCR text:

> (unless you
> S

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-006.jpg]]

- Source frame: `slide-006.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `177.06`

OCR text:

> P
> aowsyoutoretai
> Taking:NYC(NYT) 46.17 Central
> detailed control over your program while focusing on
> things that actually matter
> Allows you to create computer programs thatuse'LLMs
> as inlinefunction calls
> Why I'm such
> Programswhichyouhappentobe abletooptimize-it's a
> programmingparadigm,notawholesaleframework,andnot
> an advocate
> 'optimizer-first"
> Is built with a systems mindset;you encode intent and
> structurein awaythatis transferable
> Yourprogram design likely moves slower thanAI advancements(at
> least sofar)

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-007.jpg]]

- Source frame: `slide-007.jpg`
- Crop: `full` `[0, 0, 960, 540]` score `175.94`

OCR text:

> this way of working
> found it useful - the hope is to
> tives foryou to extrapolate to

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-008.jpg]]

- Source frame: `slide-008.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `166.58`

OCR text:

> Tang:NYC (NYT) 46.17 Cena
> Core Concepts
> Signatures
> Modules
> Tools
> Specifywhatyouwant,
> Structure your program
> Interactwiththeoutside
> nothow;lettheLLM
> logically
> world-or therestofthe
> figure it out
> program
> Adapters
> Optimizers
> Metrics
> Customizableprompt
> OptimizeyourDSPy
> Definewhattooptimize
> formatters:thinkJSON,
> program,ML-style
> against (can be multiple
> BAML,XML,etc.
> things)
> (lettheLLM figure it out!)

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-009.jpg]]

- Source frame: `slide-009.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `175.89`

OCR text:

> Taing:NYC(NYT)46.17Cental
> How you“express your
> Signatures
> declarativeintent”
> Can be simple strings or
> complex Class-based objects

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-010.jpg]]

- Source frame: `slide-010.jpg`
- Crop: `full` `[0, 0, 960, 540]` score `175.74`

OCR text:

> input text to classify sentiment
> he more positive

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-011.jpg]]

- Source frame: `slide-012.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `178.14`

OCR text:

> D
> pdf_link
> sdaau
> ront.net/CIK-0001045810/8b76daec-a85f-429a-968c
> Taikng:NYC(NYT)46.17Central
> Multimodality
> doc=Attachments(pdf_link)
> rag = dspy.ChainofThought("question,document->answer")
> FORM4
> result =rag(question="How many shares were sold in total?",document=doc)
> print(result)
> Prediction(
> reasoning='The document isa Form 4filing reporting changes in beneficial
> ownership of securities by Mark A.Stevens.It lists two transactions involving the
> sale of common stock shares on two dates:\n\n-On 9/11/2025,200,000 shares were
> sold.\n-On 9/12/2025,297,797 shares were sold.\n\nTo find the total number of
> shares so1d,we sum these tw0 amounts:\n\n200,000 +297,797=497,797 shares so1d
> in total.\n\nNo other sales transactions are listed in the document.
> answer='497,797sharesweresoldin total.'

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-012.jpg]]

- Source frame: `slide-013.jpg`
- Crop: `full` `[0, 0, 960, 540]` score `175.92`

OCR text:

> ceporting changes in beneficial
> lists two transactions involving the
> Qn9/11/2025,200,000 shaxes were
> naTofind the total number of
> 297,797=497,797 shares8o1d

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-013.jpg]]

- Source frame: `slide-014.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `158.22`

OCR text:

> G
> Taking:NYCNYT)46.17Cental
> Optimizers
> DSPy has various built-in primitives that allow you to then optimize your
> program. This allows you to quantitatively improve your performance and
> costprofile.
> "A DsPy optimizer is an algorithm that can tune the parameters of a DsPy
> program (i.e., the prompts and/or the LM weights) to maximize the metrics
> you specify, like accuracy."

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-014.jpg]]

- Source frame: `slide-015.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `172.07`

OCR text:

> Taikng:NYCNYT)46.17Cent
> DSPy is not an optimizer. It's set of
> programming abstractions (signatures, modules)
> that can be optimized.
> Omar Khattab @lateinteraction

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-015.jpg]]

- Source frame: `slide-016.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `171.65`

OCR text:

> D
> Taikng:NYC(NYT)46.17Centra
> Thereason thatthisistrickyisquitesubtle.It's thefact that
> anytimeyou use an LLM to assign areward,thoseLLMs aregiant
> thingswith billionsofparameters,and they'regameable.Ifyou're
> reinforcementlearningwithrespect to them,you willfind
> -AndrejKarpathy
> adversarial examplesforyourLMjudgesalmostguaranteed.
> (via theDwarkesh
> Podcast)
> Soyou can't do thisfor too long.You domaybe10 steps or20
> steps,andmaybeitwillwork,butyoucantdo100or100.I
> understand it'snotobvious,butbasically themodelwill find little
> cracks.It will find all these spurious things in the nooks and
> crannies of the giantmodel and find a way to cheat it

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-016.jpg]]

- Source frame: `slide-017.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `178.54`

OCR text:

> GEPA:REFLECTIVEPROMPTEVOLUTIONCANOUTPERFORM
> Taikng:NYC(NYT)46.17Centra
> REINFORCEMENTLEARNING
> LakshyaAAgrawal,ShangyinTan，DilaraSoylu²NoahZiems,
> RishiKhare',Krista Opsahl-Ong,ArnavSinghvi2s,HerumbShandilya²,
> MichaelJRyan,MengJiang',ChristopherPotts²,KoushikSen'
> AlexandrosG.Dimakis,IonStoica'DanKlein',MateiZahariaOmarKhattab
> Chris Potts
> https://www.youtube.com/
> watch?v=0bkwd9OYqfk
> Model
> HotpotQA
> IFBench
> Hover
> PUPA
> Aggregate
> Improvement
> Qwen3-8B
> Baseline
> MIPROv2
> GRPO
> GEPA
> My point here,though,is that both of them outperformed GRPO,which oughttobea
> kind ofadvanced RL-based post-training method,a fine-tuning method.

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-017.jpg]]

- Source frame: `slide-018.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `171.46`

OCR text:

> Taikng:NYC(NYT) 46.17Centra
> This is all you need to construct arbitrarily
> complex workflows, data processing pipelines,
> replication of business logic, etc.

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-018.jpg]]

- Source frame: `slide-019.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `177.32`

OCR text:

> SNOW!
> Ssopshere
> Tang:NYC(NYT) 46.17Centa
> DSPy on X
> @lateinteraction
> CreatorofDSPy(and ColBERT!)
> @maximerivest
> CreatorofAttachments
> @tech_optimist
> DSPy advocate, programmer, nice guy
> @dbreunig
> Writesexcellenttechnicalcontent
> @DSPyOSS
> OfficialDSPy account
> @getpy
> Curator of DSPyWeekly
> @kmad
> Me

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-019.jpg]]

- Source frame: `slide-020.jpg`
- Crop: `full` `[0, 0, 960, 540]` score `175.73`
![[assets/reconstructed-slides/-cKUW6n8hBU/slide-020.jpg]]

- Source frame: `slide-021.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `174.49`

OCR text:

> SatNov22440PM
> PPo
> dspy_workshop.ioymb U
> S
> DSPY_WORKSHOP
> Tang NYC(NYT） 46.17Centl
> mtntSetup>O Setupobservabiity
> >venv
> >vscode
> +Code
> +Markdown
> InterruptRestartCler Al OutputsGoTo|upyter Variables
> Outine
> venv (Python3.11.13)
> >data
> Set up observability
> DD日自
> module_example
> fromphoenix.otelimportregister
> modules
> configure thePhoenixtracer
> tracer_provider=register(
> BoundaryDetector.py
> DocumentClassifier.py
> auto_instrumentaTrueAut&-instrument your app based on installed OI dependencles
> DocumentProcessor.py
> Summarizer.py
> Python
> dezeen
> usecs/karaDmlods/de/dssy_rkshopxyLb/otho3.11/site-Rackages/tomutey:21:Tqdrning:IProgressnot found.Please pdate jupyterand ipywidgets.Seehtts//iay
> VisuaWithTools.py
> from.autonotebookLnporttqdn asnotebook_tqdm
> >output
> main.py
> 1,M
> U,o
> 3o.example
> gitignore
> python-version
> U
> dspy.workshop_cle.
> dspworkshop.ipynb
> U
> hub.ipynb
> LICENSE
> pyproject.toml
> Problem
> ndino
> Debug Console
> TerminalPorts
> Gitlens
> Jupyter
> READMEmd
> adura@MADCAPM28857:~/D/d/d/modute_exampte]-[16:39:55]-[V:.verv]-[G:main=]
> time_entry_optimizer.
> uv.lock
> OUTLINE
> Environment Setup
> MUseful tidbits
> Mi Smple Sentiment..
> MStructured informatio
> Dynamically genera..
> MAdapter Example
> XK10

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-021.jpg]]

- Source frame: `slide-022.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `174.49`

OCR text:

> A
> ·SatNov 22440PM
> PPO
> dspy_workshop.ipymbU
> aeS0
> FO
> DSPY_WORKSHOP
> dspywor（functLon）def toad_dote(
> Tang:NYC (NYT) 4617 Centl
> >env
> +Code
> dotenv_path:StrPath|None=None,
> stream:Io[str]|None=None,
> env (Python3.11.13)
> >vicode
> >data
> Lopt/hs
> verbose: boolFalse,
> skipped unsupported reflection of expression-based inde:
> oexti
> override:boolFalse,
> module_example
> LoRt/hs
> interpolate: boolTrue,
> kipped unsupported reflection of expression-based 1nde
> modules
> pexti
> OTo）b001
> encoding:str]None=“utf-8"
> BoundaryDetector.py
> for
> DocumentClassifier.py
> DocumentProcessor.py
> Parameters:
> doten_path:Absolute or relative path to eovfle.
> Summarizer.py
> stream:Text stream（tuchaso.StringIO）wiheev contnt,ed
> AdozAens
> doteynothN
> VisuWithTools.py
> load_dotenv(overrideTrue)
> >output
> 0.0s
> Python
> main.py
> 1M
> True
> OAN
> U,o
> 5example
> gitignore
> inportos
> python-version
> U
> LM_CONFIG·（
> M
> "nodel":os.getenv("DSPY_FAST_MODEL"),
> dsp_workshop.pynb
> "ap_key":os.getenv（-OSPY_API_KEY"),
> u
> "api_base”:os.getenv("DSPY_ENDPOINT"),
> hubioynb
> n
> "ap1_version:os.getenv("DSPY_FAST_API_vERSION"),
> KLICENSE
> .CLEY MIVTAWOHA
> pyproject.toml
> Problem
> Terminal
> Ports
> Gitens
> Jupyter
> README.md
> r[ks
> adgraMADCAPM28857:~/D/d/d/modute_exanple]-[16:39:55]-[V:.ve]-[G:nain=]
> M
> time_entry.optimizer.
> uvlock
> OUTLINE
> Environment Setup
> MUseful tidbits
> M Simple Sentiment...
> MStructuredinformatio
> Dynamically genera..
> MAdapter Example
> 6A8

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-022.jpg]]

- Source frame: `slide-023.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `176.42`

OCR text:

> Q·SatNov22444PM
> dspy_workshop.ipynbU
> dspy_workshop_clean.ipynbM
> hub.ipyn
> Summarizer.py
> Taing:NYC (NYT) 46.7Centa
> dspy_workshop_clean.ipynb>M Structured information from a PDF> #Attachments/multimodal / structured output
> +Code
> +Markdown
> Interrupt
> RestartClearAllOutputsQGoToJupyterVariablesOutline
> verv（Python 3.11.13)
> 口
> from attachments.dspy import Attachments
> D日
> doc=Attachnents（pdf_link)
> 0.9s
> Python
> [Attachments]
> Running prinaryprocessor'pdf_to_llm'forhttps://d18rn@p25nr6d.cloudfront.net/C1K-00e1e4581e/8b76dacc-a85f-429a-968c-3c3c9dbac3fc.pdf
> [Attachments]
> Applyingstep'load.url_to_response'tohttps://d18rn0p25owr6d.cloudfrontnet/CIK-0001045810/8b76daec-a85f-429a-968c-3c3c9dbae3fc.pdt
> [Attachments]
> Applying step‘modify.norph_to_detected_type'to httas://d18rn@g25nmr6d.cloudfront.net/CIK-0001045810/8b76daec-a8Sf-429a-968c-3c3c9dbae3fc.pdf
> [Attachments]
> Applyingstep'load.pdf_to_pdfplumber'tohttps://d18rneo25mmr6d.cloudfront.net/CIK-0801045810/8b76daec-a85f-429a-968c-3c3c9dbae3fc.pdf
> [Attachments]
> Applying stepmodity.pages'tohttos://d18rnep25nwr6d.cloudfcont.net/cIK-e001845810/8b76daec-a85f-429a-968c-3c3c9dbae3fc.pdf
> [Attachments]
> Running AdditivePipeline(present.markdown+present.images+present.metadata)
> [Attachments]
> Applyingadditivestep'present.markdown'tohttps://d18rneo25mr6d.cloudfront.net/CIK-0001045810/8b76daec-a851-429a-968c-3c3c9dbae3fc.pd1
> [Attachments]
> Applying additive step'present.inages'tohttps://d18rnlo25mar6d.cloudfront.net/CIK-ee0104581e/8b76dacc-a85f-429a-968c-3c3c9dbae3fc.pdf
> Thisiswhat we're working with
> from IPython.display inport Image,display
> display(Image(url=doc.inages[e]))
> Python
> from https://maximerivest.github.1o/attachments/architecture/sdspy-integration
> Problems
> Output
> Debug Console
> Terminal
> Ports
> GitLens
> Jupyter
> fish-mod_oxample+①
> XKtOg
> Pmain
> Launchpad
> 86A8
> CursorTab
> Spaces:4
> Cell19of59
> AmpTab

![[assets/reconstructed-slides/-cKUW6n8hBU/slide-023.jpg]]

- Source frame: `slide-024.jpg`
- Crop: `contour` `[0, 0, 960, 540]` score `175.62`

OCR text:

> A
> 2·SatNov 22447PM
> 口
> 口口
> dspy_workshop.ipynbU
> dspy_workshop_clean.ipynbM
> hub.ipyn
> summarization.ipynb M
> Summarizer.py
> Takng:NYC (NYT) 46.17Centra
> dspy_workshop_clean.ipynb>M Structured information from a PDF>MDynamicall generate a schema based on the content itself>from pydantic import BaseModel, Field
> +Code
> 十Markdown
> RunAllRestartClearAllOutputs|JupyterVariablesOutline
> venv(Python 3.11.13)
> ""-A transaction in the document.
> D
> transaction_type:str=Field(description="The type oftransaction.")
> D日
> shares_sold:int =Field(descrintinn="Thenimher nf shares snln.)
> price_per_s(class）str
> total_price
> str(object=")->str str(bytes_or_buffer[encodingL errors]l)->str
> class Docunents Create anew stringobjectfrom the given object.f encodingorerrorsis specified,then the objectmustexpose a data buffer that wil e
> Astructdecodedusingtgienencodinganderrorhanderthewisereturnsthresultfbjctst_Ofdfined）orreprobjct）encoding
> formtype:defaults tosys.getefuencoing.ersdfalts tostic
> filing_date: str=Field（descriptionaThe date of the filing in the format YyyY-MM-Do.)
> total_shares,sold:int
> transactions:list[Transaction]=Field(description"Alist of transactions.")
> class DocumentAnalyzerSchena(dspy.Signature):
> Analyze document content and extract insights.
> MIEN
> document:Attachnents=dspy.InputField()
> document_schena:DocunentSchena=dspy.OutputField(desc="A structured representation of the document content.")
> result_schema=dspy.ChainofThought(DocumentAnalyzerSchena)(docunent=doc)
> pprint(dict{Any,Any)(result_schena.document_schema))
> #Now use the typed object to get the total shares sold
> print(\n\n#Total shares sold:)
> print(result_schena.document_schena.total_shares_sold)
> 0.0s
> Python
> {'filing_date':'2025-09-15',
> 'form_type':Form 4',
> I ±
> Problems
> Output
> Debug Console
> Terminal
> Ports
> GitLens
> Jupyter
> fish-modue_example+①自
> X
> XKtooe
> main
> Launchpad
> ?6A8
> CursorTab
> Spaces:4
> Cell26of59
> AmpTab
## Dense Scene-Detected Slide Candidates
- [[youtube--cKUW6n8hBU-dense-slides]]
