#!/usr/bin/env python3
"""check_env_fingerprint.py -- ** PO-62: THE ONE TRIGGER A PUSH CANNOT SEE. **

*** WHY THIS GATE EXISTS. ***  `PO-60`'s third class is a tolerance calibrated at one machine's round-off
floor: a check that passes for a reason having nothing to do with what it is about, and that goes red on
somebody else's machine.  ** Node 70's `r6961+70.2` measured that the deciding variable is the
linear-algebra BUILD -- thread count and CPU kernel -- not any parameter inside a receipt. **  And
`r6975+70.1` then made the point this file is for:

    ⇒ *** THE ENVIRONMENT IS NOT IN ANY DIFF.  The receipts job installs numpy, scipy, sympy, mpmath,
        camb and pynucastro UNPINNED, so the build underneath every float comparison in the corpus can
        change between two nights with no push at all -- and a per-push scope, however good, cannot see
        it. ***

So the cadence for that class is two things, and only one of them is a push: the scoped sweep, and this.

** WHAT IT DOES. **  It records the fields that decide floating-point round-off -- the Python version, the
numpy and scipy versions, and the BLAS the arrays are multiplied by -- and compares them against the
committed fingerprint.  On a mismatch it FAILS and says what changed.

** WHAT A FAILURE MEANS, AND IT IS NOT THAT ANYTHING IS BROKEN. **  It means the corpus's float
comparisons have not been swept on this environment.  *The remedy is to run the tolerance sweep whole --
`python3 scripts/sweep_tolerances.py` -- repair or name what it flags, and then refresh this file.*  ⛔ It
is NOT to refresh the file: a fingerprint bumped without the sweep is exactly the vacuous green one level
up, and the same failure as a stamp moved without the prose it stands for.

⌗ *The interpreter is read at MAJOR.MINOR, not the patch -- on `PO-66` ⓶'s measurement, not on how patch
releases usually behave: the whole suite probed on two patch levels with everything else held moved no
comparison that a single interpreter does not also move between two of its own runs.*  The swept patch
is still recorded in the fingerprint file, beside the line this gate reads.

⌗ *The thread count is deliberately NOT in the fingerprint.*  It is set per run by the runner and by
whoever is at a terminal, and it varies legitimately -- which is why it belongs to the sweep's own
perturbation and not to a gate about the installed environment.  **The fingerprint answers "is this the
software we swept on", not "is this the invocation we swept with".**
"""
import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FP = os.path.join(ROOT, 'receipts', 'ENV_FINGERPRINT.txt')


def live():
    """The fields that decide round-off, each read from the installed package."""
    out = {}
    # ⛭ r7003+70.1 (node 70, PO-66 ⓶): MAJOR.MINOR only, ON A MEASUREMENT.  3.11.15 and 3.11.16, built from
    #   the same source with the same flags, numpy/scipy/BLAS identical, probed the whole suite (885
    #   receipts, 11,317 sites, 33,931 values): 4 sites differed, and all 4 differ run-to-run on ONE
    #   interpreter (a two-thread reduction, a set's order, a count of what a concurrent run left in the
    #   tree).  No comparison moved with the patch.  A MINOR move still fails here -- it is unmeasured.
    out['python'] = '.'.join(str(n) for n in sys.version_info[:2])
    try:
        import numpy as np
        out['numpy'] = np.__version__
        blas = None
        try:                                   # numpy >= 1.25
            d = np.__config__.show(mode='dicts')
            blas = (d.get('Build Dependencies', {}) or {}).get('blas', {}) or {}
        except Exception:
            blas = {}
        out['blas'] = f"{blas.get('name')} {blas.get('version')}"
    except Exception as e:                     # pragma: no cover -- numpy is a hard dependency
        out['numpy'] = f'UNREADABLE ({e})'
        out['blas'] = 'UNREADABLE'
    try:
        import scipy
        out['scipy'] = scipy.__version__
    except Exception as e:
        out['scipy'] = f'UNREADABLE ({e})'
    return out


def stored():
    if not os.path.exists(FP):
        return None
    txt = io.open(FP, encoding='utf-8', errors='replace').read()
    got = {}
    for k in ('python', 'numpy', 'scipy', 'blas'):
        m = re.search(rf'^{k}\s*=\s*(.+?)\s*$', txt, re.M)
        if m:
            got[k] = m.group(1)
    return got


def main():
    print()
    print('  ENVIRONMENT FINGERPRINT -- the trigger for PO-60\'s third class that no push can see')
    print()
    now, was = live(), stored()
    if was is None:
        print(f'  ⛔ NO FINGERPRINT IS COMMITTED at receipts/ENV_FINGERPRINT.txt.')
        print('     Run scripts/sweep_tolerances.py whole, then write the fingerprint it swept on.')
        return 1
    width = max(len(k) for k in now)
    bad = []
    for k in sorted(now):
        a, b = was.get(k), now[k]
        mark = 'same' if a == b else 'CHANGED'
        if a != b:
            bad.append((k, a, b))
        print(f'    {k:<{width}}  {b:<34} {mark}' + ('' if a == b else f'   (swept on: {a})'))
    print()
    if bad:
        print('  ⛔ THE ENVIRONMENT HAS MOVED SINCE THE TOLERANCE SWEEP:')
        for k, a, b in bad:
            print(f'       {k}: {a} -> {b}')
        print('     ⇒ every float comparison in the corpus was last swept on the OLD build, so the')
        print('       machine-dependent-tolerance class is unswept here.  Run')
        print('       `python3 scripts/sweep_tolerances.py` whole, repair or name what it flags, and')
        print('       then refresh receipts/ENV_FINGERPRINT.txt with what it swept on.')
        print('     ⛔ Refreshing the file without running the sweep is the vacuous green one level up.')
        return 1
    print('  the environment is the one the tolerance sweep was last run on.')
    print('  ⌗ Thread count is deliberately absent: that is the sweep\'s own perturbation, not the')
    print('    installed environment, and it varies legitimately between the runner and a terminal.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
