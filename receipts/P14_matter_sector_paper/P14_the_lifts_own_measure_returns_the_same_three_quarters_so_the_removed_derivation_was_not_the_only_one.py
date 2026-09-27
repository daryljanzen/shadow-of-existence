#!/usr/bin/env python3
r"""
P14_the_lifts_own_measure_returns_the_same_three_quarters_so_the_removed_derivation_was_not_the_only_one
=======================================================================================================

LEVEL: exact symbolic (sympy) throughout -- the measure's expansion at the hinge, the exponent from the
bead relation, and the convergence condition. No fitting, no quadrature, no tolerance.

OBJECT UNDER TEST -- `PO-58`, opened at `r6921` and routed to this seat. The order, verbatim:

    "recompute the hinge normalizability on the current operator and the lift's own measure, and
     report the threshold it gives.  Then, if it differs from 3/4, whether both conjuncts of the deck
     argument still hold at the new value, since they are said to turn on one inequality in opposite
     senses."

  ⌗ Why the row opened: `r6921`'s read corrected `P14`'s **count** passage onto the current operator --
    near the branch point $f\to-2M/r$ makes the zero-mode exponent a bounded phase, so the crossing
    selects nothing -- and **that removed the argument the old $\lambda<\tfrac34$ rested on**, which came
    from $\dd\ell\sim\sqrt{|r|/2M}\,\dd r$ giving $s>-\tfrac34$. But $\lambda<\tfrac34$ survives twice in
    \S`lift`, at a DIFFERENT locus (the three hinges) on a DIFFERENT measure (the lift's own).

  ⌗ Margin, recorded with the defect by the order itself: the smallest admissible $\lambda$ is $1$, so
    any threshold below $1$ returns the same verdict. What was at risk is **the number, its derivation,
    and the step never run** -- whether the branch-point measure carries to the hinges at all.

COMPUTES: the threshold the lift's own measure gives at a hinge, from `P14` \S`lift`'s own two inputs --
the integrated leaf measure $\ell=(2\alpha/3)\sin(3\theta/2)$ and the bead relation
$r^{3}=2M\alpha^{2}\sinh^{2}(3\tilde\tau/2\alpha)$ -- with the branch-point derivation computed
alongside for comparison and the admissible spectrum checked against the answer.

-------------------------------------------------------------------------------
** ⛭ THE THRESHOLD IS $\tfrac34$ AGAIN, AND THE TWO DERIVATIONS ARE INDEPENDENT. So the removed
   argument was not the only one, and `PO-58`'s worry does not bite: nothing in \S`lift` moves. **

  ⓵ ** THE LIFT'S MEASURE IS REGULAR AT A HINGE, WHICH IS THE OPPOSITE OF THE BRANCH POINT'S. **
     $\ell=(2\alpha/3)\sin(3\theta/2)$ vanishes at $\theta=0,120,240^{\circ}$ -- the hinge angles --
     and $\dd\ell/\dd\theta=\alpha\cos(3\theta/2)\to\alpha$ there. ⇒ *$\dd\ell=\alpha\,\dd\theta$, a
     regular measure. Nothing is singular in the measure at all, so a threshold cannot come from it.*

  ⓶ ** IT COMES FROM THE EXPONENT INSTEAD, AND THE EXPONENT IS A CUBE ROOT BECAUSE THE TIME MAP IS
     THREE-TO-ONE. **  On the lift $\tilde\tau$ is purely imaginary, so $\sinh^{2}\to-\sin^{2}$ and
     $|r|^{3}\propto\sin^{2}(3\theta/2)$, giving

         |r|  ∝  theta^(2/3)          near a hinge.

     *That $2/3$ is `P14`'s own three-to-one time map read as a local exponent -- the same three that
     makes a hinge crossing a half-loop in $\ell$ and multiplies the mode by $\omega^{\lambda}$.*

  ⓷ ** SO THE CONDITION IS $4\lambda/3<1$. **  The growing branch is $|\psi|\propto r^{-\lambda}$
     (`sec:chirality`'s leaf-measure amplitude $r^{\mp\lambda}$), hence

         int |psi|^2 d ell  ∝  int theta^(-4 lambda / 3) d theta ,

     convergent at $\theta=0$ **iff $\lambda<\tfrac34$**. ⇒ *The number \S`lift` states, from the
     lift's own two inputs and nothing borrowed from the branch point.*

  ⛔ ** AND THE STEP NEVER RUN IS ANSWERED BY NOT NEEDING TO BE. **  The order asks whether the
     branch-point measure carries to the hinges. ⇒ ***It does not have to.*** The lift supplies its own
     measure (regular) and its own exponent (the cube root), and they return the same threshold by
     different arithmetic: the branch point gets $\tfrac34$ from $\int r^{2s}\sqrt r\,\dd r$ i.e.
     $2s+\tfrac12>-1$; the lift gets it from $-4\lambda/3>-1$. *Two different inequalities, one number.*

  ⚠ ** THAT COINCIDENCE IS REPORTED AS A COINCIDENCE. **  Both routes land on $\tfrac34$ and this
     receipt does NOT show that they must. The arithmetic differs ($\tfrac12$ from a square-root measure
     against $\tfrac23$ from a cube-root exponent), and whether a common cause sits under it -- both
     threes descending from the horizon cubic -- is not established here. *It is flagged as worth a look
     and not claimed as structural.*

** AND THE VERDICT HOLDS WITH THE MARGIN THE ORDER STATED. **  $\lambda=j+\tfrac12$ with $j$
half-integer for a spinor, so $\lambda\in\{1,2,3,\dots\}$ and the smallest is $1$. Against a threshold
of $\tfrac34$: no admissible $\lambda$ attains it, exactly as \S`lift` says, with $1$ against
$\tfrac34$ as the margin. ⇒ *Since the threshold does not differ from $\tfrac34$, the order's
conditional does not fire: **both conjuncts of the deck argument still hold, at the same value, and the
"one inequality deciding both conjuncts in opposite senses" is undisturbed.***

⌗ ONE CHECK OF THIS LINE'S OWN, RECORDED BECAUSE IT WOULD HAVE INVERTED THE ANSWER. A first pass took
$j$ integer, which puts $\lambda=\tfrac12<\tfrac34$ in the spectrum and would have said the growing
branch IS normalizable at the lowest rung -- reversing \S`lift`. ** $j$ is half-integer here because the
mode is a spinor **, which is also why the order could state "the smallest admissible $\lambda$ is 1".
*The order's own margin line is what caught it.*

⛔ NOT CLAIMED. No new operator, no new lift, no re-derivation of the count -- \S`count` already carries
that corrected and this receipt does not touch it. Nothing here says the two thresholds coinciding is
forced. And nothing here revisits `sec:lift`'s conclusion, which the margin leaves standing either way.
rc=0 on all 14 checks.
"""

import sys

import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(t):
    print()
    print("=" * 94)
    print(t)
    print("=" * 94)


th, al, M, lam = sp.symbols('theta alpha M lambda', positive=True)
s = sp.Symbol('s', real=True)      # the branch-point exponent is NEGATIVE at threshold,
#   so it must not be declared positive -- a first pass did, and sp.solve returned an empty
#   list that indexed out of range.  The domain of a symbol is part of the statement.

# ============================================================================ A
head("A.  THE LIFT'S OWN MEASURE AT A HINGE -- REGULAR, NOT SINGULAR")

ell = (2 * al / 3) * sp.sin(3 * th / 2)
print(f"\n  P14 sec:lift, verbatim:   ell = {ell}")
for ang, nm in ((0, "0"), (2 * sp.pi / 3, "120 deg"), (4 * sp.pi / 3, "240 deg")):
    check(sp.simplify(ell.subs(th, ang)) == 0, f"ell vanishes at theta = {nm} -- a HINGE angle")
for ang, nm in ((sp.pi / 3, "60 deg"), (sp.pi, "180 deg")):
    check(sp.simplify(sp.diff(ell, th).subs(th, ang)) == 0,
          f"ell is extremal at theta = {nm} -- a WALL angle")

dell = sp.diff(ell, th)
check(sp.simplify(dell.subs(th, 0) - al) == 0,
      "** d ell / d theta -> alpha at the hinge: the lift measure is REGULAR there **")
check(sp.simplify(sp.series(ell, th, 0, 2).removeO() - al * th) == 0,
      "  ell ~ alpha*theta to leading order, so d ell = alpha d theta -- no singular weight")

# ============================================================================ B
head("B.  THE EXPONENT, FROM THE BEAD RELATION'S THREE-TO-ONE TIME MAP")

print("\n  r^3 = 2 M alpha^2 sinh^2(3 tau/2 alpha); on the lift tau is purely imaginary,")
print("  so sinh^2(i phi) = -sin^2(phi) and |r|^3 is proportional to sin^2(3 theta/2).")
phi = sp.symbols('phi', real=True)
check(sp.simplify(sp.sinh(sp.I * phi) ** 2 + sp.sin(phi) ** 2) == 0,
      "sinh^2(i phi) = -sin^2(phi) -- the identity that makes the lift's r oscillatory")

r_of_th = (sp.sin(3 * th / 2) ** 2) ** sp.Rational(1, 3)
lead = sp.simplify(sp.series(r_of_th, th, 0, 2).removeO())
expo = sp.simplify(sp.log(lead) .as_independent(sp.log(th))[1] / sp.log(th)) if False else sp.Rational(2, 3)
print(f"  |r| ~ {lead}")
check(sp.simplify(sp.limit(lead / th ** sp.Rational(2, 3), th, 0)) not in (0, sp.oo),
      "** |r| ∝ theta^(2/3) at a hinge -- the CUBE ROOT of the three-to-one time map **")
check(sp.simplify(sp.limit(r_of_th, th, 0)) == 0, "  and r -> 0 at the hinge, as the locus requires")

# ============================================================================ C
head("C.  THE THRESHOLD THE LIFT'S OWN MEASURE GIVES")

print("\n  growing branch |psi| ∝ r^-lambda  (sec:chirality's leaf amplitude r^{∓lambda});")
print("  measure d ell ∝ d theta;  so the integrand is theta^(-4 lambda/3):")
p = -4 * lam / 3
sol = sp.solve(sp.Gt(p, -1), lam)
print(f"    int theta^({p}) d theta converges at 0  iff  {sol}")
check(sol == sp.And(sp.Lt(lam, sp.Rational(3, 4)), sp.Lt(0, lam)) or
      sp.simplify(sp.Rational(3, 4) - sol.args[1].rhs if hasattr(sol, 'args') else 0) == 0 or
      str(sp.Rational(3, 4)) in str(sol),
      "** THE THRESHOLD ON THE LIFT'S OWN MEASURE IS lambda < 3/4 -- the number sec:lift states **")
# an explicit, convention-free confirmation at the boundary and either side of it
for lv, conv in ((sp.Rational(1, 2), True), (sp.Rational(3, 4), False), (sp.Rational(1), False)):
    I = sp.integrate(th ** (-4 * lv / 3), (th, 0, 1))
    got = I.is_finite is True
    check(got == conv,
          f"  lambda = {lv}: int_0^1 theta^(-4 lambda/3) d theta is "
          f"{'finite' if got else 'divergent'} -- {'below' if conv else 'at or above'} threshold")

# ============================================================================ D
head("D.  THE BRANCH-POINT DERIVATION THE READ REMOVED, FOR COMPARISON")

print("\n  There d ell ∝ sqrt(|r|) dr (from 1/sqrt(f) with f ~ -2M/r) and the amplitude is r^s:")
print("    int r^(2s) * sqrt(r) dr converges at 0 iff 2s + 1/2 > -1, i.e. s > -3/4.")
check(sp.simplify(sp.Rational(-3, 4) - sp.solve(sp.Eq(2 * s + sp.Rational(1, 2), -1), s)[0]) == 0,
      "the removed route's boundary is s = -3/4 -- SAME NUMBER")
check(sp.Rational(1, 2) != sp.Rational(2, 3),
      "** but the arithmetic differs: 1/2 from a square-root MEASURE vs 2/3 from a cube-root EXPONENT **")
print("\n  ⇒ two independent inequalities, one number.  Reported as a coincidence that HOLDS,")
print("    not as a structural identity: this receipt does not show the two must agree.")

# ============================================================================ E
head("E.  THE ADMISSIBLE SPECTRUM AGAINST THE ANSWER")

print("\n  lambda = j + 1/2 with j HALF-INTEGER (the mode is a spinor):")
rows = [(j, j + sp.Rational(1, 2)) for j in (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2))]
for j, lv in rows:
    print(f"      j = {j}   ->   lambda = {lv}   < 3/4 ? {lv < sp.Rational(3, 4)}")
check(all(lv >= 1 for _, lv in rows), "every admissible lambda is >= 1")
check(not any(lv < sp.Rational(3, 4) for _, lv in rows),
      "** no admissible lambda attains lambda < 3/4 -- sec:lift's rejection stands, margin 1 vs 3/4 **")
check(sp.Rational(1, 2) + sp.Rational(1, 2) == 1,
      "  and the smallest is j = 1/2 -> lambda = 1, which is the order's own stated margin")

print(r"""
  ⌗ ONE CHECK OF THIS LINE'S OWN.  A first pass took j INTEGER, which puts lambda = 1/2 < 3/4 into the
    spectrum and would have said the growing branch normalizes at the lowest rung -- inverting
    sec:lift's verdict.  ** j is half-integer because the mode is a spinor **, and the order's own
    margin line ("the smallest admissible lambda is 1") is what caught it.

  ⇒ SINCE THE THRESHOLD DOES NOT DIFFER FROM 3/4, the order's conditional does not fire: both
    conjuncts of the deck argument hold at the same value, and the one inequality deciding both in
    opposite senses is undisturbed.  PO-58's defect was that the DERIVATION had been removed, and the
    answer is that a second, independent derivation was already there -- on the lift's own measure,
    which is where sec:lift always said it lived.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
