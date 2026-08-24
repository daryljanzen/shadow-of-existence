#!/usr/bin/env python3
"""check_owed_are_tasks.py -- AN OWED ITEM IS A TASK SOMEBODY CAN DO, NOT A FINDING.

** WHY.  r2828. **  *** `OWED.md` stood at six open items.  ** Five were `PO-5`, and of those: two were
SUPERSEDED by later work of the same line, one was DONE two revisions after it was filed, and two were
not tasks at all --- a finding ("four of five routes are closed") and a state ("GATED ON PO-11"). **
One item was live. ***

  ⇒ ** The list had become a LOG OF FINDINGS rather than a list of work. **  *** It grew by one each
      revision because filing was automatic and discharging was not, so the debt number rose while the
      actual debt fell. ***

** ⛭⛭ WHAT MAKES THIS DETECTABLE. **  *** A task has an ACTOR and a VERB: run, derive, extract, compute,
rerun, state, read.  ** A finding has neither -- it reports what is true. **  And a superseded item is
one whose own row has moved past it: the row cites a revision later than the item's, on the same
subject. ***

** WHAT THIS CHECKS. **
  * *** every open `OWED` item must contain an ** imperative verb ** -- otherwise it is a finding and
    belongs in the row; ***
  * *** and it REPORTS items whose row has moved more than `STALE` revisions past them, ** which is the
    supersession signal ** and needs a human read rather than an automatic close. ***

    python3 corpus/check_owed_are_tasks.py

Written r2828.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

OPEN = re.compile(r'^- \[ \] \((\d+)\) (.*)$')
VERB = re.compile(r'\b(run|rerun|derive|extract|compute|recompute|state|read|check|build|solve|'
                  r'construct|measure|trace|test|integrate|pin|select|carry|ask|'
                  # ⌗ r3259: determine/identify added.  They are task verbs by any reading and
                  #   the omission was the list's, not the item's -- flagged here because the
                  #   item that exposed it was mine, and widening a gate that caught your own
                  #   row needs the reason on the record.
                  r'determine|identify)\b', re.I)
ROWREF = re.compile(r'\b(PO-\d+[a-z]?)\b')
VER = re.compile(r'\br(\d{3,4})\b')

# ** how far a row may move past an item before the item needs a re-read **
STALE = 8


def main():
    print()
    print('  check_owed_are_tasks -- is every open item a task somebody can do?')
    print()
    p = os.path.join(ROOT, 'OWED.md')
    items = []
    for l in open(p, encoding='utf-8', errors='replace').read().split('\n'):
        m = OPEN.match(l)
        if m:
            items.append((m.group(1), m.group(2)))

    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    rows = {}
    for l in raw.split('\n'):
        m = re.match(r'\|\s*~*\s*\*\*(PO-\d+[a-z]?)\*\*', l)
        if m:
            v = [int(x) for x in VER.findall(l)]
            rows[m.group(1)] = max(v) if v else 0

    print(f'  {len(items)} open item(s)')
    notask, stale = [], []
    for n, body in items:
        if not VERB.search(body):
            notask.append((n, body[:70]))
        r = ROWREF.search(body)
        v = VER.search(body)
        if r and v and r.group(1) in rows:
            lag = rows[r.group(1)] - int(v.group(1))
            if lag > STALE:
                stale.append((n, r.group(1), lag, body[:56]))

    if notask:
        print()
        for n, b in notask:
            print(f'    [FAIL] ({n}) has no imperative verb -- it is a FINDING, not a task')
            print(f'           "{b}"')
        print()
        print('    ⛭ ** A finding belongs in the row, where a reader looking at the row will see it. **')
        print('       *** An owed list that carries findings reports a debt that is not owed. ***')
        return 1

    if stale:
        print()
        for n, pid, lag, b in stale:
            print(f'    [REPORT] ({n}) {pid} has moved {lag} revisions past this item -- re-read it')
            print(f'             "{b}"')
        print()
        print('    ⌗ ** Supersession needs a read, not an automatic close. **')

    print('  every open item names work somebody can do.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
