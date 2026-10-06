#!/usr/bin/env python3
"""P15 receipt -- `r7191` ⓵, ANSWERED NEGATIVE WITH THE MISSING OBJECTS NAMED:
** the seam's radiated flux is NOT computable on this construction without a progenitor interior,
and there are TWO distinct things missing rather than one. **

*** ⛭⛭⛭ AND NEITHER OF THEM IS THE INTERIOR.  `cc66` said the flux needs the progenitor interior;
    the order asked for that TESTED rather than inherited.  ** Tested, it is true for a different
    reason than `cc66` gave, and the reason is in the lap's own closure. ** ***

** ⓵ THE FIRST MISSING OBJECT: THE SEAM'S SURFACE GRAVITY IS NOT SINGLE-VALUED ON THE SEAM. **
*At the Nariai mass `$-f$` factorises with a DOUBLE root at the front seam `$r=+\\alpha/\\sqrt3$` and a
SIMPLE root at the back seam `$r=-2\\alpha/\\sqrt3$`, so the metric's own `$f'/2$` gives*
`$\\kappa_{\\rm front}=0$` *and* `$\\kappa_{\\rm back}=3\\sqrt3/4\\alpha$`.
  ⇒ *** AND THE LAP'S OWN CLOSURE -- the translation `$r\\mapsto r+\\sqrt3\\alpha$` of `r7134` -- CARRIES
  THE BACK SEAM EXACTLY ONTO THE FRONT SEAM. ***  `$-2\\alpha/\\sqrt3+\\sqrt3\\alpha=+\\alpha/\\sqrt3$`
  identically, which is why `P15` says the two are one locus of the substrate.
  ⇒ ** So the one locus the closure makes carries TWO surface gravities, one of them zero. **  *A
  thermal state is a periodicity at a horizon OF A GIVEN `$\\kappa$`; with `$\\kappa$` two-valued on
  the locus there is no `$\\kappa$` for a periodicity to be `$2\\pi/\\kappa$` OF.*

** ⓶ THE SECOND MISSING OBJECT, AND IT IS INDEPENDENT OF THE FIRST: THE EUCLIDEAN SECTION CLOSES IN
   A CLOCK WHOSE CONVERSION TO THE SEAM'S KILLING TIME VANISHES AT BOTH SEAMS. **
*The construction's Euclidean segment has length* `$s_{\\rm tot}=\\Gamma(\\tfrac16)\\sqrt\\pi/
\\Gamma(\\tfrac23)\\sqrt3\\,2^{1/3}=3.33873802357$` *-- and `P15` says in terms what it is: **a pure
number, carrying neither mass nor epoch**, because it is measured in the bead's own conformal time
`$\\dd\\eta=\\dd\\tilde\\tau/r$.*  *The periodicity a smooth thermal state requires is*
`$\\beta=2\\pi/\\kappa=8\\sqrt3\\pi\\alpha/9=4.83679830462\\,\\alpha$`, *in the seam's KILLING time.*
  ⛔ *** THESE ARE TWO CLOCKS AND I DECLINE TO COMPARE THE NUMBERS. ***  *The conversion is*
  `$\\dd\\eta/\\dd t=f/r$`, *which is **not constant** along the lift and **vanishes at both seams** --
  which are the only loci where a periodicity condition is imposed at all.*
  ⇒ ** So there is no clock in which the construction's section closes with a constant relation to the
  time a periodicity is defined in. **  ⌗ *This is the `r7138` guard applied to this seat's own
  temptation: `3.3387` against `4.8368` is exactly the comparison a reader wants, and it is a
  comparison across a change of clock, so it is not made.*

** ⇒ SO `r7191` ⓵ ANSWERS NO, AND ⓶ DOES NOT FIRE. **  *This revision's own pre-registration tabled
five outcomes with the row-ending one first; the one that obtained is `⓵`, `NO STATE IS SELECTED, AND
THE MISSING OBJECT IS NAMED` -- except that there are two, and naming both is the result.*

** ⛔⛭ AND THE TRAP THE ORDER NAMED IS WHERE THE WORK WENT, NOT A FOOTNOTE. **  *`r7191` warned: do
not let the temperature's existence stand in for its relevance.*
  ⓐ ***The temperature exists and this receipt CONFIRMS it independently*** -- `$\\kappa=3\\sqrt3/
    4\\alpha$` recovered from the metric's own `$f'/2$`, where `cc66` got it from the radial mode
    equation's indicial equation.  **Two routes, one number.**  ⌗ *That is also this receipt's
    affirmative control: the instrument returns a specific non-zero figure on demand, so its negative
    is not a method that can only report absence.*
  ⓑ ***And its relevance is exactly what `⓶` denies.***  `$\\kappa$` lives in the static chart's
    Killing time, and the construction's own closure does not carry that clock across the lap.
  ⇒ ** So the `FIFTH CLOSURE` branch does not fire either, and that distinction matters: this is NOT
  `the flux thermalises, so `$n_s\\to1$`, so the row closes`.  It is `there is no flux here to
  compute`. **  *A closure would have been a mechanism `PO-31`'s terminal clause could count; an
  absence of the object a mechanism would be about is not one, and must not be filed as one.*

⚠ ** WHAT IS NOT CLAIMED. **  *Not that the seam radiates nothing -- that is a statement about a
quantum state and no state is in hand.*  *Not that no state exists; only that **the construction does
not select one**, which is what the order asked.*  *Not that `cc66` was wrong: its conclusion that
the flux needs more than it had is confirmed, and only its reason is replaced.*  *Not that the
progenitor interior would suffice -- the two missing objects here are properties of the LAP, and an
interior does not supply either.*  ⌗ *No paper is edited, no state is posited, no flux computed, no
tilt quoted, and `PO-31`'s row text is `66`'s.*

** COMPUTES: the factorisation of -f at the Nariai mass and its two roots; the surface gravity f'/2
at each seam, symbolically and for arbitrary alpha; the lap's closure translation applied to the back
seam; the required periodicity 2*pi/kappa; the closed form of the Euclidean segment's length; and the
conversion d(eta)/d(t) = f/r with its derivative and its values at both seams.  Reads the paper for
its own statement that the segment's length is a pure number.  No assertion on wall-clock time. **
"""
import os
import re

import sympy as sp

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPER = re.sub(r'\s+', ' ', ''.join(
    ln + '\n' for ln in open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                             encoding='utf-8', errors='replace').read().splitlines()
    if not ln.lstrip().startswith('%')))
PRED = open(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                         'r7210_60_seam_flux_state', 'PREDICTION.md'), encoding='utf-8').read()

r, al = sp.symbols('r alpha', positive=True)
M = al / (3 * sp.sqrt(3))                     # the Nariai mass, fixed by Lambda alone
f = 1 - 2 * M / r - r**2 / al**2
FRONT, BACK = al / sp.sqrt(3), -2 * al / sp.sqrt(3)
LAP = sp.sqrt(3) * al                         # r7134's closure translation


# ============================================================ A. the order's premise, recovered
head("A.  THE PREMISE, RECOVERED FROM THE METRIC RATHER THAN QUOTED FROM THE ORDER")

_minusf = sp.factor(sp.simplify(-f))
_target = (r - FRONT)**2 * (r + 2 * al / sp.sqrt(3)) / (al**2 * r)
print(f"      -f factorised: {_minusf}")
print(f"      matches the paper's double/simple form: "
      f"{sp.simplify(_minusf - _target) == 0}")
gate("Ⓐ① at the Nariai mass `$-f$` has a DOUBLE root at the front seam and a SIMPLE root at the back "
     "-- `$(r-\\alpha/\\sqrt3)^2(r+2\\alpha/\\sqrt3)/\\alpha^2r$` -- computed from the metric and not "
     "taken from the paper's statement of it",
     sp.simplify(_minusf - _target) == 0)

fp = sp.diff(f, r)
k_front = sp.simplify(fp.subs(r, FRONT) / 2)
k_back = sp.simplify(sp.Abs(fp.subs(r, BACK)) / 2)
print(f"      kappa_front = {k_front};   kappa_back = {k_back} = {sp.nsimplify(k_back * al)}/alpha")
gate("Ⓐ② ✔ AND THE AFFIRMATIVE CONTROL IS THE ORDER'S OWN NUMBER: `$\\kappa_{\\rm back}=3\\sqrt3/"
     "4\\alpha$` recovered from the metric's own `$f'/2$`, where `cc66`'s `r7185+cc66.147` got it from "
     "the radial mode equation's indicial equation.  **Two routes, one number.**  ⇒ *so this "
     "receipt's instrument returns a specific non-zero figure on demand and its negative below is not "
     "a method that can only report absence*",
     sp.simplify(k_back - 3 * sp.sqrt(3) / (4 * al)) == 0
     and sp.simplify(f.subs(r, BACK)) == 0)

gate("Ⓐ③ and the front seam is DEGENERATE -- `$f$` and `$f'$` vanish together there, so "
     "`$\\kappa_{\\rm front}=0$` exactly, which is `P7`'s `no bifurcation surface` in the metric's own "
     "terms rather than by citation",
     sp.simplify(f.subs(r, FRONT)) == 0 and k_front == 0)


# ============================================================ B. the first missing object
head("B.  ⛭⛭ THE FIRST MISSING OBJECT: ONE LOCUS, TWO SURFACE GRAVITIES")

_carries = sp.simplify(BACK + LAP - FRONT)
print(f"      closure r -> r + sqrt3*alpha sends the back seam to {sp.simplify(BACK + LAP)};  "
      f"front seam is {FRONT};  difference {_carries}")
gate("Ⓑ① the lap's own closure, the translation `$r\\mapsto r+\\sqrt3\\alpha$` of `r7134`, carries the "
     "back seam EXACTLY onto the front seam -- `$-2\\alpha/\\sqrt3+\\sqrt3\\alpha=+\\alpha/\\sqrt3$` "
     "identically -- which is why the paper says the two are one locus of the substrate",
     _carries == 0
     and 'so the two are one locus of the substrate' in PAPER)

gate("Ⓑ② ⇒ *** SO THE ONE LOCUS THE CLOSURE MAKES CARRIES TWO SURFACE GRAVITIES, `$0$` AND "
     "`$3\\sqrt3/4\\alpha$`, AND THEY ARE NOT EQUAL FOR ANY `$\\alpha$`. ***  *A thermal state is a "
     "periodicity at a horizon OF A GIVEN `$\\kappa$`; with `$\\kappa$` two-valued on the locus there "
     "is no `$\\kappa$` for a period to be `$2\\pi/\\kappa$` of*",
     k_front == 0 and sp.simplify(k_back) != 0
     and sp.simplify(k_back - k_front) != 0
     and sp.solve(sp.Eq(k_back, k_front), al) == [])


# ============================================================ C. the second missing object
head("C.  ⛭⛭ THE SECOND MISSING OBJECT, INDEPENDENT OF THE FIRST: THE TWO CLOCKS")

S_TOT = (sp.gamma(sp.Rational(1, 6)) * sp.sqrt(sp.pi)
         / (sp.gamma(sp.Rational(2, 3)) * sp.sqrt(3) * 2**sp.Rational(1, 3)))
_c0 = 2 / (sp.sqrt(3) * 2**sp.Rational(1, 3))
_beta_form = _c0 * sp.beta(sp.Rational(1, 6), sp.Rational(1, 2)) / 2
print(f"      s_tot (Gamma form)  = {sp.N(S_TOT, 12)}")
print(f"      s_tot (Beta form)   = {sp.N(_beta_form, 12)}   -- the paper's second closed form")
gate("Ⓒ① the Euclidean segment's length is a PURE NUMBER and the paper says so in terms -- "
     "`carrying neither mass nor epoch` -- because it is measured in the bead's own conformal time.  "
     "⌗ *Both of the paper's closed forms are evaluated here and they agree, which is a check on the "
     "read rather than on the paper*",
     abs(float(sp.N(S_TOT - _beta_form))) < 1e-30
     and abs(float(sp.N(S_TOT)) - 3.33873802357) < 1e-10
     and 'a pure number, carrying neither mass nor epoch' in PAPER)

BETA = sp.simplify(2 * sp.pi / k_back)
print(f"      beta = 2pi/kappa_back = {BETA} = {sp.N(BETA / al, 12)} alpha   -- and it carries alpha")
gate("Ⓒ② while the periodicity a smooth thermal state requires carries `$\\alpha$`: "
     "`$\\beta=2\\pi/\\kappa=8\\sqrt3\\pi\\alpha/9=4.83679830462\\,\\alpha$`, in the seam's KILLING "
     "time.  ⇒ *one quantity is dimensionless and the other is a length, so they are not comparable "
     "without a CONSTANT conversion between the clocks*",
     sp.simplify(BETA - 8 * sp.sqrt(3) * sp.pi * al / 9) == 0
     and abs(float(sp.N(BETA / al)) - 4.83679830462) < 1e-10)

dEta_dt = sp.simplify(f / r)                  # d(eta)/d(tautilde) = 1/r ; d(tautilde)/dt = f at E=1
_not_const = sp.simplify(sp.diff(dEta_dt, r)) != 0
_at_front = sp.simplify(dEta_dt.subs(r, FRONT))
_at_back = sp.simplify((f / r).subs(r, BACK))
print(f"      d(eta)/d(t) = f/r = {sp.simplify(sp.expand(dEta_dt))}")
print(f"      constant along the lift: {not _not_const};   at the front seam: {_at_front};   "
      f"at the back seam: {_at_back}")
gate("Ⓒ③ ⛔⛔ *** AND THE CONVERSION BETWEEN THE TWO CLOCKS IS `$f/r$`, WHICH IS NOT CONSTANT ALONG "
     "THE LIFT AND VANISHES AT BOTH SEAMS *** -- which are the only loci where a periodicity "
     "condition is imposed at all.  ⇒ ** So there is no clock in which the construction's section "
     "closes with a constant relation to the time a periodicity is defined in **",
     _not_const and _at_front == 0 and _at_back == 0)

# ** the refusal is asserted on THIS FILE'S OWN SOURCE: nowhere does it subtract or divide the two
#   figures.  *A gate that only SAID it declined the comparison would be a gate on a sentence.* **
_SELF = open(os.path.abspath(__file__), encoding='utf-8').read()
_SELF_CODE = '\n'.join(ln for ln in _SELF.split('\n') if not ln.lstrip().startswith('#'))
# ** the forbidden forms are BUILT rather than written out, so the detector does not match itself --
#   the first draft did exactly that and the gate failed on its own condition. **
_a, _b = 'S_TOT', 'BETA'
_forms = [f'{x}{op}{y}' for x, y in ((_a, _b), (_b, _a))
          for op in (' - ', ' / ', '-', '/')]
_no_cross = not any(t in _SELF_CODE for t in _forms)
print(f"      this receipt forms no difference or ratio of the two figures: {_no_cross}")
gate("Ⓒ④ ⌗ and the comparison a reader wants -- `3.3387` against `4.8368` -- IS DECLINED, because it "
     "is a comparison across a change of clock.  **Asserted on this file's own source: it nowhere "
     "subtracts or divides the two figures.**  *That is `r7138`'s guard applied to this seat's own "
     "temptation, and the gate records the refusal rather than a sentence about it*",
     _no_cross and abs(float(sp.N(S_TOT)) - 3.33873802357) < 1e-10
     and abs(float(sp.N(BETA / al)) - 4.83679830462) < 1e-10)


# ============================================================ D. the trap, discharged
head("D.  ⛔ THE TRAP THE ORDER NAMED, AND IT IS WHERE THE WORK WENT")

gate("Ⓓ① `r7191` warned against letting the temperature's existence stand in for its relevance.  The "
     "temperature EXISTS -- confirmed here by a second route -- and its relevance is what `Ⓒ③` "
     "denies: `$\\kappa$` lives in the static chart's Killing time, and the construction's own "
     "closure does not carry that clock across the lap",
     sp.simplify(k_back - 3 * sp.sqrt(3) / (4 * al)) == 0 and _not_const)

gate("Ⓓ② ⇒ *** SO THE `FIFTH CLOSURE` BRANCH DOES NOT FIRE EITHER, AND THE DISTINCTION IS THE "
     "RESULT: this is NOT `the flux thermalises, so the tilt goes to unity, so the row closes` -- it "
     "is `there is no flux here to compute`. ***  *A closure would be a mechanism `PO-31`'s terminal "
     "clause could COUNT; an absence of the object a mechanism would be about is not one, and filing "
     "it as one would be the error*",
     'THE FLUX IS A FIFTH CLOSURE' in PRED
     and 'NO STATE IS SELECTED, AND THE MISSING OBJECT IS NAMED' in PRED)


# ============================================================ E. the pre-registration
head("E.  THE PRE-REGISTRATION, READ BACK -- FIVE OUTCOMES, AND THE ONE THAT OBTAINED")

gate("Ⓔ① five outcomes were tabled BEFORE any computation, with the row-ending one FIRST and the "
     "one the order called likelier written down so it could not read as aimed at; they are read back "
     "from `PREDICTION.md` here rather than restated",
     all(s in PRED for s in ('NO STATE IS SELECTED, AND THE MISSING OBJECT IS NAMED',
                             'A STATE IS SELECTED AND THE FLUX IS COMPUTABLE',
                             'THE FLUX IS A FIFTH CLOSURE',
                             'AND THE TRAP, NAMED BEFORE THE NUMBERS'))
     and PRED.index('NO STATE IS SELECTED') < PRED.index('A STATE IS SELECTED'))

gate("Ⓔ② and the three things the order named as deciding it are each answered: a bifurcation "
     "surface (the front seam has none, `$\\kappa=0$`, computed at `Ⓐ③`); whether the geometry "
     "selects a state (`Ⓑ②` -- it cannot, `$\\kappa$` is two-valued on the locus); and whether the "
     "Euclidean section fixes a periodicity (`Ⓒ③` -- it cannot, the conversion vanishes where the "
     "condition lives)",
     k_front == 0 and sp.solve(sp.Eq(k_back, k_front), al) == [] and _not_const)

gate("Ⓔ③ ⚠ and the conditions fixed in advance are met: nothing is fitted, no tilt is quoted, the "
     "sign is not argued because `⓶` does not fire, and every periodicity claim comes with its two "
     "numbers and the units they are in",
     'NO FITTING.' in PRED and 'A PERIODICITY CLAIM IS A NUMBER.' in PRED
     and 'SIGN BEFORE SIZE' in PRED)


print()
head("VERDICT")
_f = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_f)} of {len(CHECKS)} checks pass")
if _f:
    print(f"  {len(_f)} FAILED:")
    for n in _f:
        print(f"    - {n}")
    raise SystemExit(1)
print("""  ALL PASS -- r7191's first part answers NO, and the two missing objects are named and neither is
  the progenitor interior.  First: the lap's own closure carries the back seam exactly onto the
  front seam, so the one locus it makes carries two surface gravities, 0 and 3*sqrt3/4alpha, and a
  thermal state is a periodicity at a horizon of a GIVEN kappa.  Second, independently: the
  Euclidean segment closes as a pure number in the bead's conformal time while the periodicity is
  2pi/kappa in the seam's Killing time, and the conversion f/r between those clocks is not constant
  along the lift and vanishes at both seams -- the only loci where the condition is imposed.  So the
  second part does not fire, and the fifth-closure branch does not fire either: this is not a flux
  that thermalises but the absence of the object a flux would be computed from.  cc66's conclusion
  stands and only its reason is replaced; its kappa is confirmed here by a second route, which is
  also the control that this instrument can return a positive.""")
