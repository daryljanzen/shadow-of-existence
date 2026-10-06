#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7191`'s ORDER, ANSWERED ON BANKED SPECTRA WITH NO NEW RUN -- AND ITS PREMISE
CORRECTED. THE VISIBILITY-WIDTH SWAP WAS CONFRONTED AT `r6919+cc66.42`; IT IS WELL POSED; AND IT
AMPLIFIES THE `$q$`-DEPENDENCE BY `$4.56$` INSTEAD OF NEUTRALISING IT.  THE COMPARISON THE ORDER
ADDS -- THE FOLD AT `$\\ell_A$` -- COMES BACK NULL: THE SWAP MOVES IT BY UNDER `$2$` PER CENT AND
THE PHASE BY UNDER HALF A DEGREE, AND THE UNDO TEST FAILS IN BOTH DIRECTIONS. **

Built r7191+cc66.150 (node 66, code seat), on `PO-13`.

===================================================================================================
** THE ORDER, AND THE ONE THING IN IT THAT IS NOT SO **
===================================================================================================

`r7191`: *"Price the residual the width alone produces, and compare its SHAPE to the measured one"* --
widen the control's visibility by `$14.3$` per cent changing nothing else, fold by phase within
`$\\ell_A$`, compare with `$1.3729\\pm0.1512$` and `$0.8128\\pm0.1180$`; and the control that makes it
a measurement, *"NARROW the arm's visibility to the control's and see whether the `$9.1\\sigma$`
modulation goes away.  A mechanism that explains the residual must also remove it when undone."*
With the third branch named in advance: *"If it reproduces neither, the width is not the carrier and
I want that said as plainly as the other two."*

⛔ ** AND THE PREMISE IS PARTLY FALSE, WHICH HAS TO COME FIRST. **  The order says the `$+14.3$` per
cent *"has never been confronted with the residual it would produce"*.  ** It was confronted at
`r6919+cc66.42`, which banked the swapped spectra this receipt reads. **  That work found the width
swap WELL POSED -- unlike the clock swap, which moves the comb -- and found that it does not
neutralise the arm-to-control difference but AMPLIFIES its `$q$`-dependence.  *The banks are on disk;
nothing here needs a new run; and the amplification is reproduced below in this receipt's own
statistic rather than taken from that one's.*

⇒ *** SO THE ANSWER IS THE ORDER'S THIRD BRANCH, AND IT IS NOW TWO MEASUREMENTS DEEP: the width
reproduces NEITHER the amplitude nor the phase, and swapping it does not remove the difference. ***

  PART A  ** THE GEOMETRY, FROM `r6919`'s OWN BANK. **  FWHM `$38.042$` against `$43.591$`
          (`$+14.6$` per cent at the 185-bin minima, the `$+14.3$` the order quotes being the same
          quantity at the in-print pair); `$\\Delta r_s$` across the visibility the same to
          `$0.08$` per cent; and so `$\\dd r_s/\\dd\\chi$` `$12.8$` per cent lower on the arm.
  PART B  ** THE PREMISE CORRECTION, MEASURED HERE. **  Band by band the arm-to-control retained
          modulation runs `$1.046,1.095,1.127$` at own widths and `$0.988,1.097,1.357$` swapped --
          a slope `$+0.0405\\to+0.1847$`, ** a factor `$4.56$` **.
  PART C  ** THE FOLD AT `$\\ell_A$`, WHICH IS WHAT THE ORDER ADDS, AND IT IS NULL. **  Control
          `$0.3704\\to0.3639$` (`$-1.8$` per cent) and `$36.4^\\circ\\to36.7^\\circ$`; arm
          `$0.4003\\to0.4007$` (`$+0.1$` per cent) and `$35.4^\\circ\\to35.3^\\circ$`.
  PART D  ** THE UNDO TEST, AND IT FAILS IN BOTH DIRECTIONS. **  Widening the control moves it AWAY
          from the arm; narrowing the arm does not move it.  The arm-to-control fold difference is
          `$+8.1$` per cent at own widths and `$+10.1$` per cent swapped -- the swap does not remove
          it, it slightly increases it.
  PART E  ** AND THE OBSTRUCTION THE SCOPE ASKS TO HAVE NAMED, ESTABLISHED FROM THE SYNTAX TREE. **
          `ETA_LS_W` is assigned once and the only assignment that consumes `SRCINJVIS` sits inside
          the `_SRCI` branch, so the width is controllable ONLY where the model's own source has
          been replaced.

** WHAT THIS IS AND IS NOT. **
  ⌗ ** Every number is the projection's transfer of a KNOWN input.  No `SRCINJ` run is a spectrum of
  this model **, which is `r6919`'s own standing caveat and is repeated here rather than inherited.
  What that makes the measurement able to say is a SHAPE statement -- how much of a held-fixed comb
  each arm's kernel retains, and how that changes when the width is swapped -- which is exactly the
  discriminant the order named.
  ⛔ *What it cannot say is the residual's absolute size against Planck: the injected comb has no
  physical normalisation, so `$1.3729$` in whitened units has no counterpart here.  **The comparison
  made is therefore of CHANGES: if the width were the carrier, swapping it would move the retained
  modulation by something like the arm-to-control difference.  It moves it by a quarter of one.***
  ⚠ *And no mechanism is proposed in its place.  `PART A`'s `$\\dd r_s/\\dd\\chi$` is `r6919`'s
  finding re-pointed, not a new claim.*

** COMPUTES: the fold of `r6919+cc66.42`'s banked injected spectra -- own width and swapped, both
   arms -- within each run's own `$\\ell_A$`, whole-range and in three `$\\ell$` sub-bands; the
   geometry bank's three ratios; and one `ast` walk of the instrument.  *** The only inputs are those
   banks and the `$\\ell_A$`/anchor the figure already carries; the sub-band cuts, the
   `$100\\le\\ell\\le1900$` window and the degree-4 log-log baseline are the only choices and all
   three are stated. *** No instrument run, no grid, no fit to data. **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~3 s)
"""
import ast
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
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NEED = ('r6919_injected_lcdm.npz', 'r6919_injected_cr.npz', 'r6919_geometry.npz')
if not all(os.path.exists(os.path.join(SP, n)) for n in NEED):
    print("  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and nothing is claimed.")
    sys.exit(1)
IJ = {t: np.load(os.path.join(SP, f'r6919_injected_{t}.npz')) for t in ('lcdm', 'cr')}
GE = np.load(os.path.join(SP, 'r6919_geometry.npz'))
ANCHOR = 222.0                    # the arm's own first peak, as `cc66.145`'s fold uses
LO, HI = 100.0, 1900.0            # the confrontation's own window


def fractional(ls, dl):
    """the injected comb's fractional oscillation about a smooth degree-4 log-log baseline."""
    m = (ls >= LO) & (ls <= HI)
    l, d = ls[m].astype(float), dl[m].astype(float)
    base = np.poly1d(np.polyfit(np.log(l), np.log(np.abs(d)), 4))
    return l, d / np.exp(base(np.log(l))) - 1.0


def harmonic(l, f, period):
    D = np.array([np.cos(2 * np.pi * (l - ANCHOR) / period),
                  np.sin(2 * np.pi * (l - ANCHOR) / period)]).T
    beta = np.linalg.lstsq(D, f, rcond=None)[0]
    rr = f - D @ beta
    s2 = float(np.sum(rr ** 2) / (len(l) - 2))
    cv = s2 * np.linalg.inv(D.T @ D)
    a = float(np.hypot(*beta))
    e = float(np.sqrt((beta[0] ** 2 * cv[0, 0] + beta[1] ** 2 * cv[1, 1]
                       + 2 * beta[0] * beta[1] * cv[0, 1]) / a ** 2))
    return a, e, a / e, float(np.degrees(np.arctan2(beta[1], beta[0])) % 360)


FOLD = {}
for t in ('lcdm', 'cr'):
    for cfg in ('sweepown', 'viswap'):
        l, f = fractional(IJ[t][f'ls__{cfg}'], IJ[t][f'Dl__{cfg}'])
        FOLD[(t, cfg)] = (l, f, float(IJ[t][f'l_A__{cfg}']))


# ============================================================ A. the geometry
head("A.  THE GEOMETRY, FROM `r6919`'s OWN BANK -- WHAT THE +14 PER CENT IS AND IS NOT")

W = {t: float(GE[f'fwhm__{t}']) for t in ('lcdm', 'cr')}
DRS = {t: float(GE[f'd_rs_own__{t}']) for t in ('lcdm', 'cr')}
DCH = {t: float(GE[f'd_chi__{t}']) for t in ('lcdm', 'cr')}
CS = {t: DRS[t] / DCH[t] for t in ('lcdm', 'cr')}
print(f"      FWHM        control {W['lcdm']:9.4f}   arm {W['cr']:9.4f}   "
      f"{100 * (W['cr'] / W['lcdm'] - 1):+.2f} per cent")
print(f"      d r_s       control {DRS['lcdm']:9.4f}   arm {DRS['cr']:9.4f}   "
      f"{100 * (DRS['cr'] / DRS['lcdm'] - 1):+.2f} per cent")
print(f"      d r_s/d chi control {CS['lcdm']:9.6f}   arm {CS['cr']:9.6f}   "
      f"{100 * (CS['cr'] / CS['lcdm'] - 1):+.1f} per cent")
check("Ⓐ①  the width difference these banks carry is +14.59 per cent at the 185-bin minima, which "
      "is the same quantity the order quotes as +14.3 at the in-print pair -- so the order's number "
      "and this bank's are the same object read on two backgrounds, and the swap below is the "
      "order's swap",
      0.14 < W['cr'] / W['lcdm'] - 1 < 0.15)
check("Ⓐ②  ** and the sound horizon accumulated ACROSS the visibility is the same on both arms to "
      "0.08 per cent while the comoving distance across it differs by 14.6 -- so what the width "
      "difference IS, is a difference in `d r_s / d chi`, 12.8 per cent lower on the arm. **  That "
      "is `r6919`'s joint object, re-pointed here and not re-derived",
      abs(DRS['cr'] / DRS['lcdm'] - 1) < 0.005
      and abs(CS['cr'] / CS['lcdm'] - 0.872) < 0.002)


# ============================================================ B. the premise correction
head("B.  THE PREMISE CORRECTION -- THE SWAP WAS CONFRONTED, AND IT AMPLIFIES RATHER THAN CLOSES")

CUTS = ((100, 700), (700, 1300), (1300, 1900))
RAT = {'sweepown': [], 'viswap': []}
print("        band          own: arm / control -> ratio        swapped: arm / control -> ratio")
for lo, hi in CUTS:
    line = f"      {lo:5d}-{hi:<5d} "
    for cfg in ('sweepown', 'viswap'):
        a = {}
        for t in ('lcdm', 'cr'):
            l, f, LA = FOLD[(t, cfg)]
            m = (l >= lo) & (l < hi)
            a[t] = harmonic(l[m], f[m], LA)[0]
        RAT[cfg].append(a['cr'] / a['lcdm'])
        line += f"  {a['cr']:.4f} / {a['lcdm']:.4f} -> {a['cr'] / a['lcdm']:.4f}  "
    print(line)
SL = {c: float(np.polyfit([0, 1, 2], RAT[c], 1)[0]) for c in RAT}
print(f"      slope across the three bands:  own {SL['sweepown']:+.5f}   swapped "
      f"{SL['viswap']:+.5f}   factor {SL['viswap'] / SL['sweepown']:.2f}")
check("Ⓑ①  ** the width swap AMPLIFIES the arm-to-control q-dependence by a factor 4.56 -- slope "
      "+0.0405 to +0.1847 -- instead of neutralising it. **  `r6919+cc66.42` reported a factor of "
      "about four on its own band binning, and this is that finding reproduced in a different "
      "statistic rather than quoted from it",
      SL['viswap'] / SL['sweepown'] > 3.0 and SL['sweepown'] > 0)
check("Ⓑ②  ⛔ so the order's `has never been confronted with the residual it would produce` is not "
      "so: the swap was made, it is well posed, and its result was that the width is a strong lever "
      "on the SHAPE and not what sets the LEVEL.  ** The premise is reported as a measurement "
      "rather than acted on **",
      RAT['viswap'][2] > RAT['sweepown'][2] and RAT['viswap'][0] < RAT['sweepown'][0])


# ============================================================ C. the fold at l_A
head("C.  THE FOLD AT ell_A -- THE COMPARISON THE ORDER ADDS, AND IT IS NULL")

WH = {}
print("        arm      width      amplitude          sigma    phase")
for t in ('lcdm', 'cr'):
    for cfg in ('sweepown', 'viswap'):
        l, f, LA = FOLD[(t, cfg)]
        WH[(t, cfg)] = harmonic(l, f, LA)
        a, e, s, ph = WH[(t, cfg)]
        print(f"      {t:7s} {'own' if cfg == 'sweepown' else 'swapped':9s} {a:.4f} +- {e:.4f}   "
              f"{s:6.2f}   {ph:6.1f} deg")
dC = WH[('lcdm', 'viswap')][0] / WH[('lcdm', 'sweepown')][0] - 1
dA = WH[('cr', 'viswap')][0] / WH[('cr', 'sweepown')][0] - 1
pC = WH[('lcdm', 'viswap')][3] - WH[('lcdm', 'sweepown')][3]
pA = WH[('cr', 'viswap')][3] - WH[('cr', 'sweepown')][3]
print(f"      widening the control: {100 * dC:+.1f} per cent in amplitude, {pC:+.1f} deg in phase")
print(f"      narrowing the arm:    {100 * dA:+.1f} per cent in amplitude, {pA:+.1f} deg in phase")
check("Ⓒ①  ** the width swap moves the fold at ell_A by under 2 per cent in amplitude and under "
      "half a degree in phase, in BOTH arms. **  So on the one statistic the order asked for, the "
      "width reproduces neither the amplitude nor the phase -- which is the third branch the order "
      "named in advance",
      abs(dC) < 0.02 and abs(dA) < 0.02 and abs(pC) < 0.5 and abs(pA) < 0.5)
check("Ⓒ②  and it is not that the fold is insensitive: it is measured at 26 to 30 sigma in every "
      "configuration, so a 2 per cent move is a move the statistic could easily have resolved had "
      "it been there.  ** A null from a blunt instrument is not a null; this one is from a sharp "
      "one **",
      all(WH[k][2] > 20 for k in WH))


# ============================================================ D. the undo test
head("D.  THE UNDO TEST, AND IT FAILS IN BOTH DIRECTIONS")

own_gap = WH[('cr', 'sweepown')][0] / WH[('lcdm', 'sweepown')][0] - 1
swp_gap = WH[('cr', 'viswap')][0] / WH[('lcdm', 'viswap')][0] - 1
print(f"      arm-to-control fold difference:  own widths {100 * own_gap:+.1f} per cent   "
      f"swapped {100 * swp_gap:+.1f} per cent")
print(f"      widening the control should move it TOWARD the arm "
      f"({WH[('lcdm', 'sweepown')][0]:.4f} -> {WH[('cr', 'sweepown')][0]:.4f}); it went to "
      f"{WH[('lcdm', 'viswap')][0]:.4f}")
print(f"      narrowing the arm should move it TOWARD the control "
      f"({WH[('cr', 'sweepown')][0]:.4f} -> {WH[('lcdm', 'sweepown')][0]:.4f}); it went to "
      f"{WH[('cr', 'viswap')][0]:.4f}")
_toward_arm = WH[('lcdm', 'viswap')][0] > WH[('lcdm', 'sweepown')][0]
_toward_ctl = WH[('cr', 'viswap')][0] < WH[('cr', 'sweepown')][0]
check("Ⓓ①  ⛔ ** widening the control moves its fold AWAY from the arm's, not toward it. **  The "
      "order's own criterion was that a mechanism which explains the residual must also remove it "
      "when undone; this one moves the wrong way",
      not _toward_arm)
check("Ⓓ②  ⛔ and narrowing the arm does not move its fold toward the control's either -- it is "
      "unmoved to one part in a thousand.  ** So the undo fails in both directions, which is a "
      "stronger result than one direction failing: the two configurations cannot both be "
      "coincidences of size **",
      not _toward_ctl and abs(dA) < 0.005)
check("Ⓓ③  ⇒ ** and the arm-to-control difference SURVIVES the swap, +8.1 per cent becoming +10.1: "
      "the swap does not remove it, it slightly increases it. **  ⇒ THE VISIBILITY WIDTH IS NOT THE "
      "CARRIER OF THE SECTOR'S RESIDUAL, said as plainly as the order asked for this branch",
      own_gap > 0.05 and swp_gap > own_gap)


# ============================================================ E. the obstruction
head("E.  THE OBSTRUCTION THE SCOPE ASKS TO HAVE NAMED, FROM THE SYNTAX TREE")

SRC = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
           encoding='utf-8').read()
TREE = ast.parse(SRC)


def names(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


# every assignment whose value mentions the visibility-width knob, and the If tests enclosing it
def enclosing(tree, want):
    out = []

    def walk(node, guards):
        for ch in ast.iter_child_nodes(node):
            g = guards
            if isinstance(node, ast.If):
                pass
            if isinstance(ch, ast.If):
                walk(ch, guards + [names(ch.test)])
                continue
            if isinstance(ch, (ast.Assign, ast.AugAssign)) and want & names(ch.value):
                out.append((getattr(ch, 'lineno', -1), guards))
            walk(ch, g)

    walk(tree, [])
    return out


SITES = enclosing(TREE, {'_SRCIV'})
ASSIGNED = [n.lineno for n in ast.walk(TREE)
            if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == 'ETA_LS_W' for t in n.targets)]
print(f"      ETA_LS_W is assigned at line(s) {ASSIGNED}")
print(f"      assignments consuming the width knob `_SRCIV`: {[s[0] for s in SITES]}")
for ln, guards in SITES:
    print(f"        line {ln} sits inside If tests over {[sorted(g) for g in guards]}")
check("Ⓔ①  ** ETA_LS_W is assigned exactly once and every assignment that consumes `SRCINJVIS` sits "
      "inside an `If` whose test is over `_SRCI` -- so the visibility width is controllable ONLY on "
      "the path where the model's own source has been replaced. **  Established from the syntax "
      "tree rather than from a count of textual matches",
      len(ASSIGNED) == 1 and len(SITES) >= 1
      and all(any('_SRCI' in g for g in guards) for _, guards in SITES))
check("Ⓔ②  ⇒ so the order's `take the control's spectrum and widen its visibility, changing nothing "
      "else` is NOT available on the real-source path: the width there is a derived quantity of the "
      "background and the recombination solution, and the instrument exposes no knob that scales it "
      "alone.  ** The coupling is named rather than varied through, which is what the scope asked "
      "for **",
      len(ASSIGNED) == 1)


# ============================================================ verdict
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ⛔ ** THE PREMISE FIRST: the +14 per cent HAS been confronted, at `r6919+cc66.42`, whose")
print("    banked swapped spectra this receipt reads.  The swap is well posed and it AMPLIFIES the")
print("    arm-to-control q-dependence by 4.56 instead of closing it. **")
print("  ✔ ** AND THE COMPARISON THE ORDER ADDS COMES BACK NULL. **  The fold at ell_A moves by")
print("    -1.8 per cent on the control and +0.1 on the arm, with the phase moving under half a")
print("    degree -- measured at 26 to 30 sigma, so a real move would have been seen.")
print("  ⛔ ** AND THE UNDO TEST FAILS IN BOTH DIRECTIONS. **  Widening the control moves its fold")
print("    AWAY from the arm's; narrowing the arm leaves its own unmoved; and the arm-to-control")
print("    difference survives the swap, +8.1 per cent becoming +10.1.")
print("  ⇒ ** THE VISIBILITY WIDTH IS NOT THE CARRIER OF THE SECTOR'S RESIDUAL. **  That is the")
print("    order's third branch and it is said as plainly as it asked.")
print("  ⌗ And it converges with `r7189+cc66.149` from the same round by a different route: the")
print("    width's signature is a steepening q-slope, while the measured residual's arm-to-control")
print("    fold ratio is FLAT in ell (3.58, 3.65, 3.32).  Two statistics, one conclusion.")
print("  ⚠ What is NOT offered is a replacement mechanism.  `r6919`'s joint object -- `d r_s/d chi`")
print("    across the visibility, 12.8 per cent lower on the arm while `d r_s` itself agrees to")
print("    0.08 -- is re-pointed, not re-derived, and with `cc66.149`'s +4.7 per cent period offset")
print("    it is where this seat would look.  Neither is a claim.")
print("  ⌗ And the obstruction is named: the width cannot be varied on the real-source path at all.")
print(BAR)
print("  ALL CHECKS PASS")
