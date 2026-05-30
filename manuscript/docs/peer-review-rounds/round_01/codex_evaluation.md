# Round 1 Codex Evaluation — Taxonomy claim

## Executive summary

The Hp3+HJ05 **new-genus** claim is defensible as written: the manuscript gives VIRIDIC 83.65%, Mash isolation, terminase support, and VICTOR/GBDP genus-level corroboration. The **family-level** claim is only defensible as a provisional hypothesis, but the current title, abstract, figure caption, and conclusion read too much like an asserted taxon. Two must-fix issues would be reviewer-blocking: downgrade the frontmatter/caption language, and explicitly explain why VICTOR is used for genus rank but not for family-rank OPTSIL support. No new compute is required for Round 1; the fix is transparent framing.

## Detailed evaluation

### R1-01 — ViPTree \(S_G\) and vConTACT3 as family-rank evidence

Severity: major  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "To test whether the genus falls within any established family, we placed Hp3 in a whole-proteome tree of 5,633 reference prokaryotic dsDNA viruses (ViPTree): Hp3 branched as an isolated, deep lineage, its highest genomic similarity to any reference being only \(S_G\) = 0.073 (to the unclassified \emph{Rhizobium} phage vB\_RleS\_L338C), with no member of any recognized family approaching it."

> "As HJ05 is itself an unclassified member of the \emph{Caudoviricetes}, these convergent analyses indicate that Hp3 and HJ05 constitute a new genus that represents a putative new family-level lineage."

Verification reasoning:

The NLM critique is partly correct and partly overstated. The manuscript does **not** explicitly claim that \(S_G = 0.073\) crosses a formal family threshold; it uses the value as evidence of deep proteomic isolation. That use is acceptable because the internal context says family novelty is argued from whole-proteome isolation, terminase-large-subunit branching, and a caveated vConTACT3 signal, not from a universal threshold. However, the current paragraph moves directly from \(S_G\), vConTACT3 separation, and HJ05's unclassified status to "putative new family-level lineage" without telling the reader that \emph{Caudoviricetes} family demarcation has no universal quantitative threshold and remains an ICTV case-by-case decision. That is a real communication weakness.

One NLM subpoint is already handled in the manuscript:

> "we note, however, that L338C shares only \textasciitilde3\% genome-wide nucleotide identity with Hp3 (VIRIDIC), indicating that this protein-sharing link reflects a small number of conserved proteins rather than close kinship."

Recommendation:

Keep the ViPTree \(S_G\) value as evidence of deep isolation, but explicitly state that it is not a family threshold. Do not run a new core-gene analysis for this round. Add a family-rank caveat: the evidence supports a **putative family-level lineage pending broader sampling and formal ICTV evaluation**, not an established family.

### R1-02 — Single-genus/two-genome family framing

Severity: block  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "At the nucleotide level, VIRIDIC placed Hp3 and \emph{Aeromonas} phage HJ05 (GenBank accession OQ594355) within a single genus, sharing 83.65\% intergenomic similarity---above the 70\% genus threshold but below the 95\% species threshold---indicating that the two are distinct species of the same genus."

> "As HJ05 is itself an unclassified member of the \emph{Caudoviricetes}, these convergent analyses indicate that Hp3 and HJ05 constitute a new genus that represents a putative new family-level lineage."

Verification reasoning:

The attack on the **genus** assignment should be rejected: the manuscript gives a standard VIRIDIC genus-level argument and corroborates it with Mash, terminase, and VICTOR/GBDP. The attack on using a single two-genome genus as a prominent "new family" claim is real. The internal context says the authors know the family-level claim is a hypothesis, and that formal \emph{Caudoviricetes} family rank is ICTV-guided rather than threshold-based. The manuscript does not state this distinction clearly enough. A reviewer could reasonably read the current wording as trying to establish a family from one genus without formal demarcation criteria.

NLM's wording "violates current taxonomic frameworks" is too absolute for a manuscript that says "putative"; the better adjudication is that the paper can discuss a family-level hypothesis, but should not headline it as though the family is already delineated.

Recommendation:

Preserve the new-genus claim. Remove "putative new viral family" from the title/abstract/keywords and replace it with "deeply divergent" or "currently unclassified \emph{Caudoviricetes} genus." In the Results, retain only a bounded statement that Hp3+HJ05 may represent a putative family-level lineage pending broader sampling and formal ICTV evaluation.

### R1-03 — VICTOR genus-only reporting and family-level OPTSIL omission

Severity: major  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "Genome-based phylogeny and OPTSIL-derived taxon boundaries were further assessed with VICTOR \citep{2017-VICTOR_Meier-Kolthoff}, applying the Genome-BLAST Distance Phylogeny (GBDP) method to amino-acid sequences (recommended formula D6) for Hp3, HJ05, their nearest unclassified ViPTree neighbours, and the type species of eight major \emph{Caudoviricetes} families."

> "This genus-level assignment was independently corroborated by amino-acid genome-BLAST distance phylogeny (VICTOR/GBDP, formula D6), in which Hp3 and HJ05 again formed an exclusive genus-level cluster (pseudo-bootstrap = 100), well separated from the type species of eight major \emph{Caudoviricetes} families."

Verification reasoning:

This is the most important fix. The internal context explains the omission: VICTOR family-level OPTSIL clustering failed in this saturated-divergence region, merging four ICTV-recognized families, so the authors deliberately use VICTOR only for genus-level corroboration. The manuscript does not say this. Worse, the Methods phrase "OPTSIL-derived taxon boundaries" implies that multiple ranks were assessed, but the Results report only the genus-level cluster. That creates a reasonable appearance of selective reporting even though the omission is principled.

NLM's demand to "disclose the full OPTSIL clustering results" is too broad for the main text. Reporting an unreliable family partition as if it were a result would confuse the evidence. The minimal fix is to state that higher-rank OPTSIL partitions were inspected but not used as family evidence because they were unreliable for this calibration panel, consistent with known weak family-level resolution in VICTOR for deep prokaryotic-virus relationships.

Recommendation:

Revise Methods to say "genus-level OPTSIL boundaries" and add one sentence explaining that higher-rank OPTSIL partitions were inspected but not interpreted as family evidence. Revise Results to make VICTOR explicitly genus-only and to state the family-level claim rests on ViPTree isolation, terminase branching, and caveated vConTACT3 evidence, not VICTOR family OPTSIL.

### R1-04 — Title/abstract "putative new viral family" without formal ICTV proposal

Severity: block  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "\title{\bfseries A novel bacteriophage representing a putative new viral family rescues largemouth bass from lethal \emph{Aeromonas hydrophila} infection}"

> "Taxonomic and comparative genomic analyses indicate that Hp3 represents a distinct viral lineage, forming a putative new family within the class \emph{Caudoviricetes}."

> "As a representative of a putative new family, Hp3 exhibits the rapid lytic kinetics, broad environmental stability, and safe genomic profile desirable for a therapeutic agent."

Verification reasoning:

Verified. The manuscript has no TaxoProp, proposed family name, or formal family demarcation section. That is not fatal if the claim is framed as a provisional lineage hypothesis, but it is too prominent in the title and abstract. "Putative" helps, but the frontmatter still makes the family rank the primary discovery. For Microbial Biotechnology, this would likely invite a taxonomy reviewer to block acceptance or demand heavy revision before evaluating the therapeutic data.

Recommendation:

Remove the family-rank phrase from the title, abstract, and keywords. In the body, retain a cautious formulation: Hp3+HJ05 form a deeply divergent, currently unclassified \emph{Caudoviricetes} genus that may warrant family-level recognition pending broader sampling and formal ICTV evaluation.

### R1-05 — Novelty contextualization against unclassified/floating \emph{Caudoviricetes} and \emph{Aeromonas} phages

Severity: minor  
Verdict: PLAUSIBLE-BUT-UNVERIFIABLE

Quoted manuscript text:

> "Beyond its therapeutic potential, our genomic analysis shows that Hp3 represents a novel viral lineage. Together with its closest relative, \emph{Aeromonas} phage HJ05, it forms a distinct clade that falls outside any currently defined phage family within the \emph{Caudoviricetes}, indicating that aquatic ecosystems harbor phage diversity that remains poorly characterized."

Verification reasoning:

The manuscript's discussion is not as overstated as NLM claims; it says aquatic phage diversity remains poorly characterized, which is reasonable. The exact NLM claims that there are "over 600" floating genera and that extreme divergence is a recognized hallmark of \emph{Aeromonas} phages are plausible from the NLM excerpts, and the relevant bibliography entries exist (`2023-Abolishment_Turner`, `2022-Characterization_Bujak`), but I did not independently verify those exact numerical/generalized claims from full source text inside the repository. Bujak 2022 is about \emph{Aeromonas} autographiviruses and should not be used to imply that all \emph{Aeromonas} phages commonly show family-level divergence.

Recommendation:

Nice-to-have only. Add one discussion sentence placing Hp3 in the broader post-\emph{Caudovirales} context of many unclassified \emph{Caudoviricetes} genera and divergent \emph{Aeromonas} phage groups. Do not say Hp3 "simply joins" a pool of floating genera; that would undercut the actual Hp3+HJ05 genus evidence and the whole-proteome isolation.

## Implementation plan

1. [MUST-FIX] Downgrade the title and PDF title  
Target file: `manuscript/manuscript.tex`

Before:

```latex
  pdftitle={A novel bacteriophage representing a putative new viral family rescues largemouth bass from lethal Aeromonas hydrophila infection},
```

After:

```latex
  pdftitle={A deeply divergent Aeromonas bacteriophage rescues largemouth bass from lethal Aeromonas hydrophila infection},
```

Before:

```latex
\title{\bfseries A novel bacteriophage representing a putative new viral family
rescues largemouth bass from lethal \emph{Aeromonas hydrophila} infection}
```

After:

```latex
\title{\bfseries A deeply divergent \emph{Aeromonas} bacteriophage
rescues largemouth bass from lethal \emph{Aeromonas hydrophila} infection}
```

Verification criterion: `rg -n "putative new viral family" manuscript/manuscript.tex` returns no title/PDF-title hit.

2. [MUST-FIX] Reframe the abstract family claim as provisional  
Target file: `manuscript/manuscript.tex`

Before:

```latex
Whole-genome sequencing revealed an 84.75 kb double-stranded DNA genome
with a GC content of 59\%, confirming the absence of known antimicrobial
resistance or virulence genes. Taxonomic and comparative genomic
analyses indicate that Hp3 represents a distinct viral lineage, forming
a putative new family within the class \emph{Caudoviricetes}. Genome
annotation also identified several putative auxiliary metabolic genes,
```

After:

```latex
Whole-genome sequencing revealed an 84.75 kb double-stranded DNA genome
with a GC content of 59\%, confirming the absence of known antimicrobial
resistance or virulence genes. Taxonomic and comparative genomic
analyses indicate that Hp3 and its closest known relative,
\emph{Aeromonas} phage HJ05, form a deeply divergent, currently
unclassified genus within the class \emph{Caudoviricetes} that may
warrant family-level recognition pending broader sampling and formal
ICTV evaluation. Genome annotation also identified several putative auxiliary metabolic genes,
```

Verification criterion: the abstract contains "currently unclassified genus" and no longer contains "forming a putative new family".

3. [MUST-FIX] Replace the family-rank keyword  
Target file: `manuscript/manuscript.tex`

Before:

```latex
\noindent\textbf{Keywords:} \emph{Aeromonas hydrophila}; Bacteriophage;
Phage therapy; Aquaculture; Antimicrobial resistance; Novel viral family;
Auxiliary metabolic genes; Comparative genomics.
```

After:

```latex
\noindent\textbf{Keywords:} \emph{Aeromonas hydrophila}; Bacteriophage;
Phage therapy; Aquaculture; Antimicrobial resistance; Viral taxonomy;
Auxiliary metabolic genes; Comparative genomics.
```

Verification criterion: `rg -n "Novel viral family" manuscript/manuscript.tex` returns no hits.

4. [MUST-FIX] Change the Results subsection heading  
Target file: `manuscript/body.tex`

Before:

```latex
\subsection{Genomic Analysis Reveals Hp3 Represents a Putative Novel
Viral
Family}\label{genomic-analysis-reveals-hp3-represents-a-putative-novel-viral-family}
```

After:

```latex
\subsection{Genomic Analysis Places Hp3 in a Deeply Divergent
\emph{Caudoviricetes}
Genus}\label{genomic-analysis-reveals-hp3-represents-a-putative-novel-viral-family}
```

Verification criterion: the subsection heading no longer asserts "Putative Novel Viral Family".

5. [MUST-FIX] Make the VICTOR scope explicit in Methods  
Target file: `manuscript/body.tex`

Before:

```latex
Genome-based phylogeny
and OPTSIL-derived taxon boundaries were further assessed with VICTOR
\citep{2017-VICTOR_Meier-Kolthoff}, applying the Genome-BLAST Distance
Phylogeny (GBDP) method to amino-acid sequences (recommended formula D6)
for Hp3, HJ05, their nearest unclassified ViPTree neighbours, and the
type species of eight major \emph{Caudoviricetes} families.
```

After:

```latex
Genome-based phylogeny
and genus-level OPTSIL boundaries were further assessed with VICTOR
\citep{2017-VICTOR_Meier-Kolthoff}, applying the Genome-BLAST Distance
Phylogeny (GBDP) method to amino-acid sequences (recommended formula D6)
for Hp3, HJ05, their nearest unclassified ViPTree neighbours, and the
type species of eight major \emph{Caudoviricetes} families. Higher-rank
OPTSIL partitions were inspected but not used as family-level evidence
because family-level resolution is known to be weak for distant
prokaryotic viruses in VICTOR and, in our calibration panel, merged
several ICTV-recognized families.
```

Verification criterion: Methods now says "genus-level OPTSIL boundaries" and explains non-use of higher-rank OPTSIL partitions.

6. [MUST-FIX] Replace the key Results interpretation paragraph  
Target file: `manuscript/body.tex`

Before:

```latex
As HJ05 is itself an unclassified member of the \emph{Caudoviricetes},
these convergent analyses indicate that Hp3 and HJ05 constitute a new
genus that represents a putative new family-level lineage. This
genus-level assignment was independently corroborated by amino-acid
genome-BLAST distance phylogeny (VICTOR/GBDP, formula D6), in which Hp3
and HJ05 again formed an exclusive genus-level cluster (pseudo-bootstrap
= 100), well separated from the type species of eight major
\emph{Caudoviricetes} families.
```

After:

```latex
As HJ05 is itself an unclassified member of the \emph{Caudoviricetes},
these convergent analyses indicate that Hp3 and HJ05 constitute a new,
deeply divergent genus. This genus-level assignment was independently
corroborated by amino-acid genome-BLAST distance phylogeny
(VICTOR/GBDP, formula D6), in which Hp3 and HJ05 again formed an
exclusive genus-level cluster (pseudo-bootstrap = 100), well separated
from the type species of eight major \emph{Caudoviricetes} families. We
therefore did not use VICTOR family-level OPTSIL partitions as support
for family rank. In this saturated-divergence panel, that partition
merged \emph{Straboviridae}, \emph{Ackermannviridae},
\emph{Demerecviridae}, and \emph{Herelleviridae}, illustrating the
known weak family-level resolution of VICTOR for distant prokaryotic
viruses \citep{2017-VICTOR_Meier-Kolthoff}. Because family-level
demarcation in \emph{Caudoviricetes} has no universal quantitative
threshold and formal family creation generally requires multiple genera
plus core-gene and phylogenetic criteria
\citep{2021-Roadmap_Turner,2023-Abolishment_Turner}, we interpret the
ViPTree, terminase, and vConTACT3 evidence as supporting a putative
family-level lineage pending broader sampling and formal ICTV
evaluation, rather than an established family.
```

Verification criterion: Results explicitly says VICTOR family-level OPTSIL was not used as family-rank evidence and includes the ICTV caveat.

7. [MUST-FIX] Remove asserted "novel family" wording from Figure 4 caption  
Target file: `manuscript/body.tex`

Before:

```latex
content, and GC skew. (B) Protein-sharing network placing Hp3 in a novel
viral family cluster (green nodes). Nodes represent viral genomes, and
edge thickness corresponds to the number of shared protein clusters.
Edges within the novel family are colored red. (C) Phylogenetic tree
```

After:

```latex
content, and GC skew. (B) Protein-sharing network placing Hp3 within a
small, deeply divergent protein-sharing group (green nodes). Nodes
represent viral genomes, and edge thickness corresponds to the number of
shared protein clusters. Edges connecting the Hp3-associated group are
colored red. (C) Phylogenetic tree
```

Verification criterion: Figure caption no longer says "novel viral family cluster" or "Edges within the novel family".

8. [MUST-FIX] Downgrade the conclusion family phrase  
Target file: `manuscript/body.tex`

Before:

```latex
In this study, we isolated and characterized a novel phage, Hp3, which
effectively targets the aquaculture pathogen \emph{A. hydrophila}. As a
representative of a putative new family, Hp3 exhibits the rapid lytic
kinetics, broad environmental stability, and safe genomic profile
desirable for a therapeutic agent. Hp3 administration
```

After:

```latex
In this study, we isolated and characterized a novel phage, Hp3, which
effectively targets the aquaculture pathogen \emph{A. hydrophila}. As a
representative of a deeply divergent, currently unclassified
\emph{Caudoviricetes} genus, Hp3 exhibits the rapid lytic kinetics,
broad environmental stability, and safe genomic profile desirable for a
therapeutic agent. Hp3 administration
```

Verification criterion: Conclusion no longer calls Hp3 "a representative of a putative new family".

9. [NICE-TO-HAVE] Add one discussion context sentence  
Target file: `manuscript/body.tex`

Before:

```latex
In this study, we isolated and systematically characterized a novel
\emph{Aeromonas hydrophila} phage, Hp3. Beyond its therapeutic
potential, our genomic analysis shows that Hp3 represents a novel
viral lineage. Together with its closest relative, \emph{Aeromonas}
phage HJ05, it forms a distinct clade that falls outside any currently
defined phage family within the \emph{Caudoviricetes}, indicating that
aquatic ecosystems harbor phage diversity that remains poorly characterized.
Hp3 also possesses several attributes favorable for its
```

After:

```latex
In this study, we isolated and systematically characterized a novel
\emph{Aeromonas hydrophila} phage, Hp3. Beyond its therapeutic
potential, our genomic analysis shows that Hp3 represents a novel
viral lineage. Together with its closest relative, \emph{Aeromonas}
phage HJ05, it forms a distinct clade that falls outside any currently
defined phage family within the \emph{Caudoviricetes}, indicating that
aquatic ecosystems harbor phage diversity that remains poorly characterized.
This placement should be viewed in the context of the current
post-\emph{Caudovirales} taxonomy, where many \emph{Caudoviricetes}
genera remain unclassified at family rank, and of prior reports that
\emph{Aeromonas} phages can occupy divergent protein-sharing groups
\citep{2023-Abolishment_Turner,2022-Characterization_Bujak}. Hp3 also
possesses several attributes favorable for its
```

Verification criterion: Discussion cites Turner 2023 and Bujak 2022 for context without claiming a precise "600+" number.

## Residual risk

Even after these edits, a taxonomy-focused reviewer can still ask for a formal ICTV TaxoProp, a family name, or a core-gene/pangenome analysis before accepting any family-rank language. That risk is acceptable only if the manuscript consistently treats family rank as provisional.

The vConTACT3 evidence remains weak because the Hp3-HJ05-L338C connection is explicitly few-protein-driven. The revised text should keep vConTACT3 as convergent support, not as the primary basis for family rank.

The VICTOR explanation may prompt a request for a supplemental table showing the unreliable higher-rank OPTSIL partition. If that happens, provide the table as transparency, but do not use it as family-rank support.

If the title is downgraded, the taxonomy novelty becomes less marketable but more defensible. The therapeutic claim remains unaffected.
