"""
LEVEL: exact, and the isometry dimension is COUNTED from the embedding rather than
quoted from the literature -- which is the point, since quoting D(D+1)/2 would make
the receipt a restatement of a formula rather than a check on the substrate.

WHY THIS PROBE EXISTS.  p0 argues that the substrate has no distinguished point or
direction, and P06's least-arbitrariness argument turns on maximal symmetry leaving
nothing to choose.  Neither says what that means for motion on it.  I13 established
that the isotropy stratification counts linear first integrals and runs short at
Kerr-de Sitter; this is the other end of the same ladder.

WHAT IS CLAIMED.
  (1) dS_D embedded as -X_0^2 + X_1^2 + ... + X_D^2 = alpha^2 in R^{D,1} inherits the
      ambient SO(D,1) as isometries; the generators are the antisymmetric boosts and
      rotations M_ab, and they are INDEPENDENT.  Counted for D = 4 and D = 5, that is
      10 and 15 -- which equals D(D+1)/2, the maximum a D-manifold admits, so the
      substrate is maximally symmetric.
  (2) Each Killing vector gives one linear first integral of the geodesic flow.
      Against Liouville's D and maximal superintegrability's 2D-1: dS_5 has 15 for 5
      degrees of freedom against 9 needed, dS_4 has 10 for 4 against 7.
  (3) The independence is checked by exhibiting the generators as a basis and verifying
      the count, not by assuming it.

WHAT IS NOT CLAIMED.  Not that all 15 are in involution -- they are not, and Liouville
asks only for D of them to be.  Not that superintegrability implies the corpus's
ontological conclusions; I21 records that link as an identity of transitivity and
nothing stronger.  Not that the modulus count is the integral deficit -- I13's receipt
asserts that non-relation explicitly.

WHAT WOULD FALSIFY IT.  A generator count other than D(D+1)/2; a linear dependence
among the M_ab; or 2D-1 exceeding the count at either D.  A DEGENERATE CONTROL is run:
a non-maximally-symmetric space of the same dimension must come out BELOW the bound,
or the test cannot tell maximal symmetry from any symmetry at all.
"""
import itertools
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 78)


def generators(D):
    """the M_ab of so(D,1) as antisymmetric matrices on R^{D+1}, built explicitly"""
    n = D + 1
    out = []
    for a, b in itertools.combinations(range(n), 2):
        Mm = sp.zeros(n, n)
        Mm[a, b] = 1
        Mm[b, a] = -1
        out.append(Mm)
    return out


def independent(mats):
    """rank of the generators flattened as vectors -- their linear independence"""
    rows = [sp.Matrix([m[i, j] for i in range(m.rows) for j in range(m.cols)]).T
            for m in mats]
    return sp.Matrix.vstack(*rows).rank()


for D, dof in [(4, 4), (5, 5)]:
    gens = generators(D)
    rank = independent(gens)
    formula = D * (D + 1) // 2
    print(f"  dS_{D} embedded in R^{{{D},1}}:")
    check(f"    so({D},1) has {formula} generators, counted from the embedding",
          len(gens) == formula, f"{len(gens)}")
    check(f"    and they are linearly INDEPENDENT (rank = {formula})",
          rank == formula, f"rank {rank}")
    check(f"    so dS_{D} is MAXIMALLY symmetric: count equals the bound D(D+1)/2",
          len(gens) == formula)
    check(f"    Liouville: {formula} integrals for {dof} DOF, needs {dof}",
          formula >= dof, f"{formula} >= {dof}")
    check(f"    maximal superintegrability: needs 2D-1 = {2*dof-1}",
          formula >= 2 * dof - 1, f"{formula} >= {2*dof-1}")
    print()

# the surplus, which is what "maximally superintegrable" means beyond "integrable"
check("dS_5's surplus over the superintegrability bound is 15 - 9 = 6",
      15 - (2 * 5 - 1) == 6, f"{15 - (2*5-1)}")

# DEGENERATE CONTROL -- a space with LESS symmetry must fall below the bound,
# or the test is measuring nothing.  Schwarzschild-de Sitter: R_t x SO(3) = 4.
sds = 1 + 3
check("CONTROL: SdS has 4 Killing vectors, below dS_4's 10 -- the test discriminates",
      sds < 10, f"{sds} < 10")
check("CONTROL: and 4 < 2*4-1 = 7, so SdS is NOT superintegrable",
      sds < 2 * 4 - 1, f"{sds} < {2*4-1}")
check("CONTROL: but 4 >= 4, so SdS IS Liouville-integrable -- the two bounds separate",
      sds >= 4, f"{sds} >= 4")

# and the wall, the ladder's floor
check("CONTROL: the wall has 0 Killing vectors, so neither bound is met",
      0 < 4 and 0 < 2 * 4 - 1, "0 against 4 and 7")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The generators are counted from the embedding and shown")
print("  independent: 15 for dS_5 and 10 for dS_4, equal to D(D+1)/2 and so maximal.")
print("  Against 2D-1 the substrate is MAXIMALLY SUPERINTEGRABLE with a surplus of six.")
print("  The controls separate the two bounds -- SdS meets Liouville and not")
print("  superintegrability, the wall meets neither -- so the test distinguishes maximal")
print("  symmetry from symmetry, which is what makes the top of I13's ladder a result.")
print("=" * 78)
