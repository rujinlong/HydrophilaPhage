#!/usr/bin/env python3
r"""Preprocess the flattened LaTeX source for a faithful pandoc -> docx conversion.

pandoc cannot read several constructs in this manuscript's LaTeX back into a
correct Word document. This script fixes them on the flattened source
(manuscript-flat.tex) BEFORE pandoc runs. It does NOT touch body.tex /
manuscript.tex (the PDF pipeline is left untouched).

Fixes applied (each one was an observed docx defect; see Makefile docx note):
  1. Figures: body.tex wraps every figure as
        \centering{ ... \pandocbounded{\includegraphics[..]{..}} ... }
     The `\centering{...}` brace-group hides \includegraphics from pandoc's
     figure handler and pandoc SILENTLY drops the image. We normalize to
     standard `\centering` + bare `\includegraphics` (which pandoc embeds and,
     together with `-t docx+native_numbering`, auto-numbers as "Figure N").
  2. Authors / affiliations: the frontmatter uses authblk
        \author[1,2]{Name}  ... \affil[1]{Institution} ...
     pandoc keeps only the author NAMES, dropping the affiliation superscripts
     and every \affil line entirely. We parse the authblk macros from the
     source and rebuild a clean frontmatter block (names with affiliation
     superscripts; affiliations listed one per line; corresponding-author
     line) and inject it right after \maketitle, deleting the authblk macros
     so pandoc does not emit a second, mangled author list.
  3. Abstract -> "Summary" (Microbial Biotechnology house style).

Reads argv[1] (or stdin), writes the transformed LaTeX to stdout.
"""
import re
import sys


def extract_braced(s, open_idx):
    """Given s[open_idx] == '{', return (inner_text, index_of_matching_close)."""
    depth = 0
    i = open_idx
    while i < len(s):
        c = s[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return s[open_idx + 1:i], i
        i += 1
    return None, open_idx  # unbalanced; caller should guard


def main():
    src = (open(sys.argv[1], encoding="utf-8").read()
           if len(sys.argv) > 1 else sys.stdin.read())

    # ---- 1. figure normalization -------------------------------------------
    src = re.sub(
        r'\\centering\{\s*\\pandocbounded\{'
        r'(\\includegraphics\[[^\]]*\]\{[^}]*\})\}\s*\}',
        lambda m: '\\centering\n\n' + m.group(1) + '\n',
        src,
    )
    # unwrap any remaining \pandocbounded{\includegraphics...} not in a group
    src = re.sub(
        r'\\pandocbounded\{(\\includegraphics\[[^\]]*\]\{[^}]*\})\}',
        lambda m: m.group(1),
        src,
    )

    # ---- 2. authors / affiliations -----------------------------------------
    # \author[affil_ids]{Name}  (one per line)
    authors = []
    for m in re.finditer(r'\\author\[([^\]]*)\]\{(.*)\}[ \t]*$', src, re.M):
        affil_ids, name = m.group(1).strip(), m.group(2).strip()
        corr = ('\\textsuperscript{*}' in name) or name.endswith('*')
        name = re.sub(r'\\textsuperscript\{\*\}', '', name).rstrip('*').strip()
        sup = affil_ids + (',*' if corr else '')
        authors.append((name, sup))

    # \affil[n]{Institution}  (one per line)
    affils = []
    for m in re.finditer(r'\\affil\[(\d+)\]\{(.*)\}[ \t]*$', src, re.M):
        affils.append((m.group(1).strip(), m.group(2).strip()))

    # corresponding-author footnote: \blfootnote{ ... } (balanced)
    corr_line = ""
    bf = src.find(r'\blfootnote{')
    if bf != -1:
        brace = bf + len(r'\blfootnote')
        inner, _ = extract_braced(src, brace)
        if inner:
            inner = inner.replace(r'\textsuperscript{*}', '')
            corr_line = re.sub(r'\s+', ' ', inner).strip()

    if authors:
        names = ', '.join(
            '%s\\textsuperscript{%s}' % (n, s) for n, s in authors)
        parts = [names, '']
        for num, text in affils:
            parts.append('\\textsuperscript{%s}%s' % (num, text))
            parts.append('')
        if corr_line:
            parts.append('\\textsuperscript{*}' + corr_line)
            parts.append('')
        frontmatter = '\n'.join(parts)

        # drop the authblk macros so pandoc won't emit its own author list
        src = re.sub(r'\\author\[[^\]]*\]\{.*\}[ \t]*\n', '', src)
        src = re.sub(r'\\affil\[\d+\]\{.*\}[ \t]*\n', '', src)

        # replace everything from \maketitle up to the abstract/Summary with
        # \maketitle + our clean frontmatter (this also removes \blfootnote)
        src = re.sub(
            r'\\maketitle.*?(?=\\begin\{abstract\}|\\section\*\{Summary\})',
            lambda m: '\\maketitle\n\n' + frontmatter + '\n\n',
            src, count=1, flags=re.S,
        )

    # ---- 3. abstract -> Summary --------------------------------------------
    src = src.replace(r'\begin{abstract}', r'\section*{Summary}' + '\n')
    src = src.replace(r'\end{abstract}', '')

    sys.stdout.write(src)


if __name__ == "__main__":
    main()
