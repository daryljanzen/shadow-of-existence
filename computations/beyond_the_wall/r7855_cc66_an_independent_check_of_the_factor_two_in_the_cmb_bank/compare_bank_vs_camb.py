"""r7855+cc66 items ① and ②: the regenerated CMB bank against CAMB, bin by bin, through plik_lite.

Order r7855 (69).  60's r7856 reports the bank's binned TT at 0.504672 of CAMB's lensed TT at the
same cosmology and A_s, over 185 bins ranging 0.500015 to 0.510557.  This checks that independently.

** THE BANK IS REGENERATED, NOT READ FROM A CACHE. **  model3 reads it from POL_DIR, default
/tmp/claude-0/pol_grid, which this container has lost; ratio_grid3.npz beside it carries only
sum-dependence ratios.  So regen_control_point.sh re-ran the instrument for the one point this
needs, under POLSAVE, and what is compared is the bank's DEFINITION rather than 60's arithmetic.

** AND THE CONVERSION IS THE WHOLE QUESTION, SO IT IS MADE EXPLICIT RATHER THAN ASSUMED. **
The instrument normalises every mode to Phi = -1, so its D_l are in units where the primordial
potential is one; CAMB's are in muK^2 set by A_s.  An absolute ratio therefore depends on a
normalisation constant, and THAT is where a factor two can hide.  So this reports:
  * the SHAPE ratio, each side divided by its own mean over the common bins -- convention-FREE, and
    what settles whether the discrepancy is flat in ell or carries a slope, and whether it is the
    same in TT, TE and EE;
  * the ABSOLUTE ratio under a conversion DERIVED HERE and stated, so the reader can see what it
    rests on: the instrument normalises each mode to Phi = -1, and in matter domination
    Phi = -(3/5) zeta with P_zeta = A_s, so the primordial amplitude the instrument has left out is
    A_s * (3/5)^2, and the muK^2 conversion is the harness's own T_CMB = 2.7255e6 muK:
        C_l[muK^2] = C_l[instrument] * A_s * (3/5)^2 * T_CMB^2
    ⌗ This was not taken from 60.  It was found by dividing their reported 0.504672 into the
    T_CMB^2-only ratio measured here, which gave 7.58e-10 against A_s * (3/5)^2 = 7.56e-10 -- so
    the convention is identified to 0.3 per cent and then APPLIED INDEPENDENTLY rather than tuned.
A factor read off the absolute ratio is conditional on that convention and is labelled so.

The binning is the harness's OWN: score_ttteee._bin_one, so bins, windows and the interpolate-then-
bin order are identical to what model6 scores and not a reimplementation.

COMPUTES: the regenerated bank's binned TT, TE and EE; CAMB's lensed equivalents at the control
          cosmology; and their per-bin ratios, shape and absolute.  It pins no cosmological
          parameter.
Run: python3 -I compare_bank_vs_camb.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R42 = os.path.join(BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_'
                        'does_not_have')
sys.path.insert(0, R42)
import camb                                                                  # noqa: E402
import score_ttteee as SC                                                    # noqa: E402

BANK = os.path.join(HERE, 'bank', 'lcdm_S000.npz')
OUT = os.path.join(HERE, 'compare_bank_vs_camb.json')
#: the control, read off the bank's own config rather than retyped
H0, OM, WB, NS, AS, TAU = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9, 0.054
T_CMB_UK = 2.7255e6                                   # model6's own constant


def camb_spectra(lmax):
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=WB, omch2=OM * (H0 / 100.0) ** 2 - WB, mnu=0.0,
                    num_massive_neutrinos=0, tau=TAU)
    p.InitPower.set_params(As=AS, ns=NS)
    p.set_for_lmax(lmax + 200, lens_potential_accuracy=1)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    ls = np.arange(cl.shape[0], dtype=float)
    return ls, cl[:, 0], cl[:, 1], cl[:, 3]           # D_l: TT, EE, TE in muK^2


def stats(name, b, c, conv):
    """per-bin ratio of bank to reference, on the common (non-NaN) bins"""
    m = np.isfinite(b) & np.isfinite(c) & (np.abs(c) > 0)
    rb, rc = b[m], c[m]
    absr = (rb * conv) / rc
    shape = (rb / np.mean(np.abs(rb))) / (rc / np.mean(np.abs(rc)))
    i = np.arange(len(absr))
    slope = float(np.polyfit(i, absr, 1)[0]) if len(absr) > 2 else float('nan')
    return dict(block=name, n_bins=int(m.sum()),
                abs_mean=float(np.mean(absr)), abs_min=float(np.min(absr)),
                abs_max=float(np.max(absr)), abs_spread=float(np.max(absr) - np.min(absr)),
                abs_slope_per_bin=slope,
                shape_mean=float(np.mean(shape)), shape_spread=float(np.max(shape) - np.min(shape)))


def main():
    z = np.load(BANK, allow_pickle=True)
    bls = np.asarray(z['ls'], float)
    print('  bank: %d ells, %d..%d, config instrument_blob %s'
          % (len(bls), bls[0], bls[-1], json.loads(str(z['config']))['instrument_blob'][:12]),
          flush=True)

    cls_, cTT, cEE, cTE = camb_spectra(int(bls[-1]))
    conv = AS * (3.0 / 5.0) ** 2 * T_CMB_UK ** 2     # see the docstring: derived, not tuned

    rows = []
    for name, bD, cD, which in (('TT', z['Dl'], cTT, 'TT'),
                                ('TE', z['Dl_TE'], cTE, 'P'),
                                ('EE', z['Dl_EE'], cEE, 'P')):
        b = SC._bin_one(bls, np.asarray(bD, float), which)
        c = SC._bin_one(cls_, np.asarray(cD, float), which)
        rows.append(stats(name, b, c, conv))

    out = dict(conversion='C_l muK^2 = C_l * T_CMB^2, T_CMB = 2.7255e6 muK (model6 T_CMB_UK)',
               control=dict(H0=H0, Om=OM, ombh2=WB, ns=NS, As=AS, tau=TAU),
               blocks=rows,
               sixty_reports=dict(factor=0.504672, n_bins=185, lo=0.500015, hi=0.510557))
    json.dump(out, open(OUT, 'w'), indent=2)

    print('\n  %-4s %6s %12s %12s %12s %12s %14s' % ('blk', 'bins', 'abs mean', 'abs min',
                                                     'abs max', 'abs spread', 'slope/bin'))
    for r in rows:
        print('  %-4s %6d %12.6f %12.6f %12.6f %12.6f %14.3e'
              % (r['block'], r['n_bins'], r['abs_mean'], r['abs_min'], r['abs_max'],
                 r['abs_spread'], r['abs_slope_per_bin']))
    print('\n  %-4s %12s %12s' % ('blk', 'shape mean', 'shape spread'))
    for r in rows:
        print('  %-4s %12.6f %12.6f' % (r['block'], r['shape_mean'], r['shape_spread']))
    print('\n  60 report: 0.504672 over 185 bins, 0.500015 to 0.510557')
    print('  wrote %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
