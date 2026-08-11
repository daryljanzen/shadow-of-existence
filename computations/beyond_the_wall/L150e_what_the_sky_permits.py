#!/usr/bin/env python3
"""
`L-150`.  ** WHAT THE OBSERVED SPECTRUM PERMITS: A BOUND ON THE PROGENITOR'S RADIATION FRACTION. **

c54.131 computed the mixing: the monodromy at the crunch is unipotent with off-diagonal
$2\\pi ip=-2\\pi i/\\rho$, $\\rho=2\\sqrt B/A$.  This asks what the sky allows.

  PART 1  ** WHICH MODE IS WHICH, in the radiation-dominated crunch. **
  PART 2  ** THE MONODROMY RUNS THE RIGHT WAY: dominant leaks INTO the survivor. **
  PART 3  ** THE RATIO OF LEAKED TO DIRECT IS $2\\pi/(\\rho c_s k)$ — dimensionless, and $k$ is an
          INTEGER because the interior is closed. **
  PART 4  ** THE CROSSOVER MODE NUMBER, AND THE BOUND IT PUTS ON $\\rho_r/\\rho_m$. **
  PART 5  What is solid, and the one step that is not.

Run: python3 L150e_what_the_sky_permits.py      (numpy, scipy)
"""
import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — WHICH MODE IS WHICH")
print("=" * 78)
print("  Near the crunch a = a' sigma with a' = -sqrt(B), so z ∝ a ∝ sigma and zeta = v/a:")
print()
print(f"  {'solution':>12} {'v ~':>8} {'zeta = v/a ~':>16} {'on CONTRACTION':>20} {'on EXPANSION':>16}")
for a, b, c, d, e in [("v_0 (s=0)", "1", "1/sigma", "DOMINANT", "decaying"),
                      ("v_1 (s=1)", "sigma", "constant", "subdominant", "** SURVIVES **")]:
    print(f"  {a:>12} {b:>8} {c:>16} {d:>20} {e:>16}")
print()
print("  ** Same asymmetry as the dust case: what dominates the collapse is what decays after. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE MONODROMY RUNS THE RIGHT WAY")
print("=" * 78)
print("  The unipotent monodromy is  v_0 -> v_0 + 2 pi i p v_1  (c54.131).")
print("  ** So it is precisely the DOMINANT mode that leaks into the SURVIVOR. **")
print("  That is the direction required for the collapse's spectrum to reach an observer, and it")
print("  is not a choice -- the log sits on the s = 0 solution because that is the lower exponent.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RATIO OF LEAKED TO DIRECT")
print("=" * 78)
print("  Deep inside the sound horizon the equation is v'' + (cs k)^2 v = 0 with vacuum data")
print("  v = e^{-i cs k sigma} / sqrt(2 cs k), so on approach to the crunch")
print("     |c_0| ~ 1/sqrt(2 cs k)        |c_1| ~ cs k / sqrt(2 cs k)")
print("  and therefore  |c_0| / |c_1| = 1 / (cs k).  Checked by integration:")


def coeffs(kt, p, L=400.0, s_end=-1e-3):
    """integrate from deep inside to just before the crunch; return |c0|, |c1|"""
    def rhs(s, y):
        pot = p / s
        return [y[1], -(kt**2 - pot) * y[0], y[3], -(kt**2 - pot) * y[2]]
    s0 = -max(L, 200.0 / kt)
    n = np.sqrt(2 * kt)
    y0 = [np.cos(kt * s0) / n, kt * np.sin(kt * s0) / n,
          -np.sin(kt * s0) / n, kt * np.cos(kt * s0) / n]
    sol = solve_ivp(rhs, [s0, s_end], y0, rtol=1e-11, atol=1e-14)
    v = sol.y[0, -1] + 1j * sol.y[2, -1]
    vp = sol.y[1, -1] + 1j * sol.y[3, -1]
    c1 = vp
    c0 = v - c1 * s_end
    return abs(c0), abs(c1)


print(f"\n  {'cs k':>10} {'|c0|':>14} {'|c1|':>14} {'|c0|/|c1|':>14} {'1/(cs k)':>12}")
for kt in [1.0, 2.0, 5.0, 10.0]:
    c0, c1 = coeffs(kt, p=-0.05)          # small p so the free behaviour is clean
    r = c0 / c1
    print(f"  {kt:>10.2f} {c0:>14.6g} {c1:>14.6g} {r:>14.6g} {1.0/kt:>12.6g}")
    assert abs(r * kt - 1.0) < 0.25, (kt, r)
print("\n  ** |c0|/|c1| = 1/(cs k) to better than a quarter, over a decade in k. **")
print()
print("  So the survivor receives:")
print("     LEAKED  :  |2 pi i p| * |c_0|  =  (2 pi / rho) * |c_0|")
print("     DIRECT  :  |c_1|")
print("     ratio   :  (2 pi / rho) * |c_0| / |c_1|  =  ** 2 pi / (rho cs k) **")
print()
print("  ⌗ ** AND THAT IS A PURE NUMBER, because the interior is CLOSED: k is an integer mode")
print("     number on the three-sphere, not a dimensionful wavenumber. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE CROSSOVER, AND THE BOUND")
print("=" * 78)
cs = 1.0 / np.sqrt(3.0)
print(f"  The leaked contribution dominates below the crossover mode number")
print(f"     ** k_x = 2 pi / (rho cs) = 2 pi sqrt(3) / rho = {2*np.pi*np.sqrt(3):.3f} / rho **")
print()
print("  Above k_x the SURVIVOR's own spectrum shows through, and that spectrum is blue: with")
print("  |c_1| ~ sqrt(cs k / 2), P = k^3 |zeta|^2 ∝ k^3 |c_1|^2 ∝ k^4.")
print("  ** So the observed spectrum can only be near scale-invariant out to the largest observed")
print("     mode number if the crossover lies beyond it. **")
print()
print(f"  {'flat out to mode number':>26} {'required rho':>16} {'rho_r/rho_m at a_max':>24} {'a_max/a_eq':>14}")
for lmax in [200, 1000, 2500]:
    rho_req = 2 * np.pi * np.sqrt(3) / lmax
    rr = rho_req**2 / 4.0
    print(f"  {lmax:>26} {rho_req:>16.5f} {rr:>24.3e} {1.0/rr:>14.3g}")
rho_25 = 2 * np.pi * np.sqrt(3) / 2500
rr_25 = rho_25**2 / 4
print()
print(f"  ** For flatness out to the observed multipole range, rho <~ {rho_25:.2e}, i.e. **")
print(f"  ** rho_r/rho_m at the progenitor's maximum expansion <~ {rr_25:.2e}. **")
assert 1e-7 < rr_25 < 1e-4
print()
print(f"  For comparison, our own universe today sits at a_0/a_eq ~ 3400, i.e. rho_r/rho_m ~ "
      f"{1/3400:.2e}.")
print(f"  The bound asks the progenitor to have reached ~{1.0/rr_25/3400:.0f} times further past its")
print(f"  own equality scale than we have so far.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT IS SOLID, AND THE ONE STEP THAT IS NOT")
print("=" * 78)
print(f"  {'step':>52} {'status':>18}")
for a, b in [("the monodromy off-diagonal 2 pi i p", "EXACT (c54.131)"),
             ("|c0|/|c1| = 1/(cs k) from vacuum data", "computed here"),
             ("leaked/direct = 2 pi / (rho cs k)", "follows"),
             ("k is an integer (closed interior)", "structural"),
             ("** the interior mode number = the observed one **", "** ASSUMED **")]:
    print(f"  {a:>52} {b:>18}")
print()
for s in [
 "⚠⚠ ** THE LAST LINE IS THE WHOLE UNCERTAINTY AND IT IS NOT SMALL.  The bound identifies the",
 "   interior's three-sphere harmonic index with the observed multipole, and nothing here",
 "   establishes that map. **  *The corpus's own crossing changes the comoving normalisation, and",
 "   c54.125 showed the geometry transmits no parameters — which cuts both ways: it also transmits",
 "   no scale with which to fix this correspondence.*  ***Until that map is built the number is an",
 "   ORDER OF MAGNITUDE with a stated assumption, not a measurement.***",
 "",
 "✔ ** WHAT SURVIVES THE CAVEAT IS THE SHAPE, AND IT IS THE FIRST TWO-SIDED CONSTRAINT THIS ROW",
 "   HAS EVER HAD: **",
 "   *(i) the observed spectrum's near-flatness REQUIRES the leaked component to dominate over the",
 "   observed range;*",
 "   *(ii) the leaked component dominates below $k_\\times=2\\pi\\sqrt3/\\rho$;*",
 "   *(iii) so a flatter observed spectrum, or one flat to smaller scales, forces a SMALLER $\\rho$",
 "   — a progenitor with LESS radiation at maximum expansion, i.e. one that expanded FURTHER past",
 "   its own equality scale before turning round.*",
 "",
 "⇒⇒ ** AND THE DIRECTION IS THE INTERESTING PART: the sky does not merely permit a progenitor, it",
 "   prefers a LARGE one — large in the specific sense of having run far past matter-radiation",
 "   equality before recollapsing. **  *That is a statement about the parent universe derived from",
 "   the child's power spectrum, and it is the first of its kind in this corpus.*",
 "",
 "⌗ *And it is falsifiable in the ordinary way: build the interior-to-observed mode map, and either",
 "   the required $\\rho$ lands in a physically reachable range or it does not.*",
]:
    print("  " + s)
