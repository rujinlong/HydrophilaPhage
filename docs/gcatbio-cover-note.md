# 给 GCATbio 的下单 cover note（草稿）

**收件**：董明（dongming@gcatbio.com）· 叶铭琪
**主题**：噬菌体酶基因合成 pilot 订单 + 学术合作探讨（Deng Lab × 华大新一产）

---

董明、铭琪：

非常感谢 6 月 5 日的交流。如当时所提，我们希望从一个**小规模 pilot** 起步，先把双方在「AI / 噬菌体研究 × 高通量 DNA 合成」上的协作流程跑通，再逐步扩大。

**首单（pilot）· 1 条 codon-optimized ORF**
- 基因：`hp3_0070` —— 来自我们一株 *Aeromonas hydrophila* 裂解性噬菌体 **Hp3**（GenBank **PX754746.1**）的 **amidase endolysin**（肽聚糖水解酶）
- 规格：**702 bp** · ATG + ORF + **C-末端 His6** + stop · **codon-optimized for *E. coli***（cell-free TXTL 兼容）· 已规避 8 个常用酶切位点（EcoRI / BamHI / NdeI / XhoI / HindIII / NcoI / SalI / NotI）· GC ≈ 55%
- 用途：cell-free 表达 + 体外抗菌活性验证（enzybiotic pilot）
- 附件：`gcatbio-orf-order-hp3.fasta`（**蛋白序列为 ground truth，DNA 为参考版，贵方可按合成工艺 re-optimize**）

**想请教**
1. 该 ORF 的**交期与报价**（含 / 不含 codon-opt re-optimization）？
2. 建议直接交付**线性 ORF**，还是**克隆进表达载体**（如 pET 系列）更便于我们后续 cell-free / 表达？

**关于合作模式**
我们更希望以**学术联合**推进（联合发表 / 案例共建），而非单纯采购——这与贵方和 CRG（沈玥老师参与的 *Nature* 2025 site-saturation 工作）的合作形态一致。pilot 顺利的话，下一步有两个更大的方向可一起做：
- ① *A. baumannii* 噬菌体 **RBP site-saturation 变体库**（数千条 oligo，AI 模型预测先验排序）；
- ② 噬菌体来源酶（endolysin / depolymerase）的 **ORF 库 + cell-free 筛选**。

期待回复，也欢迎线上详谈。

茹金龙（Jinlong Ru）
Deng Lab, TUM & Helmholtz Munich · jinlong.ru@tum.de

---

> 备注（不发给对方，内部）：本 pilot = brain DEC-D021 的 P1/P2 enzyme 线落地；配套方案 `enzybiotic-synthesis-proposal.md`；MVP 选 endolysin 因其可溶、cell-free 友好、证据最硬（PHROG822 Amidase_2）。诚实边界（hp3_0055 不当 depolymerase 卖、Gram⁻ 需 EDTA）见 order sheet。
