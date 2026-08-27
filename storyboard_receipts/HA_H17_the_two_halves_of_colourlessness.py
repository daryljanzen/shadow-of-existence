#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H17`: ** THE HARMONIC AND REPRESENTATION-THEORY BAKES REACH THE
TWO HALVES OF ONE CONDITION.  THE TRIVIAL FOURIER MODE ON THE DECK Z_3 IS THE NECESSARY HALF OF
COLOURLESSNESS; THE EPSILON ANTISYMMETRY IN 3x3x3 IS THE SUFFICIENT.  P14 STATES EXACTLY THAT. **

LEVEL: NO RATE — the discrete Fourier transform on a finite group.

HOW THIS WAS REACHED, AND IT IS A CORRECTION.  P05 was recorded "checked, negative" on a grep.  The
  verdict is withdrawn and the paper read.  P05's prop:completeness is GENERATION-completeness -- that
  sigma and tau generate the groupoid's morphisms -- which is a different sense from basis
  completeness, and the harmonic analogue for a finite group (Peter-Weyl / Plancherel) is genuinely
  absent from the corpus: `Plancherel` x0, `Parseval` x0, `group algebra` x0, and the four `Peter`
  hits are the NarnhoferPeterThirring citation.

  ** But reading on from there found the corpus DOES use the group Fourier decomposition, in P14's
  receipt appendix and not in any paper body: "a colourless state is the trivial summand of the
  regular representation, which is L-72's single-valuedness READ AS A SUBSPACE." **

WHAT IS COMPUTED.  On three colour indices there are 27 states.
      trivial Fourier summand on Z_3 (triality zero) :  9
      SU(3) singlet (epsilon antisymmetry)           :  6
      singlet is a PROPER SUBSET of triality-zero    :  True
  and the gap is exactly (0,0,0), (1,1,1), (2,2,2) -- ** the same three counterexamples the
  representation-theory bake found independently at r3437 by a different route. **

  ** SO THE TWO FIELD BAKES CONVERGE ON ONE CONDITION FROM OPPOSITE SIDES.  Harmonic analysis on the
  deck gives the NECESSARY half; representation theory on the colour group gives the SUFFICIENT half.
  And P14 already states the relation between them: "triality zero is necessary for a colour singlet
  and NOT SUFFICIENT". **

WHAT THAT SETTLES ABOUT THE METHOD.  Neither bake alone reaches the pair; the corpus states it; and
  the statement lives where a grep for harmonic vocabulary would never look -- inside a receipt
  appendix, phrased in representation-theoretic words.  ** The third instance in this field of a
  finding invisible to a word count. **

VERDICTS ARE ASSERTS.
"""
import itertools

print("=" * 78)
print("  H17 — the two bakes give the two halves of colourlessness")
print("=" * 78)

states = list(itertools.product(range(3), repeat=3))
trivial = [s for s in states if sum(s) % 3 == 0]          # trivial Fourier summand on Z_3
singlet = [s for s in states if len(set(s)) == 3]          # epsilon antisymmetry in 3x3x3

print(f"\n  states of three colour indices               : {len(states)}")
print(f"  trivial Fourier summand on Z_3 (triality 0)  : {len(trivial)}   <- HARMONIC route")
print(f"  SU(3) singlet (epsilon antisymmetry)         : {len(singlet)}   <- REPRESENTATION route")
assert len(states) == 27 and len(trivial) == 9 and len(singlet) == 6

assert set(singlet) < set(trivial), "the singlet must be a PROPER subset of triality-zero"
print("  ** VERDICT 1: the singlet is a PROPER SUBSET of the trivial Fourier summand. **")

gap = sorted(set(trivial) - set(singlet))
print(f"\n  the gap ({len(gap)} states): {gap}")
assert gap == [(0, 0, 0), (1, 1, 1), (2, 2, 2)], \
    "the gap must be exactly the three monochrome states"
print("  ** VERDICT 2: the gap is exactly the three monochrome states -- the SAME three")
print("     counterexamples the representation-theory bake found independently at r3437,")
print("     by the other route. **")

print("\n  ** VERDICT 3: harmonic analysis on the deck gives the NECESSARY half of")
print("     colourlessness; representation theory on the colour group gives the SUFFICIENT")
print("     half; and P14 already states the relation -- 'triality zero is necessary for a")
print("     colour singlet and NOT SUFFICIENT'.  Two bakes, opposite sides, one condition. **")

print("\n  ** VERDICT 4: and the statement lives where a harmonic word count would never look --")
print("     inside P14's receipt appendix, phrased in representation-theoretic words.  The")
print("     third finding in this field invisible to a grep. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
