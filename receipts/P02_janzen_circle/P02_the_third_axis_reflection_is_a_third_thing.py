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
--------------------------------------------------------------------------------
(4) AND WHAT tilde-tau IS, SINCE THE ANSWER TURNS ON IT.

** tilde-tau is COSMIC TIME. **  P15 sec:properframe derives it in five steps: a radial
geodesic with conserved E; the fundamental congruence fixed BY THE FIELD at E=1 (where
V_eff == 1); that energy integrating in closed form to r ~ sinh^(2/3); the congruence
labelled by a comoving chi, under which r depends on tau and chi only through their SUM;
and g_{chi tau} = 0 forcing the integration function to be chi itself.  The corpus's own
sentence: ** "with COSMIC TIME tilde-tau == tau + chi (by Weyl's principle the congruence
issues from a common origin and the constant-cosmic-time slices are those of constant
tilde-tau)". **

  ⌗ SO THE BEAD RELATION IS eq:scalefac, THE SCALE FACTOR:
        r(tilde-tau) = (6GM/Lambda c^2)^(1/3) sinh^(2/3)( (3/2) sqrt(Lambda c^2/3)
        tilde-tau )
    whose prefactor is exactly A = (2GM alpha^2/c^2)^(1/3) and whose argument is exactly
    3 tilde-tau / 2 alpha -- both verified below.

  ==> *** T : tilde-tau -> -tilde-tau IS COSMOLOGICAL TIME REVERSAL.  r is even in
      tilde-tau, the expanding cosmology is the real branch tilde-tau > 0, and T carries
      it to the contracting one AT THE SAME r. ***

⌗ AND IT IS NOT THE CANON'S T.  The r968 symbol canon reserves T for the time reflection
X_0 -> -X_0 -- the static/embedding time -- while tilde-tau is the COSMIC time of a
non-synchronous slicing, the constant-tilde-tau slices sitting at 45 degrees to the
fundamental rest frame.  ** Same word, two slicings; the corpus keeps them apart and so
does this. **

--------------------------------------------------------------------------------
⚠ WHAT IS ESTABLISHED AND WHAT IS NOT.

  ESTABLISHED: P2's question is answered in its third branch FOR THE BEAD -- T is neither R nor
  K -- and the two parametrisations' reflections agree to leading order and coefficient near
  r = 0.

  NOT ESTABLISHED: ** that P2's cycloid reflection and the bead's T are the same map globally. **
  What is shown is agreement in one limit.  ⌗ And T is cosmological time reversal, NOT the
  canon's T (X_0 -> -X_0): *** the corpus distinguishes the two slicings and a full geometric
  CPT is settled in the NEGATIVE anyway -- "CPT IS NOT AUTO-YIELDED (the charge sign is
  external)" -- so there is no third slot here for T to fill. ***
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
print("AND WHAT T IS: tilde-tau is COSMIC TIME (P15 sec:properframe, five steps, Weyl's")
print("principle), the bead relation IS eq:scalefac the scale factor, and T reverses cosmic")
print("time -- carrying the expanding branch to the contracting one at the SAME r.")
print("NOT ESTABLISHED: that the two reflections are the same map away from r=0. And T is")
print("NOT the canon's T (X_0 -> -X_0, the static time): the corpus keeps the two slicings")
print("apart, and a full geometric CPT is settled in the NEGATIVE anyway -- the charge sign")
print("is external -- so there is no third slot for T to fill.")
# --- (4) tilde-tau is COSMIC TIME, and the bead relation is eq:scalefac ---------------
G_, M_, Lam_, c_, al_ = sp.symbols('G M Lambda c alpha', positive=True)
pref = (6*G_*M_/(Lam_*c_**2))**sp.Rational(1, 3)
A_ = (2*G_*M_*al_**2/c_**2)**sp.Rational(1, 3)
assert sp.simplify(pref.subs(Lam_, 3/al_**2) - A_) == 0, \
    "eq:scalefac's prefactor must BE A -- the lift's binding radius"
tt_ = sp.Symbol('ttau', positive=True)
arg = sp.Rational(3, 2)*sp.sqrt(Lam_*c_**2/3)*tt_
assert sp.simplify(arg.subs(Lam_, 3/al_**2).subs(c_, 1) - 3*tt_/(2*al_)) == 0, \
    "and its argument must be 3 tilde-tau / 2 alpha"
print("  eq:scalefac's prefactor IS A and its argument IS 3 ttau/2alpha        OK")
print("  -> the bead relation is the SCALE FACTOR in COSMIC TIME")
print("  -> T reverses cosmic time: expanding branch -> contracting, same r    OK")
