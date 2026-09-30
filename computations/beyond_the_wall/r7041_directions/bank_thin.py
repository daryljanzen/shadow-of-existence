"""fold the acceptance law's inputs into a THIN bank a registered receipt can actually read.

** THE PROBLEM THIS SOLVES. **  `DLKSAVE`'s full transfer is (n_multipole x n_mode) and comes to 15.5 MB
the pair -- forty-three times the largest bank `spectra/` tracks, so it is deliberately untracked
(`.gitignore`).  *But a receipt that reads an untracked bank is a receipt that is RED in CI*, and a
receipt nobody can run is not a receipt.

⇒ ** So the bank is thinned rather than the receipt weakened. **  Almost all of the 15.5 MB is `Dlk`
itself; every quantity the law is BUILT from is one-dimensional:
  * `eta`, `x0`, `vis`     -- the window the kernel reads, which is the whole of the law's input
  * `k`, `P`, `r_s`, `ns`  -- the k axis and its measure
  * `ls`, `Dl`, `l_A`      -- the spectrum the prediction is tested against
  * `A`, `dkw`             -- the law's OUTPUT, so a reader can see it without recomputing all of it
  * `Dlk` for `NSAMP` multipoles only -- enough to re-derive the factorisation and `A` from scratch

⌗ ** The receipt RECOMPUTES G_l and A_l for the sampled multipoles from `vis`, `x0` and `k` and checks
them against the banked `A`. **  So the banked law is gated by re-derivation and not taken on trust, and
the cost is bounded by `NSAMP` rather than by the multipole grid.
"""
import os
import sys

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
NSAMP = 8
LO, HI = 0.85, 5.75


def main():
    for t in ('lcdm', 'cr'):
        src = os.path.join(SP, f'r7039_transfer_{t}.npz')
        if not os.path.exists(src):
            print(f"  ⛔ `spectra/r7039_transfer_{t}.npz` is not on disk -- regenerate with")
            print("     `r7039_directions/launch.sh` then its `bank.py`.")
            return 1
        d = np.load(src)
        out = {}
        for tag in ('fixed', 'sweepown'):
            ls = d[f'ls__{tag}'].astype(int)
            k = d[f'k__{tag}']
            ee, x0, v = d[f'eta__{tag}'], d[f'x0__{tag}'], d[f'vis__{tag}']
            RS, ns = float(d[f'r_s__{tag}']), float(d[f'ns__{tag}'])
            lA = float(d[f'l_A__{tag}'])
            dk = np.gradient(k)
            q = ls / lA
            # the law, on every multipole, banked as its OUTPUT
            A = np.full(len(ls), np.nan)
            dkw = np.full(len(ls), np.nan)
            for i, l in enumerate(ls):
                J = spherical_jn(int(l), k[None, :] * x0[:, None])
                G = np.trapezoid(v[:, None] * J, ee, axis=0)
                W = G ** 2 * dk / k
                s = W.sum()
                if s > 0:
                    A[i] = abs(np.sum(W * np.exp(2j * k * RS))) / s
                    kb = np.sum(W * k) / s
                    dkw[i] = 2 * np.sqrt(max(np.sum(W * (k - kb) ** 2) / s, 0.0))
            # ** the sampled multipoles are spread ACROSS the reported q range, not taken from one end,
            # so the factorisation gate cannot pass on a corner of the grid. **
            inr = np.where((q >= LO) & (q <= HI))[0]
            samp = inr[np.linspace(0, len(inr) - 1, NSAMP).round().astype(int)]
            out[f'ls__{tag}'] = ls
            out[f'q__{tag}'] = q
            out[f'Dl__{tag}'] = d[f'Dl__{tag}']
            out[f'k__{tag}'] = k
            out[f'P__{tag}'] = d[f'P__{tag}']
            out[f'eta__{tag}'] = ee
            out[f'x0__{tag}'] = x0
            out[f'vis__{tag}'] = v
            out[f'A__{tag}'] = A
            out[f'dkw__{tag}'] = dkw
            out[f'samp__{tag}'] = samp
            out[f'Dlk_samp__{tag}'] = d[f'Dlk__{tag}'][samp]
            for qn in ('l_A', 'D_M', 'r_s', 'arm', 'ns', 'eta_ls', 'eta_ls_w',
                       'nlos', 'nlosw', 'nlosf', 'inj', 'inj_rs', 'inj_vis', 'inj_ph'):
                out[f'{qn}__{tag}'] = d[f'{qn}__{tag}']
            out[f'closes__{tag}'] = d[f'closes__{tag}']
        dst = os.path.join(SP, f'r7041_accept_{t}.npz')
        np.savez(dst, nsamp=np.array(NSAMP), **out)
        mb = os.path.getsize(dst) / 1e6
        print(f"  {t}: 2 injections, {NSAMP} sampled multipoles each -> "
              f"spectra/r7041_accept_{t}.npz ({mb:.3f} MB, from "
              f"{os.path.getsize(src)/1e6:.1f} MB)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
