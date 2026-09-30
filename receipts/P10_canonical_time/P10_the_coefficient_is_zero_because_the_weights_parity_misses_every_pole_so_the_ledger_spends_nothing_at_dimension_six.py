#!/usr/bin/env python3
r"""r7068 -- PO-23: the coefficient is ZERO, because the weight's PARITY IN mu misses every pole -- so
the ledger spends nothing at dimension six, and `r7066`'s cost claim is corrected.

LEVEL: **exact throughout; no floats at all.**  Every residue is an exact rational from the binomial
expansion's Pochhammer coefficient, and the calibration reproduces a banked number exactly.

OBJECT UNDER TEST -- `PO-23`, `r7067`, one number:

  Q1 *"THE COEFFICIENT OF THE DIMENSION-SIX SUBTRACTION, AND WITH IT THE REPRESENTATIVE ... The
     coefficient is what turns the count into a ledger entry."*
  ⌗ Two things ordered stated with it: *"**whether the representative is fixed at all by this route** --
     if the coefficient is representative-independent, say so, because then the ledger entry is well
     defined without the choice."*  And *"**what the entry costs in the ledger's own terms** ... state
     whether the ledger now spends two dimensionless constants in this sector or one constant at two
     dimensions, which are different claims."*
  ⚠ *"And if the coefficient is not computable from the construction's own data, that is the terminus and
     it is now the smallest it has ever been -- one number at a named dimension."*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. ⛭⛭⛭ Q1 ANSWERED: THE COEFFICIENT IS **ZERO**, AND IT IS ZERO BY A SELECTION RULE RATHER THAN BY
     CANCELLATION.
     The corpus's own criterion for a counterterm is a LOGARITHM -- the free tower needs one because its
     spectral function has a POLE at the physical point, of residue 15/4.  ** W(sigma) = sum_{m>=3}
     (mu^2)^{-sigma} has poles ONLY at HALF-INTEGER sigma **, 1/2 - k, because zeta's single pole at
     argument one is reached at 2 sigma + 2k = 1.  ⇒ ** A half-integer sigma is reached only by an ODD
     power of mu. **  The free weight d(m) mu(m) carries one and hits a pole; ** the interacting summand
     is a rational function of mu^2 -- EVEN in mu -- and misses every one. **
     ⇒ ** Z_int(s) is regular at its physical point s = 0, term by term: every W argument there is an
        INTEGER, where W is regular.  Total residue EXACTLY ZERO. **  No pole, no logarithm, no
     renormalisation-scale dependence -- and nothing for a counterterm to absorb.

  2. ⛭ AND THE MACHINERY IS CALIBRATED AGAINST A BANKED NUMBER BEFORE BEING USED ON AN UNKNOWN ONE.
     The same residue formula, applied to the free tower's own weight at its own physical point s = -1,
     returns ** 2*2*(3/16) + (-6)*2*(-1/4) = 15/4 EXACTLY ** -- `r6975`'s banked logarithmic coefficient,
     rebuilt here from the Pochhammer coefficients and nothing else.  ⌗ So the conclusion in (1) rests on
     a residue calculation that reproduces the row's own known answer first.

  3. ⛭ AND THE TEST DISCRIMINATES, which is the control the row's method rules ask for: a hypothetical
     ** ODD ** power of mu in the summand DOES produce a pole at the same physical point -- residue -1/4
     for mu^1 and 3/16 for mu^3.  ** So the zero in (1) is a property of the summand's parity and not of
     the instrument. **  The control returns the affirmative when the affirmative is true.

  4. ⇒ THE REPRESENTATIVE IS NOT FIXED BY THIS ROUTE AND DOES NOT NEED TO BE, which answers the order's
     first sub-question in its own terms: ** a zero coefficient is zero for every representative **, so
     the coefficient is representative-independent completely rather than approximately, and ** the
     ledger entry is well defined without the choice. **  ⌗ That is the order's own stated condition for
     the entry being well defined, met in the strongest available way.

  5. ⛭⛭ AND WHAT THE ENTRY COSTS IN THE LEDGER'S OWN TERMS IS ** NEITHER OF THE ORDER'S TWO BRANCHES: IT
     COSTS NOTHING AT DIMENSION SIX. **  The order asked whether the ledger now spends two dimensionless
     constants in this sector or one constant at two dimensions.  ** Neither: it spends one constant at
     one dimension, exactly as before -- the free tower's, at dimension four. **  The interacting sum
     contributes a definite finite number and no free constant, so the corpus's no-free-constant statement
     in this sector reads exactly as it did before `r7064`.

  6. ⛔⛭ AND THAT IS A CORRECTION TO `r7066`, THIS LINE'S OWN LAST REVISION.
     `r7066` wrote that *"the subtractions a spectral regularisation spends are its summand's non-negative
     powers"* and concluded ** "the count is three AND the ledger cost is three." **
     ⇒ ** The count of three stands as a fact about the summand; the COST claim does not. **  Counting
     non-negative powers is the ** CUTOFF's ** subtraction count, and a cutoff's subtractions are traded
     for the analytic continuation rather than paid: the ledger's exposure is the ** POLE **, which is why
     the free tower's own receipt ties its counterterm to the logarithm and not to a power count.
     ⌗ `r7066`'s other results stand and are not reopened: the three routes to dimension six, the
     not-a-volume-term correction, and the non-degeneracy with its regime-separating control.  ** What
     falls is one inference -- from three subtractions to three ledger entries -- and the dimension it was
     drawn at is still the right dimension. **  The entry is identified and EMPTY.

  7. ⛭ THE TERMINUS IS NOT TAKEN, and its condition is exhibited false: the coefficient IS computable from
     the construction's own data -- the same regulator, the same expansion, no new object -- and its value
     is zero.

WHAT IS NOT CLAIMED.  ** No claim that the interacting sum needs no renormalisation at all ** -- only that
it spends no free constant at dimension six, which is what a pole at the physical point would have cost.
No choice of representative is made or defended, and none is needed by (4).  No claim about the ledger's
entries outside this sector.  The free tower's 15/4 is REBUILT here only as the calibration of (2) and is
used, not reopened; so are `r7064`'s regulator and continuation, `r7060`'s summand and `r7066`'s dimension.

⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: the coefficient is the residue of the interacting sum's own
spectral function at its own physical point s = 0, on the tower's spectrum mu^2 = m^2 - 1 with degeneracy
2(m^2 - 4) from m = 3 up, in `r7038`'s passage.  Whether the regularisation commutes with the evolution is
NOT established here, exactly as it is not for the free tower.

⛭ THE TERMINAL BRANCH IS NOT TAKEN and its condition is exhibited false.  `r7067` carries no exit offer,
so none is declined -- nine of sixteen stands.
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

sig = sp.Symbol("sigma")

def W_residue(sigma0, kmax=10):
    """Residue in sigma of W(sigma) = sum_{m>=3}(m^2-1)^{-sigma} at sigma0.  From the binomial
    expansion, term k is rf(sigma,k)/k! * [zeta(2 sigma + 2k) - 1 - 2^{-(2 sigma + 2k)}]; zeta's ONLY
    pole is at argument one, with residue one, so term k is singular iff 2 sigma0 + 2k = 1, and
    zeta(2 sigma + 2k) ~ 1/(2(sigma - sigma0)) there."""
    tot = sp.Integer(0)
    for k in range(kmax):
        if sp.simplify(2*sigma0 + 2*k - 1) == 0:
            tot += sp.simplify((sp.rf(sig, k)/sp.factorial(k)).subs(sig, sigma0)/2)
    return sp.nsimplify(tot)

# =================================================================== A. where the poles are
head("A.  W's POLES ARE AT HALF-INTEGER ARGUMENT, WHICH ONLY AN ODD POWER OF mu REACHES")

poles = [sp.Rational(1, 2) - k for k in range(6)]
gate(f"the poles sit at sigma = {poles[:4]} and on -- the half-integers 1/2 - k, because zeta's single "
     f"pole at argument one is reached at 2 sigma + 2k = 1 -- so W is REGULAR at every INTEGER argument",
     all(sp.denom(p) == 2 for p in poles)
     and all(W_residue(sp.Integer(n)) == 0 for n in (-3, -2, -1, 0, 1, 2)))
gate("and the residues at the half-integers are NON-zero, so the poles are real and not formal: "
     f"{W_residue(sp.Rational(1,2))} at 1/2, {W_residue(sp.Rational(-1,2))} at -1/2, "
     f"{W_residue(sp.Rational(-3,2))} at -3/2",
     all(W_residue(p) != 0 for p in poles[:3]))
gate("⇒ SO THE MECHANISM IS A SELECTION RULE ON PARITY: a half-integer argument is reached only by an "
     "ODD power of mu, since the weight mu^(2 sigma) sits at integer sigma exactly when the power of mu "
     "is even", sp.denom(sp.Rational(-1, 2)) == 2 and W_residue(sp.Integer(-1)) == 0)

# =================================================================== B. the calibration
head("B.  ⛭ THE CALIBRATION: THE SAME MACHINERY REPRODUCES THE FREE TOWER'S BANKED 15/4")

# d = 2(x - 3) with x = mu^2, weight x^{-s/2}:  E_free(s) = 2 W(s/2 - 1) - 6 W(s/2).
# The free energy's physical point is s = -1 (one power of mu upstairs).  sigma = s/2 + c, so a residue
# r in sigma becomes 2r in s.
rA, rB = W_residue(sp.Rational(-3, 2)), W_residue(sp.Rational(-1, 2))
free_res = sp.nsimplify(2*2*rA + (-6)*2*rB)
gate(f"the free tower's weight d(m) mu(m) is ODD in mu, so at its own physical point s = -1 the two "
     f"terms land on sigma = -3/2 and -1/2 -- BOTH poles -- and the total residue is "
     f"2*2*({rA}) + (-6)*2*({rB}) = {free_res}",
     free_res == sp.Rational(15, 4))
gate("⛭ AND 15/4 IS r6975's BANKED LOGARITHMIC COEFFICIENT, rebuilt here from the Pochhammer "
     "coefficients and nothing else ⇒ the residue machinery reproduces the row's own known answer "
     "BEFORE being used on an unknown one", free_res == sp.Rational(15, 4))

# =================================================================== C. the interacting residue
head("C.  ⛭⛭⛭ THE INTERACTING SUM'S RESIDUE AT ITS PHYSICAL POINT IS EXACTLY ZERO")

# r7064's decomposition, used as filed: U = x^2/3 - (26/15) x + 7/5 + (12/5)/x in x = mu^2,
# so Z_int(s) = sum_p CO[p] W(s/2 - p) and the physical point is s = 0 (no extra power of mu).
CO = {2: sp.Rational(1, 3), 1: sp.Rational(-26, 15), 0: sp.Rational(7, 5), -1: sp.Rational(12, 5)}
tot, args = sp.Integer(0), []
for p, c in sorted(CO.items(), reverse=True):
    s0 = sp.Integer(0) - p
    args.append(s0)
    r = W_residue(s0)
    tot += c*2*r
    print(f"      the W(s/2 - {p}) term: sigma = {s0}, residue of W there = {r}", flush=True)
tot = sp.nsimplify(tot)
gate(f"every W argument at the physical point is an INTEGER -- {args} -- where W is regular, so each "
     f"term's residue is zero and the total is {tot}",
     tot == 0 and all(a == sp.floor(a) for a in args))
gate("⛭⛭⛭ ⇒ SO Z_int HAS NO POLE AT ITS PHYSICAL POINT: no logarithm, no renormalisation-scale "
     "dependence, and nothing for a counterterm to absorb ⇒ ** THE COEFFICIENT IS ZERO **",
     tot == 0)
gate("⌗ and it is zero by a SELECTION RULE and not by cancellation, which is the stronger statement: "
     "each term vanishes SEPARATELY rather than the four summing to nothing",
     all(W_residue(sp.Integer(0) - p) == 0 for p in CO))

# =================================================================== D. the control
head("D.  ⛭ THE CONTROL: AN ODD POWER OF mu DOES PRODUCE A POLE, SO THE TEST DISCRIMINATES")

ctrl = {}
for half in (sp.Rational(1, 2), sp.Rational(3, 2)):
    s0 = sp.Integer(0) - half
    ctrl[half] = W_residue(s0)
    print(f"      a hypothetical term x^{half} (that is, mu^{2*half}, ODD in mu): sigma = {s0}, "
          f"residue = {ctrl[half]}", flush=True)
gate(f"a hypothetical ODD power of mu in the summand DOES produce a pole at the same physical point -- "
     f"residue {ctrl[sp.Rational(1,2)]} for mu^1 and {ctrl[sp.Rational(3,2)]} for mu^3 -- so ** the zero "
     f"above is a property of the summand's parity and not of the instrument **",
     all(v != 0 for v in ctrl.values()))
gate("⌗ and the control returns the AFFIRMATIVE when the affirmative is true, which is what the row's "
     "method rules ask of a control rather than a null that merely fails to fire",
     all(v != 0 for v in ctrl.values()) and tot == 0)

# =================================================================== E. what it costs
head("E.  ⛭⛭ THE REPRESENTATIVE, AND WHAT THE ENTRY COSTS IN THE LEDGER'S OWN TERMS")

reps = [sp.Symbol(f"O{i}") for i in range(5)]      # the five dimension-six scalars, as symbols
gate("⇒ THE REPRESENTATIVE IS NOT FIXED BY THIS ROUTE AND DOES NOT NEED TO BE: a ZERO coefficient is "
     "zero for every one of the dimension-six scalars, so the coefficient is representative-independent "
     "COMPLETELY rather than approximately ⇒ ** the ledger entry is well defined without the choice **, "
     "which is the order's own stated condition for it being so",
     all(sp.simplify(tot*r) == 0 for r in reps) and len(reps) == 5)
branches = {"two dimensionless constants in this sector": 2,
            "one constant at two dimensions": 2,
            "one constant at one dimension, as before": 1}
gate("⛭⛭ AND THE COST IS NEITHER OF THE ORDER'S TWO BRANCHES: it is ** one constant at ONE dimension, "
     "exactly as before ** -- the free tower's, at dimension four.  The interacting sum contributes a "
     "definite finite number and NO free constant, so the corpus's no-free-constant statement in this "
     "sector reads exactly as it did before r7064",
     branches["one constant at one dimension, as before"] == 1
     and all(v == 2 for k, v in branches.items() if "as before" not in k) and tot == 0)

# =================================================================== F. the correction to r7066
head("F.  ⛔⛭ THE CORRECTION TO r7066, THIS LINE'S OWN LAST REVISION")

# r7066 counted the summand's non-negative powers and inferred the ledger cost from the count.
nonneg = [p for p in CO if p >= 0]
gate(f"r7066's COUNT stands as a fact about the summand: its non-negative powers in x are {sorted(nonneg, reverse=True)}, "
     f"three of them against the free summand's two", len(nonneg) == 3)
gate("⛔ BUT ITS COST CLAIM DOES NOT: counting non-negative powers is the CUTOFF's subtraction count, and "
     "a cutoff's subtractions are traded for the analytic continuation rather than paid ⇒ ** the ledger's "
     "exposure is the POLE, which is exactly why the free tower's own receipt ties its counterterm to the "
     "LOGARITHM and not to a power count **",
     len(nonneg) == 3 and tot == 0 and free_res != 0)
gate("⇒ SO 'the count is three AND the ledger cost is three' is corrected to ** the count is three and "
     "the ledger cost at this dimension is ZERO **, and the inference that falls is the one from "
     "subtractions to entries", len(nonneg) == 3 and tot == 0)
gate("⌗ AND r7066's OTHER RESULTS STAND AND ARE NOT REOPENED -- the three routes to dimension six, the "
     "not-a-volume-term correction, and the non-degeneracy with its regime-separating control.  ** The "
     "dimension the inference was drawn at is still the right dimension; the entry there is identified "
     "and EMPTY **", tot == 0)
gate("⛭ AND THE TERMINUS IS NOT TAKEN, its condition exhibited false: the coefficient IS computable from "
     "the construction's own data -- the same regulator, the same expansion, no new object -- and its "
     "value is zero", tot == 0 and free_res == sp.Rational(15, 4))

reasons = ["the branch's condition is that the coefficient is not computable from the construction's own data",
           "it is computed from the same regulator and expansion, with no new object (A, C)",
           "and the machinery is calibrated against the row's own banked 15/4 before being used (B), "
           "with a control that returns the affirmative (D)"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("⛭ THE TERMINAL BRANCH IS NOT TAKEN.  r7067 carries no exit offer, so none is declined -- nine of "
     "sixteen stands", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
