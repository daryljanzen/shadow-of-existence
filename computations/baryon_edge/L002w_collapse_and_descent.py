#!/usr/bin/env python3
"""
L-2w — TWO OLD LEADS ANSWERED BY RESULTS ALREADY ON DISK, WHICH NOBODY WENT BACK TO CLAIM.

`L-02`: is the single-harmonic collapse a REQUIREMENT at other $D$, or only a fact at four?
        Its own owed action names the test: ** "ask what the collapse BUYS at D=4 -- if it is
        what makes w a dial, the demand transfers." **
`L-03`: nothing forces a descent of length > 1; the whole rise stays permitted, which R2
        condemns.  Owed: ** "is there anything a one-step descent fails to deliver?" **

** BOTH HAVE DETERMINATE ANSWERS FROM WORK ALREADY BANKED, AND IN BOTH CASES THE ANSWER IS
SHARPER THAN THE LEAD'S OWN CONDITIONAL. **

  PART 1  ** `L-02`: what the collapse buys -- and $D=5$ is the witness that it is NOT the dial. **
  PART 2  So the collapse is NECESSARY AND NOT SUFFICIENT, and the corpus already uses it that way.
  PART 3  ** `L-03`: a one-step descent delivers exactly ONE member, and it is the massless one. **
  PART 4  What that does to R2's complaint.

Run: python3 L002w_collapse_and_descent.py
"""
import sympy as sp

print(__doc__.split("Run:")[0])
r0, w = sp.symbols('r_0 w', real=True)

# =====================================================================
print("=" * 78)
print("PART 1 — `L-02`: WHAT THE COLLAPSE BUYS")
print("=" * 78)
print("  The lead's own test: if the collapse is what makes w a DIAL, the demand transfers to")
print("  higher D.  So: does the collapse give a dial?")
print()
cases = []
for Dv, c in ((4, 2/sp.sqrt(3)), (5, sp.Integer(1))):
    expr = sp.simplify(sp.fu((r0**(Dv-3) - r0**(Dv-1)).subs(r0, c*sp.sin(w))))
    dcv = sp.simplify(sp.integrate(expr, (w, 0, 2*sp.pi)) / (2*sp.pi))
    signs = {int(sp.sign(sp.N(expr.subs(w, v)))) for v in
             (sp.pi/12, sp.pi/6, sp.pi/3, sp.pi/2, 2*sp.pi/3, 5*sp.pi/6)}
    cases.append((Dv, expr, dcv, signs))
    print(f"  D = {Dv}:  collapse EXISTS, 2M(w) = {expr}")
    print(f"           mean = {sp.nsimplify(dcv)},   signs taken across the swing = {sorted(signs)}")
print()
print(f"  {'D':>4} {'collapse?':>10} {'zero mean?':>11} {'mass changes sign?':>19} {'⇒ a DIAL?':>10}")
for Dv, expr, dcv, signs in cases:
    zm = (sp.simplify(dcv) == 0)
    ch = (1 in signs and -1 in signs)
    print(f"  {Dv:>4} {'yes':>10} {str(zm):>11} {str(ch):>19} {str(ch):>10}")
assert cases[0][2] == 0 and cases[1][2] != 0
print()
for s in [
 "⇒⇒ ** THE COLLAPSE HAPPENS AT BOTH FOUR AND FIVE.  THE DIAL HAPPENS ONLY AT FOUR. **  So the",
 "   collapse is NOT what makes $w$ a dial, and `L-02`'s conditional -- 'if it is what makes $w$",
 "   a dial, the demand transfers' -- has its antecedent FALSE.",
 "",
 "⌗ ** WHAT ACTUALLY MAKES THE DIAL IS ZERO MEAN, which is the collapse TOGETHER WITH the",
 "   parity. **  At five the collapse leaves a constant, the mass never changes sign, and there",
 "   is no fundamental/antifundamental exchange for a dial to be built on.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — SO IT IS NECESSARY AND NOT SUFFICIENT")
print("=" * 78)
for s in [
 "⇒ ** `L-02`'s QUESTION -- 'a REQUIREMENT, or only a fact at four?' -- IS A FALSE ALTERNATIVE,",
 "   AND THE CORPUS ALREADY DECLINES IT. **  P14 imposes TWO conditions on the dimension, not",
 "   one: *the collapse* (a single scale removing the residual harmonic -- available at four and",
 "   five) and *the parity* (the mass odd in the offset -- even $D$ only).  ** Four is the",
 "   intersection. **",
 "",
 "⌗ ** SO THE COLLAPSE IS A REQUIREMENT ON ANY $D$ THAT IS TO CARRY A GENERATION COUNT AT ALL --",
 "   it is what makes the horizon relation readable as an angle -- AND IT IS NOT SUFFICIENT FOR",
 "   ANYTHING ELSE. **  The lead was written when only one condition was in view; with both, the",
 "   question dissolves rather than resolves.",
 "",
 "⌗ *And $D=5$ is what makes this a computation rather than a definition: it is a real case where",
 "the collapse holds and the dial does not, so the two are separated by an example and not by a",
 "distinction drawn to save the argument.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-03`: WHAT A ONE-STEP DESCENT DELIVERS")
print("=" * 78)
al, c_, M, r = sp.symbols('alpha c M r', positive=True)
print("  A one-step descent is a HYPERPLANE SECTION of the substrate -- the linear move, and the")
print("  only one available without bending the cut.  Splitting X = c n + Y with eta(n,Y)=0:")
print()
print("     eta(Y,Y) = alpha^2 - c^2      ⇒ a de Sitter four-space, for EVERY admissible n, c")
print()
print("  and Schwarzschild--de Sitter has Kretschmann scalar")
K = 48*M**2/r**6 + 24/al**4
print(f"     K = {K}")
dK = sp.simplify(sp.diff(K, r))
print(f"     dK/dr = {dK}   ⇒ constant in r only when M = 0")
sols = sp.solve(sp.Eq(sp.numer(sp.together(dK)), 0), M)
print(f"     solving for constancy: M = {sols}")
assert 0 in sols or sp.Integer(0) in sols
print()
for s in [
 "⇒ ** A PLANE SECTION OF THE SUBSTRATE IS SdS EXACTLY WHEN THE MASS VANISHES. **  So a descent",
 "   of length ONE delivers precisely the $M=0$ member and nothing else -- **not a family, a",
 "   single point of one**.",
 "",
 "⌗ ** AND THE SECOND STEP IS NOT OPTIONAL, IT IS WHAT MASS *IS* ON THIS CONSTRUCTION. **  The",
 "   closure defect of a bent cut factors with an overall $M$: the amount by which a cut fails to",
 "   close as a hypersurface is the mass it carries.  ** So 'descend twice' and 'carry mass' are",
 "   the same sentence, and a one-step descent is not a shorter route to the same place -- it is",
 "   a route to a different, massless place. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THAT DOES TO R2's COMPLAINT")
print("=" * 78)
for s in [
 "`L-03` framed this as a defect: *'nothing forces a descent of length > 1; the whole rise stays",
 "permitted, which R2 condemns.'*  R2's condemnation is of a structure that permits more than it",
 "needs.",
 "",
 "⇒ ** THE RISE IS NOT PERMISSIVE.  Each rung delivers a DIFFERENT SET of geometries, and the",
 "   first rung delivers exactly one. **  A one-step descent cannot reach any massive member,",
 "   so nothing above the first rung is reachable by skipping -- there is no shorter route being",
 "   left un-taken.",
 "",
 "⌗ ** SO R2 IS SATISFIED BY A COMPUTATION RATHER THAN BY A STIPULATION, which is the outcome",
 "   the lead wanted and could not get when it was written. **  The result it needed was banked",
 "   at c54.41 and landed in p0 at c54.49; ** nobody went back to claim it against this lead. **",
 "",
 "⌗ *That is now the sixth item in this sweep answered by work already on disk.  ** The register",
 "records what is OWED and has no mechanism for noticing when something else PAYS it. ** *",
]:
    print("  " + s)
