#!/usr/bin/env python3
"""
PHASE 4 — does a higher substrate still deliver EXACTLY P9's range?

The question was named in c54.7 as not established.  Reading P9 at source settles
its shape: P9's range theorem does NOT quantify over the substrate's full isometry
group.  Its macro is

    \\newcommand{\\so}{\\mathrm{SO}(4,1)}

and thm:bound reads "swept by a subgroup H \\subseteq \\so of the substrate's
isometries".  SO(4,1) is the ISOTROPY of the symmetric space dS_5 = SO(5,1)/SO(4,1)
-- equivalently the stabiliser of a cut.  So P9's bound is stated over the
DENOMINATOR of the coset, not the numerator.

This script checks the three facts that follow.

(1) STABILISER OF A CUT IN dS_D.  A totally geodesic four-geometry in dS_D is the
    intersection with a 5-dimensional linear subspace W of signature (1,4) in the
    ambient M^{D+1} of signature (1,D).  The subgroup of O(D,1) preserving W is
    O(1,4) x O(D-4), acting on W and on W^perp (positive definite, dim D-4).

    => The stabiliser's identity component is  SO(4,1) x SO(D-4).

(2) THE EXTRA FACTOR ACTS TRIVIALLY ON THE CUT.  SO(D-4) moves only W^perp, so the
    induced metric on the cut is untouched.  Any sweep-subgroup H of the stabiliser
    therefore induces on the four-geometry exactly its projection into SO(4,1) --
    which is precisely P9's hypothesis.  P9's range is preserved EXACTLY, for every
    D, provided the descent ends at a four-dimensional cut.

(3) WHAT THE EXTRA FACTOR DOES ACT ON.  The cut's extrinsic data -- the second
    fundamental form II^a_{mu nu} -- carries a normal index a = 1..(D-4).  SO(D-4)
    rotates it.  In CR "matter is the bend of the cut", so SO(D-4) acts on the
    MATTER data while fixing the induced geometry.  That is the definition of an
    INTERNAL symmetry.

    At D=5 the normal space is 1-dimensional: SO(1) is trivial, there is nothing to
    rotate, and any su(3) would have to act on the cut itself -- i.e. SPATIALLY.
    That is exactly P13's constraint C3.  C3 is therefore DIMENSION-CONDITIONAL and
    is stated at D=5.

    so(D-4) contains su(3) iff D-4 >= 6 iff D >= 10.

    *** THIS IS NOT AN INDEPENDENT CONFIRMATION OF PHASE 3'S D>=10. ***
    Phase 3 counted layer(3) disjoint from carrier(6) plus time = 10.  Phase 4
    counts cut(4) plus normals(6) = 10.  The layer sits inside the cut: it is ONE
    constraint in two registers, and the agreement is a consistency check, not
    evidence.  Recorded here so no later reading treats it as two votes.

Run: python3 phase4_range_stability.py     (numpy)
"""

import numpy as np
import itertools

ALPHA = 1.0


def so_dim(n):
    return n * (n - 1) // 2


print(__doc__.split("Run:")[0])
print("=" * 78)
print("(1) STABILISER OF A TOTALLY GEODESIC 4-GEOMETRY IN dS_D")
print("=" * 78)
print(f"{'D':>3} {'dim Iso(dS_D)':>14} {'stabiliser':>22} {'dim stab':>9} "
      f"{'dim moduli':>11}")
for D in range(4, 12):
    amb = D + 1                      # ambient M^{D+1}, signature (1,D)
    iso = so_dim(amb)                # dim so(D,1)
    normals = D - 4                  # dim W^perp
    stab = so_dim(5) + so_dim(normals)   # so(4,1) has dim 10 = so_dim(5)
    label = f"SO(4,1) x SO({normals})" if normals >= 2 else (
        "SO(4,1) x SO(1)=SO(4,1)" if normals == 1 else "SO(4,1)  [D=4: no normals]")
    print(f"{D:>3} {iso:>14} {label:>22} {stab:>9} {iso - stab:>11}")

print()
print("  dim so(4,1) = 10 in every row -- the isotropy P9 quantifies over is")
print("  UNCHANGED by the substrate's dimension.  Only the normal factor grows.")

# ---------------------------------------------------------------------------
# (2) explicit check that the SO(D-4) factor is trivial on the cut
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("(2) THE NORMAL FACTOR ACTS TRIVIALLY ON THE CUT -- explicit check")
print("=" * 78)

rng = np.random.default_rng(20260808)


def eta(p, q):
    """Minkowski metric diag(-1,+1,...,+1) with p timelike (=1 here)."""
    d = np.ones(p + q)
    d[:p] = -1.0
    return np.diag(d)


for D in (5, 7, 10):
    amb = D + 1
    g = eta(1, D)
    # W = span(e0..e4)  (signature (1,4));  W^perp = span(e5..eD)
    nrm = D - 4
    # random element of SO(nrm) acting on W^perp, identity on W
    if nrm >= 2:
        A = rng.normal(size=(nrm, nrm))
        A = A - A.T                              # so(nrm)
        from scipy.linalg import expm            # noqa
        R = expm(A)
    else:
        R = np.eye(max(nrm, 1))
    M = np.eye(amb)
    if nrm >= 1:
        M[5:, 5:] = R[:nrm, :nrm]

    # isometry of the ambient?
    iso_ok = np.allclose(M.T @ g @ M, g, atol=1e-10)

    # sample points of the cut  W \cap dS_D  :  X in W, X.X = alpha^2
    pts = []
    for _ in range(200):
        v = np.zeros(amb)
        v[:5] = rng.normal(size=5)
        s = v @ g @ v
        if s <= 0:
            continue
        v *= ALPHA / np.sqrt(s)
        pts.append(v)
    pts = np.array(pts)

    moved = np.abs(pts @ M.T - pts).max()
    print(f"  D={D:>2}: normal factor SO({nrm}) is an ambient isometry: {iso_ok};"
          f"  max displacement of cut points = {moved:.3e}")

print()
print("  => the normal factor fixes the cut POINTWISE.  Any H in the stabiliser")
print("     induces on the four-geometry exactly its SO(4,1) projection.")
print("     P9 thm:bound and thm:range go through verbatim, for every D.")

# ---------------------------------------------------------------------------
# (3) where su(3) can sit, and P13's C3
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("(3) su(3) IN THE NORMAL FACTOR -- and P13's C3 is dimension-conditional")
print("=" * 78)
print(f"{'D':>3} {'normal factor':>15} {'dim':>5} {'su(3) fits?':>12} "
      f"{'acts on cut?':>13}")
for D in range(4, 13):
    nrm = D - 4
    fits = "yes" if nrm >= 6 else "no"
    acts = "n/a (trivial)" if nrm == 0 else ("no (internal)" if nrm >= 1 else "")
    print(f"{D:>3} {'so(' + str(nrm) + ')':>15} {so_dim(nrm):>5} {fits:>12} "
          f"{acts:>13}")

print()
print("  P13 C3: 'where su(3) CAN act geometrically, it acts SPATIALLY, not")
print("  internally ... a would-be geometric colour is a symmetry of space, which")
print("  the physical cut destroys.'  At D=5 the normal space is 1-dimensional and")
print("  SO(1) is trivial -- there is no internal room, so C3 is forced.  From")
print("  D>=10 the normal factor so(D-4) contains su(3) and acts trivially on the")
print("  cut: internal by construction.  C3 is TRUE AT D=5 and is not a theorem")
print("  about all D.")

# ---------------------------------------------------------------------------
# (4) the honest deficit: the normal bundle's structure group is so(6), not su(3)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("(4) WHAT THIS DOES *NOT* DELIVER")
print("=" * 78)
print("  The structure group of the normal bundle is so(6) (dim 15), not su(3)")
print("  (dim 8).  Reducing so(6) -> u(3) needs an orthogonal COMPLEX STRUCTURE on")
print("  the normal space; u(3) -> su(3) needs a preferred complex volume form.")
print("  Neither is supplied by anything established above.")
print()
print("  So a rise to D>=10 makes colour PERMITTED, not REQUIRED -- which is")
print("  precisely the case R2 condemns as 'no explanation but a description'.")
print("  The gain is not a colour claim; it is that the obstruction has moved from")
print("  'su(3) cannot act internally at all' (true at D=5) to 'what reduces the")
print("  normal structure group?' -- a sharper and answerable question.")
print()
print("  Also untouched: P13's index obstruction (indifferent to product/KK")
print("  structure), P13's C7 (the Wick face), and whether a descent of length >1")
print("  is itself forced by anything.  Nothing is built.")

# ---------------------------------------------------------------------------
# (5) do extra isometries manufacture spurious cuts?
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("(5) SPURIOUS EXTRA STRUCTURE?  -- the moduli, not the catalogue")
print("=" * 78)
print("  SO(D,1) acts transitively on the totally geodesic four-geometries of")
print("  dS_D (it acts transitively on signature-(1,4) 5-planes), so the space of")
print("  cuts is the homogeneous SO(D,1)/(SO(4,1) x SO(D-4)) counted above.  Any")
print("  two such cuts are carried into each other by an ambient isometry, hence")
print("  are ISOMETRIC as four-geometries.")
print()
print("  => a taller substrate adds no new geometry TYPES to the range.  What it")
print("     adds is moduli -- more readings of the same catalogue.  In P9's own")
print("     terms that is the VANTAGE multiplicity axis, which the range paper")
print("     already carries, not a new geometric-multiplicity axis.")
print()
print("  VERDICT: P9's range is stable under a substrate rise, exactly, provided")
print("  the descent ends at a four-dimensional cut -- which is the same condition")
print("  Phase 2 extracted from P12's Dirac-algebra grading.  Phases 2 and 4")
print("  constrain the SAME object: the final coset's isotropy so(4,1).")
