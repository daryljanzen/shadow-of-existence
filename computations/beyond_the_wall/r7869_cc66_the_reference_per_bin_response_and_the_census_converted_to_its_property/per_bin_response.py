# -*- coding: utf-8 -*-
"""r7869+cc66 item ⑧ -- THE REFERENCE'S PER-BIN dchi2/dSigma ON 60's IDENTICAL 555 BINS,
BOTH RULER MODES, EACH ON ITS OWN PARAMETERS.

The CAMB leg is built HERE so the reference is this seat's own and not a read of 60's file; the
bins, the Fisher and the data come from 60's `score_ttteee` so the columns are on the SAME bins.
⇒ Neither mode waits on 60's cache fix: each calls CAMB with its own banked parameters, which is
what `same_bins.py`'s shared memo prevented.

Decomposition, 60's own (`lean.py`): with the amplitude re-solved,
    dchi2/dSigma = -2 (F r0) . d(A m)/dSigma      per-bin summand.

⚠ Measured at SEVERAL steps, because 60's banked spacing is 0.05 eV = 50 meV and at that width the
summand need not sum to the measured change.  The step sweep is what says whether a per-bin SHARE
is readable at all.

    NODE=cc66 python3 per_bin_response.py
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

# mirrors 60's own entry point (`lean.py`): r7862 first, and `tail_share` imported before the
# rest because it is what puts `score_ttteee` and `model6` on the path.  Reaching for those two
# directly fails -- they live under r7842 and r7846.
sys.path.insert(0, os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_'
                                      'the_damping_tails_share_of_the_gap'))
import tail_share as TS                                                     # noqa: E402,F401
import score_ttteee as SC                                                   # noqa: E402
import model6 as M6                                                         # noqa: E402

BANK5 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference', 'out5')
EXACT = os.path.join(_BTW, 'r7865_cc66_the_repaired_background_checked_and_the_rounded_memo_dropped',
                     'out_exact')
SIXTY = os.path.join(_BTW, 'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the_'
                           'repaired_background')

LMAX, ACC, A_S = 2600, 1, 2.1e-9        # r7853's own, read from profile_likeforlike
MODES = ('rd_camb', 'rd_min')
STEPS = (0.05, 0.02, 0.01, 0.002)       # 60's banked spacing first, then finer
N_PER_BLOCK = 12
NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
OUT = os.path.join(_HERE, 'per_bin_response.json')


def camb_binned(h0, om, wb, ns, tau, sum_ev):
    """this seat's own CAMB leg, binned through 60's own window set"""
    import camb
    om_m = om * (h0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=wb, omch2=max(om_m - wb - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=A_S, ns=ns)
        p.set_for_lmax(LMAX, lens_potential_accuracy=ACC)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    ls = np.arange(cl.shape[0], dtype=float)
    return SC.bin_three(ls, cl[:, 0], cl[:, 3], cl[:, 1])


def the_thirty_six(ok):
    """60's own construction: the twelve lowest BIN_LO per block of ITS mask"""
    idx = np.where(ok)[0]
    low = np.zeros(ok.size, bool)
    for b in (0, 1, 2):
        here = idx[SC.BLOCK[idx] == b]
        low[here[np.argsort(SC.BIN_LO[here], kind='stable')][:N_PER_BLOCK]] = True
    return low


def params(mode, where):
    f = os.path.join(where, '%s_0.000.json' % mode)
    if not os.path.exists(f):
        return None
    b = json.load(io.open(f, encoding='utf-8'))
    return (b['H0'], b['Om'], b['ombh2'], b['ns'], b['tau']), b


def main():
    print(__doc__)
    print('=' * 100)
    out = {'lmax': LMAX, 'acc': ACC, 'A_s': A_S, 'steps': list(STEPS)}

    mod = M6.Model6('lcdm')
    ok = np.asarray(mod.cmb.ok, bool)
    low = the_thirty_six(ok)
    F, d = SC.fisher_for(ok), SC.X_DATA[ok]
    low_in = low[ok]

    lo_e, hi_e = SC.BIN_LO[low], SC.BIN_HI[low]
    print('\n  Ⓑ② THE MASK AND THE THIRTY-SIX, from 60\'s own mask and construction')
    print('      60\'s covered bins: %d   (613 in the reference\'s own full set)' % int(ok.sum()))
    print('      the low set: %d bin(s), %d per block, multipoles %d..%d'
          % (int(low.sum()), N_PER_BLOCK, int(lo_e.min()), int(hi_e.max())))
    out['mask'] = dict(n_covered=int(ok.sum()), n_low=int(low.sum()),
                       ell_lo=int(lo_e.min()), ell_hi=int(hi_e.max()),
                       per_block={NAMES[b]: int(((SC.BLOCK == b) & low).sum()) for b in (0, 1, 2)})

    # cross-check the construction against 60's own recorded rows
    sixty_rows = None
    f60 = os.path.join(SIXTY, 'low_bins.json')
    if os.path.exists(f60):
        j = json.load(io.open(f60, encoding='utf-8'))
        sixty_rows = set(tuple(r) for r in j['instrument']['rows'])
        mine_rows = set((NAMES[int(SC.BLOCK[i])], int(SC.BIN_LO[i]), int(SC.BIN_HI[i]))
                        for i in np.where(low)[0])
        same = mine_rows == sixty_rows
        print('      against 60\'s own recorded rows: %s (%d mine, %d theirs, %d shared)'
              % ('IDENTICAL' if same else 'DIFFERENT', len(mine_rows), len(sixty_rows),
                 len(mine_rows & sixty_rows)))
        out['mask']['matches_sixty_rows'] = bool(same)
        out['mask']['n_shared_with_sixty'] = len(mine_rows & sixty_rows)

    out['modes'] = {}
    for mode in MODES:
        got = params(mode, BANK5)
        if got is None:
            print('\n  ⛔ %s: no banked zero-sum point' % mode)
            continue
        par, banked = got
        ex = params(mode, EXACT)
        print('\n  %s  banked params H0 %.8f Om %.8f wb %.8f ns %.8f tau %.8f'
              % ((mode,) + par))
        if ex is not None:
            same_par = all(abs(a - b) < 1e-12 for a, b in zip(par, ex[0]))
            print('      the repaired-memo bank agrees on these parameters: %s' % same_par)
        rec = {'params': dict(zip(('H0', 'Om', 'ombh2', 'ns', 'tau'), par)),
               'banked_chi2_cmb': float(banked['chi2_cmb']), 'steps': {}}

        m0_full = camb_binned(*par, sum_ev=0.0)
        m0 = m0_full[ok]
        A0 = float((m0 @ F @ d) / (m0 @ F @ m0))
        r0 = d - A0 * m0
        chi0 = float(r0 @ F @ r0)
        rec['chi2_on_instrument_bins'] = chi0
        rec['A0'] = A0
        print('      chi2 on 60\'s %d bins: %.10f' % (int(ok.sum()), chi0))

        for st in STEPS:
            m1 = camb_binned(*par, sum_ev=st)[ok]
            A1 = float((m1 @ F @ d) / (m1 @ F @ m1))
            per = -2.0 * (F @ r0) * ((A1 * m1 - A0 * m0) / st)
            r1 = d - A1 * m1
            tot_fd = (float(r1 @ F @ r1) - chi0) / st
            s_all = float(np.abs(per).sum())
            s_low = float(np.abs(per[low_in]).sum())
            rec['steps']['%g' % st] = dict(
                step=st, sum_per_bin=float(per.sum()), fd_total=float(tot_fd),
                abs_sum_all=s_all, abs_sum_low=s_low,
                low_share=(s_low / s_all) if s_all else None,
                per_bin_low=[float(v) for v in per[low_in]],
                closure=abs(float(per.sum()) - float(tot_fd)) / max(abs(float(tot_fd)), 1e-30))
            print('        step %-6g  per-bin sum %+12.5f   fd total %+12.5f   closure %8.3f   '
                  'low |share| %.5f' % (st, per.sum(), tot_fd,
                                        rec['steps']['%g' % st]['closure'], s_low / s_all))
        out['modes'][mode] = rec

    # Ⓒ③ the two modes must SEPARATE
    if len(out['modes']) == 2:
        a, b = out['modes']['rd_min'], out['modes']['rd_camb']
        sep = {}
        for k in a['steps']:
            pa = np.asarray(a['steps'][k]['per_bin_low'], float)
            pb = np.asarray(b['steps'][k]['per_bin_low'], float)
            sep[k] = dict(max_abs_diff_low=float(np.abs(pa - pb).max()),
                          sum_diff=float(b['steps'][k]['sum_per_bin'] - a['steps'][k]['sum_per_bin']))
        out['separation'] = dict(per_step=sep,
                                 chi2_diff=float(b['chi2_on_instrument_bins']
                                                 - a['chi2_on_instrument_bins']))
        print('\n  Ⓒ③ THE TWO MODES SEPARATE -- the band the cache defect makes worth registering')
        print('      chi2 on the same bins differs by %+.6f' % out['separation']['chi2_diff'])
        for k in sorted(sep, key=float):
            print('      step %-6s max per-bin |difference| over the thirty-six %.6e'
                  % (k, sep[k]['max_abs_diff_low']))

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
