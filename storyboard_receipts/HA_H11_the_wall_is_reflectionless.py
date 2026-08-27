#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H11`: ** P14'S WALL IS THE REFLECTIONLESS POSCHL-TELLER PAIR, SO
ITS MODE COMPLETENESS IS A CLASSICAL CLOSED-FORM RESULT AND NOT AN OPEN UNDERTAKING.  WHAT IS OPEN IS
THE JOIN — WHICH IS WHAT P14 ALSO SAYS. **

LEVEL: NO RATE — Sturm-Liouville on the wall profile.

WHY THIS PROBE.  The r3166 harmonic bake read ONE paper.  Measured at r3453, its vocabulary appears in
  TWELVE, and P14 carries the most of any (mode x60).  P14 lists among its open undertakings "the
  quantised field, ITS MODE COMPLETENESS, and the join between the static region's continuum and the
  wall -- which sit in different regions".  Mode completeness is this field's own object, and this
  field had never read the paper.

WHAT IS COMPUTED.  P14's wall is m(x) = tanh(x/a) and its Dirac problem factorises into the SUSY
  partner Schrodinger operators V_-/+ = m^2 -/+ m'.  At a = 1 these are

      V_-  =  tanh^2 - sech^2  =  1 - 2 sech^2 x       (Poschl-Teller, l = 1)
      V_+  =  tanh^2 + sech^2  =  1                    (free)

  Diagonalised: V_- carries EXACTLY ONE bound state, at E = 0 to six figures -- the Jackiw-Rebbi zero
  mode, matching the analytic sech(x)/sqrt(2) -- and its partner V_+ carries NONE.

  ** That is the reflectionless pair.  One bound state plus a reflectionless continuum, for which
  completeness is a classical closed-form result.  So the wall's mode completeness is not open. **

WHAT IS OPEN, AND P14 SAYS SO IN THE SAME SENTENCE: "the JOIN between the static region's continuum
  and the wall -- WHICH SIT IN DIFFERENT REGIONS".  The wall's own spectral problem is solved; joining
  it to the static region's continuum is the undertaking.  ** The clause reads as though three things
  were open and one of the three is not, which understates what the paper has. **

A TOLERANCE ERROR CAUGHT BY THIS RECEIPT'S OWN ASSERT, recorded because it is the second of its kind
  in this bake: the first draft discretised -1/2 d^2/dx^2 instead of -d^2/dx^2 and returned TWO bound
  states with E_0 negative; the second asserted |E_0| < 1e-6 against a grid delivering 1.7e-6.  The
  ledger already records an adaptive-quadrature artefact of the same family.  ** Three numerical
  slips in one field, every one caught by an assert and none of which prose would have caught. **

VERDICTS ARE ASSERTS.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

print("=" * 78)
print("  H11 — P14's wall is the reflectionless Poschl-Teller pair")
print("=" * 78)

L, N = 40.0, 12000
x = np.linspace(-L, L, N)
h = x[1] - x[0]
off = -1 / h**2 * np.ones(N - 1)

print("\n  P14's wall: m(x) = tanh(x/a).  SUSY partners V_-/+ = m^2 -/+ m'.")
print("      V_-  =  1 - 2 sech^2 x   (Poschl-Teller, l = 1)")
print("      V_+  =  1                (free)")

Vm = 1 - 2 / np.cosh(x)**2
w, v = eigh_tridiagonal(2 / h**2 + Vm, off, select='i', select_range=(0, 4))
print("\n  spectrum of -d^2/dx^2 + V_-   (continuum edge at E = 1):")
for i, e in enumerate(w):
    print(f"      E_{i} = {e:+.8f}" + ("   <- BOUND" if e < 0.999 else ""))

nb = int(np.sum(w < 0.999))
assert nb == 1, "the reflectionless l=1 well has EXACTLY one bound state"
assert abs(w[0]) < 1e-5, "and it sits at E = 0 -- the Jackiw-Rebbi zero mode"
psi = v[:, 0] / np.sqrt(np.sum(v[:, 0]**2) * h)
dev = np.max(np.abs(np.abs(psi) - 1 / np.cosh(x) / np.sqrt(2.0)))
assert dev < 1e-3, "and it must match the analytic sech(x)/sqrt(2)"
print(f"  ** VERDICT 1: exactly one bound state, at E = {w[0]:.2e}, matching sech(x)/sqrt2 to"
      f" {dev:.1e}. **")

Vp = 1 + 2 / np.cosh(x)**2
wp, _ = eigh_tridiagonal(2 / h**2 + Vp, off, select='i', select_range=(0, 2))
print(f"\n  spectrum of -d^2/dx^2 + V_+ :  {', '.join(f'{e:+.6f}' for e in wp)}")
assert np.all(wp > 0.999), "the SUSY partner must carry NO bound state"
print("  ** VERDICT 2: the partner is empty.  One bound state and an empty partner is the")
print("     REFLECTIONLESS pair, whose completeness is a classical closed-form result. **")

print("\n  ** VERDICT 3: so the wall's MODE COMPLETENESS is not an open undertaking.  What is")
print("     open is the JOIN to the static region's continuum -- which P14 names in the same")
print("     sentence.  The clause reads as though three things were open; one of the three")
print("     is a solved system, and saying so strengthens the paper. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
