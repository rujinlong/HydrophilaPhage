#!/usr/bin/env python3
"""Codon-optimize Hp3 phage-encoded enzymes for GCATbio synthesis (E. coli / cell-free TXTL)."""
import sys, traceback
from dnachisel import (DnaOptimizationProblem, EnforceTranslation, AvoidPattern,
                       EnforceGCContent, CodonOptimize)
try:
    from dnachisel import reverse_translate
except ImportError:
    from dnachisel.biotools import reverse_translate
from Bio.Seq import Seq

FAA = "/Users/allen/github/rujinlong/pc031-aquaPhage/analyses/data/00-raw/d14-taxonomy/hp3_proteins.faa"
OUT = "/Users/allen/github/rujinlong/pc031-aquaPhage/docs"

targets = [
    ("hp3_CDS_0070", "hp3_0070_endolysin", "Amidase endolysin (PHROG822 Amidase_2 + PG_binding) — MVP 主候选", "Tier1"),
    ("hp3_CDS_0069", "hp3_0069_holin1",   "Holin #1 (PHROG7045) — 膜蛋白, 与 endolysin 共表达验证协同", "Tier1"),
    ("hp3_CDS_0099", "hp3_0099_holin2",   "Holin #2 (PHROG7045) — 可选增强", "Tier2"),
    ("hp3_CDS_0055", "hp3_0055_tailfiber","Tail fiber (PHROG5986, novel) — depolymerase 假设 wet-lab 判决 (五重 in-silico 阴性, 不预设)", "Tier3"),
]

# --- parse faa (single-line seq under each header) ---
seqs, cur = {}, None
for line in open(FAA):
    line = line.strip()
    if line.startswith(">"):
        cur = line[1:].split()[0]; seqs[cur] = ""
    elif cur:
        seqs[cur] += line
def find(cds):
    for k, v in seqs.items():
        if k.endswith(cds): return v
    return None

restr = {"EcoRI":"GAATTC","BamHI":"GGATCC","NdeI":"CATATG","XhoI":"CTCGAG",
         "HindIII":"AAGCTT","NcoI":"CCATGG","SalI":"GTCGAC","NotI":"GCGGCCGC"}

res = []
for cds, name, desc, tier in targets:
    prot = find(cds)
    if not prot:
        print("MISSING", cds, file=sys.stderr); continue
    prot = prot.rstrip("*")
    tagged = prot + "HHHHHH"               # C-terminal His6
    try:
        dna = reverse_translate(tagged)     # initial back-translation (no stop)
        cons = [EnforceTranslation()] + [AvoidPattern(s) for s in restr.values()] \
               + [EnforceGCContent(mini=0.35, maxi=0.65, window=50)]
        prob = DnaOptimizationProblem(sequence=dna, constraints=cons,
                                      objectives=[CodonOptimize(species="e_coli")], logger=None)
        prob.resolve_constraints(); prob.optimize()
        orf = str(prob.sequence)
        final = orf + "TAA"                 # append stop
        tr = str(Seq(orf).translate())
        ok = (tr == tagged)
        gc = 100 * (final.count("G") + final.count("C")) / len(final)
        hits = [n for n, s in restr.items() if s in final]
        res.append((name, desc, tier, prot, tagged, final, gc, ok, hits))
        print(f"{name}: {len(final)}bp GC{gc:.1f}% transOK={ok} residual_sites={hits}")
    except Exception as e:
        print("ERR", name, repr(e), file=sys.stderr); traceback.print_exc()

# --- write FASTA ---
with open(f"{OUT}/gcatbio-orf-order-hp3.fasta", "w") as f:
    for name, desc, tier, prot, tagged, final, gc, ok, hits in res:
        f.write(f">{name} codon-opt:E.coli C-His6 len:{len(final)}bp GC:{gc:.1f}%\n")
        for i in range(0, len(final), 70):
            f.write(final[i:i+70] + "\n")

# --- write markdown order sheet ---
with open(f"{OUT}/gcatbio-orf-order-hp3.md", "w") as f:
    f.write("# GCATbio ORF 合成清单 — Hp3 phage-encoded enzymes\n\n")
    f.write("> 由 `/tmp/codon_opt_hp3.py`(DNAChisel) 生成 · 配套方案见 `enzybiotic-synthesis-proposal.md`\n\n")
    f.write("## 合成规格\n")
    f.write("- **codon-optimized for *E. coli*** (cell-free TXTL 兼容)\n")
    f.write("- 每条 ORF = ATG 起始 + **C-末端 His6 tag** + stop(TAA)\n")
    f.write("- 已规避常用酶切位点: " + ", ".join(restr.keys()) + "\n")
    f.write("- GC 控制 35–65% (滑窗 50 bp)\n")
    f.write("- ⚠️ **GCATbio 可用自家引擎按其合成工艺 re-optimize**;蛋白序列是 ground truth,DNA 是参考版\n")
    f.write("- 源序列: `analyses/data/00-raw/d14-taxonomy/hp3_proteins.faa` (Hp3 / GenBank PX754746.1)\n\n")
    f.write("## ORF 清单\n\n")
    f.write("| ORF | Tier | aa(+His6) | bp | GC% | transOK |\n|---|---|---|---|---|---|\n")
    for name, desc, tier, prot, tagged, final, gc, ok, hits in res:
        f.write(f"| {name} | {tier} | {len(tagged)} | {len(final)} | {gc:.1f} | {'✓' if ok else '✗'} |\n")
    f.write("\n")
    for name, desc, tier, prot, tagged, final, gc, ok, hits in res:
        f.write(f"### {name}  [{tier}]\n{desc}\n\n")
        f.write(f"- 蛋白 {len(prot)} aa (+C-His6 = {len(tagged)} aa) · ORF {len(final)} bp · GC {gc:.1f}% · translation-check **{'PASS' if ok else 'FAIL'}**")
        if hits: f.write(f" · ⚠️残留位点 {hits}")
        f.write("\n\n")
        f.write(f"**Protein (+C-His6):**\n```\n{tagged}\n```\n\n")
        f.write(f"**Codon-optimized ORF (DNA, ready to synthesize):**\n```\n{final}\n```\n\n")
    f.write("## 诚实边界（写进合成单备注）\n")
    f.write("- `hp3_0055` **不得标注为 depolymerase**(Pfam/InterProScan/Phold-Foldseek/MMseqs2/AlphaFold 五重 in-silico 阴性);合成仅为一次性 wet-lab 终判其有无降荚膜活性。\n")
    f.write("- `hp3_0069`/`hp3_0099` 为 **holin(膜蛋白)**,cell-free 表达需脂质体/去垢剂;先做可溶的 `hp3_0070` endolysin(MVP)。\n")
    f.write("- A. hydrophila 革兰阴性 → 外源 endolysin 活性测定需配 **EDTA/OM-permeabilizer**(或 Artilysin 融合)防假阴性。\n")
print("WROTE", f"{OUT}/gcatbio-orf-order-hp3.{{fasta,md}}", "| ORFs:", len(res))
