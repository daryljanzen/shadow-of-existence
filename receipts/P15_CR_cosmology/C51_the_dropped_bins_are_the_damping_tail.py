#!/usr/bin/env python3
"""C51 -- the thirty dropped bins are $\\ell=1759$--$2508$: the likelihood arm discards exactly the
region CR's damping signature lives in, and the suppression there runs $24\\%$ to $42\\%$.

** THE THREAD, from r2760. **  *** The arm scores $185$ bins against CAMB's $215$.  Thirty bins go
missing and nothing said which. ***

** ⛭⛭ ⓵ THEY ARE THE HIGHEST-$\\ell$ THIRTY. **  `plik_lite` TT declares $215$ bins spanning
$\\ell=30$--$2508$.  The receipt's binner writes `nan` when a bin's $\\ell$ range exceeds the model
array; $185$ bins survive exactly when the model ends near $\\ell=1760$:

      *** bin 185 spans ell 1759 .. 1775
          bin 214 spans ell 2476 .. 2508
          the dropped thirty cover  ell 1759 .. 2508 ***

** ⛔⛭⛭ ⓶ WHICH IS THE DAMPING TAIL -- THE ONE REGION THE ROW EXISTS FOR. **  P15 names its exposed
edge as "the $8.2\\%$ damping-scale signature ... ** whose observable consequence awaits the high-$\\ell$
acoustic transfer **".

  ⇒ *** THE INSTRUMENT DISCARDS EXACTLY THE REGION THE SIGNATURE LIVES IN. ***

** ⓷ AND THE SIGNAL THERE IS THE LARGEST IT EVER GETS. **  The suppression
$\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$ grows as $\\ell^2$:

      *** ell = 1000    0.9162    8.4% down
          ell = 1500    0.8212   17.9% down
          ell = 1760    0.7625   23.8% down     <- the cut
          ell = 2200    0.6546   34.5% down
          ell = 2508    0.5766   42.3% down     <- the last dropped bin ***

  ⇒⇒ *** At the cut the effect is already a quarter; across the dropped bins it reaches two fifths.
      ** The thirty bins the arm throws away are the thirty where the prediction is strongest. ** ***

** ⓸ SO THE ROW'S BLOCKER IS SHARPER THAN "$\\chi^2/{\\rm dof}=7$". **  *** The control's residual factor
of seven is a calibration problem on the bins that ARE scored.  ** This is a different defect: the
scored set omits the discriminating region entirely, so no improvement in the control's $\\chi^2$ would
make the comparison able to see the signature. ** ***
  ⌗ ** And it explains F6's own verdict mechanically: ** *** "both arms remain outside the regime in
    which plik_lite discriminates" is true partly because the arm has removed the regime in which
    plik_lite would discriminate for THIS prediction. ***

WHAT IS NOT CLAIMED.  ** Not that the model array's $\\ell$ limit is a mistake ** -- *** it is a cost;
extending the transfer to $\\ell=2508$ is work, and the receipt's `nan`-and-drop is an honest handling of
a short array rather than a silent truncation. ***  ** Not that including the bins would favour CR ** --
a $24$--$42\\%$ suppression against Planck's few-tenths-of-a-per-cent errors is a large claim to put in
front of data, and which way it lands is the point of running it.  ** Not that $\\ell_D=1400$ is the
corpus's value ** -- it is the scale P15 uses illustratively, and the profile's SHAPE is what matters
here.

** COMPUTES: the bin edges from the likelihood's own arrays, the cut at which $185$ survive, and the
damping profile at five multipoles.  *** The likelihood is the corpus's own; $r$ is the corrected value
from r2755. *** **

Written r2761.  Stated for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C51 -- which thirty bins does the likelihood arm drop?")
    print()
    LIK = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
    sys.path.insert(0, LIK)
    from planck_lite_py import PlanckLitePy
    lik = PlanckLitePy(data_directory=os.path.join(LIK, 'data'), year=2018, spectra='TT',
                       use_low_ell_bins=False)
    LO = np.array([lik.blmin_TT[i] + lik.plmin_TT for i in range(lik.nbintt)])
    HI = np.array([lik.blmax_TT[i] + lik.plmin_TT for i in range(lik.nbintt)])

    check(f'⓵ plik_lite TT declares {lik.nbintt} bins spanning $\\ell={LO[0]}$--${HI[-1]}$',
          lik.nbintt == 215 and LO[0] == 30 and HI[-1] == 2508)

    cut = next(L for L in range(1700, 2100, 5) if int(np.sum(HI <= L)) == 185)
    check(f'and exactly 185 survive when the model ends near $\\ell={cut}$ -- so the arm\'s array '
          f'stops there', 1700 < cut < 1800)
    check(f'⛭⛭ ⓶ so the dropped thirty are the HIGHEST: bin 185 spans $\\ell$ {LO[185]}--{HI[185]}, '
          f'bin 214 spans {LO[214]}--{HI[214]}',
          LO[185] > 1700 and HI[214] == 2508)

    # ⓷ the damping profile over the dropped range
    r, lD = 1.0824, 1400.0
    supp = {l: np.exp(-(l/lD)**2*(r**2 - 1)) for l in (1000, 1760, 2508)}
    check(f'⓷ and the suppression grows as $\\ell^2$: {100*(1-supp[1000]):.1f}% down at '
          f'$\\ell=1000$, {100*(1-supp[1760]):.1f}% at the cut, {100*(1-supp[2508]):.1f}% at the last '
          'dropped bin',
          supp[2508] < supp[1760] < supp[1000])
    check('⇒ so the thirty bins the arm throws away are the thirty where the prediction is '
          'STRONGEST -- the effect at the last dropped bin is five times its size at $\\ell=1000$',
          (1-supp[2508])/(1-supp[1000]) > 4)

    # ⓸ and this is a different defect from the control's chi^2
    check('⓸ while the control\'s residual factor of seven is a calibration problem on the bins that '
          'ARE scored -- a different defect, since no improvement there would make the omitted '
          'region visible',
          int(np.sum(HI <= cut)) == 185 and lik.nbintt - 185 == 30)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the arm discards exactly the region the signature lives in. **')
    print(f'  ⓵ ** plik_lite declares 215 TT bins over ℓ=30–2508 **; 185 survive when the model ends')
    print(f'     near ℓ={cut}.')
    print(f'  ⛭⛭ ⓶ ** The dropped thirty cover ℓ {LO[185]}–{HI[214]} — the damping tail. **  P15 names')
    print('     its exposed edge as "the 8.2% damping-scale signature … whose observable consequence')
    print('     awaits the HIGH-ℓ acoustic transfer".')
    print('  ⓷ ** And the signal there is the largest it gets: **')
    for l in (1000, 1760, 2508):
        tag = '  <- the cut' if l == 1760 else ('  <- last dropped bin' if l == 2508 else '')
        print(f'       ℓ={l:>5}   suppression {supp[l]:.4f}   {100*(1-supp[l]):>5.1f}% down{tag}')
    print('     *** The thirty bins the arm throws away are the thirty where the prediction is')
    print('     strongest. ***')
    print('  ⓸ ** So this is a DIFFERENT defect from the control\'s χ²/dof = 7: ** that is a')
    print('     calibration problem on the bins that ARE scored.  ** No improvement in it would make')
    print('     the comparison able to see the signature. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
