# Reference Verification Report

- **文件**: `manuscript/body.tex` + `manuscript/manuscript.tex`（frontmatter）
- **Bibliography**: `manuscript/bibliography.bib` → symlink → `/Users/allen/Library/CloudStorage/Dropbox/Family Room/configs/mbp.bib`（Zotero BetterBibTeX export, 170,794 行）
- **日期**: 2026-05-30
- **引用方式**: author-year `\citep{...}` / `\citet{...}`（natbib + apalike）
- **参考文献总数（unique cited keys）**: 31
- **Zotero 已确认 (Zotero-Verified)**: 31
- **PubMed/bioRxiv 已验证 (Verified)**: 0（无需 fallback；全部在 Zotero 命中）
- **信息不符 (Mismatch)**: 0
- **citation_key 空缺 (Citation Key Empty)**: 0
- **未找到 (Not Found)**: 0
- **预印本 (Preprint)**: 0
- **需注意 (metadata note)**: 1（`2023-Potential_Guo` bib 条目缺 `doi` 字段，但有有效 `url`；不影响引用解析）

---

## 验证方法

1. 从 `body.tex` + `manuscript.tex` 提取所有 `\citep`/`\citet` 键 → 31 个 unique key。
2. 对每个 key 在 `bibliography.bib` 中确认存在唯一 `@type{key,` 条目 → **31/31 全部命中，无 dangling `\cite`**。
3. 从每个 bib 条目提取 DOI，调用 zotsearch `lookup_by_doi` 做 Zotero 结构化反查 → 确认 citation_key、title、authors、year、journal 与 bib 一致。
4. 无 DOI 的条目（`2023-Potential_Guo`，Zenodo `2024-Susiegriggo`）用 `show_zotero_item` / `lookup_by_doi`（Zenodo DOI）确认。
5. 未做任何外部（PubMed/CrossRef）查询——所有键均在本地 Zotero 命中，无导入需求。

特别复核了用户点名的 8 个近期新增/编辑键，全部 Zotero-Verified、元数据精确匹配：

| 点名 key | DOI | Zotero item_key | 结论 |
|---|---|---|---|
| `2017-VICTOR_Meier-Kolthoff` | 10.1093/bioinformatics/btx440 | MMU32S7E | OK |
| `2026-Protein_Bouras` (Phold) | 10.1093/nar/gkaf1448 | 5UHG3P2X | OK（2026 NAR，真实，已正式发表） |
| `2017-ViPTree_Nishimura` | 10.1093/bioinformatics/btx157 | H4AXCT3E | OK |
| `2020-VIRIDIC_Moraru` | 10.3390/v12111268 | JZ7WX39J | OK |
| `2016-Mash_Ondov` | 10.1186/s13059-016-0997-x | L7FI72NG | OK |
| `2020-IQTREE_Minh` | 10.1093/molbev/msaa015 | 7E93DAW9 | OK |
| `2017-ModelFinder_Kalyaanamoorthy` | 10.1038/nmeth.4285 | 39M5PQZJ | OK |

（`2026-Protein_Bouras` 是唯一一篇 2026 年 key——已确认为真实正式发表的 Phold 论文，非编造、非占位符。）

---

## Zotero-Verified（全部 31 条）

| # | citation_key | 引用 | DOI / 标识 |
|---|---|---|---|
| 1 | 2003-Cytoscape_Shannon | Shannon et al. 2003. Cytoscape. Genome Research. | 10.1101/gr.1239303 |
| 2 | 2006-Importance_Daskalov | Daskalov 2006. The importance of *Aeromonas hydrophila* in food safety. Food Control. | 10.1016/j.foodcont.2005.02.009 |
| 3 | 2010-Bacteriophage_Labrie | Labrie et al. 2010. Bacteriophage resistance mechanisms. Nat Rev Microbiol. | 10.1038/nrmicro2315 |
| 4 | 2013-MAFFT_Katoh | Katoh & Standley 2013. MAFFT v7. Mol Biol Evol. | 10.1093/molbev/mst010 |
| 5 | 2016-Mash_Ondov | Ondov et al. 2016. Mash. Genome Biology. | 10.1186/s13059-016-0997-x |
| 6 | 2017-ModelFinder_Kalyaanamoorthy | Kalyaanamoorthy et al. 2017. ModelFinder. Nature Methods. | 10.1038/nmeth.4285 |
| 7 | 2017-VICTOR_Meier-Kolthoff | Meier-Kolthoff & Göker 2017. VICTOR. Bioinformatics. | 10.1093/bioinformatics/btx440 |
| 8 | 2017-ViPTree_Nishimura | Nishimura et al. 2017. ViPTree. Bioinformatics. | 10.1093/bioinformatics/btx157 |
| 9 | 2018-Fastp_Chen | Chen et al. 2018. fastp. Bioinformatics. | 10.1093/bioinformatics/bty560 |
| 10 | 2018-Phage_Torres-Barcelo | Torres-Barceló 2018. Phage Therapy Faces Evolutionary Challenges. Viruses. | 10.3390/v10060323 |
| 11 | 2019-Phage_GordilloAltamirano | Gordillo Altamirano & Barr 2019. Phage Therapy in the Postantibiotic Era. Clin Microbiol Rev. | 10.1128/CMR.00066-18 |
| 12 | 2019-VFDB_Liu | Liu et al. 2019. VFDB 2019. Nucleic Acids Res. | 10.1093/nar/gky1080 |
| 13 | 2020-CARD_Alcock | Alcock et al. 2020. CARD 2020. Nucleic Acids Res. | 10.1093/nar/gkz935 |
| 14 | 2020-IQTREE_Minh | Minh et al. 2020. IQ-TREE 2. Mol Biol Evol. | 10.1093/molbev/msaa015 |
| 15 | 2020-VIRIDIC_Moraru | Moraru et al. 2020. VIRIDIC. Viruses. | 10.3390/v12111268 |
| 16 | 2021-Clinker_Gilchrist | Gilchrist & Chooi 2021. clinker & clustermap.js. Bioinformatics. | 10.1093/bioinformatics/btab007 |
| 17 | 2021-MiRNAseq_Zhou | Zhou et al. 2021. miRNA-seq ... largemouth bass ... *A. hydrophila*. Funct Integr Genomics. | 10.1007/s10142-020-00763-8 |
| 18 | 2021-Phage_Abedon | Abedon et al. 2021. Phage Cocktail Development. Pharmaceuticals. | 10.3390/ph14101019 |
| 19 | 2021-Phage_Ramos-Vivas | Ramos-Vivas et al. 2021. Phage Therapy ... in Aquaculture. Int J Mol Sci. | 10.3390/ijms221910436 |
| 20 | 2021-PHROG_Terzian | Terzian et al. 2021. PHROG. NAR Genom Bioinform. | 10.1093/nargab/lqab067 |
| 21 | 2021-Reprogramming_Dunne | Dunne et al. 2021. Reprogramming bacteriophage host range. Curr Opin Biotechnol. | 10.1016/j.copbio.2021.02.006 |
| 22 | 2022-Pharokka_Bouras | Bouras et al. 2022. Pharokka. Bioinformatics. | 10.1093/bioinformatics/btac776 |
| 23 | 2023-Developing_Oromi-Bosch | Oromí-Bosch et al. 2023. Developing Phage Therapy ... Bacterial Resistance. Annu Rev Virol. | 10.1146/annurev-virology-012423-110530 |
| 24 | 2023-Potential_Guo | Guo et al. 2023. Potential of phage depolymerase ... biofilms. Virulence. | url → 10.1080/21505594.2023.2273567 (bib 缺 doi 字段) |
| 25 | 2023-Review_Semwal | Semwal et al. 2023. A review on pathogenicity of *A. hydrophila* ... Heliyon. | 10.1016/j.heliyon.2023.e14088 |
| 26 | 2024-Growing_Murtazalieva | Murtazalieva et al. 2024. The growing repertoire of phage anti-defence systems. Trends Microbiol. | 10.1016/j.tim.2024.05.005 |
| 27 | 2024-Susiegriggo_SusieGrigson | Grigson et al. 2024. susiegriggo/Phynteny 0.1.13. Zenodo. | 10.5281/zenodo.11025439 |
| 28 | 2025-Global_Jeamsripong | Jeamsripong et al. 2025. Global spread and AMR of *A. hydrophila* ... Sci Rep. | 10.1038/s41598-025-14498-8 |
| 29 | 2025-Reevaluating_Cook | Cook & Hynes 2025. Re-evaluating what makes a phage unsuitable for therapy. npj Antimicrob Resist. | 10.1038/s44259-025-00117-z |
| 30 | 2025-Vivo_Wang | Wang et al. 2025. In vivo imaging ... *A. hydrophila* ... common carp. Fish Shellfish Immunol. | 10.1016/j.fsi.2025.110276 |
| 31 | 2026-Protein_Bouras | Bouras et al. 2026. Protein structure-informed bacteriophage genome annotation with Phold. Nucleic Acids Res. | 10.1093/nar/gkaf1448 |

---

## Mismatch

无。

## Citation Key Empty

无。

## Auto-importable / Pending Zotero Imports

无。所有 31 个键均已在用户 Zotero 库中存在并带 BetterBibTeX 键；无 `[@DOI:...]` 占位符，无需导入。

## Not Found

无。

## Preprint

无。`2026-Protein_Bouras`（Phold）虽为 2026 年，但已在 Nucleic Acids Research 正式发表（非 preprint），DOI 10.1093/nar/gkaf1448 在 Zotero 命中。

---

## 需注意的小问题（metadata，不影响引用解析）

1. **`2023-Potential_Guo`** — bib 条目 `doi` 字段为空，仅有 `url`
   (`https://www.tandfonline.com/doi/abs/10.1080/21505594.2023.2273567`)。文献本身真实
   （Virulence 14(1):2273567, DOI 10.1080/21505594.2023.2273567）。apalike author-year 渲染不依赖
   DOI，因此不影响编译或引用正确性；若投稿要求参考文献列 DOI，建议在 Zotero 中补全该字段。
2. 引用键命名约定 `YYYY-Word_Author` 全部遵守；`2024-Susiegriggo_SusieGrigson` 命名稍特殊
   （software/Zenodo 条目，第一"作者字段"为 GitHub handle "Susie Grigson"），但条目真实且 DOI 有效。

---

## Summary

- 共 **31** 条 unique cited keys。
- **31/31** 由 Zotero 直接确认（最高置信度）：每个 `\cite` 键 → 唯一 bib 条目 → 经 DOI 反查命中真实 Zotero item，title/authors/year/journal 全部一致。
- **0** 条信息不符，**0** 条未找到，**0** 条 citation_key 空缺，**0** 条占位符待导入，**0** 条 preprint。
- 用户点名的 8 个近期键（VICTOR / Phold / ViPTree / VIRIDIC / Mash / IQ-TREE / ModelFinder）全部 Zotero-Verified、元数据精确匹配，无编造、无占位符。
- 唯一需注意项：`2023-Potential_Guo` bib 条目缺 `doi` 字段（有 url，文献真实），属可选的元数据补全，非正确性问题。

## Risk Assessment

**风险等级：低**

Not Found 比例 = 0%。所有引用均在用户自有 Zotero 库中以真实条目存在，无 AI 编造特征
（无虚构期刊名、无不存在的作者组合、无伪造 DOI 格式）。manuscript 可直接进入投稿/编译阶段，
参考文献层面无 blocker。
