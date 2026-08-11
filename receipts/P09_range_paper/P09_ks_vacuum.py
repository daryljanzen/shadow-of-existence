"""
P09_ks_vacuum.py -- verifies prop:ksvac: the vacuum kernel (T_munu=0) of the Kantowski-Sachs cut
  ds^2=-dtau^2+X(tau)^2 dchi^2+Y(tau)^2 dOmega^2 is the Schwarzschild-de Sitter INTERIOR: Y=r(tau),
  X=sqrt(-f), with (dr/dtau)^2=-f and f=1-2M/r-Lambda r^2/3. By direct substitution the KS stress-energy
  8pi rho = -L+(Y'/Y)^2+1/Y^2+2(X'/X)(Y'/Y), 8pi p_chi=L-2Y''/Y-(Y'/Y)^2-1/Y^2,
  8pi p_perp=L-Y''/Y-X''/X-(X'/X)(Y'/Y) all VANISH. So SdS is the vacuum member of the homogeneous
  (KS) class -- the anisotropic form the framework paper reads the SdS cosmology as carrying.
  [P9 range_paper sec:homog / prop:ksvac]
STATUS: ✔✔   RUN: python3 P09_ks_vacuum.py   RUNTIME: ~3s
COMPUTES: from (dr/dtau)^2=-f: Y'/Y=sqrt(-f)/r, Y''=-f'/2, X'/X=(-f'/2)/sqrt(-f), X''/X=-f''/2; substituting
  into the three stress-energy expressions gives rho=p_chi=p_perp=0 (symbolic). CONTROL: X=const (not the
  SdS relation) gives nonzero pressure -- the vacuum kernel is specifically the SdS interior.
ORIGIN: built new r1369 (P9 cited no receipts; prop:ksvac was an uncovered "direct substitution").
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r,M,Lam=sp.symbols('r M Lambda', positive=True)
f=1-2*M/r-Lam*r**2/3; fp=sp.diff(f,r); fpp=sp.diff(f,r,2)
print("="*70); print("P09 KS vacuum kernel = the Schwarzschild-de Sitter interior"); print("="*70)
# SdS interior derivatives (from (dr/dtau)^2 = -f), expressed via r and f
sqrtnf=sp.sqrt(-f)
YpY = sqrtnf/r                    # Y'/Y
YppY = (-fp/2)/r                 # Y''/Y  (Y''=-f'/2, Y=r)
XpX = (-fp/2)/sqrtnf             # X'/X
XppX = -fpp/2                    # X''/X
# verify the substitution relations hold from (dr/dtau)^2=-f (Y=r, Y'=sqrt(-f))
ok&=check("from (dr/dtau)^2=-f: Y'=sqrt(-f) so Y'/Y=sqrt(-f)/r; Y''=-f'/2 (chain rule)",
          sp.simplify(YpY - sqrtnf/r)==0 and sp.simplify((-fp/2) - sp.diff(sqrtnf,r)*sqrtnf)==0)  # Y''=(d/dr sqrt(-f))*Y' = -f'/2
# the three stress-energy components (times 8pi)
rho   = sp.simplify(-Lam + YpY**2 + 1/r**2 + 2*XpX*YpY)
p_chi = sp.simplify( Lam - 2*YppY - YpY**2 - 1/r**2)
p_prp = sp.simplify( Lam - YppY - XppX - XpX*YpY)
ok&=check("8pi rho = -L+(Y'/Y)^2+1/Y^2+2(X'/X)(Y'/Y) = 0  (vacuum)", rho==0)
ok&=check("8pi p_chi = L-2Y''/Y-(Y'/Y)^2-1/Y^2 = 0  (vacuum)", p_chi==0)
ok&=check("8pi p_perp = L-Y''/Y-X''/X-(X'/X)(Y'/Y) = 0  (vacuum)", p_prp==0)
# CONTROL: X=const (X'/X=X''/X=0), Y=r still -> pressure no longer vanishes
XpX0, XppX0 = sp.Integer(0), sp.Integer(0)
p_prp_ctrl = sp.simplify(Lam - YppY - XppX0 - XpX0*YpY)
ok&=check("CONTROL: X=const (breaks X=sqrt(-f)) -> 8pi p_perp = L - Y''/Y != 0 (not vacuum)", p_prp_ctrl!=0)
print("="*70)
print("RESULT:", "ALL PASS -- the KS vacuum kernel is exactly the SdS interior (Y=r, X=sqrt(-f), (dr/dtau)^2=-f):\n         rho=p_chi=p_perp=0. SdS is the vacuum member of the homogeneous anisotropic (Kantowski-Sachs) class." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   THE THREE COMPONENTS ARE EXACTLY ZERO, not small: symbolic identities, so assert them as such.
assert rho == 0 and p_chi == 0 and p_prp == 0, (rho, p_chi, p_prp)
#   AND THE CONTROL HAS A VALUE, which is what makes the kernel SPECIFICALLY the SdS interior:
#   with X held constant, 8 pi p_perp = Lambda - Y''/Y = 2 Lambda/3 + M/r^3, so at Lambda = 3/10,
#   M = 1, r = 2 the perpendicular pressure is 13/40 = 0.325 and the cut is not vacuum.
assert sp.simplify(p_prp_ctrl - (2*Lam/3 + M/r**3)) == 0, p_prp_ctrl
_ctrl = float(p_prp_ctrl.subs({Lam: sp.Rational(3, 10), M: sp.Integer(1), r: sp.Integer(2)}))
assert abs(_ctrl - 0.325) < 1e-12, _ctrl
#   the SdS profile itself: f(r) = 1 - 2M/r - Lambda r^2/3 is negative inside the horizon, which is
#   what makes X = sqrt(-f) real there -- at Lambda = 3/10, M = 1, r = 1 it is f = -1.1.
_f = float(f.subs({Lam: sp.Rational(3, 10), M: sp.Integer(1), r: sp.Integer(1)}))
assert abs(_f - (-1.1)) < 1e-12, _f
assert _f < 0.0
