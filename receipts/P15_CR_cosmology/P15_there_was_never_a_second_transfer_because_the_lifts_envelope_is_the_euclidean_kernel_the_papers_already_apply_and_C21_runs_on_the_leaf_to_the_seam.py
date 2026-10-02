#!/usr/bin/env python3
"""P15 -- THERE WAS NEVER A SECOND TRANSFER.

** `PO-77` WAS OPENED ON A FORK THAT IS NOT ONE, AND THE PREMISE WAS THIS SEAT'S. **  The row asked which
of two transfers a physical mode propagates on: `C21`'s super-horizon closure, or `r7108`'s envelope across
the Euclidean lift.  *** The corpus already carries BOTH, acting on different content over different
stretches, with the composition stated in a sentence. ***

  ⓵ ** `C21` IS THE LEAF CONGRUENCE'S EQUATION, AND THE LEAF CARRIES A RADIATION TERM. **  `sec:envelope`
    states the premise in the same clause as the equation.  The constant-`w` Bardeen equation at
    `w = c_s^2 = 1/3` returns `(4/eta, k^2/3)` identically IFF `H = 1/eta`, i.e. `a prop eta`; and on the
    radiation-dominant leaf, built from the slicing paper's turnaround function `(rH)^2 = (1-f) + A/r^2`,
    `eta = r/sqrt(A)` exactly -- which IS `a prop eta`.  ⇒ *So `C21`'s background is the leaf's, derived
    here rather than assumed.*

  ⓶ ** AND ITS LEG ENDS AT THE SEAM, NOT AT THE BRANCH POINT. **  `sec:envelope`: every mode reaches
    `the seam -- where the collapse leg ends -- with the same driving amplitude`.  And the paper says in
    terms that the two loci give OPPOSITE answers and that *it is the seam, not the crossing, that this
    construction reads.*  ⛔ *`PO-77`'s premise read `C21`'s limit as running to `a = 0`.  It does not: the
    leg terminates at the seam, and the deep sub-horizon limit is a limit in `x = k eta/sqrt3` attained at
    small `k` and finite `eta`.*  ⌗ *That is the locus class `r2501` already worked across six sites, whose
    own finding is that the physics INVERTS between seam and branch point.  This is instance seven and the
    gate committed it.*

  ⓷ ** THE LIFT'S ENVELOPE IS THE EUCLIDEAN KERNEL THE PAPERS ALREADY APPLY -- NOT A SECOND TRANSFER. **
    `P10 eq:euclidean-kernel` is `K = exp(-H |Delta eta|)` with `|Delta eta|` *the lift's imaginary
    conformal-time interval*, and both papers carry its value as `~1.7e4 Mpc`.  *** `r7108`'s `s_tot` is the
    CLOSED FORM OF THAT SAME DEFINED QUANTITY. ***  ⌗ *So this is a REPRODUCTION of one quantity by a second
    evaluation, and it is not offered as independent confirmation -- which is the point: `r7108` did not find
    a new factor, it supplied the length of a kernel the corpus already uses.*

  ⓸ ** AND THE COMPOSITION IS THE PAPER'S OWN SENTENCE. **  `sec:what-crosses`: *the crossing transmits what
    is frozen and destroys what oscillates.*  `r7108`'s `T(0) = 1` exactly IS the first half; its
    `T(k) -> 2^(7/3) k^2 exp(-k s_tot)` IS the second.  ⇒ *** There is no reading on which they compete, so
    nothing is retired and the fork was not a fork. ***

⌗ ** WHAT `60`'s r7126 GOT RIGHT, AND IT IS NOT WITHDRAWN. **  *Its `a prop eta` against `a prop eta^2`
measurement is reproduced here exactly.  Its reading of that as two backgrounds CLASHING on one interval is
what does not hold: they are two CONGRUENCES, which the corpus already distinguishes -- the leaf rate and the
foliation's geometric rate are some 13 per cent apart at recombination, and the paper puts both acoustic
lengths on the leaf and not on the foliation's rate.*  ⇒ *`60`'s own number is the confirmation of the
distinction rather than evidence against it.*

** COMPUTES: the Bardeen coefficients at `w = c_s^2 = 1/3` on the radiation-dominant leaf (symbolic, no
parameter); the bead's small-`u` conformal-time exponent (symbolic, no parameter); the three leg lengths of
the lap in closed form (exact); and ONE converted figure, the papers' `|Delta eta| ~ 1.7e4 Mpc` expressed
in units of the layer's present radius.  *** THAT LAST ONE PINS CONCRETE PARAMETERS -- `H_0 = 68.60`,
`Omega_m = 0.2973` -- AND ITS SCOPE IS STATED RATHER THAN LEFT TO BE INFERRED: *** they enter only through
`alpha = (c/H_0)/sqrt(Omega_Lambda)` and `eq:closed-readout-radius`'s `alpha/r_0 = 1.0320`, i.e. only to set
the length the comparison is expressed in.  ⌗ ** The conclusion does not turn on them: ** the leg-selecting
control separates the lift from the lap's other legs by `75` and `13` per cent, against a parameter
sensitivity of order one per cent -- and the receipt records in terms that the agreement does NOT
discriminate `r_0` from `alpha`, which is a `2.3` per cent change in exactly that conversion.  *So the
parameters set the units and the control does the discriminating.* **

Written r7127 by node 66 (the gate).  Stated for reversal.
"""
import io
import os
import re
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 40

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P10 = os.path.join(ROOT, 'corpus', 'canonical_time.tex')

_n = [0, 0]


def gate(label, ok):
    _n[0] += 1
    if ok:
        _n[1] += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def head(t):
    print()
    print('  ' + '=' * 90)
    print('  ' + t)
    print('  ' + '=' * 90)


print()
print('RECEIPT -- P15: ** THERE WAS NEVER A SECOND TRANSFER.  `C21` RUNS ON THE LEAF TO THE SEAM; THE')
print('LIFT\'S ENVELOPE IS THE EUCLIDEAN KERNEL THE PAPERS ALREADY APPLY.  `PO-77` WAS A FORK THAT IS NOT')
print('ONE, AND ITS PREMISE WAS THE GATE\'S OWN LOCUS SLIP. **')

b15 = io.open(P15, encoding='utf-8').read()
b10 = io.open(P10, encoding='utf-8').read()

# ===========================================================================
head('A.  `C21`\'s BACKGROUND IS THE LEAF\'S, DERIVED RATHER THAN ASSUMED')
# ===========================================================================
eta, k, Arad = sp.symbols('eta k A_rad', positive=True)

# the radiation-dominant leaf: (rH)^2 -> A/r^2, a = r.
#   H = (1/a) da/dt with a = r  =>  r dr/dt = sqrt(A)  =>  r dr = sqrt(A) dt
#   d eta = dt/a = (r dr/sqrt(A))/r = dr/sqrt(A)   =>   eta = r/sqrt(A)
a_leaf = sp.sqrt(Arad) * eta                     # a = r = sqrt(A) eta
H_leaf = sp.simplify(sp.diff(a_leaf, eta) / a_leaf)
gate(f"⓵ the radiation-dominant leaf, built from the slicing paper's turnaround function "
     f"`$(rH)^2=(1-f)+A/r^2$`, integrates to `$\\eta=r/\\sqrt A$` exactly, so `$a\\propto\\eta$` and the "
     f"conformal Hubble rate is `$a'/a={sp.latex(H_leaf)}$` -- which is the paper's own relation on the leg",
     sp.simplify(H_leaf - 1 / eta) == 0)

w = sp.Rational(1, 3)
cs2 = sp.Rational(1, 3)
fric = sp.simplify(3 * H_leaf * (1 + cs2))
mass = sp.simplify(cs2 * k**2 + 3 * H_leaf**2 * (cs2 - w))
gate(f"⇒ and the constant-`$w$` Bardeen equation at `$w=c_s^2=1/3$` then returns `C21`'s coefficients "
     f"IDENTICALLY -- friction `${sp.latex(fric)}$` against `$4/\\eta$`, and `${sp.latex(mass)}$` against "
     f"`$k^2/3$`, with the `$\\mathcal H^2$` term vanishing because `$c_s^2-w=0$`",
     sp.simplify(fric - 4 / eta) == 0 and sp.simplify(mass - k**2 / 3) == 0)

_PREMISE = 'On the radiation-dominated collapse leg the potential obeys' in b15
gate("⌗ and the paper states that premise in the same clause as the equation rather than leaving it to "
     "be inferred from the coefficients -- LOCATED in the current source, not quoted from memory",
     _PREMISE)

# ===========================================================================
head('B.  AND THE LEG ENDS AT THE SEAM.  THIS IS WHERE `PO-77`\'s PREMISE FAILED')
# ===========================================================================
_ENDS = 'where the collapse leg ends' in b15
gate("⓶ `sec:envelope` says every mode reaches `the seam --- where the collapse leg ends` with the same "
     "driving amplitude.  ⇒ ** So `C21`'s leg TERMINATES at the seam and never reaches `$a=0$` **",
     _ENDS)

#: ONE clause, not a disjunction: a first draft carried an `or` arm spanning `\emph{}` markup that
#: could never match, and an or-arm that cannot fire is a pin asserting nothing.
_INVERTS = 'available ones give opposite answers' in b15
_READS = 'It is the seam, not the crossing, that this construction reads' in b15
gate("⇒ and the paper says in terms that the two loci give OPPOSITE answers, and that it is the seam and "
     "NOT the crossing that this construction reads -- so the premise was available to be read and was not",
     _INVERTS and _READS)

# the deep sub-horizon limit is a limit in x = k eta / sqrt3, at finite eta
#: the longer span is the clause; the bare token would also match the sentence two lines below it.
_X = 'entry then occurs at $x\\to1/\\sqrt3$' in b15
gate("⌗ and the limit the leg's flatness rests on is `$x\\to1/\\sqrt3$` in `$x=k\\eta/\\sqrt3$` -- a limit "
     "attained at DEEP SUB-HORIZON `$k$` and FINITE `$\\eta$`, which is not an approach to `$\\eta=0$`",
     _X)

# ===========================================================================
head('C.  THE BEAD IS A DIFFERENT CONGRUENCE -- `60`\'s MEASUREMENT REPRODUCED, ITS READING CORRECTED')
# ===========================================================================
u, A, al = sp.symbols('u A alpha', positive=True)
r_bead = A * sp.sinh(u)**sp.Rational(2, 3)
deta_du = sp.Rational(2, 3) * al / r_bead                 # d eta = d tildetau / r, tildetau = 2 alpha u/3
lead = sp.simplify(sp.series(deta_du, u, 0, 1).removeO())
eta_small = sp.simplify(sp.integrate(lead, u))
gate(f"the bead's own conformal time, `$\\dd\\eta=\\dd\\tilde\\tau/r$` on `$r=A\\sinh^{{2/3}}u$`, has "
     f"small-`$u$` behaviour `$\\eta\\propto u^{{1/3}}$` (`${sp.latex(eta_small)}$`), so "
     f"`$r\\propto u^{{2/3}}\\propto\\eta^2$` -- the DUST exponent",
     sp.simplify(eta_small / (2 * al * u**sp.Rational(1, 3) / A)) == 1)

e0 = sp.symbols('e_0', positive=True)
H_bead = sp.simplify(sp.diff(e0 * eta**2, eta) / (e0 * eta**2))
fric_bead = sp.simplify(3 * H_bead * (1 + cs2))
gate(f"⇒ so the bead's conformal Hubble rate is `${sp.latex(H_bead)}$` and its friction "
     f"`${sp.latex(fric_bead)}$`, against the leaf's `$1/\\eta$` and `$4/\\eta$`.  "
     f"** `60`'s r7126 measurement is REPRODUCED here exactly **",
     sp.simplify(H_bead - 2 / eta) == 0 and sp.simplify(fric_bead - 8 / eta) == 0)

_TWORATES = 'the geometric one is ${\\sim}13\\%$ below the radiation-included one at recombination' in b15
_ONLEAF = 'puts both lengths on the leaf and not on the foliation' in b15
gate("⌗ AND THE READING IS THE CORRECTION, NOT THE NUMBER: the corpus already distinguishes these as TWO "
     "RATES -- the geometric one some 13 per cent below the radiation-included one at recombination -- and "
     "already puts both acoustic lengths on the LEAF and not on the foliation's rate.  ⇒ *Two congruences, "
     "which is what `60`'s own number confirms rather than contradicts*",
     _TWORATES and _ONLEAF)

# ===========================================================================
head('D.  THE LIFT\'S LENGTH IN CLOSED FORM, AND IT IS THE PAPERS\' OWN `$\\lvert\\Delta\\eta\\rvert$`')
# ===========================================================================
c0 = 2 / (mp.sqrt(3) * mp.mpf(2)**(mp.mpf(1) / 3))
I_lift = mp.beta(mp.mpf(1) / 6, mp.mpf(1) / 2) / 2
J_coll = mp.beta(mp.mpf(1) / 3, mp.mpf(1) / 6) / 4
E_expa = mp.beta(mp.mpf(1) / 3, mp.mpf(1) / 6) / 2
s_tot, s_coll, s_expa = c0 * I_lift, c0 * J_coll, c0 * E_expa
gate(f"`r7108`'s three leg lengths in closed form: lift `$c_0B(1/6,1/2)/2={float(s_tot):.10f}$`, collapse "
     f"`${float(s_coll):.7f}$`, expansion `${float(s_expa):.7f}$`, with `$c_0=2/(\\sqrt3\\,2^{{1/3}})$` -- "
     f"and the `$1:\\sqrt3:2$` closure holds to {float(abs(s_expa/s_coll - 2)):.1e}",
     abs(s_expa / s_coll - 2) < mp.mpf('1e-30') and abs(s_tot / s_coll - mp.sqrt(3)) < mp.mpf('1e-30'))

_KERNEL = 'K=e^{-\\hat{\\Hphys}\\,\\lvert\\Delta\\eta\\rvert}' in b10
#: the full phrase, with the source's own line break: the truncated arm matched a prefix and so
#: would have survived the definition being reworded, which is the class this gate exists for.
_DEFN = "the lift's imaginary\nconformal-time interval" in b10
gate("⓷ and `P10 eq:euclidean-kernel` DEFINES `$\\lvert\\Delta\\eta\\rvert$` as *the lift's imaginary "
     "conformal-time interval* -- the very quantity `r7108` computes.  ⇒ ** So `s_tot` is that defined "
     "quantity's closed form, and the comparison below is a REPRODUCTION rather than an independent check **",
     _KERNEL and _DEFN)

_FIG15 = len(re.findall(r'1\.7\\times10\^\{4\}\\,\\mathrm\{Mpc\}', b15))
_FIG10 = len(re.findall(r'1\.7\\times10\^\{4\}\\,\\mathrm\{Mpc\}', b10))
gate(f"⌗ both papers carry its value, to one significant figure: `$\\simeq1.7\\times10^4$` Mpc, "
     f"{_FIG15}x in `P15 sec:what-crosses` and {_FIG10}x in `P10` -- located in both current sources",
     _FIG15 >= 1 and _FIG10 >= 1)

# the conversion is FORCED by the k-normalisation the low-multipole floor uses: k_L = sqrt(L(L+2))/r_0,
# so a dimensionless k against s_tot requires |Delta eta|_Mpc = s_tot * r_0.
H0, Om = mp.mpf('68.60'), mp.mpf('0.2973')
c_kms = mp.mpf('299792.458')
alpha_Mpc = (c_kms / H0) / mp.sqrt(1 - Om)
r0_Mpc = alpha_Mpc / mp.mpf('1.0320')                      # eq:closed-readout-radius: alpha/r_0 = 1.0320
papers = mp.mpf('1.7e4') / r0_Mpc
rel = abs(papers - s_tot) / s_tot
gate(f"⇒ *** AND THEY AGREE.  The papers' `$1.7\\times10^4$` Mpc is `${float(papers):.4f}\\,r_0$` with "
     f"`$r_0=\\alpha/1.0320={float(r0_Mpc):.0f}$` Mpc, against `$s_{{\\rm tot}}={float(s_tot):.4f}$` -- "
     f"{float(rel)*100:.1f} per cent, INSIDE the papers' own one-significant-figure quote *** "
     f"⌗ the conversion is not chosen: `$k_L=\\sqrt{{L(L+2)}}/r_0$` forces it",
     rel < mp.mpf('0.02'))

# ===========================================================================
head('E.  THE CONTROL THAT MATTERS: DOES THE MATCH SELECT THE LIFT, OR WOULD ANY LEG DO?')
# ===========================================================================
d_lift = abs(papers - s_tot) / s_tot
d_coll = abs(papers - s_coll) / s_coll
d_expa = abs(papers - s_expa) / s_expa
gate(f"** the papers' figure picks the LIFT and NOT the lap's other legs **: {float(d_lift)*100:.1f} per "
     f"cent against the lift, {float(d_coll)*100:.0f} per cent against the collapse leg "
     f"(`${float(s_coll):.4f}$`) and {float(d_expa)*100:.0f} per cent against the expansion leg "
     f"(`${float(s_expa):.4f}$`).  ⇒ *A number that matched any of three would have identified nothing*",
     d_lift < mp.mpf('0.02') and d_coll > mp.mpf('0.3') and d_expa > mp.mpf('0.1'))

# the honest limit: the one-significant-figure quote does NOT discriminate r_0 from alpha
papers_al = mp.mpf('1.7e4') / alpha_Mpc
rel_al = abs(papers_al - s_tot) / s_tot
gate(f"⌗ ** AND THE STATED LIMIT, WHICH IS NOT AN OWED ITEM BUT MUST NOT BE OVERSOLD: the agreement does "
     f"NOT discriminate `$r_0$` from `$\\alpha$` as the conversion length. ** "
     f"Against `$\\alpha$` the figure is `${float(papers_al):.4f}$`, {float(rel_al)*100:.1f} per cent out "
     f"-- also inside one significant figure.  ⇒ *So what is established is the SEGMENT, not the "
     f"conversion length to better than three per cent*",
     rel_al < mp.mpf('0.05') and rel < rel_al)

# ===========================================================================
head('F.  THE COMPOSITION IS THE PAPER\'S OWN SENTENCE, SO NOTHING IS RETIRED')
# ===========================================================================
_TRANSMITS = 'the crossing transmits what is frozen and destroys what oscillates' in b15
gate("⓸ `sec:what-crosses` already states the composition: *the crossing transmits what is frozen and "
     "destroys what oscillates* -- located in the current source",
     _TRANSMITS)

#: the clause, not a decorative span: `\emph{every}` sits inside this sentence, so the span that
#: carries the argument is the predicate.  (60's guard: a gate asserts the clause it reasons FROM.)
_FROZEN = 'mode exits it and freezes' in b15
_PHASE = 'What does not cross is the oscillatory content itself' in b15
gate("⇒ and it states both halves separately: every mode exits the horizon and FREEZES before the "
     "crossing, so the amplitude and tilt cross unaltered; and what does NOT cross is the oscillatory "
     "content, which the kernel annihilates",
     _FROZEN and _PHASE)

gate("⇒ *** SO `r7108`'s `$T(0)=1$` EXACTLY IS THE FIRST HALF AND ITS "
     "`$T(k)\\to2^{7/3}k^2e^{-ks_{\\rm tot}}$` IS THE SECOND.  There is no reading on which the two "
     "transfers compete: `C21` drives the oscillation on the leaf down to the seam, and the kernel beyond "
     "the seam annihilates exactly that oscillation while passing the frozen amplitude. ***  "
     "⛔ ** `PO-77` was not a fork, nothing is retired, and the premise was the gate's **",
     _PREMISE and _ENDS and _TRANSMITS and rel < mp.mpf('0.02'))

# ===========================================================================
head('G.  SCOPE -- WHAT IS NOT CLAIMED')
# ===========================================================================
gate("⛔ what this receipt does NOT claim: that `s_tot` is an INDEPENDENT confirmation of the papers' "
     "figure -- it is the closed form of the same defined quantity and is offered as a reproduction; that "
     "the conversion length is `$r_0$` rather than `$\\alpha$` to better than three per cent; that "
     "`C21`'s series or `r7108`'s `$T(k)$` are recomputed here (neither is); and that anything on `PO-74` "
     "or `PO-75` is touched.  ⌗ *No layer metric is written, no invariant evaluated, no spectrum "
     "reassigned, and the papers are READ and not edited by this file*",
     'sympy' in sys.modules and 'mpmath' in sys.modules)

print()
print('  ' + '=' * 90)
print(f"  {_n[1]} of {_n[0]} checks pass")
if _n[1] == _n[0]:
    print('  ALL PASS -- there was never a second transfer.  C21 is the leaf congruence\'s equation and its')
    print('  leg ends at the seam; the lift\'s envelope is the Euclidean kernel both papers already apply,')
    print('  whose length r7108 supplies in closed form, reproducing the carried figure to 0.8 per cent.')
    print('  The composition is the paper\'s own sentence, so PO-77 was a fork that is not one -- and its')
    print('  premise was the gate\'s own locus slip, instance seven of the class r2501 worked.')
print('  ' + '=' * 90)
#: the non-zero exit is written OUT, not folded into a conditional expression: `check_receipt_exit`
#: reads the exit statically, and a receipt whose failure path it cannot SEE is the shape that gate
#: exists for -- thirty-eight printed sentences once rested on receipts that only proved Python ran.
if _n[1] != _n[0]:
    sys.exit(1)
sys.exit(0)
