# Statistical Paradox & Consistency Check — `body.tex`

**Manuscript:** vB_AhyM_Hp3 (Hp3) phage against *Aeromonas hydrophila* MS01
**File audited:** `/Users/allen/github/rujinlong/pc031-aquaPhage/manuscript/body.tex`
**Date:** 2026-05-30
**Method:** `statistical-paradox-checker` skill (14-point checklist) + arithmetic reconciliation of reported test statistics. No files modified.

---

## Verdict at a glance

| # | Issue | Severity | Where |
|---|-------|----------|-------|
| 1 | **ANOVA degrees of freedom are arithmetically impossible** for the stated design (6 groups × 3 reps ⇒ must be F(5,12), not F(5,15)) | **HIGH** | L421-422, L444-445 |
| 2 | **Pseudoreplication risk**: "n = 3 replicates" almost certainly technical (96-well) replicates analyzed as independent; ANOVA on a single endpoint ignores the 48-h time course | **HIGH** | L128-132, L242-252, L417-445 |
| 3 | **Omnibus ANOVA with no post-hoc test**, yet the text makes pairwise/ordinal claims ("most effective at MOI 1.0 and 10") | **HIGH** | L249-250, L423-424 |
| 4 | **Survival multiplicity**: 4 arms randomized, only 1 pairwise log-rank reported; no global test, no correction; "biosafety" claims (phage = 100%) never tested | **MEDIUM** | L207-218, L556-566 |
| 5 | **Over-claim vs. test run**: histopathology described as "significantly milder/reduced" but no statistical test was performed on histology | **MEDIUM** | L578-582 |
| 6 | **Survival-model assumption / quasi-complete separation** not addressed; log-rank borderline-valid here but Hp3 vs. bacteria (0 vs. 17 deaths) would break a Cox model | **LOW** | L556-566 |
| 7 | Reported test statistics are internally consistent with their own p-values (no fabrication detected) | **OK** | — |

**Single most important fix:** Correct the ANOVA degrees of freedom — they cannot be `F(5,15)` for "6 groups × 3 replicates" (the only design that fits 6 groups and 3 reps is `F(5,12)`). This is a hard arithmetic error a reviewer/editor will catch immediately, and resolving it forces clarification of the underlying replication/pseudoreplication issue (#2).

---

## Detailed findings

### [HIGH] 1 — ANOVA degrees of freedom are inconsistent with the stated design

**Reported (L421-422, L444-445):** One-way ANOVA, **F(5, 15) = 23.191, p < 0.001**, on OD600 "between groups at the 48-h endpoint." Figure 3 legend (L438-445): "five MOI values (0.01, 0.1, 1.0, 10 and 100) … incubated with the control group" and "mean ± SD of **three replicates**."

**The arithmetic does not close:**
- `df_between = 5` ⇒ **k = 6 groups** (5 MOI + 1 control). Consistent with the figure.
- `df_within = 15` ⇒ **N = df_within + k = 21** total observations ⇒ **21 / 6 = 3.5 replicates per group** — impossible for a balanced design.
- The design actually described (**6 groups × 3 replicates = 18** observations) gives `df_within = 18 − 6 = 12`, i.e. the test should read **F(5, 12)**, not F(5, 15).
- Conversely, `df_within = 15` would require either an unbalanced design summing to N = 21 (undocumented), or k = 7.5 groups at 3 reps (impossible).

**Why it matters:** Degrees of freedom encode the design. `F(5,15)` silently asserts ~21 independent observations; the Methods/figure assert 18. One of them is wrong. With the correct `F(5,12)`, the same F = 23.191 is still p < 0.001, so the *conclusion* survives — but the mismatch signals either (a) a transcription/software-default error, or (b) that more than 3 replicates (or wells counted as replicates) entered the model, which feeds directly into the pseudoreplication concern (#2).

**Suggested action:** Re-extract the ANOVA table from R, confirm N and k, and report df consistent with the actual number of *independent biological* replicates. If 6 groups × 3 biological reps, it is `F(5,12)`.

---

### [HIGH] 2 — Pseudoreplication: technical 96-well replicates and single-endpoint reduction

**Trigger (Survivorship/independence + design):** The lysis assay is a **96-well microplate** read every 20 min for 48 h (L128-132). "The experiment was repeated three times … three replicates" (L441-442).

**Two distinct problems:**

1. **Technical vs. biological replication.** If the "3 replicates" are 3 wells from one bacterial culture / one phage stock read in one plate run, they are *technical* replicates. Treating them as independent in ANOVA inflates the effective N and shrinks the error term — exactly the kind of independence violation that makes an F-test anticonservative. The Methods do not state whether the three repeats are independent biological replicates (separate cultures/days) or plate-level technical replicates. This must be made explicit.

2. **Throwing away the time course.** The data are a dense longitudinal trajectory (145 timepoints per well over 48 h), but the only inferential test is a **one-way ANOVA on the single 48-h endpoint**. The endpoint is the *least* informative timepoint biologically: the text itself notes regrowth from phage-resistant mutants by 48 h (L424-426, L640-642), so the endpoint OD partly reflects resistance emergence, not lytic efficacy. The strong, dose-dependent suppression the paper claims happens *earlier* in the curve and is never formally tested. A repeated-measures / mixed-effects model (or area-under-the-curve per well) would use the data the design actually generated and would respect the well as the unit of replication.

**Why it matters:** Pseudoreplication is the most common—and most penalized—statistical flaw in phage in-vitro kinetics papers. Both the inflated-independence reading of #1 and the endpoint-only choice point here.

**Suggested action:** (i) State whether n = 3 is biological or technical; if technical, the unit of analysis is the culture, not the well. (ii) Consider AUC-per-replicate or a mixed model over the full time course with MOI as a fixed effect and replicate as random; report the endpoint ANOVA only as a secondary summary.

---

### [HIGH] 3 — Omnibus ANOVA reported, but conclusions are pairwise/ordinal (no post-hoc)

**Trigger (Multiple Comparisons):** A one-way ANOVA tests only the global null "all 6 group means equal." A significant F says *somewhere* there is a difference — it does **not** license any specific pairwise statement.

**The text makes specific pairwise/ranking claims the ANOVA cannot support:**
- "Hp3 exhibited the **most effective and sustained** bacterial suppression at an MOI of **1.0 and 10**" (L423-424).
- "maintaining the bacterial density **below that of the untreated control**" (L418-419) — a treatment-vs-control contrast.

No post-hoc procedure (Tukey HSD, Dunnett vs. control, etc.) is mentioned anywhere (Methods L247-252; only "One-way ANOVA" + "p < 0.05"). The Statistical-analysis section never describes how the per-MOI comparisons were made.

**Why it matters:** This is the classic "significant omnibus → unguarded pairwise narrative" gap. Which MOI groups differ from control, and from each other, requires a multiplicity-controlled post-hoc; the global F alone is insufficient and the ranking claim ("1.0 and 10 best") is currently unsupported by any reported test.

**Suggested action:** Add a Dunnett test (each MOI vs. untreated control) or Tukey HSD for all pairwise contrasts, report adjusted p-values, and tie the "MOI 1.0/10 most effective" statement to those results — or soften it to a descriptive observation.

---

### [MEDIUM] 4 — Survival analysis: multiplicity across 4 arms, untested control claims

**Design (L207-218):** 80 fish randomized into **four** arms (phage-only, bacteria-only, treatment, PBS), 20 each.

**What is tested (L556-566, L601):** Exactly **one** pairwise log-rank: bacteria-only vs. treatment (χ² = 20.474, df = 1, p < 0.001). Verified internally consistent: χ²(1) = 20.474 ⇒ p ≈ 6.0 × 10⁻⁶, so "p < 0.001" is correct.

**Gaps:**
- **No global/stratified test** across the four curves; with 4 groups the standard practice is an overall log-rank first, then pre-specified contrasts. Selecting the single most-separated pair post hoc and reporting only it is a (mild) form of selective inference, even though here the contrast is the pre-registered primary endpoint and the effect is enormous.
- **Biosafety / phage-only "100% survival" (L556-558) and the PBS control are described but never tested.** The claim "demonstrating the biosafety of the phage" rests on an untested 100% curve. A phage-only-vs-PBS log-rank (expected non-significant) would substantiate "no phage toxicity"; absent that, it is an eyeball claim.
- **No multiplicity adjustment** is mentioned for the family of survival comparisons. With one reported test it is moot, but if the phage-vs-PBS and any other contrasts are added, control the family-wise error.

**Why it matters:** The headline result (treatment vs. bacteria) is robust and correctly tested. The surrounding *interpretive* claims (biosafety, control behavior) currently borrow significance from a test that did not include them.

**Suggested action:** Report the overall 4-group log-rank, plus the pre-specified treatment-vs-bacteria contrast; if asserting biosafety statistically, add the phage-vs-PBS (and bacteria-vs-PBS to confirm the model is lethal) comparisons with a stated correction.

---

### [MEDIUM] 5 — Over-claim vs. test run: histopathology "significant" without a test

**Reported (L578-582, L600-613):** Treated fish tissue "significantly milder than those in the infected group" and Hp3 "**significantly** reduces liver and spleen damage." Histology is qualitative H&E description; **no scoring scheme, no blinding, and no statistical test** is reported for the histopathology.

**Why it matters:** "Significantly" is a statistical word attached to a non-statistical, unblinded, unscored, descriptive observation (n and grading undocumented). Reviewers flag exactly this conflation.

**Suggested action:** Either introduce a semi-quantitative, blinded histopathology score (e.g., ordinal lesion grading) with a non-parametric group test, or replace "significantly" with descriptive language ("markedly milder," "fewer focal changes").

---

### [LOW] 6 — Survival-model assumptions / separation not addressed

The log-rank is assumption-light (it does not require proportional hazards to be valid as a test), so the reported bacteria-vs-treatment comparison is fine. Two caveats worth a sentence:
- **Quasi-complete separation** in the untested arms: phage-only and PBS appear to have 0 events; any *model-based* extension (Cox PH, hazard ratios) across all four arms would fail to converge / yield unstable HRs. Stick to log-rank + KM, or use Firth-penalized / exact methods if hazard ratios are desired.
- **Proportional-hazards** is not claimed and not needed for log-rank, but if an HR is ever reported, check PH (the bacterial curve drops fast then plateaus at 15% by day 3 — non-proportional shape).

No action required unless hazard ratios are added.

---

### [OK] 7 — Internal numerical consistency (no fabrication)

Cross-checks that **passed**:
- Survival fractions are integer-consistent with n = 20: 15% ⇒ 3 survivors / 17 deaths; 85% ⇒ 17 / 3. A crude 2×2 Pearson χ² on the final counts ≈ 19.6, close to the reported log-rank χ² = 20.474 (log-rank uses the full time course, so exact agreement is not expected) — the magnitude is plausible.
- χ²(1) = 20.474 → p ≈ 6 × 10⁻⁶: "p < 0.001" ✓.
- F(5,15) = 23.191 ≫ F₀.₀₀₁(5,15) ≈ 7.6: "p < 0.001" ✓ (and would remain p < 0.001 even at the corrected df F(5,12)).
- "Survival 15% → 85%" (L707) and "final survival rate of 85%" (L563) are mutually consistent.

So the reported statistics agree with their own claimed p-values; the issues above are **design/inference** problems, not arithmetic fabrication — except #1, where the *df themselves* are internally impossible for the stated design.

---

## Checklist coverage (paradoxes evaluated)

| Paradox | Applies? | Note |
|---|---|---|
| Simpson's | No | No pooling across hidden strata in the inferential tests |
| Ecological fallacy | No | Claims are at group level (survival, OD), matching the data level |
| Lord's paradox | Partial | Lysis curve is longitudinal but analyzed only at endpoint (see #2) — not baseline-adjusted, so Lord's per se doesn't bite; the change-vs-endpoint choice does |
| Berkson's / collider | No | No quality-filter conditioning in the wet-lab stats |
| Compositional bias | No | OD and survival are absolute, not relative-abundance data |
| **Multiple comparisons** | **Yes** | ANOVA→no post-hoc (#3); 4-arm survival, 1 test (#4) |
| Regression to mean | No | No selection on extreme baselines |
| Survivorship / pseudoreplication | **Yes** | Technical-replicate independence + endpoint reduction (#2) |
| Will Rogers | No | No reclassification between analyses |
| Base-rate neglect | No | n/a to these tests |
| MAUP | No | n/a |
| Immortal time | No | n/a (simultaneous challenge) |
| Post-treatment conditioning | No | No covariate adjustment in models |
| **Sample-size / df consistency** | **Yes** | F(5,15) impossible for 6×3 design (#1) |
| **Over-claim vs. test** | **Yes** | "significant" histopathology untested (#5); ranking claim beyond omnibus (#3) |

---

*Generated by the statistical-paradox-checker skill. This is a reasoning/consistency audit, not a re-analysis; recommendations should be confirmed against the raw data in `SupplementalData.xlsx` / Figshare before edits.*
