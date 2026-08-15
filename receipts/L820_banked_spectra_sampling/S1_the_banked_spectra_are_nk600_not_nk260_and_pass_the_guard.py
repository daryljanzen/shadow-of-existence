#!/usr/bin/env python3
r"""S1 -- cc54 ran 56's routed resampling task (r2762) and it answers BOTH halves the same way: the banked
two-arm spectra the likelihood scores are NOT under-sampled, AND even the guard-failing sampling does not
move the chi^2. (i) PROVENANCE: the banked file is NK=600 (the README's own command), which passes the
projection guard at 5.7 points per Bessel period; cc54 (15 GB) reproduced c54.178_lcdm.npz BIT-FOR-BIT
(max |dDl| = 8e-16). (ii) ROBUSTNESS -- 56's own decision test: rerun at the guard-FAILING NK=260 and score
it; chi^2 goes 1320.5 -> 1318.3 (0.17%), so the aliasing is COSMETIC for the likelihood even though the
projected spectrum visibly aliases (21.7% at a peak). 56 posed exactly this: "does the chi^2 move? If it
barely moves, the aliasing is cosmetic and PO-10's blocker is only the missing bins." It barely moves.

** WHY C52 READ IT AS NK=260, AND WHY THAT IS THE MISREAD. ** C52 inferred NK=260 from "the .npz shape
(ell=100-1996, 238 points, step 8)". But the 238 multipole points are set by LSTEP and LMAXL, not NK:
`ls = np.arange(100, int(LMAXL), int(LSTEP))` = `arange(100, 2000, 8)` = 238 points, for ANY NK. NK sets the
number of k-MODES (the projection sampling), not the number of ell-points (the output length). So the .npz
shape says nothing about NK. And 56's container is 3.7 GB, where NK=600 OOM-kills -- so C52 could not
regenerate the banked file and tested NK=260 (which fits), found it under-samples, and attached that to the
banked provenance. On a 15 GB node NK=600 runs and reproduces the banked file exactly.

** THE GUARD IS A FUNCTION OF NK, AND NK=600 PASSES IT. ** With `kk = linspace(12, LMAXL, 3*NK)/D_M` the
median spacing is (LMAXL-12)/((3*NK-1)*D_M), so points-per-period = 2*pi*(3*NK-1)/(LMAXL-12):
    NK=260 -> 2.46  (FAILS; matches C52's reported 2.5)
    NK=600 -> 5.69  (PASSES; matches the run's reported 5.7)

COMPUTES: the guard points-per-period as a function of NK (evaluated at NK=260 and NK=600 to bracket the
threshold), and the chi^2 of the banked (NK=600) and a guard-failing (NK=260) reproduction. ** NK=260 and
NK=600 are the guard's failing/passing sides and the banked provenance, not a single pinned working point;
LMAXL=2000 is the banked run's value. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE SHAPE IS LSTEP/LMAXL, NOT NK: the banked c54.178_lcdm carries exactly arange(100, 2000, 8) = 238
     multipoles, reproducible from LSTEP=8 and LMAXL=2000 with no reference to NK.
  2. THE GUARD PASSES AT NK=600: points-per-period = 2*pi*(3*NK-1)/(LMAXL-12) gives 2.46 at NK=260 (fails,
     = C52's 2.5) and 5.69 at NK=600 (passes, = the run's 5.7).
  3. THE BANKED FILE IS THE NK=600 RUN: cc54's HIER=1 BSPLIT=1 ETAEND=4000 KBATCH=300 NK=600 LMAXL=2000
     reproduces c54.178_lcdm.npz to floating point (max |dDl| < 1e-12), banked as
     L820_lcdm_nk600_reproduces_c54.178.npz -- so the banked provenance is NK=600, on the passing side.
  4. THE ALIASING IS COSMETIC FOR chi^2 (56's decision test): the guard-FAILING NK=260 reproduction
     (banked L820_lcdm_nk260_guardfail.npz) scores chi^2 = 1318.3 against the NK=600 file's 1320.5 -- a
     0.17% shift -- even though the projected spectrum aliases by up to 21.7% at a peak. So the chi^2 barely
     moves; the aliasing is cosmetic for the likelihood.
  5. THE VERDICT: the banked spectra are adequately sampled (NK=600) AND robust to sampling anyway; C52's
     "NK=260 produced the banked" is a shape-misread; the control's 7.14 and the CR arm's 280.09 stand, and
     PO-10's remaining blocker is C51's dropped bins, not the sampling.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that C52's guard is wrong -- it is right and NK=260
genuinely under-samples the SPECTRUM (21.7% at a peak); what is corrected is which NK the BANKED file used,
and the new fact is that the chi^2 is insensitive to it. NOT that the likelihood is settled -- C51's point
stands and is real: LMAXL=2000 drops the 30 damping-tail bins (ell 1759-2508), which no sampling fact
touches; the LMAXL=2512 extension is the genuine remaining run, banked separately. NOT a CR-arm discreteness
claim -- the CR ladder is checked elsewhere (c54.186 KCONT); this is the lcdm continuum provenance. NOT that
7.14 is a good fit -- it is the control's residual and is large; this only says it is not an aliasing
artefact.

** Board lead L-820 (cc54's band); corrects C52's sampling premise for the likelihood arm and runs 56's
decision test. Informs L-147 (PO-10). Clears the "banked is provisional on sampling" blocker so C51's
dropped-bin blocker is the one that remains. Companion: the LMAXL=2512 extension. **

Written r2674 (cc54, L-820). Asserts against the banked c54.178_lcdm.npz, the instrument's kk-grid and guard
arithmetic, and cc54's NK=600 (bit-for-bit) and NK=260 (guard-failing) reproductions -- never the register.
Stated for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def ppp(nk, lmaxl=2000):
    """points per Bessel period on the code's kk grid = 2*pi*(3*NK-1)/(LMAXL-12)."""
    return 2 * np.pi * (3 * nk - 1) / (lmaxl - 12)


def main():
    print()
    print('  S1 -- are the banked spectra under-sampled (C52), or NK=600 and robust to sampling anyway?')
    print()

    banked = np.load(os.path.join(SPEC, 'c54.178_lcdm.npz'))
    sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
    import chi2_of_spectrum as CS  # noqa: E402

    # 1. the shape is LSTEP/LMAXL, not NK
    check('THE SHAPE IS LSTEP/LMAXL, NOT NK: banked c54.178_lcdm has arange(100,2000,8) = 238 multipoles '
          f'(got {len(banked["ls"])}), from LSTEP=8 and LMAXL=2000 with no reference to NK',
          len(banked['ls']) == 238 and np.array_equal(banked['ls'], np.arange(100, 2000, 8)))

    # 2. the guard passes at NK=600, fails at NK=260
    p260, p600 = ppp(260), ppp(600)
    check(f'THE GUARD PASSES AT NK=600: points/period = 2pi(3NK-1)/(LMAXL-12) = {p260:.2f}@NK=260 '
          f'(FAILS<4, = C52\'s 2.5) and {p600:.2f}@NK=600 (PASSES>=4, = the run\'s 5.7)',
          p260 < 4.0 and p600 >= 4.0 and abs(p260 - 2.5) < 0.1 and abs(p600 - 5.7) < 0.1)

    # 3. the banked file IS the NK=600 run -- bit-for-bit reproduction
    repro = np.load(os.path.join(SPEC, 'L820_lcdm_nk600_reproduces_c54.178.npz'))
    max_dDl = float(np.max(np.abs(repro['Dl'] - banked['Dl'])))
    check('THE BANKED FILE IS THE NK=600 RUN: cc54\'s HIER=1 NK=600 reproduces c54.178_lcdm to floating '
          f'point (max |dDl| = {max_dDl:.1e} < 1e-12) -- banked provenance is NK=600, on the passing side',
          np.array_equal(repro['ls'], banked['ls']) and max_dDl < 1e-12)

    # 4. the aliasing is COSMETIC for chi^2 (56's decision test)
    nk260 = np.load(os.path.join(SPEC, 'L820_lcdm_nk260_guardfail.npz'))
    c260 = CS.chi2_of(nk260['ls'], nk260['Dl'])[0]
    c600 = CS.chi2_of(banked['ls'], banked['Dl'])[0]
    spec_alias = float(np.max(np.abs(nk260['Dl'] - banked['Dl']) / np.abs(banked['Dl'])))
    check(f'THE ALIASING IS COSMETIC FOR chi^2 (56\'s decision test): guard-FAILING NK=260 scores '
          f'{c260:.1f} vs NK=600\'s {c600:.1f} -- {abs(c260-c600)/c600*100:.2f}% -- while the projected '
          f'spectrum aliases {spec_alias*100:.0f}% at a peak. So chi^2 barely moves: the aliasing is '
          'cosmetic for the likelihood',
          abs(c260 - c600) / c600 < 0.01 and spec_alias > 0.1)

    # 5. verdict
    check('THE VERDICT: adequately sampled (NK=600) AND robust to sampling; C52\'s "NK=260 produced the '
          'banked" is a shape-misread; the 7.14 / 280.09 stand and PO-10\'s remaining blocker is C51\'s '
          'dropped bins, not the sampling',
          not FAILED)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (C52 corrected + 56\'s decision test run): the banked c54.178 spectra were produced at')
    print('  NK=600 -- the README\'s command -- which passes the guard at 5.7 pts/period, and cc54 reproduced')
    print('  c54.178_lcdm BIT-FOR-BIT. The 238-point shape C52 read as "NK=260" is set by LSTEP=8/LMAXL=2000,')
    print('  not NK; 56\'s 3.7 GB container OOM\'d at NK=600 and tested the guard-failing NK=260. AND the')
    print('  chi^2 barely moves under that guard-failing sampling (1320.5 -> 1318.3, 0.17%), so the aliasing')
    print('  is cosmetic for the likelihood: the 7.14 / 280.09 stand, and PO-10\'s blocker is C51\'s dropped')
    print('  damping-tail bins, which the LMAXL=2512 extension addresses.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
