#!/usr/bin/env python3
"""check_currency.py -- L-42: CONSOLIDATE's register has lapsed twice (brought current at
r1730 after 130 revisions, again at c54.13 after ~500).  A recurring defect wants a gate.

Compares the highest revision mentioned in each standing register against the fork's own
current state, and fails on any that has fallen more than a window behind.

** c54.1xx PATCH -- THE CLOCK WAS ONE OF THE THINGS BEING CHECKED. **
The original read the current revision from `FORK_c54.md` alone, and did not watch that file.
So when the fork record itself stopped being updated, every lag was computed against a stale
anchor, and the gate could not fail.  Worse, it printed the evidence: registers ahead of the
anchor showed NEGATIVE lag (`lag -73`), which the `lag <= WINDOW` test passes.  A negative
lag is not "very current" -- it is proof the anchor is wrong.

Two changes, both minimal:
  1. HEAD is the maximum over the fork record AND every watched register, so the clock cannot
     be dragged backwards by one file falling behind.
  2. `FORK_c54.md` joins the watch list, and a negative lag against HEAD is reported
     explicitly rather than silently passing.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
WINDOW = 6          # revisions a standing register may lag before it is stale
FORK = 'FORK_c54.md'
WATCH = [FORK, 'CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md', 'THE_LIVE_ARC.md',
         'THE_OPEN_PROBLEMS_LEDGER.md', 'CORPUS_MAP.md', 'INDEX.md', 'WHATS_TEED_UP.md']

def rev(path):
    if not os.path.exists(path): return None
    rs = [int(x) for x in re.findall(r'c54\.(\d+)', open(path, encoding='utf-8',
                                                         errors='replace').read())]
    return max(rs) if rs else None

def main():
    seen = {w: rev(os.path.join(ROOT, w)) for w in WATCH}
    live = [r for r in seen.values() if r is not None]
    if not live:
        print('  [FAIL] cannot read the fork state from any watched register'); return 1
    head = max(live)                      # (1) the clock is the highest thing anybody says
    fork = seen[FORK]
    src = [w for w, r in seen.items() if r == head]
    print(f"  head: c54.{head}   (highest mention across the watched set: {', '.join(src)})")
    print(f"  fork record `{FORK}` states: "
          f"{'c54.%d' % fork if fork is not None else 'nothing'}   "
          f"staleness window: {WINDOW} revisions")
    if fork is not None and head - fork > WINDOW:
        print(f"  ⚠ THE FORK RECORD IS ITSELF {head - fork} REVISIONS BEHIND THE HEAD -- "
              f"it is a standing register, not an exempt clock.")
    print()
    stale = []
    for w in WATCH:
        r = seen[w]
        lag = None if r is None else head - r
        tag = 'never' if r is None else f"c54.{r}  (lag {lag})"
        flag = '' if (r is not None and lag <= WINDOW) else '   <-- STALE'
        if flag: stale.append(w)
        print(f"    {w:>52}  {tag}{flag}")
    print()
    if stale:
        print(f"  STALE REGISTERS: {len(stale)}")
        for s in stale: print(f"    [FAIL] {s} has not been brought current")
        return 1
    print("  Every standing register is current.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
