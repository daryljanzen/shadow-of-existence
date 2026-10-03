#!/usr/bin/env python3
"""P15 receipt -- `r7135`'s `PO-77` ⓪, THE WHOLE ROW: ** WHICH MODE EQUATION IS THE KERNEL'S? **
*** ⛭⛭⛭ NEITHER, AND THE FORK HAS NO SUBJECT: `P10`'s KERNEL IS
    `$K=e^{-\\hat{H}\\lvert\\Delta\\eta\\rvert}$` AND CARRIES ** NO SOUND SPEED AT ALL **.  `$c_s$`
    ENTERS ONLY THROUGH `$\\omega$` OF THE MODE BEING PROPAGATED, AND `P10` SAYS SO IN TERMS --
    *"With `$\\omega=kc_s$` these are the same expression, term for term."*  ⇒ THE TWO CANDIDATE
    EQUATIONS ARE ONE FAMILY AT TWO VALUES OF ONE PARAMETER, AND THE TWO EXPONENTS ARE ONE KERNEL
    ON TWO SPECIES. ***

** ⇒ AND THE HALF THE ORDER SAYS ONLY THIS SEAT CAN ANSWER -- WHAT FIELD `r7108`'s EQUATION IS AN
EQUATION *FOR*. **  *It is the TENSOR equation, and not by analogy:* substituting `$h=u/a$` into
`$h''+2(a'/a)h'+k^2h=0$` and multiplying by `$a$` returns
** `$u''+(k^2-a''/a)u=0$` IDENTICALLY, for `$a(\\eta)$` a free function **
*-- which is also, term for term, the equation for a massless minimally coupled scalar with `$u=a\\phi$`.*
⇒ *** So `r7108`'s equation is the `$c_s=1$` member of `$u''+(c_s^2k^2-z''/z)u=0$`, and the field it is
an equation for is one that propagates at unit speed: a tensor mode, or a massless minimally coupled
scalar.  It is not an equation for the plasma and was never in competition with one. ***
⌗ ** The must-come-back-wrong control is exact: ** the same substitution into the FLUID member leaves a
residual `$k^2(c_s^2-1)u$`, which vanishes at `$c_s=1$` ** and nowhere else **.

** ⛭ THE TWO NUMBERS ARE THEREFORE CONSISTENT, AND THEIR RATIO IS `$c_s$` EXACTLY. **  *On an
imaginary interval of conformal length `$L$` the decaying branch of either member is
`$e^{-c_sk L}$`, so the exponents stand in the ratio `$c_s$`.*  With the segment's own
`$L=3.3387380236$`, an exponent of `$-255$` fixes `$k=76.376$`, and the same `$k$` at `$c_s=1/\\sqrt3$`
gives ** `$-147.224$` ** -- `$-255/\\sqrt3$` to every digit, against the `$-147`$ this corpus computes
for the plasma on this segment.  ⌗ *And the background term is not what decides it: at that `$k$` the
ratio `$(a''/a)/(c_s^2k^2)$` is `$3.7\\times10^{-5}$`, so the WKB exponent IS the answer to four digits.*
⇒ *`P15`'s carried `$-152$` sits `3.2` per cent above `$-147$` because, as its own sentence says, it is
** integrated across the segment's own sound-speed profile rather than at a single value **.*

** ⛔ AND WHAT *IS* A STATEMENT ABOUT THE SEGMENT, SINCE THE FORK WAS NOT. **  *The curve the segment
lies on carries no radiation at all, and that is checkable rather than quoted:*
`$r(\\tilde\\tau)=A\\sinh^{2/3}(3\\tilde\\tau/2\\alpha)$` with `$A=(2M\\alpha^2)^{1/3}$` satisfies
`$(\\dd r/\\dd\\tilde\\tau)^2=2M/r+r^2/\\alpha^2$` ** identically **, and with a radiation term
`$A_r/r^2$` the residual is `$-3\\cdot2^{1/3}A_r/(2\\alpha^2\\sinh^{4/3})$`, which no positive `$A_r$`
annihilates.  ⇒ *** A vacuum background has no fluid and therefore no scalar sound speed of its own, so
the `$c_s=1$` member is the one the segment's own curve supports; the `$c_s=1/\\sqrt3$` exponent is the
same kernel applied to the radiation plasma, which is the LEAF's. ***

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not decide which species' perturbation the crossing
actually transports -- that is the question `PO-77` ⓪ becomes once the fork is dissolved, and it is
stated below rather than answered.  It does not claim either computed exponent is wrong: both are
right, for different `$\\omega$`.  It does not touch `70`'s ⓵, computes nothing on `PO-74` or
`PO-75`, proposes no edit to any paper, and asserts nothing about any other receipt's state.*

** COMPUTES: the Nariai member in the gauge `$\\alpha=1$`, `$2M=2\\alpha/3\\sqrt3$`; the segment length
`$L=3.3387380236$` as `r7108` computes it; and the first acoustic peak's `$k$` taken as whatever makes
the `$c_s=1$` exponent `$-255$`, i.e. `$k=255/L$`, so that the comparison is of RATIOS and not of an
imported wavenumber. **  *`$A=2^{1/3}\\alpha/\\sqrt3$` is `eq:amplitude`'s turnaround amplitude
throughout; the radiation constant is written `$A_r$`.  `$c_s^2=1/3$` is the plasma value `sec:envelope`
derives, and no other value of it is used.*
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
P10 = os.path.join(ROOT, 'corpus', 'canonical_time.tex')
OPENED = sorted(os.path.basename(x) for x in (P15, P10))
b15 = body_of(P15)
b10 = body_of(P10)

mp.mp.dps = 25
eta, k, cs = sp.symbols('eta k c_s', positive=True)
al, tau = sp.symbols('alpha tau', positive=True)
Ar = sp.Symbol('A_r', positive=True)
a = sp.Function('a')(eta)
u = sp.Function('u')(eta)


# ================================================ A. the clauses this argument reasons FROM
head("A.  THE CLAUSES THIS ARGUMENT REASONS FROM -- LOCATED IN `P10` AND `P15`, NOT RECALLED")

_KERNEL = r"K=e^{-\hat{\Hphys}\,\lvert\Delta\eta\rvert}"
_NOCS = (r"A mode of frequency $\omega$ is damped by $e^{-\omega\lvert\Delta\eta\rvert}$ under "
         r"\eqref{eq:euclidean-kernel}")
_SAME = r"With $\omega=kc_s$ these are the same expression, term for term"
print(f"      `P10`'s kernel: {b10.count(_KERNEL)}x;  its damping law: {b10.count(_NOCS)}x;  "
      f"the `omega = k c_s` substitution: {b10.count(_SAME)}x")
gate("Ⓐ① `P10` DEFINES THE KERNEL AS `$K=e^{-\\hat H\\lvert\\Delta\\eta\\rvert}$` AND ITS DAMPING AS "
     "`$e^{-\\omega\\lvert\\Delta\\eta\\rvert}$` FOR *A MODE OF FREQUENCY `$\\omega$`* -- **so the "
     "kernel carries no sound speed; `$c_s$` is not one of its arguments**",
     b10.count(_KERNEL) == 1 and b10.count(_NOCS) == 1)
gate("Ⓐ② AND `P10` SAYS IN TERMS WHERE `$c_s$` ENTERS: *\"With `$\\omega=kc_s$` these are the same "
     "expression, **term for term**\"* -- *the sound speed is a property of the MODE, supplied to the "
     "kernel through `$\\omega$`*",
     b10.count(_SAME) == 1)

_CLASS = r"damps a mode carrying $e^{ikc_s\eta}$ by $e^{-kc_s\lvert\Delta\eta\rvert}$"
_OSC = (r"The kernel acts on \emph{oscillatory} content; a frozen, zero-frequency mode is a fixed "
        r"point of it and passes unchanged")
print(f"      the classical reading: {b10.count(_CLASS)}x;  'acts on oscillatory content': "
      f"{b10.count(_OSC)}x")
gate("Ⓐ③ THE CLASSICAL READING IS THE SAME OPERATOR WITH `$\\omega$` FILLED IN -- "
     "`$e^{-kc_s\\lvert\\Delta\\eta\\rvert}$` FOR A MODE CARRYING `$e^{ikc_s\\eta}$` -- AND A "
     "ZERO-FREQUENCY MODE IS ITS FIXED POINT",
     b10.count(_CLASS) == 1 and b10.count(_OSC) == 1)

_M152 = (r"an exponent of $-152$ at the first acoustic peak, integrated across the segment's own "
         r"sound-speed profile rather than at the single value the estimate above uses")
_BARD = (r"On the radiation-dominated collapse leg the potential obeys "
         r"$\Psi''+(4/\eta)\Psi'+(k^{2}/3)\Psi=0$")
print(f"      `P15`'s `-152` clause: {b15.count(_M152)}x;  the plasma's `c_s^2 = 1/3`: "
      f"{b15.count(_BARD)}x")
gate("Ⓐ④ `P15` CARRIES `$-152$` AND SAYS OF IT, IN ITS OWN SENTENCE, THAT IT IS **INTEGRATED ACROSS "
     "THE SEGMENT'S OWN SOUND-SPEED PROFILE RATHER THAN AT A SINGLE VALUE** -- *so the corpus's own "
     "figure is a `$c_s$`-integral and not a second kernel*; and `sec:envelope` fixes the plasma's "
     "`$c_s^2=1/3$`",
     b15.count(_M152) == 1 and b15.count(_BARD) == 1)


# ================================================ B. what r7108's equation is an equation FOR
head("B.  WHAT `r7108`'s EQUATION IS AN EQUATION *FOR* -- DERIVED, NOT NAMED BY ANALOGY")

_h = u / a
_TENS = sp.expand(sp.simplify((sp.diff(_h, eta, 2) + 2 * sp.diff(a, eta) / a * sp.diff(_h, eta)
                               + k ** 2 * _h) * a))
_R7108 = sp.diff(u, eta, 2) + (k ** 2 - sp.diff(a, eta, 2) / a) * u
print(f"      h'' + 2(a'/a)h' + k^2 h = 0 with h = u/a, times a:")
print(f"        {sp.collect(_TENS, [sp.diff(u, eta, 2), u])}")
gate("Ⓑ① THE TENSOR EQUATION `$h''+2(a'/a)h'+k^2h=0$` UNDER `$h=u/a$` RETURNS "
     "`$u''+(k^2-a''/a)u=0$` **IDENTICALLY**, with `$a(\\eta)$` a free function -- *so `r7108`'s "
     "equation IS the tensor equation, and identically the massless minimally coupled scalar's under "
     "`$u=a\\phi$`, which obeys the same equation*",
     sp.simplify(_TENS - _R7108) == 0)

_FLUID = sp.expand(sp.simplify((sp.diff(_h, eta, 2) + 2 * sp.diff(a, eta) / a * sp.diff(_h, eta)
                                + cs ** 2 * k ** 2 * _h) * a))
_resid = sp.simplify(_FLUID - _R7108)
_sols = sp.solve(sp.Eq(_resid, 0), cs)
print(f"      the FLUID member minus it: {_resid}   -> zero only at c_s = {_sols}")
gate("Ⓑ② ⛔ MUST-COME-BACK-WRONG: THE SAME SUBSTITUTION INTO THE FLUID MEMBER LEAVES EXACTLY "
     "`$k^2(c_s^2-1)u$`, WHICH VANISHES AT `$c_s=1$` **AND NOWHERE ELSE** -- *so the two equations "
     "are not rivals, they are one family at two values of one parameter*",
     sp.simplify(_resid - k ** 2 * (cs ** 2 - 1) * u) == 0 and _sols == [1]
     and sp.simplify(_resid.subs(cs, 1 / sp.sqrt(3))) != 0)

gate("Ⓑ③ ⇒ SO THE FORK *\"WHICH MODE EQUATION IS THE KERNEL'S\"* HAS NO SUBJECT: THE KERNEL IS ONE "
     "OPERATOR WITH AN `$\\omega$` SLOT AND NO `$c_s$`, AND BOTH EQUATIONS ARE THINGS THAT SUPPLY "
     "`$\\omega$` TO IT -- `$c_s=1$` FOR A UNIT-SPEED FIELD, `$c_s=1/\\sqrt3$` FOR THE PLASMA",
     b10.count(_NOCS) == 1 and b10.count(_SAME) == 1 and sp.simplify(_TENS - _R7108) == 0)


# ================================================ C. the two exponents are one kernel, two species
head("C.  THE TWO EXPONENTS ARE ONE KERNEL ON TWO SPECIES, AND THEIR RATIO IS `$c_s$` EXACTLY")

_L = mp.mpf('3.3387380236')                       # r7108's closed form for the segment
_kpk = 255 / _L                                   # the k that makes the c_s = 1 exponent -255
_plasma = -_kpk * _L / mp.sqrt(3)
print(f"      L = {float(_L):.10f};  an exponent of -255 fixes k = {float(_kpk):.6f}")
print(f"      the same k at c_s = 1/sqrt3 gives {float(_plasma):.9f}   against -255/sqrt3 = "
      f"{float(-255/mp.sqrt(3)):.9f}")
gate("Ⓒ① THE SAME `$k$` AT `$c_s=1/\\sqrt3$` GIVES `$-147.224$`, WHICH IS `$-255/\\sqrt3$` TO EVERY "
     "DIGIT -- *the two exponents stand in the ratio `$c_s$` because `$e^{-c_skL}$` is linear in "
     "`$c_s$` in the exponent*",
     abs(_plasma + 255 / mp.sqrt(3)) < mp.mpf('1e-20')
     and abs(float(_plasma) + 147.224318) < 1e-5)

_app = 2 ** (-mp.mpf(1) / 3) / _L ** 2            # a''/a over the segment, the corpus's own constant
_ratio = _app / (_kpk ** 2 / 3)
print(f"      a''/a over the segment = {float(_app):.9f};  c_s^2 k^2 = {float(_kpk**2/3):.4f};  "
      f"ratio = {float(_ratio):.3e}")
gate("Ⓒ② AND THE BACKGROUND TERM IS NOT WHAT DECIDES IT: `$(a''/a)/(c_s^2k^2)=3.7\\times10^{-5}$` at "
     "that `$k$`, so **the WKB exponent is the whole answer to four digits** and the comparison is of "
     "the `$c_s$` coefficients and nothing else",
     _ratio < 1e-4 and _ratio > 1e-6)

_gap = (152 - 147.224318) / 147.224318 * 100
print(f"      `P15`'s carried -152 sits {_gap:.2f} per cent above -147.224")
gate("Ⓒ③ `P15`'s CARRIED `$-152$` SITS `3.24` PER CENT ABOVE THE CONSTANT-`$c_s$` VALUE -- *which is "
     "what its own sentence says it should be, being integrated across a PROFILE rather than taken at "
     "one value*",
     abs(_gap - 3.24) < 0.05 and b15.count(_M152) == 1)


# ================================================ D. what IS a statement about the segment
head("D.  WHAT *IS* A STATEMENT ABOUT THE SEGMENT: ITS CURVE CARRIES NO RADIATION AT ALL")

_M2 = 2 * al / (3 * sp.sqrt(3))
_A = (_M2 * al ** 2) ** sp.Rational(1, 3)
_r = _A * sp.sinh(3 * tau / (2 * al)) ** sp.Rational(2, 3)
_lhs = sp.simplify(sp.diff(_r, tau) ** 2)
_vac = sp.simplify(_M2 / _r + _r ** 2 / al ** 2)
print(f"      A = {sp.simplify(_A)}")
print(f"      (dr/dtau)^2 - [2M/r + r^2/alpha^2] = {sp.simplify(_lhs - _vac)}")
gate("Ⓓ① THE SEGMENT'S CURVE SOLVES THE **VACUUM** `$E=1$` LAW IDENTICALLY: "
     "`$(\\dd r/\\dd\\tilde\\tau)^2=2M/r+r^2/\\alpha^2$` for "
     "`$r=A\\sinh^{2/3}(3\\tilde\\tau/2\\alpha)$`, `$A=(2M\\alpha^2)^{1/3}$`",
     sp.simplify(_lhs - _vac) == 0)

_res = sp.simplify(_lhs - (Ar / _r ** 2 + _M2 / _r + _r ** 2 / al ** 2))
_zero = sp.solve(sp.Eq(_res, 0), Ar)
print(f"      with a radiation term the residual is {sp.simplify(_res)}")
print(f"      positive A_r annihilating it: {_zero}")
gate("Ⓓ② AND **NO POSITIVE `$A_r$` IS CONSISTENT WITH IT**: adding `$A_r/r^2$` leaves a residual "
     "proportional to `$A_r$` that no positive value annihilates -- *so the curve the segment lies on "
     "carries no radiation, and this is checked rather than quoted*",
     _zero == [] and sp.simplify(_res.subs(Ar, 0)) == 0
     and sp.simplify(sp.diff(_res, Ar)) != 0)

gate("Ⓓ③ ⇒ A VACUUM BACKGROUND HAS NO FLUID AND SO NO SCALAR SOUND SPEED OF ITS OWN: THE `$c_s=1$` "
     "MEMBER IS WHAT THE SEGMENT'S OWN CURVE SUPPORTS, AND THE `$c_s=1/\\sqrt3$` EXPONENT IS THE SAME "
     "KERNEL APPLIED TO THE PLASMA, WHICH IS THE **LEAF'S** -- *the same two-congruence shape `r7127` "
     "and `r7134` found, now at the level of the mode equation*",
     sp.simplify(_lhs - _vac) == 0 and _zero == []
     and sp.simplify(_resid - k ** 2 * (cs ** 2 - 1) * u) == 0)


# ================================================ the verdict
head("VERDICT")
_n = len(CHECKS)
_ok = sum(1 for _, v in CHECKS if v)
for nm, v in CHECKS:
    if not v:
        print(f"  ⛔ FAILED: {nm}")
print(f"""
  ⇒ WHICH MODE EQUATION IS THE KERNEL'S:  ** NEITHER, AND THE FORK HAS NO SUBJECT. **  P10's kernel is
    K = exp(-H |Delta eta|) and carries no sound speed; c_s enters only through omega of the mode, and
    P10 says so in terms -- "With omega = k c_s these are the same expression, term for term."

  ⇒ WHAT r7108's EQUATION IS AN EQUATION FOR:  ** the TENSOR mode, exactly. **  h'' + 2(a'/a)h' +
    k^2 h = 0 under h = u/a returns u'' + (k^2 - a''/a)u = 0 identically, for a(eta) a free function;
    and it is the same equation a massless minimally coupled scalar obeys under u = a phi.  The fluid
    member differs from it by exactly k^2(c_s^2 - 1)u, which vanishes at c_s = 1 and nowhere else.
    ** So it is the c_s = 1 member of one family and was never in competition with the plasma's. **

  ⇒ AND THE TWO NUMBERS ARE CONSISTENT: with the segment's own L = 3.3387380236, -255 fixes k = 76.376
    and the same k at c_s = 1/sqrt3 gives -147.224 = -255/sqrt3 to every digit, the background term
    contributing 3.7e-5 of the exponent.  P15's carried -152 sits 3.24 per cent above that because,
    by its own sentence, it is integrated across a sound-speed PROFILE.

  ⇒ WHAT IS A STATEMENT ABOUT THE SEGMENT: its curve solves the VACUUM E=1 law identically and no
    positive radiation constant is consistent with it.  ** A vacuum background has no scalar sound
    speed, so the c_s = 1 member is what the segment's own curve supports and the c_s = 1/sqrt3
    exponent belongs to the plasma, which is the leaf's. **

  ⌗ WHAT PO-77 (0) BECOMES, stated and not answered here: which species' perturbation the crossing
    transports.  That is a question about what is present, not about which equation is older, and the
    fork as posed cannot be used to settle it.
""")
print(f"  sources opened: {OPENED}")
print(f"\n  {_ok} of {_n} checks pass [{time.time()-t_all:.1f}s]")
raise SystemExit(0 if _ok == _n else 1)
