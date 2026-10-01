"""r7041 ⓒ -- fold the injection convergence sequence and report it as a sequence.

** NOTHING HERE IS A SPECTRUM OF THE MODEL. **  Every run is the projection's transfer of a KNOWN
analytic oscillation (`SRCINJ`), so no number here may be compared with a banked spectrum or with the
sky.  What is measured is whether the arm-to-control **BAND-RMS RATIO** MOVES when a numerical setting is
refined -- and the statistic is `r6911+cc66.40`'s and `r6919+cc66.42`'s, unchanged.

⛔ ** AND IT IS NAMED THE BAND-RMS RATIO HERE, NOT "THE RETENTION", ON r7057. **  *Node 70's phase
systematic found that about a THIRD of the reported `+0.0139` per acoustic period is a phase drift between
the two arms' SOURCE combs -- periods 1.0170 and 1.0160, drifting 0.013 to 0.042 rad across the range --
which a band root-mean-square over seven tenths of a period reads as retention.  **The rise survives; two
thirds of its size does.***
  ⇒ *Nothing in this sweep changes and nothing is re-run: the convergence question is whether the number
  stops moving with the NUMERICAL SETTINGS, and that is unaffected by what fraction of the number is drift.
  ** What would be affected is the sentence written about it afterwards -- so this reader names its quantity
  for what it is and leaves no room to read "converged band-RMS ratio" as "converged retention". **
  ⌗ *Same correction as the gate label and the inert axes: make the name read what the thing is.*
"""
import os, sys
import numpy as np

import fold

D = '/tmp/n66/r7041/inj'
LO, HI, NG = 0.85, 5.75, 1200
ED = np.arange(0.85, 5.76, 0.7)
SETS = ['base', 'kfac26', 'kfac32', 'kfac40', 'nk15', 'nk20',
        'nlos1120', 'nlos2240', 'nlosw9', 'nlosw12', 'nlosf90', 'lstep4']
INJ = ['fixed', 'sweepown']
# the sequences, each an axis refined in one direction -- `base` is every sequence's first point
SEQ = {'k_max via KFAC (upward only; the guard refuses downward)':
       ['base', 'kfac26', 'kfac32', 'kfac40'],
       "the mode count NK -- the CONTROL carries this axis alone; on the arm NK is inert by "
       "construction and `base` stands in for it as an identity (see INERT)": ['base', 'nk15', 'nk20'],
       'the eta resolution NLOS': ['base', 'nlos1120', 'nlos2240'],
       'the eta half-width NLOSW': ['base', 'nlosw9', 'nlosw12'],
       'the eta split NLOSF': ['base', 'nlosf90'],
       'the reported ell grid LSTEP': ['base', 'lstep4']}
FLOOR = 0.006      # r6911's, on a KNOWN injected contrast


def env_a(x, y, win=1.0):
    e = np.empty_like(y, dtype=float)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    y = np.asarray(y, float)
    e = env_a(x, y, win)
    return (y - e) / e


GRID = '/tmp/n66/r7041/grid'
# ⛔⛭ ** THE ARM'S `NK` IS INERT BY CONSTRUCTION, AND THIS IS THE ONE SUBSTITUTION IN THE REPORT. **
# *On the arm the k ladder is `sqrt(L(L+2))*stretch` out to `KMAXL` and `NK` is only a decimation cap that
# is never reached, so `nk15` and `nk20` are the SAME COMPUTATION as `base`: `GRIDSAVE` writes 1452 modes in
# all three with `k` and `eta` byte-identical, and the banked slices agree at `max|Dl| = 0.000e+00`.  On the
# control `NK` takes 2547 modes to 3822 to 5094 and the spectra differ outright -- so the NK sequence is a
# real axis, and what moves along it is the CONTROL alone.*
#   ⇒ ** So the arm's `nk15` / `nk20` runs are not queued and `base` stands in for them -- NOT as an
#   approximation but as an identity.  ⛔ AND THE IDENTITY IS CHECKED HERE RATHER THAN ASSUMED: ** if the
#   grid files do not show `k` and `eta` equal, the substitution REFUSES and the sequence reads as absent.
#   *`r7041+cc66.60`'s gate zero is the pattern: a claim the code depends on is a claim the code tests.*
INERT = {('cr', 'nk15'), ('cr', 'nk20')}


def grid_identical(arm, s, base='base'):
    """the whole of the substitution's warrant, read off the setup and not argued"""
    try:
        a = np.load(f'{GRID}/g_{arm}_{s}.npz'); b = np.load(f'{GRID}/g_{arm}_{base}.npz')
    except Exception:
        return False
    return all(np.array_equal(a[q], b[q]) for q in ('k', 'eta', 'vis', 'x0', 'dk'))


# ⛔⛭ ** THIS READER USED TO OPEN A WHOLE-RUN `.npz` AND SO COULD NOT SEE THE SWEEP IT REPORTS ON. **
# *Five configurations finished UNSLICED and have such a file; the other sixty-one are tiled on `KSLICE`
# and have none, only `_k0.npz`, `_k100.npz`, ... .  At full coverage this reader therefore called 39 of 48
# runs "not on disk yet" and read exactly the two unsliced points of one axis -- a PARTIAL read of a
# COMPLETE sweep, which is the worst of the two failures `fold` was written to end.*
#   ⇒ ** So it loads through `fold.load`, which is the module that already knows both forms and is the
#   authority on what "complete" means.  ⌗ The completeness test is NOT duplicated here: an incomplete
#   tiling returns None from `fold` and reads as absent, exactly as a missing file did.**
def load(inj, arm, s):
    if (arm, s) in INERT:
        if not grid_identical(arm, s):
            return None                     # ⛔ the warrant failed: read nothing rather than base
        s = 'base'
    r = fold.load(D, f'inj_{inj}_{arm}_{s}')
    if r is None:
        return None
    ls, Dl, l_A, _form = r
    return ls / l_A, Dl


def ratio(inj, s, lo=LO, hi=HI):
    """r6919's own arm-to-control band-RMS statistic -- NOT purely retention; see the header on r7057"""
    a = load(inj, 'cr', s); b = load(inj, 'lcdm', s)
    if a is None or b is None:
        return None
    x = np.linspace(lo, hi, NG)
    A = np.interp(x, a[0], osc(*a)); B = np.interp(x, b[0], osc(*b))
    return float(np.sum(A * B) / np.sum(B * B))


def slope(inj, s):
    a = load(inj, 'cr', s); b = load(inj, 'lcdm', s)
    if a is None or b is None:
        return None
    xs = np.array([(p + q) / 2 for p, q in zip(ED[:-1], ED[1:])])
    ys = np.array([ratio(inj, s, p, q) for p, q in zip(ED[:-1], ED[1:])])
    return float(np.polyfit(xs, ys, 1)[0])


print(__doc__)
print("=" * 100)
miss = [(i, a, s) for i in INJ for a in ('lcdm', 'cr') for s in SETS if load(i, a, s) is None]
if miss:
    print(f"  ⚠ {len(miss)} of {2*2*len(SETS)} runs not on disk yet -- this is a PARTIAL read and is")
    print(f"    labelled as one.  missing: {[f'{i}/{a}/{s}' for i, a, s in miss][:8]}")
print()
for inj in INJ:
    print("-" * 100)
    print(f"  INJECTION `{inj}`   (r6919 banked: sweepown 1.0659 slope +0.02260, "
          f"fixed 1.0587 slope +0.01189)")
    print("-" * 100)
    for name, seq in SEQ.items():
        vals = [(s, ratio(inj, s), slope(inj, s)) for s in seq]
        have = [v for v in vals if v[1] is not None]
        if len(have) < 2:
            print(f"    {name}: fewer than two points on disk -- not read")
            continue
        txt = "  ".join(f"{s}={r:.4f}" for s, r, _ in have)
        step = abs(have[-1][1] - have[-2][1]) / abs(have[-2][1])
        mono = all((have[j + 1][1] - have[j][1]) * (have[1][1] - have[0][1]) > 0
                   for j in range(len(have) - 1))
        # ⛔ ** TWO POINTS IS NOT A CONVERGED SEQUENCE AND THE FIRST VERSION OF THIS SAID IT WAS. **
        # *The pre-registration fixed it in advance -- "a sequence that has not turned over is not
        # converged whatever its last step" -- and monotonicity is UNDEFINED on two points, so the
        # `mono` branch could not fire and a two-point axis fell through to "converged at the floor".*
        #   ⌗ A two-point axis with a small step is the cheapest way to look converged without being
        #   it: one refinement that happens to land close says nothing about where the sequence goes.
        verdict = ("⛔ UNCONVERGED -- last step above the floor" if step > FLOOR else
                   "⌗ TWO POINTS ONLY -- inside the floor, but a two-point axis cannot turn over "
                   "and is not reported as converged" if len(have) < 3 else
                   "⚠ step under the floor but the sequence has NOT turned over" if mono
                   else "✔ converged at the floor")
        print(f"    {name}")
        print(f"      {txt}")
        print(f"      last step {step*100:.3f}% against the {FLOOR*100:.1f}% floor   "
              f"toward unity: {'yes' if abs(have[-1][1]-1) < abs(have[0][1]-1) else 'no'}   {verdict}")
        print(f"      slope / unit q: " + ", ".join(f"{s}={sl:+.5f}" for s, _, sl in have))
