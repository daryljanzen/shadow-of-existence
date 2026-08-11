"""
P03_ellipse_foci.py -- verifies P3 sec:ellipse's foci computation (L336), by DERIVING the foci of the
  horizon-locus ellipse and showing they coincide with the Nariai offset the closed slicing runs out onto:
    [P3 SdS-slicing-curve_v2 sec:ellipse L336]
    (i)   ellipse r^2 + r r0 + r0^2 = 1 has quadratic-form matrix [[1,1/2],[1/2,1]], eigenvalues 1/2, 3/2,
          so semi-axes a=sqrt2 (major, anti-diagonal r=-r0) and b=sqrt(2/3) (minor, diagonal r=r0);
    (ii)  focal distance c = sqrt(a^2 - b^2) = sqrt(2 - 2/3) = 2/sqrt3 -- the foci lie on the backward-radial
          major axis at value 2/sqrt3;
    (iii) 2/sqrt3 IS the Nariai offset: the extreme r0 on the ellipse (from the discriminant 4-3 r0^2 >= 0,
          i.e. real r requires |r0| <= 2/sqrt3), the lone backward-radial root the closed slicing closes on;
    (iv)  and, for the equilateral axis ratio a/b = sqrt3 ALONE, c = sqrt(a^2-b^2) equals the r0-half-width
          sqrt((a^2+b^2)/2) -- both 2/sqrt3 -- so the metric foci and the root the curve closes on are one scale;
    (v)   in the sky angle w (r0=(2/sqrt3) sin w) the foci fall at w=pi/4, the exact bisector of the Nariai
          crest w=pi/6 and the throat-tangent extreme w=pi/3.
  [P3 SdS-slicing-curve_v2 -- the ellipse foci coincide with the Nariai offset, forced by a/b=sqrt3]
STATUS: ✔✔   RUN: python3 P03_ellipse_foci.py   RUNTIME: ~3s
COMPUTES: eigenvalues -> semi-axes -> focal distance; the extreme r0 from the discriminant; the a/b=sqrt3
  <=> c = r0-half-width equivalence; the w=pi/4 bisector.
CONTROL: a NON-equilateral ellipse (a/b != sqrt3) has c != r0-half-width -- the coincidence is the equilateral
  signature, not generic. (Break the cross-term off 1 and the axis ratio, hence the coincidence, moves.)
BOUND: cubic_factor_ellipse_locus verifies the ellipse eigenstructure and semi-axes; it does NOT compute the
  foci, the c=2/sqrt3=Nariai-offset coincidence, or the a/b=sqrt3 equivalence. This is that computation.
ORIGIN: built new (fork) -- P3 completeness re-audit finding C; the ellipse foci were uncovered.
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r, r0 = sp.symbols('r r0', real=True)
print("="*74); print("P03 ellipse foci -- foci at 2/sqrt3 = the Nariai offset (forced by a/b=sqrt3)"); print("="*74)

# (i) eigenstructure -> semi-axes
Mx = sp.Matrix([[1, sp.Rational(1,2)],[sp.Rational(1,2), 1]])
evs = sorted(Mx.eigenvals().keys())                      # 1/2, 3/2
ok&=check("quadratic-form eigenvalues = 1/2, 3/2", evs==[sp.Rational(1,2), sp.Rational(3,2)])
a = sp.sqrt(1/sp.Rational(1,2))                          # major semi-axis (smaller eigenvalue 1/2)
b = sp.sqrt(1/sp.Rational(3,2))                          # minor semi-axis (larger eigenvalue 3/2)
ok&=check("semi-axes a=sqrt2 (major, anti-diagonal), b=sqrt(2/3) (minor, diagonal)",
          sp.simplify(a-sp.sqrt(2))==0 and sp.simplify(b-sp.sqrt(sp.Rational(2,3)))==0)

# (ii) focal distance
c = sp.sqrt(a**2 - b**2)
ok&=check("focal distance c = sqrt(a^2 - b^2) = sqrt(2 - 2/3) = 2/sqrt3",
          sp.simplify(c - 2/sp.sqrt(3))==0)

# (iii) the extreme r0 on the ellipse = the Nariai offset (from the discriminant of r^2+r0 r+(r0^2-1)=0)
disc = sp.discriminant(sp.Poly(r**2 + r0*r + (r0**2 - 1), r), r)   # = 4 - 3 r0^2
ok&=check("real r on the ellipse requires disc = 4 - 3 r0^2 >= 0, i.e. |r0| <= 2/sqrt3 (the Nariai offset)",
          sp.simplify(disc - (4 - 3*r0**2))==0 and sp.simplify(sp.solve(sp.Eq(disc,0), r0)[1] - 2/sp.sqrt(3))==0)
ok&=check("=> focal distance c = 2/sqrt3 EQUALS the Nariai offset (extreme r0)", sp.simplify(c - 2/sp.sqrt(3))==0)

# (iv) the a/b=sqrt3 equivalence: c = sqrt(a^2-b^2) equals the r0-half-width sqrt((a^2+b^2)/2)
r0_halfwidth = sp.sqrt((a**2 + b**2)/2)
ok&=check("r0-half-width sqrt((a^2+b^2)/2) = 2/sqrt3", sp.simplify(r0_halfwidth - 2/sp.sqrt(3))==0)
ok&=check("axis ratio a/b = sqrt3 (the equilateral signature)", sp.simplify(a/b - sp.sqrt(3))==0)
# symbolic equivalence: sqrt(a^2-b^2)=sqrt((a^2+b^2)/2)  <=>  a^2 = 3 b^2  <=>  a/b=sqrt3
A, B = sp.symbols('A B', positive=True)                  # A=a^2, B=b^2
ok&=check("c = r0-half-width  <=>  a^2 = 3 b^2  <=>  a/b = sqrt3  (equivalence, general)",
          sp.simplify(sp.solve(sp.Eq(A - B, (A + B)/2), A)[0] - 3*B)==0)

# (v) sky-angle: foci at w=pi/4, the bisector of Nariai (pi/6) and throat-tangent (pi/3)
ok&=check("w=pi/4 is the exact bisector of Nariai w=pi/6 and throat-tangent w=pi/3",
          sp.simplify((sp.pi/6 + sp.pi/3)/2 - sp.pi/4)==0)

# CONTROL: a non-equilateral ellipse (cross-term != 1, so a/b != sqrt3) breaks c = r0-half-width
Mx2 = sp.Matrix([[1, sp.Rational(1,4)],[sp.Rational(1,4), 1]])   # cross-term 1/2 instead of 1 in r^2+ (1/2)r r0..
e2 = sorted(Mx2.eigenvals().keys())                       # 3/4, 5/4
a2, b2 = sp.sqrt(1/e2[0]), sp.sqrt(1/e2[1])
ok&=check("CONTROL: non-equilateral (a/b != sqrt3) => c != r0-half-width",
          sp.simplify(a2/b2 - sp.sqrt(3))!=0 and sp.simplify(sp.sqrt(a2**2-b2**2) - sp.sqrt((a2**2+b2**2)/2))!=0)

print("="*74)
print("RESULT:", "ALL PASS -- the horizon-locus ellipse (semi-axes sqrt2, sqrt(2/3)) has focal distance\n"
      "         c=sqrt(a^2-b^2)=2/sqrt3, which IS the Nariai offset (extreme r0 the curve closes on); and for\n"
      "         the equilateral ratio a/b=sqrt3 alone, c equals the r0-half-width sqrt((a^2+b^2)/2). Not a\n"
      "         coincidence of the number -- the equilateral signature."
      if ok else "SOME FAILED")
print("="*74)

# --- r2376+c54.159 -----------------------------------------------------------------
# The file computed a PASS/FAIL flag and only PRINTED it.  Assert the flag, and pin the
# numbers the claim rests on so the receipt does not rest on `ok`'s coverage alone:
# semi-axes a=sqrt2, b=sqrt(2/3); focal distance c = 2/sqrt3 = 1.1547005383792515,
# which is the Nariai offset and equals the r0-half-width (the a/b=sqrt3 signature).
assert ok, "P03_ellipse_foci: a check FAILED"
assert [float(e) for e in evs] == [0.5, 1.5]
assert abs(float(a) - 1.4142135623730951) < 1e-12
assert abs(float(b) - 0.816496580927726) < 1e-12
assert abs(float(c) - 1.1547005383792515) < 1e-12          # c = 2/sqrt3, the Nariai offset
assert abs(float(r0_halfwidth) - 1.1547005383792515) < 1e-12
assert sp.simplify(c - r0_halfwidth) == 0                  # equal EXACTLY, not just numerically
assert sp.simplify(disc - (4 - 3*r0**2)) == 0              # the discriminant that fixes 2/sqrt3
