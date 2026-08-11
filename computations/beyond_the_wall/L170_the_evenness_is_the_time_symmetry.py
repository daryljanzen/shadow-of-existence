#!/usr/bin/env python3
"""
`L-170`.  ** IS THERE A DETERMINATION OF THE CONTINUATION UNDER WHICH THE BACKGROUND ACQUIRES AN ODD
PART?  NO — AND THE REASON IS THAT THE EVENNESS *IS* THE CONSTRUCTION'S TIME-REVERSAL SYMMETRY. **

`L-169` found the continuation diagonal because the $\\sinh^{2/3}$ law is EVEN in $\\tau$, which places
its correction at $\\eta^{6}$ and steps the Frobenius recursion past the resonance that would force a
mixing logarithm.  It left one route: mixing needs a background correction ODD in $\\tau$, with the
$\\mathbb{Z}_3$ monodromy the named candidate — a continuation going AROUND $r=0$ through a third
sheet rather than THROUGH it.

  PART 1  ** THE EXACT FACTORISATION: the whole branch structure sits in $u^{2/3}$, and the
          remaining factor is EVEN, ANALYTIC and NON-VANISHING at the branch point. **
  PART 2  ** THE THREE SHEETS DIFFER BY A CONSTANT, so none of them has an odd part. **
  PART 3  ** THE CONJUGATE BRANCH TOO — and it does not even have a branch point. **
  PART 4  ** WHAT THE EVENNESS IS: time-reversal symmetry about the branch point.  And the SAME
          invariance is what P15 already uses to fix the peak heights. **
  PART 5  The verdict, and what would have to be false.

Run: python3 L170_the_evenness_is_the_time_symmetry.py      (sympy)
"""
import sympy as sp

print(__doc__.split("Run:")[0])
u = sp.symbols('u')
w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2          # omega, exact

# =====================================================================
print("=" * 78)
print("PART 1 — THE EXACT FACTORISATION")
print("=" * 78)
print("  The corpus's law is r^3 = 2 M alpha^2 sinh^2(u),  u = 3 tau / 2 alpha.  Write it as")
print("     r = A u^(2/3) * g(u) ,   g(u) = [ sinh(u) / u ]^(2/3) .")
print("  ** Everything branched is in u^(2/3).  The claim is that g is even, analytic at 0, and")
print("     non-vanishing there — so it carries no branch structure at all. **")
h = sp.series(sp.sinh(u) / u, u, 0, 13).removeO()
print(f"\n  sinh(u)/u = {h}")
odd_h = [n for n in range(1, 13, 2) if sp.simplify(h.coeff(u, n)) != 0]
print(f"     odd powers in sinh(u)/u : {odd_h}   -- NONE, and it equals {sp.limit(sp.sinh(u)/u, u, 0)} at u = 0")
assert not odd_h
g = sp.series((sp.sinh(u) / u)**sp.Rational(2, 3), u, 0, 13).removeO()
odd_g = [n for n in range(1, 13, 2) if sp.simplify(sp.expand(g).coeff(u, n)) != 0]
print(f"\n  g(u) = [sinh(u)/u]^(2/3) = {sp.nsimplify(sp.expand(g))}")
print(f"     ** odd powers in g : {odd_g}  -- NONE. **")
assert not odd_g
print()
for s in [
 "⇒ ** AND THE EVENNESS OF $g$ IS NOT A COINCIDENCE OF THE FIRST FEW TERMS.  $\\sinh(u)/u$ is even",
 "   and equals ONE at $u=0$, so it has a logarithm analytic in $u^2$ near the origin; two-thirds",
 "   of that logarithm is again analytic in $u^2$; and its exponential is therefore a power series",
 "   in $u^2$ exactly. **  *No determination enters, because there is nothing to determine: $g$ is",
 "   single-valued wherever $\\sinh(u)/u\\ne0$.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE THREE SHEETS")
print("=" * 78)
print("  r^3 = A^3 sinh^2(u) has three roots, and they differ by the cube roots of unity:")
print(f"  {'sheet':>8} {'r':>34} {'correction factor':>20}")
for j in range(3):
    fac = sp.simplify(w**j)
    print(f"  {j:>8} {f'omega^{j} * A u^(2/3) g(u)':>34} {'g(u), identical':>20}")
print()
print("  ** THE SHEET LABEL IS A CONSTANT MULTIPLIER.  It cannot change the PARITY of a factor it")
print("     multiplies, so g is even on every sheet and the correction is even on every sheet. **")
for j in range(3):
    prod = sp.expand(sp.simplify(w**j) * g)
    odd_j = [n for n in range(1, 9, 2) if sp.simplify(prod.coeff(u, n)) != 0]
    assert not odd_j, (j, odd_j)
print("     checked term by term on all three sheets: no odd power appears on any of them.")
print()
for s in [
 "⛔ ** SO THE $\\mathbb{Z}_3$ MONODROMY — the named candidate — CANNOT SUPPLY THE ODD PART. **",
 "   *`L-161` established that the branch point's monodromy multiplies $r$ by a primitive cube root",
 "   of unity.  A multiplication is not a deformation: it rotates the solution and leaves its",
 "   parity alone.  **The third sheet was the only route `L-169` left, and it is closed.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CONJUGATE BRANCH")
print("=" * 78)
print("  The corpus's other continuation is the half-period shift Im tautilde = -pi alpha / 3,")
print("  i.e. u -> u - i pi/2, along which the geometry is real and r is NEGATIVE:")
shifted = sp.simplify(sp.sinh(u - sp.I * sp.pi / 2))
print(f"     sinh(u - i pi/2) = {shifted}     so  r^3 ∝ {sp.simplify(shifted**2)}")
print(f"     hence r ∝ -(2 M alpha^2)^(1/3) cosh^(2/3)(u)")
ch = sp.series(sp.cosh(u)**sp.Rational(2, 3), u, 0, 9).removeO()
odd_c = [n for n in range(1, 9, 2) if sp.simplify(sp.expand(ch).coeff(u, n)) != 0]
print(f"\n     cosh^(2/3)(u) = {sp.nsimplify(sp.expand(ch))}")
print(f"     ** odd powers : {odd_c}  -- NONE.  Even here too. **")
assert not odd_c
print()
for s in [
 "⌗⌗ ** AND THIS BRANCH IS EVEN FOR A STRONGER REASON THAN THE OTHER: $\\cosh^{2/3}$ IS ANALYTIC AND",
 "   NON-ZERO AT $u=0$, so the conjugate branch HAS NO BRANCH POINT AT ALL. **  *Its $|r|$ has a",
 "   smooth minimum at $(2M\\alpha^2)^{1/3}$ rather than a zero — a genuine bounce at finite radius.",
 "   **Which makes it the wrong object for this question: the cosmological continuation is the one",
 "   THROUGH $r=0$, and the corpus is explicit that the beginning is the branch point.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE EVENNESS IS")
print("=" * 78)
print("  sinh^2(u) is even in u.  Stated as geometry rather than as algebra, that is:")
print()
print("     ** r(-tau) = r(tau) :  THE CONSTRUCTION'S COSMOGENESIS IS TIME-SYMMETRIC ABOUT THE")
print("        BRANCH POINT.  The collapse leg and the expanding leg are one another's mirror. **")
sym = sp.simplify(sp.sinh(-u)**2 - sp.sinh(u)**2)
print(f"\n     check:  sinh^2(-u) - sinh^2(u) = {sym}")
assert sym == 0
print()
for s in [
 "⇒⇒ ** SO `L-169`'s DIAGONALITY IS NOT A TECHNICAL ACCIDENT OF A FROBENIUS RECURSION.  It is the",
 "   TIME-REVERSAL SYMMETRY OF THE CONSTRUCTION, read on the perturbations. **  *A time-symmetric",
 "   background about a singular point maps the growing mode to the decaying one and cannot mix",
 "   them, because mixing would distinguish a direction of time that the background does not.*",
 "",
 "⌗⌗⌗ ** AND THE CORPUS ALREADY LEANS ON EXACTLY THIS INVARIANCE, ONE OBSERVABLE OVER: P15",
 "   `sec:amplitude` fixes the acoustic peak HEIGHTS from a driving amplitude that is *'exactly",
 "   invariant under time reversal'* and may therefore be evaluated on the contracting side. **",
 "   ⇒ *So one symmetry has two consequences and the corpus had banked only the welcome one:*",
 "     ***the time-reversal invariance that lets the peak heights be computed on the collapsing leg",
 "     is the same invariance that stops the scale-invariant spectrum from crossing.***",
 "",
 "⌗ *That is the honest shape of the result: not a missing mechanism, and not bad luck, but ONE",
 "   structural fact of the construction paying out in two directions.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE VERDICT")
print("=" * 78)
print(f"  {'route':>44} {'odd part?':>12} {'status':>14}")
for a, b, c in [("the principal sheet", "none", "closed"),
                ("the other two sheets (Z_3 monodromy)", "none", "closed"),
                ("the conjugate branch (half-period)", "none", "closed, and no branch point"),
                ("breaking the time symmetry", "would do it", "NOT AVAILABLE HERE")]:
    print(f"  {a:>44} {b:>12} {c:>14}")
print()
for s in [
 "⛔⛔ ** THE FALSIFIER FIRES NEGATIVE: THERE IS NO ODD PART ON ANY DETERMINATION, SO THE",
 "   DIAGONALITY IS ROBUST AND `L-150`'s SCALE INVARIANCE IS CONFINED TO THE CONTRACTING SIDE. **",
 "   *Not provisionally, and not pending a harder calculation — the obstruction is the parity of",
 "   $\\sinh^2$, which is the time symmetry of the cosmogenesis itself.*",
 "",
 "✔ ** WHAT THE ARC LEAVES STANDING, AND IT IS WORTH MORE THAN THE CLAIM IT REPLACED: **",
 "   *(i) the collapse leg IS a scale-invariant background, the second root of $\\beta(\\beta-1)=2$,",
 "   which the corpus had denied having;*",
 "   *(ii) the spectrum it freezes does not reach the observer, and the reason is a symmetry the",
 "   corpus already uses elsewhere;*",
 "   *(iii) so $n_s$ remains inherited — but the corpus now knows WHY it must be, rather than",
 "   merely recording that it is.*",
 "",
 "⚑ ** AND WHAT WOULD OVERTURN IT, STATED SO IT IS TESTABLE RATHER THAN COMFORTING: any physical",
 "   content on the collapse leg that breaks $r(-\\tau)=r(\\tau)$. **  *The corpus's leg is the",
 "   marginally-bound $E=1$ geodesic of an exactly vacuum SdS exterior, and that is what makes it",
 "   exactly even.  **A progenitor with real matter content — pressure, dissipation, anything with",
 "   an arrow — would not be, and THAT is where a mixing term would have to come from.***",
 "   ⌗ *Which puts the question back where `L-150` already sits: what the progenitor actually was.*",
]:
    print("  " + s)
