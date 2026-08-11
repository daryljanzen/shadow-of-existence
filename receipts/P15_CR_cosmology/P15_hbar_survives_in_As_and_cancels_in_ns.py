#!/usr/bin/env python3
"""
RECEIPT — P15 `sec:transmission`: ** hbar IS A MULTIPLICATIVE CONSTANT IN THE POWER SPECTRUM, SO IT
SURVIVES IN THE AMPLITUDE AND CANCELS IN THE TILT.  THAT IS WHY $n_s$ IS DERIVABLE HERE AND $A_s$
IS NOT — AND THE TWO HAVE BEEN CARRIED AS A PAIR THROUGHOUT. **

  PART 1  ** hbar survives in A_s, cancels in every logarithmic derivative -- asserted **
  PART 2  ** so the no-magnitude result applies to one and not the other **
  PART 3  ** the inversion: A_s measures the one modulus the construction has **

rc=0 on success.  Run: python3 P15_hbar_survives_in_As_and_cancels_in_ns.py     (sympy)
"""
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])
hbar, k, A0, ns = sp.symbols('hbar k A_0 n_s', positive=True)

print("=" * 78)
print("PART 1 — WHERE hbar SITS")
print("=" * 78)
print("  The vacuum normalisation v_k = sqrt(hbar/(2 c_s k)) e^{-i c_s k eta} is the ONLY place a")
print("  quantum constant enters; zeta = v/z with z classical.  So")
P = hbar * A0 * k**(ns - 1)
As = sp.simplify(P.subs(k, 1))
tilt = sp.simplify(k * sp.diff(P, k) / P)
print(f"     P_zeta(k) = {P}")
print(f"     A_s   = P(k_0)          = {As}      <- carries hbar")
print(f"     tilt  = d ln P/d ln k   = {tilt}      <- hbar CANCELLED")
assert sp.simplify(sp.diff(As, hbar)) != 0
assert sp.simplify(sp.diff(tilt, hbar)) == 0
print("  ** an amplitude is the spectrum at one wavenumber; a tilt is its ratio to itself at two. **")

print()
print("=" * 78)
print("PART 2 — SO THE NO-MAGNITUDE RESULT APPLIES TO ONE AND NOT THE OTHER")
print("=" * 78)
print("  Neither real form of the substrate supplies a second scale, so a dimensionless MAGNITUDE")
print("  cannot be forced; and the ledger makes hbar, c and G unit gauges over the single scale.")
print("  Once they are gauges the only dimensionless content left is the progenitor's parameters in")
print("  units of alpha -- moduli.")
print(f"\n  {'quantity':>14} {'kind':>13} {'hbar?':>14} {'derivable?':>16}")
for a, b, c, d in [("n_s", "ratio", "cancels", "YES"),
                   ("A_s", "magnitude", "survives", "NO"),
                   ("the running", "ratio", "cancels", "in principle")]:
    print(f"  {a:>14} {b:>13} {c:>14} {d:>16}")
print("  ** So A_s is permanently inherited while n_s is not, and the two were never the same kind")
print("     of quantity -- though the corpus has named them together in every statement of the")
print("     frontier, which is how one got worked and the other did not. **")

print()
print("=" * 78)
print("PART 3 — THE INVERSION")
print("=" * 78)
print("  A quantity not derivable from the invariants is a function of the moduli, and there is")
print("  essentially one: the progenitor's mass in units of alpha.  So A_s = F(2M/alpha), and the")
print("  relation runs both ways -- forwards a debt, backwards a MEASUREMENT of the parent's mass.")
print("  ** Second handle on the same object: the spectral bound constrains the parent's total")
print("     expansion past equality, this constrains its MASS, and the recollapse condition caps")
print("     that mass below Nariai.  Three constraints, one progenitor, a genuine")
print("     overdetermination once F is computed. **")
print()
print("  BOUND: F itself is NOT computed here.  The pieces exist -- the mode functions, the")
print("  monodromy, the mode map -- and what is missing is the normalisation carried through all")
print("  three rather than tracked as a scaling.  ** The settled part stands alone: A_s is not")
print("  derivable, for a reason, and the reason names exactly which other quantities share its")
print("  fate -- every magnitude, and no ratio. **")
print()
print("ALL PASS")
sys.exit(0)
