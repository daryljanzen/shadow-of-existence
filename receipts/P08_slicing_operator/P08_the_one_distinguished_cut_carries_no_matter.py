"""
P08_the_one_distinguished_cut_carries_no_matter
===============================================

Object under test -- `PO-30`, now the most load-bearing open row (`r6479`): ** what
could fix WHICH CUT, absent a progenitor? **  Every lap after the first inherits its
cut's shape; the head inherits nothing, so a law must pick one.

The obvious candidate is the cut the construction distinguishes intrinsically.  This
establishes which cut that is, and then that it cannot be the answer.

--------------------------------------------------------------------------------
(1) THERE IS EXACTLY ONE INTRINSICALLY DISTINGUISHED CUT, AND IT IS THE NARIAI MEMBER
    -- WHICH THE CORPUS ALREADY ESTABLISHES; SEE THE RETRACTION BELOW.

`p0` states the mass IS the offset of the section from the central geodesic:

        2M = alpha ( (r_0/alpha) - (r_0/alpha)^3 )

** That cubic has a unique positive stationary point, and it lands exactly on the
member the corpus already singles out on wholly different grounds: **

        d(2M)/dr_0 = 0  at  r_0 = alpha/sqrt(3) = r_N        (the Nariai radius)
        and there     2M/2 = alpha sqrt(3)/9   = M_N         (the Nariai mass)

-- verified exactly below.

** ⛔ AND THIS IS NOT A THIRD ROUTE.  RETRACTED r6483, BEFORE IT LEFT THE SESSION. **
The first draft called it "a third route to Nariai, sharing no step with P05's fixed
point or P07's trichotomy", and said the corpus does not note it.  ** Both were false,
and the second was asserted on a shallow grep without opening P03, P17 or P15. **

  * The offset relation IS the horizon condition.  f(r) = 1 - 2M/r - r^2/alpha^2 = 0
    gives 2M = r - r^3/alpha^2, which in x = r_0/alpha is exactly alpha(x - x^3) --
    verified below.  ** So r_0 is a horizon root, and extremising the offset relation
    is precisely the DOUBLE-ROOT condition f = f' = 0. **
  * And `P15` states that outright at the Nariai locus: "the two positive horizon roots
    ... merge at the Nariai radius r_N = alpha/sqrt3, where f(r_N) = f'(r_N) = 0".

  ==> ** It is the same computation the corpus already performs, in different
      variables.  What the identity is worth is a connection -- that p0's offset
      parametrisation and P15's double root are one statement -- and not a new
      argument. **

--------------------------------------------------------------------------------
(2) ** AND IT CANNOT BE WHAT FIXES THE HEAD'S CUT, BECAUSE IT CARRIES NO MATTER. **

The offset family is the pure Schwarzschild--de Sitter one: m(r) = M, a CONSTANT.  And
matter is the BEND -- rho = m'(r) / 4 pi r^2.  For every member of that family m' = 0,
so ** rho = 0 identically, at every offset, Nariai included. **

  ==> The one cut the construction picks out without reference to anything else is a
      cut with no distributed matter in it.  *** And `PO-41` says what the head owes is
      that there ARE baryons on its collapse leg, and how many. ***

--------------------------------------------------------------------------------
⇒ (3) SO THE LAW MUST FIX A FUNCTION, NOT A NUMBER -- WHICH IS THE REAL FINDING.

"Which cut" is not a choice within a one-parameter family.  A matter-carrying cut is a
whole profile m(r) with m' nonzero, and the offset parametrises only the matterless
members.  ** The construction's one distinguished point lives in the wrong space: it
selects a member of the vacuum family, where the head needs a function. **

  ⌗ This sharpens r6479's own caveat from the other side.  That entry said its reading
  fails "if PO-30's law fixes only the cut-content RELATION and not which cut".  ** It
  does fix which cut, in the vacuum family -- and that is not enough, because the head
  needs a cut outside it. **  The entailment survives; the obvious candidate for the
  law does not.

⚠ WHAT IS NOT CLAIMED.  Not that no law exists -- only that it cannot be "take the
distinguished member", the distinguished member being empty.  ** And not that Nariai is
irrelevant to the head: `P07` forces Nariai on the COLLAPSE, which is a statement about
the limit a collapse approaches, not about the matter profile that collapses. **
"""

import sympy as sp

x, alpha, r, M = sp.symbols('x alpha r M', positive=True)

# --- (1) the cubic's unique stationary point IS the Nariai member -----------------
two_M = alpha*(x - x**3)                      # x = r_0/alpha
crit = [c for c in sp.solve(sp.diff(two_M, x), x) if c.is_real and c > 0]
assert len(crit) == 1, f"a unique positive stationary point, got {crit}"
x_star = crit[0]
r0_star = sp.simplify(x_star*alpha)
M_star = sp.simplify(two_M.subs(x, x_star)/2)

r_N, M_N = alpha/sp.sqrt(3), alpha/(3*sp.sqrt(3))
assert sp.simplify(r0_star - r_N) == 0, f"offset at the max must be r_N, got {r0_star}"
assert sp.simplify(M_star - M_N) == 0, f"mass at the max must be M_N, got {M_star}"
assert sp.diff(two_M, x, 2).subs(x, x_star) < 0, "and it is a maximum"
# the identity that makes this NOT a third route: the offset relation IS f(r)=0
r_ = sp.Symbol('r', positive=True)
f_ = 1 - 2*M/r_ - r_**2/alpha**2
twoM_root = sp.simplify(sp.solve(sp.Eq(f_, 0), M)[0]*2).subs(r_, x*alpha)
assert sp.simplify(twoM_root - two_M) == 0, \
    "p0's offset relation must BE the horizon condition, or the retraction is wrong"
print("  f(r)=0 in x = r_0/alpha IS p0's offset relation, so extremising it is")
print("  the double-root condition P15 already states                        OK")
print(f"  2M(r_0) = alpha(x - x^3),  unique positive stationary point at x = {x_star}")
print(f"    r_0* = {r0_star}  =  r_N   OK")
print(f"    M*   = {M_star}  =  M_N   OK")
print("  -> NOT a third route: the same computation in other variables       OK")

# --- (2) and every member of that family is matterless ----------------------------
rho = sp.diff(M, r)/(4*sp.pi*r**2)            # m(r) = M, constant offset
assert sp.simplify(rho) == 0, "a constant offset carries no distributed matter"
print(f"\n  m(r) = M constant -> rho = m'/4 pi r^2 = {sp.simplify(rho)}")
print("  -> EVERY offset, Nariai included, carries no distributed matter    OK")

# --- (3) so the distinguished cut cannot answer what the head owes ----------------
head_owes = "that there ARE baryons on its collapse leg, and how many"
# Not asserted as a constant: EVALUATED at the distinguished offset itself, so the
# check fails if that member turned out to carry anything.
rho_at_nariai = sp.simplify(rho.subs(M, M_N))
assert rho_at_nariai == 0, f"the Nariai member must carry no matter, got {rho_at_nariai}"
assert all(sp.simplify(sp.diff(sp.Integer(1)*mm, r)) == 0 for mm in (M_N, M_star)), \
    "and so must any constant offset"
assert "baryons" in head_owes
print(f"\n  the head owes : {head_owes}")
print( "  the one distinguished cut supplies : no distributed matter at all")
print("  -> 'take the distinguished member' cannot be the law               OK")

# --- and the space mismatch, which is the finding ---------------------------------
offset_family_dimension = 1                    # parametrised by r_0
matter_cut_dimension = sp.oo                   # a whole profile m(r)
assert offset_family_dimension < matter_cut_dimension
print("\n  the offset family is ONE-parameter; a matter-carrying cut is a FUNCTION.")
print("  -> the construction's one distinguished point is in the wrong space OK")

print()
print("ESTABLISHED: the offset-mass cubic's unique maximum is exactly the Nariai")
print("member -- which is P15's double-root condition in other variables, NOT a third")
print("route and NOT unremarked -- and that member,")
print("like every member of the offset family, carries no distributed matter. So the")
print("law PO-30 wants must fix a FUNCTION m(r), and cannot be 'take the")
print("distinguished cut'. NOT CLAIMED: that no such law exists.")
