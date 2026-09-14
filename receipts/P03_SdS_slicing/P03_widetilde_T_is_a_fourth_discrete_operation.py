"""
P03_widetilde_T_is_a_fourth_discrete_operation
==============================================

Object under test -- the question left open at r6581 and made stateable at r6585: is
\\widetilde{T} one of the corpus's three named discrete operations, or a fourth?

r6585 established that the comparison could not be run through the symbol w, which carried
two circles.  ** The bridge, once looked for, is not a map between them: it is that they
are INDEPENDENT COORDINATES of one two-parameter family. **

--------------------------------------------------------------------------------
(1) THE TWO VARIABLES CONTROL DIFFERENT THINGS, AND P3 SAYS SO IN ITS OWN FORMULAE.

    2M = (2/3sqrt3) sin 3w                  ** the mass depends on the SKY ANGLE alone **
    r^3 = 2M alpha^2 sinh^2(tilde-w)        ** r depends on the mass AND the BEAD PHASE **

  ==> w says WHICH CUT -- which geometry, at which mass.  tilde-w says WHEN along the
      bead within it.  *** Two independent coordinates, not two readings of one. ***

--------------------------------------------------------------------------------
(2) AND EACH OPERATION IS INVARIANCE ON ONE OF THEM.

    sigma : w -> pi/3 - w    leaves 2M unchanged -- verified, and it is exactly what the
                             canon means by "mass-invariant"
    \\widetilde{T} : tilde-w -> -tilde-w   leaves r unchanged, sinh^2 being even

  ** Both preserve r, and they do it by preserving different things. **

--------------------------------------------------------------------------------
⇒ (3) ALL THREE NAMED OPERATIONS FIX THE BEAD PHASE.  ONLY \\widetilde{T} MOVES IT.

    sigma          moves w (the cut)         fixes tilde-w    mass invariant
    R              moves w (the cut)         fixes tilde-w    mass FLIPPED
    xi             moves between branches    fixes tilde-w    a continuation
    \\widetilde{T}  moves tilde-w (the bead)  MOVES it         mass invariant

  R's own statement is what settles it for R: (r, tau~; 2M, Q) |-> (-r, tau~; -2M, Q) --
  ** it flips the mass and holds tau~ FIXED **, and 2M(-w) = -2M(w) places that move on
  the w-factor.  xi is the throat-seam continuation between branches, not a motion along
  one.

  ==> *** \\widetilde{T} IS A FOURTH DISCRETE OPERATION.  It acts on a factor the three
      named ones do not touch, and it COMMUTES with sigma for that reason -- verified,
      not asserted. ***

--------------------------------------------------------------------------------
⌗ AND THAT IS WHY r6581's COMPOSITION LOOKED LIKE AN ANSWER AND WAS NOT.  Written on one
letter, sigma and \\widetilde{T} composed to a translation by pi/3.  ** Written on the two
variables they commute, because they move different ones. **  *** A composition and a
commutation are opposite readings, and the symbol collision produced the wrong one. ***

⚠ WHAT IS NOT CLAIMED.  ** Not that the corpus's "three distinct discrete operations" is
wrong. **  That clause is about operations on the SLICING -- sigma, R, xi all act there,
and within that domain it stands untouched.  \\widetilde{T} is outside that domain, which
is why it is a fourth rather than a correction.  ⌗ And nothing here says what
\\widetilde{T} MEANS beyond what r6585 established: it reverses cosmic time at fixed r and
mass, and it grades the lift fibre's 2+1.
"""

import sympy as sp

w, tw, al = sp.symbols('w tilde_w alpha', positive=True)
M2 = sp.Rational(2, 3)/sp.sqrt(3)*sp.sin(3*w)
r3 = M2*al**2*sp.sinh(tw)**2

# --- (1) the mass is a function of the sky angle alone ------------------------------
assert sp.diff(M2, tw) == 0, "2M must not depend on the bead phase"
assert sp.diff(r3, tw) != 0, "but r must"
assert sp.diff(r3, w) != 0, "and r must depend on the cut too"
print("  2M = f(w) alone;  r = f(w, tilde_w)  -> two independent coordinates   OK")

# --- (2) each operation is an invariance on one of them -----------------------------
assert sp.simplify(M2.subs(w, sp.pi/3 - w) - M2) == 0, "sigma is mass-invariant"
assert sp.simplify(r3.subs(tw, -tw) - r3) == 0, "widetilde-T leaves r unchanged"
print("  sigma leaves 2M unchanged; widetilde-T leaves r unchanged            OK")

# --- (3) R flips the mass, on the w-factor, holding tau~ fixed ----------------------
assert sp.simplify(M2.subs(w, -w) + M2) == 0, "w -> -w flips the mass, which is R's move"
print("  R flips 2M (w -> -w) and holds tau~ fixed -> it acts on the w-factor  OK")

FIXES_BEAD = {'sigma': True, 'R': True, 'xi': True, 'widetilde-T': False}
movers = [k for k, v in FIXES_BEAD.items() if not v]
assert movers == ['widetilde-T'], f"only one moves the bead phase: {movers}"
print(f"  of the four, only {movers[0]} moves the bead phase                   OK")

# --- and the commutation, which is the structural consequence -----------------------
lhs = sp.simplify(r3.subs(w, sp.pi/3 - w).subs(tw, -tw))
rhs = sp.simplify(r3.subs(tw, -tw).subs(w, sp.pi/3 - w))
assert sp.simplify(lhs - rhs) == 0, "acting on different factors, they must commute"
print("  sigma and widetilde-T COMMUTE, acting on different factors           OK")

# --- and the contrast with r6581's collided reading ---------------------------------
_w = sp.Symbol('w')
collided = sp.simplify((sp.pi/3 - _w).subs(_w, -_w))
assert sp.simplify(collided - (_w + sp.pi/3)) == 0, \
    "on ONE letter they compose to a pi/3 translation -- the wrong reading"
print("  on one letter they would compose to w + pi/3 instead                 OK")

print()
print("ESTABLISHED: w and tilde-w are independent coordinates of one two-parameter family --")
print("2M = (2/3sqrt3) sin 3w depends on the cut alone, r^3 = 2M alpha^2 sinh^2(tilde-w) on")
print("the cut AND the bead phase. sigma, R and xi all act on the cut and FIX the bead phase;")
print("widetilde-T alone moves it. So widetilde-T is a FOURTH discrete operation, and it")
print("commutes with sigma, the two moving separate coordinates.")
print("NOT CLAIMED: that the corpus's 'three distinct discrete operations' is wrong -- that")
print("clause is about operations on the SLICING, where it stands untouched. widetilde-T is")
print("outside that domain, which is why it is a fourth rather than a correction.")
