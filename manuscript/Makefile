# ============================================================
#  Makefile — Hp3 manuscript (PRIMARY: Cell Reports; fallback: Microbial Biotechnology)
# ------------------------------------------------------------
#  Engine: xelatex via latexmk (see .latexmkrc). Frontmatter in
#  manuscript.tex; sections in body.tex (\input). Bibliography:
#  bibliography.bib (symlink -> Zotero), author-year via apalike.
#
#  Targets:
#    make            build manuscript.pdf
#    make flat       flatten \input{body} -> manuscript-flat.tex (single-file)
#    make anonymize  -> manuscript-anon.pdf  (authors/affil/funding/URLs scrubbed;
#                       upload to NotebookLM for double-blind adversarial review)
#    make wordcount  body word count (texcount)
#    make docx       manuscript.docx via pandoc (Word submission portals)
#    make clean      remove aux files (keep PDFs)
#    make distclean  remove aux + generated PDFs/derived .tex
#
#  Deps: TeX Live (xelatex, latexmk, latexpand, texcount), python3.
#        latexpand/texcount: `tlmgr install latexpand texcount` if missing.
# ============================================================
# MAIN = primary build target. Cell Reports (manuscript-cr) is primary per pm
# DEC-D026/D027 (Cell Press Multi-Journal Submission: CR + iScience). Build the
# Microbial Biotechnology fallback instead with:  make MAIN=manuscript
MAIN = manuscript-cr
BODY = body.tex          # CR initial submission uses \input{body} (DEC-D028)
BIB  = bibliography.bib

.PHONY: all pdf flat anonymize wordcount docx clean distclean

all: pdf

## Build manuscript.pdf (latexmk handles xelatex+bibtex passes)
pdf: $(MAIN).pdf
$(MAIN).pdf: $(MAIN).tex $(BODY) $(BIB)
	latexmk $(MAIN).tex

## Flatten \input{body} into one self-contained source (journals wanting single .tex)
flat: $(MAIN)-flat.tex
$(MAIN)-flat.tex: $(MAIN).tex $(BODY)
	latexpand --keep-comments $(MAIN).tex > $(MAIN)-flat.tex
	@echo "Single-file submission source: $(MAIN)-flat.tex"

## Anonymized PDF for NotebookLM / double-blind adversarial review
##   flatten -> scrub author/affil/email/funding/contributions/URLs -> compile
anonymize: $(MAIN)-anon.pdf
$(MAIN)-anon.tex: $(MAIN).tex $(BODY) anonymize.py
	latexpand --keep-comments $(MAIN).tex > $(MAIN)-anon-raw.tex
	python3 anonymize.py $(MAIN)-anon-raw.tex $(MAIN)-anon.tex
	rm -f $(MAIN)-anon-raw.tex
$(MAIN)-anon.pdf: $(MAIN)-anon.tex $(BIB)
	latexmk $(MAIN)-anon.tex
	@echo
	@echo ">> Anonymized artifact: $(MAIN)-anon.pdf  (upload to NotebookLM)"
	@echo ">> Scan $(MAIN)-anon.tex for residual self-citations / lab names before upload."

## Word count of the body (follows \input)
wordcount:
	@texcount -sum=1 -inc $(MAIN).tex | tail -5

## Clean intermediates (keep PDFs)
clean:
	-latexmk -c >/dev/null 2>&1
	-latexmk -c $(MAIN)-anon.tex >/dev/null 2>&1
	rm -f $(MAIN)-anon-raw.tex $(MAIN)-docx.tex reference-default.docx

## Full clean incl. generated PDFs and derived sources
distclean: clean
	-latexmk -C >/dev/null 2>&1
	rm -f $(MAIN)-flat.tex $(MAIN)-anon.tex $(MAIN)-anon.pdf

## Word (.docx) via pandoc for journal portals that require Word (e.g. ScholarOne
## Main Document). pandoc CANNOT read this manuscript's LaTeX back faithfully on
## its own; prep_docx.py repairs the constructs it mishandles, then pandoc runs
## with docx-specific flags. Every piece below maps to a real, observed defect
## (figures unnumbered, citations not clickable, affiliations dropped) — see
## prep_docx.py docstring. Do NOT simplify back to a bare `pandoc flat.tex`.
##   * prep_docx.py             (a) normalize `\centering{...\pandocbounded{
##                              \includegraphics}}` figures, else pandoc SILENTLY
##                              drops every image; (b) rebuild author/affiliation
##                              frontmatter from authblk (pandoc drops \affil +
##                              author superscripts); (c) abstract -> Summary.
##   * -t docx+native_numbering auto-number figures/tables as Word SEQ fields
##                              ("Figure N"/"Table N"). A writer EXTENSION, NOT
##                              `-M native_numbering=true` (that silently no-ops).
##   * -M link-citations=true   inline citations hyperlink to the reference list;
##                              \ref cross-references become clickable.
## Verify:  unzip -p $(MAIN).docx word/document.xml | grep -c SEQ   # >0
##          unzip -l $(MAIN).docx | grep -c word/media/             # = #figures
## NOTE: figures live under the gitignored Dropbox symlink tree; if that subtree
## is offline/unreadable the images drop out (pandoc warns "Could not fetch
## resource") but every other fix still applies.
## `docx` is .PHONY (always rebuilds): the figures sit behind a gitignored
## symlink and carry stale mtimes (2025), so a file-target + timestamp check
## would wrongly report "Nothing to be done for docx" after the images change.
## Rebuilding is only a few seconds; the flat.tex prereq still triggers a
## re-flatten when body.tex / manuscript.tex change. --reference-doc applies the
## Times New Roman / all-black-heading academic house style (see reference.docx).
docx: $(MAIN)-flat.tex $(BIB) prep_docx.py reference.docx
	python3 prep_docx.py $(MAIN)-flat.tex > $(MAIN)-docx.tex
	pandoc $(MAIN)-docx.tex --bibliography=$(BIB) --citeproc \
	  -M link-citations=true -t docx+native_numbering \
	  --reference-doc=reference.docx --no-highlight \
	  --resource-path=.:../analyses/data/121-figs -o $(MAIN).docx
	@rm -f $(MAIN)-docx.tex
	@echo ">> Word version: $(MAIN).docx (Times New Roman, black headings, numbered figures, linked citations)"

## Academic reference template (Times New Roman + all-black headings) for the
## docx build. Derived from pandoc's default by make_reference_docx.py; it is
## gitignored. Delete reference.docx to force a rebuild (e.g. after editing the
## script); `make clean` removes the temp file.
reference.docx: make_reference_docx.py
	pandoc --print-default-data-file reference.docx > reference-default.docx
	python3 make_reference_docx.py reference-default.docx reference.docx
	@rm -f reference-default.docx
	@echo ">> reference.docx (Times New Roman, black headings)"
