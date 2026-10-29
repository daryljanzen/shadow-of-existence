"""r7637+70: THE OWN-COMB BAND STATISTIC -- one shared function for the excess/step family (69's ruling 1).

The step receipt's `band_excess('mean')` reads each arm on x = l/l_A, takes a running-mean envelope one unit wide,
and in each of the seven `r6959` q-bands (0.85-5.75, width 0.70) the RMS of (D - e)/e; the excess is
RMS_arm / RMS_control - 1.  A 0.70-wide band holds less than one comb period, so its RMS depends on WHICH part of
the cycle it covers.  When the two arms' combs differ in period, the two arms' bands cover different parts of
the cycle and the ratio beats.  On the arm of record the fitted periods are 1.0045 (arm) and 1.0092 (control).

THE OWN-COMB READING.  Each bank's comb, A cos(2 pi x / T + phi), is fitted with the retention-law receipt's own
period fitter and r7055's phase fit, both lifted unchanged.  The ARM is carried onto the CONTROL's comb
coordinate,
    u = T_c * (x / T_a + dphi / 2 pi),    dphi = phi_a - phi_c wrapped to (-pi, pi],
and the control's u is its own x.  Each arm's envelope window is one of ITS OWN periods: 1.0 on the control and
T_a / T_c on the arm.  The band RMS is then read on the same u-interval in both arms, so each band covers the
same comb phase in both.  With T_a = T_c and dphi = 0 this IS the shared-comb statistic, exactly.

    band_excess_own(banks, QE)    -> (excess per band, {arm: (T, phi, amp)})
    band_excess_shared(banks, QE) -> the step receipt's statistic, for comparison
    step(E) = E[0] - mean(E[1:]);  rise(E, QE) = OLS slope of E[1:] against band centre
    null(banks, QE, stat, A)      -> r7055's injection: each bank's own envelope, IDENTICAL amplitude A on both
                                     arms at each bank's own fitted comb, a common phase over 24 values; the
                                     statistic refits the combs itself.
"""
import ast
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RC = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
LAW = os.path.join(RC, 'P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_'
                       'and_the_law_has_no_fitted_coefficient.py')
R7055 = os.path.join(RC, 'P15_the_phase_systematic_leaves_the_step_standing_and_carries_a_third_of_the_retention_'
                         'slope_through_a_phase_drift_between_the_sources.py')
LO, HI = 0.85, 5.75


def _lift(path, names, ns):
    tree = ast.parse(open(path, encoding='utf-8').read())
    body = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in body} == set(names), f'{os.path.basename(path)}: {names}'
    exec(compile(ast.Module(body=body, type_ignores=[]), path, 'exec'), ns)
    return ns


_L = _lift(LAW, ['env_a', 'osc', '_fit', 'fit_period'], {'np': np, 'LO': LO, 'HI': HI})
_P = _lift(R7055, ['phase'], {'np': np})
env_a, osc, _fit, fit_period, phase = _L['env_a'], _L['osc'], _L['_fit'], _L['fit_period'], _P['phase']


def comb(x, y):
    """(envelope, T, phi, amp) of one bank -- r7055's `comb_params`, on the lifted functions."""
    o = osc(x, y)
    T = fit_period(x, o)
    m = (x >= LO) & (x <= HI)
    return env_a(x, y), T, phase(x, o, T), _fit(x[m], o[m], T)[0]


def _rms(xs, o, a, b):
    return float(np.std(np.interp(np.linspace(a, b, 400), xs, o)))


def band_excess_shared(banks, QE):
    """The step receipt's `band_excess('mean')`: both arms on their own x, a one-unit envelope."""
    R = {t: np.array([_rms(x, osc(x, y, 1.0), a, b) for a, b in zip(QE[:-1], QE[1:])])
         for t, (x, y) in banks.items()}
    return R['cr'] / R['lcdm'] - 1.0


def band_excess_own(banks, QE):
    """The own-comb reading: the arm carried onto the control's comb coordinate before the bands are cut."""
    P = {t: comb(*banks[t])[1:] for t in banks}
    Tc, pc, _ = P['lcdm']
    Ta, pa, _ = P['cr']
    dphi = (pa - pc + np.pi) % (2 * np.pi) - np.pi
    xc, yc = banks['lcdm']
    xa, ya = banks['cr']
    oc = osc(xc, yc, 1.0)
    oa = osc(xa, ya, Ta / Tc)
    ua = Tc * (xa / Ta + dphi / (2 * np.pi))          # the arm's own x, on the control's comb coordinate
    Rc = np.array([_rms(xc, oc, a, b) for a, b in zip(QE[:-1], QE[1:])])
    Ra = np.array([_rms(ua, oa, a, b) for a, b in zip(QE[:-1], QE[1:])])
    return Ra / Rc - 1.0, P


def step(E):
    return float(E[0] - np.mean(E[1:]))


def rise(E, QE):
    c = 0.5 * (QE[:-1] + QE[1:])
    return float(np.polyfit(c[1:], E[1:], 1)[0])


def null(banks, QE, stat, A=0.5, nph=24):
    """r7055's injection, fed to `stat` (which refits the combs on what it is fed).  Returns the per-phase
    (step, rise) of a spectrum pair whose true excess is zero in every band."""
    base = {t: comb(*banks[t]) for t in banks}
    out = []
    for p in np.linspace(0, 2 * np.pi, nph, endpoint=False):
        inj = {}
        for t, (x, _) in banks.items():
            e, T, ph, _ = base[t]
            inj[t] = (x, e * (1 + A * np.cos(2 * np.pi * x / T + ph + p)))
        E = stat(inj, QE)
        E = E[0] if isinstance(E, tuple) else E
        out.append((step(E), rise(E, QE)))
    return np.array(out)
