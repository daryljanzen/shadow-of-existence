#!/usr/bin/env python3
"""
L-81 — THE lambda SPECTRUM.  What turns a GRADING into a CONTENT -- and it does not.

L-78 computed: psi ~ r^(-lambda), advance omega^(-lambda) per wall crossing, so
triality = -lambda mod 3.  ** That fixes a grading on every mode of the tower and says
nothing about how many modes sit in each class. **  This asks the content question, and the
answer is a NEGATIVE that matters more than a positive would have.

  PART 1  Which lambda?  The angular Dirac spectrum on the leaf.
  PART 2  Normalizability at the wall -- and it hands back CHIRALITY = sign(lambda).
  PART 3  The tower, graded.  ** And it does not terminate. **
  PART 4  ** SO THE 12 + 3 COUNT IS NOT DELIVERED BY THE MODE SPECTRUM. **  Two
          independent countings that do not agree, stated as a conflict.
  PART 5  What P14 already said about this, which I should have read first.
  PART 6  What the negative is worth, and what it forecloses (nothing).

Run: python3 L81_the_lambda_spectrum.py     (sympy)
"""

from collections import defaultdict
import sympy as sp

print(__doc__.split("Run:")[0])
w3 = sp.exp(2 * sp.pi * sp.I / 3)

# =====================================================================
print("=" * 78)
print("PART 1 — WHICH lambda?")
print("=" * 78)
print("  P14's radial pair carries W = lambda sqrt(f)/r, with lambda the eigenvalue of the")
print("  angular Dirac operator on the cut's two-sphere.  That operator's spectrum is")
print("  standard and is not CR-specific: kappa = +-(j + 1/2) for j = 1/2, 3/2, 5/2, ...,")
print("  i.e. lambda = +-1, +-2, +-3, ..., with multiplicity 2|lambda|.")
print()
print(f"  {'|lambda|':>9} {'j':>6} {'multiplicity 2|lambda|':>24}")
for n in range(1, 7):
    print(f"  {n:>9} {str(sp.Rational(2*n-1,2)):>6} {2*n:>24}")
print()
print("  ** AND lambda = 0 IS EXCLUDED BY THE CONSTRUCTION, not by hand: W = 0 there, so")
print("     there is NO WALL and nothing to bind. **  The wall exists because lambda != 0.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — NORMALIZABILITY AT THE WALL, AND WHAT IT HANDS BACK")
print("=" * 78)
r, ell, lam = sp.symbols('r ell lambda', positive=True)
print("  From L-78: r ~ l^(2/3) near the wall, and psi ~ r^(-lambda) ~ l^(-2 lambda/3).")
print("  The leaf norm is int |psi|^2 dl, so the integrand near l = 0 goes as")
print()
expo = sp.Symbol('e')
print("     |psi|^2 dl  ~  l^(-4 lambda/3) dl     ->  converges iff -4 lambda/3 > -1")
print("                                          ->  ** lambda < 3/4 **")
print()
print("  ⇒ for lambda > 0 the branch exp(-int W) does NOT normalize at the wall, and the")
print("     CONJUGATE branch exp(+int W) ~ l^(+2 lambda/3) does.")
print("  ⇒ for lambda < 0 it is the other way round.")
print()
print(f"  {'lambda':>8} {'exp(-int W) ~':>16} {'normalizable?':>15} "
      f"{'the bound branch is':>22} {'chirality':>11}")
for lv in (1, 2, 3, -1, -2, -3):
    p1 = sp.Rational(-4 * lv, 3)
    ok1 = p1 > -1
    branch = 'chi_+  (exp -)' if ok1 else 'chi_-  (exp +)'
    chir = '+' if lv < 0 else '-'
    print(f"  {lv:>8} {'l^('+str(sp.Rational(-2*lv,3))+')':>16} {str(ok1):>15} "
          f"{branch:>22} {chir:>11}")
print()
print("  ** SO WHICH SPINOR BRANCH BINDS IS FIXED BY sign(lambda), AND THAT IS THE")
print("     CHIRALITY. **  P14 states the chirality is a definite sigma_y eigenvalue whose")
print("  sign is the sign of the signed-radius flip; here it comes out as sign(lambda),")
print("  which is a property of the ANGULAR problem.")
print("  ⇒ ** So the mode carries TWO gradings and both are read off lambda alone: **")
print("       chirality = sign(lambda)        [a Z_2]")
print("       triality  = -lambda mod 3       [a Z_3, from L-78]")
print("  ** and Z_2 x Z_3 = Z_6, which is the order of the corpus's own D_6 residue. **")
print("     (Recorded as a coincidence of orders, not an identification -- L-86.)")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TOWER, GRADED.  AND IT DOES NOT TERMINATE.")
print("=" * 78)
print(f"  {'lambda':>8} {'mult':>6} {'chirality':>11} {'triality':>10} {'class':>12}")
tally = defaultdict(int)
for lv in [x for n in range(1, 8) for x in (n, -n)]:
    mult = 2 * abs(lv)
    tri = (-lv) % 3
    cls = 'LEPTON' if tri == 0 else 'quark'
    tally[(tri, '+' if lv < 0 else '-')] += mult
    if abs(lv) <= 4:
        print(f"  {lv:>8} {mult:>6} {('+' if lv < 0 else '-'):>11} {tri:>10} {cls:>12}")
print("       ...        ...         ...        ...          ...")
print()
print("  ** THE SPECTRUM IS AN INFINITE TOWER AND NOTHING IN THE CONSTRUCTION TRUNCATES IT.")
print("     Both gradings are well defined on every rung, and every class is infinitely")
print("     occupied. **")
print()
print(f"  {'triality':>10} {'chirality':>11} {'states with |lambda| <= 7':>26}")
for (tri, ch), n in sorted(tally.items()):
    print(f"  {tri:>10} {ch:>11} {n:>26}")
print()
print("  ⚠ AND THE ONLY THING THAT COULD TRUNCATE IT IS NOT PRESENT.  P14 establishes the")
print("  leaf is COMPACT in the proper measure (finite total length), which makes the")
print("  spectrum DISCRETE.  ** Discrete is not finite. **  Compactness gives a countable")
print("  tower; it does not bound the angular quantum number.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — SO THE 12 + 3 IS NOT DELIVERED BY THE MODE SPECTRUM")
print("=" * 78)
print("  ** TWO INDEPENDENT COUNTINGS, AND THEY DO NOT AGREE. **")
print()
print(f"  {'':>22} {'counts':>10} {'what it counts':>44}")
for a, b, c in (("the LEG counting", "12 + 3",
                 "12 null legs (3 hinge x 2 horn x 2 handedness) + 3 walls"),
                ("the MODE counting", "infinite",
                 "one bound mode per angular eigenvalue lambda, mult 2|lambda|")):
    print(f"  {a:>22} {b:>10} {c:>44}")
print()
print("  ** THE LEG COUNTING IS A COUNT OF PLACES.  THE MODE COUNTING IS A COUNT OF STATES.")
print("     They are not the same question, and F-11 slid between them. **")
print()
print("  ⇒ ** F-11's 12 + 3 IS NOT REFUTED, BUT ITS STATUS CHANGES: it counts GEOMETRIC")
print("     SEATS, not field modes, and a seat carries a whole tower.  So the reading owes")
print("     a principle that selects one rung per seat -- and it does not have one. **")
print("  ⇒ AND THE HONEST SHAPE OF WHAT REMAINS: either")
print("       (a) something selects lambda (a lowest-mode principle, a boundary condition")
print("           at the horizons, or a truncation from the leaf's other end); or")
print("       (b) the tower IS the content and the Standard Model's 15 is the lowest level")
print("           of it, in which case the reading predicts an infinite family -- which is")
print("           either a signature or a fatality; or")
print("       (c) the legs and the modes are counting different things and only the")
print("           GRADING transfers, in which case the corpus gets colour/isospin/chirality")
print("           and does NOT get the multiplet count.")
print("  ** (c) is what the evidence currently supports, and it is weaker than F-11 claimed")
print("     and stronger than nothing.  L-87 splits the three. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT P14 ALREADY SAID, WHICH I SHOULD HAVE READ FIRST")
print("=" * 78)
for s in [
 "  'the index of Section sec:count counts WALLS, NOT PARTIAL WAVES.'",
 "  'The zero-mode is one Weyl mode per wall, NOT FIFTEEN; the index counts families, not",
 "   the states within them.'",
 "  'it returns one mode per wall PER INTERNAL STATE of that bundle.'",
]:
    print(s)
print()
print("  ** P14 SET THE PARTIAL-WAVE TOWER ASIDE EXPLICITLY, AND WAS RIGHT TO: it does not")
print("     carry the family count. **  What L-78 adds is that the tower it set aside is")
print("  ** exactly where the TRIALITY grading lives **.  So the thing P14 correctly")
print("  declined to read as families is the thing that carries colour.")
print()
print("  ⇒ THAT IS A REAL ADDITION AND IT IS ALSO A WARNING: P14 had already flagged that")
print("     the internal content sits 'on the far side of the gauge wall', and the leg")
print("     counting quietly walked back across it.  ** The paper's own boundary was")
print("     drawn correctly and a later reading crossed it without saying so. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT THE NEGATIVE IS WORTH, AND WHAT IT FORECLOSES")
print("=" * 78)
print("  ** WHAT STANDS, UNTOUCHED: **")
for s in ["the trichotomy and the twelve legs (geometry, proved)",
          "the wall = graze point = branch point identity (5/5, proved)",
          "the winding law and the thirds derivation (exact, conditional on closure)",
          "triality = -lambda mod 3 (computed on prop:wall's own solution)",
          "chirality = sign(lambda) (new here, and it is a second grading from one number)",
          "confinement as failure to close the lap (computed)"]:
    print("     · " + s)
print()
print("  ** WHAT IS WEAKER THAN IT WAS: **")
print("     · F-11's 12 + 3 read as a STATE count.  It is a SEAT count, and the step from")
print("       seats to states is missing.  ** Downgraded, not withdrawn. **")
print()
print("  ** AND WHAT THIS FORECLOSES: NOTHING. **  A missing selection principle is a gap in")
print("  a construction, not a verdict on it -- and the three ways out in PART 4 are all")
print("  live.  ** In particular (b) is not absurd: a graded infinite tower whose lowest")
print("  level reproduces one generation is what a Kaluza-Klein-like reading looks like,")
print("  and the corpus has never asked whether its tower has that shape. **  (L-88.)")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# NOTE ON SCOPE.  This receipt is a NEGATIVE: it forecloses nothing, and its citing sentence was
# narrowed at c54.26 for exactly that reason.  So what is pinned below is what it COMPUTES --
# the spectrum with its multiplicities, the normalizability exponent, the graded tally -- and
# NOT the ways-out of PART 4, which are stated and not chosen.
# (1) PART 1, the spectrum: |lambda| = n carries multiplicity 2n and sits at j = n - 1/2.
assert [2*n for n in range(1, 7)] == [2, 4, 6, 8, 10, 12]
assert [sp.Rational(2*n-1, 2) for n in range(1, 4)] == [sp.Rational(1,2), sp.Rational(3,2),
                                                        sp.Rational(5,2)]
# (2) PART 2, the normalizability exponent and the threshold it produces.  |psi|^2 dl goes as
#     l^(-4 lambda/3), which converges iff -4 lambda/3 > -1, i.e. lambda < 3/4.  So EVERY
#     positive integer lambda fails and every negative one passes: the bound branch, and hence
#     the chirality, is fixed by sign(lambda).  This is the receipt's one positive result.
_ok = {lv: (sp.Rational(-4*lv, 3) > -1) for lv in (1, 2, 3, -1, -2, -3)}
assert _ok == {1: False, 2: False, 3: False, -1: True, -2: True, -3: True}, _ok
assert sp.Rational(-4*1, 3) == sp.Rational(-4, 3) and sp.Rational(3, 4) > 0
assert all(not (lv < sp.Rational(3,4)) for lv in (1, 2, 3, 7)), "no positive integer lambda < 3/4"
# (3) PART 3, the graded tally actually printed -- triality = -lambda mod 3, chirality =
#     sign(lambda) -- summed over |lambda| <= 7.  All six (triality, chirality) classes are
#     occupied, which is the statement that the tower does not terminate in any class.
assert dict(tally) == {(0, '+'): 18, (0, '-'): 18, (1, '+'): 24,
                       (1, '-'): 14, (2, '+'): 14, (2, '-'): 24}, dict(tally)
assert sum(tally.values()) == 112 and len(tally) == 6
assert all(v > 0 for v in tally.values())
assert [(-lv) % 3 for lv in (1, 2, 3, 4, 5, 6)] == [2, 1, 0, 2, 1, 0]
# (4) PART 4, THE NEGATIVE ITSELF, computed rather than asserted: no truncation of the tower at
#     any |lambda| yields the leg count.  The cumulative state count over |lambda| <= n is
#     4, 12, 24, 40, 60, 84, 112 -- and 15 is not among them, so 12 + 3 is NOT delivered by the
#     mode spectrum at any cutoff.  ** This is the whole of the downgrade. **
_cum, _t = [], 0
for n in range(1, 8):
    _t += 2*(2*n)
    _cum.append(_t)
assert _cum == [4, 12, 24, 40, 60, 84, 112], _cum
assert 15 not in _cum and 12 in _cum
