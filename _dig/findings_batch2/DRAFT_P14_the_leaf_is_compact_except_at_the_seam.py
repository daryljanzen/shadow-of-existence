"""
DRAFT_P14_the_leaf_is_compact_except_at_the_seam.py -- P14 sec:count:
** THE LEAF-COMPACTNESS CLAIM THAT CARRIES THE INDEX IS MEMBER-DEPENDENT, AND THE PAPER DOES NOT
   SAY WHICH MEMBER.  It holds on every sub-Nariai member -- and fails at the NARIAI member, which
   is the corpus's own seam. **

WHAT THE CORPUS HAS.  P14 sec:count, the sentence citing [AtiyahSinger1968]:

  "In the leaf's proper measure dl = dr/sqrt|f| the closed slicing has ** FINITE ** total length
   -- the horizon turning points at finite proper distance, the r=0 crossing an integrable
   sqrt-singularity -- so ** the leaf is compact and the Dirac operator on it carries a
   well-defined analytical index dim ker **, exactly where the bulk index on the non-compact
   spacetime (tortoise measure) is obstructed."

`P14_leaf_compactness.py` verifies it, and verifies it well: five checks, a control that a
fabricated simple-pole measure fails where the sqrt measure passes, and the exponent test that is
the heart of the matter.  ** It runs at M = 0.12, alpha = 1. **

THE NARIAI MASS IS M_N = alpha/(3 sqrt3) = 0.19245, so the receipt runs at ** 0.62 M_N **, where
f has three SIMPLE roots.  There the integrable exponent is -1/2 at each and the length is finite.

--------------------------------------------------------------------------------------------
WHAT HAPPENS AT THE NARIAI MEMBER
--------------------------------------------------------------------------------------------
At M = M_N the two positive roots MERGE at r_0 = alpha/sqrt3 -- P14's own sec:cosmogenesis says so
("the Nariai crest is the fixed point of the root-permutation, where two of the three roots merge,
the discriminant 4 - 3 r_0^2 vanishing").  A DOUBLE root changes the exponent:

    f(r_0) = f'(r_0) = 0,  f''(r_0) = -6/alpha^2
    =>  |f| ~ 3 (r - r_0)^2 / alpha^2      =>  1/sqrt|f| ~ ** alpha / (sqrt3 |r - r_0|) **

-- a simple POLE, not a square root.  ** The leaf proper length diverges logarithmically at the
front seam, at the rate alpha/sqrt3 per e-fold of cutoff. **  That is exactly the exponent the
receipt's own control identifies as non-integrable, arriving at the one member it does not test.

--------------------------------------------------------------------------------------------
AND IT IS A DISCONTINUITY, NOT A LIMIT
--------------------------------------------------------------------------------------------
For every M < M_N the total length is finite, and it stays finite as M -> M_N:
the between-horizon piece INT_{r_b}^{r_c} dr/sqrt(f) tends to ** pi alpha / sqrt3 **, a clean
closed form, while the outside pieces stay integrable at each simple root.  ** But AT M = M_N the
f > 0 region has closed up, both approaches to r_0 run through f < 0, and the integral diverges. **
So the leaf length is finite on the whole open family and infinite at its endpoint.

--------------------------------------------------------------------------------------------
WHY IT MATTERS, AND WHY IT MIGHT NOT
--------------------------------------------------------------------------------------------
The Nariai member is not an exotic corner of this programme.  ** It is the seam. **  P16's spine
has the beginning as a collapse "through the finite-curvature degenerate (kappa = 0) Nariai seam";
P7's lap is drawn on the Nariai member and its two seams are named as r = -2 alpha/sqrt3 and
r = + alpha/sqrt3, the second of which IS the double root; P3's whole dial peaks there.

So the question is sharp and I cannot settle it from here:

  ** ON WHICH MEMBER IS P14's LEAF? **

  · If a GENERIC member -- the receipt's reading -- then everything is right and what is owed is a
    clause: the claim holds for M < M_N and fails at the degenerate member, and the index is a
    statement about the open family.
  · If the NARIAI member, then "the leaf is compact" is false there, and with it "the Dirac
    operator on it carries a well-defined analytical index dim ker" -- and the argument would need
    either a different measure, a regularisation at the double root, or an explicit restriction to
    M < M_N.

⌗ *Which way it goes is not a small matter of wording: the count of three generations is stated as
   a wall-localised index, and the compactness of the leaf is what P14 offers in place of the bulk
   index P13's non-compactness obstructs.  ** The load-bearing sentence should name its member. ***

HONEST WEIGHT.  ** No claim that the index is wrong. **  The three walls sit at r = 0 on the throat
circle, and the r = 0 crossing is integrable at EVERY member including Nariai (verified below) --
so the modes' own locus is not where the trouble is.  The trouble is the front seam, at the far end
of the same closed slicing, and only at one member.  This is a scope question about a stated
hypothesis, not a refutation of a result.

STATED FOR REVERSAL.  No closure on any registered item.  If P14's member is fixed somewhere I did
not find, strike this: searched `nariai` in matter_sector_paper.tex (4 hits, none about the leaf),
`double root`, `degenerate`, `simple root`, `compact` across corpus/ and receipts/.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

print(__doc__)

al = 1.0
MN = al / (3 * np.sqrt(3))
f = lambda r, M: 1 - 2 * M / r - r * r / al**2


def roots(M):
    return sorted(x.real for x in np.roots([1 / al**2, 0, -1, 2 * M]) if abs(x.imag) < 1e-9)


# ============================================================================
print("=" * 78)
print("PART 1 — THE RECEIPT'S MEMBER, REPRODUCED")
print("=" * 78)
Mr = 0.12
rb = brentq(lambda r: f(r, Mr), 0.15, 0.5)
rc = brentq(lambda r: f(r, Mr), 0.5, 0.99)
L, _ = quad(lambda r: 1 / np.sqrt(f(r, Mr)), rb, rc, points=[rb, rc], limit=400)
print(f"  M = {Mr} alpha = {Mr/MN:.3f} M_N     roots {[round(x,5) for x in roots(Mr)]}")
print(f"  horizons r_b = {rb:.4f}, r_c = {rc:.4f}   (all three roots SIMPLE)")
print(f"  between-horizon leaf length INT dr/sqrt(f) = {L:.4f}    "
      f"(P14_leaf_compactness prints 1.7671)")
assert np.isfinite(L) and 1.5 < L < 2.0
print("  ** finite, as the receipt says.  The exponent at each simple root is -1/2. **")

# ============================================================================
print()
print("=" * 78)
print("PART 2 — THE NARIAI MEMBER: THE EXPONENT CHANGES")
print("=" * 78)
r0 = al / np.sqrt(3)
fp = lambda r, M, h=1e-7: (f(r + h, M) - f(r - h, M)) / (2 * h)
fpp = lambda r, M, h=1e-5: (f(r + h, M) - 2 * f(r, M) + f(r - h, M)) / h**2
print(f"  M_N = alpha/(3 sqrt3) = {MN:.9f}       roots {[round(x,6) for x in roots(MN)]}")
print(f"  r_0 = alpha/sqrt3 = {r0:.6f}")
print(f"     f(r_0)   = {f(r0, MN):+.3e}")
print(f"     f'(r_0)  = {fp(r0, MN):+.3e}          -> DOUBLE root")
print(f"     f''(r_0) = {fpp(r0, MN):+.4f}   (exact: -6/alpha^2 = {-6/al**2:.4f})")
assert abs(f(r0, MN)) < 1e-12 and abs(fp(r0, MN)) < 1e-6
assert abs(fpp(r0, MN) + 6 / al**2) < 1e-3
print()
print("  so |f| ~ 3 (r-r_0)^2/alpha^2  and  1/sqrt|f| ~ alpha/(sqrt3 |r-r_0|) : a SIMPLE POLE.")
print()
print(f"  {'cutoff d':>10} {'INT_{r_0+d}^{r_0+0.05} dr/sqrt|f|':>34} {'(alpha/sqrt3) ln(0.05/d)':>26}")
for d in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    I, _ = quad(lambda r: 1 / np.sqrt(abs(f(r, MN))), r0 + d, r0 + 0.05, limit=800)
    pred = (al / np.sqrt(3)) * np.log(0.05 / d)
    print(f"  {d:>10.0e} {I:>34.4f} {pred:>26.4f}")
    assert abs(I - pred) < 0.05 * max(pred, 1.0)
print()
print("  ** LOGARITHMICALLY DIVERGENT, at exactly the rate alpha/sqrt3 per e-fold. **")
print("  ⌗ *and that is the very exponent `P14_leaf_compactness`'s own CONTROL identifies as")
print("     non-integrable -- the control fabricates a simple pole to show the test has teeth,")
print("     and the Nariai member supplies one for free.*")

# ============================================================================
print()
print("=" * 78)
print("PART 3 — FINITE ON THE WHOLE OPEN FAMILY, INFINITE AT ITS ENDPOINT")
print("=" * 78)
print(f"  {'M/M_N':>8} {'r_b':>9} {'r_c':>9} {'INT_{r_b}^{r_c} dr/sqrt f':>26} {'pi alpha/sqrt3':>16}")
tgt = np.pi * al / np.sqrt(3)
for frac in (0.5, 0.9, 0.99, 0.999, 0.99999):
    M = frac * MN
    rr = roots(M)
    a_, b_ = rr[1], rr[2]
    I, _ = quad(lambda r: 1 / np.sqrt(f(r, M)), a_, b_, points=[a_, b_], limit=800)
    print(f"  {frac:>8.5f} {a_:>9.5f} {b_:>9.5f} {I:>26.5f} {tgt:>16.5f}")
print()
print(f"  ** the between-horizon length tends to pi alpha/sqrt3 = {tgt:.5f} as the roots merge **")
print("     -- finite for every M < M_N.  But AT M = M_N the f > 0 region has closed up, both")
print("     approaches to r_0 run through f < 0, and PART 2's divergence is what is left.")
print()
print("  ⇒ ** the leaf's total proper length is FINITE on the whole open family and INFINITE at")
print("     its endpoint: a DISCONTINUITY, not a limit. **")

# ============================================================================
print()
print("=" * 78)
print("PART 4 — AND THE WALLS THEMSELVES ARE FINE, AT EVERY MEMBER")
print("=" * 78)
print("  P14's three zero-modes sit at r = 0 on the throat circle.  Near r = 0, |f| ~ 2M/|r|, so")
print("  1/sqrt|f| ~ sqrt(|r|/2M) -> 0 : integrable, and integrable at EVERY member including")
print("  Nariai.  ** The modes' own locus is not where the trouble is. **")
print()
print(f"  {'M/M_N':>8} {'INT_{eps}^{0.1} dr/sqrt|f|, eps->0':>34}")
for frac in (0.5, 1.0):
    M = frac * MN
    vals = [quad(lambda r: 1 / np.sqrt(abs(f(r, M))), e, 0.1, points=[e], limit=400)[0]
            for e in (1e-2, 1e-6, 1e-10)]
    print(f"  {frac:>8.4f} {'  '.join(f'{v:.5f}' for v in vals):>34}")
    assert abs(vals[-1] - vals[-2]) < 1e-3
print("  ** converges at both members: the r = 0 crossing is integrable throughout. **")
print("  ⌗ *so this finding is about the FRONT SEAM at the far end of the same closed slicing,")
print("     not about the walls the generations are counted on.*")

print()
print("=" * 78)
print("THE QUESTION, AND WHAT IS NOT CLAIMED")
print("=" * 78)
for line in [
 "** ON WHICH MEMBER IS P14's LEAF? **  The sentence does not say, and the answer decides whether",
 "this is a clause or a repair:",
 "",
 "  · GENERIC member (the receipt's reading): everything is right; what is owed is a clause saying",
 "    the claim holds for M < M_N and fails at the degenerate member.",
 "  · NARIAI member: 'the leaf is compact' is false there, and with it 'the Dirac operator on it",
 "    carries a well-defined analytical index dim ker'.  The argument would need a different",
 "    measure, a regularisation at the double root, or an explicit restriction to M < M_N.",
 "",
 "⚠ NOT CLAIMED:",
 "  · No claim that the generation count is wrong.  The three walls are at r = 0, integrable at",
 "    every member (PART 4).",
 "  · No claim that `P14_leaf_compactness` is wrong.  It is a good receipt and every check in it",
 "    passes at the member it runs.",
 "  · No claim about which member the corpus INTENDS -- that is the source's, and the receipt and",
 "    the surrounding papers point different ways, which is the whole of the finding.",
 "  · No closure on any registered item.",
]:
    print("  " + line)
