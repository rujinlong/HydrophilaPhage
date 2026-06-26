# HydrophilaPhage

This repository contains the public analysis code associated with the
manuscript:

> A novel lytic *Aeromonas* bacteriophage rescues largemouth bass from lethal
> *Aeromonas hydrophila* infection

The project is organized as a lightweight R package so that the Quarto
analysis notebooks can use shared helper functions and a declared dependency
set.

## Repository Contents

- `R/`: helper functions used by the analysis notebooks.
- `analyses/`: Quarto notebooks for genome post-processing, phylogenetic
  visualization, and manuscript figure generation.
- `DESCRIPTION`: R package metadata and dependency declarations.

## Analysis Notebooks

The public notebooks are:

- `analyses/111-bacterial_genome.qmd`
- `analyses/112-phage_genome.qmd`
- `analyses/113-tree.qmd`
- `analyses/121-figs.qmd`

They are intended to document the analysis logic and figure-generation code
used for the manuscript.

## License

This project is licensed under GPL-3.0. See [LICENSE.md](LICENSE.md).
