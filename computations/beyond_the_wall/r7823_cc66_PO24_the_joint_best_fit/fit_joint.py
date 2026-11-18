#!/usr/bin/env python3
r"""r7823 (cc66) -- PO-24's JOINT BEST FIT.  One arm per invocation, resumable.

Usage:  python3 fit_joint.py <lcdm|cr> [budget]

** THE SPLIT IS 60's, REUSED AND NOT REINVENTED (r7820). **  Planck plik_lite TT below the
`PlanckActCut` multipole, ACT DR6 CMB-only TT above it, each block carrying its OWN free
amplitude profiled analytically, and NO cross-covariance because no multipole is used twice.
60's Ⓒ③ established that the split must be made on WINDOW SUPPORT and not on an effective
multipole; that selection is reproduced here from the same banked window matrix.

** WHAT IS NEW HERE IS THE BASELINE. **  r7820 measured the tilt against a BANKED spectrum and
recorded its own standing limit: *"Neither banked control is a best fit to plik_lite ... these
remain degeneracy-fit numbers ... What would settle it is a best fit to the joint data, which the
harness's fit.py exists to do and which this revision did not run."*  This runs it: the baseline
is CAMB at a cosmology MINIMISED on the joint data, five parameters free.

⌗ `run()` and `cr_supp()` are copied VERBATIM from `computations/planck_tt_likelihood/fit.py`
rather than imported, because that module builds a `PlanckLitePy` against `/tmp/planckdata` at
import time and this container has no such path.  The physics is the harness's, unchanged, with
`z_onset=6797.0` as it stands there.
"""
import json
import os
import sys
import warnings

import numpy as np
import scipy.linalg
from scipy.integrate import quad
from scipy.optimize import minimize

warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                               # noqa: E402

AD = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

LMAX = 3600                      # CAMB reach for the fit; covers every kept ACT window with margin
LS = np.arange(2, LMAX + 1).astype(float)
C_KMS = 299792.458


# ------------------------------------------------------------------ the harness's own physics
def run(H0, ombh2, omch2, As, ns, tau=0.054):
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, tau=tau)
    p.InitPower.set_params(As=As, ns=ns)
    p.set_for_lmax(LMAX + 400, lens_potential_accuracy=0)
    p.set_accuracy(AccuracyBoost=1.0, lSampleBoost=1.0)
    r = camb.get_results(p)
    d = r.get_cmb_power_spectra(p, CMB_unit='muK')['total']
    return d, r.get_derived_params()


def cr_supp(d, dp, H0, ombh2, omch2, z_onset=6797.0):
    Om = (ombh2 + omch2) / (H0 / 100) ** 2
    OL = 1 - Om
    z_rec = dp['zstar']
    a_rec = 1 / (1 + z_rec)
    Or = Om / (1 + dp['zeq'])
    R_rec = 31500 * ombh2 / (2.7255 / 2.7) ** 4 / (1 + z_rec)
    Rf = lambda a: R_rec * (a / a_rec)                                     # noqa: E731
    g = lambda a: (Rf(a) ** 2 / (1 + Rf(a)) + 8 / 9) / (6 * (1 + Rf(a)))   # noqa: E731
    H = lambda a, rad: H0 * np.sqrt(Or / a ** 4 * rad + Om / a ** 3 + OL)  # noqa: E731
    a_s = 1 / (1 + z_onset)
    IL, _ = quad(lambda a: g(a) / H(a, 1.0), 1e-9, a_rec, limit=120)
    IC, _ = quad(lambda a: g(a) / H(a, 0.0), a_s, a_rec, limit=120)
    sL, _ = quad(lambda a: C_KMS / (a ** 2 * H(a, 1.0) * np.sqrt(3 * (1 + Rf(a)))),
                 1e-9, a_rec, limit=120)
    sC, _ = quad(lambda a: C_KMS / (a ** 2 * H(a, 0.0) * np.sqrt(3 * (1 + Rf(a)))),
                 a_s, a_rec, limit=120)
    r = (np.sqrt(IC / IL)) / (sC / sL)
    full = np.arange(d.shape[0])
    sel = (full > 1400) & (full < 2400)
    co = np.polyfit(full[sel].astype(float) ** 2, np.log(np.maximum(d[sel, 0], 1e-12)), 1)
    lD = np.sqrt(-1 / co[0])
    ell = np.arange(2, LMAX + 1)
    return np.exp(-(ell / lD) ** 2 * (r ** 2 - 1)), r, lD


# ------------------------------------------------------------------ 60's split, reproduced
def _fisher(cov):
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(cov.shape[0]))
    return 0.5 * (F + F.T)


AZ = np.load(os.path.join(AD, 'act_dr6_cmbonly.npz'), allow_pickle=True)
A_ELL, A_DL, A_WIN, A_WL = AZ['ell_TT'], AZ['Dl_TT'], AZ['win_TT'], AZ['win_ell']
A_COV = AZ['cov'][:45, :45]
CUT = int(open(os.path.join(AD, 'likelihood_source', 'PlanckActCut.yaml'),
               encoding='utf-8').read().split('lmax_cuts:')[1].split()[0])

_probe = np.ones_like(LS)
P_KEEP = np.isfinite(CS.bin_spectrum(LS, _probe)) & (CS.BIN_HI < CUT)
P_LMAX = int(CS.BIN_HI[P_KEEP].max())
A_SUPP_MIN = np.array([A_WL[A_WIN[:, i] > 0].min() for i in range(A_WIN.shape[1])])
A_SUPP_MAX = np.array([A_WL[A_WIN[:, i] > 0].max() for i in range(A_WIN.shape[1])])
# r7820's own upper bound: its banked baseline reached l = 3200, and a bandpower whose support
# leaves the reach is modelled with a flat extrapolation.  Kept here for LIKE-FOR-LIKE with that
# revision even though CAMB reaches further -- the wider selection is a robustness arm in measure.py.
REACH_R7820 = 3200.0
A_KEEP = (A_SUPP_MIN > P_LMAX) & (A_SUPP_MAX <= REACH_R7820)

P_F = _fisher(CS.COV_TT[np.ix_(P_KEEP, P_KEEP)])
P_D = CS.X_DATA[P_KEEP]
A_F = _fisher(A_COV[np.ix_(A_KEEP, A_KEEP)])
A_D = A_DL[A_KEEP]
A_W = A_WIN[:, A_KEEP]


def act_bin(dl):
    return A_W.T @ np.interp(A_WL, LS, dl)


def planck_bin(dl):
    return CS.bin_spectrum(LS, dl)[P_KEEP]


def block_chi2(d, F, m):
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r), A


def joint_chi2_of(dl):
    cp, ap = block_chi2(P_D, P_F, planck_bin(dl))
    ca, aa = block_chi2(A_D, A_F, act_bin(dl))
    return cp + ca, cp, ca, ap, aa


def theory(pv, cr):
    H0, ombh2, omch2, As9, ns = pv
    d, dp = run(H0, ombh2, omch2, As9 * 1e-9, ns)
    dl = d[2:LMAX + 1, 0].copy()
    if cr:
        s, _, _ = cr_supp(d, dp, H0, ombh2, omch2)
        dl = dl * s
    return dl


def objective(pv, cr):
    H0, ombh2, omch2, As9, ns = pv
    if not (55 < H0 < 85 and 0.018 < ombh2 < 0.026 and 0.09 < omch2 < 0.16
            and 1.5 < As9 < 3.0 and 0.85 < ns < 1.25):
        return 1e6
    try:
        return joint_chi2_of(theory(pv, cr))[0]
    except Exception:
        return 1e6


if __name__ == '__main__':
    which = sys.argv[1]
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    dest = os.path.join(OUT, f'fit_{which}.npz')
    if os.path.exists(dest):
        z = np.load(dest)
        print(f"  skip {which} (done): chi2={float(z['fun']):.2f}  x={np.round(z['x'], 6)}")
        sys.exit(0)
    print(f"  JOINT SPLIT: Planck {int(P_KEEP.sum())} bins to l={P_LMAX}; "
          f"ACT {int(A_KEEP.sum())} bandpowers, support "
          f"{A_SUPP_MIN[A_KEEP].min():.0f}..{A_SUPP_MAX[A_KEEP].max():.0f}  (cut {CUT})")
    x0 = json.load(open(os.path.join(ROOT, 'computations', 'planck_tt_likelihood',
                                     f'{which}.json'), encoding='utf-8'))['x']
    print(f"  start from the harness's Planck-only best fit: {np.round(x0, 6)}")
    n = [0]

    def f(pv):
        n[0] += 1
        v = objective(pv, which == 'cr')
        if n[0] % 20 == 0:
            print(f"    eval {n[0]:4d}  chi2={v:12.3f}  x={np.round(pv, 5)}", flush=True)
        return v

    r = minimize(f, x0, method='Nelder-Mead',
                 options={'maxfev': budget, 'xatol': 2e-3, 'fatol': 0.5})
    c, cp, ca, ap, aa = joint_chi2_of(theory(r.x, which == 'cr'))
    np.savez(dest, x=r.x, fun=float(r.fun), chi2=c, chi2_planck=cp, chi2_act=ca,
             A_planck=ap, A_act=aa, nfev=n[0], x0=np.asarray(x0),
             n_planck=int(P_KEEP.sum()), n_act=int(A_KEEP.sum()), cut=CUT, lmax=LMAX)
    print(f"  {which}: joint chi2={c:.2f}  (Planck {cp:.2f} / {int(P_KEEP.sum())}, "
          f"ACT {ca:.2f} / {int(A_KEEP.sum())})  x={np.round(r.x, 6)}  after {n[0]} evals")
