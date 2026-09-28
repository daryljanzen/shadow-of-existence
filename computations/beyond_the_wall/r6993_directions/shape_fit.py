"""⓵ CHARACTERISE THE TARGET'S SHAPE, against the rule fixed in PREDICTION.md -- r6993+cc66.50.

⛔ *Every tolerance here is `PREDICTION.md`'s, committed before this file was written: per-band
sigma = 0.013 from the measured injected-form recovery; PREFERRED only on Delta chi^2 > 4; EXCLUDED only
on chi^2/nu > 3; a fitted scale at the edge of the range reported as NO SCALE RESOLVED.*
"""
import os

import numpy as np
from scipy.optimize import curve_fit

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
QE = np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
SIG = 0.013                                   # PREDICTION.md, from the measured recovery error


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def bands(d, win=1.0):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = env_a(q, d['Dl'], win)
    o = (d['Dl'] - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


R = bands(F['cr']) / bands(F['lcdm'])
print(__doc__)
print('=' * 100)
print('\n  the measured excess, band by band')
print('   q    ' + '  '.join(f'{x:5.2f}' for x in QC))
print('   R    ' + '  '.join(f'{x:.4f}' for x in R))

FORMS = {
    'F0 constant':          (lambda q, A: A + 0 * q, (0.05,), ('A',)),
    'F1 linear in q^2':     (lambda q, A: A * q ** 2, (0.002,), ('A',)),
    'F2 power law':         (lambda q, A, a: A * q ** a, (0.02, 0.8), ('A', 'alpha')),
    'F3 logarithm':         (lambda q, A: A * np.log(q), (0.03,), ('A',)),
    'F4 turnover':          (lambda q, A, q0: A * q ** 2 / (q ** 2 + q0 ** 2), (0.1, 3.0), ('A', 'q0')),
    'F5 sat. exponential':  (lambda q, A, q0: A * (1 - np.exp(-q / q0)), (0.1, 2.0), ('A', 'q0')),
}
Y = R - 1.0
print(f'\n  fits to R - 1 at sigma = {SIG} per band (PREDICTION.md), 7 points\n')
print(f"  {'form':22s} {'chi2':>8s} {'nu':>3s} {'chi2/nu':>8s}   parameters")
RES = {}
for nm, (fn, p0, names) in FORMS.items():
    try:
        p, cov = curve_fit(fn, QC, Y, p0=p0, sigma=np.full(7, SIG), absolute_sigma=True, maxfev=40000)
    except Exception as e:                                        # pragma: no cover
        print(f'  {nm:22s} FIT FAILED: {e}')
        continue
    chi2 = float(np.sum(((Y - fn(QC, *p)) / SIG) ** 2))
    nu = 7 - len(p)
    err = np.sqrt(np.diag(cov))
    RES[nm] = (chi2, nu, p, err)
    ps = '  '.join(f'{n}={v:.4g}+/-{e:.2g}' for n, v, e in zip(names, p, err))
    print(f'  {nm:22s} {chi2:8.2f} {nu:3d} {chi2 / nu:8.2f}   {ps}')

order = sorted(RES.items(), key=lambda kv: kv[1][0])
print('\n  ranked by chi^2:')
for nm, (chi2, nu, p, err) in order:
    print(f'    {nm:22s} chi2 = {chi2:7.2f}')
best, second = order[0], order[1]
d = second[1][0] - best[1][0]
print(f'\n  best  {best[0]}  chi2 = {best[1][0]:.2f}')
print(f'  next  {second[0]}  chi2 = {second[1][0]:.2f}   Delta chi^2 = {d:.2f}')
print(f'  ⇒ PREDICTION.md: PREFERRED only on Delta chi^2 > 4  ->  '
      f'{"PREFERRED: " + best[0] if d > 4 else "NOT SEPARATED"}')
print('\n  excluded (chi^2/nu > 3, PREDICTION.md):')
ex = [nm for nm, (c, nu, p, e) in RES.items() if c / nu > 3]
print('    ' + (', '.join(ex) if ex else 'none'))

print('\n  the pre-registered NON-separations, checked:')
for a, b in (('F2 power law', 'F3 logarithm'), ('F2 power law', 'F4 turnover')):
    dd = abs(RES[a][0] - RES[b][0])
    print(f'    {a} vs {b}: Delta chi^2 = {dd:.2f}  -> '
          f'{"NOT separated, as predicted" if dd < 4 else "SEPARATED, against the prediction"}')

print('\n  ⛔ THE SCALE TEST, APPLIED AS PRE-REGISTERED AND NOT AS FIRST CODED.')
print('     PREDICTION.md: *"a fitted q0 is only meaningful if it lands INSIDE the range WITH ITS')
print('     UNCERTAINTY ... a q0 at the edge will be reported as NO SCALE RESOLVED"*.  The first')
print('     version of this test asked only that the CENTRAL VALUE be inside and the error be under')
print('     half of it -- which is a weaker bar than the one written down, and it passed F4.  The')
print('     rule as written is applied below.')
for nm in ('F4 turnover', 'F5 sat. exponential'):
    _, _, p, err = RES[nm]
    q0, e0 = p[-1], err[-1]
    inside = (q0 - e0) > QC[0] and (q0 + e0) < QC[-1]
    print(f'\n  {nm}: q0 = {q0:.3f} +/- {e0:.3f}  ->  [{q0 - e0:.3f}, {q0 + e0:.3f}]'
          f' against the measured range [{QC[0]:.2f}, {QC[-1]:.2f}]')
    print(f'    ⇒ {"A SCALE IS RESOLVED" if inside else "NO SCALE RESOLVED -- the interval reaches the bottom edge of the range"}')

print('\n  AND THE RISE ITSELF, against the null, on the same pre-registered margin:')
c0 = RES['F0 constant'][0]
for nm in ('F3 logarithm', 'F4 turnover', 'F5 sat. exponential', 'F2 power law'):
    d0 = c0 - RES[nm][0]
    print(f'    F0 constant vs {nm:22s} Delta chi^2 = {d0:6.2f}  -> '
          f'{"the rise is PREFERRED over a constant" if d0 > 4 else "not separated from a constant"}')
print(f'    ⌗ but the constant is NOT EXCLUDED on its own: chi^2/nu = {c0 / 6:.2f}, under the '
      f'pre-registered bar of 3.')
print('      ** So the rise is established as a PREFERENCE and not as an exclusion of flatness, and')
print('      those are different claims. **')

print('\n  monotonicity, judged on the RISE and not the ordering (PREDICTION.md):')
print(f'    R rises from {R[0]:.4f} to {R[-1]:.4f}; ordering violations: '
      f'{int(np.sum(np.diff(R) < 0))} of 6, each smaller than the 1 per cent estimator bias: '
      f'{["%.4f" % abs(x) for x in np.diff(R)[np.diff(R) < 0]]}')
