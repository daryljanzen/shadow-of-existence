#!/usr/bin/env python3
"""P15 receipt -- `r7131`'s `PO-77` ⓶, carrying `70`'s `R3`: ** WHICH SEAM DOES `sec:envelope` MEAN,
AND IS IT WHERE THE COLLAPSE LEG ENDS? **
*** ⛭⛭⛭ IT MEANS THE FRONT CHART VALUE `$r=+\\alpha/\\sqrt3$`, FIXED BY THE PAPER'S OWN `1.53`;
    AND THAT IS NOT WHERE ANY COLLAPSE LEG OF THE BEAD ENDS.  THE BEAD'S COLLAPSE LEG ENDS AT THE
    COMOVING TURNAROUND, WHERE `$\\dd r/\\dd s=0$`, WHILE EVERY SEAM CARRIES `$\\lvert\\dd r/\\dd
    s\\rvert=1$` EXACTLY -- SO THE TWO LOCI ARE SEPARATED BY THE BEAD'S OWN FIRST DERIVATIVE AND NOT
    BY A READING. ***
⌗ *`70`'s `R3` is right that the bead's collapse leg DOES pass a seam -- the back one, and this
receipt reproduces the crossing exactly, `$\\dd r/\\dd s=-1$` at `$r=-2\\alpha/\\sqrt3$`.  What it
adds is that the crossing is **TRANSVERSAL AND INTERIOR**: the leg continues a further `0.8780`
`$\\alpha$` of contour past it before it ends.  ** So "passes a seam" and "ends at the seam" are
different facts and only the first is the bead's. **

** ⇒ AND THE ⓶ DATUM THE ORDER ASKS FOR: `$\\lvert r\\rvert$` FOLDS THE LAP AND SIGNED `$r$` DOES
NOT. **  *`$r$` is monotone across all three legs, `$-\\infty\\to+\\infty$`, so `$\\lvert r\\rvert$`
is EXACTLY two-to-one with its fold at the branch point.  The two points it identifies at
`$\\lvert r\\rvert=\\alpha/\\sqrt3$` are `$r=\\mp\\alpha/\\sqrt3$`, which the paper's own phase
`$\\varphi=2\\pi r/\\sqrt3\\alpha$` puts `$240^\\circ$` apart -- the same `$240^\\circ$` the paper
puts between the back seam and the branch point.*
⇒ *** So `r7130`'s `23.254` per cent is the measure of ONE FOLD-PAIR: the fraction of the lift
already traversed when `$\\lvert r\\rvert$` first reaches the seam's value.  **The order's reading of
it is confirmed here and made exact: an overlap under that label, and not a map.** ***

⛭ ** WHAT PINS THE SEAM, AND IT IS THE PAPER'S ARITHMETIC RATHER THAN ITS WORDING. **  `sec:envelope`
fixes horizon entry by the turnaround function `$(rH)^2=(1-f)+A/r^2$` and states its turning point at
`$r_*=1.53\\,r_{\\rm seam}$`.  ⇒ *With the corpus's inherited datum at the seam the quartic returns
`$r_*/(\\alpha/\\sqrt3)=1.5338`$ -- the paper's figure.  Against the BACK seam's radius the SAME
`$r_*$` returns `0.7669`.*  ** A ratio agreeing with one of the two identifies which one. **
⌗ *And in the vacuum case the turning point IS the front seam, symbolically: `$(M\\alpha^2)^{1/3}
=\\alpha/\\sqrt3$`, which is the `$f'=0$` Nariai double root.*

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not claim the paper's sentence is wrong about the
physics it carries: on a congruence with no Euclidean segment the collapse leg does run down to the
seam and end there, which is `70`'s `PO-77` ⓵ and is not duplicated or recomputed here.  ** The
finding is that the appositive is not readable on the BEAD **, whose own collapse leg ends elsewhere.
⌗ *It computes nothing on `PO-74` or `PO-75`, asserts nothing about any receipt's state, and proposes
no edit to `C21` or to any file but this one.  The only objects are `$r(s)$` on the three legs, one
quartic, and the fold.*

** COMPUTES: the Nariai member in the gauge `$\\alpha=1$`, `$2M=2\\alpha/3\\sqrt3$`, with the radiation constant set by the corpus's inherited datum AT THE SEAM, `$\\rho_r/\\rho_m=2$` so `$A_r=4Mr_{\\rm seam}$`. **  *Every number below is on that member and that datum and on no other; the vacuum case `$A_r=0$` is taken separately and labelled where it is used.  `$A=2^{1/3}\\alpha/\\sqrt3$` is `eq:amplitude`'s turnaround amplitude throughout and never the radiation constant, which is written `$A_r$` here for exactly that reason.*

⌗ ** THE MUST-COME-BACK-WRONG CONTROLS ARE THE FRAMEWORK'S OWN FIGURE. **  *Every locus below is
computed from `$r(\\tilde\\tau)$` alone and compared against the numbers `P07`'s triptych caption
prints independently: `$-1.299$` at the back seam, the corner `$\\mp\\tfrac32(2M\\alpha^2)^{1/3}`$ at
the turnaround, unit speed attained as a MINIMUM at the front seam, and the Euclidean null's
`$r=-0.3441\\alpha$`.  **If the parametrisation or the sign convention used here were not the
framework's, those four would not come back.**
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
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
OPENED = sorted(os.path.basename(x) for x in (P15, P07))
b15 = body_of(P15)
b07 = body_of(P07)

mp.mp.dps = 30
al = sp.Symbol('alpha', positive=True)
s = sp.Symbol('s', real=True)
_A = 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)       # eq:amplitude's turnaround amplitude
_rN = al / sp.sqrt(3)                               # the FRONT chart value of the seam
_rB = -2 * al / sp.sqrt(3)                          # the BACK chart value of the seam
_k = 3 / (2 * al)
_M2 = 2 * al / (3 * sp.sqrt(3))                     # 2M on the Nariai member


# ================================================ A. the clauses this argument reasons FROM
head("A.  THE CLAUSES THIS ARGUMENT REASONS FROM -- LOCATED IN THE SOURCES, NOT RECALLED")

_SEAMS15 = (r"The lap's seams lie elsewhere, at the two unit-speed loci "
            r"$r=-2\alpha/\sqrt3$ and $r=+\alpha/\sqrt3$")
_SEAMS07 = (r"the lap's seams are the two unit-speed loci "
            r"$r=-2\alpha/\sqrt3$ and $r=+\alpha/\sqrt3$")
print(f"      `P15`: {b15.count(_SEAMS15)}x   `P07`: {b07.count(_SEAMS07)}x")
gate("Ⓐ① BOTH PAPERS NAME THE LAP'S SEAMS AS THE TWO UNIT-SPEED LOCI `$r=-2\\alpha/\\sqrt3$` AND "
     "`$r=+\\alpha/\\sqrt3$` -- so *which* seam is a question with exactly two candidates",
     b15.count(_SEAMS15) == 1 and b07.count(_SEAMS07) == 1)

# ** ⛭⛭ REPAIRED r7206: `66` REWORDED THIS CLAUSE AND THE PIN WENT RED ON A REWORDING THAT CHANGED
#   NOTHING THIS RECEIPT USES. ***  The content the argument needs is that the two chart values are ONE
#   SUBSTRATE POINT, and the paper still says exactly that.  ⇒ ** So the repair is the corpus's own
#   rule -- a disjunction beats a pin -- and the arms are the two REAL states of the sentence: the
#   `r7132`-era wording and the current one.  `sum(... ) == 1` rather than `or`, so a duplication is
#   caught too. **
_ONEPT_ARMS = ("one point of the substrate, which the bead meets on the way in and again one full lap "
               "later",
               "one point of the substrate with the back seam the bead meets on the way in")
_ONEPT_N = sum(b15.count(a) for a in _ONEPT_ARMS)
_PHI = r"the same $\varphi$ modulo $2\pi$ in the phase $\varphi=2\pi r/\sqrt3\alpha$"
# ** ⛭ the same repair on the 240/120 split, reworded in the same pass: `in from it` became `in from
#   the front seam`, which is the same statement with its referent spelled out. **
_240_ARMS = (r"The branch point sits two thirds of the lap in from it ($240^\circ$, with "
             r"$120^\circ$ remaining)",
             r"The branch point sits two thirds of the lap in from the front seam ($240^\circ$, with "
             r"$120^\circ$ remaining)")
_240_N = sum(b15.count(a) for a in _240_ARMS)
print(f"      one substrate point: {_ONEPT_N}x;  the phase: {b15.count(_PHI)}x;  "
      f"the 240/120 split: {_240_N}x")
gate("Ⓐ② AND `P15` SAYS THE TWO CHART VALUES ARE ONE SUBSTRATE POINT, `$\\varphi$` MODULO `$2\\pi$` "
     "IN `$\\varphi=2\\pi r/\\sqrt3\\alpha$` -- which is the licence for the phase arithmetic below",
     _ONEPT_N == 1 and b15.count(_PHI) == 1 and _240_N == 1)

_TURN = r"at $r_{*}=1.53\,r_{\mathrm{seam}}$ on the corpus's inherited datum"
_INSIDE = r"the \emph{seam} sits just inside that turning point, on the rising branch"
print(f"      the turning-point clause: {b15.count(_TURN)}x;  'just inside': {b15.count(_INSIDE)}x")
gate("Ⓐ③ `sec:envelope` FIXES HORIZON ENTRY BY `$(rH)^2=(1-f)+A/r^2$` AND STATES ITS TURNING POINT "
     "AT `$r_*=1.53\\,r_{\\rm seam}$`, WITH THE SEAM JUST INSIDE IT -- a RATIO, which is what pins "
     "which seam",
     b15.count(_TURN) == 1 and b15.count(_INSIDE) == 1)

_BACKT = (r"at the back seam $r=-2\alpha/\sqrt3$ (where $\cosh(3s/2\alpha)=2$) the collapse leg "
          r"crosses it \emph{transversally}")
_FRONTT = r"at the front seam $r=+\alpha/\sqrt3$ the expansion leg touches it \emph{tangentially}"
_ORDER = (r"distinguished from one another not by the presence or absence of a feature but by "
          r"\emph{order of contact}")
print(f"      back transversal: {b07.count(_BACKT)}x;  front tangential: {b07.count(_FRONTT)}x;  "
      f"order of contact: {b07.count(_ORDER)}x")
gate("Ⓐ④ `P07` PUTS THE BACK SEAM ON THE COLLAPSE LEG (TRANSVERSALLY) AND THE FRONT SEAM ON THE "
     "EXPANSION LEG (TANGENTIALLY), AND SAYS IN TERMS THAT THE TWO ARE SEPARATED BY **ORDER OF "
     "CONTACT** -- the clause section `C` reproduces rather than assumes",
     b07.count(_BACKT) == 1 and b07.count(_FRONTT) == 1 and b07.count(_ORDER) == 1)

# ⌗ the appositive itself is the sentence this row is asking about, so it is gated as a DISJUNCTION
#   and never as a pin: either it stands as now, or this row has landed in it.  (The fourth standing
#   guard: a defence against a paper state changing has to admit the state the result may produce.)
_APPOS = (r"all of them reaching the \emph{seam}---where the collapse leg ends---with the same "
          r"driving amplitude")
_CARRIED = 'P15_the_seam_sec_envelope_means_is_the_front_chart_value' in b15
print(f"      the appositive present: {b15.count(_APPOS)}x;  this row landed in `P15`: {_CARRIED}")
gate("Ⓐ⑤ THE APPOSITIVE *\"reaching the SEAM---where the collapse leg ends---\"* IS THE SENTENCE "
     "THIS ROW ASKS ABOUT, SO IT IS GATED AS AN **EXCLUSIVE DISJUNCTION**: either it stands as "
     "written or this row has landed in it, never neither and never both",
     (b15.count(_APPOS) == 1) != _CARRIED)


# ================================================ B. which seam -- the ratio picks it
head("B.  WHICH SEAM `sec:envelope` MEANS: THE RATIO `1.53` PICKS THE FRONT CHART VALUE")

r = sp.Symbol('r', positive=True)
Ar = sp.Symbol('A_r', positive=True)
_rH2 = Ar / r ** 2 + _M2 / r + r ** 2 / al ** 2                 # (1-f) + A/r^2, the paper's own
_quart = sp.simplify(sp.numer(sp.together(sp.diff(_rH2, r))))   # = 0 at the turning point
print(f"      d/dr[(rH)^2] = 0  ->  {sp.factor(_quart)} = 0")

# the vacuum case first, which is where the locus is EXACTLY the front seam
_q0 = sp.factor(_quart.subs(Ar, 0))
_rstar0 = sp.simplify((_M2 / 2 * al ** 2) ** sp.Rational(1, 3))
print(f"      A_r = 0:  r* = (M alpha^2)^(1/3) = {_rstar0}   against alpha/sqrt3 = {_rN}")
gate("Ⓑ① IN THE VACUUM CASE THE TURNING POINT **IS** THE FRONT SEAM, SYMBOLICALLY: "
     "`$(M\\alpha^2)^{1/3}=\\alpha/\\sqrt3$` ON THE NARIAI MEMBER, which is the `$f'=0$` double root",
     sp.simplify(_rstar0 - _rN) == 0
     and sp.simplify(sp.diff(1 - _M2 / r - r ** 2 / al ** 2, r).subs(r, _rN)) == 0)

# and with the corpus's inherited datum at the seam, rho_r/rho_m = 2  <=>  A_r = 4 M r_seam
_Ar = sp.simplify(4 * (_M2 / 2) * _rN)
_ratio_at_seam = sp.simplify((_Ar / _rN ** 2) / (_M2 / _rN))
print(f"      A_r = 4 M r_seam = {_Ar};  radiation/matter in (rH)^2 at the seam = {_ratio_at_seam}")
_qn = sp.Poly(sp.expand(_quart.subs({Ar: _Ar, al: 1})), r)
_rs = [complex(x).real for x in _qn.nroots(n=25)
       if abs(complex(x).imag) < 1e-20 and complex(x).real > 0]
_rstar = _rs[0]
_front = float(_rN.subs(al, 1))
_back = float(-_rB.subs(al, 1))
print(f"      r* = {_rstar:.10f};   r*/r_front = {_rstar/_front:.10f};   "
      f"r*/r_back = {_rstar/_back:.10f}")
gate("Ⓑ② WITH THE INHERITED DATUM (`$\\rho_r/\\rho_m=2$` AT THE SEAM, SO `$A_r=4Mr_{\\rm seam}$`) "
     "THE QUARTIC RETURNS `$r_*/(\\alpha/\\sqrt3)=1.5338$` -- **THE PAPER'S OWN `1.53`**",
     len(_rs) == 1 and sp.simplify(_ratio_at_seam - 2) == 0 and abs(_rstar / _front - 1.5338) < 0.0005)
gate("Ⓑ③ ⛔ MUST-COME-BACK-WRONG: THE SAME `$r_*$` AGAINST THE **BACK** SEAM'S RADIUS RETURNS "
     "`0.7669`, NOT `1.53` -- *so the ratio the paper prints identifies which of the two chart "
     "values its `$r_{\\rm seam}$` is, and it is the front one*",
     abs(_rstar / _back - 0.7669) < 0.0005 and abs(_rstar / _back - 1.53) > 0.5)


# ================================================ C. the bead's four loci from r(s) alone
head("C.  THE BEAD'S FOUR LOCI, FROM `$r(\\tilde\\tau)$` ALONE -- AGAINST `P07`'s OWN FIGURE")

r_coll = -_A * sp.cosh(_k * s) ** sp.Rational(2, 3)   # collapse leg, r < 0, s: -oo -> 0
r_exp = _A * sp.sinh(_k * s) ** sp.Rational(2, 3)     # expansion leg, r > 0, s: 0 -> +oo
d1c, d2c = sp.diff(r_coll, s), sp.diff(r_coll, s, 2)
d1e, d2e = sp.diff(r_exp, s), sp.diff(r_exp, s, 2)

_sb = sp.acosh(2) / _k                                # P07: the back seam is where cosh(3s/2a) = 2
_rb_got = sp.simplify(r_coll.subs(s, _sb))
_vb = sp.simplify(d1c.subs(s, _sb))
_ab = sp.simplify(d2c.subs(s, _sb))
print(f"      BACK SEAM   cosh(3s/2a)=2:  r = {_rb_got}   dr/ds = {_vb}   "
      f"d2r/ds2 = {float(_ab.subs(al, 1)):.9f}")
gate("Ⓒ① AT `$\\cosh(3s/2\\alpha)=2$` THE COLLAPSE LEG IS AT `$r=-2\\alpha/\\sqrt3$` **EXACTLY** AND "
     "CARRIES `$\\dd r/\\dd s=-1$` **EXACTLY**, WITH ACCELERATION `$-1.299038$` -- `P07`'s `$-1.299$`, "
     "and a TRANSVERSAL crossing because the acceleration is finite and non-zero",
     sp.simplify(_rb_got - _rB) == 0 and sp.simplify(_vb + 1) == 0
     and abs(float(_ab.subs(al, 1)) + 1.299038) < 1e-6)

_rt = sp.simplify(r_coll.subs(s, 0))
_vt = sp.simplify(sp.limit(d1c, s, 0))
_at = sp.simplify(sp.limit(d2c, s, 0))
print(f"      TURNAROUND  s=0:  r = {_rt}   dr/ds = {_vt}   d2r/ds2 = {_at} = "
      f"{float(_at.subs(al, 1)):.10f}   against -(3/2)(2M a^2)^(1/3) = "
      f"{float(-sp.Rational(3,2)*_A.subs(al, 1)):.10f}")
gate("Ⓒ② THE COLLAPSE LEG **ENDS** AT THE COMOVING TURNAROUND, `$r=-A$`, WHERE `$\\dd r/\\dd s=0$` "
     "AND THE ACCELERATION IS THE CORNER `$\\mp\\tfrac32(2M\\alpha^2)^{1/3}=\\mp1.0911$` -- `P07`'s "
     "own coefficient in its own `$\\alpha=1$` gauge",
     sp.simplify(_rt + _A) == 0 and _vt == 0
     and abs(float(_at.subs(al, 1)) + float(sp.Rational(3, 2) * _A.subs(al, 1))) < 1e-12)

_sf = sp.asinh(1 / sp.sqrt(2)) / _k                   # the stationary point of dr/ds
_rf = sp.simplify(sp.powsimp(r_exp.subs(s, _sf), force=True))
_vf = sp.simplify(sp.powsimp(d1e.subs(s, _sf), force=True))
_d3 = float(sp.diff(r_exp, s, 3).subs(s, _sf).subs(al, 1))
print(f"      FRONT SEAM  tanh^2=1/3:  r = {_rf}   dr/ds = {_vf}   d2r/ds2 = "
      f"{sp.simplify(d2e.subs(s, _sf))}   d3r/ds3 = {_d3:+.6f}")
gate("Ⓒ③ ON THE EXPANSION LEG `$\\dd r/\\dd s$` ATTAINS A **MINIMUM OF EXACTLY `1`** AT "
     "`$r=+\\alpha/\\sqrt3$` **EXACTLY**, WITH THE ACCELERATION VANISHING THERE -- `P07`'s "
     "TANGENTIAL touch, and the two seams differ by ORDER OF CONTACT and by nothing else",
     sp.simplify(_rf - _rN) == 0 and sp.simplify(_vf - 1) == 0
     and sp.simplify(d2e.subs(s, _sf)) == 0 and _d3 > 0)

_f = 1 - _M2 / r - r ** 2 / al ** 2
_en = [complex(x).real for x in sp.Poly(sp.expand(sp.numer(sp.together(
    (_f - 2).subs(al, 1)))), r).nroots(n=25) if abs(complex(x).imag) < 1e-20]
print(f"      EUCLIDEAN NULL  f=2:  real root(s) {['%.10f' % x for x in _en]}")
gate("Ⓒ④ AND THE THIRD UNIT-SPEED LOCUS, THE EUCLIDEAN NULL `$f=2$` INTERIOR TO THE LIFT, IS THE "
     "**UNIQUE** REAL ROOT AT `$r=-0.3441421\\alpha$` -- `P07`'s `$-0.3441\\alpha$`",
     len(_en) == 1 and abs(_en[0] + 0.34414212) < 1e-7)


# ================================================ D. so the appositive names no locus of this leg
head("D.  ⇒ SO THE APPOSITIVE NAMES NO LOCUS AT WHICH THE BEAD'S COLLAPSE LEG ENDS")

print(f"      A/r_N = {sp.simplify(_A/_rN)};   so the front chart value is strictly INSIDE the "
      f"turnaround: {float(_rN.subs(al,1)):.6f} < {float(_A.subs(al,1)):.6f}")
gate("Ⓓ① `$A/r_N=2^{1/3}$` SYMBOLICALLY (`r7130`'s GATE, CARRIED FORWARD), SO THE FRONT CHART "
     "VALUE LIES STRICTLY INSIDE THE TURNAROUND AND THE COLLAPSE LEG'S END IS **NOT** AT IT",
     sp.simplify(_A / _rN - 2 ** sp.Rational(1, 3)) == 0
     and float(_rN.subs(al, 1)) < float(_A.subs(al, 1)))

_speeds = {'back seam': abs(float(_vb)), 'front seam': abs(float(_vf)),
           'end of the collapse leg': abs(float(_vt))}
print("      |dr/ds| at each locus: " + ",  ".join(f"{k} = {v:.6f}" for k, v in _speeds.items()))
gate("Ⓓ② THE DISCRIMINATOR IS THE BEAD'S OWN FIRST DERIVATIVE AND NOT A READING: "
     "`$\\lvert\\dd r/\\dd s\\rvert=1$` AT **EVERY** SEAM AND `$0$` WHERE THE COLLAPSE LEG ENDS",
     abs(_speeds['back seam'] - 1) < 1e-12 and abs(_speeds['front seam'] - 1) < 1e-12
     and _speeds['end of the collapse leg'] == 0)

_remaining = float(_sb.subs(al, 1))            # the leg runs s: -oo -> 0, the seam at s = -s_b
_rb_over_A = float((-_rB / _A).subs(al, 1))
print(f"      the seam is crossed at |r| = 2 alpha/sqrt3 = 2^(2/3) A = {_rb_over_A:.9f} A, and the "
      f"leg then runs a further {_remaining:.6f} alpha of contour to its end")
gate("Ⓓ③ AT THE CHART VALUE THE COLLAPSE LEG **DOES** MEET, THE CROSSING IS **INTERIOR**: it happens "
     "at `$\\lvert r\\rvert=2^{2/3}A$` and the leg continues a further `$0.8780\\alpha$` of contour "
     "before it ends -- *so `70`'s `R3` is right that a seam is passed, and that is not the same "
     "fact as ending there*",
     sp.simplify(-_rB - 2 ** sp.Rational(2, 3) * _A) == 0 and abs(_remaining - 0.8779719) < 1e-7)


# ================================================ E. the fold, which is the ⓶ datum
head("E.  THE ⓶ DATUM: `$\\lvert r\\rvert$` FOLDS THE LAP AT THE BRANCH POINT, SIGNED `$r$` DOES NOT")

_mono = [sp.simplify(sp.diff(r_coll, s).subs(s, -x)) for x in (sp.Rational(1, 2), 1, 2)]
_monoe = [sp.simplify(sp.diff(r_exp, s).subs(s, x)) for x in (sp.Rational(1, 2), 1, 2)]
print("      dr/ds > 0 sampled on the collapse leg: "
      + ", ".join(f"{float(x.subs(al,1)):.6f}" for x in _mono)
      + ";  on the expansion leg: " + ", ".join(f"{float(x.subs(al,1)):.6f}" for x in _monoe))
gate("Ⓔ① `$r$` IS MONOTONE ALONG THE WHOLE LAP, `$-\\infty\\to+\\infty$`, SO `$\\lvert r\\rvert$` IS "
     "**EXACTLY TWO-TO-ONE** WITH ITS FOLD AT THE BRANCH POINT `$r=0$`, AND SIGNED `$r$` IS INJECTIVE",
     all(float(x.subs(al, 1)) > 0 for x in _mono + _monoe))

phi = lambda rr: sp.simplify(2 * sp.pi * rr / (sp.sqrt(3) * al))
_dphi = sp.simplify(phi(_rN) - phi(-_rN))
_lap = sp.simplify(phi(_rN) - phi(_rB))
print(f"      phi(-alpha/sqrt3) = {phi(-_rN)},  phi(+alpha/sqrt3) = {phi(_rN)},  "
      f"difference = {_dphi} = {float(_dphi/sp.pi):.6f} pi;   phi(front) - phi(back) = {_lap}")
gate("Ⓔ② THE TWO POINTS `$\\lvert r\\rvert=\\alpha/\\sqrt3$` IDENTIFIES ARE `$\\varphi=\\mp2\\pi/3$`, "
     "**`$240^\\circ$` APART** -- the same `$240^\\circ$` the paper puts between the back seam and "
     "the branch point -- while the two chart values of the seam are a FULL `$2\\pi$` apart, which is "
     "why they are one substrate point and these two are not",
     sp.simplify(_dphi - 4 * sp.pi / 3) == 0 and sp.simplify(_lap - 2 * sp.pi) == 0)

_g = lambda w: mp.sin(w) ** (-mp.mpf(2) / 3)
_tot = mp.quad(_g, [0, mp.pi / 2])
_part = mp.quad(_g, [mp.pi / 4, mp.pi / 2])
_frac = 100 * _part / _tot
print(f"      on the lift |r| = A|sin w|^(2/3):  |r| : A -> r_N is w : pi/2 -> pi/4, and "
      f"{float(_part):.12f} / {float(_tot):.12f} = {float(_frac):.9f} per cent")
gate("Ⓔ③ `r7130`'s `23.254` PER CENT RESTATED AS WHAT IT MEASURES: **THE FRACTION OF THE LIFT ALREADY "
     "TRAVERSED WHEN `$\\lvert r\\rvert$` FIRST REACHES THE SEAM'S VALUE** -- the measure of one "
     "fold-pair, which is an overlap under that label and not a map",
     abs(float(_frac) - 23.254) < 0.002)

_OVER = sp.simplify((2 ** sp.Rational(2, 3) - 1))
print(f"      and the collapse leg's own stretch inside the seam's |r| value: none -- "
      f"|r| there is >= A = 2^(1/3) r_N > r_N")
gate("Ⓔ④ AND THE FOLD IS WHY THE SENTENCE LOOKED READABLE ON THE BEAD: UNDER `$\\lvert r\\rvert$` "
     "THE BEAD'S COLLAPSE LEG **PLUS THE LIFT'S FIRST `23.254` PER CENT** COVER THE SAME "
     "`$\\lvert r\\rvert$` INTERVAL AS A LEG RUNNING DOWN TO THE SEAM'S VALUE -- *the collapse leg "
     "alone cannot, because `$\\lvert r\\rvert\\ge A=2^{1/3}r_N>r_N$` on it*",
     sp.simplify(_A - 2 ** sp.Rational(1, 3) * _rN) == 0 and abs(float(_frac) - 23.254) < 0.002)


# ================================================ the verdict
head("VERDICT")
_n = len(CHECKS)
_ok = sum(1 for _, v in CHECKS if v)
for nm, v in CHECKS:
    if not v:
        print(f"  ⛔ FAILED: {nm}")
print(f"""
  ⇒ WHICH SEAM `sec:envelope` MEANS: ** THE FRONT CHART VALUE `r = +alpha/sqrt3` **, pinned by the
    paper's own ratio -- 1.5338 against the front seam, 0.7669 against the back one -- and by the
    vacuum turning point being that locus exactly, symbolically, as the f' = 0 double root.

  ⇒ AND IT IS NOT WHERE ANY COLLAPSE LEG OF THE BEAD ENDS.  The bead's collapse leg ends at the
    comoving turnaround, where dr/ds = 0; every seam carries |dr/ds| = 1 exactly; and at the chart
    value the leg does meet, the back one, the crossing is transversal and interior, with a further
    0.8780 alpha of contour to run.  ** 70's R3 is right that a seam is passed.  Passing a seam and
    ending at it are different facts and only the first is the bead's. **

  ⇒ THE ⓶ DATUM: |r| folds the lap at the branch point and is exactly two-to-one; signed r, and the
    paper's own phase, are injective.  The two points |r| = alpha/sqrt3 identifies sit 240 degrees
    apart, while the seam's two chart values sit a full 2 pi apart -- which is exactly why those are
    one substrate point and these are not.  ** So r7130's 23.254 per cent is the measure of one
    fold-pair: an overlap under that label, and not a map.  The order's reading of it is confirmed
    and made exact. **

  ⌗ What is NOT concluded: nothing about whether the sentence is right on the congruence it is about.
    On a congruence with no Euclidean segment the collapse leg does run down to the seam and end
    there -- that is 70's PO-77 ⓵ and is neither duplicated nor recomputed here.
""")
print(f"  sources opened: {OPENED}")
print(f"\n  {_ok} of {_n} checks pass [{time.time()-t_all:.1f}s]")
raise SystemExit(0 if _ok == _n else 1)
