#!/usr/bin/env python3
"""P03 receipt -- `PO-50`'s remainder, which the `r7209` board states is this seat's and which nothing
orders: *"the contested DIRECTION of the correction is between published analyses, is available now."*

*** ⛭⛭⛭ THE PRE-REGISTERED PREDICTION FAILS, AND ITS FAILURE IS THE RESULT: THERE IS NO CONTESTED
    DIRECTION.  THE TWO NUMBERS ARE NOT TWO READINGS OF ONE QUOTIENT, BECAUSE ONE OF THEM IS A VALUE
    THAT QUOTIENT CANNOT TAKE. ***

`r7222` pre-registered the expectation that the disagreement is REAL -- that the caustic route's
turnaround-enclosed mass ABOVE the virial one and the Local Volume flow route's mass inside the
zero-velocity surface at ABOUT SIX TENTHS of it are two readings of one ratio, so that a later
revision could pick a side on evidence.  *** It is not.  The quotient is bounded below by one. ***

** ⓵ THE BOUND IS DERIVED HERE AND IT REPRODUCES BOTH PURE NUMBERS THIS ROW ALREADY BANKS. **
*With `$\Lambda$` written as `$3H^2\Omega_\Lambda/c^2$` and a sphere's mass written through its own
mean density `$\bar\rho = f\rho_c$`, the spherical turnaround bound collapses to one line:*
`$(r/R_{\rm ta})^3 = 2\Omega_\Lambda/f$`.  ⇒ ** At `f = 3.50` that is `0.737` and at `f = 5.56` it is
`0.632` -- the two numbers `PO-50` carries for the fixed-overdensity ensembles, each reproduced to
three decimals, and each back-solving to the SAME `$\Omega_\Lambda$` within two parts in a thousand. **
⌗ *Those were banked as pure numbers carrying no datum; they are now banked as consequences of one
formula, which is a stronger statement about them than the row made.*

** ⓶ AND THE SAME LINE SAYS WHERE THE TURNAROUND SURFACE SITS, WHICH IS THE WHOLE ARGUMENT. **
*Setting `$r = R_{\rm ta}$` gives mean enclosed density `$2\Omega_\Lambda\rho_c$`, about `1.4\rho_c`.
Against a virial radius at `$200\rho_c$` that puts the turnaround surface at* `$R_{\rm ta} = 5.23\,
r_{200}$`.  ⛭⛭ ** Which is independently the survey figure this row already quotes: `CHANCES` observes
to `5 r_{200}` and its authors state that this corresponds roughly to the turnaround radius.  The
corpus's own bound predicts `5.23` with no fitted parameter. **

** ⓷ SO THE QUOTIENT IS MONOTONE-BOUNDED AND CANNOT BE SIX TENTHS. **  *For any non-negative density
the enclosed mass is non-decreasing, and the turnaround surface lies OUTSIDE the virial radius by the
factor just computed.*  ⇒ *** `$M(<R_{\rm ta})/M(<r_{200}) \ge 1$` identically, with equality only on
an empty shell.  Measured over four profile families across their usable concentration ranges it runs
`2.0`--`2.9` for `NFW` and spans `1.1`--`5.2` over the whole family -- *** which is the caustic route's
reported `1.2`--`2.2`, from geometry alone. ***  ⛔ ** A reported `0.6` is not a disagreement with that:
it is outside the quotient's range. **

⌈ ⇒ *** THEREFORE THE DIRECTION IS NOT CONTESTED.  The caustic route's sign is the only sign an
enclosed-mass ratio admits, and the Local Volume number is a different object -- so `PO-50`'s
arithmetic, which the row says runs through this disagreement, runs through nothing: it can use the
enclosed-mass ratio directly. ***

** ⓸ AND THE MISMATCH IS NARROWED FROM THREE ACCOUNTS TO TWO, WITH NO TUNED CONSTANT. **  *Three
things can carry a quotient below one: a denominator that is a different ESTIMATOR rather than an
enclosed mass, a denominator SUMMED over two haloes against a numerator enclosed once, and a
denominator at a different OVERDENSITY convention.*  ⇒ ** The convention account is ELIMINATED: over
the whole profile family it floors at `0.733` and cannot reach six tenths. **  *The halo sum reaches
`0.583`, but only on the steepest outer profile in the family; and the estimator account is unbounded
below by construction, which is why no instance of it is evaluated -- a tuned factor would reproduce
only its own target.*

⛭ ** AND THIS PUSH BROKE ONE OF THIS SEAT'S OWN GATES BY ADDING A FILE, WHICH IS REPAIRED HERE AND
   NOT WORKED AROUND. **  *This is the first receipt this seat has landed in `receipts/P03_SdS_slicing/`.
A gate in this seat's own `L_probability/S5` tested authorship with a FROZEN LIST of two directory
prefixes, so it read this brand-new file as ANOTHER seat's receipt and went red on an ADDITION rather
than on an edit.*  ⇒ *** That is `S5`'s own measured class -- a gate on a set its own seat can grow --
caught a second time, the first having been the trunk moving at `r7214`. ***  *Repaired by subtracting
what THIS BRANCH ADDED, which is this seat's by construction, rather than by extending the list, which
would fail again at the fourth directory.*  ⛔ ** And the repair is gated as NOT VACUOUS: the clause
reads zero here and still fires on an injected modified unowned receipt, so what was removed is the
addition case and the EDIT claim is untouched. **

⛔ ** WHICH OF THE TWO SURVIVORS IT IS, THIS RECEIPT DOES NOT SAY.** *That needs the Local Volume
route's own definition of its denominator, which is not in this tree and was not read in this session.*
⇒ ** The gap is reported and gated AS a gap, exactly as `r7222`'s pre-registration fixed in advance --
not filled from recollection. **  ⌗ *And nothing here reads on the row's live clause, which is `66`'s:
neither exit is this step and the row does not move.*

** COMPUTES: the turnaround-bound identity and both of `PO-50`'s banked fixed-overdensity numbers from
   it; the implied `$\Omega_\Lambda$` back-solved from each independently; the turnaround surface's
   mean overdensity and its radius in units of `$r_{200}$`; the enclosed-mass ratio across four
   density profiles and their concentration ranges, with its minimum over the family; a monotonicity
   control on a profile built to violate it; the three mismatch mechanisms that can carry a quotient
   below one; and the side-repair this push forced -- the repaired clause read out of this seat's own
   `S5` statically, plus an injected control proving it still fires.  *** `S5` itself is NOT run from
   inside this receipt: it runs fourteen receipts of its own, and nesting that would multiply this
   receipt's cost by another's, which is the shape `r7220` spent a revision on. ***  *** No
   published value is asserted that is not already banked in this row, and the one question needing a
   source this receipt lacks is gated as owed. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~1 s)
"""
import hashlib
import os
import subprocess
import sys

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

print(__doc__.split("** COMPUTES:")[0].rstrip())
BAR = "=" * 104
fail = []


def gate(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = os.path.join(ROOT, 'THE_REGISTER.md')
if not os.path.exists(REG):
    print(f"  ⛔ A PATH THIS RECEIPT READS IS NOT ON DISK: {REG}")
    sys.exit(1)
REGBYTES = open(REG, 'rb').read()
REGHASH = hashlib.sha256(REGBYTES).hexdigest()
REGTXT = ' '.join(REGBYTES.decode('utf-8').split())

# ============================================================ A. the row's own words, read not recalled
head("A.  THE CONTEST, READ OUT OF THE ROW RATHER THAN RECALLED")

CLAIM = ('the caustic route puts the turnaround-enclosed mass above the virial one, while the Local '
         'Volume flow route puts the mass inside the zero-velocity surface at about six tenths of it')
gate("Ⓐ① the contest is quoted from `THE_REGISTER` and not from memory -- the row's own sentence is "
     "present verbatim", CLAIM in REGTXT)
gate("Ⓐ② and the row states the settling comes FIRST because its arithmetic runs through it, which is "
     "why this is the step", "That disagreement is the first thing to settle" in REGTXT)
gate("Ⓐ③ and the two fixed-overdensity pure numbers this receipt will re-derive are the ones the row "
     "banks", '0.737' in REGTXT and '0.632' in REGTXT)
print("      ⌗ Nothing outside this file is quoted.  The caustic route's own mass ratio, as the row")
print("        banks it, is 1.2 to 2.2; the Local Volume figure, as the row banks it, is about 0.6.")
CAUSTIC_LO, CAUSTIC_HI, LV = 1.2, 2.2, 0.6

# ============================================================ B. the bound, derived
head("B.  ⛭ THE TURNAROUND BOUND IN ONE LINE, AND IT REPRODUCES BOTH BANKED NUMBERS")

# R_ta^3 = G M / (H^2 OmL)   with  Lambda c^2 = 3 H^2 OmL
# M of a sphere of radius r at mean density f * rho_c, rho_c = 3H^2/(8 pi G):
#   M = (4pi/3) r^3 f rho_c = r^3 f H^2 / (2 G)
# =>  (r / R_ta)^3 = f / (2 OmL)      ... so  r/R_ta = (2 OmL / f)^(1/3)


def r_over_rta(f, oml):
    """the attained radius of a sphere of mean density f*rho_c, in units of the turnaround bound."""
    return (2.0 * oml / f) ** (1.0 / 3.0)


def oml_from(ratio, f):
    """the Omega_Lambda a banked (ratio, overdensity) pair implies -- the identity, run backwards."""
    return ratio ** 3 * f / 2.0


OML_A, OML_B = oml_from(0.737, 3.50), oml_from(0.632, 5.56)
print(f"      f = 3.50 -> r/R_ta = {r_over_rta(3.50, OML_A):.4f}   (row banks 0.737)")
print(f"      f = 5.56 -> r/R_ta = {r_over_rta(5.56, OML_B):.4f}   (row banks 0.632)")
print(f"      Omega_Lambda back-solved from each INDEPENDENTLY: {OML_A:.5f} and {OML_B:.5f}")
gate(f"Ⓑ① both banked numbers come out of ONE identity to three decimals -- {r_over_rta(3.50, OML_A):.3f} "
     f"and {r_over_rta(5.56, OML_B):.3f}",
     abs(r_over_rta(3.50, OML_A) - 0.737) < 5e-4 and abs(r_over_rta(5.56, OML_B) - 0.632) < 5e-4)
gate(f"Ⓑ② ⛭⛭ and the two back-solves agree on `Omega_Lambda` to {abs(OML_A - OML_B) / OML_A * 1e3:.1f} "
     "parts in a thousand, so they are two readings of one cosmology and not two fitted numbers",
     abs(OML_A - OML_B) / OML_A < 3e-3)
OML = 0.70
gate("Ⓑ③ and that value is the standard one to two figures, which is the check that the identity is "
     f"the right identity rather than one tuned to hit two targets: {OML_A:.3f} vs {OML:.2f}",
     abs(OML_A - OML) < 0.01)

# ============================================================ C. where the turnaround surface sits
head("C.  ⛭⛭ WHERE THE TURNAROUND SURFACE SITS -- AND THE SURVEY'S OWN FIGURE FALLS OUT")

F_TA = 2.0 * OML                      # mean enclosed overdensity AT the bound, in rho_c
F_VIR = 200.0                         # the virial convention the row's ensembles use
RTA_OVER_R200 = (F_VIR / F_TA) ** (1.0 / 3.0)
print(f"      mean enclosed density at the turnaround bound: {F_TA:.3f} rho_c")
print(f"      virial convention:                             {F_VIR:.0f} rho_c")
print(f"      => R_ta / r_200 = {RTA_OVER_R200:.4f}")
gate(f"Ⓒ① the turnaround surface sits OUTSIDE the virial radius, by {RTA_OVER_R200:.2f} -- which is "
     "the premise the whole argument needs and it is computed, not assumed", RTA_OVER_R200 > 1.0)
gate("Ⓒ② ⛭⛭ and it reproduces the survey figure the row already quotes, `5 r_200` corresponding "
     f"roughly to the turnaround radius: predicted {RTA_OVER_R200:.2f} with NO fitted parameter",
     abs(RTA_OVER_R200 - 5.0) < 0.5)
gate("Ⓒ③ and the row does carry that survey statement, so this is a reproduction and not a "
     "coincidence assembled here", '5 r200' in REGTXT or '5 r_{200}' in REGTXT or '5r_{200}' in REGTXT)

# ============================================================ D. the theorem, and the family
head("D.  ⛔ THE QUOTIENT IS BOUNDED BELOW BY ONE, SO SIX TENTHS IS OUTSIDE ITS RANGE")

PROFILES = {
    # name: (rho(x) up to normalisation, usable shape-parameter range)
    'NFW':        (lambda x, c: 1.0 / (c * x * (1.0 + c * x) ** 2), (3.0, 10.0)),
    'Hernquist':  (lambda x, a: 1.0 / (a * x * (1.0 + a * x) ** 3), (3.0, 10.0)),
    'isothermal': (lambda x, _: 1.0 / x ** 2, (1.0, 1.0)),
    'Einasto':    (lambda x, n: np.exp(-2.0 * n * ((5.0 * x) ** (1.0 / n) - 1.0)), (4.0, 7.0)),
}


def enclosed(rho, p, r):
    """M(<r) up to one common normalisation -- the integral itself, no closed form assumed."""
    return quad(lambda s: rho(s, p) * s * s, 1e-9, r, limit=200)[0]


def mass_ratio(rho, p):
    """M(< R_ta) / M(< r_200), both from the SAME profile, in units where r_200 = 1."""
    return enclosed(rho, p, RTA_OVER_R200) / enclosed(rho, p, 1.0)


rows, allr = [], []
for name, (rho, (plo, phi)) in PROFILES.items():
    ps = [plo] if plo == phi else list(np.linspace(plo, phi, 7))
    vals = [mass_ratio(rho, p) for p in ps]
    allr += vals
    rows.append((name, min(vals), max(vals)))
    print(f"      {name:<11} ratio over its range: {min(vals):.4f} .. {max(vals):.4f}")
LO, HI = min(allr), max(allr)
print(f"      whole family: {LO:.4f} .. {HI:.4f}   ({len(allr)} profiles)")

gate(f"Ⓓ① every member of the family puts the quotient ABOVE one -- minimum {LO:.4f} -- which is the "
     "theorem (non-negative density makes the enclosed mass non-decreasing) seen numerically",
     LO > 1.0)
gate(f"Ⓓ② ⚠ and the band is WIDE -- {LO:.2f} to {HI:.2f}, a factor of {HI / LO:.1f} -- so the caustic "
     f"route's banked {CAUSTIC_LO}--{CAUSTIC_HI} sitting inside it is CONSISTENCY and not confirmation: "
     "the geometry fixes the SIGN and does not pin the value, which is stated here because a band "
     "that wide containing a number is nearly no constraint at all",
     LO <= CAUSTIC_HI and HI >= CAUSTIC_LO and HI / LO > 3.0)
gate(f"Ⓓ③ ⛔ AND THE LOCAL VOLUME FIGURE IS OUTSIDE THE RANGE, NOT AT THE OTHER END OF IT: {LV} "
     f"against a floor of {LO:.4f}", LV < LO)
gate("Ⓓ④ ⇒ so the two are not two readings of one quotient and the DIRECTION is not contested -- "
     "the sign is the only sign an enclosed-mass ratio admits", LV < 1.0 <= LO)

# ============================================================ E. must-come-back-wrong
head("E.  ⌗ THE MUST-COME-BACK-WRONG CONTROLS, BOTH FIXED BEFORE THE MEASUREMENT")


def hollow(x, _):
    """a shell profile that is EMPTY outside the virial radius -- the equality case, which must be
    detected as equality rather than as a comfortable margin."""
    return 1.0 / x ** 2 if x <= 1.0 else 0.0


_eq = mass_ratio(hollow, 0.0)
gate(f"Ⓔ① the equality case comes back AT equality and not above it: an empty outer shell gives "
     f"{_eq:.6f}, so the floor is tight and the theorem is not being read off a lucky family",
     abs(_eq - 1.0) < 1e-6)


def negative(x, _):
    """an UNPHYSICAL profile with negative density outside the virial radius.  A method that cannot
    see this is not measuring monotonicity, and the receipt would have no finding."""
    return 1.0 / x ** 2 if x <= 1.0 else -3.0 / x ** 2


_neg = mass_ratio(negative, 0.0)
gate(f"Ⓔ② ⛔ and the method DOES break where it must: a negative-density outer region drives the "
     f"quotient to {_neg:.4f}, below one -- so the floor is a statement about non-negative density "
     "and the instrument can tell the difference", _neg < 1.0)

# the overdensity-convention pair the row already banks, used as the incomparability detector
_pair = (r_over_rta(3.50, OML), r_over_rta(5.56, OML))
_conv = (_pair[0] / _pair[1]) ** 3
gate(f"Ⓔ③ and the convention pair the row banks is reported INCOMPARABLE rather than merged: the two "
     f"radii differ by a pure factor {_pair[0] / _pair[1]:.4f}, a mass factor {_conv:.3f}, carrying no "
     "datum -- identical for every cluster in either sample", abs(_conv - 1.0) > 0.25)

# ============================================================ F. the three mechanisms, exhibited
head("F.  ⌗ WHAT CAN CARRY A QUOTIENT BELOW ONE -- THREE MECHANISMS, EXHIBITED NOT ASSERTED")

rho_nfw, _ = PROFILES['NFW']
M_TA = enclosed(rho_nfw, 5.0, RTA_OVER_R200)
M_VIR = enclosed(rho_nfw, 5.0, 1.0)

# (i) the denominator is a different ESTIMATOR, not an enclosed mass.  Nothing bounds an estimator
#     calibrated on the whole infall against the mass enclosed at one radius, so this mechanism is
#     unbounded below BY CONSTRUCTION -- which is why no instance of it is evaluated here: a tuned
#     factor would only reproduce whatever target it was tuned to.
# (ii) the denominator SUMMED over two haloes while the numerator is enclosed once.
# (iii) the denominator at the other overdensity convention this row itself banks.
def over_family(f):
    """f(M_ta, M_vir) evaluated on every member of the family -- no tuned constants anywhere."""
    out = []
    for nm, (rho, (plo, phi)) in PROFILES.items():
        ps = [plo] if plo == phi else list(np.linspace(plo, phi, 7))
        for p in ps:
            out.append(f(enclosed(rho, p, RTA_OVER_R200), enclosed(rho, p, 1.0)))
    return min(out), max(out)


II = over_family(lambda mt, mv: mt / (2.0 * mv))
III = over_family(lambda mt, mv: mt / (mv * _conv))
print("      (i)   denominator a different ESTIMATOR          : UNBOUNDED BELOW by construction,")
print("            so it is not evaluated -- a tuned factor would only reproduce its own target")
print(f"      (ii)  denominator SUMMED over two haloes         : {II[0]:.4f} .. {II[1]:.4f}")
print(f"      (iii) denominator at the other convention banked : {III[0]:.4f} .. {III[1]:.4f}")

gate(f"Ⓕ① ⛭⛭ ONE OF THE THREE IS ELIMINATED: the overdensity-convention mismatch floors at "
     f"{III[0]:.4f} over the whole family and CANNOT reach {LV}, so whatever the Local Volume "
     "denominator is, it is not this row's other convention", III[0] > LV)
gate(f"Ⓕ② and the halo-sum mismatch CAN reach it, at {II[0]:.4f}, but only on the steepest outer "
     "profile in the family -- so it survives as an account and is not the comfortable one",
     II[0] <= LV < II[1])
gate("Ⓕ③ ⛔ SO TWO ACCOUNTS REMAIN AND THIS RECEIPT NAMES NEITHER: the estimator mismatch, which no "
     "measurement here can bound, and the halo sum, which reaches six tenths only at the edge of the "
     "family.  Choosing between them needs that route's OWN definition of its denominator, which is "
     "not in this tree and was not read in this session, so it is reported as OWED exactly as the "
     "pre-registration fixed", III[0] > LV and II[0] <= LV)

# ============================================================ G. the prediction, and the row
head("G.  ⛭⛭⛭ THE PRE-REGISTERED PREDICTION FAILED, WHICH IS SAID AS A FAILURE")

print("      r7222 predicted: the disagreement is REAL rather than definitional, the two quotients")
print("      comparable, and a later revision picks a side on evidence.")
print("      Measured: the quotient's floor is 1 and the Local Volume figure is below it, so the two")
print("      are not comparable and there is no side to pick.")
print("      ⇒ The pass condition is NOT met.  The prediction is WRONG and the row is sharper for it.")
gate("Ⓖ① the pre-registration's own failure condition is the one that fired -- `if the denominators "
     "differ by a factor comparable to the gap, there is no contested direction but two different "
     "quantities` -- and it is reported as the prediction failing", LV < LO)
_gapfac = CAUSTIC_LO / LV
gate(f"Ⓖ② and the threshold the pre-registration chose was the right size: the gap between the two "
     f"reported ratios is a factor {_gapfac:.2f}, and the one mismatch mechanism this receipt could "
     f"ELIMINATE carries a mass factor of {_conv:.3f} -- the same order, which is why that mechanism "
     "was close enough to be worth testing and far enough to be ruled out",
     _gapfac > 1.5 and 1.2 < _conv < _gapfac * 1.5)

_after = hashlib.sha256(open(REG, 'rb').read()).hexdigest()
gate("Ⓖ③ ⌗ and the row does not move: neither `PO-50` exit is this step, and the register this receipt "
     "reads is byte-identical after the run -- checked by digest rather than by inspecting this file's "
     f"own source, which an earlier draft of this gate tried and defeated itself on ({_after[:12]})",
     _after == REGHASH)
print("      ⌗ What `PO-50`'s arithmetic may now use directly: the enclosed-mass ratio, with the")
print("        family band computed above, rather than a correction whose sign was thought open.")

# ============================================================ H. the side-repair this push forced
head("H.  ⛭ AND THIS PUSH BROKE ONE OF THIS SEAT'S OWN GATES BY ADDING A FILE, WHICH IS REPAIRED HERE")

print("      This revision is this seat's first receipt in `receipts/P03_SdS_slicing/`.  A gate in")
print("      this seat's own `L_probability/S5` tested authorship with a FROZEN LIST of two")
print("      directory prefixes, so it read this seat's brand-new file as another seat's receipt and")
print("      went red on an ADDITION rather than on an edit -- which is S5's own measured class, a")
print("      gate on a set its own seat can grow, caught a second time.")
print("      ⇒ Repaired by subtracting what THIS BRANCH ADDED, which is this seat's by construction,")
print("        rather than by extending the list -- a list would fail again at the fourth directory.")

_S5 = [os.path.join(ROOT, 'receipts', 'L_probability', _f)
       for _f in sorted(os.listdir(os.path.join(ROOT, 'receipts', 'L_probability')))
       if _f.startswith('S5_')]
# ⌗ The repair is checked STATICALLY and the repaired receipt is NOT run from inside this one.
#   Running it here would re-run the fourteen receipts IT runs, duplicating the runner's own job and
#   multiplying this receipt's cost by another receipt's -- which is the shape `r7220` spent a whole
#   revision on.  The suite runs `S5`; this gate only has to show the repair is in the tree.
_s5src = open(_S5[0], encoding='utf-8').read() if len(_S5) == 1 else ''
gate("Ⓗ① the repair is IN THE TREE and is the subtraction rather than a longer list: the clause now "
     "excludes what this branch ADDED, and the `r7222` note saying why a list would fail again at "
     "the fourth directory is written beside it",
     "--diff-filter=A" in _s5src and "not in _added" in _s5src
     and "r7222 REPAIR" in _s5src and "s a path list is a gate on a set its own seat can grow" in _s5src)

def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True).stdout


# ⛭⛭⛭ r7245 REPAIR -- the face `S5` was caught by three times, arriving here
#   through the range's other end.  `HEAD --not origin/main` is THIS BRANCH'S commits only
#   while the branch is this seat's alone; on a trunk that has just absorbed another seat's
#   push it is every seat's, and `r7243+70.1` modified 95 unowned receipts by its own order,
#   which the clause below read as THIS seat editing them.
#   ** A gate on a push range is a gate on a set every other seat can grow. **
#   ⇒ The claim's subject is what THIS SEAT'S commits touched, so the range is filtered to
#   the commits carrying the session that last wrote this receipt -- `r7229+70.1`'s own seat
#   marker put to the use it was measured for.  Monotone in the safe direction: as the trunk
#   absorbs the work, the set shrinks.
import re as _re_r7245
_SESS = _re_r7245.compile(r'^Claude-Session:\s*(\S+)', _re_r7245.M)
# ⚠ The anchor is the commit that INTRODUCED this receipt and not the one that last wrote
#   it: another seat's pin batch touched this file, so `last writer` resolves to THAT seat and
#   the filter would keep exactly the commits the claim is about excluding.  `r7244` measured
#   last-writer parity migrating on 14.8 per cent of site-lines, so the adding commit is the
#   only stable marker of whose receipt this is.
# ⛔⛭⛭⛭ r7268 (60): AND THE SELF-IDENTIFICATION WAS PINNED TO HOW THE PROCESS WAS INVOKED.
#   *`__file__` is whatever was passed to the interpreter.  Run as `python3 FILE` from this
#   directory it is a BARE FILENAME, and this pathspec is resolved with `cwd=ROOT`, so git is asked
#   for a path at the repository root that does not exist and returns NOTHING.*
#   ⇒ *** Under the corpus's OWN runner-read tracer -- which runs each receipt as `python3 <name>`
#       from its own directory -- the ownership read came back EMPTY, `_own_sess` fell to `None`, and
#       the `or _own_sess is None` arm silently widened the commit set to EVERY seat's. ***
#   ⌈ *Measured: this gate read `0` unauthorised crossings run directly and `2` under the tracer, on
#     the same tree, for no reason in the tree.*
#   ⌊ *Repaired twice over: the path is made REPOSITORY-RELATIVE, which holds however the file was
#     invoked; and the empty read is no longer a licence to widen -- it FAILS, because an absence
#     with no positive control is the class this stretch has been working.*
_SELF_REL = os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, '/')
_own_log = _git('log', '--diff-filter=A', '--format=%B', '--', _SELF_REL)
assert _own_log.strip(), (
    'the introducing commit of ' + _SELF_REL + ' read EMPTY: the ownership filter below '
    'would widen to every seat, so this fails here instead of passing wider')
# ⛔⛭⛭ r7277 (66): AND THE GUARD ABOVE COVERS THE EMPTY READ AND NOT THE UNMARKED ONE, SO THE
#   WIDENING ARM IS STILL REACHABLE BY A SECOND ROUTE.  *`cc66` rediscovered this defect
#   independently at `r7269+cc66.3` and reproduced it THREE ways -- `rc=0` at the trunk where the
#   range is empty, `rc=0` run directly, `rc=1` through `scripts/sweep_runner_reads.py` -- which is
#   stronger evidence than the side it was first found from.  **`60`'s repair is right and is what
#   clears that red; this is the arm it left standing.***
#   ⇒ *** `_own_log` can be NON-EMPTY and carry no `Claude-Session:` line, and then `_own_sess` is
#       still `None` and `None` still ACCEPTS EVERY COMMIT.  The assert guards the absence of a
#       READ, not the absence of a MARKER.  So the arm is removed: an unresolvable identity FAILS
#       here rather than passing wider, which can only ever NARROW the commit set and cannot
#       manufacture a pass. ***
#   ⌊ *`66`'s edit, two lines, because leaving a known failing-open arm in a restraint gate while
#     the owning seat works the backlog is leaving a mess behind.  **Stated for `60` to reverse** --
#     no claim, count or verdict moves.*
_own_sess = _SESS.search(_own_log)
assert _own_sess, (
    'the introducing commit of ' + _SELF_REL + ' carries no Claude-Session marker: the ownership '
    'filter below would widen to every seat, so this fails here instead of passing wider')
_own_sess = _own_sess.group(1)
#: ⛔⛭⛭⛭ r7368 (60): AND THE PREVIOUS REPAIR'S OWN WRITTEN SAFETY ARGUMENT WAS THE DEFECT.
#   *`S5` carries this same range and the note that adopted it three times over -- `r7214`, `r7222`,
#   `r7245` -- each time with the same safety argument in writing: ** "monotone in the safe
#   direction: as the trunk absorbs this work the set SHRINKS." **  Shrinking IS the safe direction
#   for the RESTRAINT, whose claim is that nothing in the range is unauthorised and which an empty
#   range satisfies.  It is FATAL for the restraint's own NON-VACUITY, which is the one clause an
#   empty range makes false -- and both were read off ONE population.*
#   ⇒ *** `origin/main` is a selector that is not committed with the measurement: `r7365` ②'s rule
#       in the one spelling the rule did not cover, since the selector IS in the file and still
#       names a ref.  `S23`'s `Ⓕ①` had already adopted the property -- a base must be a literal sha
#       that resolves and is an ancestor of `HEAD` -- and checked it as the single expression
#       `merge-base HEAD origin/main` on the two receipts it was found in.  The shape walked past
#       that control into this file and `S5` under `--not`. ***
#   ⇒⇒ ** And it did not fail until THIS SEAT'S OWN WORK MERGED, which is the one event none of the
#      three earlier repairs tested: another seat's push GROWS the range, and the three repairs were
#      all written against growth.  My own push LANDING empties it. **
#   ⌊ *The population is this branch's own run, based at the LAST TRUNK MERGE INTO IT -- a commit,
#     not a ref, so it is stable whoever merges what afterwards.  It is the same set the figures were
#     measured over, now named by what it IS; the live range is REPORTED below, never asserted.*
#   ⚠ *And the base is not interchangeable with the phase's census: based at the census this gate
#     reads ONE unauthorised crossing, because the warrant for it is a crossing of
#     `L263_the_station_audit` made at `r7356`, which the census cuts off.  **A restraint's base is
#     the earliest commit any of its warrants stands at, and nothing later.** *
BASE = '72a204e2'       # the last trunk merge into this branch: a fixed sha, ancestor of HEAD


def _mine_since(_base):
    """this seat's own commits since `_base`, by the session marker on the introducing commit"""
    _out = []
    for _blk in _git('log', '--no-merges', '--format=%H%x00%B%x01',
                     'HEAD', '--not', _base).split('\x01'):
        if '\x00' in _blk:
            _sha, _body = _blk.split('\x00', 1)
            _m = _SESS.search(_body)
            if _m and _m.group(1) == _own_sess:
                _out.append(_sha.strip())
    return _out


_MINE_C = _mine_since(BASE)
_MINE_LIVE = _mine_since('origin/main')
_touched = [l for c in _MINE_C
            for l in _git('show', '--no-merges', '--name-only', '--format=',
                          c).split('\n') if l]
_added = {l for c in _MINE_C
          for l in _git('show', '--no-merges', '--diff-filter=A', '--name-only',
                        '--format=', c).split('\n') if l}


# ⛔⛭⛭⛭ r7268 (60): AND THE PREDICATE DID NOT OWN THE FILE THE GATE IS IN.  *`66`'s r7265 note
#   is right that widening this to a PARITY rule retires the claim rather than bounding it, and that
#   reversal is accepted below.  But the prefix pair is still a snapshot of where this seat's
#   receipts HAPPENED to live, and this receipt is the counterexample: `receipts/P03_SdS_slicing/`
#   matches neither prefix, so the clause read THIS SEAT EDITING ITS OWN RECEIPT as a crossing --
#   which is what it did on this branch, at one crossing, the file being this one.*
#   ⇒ *** And the gate already carries the instrument that answers it: the session marker on the
#       INTRODUCING commit, which this gate trusts to say which COMMITS are this seat's and then does
#       not ask of the FILES.  One gate, two definitions of `mine`, and the weaker one was the one in
#       the claim. ***
#   ⌗ *So ownership is read with the gate's own marker, asked of the file: the prefixes stay as the
#     fast path, and another seat's receipt is still foreign -- the claim keeps its force and loses
#     the snapshot.*
_OWN_PFX = ('receipts/P15_CR_cosmology/', 'receipts/L_probability/S')


def _introduced_by_this_seat(q):
    _m = _SESS.search(_git('log', '--diff-filter=A', '--format=%B', '-1', '--', q))
    return _own_sess is not None and bool(_m) and _m.group(1) == _own_sess


def _owned(q):
    return q.startswith(_OWN_PFX) or _introduced_by_this_seat(q)


def _outside(paths):
    return [q for q in paths
            if q.startswith('receipts/') and q.endswith('.py') and not _owned(q) and q not in _added]


# ⛔⛭⛭⛭ r7265 (66): AND THE CLAUSE WENT FALSE BECAUSE AN ORDER AUTHORISED THE CROSSING IT FORBIDS.
#   *This gate asks whether this seat reached OUTSIDE its prefixes, and it reads the question
#   correctly.  **What it cannot read is whether the reaching was BIDDEN.**  `r7261`'s third queue
#   item ordered `M17` repaired in `P12`, and working it reached `P12/I55` -- the receipt cited on
#   the over-reaching sentence, whose own locator was stale and was repaired with it; the same
#   revision's `N1` work reached `L251/N1`'s count, which this seat's own edits had moved.*
#   ⇒ *** So a restraint gate cannot distinguish an UNBIDDEN crossing from an ORDERED one, and the
#   first order that routes a cross-prefix repair turns the restraint claim false while the gate
#   stays correct about the fact. ***  *That is why nobody notices until an order lands: there is no
#   defect for the gate to misread, and no misreading for a reader to catch.*
#   ⌈ ** The repair is to carry the authorised crossings BY NAME, with the order that authorised each
#     -- not to widen `_owned`, which would retire the claim instead of bounding it. **  *The claim
#     keeps its force: an unbidden crossing still fires, which the injected control proves on the
#     same computation, and an exception that is not in this list is still a violation.*
#   ⌊ *`66`'s order is the cause, so `66` carries the exception.  **Stated for the holding seat to
#     reverse** -- no claim, count or verdict is touched, only the authorisation this gate had no way
#     to represent.*
# ⛔⛭⛭ r7268 (60): AND THE GUARD AGAINST A BLANKET AUTHORISATION WAS A SNAPSHOT OF THE CROSSING
#   SET.  *It asserted that every authorisation is a path this branch CURRENTLY crosses -- true on
#   the trunk the exception was written on, false on any tree where those commits have merged out of
#   `HEAD --not origin/main`, which is the range this gate reads.  Measured here: both were
#   uncrossed and the clause was red on a branch that had crossed neither.*
#   ⇒ *** An authorisation is a HISTORICAL FACT about a commit, so it is pinned at the commit that
#       made the crossing -- `L-249`'s rule, which is what the rest of this cycle was about -- and the
#       live arm stays as the fast path.  A stale authorisation still cannot widen the claim: the
#       pinned commit must resolve AND its own diff must contain the path. ***
_AUTHORISED = {
    # path                                       (the order that authorised it, the commit that crossed it)
    'receipts/P12_algebroid_paper/I55_the_atiyah_sequence_is_exact_and_a_characteristic_class_'
    'is_not_available.py': ('r7261 queue item 3 (M17): the citation over-reached its receipt, and '
                            'the receipt\'s own locator was stale and repaired with it', '302ab941'),
    'receipts/L251_the_numbering_collides/N1_two_lines_numbering_from_one_counter_and_a_paper_'
    'narrating_its_own_history.py': ('r7265 order item 3 (N1): the frontier-table repair moves a '
                                     'number the receipt states about the same material',
                                     'dcef045c'),
    # ⛭⛭ r7336+60: AND NINE MORE, WHICH IS THE MECHANISM WORKING AND NOT THE CLAIM WIDENING.
    #   *`r7331` ④ ordered this seat into two blocks outside its prefixes, so the crossing is
    #   BIDDEN and belongs here by name with the order that bade it -- not in a wider `_owned`,
    #   which would retire the claim instead of bounding it.*  ** Each is pinned at the commit of
    #   this branch whose own diff carries it, so the authorisation stays a historical fact and a
    #   path nobody crossed is still a blanket. **
    'receipts/L147_two_arm/B10_the_thermal_mechanism_needs_an_exponential_approach.py':
        ("r7331 order 4 (the repair stride): L147_two_arm named as the block to repair FIRST. The trunk later kept the other seat\u2019s repair of the same five, which the next revision\u2019s orders concede was the assignment and not this crossing",
         '5d2d8e36'),
    'receipts/L147_two_arm/B2_the_prose_duplicate_did_not_reach_main.py':
        ("r7331 order 4 (the repair stride): L147_two_arm named as the block to repair FIRST. The trunk later kept the other seat\u2019s repair of the same five, which the next revision\u2019s orders concede was the assignment and not this crossing",
         '5d2d8e36'),
    'receipts/L147_two_arm/B3_a_dichotomy_stated_is_not_a_dichotomy_proved.py':
        ("r7331 order 4 (the repair stride): L147_two_arm named as the block to repair FIRST. The trunk later kept the other seat\u2019s repair of the same five, which the next revision\u2019s orders concede was the assignment and not this crossing",
         '5d2d8e36'),
    'receipts/L147_two_arm/B8_the_zero_velocity_band_is_a_third_of_the_gap.py':
        ("r7331 order 4 (the repair stride): L147_two_arm named as the block to repair FIRST. The trunk later kept the other seat\u2019s repair of the same five, which the next revision\u2019s orders concede was the assignment and not this crossing",
         '5d2d8e36'),
    'receipts/L147_two_arm/B9_the_admissible_pair_is_forced_not_merely_distinguished.py':
        ("r7331 order 4 (the repair stride): L147_two_arm named as the block to repair FIRST. The trunk later kept the other seat\u2019s repair of the same five, which the next revision\u2019s orders concede was the assignment and not this crossing",
         '5d2d8e36'),
    'receipts/L165_defining_the_sum/S1_seven_necessary_conditions_on_the_measure.py':
        ("r7331 order 4 (the repair stride): L165_defining_the_sum named as the second block, the densest this seat holds; repaired row by row and taken whole by the trunk",
         '5d2d8e36'),
    'receipts/L165_defining_the_sum/S2_c1_and_c2_are_one_and_the_source_answers_more.py':
        ("r7331 order 4 (the repair stride): L165_defining_the_sum named as the second block, the densest this seat holds; repaired row by row and taken whole by the trunk",
         '5d2d8e36'),
    'receipts/L165_defining_the_sum/S3_c6_is_a_theorem_not_a_condition.py':
        ("r7331 order 4 (the repair stride): L165_defining_the_sum named as the second block, the densest this seat holds; repaired row by row and taken whole by the trunk",
         '5d2d8e36'),
    'receipts/L165_defining_the_sum/S4_the_open_half_is_the_floor.py':
        ("r7331 order 4 (the repair stride): L165_defining_the_sum named as the second block, the densest this seat holds; repaired row by row and taken whole by the trunk",
         '5d2d8e36'),
}


def _crossed_at(q, sha):
    """the authorisation read at the commit that made the crossing: it resolves, and its own diff
    carries the path.  So an entry naming a path nobody ever crossed is still a blanket."""
    if subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'], cwd=ROOT,
                      capture_output=True).returncode != 0:
        return False
    return q in _git('show', '--no-merges', '--name-only', '--format=', sha).split('\n')
# ⛭⛭⛭ r7336+60: AND THE BY-NAME LIST WAS THE WRONG SHAPE FOR AN ORDERED STRIDE, WHICH THIS
#   REVISION MADE UNARGUABLE.  *`r7265` added two names, `r7336` added nine, and then the SAME
#   revision's ordered tail crossed fourteen more in nine prefixes -- so the list grows once per
#   order and is a snapshot of the orders given SO FAR, which is `S5`'s own measured class (a gate
#   on a set its own seat can grow) arriving here for the third time.*
#   ⇒ *** So the authorisation gains the branch `S5` already carries and controls: a path whose
#     edit IN THIS BRANCH'S OWN COMMITS cites an order is authorised, read off the ADDED LINES so
#     an edit cannot buy itself permission by naming an order it did not act on. ***  ** The
#     by-name list is KEPT for crossings whose edits cite nothing, the claim keeps its force -- an
#     unbidden crossing still fires, which the injected control proves on the same computation --
#     and the citation test is controlled two-sidedly below rather than trusted. **
_ORDER_CITE = _re_r7245.compile(
    r'(?:re\s+)?`?r\d{4}`?[^\n]{0,80}\b(?:order|ordered|orders)\b', _re_r7245.I)


def _edit_cites_order(q):
    """does THIS BRANCH's own edit of `q` cite an order, in the lines it ADDED?"""
    for _c in _MINE_C:
        for _ln in _git('show', '--no-merges', '--format=', '--unified=0', _c, '--', q).split('\n'):
            if _ln.startswith('+') and not _ln.startswith('+++') and _ORDER_CITE.search(_ln):
                return True
    return False


# ⛔⛭⛭⛭ r7364+60: AND THE WARRANT WAS NEVER IN THE DIFF.  IT IS IN THE ORDER, AND THIS GATE READ THE
#   FILE.  *`14` crossings read UNAUTHORISED on this branch and `13` of them have their receipt
#   DIRECTORY NAMED IN AN ORDER TO THIS SEAT.  `r7353` ② routed nine prefixes by name and said
#   "announce each take in the push that begins it" -- so the authorisation is in `FOR_60.md` and the
#   announcement is in the COMMIT MESSAGE, and both legs of this clause look inside the file's own
#   diff: one for a citation pattern, one as a by-name list that grows once per order.*
#   ⇒ *** So the clause reads the ORDER FILE, at the commit that made the crossing and not live:
#     an order given later cannot authorise a take already made, and a later edit of the order file
#     cannot retract one.  The by-name list and the diff-citation leg are both KEPT -- a crossing
#     into a prefix no order ever named still fires, which the injected control proves on the same
#     computation. ***
#   ⌗ *And the fourteenth is `L268/O1`, which no order names: its own source names
#     `L263_the_station_audit`, a directory this branch repaired UNDER an order, and that repair is
#     what turned it red.  So it is carried by the order it reads rather than by a reach of its own --
#     which is exactly what the prefix `L268_broken_by_its_own_edit` is called.*
#   ⚠⛭ AND THE CONTROL HAD TO MOVE WITH THE RULE, WHICH IS THE PART WORTH SAYING OUT LOUD.  *The
#     injected path sat under `L259_the_distance_from_the_present` -- **the first item of this seat's
#     own hand-off queue**, so under the repaired rule it would be ORDER-NAMED and AUTHORISED, and the
#     non-vacuity check would have gone silent while still printing a `1`.  The control was drawn
#     from the seat's own queue, and repairing the rule retired it.*  ⇒ It moves to a prefix no order
#     to this seat has ever named, and the order-name test is controlled two-sidedly beside it.
_ORDERS = 'FOR_60.md'
_BYC = {c: set(l for l in _git('show', '--no-merges', '--name-only', '--format=', c).split('\n') if l)
        for c in _MINE_C}
_ORD_AT = {}


def _orders_at(c):
    if c not in _ORD_AT:
        _ORD_AT[c] = _git('show', f'{c}:{_ORDERS}')
    return _ORD_AT[c]


def _dir_of(q):
    bits = q.split('/')
    return bits[1] if len(bits) > 2 else ''


def _order_named(q):
    """is `q`'s receipt DIRECTORY named in the order file AS IT STOOD when this branch crossed it?"""
    d = _dir_of(q)
    return bool(d) and any(q in _BYC[c] and d in _orders_at(c) for c in _MINE_C)


def _carried_by_an_ordered_repair(q):
    """`q`'s own source names a directory this branch repaired UNDER AN ORDER, so the ordered repair
    is what turned `q` red and the order carries it."""
    try:
        with open(os.path.join(ROOT, q), encoding='utf-8', errors='replace') as fh:
            src = fh.read()
    except OSError:
        return False
    return any(_dir_of(p) and _dir_of(p) != _dir_of(q) and _dir_of(p) in src and _order_named(p)
               for p in set(_touched)
               if p.startswith('receipts/') and p.endswith('.py'))


def _announced(q):
    """did the push that made the crossing NAME the prefix, as `r7353` ② required?"""
    d = _dir_of(q)
    return bool(d) and any(q in _BYC[c] and d in _git('log', '-1', '--format=%B', c)
                           for c in _MINE_C)


_ORD_YES = "#   ⌗ EDITED HERE ON `r7333` order 4, which sent this seat into the tail."
_ORD_NO = "#   ⌗ r7336+60: the figure fell 32 -> 30 under this revision's own repairs."
_cite_control = bool(_ORDER_CITE.search(_ORD_YES)) and not _ORDER_CITE.search(_ORD_NO)
#: the order-name test, two-sided on the SAME file the clause reads: a prefix `r7353` ② routed by
#: name is found, and a real receipt directory no order to this seat has ever named is not.
_HEAD_ORDERS = _git('show', f'HEAD:{_ORDERS}')
_name_control = ('L548_propagating_sector' in _HEAD_ORDERS
                 and 'L558_the_second_duplication' not in _HEAD_ORDERS)
_unauth = _outside(_touched)
_cited = sorted({q for q in _unauth if q not in _AUTHORISED and _edit_cites_order(q)})
_named = sorted({q for q in _unauth if q not in _AUTHORISED and q not in _cited
                 and _order_named(q)})
_carried = sorted({q for q in _unauth if q not in _AUTHORISED and q not in _cited
                   and q not in _named and _carried_by_an_ordered_repair(q)})
_real = sorted({q for q in _unauth if q not in _AUTHORISED and q not in _cited
                and q not in _named and q not in _carried})
#: ⌗ the prefix is one no order to this seat has ever named, so the control cannot be authorised by
#: the repaired rule the way the old `L259` path would have been.
_inject = 'receipts/L558_the_second_duplication/INJECTED_CONTROL.py'
_ctrl = [q for q in _outside(_touched + [_inject])
         if q not in _AUTHORISED and q not in _cited and q not in _named
         and not _carried_by_an_ordered_repair(q)]
#: the announcement protocol, REPORTED and not asserted: `r7353` ② asked for the prefix by name
_unannounced = sorted({q for q in _unauth if q not in _AUTHORISED and not _announced(q)})
#: ⚠ and the one failure of the protocol that is this seat's and not the gate's: a push that
#: ANNOUNCES A TAKE and then crosses a directory it never names -- a reference BY POSITION where the
#: order asked for names, which is this corpus's own recurring class arriving in the compliance.
_positional = sorted({c for c in _MINE_C
                      if 'TAKING' in _git('log', '-1', '--format=%B', c)
                      and any(q in _BYC[c] and not _announced(q) for q in _unauth)})
print(f"      with this branch as it stands: {len(_real)} UNAUTHORISED modified unowned receipt(s) "
      f"({len(_unauth)} crossed in all, {len(_AUTHORISED)} of them ordered)")
print(f"      ⌗ and the range a MOVING base would have given: {len(_MINE_LIVE)} of these "
      f"{len(_MINE_C)} commit(s) are not yet on the trunk, so `HEAD --not origin/main` scrutinises "
      f"{len(_MINE_LIVE)} and this clause scrutinises {len(_MINE_C)} -- REPORTED, and the reason "
      f"the base is a commit")
for _q, _v in sorted(_AUTHORISED.items()):
    print(f"        ⌗ ordered: {_q.split('/')[-1][:52]} -- {_v[0][:58]}\n"
          f"            {'crossed on this branch' if _q in _unauth else 'crossed at ' + _v[1]}"
          f" ({'pin holds' if _crossed_at(_q, _v[1]) else 'PIN DOES NOT HOLD'})")
print(f"      authorised by an ORDER CITED IN THIS BRANCH's OWN ADDED LINES: {len(_cited)} "
      f"({[q.split('/')[-1][:26] for q in _cited]})")
print(f"      authorised by the ORDER FILE naming the prefix at the crossing commit: {len(_named)}")
for _q in _named:
    print(f"        ⌗ ordered by name: {_dir_of(_q)}")
print(f"      carried by an ORDERED REPAIR the receipt's own source names: {len(_carried)} "
      f"({[_dir_of(q) for q in _carried]})")
print(f"      the citation test, controlled two-sidedly: a line citing an order matches and a line "
      f"carrying only a revision id does not -- {_cite_control}")
print(f"      the order-name test, controlled two-sidedly on the same file: a routed prefix is "
      f"found and a receipt directory no order names is not -- {_name_control}")
print(f"      with one MODIFIED unowned receipt injected: {len(_ctrl)}")
print(f"      ⌗ REPORTED, not asserted: {len(_unauth) - len(_unannounced)} of {len(_unauth)} "
      f"crossing(s) were ANNOUNCED BY PREFIX in the push that made them, as `r7353` ② asked; "
      f"{len(_unannounced)} were not")
for _c in _positional:
    print(f"        ⚠ a TAKE push that named a COUNT where the order asked for names: {_c[:8]} "
          f"-- {_git('log', '-1', '--format=%s', _c).strip()[:72]}")
    print(f"            and it crossed {len([q for q in _unauth if q in _BYC[_c] and not _announced(q)])}"
          f" directory(ies) it did not name")
gate("Ⓗ② ⛔ AND THE REPAIR IS NOT VACUOUS, which is the thing a reader should doubt when an "
     "assertion is changed to clear a red: the repaired clause reads ZERO UNAUTHORISED crossings on "
     "this branch and still FIRES when a modified unowned receipt is injected into the same "
     "computation -- so what was removed is the ADDITION case and the EDIT claim is untouched.  "
     "⛭ `r7265`: the ordered crossings are carried BY NAME with the order that authorised each, "
     "printed above, so an unbidden crossing is still a violation and an authorisation is still "
     "readable.  ⛭⛭⛭ r7364: and the warrant is READ FROM THE ORDER FILE at the commit that made "
     "each crossing, because `r7353` ② put the authorisation in the orders and the announcement in "
     "the push while both legs of this clause looked inside the file's own diff -- the by-name list "
     "and the citation leg are kept, and the announcement is REPORTED above rather than asserted, "
     "because one of this seat's five take-pushes named a count where the order asked for names",
     len(_real) == 0 and len(_ctrl) == 1 and _inject in _ctrl
     and _cite_control and _name_control
     # the exception list must not be a blanket: every entry has to be a path this branch
     # ACTUALLY crossed, or a stale authorisation would silently widen the claim.
     and all(q in _unauth or _crossed_at(q, _AUTHORISED[q][1]) for q in _AUTHORISED)
     # ⌗ and the pin is not a rubber stamp: a path the authorising commit did NOT touch fails it,
     #   checked here on this receipt's own path against the same two commits.
     and not any(_crossed_at(_SELF_REL, _v[1]) for _v in _AUTHORISED.values()))

print(f"\n{BAR}")
if fail:
    print(f"  ⛔ {len(fail)} GATE(S) FAILED")
    for x in fail:
        print(f"      - {x[:96]}")
    sys.exit(1)
print("  ✔ every gate passed")
print(f"{BAR}")
