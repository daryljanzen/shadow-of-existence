#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE BANK THE ROW NEEDED ALREADY EXISTED, SO THE ARM'S COUPLING IS NOW
MEASURED RATHER THAN TRANSFERRED; THE DOPPLER CARRIES A GROWING MINORITY OF THE EXCESS AND IS
SIGN-INDEFINITE AT THE BOTTOM; AND THE FOUR SHAPE MISMATCHES SHARE A REASON THAT IS ABOUT THE EXCESS
AND NOT ABOUT THE CANDIDATES. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6915_pairs_{lcdm,cr}` (the `SRCDEC` bilinear decomposition), `r6941_fine_*` and
`r6959_eta_cr`'s band edges.  ⛔ *** Nothing is SOLVED and nothing is RUN: the bank was already on
disk. ***

** THE PRE-REGISTRATION IS `r7007_directions/PREDICTION.md` **, five failure modes ahead of five
outcomes, ** with "the right quantity lands between the two wrong ones and settles nothing" tabled first
** on the order's instruction, and with the failed first construction dated as failed.

⛭⛭ ** ⓵ THE INSTRUMENT ALREADY EMITS THE RIGHT QUANTITY AND THE BANK IS ALREADY ON DISK. **  `SRCDEC`,
added at `r6915+cc66.41`, writes the full bilinear decomposition -- with $\Delta^a_\ell(k) = \int
\text{term}_a\, j_\ell\, d\eta$, $C_\ell = \sum_{a\le b} w_{ab} \sum_k P\, \Delta^a \Delta^b$ -- ***ten
numbers per multipole summing to $C_\ell$ exactly***, and `r6915_pairs_{lcdm,cr}` carry them for both
arms.  ⇒ ** No run, no instrument change, and the order's escape hatch is not needed. **  ⌗ *The grid
is $238$ multipoles against the fine banks' $1900$: it reads the contrast $1.9$ per cent low, and the
deficit agrees between the arms to three parts in ten thousand, so it CANCELS in the ratio -- which is
the only thing read from it.*

⛭ ** AND THE BANK DISCHARGES A CAVEAT `cc66.55` COULD ONLY STATE. **  The $s$-scaling of every pair is
exact -- $s^2$ on `dp*dp`, $s$ on the three `dp` crosses, $1$ on the rest -- so
$dD_\ell/d\ln s = (\texttt{sw*dp} + \texttt{dp*isw} + \texttt{dp*pol}) + 2\,\texttt{dp*dp}$ per
multipole, and the coupling follows analytically ***for the arm as well as the control***: $-0.48$ to
$-0.86$ on each, **equal between the arms to four per cent** and agreeing with `cc66.55`'s three-point
finite difference to seven.  ⇒ *`cc66.55` measured it on the control and transferred it; that caveat
is discharged.*

⚠ ** AND ONE CONSTRUCTION WAS TRIED FIRST AND IS REPORTED AS FAILED RATHER THAN DROPPED. **  The obvious
reading of the quantity, $\sqrt{\mathrm{osc}(\texttt{dp*dp})/\mathrm{osc}(\texttt{sw*sw})}$ per band, is
small and sign-indefinite on the arithmetic envelope and reaches $+134$ per cent under a median one --
*because the oscillation of a weak, smooth term about a median envelope is not a well-conditioned
quantity.*  ⇒ ** That definition inherits the envelope ambiguity through its own conditioning, so it
is not used, and the failure is dated in the pre-registration. **

⛭⛭ ** WHAT IS USED NEEDS NO EQUIVALENT-$s$ STEP: A ONE-AT-A-TIME SWAP. **  On the arm's own $q$ grid,
replace the arm's four Doppler-containing pairs by the control's, scaled by the ratio of the two arms'
envelopes, and recompute the contrast.  The Doppler's share is then $(C_{\rm arm} - C_{\rm
swapped})/(C_{\rm arm} - C_{\rm control})$ -- *a direct attribution with no coupling-times-input product
in it, and the same shape of operation as `SRCINJRS`'s one-at-a-time clock swap.*

⛔ ** ⓶ AND THE CONTRIBUTION IS A MINORITY SHARE THAT GROWS, SIGN-INDEFINITE AT THE BOTTOM. **
$-12$ to $+17$ per cent on the arithmetic envelope and $-20$ to $+48$ on the median one -- negative at
$q=1.90$ on both, rising to a fifth or a half by the top band.  ⇒ *** IT LANDS BETWEEN THE TWO WRONG
READINGS, WHICH SAID $-13$ AND $+188$ PER CENT -- AND IT DOES NOT SETTLE NOTHING: it settles that the
candidate is a real but MINORITY contributor, which neither wrong reading said. ***  ⌗ *`cc66.55`'s
split holds exactly as predicted: the coupling's SIGN is envelope-independent and the FRACTION inherits
the ambiguity, by about a factor of two.*  ⛔ *No envelope is chosen -- the order's standing refusal.*

⛭⛭⛭ ** ⓷ AND THE FOUR MISMATCHES DO SHARE A REASON, AND IT IS ABOUT THE EXCESS. **  The excess has ONE
dominant feature: ***band 1 is a third of the mean of the rest and sits five scatters below it***, while
above band 1 a constant already fits and a line only halves the residual.  ⇒ *** THE EXCESS'S
$q$-STRUCTURE IS A STEP AT THE LOWEST BAND, NOT A TREND -- AND ALL FOUR CANDIDATES WERE JUDGED ON A
TREND ACROSS BANDS 2--7, WHERE THE EXCESS IS VERY NEARLY FEATURELESS. ***  *A flat candidate (the window
weighting, the term mix, the band-power reading) matches the flat part and misses the step; a rising one
(the projection width, the field reading) matches the mild rise and misses the step, and on bands 2--7
the two are barely distinguishable because there is almost nothing there to distinguish them with.*
⇒ ** So the sector has been spending its discriminating power on the part of the excess carrying least
structure, because the part carrying the structure is the band `cc66.54` showed it cannot measure a
candidate in. **  ⌗ *Which is `cc66.54`'s own finding seen from the candidate side, and it is why four
mismatches look like four failures rather than one.*
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7007_directions')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NM = ['sw*sw', 'sw*dp', 'sw*isw', 'sw*pol', 'dp*dp', 'dp*isw', 'dp*pol',
      'isw*isw', 'isw*pol', 'pol*pol']
I = {n: k for k, n in enumerate(NM)}
DPT = [I['sw*dp'], I['dp*dp'], I['dp*isw'], I['dp*pol']]

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "r6915_pairs_*, r6941_fine_* and r6959_eta_cr's band edges only")
check("and nothing is SOLVED and nothing is RUN: the bank was already on disk",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan


def env(x, y, win=1.0, kind='mean'):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def cb(q, y, kind='mean'):
    e = env(q, y, 1.0, kind)
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, (y - e) / e)))
                     for a, b in zip(QE[:-1], QE[1:])])


def pairs(t):
    d = np.load(os.path.join(SP, f'r6915_pairs_{t}.npz'), allow_pickle=True)
    return d['ls'].astype(float) / float(d['l_A']), d['Dl'], d['Dl_pairs'], [str(x) for x in d['pairs']]


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


print("\n⛭⛭ ⓵ THE BANK\n")
EX = {t: pairs(t) for t in ('lcdm', 'cr')}
check("⛭⛭ THE INSTRUMENT ALREADY EMITS THE RIGHT QUANTITY: `SRCDEC`'s bilinear decomposition is on disk "
      "for BOTH arms, ten l-resolved terms per multipole in the order the instrument fixes, and they sum "
      "to Dl exactly.  ⇒ No run, no instrument change, and the order's escape hatch is not needed",
      all(np.max(np.abs(EX[t][2].sum(axis=1) / EX[t][1] - 1)) < 1e-12 for t in EX)
      and all(EX[t][3] == NM for t in EX),
      f"max relative departure from Dl is {max(np.max(np.abs(EX[t][2].sum(axis=1) / EX[t][1] - 1)) for t in EX):.1e}")
RC = cb(*pairs('lcdm')[:2]) / cb(*fine('lcdm'))
RA = cb(*pairs('cr')[:2]) / cb(*fine('cr'))
check("and the coarse grid is CHECKED rather than assumed adequate: it reads the contrast about two per "
      "cent low, and the deficit agrees between the arms to parts in ten thousand -- so it CANCELS in "
      "the ratio, which is the only thing read from it",
      0.97 < RC.mean() < 0.99 and np.max(np.abs(RA / RC - 1)) < 1e-3,
      f"coarse/fine {RC.mean():.4f} on the control, and arm-against-control to "
      f"{np.max(np.abs(RA / RC - 1)):.1e}")


def analytic_coupling(t, kind='mean'):
    q, Dl, P, _ = pairs(t)
    dD = P[:, I['sw*dp']] + P[:, I['dp*isw']] + P[:, I['dp*pol']] + 2 * P[:, I['dp*dp']]
    eps = 1e-3
    return (cb(q, Dl + eps * dD, kind) / cb(q, Dl, kind) - 1.0) / eps


AC = {t: analytic_coupling(t) for t in ('lcdm', 'cr')}
FD = np.array((-0.450, -0.804, -0.585, -0.614, -0.674, -0.544, -0.678))   # cc66.55's finite difference
print('    q            ' + '  '.join(f'{x:8.2f}' for x in QC))
for t in ('lcdm', 'cr'):
    print(f"    {t:5s}        " + '  '.join(f'{x:+8.3f}' for x in AC[t]))
check("⛭ AND THE BANK DISCHARGES A CAVEAT cc66.55 COULD ONLY STATE: the s-scaling of every pair is "
      "exact, so the coupling follows ANALYTICALLY for the ARM as well as the control -- negative at "
      "every band on both, equal between the arms to a few per cent, and agreeing with cc66.55's "
      "three-point finite difference",
      AC['lcdm'].max() < 0 and AC['cr'].max() < 0
      and np.max(np.abs(AC['cr'] / AC['lcdm'] - 1)) < 0.06
      and np.max(np.abs(AC['lcdm'] / FD - 1)) < 0.10,
      f"arm against control to {100 * np.max(np.abs(AC['cr'] / AC['lcdm'] - 1)):.0f}%, both against the "
      f"finite difference to {100 * np.max(np.abs(AC['lcdm'] / FD - 1)):.0f}%")


def osc(q, y, kind='mean'):
    r = y - env(q, y, 1.0, kind)
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, r)))
                     for a, b in zip(QE[:-1], QE[1:])])


def failed_quantity(kind='mean'):
    o = {}
    for t in ('lcdm', 'cr'):
        q, _, P, _ = pairs(t)
        o[t] = np.sqrt(osc(q, P[:, I['dp*dp']], kind) / osc(q, P[:, I['sw*sw']], kind))
    return o['cr'] / o['lcdm'] - 1.0


FQ, FQM = failed_quantity('mean'), failed_quantity('median')
check("⚠ AND THE FIRST CONSTRUCTION IS REPORTED AS FAILED RATHER THAN DROPPED: sqrt(osc(dp*dp) / "
      "osc(sw*sw)) is small on the arithmetic envelope and runs away under a median one, because the "
      "oscillation of a weak, smooth term about a median envelope is not well conditioned.  ⇒ That "
      "definition inherits the envelope ambiguity through its OWN conditioning, so it is not used",
      np.abs(FQ).max() < 0.02 and FQM.max() > 0.5,
      f"arithmetic |delta| <= {np.abs(FQ).max():.4f}; median reaches {FQM.max():+.3f}")


def swap_fraction(kind='mean'):
    qa, Da, Pa, _ = pairs('cr')
    qc, Dc, Pc, _ = pairs('lcdm')
    scale = env(qa, Da, 1.0, kind) / np.interp(qa, qc, env(qc, Dc, 1.0, kind))
    Dsw = Da - Pa[:, DPT].sum(axis=1) + np.interp(qa, qc, Pc[:, DPT].sum(axis=1)) * scale
    Ca, Cc, Cs = cb(qa, Da, kind), cb(qc, Dc, kind), cb(qa, Dsw, kind)
    return Ca, Cc, Cs, (Ca - Cs) / (Ca - Cc)


print("\n⛔ ⓶ THE CONTRIBUTION, BY ONE-AT-A-TIME SWAP\n")
FR = {}
for kind in ('mean', 'median'):
    Ca, Cc, Cs, fr = swap_fraction(kind)
    FR[kind] = fr
    print(f"    {kind:7s} excess " + '  '.join(f'{x:+8.4f}' for x in Ca - Cc)
          + '   fraction ' + '  '.join(f'{100 * x:+6.0f}%' for x in fr))
check("⛭⛭ THE SWAP NEEDS NO EQUIVALENT-s STEP, which is why it replaces the failed definition: the "
      "arm's four Doppler-containing pairs are replaced by the control's, envelope-scaled, on the arm's "
      "own q grid, and the share is a ratio of contrast differences",
      len(DPT) == 4 and all(NM[i].count('dp') >= 1 for i in DPT)
      and not any('dp' in NM[i] for i in range(10) if i not in DPT),
      "the four Doppler-containing pairs are exactly sw*dp, dp*dp, dp*isw, dp*pol")
check("⛔ AND THE CONTRIBUTION IS A MINORITY SHARE, ON BOTH ENVELOPES: well under half of the excess at "
      "every band on the arithmetic envelope and under half on the median one.  ⇒ THE CANDIDATE IS NOT "
      "THE CARRIER",
      FR['mean'].max() < 0.5 and FR['median'].max() < 0.5,
      f"arithmetic peaks at {100 * FR['mean'].max():+.0f}%, median at {100 * FR['median'].max():+.0f}%")
check("and it GROWS with q and is SIGN-INDEFINITE at the bottom -- negative at q = 1.90 on both "
      "envelopes -- so it cannot be told from zero at the bands where the excess's own structure is",
      FR['mean'][1] < 0 and FR['median'][1] < 0
      and FR['mean'][-1] > abs(FR['mean'][1]) and FR['median'][-1] > abs(FR['median'][1]),
      f"band 2 {100 * FR['mean'][1]:+.0f}% and {100 * FR['median'][1]:+.0f}%; band 7 "
      f"{100 * FR['mean'][-1]:+.0f}% and {100 * FR['median'][-1]:+.0f}%")
check("⛭ AND IT LANDS BETWEEN THE TWO WRONG READINGS, which said -13 and +188 per cent -- the outcome "
      "the order told this seat to table first -- AND IT DOES NOT SETTLE NOTHING: a minority share is "
      "neither of them, and neither wrong reading said it",
      -0.13 < FR['mean'].min() and FR['mean'].max() < 0.94,
      f"the swap's share spans {100 * FR['mean'].min():+.0f}% to {100 * FR['mean'].max():+.0f}% against "
      f"-13% and +94..188%")
check("⌗ and cc66.55's split is confirmed rather than assumed: the coupling's SIGN is the same on both "
      "envelopes while the FRACTION moves by about a factor of two",
      AC['lcdm'].max() < 0 and analytic_coupling('lcdm', 'median').max() < 0
      and 1.5 < np.median(FR['median'] / FR['mean']) < 4,
      f"the median-envelope share is {np.median(FR['median'] / FR['mean']):.1f}x the arithmetic one")

print("\n⛭⛭⛭ ⓷ THE PATTERN IN THE FOUR MISMATCHES\n")
T = cb(*fine('cr')) / cb(*fine('lcdm')) - 1.0
sl, ic = np.polyfit(QC[1:], T[1:], 1)
print('    the excess   ' + '  '.join(f'{x:+8.4f}' for x in T))
check("⛭⛭⛭ THE EXCESS HAS ONE DOMINANT FEATURE AND IT IS NOT A TREND: band 1 is about a third of the "
      "mean of the rest and sits nearly five scatters below it",
      T[0] < 0.45 * T[1:].mean() and (T[1:].mean() - T[0]) / T[1:].std() > 4,
      f"band 1 is {T[0] / T[1:].mean():.2f} of the bands 2-7 mean, {(T[1:].mean() - T[0]) / T[1:].std():.1f} "
      f"scatters below")
check("and above band 1 a CONSTANT already fits: a line adds a mild slope and only halves the residual, "
      "so bands 2-7 carry very little structure to distinguish a flat candidate from a rising one.  ⇒ "
      "ALL FOUR MISMATCHES WERE JUDGED THERE, which is the reason they share -- the sector has been "
      "spending its discriminating power where the excess has least structure, because the part that "
      "has the structure is the band cc66.54 showed it cannot measure a candidate in",
      T[1:].std() < 0.2 * T[1:].mean() and np.std(T[1:] - (sl * QC[1:] + ic)) > 0.4 * T[1:].std(),
      f"constant leaves {T[1:].std():.4f} on a mean of {T[1:].mean():.4f}; a line leaves "
      f"{np.std(T[1:] - (sl * QC[1:] + ic)):.4f}")

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔ THE PRE-REGISTRATION TABLES THE FAILURE MODES AHEAD OF THE OUTCOMES, with 'settles nothing' "
      "among them as the order required, and it dates the failed first construction as failed",
      TXT.index('FAIL TO DECIDE') < TXT.index('AND THE OUTCOMES')
      and 'SETTLES NOTHING' in TXT and 'reported as failed rather than dropped' in TXT,
      f"{TXT.count('| **')} tabled rows, failure modes first")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
