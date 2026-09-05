#!/usr/bin/env python3
"""
RECEIPT -- P14: ** THE CONSTRUCTION'S TWO HANDLES ON MATTER CONTENT ARE BOTH BLIND
TO THE SIXTEENTH WEYL FERMION. **

*P14 states the per-generation content as fifteen Weyl fermions, "or sixteen with a
right-handed neutrino", and argues for neither.  The question is whether anything
this construction supplies can decide between them.  It cannot, and this receipt
shows that rather than asserting it.*

** THE CONSTRUCTION HAS EXACTLY TWO HANDLES ON MATTER CONTENT, and they act at
different levels. **

  (1) THE GENERATION COUNT is a gamma-5-graded index of wall-localised zero modes,
      dim ker_+ = 3 and dim ker_- = 0.  ** It counts GENERATIONS, not the content
      within one **, so it is silent on per-generation multiplet content by its own
      construction.  Nothing to compute: the index's domain is the wrong one.

  (2) THE ANOMALY CONDITION is the one constraint the geometry places ON content.
      There is no bulk gauge field, so there is no inflow, so each wall's content
      must be anomaly-free ON ITS OWN -- and because the walls are three separate
      loci, the condition applies generation by generation.  ** This one CAN be
      computed against, and this receipt does. **

** WHAT IS COMPUTED HERE. **  All four gauge and mixed anomaly coefficients for a
Standard Model generation in left-handed Weyl form, with and without the singlet
nu^c : (1,1)_0, together with the three P14 states explicitly as the checks that the
fifteen cancel "only as a complete set".

** THE RESULT. **  nu^c carries zero colour, zero isospin and zero hypercharge, so
its contribution to every channel is identically zero.  ** Fifteen is anomaly-free
and sixteen is anomaly-free, and the condition's value is the SAME NUMBER in both
cases -- so the construction's one constraint on content cannot distinguish them. **

** WHAT THIS SETTLES AND WHAT IT DOES NOT. **  It settles that a preference for
sixteen cannot be sourced from this construction: the index does not reach the
question and the anomaly condition returns the same verdict either way.  Any such
preference must come from outside -- from the completeness of an so(10) 16, say --
and importing it is precisely the representation-content step P14 declines.  ** It
does NOT settle which content is correct **, which is not a question this
construction is in a position to ask.
"""
from fractions import Fraction as F
import sys

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


# One Standard Model generation, left-handed Weyl form.
# (name, colour multiplicity, isospin multiplicity, hypercharge)
GENERATION = [
    ('Q',   3, 2, F(1, 6)),
    ('u^c', 3, 1, F(-2, 3)),
    ('d^c', 3, 1, F(1, 3)),
    ('L',   1, 2, F(-1, 2)),
    ('e^c', 1, 1, F(1)),
]
NU_C = ('nu^c', 1, 1, F(0))          # the sixteenth: a total singlet


def anomalies(multiplets):
    """The four coefficients that must vanish, per wall."""
    u1_cubed = sum(c * i * Y ** 3 for _, c, i, Y in multiplets)
    u1_grav = sum(c * i * Y for _, c, i, Y in multiplets)
    # T(fundamental) = 1/2 for both su(2) and su(3)
    su2_sq_u1 = sum(c * F(1, 2) * Y for _, c, i, Y in multiplets if i == 2)
    su3_sq_u1 = sum(i * F(1, 2) * Y for _, c, i, Y in multiplets if c == 3)
    return {'[u1]^3': u1_cubed, 'u1-grav': u1_grav,
            '[su2]^2 u1': su2_sq_u1, '[su3]^2 u1': su3_sq_u1}


print()
print("  THE SIXTEENTH WEYL FERMION -- can the construction see it?")
print("  " + "=" * 70)
print()

a15 = anomalies(GENERATION)
a16 = anomalies(GENERATION + [NU_C])

print("  channel        fifteen      sixteen      nu^c contributes")
for k in a15:
    print(f"    {k:<13} {str(a15[k]):>8} {str(a16[k]):>12} {str(a16[k]-a15[k]):>16}")
print()

check("the fifteen are anomaly-free on every channel",
      all(v == 0 for v in a15.values()))
check("the sixteen are anomaly-free on every channel",
      all(v == 0 for v in a16.values()))
check("nu^c contributes exactly zero to every channel",
      all(a16[k] - a15[k] == 0 for k in a15))
check("** so the anomaly condition returns the SAME verdict for both **",
      a15 == a16)

print()
print("  " + "-" * 70)
print("  P14's own checks, that the fifteen cancel only as a complete set:")

# P14: removing e^c leaves [u1]^3 = -1; removing u^c leaves 8/9; removing L leaves 1/4
for drop, expected in (('e^c', F(-1)), ('u^c', F(8, 9)), ('L', F(1, 4))):
    reduced = [m for m in GENERATION if m[0] != drop]
    got = anomalies(reduced)['[u1]^3']
    print(f"    removing {drop:<4} leaves [u1]^3 = {str(got):>6}   (P14 states {str(expected)})")
    check(f"removing {drop} reproduces P14's stated residue", got == expected)

print()
check("and removing nu^c from the sixteen leaves NOTHING -- the mark of invisibility",
      anomalies([m for m in GENERATION + [NU_C] if m[0] != 'nu^c']) == a16)

print()
print("  " + "=" * 70)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f in FAILED:
        print(f"    - {f}")
    sys.exit(1)
print("  The generation index counts generations and not content within one.")
print("  The anomaly condition returns the identical verdict for fifteen and")
print("  sixteen.  ** Both of this construction's handles on matter content are")
print("  ** blind to the sixteenth state, so no preference between them can be")
print("  ** sourced here -- which is shown, not assumed.")
print()
sys.exit(0)
