# Adversarial Review — Handoff for a Fresh Session

Run the `adversarial-review` skill on the Hp3 manuscript in a NEW session
(this is the last pre-submission task; it needs full context for the
multi-round NotebookLM → Codex loop).

## Inputs (ready)
- **Anonymized PDF for NotebookLM**: `manuscript/manuscript-anon.pdf`
  (de-identified; residual-identity scan was clean — authors/affiliations/
  funding/URLs/accessions all stripped or redacted).
- Non-anon source for reference: `manuscript/manuscript.pdf`, `manuscript.tex` + `body.tex`.
- Target journal: **Microbial Biotechnology** (Wiley).

## NotebookLM source strategy (per user)
- The PDFs of references already in Zotero are all in the user's **Google Drive** →
  use **`gws` (Google Workspace Search)** to find them and add directly to NotebookLM.
- For any missing reference → upload it, or download from the web then upload,
  or import the web URL directly into NotebookLM.
- Seed sources from the manuscript's 31 cited references (`\citep` keys in
  `body.tex` / `bibliography.bib`) plus key phage-taxonomy / phage-therapy /
  Aeromonas-phage papers for an adversarial knowledge base.

## Environment (ready)
- NotebookLM: `nlm` is already logged in (notebooklm-mcp + `nlm` CLI).
- Codex: subscription active — invoke directly with the `codex` command.

## Already self-checked pre-submission (do NOT just re-litigate these)
F(5,15) df verified correct (control n=6); Tukey HSD added (MOI 1/10 strongest);
pseudoreplication addressed in Methods (replicate wells); 31/31 refs verified;
de-AI pass done; journal compliance done; ORCID added; a limitations sentence
added to the Discussion. Let the hostile reviewer find what we MISSED.

## Suggested adversarial focus (find blind spots beyond the above)
- Strength of the **new genus / putative new family** taxonomy claim (VICTOR
  family OPTSIL caveat is already handled internally — see DEC-D017).
- The **putative AMG** interpretation (deliberately down-toned; check it stays defensible).
- **In vivo design**: only one log-rank comparison reported, biosafety not
  powered, single-endpoint in vitro — is the limitations sentence sufficient?
- **Novelty vs prior Aeromonas-phage / aquaculture phage-therapy literature.**

## Loop
NotebookLM hostile review (N rounds, distinct trap category each) → Codex
(GPT-5.x) independent adjudication → implement confirmed issues into `body.tex`
→ `cd manuscript && latexmk` to recompile. See pm `S-2026-05-29-001` for full context.
