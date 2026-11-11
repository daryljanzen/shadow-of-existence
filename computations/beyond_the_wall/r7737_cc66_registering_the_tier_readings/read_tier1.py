#!/usr/bin/env python3
"""`r7737+cc66` TIER 1 READ — the registered Part A, run on 70's `r7737_xmap`.

⛭ `PREDICTION.md` Part A, registered and pushed at `r7737+cc66.0` before this build existed.
⛔ Two departures from that registration are forced by what landed, and BOTH are declared here rather
   than worked around:
     * `S1` (`F_shape`, the map's own geometry) is **NOT COMPUTABLE**: the blob carries no `x0` or
       `eta` arrays, only `x0_at_peak` as two scalars in its closure.  It is reported as not computed,
       with the one available point beside it, and NOT replaced by a different statistic.
     * `S5` asked how far the result moves under a SECOND INTERPOLATION of the map onto the other
       arm's time grid.  70 declares `"pairing": "grid index"` -- there IS no interpolation, so the
       statistic as registered has no subject.  What index pairing ASSUMES is stated instead, and the
       assumption is named as unmeasured here because the grids are not in the blob.
"""
import hashlib
import json
import os
import sys

import numpy as np

D = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
     'scratchpad/tier')
XMAP = os.path.join(D, 'r7737_xmap.npz')
R7729 = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
         'scratchpad/dlk/r7729_dlk_four.npz')
SHA_XMAP = '0314f844023623f12775a9137373e273cb80b743d8e992af6eb29ea19d55a3a7'
SHA_R7729 = '3fbad4d34030cf0ee36e43ccbe30dc630039996d9a5cfa6316fd85917760ccb9'
R_SHAPE_LO, R_SHAPE_HI = 0.20, 0.80       # registered A.3
S3_LINE = 0.80                             # registered A.4
TOL_ID = 1e-12
BINS = {'PRIMARY': 12, 'SECONDARY': 23}
FAILS = []


def gate(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def wrms(X, W):
    return float(np.sqrt((W * X ** 2).sum() / W.sum()))


def binned(X, w):
    n = X.shape[1] // w
    return X[:, :n * w].reshape(X.shape[0], n, w).sum(axis=2)


def split_l(X, W):
    """the `k`-only part (weighted mean over `l` per column) and the `l`-structured remainder"""
    cw = W.sum(axis=0, keepdims=True)
    flat = np.where(cw > 0, (W * X).sum(axis=0, keepdims=True) / np.where(cw > 0, cw, 1.0), 0.0)
    return np.broadcast_to(flat, X.shape), X - flat


def main():
    print(__doc__)
    print("=" * 100)
    for p, s in ((XMAP, SHA_XMAP), (R7729, SHA_R7729)):
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        gate('input', h == s, f"{os.path.basename(p)} is the object 70 recorded", h)
    if FAILS:
        print("  ⛔ REFUSING: an input is not the recorded one")
        return 1
    X = np.load(XMAP, allow_pickle=True)
    Z = np.load(R7729, allow_pickle=True)
    meta = json.loads(str(X['meta'].item()))
    pairing = meta['closure']['grid']['pairing']
    peak = meta['closure']['grid']['x0_at_peak']
    print(f"\n    70 declares the pairing as: {pairing!r}")

    # ---------------------------------------------------------------- S4, the refusal, MY OWN version
    #  70's C5 says six hybrids with the source arm's own map return the diagonal.  Checked here
    #  independently and differently: the two builds' DIAGONALS must be the same arrays bit for bit,
    #  because `S_A__X_A` and `S_A__K_A` are the same object built by two separate runs.
    same = []
    for arm in ('lcdm', 'cr'):
        same.append((f'Dlk {arm}', np.array_equal(X[f'Dlk__S_{arm}__X_{arm}'],
                                                  Z[f'Dlk__S_{arm}__K_{arm}'])))
        same.append((f'P {arm}', np.array_equal(X[f'P__S_{arm}__X_{arm}'],
                                                Z[f'P__S_{arm}__K_{arm}'])))
    same.append(('ls', np.array_equal(X['ls'], Z['ls'])))
    same.append(('k', np.array_equal(X['k'], Z['k'])))
    gate('S4a', all(v for _, v in same),
         "the two builds' DIAGONALS are the same arrays bit for bit -- my own check, not 70's C5",
         ', '.join(f"{n}: {'=' if v else 'DIFFER'}" for n, v in same))
    gate('S4b', meta['closure']['C5']['identical'] == meta['closure']['C5']['checked']
         and meta['closure']['C5']['ok'],
         "and 70's own C5 -- the hybrid built with the source arm's own map returns the diagonal",
         f"{meta['closure']['C5']['identical']} of {meta['closure']['C5']['checked']} identical")
    # the full arm swap must also be the same object in both builds
    gate('S4c', np.array_equal(X['Dlk__S_cr__X_cr'], Z['Dlk__S_cr__K_cr'])
         and np.array_equal(X['Dlk__S_lcdm__X_lcdm'], Z['Dlk__S_lcdm__K_lcdm']),
         "so the FULL ARM SWAP is the identical object in the two builds, and the legs are "
         "comparable across them")
    if FAILS:
        print("  ⛔ REFUSING: the registration makes S4 a refusal, and it did not pass")
        return 1

    # ---------------------------------------------------------------- S1, declared not computable
    print(f"\n    ⛔ S1 NOT COMPUTED -- the blob carries no `x0` or `eta` arrays, so `F_shape` has no "
          f"subject here.")
    print(f"       The ONE available point is 70's own `x0_at_peak`: lcdm {peak['lcdm']!r}, "
          f"cr {peak['cr']!r}")
    rp = peak['cr'] / peak['lcdm']
    xs = json.loads(json.loads(str(Z['meta'].item())))['closure']['grid']['xs']['S_lcdm__K_cr'] \
        if isinstance(json.loads(str(Z['meta'].item())), str) else None
    m2 = json.loads(str(Z['meta'].item()))
    while isinstance(m2, str):
        m2 = json.loads(m2)
    xs = m2['closure']['grid']['xs']['S_lcdm__K_cr']
    print(f"       their ratio {rp:.10f} against the distance ratio {xs!r}")
    print(f"       ⇒ they agree to {abs(rp / xs - 1):.3e} relative AT THAT ONE POINT, which is a "
          f"point and not the map.")

    # ---------------------------------------------------------------- the arena
    CX = ('S_lcdm__X_lcdm', 'S_lcdm__X_cr', 'S_cr__X_lcdm', 'S_cr__X_cr')
    MX = {c: X[f'P__{c}'][None, :] * X[f'Dlk__{c}'] ** 2 for c in CX}
    MK = {c: Z[f'P__{c}'][None, :] * Z[f'Dlk__{c}'] ** 2
          for c in ('S_lcdm__K_lcdm', 'S_lcdm__K_cr')}

    print(f"\n    ⛭ A.3 `S2` AND A.4 `S3`")
    out = {}
    for name, w in BINS.items():
        B = {c: binned(MX[c], w) for c in CX}
        Bn = binned(MK['S_lcdm__K_cr'], w)
        dead = np.zeros(B[CX[0]].shape, bool)
        for c in CX:
            dead |= B[c] <= 0
        dead |= Bn <= 0
        lg = lambda A: np.where(dead, 0.0, np.log(np.where(A > 0, A, 1.0)))
        base = lg(B['S_lcdm__X_lcdm'])
        u_map = lg(B['S_lcdm__X_cr']) - base          # the FULL map swap          (Tier 1, new)
        u_src = lg(B['S_cr__X_lcdm']) - base          # the source alone, map held  (Tier 1, new)
        obs = lg(B['S_cr__X_cr']) - base              # the full arm swap
        t_norm = lg(Bn) - base                        # the NORMALISATION only      (r7729)
        t_shape = u_map - t_norm
        W = B['S_lcdm__X_lcdm'] / B['S_lcdm__X_lcdm'].sum(axis=1, keepdims=True)
        W = np.where(dead, 0.0, W)

        R_shape = wrms(t_shape, W) / wrms(u_map, W)
        R_norm = wrms(t_norm, W) / wrms(u_map, W)
        # the three-term fit, for S3's apportionment
        sw = np.sqrt(W).ravel()
        A = np.column_stack([t_norm.ravel() * sw, t_shape.ravel() * sw, u_src.ravel() * sw])
        a = np.linalg.lstsq(A, obs.ravel() * sw, rcond=None)[0]
        parts = {'norm': a[0] * t_norm, 'shape': a[1] * t_shape, 'src': a[2] * u_src}
        lp = {kk: split_l(v, W)[1] for kk, v in parts.items()}
        var = {kk: float((W * v ** 2).sum() / W.sum()) for kk, v in lp.items()}
        cross = 0.0
        keys = list(lp)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                cross += 2 * float((W * lp[keys[i]] * lp[keys[j]]).sum() / W.sum())
        tot = sum(var.values()) + cross
        share = {kk: var[kk] / tot for kk in var}
        dist_leg = share['norm'] + share['shape']
        resid2 = wrms(obs - (u_map + u_src), W) / wrms(obs, W)
        out[name] = dict(R_shape=R_shape, R_norm=R_norm, a=a, share=share, cross=cross / tot,
                         dist_leg=dist_leg, norm_of_leg=share['norm'] / dist_leg, resid2=resid2,
                         lfrac={kk: wrms(lp[kk], W) / max(wrms(parts[kk], W), 1e-300) for kk in lp})
        o = out[name]
        print(f"\n      {name} ({B[CX[0]].shape[1]} bins, {int(dead.sum())} cells masked)")
        print(f"        rms  full map swap {wrms(u_map, W):.5f}   normalisation {wrms(t_norm, W):.5f}"
              f"   shape {wrms(t_shape, W):.5f}   source-alone {wrms(u_src, W):.5f}")
        print(f"        ⇒ R_shape {R_shape:.4f}   R_norm {R_norm:.4f}")
        print(f"        two-term closure on the NEW legs: rms(obs - (map + source))/rms(obs) "
              f"= {resid2:.4f}")
        print(f"        three-term fit  a_norm {a[0]:+.4f}  a_shape {a[1]:+.4f}  a_src {a[2]:+.4f}")
        print(f"        l-structured variance shares: norm {100*o['share']['norm']:+.1f} %  "
              f"shape {100*o['share']['shape']:+.1f} %  source {100*o['share']['src']:+.1f} %  "
              f"cross {100*o['cross']:+.1f} %")
        print(f"        ⇒ the whole distance leg {100*dist_leg:+.1f} %, of which the normalisation "
              f"is {100*o['norm_of_leg']:.1f} %")

    print("\n" + "=" * 100)
    v = [out[n]['R_shape'] for n in BINS]
    lo = all(x <= R_SHAPE_LO for x in v)
    hi = all(x >= R_SHAPE_HI for x in v)
    cross_boundary = (any(x <= R_SHAPE_LO for x in v) and not lo) or \
                     (any(x >= R_SHAPE_HI for x in v) and not hi)
    if cross_boundary:
        print("  ⛔ THE TWO BINNINGS DISAGREE ACROSS A REGISTERED BOUNDARY.")
        print("     A.3 registered that this IS the verdict: neither reading is chosen.")
    elif lo:
        print("  ⇒ R_shape WITHIN 0.20 on both binnings: the distance leg of the located step is the")
        print("    NORMALISATION, and r7735's item 3 CLOSES on that answer.")
    elif hi:
        print("  ⛔ R_shape AT OR ABOVE 0.80 on both: the distance leg is the SHAPE, the present cross")
        print("     term is the wrong object for the multipole-structure claim, and P15 owes a")
        print("     correction -- stated plainly, as registered.")
    else:
        print("  ⇒ R_shape BETWEEN the registered bounds on both binnings: both terms contribute, so")
        print("    r7735's item 3 NARROWS and does not close; the leg is reported as two terms.")
    nl = [out[n]['norm_of_leg'] for n in BINS]
    print(f"\n  A.4: the normalisation's share of the whole distance leg is "
          f"{', '.join(f'{x:.3f}' for x in nl)} against the registered line {S3_LINE}")
    print("    ⇒ " + ("P15's sentence survives as printed." if all(x >= S3_LINE for x in nl)
                      else "the printed 93.6 per cent belongs to the distance leg as a WHOLE and not "
                           "to the normalisation -- a correction to a printed sentence."))
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
