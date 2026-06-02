---
journal: "Cell Reports"
manuscript: "manuscript-cr.tex"
date: "2026-06-02"
guidelines_cached: "2026-06-02"
overall_status: "NEEDS ATTENTION"
---

# Compliance Report: Cell Reports

Manuscript: `manuscript-cr.tex` (compiled `manuscript-cr.pdf`)
Guidelines source: Cell Press pages via WebSearch (cell.com blocked automated fetch, HTTP 403), cached `~/.configure/journals/cell-reports.md` (2026-06-02)

Measured: 5 figures · 32 references · ~5,452 body words (incl. narrative Methods + figure legends).

## Summary

| Status  | Count |
|---------|-------|
| PASS    | 9     |
| WARNING | 4     |
| FAIL    | 1     |
| UNKNOWN | 2     |

## FAIL — Must Fix Before Submission

1. **Reference style — was numbered, Cell Reports requires author-year (Harvard).**
   Cell Press in-text citations are "(Smith et al., 2010)", reference list
   author-year — NOT numbered. The first CR build used `natbib[numbers]+unsrtnat`.
   **FIXED 2026-06-02**: reverted to `natbib[round,authoryear]+apalike` (same as the
   MBT build). Re-compile to confirm. *(This was an AI error from the prior turn,
   caught by the compliance check.)*

## WARNING — Review Recommended

1. **eTOC blurb length.** Cell Reports limit = **40 words**; the first draft was 47.
   **FIXED 2026-06-02**: trimmed In Brief to **39 words**.
2. **STAR Methods + Key Resources Table absent.** Methods are narrative
   ("Experimental Procedures", placed before Results). Cell Press allows a flexible
   initial-submission format, but STAR Methods + KRT are required at revision/final
   and strongly expected by Cell Reports. *Action: convert at revision; move Methods
   after Discussion; build the Key Resources Table (strains, phage, kits, software,
   accessions PRJNA1348731 / PX754746.1 / OQ594355).* 
3. **Graphical abstract not in the submission package.** Cell Reports
   requires/strongly expects one. Ready assets exist (`ga_v1.jpg … ga_v3.jpg`,
   `graphical_abstract.jpg`). *Action: pick one, confirm single-panel + size spec,
   upload as a separate file in Editorial Manager.*
4. **Summary word cap unconfirmed.** CR Summary is ~150–185 words by convention;
   current Summary ≈ 180 words. Likely fine; verify the exact cap on the
   initial-submission page.

## PASS — Compliant

- **Highlights**: 4 bullets, each ≤85 characters (incl. spaces). ✓
- **Figures**: 5 main figures ≤ 7 limit. ✓
- **Body word count**: ~5,452 incl. narrative Methods + legends; excluding Methods
  (which moves to STAR Methods, not counted) the Intro+Results+Discussion+legends is
  well under the 7,000-word Article limit. ✓
- **In Brief / eTOC**: present (39 words). ✓
- **Summary**: present, single paragraph, no citations. ✓
- **Cover letter**: CR-specific `cover_letter-cr.tex` (significance framing + 5
  suggested reviewers + confirmations). ✓
- **Data availability**: BioProject PRJNA1348731, genome PX754746.1, Figshare DOI,
  Zenodo code archive. ✓
- **Ethics**: IACUC approval (NWAFU-314020038) + AVMA euthanasia + ARRIVE reference. ✓
- **Competing interests + Author contributions**: present. ✓

## UNKNOWN — Manual Verification Needed

1. **Figure resolution of the final files.** `21-figs.qmd` saves PNG at dpi=300, but
   Cell Press wants TIFF/PDF/JPG at ≥300 DPI (≥600–1000 for line art) as separate
   files at revision. The embedded-PDF figures are fine for initial submission;
   provide hi-res separates later.
2. **Initial-submission enforcement of STAR Methods + graphical abstract** (vs
   revision). cell.com 403 prevented reading the initial-submission page directly;
   Cell Press flexible-format policy suggests narrative Methods are acceptable at
   initial submission, but confirm.

## Suggested Actions (priority order)

1. **[DONE]** Revert references to author-year (`apalike`); re-compile `manuscript-cr`.
2. **[DONE]** Trim eTOC blurb to ≤40 words.
3. Choose + size-check a graphical abstract from `ga_v*.jpg`; upload in EM.
4. Confirm Summary word cap and initial-submission STAR/GA enforcement on the live
   Cell Reports initial-submission page.
5. At revision only: convert Methods → STAR Methods, build the Key Resources Table,
   provide hi-res figure files.

## Strategic note — use Multi-Journal Submission

Cell Press Multi-Journal Submission lets one submission be considered by multiple
Cell Press journals at once (handling editor routes to those willing to review).
Recommended selection: **Cell Reports** (reach) **+ iScience** (realistic landing —
Cell Press's inclusive, technically-sound-science journal, stricter gatekeeping than
MBT, Cell-family brand, high fit for a phage isolation+characterization paper). Both
use the same author-year + STAR Methods format, so ONE manuscript serves both and
no separate Communications Biology (Nature, numbered) build is needed unless the
whole Cell Press route fails. See `~/.configure/journals/cell-reports.md`.
