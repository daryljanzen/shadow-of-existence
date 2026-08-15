#!/usr/bin/env python3
"""check_rows_name_the_open.py -- EVERY OPEN ROW'S HEAD MUST NAME WHAT IS OPEN.

** WHY.  r2835. **  *** Measuring every gate's COVERAGE (after one was found checking 1 citation out of
68) surfaced a different thing entirely: ** `OWED` holds ONE item while TEN rows are open **.  Reading
the rows, ** five of the ten named nothing that is open ** -- they stated what had been settled and
stopped. ***

  ⇒ *** So the register said what is KNOWN and not what is LEFT.  ** A reader could learn everything
      established about `PO-1b` and still not know that a kill was written, retracted, and nothing
      worked since ** -- which is the whole of its state. ***

** WHAT THIS CHECKS. **  *** Every OPEN row's `▣ CURRENT STATE` head contains a statement of what is
open: a "WHAT IS OPEN" / "LIVE REMAINDER" / "THE LIVE QUESTION" clause, or an explicit "gated on
`PO-n`". ***

  ⌗ ** A gated row satisfies this by naming its gate ** -- *** "nothing can be done here until `PO-11`
    moves" is a complete statement of what is open, and forcing more would manufacture work. ***

** ⛭ AND THE COVERAGE LESSON THAT FOUND IT IS BAKED INTO THE OUTPUT: **  *** this gate prints the
denominator, not just the count -- what it COULD have checked beside what it did. ***

    python3 corpus/check_rows_name_the_open.py

Written r2835.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

OPEN_CLAUSE = re.compile(
    r'WHAT IS OPEN|LIVE REMAINDER|THE LIVE QUESTION|remainder is|is asked nowhere|'
    r'[Gg]ated on\s*`?PO-\d|open question', re.I)


def main():
    print()
    print('  check_rows_name_the_open -- does every open row say what is open?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    total = 0
    checked = 0
    bad = []
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m:
            continue
        total += 1
        if m.group(1) or line.lstrip('|').lstrip().startswith('~~'):
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) < 5:
            continue
        checked += 1
        s = cells[4]
        j = s.find('▣ HISTORY')
        head = s[:j] if j > 0 else s
        if not OPEN_CLAUSE.search(head):
            bad.append(m.group(2))

    print(f'  {checked} open row(s) of {total} in the register')
    if bad:
        print()
        for pid in bad:
            print(f'    [FAIL] {pid}: its head states what is settled and never says what is OPEN')
        print()
        print('    ⛭ ** A register that records only what is known is a record of the past. **')
        print('       *** The row is open; its head must say what that means. ***')
        return 1

    print('  every open row names what is open.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
