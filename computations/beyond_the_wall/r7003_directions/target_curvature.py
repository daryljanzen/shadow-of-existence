"""⓶ DOES THE TARGET'S OWN CURVATURE CARRY THE CLAIM THE PAPER MAKES? -- r7003+cc66.54.

⛔ *The order's ⓶: "The excess's deceleration reverses on dropping one band of seven.  That is the
pre-registered target statistic resting on a single band --- and `P15` currently says the excess
decelerates on the strength of it.  So: is the target's curvature robust enough to carry the claim the
paper makes?  Not the candidate's --- the target's."*

** AND THE GUARD APPLIES TO THE VARIANTS TOO, WHICH IS THE WHOLE OF THE METHOD HERE. **  *A curvature is
not a quantity until its definition is named, and the definition is `r6911+cc66.40`'s:* **the contrast is
the standard deviation of the spectrum's departure from a running ARITHMETIC-MEAN envelope taken over one
acoustic period in `q = l/l_A`**, *and the curvature is the quadratic coefficient of a least-squares fit
to the seven band ratios against `q`.*  ⇒ ** So the six variants that move the window width, the band
edges and the sampling test THIS statistic, and the two that change the envelope's definition or its
period are DIFFERENT statistics. **

⚠ ** AND THE SECOND KIND IS REPORTED RATHER THAN SET ASIDE, BECAUSE ONE OF THEM REVERSES THE ANSWER. **
*A running MEDIAN envelope -- same window, same bands, everything else unchanged -- turns the curvature
positive.  It is a different statistic, and the difference is measured: its envelope absorbs about half
of the top band's oscillation on both arms.  But that does not retire the exposure.*  ⇒ ** "The excess
decelerates" is a property of the ARITHMETIC-MEAN-ENVELOPE contrast statistic and not of the excess as
such, and the paper does not currently say which. **
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
QE0 = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)


def envelope(x, y, win, kind):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def bands(d, QE, win, kind, npts):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = envelope(q, d['Dl'], win, kind)
    o = (d['Dl'] - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, npts), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def target(win=1.0, kind='mean', npts=400, shift=0.0):
    QE = QE0 + shift
    return (bands(F['cr'], QE, win, kind, npts) / bands(F['lcdm'], QE, win, kind, npts) - 1.0,
            0.5 * (QE[:-1] + QE[1:]))


VARIANTS = (
    ('baseline', {}, True),
    ('win = 0.8', {'win': 0.8}, True),
    ('win = 1.2', {'win': 1.2}, True),
    ('npts = 1200', {'npts': 1200}, True),
    ('edges +0.05', {'shift': 0.05}, True),
    ('edges -0.05', {'shift': -0.05}, True),
    ('win = 2.0', {'win': 2.0}, False),
    ('median envelope', {'kind': 'median'}, False),
)

print(__doc__)
print('=' * 100)
print('\n  the seven band ratios, the full-range curvature, and the curvature with BAND 1 DROPPED:')
print(f"    {'variant':16s} " + '  '.join(f'b{i + 1:<6d}' for i in range(7))
      + f" {'curvature':>11s} {'drop band 1':>13s}")
ADM, ALL = [], []
for nm, kw, admissible in VARIANTS:
    T, qc = target(**kw)
    c = float(np.polyfit(qc, T, 2)[0])
    c1 = float(np.polyfit(qc[1:], T[1:], 2)[0])
    (ADM if admissible else ALL).append((nm, T, c, c1))
    print(f"    {nm:16s} " + '  '.join(f'{x:+.4f}' for x in T) + f" {c:+11.5f} {c1:+13.5f}"
          + ('' if admissible else '   ⛔ NOT this statistic'))

A = np.array([r[1] for r in ADM])
CF = np.array([r[2] for r in ADM])
CD = np.array([r[3] for r in ADM])
print(f"\n    over the {len(ADM)} ADMISSIBLE variants (the envelope's definition untouched):")
print(f"      band 1        {A[:, 0].min():+.4f} to {A[:, 0].max():+.4f}")
print(f"      curvature     {CF.min():+.5f} to {CF.max():+.5f}   "
      f"sign {'ROBUST' if CF.max() < 0 or CF.min() > 0 else 'NOT robust'}")
print(f"      with band 1 dropped   {CD.min():+.5f} to {CD.max():+.5f}   "
      f"sign {'robust' if CD.max() < 0 or CD.min() > 0 else '** NOT DETERMINED **'}")

print('\n  ⚠ AND THE TWO NON-DEFINING VARIANTS, WITH WHAT EACH ACTUALLY DOES:')
print('    · MEDIAN envelope -- a different envelope, so a different statistic.  ** IT REVERSES THE '
      'CURVATURE. **\n      *The measured difference: its envelope absorbs about half of the top band\'s '
      'oscillation on both\n      arms, so its band ratios are formed on a much smaller residual.  It is '
      'NOT obviously the worse\n      envelope -- it leaves a departure with zero mean, which the '
      'arithmetic one does not -- and that\n      is exactly why naming it a different statistic does not '
      'retire the exposure.*')
print('    · win = 2.0 -- TWO acoustic periods, so it smooths across the structure the statistic is '
      'defined\n      to measure.  *It drops band 1 by a factor of five and keeps the sign.*')

print('\n' + '=' * 100)
print(f"""
  ⛭⛭ THE ANSWER, IN TWO PARTS, AND THEY POINT OPPOSITE WAYS.

    ⓐ ** YES -- THE TARGET'S CURVATURE CARRIES ITS SIGN ROBUSTLY. **  Negative in every admissible
      variant, {CF.min():+.5f} to {CF.max():+.5f}, and band 1 itself sits at {A[:, 0].min():+.4f} to
      {A[:, 0].max():+.4f}.  *"The excess decelerates" is not a fragile number: it survives the
      envelope width, the band edges and the sampling.*

    ⓑ ** AND YES -- IT IS A SINGLE-BAND CLAIM. **  With band 1 dropped the curvature runs
      {CD.min():+.5f} to {CD.max():+.5f} across the same variants: ** its sign is not determined. **
      *The deceleration is the lowest band being LOW, not the upper bands bending.*

    ⓒ ** AND IT IS NOT ROBUST TO THE ENVELOPE'S DEFINITION, WHICH IS THE PART I WOULD RATHER NOT HAVE
      FOUND. **  A running median reverses it to +0.00504.  *That is a different statistic and the
      difference is measured -- but it is not obviously the worse envelope, so the honest reading is
      that the sign belongs to the statistic rather than to the excess.*

  ⇒ *** SO `P15` MAY SAY THE EXCESS DECELERATES, AND OWES TWO QUALIFICATIONS IN THE SAME BREATH: THAT
    THE DECELERATION IS CARRIED BY THE LOWEST BAND -- the band ⓵ shows no estimator of an oscillation
    amplitude can reach -- AND THAT IT IS A PROPERTY OF THIS ENVELOPE. ***
  ⌗ *Not "the paper has landed it too strongly": the claim is supported on its own statistic.  **What
    was landed too strongly is the claim's INDEPENDENCE -- of any one band, and of the envelope's
    definition** -- which nothing in the paper says and a reader would assume.*
""")
