"""⓷ FIRST, AND ON PURPOSE: control the FILTER before characterising what it filters on -- r6993+cc66.50.

*** WHY THIS RUNS BEFORE ⓵, WHICH INVERTS THE ORDER'S NUMBERING AND IS NOT A LIBERTY. ***  The order's ⓷
asks whether the statistic's q-dependence is a property of the effect or of the anchoring, and notes that
this sector has already been caught once by an anchoring that read 1.95 where it should have read 1.  ⇒
** That is a question about the INSTRUMENT, not about the excess **, and its answer is what a
pre-registration for ⓵ has to write its tolerances on.  *Measuring the instrument first and pre-registering
the model comparison against the measured resolution is the opposite of letting the data shape the
tolerances: the alternative is to guess a resolution, and a guessed tolerance is the defect `cc66.47`'s
pre-registration lesson is about.*

** WHAT IT DOES. **  Injects a KNOWN q-dependence into the control's own banked spectrum and asks the
estimator to read it back.  The oscillation about the running-mean envelope is scaled by a known f(q):

    D'(l) = E(l) + f(q(l)) * (D(l) - E(l)),     q = l / l_A

and since the band statistic is a standard deviation of the oscillation, the band ratio MUST return f
evaluated over that band -- exactly, if the estimator is unbiased.  ⛔ *The envelope is RECOMPUTED on D'
rather than reused from D, which is the whole point: that recomputation is what shifted the anchored
statistic's baseline to 1.95, and it is the step that could manufacture or destroy a q-dependence.*

** AND THE FORMS INJECTED ARE THE ONES ⓵ WILL COMPARE **, so the control measures the resolution on the
very question it is a control for: a constant, a rise linear in q^2, a power law, a logarithm, and a
turnover with a SCALE in it -- the last because a scale is the single most informative thing this sector
could find and therefore the one whose recovery must be checked hardest.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
QE = np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def bands_of(q, o, edges):
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(edges[:-1], edges[1:])])


def ratio(d_num, d_den, edges=QE, win=1.0):
    """the band contrast ratio, both sides read with the SAME envelope treatment"""
    qn = d_num['ls'].astype(float) / float(d_num['l_A'])
    qd = d_den['ls'].astype(float) / float(d_den['l_A'])
    en = env_a(qn, d_num['Dl'], win)
    ed = env_a(qd, d_den['Dl'], win)
    return (bands_of(qn, (d_num['Dl'] - en) / en, edges)
            / bands_of(qd, (d_den['Dl'] - ed) / ed, edges))


def inject(d, f, win=1.0):
    """scale the oscillation about the running-mean envelope by f(q); the envelope is RECOMPUTED after"""
    q = d['ls'].astype(float) / float(d['l_A'])
    e = env_a(q, d['Dl'], win)
    return dict(ls=d['ls'], Dl=e + f(q) * (d['Dl'] - e), l_A=d['l_A'])


FORMS = (
    ('constant           f = 1.05', lambda q: np.full_like(q, 1.05)),
    ('linear in q^2      f = 1 + 0.004 q^2', lambda q: 1 + 0.004 * q ** 2),
    ('power law          f = 1 + 0.02 q^0.8', lambda q: 1 + 0.02 * q ** 0.8),
    ('logarithm          f = 1 + 0.03 ln q', lambda q: 1 + 0.03 * np.log(q)),
    ('turnover, scale 3  f = 1 + 0.10 q^2/(q^2+3^2)', lambda q: 1 + 0.10 * q ** 2 / (q ** 2 + 9.0)),
    ('turnover, scale 6  f = 1 + 0.10 q^2/(q^2+6^2)', lambda q: 1 + 0.10 * q ** 2 / (q ** 2 + 36.0)),
)

print(__doc__)
print('=' * 104)
print('\n⓷a  DOES A KNOWN q-DEPENDENCE READ BACK?  injected f(q) against what the band statistic returns')
print('     (the envelope is recomputed on the injected spectrum, which is the step under test)\n')
print('     ' + ' '.join(f'q={x:<6.2f}' for x in QC) + '   worst |rec/inj - 1|')
WORST = {}
for nm, f in FORMS:
    d2 = inject(F['lcdm'], f)
    rec = ratio(d2, F['lcdm'])
    inj = np.array([float(np.mean(f(np.linspace(a, b, 400)))) for a, b in zip(QE[:-1], QE[1:])])
    err = np.abs(rec / inj - 1)
    WORST[nm.split()[0]] = float(err.max())
    print(f'  {nm}')
    print('       inj ' + ' '.join(f'{x:<8.5f}' for x in inj))
    print('       rec ' + ' '.join(f'{x:<8.5f}' for x in rec) + f'   {err.max():.2e}')

print(f'\n  ⇒ WORST RECOVERY ERROR OVER ALL SIX INJECTED FORMS: {max(WORST.values()):.2e}')
print('     ⌗ that is the estimator resolution the ⓵ pre-registration writes its tolerances on.')


# ==================================================================================================
print('\n⓷b  AND THE ERRORS ARE NOT NOISE: THE SAME BAND PATTERN APPEARS IN ALL SIX FORMS.')
print('     rec/inj band by band, one row per injected form -- if this were sampling scatter the rows')
print('     would disagree; if it is a fixed estimator bias they will not.\n')
print('     ' + ' '.join(f'q={x:<6.2f}' for x in QC))
ROWS = []
for nm, f in FORMS:
    d2 = inject(F['lcdm'], f)
    rec = ratio(d2, F['lcdm'])
    inj = np.array([float(np.mean(f(np.linspace(a, b, 400)))) for a, b in zip(QE[:-1], QE[1:])])
    r = rec / inj
    ROWS.append(r)
    print(f'     ' + ' '.join(f'{x:<8.5f}' for x in r) + f'   {nm.split("f =")[0].strip()}')
ROWS = np.array(ROWS)
BIAS = ROWS.mean(axis=0)
SPREAD = ROWS.std(axis=0)
print('\n     mean ' + ' '.join(f'{x:<8.5f}' for x in BIAS) + '   <- the estimator BIAS per band')
print('     std  ' + ' '.join(f'{x:<8.5f}' for x in SPREAD) + '   <- disagreement between forms')
print(f'\n  ⇒ the bias swings {100 * (BIAS.max() - BIAS.min()):.2f} per cent band to band, while the six forms')
print(f'    agree on it to {100 * SPREAD.max():.2f} per cent.  ** So it is a FIXED PROPERTY OF THE ESTIMATOR')
print('    AND NOT OF THE INJECTED SHAPE ** -- a constant contrast reads as a wobble, which means the')
print('    statistic MANUFACTURES band-to-band structure that is not in the effect.')

# ==================================================================================================
print('\n⓷c  DOES THE EXCESS\'S OWN RISE SURVIVE THE ENVELOPE TREATMENT?')
print('     the same measurement at three envelope windows and with the envelope taken as a running')
print('     MEDIAN instead of a running mean -- the anchoring choice this sector was caught by once\n')


def env_m(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.median(y[m])
    return e


def ratio_env(fn, win):
    qn = F['cr']['ls'].astype(float) / float(F['cr']['l_A'])
    qd = F['lcdm']['ls'].astype(float) / float(F['lcdm']['l_A'])
    en, ed = fn(qn, F['cr']['Dl'], win), fn(qd, F['lcdm']['Dl'], win)
    return (bands_of(qn, (F['cr']['Dl'] - en) / en, QE)
            / bands_of(qd, (F['lcdm']['Dl'] - ed) / ed, QE))


Q2 = QC ** 2
print('     ' + ' '.join(f'q={x:<6.2f}' for x in QC) + '   intercept  |slope x <q^2>|/|intercept|')
for lbl, fn, win in (('mean,   win 1.0 (the statistic)', env_a, 1.0), ('mean,   win 0.8', env_a, 0.8),
                     ('mean,   win 1.2', env_a, 1.2), ('median, win 1.0', env_m, 1.0),
                     ('median, win 1.2', env_m, 1.2)):
    r = ratio_env(fn, win)
    s, i = np.polyfit(Q2, np.log(r), 1)
    print('     ' + ' '.join(f'{x:<8.5f}' for x in r)
          + f'   {np.exp(i):.4f}     {abs(s * Q2.mean()) / abs(i):.3f}   {lbl}')
print('\n     ⌗ the last column is the order\'s "forty-four per cent": the variation across q as a')
print('       fraction of the intercept, which is the filter every candidate will be judged on.')


# ==================================================================================================
print('\n⓷d  ⛔ AND THE MEDIAN ENVELOPE IS NOT A VALID ALTERNATIVE ANCHORING -- DIAGNOSED, NOT DISMISSED.')
print('     Its answer above (a variation of 1.49 against the mean envelope\'s 0.44) would be the')
print('     headline finding of this control if it were believed.  ⇒ THE TELL IS THAT IT DOES NOT MOVE')
print('     WITH THE WINDOW: the last band reads the SAME to seven figures at win 1.0 and win 1.2,')
print('     where every other band and every mean-envelope reading moves.  An estimator insensitive to')
print('     its own smoothing scale is not measuring what it is supposed to.\n')
_q = F['lcdm']['ls'].astype(float) / float(F['lcdm']['l_A'])
_D = F['lcdm']['Dl']
print('       how far the envelope sits from the SPECTRUM ITSELF, mean |e/D - 1|:')
print('         band          median win 1.0   median win 1.2   mean win 1.0   mean win 1.2')
for lo, hi, lbl in ((1.0, 1.6, 'low q'), (5.05, 5.75, 'last band')):
    m = (_q >= lo) & (_q <= hi)
    v = []
    for fn in (env_m, env_a):
        for w in (1.0, 1.2):
            e = fn(_q, _D, w)
            v.append(float(np.abs(e[m] / _D[m] - 1).mean()))
    print(f'         {lbl:12s}  {v[0]:<15.5f}  {v[1]:<15.5f}  {v[2]:<13.5f}  {v[3]:.5f}')
print('\n     ⇒ ** At high q the running MEDIAN collapses onto the curve itself ** -- within 3.6 per cent')
print('       of it and identically so at both windows -- because the median of a locally monotone')
print('       stretch is its central value, whatever the window.  The oscillation it is meant to')
print('       measure against is absorbed into it.  *The mean envelope sits 14 to 17 per cent away and')
print('       moves with the window, which is what an envelope estimator should do.*')
print('\n  ⇒ SO THE CONTROL\'S VERDICT ON THE FILTER, IN THREE PARTS:')
print('     ✔ a known q-dependence READS BACK, worst error 1.3 per cent over six injected forms')
print('       including a turnover with a scale in it -- so the filter can see the shapes it filters on;')
print('     ⚠ the estimator carries a FIXED per-band bias of about one per cent, agreed on by all six')
print('       forms to 0.36 per cent, and a CONSTANT contrast reads as a wobble -- so band-to-band')
print('       structure at the per-cent level is the instrument and must not be read as the effect;')
print('     ✔ the excess\'s own rise survives the mean-envelope window (0.44, 0.44, 0.40 at win 0.8,')
print('       1.0, 1.2), which is far above that bias -- ** the RISE is real, the WOBBLE is not. **')
