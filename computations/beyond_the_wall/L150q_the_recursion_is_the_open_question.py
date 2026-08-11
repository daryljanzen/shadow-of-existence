#!/usr/bin/env python3
"""
`L-150`, front #1.  ** c54.149's CORRECTION WAS ITSELF TOO CONFIDENT, AND I AM NOT MAKING A THIRD
REFRAMING.  WHAT THE TWO REVISIONS ACTUALLY BRACKET IS A QUESTION ABOUT THE CONSTRUCTION'S RECURSION
THAT THE CORPUS HAS NEVER POSED — AND ONE REAL GAIN THAT SURVIVES EITHER READING. **

c54.143–148 propagated the progenitor's FULL lap, from the closed ball's own $a=0$, and composed the
result with the monodromy into a periodic map.  c54.149 called that a background the construction
does not contain, on the strength of P16 `sec:lap`: the progenitor is a black hole in a previous
universe.  ** Both statements are true, and they do not settle the question, because in the standard
spherical-collapse description an overdense PATCH is a closed FRW solution whose $a=0$ is the
BACKGROUND's $a=0$ — the previous universe's own beginning, which in this construction is a branch
point. **

  PART 1  ** SPHERICAL COLLAPSE PUTS THE PATCH'S $a=0$ AT THE AMBIENT UNIVERSE'S OWN BEGINNING, so
          c54.149's ground for calling the full lap unphysical does not hold. **
  PART 2  ** BUT THE FULL-LAP APPARATUS IS NOT REINSTATED EITHER, because composing the monodromy at
          the patch's $a=0$ presumes the previous universe's branch point acts in the PATCH's
          harmonic basis with the PATCH's $\\rho$ — which nothing establishes. **
  PART 3  ** SO THE QUESTION IS THE RECURSION ITSELF, stated precisely, with what would settle it. **
  PART 4  ** THE ONE REAL GAIN, WHICH SURVIVES EITHER READING: chain A becomes a DERIVATION, and the
          progenitor acquires a turnaround epoch and a mass. **

Run: python3 L150q_the_recursion_is_the_open_question.py      (numpy)
"""
import numpy as np

print(__doc__.split("Run:")[0])
RHO, MPC, LAM = 0.0539, 3.0857e22, 1.1056e-52
alpha = np.sqrt(3 / LAM) / MPC
M_nar = alpha / (3 * np.sqrt(3))
A = 2 * M_nar
Z_EQ = 3399.0

# =====================================================================
print("=" * 78)
print("PART 1 — SPHERICAL COLLAPSE PUTS THE PATCH'S a=0 AT THE BACKGROUND'S")
print("=" * 78)
for s in [
 "  The textbook description of an overdensity is a CLOSED FRW solution -- the same closed",
 "  dust(+radiation) solution this arc has been using -- and it runs from a = 0, at the SAME cosmic",
 "  time as the background's a = 0.  The patch is a small perturbation early and only becomes",
 "  'its own universe' late.",
 "",
 "⇒ ** SO THE PATCH'S PAST a = 0 IS NOT A FICTITIOUS EXTENSION.  It is the ambient universe's own",
 "   beginning -- which, in this construction, is a branch point. **",
 "   *c54.149 said the ball 'separated, turned around and collapsed' and inferred that its past",
 "   $a=0$ was algebra rather than history.  **The separation is not a beginning; it is a late",
 "   feature of a history that starts with the background's.***",
]:
    print(s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — BUT THE APPARATUS IS NOT REINSTATED")
print("=" * 78)
print(f"  {'the full-lap map needs':>50} {'is it established?':>22}")
for a_, b_ in [("a branch point at the patch's a = 0", "yes -- the previous universe's"),
               ("the monodromy to act on the PATCH's modes", "** NOT established **"),
               ("in the PATCH's harmonic basis (its k_L)", "** NOT established **"),
               ("with the PATCH's rho and M", "** NOT established **")]:
    print(f"  {a_:>50} {b_:>22}")
print()
for s in [
 "⚠⚠ ** THE MONODROMY AT THE PREVIOUS BRANCH POINT IS THAT UNIVERSE'S, WITH ITS OWN $\\rho$, ITS OWN",
 "   $M$, AND ITS OWN $S^3$ HARMONIC LABELLING.  The patch's closed-FRW harmonic index is a",
 "   different decomposition of the same physical modes, and composing $J(\\rho_{\\rm patch})$ at the",
 "   patch's $a=0$ silently identifies the two. **",
 "   *Self-similarity makes the numbers agree — each universe like ours — but not the LABELLING, and",
 "   the labelling is what the Floquet composition acts on.*",
 "",
 "⌗ ** SO c54.143–148 ARE NOT RESTORED AND c54.149 IS NOT RESTORED.  Both stand withdrawn, and what",
 "   they bracket is a question neither posed. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE QUESTION, STATED PRECISELY")
print("=" * 78)
for s in [
 "  ***In this construction each universe issues from a branch point and later collapses parts of",
 "  itself into new ones.  For a mode observed today, what is its history through that recursion --",
 "  in whose harmonic basis, through how many passages, and with which monodromy at each?***",
 "",
 "  ** What would settle it, and it is a question about the construction rather than a computation: **",
 "     (i)  whether the patch's closed-$S^3$ harmonics and the ambient universe's are related by a",
 "          fixed map, or whether the patch's own labelling is only meaningful after separation;",
 "     (ii) whether a mode that is SUB-patch today was sub-patch at the previous branch point, or",
 "          only became so when the patch turned around;",
 "     (iii) and therefore whether the previous monodromy acts on it at all.",
 "",
 "⌗ ** NONE OF THE THREE IS ANSWERED ANYWHERE IN THE CORPUS, AND THE RECURSION IS ASSERTED IN ONE",
 "   SENTENCE AND NEVER UNFOLDED. **  *That is the actual state of front #1, and it took nine",
 "   revisions of apparatus to arrive at a question this plain.*",
]:
    print(s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE GAIN THAT SURVIVES EITHER READING")
print("=" * 78)
a_eq = A * RHO**2 / 4
ratio = 4 / RHO**2
z_ta = Z_EQ / ratio - 1
Mkg = (M_nar * MPC) * (2.99792458e8)**2 / 6.674e-11
print(f"  {'quantity':>50} {'value':>18}")
for nm, v, u in [("A = 2M", A, "Mpc"),
                 ("a_eq = A rho^2/4", a_eq, "Mpc  (ours: 1.490)"),
                 ("a_max/a_eq = 4/rho^2", ratio, ""),
                 ("turnaround redshift in the previous universe", z_ta, ""),
                 ("progenitor mass", Mkg, "kg"),
                 ("  in solar masses", Mkg / 1.989e30, "")]:
    print(f"  {nm:>50} {v:>18.4g} {u}")
assert abs(a_eq - 1.49) < 0.05
assert 0.5 < z_ta < 5
print()
for s in [
 "✔✔✔ ** CHAIN A IS NOW A DERIVATION RATHER THAN AN ASSERTION.  A small perturbation shares the",
 "   background's composition, so $a_{\\rm eq}$(patch) $=a_{\\rm eq}$(background) — which is exactly",
 "   what chain A asserted from 'one $M$ across the bead plus a crossing plasma'. **",
 "   *Spherical collapse gives it for free, and the arithmetic closes: $A\\rho^2/4=1.492$ Mpc against",
 "   the observable leg's $1.490$.*",
 "",
 "✔✔ ** AND THE PROGENITOR ACQUIRES TWO PHYSICAL NUMBERS IT DID NOT HAVE: it turns around at",
 f"   $z\\simeq{z_ta:.1f}$ in the previous universe — an ordinary structure-formation epoch — and its",
 f"   mass is ${Mkg:.1e}$ kg, comparable to this universe's own matter content. **",
 "   *Which is precisely what 'the matter of our hot dense era is that previous universe's collapsed",
 "   matter' requires, and the first time that sentence has been checked against a number.*",
]:
    print("  " + s)
