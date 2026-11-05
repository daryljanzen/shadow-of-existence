"""Is 2.19 reachable from this receipt's own Monte Carlo, or does it need a different input?"""
import ast, os, sys
import numpy as np
ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
print("numpy", np.__version__)
import scipy; print("scipy", scipy.__version__)
R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                 'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control.py')
tree = ast.parse(open(R, encoding='utf-8').read())
NS = {'np': np, 'CubicSpline': CubicSpline, 'argrelextrema': argrelextrema}
NS['LC'], NS['FACB'] = CS.bin_center_and_fac()
NS['X_DATA'], NS['COV_TT'] = CS.X_DATA, CS.COV_TT
want = ('spline_of', 'find_free', 'refit_anchored')
body = [n for n in tree.body
        if (isinstance(n, ast.FunctionDef) and n.name in want)
        or (isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') in ('WS', 'LF'))]
exec(compile(ast.Module(body=body, type_ignores=[]), R, 'exec'), NS)
LC, FACB, X_DATA, COV_TT = NS['LC'], NS['FACB'], NS['X_DATA'], NS['COV_TT']
WS, find_free, refit_anchored = NS['WS'], NS['find_free'], NS['refit_anchored']
D_SKY = X_DATA * FACB
sweep = np.array([find_free(D_SKY, W) for W in WS])
sky_pk = sweep.mean(0)
print("sky quartet:", " ".join(f"{v:.1f}" for v in sky_pk), " procedure spread", f"{sweep.std(0)[3]:.2f}")
Lc = np.linalg.cholesky(COV_TT)

def mc(W, seed, nmc):
    r = np.random.default_rng(seed)
    out = []
    for _ in range(nmc):
        Xr = X_DATA + Lc @ r.standard_normal(len(X_DATA))
        p = refit_anchored(np.where(np.isfinite(X_DATA), Xr * FACB, np.nan), sky_pk, W)
        if np.all(np.isfinite(p)):
            out.append(p)
    return np.array(out)

print("SKIP") if False else None
print("\n  sigma_4 at W=55 over seeds, NMC=600:")
vals = []
for sd in (6875, 99, 1, 7, 2024, 31337, 555, 12345):
    v = mc(55., sd, 600)[:, 3].std(); vals.append(v)
    print(f"    seed {sd:7d}  sigma_4 = {v:.4f}   (n={len(mc(55., sd, 60))} of 60 probe)" if sd == 6875 else f"    seed {sd:7d}  sigma_4 = {v:.4f}")
print(f"  => over 8 seeds: min {min(vals):.4f}  max {max(vals):.4f}  mean {np.mean(vals):.4f}  sd {np.std(vals):.4f}")
print(f"  the published 2.19 is {(2.19 - np.mean(vals)) / np.std(vals):.1f} seed-sigmas from that mean")
print("\n  sigma_4 at W=55, seed 6875, over NMC:")
for n in (200, 400, 600, 1000, 2000):
    print(f"    NMC {n:5d}  sigma_4 = {mc(55., 6875, n)[:, 3].std():.4f}")
print("\n  and the four peaks at W=55, seed 6875, NMC=600, against the published 2.44/2.43/1.88/2.19:")
p = mc(55., 6875, 600)
print("    " + "  ".join(f"{p[:, i].std():.4f}" for i in range(4)))
print("\n  sigma_4 at the OTHER windows, seed 6875, NMC=600:")
for W in (40., 80., 110.):
    q = mc(W, 6875, 600)
    print(f"    W={W:5.0f}  kept {len(q)}/600  sigma_4 = {q[:, 3].std():.4f}")
