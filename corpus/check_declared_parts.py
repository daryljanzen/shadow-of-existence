#!/usr/bin/env python3
"""check_declared_parts.py -- A ROW THAT DECLARES ITS PARTS MUST REPORT THEIR STATE.

** WHY.  Found twice in two revisions, on adjacent rows. **
  * ** `PO-2` (r2683) ** -- "held at do-not-assert on ** three separated levels **", the levels named in
    `GEOMETRY_PHYSICS_TAXONOMY` as "(1) skeleton grounded, (2) resemblance do-not-assert, (3)
    identification walled".  *** Four revisions of one session answered against them and NOT ONE was
    filed against a level. ***  Level (2) turned out PASSED.
  * ** `PO-6` (r2684) ** -- "this item's ** two halves ** are two halves rather than one entangled
    question".  *** Seven revisions in the row, none filed against a half. ***  Half one turned out
    FINISHED.

  ⇒ *** A row that declares a structure and never reports the structure's state reads as ONE open item.
      Both of these had a part silently completed, and both read as fully open until someone compared
      the notes to the declaration. ***

** WHAT THIS CHECKS. **  Every `PROTECTED_OPEN` row that DECLARES a decomposition -- "three levels", "two
halves", "four checks", "three routes" -- must also NAME the parts in the row, so a reader sees which
part a note answers.

  ⚠ ** It cannot check that the naming is CORRECT ** -- *** it checks that the row is self-describing,
      which is the property that was missing.  Whether half one is really finished is a reading. ***
  ⌗ ** `PO-7` and `PO-9` declare "four checks" and name them ** ⓵-⓸ ** in their kill receipts rather than
    in the row; that is accepted, because the receipt is where the checks live. **

    python3 corpus/check_declared_parts.py

Written r2684.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

DECLARES = re.compile(r'(three separated levels|three levels|two halves|four checks|three routes)', re.I)
NAMES = re.compile(r'\(1\)|\(2\)|⓵|⓶|HALF ONE|HALF TWO|level \(|check ⓵')


def main():
    print()
    print('  check_declared_parts -- does a row that declares its parts report their state?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    bad, n = [], 0
    for l in raw.split('\n'):
        m0 = re.match(r'\|\s*\*\*(PO-\d+)\*\*', l)
        if not m0:
            continue
        d = DECLARES.search(l)
        if not d:
            continue
        n += 1
        # ** a kill receipt is an accepted home for the parts: PO-7 and PO-9 name their four
        # checks there rather than in the row, and that is where the checks live. **
        if NAMES.search(l) or os.path.exists(os.path.join(ROOT, 'kills', m0.group(1) + '.md')):
            continue
        bad.append((m0.group(1), d.group(1)))

    print(f'  {n} row(s) declare a decomposition')
    if bad:
        print()
        for tag, what in bad:
            print(f'    [FAIL] {tag} declares "{what}" and never names the parts')
        print()
        print('    ⛔ ** A ROW THAT DECLARES A STRUCTURE AND NEVER REPORTS ITS STATE READS AS ONE OPEN')
        print('       ITEM. **  *** PO-2 and PO-6 each had a part silently COMPLETED and read as fully')
        print('       open until the notes were compared to the declaration. ***')
        return 1
    print('  every declaring row names its parts, or has a kill receipt that does.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
