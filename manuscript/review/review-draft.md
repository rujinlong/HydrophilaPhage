# From genomes to safe, designed phage products: resource, computational, and design pipelines for aquaculture phage therapy
Jinlong Ru
2026-05-29

<!--
综述 stub (DEC-D010 综述位 · 7 月底独投，锁优先权 + 为线② 引流)
- 角度: resource–compute–safety–enzyme–design (避开 F&F 2026 已占的"疗效+实施")
- 目标刊: FEMS Microbiology Reviews / Trends in Biotechnology / npj Viruses
- 字数 ~6000–7000 · PI lead/通讯，学生 C 协助文献+作图
- outline 源: program-docs/review-outline.md
- 动笔前: 用 add-citation / verify-refs 把下方 DOI 全部落 Zotero @citekey
- ⚠ 政策段严守: 水产走农业农村部新兽药路径，不碰 818 号令 (EL-003)
- 待 (b) 第二轮检索回填 §2 资源现状证据
-->

# Abstract

Bacteriophage therapy is a leading non-antibiotic option for the
bacterial diseases that constrain aquaculture, and its efficacy against
the major fish and shellfish pathogens is by now well documented. We
argue that efficacy is no longer the factor limiting deployment. The
barrier between a phage that clears an infection and a phage *product*
that can be registered and manufactured is infrastructural, and it spans
four computational layers that the efficacy-focused literature leaves
implicit: the genomic *resource*, the *safety* assessment that gates
regulatory approval, the *enzyme* catalogue that phage genomes encode,
and the *design* capability needed to make useful-but-unsafe phages
deployable. We review each layer for aquaculture pathogens and find the
same deficit throughout — phage databases are organised by sequence
rather than by host, none pre-screens candidates for therapeutic safety,
lytic-enzyme mining remains a scatter of single-enzyme studies blind to
structurally divergent “dark matter”, and no resource offers a design
layer. We outline what a dedicated, host-resolved aquaculture phage
resource — unifying standardised annotation, safety scoring, enzyme
cataloguing and rational design — would contain, and argue that building
this infrastructure, rather than re-demonstrating efficacy, is what will
move the field from proof to product.

# 1. Introduction

<!-- 初稿 v0 (2026-05-29)，可扩；目标 ~800w。已按 de-AI 原则写，定稿前可跑 /de-ai-academic-prose 精修。 -->

Aquaculture now supplies roughly half of the aquatic animals consumed
worldwide, and bacterial disease remains one of the largest brakes on
its productivity. Gram-negative pathogens — *Aeromonas hydrophila*,
*Vibrio* spp., *Edwardsiella* spp., *Flavobacterium* spp.,
*Photobacterium damselae* — and Gram-positive *Streptococcus* spp. cause
recurrent haemorrhagic septicaemia, enteric and ulcerative disease
across freshwater and marine culture. The historical response,
metaphylactic antibiotics, has become both ecologically and legally
untenable: antimicrobial use in food animals selects for resistance that
propagates through aquatic microbiomes, and regulators have moved to
curtail it. China’s Ministry of Agriculture and Rural Affairs
Announcement No. 194 ended the use of growth-promoting antibiotics in
feed in 2020, sharpening the search for deployable alternatives.

Bacteriophage therapy is the most developed of these alternatives for
aquaculture. Phages are naturally abundant in the water column,
self-amplify at the site of infection, are narrow in host range, and can
be delivered by immersion, feed or injection — properties that fit
aquaculture operations more naturally than they fit clinical medicine. A
substantial body of work, summarised in several recent reviews,
documents efficacy against the major aquaculture pathogens and addresses
the practical questions of administration, host immunity and microbiome
impact (James et al. 2026; Yang et al. 2024; Albarella et al. 2025;
Landor et al. 2026).

The premise of this review is that efficacy is no longer the limiting
question. The barrier between a phage that kills a pathogen in a tank
and a phage *product* that can be registered, manufactured and safely
deployed is infrastructural: it lies in the genomic resources, the
computational safety assessment, the enzyme catalogues and the design
capability that surround the phage, not in the phage’s intrinsic lytic
activity. These four layers — resource, compute/safety, enzyme and
design — are precisely what the efficacy-centred literature leaves
implicit.

This is not a semantic distinction. Approval of a phage biologic — in
aquaculture in China, through the veterinary-biologics registration
route administered by the agricultural authorities — turns on the
demonstrable absence of virulence factors, antibiotic-resistance genes
and functional lysogeny modules. These properties are read off the
genome by computation, not by the *in vivo* challenge experiments that
dominate the efficacy literature. A phage that protects fish but carries
a toxin gene or an integrase is not a product. The genome, and the tools
that interpret it, are therefore the gating layer.

We organise the review around the path from genome to safe, designed
product. Section 2 examines the resource base — which
aquaculture-pathogen phage genomes exist, how they are biased, and why
no current database serves them in a therapy-oriented, host-resolved
form. Section 3 treats the computational safety layer that converts a
genome into a regulatory verdict. Section 4 surveys lytic-enzyme mining,
where sequence-only methods systematically miss structurally divergent
depolymerases and endolysins. Section 5 addresses rational design —
engineering safer phages by removing lysogeny and virulence modules. We
close (Section 6) by arguing that these layers should be integrated into
a dedicated aquaculture phage resource, safety and design platform, and
outline what such a resource must contain.

# 2. The resource base

<!-- 初稿 v0 (2026-05-29)，目标 ~1200w；MetaVR 处暂引 IMG/VR citekey，待 cite_doi 补 MetaVR 专引。 -->

**The sequenced record is fragmented and host-biased.** Phage genomes
accumulate rapidly, but those relevant to aquaculture are scattered as
single-isolate characterisations rather than organised collections. No
genus-level pangenome exists for the phages of any major fish or
shellfish pathogen. The consequence is that comparative questions — how
conserved a candidate endolysin is, whether a depolymerase has
homologues across host genera, how a new isolate relates to described
taxa — cannot be answered without rebuilding the dataset from scratch
each time.

The bias is quantifiable. The INPHARED census of cultured phage genomes
shows that 75% of sequenced phages were isolated on only 30 bacterial
genera, and that ~54% of temperate genomes derive from just three host
genera (Cook et al. 2021). The aquaculture pathogens — *Aeromonas*,
*Vibrio*, *Edwardsiella*, *Photobacterium*, *Flavobacterium* — sit in
the long tail of this distribution. INPHARED also reports that
antibiotic-resistance-gene carriage is higher in temperate than in lytic
phages and varies with host, a finding that bears directly on the safety
screening of Section 3.

**General databases exist, but they are host-agnostic and not built for
therapy.** Several large, well-annotated resources cover phage genomes
broadly:

- PhageScope assembles ~873,000 phage sequences and applies fifteen
  tools to annotate completeness, host range, lifestyle, taxonomy and
  genetic elements (Wang et al. 2023). The annotation is thorough, but
  the database is organised by sequence rather than by host pathogen and
  makes no therapeutic-safety determination.
- MetaVR (Fiamenghi et al. 2026), the successor to IMG/VR (Camargo et
  al. 2022), now holds tens of millions of uncultivated viral genomes
  with programmatic access and predicted structures. It is environmental
  in scope and assigns hosts by prediction, which suits virome surveys
  more than curated therapeutic selection.
- PhagesDB is deep but taxonomically narrow, centred on
  actinobacteriophages that do not overlap the aquaculture pathogens
  (Russell and Hatfull 2017).
- PhageDive links 1,167 phages to physical culture-collection holdings
  with rich metadata (Rolland et al. 2024) — valuable for sourcing
  biological material, but neither aquaculture-focused nor
  therapy-screened.

None of these partitions phages by aquaculture-pathogen host, and none
pre-screens candidates for therapeutic safety. A researcher seeking
lytic, safe phages against *Aeromonas hydrophila* must today query each
resource separately, reconcile incompatible metadata, and perform safety
annotation *de novo*.

**Standardised annotation is the precondition for a usable resource.**
Because the source genomes are heterogeneous in origin and quality, a
host-resolved aquaculture resource must first impose a uniform
analytical pass: completeness and contamination estimation with CheckV;
classification that is robust rather than single-gene, combining
whole-genome intergenomic similarity (VIRIDIC (Moraru et al. 2020)) with
genome-wide proteomic trees (ViPTree (Nishimura et al. 2017)) and ICTV
alignment; lifestyle prediction; host prediction; and functional
annotation through a Pharokka–Phold pipeline. Integrated workflows of
this kind (e.g. ViroProfiler) make the pass reproducible across
pathogens.

Only once genomes are collected by host, dereplicated,
quality-controlled and uniformly annotated does a master table become
feasible — one row per phage, carrying taxonomy, lifestyle, host, safety
flags and enzyme content. That table is the shared substrate for the
safety screening (Section 3), enzyme mining (Section 4) and design
(Section 5) layers that follow, and is the natural unit that a dedicated
platform (Section 6) would expose.

# 3. The computational safety layer

<!-- 初稿 v0 (2026-05-29)，目标 ~1200w。 -->

A phage genome becomes a therapeutic candidate only after it has been
cleared of three classes of liability, and that clearance is
computational. The veterinary-biologics dossier (Section 1) requires
evidence that a candidate carries no transferable virulence factors, no
antibiotic-resistance genes, and no functional lysogeny machinery that
would let it integrate, transduce host DNA, or lysogenically convert its
target. Each is, in the first instance, a sequence-level determination.

The screening logic is simple to state. Virulence factors are detected
against curated databases such as VFDB; resistance genes against CARD,
AMRFinderPlus or ResFinder; and lysogeny from the presence of
integrases, recombinases and repressors, with prophage-associated toxin
genes flagged separately. A candidate carrying any resistance gene, any
virulence factor, or an intact lysogeny module is downgraded to
“caution” or “unsafe”; only genomes clear on all three axes pass as
therapeutic candidates. The rule set is easy to write down — applying it
consistently across a heterogeneous collection, and keeping the verdict
current as the underlying databases are revised, is not.

The bias documented in Section 2 makes the lysogeny axis especially
consequential here. INPHARED shows that resistance-gene carriage is
concentrated in temperate phages and varies with host (Cook et al.
2021); the under-sampled aquaculture pathogens are therefore exactly
where the relationship between lifestyle and safety is least
characterised, and where a confident lytic-only selection cannot yet be
made from existing annotation.

Tooling has begun to address this. Sphae automates a therapy-oriented
screen — quality control, assembly, and detection of virulence factors,
resistance genes and lysogeny markers — and reports a per-genome
suitability verdict (Papudeshi et al. 2024), showing that the screen can
be made routine. But Sphae is a host-agnostic pipeline run per dataset,
not a curated, queryable, host-resolved resource: it tells a user
whether a genome they already hold is therapy-grade; it does not let
them ask “which sequenced *Aeromonas hydrophila* phages are safe and
lytic?” and get an answer. The general databases of Section 2 carry
fragments of the needed annotation but integrate none of it into a
safety verdict tied to an aquaculture host.

The gap is thus not a missing algorithm but a missing layer: a
standardised safety score applied uniformly across host-partitioned
aquaculture phages and exposed so that the regulatory-relevant question
can be put to the resource directly. This layer is the computational
hinge between the genome collection of Section 2 and the registrable
product of Section 1.

# 4. Mining lytic enzymes

<!-- 初稿 v0 (2026-05-29)，目标 ~1200w。TODO: Foldseek/Phold/ProstT5/geNomad 等软件引用待补 citekey。 -->

Phage-encoded lytic enzymes — depolymerases that strip capsular
polysaccharide, endolysins that cleave peptidoglycan, and the holins and
spanins that govern their release — are attractive as enzybiotics in
their own right: they act on defined molecular targets, do not
self-replicate, and sidestep several of the regulatory concerns that
attach to live phages. For aquaculture they are largely untapped.

The published record is a scatter of single-enzyme characterisations
rather than a catalogue. Against *Aeromonas hydrophila* alone, the
endolysin LysE (Baliga et al. 2023), the broad-spectrum prophage
endolysin PlyD4 — which protects zebrafish *in vivo* (Wang et al. 2022)
— and the calcium-activated phage endolysin EndoA3 (Mikoulinskaia et al.
2025) have each been described in isolation. Each proves that useful
enzymes are present; none amounts to a systematic survey of the enzyme
space across aquaculture pathogens. The one host where systematic mining
has been done is *Vibrio*: a recent study recovered 573 putative
depolymerase genes across cultured and uncultivated vibriophages (Yue et
al. 2026), which both demonstrates the scale of the latent resource and
underscores how unmined the other aquaculture genera remain.

The deeper problem is methodological. Sequence-homology search — BLAST
or HMM against known families — recovers only enzymes that resemble
characterised ones, and many lytic enzymes do not. The *Vibrio*
depolymerase Dep193 carries no recognisable domain (Yue et al. 2026) and
is invisible to a domain-based scan; an enzyme catalogue built on
sequence search alone therefore systematically misses the structurally
novel “dark matter” that is often the most valuable.

Structure-based discovery closes this gap. Predicting structure for
hypothetical or no-hit proteins — directly through ProstT5’s
sequence-to-3Di translation, or by folding followed by Foldseek
structural search against the PDB, with structure-aware functional
annotation via Phold — recovers enzymes that share fold and active-site
geometry with known depolymerases and endolysins despite negligible
sequence identity. Applied as a pan-domain, multi-family search spanning
*Aeromonas*, *Edwardsiella*, *Flavobacterium* and *Photobacterium*, this
is the increment over the single-enzyme, single-motif precedents: a
structurally informed, cross-pathogen enzyme catalogue rather than
another one-off characterisation.

# 5. Rational design

<!-- 初稿 v0 (2026-05-29)，目标 ~1000w。TODO: Prophage-Activation 平台 / CRISPR-avoidant 管线 引用待补 citekey。 -->

The layers above are descriptive: they collect, screen and mine what
already exists. A design layer turns the resource generative — it asks
not only “which phages are safe?” but “how can an unsafe-but-useful
phage be made safe?”

The most tractable design objective in aquaculture is converting a
temperate phage into a lytic-equivalent therapeutic. Many phages with
desirable host range or enzyme content are excluded by the safety screen
of Section 3 because they carry lysogeny modules or virulence cassettes.
The same annotation that flags them also localises the offending
elements — the integrase, the repressor, and the attachment (*att*)
boundaries of the prophage, or the edges of a toxin cassette — to
specific coordinates. Removing or disrupting these elements, then
verifying that the edited genome stays lytic while the flagged module is
inactivated, is a Design–Build–Test–Learn (DBTL) cycle whose Design step
is computational and reads directly off the safety annotation.

This connects to a broader shift from descriptive databases toward
design-oriented tools in phage biology — for instance, *in silico*
platforms that identify prophage regulatory elements to inform the
engineering of lytic derivatives (Musrrat et al. 2025), or CRISPR-based
strategies for re-arming and re-targeting phages. What distinguishes a
design layer from a catalogue is that it proposes new sequences rather
than only annotating existing ones; this generative step —
lysogeny-module excision, host-range engineering, capsid or tail
re-targeting — is absent from every resource surveyed in Sections 2–3.

For a host-resolved aquaculture resource the design layer need not be
elaborate to be valuable. A rule engine that, given a phage flagged at
the safety step, locates the excision targets, proposes a module-deleted
variant and scores the residual risk would already convert the resource
from a filter into a generator; a single proof-of-concept design —
synthesised and shown to remain lytic with the module inactivated —
suffices to establish the capability. Full engineering iteration is a
research programme in itself. The point here is that the design layer is
a natural, and currently missing, extension of the same annotation that
drives safety screening and enzyme discovery.

# 6. Outlook: an integrated platform

<!-- 初稿 v0 (2026-05-29)，目标 ~800w。 -->

The four layers are usually handled separately, by different tools and
different papers, and that separation is itself the gap. A phage genome
must be collected and standardised (Section 2), screened for safety
(Section 3), mined for enzymes (Section 4) and, where useful but unsafe,
redesigned (Section 5) — and for aquaculture none of this is currently
available in a host-resolved, queryable form. The efficacy literature
(James et al. 2026; Yang et al. 2024; Albarella et al. 2025; Landor et
al. 2026) establishes that phage therapy works in aquaculture; the
resource, safety, enzyme and design infrastructure needed to turn that
into registrable products does not yet exist as an integrated whole.

What is needed is a dedicated aquaculture phage resource that unifies
these layers on one substrate: phages collected and partitioned by
aquaculture-pathogen host; uniformly annotated into a master table
carrying taxonomy, lifestyle, host, safety verdict and enzyme content;
queryable, so that the regulatory-relevant questions — which phages are
safe and lytic against a given pathogen, which enzymes are available,
which candidates can be redesigned — can be answered directly; and
openly accessible, since a resource of this kind earns its value through
sustained use. Such a platform would also serve the disease-ecology
layer: environmental phage signal recovered from public aquaculture
metagenomes, including the uncultivated-genome resources of Section 2,
can be mapped against the same host-resolved reference, extending the
resource from cultured isolates to the farm environment.

This framing — resource, computation, safety, enzyme and design as the
infrastructure of aquaculture phage therapy — is, to our knowledge, not
occupied by existing reviews, which centre on efficacy and
implementation. Building that infrastructure, rather than
re-demonstrating efficacy, is what will move aquaculture phage therapy
from proof to product.

## 关键文献清单 (内部注释·投稿前删除)

<!-- 三方尽调去重，真实 DOI。动笔前用 add-citation / verify-refs 全部导入 Zotero。
- 资源/库: PhageScope @2023-PhageScope_Wang · INPHARED @2021-INfrastructure_Cook · IMG/VR @2022-IMG_Camargo · MetaVR @2026-Metavirus_Fiamenghi · PhagesDB @2017-PhagesDB_Russell · PhageDive @2024-PhageDive_Rolland · Sphae @2024-Sphae_Papudeshi
- 酶: LysE @2023-Cloning_Baliga · PlyD4(斑马鱼体内) @2022-Characterization_Wang · EndoA3 @2025-Endolysin_Mikoulinskaia · Vibrio dep mining @2026-Mining_Yue
- 工具: VIRIDIC @2020-VIRIDIC_Moraru · ViPTree @2017-ViPTree_Nishimura · ViroProfiler / geNomad / CheckV / Foldseek / Phold / VICTOR (软件,引官方)
- 已占疗效综述(须显式区分): @2026-Review_James · @2024-Evaluation_Yang · @2025-Bacteriophage_Albarella · @2026-Phage_Landor
- 方法学类比: Rey-Campos 2023 @2023-Metatranscriptomics_Rey-Campos
-->

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-2025-Bacteriophage_Albarella" class="csl-entry">

Albarella, Deborah, Paola Dall’Ara, Luciana Rossi, and Lauretta Turin.
2025. “Bacteriophage Therapy in Freshwater and Saltwater Aquaculture
Species.” *Microorganisms* 13 (4): 831.
<https://doi.org/10.3390/microorganisms13040831>.

</div>

<div id="ref-2023-Cloning_Baliga" class="csl-entry">

Baliga, Pallavi, Puneeth Thadooru Goolappa, Malathi Shekar, and Girisha
Shivani Kallappa. 2023. “Cloning, Characterization, and Antibacterial
Properties of Endolysin LysE Against Planktonic Cells and Biofilms of
Aeromonas Hydrophila.” *Probiotics and Antimicrobial Proteins* 15 (3):
646–54. <https://doi.org/10.1007/s12602-021-09880-7>.

</div>

<div id="ref-2022-IMG_Camargo" class="csl-entry">

Camargo, Antonio Pedro, Stephen Nayfach, I-Min A Chen, et al. 2022.
“IMG/VR V4: An Expanded Database of Uncultivated Virus Genomes Within a
Framework of Extensive Functional, Taxonomic, and Ecological Metadata.”
*Nucleic Acids Research*, November, gkac1037.
<https://doi.org/10.1093/nar/gkac1037>.

</div>

<div id="ref-2021-INfrastructure_Cook" class="csl-entry">

Cook, Ryan, Nathan Brown, Tamsin Redgwell, et al. 2021. “INfrastructure
for a PHAge REference Database: Identification of Large-Scale Biases in
the Current Collection of Cultured Phage Genomes.” *PHAGE*, ahead of
print, October. <https://doi.org/10.1089/phage.2021.0007>.

</div>

<div id="ref-2026-Metavirus_Fiamenghi" class="csl-entry">

Fiamenghi, Mateus B, Antonio Pedro Camargo, Iro N Chasapi, et al. 2026.
“Meta-Virus Resource (MetaVR): Expanding the Frontiers of Viral
Diversity with 24 Million Uncultivated Virus Genomes.” *Nucleic Acids
Research* 54 (D1): D801–12. <https://doi.org/10.1093/nar/gkaf1283>.

</div>

<div id="ref-2026-Review_James" class="csl-entry">

James, Louise, Tamsyn M. Uren Webster, Gethin Thomas, Mathias Middelboe,
and Sofia Consuegra. 2026. “A Review of Phage Therapy for Aquaculture
Applications: Efficacy, Health Ramifications and Research Challenges.”
*Fish and Fisheries* 27 (2): 300–312.
<https://doi.org/10.1111/faf.70055>.

</div>

<div id="ref-2026-Phage_Landor" class="csl-entry">

Landor, Lotta A. I., Valeria Ruffo, Sachia J. Traving, and Mathias
Middelboe. 2026. “Phage Therapy in Finfish Aquaculture: How to Get
There?” *Trends in Microbiology* 34 (2): 149–58.
<https://doi.org/10.1016/j.tim.2025.08.002>.

</div>

<div id="ref-2025-Endolysin_Mikoulinskaia" class="csl-entry">

Mikoulinskaia, Galina V., Sergei V. Chernyshov, Sergey V. Tarlachkov, et
al. 2025. “Endolysin of Aeromonas Bacteriophage 3: A Novel
Ca2+-Activated Peptidoglycan Hydrolase Giving Insight into the
Regulation of Phage Lysis in <span class="nocase">Gram-negative</span>
Bacteria.” *International Journal of Biological Macromolecules* 322
(September): 146934. <https://doi.org/10.1016/j.ijbiomac.2025.146934>.

</div>

<div id="ref-2020-VIRIDIC_Moraru" class="csl-entry">

Moraru, Cristina, Arvind Varsani, and Andrew M. Kropinski. 2020.
“VIRIDIC—A Novel Tool to Calculate the Intergenomic Similarities of
Prokaryote-Infecting Viruses.” *Viruses* 12 (11): 1268.
<https://doi.org/10.3390/v12111268>.

</div>

<div id="ref-2025-Prophage_Musrrat" class="csl-entry">

Musrrat, Saher, Zequan Han, Kai Wang, et al. 2025. “Prophage Activation:
An In Silico Platform for Identifying Prophage Regulatory Elements to
Inform Phage Engineering Against Drug-Resistant Bacteria.” *Life* 15
(9): 1417. <https://doi.org/10.3390/life15091417>.

</div>

<div id="ref-2017-ViPTree_Nishimura" class="csl-entry">

Nishimura, Yosuke, Takashi Yoshida, Megumi Kuronishi, Hideya Uehara,
Hiroyuki Ogata, and Susumu Goto. 2017. “ViPTree: The Viral Proteomic
Tree Server.” *Bioinformatics* 33 (15): 2379–80.
<https://doi.org/10.1093/bioinformatics/btx157>.

</div>

<div id="ref-2024-Sphae_Papudeshi" class="csl-entry">

Papudeshi, Bhavya, Michael J Roach, Vijini Mallawaarachchi, et al. 2024.
“Sphae: An Automated Toolkit for Predicting Phage Therapy Candidates
from Sequencing Data.” *Bioinformatics Advances* 5 (1): vbaf004.
<https://doi.org/10.1093/bioadv/vbaf004>.

</div>

<div id="ref-2024-PhageDive_Rolland" class="csl-entry">

Rolland, Clara, Johannes Wittmann, Lorenz C Reimer, et al. 2024.
“Phage*Dive*: The Comprehensive Strain Database of Prokaryotic Viral
Diversity.” *Nucleic Acids Research*, October, gkae878.
<https://doi.org/10.1093/nar/gkae878>.

</div>

<div id="ref-2017-PhagesDB_Russell" class="csl-entry">

Russell, Daniel A., and Graham F. Hatfull. 2017. “PhagesDB: The
Actinobacteriophage Database.” *Bioinformatics (Oxford, England)* 33
(5): 784–86. <https://doi.org/10.1093/bioinformatics/btw711>.

</div>

<div id="ref-2022-Characterization_Wang" class="csl-entry">

Wang, Chaojie, Shengchi Shi, Meiju Wei, and Yi Luo. 2022.
“Characterization of a Novel Broad-Spectrum Endolysin PlyD4 Encoded by a
Highly Conserved Prophage Found in Aeromonas Hydrophila ST251 Strains.”
*Applied Microbiology and Biotechnology* 106 (2): 699–711.
<https://doi.org/10.1007/s00253-021-11752-7>.

</div>

<div id="ref-2023-PhageScope_Wang" class="csl-entry">

Wang, Ruo Han, Shuo Yang, Zhixuan Liu, et al. 2023. “PhageScope: A
Well-Annotated Bacteriophage Database with Automatic Analyses and
Visualizations.” *Nucleic Acids Research*, October, gkad979.
<https://doi.org/10.1093/nar/gkad979>.

</div>

<div id="ref-2024-Evaluation_Yang" class="csl-entry">

Yang, Lei, Qing Yang, Ren-Ge Hu, Wei Cong, Shu Li, and Yuan-Huan Kang.
2024. “The Evaluation of Bacteriophage Therapy in Aquaculture: A
Systematic Review and Meta-Analysis.” *Aquaculture* 588 (July): 740925.
<https://doi.org/10.1016/j.aquaculture.2024.740925>.

</div>

<div id="ref-2026-Mining_Yue" class="csl-entry">

Yue, Yufei, Jiulong Zhao, Zengmeng Wang, et al. 2026. “Mining a
Vibriophage Depolymerase for Enhanced Pathogen Control in Aquaculture.”
*Applied and Environmental Microbiology* 92 (2): e01824–25.
<https://doi.org/10.1128/aem.01824-25>.

</div>

</div>
