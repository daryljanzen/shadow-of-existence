"""r7695+cc66 -- THE ACCEPTANCE LAW AT A SCALED COMB PERIOD, with the identity leg as its control.

`A_l = |INT W_l exp(2 i k r_s*) dk| / INT W_l dk`, `W_l = G_l^2 dk/k`, `G_l = INT v j_l(k x0) deta`.
`COMBRHO` scales the SOURCE's k and touches neither the kernel nor the visibility nor the measure, so
`W` is unchanged and only the phase moves: the counterfactual's own law is `A` at `rho * r_s*`.

⛭⛭ ** `W` IS BUILT ONCE AND REUSED, AND THAT IS NOT AN OPTIMISATION -- IT IS THE FINDING. **
`BEFORE_READING_IT.md` registers that `W` is independent of `r_s*`; a script that rebuilt it per `rho`
would be asserting the opposite in code while the note asserted it in prose.  *The first form of this
file did exactly that -- two full Bessel loops over 238 multipoles x 560 etas x 1452 modes for one
quantity that does not depend on the parameter being varied -- which was twice the cost for nothing and
a contradiction of its own premise.*

TWO LEGS, AND THE FIRST IS WHAT MAKES THE SECOND WORTH HAVING:
  * `A(rho = 1)` must reproduce the BANKED `A` to floating point on every multipole -- otherwise `W`
    or the normalisation is mine and not the bank's, and "the law at a different period" would be my
    own integral wearing the bank's name;
  * `A(rho)` must DIFFER from it, or the scaling is plumbed to nothing.

    python3 law_at_rho.py [RHO]     writes the two A columns into the cache beside this file
"""
import os
import sys
import time

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, '..', 'spectra'))
CACHE = os.path.join(HERE, 'law_at_rho_cache.npz')
WCACHE = os.path.join(HERE, 'law_W_cache.npz')
RHO = float(sys.argv[1]) if len(sys.argv) > 1 else 0.9945919371
BANK = 'r7041_accept_cr_leafrec1.npz'


def projection_window():   # r7701 (69): renamed from `kernel` -- the C71/C72/C81 census reads any function named for a kernel as a null-space solver
    """W_l and k, built once from the bank's own inputs.  Independent of r_s*, hence of rho."""
    d = np.load(os.path.join(SP, BANK), allow_pickle=True)
    ls = d['ls__fixed'].astype(int)
    k = np.asarray(d['k__fixed'], float)
    ee = np.asarray(d['eta__fixed'], float)
    x0 = np.asarray(d['x0__fixed'], float)
    v = np.asarray(d['vis__fixed'], float)
    dk = np.gradient(k)
    if os.path.exists(WCACHE):
        _c = np.load(WCACHE)
        if _c['n'].shape == () and np.array_equal(np.asarray(_c['ls'], int), ls) \
                and np.array_equal(np.asarray(_c['k'], float), k):
            print(f"    W read from the cache beside this file ({len(ls)} multipoles)")
            return ls, k, np.asarray(_c['W'], float), float(d['r_s__fixed']), \
                np.asarray(d['l_A__fixed'], float), np.asarray(d['A'], float)
    W = np.empty((len(ls), len(k)))
    _t0 = time.time()
    for i, l in enumerate(ls):
        J = spherical_jn(int(l), k[None, :] * x0[:, None])
        G = np.trapezoid(v[:, None] * J, ee, axis=0)
        W[i] = G ** 2 * dk / k
        if i % 40 == 0:
            print(f"    W: {i+1}/{len(ls)} multipoles, {time.time()-_t0:.0f}s", flush=True)
    np.savez(WCACHE, ls=ls, k=k, W=W, n=np.array(len(ls)))
    print(f"    W built once in {time.time()-_t0:.0f}s and cached")
    return ls, k, W, float(d['r_s__fixed']), np.asarray(d['l_A__fixed'], float), \
        np.asarray(d['A'], float)


def A_at(k, W, rs):
    """the law, one sum per multipole -- the only thing rho changes"""
    out = np.full(len(W), np.nan)
    ph = np.exp(2j * k * rs)
    sw = W.sum(axis=1)
    ok = sw > 0
    out[ok] = np.abs(W[ok] @ ph) / sw[ok]
    return out


print(f"  THE LAW AT rho = {RHO:.10f}, on the arm's acceptance bank")
ls, k, W, RS, lA, A_bank = projection_window()
A_1 = A_at(k, W, RS)
A_r = A_at(k, W, RHO * RS)

_fin = np.isfinite(A_bank) & np.isfinite(A_1)
_d1 = float(np.max(np.abs(A_1[_fin] - A_bank[_fin])))
_ok1 = _d1 < 1e-12
print(f"    ⛭ LEG 1 (the identity): A(rho=1) against the BANKED A, {int(_fin.sum())} multipoles, "
      f"max |diff| = {_d1:.3e}")
print(f"       {'✔ the route IS the bank s own' if _ok1 else '⛔ [FAIL] the route is NOT the bank s'}")
_d2 = float(np.max(np.abs(A_r[_fin] - A_bank[_fin])))
_ok2 = _d2 > 1e-6
print(f"    ⛭ LEG 2 (the inverse): A(rho) against the banked A, max |diff| = {_d2:.3e}")
print(f"       {'✔ the scaling is wired' if _ok2 else '⛔ [FAIL] the scaling is plumbed to nothing'}")

np.savez(CACHE, ls=ls, l_A=lA, A_bank=A_bank, A_identity=A_1, A_rho=A_r, rho=RHO, r_s=RS,
         leg1_maxdiff=_d1, leg2_maxdiff=_d2)
print(f"\n    r_s* = {RS:.6f} -> {RHO * RS:.6f}  ({100*(RHO-1):+.4f} per cent)")
print(f"    -> {os.path.basename(CACHE)}")
raise SystemExit(0 if (_ok1 and _ok2) else 1)
