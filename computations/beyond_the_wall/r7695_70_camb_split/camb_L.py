#!/usr/bin/env python3
"""r7695+70 step 2: arm A carried onto the arm of record's construction (L).

CAMB's exact Boltzmann state (stock 2.0.4, unmodified; the low-l receipt's `armA` parameters) is extracted in the Newtonian
gauge at the times HIER's grid maps to, and handed to HIER's own source assembly and the arm-B harness's own depth
arithmetic. HIER is imported with SPLITCLOCK=<mode> (unset = one clock, the gate; L = the arm of record), so the projection
-- chi = eta_0 - eta on that grid, the visibility in that grid's measure (built from CAMB's own opacity), Psi on that grid's
H -- is the one arm B (L) uses. Only the dynamics differ between the two arms.

Usage: python3 camb_L.py <point: distances|refit> <mode: one|L>   -> prints __R__ {json}
"""
import contextlib
import io
import json
import os
import sys

import numpy as np
from scipy.interpolate import interp1d
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
PT, MODE = sys.argv[1], sys.argv[2]
POINTS = {'refit': (68.570730, 0.291246, 0.021643, {'OBF': f'{0.021643 / 0.02237:.12f}', 'ORF': f'{4.15 / 4.1833:.12f}'}),
          'distances': (68.60, 0.2973, 0.02237, {})}
H0, Om, WB, PENV = POINTS[PT]
for k in ('SPLITCLOCK', 'SPLITIC', 'ARM', 'ETADEC', 'ETAEND'):
    os.environ.pop(k, None)
os.environ.update(PENV)
os.environ.update({'KMAXL': '700', 'H0_L': '%.10f' % H0, 'OMF': '%.12f' % (Om / 0.3150)})
if MODE == 'L':
    os.environ['SPLITCLOCK'] = 'L'
sys.path.insert(0, os.path.join(ROOT, 'storyboard_receipts'))
with contextlib.redirect_stdout(io.StringIO()):
    import HIER_photon_hierarchy as H
import camb  # noqa: E402
import camb.symbolic as sy  # noqa: E402

C, NS, LMAX = 299792.458, 0.9649, 48


def r0_of(H0, Om):
    OL = 1.0 - Om
    return 2.0 ** (1 / 3) * (C / (H0 * np.sqrt(3 * OL))) * np.sinh(np.arcsinh(np.sqrt(OL / Om))) ** (2 / 3)


# --- CAMB, exactly armA's construction
h = H0 / 100
pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=WB, omch2=Om * h * h - WB - 0.06 / 93.14, mnu=0.06, tau=0.0544)
pars.InitPower.set_params(As=2.1e-9, ns=NS)
pars.set_for_lmax(LMAX + 8, lens_potential_accuracy=0)
pars.set_accuracy(AccuracyBoost=3, lSampleBoost=50, lAccuracyBoost=3)
res = camb.get_results(pars)

# --- the harness's k set (identical construction)
R0 = r0_of(H0, Om)
Ls = np.arange(2, 260); kL = np.sqrt(Ls * (Ls + 2)) / R0
KLO, NLOW = 0.1, 320
kd = np.exp(np.linspace(np.log(kL[0] * KLO), np.log(kL[-1]), NLOW))
kk = np.unique(np.concatenate([kL, kd]))

# --- the grid: from eta_rec-160 (as the harness) to eta_0, fine through recombination, then coarser
e0, er = float(H.eta_0), float(H.eta_rec)
ee = np.unique(np.concatenate([np.linspace(er - 160, er + 400, 2801), np.linspace(er + 400, e0 - 1e-3, 3001)]))
a_of = interp1d(H.eg, np.log(H.ag), kind='cubic')
aa = np.exp(a_of(ee))
tauC = np.asarray(res.conformal_time(1 / aa - 1), float)       # CAMB's (leaf) conformal time at each grid time
assert np.all(np.diff(tauC) > 0)
VARS = [sy.Delta_g, sy.v_b, sy.Phi_N, sy.Psi_N, sy.polter, sy.opacity]
ev = res.get_time_evolution(kk, tauC, VARS, frame='Newtonian')  # (nk, nt, nvar)
ev = np.transpose(ev, (1, 0, 2))                                 # (nt, nk, nvar)
dg, vb, Ph, Ps, pol, opac = (ev[:, :, j] for j in range(6))
op = opac[:, 0]
# visibility in the GRID measure from CAMB's own opacity (one clock: CAMB's own; L: kappa over d eta_stack)
seg = 0.5 * (op[1:] + op[:-1]) * np.diff(ee)
tau = np.concatenate([np.cumsum(seg[::-1])[::-1], [0.0]])
g = op * np.exp(-tau)
Hl = np.array([float(H._Hdyn(e)) for e in ee])[:, None]          # the leaf conformal H HIER's dynamics read
On = np.array([float(H.On_of(e)) for e in ee])[:, None]
Yv = np.zeros((len(ee), len(kk), 6))
Yv[:, :, 0] = dg / 4                                             # Theta_0
Yv[:, :, 1] = kk[None, :] * vb                                   # theta_b
Yv[:, :, 2] = Ph                                                 # Phi
Yv[:, :, 3] = (Ph - Ps) * kk[None, :] ** 2 / (6 * Hl ** 2 * On)  # sigma_nu,eff: HIER's formula returns CAMB's Psi on H_leaf
Yv[:, :, 4] = 0.0
Yv[:, :, 5] = 10.0 * pol                                         # Pi_F
with contextlib.redirect_stdout(io.StringIO()):
    Sm, Sd, Si, Sq = H.source_terms(ee, Yv, kk, g, tau)

# --- the harness's depth arithmetic, verbatim
has_q = Sq is not None; x0m = H.eta_0 - ee; lnk = np.log(kk); _u, _ix = np.unique(lnk, return_index=True)


def Delta(l):
    X = kk[None, :] * x0m[:, None]
    jl = spherical_jn(int(l), X); jlp = spherical_jn(int(l), X, derivative=True)
    it = Sm * jl + Sd * jlp + Si * jl
    if has_q:
        Xs = np.maximum(X, 1e-8)
        it = it + Sq * 2.0 * (-3.0 * jlp / Xs + (3.0 * l * (l + 1) / (2.0 * Xs ** 2) - 1.0) * jl)
    return np.trapezoid(it, ee, axis=0)


wL = (Ls + 1.0) / (Ls * (Ls + 2.0)); ls = np.arange(2, 45)
Cc = np.zeros(len(ls)); Cd = np.zeros(len(ls))
for i, l in enumerate(ls):
    D = Delta(l)
    Cc[i] = np.trapezoid(kk ** (0.9649 - 1.0) * D ** 2, lnk)
    f = interp1d(_u, D[_ix], kind='cubic', bounds_error=False, fill_value=0.0)
    Cd[i] = np.sum(wL * kL ** (0.9649 - 1.0) * f(np.log(kL)) ** 2)


def pl(Cq):
    d = Cq * ls * (ls + 1); return d / np.mean(d[(ls >= 25) & (ls <= 40)])


r = pl(Cd) / pl(Cc)
print('__R__' + json.dumps(dict(point=PT, mode=MODE, depths=[float(x) for x in r[:7]], eta_0=e0, eta_rec=er,
                                nk=len(kk), nt=len(ee), tau_reion_end=float(tau[np.searchsorted(ee, er + 400)]),
                                camb=camb.__version__, SPLITCLOCK=os.environ.get('SPLITCLOCK'))))
