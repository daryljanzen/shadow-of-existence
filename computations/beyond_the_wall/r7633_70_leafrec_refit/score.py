#!/usr/bin/env python3
"""r7633+70: the refitted ruled arm's fourth acoustic feature, scored.  Runs r7631's measure.py (PO-47's locator,
unchanged) on the refitted arm against the control, then the joint score over TT, EE and TE:
   distinguishability  sqrt(sum_s (d_s / sigma_s)^2), chi^2 with 3 dof, converted to a Gaussian sigma;
   which is off        chi^2_arm - chi^2_control, chi^2 = sum_s ((model_s - sky_s) / sigma_s)^2.
Correlations between the three spectra (shared sample variance) are not modelled -- stated, not hidden.
    python3 score.py REFIT_ARM_POL_NPZ CONTROL_POL_NPZ ACT_SACC"""
import os, re, subprocess, sys
import numpy as np
from scipy import stats
H = os.path.dirname(os.path.abspath(__file__))
out = subprocess.run([sys.executable, os.path.join(H, '..', 'r7631_70_PO87_polarisation', 'measure.py')] + sys.argv[1:4],
                     capture_output=True, text=True).stdout
out = '\n'.join(l for l in out.splitlines() if 'Warn' not in l and 'Assum' not in l)
print(out)
mod = {m[0]: (float(m[1]), float(m[2])) for m in re.findall(r'(TT|EE|TE): CR\s+([\d.]+)\s+control\s+([\d.]+)', out)}
sky = {}
for m in re.finditer(r'^\s+(TT|EE|TE)\s+(Planck|ACT)\s+([\d.]+)\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+([\d.]+)\s+([\d.]+)', out, re.M):
    sky[(m[1], m[2])] = (float(m[3]), float(m[4]), float(m[5]))
print("\n  PART 4 -- the joint score over TT, EE and TE (W = 55 / W = 80)")
for which in ('Planck', 'ACT', 'combined'):
    for wi, wl in ((1, 'W=55'), (2, 'W=80')):
        z2 = ca = cc = 0.0
        for s in ('TT', 'EE', 'TE'):
            a, c = mod[s]
            if which == 'combined':
                (lp, *sp), (la, *sa) = sky[(s, 'Planck')], sky[(s, 'ACT')]
                wp, wa = sp[wi - 1] ** -2, sa[wi - 1] ** -2
                l0, sg = (wp * lp + wa * la) / (wp + wa), (wp + wa) ** -0.5
            else:
                l0, *ss = sky[(s, which)]; sg = ss[wi - 1]
            z2 += ((a - c) / sg) ** 2; ca += ((a - l0) / sg) ** 2; cc += ((c - l0) / sg) ** 2
        p = stats.chi2.sf(z2, 3); zs = stats.norm.isf(p / 2)
        print(f"    {which:>8} {wl}: arms apart chi2 {z2:6.2f} (3 dof) = {zs:4.2f} sigma;   chi2 to sky: arm {ca:6.2f}, "
              f"control {cc:6.2f}, arm - control {ca - cc:+6.2f}")
