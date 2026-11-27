# -*- coding: utf-8 -*-
"""r7885+cc66 item ⑰ -- THE SECOND FIT ON `60`'s r7882 VALIDATION LEGS.

Three legs, `base`, `nq24`, `lmax18`; TT and EE at `Σ = 0.30` and `0.60` eV; twelve fits against
`60`'s own twelve figures, on `60`'s `41` in-band multipoles, with this seat's own CAMB leg and
fitter -- as at ⑬ and ⑮.

⛔ THE SAME INSTRUMENT.  This imports `r7875`'s fitter and CAMB leg THROUGH `r7879`, which imports
   it through `r7877`, rather than re-implementing any of it, and re-derives `r7875`'s four landed
   amplitudes before a validation leg is read.

⛔ THE ZERO LEG IS SHARED AND THAT IS A FACT, NOT A CHOICE.  `lcdm_S000_pol.npz` and
   `lcdm_S000_tt.npz` are BYTE-IDENTICAL across all three legs, so the convergence switch is
   provably inert at `Σ = 0`.  The identity is checked here rather than assumed.

⛔ AND THE LEGS ARE CONVERGENCE VARIANTS, SO THE FLOOR DECIDES WHAT AN AGREEMENT IS WORTH.
   PREDICTION.md registered, before any fit, that `base`-`lmax18` in EE at both sums would fall
   BELOW this seat's own EE interpolation floor and so would confirm the bank reading, not the leg.

    NODE=cc66 python3 valid_legs.py
"""
import hashlib
import io
import itertools
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
R7879 = os.path.join(_BTW, 'r7879_cc66_the_decomposition_legs_and_cambs_own_hierarchy_reference')
R7882 = os.path.join(_BTW, 'r7882_60_the_massive_species_own_boltzmann_hierarchy')
sys.path.insert(0, R7879)
import legs_five as LF                                                      # noqa: E402
RL, AC = LF.RL, LF.AC

VALID = os.path.join(R7882, 'valid')
OUT = os.path.join(_HERE, 'valid_legs.json')
LEGS = ('base', 'nq24', 'lmax18')
SUMS = (0.30, 0.60)
BLOCKS = ('TT', 'EE')
KEY = LF.KEY
BAR = LF.BAR                        # 0.03, 69's joint bar, unchanged
FLOOR = LF.FLOOR                    # this seat's own r7875 interpolation floors
TOL = 5e-05                         # the reproduction tolerance REGISTERED at r7885+cc66.1

TARGET = {
    ('base',   'TT', 0.30): 0.9891418529, ('base',   'TT', 0.60): 0.9788502587,
    ('base',   'EE', 0.30): 0.9805523438, ('base',   'EE', 0.60): 0.9773976912,
    ('nq24',   'TT', 0.30): 0.9899863000, ('nq24',   'TT', 0.60): 0.9792040229,
    ('nq24',   'EE', 0.30): 0.9808176001, ('nq24',   'EE', 0.60): 0.9775688622,
    ('lmax18', 'TT', 0.30): 0.9891807779, ('lmax18', 'TT', 0.60): 0.9788775687,
    ('lmax18', 'EE', 0.30): 0.9805525020, ('lmax18', 'EE', 0.60): 0.9773980281,
}


def _sha(p):
    return hashlib.sha256(io.open(p, 'rb').read()).hexdigest()


def leg_ratio(leg, s, blk):
    """`60`'s banked ratio for one leg/sum/block, on the leg's OWN shared zero."""
    z = os.path.join(VALID, leg, 'lcdm_S000_pol.npz')
    p = os.path.join(VALID, leg, 'lcdm_S%03d_pol.npz' % int(round(s * 100)))
    if not os.path.exists(p):
        return None, None
    ls = RL._npz(z, 'ls').astype(int)
    d0 = RL._npz(z, KEY[blk])
    ds = RL._npz(p, KEY[blk])
    m = (ls >= AC.L_LO) & (ls <= AC.L_HI)
    return ls[m].astype(float), (ds / d0 - 1.0)[m]


def main():
    print(__doc__)
    print('=' * 100)
    con = AC.control()
    out = {'control': con, 'legs': list(LEGS), 'bar': BAR, 'floors': FLOOR, 'tol': TOL,
           'window': [AC.L_LO, AC.L_HI], 'absent': []}
    print('\n  Ⓐ① control %s; band %d-%d; 60\'s 41 multipoles; three legs %s'
          % (con, AC.L_LO, AC.L_HI, ', '.join(LEGS)))

    # ── Ⓐ①b the shared zero leg, checked rather than assumed ──
    shas = {}
    for leg in LEGS:
        for f in ('lcdm_S000_pol.npz', 'lcdm_S000_tt.npz'):
            shas.setdefault(f, {})[leg] = _sha(os.path.join(VALID, leg, f))
    zero_shared = all(len(set(d.values())) == 1 for d in shas.values())
    out['zero_leg_byte_identical_across_legs'] = bool(zero_shared)
    out['zero_leg_sha'] = {f: sorted(set(d.values()))[0][:16] for f, d in shas.items()}
    print('\n  Ⓐ①b THE SHARED ZERO LEG: byte-identical across all three legs -> %s'
          % ('YES, so the switch is inert at Σ=0' if zero_shared else '⛔ NO'))
    for f, d in sorted(out['zero_leg_sha'].items()):
        print('       %-22s %s' % (f, d))

    CA = {}
    for s in (0.0,) + SUMS:
        CA[s], _, _ = AC.camb_one(con, s)
    l_dense = np.arange(2, AC.LMAX + 1, dtype=float)
    g = np.linspace(-0.08, 0.08, 3201)

    # ── Ⓕ⑥ the regression control, before any validation leg is read ──
    print('\n  Ⓕ⑥ THE REGRESSION CONTROL -- r7875\'s four landed amplitudes, re-derived here')
    worst_reg = 0.0
    for blk in BLOCKS:
        for s in SUMS:
            ls = AC.bank_arr(AC.TAGS[0.0], 'ls')
            r_i = AC.bank_arr(AC.TAGS[s], KEY[blk]) / AC.bank_arr(AC.TAGS[0.0], KEY[blk]) - 1.0
            m = (ls >= AC.L_LO) & (ls <= AC.L_HI)
            rc = CA[s][2:AC.LMAX + 1, AC.COL[blk]] / CA[0.0][2:AC.LMAX + 1, AC.COL[blk]] - 1.0
            e0 = AC.fit_A_eps(ls[m].astype(float), r_i[m], l_dense, rc, g)[0]
            _, A, _ = AC.refine(ls[m].astype(float), r_i[m], l_dense, rc, e0)
            worst_reg = max(worst_reg, abs(A - RL.R7875_LANDED[(blk, s)]))
    out['regression_worst'] = float(worst_reg)
    print('      worst %.3e   %s' % (worst_reg, 'PASSES' if worst_reg < 1e-9 else '⛔ FAILS'))
    if worst_reg >= 1e-9:
        out['legs_read'] = False
        io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
        return

    # ── Ⓑ② the twelve fits ──
    print('\n  Ⓑ② THE TWELVE FITS, against 60\'s own twelve figures (tolerance %.0e)' % TOL)
    fits = {}
    for leg in LEGS:
        for blk in BLOCKS:
            for s in SUMS:
                lo, r_i = leg_ratio(leg, s, blk)
                if lo is None:
                    out['absent'].append('%s|%s|%.2f' % (leg, blk, s))
                    continue
                rc = CA[s][2:AC.LMAX + 1, AC.COL[blk]] / CA[0.0][2:AC.LMAX + 1, AC.COL[blk]] - 1.0
                e0 = AC.fit_A_eps(lo, r_i, l_dense, rc, g)[0]
                e, A, res = AC.refine(lo, r_i, l_dense, rc, e0)
                tgt = TARGET[(leg, blk, s)]
                d = abs(A - tgt)
                fits['%s|%s|%.2f' % (leg, blk, s)] = dict(
                    A=float(A), eps=float(e), resid=float(res), target_60=tgt,
                    diff_from_60=float(d), hits=bool(d < TOL),
                    dist_from_unity=float(abs(A - 1.0)),
                    within_bar=bool(abs(A - 1.0) <= BAR), n=int(lo.size))
    out['fits'] = fits
    out['legs_read'] = True
    out['n_hits'] = sum(1 for v in fits.values() if v['hits'])
    out['worst_diff'] = float(max(v['diff_from_60'] for v in fits.values()))
    for leg in LEGS:
        for blk in BLOCKS:
            cells = []
            for s in SUMS:
                v = fits['%s|%s|%.2f' % (leg, blk, s)]
                cells.append('%s %.2f  %.10f  (60 %.10f, |d| %.3e)%s'
                             % (blk, s, v['A'], v['target_60'], v['diff_from_60'],
                                '' if v['hits'] else '  ⛔'))
            print('      %-7s %s' % (leg if blk == 'TT' else '', '   '.join(cells)))
    print('      ⇒ %d of %d inside %.0e; worst %.6e'
          % (out['n_hits'], len(fits), TOL, out['worst_diff']))

    # ── Ⓒ③ the leg-pair separations against this seat's floors ──
    print('\n  Ⓒ③ LEG-PAIR SEPARATIONS against my own floors (TT %.6e, EE %.6e)'
          % (FLOOR['TT'], FLOOR['EE']))
    sep, n_un = {}, 0
    for a, b in itertools.combinations(LEGS, 2):
        for blk in BLOCKS:
            for s in SUMS:
                ka, kb = '%s|%s|%.2f' % (a, blk, s), '%s|%s|%.2f' % (b, blk, s)
                mine = abs(fits[ka]['A'] - fits[kb]['A'])
                theirs = abs(TARGET[(a, blk, s)] - TARGET[(b, blk, s)])
                ok = mine > FLOOR[blk]
                n_un += (not ok)
                sep['%s-%s|%s|%.2f' % (a, b, blk, s)] = dict(
                    mine=float(mine), theirs=float(theirs), floor=FLOOR[blk],
                    resolvable=bool(ok))
                if not ok:
                    print('      ⛔ %-16s %s %.2f  mine %.6e  (60 %.6e)  BELOW the %.6e floor'
                          % (a + '-' + b, blk, s, mine, theirs, FLOOR[blk]))
    out['separation'] = sep
    out['n_pairs'] = len(sep)
    out['n_unresolvable'] = int(n_un)
    out['unresolvable_keys'] = sorted(k for k, v in sep.items() if not v['resolvable'])
    print('      ⇒ %d of %d pair comparisons resolvable; %d NOT'
          % (len(sep) - n_un, len(sep), n_un))

    # ── Ⓓ④ 69's joint bar, on a second fitter ──
    print('\n  Ⓓ④ 69\'s JOINT BAR %.2f, on this fitter' % BAR)
    bar, all_in = {}, True
    for leg in LEGS:
        ds = {'%s|%.2f' % (blk, s): fits['%s|%s|%.2f' % (leg, blk, s)]['dist_from_unity']
              for blk in BLOCKS for s in SUMS}
        w = max(ds.values())
        wk = max(ds, key=ds.get)
        ok = w <= BAR
        all_in &= ok
        bar[leg] = dict(worst=float(w), worst_key=wk, passes=bool(ok))
        print('      %-7s worst |A-1| = %.6f at %-9s -> %s'
              % (leg, w, wk, 'WITHIN the bar' if ok else '⛔ OUTSIDE'))
    out['against_bar'] = bar
    out['all_legs_within_bar'] = bool(all_in)
    out['verdict_A_joint_on_two_fitters'] = bool(all_in and out['n_hits'] == len(fits))
    print('      ⇒ verdict Ⓐ %s on two fitters'
          % ('IS JOINT' if out['verdict_A_joint_on_two_fitters'] else 'is NOT joint'))

    # ── Ⓔ⑤ eps, reported and never used to decide ──
    out['eps'] = {k: v['eps'] for k, v in fits.items()}
    print('\n  Ⓔ⑤ ε reported, never used to decide: %.6g .. %.6g'
          % (min(out['eps'].values()), max(out['eps'].values())))

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  wrote %s' % OUT)


if __name__ == '__main__':
    main()
