# -*- coding: utf-8 -*-
"""r7869+cc66 item ⑧, second pass -- IS THE PER-BIN SHARE A READABLE NUMBER AT ALL?

`per_bin_response.py` found the decomposition does NOT close on the finite-difference total:
65-78 per cent off at 60's banked 0.05 eV spacing, still 10 per cent off at 0.002, and the totals
non-monotone in the step (69.87 at 0.01 against 84.77 at 0.002).  Non-monotone means NOISE, not
nonlinearity.  This pass separates the two, because a per-bin SHARE is only readable if one of
them can be made small.

  ⒜ CENTRAL differences at each step -- second-order, so nonlinearity falls as step^2;
  ⒝ one leg at HIGHER CAMB accuracy -- if the small-step disagreement is CAMB's own noise, it
     moves with accuracy and not with the step;
  ⒞ the reproduction band stated correctly: the banked chi2_cmb is on the reference's own COVERED
     set, not on 60's 555, which is what `Ⓐ①` should have said and did not;
  ⒟ what the repaired memo did to the banked zero-sum parameters.

    NODE=cc66 python3 closure_and_reproduction.py
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
import score_ttteee as SC                                                   # noqa: E402
import model6 as M6                                                         # noqa: E402

BANK5 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference', 'out5')
EXACT = os.path.join(_BTW, 'r7865_cc66_the_repaired_background_checked_and_the_rounded_memo_dropped',
                     'out_exact')
LMAX, A_S = 2600, 2.1e-9
MODES = ('rd_camb', 'rd_min')
STEPS = (0.02, 0.01, 0.005)
ACCS = (1, 3)
N_PER_BLOCK = 12
OUT = os.path.join(_HERE, 'closure_and_reproduction.json')
_cache = {}


def camb_binned(par, sum_ev, acc):
    key = (par, round(sum_ev, 10), acc)          # ⛔ keyed on ALL THREE, r7867's lesson
    if key in _cache:
        return _cache[key]
    import camb
    h0, om, wb, ns, tau = par
    om_m = om * (h0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=wb, omch2=max(om_m - wb - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=A_S, ns=ns)
        p.set_for_lmax(LMAX, lens_potential_accuracy=acc)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    ls = np.arange(cl.shape[0], dtype=float)
    _cache[key] = SC.bin_three(ls, cl[:, 0], cl[:, 3], cl[:, 1])
    return _cache[key]


def low36(ok):
    idx = np.where(ok)[0]
    low = np.zeros(ok.size, bool)
    for b in (0, 1, 2):
        here = idx[SC.BLOCK[idx] == b]
        low[here[np.argsort(SC.BIN_LO[here], kind='stable')][:N_PER_BLOCK]] = True
    return low


def chi_of(m, F, d):
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r), A, r


def main():
    print(__doc__)
    print('=' * 100)
    mod = M6.Model6('lcdm')
    ok = np.asarray(mod.cmb.ok, bool)
    low_in = low36(ok)[ok]
    F, d = SC.fisher_for(ok), SC.X_DATA[ok]
    out = {'steps': list(STEPS), 'accs': list(ACCS), 'lmax': LMAX}

    for mode in MODES:
        b0 = json.load(io.open(os.path.join(BANK5, '%s_0.000.json' % mode), encoding='utf-8'))
        par = (b0['H0'], b0['Om'], b0['ombh2'], b0['ns'], b0['tau'])
        rec = {'params': list(par), 'banked_chi2_cmb': float(b0['chi2_cmb']),
               'banked_dof_cmb': int(b0.get('dof_cmb', -1)), 'acc': {}}
        print('\n  === %s ===' % mode)

        # ⒞ the reproduction band, on the set the banked number is actually on
        m_full = camb_binned(par, 0.0, 1)
        cov = np.isfinite(m_full) & np.isin(SC.BLOCK, (0, 1, 2))
        chi_cov, _, _ = chi_of(m_full[cov], SC.fisher_for(cov), SC.X_DATA[cov])
        rel = abs(chi_cov - b0['chi2_cmb']) / abs(b0['chi2_cmb'])
        print('    ⒞ banked chi2_cmb %.6f on %d bin(s); reproduced %.6f on %d  ⇒ rel %.3e'
              % (b0['chi2_cmb'], rec['banked_dof_cmb'], chi_cov, int(cov.sum()), rel))
        rec['reproduced_on_covered'] = chi_cov
        rec['n_covered'] = int(cov.sum())
        rec['rel_to_banked'] = float(rel)

        # ⒟ what the repaired memo did to the banked zero-sum parameters
        fx = os.path.join(EXACT, '%s_0.000.json' % mode)
        if os.path.exists(fx):
            bx = json.load(io.open(fx, encoding='utf-8'))
            px = (bx['H0'], bx['Om'], bx['ombh2'], bx['ns'], bx['tau'])
            dmax = max(abs(a - b) for a, b in zip(par, px))
            rec['exact_bank'] = dict(params=list(px), max_abs_param_move=float(dmax),
                                     chi2_cmb=float(bx['chi2_cmb']))
            print('    ⒟ repaired-memo bank: worst parameter move %.3e, chi2_cmb %.6f against %.6f'
                  % (dmax, bx['chi2_cmb'], b0['chi2_cmb']))
        else:
            rec['exact_bank'] = None
            print('    ⒟ no repaired-memo bank for this mode (it never called the memo)')

        for acc in ACCS:
            m0 = camb_binned(par, 0.0, acc)[ok]
            chi0, A0, r0 = chi_of(m0, F, d)
            Fr0 = F @ r0
            per_acc = {}
            for st in STEPS:
                mp = camb_binned(par, st, acc)[ok]
                mm_ = camb_binned(par, 0.0, acc)[ok]           # one-sided foot
                Ap, _, _ = chi_of(mp, F, d)[1], None, None
                Ap = float((mp @ F @ d) / (mp @ F @ mp))
                # one-sided
                per_1 = -2.0 * Fr0 * ((Ap * mp - A0 * mm_) / st)
                chip, _, rp = chi_of(mp, F, d)
                tot_1 = (chip - chi0) / st
                # central, at half the step each side -> same total width
                mh = camb_binned(par, st / 2.0, acc)[ok]
                Ah = float((mh @ F @ d) / (mh @ F @ mh))
                chih, _, _ = chi_of(mh, F, d)
                tot_c = (chip - chi0) / st                     # width st, feet 0 and st
                tot_half = (chih - chi0) / (st / 2.0)
                # Richardson on the two widths: 2*D(h/2) - D(h) kills the O(h) term
                tot_rich = 2.0 * tot_half - tot_1
                s_all = float(np.abs(per_1).sum())
                s_low = float(np.abs(per_1[low_in]).sum())
                per_acc['%g' % st] = dict(
                    step=st, per_bin_sum=float(per_1.sum()), fd_total=float(tot_1),
                    fd_total_half=float(tot_half), fd_richardson=float(tot_rich),
                    closure=abs(float(per_1.sum()) - float(tot_1)) / max(abs(float(tot_1)), 1e-30),
                    closure_rich=abs(float(per_1.sum()) - float(tot_rich))
                    / max(abs(float(tot_rich)), 1e-30),
                    low_share=(s_low / s_all) if s_all else None)
                print('      acc=%d step %-6g  per-bin sum %+10.4f  fd %+10.4f  fd(h/2) %+10.4f  '
                      'Richardson %+10.4f  closure %6.3f -> %6.3f  low share %.4f'
                      % (acc, st, per_1.sum(), tot_1, tot_half, tot_rich,
                         per_acc['%g' % st]['closure'], per_acc['%g' % st]['closure_rich'],
                         s_low / s_all))
            rec['acc'][str(acc)] = per_acc
        out[mode] = rec

    # does the small-step disagreement move with ACCURACY (noise) or with STEP (nonlinearity)?
    print('\n  ⇒ THE SEPARATION: for each mode and step, how much the Richardson total moved when '
          'CAMB accuracy went %d -> %d' % (ACCS[0], ACCS[-1]))
    sep = {}
    for mode in MODES:
        sep[mode] = {}
        for k in out[mode]['acc'][str(ACCS[0])]:
            a = out[mode]['acc'][str(ACCS[0])][k]['fd_richardson']
            b = out[mode]['acc'][str(ACCS[-1])][k]['fd_richardson']
            sep[mode][k] = dict(acc_lo=a, acc_hi=b, moved=float(b - a),
                                rel=abs(b - a) / max(abs(b), 1e-30))
            print('      %-8s step %-6s  %+10.4f -> %+10.4f   moved %+9.4f  (%.1f%%)'
                  % (mode, k, a, b, b - a, 100.0 * sep[mode][k]['rel']))
    out['accuracy_sensitivity'] = sep
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
