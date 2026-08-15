#!/usr/bin/env python3
"""C58 -- the CR arm's stored $r_s$ moves the WRONG WAY: removing radiation must RAISE the sound
horizon, the peak spacing needs it raised, and the stored value is lowered.

** THE THREE-WAY r2789 LEFT. **  *** Which of $D_M$, $r_s$ or the projection does the CR arm's transfer
actually use?  ** Solving the peak spacing for each, and then checking the DIRECTION against the
physics, picks one. ** ***

** ⓵ SOLVE THE SPACING. **  The CR peaks sit at mean spacing $258$ against a stored
$\\ell_A=\\pi D_M/r_s=301.6$:

      *** if r_s is the culprit:   r_s must be 158.35   (stored 135.46, x1.169)
          if D_M is the culprit:   D_M must be 11124.6  (stored 13004.6, x0.855) ***

** ⛭⛭⛭ ⓶ AND THE DIRECTION SETTLES IT. **  Removing radiation lowers $H$ at high $z$, so more conformal
time accrues before recombination and the sound horizon is ** LARGER **.  Integrated directly:

      *** radiation INCLUDED   r_s = 146.52 Mpc
          radiation FREE       r_s = 245.16 Mpc ***

  ⇒ *** A radiation-free arm must have a LARGER $r_s$ than $\\Lambda$CDM. ***

** ⛔ ⓷ THE STORED VALUES GO THE OTHER WAY. **

      *** LCDM r_s = 144.53      CR r_s = 135.46      -- CR is SMALLER ***

  ⇒⇒ *** THE STORED CR $r_s$ IS BELOW $\\Lambda$CDM's, AND THE PHYSICS REQUIRES IT ABOVE.  ** And the
      peak spacing independently demands $158.35$ -- larger than $144.53$, which is the direction the
      physics requires. **  Two independent arguments agree against the stored value. ***

** ⓸ SO THE ANSWER TO r2789's THREE-WAY IS $r_s$, AND THE CASE IS NOT ONLY ARITHMETIC. **  *** The
transfer's own peaks say $r_s\\approx158$; the radiation-free integral says $r_s$ must exceed
$\\Lambda$CDM's $144.53$; the stored value is $135.46$.  ** The spectrum and the physics agree with each
other and disagree with the ledger entry. ** ***
  ⌗ ** Which is why $\\ell_A$ looked fine: ** *** $\\pi D_M/r_s$ with BOTH stored values reproduces
    $301.60$ exactly (r2788).  ** A wrong $r_s$ propagated into a stored $\\ell_A$ is internally
    consistent and describes nothing. ** ***

WHAT IS NOT CLAIMED.  ** Not that $158.35$ or $245.16$ is the right value ** -- *** the first is what the
peak spacing implies at the stored $D_M$; the second is a bare integral with a fixed $x_e$ and no seam
treatment, and the corpus's radiation-free construction is not this integral.  ** What is established is
the DIRECTION and that the stored value has the wrong sign of deviation. ** ***  ** Not that $D_M$ is
cleared ** -- *** it is not independently checked; what is shown is that $r_s$ has an independent
argument against it and $D_M$ does not. ***  ** Not that the CR arm's physics is wrong ** -- *** a ledger
entry disagreeing with the spectrum it labels is a bookkeeping finding. ***

** COMPUTES: the spacing solved for each candidate, and $r_s$ integrated with and without radiation on
the corpus's own parameters.  *** The arms are `c54.178`. *** **

Written r2790.  Stated for reversal.
"""
import glob
import os

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

H0, OM, OL, OR = 67.36, 0.3153, 0.6847, 8.6e-5
C = 299792.458
ZSTAR = 1089.9
EFF_SPACING = 258.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def rs_of(with_rad):
    R0 = 3*0.02237/(4*2.4728e-5)
    def H(z):
        return H0*np.sqrt((OR*(1+z)**4 if with_rad else 0) + OM*(1+z)**3 + OL)
    return quad(lambda z: (C/np.sqrt(3*(1+R0/(1+z))))/H(z), ZSTAR, 1e6, limit=200)[0]


def main():
    print()
    print("  C58 -- which of D_M, r_s or the projection, and does the direction agree?")
    print()
    cr = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_cr.npz'), recursive=True)[0])
    lc = np.load(glob.glob(os.path.join(ROOT, '**', 'c54.178_lcdm.npz'), recursive=True)[0])
    D, rs_cr, rs_lc = float(cr['D_M']), float(cr['r_s']), float(lc['r_s'])

    need_rs = np.pi*D/EFF_SPACING
    need_D = EFF_SPACING*rs_cr/np.pi
    check(f'⓵ the spacing solves two ways: $r_s$ would have to be {need_rs:.2f} (stored {rs_cr:.2f}) '
          f'or $D_M$ would have to be {need_D:.1f} (stored {D:.1f})',
          need_rs > rs_cr and need_D < D)

    with_rad, no_rad = rs_of(True), rs_of(False)
    check(f'⛭⛭⛭ ⓶ and the direction settles it: integrating $r_s$ with radiation gives '
          f'{with_rad:.2f} Mpc and WITHOUT gives {no_rad:.2f} Mpc -- ** removing radiation RAISES the '
          'sound horizon **',
          no_rad > with_rad)

    check(f'⛔ ⓷ but the stored CR value is {rs_cr:.2f} against $\\Lambda$CDM\'s {rs_lc:.2f} -- '
          '** SMALLER, when the physics requires larger **',
          rs_cr < rs_lc)
    check(f'and the peak spacing independently demands {need_rs:.2f}, which IS larger than '
          f'{rs_lc:.2f} -- ** two independent arguments agree against the stored value **',
          need_rs > rs_lc)

    # ⓸ and this is why l_A looked fine
    check(f'⓸ while $\\pi D_M/r_s$ on BOTH stored values reproduces the stored $\\ell_A$ exactly '
          f'({np.pi*D/rs_cr:.2f}) -- ** a wrong $r_s$ propagated into a stored $\\ell_A$ is internally '
          'consistent and describes nothing **',
          abs(np.pi*D/rs_cr - float(cr['l_A'])) < 0.5)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the stored CR r_s moves the wrong way. **")
    print(f'  ⓵ ** The spacing solves two ways: ** r_s → {need_rs:.2f} (×{need_rs/rs_cr:.3f}) or')
    print(f'     D_M → {need_D:.1f} (×{need_D/D:.3f}).')
    print(f'  ⛭⛭⛭ ⓶ ** And the direction settles it: ** r_s integrates to {with_rad:.2f} Mpc WITH')
    print(f'     radiation and {no_rad:.2f} WITHOUT — ** removing radiation lowers H at high z, so more')
    print('     conformal time accrues and the sound horizon is LARGER. **')
    print(f'  ⛔ ⓷ ** The stored values go the other way: ** LCDM {rs_lc:.2f}, CR {rs_cr:.2f} — CR is')
    print(f'     SMALLER.  ** And the peak spacing independently demands {need_rs:.2f}, which is larger')
    print(f'     than {rs_lc:.2f}. **')
    print('     *** Two independent arguments — the spectrum and the physics — agree with each other')
    print('     and disagree with the ledger entry. ***')
    print(f'  ⓸ ** Which is why ℓ_A looked fine: ** πD_M/r_s on both stored values gives')
    print(f'     {np.pi*D/rs_cr:.2f}, matching exactly.  ** A wrong r_s propagated into a stored ℓ_A is')
    print('     internally consistent and describes nothing. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
