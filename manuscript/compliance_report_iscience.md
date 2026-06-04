---
journal: "iScience"
manuscript: "manuscript-cr.tex"
date: "2026-06-04"
guidelines_source: "cell.com/iscience (via WebSearch 2026-06-04; cell.com blocks automated fetch, HTTP 403)"
overall_status: "PASS (initial-submission ready; 3 revision/production-stage items noted)"
---

# Compliance Report: iScience

Manuscript: `manuscript-cr.tex`（iScience 投稿版：Cell Press front matter + `\input{body}` narrative body）
Guidelines: iScience information-for-authors（WebSearch 2026-06-04，cell.com 阻止自动抓取）

## Summary

| Status | Count |
|--------|-------|
| PASS | 11 |
| WARNING | 3 |
| FAIL | 0 |
| UNKNOWN | 1 |

## FAIL — 无

initial submission 无阻断性问题。

## WARNING — 建议处理（多为 revision/production 阶段）

1. **STAR Methods**：iScience 正式发表用 STAR Methods section。当前投稿版用 narrative methods（`body.tex` 的 Experimental Procedures）。Cell Press **initial submission 格式灵活、接受 narrative**；`manuscript-cr.tex` 注释已规划 revision 时切 `\input{body-cr}`（加载已备好的 `star_methods.tex` = Key Resources Table + Data/code availability）。→ **initial OK，revision 切换**。

2. **引用 DOI 显示**：iScience 要求每条 reference 含 DOI。当前 `.bbl`（natbib/apalike 风格）39 条仅 1 条显示 DOI。**bib 条目本身有 DOI**（verify-refs 已确认 38/38），只是 apalike 风格不输出。正式提交切 Cell Press `cell.bst` 即输出 DOI。→ **production/revision 时切 cell.bst**。

3. **front matter 注释残留 "Cell Reports"**：`manuscript-cr.tex` 注释写 "Cell Reports front matter / Cell Reports limit"。不影响渲染（仅注释），但建议更新为 iScience，并确认 iScience eTOC 标题用 "In Brief"（Cell Press 通用）。

## PASS — Compliant

- 正文 **6,186 词** < iScience **8,000** 上限 ✓
- **Highlights**：4 条，字符数 80 / 65 / 80 / 61，全部 ≤ **85** ✓
- **In Brief / eTOC**：**40 词**（= 40 上限）✓
- **Summary**：159 词，单段无引用（Cell Press 惯例 150–185）✓
- **Graphical abstract** ✓
- **References**：author-year（Cell Press Harvard 风格）✓
- **Declarations 完整**：Ethics（IACUC 批准号 NWAFU-314020038 + 批准日期 + ARRIVE）、Competing interests、Funding（NKRDP 2023YFD2400700 / DFG / ERC StG 803077）、Data + code availability（NCBI PRJNA1348731 / GenBank PX754746.1 / Figshare DOI / Zenodo DOI + GitHub）、Authors' contributions ✓
- **ORCID** ✓
- **Figures**：5 主图（fig1–5）+ Graphical abstract + 3 SI（vConTACT3 / PHROG / ViPTree）；iScience 图数限制宽松 ✓
- **Animal ethics**：ARRIVE guidelines + IACUC 审批声明 ✓

## UNKNOWN — 需人工核验

**（已全部核验,无未决项）**

- Figure resolution **已核验**（2026-06-04 via `sips`）：fig1–5 = 330 / 300 / 300 / 330 / 330 DPI，全部 ≥ 300，满足 iScience 彩图要求 ✓

## Suggested Actions（按优先级）

1. **检查 fig1–5.png 分辨率 ≥ 300 DPI**（唯一 initial-submission 前需确认的项）。
2. （revision 阶段）切 `\input{body-cr}` 启用 STAR Methods + Key Resources Table。
3. （production/revision 阶段）bibliography 切 `cell.bst` 输出 reference DOI。
4. （可选）`manuscript-cr.tex` 注释里 "Cell Reports" → "iScience"。

**结论**：manuscript 已基本满足 iScience **initial submission** 要求，无阻断性 FAIL。3 个 WARNING 均为 revision/production 阶段切换项（作者已在源码注释中规划）；唯一 initial 阶段需确认的是图像分辨率。
