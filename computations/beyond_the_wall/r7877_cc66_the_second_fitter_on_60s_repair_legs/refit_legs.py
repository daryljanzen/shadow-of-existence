# -*- coding: utf-8 -*-
"""r7877+cc66 item ⑮ -- THE SECOND FITTER ON `60`'s BANKED REPAIR LEGS.

`69`: *"A repair is accepted on two fitters, not one."*  `r7875` was this seat's first pass and
agreed with `60` to `3e-06` on the LANDED instrument.  This applies the same instrument to the
repair legs `60` have banked.

⛔ ONLY TWO LEGS ARE BANKED.  `60`'s `r7876/nupert/` holds the Fermi-Dirac fluid repair ON and OFF at
   `Σ = 0.30` and `0.60`.  The FOUR decomposition legs `69` names -- weight alone, continuity alone,
   Euler alone, the `c_a²` variant -- are NOT there; `69` ordered `60` to make them this round.  That
   half of ⑮ waits, and nothing is invented for it.

⌗ THE ZERO LEG IS THE LANDED ONE, which is `60`'s own choice and their stated reason: `NUFD` is gated
  on a non-zero sum, so the repair is provably inert at `Σ = 0`.  I take the same zero leg rather
  than a different one, because a ratio against a different denominator is a different quantity.

⛔ THE REGRESSION CONTROL GATES EVERYTHING.  This file IMPORTS `r7875`'s fitter and CAMB leg rather
   than re-implementing them, and first re-derives `r7875`'s four landed amplitudes.  ** If the
   instrument has drifted, its numbers for the new legs would be unattributable. **

    NODE=cc66 python3 refit_legs.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
R7875 = os.path.join(_BTW, 'r7875_cc66_the_independent_check_of_the_amplitude_and_the_branch_'
                           'scan_across_the_sums')
R7876 = os.path.join(_BTW, 'r7876_60_the_epoch_consistent_neutrino_perturbations_and_whether_'
                           'the_amplitude_excess_is_the_lean')
sys.path.insert(0, R7875)
import amplitude_check as AC                                                # noqa: E402

NUP = os.path.join(R7876, 'nupert')
LANDED_ZERO = os.path.join(AC.BANK, 'lcdm_S000.npz')
OUT = os.path.join(_HERE, 'refit_legs.json')

LEGS = ('shear_on', 'shear_off')
SUFFIX = {'shear_on': 'on', 'shear_off': 'off'}
SUMS = (0.30, 0.60)
BLOCKS = ('TT', 'EE')
KEY = {'TT': 'Dl', 'EE': 'Dl_EE'}

# 60's own figures, from their refit.json, as the registered expectation
TARGET = {
    ('shear_on', 'TT', 0.30): 0.8640089087, ('shear_on', 'TT', 0.60): 0.8146639734,
    ('shear_on', 'EE', 0.30): 0.9447357702, ('shear_on', 'EE', 0.60): 0.9112041475,
    ('shear_off', 'TT', 0.30): 0.8602539020, ('shear_off', 'TT', 0.60): 0.8110274011,
    ('shear_off', 'EE', 0.30): 0.9447351664, ('shear_off', 'EE', 0.60): 0.9112137927,
}
R7875_LANDED = {('TT', 0.30): 1.151621417168135, ('TT', 0.60): 1.2959211454888449,
                ('EE', 0.30): 1.0140591924745146, ('EE', 0.60): 1.0463071504477712}
EE_BAND = 0.05


def _npz(path, key):
    with np.load(path, allow_pickle=True) as z:
        return np.asarray(z[key], float)


def leg_ratio(leg, s, blk):
    """r_inst on 60's own multipoles, against the LANDED zero leg as 60 do"""
    p = os.path.join(NUP, 'lcdm_S%03d%s_pol.npz' % (int(round(s * 100)), SUFFIX[leg]))
    if not os.path.exists(p):
        return None, None
    ls = _npz(LANDED_ZERO, 'ls').astype(int)
    d0 = _npz(LANDED_ZERO, KEY[blk])
    ds = _npz(p, KEY[blk])
    m = (ls >= AC.L_LO) & (ls <= AC.L_HI)
    return ls[m].astype(float), (ds / d0 - 1.0)[m]


def main():
    print(__doc__)
    print('=' * 100)
    con = AC.control()
    print('\n  Ⓐ① control read at run time: %s;  tau %.3f, lmax %d, band %d-%d, 60\'s multipoles'
          % (con, AC.TAU, AC.LMAX, AC.L_LO, AC.L_HI))
    out = {'control': con, 'tau': AC.TAU, 'lmax': AC.LMAX, 'window': [AC.L_LO, AC.L_HI],
           'legs_banked': [], 'legs_missing': [], 'ee_band': EE_BAND}

    for want in ('weight', 'continuity', 'euler', 'c_a2'):
        out['legs_missing'].append(want)
    print('\n  ⛔ THE FOUR DECOMPOSITION LEGS ARE NOT BANKED: %s'
          % ', '.join(out['legs_missing']))
    print('     69 ordered 60 to produce them this round, so that half of the item waits.')

    CA, CL = {}, {}
    for s in (0.0,) + SUMS:
        CA[s], CL[s], _ = AC.camb_one(con, s)
    l_dense = np.arange(2, AC.LMAX + 1, dtype=float)
    g = np.linspace(-0.08, 0.08, 3201)

    # ── Ⓑ② the regression control ──
    print('\n  Ⓑ② THE REGRESSION CONTROL -- does this harness still give `r7875`\'s landed four?')
    reg, worst = {}, 0.0
    for blk in BLOCKS:
        for s in SUMS:
            ls = AC.bank_arr(AC.TAGS[0.0], 'ls')
            r_i = AC.bank_arr(AC.TAGS[s], KEY[blk]) / AC.bank_arr(AC.TAGS[0.0], KEY[blk]) - 1.0
            m = (ls >= AC.L_LO) & (ls <= AC.L_HI)
            rc = CA[s][2:AC.LMAX + 1, AC.COL[blk]] / CA[0.0][2:AC.LMAX + 1, AC.COL[blk]] - 1.0
            e0 = AC.fit_A_eps(ls[m].astype(float), r_i[m], l_dense, rc, g)[0]
            _, A, _ = AC.refine(ls[m].astype(float), r_i[m], l_dense, rc, e0)
            d = abs(A - R7875_LANDED[(blk, s)])
            worst = max(worst, d)
            reg['%s|%.2f' % (blk, s)] = dict(A=float(A), r7875=R7875_LANDED[(blk, s)],
                                             diff=float(d))
            print('      %s %.2f: %.10f against r7875\'s %.10f   |d| %.2e'
                  % (blk, s, A, R7875_LANDED[(blk, s)], d))
    out['regression'] = reg
    out['regression_worst'] = float(worst)
    ok = worst < 1e-9
    print('      ⇒ worst %.3e   %s' % (worst, 'PASSES the 1e-9 band' if ok else '⛔ FAILS'))
    if not ok:
        print('\n  ⛔ THE HARNESS HAS DRIFTED SINCE r7875, so no leg is read.')
        out['legs_read'] = False
        io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
        return

    # ── Ⓔ⑤ the planted-recovery control ──
    print('\n  Ⓔ⑤ THE PLANTED-RECOVERY CONTROL')
    rc6 = CA[0.60][2:AC.LMAX + 1, 0] / CA[0.0][2:AC.LMAX + 1, 0] - 1.0
    lobs = np.arange(AC.L_LO, AC.L_HI + 1, dtype=float)
    pl = {}
    for A_p, e_p in ((0.85, 0.0055), (1.25, -0.0020)):
        planted = A_p * np.interp(lobs * (1.0 + e_p), l_dense, rc6)
        e_h, A_h, _ = AC.refine(lobs, planted, l_dense, rc6,
                                AC.fit_A_eps(lobs, planted, l_dense, rc6, g)[0])
        pl['A%.2f' % A_p] = dict(A_true=A_p, A_fit=float(A_h), dA=float(abs(A_h - A_p)))
        print('      planted A %.2f eps %+.4f -> A %.8f eps %+.6f  |dA| %.2e  %s'
              % (A_p, e_p, A_h, e_h, abs(A_h - A_p), 'OK' if abs(A_h - A_p) < 1e-3 else '⛔'))
    out['planted'] = pl
    out['planted_ok'] = bool(all(v['dA'] < 1e-3 for v in pl.values()))

    # ── Ⓓ④ the two banked legs ──
    print('\n  Ⓓ④ THE TWO BANKED LEGS, against 60\'s own figures')
    fits = {}
    for leg in LEGS:
        for blk in BLOCKS:
            for s in SUMS:
                lo, r_i = leg_ratio(leg, s, blk)
                if lo is None:
                    print('      %s %s %.2f: NOT BANKED' % (leg, blk, s))
                    continue
                rc = CA[s][2:AC.LMAX + 1, AC.COL[blk]] / CA[0.0][2:AC.LMAX + 1, AC.COL[blk]] - 1.0
                e0 = AC.fit_A_eps(lo, r_i, l_dense, rc, g)[0]
                e, A, res = AC.refine(lo, r_i, l_dense, rc, e0)
                tgt = TARGET[(leg, blk, s)]
                d = abs(A - tgt)
                fits['%s|%s|%.2f' % (leg, blk, s)] = dict(
                    A=float(A), eps=float(e), resid=float(res), target_60=tgt,
                    diff_from_60=float(d), hits=bool(d < 0.005),
                    n_multipoles=int(lo.size), dist_from_unity=float(abs(A - 1.0)))
                print('      %-9s %s %.2f: A %.8f  eps %+.6f  (60: %.8f, |d| %.2e)  %s'
                      % (leg, blk, s, A, e, tgt, d, 'MATCHES' if d < 0.005 else '⛔ MISSES'))
                if leg not in out['legs_banked']:
                    out['legs_banked'].append(leg)
    out['fits'] = fits
    out['legs_read'] = True
    out['n_hits'] = sum(1 for v in fits.values() if v['hits'])

    # ── Ⓕ⑥ EE against its band ──
    print('\n  Ⓕ⑥ EE AGAINST ITS OWN BAND of %.2f, which 69 ruled a constraint' % EE_BAND)
    ee = {}
    for k, v in sorted(fits.items()):
        if '|EE|' in k:
            ee[k] = dict(dist=v['dist_from_unity'], outside=bool(v['dist_from_unity'] > EE_BAND))
            print('      %-20s |A - 1| = %.6f  %s the %.2f band'
                  % (k, v['dist_from_unity'],
                     'OUTSIDE' if v['dist_from_unity'] > EE_BAND else 'inside', EE_BAND))
    out['ee_vs_band'] = ee

    # ── Ⓖ⑦ the direction: has the repair changed the sign of the discrepancy? ──
    print('\n  Ⓖ⑦ THE DIRECTION -- the landed instrument is ABOVE CAMB, the repair is BELOW')
    dirn = {}
    for blk in BLOCKS:
        for s in SUMS:
            land = R7875_LANDED[(blk, s)]
            for leg in LEGS:
                k = '%s|%s|%.2f' % (leg, blk, s)
                if k not in fits:
                    continue
                a = fits[k]['A']
                dirn[k] = dict(landed=land, repaired=a,
                               landed_dist=float(abs(land - 1.0)),
                               repaired_dist=float(abs(a - 1.0)),
                               nearer_unity=bool(abs(a - 1.0) < abs(land - 1.0)),
                               sign_flipped=bool((land - 1.0) * (a - 1.0) < 0))
            k = '%s|%s|%.2f' % ('shear_on', blk, s)
            if k in dirn:
                v = dirn[k]
                print('      %s %.2f  landed %.6f (%.6f from 1) -> repaired %.6f (%.6f from 1)'
                      '  nearer %s, sign flipped %s'
                      % (blk, s, v['landed'], v['landed_dist'], v['repaired'],
                         v['repaired_dist'], v['nearer_unity'], v['sign_flipped']))
    out['direction'] = dirn

    # ── Ⓗ⑧ can the fitter separate the two legs at all? ──
    print('\n  Ⓗ⑧ CAN THIS FITTER SEPARATE THE TWO LEGS? -- registered AT RISK for EE')
    sep = {}
    for blk in BLOCKS:
        for s in SUMS:
            a = fits.get('shear_on|%s|%.2f' % (blk, s))
            b = fits.get('shear_off|%s|%.2f' % (blk, s))
            if not (a and b):
                continue
            mine = abs(a['A'] - b['A'])
            theirs = abs(TARGET[('shear_on', blk, s)] - TARGET[('shear_off', blk, s)])
            # r7875's own interpolation sensitivity for this block
            floor = 5.307332502169082e-05 if blk == 'EE' else 3.515263913511646e-06
            sep['%s|%.2f' % (blk, s)] = dict(mine=float(mine), theirs=float(theirs),
                                             my_floor=float(floor),
                                             resolvable=bool(mine > floor))
            print('      %s %.2f: on-off is %.3e by my fitter, %.3e by 60\'s; my own floor is '
                  '%.3e ⇒ %s' % (blk, s, mine, theirs, floor,
                                 'RESOLVABLE' if mine > floor else
                                 '⛔ BELOW MY FLOOR -- an agreement here says nothing about the leg'))
    out['separation'] = sep

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n' + '=' * 100)
    print('  %d of %d banked fits reproduce 60\'s A to 0.005' % (out['n_hits'], len(fits)))
    print('  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
