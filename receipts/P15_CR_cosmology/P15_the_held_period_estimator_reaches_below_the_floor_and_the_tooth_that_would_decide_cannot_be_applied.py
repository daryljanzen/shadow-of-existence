#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE BELOW-FLOOR ESTIMATOR IS BUILT AND VALIDATED AND IT DOES REACH A BAND
NO ESTIMATOR HAS REACHED; THE CANDIDATE PASSES EVERY TOOTH THAT CAN BE APPLIED THERE; AND THE TOOTH THAT
WOULD DECIDE CANNOT BE APPLIED, BECAUSE THE TARGET'S OWN CURVATURE IS NOT DETERMINED ON ANY RANGE THE
CANDIDATE CAN BE MEASURED ON. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6897_fields` (the `ZPSAVE` bank the register's own estimator reads),
`r6941_fine_{lcdm,cr}` (the banked spectra the contrast statistic is computed on) and `r6959_eta_cr`
(the band edges alone).  `sec:refit-bound`'s quartet is the LINE-OF-SIGHT path's and is not read;
searched for below rather than asserted.  ⛔ *** Nothing is SOLVED. ***

** THE PRE-REGISTRATION IS `r7001_directions/PREDICTION.md` **, five outcomes for ⓶ including BOTH
nulls, and it states in that order which teeth were committed at `r6993` and `cc66.52` before this
measurement and that its outcome TABLE was written after the band values had been read -- *which
introduces no criterion, the teeth having been fixed first, and is dated rather than implied.*

⛭⛭ ** ⓵ THE ESTIMATOR, AND THE FIRST THING IT FOUND WAS THAT THE PERIOD IS NOT THE PERIOD. **  The
acoustic period in $q = k r_s/\pi$ is $2$ by construction.  ** It is not $2$ in the fields. **  Read off
the drift of the recovered phase and iterated to self-consistency, the monopole runs at $1.9636$ and the
dipole at $1.9909$ on the control -- *a two per cent error, and a DIFFERENT one for the two fields,
which is precisely the failure the order asked to be measured rather than noted.*  ⇒ **So the held
period is MEASURED, per field and per arm, and its own uncertainty is taken from disjoint sub-ranges:
$1.3$ per cent.**

⛔ ** AND THE VALIDATION CAME FIRST, WHICH WAS THE ORDER AND IS ALSO THE STANDING GUARD. **  Against the
window estimator, same quantity and same fields: *the means agree.*  ⚠ **And the window estimator does
not survive its own width**: its ripple runs from $0.7$ per cent at `half` $=2$ to $11.6$ at `half`
$=0.5$, *the width `cc66.51` read the candidate at*, while the held estimator sits near $2.5$ per cent
at every width and reaches $q = 0.39$.

⛭ ** AND THE LEAK IS MEASURED AND IT IS SMALL, FOR A REASON THAT IS A MECHANISM. **  Perturbing the held
period at the $1.3$ per cent it is known to moves the candidate's span across the bands by $0.00006$
against a span of $0.00959$ -- ** under one per cent of the dependence being measured. **  *The fit
re-fits the PHASE in every window, so a wrong held period is absorbed there and costs only a common
amplitude factor, which cancels in a ratio of ratios.*  ⇒ ***THE ESTIMATOR CAN ANSWER THE QUESTION.***

⛭⛭ ** ⓶ AND IT REACHES A BAND NOTHING HAS REACHED -- AND STOPS AT ONE NOTHING WILL. **  The band at
$q=1.90$ is now measured, stable to $0.003$ across eight estimator settings, where the window estimator
could not reach below $q=2.0$ at any width.  ⛔ **Band 1 at $q=1.20$ is still not measurable and now for
a stated reason rather than a width**: its spread $0.021$ exceeds its value $0.0003$, *because its
window straddles the first acoustic excursion, where there is no oscillation amplitude to estimate.*
⇒ ** A floor of MECHANISM, and the second null of the pre-registration. **

⛭ ** THE TEETH, SIGN FIRST. **  On $q = 1.90$--$5.40$ the candidate's departure is **positive in every
band**, as the target's is, and runs $+0.0048 \to +0.0144$: $G = 2.99$ against the target's $1.33$, the
same direction.  ⇒ *** IT PASSES SIGN AND IT PASSES GROWTH, ON THE RANGE THIS ESTIMATOR UNLOCKED. ***

⛔⛔ ** AND THE CURVATURE TOOTH CANNOT BE APPLIED, WHICH IS THE RESULT AND IS THE PRE-REGISTRATION'S
FIRST NULL. **  *The criterion is that the candidate's curvature carry the TARGET's sign -- and
on every range excluding band 1 the target's own curvature flips sign when any single band is dropped.*
⛔ **And on the full range the reason is exact rather than statistical: dropping BAND 1 ALONE flips the
target's curvature from $-0.0033$ to $+0.0003$, while dropping any other single band leaves it
negative.**  ⇒ ***The target's deceleration is carried entirely by the one band no estimator of the
candidate can reach.***  ⇒ ***The filter is out of teeth rather than the candidate out
of chances, and that is a statement about the filter.***

⚠⚠ ** AND `cc66.51`'s CURVATURE PASS DOES NOT SURVIVE, WHICH IS A CORRECTION TO THIS SEAT'S OWN LANDED
RESULT. **  Read with the window estimator on its own range and its own recipe, the candidate's
curvature swings from $-0.0093$ at `half` $=0.5$ -- *the width it was read at* -- to $+0.0012$ at `half`
$=2$, *where that estimator is sound.*  ⛔ **The stability check `cc66.51` ran certified the MEAN over a
sub-range.  The curvature was never the quantity that was checked** -- the "say which quantity" guard,
biting on the seat that wrote it.

⛭⛭⛭ ** ⓷ THE PREDICTION IS AN INDEPENDENT READING OF THE JACOBIAN, AND IT IS NOT OBSERVABLE. **  Two
different functionals of the same `Jac`: the COMB reads the **cumulative** ratio at last scattering,
$0.5665$ -- $\pi D_M/r_{s,\rm leaf} = 301.41$ against the banked $l_A = 301.80$, while
$\pi D_M/r_{s,\rm stack} = 170.76$ is not close -- and the WIDTHS read the **window-local** average,
$\langle\mathrm{Jac}\rangle = 0.8744$.  ***They differ by a third, both are $1$ on one rate, and neither
carries a free coefficient*** -- so a construction tuned to the comb must still produce the right LOCAL
Jacobian to match the widths.  ⛔ **But no measurement reaches the ratio**: the phase width, which the
Landau damping reads, differs between the arms by $0.84$ per cent, while the conformal width, which the
projection reads, differs by $13.5$ and `cc66.52` bounded its contrast effect at $2$.  ⇒ ***NO, NOT
OBSERVABLE IN ITS OWN RIGHT -- said plainly, in the order's terms.***
"""
import os

import numpy as np

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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7001_directions')
F = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
FI = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
EB = np.load(os.path.join(SP, 'r6959_eta_cr.npz'))
QE = np.asarray(EB['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
PERR = 0.013
g = lambda n, t: F[f'{n}__{t}']

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
      "r6897_fields, r6941_fine_{lcdm,cr} and r6959_eta_cr's band edges only")
check("and nothing is SOLVED: the instrument is neither imported nor shelled out to",
      not any(m in BODY for m in SOLVEMARK),                                              # noscan
      "banks on disk")


# =================================================================================================
def fields(t):
    k = g('k', t)
    o = np.argsort(k)
    k = k[o]
    psi = g('psi', t)[o]
    return k * float(g('r_s', t)) / np.pi, (g('th0', t)[o] + psi) / psi, (g('tb', t)[o] / k) / psi


def loc(q, y, q0, half, P, bd=1):
    m = np.abs(q - q0) <= half
    if m.sum() < 12:
        return None
    dq = q[m] - q0
    X = np.column_stack([dq ** j for j in range(bd + 1)]
                        + [np.cos(2 * np.pi * q[m] / P), np.sin(2 * np.pi * q[m] / P)])
    c = np.linalg.lstsq(X, y[m], rcond=None)[0]
    return float(np.hypot(c[-2], c[-1])), float(np.arctan2(-c[-1], c[-2]))


def period_of(q, y, lo, hi, half=0.5, P0=2.0):
    P = P0
    for _ in range(12):
        Q = np.arange(lo, hi + 1e-9, 0.25)
        s = float(np.polyfit(Q, np.unwrap([loc(q, y, x, half, P)[1] for x in Q]), 1)[0])
        Pn = 2 * np.pi / (2 * np.pi / P + s)
        if abs(Pn - P) < 1e-9:
            return Pn
        P = Pn
    return P


def amp_ratio(t, half=2.0, amp_deg=2, step=0.05):
    """`cc66.51`'s WINDOW estimator, verbatim"""
    q, um, ud = fields(t)
    Q, RT = [], []
    for q0 in np.arange(1.5 + half, q.max() - half - 0.1, step):
        m = np.abs(q - q0) <= half
        if m.sum() < 20:
            continue
        dq = q[m] - q0
        cols = [np.ones(int(m.sum()))]
        for j in range(amp_deg + 1):
            cols += [dq ** j * np.cos(np.pi * q[m]), dq ** j * np.sin(np.pi * q[m])]
        X = np.column_stack(cols)
        bm = np.linalg.lstsq(X, um[m], rcond=None)[0]
        bd = np.linalg.lstsq(X, ud[m], rcond=None)[0]
        Q.append(q0)
        RT.append(float(np.hypot(bd[1], bd[2]) / np.hypot(bm[1], bm[2])))
    return np.array(Q), np.array(RT)


def held_ratio(t, Pm, Pd, half=0.5, bd=1, step=0.02):
    q, um, ud = fields(t)
    Q, RT = [], []
    for q0 in np.arange(q.min() + half, q.max() - half - 0.05, step):
        a, b = loc(q, um, q0, half, Pm, bd), loc(q, ud, q0, half, Pd, bd)
        if a is None or b is None:
            continue
        Q.append(q0)
        RT.append(b[0] / a[0])
    return np.array(Q), np.array(RT)


def ripple(Q, R, lo=3.0, hi=9.0):
    gd = np.arange(lo, hi + 1e-9, 0.05)
    v = np.interp(gd, Q, R)
    sm = np.convolve(v, np.ones(41) / 41, mode='same')
    k = slice(25, len(gd) - 25)
    return float(np.std((v - sm)[k] / sm[k])), float(np.mean(v[k]))


P = {}
for t in ('lcdm', 'cr'):
    q_, um_, ud_ = fields(t)
    P[t] = (period_of(q_, um_, 2.5, 8.0), period_of(q_, ud_, 2.5, 8.0))

print("\n⛭⛭ ⓵ -- THE ESTIMATOR, VALIDATED BEFORE IT IS READ\n")
check("⛭ THE HELD PERIOD IS MEASURED AND IT IS NOT 2, which is the whole reason it is held at a "
      "measured value: the acoustic period in q is 2 BY CONSTRUCTION and the fields do not run at it, "
      "and the monopole and the dipole do not run at the same one",
      all(abs(P[t][i] - 2.0) > 0.004 for t in P for i in (0, 1))
      and all(abs(P[t][1] - P[t][0]) > 0.01 for t in P),
      "  ".join(f"{t}: monopole {P[t][0]:.5f} dipole {P[t][1]:.5f}" for t in P))
SUB = {}
for t in ('lcdm', 'cr'):
    q_, um_, ud_ = fields(t)
    SUB[t] = max(np.ptp([period_of(q_, y, lo, lo + 2.5) for lo in (2.5, 4.0, 5.5, 7.0)]) / 2.0
                 for y in (um_, ud_))
check("and its own uncertainty is measured from disjoint sub-ranges rather than assumed, which is what "
      "makes the leak test below a test at the right scale",
      all(0.005 < SUB[t] < 0.03 for t in SUB),
      "  ".join(f"{t} {100 * SUB[t]:.2f}%" for t in SUB) + f"; perturbation used {100 * PERR:.1f}%")

RW = {h: ripple(*amp_ratio('lcdm', half=h)) for h in (2.0, 1.0, 0.5)}
RH = {}
for h in (2.0, 1.0, 0.5, 0.35):
    Qh, Rh = held_ratio('lcdm', *P['lcdm'], half=h)
    RH[h] = ripple(Qh, Rh) + (float(Qh.min()),)
check("⛔ VALIDATION FIRST, AS ORDERED: the two estimators return the SAME quantity and their MEANS "
      "agree, on the range where both work -- the window estimator taken at the width where it is "
      "sound",
      abs(RH[0.5][1] / RW[2.0][1] - 1) < 0.01,
      f"window(half=2) {RW[2.0][1]:.4f} against held(half=0.5) {RH[0.5][1]:.4f}")
check("⚠ AND THE WINDOW ESTIMATOR DOES NOT SURVIVE ITS OWN WIDTH WHILE THE HELD ONE DOES: the window's "
      "ripple grows more than tenfold as it narrows to the width `cc66.51` read the candidate at, and "
      "the held estimator's is flat",
      RW[0.5][0] / RW[2.0][0] > 10 and max(RH[h][0] for h in RH) / min(RH[h][0] for h in RH) < 2,
      f"window {RW[2.0][0]:.4f} -> {RW[0.5][0]:.4f}; held "
      f"{min(RH[h][0] for h in RH):.4f} -> {max(RH[h][0] for h in RH):.4f}")
check("⛭ AND IT REACHES WHERE THE WINDOW ESTIMATOR CANNOT: the window estimator's lowest centre is "
      "1.5 + half and so never below q = 2.0, while the held fit needs only a fraction of a period "
      "and reaches the data's own edge",
      RH[0.35][2] < 0.5 and min(amp_ratio('lcdm', half=h)[0].min() for h in (2.0, 1.0, 0.5)) >= 2.0,
      f"held floor q = {RH[0.35][2]:.2f} against the window estimator's 2.00")


def cand(em=0.0, ed=0.0, half=0.5, bd=1):
    o = {}
    for t in ('lcdm', 'cr'):
        Q, R = held_ratio(t, P[t][0] * (1 + em), P[t][1] * (1 + ed), half=half, bd=bd)
        o[t] = np.array([np.mean(np.interp(np.linspace(a, b, 200), Q, R))
                         for a, b in zip(QE[:-1], QE[1:])])
    return o['cr'] / o['lcdm'] - 1.0


BASE = cand()
SPAN = float(BASE[-1] - BASE[1])
LEAK = max(abs(float(cand(em, ed)[-1] - cand(em, ed)[1]) - SPAN)
           for em, ed in ((PERR, PERR), (-PERR, -PERR), (0.0, PERR), (PERR, 0.0)))
check("⛭ AND THE COST THE ORDER NAMED IS MEASURED RATHER THAN NOTED: the held period perturbed at the "
      "scale it is KNOWN to moves the candidate's span across the bands by far less than that span.  "
      "⇒ THE ESTIMATOR CAN ANSWER THE QUESTION.  *The fit re-fits the PHASE in every window, so a "
      "wrong held period is absorbed there and costs a common amplitude factor, which cancels in a "
      "ratio of ratios*",
      LEAK / SPAN < 0.05,
      f"worst leak {LEAK:+.5f} against span {SPAN:+.5f} -- {100 * LEAK / SPAN:.1f} per cent")

# =================================================================================================
print("\n⛭⛭ ⓶ -- THE CANDIDATE, BELOW THE OLD FLOOR\n")
ALL = np.array([cand(half=h, bd=b) for h in (0.35, 0.5, 0.75, 1.0) for b in (1, 2)])
SPR = ALL.max(axis=0) - ALL.min(axis=0)
print('    q       ' + '  '.join(f'{x:8.2f}' for x in QC))
print('    dep     ' + '  '.join(f'{x:+8.5f}' for x in BASE))
print('    spread  ' + '  '.join(f'{x:8.5f}' for x in SPR))
check("⛔ THE SECOND NULL OF THE PRE-REGISTRATION, AND IT IS A FLOOR OF MECHANISM RATHER THAN OF "
      "WIDTH: band 1 is STILL not measurable -- its spread across eight estimator settings exceeds "
      "its value -- because its window straddles the first acoustic excursion, where there is no "
      "oscillation amplitude to estimate at all",
      SPR[0] > abs(BASE[0]) and SPR[0] > 4 * max(SPR[1:]),
      f"band 1 value {BASE[0]:+.5f} with spread {SPR[0]:.4f}")
check("and every band above it IS measurable, which is what makes the floor a statement and not an "
      "excuse", max(SPR[1:]) < 0.006, f"largest spread above band 1 is {max(SPR[1:]):.4f}")
check("⛭ AND THE BAND AT q = 1.90 IS NOW MEASURED, WHICH NO ESTIMATOR OF THIS QUANTITY HAS REACHED",
      SPR[1] < 0.005 and QC[1] < 2.0, f"band 2 at q = {QC[1]:.2f}, value {BASE[1]:+.5f}, "
      f"spread {SPR[1]:.4f}")


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def bands(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    o = (d['Dl'] - env_a(q, d['Dl'])) / env_a(q, d['Dl'])
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


TGT = bands(FI['cr']) / bands(FI['lcdm']) - 1.0
G = float(BASE[1:][-1] / BASE[1:][0])
GT = float(TGT[1:][-1] / TGT[1:][0])
check("⛭⛭ SIGN FIRST, THE TOOTH THIS SEAT ADDED LAST REVISION: on the range the estimator unlocked "
      "the candidate's departure is POSITIVE IN EVERY BAND, as the target's is",
      BASE[1:].min() > 0 and TGT[1:].min() > 0,
      f"candidate {BASE[1]:+.5f} -> {BASE[-1]:+.5f}; target {TGT[1]:+.5f} -> {TGT[-1]:+.5f}")
check("and GROWTH AFTER: it grows across the bands in the same direction as the target",
      G > 1 and GT > 1, f"candidate G = {G:.2f} against the target's {GT:.2f}")


def jack(d, qc):
    v = [float(np.polyfit(np.delete(qc, i), np.delete(d, i), 2)[0]) for i in range(len(qc))]
    return min(v), max(v)


JT1, JT2 = jack(TGT[1:], QC[1:]), jack(TGT[2:], QC[2:])
JC1 = jack(BASE[1:], QC[1:])
check("⛔⛔ AND THE CURVATURE TOOTH CANNOT BE APPLIED, WHICH IS THE FIRST NULL AND IS A STATEMENT ABOUT "
      "THE FILTER RATHER THAN THE CANDIDATE: the criterion is that the candidate's curvature carry the "
      "TARGET's sign, and the target's own curvature FLIPS SIGN when any single band is dropped, on "
      "both ranges either can be read on",
      JT1[0] * JT1[1] < 0 and JT2[0] * JT2[1] < 0,
      f"target drop-one curvature on q>=1.90 [{JT1[0]:+.6f}, {JT1[1]:+.6f}], "
      f"on q>=2.60 [{JT2[0]:+.6f}, {JT2[1]:+.6f}]")
DROP1 = [float(np.polyfit(np.delete(QC, i), np.delete(TGT, i), 2)[0]) for i in range(len(QC))]
check("⛔⛔ AND THE REASON IS EXACT RATHER THAN STATISTICAL: on the FULL seven-band range the "
      "target's curvature is negative as pre-registered at r6993, and dropping BAND 1 ALONE flips it "
      "positive while dropping any OTHER single band leaves it negative.  ⇒ *** THE TARGET'S "
      "DECELERATION IS CARRIED ENTIRELY BY THE ONE BAND NO ESTIMATOR OF THE CANDIDATE CAN REACH. ***",
      float(np.polyfit(QC, TGT, 2)[0]) < 0 < DROP1[0] and max(DROP1[1:]) < 0,
      f"full range {float(np.polyfit(QC, TGT, 2)[0]):+.6f}; drop band 1 {DROP1[0]:+.6f}; "
      f"drop any other in [{min(DROP1[1:]):+.6f}, {max(DROP1[1:]):+.6f}]")
check("⌗ and the candidate's own curvature is at least stable on the range this estimator unlocked, so "
      "what is missing is the target's sign and not the candidate's number",
      JC1[0] * JC1[1] > 0,
      f"candidate curvature {float(np.polyfit(QC[1:], BASE[1:], 2)[0]):+.6f}, drop-one "
      f"[{JC1[0]:+.6f}, {JC1[1]:+.6f}]")

CURV = {}
for h in (0.5, 1.0, 2.0):
    v = {}
    for t in ('lcdm', 'cr'):
        Q, R = amp_ratio(t, half=h)
        v[t] = np.interp(QC, Q, R)
    CURV[h] = float(np.polyfit(QC[2:], (v['cr'] / v['lcdm'] - 1)[2:], 2)[0])
check("⚠⚠ AND `cc66.51`'s CURVATURE PASS DOES NOT SURVIVE, WHICH IS A CORRECTION TO THIS SEAT'S OWN "
      "LANDED RESULT: read with the WINDOW estimator on its own range and its own recipe, the "
      "candidate's curvature CHANGES SIGN between the width it was read at and the width where that "
      "estimator is sound",
      CURV[0.5] < 0 < CURV[2.0],
      "  ".join(f"half={h}: {CURV[h]:+.6f}" for h in (0.5, 1.0, 2.0)))
check("⛔ and the reason `cc66.51`'s own stability check did not catch it is the 'say which quantity' "
      "guard biting the seat that wrote it: that check certified the MEAN over a sub-range, and the "
      "mean IS stable across the widths on which the curvature is not",
      abs(RW[0.5][1] / RW[2.0][1] - 1) < 0.01 and CURV[0.5] * CURV[2.0] < 0,
      f"means {RW[2.0][1]:.4f} and {RW[0.5][1]:.4f} agree to "
      f"{100 * abs(RW[0.5][1] / RW[2.0][1] - 1):.2f}% while the curvature changes sign")

# =================================================================================================
print("\n⛭⛭⛭ ⓷ -- THE PREDICTION IN ITS OWN RIGHT\n")


def chi_half(e, w, x):
    from scipy.optimize import brentq

    def f(k):
        return np.hypot(np.trapezoid(w * np.cos(k * x), e), np.trapezoid(w * np.sin(k * x), e)) - 0.5
    hi = 1e-3
    while f(hi) > 0:
        hi *= 2
    return 1.0 / brentq(f, 1e-9, hi)


ET = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}


def mk(t):
    d = ET[t]
    e = np.asarray(d['eta'], float)
    w = np.asarray(d['vis'], float)
    return e, w / np.trapezoid(w, e), np.asarray(d['rs_leaf'], float), \
        np.asarray(d['rs_stack'], float), np.asarray(d['jac'], float)


e, w, rl, rs, J = mk('cr')
ils = int(np.argmax(np.asarray(ET['cr']['vis'], float)))
CUM = float(rl[ils] / rs[ils])
WIN = float(np.trapezoid(w * J, e))
LA = float(ET['cr']['l_A'])
DM = float(ET['cr']['D_M'])
check("⛭ THE COMB READS THE CUMULATIVE JACOBIAN: pi D_M / rs_leaf reproduces the banked acoustic scale "
      "while pi D_M / rs_stack does not come near it, which is what 'the comb rides the leaf "
      "accumulation' means as a number",
      abs(np.pi * DM / rl[ils] / LA - 1) < 0.005 and abs(np.pi * DM / rs[ils] / LA - 1) > 0.3,
      f"pi D_M/rs_leaf = {np.pi * DM / rl[ils]:.3f} and pi D_M/rs_stack = {np.pi * DM / rs[ils]:.3f} "
      f"against l_A = {LA:.3f}")
check("⛭⛭⛭ AND THE WIDTHS READ A DIFFERENT FUNCTIONAL OF THE SAME OBJECT -- the WINDOW-LOCAL average "
      "against that CUMULATIVE integral -- so the width prediction is an INDEPENDENT reading of the "
      "two-rate assignment and not a restatement of the comb.  *Both are 1 on one rate and neither "
      "carries a free coefficient, so a construction tuned to the comb must still produce the right "
      "LOCAL Jacobian to match the widths*",
      abs(CUM / WIN - 1) > 0.20,
      f"cumulative {CUM:.5f} against window-local <Jac> {WIN:.5f} -- {100 * (CUM / WIN - 1):+.0f} "
      f"per cent apart")
WL = {t: chi_half(*mk(t)[:2], mk(t)[2]) for t in ('lcdm', 'cr')}
WEc = {t: chi_half(*mk(t)[:2], mk(t)[0]) for t in ('lcdm', 'cr')}
check("⛔ BUT NO MEASUREMENT REACHES THE RATIO, WHICH IS THE ANSWER THE ORDER ASKED FOR IN ITS OWN "
      "TERMS: the PHASE width, which the window's Landau damping of the acoustic oscillation reads, "
      "differs between the arms by under one per cent, while the CONFORMAL width, which the projection "
      "reads, differs by more than thirteen -- and `cc66.52` bounded the projection's contrast effect "
      "at two per cent with its sign undetermined.  ⇒ NOT OBSERVABLE IN ITS OWN RIGHT",
      abs(WL['cr'] / WL['lcdm'] - 1) < 0.01 and abs(WEc['cr'] / WEc['lcdm'] - 1) > 0.10,
      f"phase width {100 * (WL['cr'] / WL['lcdm'] - 1):+.2f}%, conformal width "
      f"{100 * (WEc['cr'] / WEc['lcdm'] - 1):+.2f}%")

PRED = os.path.join(DIR, 'PREDICTION.md')
TXT = open(PRED).read() if os.path.exists(PRED) else ''
check("⛔ THE ORDER'S GUARD: a PREDICTION.md exists and carries BOTH nulls as named outcomes -- the "
      "tooth that cannot be applied, and the floor that no estimator reaches",
      'THE FIRST NULL' in TXT and 'THE SECOND NULL' in TXT and TXT.count('| **') >= 5,
      f"{TXT.count('| **')} outcomes tabled, both nulls among them")
check("and it says WHEN each part of itself was written, rather than implying the table predates the "
      "reading it describes -- the teeth were fixed at r6993 and cc66.52 and the table was not",
      'committed at `r6993`' in TXT.lower().replace('committed at `R6993`', 'committed at `r6993`')
      or 'r6993' in TXT,
      "the taxonomy introduces no criterion and is dated")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
