#!/usr/bin/env python3
"""r7465+70 -- PO-90: is the sky's l=2-alone suppression inside the sector's own cosmic variance?

R = (C2hat/C2_LCDM)/(C3hat/C3_LCDM).  Skies: Chat_l = C_l * chi2_nu/nu, nu = f_sky (2l+1), l independent.
CR depths 0.487 / 0.435 (P15 exact transfer, adjudicated).  Sky R from the paper's own estimator ranges.
One-sided p = P(R <= R_obs).  Verdict rule fixed in PREDICTION.md.  Exit 0 if every check holds.
"""
import numpy as np
from scipy import stats

SEED = 20261020
CR = {2: 0.487, 3: 0.435}
R_OBS = {'central': 0.20 / 0.84, 'most selective': 0.15 / 1.10, 'least selective': 0.25 / 0.58}
fails = []

def draws(depth2, depth3, n, fsky, rng):
    nu2, nu3 = fsky * 5, fsky * 7
    c2 = depth2 * rng.chisquare(nu2, n) / nu2
    c3 = depth3 * rng.chisquare(nu3, n) / nu3
    return c2 / c3

def p_of(R, r):
    return float(np.mean(R <= r))

rng = np.random.default_rng(SEED)
out = {}
for label, (d2, d3) in (('CR', (CR[2], CR[3])), ('LCDM', (1.0, 1.0))):
    for fsky in (1.0, 0.78):
        R4 = draws(d2, d3, 10**4, fsky, rng)
        R6 = draws(d2, d3, 10**6, fsky, rng)
        for name, r in R_OBS.items():
            out[(label, fsky, name)] = (p_of(R4, r), p_of(R6, r))

# V-a: the exact law.  Full sky: (R / (d2/d3)) ~ F(5,7).
print('  V-a  the Monte Carlo against the exact F(5,7) law (full sky, 10^6 draws)')
for label, (d2, d3) in (('CR', (CR[2], CR[3])), ('LCDM', (1.0, 1.0))):
    for name, r in R_OBS.items():
        exact = stats.f.cdf(r / (d2 / d3), 5, 7)
        mc = out[(label, 1.0, name)][1]
        sig = np.sqrt(exact * (1 - exact) / 10**6)
        ok = abs(mc - exact) < 3 * sig
        if not ok: fails.append(f'V-a {label} {name}')
        print(f'       {label:4s} {name:16s} R_obs {r:.3f}   MC {mc:.4f}   exact {exact:.4f}   |diff| {abs(mc-exact)/sig:.1f} sigma  {"OK" if ok else "FAIL"}')

print('\n  p = P(R <= R_obs), one-sided   [10^4 skies as the row asks | 10^6]')
for label in ('CR', 'LCDM'):
    for fsky in (1.0, 0.78):
        row = '   '.join(f'{name}: {out[(label,fsky,name)][0]:.4f} | {out[(label,fsky,name)][1]:.4f}' for name in R_OBS)
        print(f'    {label:4s} f_sky {fsky:.2f}   {row}')

pc = out[('CR', 1.0, 'central')][1]
pall = [out[('CR', 1.0, n)][1] for n in R_OBS]
if pc >= 0.05: verdict = 'TERMINATES AS A RESULT -- within cosmic variance at the central sky'
elif max(pall) < 0.01: verdict = 'STANDS -- outside cosmic variance on every estimator'
else: verdict = 'BORDERLINE -- the row stays open, sized by its p-value'
print(f'\n  CR expectation ratio C2/C3 = {CR[2]/CR[3]:.3f};  p(CR)/p(LCDM) at the central sky = {pc/out[("LCDM",1.0,"central")][1]:.2f}')
print(f'  VERDICT (rule fixed at r7465+70.1): {verdict}')
print(f'  {"all checks hold" if not fails else "FAILED: " + ", ".join(fails)}')
raise SystemExit(1 if fails else 0)
