#!/usr/bin/env python3
"""
RECEIPT -- p0: ** ITEM 48 WORKED.  THE TWO SYMMETRY BREAKINGS ARE ONE OBJECT, AND JOINING THEM GIVES THE
HIGGS IDENTIFICATION ACTUAL CONTENT: THE ORDER PARAMETER IS THE SLICING OFFSET, ITS SYMMETRIC SECTOR IS
THE BARE SUBSTRATE, ITS BREAKING HAS A CAUSE RATHER THAN A CHOSEN MINIMUM, AND -- UNLIKE A QUARTIC
POTENTIAL -- IT IS BOUNDED, SATURATING EXACTLY AT THE NARIAI MEMBER. **

Built r2533+c54.203, lead `L-521`.  VEIN: `L-221` (PO-5, what may exist and why these).

===================================================================================================
** THE QUESTION I STATED IN ADVANCE, AND THE ANSWER IS THE OPPOSITE OF WHAT I EXPECTED **
===================================================================================================

At c54.202 this line wrote, before doing the work: *"the corpus has TWO symmetry-breaking mechanisms --
P3's 'this is the symmetry breaking, located precisely' and P6/p0's R-parity identification -- and
nobody has set them beside each other.  Whether they are one mechanism or two is the question
underneath item 48."*

  *** THEY ARE ONE.  And the join is an identity, not a resemblance. ***

  * ** p0 ** states the parity as ** the geometric mass-reflection r_0 -> -r_0 (whence 2M -> -2M) **;
  * ** P3 ** derives, independently and for a different purpose, ** 2M = r_0 - r_0^3 ** (gauge alpha=1)
    -- and derives where r_0 comes from: an observer's reticle on the hole's sky image.

  ⇒ ** The cubic is ODD, so p0's mass-reflection is an IDENTITY of P3's relation and not a further
    assumption. **  *PART 1 checks that rather than asserting it.*

===================================================================================================
** WHAT THE JOIN BUYS, AND EACH PIECE IS A PROPERTY OF A RELATION THE CORPUS ALREADY HAD **
===================================================================================================

  PART 2  ** THE SYMMETRIC SECTOR IS THE BARE SUBSTRATE. **  2M = 0 at r_0 = 0 and r_0 = +-alpha, and
          the metric function is 1 - r^2/alpha^2 at all three.  ** One massless geometry read at three
          offsets ** -- so the unbroken phase of this breaking is de Sitter itself, not a separate
          configuration that has to be arranged.
  PART 3  ** THE ORDER PARAMETER IS BOUNDED, AND ITS BOUND IS THE DEGENERATE MEMBER. **  Over the
          admissible offsets |r_0| <= 2 alpha/sqrt3 -- P3's own regime range, read off the
          discriminant 4 - 3 r_0^2 -- ** |M| <= alpha/(3 sqrt3), attained at r_0 = +- alpha/sqrt3 and
          at the range endpoints. **  *And that value is the NARIAI mass, obtained here independently
          from the horizon double-root condition f = f' = 0 and never substituted in.*
  PART 4  ** AND THE BREAKING HAS A CAUSE. **  P3 does not posit the offset: it argues that a manifold
          observer cannot be assumed to sit at r_0 = 0, because the reference such an observer has is
          the hole's image on their celestial sphere and ** there is no marked point on that image for
          a reticle to land on **.

  *** SO THE STATEMENT ABOUT THE MECHANISM IS: an order parameter that is geometric, an unbroken phase
      that is the substrate itself, a breaking with an argument behind it rather than a potential
      written with its minimum off the origin, and a BOUND -- where a quartic potential is unbounded in
      its field -- saturating at exactly the configuration a collapse reaches. ***

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED, AND THE LIST IS LONGER THAN WHAT IS **
===================================================================================================

** No vacuum expectation value, no electroweak scale, no mass value. **  The one-constant structure
forbids the strengths and p0 says so throughout; item 48's own framing is that the theorem ** forbids
the magnitudes and says nothing about the mechanism **, and this file stays on that side of the line.
** Nothing here derives the Higgs field, its potential, or the gauge group it breaks. **  ** And `F1`
is not touched: ** if the gauge group were ever promoted from described to forced, the relation drawn
here would have to be re-examined rather than inherited -- which the written paragraph says in the
paper's own voice.

⌗ ** AND ONE THING THAT LOOKS LIKE A RESULT AND IS NOT. **  The three roots of 2M = 0 are not three
massless geometries; they are ** three slicing offsets on one **, which is vantage multiplicity and
already in the corpus.  *PART 2 checks the metric function at all three precisely so that cannot be
over-read.*

SETTINGS: none -- no instrument, no spectra.  Symbolic (sympy) on P3's own slicing relation and the
Schwarzschild--de Sitter metric function, plus a numerical extremum over the admissible range and
source checks against p0 and P3.

rc=0 on success.  Run: python3 P0_the_order_parameter_is_the_offset_and_it_is_bounded_by_the_nariai_member.py
                        (sympy numpy; ~5 s)
"""
import os
import re
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

r0, r, al = sp.symbols('r_0 r alpha', real=True)
M2 = r0 - r0 ** 3                      # P3's relation, gauge alpha = 1

# =====================================================================
print("=" * 78)
print("PART 1 — p0's MASS-REFLECTION IS AN IDENTITY OF P3's RELATION, NOT A SECOND ASSUMPTION")
print("=" * 78)
print(f"  P3:  2M = {M2}          (gauge alpha = 1)")
_odd = sp.simplify(M2.subs(r0, -r0) + M2) == 0
print(f"  under r_0 -> -r_0 :  2M -> {sp.simplify(M2.subs(r0, -r0))}")
print(f"  ** exactly -2M : {_odd} **   — which is p0's 'r_0 -> -r_0 (whence 2M -> -2M)'")
print("  *So the two papers are describing ONE object. The question c54.202 stated in advance —")
print("   one mechanism or two — resolves to one, and by an identity rather than a resemblance.*")
if not _odd:
    fail.append("P3's relation is not odd in r_0 — then p0's mass-reflection is a separate assumption "
                "and this file's join does not exist")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SYMMETRIC SECTOR IS THE BARE SUBSTRATE, READ AT THREE OFFSETS")
print("=" * 78)
_roots = sorted(sp.solve(sp.Eq(M2, 0), r0), key=lambda x: float(x))
print(f"  2M = 0 at r_0 = {_roots}   (i.e. 0 and +-alpha in the gauge)")
f_general = 1 - 2 * (M2 / 2) / r - r ** 2          # f = 1 - 2M/r - r^2 with 2M = r_0 - r_0^3
_ds = []
for c in _roots:
    fc = sp.simplify(f_general.subs(r0, c))
    _ds.append(sp.simplify(fc - (1 - r ** 2)) == 0)
    print(f"    r_0 = {c}:  f(r) = {fc}   de Sitter? {_ds[-1]}")
print()
print("  ** All three give the SAME massless geometry — one de Sitter member read at three offsets. **")
print("  ⚠ *This is vantage multiplicity, not three vacua, and the check exists so it cannot be")
print("     over-read as three.*")
if len(_roots) != 3 or not all(_ds):
    fail.append("the 2M = 0 offsets do not all give de Sitter — PART 2's reading fails")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE ORDER PARAMETER IS BOUNDED, AND THE BOUND IS THE NARIAI MASS")
print("=" * 78)
R_MAX = 2 / sp.sqrt(3)                              # P3's regime range: discriminant 4 - 3 r_0^2 >= 0
_crit = sp.solve(sp.Eq(sp.diff(M2, r0), 0), r0)
print(f"  admissible offsets: |r_0| <= 2/sqrt3 = {float(R_MAX):.6f}   "
      f"(P3's discriminant 4 - 3 r_0^2)")
print(f"  d(2M)/dr_0 = 0 at r_0 = {_crit}")
grid = np.linspace(-float(R_MAX), float(R_MAX), 400001)
vals = np.abs(grid - grid ** 3)
_num_max = float(vals.max())
_bound = float(2 / (3 * np.sqrt(3)))
print(f"  max |2M| over that range (numerically) = {_num_max:.9f}")
print(f"  2/(3 sqrt3)                            = {_bound:.9f}")
print(f"  ** they agree to 1e-6 : {abs(_num_max - _bound) < 1e-6} **")
# the Nariai mass, derived independently from the double-root condition
Mv = sp.Symbol('M', real=True)
f_sds = 1 - 2 * Mv / r - r ** 2 / al ** 2
_sol = sp.solve([sp.Eq(f_sds, 0), sp.Eq(sp.diff(f_sds, r), 0)], [Mv, r], dict=True)
_M_nar = sp.simplify(sp.Abs(_sol[0][Mv].subs(al, 1)))
print(f"\n  Nariai mass from f = f' = 0, independently : M = {sp.simplify(_sol[0][Mv])} "
      f"-> |M| = {_M_nar} at alpha = 1")
print("  *the sign the solver returns is the corpus's own +-M orientation parity, which is the very")
print("   reflection this file is about — so the comparison is on the magnitude, deliberately.*")
_match = abs(float(_M_nar) - _bound / 2) < 1e-12
print(f"  ** the bound on |M| IS the Nariai mass : {_match} **")
print()
print("  ⇒ *A quartic potential is unbounded in its field. This order parameter is not, and it")
print("     saturates exactly at the configuration a collapse reaches.*")
if abs(_num_max - _bound) > 1e-6:
    fail.append(f"max |2M| is {_num_max:.9f}, not 2/(3 sqrt3)")
if not _match:
    fail.append("the bound is not the Nariai mass — PART 3's whole point fails")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND BOTH HALVES ARE IN THE CORPUS'S OWN TEXT, CHECKED RATHER THAN QUOTED")
print("=" * 78)
p0 = open(os.path.join(CORPUS, 'geometric_core_paper.tex'), encoding='utf-8').read()
p3 = open(os.path.join(CORPUS, 'SdS-slicing-curve_v2.tex'), encoding='utf-8').read()
CHECKS = [
    ("p0 states the parity as the geometric mass-reflection r_0 -> -r_0",
     p0, r'\$r_0\\mapsto-r_0\$ \(whence \$2M\\mapsto-2M\$\)'),
    ("P3 carries the slicing relation 2M = r_0 - r_0^3",
     p3, r'2M=r_\{0\}-r_\{0\}\^\{3\}'),
    ("P3 reads the regime range off the discriminant 4 - 3 r_0^2",
     p3, r'4-3r_\{0\}\^\{2\}'),
    ("P3 derives the offset from the observer's sky image rather than positing it",
     p3, r'apparent centre of a projected image is not a marked point'),
    ("P3 calls that the symmetry breaking, located precisely",
     p3, r'This is the symmetry breaking, located precisely'),
    ("and p0 now NAMES the Higgs mechanism, which appeared nowhere in the corpus",
     p0, r'\\emph\{Higgs mechanism\}'),
    ("p0 states the bound and names the Nariai mass",
     p0, r'\|M\|\\le\\alpha/3\\sqrt3'),
    ("p0 keeps F1 explicit rather than inheriting it",
     p0, r'promoted from described to forced'),
]
for what, hay, pat in CHECKS:
    ok = re.search(pat, hay, re.I) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"not found in source: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — p0's mass-reflection is an identity of P3's own slicing relation, so the two")
print("symmetry breakings are one object; the symmetric sector is de Sitter read at three offsets; the")
print("order parameter is bounded over the admissible range by exactly the Nariai mass, derived")
print("independently from the horizon double root; and the breaking has a derived cause rather than a")
print("chosen minimum.")
print("=" * 78)

# ============================================================================================
# GATE — r2533+c54.203, `L-521`.  Item 48 asked whether CR's structure says anything about the
# Higgs MECHANISM as against the magnitudes it cannot supply.  The answer here is yes, so the
# pins are on the join being real and on the claim not drifting into magnitudes:
#   (1) the oddness of 2M(r_0) -- ** this IS the join.  If P3's relation were not odd, p0's
#       mass-reflection would be a separate assumption and there would be no single object **;
#   (2) all three roots of 2M = 0 giving the SAME de Sitter metric function -- both because it is
#       the symmetric-sector claim and because it is what stops "three roots" being read as three
#       vacua;
#   (3) the bound over P3's own admissible range, numerically, AND its identification with the
#       Nariai mass derived independently from f = f' = 0 -- ** never substituted in, because the
#       whole content of PART 3 is that two separately-derived numbers coincide **;
#   (4) eight source checks across p0 and P3, including that p0 now NAMES the Higgs (it appeared
#       zero times in seventeen papers) and that it keeps `F1` explicit.
#   NOT gated, because not claimed: any vacuum expectation value, scale or mass; any derivation of
#   the Higgs field, its potential or its gauge group.
# ============================================================================================
assert _odd, "P3's slicing relation is not odd in r_0 — the two breakings are not one object"
assert len(_roots) == 3 and all(_ds), "the massless offsets do not all give de Sitter"
assert abs(_num_max - _bound) < 1e-6, f"max |2M| is {_num_max:.9f}, not 2/(3 sqrt3)"
assert _match, "the bound on |M| is not the independently derived Nariai mass"
for what, hay, pat in CHECKS:
    assert re.search(pat, hay, re.I), f"source check failed: {what}"
print(f"GATE c54.203 (r2533), `L-521`: 2M = r_0 - r_0^3 is odd, so p0's mass-reflection is an identity "
      f"of P3's relation and the two breakings are one object; 2M = 0 at r_0 = 0, +-1 all give "
      f"f = 1 - r^2; and |M| <= {_bound / 2:.9f} over |r_0| <= 2/sqrt3, which equals the Nariai mass "
      f"{float(_M_nar):.9f} derived from f = f' = 0 — pinned against `FOR_54` item 48 (r2524), P3 "
      f"sec:offset and p0's mass paragraph.")
