#!/usr/bin/env python3
"""r7471+70 -- best fit, Fisher sigma (numerical Hessian) and the n_s profile likelihood for one configuration.
   python3 fit.py NAME LMAX SPECTRA LENSING(0/1) PROFILE(0/1)"""
import json, os, sys, time
import numpy as np
import like

NAME, LMAX, SPEC, LENS, PROF = sys.argv[1], int(sys.argv[2]), sys.argv[3], bool(int(sys.argv[4])), bool(int(sys.argv[5]))
L = like.Like(lmax=LMAX, spectra=SPEC, lensing=LENS)
NAMES = ['ombh2', 'omch2', 'H0', 'ln10As', 'ns', 'tau', 'cal']
x0 = np.array([0.02237, 0.1200, 67.36, 3.044, 0.9649, 0.0544, 1.0])
S = np.array([0.00015, 0.0012, 0.54, 0.014, 0.0042, 0.0073, 0.0025])   # step scale, Planck-sized
NS = 4
ncall = [0]
def f(x):
    ncall[0] += 1
    return L.chi2(x)

def grad_hess(x, idx, h=0.5):
    n = len(idx); g = np.zeros(n); H = np.zeros((n, n)); f0 = f(x)
    fp, fm = {}, {}
    for a, i in enumerate(idx):
        e = np.zeros_like(x); e[i] = h * S[i]
        fp[a], fm[a] = f(x + e), f(x - e)
        g[a] = (fp[a] - fm[a]) / (2 * h * S[i]); H[a, a] = (fp[a] - 2 * f0 + fm[a]) / (h * S[i]) ** 2
    for a, i in enumerate(idx):
        for b in range(a + 1, n):
            j = idx[b]
            e1 = np.zeros_like(x); e1[i] = h * S[i]; e2 = np.zeros_like(x); e2[j] = h * S[j]
            v = (f(x + e1 + e2) - f(x + e1 - e2) - f(x - e1 + e2) + f(x - e1 - e2)) / (4 * h * h * S[i] * S[j])
            H[a, b] = H[b, a] = v
    return f0, g, H

def newton(x, idx, iters=4, tol=0.02):
    x = x.copy()
    for k in range(iters):
        c, g, H = grad_hess(x, idx)
        try:
            step = -np.linalg.solve(0.5 * H, 0.5 * g) if np.all(np.linalg.eigvalsh(H) > 0) else -g / np.abs(np.diag(H))
        except np.linalg.LinAlgError:
            step = -g / np.abs(np.diag(H))
        lam = 1.0
        while lam > 1 / 16:
            xn = x.copy(); xn[idx] += lam * step
            cn = f(xn)
            if cn < c: break
            lam /= 2
        if cn >= c:
            return x, c, H
        x = xn
        print(f'   [{NAME}] newton {k}: chi2 {c:.3f} -> {cn:.3f}  ns {x[NS]:.5f}', flush=True)
        if c - cn < tol:
            break
    c, g, H = grad_hess(x, idx)
    return x, c, H

t0 = time.time()
ALL = list(range(7))
xb, cb, H = newton(x0, ALL, iters=6)
cov = np.linalg.inv(0.5 * H)
sig_f = float(np.sqrt(cov[NS, NS]))
out = dict(name=NAME, lmax=LMAX, spectra=SPEC, lensing=LENS, nbins=L.nbins, best=dict(zip(NAMES, xb.tolist())),
           chi2=cb, sigma_fisher=dict(zip(NAMES, np.sqrt(np.diag(cov)).tolist())))
print(f'   [{NAME}] best ns {xb[NS]:.5f}  Fisher sigma {sig_f:.5f}  chi2 {cb:.2f} over {L.nbins} bins (+lens {LENS})', flush=True)
if PROF:
    oth = [i for i in ALL if i != NS]
    Hoo, Hon = H[np.ix_(oth, oth)], H[oth, NS]
    prof = []
    for k in (-2, -1, -0.5, 0.5, 1, 2):
        ns = xb[NS] + k * sig_f
        x = xb.copy(); x[NS] = ns
        x[oth] = xb[oth] - np.linalg.solve(Hoo, Hon) * (ns - xb[NS])   # the Fisher-conditional optimum as start
        x, c, _ = newton(x, oth, iters=3)
        prof.append((float(ns), float(c)))
        print(f'   [{NAME}] profile ns {ns:.5f}: dchi2 {c - cb:+.3f}', flush=True)
    ns_ = np.array([p[0] for p in prof] + [xb[NS]]); d_ = np.array([p[1] for p in prof] + [cb])
    a, b, c0 = np.polyfit(ns_, d_, 2)
    sig_p = float(np.sqrt(1 / a)); ns_p = float(-b / (2 * a))
    # direct Delta chi2 = 1 crossings by interpolation on each side
    out.update(profile=prof, sigma_profile=sig_p, ns_profile=ns_p)
    print(f'   [{NAME}] PROFILE: ns {ns_p:.5f} +/- {sig_p:.5f}   (Fisher {sig_f:.5f}; ratio {sig_p/sig_f:.3f})', flush=True)
out['ncall'] = ncall[0]; out['wall_s'] = time.time() - t0
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'fit_{NAME}.json'), 'w'), indent=1)
