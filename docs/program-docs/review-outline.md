# 综述 outline — 水产噬菌体疗法的资源/计算/安全/设计全栈

> 7 月底独投(锁优先权,为线② 引流);插旗 **resource–compute–safety–enzyme–design**;**避开** *Fish & Fisheries* 2026(faf.70055)/ Yang 2024 / Albarella 2025 / Landor 2026 已占的"疗效+实施"角度。
> 目标刊:*FEMS Microbiology Reviews* / *Trends in Biotechnology* / *npj Viruses* · 字数 ~6000–7000 · 你 lead/通讯,学生 C 协助文献+作图。

## 标题(候选)
"From genomes to safe, designed phage products: resource, computational, and design pipelines for aquaculture phage therapy"

## 章节
1. **引言**(~800):水产抗生素禁令(农业农村部 194 号)+ 病害负担 → 噬菌体绿色替抗 → **核心论点:瓶颈在资源/计算/设计基础设施,非疗效本身**(差异化于上述疗效综述)。
2. **资源底座**(~1200):水产病原噬菌体基因组现状=碎片化(单分离株为主)+ host-genus 采样偏倚(INPHARED:75% phage 集中 30 genera,鱼虾病原 underrepresented);通用大库(PhageScope NAR 2024 / IMG-VR / PhagesDB / PhageDive)**不按水产 host 切分**;标准化注释(ViroProfiler)。
3. **安全筛查计算层**(~1200):毒力(VFDB)/ARG(CARD)/溶原(integrase-repressor)判定 = 治疗噬菌体的**监管 gating step**(对接新兽药注册);描述性库不足(Sphae 是 host-agnostic pipeline 非 curated 水产库)。
4. **裂解酶资源挖掘**(~1200):depolymerase/endolysin 注释与功能预测;**序列法(BLAST/HMM)的暗物质盲区**(Vibrio Dep193 无可识别 domain)→ **AI 结构挖掘(Foldseek/Phold/ProstT5)**;已有单酶实例(LysE `10.1007/s12602-021-09880-7`、PlyD4 含斑马鱼体内 `10.1007/s00253-021-11752-7`、EndoA3 `10.1016/j.ijbiomac.2025.146934`)→ 凸显"系统性 catalog 缺位"。
5. **DBTL 逆向设计**(~1000):safe-phage engineering 的 Design-Build-Test-Learn;溶原模块切除 / 宿主范围工程;设计前沿(Prophage Activation 平台、CRISPR-avoidant phage 管线)。
6. **缺口与展望**(~800):提出"**need for a dedicated aquaculture phage resource + safety + design platform**"→ 自然引出线② web server(锁优先权)。

## 关键文献(三方尽调去重,真实 DOI)
- 资源/库:PhageScope `10.1093/nar/gkad979`、INPHARED `10.1089/phage.2021.0007`、IMG/VR `10.1093/nar/gkac1037`、PhagesDB `10.1093/bioinformatics/btw711`、PhageDive `10.1093/nar/gkae878`、Sphae `10.1093/bioadv/vbaf004`
- 酶:LysE/PlyD4/EndoA3(上)、Vibrio dep mining `10.1128/aem.01824-25`
- 工具:ViroProfiler、geNomad、CheckV、Foldseek、Phold、VIRIDIC `10.3390/v12111268`、ViPTree `10.1093/bioinformatics/btx157`、VICTOR
- 已占疗效综述(须显式区分):`10.1111/faf.70055`、`10.1016/j.aquaculture.2024.740925`、`10.3390/microorganisms13040831`、`10.1016/j.tim.2025.08.002`
- 方法学类比:Rey-Campos 2023 软体动物公共 SRA virome meta-analysis `10.3389/fmars.2023.1209103`

## 注
作动笔前用 add-citation / verify-refs 把上述 DOI 全部落 Zotero @citekey;政策段严守 EL-003(水产走兽药、不碰 818)。
