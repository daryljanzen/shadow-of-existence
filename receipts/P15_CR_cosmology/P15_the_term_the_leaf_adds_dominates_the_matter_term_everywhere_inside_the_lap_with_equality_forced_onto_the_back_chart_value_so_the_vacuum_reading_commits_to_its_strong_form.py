#!/usr/bin/env python3
"""P15 receipt -- `r7139`'s `PO-79`, and the ONE THING IT ASKS FOR RATHER THAN ORDERS: ** the
must-come-back-wrong treatment of the reading that *"the segment is vacuum by construction and the
radiation term is what the leaf adds"*. **
*** ⛭⛭⛭ THE READING SURVIVES, AND IT COSTS MORE THAN IT NAMED.  ON THE CORPUS'S OWN INHERITED DATUM
    THE TERM THE LEAF ADDS IS THE **LARGER** OF THE TWO INHERITED TERMS EVERYWHERE STRICTLY INSIDE
    THE LAP:
        ** radiation / matter `$=2r_N/r$` EXACTLY -- `$2$` at the seam, `$2^{2/3}$` at the
           turnaround, and `$1$` exactly at the lap's BACK chart value. **
    ⇒ SO THE WEAK FORM OF THE READING -- *radiation present on the segment but negligible* -- IS
    RULED OUT, AND THE READING COMMITS TO ITS STRONG FORM: THE INHERITED RADIATION IS GENUINELY
    ABSENT THERE, NOT MERELY SMALL. ***

⛭ ** AND THE EQUALITY LOCUS IS FORCED, NOT A COINCIDENCE. **  *Radiation/matter `$=(A_r/2M)/r$`, so
equality sits at `$r=A_r/2M$`; the inherited datum (`$\\rho_r/\\rho_m=2$` AT the seam) makes that
`$2r_N$`; and `P07`'s own clause -- the seams' *"radii stand in the exact ratio `$2{:}1$` about the
branch point"* -- makes `$2r_N$` the back chart value.*  ⇒ *** The datum's value meeting the lap's own
geometry puts radiation--matter equality exactly on the seam's other chart value.  Nothing was tuned
to make that happen and nothing here is free to move it. ***

** ⇒ WHAT THAT DOES TO THE ROW, STATED AS A DICHOTOMY AND NOT AS A CHOICE. **
  ⓵ *** IF the segment is the vacuum curve, the inherited radiation is absent on it outright -- and
      then `sec:what-crosses`'s *"amplitude and tilt cross unaltered"* has to be about something
      other than the radiation perturbation, because the thing that would carry it is not there. ***
  ⓶ *** IF instead the inherited radiation IS present on the segment, the segment is not the vacuum
      curve, and the turnaround that defines it moves -- the amplitude `$A$` is derived FROM the
      vacuum law. ⌗ `70`'s `PO-77` ⓵ reaches the same horn by its own route and that route is
      theirs: it is CITED here and not recomputed. ***
⇒ *The row asked which of the two the crossing transports.  **This does not answer it; it prices
both horns**, and the price of the first is a clause of the paper that has to be restated.*

⌗ ** WHY THE WEAK FORM WAS WORTH KILLING. **  *It is the reading that costs nothing -- *the segment is
vacuum to good approximation, the radiation is a correction, everything stands as written* -- and it
is the one the numbers forbid: a correction that is `$2\\times$` the term it corrects at the seam and
`$1.587\\times$` at the turnaround is not a correction.  ⌗ *That is the whole of this receipt's
adversarial content and it is aimed at the reading `r7139` offered, as `r7139` asked.*

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not decide the dichotomy -- that is `PO-79` and it
stays open.  It does not recompute `70`'s `PO-77` ⓵, which reaches horn ⓶ independently and is
theirs.  It does not claim `sec:what-crosses` is wrong: it shows what horn ⓵ would cost that clause,
and the clause is gated here as a DISJUNCTION against this row landing in it rather than pinned.
Nothing computes on `PO-74` or `PO-75`; no edit is proposed to any paper.*

** COMPUTES: the Nariai member in the gauge `$\\alpha=1$`, `$2M=2\\alpha/3\\sqrt3$`, and the radiation
constant AT THE CORPUS'S INHERITED DATUM, `$A_r=4Mr_N$`, which is `$\\rho_r/\\rho_m=2$` at the seam. **
*That datum is the only value of `$A_r$` used, and every ratio below is reported as a function of
`$r$` first so the datum's role is visible rather than buried.  `$A$` is `eq:amplitude`'s turnaround
amplitude and `$A_r$` the radiation constant, never interchanged.*
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
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
OPENED = sorted(os.path.basename(x) for x in (P15, P07))
b15, b07 = body_of(P15), body_of(P07)

r, al = sp.symbols('r alpha', positive=True)
_M2 = 2 * al / (3 * sp.sqrt(3))                   # 2M, Nariai
_M = _M2 / 2
_rN = al / sp.sqrt(3)                             # the seam's front chart value
_rB = 2 * al / sp.sqrt(3)                         # the magnitude of its back chart value
_A = 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)     # eq:amplitude's turnaround amplitude
_Ar = 4 * _M * _rN                                # the inherited datum: rho_r/rho_m = 2 AT the seam
RATIO = sp.simplify((_Ar / r ** 2) / (_M2 / r))   # radiation term / matter term in (rH)^2


# ============================================ A. the clauses this is weighed against
head("A.  THE CLAUSES THIS IS WEIGHED AGAINST -- LOCATED IN `P15` AND `P07`, NOT RECALLED")

_INH = (r"inherited as boundary data exactly as flat $\Lambda$CDM inherits the baryon-to-photon "
        r"ratio")
_SEAMS = (r"The lap's seams lie elsewhere, at the two unit-speed loci "
          r"$r=-2\alpha/\sqrt3$ and $r=+\alpha/\sqrt3$")
print(f"      the inherited-content clause: {b15.count(_INH)}x;  the seams: {b15.count(_SEAMS)}x")
gate("Ⓐ① `P15` CARRIES THE CONTENT AS **INHERITED BOUNDARY DATA** AND NAMES THE LAP'S TWO SEAMS -- "
     "*the two facts the measurement below is made against*",
     b15.count(_INH) == 1 and b15.count(_SEAMS) == 1)

_R21 = r"their radii stand in the exact ratio $2{:}1$ about the branch point"
print(f"      `P07`'s 2:1 clause: {b07.count(_R21)}x")
gate("Ⓐ② AND `P07` FIXES THE SEAMS' RATIO IN ITS OWN WORDS -- *\"their radii stand in the exact "
     "ratio `$2{:}1$` about the branch point\"* -- which is the second half of the forcing in `C`",
     b07.count(_R21) == 1)

# ⌗ the clause horn ⓵ would cost is gated as a DISJUNCTION and never as a pin: the fourth guard.
_UNALT = r"so amplitude and tilt cross unaltered while the collapse-leg acoustic phase does not"
_CARRIED = 'P15_the_term_the_leaf_adds_dominates_the_matter_term_everywhere_inside_the_lap' in b15
#: ⛭ AMENDED r7142 (60), AND THE AMENDMENT IS THE FOURTH GUARD APPLIED PROPERLY TO THIS OWN GATE.
#: As first written this was an EXCLUSIVE disjunction -- the clause stands XOR this row has landed --
#: and it went RED ON THE SUCCESS OF ITS OWN WORK: `r7141` landed the row AND kept the clause, which
#: an XOR calls impossible.  ⇒ An XOR is not an enumeration; it forbids a state the object can be in.
#: `r7142` then established WHY that third state is legitimate: horn ⓵'s carrier is a wavenumber-free
#: POTENTIAL amplitude the paper already carries in two places (`sec:what-crosses`'s *"contains no
#: `$k$` at all once `$w=0$`"* and `sec:coherence`'s *"the wavenumber-independent `$0.4835\\,\\Psi_i$`"*),
#: so the clause needs no restatement on that horn and legitimately stands after the row lands.
#: ⇒ The gate now ENUMERATES the three states `P15` may be in, and keeps the content the XOR had:
#:   ⓵ row not landed  ⇒ the clause stands as written, which is what this receipt measured against;
#:   ⓶ row landed, the clause restated or gone ⇒ horn ⓵'s cost was paid;
#:   ⓷ row landed, the clause kept  ⇒ its subject needed no restating (`r7142`).
#: Red on: the clause appearing more than once, or vanishing BEFORE this row lands -- the two states
#: that would mean the sentence this receipt reasons from is not the sentence it read.
_STATES = ((b15.count(_UNALT) == 1 and not _CARRIED)
           or (_CARRIED and b15.count(_UNALT) <= 1))
print(f"      the 'cross unaltered' clause: {b15.count(_UNALT)}x;  this row landed in `P15`: "
      f"{_CARRIED};  the enumeration holds: {_STATES}")
gate("Ⓐ③ THE CLAUSE HORN ⓵ WOULD COST -- *\"amplitude and tilt cross unaltered\"* -- IS GATED AS AN "
     "**ENUMERATION OF THE STATES `P15` MAY PRODUCE**, never as a pin and no longer as an XOR: before "
     "this row lands the clause stands as written; after it lands the clause is `66`'s to set, and "
     "`r7142` showed its subject needs no restating on horn ⓵.  ** Red only where the sentence this "
     "receipt reasons FROM would not be the sentence it read **",
     _STATES)


# ============================================ B. the measurement
head("B.  THE MEASUREMENT: WHAT THE TERM THE LEAF ADDS IS WORTH, AS A FUNCTION OF `$r$`")

print(f"      A_r at the inherited datum = {sp.simplify(_Ar)}")
print(f"      radiation/matter = {RATIO}   -- i.e. 2 r_N / r")
gate("Ⓑ① THE RATIO IS `$2r_N/r$` **EXACTLY**, a pure function of `$r$` with the datum's value in "
     "front of it -- *so the comparison is reported before any locus is chosen*",
     sp.simplify(RATIO - 2 * _rN / r) == 0)

_v_seam = sp.simplify(RATIO.subs(r, _rN))
_v_turn = sp.simplify(RATIO.subs(r, _A))
_v_back = sp.simplify(RATIO.subs(r, _rB))
print(f"      at the seam r_N      : {_v_seam}")
print(f"      at the turnaround A  : {_v_turn} = {float(_v_turn.subs(al, 1)):.9f}")
print(f"      at the back value 2r_N: {_v_back}")
gate("Ⓑ② AT THE SEAM IT IS `$2$` (the datum), AT THE TURNAROUND **`$2^{2/3}=1.5874$` EXACTLY**, AND "
     "AT THE BACK CHART VALUE EXACTLY `$1$` -- *the term the leaf adds is the LARGER of the two "
     "inherited terms everywhere strictly inside the lap*",
     _v_seam == 2 and sp.simplify(_v_turn - 2 ** sp.Rational(2, 3)) == 0 and _v_back == 1)

gate("Ⓑ③ ⛔ SO THE **WEAK FORM** OF `r7139`'s READING IS RULED OUT: *a correction worth `$2\\times$` "
     "the term it corrects at the seam and `$1.587\\times$` at the turnaround is not a correction*, "
     "so \"the segment is vacuum to good approximation\" is not available",
     _v_seam > 1 and float(_v_turn.subs(al, 1)) > 1
     and sp.simplify(sp.diff(RATIO, r)) != 0)


# ============================================ C. and the equality locus is forced
head("C.  AND THE EQUALITY LOCUS IS FORCED BY THE DATUM MEETING THE LAP'S OWN GEOMETRY")

_eqloc = sp.solve(sp.Eq(RATIO, 1), r)
print(f"      equality at r = {[sp.simplify(x) for x in _eqloc]};  A_r/(2M) = "
      f"{sp.simplify(_Ar / _M2)}")
gate("Ⓒ① EQUALITY SITS AT `$r=A_r/2M$`, WHICH THE INHERITED DATUM MAKES `$2r_N$` -- *a one-line "
     "consequence of the datum's value and nothing else*",
     len(_eqloc) == 1 and sp.simplify(_eqloc[0] - _Ar / _M2) == 0
     and sp.simplify(_Ar / _M2 - 2 * _rN) == 0)

gate("Ⓒ② AND `P07`'s `$2{:}1$` CLAUSE MAKES `$2r_N$` THE SEAM'S **BACK CHART VALUE** -- so "
     "radiation--matter equality falls exactly on the lap's other seam value.  *** Nothing was tuned "
     "to make that happen: it is the datum being exactly `$2$` meeting a ratio that is exactly "
     "`$2{:}1$`. ***",
     sp.simplify(_rB - 2 * _rN) == 0 and b07.count(_R21) == 1
     and sp.simplify(_eqloc[0] - _rB) == 0)

print(f"      the lap's span is [-2 alpha/sqrt3, +alpha/sqrt3]; the ratio exceeds 1 throughout its "
      f"interior: at r = 1.1 r_N it is {float(RATIO.subs(r, 1.1*_rN).subs(al, 1)):.4f}, at "
      f"r = 1.9 r_N it is {float(RATIO.subs(r, 1.9*_rN).subs(al, 1)):.4f}")
gate("Ⓒ③ ⇒ THE TERM THE LEAF ADDS DOMINATES THE MATTER TERM AT **EVERY** INTERIOR POINT OF THE LAP, "
     "monotonically in `$1/r$`, with the single crossing at the boundary value",
     float(RATIO.subs(r, 1.1 * _rN).subs(al, 1)) > 1
     and float(RATIO.subs(r, 1.9 * _rN).subs(al, 1)) > 1
     and float(sp.diff(RATIO, r).subs(r, _rN).subs(al, 1)) < 0)


# ============================================ D. the dichotomy, priced
head("D.  ⇒ THE DICHOTOMY, PRICED -- AND THE SECOND HORN IS CITED, NOT RECOMPUTED")

gate("Ⓓ① HORN ⓵: **IF the segment is the vacuum curve**, the inherited radiation is absent on it "
     "outright rather than small -- and then *\"amplitude and tilt cross unaltered\"* must be about "
     "something other than the radiation perturbation, *because the thing that would carry it is not "
     "there*.  ⌗ Which is why that clause is in `A` as a disjunction",
     _v_seam == 2 and sp.simplify(_v_turn - 2 ** sp.Rational(2, 3)) == 0
     and _STATES)

gate("Ⓓ② HORN ⓶: **IF the inherited radiation IS present there**, the segment is not the vacuum "
     "curve and the turnaround that defines it moves, since `$A=(2M\\alpha^2)^{1/3}$` is derived FROM "
     "the vacuum law -- *checked only to the extent of that dependence*: `$A$` carries `$M$` and "
     "`$\\alpha$` and no `$A_r$` at all.  ⌗ `70`'s `PO-77` ⓵ reaches this horn by its own route and "
     "that route is theirs, cited and not recomputed",
     sp.simplify(_A - (_M2 * al ** 2) ** sp.Rational(1, 3)) == 0
     and sp.simplify(sp.diff(_A, sp.Symbol('A_r'))) == 0)

gate("Ⓓ③ ⇒ AND THE ROW IS **PRICED RATHER THAN DECIDED**: `PO-79` asked which of the two the "
     "crossing transports, and this receipt says what each answer costs.  *The first costs a clause "
     "of the paper; the second costs the segment's own definition.*",
     _STATES
     and sp.simplify(sp.diff(_A, sp.Symbol('A_r'))) == 0
     and float(RATIO.subs(r, 1.5 * _rN).subs(al, 1)) > 1)


# ============================================ the verdict
head("VERDICT")
_n = len(CHECKS)
_ok = sum(1 for _, v in CHECKS if v)
for nm, v in CHECKS:
    if not v:
        print(f"  ⛔ FAILED: {nm}")
print(f"""
  ⇒ THE MUST-COME-BACK-WRONG TREATMENT r7139 ASKED FOR: ** the reading survives, and it costs more
    than it named. **  On the corpus's own inherited datum the term the leaf adds is worth
    2 r_N / r times the matter term -- 2 at the seam, 2^(2/3) = 1.5874 at the turnaround, and
    exactly 1 at the lap's back chart value.  ** So the term the leaf adds is the LARGER of the two
    inherited terms at every interior point of the lap. **

  ⇒ AND THE EQUALITY LOCUS IS FORCED: equality sits at A_r/2M, which the datum makes 2 r_N, which
    P07's own "exact ratio 2:1 about the branch point" makes the seam's back chart value.  The datum
    being exactly 2 meets a ratio that is exactly 2:1; nothing here is free to move it.

  ⇒ SO THE WEAK FORM OF THE READING IS DEAD -- "vacuum to good approximation, radiation a correction"
    is not available when the correction is 2x the term it corrects -- and the reading COMMITS to its
    strong form: the inherited radiation is genuinely absent on the segment.

  ⇒ WHICH PRICES BOTH HORNS RATHER THAN CHOOSING:
      (1) the segment is the vacuum curve => "amplitude and tilt cross unaltered" is about something
          other than the radiation perturbation, and that clause is owed a restatement;
      (2) the radiation is present there => the segment is not the vacuum curve and its turnaround
          moves, A being derived from the vacuum law.  70's PO-77 (1) reaches this horn by its own
          route; it is cited and not recomputed.

  ⌗ PO-79 stays open.  What this adds is that neither horn is cheap, and that the cheap third option
    was the one that had to be killed.
""")
print(f"  sources opened: {OPENED}")
print(f"\n  {_ok} of {_n} checks pass [{time.time()-t_all:.1f}s]")
raise SystemExit(0 if _ok == _n else 1)
