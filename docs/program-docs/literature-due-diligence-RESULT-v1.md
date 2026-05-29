# 文献尽调结果 — 三线 go/no-go 裁决 (v1)

> **来源**: `deep-research` workflow (run wf_b8b8c6d4-c12, 2026-05-29) · 104 agents · 4.67M tokens · 22 源 · 108 claims → 25 验证(19 confirmed / 6 killed) · 3 票对抗式
> **母战略**: `aquaculture-track-record-plan-v1.md` (DEC-D010) · 对应 `literature-due-diligence-brief-v1.md`
> **决策**: DEC-D011
> ⚠ **可信度边界**: 见 §5 caveat。三线均非"铁证空白";线③+综述位为 **provisional**(本轮 3 个验证 agent 失败,覆盖不足)。重大投入(学生 onboarding)前须按 §6 复跑。

---

## 0. 总裁决
**三线全 GO**(novelty + 可发表性双半满足,Aeromonas/aquaculture scope 下无正面撞车),但带 **3 个强制 pivot**、**1 个待你亲核的硬伤风险(Hp3 new family)**,且 **线③/综述位需第二轮检索**才能从 provisional 转 final。

---

## 1. 线① — Aeromonas phage pangenome + depolymerase/endolysin 系统挖掘 → **GO**

**已发表关键文献**(均单分离株/小 N,非 genus 级 pangenome):
| 文献 | 刊(年) | DOI/ID | 核心 | 重合度 |
|---|---|---|---|---|
| Hp3 (本人) | SSRN preprint | `10.2139/ssrn.5897348` | 单 phage 分离表征(锚点) | — (自有) |
| BUCT551 | Front Vet Sci 2025 | `10.3389/fvets.2025.1679093` (PMC12512217) | 1 phage(61.4 kb/74 ORF)vs 1 ref | 中 |
| 俄罗斯三联(A. veronii) | Viruses 2025 | `10.3390/v17081027` (PMC12390700) | 3 phage/1 株;提新属+科 Chimallinviridae | 中(新属角度**高**) |
| EndoA3 | Int J Biol Macromol 2025 | `10.1016/j.ijbiomac.2025.146934` (PMID 40825433) | 单酶生化表征;**preamble 已挖 71 个 M15_C peptidase**(Aeromonas/Edwardsiella) | 中(酶挖掘**部分先例**) |
| Ely174 | AEM 2025 | `10.1128/aem.01891-25` (PMC12628812) | 单酶 Flavobacterium endolysin + 工程 | 低 |
| (历史) 60-genome taxonomy | Viruses 2019 | PMC6669705 | Aeromonas phage 分类奠基 | 低 |

**Gap**: 无"genus 级 Aeromonas pangenome + 系统性(多家族)depolymerase/endolysin 多样性挖掘"专文。
**可发表性**: Front Vet Sci 2025 / Viruses 2025(×2)/ Int J Biol Macromol 2025 —— 同类近 2 年高频。
**强制 pivot**:
- ⛔ **不碰 Vibrio**(见 §4 边界)。
- 酶挖掘走 **pan-domain 多家族 + 跨 Aeromonas/Edwardsiella/Flavobacterium/Photobacterium**,显式引用并超越 EndoA3 的"71 个 M15_C 单 motif"先例。
- 分类**别主打 "first new Aeromonas family"**(俄罗斯那篇已提新科);框成 **systematic pangenome + enzyme catalog**。

## 2. 线② — 水产病原 host-segmented 安全筛查/设计 DB + web server → **GO + PIVOT**

**已发表关键文献**:
| 资源 | 刊(年) | DOI/ID | 与线②关系 |
|---|---|---|---|
| PhageScope | NAR 2024 | `10.1093/nar/gkad979` (PMID 37904614) | 873K phage,**已注释 lifestyle/VFDB 毒力/CARD ARG**;无水产 host 切分、无治疗判定 |
| **Sphae** | Bioinformatics Advances 2025 | `10.1093/bioadv/vbaf004` (PMC11783317) | **已自动做 therapy 候选的毒力/ARG/溶原筛查 pipeline**;但非 web、非 curated DB、host-agnostic |
| INPHARED | PHAGE 2021 | `10.1089/phage.2021.0007` (PMID 36159887) | host-genus bias:**75% phage 集中 30 个 genera**,Aeromonas/Photobacterium 欠采样(gap 支撑) |

**Gap**: 无"水产病原 host(Aeromonas/Vibrio/Edwardsiella/Flavobacterium/Streptococcus)切分 + 预筛 safe-phage 候选 + web server"的资源。
**可发表性**: PhageScope→NAR Database issue;Sphae→Bioinformatics Advances(Oxford)。
**强制 pivot**: **筛查方法不是 novelty**(PhageScope/Sphae 已实现)。novelty = **host 切分 + 水产索引 + web 打包 + safe-phage 设计**。引用 PhageScope/Sphae 为上游 primitive。

## 3. 线③ + 综述位 → **GO (PROVISIONAL,须第二轮检索)**
本轮 3 个结构化验证 agent 失败,线③/综述位**未充分验证**。已抓到但未核实的源(供第二轮深读):
- 线③: bioRxiv `2025.10.19.683331` · Nature Sci Data `s41597-026-07383-0` · Microbiol Spectrum `10.1128/spectrum.00013-25` · Aquaculture `S0044848624010329` · Environ `S0013935122002286` · PMC8922420
- 综述位: Fish & Fisheries `10.1111/faf.70055` · Aquaculture, Fish & Fisheries `aff2.70171` · Brief Bioinform `bbae117` (PMC12029768/12838229/11680434 为 secondary)
**未答(openQuestions)**: 鱼/虾肠道 virome 已发表数量、跨研究 meta-analysis 是否存在、主养品种/地理空白、bulk-vs-VLP 审稿立场、2023-26 水产 phage 综述占位与 DBTL 视角空缺。

## 4. 关键边界 — Vibrio 酶挖掘已被占(线①禁区)
Yue et al. 2026, *Appl Environ Microbiol* 92(2):e01824-25, `10.1128/aem.01824-25` (PMID 41524417, PMC12915355, 青岛能源所 CAS): 系统挖掘 cultured(RefSeq v210, 79.4%)+ uncultured(IMG/VR v4, 46.2%)Vibrio phage,得 **573 个 putative depolymerase 基因** + 系统发育 + 验证 Dep193。→ **Vibrio host 酶挖掘 = 高撞车**;Aeromonas = 安全。(注:orchestrator 一度误标此刊为 Microbiology Spectrum,实为 AEM,已校正。)

## 5. Caveats(对抗式验证残留风险)
- ✅ **Hp3 "putative new family" 已亲核(2026-05-29)**:verifier 的 0-3 refute 是**误报**——pc031 `manuscript.qmd` abstract(line 60)+ 正文 §Genomic Analysis 均明确论证 new family。**但证据偏弱**:单基因(terminase large subunit)系统发育 + 仅 3-genome vConTACT3 cluster(Hp3 + HJ05 + vB_RleS_L338C)+ 最近亲 HJ05 本身 "unclassified Caudoviricetes",未用 VIRIDIC/ICTV family demarcation。→ pc031 论文潜在审稿软肋(分类学审稿可要 VIRIDIC/多基因树;revision 补 heatmap 即可缓);线①应以 pangenome + VIRIDIC + 多基因 proteomic tree 升级此弱主张,但勿主打"first new family"(Chimallinviridae 已占)。
- **时效性**: 最强撞车(Vibrio AEM)2026-01-12 才发,距检索数周。onboarding 前 re-run 线①+③。
- **absence 不可证**: "无 Aeromonas 酶挖掘专文""无水产 phage 库"过了多轮对抗 + PubMed 零命中,probable 非铁证。
- **Hp3 证据基于 SSRN preprint**(非同行评审);"在审 Fish & Shellfish Immunology"来自项目笔记非 cited source。
- **被否决的过强表述**(0-0/1-2 abstain,非结论): Ely174 的 SprA 融合机制、Dep193 "首个" 等——引用时勿照搬。

## 6. 建议开工顺序(deep-research 建议,已采纳)
1. **线①** 先做(in-house Hp3 + 最干净白区 + 最省 pivot);投 *Viruses* / *Int J Biol Macromol*。
2. **线②** 次之(复用线①的 curated genomes);投 *Database (Oxford)* / *Scientific Data* / NAR。
3. **线③ + 综述位** 第三(**先跑第二轮专项检索**确认 gap 再投学生);投 *mSystems* / *Environmental Microbiome*。

## 7. 下一步 TODO
- [x] ~~亲核 Hp3 new family~~ → 已核(见 §5):论文有论证但证据偏弱(单基因 + 3-genome),verifier 误报已证伪。后续:pc031 投稿备 VIRIDIC heatmap 应对分类学审稿;线①用 pangenome 升级证据。
- [ ] 线③/综述位**第二轮专项检索**(转 final 前必做)
- [ ] onboarding 前 re-run 线①Aeromonas + 线③virome(时效性)
- [ ] (可选)用 zotsearch/PubMed 终核上述关键 DOI 后再正式立项
