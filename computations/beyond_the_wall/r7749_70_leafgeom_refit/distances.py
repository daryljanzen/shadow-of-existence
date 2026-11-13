"""r7749+70 Ⓒ: the distances on the leaf-rate assignment, beside the arm of record's.

theta_* = r_s / D_M(z_*) read from each run's own outputs (`r_s`, `D_M`), against Planck's 0.0104085
(the datum the distances' point is fitted to; P15 DESI receipt's THETA_OBS) at Planck's sigma 0.31e-5
(100 theta_* = 1.04110 +- 0.00031 => sigma(theta_*) = 3.1e-6).

BAO: DESI DR2 (arXiv:2503.14738 Table IV, 13 measurements), with the P15 DESI receipt's own data and
distance integrals copied verbatim.  The arm of record reads its geometry on the stacking rate (E_stack,
radiation-free); this assignment on the leaf rate (E_leaf, radiation included).  At a common r_d -- the one
that minimises the stacking-rate chi^2, so the comparison isolates the geometry -- both chi^2 are reported,
and each geometry's own best-r_d chi^2 as well.

Usage: python3 distances.py <A_nofit.npz> <V_verify.npz> [Bpoint H0 OM]
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(os.path.dirname(HERE), 'spectra')
trapz = np.trapezoid
c = 299792.458
DESI_ANISO = [(0.510, 13.588, 0.167, 21.863, 0.425, -0.459),
              (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
              (0.934, 21.576, 0.152, 17.641, 0.193, -0.416),
              (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
              (1.484, 30.512, 0.760, 12.817, 0.516, -0.500),
              (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
DESI_ISO = [(0.295, 7.942, 0.075)]
WR = 4.15e-5
THETA_OBS, THETA_SIG = 0.0104085, 3.1e-6


def E_stack(z, Om, h):
    return np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


def E_leaf(z, Om, h):
    return np.sqrt(Om * (1 + z) ** 3 + (WR / h ** 2) * (1 + z) ** 4 + (1 - Om))


def D_M(z, H0, Om, E, n=4000):
    zz = np.linspace(0, z, n)
    return trapz(c / (H0 * E(zz, Om, H0 / 100)), zz)


def D_H(z, H0, Om, E):
    return c / (H0 * E(z, Om, H0 / 100))


def D_V(z, H0, Om, E):
    return (z * D_M(z, H0, Om, E) ** 2 * D_H(z, H0, Om, E)) ** (1 / 3)


def chi2_bao(H0, Om, rd, E):
    x2 = 0.0
    for z, dm, sdm, dh, sdh, rho in DESI_ANISO:
        r = np.array([D_M(z, H0, Om, E) / rd - dm, D_H(z, H0, Om, E) / rd - dh])
        cov = np.array([[sdm ** 2, rho * sdm * sdh], [rho * sdm * sdh, sdh ** 2]])
        x2 += r @ np.linalg.solve(cov, r)
    for z, dv, sdv in DESI_ISO:
        x2 += ((D_V(z, H0, Om, E) / rd - dv) / sdv) ** 2
    return float(x2)


def bao(H0, Om):
    best_s = minimize_scalar(lambda rd: chi2_bao(H0, Om, rd, E_stack), bounds=(120, 170), method='bounded')
    best_l = minimize_scalar(lambda rd: chi2_bao(H0, Om, rd, E_leaf), bounds=(120, 170), method='bounded')
    rd = best_s.x
    return dict(rd_common=rd, stack_at_rd=chi2_bao(H0, Om, rd, E_stack), leaf_at_rd=chi2_bao(H0, Om, rd, E_leaf),
                stack_best=best_s.fun, leaf_best=best_l.fun, rd_leaf_best=best_l.x)


def theta(path):
    z = np.load(path, allow_pickle=True)
    t = float(z['r_s']) / float(z['D_M'])
    return dict(theta=t, l_A=float(z['l_A']), D_M=float(z['D_M']), r_s=float(z['r_s']),
                pull_sigma=(t - THETA_OBS) / THETA_SIG)


def main():
    a_npz, v_npz = sys.argv[1], sys.argv[2]
    out = {}
    out['theta'] = {
        "A arm of record (stacking D_M), distances' point": theta(os.path.join(SP, 'cc66_cr_x_h686_L2000_leafrec1_distances.npz')),
        "A leaf-rate D_M, distances' point": theta(a_npz),
        'B arm of record, refit point': theta(os.path.join(SP, 'cc66_r185_verify_cr_leafrec1.npz')),
        'B leaf-rate D_M, refit minimum': theta(v_npz),
    }
    pts = {"distances' point (68.60, 0.2973)": (68.60, 0.2973)}
    if len(sys.argv) > 4:
        pts['leaf-rate refit minimum'] = (float(sys.argv[3]), float(sys.argv[4]))
    out['bao'] = {k: bao(*v) for k, v in pts.items()}
    for k, v in out['theta'].items():
        print(f"  theta*  {k:>52}: 100 theta* {100 * v['theta']:.5f}  l_A {v['l_A']:.3f}  "
              f"D_M {v['D_M']:.1f}  r_s {v['r_s']:.3f}  pull {v['pull_sigma']:+.1f} sigma")
    for k, v in out['bao'].items():
        print(f"  BAO {k}: common r_d {v['rd_common']:.2f}: stacking {v['stack_at_rd']:.3f}, leaf {v['leaf_at_rd']:.3f} "
              f"(delta {v['leaf_at_rd'] - v['stack_at_rd']:+.4f}); each own best: {v['stack_best']:.3f} / {v['leaf_best']:.3f}")
    json.dump(out, open(os.path.join(HERE, 'distances.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
