"""Q5 — the pencil premise, tested.  Horizon cubic r^3 - r + 2M, with 2M = r0 - r0^3."""
import numpy as np, sympy as sp
r, r0, M = sp.symbols('r r0 M', real=True)

print("="*78); print("Q5 — IS THE HORIZON LOCUS A PENCIL?  Tested against what the corpus already has."); print("="*78)

cubic = r**3 - r + (r0 - r0**3)
fact  = sp.factor(cubic)
print("\nSTEP 1 — the factorisation, verified symbolically:")
print("   r^3 - r + 2M   with 2M = r0 - r0^3   =  ", fact)
line = r - r0
conic = r**2 + r*r0 + r0**2 - 1
print("   line x conic  =", sp.expand(line*conic), "  matches:", sp.simplify(sp.expand(line*conic) - cubic)==0)

print("\nSTEP 2 — IS IT A PENCIL?  A pencil is a ONE-PARAMETER FAMILY  lambda*C1 + mu*C2.")
print("   Here the locus is ONE cubic curve in the (r0,r)-plane that is REDUCIBLE:")
print("   a LINE union a CONIC.  That is a degenerate member of the space of cubics,")
print("   not a pencil.  => THE PENCIL PREMISE IS WRONG AS STATED.")

print("\nSTEP 3 — but a REDUCIBLE plane cubic has its own classical theory, and its")
print("   SINGULAR POINTS are where the components meet.  Solve line = conic = 0:")
sol = sp.solve([line, conic], [r, r0], dict=True)
print("   line ∩ conic :", sol)
print("\n   Substituting r = r0 into the conic:  3 r0^2 = 1  =>  r0 = ±1/sqrt(3) =", float(1/np.sqrt(3)))

print("\nSTEP 4 — and what IS r0 = ±1/sqrt(3)?")
print("   The corpus: sigma(r0) = (-r0 + sqrt(4-3r0^2))/2 has its FIXED POINT at r0 = 1/sqrt3,")
print("   which is NARIAI.  Check the cubic has a double root there:")
for val in [sp.Rational(1,1)/sp.sqrt(3), -sp.Rational(1,1)/sp.sqrt(3)]:
    c = sp.expand(cubic.subs(r0, val))
    roots = sp.solve(sp.Eq(c,0), r)
    disc = sp.discriminant(sp.Poly(c, r))
    print(f"   r0 = {sp.nsimplify(val)} :  roots = {[sp.nsimplify(x) for x in roots]}   discriminant = {sp.simplify(disc)}")
# --- r2376+c54.159 -----------------------------------------------------------------
# THE CLAIM, ASSERTED.  (a) the locus is REDUCIBLE: line x conic = the cubic, exactly --
# an exact symbolic zero, which is what "not a pencil but one degenerate cubic" rests on.
# (b) the singular points -- line n conic -- are the TWO Nariai configurations
#     r0 = +-1/sqrt3 = +-0.5773502691896258 (INDEX: "3r0^2=1 => r0=+-1/sqrt3").
# (c) at the last of them (r0 = -1/sqrt3) the cubic's roots are the mirror of INDEX's
#     quoted triple (-2/sqrt3, 1/sqrt3, 1/sqrt3): here (2/sqrt3, -1/sqrt3, -1/sqrt3)
#     = (1.1547005383792517, -0.5773502691896258 twice), and the discriminant is EXACTLY 0.
assert sp.simplify(sp.expand(line*conic) - cubic) == 0, \
    "the horizon cubic must factor as (r - r0)(r^2 + r r0 + r0^2 - 1)"
_sing = sorted(float(s[r0]) for s in sol)
assert len(sol) == 2 and abs(_sing[0] + 0.5773502691896258) < 1e-12 \
    and abs(_sing[1] - 0.5773502691896258) < 1e-12, \
    "line n conic must be exactly the two Nariai points r0 = +-1/sqrt3"
assert all(sp.simplify(s[r] - s[r0]) == 0 for s in sol), \
    "the singular points must lie on the line component r = r0"
assert sp.simplify(disc) == 0, "the cubic's discriminant must vanish at Nariai"
_rts = sorted((complex(sp.N(x)) for x in roots), key=lambda z: z.real)
assert len(roots) == 3 and all(abs(z.imag) < 1e-12 for z in _rts), \
    "the horizon roots at Nariai must all be real"
assert abs(_rts[0].real + 0.5773502691896258) < 1e-12 \
    and abs(_rts[1].real + 0.5773502691896258) < 1e-12 \
    and abs(_rts[2].real - 1.1547005383792517) < 1e-12, \
    "at r0 = -1/sqrt3 the roots must be the DOUBLE -1/sqrt3 and the lone 2/sqrt3"
# -----------------------------------------------------------------------------------
print("\n" + "="*78)
print("RESULT: the horizon locus is NOT a pencil -- it is a REDUCIBLE plane cubic,")
print("  line (r = r0)  union  conic (r^2 + r.r0 + r0^2 = 1).")
print("  AND ITS TWO SINGULAR POINTS -- where the line meets the conic -- ARE EXACTLY")
print("  THE TWO NARIAI CONFIGURATIONS, r0 = +-1/sqrt(3), where the cubic's discriminant")
print("  vanishes and two horizon roots merge.")
print("="*78)

print("\n" + "="*78)
print("STEP 5 — WHAT P3 COMPUTED BUT DID NOT DRAW.")
print("="*78)
print("  prop:locus's proof: the quadratic form has eigenvalues 1/2 and 3/2, eigenvectors")
print("  (1,-1) and (1,1); the LARGER eigenvalue 3/2 gives the SHORTER semi-axis sqrt(2/3)")
print("  ALONG THE DIAGONAL r = r0.")
print("\n  But the diagonal r = r0 IS the locus's LINE COMPONENT.  So:")
import numpy as np
semi = np.sqrt(2/3)
pt = semi*np.array([1,1])/np.sqrt(2)
print(f"   endpoint of the minor semi-axis = sqrt(2/3) * (1,1)/sqrt2 = ({pt[0]:.10f}, {pt[1]:.10f})")
print(f"   1/sqrt(3)                                                 =  {1/np.sqrt(3):.10f}")
print(f"   equal: {abs(pt[0]-1/np.sqrt(3))<1e-12 and abs(pt[1]-1/np.sqrt(3))<1e-12}")
# --- r2376+c54.159 -----------------------------------------------------------------
# THE METRIC CHARACTERISATION, ASSERTED.  INDEX: "checks that sqrt(2/3) (1,1)/sqrt2 =
# (1/sqrt3, 1/sqrt3) -- the minor-axis endpoint P3's own proof computes."  Both components
# of the endpoint must be 1/sqrt3 = 0.5773502691896258, which is the Nariai r0 pinned above.
assert abs(pt[0] - 0.5773502691896258) < 1e-12 and abs(pt[1] - 0.5773502691896258) < 1e-12, \
    "the ellipse's minor semi-axis endpoint must be (1/sqrt3, 1/sqrt3), the Nariai point"
# -----------------------------------------------------------------------------------
print("\n  => THE TWO NARIAI CONFIGURATIONS ARE THE ENDPOINTS OF THE FUNDAMENTAL ELLIPSE'S")
print("     MINOR AXIS, and the locus's line component IS that minor axis.")
print("\n  Three characterisations of one point, and the corpus states only the first:")
print("     (i)  ALGEBRAIC : the cubic's double root; the fixed point of sigma.        [in P3]")
print("     (ii) INCIDENCE : where the locus's line component meets its conic          [NEW]")
print("                      component -- the reducible cubic's SINGULAR POINT.")
print("     (iii) METRIC   : the endpoint of the ellipse's minor semi-axis, sqrt(2/3). [NEW,")
print("                      and P3 computes sqrt(2/3) in prop:locus's own proof.]")
print("="*78)
