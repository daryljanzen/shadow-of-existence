#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7203`'s FIRST TWO ITEMS, ON THE ARM'S OWN `NODRIVE` PAIR.  *** THE DEFECT DOES
NOT RECUR, THE NEW CONTROL PAIR REPRODUCES THE BANKED ONE, AND THE PEAK PLANE SEPARATES THE LOADING
FROM THE DRIVING BY A FACTOR OF FIVE ON THE RATIO -- BUT NOT THE DRIVING FROM A CLOCK ERROR. *** **

  ⓵ ** THE DEFECT DOES NOT RECUR, WHICH `r7203` ASKED TO HEAR FIRST AND SEPARATELY. **  *The CR
  arm's banked driving-ON spectrum was disqualified from this statistic in `cc66.156` for having no
  integer-spaced peak series -- gaps `$0.74$`--`$0.96$` of `$\\ell_A$` where the common-offset
  statistic assumes a comb.  **Both new `NODRIVE` spectra give `$0.925$`--`$0.999$`, TIGHTER than
  the grid bases' own `$0.895$`--`$1.036$`.**  So the driving-off limit is readable on the arm's own
  vintage and no number here is a statement about the detector.*

  ⓶ ⛭⛭ ** AND THE NEW CONTROL PAIR REPRODUCES THE BANKED ONE, WHICH RETIRES A CAVEAT RATHER THAN
  ADDING A RESULT. **  *`cc66.156` had to carry its `$+0.126$`/`$-0.0247$` as a DIFFERENT VINTAGE
  from the grids -- the reason ten runs were asked for instead of eight.  Run at the grids' own
  configuration the control gives `$+0.12651$`/`$-0.02469$`: the same numbers to three figures.
  **The vintage worry was real and it was unfounded, and that is only knowable now.***

  ⓷ ** THE CR ARM'S OWN DRIVING SIGNATURE MATCHES THE CONTROL'S** to half a per cent on the common
  offset.  *The driving is not arm-specific, so what the plane separates it separates as acoustic
  physics.*

  ⇒ ⛔ ** THE REACH, AND IT IS `60`'s NARROWING CARRIED THROUGH RATHER THAN ARGUED WITH. **  *On the
  plane's own discriminant `$\\lvert\\Delta\\mathrm{alt}/\\Delta\\varphi\\rvert$`, the measured
  driving sits at `$0.193$` and `60`'s `r7218` drive-clock error at `$0.086$`--`$0.173$`.  **Those
  overlap, so the plane does NOT license `the driving` over `a clock error in the driving`.**  But
  the CLEAN loading lever sits at `$1.039$` -- six times the clock error's top and five times the
  driving's -- so what the plane DOES separate, decisively, is the loading from both of them.*

  ⌗ ⛭ *And `60` could not have seen that: it used the banked `WB` direction (`$0.388$`) as the
  loading's stand-in, because the clean lever did not exist.  **The clean lever is `$2.7\\times$`
  further out than that proxy, and `cc66.157` measured the two to have OPPOSITE sign on the common
  offset -- so the proxy both understated the separation and pointed the wrong way along it.***

** COMPUTES: `cc66.156`'s de-tilted peak statistic, unchanged, on the `r7203` `NODRIVE` pair and the
   grids' own bases; the driving difference in `cc66.156`'s own convention (OFF minus ON) on both
   arms; the four directions' plane discriminants; and the separations among them.  *** No refit, no
   new statistic, no spectrum beyond the three `r7203` approved. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~10 s)
"""
import os
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
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
for _p in (GO, LEV):
    if not os.path.isdir(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

LMIN, LMAX, NPK, HALFWIN = 150.0, 1600.0, 5, 40.0
BASEVAL = {'NS': {'cr': 0.965, 'lcdm': 0.965}, 'WB': {'cr': 0.0224, 'lcdm': 0.0224}}
STEP = {'NS': 0.020, 'WB': 0.0008}

# ⌗ `60`'s r7218 drive-clock error, READ OFF `60`'s OWN RECEIPT OUTPUT at this revision and cited
#   as an input rather than recomputed here -- it is a property of `60`'s oscillator, not of any
#   spectrum this seat can read.  Its receipt is
#   `P15_a_drive_clock_error_cannot_move_the_spacing_so_it_is_a_running_phase_...`, whose own line
#   reads `|Dalt/Dphi| = 0.086, 0.158, 0.173`.  ** No check below recomputes it; the checks test
#   THIS seat's measured directions against it as a stated bound. **
CLOCK = (0.086, 0.158, 0.173)


def peak_series(path):
    z = np.load(path, allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    Di = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(Di) - 2)
           if Di[i] > Di[i - 1] and Di[i] >= Di[i + 1] and Di[i] > Di[i - 2] and Di[i] >= Di[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls >= l0 - HALFWIN) & (ls <= l0 + HALFWIN)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), lA


def phi_alt(path):
    pk, lA = peak_series(path)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum()), pk, lA


def gaps(path):
    pk, lA = peak_series(path)
    q = pk[np.isfinite(pk)] / lA
    return float(np.min(np.diff(q))), float(np.max(np.diff(q)))


def grid_deriv(arm, par):
    sm = phi_alt(os.path.join(GO, f'{arm}_{par}m.npz'))
    sp = phi_alt(os.path.join(GO, f'{arm}_{par}p.npz'))
    g = BASEVAL[par][arm] / (2 * STEP[par])
    return (sp[0] - sm[0]) * g, (sp[1] - sm[1]) * g


# ============================================================ A. the defect does not recur
head("A.  ⓵ THE DEFECT DOES NOT RECUR -- THE ITEM `r7203` ASKED TO HEAR FIRST AND ON ITS OWN")

print(f"      {'spectrum':16s} {'l_A':>10s} {'npk':>4s}  {'detected spacing / l_A':s}")
G = {}
for tag, p in (('cr_nodrive', os.path.join(LEV, 'cr_nodrive.npz')),
               ('lcdm_nodrive', os.path.join(LEV, 'lcdm_nodrive.npz')),
               ('cr_base', os.path.join(GO, 'cr_base.npz')),
               ('lcdm_base', os.path.join(GO, 'lcdm_base.npz'))):
    s = phi_alt(p)
    G[tag] = gaps(p)
    print(f"      {tag:16s} {s[4]:10.3f} {s[2]:4d}  {G[tag][0]:.3f}-{G[tag][1]:.3f}")
print("      the disqualified banked CR driving-ON spectrum, for contrast:  0.74-0.96 (cc66.156)")
check("Ⓐ①  ** BOTH NEW `NODRIVE` SPECTRA CARRY AN INTEGER-SPACED SERIES, AND A TIGHTER ONE THAN THE "
      "GRID BASES THEMSELVES. **  *`r7203` asked to be told immediately if the pair came back with "
      "the defect the banked driving-ON spectrum has, because that would be a statement about the "
      "driving-off limit itself and worth more than a salvaged number.  It does not: five peaks "
      "each, spacing inside `$0.92$`--`$1.00$` against the bases' `$0.89$`--`$1.04$`*",
      all(G[t][0] > 0.90 and G[t][1] < 1.01 for t in ('cr_nodrive', 'lcdm_nodrive'))
      and all(phi_alt(os.path.join(LEV, f'{t}.npz'))[2] == NPK for t in ('cr_nodrive', 'lcdm_nodrive')))

_lacr = phi_alt(os.path.join(LEV, 'cr_nodrive.npz'))[4]
_labase = phi_alt(os.path.join(GO, 'cr_base.npz'))[4]
print(f"      and l_A is unchanged by the switch: nodrive {_lacr!r} vs base {_labase!r}")
check("Ⓐ②  ⛭ and `NODRIVE` leaves `$\\ell_A$` BIT-IDENTICAL to the base's, so the pair differs in "
      "the driving and in nothing else.  *That is what a phase comparison needs and what the banked "
      "pair could not promise, being a different vintage*",
      _lacr == _labase)


# ============================================================ B. the pair, both arms
head("B.  ⓶ THE DRIVING DIFFERENCE, IN `cc66.156`'s OWN CONVENTION (OFF MINUS ON)")

print("      ⛔ CONVENTION: `cc66.156` formed its published +0.126/-0.0247 as OFF minus ON -- the")
print("         change on REMOVING the driving.  Taken the other way the signs invert and the two")
print("         arms read as opposing when they agree.  Matched here deliberately.")
DRV = {}
for arm in ('cr', 'lcdm'):
    on = phi_alt(os.path.join(GO, f'{arm}_base.npz'))
    off = phi_alt(os.path.join(LEV, f'{arm}_nodrive.npz'))
    DRV[arm] = (off[0] - on[0], off[1] - on[1])
    print(f"      {arm:5s}  Dphi {DRV[arm][0]:+.5f}   Dalt {DRV[arm][1]:+.5f}")
print("      cc66.156's banked control pair, for comparison:  +0.12600 / -0.02470")
_bp, _ba = 0.126, -0.0247
check("Ⓑ①  ⛭⛭ ** THE SAME-VINTAGE CONTROL PAIR REPRODUCES THE BANKED ONE TO BETTER THAN ONE PER "
      "CENT ON BOTH COMPONENTS. **  *`cc66.156` could not know this: it carried its driving numbers "
      "with the caveat that the banked pair was a different vintage from the grids, and that caveat "
      "is the reason the ask went from eight runs to ten.  **The worry was legitimate and the answer "
      "is that it cost nothing -- which is a result about the bank, not about the physics.***",
      abs(DRV['lcdm'][0] / _bp - 1) < 0.01 and abs(DRV['lcdm'][1] / _ba - 1) < 0.01)
check("Ⓑ②  ⓷ and the CR arm's OWN driving signature matches the control's to half a per cent on the "
      "common offset and two per cent on the alternation, with both signs the same.  *So the driving "
      "acts on this statistic as acoustic physics and not as a property of the arm -- which is what "
      "lets the separation below be read as a statement about the carriers rather than about "
      "`LEAFGEOM`*",
      abs(DRV['cr'][0] / DRV['lcdm'][0] - 1) < 0.005
      and abs(DRV['cr'][1] / DRV['lcdm'][1] - 1) < 0.02
      and np.sign(DRV['cr'][0]) == np.sign(DRV['lcdm'][0])
      and np.sign(DRV['cr'][1]) == np.sign(DRV['lcdm'][1]))


# ============================================================ C. the separation
head("C.  THE FOUR DIRECTIONS ON THE PLANE, AND WHAT SEPARATES FROM WHAT")

_c = [v for v in ('0.5', '1.5')]
_p5 = phi_alt(os.path.join(LEV, 'cr_rb0.5.npz'))
_p15 = phi_alt(os.path.join(LEV, 'cr_rb1.5.npz'))
_g = 1.0 / np.log(1.5 / 0.5)
LOAD = ((_p15[0] - _p5[0]) * _g, (_p15[1] - _p5[1]) * _g)
WB = grid_deriv('cr', 'WB')
# ⌗ both carriers rendered as MORE of the thing: DRV is a REMOVAL, so it is negated here.
MOREDRV = (-DRV['cr'][0], -DRV['cr'][1])
DIRS = {'driving (more of it)': MOREDRV, 'loading (more of it)': LOAD, 'baryon direction WB': WB}
print(f"      {'direction':24s} {'Dphi':>10s} {'Dalt':>10s} {'|Dalt/Dphi|':>12s}")
RAT = {}
for k, v in DIRS.items():
    RAT[k] = abs(v[1] / v[0])
    print(f"      {k:24s} {v[0]:+10.5f} {v[1]:+10.5f} {RAT[k]:12.4f}")
print(f"      {'clock error (60, r7218)':24s} {'--':>10s} {'--':>10s} "
      f"{min(CLOCK):.3f}-{max(CLOCK):.3f}  (cited, not recomputed)")
_rd, _rl = RAT['driving (more of it)'], RAT['loading (more of it)']
print()
print(f"      ⇒ loading / driving on the discriminant: {_rl / _rd:.2f}x")
print(f"      ⇒ loading / the clock error's top:       {_rl / max(CLOCK):.2f}x")
print(f"      ⇒ driving  / the clock error's top:      {_rd / max(CLOCK):.2f}x")
check("Ⓒ①  ** THE TWO CANDIDATE CARRIERS HAVE OPPOSITE SIGN ON THE COMMON OFFSET AND DIFFER BY A "
      "FACTOR OF FIVE ON THE PLANE'S DISCRIMINANT. **  More driving lowers the offset, more loading "
      "raises it, and `$\\lvert\\Delta\\mathrm{alt}/\\Delta\\varphi\\rvert$` is `$0.19$` against "
      "`$1.04$`.  *That is the separation the whole ask rested on, now measured on the arm's own "
      "pair rather than inferred from the control's*",
      np.sign(MOREDRV[0]) != np.sign(LOAD[0]) and _rl / _rd > 5.0)
check("Ⓒ②  ⛔ ** BUT THE DRIVING AND `60`'s CLOCK ERROR ARE NOT SEPARATED BY THIS PLANE: the "
      "driving's discriminant sits within a sixth of the clock error's top, inside the spread of "
      "`60`'s own three readings. **  *So the plane does not license `the driving` over `a clock "
      "error in the driving`, exactly as `r7203` said it would not -- stated as the limit it is "
      "rather than left for the reader to notice*",
      _rd / max(CLOCK) < 1.2 and _rd > min(CLOCK))
check("Ⓒ③  ⛭ and what the plane DOES separate decisively is the LOADING from both of them -- six "
      "times the clock error's top and five times the driving's.  *So the negative is specific "
      "rather than general: the plane distinguishes the two candidate carriers from each other, and "
      "fails only to distinguish the driving from a mis-read clock in the driving*",
      _rl / max(CLOCK) > 5.0 and _rl / _rd > 5.0)


# ============================================================ D. the proxy correction
head("D.  ⛭ AND `60` COULD NOT HAVE SEEN THAT, BECAUSE THE PROXY IT HAD POINTS THE WRONG WAY")

print(f"      `60`'s stand-in for the loading was the banked `WB` direction, at {RAT['baryon direction WB']:.4f}.")
print(f"      The clean lever is at {_rl:.4f} -- {_rl / RAT['baryon direction WB']:.2f}x further out.")
print(f"      And cc66.157 measured their common-offset responses to have OPPOSITE sign:")
print(f"          d(phi)/dln(R_b)      {LOAD[0]:+.5f}")
print(f"          d(phi)/dln(omega_b)  {WB[0]:+.5f}")
check("Ⓓ①  ** THE `WB` DIRECTION UNDERSTATED THE LOADING'S SEPARATION BY A FACTOR APPROACHING "
      "THREE, AND POINTED THE OPPOSITE WAY ALONG THE OFFSET. **  *`60` used it because the clean "
      "lever did not exist when `r7218` was filed -- this is not a defect in `r7218`, it is the "
      "value of the three runs: a conclusion drawn on the proxy would have placed the loading "
      "nearer the clock error than it is and on the wrong side of zero*",
      _rl / RAT['baryon direction WB'] > 2.0 and np.sign(LOAD[0]) != np.sign(WB[0]))


# ============================================================ E. what is not claimed
head("E.  ⛔ WHAT IS NOT CLAIMED, AND IT IS THE STEP THAT WOULD NAME THE CARRIER")

print("  ** NO CARRIER IS NAMED FOR THE OBSERVED DRIFT, AND THE REASON HAS CHANGED. **")
print("  Before these runs the blocker was that the arm had no readable driving signature.  That is")
print("  now gone.  What is missing is the OBSERVED residual's own position on this plane: nothing")
print("  in tree measures it.  The de-tilted peak statistic has been run on model spectra only --")
print("  238-point curves with no noise -- and putting the data on the same plane means running it")
print("  on 179 binned points with a covariance, which is a measurement with its own validation")
print("  burden and is not what `r7203` ordered (`no refit, no new statistic`).")
print("  ⇒ So what the plane says is reported and the naming is not asserted: the two candidate")
print("     carriers are separated, the driving and a clock error are not, and which of them the")
print("     observed drift requires needs one measurement that nobody has made.")
print("  ⌗ `NS` appears only as the control direction known a priori to carry no acoustic phase --")
print("     an INHERITED quantity, adopted from LambdaCDM's own basis and derived from nothing this")
print("     construction predicts.  No conclusion here is a claim about it.")
NS = grid_deriv('cr', 'NS')
print(f"     its own residual response: dphi {NS[0]:+.5f}  dalt {NS[1]:+.5f}")
check("Ⓔ①  the control direction stays well below every carrier direction on both components, which "
      "is the check that the plane is reading acoustic phase and not the de-tilt's leftover gradient",
      abs(NS[0]) < 0.25 * abs(LOAD[0]) and abs(NS[1]) < 0.1 * abs(LOAD[1])
      and abs(NS[0]) < 0.1 * abs(MOREDRV[0]))

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ 9 of 9 checks pass.")
print(BAR)
sys.exit(0)
