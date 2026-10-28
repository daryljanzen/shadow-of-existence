"""How the Planck+ACT overlap-corrected ratio depends on ACT's effective sky (measure.py fits 0.061 from ACT's lowest
bins, where atmospheric noise is not negligible, so it is a floor).  A lower bound on f_ACT that needs no noise model:
f >= 2/((2l+1) pp^2) at every bin, since noise only adds.  python3 fsky_scan.py ACT_SACC SPT_LITE_DIR"""
import sys, numpy as np
sys.argv = sys.argv[:3]
src = open('measure.py').read().split("P, A, S = planck()")[0]
exec(src)
P, A = planck(), act(sys.argv[1])
lb = 2.0 / ((2 * A['l'] + 1) * pp(A) ** 2)
print(f"  f_ACT lower bound from each bin (noise >= 0): max over bins = {lb.max():.3f} at l = {A['l'][np.argmax(lb)]:.0f}")
lg = np.arange(LO, HI + 1, dtype=float); fP = fsky(P)
vP = np.interp(lg, P['l'], pp(P)) ** 2; vA = np.interp(lg, A['l'], pp(A)) ** 2
J = np.vstack([np.ones_like(lg), np.log(lg / PIV)]).T
def st(v): return float(np.sqrt(np.linalg.inv((J / v[:, None]).T @ J)[1, 1]))
bt, ba = st(vP), np.sum(1 / vP)
print(f"  independent (upper bound): tilt {bt / st(1 / (1 / vP + 1 / vA)):.3f}")
print(f"  {'f_ACT':>6} {'amp overlap':>12} {'tilt overlap':>13}")
for fA in (max(lb.max(), 0.061), 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50):
    if fA >= fP: continue
    nP = nsr(P, fP, lg); nA = nsr(A, fA, lg)
    nC = np.where((nP > 0) & (nA > 0), 1 / (1 / np.maximum(nP, 1e-12) + 1 / np.maximum(nA, 1e-12)), 0.0)
    cv = 2.0 / (2 * lg + 1)
    ov = 1 / (cv / fA * (1 + nC) ** 2) + 1 / (cv / (fP - fA) * (1 + nP) ** 2)
    print(f"  {fA:>6.3f} {np.sqrt(ov.sum() / ba):>12.3f} {bt / st(1 / ov):>13.3f}")
