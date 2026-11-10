#!/usr/bin/env python3
"""`r7731+cc66.2` the detectability test on 70's `(l, k)` arrays, read as registered.

⛭ Registration: `r7723_cc66_the_detectability_half/PREDICTION_detectability.md` with amendments 1-5.
⛔ Nothing here is redesigned.  Where the registration's LETTER cannot be run on this object, that is said
and its CONTENT is run instead, with the substitution named.

The convention is taken from 70's own C4 identity and not guessed:
    M(l, k) = P(k) * Dlk(l, k)**2        and      Dl(l) = l(l+1) * sum_k M(l, k)
so `P` already carries the source spectrum and the ladder measure.
"""
import json
import math
import os
import sys

import numpy as np
from scipy.stats import norm

BLOB = '/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/scratchpad/dlk/r7729_dlk_four.npz'
TOL_GRID = 1e-3          # registered §2c
TOL_ID = 1e-12           # registered Gate 0 / Gate 1 tolerance
CORR_MAX, VIF_MAX = 0.70, 2.0      # registered §4, untouched in all five amendments
D1_CORR, D1_VIF = -0.9200, 6.51    # the collapsed route's figures
BINS = {'PRIMARY (12 nodes, 5.2 osc)': 12, 'SECONDARY (23 nodes, 10.0 osc)': 23}
FAILS = []


def gate(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def wcorr(x, y, w):
    """registered amendment 2: contribution-weighted correlation; cond and VIF follow from it"""
    w = w / w.sum()
    a, b = x - (w * x).sum(), y - (w * y).sum()
    r = float((w * a * b).sum() / np.sqrt((w * a * a).sum() * (w * b * b).sum()))
    return r, float(np.sqrt((1 + abs(r)) / (1 - abs(r)))), float(1.0 / (1.0 - r * r))


def binned(M, w):
    """sum M within bins of w nodes -- the registered amendment-5 reduction, an integral per bin"""
    n = M.shape[1] // w
    return M[:, :n * w].reshape(M.shape[0], n, w).sum(axis=2)


def main():
    z = np.load(BLOB, allow_pickle=True)
    ls, k = z['ls'], z['k']
    C = ('S_lcdm__K_lcdm', 'S_lcdm__K_cr', 'S_cr__K_lcdm', 'S_cr__K_cr')
    M = {c: z[f'P__{c}'][None, :] * z[f'Dlk__{c}'] ** 2 for c in C}
    meta = json.loads(str(z['meta']))
    print(f"\n  ⛭ `r7731+cc66.2` the detectability test on 70's arrays\n"
          f"     l {ls[0]}-{ls[-1]} ({len(ls)}), k {len(k)} ladder nodes, "
          f"{meta['closure']['grid']['nodes_per_bessel_period']:.4f} nodes per Bessel period\n")

    # ---- Gate 0: the convention, recomputed rather than cited -------------
    worst = max(float(np.abs(ls * (ls + 1) * M[c].sum(axis=1) / z[f'Dl__{c}'] - 1).max()) for c in C)
    gate('0', worst <= TOL_ID,
         "the convention: l(l+1) sum_k P Dlk^2 == Dl, RECOMPUTED here and not taken from the record",
         f"worst relative departure over all four combinations: {worst:.3e}")

    # ---- §2c: the registered control, its CONTENT not its letter ---------
    # ⛔ The registration named "the banked spectra" as the comparison object.  THOSE ARE THE
    #    PSEUDO-SPECTRA, and these arrays are the FULL computation -- a different object, so the
    #    letter of §2c cannot be run.  Its CONTENT is: does the move to the common grid change the
    #    collapse?  On this object that is ladder-against-native, which is what 70's C3 asks.
    #    ⇒ Recomputed here from the bytes, so it is this seat's arithmetic and not 70's number.
    r3 = float(np.abs(z['Dl__S_lcdm__K_lcdm'] / z['Dl__native_lcdm'] - 1).max())
    gate('§2c', r3 <= TOL_GRID,
         "the grid move does not change the collapse -- ladder against native, MY arithmetic",
         f"max relative departure {r3:.4e} against the registered {TOL_GRID:.0e}  "
         f"⌗ 70's C3 records {meta['closure']['C3']['max_rel']:.4e} on the same comparison; "
         f"agreement is a cross-check, not a substitution")

    # ---- Gate 1: the premise -- is the source swap a column rescaling? ---
    same_src = (float(np.abs(z['P__S_cr__K_cr'] / z['P__S_cr__K_lcdm'] - 1).max()),
                float(np.abs(z['P__S_lcdm__K_lcdm'] / z['P__S_lcdm__K_cr'] - 1).max()))
    gate('1', max(same_src) <= TOL_ID,
         "the premise: P depends on the SOURCE arm alone, so the source swap is a column rescaling",
         f"within-source departures {same_src[0]:.3e} (cr) and {same_src[1]:.3e} (lcdm)")

    # ---- Gate 1b: IS THE FIT A TAUTOLOGY HERE TOO? ------------------------
    # ⛔ On the pseudo-spectra it was, to 1.4e-14, because that integrand factorises.  THIS is the
    #    object the question is about, so this is where the fit either has content or does not.
    live = (M['S_lcdm__K_lcdm'] > 0) & (M['S_cr__K_cr'] > 0) & \
           (M['S_lcdm__K_cr'] > 0) & (M['S_cr__K_lcdm'] > 0)
    with np.errstate(divide='ignore', invalid='ignore'):
        lg = {c: np.log(M[c]) for c in C}
    t_ker = lg['S_lcdm__K_cr'] - lg['S_lcdm__K_lcdm']
    t_src = lg['S_cr__K_lcdm'] - lg['S_lcdm__K_lcdm']
    full = lg['S_cr__K_cr'] - lg['S_lcdm__K_lcdm']
    res = (full - (t_ker + t_src))[live]
    scale = float(np.sqrt((full[live] ** 2).mean()))
    rms = float(np.sqrt((res ** 2).mean()))
    gate('1b', rms / scale > 1e-6,
         "the two-amplitude fit is NOT an algebraic identity on this object",
         f"rms residual of full - (t_ker + t_src) = {rms:.4e} against a signal rms of {scale:.4f} "
         f"⇒ ratio {rms / scale:.3e}.  ⌗ on the pseudo-spectra this ratio was 2.6e-15, a tautology; "
         f"here it is {'NOT' if rms / scale > 1e-6 else 'STILL'} one")
    print(f"\n    ⇒ live cells (all four combinations positive): {int(live.sum())} of {live.size}\n")

    # ---- Gate A5a, RESTATED by amendment 6 in the registration's own terms ----
    # ⛔ The first form demanded "strictly positive", which conflates a NEGATIVE bin (fatal, no
    #    masking fixes it) with an EXACTLY ZERO one (the underflow case amendment 3 masks).  §A5.4's
    #    closing condition is "the same way it failed on the pseudo-spectra" -- the lowest bands dead
    #    at EVERY l.  So the predicate is split, and both halves are measured.
    ok_all = True
    for name, w in BINS.items():
        negs = sum(int((binned(M[c], w) < 0).sum()) for c in C)
        allz = sum(int((binned(M[c], w) <= 0).all(axis=0).sum()) for c in C)
        zer = sum(int((binned(M[c], w) <= 0).sum()) for c in C)
        ok_all &= (negs == 0 and allz == 0)
        gate(f'A5a-i/{name.split()[0]}', negs == 0,
             f"no bin sum is NEGATIVE anywhere [{name}]  -- a negative contribution is fatal",
             f"negative bin cells: {negs}")
        gate(f'A5a-ii/{name.split()[0]}', allz == 0,
             f"no bin is dead at EVERY l [{name}]  -- THAT is the pseudo-spectra failure",
             f"bins dead at every l: {allz};  bin-cells dead at some l: {zer} "
             f"({100.0 * zer / (4 * binned(M[C[0]], w).size):.1f}%), masked at weight 0 per amendment 3")
    if not ok_all:
        raise SystemExit("  ⛔ the binned route is closed the way amendment 2 closed banding; "
                         "reporting that rather than retuning")

    # ---- Gates 2, 3, 4 on each registered binning ------------------------
    read = {}
    for name, w in BINS.items():
        B = {c: binned(M[c], w) for c in C}
        dead = np.zeros(B[C[0]].shape, bool)
        for c in C:
            dead |= B[c] <= 0
        with np.errstate(divide='ignore'):
            lb = {c: np.where(dead, 0.0, np.log(np.where(B[c] > 0, B[c], 1.0))) for c in C}
        tk = lb['S_lcdm__K_cr'] - lb['S_lcdm__K_lcdm']
        ts = lb['S_cr__K_lcdm'] - lb['S_lcdm__K_lcdm']
        W = B['S_lcdm__K_lcdm'] / B['S_lcdm__K_lcdm'].sum(axis=1, keepdims=True)
        W = np.where(dead, 0.0, W)          # amendment 6: dead bins weigh exactly 0
        col = (W * tk).sum(axis=0) / W.sum(axis=0)
        R = tk - col[None, :]
        nf = np.sqrt((W * tk * tk).sum())
        f_mimic = float(np.sqrt((W * np.tile(col, (tk.shape[0], 1)) ** 2).sum()) / nf)
        f_sep = float(np.sqrt((W * R * R).sum()) / nf)
        r, c_, v = wcorr(tk.ravel(), ts.ravel(), W.ravel())
        read[name] = (r, c_, v, f_mimic, f_sep, B[C[0]].shape)
        print(f"    ⛭ {name}: {B[C[0]].shape[1]} bins   f_mimic {f_mimic:.4f}  f_sep {f_sep:.4f}")

    print(f"\n    ⛭ THE VERDICT -- conditioning, against the collapsed route's "
          f"{D1_CORR} / {D1_VIF}x:")
    passes = []
    for name, (r, c_, v, _, _, sh) in read.items():
        ok = abs(r) <= CORR_MAX and v <= VIF_MAX
        passes.append(ok)
        print(f"             {name:30s} corr {r:+.4f}  cond {c_:.2f}  VIF {v:.2f}x  "
              f"=> {'MEETS' if ok else 'MISSES'}")
    gate('agree', all(passes) or not any(passes),
         "the two binnings agree on the verdict (registered: a disagreement IS the verdict)",
         f"{'both ' + ('meet' if all(passes) else 'miss') if (all(passes) or not any(passes)) else 'THEY DISAGREE'}")
    gate('3', all(passes), f"THE REGISTERED THRESHOLD -- |corr| <= {CORR_MAX} AND VIF <= {VIF_MAX}",
         'the (l,k) plane BREAKS the degeneracy on the real computation' if all(passes)
         else 'the (l,k) plane does NOT break it on the real computation')

    # ---- Gate 3b: the same-object baseline, collapsed --------------------
    ck = np.log(z['Dl__S_lcdm__K_cr']) - np.log(z['Dl__S_lcdm__K_lcdm'])
    cs = np.log(z['Dl__S_cr__K_lcdm']) - np.log(z['Dl__S_lcdm__K_lcdm'])
    r1, c1, v1 = wcorr(ck, cs, np.ones_like(ck))
    gate('3b', abs(r1) >= CORR_MAX and v1 >= VIF_MAX,
         "SAME-OBJECT BASELINE -- the same statistic on the COLLAPSED arrays still sees a degeneracy",
         f"collapsed: corr {r1:+.4f}  cond {c1:.2f}  VIF {v1:.2f}x over {len(ls)} l")

    # ---- the ceiling, for the record ------------------------------------
    for nb in sorted({read[n][5][1] for n in read}):
        p = 1.0 / math.factorial(min(nb, 170))
        print(f"\n    ⌗ a {nb}-bin family's resampling floor is p = {p:.3g} ⇒ "
              f"{norm.isf(p / 2.0):.2f} sd-equivalent" if nb <= 170 else '')
    nf_ = len(FAILS)
    print(f"\n  {'OK' if not nf_ else '⛔'}  {8 + 2 * len(BINS) - 2 - nf_} gate(s) pass, {nf_} failure(s)"
          f"{'' if not nf_ else '; FAILED: ' + ', '.join(FAILS)}\n")
    return 1 if nf_ else 0


if __name__ == '__main__':
    sys.exit(main())
