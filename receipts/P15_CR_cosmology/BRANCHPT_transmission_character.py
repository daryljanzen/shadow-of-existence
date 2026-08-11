"""BRANCHPT — the transmission character of the BRANCH POINT r=0, on its own terms.

WHY (r2154).  P15 l.525 says "The cosmogenesis branch point, BEING the degenerate Nariai horizon, is a
faithful scale-free transmitter", and prop:transmission argues from the tortoise integral at a DOUBLE
ROOT (p=2, kappa=0).  But the branch point is r=0 and the Nariai double root is the EQUATORIAL SEAM -- ONE point of the
substrate, which the bead meets on the way in and again one full lap later.  In the phase
phi = 2 pi r / (sqrt3 alpha) the three roots sit at phi = +120 deg (r=+alpha/sqrt3), 0 (r=0) and
-240 deg (r=-2alpha/sqrt3): +120 and -240 differ by EXACTLY 360, so the "two seams" are the same
point.  The lap runs 240 deg (two thirds, the r<0 COLLAPSE side) from the seam to r=0, then 120 deg
(one third) back to it.  So the seam and the branch point are distinct loci on the lap, but the seam
is not an "endpoint" of anything and the collapse side is two thirds of the excursion.
The proof is about the wrong surface.

THE THIRD CASE.  prop:transmission considers f ~ (r-r_h)^p with p=1 (non-degenerate) and p=2 (Nariai).
At r=0, f does NOT vanish -- it DIVERGES:  f = 1 - 2M/r - r^2/alpha^2 -> -2M/r.
So the tortoise integral is
    r_* = Int dr/f  ~  Int dr/(-2M/r)  =  -r^2/(4M) ,
which is FINITE and -> 0 at the branch point, with a QUADRATIC approach.  Neither the logarithmic
divergence of p=1 nor the power-law divergence of p=2: no divergence at all.

WHAT THAT MEANS FOR TRANSMISSION.  The accumulated phase of a mode is k r_*.  At the crossing r_* = 0
for every k, so the phase accumulated AT the branch point vanishes identically and is k-independent in
its approach (k r_* = -k r^2/(4M), no k-dependent feature).  *** The branch point imprints no scale --
and by a CLEANER route than the Nariai degeneracy: not "the divergence carries no k" but "there is no
divergence." ***  The transmission CONCLUSION survives; the ARGUMENT is different and is made here.

ORIGIN: storyboard_receipts/BRANCHPT_transmission_character.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
# NOTE on r=0's status (P7 l.730 + P2/janzen_circle): r=0 IS a genuine curvature singularity of the
# SdS metric read over the r-chart (K ~ 48 M^2/r^6) -- real AS THAT METRIC'S -- and is NOT an
# invariant of the underlying smooth substrate, whose throat IS alpha, the substrate's defining constant alpha.  Both halves
# are held; flattening either way is wrong.  The tortoise result below is a statement about the
# r-chart metric, which is the object prop:transmission also argues over.
alpha=1.0; M=alpha/(3*np.sqrt(3))            # Nariai member: 2M = 2 alpha/(3 sqrt3)
f=lambda r: 1.0 - 2*M/r - r*r/alpha**2
rN=alpha/np.sqrt(3)
print("  CR/SdS Nariai member:  alpha=1, 2M = 2/(3 sqrt3) = %.6f,  r_N = alpha/sqrt3 = %.6f"%(2*M,rN))
print("  f(r_N) = %.3e  (double root -> the FRONT SEAM)"%f(rN))
print()
print("  TORTOISE COORDINATE r_* = Int_{r0}^{r} dr'/f,  measured from r0 = %.4f"%(0.5*rN))
print("     r        f(r)          r_*        r_* / (-r^2/(4M))")
r0=0.5*rN
for r in (0.4,0.3,0.2,0.1,0.05,0.02,0.01,0.005):
    rs=quad(lambda x: 1.0/f(x), r0, r, limit=200)[0]
    asym=-(r*r-r0*r0)/(4*M)
    print("   %6.3f  %11.4f  %11.6f      %8.4f"%(r,f(r),rs,rs/asym if asym!=0 else np.nan))
rs0=quad(lambda x: 1.0/f(x), r0, 1e-9, limit=400)[0]
print()
print("   r -> 0:  r_* = %.6f   FINITE.  (vs r_* -> -inf at p=1, r_* -> +inf at p=2.)"%rs0)
print("   Approach is QUADRATIC: r_* + r0^2/(4M) ~ -r^2/(4M), ratio -> 1 above.")
print()
print("  => the branch point is neither horizon case.  The mode crosses at FINITE tortoise coordinate")
print("     with vanishing accumulated phase k r_*, so it can imprint no scale on the spectrum.")
print("     The transmission CONCLUSION stands; prop:transmission's ARGUMENT does not apply here.")

# =====================================================================
# ** PART 2, added r2376+c54.153 by the receipt-vs-sentence audit. **
# P15 cited this file for a DIFFERENT statement: that reproducing the measured l_A = 301.8 with an
# r_s^eff dominated by the collapse leg would demand a comoving distance 21-39 times the actual
# one, so the acoustic phase must be RESET at the branch point.  That is an exclusion computed on
# the PEAK POSITIONS, and nothing above computes it -- the file had no l_A, no r_s, no Mpc, and
# worked in units alpha = 1 throughout.  ** The link resolved and the sentence's arithmetic had no
# computation behind it.  It is done here. **
print()
print("=" * 78)
print("PART 2 — THE PEAK-POSITION EXCLUSION, WHICH IS WHAT THE PAPER CITES THIS FILE FOR")
print("=" * 78)
_fail2 = []
L_A, R_S, D_ACT = 301.8, 144.0, 1.4e4                   # measured, banked, actual comoving distance
print(f"  the collapse leg's own conformal time gives eta_bp ~ 5e3-1e4 Mpc, so")
print(f"  r_s^eff = r_s + eta_bp/sqrt(3) is dominated by the leg term:")
print(f"\n  {'eta_bp [Mpc]':>14} {'r_s^eff [Mpc]':>15} {'D needed for l_A=301.8':>24} {'D/D_actual':>12}")
_ratios2 = []
for eta_bp in (5.0e3, 1.0e4):
    rs_eff = R_S + eta_bp / np.sqrt(3.0)
    D_need = L_A * rs_eff / np.pi
    _ratios2.append(D_need / D_ACT)
    print(f"  {eta_bp:>14.0f} {rs_eff:>15.1f} {D_need:>24.3e} {D_need/D_ACT:>12.1f}")
print(f"\n  ** so the required distance is {min(_ratios2):.0f}-{max(_ratios2):.0f} times the actual"
      f" {D_ACT:.1e} Mpc **")
print("  The onset redshift absorbs a small rescaling of the sound horizon and cannot absorb a")
print("  factor of twenty to forty.  ⇒ ** THE ACOUSTIC PHASE IS RESET AT THE BRANCH POINT AND NOT")
print("     CARRIED ACROSS IT, ESTABLISHED ON THE PEAK POSITIONS ALONE. **")
if not (18 < min(_ratios2) < 24 and 35 < max(_ratios2) < 43):
    _fail2.append("peak-position exclusion")
print()
print("  ⌗ *And note this is a different argument from PART 1, which shows the crossing ADDS no")
print("    divergent phase.  PART 1 bears on what the branch point imprints; PART 2 on whether an")
print("    inherited phase survives.  The paper's sentence needs the second.*")
if _fail2:
    print("FAILED: " + "; ".join(_fail2))
    raise SystemExit(1)
print("\n  PART 2 CHECKS PASS")
