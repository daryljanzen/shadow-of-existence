#!/usr/bin/env python3
"""
** !! THE BOUND THIS FILE COMPUTES IS WITHDRAWN (r2376+c54.143, ground revised c54.151).  IT
IS ONE OF THE FIVE SUCCESSIVE UPPER BOUNDS ON rho, AND IT IS ALSO THE LAST OF THEM TO BE
MARKED. **  Two independent reasons, and the file presents itself as live for neither:

  (i)  ** THE OBSERVABLE. **  It asks where the spectral KNEE sits rather than what curvature
       such a knee would leave in the range where the spectrum is actually measured.  That
       ground is untouched by every later revision.
  (ii) ** THE PREMISE. **  Its leaked/direct ratio 1/(rho c_s k) is the WKB value for an
       incoming FREE OSCILLATION -- and its own PART 2 asserts that ratio at p = -0.05,
       i.e. rho = 20, seven orders in radiation fraction away from the rho <~ 0.0044 it then
       derives.  It is verified in the one regime where it is trivial and applied where it
       is not.  The construction supplies no free oscillation: the progenitor is an
       overdensity in a universe like ours, so it carries a processed adiabatic spectrum.

** AND A THIRD DEFECT, SEPARATE FROM THE WITHDRAWAL: the chain here is SCALAR (zeta = v/z,
a sound speed, an acoustic index) and it uses z ~ a and the off-diagonal 2 pi/rho, which are
the TENSOR values.  The scalar residue doubles (c54.146), so this file's crossover and bound
would move by a factor 4 even on its own terms. **

*What survives is the direction of the effect stated in PART 1 -- more radiation mixes less --
which is read off the monodromy and needs no bound.*  The composition is DETERMINED, not
bounded: see `P16_the_progenitor_composition_is_bracketed`.

RECEIPT — P16 (the collapse excursion): ** THE OBSERVED SPECTRUM'S FLATNESS BOUNDS THE PROGENITOR'S
RADIATION FRACTION AT MAXIMUM EXPANSION.  THE FIRST TWO-SIDED CONSTRAINT ON THE PROGENITOR. **

  PART 1  which mode is which at a radiation-dominated crunch, and that the monodromy runs the
          right way -- the DOMINANT mode leaks INTO the SURVIVOR
  PART 2  ** |c0|/|c1| = 1/(cs k) from vacuum data, so leaked/direct = 2 pi/(rho cs k) **
  PART 3  ** the crossover mode number, and the bound **

rc=0 on success.  Run: python3 P16_what_the_sky_permits.py     (numpy, scipy)
"""
import sys

import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("rc=0")[0])

print("=" * 78)
print("PART 1 — THE MONODROMY RUNS THE RIGHT WAY")
print("=" * 78)
print("  a = a' sigma near the crunch, z ∝ a, so zeta = v/a:")
print("     v_0 ~ 1     -> zeta ~ 1/sigma : DOMINANT on contraction, decaying after")
print("     v_1 ~ sigma -> zeta ~ const   : subdominant, and the SURVIVOR")
print("  and the unipotent monodromy is v_0 -> v_0 + 2 pi i p v_1.")
print("  ** So the collapse's dominant mode leaks precisely into the mode that survives, and it is")
print("     not a choice: the log sits on s = 0 because that is the lower exponent. **")

print()
print("=" * 78)
print("PART 2 — THE RATIO OF LEAKED TO DIRECT")
print("=" * 78)


def coeffs(kt, p=-0.05, s_end=-1e-3):
    def rhs(s, y):
        pot = p / s
        return [y[1], -(kt**2 - pot) * y[0], y[3], -(kt**2 - pot) * y[2]]
    s0 = -max(400.0, 200.0 / kt)
    n = np.sqrt(2 * kt)
    y0 = [np.cos(kt * s0) / n, kt * np.sin(kt * s0) / n,
          -np.sin(kt * s0) / n, kt * np.cos(kt * s0) / n]
    sol = solve_ivp(rhs, [s0, s_end], y0, rtol=1e-11, atol=1e-14)
    v = sol.y[0, -1] + 1j * sol.y[2, -1]
    vp = sol.y[1, -1] + 1j * sol.y[3, -1]
    return abs(v - vp * s_end), abs(vp)


print(f"  {'cs k':>8} {'|c0|/|c1|':>14} {'1/(cs k)':>12} {'product':>10}")
for kt in [1.0, 2.0, 5.0, 10.0]:
    c0, c1 = coeffs(kt)
    r = c0 / c1
    print(f"  {kt:>8.2f} {r:>14.6g} {1.0/kt:>12.6g} {r*kt:>10.4f}")
    assert abs(r * kt - 1.0) < 0.25, (kt, r)
print("  ** |c0|/|c1| = 1/(cs k), asserted within a quarter over a decade. **")
print("  So  leaked/direct = (2 pi/rho) |c0|/|c1| = ** 2 pi / (rho cs k) **, a PURE NUMBER --")
print("  the interior is CLOSED, so k is an integer harmonic index on the three-sphere.")

print()
print("=" * 78)
print("PART 3 — THE CROSSOVER AND THE BOUND")
print("=" * 78)
kx = 2 * np.pi * np.sqrt(3)
print(f"  crossover:  k_x = 2 pi sqrt(3) / rho = {kx:.3f} / rho")
print("  above it the survivor's own spectrum shows through, and it is blue (P ∝ k^4), so the")
print("  observed near-flatness requires the crossover to lie beyond the observed range.")
print()
print(f"  {'flat to mode number':>22} {'rho <=':>12} {'rho_r/rho_m at a_max':>22} {'a_max/a_eq':>12}")
for lm in [200, 1000, 2500]:
    rr = (kx / lm)**2 / 4
    print(f"  {lm:>22} {kx/lm:>12.5f} {rr:>22.3e} {1/rr:>12.3g}")
rr25 = (kx / 2500)**2 / 4
assert 1e-7 < rr25 < 1e-4
print(f"\n  ** rho_r/rho_m at the progenitor's maximum expansion <~ {rr25:.2e} **")
print(f"     (our own universe today: a_0/a_eq ~ 3400, rho_r/rho_m ~ {1/3400:.2e})")
print()
print("  ⚠ THE ASSUMPTION, AND IT IS THE WHOLE UNCERTAINTY: this identifies the interior's")
print("  three-sphere harmonic index with the observed multipole.  Nothing here establishes that")
print("  map, and c54.125 showed the geometry transmits no parameter with which to fix it.")
print("  ** Until it is built the NUMBER is an order of magnitude with a stated assumption.  What")
print("  survives regardless is the SHAPE: a flatter observed spectrum, or one flat to smaller")
print("  scales, forces a SMALLER rho -- a progenitor that ran further past its own equality scale")
print("  before turning round. **")
print()
print("ALL PASS")
sys.exit(0)
