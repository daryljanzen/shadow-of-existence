"""⓵ THE RECONCILIATION -- which quantity does each path measure? -- r6997+cc66.51.

⛔ *Nothing is RUN: the order's ⓸.  Both quantities are rebuilt from `spectra/r6897_fields.npz`, the
`ZPSAVE` bank the register's own receipt reads, and from `r6959_eta_*`'s per-band term profiles.*

** THE DISAGREEMENT AS IT STOOD. **  `THE_REGISTER` records the dipole-to-monopole ratio at the
visibility peak as *two per cent ABOVE the control's and rising with wavenumber*.  `cc66.50` read it, on
the same profiles, as *fourteen per cent BELOW and flat*.  ⇒ **Fourteen per cent and a sign, on a channel
this sector has quoted for revisions.**
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
FLD = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
NF = 3.0
g = lambda n, t: FLD[f'{n}__{t}']


def amp_ratio(t, half=2.0, amp_deg=2, step=0.25):
    """THE REGISTER'S QUANTITY, rebuilt from its own receipt: the ratio of the OSCILLATION AMPLITUDES
    of the Doppler and monopole source fields at last scattering, each normalised by Psi, from a
    sliding sinusoid fit in q."""
    k = g('k', t)
    o = np.argsort(k)
    k = k[o]
    psi = g('psi', t)[o]
    um = (g('th0', t)[o] + psi) / psi
    ud = (g('tb', t)[o] / k) / psi
    q = k * float(g('r_s', t)) / np.pi
    Q, RT = [], []
    for q0 in np.arange(1.5 + half, q.max() - half - 0.1, step):
        m = np.abs(q - q0) <= half
        if m.sum() < 20:
            continue
        dq = q[m] - q0
        cols = [np.ones(int(m.sum()))]
        for j in range(amp_deg + 1):
            cols += [dq ** j * np.cos(np.pi * q[m]), dq ** j * np.sin(np.pi * q[m])]
        X = np.column_stack(cols)
        bm = np.linalg.lstsq(X, um[m], rcond=None)[0]
        bd = np.linalg.lstsq(X, ud[m], rcond=None)[0]
        Q.append(q0)
        RT.append(float(np.hypot(bd[1], bd[2]) / np.hypot(bm[1], bm[2])))
    return np.array(Q), np.array(RT)


def band_power(d, key):
    """`cc66.50`'s QUANTITY: the term's INTEGRATED BAND POWER over the visibility window."""
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    return np.array([float(np.trapezoid(d[key][m][:, b], ee[m])) for b in range(len(QC))])


print(__doc__)
print('=' * 104)
AR = {t: amp_ratio(t) for t in ('lcdm', 'cr')}
print(f"\n  the register's fit covers q = {AR['lcdm'][0].min():.2f} to {AR['lcdm'][0].max():.2f};  "
      f"cc66.50's bands cover q = {QC[0]:.2f} to {QC[-1]:.2f}")

print('\n⓵a  THE TWO QUANTITIES ARE DIFFERENT IN THREE INDEPENDENT WAYS, WHICH IS THE WHOLE ANSWER.')
print('      1. WHAT IS RATIOED.  The register takes the OSCILLATION AMPLITUDE of each source field')
print('         -- a sinusoid fitted in q, its amplitude hypot(cos, sin).  cc66.50 takes the')
print('         INTEGRATED BAND POWER of each term, which includes the smooth part.')
print('      2. WHICH FIELDS.  The register uses the SOURCE fields at last scattering, each divided')
print('         by Psi: (Theta_0+Psi)/Psi against (theta_b/k)/Psi.  cc66.50 uses the terms\'')
print('         contributions to the projected integrand, w2sw and w2dp.')
print('      3. OVER WHAT RANGE.  The register fits q in [3.5, 11]; cc66.50 bands q in [1.2, 5.4].')
print('         ⇒ The two ranges overlap over less than half of either.')

print('\n⓵b  AND PUT ON THE SAME FOOTING THEY DO NOT CONTRADICT -- each is right about its own object.')
QD = np.arange(3.5, 11.0, 0.25)
arl = np.interp(QD, AR['lcdm'][0], AR['lcdm'][1])
arc = np.interp(QD, AR['cr'][0], AR['cr'][1])
reg = arc / arl
print(f"      the register's quantity over ITS range  q in [3.5, 11]:   "
      f"{reg.mean():.4f}  ({100 * (reg.mean() - 1):+.2f}%)")
QD2 = np.arange(QC[0], QC[-1] + 0.01, 0.25)
m2 = (QD2 >= AR['lcdm'][0].min()) & (QD2 <= AR['lcdm'][0].max())
arl2 = np.interp(QD2[m2], AR['lcdm'][0], AR['lcdm'][1])
arc2 = np.interp(QD2[m2], AR['cr'][0], AR['cr'][1])
reg2 = arc2 / arl2
print(f"      the SAME quantity over cc66.50's range  q in "
      f"[{QD2[m2].min():.2f}, {QD2[m2].max():.2f}]:  {reg2.mean():.4f}  ({100 * (reg2.mean() - 1):+.2f}%)")
pw = ((band_power(A['cr'], 'w2dp') / band_power(A['cr'], 'w2sw'))
      / (band_power(A['lcdm'], 'w2dp') / band_power(A['lcdm'], 'w2sw')))
print(f"      cc66.50's quantity over cc66.50's range:                  "
      f"{np.sqrt(pw).mean():.4f}  ({100 * (np.sqrt(pw).mean() - 1):+.2f}%)  [amplitude = sqrt(power)]")


print('\n⓵c  ⇒ SO THE SIGN DIFFERENCE IS NOT THE RANGE, IT IS THE QUANTITY.')
print('      The register\'s quantity is ABOVE the control on BOTH ranges (+2.06% and +0.95%);')
print('      cc66.50\'s is BELOW on the same range (-11.58%).  ** Neither reading is wrong and they')
print('      are not in contradiction: they are ratios of different things. **')

print('\n⓵d  AND WHICH ONE THE TROUGH-FILLING ARGUMENT NEEDS, WHICH IS WHAT THE ORDER ASKED.')
print('      Trough-filling is the Doppler term, a quarter period out of phase, adding INTO the')
print('      troughs of the monopole\'s oscillation.  What fills a trough is the OSCILLATING part\'s')
print('      amplitude relative to the monopole\'s oscillating part; the smooth part of either term')
print('      displaces the envelope and fills nothing.')
print('      ⇒ ** THE REGISTER\'S QUANTITY IS THE RIGHT ONE FOR THE TROUGH-FILLING ARGUMENT, AND')
print('        cc66.50\'s IS NOT. **  An integrated band power mixes the smooth part back in.')
print('      ⛔ AND THE SAME IS TRUE OF THE FILTER, WHICH IS THIS SEAT\'S OWN ERROR TO OWN: the')
print('        contrast statistic is the standard deviation of the OSCILLATION about a running-mean')
print('        envelope, so the quantity that could carry its q-dependence is an oscillation')
print('        amplitude.  ⇒ *cc66.50 filtered this candidate on integrated band power and that row')
print('        of its table is answering the wrong question.*')

# ==================================================================================================
print('\n⓵e  CAN THE RIGHT QUANTITY BE MEASURED OVER THE FILTER\'S RANGE AT ALL?  The register\'s fit')
print('      starts at q = 3.5 because its sliding window is half-width 2 in q, and the filter needs')
print('      q down to 1.2.  A narrower window reaches lower -- and the question is whether it is')
print('      still measuring the same thing.  *Tested rather than assumed:*\n')
print(f"      {'half':>6s} {'q_min':>7s} {'overlap mean on [3.7,5.2]':>27s}   verdict")
REF = None
for half in (2.0, 1.5, 1.0, 0.75, 0.5):
    try:
        ql, rl = amp_ratio('lcdm', half=half)
        qc, rc = amp_ratio('cr', half=half)
    except Exception as e:
        print(f"      {half:6.2f}   fit failed: {e}")
        continue
    lo = max(ql.min(), qc.min())
    gd = np.arange(3.7, 5.21, 0.1)
    if lo > gd.min():
        ov = float('nan')
    else:
        ov = float((np.interp(gd, qc, rc) / np.interp(gd, ql, rl)).mean())
    if REF is None:
        REF = ov
    d = abs(ov / REF - 1) if REF and np.isfinite(ov) else float('nan')
    v = ('reference' if half == 2.0 else
         ('agrees with the reference to %.1f%%' % (100 * d) if d < 0.02 else
          'DIVERGES from the reference by %.1f%% -- not the same measurement' % (100 * d)))
    print(f"      {half:6.2f} {lo:7.2f} {ov:27.5f}   {v}")


# ==================================================================================================
print('\n⓵f  ⛔ AND THE RIGHT QUANTITY BOTTOMS OUT AT q = 2.0, WHERE THE FILTER NEEDS 1.2.')
print('      The narrow windows agree with the reference to a tenth of a per cent, so the')
print('      measurement is sound -- it simply does not reach.  A sinusoid amplitude needs at least')
print('      about one period of q either side, and the acoustic period in q is 2.')
print('      ⇒ ** So the growth statistic cannot be formed over the filter\'s own range for this')
print('        candidate, and the honest move is to restrict BOTH to the range they share. **\n')
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def bands(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = env_a(q, d['Dl'])
    o = (d['Dl'] - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


R = bands(F['cr']) / bands(F['lcdm'])
ql, rl = amp_ratio('lcdm', half=0.5)
qc, rc = amp_ratio('cr', half=0.5)
CAND = np.interp(QC, qc, rc) / np.interp(QC, ql, rl)
lo_i = int(np.argmax(QC >= 2.0))
print(f"      {'q':>6s} {'target (r-1)':>14s} {'candidate (r-1)':>18s}")
for i in range(len(QC)):
    mark = '  <- below the candidate\'s floor' if i < lo_i else ''
    c = '   --- ' if i < lo_i else f"{CAND[i] - 1:18.5f}"
    print(f"      {QC[i]:6.2f} {R[i] - 1:14.5f} {c}{mark}")


def G_c(y, i0, i1):
    """⛔ THE GROWTH STATISTIC HAS A DOMAIN, AND THIS CANDIDATE IS OUTSIDE IT.

    G = (r-1) at the top over (r-1) at the bottom is scale-free and right for a departure that keeps
    one sign across the range, which every candidate in `cc66.50`'s table did.  *This one does not:
    its departure CROSSES ZERO near q = 2.6, so the denominator is a small difference of a number from
    itself and G is not a ratio of anything.*  ⇒ **Reported as UNDEFINED rather than as the large
    number the arithmetic returns**, which would have read as a spectacular pass.
    """
    d0, d1 = y[i0] - 1, y[i1] - 1
    if abs(d0) < 0.005:
        return None
    return float(d1 / d0)


print(f"\n      growth over the FULL range  q = {QC[0]:.2f} to {QC[-1]:.2f}:  target G = "
      f"{G_c(R, 0, -1):.2f},  candidate NOT MEASURABLE (no data below q = 2)")
_gc = G_c(CAND, lo_i, -1)
print(f"      growth over the SHARED range q = {QC[lo_i]:.2f} to {QC[-1]:.2f}:  target G = "
      f"{G_c(R, lo_i, -1):.2f},  candidate G = "
      + ("UNDEFINED -- its departure crosses zero at the bottom of this range "
         f"({CAND[lo_i] - 1:+.5f}), so G is not a ratio" if _gc is None else f"{_gc:.2f}"))
print(f"      the candidate's departure instead runs {CAND[lo_i] - 1:+.5f} -> {CAND[-1] - 1:+.5f}"
      f" across that range, i.e. it grows FROM ABOUT NOTHING")
cur_t = float(np.polyfit(QC[lo_i:], R[lo_i:] - 1, 2)[0])
cur_c = float(np.polyfit(QC[lo_i:], CAND[lo_i:] - 1, 2)[0])
print(f"      curvature over the shared range:      target {cur_t:+.5f},  candidate {cur_c:+.5f}"
      f"   -- SAME SIGN, both decelerating")

print('\n  ⇒ ⓶ THE SECOND TOOTH IS USED, AND IT IS USED BECAUSE SOMETHING SURVIVED THE FIRST.')
print('    On the range where the RIGHT quantity can be measured, the candidate grows from about')
print('    nothing to two per cent and DECELERATES, with the same curvature sign as the target.')
print('    ⇒ ** So it passes both teeth where it can be tested -- which reverses cc66.50\'s')
print('      dismissal of it, and the reversal is this seat\'s own error and not new data: that')
print('      revision filtered the candidate on integrated band power, which is the wrong object. **')
print('\n  ⛔ AND YET THE FILTER STILL CANNOT CLOSE IT, WHICH IS THE RESULT AND NOT A GAP.')
print(f'    The target grows {G_c(R, 0, -1):.2f}-fold over the full range and only '
      f'{G_c(R, lo_i, -1):.2f}-fold over the shared one:')
print('    ** the target\'s growth is concentrated BELOW q = 2, which is exactly where the only')
print('    quantity that could carry it cannot be measured by this method. **  ⇒ *Passing both')
print('    teeth on [2.6, 5.4] is therefore weaker than it sounds: it is a pass on the part of the')
print('    range that carries least of the thing being explained.*')
print('\n  ⌗ WHAT WOULD CLOSE IT, stated so the next order can price it: a measurement of the')
print('    oscillation-amplitude ratio below q = 2.  The sinusoid fit cannot go there -- the')
print('    acoustic period in q is 2 and the fit needs about a period either side -- so it needs a')
print('    different estimator of the same quantity, not a longer run of this one.')
