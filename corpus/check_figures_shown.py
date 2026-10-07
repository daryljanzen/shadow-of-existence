#!/usr/bin/env python3
"""check_figures_shown.py -- A CAPTION IS NOT A FIGURE.

** WHAT THIS CATCHES, AND IT HAD SHIPPED ON THE PUBLIC SITE. **  A figure reaches a
generated page as a picture plus a caption.  When the generator cannot produce the
picture it emitted the caption anyway, so the page read `Figure 3.` followed by several
sentences describing a diagram ** that was not on the page at all **.  Nothing failed;
the page was well-formed, the caption was correct, and the only instrument that could
notice was a person scrolling past it.  Found at r7207 by exactly that, on a phone.

Two distinct causes, both silent:
  - a figure drawn as a `tikzpicture`, which has no `\\includegraphics` for the
    generator to carry across -- two in `P7`;
  - an `\\includegraphics` of a PDF with no raster beside it, which cannot be an `<img>`
    and degraded to a link -- two in `P15`.

** WHAT IS CHECKED. **  Every `<figure>` on every generated paper page carries an `<img>`,
and every `src` it names exists on disk.  * A dangling `src` is the same defect wearing
a valid element: the markup is right and the reader still sees nothing. *

⛭ SEEDED ON THE SHIPPED STATE, in a worktree at the commit this was written against:
** all four flagged -- `fig:acoustic` and `fig:acoustic-nofit` in `P15`, `fig:cr-gr-venn`
and `fig:dependency-structure` in `P7`. **  So the gate is known to fire on the defect it
was built for, and not only to pass once the defect is cleared.

⌗ The remedy is to produce the picture -- `scripts/render_tikz.py` for a drawing, a
raster beside the PDF for a plot -- never to drop the caption.  A figure the paper
refers to by number has to be on the page the number is on.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
PAGES = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave')

FIG = re.compile(r'<figure[^>]*>.*?</figure>', re.S)
IMG = re.compile(r'<img[^>]*src="([^"]+)"')
AID = re.compile(r'id="([^"]+)"')

#: Where a page's `./fig/...` resolves on disk.  The deploy copies `corpus/*.png` and
#: `BOOK_INTRO_cosmiCave/fig/*.svg` into one served directory, so both are searched.
ROOTS = (os.path.join(PAGES, 'fig'), os.path.join(ROOT, 'corpus'))


def resolve(src):
    rel = src.split('?')[0]
    if rel.startswith('./'):
        rel = rel[2:]
    if rel.startswith('fig/'):
        rel = rel[4:]
    for base in ROOTS:
        if os.path.exists(os.path.join(base, rel)):
            return True
    return False


def main():
    print()
    print('  FIGURES SHOWN -- does every caption have its picture?')
    pages = sorted(f for f in os.listdir(PAGES)
                   if f.startswith('paper_P') and f.endswith('.html'))
    if not pages:
        print('  ⛔ no generated paper pages found')
        return 1

    nofig, dangling, total = [], [], 0
    for fn in pages:
        s = io.open(os.path.join(PAGES, fn), encoding='utf-8').read()
        for block in FIG.finditer(s):
            total += 1
            b = block.group(0)
            aid = AID.search(b)
            where = f'{fn}  {aid.group(1) if aid else "(unlabelled)"}'
            m = IMG.search(b)
            if not m:
                nofig.append(where)
            elif not resolve(m.group(1)):
                dangling.append(f'{where}  src={m.group(1)}')

    if nofig:
        print(f'  ⛔ {len(nofig)} CAPTION(S) WITH NO PICTURE:')
        for w in nofig:
            print(f'    [FAIL] {w}')
    if dangling:
        print(f'  ⛔ {len(dangling)} FIGURE(S) WHOSE IMAGE IS NOT ON DISK:')
        for w in dangling:
            print(f'    [FAIL] {w}')
    if nofig or dangling:
        print('     ⌗ PRODUCE THE PICTURE, do not drop the caption.  A tikzpicture is')
        print('       rendered by scripts/render_tikz.py; a PDF plot needs a raster')
        print('       beside it in corpus/.  A figure the prose cites by number has to')
        print('       be on the page that number is on.')
        print()
        return 1

    print(f'  {total} figure(s) across {len(pages)} page(s); every one carries an image '
          f'that is on disk.')
    print('  ⌗ This says the picture is THERE, not that it is the right picture --')
    print('    which is what an unread figure is, and PO-78 carries that count.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
