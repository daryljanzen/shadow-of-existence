#!/usr/bin/env python3
"""check_absorption.py -- the NINETEENTH gate: how long since the working fork was absorbed?

** THE GAP THIS CLOSES IS THE ONE NO OTHER GATE CAN SEE, AND IT IS SELF-REFERENTIAL. **

Every currency measurement in this tree is taken against "the fork front", and the fork front is
read out of THIS TREE'S OWN DOCUMENTS.  So if the working fork advances twenty revisions and nothing
is absorbed, the front does not move, every document still measures as current, and

    ** the tree reports itself perfectly up to date with respect to a number it wrote itself. **

That is the r2377 defect one level up.  `check_currency` used to read the fork front from a document
frozen at c54.35, so the baseline sank with the documents it measured and every register looked
current while the map was 76 revisions behind.  Fixed there by taking the max over all fork-carrying
documents -- which is still, unavoidably, a maximum over OUR OWN FILES.

** SO ABSORPTION IS DECLARED, NOT INFERRED. **  `ABSORPTION.md` records, per absorption: the fork
revision absorbed, the main-line revision that did it, and the date.  This gate reads that file and
reports the elapsed distance.  It cannot be satisfied by writing prose, because the only thing that
moves it is an absorption actually happening.

WHAT IT DOES AND DOES NOT FAIL ON.  It cannot know the fork's true front -- only a bundle tells us
that -- so it never fails for being behind: ** being behind the fork is the normal condition of an
observer line, not a defect. **  It FAILS only when the record itself is broken: absent, unparseable,
or contradicted by the tree (a fork revision in the documents that is NEWER than the newest recorded
absorption, which means an absorption happened and was never recorded).  Everything else is a
REPORT, so that the elapsed distance is in front of whoever reads the suite.

    python3 corpus/check_absorption.py

Written r2386, at Daryl's standing reminder that the fork's progress wants periodic absorption.
Stated for reversal.
"""
import os, re, sys, glob
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REC = os.path.join(ROOT, 'ABSORPTION.md')

# how many fork revisions may elapse before the report says "ask for a bundle"
WINDOW = 15


def recorded():
    """[(fork_rev, mainline_rev, date_str)] newest last."""
    if not os.path.exists(REC):
        return None
    out = []
    for ln in open(REC, encoding='utf-8', errors='replace').read().split('\n'):
        m = re.match(r'\|\s*c54\.(\d+)\s*\|\s*r(\d+)\s*\|\s*([\d-]+)\s*\|', ln)
        if m:
            out.append((int(m.group(1)), int(m.group(2)), m.group(3)))
    return sorted(out)


def tree_front():
    """The highest c54 revision any document in this tree names."""
    best = 0
    for p in glob.glob(os.path.join(ROOT, '*.md')) + glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        t = open(p, encoding='utf-8', errors='replace').read()
        for x in re.findall(r'c54\.(\d+)', t):
            best = max(best, int(x))
    return best


def main():
    rows = recorded()
    print()
    print('  ABSORPTION -- how long since the working fork was absorbed?')
    print()
    if rows is None:
        print('  [FAIL] ABSORPTION.md is missing.  The absorption record is DECLARED, not inferred:')
        print('     no other gate can see that the fork has advanced, because every currency')
        print('     measurement in this tree is taken against a front this tree wrote itself.')
        return 1
    if not rows:
        print('  [FAIL] ABSORPTION.md carries no parseable rows (| c54.N | rNNNN | YYYY-MM-DD |).')
        return 1

    print(f'  {len(rows)} absorption(s) recorded:')
    for f, m, d in rows:
        print(f'    c54.{f:<5} absorbed at r{m}  ({d})')
    print()
    newest_absorbed = rows[-1][0]
    front = tree_front()
    if front > newest_absorbed:
        print(f'  [FAIL] the tree names c54.{front} but the newest recorded absorption is '
              f'c54.{newest_absorbed}.')
        print('     ** An absorption happened and was never recorded **, which is the one thing this')
        print('     gate can prove.  Add the row; the record is the only thing that moves.')
        return 1

    print(f'  Newest absorbed: c54.{newest_absorbed}.  The tree names nothing newer, which is')
    print('  consistent -- and consistent is all it can be: only a bundle reveals the fork\'s')
    print('  true front.')
    print()
    print('  ** BEING BEHIND THE FORK IS THE NORMAL CONDITION OF AN OBSERVER LINE, not a defect. **')
    print('     So this gate does not fail for distance.  What it does is keep the distance in')
    print('     front of whoever runs the suite, because the failure mode is not falling behind --')
    print('     it is falling behind WITHOUT NOTICING, while every other gate reports green')
    print('     against a front we wrote ourselves.')
    if len(rows) >= 2:
        span = rows[-1][0] - rows[-2][0]
        print()
        print(f'  Last span: c54.{rows[-2][0]} -> c54.{rows[-1][0]} ({span} fork revisions).')
        if span > WINDOW:
            print(f'     [REPORT] that span exceeded the {WINDOW}-revision window.  A longer span is')
            print('     a bigger three-way merge and a longer trail audit -- the r2385 absorption of')
            print('     19 revisions lost three annotations and needed 7 real file merges.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
