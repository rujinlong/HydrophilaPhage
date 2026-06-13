# Hp3 Phage-Encoded Enzyme — Enzybiotic 合成与体外验证方案（草案）

> **状态**：草案 v0.1（2026-06-05）· 基于 `vB_AhyM_Hp3` 已有注释起草 · 服务 Deng Lab × GCATbio × Geist × 王高学 合作
> **一句话**：把已表征但「只有整噬菌体 in-vivo 救鱼数据、缺单酶 in-vitro 活性」的 Hp3，通过 **GCATbio 合成其 lysis-cassette 酶 → cell-free 表达 → 体外活性筛选** 补上 enzybiotic 数据——**全程不碰活鱼**，正好契合 Geist 水产设施翻修期。

---

## 1 · 背景与机会

**Hp3 现状**（来自 pc031-aquaPhage / manuscript-cr.tex）：
- 基因组 84,750 bp · GC 59% · 105 CDS · 严格裂解性（BACPHLIP 0.97，无 integrase/CI）· 新属（与 *Aeromonas* phage HJ05 同属，putative new family）· GenBank **PX754746.1**
- 已有数据：one-step growth / 稳定性 / MOI / **in-vivo efficacy（largemouth bass 存活 15%→85%）**
- 稿件：Cell Reports（主投）→ Microbial Biotechnology → Fish & Shellfish Immunology；通讯作者 **Li Deng · 王高学 Gaoxue Wang · Jinlong Ru**

**核心 gap（机会所在）**：稿件**没有任何单个 phage-encoded enzyme 的 in-vitro 活性数据**——所有酶（endolysin/holin/tail fiber）仅停在序列+结构注释。补上这块 = 把 Hp3 从「一个噬菌体的故事」升级为「一个可复用 enzybiotic 平台的起点」。

**三方就绪**（这是为什么现在可做）：
| 角色 | 提供 | 就绪度 |
|---|---|---|
| Deng Lab / Jinlong | Hp3 注释 + 方案设计 + AI/in-silico + 数据分析 | ✅ 已有 |
| **GCATbio**（华大新一产/BGI） | ORF 合成（mMPS）+ cell-free TXTL + mg-Kg 蛋白生产 | ✅ 能力对口 |
| **Geist**（TUM Aquatic Systems Biology） | **A. hydrophila 培养物**（含其设施的，2026-06 邮件确认）| ✅ isolate 可得 |
| **王高学**（西农） | in-vivo 鱼病模型 + 鱼用疫苗 + 中草药抗菌（TCM 角度）| ✅ 已是 Hp3 通讯作者 |

**时机**：Geist 设施翻修今年 in-vivo 受限 → **本方案刻意全程 in-vitro / cell-free，不依赖任何活体设施**，把约束变成"正好今年做酶平台"的理由。

---

## 2 · 候选酶清单（基于 Hp3 真实注释，诚实标注边界）

| 优先级 | 基因 | 坐标 | aa | 注释 / 依据 | enzybiotic 角色 |
|---|---|---|---|---|---|
| **⭐⭐⭐ Tier 1** | **`hp3_0070`** | 50837–51520 | 227 | **Amidase endolysin**（PHROG 822 Amidase_2 + Pfam PG_binding，bitscore 123）| **主候选**：降解肽聚糖；可溶酶、cell-free 友好；独立工程化为 PDA 的成熟范式 |
| ⭐⭐ Tier 1 | `hp3_0069` | 50393–50830 | 146 | Holin #1（PHROG 7045）| 与 endolysin 协同；**膜蛋白、cell-free 表达难**（需脂质体/去垢剂）→ 次优先，先单测 endolysin |
| 🟡 Tier 2 | `hp3_0099` | 78661–78921 | 87 | Holin #2（PHROG 7045）| 可选增强；同膜蛋白限制 |
| 🟡 **Tier 3（探索/判决）** | **`hp3_0055`** | 37828–39045 | 406 | Tail fiber（PHROG 5986, novel；含 Ig-like/fn3 fold）| **depolymerase 假设的 wet-lab 终判**——⚠️ 见下 |

**⚠️ 诚实边界（必须遵守，避免过度宣称）**：
- **`hp3_0055` 不得标注为 depolymerase**：Pfam / InterProScan / Phold-Foldseek / MMseqs2 / AlphaFold+Foldseek **五重 in-silico 检测全阴性**（见 `manuscript/feedback/0604/FEEDBACK_SYNTHESIS.md` §D）。合成它只为**一次性 wet-lab 判决**「它到底有没有降荚膜活性」，结果两可都写进稿——阴性也是有价值的结论。
- **`hp3_0002`（DAHP synthase，shikimate pathway，Foldseek fident=0.38）排除出 enzybiotic 线**：底物/活性完全未知、非裂解酶，留作 manuscript 的 genomic-novelty 卖点即可，不进合成清单。
- DNA 复制酶组（pol/helicase/primase）需活细胞背景，不适合 enzybiotic，排除。

---

## 3 · 工作流（4 阶段，全干 → in-vitro）

```
Phase 0  in-silico 精修(可选)   Phase 1  GCATbio 合成      Phase 2  cell-free 表达     Phase 3  in-vitro 活性
─────────────────────────      ─────────────────         ────────────────────       ──────────────────────
hp3_0070/0069/0099/0055    →   codon-opt ORF 合成    →   TXTL 无细胞表达         →   vs A. hydrophila(Geist)
active-site/AlphaFold 精修      (mMPS, 同批)              (endolysin 优先)            turbidity / zymogram / 降荚膜
[用 vpipe 现成模块, 落地前        附 His-tag + 标准              ↑                          ↓
 先 /vpipe-ask]                cloning sites          可溶酶友好;holin 需膜系统     Phase 4: top hits 纯化+动力学
                                                                                    +(后期)王高学 in-vivo 鱼模型
```

- **Phase 0**（可选，零成本）：对候选酶做 active-site / catalytic-residue 预测 + AlphaFold 结构精修，给合成做最后确认。**用 vpipe 现成模块**（落地前 `/vpipe-ask` 查 Foldseek/Phold/结构注释是否已有）。
- **Phase 1 · GCATbio 合成**：codon-optimized ORF（见 §4 清单），mMPS 单批出货（远低于其 10⁵ 通量上限）。
- **Phase 2 · cell-free TXTL 表达**：endolysin（可溶）直接 TXTL → 省克隆、周转 ~1.5 周；holin（膜蛋白）需脂质体/去垢剂体系，列为次步。
- **Phase 3 · in-vitro 活性筛选**：底物 = **A. hydrophila（Geist 设施 isolate）** + Hp3 宿主 MS01。assay 见 §5。
- **Phase 4 · 推进**：top hits → His-tag 纯化 + 酶动力学（Km/Vmax/比活）+ 谱系（对其他水产病原的广谱性）；**后期**接王高学 in-vivo 鱼模型（设施修好后）。

---

## 4 · 给 GCATbio 的合成清单（Phase 1）

| ORF | aa | ~nt(含 stop) | 合成形式 | 备注 |
|---|---|---|---|---|
| **`hp3_0070` endolysin** | 227 | ~684 | codon-opt(E. coli/cell-free) + C-His6 + 标准 cloning sites | **MVP 必做**；主验证对象 |
| `hp3_0069` holin#1 | 146 | ~441 | 同上 | 膜蛋白；与 endolysin 共表达/脂质体测协同 |
| `hp3_0099` holin#2 | 87 | ~264 | 同上 | 可选增强 |
| `hp3_0055` tail fiber | 406 | ~1221 | 同上（可加截短构建分离 Ig-like 区）| depolymerase 假设判决；非主线 |

- **量级**：4 条 ORF，总 ~2.6 kb，**同批一次出**（对 GCATbio 是小通量用例，正好做 turnaround/quality 的 pilot 验证）。
- **序列来源**：`analyses/data/00-raw/d14-taxonomy/hp3_proteins.faa`（蛋白）+ `hp3.gbk`（坐标）→ 反翻译 + codon-opt。
- **对接 GCATbio roadmap**：此清单 = brain `discussion-notes.md §8` 的 **P1/P2 enzyme 线**，与 P0（A. baumannii RBP 库）并行作为 GCATbio 的两个起步 pilot。

---

## 5 · 体外活性 assay 设计（Phase 3）

| 候选 | assay | 读出 | 对照 |
|---|---|---|---|
| **endolysin `hp3_0070`** | ① 浊度下降法（外源加酶到 A. hydrophila 悬液，OD600 drop）② zymogram（PG-embedded SDS-PAGE 透明带）③ 杀菌曲线 / lytic zone | 比活、最适 pH/盐、外膜通透剂(EDTA)增效 | 商业 lysozyme + 已知 Gram⁻ endolysin |
| holin `hp3_0069/0099` | 与 endolysin 共表达 / 脂质体膜电位实验 | 协同裂解增效 | 单 endolysin |
| **tail fiber `hp3_0055`** | 降荚膜活性：Alcian blue / uronic-acid assay / 荚膜染色 + 噬菌斑 halo | **判决"有/无 depolymerase"** | 已知 depolymerase 阳性株 |

> **Gram⁻ 注意**：A. hydrophila 是革兰阴性，外膜屏障使外源 endolysin 天然受限 → 需配 **OM-permeabilizer（EDTA / 多肽）** 或做 "Artilysin"-式融合。这点要在方案里预先设计，否则易得假阴性。

---

## 6 · 合作方分工

- **Deng Lab / Jinlong**：候选挑选 + Phase 0 in-silico + 合成序列设计 + Phase 3 数据分析 + 统稿
- **GCATbio**：Phase 1 ORF 合成 + Phase 2 cell-free 表达 + （Phase 4）mg-Kg 蛋白生产
- **Geist**：A. hydrophila isolate（设施培养物 / 基因组 DNA）
- **王高学**：Phase 4 in-vivo 鱼模型验证；**TCM 角度**——endolysin × 中草药/天然抗菌物联用（他的强项），可作独立交叉子课题

---

## 7 · 产出与里程碑

1. **补 Hp3 manuscript 的单酶 in-vitro 数据** → 强化 Cell Reports 卖点（从"基因组新颖 + in-vivo"到"+ 功能化 enzybiotic"），或至少让备选期刊更有底气。
2. **独立 enzybiotic 短稿**（Hp3 endolysin 体外表征 ± 广谱性），target: *Antibiotics* / *Microbiol Spectrum* / *IJBM*。
3. **海优 application record**：真实水产 + 合成生物学交叉产出。
4. **GCATbio 第二个 pilot 案例**（与 A. baumannii RBP 并行，覆盖 mechanism + enzyme 两端）。

---

## 8 · 最小起步（MVP，建议先跑这一步）

> **只合成 `hp3_0070` endolysin 单条 → cell-free TXTL 表达 → 浊度下降 assay（+EDTA）vs A. hydrophila**。
> 一步同时验证：① 三方流程（Geist isolate → GCATbio 合成 → 体外验证）跑得通；② 拿到 Hp3 的**第一个单酶活性数据点**；③ GCATbio 真实 turnaround/quality。成功后再扩 holin 协同 + tail fiber 判决 + 广谱性。

---

## 附 · 关键数据文件（执行时取数用）

| 用途 | 路径 |
|---|---|
| 蛋白序列(faa) | `analyses/data/00-raw/d14-taxonomy/hp3_proteins.faa` |
| 基因坐标(gbk/gff) | `analyses/data/00-raw/d112-phage_genome/hp3.{gbk,gff}` |
| 完整注释表(PHROG/Pfam/category) | `analyses/data/00-raw/d112-phage_genome/hp3_cds_final_merged_output.tsv` |
| CDS 汇总 | `analyses/data/112-phage_genome/phage_cds.tsv` |
| depolymerase 五重阴性记录 | `manuscript/feedback/0604/FEEDBACK_SYNTHESIS.md` §D |
| 安全性(CARD 零命中/VFDB 假阳性) | `analyses/data/00-raw/d112-phage_genome/top_hits_{card,vfdb}.tsv` |
