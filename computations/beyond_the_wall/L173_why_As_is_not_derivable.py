#!/usr/bin/env python3
"""
`L-173`.  ** WHY $A_s$ IS NOT DERIVABLE AND $n_s$ IS — AND IT IS ONE LINE: $\\hbar$ IS A
MULTIPLICATIVE CONSTANT IN THE POWER SPECTRUM, SO IT SURVIVES IN THE AMPLITUDE AND CANCELS IN THE
TILT. **

The row predicted the verdict and existed to test it rather than assume it: a tilt is a RATIO, an
amplitude is a MAGNITUDE, and c54.128 established this construction cannot force a magnitude.

  PART 1  ** $A_s$ CARRIES $\\hbar$; $n_s$ DOES NOT.  The logarithmic derivative kills it. **
  PART 2  ** SO c54.128's THEOREM APPLIES TO ONE AND NOT THE OTHER, and the corpus carried them as
          a pair for its whole history. **
  PART 3  ** THE INVERSION, WHICH IS THE PAYOFF: $A_s$ is a function of the moduli, so measuring it
          DETERMINES one.  It stops being a debt and becomes an instrument. **
  PART 4  What is settled, and what the inversion still needs.

Run: python3 L173_why_As_is_not_derivable.py      (sympy)
"""
import sympy as sp

print(__doc__.split("Run:")[0])
hbar, k, A0, ns = sp.symbols('hbar k A_0 n_s', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — WHERE hbar SITS")
print("=" * 78)
print("  The mode function's vacuum normalisation is the only place a quantum constant enters:")
print("     v_k = sqrt( hbar / (2 c_s k) ) exp(-i c_s k eta)")
print("  and the curvature perturbation is zeta = v/z with z a CLASSICAL background quantity.")
print("  So the power spectrum carries hbar as an overall multiplicative factor:")
P = hbar * A0 * k**(ns - 1)
print(f"     P_zeta(k) = {P}")
print()
As = sp.simplify(P.subs(k, 1))
tilt = sp.simplify(sp.log(P).diff(sp.log(k)) if False else k * sp.diff(P, k) / P)
print(f"  ** the AMPLITUDE  A_s = P(k_0)      = {As}        -- carries hbar **")
print(f"  ** the TILT       d ln P / d ln k   = {tilt}        -- hbar has CANCELLED **")
assert sp.simplify(sp.diff(As, hbar)) != 0
assert sp.simplify(sp.diff(tilt, hbar)) == 0
print()
for s in [
 "⇒⇒ ** THAT IS THE WHOLE ASYMMETRY, AND IT IS ONE LINE.  $\\hbar$ is a MULTIPLICATIVE constant in",
 "   the spectrum, so it survives in the amplitude and cancels in every logarithmic derivative. **",
 "   *A tilt is a ratio of the spectrum to itself at two wavenumbers; an amplitude is the spectrum",
 "   at one.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — SO c54.128'S THEOREM APPLIES TO ONE AND NOT THE OTHER")
print("=" * 78)
print("  c54.128: a dimensionless MAGNITUDE cannot be forced, because it needs two invariants and")
print("  the substrate has one.  The corpus's ledger makes hbar, c and G ** unit gauges over the")
print("  single scale alpha ** -- so once they are fixed as gauges, the only dimensionless content")
print("  left in the construction is the progenitor's parameters in units of alpha: MODULI.")
print()
print(f"  {'quantity':>16} {'kind':>14} {'carries hbar?':>16} {'derivable here?':>18}")
for a, b, c, d in [("n_s", "a ratio", "no -- cancels", "** YES (c54.122) **"),
                   ("A_s", "a magnitude", "YES", "** NO -- c54.128 **"),
                   ("the running", "a ratio", "no -- cancels", "in principle yes")]:
    print(f"  {a:>16} {b:>14} {c:>16} {d:>18}")
print()
for s in [
 "✔✔ ** SO THE ROW'S PREDICTION IS CONFIRMED AND IS NOW A RESULT: $A_s$ IS PERMANENTLY INHERITED",
 "   WHILE $n_s$ IS NOT, and the two were never the same kind of quantity. **",
 "",
 "⌗⌗ ** AND THE CORPUS CARRIED THEM AS A PAIR FOR ITS ENTIRE HISTORY — 'the amplitude $A_s$ and",
 "   tilt $n_s$, inherited as boundary data' — in every statement of the frontier. **  *Which is",
 "   exactly how one of them got worked for thirteen revisions while the other went unexamined:",
 "   **a phrase that names two things together stops anyone asking whether they are the same kind",
 "   of thing.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE INVERSION")
print("=" * 78)
print("  A quantity that cannot be derived from the invariants is a function of the MODULI, and the")
print("  construction has essentially one: the progenitor's mass in units of alpha.  So")
print()
print("     ** A_s = F(2M/alpha) * (hbar in its gauge) **")
print()
print("  and the relation runs BOTH WAYS.  Read forwards it is a debt; read backwards it is a")
print("  measurement:")
print()
print(f"  {'read':>12} {'statement':>58}")
for a, b in [("forwards", "the geometry cannot predict A_s"),
             ("backwards", "** the observed A_s DETERMINES the progenitor's mass **")]:
    print(f"  {a:>12} {b:>58}")
print()
for s in [
 "⇒⇒⇒ ** SO $A_s$ STOPS BEING A DEBT AND BECOMES AN INSTRUMENT — the only observable that reaches",
 "   the one modulus the construction has. **",
 "",
 "⌗⌗ ** AND IT IS THE SECOND HANDLE ON THE SAME OBJECT, WHICH IS WHAT MAKES IT WORTH HAVING:",
 "   c54.133 constrains the parent's total EXPANSION past equality ($\\rho_r/\\rho_m$ at maximum",
 "   expansion), and this constrains its MASS.  Different combinations, one progenitor. **",
 "   *Two independent observables on a one-parameter family is an OVERDETERMINATION, and that is a",
 "   testable prediction rather than a fit — **which is what `L-172` turned out NOT to be, an hour",
 "   ago, when its advertised overdetermination dissolved on inspection.***",
 "",
 "⌗ *And a third arrives with it: c54.135's recollapse condition caps $2M\\le2\\alpha/3\\sqrt3$. So",
 "   the mass $A_s$ measures must land BELOW Nariai, and that is a yes-or-no check on the whole",
 "   picture the moment $F$ is computed.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT IS SETTLED, AND WHAT THE INVERSION NEEDS")
print("=" * 78)
print(f"  {'claim':>56} {'status':>16}")
for a, b in [("hbar survives in A_s and cancels in n_s", "EXACT"),
             ("so c54.128 forbids deriving A_s but not n_s", "FOLLOWS"),
             ("A_s is a function of the progenitor's mass", "FOLLOWS"),
             ("the function F itself", "** NOT COMPUTED **"),
             ("whether the measured mass lands below Nariai", "awaits F")]:
    print(f"  {a:>56} {b:>16}")
print()
for s in [
 "⚠ ** WHAT THE INVERSION NEEDS IS $F$, AND THAT IS A REAL CALCULATION: the amplitude of the",
 "   surviving mode at the crossing, normalised against the vacuum data, in units of the",
 "   progenitor's mass. **  *The pieces exist — the mode functions (c54.122), the monodromy",
 "   (c54.131), the mode map (c54.133) — and what is missing is the normalisation carried through",
 "   all three rather than tracked as a scaling.*",
 "",
 "⌗ *That is a well-posed next step and it is the FIRST time this row has had one.  Until then the",
 "   settled part stands on its own: **$A_s$ is not derivable, for a reason, and the reason says",
 "   exactly which other quantities share its fate — every magnitude, and no ratio.***",
]:
    print("  " + s)
