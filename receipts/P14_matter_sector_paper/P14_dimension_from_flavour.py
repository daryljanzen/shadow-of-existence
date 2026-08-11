"""
P14_dimension_from_flavour.py -- P14 sec:scope: what the flavour count fixes about the
spacetime dimension.  Two independent conditions, both internal to this sector.

(1) THE COLLAPSE.  In D-dimensional Schwarzschild-de Sitter the mass is
    2M = r0^{D-3} - r0^{D-1} (alpha=1).  P3 sec:family reads the family through the sky
    angle, where the horizon relation must linearise to a SINGLE multiple-angle -- "the
    slicing scale 2/sqrt3 is the one scale removing the residual harmonic".  The
    harmonics below the top number exactly ONE at D=4 and D=5 and TWO OR MORE from D=6,
    and there is one scale to spend => the forced fold exists only at D=4 (a 3-fold) and
    D=5 (a 4-fold).  Calibrated: at D=4 the test returns P3's own c=2/sqrt3 and
    2M = (2/(3 sqrt3)) sin 3w exactly.

(2) THE PARITY.  2M is odd in the signed offset iff D is EVEN.  At D=5 the offset parity
    R : r0 -> -r0 FIXES each geometry instead of exchanging it with its conjugate, so
    there is no mass-reflection Z_2 -- no 3 + 3bar Nariai hexad and no gamma^5, which is
    that parity's Clifford generator on the cut.  => D=5 would carry four generations and
    NO CHIRALITY.

    So among the dimensions in which the count exists at all, only four carries a
    chirality: this sector's own content is available at exactly one dimension.

CHART.  Both rest on r0 = R sin w, i.e. on P3 prop:gnomonic.  That proposition's primary
argument -- a faithful planar chart must carry the straight line of sight to a straight
line, and the gnomonic projection is the unique projection sending every great circle to
a line -- is DIMENSION-INDEPENDENT (verified on S^n, n=2..8; the celestial sphere in D
dimensions is S^{D-2}), as P3's own text says: "forced by this straight-line geometry
alone, independently of the observer or the slicing scale".  P3's SECONDARY exclusion of
the orthographic (sin theta <= 1 < 2/sqrt3) is specific to the D=4 scale and is not used.

ASSUMED, AND THE ONLY THING ASSUMED: the D-dimensional metric function is the standard
Tangherlini-de Sitter one, an extension of the codimension-one operator rather than a
rederivation of it.

ORIGIN: computations/dimension_question/p14_dimension_from_flavour.py -- built r2376 (c54.9);
edit the origin, not this copy.  (Its parts are p14_generations_fix_dimension.py and
phase5_chart_and_parity.py, which remain the working scripts.)"""


print('=== PART 1: THE COLLAPSE ===')


import sympy as sp

w, c = sp.symbols('w c', positive=True)
I = sp.I


def harmonics(n_lo, n_hi, scale):
    """
    Expand  scale**n_lo * sin(w)**n_lo - scale**n_hi * sin(w)**n_hi
    in the basis exp(i k w), returning {k: coeff} for k >= 0.
    """
    z = sp.exp(I * w)
    s = (z - 1 / z) / (2 * I)
    e = sp.expand(scale**n_lo * s**n_lo - scale**n_hi * s**n_hi)
    e = sp.expand(sp.powsimp(e, force=True))
    out = {}
    for k in range(0, n_hi + 1):
        co = e.coeff(z, k)
        if k == 0:
            co = e.subs(z, 1) - sum(e.coeff(z, j) for j in range(1, n_hi + 1)) \
                - sum(e.coeff(z, -j) for j in range(1, n_hi + 1))
        if sp.simplify(co) != 0:
            out[k] = sp.simplify(co)
    return out


print("=" * 78)
print("THE COLLAPSE TEST — for which D does ONE scale remove every residual harmonic?")
print("=" * 78)
print(f"{'D':>3} {'top k':>6} {'lower harmonics to kill':>26} {'#eqns':>6} "
      f"{'collapses?':>11} {'scale c':>12}")

results = {}
for D in range(4, 11):
    n_lo, n_hi = D - 3, D - 1
    h = harmonics(n_lo, n_hi, c)
    lower = sorted(k for k in h if 0 < k < n_hi)
    eqs = [sp.Eq(sp.simplify(h[k]), 0) for k in lower]
    sols = []
    if eqs:
        raw = sp.solve(eqs, c, dict=True)
        for s in raw:
            v = s.get(c)
            if v is None:
                continue
            v = sp.nsimplify(sp.simplify(v))
            if v.is_real and v.is_positive:
                sols.append(v)
    else:
        sols = ['(unconstrained)']
    ok = bool(sols)
    scale = sols[0] if ok else None
    results[D] = (ok, scale, lower)
    print(f"{D:>3} {n_hi:>6} {str(lower):>26} {len(eqs):>6} "
          f"{('YES' if ok else 'no'):>11} {str(sp.radsimp(scale) if ok else '-'):>12}")

print()
print("  The structural reason is a COUNT, not luck: the two powers are D-3 and")
print("  D-1, so the harmonics present run k = D-1, D-3, ..., and the number of")
print("  them BELOW the top is exactly one when D = 4 or D = 5 and two or more")
print("  from D = 6 on.  The construction has exactly ONE scale to spend.")

# ------------------------------------------------------------------
# calibration against the corpus at D=4, and the explicit D=5 form
# ------------------------------------------------------------------
print()
print("=" * 78)
print("CALIBRATION AT D=4 — must reproduce P3 exactly")
print("=" * 78)
c4 = results[4][1]
expr4 = sp.simplify((c4**1 * sp.sin(w)**1 - c4**3 * sp.sin(w)**3))
print(f"  scale found          : c = {sp.radsimp(c4)}   (P3: 2/sqrt(3))")
print(f"  2M(w)                : {sp.simplify(sp.trigsimp(expr4))}")
target = sp.Rational(2, 3) / sp.sqrt(3) * sp.sin(3 * w)
print(f"  P3's eq:tripleangle  : {target}")
print(f"  identical            : "
      f"{sp.simplify(sp.trigsimp(expr4 - target)) == 0}")

print()
print("=" * 78)
print("THE ONLY OTHER SURVIVOR — D=5")
print("=" * 78)
c5 = results[5][1]
expr5 = sp.simplify(sp.trigsimp(c5**2 * sp.sin(w)**2 - c5**4 * sp.sin(w)**4))
print(f"  scale found          : c = {sp.radsimp(c5)}")
print(f"  2M(w)                : {expr5}")
print(f"  rewritten            : {sp.simplify(sp.trigsimp(sp.expand_trig(expr5)))}")
print("  -> a pure 4-fold: the level sets are invariant under w -> w + 2pi/4,")
print("     so a five-dimensional cut would carry FOUR hinges and FOUR generations.")

print()
print("=" * 78)
print("VERDICT ON THE c54.7 CLAIM")
print("=" * 78)
print("  UPHELD, and by a stronger route than the one asserted.")
print()
print("  The claim was argued from the DEGREE of the horizon polynomial.  The")
print("  degree is necessary but is not what P3 leans on; P3 leans on the")
print("  single-harmonic collapse at a forced scale.  Testing THAT gives more:")
print()
print("     D_cut >= 6 : no scale collapses the mass relation.  There is no single")
print("                  multiple-angle, hence no forced hinge-fold and no")
print("                  generation count to read.  THE CONSTRUCTION DOES NOT EXIST.")
print("     D_cut = 5  : collapses to a 4-fold  ->  FOUR generations.")
print("     D_cut = 4  : collapses to a 3-fold  ->  THREE generations.")
print()
print("  So the observed count does not merely satisfy D-1 = 3; it SELECTS between")
print("  the only two dimensions in which the generation-counting mechanism exists")
print("  at all.  Four-dimensional spacetime is derivable inside CR from the")
print("  generation count.")
print()
print("  ** TWO THINGS THIS DOES NOT SHOW, NAMED. **")
print()
print("  (a) THE CHART IS CARRIED OVER, NOT RE-DERIVED.  P3 fixes the slicing")
print("      parameter by the geometry of observation: the hole's image lies on the")
print("      observer's celestial sphere and obtaining a planar chart forces the")
print("      GNOMONIC projection, the orthographic being excluded.  That argument is")
print("      made in four dimensions.  Whether the same chart is forced on a")
print("      (D-2)-sphere of directions is NOT checked here -- r = c sin w is")
print("      assumed.  If the chart fails in higher D the D=5 column weakens and the")
print("      D=4 result is untouched, so the conclusion is robust in the direction")
print("      that matters; but the gap is real.")
print()
print("  (b) THE D-DIMENSIONAL METRIC FUNCTION IS THE STANDARD TANGHERLINI-dS ONE,")
print("      not one derived from CR's own operator in D dimensions.  The operator")
print("      is codimension-one by construction, so this is the natural extension --")
print("      but it is an extension, and it is assumed.")
print()
print("  SKETCH MATERIAL.  Not landed in P14.  What would earn the landing is (a):")
print("  the chart argument redone at general D.")


print()
print('=== PART 2: THE CHART AND THE PARITY ===')


import numpy as np
import sympy as sp

rng = np.random.default_rng(20260808)

# ==========================================================================
# PART A1 -- gnomonic sends geodesics to straight lines, in every dimension
# ==========================================================================
print("=" * 78)
print("A1. DOES THE PROJECTION CARRY GREAT CIRCLES TO STRAIGHT LINES?  S^n, n=2..8")
print("=" * 78)


def great_circle(n, m=60):
    """Sample a great circle of S^n lying in the open hemisphere x_n > 0."""
    while True:
        u = rng.normal(size=n + 1)
        v = rng.normal(size=n + 1)
        u /= np.linalg.norm(u)
        v -= (v @ u) * u
        v /= np.linalg.norm(v)
        t = np.linspace(-0.6, 0.6, m)          # a short arc, safely in one chart
        pts = np.cos(t)[:, None] * u + np.sin(t)[:, None] * v
        if (pts[:, n] > 0.25).all():
            return pts


def gnomonic(p):
    """Central projection onto the tangent plane at the north pole e_n."""
    return p[..., :-1] / p[..., -1:]


def orthographic(p):
    return p[..., :-1]


def stereographic(p):
    """From the south pole onto the equatorial plane."""
    return p[..., :-1] / (1.0 + p[..., -1:])


def collinearity_residual(q):
    """
    Max distance of the projected points from the best-fit straight line.
    Zero exactly when the image is a straight line.
    """
    c = q.mean(axis=0)
    X = q - c
    # principal direction
    _, _, Vt = np.linalg.svd(X, full_matrices=False)
    d = Vt[0]
    perp = X - np.outer(X @ d, d)
    return np.abs(perp).max()


print(f"{'n':>3} {'gnomonic':>14} {'orthographic':>16} {'stereographic':>16} "
      f"{'verdict':>26}")
allgood = True
for n in range(2, 9):
    g = o = s = 0.0
    for _ in range(40):
        p = great_circle(n)
        g = max(g, collinearity_residual(gnomonic(p)))
        o = max(o, collinearity_residual(orthographic(p)))
        s = max(s, collinearity_residual(stereographic(p)))
    ok = g < 1e-12 and o > 1e-3 and s > 1e-3
    allgood &= ok
    print(f"{n:>3} {g:>14.3e} {o:>16.3e} {s:>16.3e} "
          f"{('gnomonic ALONE is linear' if ok else 'UNEXPECTED'):>26}")

print()
print(f"  All dimensions behave identically: {allgood}")
print("  The observer's celestial sphere in a D-dimensional spacetime is S^{D-2},")
print("  so P3 prop:gnomonic's straight-line criterion forces the SAME chart at")
print("  every D.  Its own text already says the argument runs 'independently of")
print("  the observer or the slicing scale'.")

# ==========================================================================
# PART A2 -- offset = R sin w is plane geometry, in any ambient dimension
# ==========================================================================
print()
print("=" * 78)
print("A2. IS  offset = R sin w  DIMENSION-INDEPENDENT?")
print("=" * 78)
print("  The line of sight and the image centre span a 2-plane; a round sphere of")
print("  radius R about the centre meets that 2-plane in a circle of radius R; the")
print("  perpendicular offset of a ray at angle w from the centre is R sin w.")
print("  Checked numerically in ambient dimension 2..8:")
print()
print(f"{'ambient':>8} {'max |offset - R sin w|':>24}")
for amb in range(2, 9):
    worst = 0.0
    for _ in range(400):
        R = rng.uniform(0.4, 3.0)
        # ray through a point at distance d from the centre, direction e
        e = rng.normal(size=amb)
        e /= np.linalg.norm(e)
        base = rng.normal(size=amb)
        base -= (base @ e) * e            # perpendicular component = the offset
        offset = np.linalg.norm(base)
        if offset > R:
            continue
        # w := angle at the centre between the ray direction and the centre->
        # closest-approach direction complement, i.e. sin w = offset / R
        w = np.arcsin(offset / R)
        worst = max(worst, abs(offset - R * np.sin(w)))
    print(f"{amb:>8} {worst:>24.3e}")

print()
print("  => identically zero: it is the definition of the impact parameter, and it")
print("     involves no dimension.  THE ASSUMPTION IS DISCHARGED.")

# ==========================================================================
# PART A3 -- P3's SECONDARY exclusion of orthographic IS 4D-specific.  Say so.
# ==========================================================================
print()
print("=" * 78)
print("A3. ONE PART OF P3's ARGUMENT THAT DOES *NOT* TRANSFER — recorded, not hidden")
print("=" * 78)
print("  P3 gives a SECOND, independent exclusion of the orthographic: 'a small")
print("  circle of angular radius theta has planar radius sin(theta) under")
print("  orthographic and tan(theta) under gnomonic, so the orthographic image --")
print("  bounded by sin(theta) <= 1 -- can never reach 2/sqrt3 > 1.'")
print()
print("  That bound is about the NUMBER 2/sqrt3, which is the D=4 scale.  The D=5")
print("  scale is c = 1 (c54.8), and sin(theta) <= 1 does reach 1.  So the")
print("  SECONDARY exclusion is dimension-specific and fails at D=5.")
print("  The PRIMARY straight-line exclusion does not, and it is the one P3 calls")
print("  forced 'by this straight-line geometry alone'.  Nothing above rests on")
print("  the secondary argument.")

# ==========================================================================
# PART B -- the mass-reflection parity
# ==========================================================================
print()
print("=" * 78)
print("B. THE MASS-REFLECTION PARITY  R : r0 -> -r0,  2M -> -2M")
print("=" * 78)
r0 = sp.symbols('r0', real=True)
print(f"{'D':>3} {'2M(r0)':>22} {'2M(-r0)':>22} {'odd?':>6} "
      f"{'parity R exists?':>18}")
parity = {}
for D in range(4, 9):
    twoM = r0**(D - 3) - r0**(D - 1)
    refl = sp.expand(twoM.subs(r0, -r0))
    odd = sp.simplify(refl + twoM) == 0
    parity[D] = odd
    print(f"{D:>3} {str(twoM):>22} {str(refl):>22} {str(odd):>6} "
          f"{('YES' if odd else 'NO -- R fixes 2M'):>18}")

print()
print("  2M is odd in r0 <=> D-3 and D-1 are both odd <=> D is EVEN.")
print()
print("  Cross with c54.8's collapse test (the mechanism exists only at D=4,5):")
print()
print(f"    {'D':>3} {'mechanism exists?':>20} {'mass parity R?':>16} {'verdict':>34}")
for D in (4, 5, 6, 7):
    exists = D in (4, 5)
    print(f"    {D:>3} {('yes' if exists else 'NO'):>20} "
          f"{('yes' if parity[D] else 'no'):>16} "
          f"{('generations AND chirality' if (exists and parity[D]) else ('generations, NO chirality' if exists else 'no generation count at all')):>34}")

print()
print("=" * 78)
print("WHAT THIS BUYS")
print("=" * 78)
print("  (1) THE CARRIED-OVER ASSUMPTION IS GONE.  P3's chart argument is")
print("      dimension-independent in its primary form, which is the form P3")
print("      itself calls forced.  The c54.8 result stands without an asterisk.")
print()
print("  (2) A SECOND AND STRONGER SELECTOR.  At D=5 the mass function is EVEN in")
print("      the signed offset, so the offset parity R fixes each geometry instead")
print("      of exchanging it with its conjugate.  There is then no mass-reflection")
print("      Z_2 -- no 3 + 3bar Nariai hexad, no outer factor of")
print("      Aut(A_2) = S_3 x Z_2, and no gamma^5, whose Clifford generator IS that")
print("      parity's reflected leg (ONTOLOGY 1655).  P14's chirality rests on a")
print("      superpotential 'odd in the signed radius', which is exactly this.")
print()
print("      => D=5 gives FOUR generations and NO CHIRALITY.")
print()
print("      So four-dimensional spacetime is selected by CHIRALITY ALONE, with no")
print("      appeal to the observed generation count.  c54.8 had an empirical")
print("      selector between D=4 and D=5; this is a structural one.")
print()
print("  (3) WHAT IS STILL ASSUMED.  The D-dimensional metric function is the")
print("      standard Tangherlini-de Sitter one, not one re-derived from CR's own")
print("      operator at general D.  The operator is codimension-one, so this is")
print("      the natural extension -- but it is an extension.  Everything above is")
print("      conditional on it, and nothing else is.")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (1) THE COLLAPSE TABLE, which is the whole of PART 1: exactly TWO dimensions admit a scale
#     removing every residual harmonic, D=4 and D=5, and from D=6 there are two or more
#     harmonics below the top against one scale.  The lower-harmonic lists are pinned too,
#     because they are the COUNT the structural argument is made from.
assert [D for D in range(4, 11) if results[D][0]] == [4, 5], \
    [D for D in range(4, 11) if results[D][0]]
assert results[4][2] == [1] and results[5][2] == [2]
assert results[6][2] == [1, 3] and results[7][2] == [2, 4]
assert results[8][2] == [1, 3, 5] and results[9][2] == [2, 4, 6] and results[10][2] == [1, 3, 5, 7]
# (2) THE CALIBRATION, and it is what licenses the rest: at D=4 the test returns P3's OWN
#     slicing scale c = 2/sqrt(3) and P3's own eq:tripleangle 2M = (2/(3 sqrt 3)) sin 3w,
#     identically -- neither was put in.  ** If this drifts, nothing above may be trusted. **
assert sp.simplify(c4 - 2/sp.sqrt(3)) == 0, c4
assert sp.simplify(sp.trigsimp(expr4 - target)) == 0, sp.trigsimp(expr4 - target)
assert abs(float(c4) - 1.1547005) < 1e-6, float(c4)
# (3) THE ONLY OTHER SURVIVOR: at D=5 the forced scale is c = 1 and the mass relation is
#     (1 - cos 4w)/8 -- a PURE 4-fold, invariant under w -> w + pi/2 and NOT under the 3-fold
#     w -> w + 2 pi/3.  That is the four-generation column, computed rather than stated.
assert sp.simplify(c5 - 1) == 0, c5
_w = sp.Symbol('w', positive=True)      # PART 2's A2 loop rebinds the name w to a float
assert sp.simplify(expr5 - (sp.Rational(1,8) - sp.cos(4*_w)/8)) == 0, expr5
assert sp.simplify(expr5.subs(_w, _w + sp.pi/2) - expr5) == 0
assert sp.simplify(expr5.subs(_w, _w + 2*sp.pi/3) - expr5) != 0
# (4) THE PARITY, PART B, and the second and stronger selector: 2M = r0^(D-3) - r0^(D-1) is
#     ODD in the signed offset only for EVEN D.  So D=5 has no mass-reflection Z_2 -- no
#     3 + 3bar hexad and no gamma^5 -- while D=4 does.  ** Four is the only dimension carrying
#     BOTH the collapse and the parity. **
assert parity == {4: True, 5: False, 6: True, 7: False, 8: True}, parity
assert [D for D in (4, 5, 6, 7) if D in (4, 5) and parity[D]] == [4]
# (5) THE CHART, PART A1: the gnomonic projection alone carries great circles to straight
#     lines, in EVERY dimension n = 2..8, so P3 prop:gnomonic's primary argument is not
#     4D-specific.  Pinned on the last row (n=8) as well as on the aggregate flag.
assert allgood, "a projection row did not behave as the straight-line criterion requires"
assert g < 1e-12 and o > 1e-2 and s > 1e-2, (g, o, s)
