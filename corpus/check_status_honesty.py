#!/usr/bin/env python3
"""check_status_honesty.py -- A ROW IS CLOSED ONLY WHEN ITS ROW SAYS SO.

** WHY.  r2827. **  *** Four consecutive status reports called `PO-6` "closed, ~2%, merge only" on the
strength of `L-821`'s $7/40$.  ** The $7/40$ was OWED ITEM #472 under the row.  THE ROW is "the
interacting tower --- the spectrum of $\\hat\\Gamma$, whether it is bounded below, the UV definition". **
The row read OPEN throughout. ***

  ⇒ ** AN OWED ITEM DISCHARGING IS NOT A ROW CLOSING. **  *** The register was right the whole time and
      the summary was wrong -- which is the worse direction, because a reader checks the summary. ***

** ⛭⛭ WHAT MAKES THIS DETECTABLE. **  *** A row is closed when it is STRUCK (`~~`) or its status cell
opens with a closure word.  ** Anything else is open, whatever any receipt discharged. **  So the check
is: for every row not struck, the status cell must not be described anywhere as closed. ***

** WHAT THIS CHECKS. **  Every `PROTECTED_OPEN` row's own struck-state against the closure words in
`BOARD.md`, `THE_PLAN.md` and `OPEN_PROBLEMS_MAP.md` -- the documents a reader takes a status from.

  ⌗ ** It cannot check a chat reply, ** *** which is where r2827's error lived.  What it can do is stop
    the same claim entering the DOCUMENTS, and print the true state so a summary has something correct
    to copy. ***

    python3 corpus/check_status_honesty.py

Written r2827.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
# ** r2827a: the first pattern matched SUB-OBJECTS -- "PO-7's inversion 3 is closed",
# "four of five ROUTES are closed", "PO-3 corrected, NOT closed".  *** A row is described as
# closed only when the CLOSURE VERB attaches to the row itself, with nothing between. ***
# ** Require the id immediately followed by the verb, and exclude negations. **
CLOSED = re.compile(r'\b(PO-\d+[a-z]?)`?\*{0,2}\s+(?:is |now )?(?:CLOSED|closed)\b', re.I)
NEGATED = re.compile(r'not closed|corrected, not|un-?closed', re.I)

DOCS = ['BOARD.md', 'THE_PLAN.md', 'OPEN_PROBLEMS_MAP.md']


def main():
    print()
    print('  check_status_honesty -- is any open row described as closed?')
    print()
    raw = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8', errors='replace').read()

    state = {}
    for l in raw.split('\n'):
        m = ROW.match(l)
        if m:
            state[m.group(2)] = bool(m.group(1)) or l.lstrip('|').lstrip().startswith('~~')

    openrows = sorted(p for p, s in state.items() if not s)
    print(f'  {len(state)} row(s); {len(openrows)} OPEN: {openrows}')

    bad = []
    for d in DOCS:
        p = os.path.join(ROOT, d)
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        for m in CLOSED.finditer(t):
            pid = m.group(1)
            if pid in state and not state[pid] and not NEGATED.search(
                    t[max(0, m.start()-60):m.end()+30]):
                bad.append((d, pid, re.sub(r'\s+', ' ', m.group(0))[:70]))

    if bad:
        print()
        for d, pid, seg in bad:
            print(f'    [FAIL] {d}: {pid} is OPEN in the register but described as closed')
            print(f'           "{seg}"')
        print()
        print('    ⛭ ** An owed item discharging is not a row closing. **  *** The row is the object in')
        print('       its own object cell; a receipt discharges an OWED ITEM under it. ***')
        return 1

    print('  no open row is described as closed.')
    print()
    print('  ⌗ the true state, for any summary to copy:')
    for p in openrows:
        print(f'      {p}  OPEN')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
