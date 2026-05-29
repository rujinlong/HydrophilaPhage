# 三方 DeepResearch 交叉验证 — program 尽调最终裁决

> 三方 = Claude(deep-research workflow,真实 DOI + 对抗式验证)/ Gemini DeepResearch / ChatGPT DeepResearch。
> 来源:`literature-due-diligence-RESULT-v1.md`(Claude)+ `lit-review/gemini-*.md` + `lit-review/chatgpt-*.md`。日期 2026-05-29。
> **总裁决:三线 + 综述位全部 GO,无一 no-go;全部带 pivot/约束。立项前两个硬动作:实跑 SRA 盘点(线③)、NAR 7/1 日历倒排(线②)。**

## 裁决一致性总表
| | 裁决 | 三方一致度 |
|---|---|---|
| 线① Aeromonas 泛基因组+酶挖掘 | **GO-with-PIVOT** | 高(均不 no-go) |
| 线② 安全筛查/设计 DB(web) | **GO**(最强 novelty) | 三方一致 |
| 线③ 养殖 virome landscape | **GO-with-PIVOT** | 二对一(pivot 方向分歧) |
| 综述位 资源/生信/DBTL | **GO** | 三方一致 |

## 逐线关键(尤其多引擎相对 Claude 第一轮的新增)
### 线① — GO-with-PIVOT
- 三方一致:Aeromonas phage 文献碎片化、无 genus 级 pangenome 专文;Vibrio 酶挖掘已被占(`10.1128/aem.01824-25`)→ 锚 Aeromonas;可发表性强。
- **ChatGPT 补我漏的 Aeromonas 邻近酶竞品**:LysE endolysin(`10.1007/s12602-021-09880-7`)、**PlyD4**(`10.1007/s00253-021-11752-7`,含斑马鱼体内保护)、S. iniae prophage endolysin(`10.4014/jmb.2508.08038`)→ "Aeromonas 酶全空白"判断**偏松**,但不改 go。
- **Gemini+ChatGPT 方法学新刀**:走 **AI 结构预测(Foldseek/Phold/ProstT5)暗物质酶挖掘**,绕开 BLAST 失效(Dep193 无可识别 domain)+ 已发表单酶先例。
- **pivot**:别主打"first new Aeromonas family"(Chimallinviridae 已占);框成 pangenome + 多家族酶 catalog + **AI 结构挖掘** + 选择性验证;跨 Aeromonas/Edwardsiella/Flavobacterium/Photobacterium;**避 Vibrio**。

### 线② — GO(最强,三方一致)
- 三方一致:无水产 host 切分的治疗设计 DB = 最干净 novelty;PhageScope/Sphae 是上游 primitive 非竞品。
- **ChatGPT 补竞品矩阵**:IMG/VR v4、PhagesDB、PhageDive(NAR 2025)、PhageLeads、FVD(水产病毒 DB 但非 phage/治疗向)。
- **Gemini 加"设计层"竞品**:Prophage Activation 平台、CRISPR-avoidant phage 管线 → DB 须含 safe-phage **逆向工程设计层**(溶原模块切除靶点),不止筛查。
- **硬约束(ChatGPT)**:NAR Database **7/1 pre-submission + 8/15 稿 + 站点免登录全功能**。否则先投 *Database*(Oxford)/*Scientific Data*。

### 线③ — GO-with-PIVOT(二对一,pivot 方向分歧)
- 三方一致:有零散单点、**无跨研究公共 SRA meta-analysis(niche 空白)**;bulk-vs-VLP 是审稿命门。
- **分歧(实质)**:Claude=纯 bulk DNA-phage 可行(Spectrum `10.1128/spectrum.00013-25` 两法互补);**ChatGPT 反驳→ VLP-first**(补 Kosmopoulos 2024 *Microbiome* `10.1186/s40168-024-01905-x` + Chang 2024 *Comms Biol* `10.1038/s42003-024-07212-3`);Gemini=bulk/VLP 协方差校正。**建议从保守(VLP-first 或从第一张图就 bulk/VLP 分层)**。
- 竞品:Claude 独家高重合竞品 bioRxiv `2025.10.19.683331`(中山大,水+虾+鱼 metatranscriptome,3211 RNA 病毒;Claude 威胁评估最准);ChatGPT 补 landscape 竞品(对虾池 `10.3389/fmicb.2022.1011342`、Atlantic salmon catalogue `10.1186/s42523-025-00453-5`、largemouth bass RNA virome `10.1016/j.aquaculture.2024.741571`)+ **方法学黄金类比 Rey-Campos 2023 软体动物公共 SRA virome meta-analysis `10.3389/fmars.2023.1209103`**(证明此类可发表)。
- **pivot**:DNA-phage landscape + 公共 SRA 重分析 + 中国主养种(避开 RNA-metatranscriptome 单点竞品)+ **VLP-first/分层**;**先做 protocol-aware dataset 审计**(ChatGPT gating)。

### 综述位 — GO(三方一致)
- "疗效+实施"综述位已满(Claude:F&F 2026 `10.1111/faf.70055`;ChatGPT 补 Yang 2024 `10.1016/j.aquaculture.2024.740925`、Albarella 2025、Landor 2026 `10.1016/j.tim.2025.08.002`);"**资源+计算+安全筛查+酶挖掘+DBTL 设计**"视角仍空。零湿实验、软启动、插旗。

## 开工顺序(收敛:采纳 ChatGPT/Gemini 而非 Claude 的"线①先")
1. **综述 + 线② feasibility sprint 即刻并行**(综述零成本插旗;NAR 7/1 倒逼;线② sprint 顺产线①需要的 curated inventory)
2. **线① 第一篇全研究稿**(pangenome + AI 结构酶挖掘 + 选择性验证,锚 Hp3)
3. **线③ 最后**,先 protocol-aware SRA 审计,定 VLP-first/分层

## 三方都未覆盖的盲区(立项前必处理)
1. **学生能力 vs 线难度匹配**:线② web server(前后端+API+维护)工程量远超①③,对学生隐藏高风险——分配要匹配。
2. **数据可得性硬核查**:三方都说线③"SRA 有数据"但无人实跑 query 给可用 run 数。**立项前必须实跑 SRA/ENA 盘点**。
3. **政策/法规对接**:818 号令水产走农业农村部新兽药路径,三方全未触及(与 novelty 无关但影响 program 叙事)。

## 待亲核(三方分歧项)
- **已澄清**:P19 论文 DOI 三方互斥,是 ChatGPT/Gemini 把 Hp3 误关联到不相关的 P19 jumbo phage 论文;**Hp3 = SSRN ssrn.5897348 = GenBank PX754746**,Claude 已用 manuscript 正文核实,确定无误。
- Vibrio depolymerase 作者标注分歧(Yue vs Zhao,DOI 同为 `10.1128/aem.01824-25`)——不影响"Vibrio 已封堵"结论,投稿引用前核作者即可。
