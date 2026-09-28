"""⓶ ENUMERATE WHAT IN THIS ARM HAS THE TARGET'S SHAPE, AND FILTER ON PAPER -- r6993+cc66.50.

⛔ *The order's ⓸: nothing is RUN here.  Every number below comes from banks already on disk -- the
`SRCETA` per-band term profiles from `r6959` and the two banked channel responses -- so a candidate is
filtered before a run is spent on it, which is the point of having a filter at all.*

** THE FILTER, AS ⓵ LEFT IT AND NOT AS THE ORDER FIRST STATED IT. **  The order set the criterion as
"vary across wavenumber by something near forty-four per cent of its own value".  ⓵ sharpens that in the
direction that matters: *** the target is a CONCAVE, DECELERATING rise. ***  A rise linear in q^2 is
EXCLUDED at chi^2/nu = 4.66 -- and that is the corpus's own working parametrisation.  ⇒ **So the filter
has two teeth, not one: a candidate must vary by enough, AND it must decelerate.  Anything flat fails the
first; anything that accelerates like a damping term fails the second, however large it is.**
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
WIN = np.load(os.path.join(SP, 'r6959_nswap_lcdm.npz'))
MIX = np.load(os.path.join(SP, 'r6975_mix_lcdm.npz'))
JNT = np.load(os.path.join(SP, 'r6983_joint_lcdm.npz'))

QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
NF = 3.0
TERMS = (('monopole  w2sw', 'w2sw'), ('Doppler   w2dp', 'w2dp'), ('early ISW w2isw', 'w2isw'),
         ('polarisn  w2pol', 'w2pol'), ('monop.dot w2md', 'w2md'), ('full src  w2', 'w2'))


def band_power(d, key):
    """the term's band power, integrated over the visibility window -- `cc66.48`'s own reading"""
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    return np.array([float(np.trapezoid(d[key][m][:, b], ee[m])) for b in range(len(QC))])


def shape_stats(r):
    """⛔ THE FILTER STATISTIC, AND THE FIRST ONE I WROTE WAS NOT COMPARABLE ACROSS CANDIDATES.

    *The sector quotes |slope x <q^2>| / |intercept| on ln r.  That divides by ln r at q=0, so a
    candidate sitting at r ~ 0.78 is divided by 0.25 where the excess at r ~ 1.04 is divided by 0.04 --
    the same shape reads twenty times larger at the lower level.  It is a fine statistic for ONE
    quantity near unity and a bad one for comparing several at different levels, which is what a filter
    has to do.*

    ⇒ ** So the filter is the GROWTH OF THE DEPARTURE FROM UNITY across the measured range, which is
    scale-free and is exactly what "carries the wavenumber dependence" means: ** G = (r-1) at the top
    band divided by (r-1) at the bottom.  The target is G = 3.54.  The second tooth is the curvature of
    (r-1) against q, which must be negative.
    """
    d = r - 1.0
    G = float(d[-1] / d[0]) if abs(d[0]) > 1e-9 else float('nan')
    c = float(np.polyfit(QC, d, 2)[0])
    return G, c


print(__doc__)
print('=' * 104)
TGT = None
print()
print(f"  {'candidate':32s} {'(r-1) at q=1.2':>15s} {'(r-1) at q=5.4':>15s} {'growth G':>9s} {'curv':>9s}  verdict")


def row(lbl, r, target=False):
    G, c = shape_stats(r)
    global TGT
    if target:
        TGT = (G, c)
        v = '<- THE TARGET'
    elif not np.isfinite(G):
        v = 'no departure to speak of'
    elif G < 2.0:
        v = 'TOO FLAT -- its departure barely grows'
    elif c > 0:
        v = 'ACCELERATES -- wrong curvature'
    else:
        v = '** SHAPE MATCH -- survives both teeth **'
    print(f"  {lbl:32s} {r[0] - 1:>15.5f} {r[-1] - 1:>15.5f} {G:>9.2f} {c:>+9.5f}  {v}")


def _env(x, y, w=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        mm = (x >= v - w / 2) & (x <= v + w / 2)
        e[j] = np.mean(y[mm])
    return e


def _b(dd):
    qq = dd['ls'].astype(float) / float(dd['l_A'])
    ee = _env(qq, dd['Dl'])
    oo = (dd['Dl'] - ee) / ee
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), qq, oo)))
                     for a, b in zip(QE[:-1], QE[1:])])


C0 = _b(F['lcdm'])
row('THE MEASURED EXCESS', _b(F['cr']) / C0, target=True)
print()
for lbl, key in TERMS:
    row(f'source term: {lbl}', band_power(A['cr'], key) / band_power(A['lcdm'], key))
rn = band_power(A['cr'], 'w2dp') / band_power(A['cr'], 'w2sw')
rd = band_power(A['lcdm'], 'w2dp') / band_power(A['lcdm'], 'w2sw')
row('dipole/monopole ratio', rn / rd)
print()
for lbl, d in (('channel: window  (cc66.47)', WIN), ('channel: term mix (cc66.48)', MIX),
               ('channel: the pair (cc66.49)', JNT)):
    row(lbl, _b(d) / C0)

print(f"\n  ⇒ THE TARGET IS G = {TGT[0]:.2f} WITH NEGATIVE CURVATURE.  A candidate must reach a comparable")
print("    growth AND decelerate.  ⌗ *The order named the dipole-to-monopole ratio as the one thing in the")
print("    register already measured to rise with q.  It is in the table, read from the same profiles, and")
print("    it is reported as the filter finds it rather than as the order expected it.*")


# ==================================================================================================
print('\n  ⚠ AND THE ORDER\'S NAMED CANDIDATE DISAGREES WITH THE REGISTER, WHICH IS REPORTED AND NOT')
print('    RESOLVED HERE.  The register records the dipole-to-monopole ratio as "two per cent ABOVE')
print('    the control\'s and RISING with q".  Read from `r6959`\'s profiles on the HIERARCHY path,')
print('    at each arm\'s own visibility peak:\n')


def at_peak(d, key):
    return d[key][int(np.argmax(d['vis'])), :]


_rn = at_peak(A['cr'], 'w2dp') / at_peak(A['cr'], 'w2sw')
_rd = at_peak(A['lcdm'], 'w2dp') / at_peak(A['lcdm'], 'w2sw')
_amp = np.sqrt(_rn / _rd)
print('      q          ' + '  '.join(f'{x:6.2f}' for x in QC))
print('      amplitude  ' + '  '.join(f'{x:.4f}' for x in _amp))
_d = _amp - 1
print(f'\n    ⇒ it sits {100 * (1 - _amp.mean()):.0f} per cent BELOW the control, not two per cent above, and its')
print(f'      departure grows by G = {_d[-1] / _d[0]:.2f} with curvature {np.polyfit(QC, _d, 2)[0]:+.5f} -- flat, and if')
print('      anything accelerating.  ** It fails both teeth of the filter as measured here. **')
print('    ⛔ *That is NOT a refutation of the register\'s number.  The register\'s reading may be the')
print('      LINE-OF-SIGHT path, or a different definition, and this receipt reads only the hierarchy')
print('      path.  ⇒ What is owed before this candidate is closed is which quantity the register')
print('      measured, and that is named here rather than settled.*')
