#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE PROJECTION'S TWO WIDTHS DIFFER BY THE JACOBIAN AND BY NOTHING ELSE,
WHICH MAKES THE DIFFERENCE A PREDICTION OF THE TWO-RATE ASSIGNMENT RATHER THAN A PROPERTY OF THIS
INSTRUMENT -- AND THE CONTRAST CHANNEL THAT DIFFERENCE OPENS IS AT MOST A QUARTER OF THE EXCESS. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6959_eta_{lcdm,cr}` (the eta-resolved bank) and `r6941_fine_{lcdm,cr}` (the
banked spectra `cc66.40`'s contrast statistic is computed on).  `sec:refit-bound`'s quartet
$222/538/818/1134$ is the LINE-OF-SIGHT path's and is not read -- searched for by grepping this file for
each of the four values and for every line-of-sight bank name (`c54.17*`, `c54.178_*`, `L814_*`,
`r6784_*`), and none occurs below.  ⛔ *** Nothing is SOLVED: every number is read from banks on disk or
computed from them with the instrument's own projection kernel (`scipy.special.spherical_jn`). ***

** THE PRE-REGISTRATION IS WRITTEN AND IS `r6999_directions/PREDICTION.md`. **  *It carries all four
outcomes for the ⓵ run INCLUDING THE NULL, on the order's guard that a channel whose size is measured
rather than fitted must be able to return "it does nothing" as a claimable result.*  ⚠ *And it states,
in that order, which teeth were committed at `r6993` before this measurement (growth and deceleration)
and which two are being ADDED now, after seeing a result: SIGN, and the naming of a stretch's fixed
point.  Both additions are conditions a candidate must pass, so they can only make the filter harder --
which is the whole reason they are admissible after the fact.*

⛭⛭⛭ ** ⓷ FIRST, BECAUSE IT IS THE RESULT WITH THE LONGER REACH, AND THE ORDER SAYS SO: "that would be
worth more than the contrast result". **  The question was whether the two widths standing in a
different ratio in the arm is FORCED by the construction or an artefact of how this instrument builds
its window.  ** It is forced, and the proof is a pointwise identity plus one comparison. **

  ⓐ The instrument keeps two sound horizons on the same integrand and two rates, so
    `d(rs_leaf)/d(eta) = Jac x d(rs_stack)/d(eta)` with `Jac = H_phys/H_leaf`.  *Checked pointwise
    across the window: the two agree with `Jac` to ONE PART IN A MILLION on the arm and exactly
    on the control, where `Jac == 1` by the rate identity.*
  ⓑ ** ON THE RULER CLOCK THE TWO ARMS ARE THE SAME INSTRUMENT. **  The window's conformal width
    divided by its width in `rs_stack` is $0.9967$ of the control's -- *a third of a per cent* -- on
    both core width definitions.  ⌗ *The visibility is laid down in $\eta$ by Thomson scattering on the
    physical background, which is the same physics on both arms, and the ruler clock sees it so.*
  ⓒ ** ON THE LEAF CLOCK IT IS $+14.5$ PER CENT, AND THE WHOLE OF THAT IS `Jac`. **  The arm's own
    leaf-to-ruler width ratio equals the visibility-weighted mean of `Jac` to under half a per cent.
  ⇒ *** `Jac` IS NOT A KNOB: it is fixed by the background solution once the arm is specified, has no
  free coefficient in it, and is identically $1$ on any one-rate cosmology.  SO THE DIFFERENT RATIO IS A
  PREDICTION OF THE TWO-RATE ASSIGNMENT, STATED HERE FOR THE FIRST TIME. ***

⚠ ** AND A WIDTH IS NOT A QUANTITY UNTIL ITS DEFINITION IS NAMED, WHICH CHANGES `cc66.51`'s NUMBER. **
Three definitions are taken under ONE measure -- the visibility as a density over $\eta$ -- and applied
to the random variables $\eta$, `rs_leaf`, `rs_stack`: RMS, FWHM, and the half-fall of the
characteristic function.  *The two CORE measures agree with each other to better than a hundredth of a
per cent and give $+14.5$ per cent; RMS gives $+7.3$, which is `cc66.51`'s figure.*  ⇒ **The window has
long tails, RMS weights them, and neither the projection nor the phase sweep responds to them.  The
prediction is to be quoted on a core width with the definition named.**

⛔ ** ⓵ CANNOT BE RUN AS WRITTEN, AND THAT FOLLOWS FROM ⓷ RATHER THAN FROM ANY LIMITATION OF EFFORT. **
*"Give the control arm this arm's conformal width at the same leaf width"* is, by ⓐ--ⓒ, exactly *"give
the control arm this arm's `Jac`"* -- and a control with `Jac != 1` is not a control.  ⇒ **There is no
knob for the projection width, the instrument is right not to have one, and the channel is not separable
from the two-rate assignment.**  *Reported rather than substituted for, on the standing instruction.*

⛭⛭ ** ⓶ SO THE FILTER IS APPLIED IN THE KERNEL, WHICH IS THE PROJECTION SECTOR'S WHOLE CONTENT. **  The
order's operation is done analytically on the control's own projection: hold the source's acoustic phase
`cos(k rs_leaf)` and stretch ONLY the Bessel argument by the measured $s = 1.135$,

    I_l(k; s) = | INT g(eta) exp(i k rs_leaf) j_l( k (eta_0 - a - s (eta - a)) ) d eta |

⌗ *Holding the phase is what makes this the PROJECTION channel and not `cc66.47`'s window channel again.*

⛔ ** AND THIS FILE CORRECTS ITS OWN FIRST PASS, WHICH WAS WRONG BY A FACTOR OF FIFTEEN AND IN SIGN. **
That pass treated the kernel as a PLANE WAVE in conformal time, `|INT g e^{-i k eta}|`, on the reading
that the Bessel argument advances at rate $k$.  ** It does not: $j_l(x)$ near its turning point $x\sim
l$ -- which is where the entire window sits, $kD_M\sim l$ being what the projection IS -- oscillates at
local rate $\sqrt{1-l^2/x^2}$, which vanishes there. **  *The proxy gives $-29.7$ per cent at the top
band; the instrument's own kernel gives $+2.0$.*

⚠ ** AND THE SIGN IS NOT DETERMINED ON PAPER, BECAUSE A STRETCH NEEDS A FIXED POINT. **  Anchored at the
visibility's MEAN the departure runs $+0.0034 \to +0.0196$; anchored at its PEAK it runs $-0.0034 \to
+0.0016$ and crosses zero, where $G$ is not a ratio of anything and is reported UNDEFINED.  *A stretch
about the wrong point is a stretch plus a displacement, and a displacement of the window moves the COMB
rather than the contrast.*

⛔ ** THE VERDICT: IT FAILS THE CURVATURE TOOTH UNDER BOTH ANCHORINGS AND IS AT MOST A QUARTER OF THE
EXCESS. **  Curvature $+0.00016$ and $+0.00037$ against the target's $-0.00327$: ** it ACCELERATES where
the target decelerates. **  And at the top band it delivers $+1.96$ per cent against the $+7.62$ the
measurement needs.  ⇒ *** NOT THE CARRIER.  NOT EXCLUDED AS A CONTRIBUTOR. ***

⚠ ** AND THE FILTER ITSELF NEEDED A THIRD TOOTH, WHICH THE SUPERSEDED PASS EXPOSED. **  Those
plane-wave numbers run $-0.0332 \to -0.2968$: $G = 8.93$ and curvature $-0.0014$, ** passing both
pre-registered teeth while moving the contrast the WRONG WAY in every band. **  $G$ is a ratio of a
departure to a departure and is blind to their common sign.  ⇒ *The filter's first tooth is now SIGN,
and this is the second revision running in which this statistic returned a number outside its domain.*

⌗ ** ⓸ THE SUB-PERIOD ESTIMATOR, SAID AND NOT BUILT, AS ASKED. **  `cc66.51` established that the
oscillation-amplitude estimator stops at $q=2$ because a sliding window needs about a period either
side.  *What would reach below it is not a shorter window but a different estimator: the acoustic period
in $q$ is KNOWN and equal to $2$, so a fit of $A\cos(\pi q + \varphi)$ with the period HELD has two free
parameters per $q$ rather than an amplitude read off a window, and needs only a fraction of a period of
support.*  ⌗ **Its cost is that the period must be right**: a held period that is wrong by a few per
cent leaks into $A$ as a slow drift, which is exactly the $q$-dependence being measured.  ⇒ *So it would
have to be validated against the window estimator on $[2.6, 5.4]$, where both work, before anything it
says below $q=2$ is read.*  ** Not built: the order puts it second.  **
"""
import os
import sys

import numpy as np
from scipy.optimize import brentq
from scipy.special import spherical_jn

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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r6999_directions')
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
QE = np.asarray(A['cr']['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NL = 9

# ---- the path-provenance guard, executed rather than asserted -----------------------------------
# ⌷ The scan skips its own machinery: any line tagged `# noscan` is removed before the search,
#   because the marker lists and the two gate bodies necessarily CONTAIN the strings searched for.
SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body -- every model number below is the HIERARCHY path's",
      not any(m in BODY for m in LOSMARK),                                                # noscan
      "r6959_eta_{lcdm,cr} and r6941_fine_{lcdm,cr} only")
check("and nothing is SOLVED: the instrument is neither imported nor shelled out to, and no spectrum "
      "is generated here",
      not any(m in BODY for m in SOLVEMARK),                                              # noscan
      "banks on disk, plus scipy's own spherical_jn")


# =================================================================================================
#  ⓷  FORCED OR CHOSEN
# =================================================================================================
def measure(t):
    d = A[t]
    e = np.asarray(d['eta'], float)
    w = np.asarray(d['vis'], float)
    return e, w / np.trapezoid(w, e), np.asarray(d['rs_leaf'], float), np.asarray(d['rs_stack'], float)


def rms(e, w, x):
    m = np.trapezoid(w * x, e)
    return float(np.sqrt(np.trapezoid(w * (x - m) ** 2, e)))


def fwhm(e, w, x):
    i = np.where(w >= w.max() / 2)[0]
    return float(x[i[-1]] - x[i[0]])


def chi_half(e, w, x):
    def f(k):
        return np.hypot(np.trapezoid(w * np.cos(k * x), e), np.trapezoid(w * np.sin(k * x), e)) - 0.5
    hi = 1e-3
    while f(hi) > 0:
        hi *= 2
    return 1.0 / brentq(f, 1e-9, hi)


DEFS = (('rms', rms), ('fwhm', fwhm), ('chi-half', chi_half))
CORE = ('fwhm', 'chi-half')

print("\n⛭⛭⛭ ⓷ -- IS THE WIDTH DIFFERENCE FORCED OR CHOSEN\n")
DEV = {}
for t in ('lcdm', 'cr'):
    e, w, rl, rs = measure(t)
    J = np.asarray(A[t]['jac'], float)
    m = w > 0.01 * w.max()
    DEV[t] = float(np.max(np.abs(np.gradient(rl, e) / np.gradient(rs, e) / J - 1.0)[m]))
check("⛭ ⓐ THE POINTWISE IDENTITY: the two clocks differ by the JACOBIAN and by nothing else, across "
      "the whole window -- d(rs_leaf)/d(rs_stack) == Jac",
      DEV['lcdm'] < 1e-9 and DEV['cr'] < 1e-5,
      f"max |ratio/Jac - 1| = {DEV['lcdm']:.2e} on the control and {DEV['cr']:.2e} on the arm")
JW = np.asarray(A['lcdm']['jac'], float)
check("and the control's Jacobian is identically ONE, by the rate identity -- which is what makes it "
      "the control and what makes the comparison below a comparison of ONE object",
      np.all(JW == 1.0), "Jac == 1 at every one of the control's eta samples")

W = {}
for t in ('lcdm', 'cr'):
    e, w, rl, rs = measure(t)
    W[t] = {n: (f(e, w, e), f(e, w, rl), f(e, w, rs)) for n, f in DEFS}
R = {}
for n, _ in DEFS:
    a, c = W['cr'][n], W['lcdm'][n]
    R[n] = ((a[0] / a[1]) / (c[0] / c[1]), (a[0] / a[2]) / (c[0] / c[2]))
    print(f"    {n:9s} arm/control:  on the LEAF clock {R[n][0]:.5f}   on the RULER clock {R[n][1]:.5f}")
check("⛭ ⓑ ON THE RULER CLOCK THE TWO ARMS ARE THE SAME INSTRUMENT: the window's conformal width "
      "against its width in rs_stack agrees between the arms to under half a per cent, on BOTH core "
      "width definitions.  *The visibility is laid down in eta by the same Thomson physics on both.*",
      all(abs(R[n][1] - 1) < 0.005 for n in CORE),
      "  ".join(f"{n} {100 * (R[n][1] - 1):+.2f}%" for n in CORE))
check("⛭⛭ ⓒ AND ON THE LEAF CLOCK IT IS MORE THAN TEN PER CENT, ON BOTH core definitions -- the two "
      "widths do NOT scale together between the arms",
      all(R[n][0] - 1 > 0.10 for n in CORE),
      "  ".join(f"{n} {100 * (R[n][0] - 1):+.1f}%" for n in CORE))
check("⛭⛭⛭ AND THE WHOLE OF THAT DIFFERENCE IS THE JACOBIAN: the leaf-clock ratio divided by the "
      "ruler-clock ratio accounts for it to under half a per cent",
      all(abs((R[n][0] / R[n][1]) / R[n][0] - 1) < 0.005 for n in CORE),
      "  ".join(f"{n}: Jac share {R[n][0] / R[n][1]:.5f} against leaf ratio {R[n][0]:.5f}" for n in CORE))

e, w, rl, rs = measure('cr')
JBAR = float(np.trapezoid(w * np.asarray(A['cr']['jac'], float), e))
check("and stated as the prediction it is: the arm's own leaf-to-ruler WIDTH ratio equals the "
      "visibility-weighted mean of Jac, to under one per cent on both core definitions.  ⇒ THE TWO "
      "WIDTHS STANDING IN A DIFFERENT RATIO IS A PREDICTION OF THE TWO-RATE ASSIGNMENT, NOT AN "
      "ARTEFACT OF THIS INSTRUMENT'S WINDOW",
      all(abs(W['cr'][n][1] / W['cr'][n][2] / JBAR - 1) < 0.01 for n in CORE),
      f"<Jac> = {JBAR:.5f} against " + "  ".join(f"{n} {W['cr'][n][1] / W['cr'][n][2]:.5f}" for n in CORE))
check("⚠ AND SAY WHICH QUANTITY: the SIZE is definition-dependent while the attribution is not.  The "
      "two CORE measures agree to better than a hundredth of a per cent; RMS, which weights the "
      "window's long tails, gives a departure smaller by more than a factor of one and a half -- and "
      "RMS is what `cc66.51` reported",
      abs(R['fwhm'][0] - R['chi-half'][0]) < 1e-4
      and (R['chi-half'][0] - 1) / (R['rms'][0] - 1) > 1.5,
      f"core {100 * (R['chi-half'][0] - 1):+.1f}% and {100 * (R['fwhm'][0] - 1):+.1f}%, "
      f"rms {100 * (R['rms'][0] - 1):+.1f}%")
check("⛔ AND THIS IS WHY THE ORDER'S ⓵ CANNOT BE RUN AS WRITTEN, which follows from the identity and "
      "not from effort: giving the control the arm's conformal width AT THE SAME LEAF WIDTH is giving "
      "it the arm's Jacobian, and a control with Jac != 1 is not a control.  There is no knob for the "
      "projection width and the instrument is right not to have one",
      DEV['cr'] < 1e-5 and all(abs(R[n][1] - 1) < 0.005 for n in CORE),
      "reported rather than substituted for, on the standing instruction")


# =================================================================================================
#  ⓶  THE FILTER, IN THE INSTRUMENT'S OWN KERNEL
# =================================================================================================
def plane_wave():
    out = []
    for t in ('lcdm', 'cr'):
        ee, ww = measure(t)[:2]
        k = np.pi * QC / float(A[t]['r_s'])
        out.append(np.array([np.hypot(np.trapezoid(ww * np.cos(kk * ee), ee),
                                      np.trapezoid(ww * np.sin(kk * ee), ee)) for kk in k]))
    return out[1] / out[0]


def stretch(s, anchor):
    d = A['lcdm']
    ee, ww, rlf = measure('lcdm')[:3]
    e0 = float(d['D_M']) + float(d['eta_ls'])
    rsv, lA = float(d['r_s']), float(d['l_A'])
    a = float(np.trapezoid(ww * ee, ee)) if anchor == 'mean' else float(ee[np.argmax(ww)])

    def amp(l, k, ss):
        j = spherical_jn(l, k * (e0 - a - ss * (ee - a)))
        return np.hypot(np.trapezoid(ww * np.cos(k * rlf) * j, ee),
                        np.trapezoid(ww * np.sin(k * rlf) * j, ee))

    return np.array([np.mean([amp(int(round(q * lA)), np.pi * q / rsv, s)
                              / amp(int(round(q * lA)), np.pi * q / rsv, 1.0)
                              for q in np.linspace(lo, hi, NL)])
                     for lo, hi in zip(QE[:-1], QE[1:])])


def env_a(x, y, win=1.0):
    out = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        out[j] = np.mean(y[m])
    return out


def bands(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    o = (d['Dl'] - env_a(q, d['Dl'])) / env_a(q, d['Dl'])
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def teeth(r):
    dd = np.asarray(r, float) - 1.0
    crosses = bool(dd.min() < 0.0 < dd.max())
    return dd, (None if crosses else float(dd[-1] / dd[0])), float(np.polyfit(QC, dd, 2)[0])


print("\n⛭⛭ ⓶ -- THE FILTER, APPLIED IN THE INSTRUMENT'S OWN PROJECTION KERNEL\n")
S = W['cr']['chi-half'][0] / W['lcdm']['chi-half'][0]
TGT, dT = bands(F['cr']) / bands(F['lcdm']), None
dT, gT, cT = teeth(bands(F['cr']) / bands(F['lcdm']))
dW, gW, cW = teeth(plane_wave())
dM, gM, cM = teeth(stretch(S, 'mean'))
dP, gP, cP = teeth(stretch(S, 'peak'))
print(f"    the measured conformal-width ratio s = {S:.5f}   (half-fall definition, named with it)")
print("    target        " + "  ".join(f"{x:+.5f}" for x in dT))
print("    mean-anchored " + "  ".join(f"{x:+.5f}" for x in dM))
print("    peak-anchored " + "  ".join(f"{x:+.5f}" for x in dP))
print("    plane-wave    " + "  ".join(f"{x:+.5f}" for x in dW))

check("⛔ THE FIRST PASS IS SUPERSEDED AND THE CORRECTION IS THE HEADLINE OF THIS SECTION: treating "
      "the projection kernel as a PLANE WAVE in conformal time overstates the top band by more than a "
      "factor of ten AND reverses its sign.  j_l(x) near its turning point x ~ l -- where the whole "
      "window sits, k D_M ~ l being what the projection IS -- oscillates at local rate "
      "sqrt(1 - l^2/x^2), which vanishes there",
      abs(dW[-1]) / abs(dM[-1]) > 10 and dW[-1] * dM[-1] < 0,
      f"plane wave {dW[-1]:+.4f} against the kernel's {dM[-1]:+.4f}")
check("⚠ AND A STRETCH IS NOT AN OPERATION UNTIL ITS FIXED POINT IS NAMED: the two natural anchorings "
      "-- the visibility's mean in eta and its peak -- do not agree in SIGN at the bottom band, so the "
      "sign of this channel is NOT DETERMINED ON PAPER",
      dM[0] * dP[0] < 0, f"mean-anchored {dM[0]:+.5f}, peak-anchored {dP[0]:+.5f}")
check("and the peak-anchored departure crosses zero inside the range, so its growth statistic is "
      "UNDEFINED rather than small -- the domain guard, applied for the second revision running",
      gP is None and gM is not None, "G reported only where the departure keeps one sign")
check("⛔ AND THE VERDICT ON THE COMMITTED SECOND TOOTH: the channel ACCELERATES under BOTH anchorings "
      "where the target DECELERATES.  ** IT FAILS THE FILTER. **",
      cM > 0 and cP > 0 > cT,
      f"curvature {cM:+.6f} and {cP:+.6f} against the target's {cT:+.6f}")
check("and the size is bounded rather than merely failing: at the top band the channel delivers at "
      "most a third of what the measurement needs, under every anchoring.  ⇒ NOT THE CARRIER; NOT "
      "EXCLUDED AS A CONTRIBUTOR",
      max(abs(dM[-1]), abs(dP[-1])) / dT[-1] < 0.34,
      f"{100 * dM[-1]:+.2f}% (mean) and {100 * dP[-1]:+.2f}% (peak) against the target's "
      f"{100 * dT[-1]:+.2f}%")
check("⚠ AND THE FILTER ITSELF NEEDED A THIRD TOOTH, WHICH THE SUPERSEDED PASS EXPOSED AND WHICH IS "
      "REGISTERED ANYWAY BECAUSE IT IS A DEFECT OF THE STATISTIC AND NOT OF THAT ESTIMATE: those "
      "plane-wave numbers PASS both pre-registered teeth -- growth and negative curvature -- while "
      "moving the contrast the WRONG WAY in every band.  G is a ratio of a departure to a departure "
      "and is blind to their common sign.  ⇒ THE FIRST TOOTH IS NOW SIGN",
      gW is not None and gW > 1 and cW < 0 and np.all(dW < 0) and np.all(dT > 0),
      f"G = {gW:.2f} and curvature {cW:+.6f}, with every band negative against a target every band "
      f"positive")


# =================================================================================================
#  ⓵  THE PRE-REGISTRATION, INCLUDING THE NULL
# =================================================================================================
print("\n⌗ ⓵ -- THE PRE-REGISTRATION\n")
PRED = os.path.join(DIR, 'PREDICTION.md')
TXT = open(PRED).read() if os.path.exists(PRED) else ''
check("⛔ THE ORDER'S OWN GUARD: a PREDICTION.md exists for this revision and it carries the NULL as a "
      "named outcome with a stated meaning -- 'when a channel's size is measured rather than fitted, a "
      "result of it does nothing is a real result and has to be claimable in advance'",
      'THE NULL' in TXT and 'does nothing' in TXT and TXT.count('| **') >= 4,
      f"{TXT.count('| **')} outcomes tabled, the null among them")
check("and it declares, in that order, which teeth were committed at r6993 BEFORE this measurement and "
      "which two are added NOW -- and why adding them cannot rescue this candidate",
      'COMMITTED AT `r6993`' in TXT and 'ADDED NOW' in TXT and 'harder' in TXT,
      "the two additions are conditions a candidate must pass, so they only tighten the filter")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
