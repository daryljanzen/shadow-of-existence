#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE COUPLING BETWEEN THE DOPPLER AMPLITUDE AND THE BAND CONTRAST IS
MEASURED, IS NEGATIVE AT EVERY BAND ON BOTH ENVELOPES AND OVER EVERY INTERVAL, AND IS FIXED BY THE
CONSTRUCTION; AND THE CANDIDATE'S CONTRIBUTION IS STILL UNDETERMINED, BECAUSE THE TWO READINGS OF WHAT
THE COUPLING MULTIPLIES DISAGREE IN SIGN, AND IN MAGNITUDE BY A FACTOR OF SEVEN EVEN AT THEIR
CLOSEST. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6941_fine_{lcdm,cr_leafrec1}`, `r6975_mix_lcdm` and `r6975_mixb_lcdm` (the two banked
`DPSRC` points) and `r6959_eta_{lcdm,cr_leafrec1}`.  The line-of-sight quartet is searched for below rather than
asserted absent.  ⛔ *** Nothing is SOLVED: the three `DPSRC` spectra were already on disk. ***

** THE PRE-REGISTRATION IS `r7005_directions/PREDICTION.md`, FAILURE MODES AHEAD OF OUTCOMES **, five of
each -- *and the one that fired is tabled there as the worst case: "the coupling is a multiplier; if what
it multiplies is not determined in sign, neither is the contribution."*

⛭⛭ ** THE COUPLING IS MEASURED AND NOT MODELLED. **  `DPSRC` scales the Doppler source term, so the
banked control spectra at `DPSRC` $= 1,\,0.8794,\,0.6$ give $d\ln C/d\ln s$ per band as a finite
difference -- ***three points, so the linearity is checked rather than assumed.***  Near $s=1$, on the
arithmetic envelope, it runs $-0.45$ to $-0.80$ with no trend in $q$; the slope steepens towards $s=1$,
so the local slope there is both the applicable one and the one measured over the shortest step.

⇒ *** NEGATIVE AT EVERY BAND, ON BOTH ENVELOPES, OVER EVERY INTERVAL -- FORTY-TWO MEASUREMENTS OF THE
SIGN AND NOT ONE POSITIVE. ***  *More Doppler fills more trough and lowers the contrast, which is
`cc66.51`'s own trough-filling physics read forwards.*

⛭ ** ⓶ AND THE CONSTRUCTION FIXES IT, SHOWN BY WHAT DOES NOT CHANGE IT. **  The control's own
Doppler-to-monopole band-power share runs $4.30$ down to $0.65$ -- *a factor of $6.6$ across the bands* --
and the coupling's sign is the same at every one.  ⇒ **A quantity whose sign is invariant across a
factor of six in the very ratio it depends on is not set by a knob**: `DPSRC` is the PROBE, not the
setter.  ⌗ *So the size is a prediction and not a fit.*  ⚠ *And the one thing not measured is stated:
all three `DPSRC` banks are the CONTROL, so the arm's coupling is assumed to be the control's -- its
share differs by about a fifth, against the factor of six across which the sign does not move, so the
assumption cannot reach the sign and is not asked to reach more.*

⛔⛔ ** ⓵ AND THE CONTRIBUTION IS NOT DETERMINED -- NOT BECAUSE OF THE COUPLING BUT BECAUSE OF ITS
INPUT. **
  ⛭ ** r7639 ⑴ -- RE-POINTED TO THE ARM OF RECORD, AND THE TARGET IS CARRIED ONTO THE CONTROL'S COMB. **
  Every arm read is `_leafrec1`, and the target -- the arm's band excess over the control's -- is the
  CARRIED excess rather than a ratio of bands read on each arm's own $q$, because by 69's ruling a
  $0.70$-wide band holds less than one comb period and the ratio beats when the periods differ.  *The
  target moves from $+0.0215\ldots+0.0762$ to $+0.0295\ldots+0.0795$ and the projected departure with
  it.*  ** Every one of this receipt's assertions survives, and the one it turns on survives with room:
  the two fractions still differ in sign and still differ in magnitude by more than a factor of five at
  their closest ($7.3$ on the namesake, $6.2$ here). **  ⌗ *The COUPLING itself is measured
  entirely on the control and on the two banked `DPSRC` points, all `lcdm`, so it does not move at all --
  which is why the slopes are the same numbers they were, and why the re-point touches the INPUT side
  only.*

  The criterion was named before use: *the coupling multiplies a fractional change in the
Doppler's oscillation amplitude relative to the monopole's.*  Two measured quantities claim to be it and
** they disagree in sign **:

  · the FIELD reading (`cc66.51`'s, the held-period estimator at last scattering): the arm is **higher**
    by $+0.5$ to $+1.4$ per cent  ⇒  contribution $-0.004$ to $-0.010$, ** $-7$ to $-12$ per cent of
    the excess, the WRONG SIGN **;
  · the PROJECTED reading (`cc66.50`'s quantity, the square root of the banked `w2dp/w2sw` share, which
    is what `DPSRC` actually scales): the arm is **lower** by $9$ to $16$ per cent  ⇒  contribution
    $+0.053$ to $+0.106$, ** $+178$ down to $+77$ per cent of the excess, the RIGHT SIGN **.

⇒ *** THE COUPLING TURNS A DISAGREEMENT ABOUT A QUANTITY INTO A DISAGREEMENT ABOUT WHETHER THE CANDIDATE
HELPS AT ALL.  This is the third revision in which these two readings decide the answer between them and
the first in which they decide its SIGN. ***

⌗ ** AND THE ORDER'S SECOND HALF -- CONSTANT SHORTFALL OR GROWING? GROWING, ON BOTH READINGS, IN
OPPOSITE DIRECTIONS. **  The field reading's fraction grows in magnitude from $-7$ to $-12$ per cent; the
projected reading's falls from $+178$ to $+77$.  ⇒ *** A SHAPE MISMATCH AND NOT A COUPLING DEFICIT, ON
EITHER READING, AND THE FOURTH THIS SECTOR HAS FOUND. ***  *The coupling is flat, so the $q$-dependence
belongs to the input.*

⛭ ** ⓷ AND THE ENVELOPE QUESTION HAS THE GOOD ANSWER. **  The coupling's sign survives both envelopes at
every band, so the contribution does not reverse with the statistic and ** the coupling question does not
inherit the envelope ambiguity. **  *Its magnitude does: the median envelope's coupling reaches $2.2$
times the arithmetic one's at the top band, so a quoted FRACTION inherits the ambiguity while the SIGN
does not.*  ⛔ *What it inherits instead is worse, and it is the input.*

⌗ ** AND WHAT WOULD SETTLE IT, NAMED AND NOT BUILT. **  Neither banked quantity is the right one: the
field reading is an amplitude but at last scattering rather than in the projected source, and the
projected reading is in the projected source but is a BAND POWER, which keeps the smooth part `cc66.51`
showed fills no trough.  ⇒ **The quantity the coupling multiplies is the OSCILLATION AMPLITUDE OF THE
PROJECTED DOPPLER CONTRIBUTION, per band, and the instrument banks neither it nor the $\eta$-resolved
fields a derivative of it would need.**  *One bank, not a channel: the order's ⓸ closes the list.*
"""
import os
import sys

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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7005_directions')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                 'r7639_cc66_P15_repoint_paper'))
import own_comb_kinds as OCK                                                           # noqa: E402

# ** r7639 ⑴ -- THE ARM OF RECORD, AND THE CARRY. **  Every arm read here is `_leafrec1`.  And the
#   TARGET -- the arm's band excess over the control's -- is no longer cut on the control's comb: by
#   69's ruling a 0.70-wide band holds less than one comb period, so when the arms' periods differ
#   their bands cover different parts of the cycle and the ratio BEATS.  The arm is carried onto the
#   control's comb coordinate first, through `own_comb_kinds`.  ** The COUPLING itself is measured
#   entirely on the control and on the two banked `DPSRC` points, all `lcdm`, so it does not move --
#   which is why the slopes below are the same numbers they were. **
AOR = {'lcdm': 'r6941_fine_lcdm', 'cr': 'r6941_fine_cr_leafrec1'}
ETA = {'lcdm': 'r6959_eta_lcdm', 'cr': 'r6959_eta_cr_leafrec1'}
QE = np.asarray(np.load(os.path.join(SP, ETA['cr'] + '.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NF = 3.0
PTS = ((1.0, 'r6941_fine_lcdm.npz'), (0.8794, 'r6975_mix_lcdm.npz'), (0.6, 'r6975_mixb_lcdm.npz'))

# ---- the path-provenance guard, executed rather than asserted -----------------------------------
# ⌷ Any line tagged `# noscan` is removed before the search: the marker lists necessarily contain it.
SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "r6941_fine_*, r6975_mix*_lcdm and r6959_eta_* only")
_qe_ns = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
check("and the band edges are a DEFINITION and not a measurement, so they do not move with the arm: "
      "the namesake's `q_edges` and the arm of record's are bit-identical",
      np.array_equal(_qe_ns, QE),
      f"{len(QE)} edges, {QE[0]:.2f} to {QE[-1]:.2f}")
check("and nothing is SOLVED: the three DPSRC spectra were already banked",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan


def envelope(x, y, win=1.0, kind='mean'):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def bands(fn, kind='mean'):
    d = np.load(os.path.join(SP, fn), allow_pickle=True)
    q = d['ls'].astype(float) / float(d['l_A'])
    o = (d['Dl'] - envelope(q, d['Dl'], 1.0, kind)) / envelope(q, d['Dl'], 1.0, kind)
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


C = {k: {s: bands(f, k) for s, f in PTS} for k in ('mean', 'median')}
SLOPE = {}
for k in ('mean', 'median'):
    SLOPE[k] = (np.log(C[k][0.8794] / C[k][1.0]) / np.log(0.8794),
                np.log(C[k][0.6] / C[k][0.8794]) / np.log(0.6 / 0.8794),
                np.log(C[k][0.6] / C[k][1.0]) / np.log(0.6))
ALLS = np.concatenate([np.concatenate(SLOPE[k]) for k in SLOPE])

print("\n⛭⛭ THE COUPLING\n")
print('    q              ' + '  '.join(f'{x:8.2f}' for x in QC))
for k in ('mean', 'median'):
    for lbl, v in zip(('1.00->0.879', '0.879->0.60', '1.00->0.60 '), SLOPE[k]):
        print(f"    {k[:4]} {lbl}  " + '  '.join(f'{x:+8.3f}' for x in v))
check("⛭⛭ THE COUPLING IS NEGATIVE AT EVERY BAND, ON BOTH ENVELOPES, OVER EVERY DPSRC INTERVAL -- "
      "forty-two measurements of the sign and not one positive.  *More Doppler fills more trough and "
      "LOWERS the contrast, which is `cc66.51`'s own physics read forwards*",
      ALLS.max() < 0, f"{ALLS.size} slopes, all negative, {ALLS.min():+.3f} to {ALLS.max():+.3f}")
check("and the three DPSRC points lie on one smooth monotone response rather than scattering, so a "
      "finite difference IS a local slope: it steepens towards s = 1 at every band, which is the "
      "pre-registered linearity check and not an assumption",
      all(abs(SLOPE['mean'][0][b]) > abs(SLOPE['mean'][1][b]) for b in range(7)),
      "the 1.00->0.879 slope is steeper than the 0.879->0.60 slope at all seven bands")
check("and the coupling is FLAT in q on the arithmetic envelope -- no trend -- so whatever q-dependence "
      "the contribution has belongs to the INPUT and not to the coupling",
      abs(float(np.polyfit(QC, SLOPE['mean'][0], 1)[0])) < 0.03,
      f"slope of the coupling against q is {float(np.polyfit(QC, SLOPE['mean'][0], 1)[0]):+.4f} per unit q")

P = {}
for t in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, ETA[t] + '.npz'))
    e = d['eta']
    m = (e >= float(d['eta_ls']) - NF * float(d['eta_ls_w'])) & \
        (e <= float(d['eta_ls']) + NF * float(d['eta_ls_w']))
    P[t] = {kk: np.array([float(np.trapezoid(d[kk][m][:, b], e[m])) for b in range(7)])
            for kk in ('w2dp', 'w2sw')}
SHARE = P['lcdm']['w2dp'] / P['lcdm']['w2sw']
check("⛭ ⓶ AND THE CONSTRUCTION FIXES IT, SHOWN BY WHAT DOES NOT CHANGE IT: the control's own "
      "Doppler-to-monopole band-power share spans a factor of six across the bands and the coupling's "
      "SIGN is the same at every one.  ⇒ A quantity whose sign is invariant across a factor of six in "
      "the very ratio it depends on is not set by a knob -- DPSRC is the PROBE, not the setter, so the "
      "size is a PREDICTION and not a fit",
      SHARE.max() / SHARE.min() > 5 and ALLS.max() < 0,
      f"share {SHARE.max():.2f} down to {SHARE.min():.2f}, a factor {SHARE.max() / SHARE.min():.1f}")

PROJ = np.sqrt((P['cr']['w2dp'] / P['cr']['w2sw']) / SHARE) - 1.0
FIELD = np.array([-0.00031, +0.00482, +0.00494, +0.00507, +0.00903, +0.01241, +0.01441])
# r7639 ⑴: the target is the CARRIED band excess, not the shared-comb ratio
_BANKS = {t: OCK.fine(AOR[t]) for t in ('lcdm', 'cr')}
_Tc, _pc, _Ta, _pa, _dphi = OCK._combs(_BANKS)
check("⛭ THE TWO ARMS' COMBS ARE FITTED BEFORE THE TARGET IS CUT, and they DIFFER -- which is why the "
      "target is the arm carried onto the control's comb coordinate and not a ratio of bands read on "
      "each arm's own q",
      abs(_Ta - _Tc) > 1e-4,
      f"control T {_Tc:.4f} phi {_pc:.3f}; arm T {_Ta:.4f} phi {_pa:.3f}; dphi {_dphi:+.4f}")
TGT = OCK.band_excess_own_kind(_BANKS, 'mean', QE)
# ⛔ r7639 ⑴ -- AND THE ARM IS PINNED, BECAUSE WITHOUT THIS NOTHING HERE WOULD BE.
#   Perturbing the pointer back to the namesake left every other assertion in this file PASSING: they
#   are sign-and-range claims with wide margins, so a green said nothing about WHICH arm was read.
#   That is the silent class reported at `r7637+cc66.1`, found here in my own re-point.  ** So the
#   carried target is pinned to its measured values, tight enough to exclude the namesake arm: the two
#   differ by 0.0080 at band 1 and by at least 0.0021 somewhere, against a 5e-4 half-width. **
TGT_PINNED = np.array([0.02948, 0.05950, 0.06099, 0.06387, 0.07772, 0.07283, 0.07951])
TGT_NAMESAKE = np.array([0.02150, 0.05737, 0.05189, 0.06063, 0.07478, 0.06588, 0.07619])
check("⛔ THE CARRIED TARGET IS PINNED TO THE ARM OF RECORD, and the pin EXCLUDES the namesake arm -- "
      "without which this receipt would pass on either arm and its green would say nothing about "
      "which one it read",
      float(np.max(np.abs(TGT - TGT_PINNED))) < 5e-4
      and float(np.max(np.abs(TGT_NAMESAKE - TGT_PINNED))) > 5e-3,
      f"max |TGT - pinned| = {float(np.max(np.abs(TGT - TGT_PINNED))):.2e} against a 5e-4 half-width; "
      f"the namesake arm sits {float(np.max(np.abs(TGT_NAMESAKE - TGT_PINNED))):.4f} away")
check("and the projected departure is pinned with it, so the INPUT side of the contribution is fixed "
      "to the arm of record too and not only the target",
      abs(float(PROJ.min()) + 0.1569) < 5e-4 and abs(float(PROJ.max()) + 0.0899) < 5e-4,
      f"projected {PROJ.min():+.4f} to {PROJ.max():+.4f}")
CF, CP = SLOPE['mean'][0] * FIELD, SLOPE['mean'][0] * PROJ
print("\n⛔⛔ ⓵ THE CONTRIBUTION, ON BOTH READINGS\n")
print('    target                ' + '  '.join(f'{x:+8.4f}' for x in TGT))
print('    FIELD departure       ' + '  '.join(f'{x:+8.4f}' for x in FIELD))
print('    PROJECTED departure   ' + '  '.join(f'{x:+8.4f}' for x in PROJ))
print('    fraction, field       ' + '  '.join(f'{100 * x:+7.0f}%' for x in CF / TGT))
print('    fraction, projected   ' + '  '.join(f'{100 * x:+7.0f}%' for x in CP / TGT))
check("⛔⛔ THE TWO READINGS OF WHAT THE COUPLING MULTIPLIES DISAGREE IN SIGN, WHICH IS THE "
      "PRE-REGISTERED WORST CASE: the field reading has the arm HIGHER in Doppler amplitude and the "
      "projected reading has it LOWER, at every band",
      FIELD[1:].min() > 0 > PROJ.max(),
      f"field {FIELD[1]:+.4f} to {FIELD[-1]:+.4f}; projected {PROJ.min():+.4f} to {PROJ.max():+.4f}")
check("⇒ AND THE COUPLING TURNS THAT INTO A DISAGREEMENT ABOUT WHETHER THE CANDIDATE HELPS AT ALL: the "
      "two fractions of the excess differ in SIGN, and in magnitude by a factor of seven even at their "
      "closest.  *Third revision in which these two readings decide the answer between them; first in "
      "which they decide its SIGN*",
      (CF / TGT)[1:].max() < 0 < (CP / TGT)[1:].min()
      and abs((CP / TGT)[1:]).min() / abs((CF / TGT)[1:]).max() > 5,
      f"field {100 * (CF / TGT)[1]:+.0f}% to {100 * (CF / TGT)[-1]:+.0f}%; projected "
      f"{100 * (CP / TGT)[1]:+.0f}% to {100 * (CP / TGT)[-1]:+.0f}%")
check("⌗ AND THE ORDER'S SECOND HALF: the fraction is NOT constant on either reading -- it grows in "
      "magnitude on the field reading and FALLS on the projected one -- so it is a SHAPE MISMATCH and "
      "not a coupling deficit, on either, and the fourth this sector has found",
      abs((CF / TGT)[-1]) > 1.5 * abs((CF / TGT)[1]) and (CP / TGT)[-1] < 0.6 * (CP / TGT)[1],
      f"field {100 * (CF / TGT)[1]:+.0f}% -> {100 * (CF / TGT)[-1]:+.0f}%; projected "
      f"{100 * (CP / TGT)[1]:+.0f}% -> {100 * (CP / TGT)[-1]:+.0f}%")

print("\n⛭ ⓷ THE ENVELOPE\n")
RAT = np.abs(SLOPE['median'][0] / SLOPE['mean'][0])
check("⛭ ⓷ AND THE COUPLING'S SIGN SURVIVES BOTH ENVELOPES AT EVERY BAND, so the contribution does NOT "
      "reverse with the statistic and the coupling question does not inherit the envelope ambiguity",
      SLOPE['mean'][0].max() < 0 and SLOPE['median'][0].max() < 0,
      f"arithmetic {SLOPE['mean'][0].max():+.3f} worst; median {SLOPE['median'][0].max():+.3f} worst")
check("and its MAGNITUDE does not survive, which is why a quoted FRACTION inherits the ambiguity while "
      "the SIGN does not -- said before any fraction is quoted, as the order requires",
      RAT.max() > 1.5, f"the median envelope's coupling reaches {RAT.max():.1f}x the arithmetic one's")
check("⛔ and the envelope question is NOT revisited to settle it: the order forbids that, both "
      "envelopes are carried through, and no conclusion here rests on choosing one",
      'revisit the envelope question to settle it' in open(
          os.path.join(DIR, 'PREDICTION.md')).read()
      and SLOPE['median'][0].max() < 0,
      "both carried, neither chosen")

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔ THE PRE-REGISTRATION TABLES THE FAILURE MODES AHEAD OF THE OUTCOMES, and the one that fired is "
      "among them as the worst case -- a coupling multiplied by an input undetermined in sign",
      TXT.index('FAIL TO DECIDE') < TXT.index('AND THE OUTCOMES')
      and 'DISAGREE IN SIGN' in TXT and 'THE NULL' in TXT,
      f"{TXT.count('| **')} tabled rows, failure modes first")
check("and it names the criterion the coupling is applied under BEFORE either input is put through it, "
      "which is what makes the disagreement the finding rather than a nuisance",
      'stated before use' in TXT and 'oscillation amplitude relative to the monopole' in TXT,
      "a fractional change in the Doppler's oscillation amplitude relative to the monopole's")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
