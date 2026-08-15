#!/usr/bin/env python3
"""check_cross_row_dupes.py -- A FINDING BELONGS IN ONE ROW, NOT COPIED INTO EVERY ROW IT TOUCHES.

** WHY.  r2832. **  *** Working an arc that bears on two rows, this line wrote the SAME BLOCKS into
both.  Measured: ** `PO-2` carried 10,878 bytes verbatim from `PO-5` ** (the colour-route arc,
r2810-r2823) and ** `PO-7` carried 8,875 from `PO-10` ** (the acoustic-diagnosis arc, r2781-r2807).
Nearly twenty thousand bytes of the register were one text stored twice. ***

  ⇒ *** And it is worse than waste: ** when the finding is later corrected, the correction lands in one
      copy. **  That is exactly the defect `check_withdrawals_propagate` was built for at the same
      revision -- ** the duplication is what MAKES the propagation failure possible. ** ***

** THE RULE THIS ENFORCES. **  *** A finding lives in the row whose OBJECT it bears on.  Other rows
carry a POINTER, never a copy. ***

** WHAT THIS CHECKS. **  For every pair of rows, any block over 250 characters that is more than 85%
similar to a block in the other row.

  ⌗ ** Similarity, not equality ** -- *** the byte-exact check that ran first missed both of these,
    because an edit to one copy makes them merely near-identical while leaving the defect intact. ***

    python3 corpus/check_cross_row_dupes.py

Written r2832.  Stated for reversal.
"""
import difflib
import itertools
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
SPLIT = r'(?=⛭⛭⛭|⛔⛭⛭|⛔⛔)'
MIN = 250
SIM = 0.85
BUDGET = 800   # ** bytes of overlap tolerated before it is a copy rather than a coincidence **


def main():
    print()
    print('  check_cross_row_dupes -- is any finding stored in two rows?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    rows = {}
    for l in raw.split('\n'):
        m = ROW.match(l)
        if not m:
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', l)[1:-1]]
        if len(cells) > 4:
            rows[m.group(2)] = [b for b in re.split(SPLIT, cells[4]) if len(b.strip()) > MIN]

    bad = []
    for a, b in itertools.combinations(rows, 2):
        n = 0
        for x in rows[a]:
            if max((difflib.SequenceMatcher(None, x, y).ratio() for y in rows[b]), default=0) > SIM:
                n += len(x)
        if n > BUDGET:
            bad.append((a, b, n))

    print(f'  {len(rows)} row(s), {len(list(itertools.combinations(rows, 2)))} pairs compared')
    if bad:
        print()
        for a, b, n in sorted(bad, key=lambda t: -t[2]):
            print(f'    [FAIL] {a} and {b} share {n:,} bytes of near-identical blocks')
        print()
        print('    ⛭ ** A finding lives in the row whose OBJECT it bears on; other rows carry a')
        print('       POINTER, never a copy. *** And the copy is what makes a later correction land')
        print('       in one row and not the other. ***')
        return 1

    print('  no finding is stored in two rows.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
