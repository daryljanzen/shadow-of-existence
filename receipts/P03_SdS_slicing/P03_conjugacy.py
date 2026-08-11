"""
P03_conjugacy.py -- verifies P3 prop:conjugacy, by CHECKING the closed-form conjugacy that makes the
  throat-circle reflection g1 and the cubic root-exchange sigma one involution in two coordinates:
    [P3 SdS-slicing-curve_v2 prop:conjugacy eq:chi]
    chi o g1 = sigma o chi,   with   chi(x) = (2/sqrt3) sin( (2/3) arcsin x ),
      g1(x) = sqrt(1-x^2)                         (throat-circle reflection, u <-> pi/2 - u)
      sigma(xi) = (1/2)(-xi + sqrt(4 - 3 xi^2))   (cubic root-exchange involution)
    Both sides equal (2/sqrt3) sin(pi/3 - 2a/3) with x=sin a, the identity holding in closed form; the
    collapse 4 - 3 chi(x)^2 = 4 cos^2(2a/3) that makes it closed is the forced slicing scale 2/sqrt3.
  [P3 SdS-slicing-curve_v2 -- the exact map between the two presentations of the one involution]
STATUS: ✔✔   RUN: python3 P03_conjugacy.py   RUNTIME: ~3s
COMPUTES: both compositions in the angle a=arcsin x (symbolic), the 4-3chi^2 collapse, and a numeric sweep.
CONTROL: chi is a genuine map, not the identity (chi(g1) != g1); and sigma is the involution the other
  receipt fixes -- here it is reached through chi from the throat reflection. A wrong scale (rho != 2/sqrt3)
  breaks the closed-form collapse 4-3chi^2 = 4cos^2.
BOUND: cubic_factor_ellipse_locus verifies sigma (the cubic involution) and triple_angle the throat/sky
  relation; NEITHER verifies chi or the conjugacy chi o g1 = sigma o chi. This is that map.
ORIGIN: built new (fork) -- P3 completeness re-audit finding B; prop:conjugacy was uncovered.
"""
import sympy as sp
import numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
S3 = sp.sqrt(3)
x = sp.Symbol('x', positive=True)
a = sp.Symbol('a', positive=True)          # a = arcsin x in [0, pi/2]
g1    = lambda t: sp.sqrt(1 - t**2)
sig   = lambda xi: (-xi + sp.sqrt(4 - 3*xi**2))/2
chi   = lambda t: (2/S3)*sp.sin(sp.Rational(2,3)*sp.asin(t))
print("="*74); print("P03 conjugacy -- chi o g1 = sigma o chi (closed form)"); print("="*74)

# LHS: chi(g1(x)) with x=sin a  =>  g1 = cos a = sin(pi/2 - a), arcsin(cos a)=pi/2-a on [0,pi/2]
lhs = (2/S3)*sp.sin(sp.Rational(2,3)*(sp.pi/2 - a))                 # chi(g1(sin a))
lhs_target = (2/S3)*sp.sin(sp.pi/3 - sp.Rational(2,3)*a)
ok&=check("chi(g1(x)) = (2/sqrt3) sin(pi/3 - 2a/3)   [x=sin a]", sp.simplify(lhs - lhs_target)==0)

# RHS: sigma(chi(x)) with chi(x)=(2/sqrt3) sin(2a/3); 4-3chi^2 = 4 cos^2(2a/3)
chi_x = (2/S3)*sp.sin(sp.Rational(2,3)*a)
collapse = sp.simplify(4 - 3*chi_x**2)
ok&=check("collapse: 4 - 3 chi(x)^2 = 4 cos^2(2a/3)  (what makes the conjugacy closed)",
          sp.simplify(collapse - 4*sp.cos(sp.Rational(2,3)*a)**2)==0)
# sqrt(4-3chi^2)=2 cos(2a/3) on the range; build sigma(chi_x)
sqrt_term = 2*sp.cos(sp.Rational(2,3)*a)
rhs = sp.simplify((-chi_x + sqrt_term)/2)
ok&=check("sigma(chi(x)) = cos(2a/3) - (1/sqrt3) sin(2a/3) = (2/sqrt3) sin(pi/3 - 2a/3)",
          sp.simplify(rhs - lhs_target)==0)

# the identity itself
ok&=check("=> chi o g1 = sigma o chi  (both = (2/sqrt3) sin(pi/3 - 2a/3))", sp.simplify(lhs - rhs)==0)

# numeric sweep over x in (0,1), independent of the symbolic route
def g1n(t): return np.sqrt(1-t*t)
def sign(xi): return 0.5*(-xi + np.sqrt(4-3*xi*xi))
def chin(t): return (2/np.sqrt(3))*np.sin((2/3)*np.arcsin(t))
ok&=check("numeric: |chi(g1(x)) - sigma(chi(x))| < 1e-12 over x in [0.05..0.95]",
          all(abs(chin(g1n(t)) - sign(chin(t))) < 1e-12 for t in np.linspace(0.05,0.95,19)))

# CONTROLS
ok&=check("CONTROL: chi is not the identity (chi(0.5) != 0.5)", abs(chin(0.5)-0.5) > 1e-3)
ok&=check("CONTROL: a wrong scale rho=1 breaks the closed collapse (4-3(sin(2a/3))^2 != 4cos^2(2a/3))",
          sp.simplify((4 - 3*sp.sin(sp.Rational(2,3)*a)**2) - 4*sp.cos(sp.Rational(2,3)*a)**2)!=0)

# r2376+c54.159 -- (a) the receipt's own PASS/FAIL flag, which was only printed; and (b) an
# INDEPENDENT pin of prop:conjugacy at a named point, so the file does not rest on the flag alone.
# At x = 1/2 (a = pi/6): chi(1/2) = (2/sqrt3) sin(pi/9) = 0.3949308436, and BOTH sides of the
# conjugacy land on chi(g1(1/2)) = sigma(chi(1/2)) = (2/sqrt3) sin(2 pi/9) = 0.7422271990.
# Symbolically the two compositions are the SAME closed form, exactly; and the closing collapse
# forces the scale 2/sqrt3 = 1.1547005384 -- sigma's fixed point is 1/sqrt3 = 0.5773502692.
assert ok, "P03_conjugacy: a check() line FAILED -- see the PASS/FAIL column above"
assert abs(chin(0.5) - 0.3949308436) < 1e-9, chin(0.5)
assert abs(chin(g1n(0.5)) - 0.7422271990) < 1e-9, chin(g1n(0.5))
assert abs(sign(chin(0.5)) - 0.7422271990) < 1e-9, sign(chin(0.5))
assert sp.simplify(lhs - rhs) == 0            # exact symbolic zero: the conjugacy, in closed form
assert abs(float(2/S3) - 1.1547005384) < 1e-9            # the scale the collapse forces
assert abs(sign(1/np.sqrt(3)) - 0.5773502692) < 1e-9, sign(1/np.sqrt(3))   # sigma's Nariai fixed pt

print("="*74)
print("RESULT:", "ALL PASS -- chi(x)=(2/sqrt3)sin(2/3 arcsin x) conjugates the throat reflection g1 and the\n"
      "         cubic involution sigma: chi o g1 = sigma o chi, both (2/sqrt3)sin(pi/3-2a/3); the closing\n"
      "         collapse 4-3chi^2=4cos^2(2a/3) is the forced 2/sqrt3 scale. The two involutions are one."
      if ok else "SOME FAILED")
print("="*74)
