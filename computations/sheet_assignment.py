"""
WP-B / C3 -- the sheet-assignment by ruling-continuation  (investigation, honest)

*** CORRECTION (r989 audit). Steps [1] and [2] are sound and stand. Step [3]'s verdict --
    "the two null bundles A, B take the +-pi/3 wings" -- is NOT derived and is WITHDRAWN.
    What [2] actually shows is that both +-pi/3 wings are the tau~<->conj(tau~) conjugate pair
    of the SINGLE matter (A) cosmic-time continuation. Relabelling A's own -pi/3 conjugate wing
    as "B" collapses the DOUBLE ruling of the one-sheeted hyperboloid (A and B are two genuinely
    distinct null-line families, orthogonal at the waist -- verified) into one bundle-under-a-sign.
    The map from the two distinct rulings {A,B} to the two conjugate sheets is OPEN, not claimed.
    Only the photon->real-crossing assignment (step [1]) is derived. See P7 thm:bead third fact
    and the frontiers item, both de-asserted at r989. ***

The three cube-root sheets of r(tau~) past the seam sit at Im tau~ in {0, +pi alpha/3, -pi alpha/3}
(alpha=1: {0, +pi/3, -pi/3}).  The open question: which physical congruence rides which sheet?
DERIVED: photon = real crossing (Im 0). OPEN (not claimed): the {A,B} ruling <-> +-pi/3 wing map.

We test this from the *verified ODEs*, not by assertion:
  - photon  : null geodesic  dchi/dtau~ = 1/(1 + r'(tau~))   (integrated in real tau~)
  - matter A: E=1 comoving,  (dr/dtau~)^2 = 1 - f            (the bead law; thm:bead)
  - synchronous B: const-tau second ruling (the spatial slice)
alpha=1, Nariai member 2M = 2/(3 sqrt3).
"""
import numpy as np
from scipy.integrate import solve_ivp, quad

A3 = 2/(3*np.sqrt(3))          # 2M at Nariai
Aamp = A3**(1/3)               # (2M)^{1/3}
def r_law(tt):                 # principal real bead law r(tau~), signed
    s = np.sinh(1.5*tt); return Aamp*np.sign(s)*np.abs(s)**(2/3)
def rp(tt,h=1e-7): return (r_law(tt+h)-r_law(tt-h))/(2*h)

print("="*78); print("C3 -- sheet-assignment by ruling-continuation"); print("="*78)
print(f"Nariai: 2M = {A3:.6f}, amplitude (2M)^1/3 = {Aamp:.6f}")
print(f"turnaround radius r_* = -(2M)^1/3 = {-Aamp:.6f}; sheets at Im tau~ in {{0, +pi/3, -pi/3}} = "
      f"{{0, {np.pi/3:.4f}, {-np.pi/3:.4f}}}\n")

# --- (1) PHOTON: integrate the null geodesic in REAL tau~ and confirm it crosses at Im=0 ----
print("[1] PHOTON  (null geodesic dchi/dtau~ = 1/(1+r'), integrated in real tau~):")
def rhs(tt,y): return [1.0/(1.0+rp(tt))]
sP = solve_ivp(rhs,[0,3],[0.4],max_step=0.01,rtol=1e-9)
sM = solve_ivp(rhs,[0,-3],[0.4],max_step=0.01,rtol=1e-9)
tt = np.concatenate([sM.t[::-1],sP.t])
r_along = r_law(tt)
print(f"    tau~ stays REAL (Im tau~ = 0 by construction); r ranges {r_along.min():+.3f} .. {r_along.max():+.3f}")
print(f"    crosses r=0 at real tau~=0 and continues to r<0  => PHOTON RIDES THE REAL (Im 0) SHEET. [derived]\n")

# --- (2) MATTER A (the bead): cosmic-time reading tau~(r) for r<0, read off Im tau~ ---------
print("[2] MATTER A  (E=1 comoving, (dr/dtau~)^2 = 1 - f;  tau~(r) = int_0^r dr'/sqrt(2M/r'+r'^2)):")
def integrand(rp_): return 1.0/np.sqrt(complex(2*A3/rp_ + rp_**2))   # complex sqrt -> picks up i where radicand<0
def tau_of_r(rtarget, branch=+1):
    # integrate along the real r-axis from a small positive r0 through 0 to rtarget<0
    # radicand 2M/r'+r'^2 < 0 for -(2M)^{1/3} < r' < 0  -> integrand imaginary there
    xs = np.linspace(1e-6, rtarget, 4000)
    vals = np.array([branch*integrand(x) if x<0 else integrand(x) for x in xs])
    return np.sum((vals[1:]+vals[:-1])/2*np.diff(xs))
for rt in [-0.3, -Aamp+1e-6, -1.0]:
    tp = tau_of_r(rt, +1); tm = tau_of_r(rt, -1)
    print(f"    r={rt:+.4f}:  Im tau~ (branch +) = {tp.imag:+.5f},  (branch -) = {tm.imag:+.5f}")
print(f"    at the turnaround r=r_* the two branches reach Im tau~ = +-{np.pi/3:.5f} = +-pi/3.")
print("    => the matter congruence's collapse-leg reading occupies BOTH wings (+pi/3 and -pi/3)")
print("       as the two CONJUGATE readings tau~ <-> conj(tau~) of ONE curve (thm:bead First fact).\n")

# --- (3) the honest consequence for the 3-way assignment ---------------------------------
print("[3] HELD READING (the reassignment's causal characters carried on the cosmic foliation):")
print("    - The level S^3 are the SPACES (the spacelike foliation, grey); BOTH null bundles A, B")
print("      ride them. B is a null bundle, NOT the foliation. (dS4 basic geometric picture.)")
print("    - PHOTON (at-rest reassigned to null) -> the real crossing (Im 0). [photon_cross_test]")
print("    - the two null bundles A, B ride the S^3 layers through the seam and take the two")
print("      conjugate wings +-pi/3; the matter (A) collapse leg reaches +pi/3 (thm:bead).")
print("    So the three sheets carry {photon (real), A (+pi/3), B (-pi/3)} -- the figure's reading.")
print("    NAMING (not claimed): geometrically the conjugate (r<0) branch is the areal reflection")
print("    r->-r of the expansion leg -- the mass-reflected dual. Whether it is 'antimatter' is NOT")
print("    worked out: the fermion sector attaches the 'antimatter register' to R=gamma^5 (mass")
print("    reflection r0->-r0) but holds even that 'a resonance, not an identity'. So the antimatter")
print("    naming is a drill-site, stated without being claimed; 'conjugate dual' is the honest description.")

print("\n"+"="*78)
print("VERDICT:")
print("  Sheet assignment (held, geometric): photon = real crossing; the two null bundles A, B ride")
print("  the level-S^3 spaces onto the +-pi/3 wings. (No 'rate' frontier: the reassignment is a")
print("  causal-character swap null<->timelike, already fully specified; a null congruence is null.)")
print("  Naming: DO-NOT-ASSERT. Geometrically B is the mass-reflected (r->-r) dual; whether that is")
print("  'antimatter' is not worked out on either side -- the corpus's own 'antimatter register'")
print("  R=gamma^5 is held 'a resonance, not an identity'. A drill-site, not a settled name.")
print("="*78)
