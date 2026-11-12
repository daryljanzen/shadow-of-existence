#!/usr/bin/env python3
"""`r7741+cc66` THE COMMITTED ARTEFACT FOR THE PAIRING CONTINUUM.

⛭ ** WHY AN ARTEFACT RATHER THAN A RECEIPT THAT COMPUTES. **  Each point of the continuum costs two
`G_l(k)` builds at about `33` minutes each -- `698` multipoles x `1450` wavenumbers x `560` nodes of
`spherical_jn` -- so the four points are some four hours and cannot run inside a receipt's budget.  The
inputs are also 70's `refs/ci` artefacts sitting in a scratchpad, not in the tree.  ⇒ *This reduces them
to the `l`-vectors the verdict is actually read off -- `A_l` per leg per pairing, and the two arms' maps
and visibilities -- which is `~75 KB` and commits.  Same route `r7733` took with `bank_binned.py`, and
for the same reason.*

⛔ ** WHAT THIS ARTEFACT DOES AND DOES NOT MAKE CHECKABLE. **  It makes the REDUCTION checkable: the
receipt recomputes every share, every ratio and the monotonicity from these vectors, and recomputes
`P1 == the scalar-1.0 member` from the maps themselves at full precision.  It does NOT re-derive the
`G` builds; those are upstream and are recorded here by the sha256 of each input.  ⌗ *Stated plainly
because a receipt that reduces a committed array can look like it verified the array.*

⛭ ** NO `PREDICTION.md` FOR `r7741`, AND THAT IS DELIBERATE. **  The register-before-computing rule
exists so an outcome cannot be fitted to a licence.  Every figure below was measured, reported and
MERGED at `r7739+cc66.2`-`.8` before `r7741` was written; this revision pins published numbers and
drafts prose for them.  ⇒ *There is nothing left to fit. The registration that governs these figures is
`r7739`'s, and the receipt names it.*
"""
import hashlib
import os
import sys

import numpy as np

D = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
     'scratchpad/tier')
SHA = {
    'r7737_grid.npz': '546977c4f05f2cffb4299900586f5a6d3ab452f561b13f9272a24bdab7dc7305',
    'r7737_vis.npz': 'c3da5390680d86b2f9dddcae3738a01e88974545b1a5d1ea4c36a2739ceb6ba4',
}
# the three P2 builds this seat made at r7739 (merged); their shas are recorded, not pinned, because
# they are this seat's own outputs rather than 70's handed-over artefacts
P2 = {'grid span': 'r7739_P2_grid_span.npz',
      'sigma (mine)': 'r7739_P2_sigma_(mine).npz',
      "70's W": 'r7739_P2_70s_W.npz'}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def A_of(G, k, dk, rs):
    Wl = G ** 2 * dk[None, :] / k[None, :]
    return np.abs((Wl * np.exp(2j * k[None, :] * rs)).sum(axis=1)) / Wl.sum(axis=1)


def main():
    for f, s in SHA.items():
        h = sha(os.path.join(D, f))
        if h != s:
            print(f"  ⛔ REFUSING: {f} sha256 {h} != recorded {s}")
            return 1
        print(f"  [ok] {f} is the object 70 recorded")

    Z = np.load(os.path.join(D, 'r7737_grid.npz'), allow_pickle=True)
    V = np.load(os.path.join(D, 'r7737_vis.npz'), allow_pickle=True)
    k, dk, ls = V['k'], V['dk'], V['ls']
    rs_l, rs_c = float(Z['r_s_lcdm']), float(Z['r_s_cr'])

    out = dict(ls=ls, rs_lcdm=rs_l, rs_cr=rs_c,
               D_M_lcdm=float(Z['D_M_lcdm']), D_M_cr=float(Z['D_M_cr']),
               x0_lcdm=Z['x0_lcdm'], x0_cr=Z['x0_cr'],
               vis_lcdm=Z['vis_lcdm'], vis_cr=Z['vis_cr'],
               eta_lcdm=Z['eta_lcdm'], eta_cr=Z['eta_cr'],
               W_lcdm=float(Z['eta_ls_w_lcdm']), W_cr=float(Z['eta_ls_w_cr']))

    # the common baseline and the comb-period leg, shared by every pairing
    out['A_base'] = A_of(V['G__g_lcdm__X_lcdm'], k, dk, rs_l)
    out['A_rs'] = A_of(V['G__g_lcdm__X_lcdm'], k, dk, rs_c)
    # P1: 70's own index-paired hybrids
    out['A_g__P1'] = A_of(V['G__g_cr__X_lcdm'], k, dk, rs_l)
    out['A_x__P1'] = A_of(V['G__g_lcdm__X_cr'], k, dk, rs_l)
    print(f"  [ok] P1 legs reduced from 70's own hybrids")

    shas = {f: sha(os.path.join(D, f)) for f in list(SHA) + list(P2.values())
            + ['r7739_norm_only.npz']}
    for name, f in P2.items():
        P = np.load(os.path.join(D, f))
        key = name.replace(' ', '_').replace("'", '')
        out[f'A_g__{key}'] = A_of(P['Gg'], k, dk, rs_l)
        out[f'A_x__{key}'] = A_of(P['Gx'], k, dk, rs_l)
        out[f'ratio__{key}'] = float(P['ratio'])
        print(f"  [ok] P2 / {name} legs reduced, ratio {float(P['ratio']):.6f}")

    N = np.load(os.path.join(D, 'r7739_norm_only.npz'))
    out['A_norm'] = A_of(N['Gn'], k, dk, rs_l)
    out['A_norm_rs_scaled'] = A_of(N['Gn'], k, dk, rs_l * float(N['xs']))
    out['xs'] = float(N['xs'])
    print(f"  [ok] the scalar-only leg reduced, xs {float(N['xs']):.10f}")

    out['input_sha'] = np.array([f"{f}={s}" for f, s in sorted(shas.items())])
    np.savez_compressed('r7741_continuum.npz', **out)
    n = os.path.getsize('r7741_continuum.npz')
    print(f"\n  wrote r7741_continuum.npz, {n} bytes")
    for line in out['input_sha']:
        print(f"      {line}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
