# 学生 A — onboarding brief: 线① Aeromonas phage 泛基因组 + 杀菌酶系统挖掘

> **状态**: 骨架 v1 (2026-05-29, 待细化) · **学生**: TODO · **导师署名**: 你 lead/通讯 (+ 王高学共同通讯) · **母战略**: `aquaculture-track-record-plan-v1.md`
> **定位**: must-win 线 —— 全 program 最快、最确定、有 Hp3 wet 锚点的一篇,是"至少 1 篇见刊"的保底。
> **开工顺序**: 本线为"第一篇全研究稿",在**综述 + 线② sprint 之后**启动 (DEC-D012);线② 顺产的 curated inventory 是本线泛基因组的输入。

## 一句话目标
从 _Aeromonas_ 噬菌体泛基因组系统挖掘 depolymerase/endolysin 多样性,合成并验证 top 候选,产出一批可用于水产病原防控的 enzybiotics 候选——把 Hp3 (new family) 从"单噬菌体表征"延伸为"Aeromonas phage 抗菌酶资源 + 功能验证"。

## 依赖共享底座
- Aeromonas 子集 (A. hydrophila / salmonicida / veronii phage)
- 底座的酶注释模块 (PhaLP / dbAPIS / 结构预测) 与分类模块 (vConTACT3)

## 数据源
- 底座 Aeromonas phage 基因组集 (NCBI/INPHARED/IMG-VR + Aeromonas 菌基因组的 prophage)
- Hp3 (vB_AhyM_Hp3) 自有基因组作为种子 / 参照

## 分析步骤 (dry pipeline 大纲)
1. 收齐 Aeromonas phage 基因组 → CheckV 质控 → 去冗 (≥95% ANI)
2. 分类:复用**已验证的五法 pipeline**(VIRIDIC genus/species + mash context + TerL ML 树 + ViPTree 全库 proteomic + VICTOR GBDP;完整记录见 pc031 `data/00-raw/d14-taxonomy/TAXONOMY_analysis_log.md`)系统化界定 Aeromonas phage 的 genus/family 边界。**Hp3+HJ05 已由此五法确证为新 genus + putative new family**(ViPTree 全库 5633 refs 中最高 S_G 仅 0.073),线①把它扩成 genus 级 pangenome。⚠ 别主打“first new Aeromonas family”(俄罗斯 Viruses 2025 已提新科 Chimallinviridae);框成 systematic pangenome + enzyme catalog
3. 系统注释 → 锁定 depolymerase / endolysin / holin / spanin
4. 酶多样性(**pan-domain 多家族,非单 motif**): 结构域架构、序列聚类、ESMFold/AlphaFold 结构 + Foldseek 比对已知活性酶。⚠ 必显式引用并超越 EndoA3(Int J Biol Macromol 2025, `10.1016/j.ijbiomac.2025.146934`)已挖的"71 个 M15_C 单 motif peptidase",做跨 Aeromonas + Edwardsiella + Flavobacterium + Photobacterium 多家族挖掘
   - **AI 结构预测暗物质酶挖掘维度** (三方裁决新增): 纯序列法 (BLAST/HMM) 会漏检无可识别 domain 的酶——典型如 Vibrio depolymerase Dep193 无任何可注释 domain。故在序列层之上叠**结构层远缘发现**: ProstT5 (序列→3Di token) + Foldseek 结构搜索 + Phold (结构指导的 phage 蛋白功能注释),对"hypothetical/无 hit"基因做结构聚类与功能赋予,挖出 BLAST 失效的暗物质 depolymerase/endolysin。这是本线相对单酶先例的方法学增量。
5. 候选优选: 多样性代表 + 预测活性 + 跨病原潜力 → top 1–3
6. (验证, 见下) → 回填活性数据做 structure-activity 讨论

## DBTL 验证
- **Build**: 合成伙伴 2 周合成密码子优化基因 (确认长度上限/表达系统)
- **Test**: 表达纯化 → 跨水产病原**裂菌谱** + **酶活** (体外即可, 不做 in vivo)
- 王高学实验室协助菌株 / 表型读出

## 目标期刊
- 主: *Microbiology Spectrum* / *Applied and Environmental Microbiology* / *Int J Biological Macromolecules*
- 备选 (若验证从略): *Viruses* (首决中位 ~17 天)

## 竞品 / 查重 (尽调已核 → `literature-due-diligence-RESULT-v1.md`；onboarding 前再 re-run 因时效性)
- ⛔ **绝对避开 Vibrio**:Vibrio phage 酶挖掘已被 Yue et al. 2026 *AEM* (`10.1128/aem.01824-25`,573 depolymerase 基因,2026-01 发表)占据。
- **Aeromonas 单酶先例**(已发表全是单分离株 / 单酶,**非 genus 级**):BUCT551 (Front Vet Sci 2025, `10.3389/fvets.2025.1679093`)、俄罗斯三联 (Viruses 2025, `10.3390/v17081027`,提新科 Chimallinviridae)、EndoA3 单酶 (Int J Biol Macromol 2025)、Ely174 单酶 (AEM 2025, `10.1128/aem.01891-25`)。
- ⚠ **三方新发现的 Aeromonas 邻近酶竞品**(此前漏列,故"单酶 Aeromonas endolysin"已非空白):LysE endolysin (`10.1007/s12602-021-09880-7`)、**PlyD4** broad-spectrum endolysin 含**斑马鱼体内保护** (`10.1007/s00253-021-11752-7`)、S. iniae prophage endolysin (`10.4014/jmb.2508.08038`)。
- 你的**超越点**(单酶先例已多 → 必须以系统化超越):**genus 级 pangenome + 多家族酶 catalog + AI 结构挖掘** + 选择性功能验证——无人做过。

## 里程碑
- M1 (2026-07): 基因组集 + 泛基因组 + new family 边界
- M2 (2026-08): 酶候选 top 1–3 锁定 → 下合成单
- M3 (2026-09): 验证数据回收
- M4 (2026 Q4): 投稿

## TODO
- [ ] 学生姓名/背景
- [ ] 合成伙伴 build 边界 (基因长度/表达宿主)
- [ ] Aeromonas 子集终稿范围 (是否纳入 Edwardsiella/Flavobacterium 做交叉裂解亮点)
