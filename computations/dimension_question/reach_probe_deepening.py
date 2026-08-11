#!/usr/bin/env python3
"""
RE-RUNNING THE REACH PROGRAMME'S OWN PROBES AT GENERAL DIMENSION.

The field bakes (R-M) and the domain bakes (R-P) were run against a four-dimensional
cut, and their constants were read as structural because nothing in the corpus then
distinguished "structural" from "true at D=4".  The dimension result supplies that
distinction, so each probe whose verdict turns on a D=4 number is owed a re-run.

This is not annotation.  Each section re-derives the probe's own computation at
general D and reports whether the verdict survives, narrows, or was dimension-specific
all along.  A probe that survives is strengthened; a probe that does not is a finding.

  P1  QUADRIC Q4   -- the vantage cross-ratio.  Q4 discounted itself: "three points
                      120 degrees apart with their centre are equianharmonic
                      AUTOMATICALLY ... this names a consequence of a forced fact and
                      does not add one."  Does the configuration even ADMIT a
                      projective invariant at other D?
  P2  QUADRIC 4d   -- the untried queue's last entry: "CR has three hinges and a
                      centre; is that a polar simplex?"  Answer it, and ask at which D
                      the question exists.
  P3  OPTICS O1    -- "the photon sphere IS the merged horizon at Nariai ... P7's
                      tangency condition and the photon-sphere condition are ONE
                      condition."  At general D?
  P4  OPTICS O6    -- "2f - r^2 f'' ... is THE CONSTANT 2 for every r and every M", so
                      Omega_c = lambda and the ringdown quality factor is "universal
                      across the whole family, independent of M and alpha".  At general D?
  P5  CATEGORY K5  -- Nariai's six faces reduce to one condition, the sixth being the
                      near-horizon dS_2 x S^2 with a six-dimensional isotropy "against
                      a generic four".  At general D?
  P6  CATEGORY K8b -- the dimension-7 orbit stratum is EMPTY because "so(4) already
                      uses all four spacelike directions".  Is that the cut's
                      four-dimensionality doing the work?

Run: python3 reach_probe_deepening.py     (numpy, sympy)
"""



import numpy as np
import sympy as sp

r, w, M, a = sp.symbols('r w M alpha', positive=True)
print(__doc__.split("Run:")[0])


def f_D(D):
    """Tangherlini-de Sitter metric function, alpha = 1."""
    return 1 - 2 * M / r**(D - 3) - r**2


# =====================================================================
print("=" * 78)
print("P1. QUADRIC Q4 — does the vantage configuration admit a cross-ratio at all?")
print("=" * 78)
print("  Q4's object: the D-1 designated offsets (the vantages) TOGETHER WITH the")
print("  centre.  A cross-ratio is an invariant of FOUR points.  The configuration")
print("  has (D-1) + 1 = D points.")
print()
print(f"{'D':>3} {'vantages':>9} {'points incl. centre':>20} "
      f"{'a single cross-ratio?':>23}")
for D in range(4, 9):
    n = D - 1
    print(f"{D:>3} {n:>9} {n+1:>20} "
          f"{('YES — exactly four' if n + 1 == 4 else 'no — ' + str(n+1) + ' points'):>23}")
print()
print("  => the vantage set is a cross-ratio configuration PRECISELY at D = 4.")
print()
# and the value, at D=4, from the three preimages of 3w
print("  Q4's value, recomputed, and the D=5 comparison done on the natural analogue")
print("  (the D-1 equally-spaced dial points on the unit circle, cross-ratio of the")
print("  first four; at D=4 the fourth point is the centre, as Q4 takes it):")
print()
print(f"{'D':>3} {'config':>28} {'cross-ratio':>28} {'name':>16}")
# D=4: three cube roots of unity + centre 0
z3 = [sp.exp(2 * sp.pi * sp.I * k / 3) for k in range(3)]
cr4 = sp.simplify(((z3[0] - z3[2]) * (z3[1] - 0)) / ((z3[1] - z3[2]) * (z3[0] - 0)))
cr4 = sp.simplify(sp.expand(cr4))
print(f"{4:>3} {'3 cube roots + centre':>28} {str(sp.nsimplify(cr4)):>28} "
      f"{'equianharmonic':>16}")
z4 = [sp.exp(2 * sp.pi * sp.I * k / 4) for k in range(4)]
cr5 = sp.simplify(((z4[0] - z4[2]) * (z4[1] - z4[3])) / ((z4[1] - z4[2]) * (z4[0] - z4[3])))
print(f"{5:>3} {'4 fourth roots (no centre)':>28} {str(sp.nsimplify(cr5)):>28} "
      f"{'harmonic':>16}")
print()
print("  So even where a four-point subset exists at D=5 it is HARMONIC (lambda = -1,")
print("  j = 1728, complex multiplication by i), not equianharmonic (lambda = e^{i pi/3},")
print("  j = 0, CM by omega).  Q4's chain 'equianharmonic <=> j=0 <=> CM by omega --")
print("  which is the corpus's own Z_3 deck action' therefore holds AT D=4 and points")
print("  the other way at D=5.")
print()
print("  ⇒ Q4's self-discount is too strong.  The 120 degrees is automatic GIVEN three,")
print("     but the three is D-1 and the configuration is a cross-ratio configuration")
print("     only at D=4.  ⚠ NOT a second vote for D=4: it is the same fold read")
print("     projectively.  What it is, is a REASON the equianharmonic value is there.")

# =====================================================================
print()
print("=" * 78)
print("P2. QUADRIC 4d (untried) — 'CR has three hinges and a centre; is that a polar")
print("    simplex?'  ANSWERED, and the question turns out to exist only at D=4.")
print("=" * 78)
print("  A self-polar triangle w.r.t. a circle of radius alpha: each vertex's polar")
print("  line is the opposite side.  The polar of a point at distance d is the line at")
print("  distance alpha^2/d, perpendicular to it, on the same side.")
print()
d_hinge = 2                      # hinge distance, alpha = 1
polar_dist = sp.Rational(1, 1)**2 / d_hinge
inradius = sp.cos(sp.pi / 3) * d_hinge          # equilateral: r_in = R cos(60 deg)
print(f"  hinge distance                 : {d_hinge} alpha")
print(f"  polar line of a hinge sits at  : alpha^2/(2 alpha) = {polar_dist} alpha")
print(f"  the OPPOSITE SIDE sits at      : the inradius = {sp.nsimplify(inradius)} alpha")
print(f"  equal?                         : {sp.simplify(polar_dist - inradius) == 0}")
print()
print("  ⇒ NO.  The hinge triangle is NOT self-polar w.r.t. the throat.  A computed")
print("     negative, and it closes the quadric ledger's last untried entry.")
print()
print("  And the question is dimension-bound in a way the queue could not see:")
print(f"{'D':>3} {'hinges':>8} {'a simplex in the plane?':>26}")
for D in range(4, 9):
    n = D - 1
    print(f"{D:>3} {n:>8} {('YES — 3 points is a triangle' if n == 3 else 'no — ' + str(n) + '-gon'):>26}")
print()
print("  ⇒ 'is the hinge figure a polar simplex' is a question that only EXISTS at")
print("     D=4, and there the answer is no.  Both halves are new.")

# =====================================================================
print()
print("=" * 78)
print("P3. OPTICS O1 — is 'photon sphere = merged horizon at Nariai' a D=4 accident?")
print("=" * 78)
print(f"{'D':>3} {'r_photon':>16} {'r_Nariai':>20} {'coincide?':>11}")
o1 = True
for D in range(4, 9):
    fD = f_D(D)
    # photon sphere: d/dr (f/r^2) = 0
    rph = sp.solve(sp.simplify(sp.diff(fD / r**2, r)), r)
    rph = [sp.simplify(x) for x in rph]
    rph = [x for x in rph if x.is_real is not False]
    # Nariai: f = f' = 0 solved jointly for (r, M)
    sol = sp.solve([sp.Eq(fD, 0), sp.Eq(sp.diff(fD, r), 0)], [r, M], dict=True)
    rN = None
    for s in sol:
        v = sp.simplify(s[r])
        if v.is_real and v.is_positive:
            rN = sp.nsimplify(v)
            MN = sp.nsimplify(sp.simplify(s[M]))
    rph_at_N = sp.nsimplify(sp.simplify(rph[0].subs(M, MN))) if rph else None
    same = sp.simplify(rph_at_N - rN) == 0 if rph_at_N is not None else False
    o1 &= bool(same)
    print(f"{D:>3} {str(rph_at_N):>16} {str(rN):>20} {str(same):>11}")
print()
print(f"  O1's identity holds in every dimension tested: {o1}")
print("  ⇒ NOT a D=4 accident.  O1 is STRENGTHENED: 'P7's tangency condition and the")
print("     photon-sphere condition are one condition' is dimension-independent, so it")
print("     is a statement about the degenerate horizon as such, not about the cubic.")
print("     The ledger may now say so; it currently cannot know it.")

# =====================================================================
print()
print("=" * 78)
print("P4. OPTICS O6 — is '2f - r^2 f'' = the constant 2' structural or D=4?")
print("=" * 78)
print(f"{'D':>3} {'2f - r^2 f_rr':>34} {'constant?':>11}")
for D in range(4, 9):
    fD = f_D(D)
    expr = sp.simplify(2 * fD - r**2 * sp.diff(fD, r, 2))
    const = sp.simplify(sp.diff(expr, r)) == 0
    print(f"{D:>3} {str(sp.simplify(expr)):>34} {str(const):>11}")
print()
print("  ⇒ THE CONSTANT 2 IS A D=4 FACT.  From D=5 the combination carries an")
print("     r-dependent mass term, so Omega_c = lambda fails and O6's 'the ringdown's")
print("     SHAPE is universal across the whole family, independent of M and alpha'")
print("     needs its dimension clause.  The claim is TRUE and its stated scope is")
print("     WIDER THAN ITS COMPUTATION — the failure class the figure ledger's own")
print("     r1110 audit names as the check to run on every future entry.")

# =====================================================================
print()
print("=" * 78)
print("P5. CATEGORY K5 — Nariai's near-horizon isotropy, at general D")
print("=" * 78)
print("  At a double root the near-horizon geometry is dS_2 x S^(D-2), with isometry")
print("  SO(2,1) x SO(D-1).  K5's sixth face is that this is 'six-dimensional against a")
print("  generic four'.")
print()
print(f"{'D':>3} {'near-horizon':>18} {'dim isotropy':>13} {'generic (R_t x SO(D-2))':>24} "
      f"{'enhancement':>12}")
for D in range(4, 9):
    # the near-horizon sphere is S^(D-2); its isometry is so(D-1), NOT so(D-2).
    # An earlier version of this section used so(D-2) and returned (4,2) at D=4,
    # contradicting K5's own (6,4).  Caught by checking against the ledger's stated
    # numbers before propagating.  The +2 conclusion was unaffected; the table was not.
    sphere = (D - 1) * (D - 2) // 2               # dim so(D-1), acting on S^(D-2)
    dim_nh = 3 + sphere                            # so(2,1) + so(D-1)
    dim_gen = 1 + sphere                           # R_t     + so(D-1)
    print(f"{D:>3} {'dS_2 x S^' + str(D-2):>18} {dim_nh:>13} {dim_gen:>24} "
          f"{dim_nh - dim_gen:>12}")
print()
print("  ⇒ the ENHANCEMENT is +2 in every dimension — K5's mechanism survives — but")
print("     the NUMBERS 6 and 4 are D=4 values.  K5's sixth face should be stated as")
print("     the enhancement, not as the pair (6,4).  A narrowing, not a kill.")

# =====================================================================
print()
print("=" * 78)
print("P6. CATEGORY K8b — is the empty dimension-7 stratum a cut-dimension fact?")
print("=" * 78)
print("  K8b: 'neither dim-7 pair embeds there -- so(4) already uses all four spacelike")
print("  directions, and so(3,1) leaves only one where a rotation needs two.'")
print()
print("  The isotropy a swept geometry may carry is a subalgebra of so(4,1), and")
print("  so(4,1) is the STABILISER OF A FOUR-DIMENSIONAL CUT.  Its dimension:")
for D in range(4, 9):
    print(f"    cut dimension {4:>2} in dS_{D:<2} : stabiliser so(4,1) x so({D-4}), "
          f"dim so(4,1) = {5*4//2}")
print()
print("  ⇒ the bound K8b argues from is the CUT's four-dimensionality, not the")
print("     substrate's.  With the cut's four now derived, K8b's emptiness proof stops")
print("     being a coincidence of counting and becomes a consequence.  Its own")
print("     wording ('so(4) already uses all four spacelike directions') names the four")
print("     without saying where it comes from.")

print()
print("=" * 78)
print("SUMMARY — what the re-run did to each probe")
print("=" * 78)
rows = [
    ("QUADRIC Q4", "self-discount too strong", "the cross-ratio configuration exists only at D=4"),
    ("QUADRIC 4d", "answered (was untried)", "NOT self-polar; and the question exists only at D=4"),
    ("OPTICS O1", "STRENGTHENED", "the identity is dimension-independent"),
    ("OPTICS O6", "scope wider than computation", "the constant 2 is a D=4 fact"),
    ("CATEGORY K5", "narrowed", "the +2 enhancement survives; the pair (6,4) does not"),
    ("CATEGORY K8b", "grounded", "its four is the cut's, now derived rather than counted"),
]
for k, v, why in rows:
    print(f"  {k:<14} {v:<30} {why}")
print()
print("  Two of six survive unchanged or strengthened, three narrow, one answers an")
print("  open queue item.  NONE of them is a second vote for D=4: every dimension")
print("  statement here descends from the one fold, and counting them again would be")
print("  the trap the figure ledger names -- 'the count matches and the match means")
print("  nothing.  A count is not a map.'")

# --- r2376+c54.159 -----------------------------------------------------------------
# Six probe verdicts, all printed and none checked.  Assert O1's accumulator, and pin
# the numbers each verdict actually turns on: Q4's cross-ratio is equianharmonic
# e^{i pi/3} = 0.5 + 0.8660254037844386 i at D=4 and merely harmonic (= 2) at D=5;
# QUADRIC 4d's polar sits at alpha/2 against an opposite side at alpha (NOT self-polar);
# O1's r_photon = r_Nariai = sqrt(35)/7 at D=8, the last row; O6's combination is the
# constant 2 only at D=4; K5's isotropy dims are (24, 22) at D=8, so (6,4) is a D=4 pair.
assert o1, "O1: r_photon and r_Nariai part company in some dimension"
assert abs(complex(sp.N(cr4)) - complex(0.5, 0.8660254037844386)) < 1e-12
assert sp.simplify(cr5 - 2) == 0
assert polar_dist == sp.Rational(1, 2) and sp.simplify(inradius - 1) == 0
assert sp.simplify(polar_dist - inradius) != 0, "the hinge triangle IS self-polar -- P2 dies"
assert sp.simplify(rph_at_N - sp.sqrt(35)/7) == 0 and sp.simplify(rN - sp.sqrt(35)/7) == 0
assert sp.simplify(2*f_D(4) - r**2*sp.diff(f_D(4), r, 2) - 2) == 0        # O6: constant 2 at D=4
assert sp.simplify(sp.diff(2*f_D(5) - r**2*sp.diff(f_D(5), r, 2), r)) != 0  # ... and not at D=5
assert (dim_nh, dim_gen) == (24, 22)          # D=8, the last row; enhancement still +2
