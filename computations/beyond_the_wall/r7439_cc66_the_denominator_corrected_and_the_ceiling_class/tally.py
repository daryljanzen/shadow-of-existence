#!/usr/bin/env python3
"""r7439 — THE REGISTER'S OWN TALLY, READ FROM ITS CELLS, with a RUNNING TOTAL.

** WHY THIS EXISTS. **  `.80` reported `78` refusal sites and `19` distinct sources.  Both were wrong: the
hand sum stopped one row short of the table's end, dropping `red_carry`'s `3`, and the source count included
the shared row.  **The running total below is printed precisely so that the place a sum goes wrong is
visible** -- it reaches `78` after `check_view_tables` and `81` after `red_carry`, which is exactly the error.

⛭ r7441 ① -- A SECOND MISS, IN THIS FILE, FOUND BY USING IT.  The grade counters were
`len(re.findall('SELF-REFERENTIAL', cell))` -- occurrences of the PHRASE, one per branch by convention.
A cell written "⌗ 2 SELF-REFERENTIAL, now a PAIR" names TWO branches and says the phrase ONCE, so it
counted 1 and `check_pin_board` read 2 of 3 instead of 3 of 3.  **A counter that depends on how a
sentence is spelled is the same defect as the hand sum it replaced**, so it is fixed here rather than
worked around in the cell: an explicit leading integer is read when present (`2 SELF-REFERENTIAL`), and
a bare phrase still counts 1.  The miss is recorded instead of quietly repaired, by the same rule that
put sites.py's missed `bad = True` idiom in its own source.

⚠ r7441 ⑨ -- THE RESIDUAL, STATED RATHER THAN HIDDEN.  The counter above reads an explicit leading
integer, which fixes the "2 SELF-REFERENTIAL" miss.  It does NOT fix the deeper shape: the count still
comes out of PROSE, so a cell that merely MENTIONS a grade by name inflates it.  That happened at once --
check_revision_collisions' new cell said "its printed address is SELF-REFERENTIAL" as a description and
the row read 3 self-referential branches instead of 1.  I worked around it in the CELL (the prose no longer
spells the grade) because the robust fix is a DEDICATED COLUMN for the per-grade counts, and the register's
shape is 66's call, not this seat's -- the same place r7429's per-direction question was left.
** Until that is ruled, a cell must spell a grade name ONLY where it is counting a branch. **

    python3 tally.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.abspath(os.path.join(HERE, '..', 'r7419_cc66_the_register_of_keys', 'register.tsv'))


def graded(cell, phrase):
    """how many branches a cell puts under `phrase` -- an explicit leading count wins over an occurrence count

    r7441 ①: `2 SELF-REFERENTIAL` means two branches in one sentence; a bare `SELF-REFERENTIAL` means one.
    Counting occurrences alone undercounts the first, which is how check_pin_board read 2 of 3.
    """
    numbered = [int(n) for n in re.findall(r'(\d+)\s+' + re.escape(phrase), cell)]
    unnumbered = len([m for m in re.finditer(re.escape(phrase), cell)
                      if not re.search(r'\d+\s+$', cell[:m.start()])])
    return sum(numbered) + unnumbered


def main():
    rows, run = [], 0
    for line in open(REG, encoding='utf-8'):
        f = line.rstrip('\n').split('\t')
        if len(f) != 8 or f[0].startswith('#'):
            continue
        m = re.search(r'\((\d+) of (\d+) refusal sites walked', f[7])
        shared = 'SAME SOURCE' in f[7]
        rows.append((f[0], m and (int(m.group(1)), int(m.group(2))), shared,
                     graded(f[7], 'SELF-REFERENTIAL'), graded(f[7], 'ONE STEP FROM A WALL')))
    print('  instrument                            walked  self-ref  one-step   of  running')
    w = s = sr = osw = 0
    for name, v, shared, n_sr, n_os in rows:
        if v is None:
            print(f'  {name:<36}      --  nothing refuses on this key')
            continue
        if shared:
            print(f'  {name:<36} {v[0]:>6} {n_sr:>9} {n_os:>9} {v[1]:>4}   (shared source -- not added)')
            continue
        w += v[0]; s += v[1]; sr += n_sr; osw += n_os; run += v[1]
        print(f'  {name:<36} {v[0]:>6} {n_sr:>9} {n_os:>9} {v[1]:>4} {run:>8}')
    print(f'\n  {len([r for r in rows if r[1] and not r[2]])} distinct sources, {s} refusal sites')
    print(f'  {w} walked, {sr} self-referential, {s - w - sr} pending   ({w / s:.1%} walked)')
    print(f'  {osw} cell(s) carry the ONE STEP FROM A WALL grade')
    full = [n for n, v, sh, a, b in rows if v and not sh and v[0] + a == v[1]]
    print(f'  fully accounted: {len(full)} -> {", ".join(full)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
