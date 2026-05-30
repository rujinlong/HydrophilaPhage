# Rounds 2-4 Codex Evaluation

## Executive summary

Round 2 has 3 MUST-FIX items (R2-01, R2-02, R2-04), 1 REJECT-on-premise item with a NICE-TO-HAVE preemptive clause (R2-03), and 1 mostly ALREADY-ADDRESSED item needing only a small qualifier (R2-05). The real issue is not host-contamination of hp3_0002; it is overconfident AMG/DAHP wording.

Round 3 has 6 MUST-FIX items. R3-01 is resolved analytically by the already-computed survival statistics and should now be reported, not treated as a limitation. R3-02/R3-03/R3-06 should be handled as candid limitations rather than invented methods. R3-04 and R3-05 require claim-softening and mechanistic caveats.

Round 4 has 4 MUST-FIX items (R4-01, R4-04, R4-05, R4-06), 1 ALREADY-ADDRESSED-by-Round-1 taxonomy item that must remain compatible with "a new, deeply divergent Aeromonas-phage genus with validated in vivo efficacy" (R4-02), and 1 REJECT/NICE-TO-HAVE editorial preference (R4-03). The main novelty fix is to contextualize the in vivo result against prior Aeromonas phage therapy, especially AhFM11.

Reject: R2-03's contig-edge/assembly-artifact premise is false for the current manuscript: the genome is described as complete (Unicycler v0.5.1) and shown as a circular map, and the annotation table contains a single 84,750-bp contig with hp3_0002 immediately after the terminase large-subunit gene. R2-05's "metabolic hijack" contradiction is also mostly a strawman because the current manuscript no longer uses reprogram/remodel/hijack framing.

## Round 2

### R2-01 - thyA/nrdD AMG framing

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "Beyond the structural and replication modules typical of the \emph{Caudoviricetes}, the Hp3 genome encodes several putative auxiliary metabolic genes (AMGs). Two are homologs involved in nucleotide metabolism---a thymidylate synthase (hp3\_0036, \emph{thyA}) and an anaerobic ribonucleotide reductase (hp3\_0058, \emph{nrdD})---genes commonly carried by lytic phages to sustain the deoxynucleotide supply required for rapid genome replication."

Reasoning: The current wording still places thyA and nrdD inside the "AMGs" sentence. The same sentence already admits they are nucleotide-metabolism genes commonly carried by lytic phages to sustain deoxynucleotide supply, so the clean fix is to remove them from the AMG label and present them as replication/nucleotide-metabolism genes.

Recommendation: Reframe thyA/nrdD as nucleotide-metabolism/replication-support genes. Do not claim they are unusual AMGs.

### R2-02 - DAHP synthase functional assertion

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "A less common feature is hp3\_0002, encoding a 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP) synthase, the rate-limiting enzyme of the shikimate pathway (Foldseek structural homology to characterized DAHP synthases, fident = 0.38, E-value = 5 × 10\textsuperscript{-36})."

Reasoning: The manuscript states the exact enzyme and pathway role too strongly for a distant structural hit. The raw annotation also calls hp3_0002 "phospho-2-dehydro-3-deoxyheptonate aldolase" under a broad "moron, auxiliary metabolic gene and host takeover" category, which supports caution rather than certainty.

Recommendation: Replace the functional assertion with "putative, distantly related DAHP-synthase structural homolog" and explicitly state that activity and physiological role remain unvalidated.

### R2-03 - hp3_0002 contig-edge / host-contamination premise

Severity: NICE-TO-HAVE preemptive wording only  
Verdict: REJECT

Quoted manuscript text:

> "assembled using Unicycler v0.5.1 ... to obtain the complete genome sequence."

> "Whole-genome sequencing revealed that phage Hp3 possesses a double-stranded DNA genome of 84,750 bp..."

> "Circular map of the Hp3 genome."

Repository check: `analyses/data/112-phage_genome/phage_cds.tsv` contains one contig (`hp3`) of 84,750 bp. hp3_0001 is a terminase large subunit at 1-1941, hp3_0002 is at 1880-3040, and downstream ORFs are part of the same phage annotation record. hp3_0002 is ORF #2 in the complete Hp3 genome, not a fragment at an unresolved contig edge.

Reasoning: The NLM attack infers an assembly-edge problem from the locus tag "hp3_0002". That inference is invalid here. Running VIBRANT/DRAM-v is unnecessary for this targeted rebuttal, because this is not a metagenomic bin or fragmented virome contig in the manuscript.

Recommendation: Reject the demanded reanalysis. Add one short provenance clause only, stating that hp3_0002 lies within the complete circular Hp3 genome and is adjacent to phage-annotated ORFs. Also flag the R2-03 Roux 2015 citation provenance problem below.

### R2-04 - "concrete, hypothesis-driven target" rhetoric

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "Phage-encoded metabolic genes are an emerging theme in phage biology, and those identified here---particularly the less common shikimate-pathway DAHP synthase---offer concrete, hypothesis-driven targets for future mechanistic work."

Reasoning: This is overconfident given the same Results paragraph says the assignments await experimental validation. The phrase "concrete, hypothesis-driven targets" makes the DAHP-like hit sound functionally established.

Recommendation: Demote to a neutral, speculative genomic observation. Say that biochemical activity, expression, and infection-stage relevance remain unknown.

### R2-05 - safety versus metabolic hijack contradiction

Severity: NICE-TO-HAVE  
Verdict: ALREADY-ADDRESSED

Quoted manuscript text:

> "These assignments rest on sequence and structural homology and await experimental validation; the physiological role of these genes during infection remains to be determined..."

> "Finally, a safety assessment of the Hp3 genome detected no antibiotic-resistance genes and no high-confidence virulence determinants..."

Reasoning: The current manuscript does not claim host metabolic reprogramming/remodeling/hijacking. NLM's strongest premise is therefore a strawman. Still, the safety language can be slightly tightened because hp3_0002 remains uncharacterized.

Recommendation: Add one clause that the genomic safety assessment is preliminary and does not substitute for functional validation of uncharacterized proteins. No major new "safety contradiction" paragraph is warranted.

## Round 3

### R3-01 - four-group survival statistics

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "the Log-rank (Mantel-Cox) test was used to determine the statistical significance of survival differences between the bacterial group and the treatment group."

> "Statistical analysis confirmed that the survival rate in the treatment group was significantly higher than that in the bacterial group (Log-rank test, \(\chi^2\) = 20.474, df = 1, p \textless{} 0.001)."

Reasoning: The manuscript currently reports only one pairwise survival comparison. The repository script `manuscript/docs/peer-review-rounds/round_03/survival_stats.R` reconstructs n=20/group survival data and reproduces the full analysis: overall log-rank chi-square = 64.6, df = 3, p < 0.001 (p = 6.2e-14); treatment vs bacterial pairwise log-rank chi-square = 20.474, BH-adjusted p = 1.2e-5; treatment vs PBS and treatment vs phage-only not significant after BH correction (p_adj = 0.09); Cox HR = 0.091, 95% CI 0.026-0.320, p = 1.8e-4.

Recommendation: Add the full statistical method and Results text. Remove the limitation that only treated-vs-untreated was formally tested.

### R3-02 - power, randomization, blinding, ARRIVE

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "Eighty healthy largemouth bass were randomly divided into four groups of 20 each..."

> "The study was reported in accordance with the ARRIVE guidelines (Animal Research: Reporting of In Vivo Experiments) for reporting animal research."

Reasoning: The manuscript states random assignment but gives no sequence-generation/allocation method, no a priori power calculation, and no blinding statement. These omissions are real. The fix must not fabricate methods.

Recommendation: Downgrade the ARRIVE sentence to "reported with reference to ARRIVE" and move missing power/randomization/blinding details into limitations.

### R3-03 - histopathology rigor

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "The liver and spleen tissues of fish in each group were then collected..."

> "Representative histopathological images (H\&E staining)..."

Reasoning: The current manuscript does not state histology n per group, field-selection criteria, blinding, or semi-quantitative lesion scoring. The NLM demand to implement a new blinded scoring system is beyond "minimal text edits" unless the data already exist; no such scoring data were found in the repo.

Recommendation: State this as a limitation. If lab records provide histology n per group, add it later; do not invent a score.

### R3-04 - biosafety claim strength

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "intraperitoneal injection of a high dose of Hp3 resulted in 100\% survival over 7 days, demonstrating the biosafety of the phage for the host."

> "Fish treated with the phage alone showed 100\% survival with no pathology, demonstrating its safety for the host."

Reasoning: Seven-day survival and descriptive histology support "no acute mortality or overt pathology under these conditions", not broad biosafety.

Recommendation: Replace "demonstrating biosafety/safety" with a narrow acute-tolerability formulation in Abstract and Results.

### R3-05 - immunophage synergy and missing CFU mechanism

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "regrowth was observed at later time points, likely due to the emergence of phage-resistant bacteria."

> "Hp3 can reduce bacterial burden, giving the host's immune system time to clear the pathogen before resistance can become clinically relevant."

Reasoning: The manuscript already gestures toward host immunity but without a citation and without acknowledging that tissue bacterial load was not measured. The proper interpretation is immunophage synergy as a plausible explanation, not proven bacterial eradication.

Recommendation: Add a Torres-Barcelo immunophage-synergy sentence and explicitly state that tissue CFU/g was not measured.

### R3-06 - independent replication / single cohort

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "Eighty healthy largemouth bass were randomly divided into four groups of 20 each..."

Reasoning: The manuscript describes one formal 80-fish experiment and gives no independent biological replicate. The user-provided verified facts identify it as a single, unreplicated cohort.

Recommendation: State the single-cohort design as a limitation, along with tank/cohort effects and lack of independent replication.

## Round 4

### R4-01 - prior in vivo Aeromonas-phage therapy

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "The therapeutic efficacy of Hp3 was validated in a largemouth bass (\emph{Micropterus salmoides}) infection model."

> "the central result of this study is the therapeutic efficacy of Hp3 in an \emph{in vivo} model."

Reasoning: The manuscript cites general aquaculture phage therapy in the Introduction but does not cite or compare recent in vivo Aeromonas-phage therapy such as AhFM11. The verified bibliography contains `2024-Novel_MuliyaSankappa` and `2021-Phage_Ramos-Vivas`.

Recommendation: Add a Discussion comparison stating that Hp3 is consistent with and builds on established aquaculture phage therapy, rather than implying that fish rescue by Aeromonas phage is unprecedented.

### R4-02 - novelty should not hinge on putative new family

Severity: MUST-FIX via Round 1 plan  
Verdict: ALREADY-ADDRESSED

Quoted manuscript text:

> "A novel bacteriophage representing a putative new viral family rescues largemouth bass from lethal \emph{Aeromonas hydrophila} infection"

> "As a representative of a putative new family..."

Reasoning: This is real in the current source, but it was already adjudicated in `manuscript/docs/peer-review-rounds/round_01/codex_evaluation.md`. Round 4 should not create a second, inconsistent taxonomy plan.

Recommendation: Keep all Round 2-4 novelty wording compatible with the Round 1 fix: Hp3 is a new, deeply divergent Aeromonas-phage genus with validated in vivo efficacy, and any family-level language is provisional and secondary.

### R4-03 - routine characterization presented as novelty

Severity: NICE-TO-HAVE  
Verdict: REJECT

Quoted manuscript text:

> "Hp3 Has a Narrow Host Range"

> "Hp3 Has a Rapid Lytic Cycle and Is Stable Across Temperature and pH"

Reasoning: The sections are routine, but the current Results mostly report them as baseline characterization rather than claiming each assay is a breakthrough. A major condensation is not necessary for the current task.

Recommendation: No mandatory edit. The benchmark paragraph proposed for R4-04 is sufficient to prevent over-reading standard assays as novelty.

### R4-04 - missing comparators

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "The one-step growth curve revealed a latent period of approximately 45 minutes..."

> "Hp3 exhibited a narrow lytic range, successfully lysing only two bacterial strains."

Reasoning: These values are reported without context. The verified bibliography supports comparison to AhFM11 and to Aeromonas Autographiviridae examples from Bujak et al. without overgeneralizing to all Aeromonas phages.

Recommendation: Add a concise Discussion benchmark: Hp3 has a 45-min latent period and 2/19 host range; AhFM11 is a 168-kb Straboviridae phage with reported in vivo efficacy by injection, immersion, and feed; Bujak et al. show additional Aeromonas phage diversity but should not be used to imply all Aeromonas phages behave similarly.

### R4-05 - engineering platform overclaim

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "a valuable platform for engineering next-generation phage therapies."

> "a platform for investigating the molecular arms race and engineering the next generation of evolution-informed therapeutics."

> "a platform for developing next-generation phage therapies..."

Reasoning: No engineering, receptor-binding-protein modification, or synthetic-biology experiment was performed. The manuscript may say the genome can inform future work, but not that Hp3 is an engineering platform.

Recommendation: Remove "platform for engineering" rhetoric in Abstract, Discussion, and Conclusion.

### R4-06 - translational gaps

Severity: MUST-FIX  
Verdict: VERIFIED-REAL

Quoted manuscript text:

> "The treatment group received a single dose of phage Hp3 (MOI = 1.0) one hour post-infection."

> "intraperitoneally..."

> "regrowth was observed at later time points, likely due to the emergence of phage-resistant bacteria."

Reasoning: The efficacy model used intraperitoneal injection, which is useful experimentally but not a field-scalable aquaculture route. The in vitro regrowth and narrow host range also argue against monophage field use.

Recommendation: Add translational limitations: immersion/feed delivery remains untested; cocktail formulation is likely required for resistance management and host-range breadth.

## Implementation plan

1. [MUST-FIX] Replace Abstract novelty/safety/AMG/engineering wording  
Target file: `manuscript/manuscript.tex`

Before:

```latex
\emph{Aeromonas hydrophila} is a common pathogen in aquaculture where
antibiotic overuse has driven multidrug resistance. Phage therapy offers
a promising alternative. In this study, we isolated and characterized a
novel bacteriophage, vB\_AhyM\_Hp3 (hereafter referred to as Hp3).
Characterization of Hp3 revealed a potent lytic cycle with a latent
period of approximately 45 minutes and high environmental stability
across a wide range of temperatures (4--45\,\textdegree C) and pH (6.0--10.0).
Whole-genome sequencing revealed an 84.75 kb double-stranded DNA genome
with a GC content of 59\%, confirming the absence of known antimicrobial
resistance or virulence genes. Taxonomic and comparative genomic
analyses indicate that Hp3 represents a distinct viral lineage, forming
a putative new family within the class \emph{Caudoviricetes}. Genome
annotation also identified several putative auxiliary metabolic genes,
including nucleotide-metabolism homologs and a less common
shikimate-pathway enzyme, that may support efficient replication and
warrant future mechanistic study. The therapeutic efficacy of Hp3 was
validated in a largemouth bass (\emph{Micropterus salmoides}) infection
model. A single administration at a multiplicity of infection (MOI) of
1.0 rescued the fish from a lethal challenge, increasing the seven-day
survival rate from 15\% to 85\%. Fish treated with the phage alone
showed 100\% survival with no pathology, demonstrating its safety for
the host. Collectively, these findings establish phage Hp3 not only as a
promising biocontrol agent for aquaculture but also as a valuable
platform for engineering next-generation phage therapies.
```

After:

```latex
\emph{Aeromonas hydrophila} is a common pathogen in aquaculture where
antibiotic overuse has driven multidrug resistance. Phage therapy offers
a promising alternative. In this study, we isolated and characterized a
novel bacteriophage, vB\_AhyM\_Hp3 (hereafter referred to as Hp3).
Characterization of Hp3 revealed a lytic cycle with a latent period of
approximately 45 minutes and high environmental stability across a wide
range of temperatures (4--45\,\textdegree C) and pH (6.0--10.0).
Whole-genome sequencing revealed an 84.75 kb double-stranded DNA genome
with a GC content of 59\%, confirming the absence of known antimicrobial
resistance or high-confidence virulence genes. Taxonomic and comparative
genomic analyses indicate that Hp3 belongs to a deeply divergent,
currently unclassified \emph{Caudoviricetes} genus. Genome annotation
identified nucleotide-metabolism genes and a putative, distantly related
DAHP-synthase structural homolog; these annotations require experimental
validation before any physiological role during infection can be
assigned. The therapeutic efficacy of Hp3 was validated in a largemouth
bass (\emph{Micropterus salmoides}) infection model. A single
administration at a multiplicity of infection (MOI) of 1.0 rescued the
fish from a lethal challenge, increasing the seven-day survival rate from
15\% to 85\%. Fish treated with the phage alone showed 100\% survival
without overt tissue pathology, indicating no acute mortality or obvious
pathology under the tested conditions. Collectively, these findings
support Hp3 as a genetically distinctive phage candidate for aquaculture
biocontrol and provide a basis for future mechanistic and formulation
studies.
```

Verification criterion: Abstract contains no "putative auxiliary metabolic genes", "demonstrating its safety", or "platform for engineering" phrasing.

2. [MUST-FIX] Replace keywords that overclaim family rank and AMG status  
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
Phage therapy; Aquaculture; Antimicrobial resistance; Novel viral genus;
Nucleotide metabolism; Comparative genomics.
```

Verification criterion: `Novel viral family` and `Auxiliary metabolic genes` are absent from keywords.

3. [MUST-FIX] Downgrade ARRIVE/compliance wording without inventing methods  
Target file: `manuscript/body.tex`

Before:

```latex
All procedures were performed in strict
accordance with the ethical protocols approved by Northwest A\&F
University and adhered to the American Veterinary Medical Association
(AVMA) Guidelines for the Euthanasia of Animals (2020). The study was
reported in accordance with the ARRIVE guidelines (Animal Research:
Reporting of In Vivo Experiments) for reporting animal research.
```

After:

```latex
All procedures were performed in strict
accordance with the ethical protocols approved by Northwest A\&F
University and adhered to the American Veterinary Medical Association
(AVMA) Guidelines for the Euthanasia of Animals (2020). The \emph{in
vivo} study is reported with reference to the ARRIVE guidelines (Animal
Research: Reporting of In Vivo Experiments), with unresolved reporting
limitations for power calculation, allocation procedures, and blinding
described in the Discussion.
```

Verification criterion: Methods no longer claims full ARRIVE compliance without qualification.

4. [MUST-FIX] Add full survival-analysis methods  
Target file: `manuscript/body.tex`

Before:

```latex
Unless otherwise specified in the figure legends, all quantitative data
from experiments with multiple replicates are presented as the mean ±
standard deviation (SD). The Kaplan-Meier method was used to plot
survival curves, and the Log-rank (Mantel-Cox) test was used to
determine the statistical significance of survival differences between
the bacterial group and the treatment group. For bacterial growth (in
vitro lysis) assays, differences in optical density between groups at
the experimental endpoint (48 h) were analyzed using one-way analysis of
variance (ANOVA) followed by Tukey's honestly significant difference (HSD)
post-hoc test for pairwise comparisons. A p-value \textless{} 0.05 was
considered statistically significant. All statistical analyses were performed using
R software (v4.5.1).
```

After:

```latex
Unless otherwise specified in the figure legends, all quantitative data
from experiments with multiple replicates are presented as the mean ±
standard deviation (SD). The Kaplan-Meier method was used to plot
survival curves. Survival differences were first assessed using an
overall k-sample Log-rank (Mantel-Cox) test across the PBS, phage-only,
bacterial, and treatment groups. Pairwise Log-rank comparisons were then
performed with Benjamini-Hochberg adjustment for multiple testing. The
treatment effect relative to the bacterial group was additionally
estimated using a Cox proportional-hazards model with the bacterial group
as the reference. For bacterial growth (in vitro lysis) assays,
differences in optical density between groups at the experimental
endpoint (48 h) were analyzed using one-way analysis of variance (ANOVA)
followed by Tukey's honestly significant difference (HSD) post-hoc test
for pairwise comparisons. A p-value \textless{} 0.05 was considered
statistically significant. All statistical analyses were performed using
R software (v4.5.1).
```

Verification criterion: Statistical methods describe overall Log-rank, BH-adjusted pairwise tests, and Cox HR.

5. [MUST-FIX] Reframe nucleotide genes and hp3_0002 in Results  
Target file: `manuscript/body.tex`

Before:

```latex
Beyond the structural and replication modules typical of the
\emph{Caudoviricetes}, the Hp3 genome encodes several putative auxiliary
metabolic genes (AMGs). Two are homologs involved in nucleotide
metabolism---a thymidylate synthase (hp3\_0036, \emph{thyA}) and an
anaerobic ribonucleotide reductase (hp3\_0058, \emph{nrdD})---genes
commonly carried by lytic phages to sustain the deoxynucleotide supply
required for rapid genome replication. A less common feature is
hp3\_0002, encoding a 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP)
synthase, the rate-limiting enzyme of the shikimate pathway (Foldseek
structural homology to characterized DAHP synthases, fident = 0.38,
E-value = 5 × 10\textsuperscript{-36}). These assignments rest on
sequence and structural homology and await experimental validation; the
physiological role of these genes during infection remains to be
determined and represents a target for future mechanistic study.
```

After:

```latex
Beyond the structural modules typical of the \emph{Caudoviricetes}, the
Hp3 genome carries nucleotide-metabolism genes that may support phage
DNA replication, including a thymidylate synthase (hp3\_0036,
\emph{thyA}) and an anaerobic ribonucleotide reductase (hp3\_0058,
\emph{nrdD}). These genes are common replication-associated features of
lytic phages rather than evidence for broad host-metabolism remodeling.
A less common annotation is hp3\_0002, a putative, distantly related
DAHP-synthase structural homolog (annotated as
phospho-2-dehydro-3-deoxyheptonate aldolase; Foldseek structural
homology to characterized DAHP synthases, fident = 0.38, E-value = 5 ×
10\textsuperscript{-36}). hp3\_0002 lies within the complete circular
Hp3 genome, adjacent to the terminase large-subunit gene and followed by
additional phage-annotated ORFs, rather than at an unresolved contig
edge. These assignments rest on sequence and structural homology and
await experimental validation; the enzymatic activity, substrate
specificity, and physiological role of hp3\_0002 during infection remain
unknown.
```

Verification criterion: thyA/nrdD are no longer called AMGs, hp3_0002 is "putative, distantly related", and the complete-circular-genome provenance clause is present.

6. [NICE-TO-HAVE] Add a one-clause safety qualifier for uncharacterized proteins  
Target file: `manuscript/body.tex`

Before:

```latex
Finally, a safety assessment of the Hp3 genome detected no
antibiotic-resistance genes and no high-confidence virulence
determinants---the sole virulence-database match was a weak,
low-identity hit unlikely to reflect a functional virulence
factor---supporting its suitability for therapeutic applications.
```

After:

```latex
Finally, a genomic safety screen detected no antibiotic-resistance genes
and no high-confidence virulence determinants---the sole
virulence-database match was a weak, low-identity hit unlikely to
reflect a functional virulence factor---supporting Hp3 as a candidate
for therapeutic evaluation while leaving uncharacterized proteins,
including hp3\_0002, for future functional validation.
```

Verification criterion: safety language is genomic/preliminary and acknowledges uncharacterized proteins.

7. [MUST-FIX] Replace survival Results with full analysis and softened acute-safety claim  
Target file: `manuscript/body.tex`

Before:

```latex
The in vivo experimental design is illustrated in
Figure~\ref{fig-therapy} A, and the resulting survival curves for each
group are shown in Figure~\ref{fig-therapy} B. In the phage-only group,
intraperitoneal injection of a high dose of Hp3 resulted in 100\%
survival over 7 days, demonstrating the biosafety of the phage for the
host. In contrast, the group infected with \emph{A. hydrophila} began to
exhibit mortality within 24 hours post-infection, and by day three, the
survival rate had dropped to 15\%, where it remained for the rest of the
experiment. In the treatment group, however, administration of Hp3 one
hour after infection resulted in a final survival rate of 85\%.
Statistical analysis confirmed that the survival rate in the treatment
group was significantly higher than that in the bacterial group
(Log-rank test, \(\chi^2\) = 20.474, df = 1, p \textless{} 0.001).
```

After:

```latex
The in vivo experimental design is illustrated in
Figure~\ref{fig-therapy} A, and the resulting survival curves for each
group are shown in Figure~\ref{fig-therapy} B. In the phage-only group,
intraperitoneal injection of a high dose of Hp3 resulted in 100\%
survival over 7 days, indicating no acute mortality under these dosing
and timeframe conditions. In contrast, the group infected with
\emph{A. hydrophila} began to exhibit mortality within 24 hours
post-infection, and by day three, the survival rate had dropped to
15\%, where it remained for the rest of the experiment. In the treatment
group, however, administration of Hp3 one hour after infection resulted
in a final survival rate of 85\%. Survival differed strongly across the
four groups (overall Log-rank test, \(\chi^2\) = 64.6, df = 3,
p \textless{} 0.001; exact \(p = 6.2 \times 10^{-14}\)). In
Benjamini-Hochberg-adjusted pairwise comparisons, treatment significantly
improved survival relative to the bacterial group (Log-rank test,
\(\chi^2\) = 20.474, \(p_{\mathrm{adj}}\) = 1.2 ×
10\textsuperscript{-5}), whereas treatment did not differ significantly
from the PBS or phage-only controls (both \(p_{\mathrm{adj}}\) = 0.09);
the PBS and phage-only curves were identical. A Cox proportional-hazards
model using the bacterial group as the reference estimated a strong
reduction in mortality hazard for treated fish (HR = 0.091, 95\% CI =
0.026--0.320, \(p = 1.8 \times 10^{-4}\)).
```

Verification criterion: Results report overall Log-rank, BH-adjusted pairwise tests, and Cox HR with the supplied values.

8. [MUST-FIX] Update the survival statistic in the Figure 5 caption  
Target file: `manuscript/body.tex`

Before:

```latex
Survival rates were significantly different between the bacterial group
and the treatment group (Log-rank test, \(\chi^2\) = 20.474, df = 1, p
\textless{} 0.001).
```

After:

```latex
Survival differed across groups (overall Log-rank test, \(\chi^2\) =
64.6, df = 3, p \textless{} 0.001), and treatment improved survival
relative to the bacterial group after Benjamini-Hochberg correction
(pairwise Log-rank test, \(\chi^2\) = 20.474,
\(p_{\mathrm{adj}}\) = 1.2 × 10\textsuperscript{-5}).
```

Verification criterion: Figure 5 caption no longer reports only the single unadjusted pairwise test.

9. [MUST-FIX] Reframe the opening Discussion around genus-level novelty and preliminary safety  
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
development as an antibiotic alternative in aquaculture. These
include a short lytic cycle, stability across the temperature and pH
ranges typical of aquaculture, and a genomic profile that confirms the
absence of known genes associated with antibiotic resistance or
virulence factors, providing a preliminary basis for its biosafety.
```

After:

```latex
In this study, we isolated and systematically characterized a lytic
\emph{Aeromonas hydrophila} phage, Hp3. Beyond its therapeutic
potential, our genomic analysis supports the placement of Hp3 and its
closest relative, \emph{Aeromonas} phage HJ05, in a deeply divergent,
currently unclassified \emph{Aeromonas}-phage genus within the
\emph{Caudoviricetes}. Hp3 also possesses several attributes favorable
for further evaluation as an antibiotic alternative in aquaculture,
including a lytic cycle of approximately 90 minutes, stability across
temperature and pH ranges relevant to aquaculture, and a genomic profile
with no known antimicrobial-resistance genes or high-confidence
virulence determinants, providing a preliminary genomic safety basis for
therapeutic assessment.
```

Verification criterion: Discussion opening emphasizes deeply divergent genus-level novelty, not family-rank novelty.

10. [MUST-FIX] Replace resistance/engineering paragraphs with immunophage synergy, cocktail, and route limitations  
Target file: `manuscript/body.tex`

Before:

```latex
However, the long-term efficacy of any phage therapy is fundamentally
dictated by the co-evolutionary ``arms race'' between the phage and its
bacterial host \citep{2023-Developing_Oromi-Bosch}. Two of our
observations reflect this pressure. First, the
narrow host range of Hp3 reflects the highly specific interaction
between phage receptor-binding proteins and specific bacterial surface
molecules, which are the very structures bacteria constantly modify to
evade predation. Second, the regrowth of the bacterial population
observed in our in vitro lysis assays serves as direct evidence for the
rapid emergence of resistant variants under phage selection pressure.
Hp3 should therefore not be treated as a static antimicrobial agent;
any application strategy must account for the
evolutionary plasticity of the target bacteria.

Two strategies can help counter bacterial resistance: phage cocktails
and phage engineering. The first
approach is to mimic natural diversity by formulating phage cocktails.
Combining multiple phages that recognize different cellular receptors or
employ distinct lytic mechanisms can significantly decrease the
probability of simultaneous resistance emerging, thereby imposing a
greater evolutionary hurdle on the pathogen \citep{2021-Phage_Abedon}.
With its well-defined biological properties, Hp3 serves as a reliable
foundational component for such multi-phage formulations. A second, more
proactive strategy involves leveraging phage engineering
\citep{2021-Reprogramming_Dunne}. Advances in structural biology and
protein engineering offer a pathway to rationally modify the
receptor-binding proteins of Hp3, potentially expanding its host range
or enabling it to recognize newly evolved bacterial receptors, thereby
directly countering the host's evolutionary trajectory.
```

After:

```latex
However, the long-term efficacy of any phage therapy is fundamentally
dictated by the co-evolutionary ``arms race'' between the phage and its
bacterial host \citep{2023-Developing_Oromi-Bosch}. Two of our
observations reflect this pressure. First, the narrow host range of Hp3
reflects the highly specific interaction between phage receptor-binding
proteins and bacterial surface molecules, which are the very structures
bacteria can modify to evade predation. Second, the regrowth of the
bacterial population observed in our in vitro lysis assays is consistent
with the rapid emergence of resistant variants under phage selection
pressure. The durable in vivo rescue despite this in vitro regrowth may
reflect immunophage synergy, in which phage-mediated reduction of
pathogen density allows host immunity to clear residual bacteria before
resistance becomes clinically dominant \citep{2018-Phage_Torres-Barcelo}.
Because tissue bacterial loads were not quantified as CFU/g, bacterial
clearance remains an inferred mechanism rather than a directly measured
endpoint in this study.

Hp3 should therefore not be treated as a static monophage antimicrobial
agent. Combining phages that recognize different receptors or use
distinct infection mechanisms can reduce the probability of simultaneous
resistance and improve host-range breadth \citep{2021-Phage_Abedon,
2023-Developing_Oromi-Bosch}. Hp3 may contribute to such future
multi-phage formulations, but cocktail compatibility, resistance
management, and scalable delivery remain to be tested. The present
efficacy experiment used intraperitoneal injection; field deployment in
aquaculture will require evaluation by practical delivery routes such as
immersion or feed administration \citep{2021-Phage_Ramos-Vivas}.
```

Verification criterion: Discussion contains immunophage synergy, CFU limitation, cocktail need, and delivery-route limitation; engineering-platform rhetoric is removed from this paragraph.

11. [MUST-FIX] Demote DAHP mechanistic interpretation in Discussion  
Target file: `manuscript/body.tex`

Before:

```latex
A deeper layer of the arms race unfolds intracellularly, where bacteria
deploy defense systems such as restriction-modification and CRISPR-Cas
to neutralize invading genomes \citep{2010-Bacteriophage_Labrie},
against which phages have evolved diverse anti-defense systems
\citep{2024-Growing_Murtazalieva}. Our in silico screen did not detect
any known anti-defense genes in the Hp3 genome, and the HJ05-absent 5'
gene block consists largely of hypothetical proteins whose functions
remain undetermined; whether any of these contribute to host takeover or
counter-defense is an open question that will require direct functional
testing. A more tractable avenue is offered by the putative AMGs
described above. Phage-encoded metabolic genes are an emerging theme in
phage biology, and those identified here---particularly the less common
shikimate-pathway DAHP synthase---offer concrete, hypothesis-driven
targets for future mechanistic work.
```

After:

```latex
A deeper layer of the arms race unfolds intracellularly, where bacteria
deploy defense systems such as restriction-modification and CRISPR-Cas
to neutralize invading genomes \citep{2010-Bacteriophage_Labrie},
against which phages have evolved diverse anti-defense systems
\citep{2024-Growing_Murtazalieva}. Our in silico screen did not detect
any known anti-defense genes in the Hp3 genome, and the HJ05-absent 5'
gene block consists largely of hypothetical proteins whose functions
remain undetermined; whether any of these contribute to counter-defense
is an open question that will require direct functional testing. The
nucleotide-metabolism genes identified in Hp3 are consistent with
replication support in lytic phages. By contrast, the hp3\_0002
DAHP-synthase-like hit is a more unusual but still speculative genomic
observation: given the distant structural homology and the absence of
transcriptomic, biochemical, or infection-stage functional data, it
should not yet be interpreted as evidence for shikimate-pathway
modulation during infection.
```

Verification criterion: "concrete, hypothesis-driven targets" is absent and hp3_0002 is explicitly speculative.

12. [MUST-FIX] Replace in vivo interpretation/limitations with prior-art context, benchmark, and updated limitations  
Target file: `manuscript/body.tex`

Before:

```latex
Despite these long-term evolutionary considerations, the central
result of this study is the therapeutic efficacy of Hp3 in an
\emph{in vivo} model. A single administration of the phage significantly
improved the survival of largemouth bass following a lethal challenge
and effectively mitigated tissue pathology. This indicates that
during the acute phase of an infection, Hp3 can reduce bacterial burden,
giving the host's immune system time to clear the pathogen before
resistance can become clinically relevant. Several limitations temper this
\emph{in vivo} result: the survival benefit was formally tested only for the
treated versus untreated infected groups (Log-rank test), whereas the other
group comparisons, the apparent safety of phage-only administration, and the
histopathological differences were assessed descriptively rather than by
powered statistical tests; and \emph{in vitro} suppression was compared at a
single 48-h endpoint.
```

After:

```latex
Despite these long-term evolutionary considerations, Hp3 showed clear
therapeutic activity in the largemouth bass infection model. A single
administration of the phage significantly improved survival after lethal
\emph{A. hydrophila} challenge and was accompanied by milder liver and
spleen pathology. This result is consistent with, and builds on, an
established aquaculture phage-therapy paradigm rather than representing
an unprecedented proof of principle. For example, phage AhFM11, a
168-kb \emph{Straboviridae} phage active against hypervirulent
\emph{A. hydrophila}, achieved high protection in fish by injection,
immersion, and oral-feed delivery routes \citep{2024-Novel_MuliyaSankappa};
aquaculture phage therapy more broadly has also been reviewed as a
focused disease-management strategy \citep{2021-Phage_Ramos-Vivas}.
Hp3 differs from this benchmark by representing a deeply divergent
\emph{Aeromonas}-phage genus, but its approximately 45-minute latent
period and narrow host range (2 of 19 tested strains) should be viewed
as baseline biological properties rather than evidence of superior
biocontrol breadth \citep{2022-Characterization_Bujak,
2024-Novel_MuliyaSankappa}.

Although the full four-group survival design was statistically analysed,
several limitations temper the \emph{in vivo} interpretation. No
a priori power calculation was performed, and the randomization sequence,
allocation concealment, survival-monitoring blinding, and histopathology
assessment blinding were not formally documented. The animal challenge
was a single, unreplicated cohort, leaving possible cohort or tank effects
unresolved. Histopathology was descriptive and based on representative
images rather than blinded semi-quantitative lesion scoring, and tissue
bacterial loads were not measured. Finally, treatment was evaluated only
as a single intraperitoneal phage dose one hour after bacterial challenge,
while \emph{in vitro} suppression was compared at a single 48-h endpoint.
```

Verification criterion: Discussion cites AhFM11 and Ramos-Vivas, removes the obsolete "only treated-vs-untreated was formally tested" limitation, and adds the remaining design limitations.

13. [MUST-FIX] Replace final Discussion paragraph to remove platform/engineering overclaim  
Target file: `manuscript/body.tex`

Before:

```latex
The characterization of Hp3 yields more than a biocontrol candidate. Its
therapeutic potential is best understood within the dynamic framework of
phage-bacterium co-evolution. Hp3 is both an immediate candidate against
\emph{A. hydrophila} and a platform for investigating the molecular arms
race and engineering the next generation of evolution-informed
therapeutics.
```

After:

```latex
The characterization of Hp3 therefore yields a genetically distinctive
candidate rather than a finished field-ready product. Its complete
genome, divergent genus-level placement, lytic activity, and in vivo
rescue support further development, while resistance, host-range breadth,
delivery route, and mechanism-of-clearance questions define the next
experimental priorities.
```

Verification criterion: final Discussion contains no "platform", "engineering", or "next generation" claim.

14. [MUST-FIX] Replace Conclusion to use defensible novelty and translational limits  
Target file: `manuscript/body.tex`

Before:

```latex
In this study, we isolated and characterized a novel phage, Hp3, which
effectively targets the aquaculture pathogen \emph{A. hydrophila}. As a
representative of a putative new family, Hp3 exhibits the rapid lytic
kinetics, broad environmental stability, and safe genomic profile
desirable for a therapeutic agent. Hp3 administration
increased the survival rate from 15\% to 85\% in a largemouth bass
infection model, demonstrating protective efficacy. These findings
position phage Hp3 as both a promising antimicrobial agent and a
platform for developing next-generation
phage therapies against \emph{A. hydrophila}.
```

After:

```latex
In this study, we isolated and characterized Hp3, a lytic phage targeting
the aquaculture pathogen \emph{A. hydrophila}. Genomic analyses support
its placement in a deeply divergent \emph{Aeromonas}-phage genus within
the \emph{Caudoviricetes}, with no known antimicrobial-resistance genes
or high-confidence virulence determinants. Hp3 administration increased
the survival rate from 15\% to 85\% in a largemouth bass infection
model, demonstrating protective efficacy under the tested experimental
conditions. These findings position Hp3 as a promising but early-stage
antimicrobial candidate; future work should validate scalable delivery
routes, cocktail formulation, resistance management, and mechanisms of
in vivo bacterial clearance.
```

Verification criterion: Conclusion contains no "putative new family" or "platform for developing next-generation phage therapies" language.

## NLM hallucination flags

R2-03 Roux 2015: Flag as unsupported by the saved NLM corpus metadata. The R2 review lists only opaque source IDs and provides no source mapping showing Roux et al. 2015 in the Round 2 corpus. A Zotero export entry `2015-Viral_Roux` exists in `manuscript/bibliography.bib`, but that does not validate NLM's claim that the cited paper was in its active corpus or that it supports a contig-edge critique of a complete isolate genome.

R2-04 Abedon 2017: Flag as likely hallucinated or at least mis-cited for this manuscript. I found `2021-Phage_Abedon` in the bibliography and manuscript, but no `Abedon 2017` / "Information phage therapy research should report" citekey or reference in the manuscript bibliography, bbl, aux, or review reports. Do not cite the R2-04 Abedon 2017 reference.

Round 3 citations: The Round 3 NLM file has `sources_used: []`, so the Torres-Barcelo quotation provenance cannot be accepted as an NLM-corpus quote. However, the verified citekey `2018-Phage_Torres-Barcelo` exists and is appropriate for the immunophage-synergy/resistance-evolution sentence.

Round 4 citations: The Round 4 NLM file also has `sources_used: []`. The requested citekeys `2024-Novel_MuliyaSankappa`, `2022-Characterization_Bujak`, and `2021-Phage_Ramos-Vivas` exist in the bibliography and may be cited, but the NLM provenance itself is blank.

Other citation caution: R2-02 cites Turner 2021 for a Foldseek/functional-annotation-confidence point. Turner 2021 is relevant to phage taxonomy standards, not directly to DAHP enzyme-function validation; the DAHP downgrade is justified by the manuscript's own low-identity structural-homology basis, not by Turner 2021.

## Residual risk

The proposed text fixes do not create new data. Reviewers can still object to the absence of a priori power calculation, formally documented randomization/allocation/blinding, blinded histopathology scoring, tissue CFU/g, independent animal replication, and scalable delivery-route testing.

The complete circular genome point is strong enough to reject the contig-edge premise, but if a reviewer asks for primary assembly evidence, the authors should be ready to provide the Unicycler circularity/assembly record or update deposited GenBank topology metadata accordingly.

The exact diffs above assume Round 1 taxonomy de-emphasis is applied in the same revision pass. If Round 1 edits change the same abstract/title/conclusion wording first, apply the scientific intent of these Round 2-4 edits rather than duplicating conflicting text.
