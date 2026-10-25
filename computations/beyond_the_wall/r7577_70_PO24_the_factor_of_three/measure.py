#!/usr/bin/env python3
"""r7577+70 -- PO-24's open half: the instrument's own damping ratio from the banked DAMPX pairs, the alpha it
implies against route A's exp[-(DAMPX-1)(l/1951.9)^2], closure of route A with alpha measured, and the magnitude
at the settled endpoint r = 0.9918 on the faithful route.  Banked spectra and the existing likelihood only."""
import math, os, sys
import numpy as np
import scipy.linalg
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
L_D, L_PIV = 1951.9, 1000.0
lc = 0.5 * (CS.BIN_LO + CS.BIN_HI)

def load(stem):
    z = np.load(os.path.join(SP, stem + '.npz'), allow_pickle=True)
    return z['ls'].astype(float), z['Dl'].astype(float)

def alpha(stem0, stem1, fac, lo=500, hi=2000):
    l0, D0 = load(stem0); l1, D1 = load(stem1)
    assert np.allclose(l0, l1)
    m = (l0 >= lo) & (l0 <= hi) & (D0 > 0) & (D1 > 0)
    x = fac * (l0[m] / L_D) ** 2; y = np.log(D1[m] / D0[m])
    A = np.vstack([np.ones_like(x), -x]).T
    (c, a), res, *_ = np.linalg.lstsq(A, y, rcond=None)
    rms = float(np.sqrt(np.mean((y - (c - a * x)) ** 2)))
    return float(a), float(c), rms

def refit(b_, d_, keep):
    n_ = int(keep.sum())
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(keep, keep)]), np.identity(n_)); F = 0.5 * (F + F.T)
    b, d = b_[keep], d_[keep]
    X = np.vstack([b, b * np.log(lc[keep] / L_PIV)]).T
    G = X.T @ F @ X; th = np.linalg.solve(G, X.T @ F @ d)
    r = d - X @ th; c2 = float(r @ F @ r)
    cov = np.linalg.inv(G); dn = th[1] / th[0]
    sdn = math.sqrt(cov[1, 1]) / abs(th[0])
    return n_, c2, dn, sdn

base = CS.X_DATA.copy()
def route_A(fac, a):
    return base * np.exp(-a * fac * (lc / L_D) ** 2)

FAC7, FAC4 = 1.174306 - 1, 1.156766 - 1
a7, c7, rms7 = alpha('r7099_lcdm_LEAFREC1_DAMPX1.000', 'r7099_lcdm_LEAFREC1_DAMPX1.174', FAC7)
a4, c4, rms4 = alpha('r4494_lcdm_DAMPX1.000', 'r4494_lcdm_DAMPX1.157', FAC4)
print(f'  T1  alpha (r7099 pair, l 500-2000) = {a7:.3f}  (const {c7:+.4f}, rms {rms7:.4f})')
print(f'  T3  alpha (r4494 pair)            = {a4:.3f}  ratio {a4/a7:.3f}')
for lo, hi in ((500, 1200), (1200, 2000)):
    print(f'      alpha over {lo}-{hi}: {alpha("r7099_lcdm_LEAFREC1_DAMPX1.000","r7099_lcdm_LEAFREC1_DAMPX1.174",FAC7,lo,hi)[0]:.3f}')
win = [(100, 1760), (700, 1760)]
f = np.isfinite(base)
print('  T2  route A closure (the C62 refit, amplitude + tilt):')
for a, lab in ((1.0, 'A as built (alpha=1)'), (a7, f'A, alpha measured ({a7:.2f})')):
    for lo, hi in win:
        k = f & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
        n, c2, dn, sdn = refit(base, route_A(FAC7, a), k)
        print(f'      {lab:28s} {lo}-{hi}: {c2/n:.3f} chi2/bin  dn {dn:+.4f} +/- {sdn:.4f}')
R2 = 0.9918 ** 2
print(f'  MAGNITUDE at r = 0.9918 (DAMPX-1 = {R2-1:+.5f}), faithful shape alpha = {a7:.3f}:')
for lo, hi in win + [(1000, 2508)]:
    k = f & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
    n, c2, dn, sdn = refit(base, route_A(R2 - 1, a7), k)
    nA, c2A, dnA, sdnA = refit(base, route_A(R2 - 1, 1.0), k)
    print(f'      {lo}-{hi}: {c2/n:.4f} chi2/bin (total {c2:.2f} over {n})  dn {dn:+.4f} +/- {sdn:.4f} ({abs(dn)/sdn:.1f} sigma)   [alpha=1: {c2A/nA:.4f}, dn {dnA:+.4f}]')

# REFINEMENT (reported beside the registered alpha-Gaussian, not replacing it): route B's own measured ratio,
# ln R(l) scaled linearly to the endpoint (T3 licenses the linearity), binned with plik_lite's weights.
l0, D0 = load('r7099_lcdm_LEAFREC1_DAMPX1.000'); l1, D1 = load('r7099_lcdm_LEAFREC1_DAMPX1.174')
lnR = np.log(D1 / D0)
def route_Bratio(fac):
    s = np.exp(lnR * fac / FAC7)
    return base * CS.bin_spectrum(l0, D0 * s) / CS.bin_spectrum(l0, D0)
print('  REFINEMENT: route B\'s measured ratio itself (l <= 2200 instrument ceiling):')
for fac, lab in ((FAC7, 'DAMPX 1.174 (B, reproduce 0.92)'), (R2 - 1, 'r = 0.9918 (the magnitude)')):
    for lo, hi in win:
        k = f & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
        mod = route_Bratio(fac); k &= np.isfinite(mod)
        n, c2, dn, sdn = refit(base, mod, k)
        print(f'      {lab:32s} {lo}-{hi}: {c2/n:.4f} chi2/bin (total {c2:.2f}/{n})  dn {dn:+.4f} +/- {sdn:.4f} ({abs(dn)/sdn:.1f} sigma)')
