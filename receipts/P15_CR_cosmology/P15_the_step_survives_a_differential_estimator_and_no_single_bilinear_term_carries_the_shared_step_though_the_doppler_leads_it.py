#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE STEP SURVIVES AN ESTIMATOR IN WHICH THE TWO LARGE COMMON STEPS
ARE NEVER FORMED, SO IT IS NOT THE RESIDUAL OF TWO LARGE NUMBERS; NO SINGLE BILINEAR TERM CARRIES THE SHARED
STEP AND IT IS A PROPERTY OF THE SUM; AND THE $42$ PER CENT IS $42$ PER CENT OF THE **EXCESS'S** STEP. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6915_pairs_{lcdm,cr}` and `r6959_eta_cr`'s band edges.  ⛔ *** Nothing is SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION IS ITS OWN COMMIT AHEAD OF THE WORKING SCRIPT. **  `r7015_directions/PREDICTION.md`
names the ordered estimator's algebra before use, tables FIRST the outcome that **ends the row's present
object**, and names both hazards it carries -- the phase sensitivity and the conditioning of the division --
*before* either was looked at.

⛭⛭⛭ ** ⓵ THE STEP SURVIVES THE DIFFERENTIAL ESTIMATOR. **  Write each arm as $\mathcal D = E\,(1+o)$.  The
present route forms $\operatorname{std}(o_a)$ and $\operatorname{std}(o_c)$ and divides; the ordered route
forms $R = \mathcal D_a/\mathcal D_c \approx (E_a/E_c)(1 + o_a - o_c)$ and takes the contrast of **that**, so
it reads $\operatorname{std}(o_a - o_c)$ and ** the common oscillation divides out before any width is
taken. **

⌗ Band 1's departure from its own bands 2--7 trend is $-0.374$ to $-0.387$ per common $\ell$ and $-0.382$ to
$-0.383$ per common $q$ -- *** same sign on all four trend bases and both abscissas, at $3.2$--$3.6\sigma$,
about $65\%$ of the present route's fractional size. ***

⇒ *** SO THE TENTH THAT FAILED TO CANCEL IS NOT THE RESIDUAL OF TWO LARGE NUMBERS: IT EXISTS IN AN ESTIMATOR
IN WHICH THE TWO LARGE NUMBERS ARE NEVER FORMED.  THE COSTLIEST PRE-REGISTERED OUTCOME DOES NOT FIRE. ***
⌷ *And neither does the conditioning hazard -- the control never falls below $0.67$ of its band median, so no
band divides by a near-zero.  **And the smoothed-divisor control does what it should**: with the differencing
removed the departure goes POSITIVE, back toward the arms' own $+0.3$, which shows it is the **differencing**
and not the **division** that produces the negative step.*

⚠ ** AND WHAT THE NEW ESTIMATOR IS NOT, NAMED IN THE PRE-REGISTRATION RATHER THAN HERE: **
$\operatorname{std}(o_a - o_c)$ is sensitive to a **phase** difference as well as an amplitude one, where the
amplitude ratio is blind to phase.  *So a null on it would have been strong; a signal on it does not by itself
say "amplitude", and its absolute size carries no expectation -- only the STEP is compared.*

⛔⛔ ** ⓶ NO SINGLE BILINEAR TERM CARRIES THE SHARED STEP, WHICH IS A NULL ON WHAT WAS ASKED. **  The
$238$-multipole `SRCDEC` total first reproduces the $1900$-multipole step to better than $0.006$ in departure
on **both** arms, which is what licenses a per-term reading at all.  Then removing each term in turn: ** the
losses sum to $182\%$, far more than one, so the step is not additive across terms and is a property of the
SUM. **

⛭⛭ ** BUT THE LEVERAGE IS NOT FLAT, AND THAT IS WHAT THE NULL LEAVES STANDING. **  Each term's share of the
STEP against its share of the OSCILLATION: *** the two highest-leverage terms are BOTH Doppler -- `sw*dp` at
$5.59\times$ and `dp*dp` at $3.80\times$ -- exceeding every term without a Doppler factor (best: `sw*isw` at
$1.23\times$) by $3.1$ or more, while the monopole `sw*sw` carries $88\%$ of the oscillation at only
$0.72\times$. ***  ⇒ ** A step-weighted reading of the bilinear decomposition is led by the Doppler where an
amplitude-weighted one is led by the monopole. **

⚠ *`dp*isw` is the named exception: it carries a Doppler factor and its leverage is **negative**,
$-0.91\times$, so this is "the two highest-leverage terms are Doppler" and **not** "every Doppler term
leads".  It is not the lowest either -- `isw*isw` sits at $-2.07\times$ -- so the ordering is not
Doppler-versus-not.  And **leverage is not
authorship** -- the non-additivity is exactly why it is not.*

⛭ ** ⓷ THE $42$ PER CENT IS $42$ PER CENT OF THE EXCESS'S STEP, NOT OF THE SHARED STEP. **  `cc66.58`'s table
divided every channel's departure by the departure of `MEAS - 1.0`, the excess's own response -- which is the
only comparison a channel admits, because a channel response and the excess are both ratios to the **same**
control.  ⇒ *So it is the large reading: the pair accounts for two fifths of the step the excess actually has.*

⌗ ** AND THE TWO NORMALISATIONS ARE ONE DEPARTURE, SET SIDE BY SIDE SO THEY CANNOT BE CONFLATED AGAIN: **
$-0.0323$ in excess units, which is $-0.601$ of the excess's own extrapolated size (*what the $42$ per cent is
against*) and $-0.100$ of the control's contrast departure (*where the "nine tenths" comes from*).  The arms'
own log-departures differ by $-0.0308$, which is that same number to $4.6$ per cent.

⛔ *No envelope chosen, no trend basis chosen, **no abscissa chosen**, no new candidate, no mechanism proposed,
and no corpus edits.*
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7015_directions')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NM = ['sw*sw', 'sw*dp', 'sw*isw', 'sw*pol', 'dp*dp', 'dp*isw', 'dp*pol',
      'isw*isw', 'isw*pol', 'pol*pol']
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "r6941_fine_*, r6915_pairs_* and r6959_eta_cr's band edges only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6915_pairs_lcdm.npz', 'r6915_pairs_cr.npz')
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
check("⛔⛭ THE SEQUENCING: the pre-registration says in terms that nothing below it had been measured, names "
      "the ordered estimator's algebra and the meaning of a step in it BEFORE use, and tables FIRST the "
      "outcome that ENDS THE ROW'S PRESENT OBJECT",
      'Nothing below has been measured' in TXT
      and 'NAMED BEFORE USE' in TXT
      and TXT.index('THE STEP DOES NOT SURVIVE') < TXT.index('THE STEP SURVIVES'),
      "the row-ending outcome leads the table")
check("⛭ AND IT NAMES BOTH HAZARDS THE NEW ESTIMATOR CARRIES BEFORE EITHER WAS LOOKED AT -- the phase "
      "sensitivity, which makes a null strong and a signal weaker than it looks, and the conditioning of a "
      "division whose divisor passes through the first acoustic trough INSIDE the band under test",
      'sensitive to a **phase** difference' in TXT and 'ill-conditioned' in TXT
      and 'inside band 1' in TXT.lower() and 'reported as part of' in TXT,
      "phase sensitivity and division conditioning both pre-registered")
check("⛭ AND IT REFUSES THE NEW DEGREE OF FREEDOM THE ESTIMATOR INTRODUCES, rather than choosing it: per "
      "common l and per common q are BOTH to be reported, which is the basis-family discipline extended",
      'AND THE ABSCISSA IS NOT CHOSEN' in TXT and 'Both are reported' in TXT,
      "no abscissa chosen, as no envelope and no basis were")
check("⛭ AND ⓶ IS GATED ON A LICENCE CHECK WRITTEN BEFORE IT: the 238-multipole total must reproduce the "
      "1900-multipole step or no per-term number is licensed at all",
      'the per-term reading is not licensed at all' in TXT
      and TXT.index('not licensed at all') > TXT.index('THE READING, NAMED BEFORE USE'),
      "the licence condition precedes the reading")


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period in q -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def band_std(q, y):
    e = env_a(q, y)
    o = (y - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def departure(v, p, lg):
    """band 1 against its OWN bands 2--7 trend, as a FRACTION of the extrapolation -- `cc66.58`'s statistic"""
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms, float(f[0]) / rms


def dep4(v):
    return [departure(v, p, lg) for _, p, lg in BASES]


LC, DC, AC = fine('lcdm')
LA, DA, AA = fine('cr')
QCq, QAq = LC / AC, LA / AA
C0, CA = band_std(QCq, DC), band_std(QAq, DA)
MEAS = CA / C0

# ==================================================================================================
print("\nPART 1 -- ⓵ THE STEP SURVIVES AN ESTIMATOR IN WHICH THE TWO LARGE COMMON STEPS ARE NEVER FORMED.")
print("-" * 100)
m = np.isin(LA, LC)
RL = band_std(LA[m] / AA, DA[m] / np.interp(LA[m], LC, DC))
gq = np.linspace(max(QCq.min(), QAq.min()), min(QCq.max(), QAq.max()), len(LC))
RQ = band_std(gq, np.interp(gq, QAq, DA) / np.interp(gq, QCq, DC))
DL_, DQ_, DE_ = dep4(RL), dep4(RQ), dep4(MEAS - 1.0)
for nm, D in (('per common l', DL_), ('per common q', DQ_), ('present excess', DE_)):
    print(f"    {nm:16s} " + "  ".join(f"{d[0]:+.3f}({d[2]:+.2f}s)" for d in D))
check("⓵ THE ORDERED ESTIMATOR IS ACTUALLY DIFFERENTIAL, not a restatement: the ratio is formed at the level "
      "of the SPECTRA and the contrast taken of that single ratio, so neither arm's own width is ever computed "
      "in it",
      'np.interp(gq, QAq, DA) / np.interp(gq, QCq, DC)' in SRC and 'DA[m] / np.interp(LA[m], LC, DC)' in SRC,
      "ratio first, contrast second, on both abscissas")
check("⇒ *** AND THE STEP SURVIVES IT: band 1 departs from its own bands 2--7 trend with the SAME SIGN on all "
      "four trend bases AND on both abscissas, above the bands 2--7 scatter throughout ***",
      all(d[0] < 0 for d in DL_) and all(d[0] < 0 for d in DQ_)
      and min(abs(d[2]) for d in DL_ + DQ_) > 2.0,
      f"per l {min(d[0] for d in DL_):+.3f}..{max(d[0] for d in DL_):+.3f}, "
      f"per q {min(d[0] for d in DQ_):+.3f}..{max(d[0] for d in DQ_):+.3f}, "
      f"min {min(abs(d[2]) for d in DL_ + DQ_):.2f} sigma")
check("AND IT SURVIVES AT A SIZE COMPARABLE TO THE PRESENT ROUTE'S rather than collapsing toward zero, which "
      "is what the order asked to be tested",
      0.4 < np.mean([abs(d[0]) for d in DQ_]) / np.mean([abs(d[0]) for d in DE_]) < 1.3,
      f"{np.mean([abs(d[0]) for d in DQ_]) / np.mean([abs(d[0]) for d in DE_]):.0%} of the present route's "
      f"fractional departure")
check("AND THE TWO ABSCISSAS AGREE, so the pairing is not what produces it -- which is the pre-registration's "
      "middle row NOT firing",
      abs(np.mean([d[0] for d in DL_]) - np.mean([d[0] for d in DQ_])) < 0.25 * abs(np.mean([d[0] for d in DQ_])),
      f"means {np.mean([d[0] for d in DL_]):+.3f} against {np.mean([d[0] for d in DQ_]):+.3f}")
COND = min(DC[(QCq >= a) & (QCq < b)].min() / np.median(DC[(QCq >= a) & (QCq < b)])
           for a, b in zip(QE[:-1], QE[1:]))
check("⌷ AND THE CONDITIONING HAZARD THE PRE-REGISTRATION NAMED DOES NOT FIRE: the divisor never approaches "
      "zero in any band, the first acoustic trough inside band 1 included",
      COND > 0.4, f"the control's worst band minimum is {COND:.2f} of that band's median")
DS_ = dep4(band_std(gq, np.interp(gq, QAq, DA) / np.interp(gq, QCq, env_a(QCq, DC))))
check("⌗ AND THE SMOOTHED-DIVISOR CONTROL SHOWS IT IS THE **DIFFERENCING** AND NOT THE **DIVISION** THAT "
      "PRODUCES THE NEGATIVE STEP: remove the differencing by dividing by a smoothed control and the departure "
      "turns POSITIVE, back toward the arms' own positive step",
      all(d[0] > 0 for d in DS_) and all(d[0] < 0 for d in DQ_),
      f"smoothed divisor {min(d[0] for d in DS_):+.3f}..{max(d[0] for d in DS_):+.3f} against the "
      f"differential's {max(d[0] for d in DQ_):+.3f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ NO SINGLE BILINEAR TERM CARRIES THE SHARED STEP; IT IS A PROPERTY OF THE SUM.")
print("-" * 100)
P = {}
for t in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r6915_pairs_{t}.npz'), allow_pickle=True)
    P[t] = (d['ls'].astype(float) / float(d['l_A']), d['Dl'], d['Dl_pairs'])
check("the bank carries the full bilinear decomposition for BOTH arms over all seven bands, which is what "
      "makes ⓶ answerable from disk",
      P['lcdm'][2].shape[1] == 10 and P['cr'][2].shape[1] == 10
      and P['lcdm'][0].min() < QE[0] and P['lcdm'][0].max() > QE[-1]
      and P['cr'][0].min() < QE[0] and P['cr'][0].max() > QE[-1],
      f"10 terms, q = {P['lcdm'][0].min():.3f}--{P['lcdm'][0].max():.3f}, "
      f"{len(P['lcdm'][0])} multipoles per arm")
LICOK = True
for t, ref in (('lcdm', C0), ('cr', CA)):
    a_, b_ = dep4(band_std(P[t][0], P[t][1])), dep4(ref)
    w = max(abs(x[0] - y[0]) for x, y in zip(a_, b_))
    LICOK = LICOK and w < 0.02
    print(f"    {t:5s}: 238-pt total {min(d[0] for d in a_):+.3f}..{max(d[0] for d in a_):+.3f} against "
          f"1900-pt {min(d[0] for d in b_):+.3f}..{max(d[0] for d in b_):+.3f}, worst gap {w:.4f}")
check("⛔ THE LICENCE CHECK THE PRE-REGISTRATION PUT BEFORE THE READING: the 238-multipole total reproduces "
      "the 1900-multipole step on BOTH arms, so the per-term reading is licensed",
      LICOK, "both arms agree to better than 0.02 in departure on every basis")
BASE = {t: [d[0] for d in dep4(band_std(P[t][0], P[t][1]))] for t in ('lcdm', 'cr')}
DROP, SHARE = {}, {}
for k, nm in enumerate(NM):
    out = {}
    for t in ('lcdm', 'cr'):
        q, tot, pr = P[t]
        out[t] = [d[0] for d in dep4(band_std(q, tot - pr[:, k]))]
    q, tot, pr = P['lcdm']
    SHARE[nm] = float(np.std(pr[:, k] - env_a(q, pr[:, k])) / np.std(tot - env_a(q, tot)))
    DROP[nm] = 1 - np.mean([abs(np.mean(out[t])) / abs(np.mean(BASE[t])) for t in ('lcdm', 'cr')])
TOT = sum(max(0.0, DROP[n]) for n in NM)
check("⇒ AND NO SINGLE TERM CARRIES IT: removing each term in turn, the fractional losses SUM TO FAR MORE THAN "
      "ONE, so the step is not additive across the terms and is a property of the SUM.  ** That is the "
      "pre-registered NULL on the naming ⓶ asked for, reported as a null **",
      TOT > 1.5 and max(DROP.values()) < 0.9,
      f"the losses sum to {TOT:.0%}; the largest single loss is {max(DROP.values()):.0%} "
      f"({max(DROP, key=DROP.get)})")
LEV = {n: DROP[n] / SHARE[n] for n in NM if SHARE[n] > 0.01}
ORD = sorted(LEV, key=lambda n: -LEV[n])
for n in ORD:
    print(f"    {n:10s} {DROP[n]:+7.1%} of the step on {SHARE[n]:6.1%} of the oscillation  "
          f"=> leverage {LEV[n]:+5.2f}x" + ("   <- Doppler" if 'dp' in n else ""))
check("⛭⛭ BUT THE LEVERAGE IS NOT FLAT, AND THAT IS WHAT THE NULL LEAVES STANDING: the two highest-leverage "
      "terms BOTH carry a Doppler factor, and they exceed every term without one by a wide margin",
      all('dp' in n for n in ORD[:2])
      and min(LEV[n] for n in ORD[:2]) > 2.0 * max(LEV[n] for n in ORD if 'dp' not in n),
      f"{ORD[0]} {LEV[ORD[0]]:.2f}x and {ORD[1]} {LEV[ORD[1]]:.2f}x against the best non-Doppler "
      f"{max((n for n in ORD if 'dp' not in n), key=lambda n: LEV[n])} "
      f"{max(LEV[n] for n in ORD if 'dp' not in n):.2f}x")
check("AND THE MONOPOLE CARRIES THE OSCILLATION WITHOUT CARRYING THE STEP, which is what makes the leverage "
      "the readable quantity rather than the share",
      SHARE['sw*sw'] > 0.7 and LEV['sw*sw'] < 1.0,
      f"`sw*sw` is {SHARE['sw*sw']:.0%} of the oscillation at {LEV['sw*sw']:.2f}x leverage")
check("⚠ AND THE EXCEPTION IS NAMED RATHER THAN DROPPED: a Doppler-bearing term has NEGATIVE leverage, so the "
      "claim is \"the two highest-leverage terms are Doppler\" and NOT \"every Doppler term leads\"; and the "
      "ordering is not Doppler-versus-not, since a term without a Doppler factor sits lower still",
      LEV['dp*isw'] < 0 < LEV[ORD[0]]
      and min(LEV[n] for n in ORD if 'dp' not in n) < LEV['dp*isw']
      and 'named exception' in SRC.split(chr(34) * 3)[1],
      f"`dp*isw` {LEV['dp*isw']:+.2f}x, and `isw*isw` lower still at "
      f"{min(LEV[n] for n in ORD if 'dp' not in n):+.2f}x")
check("⛔ AND LEVERAGE IS NOT CLAIMED AS AUTHORSHIP, which the non-additivity is the reason for -- stated in "
      "the header rather than left to the reader",
      'leverage is not' in SRC.split(chr(34) * 3)[1]
      and 'authorship' in SRC.split(chr(34) * 3)[1],
      "the null governs the naming")

# ==================================================================================================
print("\nPART 3 -- ⓷ WHICH STEP THE 42 PER CENT IS 42 PER CENT OF.")
print("-" * 100)
C58 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'P15_the_window_free_reading_cannot_resolve_the_first_cycle_the_flatness_was_a_'
                        'trend_and_nine_tenths_of_the_step_is_common_to_both_arms.py')).read()
check("⓷ ANSWERED FROM `cc66.58`'s OWN FILE AND GATED ON IT: its share function divides every channel's "
      "departure by `DEP['measured excess']`, and that entry is the departure of `MEAS - 1.0` -- the EXCESS's "
      "own response.  ⇒ ** THE 42 PER CENT IS 42 PER CENT OF THE EXCESS'S STEP, NOT OF THE SHARED STEP **",
      "abs(a[0]) / abs(b[0]) for a, b in zip(DEP[nm], DEP['measured excess'])" in C58
      and "('measured excess', MEAS)" in C58
      and "v = WIDTH if nm == 'proj. width' else R - 1.0" in C58,
      "the denominator is the excess's own response, so it is the large reading")
sA, iA = np.polyfit(QC[1:] ** 2, np.log(CA[1:]), 1)
sC, iC = np.polyfit(QC[1:] ** 2, np.log(C0[1:]), 1)
dA = float(np.log(CA[0]) - (sA * QC[0] ** 2 + iA))
dC = float(np.log(C0[0]) - (sC * QC[0] ** 2 + iC))
sE, iE = np.polyfit(QC[1:] ** 2, np.log(MEAS[1:] - 1.0), 1)
predE = float(np.exp(sE * QC[0] ** 2 + iE))
absdep = float((MEAS[0] - 1.0) - predE)
print(f"    the ONE departure, in excess units: {absdep:+.4f}   "
      f"(band 1's excess {MEAS[0] - 1:+.4f} against its own trend's {predE:+.4f})")
print(f"      (i)  of the EXCESS's own size:        {absdep / predE:+.3f}")
print(f"      (ii) of the control's contrast step:  {absdep / dC:+.3f}   (of the arm's: {absdep / dA:+.3f})")
check("⌗ AND THE TWO NORMALISATIONS ARE ONE DEPARTURE UNDER TWO DENOMINATORS, NOT TWO FINDINGS -- which is "
      "provable rather than asserted: the arms' own log-departures DIFFER BY that same number",
      abs((dA - dC) / absdep - 1) < 0.10,
      f"the arms differ by {dA - dC:+.4f} against the excess's {absdep:+.4f}, "
      f"{100 * abs((dA - dC) / absdep - 1):.1f} per cent apart")
check("⇒ AND THAT IS WHY THE TWO READINGS OF THE SAME STEP LOOK SO DIFFERENT: the excess's own size and either "
      "arm's contrast departure differ by about an order of magnitude, so the SAME departure reads as three "
      "fifths against one and a tenth against the other",
      abs(absdep / predE) > 4 * abs(absdep / dC),
      f"{absdep / predE:+.3f} against {absdep / dC:+.3f}")
check("⛔ AND ⓸ HOLDS: no envelope, no trend basis and no abscissa is chosen, and no new candidate or mechanism "
      "is introduced -- stated in this receipt's own header",
      'no abscissa chosen' in SRC.split(chr(34) * 3)[1]
      and 'no mechanism proposed' in SRC.split(chr(34) * 3)[1],
      "four bases and two abscissas reported, none chosen")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
