"""r7093 (70) -- the one number the order asks for: the arm-to-control contrast statistic read on a banked pair
from EACH configuration.  Nothing is run.  The statistic is the band-RMS-ratio receipt's own (oscillation about a
running mean over one unit of q = ell/l_A, ratio sum(A*B)/sum(B*B) on q in [0.85, 5.75]).

  model A -- the code's DEFAULT: LEAFSCALES unset (stacking rate), ZSTART unset (onset solved for l_A = 301.6):
             spectra/c54.178_{cr,lcdm}.npz  and  spectra/c54.186_{cr,lcdm}_L3000.npz
  model B -- LEAFSCALES=1 ZSTART=3e7, at the 185-bin refit minimum (refit_grid185/verify.sh):
             spectra/cc66_r185_verify_{cr,lcdm}.npz ;  and at the refit grid's base: refit_grid185/{cr,lcdm}_base.npz
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
LO, HI, NG = 0.85, 5.75, 1200


def env_a(x, y, win=1.0):
    e = np.empty_like(y, dtype=float)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(f):
    z = np.load(os.path.join(BW, f))
    q = z['ls'].astype(float) / float(z['l_A'])
    y = np.asarray(z['Dl'], float)
    e = env_a(q, y)
    x = np.linspace(LO, HI, NG)
    return np.interp(x, q, (y - e) / e), float(z['l_A']), float(z['r_s'])


PAIRS = [('A  default, solved onset   c54.178', 'spectra/c54.178_cr.npz', 'spectra/c54.178_lcdm.npz'),
         ('A  default, solved onset   c54.186 L3000', 'spectra/c54.186_cr_L3000.npz', 'spectra/c54.186_lcdm_L3000.npz'),
         ('B  LEAFSCALES=1 ZSTART=3e7 refit grid base', 'refit_grid185/cr_base.npz', 'refit_grid185/lcdm_base.npz'),
         ('B  LEAFSCALES=1 ZSTART=3e7 refit minimum (verify)', 'spectra/cc66_r185_verify_cr.npz', 'spectra/cc66_r185_verify_lcdm.npz')]
print(f'{"pair":52s} {"CR l_A":>8s} {"CR r_s":>8s} {"ctl l_A":>8s}  {"projected ratio":>15s} {"RMS ratio":>10s} {"phase cos":>10s}')
for lab, c, l in PAIRS:
    a, la, ra = osc(c)
    b, lb, _ = osc(l)
    proj = float(np.sum(a * b) / np.sum(b * b))
    rms = float(np.sqrt(np.sum(a * a) / np.sum(b * b)))
    cos = float(np.sum(a * b) / np.sqrt(np.sum(a * a) * np.sum(b * b)))
    print(f'{lab:52s} {la:8.3f} {ra:8.3f} {lb:8.3f}  {proj:15.4f} {rms:10.4f} {cos:10.4f}')
print('  projected = the receipts\' statistic, sum(A*B)/sum(B*B), which mixes amplitude with phase;')
print('  RMS ratio = amplitude only;  phase cos = sum(A*B)/|A||B|, 1 when the two oscillations are in phase in q.')
