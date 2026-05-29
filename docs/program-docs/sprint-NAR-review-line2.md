# 综述 + 线② NAR 2027 sprint 计划 (DEC-D013)

> 来源:NAR deadline 经 OUP 官方核实 + 三方裁决(DEC-D012)+ SRA 实跑盘点(DEC-D013)。今天 2026-05-29。
> **开工顺序(最终)**:综述 + 线② **即刻并行 sprint**(NAR 8/15 倒逼)→ 线① 第一篇全研究稿 → ~~线③~~ **已降级为支撑层**。

## 1. NAR Database Issue deadline(2027 issue,OUP 官方核实)
| 节点 | 日期 | 备注 |
|---|---|---|
| Pre-submission inquiry | **2026-07-01** | email Prof. Daniel Rigden(nardatabase@gmail.com),含 DB URL + 简述;**invitation only,不能直投** |
| 最早可投 | 2026-06-01 | — |
| **新库 full manuscript** | **2026-08-15** | 本项目走此线 |
| 出刊 | **2027 年 1 月**(Vol 55, D1) | — |
- **Web server 硬要求(逐字)**:免登录/免注册/无密码;投稿时即须**全功能、可评审**。
- 来源:`academic.oup.com/nar/pages/ms_prep_database` · `academic.oup.com/nar/article/54/D1/D1`

## 2. 综述(申请人 lead/通讯,零湿实验,7 月底独投)
- **角度(差异化)**:不写"phage therapy works",写"**from genomes to safe, designed phage products: a resource–compute–safety–enzyme–design pipeline**"(避开 *Fish & Fisheries* 2026 已占的"疗效+实施")
- **目标刊**:*FEMS Microbiology Reviews* / *Trends in Biotechnology* / *npj Viruses*
- **outline**:① 引言(194 号禁抗→病害→**资源/计算瓶颈**非疗效瓶颈)② 资源底座(基因组集现状/缺口/ViroProfiler 标准化注释)③ 安全筛查计算层(毒力/ARG/溶原判定=监管 gating)④ 裂解酶资源挖掘(depolymerase/endolysin)⑤ DBTL 逆向设计(safe-phage engineering)⑥ 缺口展望 → 引出线② web server
- **时点**:与线②解耦,7 月底先投(为线②引流 + 锁优先权)

## 3. 线② sprint 里程碑(对齐 8/15;现有底座=基因组集+ViroProfiler 注释+毒力/ARG/溶原筛查+酶注释)
- **M1** 数据冻结 + DB schema(read-only)
- **M2** 后端 API(FastAPI:检索/筛查/酶注释 REST + Docker)← **关键路径**
- **M3** 前端 alpha(浏览 + 安全筛查报告 + 酶查询,**无登录**)← **关键路径**
- **M4** safe-phage 逆向工程设计层 POC(规则引擎/打分定位溶原模块切除靶点)
- **M5** 公开部署 + 压测(免登录全功能 URL,外部可评审)
- **M6** manuscript(与 M5 并行,8/15 投)
- ⚠ **三盲区之一**:web server = 前后端+API+运维,工程量远超注释脚本;**M2–M3 是致命路径**。缓解:导师预置后端骨架、学生只填业务逻辑;或用 **streamlit/gradio 降前端工程量**换按时上线。

## 4. 倒排时间线
| 时段 | 线② | 综述 | 关口 |
|---|---|---|---|
| 5/29–6/13 | M1 数据冻结+schema | outline+§1–2 | — |
| 6/14–6/30 | M2 后端 API+Docker | §3–4 | — |
| **7/1** | URL 草稿就绪 | — | **pre-inquiry email Rigden** |
| 7/1–7/15 | M3 前端 alpha | §5–6+打磨 | — |
| ~7/31 | M4 设计层 POC | — | **综述投稿** |
| 8/1–8/10 | M5 公开部署+压测 | manuscript(并行 M6) | DB 须全功能可评审 |
| 8/11–8/14 | 冻结+免登录回归 | 终稿 | — |
| **8/15** | — | — | **NAR manuscript 投稿** |

## 5. 判断与退路
- **临界可行**;唯一致命路径=web server 工程不滑期(导师预置骨架 or streamlit)。7 月中 M3 前端跑不通就切退路:
  - **退路 A(同年)**:*Database* (Oxford)——滚动收稿无 8/15 死线,OUP 同源缓冲
  - **退路 B**:*Scientific Data* data descriptor(先发基因组集+注释,server 留 NAR 2028 / NAR Web Server Issue,后者 proposal 截止 ~12/20)
- 综述无 NAR 死线,**无论线②成败都 7 月底独立投出**。

## 6. 线③ 降级落点(DEC-D013,SRA 实跑盘点结论)
线③ 不独立成稿。对 **~139 条中国/东南亚 bulk 水产 shotgun + common carp 77 条 community WGS** 做 viral-from-bulk(geNomad/VIBRANT)二次挖掘,作**线②/综述的 landscape 支撑证据**。关键 accession:PRJNA905657(西藏鱼)、PRJNA1046569(小龙虾 virome)、PRJNA789348(东山湾水产水)、PRJNA1353574、PRJNA843132。(水产 VLP-enriched run≈0,坚持 VLP-first 须自测序补数据。)
