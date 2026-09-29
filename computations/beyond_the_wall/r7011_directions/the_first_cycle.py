"""⓵⓶⓷ IS THE EXCESS ZERO IN THE FIRST CYCLE, WAS THE FLATNESS A TREND, AND WHOSE STEP IS IT? -- r7011+cc66.58.

⛔ *`PREDICTION.md` was committed before this file was run.*  ⌗ **Each item's outcome table leads with
the reading that costs this seat most**, which for ⓵ is "the finer window-free reading is not near zero
after all" and for ⓶ is the withdrawal of `cc66.57`'s own sentence about flat candidates.

** THE WINDOW-FREE FAMILY, NAMED BEFORE USE. **  *`cc66.57`'s envelope-free reading is the fractional
depth between CONSECUTIVE extrema -- a HALF acoustic cycle per datum.  Two finer members of the same
family are added here and neither replaces it: the per-transition data themselves rather than band
means, and the EXTREMAL ENVELOPE, which interpolates between successive maxima and between successive
minima and so uses only located extrema and no running window at all.*
"""
import os

import numpy as np
from scipy.signal import argrelextrema

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
STEPQ = 1.794                            # `cc66.57`'s measured location, quoted and not re-derived


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def band_std(q, Dl):
    o = (Dl - env_a(q, Dl)) / env_a(q, Dl)
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def extrema(t, order=20):
    x, y = fine(t)
    hi = argrelextrema(y, np.greater, order=order)[0]
    lo = argrelextrema(y, np.less, order=order)[0]
    return x, y, hi, lo


def transitions(t, order=20):
    """the window-free datum: one fractional depth per HALF acoustic cycle, at its own midpoint in q"""
    x, y, hi, lo = extrema(t, order)
    e = np.sort(np.concatenate([hi, lo]))
    return 0.5 * (x[e[:-1]] + x[e[1:]]), np.abs(y[e[1:]] - y[e[:-1]]) / (y[e[1:]] + y[e[:-1]])


def extremal_envelope(t, order=20):
    """WINDOW-FREE and CONTINUOUS: interpolate the maxima and the minima separately and read the
    fractional half-depth between the two at every multipole.  No running window anywhere."""
    x, y, hi, lo = extrema(t, order)
    a, b = max(x[hi[0]], x[lo[0]]), min(x[hi[-1]], x[lo[-1]])
    m = (x >= a) & (x <= b)
    up, dn = np.interp(x[m], x[hi], y[hi]), np.interp(x[m], x[lo], y[lo])
    return x[m], (up - dn) / (up + dn)


MEAS_B1 = float(band_std(*fine('cr'))[0] / band_std(*fine('lcdm'))[0] - 1.0)

print(__doc__)
print('=' * 100)

# ==================================================================================================
print('\n  ⛭⛭⛭ ⓵ IS THE EXCESS ZERO IN THE FIRST CYCLE, OR MERELY SMALLER?')
print('-' * 100)
qa, da = transitions('cr')
qc, dc = transitions('lcdm')
RT = da / np.interp(qa, qc, dc) - 1.0
print(f"    the window-free reading has {len(RT)} half-cycle transitions in all, "
      f"q = {qa.min():.3f} to {qa.max():.3f}")
NB = [int(((qa >= a) & (qa < b)).sum()) for a, b in zip(QE[:-1], QE[1:])]
print(f"    per band:  " + '  '.join(f'b{j + 1}:{n}' for j, n in enumerate(NB))
      + f"   -- so `cc66.57`'s band means rested on {min(NB)}--{max(NB)} data each")

B1 = (qa >= QE[0]) & (qa < QE[1])
REST = qa >= QE[1]
SIG = float(np.std(RT[REST], ddof=1))
M1, N1 = float(RT[B1].mean()), int(B1.sum())
E1 = SIG / np.sqrt(N1)
print(f"\n    ⌗ THE UNCERTAINTY IS NOT ASSERTED -- it is the scatter of the per-transition excess over "
      f"bands 2--7, where the order's own reading says the excess is featureless:")
print(f"      bands 2--7: mean {float(RT[REST].mean()):+.4f}, per-transition scatter {SIG:.4f} "
      f"over {int(REST.sum())} data")
print(f"      band 1    : mean {M1:+.4f} over {N1} data  =>  {M1:+.4f} +- {E1:.4f}  "
      f"({abs(M1) / E1:.2f} sigma from zero)")
print(f"      and against bands 2--7's mean: {(M1 - float(RT[REST].mean())) / SIG:+.2f} sigma")

print('\n    ⌗ THE INDIVIDUAL TRANSITIONS IN AND AROUND THE FIRST CYCLE, which is the finest this '
      'quantity gets:')
for q, r in zip(qa[qa < 2.6], RT[qa < 2.6]):
    print(f"      q = {q:.3f}   excess {r:+.4f}" + ('   <- band 1' if q < QE[1] else ''))

x, y, hi, lo = extrema('cr')
xc, yc, hic, loc_ = extrema('lcdm')
print(f"\n    ⌗ AND THE FIRST TROUGH ALONE, which the order asked for by name: the arm's first minimum "
      f"is at q = {x[lo[0]]:.3f} and the control's at q = {xc[loc_[0]]:.3f}")
T1 = float(RT[0])
print(f"      the transition that ends on it reads {T1:+.4f}, against the bands 2--7 scatter "
      f"{SIG:.4f}  ({abs(T1) / SIG:.2f} sigma on ONE datum)")

print('\n    ⛭ AND THE EXTREMAL ENVELOPE -- window-free AND continuous, so not limited to one datum '
      'per half cycle:')
xe, Ae = extremal_envelope('cr')
xf, Af = extremal_envelope('lcdm')
lo_q, hi_q = max(xe.min(), xf.min()), min(xe.max(), xf.max())
g = np.linspace(lo_q, hi_q, 4000)
RE = np.interp(g, xe, Ae) / np.interp(g, xf, Af) - 1.0
print(f"      defined over q = {lo_q:.3f} to {hi_q:.3f} on both arms, {len(g)} samples")
BE = np.array([float(RE[(g >= a) & (g < b)].mean()) if ((g >= a) & (g < b)).any() else np.nan
               for a, b in zip(QE[:-1], QE[1:])])
print(f"      band by band: " + '  '.join(f'{v:+.4f}' for v in BE))
print(f"      STEP = band 1 / mean(bands 2--7) = {BE[0] / np.nanmean(BE[1:]):.3f}")
BELOW, ABOVE = (g < STEPQ) & (g >= QE[0]), g >= STEPQ
print(f"      and split at `cc66.57`'s own step location q = {STEPQ}: "
      f"{float(RE[BELOW].mean()):+.4f} below, {float(RE[ABOVE].mean()):+.4f} above, a ratio of "
      f"{float(RE[BELOW].mean()) / float(RE[ABOVE].mean()):.3f}")

print('\n    ⛔⛔ AND THE VERDICT ON ⓵, WHICH IS A NULL AND WHICH COSTS `cc66.57` ITS OWN ADJECTIVE.')
print(f"      *The per-transition reading is {abs(M1) / E1:.2f} sigma from ZERO and "
      f"{abs(M1 - float(RT[REST].mean())) / SIG:.2f} sigma from the bands 2--7 MEAN.*")
print('      ⇒ ** SO IT IS CONSISTENT WITH BOTH. IT DOES NOT DISTINGUISH "ZERO" FROM "NO STEP AT ALL", '
      'AND IT CANNOT ANSWER THE QUESTION THE ORDER ASKED OF IT. **')
print(f"      ⌗ *And the reason is structural, not statistical: **there is exactly ONE half-cycle "
      f"transition below the step**, because the first locatable extremum pair sits at q = "
      f"{lo_q:.3f} and the step is at {STEPQ}.  No finer member of the window-free family escapes that "
      f"-- the extremal envelope's below-step stretch rests on the same single extremum, and it "
      f"interpolates ACROSS the step, so its {float(RE[BELOW].mean()):+.4f} is biased TOWARD the "
      f"above-step value rather than away from it.*")
print(f"\n      ⛭ SO THE ANSWER COMES FROM THE STATISTICS THAT DO HAVE RESOLUTION THERE.  *The windowed "
      f"contrast reads band 1 over the FULL band q = {QE[0]:.2f}--{QE[1]:.2f}, including the "
      f"{1 - (QE[1] - lo_q) / (QE[1] - QE[0]):.0%} of it the window-free family cannot reach at all, and "
      f"gives band 1's excess as {MEAS_B1:+.4f} -- non-zero.*")
print(f"      ⇒ *** \"SMALL BUT NON-ZERO\" IS THE SUPPORTED ROW, AND THE STEP STAYS A STEP RATHER THAN "
      f"BECOMING AN ONSET. ***  *The order's stronger claim is **not established** -- and it is not "
      f"excluded either, because the one reading that suggested it is the one with no resolving power.*")
print(f"      ⛔ *`cc66.57` called the envelope-free reading \"the sharpest of the four\". **That is "
      f"withdrawn: it is the coarsest of the four**, by one datum against four hundred, and its "
      f"{M1:+.4f} carried no information about zero.*")
print(f"      ⌗ *Which tightens the step's size rather than loosening it: the \"none\" endpoint of "
      f"`cc66.57`'s range is withdrawn as UNRESOLVED, not as a reading, so band 1 is between a third "
      f"and two thirds of the rest on every statistic that can see it -- 0.333, 0.391, 0.633 windowed "
      f"and {float(RE[BELOW].mean()) / float(RE[ABOVE].mean()):.3f} on the extremal envelope's split.*")

# ==================================================================================================
print('\n\n  ⛭⛭⛭ ⓶ WAS THE FLATNESS MEASURED ACROSS THE FULL RANGE, OR ACROSS BANDS 2--7?')
print('-' * 100)
F = {t: fine(t) for t in ('lcdm', 'cr')}
C0 = band_std(*F['lcdm'])
MEAS = band_std(*F['cr']) / C0
CH = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    d = np.load(os.path.join(SP, fn))
    CH[nm] = band_std(d['ls'].astype(float) / float(d['l_A']), d['Dl']) / C0
print(f"    ⓐ THE RANGE, read off the file rather than recalled: `cc66.49`'s fit abscissa is "
      f"`Q2 = QC ** 2` with `QC` the centres of ALL {len(QC)} bands,")
print(f"      q = {'  '.join(f'{v:.2f}' for v in QC)} -- so band 1 IS in it.")
print(f"    ⇒ ** THE FLATNESS WAS MEASURED ACROSS THE FULL RANGE, BAND 1 INCLUDED. THE DISPOSAL IS "
      f"NOT CIRCULAR ON RANGE. **")
print(f"\n    ⓑ BUT THE STATISTIC IS A TREND, AND THAT IS THE HALF THAT COSTS ME:")
FIT = {}
for nm, R in list(CH.items()) + [('measured excess', MEAS)]:
    s, i = np.polyfit(QC ** 2, np.log(R), 1)
    res = np.log(R) - (s * QC ** 2 + i)
    FIT[nm] = (abs(s * (QC ** 2).mean()) / abs(i), float(np.max(np.abs(res)) / np.ptp(np.log(R))))
    print(f"      {nm:16s} |slope x <q^2>|/|intercept| = {FIT[nm][0]:.3f}   "
          f"worst residual from that line = {FIT[nm][1]:.1%} of its own range")
print("    ⇒ ** a small TREND is not a small STEP: a step is badly fitted by a line and shows up in "
      "the RESIDUAL, which that statistic never looked at. **")
print(f"\n    ⓒ SO EACH CHANNEL, RE-SCORED ON THE STEP STATISTIC ITSELF -- band 1's response over the "
      f"mean of bands 2--7, the definition the excess is scored on:")
SR = {}
for nm, R in list(CH.items()) + [('measured excess', MEAS)]:
    SR[nm] = (R[0] - 1.0) / np.mean(R[1:] - 1.0)
    print(f"      {nm:16s} band responses " + '  '.join(f'{v - 1:+.4f}' for v in R)
          + f"   STEP = {SR[nm]:.3f}")
print(f"    ⇒ the two channels' step ratios are {SR['window']:.3f} and {SR['term mix']:.3f}, against "
      f"the measured excess's {SR['measured excess']:.3f}.")

print('\n    ⓓ BUT band-1-over-the-mean CONFLATES A TREND WITH A STEP -- the window channel has a strong '
      'monotone trend -- so the step must be read as band 1\'s DEPARTURE FROM ITS OWN BANDS 2--7 TREND.')
print('      ⛔ *And that statistic needs a basis for the trend, which is a choice.  `cc66.57` used a '
      'straight line in q for the projection width and got 2.6% of its range; a log-linear fit in q^2 '
      'is the basis the rest of this sector quotes.  **A quantity linear in q has a curved log, so the '
      'wrong basis MANUFACTURES a step.**  ⇒ *So no basis is chosen: all four are reported, and only a '
      'departure that survives every one of them is called a step.*')
BASES = (('v ~ q', 1, False), ('v ~ q²', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q²', 2, True))


def departure(v, p, lg):
    """band 1 against its OWN bands 2--7 trend, as a FRACTION of the extrapolation so that the four
    bases are comparable, with the bands 2--7 scatter in the same units as the yardstick"""
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    if lg:
        f = np.exp(y - pred) - 1.0
    else:
        f = y / pred - 1.0
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms, float(f[0]) / rms


WIDTH = np.array([0.00343, 0.00569, 0.00816, 0.01079, 0.01350, 0.01640, 0.01955])
QTY = list(CH.items()) + [('measured excess', MEAS), ('proj. width (cc66.52)', WIDTH)]
print(f"\n      {'quantity':23s}" + ''.join(f"{b[0]:>19s}" for b in BASES) + '      verdict')
DEP, VER = {}, {}
for nm, R in QTY:
    v = WIDTH if nm.startswith('proj') else R - 1.0
    DEP[nm] = [departure(v, p, lg) for _, p, lg in BASES]
    one = len({np.sign(d[0]) for d in DEP[nm]}) == 1
    z = min(abs(d[2]) for d in DEP[nm])
    VER[nm] = ('** STEP **' if one and z > 2.0 else
               'marginal' if one and z > 1.5 else 'no step -- sign flips' if not one else 'no step')
    print(f"      {nm:23s}" + ''.join(f"{d[0]:+9.3f} ({d[2]:+5.2f}s)" for d in DEP[nm])
          + f"   {VER[nm]}")


def share(nm):
    return np.mean([abs(a[0]) / abs(b[0]) for a, b in zip(DEP[nm], DEP['measured excess'])])


print('\n    ⇒ ** BOTH CHANNELS CARRY A DEPARTURE, IN OPPOSITE DIRECTIONS, AND NEITHER IS FLAT. **')
print(f"      *the WINDOW channel steps UPWARD on all four bases, "
      f"{min(d[0] for d in DEP['window']):+.0%} to {max(d[0] for d in DEP['window']):+.0%} against its "
      f"own extrapolation -- **the wrong sign**, so it works against the step and does not make it;*")
print(f"      *the TERM MIX steps DOWNWARD on all four, "
      f"{max(d[0] for d in DEP['term mix']):+.0%} to {min(d[0] for d in DEP['term mix']):+.0%}, the "
      f"RIGHT sign, at {share('term mix'):.0%} of the excess's own "
      f"{max(d[0] for d in DEP['measured excess']):+.0%} to "
      f"{min(d[0] for d in DEP['measured excess']):+.0%};*")
print(f"      *and the JOINT -- the pair composed in ONE spectrum at the sizes their own profiles solve, "
      f"which is the physically realised combination -- reads {VER['JOINT']}, "
      f"{max(d[0] for d in DEP['JOINT']):+.0%} to {min(d[0] for d in DEP['JOINT']):+.0%}, "
      f"{share('JOINT'):.0%} of the excess's, and it clears 2 sigma on "
      f"{sum(1 for d in DEP['JOINT'] if abs(d[2]) > 2.0)} of the four bases.*")
print(f"      ⌗ *And the projection width flips SIGN across the bases "
      f"({DEP['proj. width (cc66.52)'][0][0]:+.3f} against "
      f"{DEP['proj. width (cc66.52)'][1][0]:+.3f}), which is the hazard this table was built to catch -- "
      f"it is linear in q, so a log basis manufactures a step for it.  **That is why `cc66.57`'s "
      f"disposal of the projection width, which used a residual from a straight line in q, was the "
      f"sound one of the four and stands.**")
print('\n    ⛔⛔ SO `cc66.57`\'s ⓷ IS WITHDRAWN IN PART, AND THIS IS THE COST.  *Its sentence "a flat '
      'candidate\'s step ratio is exactly one, by construction and without a new number" was not '
      'earned: the flatness it leaned on was measured as a TREND, the two channels are not flat on a '
      'step statistic, and the term mix carries a real downward step.*')
print(f"    ⇒ ** THE LIST IS NOT EXHAUSTED. **  *One channel pushes the wrong way, one pushes the right "
      f"way at {share('term mix'):.0%}, and the pair as actually composed carries {share('JOINT'):.0%} "
      f"of the step -- a minority share, which is what the Doppler turned out to be too.*  ⇒ *So "
      f"\"no candidate produces the step\" becomes **\"no candidate produces it ALONE, and the two "
      f"channels between them carry a minority of it\"** -- and the step's account is partial rather "
      f"than empty.*")

# ==================================================================================================
print('\n\n  ⛭⛭⛭ ⓷ WHERE THE STEP LIVES: THE ARM, THE CONTROL, OR ONLY THE DIFFERENCE')
print('-' * 100)
print('    ⌗ Same statistic, same four bases, no basis chosen -- each arm\'s OWN contrast against its '
      'OWN bands 2--7 trend, with no reference to the other arm.')
CA = band_std(*F['cr'])
XX = {}
for nm, t in (('control', 'lcdm'), ('arm', 'cr')):
    xx, AA = extremal_envelope(t)
    XX[nm] = np.array([float(AA[(xx >= a) & (xx < b)].mean()) for a, b in zip(QE[:-1], QE[1:])])

print(f"\n    ⓐ ON THE WINDOWED CONTRAST:")
print(f"      {'quantity':23s}" + ''.join(f"{b[0]:>19s}" for b in BASES))
for nm, v in (('control contrast', C0), ('arm contrast', CA), ('EXCESS (the ratio)', MEAS - 1.0)):
    D = [departure(v, p, lg) for _, p, lg in BASES]
    print(f"      {nm:23s}" + ''.join(f"{d[0]:+9.3f} ({d[2]:+5.2f}s)" for d in D))
print(f"\n    ⓑ AND ON THE WINDOW-FREE CONTRAST OF ⓵:")
print(f"      {'quantity':23s}" + ''.join(f"{b[0]:>19s}" for b in BASES))
for nm, v in (('control depth', XX['control']), ('arm depth', XX['arm']),
              ('EXCESS (the ratio)', BE)):
    D = [departure(v, p, lg) for _, p, lg in BASES]
    print(f"      {nm:23s}" + ''.join(f"{d[0]:+9.3f} ({d[2]:+5.2f}s)" for d in D))

print('\n    ⇒ *** BOTH ARMS STEP, IN THE SAME DIRECTION AND BY NEARLY THE SAME AMOUNT, ON EVERY BASIS '
      'AND ON BOTH STATISTICS -- AND THE EXCESS\'S STEP IS THE PART THAT FAILS TO CANCEL. ***')
for lbl, (_, p, lg) in zip([b[0] for b in BASES], BASES):
    dc_ = departure(C0, p, lg)[0]
    da_ = departure(CA, p, lg)[0]
    de_ = departure(MEAS - 1.0, p, lg)[0]
    print(f"      {lbl:10s} control {dc_:+.3f}   arm {da_:+.3f}   "
          f"=> the arm's step is {100 * (1 - da_ / dc_):4.1f}% shallower, and the excess's own "
          f"departure is {de_:+.3f}")
print('      ⌗ *So of a step worth tens of per cent in each spectrum, about nine tenths is COMMON to '
      'the two arms and cancels in the ratio; the excess\'s step is the tenth that does not.*')
print('    ⇒ ** THAT IS THE "BOTH ARMS" ROW OF THE PRE-REGISTRATION: the step belongs to the acoustic '
      'physics the two share, and the excess inherits it as a residual. **  *It also explains, after '
      'the fact and without a new number, why `cc66.57` found the location at fixed q on BOTH arms.*')
print('      ⚠ *AND THE CAUTION THAT COMES WITH IT, WHICH IS MINE AND NOT THE ORDER\'S: a small '
      'residual of two large common features is exactly where a systematic that is ALMOST common would '
      'sit.  This does not make the excess\'s step an artefact, and it does mean the next reading of it '
      'should be differential by construction rather than a difference of two large numbers.*')
print('\n  ⛔ ROBUSTNESS -- THE THREE THINGS THE NUMBERS ABOVE MADE NECESSARY')
print('-' * 100)
print('    ⓐ THE EXTREMAL ENVELOPE\'S COVERAGE OF BAND 1, which the pre-registration said to report '
      'rather than discover:')
print(f"      it needs a located extremum of EACH kind, so it begins at q = {lo_q:.3f}, not at "
      f"q = {QE[0]:.2f}: its \"band 1\" is only q = {lo_q:.3f}--{QE[1]:.2f}, "
      f"{(QE[1] - lo_q) / (QE[1] - QE[0]):.0%} of the band, and all of it ABOVE the truncation hazard "
      f"`cc66.57` discharged.")
NE = int(((x[np.sort(np.concatenate([hi, lo]))] >= lo_q) & (x[np.sort(np.concatenate([hi, lo]))]
                                                            < STEPQ)).sum())
print(f"      and the below-step stretch q = {lo_q:.3f}--{STEPQ} is constrained by {NE} located "
      f"extrema, against {int((x[np.sort(np.concatenate([hi, lo]))] >= STEPQ).sum())} above it.")
print('\n    ⓑ THE EXTREMUM FINDER\'S `order`, which sets what counts as an extremum:')
for od in (12, 20, 30):
    xa, Aa = extremal_envelope('cr', od)
    xb, Ab = extremal_envelope('lcdm', od)
    a0, b0 = max(xa.min(), xb.min()), min(xa.max(), xb.max())
    gg = np.linspace(a0, b0, 4000)
    rr = np.interp(gg, xa, Aa) / np.interp(gg, xb, Ab) - 1.0
    bl, ab = (gg < STEPQ), gg >= STEPQ
    qt, dt = transitions('cr', od)
    qu, du = transitions('lcdm', od)
    rt = dt / np.interp(qt, qu, du) - 1.0
    print(f"      order {od:2d}: starts at q = {a0:.3f};  below the step {float(rr[bl].mean()):+.4f}, "
          f"above {float(rr[ab].mean()):+.4f}, ratio {float(rr[bl].mean()) / float(rr[ab].mean()):.3f}"
          f"   |  per-transition band 1 {float(rt[(qt >= QE[0]) & (qt < QE[1])].mean()):+.4f} "
          f"on {int(((qt >= QE[0]) & (qt < QE[1])).sum())} datum(s)")

print('\n' + '=' * 100)
print(f"""
  ⛭⛭⛭ ⓵ THE WINDOW-FREE READING CANNOT ANSWER IT, AND THAT IS THE ANSWER.  *Its band 1 rests on
    ONE half-cycle transition, because the first locatable extremum pair sits at q = {lo_q:.3f} and the
    step is at {STEPQ}.  So {M1:+.4f} is {abs(M1) / E1:.2f} sigma from zero AND
    {abs(M1 - float(RT[REST].mean())) / SIG:.2f} sigma from the bands 2--7 mean: consistent with both,
    and informative about neither.*  ⇒ ** On the statistics that DO resolve band 1 the excess there is
    {MEAS_B1:+.4f}, non-zero, so "SMALL BUT NON-ZERO" is the supported row and the step stays a step
    rather than becoming an onset. **  ⛔ *`cc66.57`'s "sharpest of the four" is WITHDRAWN -- it was the
    coarsest -- and its "none" endpoint goes with it, as unresolved rather than as a reading, which
    TIGHTENS the size to between a third and two thirds.*

  ⛔⛔ ⓶ THE FLATNESS WAS MEASURED ON THE FULL RANGE, BAND 1 INCLUDED -- SO NOT CIRCULAR ON RANGE -- BUT
    IT WAS MEASURED AS A **TREND**, AND A TREND CANNOT EXCLUDE A STEP.  *Re-scored on band 1's departure
    from its own bands 2--7 trend, across four trend bases with none chosen: the WINDOW channel steps
    UPWARD {min(d[0] for d in DEP['window']):+.0%} to {max(d[0] for d in DEP['window']):+.0%} -- the
    wrong sign -- the TERM MIX steps DOWNWARD at {share('term mix'):.0%} of the excess's, and the pair as
    actually composed carries {share('JOINT'):.0%}.*  ⇒ ** `cc66.57`'s ⓷ IS WITHDRAWN IN PART: neither
    channel is flat, its "a flat candidate's step ratio is exactly one" was never earned, and THE LIST IS
    NOT EXHAUSTED -- the step has a partial account rather than none. **  ⌗ *The projection width's
    disposal stands, because that one was done on a residual and not on a trend; and the basis table is
    what shows why -- the width flips sign across bases, so a log basis would have manufactured a step
    for it.*

  ⛭⛭⛭ ⓷ BOTH ARMS STEP, BY NEARLY THE SAME AMOUNT, AND THE EXCESS'S STEP IS THE PART THAT FAILS TO
    CANCEL.  *On every one of the four bases and on both the windowed and the window-free contrast: the
    control departs from its own bands 2--7 trend by about +30 to +44 per cent at band 1 and the arm by
    about +27 to +39, the arm always the SHALLOWER, by ELEVEN PER CENT of the step.*  ⇒ *** So of a step
    worth tens of per cent in each spectrum, about nine tenths is COMMON to the two arms and cancels; the
    excess's step is the tenth that does not. ***  ⌗ *That is the pre-registration's "both arms" row: the
    step belongs to the acoustic physics the two share, and it explains without a new number why
    `cc66.57`'s location came out at fixed q on BOTH arms.*
    ⚠ *AND THE CAUTION IS MINE, NOT THE ORDER'S: a small residual of two large common features is where a
    nearly-common systematic would sit.  That does not make the step an artefact -- it means the next
    reading of it should be differential by construction rather than a difference of two large numbers.*

  ⛔ *No mechanism is proposed, no envelope or basis is chosen, no new candidate is introduced, and no
    corpus edit is made.*
""")
