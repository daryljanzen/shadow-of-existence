import ast, os, sys
import numpy as np
ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
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
sky_pk = np.array([find_free(D_SKY, W) for W in WS]).mean(0)
Lc = np.linalg.cholesky(COV_TT)

def draws(W, seed, nmc):
    r = np.random.default_rng(seed)
    out = []
    for _ in range(nmc):
        Xr = X_DATA + Lc @ r.standard_normal(len(X_DATA))
        p = refit_anchored(np.where(np.isfinite(X_DATA), Xr * FACB, np.nan), sky_pk, W)
        if np.all(np.isfinite(p)):
            out.append(p)
    return np.array(out)

print("  CONVERGENCE of sigma_4 at W=55, three seeds, by draw count")
print(f"    {'NMC':>7s} " + " ".join(f"{'seed ' + str(s):>12s}" for s in (6875, 99, 2024)) + f" {'spread':>8s}")
for n in (600, 1500, 4000, 10000):
    vs = [draws(55., s, n)[:, 3].std() for s in (6875, 99, 2024)]
    print(f"    {n:7d} " + " ".join(f"{v:12.4f}" for v in vs) + f" {max(vs)-min(vs):8.4f}")
print()
print("  and the four peaks at NMC=10000, seed 6875, against the published 2.44/2.43/1.88/2.19:")
p = draws(55., 6875, 10000)
print("    " + "  ".join(f"{p[:, i].std():.4f}" for i in range(4)))
print(f"    combined with the 0.87 procedure spread: {float(np.hypot(p[:, 3].std(), 0.87)):.4f}")
