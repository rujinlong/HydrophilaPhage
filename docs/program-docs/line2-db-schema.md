# 线② 平台 — DB schema + API + 架构设计

> 水产病原噬菌体**安全筛查/设计平台**;对接 NAR 8/15(**免登录、全功能、投稿时可评审**);构建在"共享底座"(`shared-base-spec-v1.md`)之上。novelty = host 切分 + 治疗安全评分 + safe-phage 设计层(区别于 PhageScope/Sphae/IMG-VR/PhageDive)。

## 1. DB schema(核心表)
**`phages`**: phage_id(PK) · name · accession · host_genus · host_species · host_taxid · genome_len · gc · molecule(dsDNA) · checkv_completeness · checkv_quality · lifestyle(virulent/temperate) · taxonomy_family · taxonomy_genus · source_db · seq_path
**`safety`** ⭐: phage_id(FK) · n_vfdb_virulence · vfdb_hits(json) · n_card_arg · card_hits(json) · lysogeny_flag(bool) · integrase · repressor · recombinase · known_toxin · **safety_grade**(safe / caution / unsafe)
> 规则:有 ARG 或毒力基因 或 溶原模块(integrase+repressor)→ caution/unsafe;全清 → safe(治疗候选)。
**`enzymes`** ⭐: enzyme_id(PK) · phage_id(FK) · type(depolymerase/endolysin/holin/spanin) · domain_arch · length_aa · structure_model(ESMFold/AF) · foldseek_top_hit · predicted_activity
**`hosts`**: host_taxid(PK) · host_name · pathogen_of(鱼/虾 species) · disease
**`designs`**(设计层): design_id · parent_phage_id(FK) · removed_module · rationale · status

## 2. API endpoints(FastAPI)
- `GET /api/phages?host=Aeromonas&lifestyle=virulent&safe=true` — 检索/筛
- `GET /api/phage/{id}` — 治疗适配性卡片(lifestyle + host谱 + safety + enzymes)
- `GET /api/safety/{id}` — 安全筛查报告(VFDB/CARD/溶原 + grade)
- `GET /api/enzymes?type=depolymerase&host=...` — 酶查询
- `POST /api/design` ⭐ — safe-phage:输入 phage → 溶原模块切除靶点 + 改造设计
- `GET /api/download` — 基因组/注释批量下载(免登录)

## 3. web 架构
- 后端:FastAPI + SQLite(alpha)→ PostgreSQL;**Docker 化**
- 前端:**streamlit/gradio(alpha,压低前端工程量)** → React(后续);**全功能、免登录**(NAR 硬要求)
- 部署:西农/现有 HPC 或云;公开持久 URL(对标 TCMSP 持续可访问=持续引用)
- ⚠ **M2 后端 API + M3 前端是致命路径**(三盲区:web 工程量 > 注释脚本)——导师预置后端骨架 / streamlit 降工程量。

## 4. safe-phage 设计层逻辑(POC,区别于纯描述性 DB)
输入一个携带溶原/毒力模块的 phage → ① 注释定位 integrase/repressor/att 边界 + 毒力 cassette → ② 标记可切除模块 → ③ 输出"去除该模块"的改造 genome 设计 + 风险评分 → ④(合成伙伴 build → 验证改造版仍 lytic、模块已失活)。仅做 1 个 POC(完整工程化是回国研究内容)。

## 5. 里程碑
对齐 `sprint-NAR-review-line2.md §3`(M1 数据冻结+schema → M2 后端 API → M3 前端 alpha → M4 设计层 POC → M5 公开部署+压测 → M6 manuscript 8/15)。

## 6. 数据来源
全部来自共享底座(水产病原噬菌体基因组集 + ViroProfiler 注释 + 安全筛查 + 酶注释);线③ 降级后的 viral-from-bulk 结果(~139 条 bulk 二次挖掘)作为 landscape 补充层并入。
