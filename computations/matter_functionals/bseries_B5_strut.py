"""
B-5 (P9 rem:accel caveat): no strut-free accelerating vacuum. Show the bare accelerating mass
(C-metric) carries an IRREMOVABLE conical strut on the axis whose strength is set by the
acceleration, and that the cosmological constant cannot regularise it -- so acceleration is not a
vacuum parameter; it enters on the matter side as the bend (the strut's stress-energy), exactly as
P9 sec:pd states and C9 placed as the axisymmetric class's canonical non-fluid functional.

The axis regularity of the (A)dS C-metric is governed by the ANGULAR structure function
   P(x) = (1-x^2)(1 + 2 m A x)          [Griffiths-Podolsky; A = acceleration, m = mass]
which is Lambda-INDEPENDENT (Lambda enters only the radial function Q(y)). Regularity at a pole
x_i requires the phi-period Delta_phi = 4 pi / |P'(x_i)|. Both poles regular <=> |P'(x_+)|=|P'(x_-)|.
"""
import sympy as sp
x, m, A, Lam = sp.symbols('x m A Lambda', real=True)
P = (1 - x**2)*(1 + 2*m*A*x)          # angular function (no Lambda)
Pp = sp.diff(P, x)
xn, xp = -1, 1                          # the two axis poles (north/south), roots of (1-x^2)
Pp_n = sp.simplify(Pp.subs(x, xn))      # P'(-1)
Pp_p = sp.simplify(Pp.subs(x, xp))      # P'(+1)
print("="*70); print("B-5 :: no strut-free accelerating vacuum (C-metric conical strut)"); print("="*70)
print(f"  P(x) = (1-x^2)(1+2mAx)   [Lambda-independent angular function]")
print(f"  P'(-1) = {Pp_n}      P'(+1) = {Pp_p}")
print(f"  |P'| ratio (north/south) = {sp.simplify(sp.Abs(Pp_n)/sp.Abs(Pp_p))}  -> 1 only if mA=0")

# regularise the south pole x=-1: Delta_phi = 4 pi / |P'(-1)|
dphi = 4*sp.pi/sp.Abs(Pp_n)
# conical defect at the north pole x=+1 with that period: delta = 2pi - Delta_phi |P'(+1)|/2
delta_N = sp.simplify(2*sp.pi - dphi*sp.Abs(Pp_p)/2)
print("-"*70)
print(f"  Fix the south axis (Delta_phi = 4 pi/|P'(-1)| = {sp.simplify(dphi)}):")
print(f"    residual conical defect at the NORTH axis:  delta = {delta_N}")
print(f"    (negative delta = conical EXCESS = a positive-tension STRUT along the axis)")
mu = sp.simplify(-delta_N/(8*sp.pi))    # strut tension mu = -delta/8pi
print(f"    strut tension  mu = -delta/8pi = {mu}   -> vanishes iff mA=0, grows with acceleration A")
print("-"*70)
print(f"  Lambda-dependence of the axis: dP/dLambda = {sp.diff(P,Lam)}  (P carries no Lambda)")
print("""  => the cosmological constant enters the RADIAL function Q(y), not the angular P(x); the
     conical defect is fixed by P'(x_pm), which are Lambda-free, so Lambda CANNOT regularise the
     axis. The strut is irremovable for A != 0.""")
print("="*70)
print("""VERDICT (B-5 closed): a bare accelerating mass necessarily carries a conical strut of tension
mu = mA/(1-2mA) (to this order) on one axis; the defect is set by the Lambda-independent angular
function, so no choice of Lambda (or of the phi-period) removes it. Acceleration is therefore NOT a
vacuum parameter of the substrate -- it must be sourced, and it enters on the matter side as the
bend (the strut's stress-energy, T^z_z = -rho, the conical-defect equation of state C9 collected).
This closes the P9 rem:accel 'strut-free accelerating vacuum' caveat in the negative: there is none.""")
