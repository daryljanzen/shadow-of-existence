"""
P14_dual_norm.py -- verifies the LOAD-BEARING norm caveat behind prop:wall ("never quote the normalizability
  without the norm"): the exact wall zero-mode psi=cosh^{-a}(x/a) chi_+ is normalizable in the spatial-LEAF
  norm (the one CR's ontology selects -- the fermion is a field on the evolving leaf) but is NOT normalizable
  in the conserved spacetime DIRAC norm (tortoise dr_*=dr/f), because that measure diverges at the horizons
  (f=0, a square-root/simple-zero singularity). BOTH limits confirmed, opposite verdicts:
    (leaf, flat dx)      : int cosh^{-2a} dx  converges         => NORMALIZABLE   (a=lambda=j+1/2>0)
    (conjugate cosh^{+a}): int cosh^{+2a} dx  diverges          => REJECTED branch
    (Dirac, dr_*=dr/f)   : int |psi|^2 dr/f near a horizon      => LOG-DIVERGES  => NOT normalizable
  So the selected leaf norm makes exactly one branch bound; the conserved norm makes neither. [P14 prop:wall]
STATUS: ✔✔   RUN: python3 P14_dual_norm.py   RUNTIME: ~2s
COMPUTES: the two wall-norm integrals (bound branch converges, conjugate diverges) in the flat leaf measure;
  and the horizon behaviour of the conserved-norm measure 1/f (simple zero => log divergence) vs the flat
  measure (finite), on the concrete SdS of B-2 (M=0.12, alpha=1). CONTROL: away from any horizon (f bounded
  below) the two measures agree up to a constant -- the split is a horizon effect, not a coordinate artefact.
ORIGIN: built new r1385 (P14 body's load-bearing dual-norm claim; comment L22-27; previously unreceipted).
"""
import numpy as np
from scipy import integrate
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
print("="*72); print("P14 prop:wall -- the wall mode: leaf-normalizable, NOT conserved-Dirac-normalizable"); print("="*72)

# --- (1) leaf norm of the wall mode on m=tanh(x/a): psi = cosh^{-a}(x/a) ---
a=1.5   # a = lambda = j+1/2 > 0
psi2      = lambda x: np.cosh(x/a)**(-2*a)   # |bound branch|^2
psi2_conj = lambda x: np.cosh(x/a)**(+2*a)   # |conjugate branch|^2
Nbound,_ = integrate.quad(psi2, -60, 60)
ok&=check(f"LEAF norm of bound branch cosh^-a: int|psi|^2 dx = {Nbound:.4f} FINITE => normalizable", np.isfinite(Nbound) and Nbound<1e3)
# conjugate branch diverges: integrate on a growing window, show it blows up
w1=integrate.quad(psi2_conj,-10,10)[0]; w2=integrate.quad(psi2_conj,-20,20)[0]
ok&=check(f"conjugate branch cosh^+a: int grows without bound ({w1:.1f} -> {w2:.1f} as window doubles) => REJECTED", w2>10*w1)

# --- (2) horizon behaviour: conserved Dirac measure dr_*=dr/f vs flat dr, on B-2's SdS ---
from scipy.optimize import brentq
M,alph=0.12,1.0
f=lambda r: 1-2*M/r-r**2/alph**2
rb=brentq(f,0.15,0.5); rout=rb+0.30   # inner horizon (root of f); FIXED outer bound, still f>0 (rout<rc)
# shrink the inner cutoff toward the horizon with rout FIXED: watch each measure
eps=np.array([1e-1,1e-2,1e-3,1e-4,1e-5,1e-6])
flat =np.array([integrate.quad(lambda r: 1.0,      rb+e, rout)[0] for e in eps])   # flat leaf measure
dirac=np.array([integrate.quad(lambda r: 1.0/f(r), rb+e, rout)[0] for e in eps])   # conserved Dirac measure 1/f
incrF=np.diff(flat); incrD=np.diff(dirac)
ok&=check(f"FLAT leaf measure CONVERGES to a finite limit as r->horizon (increments ->0: {incrF[-3]:.4f},{incrF[-2]:.4f},{incrF[-1]:.4f})",
          np.isfinite(flat[-1]) and incrF[-1] < 0.01*incrF[0])
ok&=check(f"conserved DIRAC measure DIVERGES (increments do NOT shrink -- stay ~const {incrD[-3]:.2f},{incrD[-2]:.2f},{incrD[-1]:.2f}; total {dirac[0]:.2f}->{dirac[-1]:.2f})",
          incrD[-1] > 0.4 and incrD[-1] > 0.5*incrF[0] and abs(incrD[-1]-incrD[-3])/incrD[-3] < 0.05)
# log structure: increment per decade of eps is ~constant = 1/f'(rb) * ln(10)
incr=np.diff(dirac)
ok&=check(f"the divergence is LOGARITHMIC (near-constant increment/decade: {incr[-3]:.2f},{incr[-2]:.2f},{incr[-1]:.2f})",
          np.std(incr[-4:])/np.mean(incr[-4:]) < 0.06)

# --- (3) CONTROL: away from any horizon the two measures agree up to a bounded factor ---
r0,r1=0.45,0.55   # a window with f bounded away from 0
flatC=integrate.quad(lambda r:1.0, r0,r1)[0]; diracC=integrate.quad(lambda r:1.0/f(r), r0,r1)[0]
ok&=check(f"CONTROL: off-horizon the two measures agree up to a bounded factor ({diracC/flatC:.2f}x) -- split is a HORIZON effect",
          np.isfinite(diracC) and diracC/flatC < 5)
print("="*72)
print("RESULT:", "ALL PASS -- the wall mode is normalizable in the spatial-leaf norm CR selects and NOT in the\n         conserved spacetime Dirac norm (tortoise measure log-diverges at the horizon). Both limits\n         confirmed; the normalizability may not be quoted without naming the leaf norm (prop:wall)." if ok else "SOME FAILED")
print("="*72)

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (0) the six checks above compute a PASS/FAIL boolean and only PRINT it.  Assert it, so a FAIL
#     stops the run instead of changing one word of the RESULT line.
assert ok, "a check in P14_dual_norm FAILED -- see the [FAIL] line above"
# (1) PINS OF OUR OWN, on the two verdicts the caveat rests on.  LEAF norm of the bound branch
#     cosh^{-2a} at a=1.5 is 2.3561945 (= 3 pi / 4), finite; the conjugate branch grows by a
#     factor 4.85e8 when the window merely doubles, so it is not a borderline rejection.
assert abs(Nbound - 2.3561945) < 1e-6, Nbound
assert w2/w1 > 1e8, w2/w1
# (2) the concrete SdS the horizon test runs on: the inner root of f at M=0.12, alpha=1.
assert abs(rb - 0.2569683) < 1e-6, rb
assert abs(f(rb)) < 1e-12 and f(rout) > 0, (f(rb), f(rout))
# (3) THE SPLIT ITSELF, which is the load-bearing claim: as the cutoff is driven to the horizon
#     the FLAT leaf measure converges to 0.3 while the conserved DIRAC measure walks off,
#     0.7924 -> 4.6480, adding a near-constant 0.73786 per decade.  ** And that constant is
#     ln(10)/f'(r_b) -- the signature of a LOGARITHMIC divergence at a simple zero of f, which
#     is what makes this a horizon effect rather than a slow numerical drift. **
assert abs(flat[-1] - 0.299999) < 1e-5, flat[-1]
assert abs(dirac[0] - 0.792267) < 1e-5 and abs(dirac[-1] - 4.647976) < 1e-5, (dirac[0], dirac[-1])
_fprime = (f(rb+1e-6) - f(rb-1e-6))/2e-6
assert abs(incrD[-1] - 0.73787) < 1e-4, incrD[-1]
assert abs(incrD[-1] - np.log(10.0)/_fprime) < 1e-3, (incrD[-1], np.log(10.0)/_fprime)
assert abs(_fprime - 3.120625) < 1e-5, _fprime
# (4) the CONTROL, pinned: off the horizon the two measures differ by 3.7378x, a bounded factor.
assert abs(diracC/flatC - 3.73783) < 1e-4, diracC/flatC
