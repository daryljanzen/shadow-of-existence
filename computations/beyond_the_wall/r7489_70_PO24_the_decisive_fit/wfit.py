#!/usr/bin/env python3
"""r7489+70 -- n_s over a tail window [LMIN, LMAX]: the r7471 likelihood with l_min raised, all six LCDM
parameters free (omega_b included), plus lensing and the tau prior.  Modes:
   sky     the real Planck data
   null    a noise-free mock = the off-tail best fit (the control: must return M = 0)
   sig     the same mock times S(l) = exp[-(r^2-1)(l/l_D)^2], r = 0.9918, l_D = 1362, on TT, TE and EE
   python3 wfit.py MODE LMIN LMAX PROFILE(0/1)"""
import json, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
OFF = os.path.join(HERE, '..', 'r7471_70_PO24_tilt_off_the_tail')
sys.path.insert(0, OFF)
import like as LK
import scipy.linalg

MODE, LMIN, LMAX, PROF = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), bool(int(sys.argv[4]))
NAME = f'{MODE}_{LMIN}_{LMAX}'
R, LDAMP = 0.9918, 1362.0
NAMES = ['ombh2', 'omch2', 'H0', 'ln10As', 'ns', 'tau', 'cal']
OFFB = json.load(open(os.path.join(OFF, 'fit_primary.json')))['best']
XOFF = np.array([OFFB[n] for n in NAMES])


class WLike(LK.Like):
    def __init__(self):
        super().__init__(lmax=LMAX, spectra='TTTEEE', lensing=True, tau_prior=True)
        blo = LK.blmin[:LK.NTT] + LK.LMIN
        tt = (blo >= LMIN) & (LK.BIN_HI <= LMAX)
        pol = (blo[:LK.NTE] >= LMIN) & (LK.BIN_HI[:LK.NTE] <= LMAX)
        sel = np.zeros(LK.N, bool); sel[:LK.NTT] = tt; sel[LK.NTT:LK.NTT + LK.NTE] = pol; sel[LK.NTT + LK.NTE:] = pol
        self.sel = sel
        self.icov = scipy.linalg.cho_solve(scipy.linalg.cho_factor(LK.COV[np.ix_(sel, sel)]), np.identity(sel.sum()))
        self.nbins = int(sel.sum())
        self.lmax_camb = 2650
        self.tau0, self.cal0 = 0.054, 1.0
        self.X = LK.X.copy(); self.LENS = LK.LENS_DATA.copy()

    def model(self, p, S=None):
        tot, pp, _ = self.spectra(p)
        NL = LK.NL; lm = min(LK.LMAXD, tot.shape[0] - 1)
        l = np.arange(LK.LMIN, LK.LMIN + NL)
        f = np.ones(NL) if not S else np.exp(-(R ** 2 - 1) * (l / LDAMP) ** 2)
        def binned(col):
            c = np.zeros(NL); c[:lm - LK.LMIN + 1] = tot[LK.LMIN:lm + 1, col]
            return LK.BIN @ (c * f)
        m = np.concatenate([binned(0), binned(3)[:LK.NTE], binned(1)[:LK.NEE]]) / p[6] ** 2
        L = np.arange(pp.shape[0]); PPm = pp[:, 0] * (L * (L + 1)) ** 2 / (2 * np.pi)
        bp = np.array([np.sum(w * PPm[Ls]) for Ls, w in LK.LENS_W])
        return m, bp

    def chi2(self, p):
        try:
            m, bp = self.model(p)
        except Exception:
            return 1e30
        d = (self.X - m)[self.sel]
        c2 = float(d @ self.icov @ d)
        r = self.LENS - bp; c2 += float(r @ LK.LENS_COVINV @ r)
        c2 += ((p[5] - self.tau0) / 0.007) ** 2 + ((p[6] - self.cal0) / 0.0025) ** 2
        return c2


L = WLike()
if MODE in ('null', 'sig'):
    m, bp = L.model(XOFF, S=(MODE == 'sig'))
    L.X, L.LENS, L.tau0, L.cal0 = m, bp, XOFF[5], XOFF[6]

S = np.array([0.00015, 0.0012, 0.54, 0.014, 0.0042, 0.0073, 0.0025]) * 3.0   # tail windows are wider
NS = 4
ncall = [0]
def f(x):
    ncall[0] += 1
    return L.chi2(x)

def grad_hess(x, idx, h=0.5):
    n = len(idx); g = np.zeros(n); H = np.zeros((n, n)); f0 = f(x)
    for a, i in enumerate(idx):
        e = np.zeros_like(x); e[i] = h * S[i]
        fp, fm = f(x + e), f(x - e)
        g[a] = (fp - fm) / (2 * h * S[i]); H[a, a] = (fp - 2 * f0 + fm) / (h * S[i]) ** 2
    for a, i in enumerate(idx):
        for b in range(a + 1, n):
            j = idx[b]
            e1 = np.zeros_like(x); e1[i] = h * S[i]; e2 = np.zeros_like(x); e2[j] = h * S[j]
            H[a, b] = H[b, a] = (f(x + e1 + e2) - f(x + e1 - e2) - f(x - e1 + e2) + f(x - e1 - e2)) / (4 * h * h * S[i] * S[j])
    return f0, g, H

def newton(x, idx, iters=8, tol=0.01):
    x = x.copy()
    for k in range(iters):
        c, g, H = grad_hess(x, idx)
        ev = np.linalg.eigvalsh(H)
        if np.all(ev > 0):
            step = -np.linalg.solve(H, g)
        else:
            Hd = H + np.eye(len(idx)) * (abs(ev.min()) + 1e-3 * abs(ev.max()))
            step = -np.linalg.solve(Hd, g)
        lam = 1.0; cn = c
        while lam > 1 / 32:
            xn = x.copy(); xn[idx] += lam * step
            if xn[5] < 0.01: lam /= 2; continue
            cn = f(xn)
            if cn < c: break
            lam /= 2
        if cn >= c:
            break
        x = xn
        print(f'   [{NAME}] newton {k}: chi2 {c:.4f} -> {cn:.4f}  ns {x[NS]:.5f}', flush=True)
        if c - cn < tol:
            break
    c, g, H = grad_hess(x, idx)
    return x, c, H

t0 = time.time()
ALL = list(range(7))
xb, cb, H = newton(XOFF, ALL)
cov = np.linalg.inv(0.5 * H)
sig = np.sqrt(np.abs(np.diag(cov)))
out = dict(name=NAME, mode=MODE, lmin=LMIN, lmax=LMAX, nbins=L.nbins, best=dict(zip(NAMES, xb.tolist())), chi2=cb,
           sigma_fisher=dict(zip(NAMES, sig.tolist())), hess_posdef=bool(np.all(np.linalg.eigvalsh(H) > 0)))
print(f'   [{NAME}] ns {xb[NS]:.5f} +/- {sig[NS]:.5f}  M = {xb[NS] - 0.96095:+.5f}  ombh2 {xb[0]:.5f}  chi2 {cb:.2f} / {L.nbins}', flush=True)
if PROF:
    oth = [i for i in ALL if i != NS]
    Hoo, Hon = H[np.ix_(oth, oth)], H[oth, NS]
    prof = []
    for k in (-2, -1, 1, 2):
        ns = xb[NS] + k * sig[NS]
        x = xb.copy(); x[NS] = ns
        x[oth] = xb[oth] - np.linalg.solve(Hoo, Hon) * (ns - xb[NS])
        x, c, _ = newton(x, oth, iters=4)
        prof.append((float(ns), float(c)))
        print(f'   [{NAME}] profile ns {ns:.5f}: dchi2 {c - cb:+.3f}', flush=True)
    nsv = np.array([p[0] for p in prof] + [xb[NS]]); dv = np.array([p[1] for p in prof] + [cb])
    a, b, _ = np.polyfit(nsv, dv, 2)
    out.update(profile=prof, sigma_profile=float(np.sqrt(1 / a)), ns_profile=float(-b / (2 * a)))
    print(f'   [{NAME}] PROFILE ns {-b/(2*a):.5f} +/- {np.sqrt(1/a):.5f}', flush=True)
out['ncall'] = ncall[0]; out['wall_s'] = time.time() - t0
json.dump(out, open(os.path.join(HERE, f'w_{NAME}.json'), 'w'), indent=1)
