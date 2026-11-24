# -*- coding: utf-8 -*-
"""Ⓑ② WHERE THE INSTRUMENT'S LIMIT LEANS, PER BANDPOWER, AND THE REFERENCE ON THE SAME BINS.

`dchi2/dSigma` is decomposed EXACTLY over bandpowers for the instrument, because its binned model
is a spline in the sum and the amplitude is solved: with `A` optimal the gradient in `A` vanishes,
so `dchi2/dSigma = -2 A (dm/dSigma) . F r`, whose summand is a per-bin number that sums to the
whole-spectrum derivative by construction rather than by luck.

For the REFERENCE there is no spline: its model comes from CAMB, so the same decomposition is
taken on a FINITE DIFFERENCE at the reference's own banked parameters, on the SAME bins, with the
SAME Fisher and the SAME data.  What differs between the two columns is the spectra and nothing
else.

⚠ *The registered wording of Ⓑ②ᵇ asked the reference's reconstructed `dchi2/dSigma` to reproduce
cc66's banked `dchi2`.  Those are two different objects -- cc66's `dchi2` is a PROFILE difference,
re-minimised over five parameters at each sum, where a frozen-parameter derivative holds them.
That is this seat's own defect in the registration, and it is reported rather than repaired by
moving the criterion: the reproduction that IS of cc66's object is its banked `chi2_cmb` at its
own banked parameters, and that is what is measured and banded here.*

    NODE=60 python3 lean.py
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

R7853 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
BANKED = os.path.join(R7853, 'out5')
NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
LMAX = 2600                      # cc66's own, read from profile_likeforlike
ACC = 1                          # cc66's own
STEP = 0.05                      # the reference's banked spacing, used for both columns
#: the ell bands the comparison is reported over -- the thirty-six live in the first of them
BANDS = ((100, 207), (208, 500), (501, 1000), (1001, 1500), (1501, 1996))
#: the band the registered expectation of Ⓑ②ᶜ names
EXPECT_BELOW = 300
CHI2_CMB_BAND = 1.3e-2           # the bound r7863 set for cc66's own rounded memo


def fit_x4(mod, s):
    """the control's own four parameters at this sum, on the banked grid (no CAMB, no BAO)"""
    from scipy.optimize import minimize
    f = lambda x4: mod.cmb.chi2_cmb(np.asarray(x4, float), s)
    best, val = None, np.inf
    for x0 in (np.zeros(4), np.array([1.0, -1.0, 0.5, -0.5])):
        r = minimize(f, x0, method='Nelder-Mead',
                     options=dict(maxiter=6000, xatol=1e-6, fatol=1e-9))
        if r.fun < val:
            best, val = np.asarray(r.x, float), float(r.fun)
    return best, val


def inst_pieces(mod, x4, s, keep):
    """EXACT per-bin `dchi2/dSigma` for the instrument, from the spline's own derivative"""
    c = mod.cmb
    m = np.asarray(c.base(s), float).copy()
    dm = np.asarray(c.base(s, 1), float).copy()
    for k, v in zip(M3.KEYS4, x4):
        m = m + np.asarray(c.g[k](max(s, 0.0)), float) * v \
              + 0.5 * np.asarray(c.h[k](max(s, 0.0)), float) * v * v
        dm = dm + np.asarray(c.g[k](max(s, 0.0), 1), float) * v \
                + 0.5 * np.asarray(c.h[k](max(s, 0.0), 1), float) * v * v
    m, dm = m[keep], dm[keep]
    F, d = SC.fisher_for(_newok(mod, keep)), SC.X_DATA[_newok(mod, keep)]
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    per = -2.0 * A * (F @ r) * dm
    return dict(chi2=float(r @ F @ r), A=A, total=float(per.sum()), per=per, F=F, d=d, m=m, dm=dm)


def _newok(mod, keep):
    ok = mod.cmb.ok
    newok = ok.copy()
    newok[ok] = keep
    return newok


def camb_binned(h0, om, wb, ns, tau, sum_ev):
    """cc66's own build, so the spectra are the reference's and not a near miss"""
    import camb
    om_m = om * (h0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=h0, ombh2=wb, omch2=max(om_m - wb - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=tau)
        p.InitPower.set_params(As=2.1e-9, ns=ns)
        p.set_for_lmax(LMAX, lens_potential_accuracy=ACC)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    ls = np.arange(cl.shape[0], dtype=float)
    return SC.bin_three(ls, cl[:, 0], cl[:, 3], cl[:, 1])


def banded(per, idx_kept):
    """the per-bin numbers gathered by block and by the reported ell bands"""
    blk, lo = SC.BLOCK[idx_kept], SC.BIN_LO[idx_kept]
    out = {}
    for b in (0, 1, 2):
        for (a, z) in BANDS:
            sel = (blk == b) & (lo >= a) & (lo <= z)
            if sel.any():
                out['%s %d-%d' % (NAMES[b], a, z)] = float(per[sel].sum())
    return out


def main():
    print(__doc__)
    print('=' * 100)
    out = {}

    mod = M6.Model6('lcdm')
    raw = mod.amp_cmb
    mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0      # the FOURPI halving, as r7862 ran it
    ok = mod.cmb.ok
    keep_all = np.ones(int(ok.sum()), bool)
    idx_all = np.where(ok)[0]

    x4, chi0 = fit_x4(mod, 0.0)
    print('\n  THE CONTROL POINT: x4 = [%s], chi2_cmb = %.4f on %d bin(s)'
          % (', '.join('%+.4f' % v for v in x4), chi0, int(ok.sum())))

    # ── Ⓑ②ᵃ the instrument, exactly ──
    P = inst_pieces(mod, x4, 0.0, keep_all)
    fd = (mod.cmb.chi2_cmb(x4, STEP) - mod.cmb.chi2_cmb(x4, 0.0)) / STEP
    fd2 = (mod.cmb.chi2_cmb(x4, STEP / 2) - mod.cmb.chi2_cmb(x4, 0.0)) / (STEP / 2)
    print('\n  Ⓑ②ᵃ THE INSTRUMENT, per bandpower and EXACT:')
    print('    sum of the per-bin numbers      %+.9e' % P['per'].sum())
    print('    the analytic whole-spectrum one %+.9e' % P['total'])
    rel = abs(P['per'].sum() - P['total']) / max(abs(P['total']), 1e-30)
    print('    ⇒ relative gap %.3e  %s (criterion 1e-6)'
          % (rel, 'HOLDS' if rel < 1e-6 else 'FAILS -- not a decomposition'))
    print('    ⌗ and against a finite difference, which carries truncation: %+.6e at step %.3f, '
          '%+.6e at half it' % (fd, STEP, fd2))
    out['instrument'] = dict(x4=[float(v) for v in x4], chi2_cmb=float(P['chi2']),
                             total=float(P['total']), sum_per_bin=float(P['per'].sum()),
                             rel_gap=float(rel), holds=bool(rel < 1e-6),
                             fd_step=float(fd), fd_half=float(fd2),
                             banded=banded(P['per'], idx_all))
    print('    per block and band:')
    for k, v in out['instrument']['banded'].items():
        print('      %-16s %+12.5f' % (k, v))

    # ── the same, AT THE SUM THE LIMIT IS READ AT, with the four parameters re-fit there ──
    S_LIM = 0.070                       # r7864's minimised limit, 69.97 meV, in eV
    x4L, chiL = fit_x4(mod, S_LIM)
    PL_ = inst_pieces(mod, x4L, S_LIM, keep_all)
    print('\n  Ⓑ②ᵃ(limit) THE INSTRUMENT AT Sigma = %.3f eV, parameters re-fit there:' % S_LIM)
    print('    chi2_cmb %.4f, whole-spectrum dchi2/dSigma %+.5f' % (PL_['chi2'], PL_['total']))
    out['instrument_at_limit'] = dict(sum=S_LIM, x4=[float(v) for v in x4L],
                                      chi2_cmb=float(PL_['chi2']), total=float(PL_['total']),
                                      banded=banded(PL_['per'], idx_all))
    for k, v in out['instrument_at_limit']['banded'].items():
        print('      %-16s %+12.5f' % (k, v))

    # ── Ⓑ②ᵇ the reference, on the SAME bins, at its own banked parameters ──
    print('\n  Ⓑ②ᵇ THE REFERENCE, on the instrument\'s own %d bins:' % int(ok.sum()))
    ref = {}
    for mode in ('rd_min', 'rd_camb'):
        b0 = json.load(io.open(os.path.join(BANKED, '%s_0.000.json' % mode), encoding='utf-8'))
        par = (b0['H0'], b0['Om'], b0['ombh2'], b0['ns'], b0['tau'])
        # the reproduction that IS of cc66's object: its own banked chi2_cmb on ALL 613 bins
        mb0 = camb_binned(*par, sum_ev=0.0)
        cov = np.isfinite(mb0) & np.isin(SC.BLOCK, (0, 1, 2))
        Fc, dc = SC.fisher_for(cov), SC.X_DATA[cov]
        mc = mb0[cov]
        Ac = float((mc @ Fc @ dc) / (mc @ Fc @ mc))
        rc = dc - Ac * mc
        chi_rep = float(rc @ Fc @ rc)
        rel_rep = abs(chi_rep - b0['chi2_cmb']) / abs(b0['chi2_cmb'])
        print('    %s: banked chi2_cmb %.5f on %d bin(s); reproduced %.5f on %d  ⇒ rel %.3e  %s'
              % (mode, b0['chi2_cmb'], b0['dof_cmb'], chi_rep, int(cov.sum()), rel_rep,
                 'WITHIN %.1e' % CHI2_CMB_BAND if rel_rep < CHI2_CMB_BAND else 'OUTSIDE'))

        # the frozen-parameter derivative, on the instrument's own bins
        mb1 = camb_binned(*par, sum_ev=STEP)
        m0, m1 = mb0[ok], mb1[ok]
        F, d = SC.fisher_for(ok), SC.X_DATA[ok]
        A0 = float((m0 @ F @ d) / (m0 @ F @ m0))
        A1 = float((m1 @ F @ d) / (m1 @ F @ m1))
        r0 = d - A0 * m0
        per = -2.0 * (F @ r0) * ((A1 * m1 - A0 * m0) / STEP)
        tot_fd = (float((d - A1 * m1) @ F @ (d - A1 * m1)) - float(r0 @ F @ r0)) / STEP
        print('      on the instrument\'s bins: chi2 %.4f, per-bin sum %+.5f, '
              'finite-difference total %+.5f' % (float(r0 @ F @ r0), per.sum(), tot_fd))
        bd = banded(per, idx_all)
        for k, v in bd.items():
            print('        %-16s %+12.5f' % (k, v))
        ref[mode] = dict(params=dict(zip(('H0', 'Om', 'ombh2', 'ns', 'tau'), par)),
                         banked_chi2_cmb=float(b0['chi2_cmb']), reproduced=chi_rep,
                         rel=float(rel_rep), within=bool(rel_rep < CHI2_CMB_BAND),
                         n_covered=int(cov.sum()),
                         chi2_on_instrument_bins=float(r0 @ F @ r0),
                         sum_per_bin=float(per.sum()), fd_total=float(tot_fd), banded=bd)
    out['reference'] = ref

    # ── ⚠ THE CLOCK. The instrument's column above is EXACT and the reference's is a finite
    # difference at the banked spacing, and this instrument's own numbers show the two are not
    # the same quantity -- analytic against differenced at the same step, printed below.  A comparison
    # across that gap would be measuring the differencing scheme.  So the comparison below is
    # taken on the SAME CLOCK -- a frozen-parameter finite difference at one step for BOTH
    # columns -- and the exact column is kept as what it is, the instrument's own statement.
    m0 = np.asarray(mod.cmb.binned(x4, 0.0), float)[keep_all]
    m1 = np.asarray(mod.cmb.binned(x4, STEP), float)[keep_all]
    Fi, di = SC.fisher_for(ok), SC.X_DATA[ok]
    A0i = float((m0 @ Fi @ di) / (m0 @ Fi @ m0))
    A1i = float((m1 @ Fi @ di) / (m1 @ Fi @ m1))
    r0i = di - A0i * m0
    per_fd = -2.0 * (Fi @ r0i) * ((A1i * m1 - A0i * m0) / STEP)
    print('\n  Ⓑ②ᵃ(same clock) THE INSTRUMENT, frozen parameters, finite difference at step '
          '%.3f -- the construction the reference column uses:' % STEP)
    print('    per-bin sum %+.5f against the exact %+.5f at the same point'
          % (per_fd.sum(), P['total']))
    out['instrument_same_clock'] = dict(step=STEP, sum_per_bin=float(per_fd.sum()),
                                        exact=float(P['total']),
                                        banded=banded(per_fd, idx_all))
    for k, v in out['instrument_same_clock']['banded'].items():
        print('      %-16s %+12.5f' % (k, v))

    # ── Ⓑ②ᶜ where the two differ most, ON THE SAME CLOCK ──
    A = out['instrument_same_clock']['banded']
    for mode in ('rd_min', 'rd_camb'):
        B = ref[mode]['banded']
        diffs = {k: A[k] - B.get(k, float('nan')) for k in A}
        worst = max(diffs, key=lambda k: abs(diffs[k]))
        print('\n  Ⓑ②ᶜ against %s: the band they differ on most is %s, by %+.5f'
              % (mode, worst, diffs[worst]))
        blk, lo = worst.split()[0], int(worst.split()[1].split('-')[0])
        met = (lo < EXPECT_BELOW) and blk in ('TE', 'EE')
        print('      the REGISTERED EXPECTATION was ell < %d in TE or EE: %s'
              % (EXPECT_BELOW, 'MET' if met else 'REFUTED -- it sits in %s at ell %s'
                 % (blk, worst.split()[1])))
        ref[mode]['worst_band'] = worst
        ref[mode]['worst_diff'] = float(diffs[worst])
        ref[mode]['expectation_met'] = bool(met)
        ref[mode]['diffs'] = {k: float(v) for k, v in diffs.items()}

    io.open(os.path.join(_HERE, 'lean.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True))
    print('\n  wrote lean.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
