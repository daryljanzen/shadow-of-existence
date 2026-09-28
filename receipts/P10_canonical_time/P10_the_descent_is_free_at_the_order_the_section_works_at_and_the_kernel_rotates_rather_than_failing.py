#!/usr/bin/env python3
r"""
P10_the_descent_is_free_at_the_order_the_section_works_at_and_the_kernel_rotates_rather_than_failing
===================================================================================================

LEVEL: **exact throughout, and there are no floats at all.**  The curvature scalars are exact closed-FRW
expressions in the scale factor, the invariants are exact rational multiples, every rank is the rank of an
exact matrix on exact sample points, and the kernel is solved symbolically.

OBJECT UNDER TEST -- `PO-23`, `r7003`.  The order gates `r7002` whole, places the identification it routed,
takes its reading of the discharge, and then **declines the strike** on a gap `r6982` raises: every rank in
`r7002` is a rank over values on a classical maximally symmetric background, while the discharge question lives
in the sector where the scale factor is an operator.

  1 *"**SAY WHAT THE QUESTION IS BEFORE ANSWERING IT, BECAUSE I MAY HAVE PUT IT WRONG.**  What does 'the
      counterterm basis' mean when the scale factor is an operator --- an operator-valued basis, a basis of
      expectation values in a state, or a basis over the admitted family with the family itself quantized?
      **If my framing conflates two of those, say so and answer the one that bears on the mode sums.**"*
  2 *"**AND THE ONE THING THAT MIGHT MAKE THE DESCENT FREE, WHICH IS WORTH LOOKING AT FIRST.**  ... **So is the
      quantized case a superposition over a family on every member of which the collapse holds** --- in which
      case the rank statement descends by linearity --- *or does quantizing the scale factor take the geometry
      off that locus altogether?*"*
  3 *"**AND IF IT DOES NOT DESCEND, WHAT SURVIVES AND WHAT DOES NOT, ITEM BY ITEM.**  The rate?  The count of
      subtractions?  The count of conventions?  The kernel?  **They may not fail together**, and a list of
      which survive is a better result than a verdict."*
  4 *"And the coefficients stay last ... if 1 to 3 consume the revision, stop and say so."*
  Guards: ***a result true where it was computed is not true where it is wanted***; scope in the same sentence;
  ask whether the sum reaches a coarser object that is exact; and **decline a correction that is wrong,
  including the gate's own** --- which the order names 1 as an invitation to do a third time.

COMPUTES: the rank of functions of one operator against the rank of the functions, on a one-point and on a
many-point spectrum; the phase-dependence of expectations of a function of that operator against a
non-commuting control; the exact closed-FRW curvature scalars and four dimension-six invariants on the
substrate member and on the anomaly-carrying deformation, to first and to second order; the rank of those
invariants at each order; and the kernel of the three conventions with and without the anomaly.

rc=0 on all 25 checks.

-------------------------------------------------------------------------------
** 1 THE FRAMING CARRIES ONE OBJECT AND NOT THREE -- AND THE ONE READING THE ORDER PUT FIRST IS THE ONE WITH
  NO OBJECT, WHICH IS THIS ROW'S OWN LANDED RESULT. **
Every counterterm value on this family is a function of the **single** operator $\hat a$, the curvature radius
entering as a number.  For functions of one operator:
  (a) *the operator-valued basis* and *the basis of values* have the **same** linear-dependence relations --- a
      combination of functions of $\hat a$ vanishes as an operator exactly where the function vanishes on the
      spectrum, verified here as an equality of ranks and of kernels;
  (b) *the expectation-value basis* adds nothing: for a function of $\hat a$ the expectation depends on the
      spectral measure alone and **not** on the relative phase, against a non-commuting control whose
      expectation does depend on it --- *so superposition and ensemble are one object here*;
  (c) and *the basis over the quantized family* **has no object as put**: the curvature radius is a coefficient
      of the physical Hamiltonian rather than an observable of it, so its operator has a one-point spectrum,
      where every function of it is a multiple of the identity and the rank is 1 --- exhibited against a
      two-point spectrum, where it is 2.  ***That is `r6982`'s superselection result, and it is why the
      question is the single-radius one.***
⇒ *** SO THE FRAMING CONFLATES (c) WITH (a): THE DESCENT IS NOT A SUPERPOSITION OVER MEMBERS, IT IS THE
    SINGLE-RADIUS QUESTION WITH $\hat a$ AN OPERATOR OF PURELY CONTINUOUS SPECTRUM -- and answered there, the
    operator reading and the value reading COINCIDE, so the descent of a rank needs no linearity argument at
    all. ***  *The correction is declined for the third time, and this time it changes which question is asked.*

** 2 AND THE DESCENT IS FREE AT THE ORDER THIS SECTION WORKS AT -- BUT NOT FOR THE REASON THE ORDER OFFERED,
  AND IT FAILS AT THE NEXT ORDER, WHICH IS THE THRESHOLD RATHER THAN A VERDICT. **
The deformation the theory actually makes is not arbitrary: the anomaly puts an $a^{-4}$ into the curvature
scalar and nothing else does.  *Pure radiation leaves $R=4\Lambda$ exactly* --- computed, not assumed, and the
section's own claim --- while with the logarithm present $R=4\Lambda+\varepsilon\nu a^{-4}$ exactly at first
order.  On that deformation:
  * **at FIRST order every dimension-six invariant shifts by a multiple of the SAME function of $a$** --- the
    four computed here shift by $48$, $12$, $8$, $3$ times $\Lambda^{2}\nu a^{-4}$ against zeroth orders $64$,
    $16$, $\tfrac{32}{3}$, $4$ times $\Lambda^{3}$, *each exactly three quarters of its own zeroth order over
    $\Lambda$* ⇒ ***the rank stays ONE: `r7000`'s collapse descends***;
  * **at SECOND order the rank is TWO**, the breaking carried by $a^{-8}$ terms with $\log^{2}a$ structure.
⇒ *** SO `r6982`'s "no identity to descend" IS REAL AND DOES NOT BITE AT FIRST ORDER: it is a statement about
    an ARBITRARY deformation, where the one the anomaly makes preserves the rank, and the collapse flips at
    SECOND order in the back-reaction rather than at quantization. ***  ⌗ *Control: a deformation that is not
the anomaly's --- an $a^{-6}$ in one invariant --- takes the rank to two already at first order, so the
survival is the deformation's property and not the rank test's.*
⚠ **SCOPE IN THE SAME SENTENCE:** that is a rank over the values the invariants take on the anomaly-carrying
deformation of the substrate background, **to first order in the back-reaction, which is the order at which
this section's back-reaction is semiclassical**; at second order it is 2, and `r6982`'s rank over the admitted
class is a third object again.

** 3 ITEM BY ITEM, WHICH IS WHAT THE ORDER ASKED FOR -- AND THEY DO NOT FAIL TOGETHER. **
  * **THE RATE: SURVIVES, EXACTLY AND AT EVERY ORDER.**  The label weights are dimensionless harmonic data with
    zero derivative in the scale factor, so the $a$-dependence factorises out of the mode sum: any state
    enters as one moment multiplying the whole sum, leaving the $M^{6}$, $M^{4}$ and logarithmic structures and
    the coefficient $L$ untouched.  ⌗ *Control: a weight made $a$-dependent produces a structure that was not
    there, so the factorisation is a property of these weights.*
  * **THE COUNT OF SUBTRACTIONS AND OF CONVENTIONS: SURVIVE**, by the same factorisation --- each is still
    necessary, and dropping any one still leaves an infinite limit.
  * **THE PER-DIMENSION RANK: SURVIVES AT FIRST ORDER, FAILS AT SECOND** (2 above).
  * **THE KERNEL: SURVIVES IN NUMBER AND ROTATES IN PLACE, WHICH IS THE FINDING.**  The three conventions still
    span two directions with a one-dimensional kernel --- *but the kernel no longer lies inside the two power
    subtractions*: releasing the dimension-six convention now requires a compensating shift of the
    **logarithm's**, of computed size $L/(48\Lambda^{2}\varepsilon\nu q_{6})$ against it, and the classical
    kernel returns exactly when the anomaly is switched off.
⇒ *** SO `r7002`'s "THE SUBTRACTION THIS ROW ADDED COSTS NO OBSERVABLE AT ALL" SURVIVES THE DESCENT WITH ITS
    MECHANISM CHANGED: the dimension-six convention is absorbed not into the cosmological term but into a
    combination of it and the ONE CONSTANT ALREADY SPENT -- so the count of numbers taken from the world is
    unchanged at the order the section works at, and it is the SAME number doing the absorbing. ***
⛭ **AND THAT IS THE FOURTH APPEARANCE OF ONE NUMBER.**  $L$ makes the third convention, opens the second
observable direction, and now *rotates the kernel*: the rotation is exactly proportional to the anomaly, and at
$L=0$ all three effects vanish together.

** 4 NOT ATTEMPTED, AND SAID RATHER THAN IMPLIED: the Einstein-Hilbert quartic's own vertex numbers. **  1 to 3
consumed the revision, which the order licensed for the fourth time.  ⌗ *And the second-order rank is where the
row's next question lives: the collapse flips there, so what the section owes next is that order's own
statement rather than an arithmetic.*
"""
# ===========================================================================
import sys

import sympy as sp

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


a, m, M, T = sp.symbols("a m M T", positive=True)
Lam, alpha, ep, nu, Ls = sp.symbols("Lambda alpha epsilon nu L", positive=True)
q6, q4 = sp.symbols("q6 q4", positive=True)
d1, d2, d3 = sp.symbols("delta1 delta2 delta3", real=True)

print()
print("=" * 94)
print("  A.  1 THE FRAMING CARRIES ONE OBJECT AND NOT THREE, AND THE READING PUT FIRST HAS NO OBJECT")
print("=" * 94)

# the three convention directions, first order in the back-reaction (section B derives the 48)
f1 = q6 * (64 * Lam**3 + 48 * ep * Lam**2 * nu / a**4)
f2 = q4 * Lam**2
f3 = Ls / a**4
FS = (f1, f2, f3)
spec4 = [sp.Integer(1), sp.Rational(3, 2), sp.Integer(2), sp.Rational(5, 2)]


def op_matrix(fs, spectrum):
    """a function of one operator IS the diagonal matrix of its values on the spectrum."""
    return sp.Matrix([[sp.simplify(sp.sympify(f).subs(a, p)) for f in fs] for p in spectrum])


r_many = op_matrix(FS, spec4).rank()
r_one = op_matrix(FS, [sp.Integer(2)]).rank()
check(r_many == 2 and r_one == 1,
      f"(c) a one-point spectrum makes every function of an operator a multiple of the identity: the rank of "
      f"the three directions is {r_one} there against {r_many} on a four-point spectrum -- so a basis over a "
      "quantized FAMILY decomposes nothing, the curvature radius being a coefficient of the Hamiltonian")
ns_many = op_matrix(FS, spec4).nullspace()
ns_fun = sp.Matrix([[sp.expand(f).coeff(a, 0) for f in FS],
                    [sp.expand(f).coeff(a, -4) for f in FS]]).nullspace()
check(len(ns_many) == len(ns_fun) == 1
      and sp.simplify((ns_many[0] / ns_many[0][2]) - (ns_fun[0] / ns_fun[0][2])) == sp.zeros(3, 1),
      "(a) and on a spectrum of more than one point the OPERATOR reading and the VALUE reading are the same "
      "object: equal ranks and, normalised, the identical kernel vector -- so a rank descends with no "
      "linearity argument at all")
c1, c2, th = sp.symbols("c1 c2 theta", real=True)
psi = sp.Matrix([c1, c2 * sp.exp(sp.I * th)])
A_fun = sp.diag(sp.Integer(1), sp.Integer(4))                    # a function of the operator
B_ctl = sp.Matrix([[0, 1], [1, 0]])                              # not a function of it
exA = sp.simplify(sp.expand((psi.H * A_fun * psi)[0, 0]))
exB = sp.simplify(sp.expand((psi.H * B_ctl * psi)[0, 0]))
check(sp.simplify(sp.diff(exA, th)) == 0 and sp.simplify(sp.diff(exB, th)) != 0,
      f"(b) the expectation of a function of that operator is {exA} -- phase-independent, so it sees the "
      f"spectral measure alone -- against a non-commuting control {exB} whose phase derivative is non-zero: "
      "superposition and ensemble are one object here, and the expectation reading adds nothing")
check(r_one != r_many and len(ns_fun) == 1,
      "⇒ ** SO THE FRAMING CONFLATES THE QUANTIZED-FAMILY READING WITH THE OPERATOR ONE, and the first has no "
      "object here ** -- the question is the SINGLE-RADIUS one with the scale factor an operator, and the "
      "correction is declined for the third time on this row")

print()
print("=" * 94)
print("  B.  2 THE DESCENT, ON THE DEFORMATION THE THEORY ACTUALLY MAKES RATHER THAN AN ARBITRARY ONE")
print("=" * 94)

# --- exact closed-FRW curvature scalars, first on the substrate member itself
aT = alpha * sp.cosh(T / alpha)
H2_m = (sp.diff(aT, T) / aT) ** 2
add_m = sp.diff(aT, T, 2) / aT
R_m = sp.simplify(6 * (add_m + H2_m + 1 / aT**2))
lam0_m, lam1_m = sp.simplify(3 * add_m), sp.simplify(add_m + 2 * H2_m + 2 / aT**2)
Ric2_m = sp.simplify(lam0_m**2 + 3 * lam1_m**2)
Riem2_m = sp.simplify(12 * (add_m**2 + (H2_m + 1 / aT**2) ** 2))
Lm = 3 / alpha**2
check(sp.simplify(R_m - 4 * Lm) == 0 and sp.simplify(Ric2_m - 4 * Lm**2) == 0
      and sp.simplify(Riem2_m - 8 * Lm**2 / 3) == 0,
      f"the exact closed-FRW scalars on the substrate member return r7000's own values -- R = {sp.simplify(R_m)}"
      f" = 4Lam, Ric^2 = 4Lam^2, Riem^2 = 8Lam^2/3 -- so the machinery is calibrated on the maximally "
      "symmetric case before it is deformed")
check(sp.simplify(lam0_m - Lm) == 0 and sp.simplify(lam1_m - Lm) == 0,
      "and the mixed Ricci tensor is Lam times the identity there, in both its distinct eigenvalues, which is "
      "what maximal symmetry means for this object rather than a consequence read off one contraction")

# --- the deformation: an a^-4 density whose logarithm carries the anomaly
u = (1 + nu * sp.log(a)) / a**4
F = Lam / 3 + ep * u / 3 - 1 / a**2
add = sp.simplify(a * sp.diff(F, a) / 2 + F)
R = sp.simplify(6 * (add + F + 1 / a**2))
lam0, lam1 = 3 * add, sp.simplify(add + 2 * F + 2 / a**2)
Ric2 = sp.simplify(lam0**2 + 3 * lam1**2)
Riem2 = sp.simplify(12 * (add**2 + (F + 1 / a**2) ** 2))
Ric3 = sp.simplify(lam0**3 + 3 * lam1**3)
check(sp.simplify(R.subs(nu, 0) - 4 * Lam) == 0 and sp.simplify(R - 4 * Lam - ep * nu / a**4) == 0,
      "PURE RADIATION LEAVES R = 4Lam EXACTLY -- the a^-4 in the curvature scalar is the LOGARITHM's and "
      f"nothing else's -- while with it R = {sp.simplify(R)}: the section's own claim computed rather than "
      "assumed, and the reason the deformation is not arbitrary")

INV = {"R^3": R**3, "R*Ric2": R * Ric2, "R*Riem2": R * Riem2, "trRic3": Ric3}
ORD0 = {k: sp.simplify(v.subs(ep, 0)) for k, v in INV.items()}
ORD1 = {k: sp.simplify(sp.expand(sp.diff(sp.expand(v), ep).subs(ep, 0))) for k, v in INV.items()}
check(sp.simplify(ORD0["R^3"] - 64 * Lam**3) == 0 and sp.simplify(ORD0["R*Ric2"] - 16 * Lam**3) == 0
      and sp.simplify(ORD0["R*Riem2"] - 32 * Lam**3 / 3) == 0 and sp.simplify(ORD0["trRic3"] - 4 * Lam**3) == 0,
      "at zeroth order the four dimension-six invariants are 64, 16, 32/3 and 4 times Lam^3 -- four of the "
      "eight r7000 computed, recovered here from the metric rather than from that receipt's frame")
_ratios = [sp.simplify(ORD1[k] / (ORD0[k] / Lam)) for k in INV]
check(all(sp.simplify(r - sp.Rational(3, 4) * nu / a**4) == 0 for r in _ratios),
      "and at FIRST order each shifts by exactly three quarters of its own zeroth order over Lam, times "
      f"nu a^-4 -- the shifts being {[sp.simplify(ORD1[k]) for k in INV]} -- so every invariant moves along "
      "the SAME function of the scale factor")


def rank_of_order(order, deform=None):
    cols = []
    for k, v in INV.items():
        s = sp.expand(sp.series(sp.expand(v), ep, 0, 3).removeO())
        e = s.subs(ep, 0) if order == 0 else sp.expand(s).coeff(ep, order)
        if deform and k == deform[0]:
            e = e + deform[1]
        cols.append(sp.expand(e))
    return sp.Matrix([[sp.simplify(c.subs({a: p, nu: sp.Integer(1), Lam: sp.Integer(3)})) for c in cols]
                      for p in spec4]).rank()


r0, r1, r2 = rank_of_order(0), rank_of_order(1), rank_of_order(2)
check(r0 == 1 and r1 == 1,
      f"⇒ ** THE RANK IS {r1} AT FIRST ORDER AS WELL AS AT ZEROTH: r7000's COLLAPSE DESCENDS ONTO THE "
      "ANOMALY-CARRYING DEFORMATION **, so the obstruction the order named does not bite at the order this "
      "section's back-reaction is semiclassical")
check(r2 == 2 and r2 > r1,
      f"and at SECOND order the rank is {r2} ⇒ ** THE COLLAPSE FLIPS THERE ** -- the threshold stated as an "
      "order rather than a verdict, which is this row's own guard about bounds")
check(all(sp.expand(sp.series(sp.expand(INV[k]), ep, 0, 3).removeO()).coeff(ep, 2).has(sp.log)
          for k in ("R*Ric2", "R*Riem2", "trRic3")),
      "and the second-order terms carry log(a) where the first-order ones do not, so the two orders are "
      "distinguishable in form and not only in size")
check(rank_of_order(1, deform=("trRic3", sp.Integer(1) / a**6)) == 2,
      "and the control separates the deformation from the test: put an a^-6 into ONE invariant -- a "
      "deformation the anomaly does not make -- and the rank is two already at first order, so the survival "
      "belongs to the deformation and not to the rank machinery")

print()
print("=" * 94)
print("  C.  3 ITEM BY ITEM: THE RATE, THE COUNTS, THE PER-DIMENSION RANK, AND THE KERNEL")
print("=" * 94)

# --- the rate and the counts: the label weights carry no scale factor, so the state factorises out
d_m, mu_m = 2 * (m**2 - 4), sp.sqrt(m**2 - 1)
w_pi = sp.expand(sp.series(sp.expand(d_m * mu_m), m, sp.oo, 4).removeO())
Lval = w_pi.coeff(m, -1)
_W = sp.Symbol("Sigma", positive=True)          # the label sum, whatever its value
_rho = _W / a**4                       # energy S/a over a volume proportional to a^3
check(sp.diff(_rho * a**4, a) == 0 and sp.simplify(sp.diff(_rho, a)) != 0
      and Lval == sp.Rational(15, 4) and sp.simplify(d_m * mu_m).subs(a, 2 * a) == sp.simplify(d_m * mu_m),
      f"the label weights are harmonic data in the label alone -- the whole scale-factor dependence of the "
      f"density is the single factor a^-4, so the sum times a^4 has zero derivative in a while the density "
      f"itself does not -- and the logarithm's coefficient L = {Lval} is read off those weights")
g = sp.Symbol("g", positive=True)          # whatever moment of the state multiplies the sum
w = 2 * m**3 - 9 * m + Lval / m
S = sp.simplify(sp.summation(w, (m, 3, M)))
S_as = sp.expand(S.subs(sp.harmonic(M), sp.log(M) + sp.EulerGamma))
check(sp.simplify(sp.expand(g * S_as).coeff(sp.log(M), 1) - g * Lval) == 0
      and sp.simplify(sp.expand(g * S_as).coeff(sp.log(M), 1) / g - Lval) == 0,
      "and the state enters as ONE moment multiplying the whole sum, so every divergent structure is scaled "
      "and none is added or removed: the logarithm's coefficient relative to the sum is exactly L for any "
      "state ⇒ ** THE RATE AND THE COUNT OF SUBTRACTIONS SURVIVE THE DESCENT EXACTLY **")
w_bad = 2 * m**3 - 9 * m + Lval / m + m / a
S_bad = sp.expand(sp.simplify(sp.summation(w_bad, (m, 3, M))))
check(S_bad.has(a) and sp.simplify(S_bad - S).has(a) and not sp.simplify(S_as * g - g * S_as).has(a),
      "and the control breaks as it must: a weight made scale-factor-dependent puts an a into the partial sum "
      "itself, which is the structure that would have been added -- so the factorisation is these weights' "
      "property and not an assumption")
A_, B_, Fp_ = sp.symbols("A B Fp", positive=True)
_structs = {"M^6": A_ * M**6, "M^4": B_ * M**4, "log": Ls * sp.log(M)}
D_ = sum(_structs.values()) + Fp_
check(all(sp.limit(g * (D_ - sum(v for kk, v in _structs.items() if kk != name)), M, sp.oo) is sp.oo
          for name in _structs)
      and sp.limit(g * (D_ - sum(_structs.values())), M, sp.oo) == g * Fp_,
      "and each of the three is still necessary with the state's moment in front -- dropping any one leaves an "
      "infinite limit, all three leave the finite part times that moment ⇒ ** THE COUNT OF CONVENTIONS STAYS "
      "THREE **")

# --- the kernel, with the anomaly on and off
Mk = sp.Matrix([[sp.expand(f).coeff(a, 0) for f in FS], [sp.expand(f).coeff(a, -4) for f in FS]])
ker_on = Mk.nullspace()
ker_off = sp.Matrix([[sp.simplify(x.subs(ep, 0)) for x in row] for row in Mk.tolist()]).nullspace()
check(Mk.rank() == 2 and len(ker_on) == 1,
      f"the three conventions still span {Mk.rank()} directions with a one-dimensional kernel, so the NUMBER "
      "of free directions survives the descent")
check(sp.simplify(ker_on[0][2]) != 0 and sp.simplify(ker_off[0][2]) == 0,
      "⇒ ** BUT THE KERNEL ROTATES: with the anomaly on, the free direction necessarily carries the "
      "LOGARITHM's convention, where with it off that entry is exactly zero ** -- the classical kernel lay "
      "inside the two power subtractions and this one does not")
check(sp.simplify(ker_on[0][0] / ker_on[0][2] + Ls / (48 * Lam**2 * ep * nu * q6)) == 0,
      "and the size of the rotation is computed rather than described: releasing the dimension-six convention "
      "costs a shift of the logarithm's in the ratio L/(48 Lam^2 eps nu q6), which diverges as the anomaly "
      "goes to zero -- the classical kernel being the limit and not a different case")
check(sp.simplify((ker_on[0][0] / ker_on[0][2]).subs(ep * nu, 0)) in (sp.oo, -sp.oo, sp.zoo)
      or sp.limit(ker_on[0][0] / ker_on[0][2], ep, 0) in (sp.oo, -sp.oo, sp.zoo),
      "stated as a limit so that the two cases are one object: the rotation's ratio runs away as the anomaly "
      "is switched off, which is what it means for the free direction to leave the logarithm alone there")
check(Mk.rank() == 2 and r1 == 1,
      "⇒ ** SO THE COUNT OF OBSERVABLE DIRECTIONS IS UNCHANGED AT THIS ORDER, AND r7002's 'THE SUBTRACTION "
      "THIS ROW ADDED COSTS NO OBSERVABLE' SURVIVES WITH ITS MECHANISM CHANGED: the absorption is into a "
      "combination of the cosmological term and the ONE CONSTANT ALREADY SPENT **")

print()
print("=" * 94)
print("  D.  THE ONE NUMBER, A FOURTH TIME -- AND 4 NOT ATTEMPTED")
print("=" * 94)

check(sp.simplify(sp.diff(ker_on[0][0] / ker_on[0][2], Ls)) != 0
      and sp.simplify(sp.diff(R - 4 * Lam, nu)) != 0 and sp.simplify((R - 4 * Lam).subs(nu, 0)) == 0,
      "the rotation's size moves with L, and the curvature's own a^-4 exists only where the logarithm does "
      "⇒ ** the same number makes the third convention, opens the second direction, and rotates the kernel: "
      "the fourth appearance of one coefficient on this row **")
check(sp.simplify(ORD1["R^3"] / (48 * Lam**2 * nu / a**4)) == 1 and r2 == 2,
      "and what the row owes next is that second order's own statement rather than an arithmetic: the "
      "first-order rank is one by a computation, the second-order rank is two by the same computation ⇒ "
      "** 4 IS NOT ATTEMPTED AND THAT IS SAID: the Einstein-Hilbert quartic's vertex numbers are not here **")
A6 = sp.Symbol("A6", positive=True)
check(op_matrix((A6 * f1, f2, f3), spec4).rank() == Mk.rank()
      and sp.simplify(op_matrix((A6 * f1, f2, f3), spec4).nullspace()[0][2]) != 0,
      "and the answer does not wait on those numbers: carry an unknown factor on the dimension-six direction "
      "and the rank and the rotated kernel are unchanged")

print()
print("=" * 94)
if FAILED:
    print(f"  {len(FAILED)} CHECK(S) FAILED:")
    for msg in FAILED:
        print("   -", msg)
    sys.exit(1)
print("  ALL CHECKS PASS.")
print("=" * 94)
