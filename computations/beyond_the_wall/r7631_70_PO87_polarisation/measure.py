#!/usr/bin/env python3
"""r7631+70 -- PO-87's fourth acoustic feature in polarisation.  PO-47's locator (cubic spline through the binned
D_l, parabola over +-W anchored on the unperturbed feature, Monte Carlo of the covariance), on the EE fourth peak
(l ~ 990) and the TE feature nearest it (the TE trough near l ~ 1070), for the two arms (POLSAVE spectra),
Planck plik_lite, ACT DR6 CMB-only, and a full-sky noise-free floor.
    python3 measure.py CR_POL_NPZ LCDM_POL_NPZ ACT_SACC_FITS"""
import os, sys
import numpy as np
from scipy.interpolate import CubicSpline
import sacc
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'r7471_70_PO24_tilt_off_the_tail'))
import like as LK
NMC, WS = 600, (45., 50., 55., 60., 70., 80.)
FEAT = {'TT': (1050., 1200., +1), 'EE': (930., 1060., +1), 'TE': (1010., 1130., -1)}     # search range for the anchor, and the sign (TE: a trough)


class Data:
    def __init__(s, name, l, d, cov):
        s.name, s.l, s.d, s.cov = name, np.asarray(l, float), np.asarray(d, float), cov
        s.Lc = np.linalg.cholesky(cov) if cov is not None else None
        s.LF = np.arange(max(300., s.l.min()), min(1600., s.l.max()), 1.0)
    def spline(s, d):
        m = (s.l >= s.LF[0] - 60) & (s.l <= s.LF[-1] + 60) & np.isfinite(d)
        return CubicSpline(s.l[m], d[m])(s.LF)
    def at(s, d, anchor, W, sg):
        Df = sg * s.spline(d); k = (s.LF >= anchor - W) & (s.LF <= anchor + W)
        c = np.polyfit(s.LF[k], Df[k], 2)
        return float(-c[1] / (2 * c[0])) if c[0] < 0 else np.nan
    def anchor(s, d, lo, hi, sg):
        Df = sg * s.spline(d); k = (s.LF > lo) & (s.LF < hi)
        return float(s.LF[k][np.argmax(Df[k])])


def locate(D, spec, mc=True):
    lo, hi, sg = FEAT[spec]
    a0 = D.anchor(D.d, lo, hi, sg)
    c = D.at(D.d, a0, 55., sg)
    proc = np.array([D.at(D.d, a0, W, sg) for W in WS])
    out = dict(c=c, proc=np.nanstd(proc), anchor=a0)
    if mc and D.Lc is not None:
        rng = np.random.default_rng(7631)
        for W in (55., 80.):
            v = np.array([D.at(D.d + D.Lc @ rng.standard_normal(len(D.d)), a0, W, sg) for _ in range(NMC)])
            out[f'stat{int(W)}'] = np.nanstd(v); out[f'kept{int(W)}'] = int(np.isfinite(v).sum())
        out['tot'] = float(np.hypot(out['stat55'], out['proc']))
        out['tot80'] = float(np.hypot(out['stat80'], out['proc']))
    return out


# ---- the two arms: the coarse POLSAVE grid (LSTEP=8) splined to every multipole, as the TT locator receipt validated
arms = {}
for t, p in (('cr', sys.argv[1]), ('lcdm', sys.argv[2])):
    z = np.load(p); arms[t] = {k: (z['ls'].astype(float), z[k]) for k in ('Dl', 'Dl_EE', 'Dl_TE')}
print("  PART 1 -- the two arms' fourth acoustic feature (locator on the model spectra themselves, no noise)")
mod = {}
for spec, key in (('TT', 'Dl'), ('EE', 'Dl_EE'), ('TE', 'Dl_TE')):
    for t in ('cr', 'lcdm'):
        l, d = arms[t][key]
        mod[(spec, t)] = locate(Data(t, l, d, None), spec, mc=False)['c']
    print(f"    {spec}: CR {mod[(spec, 'cr')]:8.2f}   control {mod[(spec, 'lcdm')]:8.2f}   arm - control "
          f"{mod[(spec, 'cr')] - mod[(spec, 'lcdm')]:+.2f}")
# ---- the skies
NTT, NTE = LK.NTT, LK.NTE
lb = LK.bval
fac = lambda l: l * (l + 1) / (2 * np.pi)
sl = {'TT': slice(0, NTT), 'TE': slice(NTT, NTT + NTE), 'EE': slice(NTT + NTE, NTT + 2 * NTE)}
s = sacc.Sacc.load_fits(sys.argv[3])
skies = {}
for spec in ('TT', 'EE', 'TE'):
    i = sl[spec]; lP = lb[i]; f = fac(lP)
    skies[(spec, 'Planck')] = Data('Planck plik_lite', lP, LK.X[i] * f, LK.COV[i, i] * np.outer(f, f))
    dt = {'TT': 'cl_00', 'EE': 'cl_ee', 'TE': 'cl_0e'}[spec]
    ind = s.indices(dt); tr = s.get_tracer_combinations(dt)[0]
    _, cl = s.get_ell_cl(dt, *tr)
    w = s.get_bandpower_windows(ind); W = w.weight.T; lv = np.asarray(w.values, float)
    skies[(spec, 'ACT')] = Data('ACT DR6 CMB-only', (W * lv[None, :]).sum(1) / W.sum(1), cl,
                               s.covariance.covmat[np.ix_(ind, ind)])
print("\n  PART 2 -- the sky's fourth acoustic feature, and the arms scored against it (2 sigma needed)")
print(f"    {'':>4} {'sky':>8} {'l4':>8} {'stat55':>7} {'stat80':>7} {'proc':>5} {'tot55':>6} {'tot80':>6}  "
      f"{'arm-ctl':>8} {'/tot55':>7} {'/tot80':>7}  {'ctl-sky':>8} {'arm-sky':>8}")
res = {}
for spec in ('TT', 'EE', 'TE'):
    d = mod[(spec, 'cr')] - mod[(spec, 'lcdm')]
    for sky in ('Planck', 'ACT'):
        r = locate(skies[(spec, sky)], spec); res[(spec, sky)] = r
        print(f"    {spec:>4} {sky:>8} {r['c']:8.1f} {r['stat55']:7.2f} {r['stat80']:7.2f} {r['proc']:5.2f} "
              f"{r['tot']:6.2f} {r['tot80']:6.2f}  {d:+8.2f} {d / r['tot']:7.2f} {d / r['tot80']:7.2f}  "
              f"{mod[(spec, 'lcdm')] - r['c']:+8.2f} {mod[(spec, 'cr')] - r['c']:+8.2f}")
    a, b = res[(spec, 'Planck')], res[(spec, 'ACT')]
    tc = (a['tot'] ** -2 + b['tot'] ** -2) ** -0.5
    print(f"    {spec:>4} {'P+A bnd':>8} {'':8} {'':7} {'':7} {'':5} {tc:6.2f} {'':6}  {d:+8.2f} {d / tc:7.2f}")

print("\n  PART 3 -- the full-sky, noise-free floor on the feature's location (the control's spectra, plik_lite's bins)")
lc, Dc = arms['lcdm']['Dl'], arms['lcdm']['Dl_EE'][1]; Tc = arms['lcdm']['Dl_TE'][1]
lF = np.arange(30., 2000., 1.0)
TT = CubicSpline(lc[0], lc[1])(lF); EE = CubicSpline(lc[0], Dc)(lF); TE = CubicSpline(lc[0], Tc)(lF)
for spec in ('TT', 'EE', 'TE'):
    nb = NTT if spec == 'TT' else NTE                         # TE/EE share TT's first 199 bins
    blo, bhi = LK.blmin[:nb] + LK.LMIN, LK.blmax[:nb] + LK.LMIN
    d = mod[(spec, 'cr')] - mod[(spec, 'lcdm')]
    var_l = {'TT': 2 * TT ** 2, 'EE': 2 * EE ** 2, 'TE': TE ** 2 + TT * EE}[spec] / (2 * lF + 1)      # per-multipole, full sky, in D_l^2
    y = {'TT': TT, 'EE': EE, 'TE': TE}[spec]
    lb_, yb, sb = [], [], []
    for lo_, hi_ in zip(blo, bhi):
        m = (lF >= lo_) & (lF <= hi_)
        if m.sum() == 0: continue
        lb_.append(lF[m].mean()); yb.append(y[m].mean()); sb.append(np.sqrt(var_l[m].sum()) / m.sum())
    lb_, yb, sb = map(np.array, (lb_, yb, sb))
    D = Data('cv', lb_, yb, np.diag(sb ** 2))
    lo, hi, sg = FEAT[spec]; a0 = D.anchor(D.d, lo, hi, sg); rng = np.random.default_rng(1)
    for W in (55., 80.):
        v = np.array([D.at(D.d + sb * rng.standard_normal(len(sb)), a0, W, sg) for _ in range(NMC)])
        f0 = np.nanstd(v)
        print(f"    {spec} W={W:.0f}: floor sigma(l4) = {f0:.2f}  -> arm-control {d:+.2f} at best {abs(d) / f0:.2f} sigma; "
              f"half the difference is {abs(d) / 2:.2f}: floor {'ABOVE' if f0 > abs(d) / 2 else 'below'} it")
