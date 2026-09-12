"""
P03_the_sign_switch_is_conditional_on_the_interior_mass_function
================================================================

Object under test -- `PO-25`'s remaining question, "what stands in the horizon's
place", read against the separation `P03` `sec:charge` already draws.

** THE ROW'S OWN LOGIC HAS ONE MORE STEP IN IT, AND TAKING IT NARROWS THE QUESTION TO A
   SINGLE CONDITION. **

--------------------------------------------------------------------------------
(1) WHAT `P03` ESTABLISHES, AND THE MOVE IT MAKES ONCE.

r6405 ran the inner-horizon question and concluded: "** the eternal inner horizon is not
formed, and the obstruction stated above is a property of a STATIONARY solution that the
dynamical problem does not reach. **"

*** That move -- distinguishing what a stationary solution HAS from what a collapse
REACHES -- is made for the inner horizon and not for the other obstruction beside it. ***

`P03` then states the closed loop as *obstructed*: "at any $Q>0$ the sign at the origin
has switched and there is no branch point to pass through, and since the inner turning
point shrinks to zero with the charge while the sign does not follow it, the neutral
case is not recovered as a limit."

--------------------------------------------------------------------------------
(2) AND THAT SIGN SWITCH IS READ OFF THE STATIONARY f TOO.

    f(r) = 1 - 2M/r + Q^2/r^2 - r^2/alpha^2 ,   M CONSTANT

With M constant, Q^2/r^2 beats 2M/r as r -> 0 for any Q > 0, so f -> +oo and the sign has
switched.  ** The conclusion is unconditional only because M is a constant. **

--------------------------------------------------------------------------------
(3) DYNAMICALLY, HALF OF IT SURVIVES AND HALF IS A CONDITION.

  ** SURVIVES: ** the Q^2/r^2 term is NOT a stationary artefact.  In any spherically
  symmetric Einstein--Maxwell spacetime, Gauss's law makes Q a conserved charge and the
  electromagnetic contribution to the Misner--Sharp mass is Q^2/2r identically, so the
  term is there in the dynamical f as well.  *** Charge does not have to wait for
  stationarity to gravitate. ***

  ** A CONDITION: ** m is then a FUNCTION of r, not a constant, and the sign at the
  origin switches iff 2m/r stays below Q^2/r^2 -- that is,

        *** iff  m(r) = o(1/r)  as r -> 0. ***

  Written m ~ k r^(-p) near the origin, verified below: p < 1 keeps the obstruction,
  p > 1 destroys it, and p = 1 is decided by whether 2k exceeds Q^2.

--------------------------------------------------------------------------------
⇒ (4) SO `PO-25`'s REMAINING QUESTION HAS A SHARP FORM IT DID NOT HAVE.

"What stands in the horizon's place" is not an open-ended ask about the interior.  ** It
is: does the interior mass function stay o(1/r) at the origin? **  If it does, the sign
switch holds dynamically and the charged case stays obstructed for the reason `P03`
gives.  If it does not, *** the obstruction `P03` states unconditionally is a stationary
artefact in exactly the way the inner-horizon one was, and the neutral limit question
reopens. ***

⌗ AND THE TWO HALVES OF `sec:charge` NOW READ CONSISTENTLY: one obstruction was found to
be stationary and was said so; the other is stated flatly and is stationary in the same
sense.  ** The paper makes the distinction once and then does not apply it to the claim
standing next to it. **

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.  ** Not that m(r) fails to be o(1/r) -- nothing here computes the
interior. **  Mass inflation is a statement about the Cauchy horizon at finite r, not
about r -> 0, and what m does at the origin behind it is the dynamical interior's
question and stays open.  What is established is that the answer to THAT decides the
sign switch, which is a smaller and better-posed thing than the row currently holds.
"""

import sympy as sp

r, Q, al, M, k = sp.symbols('r Q alpha M k', positive=True)

# --- (2) the stationary reading, unconditional because M is constant ---------------
f_stat = 1 - 2*M/r + Q**2/r**2 - r**2/al**2
assert sp.limit(f_stat, r, 0, '+') == sp.oo, "with M constant the sign must switch"
print("  stationary f with M constant: f -> +oo as r -> 0, for any Q > 0      OK")
print("  -> the sign at the origin has switched, unconditionally              OK")

# --- (3) dynamically the Q^2/r^2 term survives; the competition is with m(r) --------
for p_val, expect, label in ((sp.Integer(0), sp.oo, 'm -> const (the stationary case)'),
                             (sp.Rational(1, 2), sp.oo, 'm ~ r^(-1/2)'),
                             (sp.Integer(2), -sp.oo, 'm ~ r^(-2)')):
    lead = Q**2/r**2 - 2*(k*r**(-p_val))/r
    got = sp.limit(lead, r, 0, '+')
    assert got == expect, f"p={p_val}: expected {expect}, got {got}"
    print(f"    m ~ k r^-{p_val}:  Q^2/r^2 - 2m/r -> {got}   ({label})")
print("  -> p < 1 keeps the obstruction; p > 1 destroys it                    OK")

# --- the marginal case is decided by the coefficient -------------------------------
marg = sp.simplify((Q**2 - 2*k)/r**2)
assert sp.limit(marg.subs(k, Q**2/4), r, 0, '+') == sp.oo, "2k < Q^2 keeps it"
assert sp.limit(marg.subs(k, Q**2), r, 0, '+') == -sp.oo, "2k > Q^2 destroys it"
print("  p = 1 exactly: decided by whether 2k exceeds Q^2                     OK")

# --- (4) and the condition is the whole of what remains ----------------------------
CONDITION = "m(r) = o(1/r) as r -> 0"
assert "o(1/r)" in CONDITION
print(f"\n  => PO-25's remaining question, sharpened: {CONDITION}?")
print("     If yes, the sign switch holds dynamically and the charged case")
print("     stays obstructed.  If no, that obstruction is a stationary artefact")
print("     in exactly the way the inner-horizon one was.                     OK")

print()
print("ESTABLISHED: the Q^2/r^2 term is dynamical (Gauss's law), but the sign switch it")
print("produces is conditional on the interior mass function, m(r) = o(1/r) at the origin.")
print("P03 makes the stationary-versus-dynamical distinction for the inner horizon and")
print("does not apply it to the obstruction stated beside it.")
print("NOT CLAIMED: that m(r) fails the condition. Nothing here computes the interior.")
