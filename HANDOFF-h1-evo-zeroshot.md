# HANDOFF — H1 PoC: Evo/ESM zero-shot 噬菌体变体效应预测

> **给下一个 session 的冷启动文档。** 创建于 2026-06-02。工作 path = 本 repo（`~/github/rujinlong/pc031-aquaPhage`）。
> 上游决策与三篇论文深读在 `~/brain/wiki/atlas/`，pm 记录在 `~/brain/.claude/context/pm.sqlite`（DEC-D??? / TASK 见 pm_index）。

---

## 0. 一句话任务

在本 repo 的 `analyses/` 里跑一个**最小可行 PoC**：用 **Evo**（基因组语言模型）和 **ESM-2**（蛋白语言模型）对噬菌体变体做 **zero-shot 打分**（log-likelihood delta），检验「基因组/蛋白语言模型能否**不训练**就预测噬菌体变体效应」。**判决：AUC ≥ 0.7 → 方向成立，推进固化进 vpipe；< 0.7 → 走 fallback。** 成本：一下午 · 1 GPU · 零湿实验 · 零新预算。

这是 H1 假设（见 `~/brain/wiki/atlas/papers/nguyen_2024_science/profile.md` §19 H1）。

---

## 1. 为什么做这个（背景，5 行）

本 session 建立了 **missense-variant effect 方法学三角**（三篇 atlas profile）：
- **Beltran 2025 Nature**（实验 DMS / 蛋白稳定性，Human Domainome 1）
- **AlphaMissense / Cheng 2023 Science**（计算预测，但 **human-only，不能用于噬菌体**）
- **Evo / Nguyen 2024 Science**（基因组语言模型，**Arc Institute，训练数据含数百万 phage 基因组、排除真核宿主病毒**）→ 正是把"AlphaMissense 范式"上噬菌体的现成起点。

关键：**Evo 论文本身就做了噬菌体基因 essentiality 的 zero-shot 预测** + E. coli 蛋白 DMS fitness——所以 H1 不是空想，风险只在"RBP 这类高变蛋白还成不成立"。

---

## 2. 必读上下文（新 session 先读这 2 个，其余备查）

| 文件 | 作用 | 优先级 |
|---|---|---|
| `~/brain/wiki/atlas/papers/nguyen_2024_science/H1-evo-zeroshot-protocol.md` | **主 protocol**：带 Python 代码骨架、数据格式、判决标准、fallback | ★★★ 必读 |
| `~/brain/wiki/atlas/papers/nguyen_2024_science/profile.md` | Evo 深读：§8 variant-scoring 接口 / §16 compute / §23 落地 / §19 H1-H3 | ★★★ 必读 |
| `~/brain/wiki/atlas/papers/cheng_2023_science/profile.md` | AlphaMissense + §23 missense 系统地图（为什么 human-only 不能用） | ★★ 备查 |
| `~/brain/wiki/atlas/papers/beltran_2025_nature/profile.md` | 实验 DMS 对照（后续 fine-tune 的 ground-truth 范式） | ★ 备查 |
| 本文件 §4 vpipe 积木 | 哪些步骤用 vpipe 现成命令，不要重造 | ★★★ 必读 |

---

## 3. 两个 testbed（建议先 Hp3，更快起步）

> **2026-06-02 更新（重要）**：a_baumannii 数据已定位且**远比预期 ready**（`p0083-AbpBiofilm/data/df_breseq.rda`，treatment-resolved 抗性突变矩阵）。**主从关系已修正**：a_baumannii = **主判决场**（唯一能算真 AUC），Hp3 = 接口预热/sanity check。a_baumannii 侧有自己的完整 handoff：`~/github/rujinlong/p0083-AbpBiofilm/HANDOFF-h1-evo-zeroshot.md`。

### Testbed A（本 repo）— Hp3：接口预热 / sanity check
- **基因组**：`analyses/data/00-raw/d112-phage_genome/out_hp3_phold/out_hp3_phynteny/phynteny.gbk`（Aeromonas hydrophila phage vB_AhyM_Hp3，84.7 kb，CDS+product+translation 齐全）；`vpipe gbk to-fasta` 一行抽 FASTA。
- **角色**：无抗性 ground truth → 做 **essentiality / 保守性 zero-shot**（Evo 论文先例）或人工饱和突变 likelihood 分布，用于**跑通接口 + 方法 sanity check**。不是 AUC 判决场。

### Testbed B（p0083-AbpBiofilm）— a_baumannii PhageX/M：**主判决场**
- **数据已现成**：`~/github/rujinlong/p0083-AbpBiofilm/data/df_breseq.rda`（11187 突变 × 17 列，样本 = BACN1 背景 / X_H X_L(PhageX) / M_H M_L(PhageM) / X_M_*(组合)，**已标注同义/非同义**）。
- 这是真正的 **AUC 判决数据**：resistant = phage-treatment 富集、neutral = 背景/未富集；按 PhageX-受体(LPS/OmpA) vs PhageM-受体(Wzc/capsule) **分端**。
- 完整指引见 p0083 的 handoff；**scoring 脚本与本 repo Hp3 共用一份**（最终归 vpipe，DEC-D017）。

**推荐流程（方法共享、testbed 分工）**：先在 **p0083（数据最强）** 用 df_breseq 跑通 Evo/ESM scoring + 出 AUC 判决 → 同一份脚本回灌 Hp3 做 sanity check → AUC≥0.7 后固化进 vpipe。**⛔ 两个 repo 不各搭一套 scoring**（EL-004）。

---

## 4. vpipe 现成积木（vpipe-ask 已盘点，别重造 — EL-004 教训）

vpipe 在 `~/.nextflow/assets/rujinlong/vpipe`。本链 ~60% 是现成积木：

| 步骤 | vpipe 命令 | 判定 |
|---|---|---|
| Hp3 gbk → 蛋白/核酸 FASTA | `vpipe gbk to-fasta -g phynteny.gbk -o hp3.faa -k CDS -t prot --strict`（再 `-t nucl -o hp3.fna`） | REUSE |
| breseq HTML → 突变表 | `vpipe parse breseq` | REUSE |
| ESM-2 推理基础设施 | `bin/esm2.slurm` + `bin/esm2_nn.py`（fair-esm，目前只 embedding+FAISS NN） | **EXTEND**：加 `score-llr` 模式算 LLR |
| 结构特征（可选，后续） | `anno_prot3D.slurm esmfold2`（GPU + HF cache） | REUSE |
| host prediction（genome 级） | `iphop_sg` | REUSE（非 RBP variant 级） |
| Hp3 编排归宿 | `subworkflows/local/aquaphage_base/main.nf`（pc031-aquaPhage 母赛道，v0 骨架有 TODO 等挂工具） | REUSE 骨架 |

**真正 NEW 的只有两块**：
1. **Evo 推理**（github.com/evo-design/evo，GPU 7B 模型）— PoC 阶段临时脚本；固化时照 `anno_prot3D.slurm esmfold2` 模板做容器化工具（docker/evo/ + conf/database.yml `DB_EVO_*` + bin/00-config.sh + bin/variant_score.slurm）。
2. **variant → AUC/Spearman 评估** — 固化时落 `pkgs/vpipe/src/vpipe/core/variant.py`（纯函数，INV-PY-01）+ `cli/variant.py`。

---

## 5. 关键决策：先 PoC，后固化（不要过早工程化）

| 阶段 | 放哪 | 说明 |
|---|---|---|
| **H1 PoC（现在）** | **本 repo `analyses/`**（独立脚本，Python 为主） | 研究性、可能证伪；先证 AUC≥0.7 |
| **验证后固化** | **vpipe**（EXTEND esm2 + NEW core/variant.py + 可选 Evo 容器，挂 aquaphage_base TODO） | 会被 a_baumannii/vpa/aqua 多项目复用 |

**⛔ 不要**一上来就往 vpipe 加 module——先在 analyses/ 跑通、验证方向。

---

## 6. 第一步具体命令（新 session 落地）

```bash
cd ~/github/rujinlong/pc031-aquaPhage

# 1. 抽 Hp3 蛋白 + 核酸（vpipe REUSE）
GBK=analyses/data/00-raw/d112-phage_genome/out_hp3_phold/out_hp3_phynteny/phynteny.gbk
vpipe gbk to-fasta -g "$GBK" -o /tmp/hp3.faa -k CDS -t prot --strict
vpipe gbk to-fasta -g "$GBK" -o /tmp/hp3.fna -k CDS -t nucl

# 2. 建 PoC 目录（建议 analyses/ 下新分析编号，遵循本 repo qproj/projthis 规范 — 见 CLAUDE.md）
# 3. ESM-2 LLR：参照 protocol §3 代码骨架；先复用 bin/esm2_nn.py 的 fair-esm 加载，加 score 模式
# 4. Evo：pip/clone github.com/evo-design/evo；nucleotide 序列算 log-likelihood（GPU ~16-40GB）
# 5. sanity check（Hp3）：essential vs 非 essential CDS 的 likelihood 分布是否分离（Evo 论文先例）
# 6. 正式判决（a_baumannii）：先定位 breseq 数据 → vpipe parse breseq → delta vs 抗性标签算 AUC
```

环境注意（来自 Evo profile §16 / §18）：
- Evo 输入是**核苷酸序列**（不是氨基酸）；WT/MUT 用相同 reduction（都 sum 或都 mean per-token）；
- 控制**同义突变**基线（查 H3：codon-usage 混杂）；
- host 侧（Wzc，细菌）与 phage 侧（RBP）**分开打分、分开算 AUC**（正中 a_baumannii "asymmetric cross-resistance" 核心问题）；
- 设 ESM-2 对照（H2：验证 Evo 的 phage 训练域是否带来增益）。

---

## 7. 判决与产出

- **AUC ≥ 0.7** → H1 成立。产出 = 方法学短文 figure 1（"genome language model zero-shot predicts phage-host resistance variants"）+ AIphage grant preliminary data → 接 GCATbio 合成 RBP 饱和库做 supervised（见 `~/brain/wiki/atlas/meetings/2026-05-20-gcatbio-mmps-dna-synthesis/profile.md`）。
- **0.6–0.7** → 方向对、需 fine-tune（少量 host-range DMS 造 ground truth）。
- **≤ 0.6** → 纯 zero-shot 不够，转 ESM-2 supervised 或等 DMS 数据。

三个假设（H1/H2/H3）完整定义在 Evo profile §19（canonical 格式，已入 `~/brain/wiki/atlas/_hypotheses/`）。

---

## 8. 一句话给新 session

**先 `cd ~/github/rujinlong/pc031-aquaPhage`，读 H1-evo-zeroshot-protocol.md + Evo profile §8/§19/§23，用 `vpipe gbk to-fasta` 抽 Hp3 蛋白跑通 ESM/Evo likelihood 接口，再切 a_baumannii breseq 做正式 AUC 判决。别急着进 vpipe——先在 analyses/ 证明 AUC≥0.7。**
