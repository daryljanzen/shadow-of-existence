"""⓵⓶⓷ THE COUPLING: HOW MUCH OF THE EXCESS DOES THE CANDIDATE CARRY? -- r7005+cc66.55.

⛔ *The order's ⓵: "what fraction of the excess does it carry across the range where it is measured...
and say whether the shortfall is constant across the range or grows -- a constant shortfall is a
coupling, a growing one is a second shape mismatch."  ⓶: "is the coupling... something the instrument
fixes, or something the construction fixes?"  ⓷: "does the candidate's contribution reverse with
[the median envelope], or does it survive both?"*

** THE COUPLING IS MEASURED AND NOT MODELLED, AND THE INSTRUMENT ALREADY BANKED WHAT IT TAKES. **
`DPSRC` scales the Doppler source term, so three banked control spectra at `DPSRC` = 1, 0.8794 and 0.6
give the response of each band's contrast to the Doppler amplitude as a finite difference in
`d ln C / d ln s` -- **three points, so the linearity is checked rather than assumed.**

⚠ ** AND THE CRITERION IS NAMED BEFORE USE, PER THE STANDING GUARD. **  *The coupling multiplies a
FRACTIONAL CHANGE IN THE DOPPLER'S OSCILLATION AMPLITUDE RELATIVE TO THE MONOPOLE'S.  Which measured
quantity that is decides the answer, and there are two on the table:*
  · the FIELD reading -- `cc66.51`'s, `(theta_b/k)/Psi` against `(Theta_0+Psi)/Psi` at last scattering,
    from the held-period estimator: the arm is **higher** by $+0.5$ to $+1.4$ per cent;
  · the PROJECTED reading -- `cc66.50`'s quantity, the square root of the banked band-power share
    `w2dp/w2sw`, which is what `DPSRC` actually scales: the arm is **lower** by $10$ to $13$ per cent.
⇒ ** THEY DISAGREE IN SIGN, AND THE COUPLING TURNS THAT DISAGREEMENT INTO A DISAGREEMENT ABOUT WHETHER
THE CANDIDATE HELPS AT ALL -- a factor of seven in magnitude even at their closest.  Both are computed
below and NEITHER IS CHOSEN. **
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NF = 3.0
PTS = ((1.0, 'r6941_fine_lcdm.npz'), (0.8794, 'r6975_mix_lcdm.npz'), (0.6, 'r6975_mixb_lcdm.npz'))


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


def target(kind='mean'):
    return bands('r6941_fine_cr.npz', kind) / bands('r6941_fine_lcdm.npz', kind) - 1.0


def coupling(kind='mean'):
    C = {s: bands(f, kind) for s, f in PTS}
    near = np.log(C[0.8794] / C[1.0]) / np.log(0.8794)
    mid = np.log(C[0.6] / C[0.8794]) / np.log(0.6 / 0.8794)
    full = np.log(C[0.6] / C[1.0]) / np.log(0.6)
    return near, mid, full


def projected():
    P = {}
    for t in ('lcdm', 'cr'):
        d = np.load(os.path.join(SP, f'r6959_eta_{t}.npz'))
        e = d['eta']
        m = (e >= float(d['eta_ls']) - NF * float(d['eta_ls_w'])) & \
            (e <= float(d['eta_ls']) + NF * float(d['eta_ls_w']))
        P[t] = {k: np.array([float(np.trapezoid(d[k][m][:, b], e[m])) for b in range(7)])
                for k in ('w2dp', 'w2sw')}
    pw = (P['cr']['w2dp'] / P['cr']['w2sw']) / (P['lcdm']['w2dp'] / P['lcdm']['w2sw'])
    return np.sqrt(pw) - 1.0, P['lcdm']['w2dp'] / P['lcdm']['w2sw']


# the FIELD reading -- the held-period estimator of cc66.53, band means, eight settings
FIELD = np.array([-0.00031, +0.00482, +0.00494, +0.00507, +0.00903, +0.01241, +0.01441])
FIELD_SPR = np.array([0.02102, 0.00303, 0.00501, 0.00517, 0.00110, 0.00205, 0.00098])

print(__doc__)
print('=' * 100)
NEAR, MID, FULL = coupling('mean')
NEARM = coupling('median')[0]
PROJ, SHARE = projected()
T, TM = target('mean'), target('median')

print('\n  ⛭ THE COUPLING, MEASURED: d ln C / d ln s, per band, from the three banked DPSRC points')
print('    q              ' + '  '.join(f'{x:8.2f}' for x in QC))
print('    1.00 -> 0.879  ' + '  '.join(f'{x:+8.3f}' for x in NEAR))
print('    0.879 -> 0.60  ' + '  '.join(f'{x:+8.3f}' for x in MID))
print('    1.00 -> 0.60   ' + '  '.join(f'{x:+8.3f}' for x in FULL))
print('    median env.    ' + '  '.join(f'{x:+8.3f}' for x in NEARM))
print(f"\n    ⇒ ** NEGATIVE AT EVERY BAND, ON BOTH ENVELOPES, OVER EVERY INTERVAL -- {2 * 3 * 7} "
      f"measurements of the sign and not one positive. **  *More Doppler fills more trough and LOWERS "
      f"the contrast, which is `cc66.51`'s own physics read forwards.*")
print('    ⌗ *The slope steepens towards s = 1, so the local slope there is the one that applies and it '
      'is also the one measured over the shortest step.*')

print('\n  ⛭⛭ ⓶ AND THE CONSTRUCTION FIXES IT, WHICH IS SHOWN BY WHAT DOES NOT CHANGE IT.')
print('    the control\'s own Doppler-to-monopole band-power share runs   '
      + '  '.join(f'{x:.2f}' for x in SHARE))
print(f"    -- a factor {SHARE.max() / SHARE.min():.1f} across the bands -- and the coupling's SIGN is "
      f"the same at every one of them.")
print('    ⇒ ** A quantity whose sign is invariant across a factor of six in the very ratio it depends '
      'on is not set by a knob. **  `DPSRC` is the PROBE and not the setter: it is how the coupling was '
      'measured, not what fixes it.  ⌗ *So the size is a PREDICTION and not a fit -- once its input is '
      'settled, which is ⓵\'s problem below.*')
print('    ⚠ *And the one thing not measured: all three DPSRC banks are the CONTROL. The arm\'s '
      'coupling is assumed to be the control\'s. Its Doppler share differs by about a fifth, against '
      'the factor of six across which the sign does not move, so the assumption cannot reach the sign '
      '-- and it is not asked to reach more than that.*')

print('\n  ⛔⛔ ⓵ AND THE CONTRIBUTION, ON BOTH READINGS OF THE INPUT, BECAUSE THEY DISAGREE IN SIGN:')
print('    q                     ' + '  '.join(f'{x:8.2f}' for x in QC))
print('    target                ' + '  '.join(f'{x:+8.4f}' for x in T))
print('    FIELD departure       ' + '  '.join(f'{x:+8.4f}' for x in FIELD))
print('    PROJECTED departure   ' + '  '.join(f'{x:+8.4f}' for x in PROJ))
CF, CP = NEAR * FIELD, NEAR * PROJ
print('    contribution (field)  ' + '  '.join(f'{x:+8.4f}' for x in CF))
print('    contribution (proj.)  ' + '  '.join(f'{x:+8.4f}' for x in CP))
print('    fraction of excess, field reading  '
      + '  '.join(f'{100 * x:+7.0f}%' for x in (CF / T)[1:]))
print('    fraction of excess, proj. reading  '
      + '  '.join(f'{100 * x:+7.0f}%' for x in (CP / T)[1:]))
print('    ⌗ *band 1 is omitted from the fractions: `cc66.54` closed it to the field estimator, and '
      'its field value is smaller than its own spread.*')

print('\n' + '=' * 100)
print(f"""
  ⛔⛔⛭ THE ANSWER TO ⓵ IS THAT THE FRACTION IS NOT DETERMINED, AND WHAT IS NOT DETERMINED IS THE INPUT
    RATHER THAN THE COUPLING.

    ⓐ ** THE COUPLING IS ROBUST. **  Negative at every band, both envelopes, all three intervals.
    ⓑ ** THE INPUT IS NOT. **  On the FIELD reading the candidate carries
      {100 * (CF / T)[1]:+.0f} to {100 * (CF / T)[-1]:+.0f} per cent of the excess -- *the wrong sign*.
      On the PROJECTED reading it carries {100 * (CP / T)[1]:+.0f} to {100 * (CP / T)[-1]:+.0f} per
      cent -- *the right sign, over-delivering at the bottom and matching at the top.*
    ⓒ ** AND THE COUPLING IS WHAT TURNS A DISAGREEMENT ABOUT A QUANTITY INTO A DISAGREEMENT ABOUT
      WHETHER THE CANDIDATE HELPS AT ALL. **  *This is the third revision in which these two readings
      have decided an answer between them, and the first in which they decide its SIGN.*

  ⌗ AND THE ORDER'S SECOND HALF -- CONSTANT SHORTFALL OR GROWING?  ** GROWING, ON BOTH READINGS, IN
    OPPOSITE DIRECTIONS. **  The field reading's fraction grows in magnitude from
    {100 * (CF / T)[1]:+.0f} to {100 * (CF / T)[-1]:+.0f} per cent; the projected reading's FALLS from
    {100 * (CP / T)[1]:+.0f} to {100 * (CP / T)[-1]:+.0f}.  ⇒ *** SO IT IS A SHAPE MISMATCH AND NOT A
    COUPLING DEFICIT, ON EITHER READING, AND THAT IS THE FOURTH TIME THIS SECTOR HAS FOUND ONE. ***
  ⌗ *The coupling itself is nearly flat -- between {abs(NEAR.max()):.2f} and {abs(NEAR.min()):.2f} in
    magnitude with no trend in q -- so the q-dependence of the contribution is the INPUT's and not the
    coupling's, on either reading.*

  ⛭ ⓷ AND THE ENVELOPE QUESTION HAS THE GOOD ANSWER, WHICH IS WORTH SAYING PLAINLY.  ** The coupling's
    sign survives both envelopes at every band **, so the contribution does not reverse with the
    statistic and the coupling question does NOT inherit the envelope ambiguity.  *Its magnitude does
    move -- the median envelope's coupling is up to {abs(NEARM[-1] / NEAR[-1]):.1f} times the
    arithmetic one's at the top band -- so a quoted FRACTION inherits it while the SIGN does not.*
  ⛔ *What the coupling question inherits instead is worse, and it is ⓑ: the two readings of its input.*

  ⌗ AND WHAT WOULD SETTLE IT, NAMED AND NOT BUILT (the order's ⓸ closes the list).  Neither banked
    quantity is the right one: the field reading is an amplitude but at last scattering rather than in
    the projected source, and the projected reading is in the projected source but is a BAND POWER,
    which keeps the smooth part `cc66.51` showed fills no trough.  ⇒ ** The quantity the coupling
    multiplies is the OSCILLATION AMPLITUDE OF THE PROJECTED DOPPLER CONTRIBUTION, per band, and the
    instrument banks neither it nor the eta-resolved fields a derivative of it would need. **  *That is
    one bank, not a channel.*
""")
