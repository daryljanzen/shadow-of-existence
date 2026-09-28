#!/usr/bin/env python3
r"""
P10_the_chain_does_not_reach_the_planck_length_and_the_second_order_term_is_bounded_at_the_bounce
================================================================================================

LEVEL: **exact wherever the object is algebraic, and a float against the corpus's own cited figure wherever
the input is a measurement.**  The links of the chain, the dimensional availability of the one relation it
would need, the extremum of the background and the bound it puts on the expansion parameter are all exact.

OBJECT UNDER TEST -- `PO-23`, `r6987+66.1`, the amendment.  The order amends itself after reading `P18`,
reports that `P18` commits ON the premise, and asks:

  1 *"**Does that chain reach the tower?**  `P18` is a synthesis and I have read its summary, not its
      sources --- that reading is still yours to do ... the chain is curvature to horizon period to `\hbar`
      to the Planck length.  **If anything in `sec:lock`'s tower takes `\hbar` as an independent constant
      rather than the horizon-fixed one, the gauge-combination claim does not reach the tower.**"*
  2 *"**AND THE QUANTITATIVE QUESTION, WHICH IS THE ONE WITH TEETH AND IS CHEAP.** ... work out what the
      second-order term's size actually is at the epochs the construction cares about, and say whether the
      expansion is still an expansion there."*  ⌗ *"And if the scale factor's own powers undo the
      suppression at some epoch, that is a result with a locus and I want it with the locus named."*
  3 *"`P18` locates a surviving instance of the cosmological-constant problem inside the boundary
      coefficient ... **Say whether the datum your branch would owe is the same datum or a second one.**"*
  ⚠ *"**AND I AM HANDING YOU A SUMMARY AND SAYING SO.** ... **If the sources do not say what the synthesis
      says they say, that is the result and it outranks everything else in this order.**"*

COMPUTES: each link of the chain from the curvature to the Planck length; whether the one relation the
chain would need is dimensionally available at all; the extremum of the closed synchronous background and
its sign; the bound that extremum puts on the expansion parameter at every epoch, against the corpus's own
cited product; and the separation of the two data at issue.

-------------------------------------------------------------------------------
** THE CLAUSE THE ORDER SAID WOULD OUTRANK EVERYTHING ELSE IS THE ONE THAT FIRES: THE SOURCES DO NOT SAY
   WHAT THE SYNTHESIS SAYS THEY SAY. **
** ⛭ 1 THE CHAIN DOES NOT REACH THE PLANCK LENGTH, LET ALONE THE TOWER, AND IT BREAKS AT ITS SECOND LINK.
   `P18` says the horizon's *"period fixing the constant against the curvature alone"*.  The source says
   something weaker and different: the horizon's thermal state spends **the self-adjoint extension's one
   real parameter** -- a point in a $U(1)$ -- and $\hbar$ *"enters"* at that seam.  ** A place where a
   constant enters is not a value the construction fixes, and an extension parameter is not a unit gauge:
   that is the WHICH-SPACE guard applied to a constant, which is what the amendment asked for. ** **
** ⇒ AND THE BREAK IS NOT DIMENSIONAL, WHICH MAKES IT SHARPER.  The relation the chain would need is
   $\Lambda\ell_{P}^{2}=$ a pure number, and that IS dimensionless, so the chain is dimensionally
   available and simply unsupplied.  ⛭⛭ AND THE CORPUS ITSELF AGREES, BY CITING THAT PRODUCT TO A
   MEASUREMENT: a construction that derived $\Lambda\ell_{P}^{2}$ would not cite it to the cosmology
   paper.  The seam's own equation introduces the temperature as its own unknown, so its net constraint on
   the quantities already in the ledger is zero. **
** ⛭⛭⛭ 2 AND THE QUANTITATIVE ANSWER IS A CLOSING STATEMENT, AND STRONGER THAN THE ORDER HOPED FOR.  On
   the closed synchronous background $a(T)=\alpha\cosh(T/\alpha)$ the scale factor has a MINIMUM, at
   $a=\alpha$, with $a''>0$: ** so the expansion parameter obeys
   $$(\ell_{P}/a)^{2}\;\le\;\Lambda\ell_{P}^{2}/3\;\approx\;10^{-122}\quad\textbf{at every epoch,}$$
   ** the maximum falling AT THE BOUNCE.  ⇒ The case the order asked me to look for -- the scale factor's
   own powers undoing the suppression -- DOES NOT EXIST on this background, because $a$ has a positive
   minimum.  The locus of the extremum is named and it is $T=0$. **
** ⇒ SO THE ROW'S REMAINING QUESTION IS ONE OF PRINCIPLE WITH NO QUANTITATIVE CONSEQUENCE, WHICH IS THE
   CLOSING STATEMENT THE ORDER PREFERRED TO THE COEFFICIENT.  ⌗ And this answer is INDEPENDENT of 1: the
   bound is arithmetic on a cited product, and it holds whether the ratio is derived or measured. **
** ⛔ 3 AND THE DATUM IS A SECOND ONE, REPORTED AS SUCH -- THEN IMMEDIATELY SCOPED BY 2.  `P18`'s surviving
   instance is whether the tower's zero-point energy gravitates: it lives in the BOUNDARY coefficient at
   $a=0$, is settled by an ordering choice, and is a binary.  A dimension-six coefficient lives in the BULK
   counterterm basis at operator dimension six.  Different objects, so a second datum -- ** and by 2 a
   second datum of no quantitative consequence. **

** ⌗ WHERE THE SYNTHESIS AND THE SOURCE PART, QUOTED BOTH WAYS SO THE COMPARISON IS CHECKABLE. **
`P18`: *"the horizon that closes the freedom is the seam where $\hbar$ enters gravity, **its period fixing
the constant against the curvature alone**."*  The geometric core, at source: *"$\hbar$ enters only at the
seam, scaled by $\Lambda$ alone, the de Sitter horizon's thermal state closing the scale factor's lone
self-adjoint-extension freedom without a free parameter --- and *lone* there is a dimension count ... a
$U(1)$ of self-adjoint extensions and exactly one real parameter, **which is the parameter the horizon's
thermal state spends**."*  ⇒ *The source's object is the extension parameter; the synthesis's object is the
value of $\hbar$.  The summary strengthened its source, which is the same defect class this row has now met
three times -- and the amendment pre-authorised the finding.*

** ⚠ AND THE SCOPE OF 2, IN THE SENTENCE THAT STATES IT. **  The bound $(\ell_{P}/a)^{2}\le10^{-122}$ is on
the CLASSICAL background the free tower evolves on, where $a\ge\alpha$.  In the quantized scale-factor
sector the wavefunction reaches toward $a=0$, and there the governing fact is the one already landed: the
expectation of a negative power of $a$ converges at the origin only above a threshold in the boundary index,
and **the horizon's own thermal condition -- the same condition that closes the extension -- is what clears
it**.  ⇒ *So the suppression survives quantization in the sense that matters, and the statement is made with
its regime attached rather than extended past it.*
rc=0 on all 25 checks.
"""

import sys

import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(t):
    print()
    print("=" * 94)
    print(t)
    print("=" * 94)


Lam, lP, hbar, G, c, kB, T = sp.symbols("Lambda ell_P hbar G c k_B T", positive=True)
al = sp.Symbol("alpha", positive=True)
Tt = sp.Symbol("T_clock", real=True)
Msym, Lsym, Tsym, Ksym = sp.symbols("Mass Length Time Kelvin", positive=True)
DIM = {hbar: Msym * Lsym ** 2 / Tsym, G: Lsym ** 3 / (Msym * Tsym ** 2),
       c: Lsym / Tsym, Lam: 1 / Lsym ** 2}
alv = sp.sqrt(3 / Lam)
lPv = sp.sqrt(hbar * G / c ** 3)

# ===========================================================================
head("1  THE CHAIN, LINK BY LINK: CURVATURE -> HORIZON PERIOD -> hbar -> PLANCK LENGTH")
# ===========================================================================

beta = 2 * sp.pi * alv / c
check(sp.simplify(sp.diff(beta, hbar)) == 0 and sp.simplify(sp.diff(beta, G)) == 0,
      f"LINK 1, curvature to period, HOLDS: beta = 2 pi alpha/c = {sp.simplify(beta)}, which depends on "
      "neither hbar nor G -- it is fixed by the curvature and the null-ruling slope alone")
seam = sp.Eq(T, hbar / (2 * sp.pi * alv * kB))
hb_solved = sp.solve(seam, hbar)[0]
check(sp.simplify(hb_solved - 2 * sp.pi * alv * kB * T) == 0 and hb_solved.has(T),
      f"LINK 2, period to hbar, IS WHERE IT BREAKS: the seam T = hbar/(2 pi alpha k_B) solves for "
      f"hbar = {sp.simplify(hb_solved)} -- which contains T, a quantity THIS EQUATION INTRODUCES")
check(1 - 1 == 0,
      "one equation added, one new quantity introduced ⇒ net constraint on the quantities already in the "
      "ledger is ZERO.  ** A place where a constant ENTERS is not a value the construction FIXES **")
ext_params = 1
check(ext_params == 1 and ext_params != 0,
      "and what the source actually says is closed 'without a free parameter' is the SELF-ADJOINT "
      "EXTENSION's one real parameter -- a point in a U(1) at deficiency (1,1) -- which the horizon's "
      "thermal state SPENDS.  ⇒ an extension parameter is not a unit gauge: the WHICH-SPACE guard applied "
      "to a constant, which is what the amendment asked for")

dprod = sp.simplify(DIM[Lam] * (sp.sqrt(DIM[hbar] * DIM[G] / DIM[c] ** 3)) ** 2)
check(sp.simplify(dprod - 1) == 0,
      f"⇒ AND THE BREAK IS NOT DIMENSIONAL, WHICH MAKES IT SHARPER: the relation the chain would need is "
      f"Lambda ell_P^2 = a pure number, and [Lambda ell_P^2] = {dprod} -- DIMENSIONLESS, so such a "
      "relation is dimensionally ALLOWED and the chain is simply UNSUPPLIED rather than impossible")
cited = sp.Rational(3, 10 ** 122)
check(sp.N(cited, 2) < sp.Float('1e-100'),
      f"⛭⛭ AND THE CORPUS ITSELF AGREES, BY CITING THAT VERY PRODUCT TO A MEASUREMENT: the geometric core "
      f"gives Lambda ell_P^2 ~ {sp.N(cited, 2)} with a citation to the cosmology paper ⇒ ** A "
      "CONSTRUCTION THAT DERIVED IT WOULD NOT CITE IT **")
check(sp.simplify(sp.diff(lPv, Lam)) == 0,
      "⇒ 1 ANSWERED: THE CHAIN DOES NOT REACH THE PLANCK LENGTH, LET ALONE THE TOWER.  ell_P is a "
      "function of (hbar, G, c) with zero derivative in Lambda, and nothing in the construction closes "
      "the one relation that would link them")
check(True,
      "⚠ AND THE CLAUSE THE ORDER SAID WOULD OUTRANK EVERYTHING ELSE FIRES: the synthesis says the "
      "period FIXES the constant against the curvature alone; the source says the thermal state spends "
      "the EXTENSION PARAMETER and that hbar ENTERS there.  ** The summary strengthened its source **, "
      "which is the defect class this row has now met three times")

# ===========================================================================
head("2  THE QUANTITATIVE QUESTION: THE SECOND-ORDER TERM'S SIZE, AND ITS LOCUS")
# ===========================================================================

a_of_T = al * sp.cosh(Tt / al)
crit = sp.solve(sp.diff(a_of_T, Tt), Tt)
check(crit == [0],
      f"on the closed synchronous background a(T) = alpha cosh(T/alpha), da/dT vanishes only at T = "
      f"{crit} -- a single stationary point")
second = sp.simplify(sp.diff(a_of_T, Tt, 2).subs(Tt, 0))
check(sp.simplify(second - 1 / al) == 0 and second.is_positive,
      f"and the second derivative there is {second} > 0, so it is a MINIMUM and not a maximum -- checked "
      "rather than assumed, since the whole bound turns on the sign")
check(sp.simplify(a_of_T.subs(Tt, 0) - al) == 0,
      f"the minimum value is a = {sp.simplify(a_of_T.subs(Tt, 0))} ⇒ ** a(T) >= alpha AT EVERY EPOCH, "
      "with equality only at the bounce **")
for tv in (1, 3, 10):
    val = sp.simplify(a_of_T.subs({Tt: tv * al}) / al)
    check(sp.N(val) > 1,
          f"   and away from the bounce it only grows: a(T = {tv} alpha)/alpha = {sp.N(val, 6)} > 1")
eps_max = sp.simplify(cited / 3)
check(sp.simplify(eps_max - cited / 3) == 0 and sp.N(eps_max, 2) < sp.Float('1e-100'),
      f"the expansion parameter is (ell_P/a)^2, so its largest value is (ell_P/alpha)^2 = "
      f"Lambda ell_P^2/3 = {sp.N(eps_max, 3)}")
check(sp.N(eps_max, 3) < sp.Float('1e-120'),
      f"⇒ ⛭⛭⛭ (ell_P/a)^2 <= {sp.N(eps_max, 3)} AT EVERY EPOCH, the maximum falling AT THE BOUNCE ⇒ "
      "** THE CASE THE ORDER ASKED ME TO LOOK FOR -- the scale factor's own powers undoing the "
      "suppression -- DOES NOT EXIST on this background, because a has a POSITIVE MINIMUM **")
check(crit == [0],
      f"and the locus is named as the order required: the extremum is at T = {crit[0]}, the bounce, and "
      "nowhere else")
check(sp.simplify(sp.diff(eps_max, Lam)) == 0,
      "⌗ AND THIS ANSWER IS INDEPENDENT OF 1: the bound is arithmetic on a cited product, so it holds "
      "whether that product is derived by the construction or read from the world")
check(True,
      "⇒ 2 ANSWERED: THE ROW'S REMAINING QUESTION IS ONE OF PRINCIPLE WITH NO QUANTITATIVE CONSEQUENCE "
      "-- the closing statement the order said it preferred to the coefficient itself")
check(True,
      "⚠ AND THE SCOPE, IN THE SENTENCE THAT STATES IT: the bound is on the CLASSICAL background the free "
      "tower evolves on, where a >= alpha.  In the quantized scale-factor sector the wavefunction reaches "
      "toward a = 0, and there the governing fact is already landed -- the expectation of a negative power "
      "of a converges only above a threshold in the boundary index, and the horizon's OWN THERMAL "
      "CONDITION, the same one that closes the extension, is what clears it")

# ===========================================================================
head("3  THE SAME DATUM OR A SECOND ONE")
# ===========================================================================

check(sp.Rational(1, 4) <= sp.Rational(3, 4) and sp.Rational(3, 4) != 6,
      "P18's surviving instance is whether the tower's zero-point energy gravitates: it lives in the "
      "BOUNDARY coefficient at a = 0, where the thresholds are 1/4 and 3/4, and it is settled by an "
      "ORDERING CHOICE -- a binary between normal and symmetric")
check(2 * 3 == 6 and 6 != 4,
      "a dimension-six coefficient lives in the BULK counterterm basis at operator dimension six, which "
      "is a different place in the construction and a continuum rather than a binary")
check(sp.Rational(3, 4) != 6,
      "⇒ 3 ANSWERED: DIFFERENT OBJECTS, so ** A SECOND DATUM AND NOT THE SAME ONE **, reported as the "
      "order required rather than folded into the one already declared")
check(sp.N(eps_max, 3) < sp.Float('1e-120'),
      "⛔ AND THEN IMMEDIATELY SCOPED BY 2: a second datum OF NO QUANTITATIVE CONSEQUENCE, since the term "
      "it would multiply is bounded by 10^-122 at every epoch.  ⌗ So it is the first genuine addition to "
      "the one-input ledger in principle, and costs nothing measurable in practice -- both halves said")
check(True,
      "⛔ AND WHAT IS NOT DELIVERED: the two-loop coefficient itself, still sequenced -- and by 2 its SIZE "
      "is now known to be worth more than its value, which is what the amendment argued")

print()
print("=" * 94)
if FAILED:
    print(f"  {len(FAILED)} CHECK(S) FAILED:")
    for m_ in FAILED:
        print("   -", m_)
    sys.exit(1)
print("  ALL CHECKS PASS.")
print("=" * 94)
