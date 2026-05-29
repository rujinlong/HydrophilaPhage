# 文献尽调 Research Brief — 投入前的 novelty + 可发表性验证 (v1)

> **状态**: v1 (2026-05-29) · **母战略**: `aquaculture-track-record-plan-v1.md` (DEC-D010)
> **用途**: 双重——(a) Claude `deep-research` skill 的执行 scope;(b) 喂给 Google Gemini DeepResearch / ChatGPT DeepResearch 做**交叉验证**(due diligence 不押单一引擎)。
> **决策门**: 本调研结论决定 program 三条线各自 **go / pivot / no-go**。在底座 v0 开工**之前**必须完成。

---

## 0. 一句话需求
对下列 3 条研究线 + 1 个综述位,逐条回答两个问题:**(A) 是否已被做过/正在被做(撞车风险)?(B) 我们做完后真的发得出去吗(可发表性证据)?** 不要泛泛而谈,要带**具体文献题录(作者-年份-刊-DOI)+ 明确 gap 陈述 + 同类近 2 年发表实例**。

## 1. 背景上下文(给任意调研引擎)
申请人:病毒组生物信息学专家,自研噬菌体组分析流程 ViroProfiler;有 HPC + 数据库构建经验;已与西农王高学团队合作发现抗嗜水气单胞菌噬菌体 Hp3(大口黑鲈,存活 15%→85%,在审)。目标:用**纯生信/数据挖掘/数据库**为主、湿验证为辅,在**水产噬菌体/水产病毒组**方向建立发表记录。关注病原:_Aeromonas hydrophila/veronii/salmonicida_(锚点)、_Vibrio_、_Edwardsiella_、_Flavobacterium_、_Streptococcus iniae/agalactiae_、_Photobacterium_、_Yersinia ruckeri_ 等鱼虾病原。

---

## 2. 逐条调研任务

### 线① — Aeromonas 噬菌体泛基因组 + depolymerase/endolysin 系统挖掘
- **精确问题**:
  1. 已发表的 _Aeromonas_ phage **比较基因组/泛基因组/系统发育/分类(新科新属)** 研究做到什么规模?最新、最大的是哪几篇(2020–2026)?
  2. _Aeromonas_(及 _Edwardsiella_/_Flavobacterium_/_Photobacterium_)phage 的 **depolymerase / endolysin 系统性多样性挖掘**是否已有专文?(注:_Vibrio_ phage 的酶挖掘 2025 已有,需确认并避开)
  3. 有无"挖掘 + 合成/表达 + 裂菌验证"闭环的水产 phage enzybiotics 论文?发在哪?
- **英文检索词**: `Aeromonas hydrophila bacteriophage comparative genomics` · `Aeromonas phage taxonomy new genus` · `phage depolymerase aquaculture` · `endolysin Aeromonas fish pathogen` · `phage enzybiotics aquaculture`
- **重点刊**: *Viruses* · *Microbiology Spectrum* · *Appl Environ Microbiol* · *Int J Biol Macromol* · *Archives of Virology*
- **要的产出**: 关键文献清单 + "Aeromonas 酶挖掘是否仍空白"明确判断 + 我方差异化(更大基因组集 + 酶维度 + 功能验证)是否成立。

### 线② — 水产病原噬菌体"治疗安全性筛查/设计"数据库 (web server)
- **精确问题**:
  1. 是否存在**针对鱼虾病原宿主**的专门 phage 基因组数据库/web 资源?(名称/URL/年份/覆盖)
  2. 现有通用大库(**PhageScope** NAR 2024、**INPHARED**、IMG/VR、PhagesDB)是否按"水产病原宿主"切分、是否做**治疗安全性筛查(毒力基因/ARG/溶原模块)**、是否支持 **safe-phage 设计**?
  3. 以"治疗适配/安全筛查"为卖点的 phage database paper 近年发在哪(*Database (Oxford)* / *Scientific Data* / *NAR Database issue*)?其 novelty 门槛与 web server 要求?
- **英文检索词**: `bacteriophage database aquaculture fish pathogen` · `phage therapy candidate database virulence antibiotic resistance screening` · `phage genome database web server NAR` · `safe phage engineering lysogeny module removal`
- **重点刊**: *Database (Oxford)* · *Scientific Data* · *NAR Database issue* · *mSystems*
- **要的产出**: "有无专门库"明确判断 + 通用库局限对照表 + 我方差异化(水产宿主切分 + 安全筛查 + 设计)是否成立 + NAR Database issue 收录门槛与年度窗口。

### 线③ — 养殖系统 virome + 病原噬菌体 landscape (公共数据重分析)
- **精确问题**:
  1. **鱼/虾肠道 virome、养殖水体/底泥 virome** 已发表多少?有无**跨研究公共数据 meta-analysis**?
  2. 哪些主养品种(罗非鱼/对虾/鲤/鲈/大口黑鲈)、哪些地理区(中国/东南亚养殖带)是空白?
  3. **bulk metagenome vs VLP-enriched** 的 viral-signal 可靠性争议,审稿现状如何?这类 landscape 发在哪?
- **英文检索词**: `fish gut virome aquaculture` · `shrimp virome metagenome` · `aquaculture water virome bacteriophage` · `viral metagenomics fish farm` · `largemouth bass virome`
- **重点刊**: *mSystems* · *Environmental Microbiome* · *Animal Microbiome* · *ISME Communications*
- **要的产出**: 已发表 landscape 清单 + 空白(品种/地理/方法)陈述 + bulk-vs-VLP 审稿风险评估 + 可发表性判断。

### 综述位 — 水产噬菌体疗法的资源/生信现状
- **精确问题**: 近 3 年(2023–2026)有无**水产噬菌体疗法/水产 phage 生物信息学**的综述或 perspective 已占位?各自侧重?是否还留有"资源 + 计算/设计"视角的综述空间?
- **英文检索词**: `phage therapy aquaculture review` · `bacteriophage fish disease control review 2024 2025` · `bioinformatics phage aquaculture perspective`
- **要的产出**: 已有综述清单 + "资源/生信/DBTL 视角综述位是否仍空"判断。

---

## 3. 检索源 / 范围 / 语言
- **源**: PubMed · Google Scholar · bioRxiv · Web of Science(若可) · 各目标刊官网 · ICTV(分类) · 上述数据库官网
- **时间**: 重点 **2020–2026**;分类/数据库类追溯更早奠基文献
- **语言**: 英文为主;中文文献(CNKI/万方)如有水产 phage 综述也纳入
- ⚠ **去重 + 真实性**: 题录须真实可核(DOI/PMID);不得编造文献或数据库

## 4. 输出格式要求
每条线给:
1. **已有关键文献表**: 作者(年) · 刊 · DOI · 一句话核心结论 · 与我方重合度(高/中/低)
2. **Gap 陈述**: 一段话,明确"什么还没被做"
3. **可发表性证据**: 近 2 年同类工作实例(刊 + 频率) → 证明"这类工作发得出去"
4. **裁决**: **go / pivot(给出调整方向) / no-go** + 一句理由
5. 末尾:跨线**综合裁决**与建议的开工顺序

## 5. 已知起点(供深化/证伪,非结论)
前一轮初步 landscape(medium 深度,**需本轮严格核实**)倾向认为:
- 线①: _Aeromonas_ 酶挖掘**疑似空白**(_Vibrio_ 已被 2025 占)——**需确认**
- 线②: **疑似无**水产病原 phage 专门库;PhageScope/INPHARED 通用、不做安全筛查——**需确认**
- 线③: 水产 virome meta-analysis **疑似空白**(fish gut virome 仅个位数);bulk-vs-VLP 是风险——**需确认**
- 综述位: **疑似仍空**——**需确认**
- prophage/anti-phage defense: 2025 *Fish & Shellfish Immunol* 已占首创(已降级,不在本调研主问,可顺带核实)

> 把上述当**待证伪假设**,不要直接采信;本轮的价值正在于用具体文献坐实或推翻它们。
