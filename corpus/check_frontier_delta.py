#!/usr/bin/env python3
"""THE FRONTIER DELTA GATE -- `r7399` ⑪, ROUTE B.

** WHAT WENT WRONG AND WHY A GATE. **  THE_FRONTIER's headline publishes
`N OPEN · S STEPS LEFT (was W last revision)`.  `W` was `sum(EST[p][2] for p in ORDER if p in live)`
-- index 2 being `steps-last-revision`, hand-written and backfilled by nobody.  Seven of nine live
rows carried `0`.  Measured against the history by
computations/beyond_the_wall/r7399_cc66_the_unrottable_delta/history.py: **the published delta was
FALSE at 14 of the 15 revisions `r7371`..`r7399`, and at `r7389` the SIGN WAS INVERTED** -- the real
step count fell `19` -> `16` while the headline announced a rise from `2` to `16`.

`r7399` ⑪ named two routes and this repository's answer is BOTH, because they fail differently:
  ROUTE A (`scripts/regen_frontier.py`) persists the per-revision total, so the headline no longer
    reads a hand-written field at all.  It PREVENTS.
  ROUTE B (this file) checks that the persistence is CURRENT and that the published line agrees with
    it.  It DETECTS -- which Route A cannot do, because a generator that is never run cannot notice
    that it was never run, and `regen_frontier.py` has no `--check` mode and appears nowhere in
    `.github/workflows/gates.yml`.

** WHAT IT DOES NOT CATCH, stated because ⑪ asked. **  A seat reading a NAMED step as an INCREMENT
-- `r7399`'s `PO-88` case, where 20 would be reported against a real 19 -- is not reachable from
here.  Whether a named step SHARPENS an existing step or ADDS one is a reading of what the step is,
and no comparison of numbers decides it.  *** Said rather than approximated. ***

Usage:  python3 corpus/check_frontier_delta.py
"""
import importlib.util, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_generator():
    spec = importlib.util.spec_from_file_location(
        'rf_gate', os.path.join(ROOT, 'scripts', 'regen_frontier.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    rf = _load_generator()
    raw = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8', errors='replace').read()
    live = set()
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if m and not (m.group(1) or line.lstrip('|').lstrip().startswith('~~')):
            live.add(m.group(2))
    steps = sum(rf.EST[p][1] for p in rf.ORDER if p in live and p in rf.EST)
    rev = rf._register_rev()
    hist = rf._steps_history()

    front = open(os.path.join(ROOT, 'THE_FRONTIER.md'), encoding='utf-8',
                 errors='replace').read()
    hm = re.search(r'\*\*(\d+) OPEN · (\d+) STEPS LEFT\*\*\s*\*\(was (\d+) last revision\)\*', front)

    fails = []
    print()
    print('  FRONTIER DELTA -- is the published step delta a measurement or a hand-written field?')
    print(f'    register revision (DERIVED from its rows, not its `current:` stamp): {rev}')
    print(f'    {len(live)} live row(s); {steps} step(s) recomputed from the generator\'s own EST')
    print(f'    step history: {len(hist)} revision(s) on record'
          + (f', last {hist[-1][0]} = {hist[-1][1]}' if hist else ''))
    print()

    if not hist:
        fails.append('the step history is empty -- run python3 scripts/regen_frontier.py')
    else:
        if hist[-1][0] != rev:
            fails.append(f'the step history\'s last revision is {hist[-1][0]} and the register is '
                         f'at {rev} -- the generator has not been run at this revision')
        elif hist[-1][1] != steps:
            fails.append(f'the step history records {hist[-1][1]} step(s) at {rev} and the '
                         f'generator\'s EST now gives {steps} -- the history is stale')
    if hm is None:
        fails.append('THE_FRONTIER.md carries no readable headline')
    elif hist:
        want_steps = steps
        want_was = hist[-2][1] if len(hist) > 1 and hist[-1][0] == rev else hist[-1][1]
        if int(hm.group(2)) != want_steps:
            fails.append(f'THE_FRONTIER publishes {hm.group(2)} steps and the register gives '
                         f'{want_steps}')
        if int(hm.group(3)) != want_was:
            fails.append(f'THE_FRONTIER publishes "(was {hm.group(3)})" and the previous '
                         f'revision\'s own recorded total is {want_was}')

    # ⌗ REPORTED, NOT FAILED: the old hand-written field.  It no longer feeds the headline, so a 0
    #   in it is a dead value rather than a false published statement -- the exact condition that was
    #   true for seven rows and silent, kept visible so its disappearance can be seen.
    zeros = [p for p in rf.ORDER if p in live and p in rf.EST
             and rf.EST[p][2] == 0 and rf.EST[p][1] != 0]
    if zeros:
        print(f'  ⌗ {len(zeros)} live row(s) still carry steps-last-revision 0 with a non-zero '
              f'steps-left: {" ".join(zeros)}')
        print('    Reported, NOT a failure: index 2 no longer feeds the headline (r7399 ⑪, Route A).')
        print()

    # ⌗ REPORTED: the same failure shape one level down, found while building this.
    stamp = re.search(r'(?m)^current:\s*(\S+)', raw)
    if stamp and stamp.group(1) != rev:
        print(f'  ⌗ THE_REGISTER.md\'s `current:` stamp reads {stamp.group(1)} while its own rows '
              f'reach {rev}.')
        print('    A hand-written stamp, rotted the same way the delta was -- and '
              'regen_frontier.py')
        print('    copies it into THE_FRONTIER\'s `current:`.  REPORTED: the register is not this')
        print('    gate\'s to repair, and keying the step history by that stamp would have recorded')
        print('    every revision under one key and published a permanent zero delta.')
        print()

    if fails:
        for f in fails:
            print(f'  [FAIL] {f}')
        print()
        print('     Run: python3 scripts/regen_frontier.py')
        return 1

    print('  the published delta is the previous revision\'s own recorded total.')
    print('  ⌗ WHAT THIS DOES NOT CATCH, and ⑪ asked: a NAMED step read as an INCREMENT -- PO-88 at')
    print('    r7399, where 20 would be reported against a real 19.  Whether a named step SHARPENS')
    print('    a step or ADDS one is a reading, and no comparison of numbers decides it.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
