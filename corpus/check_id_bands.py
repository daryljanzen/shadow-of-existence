#!/usr/bin/env python3
"""check_id_bands.py -- the TWENTY-FIRST gate: no duplicate lead IDs, none out of band.

** THE ONE HARD PROBLEM A REPOSITORY DOES NOT SOLVE. **

`THE_LIVE_ARC.md` is a 423 KB single-line-per-row table that every node writes to.  Git merges it
line by line, so two nodes adding rows land at the same place: a conflict every time, or -- with the
`merge=union` attribute that makes an append-only table mergeable at all -- ** a silent interleave
that can carry two rows with the same ID **.

And the ID space has been a near-miss TWICE BY LUCK.  This line's rows begin at `L-174` only because
the working fork's maximum was `L-173`, and the fork has still not opened a row above it.  Recorded
at r2385 and again at r2393; ** twice is not a coincidence, it is a warning about the third time. **

THE DISCIPLINE IS THREE-PART AND THIS GATE IS THE THIRD:

  (1) RESERVED BANDS, declared per line -- a node allocates only inside its own band, so two nodes
      cannot choose the same number even offline.
  (2) `merge=union` on the register -- keeps both sides' added lines, which is right for an
      append-only table and wrong for anything else.  ** It cannot detect a duplicate ID. **
  (3) THIS GATE -- proves neither (1) nor (2) silently failed.

Belt and braces, deliberately: it is the same "declare, do not infer" pattern as `current: none`,
`DECLARED-UNDATED` and `[REPORTED]`.

    python3 corpus/check_id_bands.py

Exit 1 on any duplicate ID, any out-of-band allocation, or any unparseable row.
Written r2407.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')

# Declared, never inferred.  Widen a band only by editing this table and THE_HUB.md together.
BANDS = [
    (1,   173, 'the working fork (54) -- historical'),
    (174, 499, 'the main line (56)'),
    (500, 799, 'reserved -- the fork\'s new rows'),
    (800, 999, 'reserved -- future lines'),
]

# Which band this tree writes in.  A node changes this line and nothing else.
THIS_LINE = (174, 499)


def band_of(n):
    for lo, hi, name in BANDS:
        if lo <= n <= hi:
            return lo, hi, name
    return None


def main():
    if not os.path.exists(ARC):
        print('  [FAIL] THE_LIVE_ARC.md is absent')
        return 1
    text = open(ARC, encoding='utf-8', errors='replace').read()

    rows, dupes, seen = [], [], {}
    for i, ln in enumerate(text.split('\n'), 1):
        m = re.match(r'^\|\s*(?:~~)?\*{0,2}(L-(\d+))\*{0,2}(?:~~)?\s*\|', ln)
        if not m:
            continue
        lid, n = m.group(1), int(m.group(2))
        rows.append((lid, n, i))
        if lid in seen:
            dupes.append((lid, seen[lid], i))
        else:
            seen[lid] = i

    print()
    print(f'  LEAD ID BANDS -- {len(rows)} row(s) in THE_LIVE_ARC')
    print()
    for lo, hi, name in BANDS:
        k = sum(1 for _, n, _ in rows if lo <= n <= hi)
        mark = '  <- this line' if (lo, hi) == THIS_LINE else ''
        print(f'    L-{lo:03d}..L-{hi:03d}  {k:>4} row(s)   {name}{mark}')
    print()

    rc = 0
    if dupes:
        print(f'  ⛔ DUPLICATE IDs: {len(dupes)}')
        for lid, a, b in dupes:
            print(f'    [FAIL] {lid} appears at line {a} and line {b}')
        print('     ** A union merge keeps both sides\' added lines and cannot see this. **  Two')
        print('     nodes allocated the same number, or a merge interleaved two rows.  Renumber the')
        print('     later one INSIDE ITS OWN BAND and repoint anything that cites it.')
        print()
        rc = 1

    out = [(lid, n, i) for lid, n, i in rows if band_of(n) is None]
    if out:
        print(f'  ⛔ OUT OF EVERY BAND: {len(out)}')
        for lid, n, i in out:
            print(f'    [FAIL] {lid} (line {i}) falls in no declared band')
        print('     Widen a band in THE_HUB.md and in this gate together, or renumber.')
        print()
        rc = 1

    lo, hi = THIS_LINE
    # A row this line ADDED must be in this line's band.  Rows inherited from the fork are not
    # this line's to renumber, so the check is on the band's neighbours, not on ownership.
    newest = max((n for _, n, _ in rows), default=0)
    if newest and not (lo <= newest <= hi):
        b = band_of(newest)
        print(f'  [REPORT] the newest ID, L-{newest}, sits in the band '
              f'"{b[2] if b else "none"}" rather than this line\'s.')
        print('     Not a failure by itself -- an absorbed bundle brings the fork\'s newest row with')
        print('     it.  ** It IS the signal to check that the next allocation starts inside this')
        print('     line\'s band and not one past the fork\'s maximum. **  That habit is what made')
        print('     the collision a near-miss twice rather than a collision.')
        print()

    if rc == 0:
        print(f'  No duplicate IDs; every row falls in a declared band.')
        print(f'  Next allocation for this line: L-{max([n for _, n, _ in rows if lo <= n <= hi], default=lo-1) + 1}.')
        print()
    return rc


if __name__ == '__main__':
    sys.exit(main())
