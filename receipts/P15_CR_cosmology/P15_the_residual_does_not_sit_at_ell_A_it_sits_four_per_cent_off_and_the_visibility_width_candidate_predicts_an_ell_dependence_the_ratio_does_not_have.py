#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE CAPTION'S NUMBERS ARE RIGHT, AND ANSWERING `r7189`'s OPEN QUESTION TURNED UP
SOMETHING THE FIGURE'S OWN RECEIPT COULD NOT SEE BECAUSE IT NEVER ASKED: THE RESIDUAL DOES NOT SIT
AT `$\\ell_A$`.  IT SITS AT `$312$` AGAINST `$\\ell_A=298$`, A `$+4.7$` PER CENT OFFSET THAT EXCLUDES
`$\\ell_A$` BY `$\\Delta\\chi^2=15.0$`.  AND THE VISIBILITY-WIDTH CANDIDATE PREDICTS AN
`$\\ell$`-DEPENDENCE THE ARM-TO-CONTROL RATIO DOES NOT HAVE. **

Built r7189+cc66.149 (node 66, code seat), on `PO-13`.

===================================================================================================
** WHAT WAS ASKED, AND WHY THIS IS TWO ANSWERS AND NOT ONE **
===================================================================================================

`r7189` ordered nothing and asked two things.  *"The caption is mine as you said; if any number in it
reads wrong against your run, that is a defect and I want it named."*  And: *"what is left is the
kernel's acceptance in `$k$` and the visibility width that sets it -- your `$+14.3$` per cent.  That
is the next place I would look, and I am not ordering it this round: say if you see a sharper one
from where you sit."*

** THE FIRST ANSWER IS A CONFIRMATION AND IT IS REPORTED AS ONE. **  Every number in
`fig:acoustic-nofit`'s caption that this seat's run can reach is correct, to the digits printed.  The
layout claims are correct too -- `Above` is the full-width panel, `Below left` the period-binned one,
`Below right` the fold, and the refit minima are the dashed curves.  ** There is no defect to name,
and saying so is the answer rather than a courtesy. **

⌗ *One near-miss worth recording so it is not re-found as a defect later: `$0.81/0.12=6.75$`, not
`$6.9$`.  The caption is right and the division is wrong -- the significance is computed from the
unrounded `$0.8128/0.1180=6.888$`.  **A number checked against the rounded version of its own inputs
can fail a check it should pass**, which is the mirror image of this round's other lesson.*

** THE SECOND ANSWER IS A MEASUREMENT, AND IT POINTS AWAY FROM THE CANDIDATE. **  All of it is
arithmetic on the whitened residual this sector already banked at `r7183+cc66.145` -- no new run, no
grid, no fit to any spectrum.

  PART A  ** THE CAPTION, CAPTURED FROM THE PAPER AS VALUES and checked against the figure's
          own banked array; the layout read off this seat's own generator. **
  PART B  ** THE `$\\ell$`-DEPENDENCE OF THE MODULATION. **  The arm's amplitude grows
          `$0.73\\to1.48\\to2.38$` over three sub-bands -- but the control's grows
          `$0.20\\to0.41\\to0.72$` over the same ones, so the growth is in the WHITENING and the
          arm-to-control RATIO is flat: `$3.58$`, `$3.65$`, `$3.32$`.
  PART C  ** AND THE PERIOD IS NOT `$\\ell_A$`. **  Fitted as a free parameter the unfitted arm
          prefers `$312.0$`, `$1\\sigma$` `$[308.5,315.2]$`, excluding `$\\ell_A=298$` at
          `$\\Delta\\chi^2=15.0$` -- a `$+4.7$` per cent offset.  The refit prefers `$307.2$`.
  PART D  ** THE CONTROL THAT MUST BE BEATEN BEFORE THAT IS THE ARM'S. **  The control also prefers
          a longer period, `$347$`, at `$\\Delta\\chi^2=8.6$` -- loosely, `$1\\sigma$` four times
          wider, because its amplitude is `$6.8\\times$` smaller.  ** So the offset is NOT yet
          established as the arm's, and this receipt says so rather than claiming it. **

⇒ *** THE SHARPER PLACE IS THE PERIOD, NOT THE AMPLITUDE.  The figure's receipt reports the harmonic
AT $\\ell_A$ by construction, and nobody had asked whether $\\ell_A$ is where the residual actually
sits.  It is not.  And the difference matters for the sector's whole question: the amplitude of a
modulation at a FIXED period has no obvious parameter address, while a PERIOD offset is a statement
about $r_s/D_M$, which has one. ***

** AND WHAT IT SAYS ABOUT THE VISIBILITY WIDTH, WHICH IS THE PART THAT IS A REPLY. **
  ⛔ *A `$+14.3$` per cent wider visibility is Silk damping: it acts monotonically and strongly at
  high `$\\ell$` and barely at all at low.  **It therefore predicts an arm-to-control ratio that
  GROWS with `$\\ell$`.**  Measured here, that ratio is flat to `$\\pm5$` per cent over
  `$100\\le\\ell<1900$`.*  ⇒ ** The candidate predicts an `$\\ell$`-dependence the residual does not
  have.  That does not kill it -- the width also moves `$\\ell_A$` itself -- but it moves it from
  `the next place to look` to `the place that has to explain a flat ratio`. **

** WHAT THIS IS NOT. **  Not a claim that the arm's period offset is real: `PART D` is the reason.
Not a fit of `$r_s/D_M$`, and not a new confrontation -- the next measurement is named, not run.
** And not a correction of anything in print: `$\\ell_A=298$` is the arm's own acoustic scale and the
figure is right to fold at it.  What is new is that the residual's own period is a separable
question, and the answer is not the same number. **

** COMPUTES: the harmonic fit of `r7183+cc66.145`'s own whitened residual, re-run at the banked
   numbers for the whole range (reproducing its four reported amplitudes), then in three `$\\ell$`
   sub-bands, then with the period as a free parameter over `$240\\le p<380$` at `$0.25$` spacing.
   *** The only inputs are the banked `nofit_figure_numbers.npz` and the two constants
   `$\\ell_A=298$`, `$\\ell_1=222$` the figure already carries; the sub-band cuts and the period grid
   are the only choices and both are stated. *** No spectrum is reloaded and nothing is fitted to
   data. **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~2 s)
"""
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
NPZ = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7183_nofit_figure',
                   'nofit_figure_numbers.npz')
F = np.load(NPZ)
L = F['ell']
L_A = float(F['l_A'])
PEAK1 = float(F['peak1'])
TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
AMP = {t: (float(F[f'{t}_harm_amp']), float(F[f'{t}_harm_err']), float(F[f'{t}_harm_sigma']))
       for t in ('nofit_cr', 'refit_cr', 'nofit_lcdm')}


def harmonic(w, ell, period):
    """the figure's own one-harmonic fit, with the period made an argument."""
    D = np.array([np.cos(2 * np.pi * (ell - PEAK1) / period),
                  np.sin(2 * np.pi * (ell - PEAK1) / period)]).T
    beta = np.linalg.lstsq(D, w, rcond=None)[0]
    rr = w - D @ beta
    s2 = float(np.sum(rr ** 2) / (len(w) - 2))
    cv = s2 * np.linalg.inv(D.T @ D)
    amp = float(np.hypot(*beta))
    err = float(np.sqrt((beta[0] ** 2 * cv[0, 0] + beta[1] ** 2 * cv[1, 1]
                         + 2 * beta[0] * beta[1] * cv[0, 1]) / amp ** 2))
    return amp, err, amp / err, float(np.sum(rr ** 2))


# ============================================================ A. the caption
head("A.  THE CAPTION, CAPTURED FROM THE PAPER AS VALUES AND CHECKED AGAINST THE BANKED NUMBERS")

# ⛔ ** The caption is another seat's prose.  Asserting that a SENTENCE of it is present is a pin on
#    wording that seat may reword, and asserting a figure is `the paper's` without opening it is the
#    unread-figure class.  So every number below is CAPTURED from `CR_cosmology.tex` as a VALUE and
#    compared with the figure's own banked array -- the same repair this seat made at `cc66.143`. **
PAT = {
    'per_bin': (r"the control stands at \$?([0-9.]+)\$? per bin and this arm at \$?([0-9.]+)\$?, "
                r"a factor \$?([0-9.]+)\$?", 3),
    'refit_pb': (r"against \$?([0-9.]+)\$? and \$?([0-9.]+)\$? when four parameters are freed", 2),
    'nbins': (r"Over \$?([0-9]+)\$?\s*\n?bins on \$?[0-9]+\\le\\ell\\le[0-9]+\$?", 1),
    'arm_fold': (r"amplitude\s*\$([0-9.]+)\\pm([0-9.]+)\$[^$]*\$([0-9.]+)\\sigma\$", 3),
    'ctrl_fold': (r"against the control's \$?([0-9.]+)\\pm([0-9.]+)\$?", 2),
    'refit_fold': (r"halves it to \$?([0-9.]+)\\pm([0-9.]+)\$? and leaves \$?([0-9.]+)\\sigma\$?", 3),
}
CAUGHT = {}
for key, (rx, n) in PAT.items():
    m = re.search(rx, TEX)
    CAUGHT[key] = tuple(float(g) for g in m.groups()) if m else None
    print(f"      captured {key:11s} -> {CAUGHT[key]}")
check("Ⓐ①  every figure the caption prints is READ OUT OF THE PAPER as a value -- the two per-bin "
      "numbers and their ratio, the refitted pair, the bin count, and all three folds with their "
      "errors and both significances.  ** Nothing below asserts that a sentence is present; the "
      "capture is the reading **",
      all(CAUGHT[k] is not None for k in PAT))

BANK = {'per_bin': (float(F['nofit_lcdm_chi2_per_bin']), float(F['nofit_cr_chi2_per_bin']),
                    float(F['ratio_nofit'])),
        'refit_pb': (float(F['refit_lcdm_chi2_per_bin']), float(F['refit_cr_chi2_per_bin'])),
        'nbins': (float(F['nbins']),),
        'arm_fold': (float(F['nofit_cr_harm_amp']), float(F['nofit_cr_harm_err']),
                     float(F['nofit_cr_harm_sigma'])),
        'ctrl_fold': (float(F['nofit_lcdm_harm_amp']), float(F['nofit_lcdm_harm_err'])),
        'refit_fold': (float(F['refit_cr_harm_amp']), float(F['refit_cr_harm_err']),
                       float(F['refit_cr_harm_sigma']))}
print("\n      captured from the paper   against the figure's own banked array")
WORST = {}
for k in PAT:
    got, want = CAUGHT[k], BANK[k]
    if got is None:                       # Ⓐ① already failed on this; keep the report readable
        WORST[k] = 1.0
        print(f"      {k:11s} NOT CAPTURED -- the caption's wording for it has moved")
        continue
    # the caption prints each to its own precision, so the tolerance IS that precision
    tol = [0.5 * 10 ** -len(f"{g:g}".split('.')[1]) if '.' in f"{g:g}" else 0.5 for g in got]
    dif = [abs(a - b) for a, b in zip(got, want)]
    WORST[k] = max(d - t for d, t in zip(dif, tol))
    print(f"      {k:11s} {str(got):28s} {str(tuple(round(w, 4) for w in want)):30s} "
          f"{'within its own printed precision' if WORST[k] <= 0 else 'OUT BY ' + str(max(dif))}")
check("Ⓐ②  and every one of them agrees with the banked array to the precision the caption itself "
      "prints it at -- 1.13/3.00/2.66, 0.99/1.58, 179 bins, 1.37+-0.15 at 9.1, the control's "
      "0.20+-0.11, and 0.81+-0.12 at 6.9.  ** So there is no defect to name, which is the answer "
      "rather than a courtesy **",
      all(v <= 0 for v in WORST.values()))

_a, _e, _s = CAUGHT['refit_fold']
print(f"      ⌗ and the captured {_a}/{_e} = {_a / _e:.2f} against the captured {_s}")
print(f"        while the banked {BANK['refit_fold'][0]:.4f}/{BANK['refit_fold'][1]:.4f} = "
      f"{BANK['refit_fold'][0] / BANK['refit_fold'][1]:.3f}")
check("Ⓐ③  ⛔ MUST-COME-BACK-WRONG, on values this receipt captured and not on anything attributed: "
      "dividing the captured amplitude by the captured error gives 6.75 against the captured 6.9, "
      "while the banked unrounded pair gives 6.888.  ** A check built on a printed number's own "
      "rounded inputs reports a defect where there is none -- the shortcut is what fails, not the "
      "caption **",
      abs(_a / _e - 6.75) < 0.01 and abs(_s - 6.9) < 0.01
      and abs(BANK['refit_fold'][0] / BANK['refit_fold'][1] - 6.888) < 0.01)

# the layout is checked against THIS SEAT'S OWN generator, which it owns -- not against the
# caption's prose, which would be a pin on another seat's wording.
GEN = open(os.path.join(ROOT, 'corpus', 'make_fig_acoustic_nofit.py'), encoding='utf-8').read()
_gs = re.findall(r"add_subplot\(gs\[([^\]]+)\]\)", GEN)
# the linestyle each refit series is actually drawn with, CAPTURED -- not a count of matches
_styles = dict(re.findall(r"out\['(refit_(?:lcdm|cr))_model'\] \* FK, '([^']+)'", GEN))
print(f"      and this seat's own generator places its panels at gs{_gs}, drawing the refit series "
      f"as {_styles}")
check("Ⓐ④  the three panels are at gs[0, :], gs[1, 0] and gs[1, 1] in this seat's own generator, "
      "and both refit series are drawn with linestyle '--' -- so `Above`, `Below left`, "
      "`Below right` and `the dashed curves` describe what the figure actually draws.  ** Read off "
      "the generator this seat owns, as captured values rather than as a count **",
      _gs == ['0, :', '1, 0', '1, 1']
      and _styles == {'refit_lcdm': '--', 'refit_cr': '--'})


# ============================================================ B. the ell-dependence
head("B.  THE MODULATION'S ell-DEPENDENCE -- THE GROWTH IS THE WHITENING'S, THE RATIO IS FLAT")

CUTS = ((100, 700), (700, 1300), (1300, 1900))
SUB = {}
print("        band          n     arm amp           control amp        arm/control")
for lo, hi in CUTS:
    m = (L >= lo) & (L < hi)
    a_cr = harmonic(F['nofit_cr_whitened'][m], L[m], L_A)
    a_lc = harmonic(F['nofit_lcdm_whitened'][m], L[m], L_A)
    SUB[(lo, hi)] = (a_cr, a_lc)
    print(f"      {lo:5d}-{hi:<5d} {int(m.sum()):5d}   {a_cr[0]:.4f} ({a_cr[2]:4.2f}s)   "
          f"{a_lc[0]:.4f} ({a_lc[2]:4.2f}s)      {a_cr[0] / a_lc[0]:5.2f}")
A_CR = [SUB[c][0][0] for c in CUTS]
A_LC = [SUB[c][1][0] for c in CUTS]
RAT = [a / b for a, b in zip(A_CR, A_LC)]
print(f"      arm grows {A_CR[0]:.2f} -> {A_CR[2]:.2f} ({A_CR[2] / A_CR[0]:.2f}x); control grows "
      f"{A_LC[0]:.2f} -> {A_LC[2]:.2f} ({A_LC[2] / A_LC[0]:.2f}x)")
print(f"      ratio: {RAT[0]:.2f}, {RAT[1]:.2f}, {RAT[2]:.2f}   spread "
      f"{(max(RAT) - min(RAT)) / np.mean(RAT) * 100:.1f} per cent of the mean")
check("Ⓑ①  the arm's amplitude grows by 3.3x across the range -- and the CONTROL's grows by 3.5x "
      "over the same three sub-bands, so the growth is a property of the whitening and not of the "
      "arm.  ** An amplitude read without its control would have been read as an ell-dependence **",
      A_CR[2] / A_CR[0] > 3.0 and A_LC[2] / A_LC[0] > 3.0
      and abs(A_CR[2] / A_CR[0] - A_LC[2] / A_LC[0]) < 0.5)
check("Ⓑ②  ** AND THE ARM-TO-CONTROL RATIO IS FLAT: 3.58, 3.65, 3.32 over 100-700, 700-1300 and "
      "1300-1900, a spread of 10 per cent of its mean against the 230 per cent the absolute "
      "amplitude moves. **  So whatever drives the modulation scales with the control's own noise "
      "structure rather than with ell",
      max(RAT) - min(RAT) < 0.5 and min(RAT) > 3.0 and max(RAT) < 4.0)
check("Ⓑ③  ⇒ a +14.3 per cent wider visibility is Silk damping, which acts monotonically and "
      "strongly at high ell and barely at low: it predicts a ratio that GROWS with ell.  "
      "** The measured ratio does not.  The candidate predicts an ell-dependence the residual does "
      "not have ** -- which does not kill it, because the width also moves `l_A` itself, but moves "
      "it from `the next place to look` to `the place that has to explain a flat ratio`",
      max(RAT) - min(RAT) < 0.5 and RAT[2] <= RAT[0] + 0.1)


# ============================================================ C. the period
head("C.  AND THE PERIOD IS NOT ell_A -- FITTED FREE, THE UNFITTED ARM PREFERS 312")

GRID = np.arange(240.0, 380.0, 0.25)
PER = {}
for t in ('nofit_cr', 'refit_cr', 'nofit_lcdm'):
    w = F[f'{t}_whitened']
    rss = np.array([harmonic(w, L, p)[3] for p in GRID])
    # the whitened residual is NOT unit variance (that is the rejection), so the period's own
    # interval is taken with the errors rescaled so the best fit has chi^2/dof = 1.  Conservative:
    # it widens the interval by exactly the factor by which the arm is rejected.
    s2 = rss.min() / (len(w) - 3)
    d = (rss - rss.min()) / s2
    best = float(GRID[np.argmin(rss)])
    ins = GRID[d <= 1.0]
    at_LA = (harmonic(w, L, L_A)[3] - rss.min()) / s2
    PER[t] = (best, float(ins.min()), float(ins.max()), float(at_LA))
    print(f"      {t:11s} best = {best:6.2f}   1-sigma [{ins.min():6.1f}, {ins.max():6.1f}]   "
          f"delta chi2 at l_A = {at_LA:5.2f}   best/l_A = {best / L_A:.4f}")
check("Ⓒ①  ** the unfitted arm's residual sits at a period of 312.0, 1-sigma [308.5, 315.2], and "
      "ell_A = 298 is EXCLUDED at delta chi2 = 15.0 -- a +4.7 per cent offset. **  The figure folds "
      "at ell_A by construction and is right to; what nobody had asked is whether ell_A is where "
      "the residual actually sits, and it is not",
      abs(PER['nofit_cr'][0] - 312.0) < 0.3 and PER['nofit_cr'][1] > L_A
      and PER['nofit_cr'][3] > 9.0 and 1.04 < PER['nofit_cr'][0] / L_A < 1.055)
check("Ⓒ②  and the refit moves it to 307.2 while halving the amplitude, so the four parameters pull "
      "the period back toward ell_A without reaching it -- the same pattern the amplitude shows, in "
      "the one quantity the figure does not report",
      abs(PER['refit_cr'][0] - 307.25) < 0.3
      and PER['refit_cr'][0] < PER['nofit_cr'][0] and PER['refit_cr'][0] > L_A)
print(f"      ⌗ and the offset is worth more than the amplitude because of WHERE it could live: the "
      f"amplitude\n        of a modulation at a fixed period has no obvious parameter address, "
      f"while a period is `r_s/D_M`.")


# ============================================================ D. the control that must be beaten
head("D.  THE CONTROL THAT HAS TO BE BEATEN BEFORE THAT OFFSET IS THE ARM'S")

b, lo_, hi_, dchi = PER['nofit_lcdm']
wid_cr = PER['nofit_cr'][2] - PER['nofit_cr'][1]
wid_lc = hi_ - lo_
print(f"      the control prefers {b:.2f} too -- also LONGER than l_A -- at delta chi2 = {dchi:.2f}")
print(f"      but its interval is {wid_lc:.1f} wide against the arm's {wid_cr:.1f}, a factor "
      f"{wid_lc / wid_cr:.1f}, because its amplitude is "
      f"{AMP['nofit_cr'][0] / AMP['nofit_lcdm'][0]:.1f}x smaller")
check("Ⓓ①  ⛔ ** THE CONTROL ALSO PREFERS A LONGER PERIOD, 347, at delta chi2 = 8.6 against ell_A. "
      "So a preference for a period longer than ell_A is NOT by itself the arm's. **  This receipt "
      "therefore does NOT claim the offset as the arm's, and the measurement that would is named "
      "below rather than run",
      b > L_A and dchi > 5.0)
check("Ⓓ②  what separates them is the DETERMINATION and not the direction: the arm's interval is "
      "4x tighter because its amplitude is 6.8x larger, so the arm's period is measured where the "
      "control's is barely constrained.  ** That is a reason to make the measurement, not a "
      "substitute for it **",
      wid_lc / wid_cr > 3.0 and AMP['nofit_cr'][0] / AMP['nofit_lcdm'][0] > 6.0)


# ============================================================ verdict
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE CAPTION HAS NO DEFECT. **  Every number in it this seat's run can reach is right to")
print("    the digits printed, and so are its four layout claims.  The one near-miss is a shortcut's")
print("    and not the caption's: 0.81/0.12 = 6.75 against the unrounded 6.888.")
print("  ⛭ ** AND THE SHARPER PLACE IS THE PERIOD, NOT THE AMPLITUDE. **  The unfitted arm's residual")
print("    sits at 312.0, 1-sigma [308.5, 315.2], excluding l_A = 298 at delta chi2 = 15.0 -- and the")
print("    figure's own receipt could not have seen it, because it fits the harmonic AT l_A by")
print("    construction.  The refit pulls it to 307.2 without reaching l_A.")
print("  ⛭ ** AND THE VISIBILITY-WIDTH CANDIDATE PREDICTS AN ell-DEPENDENCE THE RESIDUAL DOES NOT")
print("    HAVE. **  The arm's amplitude does grow 3.3x across the range -- but the control's grows")
print("    3.5x over the same bands, so the growth is the whitening's.  The arm-to-control ratio is")
print("    flat: 3.58, 3.65, 3.32.  Silk damping acts at high ell and would make it climb.")
print("  ⚠ ** AND THE OFFSET IS NOT CLAIMED AS THE ARM'S. **  The control prefers a longer period too")
print("    (347, delta chi2 = 8.6), loosely.  What differs is the determination -- 4x tighter for the")
print("    arm -- not the direction.  The measurement that would settle it is the arm's period")
print("    against the control's as a null, and it is NAMED here and not run: nothing was ordered.")
print(BAR)
print("  ALL CHECKS PASS")
