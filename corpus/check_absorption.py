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
    """[(fork_rev, mainline_rev_or_0, date_str, raw_id)] newest last."""
    if not os.path.exists(REC):
        return None
    out = []
    for ln in open(REC, encoding='utf-8', errors='replace').read().split('\n'):
        # ** THE SECOND COLUMN MAY BE A MAIN-LINE REVISION *OR* A COMMIT SHA, AND r2441+c54.187 IS
        # WHY. **  Since r2429 absorptions happen BY MERGE, and the fork -- which cannot see the
        # observer line's revision numbering from its own tree -- knows only the SHA it was told.
        # ** A row recorded with a SHA is still a recorded absorption; refusing to parse it made the
        # file silently claim the fork had not advanced, which is the exact failure this gate
        # exists to prevent, one level down. **  The mainline number is 0 when unknown, so the
        # report can say so rather than invent one.
        m = re.match(r'\|\s*c54\.(\d+)\s*\|\s*(?:r(\d+)|([0-9a-f]{7,40}))\s*\|\s*([\d-]+)\s*\|', ln)
        if m:
            out.append((int(m.group(1)), int(m.group(2)) if m.group(2) else 0, m.group(4),
                        ('r' + m.group(2)) if m.group(2) else m.group(3)))
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
    for f, m, d, raw in rows:
        print(f'    c54.{f:<5} absorbed at {raw}  ({d})')
    print()
    newest_absorbed = rows[-1][0]
    front = tree_front()
    # ** IN-FLIGHT, AND r2441+c54.186 IS WHY. **  This gate's inference -- "a fork revision in the
    # documents newer than the newest absorption means an absorption happened and was never
    # recorded" -- is sound on the OBSERVER's tree and false on the FORK's.  Since r2407 both lines
    # work in the same repository, so the fork writing its own revision into its own documents trips
    # a gate that then reports the fork's normal condition as a broken record.  ** The exemption is
    # DECLARED and not inferred, which is this file's whole philosophy: the fork names the revision
    # it is cutting and the node clears the line when it absorbs. **  A revision that is neither
    # absorbed nor declared in flight still FAILS, so the gate keeps its teeth.
    inflight = set()
    # ** ANCHORED TO LINE START, and that is not pedantry: unanchored, the paragraph ABOVE the record
    # explaining what `IN-FLIGHT:` is -- which names c54.186 as the example -- satisfied the marker by
    # itself, so the gate passed on a tree that had declared nothing.  Caught by seeding the defect
    # rather than by reading the fix. **
    _m = re.search(r'^IN-FLIGHT:([^\n]*)', open(REC, encoding='utf-8').read(), re.M)
    if _m:
        inflight = {int(x) for x in re.findall(r'c54\.(\d+)', _m.group(1))}
    if inflight:
        print('  declared IN FLIGHT (cut by the fork, not yet absorbed): '
              + ', '.join('c54.%d' % n for n in sorted(inflight)))
    if front > newest_absorbed and front not in inflight:
        print(f'  [FAIL] the tree names c54.{front} but the newest recorded absorption is '
              f'c54.{newest_absorbed}, and c54.{front} is not declared in flight.')
        print('     ** An absorption happened and was never recorded **, which is the one thing this')
        print('     gate can prove.  Add the row; the record is the only thing that moves.')
        print('     *If instead this tree is the FORK and that is its own revision in progress,')
        print('      declare it on the `IN-FLIGHT:` line in ABSORPTION.md -- declared, not inferred.*')
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
