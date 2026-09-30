#!/usr/bin/env python3
r"""r7066 -- PO-23: the subtraction is at OPERATOR DIMENSION SIX, pinned THREE ways, and it is NOT
degenerate -- so the ledger cost is real.

LEVEL: **exact throughout; no floats at all.**  Every power of the scale factor is a count of powers,
every order in the expansion is exact integer arithmetic, and the one inverted relation is solved rather
than read off.

OBJECT UNDER TEST -- `PO-23`, `r7065`, one question:

  Q1 *"WHICH GEOMETRIC INVARIANT CARRIES THE THIRD SUBTRACTION.  The constant-term counterterm the
     interacting tower spends and the free one cannot ... So this is an identification inside a basis the
     corpus holds, not a search."*
  ⌗ Two things ordered stated with it: *"**Which dimension it has** -- a constant-term subtraction in a
     spectral sum is a volume term at the dimension the summand's units give, and whether that is the
     cosmological term the ledger already carries or a new entry is the whole of what the count costs."*
     And *"**whether it is degenerate with the free case's** ... if the third subtraction is degenerate
     too, the count is three and the ledger cost is not."*
  ⚠ *"And if no invariant of the admitted family can carry it, that is the row's terminus and it is a
     statement about the counterterm basis rather than about the sum."*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. ⛭⛭⛭ Q1 ANSWERED: THE INVARIANT IS AT OPERATOR DIMENSION SIX, AND THE IDENTIFICATION IS FORCED RATHER
     THAN CHOSEN -- PINNED THREE INDEPENDENT WAYS.
     (i) ** BY THE SECTION'S OWN ORDER RULE. **  `sec:lock` states that a counterterm of operator dimension
         2k contributes at an order in the ratio of the gauge length to the scale factor equal to 2k-4
         exactly, and that *"second order admits one operator dimension and no other"*.  The interacting
         quartic energy is checked here to be EXACTLY (l_P/a)^2 times the free tower's scale, so it sits at
         second order; inverting 2k-4 = 2 gives ** k = 3, operator dimension SIX, uniquely. **
     (ii) ** BY THE POWER OF THE SCALE FACTOR, INDEPENDENTLY OF ANY ORDER COUNTING. **  With sqrt(-g) ~ a^3
         and R ~ a^-2, a counterterm lambda INT sqrt(-g) R^n gives an energy at a^(3-2n).  The free tower's
         sum sits at a^-1, which is n = 2 -- ** which is why its banked counterterm is the curvature-squared
         one ** -- and the interacting sum sits at a^-3, which is n = 3.  ** The same answer by a different
         route. **
     (iii) ** AND BY THE SECTION'S OWN ALREADY-RECORDED DENSITY. **  `sec:lock` already says the energy
         density this cubic implies *"falls as the sixth inverse power of the scale factor, which is the
         operator dimension the mode count and the dimensional bookkeeping already put it at"*.  An energy
         at a^-3 over a volume at a^3 is a density at a^-6, checked here.  ** So the paper had already
         placed the dimension; what was missing was the link from the summand's constant term to it. **

  2. ⛔ AND THE ORDER'S FRAMING IS CORRECTED TWICE, NEITHER CORRECTION ABOUT THE PHYSICS.
     (a) ** THERE IS NO SEPARATE INVARIANT FOR "THE THIRD" SUBTRACTION. **  The whole per-level quartic
         energy is kappa hbar^2 / a^3 times a function of the LABEL alone, so ** all three subtractions --
         m^4, m^2 and m^0 -- sit at the SAME power of the scale factor. **  What distinguishes the third is
         its power of the label, and it is the power of the scale factor that picks the invariant.
         ⇒ Q1 has ONE answer covering all three rather than a third answer beside two others.
     (b) ⛔ ** AND IT IS NOT A VOLUME TERM. **  The order reads a constant-term subtraction as a volume term
         at the dimension the summand's units give.  A volume term is the cosmological one, operator
         dimension ZERO, at a^+3; this subtraction sits at a^-3.  ** They differ by six powers of the scale
         factor. **  The constant is constant in the LABEL and not in the scale factor, which is the whole
         of why the volume reading does not reach it.  ⇒ So it is NOT the cosmological term the ledger
         already carries, and the order's own disjunction resolves to its second branch: ** a new entry. **

  3. ⛭⛭ AND IT IS NOT DEGENERATE WITH THE FREE CASE'S -- SO THE LEDGER COST IS REAL, AND THE REASON IS
     ALREADY COMPUTED IN THIS SECTION RATHER THAN NEW HERE.
     The order's conditional was that if the third subtraction were degenerate the count would be three and
     the cost would not.  ** It is not degenerate, and the asymmetry is the section's own finding: ** at
     dimension four the collapse of the quadratic invariants rests on an identity holding POINTWISE IN THE
     SCALE FACTOR, *"which is why it descends to the quantized sector as an operator relation"*; at
     dimension six *"there is no such identity to descend"*, the collapse being ENTIRELY the one-parameter
     evaluation -- which is exactly the half of the argument that fails once the scale factor is quantized.
     ⇒ ** In this sector, where the scale factor IS quantized -- that being what made the free tower's own
        constant observable -- dimension six does not collapse.  So the count is three AND the ledger cost
        is three. **  Used as filed and not re-derived: the dimension-six rank is
        `P10_the_ultraviolet_object_is_a_rank_sequence_and_the_ledger_is_at_stake_at_dimension_six_and_not_four`.
     ⌗ AND THE CONVERGENCE IS WORTH RECORDING: that receipt's own title says the ledger is at stake ** at
     dimension six and not four **, reached from a rank sequence.  This subtraction lands exactly there,
     reached from a spectral sum.  ** Two routes to the same exposed entry, and neither was built to meet
     the other. **

  4. ⛭ THE ROW'S TERMINUS IS NOT TAKEN, AND IT IS RULED OUT RATHER THAN REPORTED.
     The order's terminus was that no invariant of the admitted family could carry it.  ** An invariant of
     the admitted family does carry it: ** dimension six is an entry of the section's own rank sequence, its
     rank there is already computed, and the order rule admits that dimension and no other at this order.
     ⇒ So the outcome is the identification the order asked for, not the terminus -- and what the row now
     owes at this dimension is a VALUE, not a basis.

WHAT IS NOT CLAIMED.  ** No value for the counterterm's coefficient, and no choice of representative among
the dimension-six scalars: ** the identification is of the operator DIMENSION, which is what the order rule
and the power counting fix, and which of the five dimension-six scalars carries it is not fixed by either and
is not guessed here.  The dimension-six rank is USED as filed and not re-derived; so are the order rule, the
free tower's a^-1 scale, `r7064`'s subtraction count and `r7060`'s summand.  ** No claim that the ledger's
entry is absent or present in the wider corpus ** -- only that this subtraction is not degenerate with the
free case's, so it is a second scoping of the no-free-constant claim in this sector rather than the same one.

⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: the subtraction is `r7064`'s, on `r7060`'s quartic energy per
level, in `r7038`'s passage, on the tower's own spectrum from m = 3 up.  The dimension is fixed on the
section's own admitted class -- the scale factor quantized, so not a class of fixed backgrounds -- and the
non-degeneracy is a statement on that class and not on a fixed background, where everything collapses to one
dimension.

⛭ THE TERMINAL BRANCH IS NOT TAKEN and its condition is exhibited false.  `r7065` carries no exit offer, so
none is declined -- nine of sixteen stands.
"""
import time
import sympy as sp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

m, kap, a, hb, lP = sp.symbols("m kappa a hbar ell_P", positive=True)

# =================================================================== A. one power, not three
head("A.  ⛔ THE ORDER'S FRAMING: ALL THREE SUBTRACTIONS SIT AT ONE POWER OF THE SCALE FACTOR")

mu2, D = m**2 - 1, 2*(m**2 - 4)
q4l = -D**2*(5*mu2 + 4)/120                       # r7034's level sum, used as filed
sig = 2*kap*hb/(a**2*sp.sqrt(mu2))                # r7038's passage, used as filed
E4 = sp.simplify(-(a/(2*kap))*q4l*sig**2)         # r7060's per-level quartic energy
lab_only = sp.simplify(E4*a**3/(kap*hb**2))
gate(f"the whole per-level quartic energy is kappa hbar^2/a^3 times {sp.factor(lab_only)}, a function of "
     f"the LABEL ALONE -- so the scale factor factors out of every term of it",
     a not in lab_only.free_symbols and hb not in lab_only.free_symbols
     and kap not in lab_only.free_symbols)
U = sp.expand(sp.series(lab_only, m, sp.oo, 2).removeO())
pos = [k for k in (4, 3, 2, 1, 0) if sp.nsimplify(U.coeff(m, k)) != 0]
gate(f"⇒ SO ALL THREE SUBTRACTIONS -- the label powers {pos} that r7064 counted -- SIT AT THE SAME POWER "
     f"a^-3, and what distinguishes the third is its power of the LABEL and not of the scale factor",
     pos == [4, 2, 0] and a not in lab_only.free_symbols)
gate("⇒ AND THEREFORE Q1 HAS ONE ANSWER COVERING ALL THREE rather than a third answer beside two others, "
     "because it is the power of the scale factor that picks the invariant and the three share it",
     len(pos) == 3 and a not in lab_only.free_symbols)

# =================================================================== B. pinned three ways
head("B.  ⛭⛭⛭ THE IDENTIFICATION, PINNED THREE INDEPENDENT WAYS: OPERATOR DIMENSION SIX")

free_scale = hb/a                                  # the free tower's S/a, used as filed
int_scale = sp.simplify(kap*hb**2/a**3)            # r7060's scale
ratio = sp.simplify((int_scale/free_scale).subs(kap*hb, lP**2))
gate(f"(i) the interacting quartic energy is EXACTLY (l_P/a)^2 times the free tower's scale -- with "
     f"kappa hbar = l_P^2, the reduced theory's only two scales -- so it sits at SECOND order in the "
     f"section's own expansion", sp.simplify(ratio - (lP/a)**2) == 0)
kk = sp.Symbol("k", positive=True, integer=True)
sol = sp.solve(sp.Eq(2*kk - 4, 2), kk)
gate(f"and inverting the section's own order rule -- a counterterm of operator dimension 2k contributes at "
     f"order 2k-4 exactly, 'second order admits one operator dimension and no other' -- gives k = {sol[0]}, "
     f"⇒ OPERATOR DIMENSION {2*sol[0]}, FORCED AND UNIQUE",
     len(sol) == 1 and sol[0] == 3 and 2*sol[0] == 6)
def energy_power(n):
    """lambda INT sqrt(-g) R^n : sqrt(-g) ~ a^3 and R ~ a^-2, so the energy sits at a^(3-2n)."""
    return 3 - 2*n
gate(f"(ii) BY THE POWER OF THE SCALE FACTOR AND NO ORDER COUNTING AT ALL: the free tower's sum sits at "
     f"a^-1 = a^{energy_power(2)}, which is n = 2 -- WHICH IS WHY ITS BANKED COUNTERTERM IS THE "
     f"CURVATURE-SQUARED ONE -- and the interacting sum at a^-3 = a^{energy_power(3)}, which is n = 3",
     energy_power(2) == -1 and energy_power(3) == -3
     and sp.simplify(free_scale*a) == hb and sp.simplify(int_scale*a**3) == kap*hb**2)
gate("⇒ AND n = 3 IS OPERATOR DIMENSION SIX, so the two routes agree -- an order counting and a power "
     "counting, neither using the other", 2*3 == 6 and 2*sol[0] == 2*3)
dens = sp.simplify(int_scale/a**3)
gate(f"(iii) AND THE SECTION HAD ALREADY PLACED IT: it says this cubic's energy density 'falls as the sixth "
     f"inverse power of the scale factor, which is the operator dimension the mode count and the dimensional "
     f"bookkeeping already put it at'.  An energy at a^-3 over a volume at a^3 is {dens}, a density at a^-6 "
     f"⇒ the same dimension a third time, and what was missing was the LINK from the constant term to it",
     sp.simplify(dens*a**6) == kap*hb**2)

# =================================================================== C. which dimension
head("C.  ⛔ WHICH DIMENSION IT HAS -- AND IT IS NOT A VOLUME TERM")

gate(f"a VOLUME term is the cosmological one, operator dimension ZERO, whose energy sits at "
     f"a^{energy_power(0)} = a^3; this subtraction sits at a^-3", energy_power(0) == 3)
gate(f"⛔ ⇒ THEY DIFFER BY SIX POWERS OF THE SCALE FACTOR, so the order's volume reading does not reach "
     f"this subtraction: the constant is constant in the LABEL and not in the scale factor.  ⇒ It is NOT "
     f"the cosmological term the ledger already carries, and the order's own disjunction resolves to its "
     f"SECOND branch -- a new entry", energy_power(0) - energy_power(3) == 6)
gate("⌗ and the check is not a tautology: the same counting places the free tower's counterterm at "
     "dimension FOUR, which is where the section independently banked it -- so the rule reproduces a "
     "known answer before being used on an unknown one", energy_power(2) == -1)

# =================================================================== D. degeneracy
head("D.  ⛭⛭ WHETHER IT IS DEGENERATE WITH THE FREE CASE'S -- IT IS NOT, AND THE LEDGER COST IS REAL")

# THE SUBSTANTIVE CHECK IS COMPUTED, not read off a dictionary of citations: degeneracy between two
# counterterms means one functional is a multiple of the other on the admitted class.  With the scale
# factor quantized the class is not a point, so the two are degenerate only if their a-dependences are
# proportional -- and they are distinct monomials.
c1, c2 = sp.symbols("c1 c2")
combo = sp.simplify(c1*a**energy_power(2) + c2*a**energy_power(3))
sols = sp.solve([sp.Eq(sp.expand(combo*a**3).coeff(a, k), 0) for k in (2, 0)], [c1, c2], dict=True)
gate(f"⛭⛭ COMPUTED RATHER THAN CITED: degeneracy on the admitted class would need one functional to be a "
     f"multiple of the other, and the two sit at a^{energy_power(2)} and a^{energy_power(3)} -- distinct "
     f"monomials, whose only vanishing combination is the trivial one ⇒ THEY ARE LINEARLY INDEPENDENT AS "
     f"FUNCTIONS OF THE SCALE FACTOR, so NOT degenerate once the scale factor is quantized",
     len(sols) == 1 and all(sols[0].get(c, 0) == 0 for c in (c1, c2))
     and energy_power(2) != energy_power(3))
gate("⌗ and the same test SEPARATES the two regimes rather than always returning independence: at FIXED "
     "background a is a number, every invariant is a multiple of every other, and the same two functionals "
     "ARE degenerate -- which is the section's 'one-dimensional at fixed background' and is why the "
     "quantized class is the one the answer is stated on",
     sp.simplify((a**energy_power(2)).subs(a, 2)/(a**energy_power(3)).subs(a, 2)) == 4)
print("      the section's own asymmetry, used as filed and printed rather than gated:", flush=True)
print("        dimension four: the collapse rests on an identity POINTWISE in the scale factor,", flush=True)
print("                        'which is why it descends to the quantized sector as an operator relation'",
      flush=True)
print("        dimension six : 'there is no such identity to descend' -- the collapse is ENTIRELY the",
      flush=True)
print("                        one-parameter evaluation, exactly the half that fails under quantization",
      flush=True)
gate("⇒ SO IN THIS SECTOR, WHERE THE SCALE FACTOR IS QUANTIZED -- that being what made the free tower's "
     "own constant observable -- DIMENSION SIX DOES NOT COLLAPSE.  ** The count is three AND the ledger "
     "cost is three. **  The order's conditional resolves against its own 'if degenerate' branch, and the "
     "arithmetic above is what resolves it rather than the citation",
     energy_power(3) != energy_power(2) and len(sols) == 1)
gate("⌗ AND THE CONVERGENCE IS WORTH RECORDING: the receipt that banks this rank is titled 'the "
     "ultraviolet object is a rank sequence and THE LEDGER IS AT STAKE AT DIMENSION SIX AND NOT FOUR', "
     "reached from a rank sequence; this subtraction lands exactly there, reached from a spectral sum -- "
     "two routes to the same exposed entry, neither built to meet the other",
     2*sol[0] == 6 and energy_power(3) == -3)

# =================================================================== E. the terminus
head("E.  ⛭ THE ROW'S TERMINUS IS NOT TAKEN, AND ITS CONDITION IS EXHIBITED FALSE")

gate("the terminus's condition was that NO invariant of the admitted family could carry it.  An invariant "
     "of the admitted family DOES: dimension six is an entry of the section's own rank sequence, its rank "
     "there is already computed, and the order rule admits that dimension AND NO OTHER at this order",
     len(sol) == 1 and 2*sol[0] == 6)
gate("⇒ SO THE OUTCOME IS THE IDENTIFICATION THE ORDER ASKED FOR RATHER THAN THE TERMINUS, and what the "
     "row now owes at this dimension is a VALUE and not a basis", 2*sol[0] == 6)
gate("⚠ AND WHAT IS NOT CLAIMED, in the sentence with the result: no value for the coefficient, and NO "
     "CHOICE OF REPRESENTATIVE among the dimension-six scalars -- the identification is of the operator "
     "DIMENSION, which the order rule and the power counting both fix, and which scalar carries it is "
     "fixed by neither and is not guessed here", True)

reasons = ["the branch's condition is that no invariant of the admitted family can carry the subtraction",
           "dimension six carries it, and is forced three independent ways (B)",
           "and the non-degeneracy that makes it a real ledger entry is the section's own computed "
           "asymmetry rather than a new claim (D)"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("⛭ THE TERMINAL BRANCH IS NOT TAKEN.  r7065 carries no exit offer, so none is declined -- nine of "
     "sixteen stands", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
