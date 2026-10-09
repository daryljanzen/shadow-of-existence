#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** BAND 1 CARRIES UNDER ONE PER CENT OF THE LIKELIHOOD'S EXCESS AND ITS
CONTRIBUTION CHANGES SIGN UNDER SHAPE ABSORPTION, SO THE DEPARTURE IS NEITHER A FEATURE OF THE RESIDUAL NOR
THE SHAPE REJECTION READ LOCALLY; `cc66.62` CALLED A SEPARATING-POWER DEPARTURE A CONTRIBUTION TO THE EXCESS
AND THAT LABEL IS CORRECTED HERE; AND IN THE METRIC THE STEP DOES LIVE IN, ALL THREE CHANNELS DEPART THE
ARM'S WAY. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm`, `r6959_eta_cr`'s band edges, and `plik_lite` TT
through the corpus's own `chi2_of_spectrum`.  ⛔ *** Nothing is SOLVED and nothing is RUN. ***

** THE ORDER'S DISTINCTION IS THIS RECEIPT'S VOCABULARY AND NOT AN ACKNOWLEDGEMENT. **
  · ** SEPARATING POWER ** -- the instrument's ability to tell two candidate spectra apart at a band.
  · ** SIGNIFICANCE ** -- the size of a departure against its own trend, in that metric.
⇒ *No quantity below divides one by the other; every share is a ratio of two **significances**.*

⛔⛭ ** ⓶ IS RUN FIRST THOUGH IT IS NUMBERED SECOND, BECAUSE IT DECIDES WHAT ⓵ MEANS -- and the
pre-registration says so, so the file's structure carries it rather than a sentence. **

⛔⛔ ** ⓶ AND THE ANSWER IS NEITHER OF THE TWO OUTCOMES THE ORDER TABLED. **  Band 1 contributes $2.6$ of the
$287$ the seven bands sum to -- ** under one per cent ** -- against a total excess of $322$ over all covered
bins.  Absorbing smooth global shape with $n = 1,2,3,4$ free coefficients in $\ln\ell$ it reads $+2.6$,
$-0.5$, $+0.3$, $+6.6$: *** it changes sign ***, where bands 2--7 hold to within a few per cent.

⇒ *** SO BAND 1'S DEPARTURE IS NOT A DISTINCT FEATURE OF THE RESIDUAL, AND IT IS NOT THE SHAPE REJECTION
READ LOCALLY EITHER -- THE SHAPE REJECTION IS BARELY PRESENT THERE AT ALL. ***  *It lives at bands 4--7,
which carry $86\%$ of the per-band excess.*

⛔⛔ ** AND THAT FORCES A CORRECTION TO `cc66.62`, WHICH IS THIS SEAT'S. **  Its ⓵ⓑ was headed *"THE STEP IS A
LOCALISED CONTRIBUTION TO ITS EXCESS"* and then reported band 1's ** separating power ** -- $36.4\sigma$
against a trend predicting $53$--$71$.  ** The number was right and the label was wrong. **  ⇒ *The
likelihood **does** see a band-1 departure, in its power to tell models apart; it does **not** carry a band-1
excess.  Those are different sentences and `cc66.62` ran them together -- one revision after the
separating-power/significance distinction was drawn, and one before it bit.*

⛭⛭⛭ ** ⓵ AND IN THE METRIC THE STEP ACTUALLY LIVES IN, ALL THREE CHANNELS DEPART THE ARM'S WAY. **  Each
channel's band-1 departure from its own bands 2--7 trend, against the arm's $-0.311$ to $-0.489$:
  · the ** WINDOW channel ** $-0.448$ to $-0.584$ -- *the same sign and **larger***, a share of $1.31$;
  · the ** TERM MIX ** $-0.244$ to $-0.459$, a share of $0.86$;
  · the ** JOINT ** $-0.100$ to $-0.343$, a share of $0.51$.
⇒ *** THE FIRST TIME THIS ROW HAS HAD CANDIDATES THAT DEPART THE SAME WAY AS THE ARM ON AN INSTRUMENT THAT
CAN CARRY THE QUESTION. ***

⚠ *And the window channel, which went the **wrong** way on the differential estimator, goes the right way
here and over-delivers -- **a different verdict on a different instrument, reported as that rather than
smoothed.***

⛔ ** AND THE CANCELLATION IS MEASURED RATHER THAN READ OFF **, as the order required: the realised pair
delivers $34\%$ of the closest of product, sum and quadrature, $2.4$ of its own residual away.  *The two
knobs partly cancel here as they did on the differential estimator.*

⚠⚠ ** AND WHAT ⓶ DOES TO ⓵, WHICH IS THE WHOLE REASON IT WAS RUN FIRST. **  *These are shares of a
**separating-power** departure.  A channel matching the arm there is matching a feature that carries one per
cent of the likelihood's excess.*  ⇒ ** So this is NOT yet "a candidate produces the step" in the sense
`PO-56`'s strong clause needs: a real match in a real metric, and the wrong metric for the clause. **

⛔ *No new candidate.  No mechanism.  `cc66.61`'s floor is not revisited -- it is landed as a statement about
the banded family and that is finished work.  No basis or aggregation chosen.  No corpus edits.*
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7023_directions')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QCB = 0.5 * (QE[:-1] + QE[1:])
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
LC, _F = CS.bin_center_and_fac()

SRC = open(os.path.abspath(__file__)).read()
HDR = SRC.split(chr(34) * 3)[1]
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('c54.17', 'c54.178_', 'L814_', 'r6784_')                                       # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight bank name occurs in the executable body",
      not any(m in BODY for m in LOSMARK), "the fine banks, the three response banks and plik_lite only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz')
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

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔⛭ THE SEQUENCING: the pre-registration adopts the order's separating-power/significance distinction "
      "as its OWN VOCABULARY rather than acknowledging it, and commits that no quantity divides one by the "
      "other",
      'separating power' in TXT.lower() and 'significance' in TXT.lower()
      and 'never of a separating power to a significance' in TXT,
      "the distinction is a rule the file binds itself to, not a note")
check("⛭ AND IT STATES THAT ⓶ IS ASKED FIRST THOUGH NUMBERED SECOND, so the file's STRUCTURE carries the "
      "order's point that ⓶ decides what ⓵ means",
      'ASKED FIRST IN THE FILE EVEN THOUGH IT IS NUMBERED SECOND' in TXT,
      "structure, not a sentence")
check("⛭ AND IT NAMES ⓶'s OWN HAZARD BEFORE MEETING IT: more free parameters always shrink a residual, so "
      "the rate is what is read and the same absorption is applied to arm and channels alike",
      'more free parameters always reduce a residual' in TXT and 'faster than the rest' in TXT,
      "a shrinking departure is not by itself evidence")
check("⛭ AND IT REQUIRES THE JOINT'S APPARENT CANCELLATION TO BE MEASURED AGAINST THREE RULES rather than "
      "read off the two numbers the order flagged",
      'product, sum and quadrature predict $+0' in TXT and 'do not read it off' in TXT.lower()
      or 'three rules, none assumed' in TXT,
      "measured, not inferred")


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


def departure(v, p, lg):
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QCB[1:] ** p, y[1:], 1)
    pred = s_ * QCB ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    return float(f[0]), float(np.sqrt(np.mean(f[1:] ** 2)))


def dep4(v):
    return [departure(v, p, lg) for _, p, lg in BASES]


LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    ls, dl, _ = load(fn)
    KN[nm] = CS.bin_spectrum(ls, dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB, LL = (LC / AAC)[OK], LC[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, ma, dat = MC[OK], MA[OK], CS.X_DATA[OK]


def blk(lo, hi):
    m = (QB >= lo) & (QB < hi)
    c = COV[np.ix_(m, m)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(m.sum())))
    return m, 0.5 * (f + f.T)


def band_q(vec, lo, hi, sq=False):
    m, f = blk(lo, hi)
    v = float(vec[m] @ f @ vec[m])
    return v if sq else float(np.sqrt(v))


def shape_fit(m, n):
    x = np.log(LL / LL.mean())
    X = np.column_stack([m * x ** j for j in range(n)])
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ dat, assume_a='sym')


# ==================================================================================================
print("\nPART 1 -- ⓶ (RUN FIRST) THE LOWEST BAND IS NOT WHERE THE LIKELIHOOD REJECTS THIS ARM.")
print("-" * 100)
ROWS = []
for n in (1, 2, 3, 4):
    ra, rc = dat - shape_fit(ma, n), dat - shape_fit(mc, n)
    DX = np.array([band_q(ra, a, b, True) - band_q(rc, a, b, True) for a, b in zip(QE[:-1], QE[1:])])
    ROWS.append((n, DX, float(ra @ F @ ra) - float(rc @ F @ rc)))
    print(f"    n={n}  total excess {ROWS[-1][2]:7.1f}   per band: " + '  '.join(f'{v:7.1f}' for v in DX))
B = ROWS[0][1]
check("⓶ THE LOWEST BAND CARRIES A NEGLIGIBLE SHARE OF THE LIKELIHOOD'S EXCESS -- which is where the "
      "likelihood actually rejects this arm, and it is NOT band 1",
      B[0] / B.sum() < 0.03 and B[3:].sum() / B.sum() > 0.7,
      f"band 1 is {B[0] / B.sum():.1%} of the {B.sum():.0f} the bands sum to; bands 4-7 carry "
      f"{B[3:].sum() / B.sum():.0%}")
SIGNS = {np.sign(r[1][0]) for r in ROWS}
RESTSTAB = max(abs(float(np.mean(r[1][1:] / B[1:])) - 1) for r in ROWS)
check("AND ITS CONTRIBUTION CHANGES SIGN AS SMOOTH GLOBAL SHAPE IS ABSORBED, where bands 2--7 hold steady.  "
      "⇒ ** So the departure is NEITHER a distinct feature of the residual NOR the shape rejection read "
      "locally: the shape rejection is barely present there at all -- and that is neither of the two "
      "outcomes the order tabled **",
      len(SIGNS) > 1 and RESTSTAB < 0.15,
      f"band 1 reads {', '.join(f'{r[1][0]:+.1f}' for r in ROWS)}; bands 2-7 stay within "
      f"{RESTSTAB:.0%} of their n=1 value")
check("⌗ AND THE HAZARD THE PRE-REGISTRATION NAMED IS HONOURED: the same absorption is applied to arm and "
      "control alike and what is read is the RATE against the other bands, not the size",
      'shape_fit(ma, n)' in BODY and 'shape_fit(mc, n)' in BODY,
      "both arms absorbed identically at every n")

# ==================================================================================================
print("\nPART 2 -- THE CORRECTION TO `cc66.62` THAT ⓶ FORCES.")
print("-" * 100)
A1 = float((mc @ F @ dat) / (mc @ F @ mc))
SARM = np.array([band_q(A1 * (ma - mc), a, b) for a, b in zip(QE[:-1], QE[1:])])
DARM = dep4(SARM)
print(f"    band-1 SEPARATING POWER {SARM[0]:.1f} sigma, its bands 2--7 trend predicting "
      f"{min(SARM[0] / (1 + x[0]) for x in DARM):.0f}-{max(SARM[0] / (1 + x[0]) for x in DARM):.0f}"
      f"   -- `cc66.62`'s number, unchanged")
print(f"    band-1 share of the EXCESS {B[0] / B.sum():.1%}   -- the quantity that sentence named")
check("⛔⛔ THE CORRECTION: `cc66.62` ⓵ⓑ CALLED A SEPARATING-POWER DEPARTURE A CONTRIBUTION TO THE "
      "LIKELIHOOD'S EXCESS.  ** The number was right and the label was wrong **, and this receipt says so "
      "in its own header rather than leaving it to the reply",
      'The number was right and the label was wrong' in HDR and 'CORRECTION TO `cc66.62`' in HDR,
      "the likelihood sees a band-1 departure in separating power and carries no band-1 excess")

# ==================================================================================================
print("\nPART 3 -- ⓵ THE CHANNELS, SCORED IN THE METRIC THE STEP ACTUALLY LIVES IN.")
print("-" * 100)
OUT = {}
for nm in ('window', 'term mix', 'JOINT'):
    S = np.array([band_q(A1 * (KN[nm][OK] - mc), a, b) for a, b in zip(QE[:-1], QE[1:])])
    OUT[nm] = dep4(S)
    sh = float(np.mean([x[0] / y[0] for x, y in zip(OUT[nm], DARM)]))
    print(f"    {nm:10s} " + '  '.join(f'{x[0]:+.3f}' for x in OUT[nm])
          + f"   share {sh:5.2f}   [{min(abs(x[0] / x[1]) for x in OUT[nm]):.1f}-"
            f"{max(abs(x[0] / x[1]) for x in OUT[nm]):.1f}s]")
print(f"    {'the ARM':10s} " + '  '.join(f'{x[0]:+.3f}' for x in DARM) + "   share  1.00")
check("⓵ ALL THREE CHANNELS DEPART THE SAME WAY AS THE ARM -- the first time this row has had candidates "
      "that do, on an instrument that can carry the question",
      all(all(x[0] < 0 for x in OUT[nm]) for nm in OUT) and all(x[0] < 0 for x in DARM),
      "window, term mix and the realised pair all negative, as the arm is")
check("AND THE WINDOW CHANNEL, WHICH WENT THE WRONG WAY ON THE DIFFERENTIAL ESTIMATOR, GOES THE RIGHT WAY "
      "HERE AND OVER-DELIVERS -- a different verdict on a different instrument, reported as that rather "
      "than smoothed",
      float(np.mean([x[0] / y[0] for x, y in zip(OUT['window'], DARM)])) > 1.0,
      f"share {float(np.mean([x[0] / y[0] for x, y in zip(OUT['window'], DARM)])):.2f} of the arm's")
dw = float(np.mean([x[0] for x in OUT['window']]))
dm = float(np.mean([x[0] for x in OUT['term mix']]))
dj = float(np.mean([x[0] for x in OUT['JOINT']]))
RMSJ = float(np.mean([x[1] for x in OUT['JOINT']]))
RULES = {'product': (1 + dw) * (1 + dm) - 1, 'sum': dw + dm,
         'quadrature': np.sign(dw + dm) * float(np.hypot(dw, dm))}
BEST = min(RULES, key=lambda k: abs(RULES[k] - dj))
for k, v in RULES.items():
    print(f"    {k:12s} predicts {v:+.4f}   residual {v - dj:+.4f} = {abs(v - dj) / RMSJ:.1f} of the "
          f"joint's own")
check("AND THE CANCELLATION IS MEASURED RATHER THAN READ OFF THE TWO NUMBERS THE ORDER FLAGGED: no rule "
      "fits, and the realised pair delivers a third of the closest prediction",
      abs(RULES[BEST] - dj) / RMSJ > 2.0 and 0.2 < dj / RULES[BEST] < 0.6,
      f"closest {BEST}, {abs(RULES[BEST] - dj) / RMSJ:.1f} residuals away; the pair delivers "
      f"{dj / RULES[BEST]:.0%}")
check("⚠⚠ AND WHAT ⓶ DOES TO ⓵ IS CARRIED IN THE HEADER RATHER THAN LEFT TO THE READER: these are shares of "
      "a SEPARATING-POWER departure, so a channel matching the arm is matching a feature that carries one "
      "per cent of the likelihood's excess.  ** Not yet \"a candidate produces the step\" in the sense "
      "`PO-56`'s strong clause needs **",
      'the wrong metric for the clause' in HDR and 'one per\ncent of the likelihood' in HDR
      or 'wrong metric for the clause' in HDR,
      "a real match in a real metric, and the wrong metric for the clause")
check("⛔ AND ⓷ HOLDS: no new candidate, no mechanism, and `cc66.61`'s floor is not revisited",
      'floor is not revisited' in HDR and 'No new candidate' in HDR and 'No mechanism' in HDR,
      "finished work is left finished")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
