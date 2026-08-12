#!/usr/bin/env python3
"""check_depth.py -- THE DEPTH LINT: a statistic read off a spectrum shallower than the deepest run
of the same arm is a statistic about the depth.

** WHY THIS EXISTS, and it is the fork's finding rather than this line's. **  c54.190 retracted the
headline of its own previous three revisions:

  "c54.187, c54.188 and c54.189 all ran at LMAXL = 1000 so that eighteen datum readings and five pins
   were affordable.  ** At that depth the CR arm has FOUR peaks, so 'the mean peak spacing' was a mean
   of THREE GAPS --- and the first three gaps are the only ones where the two arms disagree. **
   ⇒ At production depth both arms carry EIGHT peaks and the CR arm's asymptotic spacing is 0.975 of
   l_A against the control's 1.002 --- ** 2.5% short, not 21%. **"

And it routed the general shape here:

  "** A quantity measured at the depth an experiment can afford, then named as though it were the
   quantity itself, is the shape of this error ** --- and the corpus already holds the same shape
   twice: c54.176 (a target below the resolution of its own statistic) and c54.164 (a figure not
   stable under its own stated conditions).  ** Three instances is a pattern, and I do not know what
   gate catches it. **"

** ⛭⛭ AND THIS ONE IS GATEABLE, WHICH IS WHY IT IS BUILT AND THE OTHER THREE REQUESTS WERE NOT. **

L-237's rule: ** every gate checks something SOMEBODY DECLARED. **  Three earlier requests --- the
arrival-path metric, the prose-duplicate scanner, the travelling-finding detector --- each needed a
declaration the corpus does not carry, and each was answered with a convention or a refusal.

*** HERE THE DECLARATION ALREADY EXISTS AND IS MACHINE-READABLE: every spectrum carries its own `ls`
    array, so its l range is declared IN THE FILE, and the peak count inside that range is a
    computation. ***

** THE CHECK. **  For each arm, find the greatest number of peaks any spectrum of that arm resolves.
Any spectrum resolving FEWER is SHALLOW for that arm, and ** any peak-derived statistic read off it is
a statement about that spectrum's depth and not about the arm. **

** ⚠ IT IS A LINT AND NOT A GATE, DELIBERATELY. **  A shallow spectrum is not a defect --- c54.187's
eighteen readings were only affordable at LMAXL = 1000 and the scan was right to run there.  ** The
defect is quoting an asymptotic quantity from one, and no script can see which quantity a human
quoted. **  So this reports and never fails the turn, exactly as `check_loci` and `scope_table` do,
and for the same stated reason: ** a gate can check a declaration, it cannot check a judgement. **

    python3 corpus/check_depth.py            # report
    python3 corpus/check_depth.py --verbose  # every spectrum, with its depth and peak count

Written r2484.  Stated for reversal.
"""
import os
import sys
import glob
import collections

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')


def survey():
    rows, unreadable = [], []
    for f in sorted(glob.glob(os.path.join(SP, '*.npz'))):
        z = np.load(f)
        if 'ls' not in z or 'Dl' not in z:
            # ** not every file in this directory is a C_l spectrum -- the lensing-potential run
            # carries Phi/cl/k instead.  SKIP AND SAY SO rather than crash or silently drop it. **
            unreadable.append((os.path.basename(f), sorted(z.keys())))
            continue
        ls, Dl = z['ls'], z['Dl']
        arm = str(z['arm']) if 'arm' in z else (
            'lcdm' if 'lcdm' in os.path.basename(f) else 'cr')
        arm = 'lcdm' if 'lcdm' in arm.lower() else 'cr'
        pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
        rows.append((os.path.basename(f), arm, int(ls.max()), len(pk)))
    return rows, unreadable


def main():
    verbose = '--verbose' in sys.argv
    rows, unreadable = survey()
    print()
    print('  check_depth -- a statistic read off a shallow spectrum is a statistic about the depth')
    print()
    if not rows:
        print('  no spectra found; nothing to report.')
        return 0

    best = collections.defaultdict(int)
    for _, arm, _, n in rows:
        best[arm] = max(best[arm], n)
    print('  deepest peak count resolved, per arm: '
          + ', '.join(f'{a}={n}' for a, n in sorted(best.items())))
    print()

    if verbose:
        for nm, arm, lm, n in rows:
            flag = '  <- SHALLOW' if n < best[arm] else ''
            print(f'    {nm:<40} arm={arm:<5} l_max={lm:<6} peaks={n}{flag}')
        print()

    shallow = [r for r in rows if r[3] < best[r[1]]]
    print(f'  {len(shallow)} of {len(rows)} spectra resolve FEWER peaks than the deepest run '
          f'of their own arm.')
    if shallow:
        # ** group by the SOURCE the file names, not by its first underscore field: the
        # lcdm_<number> scan has no revision prefix and grouping on field 0 labelled eight of
        # them "lcdm×8" as though that were a revision.  The FLAG was right; the LABEL was not. **
        def src(nm):
            return nm.split('_')[0] if nm.startswith('c54.') else nm.rsplit('_', 1)[0] + '_*'
        by = collections.Counter(src(nm) for nm, _, _, _ in shallow)
        print('     by source: ' + ', '.join(f'{k}×{v}' for k, v in sorted(by.items())))
        print()
        print('  ⚠ ** ANY PEAK-DERIVED STATISTIC READ OFF THESE IS A STATEMENT ABOUT THEIR DEPTH.**')
        print('     A shallow run is not a defect -- it is often the only affordable one.')
        print('     ** The defect is quoting an ASYMPTOTIC quantity from one, and no script can see')
        print('     which quantity a human quoted. **')

    if unreadable:
        print()
        print(f'  ⌗ {len(unreadable)} file(s) in the directory are not C_l spectra and were skipped:')
        for nm, keys in unreadable:
            print(f'     {nm}  (keys: {", ".join(keys)})')

    print()
    print('  ⌗ LINT, NOT A GATE: reports and never fails the turn, like check_loci and scope_table,')
    print('    and for the same reason -- ** a gate can check a declaration, not a judgement. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
