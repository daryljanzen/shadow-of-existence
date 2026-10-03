#!/usr/bin/env python3
"""P15 -- THE FREEZING CENSUS IS THE VACUUM CURVE'S OWN RATE, READ ON THE BRANCH THE LIFT IS NOT ON.

** THIS ANSWERS `PO-77` ⓵ AND IT ANSWERS IT AGAINST NODE 70's OWN READING, ON THE CHECK 70 ASKED FOR. **
*`70` established that every computed freezing census evaluates `$(rH)^2$` at POSITIVE `$r$`, and read that as
the LEAF's -- then named the one thing that would change the answer: whether that positive `$r$` is the leaf
or `$\\lvert r\\rvert$` on the vacuum curve.*  ⇒ *** It is the vacuum curve.  `C2` says so in its own words at
the line where it sets the radiation term: `Take the vacuum case A=0 first, which is the pure bead`. ***

  ⓵ ** BOTH CENSUS RECEIPTS COMPUTE WITH NO RADIATION TERM. **  *`C2` and
    `P15_the_locus_is_wrong_in_six_places_...` share one function, `rH2(r, A=0.0)`, and **every census call
    uses the default.**  The locus receipt does define `A_RAD = 4 M r_seam` --- the corpus's inherited
    `$\\rho_r/\\rho_m\\simeq2$` datum --- but uses it ONLY for the separate `$r_*$` maximum, never for the
    table.*  ⇒ *So the census carries no radiation and is not the leaf's.*

  ⓶ ** AND POSITIVE `$r$` WITH `$\\lvert r\\rvert<A$` IS THE EXPANSION LEG. **  *The collapse leg is
    `$r=A\\cosh^{2/3}x\\ge A$` and never descends below `$A$`; the expansion leg runs `$0\\to\\infty$`.*
    ⇒ *** So the freezing census is computed on the bead's EXPANSION leg --- the stretch that FOLLOWS the
    kernel, read backwards --- and not on the contracting side that precedes it. ***

  ⓷ ** ON THE CONTRACTING SIDE THE SAME RATE FALLS TO EXACTLY ZERO AT THE TURNAROUND. **  *`$1-f=0$` at
    `$\\lvert r\\rvert=(2M)^{1/3}$`, which IS `$A$` identically.  **So where the lift begins every mode is
    inside the horizon**, and the census's `grows without bound` is false on that branch.*

  ⓸ *** AND THE PAPER'S THREE FIGURES SIT ON TWO BRANCHES, WITH THE FIRST UNREPRODUCIBLE AT THE LOCUS IT
    NAMES --- `70`'s `R2`, VERIFIED AND SHARPENED. ***  *`1.96` and `19.6` are the positive-branch vacuum
    rate normalised at the seam, where it is exactly `1`.  **But `$0.13$` cannot occur on that branch at all:
    the normalised rate's minimum over `$r>0$` is exactly `1.0`, at the seam.**  And at the comoving
    turnaround the sentence attributes `$0.13$` to, the rate is `$0$` --- `$0.13$` is reached near `$A$` on
    the signed-negative branch, at `$\\lvert r\\rvert=0.7197$` or `$0.7352$`, within `1.1` per cent of it.*

  ⓹ ** WHAT `70`'s THRESHOLD THEN SAYS, AND IT STANDS: A RADIATION-CARRYING CONGRUENCE HAS NO LIFT AT ALL
    HERE. **  *The double root of `$A_r/x^2-2M/x+x^2$` is `$A_r^*=3\\cdot2^{2/3}M^{4/3}/4$`, re-derived
    symbolically, which against the corpus's datum `$A_r=4Mr_{\\rm seam}$` is a threshold of
    `$\\rho_r/\\rho_m=3\\cdot2^{2/3}/8=0.5953$` at the seam against an inherited `2`.*  ⇒ *** So the kernel
    belongs to the vacuum curve alone, and the census belongs to its expansion leg.  The two are the same
    curve read on opposite sides of its turnaround. ***

** WHAT THIS LEAVES, STATED AS THE NARROWING IT IS. **  *`PO-77` ⓵ asked which congruence's horizon decides
`frozen` at the lift.  **The answer is that no computed census is about that stretch at all** --- one is on the
expansion leg, and the radiation-carrying description has no lift to decide at.*  ⛔ *It does NOT settle ⓪ or
⓶, and it does not say what the census ON the contracting side would be: nothing in the corpus computes one.*

** COMPUTES: the two census receipts' own `rH2` with its own default (no parameter of this file's choosing);
the positive-branch minimum over a dense sweep; the turnaround locus symbolically; the signed-negative rate at
two radii; and the radiation threshold's double root symbolically.  *** THE ONLY NUMBERS PINNED ARE THE
PAPER'S OWN THREE AND THE CORPUS'S OWN DATUM, *** in the gauge those receipts set (`alpha = 1`, Nariai
`M = 1/(3 sqrt3)`), which is read from them rather than chosen here. **

Written r7131 by node 66 (the gate), on the check node 70 named as the one that would change its answer.
Stated for reversal.
"""
import io
import os
import sys

import numpy as np
import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
C2 = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', 'C2_horizon_limits.py')
LOCUS = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                     'P15_the_locus_is_wrong_in_six_places_and_the_lint_cannot_see_the_worst.py')

_n = [0, 0]


def gate(label, ok):
    _n[0] += 1
    if ok:
        _n[1] += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def head(t):
    print()
    print('  ' + '=' * 92)
    print('  ' + t)
    print('  ' + '=' * 92)


print()
print('RECEIPT -- P15: ** THE FREEZING CENSUS IS THE VACUUM CURVE\'S OWN RATE ON THE BRANCH THE LIFT IS NOT')
print('ON, AND THE TURNAROUND FIGURE IS EXACTLY ZERO THERE.  `PO-77` ⓵, ANSWERED AGAINST NODE 70\'s READING')
print('ON THE CHECK 70 ITSELF NAMED. **')

b15 = io.open(P15, encoding='utf-8').read()
bc2 = io.open(C2, encoding='utf-8').read()
blo = io.open(LOCUS, encoding='utf-8').read()

# the gauge is READ from the census receipts, not chosen here
M = 1.0 / (3.0 * np.sqrt(3.0))
A = 2.0 ** (1.0 / 3.0) / np.sqrt(3.0)
SEAM = 1.0 / np.sqrt(3.0)


def rH2(r, Ar=0.0):
    """the two census receipts' own function, with their own default"""
    return Ar / r ** 2 + 2.0 * M / r + r ** 2


ref = np.sqrt(rH2(SEAM))

# ===========================================================================
head('A.  THE CENSUS CARRIES NO RADIATION TERM, AND `C2` SAYS SO IN ITS OWN WORDS')
# ===========================================================================
gate("⓵ `C2` declares the vacuum case in terms: `Take the vacuum case A=0 first, which is the pure bead` -- "
     "LOCATED in the current source.  ⇒ ** So the object its census is about is named by the receipt itself **",
     'Take the vacuum case A=0 first, which is the pure bead' in bc2)

gate("⇒ and both census receipts share one function signature with the radiation term DEFAULTED OFF, "
     "`def rH2(r, A=0.0)` -- located in both",
     'def rH2(rr, A=0.0)' in bc2 and 'def rH2(r, A=0.0)' in blo)

_DATUM = 'A_RAD = 4.0 * MASS * R_SEAM' in blo
_TABLE_NO_AR = 'aH = np.sqrt(rH2(r)) / _ref' in blo
gate("⓶ and the locus receipt DOES define the corpus's inherited datum, `A_RAD = 4 M r_seam` for "
     "`$\\rho_r/\\rho_m\\simeq2$` at the seam -- ** but its census table calls `rH2(r)` with no `A`, so the "
     "datum never enters the table ** and is used only for the separate `$r_*$` maximum",
     _DATUM and _TABLE_NO_AR)

gate(f"⌗ and the normalisation is exact, which is why the paper's figures are pure ratios: "
     f"`$\\sqrt{{(rH)^2}}$` at the seam is {ref:.10f}",
     abs(ref - 1.0) < 1e-12)

# ===========================================================================
head('B.  POSITIVE `$r$` BELOW `$A$` IS THE EXPANSION LEG, NOT THE CONTRACTING SIDE')
# ===========================================================================
x = sp.symbols('x', positive=True)
Ms, als = sp.symbols('M alpha', positive=True)
Asym = 2**sp.Rational(1, 3) * als / sp.sqrt(3)
gate(f"⓷ the collapse leg is `$r=A\\cosh^{{2/3}}x$`, whose minimum is `$A={A:.6f}\\alpha$`, so it never "
     f"descends below `$A$`; the expansion leg runs `$0\\to\\infty$` and is the only leg covering "
     f"`$\\lvert r\\rvert<A$`.  ⇒ ** The census's sampled radii `$0.1\\alpha$` and `$10^{{-3}}\\alpha$` are "
     f"on the EXPANSION leg **",
     0.1 < A and 1e-3 < A)

# the turnaround, symbolically: 1 - f = 0 on the signed-negative branch
turn = sp.solve(sp.Eq(-2 * Ms / x + x**2, 0), x)
M_nar = 1 / (3 * sp.sqrt(3)) * als**0
turn_val = sp.simplify(turn[0].subs(Ms, 1 / (3 * sp.sqrt(3))))
gate(f"⓸ and on the signed-negative branch the rate VANISHES at `$\\lvert r\\rvert=(2M)^{{1/3}}$`, which at "
     f"the Nariai mass is `${sp.nsimplify(turn_val)}$` = `{float(turn_val):.7f}` -- ** identically `$A$` **.  "
     f"⇒ *So where the lift begins `$aH=0$` exactly and EVERY mode is inside the horizon*",
     abs(float(turn_val) - A) < 1e-12)

# ===========================================================================
head('C.  THE PAPER\'S THREE FIGURES SIT ON TWO BRANCHES, AND THE FIRST CANNOT OCCUR ON THE OTHERS\'')
# ===========================================================================
v1, v2 = np.sqrt(rH2(0.1)) / ref, np.sqrt(rH2(1e-3)) / ref
#: the first figure WITH its radius is the clause; `'$19.6$ at'` was a truncated second arm that
#: would survive its own radius being reworded, so it is dropped rather than baselined.
_F = '$1.96$ at $\\lvert r\\rvert=0.1\\,\\alpha$' in b15
gate(f"⓹ the paper's `1.96` and `19.6` reproduce on the POSITIVE branch as {v1:.4f} and {v2:.4f}, "
     f"normalised at the seam -- located in the current source",
     abs(v1 - 1.96) < 0.01 and abs(v2 - 19.6) < 0.1 and _F)

rs = np.linspace(1e-4, 3.0, 400000)
pos_min = float(np.min(np.sqrt(rH2(rs)) / ref))
argmin = float(rs[int(np.argmin(rH2(rs)))])
gate(f"⓺ *** BUT `$0.13$` CANNOT OCCUR ON THAT BRANCH AT ALL: the normalised rate's minimum over `$r>0$` is "
     f"{pos_min:.6f}, attained at `$r={argmin:.6f}\\alpha$` --- the seam. *** ⇒ *So the sentence's first "
     f"figure is on a different branch from its other two*",
     abs(pos_min - 1.0) < 1e-5 and abs(argmin - SEAM) < 1e-3)

#: ⛭ THE CURRENT STATE, NOT THE DEFECT.  A first draft asserted the paper still carried
#: `$0.13$ at the comoving turnaround` -- and the finding below is WHY that figure was removed, so
#: the check went red on the success of its own work.  That is instance ten of the pattern in this
#: programme and the second in this seat's own files.  ⇒ Per `L-249`'s rule (r3105): assert the
#: CURRENT state, and let the computation carry the finding.  The clause the argument reasons from
#: is that the paper no longer attributes a NONZERO rate to the turnaround.
_013 = '0.13' not in b15


def aH_neg(xx):
    return np.sqrt(abs(-2.0 * M / xx + xx ** 2)) / ref


at_turn = aH_neg(A)
n1, n2 = aH_neg(0.7197), aH_neg(0.7352)
gate(f"⓻ ⛔ AT THE COMOVING TURNAROUND THE RATE IS ZERO, NOT `$0.13$`: `$aH$` there is {at_turn:.2e}.  "
     f"`$0.13$` is reached NEAR `$A$` on the signed-negative branch instead -- {n1:.4f} at "
     f"`$\\lvert r\\rvert=0.7197$` (inside `$A$`) and {n2:.4f} at `$0.7352$` (outside it), both within "
     f"`1.1` per cent of `$A$`.  ⇒ *Node 70's `R2`, verified and sharpened: the figure was never wrong "
     f"in value, only in the locus it was attributed to* -- ** and the paper no longer carries it, "
     f"which is what this gate asserts rather than the defect **",
     at_turn < 1e-12 and abs(n1 - 0.13) < 0.01 and abs(n2 - 0.13) < 0.01 and _013)

# ===========================================================================
head('D.  AND A RADIATION-CARRYING CONGRUENCE HAS NO LIFT HERE -- 70\'s THRESHOLD, RE-DERIVED')
# ===========================================================================
Ar = sp.symbols('A_r', positive=True)
g = Ar / x**2 - 2 * Ms / x + x**2
sol = sp.solve([sp.Eq(g, 0), sp.Eq(sp.diff(g, x), 0)], [x, Ar], dict=True)
Ar_star = sp.simplify(sol[0][Ar])
gate(f"⓼ the double root of `$A_r/x^2-2M/x+x^2$` is `$A_r^*={sp.latex(Ar_star)}$`, derived symbolically -- "
     f"** below it a Euclidean segment exists, above it the rate never vanishes **",
     sp.simplify(Ar_star - 3 * 2**sp.Rational(2, 3) * Ms**sp.Rational(4, 3) / 4) == 0)

Ar_datum = 4 * Ms * als / sp.sqrt(3)
ratio = sp.simplify((Ar_star / Ar_datum).subs({Ms: 1 / (3 * sp.sqrt(3)), als: 1}))
thresh = sp.simplify(2 * ratio)
gate(f"⇒ *** against the corpus's own datum `$A_r=4Mr_{{\\rm seam}}$` that is a threshold of "
     f"`$\\rho_r/\\rho_m={sp.latex(sp.nsimplify(thresh))}={float(thresh):.4f}$` at the seam, against an "
     f"inherited `2` --- {float(2 / thresh):.2f} times over. *** ⇒ ** So the radiation-carrying description "
     f"has no lift at all, and the kernel belongs to the vacuum curve alone **",
     sp.simplify(thresh - 3 * 2**sp.Rational(2, 3) / 8) == 0 and float(thresh) < 2)

# ===========================================================================
head('E.  SCOPE -- WHAT THIS ANSWERS AND WHAT IT LEAVES')
# ===========================================================================
gate("⇒ ** `PO-77` ⓵ asked which congruence's horizon decides `frozen` at the lift.  THE ANSWER IS THAT NO "
     "COMPUTED CENSUS IS ABOUT THAT STRETCH: ** one is the vacuum curve's own rate on its EXPANSION leg, and "
     "the radiation-carrying description has no lift to decide at.  ⇒ *The census and the lift are the same "
     "curve read on opposite sides of its turnaround*",
     'Take the vacuum case A=0 first, which is the pure bead' in bc2 and at_turn < 1e-12)

#: ⛭ r7141 (66): this scope statement was a `gate(...)` whose condition was `'<module>' in sys.modules`
#: -- true whatever the receipt measured, so it added a PASS to `N of N checks pass` for a
#: sentence that tests nothing.  ** Node 70's `--cannot-fail` operator found all four of its
#: TRIVIAL-ENV sites in this seat's own two receipts (r7139+70.1), which is the right place for
#: a ruling to land first. **  ⇒ The defect is the COUNT, not the sentence: scope is PRINTED
#: here and no longer counted.  Same ruling as the 63 SCOPE-AS-CHECK sites.
print("  ⛔ NOT claimed: that `PO-77` ⓪ or ⓶ is settled; that the `$0.13$` figure's VALUE is wrong (it is")
print("     right near `$A$` on the signed-negative branch, and only its stated locus is); that any")
print("     transfer is retired; or that what a census ON the contracting side would say is known --")
print("     nothing in the corpus computes one, and that absence is the finding rather than a gap this")
print("     file fills.")

print()
print('  ' + '=' * 92)
print(f"  {_n[1]} of {_n[0]} checks pass")
if _n[1] == _n[0]:
    print('  ALL PASS -- the freezing census is the vacuum curve\'s own rate with the radiation term off, read')
    print('  at positive r, which below A is the EXPANSION leg.  On the contracting side the same rate is')
    print('  exactly zero at the turnaround, where the lift begins, so every mode is inside the horizon')
    print('  there.  The paper\'s 0.13 cannot occur on the branch its other two figures are on, and at the')
    print('  locus it names the rate is zero.  And a radiation-carrying congruence has no lift at all above')
    print('  rho_r/rho_m = 0.5953, against an inherited 2.')
print('  ' + '=' * 92)
#: the non-zero exit is written OUT so `check_receipt_exit` can see the failure path statically.
if _n[1] != _n[0]:
    sys.exit(1)
sys.exit(0)
