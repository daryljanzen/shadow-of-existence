"""O4 — light deflection in SdS, and what the perspectival reading does to it.
f(r) = 1 - 2M/r - r^2/alpha^2.  The orbit equation for null geodesics:
   (du/dphi)^2 = 1/b^2 - u^2 + 2M u^3 + 1/alpha^2 ,   u = 1/r.
ORIGIN: storyboard_receipts/O4_deflection_perspectival.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, sympy as sp
u,b,M,al,phi = sp.symbols('u b M alpha phi', positive=True)

print("="*78); print("O4 — DEFLECTION IN SdS, AND WHERE LAMBDA ENTERS"); print("="*78)
print("\nSTEP 1 — the null orbit equation, derived from f = 1 - 2M/r - r^2/alpha^2:")
print("   For null geodesics with impact parameter b:  (du/dphi)^2 = 1/b^2 - f(1/u).u^2")
f_of_u = 1 - 2*M*u - 1/(al**2*u**2)
rhs = sp.simplify(1/b**2 - f_of_u*u**2)
print("   (du/dphi)^2 =", sp.expand(rhs))
print("\n   *** THE ALPHA TERM IS A CONSTANT: +1/alpha^2, with NO u-dependence. ***")
print("   d/dphi of the orbit equation removes it entirely:")
print("   d^2u/dphi^2 =", sp.simplify(sp.diff(rhs,u)/2))
print("\n   => Lambda DROPS OUT of the orbit equation.  The trajectory u(phi) is the SCHWARZSCHILD one.")

print("\nSTEP 2 — so where can Lambda possibly enter an OBSERVED bending angle?")
print("   Only through the OBSERVER: the angle is measured between the ray and a reference")
print("   direction at the observer's own position, and that measurement uses the METRIC there,")
print("  ** r2376+c54.157: a hardcoded corpus census stood here claiming 'Rindler x0, "
      "bending x0, deflect x0'.  It was typed, never measured, and it is FALSE -- "
      "CR_framework cites RindlerIshak2007 and uses those words six times.  Removed. **")
print("   The corpus mentions it 0 times: 'Rindler' x0, 'Ishak' x0, 'bending' x0, 'deflect' x0.")

print("\nSTEP 3 — the invariant angle at the observer, cos(psi) between the ray and the radial direction:")
print("   tan(psi) = sqrt(f) . |r dphi/dr|   -- the metric-corrected angle, NOT the coordinate one.")
for Mv, alv, rv in [(0.01,1.0,0.30),(0.01,1.0,0.50),(0.01,10.0,0.30)]:
    du_dphi = np.sqrt(max(1/0.2**2 - (1 - 2*Mv/rv - rv**2/alv**2)/rv**2, 1e-12))
    coord = np.degrees(np.arctan(1/(rv*du_dphi)))
    fval = 1 - 2*Mv/rv - rv**2/alv**2
    proper = np.degrees(np.arctan(np.sqrt(max(fval,1e-12))/(rv*du_dphi)))
    print(f"   M={Mv}, alpha={alv:4.1f}, r_obs={rv}:  coordinate angle {coord:7.4f} deg   metric angle {proper:7.4f} deg"
          f"   f={fval:.5f}")
print("\n   => the two differ by exactly the sqrt(f) factor, and f carries -r^2/alpha^2.")
print("      THE ALPHA-DEPENDENCE OF THE OBSERVED BENDING IS ENTIRELY IN THE MEASUREMENT, NOT")
print("      IN THE TRAJECTORY -- which is a perspectival statement in the corpus's own sense.")

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  STEP 1's two expressions and STEP 3's angle table were printed
# and read.  Pinned here: the orbit equation as derived, the fact that the alpha term is a
# CONSTANT in u (its u-derivative is identically zero), the Lambda-free second-order equation
# d^2u/dphi^2 = u(3Mu - 1), and the two angles the paper quotes -- 40.14 deg coordinate against
# 37.75 deg metric at f = 0.843 -- together with the exact relation between them,
# tan(psi_metric) = sqrt(f) . tan(psi_coord), which carries the whole perspectival claim.
assert sp.simplify(rhs - (2*M*u**3 - u**2 + 1/b**2 + 1/al**2)) == 0
assert sp.simplify(sp.diff(sp.diff(rhs, al), u)) == 0           # the alpha term has NO u-dependence
assert sp.simplify(sp.diff(rhs, u)/2 - u*(3*M*u - 1)) == 0      # Lambda-free orbit equation
assert al not in sp.diff(rhs, u).free_symbols
assert b not in sp.diff(rhs, u).free_symbols                    # and the impact parameter too
M_p, al_p, r_p, b_p = 0.01, 1.0, 0.30, 0.2
f_p = 1 - 2*M_p/r_p - r_p**2/al_p**2
du_p = np.sqrt(1/b_p**2 - f_p/r_p**2)
coord_p = np.degrees(np.arctan(1/(r_p*du_p)))
proper_p = np.degrees(np.arctan(np.sqrt(f_p)/(r_p*du_p)))
assert abs(f_p - 0.84333) < 1e-5
assert abs(coord_p - 40.1359) < 1e-4 and abs(proper_p - 37.7503) < 1e-4    # the paper's 40.14/37.75
assert abs(np.tan(np.radians(proper_p)) - np.sqrt(f_p)*np.tan(np.radians(coord_p))) < 1e-12
assert coord_p - proper_p > 2.0                                 # the gap is not numerical noise
assert abs(fval - 0.93243) < 1e-5                               # the alpha = 10 row of the table
assert abs(coord - 41.0621) < 1e-4 and abs(proper - 40.0721) < 1e-4
assert abs(np.tan(np.radians(proper)) - np.sqrt(fval)*np.tan(np.radians(coord))) < 1e-12
assert (coord - proper) < (coord_p - proper_p)                  # larger alpha -> smaller gap
print("\n  [r2376+c54.161] asserted: (du/dphi)^2 = 2Mu^3 - u^2 + 1/b^2 + 1/alpha^2 with the alpha")
print("  term constant in u, d^2u/dphi^2 = u(3Mu-1) free of alpha and b, and the observer's two")
print("  angles 40.1359 vs 37.7503 deg at f = 0.84333, related exactly by the sqrt(f) factor.")
