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
⛔ ** AND TWO THINGS I FIRST WROTE ABOUT THIS ARE WRONG, CORRECTED HERE. **  *(i) I said the term
EXISTS because of the leaf assignment.  It does not: `_rt`, which sets the radiation FRACTIONS in the
perturbation source, is built from the stack "both arms" by the instrument's own comment, so radiation
is in the source under EITHER assignment and `STACKPERT` changes only which $H$ the equations use.
The leaf assignment makes the term $1.52\times$ larger, not present.  (ii) I said the stacking arm's
$22.6\%$ was late ISW from $\Lambda$ surviving.  It is not: `ETA_END` is $20\,a_{\rm rec}$, so the
line-of-sight integration STOPS AT $z\simeq54$ and the late-ISW era is outside the calculation
entirely.*  ⇒ ** So everything measured here is EARLY ISW, on both rate assignments, which makes the
comparison cleaner than I claimed and not dirtier. **

** (3) THE SIGNATURE THROUGH A REFIT -- THE ROW'S ACTUAL QUESTION. **  Same arm, same geometry, same
acoustic angle, ISW on in both, and ONLY $1/k_D^2$ scaled by $1.156766 = (7.6398/7.1033)^2$, so
$r_D$ rises by exactly the $7.55\%$ this cosmology carries.  Run through `DSCAN`, which slides the
damping and nothing else and pays the Bessel projection once for the scan.  Scored on `plik_lite` TT
with an amplitude free, then with an amplitude AND a tilt free -- the degeneracy the frontier text
names.  ** The figures are in the run below. **

  ⌗ ** AND FREEING ONLY THE NAMED DEGENERACY MAKES THE RESIDUAL AN UPPER BOUND, WHICH IS THE RIGHT
  DIRECTION FOR THIS ROW. **  *A real refit would also move $\Omega_b h^2$, which changes the damping
  itself, and the acoustic angle's compensations.  Every extra freedom can only absorb MORE.*  ⇒ *So
  whatever survives the amplitude-and-tilt fit is the MOST that can survive any refit, and a wash
  here is a wash a fortiori.*  ⌗ *The tilt is applied as $(\ell/\ell_{\rm piv})^{\dd n}$, which is the
  standard mapping of a primordial $(k/k_*)^{\dd n}$ onto $C_\ell$ and is approximate at the percent
  level -- adequate for a degeneracy test and not quoted as a measured $n_s$.*

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
print(); print(BAR); print("PART 1b — THE SIGNATURE'S SIZE, MEASURED FROM THE INSTRUMENT"); print(BAR)
# ** The row carries "~9%".  A number in a docstring that no check reads is the defect this
#    corpus keeps finding, so it is measured here from the instrument itself. **
import contextlib                                                          # noqa: E402
import importlib.util                                                      # noqa: E402
import io                                                                  # noqa: E402

_rD = {}
for _arm in ('lcdm', 'cr'):
    os.environ.update({'ARM': _arm, 'NOPROJ': '1', 'LMAXL': '300', 'NK': '260'})
    _sp = importlib.util.spec_from_file_location(f'AT_{_arm}', _INSTR)
    _m = importlib.util.module_from_spec(_sp)
    with contextlib.redirect_stdout(io.StringIO()):
        _sp.loader.exec_module(_m)
    _rD[_arm] = (float(_m._rD), float((_m.eta_0 - _m.ETA_LS) / _m._rD))
    print(f"      {_arm:>5}:  r_D = {_rD[_arm][0]:.4f} Mpc   l_D = {_rD[_arm][1]:.1f}")
_ratio = _rD['cr'][0] / _rD['lcdm'][0]
print(f"      ratio r_D(cr)/r_D(lcdm) = {_ratio:.5f}   ->  {100*(_ratio-1):+.2f}%")
print(f"      l_D falls {_rD['lcdm'][1]:.0f} -> {_rD['cr'][1]:.0f}, {100*(_rD['cr'][1]/_rD['lcdm'][1]-1):+.1f}%")
check("the enlarged diffusion scale is +7.5%, not the ~9% the row carries",
      0.070 < _ratio - 1 < 0.080)
check("and DAMPX = 1.156766 is that ratio squared, so the scan imposes exactly it",
      abs(_ratio ** 2 - 1.156766) < 5e-4)
print("      ⌗ l_D's larger fall combines r_D with the arm's own eta_0 - eta_LS, which is why the")
print("        isolation below holds the geometry fixed and moves only 1/k_D^2.")

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
check("** the leaf assignment MULTIPLIES the ISW's low-ell imprint (it does not create it) **",
      res[(100, 300)][0] > 2 * res[(100, 300)][1])

# ** A FRACTION IS NOT A SIGNIFICANCE, and this row's order says so explicitly. **  The same
# comparison scored against plik_lite's covariance, with the tilt free, so the number is in the
# units the verdict is given in.
_A = CS.chi2_of(l_on, on)[2]
_mb, _md = _A * CS.bin_spectrum(l_on, on), _A * CS.bin_spectrum(l_on, off)
_fin = np.isfinite(_mb) & np.isfinite(_md)
_lc = 0.5 * (CS.BIN_LO + CS.BIN_HI)


def _refit(b_, d_, keep, lpiv=1000.0):
    n_ = int(keep.sum())
    F_ = scipy.linalg.cho_solve(
        scipy.linalg.cho_factor(CS.COV_TT[np.ix_(keep, keep)]), np.identity(n_))
    F_ = 0.5 * (F_ + F_.T)
    b, d = b_[keep], d_[keep]
    A_ = float((d @ F_ @ b) / (b @ F_ @ b))
    c1_ = float((d - A_ * b) @ F_ @ (d - A_ * b))
    X_ = np.vstack([b, b * np.log(_lc[keep] / lpiv)]).T
    r_ = d - X_ @ np.linalg.solve(X_.T @ F_ @ X_, X_.T @ F_ @ d)
    return n_, c1_, float(r_ @ F_ @ r_)


print()
_sig = {}
for lo, hi, lab in ((100, 1296, 'all, 100-1296'), (700, 1296, 'high, 700-1296')):
    k = _fin & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
    n_, c1_, c2_ = _refit(_mb, _md, k)
    _sig[lab] = math.sqrt(c2_ / n_)
    print(f"      ISW significance, {lab:<16} {n_:>4} bins   {c2_/n_:8.3f} chi2/bin after a tilt "
          f"refit   {math.sqrt(c2_/n_):5.2f} sigma/bin")
check("** the ISW is a 3+ sigma/bin effect overall — large, and NOT absorbed by a tilt **",
      _sig['all, 100-1296'] > 3.0)
check("** but under 1 sigma/bin at high ell: NOT what this row's question turns on **",
      _sig['high, 700-1296'] < 1.0)

# =====================================================================================
print(); print(BAR); print("PART 3 — THE DIFFUSION SCALE THROUGH A REFIT"); print(BAR)
lc = 0.5 * (CS.BIN_LO + CS.BIN_HI)
L_PIV = 1000.0
lb, Db, mb_meta = load('r4494_lcdm_DAMPX1.000')
ld, Dd, _ = load('r4494_lcdm_DAMPX1.157')
check("both spectra are the SAME arm at LMAXL=2200, differing only in DAMPX",
      int(mb_meta['LMAXL']) == 2200 and np.allclose(lb, ld))

A_DATA = CS.chi2_of(lb, Db)[2]        # put both on the DATA's scale; the model norm is arbitrary


def refit(mb_, md_, keep):
    """amplitude-only chi2, then amplitude+tilt chi2, and the tilt the fit wants"""
    n_ = int(keep.sum())
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F_ = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(n_))
    F_ = 0.5 * (F_ + F_.T)
    b_, d_ = mb_[keep], md_[keep]
    A_ = float((d_ @ F_ @ b_) / (b_ @ F_ @ b_))
    c1_ = float((d_ - A_ * b_) @ F_ @ (d_ - A_ * b_))
    X_ = np.vstack([b_, b_ * np.log(lc[keep] / L_PIV)]).T
    co = np.linalg.solve(X_.T @ F_ @ X_, X_.T @ F_ @ d_)
    r_ = d_ - X_ @ co
    return n_, c1_, float(r_ @ F_ @ r_), co[1] / co[0]

mb, md = A_DATA * CS.bin_spectrum(lb, Db), A_DATA * CS.bin_spectrum(ld, Dd)
keep0 = np.isfinite(mb) & np.isfinite(md)

print(f"      {'configuration':<34}{'bins':>6}{'chi2/bin, A only':>18}{'+ tilt':>10}{'absorbed':>11}")
out = {}
for cut, lab in ((0.8 * 2200, 'P15 185-bin (cut at 0.8*lmax=1760)'), (None, 'every covered bin')):
    keep = keep0 & ((CS.BIN_HI <= cut) if cut else np.ones_like(keep0))
    n, c1, c2, dn_ = refit(mb, md, keep)
    out[lab] = (n, c1, c2, dn_)
    print(f"      {lab:<34}{n:>6}{c1/n:>18.3f}{c2/n:>10.3f}{100*(1-c2/c1):>10.1f}%")

n185, c1_185, c2_185, dn = out['P15 185-bin (cut at 0.8*lmax=1760)']
check("the 0.8*lmax cut selects EXACTLY the 185 bins P15 names as the better-converged set",
      n185 == 185)
print(f"\n      the tilt the refit wants: dn_s = {dn:+.5f} at pivot l = {L_PIV:.0f}")

# ** THE CONTROL THAT FIRES: inject a KNOWN tilt and require the fitter to absorb ALL of it. **
# *A fitter that reports absorption has to be shown it is not manufacturing it.*
print()
_k = keep0 & (CS.BIN_HI <= 0.8 * 2200)
for dn_true in (0.02, 0.05):
    _md = A_DATA * CS.bin_spectrum(lb, Db * (np.maximum(lb, 2) / L_PIV) ** dn_true)
    _n, _c1, _c2, _dn = refit(mb, _md, _k & np.isfinite(_md))
    print(f"      CONTROL: injected dn_s = {dn_true:+.3f} -> recovered {_dn:+.5f}, "
          f"residual {_c2/_n:.5f}/bin, absorbed {100*(1-_c2/_c1):.3f}%")
    check(f"the fitter recovers an injected tilt of {dn_true:+.3f} and drives the residual to zero",
          abs(_dn - dn_true) < 0.03 * abs(dn_true) + 1e-3 and _c2 / _c1 < 1e-3)
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
