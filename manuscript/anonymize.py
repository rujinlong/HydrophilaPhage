#!/usr/bin/env python3
"""Anonymize a flattened LaTeX manuscript for NotebookLM / double-blind review.

Adapted for the pc031-aquaPhage manuscript, which uses an article-class +
authblk frontmatter (\\author[..]{..}, \\affil[..]{..}, \\thanks{..}) and a
\\subsection-based Declarations block. Scrubs:
  - frontmatter: \\author / \\affil bodies, \\thanks (corresponding emails),
    \\samethanks, pdfauthor metadata
  - Declarations: Ethics / Funding / Data availability / Author contributions /
    Acknowledgements section bodies -> [Redacted for double-blind review]
  - identity-leaking URLs (github.com/rujinlong, figshare, zenodo), accessions
    (PRJNA*, NWAFU-*), and institution names

Preserves: title, abstract, keywords, body text, figures, tables, references.
Usage: anonymize.py <input.tex> <output.tex>
NOTE: always eyeball the output .tex for residual self-citations / lab names.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def _find_balanced(s: str, start: int) -> int:
    if s[start] != "{":
        raise ValueError(f"expected '{{' at pos {start}, got {s[start]!r}")
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError("unbalanced braces")


def _replace_command(text: str, head_pattern: str, repl_fn) -> str:
    """Replace `head_pattern` + following balanced `{...}` body."""
    out: list[str] = []
    cursor = 0
    for m in re.finditer(head_pattern, text):
        body_open = m.end()
        while body_open < len(text) and text[body_open] != "{":
            body_open += 1
        if body_open >= len(text):
            continue
        body_close = _find_balanced(text, body_open)
        out.append(text[cursor : m.start()])
        out.append(repl_fn(m, text[body_open + 1 : body_close - 1]))
        cursor = body_close
    out.append(text[cursor:])
    return "".join(out)


def anonymize(text: str) -> str:
    # --- \author[..]{Name ...\thanks{...}} -> anonymous (also drops \thanks) ---
    idx = [0]

    def repl_author(m, body):
        idx[0] += 1
        return rf"\author[1]{{Anonymous Author~{idx[0]}}}"

    text = _replace_command(text, r"\\author\[[^\]]*\]", repl_author)

    # --- \affil[N]{...} -> anonymized institution ---
    def repl_affil(m, body):
        num_m = re.search(r"\[([^\]]*)\]", m.group(0))
        num = num_m.group(1) if num_m else "1"
        return rf"\affil[{num}]{{[Anonymized affiliation {num}]}}"

    text = _replace_command(text, r"\\affil\[[^\]]*\]", repl_affil)

    # --- corresponding-author footnotes: \thanks{...} and \blfootnote{...} ---
    text = _replace_command(text, r"\\thanks", lambda m, b: "")
    # lookahead {...} so we strip the \blfootnote{...} CALL but keep the
    # \newcommand\blfootnote[1]{...} DEFINITION (whose name is followed by '[').
    text = _replace_command(text, r"\\blfootnote(?=\{)", lambda m, b: "")
    text = text.replace(r"\samethanks", "")

    # --- pdf metadata leaking author names ---
    text = _replace_command(text, r"pdfauthor=", lambda m, b: "pdfauthor={Anonymous}")

    # --- redact identifying Declarations subsections (body kept structurally) ---
    decl = r"Ethics statement|Funding|Data availability|Authors['’]? [Cc]ontributions|Acknowledgements"
    text = re.sub(
        rf"(\\subsection\{{(?:{decl})\}}(?:\s*\\label\{{[^}}]*\}})?\s*)"
        rf"(.*?)"
        rf"(?=\\subsection\{{|\\section\{{|\\bibliography|\\end\{{document\}})",
        r"\1\n[Redacted for double-blind review.]\n\n",
        text,
        flags=re.DOTALL,
    )

    # --- scrub identity-leaking URLs / accessions ---
    text = re.sub(r"https?://[^\s,)}]*github\.com/rujinlong[^\s,)}]*", "[anonymized repository]", text)
    text = re.sub(r"https?://[^\s,)}]*(?:figshare|zenodo)[^\s,)}]*", "[anonymized data repository]", text)
    text = re.sub(r"\bPRJNA\d+\b", "[anonymized BioProject]", text)
    text = re.sub(r"\bNWAFU-\d+\b", "[anonymized approval no.]", text)

    # --- belt-and-suspenders: institution names anywhere (incl. across line breaks) ---
    # \s+ matches the line wraps that latexpand preserves from the source.
    for inst in (
        r"Hainan\s+Institute\s+of\s+Northwest\s+A\\?&F\s+University",
        r"Northwest\s+A\\?&F\s+University",
        r"Technical\s+University\s+of\s+Munich",
        r"Helmholtz\s+Centre\s+Munich",
        r"TUM\s+School\s+of\s+Life\s+Sciences",
        r"Central\s+Institute\s+of\s+Infection\s+Prevention",
        r"Institute\s+of\s+Virology",
    ):
        text = re.sub(inst, "[Anonymized institution]", text)

    return text


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: anonymize.py <input.tex> <output.tex>", file=sys.stderr)
        return 1
    src = Path(sys.argv[1]).read_text(encoding="utf-8")
    Path(sys.argv[2]).write_text(anonymize(src), encoding="utf-8")
    print(f"Wrote anonymized manuscript: {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
