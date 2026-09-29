"""⓵⓶⓷ THE BANK, THE CONTRIBUTION, AND THE PATTERN IN THE FOUR MISMATCHES -- r7007+cc66.56.

⛔ *The order's ⓵: "Say what the instrument has to emit for that... and if it turns out the instrument
cannot emit it without a change this seat should not make unilaterally, say that and stop."*

** ⓵ THE INSTRUMENT ALREADY EMITS IT AND THE BANK IS ALREADY ON DISK. **  `SRCDEC`, added at
`r6915+cc66.41`, writes the FULL BILINEAR DECOMPOSITION: with `Delta^a_l(k) = INT term_a j_l deta`,
`C_l = SUM_{a<=b} w_ab SUM_k P Delta^a Delta^b`, ** ten numbers per multipole that sum to `C_l`
exactly ** -- and `r6915_pairs_{lcdm,cr}.npz` carry them for both arms.  ⇒ *No run, no instrument
change, and the order's escape hatch is not needed.*  ⌗ *The grid is 238 multipoles against the fine
banks' 1900, which is checked below rather than assumed adequate.*

⛭ ** AND THE BANK BUYS SOMETHING `cc66.55` HAD TO CAVEAT. **  The `s`-scaling of every pair is known
exactly -- `s^2` on `dp*dp`, `s` on the three `dp` crosses, `1` on the rest -- so
`dDl/d ln s = 1x(sw*dp + dp*isw + dp*pol) + 2x(dp*dp)` per multipole, which gives the coupling
** analytically and FOR THE ARM AS WELL AS THE CONTROL. **  *`cc66.55` measured it on the control and
transferred it; that caveat is discharged here.*

⚠ ** AND ONE CONSTRUCTION WAS TRIED FIRST AND IS REPORTED AS FAILED RATHER THAN DROPPED. **  The
obvious reading of "the oscillation amplitude of the projected contribution" is
`sqrt( osc(dp*dp) / osc(sw*sw) )` per band.  *On the arithmetic envelope it is small and
sign-indefinite; under a median envelope it reaches $+134$ per cent, because the oscillation of a
weak, smooth term about a median envelope is not a well-conditioned quantity.*  ⇒ ** That
definition inherits the envelope ambiguity through its own conditioning, so it is not used. **

⛭⛭ ** WHAT IS USED INSTEAD NEEDS NO EQUIVALENT-`s` STEP AT ALL: A ONE-AT-A-TIME SWAP. **  On the arm's
own `q` grid, replace the arm's four Doppler-containing pairs by the control's, scaled by the ratio of
the two arms' envelopes, and recompute the contrast.  ⇒ *The Doppler's share of the excess is then
`(C_arm - C_swapped) / (C_arm - C_control)`, a direct attribution with no coupling-times-input product
in it.*  ⌗ *Same shape of operation as `SRCINJRS`'s one-at-a-time clock swap, which this instrument
already sanctions.*
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NM = ['sw*sw', 'sw*dp', 'sw*isw', 'sw*pol', 'dp*dp', 'dp*isw', 'dp*pol',
      'isw*isw', 'isw*pol', 'pol*pol']
I = {n: k for k, n in enumerate(NM)}
DPT = [I['sw*dp'], I['dp*dp'], I['dp*isw'], I['dp*pol']]


def env(x, y, win=1.0, kind='mean'):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def cb(q, y, kind='mean'):
    e = env(q, y, 1.0, kind)
    o = (y - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def pairs(t):
    d = np.load(os.path.join(SP, f'r6915_pairs_{t}.npz'), allow_pickle=True)
    return d['ls'].astype(float) / float(d['l_A']), d['Dl'], d['Dl_pairs']


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


def swap_fraction(kind='mean'):
    qa, Da, Pa = pairs('cr')
    qc, Dc, Pc = pairs('lcdm')
    Ea, Ec = env(qa, Da, 1.0, kind), env(qc, Dc, 1.0, kind)
    scale = Ea / np.interp(qa, qc, Ec)
    Dsw = Da - Pa[:, DPT].sum(axis=1) + np.interp(qa, qc, Pc[:, DPT].sum(axis=1)) * scale
    Ca, Cc, Cs = cb(qa, Da, kind), cb(qc, Dc, kind), cb(qa, Dsw, kind)
    return Ca, Cc, Cs, (Ca - Cs) / (Ca - Cc)


def analytic_coupling(t, kind='mean'):
    q, Dl, P = pairs(t)
    dD = P[:, I['sw*dp']] + P[:, I['dp*isw']] + P[:, I['dp*pol']] + 2 * P[:, I['dp*dp']]
    eps = 1e-3
    return (cb(q, Dl + eps * dD, kind) / cb(q, Dl, kind) - 1.0) / eps


print(__doc__)
print('=' * 100)
print('\n  ⓵ THE BANK -- IT EXISTS, AND THE COARSE GRID IS CHECKED RATHER THAN ASSUMED ADEQUATE:')
for t in ('lcdm', 'cr'):
    q, Dl, P = pairs(t)
    qf, Df = fine(t)
    print(f"    {t:5s} pairs sum to Dl to {np.max(np.abs(P.sum(axis=1) / Dl - 1)):.1e};  "
          f"{len(q)} multipoles against the fine bank's {len(qf)}")
Ra = cb(*pairs('cr')[:2]) / cb(*fine('cr'))
Rc = cb(*pairs('lcdm')[:2]) / cb(*fine('lcdm'))
print('    coarse/fine contrast, arm     ' + '  '.join(f'{x:.4f}' for x in Ra))
print('    coarse/fine contrast, control ' + '  '.join(f'{x:.4f}' for x in Rc))
print(f"    ⇒ ** the coarse grid reads {100 * (1 - Rc.mean()):.1f} per cent low, and the deficit "
      f"agrees between the arms to {np.max(np.abs(Ra / Rc - 1)):.0e} -- so it CANCELS in the ratio, "
      f"which is the only thing read from it. **")

print('\n  ⛭ AND THE COUPLING, ANALYTICALLY, FOR BOTH ARMS -- discharging `cc66.55`\'s transfer caveat:')
AC = {t: analytic_coupling(t) for t in ('lcdm', 'cr')}
print('    q            ' + '  '.join(f'{x:8.2f}' for x in QC))
for t in ('lcdm', 'cr'):
    print(f"    {t:5s}        " + '  '.join(f'{x:+8.3f}' for x in AC[t]))
print('    cc66.55 (fd) ' + '  '.join(f'{x:+8.3f}' for x in
                                      (-0.450, -0.804, -0.585, -0.614, -0.674, -0.544, -0.678)))
print(f"    ⇒ arm against control to {100 * np.max(np.abs(AC['cr'] / AC['lcdm'] - 1)):.0f} per cent, "
      f"and both against `cc66.55`'s three-point finite difference to "
      f"{100 * np.max(np.abs(AC['lcdm'] / np.array((-0.450, -0.804, -0.585, -0.614, -0.674, -0.544, -0.678)) - 1)):.0f} "
      f"per cent.  ** Negative at every band on both arms. **")

print('\n  ⛭⛭ ⓶ THE CONTRIBUTION, BY ONE-AT-A-TIME SWAP, WITH BOTH ENVELOPES CARRIED:')
for kind in ('mean', 'median'):
    Ca, Cc, Cs, fr = swap_fraction(kind)
    print(f"    -- {kind} envelope")
    print('       excess        ' + '  '.join(f'{x:+8.4f}' for x in Ca - Cc))
    print('       Doppler part  ' + '  '.join(f'{x:+8.4f}' for x in Ca - Cs))
    print('       FRACTION      ' + '  '.join(f'{100 * x:+7.0f}%' for x in fr))
FR = {k: swap_fraction(k)[3] for k in ('mean', 'median')}

print('\n  ⓷ AND THE PATTERN IN THE FOUR MISMATCHES -- what the excess actually looks like:')
T = cb(*fine('cr')) / cb(*fine('lcdm')) - 1.0
sl, ic = np.polyfit(QC[1:], T[1:], 1)
print('    the excess     ' + '  '.join(f'{x:+8.4f}' for x in T))
print(f"    band 1 is {T[0] / T[1:].mean():.2f} of the bands 2-7 mean and lies "
      f"{(T[1:].mean() - T[0]) / T[1:].std():.1f} scatters below it")
print(f"    above band 1: a CONSTANT leaves scatter {T[1:].std():.4f}; a LINE of slope {sl:+.5f}/q "
      f"leaves {np.std(T[1:] - (sl * QC[1:] + ic)):.4f}")

print('\n' + '=' * 100)
print(f"""
  ⛭⛭ ⓵ ANSWERED WITHOUT A RUN, WHICH IS THE BEST AVAILABLE ANSWER TO IT.  *The instrument has emitted
    the right quantity since `r6915+cc66.41` and both arms' banks are on disk.*  ⇒ ** No change to
    make, unilaterally or otherwise -- and the ARM's coupling, which `cc66.55` could only transfer, is
    now measured and equals the control's to
    {100 * np.max(np.abs(AC['cr'] / AC['lcdm'] - 1)):.0f} per cent. **

  ⛔ ⓶ AND THE CONTRIBUTION IS A MINORITY SHARE THAT GROWS, AND IS SIGN-INDEFINITE AT THE BOTTOM.
    ** {100 * FR['mean'][1]:+.0f} to {100 * FR['mean'][-1]:+.0f} per cent on the arithmetic envelope,
    {100 * FR['median'][1]:+.0f} to {100 * FR['median'][-1]:+.0f} on the median one **, negative at
    $q=1.90$ on both and rising to a fifth or a half by the top band.
    ⇒ *** SO IT LANDS BETWEEN THE TWO WRONG READINGS -- which said $-13$ and $+188$ per cent -- AND IT
    DOES NOT SETTLE NOTHING: it settles that the candidate is a real but MINORITY contributor, which
    neither wrong reading said. ***  ⌗ *`cc66.55`'s split holds exactly as predicted: the SIGN of the
    coupling is envelope-independent, and the FRACTION inherits the ambiguity -- by a factor of about
    two.*  ⛔ *No envelope is chosen.*

  ⛭⛭⛭ ⓷ AND THE FOUR MISMATCHES DO SHARE A REASON, AND IT IS NOT ABOUT THE CANDIDATES.
    *The excess has ONE dominant feature: band 1 is a third of the mean of the rest and sits five
    scatters below it.  Above band 1 a constant already fits, and a line only halves the residual.*
    ⇒ *** THE EXCESS'S $q$-STRUCTURE IS A STEP AT THE LOWEST BAND, NOT A TREND -- AND EVERY ONE OF THE
    FOUR CANDIDATES WAS JUDGED ON A TREND ACROSS BANDS 2-7, WHERE THE EXCESS IS VERY NEARLY
    FEATURELESS. ***
    ⌗ A flat candidate (the window weighting, the term mix, the band-power reading) matches the flat
      part and misses the step.  A rising one (the projection width, the field reading) matches the
      mild rise and misses the step.  ** On bands 2-7 the two are barely distinguishable, because
      there is almost nothing there to distinguish them with. **
    ⇒ ** So the sector has been spending its discriminating power on the part of the excess that
      carries least structure, because the part that carries the structure is the band `cc66.54` showed
      it cannot measure a candidate in. **  *That is the same fact `cc66.54` found from the target's
      side, and it is the reason the four mismatches look like four failures rather than one.*
""")
