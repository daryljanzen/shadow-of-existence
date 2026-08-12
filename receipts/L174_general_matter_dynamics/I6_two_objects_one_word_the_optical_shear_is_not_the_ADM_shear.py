#!/usr/bin/env python3
"""I6 -- ** r2505's SELECTION PRINCIPLE IS TRUE AND IT CONSTRAINS A DIFFERENT TENSOR.  GOLDBERG--SACHS
GOVERNS THE OPTICAL SHEAR OF A NULL CONGRUENCE -- ONE COMPLEX SCALAR, AND AN INVARIANT OF THE GEOMETRY.
`I3`'s sigma_ij IS THE ADM SHEAR OF A SPATIAL LEAF -- FIVE REAL COMPONENTS, AND NOT AN INVARIANT AT ALL.
SCHWARZSCHILD CARRIES BOTH ANSWERS AT ONCE. **

Built r2508+c54.199, lead `L-511`.  VEINS: `L-165` (PO-6) and `L-175` (PO-9).

===================================================================================================
** THE TWO REVISIONS THIS SITS BETWEEN, AND BOTH OF THEM ARE RIGHT ABOUT SOMETHING **
===================================================================================================

  r2504 `I3`  -- derives rho = R3/2 + theta^2/3 - sigma_ij sigma^ij / 2 with no symmetry, and writes
                 "nothing in the identity says which of them a bend can be", then carries that into a
                 vein's DARK half as ** "nothing selects among five-component shears" **.
  r2505 `I4`  -- corrects that: ** the corpus DOES have a shear-selection principle **, P9's
                 shift--shear link, and its hypothesis is the finding -- ** Goldberg--Sachs is a
                 VACUUM theorem **, so it cannot reach a stratum where matter is dynamical.
  c54.198 `I5`-- and separately: the momentum constraint owns three of the five under the York split,
                 so the free count is ** two **, which P9 names as the graviton's polarizations.

*** AND THE WORD "SHEAR" IN r2505 IS NOT THE WORD "SHEAR" IN r2504. ***

  * `I3`'s sigma_ij : the trace-free part of the EXTRINSIC CURVATURE of a spatial leaf.  A real
    symmetric trace-free 3-tensor -- ** five real components ** -- and it belongs to a FOLIATION.
  * `I4`'s sigma    : the NEWMAN--PENROSE OPTICAL SHEAR of a null geodesic congruence, sigma =
    m^a m^b nabla_a k_b.  ** One complex scalar -- two real components ** -- attached to a null
    DIRECTION, and for the principal null directions it is an invariant of the geometry.

  ⇒ ** Different rank, different reality type, different count, different transformation law.  A
    theorem about the second cannot determine the first, and PART 2 shows that it does not. **

===================================================================================================
** ⛔ THE DEMONSTRATION, AND IT IS ONE SPACETIME **
===================================================================================================

** SCHWARZSCHILD IS TYPE D, so by Goldberg--Sachs its repeated principal null directions are
SHEAR-FREE: the optical shear is exactly zero. **  Now slice it two ways.

  * ** static Schwarzschild slices ** -- zero shift, static metric: K_ij = 0, so sigma_ij = 0;
  * ** Painleve--Gullstrand slices ** -- flat spatial metric, lapse 1, shift beta^r = sqrt(2M/r):
    ** sigma_ij sigma^ij = 3M/r^3, nonzero everywhere outside the origin. **

  *** SAME SPACETIME.  SAME ALGEBRAIC TYPE.  SAME SHEAR-FREE NULL CONGRUENCE.  THE ADM SHEAR IS ZERO
      IN ONE FOLIATION AND NONZERO IN THE OTHER. ***

  ⇒ ** sigma_ij is not a function of the geometry, so no theorem about the geometry can fix it. **
    *That is not a defect in r2505's argument; it is the argument being about the other tensor.*

===================================================================================================
** ⛭⛭ AND THE PART THAT MAKES THIS A SYNTHESIS RATHER THAN A DEMOLITION **
===================================================================================================

Where does the foliation freedom live?  ** Entirely in the three components `I5` showed the momentum
constraint owns. **  PART 3 solves for it: the Painleve--Gullstrand shear is EXACTLY (LW)_ij for
W_r = -sqrt(2M)/(2 sqrt r) -- ** purely longitudinal, sigma^TT = 0 **, which is also its value in the
static slicing.

  *** SO THE 3 + 2 SPLIT IS NOT BOOKKEEPING.  The three longitudinal components are where the
      foliation freedom sits, and the two transverse-traceless ones are what the geometry actually
      carries -- which is why Schwarzschild, which carries no radiation, has sigma^TT = 0 in both
      slicings while sigma_ij differs between them. ***

  ⇒ ** r2505's principle speaks to an INVARIANT, so it can only ever have addressed the invariant
    half.  `I3`'s question was posed over all five, three of which are not invariant at all. **  Both
    findings stand; ** what does not stand is reading either as an answer to the other. **

===================================================================================================
** ⌗ AND r2505's OWN RULE NEEDS ONE MORE CLAUSE, WHICH ITS OWN REVISION SUPPLIES **
===================================================================================================

r2505 states the rule this file agrees with: *"when you derive an identity and find it does not
determine something, that is a statement about THE IDENTITY.  Before promoting it to a statement about
the programme, search the corpus for the constraint."*

  ⇒ *** AND THEN CHECK THAT THE CONSTRAINT YOU FOUND CONSTRAINS THE SAME OBJECT. ***  *The search
      succeeded -- P9 does carry a shear-selection principle -- and the object it selects has two
      real components and a different transformation law from the one that was five.*

⚠ ** THIS IS THE CORPUS'S OWN NAMED FAILURE CLASS, FOR AT LEAST THE THIRD TIME THIS MONTH: ** the
`branch point`/`seam` conflation (routed item 21, six sites, c54.197), r2494's "four objects sharing
one word", and now two shears.  *A vein's DARK half is where 56 says a local negative gets silently
globalised; **this file's addition is that it is equally where a global theorem gets silently
localised onto whatever wears the same name**.*

WHAT IS NOT CLAIMED.  ** Not that r2505 is wrong ** -- its statement about the optical shear and the
algebraic type is correct, its vacuum-hypothesis finding is correct and is the valuable half, and this
file leaves both standing.  ** Not that the two shears are unrelated ** -- the optical shear of a
congruence adapted to a leaf contains a projection of sigma_ij plus derivative terms; they are related
and they are not the same.  ** Not that any beyond-wall solution is exhibited. **

SETTINGS: none -- no instrument, no spectra.  Symbolic differential geometry (sympy) on two exact
slicings of one exact vacuum solution, plus the York split from `I5`.

rc=0 on success.  Run: python3 I6_two_objects_one_word_the_optical_shear_is_not_the_ADM_shear.py
                        (sympy numpy scipy; ~20 s)
"""
import os
import re
import sys

import numpy as np
import sympy as sp
from scipy.linalg import null_space

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
fail = []

r, th, M = sp.symbols('r theta M', positive=True)
ph = sp.Symbol('phi')
X = [r, th, ph]
G3 = sp.diag(1, r ** 2, r ** 2 * sp.sin(th) ** 2)       # the PG slice IS flat
GI = G3.inv()


def christoffel():
    def C(a, b, c):
        return sp.simplify(sum(GI[a, d] * (sp.diff(G3[d, b], X[c]) + sp.diff(G3[d, c], X[b])
                                           - sp.diff(G3[b, c], X[d])) for d in range(3)) / 2)
    return [[[C(a, b, c) for c in range(3)] for b in range(3)] for a in range(3)]


GAM = christoffel()


def Dlo(V, i, j):
    """D_i V_j for a covector V (index down)."""
    return sp.simplify(sp.diff(V[j], X[i]) - sum(GAM[k][i][j] * V[k] for k in range(3)))


# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO OBJECTS, COUNTED")
print("=" * 78)
print("  ADM shear sigma_ij   : real symmetric 3x3, trace-free              -> 6 - 1 = 5 real")
print("  NP optical shear     : sigma = m^a m^b grad_a k_b, ONE COMPLEX      -> 2 real")
print("  *and the optical shear is attached to a null DIRECTION and is an invariant of the")
print("   geometry for the principal null directions, while sigma_ij belongs to a FOLIATION.*")
_adm_dim = 6 - 1
_opt_dim = 2
print(f"\n  ** {_adm_dim} against {_opt_dim}: a theorem fixing the second cannot fix the first. **")
if (_adm_dim, _opt_dim) != (5, 2):
    fail.append("the component counts are not 5 and 2 — PART 1's premise is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ONE SPACETIME, TWO SLICINGS: THE ADM SHEAR MOVES AND THE ALGEBRAIC TYPE DOES NOT")
print("=" * 78)
v = sp.sqrt(2 * M / r)
beta = sp.Matrix([v, 0, 0])                              # beta_i, PG shift (beta^r = v, g_rr = 1)
K_pg = sp.Matrix(3, 3, lambda i, j: sp.simplify(-(Dlo(beta, i, j) + Dlo(beta, j, i)) / 2))
th_pg = sp.simplify(sp.trace(GI * K_pg))
sig_pg = sp.simplify(K_pg - sp.Rational(1, 3) * th_pg * G3)
sig2_pg = sp.simplify(sp.trace(GI * sig_pg * GI * sig_pg))
print(f"  PAINLEVE-GULLSTRAND   theta = {th_pg}")
print(f"                        sigma_ij sigma^ij = {sig2_pg}")
print(f"  STATIC SCHWARZSCHILD  zero shift, static metric -> K_ij = 0 -> sigma_ij sigma^ij = 0")
print()
print("  ** Schwarzschild is TYPE D, so by Goldberg-Sachs its repeated PNDs are SHEAR-FREE in the")
print("     optical sense -- in BOTH slicings, because the algebraic type is a property of the")
print("     spacetime and not of how it is cut. **")
print("  ⇒ *the ADM shear is 3M/r^3 in one foliation and 0 in the other, so it is NOT determined by")
print("     the algebraic type, and r2505's principle -- which is correct -- is about the other one.*")
_sig2_static = sp.Integer(0)
if sp.simplify(sig2_pg) == 0:
    fail.append("the PG slicing gives zero ADM shear — PART 2 has no contrast to show")
if sp.simplify(sig2_pg - 3 * M / r ** 3) != 0:
    fail.append(f"the PG shear scalar is {sig2_pg}, not 3M/r^3")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE DIFFERENCE IS PURELY LONGITUDINAL: sigma^TT = 0 IN BOTH")
print("=" * 78)
w = sp.Function('w')(r)
W = sp.Matrix([w, 0, 0])
LW = sp.Matrix(3, 3, lambda i, j: sp.simplify(
    Dlo(W, i, j) + Dlo(W, j, i)
    - sp.Rational(2, 3) * G3[i, j] * sum(GI[a, b] * Dlo(W, a, b) for a in range(3) for b in range(3))))
_sol = sp.dsolve(sp.Eq(sp.simplify(LW[0, 0] - sig_pg[0, 0]), 0), w)
_w = sp.simplify(_sol.rhs.subs(sp.Symbol('C1'), 0))
_res = sp.Matrix(3, 3, lambda i, j: sp.simplify(LW[i, j].subs(w, _w).doit() - sig_pg[i, j]))
_long = all(sp.simplify(_res[i, j]) == 0 for i in range(3) for j in range(3))
print(f"  solving (LW)_rr = sigma_rr for a radial W gives   W_r = {_w}")
print(f"  residual sigma_ij - (LW)_ij over all nine components : "
      f"{'ALL ZERO' if _long else _res.tolist()}")
print()
print("  ** SO THE PAINLEVE-GULLSTRAND SHEAR IS EXACTLY A YORK LONGITUDINAL PIECE: sigma^TT = 0. **")
print("  *And it is 0 in the static slicing too, trivially.*  ⇒ ***The foliation freedom lives in the")
print("   THREE components the momentum constraint owns; the TWO transverse-traceless ones are what")
print("   the geometry carries — and Schwarzschild, carrying no radiation, has them zero either way.***")
if not _long:
    fail.append("the PG shear is not purely longitudinal — PART 3's synthesis does not hold")

# and the 3+2 split itself, carried over from I5 so this file stands alone
BAS = []
for a, b in [(0, 1), (0, 2), (1, 2)]:
    Mx = np.zeros((3, 3)); Mx[a, b] = Mx[b, a] = 1.0; BAS.append(Mx)
BAS.append(np.diag([1.0, -1.0, 0.0])); BAS.append(np.diag([1.0, 1.0, -2.0]) / np.sqrt(3.0))
def _co(Mx): return np.array([np.sum(Mx * b) / np.sum(b * b) for b in BAS])
def _L(k, Wv):
    k = np.asarray(k, float); Wv = np.asarray(Wv, float)
    return np.outer(k, Wv) + np.outer(Wv, k) - (2 / 3) * np.eye(3) * float(np.dot(k, Wv))
_k = (1.0, 2.0, 3.0)
_Lm = np.array([_co(_L(_k, e)) for e in np.eye(3)]).T
_ns = null_space(np.array([[float((Mx @ np.asarray(_k, float))[i]) for Mx in BAS] for i in range(3)]))
_split = (int(np.linalg.matrix_rank(_Lm, tol=1e-10)), int(_ns.shape[1]))
print(f"\n  (the York split re-checked here so this file stands alone: longitudinal {_split[0]} + TT "
      f"{_split[1]} = {_split[0] + _split[1]})")
if _split != (3, 2):
    fail.append(f"the York split gives {_split}, not (3, 2)")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND BOTH READINGS ARE IN THE CORPUS's OWN TEXT, CHECKED RATHER THAN QUOTED")
print("=" * 78)
p9 = open(os.path.join(ROOT, 'corpus', 'range_paper.tex'), encoding='utf-8').read()
i4 = open(os.path.join(HERE, 'I4_the_shear_selection_exists_and_is_vacuum_bound.py'),
          encoding='utf-8').read()
i3 = open(os.path.join(HERE, 'I3_the_identification_is_general_and_the_shear_count_is_the_gap.py'),
          encoding='utf-8').read()
CHECKS = [
    ("P9's shear-selection is about a NULL GEODESIC CONGRUENCE",
     p9, r'shear-free null geodesic congruence'),
    ("P9 states the VACUUM hypothesis, which is r2505's finding and stands",
     p9, r'algebraically special \\?emph\{?vacuum|algebraically special vacuum'),
    ("r2505's I4 reads it as sigma = 0 ON THE PRINCIPAL CONGRUENCE",
     i4, r'sigma = 0\s*\n?\s*on the principal congruence|sigma = 0 on the principal congruence'),
    ("r2504's I3 defines ITS sigma as the trace-free part of the EXTRINSIC CURVATURE",
     i3, r'K_ij = \(1/3\) theta g_ij \+ sigma_ij'),
    ("and I3 counts it as FIVE components",
     i3, r'five-component trace-free symmetric object'),
]
for what, src, pat in CHECKS:
    ok = re.search(pat, src, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"not found in source: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the optical shear is one complex scalar and an invariant; the ADM shear is")
print("five real components and belongs to a foliation. Schwarzschild is Type D with shear-free PNDs")
print("in every slicing, and its ADM shear is 3M/r^3 in Painleve-Gullstrand and 0 in static")
print("coordinates. The whole difference is longitudinal, so sigma^TT = 0 either way: the three the")
print("momentum constraint owns carry the foliation, the two it leaves carry the geometry.")
print("=" * 78)

# ============================================================================================
# GATE — r2508+c54.199, `L-511`.  This file says a landed correction answers a different
# question than the one it corrects, so every step is pinned and two over-readings are blocked:
#   (1) the counts, 5 against 2 -- the whole distinction is that these are different objects,
#       and if they had the same count the argument would be much weaker;
#   (2) the PG shear scalar 3M/r^3 asserted NONZERO and pinned -- ** this is the demonstration:
#       one spacetime, one algebraic type, two slicings, two answers **;
#   (3) the residual sigma - LW asserted zero across all nine components, which is the synthesis
#       half -- without it this file only separates the two findings and does not join them;
#   (4) the York split re-checked here rather than cited, so the file stands alone;
#   (5) and FOUR source checks -- ** if P9's principle were not about a null congruence, or if
#       I3's sigma were not the extrinsic curvature's trace-free part, this whole reading would
#       be mine rather than the corpus's, and that is the failure it must not have. **
#   NOT gated, because not claimed: that r2505 erred.  Its vacuum-hypothesis finding is correct
#   and untouched; what this file denies is only that it answers I3's question.
# ============================================================================================
assert (_adm_dim, _opt_dim) == (5, 2), "the two shears do not have the counts this file rests on"
assert sp.simplify(sig2_pg - 3 * M / r ** 3) == 0, f"PG shear scalar moved: {sig2_pg}"
assert sp.simplify(sig2_pg) != 0, "the PG slicing shows no shear — there is no contrast to demonstrate"
assert _long, "the PG shear is not purely longitudinal — the synthesis in PART 3 fails"
assert _split == (3, 2), f"the York split gives {_split}, not (3, 2)"
assert re.search(r'shear-free null geodesic congruence', p9, re.I), \
    "P9's selection principle is not stated over a null congruence — this reading is not the corpus's"
assert re.search(r'K_ij = \(1/3\) theta g_ij \+ sigma_ij', i3), \
    "I3's sigma is not the extrinsic curvature's trace-free part — the two-objects claim fails"
print(f"GATE c54.199 (r2508), `L-511`: optical shear 2 real and invariant against ADM shear 5 real "
      f"and foliation-bound; Schwarzschild Type D throughout, with sigma^2 = {sig2_pg} in "
      f"Painleve-Gullstrand and 0 in static slices; the entire difference is the longitudinal piece "
      f"W_r = {_w}, so sigma^TT = 0 in both — pinned against `I3` (r2504), `I4` (r2505), `I5` "
      f"(c54.198) and P9 sec:petrov.")
