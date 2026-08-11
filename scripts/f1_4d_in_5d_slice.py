import sympy as sp

print("="*70)
print("How the 4D background geometry sits in the 5D substrate as a slice.")
print("="*70)

t, rho, chi, th, ph, al, M = sp.symbols('t rho chi theta phi alpha M', positive=True)

# dS5 static patch: spatial S^3 written as  dchi^2 + sin^2(chi) dOmega2^2
# ds^2 = -(1-rho^2/al^2) dt^2 + drho^2/(1-rho^2/al^2) + rho^2 ( dchi^2 + sin^2 chi dOmega2^2 )
fdS = 1 - rho**2/al**2
dOmega2 = sp.diag(1, sp.sin(th)**2)                      # (theta, phi) 2-sphere
# full dS5 metric in coords (t, rho, chi, theta, phi)
g5 = sp.diag(-fdS, 1/fdS, rho**2, rho**2*sp.sin(chi)**2, rho**2*sp.sin(chi)**2*sp.sin(th)**2)
print("\ndS5 metric diag (t, rho, chi, theta, phi):")
sp.pprint(g5)

# --- the slice chi = pi/2 (the equator of the S^3) ---
print("\n[1] Slice at chi = pi/2.  Induced metric (drop chi, set sin(chi)=1):")
g4 = sp.diag(-fdS, 1/fdS, rho**2*sp.sin(th)**2/sp.sin(th)**2 * 0 + rho**2, rho**2*sp.sin(th)**2)
# build induced metric on (t, rho, theta, phi) directly
g4 = sp.Matrix([
    [-fdS, 0, 0, 0],
    [0, 1/fdS, 0, 0],
    [0, 0, rho**2, 0],
    [0, 0, 0, rho**2*sp.sin(th)**2],
])
sp.pprint(g4)
print("   = -(1-rho^2/al^2) dt^2 + drho^2/(1-rho^2/al^2) + rho^2 dOmega2^2")
print("   = the 4D de Sitter background dS4 (static patch), with S^2 angular. ")

# --- is the slice totally geodesic?  extrinsic curvature ~ d/dchi (g) at chi=pi/2 ---
print("\n[2] Totally geodesic?  K_ab is proportional to  d g_ab/d chi  at chi = pi/2.")
only_chi_dep = rho**2*sp.sin(chi)**2          # the sole chi-dependent metric component (the S^2 block)
dK = sp.diff(only_chi_dep, chi).subs(chi, sp.pi/2)
print("   d/dchi (rho^2 sin^2 chi) at chi=pi/2 =", sp.simplify(dK),
      " -> 0, so K_ab = 0  =>  the slice is TOTALLY GEODESIC.")
print("   => the LIFT direction (the 5th dimension, off the 4D geometry) is chi,")
print("      the extra S^3 angle.  dS4 = { chi = pi/2 } sits in dS5 cleanly.")

# --- SdS does NOT arise as a single tilt of this slice (see f1_sds_codim1_test.py) ---
print("\n[3] SdS (M != 0): NOT a single tilt of this slice. [RETRACTION of an earlier guess.]")
print("    The Gauss test (scripts/f1_sds_codim1_test.py) gives obstruction = -3 M^2/r^6 != 0:")
print("    SdS does NOT embed as a codim-1 slice of dS5 at all -- it is embedding class 2,")
print("    needing TWO extra dimensions. The tilt-into-chi picture holds ONLY for the vacuum")
print("    (dS4 above). SdS relates to the substrate through Paper 3's INTRINSIC slicing curve")
print("    (dS & Schwarzschild as two readings of one slicing, joined at the seam), not by")
print("    sitting inside dS5 as a surface. Lambda drops out of the obstruction entirely.")

print("\n" + "="*70)
print("PLAIN STATEMENT")
print("="*70)
print("""
The 5D substrate dS5 has 3-sphere (S^3) angular structure. The 4D background
geometry dS4 is the equatorial slice of it -- the surface chi = pi/2, where chi
is the extra S^3 angle. That slice is totally geodesic (its extrinsic curvature
is zero), so dS4 sits inside dS5 as a clean, flat cut. The "lift" -- the one
extra dimension the substrate has over the 4D geometry -- is the chi direction.

SdS (mass != 0) is NOT a single tilt of this slice. The Gauss obstruction is
-3 M^2/r^6 (nonzero): SdS is embedding class 2, it does not sit in dS5 as a
codim-1 surface at all. The tilt-into-chi picture holds only for the vacuum.
SdS relates to the substrate through Paper 3's intrinsic slicing curve, not an
embedding. (See scripts/f1_sds_codim1_test.py.)

This is a computation, not a choice: dS4 = {chi=pi/2} in dS5, lift = chi.
""")
