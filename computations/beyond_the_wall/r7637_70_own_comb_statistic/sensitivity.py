"""r7637+70: the own-comb statistic's null at r7055's DECLARED-SENSITIVITY amplitude (each bank's own fitted comb
amplitude) beside the pre-registered 0.5 -- on both arms, worst over phase and at the real phase (phase 0)."""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own_comb as oc  # noqa: E402

SP = os.path.join(oc.ROOT, 'computations', 'beyond_the_wall', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)


def bank(name):
    d = np.load(os.path.join(SP, name))
    return d['ls'].astype(float) / float(d['l_A']), np.asarray(d['Dl'], float)


own = lambda b, q: oc.band_excess_own(b, q)[0]  # noqa: E731
for lab, arm in (('old arm', 'r6941_fine_cr.npz'), ('arm of record', 'r6941_fine_cr_leafrec1.npz')):
    B = {'lcdm': bank('r6941_fine_lcdm.npz'), 'cr': bank(arm)}
    amp = float(np.mean([oc.comb(*B[t])[3] for t in B]))
    for sname, st in (('shared', oc.band_excess_shared), ('own', own)):
        E = st(B, QE)
        s, r = oc.step(E), oc.rise(E, QE)
        for A in (0.5, amp):
            N = oc.null(B, QE, st, A)
            print(f"  {lab:14s} {sname:6s} A {A:.3f}: step {s:+.4f} null real {N[0, 0]:+.4f} worst {np.abs(N[:, 0]).max():.4f}"
                  f" ({np.abs(N[:, 0]).max() / abs(s):.2f})  step-null(real) {s - N[0, 0]:+.4f} | rise {r:+.4f} null real "
                  f"{N[0, 1]:+.4f} worst {np.abs(N[:, 1]).max():.4f} ({np.abs(N[:, 1]).max() / abs(r):.2f})  rise-null(real) {r - N[0, 1]:+.4f}")
