#!/usr/bin/env python3
"""r7471+70 -- the displacement Delta(W) at the SETTLED ratio r = 0.9918, by the joint-fit receipt's own
machinery (its baseline, binning, covariance, windows and fitter), with only R changed.  Not scaled."""
import importlib.util, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                   'P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma.py')
spec = importlib.util.spec_from_file_location('jf', src)
jf = importlib.util.module_from_spec(spec); spec.loader.exec_module(jf)
WINDOWS = ((100, 1760), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508))
out = {}
for R in (1.0926, 0.9918):
    jf.R = R; jf.K = R ** 2 - 1
    print(f'  r = {R}   (r^2 - 1 = {jf.K:+.5f})')
    for lo, hi in WINDOWS:
        keep = jf.window(lo, hi); F, _ = jf._fisher(keep)
        target = jf.CS.bin_spectrum(jf.LS, jf.DL * jf.sig(jf.LS))[keep]
        dn, sdn, c, A, r, _ = jf.joint(target, keep, F)
        out[(R, lo, hi)] = dn
        print(f'      {lo:5d}-{hi:<5d}  bins {int(keep.sum()):4d}   Delta n_s = {dn:+.5f}')
D = [out[(0.9918, lo, hi)] for lo, hi in WINDOWS]
ref = [out[(1.0926, lo, hi)] for lo, hi in WINDOWS]
ok = abs(ref[0] - (-0.08304)) < 2e-4 and abs(ref[4] - (-0.52084)) < 5e-4
print(f'  reproduces the receipt table at r = 1.0926: {"OK" if ok else "FAIL"}')
print(f'  at r = 0.9918: spread S = {max(D) - min(D):.5f}   (min {min(D):+.5f}, max {max(D):+.5f}; ratio {max(D)/min(D):.2f})')
np.save(os.path.join(HERE, 'displacement.npy'), np.array(D))
sys.exit(0 if ok else 1)
