#!/usr/bin/env python3
"""
P15_the_selective_quadrupole_suppression_is_the_skys_own_and_lcdm_carries_it_at_the_same_size.py

** THE OBSERVED SKY SUPPRESSES l=2 AND NOT l=3.  THE CONSTRUCTION'S SINGLE FLOOR STARVES BOTH
TOGETHER.  IS THAT A DISCREPANCY?  MEASURED: NO. **

Statistic R = (C2hat/C2_LCDM)/(C3hat/C3_LCDM) on Gaussian isotropic skies, Chat_l = C_l chi2_nu/nu,
nu = f_sky(2l+1), l=2 and l=3 independent.  CR depths are P15's adjudicated exact-transfer values,
read from the paper's own sentence.  The observed R is read from the paper's own estimator bracket (central 0.20/0.84;
most selective 0.15/1.10; least selective 0.25/0.58).  On a full sky R/(d2/d3) ~ F(5,7) exactly, so
the Monte Carlo is checked against the closed law.

Result (PO-90, measured by 70 at r7465, computations/beyond_the_wall/r7465_70_PO90_cosmic_variance/,
prediction registered 305237dfd before any draw; struck r7469):
  p_CR   = 0.054 central  (0.017 .. 0.155 across the bracket;  0.082 at f_sky = 0.78, exact)
  p_LCDM = 0.067 central,   so p_CR / p_LCDM = 0.81
  the floor's C2/C3 = 1.12, which is the whole of the fifth it costs.
So the selective suppression is the sky's own low quadrupole, carried by LCDM at the same size; it is
not a shape this construction fails to produce.

This receipt also checks that P15 states the result.
"""
import pathlib, re, sys
import numpy as np
from scipy import stats

ROOT = pathlib.Path(__file__).resolve().parents[2]
TEX = (ROOT / 'corpus' / 'CR_cosmology.tex').read_text()
# The depths are READ from P15's own exact-transfer sentence, not typed here, so this receipt
# carries no copy of them that could drift from the paper.
_m = re.search(r'sits at \$\\approx([0-9.]+)\$, \$([0-9.]+)\$, \$([0-9.]+)\$ and \$([0-9.]+)\$ of the flat-\$\\Lambda\$CDM expectation', TEX)
if not _m:
    print('  FAIL could not read the adjudicated depths from P15'); sys.exit(1)
CR = {2: float(_m.group(1)), 3: float(_m.group(2))}
R_OBS = {'central': 0.20 / 0.84, 'most selective': 0.15 / 1.10, 'least selective': 0.25 / 0.58}
fails = []

def check(ok, msg):
    print(f"  {'OK  ' if ok else 'FAIL'} {msg}")
    if not ok:
        fails.append(msg)

def p_exact(d2, d3, r, fsky=1.0):
    # chi2_nu/nu ratios are F-distributed for any real nu, so the cut sky has a closed law too
    return float(stats.f.cdf(r / (d2 / d3), fsky * 5, fsky * 7))

def p_mc(d2, d3, r, fsky, n, rng):
    nu2, nu3 = fsky * 5, fsky * 7
    R = (d2 * rng.chisquare(nu2, n) / nu2) / (d3 * rng.chisquare(nu3, n) / nu3)
    return float(np.mean(R <= r))

rng = np.random.default_rng(20261020)
pc = p_exact(CR[2], CR[3], R_OBS['central'])
pl = p_exact(1.0, 1.0, R_OBS['central'])
lo = p_exact(CR[2], CR[3], R_OBS['most selective'])
hi = p_exact(CR[2], CR[3], R_OBS['least selective'])
cut = p_exact(CR[2], CR[3], R_OBS['central'], 0.78)
cut_mc = p_mc(CR[2], CR[3], R_OBS['central'], 0.78, 10**6, rng)
mc = p_mc(CR[2], CR[3], R_OBS['central'], 1.0, 10**6, rng)

print(f"  p_CR central {pc:.4f}  bracket {lo:.4f}..{hi:.4f}  cut sky {cut:.4f}  p_LCDM {pl:.4f}  ratio {pc/pl:.3f}")
check(abs(mc - pc) < 3 * np.sqrt(pc * (1 - pc) / 10**6), "Monte Carlo agrees with the exact F(5,7) law")
check(abs(pc - 0.054) <= 0.0005, "p_CR central is 0.054")
check(abs(lo - 0.017) <= 0.0005 and abs(hi - 0.155) <= 0.0005, "bracket 0.017 .. 0.155")
check(abs(cut - 0.082) <= 0.0005, "cut-sky p (f_sky = 0.78) is 0.082")
check(abs(cut_mc - cut) < 3 * np.sqrt(cut * (1 - cut) / 10**6), "cut-sky Monte Carlo agrees with its exact law")
check(abs(pl - 0.067) <= 0.0005, "p_LCDM central is 0.067")
check(0.80 <= pc / pl <= 0.81, "p_CR / p_LCDM = 0.81 (exact 0.805, Monte Carlo 0.807): a fifth less probable")
check(round(CR[2] / CR[3], 2) == 1.12, "floor C2/C3 = 1.12, from the depths P15 prints")
check(pc >= 0.05, "the row's termination threshold (p >= 0.05 at the central sky) is met")

flat = re.sub(r'\s+', ' ', TEX)
for s in ('$p=0.054$', '$p=0.067$', '$1.12$', 'the sky\'s own'):
    check(s in flat, f"P15 states {s}")
check('remains unaccounted for' not in flat, "P15 no longer calls the selective suppression unaccounted for")

print(f"\n  {'all checks hold' if not fails else 'FAILED: ' + '; '.join(fails)}")
sys.exit(1 if fails else 0)
