# 共享数据底座 — 可执行化 spec (v1)

> **状态**: v1 (2026-05-29) · **母战略**: `aquaculture-track-record-plan-v1.md` (DEC-D010)
> **关键路径**: 底座 v0 是三线(学生 A/B/C)的共同输入;先你 + 最强学生 2–4 周搭出,再三线并行。
> **复用**: 沿用 pc031-aquaPhage 已验证的工具链 (Pharokka/Phold/Phynteny/vConTACT3),向下游扩展安全筛查 + 酶注释模块。
> ⚠ 工具版本在环境里 pin(conda/uv lock),本文件不写死版本号;URL 仅列确信入口,存疑处标"待确认"。

---

## 0. 一句话
拉全"水产病原宿主"的噬菌体基因组 → 统一 ViroProfiler 注释 + 治疗安全筛查 + 酶注释 → 输出一张三线共用的 master 注释表。**②号库 = 这张表 + 注释结果的产品化。**

## 1. 范围: 宿主病原清单 (待你终稿冻结)
按宿主菌 taxid 检索其噬菌体 + 从宿主基因组提 prophage。候选清单:

| 病原 (genus/species) | 主要养殖危害 | 优先级 |
|---|---|---|
| _Aeromonas hydrophila / veronii / salmonicida_ | 大口黑鲈/多种淡水鱼出血败血 | **P0**(锚点, 接 Hp3) |
| _Vibrio anguillarum / harveyi / parahaemolyticus_ | 海水鱼/对虾弧菌病 | P1 |
| _Edwardsiella tarda / ictaluri / piscicida_ | 鮰/鳗爱德华氏菌病 | P1 |
| _Flavobacterium columnare / psychrophilum_ | 柱形病/冷水病 | P1 |
| _Streptococcus agalactiae / iniae_ | 罗非鱼链球菌病 | P1 |
| _Photobacterium damselae_ · _Yersinia ruckeri_ · _Lactococcus garvieae_ · _Tenacibaculum_ | 多种海淡水病害 | P2 |

> 建议 v0 先做 **P0(Aeromonas)** 跑通全 pipeline → 验证后再纳入 P1/P2(避免一上来范围过大拖垮关键路径)。

## 2. 数据源与获取

| 源 | 内容 | 获取方式 | 备注 |
|---|---|---|---|
| **INPHARED** (Millard lab) | 策展的 phage 基因组 + 元数据(月度) | 直接下载 GenBank/元数据表 | 起点最干净 |
| **NCBI** GenBank/RefSeq | 按宿主 taxid 检索 phage | Entrez/datasets CLI: `txid<host>[Organism] AND (phage OR bacteriophage)` | 注意去重叠 INPHARED |
| **PhageScope** | 大库 + 自动注释 (NAR 2024, 873K) | phagescope.deepomics.org (下载/API) | 用于补漏 + 交叉校验 |
| **MetaVR** (meta-virome.org) | UViGs 环境病毒，IMG/VR 官方 successor (24.4M UViGs / >12M vOTU, NAR 2026 D801) | **REST API** (meta-virome.org/api/docs, GET/POST) + 免登录 | **替代旧 IMG/VR**(后者需 JGI 账号、难程序化)；含 curated 真核宿主 + 预测结构；③virome 主用、底座补充。⚠ MetaVR 在线② 同一 NAR Database issue → 线② 须守 host 切分+安全+设计 niche，勿撞"大库" |
| **宿主菌基因组** | 提 prophage (温和噬菌体来源) | NCBI 下宿主基因组 → geNomad/VIBRANT | 把溶原性病原噬菌体纳入 |

**去重**: 跨源合并后按 ≥95% ANI 去冗 (CheckV + 聚类),保留代表序列 + 记录冗余成员。

## 3. 数据清洗 (主要工作量, AI 协作可控)
1. **宿主名归一化**: 自由文本宿主 → NCBI taxid (建映射表, 人工 + AI 校验歧义)
2. **质控**: CheckV 完整性/污染 → 设阈值(如 completeness ≥50% 或分级标注)
3. **元数据 schema 统一**(三线必须共用):
   `phage_id · source_db · host_taxid · host_name · genome_len · completeness · checkv_quality · lifestyle · taxonomy_family/genus · host_pred · n_vir_genes · n_arg · lysogeny_flag · n_depolymerase · n_endolysin · …`

## 4. 注释 pipeline (模块化, 每模块输入=去冗基因组集)

| 模块 | 工具 | 产出字段 |
|---|---|---|
| 质控/完整性 | CheckV | completeness, contamination, quality |
| 分类 | geNomad + vConTACT3 + **VIRIDIC(全基因组相似度,family-level demarcation)+ 多基因 proteomic tree** (+ ICTV VMR 对齐) | family/genus, **new-clade flag**(robust,非单基因) |
| Lifestyle | BACPHLIP / PhaTYP | virulent vs temperate |
| 宿主预测 | iPHoP (+ CHERRY 交叉) | host_pred, confidence |
| 基因注释 | Pharokka → Phold → Phynteny (复用 pc031) | CDS, PHROG 功能, 结构注释 |
| **安全筛查** ⭐② | 毒力 VFDB · ARG (CARD/AMRFinderPlus/ResFinder) · 溶原模块 (integrase/recombinase/repressor) · toxin | n_vir, n_arg, lysogeny_flag, 安全等级 |
| **酶注释** ⭐① | depolymerase (PhaLP/dbAPIS/HMM) · endolysin · holin/spanin · 结构 (ESMFold/AlphaFold + Foldseek vs PDB)。**pan-domain 多家族,差异化于 EndoA3 单 motif 先例** | n_depolymerase, n_endolysin, 结构域架构 |

> ⭐ 标注=各线的差异化卖点所在(①酶、②安全)。

## 5. 统一输出
- **master 注释表** (parquet/sqlite): 每行一 phage, 含 §3 schema 全字段 → 三线直接消费
- **per-phage 卡片** (②web 的数据源): lifestyle + 宿主谱 + 安全 flag + 可用酶
- **序列与注释文件库**: 供 ①酶提取 / ③mapping reference

## 6. 项目结构 + 工具化策略 (DEC-D014 已定案)
**落点**：不新建 pc032 —— 直接在 **pc031 内 qproj**(用户已迁 qproj，1xx=Hp3 原研究)。底座编号 **4xx**：
`401-collect`(数据源拉取) · `402-dereplicate` · `403-annotate`(主 pipeline) · `404-safety` · `405-enzymes` · `406-master_table`。
三线：5xx(线①) / 6xx(线②) / 7xx(线③)。重型计算走西农/现有 HPC；`data/` symlink 出仓。

**工具化策略 (做 L1 不做 L2)**：把底座做成**内部可复用 pipeline**(L1)，**不做发布级软件**(L2)。
- **复用现成工具、不重造**：geNomad / CheckV / Pharokka→Phold→Phynteny / iPHoP / VIRIDIC / BACPHLIP。
- **per-host 参数化**：host taxid 作 Snakemake wildcard，`config.yaml`(host 清单+参数)驱动 → 一菌跑通换菌只改 config。重复的 download+HPC 注释走轻量 **Snakemake**(`workflow/`)，后处理+master 表+图走 **qproj 4xx**。
- **数据获取**：host genome(提 prophage) + phage(INPHARED/NCBI/PhageScope/MetaVR) + plasmids(可选，查 ARG/毒力来源对照)。
- **避免过度工程化红线**：不做 web UI(线②平台除外，它是 deliverable)、不发 pip/conda、不写完整测试/教程、hardcode 水产清单 OK、config 而非 CLI 参数。
- **发表的是产出的数据/资源**(线②DB、线①catalog)，不是 pipeline 本身。
- 可参考结构：MetaPhage(Nextflow) / nf-core/viralmetagenome(线③ 可直接用) / Pharokka 的 Snakemake 集成。

## 7. 算力估算 (粗)
- P0 Aeromonas 子集: 数百–千级基因组,注释 pipeline 单节点数小时–1 天级
- 全 P0+P1+P2: 万级基因组,HPC 并行 1–数天;结构预测(ESMFold)是最重步,按酶候选数限量跑

## 8. TODO
- [ ] 冻结宿主病原终稿清单 (§1) — **你定**
- [ ] 确认 INPHARED/PhageScope/IMG-VR 获取权限与最新入口
- [ ] pin 工具环境 (conda/uv lock) — 复用 pc031 环境为基
- [ ] master schema 字段终稿 (三线 review 后冻结)
- [ ] repo 命名 + HPC 部署位置
- [ ] 谁搭 v0 (你 + 哪个学生)
