#!/usr/bin/env python3
"""r7399 ⑪ -- the binding test for ROUTE A's persistence, including the re-stale trap.

Each case is run in the direction that FAILS if the mechanism is absent.  The end-to-end behaviour
was separately observed on the real tree (three consecutive runs at one revision leave the headline
at `was 19`); this tests the logic the trap lives in.

    python3 -I test_route_a.py <repo-root>
"""
import importlib.util, os, sys, tempfile

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
spec = importlib.util.spec_from_file_location('rf', os.path.join(ROOT, 'scripts',
                                                                 'regen_frontier.py'))
rf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rf)

fails = []


def ck(name, got, want):
    ok = got == want
    print(f'  {"OK  " if ok else "FAIL"}  {name}: got {got!r}, want {want!r}')
    if not ok:
        fails.append(name)


with tempfile.TemporaryDirectory() as tmp:
    rf.STEPS_HISTORY = os.path.join(tmp, 'hist.tsv')

    # ⒜ no prior revision on record -> was == steps, i.e. a TRUE zero delta rather than a false one
    ck('A no history -> zero delta', rf._steps_was('r1000', 7), 7)
    ck('A no history -> row recorded', rf._steps_history(), [('r1000', 7)])

    # ⒝ a NEW revision takes the previous revision's own total
    ck('B new revision -> prior total', rf._steps_was('r1002', 9), 7)
    ck('B new revision -> appended', rf._steps_history(), [('r1000', 7), ('r1002', 9)])

    # ⒞ ⛭ THE RE-STALE TRAP: a SECOND run in the SAME revision must not shift the baseline
    ck('C same revision again -> baseline unmoved', rf._steps_was('r1002', 9), 7)
    ck('C same revision again -> NOT appended', rf._steps_history(), [('r1000', 7), ('r1002', 9)])

    # ⒟ and a second run at the same revision with a CHANGED total updates the row, not the baseline
    ck('D same revision, new total -> baseline still prior', rf._steps_was('r1002', 12), 7)
    ck('D same revision, new total -> row replaced', rf._steps_history(),
       [('r1000', 7), ('r1002', 12)])

    # ⒠ the NEXT revision then reads the UPDATED total, not the one first written
    ck('E next revision -> updated prior total', rf._steps_was('r1004', 12), 12)

    # ⒡ a FALLING total is published as a fall -- the r7389 case, where the hand-written field
    #    inverted the sign (real 19 -> 16, published "from 2 to 16")
    ck('F falling total -> prior total, so the delta falls', rf._steps_was('r1006', 9), 12)

print()
if fails:
    print(f'⛔ {len(fails)} FAILED: {" ".join(fails)}')
    raise SystemExit(1)
print('  all 10 checks hold: the baseline moves only when the REVISION moves, and a repeat run in')
print('  one revision replaces its own row.  ⌗ ⒡ is the r7389 case, now published with its sign.')
