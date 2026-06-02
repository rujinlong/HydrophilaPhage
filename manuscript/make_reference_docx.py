#!/usr/bin/env python3
r"""Build the pandoc --reference-doc for the docx build, enforcing an academic
house style on pandoc's default template:

  1. Times New Roman everywhere. pandoc's default leans on the Office theme
     fonts (majorFont = headings, minorFont = body; currently "Aptos Display"
     / "Aptos"). Every built-in style inherits from the theme rather than
     naming a font, so rewriting the theme's major/minor <a:latin> typefaces
     is enough to switch the whole document to Times New Roman.
  2. All text black. The default colours headings/title/subtitle/caption in
     blues and greys (0F4761, 365F91, 4F81BD, 272727, 595959). Academic
     journals typeset everything in black, so every explicit <w:color> in
     styles.xml is forced to 000000 (theme-tinted colours dropped too).

Usage: make_reference_docx.py <pandoc-default-reference.docx> <output.docx>
"""
import re
import sys
import zipfile

THEME = "word/theme/theme1.xml"
STYLES = "word/styles.xml"


def patch_theme(xml):
    # the FIRST <a:latin> inside majorFont / minorFont = heading / body font
    xml = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*(")',
                 r"\1Times New Roman\2", xml)
    xml = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*(")',
                 r"\1Times New Roman\2", xml)
    return xml


def patch_styles(xml):
    # force every explicit run colour to pure black (drop themeColor/themeTint
    # attributes so Word cannot re-tint headings)
    return re.sub(r"<w:color\b[^>]*/>", '<w:color w:val="000000"/>', xml)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with zipfile.ZipFile(src) as zin:
        infos = zin.infolist()
        blobs = {i.filename: zin.read(i.filename) for i in infos}

    if THEME in blobs:
        blobs[THEME] = patch_theme(blobs[THEME].decode("utf-8")).encode("utf-8")
    if STYLES in blobs:
        blobs[STYLES] = patch_styles(
            blobs[STYLES].decode("utf-8")).encode("utf-8")

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for i in infos:                      # preserve original member order
            zout.writestr(i, blobs[i.filename])


if __name__ == "__main__":
    main()
