#!/usr/bin/env python3
"""I5 -- ** THE UNWORKED STRATUM'S FREE SHEAR IS TWO COMPONENTS, NOT FIVE.  THE MOMENTUM CONSTRAINT --
WHICH I3 WRITES DOWN TWO LINES ABOVE THE CLAIM -- FIXES THREE OF THE FIVE, AND P9 ALREADY NAMES THE
REMAINING TWO IN ITS OWN VOICE: "THE GRAVITON'S TWO PROPAGATING POLARIZATIONS." **

Built r2504+c54.198, lead `L-510`.  VEINS: `L-165` (PO-6, what a quantum of this geometry is) and
`L-175` (PO-9) -- the two `L-174` informs.

===================================================================================================
** WHAT I3 LANDED, AND IT IS RIGHT **
===================================================================================================

r2504 made the first purchase on `L-174`'s one unworked stratum and it holds:

  * K_ij = (1/3) theta g_ij + sigma_ij gives K^2 - K_ij K^ij = (2/3) theta^2 - sigma_ij sigma^ij
    IDENTICALLY -- re-verified here on a general 3-metric with a general symmetric K, PART 1;
  * so rho = R3/2 + theta^2/3 - sigma^2/2 uses no symmetry, and "the energy and momentum ARE the
    shear" is a general ADM identity rather than a Gowdy fact;
  * so the two Killing vectors buy a COUNT rather than a CONTENT.  ** That reframing is the purchase
    and nothing here touches it. **

===================================================================================================
** ⛔ AND THE COUNT IT BUYS IS 1-OF-2, NOT 1-OF-5 **
===================================================================================================

I3 closes: *"With FIVE there is a five-dimensional space of shear configurations at fixed rho and
fixed theta -- and nothing in the identity says which of them a bend can be ... THAT TRADE IS THE
INTERIOR OF THE STRATUM, AND IT IS DARK."*

** The clause "nothing in the IDENTITY" is exact.  The promotion to "nothing selects" is not, because
the identity is one of two constraints and I3 writes the other one down itself: **

    I3, four lines above: "the trace-free part of the momentum constraint ... is exactly D_j sigma^ij."

  *** A symmetric trace-free sigma_ij splits uniquely and ORTHOGONALLY as sigma^TT + (LW), where
      (LW)_ij = D_i W_j + D_j W_i - (2/3) g_ij D_k W^k and D^j sigma^TT_ij = 0 (York).  The momentum
      constraint is an elliptic equation for W alone -- sigma^TT drops out of it identically -- so it
      DETERMINES the three longitudinal components and says nothing about the other two. ***

PART 2 verifies the split numerically at several wavevectors: longitudinal image rank 3, transverse
null space 2, the two blocks orthogonal, and 3 + 2 = 5 exactly.

  ⇒ ** So the free shear is TWO components, not five, and the Killing vectors buy ONE of those two --
    not one of five. **  *The other three were never free; they are fixed by the constraint that names
    the matter momentum, which is the same constraint I3 identifies as the "momentum" half of "the
    energy and momentum are the shear".*

===================================================================================================
** ⛭⛭ AND THE TWO THAT REMAIN ARE NOT NAMELESS -- P9 NAMES THEM, AND CALLS THEM THE WALL **
===================================================================================================

`corpus/range_paper.tex`, sec:reach, in its own voice:

    "The graviton's TWO propagating polarizations are exactly the transverse degrees of freedom a
     sweep cannot carry, since a swept geometry depends only on its orbit-space coordinates while a
     free wave depends on the transverse coordinates through which it propagates."

  *** The two components the momentum constraint leaves are the two P9 already identifies with the
      onset of free gravitational radiation -- which is the boundary `L-174`'s stratum sits beyond. ***

PART 3 checks that against the corpus text rather than asserting it, and PART 4 runs the control the
whole reframing needs: ** the polarized Gowdy leaf. **  With two commuting Killing vectors the
propagation direction is fixed, so the transverse 2-plane is one plane over the whole leaf and the TT
space at that wavevector is spanned by exactly the two familiar polarizations; ** polarized ** is the
further restriction to one of them.  *That is I3's "on a polarized Gowdy leaf the shear is one
function" recovered as 1 of 2, and it is the number that changes.*

===================================================================================================
** ⌷ SO WHAT IS ACTUALLY DARK, AND IT IS NARROWER AND SHARPER THAN "WHICH OF FIVE" **
===================================================================================================

** It is not WHICH of a five-dimensional family.  It is HOW THE TRANSVERSE 2-PLANE TURNS. **  With a
confining isometry the propagation direction is pinned, so one 2-plane serves the whole leaf and a
polarization is a constant choice inside it.  Lose the last isometry and the 2-plane varies from
point to point -- and ** P9 says exactly this, in the source comment its own header carries: **

    "the loss of the last confining isometry is exactly the point at which the wave's polarization
     MUST REORIENT FROM PLACE TO PLACE"

  ⇒ *** So `L-174`'s dark interior is the turning of the polarization plane over the leaf, which the
      corpus already treats as a named object (P9's chirality reading, and the dynamics paper's
      territory) rather than a five-dimensional unknown. ***

⚠ ** WHY THE FIVE READS AS FREE, WHICH IS THE PART WORTH KEEPING FROM I3. **  I3 asks: hold the
PHYSICAL leaf metric, theta and rho fixed; which sigma?  That fixes |sigma|^2 pointwise (1 condition)
and the momentum constraint adds 3 more -- ** four conditions on five components, and the leftover
looks unselected because the formulation has fixed one thing too many. **  *York's formulation holds
the CONFORMAL class fixed and solves the Hamiltonian constraint for the conformal factor, not by
choosing among shears; then the free datum is sigma^TT and the count is clean.*  ⇒ ** The "nothing
selects" reading is an artefact of the fixed-physical-metric framing, not a property of the stratum. **

** WHAT IS NOT CLAIMED. **  ** No beyond-wall solution is exhibited and none is claimed **; I3's own
disclaimer stands unchanged.  Not that the two-component problem is tractable.  Not that sigma^TT = 0
characterises the wall -- ** it does not, and the polarized Gowdy leaf is the counterexample: it has
two Killing vectors AND a nonzero sigma^TT. **  *The wall is the loss of the PIN on the propagation
direction, not the vanishing of the transverse freedom, and PART 4 is what keeps those apart.*

SETTINGS: none -- no instrument, no spectra.  Symbolic (sympy) and finite-dimensional linear algebra
(numpy/scipy) only, plus two string checks against the corpus's own .tex.

rc=0 on success.  Run: python3 I5_the_free_shear_is_two_not_five_and_the_corpus_already_names_the_two.py
                        (sympy numpy scipy; ~5 s)
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

# =====================================================================
print("=" * 78)
print("PART 1 — I3's IDENTITY, RE-VERIFIED ON A GENERAL 3-METRIC AND A GENERAL SYMMETRIC K")
print("=" * 78)
g = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'g{min(i, j)}{max(i, j)}'))
K = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'K{min(i, j)}{max(i, j)}'))
gi = g.inv()
theta = sp.trace(gi * K)
sig = K - sp.Rational(1, 3) * theta * g
_tr = sp.simplify(sp.trace(gi * sig))
_lhs = sp.simplify(theta ** 2 - sp.trace(gi * K * gi * K))
_rhs = sp.simplify(sp.Rational(2, 3) * theta ** 2 - sp.trace(gi * sig * gi * sig))
_id = sp.simplify(_lhs - _rhs) == 0
print(f"  sigma is trace-free                                  : {_tr == 0}")
print(f"  K^2 - K_ij K^ij  ==  (2/3) theta^2 - sigma_ij sigma^ij : {_id}")
print("  *So rho = R3/2 + theta^2/3 - sigma^2/2 uses NO symmetry — I3's purchase, re-derived.*")
if _tr != 0:
    fail.append("the trace-free part is not trace-free")
if not _id:
    fail.append("the ADM identity I3 rests on does not hold — PART 1 blocks everything after it")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE YORK SPLIT: THE MOMENTUM CONSTRAINT OWNS THREE OF THE FIVE")
print("=" * 78)
# an orthogonal basis for symmetric trace-free 3x3 (5 elements)
BAS = []
for a, b in [(0, 1), (0, 2), (1, 2)]:
    M = np.zeros((3, 3))
    M[a, b] = M[b, a] = 1.0
    BAS.append(M)
BAS.append(np.diag([1.0, -1.0, 0.0]))
BAS.append(np.diag([1.0, 1.0, -2.0]) / np.sqrt(3.0))
NAMES = ['xy', 'xz', 'yz', 'diag(1,-1,0)', 'diag(1,1,-2)/sqrt3']


def coords(M):
    return np.array([np.sum(M * b) / np.sum(b * b) for b in BAS])


def L_of(k, W):
    """(LW)_ij = k_i W_j + k_j W_i - (2/3) delta_ij (k.W)  -- the conformal Killing operator in Fourier."""
    k = np.asarray(k, float)
    W = np.asarray(W, float)
    return np.outer(k, W) + np.outer(W, k) - (2.0 / 3.0) * np.eye(3) * float(np.dot(k, W))


def transversality(k):
    """the 3 x 5 matrix of the conditions k_j sigma^ij = 0"""
    k = np.asarray(k, float)
    return np.array([[float((M @ k)[i]) for M in BAS] for i in range(3)])


print(f"  {'wavevector':>22s} {'longit. rank':>13s} {'TT dim':>8s} {'3+2 spans 5':>13s} {'<L,TT>':>10s}")
_results = []
for k in [(0, 0, 1.0), (1, 0, 0.0), (1, 1, 0.0), (1, 2, 3.0), (0.31, -1.07, 2.73)]:
    Lm = np.array([coords(L_of(k, e)) for e in np.eye(3)]).T          # 5 x 3
    ns = null_space(transversality(k))                                 # 5 x d
    rk = int(np.linalg.matrix_rank(Lm, tol=1e-10))
    tt = int(ns.shape[1])
    span = int(np.linalg.matrix_rank(np.hstack([Lm, ns]), tol=1e-10))
    orth = float(np.abs(Lm.T @ ns).max())
    print(f"  {str(k):>22s} {rk:>13d} {tt:>8d} {str(span == 5):>13s} {orth:>10.1e}")
    _results.append((rk, tt, span, orth))
    if (rk, tt, span) != (3, 2, 5) or orth > 1e-9:
        fail.append(f"the York split fails at k={k}: rank {rk}, TT {tt}, span {span}, overlap {orth:.1e}")
print()
print("  ** LONGITUDINAL 3 + TRANSVERSE-TRACELESS 2 = 5, ORTHOGONALLY, AT EVERY WAVEVECTOR. **")
print("  *The momentum constraint D_j sigma^ij is an equation for the longitudinal part alone —")
print("   sigma^TT is annihilated by D^j identically — so it fixes THREE and leaves TWO.*")
print("  ⇒ *the free shear is 2, and I3's 'five-dimensional space ... nothing selecting among them'")
print("     counts the space BEFORE the constraint I3 itself wrote down.*")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE CORPUS ALREADY NAMES THE TWO.  CHECKED AGAINST P9's TEXT, NOT ASSERTED")
print("=" * 78)
p9 = open(os.path.join(ROOT, 'corpus', 'range_paper.tex'), encoding='utf-8').read()
CLAIMS = [
    ("P9 names the count as TWO and calls them the graviton's polarizations",
     r"graviton'?s two propagating polarizations"),
    ("P9 ties them to what a sweep cannot carry",
     r"transverse degrees of freedom a sweep cannot carry"),
    ("P9 identifies the wall as the ONSET of free gravitational radiation",
     r"onset of free gravitational radiation"),
    ("P9 states the reachable sector carries NO free propagating tensor mode",
     r"reachable sector carries no free propagating tensor mode"),
    ("P9 places Gowdy (two Killing vectors) INSIDE the reachable sector, on its edge",
     r"Gowdy waves, type I with two Killing vectors"),
]
for what, pat in CLAIMS:
    ok = re.search(pat, p9, re.I) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P9 does not carry: {what} — PART 3's reading is not the corpus's")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE GOWDY CONTROL, WHICH IS WHAT KEEPS THE TWO CLAIMS APART")
print("=" * 78)
kz = (0.0, 0.0, 1.0)
ns = null_space(transversality(kz))
print("  two commuting Killing vectors pin the propagation direction; take it along z.")
print("  the TT space at that wavevector, in the basis "
      f"[{', '.join(NAMES)}]:")
for c in ns.T:
    lab = ', '.join(f'{NAMES[i]}: {v:+.3f}' for i, v in enumerate(np.round(c, 6)) if abs(v) > 1e-9)
    print(f"    {lab}")
_supports = [set(i for i, v in enumerate(c) if abs(v) > 1e-9) for c in ns.T]
_is_plus_cross = ({3} in _supports and {0} in _supports)
print()
print(f"  ** the two are exactly the familiar polarizations: 'plus' = diag(1,-1,0) and 'cross' = xy. **"
      f"  [{_is_plus_cross}]")
print("  *POLARIZED Gowdy is the restriction to ONE of them — which is I3's 'the shear is one")
print("   function', now read as **1 of 2** rather than 1 of 5.*")
print()
print("  ⛔ AND THE THING THIS CONTROL FORBIDS: an UNpolarized Gowdy leaf has two Killing vectors")
print("     AND both TT components, so ** sigma^TT = 0 is NOT the wall ** and must not be read as it.")
print("     *The wall is the loss of the PIN on the propagation direction — after which the transverse")
print("      2-plane itself turns from place to place, which is P9's own sentence.*")
if not _is_plus_cross:
    fail.append("the TT space at k along z is not the plus/cross pair — PART 4's control does not hold")
if ns.shape[1] != 2:
    fail.append(f"the TT space at k along z has dimension {ns.shape[1]}, not 2")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the ADM identity holds with no symmetry; the momentum constraint owns three")
print("of the five shear components and leaves two, orthogonally, at every wavevector; P9 already")
print("names those two as the graviton's polarizations and the wall as their onset; and the polarized")
print("Gowdy leaf is 1 of 2, not 1 of 5 — while an unpolarized one shows sigma^TT = 0 is not the wall.")
print("=" * 78)

# ============================================================================================
# GATE — r2504+c54.198, `L-510`.  This file NARROWS the board's top lead rather than closing it,
# and the pins are on the narrowing being real and on the two over-readings it would be easy to
# fall into being blocked:
#   (1) I3's identity, re-derived on a GENERAL metric -- if it failed, nothing after it means
#       anything and the correction would be to I3's premise instead of its count;
#   (2) the York split at five wavevectors: longitudinal rank 3, TT dim 2, orthogonal, spanning
#       5.  ** This is the whole correction: 5 was counted before the momentum constraint. **
#   (3) P9's own words, matched in the .tex rather than quoted from memory -- ** if the corpus
#       did not already name the two, this file would be importing standard GR into a corpus
#       claim, which is the one thing it must not do **;
#   (4) the plus/cross pair at k along z, which is what makes "1 of 2" concrete and is the
#       control on I3's Gowdy statement;
#   (5) and the TT dimension asserted to be 2 there -- because if a confining isometry left only
#       ONE transverse direction, "sigma^TT = 0 is not the wall" would lose its counterexample
#       and the wall could be misread as the vanishing of the transverse freedom.
# ============================================================================================
assert _tr == 0 and _id, "the ADM identity underlying I3 does not hold"
assert len(_results) == 5, f"only {len(_results)} wavevector(s) tested — one is a coincidence"
for rk, tt, span, orth in _results:
    assert (rk, tt, span) == (3, 2, 5), f"York split gave rank {rk}, TT {tt}, span {span}"
    assert orth < 1e-9, f"longitudinal and TT blocks are not orthogonal: {orth:.1e}"
assert re.search(r"graviton'?s two propagating polarizations", p9, re.I), \
    "P9 does not name the two polarizations — this file's reading is not the corpus's"
assert re.search(r"onset of free gravitational radiation", p9, re.I), \
    "P9 does not call the wall the onset of free radiation"
assert ns.shape[1] == 2 and _is_plus_cross, \
    "the TT space at a pinned propagation direction is not the plus/cross pair"
print(f"GATE c54.199 (r2508), `L-510`: the ADM identity holds with no symmetry; the momentum "
      f"constraint owns 3 of 5 shear components at every wavevector tested, leaving "
      f"{_results[0][1]} orthogonally; P9 names those two as the graviton's polarizations and the "
      f"wall as their onset; and the pinned-direction TT space is exactly plus/cross, so the "
      f"polarized Gowdy leaf is 1 of 2 — pinned against `I3` (r2504) and P9 sec:reach.")
