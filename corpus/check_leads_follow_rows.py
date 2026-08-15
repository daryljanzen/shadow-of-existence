#!/usr/bin/env python3
"""check_leads_follow_rows.py -- A LEAD WHOSE ROW IS STRUCK MUST BE STRUCK TOO.

** WHY.  r2832. **  *** `THE_LIVE_ARC` carries a lead row for each protected row.  When `PO-9` was
struck, its lead `L-175` stayed OPEN -- still posing "can a second slicing be non-arbitrary?" as the
live question, in the register a node reads to pick up work. ***

  ⇒ ** This is the propagation failure at a FOURTH level. **  *** Within a row; across rows; out to the
      reporting documents; and now out to the LEAD register, which is where the work is actually picked
      up.  ** A struck row with a live lead is closed work still being offered. ** ***

** WHAT THIS CHECKS. **  *** Every lead naming a struck row in its ANCHOR cell must itself be struck,
or carry a note saying why it outlives its row. ***

  ⌗ ** A lead may legitimately outlive its row ** -- *** its anchor may have moved, or it may carry a
    residue the row did not own.  The check requires that to be SAID, not that it not happen. ***

    python3 corpus/check_leads_follow_rows.py

Written r2832.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def main():
    print()
    print('  check_leads_follow_rows -- is every lead of a struck row struck too?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    struck = set()
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if m and (m.group(1) or line.lstrip('|').lstrip().startswith('~~')):
            struck.add(m.group(2))

    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()

    bad, checked = [], 0
    for line in arc.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(L-\d+)\*\*', line)
        if not m:
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) < 3:
            continue
        anchor = cells[2]
        for pid in struck:
            if not re.search(rf'\b{re.escape(pid)}\b', anchor):
                continue
            checked += 1
            lead_struck = bool(m.group(1)) or line.lstrip('|').lstrip().startswith('~~')
            # ** r2832a: an `'r2832' in line` clause passed ANY row touched this revision --
            # a revision-number escape hatch, not a check.  *** The lead must be STRUCK, or
            # carry an explicit note that it OUTLIVES its row. ***
            if lead_struck or 'STRUCK' in line:
                continue
            if re.search(r'outlives its row|survives its row', line, re.I):
                continue
            bad.append((m.group(2), pid))

    # ** r2835: a coverage number must say what COULD have been checked, not only what
    # was.  *** "1 lead checked" reads as thin coverage; "1 of 27, and 26 are not anchored
    # on a struck row" says the denominator is right. ***
    total = sum(1 for l in arc.split('\n')
                if re.match(r'\|\s*(~~)?\s*\*\*(L-\d+)\*\*', l))
    print(f'  {checked} of {total} lead(s) anchored on a struck row '
          f'({total - checked} anchored elsewhere or on a live row)')
    if bad:
        print()
        for lid, pid in bad:
            print(f'    [FAIL] {lid} is LIVE and its row {pid} is STRUCK')
        print()
        print('    ⛭ ** A struck row with a live lead is closed work still being offered. **')
        print('       *** Strike the lead, or say why it outlives its row. ***')
        return 1

    print('  every lead of a struck row is struck or explains itself.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
