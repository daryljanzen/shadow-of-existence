#!/usr/bin/env python3
"""check_floats_carried.py -- A FLOAT THE SOURCE HAS AND THE PAGE DOES NOT.

** WHY THIS IS NOT check_figures_shown. **  That gate asks whether every figure ON a
page carries its picture.  It cannot see a figure that never reached the page at all,
because it counts what is there -- and at r7207 it passed, green, over a page that was
missing its paper's hallmark figure entirely.

** WHAT HAPPENED. **  `P7`'s six-panel synthesis figure is written `\\begin{figure*}`, the
starred full-width form.  The generator matched `\\begin{figure}` and nothing else, so
the whole float -- picture, caption, label and all -- was dropped silently; the page did
not say `Figure 1.` and then show nothing, it simply had no Figure 1.  Separately the
generator had ** no table handler at all **, so four tables across the corpus, `P7`'s
dependency matrix and ledger block among them, were absent from their pages while
rendering correctly in the PDF.  The framework paper's own prose sends a reader to that
matrix, so on the page it sent them to nothing.

** WHAT IS CHECKED, and it is a count rather than a rendering. **  For each paper, the
number of `figure`/`figure*` and `table`/`table*` environments in the source against the
number of `<figure>` and `<table>` elements on its page.  * A count is the only thing
that can see an absence; every richer check needs the element to exist before it can
examine it. *

⛭ SEEDED, in a worktree at the commit this was written against, and it reported exactly
that: ** `P7: source has 5 figure float(s), page has 4`, `P7: source has 2 table
float(s), page has 0`, `P18: source has 2 table float(s), page has 0`. **

⚠ WHAT IT CANNOT SEE: a float carried to the page in the WRONG PLACE, and a float whose
content is wrong.  Counting establishes presence and nothing else.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
CORPUS = os.path.join(ROOT, 'corpus')
PAGES = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave')

#: The paper -> source-stem map is READ FROM THE GENERATOR rather than copied here.
#: r7209: it was copied first, and the copy had `P1` wrong within the hour -- the gate
#: then silently checked seventeen papers and reported success on eighteen.  * A second
#: copy of a mapping is a second thing to keep right, and this tree has a row about
#: exactly that. *
def _papers():
    import importlib.util as u
    p = os.path.join(ROOT, 'scripts', 'gen_paper_html.py')
    spec = u.spec_from_file_location('_gph', p)
    mod = u.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {k: v[0] for k, v in mod.PAPERS.items()}


SRC_FIG = re.compile(r'\\begin\{figure\*?\}')
SRC_TAB = re.compile(r'\\begin\{table\*?\}')


def main():
    print()
    print('  FLOATS CARRIED -- is every float in the source on its page?')
    bad, checked = [], 0
    papers = _papers()
    for pid, stem in sorted(papers.items(), key=lambda kv: int(kv[0][1:])):
        src_p = os.path.join(CORPUS, stem + '.tex')
        pg_p = os.path.join(PAGES, f'paper_{pid}.html')
        if not os.path.exists(src_p) or not os.path.exists(pg_p):
            continue
        checked += 1
        src = io.open(src_p, encoding='utf-8').read()
        # Comment lines cannot contribute a float.
        src = re.sub(r'(?m)(?<!\\)%.*$', '', src)
        pg = io.open(pg_p, encoding='utf-8').read()
        sf, st_ = len(SRC_FIG.findall(src)), len(SRC_TAB.findall(src))
        pf = len(re.findall(r'<figure[\s>]', pg))
        pt = len(re.findall(r'<table[\s>]', pg)) - len(re.findall(r'<table>', pg))
        # A bare `<table>` with no attributes is the math converter's rendering of a
        # tabular inside a formula, not a float; floats carry an id or sit in a wrap.
        pt = len(re.findall(r'<div class="tablewrap">', pg))
        if sf != pf:
            bad.append(f'{pid}: source has {sf} figure float(s), page has {pf}')
        if st_ != pt:
            bad.append(f'{pid}: source has {st_} table float(s), page has {pt}')

    if bad:
        print(f'  ⛔ {len(bad)} FLOAT COUNT MISMATCH(ES):')
        for b in bad:
            print(f'    [FAIL] {b}')
        print('     ⌗ A float missing from the page is not a rendering defect, it is an')
        print('       ABSENCE -- nothing on the page is wrong, and the thing the prose')
        print('       cites is not there.  Teach the generator the environment; do not')
        print('       adjust the count.')
        print()
        return 1

    print(f'  {checked} paper(s); every figure and table float in the source is on '
          f'its page.')
    print('  ⌗ Presence is what a count establishes.  Whether a float is in the RIGHT')
    print('    PLACE, and whether its content is right, are read by a person.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
