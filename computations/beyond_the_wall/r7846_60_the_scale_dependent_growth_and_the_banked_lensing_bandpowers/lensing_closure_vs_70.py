"""** THE CLOSURE THIS SEAT SHOULD HAVE REGISTERED AND DID NOT: IS THE LENSING HALF MY BINNING? **

NOT a registered arm.  `PREDICTION.md`'s eleven arms do not contain it, and this file says so rather
than pretending otherwise.  It is run and reported because `r7848` is about to report that adding
the lensing bandpowers made the control WORSE, and an instrument whose limit has moved 277.7 ->
99.67 -> 111.38 meV across three revisions has never once been checked against another seat's
score of the same data.  ** Reporting a failure whose cause might be my own binning would be worse
than spending twenty minutes ruling it out. **

Node `70` scored these same nine bandpowers at `r7471`, in `like.py`:

    PPm = pp[:, 0] * (L * (L + 1)) ** 2 / (2 * np.pi)
    bp = np.array([np.sum(w * PPm[Ls]) for Ls, w in LENS_W])
    r = LENS_DATA - bp ;  c2 += float(r @ LENS_COVINV @ r)

`pp` there is CAMB's output at EVERY integer multipole, so `PPm[Ls]` is an exact lookup.  This
seat's `bandpowers_from` splines from the 36 log-spaced multipoles the Limber integral is actually
solved on, because each one costs about a second.  ** That interpolation is the ONLY place the two
paths differ, and it has never been measured. **

So this file measures three things, in increasing severity:

  ① the data, the covariance and the nine windows this seat loads are BITWISE what `70`'s own
     loader expressions produce -- which rules out a wrong column, a wrong file or a transposed
     covariance;
  ② `C_L^phiphi` solved at ALL 393 integer multipoles the windows cover, binned `70`'s way with no
     interpolation at all, against the same spectrum binned this seat's way from its 36-point grid;
  ③ the chi^2 each path gives against the banked data.

If ② disagrees at the per-cent level then the lensing half of `r7848` is an interpolation artefact
and the report must say so.  If it agrees, the failure is not the binning, and that is worth
knowing with a number rather than by assertion.

Run: python3 lensing_closure_vs_70.py            (writes lensing_closure_vs_70.json)
"""
import io
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)
import lensing_like as LL                                                  # noqa: E402
import phiphi as PP                                                        # noqa: E402

LENS70 = os.path.join(_BTW, 'r7471_70_PO24_tilt_off_the_tail', 'lensing')
LIKE70 = os.path.join(_BTW, 'r7471_70_PO24_tilt_off_the_tail', 'like.py')


def seventy_loader():
    """`70`'s own loader expressions, copied from `like.py` and run on `70`'s own files"""
    _lb = np.loadtxt(os.path.join(LENS70, 'x_bandpowers.dat'))
    data = _lb[:, 4]
    covinv = np.linalg.inv(np.loadtxt(os.path.join(LENS70, 'x_cov.dat')))
    w70 = []
    for i in range(1, len(data) + 1):
        w = np.loadtxt(os.path.join(LENS70, 'win', f'window{i}.dat'))
        w70.append((w[:, 0].astype(int), w[:, 1]))
    return data, covinv, w70


def bin_seventy(ppm, w70):
    """`70`'s binning verbatim: an exact lookup at every integer multipole, no interpolation"""
    return np.array([float(np.sum(w * ppm[Ls])) for Ls, w in w70])


def main():
    out = {}
    print('\n  the closure this seat should have registered -- is the lensing half my binning?\n')

    # ① the inputs are the same objects
    d70, ci70, w70 = seventy_loader()
    src70 = io.open(LIKE70, encoding='utf-8').read()
    same_data = bool(np.array_equal(d70, LL.DATA))
    # ** the Fisher is ~1e16 because the bandpowers are ~1e-7, so an ABSOLUTE difference says
    # nothing here. **  The first pass printed 1.000e+00 and it looked like a disagreement; it is
    # one part in 1e16, which is the symmetrisation and the inversion's own rounding.
    _den = float(np.max(np.abs(ci70)))
    same_cov = float(np.max(np.abs(ci70 - LL.FISHER)))
    same_cov_rel = same_cov / _den
    same_win = all(np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1])
                   for a, b in zip(w70, LL.WINDOWS))
    conv70 = '(L * (L + 1)) ** 2 / (2 * np.pi)' in src70
    print('  ① inputs: data bitwise identical %s; windows bitwise identical %s; '
          'Fisher agrees to %.3e RELATIVE\n     (absolute %.3e on entries of order %.3e -- an '
          'absolute difference means nothing at this scale)'
          % (same_data, same_win, same_cov_rel, same_cov, _den))
    print('     and 70\'s own convention string is present in its source: %s' % conv70)
    out['inputs'] = dict(data_bitwise_identical=same_data, windows_bitwise_identical=same_win,
                         fisher_max_abs_difference=same_cov,
                         fisher_max_rel_difference=same_cov_rel,
                         fisher_scale=_den,
                         seventy_convention_in_source=conv70)
    assert same_data and same_win and conv70, 'the two seats are not reading the same data'
    assert same_cov_rel < 1e-10, ('the two seats\' Fisher matrices differ by %.3e relative'
                                  % same_cov_rel)

    # ② the same spectrum binned both ways
    Lall = np.unique(np.concatenate([L for L, _ in w70]))
    Lcoarse = np.unique(np.round(np.logspace(np.log10(max(2, Lall.min())),
                                             np.log10(Lall.max()), 36)).astype(int))
    print('\n  ② solving C_L^phiphi at ALL %d integer multipoles %d..%d (70\'s path), and at the '
          '%d this seat\n     actually solves on (its own path)'
          % (len(Lall), Lall.min(), Lall.max(), len(Lcoarse)), flush=True)
    cache = os.path.join(_HERE, 'lensing_closure_vs_70_spectrum.npz')
    if os.path.exists(cache):
        _z = np.load(cache)
        assert np.array_equal(_z['Lall'], Lall), 'the cached spectrum is on another multipole set'
        cl_all = np.asarray(_z['cl_all'], float)
        print('     %d multipoles read from the cached solve' % len(Lall), flush=True)
    else:
        t0 = time.time()
        cl_all = PP.clpp(Lall, 0.0, growth=None)
        print('     %d multipoles in %.1f s' % (len(Lall), time.time() - t0), flush=True)
        np.savez_compressed(cache, Lall=Lall, cl_all=cl_all)

    # 70's path: an array indexed by multipole, exact lookup
    ppm = np.zeros(int(Lall.max()) + 1)
    ppm[Lall] = cl_all * (Lall.astype(float) * (Lall.astype(float) + 1.0)) ** 2 / (2.0 * np.pi)
    b70 = bin_seventy(ppm, w70)

    # this seat's path: the SAME spectrum, restricted to its own coarse grid, then splined
    cl_coarse = cl_all[np.searchsorted(Lall, Lcoarse)]
    b60 = LL.bandpowers_from(Lcoarse, cl_coarse)

    rel = np.abs(b60 / b70 - 1.0)
    err = np.sqrt(np.diag(np.linalg.inv(LL.FISHER)))
    in_sigma = np.abs(b60 - b70) / err
    print('\n     bin   L_av      70 exact        60 splined      rel. diff    in bin sigma')
    for i in range(len(b70)):
        print('      %d   %6.1f   %.6e   %.6e   %9.3e   %9.3e'
              % (i + 1, LL.L_AV[i], b70[i], b60[i], rel[i], in_sigma[i]))
    print('\n     worst relative difference %.3e, worst in units of the bin error %.3e'
          % (rel.max(), in_sigma.max()))
    out['binning'] = dict(n_exact=int(len(Lall)), n_coarse=int(len(Lcoarse)),
                          seventy=[float(v) for v in b70], sixty=[float(v) for v in b60],
                          rel_diff=[float(v) for v in rel],
                          in_bin_sigma=[float(v) for v in in_sigma],
                          worst_rel=float(rel.max()), worst_in_sigma=float(in_sigma.max()))

    # ③ the chi^2 each path gives, at the data's own best normalisation so the comparison is of
    #   the SHAPE each binning produces and not of an amplitude
    def best_chi2(b):
        a = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
        r = LL.DATA - a * b
        return float(r @ LL.FISHER @ r), a

    c70, a70 = best_chi2(b70)
    c60, a60 = best_chi2(b60)
    print('\n  ③ chi^2 at each path\'s own best normalisation: 70\'s binning %.6f, this seat\'s '
          '%.6f\n     (difference %.3e); the amplitudes differ by %.3e relative'
          % (c70, c60, abs(c60 - c70), abs(a60 / a70 - 1.0)))
    out['chi2'] = dict(seventy=c70, sixty=c60, difference=abs(c60 - c70),
                       amp_seventy=a70, amp_sixty=a60,
                       amp_rel_difference=abs(a60 / a70 - 1.0))

    verdict = ('the interpolation is not the lensing half: the two binnings agree to %.3e '
               'relatively and %.3e of a bin error, and their chi^2 differ by %.3e'
               % (rel.max(), in_sigma.max(), abs(c60 - c70))) if in_sigma.max() < 0.05 else (
              'THE INTERPOLATION MATTERS: the two binnings differ by up to %.3e of a bin error, '
              'so r7848\'s lensing half must be re-read on the exact path' % in_sigma.max())
    out['verdict'] = verdict
    out['is_not_a_registered_arm'] = True
    out['why_it_was_run'] = ('r7848 reports that adding the lensing bandpowers made the control '
                            'worse; this rules out -- or in -- the only place this seat\'s '
                            'scoring path differs from the seat that banked the data')
    print('\n  => %s\n' % verdict)
    with io.open(os.path.join(_HERE, 'lensing_closure_vs_70.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote lensing_closure_vs_70.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
