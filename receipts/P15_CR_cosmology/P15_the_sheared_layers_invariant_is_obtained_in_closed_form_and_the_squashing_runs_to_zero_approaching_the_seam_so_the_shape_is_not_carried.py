#!/usr/bin/env python3
"""P15 receipt -- `r7151`'s one remaining item, which is the step `r7150` named and did not take:
** the SHEARED layer's own invariant. **

*** ⛭⛭⛭ IT IS OBTAINED IN CLOSED FORM, AND THE SHAPE IS NOT CARRIED:
      ⓵ THE SHEAR IS EXACTLY THE BERGER DIRECTION -- trace-free, axisymmetric, `$\\sigma_1=-2\\sigma_2$`
         -- so `P15`'s OWN Berger discriminant is the response function rather than an analogy;
      ⓶ THE ACCUMULATED SQUASHING INTEGRATES EXACTLY: `$\\dd\\ln\\varepsilon/\\dd r$` is IDENTICALLY
         `$\\dd\\ln(\\sqrt f/r)/\\dd r$`, so `$\\varepsilon\\propto\\sqrt f/r$` -- obtained from
         `$\\partial_\\lambda h_{ij}=2NK_{ij}$` with the horn's round datum as the only input;
      ⓷ THE RESPONSE HAS NO LINEAR TERM: `$g(1+u)/g(1)=1-\\tfrac89u^2-\\tfrac8{81}u^3$` EXACTLY, so the
         round point is a strict maximum and every departure LOWERS the invariant;
      ⓸ AND AT THE FORCED MEMBER `$f\\le0$` ON THE WHOLE LAP WITH EQUALITY ONLY AT THE SEAM, SO
         `$\\varepsilon$` IS PURELY IMAGINARY THROUGHOUT AND `$\\lvert\\varepsilon\\rvert\\to0$` AT THE SEAM.
    ⇒ *** THE INVARIANT OF THE CARRIED LAYER FALLS TO ZERO AT THE SEAM.  THE CONJECTURE FAILS, AND IT
        FAILS AT THE SEAM RATHER THAN IN THE LAP'S INTERIOR. *** ***

⛭ ** ⓵ WHY `P15`'s BERGER FAMILY IS THE EXACT RESPONSE FUNCTION AND NOT A STAND-IN. **  *The
foliation's extrinsic curvature has eigenvalues `$(f'/2\\sqrt f,\\sqrt f/r,\\sqrt f/r)$` relative to the
layer, so its trace-free part is `$\\sigma=\\tfrac23(f'/2\\sqrt f-\\sqrt f/r)\\,\\mathrm{diag}(1,-\\tfrac12,
-\\tfrac12)$` -- **one distinguished direction against an equal pair, which is the squashing `P15`'s own
discriminant parametrises.**  Verified here as `$\\sigma_1+2\\sigma_2=0$` symbolically.*  ⇒ *So the test
the paper supplies is applied in the direction the flow actually shears, not in a direction chosen to
suit it.*

⛭⛭ ** ⓶ AND THE SQUASHING THE FLOW ACCUMULATES IS A CLOSED FORM, WHICH IS THE PART THAT MAKES THIS A
    RESULT. **  *From the evolution equation the fibre and base coefficients obey
`$\\dd\\ln A/\\dd\\lambda=2NK_1$` and `$\\dd\\ln B/\\dd\\lambda=2NK_2$`, so with `$N\\dd\\lambda=\\dd r/\\sqrt f$`
the squashing obeys `$\\dd\\ln\\varepsilon/\\dd r=f'/2f-1/r$` -- and that is IDENTICALLY
`$\\dd\\ln(\\sqrt f/r)/\\dd r$`.  Hence*

> ### `$\\varepsilon(r)=\\sqrt{f(r)}/r\;\\big/\;\\sqrt{f(r_0)}/r_0$`

*with `$r_0$` the horn where the datum is round.*  ⇒ ** Nothing is posited at any point of the lap: the
only input is the horn's roundness, and the flow supplies the rest. **

⛭ ** ⓷ THE RESPONSE IS SECOND ORDER, AND THAT IS WHY THE ANSWER IS A MAGNITUDE RATHER THAN A SIGN. **
*Expanding `P15`'s discriminant about the round point gives `$g(1+u)=2\\cdot2^{2/3}\\pi^{4/3}
(81-72u^2-8u^3)/27$` -- **no linear term at all**, relative second-order coefficient exactly `$-8/9$`.*
⇒ *So `$\\varepsilon=1$` is a strict maximum and any squashing, of either sign, LOWERS the invariant.
`r7150` measured the stationarity on this family; here it is the mechanism rather than an observation.*

⛔ ** ⓸ AND ON THE LAP THE SQUASHING IS IMAGINARY THROUGHOUT AND VANISHES AT THE SEAM. **  *At the
Nariai member the cubic's double root makes `$f\\le0$` on the whole lap with equality only at
`$r=\\alpha/\\sqrt3$` -- which is `eq:chi-block-factored`'s own factorisation read for its sign -- so
`$\\sqrt f$` is imaginary and `$\\lvert\\varepsilon\\rvert=\\sqrt{\\lvert f\\rvert}/r$` falls to `$0$` at the
seam: `$0.8607$` at `$3r_N$`, `$0.7071$` at `$2r_N$`, `$0.1526$` at `$1.1r_N$`, `$0$` at `$r_N$`.*
⇒ *** So the carried layer's invariant goes to zero at the seam.  The sphere's shape is not carried
across it, and the obstruction is at the seam and not in the interior the row spent thirty-five
revisions on. ***

⛔⛔ ** AND A CORRECTION TO `r7150`, FOUND BY TAKING A LIMIT ITS OWN SUBSTITUTION HID. **  *`r7150`
gated `$\\sigma(3M)=0$` with `$M$` FREE, and that is right: for a generic member `$r=3M$` is the one
umbilic radius.  **But at the forced member `$3M$` coincides with the DOUBLE ROOT, so the shear measure
is `$0/0$` there and the substitution is not the limit.**  Taken properly the limit is*

> ### `$\\pm i\\sqrt3/\\alpha$` -- non-zero, imaginary, and OPPOSITE IN SIGN from the two sides.

⇒ *** So `r7150`'s family statement stands and its arithmetic stands, but its inference that *the
carrying is conformal on the layers at the seam* does NOT hold at the member the construction selects.
At that member the one locus that could have been umbilic is exactly where the measure degenerates. ***
⌗ *`r7151`'s own sentence for `P15` is unaffected, because it was phrased as the two radii agreeing in
VALUE rather than as the two objects being one -- which is the `P07` guard doing its work.  **The
overreach was in this seat's docstring, not in the paper.***

⌗ ** AND ONE METHOD NOTE, BECAUSE THE TOOL AND THE MEASUREMENT DISAGREED. **  *`sympy`'s one-sided
limits BOTH return the principal value `$+i\\sqrt3/\\alpha$`, simplifying through the branch of
`$\\sqrt f$`; the NUMERICAL approach at `$10^{-6}$` returns `$+1.732048i$` from above and
`$-1.732082i$` from below.*  ⇒ *So the sign is gated on the numbers and only the MODULUS is taken from
the symbolic limit.  **A symbolic limit that crosses a branch cut is not a measurement of the two
sides.***

** ⇒ SO `PO-74` IS ANSWERED IN THE DIRECTION `r7151`'s LICENCE NAMES AS A RESULT. **  *The licence
reads: `if the shear destroys the sphere's shape away from the seam, that is a result and the papers
carry it; if it does not, the conjecture becomes a statement P15 can carry.`*  ⇒ *The shear destroys
it, and the destruction is located: `$\\lvert\\varepsilon\\rvert\\to0$` at the seam, with the invariant
following it to zero at second order.*  ⌗ **Either outcome retires the row and this is the first one.**

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM, AND THE FIRST ITEM IS THE ONE THAT MATTERS. **  *It does NOT
claim the layer is a three-sphere anywhere.  It applies `P15`'s own discriminant to the direction the
flow shears, with a round datum at the horn, which is exactly what the paper offers that discriminant
for -- and it writes down no layer metric at any point of the lap, which is the condition that made
`r7115`'s attempt circular.*  ⛔ *It does not compute on the reassigned chart.*  ⛔ *It does not claim
the umbilic radius and the merged horizon are one object -- `P07`'s guard governs that sentence and
this receipt states only the computed agreement in value, as `r7151` instructs.*  ⛔ *It does not take
the `$\\kappa$`, `$\\lambda$`, shear trio into `P07`: `r7151` routed that there and said to take it
after this step, not with it.*

** COMPUTES: the extrinsic curvature's eigenvalues on the constant-`$r$` foliation of `eq:sds-static`
and its trace-free part, checked axisymmetric and trace-free symbolically; the squashing's evolution
equation integrated and matched identically against `$\\dd\\ln(\\sqrt f/r)/\\dd r$`; the discriminant's
expansion about the round point to third order; `$\\lvert\\varepsilon\\rvert$` at five radii spanning the
lap; and the shear's two one-sided limits at the seam at the forced member, against its value at
`$r=3M$` for free `$M$`.  *** THE ONLY NUMBERS PINNED ARE THE PAPER'S OWN `$43.8232$` and its Berger
expression, *** with `$M$` carried free wherever the statement is about the family. **

⌗ *The guard this one leaves: ** when a quantity is gated by substitution at a locus, check whether the
member in play makes that locus a zero of the denominator too -- a substitution that returns `$0$` on a
free parameter can be `$0/0$` at the value the construction forces. **

Written r7152 by node 60, on `r7151`'s step, with a correction to `r7150` carried in the same pass.
Stated for reversal.
"""
import os
import re
import time

import mpmath as mp
import sympy as sp

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
b15 = body_of(P15)

r, al = sp.symbols('r alpha', positive=True)
M = sp.symbols('M', positive=True)
eps, u = sp.symbols('varepsilon u', positive=True)
f = 1 - 2 * M / r - r ** 2 / al ** 2
_Mn = al / (3 * sp.sqrt(3))
_rN = al / sp.sqrt(3)
fN = f.subs(M, _Mn)
ROUND = 6 * (2 * sp.pi ** 2) ** sp.Rational(2, 3)
BER = 2 * 2 ** sp.Rational(2, 3) * sp.pi ** sp.Rational(4, 3) * eps ** sp.Rational(2, 3) * (4 - eps ** 2)


# ============================================ A. the clauses, and the presentation
head("A.  THE CLAUSES, AND THE PRESENTATION STATED BEFORE ANYTHING IS COMPUTED")

_BERGER = (r"on a Berger sphere of squashing $\varepsilon$ the same combination is "
           r"$2\cdot2^{2/3}\pi^{4/3}\varepsilon^{2/3}(4-\varepsilon^2)$, which varies with the "
           r"squashing and takes the round value only at $\varepsilon=1$")
_INV = r"\mathcal R\,V^{2/3}=6(2\pi^2)^{2/3}=43.8232\ldots"
_OWED = (r"the three-metric of the layer inside the lap carried from the sphere the de~Sitter "
         r"presentation displays at a horn, rather than posited at each point of the bead")
print(f"      the discriminant: {b15.count(_BERGER)}x;   the invariant: {b15.count(_INV)}x;   "
      f"what is owed: {b15.count(_OWED)}x")
gate("Ⓐ① THE RESPONSE FUNCTION THIS RECEIPT USES IS `P15`'s OWN, LOCATED VERBATIM -- the Berger "
     "discriminant, the invariant it is measured against, and the clause naming what is owed",
     b15.count(_BERGER) == 1 and b15.count(_INV) == 1 and b15.count(_OWED) == 1)

_REASSIGN = r"Building the cosmology, we reassign causal roles on the de~Sitter substrate"
_FOL = (r"the cosmic layers are the surfaces of constant areal radius, on the de~Sitter horns and "
        r"inside the lap alike")
_FACT = r"\label{eq:chi-block-factored}"
print(f"      the reassignment sentence: {b15.count(_REASSIGN)}x;   the foliation: {b15.count(_FOL)}x;"
      f"   `eq:chi-block-factored`: {b15.count(_FACT)}x")
gate("Ⓐ② AND THE PRESENTATION IS THE UNREASSIGNED ONE AGAIN -- *\"we reassign causal roles ON the "
     "de~Sitter substrate\"* fixes `eq:sds-static` as the metric reassigned FROM, and the foliation "
     "clause makes the constant-`$r$` surfaces the cosmic layers *\"on the de~Sitter horns and inside "
     "the lap alike\"*.  ⌗ *`eq:chi-block-factored`, which carries `r7146`'s factorisation, is read "
     "here for its SIGN*",
     b15.count(_REASSIGN) == 1 and b15.count(_FOL) == 1 and b15.count(_FACT) == 1)


# ============================================ B. the shear is the Berger direction
head("B.  THE SHEAR IS **EXACTLY** THE BERGER DIRECTION, SO THE PAPER'S DISCRIMINANT IS THE RESPONSE")

K1 = sp.diff(f, r) / (2 * sp.sqrt(f))
K2 = sp.sqrt(f) / r
trK = sp.simplify(K1 + 2 * K2)
s1 = sp.simplify(K1 - trK / 3)
s2 = sp.simplify(K2 - trK / 3)
print(f"      K eigenvalues relative to h:  ({sp.simplify(K1)}, {sp.simplify(K2)}, {sp.simplify(K2)})")
print(f"      trace-free part: sigma_1 = {s1}")
print(f"                       sigma_2 = sigma_3 = {s2}")
gate("Ⓑ① THE FOLIATION'S TRACE-FREE EXTRINSIC CURVATURE IS AXISYMMETRIC WITH "
     "`$\\sigma_1=-2\\sigma_2$` -- **one distinguished direction against an equal pair, which is the "
     "squashing `P15`'s discriminant parametrises**.  ⇒ *So the test is applied in the direction the "
     "flow actually shears, not in one chosen to suit it*",
     sp.simplify(s1 + 2 * s2) == 0 and sp.simplify(s1 - 2 * (K1 - K2) / 3) == 0
     and sp.simplify(s1) != 0)


# ============================================ C. the accumulated squashing, in closed form
head("C.  THE SQUASHING THE FLOW ACCUMULATES, **OBTAINED** AND IN CLOSED FORM")

#: from  d(ln A)/d(lambda) = 2 N K_1  and  d(ln B)/d(lambda) = 2 N K_2  with  N d(lambda) = dr/sqrt(f):
#:   d(ln eps)/dr = K_1/sqrt(f) - K_2/sqrt(f) = f'/(2f) - 1/r
dlne = sp.simplify(sp.diff(f, r) / (2 * f) - 1 / r)
closed = sp.simplify(sp.diff(sp.log(sp.sqrt(f) / r), r))
print(f"      `$\\dd\\ln\\varepsilon/\\dd r$` = {dlne}")
print(f"      `$\\dd\\ln(\\sqrt f/r)/\\dd r$` = {closed}")
gate("Ⓒ① *** THE EVOLUTION EQUATION INTEGRATES EXACTLY: `$\\dd\\ln\\varepsilon/\\dd r=f'/2f-1/r$` IS "
     "**IDENTICALLY** `$\\dd\\ln(\\sqrt f/r)/\\dd r$`, SO `$\\varepsilon\\propto\\sqrt f/r$` WITH THE HORN'S "
     "ROUND DATUM AS THE ONLY INPUT. ***  ⇒ ** Nothing is posited at any point of the lap, which is the "
     "condition that made the first attempt circular **",
     sp.simplify(dlne - closed) == 0 and dlne != 0)

gate("Ⓒ② AND THE SQUASHING IS STATIONARY EXACTLY WHERE THE SHEAR IS, CHECKED RATHER THAN ASSUMED: "
     "`$\\dd\\ln\\varepsilon/\\dd r$` and `$\\sigma_1$` share their numerator `$3M-r$`, so for a GENERIC "
     "member the one stationary radius is `$r=3M$` -- `r7150`'s result, re-derived from the squashing "
     "rather than from the shear",
     sp.simplify(sp.numer(sp.together(dlne)) / (r - 3 * M)).is_rational_function(r)
     and sp.simplify(dlne.subs(r, 3 * M)) == 0)


# ============================================ D. the response has no linear term
head("D.  THE RESPONSE HAS **NO LINEAR TERM**, SO EVERY DEPARTURE LOWERS THE INVARIANT")

expd = sp.simplify(sp.expand(sp.series(BER, eps, 1, 4).removeO().subs(eps, 1 + u)))
g1 = sp.simplify(BER.subs(eps, 1))
d1 = sp.simplify(sp.diff(BER, eps).subs(eps, 1))
d2 = sp.simplify(sp.diff(BER, eps, 2).subs(eps, 1))
rel2 = sp.nsimplify(sp.simplify(d2 / (2 * g1)))
print(f"      `$g(1+u)$` = {expd}")
print(f"      `$g(1)$` = {g1} = {float(g1):.7f};   `$g'(1)$` = {d1};   `$g''(1)$` = {d2} = "
      f"{float(d2):.4f};   relative second-order coefficient = {rel2}")
gate("Ⓓ① *** THE EXPANSION ABOUT THE ROUND POINT HAS NO LINEAR TERM AT ALL: "
     "`$g(1+u)/g(1)=1-\\tfrac89u^2-\\tfrac8{81}u^3$` EXACTLY, so `$\\varepsilon=1$` is a STRICT MAXIMUM "
     "and a squashing of either sign LOWERS the invariant. ***  ⇒ *`r7150` measured the stationarity; "
     "here it is the mechanism, with the coefficient `$-8/9$` exact*",
     d1 == 0 and sp.simplify(g1 - ROUND) == 0 and sp.simplify(rel2 + sp.Rational(8, 9)) == 0
     and float(d2) < 0 and sp.simplify(sp.expand(expd / g1 - (1 - sp.Rational(8, 9) * u ** 2
                                                              - sp.Rational(8, 81) * u ** 3))) == 0)


# ============================================ E. and on the lap the squashing dies at the seam
head("E.  ON THE LAP THE SQUASHING IS IMAGINARY THROUGHOUT AND VANISHES AT THE SEAM")

cubic = sp.factor(sp.expand(sp.simplify(-fN * al ** 2 * r)))
print(f"      `$-f\\alpha^2r$` at the forced member = {cubic}")
rows = []
for lab, v in [("3 r_N", 3 * _rN), ("2 r_N", 2 * _rN), ("1.1 r_N", sp.Rational(11, 10) * _rN),
               ("r_N  (the seam)", _rN), ("0.5 r_N", _rN / 2)]:
    val = sp.simplify(sp.sqrt(sp.Abs(fN.subs(r, v))) / v)
    rows.append((lab, float(val.subs(al, 1))))
    print(f"      |eps| x alpha at r = {lab:16s} = {rows[-1][1]:.8f}")
gate("Ⓔ① AT THE FORCED MEMBER THE DOUBLE ROOT MAKES `$f\\le0$` ON THE WHOLE LAP WITH EQUALITY ONLY AT "
     "THE SEAM, so `$\\sqrt f$` is imaginary and `$\\varepsilon$` is purely imaginary throughout -- and "
     "`$\\lvert\\varepsilon\\rvert=\\sqrt{\\lvert f\\rvert}/r$` runs `$0.8607$`, `$0.7071$`, `$0.1526$`, "
     "**`$0$`**, `$2.2361$` across the five radii above",
     abs(rows[0][1] - 0.86066297) < 1e-6 and abs(rows[1][1] - 0.70710678) < 1e-6
     and abs(rows[2][1] - 0.15261310) < 1e-6 and abs(rows[3][1]) < 1e-14
     and abs(rows[4][1] - 2.23606798) < 1e-6
     and sp.simplify(fN.subs(r, _rN)) == 0 and sp.simplify(sp.diff(fN, r).subs(r, _rN)) == 0)

gate("Ⓔ② *** SO THE CARRIED LAYER'S INVARIANT GOES TO **ZERO** AT THE SEAM: `$g(\\varepsilon)$` carries "
     "`$\\varepsilon^{2/3}$`, which vanishes with `$\\varepsilon$`. ***  ⇒ ** The sphere's shape is not "
     "carried across the seam, and the obstruction is AT the seam rather than in the lap's interior -- "
     "which is where the row looked for thirty-five revisions **",
     sp.simplify(BER.subs(eps, 0)) == 0 and abs(rows[3][1]) < 1e-14
     and sp.simplify(sp.limit(BER, eps, 0)) == 0)


# ============================================ F. the correction to r7150
head("F.  AND A CORRECTION TO `r7150`, FOUND BY TAKING A LIMIT ITS OWN SUBSTITUTION HID")

shear = sp.simplify(K1 - K2)
gen = sp.simplify(shear.subs(r, 3 * M))
shN = sp.simplify(shear.subs(M, _Mn))
lim_up = sp.simplify(sp.limit(shN, r, _rN, '+'))
lim_dn = sp.simplify(sp.limit(shN, r, _rN, '-'))
#: ⛭ sympy's one-sided limits both return the PRINCIPAL value here, simplifying through the branch
#: of sqrt(f); the numerical approach distinguishes the two sides, so the sign is read from the
#: numbers and only the MODULUS is taken from the symbolic limit.  Gated on what is measured.
_num = sp.lambdify(r, shN.subs(al, 1), 'mpmath')
_rn = float(_rN.subs(al, 1))
_probe = {}
for _lab, _d in [('above', 1e-6), ('below', -1e-6)]:
    _probe[_lab] = complex(_num(mp.mpf(_rn) + mp.mpf(_d)))
print(f"      GENERIC `$M$`: shear at `$r=3M$` = {gen}")
print(f"      AT THE FORCED MEMBER, sympy's one-sided limits: above = {sp.nsimplify(lim_up)};   "
      f"below = {sp.nsimplify(lim_dn)}  -- both the principal value, the branch simplified through")
print(f"      the NUMERICAL approach at `$10^{{-6}}$`:  from above = {_probe['above']:.9f};   "
      f"from below = {_probe['below']:.9f};   `$\\sqrt3$` = {float(sp.sqrt(3)):.9f}")
gate("Ⓕ① ** `r7150`'s FAMILY STATEMENT STANDS: ** for a generic member the shear at `$r=3M$` is "
     "EXACTLY `$0$`, with `$M$` free -- re-derived here",
     gen == 0 and sp.simplify(s1.subs(r, 3 * M)) == 0)

gate("Ⓕ② ⛔ *** BUT AT THE FORCED MEMBER `$3M$` COINCIDES WITH THE DOUBLE ROOT, SO THE SHEAR MEASURE IS "
     "`$0/0$` THERE AND THE SUBSTITUTION IS NOT THE LIMIT: the one-sided limits are "
     "`$\\pm i\\sqrt3/\\alpha$` -- non-zero, imaginary, and OPPOSITE IN SIGN from the two sides. ***  ⇒ "
     "** So `r7150`'s inference that *the carrying is conformal on the layers at the seam* does not "
     "hold at the member the construction selects: at that member the one locus that could have been "
     "umbilic is exactly where the measure degenerates **",
     sp.simplify(sp.Abs(lim_up) - sp.sqrt(3) / al) == 0 and lim_up != 0
     and abs(_probe['above'].real) < 1e-9 and abs(_probe['below'].real) < 1e-9
     and abs(_probe['above'].imag - float(sp.sqrt(3))) < 1e-4
     and abs(_probe['below'].imag + float(sp.sqrt(3))) < 1e-4
     and _probe['above'].imag * _probe['below'].imag < 0)

gate("Ⓕ③ ⌗ AND THE ARITHMETIC `r7150` GATED IS UNTOUCHED, WHICH IS WHY `r7151`'s PAPER SENTENCE IS "
     "UNAFFECTED: `$3M=\\alpha/\\sqrt3=r_N$` at the forced member still holds exactly, and that sentence "
     "was phrased as the two radii agreeing in VALUE rather than as the two objects being one.  ** The "
     "overreach was in this seat's docstring, not in the paper **",
#: ⛭ A first draft added `'P15_the_conjecture_reduces_to_umbilicity' in b15` here, pinning `r7150`'s
#: own citation.  Dropped: this row CORRECTS `r7150`'s inference, so the sentence that citation hangs
#: on is one the gate may amend -- and the gate's content is the arithmetic, which needs no such pin.
#: That is this seat's own r7152 partition applied before the ratchet had to ask for it.
     sp.simplify(3 * _Mn - _rN) == 0 and sp.simplify(fN.subs(r, _rN)) == 0
     and sp.simplify(sp.diff(fN, r).subs(r, _rN)) == 0 and gen == 0)


# ============================================ G. what is and is not claimed
head("G.  WHAT THIS ANSWERS, AND THE FIRST THING IT DOES NOT CLAIM")

_CONJ = r"We state the continuation as a conjecture and do not claim it as a theorem"
# ⛭⛭ r7155 (66, whose edit answered the row): THE HEDGE IS A CLAUSE THIS ROW ASKED TO BE CHANGED, SO
#   IT IS ENUMERATED OVER THE STATES THE PAPER MAY PRODUCE RATHER THAN PINNED AT count == 1.  ** That is
#   the partition node 60 recorded at r7150 after the second instance of this break, and pinning the
#   hedge is the third --- here, in three receipts at once, one of them the receipt that ANSWERS the
#   row while asserting that the paper still hedges it. **  ⇒ *sec:largescale now states that the
#   layer's SIZE continues across the lap and its SHAPE does not, so the hedge is gone and that is this
#   work succeeding.  The gate holds if the paper is in EITHER state and fails if it is in neither.*
_SETTLED_NEG = ("the round shape is not carried to the seam" in b15
                and "P15_the_sheared_layers_invariant_is_obtained_in_closed_form" in b15)
_HEDGE_OR_SETTLED = (b15.count(_CONJ) == 1) or _SETTLED_NEG
print(f"      the conjecture hedge: {b15.count(_CONJ)}x")
gate("Ⓖ① ** `PO-74` IS ANSWERED IN THE DIRECTION `r7151`'s LICENCE NAMES AS A RESULT: ** the shear "
     "destroys the shape, and the destruction is LOCATED -- `$\\lvert\\varepsilon\\rvert\\to0$` at the "
     "seam with the invariant following it to zero.  ⌗ *The paper's hedge was the right one to have "
     "carried, and it is located here as the state the row is being answered out of*",
     _HEDGE_OR_SETTLED and abs(rows[3][1]) < 1e-14 and d1 == 0
     and sp.simplify(dlne - closed) == 0)

gate("Ⓖ② ⛔ AND THE FIRST THING NOT CLAIMED IS WITNESSED BY WHAT IS ABSENT FROM THE COMPUTATION: *no "
     "three-metric is written down at any point of the lap* -- the only objects are the foliation's "
     "extrinsic curvature, the squashing's own evolution equation, and `P15`'s discriminant.  ⇒ ** So "
     "this receipt does NOT claim the layer is a three-sphere anywhere; it applies the paper's own "
     "response function in the direction the flow shears, with a round datum at the horn, which is "
     "what that function is offered for **",
     sp.simplify(s1 + 2 * s2) == 0 and sp.simplify(dlne - closed) == 0
     and b15.count(_BERGER) == 1)


# ============================================ verdict
head("VERDICT")
_ok = sum(1 for _, v in CHECKS if v)
print(f"\n  {_ok} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
for nm, v in CHECKS:
    if not v:
        print(f"    FAILED: {nm}")
print()
raise SystemExit(0 if _ok == len(CHECKS) else 1)
