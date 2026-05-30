# Round 2 — NotebookLM Hostile Review (AMG 解读)

**sources_used**: ['c2690ce8-7433-4403-bab7-dea98434459b', '86564eb0-9fc6-435d-9985-0ae7d662f29c', '3155957c-1b04-4591-8793-cda91c2b9a3e']

---

## NotebookLM answer (verbatim)

Here is the adversarial, virome-expert peer review focusing on the manuscript's putative Auxiliary Metabolic Genes (AMGs):

**R2-01**
*   **(a) Precise claim/line attacked:** Lines 244–247, which assert that the genome "encodes several putative auxiliary metabolic genes (AMGs)" and explicitly labels the thymidylate synthase (*thyA*) and anaerobic ribonucleotide reductase (*nrdD*) as such.
*   **(b) Why it is vulnerable:** The authors are conflating fundamental viral replication machinery with true AMGs to artificially inflate the novelty of their genomic analysis. The AMG concept was established to describe genes that supplement host energy or resource acquisition during infection (e.g., cyanophage photosynthesis genes). Nucleotide-metabolism genes like *thyA* and *nrdD* are overwhelmingly common, core replication genes for large lytic phages that simply sustain the deoxynucleotide supply [1, 2]. Slapping the "AMG" label on basic DNA replication machinery reveals a lack of rigor in phage genomics.
*   **(c) Supporting corpus citation:** Gordillo Altamirano & Barr, 2019 ("Phage Therapy in the Postantibiotic Era") [2].
*   **(d) Specific revision/qualifier required:** The reviewer demands that the authors immediately cease referring to *thyA* and *nrdD* as AMGs. They must be reclassified strictly as "nucleotide-metabolism/replication genes," and the text must be revised to reflect that their presence is a standard, expected feature of large lytic phages, not a novel metabolic intervention.

**R2-02**
*   **(a) Precise claim/line attacked:** Lines 247–249, asserting that hp3_0002 encodes "a 3-deoxy-D-arabino-heptulosonate-7-phosphate (DAHP) synthase... (Foldseek structural homology... fident = 0.38)".
*   **(b) Why it is vulnerable:** A Foldseek *fident* (fraction of identical residues) of 0.38 indicates only a ~38% structural identity. This is a weak-to-moderate structural match, not a definitive functional identification. In phage genomics, asserting an exact, highly specific enzymatic function (like "DAHP synthase, the rate-limiting enzyme of the shikimate pathway") based on a 38% match is unacceptably overconfident. This could easily be a distantly related aldolase, kinase, or a completely different synthase with a distinct substrate.
*   **(c) Supporting corpus citation:** Turner et al., 2021 ("A Roadmap for Genome-Based Phage Taxonomy") [3]. 
*   **(d) Specific revision/qualifier required:** The authors must strike the definitive functional assignment. The text must be downgraded to state that hp3_0002 is merely a "putative, distantly related structural homolog of DAHP synthase." The authors must explicitly acknowledge the high probability of functional misannotation at this low identity threshold.

**R2-03**
*   **(a) Precise claim/line attacked:** Lines 247–251, declaring hp3_0002 as a viral AMG without any methodological proof of its viral provenance.
*   **(b) Why it is vulnerable:** Modern viromics requires strict standards to call an AMG, primarily to rule out bacterial host contamination or genome assembly artifacts. The very locus tag "hp3_0002" is a massive red flag, strongly implying this gene is located at the extreme edge of the assembled contig. Contig edges are notorious for capturing fragments of host bacterial genomes. The authors present absolutely no evidence that this gene is flanked by clear viral structural genes, nor did they use dedicated, robust viromic tools (like VIBRANT or DRAM-v) to validate the contig.
*   **(c) Supporting corpus citation:** Roux et al., 2015 ("Viral dark matter and virus-host interactions resolved from publicly available microbial genomes" - referenced in the corpus taxonomy frameworks) [4].
*   **(d) Specific revision/qualifier required:** The reviewer demands a complete topological map of the hp3_0002 genomic neighborhood. What flanks this gene? Is it at the contig edge? The authors must run their genome through VIBRANT or DRAM-v and explicitly prove that this gene is of viral origin and not an *Aeromonas* host artifact mistakenly binned with the phage assembly.

**R2-04**
*   **(a) Precise claim/line attacked:** Lines 307–311 in the Discussion, elevating the DAHP synthase to a "concrete, hypothesis-driven target for future mechanistic study."
*   **(b) Why it is vulnerable:** The presence of a shikimate-pathway enzyme in a lytic *Caudoviricetes* phage is biologically unusual. Highlighting it as a "concrete target" based solely on a 38% structural identity match—with zero transcriptomic data, zero protein expression data, and zero in vitro functional validation—is a severe over-interpretation. The authors are building a massive speculative narrative on a highly tenuous bioinformatic thread.
*   **(c) Supporting corpus citation:** Abedon, 2017 ("Information phage therapy research should report") [5].
*   **(d) Specific revision/qualifier required:** The authors must drastically demote this finding. The rhetoric elevating this to a "concrete target" must be deleted entirely. It should be framed as a neutral, highly speculative genomic observation that requires absolute biochemical proof before any biological significance can be assumed.

**R2-05**
*   **(a) Precise claim/line attacked:** Lines 253–255 (framing the phage as safe for therapy because it lacks known AMR/virulence genes) juxtaposed against lines 244–251 and 307–311 (claiming the phage encodes metabolic enzymes that reprogram host pathways).
*   **(b) Why it is vulnerable:** The authors have created a glaring cognitive dissonance. They cannot claim the phage has a perfectly safe, predictable genomic profile while simultaneously boasting that it injects active metabolic enzymes (like DAHP synthase) designed to hijack and alter the host's metabolism. Phage-encoded auxiliary proteins that alter bacterial physiology represent a known "black box" regarding in vivo safety [6]. An enzyme tweaking the shikimate pathway could unpredictably alter bacterial metabolite or toxin secretion just before cell lysis, potentially causing adverse effects in the fish host.
*   **(c) Supporting corpus citation:** Gordillo Altamirano & Barr, 2019 ("Phage Therapy in the Postantibiotic Era") [6].
*   **(d) Specific revision/qualifier required:** The authors must explicitly acknowledge the tension between their biosafety claims and their AMG claims. They must add a specific disclaimer to the safety section stating that while known virulence genes are absent, the presence of uncharacterized auxiliary metabolic proteins poses unpredictable physiological effects on the bacterial host that could complicate therapeutic biosafety profiles.

**Reviewer Verdict:**
The AMG section of this manuscript is currently scientifically indefensible and requires severe qualification and partial removal. The authors have artificially inflated the novelty of their genome by mislabeling core replication machinery (*thyA*, *nrdD*) as AMGs, and they have built an overarching narrative around a highly suspect, weakly supported (38% identity) gene call (hp3_0002) without performing the basic methodological rigor required to rule out an assembly artifact. Until the authors validate the viral provenance of hp3_0002, correctly reclassify the nucleotide genes, and strip the exaggerated "concrete target" rhetoric from the Discussion, this entire section undermines the credibility of the otherwise solid *in vivo* therapeutic data.