---
journal: "Microbial Biotechnology"
manuscript: "manuscript.tex"
date: "2026-05-30"
guidelines_cached: "2026-05-30"
overall_status: "NEEDS ATTENTION"
---

# Compliance Report: Microbial Biotechnology

Manuscript: `manuscript.tex` (+ `body.tex`, compiled `manuscript.pdf`, 17 pp)
Guidelines source: Wiley author guidelines (page paywalled to fetch; WebSearch snippets + Wiley standards), cached 2026-05-30.

## Summary

| Status | Count |
|--------|-------|
| PASS    | 8 |
| WARNING | 4 |
| FAIL    | 2 |
| UNKNOWN | 3 |

## FAIL — Must Fix Before Submission

1. **ORCID missing.** Wiley requires/strongly expects an ORCID iD for the submitting/corresponding author at submission. The manuscript and frontmatter contain none.
   → Fix: at minimum supply ORCID for the submitting corresponding author (Jinlong Ru) in the submission system; ideally add ORCIDs for all corresponding authors. Not necessarily in the .tex, but required in ScholarOne.

2. **Cover letter — explicit confirmations.** Microbial Biotechnology requires the cover letter to (a) give the corresponding author's **consent to publication** and (b) **explicitly state that content and authorship are approved by all authors**. The current `cover_letter.tex` implies originality/approval but does not use these explicit confirmations.
   → Fix: add one sentence, e.g. *"The corresponding author consents to publication, and confirms that the content and authorship of this manuscript have been approved by all authors."* (Easy; I can patch it.)

## WARNING — Review Recommended

1. **APC is mandatory (~$4,260 USD).** Microbial Biotechnology is fully Open Access; there is no non-OA route. Confirm funding/waiver eligibility before committing. (Not a formatting issue, but a hard gate.)
2. **Figure format = PNG.** Figures are 300-dpi PNG (`121-figs/fig1–5.png`). Acceptable for initial submission; **production** typically wants TIFF/EPS/PDF (vector for line art). Keep editable sources ready.
3. **Reference style approximation.** Body uses `apalike` (author-year). Microbial Biotechnology's exact rule (≤7 authors list all; ≥8 → first 6 + "et al."; title included) may differ from apalike's truncation. Fine for initial submission; switch to the official Wiley `.bst` at revision.
4. **Abstract length.** 231 words — under the common 250-word ceiling but close; trim if the journal's confirmed limit is lower.

## PASS — Compliant

- Manuscript structure: Abstract / Introduction / Materials & Methods / Results / Discussion / Conclusion all present.
- Reference style family correct (author-year, not numbered).
- All required declarations present: Ethics, Competing interests, Funding, Data availability, Authors' contributions, Acknowledgements.
- Data availability names recognized repositories (BioProject PRJNA1348731, Figshare DOI, Zenodo DOI).
- Animal-study reporting: ARRIVE guidelines + IACUC approval (NWAFU-314020038) stated.
- Cover letter exists and asserts originality / not under consideration / no competing interests.
- Body length (~5,000 words) is reasonable for a research article ("concise").
- Compiles cleanly to PDF (single-PDF initial submission supported).

## UNKNOWN — Manual Verification Needed

1. Exact abstract word limit (assumed ≤250; verify).
2. Exact figure dpi/format requirement (assumed Wiley-standard 300 dpi; verify).
3. Whether native LaTeX is required at initial submission or PDF suffices with source later (verify in submission system).

## Suggested Actions (priority order)

1. **[FAIL-2]** Patch `cover_letter.tex` with the explicit consent + all-authors-approval sentence. *(I can do this now.)*
2. **[FAIL-1]** Obtain/record ORCID for corresponding author(s) — enter in ScholarOne at submission.
3. **[WARNING-1]** Confirm APC funding (~$4,260) — institutional/grant OA support or waiver.
4. **[WARNING-2]** Keep vector/TIFF figure sources ready for production.
5. **[UNKNOWN]** Verify abstract limit, figure spec, and initial-submission file policy on the journal site/ScholarOne before final upload.
