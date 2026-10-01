"""r7091 (70) -- where the fit is pinned: the effective degrees of freedom of the six-parameter refit, the
coupling between the acoustic shift and the contrast, the reach, and the residual's shape against noise.

Pre-registered at PREDICTION.md beside this file.  The model is the registered receipt's own, rebuilt here
from the banked grid `computations/beyond_the_wall/refit_grid185/` (base and two-sided steps in H0, Omega_m,
omega_b and n_s per arm; A_s in closed form; tau exactly degenerate with A_s, so not a direction).  Nothing
is run through the transfer: every response is a banked spectrum.

Usage:  python3 rigidity.py [--mc N]
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                   # noqa: E402

GRID = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.020)            # the receipt's own steps
NMC = int(sys.argv[sys.argv.index('--mc') + 1]) if '--mc' in sys.argv else 20000
rng = np.random.default_rng(7091)

# ---------------------------------------------------------------- the lensing operator, as the receipt has it
_lr = os.path.join(SPEC, 'cc66_lens_ratio.npz')
if os.path.exists(_lr):
    _z = np.load(_lr)
    LG, RATIO = np.asarray(_z['lg'], float), np.asarray(_z['ratio'], float)
    LENSSRC = 'banked cc66_lens_ratio.npz'
else:
    import camb
    _p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                         mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    _cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
    _le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
    LG = np.arange(len(_le), dtype=float)
    RATIO = np.ones_like(_le)
    RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]
    LENSSRC = 'CAMB at the control\'s parameters (the receipt\'s own fallback)'


def binned(ls, Dl):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO))


def load(tag):
    z = np.load(os.path.join(GRID, f'{tag}.npz'))
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])


def build(arm):
    ls, Dl, lA = load(f'{arm}_base')
    m0 = binned(ls, Dl)
    ok = np.isfinite(m0)
    C = CS.COV_TT[np.ix_(ok, ok)]
    L = np.linalg.cholesky(C)
    g = {}
    lAs = {'base': lA}
    for k in STEP:
        lp, Dp, ap = load(f'{arm}_{k}p')
        lm, Dm, am = load(f'{arm}_{k}m')
        g[k] = (binned(lp, Dp)[ok] - binned(lm, Dm)[ok]) / (2 * STEP[k])
        lAs[k] = (ap - am) / (2 * STEP[k])
    # the templates of m0, built on the unbinned base so the derivative is taken where it is smooth
    dD = np.gradient(Dl, ls)
    shift = binned(ls, -ls * dD)[ok]                           # a stretch in ell: d m / d ln(ell-scale)
    env = np.array([Dl[(ls >= l - 0.5 * lA) & (ls <= l + 0.5 * lA)].mean() for l in ls])
    contrast = binned(ls, Dl - env)[ok]                         # the oscillatory part, scaled
    # ** THE MODEL IS IN ARBITRARY UNITS UNTIL THE CLOSED-FORM AMPLITUDE IS APPLIED ** -- every response is
    # scaled by the base's fitted amplitude, so a whitened response is in the DATA's sigma, not the model's.
    d = CS.X_DATA[ok]
    Fi = np.linalg.inv(C)
    A0 = float((m0[ok] @ Fi @ d) / (m0[ok] @ Fi @ m0[ok]))
    g = {k: A0 * v for k, v in g.items()}
    return dict(ls=ls, m0=A0 * m0[ok], ok=ok, C=C, L=L, d=d, g=g, lA=lAs, A0=A0,
                bins=0.5 * (CS.BIN_LO + CS.BIN_HI)[ok], shift=A0 * shift, contrast=A0 * contrast)


def W(B, v):
    """whiten: L^-1 v, so a response is in the data's own sigma"""
    return scipy.linalg.solve_triangular(B['L'], v, lower=True)


def bestfit(B):
    """the receipt's quadratic-free linearised model is not used for the minimum: Nelder-Mead on the
    linear-in-gradient model with the amplitude closed-form, as the receipt does (its curvature terms are
    a small correction at the step sizes; the linear span is what Q1 measures)"""
    F = np.linalg.inv(B['C'])

    def chi2(x):
        m = B['m0'] + sum(B['g'][k] * v for k, v in zip(STEP, x))
        if np.any(m <= 0):
            return 1e12
        A = float((m @ F @ B['d']) / (m @ F @ m))
        r = B['d'] - A * m
        return float(r @ F @ r)
    r = minimize(chi2, np.zeros(4), method='Nelder-Mead', options=dict(xatol=1e-5, fatol=1e-4, maxiter=8000))
    m = B['m0'] + sum(B['g'][k] * v for k, v in zip(STEP, r.x))
    A = float((m @ F @ B['d']) / (m @ F @ m))
    return r.x, A, A * m, chi2(np.zeros(4)), r.fun


def runs(s):
    sg = np.sign(s)
    ch = int(np.sum(sg[1:] != sg[:-1]))
    edges = np.flatnonzero(np.r_[True, sg[1:] != sg[:-1], True])
    seg = [s[a:b] for a, b in zip(edges[:-1], edges[1:])]
    return ch, max(len(x) for x in seg), float(sum(x.sum() ** 2 for x in seg))


def lowpower(s, frac=0.10):
    p = np.abs(np.fft.rfft(s - s.mean())) ** 2
    k = max(1, int(round(frac * (len(p) - 1))))
    return float(p[1:k + 1].sum() / p[1:].sum())


def stats(rw):
    ch, lr, ex = runs(rw)
    return dict(crossings=ch, longest=lr, excursion=ex, lowfreq=lowpower(rw))


OUT = {}
for arm, name in (('lcdm', 'CONTROL (LCDM)'), ('cr', 'CR, crossing')):
    B = build(arm)
    n = int(B['ok'].sum())
    print('=' * 100)
    print(f'  {name}   {n} bins, lensing: {LENSSRC}')
    print(f'  l_A at base {B["lA"]["base"]:.3f}   d l_A / d param: ' +
          ', '.join(f'{k} {B["lA"][k]:+.3f}' for k in STEP))
    # ------------------------------------------------------------------ Q1 (1) the rank
    cols = ['A'] + list(STEP)
    J = np.column_stack([B['m0'] * 0.02] + [B['g'][k] * STEP[k] for k in STEP])   # one step each; A: 2%
    Jw = np.column_stack([W(B, J[:, i]) for i in range(J.shape[1])])
    U, S, Vt = np.linalg.svd(Jw, full_matrices=False)
    print('\n  Q1 (1)  singular values of the whitened response, one receipt-step per parameter (A: 2 %):')
    print('          ' + '  '.join(f'{s:9.2f}' for s in S) + '      [sqrt(dchi2) for a unit move along each]')
    print(f'          effective rank: {int(np.sum(S ** 2 > 1))} with dchi2 > 1 per step;  '
          f'{int(np.sum(S > 0.01 * S[0]))} above 1% of the largest;  condition {S[0] / S[-1]:.0f}')
    for j in range(len(S) - 1, max(len(S) - 3, 0), -1):
        v = Vt[j]
        print(f'          soft direction {j + 1} (sv {S[j]:.2f}): ' +
              ', '.join(f'{c}{v[i]:+.2f}' for i, c in enumerate(cols)))
    # pairwise cosines of the whitened responses (degeneracy, pair by pair)
    nrm = Jw / np.linalg.norm(Jw, axis=0)
    cs = nrm.T @ nrm
    print('          |cos| between whitened responses:')
    for i in range(len(cols)):
        print('            ' + f'{cols[i]:>3s} ' + ' '.join(f'{abs(cs[i, j]):6.3f}' for j in range(len(cols))))
    # ------------------------------------------------------------------ Q1 (2) shift / contrast coupling
    T = np.column_stack([W(B, B['m0']), W(B, B['shift']), W(B, B['contrast'])])
    coef = {}
    fitq = {}
    for k in STEP:
        y = W(B, B['g'][k] * STEP[k])
        c, *_ = np.linalg.lstsq(T, y, rcond=None)
        coef[k] = c
        fitq[k] = 1 - np.sum((y - T @ c) ** 2) / np.sum(y ** 2)
    M = np.array([[coef[k][1], coef[k][2]] for k in STEP])        # 4 params x (shift, contrast)
    # make the two template coordinates comparable: scale by the templates' whitened norms
    M = M * np.array([np.linalg.norm(T[:, 1]), np.linalg.norm(T[:, 2])])
    s2 = np.linalg.svd(M, compute_uv=False)
    print('\n  Q1 (2)  each parameter\'s response on (amplitude, SHIFT, CONTRAST), whitened; '
          'R^2 = share of the response the three templates carry')
    for k in STEP:
        i = list(STEP).index(k)
        print(f'          {k:3s}  amplitude {coef[k][0]:+.3e}  shift {M[i, 0]:+.3e}  contrast {M[i, 1]:+.3e}'
              f'   (contrast/shift {M[i, 1] / M[i, 0]:+.3f})   R^2 {fitq[k]:.3f}')
    print(f'          the 4x2 (shift, contrast) matrix: singular values {s2[0]:.3f}, {s2[1]:.3f}  '
          f'-> ratio {s2[1] / s2[0]:.3f}  ({"COLLINEAR: shift and contrast move together" if s2[1] / s2[0] < 0.1 else "independent directions exist"})')
    cs_tc = float(T[:, 1] @ T[:, 2] / np.linalg.norm(T[:, 1]) / np.linalg.norm(T[:, 2]))
    print(f'          (the shift and contrast templates themselves: |cos| {abs(cs_tc):.3f})')
    # ------------------------------------------------------------------ Q1 (3) the reach
    x, A, mfit, c0, c1 = bestfit(B)            # the receipt-style fit, reported for reference
    # ** THE REACH, EXACTLY: the generalised-least-squares minimum of the model LINEARISED about the base, so
    #    the residual is by construction orthogonal to all five directions and nothing reachable is left in it **
    dw = W(B, B['d'])
    Q, _ = np.linalg.qr(Jw)
    rw = dw - Q @ (Q.T @ dw)
    r = B['L'] @ rw
    tot = float(rw @ rw)
    xg = np.linalg.lstsq(Jw, dw - W(B, B['m0']), rcond=None)[0]   # the move FROM the base
    print(f'\n  Q1 (3)  receipt-style fit (Nelder-Mead, closed-form A): ' + ', '.join(f'{k} {v:+.4f}' for k, v in zip(STEP, x)) +
          f'   chi2 {c0:.1f} -> {c1:.1f}')
    print(f'          the linearised GLS minimum, in receipt steps: ' + ', '.join(f'{c} {v:+.3f}' for c, v in zip(cols, xg)))
    print(f'          residual chi2 at the linear minimum {tot:.1f} -- by construction UNREACHABLE by any linear move '
          f'of the five -- against n-5 = {n - 5} ({(tot - (n - 5)) / np.sqrt(2 * (n - 5)):+.1f} sigma)')
    # ** DECLARED POST-HOC (not in PREDICTION.md): if the CONTRAST were free, how much of it would be reached? **
    for lab, tmpl in (('contrast, free', B['contrast']),
                      ('contrast x (ell - mid), free', B['contrast'] * (B['bins'] - B['bins'].mean()) / np.ptp(B['bins'])),
                      ('shift x (ell - mid), free', B['shift'] * (B['bins'] - B['bins'].mean()) / np.ptp(B['bins']))):
        tw = W(B, tmpl)
        tw = tw - Q @ (Q.T @ tw)
        drop = float((tw @ rw) ** 2 / (tw @ tw))
        print(f'          + {lab:30s} would remove dchi2 {drop:7.1f}  ({100 * drop / tot:4.1f}% of the residual)')
    # ------------------------------------------------------------------ Q2 the residual's shape against noise
    # ** the residual ITSELF in ell order, each bin in its own sigma ** -- what "crosses the data" describes;
    # the noise is drawn CORRELATED (plik_lite covariance), and the fit's five directions are removed from each
    # draw in whitened space exactly as the fit removes them from the data
    sig = np.sqrt(np.diag(B['C']))
    obs = stats(r / sig)
    P = np.identity(n) - Q @ Q.T
    sims = {k: [] for k in obs}
    for _ in range(NMC):
        e = B['L'] @ (P @ rng.standard_normal(n))    # correlated noise, the fit's five directions removed
        for k, v in stats(e / sig).items():
            sims[k].append(v)
    print(f'\n  Q2      the residual in ell order, per-bin sigma, against {NMC} correlated noise draws with the fit\'s five directions removed:')
    res = {}
    for k, v in obs.items():
        a = np.asarray(sims[k], float)
        lo = float(np.mean(a <= v))
        hi = float(np.mean(a >= v))
        p2 = min(1.0, 2 * min(lo, hi))
        z = (v - a.mean()) / a.std()
        res[k] = (v, a.mean(), a.std(), p2, z)
        print(f'          {k:10s} data {v:10.3f}   noise {a.mean():10.3f} +- {a.std():8.3f}   '
              f'{z:+6.2f} sigma   p(two-sided) {p2:.4f}{"   <1/NMC" if p2 == 0 else ""}')
    OUT[arm] = dict(S=S, ratio=s2[1] / s2[0], reach=(tot, 0.0, n), q2=res, x=x)

print('=' * 100)
print('  SUMMARY')
for arm in OUT:
    o = OUT[arm]
    print(f'  {arm:5s} rank(dchi2>1) {int(np.sum(o["S"] ** 2 > 1))}, shift/contrast sv-ratio {o["ratio"]:.3f}, '
          f'unreachable chi2 {o["reach"][0] - o["reach"][1]:.1f} of n-5={o["reach"][2] - 5}, '
          f'crossings {o["q2"]["crossings"][0]:.0f} vs noise {o["q2"]["crossings"][1]:.1f} (p {o["q2"]["crossings"][3]:.4f})')
