#!/usr/bin/env python3
"""** THE TT-ONLY CLOSURE: WHAT THE EXTENSION CHANGED, AND WHAT ONLY LOOKED CHANGED. **

Registered arm `Ⓑ②` asked that the extended harness, scored on TT alone, reproduce `r7838`'s own
TT numbers: the control's `95` per cent upper limit to within `1` meV of `277.7` and its `chi^2` at
the minimum to within `0.05` of `194.57`.  Its reachable negative was named as *a TT number that
moves when only TE and EE were added, which would mean the extension changed the TT scoring rather
than adding to it.*

** THE chi^2 HALF HOLDS AND THE LIMIT HALF DOES NOT, AND THE TWO HALVES FAIL AND HOLD FOR THE SAME
REASON. **  Everything DETERMINISTIC reproduces: the nine direction spectra are bit-identical, the
sum node set is the same eight, the TT lensing operator is bit-identical, the Fisher matrix is
bit-identical, and the two models' chi^2 agree to the last few bits.  The one thing that moved is a
POSTERIOR QUANTILE read off a finite chain -- and this script measures that quantile's own
Monte-Carlo error, which is LARGER than the tolerance the arm was registered with.

** SO THE ARM FAILS ON A CRITERION I WROTE TIGHTER THAN THE INSTRUMENT IT JUDGES. **  That is
reported as a failure with the criterion unchanged, because the criterion is what was registered;
but the negative it was built to catch is ruled out by measurement rather than by argument, and the
thing that is actually wrong is the tolerance.  *A 1 meV window on a quantile whose standard error
is 1.7 meV could not have been met by a rerun of `r7838`'s own code against itself.*

** AND A THIRD REALISATION IS REPORTED HERE BECAUSE IT PASSES. **  The sampler's proposal was found
mis-scaled by `1812` (see `sampler3.laplace_cov`) and fixed; re-run on the fixed sampler, the same
TT-only closure returns `277.7` meV -- `r7838`'s figure to the printed digit, inside the registered
`1` meV.  *It is reported precisely so that the failing realisation is not quietly replaced by the
passing one.*  Three realisations of one posterior read `275.3`, `277.7` and `277.7` against a
standard error of about `1.7`: that is consistency, not restoration, and nothing here licenses the
claim that the fix RECOVERED the number.  The arm stands as registered and as first measured:
FAILED on its limit half.  What the third run adds is that the criterion is satisfiable and
satisfied on some draws and not others -- which is what a tolerance below the instrument's own
precision means.

Writes `closure_tt.json`.  Run from this directory with `SUM_ARMS=lcdm`.
"""
import json
import os
import sys
import time

import numpy as np
import scipy.linalg

_HERE = os.path.dirname(os.path.abspath(__file__))
_R38 = os.path.join(os.path.dirname(_HERE),
                    'r7838_60_the_lensing_operator_moves_with_the_sum_and_the_profile_becomes_a_'
                    'sampler')
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'planck_tt_likelihood'))

KEYS9 = ('base', 'H0p', 'H0m', 'OMp', 'OMm', 'WBp', 'WBm', 'NSp', 'NSm')
TAG = {'base': 'S000'}


def _rel(a, b):
    """max |b/a - 1| over two spectra that must share their multipole grid"""
    la, lb = np.asarray(a['ls'], float), np.asarray(b['ls'], float)
    if la.shape != lb.shape or not np.array_equal(la, lb):
        return None
    return float(np.max(np.abs(np.asarray(b['Dl'], float) / np.asarray(a['Dl'], float) - 1.0)))


def directions(pol_dir):
    """① the nine banked lcdm direction spectra against the ones this revision generated"""
    out = {}
    for k in KEYS9:
        a = np.load(os.path.join(_R38, '..', 'refit_grid185', f'lcdm_{k}.npz'), allow_pickle=True)
        b = np.load(os.path.join(pol_dir, f"lcdm_{TAG.get(k, k)}.npz"), allow_pickle=True)
        out[k] = _rel(a, b)
    return out


def fisher_pair():
    """② the TT Fisher built from the TT sub-block, and from the full 613-bin covariance masked

    The old module takes the `215 x 215` TT sub-block, drops the uncovered rows and inverts.  The
    new one drops every TE and EE row AND the uncovered TT rows from the FULL `613 x 613`
    covariance, then inverts.  ** THOSE ARE THE SAME OPERATION: a sub-block of a sub-block is a
    sub-block, and marginalising twice in a row is marginalising once. **  Asserting it is how the
    claim stops being an argument.
    """
    import chi2_of_spectrum as OLD
    import score_ttteee as NEW
    z = np.load(os.path.join(_R38, '..', 'refit_grid185', 'lcdm_base.npz'), allow_pickle=True)
    ko = np.isfinite(OLD.bin_spectrum(z['ls'], z['Dl']))
    cov = OLD.COV_TT[np.ix_(ko, ko)]
    Fo = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(ko.sum())))
    Fo = 0.5 * (Fo + Fo.T)
    zero = np.zeros_like(np.asarray(z['Dl'], float))
    kn = np.isfinite(NEW.bin_three(z['ls'], z['Dl'], zero, zero)) & np.isin(NEW.BLOCK, [0])
    Fn = NEW.fisher_for(kn)
    return dict(bins_old=int(ko.sum()), bins_new=int(kn.sum()),
                same_mask=bool(np.array_equal(ko, kn[:len(ko)])),
                max_abs=float(np.max(np.abs(Fn - Fo))), bitwise=bool(np.array_equal(Fn, Fo)))


def chi2_agreement(m8, m42, x0, n=200, seed=1):
    """③ the two models' chi^2 at the same points, at FULL precision and not at printing precision

    ** THE DIFFERENCE IS SUMMATION ORDER AND NOTHING ELSE. **  The same Fisher contraction is run
    over a `613`-long vector masked to `185` entries in one model and over a `185`-long vector in
    the other; the last bits of the sum depend on the order the terms arrive in.  *A Metropolis
    chain is chaotic in exactly those bits:* the first time a proposal's log-ratio lands within
    `1e-13` of its acceptance threshold the two chains take different steps, and from there they are
    independent realisations of one posterior rather than one realisation computed twice.
    """
    rng = np.random.default_rng(seed)
    step = np.array([0.8, 0.011, 2.5e-4, 6e-3, 0.084])
    pts = [np.asarray(x0, float)] + [np.asarray(x0, float) + rng.normal(0, 1, 5) * step
                                     for _ in range(n - 1)]
    d, exact = [], 0
    for x in pts:
        a, b = m8.chi2(x), m42.chi2(x)
        exact += int(a == b)
        d.append(abs(b - a))
    d = np.asarray(d)
    return dict(points=int(n), bitwise_equal=int(exact), max_abs=float(d.max()),
                median_abs=float(np.median(d)),
                at_best_fit=dict(old=float(m8.chi2(x0)), new=float(m42.chi2(x0)),
                                 abs_diff=float(abs(m42.chi2(x0) - m8.chi2(x0)))))


def quantile_error(chain, ess, q=0.95):
    """④ the Monte-Carlo standard error of the `95` per cent upper limit, from the chain itself

    The standard error of a sample quantile is `sqrt(q(1-q)/N_eff) / f(x_q)`.  `N_eff` is the
    chain's own effective sample size for the sum -- NOT its length, which would understate the
    error by the autocorrelation -- and `f` is the posterior density at the quantile, estimated
    from the same draws on Silverman's width.  ** THE SIX CHAINS' OWN SPREAD IS REPORTED BESIDE IT
    as the check that the formula is not flattering itself. **
    """
    s = chain.reshape(-1, 5)[:, 4]
    xq = float(np.quantile(s, q))
    h = 1.06 * float(s.std(ddof=1)) * len(s) ** -0.2
    f = float(np.mean(np.exp(-0.5 * ((s - xq) / h) ** 2)) / (h * np.sqrt(2 * np.pi)))
    per = [float(np.quantile(chain[i, :, 4], q) * 1000.0) for i in range(chain.shape[0])]
    return dict(upper95_mev=xq * 1000.0, ess=float(ess),
                mcse_mev=float(1000.0 * np.sqrt(q * (1 - q) / ess) / f),
                per_chain_mev=per, per_chain_range_mev=float(max(per) - min(per)))


def main():
    t0 = time.time()
    # ⛔ ** THE BANK NO LONGER LIVES IN `/tmp`, AT `r7857`'s ORDER ③. **  *Three banks on this
    #   line were lost to a `/tmp` default -- the `555`-bin mask, the Phi bandpowers and this
    #   grid -- so what the scorers read is COMMITTED beside the instrument and this default
    #   points at it, computed from this file's own location rather than from an absolute path
    #   that would differ between containers.  The environment variable still overrides it.
    _BANK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         'bank', 'pol_grid')
    assert os.path.isdir(_BANK), _BANK      # two dirnames: this file sits one below `beyond_the_wall`
    pol = os.environ.get('POL_DIR', _BANK)
    os.environ.setdefault('SUM_ARMS', 'lcdm')
    sys.path.insert(0, _R38)
    import model as M8
    import model3 as M42

    jA = json.load(open(os.path.join(_R38, 'sampler.json')))['lcdm_bounded']
    jB = json.load(open(os.path.join(_HERE, 'sampler3_ttonly.json')))['lcdm_bounded']
    x0 = jA['best_fit']['x']

    print('  ① the nine direction spectra', flush=True)
    dirs = directions(pol)
    print('     max |dDl/Dl| over all nine: %.3e'
          % max(v for v in dirs.values() if v is not None), flush=True)

    print('  ② the sum node set', flush=True)
    nodes = dict(r7838=[float(s) for s in sorted(M8.SPEC)],
                 r7842=[float(s) for s in M42.available_sums(('lcdm',))])
    nodes['identical'] = bool(nodes['r7838'] == nodes['r7842'])
    print('     %s   identical: %s' % (nodes['r7842'], nodes['identical']), flush=True)

    print('  ③ the TT lensing operator', flush=True)
    a = np.load(os.path.join(_R38, 'ratio_grid.npz'))
    b = np.load(os.path.join(_HERE, 'ratio_grid3.npz'))
    op = dict(ls_identical=bool(np.array_equal(np.asarray(a['ls']), np.asarray(b['ls']))),
              grid_identical=bool(np.array_equal(np.asarray(a['grid']), np.asarray(b['grid']))),
              max_abs=float(np.max(np.abs(np.asarray(b['ratio_tt'], float)
                                          - np.asarray(a['ratio'], float)))))
    op['bitwise'] = bool(op['max_abs'] == 0.0 and op['ls_identical'] and op['grid_identical'])
    print('     max |ratio_tt - ratio| = %.3e   bitwise: %s' % (op['max_abs'], op['bitwise']),
          flush=True)

    print('  ④ the Fisher matrix', flush=True)
    fish = fisher_pair()
    print('     %d bins both ways; bitwise identical: %s' % (fish['bins_new'], fish['bitwise']),
          flush=True)

    print('  ⑤ the two models’ chi^2 over 200 points', flush=True)
    m8 = M8.Model('lcdm')
    m42 = M42.Model3('lcdm', blocks=(0,))
    agree = chi2_agreement(m8, m42, x0)
    print('     max %.3e, median %.3e, bitwise equal at %d of 200'
          % (agree['max_abs'], agree['median_abs'], agree['bitwise_equal']), flush=True)

    print('  ⑥ the quantile’s own Monte-Carlo error', flush=True)
    cA = np.load(os.path.join(_R38, 'chain_lcdm_b_free.npz'), allow_pickle=True)
    cB = np.load(os.path.join(_HERE, 'chain3_lcdm_b_0.npz'), allow_pickle=True)
    kA, kB = list(cA.keys())[0], list(cB.keys())[0]
    qA = quantile_error(np.asarray(cA[kA], float), jA['diagnostics']['MNU']['ess'])
    qB = quantile_error(np.asarray(cB[kB], float), jB['diagnostics']['MNU']['ess'])
    # the third realisation: the same closure on the FIXED sampler, reported because it passes
    qC, jC = None, None
    _fx = os.path.join(_HERE, 'sampler3_ttonly_fixed.json')
    _fc = os.path.join(_HERE, 'chain3_lcdm_b_0_fixed.npz')
    if os.path.exists(_fx) and os.path.exists(_fc):
        jC = json.load(open(_fx))['lcdm_bounded']
        cC = np.load(_fc, allow_pickle=True)
        qC = quantile_error(np.asarray(cC[list(cC.keys())[0]], float),
                            jC['diagnostics']['MNU']['ess'])
    comb = float(np.hypot(qA['mcse_mev'], qB['mcse_mev']))
    gap = abs(qB['upper95_mev'] - qA['upper95_mev'])
    print('     r7838 %.1f +/- %.2f meV (six chains span %.1f)'
          % (qA['upper95_mev'], qA['mcse_mev'], qA['per_chain_range_mev']), flush=True)
    print('     r7842 %.1f +/- %.2f meV (six chains span %.1f)'
          % (qB['upper95_mev'], qB['mcse_mev'], qB['per_chain_range_mev']), flush=True)
    print('     the two differ by %.2f meV = %.2f combined standard errors; the arm asked for 1'
          % (gap, gap / comb), flush=True)
    if qC is not None:
        print('     the fixed sampler %.1f +/- %.2f meV (six chains span %.1f) -- INSIDE the '
              'registered 1 meV, reported because it passes'
              % (qC['upper95_mev'], qC['mcse_mev'], qC['per_chain_range_mev']), flush=True)
        _three = [qA['upper95_mev'], qB['upper95_mev'], qC['upper95_mev']]
        print('     three realisations of one posterior: %s meV, spread %.2f against a standard '
              'error of about %.2f'
              % (', '.join('%.1f' % v for v in _three), max(_three) - min(_three),
                 float(np.mean([qA['mcse_mev'], qB['mcse_mev'], qC['mcse_mev']]))), flush=True)

    out = dict(
        arm='Ⓑ②',
        registered=dict(limit_mev=277.7, limit_tol_mev=1.0, chi2=194.57, chi2_tol=0.05),
        directions=dirs,
        directions_max_rel=max(v for v in dirs.values() if v is not None),
        nodes=nodes,
        operator=op,
        fisher=fish,
        chi2=agree,
        r7838=qA, r7842=qB, r7842_fixed_sampler=qC,
        combined_mcse_mev=comb, limit_gap_mev=gap, limit_gap_in_mcse=gap / comb,
        three_realisations=([qA['upper95_mev'], qB['upper95_mev'], qC['upper95_mev']]
                            if qC is not None else None),
        chains=dict(burn_accept_r7838=jA['burn_accept'], burn_accept_r7842=jB['burn_accept'],
                    burn_accept_identical=bool(jA['burn_accept'] == jB['burn_accept']),
                    accept_r7838=jA['accept'], accept_r7842=jB['accept'],
                    chi2min_r7838=jA['best_fit']['chi2'], chi2min_r7842=jB['best_fit']['chi2'],
                    chi2min_identical=bool(jA['best_fit']['chi2'] == jB['best_fit']['chi2'])),
        verdict=dict(
            chi2_half_holds=bool(abs(jB['best_fit']['chi2'] - 194.57) <= 0.05),
            limit_half_holds=bool(gap <= 1.0),
            limit_half_holds_on_fixed_sampler=(
                bool(abs(qC['upper95_mev'] - 277.7) <= 1.0) if qC is not None else None),
            scoring_unchanged=bool(op['bitwise'] and fish['bitwise']
                                   and agree['max_abs'] < 1e-10 and nodes['identical']),
            tolerance_tighter_than_instrument=bool(1.0 < comb)),
        seconds=time.time() - t0)
    with open(os.path.join(_HERE, 'closure_tt.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote closure_tt.json in %.1f s' % out['seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
