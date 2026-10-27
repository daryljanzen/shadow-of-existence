#!/usr/bin/env python3
"""Chat-seat order (48889c6): TT precision on l 1000-2508, ACT DR6 (CMB-only) and SPT-3G D1 (SPT-lite) against
Planck 2018 plik_lite, alone and combined, measured against the 1.44x bar r7611+70.2 left.
   python3 measure.py ACT_SACC_FITS SPT_LITE_DIR
Precision is compared per multipole: the fractional bandpower error times sqrt(N_eff), N_eff = (sum w)^2 / sum w^2
of the bin's window (for plik_lite, the bin's width).  Three band figures:
   amp   sqrt(F_X/F_P), F = sum (D/sigma)^2 over bins centred in the window (diagonal)
   ampC  the same with each dataset's full covariance (1^T C_frac^-1 1)
   tilt  sigma(n_s)_P / sigma(n_s)_X from an amplitude-plus-tilt Fisher, full covariance, pivot 1500
Combinations: 'indep' adds the Fishers (an upper bound: the skies overlap); 'overlap' splits each per-l variance into
sample variance on the dataset's effective sky (fitted from its own lowest bins, where noise is smallest) and an excess
treated as noise, and combines only the noise over the shared sky."""
import os, sys
import numpy as np
import sacc
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS

LO, HI, BAR, PIV = 1000, 2508, 1.44, 1500.0


def planck():
    lc = 0.5 * (CS.BIN_LO + CS.BIN_HI); neff = CS.BIN_HI - CS.BIN_LO + 1.0
    return dict(name='Planck plik_lite', l=lc, d=CS.X_DATA.copy(), cov=CS.COV_TT.copy(), neff=neff)


def act(path):
    s = sacc.Sacc.load_fits(path)
    ind = s.indices('cl_00')
    ell, cl = s.get_ell_cl('cl_00', 'dr6_cmb_s0', 'dr6_cmb_s0')
    cov = s.covariance.covmat[np.ix_(ind, ind)]
    w = s.get_bandpower_windows(ind)
    W = w.weight.T                                  # (nbin, nl)
    neff = W.sum(1) ** 2 / (W ** 2).sum(1)
    leff = (W * w.values[None, :]).sum(1) / W.sum(1)
    return dict(name='ACT DR6 CMB-only', l=leff, d=cl, cov=cov, neff=neff)


def spt(d):
    bdp = np.loadtxt(os.path.join(d, 'SPT3G_D1_TnE_lite_bdp.txt'))
    cov = np.loadtxt(os.path.join(d, 'SPT3G_D1_TnE_lite_cov.txt'))
    win = np.loadtxt(os.path.join(d, 'windows', 'TT_lxl_window_functions.txt'))
    ls, W = win[:, 0], win[:, 1:].T                 # (nbin, nl)
    n = W.shape[0]
    neff = W.sum(1) ** 2 / (W ** 2).sum(1)
    leff = (W * ls[None, :]).sum(1) / W.sum(1)
    return dict(name='SPT-3G D1 SPT-lite', l=leff, d=bdp[:n], cov=cov[:n, :n], neff=neff)


def frac(X):
    s = np.sqrt(np.diag(X['cov']))
    return s / np.abs(X['d'])


def pp(X):                                          # per-multipole fractional error
    return frac(X) * np.sqrt(X['neff'])


def window(X):
    return (X['l'] >= LO) & (X['l'] <= HI)


def fishers(X, m=None):
    m = window(X) if m is None else m
    D = X['d'][m]; C = X['cov'][np.ix_(m, m)] / np.outer(D, D)
    Ci = np.linalg.inv(C)
    one = np.ones(m.sum()); t = np.log(X['l'][m] / PIV)
    Fd = float(np.sum(1 / np.diag(C)))
    Fc = float(one @ Ci @ one)
    J = np.vstack([one, t]).T; F2 = J.T @ Ci @ J
    return Fd, Fc, float(np.sqrt(np.linalg.inv(F2)[1, 1]))


def fsky(X, n=4):
    """effective sky from the dataset's own lowest-l bins: frac^2 = 2/((2l+1) N_eff f) with noise neglected."""
    i = np.argsort(X['l'])[:n]
    return float(np.median(2.0 / ((2 * X['l'][i] + 1) * X['neff'][i] * frac(X)[i] ** 2)))


def nsr(X, f, l):
    """noise-to-signal power at l: per-l fractional sd = sqrt(2/((2l+1) f)) (1 + n)."""
    p = np.interp(l, X['l'], pp(X))
    return np.clip(p / np.sqrt(2.0 / ((2 * l + 1) * f)) - 1.0, 0.0, None)


P, A, S = planck(), act(sys.argv[1]), spt(sys.argv[2])
print(f"  window l = {LO}-{HI}; bar {BAR}x Planck (r7611+70.2)\n")
for X in (P, A, S):
    m = window(X)
    print(f"  {X['name']:>20}: {len(X['l'])} TT bins, {m.sum()} centred in the window, l_eff {X['l'][m][0]:.0f}-{X['l'][m][-1]:.0f}, "
          f"effective sky (lowest bins) {fsky(X):.3f}")

print("\n  PER-BIN: Planck bins in the window, R = (frac err x sqrt N_eff)_Planck / (same)_X, X interpolated in l")
mP = window(P)
lP, pP = P['l'][mP], pp(P)[mP]
RA = pP / np.interp(lP, A['l'], pp(A)); RS = pP / np.interp(lP, S['l'], pp(S))
print(f"  {'l':>7} {'Planck':>8} {'R ACT':>7} {'R SPT':>7}")
for i in range(0, len(lP), 3):
    print(f"  {lP[i]:>7.0f} {pP[i]:>8.4f} {RA[i]:>7.3f} {RS[i]:>7.3f}")
cross = lP[np.argmax(RA > 1)] if (RA > 1).any() else None
print(f"  ACT overtakes Planck (R > 1) from l = {cross}" if cross else "  ACT does not overtake Planck in the window")
crossS = lP[np.argmax(RS > 1)] if (RS > 1).any() else None
print(f"  SPT overtakes Planck (R > 1) from l = {crossS}" if crossS else "  SPT does not overtake Planck in the window")

print("\n  BAND-AVERAGED (alone)")
FP = fishers(P)
res = {}
print(f"  {'':>20} {'amp':>7} {'ampC':>7} {'tilt':>7}   sigma_ns(TT, A+tilt)")
for X in (P, A, S):
    F = fishers(X)
    res[X['name']] = (np.sqrt(F[0] / FP[0]), np.sqrt(F[1] / FP[1]), FP[2] / F[2])
    print(f"  {X['name']:>20} {res[X['name']][0]:>7.3f} {res[X['name']][1]:>7.3f} {res[X['name']][2]:>7.3f}   {F[2]:.4f}")

print("\n  COMBINED WITH PLANCK, per-l Fisher integrated over l = 1000-2508 (diagonal, per-multipole model)")
lg = np.arange(LO, HI + 1, dtype=float)
fP = fsky(P)
vP = np.interp(lg, P['l'], pp(P)) ** 2
J = np.vstack([np.ones_like(lg), np.log(lg / PIV)]).T


def sig_tilt(v):
    F = (J / v[:, None]).T @ J
    return float(np.sqrt(np.linalg.inv(F)[1, 1]))


base_amp, base_tilt = float(np.sum(1 / vP)), sig_tilt(vP)
print(f"  {'':>16} {'f_X':>6} {'amp indep':>10} {'amp overlap':>12} {'tilt indep':>11} {'tilt overlap':>13}  clears {BAR}?")
for X in (A, S):
    fX = min(fsky(X), fP)
    vX = np.interp(lg, X['l'], pp(X)) ** 2
    ind = 1 / vP + 1 / vX
    nP, nX = nsr(P, fP, lg), nsr(X, fX, lg)
    nC = np.where((nP > 0) & (nX > 0), 1 / (1 / np.maximum(nP, 1e-12) + 1 / np.maximum(nX, 1e-12)), 0.0)
    cv = 2.0 / (2 * lg + 1)
    ov = 1 / (cv / fX * (1 + nC) ** 2) + 1 / (cv / (fP - fX) * (1 + nP) ** 2)
    a_i, a_o = np.sqrt(ind.sum() / base_amp), np.sqrt(ov.sum() / base_amp)
    t_i, t_o = base_tilt / sig_tilt(1 / ind), base_tilt / sig_tilt(1 / ov)
    print(f"  {'Planck + ' + X['name'].split()[0]:>16} {fX:>6.3f} {a_i:>10.3f} {a_o:>12.3f} {t_i:>11.3f} {t_o:>13.3f}  "
          f"{'YES' if max(a_o, t_o) >= BAR else 'no'}")
print(f"\n  Planck's own effective sky from its lowest bins: {fP:.3f}")
