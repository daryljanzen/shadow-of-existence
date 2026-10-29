"""r7633+70: refit_grid185/fit.py's response-model refit, unchanged in method, pointed at a chosen grid directory and the
regenerated lens ratio.   python3 refit.py GRID_DIR [arm_tag=cr] [H0 OM WB NS of the grid's base]"""
import os, sys, types
import numpy as np
from scipy.optimize import minimize
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, '..', 'refit_grid185', 'fit.py')).read().split("if __name__ == '__main__':")[0]
src = src.replace("lg, r = np.load('/tmp/n66/lens_ratio.npy')", f"lg, r = np.load({os.path.join(H, 'lens_ratio.npy')!r})")
G = {'__name__': 'fit185'}
exec(src, G)
D = sys.argv[1]; tag = sys.argv[2] if len(sys.argv) > 2 else 'cr'
th0 = dict(zip(('H0', 'OM', 'WB', 'NS'), map(float, sys.argv[3:7]))) if len(sys.argv) >= 7 else \
      dict(H0=68.60, OM=0.2973, WB=0.0224, NS=0.965)
G['D'] = D
B = G['build'](dict(tag=tag, base=f'{D}/{tag}_base.npz', th0=th0))
n = int(B['ok'].sum()); c0 = G['chi2_at'](B, np.zeros(4))
r = minimize(lambda x: G['chi2_at'](B, x), np.zeros(4), method='Nelder-Mead', options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))
th = {k: th0[k] + v for k, v in zip(G['STEP'], r.x)}
print(f"  {tag} on {D} ({n} bins): chi2 at base {c0:.1f}, refitted {r.fun:.1f}")
for i, k in enumerate(G['STEP']):
    print(f"    {k:>3} {th0[k]:10.6f} -> {th[k]:10.6f}  ({r.x[i] / G['STEP'][k]:+.2f} steps)")
print("  BEST " + " ".join(f"{k}={th[k]:.6f}" for k in G['STEP']))
