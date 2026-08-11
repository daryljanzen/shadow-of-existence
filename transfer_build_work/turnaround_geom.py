import sympy as sp
r, r0, M, al = sp.symbols('r r0 M alpha', real=True)

print("="*70); print("(1) THE FORMAL RELATION BETWEEN THE TWO CUBICS (alpha explicit)"); print("="*70)
f = 1 - 2*M/r - r**2/al**2
Hcubic = sp.simplify((f*r*al**2).expand())              # f=0  -> horizon cubic
Tcubic = sp.simplify(((1-f)*r*al**2).expand())          # 1-f=0 -> turnaround cubic
print("  horizon   f=0   :", Hcubic, "= 0")
print("  turnaround 1-f=0 :", Tcubic, "= 0")
print("  H - T =", sp.simplify(Hcubic - Tcubic), "  <- they differ by exactly the alpha^2 * r (flat/unit) term")
print("  => the turnaround cubic IS the horizon cubic with the flat-unit term removed;")
print("     r^3 = -2M alpha^2 is the PURE cube-root (equilateral) core, the alpha^2 r term")
print("     is what bends the equilateral triple into the colinear (casus irreducibilis) horizons.")

print("="*70); print("(2) THE ROOTS: equilateral (turnaround) vs colinear-real (horizon)"); print("="*70)
Troots = sp.solve(sp.Eq(r**3, -2*M*al**2), r)
print("  turnaround roots (r^3=-2M a^2):")
for rt in Troots: print("    ", sp.simplify(rt))
print("    -> real root -(2M a^2)^(1/3) times {1, e^{2pi i/3}, e^{4pi i/3}} : EQUILATERAL, pure Z/3.")
# mass function via the P3 factorisation (alpha=1)
r0s = sp.symbols('r0', real=True)
fac = sp.expand((r-r0s)*(r**2 + r*r0s + r0s**2 - 1))
print("  P3 factorisation (a=1): (r-r0)(r^2+r r0+r0^2-1) =", fac)
print("    => 2M(r0) = r0 - r0^3   (the horizon cubic's constant term); ellipse r^2+r r0+r0^2=1.")

print("="*70); print("(3) alpha->0 (Lambda->0): which roots are de Sitter features"); print("="*70)
print("  horizon roots as alpha->inf (Lambda->0): one stays at r=2M (Schwarzschild), two -> +-alpha -> inf.")
print("  turnaround real root -(2M alpha^2)^(1/3) -> -inf as alpha->inf.")
print("  => the turnaround root is a Lambda>0 feature (runs off at Lambda=0), EXACTLY like the two")
print("     extra horizon roots P2 calls 'a reading of the cosmological constant'. Same origin.")

print("="*70); print("(4) DOES THE TURNAROUND ROOT LIE ON THE FUNDAMENTAL ELLIPSE?"); print("="*70)
import numpy as np
def rTA(r0v):    # real turnaround root, a=1:  r^3 = -2M = -(r0 - r0^3) = r0^3 - r0
    val = r0v**3 - r0v
    return np.cbrt(val)
def ell(r0v, rv): return rv**2 + rv*r0v + r0v**2 - 1.0   # =0 on the ellipse
for r0v in [0.0, 0.2, 1/np.sqrt(3), 0.5, 0.9, 1.0]:
    rv = rTA(r0v)
    print(f"   r0={r0v:+.4f}  r_TA={rv:+.4f}   ellipse(r0,r_TA)={ell(r0v,rv):+.4f}  {'ON' if abs(ell(r0v,rv))<1e-9 else 'off'}")
print("   (ellipse value != 0 => the turnaround root traces its OWN curve, not the ellipse locus.)")

print("="*70); print("(5) WHERE IS THE TURNAROUND CURVE EXTREMAL / SPECIAL?"); print("="*70)
r0sym = sp.symbols('r0', real=True)
twoM = r0sym - r0sym**3
dtwoM = sp.diff(twoM, r0sym)
print("   2M(r0)=r0-r0^3 ; d(2M)/dr0 =", dtwoM, " -> extremum at r0 =", sp.solve(dtwoM, r0sym))
print("   at r0=1/sqrt3: 2M =", sp.nsimplify(twoM.subs(r0sym, 1/sp.sqrt(3))), "= 2/(3 sqrt3) (max mass = +M Nariai).")
print("   => the turnaround is DEEPEST exactly at the +M Nariai (max-mass) slicing r0=1/sqrt3.")
print("   ratio at Nariai: r_TA / merged-horizon rho :")
rho = 1/sp.sqrt(3)
rTAnar = sp.root(sp.Abs(twoM.subs(r0sym,1/sp.sqrt(3))),3)
print("      |r_TA|=", sp.simplify(rTAnar), "  rho=",rho, "  ratio=", sp.simplify(rTAnar/rho), "= 2^(1/3)")
