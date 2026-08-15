#!/usr/bin/env python3
"""check_arc_columns.py -- THE_LIVE_ARC's TABLES MUST EACH HOLD THEIR OWN COLUMN COUNT.

** WHY.  cc54, c54.222, routed to this line deliberately: ** *** "`THE_LIVE_ARC.md` has no column lint,
and ** 106 of its 314 rows are off the modal shape **.  I repaired the one that was mine and handed
them the number." ***

** ⓵ THE FINDING HOLDS AND THE INSTRUMENT OVERCOUNTED. **  *** A single global mode is the wrong test
for this file: it holds ** eleven distinct tables **, and `| finding | where | disposal |` is a
three-column table with its own header, not a broken row of a six-column one.  Measured per-table:
** 98 genuine breaks, against 137 by a global mode ** -- the 39-row difference is tables of different
widths counted as defects. ***

  ⌗ ** cc54's number is real and its interpretation would have been wrong ** -- *** which is why the
    handoff was the right call and the repair was not.  A node repairing 137 rows would have flattened
    three tables into one shape. ***

** ⛭⛭ ⓶ AND THIS GATE EXISTS BECAUSE MY OWN HAD THE SAME DEFECT c54.222 FOUND IN THEIRS. **  *** Their
INDEX lint sat INSIDE the membership filter, so rows the filter dropped were linted by nobody.
`check_register_columns` had no filter -- but its SELECTOR was narrower than its table: `PO-\\d+` missed
`PO-1a`--`PO-1d` entirely, eight rows lint-free.  ** A narrow selector is a filter wearing a different
name. ** ***

** WHAT THIS CHECKS. **  Each contiguous table block in `THE_LIVE_ARC.md` is read separately; every row
must carry its OWN table's modal raw-pipe count.

  ⚠ ** REPORT-ONLY. **  *** 98 breaks predate this gate and repairing them blind would mean guessing
    which cell each stray `|` belonged to.  ** New breaks are what this catches ** -- it reports the
    count so a rise is visible, and the backlog is filed as owed. ***

    python3 corpus/check_arc_columns.py

Written r2783.  Stated for reversal.
"""
import collections
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')

RAW = re.compile(r'(?<!\\)\|')
# ** r2802: 98 -> 33.  *** 65 of the 98 were over-piped -- unescaped bars, fixed by ESCAPING,
# which needs no knowledge of which cell they belonged to (159,248 words before and after).
# The claim that they were "not blind-repairable" was made without testing it. ***  The
# remaining 33 are UNDER-piped: genuinely short rows, a different thing from a break. **
BASELINE = 33


def blocks(lines):
    """contiguous runs of table rows -- each is its own table with its own width"""
    out, cur = [], []
    for i, l in enumerate(lines):
        if l.startswith('|') and l.count('|') > 2:
            cur.append((i, l))
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def main():
    print()
    print("  check_arc_columns -- does each of THE_LIVE_ARC's tables hold its own shape?")
    print()
    if not os.path.exists(ARC):
        print('  [FAIL] THE_LIVE_ARC.md is missing')
        return 1

    lines = open(ARC, encoding='utf-8', errors='replace').read().split('\n')
    bs = blocks(lines)
    total, off = 0, []
    for b in bs:
        c = collections.Counter(len(RAW.findall(l)) for _, l in b)
        mode = c.most_common(1)[0][0]
        total += len(b)
        for i, l in b:
            if len(RAW.findall(l)) != mode:
                off.append((i+1, len(RAW.findall(l)), mode))

    print(f'  {len(bs)} table(s), {total} row(s) · {len(off)} off their own table\'s shape')
    print(f'  baseline at r2783: {BASELINE}')
    if len(off) > BASELINE:
        print()
        print(f'    [FAIL] {len(off) - BASELINE} NEW break(s) since the baseline')
        for ln, n, m in off[:6]:
            print(f'      line {ln}: {n} raw pipes, its table\'s mode is {m}')
        print()
        print('    ⛭ ** An unescaped `|` inside a cell is a cell boundary to markdown. **  *** Escape')
        print('       it as `\\|` or write `\\vert`. ***')
        return 1
    print('  no new breaks.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
