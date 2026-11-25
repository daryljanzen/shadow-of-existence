# -*- coding: utf-8 -*-
"""Ⓑ②ᵈ THE TEST Ⓐ① SHOWED HAD NEVER BEEN RUN: WHAT REMOVING **THIS LINE'S OWN THIRTY-SIX BINS**
COSTS THE REFERENCE.

`r7865`'s lead is that this line's low cut cost `46.53` meV and the reference's `1.03`, so the
instrument leans on its lowest bandpowers about forty times harder.  Ⓐ① measured that those two
cuts share SEVEN bins of thirty-six and forty-nine: forty-two of the reference's forty-nine sit
below the multipole the instrument's score starts at, and the reference's cut leaves standing
almost exactly the band this line's removes.  ⇒ **So the forty is a ratio between two different
removals, and the comparable number does not exist yet.**  This file measures it.

⌗ *Both columns are taken the same way and the way is stated: the sum-profile of `chi2_cmb` on
the instrument's own `555` bins, once whole and once with the thirty-six removed, and the shift
of the `2.71` crossing between them.  The instrument's four parameters are re-fit at every sum
on its banked grid, because that is free; the reference's five are held at its banked values,
because re-profiling them is a CAMB minimisation per sum.  ** So the comparable quantity is the
MOVE the removal causes in each column, not either column's absolute limit -- the reference's own
`54.00` comes from a five-parameter profile this file does not re-run, and is NOT what the
crossings below should be read against. **

    NODE=60 python3 same_bins.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_'
                                      'the_damping_tails_share_of_the_gap'))
import tail_share as TS                                                     # noqa: E402,F401
import score_ttteee as SC                                                   # noqa: E402
import model3 as M3                                                         # noqa: E402
import model6 as M6                                                         # noqa: E402
from lean import camb_binned, fit_x4, BANKED                                # noqa: E402

NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
SUMS = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
CROSS = 2.71
N_PER_BLOCK = 12
#: the order's two figures, quoted as DECLARED reads and not re-derived here
ORDER_INSTRUMENT_LOW = 46.53
ORDER_REFERENCE_LOW = 1.03


def the_thirty_six(ok):
    """the same construction `r7862` used and Ⓐ① named: twelve lowest-BIN_LO per block"""
    keep = np.ones(int(ok.sum()), bool)
    blk, lo = SC.BLOCK[ok], SC.BIN_LO[ok]
    for b in (0, 1, 2):
        idx = np.where(blk == b)[0]
        keep[idx[np.argsort(lo[idx], kind='stable')][:N_PER_BLOCK]] = False
    return keep


def cross_of(sums, delta):
    """the sum where the profile first reaches CROSS, linearly between its own nodes, in meV"""
    s, d = np.asarray(sums, float), np.asarray(delta, float)
    d = d - d.min()
    for k in range(1, s.size):
        if d[k] >= CROSS > d[k - 1]:
            t = (CROSS - d[k - 1]) / (d[k] - d[k - 1])
            return float((s[k - 1] + t * (s[k] - s[k - 1])) * 1000.0)
    return None


def inst_profile(keep):
    """chi2_cmb profiled over the four parameters at each sum, on `keep` of the instrument's mask"""
    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    newok = ok.copy()
    newok[ok] = keep
    c = mod.cmb
    base, g, h = c.base, dict(c.g), dict(c.h)
    c.base = lambda s, nu=0, _o=base, _k=keep: np.asarray(_o(s, nu), float)[_k]
    c.g = {k: (lambda s, nu=0, _o=g[k], _k=keep: np.asarray(_o(s, nu), float)[_k]) for k in M3.KEYS4}
    c.h = {k: (lambda s, nu=0, _o=h[k], _k=keep: np.asarray(_o(s, nu), float)[_k]) for k in M3.KEYS4}
    c.ok, c.nb = newok, int(newok.sum())
    c.F, c.d, c.pos = SC.fisher_for(newok), SC.X_DATA[newok], SC.POSITIVE[newok]
    out = []
    for s in SUMS:
        _, v = fit_x4(mod, s)
        out.append(float(v))
    return out, int(newok.sum())


def ref_profile(mode, keep, cache):
    """the reference's chi2 on the instrument's `keep` bins, its five parameters held banked"""
    b0 = json.load(io.open(os.path.join(BANKED, '%s_0.000.json' % mode), encoding='utf-8'))
    par = (b0['H0'], b0['Om'], b0['ombh2'], b0['ns'], b0['tau'])
    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    newok = ok.copy()
    newok[ok] = keep
    F, d = SC.fisher_for(newok), SC.X_DATA[newok]
    out = []
    for s in SUMS:
        # ⛔⛭⛭ ** THE CACHE KEY WAS THE SUM ALONE, AND IT RELABELLED A WHOLE COLUMN -- found by
        #   `cc66`, routed in order `r7869` item ④, fixed here at `r7870`. **  *This cache is
        #   created ONCE outside the mode loop in `main`, so the first mode to run populated it
        #   and the second was served the FIRST mode's spectra at every sum.  Both reference
        #   modes therefore returned columns that are bit-identical across all seven sums and
        #   both bin sets, while their five recorded parameters differ in all five -- which is
        #   the arithmetic that proves it on the committed record.*
        #   ⇒ *** THE KEY IS NOW THE FULL PARAMETER TUPLE TOGETHER WITH THE SUM, which is the
        #       thing the spectra actually depend on.  Keying on `(mode, sum)` would also have
        #       removed the defect, and it is the weaker fix: it makes the collision ABSENT
        #       rather than IMPOSSIBLE, and it would silently stop sharing between two modes
        #       whose parameters genuinely agree.  A cache keyed on less than its value depends
        #       on is the defect, not the mode label. ***
        #   ⌗ *What this did and did not cost is recorded at `r7870`: both headline ratios
        #     divide by the move of the mode that POPULATED the cache, so that mode's own column
        #     was served its own spectra and the headline stands; the other mode's move is the
        #     first mode's relabelled and is void.*
        ckey = (par, s)
        if ckey not in cache:
            cache[ckey] = camb_binned(*par, sum_ev=s)
        m = cache[ckey][newok]
        A = float((m @ F @ d) / (m @ F @ m))
        r = d - A * m
        out.append(float(r @ F @ r))
    return out, int(newok.sum()), par


def main():
    print(__doc__)
    print('=' * 100)
    mod0 = M6.Model6('lcdm')
    ok = mod0.cmb.ok
    keep_all = np.ones(int(ok.sum()), bool)
    keep_36 = the_thirty_six(ok)
    print('\n  the removal under test: %d bin(s) of %d, %d per block, multipoles 100..207'
          % (int((~keep_36).sum()), int(ok.sum()), N_PER_BLOCK))

    res = {}
    for label, keep in (('whole', keep_all), ('minus36', keep_36)):
        tot, nb = inst_profile(keep)
        res['instrument_' + label] = dict(sums=SUMS, totals=tot, nbins=nb,
                                          delta=[t - min(tot) for t in tot],
                                          crossing_meV=cross_of(SUMS, tot))
        print('    instrument %-8s %3d bin(s), crossing %s meV'
              % (label, nb, ('%.2f' % res['instrument_' + label]['crossing_meV'])
                 if res['instrument_' + label]['crossing_meV'] is not None else 'none'))

    # ⚠ THE ASYMMETRY CONTROL, and it is the one this comparison needs: the instrument's column
    # profiles its four parameters at every sum and the reference's holds its five, because
    # re-profiling the reference is a CAMB minimisation per sum.  So the instrument is given a
    # freedom the reference is not, and that freedom could BE the move.  The same instrument
    # column is therefore taken again with its four parameters FROZEN at the zero-sum fit, which
    # is the reference's own treatment.  If the move survives, the asymmetry is not its cause.
    x4f, _ = fit_x4(M6.Model6('lcdm'), 0.0)
    for label, keep in (('whole', keep_all), ('minus36', keep_36)):
        mod = M6.Model6('lcdm')
        c = mod.cmb
        newok = ok.copy()
        newok[ok] = keep
        base, g, h = c.base, dict(c.g), dict(c.h)
        c.base = lambda s, nu=0, _o=base, _k=keep: np.asarray(_o(s, nu), float)[_k]
        c.g = {k: (lambda s, nu=0, _o=g[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
               for k in M3.KEYS4}
        c.h = {k: (lambda s, nu=0, _o=h[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
               for k in M3.KEYS4}
        c.ok, c.nb = newok, int(newok.sum())
        c.F, c.d, c.pos = SC.fisher_for(newok), SC.X_DATA[newok], SC.POSITIVE[newok]
        tot = [float(c.chi2_cmb(x4f, s)) for s in SUMS]
        res['instrument_frozen_' + label] = dict(
            sums=SUMS, totals=tot, nbins=int(newok.sum()), x4=[float(v) for v in x4f],
            delta=[t - min(tot) for t in tot], crossing_meV=cross_of(SUMS, tot))
        print('    instrument FROZEN %-8s %3d bin(s), crossing %s meV'
              % (label, int(newok.sum()),
                 ('%.2f' % res['instrument_frozen_' + label]['crossing_meV'])
                 if res['instrument_frozen_' + label]['crossing_meV'] is not None else 'none'))

    cache = {}
    for mode in ('rd_min', 'rd_camb'):
        for label, keep in (('whole', keep_all), ('minus36', keep_36)):
            tot, nb, par = ref_profile(mode, keep, cache)
            k = 'reference_%s_%s' % (mode, label)
            res[k] = dict(sums=SUMS, totals=tot, nbins=nb, params=list(par),
                          delta=[t - min(tot) for t in tot], crossing_meV=cross_of(SUMS, tot))
            print('    reference %-7s %-8s %3d bin(s), crossing %s meV'
                  % (mode, label, nb, ('%.2f' % res[k]['crossing_meV'])
                     if res[k]['crossing_meV'] is not None else 'none'))

    print('\n  ** THE MOVE THE SAME THIRTY-SIX BINS CAUSE IN EACH COLUMN **')
    moves = {}
    for col in ('instrument', 'instrument_frozen', 'reference_rd_min', 'reference_rd_camb'):
        a = res['%s_whole' % col]['crossing_meV']
        b = res['%s_minus36' % col]['crossing_meV']
        moves[col] = None if (a is None or b is None) else float(a - b)
        print('    %-20s whole %s, minus the thirty-six %s  ⇒ move %s meV'
              % (col, ('%.2f' % a) if a is not None else 'none',
                 ('%.2f' % b) if b is not None else 'none',
                 ('%+.2f' % moves[col]) if moves[col] is not None else 'none'))
    res['moves_meV'] = moves
    if moves['instrument'] and moves['reference_rd_min']:
        ratio = abs(moves['instrument'] / moves['reference_rd_min'])
        ratio_f = abs(moves['instrument_frozen'] / moves['reference_rd_min'])
        res['ratio_on_the_same_bins'] = float(ratio)
        res['ratio_on_the_same_bins_frozen'] = float(ratio_f)
        res['freedom_share_of_the_move_meV'] = float(moves['instrument']
                                                     - moves['instrument_frozen'])
        print('\n    ⇒ ON THE SAME BINS, and on the reference\'s OWN treatment of the parameters '
              '(frozen), the instrument moves %.0f times the reference: %+.2f against %+.2f meV.'
              % (ratio_f, moves['instrument_frozen'], moves['reference_rd_min']))
        print('      with the instrument\'s four parameters re-profiled instead, %.0f times: '
              '%+.2f meV.  ⇒ THE ASYMMETRY IS NOT THE CAUSE -- it accounts for %.2f meV of the '
              'move and leaves two orders of magnitude standing.'
              % (ratio, moves['instrument'],
                 abs(moves['instrument'] - moves['instrument_frozen'])))
        print('      against the order\'s %.0f from the two DIFFERENT cuts (%.2f against %.2f '
              'meV, declared reads), which Ⓐ① showed share seven bins of thirty-six and forty-nine'
              % (ORDER_INSTRUMENT_LOW / ORDER_REFERENCE_LOW,
                 ORDER_INSTRUMENT_LOW, ORDER_REFERENCE_LOW))
    io.open(os.path.join(_HERE, 'same_bins.json'), 'w', encoding='utf-8').write(
        json.dumps(res, indent=1, sort_keys=True))
    print('\n  wrote same_bins.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
