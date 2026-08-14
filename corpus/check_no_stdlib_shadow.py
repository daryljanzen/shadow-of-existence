#!/usr/bin/env python3
"""check_no_stdlib_shadow.py -- NO MODULE IN THIS TREE MAY SHADOW A STDLIB MODULE.

** WHY.  THE FOURTH NAMESPACE-COLLISION CLASS, and the most expensive so far. **  `scripts/queue.py`
(r2615, the work-list) shadowed the stdlib `queue`.  `concurrent.futures` imports `queue` ** lazily **, so
the collision:

  * ** survived import ** and died on first use -- `module 'queue' has no attribute 'SimpleQueue'`;
  * ** presented as no verdict line **, which reads as NOT YET RUN rather than BROKEN;
  * *** took down `run_all_receipts.py` and with it the nightly heavy CI tier -- the one gate that runs
      the cosmology receipts -- SILENTLY, from r2615 to r2670. ***

  ⌗ ** Found by cc54, by RUNNING the full camb+pynucastro sweep ** -- which neither chat line can do.  ⇒
  *** A shadow is invisible to every reader and to every fast-tier gate; only an execution that reaches
  the lazy import sees it. ***

** WHAT THIS CHECKS. **  Every `.py` in `scripts/` and `corpus/` -- the two directories that land on
`sys.path[0]` when a script there is run -- against `sys.stdlib_module_names`.

  ⚠ ** It cannot catch a shadow of a THIRD-PARTY module ** (`numpy`, `sympy`, `camb`) -- *** those are not
      enumerable without importing them, and importing to check is the same risk. ***  Recorded so the
      coverage is not overstated.

    python3 corpus/check_no_stdlib_shadow.py

Written r2675.  Stated for reversal.
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** directories whose contents land on sys.path[0] when a script inside them runs. **
ON_PATH = ('scripts', 'corpus')


def main():
    print()
    print('  check_no_stdlib_shadow -- does any module here shadow the stdlib?')
    print()
    std = set(sys.stdlib_module_names)
    bad = []
    n = 0
    for d in ON_PATH:
        for f in sorted(glob.glob(os.path.join(ROOT, d, '*.py'))):
            n += 1
            name = os.path.basename(f)[:-3]
            if name in std:
                bad.append((d, name))
    print(f'  {n} modules checked against {len(std)} stdlib names')
    if bad:
        print()
        for d, name in bad:
            print(f"    [FAIL] {d}/{name}.py shadows the stdlib module '{name}'")
        print()
        print('    ⛔ ** A SHADOW IS INVISIBLE TO EVERY READER AND EVERY FAST-TIER GATE. **  *** The')
        print("       r2615 `queue` shadow took down the nightly heavy tier for 55 revisions and")
        print('       presented as "not yet run" rather than "broken", because `concurrent.futures`')
        print('       imports lazily and the crash produced no verdict line. ***  Rename the module.')
        return 1
    print('  no module shadows the stdlib.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
