#!/usr/bin/env python3
"""P15 receipt -- `r7131`'s `PO-77` ⓶ CONTINUED: ** WHAT IDENTIFIES A POINT ON ONE SIDE OF THE FOLD
WITH A POINT ON THE OTHER? **
*** ⛭⛭⛭ THE PAPER ALREADY SUPPLIES THE IDENTIFICATION AND IT IS A **TRANSLATION**, NOT A REFLECTION:
    POINTS WITH THE SAME `$\\varphi$` MODULO `$2\\pi$` ARE ONE SUBSTRATE POINT, AND IN THE CHART THAT
    IS `$r\\equiv r+\\sqrt3\\alpha$` EXACTLY.  `$\\lvert r\\rvert$` IMPLEMENTS `$r\\mapsto-r$` INSTEAD,
    WHICH ** DOES NOT CARRY EITHER SEAM TO A SEAM ** -- SO IT CANNOT BE THE IDENTIFICATION. ***

⛭ ** THE ONE LINE THAT DECIDES IT. **  *The lap's seams are the two chart values `$r=-2\\alpha/\\sqrt3$`
and `$r=+\\alpha/\\sqrt3$`, which `sec:what-crosses` says are ONE substrate point, `$\\varphi$` modulo
`$2\\pi$` in `$\\varphi=2\\pi r/\\sqrt3\\alpha$`.*  ⇒ *One lap is therefore `$\\Delta\\varphi=2\\pi$`,
i.e. `$\\Delta r=\\sqrt3\\alpha$`, and `$-2\\alpha/\\sqrt3+\\sqrt3\\alpha=+\\alpha/\\sqrt3$` **exactly**.
⛔ *** The reflection sends the back seam to `$+2\\alpha/\\sqrt3$` and the front seam to
`$-\\alpha/\\sqrt3$`, ** neither of which is a seam **.  An identification that does not preserve the
only two loci the paper calls one point is not the identification. ***

** ⇒ AND THE TWO AGREE AT EXACTLY ONE POINT, WHICH IS NOT ON THE LIFT. **  `$-r=r+\\sqrt3\\alpha$` has
the single root `$r=-\\sqrt3\\alpha/2$`, whose phase is `$\\varphi=-\\pi$` **exactly** -- *the lap's
antipode to the branch point* -- and `$\\lvert r\\rvert=0.8660\\alpha>A=0.7274\\alpha$` there, so it lies
on the **collapse leg**.  ⌗ *So on the lift the two identifications disagree EVERYWHERE.*

** ⛔ WHAT THAT DOES TO `r7130`'s `23.254` PER CENT AND `r7132`'s FOLD-PAIR: THEY ARE REFLECTION
QUANTITIES AND THE LAP'S OWN CLOSURE DOES NOT ENDORSE THEM. **  *The lift is `$r:-A\\to0$`.  Its image
under the translation is `$[\\sqrt3\\alpha-A,\;\\sqrt3\\alpha]=[1.004635,\\,1.732051]\\alpha$`; under the
reflection it is `$[0,\\,A]=[0,\\,0.727416]\\alpha$`.*  ⇒ *** ** The two images are DISJOINT. ** ***
⌗ *And pulling the census's stretch `$0<r<A$` back by one lap gives
`$[-1.732051,\\,-1.004635]\\alpha$`, which is **entirely on the collapse leg** (`$\\lvert
r\\rvert>A$` throughout).  ⇒ So under the lap's own closure the census's stretch and the kernel's are
NEITHER the same stretch NOR each other's image: they are not the two sides of one identification.*

⌗ ** AND CONFORMAL TIME CANNOT CARRY IT EITHER -- BOTH CLOCKS TAKEN FROM THE ONE TURNAROUND
FUNCTION. **  *Radiation-dominant, `$\\dd\\eta/\\dd r\\to1/\\sqrt{A_r}$`, so `$\\eta=r/\\sqrt{A_r}$` and
`$a\\propto\\eta$`; matter-dominant on the vacuum curve, `$\\dd\\eta/\\dd r\\propto r^{-1/2}$`, so
`$\\eta\\propto\\sqrt r$` and `$a\\propto\\eta^2$`.*  ⇒ *The two congruences assign DIFFERENT clocks to
the same `$r$` -- the exponent pair `$(1,2)$` that `r7126` found and `r7127` re-derived -- so the
shared label is the signed areal radius and nothing else, and its identification is the translation.*

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not claim the lap is periodic in `$r$` beyond the
one closure the paper states, does not extend the translation past the pair of chart values it is
derived from, and concludes nothing about which congruence any computation in the corpus is on --
`PO-77` ⓵ is `70`'s.*  ⌗ *It withdraws nothing from `r7130` or `r7132`: the `23.254` per cent is still
the exact measure of the reflection's fold-pair, which is what it was stated to be.  **What is new is
that the reflection is not the substrate identification, so that measure answers a different question
than ⓶ asks.**  ⌗ *Nothing computes on `PO-74` or `PO-75`; no file but this one is touched.*

** COMPUTES: the Nariai member in the gauge `$\\alpha=1$`, `$2M=2\\alpha/3\\sqrt3$`, with the radiation
constant left SYMBOLIC as `$A_r$` wherever it appears. **  *`$A=2^{1/3}\\alpha/\\sqrt3$` is
`eq:amplitude`'s turnaround amplitude throughout and never the radiation constant; the two are written
`$A$` and `$A_r$` for exactly that reason.  No value of `$A_r$` is needed for any result below.*
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
OPENED = sorted(os.path.basename(x) for x in (P15,))
b15 = body_of(P15)

al = sp.Symbol('alpha', positive=True)
r = sp.Symbol('r', real=True)
Ar = sp.Symbol('A_r', positive=True)
_A = 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)       # eq:amplitude's turnaround amplitude
_rN = al / sp.sqrt(3)                               # the FRONT chart value
_rB = -2 * al / sp.sqrt(3)                          # the BACK chart value
_M2 = 2 * al / (3 * sp.sqrt(3))                     # 2M, Nariai
PHI = lambda x: 2 * sp.pi * x / (sp.sqrt(3) * al)   # sec:what-crosses' own phase
LAP = sp.sqrt(3) * al                               # one lap in the chart


# ============================================ A. the clause the whole argument turns on
head("A.  THE CLAUSE THE ARGUMENT TURNS ON -- LOCATED IN `P15`, NOT RECALLED")

_ONEPT = ("one point of the substrate, which the bead meets on the way in and again one full lap "
          "later")
_PHI = r"the same $\varphi$ modulo $2\pi$ in the phase $\varphi=2\pi r/\sqrt3\alpha$"
_SEAMS = (r"The lap's seams lie elsewhere, at the two unit-speed loci "
          r"$r=-2\alpha/\sqrt3$ and $r=+\alpha/\sqrt3$")
print(f"      one substrate point: {b15.count(_ONEPT)}x;  the phase: {b15.count(_PHI)}x;  "
      f"the seams: {b15.count(_SEAMS)}x")
gate("Ⓐ① `P15` SAYS THE TWO CHART VALUES ARE **ONE SUBSTRATE POINT**, `$\\varphi$` MODULO `$2\\pi$` IN "
     "`$\\varphi=2\\pi r/\\sqrt3\\alpha$` -- *the identification is in the corpus already; what this "
     "receipt does is read off which map it is*",
     b15.count(_ONEPT) == 1 and b15.count(_PHI) == 1 and b15.count(_SEAMS) == 1)

print(f"      phi(r + sqrt3 alpha) - phi(r) = {sp.simplify(PHI(r + LAP) - PHI(r))}")
gate("Ⓐ② SO ONE LAP IS `$\\Delta\\varphi=2\\pi$`, WHICH IN THE CHART IS `$\\Delta "
     "r=\\sqrt3\\alpha$` **EXACTLY** -- the translation is read off the paper's own phase and not "
     "chosen",
     sp.simplify(PHI(r + LAP) - PHI(r) - 2 * sp.pi) == 0)


# ============================================ B. translation yes, reflection no
head("B.  THE CLOSURE IS A TRANSLATION, AND THE REFLECTION IS NOT A CANDIDATE AT ALL")

print(f"      back + one lap = {sp.simplify(_rB + LAP)}   against the front value {_rN}")
gate("Ⓑ① THE TRANSLATION `$r\\mapsto r+\\sqrt3\\alpha$` CARRIES THE BACK CHART VALUE TO THE FRONT ONE "
     "**EXACTLY**: `$-2\\alpha/\\sqrt3+\\sqrt3\\alpha=+\\alpha/\\sqrt3$`",
     sp.simplify(_rB + LAP - _rN) == 0)

_refl_back = sp.simplify(-_rB)
_refl_front = sp.simplify(-_rN)
print(f"      reflection: back -> {_refl_back} (a seam? {sp.simplify(_refl_back - _rN) == 0});  "
      f"front -> {_refl_front} (a seam? {sp.simplify(_refl_front - _rB) == 0})")
gate("Ⓑ② ⛔ THE REFLECTION `$r\\mapsto-r$` -- WHICH IS WHAT `$\\lvert r\\rvert$` IMPLEMENTS -- CARRIES "
     "**NEITHER** SEAM TO A SEAM: the back value goes to `$+2\\alpha/\\sqrt3$` and the front to "
     "`$-\\alpha/\\sqrt3$`, *and the paper names only two seams*",
     sp.simplify(_refl_back - _rN) != 0 and sp.simplify(_refl_front - _rB) != 0
     and sp.simplify(_refl_back - _rB) != 0 and sp.simplify(_refl_front - _rN) != 0)

_agree = sp.solve(sp.Eq(-r, r + LAP), r)
_a0 = sp.simplify(_agree[0])
print(f"      -r = r + lap has the single root r = {_a0} = {float(_a0.subs(al, 1)):.10f} alpha,  "
      f"phi there = {sp.simplify(PHI(_a0))}")
gate("Ⓑ③ THE TWO MAPS AGREE AT **EXACTLY ONE POINT**, `$r=-\\sqrt3\\alpha/2$`, WHOSE PHASE IS "
     "`$\\varphi=-\\pi$` **EXACTLY** -- *the lap's antipode to the branch point*",
     len(_agree) == 1 and sp.simplify(PHI(_a0) + sp.pi) == 0)

print(f"      |r| there = {float(-_a0.subs(al, 1)):.10f} alpha  against  A = "
      f"{float(_A.subs(al, 1)):.10f} alpha  ->  on the collapse leg")
gate("Ⓑ④ AND THAT ONE POINT IS **NOT ON THE LIFT**: `$\\lvert r\\rvert=0.8660\\alpha>A$` there, which "
     "is the collapse leg -- *so along the whole of the lift the two identifications disagree*",
     float(-_a0.subs(al, 1)) > float(_A.subs(al, 1)))


# ============================================ C. what that does to the fold measurement
head("C.  ⇒ SO THE FOLD-PAIR IS A REFLECTION QUANTITY AND THE CLOSURE DOES NOT ENDORSE IT")

_lift = (sp.simplify(-_A), sp.Integer(0))                       # the lift, r : -A -> 0
_T = (sp.simplify(-_A + LAP), sp.simplify(LAP))                 # its image under the translation
_R = (sp.Integer(0), sp.simplify(_A))                           # its image under the reflection
print(f"      lift r in [{float(_lift[0].subs(al,1)):.6f}, 0]")
print(f"        translation image [{float(_T[0].subs(al,1)):.6f}, {float(_T[1].subs(al,1)):.6f}]")
print(f"        reflection  image [{float(_R[0].subs(al,1)):.6f}, {float(_R[1].subs(al,1)):.6f}]")
gate("Ⓒ① THE LIFT'S IMAGE UNDER THE TRANSLATION, `$[1.004635,\\,1.732051]\\alpha$`, IS **DISJOINT** "
     "FROM ITS IMAGE UNDER THE REFLECTION, `$[0,\\,0.727416]\\alpha$` -- *the two identifications do "
     "not merely differ in detail, they share no point at all here*",
     float(_T[0].subs(al, 1)) > float(_R[1].subs(al, 1)))

_pull = (sp.simplify(0 - LAP), sp.simplify(_A - LAP))           # 0 < r < A pulled back one lap
print(f"      the stretch 0 < r < A pulled back one lap: "
      f"[{float(_pull[0].subs(al,1)):.6f}, {float(_pull[1].subs(al,1)):.6f}]  -- |r| from "
      f"{float((LAP-_A).subs(al,1)):.6f} to {float(LAP.subs(al,1)):.6f}, all above A")
gate("Ⓒ② AND THE EXPANSION-LEG STRETCH `$0<r<A$` PULLED BACK ONE LAP LANDS **ENTIRELY ON THE COLLAPSE "
     "LEG** (`$\\lvert r\\rvert>A$` throughout) ⇒ *under the lap's own closure it is neither the lift "
     "nor the lift's image: those two stretches are not the two sides of one identification*",
     float((LAP - _A).subs(al, 1)) > float(_A.subs(al, 1)))

gate("Ⓒ③ ⌗ AND NOTHING IS WITHDRAWN FROM `r7130` OR `r7132`: `$A/r_N=2^{1/3}$` STILL HOLDS AND THE "
     "`23.254` PER CENT IS STILL THE EXACT MEASURE OF THE REFLECTION'S FOLD-PAIR -- **what changes is "
     "which question that measure answers**",
     sp.simplify(_A / _rN - 2 ** sp.Rational(1, 3)) == 0
     and sp.simplify(_A - 2 ** sp.Rational(1, 3) * _rN) == 0)


# ============================================ D. nor can conformal time carry it
head("D.  NOR CAN CONFORMAL TIME CARRY IT -- BOTH CLOCKS FROM THE ONE TURNAROUND FUNCTION")

rp = sp.Symbol('r', positive=True)
_f = 1 - _M2 / rp - rp ** 2 / al ** 2
_leaf = sp.simplify((1 - _f) + Ar / rp ** 2)      # the paper's (rH)^2 with radiation
_bead = sp.simplify(1 - _f)                       # the vacuum case
print(f"      (rH)^2 leaf = {sp.expand(_leaf)}")
print(f"      (rH)^2 bead = {sp.expand(_bead)}")
_dl = sp.limit(sp.sqrt(Ar) / (rp * sp.sqrt(_leaf)), rp, 0)
_db = sp.limit(sp.sqrt(rp) / (rp * sp.sqrt(_bead)), rp, 0)
print(f"      radiation-dominant:  sqrt(A_r) d eta/dr -> {_dl}      => eta = r/sqrt(A_r), a ~ eta^1")
print(f"      matter-dominant:     sqrt(r)   d eta/dr -> {sp.simplify(_db)}   => eta ~ sqrt(r), "
      f"a ~ eta^2")
gate("Ⓓ① FROM THE **ONE** FUNCTION `$(rH)^2=(1-f)+A_r/r^2$`: RADIATION-DOMINANT GIVES "
     "`$\\dd\\eta/\\dd r\\to1/\\sqrt{A_r}$`, SO `$\\eta=r/\\sqrt{A_r}$` AND `$a\\propto\\eta$`; "
     "MATTER-DOMINANT ON THE VACUUM CURVE GIVES `$\\eta\\propto\\sqrt r$` AND `$a\\propto\\eta^2$` "
     "-- *the exponent pair `$(1,2)$`, re-derived here from the function rather than taken*",
     sp.simplify(_dl - 1) == 0 and _db.is_finite and _db != 0)

_far = sp.limit(rp * sp.sqrt(_leaf), rp, sp.oo)
print(f"      ⛔ control: the SAME expression at large r gives r sqrt((rH)^2) -> {_far}, the "
      f"substrate term -- so neither exponent is a property of the congruence label")
gate("Ⓓ② ⛔ MUST-COME-BACK-WRONG: THE SAME EXPRESSION TAKEN AT LARGE `$r$` RETURNS THE SUBSTRATE TERM "
     "AND NOT EITHER EXPONENT -- *so `$(1,2)$` is a statement about which term dominates where, which "
     "is exactly why conformal time is not a shared label*",
     _far == sp.oo)

gate("Ⓓ③ ⇒ THEREFORE THE ONLY LABEL BOTH CONGRUENCES SHARE IS THE **SIGNED AREAL RADIUS**, AND ITS "
     "IDENTIFICATION ON THE LAP IS THE TRANSLATION `$r\\equiv r+\\sqrt3\\alpha$` -- *which is the "
     "answer ⓶ was asking for, with the reflection excluded rather than assumed away*",
     sp.simplify(_rB + LAP - _rN) == 0 and sp.simplify(PHI(LAP) - 2 * sp.pi) == 0)


# ============================================ the verdict
head("VERDICT")
_n = len(CHECKS)
_ok = sum(1 for _, v in CHECKS if v)
for nm, v in CHECKS:
    if not v:
        print(f"  ⛔ FAILED: {nm}")
print(f"""
  ⇒ WHAT IDENTIFIES A POINT ON ONE SIDE OF THE FOLD WITH A POINT ON THE OTHER:
    ** the lap's own closure, which is the TRANSLATION r = r + sqrt3 alpha (one full 2 pi of the
    paper's phase), and NOT the reflection r -> -r that |r| implements. **  The decider is one line of
    arithmetic: the translation carries the back chart value of the seam to the front one exactly,
    while the reflection carries neither seam to a seam.

  ⇒ THE TWO AGREE AT EXACTLY ONE POINT, r = -sqrt3 alpha/2, phase -pi exactly -- the lap's antipode to
    the branch point -- and it lies on the collapse leg.  ** So on the lift they disagree everywhere. **

  ⇒ AND THE CONSEQUENCE FOR THE FOLD-PAIR: the lift's image under the translation,
    [1.004635, 1.732051] alpha, is DISJOINT from its image under the reflection, [0, 0.727416] alpha;
    and the expansion-leg stretch 0 < r < A pulled back one lap lands entirely on the collapse leg.
    ** So the census's stretch and the kernel's are not the two sides of one identification. **

  ⌗ Nothing is withdrawn from r7130 or r7132.  The 23.254 per cent is still the exact measure of the
    reflection's fold-pair.  What changes is which question that measure answers -- and the guard it
    earns is that an identification has to be checked on the loci the object itself distinguishes.

  ⌗ Conformal time cannot carry the identification either: the one turnaround function gives
    eta ~ r where radiation dominates and eta ~ sqrt(r) where matter does, so the shared label is the
    signed areal radius and nothing else.
""")
print(f"  sources opened: {OPENED}")
print(f"\n  {_ok} of {_n} checks pass [{time.time()-t_all:.1f}s]")
raise SystemExit(0 if _ok == _n else 1)
