#!/usr/bin/env python3
"""r7629+70 -- PO-87's fourth peak with ACT DR6.  PO-47's locator, unchanged (cubic spline through the binned TT D_l,
parabola over +-W anchored on the unperturbed peak, Monte Carlo of the bandpower covariance), on Planck plik_lite,
ACT DR6 CMB-only, and the two combined; the CR arm and the control scored against each; the shared fraction; the
cosmic-variance floor on the peak's location.      python3 measure.py ACT_SACC_FITS"""
import os, sys
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
import sacc
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NMC, WREF, WS = 600, (55., 80.), (45., 50., 55., 60., 70., 80.)

def peaks_sub(ls, Dl, n=4, order=3):            # PO-47 / cc66's three-point parabola on the fine model spectra
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        out.append(float(ls[i] + 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2) * (ls[i + 1] - ls[i])))
    return out

class Data:
    def __init__(s, name, l, d, cov, lo):
        s.name, s.l, s.d, s.cov = name, l, d, cov
        s.LF = np.arange(lo, 1300.0, 1.0); s.lo = lo
        s.Lc = np.linalg.cholesky(cov)
    def spline(s, d):
        m = (s.l >= s.lo) & (s.l <= 1400) & np.isfinite(d)
        return CubicSpline(s.l[m], d[m])(s.LF)
    def at(s, d, anchor, W):
        Df = s.spline(d); k = (s.LF >= anchor - W) & (s.LF <= anchor + W)
        c = np.polyfit(s.LF[k], Df[k], 2)
        return float(-c[1] / (2 * c[0])) if c[0] < 0 else np.nan
    def anchor(s, d):
        Df = s.spline(d); k = (s.LF > 1050) & (s.LF < 1200)
        return float(s.LF[k][np.argmax(Df[k])])

def planck():
    LC, FACB = CS.bin_center_and_fac()
    return Data('Planck plik_lite', LC, CS.X_DATA * FACB, CS.COV_TT * np.outer(FACB, FACB), 100.), FACB

def act(path):
    s = sacc.Sacc.load_fits(path)
    ind = s.indices('cl_00'); _, cl = s.get_ell_cl('cl_00', 'dr6_cmb_s0', 'dr6_cmb_s0')
    w = s.get_bandpower_windows(ind); W = w.weight.T; lv = np.asarray(w.values, int)
    leff = (W * lv[None, :]).sum(1) / W.sum(1)
    return Data('ACT DR6 CMB-only', leff, cl, s.covariance.covmat[np.ix_(ind, ind)], 600.), (W, lv)

def locate(D, label):
    a0 = D.anchor(D.d)
    proc = np.array([D.at(D.d, a0, W) for W in WS])
    c = D.at(D.d, a0, WREF[0])
    rng = np.random.default_rng(7629); mc = {}
    for W in WREF:
        v = np.array([D.at(D.d + D.Lc @ rng.standard_normal(len(D.d)), a0, W) for _ in range(NMC)])
        mc[W] = v[np.isfinite(v)]
    st = mc[WREF[0]].std(); tot = float(np.hypot(st, proc.std()))
    print(f"  {label:>20}: l4 = {c:7.1f}  stat {st:.2f} (W=55), {mc[WREF[1]].std():.2f} (W=80)  procedure {proc.std():.2f}  "
          f"combined {tot:.2f}   kept {len(mc[55.])}/{NMC}, bias {mc[55.].mean() - c:+.2f}")
    return dict(c=c, stat=st, stat80=mc[WREF[1]].std(), proc=proc.std(), tot=tot, mc=mc[WREF[0]], anchor=a0)

P, FACB = planck()
A, (WA, LVA) = act(sys.argv[1])
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
print("  PART 1 -- the sky's fourth peak by PO-47's locator\n")
sk = {'P': locate(P, P.name), 'A': locate(A, A.name)}
wP, wA = 1 / sk['P']['tot'] ** 2, 1 / sk['A']['tot'] ** 2
comb = dict(c=(wP * sk['P']['c'] + wA * sk['A']['c']) / (wP + wA), tot=(wP + wA) ** -0.5)
print(f"  {'combined (indep.)':>20}: l4 = {comb['c']:7.1f}  combined {comb['tot']:.2f}   (a bound: the skies overlap)")
print(f"  ACT / Planck precision at the fourth peak: {sk['P']['tot'] / sk['A']['tot']:.2f}")

print("\n  PART 2 -- the models' fourth peaks: fine grid (as PO-47), and through each sky's own binning and locator")
mod = {}
for t in ('cr', 'lcdm'):
    ls, Dl = F[t]['ls'].astype(float), F[t]['Dl']
    fine = peaks_sub(ls, Dl)[3]
    bP = CS.bin_spectrum(ls, Dl) * FACB
    inside = (LVA >= ls[0]) & (LVA <= ls[-1])
    bA = WA[:, inside] @ np.interp(LVA[inside], ls, Dl)
    bA[np.abs(WA[:, ~inside]).sum(1) > 0] = np.nan          # a window reaching past the model's range is not scored
    mod[t] = dict(fine=fine, P=P.at(bP, sk['P']['anchor'], 55.), A=A.at(bA, sk['A']['anchor'], 55.))
    print(f"  {t:>5}: fine {fine:7.2f}   Planck-binned {mod[t]['P']:7.2f}   ACT-binned {mod[t]['A']:7.2f}")
dfine = mod['cr']['fine'] - mod['lcdm']['fine']

print("\n  PART 3 -- arm against control, in each sky's spread (2 sigma needed)")
print(f"  {'sky':>22} {'sigma':>6} {'arm-ctl':>8} {'in sigma':>9} {'ctl-sky':>8} {'arm-sky':>8}  shared f (median, 16-84%)")
rows = (('Planck', sk['P'], 'P'), ('ACT alone (P-ACT)', sk['A'], 'A'), ('Planck+ACT (bound)', comb, None))
for lab, s, key in rows:
    for how in ('fine', 'binned'):
        if how == 'binned' and key is None: continue
        a = mod['cr']['fine' if how == 'fine' else key]; c = mod['lcdm']['fine' if how == 'fine' else key]
        d = a - c; cs = c - s['c']; as_ = a - s['c']
        if 'mc' in s:
            sr = s['mc'] - s['mc'].mean() + s['c']; f = (c - sr) / (a - sr); q = np.percentile(f, [16, 50, 84])
            fs = f"{q[1]:.2f} ({q[0]:.2f} to {q[2]:.2f})"
        else:
            fs = '-'
        print(f"  {lab + ' / ' + how:>22} {s['tot']:>6.2f} {d:>+8.2f} {d / s['tot']:>9.2f} {cs:>+8.2f} {as_:>+8.2f}  {fs}")

print("\n  PART 4 -- the cosmic-variance floor: full sky, no noise, the control binned as plik_lite bins it")
lsC, DlC = F['lcdm']['ls'].astype(float), F['lcdm']['Dl']
bC = CS.bin_spectrum(lsC, DlC) * FACB
m = np.isfinite(bC)
nl = (CS.BIN_HI - CS.BIN_LO + 1.0); lc = 0.5 * (CS.BIN_HI + CS.BIN_LO)
for fsky, lab in ((1.0, 'full sky'), (0.55, "Planck's effective sky (0.55)")):
    sd = np.where(m, np.sqrt(2.0 / ((2 * lc + 1) * nl * fsky)) * np.abs(bC), 1.0)
    D = Data('cv', P.l, np.where(m, bC, 0.0), np.diag(sd ** 2), 100.)
    a0 = D.anchor(D.d); rng = np.random.default_rng(1)
    for W in WREF:
        v = np.array([D.at(D.d + sd * rng.standard_normal(len(sd)), a0, W) for _ in range(NMC)])
        v = v[np.isfinite(v)]
        print(f"  {lab:>30}, W={W:.0f}: sigma(l4) = {v.std():.2f} (stat only)   -> arm-control +{dfine:.2f} would sit at "
              f"{dfine / v.std():.2f} sigma")
print(f"  separating +{dfine:.2f} at 2 sigma needs sigma(l4) <= {dfine / 2:.2f}")
