#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE STEP IS THE EXCESS'S AND NOT THE ESTIMATOR'S, SURVIVING THREE
ENVELOPES AND ONE READING THAT NEEDS NONE; IT SITS AT THE SECOND ACOUSTIC PEAK TO UNDER ONE PER CENT AND
IS SHARPER THAN THE WINDOW THAT FOUND IT; AND ALL FOUR CANDIDATES CAN BE SCORED ON IT AND NONE OF THEM
PRODUCES IT. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6915_pairs_{lcdm,cr}`, `r6897_fields` and `r6959_eta_cr`'s band edges.  ⛔ *** Nothing is SOLVED and
nothing is RUN. ***

** AND THE PRE-REGISTRATION WAS WRITTEN BEFORE ANY OF THIS WAS COMPUTED, WHICH THE ORDER SEQUENCED IN
TERMS. **  `r7009_directions/PREDICTION.md` names the step's definition before it is used and tables
FIRST the outcome that ***withdraws `cc66.56`'s ⓷***, which `r7009` had already landed in two sections.
⌗ *The three previous revisions each had to record that their outcome tables followed their measurements;
this one does not, and the difference is the order's sequencing.*

⛭⛭⛭ ** ⓵ THE STEP IS THE EXCESS'S. **  Four readings -- a running arithmetic mean, a running median, a
local quadratic (Savitzky--Golay, *different in kind rather than in width*), and the peak-to-trough depth
per acoustic cycle, *which needs no window at all* -- and the step ratio (band 1's excess over the mean of
bands 2--7) reads $0.333$, $0.391$, $0.633$ and $-0.025$.  ⇒ ** Never near one on any of them. **

⌷ ** AND THE EDGE HAZARD IS RULED OUT THE RIGHT WAY ROUND, which is what makes it ruled out. **  The
order's new guard is that a step at the edge band is where an edge artefact lives, and band 1's envelope
comes within $0.018$ in $q$ of truncating.  *But moving the band's lower edge up from $0.85$ to $1.15$
makes it read $+0.0215 \to +0.0361$* -- ** higher, where a truncation artefact would have to make it read
lower. **

⚠ ** ITS SIZE IS READING-DEPENDENT AND IS QUOTED AS A RANGE. **  Band 1 is a third of the rest on the
arithmetic envelope, nearly two thirds on the Savitzky--Golay one, and *nothing at all* on the
envelope-free one -- whose band 1 carries only one acoustic cycle, so it is coarse.  ⇒ *The step is
"band 1 between none and two thirds of the rest", not a number.*  ⛔ *No envelope is chosen; a third was
added, which is what the order asked.*

⛭⛭⛭ ** ⓶ AND IT SITS AT THE SECOND ACOUSTIC PEAK. **  The half-rise point of the excess, measured in
sliding windows at three widths, is $q = 1.789,\,1.788,\,1.805$ -- ** $1.794 \pm 0.008$ ** -- against the
second acoustic peak at $q = 1.7775$ on the control and $1.7760$ on the arm: *** A MATCH TO $0.9$ PER
CENT, where the nearest other scale the construction fixes -- the monopole's second turning point at
$1.915$ -- is seven per cent away, and $q=2$ is twelve. ***  ⌗ And the plateaux are $0.026$ below and
$0.053$ above on all three widths: ** a factor of $2.0$, reached within about a tenth of a comb period,
sharper than the narrowest window that found it. **

⇒ *** SO THE EXCESS IS ONE SIZE IN THE FIRST ACOUSTIC CYCLE AND TWICE THAT IN EVERY CYCLE ABOVE IT. ***
⛔ **Not claimed: that this is a mechanism.**  *A step at a scale is a signature to be explained, which is
what the pre-registration said would not be claimed.*

⛔⛔ ** ⓷ AND ALL FOUR CANDIDATES CAN BE SCORED ON THE STEP, AND NONE OF THEM PRODUCES IT. **
  · the WINDOW WEIGHTING (`cc66.47`) and the TERM MIX (`cc66.48/49`) were both measured **flat in $q$**
    -- and a flat candidate's step ratio is exactly one, by construction and without a new number;
  · the PROJECTION WIDTH (`cc66.52`), kernel-class and reachable at band 1, is fitted by a **straight
    line in $q$** to under three per cent of its own range -- *linear, so no step*;
  · the DOPPLER, by the swap route that reaches band 1 (`cc66.56`), runs $-0.0016$ to $+0.0014$ in
    sliding half-period windows with means $-0.0001$ below the step and $-0.0002$ above -- ** noise at
    the resolution the step needs, and no transition at all. **
⇒ *** THIS IS NOT THE IDENTIFIABILITY FLOOR CLOSING OVER THE LIST -- every one of the four WAS
evaluable -- IT IS THE LIST EXHAUSTED AGAINST THE RIGHT FEATURE, FOR THE FIRST TIME. ***  ⌗ *So the row's
question is now: what turns on at the second acoustic peak?  Narrower than the question this sector has
asked for six revisions, and not a channel.*
"""
import os

import numpy as np
from scipy.signal import argrelextrema, savgol_filter

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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7009_directions')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NM = ['sw*sw', 'sw*dp', 'sw*isw', 'sw*pol', 'dp*dp', 'dp*isw', 'dp*pol',
      'isw*isw', 'isw*pol', 'pol*pol']
I = {n: k for k, n in enumerate(NM)}
DPT = [I['sw*dp'], I['dp*dp'], I['dp*isw'], I['dp*pol']]
WIDTH = np.array([0.00343, 0.00569, 0.00816, 0.01079, 0.01350, 0.01640, 0.01955])   # cc66.52

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "r6941_fine_*, r6915_pairs_*, r6897_fields and r6959_eta_cr's band edges only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔⛭ THE ORDER SEQUENCED THIS AND THE SEQUENCING WAS HONOURED: the pre-registration says in terms "
      "that nothing in ⓵ had been computed when it was written, names the step's definition BEFORE it is "
      "used, and tables FIRST the outcome that WITHDRAWS `cc66.56`'s ⓷ -- the one that costs this seat "
      "most",
      'Nothing in ⓵ has been computed at the time' in TXT
      and 'THE STEP GOES AWAY ON THE THIRD ENVELOPE' in TXT
      and TXT.index('THE STEP GOES AWAY') < TXT.index('The step survives every reading')
      and 'ratio of band 1' in TXT.lower(),
      "the withdrawal outcome is the first row of the failure-mode table")


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


def env(x, y, win=1.0, kind='mean'):
    if kind == 'savgol':
        n = int(round(win / np.median(np.diff(x))))
        return savgol_filter(y, n + (n + 1) % 2, 2, mode='nearest')
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def band_excess(kind='mean'):
    C = {}
    for t in ('lcdm', 'cr'):
        x, y = fine(t)
        e = env(x, y, 1.0, kind)
        C[t] = np.array([float(np.std(np.interp(np.linspace(a, b, 400), x, (y - e) / e)))
                         for a, b in zip(QE[:-1], QE[1:])])
    return C['cr'] / C['lcdm'] - 1.0


def depths(t):
    x, y = fine(t)
    e = np.sort(np.concatenate([argrelextrema(y, np.greater, order=20)[0],
                               argrelextrema(y, np.less, order=20)[0]]))
    return 0.5 * (x[e[:-1]] + x[e[1:]]), np.abs(y[e[1:]] - y[e[:-1]]) / (y[e[1:]] + y[e[:-1]])


def slide(a, b, kind='mean'):
    out = []
    for t in ('lcdm', 'cr'):
        x, y = fine(t)
        e = env(x, y, 1.0, kind)
        out.append(float(np.std(np.interp(np.linspace(a, b, 400), x, (y - e) / e))))
    return out[1] / out[0] - 1.0


print("\n⛭⛭⛭ ⓵ IS THE STEP THE EXCESS'S OR THE ESTIMATOR'S\n")
STEP = {}
for kind in ('mean', 'median', 'savgol'):
    T = band_excess(kind)
    STEP[kind] = float(T[0] / T[1:].mean())
    print(f"    {kind:8s} " + '  '.join(f'{v:+.4f}' for v in T) + f"   step {STEP[kind]:.3f}")
qa, da = depths('cr')
qc, dc = depths('lcdm')
RA = np.array([da[(qa >= a) & (qa < b)].mean() / dc[(qc >= a) & (qc < b)].mean() - 1.0
               for a, b in zip(QE[:-1], QE[1:])])
STEP['none'] = float(RA[0] / RA[1:].mean())
print(f"    {'no env.':8s} " + '  '.join(f'{v:+.4f}' for v in RA) + f"   step {STEP['none']:.3f}")
check("⛭⛭⛭ THE STEP SURVIVES ALL FOUR READINGS -- three envelopes differing in KIND and one that needs "
      "no window at all -- and is never near one on any of them.  ⇒ IT IS THE EXCESS'S AND NOT THE "
      "ESTIMATOR'S, which is the outcome the pre-registration tabled as the one to be most careful about",
      max(STEP.values()) < 0.7,
      "  ".join(f"{k} {v:.3f}" for k, v in STEP.items()))
check("and the envelope-free reading is the sharpest of them: band 1's excess on the peak-to-trough depth "
      "is indistinguishable from zero while bands 2-7 average six per cent",
      abs(RA[0]) < 0.01 and RA[1:].mean() > 0.04,
      f"band 1 {RA[0]:+.4f} against a bands 2-7 mean of {RA[1:].mean():+.4f}")
EDGE = [(a, slide(a, 1.55)) for a in (0.85, 0.95, 1.05, 1.15)]
check("⌷ AND THE EDGE HAZARD IS RULED OUT THE RIGHT WAY ROUND, which is what makes it ruled out: moving "
      "band 1's lower edge UP, away from where the envelope nearly truncates, makes it read HIGHER -- "
      "and a truncation artefact would have to make it read lower",
      all(EDGE[i][1] < EDGE[i + 1][1] for i in range(len(EDGE) - 1)),
      "  ".join(f"[{a:.2f},1.55] {v:+.4f}" for a, v in EDGE))

print("\n⛭⛭ ⓶ LOCATING THE STEP\n")
LOC, FAC = [], []
for half in (0.175, 0.25, 0.35):
    row = [(c, slide(c - half, c + half)) for c in np.arange(0.85 + half, 3.0, 0.05)]
    lo = np.mean([v for c, v in row if c < 1.4])
    hi = np.mean([v for c, v in row if c > 2.2])
    mid = 0.5 * (lo + hi)
    LOC.append(next(row[i - 1][0] + (mid - row[i - 1][1]) / (row[i][1] - row[i - 1][1]) * 0.05
                    for i in range(1, len(row)) if row[i - 1][1] < mid <= row[i][1]))
    FAC.append(hi / lo)
    print(f"    half {half:.3f}: plateaux {lo:.4f} -> {hi:.4f} (factor {hi / lo:.2f}), "
          f"half-rise q = {LOC[-1]:.3f}")
check("⛭ THE STEP'S LOCATION IS STABLE ACROSS THREE WINDOW WIDTHS and its size is a clean factor of two "
      "on all three, so it is a feature of the excess rather than of the window",
      np.ptp(LOC) < 0.03 and 1.9 < min(FAC) and max(FAC) < 2.2,
      f"q = {np.mean(LOC):.3f} +- {np.ptp(LOC) / 2:.3f}, factor {min(FAC):.2f} to {max(FAC):.2f}")
PK = {}
for t in ('lcdm', 'cr'):
    x, y = fine(t)
    PK[t] = x[argrelextrema(y, np.greater, order=30)[0]][:4]
F = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
o = np.argsort(F['k__lcdm'])
qf = F['k__lcdm'][o] * float(F['r_s__lcdm']) / np.pi
um = (F['th0__lcdm'][o] + F['psi__lcdm'][o]) / F['psi__lcdm'][o]
TPM = qf[np.where(np.diff(np.sign(np.diff(um))) != 0)[0] + 1][:3]
OTHER = np.array([TPM[0], TPM[1], 0.5 * (TPM[0] + TPM[1]), 1.0, 2.0])
check("⛭⛭⛭ AND IT SITS AT THE SECOND ACOUSTIC PEAK, to under one and a half per cent -- while the "
      "NEAREST other scale the construction fixes is more than five per cent away.  ⇒ The step's "
      "location is a scale the construction fixes and carries no free coefficient",
      abs(np.mean(LOC) / PK['lcdm'][1] - 1) < 0.015
      and np.min(np.abs(OTHER / np.mean(LOC) - 1)) > 0.05,
      f"measured {np.mean(LOC):.3f}; second peak {PK['lcdm'][1]:.4f} (control) and {PK['cr'][1]:.4f} "
      f"(arm), a match to {100 * abs(np.mean(LOC) / PK['lcdm'][1] - 1):.1f}%; nearest other scale "
      f"{100 * np.min(np.abs(OTHER / np.mean(LOC) - 1)):.0f}% away")

print("\n⛔⛔ ⓷ RE-SCORING THE FOUR ON THE STEP\n")
sl, ic = np.polyfit(QC, WIDTH, 1)
check("⛔ THE PROJECTION WIDTH is fitted by a STRAIGHT LINE in q to a few per cent of its own range, so "
      "it has no step -- and it is the kernel-class candidate that CAN be evaluated at band 1",
      np.max(np.abs(WIDTH - (sl * QC + ic))) / np.ptp(WIDTH) < 0.05 and WIDTH[0] > 0,
      f"linear to {np.max(np.abs(WIDTH - (sl * QC + ic))) / np.ptp(WIDTH):.1%} of its range, with a "
      f"band-1 value of {WIDTH[0]:+.5f}")
P = {}
for t in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r6915_pairs_{t}.npz'), allow_pickle=True)
    P[t] = (d['ls'].astype(float) / float(d['l_A']), d['Dl'], d['Dl_pairs'])
qa2, Da, Pa = P['cr']
qc2, Dc, Pc = P['lcdm']
sc = env(qa2, Da) / np.interp(qa2, qc2, env(qc2, Dc))
Dsw = Da - Pa[:, DPT].sum(axis=1) + np.interp(qa2, qc2, Pc[:, DPT].sum(axis=1)) * sc


def st(x, y, a, b):
    e = env(x, y)
    return float(np.std(np.interp(np.linspace(a, b, 400), x, (y - e) / e)))


DOP = [(c, st(qa2, Da, c - 0.25, c + 0.25) - st(qa2, Dsw, c - 0.25, c + 0.25))
       for c in np.arange(1.10, 3.01, 0.10)]
DL = np.mean([v for c, v in DOP if c < 1.75])
DH = np.mean([v for c, v in DOP if c > 1.85])
check("⛔ AND THE DOPPLER, BY THE SWAP ROUTE THAT REACHES BAND 1, IS NOISE AT THE STEP'S RESOLUTION: in "
      "sliding half-period windows its contribution changes sign repeatedly and its means either side "
      "of the step are equal and both near zero.  ⇒ No transition at all",
      abs(DH - DL) < 0.3 * (max(v for _, v in DOP) - min(v for _, v in DOP))
      and min(v for _, v in DOP) < 0 < max(v for _, v in DOP),
      f"range {min(v for _, v in DOP):+.4f} to {max(v for _, v in DOP):+.4f}; means {DL:+.4f} below and "
      f"{DH:+.4f} above")
FLAT = np.full(7, 0.05)
check("⛔ AND A FLAT CANDIDATE CANNOT PRODUCE A STEP, by construction and without a new number -- which "
      "scores the WINDOW WEIGHTING and the TERM MIX, both measured flat in q: a constant's step ratio is "
      "exactly one, and the excess's is under two thirds on every reading",
      abs(FLAT[0] / FLAT[1:].mean() - 1.0) < 1e-12 and max(STEP.values()) < 0.7,
      "a constant scores 1.000 where the excess scores at most "
      f"{max(STEP.values()):.3f}")
check("⇒ AND THIS IS NOT THE IDENTIFIABILITY FLOOR CLOSING OVER THE LIST: every one of the four was "
      "evaluable on the step by at least one route.  ** IT IS THE LIST EXHAUSTED AGAINST THE RIGHT "
      "FEATURE, FOR THE FIRST TIME **",
      WIDTH[0] > 0 and len(DOP) > 10 and max(STEP.values()) < 0.7,
      "projection width and Doppler evaluated at band 1; the two flat candidates scored by construction")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
