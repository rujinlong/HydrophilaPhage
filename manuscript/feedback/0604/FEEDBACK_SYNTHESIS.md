# 0604 合作者投稿前反馈：提取 · 关联 · 整合评估

> 状态：已核实 ✅（PDF 标注 + 源文件 + Phold 全注释三方交叉验证完成，2026-06-04）
> 三位合作者：**liang**（PDF 批注）、**chen**（PDF 高亮 + txt 行号备注）、**xue**（txt 机理建议）
> 提取方式：PyMuPDF 提取 PDF annotation（FreeText 批注 + Highlight 覆盖文本），与 txt 备注按行号/语义关联。

---

## 0. 反馈来源清单

| 合作者 | 文件 | 形式 | 条目数 |
|---|---|---|---|
| liang | `manuscript-feedback-liang2.pdf` | 2 条 FreeText 边注 + 2 处 Highlight | 3 个实质问题 |
| chen | `manuscript_highlighted-chen.pdf` | 22 处 Highlight（无 popup，备注在 txt） | — |
| chen | `supplementary_highlighted-chen.pdf` | 1 处 Highlight | 1 |
| chen | `修正建议-chen.txt` | 按**行号**定位的逐条修正 | 21 条 |
| xue | `feedback-xue.txt` | 针对全文的**机理层面**整体建议 | 1 大项（含 3 推测 + 2 图文建议）|

**关键关联**：chen 的高亮本身**无 popup 文字**，真正的修改意见全在 `修正建议-chen.txt`，靠**行号**定位。下表已把"行号备注 ↔ PDF 高亮原文"对齐，确保每条意见都锚定到具体句子。

---

## A. chen 的逐条语言/格式修正（行号 ↔ 高亮 ↔ 评估）

> 类型标记：【语法】【拼写】【格式】【表达/AI痕迹】

| # | 行 | 高亮原文（PDF 实测） | chen 建议 | 类型 | 我的评估 |
|---|---|---|---|---|---|
| A1 | 86 | `Determination of optimal Multiplicity of Infection (MOI)` | optimal→**O**ptimal（标题 title case） | 格式 | ✅ 接受（标题词首大写）|
| A2 | 87 | `was prepared as the test concentration.` | `as`→`at` the test concentration | 表达 | ⚠️ 见正文：建议整句重写，"test concentration" 指代不清 |
| A3 | 88 | `MOI of 0.001, 0.01, 0.1, 1.0, 10, 100, and 1000` | 多个值→**MOIs** | 语法 | ✅ 接受（liang 同提）|
| A4 | 95 | `The one-step growth curve was performed` | curve 不搭配 perform→`A one-step growth assay was performed` | 表达 | ✅ 接受 |
| A5 | 112 | `manufacturer instructions.` / `Nanodrop` | `manufacturer's instructions`；`NanoDrop` | 格式/拼写 | ✅ 接受（NanoDrop 为商标正确写法）|
| A6 | 152 | `The LD50  calculated` | 缺 be→`The LD50 was calculated` | 语法 | ✅ 接受 |
| A7 | 156 | `a phage Hp3 suspension` | →`an Hp3 phage suspension` 或 `a suspension of phage Hp3` | 表达 | ✅ 接受（后者更规范）|
| A8 | 169 | `sliced (3 μm)` | →`sectioned at 3 μm` | 表达 | ✅ 接受（组织学规范用 sectioned）|
| A9 | 172–175 | `...reported with reference to the ARRIVE guidelines..., with unresolved reporting limitations for power calcu...` | 双重 with，**AI 痕迹明显** | 表达/**AI痕迹** | ✅ 接受：拆句重写（详见 §E）|
| A10 | 190 | `Hp3 forms single round, small,` | 形容词语序+时态+with no→`Hp3 formed small, round, transparent plaques without...` | 表达 | ✅ 接受 |
| A11 | 192–193 | `the tail length is about 143 nm, and the width is about 23 nm.` | 多次 is about→`the tail was approximately 143 nm long and 23 nm wide` | 表达 | ✅ 接受 |
| A12 | 197 | `Temperature and pH` | 标题→`Temperatures and pH Values` | 格式 | ✅ 接受 |
| A13 | 201 | `set 7 MOIs` | →`Seven MOIs were tested`（被动）| 表达 | ✅ 接受 |
| A14 | 202 | `MOI=1.0,` | 等号两边加空格→`MOI = 1.0` | 格式 | ✅ 接受 |
| A15 | 224 | `with MOI` | 同样→MOIs？ | 语法 | ⚠️ 需看上下文：若指多个值则 MOIs |
| A16 | Fig.3 | `five MOI va...` / `...were incubated with the control group` | five 首句大写；**"incubated with the control group" 是和对照组一起孵育吗？** | 表达/**逻辑** | 🔴 **实质问题**（liang 同提）见 §C |
| A17 | 全文 | `p <` | 全文 **P** 大写斜体（P value）| 格式 | ✅ 接受（Cell Press 要求斜体 *P*）|
| A18 | 302 | `dosing and timeframe conditions.` | 表达→`under this dose and observation period` | 表达 | ✅ 接受（措辞更准）|
| A19 | 375 | （无高亮，纯 txt）`analysed` | →`analyzed`（全文统一）| 拼写 | ✅ 接受（确认全文用美式拼写）|
| A20 | S-Fig.S2 | `) grouped by`（supplementary）| `The 105 predicted ORFs **were** grouped by` | 语法 | ✅ 接受 |

---

## B. liang 的批注（边注 + 高亮）

| # | 页 | 形式 | 原文/批注 | 我的评估 |
|---|---|---|---|---|
| B1 | p2 | FreeText | "**ph错误，应该是6-9**" | 🔴 **数据/事实问题**：需核对原文 pH 稳定范围与 21-figs.qmd 实测数据是否一致，见 §C |
| B2 | p4 | Highlight `MOI` + FreeText | "这个要加复数吗 MOIs" | ✅ 同 A3，接受 |
| B3 | p10 | Highlight 整句 + FreeText | 高亮：`five MOI values (0.01, 0.1, 1.0, 10 and 100) were incubated with the control group at 37°C.`；批注："这句话感觉怪怪的。应该是5个浓度的感染复数的噬菌体hp3与嗜水气单胞菌培养液混合培养" | 🔴 **实质问题**，与 A16 同指一句，见 §C |

---

## C. 多人重合 / 实质性问题（最高优先级）

### C1. Figure 3 legend "incubated with the control group" —— liang(B3) + chen(A16) 双人指出 🔴 已核实
- **源文件位置**：`body-cr.tex:241–242`（lysis-curve legend）；正文 `body-cr.tex:222` 已正确写 "All five MOIs suppressed bacterial density"。
- **现状 legend**：`...Hp3. five MOI values (0.01, 0.1, 1.0, 10 and 100) were incubated with the control group at 37°C`
- **问题确认**：legend 字面"5 个 MOI **与对照组**孵育"逻辑不通；错只在 **legend**，正文逻辑无误。liang 的理解正确：应是噬菌体以 5 个 MOI 与菌液共培养。
- **建议改法**：`Five MOIs (0.01, 0.1, 1.0, 10, and 100) of phage Hp3 were co-cultured with A. hydrophila at 37 °C; the control received bacteria without phage.`（Five 首字母大写；明确孵育对象=噬菌体+菌液；对照=不加噬菌体）
- **裁决**：✅ 接受，重写 legend（body-cr.tex + body.tex 对应 legend 同步）。

### C2. pH 范围 —— liang(B1) 🟡 已核实：数据正确，属"措辞明确化"非"纠错"
- **核实结果**：两版 PDF 的 results 段**都**写 "stable ... pH values from 6.0 to 9.0"（CR p546 / MJS p543），与实测一致 → **数据没错**（pH 10 一个 log 下降；<5、>11 完全失活）。
- **liang 批注落点**：CR 版 **Summary**（p2），那里只笼统写 "pH ranges typical of aquaculture"，**无数字**。
- **重新判断**：liang 不是说写错，而是希望明确范围。另注意正文另有"养殖水体 pH 6.8–8.0"（环境条件，≠稳定性，勿混淆）。
- **建议改法**：Summary 把 "across the temperature and pH ranges typical of aquaculture" → "across a broad temperature range and pH 6–9"。
- **裁决**：✅ 接受（Summary 措辞明确化）；results 数据保持 6–9 不动。

### C3. MOI → MOIs —— liang(B2) + chen(A3, A15) 双人指出
- ✅ 接受。全文统一：单数概念用 MOI，列举多个值用 MOIs（正文 222 行已用 MOIs，主要修 methods/legend）。

---

## D. xue 的机理建议（系统评估）—— 已用 Phold 全注释核实 ⚠️ 重要裁决

> xue 方向：把论文从"杀菌描述"升级到"机理解释"，尤其解释**抗性快速涌现（222/229 行）vs 存活率 15%→85%** 的表观矛盾。**方向高度正确**。
> 但 xue 假设的两个分子载体，经 Hp3 全基因组注释（Phold/Pharokka，**105 CDS**）核查：

**Hp3 注释事实（决定性）**：
- tail fiber protein：**仅 1 个**（hp3_CDS_0055）；tail 类共 13 个结构蛋白
- lysis cassette：2 holin（hp3_0069/0099）+ 1 amidase endolysin（hp3_0070）— 真实，可强调
- ❌ **无 depolymerase 注释**　❌ **无 Ig-like / immunoglobulin domain**　❌ **无 adhesin**
- 50/105（48%）为 hypothetical / unknown function
- 唯一 VFDB 命中 hp3_0022（16% identity）正文已判为假阳性

| # | xue 建议 | Hp3 证据现状 | 裁决 |
|---|---|---|---|
| D1 致病位点（皮肤/肠道）| 文献性，不依赖 Hp3 注释 | ✅ discussion 可补（引文）|
| D2 游离菌 vs biofilm | 文献性；intro 27 行已提 biofilm | ✅ discussion 可补 |
| **D3a depolymerase 干扰 biofilm** | ❌ **无 depolymerase 注释**；仅 1 个未分域 tail fiber | ⛔ **不能作机理写入**。可选：补 domain 分析（dbCAN/InterPro 查 tail fiber 是否含 pectin-lyase-like/解聚酶 fold）再定；否则仅 future work + caveat |
| **D3b Ig-like domain 增强免疫/粘附粘液** | ❌ **完全无 Ig-like 注释** | ⛔ **不写**。无任何证据；除非单独跑 Pfam Big_2/I-set 检测 |
| D3c 抗性突变→毒力减弱（进化权衡）| 纯文献推测，本研究无数据；但能解释 222/229 行矛盾 | ✅ **采纳为 discussion 主线解释**，文献支持 + 明确标"推测"，不可当结论 |
| D4 基因组图突出功能基因 + 结构 | lysis cassette/tail fiber/复制系统真实可标；depolymerase/adhesin 标不出 | 🟡 部分接受：突出**真实注释**模块，勿臆造 |
| D5 discussion 重写机理 | — | ✅ 以 D3c 为主线，D1/D2 铺背景，D3a/b 降级为 future work |

**核心判断给用户**：xue 的科学直觉对（论文确实缺机理），但他设想的两个分子机制（depolymerase、Ig-like domain）**在 Hp3 基因组里没有注释证据支撑**。诚实且稳妥的落地：
1. 用 **D3c（抗性-毒力权衡）** 作为解释存活率矛盾的主线（有文献、能自洽）；
2. depolymerase 若要保留，**先补 domain 级分析**验证 tail fiber 是否携带解聚酶折叠，再决定写不写；
3. Ig-like domain 不纳入（或仅 future work 一句带过）；
4. 基因组图突出**真实存在**的功能模块（lysis cassette / tail fiber / 复制系统）。

这样既尊重 xue 的洞见，又不把无证据的分子机制写进论文（避免审稿人质疑）。

### D-追问. 针对用户两个追问的核查结论（基因组注释 + 文献双重核实）

**追问①：Ig-like domain 是噬菌体带还是 A. hydrophila 带的？**
- xue 原文明确指**噬菌体**携带 Ig-like domain 粘附鱼体粘液 → 即 **BAM 模型**（Bacteriophage Adherence to Mucus），文献充分：Barr 2013 PNAS [@2013-Bacteriophage_Barr]、Fraser 2006 JMB [@2006-IgLike_Fraser]/2007 [@2007-Immunoglobulinlike_Fraser]、**Wu 2024 Nat Commun [@2024-Bacteriophage_Wu]**（phage Hoc 蛋白 Ig-like domain 结合肠道 MUC2 粘液、增强 phage 治疗持留）。→ **xue 的假设有文献依据，非凭空**。
- **但 Hp3 注释无显式 Hoc/Ig-like domain**。Hp3 是 T4-like myovirus（baseplate + tail sheath + UvsX 重组系统），而 T4 的 Hoc/Soc capsid 蛋白正是 Ig-like domain 经典载体 → Hp3 **有可能**有，需 domain 检测确认。候选：hp3_CDS_0096（**913aa** virion structural，异常大）、hp3_CDS_0054（**640aa** baseplate wedge，结构占比不纯 tail=0.566）。
- A. hydrophila 自身的 Ig-like/adhesin（Tad pili、T4P [@2024-Tad_Tekedar]）是**细菌毒力因子**（助菌粘附+成 biofilm），方向相反，不是噬菌体保护机制 → 讨论噬菌体治疗机理应聚焦**噬菌体** domain。

**追问②：A. hydrophila 是否形成 biofilm？Hp3 是否有其它 biofilm 降解基因？**
- ✅ **A. hydrophila 确证形成 biofilm**，且 biofilm 是毒力/持留因子：Tad pili 敲除显著降低 biofilm + 毒力 [@2024-Tad_Tekedar]；毒力综述 [@2016-Virulence_Rasmussen-Ivey, @2023-Whole_Abdella]。
- Hp3 **无显式 EPS depolymerase**，但：
  - **tail fiber hp3_CDS_0055（406aa）是 depolymerase 的经典载体** —— phage tail fiber 常兼具 depolymerase 活性降解荚膜/biofilm：Wu 2019 [@2019-Novel_Wu]（tail fiber Dep42 降解 Klebsiella 荚膜+biofilm）、Pires 2016 [@2016-Bacteriophageencoded_Pires]（多数 depolymerase 即 tail fiber/spike）。
  - endolysin（amidase hp3_0070）降解肽聚糖（裂菌），非 EPS depolymerase。
  - depolymerase 去荚膜可**降低毒力 + 致敏免疫** [@2015-Phage_Maszewska, @2021-BacteriophageDerived_Topka-Bielecka] —— 与 xue 的"毒力减弱"逻辑自洽。

**核心判断**：xue 的两个机制在**文献上都成立**，A. hydrophila 形成 biofilm 也确证。唯一缺的是 **Hp3 自身这两个 domain 的直接证据**（tail fiber 作为 depolymerase 候选载体是间接支持；Ig-like 无线索）。两条路：
- **(b 推荐) 先验证**：跑 domain 检测（InterProScan 或 hmmscan + Pfam[Ig: Big_2/I-set/fn3] + dbCAN[CAZy/depolymerase]），针对 hp3_CDS_0054/0055/0096 等结构蛋白。检出 → 写成有据机理 + 基因组图标注（满足 D4），强力提升论文；未检出 → discussion 只走"抗性-毒力权衡"主线，depolymerase 降为 future work。
- **(a) 不验证**：直接以"tail fiber 可能携带 depolymerase 活性"作**假设/future work** 写入，引文献支撑普适性，明确标注未验证。
- ⚠️ 本地无 Pfam/dbCAN DB，路 (b) 需先下载数据库（dbCAN ~50MB 较轻；Pfam ~1.5GB）。

### D-验证. Pfam-A 全库检测结果（2026-06-04）——双阴性 ⛔

> dbCAN 官方库已下线（UNL 迁移 + WAF 封锁 + 镜像失效），改用 **Pfam-A 全库** hmmscan（`-E 0.01`，比 GA 阈值更松以免漏远同源），Hp3 105 蛋白共 84 个 domain 命中。

**结论 A — depolymerase：无**
- 全基因组**无** Pectate_lyase / Glyco_hydro / Sialidase / polysaccharide lyase / CBM 等 EPS/荚膜降解家族
- 唯一 peptidase 命中 `hp3_CDS_0039` = Peptidase_S78（**phage prohead 成熟蛋白酶**，非 depolymerase）
- endolysin `hp3_CDS_0070` = Amidase_2 + PG_binding（**肽聚糖 amidase 裂菌**，非 EPS depolymerase）

**结论 B — Ig-like domain：无**
- 全基因组**无** Big_2 / I-set / fn3 / He_PIG / Ig 任何命中

**三个候选载体蛋白的 domain 构成**：
- tail fiber `hp3_CDS_0055`（406aa）：**Pfam 零命中**（novel；无 depolymerase 也无 Ig）
- baseplate wedge `hp3_CDS_0054`（640aa）：仅 DUF4815（baseplate 结构 domain，非酶）
- virion structural `hp3_CDS_0096`（913aa）：**Pfam 零命中**（novel）

**双重证据**：Pfam（序列同源）+ phold（结构 foldseek，前已查）**双阴性** → Hp3 无 depolymerase / Ig-like 的证据相当强。
**Caveat**：tail fiber 0055 与 0096 是 novel 蛋白（Pfam 无注释），活性理论上可能藏于 novel 序列、序列法测不到；100% 排除需 AlphaFold + Foldseek 查 depolymerase fold（β-helix / pectin-lyase），属更深可选分析。

**最终裁决（xue 机理）**：
- D3a depolymerase / D3b Ig-like：**无 Hp3 证据 → 不写入机理**；至多作 future work（"novel 结构蛋白功能待结构验证"，且呼应论文 'highly distinct genus' 新颖性）
- D3c 抗性-毒力权衡：**作 discussion 主线**（文献支撑、解释存活率矛盾、不依赖缺失的 domain）
- 可正面强调的真实机制：完整 lysis cassette（2 holin + Amidase_2 endolysin）

### D-验证（续，2026-06-04）. InterProScan + MMseqs2 正交确认 → 四重阴性

**InterProScan 全库**（Pfam+CDD+SMART+PROSITE+PANTHER + **Gene3D/SUPERFAMILY fold-level**；EBI iprscan5 REST，不绕 interpro-database skill——后者需 UniProt accession，对 novel phage 蛋白不适用）：
- `0048` baseplate spike：**Vgr/Gp5 OB-fold injector**（PF04717 + Gene3D OB-fold）— 穿刺装置，非降解酶
- `0054`：仅 DUF4815
- `0055` tail fiber：**0 命中**（真 novel，连 fold 都无）
- `0096` 913aa：**0 domain**（仅 MobiDBLite disorder）
- → 连 fold-level（depolymerase β-helix / Ig β-sandwich）都无命中，比纯 Pfam 更强的阴性

**MMseqs2 同源**（ColabFold，1544 UniRef hits；top 主要是 0054 DUF4815 的细菌同源）：同源全是 **DUF4815 baseplate wedge + Toxin subunit YenA2（eCIS 收缩注射系统结构组分）+ phage structural**，关键词 tally **无 depolymerase/lyase/Ig/adhesin**。附带提示：Hp3 baseplate/tail 同源到 eCIS/Yen-Tc，印证其**收缩性尾部穿刺递送**机制（Myovirus 特征），而非降解。

**四重正交阴性汇总**：

| 方法 | 层面 | depolymerase | Ig-like |
|---|---|---|---|
| Pfam 全库 | 序列 HMM | ❌ | ❌ |
| InterProScan | 多库 + Gene3D/SUPERFAMILY **fold** | ❌ | ❌ |
| phold | 结构 foldseek | ❌ | ❌ |
| MMseqs2 | 序列同源功能 | ❌（同源皆 structural）| ❌ |

→ **Hp3 没有可检测的 depolymerase / Ig-like domain，证据已达四重正交。** 仅剩用户在跑的 AlphaFold + Foldseek（真结构）作最终确认（大概率一致阴性）。novel 蛋白 `0055`/`0096` 的"暗物质"特性恰好呼应论文 "highly distinct unclassified genus" 卖点。

### D-验证（终）. AlphaFold + Foldseek 真结构 → 五重判定 + Discussion 落地 ✅

**AlphaFold Server**（`vpipe parse alphafold` 批量 JSON）→ best-model cif（pTM）：0055 tail fiber **0.78**、0054 0.60、0048 0.38、0096 0.17。
**Foldseek**（foldseek-structural-search skill，pdb100+BFVD+afdb50）：
- 0055/0054 主体压倒性同源 **DUF4815 / baseplate-tail structural**（E e-71~e-28）
- ⚠️ **假阳性核查**：0055 唯一 Glycosyl hydrolase 命中（292 中 1，seq id 23%，Fragment）= 噪音；0054 的 32 个 SGNH/GDSL 是弱命中（E e-06，比主命中弱 60+ 量级，SGNH=酯酶非经典 depolymerase）→ **不构成 depolymerase 证据**（差点误判，核查排名后否定）
- Ig-like：0055 确含 Ig-like/fn3 fold（cov 90%+），但属 tail fiber 通用结构支架（BAM 结构基础），功能未证

**五重正交终判**：depolymerase **五重阴性**（foldseek 零星命中=噪音）；Ig-like **结构上存在、功能未证**。

**Discussion 改动**（body.tex + body-cr.tex 同步，latexmk exit 0 验证）：
1. 抗性-毒力权衡（`@2015-Virulence_Leon`）作 immunophage synergy 的**互补**机理，解释 15%→85% 矛盾；明确两机制均"inferred rather than demonstrated"+ 给验证方向（CFU/g + 抗性株毒力）
2. 新增"分子机制 future work"段：tail fiber `0055`/`0096` novel（呼应 distinct genus）+ Ig-like/BAM（`@2013-Bacteriophage_Barr` `@2006-IgLike_Fraser` `@2024-Bacteriophage_Wu`，谨慎）+ depolymerase（`@2016-Bacteriophageencoded_Pires` `@2023-Potential_Guo`，标"weak, unconfirmed signals"）+ A. hydrophila biofilm（`@2024-Tad_Tekedar`）—— 全部 testable hypotheses，不夸大

**xue 的反馈最终落地**：方向（机理）✅采纳；depolymerase/Ig-like ✅作 future work（诚实，五重验证支撑"未确证"）；致病/biofilm 背景 ✅补入。

---

## E. AI 痕迹清单（用户特别关注）

chen 明确点名 1 处，其余"表达不自然"类高度疑似 AI 腔，建议 `de-ai-academic-prose` 复核：

| 位置 | 源文件落点 | 现象 | AI 痕迹特征 |
|---|---|---|---|
| 172–175（A9）| body.tex:246 / star_methods.tex:101 | 双重 with：`...with reference to the ARRIVE guidelines..., with unresolved reporting limitations...` | chen **明确标注 AI 痕迹**；同句叠用介词短语，建议拆句 |
| 87, 95, 156, 169, 190, 192–193, 302 | Methods/Results | chen 标"表达不自然" | 中式英语 / AI 冗余措辞 |

> 建议：本轮逐条修语言后，对 Methods+Results 整体跑一遍 `/de-ai-academic-prose`。

---

## F. 给用户的建议与待讨论项

**A. 可直接接受（语言/格式，低风险，批量改）**：A1, A3–A14, A17–A20, B2 —— ~18 条纯语言修正，需在 **body.tex / body-cr.tex / star_methods.tex** 三处同步。

**B. 实质问题（已核实，待你确认改法）**：
1. **C1** Fig.3 legend 重写（孵育对象 + 对照定义）—— 已给改法，建议接受。
2. **C2** pH：数据没错；仅把 Summary 措辞明确为 "pH 6–9" —— 建议接受。
3. **A9** ARRIVE 双重 with 拆句（AI 痕迹）—— 建议接受。

**C. 需你拍板的方向性决策（xue 机理建议）**：
1. **D3c 抗性-毒力权衡**作主线写入 discussion？（推荐：是）
2. **depolymerase（D3a）**：(a) 不写 / (b) 仅 future work / (c) 我先跑 domain 分析（dbCAN/InterProScan on hp3_CDS_0055）验证后再定？← 需你选
3. **Ig-like（D3b）**：建议不写（无证据）。是否同意？
4. 是否要我据此**重写 discussion 段**并跑一遍 `de-ai-academic-prose`？

**版本同步提醒**：chen 审 MJS 版（`body.tex`，methods-first），liang 审 CR 版（`manuscript-cr.tex`）。任何语言修改需在 **body.tex + body-cr.tex + star_methods.tex** 三处保持一致（CLAUDE.md 要求）。

---

## G. 改稿执行状态 — 2026-06-04 已完成并 git diff 验证 ✅

**改动文件（5）**：`body.tex` / `body-cr.tex` / `star_methods.tex` / `manuscript-cr.tex` / `supplementary/supplementary.tex`

**语言/格式（chen + liang）全部已改并验证**：
- R1 plaques 时态+语序 / R2 tail 尺寸 / R3 标题 "Temperatures and pH Values" / R4 "seven MOIs … were tested" / R5 "MOI = 1.0" / R6 "this dose and observation period" / R7 analysed→analyzed（全文统一美式）
- M1 bacterial host / M2 MOIs of / M3 one-step assay / M4 manufacturer's / M5 NanoDrop / M7 suspension of phage Hp3 / M8 sectioned at 3 μm
- A20 / S-Fig.S2 "were grouped by"（`supplementary.tex:102`）
- **P 值全部斜体大写**（文本 `\textit{P}`、数学 `P`）— ⚠️ agent 漏做，已由我补全；验证：无遗漏、未误伤 pH/PFU

**实质问题已改并验证**：
- C1 Fig.3 legend 重写："Five MOIs … of phage Hp3 were co-cultured with *A. hydrophila*; the control received bacteria without phage"（`body-cr.tex:242` + `body.tex:459`）
- C2 Summary 明确 "pH 6–9"（`manuscript-cr.tex:153`）；**results 段 6.0–9.0 数据未动**（已核验）
- A9 ARRIVE 双重 with 拆两句（`body.tex:246-247` + `star_methods.tex:101`）

**修正合作者误判（CLAUDE.md：reviewer flag 先验证）**：
- M6（chen 第 152 行）：chen 称 "LD50 calculated … was" 缺 be。实际原句是后置定语（语法成立），直接加 `was` 会造成 "was calculated … was" 双 was 错误。**正确改法 = 加逗号**："The LD50, calculated using the modified Käber method, was …"

**待你决策（未改）**：
- ⏸️ D（xue 机理 discussion）：取决于 domain 检测结果
- ⏸️ domain 检测（dbCAN/Pfam on `hp3_CDS_0054/0055/0096`）：待确认是否跑（本地需下载 DB）

**收尾 checklist（改完 discussion 后）**：
1. domain 检测方向 → discussion 深度
2. `/de-ai-academic-prose` 复检 Methods+Results
3. `latexmk manuscript-cr.tex` 渲染确认无 LaTeX 报错（P 斜体 / 拆句改动）
4. `/verify-refs` 验证新增文献引用
