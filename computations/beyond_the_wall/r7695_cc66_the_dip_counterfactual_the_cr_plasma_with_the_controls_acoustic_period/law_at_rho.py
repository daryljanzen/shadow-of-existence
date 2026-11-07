"""r7695+cc66 -- THE ACCEPTANCE LAW AT A SCALED COMB PERIOD, with the identity leg as its control.

`A_l = |INT W_l exp(2 i k r_s*) dk| / INT W_l dk`, `W_l = G_l^2 dk/k`, `G_l = INT v j_l(k x0) deta`.
`COMBRHO` scales the SOURCE's k and touches neither the kernel nor the visibility nor the measure, so
`W` is unchanged and only the phase moves: the counterfactual's own law is `A` at `rho * r_s*`.

TWO LEGS, AND THE FIRST IS WHAT MAKES THE SECOND WORTH HAVING:
  * `A(rho = 1)` must reproduce the BANKED `A` to floating point on every multipole -- otherwise `W`
    or the normalisation is mine and not the bank's, and "the law at a different period" would be my
    own integral wearing the bank's name;
  * `A(rho)` must DIFFER from it, or the scaling is plumbed to nothing.

    python3 law_at_rho.py [RHO]     writes A__rho into the cache beside this file
"""
import os
import sys

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, '..', 'spectra'))
CACHE = os.path.join(HERE, 'law_at_rho_cache.npz')
RHO = float(sys.argv[1]) if len(sys.argv) > 1 else 0.9945919371


def W_and_A(bank, rho):
    """(W per multipole, A at rho*r_s*) -- the bank's own inputs, the law's own expression"""
    d = np.load(os.path.join(SP, bank), allow_pickle=True)
    ls = d['ls__fixed'].astype(int)
    k = np.asarray(d['k__fixed'], float)
    ee = np.asarray(d['eta__fixed'], float)
    x0 = np.asarray(d['x0__fixed'], float)
    v = np.asarray(d['vis__fixed'], float)
    RS = float(d['r_s__fixed'])
    dk = np.gradient(k)
    A = np.full(len(ls), np.nan)
    for i, l in enumerate(ls):
        J = spherical_jn(int(l), k[None, :] * x0[:, None])
        G = np.trapezoid(v[:, None] * J, ee, axis=0)
        W = G ** 2 * dk / k
        sw = float(W.sum())
        if sw > 0:
            A[i] = abs(np.sum(W * np.exp(2j * k * (rho * RS)))) / sw
    return ls, np.asarray(d['l_A__fixed'], float), np.asarray(d['A'], float), A, RS


print(f"  THE LAW AT rho = {RHO:.10f}, on the arm's acceptance bank")
ls, lA, A_bank, A_1, RS = W_and_A('r7041_accept_cr_leafrec1.npz', 1.0)
_fin = np.isfinite(A_bank) & np.isfinite(A_1)
_d1 = float(np.max(np.abs(A_1[_fin] - A_bank[_fin])))
print(f"    ⛭ LEG 1 (the identity): A(rho=1) against the BANKED A, {int(_fin.sum())} multipoles, "
      f"max |diff| = {_d1:.3e}")
_ok1 = _d1 < 1e-12
print(f"       {'✔ the route IS the bank s own' if _ok1 else '⛔ [FAIL] the route is NOT the bank s'}")

_, _, _, A_r, _ = W_and_A('r7041_accept_cr_leafrec1.npz', RHO)
_d2 = float(np.max(np.abs(A_r[_fin] - A_bank[_fin])))
print(f"    ⛭ LEG 2 (the inverse): A(rho) against the banked A, max |diff| = {_d2:.3e}")
_ok2 = _d2 > 1e-6
print(f"       {'✔ the scaling is wired' if _ok2 else '⛔ [FAIL] the scaling is plumbed to nothing'}")

np.savez(CACHE, ls=ls, l_A=lA, A_bank=A_bank, A_identity=A_1, A_rho=A_r, rho=RHO, r_s=RS,
         leg1_maxdiff=_d1, leg2_maxdiff=_d2)
print(f"\n    r_s* = {RS:.6f} -> {RHO * RS:.6f}  ({100*(RHO-1):+.4f} per cent)")
print(f"    -> {os.path.relpath(CACHE, os.path.abspath(os.path.join(HERE, '..', '..', '..')))}")
raise SystemExit(0 if (_ok1 and _ok2) else 1)
