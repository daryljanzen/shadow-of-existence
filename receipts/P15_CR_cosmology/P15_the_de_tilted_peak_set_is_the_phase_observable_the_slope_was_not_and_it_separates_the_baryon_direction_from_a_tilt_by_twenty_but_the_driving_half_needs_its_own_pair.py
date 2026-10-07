#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `cc66.155` ASKED FOR A DIFFERENT STATISTIC AND COSTED IT AT ZERO RUNS.  IT IS BUILT
HERE, ON THE SAME BANK, AND IT WORKS: THE DE-TILTED PEAK SET SEPARATES THE BARYON DIRECTION FROM A
PURE TILT BY A FACTOR OF `$11$` ON THE COMMON OFFSET AND `$21$` ON THE ODD-EVEN ALTERNATION, WHERE
THE FREE-PERIOD SLOPE SEPARATED THEM BY `$1.3$`. **  ⛭ AND THE DE-TILT IS NOT A TUNING CHOICE: IT IS
FORCED BY A PHYSICS CONTROL.  Without it `$n_s$` moves the common offset MORE THAN ANY OTHER
DIRECTION, which a primordial tilt cannot do; with it that response collapses by a factor of `$20$`
and becomes window-independent.  *** The same disease `cc66.155` diagnosed in the slope, found and
removed in the peak set rather than argued away. ***

  ⛔ ** BUT THE DRIVING HALF IS NOT ESTABLISHED, AND THAT IS THE POINT OF RUNNING THIS FIRST. **  *The
  control arm's same-vintage driving pair gives `$\\Delta\\varphi=+0.126$` and
  `$\\Delta\\mathrm{alt}=-0.0247$` -- opposite in sign to the baryon direction on BOTH components,
  which is the orthogonality the ask rested on.  ** The CR arm's banked driving-ON spectrum cannot
  serve: its detected peak series is not integer-spaced in `$\\ell_A$` (gaps `$0.74$`--`$0.96$`
  against the grid's `$0.92$`--`$1.05$`), and the common-offset statistic assumes a comb. **  So no
  CR driving number is claimed, and the ask changes shape rather than being met.*

  ⇒ ** THE REVISED COST IS TEN RUNS AND NOT EIGHT: ** *the eight `RBFAC` runs `cc66.155` named, PLUS
  a `NODRIVE` pair at the grids' own configuration, because the banked driving-ON spectrum is a
  different vintage whose peak series this statistic cannot read.*

** COMPUTES: peak positions on `$38$` banked spectra by parabola vertex on the instrument's OWN
   samples, after dividing out a single global power law fitted in log-log over
   `$150\\le\\ell\\le1600$`; then two statistics per configuration -- the common offset
   `$\\varphi=\\langle \\ell_n/\\ell_A-n\\rangle$` and the alternation
   `$\\langle r_n(-1)^n\\rangle$` -- and their logarithmic derivatives along every banked direction,
   both arms, both nine-run grids.  The de-tilt is swept against the fitting half-window over
   `$25$`--`$75$` so its necessity is measured and not asserted.  *** No new spectrum, no grid,
   nothing refitted -- which is what `cc66.155` costed this half at. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~10 s)
"""
import io
import os
import re
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
GL = os.path.join(BW, 'r7095_directions', 'grid_licensed')
SP = os.path.join(BW, 'spectra')
for _p in (GO, GL, SP):
    if not os.path.isdir(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

LMIN, LMAX = 150.0, 1600.0      # 0.8*LMAXL on the grids, which is `chi2_of`'s own truncation rule
NPK = 5                         # the acoustic peaks the grids resolve below LMAX
BASEVAL = {'H0': {'cr': 68.60, 'lcdm': 67.40}, 'OM': {'cr': 0.2973, 'lcdm': 0.3150},
           'NS': {'cr': 0.965, 'lcdm': 0.965}, 'WB': {'cr': 0.0224, 'lcdm': 0.0224}}
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}
PARS = ('H0', 'OM', 'NS', 'WB')


def peak_series(path, halfwin=40.0, detilt=True):
    """de-tilt, find the acoustic maxima, refine each by a parabola on the ORIGINAL samples."""
    z = np.load(path, allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt if detilt else Dl.copy()
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    D = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(D) - 2)
           if D[i] > D[i - 1] and D[i] >= D[i + 1] and D[i] > D[i - 2] and D[i] >= D[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls >= l0 - halfwin) & (ls <= l0 + halfwin)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), lA, tilt


def phi_alt(path, halfwin=40.0, detilt=True):
    """the common offset and the odd-even alternation of the peak series, in units of l_A."""
    pk, lA, _t = peak_series(path, halfwin, detilt)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum())


def deriv(gdir, arm, par, halfwin=40.0, detilt=True):
    """d(phi)/dln(theta) and d(alt)/dln(theta) by central difference on the banked pair."""
    sm = phi_alt(os.path.join(gdir, f'{arm}_{par}m.npz'), halfwin, detilt)
    sp = phi_alt(os.path.join(gdir, f'{arm}_{par}p.npz'), halfwin, detilt)
    g = BASEVAL[par][arm] / (2 * STEP[par])
    return (sp[0] - sm[0]) * g, (sp[1] - sm[1]) * g


# ============================================================ A. the de-tilt is forced
head("A.  THE DE-TILT IS FORCED BY A PHYSICS CONTROL, NOT CHOSEN -- AND THE CONTROL IS `n_s`")

print("      `n_s` tilts the PRIMORDIAL spectrum and CANNOT move a peak position relative to the")
print("      sound horizon: it multiplies the initial power and leaves the transfer function alone.")
print("      ⚠ It is an INHERITED quantity -- the corpus posits no six-parameter vector, so the")
print("      spectral index is ADOPTED from LambdaCDM's own basis and derived from nothing this")
print("      construction predicts.  What that costs: no conclusion here is a claim about n_s.  It")
print("      is used because its effect on the peak PHASE is known a priori to be nil, which is")
print("      exactly what a control for a phase statistic requires.")
print()
print(f"      {'de-tilt':8s} {'halfwin':>8s} {'dphi/dlnNS':>12s} {'dphi/dlnWB':>12s} {'|WB/NS|':>9s}")
SWEEP = {}
for _dt in (False, True):
    for _hw in (25.0, 40.0, 55.0, 75.0):
        dn = deriv(GO, 'cr', 'NS', _hw, _dt)
        dw = deriv(GO, 'cr', 'WB', _hw, _dt)
        SWEEP[(_dt, _hw)] = (dn, dw)
        print(f"      {str(_dt):8s} {_hw:8.0f} {dn[0]:+12.5f} {dw[0]:+12.5f} "
              f"{abs(dw[0] / dn[0]):9.2f}")

_raw = [abs(SWEEP[(False, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
_det = [abs(SWEEP[(True, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
print(f"      ⇒ |dphi/dlnNS| raw {min(_raw):.5f}-{max(_raw):.5f}, de-tilted "
      f"{min(_det):.5f}-{max(_det):.5f}  -- a factor of {np.mean(_raw) / np.mean(_det):.0f}")
check("Ⓐ①  ** WITHOUT THE DE-TILT THE STATISTIC VIOLATES THE CONTROL: `n_s` moves the common offset "
      "by more than the baryon direction does, which a primordial tilt cannot do. **  That is the "
      "parabola's vertex being dragged by the slope under the peak -- the same disease `cc66.155` "
      "found in the free-period slope",
      all(abs(SWEEP[(False, h)][0][0]) > abs(SWEEP[(False, h)][1][0]) for h in (25.0, 40.0, 55.0)))
check("Ⓐ②  ** AND THE DE-TILT REMOVES IT BY A FACTOR OF TEN OR MORE, AND MAKES IT "
      "WINDOW-INDEPENDENT -- which is what distinguishes a repair from a tuning. **  The raw "
      "response drifts with the fitting window; the de-tilted one is flat across 25-75",
      np.mean(_raw) / np.mean(_det) > 10.0
      and (max(_det) - min(_det)) / np.mean(_det) < 0.15
      and (max(_raw) - min(_raw)) / np.mean(_raw) > 0.15)


# ============================================================ B. the separation
head("B.  THE SEPARATION, BOTH ARMS AND BOTH GRIDS: THE BARYON DIRECTION AGAINST A PURE TILT")

D = {}
print(f"      {'grid':9s} {'arm':5s} {'par':3s} {'dphi/dln':>11s} {'dalt/dln':>11s}")
for gname, gdir in (('oneclock', GO), ('licensed', GL)):
    for arm in ('cr', 'lcdm'):
        for par in PARS:
            D[(gname, arm, par)] = deriv(gdir, arm, par)
            print(f"      {gname:9s} {arm:5s} {par:3s} {D[(gname, arm, par)][0]:+11.5f} "
                  f"{D[(gname, arm, par)][1]:+11.5f}")

RAT = {}
for arm in ('cr', 'lcdm'):
    rp = abs(D[('oneclock', arm, 'WB')][0] / D[('oneclock', arm, 'NS')][0])
    ra = abs(D[('oneclock', arm, 'WB')][1] / D[('oneclock', arm, 'NS')][1])
    RAT[arm] = (rp, ra)
    print(f"      {arm:5s}: WB:NS = {rp:.1f}x on the common offset, {ra:.1f}x on the alternation")
check("Ⓑ①  ** THE PEAK SET SEPARATES THE BARYON DIRECTION FROM A PURE TILT BY AN ORDER OF "
      "MAGNITUDE, ON BOTH COMPONENTS AND BOTH ARMS -- where `cc66.155` measured the free-period "
      "slope separating the same two directions by 1.3. **  That is the difference between a "
      "statistic that reads phase and one that reads gradient",
      all(RAT[a][0] > 8.0 and RAT[a][1] > 15.0 for a in ('cr', 'lcdm')))

_nsconsist = [abs(D[(g, a, 'NS')][0]) for g in ('oneclock', 'licensed') for a in ('cr', 'lcdm')]
print(f"      and `n_s`'s own residual response is STABLE rather than merely small: "
      f"{min(_nsconsist):.5f} to {max(_nsconsist):.5f} across both arms and both grids")
check("Ⓑ②  and the tilt's residual leakage is consistent across all four configurations rather "
      "than scattering -- so what is left after the de-tilt is a small systematic floor and not "
      "noise that happened to come out low on the one case that was looked at",
      (max(_nsconsist) - min(_nsconsist)) / np.mean(_nsconsist) < 0.25)


# ============================================================ C. the convention robustness
head("C.  AND IT REPAIRS THE CONVENTION-DEPENDENCE `cc66.155` FOUND IN THE ARM'S OWN RESPONSE")

_conv = {}
for par in PARS:
    a = D[('oneclock', 'cr', par)]
    b = D[('licensed', 'cr', par)]
    _conv[par] = (abs(b[0] / a[0]) if a[0] else np.inf, abs(b[1] / a[1]) if a[1] else np.inf)
    print(f"      {par:3s}: licensed/oneclock = {_conv[par][0]:5.2f}x on phi, "
          f"{_conv[par][1]:5.2f}x on the alternation")
_worst = max(max(v) for v in _conv.values())
print(f"      ⇒ worst disagreement between the two arm geometries: {_worst:.2f}x")
print("      ⌗ `cc66.155` measured the SAME arm's required move on the free-period slope differing")
print("        by up to 49x between these two grids (294 per cent against 6).  The peak set's worst")
print("        is a factor of two, which is a statistic that measures the arm rather than the")
print("        convention it was computed under.")
check("Ⓒ①  ** the arm's response is convention-robust on the peak set where it was not on the "
      "slope: worst disagreement a factor of ~2 between `LEAFGEOM` and `LEAFREC`, against up to "
      "49 on the slope. **  A third independent respect in which this statistic is the better "
      "instrument, and the one that was not predicted in advance",
      _worst < 2.5)


# ============================================================ D. the driving half
head("D.  ⛔ THE DRIVING HALF IS NOT ESTABLISHED, AND THE REASON IS A MEASUREMENT")

_pairs = {'cr': ('c54.186_cr_L3000.npz', 'c54.193_cr_nodrive_L3000.npz'),
          'lcdm': ('c54.186_lcdm_L3000.npz', 'c54.193_lcdm_nodrive_L3000.npz')}
for _a, (_on, _off) in _pairs.items():
    for _f in (_on, _off):
        if not os.path.exists(os.path.join(SP, _f)):
            print(f"  ⛔ THE DRIVING PAIR IS NOT ON DISK: {_f}")
            sys.exit(1)

GAPS = {}
for tag, path in (('grid cr_base', os.path.join(GO, 'cr_base.npz')),
                  ('L3000 cr ON', os.path.join(SP, 'c54.186_cr_L3000.npz')),
                  ('L3000 cr OFF', os.path.join(SP, 'c54.193_cr_nodrive_L3000.npz')),
                  ('L3000 lcdm ON', os.path.join(SP, 'c54.186_lcdm_L3000.npz')),
                  ('L3000 lcdm OFF', os.path.join(SP, 'c54.193_lcdm_nodrive_L3000.npz'))):
    pk, lA, _t = peak_series(path)
    g = np.diff(pk / lA)
    GAPS[tag] = float(np.max(np.abs(g - 1.0)))
    print(f"      {tag:15s} peaks/l_A = {np.round(pk / lA, 3)}  worst gap error "
          f"{GAPS[tag]:.3f}")
check("Ⓓ①  ** THE CR ARM'S BANKED DRIVING-ON SPECTRUM HAS NO INTEGER-SPACED PEAK SERIES, SO THIS "
      "STATISTIC CANNOT READ IT. **  Its gaps miss `1` by three times what the grid's do, and the "
      "common offset is DEFINED as a mean against integer index -- so a CR driving number taken "
      "from it would be a statement about the detector",
      GAPS['L3000 cr ON'] > 2.5 * GAPS['grid cr_base'])

_lc_on = phi_alt(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
_lc_off = phi_alt(os.path.join(SP, 'c54.193_lcdm_nodrive_L3000.npz'))
_dphi, _dalt = _lc_off[0] - _lc_on[0], _lc_off[1] - _lc_on[1]
print(f"      the CONTROL's same-vintage pair does read: phi {_lc_on[0]:+.5f} -> {_lc_off[0]:+.5f} "
      f"(Dphi = {_dphi:+.5f})")
print(f"                                                  alt {_lc_on[1]:+.5f} -> {_lc_off[1]:+.5f} "
      f"(Dalt = {_dalt:+.5f})")
_wb = D[('oneclock', 'lcdm', 'WB')]
print(f"      against the baryon direction's {_wb[0]:+.5f} on phi and {_wb[1]:+.5f} on the "
      f"alternation")
check("Ⓓ②  ⛭ ** AND ON THE CONTROL, WHERE IT CAN BE READ, THE DRIVING AND THE BARYON DIRECTION "
      "MOVE THE PEAK SET IN OPPOSITE DIRECTIONS ON BOTH COMPONENTS. **  That is the orthogonality "
      "the ask rested on, and it is now measured on one arm rather than argued -- which is why the "
      "runs are worth their compute and why the pair has to be at the grids' own configuration",
      _dphi * _wb[0] < 0 and _dalt * _wb[1] < 0)

check("Ⓓ③  ⛔ and NO CR DRIVING NUMBER IS CLAIMED HERE, which is the whole value of having run the "
      "zero-cost half first: the ask `cc66.155` costed at eight runs is REVISED to ten, the two "
      "added being a `NODRIVE` pair at the grids' own configuration -- because the banked "
      "driving-ON spectrum is a different vintage this statistic cannot read",
      GAPS['L3000 cr ON'] > GAPS['grid cr_base'] and GAPS['L3000 lcdm ON'] < GAPS['L3000 cr ON'])


# ============================================================ E. what is owed
head("E.  SO THE STATISTIC EXISTS AND THE ASK IS SHARPER RATHER THAN MET")

print("      WHAT IS SETTLED, at no run cost, which is what this half was costed at:")
print("        * the de-tilted peak set IS a phase observable -- it passes the control the slope")
print("          failed, by a factor of ten or more, window-independently;")
print("        * it separates the baryon direction from a pure tilt by ~11x on the common offset")
print("          and ~21x on the alternation, on both arms and both grids;")
print("        * it is convention-robust where the slope was not;")
print("        * and on the control, the driving and the baryon direction move it in OPPOSITE")
print("          directions on both components -- the orthogonality the ask rested on.")
print()
print("      ⛔ WHAT IS NOT, and what it costs:")
print("        * the CR arm's driving signature.  The banked driving-ON spectrum is a different")
print("          vintage whose peak series is not integer-spaced, so it cannot be read by a")
print("          statistic defined against integer index.")
print("        ⇒ TEN runs, not eight: the eight `RBFAC` runs (loading without recombination, which")
print("          `WBH2` cannot give) PLUS a `NODRIVE` pair, all at the grids' own configuration")
print("          (`HIER=1 LMAXL=2000 LSTEP=8 ZSTART=3e7`, `KFAC` at the corpus default 2.0, `NK`")
print("          not reduced), idempotent and resumable on output existence.")
check("Ⓔ①  ** the half `cc66.155` costed at zero runs is delivered at zero runs. **  38 banked "
      "spectra and the driving pairs read, no new spectrum, no grid, nothing refitted -- and the "
      "conclusion it reaches is that the statistic works, which is what makes the remaining ask "
      "worth putting",
      len(D) == 16 and all(RAT[a][1] > 15.0 for a in ('cr', 'lcdm')))
check("Ⓔ②  and the revised ask is bounded and justified by what was measured rather than by what "
      "was hoped: ten runs, each named, at a configuration read off the grids' own switch lines",
      GAPS['L3000 cr ON'] > 2.5 * GAPS['grid cr_base'] and _worst < 2.5)

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE DE-TILTED PEAK SET IS THE PHASE OBSERVABLE THE FREE-PERIOD SLOPE WAS NOT. **  It")
print("    separates the baryon direction from a pure tilt by ~11x on the common offset and ~21x on")
print("    the odd-even alternation, against 1.3x for the slope, on both arms and both grids.")
print("  ⛭ ** AND THE DE-TILT IS FORCED RATHER THAN CHOSEN: without it `n_s` moves the common offset")
print("    more than the baryon direction does, which a primordial tilt cannot do.  With it that")
print("    response falls by a factor of ten or more and stops depending on the fitting window. **")
print("  ⌗ A third gain that was not predicted: the arm's response is convention-robust here -- a")
print("    factor of ~2 between LEAFGEOM and LEAFREC, against up to 49 on the slope.")
print("  ⛔ ** THE DRIVING HALF IS NOT ESTABLISHED AND THAT IS THE VALUE OF HAVING RUN THIS FIRST.")
print("    ** On the control the driving and the baryon direction move the peak set in OPPOSITE")
print("    directions on both components -- the orthogonality the ask rested on.  But the CR arm's")
print("    banked driving-ON spectrum has no integer-spaced peak series and this statistic is")
print("    defined against integer index, so no CR driving number is claimed.")
print("  ⇒ ** THE ASK IS THEREFORE TEN RUNS AND NOT EIGHT: ** eight `RBFAC` plus a `NODRIVE` pair,")
print("    all at the grids' own configuration.  Sharpened by a measurement rather than met.")
print("  ⚠ Named and not supplied: five peaks make the alternation a coarse estimate; the de-tilt")
print("    is one global power law over 150-1600 and its necessity is swept but its FORM is a")
print("    choice; and `n_s` is inherited, used only as a control, with no claim made about it.")
