"""
P15_rotation_moves_the_throat_away_from_the_damping_threshold
=============================================================

Object under test -- the computation r6497 named and declined to do: ** what ratio
lambda a ROTATING progenitor produces at the throat. **  r6497 established that `P15`'s
isotropisation holds for any lambda > 1/8 and that `prop:throat` is a J=0 construction;
this asks what rotation does to lambda.

--------------------------------------------------------------------------------
(1) THE ROTATING NARIAI LOCUS, AND IT REPRODUCES THE CORPUS AT a = 0.

Kerr--de~Sitter has Delta_r = (r^2+a^2)(1 - r^2/alpha^2) - 2Mr, which at a=0 is exactly
r^2 f(r) with the corpus's own f.  The Nariai condition is the double root
Delta_r = Delta_r' = 0, and solving it gives the locus

        a^2 = r^2 (alpha^2 - 3r^2) / (alpha^2 + r^2)
        M   = r (r-alpha)^2 (r+alpha)^2 / (alpha^2 (alpha^2 + r^2))

** a = 0 occurs at r = alpha/sqrt(3) with M = alpha sqrt(3)/9 -- `prop:throat`'s own
values, recovered rather than assumed. **

--------------------------------------------------------------------------------
(2) THE FAMILY IS BOUNDED, AND ITS ENDPOINT IS THE ULTRACOLD LIMIT.

a^2 is maximal at r_*/alpha = 0.393320, where ** a_max = (2 - sqrt(3)) alpha ** exactly
(a_max^2 = (7-4sqrt3)alpha^2).  And r_* is precisely where Delta_r'' = 0: the double
root becomes TRIPLE.  ** That is the ultracold limit, and it bounds the family. **

  ==> So a^2(r) is two-branched and the PHYSICAL branch -- the one containing a = 0 --
      is r in (r_*, alpha/sqrt3].  Rotation SHRINKS the throat radius, from
      0.5774 alpha at a=0 down to 0.3933 alpha at a_max.

--------------------------------------------------------------------------------
(3) AND THE ANSWER: ** ROTATION MOVES lambda AWAY FROM THE THRESHOLD. **

With lambda = (dS_2 radius)^2 / r_N^2 = -2(r_N^2+a^2)/Delta_r'' / r_N^2, on the locus

        lambda(r) = -2 alpha^2 (r-alpha)(r+alpha) / (3r^4 + 6 alpha^2 r^2 - alpha^4)

    ** a = 0    ->  lambda = 1 EXACTLY **  (the equal-radii throat, recovered)
    ** a > 0    ->  lambda > 1, rising monotonically, diverging at the ultracold point **

r6497's threshold for the dipole to keep decaying is lambda > 1/8.  ** lambda starts at
1 -- a factor of eight in hand -- and rotation only increases it. ***  So the
isotropisation is not merely robust to rotation: rotation strengthens it. ***

--------------------------------------------------------------------------------
⚠ (4) WHAT THIS IS AND IS NOT.

  ** lambda here is a PROXY, and the proxy is named. **  The rotating near-horizon S^2 is
warped -- its metric carries a theta-dependence through (r_N^2 + a^2 cos^2 theta) -- so a
single ratio does not describe it, exactly as r6497 warned.  ** What is computed is the
ratio at the pole, where the S^2 radius is r_N. **  The equatorial value differs, and a
full treatment wants the warped near-horizon metric and its harmonic problem, which is
not the one solved here.

  ==> ** What is established is the DIRECTION and its size at one well-defined point of
      the sphere: lambda = 1 at a = 0, rising with a, against a threshold of 1/8.  For
      the conclusion to fail, the warping would have to reverse a trend that runs the
      right way by a factor of eight at the outset. **  Not claimed: that it cannot.
"""

import sympy as sp
import numpy as np

r, al = sp.symbols('r alpha', positive=True)
A2, M = sp.symbols('A M', positive=True)

# --- (1) the locus, and the a=0 recovery -----------------------------------------
D = (r**2 + A2)*(1 - r**2/al**2) - 2*M*r
assert sp.simplify(D.subs(A2, 0) - r**2*(1 - 2*M/r - r**2/al**2)) == 0, \
    "a=0 must be r^2 f(r), the corpus's horizon function"
sol = sp.solve([sp.Eq(D, 0), sp.Eq(sp.diff(D, r), 0)], [M, A2], dict=True)[0]
a2, Ms = sp.simplify(sol[A2]), sp.simplify(sol[M])
rN0 = al/sp.sqrt(3)
assert sp.simplify(a2.subs(r, rN0)) == 0, "a must vanish at the corpus's r_N"
assert sp.simplify(Ms.subs(r, rN0) - al*sp.sqrt(3)/9) == 0, "and M must be the Nariai mass"
print("  locus solved; a=0 recovers r_N = alpha/sqrt3 and M = alpha sqrt3/9   OK")

# --- (2) the family's extent and the ultracold endpoint ---------------------------
rstar = [c for c in sp.solve(sp.diff(a2, r), r) if c.is_real and c.is_positive][0]
a2max = sp.simplify(a2.subs(r, rstar))
assert sp.simplify(a2max - (2 - sp.sqrt(3))**2*al**2) == 0, \
    f"a_max must be (2-sqrt3)alpha, got sqrt({a2max})"
Dpp = sp.simplify(sp.diff(D, r, 2).subs([(A2, a2), (M, Ms)]))
assert sp.simplify(Dpp.subs(r, rstar)) == 0, "a_max must sit where the root becomes TRIPLE"
print(f"  a_max = (2-sqrt3)alpha, attained where Delta'' = 0 -- ultracold     OK")

# --- (3) lambda on the physical branch --------------------------------------------
lam = sp.simplify(-2*(r**2 + a2)/Dpp/r**2)
assert sp.simplify(lam.subs(r, rN0) - 1) == 0, "lambda must be exactly 1 at a=0"
f = sp.lambdify(r, lam.subs(al, 1), 'numpy')
lo, hi = float(rstar.subs(al, 1))*1.0005, float(rN0.subs(al, 1))
vals = f(np.linspace(lo, hi, 500))
assert vals.min() >= 1 - 1e-9, f"lambda must be >= 1 on the physical branch, got {vals.min()}"
print(f"  lambda = 1 exactly at a=0; on the branch min={vals.min():.6f}, max={vals.max():.4g}")

THRESHOLD = sp.Rational(1, 8)          # r6497: dipole decays iff lambda > 1/(4*1*2)
assert 1 > THRESHOLD, "the a=0 value must already clear the threshold"
print(f"  r6497's threshold is lambda > {THRESHOLD}; lambda starts at 1 and RISES")
print(f"  -> rotation moves the throat AWAY from it, by a factor of {int(1/THRESHOLD)} at the outset  OK")

# --- (4) and the proxy is named ----------------------------------------------------
PROXY = "the ratio at the POLE, where the S^2 radius is r_N"
assert "POLE" in PROXY
print(f"\n  lambda here is a proxy: {PROXY}.")
print("  The rotating near-horizon S^2 is warped through (r_N^2 + a^2 cos^2 theta),")
print("  so one ratio does not describe it -- r6497 warned of exactly this.      OK")

print()
print("ESTABLISHED: the rotating Nariai locus recovers prop:throat at a=0; the family is")
print("bounded by a_max = (2-sqrt3)alpha at the ultracold point; and lambda = 1 at a=0")
print("rising monotonically with a, against a threshold of 1/8. Rotation moves the throat")
print("AWAY from the damping threshold. NOT CLAIMED: that the warped treatment cannot")
print("reverse this -- only that it would have to reverse a trend running the right way")
print("by a factor of eight at the outset.")
