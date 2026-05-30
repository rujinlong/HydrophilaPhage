# latexmk configuration for the Hp3 manuscript (Microbial Biotechnology build)
# Engine: xelatex (Times New Roman via fontspec). References: bibtex + apalike.
# Usage:  latexmk            # build manuscript.pdf
#         latexmk -c         # clean aux files (keep .pdf/.bbl)
#         latexmk -C         # clean everything incl. .pdf

$pdf_mode      = 5;          # 5 = xelatex
$bibtex_use    = 2;          # run bibtex; clean .bbl on -C
@default_files = ('manuscript.tex');

# treat undefined-citation / rerun prompts as non-fatal during iteration
$xelatex = 'xelatex -interaction=nonstopmode -halt-on-error -synctex=1 %O %S';

# extra files to remove on cleanup
$clean_ext = 'bbl run.xml synctex.gz';
