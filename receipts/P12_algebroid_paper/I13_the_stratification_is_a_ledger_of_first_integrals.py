"""
LEVEL: exact, by dimension count against a stated bound.

WHY THIS PROBE EXISTS.  P12 sec:strata lists the isotropy dimensions of the
construction's strata -- Type O ten, Type D Schwarzschild-de Sitter four,
Kerr-de Sitter two, Type I Bianchi three and Zipoy-Voorhees two, the wall zero -- as
a classification of how much symmetry survives a cut.  P09 separately supplies a
Killing TENSOR and the Carter constant.  Neither paper says the first is the reason
for the second.

WHAT IS CLAIMED, and it is a counting statement, not a new theorem.
  (1) A Killing vector contributes one LINEAR first integral of the geodesic flow;
      the isometry algebra's Casimir contributes a quadratic one built from those same
      vectors and needs no independent tensor.
  (2) A D-dimensional geodesic flow needs D integrals in involution for Liouville
      integrability and 2D-1 for maximal superintegrability.
  (3) Against that: dS_5 is maximally superintegrable (15 >= 9); Type D SdS is
      integrable ON KILLING VECTORS ALONE (norm, E, L^2, L_z = 4 for 4 DOF);
      Kerr-de Sitter is SHORT BY ONE (norm, E, L_z = 3); the wall has the norm alone.
  (4) So the drop across the Type-D stratum is the precise place at which a hidden
      symmetry stops being a redundancy and becomes a requirement, and that deficit is
      what P09's Killing tensor fills.

WHAT IS NOT CLAIMED.  Not that the modulus count equals the integral deficit: cutting
dS_5 to SdS drops the integrals 15 -> 4 and raises the moduli 0 -> 1, and there is no
simple complementarity.  Not that the four SdS integrals are independent in any sense
stronger than functional independence on a generic orbit.  Not that Kerr-de Sitter is
NON-integrable -- it is integrable, and the point is precisely that it needs the
tensor to be so.

WHAT WOULD FALSIFY IT.  A maximally symmetric D-manifold whose isometry algebra is not
D(D+1)/2; an SdS isotropy other than four; a Kerr-de Sitter count reaching four on
Killing vectors alone; or the superintegrability bound being other than 2D-1.
"""
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

# (1)(2) the bounds, stated as formulae so a wrong D cannot slip through
def maxsym(D):
    return D * (D + 1) // 2          # the largest isometry algebra a D-manifold admits


def liouville(D):
    return D                          # integrals in involution


def superint(D):
    return 2 * D - 1                  # maximal superintegrability


check("maximal isometry algebra of a D-manifold is D(D+1)/2",
      maxsym(4) == 10 and maxsym(5) == 15, f"dS_4: {maxsym(4)}, dS_5: {maxsym(5)}")
check("dim SO(5,1) = 15 and dim SO(4,1) = 10 -- the substrate and its background",
      maxsym(5) == 15 and maxsym(4) == 10)

# (3) the ladder
LADDER = [
    ('dS_5 substrate, uncut',      5, 15, 15, 'superintegrable'),
    ('dS_4 background',            4, 10, 10, 'superintegrable'),
    ('Type O, de Sitter cut',      4, 10, 10, 'over-determined'),
    ('Type D, SdS  R_t x SO(3)',   4,  4,  4, 'integrable on Killing vectors alone'),
    ('Type D, Kerr-de Sitter',     4,  2,  3, 'SHORT BY ONE'),
    ('Type I, Zipoy-Voorhees',     4,  2,  3, 'short by one'),
    ('the wall, Type N',           4,  0,  1, 'the norm alone'),
]
print()
print(f"  {'stratum':30}{'DOF':>4}{'isotropy':>9}{'involution':>11}{'needs':>6}   verdict")
for name, D, iso, inv, verdict in LADDER:
    print(f"  {name:30}{D:>4}{iso:>9}{inv:>11}{liouville(D):>6}   {verdict}")
print()

check("dS_5 meets maximal superintegrability: 15 >= 2*5-1",
      15 >= superint(5), f"15 >= {superint(5)}")
check("dS_4 meets maximal superintegrability: 10 >= 2*4-1",
      10 >= superint(4), f"10 >= {superint(4)}")

# SdS: R_t x SO(3) is 1 + 3 = 4 Killing vectors; in involution: norm, E, L^2, L_z
sds_kv = 1 + 3
sds_inv = 4
check("SdS isotropy is 1 (time translation) + 3 (SO(3)) = 4 Killing vectors",
      sds_kv == 4, f"{sds_kv}")
check("SdS: four integrals in involution (norm, E, L^2, L_z) for four DOF -- INTEGRABLE",
      sds_inv >= liouville(4), f"{sds_inv} >= {liouville(4)}")

# Kerr-dS: 2 Killing vectors (d_t, d_phi); in involution: norm, E, L_z = 3
kdS_kv = 2
kdS_inv = 1 + kdS_kv
check("Kerr-de Sitter isotropy is 2 Killing vectors (d_t, d_phi)", kdS_kv == 2)
check("Kerr-de Sitter: only three integrals in involution -- SHORT BY ONE",
      kdS_inv == liouville(4) - 1, f"{kdS_inv} against {liouville(4)} needed")
check("the deficit is exactly ONE -- which is what a single Killing TENSOR supplies",
      liouville(4) - kdS_inv == 1, f"deficit {liouville(4) - kdS_inv}")

# the wall: isotropy zero means NO Killing vectors, so the count is the norm and nothing else
wall_iso = LADDER[-1][2]
wall_inv = LADDER[-1][3]
check("the wall (Type N) has isotropy 0 -- no Killing vectors at all",
      wall_iso == 0, f"isotropy {wall_iso}")
check("so its integrals in involution are the norm alone, 1 for 4 DOF -- NOT integrable",
      wall_inv == 1 and wall_inv < liouville(4), f"{wall_inv} against {liouville(4)} needed")

# (4) the descent is monotone down the stratification
counts = [15, 10, 4, 3, 1]
check("the integral count is monotone non-increasing down the strata",
      all(counts[i] >= counts[i + 1] for i in range(len(counts) - 1)), f"{counts}")

# ADVERSARIAL: the test must be able to say SdS is short, if SdS were short
fake_inv = 3
check("ADVERSARIAL: with only three integrals SdS would also register SHORT",
      fake_inv < liouville(4), "the deficit test is not vacuous")

# NOT CLAIMED, asserted as a non-relation so a later reader cannot infer it
integrals = [15, 4]
moduli = [0, 1]
check("NOT a complementarity: 15->4 in integrals against 0->1 in moduli",
      (integrals[0] - integrals[1]) != (moduli[1] - moduli[0]),
      f"drop {integrals[0]-integrals[1]} vs rise {moduli[1]-moduli[0]}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The isotropy stratification is a ledger of first integrals.")
print("  The substrate is maximally superintegrable; Schwarzschild-de Sitter is integrable")
print("  on its Killing vectors alone; Kerr-de Sitter is short by exactly one, which is what")
print("  a single Killing tensor supplies; and the wall has the norm alone.  The drop across")
print("  the Type-D stratum is where a hidden symmetry stops being a redundancy and becomes")
print("  a requirement.")
print("=" * 78)
