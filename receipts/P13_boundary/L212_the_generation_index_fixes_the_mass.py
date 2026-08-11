#!/usr/bin/env python3
"""L212_the_generation_index_fixes_the_mass.py -- L-212's second move, and it CLOSES the lead.

L-212 asks whether the R-odd fermion mass departure inherits a THREE-FOLD FORM from the geometry.
Move 1 (`L212_the_factorisation_singles_out_nothing`) removed the route through the horizon cubic's
factorisation: every root satisfies 2M = r - r^3, so the 1+2 split is a choice of which root is the
hole and the Weyl S_3 permutes that choice with the roots.  ** The question survived; the route did
not. **  Move 2 asks the same question of the OTHER two threes the corpus distinguishes.

THE CORPUS DISTINGUISHES THREE THREES, and P14 sec:whichthree settles which is which:

  * the HORIZON three  -- the cubic's roots, permuted by the Weyl S_3.  Killed as a route by move 1.
  * the HINGE three    -- ** a WITHIN-STATE index, not a family symmetry **: the substrate's null
                          structure admits a bound triple, and the causal classification of the six
                          hinge-ends forces it to take ONE PUNCTURE PER HINGE (two ends of one hinge
                          timelike, two on one horn spacelike, only the cross pairs null).  "If the
                          three hinges were the generations, a bound triple would be one constituent
                          from each generation, which is not what a bound triple of like constituents
                          is."  So it indexes constituents WITHIN a bound state, not copies of it.
  * the TURNAROUND three -- ** where the generations actually sit **: the marginally-bound congruence
                          integrates to r^{D-1} = 2M a^2 sinh^2((D-1) tau / 2a), and the shift
                          tau -> tau + 2 pi i a/(D-1) leaves r^{D-1} INVARIANT while sending
                          r -> e^{2 pi i/(D-1)} r -- a cyclic deck action of order D-1 = 3.

** THE DECISIVE FACT IS IN THE DECK'S OWN DEFINITION: the shift leaves r^{D-1} invariant, and
r^{D-1} carries 2M as its coefficient.  So the generation index acts on the turnaround RADIUS by a
cube root of unity and FIXES THE MASS PARAMETER exactly. **

A grading needs the index to MOVE the graded quantity.  The generations' index does not move 2M at
all, so no three-fold mass structure can descend from it; and 2M is not equivariant either --
2M(w r0) = w r0 - r0^3, which is neither 2M(r0) nor w.2M(r0).  ** The mass parameter is deck-blind. **

⇒ ALL THREE THREES ARE ELIMINATED AS SOURCES OF A MASS GRADING: the horizon three by move 1, the
hinge three because it is a within-state index, the turnaround three because it fixes 2M.  This
closes L-212 in the negative, and the closure is consistent with what the corpus already says in its
own voice -- the deck Z_3 "says the three are ONE OBJECT READ THREE WAYS and predicts NO MIXING,
because it is not a symmetry that gets broken."

** WHAT IS NOT SHOWN, and must not be read in. **  This does not show that no geometric structure
could ever bear on fermion masses; it shows that ** the three-fold indices the corpus actually has do
not grade the mass parameter **.  A2's flavour-guard stands unchanged either way: no
geometric-quantity = mass identification.

Written r2404.  Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  L-212 MOVE 2 -- do the hinge or turnaround threes grade the mass parameter?")
    print()

    tau, a, M = sp.symbols('tau alpha M', positive=True)
    w = sp.exp(2*sp.pi*sp.I/3)
    r0 = sp.Symbol('r0')

    # the deck shift leaves r^{D-1} invariant (D = 4)
    r3 = 2*M*a**2*sp.sinh(3*tau/(2*a))**2
    r3s = 2*M*a**2*sp.sinh(3*(tau + 2*sp.pi*sp.I*a/3)/(2*a))**2
    check("deck shift tau -> tau + 2.pi.i.a/3 leaves r^3 invariant",
          sp.simplify(sp.expand_trig(r3s - r3)) == 0)

    # r^3 carries 2M as its coefficient, so 2M is untouched by the deck
    check("r^3 = 2M.a^2.sinh^2(3.tau/2a): the deck fixes the coefficient 2M",
          sp.simplify(sp.diff(r3, M) - 2*a**2*sp.sinh(3*tau/(2*a))**2) == 0)

    # and 2M(r0) is not equivariant under r0 -> w r0 either
    lhs = sp.expand(w*r0 - (w*r0)**3)
    check("2M(w.r0) != 2M(r0)  (not invariant as a function of the root)",
          sp.simplify(lhs - (r0 - r0**3)) != 0)
    check("2M(w.r0) != w.2M(r0)  (not equivariant: no character grading)",
          sp.simplify(lhs - w*(r0 - r0**3)) != 0)

    # the cube of the deck is the identity -- it is an order-3 action, not a scaling family
    check("the deck action has order 3 (w^3 = 1)", sp.simplify(w**3 - 1) == 0)

    # a grading needs the index to move the graded quantity; sanity: it does move r
    check("the deck DOES move the turnaround radius: w.r0 != r0 for r0 != 0",
          sp.simplify(w*r0 - r0) != 0)

    print()
    if FAILED:
        print(f"  {len(FAILED)} check(s) FAILED")
        return 1
    print("  VERDICT: the generation index (the turnaround deck Z_3) acts on the RADIUS and FIXES")
    print("  the mass parameter 2M exactly; and 2M is neither invariant nor equivariant as a")
    print("  function of the root.  The hinge three is a WITHIN-STATE index by P14 sec:whichthree,")
    print("  and the horizon three was eliminated by move 1.")
    print("  ** All three threes are eliminated as sources of a mass grading.  L-212 closes in the")
    print("     negative -- and the corpus already said so: the deck 'predicts NO mixing, because it")
    print("     is not a symmetry that gets broken'. **")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
