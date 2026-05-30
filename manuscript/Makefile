# ============================================================
#  Makefile — Hp3 manuscript (Microbial Biotechnology / Wiley build)
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
#    make clean      remove aux files (keep PDFs)
#    make distclean  remove aux + generated PDFs/derived .tex
#
#  Deps: TeX Live (xelatex, latexmk, latexpand, texcount), python3.
#        latexpand/texcount: `tlmgr install latexpand texcount` if missing.
# ============================================================
MAIN = manuscript
BODY = body.tex
BIB  = bibliography.bib

.PHONY: all pdf flat anonymize wordcount clean distclean

all: pdf

## Build manuscript.pdf (latexmk handles xelatex+bibtex passes)
pdf: $(MAIN).pdf
$(MAIN).pdf: $(MAIN).tex $(BODY) $(BIB)
	latexmk

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
	rm -f $(MAIN)-anon-raw.tex

## Full clean incl. generated PDFs and derived sources
distclean: clean
	-latexmk -C >/dev/null 2>&1
	rm -f $(MAIN)-flat.tex $(MAIN)-anon.tex $(MAIN)-anon.pdf
