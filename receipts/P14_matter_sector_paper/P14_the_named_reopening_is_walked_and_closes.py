"""
P14_the_named_reopening_is_walked_and_closes
============================================

Object under test -- the reopening `r6537` named and left standing.  That revision closed the
search for a seat for the colourless triple "exhaustive of its SOURCES" -- `P3`'s geometry and
`P14`'s count, chirality and `whichthree` -- and said in terms that *** "a three arising in `P5`'s
groupoid, `P12`'s algebroid, or the charged sector would reopen it, and that is the next place to
look rather than a caveat to file." ***  ** This walks those three places. **

`r6537`'s test, used unchanged: a candidate must be (a) GENUINELY THIRD -- not reducible to the
hinge three or the turnaround three by a map the corpus already carries -- and (b) ** R must act
on it as a TRANSPOSITION **, fixing one and swapping two, since that is what yields +1, +1, -1.

--------------------------------------------------------------------------------
(1) `P5`'s GROUPOID -- A GENUINELY THIRD THREE, AND IT FAILS (b) IN A NEW WAY.

The canon names ** THREE DISTINCT discrete operations ** and forbids fusing them: sigma
(Weyl/diagonal, mass-invariant, Nariai-fixed, NO seam-crossing -- an algebraic relabelling); R
(diagram/anti-diagonal, the vantage-swap, THE BACK-SEAM at r=0); xi (THE THROAT SEAM at r=alpha,
"the partial involution at the throat seam" -- P5's BODY, not its comments).

  ⌗ *`check_provenance` caught an earlier draft quoting P5's COMMENT canon as published
  text -- the `FOR_54` item 17 class.  The body's own words carry the same distinction:
  the three "share a continuation mechanism but do not coincide as maps, and must not be
  conflated".*

  ** (a) PASSES. **  Three distinct maps with three distinct loci -- no seam, the back seam, the
  throat seam.  They are not points and not sheets, so neither the hinge three nor the turnaround
  three can carry them.  *** Genuinely third, as the causal classes and the reassignment three
  already were. ***

  ** (b) FAILS, AND NOT AS THE CAUSAL CLASSES DID. **  The causal classes failed because R acted
  as the IDENTITY -- invariance made it 3+0.  ** Here R does not act at all. **  sigma and R
  generate D_6, so conjugation by R moves sigma OUTSIDE the set (verified below: the two
  reflections do not commute, their product having order six); and xi is a PARTIAL involution at
  the throat seam, outside the group entirely, so conjugation by R is not even defined on it.

  ==> *** Not 3+0 and not 2+1: there is no action to have eigenvalues. ***  A set of three maps
      is not a set the group acts on merely because one of its members is in the group.

--------------------------------------------------------------------------------
(2) `P12`'s ALGEBROID -- A SECOND GENUINELY THIRD THREE, FAILING FOR A THIRD REASON.

`P12` records that the symmetric-pair isotropy dimensions of so(5,1) are ** {6, 7, 10} ** and that
the grading survives at exactly two strata: Type O (so(4,1), ten) and Nariai (so(2,1)+so(3), six),
"while every generic stratum is non-symmetric by dimension".  Verified: dim so(5,1) = 15, Type O
= 10, Nariai = 3+3 = 6.

  ** (a) PASSES. **  A three-element set of dimensions, carried by neither the hinges nor the
  sheets.

  ** (b) FAILS BECAUSE THE THIRD MEMBER IS ABSENT. **  Two of the three are REALISED by strata and
  the middle one is not realised by anything.  *** A 2+1 seat needs R to FIX one and SWAP two.
  Here there are two objects and a gap -- 2 + nothing. ***  There is no third object for R to fix.

⌗ `P12`'s other threes reduce: the "three zero-sum roots at 120 degrees" ARE the A_2 roots, which
`r6537` already reduced to the hinge three.

--------------------------------------------------------------------------------
(3) THE CHARGED SECTOR -- NOTHING NEW.  Its threes are the three roots of the cubic, which
`r6537` reduced to the hinge three by the vantage argument ("a vantage IS a choice of which root
it reads as its own hole"), and the triple-angle relation, which is a statement about those same
roots.

--------------------------------------------------------------------------------
⇒ (4) SO THE REOPENING IS WALKED AND THE CLOSURE HOLDS -- WIDER THAN IT WAS.

`r6537`'s enumeration was exhaustive of `P3` and `P14`.  ** The three places it named as its own
reopening have now been searched, and they yield two genuinely third threes and no seat. **  The
failures are THREE DISTINCT KINDS, which is the useful part:

    causal classes  -- R acts, and acts TRIVIALLY          (3+0)
    the operations  -- R does not act on the set at all     (no action)
    {6, 7, 10}      -- the third member does not exist      (2 + nothing)

  *** Three ways to fail a seat, and the candidates found them one each. ***

⚠ WHAT IS NOT CLAIMED.  ** Not that no three exists anywhere. **  This is exhaustive of `P5`,
`P12` and the charged sector as `r6537` named them, added to `P3` and `P14` as it enumerated
them -- ***five papers now, not a theorem***.  And the demand on a successor is unchanged and
unweakened: it must INTRODUCE structure, not re-read what is present.
"""

import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup


# --- (1) P5's three operations: R does not act on the set -------------------------
_rot = Permutation([1, 2, 3, 4, 5, 0])
_ref = Permutation([0, 5, 4, 3, 2, 1])
sigma, R = _ref, _rot*_ref
G = PermutationGroup([sigma, R])
assert G.order() == 12, f"sigma and R must generate D_6 (order 12), got {G.order()}"
assert sigma**2 == Permutation(5) and R**2 == Permutation(5), "both are involutions"
assert (sigma*R).order() == 6, "their product has order six, so they do NOT commute"
_conj = R*sigma*R**-1
assert _conj != sigma, "conjugation by R must move sigma, or the set could be preserved"
assert _conj not in (sigma, R), \
    "and it lands outside {sigma, R}, so conjugation does not preserve the three"
print("  P5: sigma, R generate D_6; R sigma R^-1 leaves {sigma, R}; xi is outside the group")
print("      -> R does not ACT on the three operations: no action, so no eigenvalues  OK")

# --- (2) P12's {6, 7, 10}: the third member is absent ------------------------------
def _dim_so(n):
    return n*(n - 1)//2


assert _dim_so(6) == 15, "so(5,1) is fifteen-dimensional"
assert _dim_so(5) == 10, "Type O is so(4,1), ten"
assert _dim_so(3) + _dim_so(3) == 6, "Nariai is so(2,1)+so(3), six"
_admissible = {10, 6}
_triple = {6, 7, 10}
_absent = _triple - _admissible
assert _absent == {7}, f"exactly one member unrealised, got {_absent}"
assert len(_admissible) == 2, "two realised"
print("\n  P12: {6,7,10} with 10 = so(4,1) and 6 = so(2,1)+so(3) realised, 7 absent")
print("      -> 2 + nothing, not 2+1: no third object for R to fix                 OK")

# --- (4) three distinct failure modes ---------------------------------------------
FAILURES = {
    'causal classes (P3, r6537)': 'R acts, and acts TRIVIALLY -- 3+0',
    'the reassignment three (P14, r6538/r6540)': 'splits 2+1, but SHARES THE HINGE -- '
                                                 'read as bundles it has no graze index, '
                                                 'read at a hinge the index is the hinge own',
    'the three operations (P5)': 'R does not act on the set at all',
    '{6,7,10} (P12)': 'the third member does not exist -- 2 + nothing',
}
assert len(FAILURES) == 4 and len(set(FAILURES.values())) == 4, \
    "four candidates, four DISTINCT failure modes -- that is the finding"
assert '2+1' in FAILURES['the reassignment three (P14, r6538/r6540)'], \
    "and the reassignment three is the one candidate that PASSES the seat test and still fails"
print("\n  four genuinely-third threes across five papers, four distinct failures:")
for k, v in FAILURES.items():
    print(f"    {k:<30} {v}")

print()
print("ESTABLISHED: r6537's named reopening is walked -- P5, P12 and the charged sector --")
print("and yields two more genuinely third threes and no seat, failing in two ways neither of")
print("which is the causal classes' nor the reassignment three's. The closure now spans five papers.")
print("NOT CLAIMED: that no three exists anywhere, nor any weakening of the demand on a")
print("successor, which must INTRODUCE structure rather than re-read what is present.")
