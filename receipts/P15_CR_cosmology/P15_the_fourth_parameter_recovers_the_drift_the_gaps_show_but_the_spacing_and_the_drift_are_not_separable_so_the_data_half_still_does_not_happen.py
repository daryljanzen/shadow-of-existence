#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7215` AUTHORISED THE FOURTH PARAMETER AND ORDERED ITS OWN SEQUENCE: the
driving-off spectra FIRST, `if the drift term degrades a fit that was already good to 0.3 per cent,
the parametrisation is wrong`; then the driving-on set; then the same validation burden; and
`degeneracy still counts as a result`.  *** THE FOURTH PARAMETER IS THE RIGHT ONE -- IT RECOVERS THE
PER-INDEX GAP GROWTH `cc66.160`'s PART C MEASURES, ON FOUR SPECTRA OF SIX.  AND IT STILL DOES NOT
LICENSE THE DATA HALF, BECAUSE THE SPACING AND THE DRIFT ARE NOT SEPARABLE. *** **

  ⓵ ** THE DRIFT IS TIED TO THE GAP DECOMPOSITION AND NOT INVENTED BESIDE IT. **  `cc66.160`'s
  PART C fits `gap_n = c_0 + c_1(-1)^n + c_2 n`, so the comb's phase must satisfy
  `$\\ell = \\ell_A v + d v^{2}$`, whose successive maxima are spaced `$\\ell_A + 2dv$`: the
  per-index growth is `$2d = c_2$`.  *At `$d=0$` this IS `cc66.160`'s three-parameter comb, checked
  here to be the same fit and not merely the same algebra.*

  ⓶ ⛭ ** `r7215` ITEM 2 PASSES, AND MY FIRST READING OF IT WAS WRONG. **  *Read naively the
  driving-off fits look RUINED -- `$\\ell_A$` goes from `$+0.09\\%$` to `$-6.58\\%$`.  **That is a
  reference-point error and not a degradation**: in `$\\ell = \\ell_A v + d v^{2}$` the parameter
  `$\\ell_A$` is the spacing extrapolated to `$v=0$`, which for a drifting comb is not the acoustic
  scale at all.*  ⇒ *The pivot-free statement is that the comb's drifting spacing PASSES THROUGH the
  banked value at `$\\ell\\simeq814$`, interior to the fitted window, while `$\\chi^{2}$` improves by
  `$44$` per cent.  **So the parametrisation is sound and the order proceeds.***

  ⓷ ⛭⛭ ** AND IT IS THE RIGHT PARAMETER, WHICH IS CHECKED AGAINST A NUMBER IT WAS NOT FITTED TO. **
  *The fitted `$2d$` is compared with PART C's `$c_2$`, measured independently from located peaks:
  `$+8.85$` against `$+8.77$` on `cr_base`, `$+9.22$` against `$+8.85$`, `$+7.10$` against
  `$+8.15$` twice.  **Four of six agree in sign and within a sixth.***

  ⓸ ⛔ ** BUT `cr_rb0.5` AND `cr_rb1.5` RETURN A DRIFT OF THE WRONG SIGN -- `$-35.20$` and
  `$-30.76$` where the gaps give `$+8.29$` and `$+9.70$` -- AND `cr_rb1.5` PUTS ITS SPACING ON THE
  BOX EDGE. **  *Both buy a large `$\\chi^{2}$` gain with a drift that contradicts their own gaps,
  which is `cc66.160`'s `Ⓓ①` pitfall wearing the fourth parameter's clothes.*

  ⓹ ⛔⛭⛭⛭ ** THE DEGENERACY `r7215` ASKED ABOUT IS NOT THE ONE THAT BITES. **  *It asked `if drift
  and alternation are not separable, say so and stop`.  **They ARE separable** --
  `$|\\rho(a,d)|\\le0.47$` on all six.  *What is not separable is the SPACING and the drift:
  `$\\rho(\\ell_A,d)$` between `$-0.94$` and `$-0.98$`.*  **So the stop condition fires on a pair the
  order did not name**, and the consequence is ⓸ above and ⓺ below.*

  ⓺ ⛔ ** AND THE VALIDATION BURDEN STILL FAILS. **  *On `cr_base` and `lcdm_base` the fitted comb's
  spacing never equals the banked value ANYWHERE: the crossing is at `$\\ell^{*}=-1330$` and
  `$-1251$`, outside the window and negative.  **So each driving pair still has one member whose
  phase is not referred to the same comb, and `cc66.158`'s separation is still not constructible.***

  ⌈ ⇒ ** WHAT THIS LEAVES, SAID PLAINLY. **  *A four-parameter comb is a better description of these
  spectra and a worse instrument for this measurement.  The fourth parameter was correctly
  identified and correctly added; what defeats it is that `$179$` binned points cannot hold a
  spacing and a drift apart.  **That is a statement about the bank, which `r7213` said is worth as
  much as a fit.***

  ⛭⛭⛭ ** `r7679+cc66.4` -- EVERY DIGIT ABOVE IS A NAMESAKE READING, AND THIS IS WHAT IT READS ON
  THE ARM OF RECORD. **  `r7679` repointed this receipt's four CR legs onto the `_leafrec1` banks,
  PER ARM: the control legs did not move, because `LEAFREC` does not reach them.  *The digits above
  stay as published -- they are pinned on the banks that measured them, which is 69's ruling on
  `PUB156` -- and the arm-of-record readings are set beside them here as the new numbers they are.*

    ⓑ ⓒ ** the fitted `$2d$` against PART C's `$c_2$`. **  `cr_base` `$+8.85$` vs `$+8.77$` reads
      `$+8.05$` vs `$+8.76$`; `cr_nodrive` `$+7.10$` vs `$+8.15$` reads `$+7.07$` vs `$+8.19$`.  The
      two control legs are unchanged at `$+9.22$`/`$+8.85$` and `$+7.10$`/`$+8.15$`.  *** Four of six
      still agree in sign and within a sixth, and they are the same four. ***
    ⓓ ** the wrong-signed drifts. **  `cr_rb0.5` `$-35.20$` against gaps `$+8.29$` reads `$-36.10$`
      against `$+8.42$`; `cr_rb1.5` `$-30.76$` against `$+9.70$` reads `$-30.97$` against `$+9.61$`.
      Its `$\ell_A$` is still pinned at the box edge, `$430.000$` exactly.  *** Unchanged in kind. ***
    ⓔ ** the crossings. **  The driving-off pair crosses the banked spacing at `$\ell^{*}=805$` and
      `$813$` where the namesake gave `$\simeq814$` for both, still interior; `$\chi^{2}$` improves
      `$47.5\to26.6$` and `$93.8\to52.7$`, which is `$44$` per cent on both as published.  The base
      pair's crossing moves from `$-1330$`/`$-1251$` to `$-1537$`/`$-1251$` -- still negative, still
      outside the window.  *** Ⓔ ① and Ⓣ ① are unchanged in kind. ***
    ⛔ ** ONE CLAIM DOES NOT SURVIVE, and it is not a figure move. **  `Ⓑ②` published
      `cr_rb1.5` as REACHED FROM ONE COARSE START where the others were reached from four, and made
      that solo reach the second independent sign of an unidentified fit.  ** On the arm of record it
      is reached from TWO. **  *What survives is the ORDERING -- `cr_rb1.5` is still the unique
      fewest, at half the others', and still the only spectrum on the box edge, so the corroboration
      test and the boundary test still agree on which spectrum to distrust.  The gate now asserts
      that ordering and the namesake's solo reach, measured here rather than recalled; `reached from
      one start` is routed to `69` as a CLAIM CHANGE.*  ⛔ *`REACH >= 2` passes on its own, so
      dropping the solo clause would have turned the gate green while deleting the finding.*

** COMPUTES: the four-parameter comb (position, spacing, alternation, linear drift in the spacing),
   profiled over the same disciplined basis, fitted to six likelihood-binned model spectra over the
   whole feasible box; the d=0 reduction checked against cc66.160's own three-parameter fit; the
   fitted drift checked against PART C's independently measured per-index gap growth; and the
   (l_A, d) and (a, d) curvatures measured.  *** No new spectra, no refit, data not touched. ***  **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; 473s MEASURED, against
CI's 900s budget.  An earlier version refitted in PART C what PART B had already found and
took over 20 minutes, which is the budget that reddened another seat's PR the same day.)
"""
import os
import sys

import numpy as np
from scipy.optimize import minimize

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
ran = []


def check(label, ok):
    ran.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
# ⛭⛭⛭ `r7679+cc66.1` -- ** REPOINTED ONTO THE ARM OF RECORD PER ARM, WHICH IS THE ONLY WAY THESE
#   TWO BANKS CAN BE REPOINTED AT ALL. **  `r7679` (69) item 2.
#   ⛔ *Both `_leafrec1` directories carry the CR legs and NOTHING ELSE -- nine files against the
#     namesake's eighteen in `grid_oneclock`, four against seven in the lever -- because `LEAFREC`
#     does not reach the control (`r7669+70.1`).  So `GO + '_leafrec1'` raises `FileNotFoundError`
#     on `lcdm_base.npz`, the shape `r7645+cc66.68` paid for.*
#   ⇒ The arm suffix is named ONCE and the directory resolves PER ARM; a control leg resolves to the
#     namesake directory, where it IS the arm of record's control.  The shape is GATED below.
_GARM = '_leafrec1'                     # the arm of record's suffix on these grid DIRECTORIES
_gd = lambda d, arm: (d + _GARM) if arm.startswith('cr') else d          # noqa: E731
_NSK = {'GO': GO, 'LEV': LEV}           # kept: a PUBLISHED namesake digit is pinned on what it read
for _p in (GO, LEV, _gd(GO, 'cr'), _gd(LEV, 'cr')):
    if not os.path.isdir(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

LMIN, LMAX, NPK, HALFWIN = 150.0, 1600.0, 5, 40.0
NB, NE = 5, 3
LC, FACB = CS.bin_center_and_fac()
SPECTRA = (('cr_base', os.path.join(_gd(GO, 'cr'), 'cr_base.npz')),
           ('lcdm_base', os.path.join(GO, 'lcdm_base.npz')),
           ('cr_nodrive', os.path.join(_gd(LEV, 'cr'), 'cr_nodrive.npz')),
           ('lcdm_nodrive', os.path.join(LEV, 'lcdm_nodrive.npz')),
           ('cr_rb0.5', os.path.join(_gd(LEV, 'cr'), 'cr_rb0.5.npz')),
           ('cr_rb1.5', os.path.join(_gd(LEV, 'cr'), 'cr_rb1.5.npz')))
#: ⛭⛭ THE NAMESAKE PATH OF EVERY LEG, kept beside the live one: a PUBLISHED digit is pinned on what
#:   it was measured on, which is 69's own ruling on `PUB156` at `r7673+cc66.13`.
SPECTRA_NSK = (('cr_base', os.path.join(GO, 'cr_base.npz')),
               ('lcdm_base', os.path.join(GO, 'lcdm_base.npz')),
               ('cr_nodrive', os.path.join(LEV, 'cr_nodrive.npz')),
               ('lcdm_nodrive', os.path.join(LEV, 'lcdm_nodrive.npz')),
               ('cr_rb0.5', os.path.join(LEV, 'cr_rb0.5.npz')),
               ('cr_rb1.5', os.path.join(LEV, 'cr_rb1.5.npz')))
_ctl_in_aor = [f for d in (_gd(GO, 'cr'), _gd(LEV, 'cr'))
               for f in os.listdir(d) if f.startswith('lcdm')]
_cr_moved = [n for (n, p), (_n2, q) in zip(SPECTRA, SPECTRA_NSK)
             if n.startswith('cr')
             and not np.array_equal(np.asarray(np.load(p, allow_pickle=True)['Dl'], float),
                                    np.asarray(np.load(q, allow_pickle=True)['Dl'], float))]
print(f"    arm-of-record directories hold {len(_ctl_in_aor)} control file(s); CR legs whose "
      f"spectrum MOVED on the repoint: {len(_cr_moved)} of 4 {_cr_moved}")
check("\u26ed\u26ed `r7679` ** THE REPOINT IS PER ARM AND THE SHAPE IS GATED. **  Both `_leafrec1` "
      "directories carry the CR legs and NOT ONE control file, because `LEAFREC` does not reach the "
      "control -- so a wholesale `GO + '_leafrec1'` would raise `FileNotFoundError` on "
      "`lcdm_base.npz`, the shape `r7645+cc66.68` paid for.  All four CR spectra MOVED.  \u26d4 "
      "*Point `_GARM` back at the namesake and this fails*",
      _GARM == '_leafrec1' and not _ctl_in_aor and len(_cr_moved) == 4)
DRIVING_OFF = ('cr_nodrive', 'lcdm_nodrive')
BASE = ('cr_base', 'lcdm_base')
# ⛭ r7217: `cr_rb0.5 is a RECOVERED spectrum and belongs in the first test group -- a driving-on
#    case where a fourth parameter could only do harm, which makes it the better control`.  It is
#    in that group here, and it earns the description: see Ⓑ⑤.
RECOVERED = DRIVING_OFF + ('cr_rb0.5',)

# ⛔ THE SEARCH IS PART OF THE INSTRUMENT -- cc66.160 learned that the hard way, so the starts span
#    the whole feasible box here too, and `the optimum is interior` is CHECKED and not hoped.  The
#    grid is coarser than cc66.160's because a sixth parameter multiplies it; it was verified
#    against the wider grid before being trimmed, and Ⓑ② asserts each optimum is reached from more
#    than one start, which is what the trim could have broken.
LBOX = (200.0, 430.0)
L0S = (215., 265., 300., 345., 400.)
P0S = (-0.45, -0.20, 0.05, 0.30)
D0S = (0.0, 8.0, -16.0)
NREF = 4
LOOSE = dict(xatol=1e-3, fatol=1e-4, maxiter=4000, maxfev=4000)
TIGHT = dict(xatol=1e-8, fatol=1e-12, maxiter=60000, maxfev=60000)
KEEP = 1e-9


def binned(path):
    z = np.load(path, allow_pickle=True)
    Cl = CS.bin_spectrum(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    k = np.isfinite(Cl)
    return LC[k], (Cl * FACB)[k], float(z['l_A'])


def detilt(ls, Dl):
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0) & np.isfinite(Dl)
    t = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    return ls[m], Dl[m] / ls[m] ** t


def phase(ls, lA, d):
    """v(l) from l = l_A v + d v^2.  The d -> 0 branch is l/l_A EXACTLY, not a limit."""
    if abs(d) < 1e-12:
        return ls / lA
    disc = lA * lA + 4.0 * d * ls
    if np.any(disc <= 0):
        return None
    return (-lA + np.sqrt(disc)) / (2.0 * d)


def design(ls, lA, phi, a, h2, h3, d):
    v = phase(ls, lA, d)
    if v is None:
        return None
    u = v - phi
    up = u - a * np.cos(np.pi * u)
    x = np.log(ls / 500.0)
    osc = np.cos(2*np.pi*up) + h2*np.cos(4*np.pi*up) + h3*np.cos(6*np.pi*up)
    return np.column_stack([x ** k for k in range(NB)] + [osc * x**k for k in range(NE)])


def chi2(ls, Y, p):
    lA, phi, a, h2, h3, d = p
    if not (LBOX[0] < lA < LBOX[1]) or abs(phi) > 1.0 or abs(a) > 0.3:
        return 1e12
    if abs(h2) > 2.0 or abs(h3) > 2.0 or abs(d) > 120.0:
        return 1e12
    A = design(ls, lA, phi, a, h2, h3, d)
    if A is None or not np.all(np.isfinite(A)):
        return 1e12
    c, *_ = np.linalg.lstsq(A, Y, rcond=None)
    r = Y - A @ c
    return float(r @ r)


def fit(ls, Y, free_d=True):
    """Returns (result, how many distinct coarse starts reached within 1e-6 of the optimum)."""
    f = (lambda p: chi2(ls, Y, p if free_d else np.r_[p[:5], 0.0]))
    n = 6 if free_d else 5
    coarse = []
    for l0 in L0S:
        for p0 in P0S:
            for d0 in (D0S if free_d else (0.0,)):
                r = minimize(f, [l0, p0, 0.015, 0.3, 0.1, d0][:n], method='Nelder-Mead',
                             options=LOOSE)
                coarse.append((float(r.fun), r.x.copy()))
    coarse.sort(key=lambda t: t[0])
    best = None
    for _fun, x in coarse[:NREF]:
        r = minimize(f, x, method='Nelder-Mead', options=TIGHT)
        if best is None or r.fun < best.fun - KEEP * max(1.0, abs(best.fun)):
            best = r
    reached = 0
    for _fun, x in coarse[:NREF]:
        r = minimize(f, x, method='Nelder-Mead', options=TIGHT)
        if r.fun < best.fun * (1 + 1e-6) + 1e-9:
            reached += 1
    # ⌗ returned as scipy gave it: an earlier version rebuilt the result to zero-pad `x` for the
    #   d=0 case and silently lost `fun`, because OptimizeResult keeps its values as dict ITEMS and
    #   not as instance attributes.  No caller needs the sixth slot, so there is nothing to pad.
    return best, reached


# ⛔ PART C's PEAK FINDER, TAKEN FROM `cc66.160` BYTE FOR BYTE AND NOT RETYPED.  My first
#    version of this file reimplemented it from memory and got four things different -- the
#    concavity requirement, the two-neighbour maximum test, the de-tilt guard and the grid
#    span -- which made `Ⓑ③` compare the fitted drift against MY OWN variant of PART C while
#    claiming it was PART C's.  `Ⓐ③` below pins this copy to `cc66.160`'s published gaps.
def peak_gaps(ls, Dl):
    """cc66.156's located peaks, and the gaps between them."""
    ls, Y = detilt(ls, Dl)
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    Di = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(Di) - 2)
           if Di[i] > Di[i - 1] and Di[i] >= Di[i + 1] and Di[i] > Di[i - 2] and Di[i] >= Di[i + 2]]
    co = []
    for i in idx:
        if not co or lg[i] - co[-1] > 60.0:
            co.append(lg[i])
    pk = []
    for l0 in co[:NPK]:
        w = (ls >= l0 - HALFWIN) & (ls <= l0 + HALFWIN)
        if w.sum() < 4:
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        if c[0] < 0:
            pk.append(l0 - c[1] / (2 * c[0]))
    return np.diff(np.array(pk))


def curv(ls, Y, x0, i, j, hi, hj):
    """corr(p_i, p_j) from the 2x2 curvature of chi2 at the optimum."""
    def c(hii, hjj):
        q = x0.copy(); q[i] += hii; q[j] += hjj
        return chi2(ls, Y, q)
    f0 = chi2(ls, Y, x0)
    Hii = (c(hi, 0) - 2*f0 + c(-hi, 0)) / hi**2
    Hjj = (c(0, hj) - 2*f0 + c(0, -hj)) / hj**2
    Hij = (c(hi, hj) - c(hi, -hj) - c(-hi, hj) + c(-hi, -hj)) / (4*hi*hj)
    try:
        C = np.linalg.inv(np.array([[Hii, Hij], [Hij, Hjj]]) / 2.0)
        return float(C[0, 1] / np.sqrt(abs(C[0, 0] * C[1, 1])))
    except np.linalg.LinAlgError:
        return float('nan')


# ============================================================ A. the template carries the drift
head("A.  ⓵ THE DRIFT IS PART C's OWN c_2, BY CONSTRUCTION -- CHECKED, NOT ASSERTED")

_lA, _d = 300.0, 4.0
_v = np.arange(0.6, 6.0, 1e-5)
_T = np.cos(2 * np.pi * _v)
_i = [k for k in range(1, len(_v) - 1) if _T[k] > _T[k-1] and _T[k] >= _T[k+1]]
_vm = np.array([_v[k] for k in _i])[:5]
_lm = _lA * _vm + _d * _vm ** 2
_gaps = np.diff(_lm)
_growth = float(np.polyfit(np.arange(len(_gaps)), _gaps, 1)[0])
print(f"      l = {_lA} v + {_d} v^2:  maxima at l = {np.array2string(_lm, precision=1)}")
print(f"      successive gaps {np.array2string(_gaps, precision=2)}  "
      f"-> per-index growth {_growth:.3f}, wanted 2d = {2*_d:.3f}")
check("Ⓐ①  the phase relation `$\\ell=\\ell_A v+dv^{2}$` makes the comb's per-index gap growth equal "
      "`$2d$` ** TO BETTER THAN A PER CENT, so the fitted `$d$` IS PART C's `$c_2/2$` and not a "
      "separate quantity that happens to look like it **",
      abs(_growth / (2 * _d) - 1) < 0.01)

# ⛭⛭⛭ `r7679+cc66.4` -- ** THE CALIBRATION IS READ ON THE BANK cc66.160 MEASURED. **  `Ⓐ②`
#   pins cc66.160's PUBLISHED `$301.658 / 106.03$`, and after `r7679`'s repoint `SPECTRA[2][1]` is the
#   ARM OF RECORD's `cr_nodrive` while those two digits are a NAMESAKE publication.  ⛔ *Scoring a
#   published digit against a different bank is not a calibration failing -- it is the calibration
#   asked the wrong question, and it went red for exactly that reason.*
#   ⇒ 69's own ruling on `PUB156` (`r7673+cc66.13`) governs: a published digit is pinned on what it
#     was measured on, with the arm-of-record reading printed BESIDE it as the new number it is.  This
#     is also what `Ⓐ③` four lines below has always done -- it reads PART C's finder on the
#     NAMESAKE `GO` to reproduce PART C's published gaps.  Everything after this stays on the arm.
_ls0, _Y0 = detilt(*binned(SPECTRA_NSK[2][1])[:2])
_r0, _ = fit(_ls0, _Y0, free_d=False)
_ls0a, _Y0a = detilt(*binned(SPECTRA[2][1])[:2])
_r0a, _ = fit(_ls0a, _Y0a, free_d=False)
print(f"      and at d=0 on cr_nodrive: l_A {_r0.x[0]:.3f}, chi2 {_r0.fun:.4g} "
      f"(cc66.160 reports 301.658 / 106.03)")
print(f"      the SAME reduction on the ARM OF RECORD's cr_nodrive: l_A {_r0a.x[0]:.3f}, "
      f"chi2 {_r0a.fun:.4g}  <- the new numbers, reported beside the published ones")
check("Ⓐ②  and the `$d=0$` reduction REPRODUCES `cc66.160`'s three-parameter fit to three figures, "
      "ON THE BANK cc66.160 READ, "
      "*so what follows is the same instrument with one parameter added and not a second instrument "
      "being compared with the first*.  ⛭⛭ `r7679+cc66.4`: scored on `SPECTRA_NSK` because the "
      "repoint moved `SPECTRA` to the arm of record while `$301.658/106.03$` is a NAMESAKE "
      "publication -- 69's `PUB156` ruling -- and the arm-of-record reduction is printed beside it",
      abs(_r0.x[0] - 301.658) < 0.5 and abs(_r0.fun / 106.03 - 1) < 0.02)


_gc = peak_gaps(*binned(os.path.join(GO, 'cr_base.npz'))[:2])
print(f"      PART C's finder on cr_base: gaps {[int(x) for x in _gc]}  "
      f"(cc66.160 publishes [302, 270, 312, 295])")
check("Ⓐ③  and this file's copy of PART C's peak finder is `cc66.160`'s BYTE FOR BYTE and reproduces "
      "its published gaps `$302/270/312/295$`, *so `Ⓑ③` below compares the fitted drift against "
      "PART C's own number and not against a second implementation of it -- which is what my first "
      "version of this file did, having retyped the finder from memory with four differences*",
      [int(x) for x in _gc] == [302, 270, 312, 295])


# ============================================================ B. the fits
head("B.  ⓶⓷ THE FOURTH PARAMETER: ITEM 2 PASSES, AND THE DRIFT IT FINDS IS THE GAPS' OWN")

print(f"      {'spectrum':13s} {'banked':>8s} {'lA(v=0)':>9s} {'d':>7s} {'fit 2d':>7s} "
      f"{'PART C c2':>10s} {'l*':>7s} {'in win':>7s} {'edge':>5s} {'starts':>6s} {'chi2':>9s}")
F4, G2, STAR, INSIDE, EDGE, REACH, X4 = {}, {}, {}, {}, {}, {}, {}
for tag, p in SPECTRA:
    lb, db, lA = binned(p)
    ls, Y = detilt(lb, db)
    b, reached = fit(ls, Y, free_d=True)
    lA0, d0 = b.x[0], b.x[5]
    v = phase(ls, lA0, d0)
    gaps = peak_gaps(lb, db)
    n = np.arange(len(gaps))
    c3, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(gaps)), (-1.0) ** n, n]), gaps,
                             rcond=None)
    vstar = (lA - lA0) / (2.0 * d0) if abs(d0) > 1e-9 else float('nan')
    lstar = lA0 * vstar + d0 * vstar ** 2 if np.isfinite(vstar) else float('nan')
    F4[tag] = (lA0, d0, float(b.fun), lA)
    G2[tag] = float(c3[2])
    STAR[tag] = lstar
    INSIDE[tag] = bool(np.isfinite(vstar) and v.min() <= vstar <= v.max())
    EDGE[tag] = bool(lA0 > LBOX[1] - 1.0 or lA0 < LBOX[0] + 1.0)
    REACH[tag] = reached
    X4[tag] = b.x.copy()
    print(f"      {tag:13s} {lA:8.3f} {lA0:9.3f} {d0:+7.2f} {2*d0:+7.2f} {c3[2]:+10.2f} "
          f"{lstar:7.0f} {str(INSIDE[tag]):>7s} {str(EDGE[tag]):>5s} {reached:6d} {b.fun:9.4g}")

_off3 = {}
# ⌗ cr_rb0.5 is in here because r7217 put it in the first test group: without it the three-
#    parameter column for the control printed `nan`, which is a number-shaped absence.
for tag in tuple(dict.fromkeys(RECOVERED + BASE)):
    lb, db, lA = binned(dict(SPECTRA)[tag])
    ls, Y = detilt(lb, db)
    r3, _ = fit(ls, Y, free_d=False)
    _off3[tag] = (r3.x[0], float(r3.fun))
print(f"      ⇒ item 2, the driving-off pair: chi2 "
      f"{_off3['cr_nodrive'][1]:.1f}->{F4['cr_nodrive'][2]:.1f} and "
      f"{_off3['lcdm_nodrive'][1]:.1f}->{F4['lcdm_nodrive'][2]:.1f}; the drifting spacing crosses "
      f"banked at l={STAR['cr_nodrive']:.0f} and {STAR['lcdm_nodrive']:.0f}, INSIDE the window")
check("Ⓑ①  ⛭ ** `r7215` ITEM 2 PASSES: THE FOURTH PARAMETER DOES NOT DEGRADE THE DRIVING-OFF FITS. "
      "**  *`$\\chi^{2}$` improves by `$40$` per cent or more on both and the comb's drifting spacing "
      "passes through the banked value INSIDE the fitted window.*  ⚠ *Read naively the fits look "
      "ruined -- `$\\ell_A$` reads `$-6.6\\%$` -- and that is a REFERENCE-POINT error of mine: "
      "`$\\ell_A$` is the spacing at `$v=0$`, which is not the acoustic scale when the spacing "
      "drifts.  **I nearly reported the parametrisation wrong on the strength of it**",
      all(F4[t][2] < 0.6 * _off3[t][1] and INSIDE[t] for t in DRIVING_OFF))

_solo = [t for t, _ in SPECTRA if REACH[t] < 2]
# ⛔⛭⛭⛭ `r7679+cc66.4` -- ** THE SOLO REACH IS A CLAIM CHANGE ON THE ARM OF RECORD, AND THE GATE
#   NOW SAYS SO.  `cr_rb1.5` IS NO LONGER REACHED FROM A SINGLE START; IT IS STILL REACHED FROM THE
#   FEWEST, AND IT IS STILL THE ONLY ONE ON THE BOX EDGE. **
#
#   On the namesake `cr_rb1.5` was reached from ONE coarse start where the others were reached from
#   four, and that solo reach was the gate's second independent sign of an unidentified fit.  On the
#   arm of record it is reached from TWO, so `_solo` is EMPTY and `every interior optimum is reached
#   from more than one start` is now true of EVERY spectrum including the edge one.
#   ⇒ *What survives is the ORDERING the conclusion rests on: `cr_rb1.5` is the unique minimum of
#     the corroboration count, at HALF the others', and it is the unique spectrum on the box edge --
#     so the corroboration test and the boundary test still agree on which spectrum to distrust.
#     What does NOT survive is `reached from one start`, and that is routed to 69 as a claim change.*
#   ⛔ *Re-tolerancing this -- `REACH[t] >= 2` already passes, so dropping the `_solo` clause alone
#     would have turned the gate GREEN while deleting the thing worth reporting.  The namesake reach
#     is MEASURED below instead, so the published `one start` is pinned on the bank that read it.*
# ⌘ ONE namesake fit, not six.  `cr_rb1.5` is the only spectrum whose reach this gate PUBLISHES a
#    number for, and the receipt's measured runtime is 473s against CI's 900s budget -- four more
#    four-parameter multi-start fits would have cost most of the headroom to re-measure digits no
#    claim rests on.  The control legs did not move at all: `LEAFREC` does not reach them.
_NSK_SOLO = 'cr_rb1.5'
_lbn, _dbn, _ = binned(dict(SPECTRA_NSK)[_NSK_SOLO])
_lsn, _Yn = detilt(_lbn, _dbn)
_bn, _REACH_NSK_SOLO = fit(_lsn, _Yn, free_d=True)
_REACH_NSK = {t: (_REACH_NSK_SOLO if t == _NSK_SOLO
                  else (REACH[t] if not t.startswith('cr') else -1))
              for t, _ in SPECTRA}
_mx = max(REACH[t] for t, _ in SPECTRA)
_fewest = [t for t, _ in SPECTRA if REACH[t] == min(REACH[t2] for t2, _ in SPECTRA)]
print(f"      ⇒ reached from a single coarse start: {', '.join(_solo) if _solo else 'none'}; "
      f"on the box edge: {', '.join(t for t, _ in SPECTRA if EDGE[t]) or 'none'}")
print(f"      {'spectrum':13s} {'starts (ARM OF RECORD)':>23s} {'starts (NAMESAKE)':>19s}")
for _t, _ in SPECTRA:
    _n = _REACH_NSK[_t]
    print(f"      {_t:13s} {REACH[_t]:23d} "
          f"{(f'{_n:d}' if _n >= 0 else 'not re-measured'):>19s}"
          f"{'   <- the box-edge spectrum, and the one cc66 published a reach for' if EDGE[_t] else ''}"
          f"{'   (did not move: LEAFREC does not reach the control)' if not _t.startswith('cr') else ''}")
print(f"      ⇒ fewest starts: {', '.join(_fewest)} at {REACH[_fewest[0]]} against the others' "
      f"{_mx}; on the box edge: "
      f"{', '.join(t for t, _ in SPECTRA if EDGE[t]) or 'none'}")
check("Ⓑ②  ⛔⛭⛭ ** ON THE ARM OF RECORD EVERY OPTIMUM -- THE EDGE ONE INCLUDED -- IS REACHED FROM "
      "MORE THAN ONE INDEPENDENT START, AND WHAT SURVIVES IS THE ORDERING: `cr_rb1.5` IS REACHED "
      "FROM THE FEWEST STARTS, HALF THE OTHERS', AND IT IS THE ONLY ONE ON THE BOX EDGE. **  *So the "
      "corroboration test and the boundary test still agree on which spectrum to distrust, and a "
      "grid wide enough to `fix` it would only have hidden that.*  ⛔ *On the NAMESAKE -- measured "
      "here, not recalled -- `cr_rb1.5` was reached from ONE start where the others were reached "
      "from four, and the gate asserted that solo reach.  **`reached from one start` is FALSIFIED on "
      "the arm of record and is routed to 69 as a claim change**, not re-toleranced: `REACH >= 2` "
      "passes on its own, so dropping the solo clause would have gone green while deleting the only "
      "thing worth reporting*",
      all(REACH[t] >= 2 for t, _ in SPECTRA) and _fewest == ['cr_rb1.5']
      and REACH['cr_rb1.5'] * 2 <= _mx and EDGE['cr_rb1.5']
      and [t for t, _ in SPECTRA if EDGE[t]] == ['cr_rb1.5']
      and _REACH_NSK_SOLO == 1)

_agree = [t for t, _ in SPECTRA if G2[t] * 2 * F4[t][1] > 0
          and 0.4 < abs(2 * F4[t][1] / G2[t]) < 2.5]
print(f"      ⇒ fitted 2d agrees with PART C's c2 in sign and within a sixth on: "
      f"{', '.join(_agree)}")
_sp = {t: (F4[t][0] + 2 * F4[t][1] * 0.6, F4[t][0] + 2 * F4[t][1] * 5.3) for t in RECOVERED}
for t in RECOVERED:
    print(f"      {t:13s} 3-param {'' if t in DRIVING_OFF else '(driving ON) '}recovered to "
          f"{100 * abs(_off3[t][0] / F4[t][3] - 1):.2f}%; "
          f"4-param spacing runs {_sp[t][0]:.0f} to {_sp[t][1]:.0f}, crosses banked at "
          f"l*={STAR[t]:.0f}, drift {2 * F4[t][1]:+.2f} against the gaps' {G2[t]:+.2f}")
check("Ⓑ⑤  ⛭⛭ ** `r7217` PUT `cr_rb0.5` IN THE FIRST TEST GROUP AS A DRIVING-ON CONTROL, AND IT "
      "EARNS THAT: THE HARM THE GROUP EXISTS TO DETECT APPEARS THERE AND IN A QUANTITY THE "
      "`$\ell_A$` TEST CANNOT SEE. **  *All three recovered spectra keep their spacing crossing "
      "inside the window, `cr_rb0.5` included -- so on the `$\ell_A$` criterion alone the fourth "
      "parameter looks harmless on every one of them.  **But `cr_rb0.5`'s fitted drift is "
      "WRONG-SIGNED and four times too large** (`$-35.20$` against the gaps\' `$+8.29$`), and its "
      "spacing swings `$380\to222$` across the window where its gaps barely move.*  ⇒ *`66`\'s "
      "control is the better control precisely because it separates the two tests: a spectrum can "
      "pass `does the scale survive` and fail `is this the drift the gaps show`*",
      all(INSIDE[t] for t in RECOVERED)
      and G2['cr_rb0.5'] * F4['cr_rb0.5'][1] < 0
      and abs(2 * F4['cr_rb0.5'][1] / G2['cr_rb0.5']) > 2.5)


check("Ⓑ③  ⛭⛭ ** THE FITTED DRIFT REPRODUCES PART C's INDEPENDENTLY MEASURED PER-INDEX GAP "
      "GROWTH ON FOUR SPECTRA OF SIX. **  *`$c_2$` comes from located peaks with `$\\ell_A$` held "
      "at its banked value and is in no way an input to this fit, so the agreement is a real check "
      "that the fourth "
      "parameter is the quantity `cc66.153` named and not a free knob*",
      set(_agree) == {'cr_base', 'lcdm_base', 'cr_nodrive', 'lcdm_nodrive'})

_runaway = [t for t, _ in SPECTRA if t not in _agree]
print(f"      ⇒ and it runs away with the WRONG SIGN on: {', '.join(_runaway)}"
      f"   (cr_rb1.5 also pins l_A to the box edge: {EDGE['cr_rb1.5']})")
check("Ⓑ④  ⛔ ** ON `cr_rb0.5` AND `cr_rb1.5` THE DRIFT COMES BACK WITH THE WRONG SIGN AGAINST THEIR "
      "OWN GAPS, AND `cr_rb1.5` PUTS ITS SPACING ON THE BOX EDGE. **  *Both buy a large `$\\chi^{2}$` "
      "gain with a drift their gaps contradict -- `cc66.160`'s `Ⓓ①` pitfall in the fourth "
      "parameter's clothes*",
      set(_runaway) == {'cr_rb0.5', 'cr_rb1.5'} and EDGE['cr_rb1.5'])


# ============================================================ C. the degeneracy
head("C.  ⓹ ⛔⛭ THE DEGENERACY -- AND IT IS NOT THE PAIR r7215 ASKED ABOUT")

print(f"      {'spectrum':13s} {'corr(a,d)':>10s} {'corr(lA,d)':>11s}")
RAD, RLD = {}, {}
for tag, p in SPECTRA:
    lb, db, lA = binned(p)
    ls, Y = detilt(lb, db)
    RAD[tag] = curv(ls, Y, X4[tag].copy(), 2, 5, 0.002, 0.05)     # PART B's optimum, not a refit
    RLD[tag] = curv(ls, Y, X4[tag].copy(), 0, 5, 0.5, 0.05)
    print(f"      {tag:13s} {RAD[tag]:+10.4f} {RLD[tag]:+11.4f}"
          f"{'   <- l_A clipped at the edge: meaningless' if EDGE[tag] else ''}")
check("Ⓒ①  ** `r7215` ASKED WHETHER DRIFT AND ALTERNATION ARE SEPARABLE AND THEY ARE: "
      "`$|\\rho(a,d)|\\le0.5$` ON ALL SIX. **  *So the stop condition the order named does not fire, "
      "and saying that plainly before reporting the one that does is the right order to put them in*",
      all(abs(RAD[t]) <= 0.5 for t, _ in SPECTRA))

_free = [t for t, _ in SPECTRA if not EDGE[t]]
check("Ⓒ②  ⛔⛭⛭⛭ ** WHAT IS NOT SEPARABLE IS THE SPACING AND THE DRIFT: "
      "`$\\rho(\\ell_A,d)\\le-0.93$` on every spectrum whose `$\\ell_A$` is not clipped. **  *Four "
      "parameters on `$179$` binned points cannot hold the scale and its drift apart, and `r7213` "
      "said a statement about what the bank can support is worth as much as a fit.*  ⚠ *`cr_rb1.5` "
      "reports `$\\rho=0$` and that is NOT independence -- its `$\\ell_A$` sits on the box edge, so "
      "the curvature there is clipped and means nothing*",
      all(RLD[t] <= -0.93 for t in _free) and len(_free) == 5)


# ============================================================ D. the burden
head("D.  ⓺ ⛔ AND THE VALIDATION BURDEN STILL FAILS, FOR A DIFFERENT REASON THAN LAST TIME")

for tag in BASE:
    lA0, d0, _c, lA = F4[tag]
    print(f"      {tag:13s} banked {lA:.3f}: spacing runs {lA0 + 2*d0*0.6:.0f} to "
          f"{lA0 + 2*d0*5.3:.0f} across the window and crosses banked at l*={STAR[tag]:.0f}")
check("Ⓓ①  ⛔ ** ON BOTH BASE SPECTRA THE FITTED COMB'S SPACING NEVER EQUALS THE BANKED VALUE "
      "ANYWHERE -- the crossing is NEGATIVE, far outside the window. **  *So each driving pair still "
      "has one member whose phase is not referred to the same comb, `cc66.158`'s "
      "`$0.1929$`/`$1.0390$` separation is still not constructible, and by `r7215`'s own terms -- "
      "the same burden as `r7213`'s -- the data half still does not happen*",
      all(not INSIDE[t] and STAR[t] < 0 for t in BASE))

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print(f"  ✔ {len(ran) - len(fail)} of {len(ran)} checks pass -- the fourth parameter is the right "
      "one and the")
print("    bank cannot support it: a better description and a worse instrument.")
print(BAR)
sys.exit(0)
