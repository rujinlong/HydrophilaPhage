# 学生 C — onboarding brief: 线③ 养殖系统 virome + 病原噬菌体 landscape

> **状态**: 骨架 v1 (2026-05-29, 待细化) · **学生**: TODO · **导师署名**: 你 lead/通讯 · **母战略**: `aquaculture-track-record-plan-v1.md`
> **定位**: stretch 线 —— 最贴"水生病毒生态学家" narrative,gap 最大;但方法学风险最高 (bulk vs VLP),失败时降级为线②的一个应用章节。
> **⚠ 已 gating → 降级 (DEC-D013)**: SRA/ENA 实跑盘点证伪"数据充足"假设——水产 **VLP/viral run ≈ 0**、可挖 bulk 仅 ~139 条且非 virome 设计。**本线不作独立全研究稿,降级为线②/综述的 viral-from-bulk 支撑层**(对 ~139 条中国/东南亚 bulk + carp 77 条做 geNomad/VIBRANT 二次挖掘;关键 accession 见 `sprint-NAR-review-line2.md §6`)。坚持 VLP-first 须自测序补数据。下文 pipeline 作支撑层执行,不单独成稿。
> **方法学立场 (三方裁决,改为保守)**: **VLP-first**,或 bulk/VLP **严格分层**(从第一张图就分层呈现) —— 弃"纯 bulk"。依据 Kosmopoulos 2024 *Microbiome* (`10.1186/s40168-024-01905-x`) + Chang 2024 *Comms Biol* (`10.1038/s42003-024-07212-3`):两法捕获的 viral 群落系统性偏倚,VLP-first/分层的审稿防御力远强于纯 bulk。

## 一句话目标
重分析公共 SRA 中**特定养殖系统 (大口黑鲈 / 对虾优先)** 的宏基因组,刻画其 virome landscape 与**病原噬菌体分布**,用共享底座 phage 当 reference,把"水产病害防控"锚点贯穿到生态层。

## 依赖共享底座
- 底座 phage 基因组集作为 **reference** (mapping / 检出养殖环境中的病原噬菌体)
- 同一套 ViroProfiler 注释 pipeline

## 数据源
- **公共 SRA** (鱼/虾肠道宏基因组、养殖水体/底泥宏基因组)
- ⚠ 多为 bulk metagenome 而非 VLP-enriched → 见风险

## 立项前 gating (三方裁决: 决定本线去留的硬动作)
**先做 protocol-aware SRA/ENA dataset 审计** → 给出**实际可用 run 数**(按建库类型 bulk vs VLP-enriched + 宿主/系统分层统计)。决策门: 若存在足量 VLP-enriched 或可严格分层的 run → 全研究稿;**若数据多为记录差的 bulk → 降级为线② DB / 综述的支撑层**,不单独成稿。⚠ 三方都假设"SRA 有数据"但无人实跑 query——此 gating 必须在立项前完成。

## 分析步骤 (dry pipeline)
1. SRA 系统检索 + 元数据整理 (宿主/环境/地理/测序类型) → 明确纳入/排除标准
2. 质控 → assembly (per-sample / co-assembly)
3. viral identification (geNomad / VIBRANT) → CheckV 完整性
4. 聚类成 vOTU → 与底座 reference 比对,标出病原噬菌体
5. 宿主预测 (iPHoP) + 病原-噬菌体互作网络
6. landscape: 多样性 / 优势类群 / 跨系统比较 / ARG 共现

## 验证
- 保持 **dry** (不强塞 wet);如有突出新 phage,可选做实验确认 (与王高学协调,非必须)

## 目标期刊
- 主: *mSystems* / *Environmental Microbiome* / *Animal Microbiome*
- 备选: *ISME Communications*

## 竞品 / 查重 (动笔前再 update)
- gap 大: "fish gut virome aquaculture" 仅检到 1 篇;**无跨研究公共数据 virome 大 meta-analysis** (niche 空白)
- 零散单物种已有 (grass carp DNA virome; Atlantic salmon virome catalogue 2025, `10.1186/s42523-025-00453-5`; 对虾池 `10.3389/fmicb.2022.1011342`; largemouth bass RNA virome `10.1016/j.aquaculture.2024.741571`) → 主养品种 (罗非鱼/对虾/鲤/鲈) + 中国/东南亚养殖带几乎空白
- ⚠ **高重合竞品** (三方最准威胁评估): bioRxiv `2025.10.19.683331` (中山大,水+虾+鱼 metatranscriptome,3211 RNA 病毒)。**避让策略**: 该文走 **RNA-metatranscriptome**,故本线锚 **DNA-phage** + **中国主养种**,与其正面错开。
- **方法学黄金类比** (证明此类公共数据 meta-analysis 可发表): Rey-Campos 2023 软体动物公共 SRA virome meta-analysis (`10.3389/fmars.2023.1209103`) —— 论文设计直接对标。

## 风险 (必须正面处理)
- **bulk vs VLP**: 已采 **VLP-first / 严格分层**立场 (见顶部);仍须在方法与讨论显式界定 viral signal 的可靠性边界,绝不把 bulk 与 VLP 信号混并,否则被批
- 数据异质性 (测序平台/深度/建库) → 标准化 + 敏感性分析
- 失败 fallback: 降级为线② web 平台的"养殖环境应用案例"模块

## 里程碑
- M1 (2026-07): SRA 纳入清单 + 标准冻结
- M2 (2026-09): vOTU catalogue + 病原噬菌体检出
- M3 (2026-12): landscape 分析完成
- M4 (2027 Q1): 投稿

## TODO
- [ ] 学生姓名/背景
- [ ] 优先养殖系统定 1–2 个 (建议大口黑鲈,与 Hp3/王高学呼应)
- [ ] 是否纳入自有/王高学未公开测序数据 (增独家性)
