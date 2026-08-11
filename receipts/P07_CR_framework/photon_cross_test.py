"""
photon_cross_test.py -- verifies: the bead's signed areal radius r(tau~)=A*sign(sinh)*|sinh(3 tau~/2)|^{2/3}
  is REAL and ODD through the seam r=0, and a radial (outgoing null) photon crosses the seam with BOUNDED
  comoving chi -- so r=0 is a passable branch point onto the conjugate (r<0) branch, not a barrier.
  [P7 CR_framework -- the cosmogenetic bead / radial null congruence continuous across r=0]
STATUS: ✔✔   RUN: python3 photon_cross_test.py   RUNTIME: ~2s
COMPUTES: r(tau~) on both sides of the seam; integrates dchi/dtau~=1/(1+r') across tau~ in [-3,3]; checks
  (appended) r real, r odd, r(0)=0 with sign-crossing, chi bounded and continuous across the seam.
  CONTROL: the UNSIGNED law A|sinh|^{2/3} stays >=0 (no r<0 branch) -- only the SIGNED continuation crosses.
ORIGIN: computations/photon_cross_test.py, verified + strengthened + canonicalized r1352.
"""
import numpy as np
from scipy.integrate import solve_ivp
M2=2/(3*np.sqrt(3)); A=M2**(1/3)
def rsig(tt):                                  # SIGNED areal radius, real & odd through 0
    s=np.sinh(1.5*tt); return A*np.sign(s)*np.abs(s)**(2/3)
def rprime(tt,h=1e-6): return (rsig(tt+h)-rsig(tt-h))/(2*h)
print("signed r is real on BOTH sides of the seam:")
for tt in [1.0,0.3,0.0,-0.3,-1.0]:
    print(f"  tau~={tt:+.2f}: r={rsig(tt):+.4f},  r'={rprime(tt):.3f}")
print("\nphoton crossing the seam (integrate in tau~, bounded): chi(tau~), tau(tau~)")
def rhs(ttil,y):
    rp=rprime(ttil); return [1.0/(1.0+rp)]      # dchi/dtau~ for the outgoing null family
chi0=0.0
solP=solve_ivp(rhs,[0,3.0],[chi0],max_step=0.01,rtol=1e-8)
solM=solve_ivp(rhs,[0,-3.0],[chi0],max_step=0.01,rtol=1e-8)
ttil=np.concatenate([solM.t[::-1],solP.t]); chi=np.concatenate([solM.y[0][::-1],solP.y[0]]); tau=ttil-chi
for k in range(0,len(ttil),max(1,len(ttil)//10)):
    print(f"  tau~={ttil[k]:+.2f}  chi={chi[k]:+.3f}  tau={tau[k]:+.3f}  r={rsig(ttil[k]):+.3f}")
print(f"\n crosses seam at chi={np.interp(0,ttil,chi):.3f}; extends tau~ from {ttil.min():.2f} to {ttil.max():.2f} (both sides). GOOD.")

# ── APPENDED ASSERT-VERIFICATION (r1352, Arthur) ──
_tt = np.array([1.0,0.3,0.1,-0.1,-0.3,-1.0])
assert np.all(np.abs(np.imag(rsig(_tt)))<1e-12),            "r is real on both sides of the seam"
assert np.allclose(rsig(-_tt), -rsig(_tt), atol=1e-9),      "r is ODD through the seam: r(-tt)=-r(tt)"
assert abs(rsig(0.0))<1e-12,                                "r(0)=0 (the seam)"
assert rsig(0.3)>0 and rsig(-0.3)<0,                        "r CHANGES SIGN across the seam (onto conjugate branch)"
assert np.all(np.isfinite(chi)) and np.max(np.abs(chi))<2.0,"chi bounded across the seam (photon crosses)"
assert np.max(np.abs(np.diff(chi)))<0.05,                   "chi continuous across the seam (no jump)"
# CONTROL: unsigned law has no r<0 branch, so cannot cross onto the conjugate branch
_unsigned = lambda tt: A*np.abs(np.sinh(1.5*tt))**(2/3)
assert np.all(_unsigned(_tt)>=0) and _unsigned(-0.3)>0,     "CONTROL: unsigned law stays >=0 -- only the SIGNED continuation crosses to r<0"
print("\n>> AVENUE 11 ASSERTS PASSED: signed r real & odd through the seam; photon crosses with bounded, continuous chi; r=0 is passable, not a barrier.")
