# Supplementary Information — *Aeromonas* phage vB_AhyM_Hp3 (Hp3)

Self-contained SI package for the Cell Press **Multi-Journal Submission**
(Cell Reports + iScience).

## Upload to Editorial Manager (2 files)
| File | Role |
|------|------|
| `supplementary.pdf` | Supplementary figures (S1–S3) & tables (S1–S5) |
| `SupplementalData.xlsx` | **Data S1** — raw *in vitro* / *in vivo* source data |

## Contents of `supplementary.pdf`
- **Figure S1** — vConTACT3 protein-sharing network
- **Figure S2** — PHROG functional-category distribution (105 ORFs)
- **Figure S3** — ViPTree whole-proteome similarity (*S*_G) of Hp3 to 5,632 references
- **Table S1** — Genome annotation (105 ORFs)
- **Table S2** — Resistance / virulence screening (CARD, VFDB)
- **Table S3** — Survival statistics (log-rank, Cox PH)
- **Table S4** — Closest references by *S*_G (ViPTree)
- **Table S5** — VIRIDIC nucleotide-level intergenomic similarity

## Rebuild
```bash
python3 make_si_tables.py     # Table S1, S4   (from analysis TSVs)
Rscript  make_si_figures.R    # Figure S2, S3  (from analysis TSVs)
latexmk supplementary.tex     # -> supplementary.pdf  (xelatex)
```
Source TSV/xlsx inputs live in the gitignored Dropbox data tree
(`~/Dropbox/project/pc031-aquaPhage/data`, reached via the `analyses/data` symlink).
Figure S1 (`vc3.png`) is read from `../../analyses/data/121-figs/`.
