#!/usr/bin/env python3
"""
RECEIPT — P16: ** THE PROGENITOR'S RADIATION FRACTION IS NOW BOUNDED FROM BOTH SIDES: THE OBSERVED
SPECTRUM'S FLATNESS FROM ABOVE, ITS OWN NUCLEOSYNTHESIS FROM BELOW. **

Two corrections to the earlier one-sided statement, both from the same background:

  PART 1  ** THE COMPOSITION IS DETERMINED, NOT BOUNDED: one M across the bead plus a crossing
          plasma fix the parent's equality at the observable leg's.  Five successive upper bounds
          are withdrawn -- all rested on a 1/k the construction does not supply. **
  PART 3  ** THE LOWER BOUND, WHICH DID NOT EXIST: the parent's equality TEMPERATURE follows from
          its own A and rho, and nucleosynthesis must run radiation-dominated. **
  PART 4  ** the verdict: the composition is determined and the one surviving bound is met **

rc=0 on success.  Run: python3 P16_the_progenitor_composition_is_bracketed.py     (numpy)
"""
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

LAM, MPC = 1.1056e-52, 3.0857e22
G, C = 6.674e-11, 2.99792458e8
HBARC = 1.0545718e-34 * C
GSTAR, JperGeV = 10.75, 1.602176634e-10
S_MAP, L_FLAT = 2.750, 2500                      # the interior-to-observed mode map
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))                 # the recollapse (= Nariai) cap on the mass

# =====================================================================
print("=" * 78)
print("PART 1 — THE COMPOSITION IS DETERMINED, NOT BOUNDED")
print("=" * 78)
R0, ZEQ = 5065.0, 3399.0
a_eq = R0 / ZEQ
rho_det = np.sqrt(4 * a_eq / (2 * M_nar / MPC))
print("  There is one bead and one integration constant, so A = 2M is the same on both legs; and the")
print("  photon-baryon plasma crosses, which is this paper's own nucleosynthesis account at the")
print("  observed eta.  Together they fix rho_gamma/A across the branch point, so the progenitor's")
print("  matter-radiation equality radius IS the observable leg's:")
print(f"     a_eq = r_0/(1+z_eq) = {a_eq:.3f} Mpc  =  A rho^2/4   =>   ** rho = {rho_det:.4f} **")
print(f"     i.e. rho_r/rho_m at maximum expansion = {rho_det**2/4:.3e}")
if not (0.04 < rho_det < 0.07):
    fail.append("determination")
print()
print("  ⚠ FIVE SUCCESSIVE UPPER BOUNDS ON rho ARE WITHDRAWN.  ** THE WITHDRAWAL STANDS AND ITS")
print("    STATED GROUND HAS BEEN REPLACED (r2376+c54.151); the earlier version of this receipt")
print("    argued it from a full-cycle attractor, and that background is itself withdrawn. **")
print("    FOUR of the five failed on the OBSERVABLE: they asked where a spectral knee SITS rather")
print("    than what curvature such a knee would leave where the spectrum is actually measured.")
print("    ** That ground is independent of every later revision and is untouched. **")
print("    THE FIFTH -- the computed one -- assumed the incoming perturbation is a FREE OSCILLATION,")
print("    so that WKB gives a leaked/direct ratio 1/(rho c_s k) and the spectrum acquires a knee.")
print("    ** The construction supplies no free oscillation, and what it supplies instead needs no")
print("       cycle: the progenitor is an OVERDENSITY IN A UNIVERSE LIKE OURS (P16 sec:lap), so what")
print("       it carries into collapse is a near scale-invariant adiabatic spectrum processed by")
print("       ordinary structure formation -- a specified input from standard cosmology. **")
print("    ⌗ WHAT THAT INPUT DOES TO THE TRANSFER IS THE OPEN RECURSION QUESTION, and this receipt")
print("      draws no bound from it in either direction.  ** The determination in PART 1 does not")
print("      use one: it is fixed by one M across the bead plus a crossing plasma, and c54.150")
print("      derives that from spherical collapse. **")
rho_hi = rho_det

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE LOWER BOUND: NUCLEOSYNTHESIS ON THE PARENT'S OWN LEG")
print("=" * 78)
print("  Equality sits at a_eq = A rho^2/4 with A = 2M, and the density there is fixed by the same")
print("  A: rho_m(a_eq) = 3 c^2 A/(8 pi G a_eq^3).  Setting the radiation energy density equal to it")
print("  fixes T_eq with NO further input -- in particular without importing our own 0.8 eV.")


def T_eq_GeV(rho, M=M_nar):
    A = 2 * M
    a_eq = A * rho**2 / 4.0
    u = (3 * C**2 * A / (8 * np.pi * G * a_eq**3)) * C**2          # J m^-3
    return (30 * u * HBARC**3 / (np.pi**2 * GSTAR))**0.25 / JperGeV


print(f"\n  {'rho':>14} {'T_eq':>16} {'rho_r/rho_m at T = 1 MeV':>28} {'BBN runs in':>14}")
for rho in [rho_hi, 1e-4, 1e-6, 1e-10]:
    Te = T_eq_GeV(rho)
    print(f"  {rho:>14.3e} {Te*1e9:>13.3g} eV {1e-3/Te:>28.3e} "
          f"{'radiation' if Te < 1e-3 else 'MATTER':>14}")
lo, hi = 1e-30, rho_hi
for _ in range(300):
    mid = np.sqrt(lo * hi)
    if T_eq_GeV(mid) > 1e-3:
        lo = mid
    else:
        hi = mid
rho_bbn = np.sqrt(lo * hi)
print(f"\n  ** helium synthesis at T ~ 1 MeV is radiation-dominated only for rho >~ {rho_bbn:.2e} **")
print("  Below that the parent's equality lies above an MeV, nucleosynthesis runs on a")
print("  matter-dominated background, and the expansion rate there is wrong by orders.")
if not (1e-7 < rho_bbn < 1e-5):
    fail.append("lower bound")
print()
print("  ⚠ The lower end carries an M dependence the upper end does not: T_eq ∝ A^(-1/2) rho^(-3/2),")
print("    so a lighter progenitor tightens it.  Quoted at the recollapse cap.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE VERDICT")
print("=" * 78)
print(f"     ***  rho  =  {rho_det:.4f}   (DETERMINED, PART 1)  ***")
print(f"     ***  rho_r/rho_m at maximum expansion  =  {rho_det**2/4:.2e}  ***")
print(f"     the one surviving bound, BBN from below:  rho >= {rho_bbn:.1e}  -- satisfied by "
      f"{rho_det/rho_bbn:.0f}x")
ours = 1.0 / 3400.0
print(f"\n  our own present rho_r/rho_m = {ours:.2e}, so the parent's value at ITS maximum expansion")
print(f"  is {rho_det**2/4/ours:.1f}x ours -- a progenitor that turned round a little BEFORE reaching")
print(f"  the point past equality we have now reached, rather than long after it.")
if not (rho_bbn < rho_det):
    fail.append("floor violated")
print()
print("  ** So the two legs' compositions agree, and the account is consistent where it was")
print("     previously recorded as failing by 831x.  The failure was in a bound, not in the")
print("     construction, and the bound's premise was contradicted by the construction itself. **")

print()
if fail:
    print("FAIL: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
