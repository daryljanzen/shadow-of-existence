#!/usr/bin/env python3
"""check_tilt_pins.py -- EVERY FLOAT PIN THAT SURVIVES A TILT OF ITS OWN DATA IS ADJUDICATED, AND THE OWED COUNT ONLY FALLS.

** WHAT DETACHED MEANS. **  A float pin that neither moves nor flips when every float the receipt reads is
tilted by a smooth five per cent -- *in a receipt the tilt demonstrably REACHED.*  *** The defect is an
assertion that passes on something other than its own measurement. ***

** THE MEASUREMENT IS NODE 70's AND THIS GATE DOES NOT REIMPLEMENT IT. **  It runs
`scripts/mutate_assertions.py --tilt` over that instrument's own scoped list and compares the DETACHED sites
against `corpus/tilt_pin_baseline.tsv`.

** WHY THIS IS GATE-GRADE NOW AND WAS NOT WHEN THE INSTRUMENT WAS FIRST BUILT. **  *At `r7113` the operator
scored 2 of 9 and node 70 said plainly it would not gate on it, which this seat accepted.*  ⇒ ** Both false
classes are now closed BY CONSTRUCTION rather than by tuning: **
  - ** the IMPORT ROUTE is hooked **, so a receipt reading its measurement by importing an instrument is
    perturbed like any other -- `C62`'s two `DAMPX` pins go from clean to `2.2e-2` and `8.2e-3` and FAIL, and
    its `r_D` equality moves `7.103 -> 6.910` instead of staying bit-identical;
  - ** CONSTANT is an exemption class ** for a pin whose operand traces only to literals and arithmetic, and
    *it must actually compute*: a bare literal compared with itself stays DETACHED, because it checks nothing.
⇒ *** Site precision went 2 of 9 to 2 of 2 on the same 69 receipts, and the remaining two are real. ***

  ⌗ ** AND NOT REACHED IS NOT CLEAN. **  *Three receipts the tilt does not reach are reported as unmeasured
  and never as passing.  That distinction is what makes the precision figure mean anything, and this gate
  prints the unmeasured count rather than folding it into a pass.*

** WHERE IT RUNS, AND WHY NOT PER PUSH. **  *Its cost is one receipt run per site -- node 70's own figure,
the same shape as the tolerance sweep.  So it belongs in the monthly backstop beside that sweep and not in
the fast list, whose budget is 420s per gate.*  ⛔ *A gate placed where it cannot finish is a gate that
reports the clock instead of the tree.*

  python3 corpus/check_tilt_pins.py
  python3 corpus/check_tilt_pins.py --list      # print the owed sites, complete and unfiltered

Written r7123.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'tilt_pin_baseline.tsv')
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')
LIST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7119_70_tilt_coverage', 'tilt_list.txt')

SITE = re.compile(r'\s*\[(DETACHED|NOT REACHED)\s*\]\s+(\S+?):(\d+):(\d+)\s+(.*)$')
OWED = 'OWED'
CEILING = 0          # the declared ceiling lives HERE and nowhere else, so it cannot go stale against itself
#: ⛭ r7123+cc66.92: 2 -> 0.  Both OWED sites (B4/B5) are repaired, so the bucket is empty and a
#: ceiling of 2 would be a standing permission for two new owed sites -- the same "silent permission
#: to regress" the baseline warns of for a stale entry.  A ceiling can only tighten the gate, which is
#: why this seat moved it in another seat's file; it reverses in one line if `70` wants it back.


def read_baseline():
    rows = {}
    if not os.path.exists(BASELINE):
        return rows
    for ln in open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 3:
            rows[(p[0], p[1])] = (p[2], p[3] if len(p) > 3 else '')
    return rows


def main():
    print()
    print('  TILT RATCHET -- does every float pin move when its own data moves?')
    print()
    base = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1
    if not os.path.exists(LIST):
        print(f'  ⛔ the instrument\'s scoped list is missing at {os.path.relpath(LIST, ROOT)}.')
        print('     ⌗ This gate runs 70\'s operator over ITS OWN list and does not invent a scope.')
        return 1

    # ⛭ r7123: `--list` returns BEFORE the instrument runs.  *A first draft placed it after, so printing
    #   the backlog paid the full one-run-per-site cost -- which is the same defect as a gate placed where
    #   it cannot finish, in miniature.*  The list is a property of the baseline alone and needs no run.
    verd0 = {}
    for v, _w in base.values():
        verd0[v] = verd0.get(v, 0) + 1
    if '--list' in sys.argv:
        n = verd0.get(OWED, 0)
        print(f'  THE OWED SITES, COMPLETE AND UNFILTERED -- {n} (read from the baseline, no run needed):')
        for (p_, e_), (v_, w_) in sorted(base.items()):
            if v_ == OWED:
                print(f'    {p_}')
                print(f'      {e_}')
                print(f'      {w_}')
        return 0

    out = os.path.join(os.environ.get('RUNNER_TEMP', '/tmp'), 'tilt_ratchet.txt')
    r = subprocess.run([sys.executable, INSTRUMENT, '--tilt', LIST, out],
                       cwd=ROOT, capture_output=True, text=True, timeout=14400)
    live, unreached = {}, []
    for ln in r.stdout.splitlines():
        m = SITE.match(ln)
        if not m:
            continue
        kind, path, _l, _c, expr = m.groups()
        if kind == 'DETACHED':
            live[(path, expr)] = True
        else:
            unreached.append(path)

    print(f'    DETACHED: {len(live)};  the baseline carries {len(base)}')
    print(f'    NOT REACHED: {len(set(unreached))} receipt(s) -- reported as UNMEASURED and never as clean')
    verd = {}
    for v, _w in base.values():
        verd[v] = verd.get(v, 0) + 1
    print(f'    by verdict: {verd}')
    owed = verd.get(OWED, 0)
    print(f'    {OWED}: {owed}   ** the only bucket that means work, and it may only fall **')

    bad = 0
    new = sorted(k for k in live if k not in base)
    if new:
        print()
        print(f'  ⛔ {len(new)} NEW DETACHED SITE(S) -- not in the baseline:')
        for p, e in new:
            print(f'    [FAIL] {p}')
            print(f'           {e}')
        print('     ⌗ A float pin that does not move when its own data moves is asserting something else.')
        print('       READ IT AND RECORD A VERDICT; the four hand-caught instances were all this class.')
        bad += 1
    else:
        print('    no new DETACHED site: the class has not grown.')

    gone = sorted(k for k in base if k not in live)
    if gone:
        print()
        print(f'  ⛔ {len(gone)} STALE BASELINE ENTR(Y/IES) -- no longer reported, so the adjudication')
        print('     describes nothing.  REMOVE the entry:')
        for p, e in gone:
            print(f'    [STALE] {p}')
            print(f'            {e}')
        print('     ⌗ A fixed site left in a baseline is a silent permission to regress there (r7069).')
        bad += 1
    else:
        print('    no stale entry: every adjudication still describes a live site.')

    if owed > CEILING:
        print()
        print(f'  ⛔ THE OWED COUNT ROSE: {owed} against the declared ceiling {CEILING}.')
        bad += 1
    else:
        print(f'    the ratchet holds: {owed} owed against a ceiling of {CEILING}')

    print()
    if bad:
        print('  ⛔ THE TILT RATCHET IS RED.')
        return 1
    print('  every float pin that survives a tilt of its own data is adjudicated, and the unmeasured')
    print('  receipts are named rather than counted as clean.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
