# Self-contained latexmk config for the SI document.
# Engine: xelatex (Times New Roman via fontspec). No bibliography (SI has no \cite).
# Usage:  latexmk            # build supplementary.pdf
#         latexmk -C         # clean everything incl. .pdf
$pdf_mode      = 5;          # 5 = xelatex
$xelatex       = 'xelatex -interaction=nonstopmode -halt-on-error -synctex=1 %O %S';
@default_files = ('supplementary.tex');
$clean_ext     = 'synctex.gz';
