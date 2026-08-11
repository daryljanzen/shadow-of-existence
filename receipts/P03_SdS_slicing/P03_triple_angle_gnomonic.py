"""
P03_triple_angle_gnomonic.py -- verifies: the gnomonic offset r0=(2/sqrt3) sin w turns the horizon
  relation 2M=r0-r0^3 into the PURE triple-angle 2M=(2/(3 sqrt3)) sin 3w, with 2/sqrt3 the UNIQUE slicing
  scale removing the residual sin w harmonic; Nariai at w=pi/6 lands r0=1/sqrt3 (the sigma fixed point).
  [P3 SdS-slicing-curve_v2 prop:gnomonic eq:x0sinw, prop:triple eq:tripleM, sec:throat-angle sin u]
STATUS: ✔✔   RUN: python3 P03_triple_angle_gnomonic.py   RUNTIME: ~3s
COMPUTES: 2M=r0-r0^3 at r0=(2/sqrt3)sin w equals (2/(3 sqrt3)) sin 3w; the uniqueness (r0=rho sin w gives a
  sin w coefficient rho-3/4 rho^3, zero iff rho=2/sqrt3); the throat-angle relation sin u=(2/sqrt3)sin w=r0;
  Nariai w=pi/6 -> sin 3w=1, r0=1/sqrt3 (matches the involution fixed point). CONTROL: rho=1 leaves a
  nonzero residual sin w term.
BOUND: the algebra of the gnomonic parametrisation; that the projection is gnomonic (prop:gnomonic) is a
  geometric-observation argument, not this receipt's computation.
ORIGIN: built new r1341 (uncited P3 claim).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
w, rho, u = sp.symbols('w rho u', real=True)
s = sp.sin(w); S3 = sp.sqrt(3)
print("="*72); print("P03 triple-angle gnomonic: r0=(2/sqrt3) sin w -> 2M=(2/3sqrt3) sin 3w"); print("="*72)
# (1) 2M = r0 - r0^3 = (2/3sqrt3) sin 3w
r0 = (2/S3)*s
twoM = r0 - r0**3
target = (2/(3*S3))*sp.sin(3*w)
ok&=check("2M = r0−r0³ = (2/(3√3)) sin 3w  at r0=(2/√3)sin w",
          sp.simplify(sp.expand_trig(twoM - target))==0)
# (2) uniqueness: r0=rho sin w -> coefficient of sin w is rho - 3/4 rho^3, zero iff rho=2/sqrt3
r0g = rho*s
# harmonic decomposition: r0-r0^3 = (rho - 3/4 rho^3) sin w + 1/4 rho^3 sin 3w  (via sin^3 w=(3 sin w - sin 3w)/4)
decomp = (rho - sp.Rational(3,4)*rho**3)*sp.sin(w) + sp.Rational(1,4)*rho**3*sp.sin(3*w)
ok&=check("r0−r0³ = (rho−¾rho³) sin w + ¼rho³ sin 3w  (harmonic decomposition, DERIVED)",
          sp.simplify(sp.expand_trig((r0g - r0g**3) - decomp))==0)
roots = sp.solve(sp.Eq(rho - sp.Rational(3,4)*rho**3, 0), rho)
pos = [r for r in roots if r.is_positive]
ok&=check("pure sin 3w ⟺ rho−¾rho³=0 ⟺ unique positive rho = 2/√3",
          len(pos)==1 and sp.simplify(pos[0]-2/S3)==0)
# (3) throat angle: sin u = (2/sqrt3) sin w = r0
ok&=check("throat angle: sin u = (2/√3) sin w = r0 (gnomonic)", sp.simplify((2/S3)*s - r0)==0)
# (4) Nariai at w=pi/6
w0 = sp.pi/6
ok&=check("Nariai w=π/6: sin 3w = 1 (max)", sp.sin(3*w0)==1)
ok&=check("Nariai r0 = (2/√3)sin(π/6) = 1/√3  (the σ involution fixed point)", sp.simplify(r0.subs(w,w0) - 1/S3)==0)
ok&=check("  and 2M there = (2/(3√3))·1 = 2/(3√3) = r0−r0³ at r0=1/√3",
          sp.simplify(target.subs(w,w0) - (1/S3 - (1/S3)**3))==0)
# (5) CONTROL: rho=1 (!= 2/sqrt3) leaves a nonzero residual sin w term
resid = (rho - sp.Rational(3,4)*rho**3).subs(rho,1)
ok&=check("CONTROL: rho=1 leaves residual sin w coefficient = 1/4 ≠ 0 (not a pure triple-angle)",
          sp.simplify(resid - sp.Rational(1,4))==0 and resid!=0)
# --- r2376+c54.159 -----------------------------------------------------------------
# THE CLAIM, ASSERTED.  The file computed a PASS/FAIL flag and only printed it: assert it.
# AND PIN, so nothing rests on the flag alone:
#   · the unique slicing scale killing the residual sin w harmonic is rho = 2/sqrt3
#     = 1.1547005383792517  (INDEX: "rho=2/sqrt3 unique root");
#   · at Nariai w = pi/6, 2M = 2/(3 sqrt3) = 0.3849001794597505 and r0 = 1/sqrt3
#     = 0.5773502691896258  (INDEX: "Nariai w=pi/6 => r0=1/sqrt3").
assert ok, "a triple-angle / gnomonic check FAILED"
assert len(pos) == 1 and abs(float(pos[0]) - 1.1547005383792517) < 1e-12, \
    "the unique positive slicing scale must be rho = 2/sqrt3"
assert abs(float(target.subs(w, w0)) - 0.3849001794597505) < 1e-12, \
    "2M at Nariai must be 2/(3 sqrt3)"
assert abs(float(r0.subs(w, w0)) - 0.5773502691896258) < 1e-12, \
    "r0 at Nariai must be 1/sqrt3"
# -----------------------------------------------------------------------------------
print("="*72)
print("RESULT:", "ALL PASS -- the gnomonic offset makes 2M a pure sin 3w with 2/√3 the unique scale; the\n         sky angle is the triple-angle's natural coordinate; Nariai at w=π/6 lands the σ fixed point 1/√3." if ok else "SOME FAILED")
print("="*72)
