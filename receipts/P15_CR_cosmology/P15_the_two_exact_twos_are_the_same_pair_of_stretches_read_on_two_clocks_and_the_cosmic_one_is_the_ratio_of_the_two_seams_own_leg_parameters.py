#!/usr/bin/env python3
"""P15 receipt -- `r7195`'s offered item, taken: ** the lap's TWO exact factors of two, and what the
bare phrase `the $2:1$ leg` cannot say. **

*** ⛭⛭⛭ THE TWO TWOS ARE NOT TWO COINCIDENCES. THE COSMIC ONE IS THE RATIO OF THE TWO SEAMS' OWN LEG
    PARAMETERS, AND THE SAME PAIR OF STRETCHES IS `2:1` IN THAT CLOCK AND `2.3042:1` IN CONFORMAL
    LENGTH. ***

** ⓵ WHERE THE SECOND TWO COMES FROM, AND IT IS A STATEMENT ABOUT THE SEAMS. **  *The back seam sits
at `$r=-2\\alpha/\\sqrt3$` and the front seam at `$r=+\\alpha/\\sqrt3$`, with the amplitude
`$A=2^{1/3}\\alpha/\\sqrt3$`.*  ⇒ ** On the collapse leg that is `$\\cosh u=2$` and on the expansion
leg `$\\sinh u=1/\\sqrt2$`, so the two seams' own parameters are `$\\operatorname{arccosh}2$` and
`$\\operatorname{arcsinh}(1/\\sqrt2)$` --- and those stand in ratio EXACTLY `2`, residual `0` at fifty
digits, by `cc66`'s identity
`$\\operatorname{arccosh}2=2\\operatorname{arcsinh}(1/\\sqrt2)=\\ln(2+\\sqrt3)$`. **
  ⌗ *So the cosmic-time two is not an independent fact about lengths: **it IS the statement that one
  seam's parameter is half the other's.** That is why it is attached to the seam-bounded pieces.*

** ⛭ ⓶ AND THE CONFORMAL TWO DOES NOT RUN THROUGH THE SEAMS AT ALL. **  *`$1:\\sqrt3:2$` is on the
WHOLE horns, `$1.9276:3.3387:3.8552$`.*  ⛔ ** Measured on the seam-bounded pieces instead, the same
pair is `$2.3759$` to `$1.0311$` --- a ratio of `2.3042`, not `2`. **  ⇒ *** SO THE SAME TWO STRETCHES
ARE `2:1` ON ONE CLOCK AND `2.304:1` ON THE OTHER, AND THE PHRASE `the $2:1$ leg` NAMES NEITHER CLOCK.
*** *The two readings differ by fifteen per cent on the identical objects.*
  ⌗ *And the seams divide neither horn simply: `$0.5349$` of the collapse horn and `$0.6163$` of the
  expansion horn, neither one a half nor anything `PSLQ` will name.*

** ⇒ ⓷ WHICH IS WHY `r7112`'s LABEL WAS WRONG TWICE OVER, AND BOTH ARE NOW MEASURED. **  *It said the
minimum sits `$\\lvert\\Delta\\eta\\rvert_{\\rm coll}$` **after the seam**, at the midpoint of the
`$2:1$` leg.*  ⛔ ** The origin is the BRANCH POINT, and the front seam is `$0.4482\\alpha$` further
out --- `23.3` per cent of a horn, so the retired wording named the wrong origin by a measured amount
and not loosely.  And the `$2:1$` it cited is the CONFORMAL two, which on that stretch is the only one
that holds. **  ⌗ *Repaired in `r7112`'s receipt in the same revision, with the gap gated there so a
reader cannot meet the old reading again.*

⚠ ** AND THE CONTROL THAT SAYS WHY FOUR FIGURES COULD NOT HAVE SETTLED ANY OF THIS. **  *The seam's
conformal locus over the midpoint is `$1.2325401027$`, and `$\\sqrt3-\\tfrac12=1.2320508076$` sits
`$4.9\\times10^{-4}$` away --- agreeing to three decimals.*  ⇒ *** A LABEL QUOTING FOUR FIGURES CANNOT
TELL THE TRUE RATIO FROM A WRONG CLOSED FORM, WHICH IS THE SAME DEFECT ONE LEVEL UP FROM THE ONE
`r7195` ROUTED. ***  *The near-miss is named and refused at thirty digits, and `PSLQ` is run over a
basis and returns nothing, so the ratio is reported as having NO closed form found rather than as
irrational.*

⌗ ** WHOSE EACH PIECE IS. **  *The identity and the cosmic-time two are `cc66`'s, group `I` of
`P07_the_back_seam_is_the_laps_one_non_degenerate_horizon_...`; they are re-derived here independently
as a control and not claimed.  The conformal `$1:\\sqrt3:2$` is `r7108`'s.  **What is this seat's is
the link between them and the measurement of what the bare phrase costs.**  And the paper states the
distinction in its own voice at `r7195` --- read here, not recalled.*

** COMPUTES: the three conformal horn lengths and their 1:sqrt3:2 at 12 digits; both seams' own leg
parameters, derived from the seam radii and the amplitude rather than taken, and their ratio against
cc66's identity at 50 digits; the conformal lengths of the two seam-bounded pieces and their ratio;
the seams' fractional positions along their horns; the branch-point-to-midpoint and
branch-point-to-seam conformal distances and the gap between them; a PSLQ search over a basis for the
seam-over-midpoint ratio and the sqrt3-minus-a-half near-miss refused at thirty digits; and the
paper's own two sentences on the distinction, read live and each present at exactly one site.  No
transfer, spectrum, kernel or likelihood is computed and no banked file is read.  No assertion on
wall-clock time. **
"""
import os
import re

import mpmath as mp

mp.mp.dps = 60

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__.split('COMPUTES:')[0].rstrip())
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ** the lap's own constants, in the form r7108 and r7112 carry them. **
C0 = 2 / (mp.sqrt(3) * 2 ** (mp.mpf(1) / 3))


def _coll_integrand(u):
    return mp.cosh(u) ** (-mp.mpf(2) / 3)


def _expa_integrand(u):
    return mp.sinh(u) ** (-mp.mpf(2) / 3)


L_COLL = C0 * mp.quad(_coll_integrand, [0, mp.inf])
L_LIFT = C0 * mp.quad(lambda u: mp.sin(u) ** (-mp.mpf(2) / 3), [0, mp.pi / 2])
L_EXPA = C0 * mp.quad(_expa_integrand, [0, mp.inf])

# ============================================================ A. the order's figures, reproduced
head("A.  THE CONFORMAL TWO, ON THE WHOLE HORNS")

print(f"      L_COLL {mp.nstr(L_COLL, 13)}   L_LIFT {mp.nstr(L_LIFT, 13)}   "
      f"L_EXPA {mp.nstr(L_EXPA, 13)}")
_r1 = L_LIFT / L_COLL
_r2 = L_EXPA / L_COLL
print(f"      ratios 1 : {mp.nstr(_r1, 13)} : {mp.nstr(_r2, 13)}   against 1 : "
      f"{mp.nstr(mp.sqrt(3), 13)} : 2")

gate("Ⓐ① the CONFORMAL two is on the WHOLE horns: the three leg lengths stand at "
     "`$1:\\sqrt3:2$`, with the lift's `$\\sqrt3$` to better than `1e-12` and the expansion horn's "
     "`$2$` exact to the same --- which is `r7108`'s result, recomputed here as the baseline the "
     "second two is to be compared against",
     abs(_r1 - mp.sqrt(3)) < mp.mpf('1e-12') and abs(_r2 - 2) < mp.mpf('1e-12'))

# ============================================================ B. the two seams' own parameters
head("B.  BOTH SEAMS' OWN LEG PARAMETERS, DERIVED FROM THE SEAM RADII AND NOT TAKEN")

# ** the amplitude and the two seam radii.  r = A cosh^{2/3} on the collapse leg and A sinh^{2/3} on
#   the expansion leg, so a seam radius fixes its own parameter. **
A_AMP = 2 ** (mp.mpf(1) / 3) * 1 / mp.sqrt(3)            # in units of alpha
R_BACK = -2 / mp.sqrt(3)
R_FRONT = 1 / mp.sqrt(3)
_cosh_back = (abs(R_BACK) / A_AMP) ** mp.mpf('1.5')
_sinh_front = (abs(R_FRONT) / A_AMP) ** mp.mpf('1.5')
U_BACK = mp.acosh(_cosh_back)
U_FRONT = mp.asinh(_sinh_front)
print(f"      A = 2^(1/3)/sqrt3 = {mp.nstr(A_AMP, 14)};   back seam cosh u = "
      f"{mp.nstr(_cosh_back, 14)};   front seam sinh u = {mp.nstr(_sinh_front, 14)}")
print(f"      u_back  = {mp.nstr(U_BACK, 22)}")
print(f"      u_front = {mp.nstr(U_FRONT, 22)}")

gate("Ⓑ① the seam radii FIX their own parameters and the values are derived rather than quoted: "
     "`$\\cosh u=2$` at the back seam `$r=-2\\alpha/\\sqrt3$` and `$\\sinh u=1/\\sqrt2$` at the front "
     "seam `$r=+\\alpha/\\sqrt3$`, both from the amplitude `$A=2^{1/3}\\alpha/\\sqrt3$` alone",
     abs(_cosh_back - 2) < mp.mpf('1e-40')
     and abs(_sinh_front - 1 / mp.sqrt(2)) < mp.mpf('1e-40'))

_ident_a = mp.acosh(2) - 2 * mp.asinh(1 / mp.sqrt(2))
_ident_b = mp.acosh(2) - mp.log(2 + mp.sqrt(3))
print(f"      arccosh 2 - 2 arcsinh(1/sqrt2) = {mp.nstr(_ident_a, 6)};   "
      f"arccosh 2 - ln(2+sqrt3) = {mp.nstr(_ident_b, 6)}")

gate("Ⓑ② and `cc66`'s identity is re-derived here INDEPENDENTLY as a control rather than cited: "
     "`$\\operatorname{arccosh}2=2\\operatorname{arcsinh}(1/\\sqrt2)=\\ln(2+\\sqrt3)$`, both residuals "
     "below `1e-45` at sixty digits.  ⌗ *It is `cc66`'s, group `I` of its own `P07` receipt, and is "
     "not claimed here*",
     abs(_ident_a) < mp.mpf('1e-45') and abs(_ident_b) < mp.mpf('1e-45'))

_param_ratio = U_BACK / U_FRONT
print(f"      u_back / u_front = {mp.nstr(_param_ratio, 25)}   minus 2: "
      f"{mp.nstr(_param_ratio - 2, 6)}")

gate("Ⓑ③ ⛭⛭ SO THE SECOND TWO IS THE RATIO OF THE TWO SEAMS' OWN LEG PARAMETERS, EXACTLY: "
     "`$\\operatorname{arccosh}2:\\operatorname{arcsinh}(1/\\sqrt2)=2:1$` with residual below `1e-45` "
     "--- ***it is not an independent fact about lengths, it IS the statement that one seam's "
     "parameter is half the other's***, which is what attaches it to the seam-bounded pieces",
     abs(_param_ratio - 2) < mp.mpf('1e-45'))

# ============================================================ C. the same pair on two clocks
head("C.  THE SAME PAIR OF STRETCHES ON TWO CLOCKS, AND THEY DISAGREE BY FIFTEEN PER CENT")

D_BACK = C0 * mp.quad(_coll_integrand, [0, U_BACK])
D_FRONT = C0 * mp.quad(_expa_integrand, [0, U_FRONT])
_conf_ratio = D_FRONT / D_BACK
print(f"      conformal back seam -> turnaround  : {mp.nstr(D_BACK, 14)}")
print(f"      conformal branch point -> front seam: {mp.nstr(D_FRONT, 14)}")
print(f"      their conformal ratio = {mp.nstr(_conf_ratio, 14)}   against the parameter ratio 2")

gate("Ⓒ① the two seam-bounded pieces in CONFORMAL length are `$1.0311\\alpha$` and `$2.3759\\alpha$` "
     "--- and their ratio is `$2.3042$`, NOT `$2$`",
     abs(D_BACK - mp.mpf('1.0311227881')) < mp.mpf('1e-9')
     and abs(D_FRONT - mp.mpf('2.3758705509')) < mp.mpf('1e-9')
     and abs(_conf_ratio - mp.mpf('2.3041587077')) < mp.mpf('1e-9'))

_disagree = abs(_conf_ratio - 2) / 2
print(f"      the two clocks disagree on the IDENTICAL pair by {mp.nstr(100 * _disagree, 4)} per cent")

gate("Ⓒ② ⇒⇒ SO THE SAME TWO STRETCHES ARE `$2:1$` ON THE SEAMS' OWN PARAMETER AND `$2.304:1$` IN "
     "CONFORMAL LENGTH --- a disagreement of `15.2` per cent on the identical objects.  ***That is "
     "what the bare phrase `the $2:1$ leg` cannot say, and it is a structural ambiguity rather than a "
     "loose word: whichever clock a reader supplies, the other one is wrong about these pieces***",
     abs(100 * _disagree - mp.mpf('15.208')) < mp.mpf('0.01'))

_f_coll = D_BACK / L_COLL
_f_expa = D_FRONT / L_EXPA
print(f"      and the seams divide neither horn simply: {mp.nstr(_f_coll, 14)} of the collapse horn, "
      f"{mp.nstr(_f_expa, 14)} of the expansion horn")

gate("Ⓒ③ and the seams divide NEITHER horn simply --- `$0.5349$` and `$0.6163$` of their horns, "
     "neither a half --- so there is no reading on which a seam is a midpoint of anything, which is "
     "the half of `r7195`'s finding that makes `after the seam` wrong rather than merely different",
     abs(_f_coll - mp.mpf('0.5349197946')) < mp.mpf('1e-9')
     and abs(_f_expa - mp.mpf('0.6162700513')) < mp.mpf('1e-9')
     and abs(_f_coll - mp.mpf('0.5')) > mp.mpf('0.03')
     and abs(_f_expa - mp.mpf('0.5')) > mp.mpf('0.03'))

# ============================================================ D. r7112's label, measured
head("D.  WHAT r7112's RETIRED LABEL COST, MEASURED")

XM = mp.log(2) / 2
D_MIN = C0 * mp.quad(_expa_integrand, [0, XM])
_gap = D_FRONT - L_EXPA / 2
print(f"      the minimum at x = ln2/2: conformal {mp.nstr(D_MIN, 14)};   the midpoint "
      f"{mp.nstr(L_EXPA / 2, 14)};   the collapse horn {mp.nstr(L_COLL, 14)}")
print(f"      the front seam is {mp.nstr(_gap, 13)} beyond that midpoint = "
      f"{mp.nstr(100 * _gap / (L_EXPA / 2), 4)} per cent of a horn")

gate("Ⓓ① `r7112`'s arithmetic is RIGHT and is confirmed here, which is what `r7195` says and what "
     "makes this a prose repair: the minimum sits at the conformal midpoint of the expansion horn and "
     "at exactly one collapse horn from the branch point, both to better than `1e-12`",
     abs(D_MIN - L_EXPA / 2) < mp.mpf('1e-12') and abs(D_MIN - L_COLL) < mp.mpf('1e-12'))

gate("Ⓓ② and what the retired word cost is MEASURED, not called loose: the front seam lies "
     "`$0.4482\\alpha$` beyond that midpoint, `23.3` per cent of a horn, so `after the seam` named an "
     "origin that far from the right one",
     abs(_gap - mp.mpf('0.4482492543')) < mp.mpf('1e-9')
     and abs(100 * _gap / (L_EXPA / 2) - mp.mpf('23.254')) < mp.mpf('0.01'))

# ============================================================ E. the four-figure control
head("E.  AND WHY FOUR FIGURES COULD NOT HAVE SETTLED ANY OF IT")

_ratio = D_FRONT / (L_EXPA / 2)
_near = mp.sqrt(3) - mp.mpf(1) / 2
print(f"      seam over midpoint = {mp.nstr(_ratio, 20)}")
print(f"      sqrt3 - 1/2        = {mp.nstr(_near, 20)}   difference "
      f"{mp.nstr(_ratio - _near, 6)}")
_pslq = mp.pslq([_ratio, mp.mpf(1)], maxcoeff=10 ** 6, maxsteps=10 ** 4)
_ident = mp.identify(_ratio, ['sqrt(2)', 'sqrt(3)', 'pi', 'log(2)'])
print(f"      PSLQ on [ratio, 1]: {_pslq};   identify over a basis: {_ident}")

gate("Ⓔ① ⛔ THE MUST-COME-BACK-WRONG CONTROL: `$\\sqrt3-\\tfrac12=1.2320508$` sits `$4.9\\times10^{-4}$` "
     "from the true `$1.2325401$`, agreeing to THREE DECIMALS --- ***so a label quoting four figures "
     "cannot tell the true ratio from a wrong closed form***, which is `r7195`'s own defect one level "
     "up.  The near-miss is REFUSED at thirty digits rather than left to look like an identity",
     abs(_ratio - _near) < mp.mpf('1e-3') and abs(_ratio - _near) > mp.mpf('1e-30'))

gate("Ⓔ② and the ratio is reported as having NO CLOSED FORM FOUND rather than as irrational, which is "
     "a different claim and not one a search can make: `PSLQ` over `[ratio, 1]` at a million-coefficient "
     "bound returns nothing, and `identify` over a basis of `$\\sqrt2$`, `$\\sqrt3$`, `$\\pi$` and "
     "`$\\ln2$` returns nothing",
     _pslq is None and not _ident)

# ============================================================ F. the paper's own voice
head("F.  AND THE PAPER STATES THE DISTINCTION IN ITS OWN VOICE --- READ, NOT RECALLED")

_P15 = re.sub(r'\s+', ' ', '\n'.join(
    l for l in open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                    encoding='utf-8', errors='replace').read().split('\n')
    if not l.lstrip().startswith('%')))
_SENT_APART = ("So one factor of two is conformal and on the whole horns and the other is in cosmic "
               "time and on the seam-bounded pieces, and neither is to be read with the other's "
               "stretches")
_SENT_FIGS = ("The seam-bounded pieces are $1.0311\\alpha$ from the back seam to the turnaround and "
              "$2.3759\\alpha$ from the branch point to the front seam")
print(f"      the separation sentence: {_P15.count(_SENT_APART)}x;   the two figures: "
      f"{_P15.count(_SENT_FIGS)}x")

gate("Ⓕ① the paper SAYS it, and the sentence is read from `P15` live and at EXACTLY ONE site --- "
     "`neither is to be read with the other's stretches` --- so this receipt reasons from the "
     "corpus's own separation rather than asserting one of its own",
     _P15.count(_SENT_APART) == 1)

gate("Ⓕ② and the paper's OWN two figures for the seam-bounded pieces are the ones computed above, "
     "pinned at one site and matched rather than assumed: `$1.0311\\alpha$` and `$2.3759\\alpha$`, "
     "reproduced here to `1e-9` from the seam radii and the amplitude alone",
     _P15.count(_SENT_FIGS) == 1
     and abs(D_BACK - mp.mpf('1.0311227881')) < mp.mpf('1e-9')
     and abs(D_FRONT - mp.mpf('2.3758705509')) < mp.mpf('1e-9'))

# ============================================================ verdict
head("VERDICT")
_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)} of {len(CHECKS)} check(s) pass.\n")
if _bad:
    print("  FAILED:")
    for n in _bad:
        print(f"    - {n}")
    raise SystemExit(1)
print("""  ALL PASS.  r7195's offered item comes back as a link rather than a choice of words.  The lap's
  cosmic-time two is the ratio of the two SEAMS' OWN LEG PARAMETERS -- arccosh 2 against
  arcsinh(1/sqrt2), exactly 2:1 -- so it is not an independent fact about lengths but the statement
  that one seam's parameter is half the other's, which is what attaches it to the seam-bounded
  pieces.  The conformal two does not run through the seams at all: measured on the SAME pair of
  stretches, conformal length gives 2.304:1 and not 2:1, a disagreement of 15.2 per cent on the
  identical objects, and the seams divide neither horn simply.  SO `the 2:1 leg` IS STRUCTURALLY
  AMBIGUOUS AND NOT MERELY LOOSE: whichever clock a reader supplies, the other is wrong about these
  pieces.  r7112's arithmetic is confirmed right, and what its retired word cost is measured -- the
  front seam is 0.4482 alpha, 23.3 per cent of a horn, beyond the midpoint the check is about.  And
  four figures could not have settled any of it: sqrt3 - 1/2 agrees with the true seam-over-midpoint
  ratio to three decimals, so it is refused at thirty digits, with PSLQ and identify both returning
  nothing and the ratio reported as no closed form FOUND rather than irrational.""")
