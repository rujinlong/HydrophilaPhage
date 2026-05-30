# De-AI Scan — `body.tex` (Hp3 vs *A. hydrophila*, largemouth bass phage therapy)

**Mode:** DOCUMENT / SCAN — REPORT ONLY, no edits applied.
**Scope guard:** Results numbers, statistics, citations, and the AMG/taxonomy wording were treated as load-bearing and left untouched. Suggestions below target prose style only.

Flags are ordered by section. Each entry: location → quote → why it reads as AI → tighter rewrite.

---

## A. Formulaic connectives / signposting openers

### A1. Discussion — "Furthermore" paragraph opener
- **Quote:** "Furthermore, Hp3 possesses several attributes favorable for its development as an alternative to antibiotics..."
- **Why AI:** "Furthermore" as a paragraph-level discourse glue after an already-additive sentence is a classic LLM connective; the logical link (still listing favorable attributes) does not need an explicit signpost.
- **Rewrite:** "Hp3 also possesses several attributes favorable for its development as an antibiotic alternative in aquaculture." (or drop the connective entirely and start "Hp3 possesses…")

### A2. Results (lysis curve) — "Notably,"
- **Quote:** "Notably, Hp3 exhibited the most effective and sustained bacterial suppression at an MOI of 1.0 and 10."
- **Why AI:** "Notably" is a top-tier AI emphasis opener flagging significance the data already convey.
- **Rewrite:** "Hp3 produced the strongest and most sustained suppression at MOI 1.0 and 10."

### A3. Results (histopathology) — "Taken together, these results indicate"
- **Quote:** "Taken together, these results indicate that Hp3 not only improves survival... but also significantly reduces liver and spleen damage in vivo."
- **Why AI:** "Taken together, these results indicate" is a templated Results-summary scaffold; combined here with a "not only… but also" frame (see C1).
- **Rewrite:** "These histopathological findings parallel the survival data: Hp3 improved survival and reduced liver and spleen damage in vivo." (note: keep "significantly" only if it maps to a statistical test; here it describes histology, so prefer "markedly" or drop — see B-block.)

### A4. Discussion — "Therefore," (judgement opener)
- **Quote:** "Therefore, viewing Hp3 as a static antimicrobial agent would be short-sighted."
- **Why AI:** "Therefore," + an evaluative aphorism ("would be short-sighted") is LLM editorializing; the prior two sentences already make the point.
- **Rewrite:** "Hp3 should therefore not be treated as a static antimicrobial agent; any application strategy must account for the evolutionary plasticity of the target bacteria." (merges with the trailing sentence, removes the standalone flourish)

### A5. Conclusion — "Collectively, our findings establish"
- **Quote:** "Collectively, our findings establish phage Hp3 not only as a promising antimicrobial agent but also as a valuable platform..."
- **Why AI:** "Collectively, our findings establish" is a signature closing scaffold; pairs with "not only… but also" (C-block) and the inflated verb "establish" (D-block).
- **Rewrite:** "These findings position phage Hp3 as both a promising antimicrobial agent and a platform for developing next-generation phage therapies against *A. hydrophila*." ("position … as both … and" replaces the triple AI stack).

### A6. Discussion — "In conclusion," mid-Discussion paragraph
- **Quote:** "In conclusion, our characterization of phage Hp3 provides more than just a promising candidate for biocontrol."
- **Why AI:** A second "In conclusion" inside the Discussion (the manuscript already has a separate Conclusion section) is redundant signposting; "provides more than just" is salesy framing.
- **Rewrite:** "The characterization of Hp3 yields more than a biocontrol candidate." (or fold this paragraph's content into the dedicated Conclusion to avoid a duplicate wrap-up.)

---

## B. Empty intensifiers / non-statistical "significant" / hype adjectives

### B1. Results (stability) — "robust stability"
- **Quote:** "Similarly, Hp3 exhibited robust stability across a wide pH range."
- **Why AI:** "robust" is a flagged empty intensifier; "Similarly," adds a mechanical transition.
- **Rewrite:** "Hp3 was also stable across a wide pH range." (Note: the parallel temperature sentence "Hp3 demonstrated high thermal stability" is acceptable but "demonstrated" → "showed" tightens it.)

### B2. Discussion — "robust tolerance to environmental stressors"
- **Quote:** "...a short lytic cycle, robust tolerance to environmental stressors such as temperature and pH..."
- **Why AI:** "robust tolerance" is an empty-intensifier + abstraction combo; "environmental stressors such as temperature and pH" is noun-heavy padding for "temperature and pH."
- **Rewrite:** "...a short lytic cycle, stability across the temperature and pH ranges typical of aquaculture..."

### B3. Discussion — "the most critical finding of this study"
- **Quote:** "Despite these long-term evolutionary considerations, the most critical finding of this study is the clear therapeutic efficacy of Hp3..."
- **Why AI:** "most critical finding" is vague significance inflation; ranking findings by importance is an LLM tic.
- **Rewrite:** "The central result of this study is the therapeutic efficacy of Hp3 in vivo." (drop "clear"; the survival statistic carries it.)

### B4. Discussion — "decisive therapeutic advantage" / "winning a critical window"
- **Quote:** "...Hp3 can provide a decisive therapeutic advantage, winning a critical window of time for the host's immune system to clear the pathogen..."
- **Why AI:** "decisive… advantage" + "winning a critical window" stacks two motivational metaphors; "critical" is an empty intensifier.
- **Rewrite:** "...Hp3 can reduce bacterial burden during the acute phase, giving the host's immune system time to clear the pathogen before resistance becomes clinically relevant."

### B5. Conclusion — "potent protective efficacy"
- **Quote:** "We demonstrated its potent protective efficacy in a largemouth bass infection model..."
- **Why AI:** "potent … efficacy" is adjective inflation; the 15%→85% number that follows is the actual evidence.
- **Rewrite:** "Hp3 administration increased survival from 15% to 85% in a largemouth bass infection model, demonstrating protective efficacy." (also resolves the redundant "demonstrated… efficacy… demonstrated" feel).

### B6. Results (lysis) — "potent lytic capability… potential for therapeutic use"
- **Quote:** "Nevertheless, these results confirm the potent lytic capability of phage Hp3 and its potential for therapeutic use."
- **Why AI:** Generic Results-paragraph flourish ("confirm the potent … and its potential for…"); "Nevertheless" patches the regrowth caveat in a templated way; "confirm" overstates (see D-block).
- **Rewrite:** "Despite this regrowth, Hp3 suppressed *A. hydrophila* across MOIs, supporting its lytic activity against the strain." (move therapeutic-potential claims to the Discussion where they are argued.)

### B7. Section heading — "Hp3 Exhibits Potent Lytic Activity"
- **Quote:** "Hp3 Exhibits Potent Lytic Activity and a Narrow Host Range"
- **Why AI:** "Potent" in a results heading is editorializing; note the result is actually a *narrow* range (lyses 2/19), so "potent" is also in mild tension with the data.
- **Rewrite:** "Hp3 has a narrow host range." (or "Hp3 lyses two of nineteen *A. hydrophila* strains.")

### B8. Heading — "Broad Environmental Stability"
- **Quote:** "Hp3 Possesses a Rapid Lytic Cycle and Broad Environmental Stability"
- **Why AI:** "Broad … Stability" mirrors the AI heading cadence (adjective + abstraction). Acceptable but tightenable.
- **Rewrite:** "Rapid lytic cycle and stability across temperature and pH." (lower-case sentence style if the journal allows.)

### B9. Methods — "comprehensively validate" / "comprehensive evaluation"
- **Quote (Intro/Methods framing):** "comprehensively validate a novel phage"; "A comprehensive evaluation of a phage's lytic efficiency, stability, genomic safety..."
- **Why AI:** "comprehensive/comprehensively" is a flagged empty intensifier; appears 2x plus in the Fig.4 caption ("Comprehensive genomic… analyses").
- **Rewrite:** Intro: "...to identify and characterize a novel phage against *A. hydrophila*." Methods sentence: "Evaluating lytic efficiency, stability, genomic safety, and efficacy in a relevant model is required." (Caption: "Genomic, taxonomic, and comparative analyses of phage Hp3.")

---

## C. "not only … but also" / rule-of-three padding / paired-contrast templates

### C1. Results (histopathology) — "not only… but also" (mechanical)
- **Quote:** "...Hp3 not only improves survival after infection... but also significantly reduces liver and spleen damage in vivo."
- **Why AI:** Mechanical "not only X but also Y" frame; both clauses are simple coordinate facts.
- **Rewrite:** "...Hp3 both improved survival and reduced liver and spleen damage in vivo." (see also A3.)

### C2. Conclusion — "not only… but also" (again)
- **Quote:** "...establish phage Hp3 not only as a promising antimicrobial agent but also as a valuable platform..."
- **Why AI:** Second mechanical "not only… but also" in the closing matter; reads as a template reused across sections.
- **Rewrite:** see A5 ("as both … and …").

### C3. Discussion — "not just / dual value" closing
- **Quote:** "...provides more than just a promising candidate for biocontrol... which reveals its dual value. Hp3 serves as both an effective agent... and, perhaps more significantly, as a platform..."
- **Why AI:** "more than just," "dual value," "serves as both… and… perhaps more significantly" is a dense cluster of paired-contrast flourishes and vague significance ("perhaps more significantly").
- **Rewrite:** "Hp3 is both an immediate candidate against *A. hydrophila* and a platform for studying phage–host co-evolution and engineering evolution-informed therapeutics." (remove "perhaps more significantly"; let the two roles stand equally.)

### C4. Intro — rule-of-three "lytic efficiency, stability, genomic safety, and, most critically, its efficacy"
- **Quote:** "A comprehensive evaluation of a phage's lytic efficiency, stability, genomic safety, and, most critically, its efficacy in a relevant clinical model is required..."
- **Why AI:** List padding with an inserted ranking flourish ("and, most critically,"); the "most critically" pre-judges importance.
- **Rewrite:** "Lytic efficiency, stability, genomic safety, and efficacy in a relevant model must all be assessed..." (drop "most critically".)

### C5. Discussion — "manifested in two key findings" rule-of-two scaffold
- **Quote:** "This evolutionary pressure is manifested in two key findings of our study. First,... Second,..."
- **Why AI:** "manifested in two key findings" + "First/Second" is an enumerated topic-sentence scaffold; "key" is an empty intensifier (D-block).
- **Rewrite:** "Two of our observations reflect this pressure. The narrow host range of Hp3 follows from the specific interaction between receptor-binding proteins and bacterial surface molecules — structures bacteria continually modify to evade predation — and the bacterial regrowth in our in vitro lysis assays signals the rapid emergence of resistant variants under phage selection." (or keep First/Second but drop "two key findings of our study".) **Punctuation note:** this rewrite uses an em dash for illustration only; in the actual edit replace with commas or a sentence split per house style.

---

## D. Inflated result verbs (verb stronger than evidence)

### D1. "underscores the vast, unexplored phage diversity"
- **Quote:** "...a finding that underscores the vast, unexplored phage diversity in aquatic ecosystems."
- **Why AI:** "underscores" + "vast, unexplored" is an AI emphasis verb plus an absolutist gap claim from a single-isolate study.
- **Rewrite:** "...indicating that aquatic ecosystems harbor phage diversity that remains poorly characterized." (downgrade "underscores"→"indicating"; "vast, unexplored"→"poorly characterized".)

### D2. "underscoring the isolation of this genus"
- **Quote:** "...the Mash distance to every other *Aeromonas* phage was 1.0 (no shared k-mers), underscoring the isolation of this genus."
- **Why AI:** "underscoring" again as an emphasis verb. (The numbers here are load-bearing and must stay.)
- **Rewrite:** "...was 1.0 (no shared k-mers), consistent with the isolation of this genus." (verb-only change; numbers untouched.)

### D3. "confirm" (lysis Results)
- **Quote:** "these results confirm the potent lytic capability"
- **Why AI:** "confirm" overstates an in vitro OD assay with observed regrowth.
- **Rewrite:** "support" / "demonstrate" — see B6.

### D4. "establish" (Conclusion)
- **Quote:** "our findings establish phage Hp3 not only as..."
- **Why AI:** "establish" is an inflated claim verb for a single-phage, single-model proof-of-concept.
- **Rewrite:** "position" / "identify" — see A5.

### D5. "demonstrates that… decisive therapeutic advantage"
- **Quote:** "This demonstrates that during the acute phase of an infection, Hp3 can provide a decisive therapeutic advantage..."
- **Why AI:** "demonstrates that" before a speculative mechanistic narrative (immune-window argument) overshoots; the survival data show efficacy, not the immune-clearance mechanism.
- **Rewrite:** "This indicates that, during acute infection, Hp3 can reduce bacterial burden enough to..." (keep mechanism as interpretation, not demonstrated fact.)

---

## E. Vague significance / over-smooth topic sentences / motivational framing

### E1. Intro — "now a failing strategy"
- **Quote:** "The industry's reliance on traditional antibiotics to control these infections is now a failing strategy."
- **Why AI:** Punchy editorial topic sentence ("now a failing strategy") with rhetorical finality; reads as op-ed, not literature-grounded.
- **Rewrite:** "Conventional antibiotic control of these infections is increasingly ineffective." (let the following sentence supply the resistance/contamination evidence.)

### E2. Intro — "This dual crisis… creates an urgent need"
- **Quote:** "This dual crisis of antimicrobial resistance and ecological damage creates an urgent need for effective and sustainable alternatives."
- **Why AI:** "dual crisis," "urgent need," "effective and sustainable alternatives" is stacked motivational framing with a rule-of-two ("effective and sustainable").
- **Rewrite:** "Together, resistance and environmental contamination motivate the search for alternatives to antibiotics." (drop "dual crisis/urgent/effective and sustainable".)

### E3. Intro — "Bacteriophage therapy has emerged as a leading candidate"
- **Quote:** "Bacteriophage therapy has emerged as a leading candidate to meet this need."
- **Why AI:** "has emerged as a leading candidate to meet this need" is a generic, over-smooth field-status sentence.
- **Rewrite:** "Bacteriophage therapy is one alternative under active investigation." (or state what makes it suited, then cite.)

### E4. Intro — "This precision and safety profile make them a powerful tool"
- **Quote:** "This precision and safety profile make them a powerful tool to combat bacterial pathogens in sensitive ecosystems like aquaculture."
- **Why AI:** "powerful tool to combat" is motivational; over-smooth summarizing topic sentence.
- **Rewrite:** "These properties make phages well suited to controlling pathogens in sensitive ecosystems such as aquaculture."

### E5. Intro — "The path from environmental isolate… is demanding, fraught with challenges"
- **Quote:** "The path from environmental isolate to viable therapeutic agent is demanding, fraught with challenges such as environmental instability and the complex co-evolutionary dynamics..."
- **Why AI:** "The path from X to Y is demanding, fraught with challenges such as…" is a textbook LLM transition sentence with a rule-of-two challenge list.
- **Rewrite:** "Developing an environmental isolate into a therapeutic agent is difficult, because phages may be environmentally unstable and because phage–bacterium co-evolution erodes efficacy." (replace "fraught with challenges"; keep the two specific obstacles as causes.)

### E6. Intro — "culminating in a successful demonstration"
- **Quote:** "...culminating in a successful demonstration of its therapeutic efficacy in a lethal largemouth bass infection model."
- **Why AI:** "culminating in a successful demonstration" is a narrative flourish; "successful" pre-judges the result in the Introduction.
- **Rewrite:** "...and its therapeutic efficacy in a lethal largemouth bass infection model." (drop "culminating in a successful demonstration".)

### E7. Discussion — over-smooth transition "This fundamental challenge points toward two complementary strategies widely considered in the field"
- **Quote:** "This fundamental challenge points toward two complementary strategies widely considered in the field to outpace bacterial defenses."
- **Why AI:** "This fundamental challenge points toward two complementary strategies" is an over-engineered topic sentence; "widely considered in the field" and "outpace bacterial defenses" add filler.
- **Rewrite:** "Two strategies can help counter bacterial resistance: phage cocktails and phage engineering." (then develop each, as the paragraph already does.)

### E8. Discussion — "reinforcing the value of Hp3 as a platform"
- **Quote:** "...offer concrete, hypothesis-driven targets for future mechanistic study, reinforcing the value of Hp3 as a platform for investigating phage–host interactions beyond its immediate therapeutic application."
- **Why AI:** "reinforcing the value of … as a platform" is self-promotional closing glue (the "platform" framing recurs 3x across Discussion/Conclusion).
- **Rewrite:** "...offer testable targets for future mechanistic work." (let the platform claim appear once, in the Conclusion.)

### E9. Conclusion — "more than just a promising candidate" duplication
- **Quote (Discussion) vs (Conclusion):** Both the Discussion close and the Conclusion frame Hp3 as "a promising candidate… platform for next-generation phage therapies."
- **Why AI:** Near-verbatim "promising candidate + platform for next-generation therapies" is repeated in two consecutive sections — an LLM tends to re-deploy the same closing template.
- **Rewrite:** Keep the "candidate + platform" framing in **one** place (the Conclusion) and end the Discussion on a concrete, forward-looking experiment instead.

---

## F. Minor / lower-priority style notes (optional)

- **F1. "Similarly,"** (Results stability, B1) — mechanical inter-paragraph transition; delete.
- **F2. "In contrast,"** appears 3x (survival Results, histopathology Results) — acceptable for genuine contrasts, but check it is not reflexive; at least one ("In contrast, the tissue structure…") could become "Fish treated with Hp3 retained largely intact tissue…".
- **F3. "Beyond its therapeutic potential, our genomic analysis reveals that…"** (Discussion opener) — "reveals" is a mild inflation; "Beyond its therapeutic potential" is a smooth pivot. Consider "Our genomic analysis also shows that Hp3 represents a novel viral lineage."
- **F4. "winning a critical window of time"** (B4) and **"arms race"** metaphors — the co-evolution "arms race" framing is standard in phage biology and may stay; only the stacked metaphors (B4) need trimming.
- **F5. Heading "Genomic Analysis Reveals Hp3 Represents a Putative Novel Viral Family"** — "Reveals" in a heading is mild editorializing; "Hp3 represents a putative novel viral family" works without "Reveals". (Taxonomy wording itself left intact per instructions.)

---

## Items deliberately NOT flagged (per scope guard)

- All Results numbers, F-statistics, χ², p-values, Mash/VIRIDIC/ViPTree/VICTOR similarity values, accession numbers, MOI/titer/temperature/pH values.
- AMG wording (thyA, nrdD, DAHP synthase, shikimate pathway, Foldseek fident/E-value) and the surrounding hedges ("rest on sequence and structural homology and await experimental validation", "remains to be determined").
- Taxonomy/novel-family claims and their hedges ("putative", "convergent analyses indicate", "indicating that this protein-sharing link reflects a small number of conserved proteins").
- All `\citep{}` keys and their positions; all figure/table cross-references and captions' factual content.
- The "arms race" co-evolution framing (domain-standard) and the AMG "open question / future mechanistic study" hedges, which are appropriately calibrated.

**Statistical-significance check:** every remaining "significant/significantly" tied to a reported test (Log-rank, One-way ANOVA) is legitimate and was left in place. The only "significant"-class words flagged are the *non-statistical* uses: B3 "most critical finding", C3/A5 "perhaps more significantly", and the histology "significantly milder/reduces" (A3/C1) where the comparison is qualitative histopathology rather than a reported test.
