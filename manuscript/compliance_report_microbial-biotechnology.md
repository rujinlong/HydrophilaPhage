---
journal: "Microbial Biotechnology"
manuscript: "manuscript.tex → manuscript.docx"
date: "2026-06-17"
guidelines_source: "for-authors.txt (full local copy of MBT author guidelines) + cache ~/.configure/journals/microbial-biotechnology.md"
overall_status: "PASS (ready to submit; 4 manual system-side items)"
---

# Compliance Report: Microbial Biotechnology (2026-06-17 重核)

Manuscript: `manuscript.docx` (MB 版, 由 `manuscript.tex` + `body.tex` 经 pandoc 转换)
Guidelines: 官方页面 (enviromicro-journals.onlinelibrary.wiley.com .../forauthors.html)
对自动抓取返回 HTTP 402；以本地全文 `for-authors.txt`（MBT 完整指南）为权威依据复核。

## 关键事实更正（相对 2026-05-30 旧版报告）

1. **投稿模式 = Free Format submission**：接受可编辑 Word 文件（text+figures+tables 同档或分档皆可）。→ 本次按用户要求全部产出 **docx**。
2. **投稿系统 = Research Exchange**（https://authors.wiley.com/journal/MBT2），非 ScholarOne。
3. **Summary 上限 = 200 词**（旧报告误按 250）。当前 168 词 ✓。
4. 引用风格 Free Format 阶段接受任一自洽风格；接收后再切 Wiley `.bst`。

## Summary

| Status | Count |
|--------|-------|
| PASS    | 12 |
| WARNING | 2 |
| FAIL    | 0 |
| 系统内待办 | 4 |

## FAIL — 无

旧报告两项 FAIL 均已闭环：
- cover letter 已含「通讯作者同意发表 + 全体作者批准内容与署名」明确语句 ✓
- ORCID（通讯作者 J.R.）已在 title page footnote 给出 ✓

## WARNING — 建议关注

1. **APC 强制 ≈ $4,260 USD**（全 OA，无非 OA 通道）。投稿前确认 TUM 报销。
2. **另两位通讯作者 ORCID**：L.D. / G.W. 建议在系统内补关联（MB 通讯作者要求 ORCID）。

## PASS — 合规

- Summary 168 词 ≤ 200 ✓
- 结构：Introduction / Experimental Procedures / Results / Discussion / Conclusion ✓
- Declarations 完整：Ethics / Declaration of interests / Data availability / Authors' contributions / Acknowledgements ✓
- 数据公开：PRJNA1348731 + Figshare DOI + Zenodo DOI（投稿时均公开）✓
- 动物实验：ARRIVE + IACUC（NWAFU-314020038）✓
- Title page：作者、单位、ORCID、通讯地址/邮箱、running title ≤50 字符 ✓
- 关键词已提供 ✓
- 引用 author-year，正文 39 篇全部解析、参考文献列表含刊名+DOI、无断引 ✓
- 主文图 5 张、SI 图 3 张全部嵌入 docx（已逐一核 `word/media/` 计数）✓
- cover letter 含 consent + all-authors-approval + 无利益冲突 + 数据公开 + suggested reviewers ✓

## 系统内待办（非文件，投稿步骤中填写）

1. 关联通讯作者 ORCID（至少 J.R.，建议补 L.D./G.W.）。
2. 确认 APC 资助。
3. 逐位核对共同作者邮箱/单位。
4. declaration 步骤再勾选 data/funding/COI/ethics。

## 产出投稿包

`mb-submission/`：cover_letter.docx · manuscript.docx · figures/Figure1-5.png ·
supporting_information/{Supporting_Information.docx, SupplementalData.xlsx} ·
graphical_abstract.png · SUBMISSION_CHECKLIST.md
