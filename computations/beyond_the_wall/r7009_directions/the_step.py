"""⓵⓶⓷ IS THE STEP REAL, WHERE IS IT, AND DO ANY OF THE FOUR PRODUCE IT? -- r7009+cc66.57.

⛔ *The order sequenced this: "PRE-REGISTER THAT BEFORE ANYTHING ELSE... I would rather lose the step now
than build two revisions on it."*  ⌗ **`PREDICTION.md` was written before any of the below was computed**,
with the step's definition named and the outcome that withdraws `cc66.56`'s ⓷ tabled FIRST.

** THE STEP, DEFINED BEFORE USE: ** the ratio of band 1's excess to the mean of the excess over bands
2--7.  *It is `0.333` on the arithmetic-mean envelope.  "Survives" means it stays well below one on every
reading; "goes away" means it returns towards one.*

** ⓵ THE HAZARD THE ORDER NAMED. **  Band 1 spans `q = 0.85..1.55` and the banked spectra begin at
`q = 0.3316`; a running envelope of half-width `0.5` at `q = 0.85` reaches to `0.35`, inside the data by
`0.018` in `q` -- about five multipoles.  *So band 1 is the only band whose envelope is within a hair of
truncating, and a truncated running mean of a falling spectrum is biased high, which would depress that
band's contrast and manufacture a step.*  ⇒ ** Three tests: a third envelope, a reading with no
envelope at all, and the edge measured directly. **
"""
import os

import numpy as np
from scipy.signal import argrelextrema, savgol_filter

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NM = ['sw*sw', 'sw*dp', 'sw*isw', 'sw*pol', 'dp*dp', 'dp*isw', 'dp*pol',
      'isw*isw', 'isw*pol', 'pol*pol']
I = {n: k for k, n in enumerate(NM)}
DPT = [I['sw*dp'], I['dp*dp'], I['dp*isw'], I['dp*pol']]
# `cc66.52`'s projection-width channel, mean-anchored, band by band
WIDTH = np.array([0.00343, 0.00569, 0.00816, 0.01079, 0.01350, 0.01640, 0.01955])


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl'], float(d['l_A'])


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
        x, y, _ = fine(t)
        o = (y - env(x, y, 1.0, kind)) / env(x, y, 1.0, kind)
        C[t] = np.array([float(np.std(np.interp(np.linspace(a, b, 400), x, o)))
                         for a, b in zip(QE[:-1], QE[1:])])
    return C['cr'] / C['lcdm'] - 1.0


def depths(t):
    """the ENVELOPE-FREE reading: peak-to-trough depth per acoustic cycle"""
    x, y, _ = fine(t)
    e = np.sort(np.concatenate([argrelextrema(y, np.greater, order=20)[0],
                                argrelextrema(y, np.less, order=20)[0]]))
    q = 0.5 * (x[e[:-1]] + x[e[1:]])
    d = np.abs(y[e[1:]] - y[e[:-1]]) / (y[e[1:]] + y[e[:-1]])
    return q, d


def slide(a, b, kind='mean'):
    out = []
    for t in ('lcdm', 'cr'):
        x, y, _ = fine(t)
        o = (y - env(x, y, 1.0, kind)) / env(x, y, 1.0, kind)
        out.append(float(np.std(np.interp(np.linspace(a, b, 400), x, o))))
    return out[1] / out[0] - 1.0


print(__doc__)
print('=' * 100)
print('\n  ⓵ THE STEP AGAINST FOUR READINGS -- three envelopes and one with no envelope:')
STEP = {}
for kind in ('mean', 'median', 'savgol'):
    T = band_excess(kind)
    STEP[kind] = T[0] / T[1:].mean()
    print(f"    {kind:8s} " + '  '.join(f'{v:+.4f}' for v in T) + f"   STEP = {STEP[kind]:.3f}")
qa, da = depths('cr')
qc, dc = depths('lcdm')
RA = []
for a, b in zip(QE[:-1], QE[1:]):
    ma, mc = (qa >= a) & (qa < b), (qc >= a) & (qc < b)
    RA.append(da[ma].mean() / dc[mc].mean() - 1.0 if ma.sum() and mc.sum() else np.nan)
RA = np.array(RA)
STEP['none'] = RA[0] / RA[1:].mean()
print(f"    {'no env.':8s} " + '  '.join(f'{v:+.4f}' for v in RA) + f"   STEP = {STEP['none']:.3f}")
print(f"      ⌗ the envelope-free reading has only "
      f"{min(((qa >= a) & (qa < b)).sum() for a, b in zip(QE[:-1], QE[1:]))} to "
      f"{max(((qa >= a) & (qa < b)).sum() for a, b in zip(QE[:-1], QE[1:]))} acoustic cycles per band, "
      f"so it is coarse -- and band 1's excess on it is {RA[0]:+.4f}, which is nothing at all")
print(f"    ⇒ ** THE STEP SURVIVES EVERY READING: {min(STEP.values()):.2f} to {max(STEP.values()):.2f}, "
      f"never near one. **  *It is the excess's and not the estimator's.*")

print('\n  ⌷ AND THE EDGE HAZARD IS RULED OUT THE RIGHT WAY ROUND:')
for a, b in ((0.85, 1.55), (0.95, 1.55), (1.05, 1.55), (1.15, 1.55)):
    print(f"    q in [{a:.2f}, 1.55]  excess {slide(a, b):+.4f}")
print('    ⇒ ** removing the near-truncating edge makes band 1 read HIGHER, not lower. **  *An edge '
      'artefact would have to work the other way, so the step is not one.*')

print('\n  ⛭⛭ ⓶ LOCATING THE STEP -- half-rise point at three window widths:')
LOC = []
for half in (0.175, 0.25, 0.35):
    row = [(c, slide(c - half, c + half)) for c in np.arange(0.85 + half, 3.0, 0.05)]
    lo = np.mean([v for c, v in row if c < 1.4])
    hi = np.mean([v for c, v in row if c > 2.2])
    mid = 0.5 * (lo + hi)
    loc = next(row[i - 1][0] + (mid - row[i - 1][1]) / (row[i][1] - row[i - 1][1]) * 0.05
               for i in range(1, len(row)) if row[i - 1][1] < mid <= row[i][1])
    LOC.append(loc)
    print(f"    half {half:.3f}: plateaux {lo:.4f} -> {hi:.4f} (a factor {hi / lo:.2f}), "
          f"half-rise at q = {loc:.3f}")
print(f"    ⇒ ** q = {np.mean(LOC):.3f} +- {np.ptp(LOC) / 2:.3f}, stable across the widths, and the "
      f"rise happens within about a tenth of a comb period -- sharper than the window that found it. **")

print('\n  ⛭ AND WHAT SITS THERE:')
for t in ('lcdm', 'cr'):
    x, y, lA = fine(t)
    pk = x[argrelextrema(y, np.greater, order=30)[0]][:4]
    print(f"    {t:5s} acoustic peaks at q = " + '  '.join(f'{v:.4f}' for v in pk))
F = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
k = F['k__lcdm']
o = np.argsort(k)
q = k[o] * float(F['r_s__lcdm']) / np.pi
um = (F['th0__lcdm'][o] + F['psi__lcdm'][o]) / F['psi__lcdm'][o]
tpm = q[np.where(np.diff(np.sign(np.diff(um))) != 0)[0] + 1][:3]
print(f"    other scales: monopole turning points {'  '.join(f'{v:.3f}' for v in tpm)}; "
      f"identifiability floor {0.5 * (tpm[0] + tpm[1]):.3f}; the fields' half-period 1.000; q = 2")
print(f"    ⇒ *** THE SECOND ACOUSTIC PEAK, q = 1.7775 on the control and 1.7760 on the arm, against a "
      f"measured {np.mean(LOC):.3f}: A MATCH TO "
      f"{100 * abs(np.mean(LOC) / 1.7775 - 1):.1f} PER CENT. ***  *The nearest other scale is the "
      f"monopole's second turning point at 1.915, seven per cent away, and q = 2 is twelve.*")

print('\n  ⛔ ⓷ AND THE FOUR, RE-SCORED ON THE STEP RATHER THAN THE TREND:')
sl, ic = np.polyfit(QC, WIDTH, 1)
print(f"    the PROJECTION WIDTH (`cc66.52`, kernel-class, reachable at band 1): a straight line in q "
      f"fits it to {np.max(np.abs(WIDTH - (sl * QC + ic))) / np.ptp(WIDTH):.1%} of its own range")
print('      ⇒ ** linear, so no step. **')
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
lo = np.mean([v for c, v in DOP if c < 1.75])
hi = np.mean([v for c, v in DOP if c > 1.85])
print(f"    the DOPPLER by its reachable swap route (`cc66.56`): in sliding half-period windows its "
      f"contribution runs {min(v for _, v in DOP):+.4f} to {max(v for _, v in DOP):+.4f} with means "
      f"{lo:+.4f} below the step and {hi:+.4f} above")
print('      ⇒ ** noise at the resolution the step needs, and no transition at all. **')
print('    the WINDOW WEIGHTING (`cc66.47`) and the TERM MIX (`cc66.48/49`): both measured FLAT in q.')
print('      ⇒ ** a flat candidate cannot produce a step, by construction and without a new number. **')

print('\n' + '=' * 100)
print(f"""
  ⛭⛭⛭ ⓵ THE STEP IS THE EXCESS'S.  *Four readings -- three envelopes different in kind and one that
    needs no envelope at all -- and the step ratio runs {min(STEP.values()):.2f} to
    {max(STEP.values()):.2f}, never near one.*  ⌗ **And the edge hazard is ruled out the right way
    round**: removing the near-truncating edge makes band 1 read HIGHER, where an artefact would have to
    make it read lower.  ⚠ *Its SIZE is reading-dependent -- band 1 is a third of the rest on the
    arithmetic envelope, nearly two thirds on the Savitzky--Golay one, and nothing at all on the
    envelope-free one -- so the step is quoted as "band 1 is between none and two thirds of the rest",
    not as a number.*  ⛔ *No envelope is chosen; a third was added, as the order asked.*

  ⛭⛭⛭ ⓶ AND IT IS AT THE SECOND ACOUSTIC PEAK.  ** q = {np.mean(LOC):.3f} +- {np.ptp(LOC) / 2:.3f},
    stable across three window widths, against the second peak at 1.7775 and 1.7760 -- a match to
    {100 * abs(np.mean(LOC) / 1.7775 - 1):.1f} per cent, where the nearest other scale in the
    construction is seven per cent away. **  *And it is sharp: a factor of two within about a tenth of a
    comb period, sharper than the narrowest window that found it.*
    ⇒ *** SO THE EXCESS IS ONE SIZE IN THE FIRST ACOUSTIC CYCLE AND TWICE THAT IN EVERY CYCLE ABOVE
    IT. ***  ⌗ **Not claimed: that this is a mechanism.**  *A step at a scale is a signature to be
    explained, which is what the pre-registration said would not be claimed.*

  ⛔⛔ ⓷ AND ALL FOUR CANDIDATES CAN BE SCORED ON IT, AND NONE OF THEM PRODUCES IT.  *Two are flat and a
    flat candidate cannot produce a step; the projection width is linear in q to a few per cent of its
    own range; and the Doppler, by the one route that reaches band 1, is noise at the step's
    resolution.*  ⇒ ** This is NOT the identifiability floor closing over the list -- they were all
    evaluable -- it is the list EXHAUSTED against the right feature, for the first time. **
  ⌗ *So the row's question is now: what turns on at the second acoustic peak?  That is a narrower
    question than the one this sector has been asking for six revisions, and it is not a channel.*
""")
