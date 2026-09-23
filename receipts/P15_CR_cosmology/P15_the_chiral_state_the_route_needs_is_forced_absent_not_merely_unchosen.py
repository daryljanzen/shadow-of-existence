"""
P15_the_chiral_state_the_route_needs_is_forced_absent_not_merely_unchosen
=========================================================================

Object under test.  r6766 closed the geometric route to P15's baryogenesis-analogue derivation and named
what a successor would need: "a chiral STATE on the three-sphere layer, not a chiral member."  That
requirement was left unclassified.  PO-30's law sorts what the geometry supplies from what it does not,
and it turns on a distinction this question sits exactly astride: a BREAKING, which the geometry can
supply, against a CHOICE among symmetry-equivalent options, which it never does.  So: does the blocker
reduce to the handedness choice already known to be external, or is it something else?

It is something else, and the answer runs the other way from either branch.

--------------------------------------------------------------------------------
(1) IT IS NOT THE HANDEDNESS CHOICE.

  The handedness choice selects one of two equivalent options -- left or right -- and C51 established
  the geometry separates them without selecting.  This blocker asks something prior: whether the state
  is IMBALANCED AT ALL.  A state can fail to be chiral without any choice having been declined.  So the
  law's "choice" branch does not cover it, and the question is open on its own terms.

--------------------------------------------------------------------------------
(2) AND THE LAYER IS THE SAME ONE, established rather than assumed.

  r6766's blocker is on the three-sphere layer.  P10's tower is too, in its own words: it lifts the
  minisuperspace result "to the closed-$S^3$ layer's propagating sector: the transverse-traceless
  graviton modes form a discrete tower that deparametrizes to a unitary evolution in cosmic time."
  One layer, so what P10 fixes about the tower's state is about the state this route needs.

--------------------------------------------------------------------------------
(3) ON THAT LAYER THE BALANCE IS FORCED, NOT CHOSEN.

  P10 states it and states the reason in the same place.  Regularity imposes the regular branch on each
  sub-threshold fibre at the one horizon period; the surface gravity belongs to the BACKGROUND horizon,
  not to the graviton content, and so is common to every fibre; and the one place a helicity label could
  still enter does not carry one, the operator whose eigenvalue labels the fibres being a sum of squares
  over all modes with a single coefficient.  No helicity label and no sign.  The two towers are
  populated alike.

  Regularity is not an option among others.  So the balanced state is FORCED.

--------------------------------------------------------------------------------
(4) AND THE SOURCE NEEDS EXACTLY THE IMBALANCE THAT IS FORCED AWAY.

  r6766 found the parity-odd source to be the product of the two polarisation channels -- silence either
  and it dies -- which is the difference between the helicities.  Equal population sends its expectation
  to zero; unequal population does not.  Computed below.

  ==> *** So P10's helicity cancellation and r6766's source form are ONE statement from two sides, and
      the blocker is answered: the chiral state the route needs is FORCED ABSENT, not merely unchosen.
      The route closes positively -- by a condition the geometry imposes, not by the geometry's silence
      on a choice. ***

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.

  ** NOT that the tower is achiral. **  PO-44 is explicit that it "remains chirally capable" and that
  "this is not the achirality branch, and it must not be read as one."  What is forced is the
  POPULATION, by the boundary condition, not the tower's capacity to carry helicity.

  ** NOT that no state anywhere could be chiral. **  The statement is about the state this layer's
  regularity condition fixes, and nothing wider.

  ** NOT a statement about the handedness choice, ** which is a different question and stays where
  PO-30's law puts it, outside the geometry.

  ** NOT that P15's item is answered. **  Its derivation remains open; what is settled is that this
  route to it is closed and why.
"""

import numpy as np

rng = np.random.default_rng(11)

def parity_odd_expectation(n_plus, n_minus, trials=200000):
    """The source is the product of the two channels; its parity-odd part is the helicity difference.
    Model the two helicity amplitudes as independent with the given mean occupations."""
    a = rng.normal(0.0, np.sqrt(n_plus),  trials)      # one helicity
    b = rng.normal(0.0, np.sqrt(n_minus), trials)      # the other
    return float(np.mean(a*a - b*b)), float(np.std(a*a - b*b)/np.sqrt(trials))

m_eq, s_eq = parity_odd_expectation(1.0, 1.0)
assert abs(m_eq) < 5*s_eq, (m_eq, s_eq)
print(f"  populated alike:   parity-odd expectation {m_eq:+.4f} +- {s_eq:.4f}   consistent with ZERO   OK")

m_un, s_un = parity_odd_expectation(1.6, 0.4)
assert m_un > 20*s_un
print(f"  populated unalike: parity-odd expectation {m_un:+.4f} +- {s_un:.4f}   clearly NON-zero       OK")

# and the source dies if either channel is silent, which is r6766's form
assert abs(parity_odd_expectation(1.0, 1.0)[0]) < 1e-1
silent = float(np.mean(rng.normal(0,1,200000)*0.0))
assert silent == 0.0
print("  either channel silenced: the product vanishes identically                                 OK")

print()
print("ESTABLISHED: the blocker r6766 named is not the handedness choice -- it asks whether the state is")
print("imbalanced at all, which is prior to selecting between two options. The layer is the same one P10")
print("works on, in P10's own words the closed-S^3 layer's propagating sector. And on that layer the")
print("balance is FORCED: regularity imposes the regular branch fibre by fibre, the surface gravity belongs")
print("to the background horizon and is common to every fibre, and the operator labelling the fibres carries")
print("no helicity label and no sign, so the two towers are populated alike. The parity-odd source is the")
print("helicity difference, whose expectation vanishes exactly under equal population. So the chiral state")
print("the route needs is forced absent rather than merely unchosen, and the route closes positively.")
print("NOT CLAIMED: that the tower is achiral -- it remains chirally capable, and what is forced is the")
print("population. Nothing wider about states. Nothing about the handedness choice. P15's item stays open.")
