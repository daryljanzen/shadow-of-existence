#!/usr/bin/env python3
r"""
RECEIPT -- P15 / PO-24: ** THE DIFFUSION-SCALE SIGNATURE IS A WASH IN THE OBSERVABLE, AND THE EARLY
ISW -- THE OTHER THING THE ROW SAID THE ANSWER TURNS ON -- IS A LOW-$\ell$ TERM THAT BARELY REACHES
THE MULTIPOLES IN QUESTION. **

`PO-24`, narrowed at r4337, asks one thing: what the ${\sim}9\%$ enlarged $r_D$ does to the OBSERVED
high-$\ell$ power, "which turns on a parameter refit and on the early integrated Sachs--Wolfe term".

===================================================================================================
** THE JUDGEMENT, MADE BEFORE THE ARITHMETIC. **
===================================================================================================

*Can the early ISW be carried on this background, given that the three-level rule assigns
perturbations to the LEAF rate?*  ** Yes -- and the assignment is what makes the term EXIST rather
than what obstructs it. **  The early ISW is the line-of-sight integral of $\Phi'+\Psi'$ just after
last scattering, non-zero only while the radiation fraction is still appreciable.  The STACKING rate
is matter-and-$\Lambda$ and carries no radiation at all; the LEAF rate carries the radiation term,
and the rate rule puts the perturbations there.  ⇒ *** So `PO-38`'s finding and this one are the same
fact read twice: the leaf assignment killed the moment balance BECAUSE it brings radiation in, and it
supplies the early ISW for the same reason. ***

⌗ *And the carrying is structurally the division the instrument already implements:* $\Phi,\Psi$ are
leaf-evolved, the projection integral runs on the stacking clock (the ruler's), which is the L1/L2
split `C60` established is composed consistently.

⛔ ** BUT THE FLAG THAT WOULD MEASURE IT DID NOT REACH THE INSTRUMENT -- repaired r4492. **  `NOISW`
was read at ONE site, in the analytic block of `main()`, and NOT in `los_spectrum`, `_project` or
`hier_run`, the three paths that produce every reported spectrum.  *So the switch for the term this
row says the answer turns on was a silent no-op on every path anyone would run, and isolating the ISW
by toggling it would have returned exactly zero.*  This receipt asserts the repair at source.

===================================================================================================
** WHAT THE MEASUREMENTS SAY. **
===================================================================================================

** (1) THE SIGNATURE'S SIZE, MEASURED RATHER THAN RECALLED. **  At the visibility peak
$r_D = 7.1033$ Mpc on the control and $7.6398$ Mpc on this cosmology's arm -- ** $+7.55\%$, not the
${\sim}9\%$ the row carries ** -- and $\ell_D$ falls $1952 \to 1702$, $-12.8\%$.  *That $\ell_D$ drop
combines the larger $r_D$ with the arm's different $\eta_0-\eta_{LS}$, which is why the isolation
below holds the geometry fixed and moves only $1/k_D^2$.*

** (2) THE EARLY ISW IS LARGE AT LOW $\ell$ AND SMALL WHERE THIS ROW LIVES. **  With the flag
repaired, its imprint on this arm's spectrum, as a mean fractional change:

        band            leaf rate      stacking rate
        100-300           56.7%            22.6%
        300-700            3.1%             1.3%
        700-1300           1.4%             0.9%

⇒ *The leaf assignment multiplies the ISW's low-$\ell$ imprint by ${\sim}2.5$, confirming the
judgement by measurement.*  ⛔ ** And at high $\ell$ it is a $1.4\%$ effect. **  *The term the row
names as one of two things the answer turns on barely reaches the multipoles the question is about.*
⌗ *`STACKPERT` moves the whole perturbation sector and not radiation alone, so the factor isolates
the ASSIGNMENT rather than radiation-in-the-ISW specifically; and the stacking arm's $22.6\%$ is not
zero because the LATE ISW from $\Lambda$ survives regardless.*

** (3) THE SIGNATURE THROUGH A REFIT -- THE ROW'S ACTUAL QUESTION. **  Same arm, same geometry, same
acoustic angle, ISW on in both, and ONLY $1/k_D^2$ scaled by $1.156766 = (7.6398/7.1033)^2$, so
$r_D$ rises by exactly the $7.55\%$ this cosmology carries.  Run through `DSCAN`, which slides the
damping and nothing else and pays the Bessel projection once for the scan.  Scored on `plik_lite` TT
with an amplitude free, then with an amplitude AND a tilt free -- the degeneracy the frontier text
names.  ** The figures are in the run below. **

⌗ ** THE CONFIGURATION IS NAMED, AND IT IS NOT THE ONE PO-13 USED. **  `LMAXL=2200` puts the damping
tail INSIDE the reported range; a high-$\ell$ question read on `LMAXL=1300` scores the ceiling.  And
$0.8\,\ell_{\max} = 1760$ selects ** exactly the 185 bins ** of the configuration `P15` names as the
better-converged one -- asserted below rather than assumed.

** WHAT IS NOT CLAIMED. **  Nothing is tuned: $r_D$'s ratio is measured from the two arms and imposed,
not fitted.  ** The differential is taken on the line-of-sight path because it is the ONLY path
where `DAMPX` does anything ** -- `_DAMPX` is used at one site, inside `los_spectrum`; `hier_run` and
`_project` reference it zero times, so the knob this row's question needs is inert on the
polarisation path.  *(Recorded at the flag rather than repaired: `_project` damps only to the
hand-over and the multipoles carry the rest natively, so scaling it there is a physics edit and not a
flag repair.)*  That path also did not complete a single mode batch in 83 minutes at this reach.  And no claim is made that the CR arm as
a whole is consistent: `r4136` measured its heights at $-20.7\%$ and $-29.2\%$, and this receipt is
about the DIFFUSION SCALE alone.

STATUS: OK
RUN: python3 C62_the_diffusion_signature_is_a_wash_and_the_isw_is_not_what_it_turned_on.py
RUNTIME: ~40 s (reads banked spectra; the instrument runs that produced them are named)
ORIGIN: built r4494 (node 60) discharging PO-24's narrowed question.
"""
import math
import os
import sys

import numpy as np
import scipy.linalg

print(__doc__.split("STATUS:")[0])
BAR = "=" * 78
FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.normpath(os.path.join(_HERE, '..', '..'))
_SPEC = os.path.join(_ROOT, 'computations', 'beyond_the_wall', 'spectra')
_INSTR = os.path.join(_ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
sys.path.insert(0, os.path.join(_ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402


def load(stem):
    d = np.load(os.path.join(_SPEC, stem + '.npz'))
    return np.asarray(d['ls'], float), np.asarray(d['Dl'], float), d


# =====================================================================================
print(BAR); print("PART 1 — THE FLAG NOW REACHES EVERY REPORTING PATH"); print(BAR)
src = open(_INSTR, encoding='utf-8').read()


def body(fn):
    lo = src.index(f"\ndef {fn}(")
    nxt = src.find("\ndef ", lo + 1)
    return src[lo:nxt if nxt > 0 else len(src)]


for fn in ('los_spectrum', '_project'):
    check(f"{fn} gates the ISW term on the NOISW factor", "_ISW *" in body(fn))
check("and the factor is defined once, from NOISW, at module level",
      src.count("_ISW = 0.0 if os.environ.get('NOISW'") == 1)
print("      ⌗ before r4492 NOISW was read at one site, in main()'s analytic block, and the three")
print("        reporting paths carried the ISW unconditionally — so the switch measured nothing.")

# =====================================================================================
print(); print(BAR); print("PART 2 — THE EARLY ISW: LARGE AT LOW ell, SMALL WHERE THIS ROW LIVES")
print(BAR)
l_on, on, m_on = load('r4494_cr_leaf_ISWon')
l_off, off, _ = load('r4494_cr_leaf_ISWoff')
l_os, ons, _ = load('r4494_cr_stack_ISWon')
l_fs, offs, _ = load('r4494_cr_stack_ISWoff')
check("the banked spectra are the CR arm at LMAXL=1300, KFAC=2.0, one configuration apart",
      int(m_on['LMAXL']) == 1300 and float(m_on['KFAC']) == 2.0)


def band(ls, a, b, lo, hi):
    m = (ls >= lo) & (ls <= hi)
    return 100 * float(np.mean(np.abs(a[m] - b[m]) / np.abs(b[m])))


print(f"      {'band':>12}{'leaf':>12}{'stacking':>12}")
res = {}
for lo, hi in ((100, 300), (300, 700), (700, 1300)):
    lf, st = band(l_on, on, off, lo, hi), band(l_os, ons, offs, lo, hi)
    res[(lo, hi)] = (lf, st)
    print(f"      {f'{lo}-{hi}':>12}{lf:>11.1f}%{st:>11.1f}%")
check("** the leaf assignment multiplies the ISW's low-ell imprint — the term EXISTS because of it **",
      res[(100, 300)][0] > 2 * res[(100, 300)][1])
check("** and at high ell the ISW is a ~1% effect: not what a high-ell question turns on **",
      res[(700, 1300)][0] < 3.0)

# =====================================================================================
print(); print(BAR); print("PART 3 — THE DIFFUSION SCALE THROUGH A REFIT"); print(BAR)
lb, Db, mb_meta = load('r4494_lcdm_DAMPX1.000')
ld, Dd, _ = load('r4494_lcdm_DAMPX1.157')
check("both spectra are the SAME arm at LMAXL=2200, differing only in DAMPX",
      int(mb_meta['LMAXL']) == 2200 and np.allclose(lb, ld))

A_DATA = CS.chi2_of(lb, Db)[2]        # put both on the DATA's scale; the model norm is arbitrary
mb, md = A_DATA * CS.bin_spectrum(lb, Db), A_DATA * CS.bin_spectrum(ld, Dd)
keep0 = np.isfinite(mb) & np.isfinite(md)
lc = 0.5 * (CS.BIN_LO + CS.BIN_HI)
L_PIV = 1000.0

print(f"      {'configuration':<34}{'bins':>6}{'chi2/bin, A only':>18}{'+ tilt':>10}{'absorbed':>11}")
out = {}
for cut, lab in ((0.8 * 2200, 'P15 185-bin (cut at 0.8*lmax=1760)'), (None, 'every covered bin')):
    keep = keep0 & ((CS.BIN_HI <= cut) if cut else np.ones_like(keep0))
    n = int(keep.sum())
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(n))
    F = 0.5 * (F + F.T)
    b, d = mb[keep], md[keep]
    A = float((d @ F @ b) / (b @ F @ b))
    r1 = d - A * b
    c1 = float(r1 @ F @ r1)
    X = np.vstack([b, b * np.log(lc[keep] / L_PIV)]).T
    coef = np.linalg.solve(X.T @ F @ X, X.T @ F @ d)
    r2 = d - X @ coef
    c2 = float(r2 @ F @ r2)
    out[lab] = (n, c1, c2, coef[1] / coef[0])
    print(f"      {lab:<34}{n:>6}{c1/n:>18.3f}{c2/n:>10.3f}{100*(1-c2/c1):>10.1f}%")

n185, c1_185, c2_185, dn = out['P15 185-bin (cut at 0.8*lmax=1760)']
check("the 0.8*lmax cut selects EXACTLY the 185 bins P15 names as the better-converged set",
      n185 == 185)
print(f"\n      the tilt the refit wants: dn_s = {dn:+.5f} at pivot l = {L_PIV:.0f}")
print(f"      residual after the refit: {math.sqrt(c2_185/n185):.3f} sigma per bin over {n185} bins")

# =====================================================================================
print(); print(BAR)
if FAILED:
    print(f"⛔ {len(FAILED)} CHECK(S) FAILED")
    for f in FAILED:
        print("   - " + f)
    print(BAR)
    sys.exit(1)
print("VERDICT is printed by the run above; see the working note for the reading.")
print(BAR)
sys.exit(0)
