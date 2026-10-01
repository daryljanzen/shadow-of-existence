#!/usr/bin/env python3
"""r7091 ⓑ -- THE RESIDUAL'S SHAPE, WHICH IS WHAT THE PLOT SHOWS AND WHAT chi^2 HIDES.

** WHY A SHAPE READER AND NOT ANOTHER chi^2. **  `r7091`'s order is Daryl's reading of the plot: *the
model is inaccurate everywhere except where it accidentally crosses the data, swinging above and
below.*  That is the signature of a fit constrained in a direction the physics does not constrain, and
a chi^2 per bin hides it completely -- a large alternating residual and a small random one can score
the same.

⇒ ** So this reports the SIGN PATTERN, the CROSSINGS and the EXCURSIONS, and chi^2 only beside them. **
  - the per-bin residual (d - A m) in units of the bin's own sigma, A fitted exactly as the likelihood
    fits it, so the amplitude is not a free excuse for a swing;
  - the RUNS of constant sign, each with its ell range, its length in bins and its extremum: a swing is
    a small number of long runs with large extrema, and noise is many short runs with small ones;
  - the CROSSINGS, counted and located, as the plot's own feature;
  - the EXCURSION between consecutive crossings, which is the swing's amplitude.

⛔ ** AND THE VERDICT RULE IS FIXED HERE BEFORE ANY SPECTRUM IS READ, because the order fixes it: **
*"A chi^2 that improves while the swing stays is not the fix, and a swing that flattens is the fix even
if chi^2 moves little."*  ⇒ So the comparison reports BOTH and names which moved: the swing is measured
by the longest run, the mean |extremum| over runs, and the number of crossings -- a flattened swing has
more crossings, shorter runs and smaller extrema.  *Stated in advance so neither number can be chosen
after the fact.*

⌗ Usage:  python3 shape.py BEFORE.npz [AFTER.npz] [--lmax 1040]
"""
import os
import sys

import numpy as np

# ⛔⛭ FIXED AT r7097+cc66.80.  ** THIS LINE WAS AN ABSOLUTE PATH TO ONE MACHINE'S FILESYSTEM, and it
# ** worked for as long as nothing but a hand-run in that container ever read this file. **
# *`cc66.78` made a REGISTERED RECEIPT invoke `shape.py` as a subprocess, so for the first time it ran on
# a CI runner, where the checkout is at `/home/runner/work/...`.  The import failed, the process died
# before printing anything, and the receipt saw "no statistics" with no idea why -- a 0-second red on a
# tree where the physics was fine.*
#   ⇒ *Derived from `__file__` now, as the rest of the tree does.  ⚠ **The pattern is NOT unique to this
#   file** -- roughly forty drivers and launchers under `computations/beyond_the_wall/` carry the same
#   absolute root, including `refit_grid185/fit.py`.  They are latent rather than broken: nothing
#   registered reads them, so CI never runs them.  **Fixed here only, and the pattern is routed rather
#   than swept, because a sweep of forty files is not this revision's subject.***
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(_ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS


# ⛭⛭ ** AND A SECOND READING WITH A TILT MARGINALISED, BECAUSE THE FIRST ONE CANNOT TELL THE TWO
#   ANSWERS APART. **  *A comparison at FIXED parameters is the right isolation of a change to the
#   geometry -- but the geometry moves `D_M` and the visibility's width in eta, so the best-fit
#   parameters move with it, and the parameters were fitted under the OLD geometry.*
#   ⇒ ** A long run of ONE sign across the low-ell half is exactly the shape an amplitude-and-tilt
#   mismatch makes, and the amplitude is already fitted. **  *So the swing at fixed parameters cannot
#   distinguish "the geometry does not fix the shape" from "the geometry needs its own n_s".*
# ⇒ So every spectrum is read TWICE: once with the amplitude alone fitted, as the likelihood fits it,
#   and once with an amplitude AND a power-law tilt in ell fitted together -- `m -> A (ell/500)^t m`,
#   the two directions a refit would move first.  ⌗ *If the swing survives the tilt it is in the
#   SHAPE and the one-clock build has not fixed it; if the tilt absorbs it, the fixed-parameter
#   comparison was unfair to the after and a refit is owed before it is scored.*
#   ⚠ *This is NOT a refit and is not offered as one: two linear directions are not four, n_s is not
#   a pure tilt in ell, and nothing here re-runs the instrument.  It is the cheapest honest
#   discriminator between a shape defect and a parameter deficit, and it is labelled as that.*
def _fit_with_tilt(mb, keep, F):
    """A and t minimising the covariance-weighted residual for m -> A (ell/500)^t m"""
    import scipy.optimize
    d = CS.X_DATA[keep]
    lc = 0.5 * (CS.BIN_LO[keep] + CS.BIN_HI[keep]).astype(float)
    m0 = mb[keep]

    def chi2_t(t):
        m = m0 * (lc / 500.0) ** t
        A = float((m @ F @ d) / (m @ F @ m))
        r = d - A * m
        return float(r @ F @ r)

    t = float(scipy.optimize.minimize_scalar(chi2_t, bounds=(-2.0, 2.0), method='bounded').x)
    m = m0 * (lc / 500.0) ** t
    A = float((m @ F @ d) / (m @ F @ m))
    return A, t, (d - A * m), chi2_t(t)


def read(path, lmax=None, tilt=False):
    """the per-bin residual in sigma, with the amplitude fitted as the likelihood fits it"""
    z = np.load(path)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    mb = CS.bin_spectrum(ls, Dl)
    keep = np.isfinite(mb)
    if lmax is not None:
        keep = keep & (CS.BIN_HI <= float(lmax))
    chi2, nb, A, lo, hi = CS.chi2_of(ls, Dl, lmax=lmax)
    tfit = None
    if tilt:
        import scipy.linalg
        cov = CS.COV_TT[np.ix_(keep, keep)]
        F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
        F = 0.5 * (F + F.T)
        A, tfit, _r, chi2 = _fit_with_tilt(mb, keep, F)
    # ⌗ the residual is reported in units of the bin's OWN sigma -- the covariance diagonal -- so a
    #   run of one sign is a run in a quantity the eye and the likelihood both read the same way.
    sig = np.sqrt(np.diag(CS.COV_TT))[keep]
    lcm = 0.5 * (CS.BIN_LO[keep] + CS.BIN_HI[keep]).astype(float)
    m = mb[keep] * ((lcm / 500.0) ** tfit if tfit is not None else 1.0)
    r = (CS.X_DATA[keep] - A * m) / sig
    return dict(lc=CS.BIN_LO[keep].astype(float), lhi=CS.BIN_HI[keep].astype(float),
                r=r, chi2=chi2, nbin=nb, A=A, lo=lo, hi=hi, path=path, tilt=tfit)


def runs_of_sign(lc, lhi, r):
    """the maximal runs of one sign, each (ell_lo, ell_hi, nbins, signed extremum)"""
    out, i = [], 0
    s = np.sign(r)
    while i < len(r):
        j = i
        while j + 1 < len(r) and s[j + 1] == s[i]:
            j += 1
        seg = r[i:j + 1]
        k = int(np.argmax(np.abs(seg)))
        out.append((float(lc[i]), float(lhi[j]), j - i + 1, float(seg[k])))
        i = j + 1
    return out


def report(d, label):
    rr = runs_of_sign(d['lc'], d['lhi'], d['r'])
    cross = [(rr[i][1] + rr[i + 1][0]) / 2 for i in range(len(rr) - 1)]
    ex = [abs(x[3]) for x in rr]
    print(f"  {label}:  {os.path.basename(d['path'])}")
    print(f"    chi2 = {d['chi2']:.1f} over {d['nbin']} bins (ell {d['lo']}-{d['hi']}), "
          f"chi2/bin = {d['chi2']/d['nbin']:.2f}, amplitude {d['A']:.4f}"
          + (f", tilt {d['tilt']:+.4f}" if d.get('tilt') is not None else ""))
    print(f"    SIGN RUNS: {len(rr)}   CROSSINGS: {len(cross)}   "
          f"longest run {max(x[2] for x in rr)} bins   "
          f"mean |extremum| {np.mean(ex):.2f} sigma   max {max(ex):.2f} sigma")
    print(f"    rms residual {np.sqrt(np.mean(d['r']**2)):.2f} sigma, "
          f"mean {np.mean(d['r']):+.2f}")
    print("    run    ell range        bins   extremum")
    for a, b, n, e in rr:
        bar = ('+' if e > 0 else '-') * min(n, 40)
        print(f"      {'+' if e > 0 else '-'}  {a:6.0f}-{b:<6.0f} {n:5d}   {e:+6.2f} s  {bar}")
    if cross:
        print("    crossings at ell: " + " ".join(f"{c:.0f}" for c in cross))
    return dict(nruns=len(rr), ncross=len(cross), longest=max(x[2] for x in rr),
                mean_ex=float(np.mean(ex)), max_ex=float(max(ex)),
                rms=float(np.sqrt(np.mean(d['r'] ** 2))), chi2=d['chi2'], nbin=d['nbin'])


def main(argv):
    lmax = None
    if '--lmax' in argv:
        i = argv.index('--lmax')
        lmax = float(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    paths = argv
    print(__doc__.split('⌗ Usage')[0])
    print("=" * 100)
    if lmax:
        print(f"  scored to ell <= {lmax:.0f}  (bins above ~0.8*LMAXL score the k truncation, "
              f"not the physics -- c54.178)")
    tilt = '--tilt' in paths
    paths = [p for p in paths if p != '--tilt']
    if tilt:
        print("  with an amplitude AND a power-law tilt in ell fitted -- the two directions a refit")
        print("  would move first.  NOT a refit; the cheapest discriminator between shape and parameters.")
    outs = []
    for p, lab in zip(paths, ['BEFORE', 'AFTER', 'THIRD', 'FOURTH']):
        print("-" * 100)
        outs.append(report(read(p, lmax, tilt=tilt), lab))
    if len(outs) >= 2:
        b, a = outs[0], outs[1]
        print("=" * 100)
        print("  WHAT MOVED -- the order's own rule: a chi2 that improves while the swing stays is")
        print("  not the fix; a swing that flattens is the fix even if chi2 moves little.")
        print(f"    chi2      {b['chi2']:9.1f} -> {a['chi2']:9.1f}   "
              f"({100*(a['chi2']-b['chi2'])/b['chi2']:+.1f}%)")
        for k, name in [('ncross', 'crossings'), ('longest', 'longest run (bins)'),
                        ('mean_ex', 'mean |extremum| (sigma)'), ('max_ex', 'max |extremum| (sigma)'),
                        ('rms', 'rms residual (sigma)')]:
            print(f"    {name:26s} {b[k]:9.2f} -> {a[k]:9.2f}")
        flat = (a['ncross'] > b['ncross'] and a['longest'] < b['longest']
                and a['mean_ex'] < b['mean_ex'])
        print(f"    ⇒ the swing {'FLATTENED' if flat else 'did NOT flatten'} by the rule stated above")


if __name__ == '__main__':
    main(sys.argv[1:])
