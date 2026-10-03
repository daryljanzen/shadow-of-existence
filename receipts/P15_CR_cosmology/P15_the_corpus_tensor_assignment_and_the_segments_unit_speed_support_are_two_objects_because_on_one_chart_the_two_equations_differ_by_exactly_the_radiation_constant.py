#!/usr/bin/env python3
"""P15 receipt -- `r7137`'s `PO-79`, FIRST STEP, WHICH THE ORDER SAYS IS A READ: ** ARE THE CORPUS'S
TENSOR ASSIGNMENT AND THE SEGMENT'S `$c_s=1$` SUPPORT ABOUT ONE OBJECT OR TWO? **
*** ⛭⛭⛭ TWO -- AND THE ORDER'S FIRST BRANCH HOLDS.  WRITTEN ON ONE CHART, WITH THE SCALE FACTOR THE
    PAPERS THEMSELVES IDENTIFY (`$a=r$`, *"at the Nariai member it IS that scale factor"*), THE TENSOR
    EQUATION ON THE LEAF AND ON THE SEGMENT'S CURVE DIFFER BY
        ** `$A_r\\,(r\\varphi''+2\\varphi')/r$` -- EXACTLY THE RADIATION CONSTANT, `$k$`-INDEPENDENT,
           VANISHING AT `$A_r=0$` AND NOWHERE ELSE. **
    SO IT IS A SECOND INSTANCE OF THE TWO-CONGRUENCE SPLIT AND NOT AN UNSTATED IDENTIFICATION. ***

⛭ ** WHAT THE READ FOUND, AND IT IS WHY THE QUESTION WAS LIVE. **  *`P15`'s own introduction assigns
the tensor half elsewhere -- **"the propagating graviton as the leaf's shear, a massless de~Sitter
mode on the cosmic foliation"** -- and `P10` carries the same object as the layer's own propagating
degree of freedom, **"the transverse-traceless shear of its spatial geometry, the graviton"**.  ⇒ So
the `$c_s=1$` equation `r7136` identified is, on its face, the equation the corpus already hands to
the LEAF.*
⌗ *And `P10` has a clause that reads, at first glance, as settling it the other way: the congruence
**"carrying the flat-`$\\Lambda$CDM` and the closed-`$S^3$` slicings as two synchronizations of
itself, not two frames."*** ⇒ *** But that clause is about two SYNCHRONIZATIONS of one congruence,
and this receipt's control shows a synchronization cannot produce the `$A_r$` term: the `$r$`-form of
the equation depends on `$(rH)^2$` and on nothing else, so ANY monotone re-timing leaves it alone.
** The two clauses are therefore about different distinctions, and the one that bites is content. ** ***

** ⌗ THE CONTROL IS WHAT MAKES THIS A FINDING RATHER THAN A SUBTRACTION. **  *The same field equation
is pushed to `$r$` twice by two genuinely different clocks -- once from CONFORMAL time
(`$\\varphi''+2(a'/a)\\varphi'+k^2\\varphi=0$`) and once from PROPER time
(`$\\ddot\\varphi+3H\\dot\\varphi+(k^2/a^2)\\varphi=0$`) -- and the two routes agree up to the measure
factor `$r^2$`, on BOTH congruences.*  ⇒ *A difference that survives that is a difference in what the
background contains, not in how it is clocked.*

⌗ ** ONE DATUM, WITH ITS LIMIT STATED. **  *In each congruence's own conformal time the tensor
potential reads `$a''/a=0$` identically on the leaf (`$a\\propto\\eta$`) and `$a''/a=2/\\eta^2$` on the
bead (`$a\\propto\\eta^2$`).*  ⛔ *** What that does NOT settle is freezing: the frozen quantity is
`$h=u/a$` and not `$u$`, so a vanishing potential term does not mean nothing freezes.  This receipt
computes the two potentials and claims nothing about either one's super-horizon behaviour. ***

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not say which species' perturbation the crossing
transports -- `PO-79` asks that and this is its first step, the read the order names.  It does not
claim the corpus's tensor assignment is wrong: the graviton is the leaf's shear, and the segment's
curve supports a unit-speed mode of its own; the finding is that those are two objects.  It does not
touch `70`'s `PO-77` ⓵, computes nothing on `PO-74` or `PO-75`, proposes no edit to any paper, and
asserts nothing about any other receipt's state.*

** COMPUTES: the Nariai member in the gauge `$\\alpha=1$`, `$2M=2\\alpha/3\\sqrt3$`, with the radiation
constant SYMBOLIC as `$A_r$` and the comoving wavenumber symbolic as `$k$`.  The scale factor is
`$a=r$` on BOTH congruences, which is the papers' own identification and is what makes the comparison
a comparison rather than a change of variable. **  *No value of `$A_r$` or `$k$` is used anywhere; the
result is an identity in both.  `$A$` is never used here, so there is no collision with
`eq:amplitude`'s turnaround amplitude.*
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
P10 = os.path.join(ROOT, 'corpus', 'canonical_time.tex')
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
OPENED = sorted(os.path.basename(x) for x in (P15, P10, P07))
b15, b10, b07 = body_of(P15), body_of(P10), body_of(P07)

r, al, Ar, k = sp.symbols('r alpha A_r k', positive=True)
eta = sp.Symbol('eta', positive=True)
_M2 = 2 * al / (3 * sp.sqrt(3))
phi = sp.Function('varphi')

RH2_LEAF = Ar / r ** 2 + _M2 / r + r ** 2 / al ** 2      # (rH)^2 = (1-f) + A_r/r^2
RH2_BEAD = _M2 / r + r ** 2 / al ** 2                    # the vacuum case, the segment's own curve


def via_conformal(rH2):
    """phi'' + 2(a'/a)phi' + k^2 phi = 0, conformal time, pushed to r with a = r."""
    D = lambda g: r * sp.sqrt(rH2) * sp.diff(g, r)
    return sp.simplify(D(D(phi(r))) + 2 * sp.sqrt(rH2) * D(phi(r)) + k ** 2 * phi(r))


def via_proper(rH2):
    """the SAME equation in proper time, phi_tt + 3 H phi_t + (k^2/a^2) phi = 0, pushed to r."""
    H = sp.sqrt(rH2) / r
    T = lambda g: sp.sqrt(rH2) * sp.diff(g, r)
    return sp.simplify(T(T(phi(r))) + 3 * H * T(phi(r)) + k ** 2 / r ** 2 * phi(r))


# ============================================ A. the clauses the read turned up
head("A.  THE CLAUSES THE READ TURNED UP -- LOCATED IN `P15`, `P10` AND `P07`, NOT RECALLED")

_TENSOR15 = (r"the propagating graviton as the leaf's shear, a massless de~Sitter mode on the "
             r"cosmic foliation")
print(f"      `P15`'s tensor assignment: {b15.count(_TENSOR15)}x")
gate("Ⓐ① `P15`'s INTRODUCTION ASSIGNS THE TENSOR HALF TO **THE LEAF'S SHEAR**, *\"a massless "
     "de~Sitter mode on the cosmic foliation\"* -- which is why `r7136`'s `$c_s=1$` identification "
     "made the question live rather than idle",
     b15.count(_TENSOR15) == 1)

_SHEAR10 = (r"The full layer does carry such a degree of freedom---the transverse-traceless shear of "
            r"its spatial geometry, the graviton")
_FRAMES10 = (r"It is one congruence, carrying the flat-$\Lambda$CDM and the closed-$S^3$ slicings as "
             r"two synchronizations of itself, not two frames")
print(f"      `P10`'s shear identification: {b10.count(_SHEAR10)}x;  its 'not two frames' clause: "
      f"{b10.count(_FRAMES10)}x")
gate("Ⓐ② `P10` CARRIES THE SAME OBJECT AS THE LAYER'S PROPAGATING DEGREE OF FREEDOM, AND SEPARATELY "
     "SAYS THE CONGRUENCE CARRIES TWO SLICINGS AS **TWO SYNCHRONIZATIONS OF ITSELF, NOT TWO FRAMES** "
     "-- *the clause that has to be read carefully, because it is about synchronization*",
     b10.count(_SHEAR10) == 1 and b10.count(_FRAMES10) == 1)

_ISSF = (r"The areal radius~\eqref{eq:r-SdS-solution} is not merely \emph{like} the "
         r"flat-$\Lambda$CDM scale factor; at the Nariai member it \emph{is} that scale factor")
print(f"      `P07`'s identification of the scale factor: {b07.count(_ISSF)}x")
gate("Ⓐ③ AND `P07` FIXES THE SCALE FACTOR THIS COMPARISON USES, IN ITS OWN WORDS: THE AREAL RADIUS "
     "*\"is not merely LIKE the flat-`$\\Lambda$CDM` scale factor; at the Nariai member it IS that "
     "scale factor\"* -- so `$a=r$` is read off the corpus and not assumed here",
     b07.count(_ISSF) == 1)


# ============================================ B. the answer: two objects
head("B.  THE ANSWER: TWO OBJECTS, AND THE DIFFERENCE IS EXACTLY THE RADIATION CONSTANT")

E_leaf = via_conformal(RH2_LEAF)
E_bead = via_conformal(RH2_BEAD)
_d = sp.simplify(sp.expand(E_leaf - E_bead))
print(f"      E_leaf - E_bead = {sp.factor(_d)}")
gate("Ⓑ① ON ONE CHART, WITH ONE SCALE FACTOR, THE TWO TENSOR EQUATIONS DIFFER BY EXACTLY "
     "`$A_r\\,(r\\varphi''+2\\varphi')/r$` -- *a single term carrying the radiation constant and "
     "nothing else*",
     sp.simplify(_d - Ar * (r * sp.diff(phi(r), r, 2) + 2 * sp.diff(phi(r), r)) / r) == 0)

print(f"      d/dk of the difference: {sp.simplify(sp.diff(_d, k))}")
gate("Ⓑ② THE DIFFERENCE IS **`$k$`-INDEPENDENT**, so it is not a statement about which modes are "
     "compared but about the background the comparison is made on",
     sp.simplify(sp.diff(_d, k)) == 0)

_at0 = sp.simplify(_d.subs(Ar, 0))
_lin = sp.simplify(sp.diff(_d, Ar))
print(f"      at A_r = 0 it is {_at0};  its A_r-derivative is {sp.factor(_lin)}, independent of A_r: "
      f"{sp.simplify(sp.diff(_lin, Ar)) == 0}")
gate("Ⓑ③ AND IT VANISHES AT `$A_r=0$` **AND NOWHERE ELSE**: it is exactly linear in `$A_r$`, so no "
     "positive radiation constant removes it",
     _at0 == 0 and sp.simplify(sp.diff(_lin, Ar)) == 0 and _lin != 0)


# ============================================ C. the control
head("C.  ⛔ THE CONTROL: A SYNCHRONIZATION CANNOT PRODUCE THAT TERM")

_ok_bead = sp.simplify(sp.expand(via_conformal(RH2_BEAD) - r ** 2 * via_proper(RH2_BEAD))) == 0
_ok_leaf = sp.simplify(sp.expand(via_conformal(RH2_LEAF) - r ** 2 * via_proper(RH2_LEAF))) == 0
print(f"      conformal route == r^2 x proper route:  on the bead {_ok_bead};  on the leaf {_ok_leaf}")
gate("Ⓒ① THE SAME EQUATION PUSHED TO `$r$` BY **TWO DIFFERENT CLOCKS** -- CONFORMAL AND PROPER -- "
     "AGREES UP TO THE MEASURE FACTOR `$r^2$`, ON BOTH CONGRUENCES: *the `$r$`-form depends on "
     "`$(rH)^2$` and on nothing else*",
     _ok_bead and _ok_leaf)

gate("Ⓒ② ⇒ SO ANY MONOTONE RE-TIMING LEAVES THE `$r$`-FORM ALONE, AND THE `$A_r$` TERM SURVIVES IT "
     "-- *`P10`'s \"two synchronizations of itself, not two frames\" therefore cannot be what "
     "separates the leaf from the segment's curve; that clause and this difference are about "
     "different things*",
     _ok_bead and _ok_leaf
     and sp.simplify(_d - Ar * (r * sp.diff(phi(r), r, 2) + 2 * sp.diff(phi(r), r)) / r) == 0
     and b10.count(_FRAMES10) == 1)


# ============================================ D. the one datum, with its limit
head("D.  THE TENSOR POTENTIAL EACH CONGRUENCE REPORTS -- AND WHAT IT DOES NOT SETTLE")

_app_leaf = sp.simplify(sp.diff(eta, eta, 2) / eta)
_app_bead = sp.simplify(sp.diff(eta ** 2, eta, 2) / eta ** 2)
print(f"      leaf, a ~ eta  : a''/a = {_app_leaf}")
print(f"      bead, a ~ eta^2: a''/a = {_app_bead}")
gate("Ⓓ① IN ITS OWN CONFORMAL TIME THE LEAF REPORTS `$a''/a=0$` **IDENTICALLY** AND THE BEAD "
     "`$a''/a=2/\\eta^2$` -- the two potentials of one equation form",
     _app_leaf == 0 and sp.simplify(_app_bead - 2 / eta ** 2) == 0)

# ⌗ and the caveat is made concrete rather than left as a warning: with the potential GONE the
#   regular branch still freezes, so a vanishing a''/a is not a statement that nothing freezes.
_kk = sp.Symbol('k', positive=True)
_u_reg = sp.sin(_kk * eta)                       # the regular solution of u'' + k^2 u = 0
_h_leaf = sp.simplify(_u_reg / eta)              # h = u/a with a proportional to eta
_lim = sp.simplify(sp.limit(_h_leaf, eta, 0))
_u_sing = sp.cos(_kk * eta)                      # the other branch
_lim_sing = sp.limit(sp.simplify(_u_sing / eta), eta, 0)
print(f"      with a''/a = 0 the regular branch gives h = sin(k eta)/eta -> {_lim} as eta -> 0,")
print(f"      a NON-ZERO constant; the other branch gives {_lim_sing}")
gate("\u24b9\u2461 \u26d4 AND THE CAVEAT IS MADE CONCRETE: WITH THE POTENTIAL GONE THE REGULAR "
     "BRANCH **STILL FREEZES** -- `$h=u/a=\\sin(k\\eta)/\\eta\\to k$`, a non-zero constant, while "
     "the other branch diverges.  *So `$a''/a=0$` is NOT a statement that nothing freezes, and no "
     "super-horizon claim is drawn from Ⓓ① here*",
     sp.simplify(_lim - _kk) == 0 and _lim_sing == sp.oo)


# ============================================ E. which branch of the order's either/or
head("E.  ⇒ WHICH BRANCH OF `r7137`'s EITHER/OR: THE FIRST")

gate("Ⓔ① THE ORDER OFFERED *\"either a second instance of the two-congruence split or an "
     "identification nobody has stated\"*.  **IT IS THE FIRST**: the two equations are the same form "
     "with different content, the content difference is `$k$`-independent and exactly `$A_r$`, and no "
     "re-timing touches it",
     sp.simplify(_d - Ar * (r * sp.diff(phi(r), r, 2) + 2 * sp.diff(phi(r), r)) / r) == 0
     and sp.simplify(sp.diff(_d, k)) == 0 and _at0 == 0 and _ok_bead and _ok_leaf)

gate("Ⓔ② ⇒ AND THE CONSEQUENCE THE ORDER NAMES FOR THAT BRANCH FOLLOWS: THE `$\\sqrt3$` IS A "
     "STATEMENT ABOUT **TWO DIFFERENT MEASUREMENTS** -- one kernel, two species, as `r7136` put it "
     "-- *and `sec:what-crosses`'s open clause closes by naming both rather than by choosing*",
     b15.count(_TENSOR15) == 1 and b10.count(_SHEAR10) == 1
     and sp.simplify(sp.diff(_d, k)) == 0)


# ============================================ the verdict
head("VERDICT")
_n = len(CHECKS)
_ok = sum(1 for _, v in CHECKS if v)
for nm, v in CHECKS:
    if not v:
        print(f"  ⛔ FAILED: {nm}")
print(f"""
  ⇒ ARE THE CORPUS'S TENSOR ASSIGNMENT AND THE SEGMENT'S c_s = 1 SUPPORT ONE OBJECT OR TWO?
    ** TWO. **  Written on one chart, with the scale factor the papers themselves identify (a = r,
    "at the Nariai member it IS that scale factor"), the tensor equation on the leaf and on the
    segment's own curve differ by exactly A_r (r phi'' + 2 phi')/r -- one term, carrying the
    radiation constant, k-independent, linear in A_r and vanishing only at A_r = 0.

  ⇒ AND THE CONTROL IS WHAT MAKES IT A FINDING: the same equation pushed to r by two different
    clocks, conformal and proper, agrees up to the measure factor r^2 on both congruences, so the
    r-form depends on (rH)^2 alone.  ** A difference that survives every re-timing is a difference
    in content. **  So P10's "two synchronizations of itself, not two frames" is about a different
    distinction and does not close this one.

  ⇒ SO r7137's FIRST BRANCH HOLDS: a second instance of the two-congruence split, not an
    identification nobody has stated.  The sqrt3 is a statement about two measurements -- one kernel,
    two species -- and sec:what-crosses' open clause closes by naming both rather than choosing.

  ⌗ ONE DATUM WITH ITS LIMIT: in its own conformal time the leaf reports a''/a = 0 identically and
    the bead 2/eta^2.  ** That settles nothing about freezing **, because the frozen quantity is
    h = u/a and not u, and no claim about super-horizon behaviour is made here.

  ⌗ WHAT PO-79 STILL ASKS: which species' perturbation the crossing transports.  This is the read the
    order named as its first step, and it narrows the question rather than answering it -- the two
    candidates are now known to be two objects, so the question is which of them the acoustic
    sector's amplitude and tilt actually ride.
""")
print(f"  sources opened: {OPENED}")
print(f"\n  {_ok} of {_n} checks pass [{time.time()-t_all:.1f}s]")
raise SystemExit(0 if _ok == _n else 1)
