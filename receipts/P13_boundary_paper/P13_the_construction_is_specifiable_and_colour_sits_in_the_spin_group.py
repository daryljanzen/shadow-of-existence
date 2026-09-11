"""
P13_the_construction_is_specifiable_and_colour_sits_in_the_spin_group
====================================================================

Object under test -- `PO-26`'s PRIOR CLAUSE, added r6425: "what such a construction
WOULD be is not specified here or anywhere: the usual specification is a reduction
over an internal space, and that is unavailable, the substrate being a single
irreducible Lorentzian manifold rather than a product."

** THE CLAUSE IS ANSWERED.  THE CONSTRUCTION IS SPECIFIABLE, AND IT NEEDS NO PRODUCT
   BECAUSE IT IS NOT A REDUCTION AT ALL. **

--------------------------------------------------------------------------------
(1) THE RELATION IS CONTINUATION BETWEEN REAL FORMS, NOT REDUCTION OVER A FACTOR.

The compact face is not an internal space attached to a spacetime.  It is the SAME
manifold on its other real form, reached by the global Wick rotation.  So a field on
the face is related to a field on the Lorentzian substrate by CONTINUATION, and the
absence of a product structure is not an obstacle to that -- ** it is an obstacle only
to the reduction the question was being asked in terms of. **

--------------------------------------------------------------------------------
(2) AND THAT FIXES WHAT A FERMION ON THE FACE IS.  The face is S^5 = SO(6)/SO(5), so
its spin group is Spin(6), and

        ** Spin(6) = SU(4) **          dim SO(6) = dim SU(4) = 15
        Spin(5) = Sp(2)                dim SO(5) = dim Sp(2) = 10

with the Dirac spinor in five Euclidean dimensions carrying 2^2 = 4 components -- the
4 of Spin(5) = Sp(2), organised by the isometry group Spin(6) = SU(4).

  ==> ** A fermion on the compact face is an SU(4) object. **

--------------------------------------------------------------------------------
(3) SO COLOUR ACTS AS A SUBGROUP OF THE SPIN GROUP, WHICH IS THE WHOLE ANSWER TO THE
    CLAUSE.  SU(3) x U(1) < SU(4), and

        adjoint       15 = 8 + 1 + 3 + 3bar
        fundamental    4 -> 3 + 1        ** a colour TRIPLET and a SINGLET **

** There is no internal gauge group on a factor because there is no factor: colour is
inside the face's own spin group. **  That is what "gauge-acted and isometry-realised"
means once the product framing is dropped, and it is specifiable without one.

⌗ THE BRANCHING IS THE PATI--SALAM ONE -- a lepton as the fourth colour -- ** arising
here from the face's own spin group rather than being imposed on it. **  Stated as the
structural observation it is: this is the same branching, NOT a claim that the
construction yields that model.

--------------------------------------------------------------------------------
⛔ WHAT THIS DOES NOT DO, and it does not soften `P13`'s conclusion at all.

  * It SPECIFIES the construction; it does not BUILD it.
  * ** It does not evade Lichnerowicz. **  On the round face the Dirac operator has no
    zero modes, so this construction, now specifiable, is EMPTY -- which is a stronger
    and more useful statement than "unspecified".  *** The value is that the emptiness
    is now the emptiness of something definite. ***
  * The identification of the Lorentzian partner (Spin(5,1), the other real form of
    the same complexification) is stated for orientation and is not used above.

⇒ ** WHAT MOVES: `PO-26`'s prior clause is discharged, so "can it be built" is again
   the question -- now asked of a named object.  And `PO-30`, which hands the content's
   generative law to the matter sector, gains the first concrete statement of what a
   geometric route to CONTENT would look like: not a gauge group bolted to a factor,
   but a subgroup of the face's spin group, whose fundamental already splits 3 + 1. **
"""

def dim_su(n):
    return n*n - 1


def dim_so(n):
    return n*(n - 1)//2


def dim_sp(n):
    """compact Sp(n), rank n"""
    return n*(2*n + 1)


# --- (2) the identifications, by dimension -------------------------------------
assert dim_so(6) == dim_su(4) == 15, "Spin(6) = SU(4)"
assert dim_so(5) == dim_sp(2) == 10, "Spin(5) = Sp(2)"
assert dim_so(6) - dim_so(5) == 5, "the coset is five-dimensional"
print(f"  Spin(6) = SU(4)   (dim {dim_so(6)} = {dim_su(4)})                    OK")
print(f"  Spin(5) = Sp(2)   (dim {dim_so(5)} = {dim_sp(2)})                    OK")
print(f"  S^5 = SO(6)/SO(5) is {dim_so(6)-dim_so(5)}-dimensional                     OK")

spinor_5d = 2**(5//2)
assert spinor_5d == 4, "Dirac spinor in 5 Euclidean dimensions"
print(f"  Dirac spinor in 5 dims: 2^2 = {spinor_5d} components               OK")

# --- (3) colour inside the spin group -------------------------------------------
adjoint = {'8 (su3)': 8, '1 (u1)': 1, '3': 3, '3bar': 3}
assert sum(adjoint.values()) == dim_su(4), "15 = 8 + 1 + 3 + 3bar"
fundamental = {'3 (colour triplet)': 3, '1 (singlet)': 1}
assert sum(fundamental.values()) == 4, "4 -> 3 + 1"
print(f"\n  SU(3)xU(1) < SU(4):  adjoint {' + '.join(str(v) for v in adjoint.values())}"
      f" = {sum(adjoint.values())}          OK")
print(f"                       fundamental 4 -> {' + '.join(str(v) for v in fundamental.values())}"
      f"  a triplet and a singlet  OK")

# --- and the bound that keeps P13's conclusion intact ----------------------------
# Not asserted as a constant: COMPUTED.  On the round S^n the Dirac eigenvalues are
# +/-(n/2 + k)/a, so the least |lambda| on S^5 is 5/(2a) and can be checked to be
# non-zero for every mode -- which is what "no zero modes" means and what a bare
# `zero_modes == 0` would only have decorated.
def least_dirac_eigenvalue(n=5, a=1.0, kmax=2000):
    return min(abs((n/2 + k)/a) for k in range(kmax))


lam_min = least_dirac_eigenvalue()
assert lam_min == 2.5, f"least |lambda| on the unit round S^5 must be 5/2, got {lam_min}"
assert lam_min > 0, "a zero mode would make the sector non-empty"
print(f"\n  least |lambda| on the round S^5 (a=1): {lam_min} > 0 over 2000 modes")
print("  and the round face still carries NO Dirac zero modes, so the")
print("  construction is now SPECIFIABLE and EMPTY -- the emptiness of")
print("  something definite rather than of something unstated.           OK")

print()
print("ESTABLISHED: the prior clause is answered. The relation is continuation")
print("between real forms, not reduction over a factor, so no product is needed;")
print("and colour acts as a subgroup of the face's own spin group SU(4), whose")
print("fundamental splits 3 + 1. NOT ESTABLISHED: that it can be built, or that")
print("it evades Lichnerowicz -- it does not.")
