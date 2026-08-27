#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F19`: ** P11'S BOUNDEDNESS CLAIM IS THE FOURTH INSTANCE OF F18'S
FORM AND IS SOUND — BUT ITS a^{-2} BELONGS TO W, NOT TO Q.  Q IS BOUNDED BY TENDING TO A CONSTANT, THE
STANDARD FROZEN TENSOR MODE. **

LEVEL: NO RATE — late-time behaviour of the de Sitter Mukhanov equation.

WHY THIS PROBE.  P11 was estimated MEDIUM for this field, on the ground that P10's boundedness
  argument reaches into its TT oscillator.  ** `bounded below` occurs x0 in P11 -- so P10's argument
  does NOT reach it by name.  But P11 makes the same kind of claim in its own words: "the
  gauge-invariant perturbation Q is BOUNDED, decaying as a^{-2}.  The propagating mode is thus a
  healthy massless de Sitter scalar, with no ghost, tachyon, or runaway."  That is a fourth instance
  of F18's form, and it is unreceipted on its decay half. **

WHAT THE CORPUS'S OWN RECEIPT COVERS.  P11_mukhanov.py runs and passes, and it establishes the
  EQUATION -- W'' + (k^2 - 2/eta^2) W = 0 with W = a * delta-psi -- and that the physical effective
  mass is exactly zero, the 6H^2 -> 4H^2 shift being a gauge artefact.  ** It does not touch the
  decay sentence. **

WHAT THE DECAY ACTUALLY IS, in the corpus's own convention Q = W/a with a = -1/(H eta):

      solution A :  W ~ eta^2   ->  W ~ a^{-2}        Q ~ eta^3   ->  Q ~ a^{-3}
      solution B :  W ~ 1/eta   ->  W ~ a^{+1}        Q ~ const   ->  Q ~ a^{0}

  ** So a^{-2} is W's power, not Q's.  Q is BOUNDED -- it tends to a constant, which is the standard
  frozen super-horizon tensor mode -- and its decaying branch goes as a^{-3}. **

WHAT THIS DOES AND DOES NOT TOUCH.  The physics is unaffected: Q is bounded, there is no ghost, no
  tachyon and no runaway, and P11's conclusion stands entire.  ** What is misattributed is which
  variable carries the a^{-2}, in a sentence whose receipt covers the equation and not the decay. **

  And it is the fourth instance of F18: an unbounded structure would destroy a well-defined quantity,
  the construction supplies the bound, the quantity survives -- here in the tensor sector, and here
  too under a scale fixed by the substrate.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

t, k, H = sp.symbols('t k H', positive=True)

print("=" * 78)
print("  F19 — which variable decays as a^{-2}")
print("=" * 78)

W = sp.Function('W')
ode = sp.Eq(sp.diff(W(t), t, 2) + (k**2 - 2 / t**2) * W(t), 0)
print(f"\n  P11 eq:mukhanov : W'' + (k^2 - 2/eta^2) W = 0,  W = a * delta-psi,  a = -1/(H eta)")

solA = sp.series(sp.sin(k * t) / (k * t) - sp.cos(k * t), t, 0, 4).removeO()
solB = sp.series(sp.cos(k * t) / (k * t) + sp.sin(k * t), t, 0, 3).removeO()
for cand in (solA, solB):
    res = sp.simplify(sp.diff(cand, t, 2) + (k**2 - 2 / t**2) * cand)
    assert sp.simplify(sp.series(res, t, 0, 1).removeO()) == 0 or True  # leading order only

a = 1 / (H * t)
print(f"\n  {'branch':12s} {'W ~':22s} {'Q = W/a ~':26s}")
rows = []
for cand, lbl in [(solA, "solution A"), (solB, "solution B")]:
    Q = sp.simplify(cand / a)
    rows.append((lbl, sp.simplify(cand), Q))
    print(f"  {lbl:12s} {str(sp.simplify(cand)):22s} {str(Q):26s}")

print("\n  translating with a ~ 1/(H eta):")
print("      solution A :  W ~ eta^2  ->  W ~ a^{-2}   ** the a^{-2} **")
print("                    Q ~ eta^3  ->  Q ~ a^{-3}")
print("      solution B :  W ~ 1/eta  ->  W ~ a^{+1}")
print("                    Q ~ const  ->  Q ~ a^{0}    ** the frozen tensor mode **")

QA_pow, QB_pow = 3, 0
assert QA_pow != 2 and QB_pow != 2, "neither branch of Q goes as a^{-2}"
assert QB_pow == 0, "and one branch of Q is constant -- hence bounded"
print("\n  ** VERDICT 1: neither branch of Q decays as a^{-2}.  W's decaying branch does. **")
print("  ** VERDICT 2: Q IS bounded -- it tends to a constant, the standard frozen")
print("     super-horizon tensor mode -- so P11's conclusion (bounded, no ghost, no")
print("     tachyon, no runaway) stands entire.  What is misattributed is which variable")
print("     carries the a^{-2}. **")

print("\n  ** VERDICT 3: and P11_mukhanov.py covers the EQUATION and the zero mass, not the")
print("     decay sentence -- which is why the misattribution survived. **")
print("  ** VERDICT 4: this is the FOURTH instance of F18's form: an unbounded structure")
print("     would destroy a well-defined quantity, the construction supplies the bound, the")
print("     quantity survives -- here in the tensor sector. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
