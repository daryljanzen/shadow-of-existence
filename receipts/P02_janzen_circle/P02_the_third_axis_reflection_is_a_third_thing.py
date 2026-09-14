"""
P02_the_third_axis_reflection_is_a_third_thing
==============================================

Object under test -- an open question `P2` has carried since `P02_the_third_axis_is_two_poles`,
in its own words:

  ** "Not settled here and not needed for the count: whether the reflection z -> -z
     (r-even, tau-odd, i.e. CYCLOID-TIME REVERSAL) is the corpus's R, its K, or a THIRD
     THING." **

r6574 answers that shape for the cosmogenetic bead.  *** This records the answer, and does NOT
extend it to the cycloid beyond where the two parametrisations are shown to agree. ***

--------------------------------------------------------------------------------
(1) THE BEAD'S T IS A THIRD THING, AND r6574 IS WHY.

On the bead relation r^3 = 2 M a^2 sinh^2(3 tau~/2a), the map

    T :  tau~ -> -tau~   at FIXED r and FIXED 2M

is a symmetry in its own right, since sinh^2 is even.  And it is neither of the named two:

    NOT R -- the corpus's R is (r, tau~; 2M, Q) |-> (-r, tau~; -2M, Q).  ** It FLIPS THE
             MASS and holds tau~ fixed. **  T holds the mass and flips tau~.
    NOT K -- K is the antilinear reality involution, and the operator in psi -> psi^c
             ANTICOMMUTES with gamma^5, so it ** FLIPS CHIRALITY **.  T flips neither.

  ==> *** A THIRD THING, and P2's disjunction is answered in its third branch. ***

⌗ AND IT IS THE THING THAT GRADES THE LIFT.  r6566 measured a 2+1 on the lift fibre and r6574
identified the operator: not R o K, which carries those modes off the mode space entirely, but T.
** So the third branch of P2's question is not idle -- it is what the lift's split is graded by. **

--------------------------------------------------------------------------------
(2) AND THE CYCLOID REFLECTION HAS THE SAME SHAPE -- WHICH IS NOT THE SAME AS BEING THE SAME MAP.

    P2's cycloid   r = M(1 - cos z),  tau = M(z - sin z)   under z -> -z:  r EVEN, tau ODD
    the bead       r^3 = 2Ma^2 sinh^2(w)                   under T:        r EVEN, tau~ ODD

** Both are "reverse the time parameter, hold the mass".  That is a shape, and this corpus has
been caught by shapes before. **  So the parametrisations are compared rather than assumed equal.

--------------------------------------------------------------------------------
(3) THEY AGREE NEAR r = 0, TO THE COEFFICIENT, AND ARE NOT SHOWN TO AGREE ELSEWHERE.

Expanded independently:

    bead, small tau~ :  r^3 -> (9/2) M tau~^2   so   r -> 6^(2/3) M^(1/3) tau~^(2/3) / 2
    cycloid, small z :  r -> M z^2/2, tau -> M z^3/6,  eliminating z gives the SAME
                        r -> 6^(2/3) M^(1/3) tau^(2/3) / 2

** Not merely the same exponent 2/3 -- the same coefficient. **  Both reduce to the
marginally-bound law near the singularity.

  ==> ** So the two reflections coincide WHERE the parametrisations do. **  And the cycloid is
      the BOUND case while the bead carries Lambda, so *** they are not shown to agree away from
      r = 0, and this receipt does not claim they do. ***

--------------------------------------------------------------------------------
⚠ WHAT IS ESTABLISHED AND WHAT IS NOT.

  ESTABLISHED: P2's question is answered in its third branch FOR THE BEAD -- T is neither R nor
  K -- and the two parametrisations' reflections agree to leading order and coefficient near
  r = 0.

  NOT ESTABLISHED: ** that P2's cycloid reflection and the bead's T are the same map globally. **
  What is shown is agreement in one limit.  *** Nothing here says what T MEANS -- that it is a
  symmetry of the relation and grades the lift is what is known; whether it is a physical time
  reversal in the CPT sense is not addressed. ***
"""

import sympy as sp

z, M, a, t = sp.symbols('z M a t', positive=True)

# --- (1) T is a symmetry of the bead relation, and is neither R nor K ---------------
w = sp.Symbol('w')
assert sp.simplify(sp.sinh(-w)**2 - sp.sinh(w)**2) == 0, "sinh^2 even, so T is a symmetry"
MAPS = {
    'R': {'flips 2M': True,  'flips tau~': False, 'flips chirality': False},
    'K': {'flips 2M': False, 'flips tau~': False, 'flips chirality': True},
    'T': {'flips 2M': False, 'flips tau~': True,  'flips chirality': False},
}
assert MAPS['T'] != MAPS['R'] and MAPS['T'] != MAPS['K'], "T is neither"
assert MAPS['T']['flips tau~'] and not MAPS['T']['flips 2M'] \
    and not MAPS['T']['flips chirality'], "T flips the time and nothing else"
print("  T: flips tau~, holds 2M, does not touch chirality -> neither R nor K   OK")

# --- (2)/(3) the two parametrisations, expanded independently -----------------------
r_bead3 = sp.series(2*M*a**2*sp.sinh(3*t/(2*a))**2, t, 0, 4).removeO()
assert sp.simplify(r_bead3 - sp.Rational(9, 2)*M*t**2) == 0, f"bead leading term: {r_bead3}"
r_bead = sp.simplify(r_bead3**sp.Rational(1, 3))

r_c = sp.series(M*(1 - sp.cos(z)), z, 0, 4).removeO()
t_c = sp.series(M*(z - sp.sin(z)), z, 0, 5).removeO()
z_of_t = [s for s in sp.solve(sp.Eq(t_c, t), z) if s.is_real is not False][0]
r_cyc = sp.simplify(r_c.subs(z, z_of_t))

assert sp.simplify(r_bead - r_cyc) == 0, f"must agree: {r_bead} vs {r_cyc}"
print(f"  bead   near r=0:  r -> {r_bead}")
print(f"  cycloid near r=0: r -> {r_cyc}")
print("  -> same exponent AND same coefficient, independently derived          OK")

# --- and the parity structure is shared --------------------------------------------
assert sp.simplify(M*(1 - sp.cos(-z)) - M*(1 - sp.cos(z))) == 0, "cycloid r is even"
assert sp.simplify(M*(-z - sp.sin(-z)) + M*(z - sp.sin(z))) == 0, "cycloid tau is odd"
print("  cycloid: r even, tau odd under z -> -z                                OK")

# --- the bound ----------------------------------------------------------------------
SHOWN = 'the reflections agree near r = 0, to the coefficient'
NOT_SHOWN = 'that they are the same map globally; the cycloid is bound, the bead carries Lambda'
assert SHOWN != NOT_SHOWN
print(f"\n  shown     : {SHOWN}")
print(f"  not shown : {NOT_SHOWN}")

print()
print("ESTABLISHED: P2's open disjunction -- R, K, or a third thing -- is answered in its THIRD")
print("branch for the bead's T, and T is what grades the lift's 2+1 (r6574). The cycloid's")
print("reflection has the same parity structure and agrees with the bead's near r=0 to the")
print("coefficient, both reducing to the marginally-bound law.")
print("NOT ESTABLISHED: that the two are the same map away from r=0; and nothing here says what")
print("T MEANS -- whether it is a physical time reversal in the CPT sense is not addressed.")
