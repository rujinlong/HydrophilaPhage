# Liang 的稿件 review 意见整理（供审阅）

> **来源**：`manuscript/feedback/manuscript-feedback-Liang.pdf`（19 页，Liang 在稿件 PDF 上的批注，annotation author = "Lenovo"）
> **稿件**："A novel lytic *Aeromonas* bacteriophage rescues largemouth bass from lethal *Aeromonas hydrophila* infection"（phage vB_AhyM_Hp3 / Hp3）
> **提取方式**：pymupdf 程序化提取全部 PDF annotation（5 处）+ 逐页视觉核对（p1 / p7 / p9）
> **提取日期**：2026-06-02
> **状态**：**仅提取整理**，未 draft response、未改稿——待你审阅、确认采纳与否后，再据此修改稿件。

## 概要

Liang 共留下 **5 处批注**（2 条中文文字意见 + 3 处黄色高亮），归并为 **2 条核心科学意见**：

| # | 类型 | 位置 | 一句话 | 严重度 |
|---|------|------|--------|--------|
| **C1** | 数据表述不准确 / Abstract ↔ Results 不一致 | Abstract（行 15–16）；Results §3.3.3（行 200–203）| Abstract 称 pH 6.0–10.0 稳定，实测为 pH 6–9 无差异、pH 10 降一个数量级 | Major |
| **C2** | 方法学概念错误 | Figure 3 caption（p9）| lysis curve 的 OD600 测的是细菌浓度，不是 phage titer | Major |

---

## 逐条意见

### C1 — pH 稳定性表述：Abstract 不准确、且与 Results 不一致

**Liang 批注原文**（p1，FreeText 红框）：
> ph6-9稳定性没有差异，ph=10的时候稳定性降低一个数量级

**所指稿件原文**：
- **Abstract（行 15–16，p1，已高亮）**：
  > "…stable across a wide range of temperatures (4–45 °C) and **pH (6.0–10.0)**."
- **Results §3.3.3 Phage stability analysis（行 200–203，p7，已高亮）**：
  > "The phage titer remained stable at approximately 10⁸ PFU/mL … in buffers with **pH values from 6.0 to 9.0**. A moderate, **one-log reduction** in titer was observed at **pH 10.0**, while the phage was completely inactivated at pH < 5.0 and > 11.0 (Figure 2 D)."

**问题解读**：Abstract 把稳定 pH 范围笼统写成 "6.0–10.0"，但 Results / Figure 2D 的真实数据是 **pH 6.0–9.0 稳定（titer 无差异）**、**pH 10.0 已下降一个数量级（one-log reduction）**。Abstract 的概括夸大了稳定上限，与 Results 自相矛盾。Liang 同时高亮了 Results 这段正确数据，作为对照锚点。

**建议修改方向**（供参考，待你定）：
- Abstract 改为与 Results 一致，例如：
  > "…stable across temperatures 4–45 °C and **pH 6.0–9.0**, with a one-log titer reduction at pH 10.0."
- 全文自查其它复述 pH 稳定范围处（如 Discussion / §3.3 小节标题 "Stable Across Temperature and pH"）是否也需同步对齐。

---

### C2 — Figure 3 caption：OD600 测的是细菌浓度，不是 phage titer

**Liang 批注原文**（p9，FreeText 红框）：
> OD600测定的不是噬菌体的滴度，测得是细菌浓度。

**所指稿件原文**（Figure 3 caption，p9，已高亮）：
> "Figure 3: 48h lysis curve of Hp3. … **The phage titer was determined by measuring the OD600 absorbance.** The data are presented as the mean ± SD …"

**问题解读**：Figure 3 是 48 h lysis curve（纵轴 OD600 随时间），监测的是**细菌密度的下降（裂解程度）**。caption 称 "phage titer was determined by measuring OD600" 在概念上错误——OD600 反映的是**细菌浓度 / 密度**，而非噬菌体滴度（phage titer 应由 double-layer agar / PFU 计数测定）。这是基础方法学概念错误，审稿人/读者很容易指出。

**建议修改方向**（供参考，待你定）：
- caption 改为准确表述，例如：
  > "Bacterial density was monitored as **OD₆₀₀** over time"（删去 "phage titer … OD600" 的说法）。
- 顺带核查：§2.7 *In Vitro* Lysis Assay（方法段）与 §3.3.4 Phage lysis curve（正文行 206–216）——方法段本身写的是 "the optical density at 600 nm of the cultures was recorded"（表述正确），请确认正文未在别处也把这条 lysis 曲线误称为 phage titer。

---

## 提取完整性说明

- PDF 全 19 页扫描，共检出 **5 处 annotation**：p1（高亮 + 文字）、p7（高亮）、p9（高亮 + 文字），已全部纳入上面 C1 / C2。
- 3 处高亮归属：p1 + p7 → **C1**（pH 表述）；p9 → **C2**（OD600）。2 条中文 FreeText 文字意见均已逐字转录。
- 未发现其它形式批注（无手写、无 pymupdf 未解析的 popup）。
- 注：本文档仅转录 Liang 的意见，未叠加 AI 自查的其它问题。
