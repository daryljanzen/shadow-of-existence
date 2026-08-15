#!/usr/bin/env python3
"""check_routing_current.py -- A ROUTED ITEM MUST NOT NAME A STRUCK ROW AS LIVE.

** WHY.  r2834. **  *** `FOR_54` and `FOR_56` are where one line hands the other its findings.  ** A
stale claim there crosses the line boundary ** -- the one direction no other gate covers, because the
receiving line has no way to check it against a register it is not reading. ***

  ⇒ *** Swept: `FOR_56` carried ** three section headers naming `PO-4` ** with no indication the row was
      struck at r2778.  All three are cc54's record of a MERGE defect that transiently un-closed the row
      -- ** true history, and unreadable as such by anyone who did not already know **. ***

** WHAT THE SWEEP ALSO FOUND, and it is the reason the gate is narrow. **  *** Six overturn statements
across the two documents, and ** all six are self-marking ** -- each states its own retraction in the
item's own header ("WITHDRAWN c54.230", "HALF OF THIS ITEM IS RETRACTED r2699").  ** That is the correct
form, the same one `THE_LIVE_ARC` uses **, and it needs no separate mark. ***

** WHAT THIS CHECKS. **  *** Every section header in a routing document naming a struck row must carry
the strike within four lines. ***

    python3 corpus/check_routing_current.py

Written r2834.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

DOCS = ['FOR_54.md', 'FOR_56.md']


def main():
    print()
    print('  check_routing_current -- does any routed item name a struck row as live?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    struck = set()
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if m and (m.group(1) or line.lstrip('|').lstrip().startswith('~~')):
            struck.add(m.group(2))

    bad, checked = [], 0
    for d in DOCS:
        p = os.path.join(ROOT, d)
        if not os.path.exists(p):
            continue
        lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
        for i, line in enumerate(lines):
            if not re.match(r'\s*#+\s', line):
                continue
            for pid in re.findall(r'\bPO-\d+[a-z]?\b', line):
                if pid not in struck:
                    continue
                checked += 1
                if re.search(r'STRUCK|struck|~~|closed', ' '.join(lines[i:i+4])):
                    continue
                bad.append((d, pid, re.sub(r'[*`]', '', line).strip()[:56]))

    print(f'  {checked} routed header(s) naming a struck row')
    if bad:
        print()
        for d, pid, h in bad[:10]:
            print(f'    [FAIL] {d}: {pid} is struck and this header does not say so')
            print(f'           "{h}..."')
        print()
        print('    ⛭ ** A routing document crosses the line boundary. **  *** The receiving line')
        print('       cannot check it against a register it is not reading. ***')
        return 1

    print('  no routed item names a struck row as live.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
