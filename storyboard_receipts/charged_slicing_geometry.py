"""
charged_slicing_geometry.py  --  GEOMETRIC-LEVEL receipt for P3 (SdS-slicing-curve).

P3 builds the vacuum slicing curve dr/dl=sqrt|f|, f = 1 - 2M/r - r^2/alpha^2,
and shows (sec:two-readings) that the backward-radial reading-swap R (r->-r,
equivalently the mass-reflection r0->-r0 / 2M->-2M) splits f into
    R-even = (1 - r^2/alpha^2)   the INVARIANT de Sitter geometry
    R-odd  = (-2M/r)             the PERSPECTIVAL Schwarzschild mass (a turning
                                 point, not a coefficient; sec:mass).
Question this receipt settles at the geometric level: when charge is added
(RN-dS), does the charge term sit with the perspectival mass (R-odd) or with
the invariant geometry (R-even)?  And what does charge conjugation do to the
slicing CURVE itself?

Everything below is computed.
"""
import sympy as sp

r, M, Q, alpha = sp.symbols('r M Q alpha', positive=True)
twoM = sp.symbols('twoM', real=True)
Lam = 3/alpha**2

# --- charged (Reissner-Nordstrom-de Sitter) slicing function ---
f = 1 - twoM/r + Q**2/r**2 - r**2/alpha**2
print("charged f(r) =", f)

print("\n(1) Reading-swap eigenspaces, R as the areal backward-radial reflection r->-r")
fr = f.subs(r, -r)
even = sp.simplify((f+fr)/2); odd = sp.simplify((f-fr)/2)
print("   R-even part :", even)
print("   R-odd  part :", odd)
assert sp.simplify(even - (1 + Q**2/r**2 - r**2/alpha**2)) == 0
assert sp.simplify(odd - (-twoM/r)) == 0
print("   => de Sitter geometry AND charge Q^2/r^2 are R-EVEN; mass is R-ODD.")

print("\n(2) Reading-swap as the mass-reflection r0->-r0  (2M->-2M), R's corpus form")
fR = f.subs(twoM, -twoM)
evenR = sp.simplify((f+fR)/2); oddR = sp.simplify((f-fR)/2)
print("   R-even part :", evenR, "  (mass-independent: dS + charge)")
print("   R-odd  part :", oddR,  "  (the mass)")
assert sp.simplify(evenR - (1 + Q**2/r**2 - r**2/alpha**2)) == 0
assert sp.simplify(oddR - (-twoM/r)) == 0
print("   => same split. Charge is R-EVEN under BOTH readings of R: it is")
print("      reading-swap-NEUTRAL, sitting with the invariant geometry, NOT")
print("      perspectival like the mass. (But it is still a matter-side bend:")
print("      m(r)=M-Q^2/2r, m'(r)=Q^2/2r^2 -- an R-even bend, field-level.)")

print("\n(3) What charge conjugation Q->-Q does to the slicing CURVE")
print("   f(Q->-Q) - f(Q) =", sp.simplify(f.subs(Q,-Q) - f))
assert sp.simplify(f.subs(Q,-Q) - f) == 0
print("   => IDENTICALLY zero: the two charge signs trace the SAME curve.")
print("      Charge conjugation is geometrically invisible on the slicing curve;")
print("      the sign lives in the Maxwell potential A=-(Q/r)dt (linear in Q),")
print("      off the curve -- the geometric face of 'C is field-level'.")

print("\n(4) Horizon (turning-point) structure: r^2 f = 0  ->  quartic")
quartic = sp.expand(r**2 * f.subs(twoM, 2*M))   # -r^4/alpha^2 + r^2 - 2M r + Q^2
print("   r^2 f =", quartic)
print("   Q enters only as +Q^2 => horizons are even in Q (Q->-Q fixes every")
print("   turning point); charge shifts the turning points R-evenly.")

print("\n(5) HONEST SCOPE: what charge does to the r=0 lap of the vacuum curve")
# vacuum: f ~ -2M/r -> -inf as r->0+ (curve laps THROUGH r=0, the branch point).
# charged: Q^2/r^2 dominates -> +inf.
lim_vac = sp.limit((1 - twoM/r - r**2/alpha**2), r, 0, '+')
lim_chg = sp.limit(f, r, 0, '+')
print("   vacuum  f(r->0+) =", lim_vac, "  (mass term dominates; r=0 the branch point, the lap/cosmogenesis)")
print("   charged f(r->0+) =", lim_chg, "  (Q^2/r^2 dominates: f->+inf)")
print("   => with Q!=0 the charge term changes the r->0 behaviour: an inner")
print("      (Cauchy) horizon appears and r=0 is a timelike RN singularity, so")
print("      the vacuum lap-through-r=0 (the closed bead) is a GENUINE extension,")
print("      not automatic. The PARITY result (mass R-odd, charge R-even, C the")
print("      even Q-degeneracy) is robust at the level of f and its turning")
print("      points; the full charged closed-loop is the deferred extension")
print("      P3 already flags (sec open, 'adding further charges').")

# exhibit the three-positive-horizon (inner/Cauchy, event, cosmological) RN-dS regime
import numpy as np
al=1.0
found=None
for Mv in np.linspace(0.02,0.30,29):
    for Qv in np.linspace(0.02,0.30,29):
        coeffs=[-1/al**2, 0, 1, -2*Mv, Qv**2]   # -r^4/a^2 + r^2 - 2M r + Q^2
        roots=np.roots(coeffs)
        posreal=sorted([x.real for x in roots if abs(x.imag)<1e-9 and x.real>0])
        if len(posreal)==3:
            found=(round(Mv,3),round(Qv,3),np.round(posreal,4)); break
    if found: break
print("   three-horizon RN-dS sample (M,Q,a=1):", found[0], found[1],
      " positive horizons =", found[2], "-> Cauchy(inner), event, cosmological")
assert found and len(found[2])==3, "expected a 3-horizon regime to exist"

print("\nVERDICT: at the geometric level, mass is the R-ODD (perspectival) matter")
print("datum and charge the R-EVEN (reading-swap-neutral) matter datum; charge")
print("conjugation Q->-Q leaves the slicing curve identical (field-level sign),")
print("its full antilinear C field-level. The charged closed-loop is a flagged")
print("extension; the parity structure is not -- it is exact on f. ALL CHECKS PASS.")
