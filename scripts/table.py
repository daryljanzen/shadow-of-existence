#!/usr/bin/env python3
"""table.py -- ONE COMMAND, THE WHOLE PICTURE.

** WHY.  r2618, Daryl: ** "consolidate the reporting so you can report all of this concisely every step so
I can see what's happening."

  ⇒ *** `queue.py` prints every item and `status.py` prints the movement, and running two commands and
      splicing them by hand is how a report drifts from what the files say. ***

** WHAT IT PRINTS. **  The table, every item, one line each -- and against each, WHEN IT LAST MOVED.
Then the two numbers that mean something: ** how many items are on the table ** and ** how many dark
halves are answered **.  Nothing else.
  ⌗ ** No gate counts, no receipt counts. **  *** Those rise when the bookkeeping is kept and say
      nothing about the physics; they belong in `status.py` where they can be checked, not in the report
      of what is left. ***

    python3 scripts/table.py

Written r2618.  Stated for reversal.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

import re                                        # noqa: E402
import queue as Q                                # noqa: E402


def main():
    dh = Q.dark_halves()
    po = Q.po_items()
    lw = Q.ledger_work()
    rt = Q.routed()
    dp = Q.dispatch()
    live = [x for x in dh + po + lw + rt + dp if x['open']]

    print()
    print(f'  THE TABLE: {len(live)} items    DARK HALVES ANSWERED: '
          f'{sum(1 for x in dh if not x["open"])} of {len(dh)}')
    print()

    print('  DARK HALVES -- the physics not yet known')
    for x in dh:
        m = '⛔' if x['open'] else '✔ '
        print(f'    {m} {x["id"]:<7} {x["narrowed"]:>2}x  r{x["last"] or "----"}  {x["what"][:56]}')
    print()

    print(f'  PROTECTED OPEN -- {len(po)}')
    for x in po:
        k = 'kill' if x['kill'] else '    '
        print(f'    ⛔ {x["id"]:<7} {x["narrowed"]:>2}x  r{x["last"] or "----"}  {k}  {x["what"][:50]}')
    print()

    print(f'  LEDGER WORK -- {len(lw)}')
    for x in sorted(lw, key=lambda y: (y['kind'], y['paper'])):
        t = re.sub(r'\\[a-zA-Z]+|[{}$~\\]', '', x['what'])
        print(f'    ⛔ {x["kind"]:<18} {x["paper"][:16]:<16} {t[:46]}')
    print()

    print(f'  ROUTED -- {len(rt)}    DISPATCH -- {len(dp)}')
    for x in rt:
        print(f'    ⛔ {x["id"]:<9} {x["what"][:58]}')
    for x in dp:
        print(f'    ⛔ {x["id"]:<9} (L-218)')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
