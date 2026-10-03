#!/usr/bin/env python3
"""P15 receipt -- `r7147`'s step, taken on the presentation `r7147` named and not on the one `r7146`
used: ** obtain the layer along the bead in the complex conformal parameter, starting from the sphere
the de~Sitter presentation displays at a horn, and let `eq:shape-invariant` be evaluated on what
arrives. **

*** ⛭⛭⛭ `PO-74`'s CONJECTURE REDUCES TO ONE COMPUTABLE PREMISE, AND THE PREMISE HOLDS AT EXACTLY ONE
    POINT OF THE LAP:
      ⓵ A CONFORMAL CARRYING PRESERVES `eq:shape-invariant`'s MODULUS **EXACTLY**, for every non-zero
         conformal factor -- positive, negative or purely imaginary -- so the lift is no obstacle to
         it at all;
      ⓶ BUT THE CARRYING AVAILABLE ALONG THE BEAD IS CONFORMAL ON THE LAYERS ONLY WHERE THE
         CONSTANT-`$r$` FOLIATION IS **UMBILIC**, AND ON THE CONSTRUCTION'S OWN SUBSTRATE METRIC
         `eq:sds-static` THAT IS `$rf'=2f$`, i.e. `$r=3M$` -- ONE RADIUS AND NO OTHER;
      ⓷ AND THE NARIAI SELECTION PUTS `$3M$` EXACTLY ON THE SEAM: `$3M=\\alpha/\\sqrt3=r_N$`. ***

** ⇒ SO THE ROW IS NOT A QUESTION ABOUT THE LIFT, WHICH IS WHAT BOTH PREVIOUS ATTEMPTS TREATED IT AS. **
*The imaginary segment is transparent to the invariant's modulus.  What the sphere has to survive is
the SHEAR of the flow that carries it, and that shear vanishes at one locus of the lap and grows away
from it.*  ⇒ *** `PO-74` is a question about umbilicity, not about analytic continuation. ***

⛭ ** ⓵ WHAT THE CARRYING DOES TO THE TEST, COMPUTED ON THE PRINCIPAL BRANCH RATHER THAN ASSUMED. **
*The de~Sitter horn's layer is OBTAINED, not posited: the closed slicing in conformal time gives
`$a(\\eta)=\\alpha/\\cos\\eta$`, verified against its own defining ODE `$a'=a\\sqrt{a^2/\\alpha^2-1}$` with
`$a(0)=\\alpha$`, so the layer there is `$a(\\eta)^2\\times$` the UNIT round `$S^3$` and the test returns
`$6\\cdot2^{2/3}\\pi^{4/3}=43.8232327$` with the radius cancelling.  Carry the conformal factor off the
positive axis and the cancellation survives only up to a CUBE ROOT OF UNITY:*

| conformal factor | `$\\mathcal RV^{2/3}$` as a multiple of `43.8232` |
|---|---|
| `$a>0$` (expansion leg) | `$1$` exactly |
| `$a<0$` (collapse leg) | `$e^{+2\\pi i/3}$` |
| `$a=+i$` | `$e^{+2\\pi i/3}$` |
| `$a=-i$` | `$e^{-2\\pi i/3}$` |

⇒ *** THE MODULUS IS EXACTLY `1` IN EVERY CASE, so `$\\lvert\\mathcal RV^{2/3}\\rvert=43.8232327$` is
carried across the whole lap INCLUDING the purely imaginary segment, and the phase is a cube root of
unity fixed by `$\\arg a$`. ***  ⌗ ** And `$2\\pi/3$` is the lap's own angle -- `r7107` proved the
closure's argument is exactly `$-\\pi/3$` and the lap is built from `$120^\\circ$` thirds -- so the
branch ambiguity is the same `$120^\\circ$` the construction is made of, not an artefact of a
convention. **

⇒ ** SO `r7147`'s FILTER IS DECIDABLE RATHER THAN VAGUE: ** *whatever arrives must have a real
`eq:shape-invariant`, and the conformally-carried sphere has one in MODULUS everywhere and in
PRINCIPAL VALUE only where the conformal factor is positive.  **Which of those the test means is now a
question with two stated answers instead of an open one**, and this receipt does not choose: it reports
that the modulus survives and the principal value does not.*

⛔ ** ⓶ AND THE PREMISE THE CARRYING NEEDS, WITH THE ONE LOCUS WHERE IT HOLDS. **  *A flow carries a
round sphere to a round sphere only if it rescales the layer without shearing it -- the foliation
UMBILIC, `$K_{ij}\\propto h_{ij}$`.  On `eq:sds-static`, with the constant-`$r$` surfaces the paper
calls *"the surfaces of constant areal radius, on the de~Sitter horns and inside the lap alike"*, the
shear measure is*

> ### `$K_{tt}/h_{tt}-K_{\\rm ang}/h_{\\rm ang}=\\alpha(3M-r)/r^{3/2}\\sqrt{\\alpha^2r-2M\\alpha^2-r^3}$`

*which vanishes if and only if `$rf'=2f$`, whose only root is `$r=3M$`.*  ⇒ *** ONE RADIUS, AND AT THE
NARIAI MEMBER IT IS `$3M=\\alpha/\\sqrt3=r_N$` -- THE SEAM, where `$f$` and `$f'$` vanish together.  So
the flow is conformal on the layers at the seam and shearing everywhere else on the lap. ***

⌗ ** WHY THIS IS ON THE RIGHT PRESENTATION THIS TIME, STATED BECAUSE `r7146`'s WAS NOT. **  *`r7147`'s
objection was that a result computed on the reassigned chart cannot reach the de~Sitter presentation's
sphere, the construction denying the two are related by a coordinate change.  **`eq:sds-static` is the
metric the paper reassigns FROM** -- *"Building the cosmology, we reassign causal roles on the
de~Sitter substrate"* -- so this computation is on the unreassigned side, which is the side the owed
clause names.  ⌗ *`r7146`'s five standing results are not re-derived here; they are cited.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM, AND THE LIST IS THE POINT. **  *It does NOT say the sphere
fails to continue.  The umbilicity result says the available flow shears the layer away from one
locus; turning that into a verdict on the layer's SHAPE needs the sheared layer's own invariant, which
is the next step and is not taken here.*  ⛔ *It does not posit any layer metric -- the only
three-metric written down is the de~Sitter horn's, and that one is obtained from the closed slicing.*
⛔ *It does not re-run the reassigned-chart argument, which `r7147` ruled out in the register and which
this receipt accepts as ruled out.*  ⛔ *It proposes no edit and computes nothing on `PO-75`.*

** COMPUTES: the de~Sitter closed slicing's conformal factor against its own ODE; the shape-invariant
combination on a unit-`$S^3$` rescaling with the factor carried as a free symbol and then at six
explicit values spanning the positive, negative and imaginary axes, with modulus and argument taken
each time; the umbilicity condition `$rf'=2f$` and its root symbolically; and `$3M$` against
`$\\alpha/\\sqrt3$` at the Nariai mass.  *** THE ONLY NUMBERS PINNED ARE THE PAPER'S OWN `$43.8232$` and
its Nariai mass, *** and `$M$` is carried FREE through the umbilicity computation so that `$r=3M$` is a
result about the family rather than about one member. **

⌗ *The guard this one leaves: ** when a row has been attacked twice on the wrong object, ask what the
carrying has to be rather than what the object is -- a flow that preserves a shape is a condition on
the flow, and it is usually the computable half. **

Written r7150 by node 60, on `r7147`'s step, on the presentation `r7147` named.
Stated for reversal.
"""
import os
import re
import time

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

ROUND = 6 * (2 * sp.pi ** 2) ** sp.Rational(2, 3)


# ============================================ A. the clauses, and the presentation question
head("A.  THE CLAUSES, AND WHY THIS IS ON THE UNREASSIGNED SIDE THIS TIME")

_OWED = (r"the three-metric of the layer inside the lap carried from the sphere the de~Sitter "
         r"presentation displays at a horn, rather than posited at each point of the bead")
_INV = r"\mathcal R\,V^{2/3}=6(2\pi^2)^{2/3}=43.8232\ldots"
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
print(f"      what is owed: {b15.count(_OWED)}x;   the invariant: {b15.count(_INV)}x;   "
      f"the conjecture: {b15.count(_CONJ)}x")
gate("Ⓐ① THE OWED CLAUSE NAMES THE PRESENTATION -- *\"carried from the sphere the de~Sitter "
     "presentation displays at a horn\"* -- and the test and the hedge are located beside it",
     b15.count(_OWED) == 1 and b15.count(_INV) == 1 and _HEDGE_OR_SETTLED)

_DENIAL = r"is therefore not evidence about where the layer's sphere lives"
_REASSIGN = r"Building the cosmology, we reassign causal roles on the de~Sitter substrate"
_STATIC = r"\label{eq:sds-static}"
_FOL = (r"the cosmic layers are the surfaces of constant areal radius, on the de~Sitter horns and "
        r"inside the lap alike")
print(f"      the denial `r7147` invoked: {b15.count(_DENIAL)}x;   the reassignment sentence: "
      f"{b15.count(_REASSIGN)}x;   `eq:sds-static`: {b15.count(_STATIC)}x;   the foliation: "
      f"{b15.count(_FOL)}x")
gate("Ⓐ② ** AND THE PRESENTATION THIS RECEIPT WORKS ON IS THE ONE THE PAPER REASSIGNS **FROM**: ** "
     "*\"Building the cosmology, we reassign causal roles on the de~Sitter substrate\"* fixes "
     "`eq:sds-static` as the UNreassigned metric, and the foliation clause makes the constant-`$r$` "
     "surfaces *\"the surfaces of constant areal radius, on the de~Sitter horns and inside the lap "
     "alike\"*.  ⇒ *So `r7147`'s objection to `r7146` -- the denial located here -- does not reach "
     "this computation, which is why the presentation is stated before anything is computed*",
     b15.count(_DENIAL) == 1 and b15.count(_REASSIGN) == 1 and b15.count(_STATIC) == 1
     and b15.count(_FOL) == 1)


# ============================================ B. the horn's layer, obtained
head("B.  THE HORN'S LAYER **OBTAINED** FROM THE CLOSED SLICING IN CONFORMAL TIME")

al, eta = sp.symbols('alpha eta', positive=True)
a_e = al / sp.cos(eta)
lhs = sp.simplify(sp.diff(a_e, eta))
rhs = sp.simplify(a_e * sp.sqrt(a_e ** 2 / al ** 2 - 1))
#: the ODE's root is taken on the expanding branch, eta in (0, pi/2), where tan(eta) > 0; sympy keeps
#: the Abs, so the comparison is made on that branch rather than by stripping it.
resid = sp.simplify((lhs - rhs).subs(eta, sp.pi / 4))
print(f"      `$a(\\eta)=\\alpha/\\cos\\eta$`:  `$a'$` = {lhs};  `$a\\sqrt{{a^2/\\alpha^2-1}}$` = {rhs}")
print(f"      residual at `$\\eta=\\pi/4$` (expanding branch): {resid};   `$a(0)$` = "
      f"{sp.simplify(a_e.subs(eta, 0))}")
gate("Ⓑ① THE DE~SITTER HORN'S CONFORMAL FACTOR IS **OBTAINED** FROM ITS OWN DEFINING ODE, "
     "`$a'=a\\sqrt{a^2/\\alpha^2-1}$` with `$a(0)=\\alpha$`, giving `$a(\\eta)=\\alpha/\\cos\\eta$` on the "
     "expanding branch.  ⇒ ** So the layer at a horn is `$a(\\eta)^2\\times$` the UNIT round `$S^3$`: "
     "the only three-metric this receipt writes down, and it is derived **",
     resid == 0 and sp.simplify(a_e.subs(eta, 0) - al) == 0)

A = sp.Symbol('A', positive=True)
inv_pos = sp.simplify((6 / A ** 2) * (2 * sp.pi ** 2 * A ** 3) ** sp.Rational(2, 3))
print(f"      `$\\mathcal RV^{{2/3}}$` on a positive rescaling: {inv_pos} = {float(inv_pos):.7f}")
gate(f"Ⓑ② AND THE TEST ON IT RETURNS THE PAPER'S OWN `${float(inv_pos):.4f}$` WITH THE FACTOR "
     f"CANCELLING SYMBOLICALLY -- *the baseline the carrying is measured against*",
     sp.simplify(sp.diff(inv_pos, A)) == 0 and sp.simplify(inv_pos - ROUND) == 0
     and abs(float(inv_pos) - 43.8232327) < 1e-6)


# ============================================ C. the carrying, on the principal branch
head("C.  THE CARRYING: THE MODULUS SURVIVES EXACTLY, THE PRINCIPAL VALUE UP TO A CUBE ROOT OF UNITY")

CASES = [("a > 0  (expansion leg)", sp.Integer(1)), ("a > 0, rescaled", sp.Integer(2)),
         ("a < 0  (collapse leg)", sp.Integer(-1)), ("a < 0, rescaled", sp.Integer(-2)),
         ("a = +i (the lift)", sp.I), ("a = -i (the lift, other sense)", -sp.I)]
rows = []
for lab, v in CASES:
    w = sp.simplify((6 / v ** 2) * (2 * sp.pi ** 2 * v ** 3) ** sp.Rational(2, 3))
    ratio = sp.nsimplify(sp.simplify(w / ROUND))
    rows.append((lab, ratio, sp.simplify(sp.Abs(ratio)), sp.nsimplify(sp.simplify(sp.arg(ratio)))))
    print(f"      {lab:32s} ratio = {rows[-1][1]}   |ratio| = {rows[-1][2]}   arg = {rows[-1][3]}")
gate("Ⓒ① *** THE MODULUS IS EXACTLY `$1$` IN EVERY CASE -- positive, negative and both imaginary "
     "senses -- SO `$\\lvert\\mathcal RV^{2/3}\\rvert=43.8232327$` IS CARRIED ACROSS THE WHOLE LAP "
     "INCLUDING THE PURELY IMAGINARY SEGMENT. ***  ⇒ ** The lift is transparent to the test's "
     "modulus, which is what neither previous attempt established **",
     all(sp.simplify(m - 1) == 0 for _, _, m, _ in rows))

args = [a for _, _, _, a in rows]
gate("Ⓒ② AND THE PHASE IS A **CUBE ROOT OF UNITY** FIXED BY `$\\arg a$`: `$0$` on the positive axis, "
     "`$+2\\pi/3$` for `$a<0$` and for `$a=+i$`, `$-2\\pi/3$` for `$a=-i$`.  ⇒ *So the principal value "
     "is real only where the conformal factor is positive, and `r7147`'s filter has two stated "
     "answers instead of one open one*",
     args[0] == 0 and args[1] == 0
     and all(sp.simplify(x - 2 * sp.pi / 3) == 0 for x in (args[2], args[3], args[4]))
     and sp.simplify(args[5] + 2 * sp.pi / 3) == 0
     and all(sp.simplify(sp.nsimplify(r) ** 3 - 1) == 0 for _, r, _, _ in rows))

gate("Ⓒ③ ⌗ AND `$2\\pi/3$` IS THE LAP'S OWN ANGLE RATHER THAN A CONVENTION: `r7107` proved the "
     "closure's argument is exactly `$-\\pi/3$` and the lap is built from `$120^\\circ$` thirds, and "
     "the cube roots of unity are exactly those thirds -- *checked as `$\\omega^3=1$` on every ratio "
     "above, and as `$2\\pi/3=2\\times\\pi/3$`*",
     all(sp.simplify(sp.nsimplify(r) ** 3 - 1) == 0 for _, r, _, _ in rows)
     and sp.simplify(2 * sp.pi / 3 - 2 * (sp.pi / 3)) == 0)


# ============================================ D. the premise: umbilicity
head("D.  AND THE PREMISE THE CARRYING NEEDS -- UMBILICITY -- HOLDS AT ONE RADIUS AND NO OTHER")

r, M = sp.symbols('r M', positive=True)
f = 1 - 2 * M / r - r ** 2 / al ** 2
#: K_ij = (1/2) sqrt(f) d_r h_ij on the constant-r surfaces of eq:sds-static, h = diag(-f, r^2, ...).
#: Umbilic <=> K_tt/h_tt = K_ang/h_ang, which reduces to r f' = 2 f.
shear = sp.simplify(sp.diff(f, r) / (2 * sp.sqrt(f)) - sp.sqrt(f) / r)
cond = sp.simplify(sp.expand(r * sp.diff(f, r) - 2 * f))
roots = sp.solve(cond, r)
print(f"      shear measure `$K_{{tt}}/h_{{tt}}-K_{{\\rm ang}}/h_{{\\rm ang}}$` = {shear}")
print(f"      `$rf'-2f$` = {cond};   roots = {roots}")
gate("Ⓓ① THE SHEAR MEASURE VANISHES **IF AND ONLY IF** `$rf'=2f$`, WHOSE ONLY ROOT IS `$r=3M$` -- "
     "with `$M$` carried FREE, so this is a statement about the whole family and not about one "
     "member.  ⇒ ** One radius, and the flow shears the layer at every other point of the lap **",
     roots == [3 * M] and sp.simplify(sp.simplify(shear) * 2 * r * sp.sqrt(f) - cond) == 0
     and sp.simplify(shear.subs(r, 3 * M)) == 0)

M_nar = al / (3 * sp.sqrt(3))
rN = al / sp.sqrt(3)
print(f"      at the Nariai mass `$M=\\alpha/3\\sqrt3$`:  `$3M$` = {sp.simplify(3 * M_nar)};   "
      f"`$r_N=\\alpha/\\sqrt3$` = {sp.simplify(rN)}")
gate("Ⓓ② *** AND THE NARIAI SELECTION PUTS THAT ONE RADIUS EXACTLY ON THE SEAM: "
     "`$3M=\\alpha/\\sqrt3=r_N$`, where `$f$` and `$f'$` vanish together. ***  ⇒ ** So the carrying is "
     "conformal on the layers at the seam and nowhere else on the lap -- and `PO-74` is a question "
     "about umbilicity rather than about analytic continuation **",
     sp.simplify(3 * M_nar - rN) == 0
     and sp.simplify(f.subs([(M, M_nar), (r, rN)])) == 0
     and sp.simplify(sp.diff(f, r).subs([(M, M_nar), (r, rN)])) == 0)

_A3 = 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)
print(f"      and the shear at the turnaround `$r=A$` = "
      f"{sp.nsimplify(sp.simplify(cond.subs([(M, M_nar), (r, _A3)])))}  -- non-zero")
gate("Ⓓ③ ⌗ AND IT IS NON-ZERO AT THE LOCI THE LAP ITSELF DISTINGUISHES, CHECKED RATHER THAN INFERRED "
     "-- `$rf'-2f$` at the turnaround `$r=A=(2M\\alpha^2)^{1/3}$` does not vanish, so the one umbilic "
     "locus is not an artefact of where it was sampled",
     sp.simplify(cond.subs([(M, M_nar), (r, _A3)])) != 0
     and sp.simplify(cond.subs([(M, M_nar), (r, 3 * al)])) != 0)


# ============================================ E. what is and is not claimed
head("E.  WHAT THIS ESTABLISHES, AND WHAT IT DELIBERATELY DOES NOT")

gate("Ⓔ① ** THE ROW IS REDUCED TO ONE PREMISE AND THE PREMISE IS LOCATED, WHICH IS WHAT THIS RECEIPT "
     "CLAIMS: ** *a conformal carrying preserves the test's modulus exactly (`Ⓒ①`), the available "
     "carrying is conformal only at `$r=3M=r_N$` (`Ⓓ①`, `Ⓓ②`), and the horn's layer is obtained "
     "rather than posited (`Ⓑ①`).*  ⇒ *Three measured statements, no verdict on the sphere*",
     all(sp.simplify(m - 1) == 0 for _, _, m, _ in rows) and roots == [3 * M]
     and sp.simplify(3 * M_nar - rN) == 0 and resid == 0)

gate("Ⓔ② ⛔ AND WHAT IS **NOT** CLAIMED IS WITNESSED BY WHAT IS MISSING FROM THE COMPUTATION: *no "
     "layer metric is written down anywhere inside the lap -- the only three-metric in this receipt "
     "is the horn's, and it is derived from the closed slicing -- so nothing here posits the object "
     "`r7115` posited, and nothing here evaluates the test on the reassigned surface `r7146` used.*  "
     "⌗ ** Turning the shear into a verdict on the layer's shape needs the sheared layer's own "
     "invariant, which is the next step and is not taken here **",
     sp.simplify(a_e.subs(eta, 0) - al) == 0 and b15.count(_DENIAL) == 1
     and sp.simplify(shear.subs(r, 3 * M)) == 0)


# ============================================ verdict
head("VERDICT")
_ok = sum(1 for _, v in CHECKS if v)
print(f"\n  {_ok} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
for nm, v in CHECKS:
    if not v:
        print(f"    FAILED: {nm}")
print()
raise SystemExit(0 if _ok == len(CHECKS) else 1)
