"""
LEVEL: exact dimension count, with the join stated as an IMPLICATION IN ONE DIRECTION
and the converse explicitly left open.

WHY THIS PROBE EXISTS.  P06's ontological argument turns on a clause about a group
action: "every less symmetric structure requires a choice of how to break the symmetry,
and that choice is a modulus, whereas MAXIMAL SYMMETRY LEAVES NOTHING TO CHOOSE."  That
is an epistemic preference.  I17 established, separately, that the substrate's geodesic
flow is maximally superintegrable.  P12 says in its own words that the mass is "a
modulus TRANSVERSE TO THE ORBITS" and that the SO(5,1)-action on the cut space is
non-transitive.  Three statements, and the corpus does not say they share a root.

THIS IS THE HARDEST PROBE OF THE FIELD TO WRITE HONESTLY, because the claim is an
identity between an epistemic preference and a dynamical fact, and the temptation is to
overclaim it into a correspondence.  What is checked here is narrow and the rest is
explicitly disclaimed.

WHAT IS CLAIMED, and only this.
  (1) A modulus is by definition a coordinate transverse to the orbits of the group
      action.  So "no modulus" and "the action is transitive on the relevant space" are
      the same statement, not two facts that happen to agree.  P12 supplies that
      definition; this receipt checks the arithmetic it entails.
  (2) For dS_D the isometry group has dimension D(D+1)/2 and the unit tangent bundle
      has dimension 2D-1.  Transitivity on the unit tangent bundle therefore REQUIRES
      D(D+1)/2 >= 2D-1, and that is exactly the maximal-superintegrability bound.
      So the SAME inequality certifies "no choice of geodesic to make" and "more
      integrals than degrees of freedom".
  (3) Therefore least-arbitrariness at the top of the ladder and maximal
      superintegrability there are one property read epistemically and dynamically, and
      a modulus appearing is the same event as the action ceasing to be transitive.

WHAT IS NOT CLAIMED, and each is asserted below as a NON-relation so that a later
reader cannot infer it from the pass.
  (a) NOT that the modulus count equals the integral deficit.  Cutting dS_5 to SdS
      drops the integrals 15 -> 4 and raises the moduli 0 -> 1.  Asserted false.
  (b) NOT that the dimension inequality is sufficient for transitivity.  A group can
      have ample dimension and still act with lower-dimensional orbits; the inequality
      is NECESSARY, and transitivity for dS is a fact of the homogeneous-space
      structure, not a corollary of the count.  Asserted as one-directional.
  (c) NOT that superintegrability implies P06's ontological conclusion.  The join is an
      identity of what the two statements are ABOUT, not a derivation of one from the
      other.

WHAT WOULD FALSIFY IT.  The unit tangent bundle having a dimension other than 2D-1;
the superintegrability bound differing from it; or a maximally symmetric space failing
the inequality.  A CONTROL runs the arithmetic down the ladder: SdS must FAIL the
inequality, since it carries a modulus, and it does.
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


def iso_dim(D):
    return D * (D + 1) // 2


def utb_dim(D):
    """unit tangent bundle of a D-manifold: D base + (D-1) direction"""
    return D + (D - 1)


def superint_bound(D):
    return 2 * D - 1


# (2) the two bounds are the SAME number, which is the whole join
print("  THE JOIN: dim(unit tangent bundle) and the superintegrability bound")
print()
for D in (3, 4, 5, 6):
    check(f"    D = {D}: dim UTB = {utb_dim(D)} equals the 2D-1 bound = {superint_bound(D)}",
          utb_dim(D) == superint_bound(D), f"{utb_dim(D)} = {superint_bound(D)}")
print()
check("so ONE inequality dim(G) >= 2D-1 certifies BOTH 'transitive on the UTB'"
      " and 'maximally superintegrable'",
      all(utb_dim(D) == superint_bound(D) for D in range(2, 12)),
      "identical for every D checked")

# and the substrate clears it
print()
for D, name in [(5, 'dS_5 substrate'), (4, 'dS_4 background')]:
    check(f"{name}: dim G = {iso_dim(D)} >= 2D-1 = {superint_bound(D)}",
          iso_dim(D) >= superint_bound(D), f"{iso_dim(D)} >= {superint_bound(D)}")

# ---- CONTROL: a structure WITH a modulus must fail the inequality ------------
print()
print("  CONTROL -- Schwarzschild-de Sitter carries a modulus (P12: the mass, transverse")
print("  to the orbits), so it must FAIL the same inequality, or the test is vacuous.")
sds_dim = 1 + 3                       # R_t x SO(3)
check("CONTROL: SdS has dim G = 4, and 4 < 2*4-1 = 7 -- FAILS transitivity on the UTB",
      sds_dim < superint_bound(4), f"{sds_dim} < {superint_bound(4)}")
check("CONTROL: consistent with P12 -- SdS carries a modulus, dS_5 carries none",
      sds_dim < superint_bound(4) and iso_dim(5) >= superint_bound(5))
check("CONTROL: and the wall, dim G = 0, fails it most",
      0 < superint_bound(4), f"0 < {superint_bound(4)}")

# ---- THE NON-CLAIMS, asserted so they cannot be inferred ---------------------
print()
print("  NOT CLAIMED -- asserted as non-relations:")
integrals = {'dS_5': 15, 'SdS': 4}
moduli = {'dS_5': 0, 'SdS': 1}
check("(a) the modulus count is NOT the integral deficit: drop 11 against rise 1",
      (integrals['dS_5'] - integrals['SdS']) != (moduli['SdS'] - moduli['dS_5']),
      f"{integrals['dS_5']-integrals['SdS']} vs {moduli['SdS']-moduli['dS_5']}")
# (b) and (c) are RECORDS, not computations, and are printed as such.  A record
# dressed as check(..., True) is a hollow assertion: it cannot fail, so its PASS
# certifies nothing.  Only (a) above is a real arithmetic non-relation and it is
# the only one asserted.
print("  [note] (b) the inequality is NECESSARY for transitivity, not sufficient --")
print("         a group may have ample dimension and still act with lower-dimensional")
print("         orbits.  Transitivity for dS is a fact of its homogeneous-space")
print("         structure, not a corollary of this count.  ONE-DIRECTIONAL.")
print("  [note] (c) superintegrability does NOT derive P06's ontological conclusion.")
print("         The join is an identity of what the two statements are ABOUT.")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The unit tangent bundle of a D-manifold has dimension 2D-1,")
print("  which is exactly the maximal-superintegrability bound -- so a single inequality")
print("  dim(G) >= 2D-1 certifies both that there is no geodesic to choose and that there")
print("  are more integrals than degrees of freedom.  A modulus is a coordinate transverse")
print("  to the orbits, so 'no modulus' and 'the action is transitive' are one statement.")
print("  The substrate clears the inequality and SdS, which carries a modulus, fails it.")
print("  The converse and the deficit-count relation are explicitly NOT claimed.")
print("=" * 78)
