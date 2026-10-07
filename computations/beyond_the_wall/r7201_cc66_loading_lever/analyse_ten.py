#!/usr/bin/env python3
"""r7201 analysis -- the loading lever and the driving lever on the same statistic.

Statistic is cc66.156's verbatim: de-tilt by one global power law fitted in log-log over
150<=l<=1600, maxima on a 0.5-step interpolant, each refined by a parabola on the ORIGINAL
samples (halfwin=40), then phi = <l_n/l_A - n> and alt = <r_n (-1)^n>.  Nothing new.

The loading lever is the RBFAC curve {0.1, 0.5, 1.0, 1.5, 2.0}, where 1.0 is the banked grid
base -- the grids' own configuration is the RBFAC=1 point, so it need not be re-run.
The driving lever is base MINUS nodrive at that same configuration, which is the pair
cc66.156 said had to be built because the banked driving-ON spectrum is a different vintage.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
GO = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7093_directions', 'grid_oneclock')

LMIN, LMAX, NPK = 150.0, 1600.0, 5


def peak_series(path, halfwin=40.0, detilt=True):
    z = np.load(path, allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt if detilt else Dl.copy()
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    Di = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(Di) - 2)
           if Di[i] > Di[i - 1] and Di[i] >= Di[i + 1] and Di[i] > Di[i - 2] and Di[i] >= Di[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls >= l0 - halfwin) & (ls <= l0 + halfwin)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), lA, tilt


def phi_alt(path, halfwin=40.0, detilt=True):
    pk, lA, _t = peak_series(path, halfwin, detilt)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum()), pk, lA


def gaps(pk, lA):
    """the spacing of the detected series in units of l_A -- a comb has these near 1."""
    q = pk[np.isfinite(pk)] / lA
    return np.diff(q)


LEV = ('0.1', '0.5', '1.5', '2.0')
WANT = ([f'{a}_rb{v}' for v in LEV for a in ('cr', 'lcdm')]
        + ['cr_nodrive', 'lcdm_nodrive'])
have = [t for t in WANT if os.path.exists(os.path.join(HERE, f'{t}.npz'))]
print(f"  banked {len(have)} of {len(WANT)}: {' '.join(have)}")
missing = [t for t in WANT if t not in have]
if missing:
    print(f"  MISSING: {' '.join(missing)}")

print("\n  ==== the detected series, spacing in units of l_A (a comb is near 1) ====")
print(f"      {'tag':16s} {'l_A':>10s} {'npk':>4s}  {'gaps':s}")
SER = {}
for tag in have + ['cr_base', 'lcdm_base']:
    p = os.path.join(HERE, f'{tag}.npz') if tag in have else os.path.join(GO, f'{tag}.npz')
    if not os.path.exists(p):
        continue
    ph, al, npk, pk, lA = phi_alt(p)
    SER[tag] = (ph, al, npk, pk, lA)
    g = gaps(pk, lA)
    print(f"      {tag:16s} {lA:10.3f} {npk:4d}  " + " ".join(f"{x:.3f}" for x in g))

print("\n  ==== the loading lever: the RBFAC curve, each arm ====")
print(f"      {'arm':5s} {'RBFAC':>6s} {'l_A':>10s} {'phi':>10s} {'alt':>10s}")
CURVE = {}
for arm in ('cr', 'lcdm'):
    rows = []
    for v in ('0.1', '0.5', '1.0', '1.5', '2.0'):
        tag = f'{arm}_base' if v == '1.0' else f'{arm}_rb{v}'
        if tag not in SER:
            continue
        ph, al, npk, pk, lA = SER[tag]
        rows.append((float(v), lA, ph, al, npk))
        print(f"      {arm:5s} {v:>6s} {lA:10.3f} {ph:+10.5f} {al:+10.5f}")
    CURVE[arm] = rows

print("\n  ==== the driving lever: base MINUS nodrive, same configuration ====")
print(f"      {'arm':5s} {'d_phi':>10s} {'d_alt':>10s}   (control's banked pair: +0.126 / -0.0247)")
DRV = {}
for arm in ('cr', 'lcdm'):
    if f'{arm}_base' in SER and f'{arm}_nodrive' in SER:
        dp = SER[f'{arm}_base'][0] - SER[f'{arm}_nodrive'][0]
        da = SER[f'{arm}_base'][1] - SER[f'{arm}_nodrive'][1]
        DRV[arm] = (dp, da)
        print(f"      {arm:5s} {dp:+10.5f} {da:+10.5f}")

print("\n  ==== logarithmic response of the loading, by central difference about RBFAC=1 ====")
print(f"      {'arm':5s} {'dphi/dlnRB':>12s} {'dalt/dlnRB':>12s}  (over 0.5->1.5; the curve above "
      f"says whether that is linear)")
LOAD = {}
for arm in ('cr', 'lcdm'):
    d = {f'{r[0]:g}': r for r in CURVE[arm]}
    if '0.5' in d and '1.5' in d:
        g = 1.0 / np.log(1.5 / 0.5)
        LOAD[arm] = ((d['1.5'][2] - d['0.5'][2]) * g, (d['1.5'][3] - d['0.5'][3]) * g)
        print(f"      {arm:5s} {LOAD[arm][0]:+12.5f} {LOAD[arm][1]:+12.5f}")

print("\n  ==== do the signs separate the two carriers on the CR arm? ====")
if 'cr' in DRV and 'cr' in LOAD:
    dp, da = DRV['cr']
    lp, la = LOAD['cr']
    print(f"      driving   d_phi {dp:+.5f}   d_alt {da:+.5f}")
    print(f"      loading   d_phi {lp:+.5f}   d_alt {la:+.5f}")
    sep = (np.sign(dp) != np.sign(lp)) or (np.sign(da) != np.sign(la))
    both = (np.sign(dp) != np.sign(lp)) and (np.sign(da) != np.sign(la))
    print(f"      => opposite on at least one component: {sep};  on BOTH: {both}")
    print(f"      control arm for comparison: driving {DRV.get('lcdm')}  loading {LOAD.get('lcdm')}")
else:
    print("      not yet computable -- the pair or the curve is incomplete")
sys.exit(0)
