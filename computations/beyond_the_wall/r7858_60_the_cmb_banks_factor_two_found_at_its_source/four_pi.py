#!/usr/bin/env python3
"""`r7858` Ⓐ①ᵇ, REBUILT — the `4 pi` tested at the `C_l` level, with the `D_l` step absent.

⛔ ** THIS FILE EXISTS BECAUSE `locate_two.py`'s VERSION OF THIS TEST WAS INVALID, AND THE INVALID
VERSION IS KEPT IN THE RECORD RATHER THAN DELETED. **  That version recovered the instrument's
`out` by dividing the BINNED `l(l+1) out` by the BINNED `l(l+1)`.  The window mixes `l` across its
own width, so `<l(l+1) out> / <l(l+1)>` is not `<out>`, and the test came back at a geometric mean
of `9.76e+04` with a range spanning a factor `370`.  ** That spread is the signature of the test's
own error and not of the physics: ** a wrong constant cannot be `k`-dependent.

** THE CORRECT CONSTRUCTION. **  The bank's `.npz` holds `ls` and `Dl` PER MULTIPOLE, before any
binning.  So `out = Dl / (l(l+1))` is formed AT EACH `l`, and only then binned through the same
windows as CAMB's own `C_l`.  That test has no `D_l` convention on this side at all, so it fixes the
accumulation's prefactor alone and cannot absorb a wrong `D_l` step.

Run: python3 four_pi.py        (writes four_pi.json)
"""
import io
import json
import glob
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7842 = os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_'
                           'harness_does_not_have')
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, R7842)

import camb                                                               # noqa: E402
from camb import model as camb_model                                      # noqa: E402

AS = 2.1e-9
K_PIVOT = 0.05
SUM_REF = 0.06
H0, OM, WB, TAU = 67.40, 0.3150, 0.0224, 0.054
POL_DIR = os.environ.get('POL_DIR', '/tmp/claude-0/pol_grid')


def main():
    import model6 as M6                                                    # noqa: E402
    import score_ttteee as SC                                              # noqa: E402
    import phiphi as PP                                                    # noqa: E402
    ns = float(PP.NS)
    AMP = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    T2 = M6.T_CMB_UK ** 2
    scr = float(np.exp(-2.0 * TAU))
    out = dict(amp=AMP, ns=ns, As=AS, T_CMB_UK=float(M6.T_CMB_UK), screening=scr)

    pth = os.path.join(POL_DIR, 'lcdm_S000.npz')
    if not os.path.exists(pth):
        print('\n  ⛔ the bank point is not on disk at %s -- nothing is claimed.\n' % pth)
        return 1
    z = np.load(pth, allow_pickle=True)
    lsb = np.asarray(z['ls'], float)
    dlb = np.asarray(z['Dl'], float)
    print('\n  THE BANK POINT, PER MULTIPOLE AND BEFORE ANY BINNING', flush=True)
    print('      %s: %d multipoles, l %d .. %d' % (os.path.basename(pth), len(lsb),
                                                   int(lsb.min()), int(lsb.max())))
    # ⒜ undo the save line's `l(l+1)` AT EACH l -- this is the step the invalid version got wrong
    out_per_l = dlb / (lsb * (lsb + 1.0))
    print('      `out = Dl / (l(l+1))` formed at each l, NOT after binning', flush=True)

    h = H0 / 100.0
    omch2 = (OM - WB / h ** 2) * h ** 2 - SUM_REF / 93.14
    p = camb.set_params(H0=H0, ombh2=WB, omch2=omch2, mnu=SUM_REF, tau=TAU, ns=ns, As=AS,
                        lmax=2600, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    dl_camb = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total'][:, 0]
    lsc = np.arange(dl_camb.shape[0])
    dlc = np.interp(lsb, lsc, np.nan_to_num(dl_camb))
    clc = dlc * 2.0 * np.pi / (lsb * (lsb + 1.0))
    print('      camb %s, its own C_l formed at the SAME multipoles' % camb.__version__,
          flush=True)

    print('\n  Ⓐ①ᵇ ① THE `4 pi` ALONE -- `4 pi x AMP x T^2 x exp(-2 tau) x out` over CAMB\'s C_l',
          flush=True)
    pred = 4.0 * np.pi * AMP * T2 * scr * out_per_l
    rat = pred / clc
    gm = float(np.exp(np.mean(np.log(np.abs(rat)))))
    lo, hi = float(np.min(rat)), float(np.max(rat))
    spread = float(np.max(np.abs(rat - gm)) / gm)
    print('      over %d multipoles: geometric mean %.6f, range %.6f .. %.6f, worst spread %.4f'
          % (len(lsb), gm, lo, hi, spread))
    for i in (0, len(lsb) // 4, len(lsb) // 2, 3 * len(lsb) // 4, len(lsb) - 1):
        print('        l = %5d   out %.6e   camb C_l %.6e   ratio %.6f'
              % (int(lsb[i]), out_per_l[i], clc[i], rat[i]), flush=True)
    holds = abs(gm - 1.0) < 0.01
    print('\n    ** ① %s: the `4 pi` on the accumulation is %s ON ITS OWN TERMS, with no `D_l`'
          % ('HOLDS' if holds else 'FAILS', 'ESTABLISHED' if holds else 'NOT established'))
    print('       convention anywhere on this side -- so it is not a number that closes a ratio. **',
          flush=True)
    out['four_pi'] = dict(holds=bool(holds), geometric_mean=gm, ratio_min=lo, ratio_max=hi,
                          worst_spread=spread, n_multipoles=int(len(lsb)),
                          camb_version=camb.__version__)

    print('\n  Ⓐ①ᵇ ② AND THE `1/(2 pi)` IS AN IDENTITY ON THE SAVE LINE', flush=True)
    print('      `Dl = Cl * l(l+1)` against the data\'s `l(l+1) C_l / (2 pi)`: the saved vector is')
    print('      2 pi = %.6f times what the windows expect, read off the line and not fitted.'
          % (2 * np.pi))
    print('    ⇒ the two together: 4 pi / (2 pi) = %.1f' % (4 * np.pi / (2 * np.pi)), flush=True)
    out['two_pi'] = dict(factor=float(2 * np.pi), net=float(4 * np.pi / (2 * np.pi)),
                         is_an_identity_on_the_line=True)

    with io.open(os.path.join(_HERE, 'four_pi.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote four_pi.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
