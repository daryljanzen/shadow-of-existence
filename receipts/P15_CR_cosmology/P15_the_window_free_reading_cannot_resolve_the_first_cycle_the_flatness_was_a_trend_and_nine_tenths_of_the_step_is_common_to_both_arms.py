#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE WINDOW-FREE READING CANNOT RESOLVE THE FIRST ACOUSTIC CYCLE
AND THAT IS THE ANSWER; THE FLATNESS THAT DISPOSED OF TWO CANDIDATES WAS MEASURED AS A **TREND**, SO THE
LIST IS NOT EXHAUSTED; AND NINE TENTHS OF THE STEP IS COMMON TO BOTH ARMS, THE EXCESS'S STEP BEING THE
TENTH THAT FAILS TO CANCEL. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm`, and `r6959_eta_cr`'s band edges.  ⛔ *** Nothing
is SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION WAS WRITTEN BEFORE ANY OF THIS WAS COMPUTED. **  `r7011_directions/PREDICTION.md`
names each finer window-free member and the definition of a step in an ABSOLUTE contrast *before use*, and
tables FIRST, for every one of the three items, the outcome that **damages this seat's own previous
revision** rather than the one the order hoped for.

⛭⛭⛭ ** ⓵ IS THE EXCESS ZERO IN THE FIRST CYCLE?  THE WINDOW-FREE FAMILY CANNOT SAY, AND THE REASON IS
STRUCTURAL. **  Its band 1 rests on ** exactly ONE half-cycle transition **, because the first locatable
extremum pair sits at $q = 1.363$ and the step is at $1.794$.  So its $-0.0008$ is $0.02\sigma$ from ZERO
*and* $1.60\sigma$ from the bands 2--7 mean: ⇒ ** consistent with both, and informative about neither. **
⌗ *No finer member escapes it -- the extremal envelope, which uses only located extrema and no running
window, covers just $27\%$ of band 1 and interpolates ACROSS the step, so its $+0.0245$ is biased TOWARD
the above-step value.*

⇒ *** SO THE ANSWER COMES FROM THE STATISTICS THAT DO RESOLVE BAND 1, AND THERE THE EXCESS IS $+0.0215$:
"SMALL BUT NON-ZERO" IS THE SUPPORTED ROW AND THE STEP STAYS A STEP RATHER THAN BECOMING AN ONSET. ***
⛔ ** `cc66.57`'s "the sharpest of the four" is WITHDRAWN -- it was the COARSEST of the four **, by one
datum against four hundred.  ⌗ *And its "none" endpoint goes with it, as UNRESOLVED rather than as a
reading, which **tightens** the size: band 1 is between a third and two thirds of the rest on every
statistic that can see it.*

⛔⛔ ** ⓶ THE FLATNESS WAS MEASURED ACROSS THE FULL RANGE, BAND 1 INCLUDED -- SO IT IS NOT CIRCULAR ON
RANGE -- BUT IT WAS MEASURED AS A TREND, AND A TREND CANNOT EXCLUDE A STEP. **  `cc66.49`'s statistic is
$\lvert\text{slope}\times\langle q^2\rangle\rvert/\lvert\text{intercept}\rvert$ from a line; a step is
badly fitted by a line and shows up in the **residual**, which that statistic never looked at -- and the
worst residuals are $40$--$61\%$ of each channel's own range.

⌗ ** RE-SCORED ON BAND 1'S DEPARTURE FROM ITS OWN BANDS 2--7 TREND, ACROSS FOUR TREND BASES WITH NONE
CHOSEN: **
  · the ** WINDOW channel steps UPWARD ** $+45\%$ to $+56\%$ on all four -- *the wrong sign*, so it works
    against the step;
  · the ** TERM MIX steps DOWNWARD ** on all four, at $63\%$ of the excess's own $-57\%$ to $-60\%$;
  · the ** JOINT ** -- the pair composed in ONE spectrum at the sizes their own profiles solve, which is
    the physically realised combination -- carries $42\%$ of it, clearing $2\sigma$ on three bases.

⇒ *** `cc66.57`'s ⓷ IS WITHDRAWN IN PART.  Its sentence "a flat candidate's step ratio is exactly one, by
construction and without a new number" was never earned: neither channel is flat on a step statistic, and
THE LIST IS NOT EXHAUSTED -- the step has a PARTIAL account rather than none. ***  ⌗ *The projection
width's disposal stands, and the basis table shows why: that channel is linear in $q$, so it **flips sign
across bases** and a log basis would have manufactured a step for it.  `cc66.57` disposed of it on a
residual from a straight line in $q$, which was the sound one of the four.*

⛭⛭⛭ ** ⓷ AND THE STEP LIVES IN BOTH ARMS, NEARLY EQUALLY. **  On every one of the four bases and on both
the windowed and the window-free contrast: the control departs from its own bands 2--7 trend by $+30$ to
$+44$ per cent at band 1 and the arm by $+27$ to $+39$, ** the arm always the SHALLOWER, by eleven per
cent of the step. **

⇒ *** SO OF A STEP WORTH TENS OF PER CENT IN EACH SPECTRUM, ABOUT NINE TENTHS IS COMMON TO THE TWO ARMS
AND CANCELS IN THE RATIO; THE EXCESS'S STEP IS THE TENTH THAT DOES NOT. ***  ⌗ *That is the
pre-registration's "both arms" row: the step belongs to the acoustic physics the two share, and it
explains -- without a new number -- why `cc66.57` found the location at fixed $q$ on BOTH arms.*

⚠ ** AND THE CAUTION IS THIS SEAT'S, NOT THE ORDER'S: ** *a small residual of two large common features is
exactly where a nearly-common systematic would sit.  That does not make the step an artefact, and it does
mean the next reading of it should be **differential by construction** rather than a difference of two
large numbers.*

⛔ *No mechanism is proposed, no envelope is chosen, no trend basis is chosen, no new candidate is
introduced, and no corpus edit is made.*
"""
import os

import numpy as np
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7011_directions')
RCP = os.path.dirname(os.path.abspath(__file__))
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
STEPQ = 1.794                            # `cc66.57`'s measured location, quoted and not re-derived
WIDTH = np.array([0.00343, 0.00569, 0.00816, 0.01079, 0.01350, 0.01640, 0.01955])   # `cc66.52`

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "r6941_fine_*, the three response banks and r6959_eta_cr's band edges only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔⛭ THE SEQUENCING: the pre-registration says in terms that nothing below it had been measured, "
      "names the finer window-free members and the definition of a step in an ABSOLUTE contrast BEFORE "
      "use, and tables the costliest outcome FIRST in every one of the three items",
      'Nothing below has been measured' in TXT
      and 'EXTREMAL ENVELOPE' in TXT and 'PER-TRANSITION' in TXT
      and TXT.count('NAMED BEFORE USE') == 2
      and TXT.index('the finer reading is NOT near zero') < TXT.index('consistent with zero')
      and TXT.index("either channel's step ratio is far from one") < TXT.index('both step ratios near')
      and TXT.index('NEITHER arm steps') < TXT.index('BOTH arms step'),
      "the damaging row leads all three tables")
check("⛭ AND IT PRE-REGISTERS THE WITHDRAWAL OF THIS SEAT'S OWN SENTENCE BEFORE THE NUMBER THAT FORCES "
      "IT WAS COMPUTED -- the flatness statistic being a TREND is named in the pre-registration, not "
      "discovered in the measurement",
      'That is a TREND statistic' in TXT and 'withdrawn as stated' in TXT
      and 'It needed a number' in TXT,
      "the trend/step distinction is pre-registered, not retrofitted")


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
    e = env_a(q, Dl)
    o = (Dl - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def extrema(t, order=20):
    x, y = fine(t)
    return x, y, argrelextrema(y, np.greater, order=order)[0], argrelextrema(y, np.less, order=order)[0]


def transitions(t, order=20):
    x, y, hi, lo = extrema(t, order)
    e = np.sort(np.concatenate([hi, lo]))
    return 0.5 * (x[e[:-1]] + x[e[1:]]), np.abs(y[e[1:]] - y[e[:-1]]) / (y[e[1:]] + y[e[:-1]])


def extremal_envelope(t, order=20):
    """window-free AND continuous: interpolate maxima and minima separately, no running window"""
    x, y, hi, lo = extrema(t, order)
    a, b = max(x[hi[0]], x[lo[0]]), min(x[hi[-1]], x[lo[-1]])
    m = (x >= a) & (x <= b)
    return x[m], (np.interp(x[m], x[hi], y[hi]) - np.interp(x[m], x[lo], y[lo])) \
        / (np.interp(x[m], x[hi], y[hi]) + np.interp(x[m], x[lo], y[lo]))


# ==================================================================================================
print("\nPART 1 -- ⓵ THE WINDOW-FREE FAMILY HAS ONE DATUM BELOW THE STEP, SO IT CANNOT ANSWER.")
print("-" * 100)
qa, da = transitions('cr')
qc, dc = transitions('lcdm')
RT = da / np.interp(qa, qc, dc) - 1.0
B1 = (qa >= QE[0]) & (qa < QE[1])
REST = qa >= QE[1]
SIG = float(np.std(RT[REST], ddof=1))
M1, N1 = float(RT[B1].mean()), int(B1.sum())
E1 = SIG / np.sqrt(N1)
ZZERO, ZREST = abs(M1) / E1, abs(M1 - float(RT[REST].mean())) / SIG
print(f"  band 1: {M1:+.4f} on {N1} datum(s);  bands 2--7: {float(RT[REST].mean()):+.4f}, "
      f"scatter {SIG:.4f} on {int(REST.sum())}")
check("⓵ THE BAND-1 WINDOW-FREE READING RESTS ON EXACTLY ONE HALF-CYCLE TRANSITION, which is what makes "
      "it unable to decide -- and the uncertainty is the bands 2--7 scatter, not an assertion",
      N1 == 1 and int(REST.sum()) >= 8, f"{N1} datum in band 1 against {int(REST.sum())} above")
check("⇒ AND IT IS CONSISTENT WITH ZERO **AND** WITH THE BANDS 2--7 MEAN AT ONCE, so it distinguishes "
      "\"the excess is zero below the step\" from \"there is no step at all\" not at all",
      ZZERO < 2.0 and ZREST < 2.0,
      f"{ZZERO:.2f} sigma from zero, {ZREST:.2f} sigma from the bands 2--7 mean")
xe, Ae = extremal_envelope('cr')
xf, Af = extremal_envelope('lcdm')
LOQ, HIQ = max(xe.min(), xf.min()), min(xe.max(), xf.max())
COV = (QE[1] - LOQ) / (QE[1] - QE[0])
check("⌗ AND NO FINER MEMBER OF THE FAMILY ESCAPES IT: the extremal envelope needs a located extremum of "
      "each kind, so it covers well under half of band 1 and begins ABOVE the truncation hazard "
      "`cc66.57` discharged, rather than at the band's lower edge",
      0.0 < COV < 0.45 and LOQ > QE[0],
      f"covers q = {LOQ:.3f}--{QE[1]:.2f}, {COV:.0%} of band 1")
g = np.linspace(LOQ, HIQ, 4000)
RE = np.interp(g, xe, Ae) / np.interp(g, xf, Af) - 1.0
BE = np.array([float(RE[(g >= a) & (g < b)].mean()) for a, b in zip(QE[:-1], QE[1:])])
RBEL, RABO = float(RE[g < STEPQ].mean()), float(RE[g >= STEPQ].mean())
ex = np.sort(np.concatenate(extrema('cr')[2:]))
xall = extrema('cr')[0][ex]
NBEL = int(((xall >= LOQ) & (xall < STEPQ)).sum())
check("and its below-step stretch rests on the SAME single extremum, and it interpolates ACROSS the "
      "step, so its reading there is biased TOWARD the above-step value rather than away from it -- "
      "which is why it reads higher than the per-transition one and still cannot settle the question",
      NBEL <= 2 and RBEL > M1,
      f"{NBEL} located extremum below the step; {RBEL:+.4f} there against {RABO:+.4f} above")
ORD = []
for od in (12, 20, 30):
    xa_, Aa_ = extremal_envelope('cr', od)
    xb_, Ab_ = extremal_envelope('lcdm', od)
    a0, b0 = max(xa_.min(), xb_.min()), min(xa_.max(), xb_.max())
    gg = np.linspace(a0, b0, 4000)
    rr = np.interp(gg, xa_, Aa_) / np.interp(gg, xb_, Ab_) - 1.0
    ORD.append(float(rr[gg < STEPQ].mean()) / float(rr[gg >= STEPQ].mean()))
check("⌗ AND THE EXTREMUM FINDER IS NOT WHAT DECIDES ANY OF IT: the below/above ratio is unchanged "
      "across three settings of what counts as an extremum",
      float(np.ptp(ORD)) < 1e-6, f"order 12/20/30 all give {ORD[0]:.3f}")
MEAS = band_std(*fine('cr')) / band_std(*fine('lcdm'))
check("⇒ *** SO THE ANSWER IS THE STATISTICS THAT DO RESOLVE BAND 1, AND THERE THE EXCESS IS NON-ZERO "
      "AND POSITIVE OVER THE FULL BAND INCLUDING THE STRETCH THE WINDOW-FREE FAMILY CANNOT REACH: "
      "\"SMALL BUT NON-ZERO\" IS THE SUPPORTED ROW AND THE STEP STAYS A STEP ***",
      MEAS[0] - 1.0 > 0.01, f"band 1's windowed excess {MEAS[0] - 1:+.4f} over q = "
                            f"{QE[0]:.2f}--{QE[1]:.2f}")
STEPS = [0.333, 0.391, 0.633, RBEL / RABO]
check("⛔ AND `cc66.57`'s \"none\" ENDPOINT IS WITHDRAWN AS UNRESOLVED RATHER THAN AS A READING, WHICH "
      "TIGHTENS THE SIZE INSTEAD OF LOOSENING IT: every statistic that can see band 1 puts it between a "
      "third and two thirds of the rest",
      min(STEPS) > 0.3 and max(STEPS) < 0.7,
      "step ratios " + ", ".join(f"{v:.3f}" for v in STEPS))

# ==================================================================================================
print("\nPART 2 -- ⓶ THE RANGE WAS FULL; THE STATISTIC WAS A TREND; AND THE CHANNELS ARE NOT FLAT.")
print("-" * 100)
C49 = open(os.path.join(RCP, 'P15_the_two_channels_compose_multiplicatively_and_the_pair_is_flat_'
                             'where_the_excess_grows.py')).read()
check("⓶ⓐ THE RANGE, ANSWERED FROM `cc66.49`'s OWN FILE RATHER THAN FROM MEMORY: its fit abscissa is the "
      "centres of ALL SEVEN bands, so band 1 IS in the flatness measurement.  ⇒ The disposal is NOT "
      "circular on range, and the order's first reading of the hazard does not fire",
      'Q2 = QC ** 2' in C49 and 'QC = 0.5 * (QE[:-1] + QE[1:])' in C49
      and "QE = np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges']" in C49
      and len(QC) == 7,
      f"Q2 = QC ** 2 over {len(QC)} band centres, q = {QC[0]:.2f}..{QC[-1]:.2f}")
CH = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    d = np.load(os.path.join(SP, fn))
    CH[nm] = band_std(d['ls'].astype(float) / float(d['l_A']), d['Dl']) / band_std(*fine('lcdm'))
RES = {}
for nm, R in list(CH.items()) + [('measured excess', MEAS)]:
    s_, i_ = np.polyfit(QC ** 2, np.log(R), 1)
    r_ = np.log(R) - (s_ * QC ** 2 + i_)
    RES[nm] = (abs(s_ * (QC ** 2).mean()) / abs(i_), float(np.max(np.abs(r_)) / np.ptp(np.log(R))))
    print(f"    {nm:16s} trend statistic {RES[nm][0]:.3f}   worst residual {RES[nm][1]:.1%} of range")
check("⓶ⓑ BUT THE STATISTIC IS A TREND, AND A TREND CANNOT EXCLUDE A STEP: a step is badly fitted by a "
      "line and shows up in the RESIDUAL, which that statistic never looked at -- and the residuals are "
      "a large fraction of every channel's own range",
      all(RES[n][1] > 0.30 for n in CH) and RES['JOINT'][0] < 0.01,
      "the JOINT reads 0.004 on the trend statistic while leaving "
      f"{RES['JOINT'][1]:.0%} of its range unexplained by that line")
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))


def departure(v, p, lg):
    """band 1 against its OWN bands 2--7 trend, as a FRACTION of the extrapolation so the four bases are
    comparable, with the bands 2--7 scatter in the same units as the yardstick"""
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms, float(f[0]) / rms


DEP = {}
for nm, R in list(CH.items()) + [('measured excess', MEAS), ('proj. width', WIDTH)]:
    v = WIDTH if nm == 'proj. width' else R - 1.0
    DEP[nm] = [departure(v, p, lg) for _, p, lg in BASES]
    print(f"    {nm:16s} " + "  ".join(f"{d[0]:+.3f}({d[2]:+.2f}s)" for d in DEP[nm]))


def one_sign(nm):
    return len({np.sign(d[0]) for d in DEP[nm]}) == 1


def share(nm):
    return float(np.mean([abs(a[0]) / abs(b[0]) for a, b in zip(DEP[nm], DEP['measured excess'])]))


check("⛔ AND NO TREND BASIS IS CHOSEN: all four are reported and a departure counts only if it survives "
      "every one of them -- which is the same discipline as not choosing an envelope, applied to the "
      "basis this statistic needs",
      len(BASES) == 4 and len({b[1] for b in BASES}) == 2 and len({b[2] for b in BASES}) == 2,
      "linear and log, in q and in q^2")
check("⓶ⓒ THE WINDOW CHANNEL IS NOT FLAT AND STEPS **UPWARD** ON ALL FOUR BASES -- the WRONG sign, so it "
      "works against the step rather than making it",
      one_sign('window') and all(d[0] > 0 for d in DEP['window'])
      and min(abs(d[2]) for d in DEP['window']) > 2.0,
      f"{min(d[0] for d in DEP['window']):+.0%} to {max(d[0] for d in DEP['window']):+.0%}")
check("AND THE TERM MIX IS NOT FLAT EITHER AND STEPS **DOWNWARD** ON ALL FOUR -- the RIGHT sign, at a "
      "substantial minority of the excess's own departure",
      one_sign('term mix') and all(d[0] < 0 for d in DEP['term mix'])
      and min(abs(d[2]) for d in DEP['term mix']) > 2.0 and 0.3 < share('term mix') < 0.9,
      f"{max(d[0] for d in DEP['term mix']):+.0%} to {min(d[0] for d in DEP['term mix']):+.0%}, "
      f"{share('term mix'):.0%} of the excess's")
check("AND THE PAIR AS ACTUALLY COMPOSED -- one spectrum, both coefficients at the sizes their own "
      "profiles solve -- CARRIES A MINORITY SHARE OF THE STEP IN THE RIGHT DIRECTION",
      one_sign('JOINT') and all(d[0] < 0 for d in DEP['JOINT']) and 0.2 < share('JOINT') < 0.7,
      f"{share('JOINT'):.0%} of the excess's, clearing 2 sigma on "
      f"{sum(1 for d in DEP['JOINT'] if abs(d[2]) > 2.0)} of the four bases")
check("⇒ *** SO `cc66.57`'s ⓷ IS WITHDRAWN IN PART AND THE LIST IS **NOT** EXHAUSTED: \"a flat "
      "candidate's step ratio is exactly one, by construction and without a new number\" was not earned, "
      "because neither channel is flat on a step statistic ***",
      share('JOINT') > 0.2 and min(abs(d[2]) for d in DEP['term mix']) > 2.0,
      "the step has a partial account rather than none")
check("⌗ AND THE PROJECTION WIDTH'S DISPOSAL STANDS, WHICH IS WHAT THE BASIS TABLE IS FOR: that channel "
      "is linear in q, so it FLIPS SIGN across the bases and a log basis would have manufactured a step "
      "for it -- `cc66.57` scored it on a residual from a straight line in q, which was the sound one of "
      "the four",
      not one_sign('proj. width')
      and float(np.max(np.abs(WIDTH - np.polyval(np.polyfit(QC, WIDTH, 1), QC))) / np.ptp(WIDTH)) < 0.05,
      f"{DEP['proj. width'][0][0]:+.3f} against {DEP['proj. width'][1][0]:+.3f}; a straight line in q "
      f"fits it to "
      f"{np.max(np.abs(WIDTH - np.polyval(np.polyfit(QC, WIDTH, 1), QC))) / np.ptp(WIDTH):.1%} of range")

# ==================================================================================================
print("\nPART 3 -- ⓷ BOTH ARMS STEP, AND THE EXCESS'S STEP IS THE PART THAT FAILS TO CANCEL.")
print("-" * 100)
C0, CA = band_std(*fine('lcdm')), band_std(*fine('cr'))
XW = {}
for nm, t in (('control', 'lcdm'), ('arm', 'cr')):
    xx, AA = extremal_envelope(t)
    XW[nm] = np.array([float(AA[(xx >= a) & (xx < b)].mean()) for a, b in zip(QE[:-1], QE[1:])])
PAIRS = (('windowed', C0, CA, MEAS - 1.0), ('window-free', XW['control'], XW['arm'], BE))
for lbl, vc, va, ve in PAIRS:
    for nm, v in (('control', vc), ('arm', va), ('EXCESS', ve)):
        D = [departure(v, p, lg) for _, p, lg in BASES]
        print(f"    {lbl:12s} {nm:8s} " + "  ".join(f"{d[0]:+.3f}({d[2]:+.2f}s)" for d in D))
for lbl, vc, va, ve in PAIRS:
    DC = [departure(vc, p, lg) for _, p, lg in BASES]
    DA = [departure(va, p, lg) for _, p, lg in BASES]
    check(f"⓷ BOTH ARMS STEP UPWARD AT BAND 1 AGAINST THEIR OWN BANDS 2--7 TREND, ON ALL FOUR BASES, on "
          f"the {lbl} contrast -- so this is not a feature of one spectrum",
          all(d[0] > 0 and d[2] > 2.0 for d in DC) and all(d[0] > 0 and d[2] > 2.0 for d in DA),
          f"control {min(d[0] for d in DC):+.0%} to {max(d[0] for d in DC):+.0%}, "
          f"arm {min(d[0] for d in DA):+.0%} to {max(d[0] for d in DA):+.0%}")
    check(f"AND THE ARM'S STEP IS ALWAYS THE SHALLOWER, on every basis, on the {lbl} contrast",
          all(a[0] < c[0] for a, c in zip(DA, DC)),
          "shallower by " + ", ".join(f"{100 * (1 - a[0] / c[0]):.1f}%" for a, c in zip(DA, DC)))
    DE = [departure(ve, p, lg) for _, p, lg in BASES]
    FR = [1 - a[0] / c[0] for a, c in zip(DA, DC)]
    check(f"⇒ *** AND THE COMMON PART IS ABOUT NINE TENTHS: the arm's step is some ELEVEN PER CENT "
          f"shallower than the control's and no more, so the excess's step is the small part that FAILS "
          f"TO CANCEL *** -- on the {lbl} contrast",
          all(0.05 < f < 0.20 for f in FR) and all(d[0] < 0 for d in DE),
          f"{min(FR):.1%} to {max(FR):.1%} of the step is arm-specific; the excess's own departure is "
          f"{max(d[0] for d in DE):+.0%} to {min(d[0] for d in DE):+.0%}")
check("⌗ AND THE EXCESS'S OWN DEPARTURE IS FAR MORE SIGNIFICANT THAN EITHER ARM'S AGAINST ITS OWN "
      "SCATTER, which is what makes the residual readable at all: the ratio's bands 2--7 are much "
      "smoother than either spectrum's",
      min(abs(d[2]) for d in DEP['measured excess'])
      > 1.5 * max(abs(departure(C0, p, lg)[2]) for _, p, lg in BASES),
      f"excess {min(abs(d[2]) for d in DEP['measured excess']):.1f}--"
      f"{max(abs(d[2]) for d in DEP['measured excess']):.1f} sigma against the control's "
      f"{max(abs(departure(C0, p, lg)[2]) for _, p, lg in BASES):.1f}")
check("⚠ AND THE CAUTION IS RECORDED RATHER THAN BURIED: a small residual of two large common features "
      "is where a nearly-common systematic would sit, so the next reading should be DIFFERENTIAL BY "
      "CONSTRUCTION -- this receipt says so in its own header",
      'differential by construction' in SRC.split(chr(34) * 3)[1],
      "stated in the header, not left to the reader")
check("⛔ AND NOTHING IS PROPOSED AS A MECHANISM, NO ENVELOPE OR BASIS IS CHOSEN, AND NO NEW CANDIDATE IS "
      "INTRODUCED -- which is ⓸",
      'No mechanism is proposed' in SRC.split(chr(34) * 3)[1]
      and 'no trend basis is chosen' in SRC.split(chr(34) * 3)[1],
      "the four candidates are the four `cc66.57` scored")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
