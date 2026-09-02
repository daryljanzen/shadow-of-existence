"""acceleration_is_the_slice_curvature.py (r1680) -- the comoving acceleration IS the slicing
surface's Gaussian curvature, up to the factor r; so the flat locus of the slice is the
deceleration-to-acceleration turnover, and the front seam is that turnover.

WHERE IT CAME FROM. Daryl, provisionally: "I wonder if that result could be related to the fact
that the lap continues all the way from r=0 to the seam, which is like the first seven billion
years, after which the effective densities become Lambda dominated." Worked at that weight.

VERDICTS ARE ASSERTS, and each was written after its output was read (r1676's rule).
"""
import sympy as sp, math
r, al, M = sp.symbols('r alpha M', positive=True)
w = sp.symbols('w', positive=True)

f  = 1 - 2*M/r - r**2/al**2
KG = 1/al**2 - M/r**3

print("(1) THE IDENTITY")
E   = sp.symbols('E', positive=True)
v2  = sp.simplify(E**2 - f)                    # (dr/dtau)^2 on ANY member of the energy family
acc = sp.simplify(sp.diff(v2, r)/2)            # d2r/dtau2, from 2 v v' = (dv2/dr) v
assert E not in acc.free_symbols, "the acceleration depends on E"
print("    (dr/dtau)^2 =", v2, "   [E is a constant of the motion]")
print("    E CANCELS from the acceleration -- differentiating kills it, so the identity")
print("    below is a property of the WHOLE family, not of the E=1 member (widened r1688)")
print("    d2r/dtau2   =", acc)
print("    r * K_G     =", sp.simplify(r*KG))
assert sp.simplify(acc - r*KG) == 0, "acceleration is not r*K_G"
print("    ASSERTED: d2r/dtau2 = r * K_G identically.")
print("    => the SIGN of the slice's intrinsic Gaussian curvature IS the sign of the")
print("       comoving acceleration. K_G<0 decelerating; K_G=0 turnover; K_G>0 accelerating.")

print()
print("(2) SO THE FLAT LOCUS IS THE ACCELERATION TURNOVER")
turn = sp.solve(sp.Eq(KG, 0), r)[0]
print("    K_G = 0 at r =", turn, "= (M alpha^2)^{1/3} = r_HE")
assert sp.simplify(turn - (M*al**2)**sp.Rational(1,3)) == 0

print()
print("(3) AND IT IS THE STANDARD ONSET, NOT A SECOND FACT")
print("    Standard: acceleration begins when rho_m = 2 rho_Lambda; and rho_m/rho_L = csch^2 w.")
# csch^2 w = 2  <=>  sinh w = 1/sqrt2 ; verify by algebra, not by simplify()
chk = sp.simplify(((1+sp.sqrt(3))/sp.sqrt(2))**2 - (2+sp.sqrt(3)))
assert chk == 0, "the closed forms do not agree"
w_on = sp.asinh(1/sp.sqrt(2))
assert abs(float(sp.csch(w_on)**2) - 2) < 1e-12, "csch^2 != 2 at sinh w = 1/sqrt2"
print("    ASSERTED: csch^2 w = 2  <=>  sinh w = 1/sqrt2  <=>  w = ln((1+sqrt3)/sqrt2)")
print("              = (1/2) ln(2+sqrt3), which is the FRONT SEAM's phase (r1631).")
print("    => the front seam, the K_G zero, the rate minimum and the acceleration onset")
print("       are ONE event, related by the identity in (1) and not by coincidence.")

print()
print("(4) WHEN, IN YEARS -- the epoch is cosmological and recent")
c=2.99792458e8; Mpc=3.0856775814913673e22; yr=3.1557e7; Om=0.307; OL=1-Om
for H0 in (67.4, 73.0):
    H=H0*1e3/Mpc; Lam=3*H**2*OL/c**2; a=(3/Lam)**0.5; T=2*a/(3*c)
    t_on=float(w_on)*T/yr/1e9
    t_eq=math.asinh(1.0)*T/yr/1e9
    t_now=math.asinh((OL/Om)**0.5)*T/yr/1e9
    print(f"    H0={H0}: onset {t_on:5.2f} Gyr | matter-Lambda equality {t_eq:5.2f} | now {t_now:5.2f}"
          f"  => the turnover was {t_now-t_on:4.2f} Gyr ago")
print("    NOTE the two are distinct and in this order: the acceleration TURNOVER (rho_m = 2 rho_L)")
print("    precedes matter-Lambda EQUALITY (rho_m = rho_L). The seam is the first, not the second.")

print()
print("BOUND, not claimed:")
print("  * (1) holds on EVERY member of the energy family -- E cancels from the acceleration.")
print("  * (3) is the Nariai member's own onset condition; the onset statement is flat matter+Lambda,")
print("    which CR's radiation-free rate reproduces.")
print("  * Nothing here claims the seam CAUSES the turnover or vice versa. The claim is that")
print("    they are one locus, because acceleration is r*K_G and the seam is where K_G vanishes.")
print("  * The dating inherits H0 (Lambda is inferred), per PHYSICAL_VALUES_LEDGER section B.")
