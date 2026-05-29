# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project nature

This repo is structured as an **R package** (`HydrophilaPhage`, see `DESCRIPTION`) that exists primarily as a reproducibility wrapper around a set of **Quarto analysis notebooks** under `analyses/`. There is no library API to ship — `R/utils.R` holds helpers (e.g. `parse_vcontact3()`) that the notebooks load via `devtools::load_all()`. The package machinery is here so the notebooks can pin dependencies and use `devtools::load_all()` deterministically, not so users can `library(HydrophilaPhage)`.

The science: characterization of phage `vB_AhyM_Hp3` (genome + biology + in-vivo efficacy in largemouth bass) against *Aeromonas hydrophila* MS01. Heavy bioinformatics steps run **outside this repo** (Unicycler, RagTag, Bakta, Pharokka, Phold, Phynteny, vConTACT3); the `.qmd` files only ingest those outputs, post-process, and render figures.

## Data lives outside the repo

`analyses/data` is a **symlink** to `~/Dropbox/project/pc031-aquaPhage/data/` and is gitignored. Two consequences:

- Don't expect data when running on a fresh clone; the symlink target must exist locally.
- The Dropbox tree holds the manuscript artifacts (`manuscript.qmd`, `manuscript.tex`, `manuscript.docx`, `cover_letter*.docx`), the bibliography (`bibliography.bib` itself symlinks into the user's Zotero export), the LaTeX class (`elsarticle.cls`), and per-step input/output directories. Edits to the manuscript happen there, not in this repo.

`analyses/data/submit/SupplementalData.xlsx` is the wet-lab data source for `21-figs.qmd` (growth curve, temperature/pH stability, MOI, lysis, survival sheets).

## projthis layout — non-obvious conventions

Every `.qmd` setup chunk follows the same `projthis` skeleton, and downstream code depends on these path helpers being in scope:

```r
here::i_am("<NN-name>.qmd", uuid = "<stable-uuid>")
projthis::proj_create_dir_target(params$name, clean = FALSE)
path_target   <- projthis::proj_path_target(params$name)   # analyses/data/<NN-name>/
path_source   <- projthis::proj_path_source(params$name)   # analyses/data/<NN-name>/
path_raw      <- path_source("00-raw")                     # analyses/data/00-raw/
path_resource <- here::here(path_raw, "d00-resource")      # shared resources across steps
path_data     <- here::here(path_raw, paste0("d", params$name))  # raw inputs for THIS step
```

- **Outputs go to `path_target("<file>")`** — everything written by chunk code goes there. Don't write into the repo tree.
- **Raw inputs live at `path_raw / d<NN-name> /`** — each step has its own `dNN-stepname` subdir under `00-raw`. Cross-step shared inputs go in `d00-resource`.
- **UUIDs in `here::i_am()` are not decorative.** They anchor the project root; don't change them when copy-pasting a setup chunk into a new notebook (regenerate one).
- `params$name` is set both in the YAML `params:` block (for `quarto render`) and re-set inside an `eval: !expr interactive()` chunk (so RStudio runs also work). Keep both in sync if you rename a notebook.

## Notebook numbering

The leading two digits encode dependency tier, not a strict sequence:

| Range | Topic                                                              |
|-------|--------------------------------------------------------------------|
| `1x`  | Sequence/genome analyses (bioinformatics post-processing)          |
| `2x`  | Wet-lab data → figures for the manuscript                          |

Currently: `11-bacterial_genome`, `12-phage_genome`, `13-tree`, `21-figs`. New genome-side work → `14-…`; new figure-side work → `22-…`.

## How to render

```bash
# Single notebook
quarto render analyses/12-phage_genome.qmd

# Whole directory (renders every .qmd in analyses/)
quarto render analyses/
```

There is no `_quarto.yml` — each `.qmd` is self-contained (format + params in its own YAML).

R package side (rarely needed; the package isn't published):

```bash
R -e 'devtools::document()'   # regenerate NAMESPACE from roxygen2 tags in R/*.R
R -e 'devtools::load_all()'   # what the .qmd setup chunks call internally
R -e 'devtools::check()'      # CRAN-style check (heavyweight, only before tagging a release)
```

There are no unit tests (`testthat/edition: 3` is configured in DESCRIPTION but no `tests/` directory exists). Don't fabricate a test command.

## Conventions that have bitten before

- `21-figs.qmd` saves with `device = "png", dpi = 300`. Don't switch to PDF/SVG without checking that downstream manuscript inclusion (in the Dropbox tree) expects PNG.
- `geneviewer`, `ggtree`, `ape`, `survival` are step-specific and only loaded in the notebooks that need them — don't promote them into a global setup file.
- `R/utils.R::parse_vcontact3()` expects `final_assignments.csv` from vConTACT3 with columns `Genome`, `genus_prediction`, `Reference`. If the vConTACT3 output schema changes, that's where to fix it.

## Manuscript pipeline note

The manuscript itself (`.qmd` → `.tex` → `.docx`) is rendered from `~/Dropbox/project/pc031-aquaPhage/data/manuscript.qmd` using `elsarticle.cls` and the bibliography at `data/bibliography.bib` (Zotero export). When the user asks to "update the manuscript" or "respond to reviewers," work in the Dropbox tree, not in this repo's `analyses/`.
