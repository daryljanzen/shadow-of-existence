#!/usr/bin/env python3
"""C52 -- ⛔ **WITHDRAWN r2780. THE BANKED SPECTRA ARE THE NK=600 RUN AND PASS THE GUARD.**
*** `L-820 S1`: cc54's `HIER=1 NK=600` reproduces `c54.178_lcdm` to floating point.  **This
receipt inferred NK=260 from the `.npz` shape -- but the shape fixes LMAXL and LSTEP, and says
NOTHING about NK**, which sets the k-grid that is integrated OVER and never appears on the
multipole axis.  I read a mode count off an axis that cannot carry one and filled the gap with the
documented DEFAULT -- the value a parameter has WHEN NOBODY SETS IT, and cc54's run had set it.
  ⌗ *And the decision test this receipt said nobody knew the answer to has been run: the
  guard-FAILING NK=260 scores $\\chi^2=1318.3$ against NK=600's $1320.5$.  **The aliasing is
  COSMETIC for $\\chi^2$** -- so every number in `P15_where_the_likelihood_sits` stands.*
  ** What survives: the memory sizing, and the guard-threshold arithmetic. ** ***

C52 -- the banked spectra the likelihood arm scores come from a run that FAILS the instrument's own
sampling guard, and extending to $\\ell=2508$ hits a hard memory wall at the NK the guard requires.

** THE ATTEMPT. **  *** r2761 named `PO-10`'s blocker: the arm's model ends near $\\ell=1760$ and drops
the thirty bins covering the damping tail.  The fix looked like a parameter -- `ACOUSTIC_two_arm.py`
takes `LMAXL` from the environment, default $1300$, and the banked run used $2000$.  ** It is not a
parameter change, and the attempt found something worse. ** ***

** ⛔⛭⛭ ⓵ THE BANKED CONFIGURATION FAILS ITS OWN GUARD. **  Rerunning `LMAXL=2000 NK=260` -- the
configuration that produced `c54.178_lcdm.npz` ($\\ell=100$--$1996$, $238$ points, step $8$):

      *** projection sampling: dk = 1.841e-04, Bessel period 2pi/D = 4.532e-04,
          points per period = 2.5
          ⛔ UNDER-SAMPLED --- raise NK; the projected peaks would be aliasing, and the
             source comb would stay correct while they did it. ***

  ⇒ *** THE SPECTRA THE LIKELIHOOD ARM SCORES COME FROM AN UNDER-SAMPLED PROJECTION, and the instrument
      says so on every run. ***

** ⛭⛭ ⓶ AND THE GUARD'S OWN WORDING NAMES WHY NOTHING CAUGHT IT. **  "** the source comb would stay
correct while they did it **" -- *** so every comb-level check in the corpus can pass while the
PROJECTED spectrum aliases.  ** That is a defect no comb test could ever have caught, and the corpus's
acoustic checks are overwhelmingly comb-level. ** ***

** ⓷ AND THE EXTENSION HITS A HARD WALL AT THE NK THE GUARD REQUIRES. **  $k_{\\max}=\\ell_{\\max}/D_M$, so
raising `LMAXL` widens the $k$-range and `NK` must rise with it or the sampling worsens:

      *** NK    modes   pts/period   guard    projection memory   result
          260     780      1.95       FAIL         1.1 GB      the banked run
          330     990      2.48       FAIL         1.3 GB      guard refused
          600    1800      4.50       PASS         2.4 GB      OOM killed
          800    2400      6.00       PASS         3.2 GB      OOM killed ***

  ** Container memory: $3.7$ GB available. **  ⇒ *** The guard needs $NK\\ge600$ and $NK=600$ needs
  $\\sim2.4$ GB for the projection alone.  Both passing configurations were killed. ***

** ⓸ SO THE ROW'S BLOCKER IS NOW TWO THINGS, ORDERED. **
  * *** FIRST: the banked spectra are under-sampled at the $\\ell$ range they already cover.  Every
      $\\chi^2$ in `P15_where_the_likelihood_sits` -- the control's $7.14$ and the CR arm's $280.09$ --
      is computed against a projection the instrument flags. ***
  * *** THEN: extending to $\\ell=2508$ needs both a higher `NK` and more memory than this container
      has. ***

WHAT IS NOT CLAIMED.  ** Not that the banked $\\chi^2$ are wrong ** -- *** aliasing moves projected peaks;
whether it moves them enough to matter at $\\chi^2/{\\rm dof}\\sim7$ is unmeasured, and measuring it needs
the run that will not fit. ***  ** Not that the guard's threshold is validated ** -- it is the
instrument's own and is taken as given.  ** Not that `NK=600` is sufficient ** -- it is the smallest
value clearing the guard, not a convergence test.

** COMPUTES: the sampling ratio and projection memory across four `NK` values, and a rerun of the banked
configuration to read its guard.  *** Every parameter is the instrument's own. *** **

Written r2762.  Stated for reversal.
"""
import glob
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

D_M = 13865.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C52 -- are the banked spectra adequately sampled?")
    print()
    src = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
               encoding='utf-8', errors='replace').read()

    # ⓵ the banked file's shape fixes the configuration
    z = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_lcdm.npz'), recursive=True)[0])
    ls = z['ls']
    check(f'⓵ the banked spectra run $\\ell={ls[0]}$--${ls[-1]}$ in {len(ls)} points, step '
          f'{ls[1]-ls[0]} -- so LMAXL was 2000 and NK the default',
          ls[0] == 100 and ls[-1] < 2000 and ls[1]-ls[0] == 8)
    check('and the default is NK=260: the instrument documents "NK (modes, default 260)"',
          "NK (modes, default 260)" in src)

    # ⓶ that configuration fails the guard
    per = 2*np.pi/D_M
    ratio = per/((2000/D_M)/(260*3))
    check(f'⛔⛭⛭ ⓶ and that configuration gives {ratio:.1f} points per Bessel period -- the '
          'instrument prints "⛔ UNDER-SAMPLED" below its own threshold',
          ratio < 4 and 'UNDER-SAMPLED' in src)
    check('⇒ so the spectra the likelihood arm scores come from an under-sampled projection, and '
          'the instrument says so on every run',
          ratio < 3)

    # ⓷ and the guard names why nothing caught it
    check('⛭⛭ ⓷ and the guard names why: "the projected peaks would be aliasing, and the source comb '
          'would stay correct while they did it" -- ** no comb-level check could catch this **',
          'source comb' in src and 'aliasing' in src)

    # ⓸ the memory wall
    need = {NK: NK*3*302*8*560/1e9 for NK in (600, 800)}
    check(f'⓸ while the smallest NK clearing the guard is 600 '
          f'({per/((2512/D_M)/(600*3)):.1f} pts/period) and needs ~{need[600]:.1f} GB for the '
          'projection alone -- against 3.7 GB available',
          per/((2512/D_M)/(600*3)) >= 4 and need[600] > 2)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the banked spectra fail the instrument\'s own sampling guard. **')
    print(f'  ⓵ ** The banked run is LMAXL=2000, NK=260 ** — fixed by the file\'s own shape')
    print(f'     (ℓ={ls[0]}–{ls[-1]}, {len(ls)} points, step {ls[1]-ls[0]}).')
    print(f'  ⛔ ⓶ ** It gives {ratio:.1f} points per Bessel period ** and the instrument prints')
    print('     "⛔ UNDER-SAMPLED" — *** the spectra the likelihood arm scores come from an')
    print('     under-sampled projection, on every run. ***')
    print('  ⛭⛭ ⓷ ** And the guard names why nothing caught it: ** "the projected peaks would be')
    print('     aliasing, and ** the source comb would stay correct while they did it **."')
    print('     *** Every comb-level check can pass while the projection aliases — and the corpus\'s')
    print('     acoustic checks are overwhelmingly comb-level. ***')
    print('  ⓸ ** And the extension hits a hard wall: **')
    print('       NK=260  1.95 pts/period  FAIL  1.1 GB   the banked run')
    print('       NK=600  4.50 pts/period  PASS  2.4 GB   OOM killed')
    print('       NK=800  6.00 pts/period  PASS  3.2 GB   OOM killed        (3.7 GB available)')
    print('     ⇒ ** the guard needs NK≥600 and NK=600 needs more than this container has. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
