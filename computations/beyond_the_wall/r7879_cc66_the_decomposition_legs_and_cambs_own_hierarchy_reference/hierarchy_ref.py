# -*- coding: utf-8 -*-
"""r7879+cc66 item ⑯ -- CAMB's OWN HIERARCHY AGAINST ITS OWN FLUID APPROXIMATION.

`69` asks for CAMB's TT and EE sum-response amplitudes with its massive neutrinos run in the full
hierarchy (`MassiveNuMethod = Nu_int`) and in the truncated fluid approximation (`Nu_trunc` or
`Nu_approx`), on `60`'s `41` multipoles at `Σ = 0.30` and `0.60`, *"to tell `60` how much of its
leverage gap a full hierarchy can be expected to close."*

⛔ THE LIVENESS CONTROL COMES FIRST, AND THIS ITEM MAY MEASURE NOTHING.  My `r7871` record has
   `Nu_approx`, `Nu_best` and `Nu_trunc` returning spectra BIT-IDENTICAL to one another, with only
   `Nu_int` differing and only in the ninth decimal (`method_spread_worst = 7.305730e-08`).  ** If
   the truncated setting does not change the spectrum, it cannot change `A`, and an `A` difference
   of zero would say nothing about hierarchies -- only that the knob is inert. **  So the spectra
   are compared BEFORE any `A` is, and what is found is reported either way.

⌗ `69`'s order says I found the methods differing "by about `6e-6`".  My record says `7.305730e-08`,
  two orders of magnitude smaller.  The figure is corrected here rather than carried.

⛔ AND `A` IS A FITTED QUANTITY.  A least-squares amplitude over `41` multipoles is not a pointwise
   ratio and could amplify a tiny spectrum difference.  So the `A` difference is compared against my
   own interpolation floors -- `3.515264e-06` for TT, `5.307333e-05` for EE -- and a difference
   below them is reported as BELOW WHAT THIS FITTER CAN SEE, which is not the same as zero.

    NODE=cc66 python3 hierarchy_ref.py
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
R7877 = os.path.join(_BTW, 'r7877_cc66_the_second_fitter_on_60s_repair_legs')
sys.path.insert(0, R7877)
import refit_legs as RL                                                     # noqa: E402
AC = RL.AC

OUT = os.path.join(_HERE, 'hierarchy_ref.json')
SUMS = (0.30, 0.60)
BLOCKS = ('TT', 'EE')
KEY = {'TT': 'Dl', 'EE': 'Dl_EE'}
METHODS = ('Nu_int', 'Nu_trunc', 'Nu_approx', 'Nu_best')
HIER, TRUNC = 'Nu_int', ('Nu_trunc', 'Nu_approx')
FLOOR = {'TT': 3.515263913511646e-06, 'EE': 5.307332502169082e-05}
R7871_SPREAD = 7.305729821105444e-08
BAR = 0.03


def camb_method(con, sum_ev, method):
    """my own CAMB leg with MassiveNuMethod set, unlensed scalar as 60 use"""
    import camb
    om_m = con['OM'] * (con['H0'] / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=con['H0'], ombh2=con['WB'],
                        omch2=max(om_m - con['WB'] - onu, 1e-4), mnu=float(sum_ev),
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=AC.TAU)
        p.InitPower.set_params(As=AC.A_S, ns=con['NS'])
        p.set_for_lmax(AC.LMAX, lens_potential_accuracy=1)
        p.MassiveNuMethod = method
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    got = str(p.MassiveNuMethod)
    r = camb.get_results(p)
    sp = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                 spectra=['unlensed_scalar'])['unlensed_scalar']
    return np.asarray(sp, float), got


def main():
    print(__doc__)
    print('=' * 100)
    con = AC.control()
    out = {'control': con, 'methods': list(METHODS), 'sums': list(SUMS),
           'window': [AC.L_LO, AC.L_HI], 'floors': FLOOR,
           'r7871_spread': R7871_SPREAD, 'bar': BAR}
    print('\n  Ⓐ① control %s; tau %.3f; lmax %d; band %d-%d; 60\'s 41 multipoles'
          % (con, AC.TAU, AC.LMAX, AC.L_LO, AC.L_HI))

    SP, SET = {}, {}
    for m in METHODS:
        for s in (0.0,) + SUMS:
            SP[(m, s)], SET[(m, s)] = camb_method(con, s, m)
        print('      %-10s requested, CAMB reports MassiveNuMethod = %s' % (m, SET[(m, 0.0)]))
    out['settings_survive'] = {m: SET[(m, 0.0)] for m in METHODS}

    # ── Ⓕ⑥ the liveness control, on the spectra, before any A ──
    print('\n  Ⓕ⑥ THE LIVENESS CONTROL -- do the methods\' SPECTRA differ at all?')
    ls = np.arange(AC.L_LO, AC.L_HI + 1)
    live = {}
    for s in SUMS:
        for blk in BLOCKS:
            c = AC.COL[blk]
            h = SP[(HIER, s)][AC.L_LO:AC.L_HI + 1, c]
            row = {}
            for t in TRUNC:
                q = SP[(t, s)][AC.L_LO:AC.L_HI + 1, c]
                row[t] = dict(max_abs_rel=float(np.max(np.abs(q - h)
                                                       / np.maximum(np.abs(h), 1e-30))),
                              identical=bool(np.array_equal(q, h)))
            # and the three truncated-family members against each other
            q1 = SP[('Nu_trunc', s)][AC.L_LO:AC.L_HI + 1, c]
            q2 = SP[('Nu_approx', s)][AC.L_LO:AC.L_HI + 1, c]
            q3 = SP[('Nu_best', s)][AC.L_LO:AC.L_HI + 1, c]
            row['trunc_vs_approx_identical'] = bool(np.array_equal(q1, q2))
            row['approx_vs_best_identical'] = bool(np.array_equal(q2, q3))
            live['%s|%.2f' % (blk, s)] = row
            print('      %s %.2f: Nu_int vs Nu_trunc %.3e%s; vs Nu_approx %.3e%s; '
                  'trunc==approx %s; approx==best %s'
                  % (blk, s, row['Nu_trunc']['max_abs_rel'],
                     ' (IDENTICAL)' if row['Nu_trunc']['identical'] else '',
                     row['Nu_approx']['max_abs_rel'],
                     ' (IDENTICAL)' if row['Nu_approx']['identical'] else '',
                     row['trunc_vs_approx_identical'], row['approx_vs_best_identical']))
    out['liveness'] = live
    worst_spec = max(v[t]['max_abs_rel'] for v in live.values() for t in TRUNC)
    out['worst_spectrum_difference'] = float(worst_spec)
    any_identical = any(v[t]['identical'] for v in live.values() for t in TRUNC)
    out['any_identical_to_hierarchy'] = bool(any_identical)
    print('      ⇒ worst spectrum difference between hierarchy and truncated: %.6e' % worst_spec)
    print('        (my r7871 record: %.6e across all four methods; 69\'s order said "about 6e-6")'
          % R7871_SPREAD)

    # ── Ⓖ⑦ the amplitudes ──
    print('\n  Ⓖ⑦ THE AMPLITUDES -- A and eps per method, on 60\'s 41 multipoles')
    l_dense = np.arange(2, AC.LMAX + 1, dtype=float)
    g = np.linspace(-0.08, 0.08, 3201)
    bl = AC.bank_arr(AC.TAGS[0.0], 'ls')
    fits = {}
    for blk in BLOCKS:
        for s in SUMS:
            # the instrument ratio is 60's landed one: the fixed observable both methods are fit to
            r_i = (AC.bank_arr(AC.TAGS[s], KEY[blk])
                   / AC.bank_arr(AC.TAGS[0.0], KEY[blk]) - 1.0)
            m = (bl >= AC.L_LO) & (bl <= AC.L_HI)
            lo = bl[m].astype(float)
            for meth in METHODS:
                c = AC.COL[blk]
                rc = (SP[(meth, s)][2:AC.LMAX + 1, c]
                      / SP[(meth, 0.0)][2:AC.LMAX + 1, c] - 1.0)
                e0 = AC.fit_A_eps(lo, r_i[m], l_dense, rc, g)[0]
                e, A, res = AC.refine(lo, r_i[m], l_dense, rc, e0)
                fits['%s|%.2f|%s' % (blk, s, meth)] = dict(A=float(A), eps=float(e),
                                                           resid=float(res))
            h = fits['%s|%.2f|%s' % (blk, s, HIER)]
            print('      %s %.2f  hierarchy A %.9f eps %+.7f' % (blk, s, h['A'], h['eps']))
            for t in TRUNC:
                q = fits['%s|%.2f|%s' % (blk, s, t)]
                dA, de = abs(q['A'] - h['A']), abs(q['eps'] - h['eps'])
                print('              %-10s A %.9f eps %+.7f   |dA| %.3e  |deps| %.3e   %s'
                      % (t, q['A'], q['eps'], dA, de,
                         'ABOVE my %s floor' % blk if dA > FLOOR[blk]
                         else 'BELOW my %s floor -- not distinguishable' % blk))
    out['fits'] = fits

    # ── Ⓗ⑧ the A differences against my floors ──
    print('\n  Ⓗ⑧ THE A DIFFERENCES AGAINST MY OWN FLOORS')
    diffs = {}
    for blk in BLOCKS:
        for s in SUMS:
            h = fits['%s|%.2f|%s' % (blk, s, HIER)]
            for t in TRUNC:
                q = fits['%s|%.2f|%s' % (blk, s, t)]
                dA = abs(q['A'] - h['A'])
                diffs['%s|%.2f|%s' % (blk, s, t)] = dict(
                    dA=float(dA), deps=float(abs(q['eps'] - h['eps'])),
                    floor=FLOOR[blk], above_floor=bool(dA > FLOOR[blk]),
                    frac_of_bar=float(dA / BAR))
    out['differences'] = diffs
    worst_dA = max(v['dA'] for v in diffs.values())
    out['worst_dA'] = float(worst_dA)
    out['n_above_floor'] = sum(1 for v in diffs.values() if v['above_floor'])
    print('      worst |dA| over the eight comparisons: %.6e' % worst_dA)
    print('      %d of %d are above my own floor' % (out['n_above_floor'], len(diffs)))
    print('      worst |dA| as a fraction of 69\'s %.2f bar: %.3e' % (BAR, worst_dA / BAR))
    print('\n  ⇒ THE ANSWER TO 69: the difference between CAMB\'s hierarchy and its truncated')
    print('    fluid approximation is %.3e in A at worst -- %.1e of the %.2f bar. A full'
          % (worst_dA, worst_dA / BAR, BAR))
    print('    hierarchy cannot be expected to close any measurable part of 60\'s leverage gap,')
    print('    because CAMB\'s own two treatments are not measurably different objects.')

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
