#!/usr/bin/env python3
"""gate_audit.py -- WHICH WIRED GATES CAN ACTUALLY FAIL?

** WHY.  r2650. **  r2649 closed on a pattern: *** every instrument this session that reported a number
wrong reported it LOW -- and low is the direction that looks like success. ***  ⇒ ** This audit asks the
inverse question about the gate count itself, which is the one number that has only ever gone up. **

** THE FINDING IT WAS BUILT FROM. **  ** Of 34 wired gates, two have NO failure path at all: **
`check_arcpins` and `check_citations` run, print, and return 0 unconditionally.
  * ** `check_citations` says so in its own docstring ** -- "like `check_supersession` it is a REPORT and
    not a verdict" -- *** so it is honest and its presence in the wired list is the mislabelling, not the
    gate. ***
  * ** `check_arcpins` is a LINT **, and r2562's rule covers exactly this: "build the lint, measure it,
    and usually don't ship it -- the lint is the instrument, not the deliverable."

  ⇒ *** So "35 gates" was two too many.  The honest statement is THIRTY-TWO that can fail plus TWO that
      report -- and a report in the failing list is a green tick nobody earned. ***

** WHAT THIS PRINTS. **  Every wired gate, and whether it contains a failure path.  ** It does not run
them ** -- a gate can have a failure path and still be untestable, which is the separate question
`check_dupes` spent two revisions on.

    python3 scripts/gate_audit.py

Written r2650.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

FAILS = re.compile(r'return 1|exit\(1\)|sys\.exit\(1\)|SystemExit\(1\)')


def wired():
    wf = open(os.path.join(ROOT, '.github', 'workflows', 'gates.yml'),
              encoding='utf-8', errors='replace').read().split('\n')
    i = next((k for k, l in enumerate(wf) if 'for g in' in l), None)
    if i is None:
        return []
    names, k = [], i
    while True:
        names += [w.rstrip(';') for w in wf[k].split() if w.startswith('check_')]
        if not wf[k].rstrip().endswith('\\'):
            break
        k += 1
    return sorted(set(names))


def main():
    print()
    print('  gate_audit -- which wired gates can actually fail?')
    print()
    can, cannot = [], []
    for g in wired():
        p = os.path.join(ROOT, 'corpus', g + '.py')
        if not os.path.exists(p):
            cannot.append((g, 'FILE MISSING'))
            continue
        d = open(p, encoding='utf-8', errors='replace').read()
        (can if FAILS.search(d) else cannot).append(
            (g, '' if FAILS.search(d) else 'no failure path'))
    print(f'  {len(can)} wired gates CAN fail')
    print(f'  {len(cannot)} wired gates CANNOT')
    for g, why in cannot:
        print(f'    ⛔ {g:<26} {why}')
    print()
    print('  ⌗ ** A report in the failing list is a green tick nobody earned. **  *** Either give it a')
    print('    failure path, or move it out of the wired suite and run it as a lint. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
