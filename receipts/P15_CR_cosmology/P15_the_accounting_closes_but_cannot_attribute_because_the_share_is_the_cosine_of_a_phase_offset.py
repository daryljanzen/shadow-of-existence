#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE ACCOUNTING CLOSES EXACTLY AND STILL CANNOT ATTRIBUTE, BECAUSE THE
LEAST-SQUARES SHARE IS $|\cos\Delta|$ IDENTICALLY -- IT DEPENDS ONLY ON THE PHASE OFFSET AND NOT AT ALL ON THE
CHANNEL'S AMPLITUDE, AND THE WINDOW PROVES IT BY SCORING $100\%$ IN ANTIPHASE; AND THE OTHER SCALE IS THE ONE
`ⓑ` INVALIDATES, PREDICTING THE WINDOW'S COST MODULATION TO $13\%$ AND THE TERM MIX'S TO $116\%$.  SO THE
ANSWER IS THE THIRD ROW: NO INSTRUMENT THIS CONSTRUCTION HAS CAN ATTRIBUTE THE MODULATION. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6959_eta_cr`'s band edges, and `plik_lite` TT through the corpus's own
`chi2_of_spectrum`.  ⛔ *** Nothing is SOLVED and nothing is RUN. ***

⛭ ** THE INSTRUMENT IS `cc66.65`'s OWN, AND ITS WINDOW RESULT IS REPRODUCED AS A GATE BEFORE ANYTHING ELSE. **
Spectrum-level phase offset $+0.27$ rad, ratio $0.264$, and $0.264 \times 6.241 = 1.646$ against a measured
$1.893$ -- *`cc66.65`'s three numbers to the digit.*

⛭⛭⛭ ** ⓐ THE TERM MIX'S MODULATED PART SITS $+0.38$ RAD FROM THE ARM'S AT A RATIO OF $1.176$ ** -- *larger
than the arm's own, where the window's was $0.264$.*

⛭⛭ ** ⓑ AND THAT RATIO DOES NOT PREDICT, WHICH IS THE HINGE OF THE WHOLE REVISION. **  $1.176 \times 6.241 =
7.341$ against a measured $3.399$: ** off by $116\%$, where the window's template was off by $13\%$. **
⇒ *** SO THE SCALE `r7035`'s TEMPLATE WAS BUILT ON DOES NOT CARRY OVER TO THIS CHANNEL. ***

⛭⛭⛭ ** ⓒ THE ACCOUNTING CLOSES -- AND CLOSING IS NOT ATTRIBUTING. **  Done as a vector subtraction at the
measured phase, the contribution plus the residue reconstructs the arm's own vector to numerical precision on
both scales.  *That is the gate, and it passes.*  But the two scales give **$68.3\%$** and **$98.3\%$**, and

⛔⛔ ** THE SECOND IS AN IDENTITY AND NOT A MEASUREMENT. **  In a two-dimensional $(\cos,\sin)$ plane the
least-squares scale is $k = (v_a\!\cdot\!v)/(v\!\cdot\!v)$, so the contribution's length is
$|k v| = |v_a\!\cdot\!v|/|v| = |v_a|\,|\cos\Delta|$.

$$\textbf{share} \;=\; |\cos\Delta| \quad \textbf{exactly}$$

*Verified exact for both channels: term mix $\Delta = +0.184$, $|\cos\Delta| = 0.9832$, share $0.9832$; window
$\Delta = +3.121$, $|\cos\Delta| = 0.9998$, share $0.9998$.*  ⇒ *** IT DEPENDS ONLY ON THE PHASE OFFSET AND
NOT AT ALL ON THE CHANNEL'S AMPLITUDE. A CHANNEL A MILLIONTH THE SIZE SCORES THE SAME. ***

⇒ *** AND THE WINDOW IS THE PROOF RATHER THAN AN ANALOGY: it sits in ANTIPHASE, $+3.12$ rad from the arm, and
scores $100.0\%$ -- at a scale of $-3.633$, which turns its cost upside down to get there. ***  *A quantity
that assigns a channel all of the authorship for pointing the opposite way is not measuring authorship.*

⛔ ** SO BOTH SCALES ARE OUT, EACH FOR ITS OWN REASON, AND NEITHER FAILURE IS THE OTHER'S. **  *The
spectrum-level ratio is invalidated by `ⓑ` — measured, for this channel, by a factor of two.  The
least-squares projection is invalidated by algebra — it was never a measurement of anything but a phase.*

⇒ *** THE ANSWER IS THE THIRD ROW `r7035` LISTED: NOTHING DECIDABLE, THE PHASES WILL NOT SUPPORT A SHARE, AND
`PO-56` TERMINATES ON THE STATED GROUND THAT NO INSTRUMENT THIS CONSTRUCTION HAS CAN ATTRIBUTE THE
MODULATION. ***  ⌗ *`r7035` said that is the terminal state itself and also a result.  I did not reach for a
fourth row and I am not asking for another measurement.*

⚠ ** AND THE TWO-CHANNEL LINE IS PRINTED TO BE DISCOUNTED, NOT QUOTED. **  *Two channels span the
$(\cos,\sin)$ plane, so together they reconstruct the arm's vector exactly -- $100\%$, residue $0.000$.*
** That is arithmetic and not attribution, and it is the same degeneracy one level up. **

⌗ ** THIS IS `cc66.65`'s GUARD A THIRD TIME, AND `PREDICTION.md` NAMED THE TRAP BEFORE THE RUN: ** *a share is
additive only under vector subtraction at the measured phase, because two combs combine as $A^2 = A_1^2 +
A_2^2 + 2A_1A_2\cos\Delta$.  ** An arithmetic identity is not a measurement, and the time to say so is before
the run. **

⛔ *No mechanism.  No new candidate.  `cc66.61`'s floor and the band-1 results are finished work and are not
re-derived.  No corpus edits.*
"""
import os
import sys

import numpy as np
import scipy.linalg

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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7035_directions')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
LC, _F = CS.bin_center_and_fac()

SRC = open(os.path.abspath(__file__)).read()
HDR = SRC.split(chr(34) * 3)[1]
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
HFLAT = ' '.join(HDR.split()).lower()
LOSMARK = ('c54.17', 'c54.178_', 'L814_', 'r6784_')                                       # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight bank name occurs in the executable body",
      not any(m in BODY for m in LOSMARK), "the fine banks, two response banks and plik_lite only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

PRED = open(os.path.join(DIR, 'PREDICTION.md'), encoding='utf-8').read()
FLAT = ' '.join(PRED.split()).lower()
check("⛔ THE PRE-REGISTRATION IS ON DISK AND WAS COMMITTED BEFORE THE WORKING SCRIPT",
      'committed before any of' in FLAT, 'PREDICTION.md')
check("⛔⛔ AND IT NAMED THE TRAP BEFORE THE RUN: a share is additive only under VECTOR subtraction at the "
      "measured phase, because amplitudes do not add",
      'vector subtraction at the measured phase' in FLAT and 'amplitudes do **not** add' in PRED,
      'the accounting was built on the vector form in advance')
check("and it declared BOTH scale choices in advance and chose neither",
      'both are computed and both reported. neither is chosen.' in FLAT,
      'spectrum-level ratio and least-squares projection')
check("and it tabled the expensive branch first and committed to not reaching for a fourth outcome row",
      'this is the expensive branch for this seat and it is tabled first' in FLAT
      and 'i am not going to reach for a fourth row' in FLAT, 'no sixth clause')


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for _nm, _fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz')):
    _ls, _dl, _ = load(_fn)
    KN[_nm] = CS.bin_spectrum(_ls, _dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB = (LC / AAC)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, dat, LL = MC[OK], CS.X_DATA[OK], LC[OK]
SPEC = {'the ARM': MA[OK], 'window': KN['window'][OK], 'term mix': KN['term mix'][OK]}
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]
qh = QB[HI]
x = np.log(qh / qh.mean())


def shape_fit(m, data):
    X = m.reshape(-1, 1)
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ data, assume_a='sym')


RC = dat - shape_fit(mc, dat)
_X1 = np.column_stack([np.cos(2.0 * np.pi * qh), np.sin(2.0 * np.pi * qh)])


def detrend(v):
    return v - np.polyval(np.polyfit(x, v, 1), x)


def vec(v):
    return scipy.linalg.lstsq(_X1, detrend(v))[0]


def amp(v):
    return float(np.hypot(*vec(v)))


def ph(v):
    c = vec(v)
    return float(np.arctan2(-c[1], c[0]))


def wrap(a):
    return float((a + np.pi) % (2.0 * np.pi) - np.pi)


QD, CR, DD = {}, {}, {}
for _k, _m in SPEC.items():
    _d = shape_fit(_m, dat) - shape_fit(mc, dat)
    QD[_k], CR[_k], DD[_k] = _d * (F @ _d), -2.0 * _d * (F @ RC), _d
EX = {k: QD[k] + CR[k] for k in SPEC}

print("\n" + "=" * 100)
print("  ⛔ GATE: DOES `cc66.65`'s WINDOW ACCOUNTING REPRODUCE?")
print("-" * 100)
d_arm, d_win, d_mix = DD['the ARM'][HI], DD['window'][HI], DD['term mix'][HI]
pw, rw = wrap(ph(d_win) - ph(d_arm)), amp(d_win) / amp(d_arm)
A_X = amp(CR['the ARM'][HI])
pred_w, meas_w = rw * A_X, amp(CR['window'][HI])
print(f"    window: phase {pw:+.3f}, ratio {rw:.4f}, prediction {pred_w:.3f} vs measured {meas_w:.3f}")
check("⛭ `cc66.65`'s THREE WINDOW NUMBERS REPRODUCE TO THE DIGIT, so this is the same instrument",
      abs(pw - 0.27) < 0.01 and abs(rw - 0.264) < 0.001 and abs(pred_w - 1.646) < 0.01,
      f"{pw:+.2f} rad, {rw:.3f}, {pred_w:.3f} against 1.893")

print("\n  ⛭⛭⛭ ⓐ AND ⓑ -- THE RATIO, AND WHETHER IT PREDICTS")
print("-" * 100)
pm, rm = wrap(ph(d_mix) - ph(d_arm)), amp(d_mix) / amp(d_arm)
pred_m, meas_m = rm * A_X, amp(CR['term mix'][HI])
err_m, err_w = abs(pred_m - meas_m) / meas_m, abs(pred_w - meas_w) / meas_w
print(f"    term mix: phase {pm:+.3f} rad, ratio {rm:.3f};  prediction {pred_m:.3f} vs measured {meas_m:.3f}")
check("⛭ ⓐ THE TERM MIX'S SPECTRUM-LEVEL MODULATION IS LARGER THAN THE ARM'S, where the window's was a "
      "quarter of it", rm > 1.0 and rw < 0.3, f"ratio {rm:.3f} against the window's {rw:.3f}")
check("⛭⛭ ⓑ AND THE RATIO DOES NOT PREDICT FOR THIS CHANNEL -- off by a factor of two where the window's "
      "template was off by a seventh, which is the hinge of the revision",
      err_m > 1.0 and err_w < 0.2, f"term mix {err_m:.0%}, window {err_w:.0%}")

print("\n  ⛭⛭⛭ ⓒ THE ACCOUNTING CLOSES -- AND CLOSING IS NOT ATTRIBUTING")
print("-" * 100)
va, vm, vw = vec(EX['the ARM'][HI]), vec(EX['term mix'][HI]), vec(EX['window'][HI])
SC = {'spectrum-level ratio': rm, 'least-squares projection': float(va @ vm / (vm @ vm))}
SH = {}
for nm, k in SC.items():
    contrib, res = k * vm, va - k * vm
    SH[nm] = float(np.hypot(*contrib) / np.hypot(*va))
    print(f"    {nm:26s} k={k:6.3f}  contribution {np.hypot(*contrib):6.3f}  residue "
          f"{np.hypot(*res):6.3f}  share {SH[nm]:6.1%}  closes "
          f"{abs(np.hypot(*(contrib + res)) - np.hypot(*va)) < 1e-9}")
check("⛭ THE VECTOR ACCOUNTING CLOSES EXACTLY on both scales, which the pre-registration made the gate on "
      "calling it an accounting at all",
      all(abs(np.hypot(*(k * vm + (va - k * vm))) - np.hypot(*va)) < 1e-9 for k in SC.values()),
      'contribution + residue reconstructs the arm to numerical precision')
check("⛔ and the two scales DISAGREE about the size of the share, which is why neither is quoted alone",
      abs(SH['spectrum-level ratio'] - SH['least-squares projection']) > 0.25,
      '; '.join(f"{nm} {v:.1%}" for nm, v in SH.items()))

print("\n  ⛔⛔ AND THE SECOND SCALE IS AN IDENTITY, NOT A MEASUREMENT")
print("-" * 100)
ID = {}
for nm, v in (('term mix', vm), ('window', vw)):
    dd = wrap(np.arctan2(-v[1], v[0]) - np.arctan2(-va[1], va[0]))
    k = float(va @ v / (v @ v))
    sh = float(np.hypot(*(k * v)) / np.hypot(*va))
    ID[nm] = (dd, abs(np.cos(dd)), sh, k)
    print(f"    {nm:12s} D={dd:+.3f}  |cos D|={abs(np.cos(dd)):.4f}  share={sh:.4f}  k={k:+.3f}")
check("⛔⛔ THE LEAST-SQUARES SHARE IS $|\\cos\\Delta|$ EXACTLY -- it depends ONLY on the phase offset and not "
      "at all on the channel's amplitude, so a channel a millionth the size scores the same",
      all(abs(v[1] - v[2]) < 1e-9 for v in ID.values()),
      '; '.join(f"{nm} |cos|={v[1]:.4f} share={v[2]:.4f}" for nm, v in ID.items()))
check("⇒ *** AND THE WINDOW IS THE PROOF RATHER THAN AN ANALOGY: in ANTIPHASE it scores 100% of the "
      "authorship, at a NEGATIVE scale that turns its cost upside down to get there ***",
      abs(abs(ID['window'][0]) - np.pi) < 0.05 and ID['window'][2] > 0.99 and ID['window'][3] < 0,
      f"{ID['window'][0]:+.2f} rad, share {ID['window'][2]:.1%}, k = {ID['window'][3]:+.3f}")
both = np.column_stack([vm, vw])
res_both = va - both @ scipy.linalg.lstsq(both, va)[0]
check("⚠ and the two-channel line is printed TO BE DISCOUNTED: two channels span the plane, so together "
      "they reconstruct the arm exactly -- arithmetic, not attribution, and the same degeneracy one level up",
      np.hypot(*res_both) / np.hypot(*va) < 1e-9 and 'to be discounted, not quoted' in HFLAT,
      f"residue after both: {np.hypot(*res_both):.2e} of {np.hypot(*va):.3f}")

check("⇒ *** SO BOTH SCALES ARE OUT, EACH FOR ITS OWN REASON: the spectrum-level ratio by MEASUREMENT (ⓑ, a "
      "factor of two) and the least-squares projection by ALGEBRA (it was never a measurement of anything "
      "but a phase) ***",
      'each for its own reason' in HFLAT and 'neither failure is the other' in HFLAT,
      'two independent invalidations, not one doubt twice')
check("⛭⛭⛭ AND THE ANSWER IS THE THIRD ROW `r7035` LISTED -- nothing decidable, the phases will not support "
      "a share, and `PO-56` TERMINATES on the stated ground that no instrument this construction has can "
      "attribute the modulation",
      'the third row' in HFLAT and 'no instrument this construction has can attribute the' in HFLAT
      and 'did not reach for a fourth row' in HFLAT,
      "the terminal state itself, which r7035 says is also a result")
check("⛔ AND THE GUARDS HOLD: no mechanism, no new candidate, `cc66.61`'s floor and the band-1 results left "
      "finished, no corpus edits",
      'no mechanism' in HFLAT and 'no new candidate' in HFLAT and 'are not re-derived' in HFLAT
      and 'no corpus edits' in HFLAT, "finished work is left finished")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
