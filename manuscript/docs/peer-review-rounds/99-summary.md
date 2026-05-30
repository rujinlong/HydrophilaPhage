# 对抗审稿总结 — Hp3 手稿（vB_AhyM_Hp3 → Microbial Biotechnology）

**日期**: 2026-05-30  **流程**: NotebookLM(hostile) → Codex GPT-5.x(裁决) → Claude(实施) → latexmk 重编译
**语料**: 专用 notebook `6c2013cb`（25 源：手稿 anon + 21 篇领域/分类法文献 + Turner 2021 Roadmap & 2023 ICTV update + Bujak 2022 Aeromonas phages + AhFM11）

## 逐轮结果

| Round | 焦点 | NLM 命中 | Codex 裁决 | 实施 |
|-------|------|----------|-----------|------|
| 1 | 分类学（新科/新属） | 5 条（R1-02 ICTV 建科需 ≥2 属为最强） | 保留 new-genus，family 降为 provisional；8 must-fix | title/abstract/keywords/heading/Fig4 caption/Discussion/Conclusion 去 family 声明；Methods+Results 说明 VICTOR 只用 genus（EL-001）、加 ICTV caveat（引 Turner 2021/2023） |
| 2 | putative AMG | 5 条 | R2-03 污染论**驳回**（闭合环状基因组，Codex 实读 phage_cds.tsv 证 hp3_0002@1880-3040）；3 must-fix | thyA/nrdD 改称核苷酸代谢基因（非 AMG）；DAHP 降为 "putative, distantly related structural homolog"；去 "concrete target"；加闭合基因组 provenance 句 |
| 3 | in vivo + 统计 | 6 条（全 must-fix） | R3-01 用已算统计**实做** | **新增完整生存分析**：overall log-rank χ²=64.6(df=3,p<0.001) + BH 两两 + Cox HR；软化 biosafety；加 immunophage synergy(引 Torres-Barceló)+CFU/power/随机化/盲法/单 cohort limitations；ARRIVE 降为 "with reference to" |
| 4 | 新颖性 vs 前人 | 6 条 | 4 must-fix | 引 AhFM11(2024-Novel_MuliyaSankappa)+Ramos-Vivas 做对标、明说"consistent with/builds on"既有范式；去 "platform for engineering" overclaim；加 translational limitations（IP 不可规模化、需 cocktail） |

## 新增分析（可复现）

- **生存统计重做**（R3-01）：`docs/peer-review-rounds/round_03/survival_stats.R` + 回填 `analyses/121-figs.qmd` survival-stats chunk。
  - 四组（各 n=20）：PBS 100% / phage 100% / bacterial **15%** / treatment **85%**
  - Overall k-sample log-rank：χ²=64.6, df=3, p=6.2×10⁻¹⁴
  - BH 两两：treatment vs bacterial p_adj=1.2×10⁻⁵；**treatment vs PBS/phage p_adj=0.09(NS)**（治疗组存活≈健康对照）
  - Cox HR(treatment vs bacterial)=0.091, 95% CI 0.026–0.320, p=1.8×10⁻⁴

## 最终 claim 分级

- **demonstrated-by-data**：in vivo 救治 15%→85%（overall log-rank p<0.001；HR 0.091）；完整 84.75 kb 基因组；新属（VIRIDIC 83.65% + Mash + TerL UFBoot=100 + VICTOR aa/D6）；无 AMR/高置信 virulence 基因。
- **consistent-with-literature**：疗效与既往 Aeromonas phage therapy（AhFM11 注射/浸泡/投喂高保护）一致；deeply divergent genus 属 post-Caudovirales 大量未分类 floating genera 之一。
- **speculation（已显式标注）**：putative family-level lineage（待 ICTV 正式评估 + 更多属采样）；hp3_0002 DAHP-synthase-like 功能（fident=0.38，无功能数据）。
- **retracted/down-toned**：title/abstract「putative new viral family」→ deeply divergent genus；「platform for engineering next-gen therapies」→ 去除；「demonstrating biosafety」→「no acute mortality/overt pathology under tested conditions」。

## Codex 抓到的 NLM 幻觉（未采纳）

- R2-03「Roux et al. 2015」、R2-04「Abedon 2017」均不在语料/bib（幻觉引用）→ **未引用**。
- R2-03 contig-edge/污染前提对闭合环状基因组不成立 → 驳回，仅加预防性 provenance 句。

## 编译状态

- `manuscript.pdf` 18 页，34 refs（31−1 Dunne[engineering 段删除致其 uncited]+4 新），0 undefined citation。
- `manuscript-anon.pdf` 重新生成，residual-identity 扫描全清，新引用解析完毕。
- 参考文献净变化：+Turner2021 +Turner2023 +Bujak2022 +MuliyaSankappa2024，−Dunne2021（engineering 段移除）。

## 投稿前判定：**READY**（带可接受的残余风险）

接受的残余风险（已在 Discussion 显式承认，非隐藏）：
1. 无 a priori power calculation、随机化/分配/盲法未正式记录、histopathology 无盲法半定量评分、未测组织 CFU/g、单 cohort 无独立重复 → 全部列入 limitations。
2. family rank 维持 provisional；taxonomy reviewer 仍可能要求 core-gene/pangenome 分析或正式 ICTV TaxoProp（Adriaenssens 在荐审名单中——已主动防御）。
3. vConTACT3 连接 few-protein-driven，仅作 convergent 佐证。
4. fig5 PNG 未重渲染（生存曲线本身不变，plot 注释 "p<0.001" 仍成立；qmd stats chunk 已更新，建议用户重渲染 121-figs 以同步图内注释与新统计）。

## 审计轨迹

- `round_01/`…`round_04/` notebooklm_review.md + round_01 & round_234 codex_evaluation.md
- `round_03/survival_stats.R`（+ 重算输出）
- `.adversarial-review-state.json`（notebook/source ids、rounds_completed）
- pm: DEC-D019（reviewers）、本轮对抗审稿 DEC、session S-2026-05-29-001
