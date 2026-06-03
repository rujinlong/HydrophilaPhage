# latexmk configuration for the Hp3 manuscript.
# PRIMARY TARGET = Cell Reports (manuscript-cr.tex) per pm DEC-D026/D027: the
# bare `latexmk` now builds the Cell Reports PDF (manuscript-cr.pdf), which is
# what the Cell Press Multi-Journal Submission (CR + iScience) requires.
# Engine: xelatex (Times New Roman via fontspec). References: bibtex + apalike.
# Usage:  latexmk             # build manuscript-cr.pdf (Cell Reports, default)
#         latexmk manuscript  # build manuscript.pdf   (Microbial Biotechnology fallback)
#         latexmk -c          # clean aux files (keep .pdf/.bbl)
#         latexmk -C          # clean everything incl. .pdf

$pdf_mode      = 5;          # 5 = xelatex
$bibtex_use    = 2;          # run bibtex; clean .bbl on -C
@default_files = ('manuscript-cr.tex');   # Cell Reports = primary target (DEC-D026/D027)

# treat undefined-citation / rerun prompts as non-fatal during iteration
$xelatex = 'xelatex -interaction=nonstopmode -halt-on-error -synctex=1 %O %S';

# extra files to remove on cleanup
$clean_ext = 'bbl run.xml synctex.gz';
