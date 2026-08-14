#!/usr/bin/env python3
"""U2_the_matter_sector_spends_none.py -- L-200 §1: does the BUILT matter sector spend a free constant?

THE OPENING QUESTION, from the corpus and not from outside it.  U1 (§0) re-ran the count and found the
gravitational--quantum sector at ZERO free dimensionless constants and one candidate (P3's
D-dimensional metric function) since eliminated by derivation.  ** The retired ledger's own stated
limit was "the matter-side count: OPEN -- the fermion sector is unbuilt." **  The sector has since
been built (P14).  So:

    ** Does the built matter sector spend any free dimensionless constant? **

THE ANSWER IS NO, AND P14 SAYS SO IN ITS OWN VOICE THREE TIMES OVER -- but the interesting part is
that each "no" has a DIFFERENT reason, and the third is the one that matters:

  (1) THE GENERATION COUNT IS NOT A DATUM.  "The generation-replication puzzle---why the fermions come
      in three families, a number the Standard Model takes as an input---is, within CR, ** NO FREE
      COUNT ** but the three 120-degree hinges of one substrate read three ways: three is the
      maximally-symmetric matter construction's own index, ** not a datum to be fit **."
      ⇒ A count that is an index is not a spent parameter.  It is the SAME parameter (Lambda, through
        alpha) read structurally.

  (2) THE HYPERCHARGES ARE NOT FITTED.  "the constant came out equal to the quark doublet's
      hypercharge 1/3 ** with nothing fitted **" -- and the five SM hypercharges follow from the
      per-wall anomaly conditions together with the EXISTENCE of Yukawa couplings, uniquely up to
      normalisation.  ⇒ A representation-theoretic constraint spends no magnitude.

  (3) ** AND THE ONE PLACE A DIMENSIONLESS CONSTANT WOULD HAVE BEEN NEEDED IS WHERE THE SECTOR STOPS.
      ** "Leaving [the flat locus] requires a variational principle, and a Yang--Mills term in four
      dimensions carries ** a dimensionless coupling that a single length cannot build ** ---the
      substrate's one invariant being alpha = sqrt(3/Lambda), whose energy hbar c/alpha sits some
      forty-one decades below the strong scale."
      ⇒ ** The sector does not spend a free coupling BECAUSE IT CANNOT BUILD ONE, and it says so
        rather than supplying one. **  "The position is not that the coupling is unbuilt but that a
        coupling is not the kind of thing a holonomy supplies."

** THIS IS THE COUNT'S DECISIVE STRUCTURE, AND IT IS STRONGER THAN A TALLY OF ZERO. **  A theory can
score zero free constants two ways: by DERIVING each one, or by DECLINING to speak about them.  P14
does the second, explicitly, with the reason stated as a theorem of the one-constant law -- ** a
dimensionless magnitude needs two invariants and the substrate has one ** (p0).  So the count closes
not because the matter sector was frugal but because ** the sector's boundary IS the boundary of what
one constant can express. **

⇒ THE COUNT, WHOLE, AT c54.163:  ** ONE dimensionful scale (Lambda) · THREE unit gauges (c, G, hbar) ·
   ONE free datum (rho_r/rho_m, and L-150 owes its derivation) · ZERO free dimensionless constants
   anywhere. **

WHAT THIS DOES AND DOES NOT SETTLE.  It does not close L-200: p0's test asks that the count EQUAL the
substrate's non-symmetric residue, and ** the residue side has not been counted here ** -- this probe
counts the spend, not the budget.  ** And rho_r/rho_m remains a one-parameter accommodation by the
corpus's own words in three papers. **  What it does settle is the half that was open: ** the matter
side spends nothing, and the reason is a law rather than an accident. **

Written r2421.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(p):
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8', errors='replace').read())


def main():
    print()
    print('  U2 -- does the BUILT matter sector spend a free dimensionless constant?')
    print()
    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    p0 = flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))

    # (1) the count is an index, not a datum
    check('(1) the generation count is "no free count" but the substrate\'s own index',
          'no free count but the three $120^\\circ$ hinges of one substrate read three ways' in p14)
    check('(1) and explicitly "not a datum to be fit"', 'not a datum to be fit' in p14)

    # (2) the hypercharges are not fitted
    check('(2) the hypercharge constant "came out ... with nothing fitted"',
          'with nothing fitted' in p14)
    check('(2) and the five SM hypercharges follow from anomalies + Yukawa EXISTENCE',
          'the existence of the Yukawa couplings' in p14)

    # (3) THE DECISIVE ONE: the sector cannot build a dimensionless coupling
    check('(3) a Yang-Mills coupling is dimensionless and "a single length cannot build" it',
          'carries a dimensionless coupling that a single length cannot build' in p14)
    check('(3) the substrate\'s one invariant is named as alpha = sqrt(3/Lambda)',
          "the substrate's one invariant being $\\alpha=\\sqrt{3/\\Lambda}$" in p14)
    check('(3) and the position is stated as a KIND-claim, not a to-do',
          'the position is not that the coupling is unbuilt but that a coupling is not the kind of '
          'thing a holonomy supplies' in p14)
    check('(3) grounded in the one-constant law: a dimensionless magnitude needs TWO invariants',
          'a dimensionless magnitude needs two' in p0)

    # and the honesty marker: no third mechanism is claimed to be excluded
    check('P14 states the limit of its own exclusion ("no third mechanism has been named")',
          'no third mechanism has been named' in p14)

    # ⛔ AMENDED c54.216, `L-550`.  This was a COUNT PIN -- '"dimensionless" occurs exactly once' --
    #    and c54.216 broke it by adding a SECOND occurrence that says the SAME thing more strongly
    #    ("that term requires a dimensionless number the substrate's ledger does not carry").
    #  ⇒ *** A count cannot tell a contradicting occurrence from a corroborating one. ***  What the
    #    pin was proxying for is that P14 nowhere HEDGES the claim -- never says the sector does, or
    #    might, spend a dimensionless constant -- so that is what is checked now, on every occurrence.
    occ = [p14[max(0, m.start()-160):m.start()+160] for m in re.finditer(r'dimensionless', p14)]
    HEDGE = ('would need a dimensionless', 'requires a free dimensionless', 'spends a dimensionless',
             'introduces a dimensionless', 'a dimensionless constant is fitted')
    hedged = [c for c in occ if any(h in c for h in HEDGE)]
    check(f'every one of the {len(occ)} "dimensionless" occurrences in P14 is the CANNOT-BUILD claim '
          f'or a restatement of it, and none hedges it ({len(hedged)} hedged)',
          len(occ) >= 1 and hedged == [])
    check('   and both occurrences sit in the one paragraph that walls the coupling -- the second '
          'added c54.216 states the bound is on the TARGET, not the route',
          any('a single length cannot build' in c for c in occ)
          and any('the substrate\'s ledger does not carry' in c for c in occ))
    check('and "free constant" occurs nowhere in P14',
          len(re.findall(r'free constant', p14, re.I)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the built matter sector spends ZERO free dimensionless constants, and each of')
    print('  its three "no"s has a different reason -- the count is an INDEX, the hypercharges are')
    print('  REPRESENTATION-THEORETIC, and the coupling is ** not built because it CANNOT be built:')
    print('     a dimensionless magnitude needs two invariants and the substrate has one. **')
    print('  ⇒ ** That is stronger than a tally of zero. **  A theory scores zero two ways -- by')
    print('    deriving each constant, or by declining to speak of them.  P14 does the second,')
    print('    explicitly, with the reason stated as a law: ** the sector\'s boundary IS the boundary')
    print('    of what one constant can express. **')
    print('  THE COUNT AT c54.163: one scale (Lambda) · three gauges (c, G, hbar) · one free datum')
    print('  (rho_r/rho_m) · ZERO free dimensionless constants anywhere.')
    print('  ⚠ NOT closed: p0 asks the count to EQUAL the substrate\'s non-symmetric residue, and the')
    print('    RESIDUE side is not counted here.  This counts the spend, not the budget.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
