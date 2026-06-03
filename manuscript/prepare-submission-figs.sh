#!/usr/bin/env bash
# Prepare manuscript figures for submission so a plain `latexmk` build yields a
# compact, Apple-Preview-safe PDF — WITHOUT any Ghostscript post-processing.
#
# Two distinct bugs make figures render BLANK in Apple Preview / Quartz and some
# Editorial Manager viewers (poppler/pdfimages still show them, hiding the bug):
#   1. PNG alpha channel  -> becomes a PDF SMask -> blank in Quartz.
#   2. Ghostscript pdfwrite -> rewrites images to ICCBased colorspace -> blank.
# Both are avoided by fixing the figures at the SOURCE: flatten alpha onto white
# (DeviceRGB, no SMask) and downsample the oversized panels. See pm EL-007/EL-008.
#
# Originals are backed up to 121-figs/.orig-alpha/ on first run. Idempotent.
# After running, rebuild:  latexmk -gg manuscript-cr.tex
set -euo pipefail

FIGS="${1:-$HOME/Dropbox/project/pc031-aquaPhage/data/121-figs}"
cd "$FIGS"
mkdir -p .orig-alpha

# Large raster/composite panels (photos + layout) that carried alpha and were
# oversized. fig2/fig3 are small ggplot exports and render fine — left untouched.
for f in fig1 fig4 fig5; do
  [ -f ".orig-alpha/$f.png" ] || cp "$f.png" ".orig-alpha/$f.png"
  magick "$f.png" -background white -alpha remove -alpha off -resize 2000x "$f.png"
  echo "  optimized $f.png -> $(file "$f.png" | grep -oE '[0-9]+ x [0-9]+') (DeviceRGB, no alpha)"
done

echo "Done. Now rebuild the PDF:  latexmk -gg manuscript-cr.tex"
echo "Verify in Apple Preview (NOT just pdfimages): figures must be visible."
