#!/usr/bin/env python3
"""r7441 ⑫ -- CAN check_quote_pins' TARGET_DISPUTED-stale branch (line 386) FIRE ON ANY DATA?

The branch is `if _disp_stale: ... bad += 1`, and one line above:

    _disp_stale = sorted(k for k in TARGET_DISPUTED if not (k in live and k in base and live[k][0] != base[k][0]))

It is a comprehension OVER `TARGET_DISPUTED`, which is a module-level dict in the instrument:

    TARGET_DISPUTED = {}   # r7261: B57, the one entry, was ruled by 66 -- PAPER is right, ...

An empty source makes the comprehension empty for EVERY (live, base).  This probe does not argue it;
it runs the gate's own expression over adversarial (live, base) pairs and shows the result is [] each
time.  It does NOT edit the instrument.
"""
import importlib.util, os, sys
spec = importlib.util.spec_from_file_location('qp', os.path.join('corpus', 'check_quote_pins.py'))
qp = importlib.util.module_from_spec(spec); spec.loader.exec_module(qp)

print(f'  TARGET_DISPUTED as the instrument carries it: {qp.TARGET_DISPUTED!r}  (len {len(qp.TARGET_DISPUTED)})')
print()

K1, K2 = ('receipts/A/R1.py', 'a literal'), ('receipts/B/R2.py', 'another')
CASES = {
    'both empty':                      ({}, {}),
    'live and base agree':             ({K1: ('PAPER',)}, {K1: ('PAPER',)}),
    'live and base DISAGREE':          ({K1: ('PAPER',)}, {K1: ('RECEIPT',)}),
    'key only in live':                ({K1: ('PAPER',)}, {}),
    'key only in base':                ({}, {K1: ('RECEIPT',)}),
    'two keys, one disagreeing':       ({K1: ('PAPER',), K2: ('RECEIPT',)}, {K1: ('RECEIPT',), K2: ('RECEIPT',)}),
    'UNDECIDED against a verdict':     ({K1: ('UNDECIDED',)}, {K1: ('PAPER',)}),
}
bad = 0
for name, (live, base) in CASES.items():
    disp_stale = sorted(k for k in qp.TARGET_DISPUTED
                        if not (k in live and k in base and live[k][0] != base[k][0]))
    tgt_bad = sorted(k for k in live if k in base and live[k][0] != base[k][0]
                     and k not in qp.TARGET_DISPUTED)
    if disp_stale:
        bad += 1
    print(f'    _disp_stale = {disp_stale!s:<6}  (_tgt_bad = {len(tgt_bad)})   -- {name}')
print()
print(f'  {len(CASES)} (live, base) pair(s) tried, {bad} made the branch fire.')
print('  ⌗ It cannot fire while TARGET_DISPUTED is empty, and filling it is an edit to the instrument\'s')
print('    own control -- SELF-REFERENTIAL by r7437 ④, in the denominator and out of the numerator.')
print('    ⛭ Its sibling `_tgt_bad` (line 395) is the live-vs-baseline branch and IS data-reachable:')
print('      the same comprehension with TARGET_DISPUTED as an EXEMPTION rather than a source.')
print('    ⚠ Not a fault: the entry was emptied at r7261 when 66 ruled B57, and a guard left in place')
print('      with nothing to guard is the cheapest possible record that the dispute was settled.')
sys.exit(1 if bad else 0)
