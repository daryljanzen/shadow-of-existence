# -*- coding: utf-8 -*-
"""r7875+cc66 item ⑬ -- AN INDEPENDENT CHECK OF 60's AMPLITUDE `A`.

`60`'s `r7874` fits `r_inst(ℓ) ≈ A · r_camb(ℓ(1+ε))` over `ℓ = 100`-`420` and reports TT's sum
response `15` per cent above CAMB's at `Σ = 0.30` and `30` per cent at `0.60`, with EE matching to a
few per cent.  `69` asks whether MY OWN CAMB leg and MY OWN fitting code give `1.152` and `1.296`.

WHAT IS READ and WHAT IS COMPUTED, as registered:
  READ      `60`'s instrument ratios and `l_A`, from `bank/pol_grid_bvel1_nufd_only`.  I have no
            instrument of my own, so that side must be theirs.  `41` of its `238` multipoles fall
            in the band.  Also the control cosmology, from `60`'s `model3` at run time.
  COMPUTED  my CAMB leg, run here rather than read out of `r7871`; and the `(A, ε)` fit, in my own
            code.  `60`'s `shift.py` reads my `r7871` record only for the control parameters and
            runs CAMB itself, so the two CAMB legs are genuinely independent runs.

⛔ FOUR CONTROLS, none optional:
  Ⓑ②′ my fresh CAMB ratio must reproduce `r7871`'s banked `standard` values at the six named
       multipoles.  If my own two runs disagree, no `A` is reported.
  Ⓓ④  `ε`'s allowance from `θ*` must reproduce `60`'s `2.563e-04` and `5.170e-04`.
  Ⓕ⑥  a PLANTED `(A, ε)` must be recovered.  A fitter that always returns about `1.15` on TT would
       agree with `60` for no reason at all.
  Ⓖ⑦  the interpolation is my choice, so `A`'s movement between linear and cubic is measured, and a
       difference from `60` smaller than that is NOT a disagreement.

⛔ AND `A` IS REPORTED TWICE.  `60`'s own record says `eps_within_allowed = false` on all four fits,
   `eps_over_allowed` from `2.73` to `6.63`.  The best-fit `ε` is three to seven times the shift the
   geometry allows, so the free-`ε` `A` buys its amplitude with a shift that is not available.  `A`
   at `ε` FREE and `A` at `ε` PINNED to the allowance boundary are both given.

    NODE=cc66 python3 amplitude_check.py
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
sys.path.insert(0, os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_'
                                      'the_damping_tails_share_of_the_gap'))
import tail_share as TS                                                     # noqa: E402,F401
import model3 as M3                                                         # noqa: E402

BANK = os.path.join(_BTW, 'bank', 'pol_grid_bvel1_nufd_only')
R7871 = os.path.join(_BTW, 'r7871_cc66_cambs_sum_response_at_the_spectrum_level')
OUT = os.path.join(_HERE, 'amplitude_check.json')

SUMS = (0.30, 0.60)
TAGS = {0.0: 'S000', 0.30: 'S030', 0.60: 'S060'}
TAU, A_S, LMAX = 0.054, 2.1e-9, 2600          # lmax 2600 per the amendment, as 60 ran it
L_LO, L_HI = 100, 420
BLOCKS = ('TT', 'EE')
COL = {'TT': 0, 'EE': 1}
# 60's targets, from their shift.json, for the registered expectation
TARGET = {('TT', 0.30): 1.1516249552025648, ('TT', 0.60): 1.2959239656918276,
          ('EE', 0.30): 1.0140521199524910, ('EE', 0.60): 1.0462960216137143}
ALLOWED_60 = {0.30: 0.00025633773521949177, 0.60: 0.0005170088639169235}


def control():
    c = M3.ARMS['lcdm']['centre']
    return dict(H0=float(c['H0']), OM=float(c['OM']), WB=float(c['WB']), NS=float(c['NS']))


def camb_one(con, sum_ev):
    """my own CAMB leg -- unlensed scalar, and theta* for the allowance"""
    import camb
    om_m = con['OM'] * (con['H0'] / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=con['H0'], ombh2=con['WB'],
                        omch2=max(om_m - con['WB'] - onu, 1e-4), mnu=float(sum_ev),
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=A_S, ns=con['NS'])
        p.set_for_lmax(LMAX, lens_potential_accuracy=1)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    sp = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                 spectra=['unlensed_scalar', 'lensed_scalar'])
    return (np.asarray(sp['unlensed_scalar'], float),
            np.asarray(sp['lensed_scalar'], float),
            float(r.get_derived_params()['thetastar']))


def bank_arr(tag, key):
    with np.load(os.path.join(BANK, 'lcdm_%s.npz' % tag), allow_pickle=True) as z:
        return np.asarray(z[key], float)


def bank_lA(tag):
    with np.load(os.path.join(BANK, 'lcdm_%s.npz' % tag), allow_pickle=True) as z:
        return float(z['l_A'])


def fit_A_eps(l_obs, r_obs, l_c, r_c, eps_grid, kind='linear'):
    """MY fitting code.  At each eps, A is the least-squares scale: <r_obs, r_c> / <r_c, r_c>.
    The eps that minimises the residual wins.  No part of this is 60's."""
    if kind == 'cubic':
        from scipy.interpolate import CubicSpline
        f = CubicSpline(l_c, r_c, extrapolate=True)
    else:
        def f(x):
            return np.interp(x, l_c, r_c)
    best = None
    for e in eps_grid:
        rc = np.asarray(f(l_obs * (1.0 + e)), float)
        den = float(np.dot(rc, rc))
        if den <= 0:
            continue
        A = float(np.dot(r_obs, rc) / den)
        res = float(np.sqrt(np.mean((r_obs - A * rc) ** 2)))
        if best is None or res < best[2]:
            best = (float(e), A, res)
    return best


def A_at_eps(l_obs, r_obs, l_c, r_c, e, kind='linear'):
    if kind == 'cubic':
        from scipy.interpolate import CubicSpline
        f = CubicSpline(l_c, r_c, extrapolate=True)
    else:
        def f(x):
            return np.interp(x, l_c, r_c)
    rc = np.asarray(f(l_obs * (1.0 + e)), float)
    A = float(np.dot(r_obs, rc) / np.dot(rc, rc))
    return A, float(np.sqrt(np.mean((r_obs - A * rc) ** 2)))


def refine(l_obs, r_obs, l_c, r_c, e0, kind='linear'):
    """my own refinement: three shrinking local grids around the coarse winner"""
    e, step = e0, 5e-4
    for _ in range(3):
        g = np.linspace(e - step, e + step, 201)
        e, A, res = fit_A_eps(l_obs, r_obs, l_c, r_c, g, kind)
        step /= 20.0
    return e, A, res


def main():
    print(__doc__)
    print('=' * 100)
    con = control()
    print('\n  Ⓐ① control read from 60\'s module at run time: %s;  tau %.3f, A_s %.3g, lmax %d'
          % (con, TAU, A_S, LMAX))
    out = {'control': con, 'tau': TAU, 'A_s': A_S, 'lmax': LMAX, 'window': [L_LO, L_HI],
           'sums': list(SUMS), 'target_60': {'%s|%.2f' % k: v for k, v in TARGET.items()}}

    CA, CL, TH = {}, {}, {}
    for s in (0.0,) + SUMS:
        CA[s], CL[s], TH[s] = camb_one(con, s)
        print('    my CAMB at Sum %.2f: 100 theta* = %.6f' % (s, TH[s]))
    out['theta_star'] = {'%.2f' % s: TH[s] for s in TH}

    # ── Ⓑ②′ my fresh run against my own r7871 record ──
    print('\n  Ⓑ②″ MY FRESH **LENSED** LEG AGAINST MY OWN `r7871` RECORD, WHICH IS LENSED')
    print('      (the registration compared my UNLENSED leg to it -- two different quantities,')
    print('       my own error, recorded in PREDICTION.md and not repaired silently)')
    STD = json.load(io.open(os.path.join(R7871, 'sum_response.json'), encoding='utf-8'))['standard']
    worst, b2 = 0.0, {}
    for s in SUMS:
        for blk in BLOCKS:
            got = {}
            for name, L in (('l100', 100), ('l220', 220), ('l500', 500),
                            ('l1000', 1000), ('l1500', 1500), ('l1996', 1996)):
                mine = CL[s][L, COL[blk]] / CL[0.0][L, COL[blk]] - 1.0
                ref = float(STD['%g' % s][blk][name])
                rel = abs(mine - ref) / max(abs(ref), 1e-30)
                got[name] = dict(mine=float(mine), r7871=ref, rel=float(rel))
                worst = max(worst, rel)
            b2['%s|%.2f' % (blk, s)] = got
            print('      %s Sum %.2f: worst relative over the six: %.3e'
                  % (blk, s, max(v['rel'] for v in got.values())))
    out['b2_worst_rel'] = float(worst)
    out['b2'] = b2
    worst_abs = max(abs(v['mine'] - v['r7871'])
                    for g in b2.values() for v in g.values())
    out['b2_worst_abs'] = float(worst_abs)
    print('      worst ABSOLUTE difference over the 24: %.3e  (the ratio crosses zero at high'
          ' `ℓ`, so relative is not the readable metric there -- the `r7873` rule)' % worst_abs)
    ok_b2 = worst_abs < 1e-9
    print('      ⇒ %s on the 1e-9 ABSOLUTE band' % ('PASSES' if ok_b2 else '⛔ FAILS'))
    if not ok_b2:
        print('\n  ⛔ MY OWN TWO RUNS DISAGREE, so no A is reported.')
        out['A_reported'] = False
        io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
        return

    # ── Ⓓ④ the allowance from theta* and l_A ──
    print('\n  Ⓓ④ `ε`\'s ALLOWANCE from `θ*`, as 60 did -- `l_A` is READ, only `θ*` is mine')
    lA = {s: bank_lA(TAGS[s]) for s in (0.0,) + SUMS}
    allow, d4 = {}, {}
    for s in SUMS:
        f_inst = lA[s] / lA[0.0] - 1.0
        f_camb = -(TH[s] / TH[0.0] - 1.0)
        allow[s] = abs(f_inst - f_camb)
        rel = abs(allow[s] - ALLOWED_60[s]) / ALLOWED_60[s]
        d4['%.2f' % s] = dict(l_A=lA[s], l_A_zero=lA[0.0], f_inst=float(f_inst),
                              f_camb=float(f_camb), allowed=float(allow[s]),
                              allowed_60=ALLOWED_60[s], rel_to_60=float(rel))
        print('      Sum %.2f: f_inst %+.6e  f_camb %+.6e  allowance %.6e  (60: %.6e, rel %.2e)'
              % (s, f_inst, f_camb, allow[s], ALLOWED_60[s], rel))
    out['allowance'] = d4

    # ── Ⓕ⑥ the planted-recovery control ──
    print('\n  Ⓕ⑥ THE PLANTED-RECOVERY CONTROL -- can the fitter return something other than 60\'s?')
    l_dense = np.arange(2, LMAX + 1, dtype=float)
    f6 = {}
    for (A_p, e_p) in ((1.40, 0.0030), (0.80, -0.0045), (1.00, 0.0)):
        rc = CA[0.60][2:LMAX + 1, 0] / CA[0.0][2:LMAX + 1, 0] - 1.0
        l_obs = np.arange(L_LO, L_HI + 1, dtype=float)
        planted = A_p * np.interp(l_obs * (1.0 + e_p), l_dense, rc)
        g = np.linspace(-0.08, 0.08, 3201)
        e_hat, A_hat, _ = refine(l_obs, planted, l_dense, rc,
                                 fit_A_eps(l_obs, planted, l_dense, rc, g)[0])
        f6['A%.2f_e%+.4f' % (A_p, e_p)] = dict(A_true=A_p, eps_true=e_p, A_fit=float(A_hat),
                                               eps_fit=float(e_hat),
                                               dA=float(abs(A_hat - A_p)))
        print('      planted A %.2f eps %+.4f  ->  recovered A %.6f eps %+.6f   |dA| %.2e   %s'
              % (A_p, e_p, A_hat, e_hat, abs(A_hat - A_p),
                 'OK' if abs(A_hat - A_p) < 1e-3 else '⛔ NOT RECOVERED'))
    out['planted'] = f6
    ok_f6 = all(v['dA'] < 1e-3 for v in f6.values())
    print('      ⇒ %s' % ('the fitter recovers what is planted, so it is not hard-wired to 60\'s'
                          ' answer' if ok_f6 else '⛔ THE FITTER CANNOT RECOVER A PLANT'))
    out['planted_ok'] = bool(ok_f6)

    # ── Ⓔ⑤ / Ⓖ⑦ / Ⓗ⑧ the fit itself ──
    print('\n  Ⓔ⑤ THE FIT -- 60\'s 41 in-band multipoles, then all 321, then eps pinned')
    fits = {}
    for blk in BLOCKS:
        for s in SUMS:
            bl = bank_arr(TAGS[0.0], 'ls')
            key = 'Dl' if blk == 'TT' else 'Dl_EE'
            r_i_all = bank_arr(TAGS[s], key) / bank_arr(TAGS[0.0], key) - 1.0
            m = (bl >= L_LO) & (bl <= L_HI)
            l41, r41 = bl[m].astype(float), r_i_all[m]
            rc = CA[s][2:LMAX + 1, COL[blk]] / CA[0.0][2:LMAX + 1, COL[blk]] - 1.0
            g = np.linspace(-0.08, 0.08, 3201)

            e_lin, A_lin, res_lin = refine(l41, r41, l_dense, rc,
                                           fit_A_eps(l41, r41, l_dense, rc, g)[0], 'linear')
            e_cub, A_cub, _ = refine(l41, r41, l_dense, rc,
                                     fit_A_eps(l41, r41, l_dense, rc, g, 'cubic')[0], 'cubic')
            A_free, eps_free = A_lin, e_lin
            A_pin_p, _ = A_at_eps(l41, r41, l_dense, rc, +allow[s])
            A_pin_m, _ = A_at_eps(l41, r41, l_dense, rc, -allow[s])
            A_zero, _ = A_at_eps(l41, r41, l_dense, rc, 0.0)
            # all 321 multipoles, for the Ⓒ③ visibility of the choice
            l321 = np.arange(L_LO, L_HI + 1, dtype=float)
            r321 = np.interp(l321, bl.astype(float), r_i_all)
            e_321, A_321, _ = refine(l321, r321, l_dense, rc,
                                     fit_A_eps(l321, r321, l_dense, rc, g)[0], 'linear')

            rc_lens = CL[s][2:LMAX + 1, COL[blk]] / CL[0.0][2:LMAX + 1, COL[blk]] - 1.0
            e_len, A_len, _ = refine(l41, r41, l_dense, rc_lens,
                                     fit_A_eps(l41, r41, l_dense, rc_lens, g)[0], 'linear')
            tgt = TARGET[(blk, s)]
            hit = abs(A_free - tgt) < 0.005
            fits['%s|%.2f' % (blk, s)] = dict(
                n_multipoles=int(m.sum()), A_free=float(A_free), eps_free=float(eps_free),
                resid=float(res_lin), A_cubic=float(A_cub), eps_cubic=float(e_cub),
                interp_sensitivity=float(abs(A_cub - A_lin)),
                A_eps_zero=float(A_zero), A_eps_pinned_plus=float(A_pin_p),
                A_eps_pinned_minus=float(A_pin_m),
                eps_over_allowed=float(abs(eps_free) / allow[s]),
                eps_within_allowed=bool(abs(eps_free) <= allow[s]),
                A_all_321=float(A_321), eps_all_321=float(e_321),
                A_lensed_leg=float(A_len), eps_lensed_leg=float(e_len),
                lensing_moves_A=float(abs(A_len - A_free)),
                target_60=tgt, hits_target=bool(hit),
                abs_diff_from_60=float(abs(A_free - tgt)))
            v = fits['%s|%.2f' % (blk, s)]
            print('\n      %s at Sum %.2f   (60: A = %.7f)' % (blk, s, tgt))
            print('          eps FREE : A %.7f  eps %+.6f  resid %.6e   ⇒ %s 60\'s to 0.005'
                  % (A_free, eps_free, res_lin, 'MATCHES' if hit else '⛔ MISSES'))
            print('          |A - 60|  %.2e      eps is %.2f x its allowance, within = %s'
                  % (v['abs_diff_from_60'], v['eps_over_allowed'], v['eps_within_allowed']))
            print('          interp   : cubic A %.7f, sensitivity %.2e' % (A_cub,
                                                                           v['interp_sensitivity']))
            print('          eps PINNED: A %.7f at +allowance, %.7f at -allowance, %.7f at eps=0'
                  % (A_pin_p, A_pin_m, A_zero))
            print('          all 321  : A %.7f  eps %+.6f' % (A_321, e_321))
            print('          LENSED leg: A %.7f  eps %+.6f   ⇒ lensing moves A by %.2e'
                  % (A_len, e_len, v['lensing_moves_A']))
    out['fits'] = fits
    out['A_reported'] = True
    hits = sum(1 for v in fits.values() if v['hits_target'])
    out['n_hits'] = hits
    print('\n' + '=' * 100)
    print('  %d of %d fits reproduce 60\'s A to 0.005' % (hits, len(fits)))
    print('  TT: %.7f at 0.30 (60: 1.1516250) and %.7f at 0.60 (60: 1.2959240)'
          % (fits['TT|0.30']['A_free'], fits['TT|0.60']['A_free']))
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
