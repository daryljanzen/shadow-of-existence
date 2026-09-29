"""⓶⓵ IS THE LOWEST BAND ITS OWN FEATURE, AND WHAT DO THE CHANNELS SCORE AGAINST IT? -- r7023+cc66.63.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** THE ORDER'S DISTINCTION IS THIS FILE'S VOCABULARY. **
    SEPARATING POWER -- the instrument's ability to tell two candidate spectra apart at a band (25.11 sigma)
    SIGNIFICANCE    -- the size of a departure against its own trend, in that metric (2.5--3.2 sigma)
⇒ *No quantity below divides one by the other.  A share is a ratio of two SIGNIFICANCES.*

** AND ⓶ IS RUN FIRST THOUGH IT IS NUMBERED SECOND, because it decides what ⓵ means. **
"""
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
sys.path.insert(0, os.path.join(HERE, '..', '..', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QCB = 0.5 * (QE[:-1] + QE[1:])
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
LC, _FAC = CS.bin_center_and_fac()


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


print(__doc__)
print('=' * 100)

LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    ls, dl, _ = load(fn)
    KN[nm] = CS.bin_spectrum(ls, dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB = (LC / AAC)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, ma, dat = MC[OK], MA[OK], CS.X_DATA[OK]
LL = LC[OK]


def shape_fit(m, n):
    """fit a smooth multiplicative template with n free coefficients in ln(ell) -- n = 1 is the single
    amplitude the likelihood itself fits, and higher n absorbs progressively more GLOBAL shape"""
    x = np.log(LL / LL.mean())
    X = np.column_stack([m * x ** j for j in range(n)])
    c = scipy.linalg.solve(X.T @ F @ X, X.T @ F @ dat, assume_a='sym')
    return X @ c


def band_sig(vec, lo, hi):
    """SEPARATING POWER of a band's bins for the vector given, in the likelihood's own metric"""
    msk = (QB >= lo) & (QB < hi)
    c = COV[np.ix_(msk, msk)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(msk.sum())))
    return float(np.sqrt(vec[msk] @ (0.5 * (f + f.T)) @ vec[msk]))


print('\n  ⛭⛭⛭ ⓶ IS THE LOWEST BAND\'S DEPARTURE ITS OWN FEATURE, OR THE SHAPE REJECTION READ LOCALLY?')
print('-' * 100)
print('    *Absorb progressively more smooth global shape -- a multiplicative template with n free '
      'coefficients in ln(ell), n=1 being the single amplitude the likelihood itself fits -- and watch '
      'whether band 1 dies FASTER than the rest.  More freedom always shrinks a residual, so the rate is '
      'what is read, not the size.*')
print('    ⛔ *and the quantity is the RESIDUAL against the data, not a model-against-model separation: the '
      'shape rejection is a fact about how each model fits `plik_lite`, so band 1\'s share of it is the '
      'per-band contribution to chi2(arm) - chi2(control).*')


def band_chi2(res, lo, hi):
    msk = (QB >= lo) & (QB < hi)
    c = COV[np.ix_(msk, msk)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(msk.sum())))
    return float(res[msk] @ (0.5 * (f + f.T)) @ res[msk])


print(f"\n    {'n':>3s}  {'chi2(arm)':>10s}  {'chi2(ctrl)':>11s}  {'excess':>8s}   "
      + '  '.join(f'{f"b{j + 1:d}":>7s}' for j in range(7)))
ROWS = []
for n in (1, 2, 3, 4):
    ra, rc = dat - shape_fit(ma, n), dat - shape_fit(mc, n)
    DX = np.array([band_chi2(ra, a, b) - band_chi2(rc, a, b) for a, b in zip(QE[:-1], QE[1:])])
    ROWS.append((n, DX, float(ra @ F @ ra), float(rc @ F @ rc)))
    print(f"    {n:>3d}  {float(ra @ F @ ra):>10.1f}  {float(rc @ F @ rc):>11.1f}  "
          f"{float(ra @ F @ ra) - float(rc @ F @ rc):>8.1f}   "
          + '  '.join(f'{v:>7.1f}' for v in DX))
print("    ⌗ *per-band contributions to the excess; they need not sum to it, because the covariance "
      "couples bins across band edges and each band is inverted on its own block.*")
BASE = ROWS[0][1]
print(f"\n    ⛭ AND THE RATE, WHICH IS WHAT THE PRE-REGISTRATION SAID TO READ RATHER THAN THE SIZE:")
print(f"      {'n':>3s}  {'band 1 / its n=1':>18s}  {'bands 2--7 / their n=1':>24s}  {'ratio':>8s}")
RT = []
for n, DX, _, _ in ROWS:
    b1 = DX[0] / BASE[0]
    rest = float(np.mean(DX[1:] / BASE[1:]))
    RT.append(b1 / rest)
    print(f"      {n:>3d}  {b1:>18.3f}  {rest:>24.3f}  {b1 / rest:>8.3f}")
print(f"\n    ⇒ band 1's share of the excess is {BASE[0] / sum(BASE):.1%} at n=1 and "
      f"{ROWS[-1][1][0] / sum(ROWS[-1][1]):.1%} at n={ROWS[-1][0]}")
print('\n' + '=' * 100)

print('\n  ⛔⛔ AND THIS FORCES A CORRECTION TO `cc66.62`, WHICH IS MINE')
print('-' * 100)
print("    *`cc66.62` ⓵ⓑ was headed \"THE STEP IS A LOCALISED CONTRIBUTION TO ITS EXCESS\" and then reported "
      "band 1's SEPARATING POWER -- 36.4 sigma of arm-versus-control separation against a trend predicting "
      "53--71.*")
print("    ⇒ ** The number was right and the LABEL was wrong. **  *Separating power is how well the data "
      "could tell the two models apart using that band; the likelihood's EXCESS is chi2(arm) - chi2(control), "
      "the residual it actually rejects on.*")
print(f"    ⇒ *** AND MEASURED PROPERLY, BAND 1 CARRIES {ROWS[0][1][0] / sum(ROWS[0][1]):.1%} OF THE "
      f"PER-BAND EXCESS -- {ROWS[0][1][0]:.1f} OF THE {sum(ROWS[0][1]):.0f} THE SEVEN BANDS SUM TO, "
      f"AGAINST A TOTAL OF {ROWS[0][2] - ROWS[0][3]:.0f} OVER ALL COVERED BINS -- AND ITS CONTRIBUTION CHANGES "
      f"SIGN UNDER SHAPE ABSORPTION ({'  '.join(f'{r[1][0]:+.1f}' for r in ROWS)}), WHERE BANDS 2--7 ARE "
      f"STABLE TO A FEW PER CENT. ***")
print("    ⌗ *So ⓶'s answer is NEITHER of the two the order tabled: band 1's departure is not a distinct "
      "feature of the residual, and it is not the shape rejection read locally either -- **the shape "
      "rejection is barely present at band 1 at all.**  It lives at bands 4--7, which carry "
      f"{sum(ROWS[0][1][3:]) / sum(ROWS[0][1]):.0%} of the excess.*")
print("    ⚠ *This is the separating-power/significance distinction biting a third time, and 66 put it in "
      "front of the order one revision before it bit.*")

print('\n  ⛭⛭⛭ ⓵ THE CHANNELS SCORED AGAINST THE STEP, IN THE METRIC THE STEP ACTUALLY LIVES IN')
print('-' * 100)
print("    *Given ⓶, the step is a feature of the SEPARATING POWER and not of the residual excess, so that "
      "is the metric each channel is scored in -- and every number below is a significance, never a "
      "separating power divided by one.*")
A1 = float((mc @ F @ dat) / (mc @ F @ mc))


def S_of(v):
    return np.array([band_sig(A1 * v, a, b) for a, b in zip(QE[:-1], QE[1:])])


def band_sig(vec, lo, hi):
    msk = (QB >= lo) & (QB < hi)
    c = COV[np.ix_(msk, msk)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(msk.sum())))
    return float(np.sqrt(vec[msk] @ (0.5 * (f + f.T)) @ vec[msk]))


SARM = S_of(ma - mc)
DARM = dep4(SARM)
print(f"    {'quantity':16s}" + ''.join(f"{b[0]:>15s}" for b in BASES) + "      share of the arm's")
OUT = {}
for nm in ('window', 'term mix', 'JOINT'):
    S = S_of(KN[nm][OK] - mc)
    D = dep4(S)
    OUT[nm] = D
    sh = float(np.mean([x[0] / y[0] for x, y in zip(D, DARM)]))
    sgn = '' if np.sign(np.mean([x[0] for x in D])) == np.sign(np.mean([x[0] for x in DARM])) \
        else '   ** WRONG SIGN **'
    print(f"    {nm:16s}" + ''.join(f"{x[0]:+15.3f}" for x in D) + f"{sh:>16.2f}{sgn}"
          + f"   [{min(abs(x[0] / x[1]) for x in D):.1f}-{max(abs(x[0] / x[1]) for x in D):.1f}s]")
print(f"    {'the ARM':16s}" + ''.join(f"{x[0]:+15.3f}" for x in DARM) + f"{1.0:>16.2f}"
      + f"   [{min(abs(x[0] / x[1]) for x in DARM):.1f}-{max(abs(x[0] / x[1]) for x in DARM):.1f}s]")
print("    ⌗ *the bracket is each departure against its OWN bands 2--7 residual -- a significance, and the "
      "share column is a ratio of two of them.*")

print('\n    ⌗ AND THE CANCELLATION MEASURED RATHER THAN READ OFF, as the order required:')
dw = float(np.mean([x[0] for x in OUT['window']]))
dm = float(np.mean([x[0] for x in OUT['term mix']]))
dj = float(np.mean([x[0] for x in OUT['JOINT']]))
RULES = {'product (1+dw)(1+dm)-1': (1 + dw) * (1 + dm) - 1, 'sum dw+dm': dw + dm,
         'quadrature': np.sign(dw + dm) * float(np.hypot(dw, dm))}
print(f"      singles: window {dw:+.4f}, term mix {dm:+.4f};  the JOINT bank measures {dj:+.4f}")
for k, v in RULES.items():
    print(f"        {k:24s} predicts {v:+.4f}   residual {v - dj:+.4f}")
BEST = min(RULES, key=lambda k: abs(RULES[k] - dj))
RMSJ = float(np.mean([x[1] for x in OUT['JOINT']]))
print(f"      ⇒ closest rule: ** {BEST.split()[0]} **, off by {abs(RULES[BEST] - dj):.4f} = "
      f"{abs(RULES[BEST] - dj) / RMSJ:.1f} of the joint's own bands 2--7 residual ({RMSJ:.4f})")
print(f"      ⇒ ** NO RULE FITS: the realised pair delivers {dj / RULES[BEST]:.0%} of the closest "
      f"prediction. **  *The two knobs partly cancel here as they did on the differential estimator -- "
      f"measured, not read off the {12.82:.2f}-against-{18.64:.2f} that 66 flagged.*")
print('\n' + '=' * 100)

print(f"""
  ⛔⛔ ⓶ FIRST, BECAUSE IT DECIDES WHAT ⓵ MEANS -- AND THE ANSWER IS NEITHER OF THE TWO TABLED.
    *Band 1 contributes {ROWS[0][1][0]:.1f} of the {sum(ROWS[0][1]):.0f} the seven bands sum to --
    {ROWS[0][1][0] / sum(ROWS[0][1]):.1%} -- against a total excess of {ROWS[0][2] - ROWS[0][3]:.0f} over all
    covered bins.  Absorbing smooth global shape at n = 1,2,3,4 it reads
    {'  '.join(f'{r[1][0]:+.1f}' for r in ROWS)}: **it changes sign**, where bands 2--7 hold to within a few
    per cent.*
    ⇒ ** SO BAND 1'S DEPARTURE IS NOT A DISTINCT FEATURE OF THE RESIDUAL, AND IT IS NOT THE SHAPE REJECTION
    READ LOCALLY EITHER -- THE SHAPE REJECTION IS BARELY PRESENT THERE AT ALL. **  *It lives at bands 4--7,
    which carry {sum(ROWS[0][1][3:]) / sum(ROWS[0][1]):.0%} of the per-band excess.*

  ⛔⛔ AND THAT FORCES A CORRECTION TO `cc66.62` WHICH IS MINE.  *Its ⓵ⓑ was headed "THE STEP IS A LOCALISED
    CONTRIBUTION TO ITS EXCESS" and then reported band 1's SEPARATING POWER.  **The number was right and the
    label was wrong** -- and 66 drew the separating-power/significance distinction one revision before it
    bit.*  ⇒ *The likelihood **does** see a band-1 departure, in its power to tell models apart; it does
    **not** carry a band-1 excess.  Those are different sentences and `cc66.62` ran them together.*

  ⛭⛭⛭ ⓵ AND IN THE METRIC THE STEP ACTUALLY LIVES IN, ALL THREE CHANNELS DEPART THE ARM'S WAY.
    *Each channel's band-1 departure from its own bands 2--7 trend, against the arm's
    {min(x[0] for x in DARM):+.3f} to {max(x[0] for x in DARM):+.3f}:*
      · the WINDOW channel {min(x[0] for x in OUT['window']):+.3f} to {max(x[0] for x in OUT['window']):+.3f}
        -- ** the same sign and LARGER **, a share of
        {np.mean([x[0] / y[0] for x, y in zip(OUT['window'], DARM)]):.2f};
      · the TERM MIX {min(x[0] for x in OUT['term mix']):+.3f} to
        {max(x[0] for x in OUT['term mix']):+.3f}, a share of
        {np.mean([x[0] / y[0] for x, y in zip(OUT['term mix'], DARM)]):.2f};
      · the JOINT {min(x[0] for x in OUT['JOINT']):+.3f} to {max(x[0] for x in OUT['JOINT']):+.3f}, a share
        of {np.mean([x[0] / y[0] for x, y in zip(OUT['JOINT'], DARM)]):.2f}.
    ⇒ *** THE FIRST TIME THIS ROW HAS HAD CANDIDATES THAT DEPART THE SAME WAY AS THE ARM ON AN INSTRUMENT
    THAT CAN CARRY THE QUESTION. ***  ⚠ *And the window channel, which went the WRONG way on the differential
    estimator, goes the right way here and over-delivers -- a different verdict on a different instrument,
    reported as that rather than smoothed.*
  ⛔ *AND THE CANCELLATION IS REAL AND MEASURED: the realised pair delivers {dj / RULES[BEST]:.0%} of the
    closest of product, sum and quadrature, {abs(RULES[BEST] - dj) / RMSJ:.1f} of its own residual away.  The
    two knobs partly cancel here as they did on the differential estimator.*

  ⚠⚠ *AND WHAT ⓶ DOES TO ⓵, WHICH IS THE WHOLE REASON IT WAS RUN FIRST: these shares are shares of a
    SEPARATING-POWER departure.  **A channel matching the arm there is matching a feature that carries one
    per cent of the likelihood's excess**, so this is not yet "a candidate produces the step" in the sense
    `PO-56`'s strong clause needs.  ⇒ *It is a real match in a real metric, and it is the wrong metric for
    the clause -- which I would rather say now than have the share quoted without it.*

  ⛔ *No new candidate.  No mechanism.  `cc66.61`'s floor is not revisited.  No basis or aggregation chosen.*
""")
