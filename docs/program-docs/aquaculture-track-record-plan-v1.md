# 水产噬菌体疗法 Research Program — 海优 track record 补强战略 (v1)

> **状态**: v1 草案 (2026-05-29) · **目的**: 为 2027/2028 国家自然科学基金海外优青申请,建立"水产领域真实发表记录 + 连贯的可深耕科学问题域",修复历年评审三条核心批评。
> **决策记录**: 见本项目 `pm.sqlite` DEC-D010 (本文件落盘同时写入)。
> ⚠ **用语提醒**: 本文为内部规划,自由使用 "AI / DBTL / 启发式 / 平台" 等词;**任何内容写入申请书正文前,必须按 `CLAUDE.md` 雷区清单替换**(AI→具体方法名、删"启发式/暗物质/初步"等)。

---

## 0. 一句话战略

> 以 **_Aeromonas hydrophila_ / 水产病原噬菌体** 为**唯一锚点系统**,由 **3 名学生并行**推进 **3 条共享同一数据底座**的研究线,全部经 **合成生物学伙伴(2 周快速合成) + 王高学(水产 wet)** 做 **Design-Build-Test-Learn (DBTL) 闭环验证**,外加 **1 篇 你(lead/通讯) 的领域综述**——把"用通用生信迂回进入水产"重写为"用药物设计的闭环方法论深耕一个具体水产病害系统"。

---

## 1. 为什么做这个 (评审教训锚定)

历年 12 位函评 + 自查报告,核心短板**不是基础薄弱,是三条结构性批评**:

| # | 评审批评 (高频原话) | 本 program 如何修复 |
|---|---|---|
| **C1 逻辑断裂** | "已有研究基础与即将开展的研究衔接不好""换了赛道、只带走技术工具、没有可深耕的科学问题"(≥8 位) | 3 篇 + 综述全部锚定**同一病原系统** = 一个可深耕问题域,且你是 lead/通讯 |
| **C2 纯生信无验证** | "较多依赖生信分析与 AI 预测,缺乏动物实验等应用验证环节""与基础研究属性不符"(高频) | 每条线 dry candidate → **2 周合成 → 表达/裂菌/酶活验证**,DBTL 闭环 |
| **C3 药理背景割裂 / PI 独立性未展示** | "TCMSP 与噬菌体割裂"(山东大/周志刚);自查 ❺ "PI 独立性与博士后导师边界未划清" | **DBTL 闭环 = 药物设计核心范式**,把割裂背景重写为方法论根基;统筹 dry+wet+合成三方 = PI 证据 |

> **关键对照铁证**: 2024 题目直写"水产病原菌噬菌体疗法"→ 水产口专家给"非常优秀";2025 转"噬菌体启发式抗菌靶点(偏 AI)"→ 相关性批评激增。**评审买账"明确扎进水产病原菌机制",不买"通用生信迂回"。** 本 program 全程扎在病原系统内。

---

## 2. 团队与资源

| 角色 | 承担 | 关键资产 |
|---|---|---|
| 你 (Jinlong Ru) | 战略 + 共享底座 + 综述 + 全部 lead/通讯 | ViroProfiler · HPC · 数据库构建经验 (对标 TCMSP 5000 引) |
| 学生 A | 线① Aeromonas 酶挖掘 + 合成验证 | — (TODO: 姓名/背景) |
| 学生 B | 线② 安全筛查/设计平台 + web server | — (TODO: 姓名/背景) |
| 学生 C | 线③ 养殖系统 virome landscape | — (TODO: 姓名/背景) |
| 王高学 (西农) | 水产 wet 验证 + 共同通讯(证明合作真实) | 大口黑鲈模型 · 嗜水气单胞菌 MS01 · 绿色渔药工程中心 |
| 合成生物学伙伴 | **2 周快速基因/元件合成** | design-build-test 的 "build" 环节 |

> ⚠ **学生归属合法性 (待确认)**: 三个学生是你博士后期间实质指导、还是王高学的水产学生借你远程带?——**后者更理想**("我远程指导水产学生做噬菌体生信" = 合作 + 能带交叉团队的完美证据);若为前者,注意博士后导师可能也需挂名,确保仍能写成"独立/共同指导"。落笔前确认。

---

## 3. 架构: 一个共享底座 + 三个上层应用 + DBTL 验证层

```
┌─────────────────────────────────────────────────────────────┐
│  共享数据底座  (你 + 最强学生主导, 2–4 周, 关键路径)              │
│  · 水产病原噬菌体统一基因组集 (NCBI/INPHARED/IMG-VR/PhageScope) │
│    宿主: Aeromonas / Vibrio / Edwardsiella / Flavobacterium /  │
│          Streptococcus / Photobacterium / Yersinia ruckeri …  │
│  · 统一 ViroProfiler 注释 pipeline:                            │
│    CheckV · geNomad/vConTACT3 · BACPHLIP/PhaTYP · iPHoP ·      │
│    Pharokka/Phold/Phynteny · 安全筛查(VFDB/CARD/AMRFinder +    │
│    溶原模块) · depolymerase/endolysin(PhaLP/dbAPIS/Foldseek)   │
└──────────────┬──────────────┬──────────────┬─────────────────┘
               │              │              │
        ┌──────▼─────┐  ┌─────▼──────┐  ┌────▼─────────┐
        │ 学生A 线①   │  │ 学生B 线②   │  │ 学生C 线③     │
        │ Aeromonas   │  │ 底座产品化   │  │ 养殖系统virome│
        │ 泛基因组+    │  │ +web server │  │ 公共SRA重分析 │
        │ 酶系统挖掘   │  │ +安全筛查/   │  │ 用底座phage   │
        │             │  │  设计平台    │  │ 当reference   │
        └──────┬─────┘  └─────┬──────┘  └────┬─────────┘
               │              │ (POC)         │ (保持 dry)
        ┌──────▼──────────────▼───────┐       │
        │  DBTL 验证层                  │       │
        │  合成伙伴(2周build) + 王高学wet│       │
        │  ①top酶候选: 表达→裂菌谱/酶活  │       │
        │  ②safe phage: 去毒力/溶原模块 │       │
        └──────────────────────────────┘       │
               │              │                │
          Viruses→         Database→          mSystems
        MicrobiolSpectrum/  NAR Database       /Env.Microbiome
        AEM/IJBM            issue
               └──────── 全部互相引用, 口径一致 → "系列 program" ────────┘
                         + ④ 你(通讯)的 DBTL 视角领域综述 (伞)
```

**关键路径 = 共享底座**。底座没搭好,三个学生空转。先你带最强学生 2–4 周出底座 v0,再三线并行。

---

## 4. 共享底座 spec (线①②③ 共用)

**数据源** (按宿主病原拉全 phage 基因组):
- NCBI GenBank/RefSeq · **INPHARED** (Millard lab) · **IMG/VR** (JGI) · **PhageScope** (NAR 2024, 873K) · 各病原菌的 prophage (从 host 基因组用 geNomad/VIBRANT 提)
- 目标宿主清单 (鱼虾主病原): _Aeromonas hydrophila/salmonicida/veronii_ · _Vibrio anguillarum/harveyi/parahaemolyticus_ · _Edwardsiella tarda/ictaluri/piscicida_ · _Flavobacterium columnare/psychrophilum_ · _Streptococcus agalactiae/iniae_ · _Photobacterium damselae_ · _Yersinia ruckeri_ · _Lactococcus garvieae_ · _Tenacibaculum_ (TODO: 终稿固定清单)

**统一注释 pipeline** (ViroProfiler 封装):
1. 质控/完整性: CheckV, dedup (95% ANI)
2. 分类: geNomad, vConTACT3 (+ ICTV VMR 对齐), 新科/属候选标记
3. lifestyle: BACPHLIP / PhaTYP (virulent vs temperate)
4. 宿主预测: iPHoP / CHERRY
5. 基因注释: Pharokka → Phold → Phynteny
6. **治疗安全筛查**(②核心, 也供①③): 毒力基因 VFDB · ARG (CARD/ResFinder/AMRFinderPlus) · 溶原模块 (integrase/recombinase/repressor) · 已知 toxin
7. **酶注释**(①核心): depolymerase (PhaLP, dbAPIS, HMM) · endolysin · 结构 (ESMFold/AlphaFold + Foldseek 对 PDB)

> 数据清洗是主要工作量 (你已确认 AI 协作可控): 重点是宿主名归一化、重复基因组去冗、注释 schema 统一——**三条线必须共用同一 schema**,否则系列叙事破功。

---

## 5. 三条线 + 优先级 (真正的"保险"逻辑)

| 线 | 定位 | dry | DBTL 验证 | 目标刊 (升级后) |
|---|---|---|---|---|
| **① Aeromonas 酶挖掘** | **must-win** (最快/最确定/有 Hp3 wet 锚点) | Aeromonas phage 泛基因组 + depolymerase/endolysin 多样性 | 合成 top 1–3 候选 → 表达纯化 → 跨病原裂菌谱 + 酶活 | *MicrobiolSpectrum* / *AEM* / *Int J Biol Macromol* |
| **② 安全筛查/设计平台** | **high-value** (最强 resource 信号) | 底座产品化 + web server + 安全筛查框架 | 改造 1 个 safe phage (去毒力/溶原) 做 POC | **NAR Database issue** (⚠ 年提交窗口 ~9–10月) |
| **③ 养殖系统 virome** | **stretch** (最贴生态 narrative,方法学风险最高) | 公共 SRA 重分析 (大口黑鲈/对虾系统), 用底座 phage 当 ref | 保持 dry (不强塞 wet) | *mSystems* / *Environmental Microbiome* |
| ~~prophage+defense~~ | **降级** (首创已被 2025 *Fish & Shellfish Immunol* 抢) | 并入②的一个分析模块,不独立 | — | — |

**保险 = 至少 1 篇你通讯的水产论文 accepted/见刊**(从 0→1 是质变,直接拆掉 C1)。①就是这个 1 → 压最强资源确保它成。并行三条 = 拉满"至少 1 篇成"的概率 + 博 2–3 篇 upside,**不是赌三篇全中**。

---

## 6. 第四产出: 领域综述 (你 lead/通讯, 低成本高回报)

- landscape 已证实该领域**缺系统综述**。
- 主题: "水产噬菌体疗法的资源、生物信息学与 DBTL 设计现状/展望"
- 价值: ①不需新数据、最快 ②高引 ③**一举确立 domain authority,正面反驳"对水产病害了解不深"** ④把三个学生的工作框进去引用,系列感拉满。
- 定位: supporting(评审不当硬成果),但是最强的"我属于这个领域"信号。
- 目标刊: TODO (Viruses/Trends in Microbiology/npj 类综述位)

---

## 7. 时间线 (并行版, 倒排 2027 申请)

```
2026-06        共享底座 v0  (你 + 最强学生 · 关键路径)
2026-07 起     三线并行启动 + 你开写综述
2026-07~09     ① dry 完成 → 选候选 → 合成(2周) → wet 验证
2026 Q4        ① 投 MicrobiolSpectrum/AEM · 综述投出
2026Q4/27Q1    ② web server 上线 + 论文 → 冲 NAR (按其 9–10月窗口倒排)
2027 Q1        ③ 投 mSystems
2027 Q1–Q2     收割: ≥1 见刊 + 2 under review + 综述 → 喂申请
```

---

## 8. 对申请书的价值映射

| 申请书段落 | 现状 (致命) | 本 program 落地后 |
|---|---|---|
| 主要学术成绩 / 研究工作总结 | 水产真实发表 = **0** | N 篇你通讯、锚定同一系统的水产噬菌体论文 = 可深耕问题域 (修复 C1) |
| 回国研究计划 | "可行性论证薄弱""缺 preliminary" | dry+wet+合成 闭环已跑通 = 现成 preliminary + 平台雏形;**"设计平台"完整版作回国愿景,无缝同源** (修复 C2/可行性) |
| 合作基础 (D 盲区) | 外部专家对西农/王高学**零提及** | 与王高学**共同通讯** + 合成伙伴 = 多方合作可查 (把盲区变武器) |
| 政策武器对接 | — | ②安全筛查/NAR 平台 → NMDC / 数据要素×;DBTL 治疗剂 → 818 安全性逻辑 / 新兽药注册 |

---

## 9. 风险与纪律 (不可妥协)

1. **验证聚焦**: 每条线只验证 top 1–3 候选,不追求穷尽。
2. **体外即可**: 裂菌谱/酶活足以支撑论文;in vivo 留给 Hp3 主线 + 回国计划,现在不做。
3. **DBTL 只做一轮 POC**: 无限工程化迭代是回国研究内容,不是现在的 track record 任务。
4. **质量 > 数量**: 评审反感堆砌("23 篇""创新点过多");靠共享底座 + 系列叙事 + 你通讯,把三篇变成一个 program,而非"灌水三连"。
5. **共享 schema**: 三线注释口径必须统一,否则系列叙事破功。
6. **NAR 窗口**: ②若冲 NAR Database issue,按其年度提交窗口(~9–10月)+ comprehensiveness 门槛倒排。
7. **③方法学边界**: bulk metagenome vs VLP-enriched 必须说清,否则被批"viral signal 不可靠"。
8. **不撞车复核**: 每条线动笔前,各自 brief 内的"竞品/查重"小节须再 update 一次 (领域在动)。

---

## 10. 待办 / 下一步 (TODO)

- [ ] 确认 3 个学生姓名、背景、归属合法性 (§2 注)
- [ ] 固定底座宿主病原终稿清单 (§4)
- [ ] 三份学生 onboarding brief 细化 (见同目录 `student-brief-{A,B,C}-*.md`)
- [ ] 综述 outline + 目标刊确定 (§6)
- [ ] 与合成生物学伙伴对齐 build 能力边界 (基因长度上限/密码子优化/表达系统)
- [ ] 与王高学对齐 wet 验证排期 + 共同通讯署名
- [ ] 即时增益: 把"已启动 Hp3 延伸 + 多方合作"写进**2026 这一稿**回国计划的 preliminary basis (补 D 盲区)

## 11. 三方 DeepResearch 交叉验证后的调整 (2026-05-29, DEC-D012)

三方(Claude / Gemini / ChatGPT)确认三线 + 综述位**全 GO、无一 no-go**;据多引擎新增证据调整(详见 `literature-due-diligence-SYNTHESIS-3way.md`):
- **开工顺序改**:综述 + 线② sprint **即刻并行**(NAR Database **7/1 pre-submission + 8/15 稿 + 站点免登录** 硬 deadline 倒逼)→ 线① 第一篇全研究稿 → 线③ 最后。(原"线①先"被 NAR 日历推翻。)
- **线①**:加 **AI 结构预测(Foldseek/Phold/ProstT5)暗物质酶挖掘**维度,绕开 BLAST 失效 + 已发表单酶先例(LysE/PlyD4);避 Vibrio。
- **线②**:加 **safe-phage 逆向工程设计层**(溶原模块切除靶点),不止筛查。
- **线③**:SRA/ENA **实跑盘点(DEC-D013)证伪"数据充足"**——水产 VLP run≈0、可挖 bulk 仅 ~139 条 → **降级为线②/综述的 viral-from-bulk 支撑层,不作独立全研究稿**。原 VLP-first 立场只在自测序补数据时才适用。NAR sprint 见 `sprint-NAR-review-line2.md`。
- **三方未覆盖的三盲区(立项前必处理)**:① 学生能力 vs 线难度匹配(线② web 工程量最大)② 实跑 SRA/ENA 盘点给可用 run 数 ③ 818/新兽药政策对接(program 叙事)。

---

*关联文件*: `student-brief-A-aeromonas-enzymes.md` · `student-brief-B-safety-platform.md` · `student-brief-C-virome-landscape.md` · `literature-due-diligence-SYNTHESIS-3way.md` · 母项目 `~/github/rujinlong/pc031-aquaPhage` (Hp3/HydrophilaPhage)
