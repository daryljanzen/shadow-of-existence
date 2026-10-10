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


_touched = [l for l in _git('log', '--no-merges', '--name-only', '--format=',
                            'HEAD', '--not', 'origin/main').split('\n') if l]
_added = {l for l in _git('log', '--no-merges', '--diff-filter=A', '--name-only', '--format=',
                          'HEAD', '--not', 'origin/main').split('\n') if l}


def _owned(q):
    return q.startswith('receipts/P15_CR_cosmology/') or q.startswith('receipts/L_probability/S')


def _outside(paths):
    return [q for q in paths
            if q.startswith('receipts/') and q.endswith('.py') and not _owned(q) and q not in _added]


_real = _outside(_touched)
_inject = 'receipts/L259_the_distance_from_the_present/INJECTED_CONTROL.py'
_ctrl = _outside(_touched + [_inject])
print(f"      with this branch as it stands: {len(_real)} modified unowned receipt(s)")
print(f"      with one MODIFIED unowned receipt injected: {len(_ctrl)}")
gate("Ⓗ② ⛔ AND THE REPAIR IS NOT VACUOUS, which is the thing a reader should doubt when an "
     "assertion is changed to clear a red: the repaired clause reads ZERO on this branch and still "
     "FIRES when a modified unowned receipt is injected into the same computation -- so what was "
     "removed is the ADDITION case and the EDIT claim is untouched",
     len(_real) == 0 and len(_ctrl) == 1 and _inject in _ctrl)

print(f"\n{BAR}")
if fail:
    print(f"  ⛔ {len(fail)} GATE(S) FAILED")
    for x in fail:
        print(f"      - {x[:96]}")
    sys.exit(1)
print("  ✔ every gate passed")
print(f"{BAR}")
