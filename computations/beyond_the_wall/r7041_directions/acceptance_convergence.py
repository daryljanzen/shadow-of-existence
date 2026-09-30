"""** DOES THE ACCEPTANCE STOP MOVING?  r7049's convergence probe, on the operation the row is about. **

`r7049`, offering and not directing: *"The convergence question has usually been asked of the height ratios,
because those were what moved.  A_l is a sharper probe of the same thing and it is now free: it is built from
W_l = G_l^2 dk/k over the k-grid, so truncating k_max truncates the window the law integrates over -- and A_l
carries NO FITTED AMPLITUDE to absorb the truncation, where a height ratio does."*

⇒ *** "THE ACCEPTANCE STOPS MOVING" IS A CONVERGENCE STATEMENT ABOUT THE OPERATION THIS ROW IS ACTUALLY
    ABOUT, where "the heights stop moving" is one about their quotient. ***

⛭ ** AND IT COSTS NO RE-RUN. **  `A_l` needs only the background: the visibility, the kernel's argument, the
k axis and its measure, and `r_s*`.  `GRIDSAVE` writes those in 1.45 s per configuration without computing a
spectrum at all -- so this reads the acceptance at every setting WITHOUT waiting for the sweep.
  ⌗ *`r7049`: "if it costs a re-run, it is not worth one."  It did not.*

⛔ ** WHAT THIS IS NOT. **  It is not the sweep and does not replace it: the sweep asks what the RETENTION and
the heights do, measured on spectra.  This asks what the kernel's k-acceptance does.  *A converged acceptance
with an unconverged retention would itself be a finding, and the two are reported separately.*
"""
import glob
import os
import sys

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
D = '/tmp/n66/r7041/grid'
LO, HI = 0.85, 5.75
NL = 8
FLOOR = 0.006          # r6911's, on a KNOWN injected contrast
# each axis refined in ONE direction; `base` is every axis's first point
SEQ = {'k_max via KFAC (upward only; the guard refuses downward)':
       ['base', 'kfac26', 'kfac32', 'kfac40'],
       'the mode count NK': ['base', 'nk15', 'nk20'],
       'the eta resolution NLOS': ['base', 'nlos1120', 'nlos2240'],
       'the eta half-width NLOSW': ['base', 'nlosw9', 'nlosw12'],
       'the eta split NLOSF': ['base', 'nlosf90'],
       'the reported ell grid LSTEP': ['base', 'lstep4']}


def acceptance(f, ls):
    """A_l and the acceptance width, from the background alone"""
    d = np.load(f)
    k, ee, x0, v = d['k'], d['eta'], d['x0'], d['vis']
    RS, dk = float(d['r_s']), d['dk']
    A = np.full(len(ls), np.nan)
    wd = np.full(len(ls), np.nan)
    for i, l in enumerate(ls):
        J = spherical_jn(int(l), k[None, :] * x0[:, None])
        G = np.trapezoid(v[:, None] * J, ee, axis=0)
        W = G ** 2 * dk / k
        s = float(W.sum())
        if s > 0:
            A[i] = abs(np.sum(W * np.exp(2j * k * RS))) / s
            kb = float(np.sum(W * k) / s)
            wd[i] = 2 * np.sqrt(max(float(np.sum(W * (k - kb) ** 2) / s), 0.0))
    return A, wd, float(d['l_A']), RS, int(d['n_modes']), int(d['nlos'])


CACHE = '/tmp/n66/r7041/acc_cache'


def cached(arm, tag, ls):
    """A_l per configuration, CACHED -- because this probe outlives no restart otherwise.

    ** The first version computed all 24 configurations in one process and was killed twice by container
    restarts, having written nothing. **  *That is the same defect the unsliced launcher had: a unit of work
    longer than the window between restarts completes never.*  ⇒ One small file per configuration, skipped
    when present, so the probe resumes exactly where it stopped.
    """
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, f'a_{arm}_{tag}.npz')
    if os.path.exists(f):
        d = np.load(f)
        return float(d['Amean']), float(d['span']), int(d['nk']), int(d['nlos'])
    g = os.path.join(D, f'g_{arm}_{tag}.npz')
    if not os.path.exists(g):
        return None
    A, wd, _, RS, nk, nlos = acceptance(g, ls)
    Am, sp = float(np.nanmean(A)), float(np.nanmean(2 * RS * wd))
    np.savez(f, Amean=Am, span=sp, nk=nk, nlos=nlos, A=A, wd=wd, ls=np.asarray(ls))
    return Am, sp, nk, nlos


def main():
    if not glob.glob(os.path.join(D, 'g_*.npz')):
        print(f"  ⛔ no grids in {D} -- run `r7041_directions/launch_grid.sh` first (about 72 s total).")
        return 1
    print(__doc__)
    print("=" * 104)
    out = {}
    for arm in ('lcdm', 'cr'):
        b = os.path.join(D, f'g_{arm}_base.npz')
        if not os.path.exists(b):
            print(f"  ⛔ {arm}: the base grid is missing, so no sequence has a first point.")
            return 1
        lA = float(np.load(b)['l_A'])
        # ** the SAME multipoles at every setting **, so a difference is the setting's and not the grid's
        ls = np.unique(np.round(np.linspace(LO, HI, NL) * lA).astype(int))
        # ⌗ plain ints, not numpy scalars: `list(ls)` prints `[np.int64(256), ...]` and buries the numbers
        print(f"  {arm}: l_A = {lA:.2f}; reading A_l at l = {[int(x) for x in ls]}")
        for tag in sorted({t for v in SEQ.values() for t in v}):
            r = cached(arm, tag, ls)
            if r is not None:
                out[(arm, tag)] = r
    print()
    for arm in ('lcdm', 'cr'):
        print("-" * 104)
        print(f"  ARM `{arm}` -- mean A_l over the reported range, and the acoustic phase the acceptance spans")
        print("-" * 104)
        for name, seq in SEQ.items():
            have = [(t,) + out[(arm, t)] for t in seq if (arm, t) in out]
            if len(have) < 2:
                print(f"    {name}: fewer than two points -- not read")
                continue
            txt = "  ".join(f"{t}={a:.5f}" for t, a, _, _, _ in have)
            step = abs(have[-1][1] - have[-2][1]) / abs(have[-2][1])
            mono = all((have[j + 1][1] - have[j][1]) * (have[1][1] - have[0][1]) > 0
                       for j in range(len(have) - 1))
            verdict = ("⛔ MOVING -- last step above the floor" if step > FLOOR else
                       "⌗ two points only -- inside the floor, but a two-point axis cannot turn over"
                       if len(have) < 3 else
                       "⚠ inside the floor but the sequence has NOT turned over" if mono else
                       "✔ the acceptance has stopped moving, at the floor")
            print(f"    {name}")
            print(f"      {txt}")
            print(f"      last step {step * 100:.4f}% against the {FLOOR * 100:.1f}% floor   {verdict}")
            print(f"      modes: {', '.join(str(n) for _, _, _, n, _ in have)}   "
                  f"eta points: {', '.join(str(n) for _, _, _, _, n in have)}")
        print()
    # the arm-to-control ratio of the acceptance width, which is what the law's prediction rides on
    print("-" * 104)
    print("  AND THE ARM-TO-CONTROL ACCEPTANCE RATIO AT EACH SETTING -- the quantity the law's prediction rides")
    print("-" * 104)
    for tag in sorted({t for v in SEQ.values() for t in v}):
        if ('lcdm', tag) in out and ('cr', tag) in out:
            sc = out[('lcdm', tag)][1]
            sa = out[('cr', tag)][1]
            print(f"    {tag:10s} control {sc:.4f}  arm {sa:.4f}  arm narrower by {(1 - sa / sc) * 100:5.2f}%"
                  f"   (r6919's independent dr_s/dchi reading: 12.8%)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
