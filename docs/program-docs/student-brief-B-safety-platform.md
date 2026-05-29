# 学生 B — onboarding brief: 线② 水产病原噬菌体 安全筛查 / 设计平台 (web server)

> **状态**: 骨架 v1 (2026-05-29, 待细化) · **学生**: TODO · **导师署名**: 你 lead/通讯 · **母战略**: `aquaculture-track-record-plan-v1.md`
> **定位**: high-value 线,**最强 novelty (三方一致)** —— 最强 resource 信号,复刻 TCMSP/ViroProfiler "resource maker" 身份;对接 NMDC / 数据要素× / 818 安全性逻辑。
> **开工优先级**: 三线中**最先启动** —— 本线 + 综述**即刻并行 sprint** (DEC-D012)。理由: NAR Database 硬 deadline 倒逼 + 本线 sprint 顺产线① 需要的 curated inventory。
> **硬 deadline (NAR Database issue)**: **7/1 pre-submission inquiry → 8/15 manuscript**;且站点须**免登录全功能**(comprehensiveness + 公开可访问是过稿门槛)。过不去时降级投 *Database* (Oxford) / *Scientific Data*。

## 一句话目标
把共享底座**产品化**为一个**面向噬菌体疗法落地**的水产病原噬菌体在线平台: 统一注释 + **治疗安全性筛查 (毒力/ARG/溶原模块)** + 宿主谱,并用合成生物学做 1 个 "safe phage 改造" proof-of-concept——从 descriptive resource 升维到 generative design platform。

## 依赖共享底座
- **全底座** (B 线本质就是底座的对外产品化)
- 安全筛查模块 (VFDB / CARD / AMRFinderPlus / 溶原模块检测) 为 B 的核心卖点

## 数据源
- 全底座水产病原噬菌体基因组集 + 注释结果

## 分析步骤 (dry + 工程)
1. 固化数据 schema (与 A/C 共用) + 安全筛查规则 (毒力/ARG/integrase/repressor/toxin)
2. 每个 phage 计算"治疗适配性"卡片: lifestyle · 宿主谱 · 安全 flag · 可用酶
3. **web server**: 前后端 + 可检索/可下载 (你已确认资源充足、建得快)
4. POC (**safe-phage 逆向工程设计层**, 非纯筛查/描述): 选 1 个携带溶原/毒力模块的 phage → 自动定位**溶原模块切除靶点** (integrase / repressor / 毒力 cassette 的边界与 att 位点) → 输出去除该模块的改造版设计。⚠ 这一**设计层**是区别于纯描述性 DB 的关键 novelty (三方裁决: 对标 Prophage Activation 平台 / CRISPR-avoidant phage 管线等"设计层"竞品)。
5. (验证, 见下)

## DBTL 验证 (POC)
- **Build**: 合成伙伴合成改造后的元件 / genome 片段
- **Test**: 验证改造版仍 lytic、且目标模块已失活 (体外)
- 仅做 1 个 POC, 不做完整工程化迭代 (那是回国研究内容)

## 目标期刊
- 主: **NAR Database issue** (IF~14+; ⚠ **年度提交窗口 ~9–10 月** + comprehensiveness 门槛,按此倒排)
- 备选: *Database (Oxford)* / *Scientific Data* (web server 门槛过不去时)

## 竞品 / 查重 (动笔前再 update)
- ⚠ **未检索到针对鱼虾病原的专门 phage 数据库** (gap 真实)
- 通用大库 **PhageScope** (NAR 2024, 873K) / **INPHARED** 存在,但**不按水产宿主切分、不做治疗安全性筛查、无 safe-phage 设计** → 这三点是你的差异化,必须在论文里显式对标。PhageScope/Sphae 等是上游 primitive,非竞品。
- **竞品矩阵** (三方补全,论文须逐一对标):IMG/VR v4 (`10.1093/nar/gkac1037`)、PhagesDB (`10.1093/bioinformatics/btw711`)、PhageDive (NAR 2025, `10.1093/nar/gkae878`)、PhageLeads (`10.3390/v14020342`)、FVD (水产**病毒** DB,但**非 phage / 非治疗向**)。
- **novelty 锚点** (区别于上述全部):**水产 host 切分 + 治疗安全评分 + safe-phage 设计层** 三者叠加。

## 里程碑
- M1 (2026-07): schema + 安全筛查规则冻结
- M2 (2026-09): web server alpha 上线
- M3 (2026-10): POC 验证 + 数据冻结 (赶 NAR 窗口)
- M4 (2026Q4/2027Q1): 投稿

## TODO
- [ ] 学生姓名/背景 + web 技术栈
- [ ] 平台命名 (呼应回国"国家级平台"愿景)
- [ ] 是否申请域名/长期托管 (TCMSP 模式: 持续可访问 = 持续引用)
- [ ] prophage+defense 模块是否并入 (原线④降级后归并到此)
