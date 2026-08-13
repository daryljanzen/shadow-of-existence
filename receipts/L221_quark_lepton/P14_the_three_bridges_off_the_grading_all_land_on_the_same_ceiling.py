#!/usr/bin/env python3
"""
RECEIPT -- P14 / `PO-5`: ** ITEMS A3, A4, A5 WORKED TOGETHER, AND THEY ANSWER ONE QUESTION.  THE THREE
NAMED ALTERNATIVES TO `BE A KERNEL' -- COHOMOLOGY, REPRESENTATION BRANCHING, SPECTRAL PROJECTION --
FAIL IN THREE DIFFERENT WAYS AND ⛭⛭ *** ALL THREE TERMINATE AT DIMENSION 2 ***.  SO THE OBSTRUCTION IS
THE SIZE OF THE DISCRETE RESIDUE AND NOT THE CHOICE OF BRIDGE. **

Built r2566+c54.207, lead `L-534`.  VEIN: `L-221` (PO-5, what may exist and why these).

===================================================================================================
** ⛭ A3 -- COHOMOLOGY IS NOT AN ALTERNATIVE TO THE KERNEL.  ON A Z2 GRADING IT *IS* THE KERNEL. **
===================================================================================================

*The route reads: "a complex whose degree is the grading."*  ** A complex needs a differential: an
operator ODD for the grading with d^2 = 0. **

  * ** ODD is available. **  {gamma^mu, gamma^5} = 0, so D = gamma^mu nabla_mu is odd.  *(PART 1)*
  * ** NILPOTENT is not, and the reason is what a Clifford module is. **  D(p)^2 = p^2 * 1 -- an odd
    operator on a Clifford module squares to ** THE METRIC **, not to zero.  *(PART 1)*
  * ⇒ *So a Z2-graded complex on this bundle either does not exist, or one of its two maps is set to
    zero.*  ** And the two-term complex that remains, 0 -> S_+ -> S_- -> 0, has cohomology
    ker (+) coker -- whose Euler characteristic is the graded index. **

  ⇒ *** COHOMOLOGY ON A TWO-TERM GRADING IS THE KERNEL ROUTE WEARING A DIFFERENT NAME, AND INHERITS
      ITS OBSTRUCTION EXACTLY.  A3 IS NOT A DISTINCT CANDIDATE. ***
  ⌗ *And this explains an absence rather than merely recording one: the corpus contains no differential
   anywhere in seventeen papers, which had looked like a gap in its machinery.  ** On a Z2 grading there
   is nothing for a complex to be. **

===================================================================================================
** A5 -- BRANCHING RETURNS A CHARACTER, BECAUSE R GRADES AND DOES NOT EXCHANGE **
===================================================================================================

*The route reads: "the grading labels irreps."*  ** For a Z2 to contribute DIMENSION rather than a
label it must PAIR two irreps of the connected part into one; if it fixes them, it contributes a sign
and nothing else. **

  * ** AND THE CORPUS ALREADY SETTLED WHICH ONE R IS, FOR ANOTHER PURPOSE: **  *"it does not EXCHANGE
    the two chirality eigenspaces but GRADES them"* (P13).  ⇒ ** R fixes.  So R contributes a
    character. **
  * ** AND A CHARACTER IS ONE-DIMENSIONAL ** -- which is P14's own stated ceiling, here reached for R
    rather than asserted for the deck.
  * ** THE RESIDUE'S OWN CEILING, COMPUTED: **  D_6 = S_3 x Z_2.  S_3 has three classes and order six,
    so its irreducible dimensions are 1, 1, 2; tensoring with Z_2's two characters gives 1,1,2 twice.
    ⇒ *** MAX IRREDUCIBLE DIMENSION OF THE SUBSTRATE'S DISCRETE RESIDUE = 2. ***  *(PART 2)*

  ⇒ *** A BRANCHING BRIDGE CARRIES A LABEL AND, AT MOST, A DOUBLET. ***

===================================================================================================
** A4 -- THE ONLY ONE NOT CLOSED STRUCTURALLY, AND IT RETURNS A DOUBLET TOO **
===================================================================================================

*The route reads: "a band rather than a zero mode."*  ** A band projection is canonical only if some
gap is distinguished; otherwise WHICH band is an unforced parameter -- a modulus in the excluding
sense, which the programme's own Rule 2 rejects. **

  * ** THE SPECTRUM IS UNIFORMLY SPACED. **  The angular Dirac eigenvalues on the cut's two-sphere are
    lambda = +-1, +-2, ... with multiplicity 2|lambda|; every consecutive gap within a sign branch is
    ** 1 **, so no gap is distinguished by size.  *(PART 3)*
  * ** BUT ONE RUNG IS DISTINGUISHED, AND BY THE CONSTRUCTION RATHER THAN BY THE SPECTRUM: **
    lambda = 0 is excluded because W = 0 there and there is no wall, so the tower has a LOWEST
    admissible rung and "the lowest" is a forced choice rather than a chosen one.
    ⇒ ** So the principle the routed receipt said this reading OWES is available after all. **
  * ⇒ *** AND AT THAT RUNG THE MULTIPLICITY IS 2|lambda| = 2. ***

  ⇒ ** So A4 survives as a bridge and delivers a graded doublet per wall. **  *The reading is no longer
   owed a principle; it is owed a content, and the number it has to beat is now stated.*

===================================================================================================
** ⛭⛭ AND THE THREE ARRIVE AT ONE NUMBER, WHICH IS THE FINDING **
===================================================================================================

  A3 -> the index (a count, dimension 0 of content)   A5 -> a character, at most a doublet
                       A4 -> a doublet

  ⇒⇒ *** THE OBSTRUCTION IS NOT THE CHOICE OF BRIDGE.  IT IS THAT THE DISCRETE RESIDUE IS TOO SMALL:
      D_6's largest irrep is two-dimensional and the lowest angular rung's multiplicity is two, and a
      Standard Model generation is fifteen Weyl states.  Three independent routes hit the same wall
      from three sides. ***
  ⌗ *P14 states this ceiling for the deck Z_3 and states it as a property of characters.  ** What is
   added is that it is not the deck's ceiling but the residue's, and that the two other routes off the
   grading do not get past it either. **

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that `PO-5` is closed. **  *The fourth candidate -- the ANOMALY route, held back as `A6` -- is
untested here and nothing above bears on it.*  ** Not that no bridge exists **: what is shown is that
three named ones terminate, not that the space of bridges is exhausted.  ** Not that the doublet is
useless ** -- a two-dimensional irrep is exactly the shape weak isospin would want, and P14 declines
that identification on separate grounds which this file does not touch.  ** Not any new physics **:
every ingredient is the corpus's own or standard representation theory.

⚠ ** AND A4'S SURVIVAL IS THE PART MOST EASILY OVER-READ. **  *Finding the canonical rung REMOVES an
owing and does not supply a content.  The tower reading is now testable rather than blocked, and what
it returns at the canonical rung is 2.*

SETTINGS: none -- no instrument, no spectra.  Explicit Dirac matrices, the Clifford square computed
symbolically, the S_3 irreducible dimensions solved from the class equation rather than quoted, the
angular spectrum's gaps measured, and source checks.

rc=0 on success.  Run: python3 P14_the_three_bridges_off_the_grading_all_land_on_the_same_ceiling.py
                        (sympy; ~10 s)
"""
import itertools
import os
import re
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

# =====================================================================
print("=" * 78)
print("PART 1 — A3: ODD IS AVAILABLE, NILPOTENT IS NOT, AND THAT IS WHAT A CLIFFORD MODULE IS")
print("=" * 78)
I2, Z2 = sp.eye(2), sp.zeros(2, 2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])


def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


g = [blk(I2, Z2, Z2, -I2)] + [blk(Z2, s, -s, Z2) for s in (sx, sy, sz)]
g5 = sp.I * g[0] * g[1] * g[2] * g[3]
_g5sq = sp.simplify(g5 * g5) == sp.eye(4)
_odd = all(sp.simplify(g[m] * g5 + g5 * g[m]) == sp.zeros(4, 4) for m in range(4))
_mass_even = sp.simplify(sp.eye(4) * g5 - g5 * sp.eye(4)) == sp.zeros(4, 4)
print(f"  gamma5^2 = 1                          : {_g5sq}   ** the grading is a Z2, not longer **")
print(f"  {{gamma^mu, gamma5}} = 0 for every mu    : {_odd}   ** so D is ODD -- the first requirement holds **")
print(f"  [m*1, gamma5] = 0                     : {_mass_even}   ** the mass term is not an odd OPERATOR **")

p = sp.symbols('p0:4')
eta = sp.diag(1, -1, -1, -1)
Dp = sp.zeros(4, 4)
for m in range(4):
    Dp = Dp + g[m] * p[m] * eta[m, m]
D2 = sp.simplify(Dp * Dp)
_sq = sp.simplify(D2[0, 0])
_nilpotent = D2 == sp.zeros(4, 4)
print()
print(f"  D(p)^2 = ({_sq}) * 1")
print(f"  D^2 == 0 identically                  : {_nilpotent}")
print("  *** AN ODD OPERATOR ON A CLIFFORD MODULE SQUARES TO THE METRIC, NOT TO ZERO. ***")
print()
print("  ⇒ so a Z2-graded complex here either does not exist, or one of its two maps is zeroed --")
print("     and the two-term complex 0 -> S_+ -> S_- -> 0 has cohomology ker (+) coker,")
print("     ** whose Euler characteristic is the graded index.  A3 IS THE KERNEL ROUTE. **")
if not _odd:
    fail.append("gamma^mu does not anticommute with gamma5 — A3's first requirement is misstated")
if _nilpotent:
    fail.append("D^2 vanishes identically — the whole A3 argument inverts and a complex DOES exist")
if not _g5sq:
    fail.append("the grading is not an involution — 'two-term' is the wrong shape")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — A5: THE RESIDUE'S LARGEST IRREDUCIBLE REPRESENTATION, SOLVED NOT QUOTED")
print("=" * 78)
from sympy.combinatorics import SymmetricGroup

S3 = SymmetricGroup(3)
_ncl, _ord = len(S3.conjugacy_classes()), S3.order()
_sols = [t for t in itertools.combinations_with_replacement(range(1, _ord + 1), _ncl)
         if sum(x * x for x in t) == _ord and min(t) == 1]
print(f"  S_3 : order {_ord}, {_ncl} conjugacy classes")
print(f"  the class equation sum d_i^2 = |G| over {_ncl} irreps has solutions: {_sols}")
_maxS3 = max(max(t) for t in _sols)
print(f"  ** irreducible dimensions of S_3 : {list(_sols[0])}  -> max {_maxS3} **")
print(f"  D_6 = S_3 x Z_2 : irreps are (S_3 irrep) (x) (Z_2 character), so {list(_sols[0])} twice over")
print(f"  *** MAX IRREDUCIBLE DIMENSION OF THE SUBSTRATE'S DISCRETE RESIDUE = {_maxS3} ***")
print()
print("  ⇒ and R is the Z_2 factor, which the boundary paper shows GRADES rather than EXCHANGES,")
print("     ** so R contributes a character and no dimension: a branching returns a label, and the")
print("        largest multiplet anywhere in the residue is a doublet. **")
if len(_sols) != 1 or _maxS3 != 2:
    fail.append(f"S_3's irreducible dimensions came out {_sols} — the residue's ceiling is not 2")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — A4: THE SPECTRUM IS UNIFORM, SO ONLY THE LOWEST RUNG IS CANONICAL")
print("=" * 78)
LAM = [l for l in range(-8, 9) if l != 0]
MULT = {l: 2 * abs(l) for l in LAM}
print(f"  lambda       : {LAM}")
print(f"  multiplicity : {[MULT[l] for l in LAM]}    ** 2|lambda| **")
_gaps = sorted({abs(LAM[i + 1] - LAM[i]) for i in range(len(LAM) - 1) if LAM[i] * LAM[i + 1] > 0})
print(f"  consecutive gaps within a sign branch : {_gaps}")
print("  ** UNIFORM -> no gap is distinguished by size, so 'which band' would be an unforced")
print("     parameter, and Rule 2 rejects exactly that. **")
print()
_lowest = min(abs(l) for l in LAM)
print(f"  ⛭ but lambda = 0 is excluded BY THE CONSTRUCTION (W = 0 there, hence no wall),")
print(f"     so the tower has a lowest admissible rung |lambda| = {_lowest}, and 'the lowest' is forced.")
print(f"  *** ITS MULTIPLICITY IS {MULT[_lowest]}. ***")
print("  ⇒ *So A4 survives structurally and returns a doublet.  The owing is discharged and the")
print("     content is measured.*")
if _gaps != [1]:
    fail.append(f"the angular gaps are {_gaps}, not uniform — the no-distinguished-band argument fails")
if MULT[_lowest] != 2:
    fail.append(f"the lowest rung's multiplicity is {MULT[_lowest]}, not 2")

print()
print("=" * 78)
print("  ⇒⇒ THE THREE ROUTES:  A3 -> the index    A5 -> at most a doublet    A4 -> a doublet")
print(f"  *** ALL THREE TERMINATE AT {_maxS3}.  A Standard Model generation is fifteen Weyl states. ***")
print("=" * 78)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE PREMISES, IN THE CORPUS'S OWN TEXT")
print("=" * 78)
TEX = {fn: open(os.path.join(CORPUS, fn), encoding='utf-8', errors='replace').read()
       for fn in ('matter_sector_paper.tex', 'boundary_paper.tex', 'geometric_core_paper.tex')}
PREMISES = [
    ("⛭ P13: R GRADES the chirality eigenspaces rather than exchanging them — A5's whole hinge",
     'boundary_paper.tex', r'does not \\emph\{exchange\} the two chirality eigenspaces but \\emph\{grades\} them'),
    ("P13: and R lies outside the connected component",
     'boundary_paper.tex', r'\\mathrm\{O\}\(5,1\)\\setminus\\mathrm\{SO\}_0|\\O\(5,1\)\\setminus\\SO_0'),
    ("P14: the residue is D_6 = S_3 x Z_2",
     'matter_sector_paper.tex', r'D_6=S_3\\times\\mathbb\{Z\}_2'),
    ("P14: a character is one-dimensional — the ceiling this file generalises",
     'matter_sector_paper.tex', r'a character is one-dimensional: it labels and it does not\s*\n?multiplet'),
    ("P14: the angular tower is infinite and lambda fixes a grading and not a content",
     'matter_sector_paper.tex', r'\\lambda\$ fixes a \\emph\{grading\} and not a \\emph\{content\}'),
    ("P14: and lambda enters through W = lambda sqrt(f)/r, which is why lambda = 0 has no wall",
     'matter_sector_paper.tex', r'W\(r\)=\\frac\{\\lambda\\sqrt\{f\}\}\{r\}'),
    ("P14: the zero-mode operator is the Jackiw--Rebbi one, so the kernel route is the standing one",
     'matter_sector_paper.tex', r'H=-i\\sigma_x\\partial_x'),
]
for what, fn, pat in PREMISES:
    ok = re.search(pat, TEX[fn], re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"a premise is not in the corpus: {what} [{fn}]")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND WHAT P14 NOW SAYS")
print("=" * 78)
P14 = TEX['matter_sector_paper.tex']
WRITTEN = [
    ("the ceiling is attributed to the residue rather than to the deck",
     r'the ceiling is not a feature of the deck alone'),
    ("⛭ the Z2-complex identity is stated",
     r'cohomology is not an alternative to the kernel; it is the kernel'),
    ("with the Clifford reason given",
     r'square to the metric rather\s*\n?than to zero'),
    ("the grading-not-exchanging property is used and cited across",
     r'\\emph\{grades\} them~\\cite\{JanzenBoundary\}'),
    ("the residue's irreducible dimensions are given",
     r'irreducible dimensions \$1,1,2\$ twice over'),
    ("the spectral route's uniform spacing is stated",
     r'is uniformly spaced so that no gap is distinguished'),
    ("the canonical rung and its multiplicity are given",
     r'whose multiplicity\s*\n?is \$2\\lvert\\lambda\\rvert=2\$'),
    ("and the joint conclusion is that the residue's size is the obstruction",
     r'the obstruction is the size of the discrete\s*\n?residue and not the choice of bridge'),
]
for what, pat in WRITTEN:
    ok = re.search(pat, P14, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P14 does not carry: {what}")

print()
_closed = re.search(r'PO-5 is (?:now )?closed'
                    r'|(?<!none is made that )the bridge does not exist'
                    r'|no bridge exists', P14) is not None
_declines = re.search(r'none is made that the bridge does not exist', P14) is not None
print(f"  {'OK ' if not _closed else 'BREACH '}  ⛔ the vein is NOT declared closed anywhere in P14")
print(f"  {'OK ' if _declines else 'MISSING'}  and the clause says so explicitly")
print("     ⚠ *a vein reported as one settled question has been FLATTENED; three of four candidates")
print("        closed is a vein MAPPED, and the fourth stays dark and named*")
if _closed:
    fail.append("P14 declares PO-5 closed — a vein has been flattened")
if not _declines:
    fail.append("the clause does not decline the stronger reading — it will be over-read")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — D is odd but squares to the metric, so a Z2-graded complex collapses to the")
print("index; S_3's class equation gives irreducible dimensions 1,1,2 so the residue's ceiling is a")
print("doublet, and R grades rather than exchanges so it adds a character and no dimension; the angular")
print("gaps are uniform so only the lowest rung is canonical and its multiplicity is 2; and P14 carries")
print("all three with the vein left open.")
print("=" * 78)

# ============================================================================================
# GATE — r2566+c54.207, `L-534`.  ** Three kills reported together is the shape most likely to be
# over-read as a vein closing **, so the pins are on each kill's own mechanism and on the vein
# staying open:
#   (1) *** D^2 asserted NON-zero ***.  ** This is A3's entire argument: if an odd operator here were
#       nilpotent, a genuine Z2-graded complex would exist and cohomology WOULD be a distinct bridge.
#       The gate fails loudly if that ever inverts **;
#   (2) gamma^mu ODD and gamma5 an involution -- ** the first so the candidate differential exists at
#       all, the second so 'two-term' is the right shape and the collapse to ker (+) coker follows **;
#   (3) *** S_3's irreducible dimensions SOLVED from the class equation, not quoted ***, and the
#       uniqueness of the solution asserted -- ** the residue's ceiling of 2 is the number all three
#       routes land on, so it is computed rather than recalled **;
#   (4) the angular gaps pinned UNIFORM and the lowest rung's multiplicity pinned at 2 -- ** uniformity
#       is why no band is canonical, and the exclusion of lambda = 0 is why one is; both are needed and
#       they pull in opposite directions **;
#   (5) seven PREMISE checks, chief among them P13's grading-not-exchanging sentence, which is A5's
#       whole hinge and is the corpus's own, written for another purpose;
#   (6) eight checks on what P14 now says; and
#   (7) *** two VEIN checks ***: P14 must NOT declare PO-5 closed, and must explicitly decline the
#       reading that no bridge exists.  ** A vein reported as one settled question has been flattened,
#       and this file closes three candidates of four -- the fourth stays dark and named. **
#   NOT gated: the anomaly route.  ** Untested here, and nothing above bears on it. **
# ============================================================================================
assert _odd, "gamma^mu is not odd — A3's premise fails"
assert _g5sq, "the grading is not an involution"
assert not _nilpotent, "D^2 VANISHES — A3 inverts and cohomology is a distinct bridge after all"
assert _sols == [(1, 1, 2)] and _maxS3 == 2, "S_3's irreducible dimensions are not 1,1,2"
assert _gaps == [1], "the angular spectrum is not uniformly spaced"
assert MULT[_lowest] == 2, "the lowest admissible rung's multiplicity is not 2"
for what, fn, pat in PREMISES:
    assert re.search(pat, TEX[fn], re.I | re.S), f"premise missing: {what}"
for what, pat in WRITTEN:
    assert re.search(pat, P14, re.I | re.S), f"P14 does not carry: {what}"
assert not _closed and _declines, "the vein has been flattened or the stronger reading is not declined"
print(f"GATE c54.207 (r2566), `L-534`: D(p)^2 = ({_sq})*1 so no odd nilpotent exists and a two-term "
      f"complex has ker (+) coker for its cohomology; S_3's class equation gives {list(_sols[0])} so "
      f"D_6's largest irrep is {_maxS3}-dimensional and R, which grades rather than exchanges, adds a "
      f"character; the angular gaps are {_gaps} so only |lambda| = {_lowest} is canonical, at "
      f"multiplicity {MULT[_lowest]} — three routes, one ceiling of {_maxS3}, and `PO-5` left open with "
      f"the anomaly route untouched — pinned against `THE_DISPATCH` A3/A4/A5 (r2566) and `L-242`.")
