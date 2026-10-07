#!/usr/bin/env python3
"""check_pages_render.py -- NOTHING ON A GENERATED PAGE MAY RENDER AS NOTHING.

** WHAT THIS CATCHES, AND IT HAD BEEN LIVE ON THE PUBLIC SITE ACROSS EVERY PAPER. **  The
pages are generated from the corpus, and the corpus is gated to the hilt -- so every gate
was green while the artefact the public actually reads was wrong.  * A generated
document is downstream of every instrument in the tree and is checked by none of them. *

Two renderings that produced nothing, found at r7207 by a person scrolling a page on a
phone:
  - ** 1,378 inline math spans across all eighteen papers were EMPTY. **  The converter
    was handed `\\M` for a source `$M$`, because the backslash was prepended whether or
    not the source had one; an unknown control sequence renders as nothing.  Every bare
    alphabetic variable in inline math was dropped, so a sentence reached the site as
    "whose Kretschmann in the faller's own proper time is -free".
  - ** An empty list item **, from LaTeX comments sitting between `\\begin{enumerate}`
    and the first `\\item`.  Not cosmetic: item labels are numbered from the source, so
    the spurious item shifted every cross-reference by one and the prose's "item 2"
    landed the reader on item 1.

** WHY A STRUCTURAL CHECK RATHER THAN A SPELLING ONE. **  Neither defect is a wrong
value; both are an element that is present, well-formed and EMPTY.  Nothing downstream
can tell an empty span from a span whose content happens to be short, so the check is on
emptiness itself: an element the generator emitted to carry content must carry some.

⛭ SEEDED, in a worktree at the commit this was written against: ** 1,378 empty math
spans and 1 empty list item, across eighteen pages. **  The gate is known to fire on the
defect it was built for.

⚠ WHAT IT CANNOT SEE: a span that renders the WRONG symbol rather than none.  `\\M`
rendered as nothing and was findable; a `\\Theta` silently rendered as a theta of the
wrong case would pass here.  * Emptiness is the half that is mechanically decidable. *
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, '..', 'BOOK_INTRO_cosmiCave')

#: Elements the generator emits in order to carry content.  An empty one is a dropped
#: something, every time -- there is no case where the generator means to emit a blank.
EMPTY = (
    ('math span', re.compile(r'<span class="m">\s*</span>')),
    ('list item', re.compile(r'<li>\s*</li>')),
    ('display equation', re.compile(r'<div class="eq">\s*</div>')),
    ('caption', re.compile(r'<figcaption>\s*</figcaption>')),
)


def main():
    print()
    print('  PAGE RENDER -- does anything on a generated page render as nothing?')
    pages = sorted(f for f in os.listdir(PAGES)
                   if f.startswith('paper_P') and f.endswith('.html'))
    extra = [f for f in ('explainer.html', 'introduction.html')
             if os.path.exists(os.path.join(PAGES, f))]
    if not pages:
        print('  ⛔ no generated paper pages found')
        return 1

    hits = {}
    for fn in pages + extra:
        s = io.open(os.path.join(PAGES, fn), encoding='utf-8').read()
        for name, rx in EMPTY:
            n = len(rx.findall(s))
            if n:
                hits.setdefault(name, []).append((fn, n))

    if hits:
        total = sum(n for v in hits.values() for _, n in v)
        print(f'  ⛔ {total} EMPTY ELEMENT(S) -- content the generator dropped:')
        for name, rows in sorted(hits.items()):
            print(f'    {name}:')
            for fn, n in rows:
                print(f'      [FAIL] {fn}  x{n}')
        print('     ⌗ An empty element is a dropped something.  Find what the source has')
        print('       there and why the converter returned nothing for it -- an unknown')
        print('       control sequence renders as nothing and reports no error.')
        print()
        return 1

    print(f'  {len(pages) + len(extra)} generated page(s); nothing renders as nothing.')
    print('  ⌗ Emptiness is the mechanically decidable half.  A span that renders the')
    print('    WRONG symbol still passes here, and is read by a person.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
