"""
P14_the_d5_world.py -- P14 sec:whichthree (the dimension paragraph): the $D=5$ collapse is not
the same KIND of collapse as $D=4$'s, and the difference strengthens this paper's dimension
argument by one deliverable it does not currently claim.

WHAT PROMPTED IT.  A standing lead observed that "a four-generation, chirality-free world is a
real object the construction describes -- a discriminator source, and nobody has looked at it."

WHAT IS ESTABLISHED.
  1. THE TWO COLLAPSES, DONE SIDE BY SIDE.  With $2M=r_0^{D-3}-r_0^{D-1}$ in the gauge
     $\alpha=1$: at $D=4$ with scale $2/\sqrt3$, $2M=\tfrac{2}{3\sqrt3}\sin 3w$ -- ** a PURE
     multiple angle, zero mean **; at $D=5$ with scale $1$, $2M=\tfrac18(1-\cos 4w)$ -- ** one
     harmonic PLUS A CONSTANT **.  The DC terms are computed and asserted: zero at four,
     $\tfrac18$ at five.
  2. ** BOTH QUALIFY AS "single-harmonic" IN THE SENSE THIS PAPER USES -- only one non-constant
     harmonic survives -- BUT WHAT THEY COLLAPSE TO IS A DIFFERENT SHAPE, AND THAT HAS NOT BEEN
     RECORDED. **
  3. THE PARITY, RECOMPUTED AND TABULATED FOR $D=4,5,6,7$: the mass function is ODD in $r_0$
     exactly in EVEN $D$, confirming this paper's statement.  At $D=5$ it is even, so the offset
     parity FIXES each geometry rather than exchanging it with a conjugate.
  4. ** WHAT THE CONSTANT COSTS: at $D=5$ the mass NEVER CHANGES SIGN, $2M=\tfrac18(1-\cos4w)
     \ge 0$, touching zero only where $\cos4w=1$; at $D=4$ it changes sign across the dial, and
     that sign change is the whole of the mass-reflection structure. **
  5. ** SO THE CONSTANT AND THE PARITY ARE ONE FACT SEEN TWICE.  An even mass function cannot
     change sign about $r_0=0$; a harmonic-plus-DC bounded below by zero cannot either.  The DC
     term IS the parity obstruction, read in the angle variable rather than in the offset. **
  6. ** AND THAT IS WHAT REMOVES THE DIAL AT FIVE, NOT MERELY THE CHIRALITY.  The twelve
     designations rest on a hexad built from a fundamental and its ANTIfundamental exchanged by
     the mass reflection; with no sign change there is no antifundamental, hence no hexad, hence
     no twelve. **

** THE STRENGTHENING THIS OFFERS, AND IT IS ONE DELIVERABLE RATHER THAN A NEW ARGUMENT.  This
paper excludes $D=5$ because it "would carry four generations and no handedness".  The same
computation shows five carries NO ANTIMATTER either, at the geometric level: the parity whose
absence removes $\gamma^5$ is the same one whose absence removes the antifundamental.  One fact,
two deliverables, and only one of them is currently claimed. **

** AND WHY IT IS A DISCRIMINATOR, which is what the lead was after: $D=5$ is a world the
construction FULLY DESCRIBES and that is manifestly not ours, and the feature distinguishing it
is not a tuned number but a PARITY -- an evenness condition on an exponent.  A programme that
selected four by fitting would have no reason for five to fail in so structured a way. **

** SCOPE, INHERITED AND NOT WEAKENED: the $D$-dimensional metric function is taken to be the
standard Tangherlini--de Sitter one, an extension of the operator rather than a rederivation at
general $D$, exactly as this paper states. **

ORIGIN: computations/baryon_edge/L006w_the_d5_fourfold.py -- built r2376 (c54.74); edit the
origin, not this copy."""
import sympy as sp

print(__doc__.split("Run:")[0])

r0, w, D = sp.symbols('r_0 w D', real=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE MASS FUNCTION AT GENERAL D, AND THE TWO COLLAPSES")
print("=" * 78)
print("  P14: in the gauge alpha = 1, the D-dimensional Schwarzschild--de Sitter mass is the")
print("  slicing-dependent factor")
print()
print("     2M = r_0^(D-3) - r_0^(D-1)")
print()


def twoM(Dv):
    return sp.expand(r0**(Dv - 3) - r0**(Dv - 1))


for Dv in (4, 5, 6):
    print(f"     D = {Dv}:   2M = {twoM(Dv)}      powers present: "
          f"{sorted(sp.Poly(twoM(Dv), r0).monoms())}")
print()
print("  The collapse asks: is there a scale c such that r_0 = c sin w turns 2M into a SINGLE")
print("  harmonic?  P14: 'the slicing scale 2/sqrt3 is the one scale removing the residual")
print("  harmonic', available at D = 4 and D = 5 and no higher.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TWO COLLAPSES, DONE")
print("=" * 78)
res = {}
for Dv, c in ((4, 2/sp.sqrt(3)), (5, sp.Integer(1))):
    expr = sp.simplify(twoM(Dv).subs(r0, c*sp.sin(w)))
    fs = sp.simplify(sp.expand_trig(sp.simplify(sp.fu(expr))))
    fs = sp.simplify(sp.trigsimp(sp.expand(sp.simplify(expr.rewrite(sp.cos)))))
    # get the Fourier content directly
    ser = sp.simplify(sp.expand(sp.fu(expr)))
    res[Dv] = (c, sp.simplify(expr), sp.simplify(ser))
    print(f"  D = {Dv},  scale c = {sp.nsimplify(c)}")
    print(f"     2M(w) = {sp.simplify(expr)}")
    print(f"           = {sp.simplify(ser)}")
    print()

# harmonic content: project onto the constant
def dc(expr):
    return sp.simplify(sp.integrate(expr, (w, 0, 2*sp.pi)) / (2*sp.pi))


print(f"  {'D':>4} {'constant (DC) term':>22} {'pure multiple angle?':>22}")
for Dv in (4, 5):
    c, expr, ser = res[Dv]
    d = sp.simplify(dc(expr))
    print(f"  {Dv:>4} {str(sp.nsimplify(d)):>22} {str(d == 0):>22}")
assert sp.simplify(dc(res[4][1])) == 0
assert sp.simplify(dc(res[5][1])) != 0
print()
for s in [
 "⇒⇒ ** THE COLLAPSES ARE NOT THE SAME KIND OF OBJECT. **",
 "     $D=4$: $2M = \\tfrac{2}{3\\sqrt3}\\sin 3w$ -- ** a PURE multiple angle, zero mean. **",
 "     $D=5$: $2M = \\tfrac18(1-\\cos 4w)$ -- ** one harmonic PLUS A CONSTANT. **",
 "",
 "⌗ ** BOTH ARE 'single-harmonic' in the sense P14 uses -- only one non-constant harmonic",
 "   survives, which is what the residual-removal condition asks for.  But a constant is not",
 "   nothing, and PART 4 is what it costs. **  The corpus records that the collapse EXISTS at",
 "   five; it has not recorded that what it collapses TO is a different shape.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE PARITY, RECOMPUTED")
print("=" * 78)
print(f"  {'D':>4} {'2M(r_0)':>22} {'2M(-r_0)':>22} {'odd in r_0?':>12} {'chirality':>11}")
for Dv in (4, 5, 6, 7):
    e = twoM(Dv)
    eo = sp.expand(e.subs(r0, -r0))
    odd = sp.simplify(eo + e) == 0
    print(f"  {Dv:>4} {str(e):>22} {str(eo):>22} {str(odd):>12} "
          f"{('gamma^5 exists' if odd else 'NONE'):>11}")
assert sp.simplify(twoM(4).subs(r0, -r0) + twoM(4)) == 0
assert sp.simplify(twoM(5).subs(r0, -r0) - twoM(5)) == 0
print()
print("  ** So the mass function is ODD exactly in even D, confirming P14's statement -- and at")
print("     D = 5 it is EVEN, so the offset parity FIXES each geometry instead of exchanging it")
print("     with a conjugate.  No mass-reflection Z_2, no 3 + 3-bar hexad, no gamma^5. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE CONSTANT COSTS")
print("=" * 78)
c4, e4, _ = res[4]
c5, e5, _ = res[5]
z4 = sp.solve(sp.Eq(e4, 0), w)
print(f"  D = 4:  2M(w) = 0 at w = {z4}  -- ** the de Sitter members SIT ON THE DIAL **")
print(f"  D = 5:  2M(w) = {sp.simplify(e5)}")
z5 = sp.solve(sp.Eq(sp.simplify(e5), 0), w)
print(f"          2M(w) = 0 at w = {z5}")
neg5 = sp.simplify(sp.Min(*[sp.simplify(e5.subs(w, v)) for v in (0, sp.pi/8, sp.pi/4, sp.pi/2)]))
print(f"          and 2M >= 0 throughout: min over sampled w = {neg5}")
print()
for s in [
 "⇒ ** AT $D=5$ THE MASS NEVER GOES NEGATIVE.  $2M = \\tfrac18(1-\\cos 4w) \\ge 0$, touching zero",
 "   only where $\\cos 4w = 1$. **  At $D=4$ the mass changes SIGN across the dial, and that sign",
 "   change is the whole of the mass-reflection structure.",
 "",
 "⌗⌗ ** SO THE CONSTANT AND THE PARITY ARE ONE FACT SEEN TWICE. **  An even mass function cannot",
 "   change sign about $r_0=0$; a harmonic-plus-DC that is bounded below by zero cannot either.",
 "   ** The DC term IS the parity obstruction, in the angle variable. **",
 "",
 "⇒ ** AND THAT IS WHAT KILLS THE DIAL AT FIVE, NOT MERELY THE CHIRALITY. **  The twelve",
 "   designations at $D=4$ come from a chain -- $\\alpha \\to 2\\alpha \\to \\sin w=\\tfrac12 \\to",
 "   \\sin 3w = 1 \\to w = 360^\\circ/(3\\times4) = 30^\\circ$ -- whose first step is a hexad built",
 "   from a fundamental and its ANTIfundamental exchanged by the mass reflection.  ** With no",
 "   sign change there is no antifundamental, hence no hexad, hence no twelve. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE D=5 WORLD, AND WHAT MAKES IT A DISCRIMINATOR")
print("=" * 78)
print(f"  {'feature':>34} {'D = 4':>22} {'D = 5':>24}")
for a, b, c in [
    ("the fold / generation count", "3", "4"),
    ("the collapse", "pure sin 3w", "cos 4w plus a constant"),
    ("mass changes sign on the dial", "yes", "NO"),
    ("mass parity R = gamma^5", "exists (D even)", "NONE (D odd)"),
    ("fundamental + antifundamental", "the A_2 hexad", "no antifundamental"),
    ("designations around the dial", "twelve", "none of that kind"),
    ("chirality", "yes", "vector-like"),
]:
    print(f"  {a:>34} {b:>22} {c:>24}")
print()
for s in [
 "⇒ ** THE $D=5$ WORLD IS NOT 'OURS WITH A FOURTH GENERATION AND NO HANDEDNESS'.  It is a world",
 "   with no matter/antimatter parity at the geometric level at all, because the structure that",
 "   supplies one -- the sign change of the mass across the swing -- is absent. **",
 "",
 "⌗ ** AND THAT SHARPENS P14'S DIMENSION ARGUMENT RATHER THAN CHANGING IT. **  P14 excludes five",
 "   because it 'would carry four generations and no handedness'.  ** The stronger statement",
 "   available is that five carries no ANTIMATTER either, on the same computation: the parity",
 "   whose absence removes $\\gamma^5$ is the same one whose absence removes the antifundamental. **",
 "   *One fact, two deliverables, and P14 currently claims only one of them.*",
 "",
 "⌗ ** WHY IT IS A DISCRIMINATOR, WHICH IS WHAT `L-06` WAS AFTER: it is a world the construction",
 "   FULLY DESCRIBES and that is manifestly not ours -- and the feature distinguishing it is not",
 "   a tuned number but a PARITY. **  A programme that selected four by fitting would have no",
 "   reason for five to fail in so structured a way; here five fails by an evenness condition on",
 "   an exponent.",
 "",
 "⚠ *Scope, as P14 states it: the $D$-dimensional metric function is taken to be the standard",
 "Tangherlini--de~Sitter one, an extension of the operator rather than a rederivation at general",
 "$D$.  ** Everything above inherits that assumption and nothing above weakens it. **",
]:
    print("  " + s)
