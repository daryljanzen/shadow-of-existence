#!/usr/bin/env python3
"""check_map_overturns.py -- AN OVERTURNED REVISION ENTRY MUST SAY SO AT ITS OWN HEAD.

** WHY.  r2834. **  *** `CORPUS_MAP.md` is 5,084,410 characters and 2,156 revision entries, and had
never been swept.  ** Seventeen entries state a verdict that a later entry overturns, and not one said
so. **  A reader arriving at `r2766`'s entry -- "THE LEDGER DOES NOT REACH SECOND ORDER IN THE SHEAR" --
had no way to learn that `r2771` corrects its basis from three dimension-four terms to five. ***

  ⇒ ** The log is append-only by design, and that is right ** -- *** the entries are history and must
      not be rewritten.  ** But a history entry that reads as a live verdict is not history, it is a
      trap ** -- and `r696`'s entry, the cyanide-face implosion the field note records, sat unmarked
      beside `r697`'s retraction of it. ***

** THE SIZING THAT MADE IT WORKABLE. **  *** 5.08M characters sounded unbounded.  ** Counted: 32
overturn statements, 29 distinct victims, 17 unmarked. **  The debt was a morning's work, and sizing it
first is what showed that. ***

** WHAT THIS CHECKS. **  *** For every "X WITHDRAWS/CORRECTS/REVERSES/RETRACTS Y" in the map: Y's own
entry must carry a mark within 700 characters of its head. ***

    python3 corpus/check_map_overturns.py

Written r2834.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

OVERTURN = re.compile(r'(WITHDRAW[SN]?|CORRECTS|REVERSES|RETRACT\w*)\s+(r\d{3,4})', re.I)
SELFMARK = re.compile(r'WITHDRAWN|SUPERSEDED|CORRECTED|RETRACTED|OVERTURNED|reversed', re.I)


def main():
    print()
    print('  check_map_overturns -- does every overturned revision entry say so?')
    print()
    t = open(os.path.join(ROOT, 'CORPUS_MAP.md'), encoding='utf-8', errors='replace').read()

    entries = len(re.findall(r'^### Revision r\d{3,4}', t, re.M))
    victims, bad = set(), []
    for m in OVERTURN.finditer(t):
        v = m.group(2)
        if v in victims:
            continue
        victims.add(v)
        i = t.find(f'### Revision {v}')
        if i < 0:
            continue
        if not SELFMARK.search(t[i:i+700]):
            bad.append((v, m.group(1).upper()))

    print(f'  {entries:,} revision entries; {len(victims)} named as overturned')
    if bad:
        print()
        for v, verb in bad[:12]:
            print(f'    [FAIL] {v} is {verb} by a later entry and its own entry does not say so')
        print()
        print('    ⛭ ** An append-only log is right to keep its history. **  *** But a history entry')
        print('       that reads as a live verdict is not history, it is a trap. ***')
        return 1

    print('  every overturned entry carries its mark.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
