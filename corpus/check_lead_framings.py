#!/usr/bin/env python3
"""check_lead_framings.py -- A LIVE LEAD MUST NOT CALL UNTOUCHED WHAT ITS ROW HAS ANSWERED.

** WHY.  r2833. **  *** `L-165` read LIVE and said the closed-form nonlinear $\\Lambda>0$ solution was
** "untouched" ** -- while `PO-6`'s current-state head says its expansion parameter is NAMED (the
horizon separation).  It also said "what remains is defining the sum"; the row says the remainder is
** joint satisfiability **.  ** 357 revisions stale, and live. ** ***

  ⇒ ** A struck lead is caught by `check_leads_follow_rows`.  This is the other failure: a lead that is
      correctly LIVE and points at the wrong question. **  *** `L-221` was the same at r2832 -- posing
      `PO-5` as "what bridge from grading to field is not being a kernel?", a framing four route-closures
      out of date. ** A live lead with a dead framing sends the next node at the wrong question, and
      nothing downstream catches it, because the lead is not wrong about being open. ** ***

** WHAT THIS CHECKS. **  *** For every LIVE lead anchored on a row: if its question cell calls something
untouched / not yet / unbuilt / still open, that word must not sit next to a term the row's
`▣ CURRENT STATE` head reports as settled. ***

  ⌗ ** Word-level, so it is a prompt to read, not a verdict ** -- *** a flagged lead may be fine; what it
    may not be is unexamined. ***

    python3 corpus/check_lead_framings.py

Written r2833.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

STALE = re.compile(r'\b(untouched|not yet built|unbuilt|still open|not begun|remains untouched)\b', re.I)
SETTLED = re.compile(r'\b(is NAMED|is settled|is ANSWERED|IS CLOSED|is delivered|re-derived)\b')


def main():
    print()
    print('  check_lead_framings -- does any live lead call untouched what its row has answered?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    heads = {}
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m:
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        s = cells[4] if len(cells) > 4 else ''
        j = s.find('▣ HISTORY')
        heads[m.group(2)] = s[:j] if j > 0 else s

    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()

    bad, checked = [], 0
    for line in arc.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(L-\d+)\*\*', line)
        if not m or m.group(1) or line.lstrip('|').lstrip().startswith('~~'):
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) < 4:
            continue
        pid = next((p for p in heads if re.search(rf'\b{re.escape(p)}\b', ' '.join(cells[:4]))), None)
        if not pid:
            continue
        checked += 1
        hit = STALE.search(cells[3])
        if not hit:
            continue
        # ** already read and marked? **
        if 'STALE' in line or 'Read `' + pid in line:
            continue
        if SETTLED.search(heads[pid]):
            bad.append((m.group(2), pid, hit.group(0)))

    print(f'  {checked} live lead(s) anchored on a row')
    if bad:
        print()
        for lid, pid, word in bad:
            print(f'    [FAIL] {lid} calls something "{word}" and {pid}\'s head reports settled work')
            print(f'           read the lead against the row\'s ▣ CURRENT STATE head')
        print()
        print('    ⛭ ** A live lead with a dead framing sends the next node at the wrong question. **')
        print('       *** Nothing downstream catches it, because the lead is not wrong about being')
        print('       open — only about what is open. ***')
        return 1

    print('  no live lead contradicts its row\'s current state.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
